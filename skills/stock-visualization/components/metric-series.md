# Metric Series Component

## Purpose

Render one time-series metric such as PE TTM, PB, PS, turnover rate, total market value, or volume. Use it when the user asks how an indicator changed over time.

Before writing SVG `points`, use `references/rendering-helpers.md` to convert the actual returned `points` into chart coordinates. The snippet below is structural; do not reuse its example coordinates for live data.

## Input Schema

```json
{
  "title": "PE TTM",
  "unit": "x",
  "points": [
    { "trade_date": "20260511", "value": 5.82 },
    { "trade_date": "20260512", "value": 5.86 },
    { "trade_date": "20260513", "value": 5.74 },
    { "trade_date": "20260514", "value": 5.91 },
    { "trade_date": "20260515", "value": 5.94 }
  ],
  "source_dataset": "daily-basic"
}
```

Required: `title`, `points[].trade_date`, `points[].value`, `source_dataset`.

Optional: `unit`, `description`.

## Configuration

- `height`: recommended 180 to 260 pixels.
- `value_format`: `decimal`, `percent`, `compact-cny`, or `raw`.
- `empty_label`: default `No metric rows returned.`

## HTML Snippet

```html
<section class="lc-metric-series" aria-labelledby="lc-metric-series-title">
  <style>
    .lc-metric-series { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 16px; background: oklch(99% 0.005 165); }
    .lc-metric-series__title { margin: 0 0 4px; font-size: 14px; font-weight: 650; }
    .lc-metric-series__meta { margin: 0 0 12px; color: oklch(48% 0.018 165); font-size: 12px; }
    .lc-metric-series svg { display: block; width: 100%; height: auto; }
    .lc-metric-series__grid { stroke: oklch(90% 0.012 165); stroke-width: 1; }
    .lc-metric-series__line { fill: none; stroke: oklch(42% 0.12 165); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
    .lc-metric-series__dot { fill: oklch(42% 0.12 165); }
    .lc-metric-series__label { fill: oklch(46% 0.018 165); font-size: 11px; }
  </style>
  <h2 class="lc-metric-series__title" id="lc-metric-series-title">PE TTM</h2>
  <p class="lc-metric-series__meta">daily-basic, unit x</p>
  <svg viewBox="0 0 520 180" role="img" aria-label="PE TTM metric series">
    <line class="lc-metric-series__grid" x1="36" y1="32" x2="500" y2="32"></line>
    <line class="lc-metric-series__grid" x1="36" y1="136" x2="500" y2="136"></line>
    <polyline class="lc-metric-series__line" points="36,93 152,78 268,124 384,58 500,46"></polyline>
    <circle class="lc-metric-series__dot" cx="500" cy="46" r="3"></circle>
    <text class="lc-metric-series__label" x="36" y="164">20260511</text>
    <text class="lc-metric-series__label" x="444" y="164">20260515</text>
  </svg>
</section>
```

## Missing Data Behavior

Omit null points from the plotted line. If all points are null or missing, render an empty state and include the dataset/filter details in the Source Footnote.

## Example

Use after mapping `daily-basic.pe_ttm` rows into `MetricPoint` objects.
