# Drawdown Panel Component

## Purpose

Show the largest peak-to-trough loss inside the selected period and provide the drawdown curve so readers can separate return from risk.

## Input Schema

```json
{
  "drawdown": {
    "max_drawdown_pct": -18.6,
    "peak_date": "20260210",
    "trough_date": "20260318",
    "recovery_date": null,
    "points": [{ "date": "20260518", "value": -4.2 }]
  }
}
```

Required: `max_drawdown_pct`, `points[].date`, `points[].value`.

Optional: `peak_date`, `trough_date`, `recovery_date`.

## Configuration

- Use `lc-drawdown-panel`.
- Drawdown values should be negative or zero.
- Use green/down market semantics only for negative drawdown values when color is used.
- Label peak, trough, and recovery dates when available.

## HTML Snippet

```html
<section class="lc-drawdown-panel" aria-labelledby="lc-drawdown-title">
  <h2 id="lc-drawdown-title">最大回撤</h2>
  <strong class="lc-down">-18.60%</strong>
  <svg role="img" aria-label="Drawdown curve"></svg>
</section>
```

## Missing Data Behavior

If drawdown points are missing, show a compact empty state and keep the scalar max drawdown if available.

## Example

Pair this with `return-window-table.md` in `annual-performance-report.md`.
