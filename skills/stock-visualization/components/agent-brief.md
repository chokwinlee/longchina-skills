# Agent Brief Component

## Purpose

Provide a concise research-style synthesis that separates facts, derived observations, and assumptions. This is not a recommendation component.

## Input Schema

```json
{
  "agent_brief": {
    "title": "Research brief",
    "points": [
      "Price outperformed the benchmark while valuation percentile stayed mid-range."
    ],
    "assumptions": [
      "Benchmark series was supplied by the user."
    ]
  }
}
```

Required: `title`, `points`.

Optional: `assumptions`, `limitations`, `next_questions`.

## Configuration

- Use `lc-agent-brief`.
- Keep the tone restrained and evidence-oriented.
- Avoid buy, sell, hold, target price, certainty, or promised return language.
- Label assumptions and missing data.

## HTML Snippet

```html
<section class="lc-agent-brief" aria-labelledby="lc-agent-brief-title">
  <h2 id="lc-agent-brief-title">Research brief</h2>
  <ul><li>Outperformance came mostly after the March drawdown.</li></ul>
</section>
```

## Missing Data Behavior

If the brief cannot be supported by returned rows, omit interpretive points and show only factual data limitations.

## Example

Use near the end of `recipes/annual-performance-report.md`, before Source Footnote.
