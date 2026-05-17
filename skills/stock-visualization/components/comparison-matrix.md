# Comparison Matrix Component

## Purpose

Compare 2 to 5 securities across core metrics in a semantic table. Use it for quick side-by-side valuation, market value, turnover, and date checks.

## Input Schema

```json
{
  "columns": [
    { "key": "close", "label": "Close", "unit": "CNY" },
    { "key": "pe_ttm", "label": "PE TTM", "unit": "x" },
    { "key": "pb", "label": "PB", "unit": "x" },
    { "key": "total_mv", "label": "Market value", "unit": "CNY" }
  ],
  "rows": [
    {
      "ts_code": "000001.SZ",
      "name": "Example Bank",
      "trade_date": "20260515",
      "values": { "close": 11.73, "pe_ttm": 5.94, "pb": 0.62, "total_mv": 227680000000 }
    }
  ]
}
```

Required: `columns[].key`, `columns[].label`, `rows[].ts_code`, `rows[].name`, `rows[].values`.

Optional: `columns[].unit`, `rows[].trade_date`.

## Configuration

- `max_rows`: 5 for comparison pages.
- `show_units`: default true.
- `show_trade_date`: default true.
- `compact_numbers`: default true for large CNY values.

## HTML Snippet

```html
<section class="lc-comparison-matrix" aria-labelledby="lc-comparison-matrix-title">
  <style>
    .lc-comparison-matrix { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-comparison-matrix__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-comparison-matrix__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; background: oklch(99% 0.005 165); }
    .lc-comparison-matrix table { border-collapse: collapse; width: 100%; min-width: 620px; }
    .lc-comparison-matrix th, .lc-comparison-matrix td { border-bottom: 1px solid oklch(90% 0.012 165); padding: 10px 12px; text-align: right; font-size: 12px; }
    .lc-comparison-matrix th:first-child, .lc-comparison-matrix td:first-child { text-align: left; }
    .lc-comparison-matrix th { color: oklch(42% 0.018 165); font-weight: 650; background: oklch(96% 0.008 165); }
    .lc-comparison-matrix tr:last-child td { border-bottom: 0; }
    .lc-comparison-matrix__date { display: block; color: oklch(50% 0.016 165); font-size: 11px; font-weight: 400; }
  </style>
  <h2 class="lc-comparison-matrix__title" id="lc-comparison-matrix-title">Metric comparison</h2>
  <div class="lc-comparison-matrix__wrap">
    <table>
      <thead>
        <tr><th>Security</th><th>Close (CNY)</th><th>PE TTM (x)</th><th>PB (x)</th><th>Market value (CNY)</th></tr>
      </thead>
      <tbody>
        <tr><td>Example Bank <span class="lc-comparison-matrix__date">000001.SZ, 20260515</span></td><td>11.73</td><td>5.94</td><td>0.62</td><td>227.7B</td></tr>
        <tr><td>Example Industry Peer <span class="lc-comparison-matrix__date">600000.SH, 20260515</span></td><td>8.42</td><td>6.38</td><td>0.54</td><td>154.2B</td></tr>
      </tbody>
    </table>
  </div>
</section>
```

## Missing Data Behavior

Use `--` for missing values. If rows use different latest dates, keep each row's date visible and add a note in the Source Footnote.

## Example

Use below Comparison Cards in `recipes/stock-compare.md`.
