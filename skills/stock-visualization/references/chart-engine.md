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

Synchronize visible ranges both ways with `timeScale().subscribeVisibleTimeRangeChange`. Avoid recursive updates with a boolean guard.

## Crosshair And Tooltip

Register `subscribeCrosshairMove` on every chart instance. Build the tooltip from a merged `TooltipSnapshot` indexed by ISO date.

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
