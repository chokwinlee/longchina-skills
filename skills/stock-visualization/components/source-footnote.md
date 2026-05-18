# Source Footnote Component

## Purpose

Render provenance, missing-data, generation, and risk information. Every generated HTML page must include this component or an equivalent source disclosure block.

## Input Schema

```json
{
  "generated_at": "2026-05-16T16:30:00+08:00",
  "data_sources": [
    {
      "dataset": "daily",
      "fields": ["symbol", "date", "close", "volume"],
      "filters": { "symbol": "000001.SZ", "start": "20260511", "end": "20260515" },
      "row_count": 5
    }
  ],
  "notes": ["Example output uses illustrative values."],
  "risk_note": "This visualization is not investment advice."
}
```

Required: `generated_at`, `data_sources`, `risk_note`.

Optional: `notes`, `usage`.

## Configuration

- `show_filters`: default true.
- `show_fields`: default true.
- `compact`: default false.

## HTML Snippet

```html
<footer class="lc-source-footnote" aria-label="Data source and risk notes">
  <style>
    .lc-source-footnote { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(38% 0.018 165); border-top: 1px solid oklch(86% 0.018 165); padding-top: 16px; font-size: 12px; line-height: 1.55; }
    .lc-source-footnote h2 { margin: 0 0 8px; color: oklch(24% 0.012 165); font-size: 13px; font-weight: 700; }
    .lc-source-footnote dl { display: grid; grid-template-columns: max-content 1fr; gap: 6px 12px; margin: 0; }
    .lc-source-footnote dt { font-weight: 650; color: oklch(30% 0.014 165); }
    .lc-source-footnote dd { margin: 0; }
    .lc-source-footnote code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; }
  </style>
  <h2>Data source and risk notes</h2>
  <dl>
    <dt>Generated</dt><dd>2026-05-16T16:30:00+08:00</dd>
    <dt>Sources</dt><dd><code>securities</code>, <code>daily</code>, <code>daily-metrics</code></dd>
    <dt>Filters</dt><dd><code>000001.SZ</code> and <code>600000.SH</code>, 20260511 to 20260515</dd>
    <dt>Notes</dt><dd>Example output uses illustrative values. Missing values are shown as <code>--</code>.</dd>
    <dt>Risk</dt><dd>This visualization is not investment advice. Verify returned rows, dates, and assumptions before making decisions.</dd>
  </dl>
</footer>
```

## Missing Data Behavior

Never omit the footnote because source metadata is incomplete. Show the available metadata and state which metadata was unavailable.

## Example

Use as the final block in every recipe.
