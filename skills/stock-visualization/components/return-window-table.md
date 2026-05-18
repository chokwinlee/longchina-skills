# Return Window Table Component

## Purpose

Compare stock, benchmark, excess return, and drawdown across common lookback windows such as 1M, 3M, 6M, and 1Y.

## Input Schema

```json
{
  "windows": [
    { "label": "1M", "stock_return_pct": 3.2, "benchmark_return_pct": 1.1, "excess_return_pct": 2.1, "max_drawdown_pct": -4.8 },
    { "label": "1Y", "stock_return_pct": 12.4, "benchmark_return_pct": 4.1, "excess_return_pct": 8.3, "max_drawdown_pct": -18.6 }
  ]
}
```

Required: `label`, `stock_return_pct`.

Optional: `benchmark_return_pct`, `excess_return_pct`, `max_drawdown_pct`.

## Configuration

- Use semantic HTML tables.
- Use `lc-return-window-table` for the wrapper table.
- Keep columns right-aligned except the window label.
- Missing benchmark values must not be treated as zero.

## HTML Snippet

```html
<table class="lc-return-window-table">
  <thead><tr><th>窗口</th><th>股票</th><th>基准</th><th>超额</th><th>最大回撤</th></tr></thead>
  <tbody>
    <tr><td>1Y</td><td class="lc-up">+12.40%</td><td>+4.10%</td><td class="lc-up">+8.30pct</td><td class="lc-down">-18.60%</td></tr>
  </tbody>
</table>
```

## Missing Data Behavior

Show `--` for unavailable benchmark or drawdown cells and disclose the missing source in the report footnote.

## Example

Use after the main chart in annual reports so readers can compare short and long windows without hovering the chart.
