# Data Gap Notice Component

## Purpose

Make missing datasets, filters, fields, or row counts visible before the reader interprets the report. Use it when a requested dataset returns no rows or a required field is unavailable.

## Input Schema

```json
{
  "gaps": [
    {
      "dataset": "daily-metrics",
      "fields": ["float_market_value"],
      "filters": { "symbol": "000001.SZ", "start": "20260501", "end": "20260515" },
      "impact": "Peer valuation comparison excludes float market value."
    }
  ]
}
```

Required: `gaps[].dataset`, `gaps[].impact`.

Optional: `gaps[].fields`, `gaps[].filters`, `gaps[].row_count`.

## Configuration

- `lc-data-gap-severity`: `info`, `warning`, or `blocking`.
- `show_filters`: default true.
- `compact`: default false.

## HTML Snippet

```html
<aside class="lc-data-gap-notice" aria-labelledby="lc-data-gap-notice-title">
  <style>
    .lc-data-gap-notice { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; border: 1px solid oklch(82% 0.06 75); border-radius: 8px; padding: 12px; color: oklch(27% 0.018 75); background: oklch(97% 0.025 75); }
    .lc-data-gap-notice__title { margin: 0 0 8px; font-size: 14px; font-weight: 700; }
    .lc-data-gap-notice__list { margin: 0; padding-left: 18px; font-size: 12px; line-height: 1.55; }
    .lc-data-gap-notice code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; }
  </style>
  <h2 class="lc-data-gap-notice__title" id="lc-data-gap-notice-title">Data gaps</h2>
  <ul class="lc-data-gap-notice__list">
    <li><code>daily-metrics</code> missing <code>float_market_value</code>; peer comparison excludes that metric.</li>
  </ul>
</aside>
```

## Missing Data Behavior

Do not fabricate replacement datasets, row counts, or field values. If a gap affects a rendered component, show this notice near that component and repeat the gap in the Source Footnote.

## Example

Use above a peer table when `daily-metrics` rows exist but one requested metric is absent.
