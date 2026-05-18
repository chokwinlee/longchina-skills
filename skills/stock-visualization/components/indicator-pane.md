# Indicator Pane Component

## Purpose

Render a lower chart pane aligned with the candlestick time axis. Use it for volume, MACD, KDJ, RSI, or other calculated indicator series that should not share the main price scale.

## Input Schema

```json
{
  "pane": "macd",
  "title": "MACD(12,26,9)",
  "height": 160,
  "series": [
    { "kind": "histogram", "label": "MACD", "points": [{ "time": "2026-05-15", "value": 0.22 }] },
    { "kind": "line", "label": "DIF", "points": [{ "time": "2026-05-15", "value": 0.68 }] },
    { "kind": "line", "label": "DEA", "points": [{ "time": "2026-05-15", "value": 0.46 }] }
  ]
}
```

Required: `pane`, `series[].kind`, `series[].label`, `series[].points[].time`.

Optional: `title`, `height`, `series[].points[].color`, `series[].points[].value`.

## Configuration

- Use `HistogramSeries` when `kind` is `histogram`.
- Use `LineSeries` when `kind` is `line`.
- Set `priceLineVisible: false` for indicator helper lines.
- Color MACD histogram bars by sign: positive red/up in A-share convention, negative green/down unless the page chooses a clearly labeled global convention.
- Keep missing points as absent or `null`; do not draw across unavailable warmup periods.

## HTML Snippet

```html
<section class="lc-indicator-pane" aria-label="MACD indicator pane">
  <div class="lc-indicator-pane__head">
    <span class="lc-indicator-pane__title">MACD(12,26,9)</span>
    <span class="lc-indicator-pane__legend">MACD · DIF · DEA</span>
  </div>
  <div id="lc-macd-pane" class="lc-indicator-pane__chart lc-macd-pane"></div>
</section>
```

The chart initialization belongs in the page-level script so panes can synchronize their visible ranges and crosshair behavior.

## Missing Data Behavior

If every series in a pane is empty, show a compact `.lc-indicator-pane__empty` message and omit the chart instance. If only one series is missing, omit that series and disclose the reason in the Source Footnote.

## Example

Volume pane:

```json
{
  "pane": "volume",
  "title": "Volume",
  "series": [
    { "kind": "histogram", "label": "Volume", "points": [{ "time": "2026-05-15", "value": 874512.34, "color": "up" }] }
  ]
}
```
