# Candlestick Chart Component

## Purpose

Render the default stock price view for A-share OHLC data: candlesticks on the main pane, moving-average overlays, volume, MACD, optional KDJ/RSI panes, and a hover tooltip. Use this component whenever `prices` rows include `open`, `high`, `low`, and `close`.

Read `references/chart-engine.md`, `references/data-contracts.md`, and `references/indicator-rules.md` before generating the final HTML. Do not replace this component with `price-trend.md` unless OHLC rows are unavailable.

## Input Schema

```json
{
  "profile": { "symbol": "601318.SH", "name": "中国平安" },
  "summary": {
    "date_range": "2026-04-01 to 2026-05-15",
    "latest_close": 52.2,
    "interval_return_pct": 6.31,
    "row_count": 30
  },
  "candles": [
    {
      "time": "2026-05-15",
      "date": "20260515",
      "open": 51.2,
      "high": 52.8,
      "low": 50.9,
      "close": 52.2,
      "previous_close": 50.82,
      "percent_change": 2.71,
      "volume": 874512.34,
      "amount": 998231.12
    }
  ],
  "overlays": [
    { "kind": "ma", "label": "MA5", "period": 5, "points": [{ "time": "2026-05-15", "value": 51.84 }] }
  ],
  "panes": [
    {
      "pane": "volume",
      "series": [
        { "kind": "histogram", "label": "Volume", "points": [{ "time": "2026-05-15", "value": 874512.34, "color": "up" }] }
      ]
    },
    {
      "pane": "macd",
      "series": [
        { "kind": "histogram", "label": "MACD", "points": [{ "time": "2026-05-15", "value": 0.22 }] },
        { "kind": "line", "label": "DIF", "points": [{ "time": "2026-05-15", "value": 0.68 }] },
        { "kind": "line", "label": "DEA", "points": [{ "time": "2026-05-15", "value": 0.46 }] }
      ]
    }
  ],
  "tooltip": {
    "2026-05-15": {
      "time": "2026-05-15",
      "date": "20260515",
      "open": 51.2,
      "high": 52.8,
      "low": 50.9,
      "close": 52.2,
      "percent_change": 2.71,
      "volume": 874512.34,
      "amount": 998231.12,
      "pe_ttm": 8.91,
      "pb": 0.96
    }
  }
}
```

Required: `profile.symbol`, `profile.name`, `candles[].time`, `candles[].open`, `candles[].high`, `candles[].low`, `candles[].close`.

Optional: `summary`, `overlays`, `panes`, `tooltip`, daily-metrics metrics, missing-data notes.

## Configuration

- `main_height`: recommended 420 to 520 pixels on desktop, 320 to 420 on mobile.
- `volume_height`: recommended 120 pixels.
- `indicator_height`: recommended 150 to 180 pixels per indicator pane.
- `default_overlays`: `["MA5", "MA10", "MA20"]`.
- `default_panes`: `["volume", "macd"]`; add `kdj` when at least 9 valid rows exist.
- `indicator_controls`: render visible checkbox controls for every optional overlay and pane.
- `price_scale`: right side.
- `min_visible_bars`: minimum visible bars for zoom; default 20.
- `max_visible_bars`: maximum visible bars for zoom; default 160 or the available row count when smaller.
- `time_scale_sync`: required logical range synchronization across every stacked pane.
- `crosshair_sync`: required crosshair synchronization across every stacked pane with `setCrosshairPosition`.
- `empty_label`: `No OHLC rows returned for this interval.`

## HTML Snippet

```html
<section class="lc-candlestick-chart" aria-labelledby="lc-candlestick-title">
  <header class="lc-candlestick-chart__header">
    <div>
      <h2 id="lc-candlestick-title" class="lc-candlestick-chart__title">中国平安 601318.SH</h2>
      <p class="lc-candlestick-chart__meta">2026-04-01 to 2026-05-15 · daily candles · 30 rows</p>
    </div>
    <div class="lc-candlestick-chart__latest">52.20 CNY <span>+2.71%</span></div>
  </header>
  <div class="lc-indicator-controls" aria-label="Chart indicator controls">
    <label class="lc-indicator-toggle">
      <input type="checkbox" data-overlay-label="MA5" checked aria-label="Toggle MA5">
      <span class="lc-indicator-toggle__swatch" aria-hidden="true"></span>
      <span>MA5</span>
    </label>
    <label class="lc-indicator-toggle">
      <input type="checkbox" data-overlay-label="MA10" checked aria-label="Toggle MA10">
      <span class="lc-indicator-toggle__swatch" aria-hidden="true"></span>
      <span>MA10</span>
    </label>
    <label class="lc-indicator-toggle">
      <input type="checkbox" data-volume-pane checked aria-label="Toggle volume pane">
      <span class="lc-indicator-toggle__swatch" aria-hidden="true"></span>
      <span>Volume</span>
    </label>
  </div>
  <div class="lc-candlestick-chart__wrap">
    <div id="lc-main-chart" class="lc-candlestick-chart__pane" role="img" aria-label="Candlestick chart"></div>
    <div id="lc-volume-pane" class="lc-candlestick-chart__pane lc-volume-pane" role="img" aria-label="Volume histogram"></div>
    <div id="lc-macd-pane" class="lc-candlestick-chart__pane lc-macd-pane" role="img" aria-label="MACD indicator"></div>
    <div id="lc-tooltip" class="lc-tooltip" hidden></div>
  </div>
</section>
```

Use the actual chart initialization from `references/chart-engine.md`. Keep class names prefixed with `lc-`.

Indicator controls must change the chart state, not just the visual chip state:

- `data-overlay-label` controls matching main-pane line series such as MA5, MA20, MA60, MA120, BOLL upper/mid/lower, DIF, or DEA.
- `data-volume-pane` controls the volume pane visibility and histogram data.
- When unchecked, clear the corresponding series with `series.setData([])` or hide the pane and preserve the original data for re-check.
- Keep the checkbox visible and keyboard reachable; do not rely on color-only legend text.

Pane synchronization is part of the component contract:

- Use logical range synchronization, not time-range-only synchronization, for all stacked panes.
- Enforce minimum visible bars so users cannot zoom into an unreadably small fragment.
- Enforce maximum visible bars so users cannot over-compress the full history into a single narrow strip.
- Keep crosshair synchronization enabled across main, volume, MACD, KDJ, and RSI panes.
- Use pane-local values with `setCrosshairPosition` so the y-axis marker appears in each pane for the same timestamp.

## Missing Data Behavior

If there are no candles, render an empty state and do not initialize the chart. If fewer than the required rows exist for an indicator, omit that series, keep other panes visible, and state the affected indicator in the Source Footnote. Do not interpolate missing trading dates.

## Example

Use `recipes/candlestick-report.md` and `examples/candlestick-report.html` for a complete page. For two to three stock comparisons, repeat this component as small panels; for four or more stocks, use indexed lines only when that better fits the available width.
