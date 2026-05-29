# Chart Engine

Use `assets/lightweight-charts.standalone.production.js` for interactive stock price reports. The generated report still remains one offline HTML file: inline the chart engine, inline CSS, inline normalized data JSON, and inline the initialization script.

## Engine Asset

- Source package: `lightweight-charts@5.2.0`.
- Asset path: `assets/lightweight-charts.standalone.production.js`.
- License path: `assets/lightweight-charts.LICENSE`.
- Browser global: `window.LightweightCharts`.

When generating an HTML report, embed the standalone production bundle in a plain `<script>` block. Do not use `<script src>`, ESM imports, CDN URLs, remote stylesheets, remote fonts, or a development server.

The vendored asset keeps the upstream license file in the skill package. Generated reports must include TradingView attribution and a link as required by the `lightweight-charts` package README. This link is an attribution link, not a remote runtime dependency; the report must still render without network access.

## Series API

Use the v5 series API:

```js
const {
  createChart,
  CandlestickSeries,
  HistogramSeries,
  LineSeries,
} = window.LightweightCharts;

const chart = createChart(container, {
  ...options,
  layout: {
    ...options.layout,
    attributionLogo: false,
  },
});
const candles = chart.addSeries(CandlestickSeries, {
  upColor: "rgb(190, 74, 62)",
  downColor: "rgb(49, 132, 93)",
  borderVisible: false,
  wickUpColor: "rgb(190, 74, 62)",
  wickDownColor: "rgb(49, 132, 93)",
});

candles.setData(candlePoints);
```

Use `HistogramSeries` for volume and MACD histograms. Use `LineSeries` for MA, BOLL, DIF, DEA, K, D, J, and RSI lines.

Use `rgb()` or `rgba()` strings for chart-engine options. The report page CSS can use OKLCH, but `lightweight-charts` parses series colors internally and may reject OKLCH strings in current browsers.

## Pane Layout

P0 generated reports may use stacked chart instances for broad browser compatibility:

- Main chart: candlesticks, MA lines, optional BOLL bands.
- Volume chart: aligned histogram bars.
- MACD chart: histogram plus DIF and DEA lines.
- KDJ chart: K, D, and J lines when enough rows exist.

All stacked panes must behave as one chart:

- Synchronize the x-axis with `timeScale().subscribeVisibleLogicalRangeChange`, `getVisibleLogicalRange`, and `setVisibleLogicalRange`; do not rely on time-range synchronization alone.
- Keep one shared logical range for all panes. Apply updates both ways and avoid recursive updates with a boolean guard.
- Add a `clampVisibleLogicalRange(range)` helper before applying any range. Set `MIN_VISIBLE_BARS` to at least 20 bars, and set `MAX_VISIBLE_BARS` to the smaller of the available candle count and a report-appropriate cap such as 160 bars. Expand ranges below the minimum and shrink ranges above the maximum around the current center before clamping to the data edges.
- Apply the clamped range back to the source chart as well as every sibling chart. Do not skip the source chart with `if (other !== chart)`, because that leaves the active pane over-zoomed while the other panes are clamped.
- Configure `timeScale` with `minBarSpacing` and a reasonable initial `barSpacing` so bars cannot collapse into unreadable strips at the widest permitted range.
- Preserve the current logical range during fullscreen and resize refreshes. Do not call `fitContent()` on every resize after the initial layout, because it can reset one pane differently from the rest.

## Crosshair And Tooltip

Register `subscribeCrosshairMove` on every chart instance. Build the tooltip from a merged `TooltipSnapshot` indexed by ISO date.

Synchronize the crosshair across panes:

- Keep a `chartEntries` list with `{ chart, series, value }` for each pane's primary series. Use the candle close for the main pane, volume for volume, MACD histogram value for MACD, and the first available oscillator line for KDJ or RSI.
- In every `subscribeCrosshairMove` handler, call `syncCrosshairAcrossCharts(sourceEntry, param, snapshot)`. For every non-source pane, call `setCrosshairPosition(paneValue, param.time, panePrimarySeries)` when the pane value is numeric.
- On pointer leave, missing `param.time`, or missing snapshot, call `clearCrosshairPosition()` on the other panes and hide the tooltip.
- Configure `crosshair.mode` with `CrosshairMode.Normal`, not numeric mode constants and not magnet mode. Configure crosshair `vertLine` and `horzLine` with visible labels. Each pane has its own y-scale, so the synchronized vertical line aligns the timestamp while the pane-local `setCrosshairPosition` value exposes the corresponding y-axis label in that pane.

Required tooltip fields:

- Date and source `date`.
- Open, high, low, close.
- Change percentage when present.
- Volume and amount when present.
- Selected valuation metrics when requested.
- Active indicator values for the hovered date when present.

If `param.time` is missing or the pointer leaves the chart, hide the tooltip and keep the latest-value summary visible.

## Offline Failure Behavior

If JavaScript fails or the chart engine cannot initialize, the HTML must still expose:

- Title, code, date range, latest close, interval return, and row count.
- Latest OHLCV table.
- Source disclosure and risk note.
- Missing-data notes for indicators that cannot be calculated.
