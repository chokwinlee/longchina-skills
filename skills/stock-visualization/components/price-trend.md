# Price Trend Component

## Purpose

Render a compact fallback price trend chart for close-only or indexed series. For OHLC stock price visualization, use `candlestick-chart.md`; do not use this component as the primary stock chart when `open`, `high`, `low`, and `close` are available.

Before writing SVG `points`, use `references/rendering-helpers.md` to convert the actual returned `series` into chart coordinates. The snippet below is structural; do not reuse its example coordinates for live data.

## Input Schema

```json
{
  "title": "Example Bank price trend",
  "subtitle": "20260511 to 20260515",
  "series": [
    { "date": "20260511", "close": 11.42, "ma5": null, "ma20": null },
    { "date": "20260512", "close": 11.56, "ma5": null, "ma20": null },
    { "date": "20260513", "close": 11.31, "ma5": null, "ma20": null },
    { "date": "20260514", "close": 11.68, "ma5": null, "ma20": null },
    { "date": "20260515", "close": 11.73, "ma5": 11.54, "ma20": null }
  ],
  "summary": {
    "interval_return_pct": 2.71,
    "latest_close": 11.73,
    "latest_date": "20260515"
  }
}
```

Required: `title`, `series[].date`, `series[].close`.

Optional: `subtitle`, `series[].ma5`, `series[].ma20`, `summary`.

## Configuration

- `height`: recommended 220 to 320 pixels.
- `show_ma`: array such as `["ma5", "ma20"]`.
- `currency`: display label such as `CNY`.
- `empty_label`: default `No price rows returned for this interval.`

## HTML Snippet

```html
<section class="lc-price-trend" aria-labelledby="lc-price-trend-title">
  <style>
    .lc-price-trend { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); background: oklch(98% 0.006 165); border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 18px; }
    .lc-price-trend__head { display: flex; justify-content: space-between; gap: 16px; align-items: start; margin-bottom: 14px; }
    .lc-price-trend__title { margin: 0; font-size: 16px; line-height: 1.25; font-weight: 650; }
    .lc-price-trend__subtitle { margin: 4px 0 0; color: oklch(46% 0.018 165); font-size: 12px; }
    .lc-price-trend__return { font-size: 13px; font-weight: 650; }
    .lc-price-trend__return[data-state="up"] { color: oklch(42% 0.13 150); }
    .lc-price-trend__return[data-state="down"] { color: oklch(48% 0.16 28); }
    .lc-price-trend svg { display: block; width: 100%; height: auto; overflow: visible; }
    .lc-price-trend__axis { stroke: oklch(78% 0.016 165); stroke-width: 1; }
    .lc-price-trend__line { fill: none; stroke: oklch(42% 0.12 165); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
    .lc-price-trend__ma { fill: none; stroke: oklch(58% 0.10 78); stroke-width: 1.8; stroke-dasharray: 4 4; }
    .lc-price-trend__label { fill: oklch(46% 0.018 165); font-size: 11px; }
  </style>
  <div class="lc-price-trend__head">
    <div>
      <h2 class="lc-price-trend__title" id="lc-price-trend-title">Example Bank price trend</h2>
      <p class="lc-price-trend__subtitle">20260511 to 20260515, close price in CNY</p>
    </div>
    <div class="lc-price-trend__return" data-state="up">+2.71%</div>
  </div>
  <svg viewBox="0 0 640 240" role="img" aria-label="Close price line chart from 20260511 to 20260515">
    <line class="lc-price-trend__axis" x1="48" y1="196" x2="604" y2="196"></line>
    <line class="lc-price-trend__axis" x1="48" y1="34" x2="48" y2="196"></line>
    <polyline class="lc-price-trend__line" points="48,158 187,119 326,188 465,86 604,72"></polyline>
    <polyline class="lc-price-trend__ma" points="604,125"></polyline>
    <text class="lc-price-trend__label" x="48" y="220">20260511</text>
    <text class="lc-price-trend__label" x="548" y="220">20260515</text>
    <text class="lc-price-trend__label" x="8" y="40">11.73</text>
    <text class="lc-price-trend__label" x="8" y="198">11.31</text>
  </svg>
</section>
```

## Missing Data Behavior

If `series` is empty, render a bordered empty state with the configured `empty_label`. If moving averages are unavailable, omit those lines and state the reason in the Source Footnote.

## Example

Use in `recipes/stock-compare.md` after calculating `interval_return_pct`, `ma5`, and any other requested series from `prices` rows.
