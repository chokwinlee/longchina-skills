# Peer Rank Table Component

## Purpose

Rank peers only on metrics that are explicitly present. Show the metric date beside each ranked value so readers can spot stale or mismatched observations.

## Input Schema

```json
{
  "metric": { "key": "pb", "label": "PB", "unit": "x", "rank_order": "ascending" },
  "rows": [
    { "rank": 1, "symbol": "000001.SZ", "name": "Example Bank", "value": 0.62, "date": "20260515" }
  ],
  "excluded": [
    { "symbol": "600000.SH", "reason": "PB was null." }
  ]
}
```

Required: `metric.key`, `metric.label`, `metric.rank_order`, `rows[].symbol`, `rows[].value`, `rows[].date`.

Optional: `metric.unit`, `rows[].name`, `excluded`.

## Configuration

- `lc-peer-rank-method`: `present_values_only`.
- `show_excluded`: default true.
- `max_rows`: default 20.

## HTML Snippet

```html
<section class="lc-peer-rank-table" aria-labelledby="lc-peer-rank-table-title">
  <style>
    .lc-peer-rank-table { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-peer-rank-table__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-peer-rank-table__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; }
    .lc-peer-rank-table table { border-collapse: collapse; width: 100%; min-width: 520px; }
    .lc-peer-rank-table th, .lc-peer-rank-table td { border-bottom: 1px solid oklch(90% 0.012 165); padding: 9px 10px; text-align: right; font-size: 12px; }
    .lc-peer-rank-table th:first-child, .lc-peer-rank-table td:first-child { text-align: left; }
    .lc-peer-rank-table__excluded { margin: 8px 0 0; color: oklch(48% 0.016 165); font-size: 12px; }
  </style>
  <h2 class="lc-peer-rank-table__title" id="lc-peer-rank-table-title">Peer rank: PB</h2>
  <div class="lc-peer-rank-table__wrap">
    <table>
      <thead><tr><th>Rank</th><th>Security</th><th>PB</th><th>Date</th></tr></thead>
      <tbody><tr><td>1</td><td>Example Bank<br>000001.SZ</td><td>0.62x</td><td>20260515</td></tr></tbody>
    </table>
  </div>
  <p class="lc-peer-rank-table__excluded">Excluded: 600000.SH because PB was null.</p>
</section>
```

## Missing Data Behavior

Do not fabricate ranks for missing metrics. Exclude rows with missing values from ranking, list them separately, and never infer dates from neighboring rows.

## Example

Use one table per selected rank metric, such as PB or total market value, after verifying each value and date are present.
