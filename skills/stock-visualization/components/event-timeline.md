# Event Timeline Component

## Purpose

Show events that explain or contextualize price movement: earnings, dividends, filings, abnormal volume days, corporate actions, or user-supplied thesis checkpoints.

## Input Schema

```json
{
  "events": [
    { "trade_date": "20260320", "kind": "earnings", "title": "Annual report released", "summary": "Revenue +8.4%; net profit +6.1%." }
  ]
}
```

Required: `trade_date`, `kind`, `title`.

Optional: `summary`, `source_dataset`, `source_url`.

## Configuration

- Use `lc-event-timeline`.
- Sort events ascending or descending consistently and label the chosen order.
- Keep event summaries factual unless the user requested analysis.
- Use copper tags for event kind; do not use green as event emphasis.

## HTML Snippet

```html
<section class="lc-event-timeline">
  <h2>事件时间线</h2>
  <ol>
    <li><time>20260320</time><strong>Annual report released</strong></li>
  </ol>
</section>
```

## Missing Data Behavior

If no event dataset is available, show a note that no events were supplied rather than implying there were no events.

## Example

Use below the annual chart or beside the agent brief when the report needs explanatory context.
