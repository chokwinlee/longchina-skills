# Framework Scorecard Component

## Purpose

Summarize selected research frameworks and their evidence status. Use this as the overview for value, fundamental, peer, scenario, margin-of-safety, and data-gap sections without turning the report into a recommendation.

## Input Schema

```json
{
  "frameworks": [
    {
      "key": "value",
      "label": "Value framework",
      "status": "partial",
      "summary": "Valuation metrics are available for the latest returned date.",
      "evidence_count": 4,
      "missing_count": 1
    }
  ]
}
```

Required: `frameworks[].key`, `frameworks[].label`, `frameworks[].status`, `frameworks[].summary`.

Optional: `frameworks[].evidence_count`, `frameworks[].missing_count`.

## Configuration

- `lc-scorecard-statuses`: allowed statuses are `available`, `partial`, `missing`, and `not_requested`.
- `show_counts`: default true.
- `max_items`: default 8.

## HTML Snippet

```html
<section class="lc-framework-scorecard" aria-labelledby="lc-framework-scorecard-title">
  <style>
    .lc-framework-scorecard { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-framework-scorecard__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-framework-scorecard__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; }
    .lc-framework-scorecard__item { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 10px; background: oklch(99% 0.005 165); }
    .lc-framework-scorecard__status { display: inline-block; margin-bottom: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; color: oklch(38% 0.06 165); }
    .lc-framework-scorecard__label { margin: 0 0 4px; font-size: 13px; font-weight: 700; }
    .lc-framework-scorecard__summary { margin: 0; font-size: 12px; line-height: 1.45; color: oklch(42% 0.018 165); }
  </style>
  <h2 class="lc-framework-scorecard__title" id="lc-framework-scorecard-title">Framework status</h2>
  <div class="lc-framework-scorecard__grid">
    <article class="lc-framework-scorecard__item" data-lc-status="partial">
      <span class="lc-framework-scorecard__status">Partial</span>
      <h3 class="lc-framework-scorecard__label">Value framework</h3>
      <p class="lc-framework-scorecard__summary">4 available evidence items, 1 missing item.</p>
    </article>
  </div>
</section>
```

## Missing Data Behavior

Do not fabricate framework status or counts. If no evidence is present for a framework, set `status` to `missing`, show the missing state, and explain the absent datasets in the Source Footnote.

## Example

Place this component near the top of `recipes/framework-research-report.md` after the report title and before detailed evidence panels.
