# Peer Factor Heatmap Component

## Purpose

Compare peer factors across a selected security set while treating missing or null values safely. Use it for compact factor direction, not for unsupported rankings or recommendations.

## Input Schema

```json
{
  "factors": [
    { "key": "pb", "label": "PB", "direction": "lower_is_lower_valuation" },
    { "key": "total_market_value", "label": "Total market value", "direction": "higher_is_larger" }
  ],
  "rows": [
    { "symbol": "000001.SZ", "name": "Example Bank", "date": "20260515", "values": { "pb": 0.62, "total_market_value": 227680000000 } }
  ]
}
```

Required: `factors[].key`, `factors[].label`, `rows[].symbol`, `rows[].values`.

Optional: `factors[].direction`, `rows[].name`, `rows[].date`.

## Configuration

- `lc-peer-heatmap-scale`: `ranked_present_values`.
- `missing_color`: neutral background.
- `show_date`: default true.

## HTML Snippet

```html
<section class="lc-peer-factor-heatmap" aria-labelledby="lc-peer-factor-heatmap-title">
  <style>
    .lc-peer-factor-heatmap { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-peer-factor-heatmap__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-peer-factor-heatmap__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; }
    .lc-peer-factor-heatmap table { border-collapse: collapse; width: 100%; min-width: 560px; }
    .lc-peer-factor-heatmap th, .lc-peer-factor-heatmap td { border-bottom: 1px solid oklch(90% 0.012 165); padding: 9px 10px; text-align: right; font-size: 12px; }
    .lc-peer-factor-heatmap th:first-child, .lc-peer-factor-heatmap td:first-child { text-align: left; }
    .lc-peer-factor-heatmap__cell { background: oklch(92% 0.035 165); }
    .lc-peer-factor-heatmap__missing { background: oklch(95% 0.004 165); color: oklch(55% 0.012 165); }
  </style>
  <h2 class="lc-peer-factor-heatmap__title" id="lc-peer-factor-heatmap-title">Peer factor heatmap</h2>
  <div class="lc-peer-factor-heatmap__wrap">
    <table>
      <thead><tr><th>Security</th><th>PB</th><th>Total market value</th></tr></thead>
      <tbody><tr><td>Example Bank<br>000001.SZ, 20260515</td><td class="lc-peer-factor-heatmap__cell">0.62</td><td class="lc-peer-factor-heatmap__missing">--</td></tr></tbody>
    </table>
  </div>
</section>
```

## Missing Data Behavior

Do not fabricate factor values or peer medians. Render null and missing values as `--`, exclude them from color scaling, and note material missing fields in the Source Footnote.

## Example

Use with `peer-rank-table.md` when comparing the same explicit peer set across valuation and market value factors.
