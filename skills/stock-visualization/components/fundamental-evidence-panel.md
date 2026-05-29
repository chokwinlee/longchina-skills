# Fundamental Evidence Panel Component

## Purpose

Separate available fundamental evidence from missing evidence. Use it to show what the report can support from returned `securities`, `prices`, and `daily-metrics` rows.

## Input Schema

```json
{
  "available": [
    { "label": "Total market value", "value": 227680000000, "unit": "CNY", "date": "20260515", "dataset": "daily-metrics" }
  ],
  "missing": [
    { "label": "Float market value", "dataset": "daily-metrics", "reason": "No value returned for the latest date." }
  ]
}
```

Required: `available`, `missing`.

Optional: `available[].unit`, `available[].date`, `available[].dataset`, `missing[].dataset`, `missing[].reason`.

## Configuration

- `lc-evidence-empty_label`: default `No evidence returned`.
- `show_dataset`: default true.
- `show_date`: default true.

## HTML Snippet

```html
<section class="lc-fundamental-evidence" aria-labelledby="lc-fundamental-evidence-title">
  <style>
    .lc-fundamental-evidence { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-fundamental-evidence__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-fundamental-evidence__cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }
    .lc-fundamental-evidence__box { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 12px; }
    .lc-fundamental-evidence__box h3 { margin: 0 0 8px; font-size: 13px; }
    .lc-fundamental-evidence__list { margin: 0; padding-left: 18px; font-size: 12px; line-height: 1.55; }
    .lc-fundamental-evidence__meta { color: oklch(48% 0.016 165); font-size: 11px; }
  </style>
  <h2 class="lc-fundamental-evidence__title" id="lc-fundamental-evidence-title">Fundamental evidence</h2>
  <div class="lc-fundamental-evidence__cols">
    <div class="lc-fundamental-evidence__box">
      <h3>Available</h3>
      <ul class="lc-fundamental-evidence__list">
        <li>Total market value: 227.7B CNY <span class="lc-fundamental-evidence__meta">daily-metrics, 20260515</span></li>
      </ul>
    </div>
    <div class="lc-fundamental-evidence__box">
      <h3>Missing</h3>
      <ul class="lc-fundamental-evidence__list">
        <li>Float market value <span class="lc-fundamental-evidence__meta">No value returned.</span></li>
      </ul>
    </div>
  </div>
</section>
```

## Missing Data Behavior

Do not fabricate fundamental values. Keep missing evidence visible in the `missing` list and render `--` only inside an available row when one optional display field is absent.

## Example

Use after the Framework Scorecard when a report needs to distinguish facts available from `daily-metrics` from fields that were requested but not returned.
