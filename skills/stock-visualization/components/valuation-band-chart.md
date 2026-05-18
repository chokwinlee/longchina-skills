# Valuation Band Chart Component

## Purpose

Show current valuation in the context of the selected period: PE/PB current values, min/max ranges, percentiles, and a compact time-series view.

## Input Schema

```json
{
  "valuation": {
    "pe_ttm": { "current": 8.9, "min": 7.2, "max": 10.8, "percentile": 61 },
    "pb": { "current": 0.96, "min": 0.78, "max": 1.12, "percentile": 54 },
    "points": [{ "trade_date": "20260518", "pe_ttm": 8.9, "pb": 0.96 }]
  }
}
```

Required: at least one metric object and `points` for the time-series chart.

Optional: percentile fields when the sample is too short or missing.

## Configuration

- Use `lc-valuation-band`.
- Render a dense range summary plus SVG or canvas trend.
- Keep PE and PB legends explicit; do not rely on color alone.
- Use copper and blue for valuation series, not green.

## HTML Snippet

```html
<section class="lc-valuation-band">
  <h2>估值分位</h2>
  <div class="lc-valuation-band__range">
    <span>PE TTM</span><strong>8.90x</strong><small>61%</small>
  </div>
</section>
```

## Missing Data Behavior

If `daily-basic` was not returned, omit this block and disclose the missing dataset in Source Footnote. Do not fabricate valuation percentiles.

## Example

Use beside `drawdown-panel.md` in a two-column report section.
