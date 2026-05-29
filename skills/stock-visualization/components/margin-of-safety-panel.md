# Margin Of Safety Panel Component

## Purpose

Display margin-of-safety evidence as labeled observations, separating price-based downside evidence from fundamental evidence. Do not present target prices, expected returns, or promises of future performance.

## Input Schema

```json
{
  "price_downside_evidence": [
    { "label": "Latest close versus 52-week low", "value": "18.4% above low", "date": "20260515", "source": "prices" }
  ],
  "fundamental_evidence": [
    { "label": "PB versus peer median", "value": "Below peer median", "date": "20260515", "source": "daily-metrics" }
  ],
  "risk_notes": ["Historical downside ranges do not guarantee future downside limits."]
}
```

Required: `price_downside_evidence`, `fundamental_evidence`.

Optional: `risk_notes`, evidence `date`, evidence `source`.

## Configuration

- `lc-margin-mode`: `evidence_only`.
- `show_risk_notes`: default true.
- `allow_target_price`: must remain false.

## HTML Snippet

```html
<section class="lc-margin-safety" aria-labelledby="lc-margin-safety-title">
  <style>
    .lc-margin-safety { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-margin-safety__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-margin-safety__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px; }
    .lc-margin-safety__panel { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 12px; background: oklch(99% 0.005 165); }
    .lc-margin-safety__panel h3 { margin: 0 0 8px; font-size: 13px; }
    .lc-margin-safety__panel p { margin: 0 0 6px; font-size: 12px; line-height: 1.45; }
    .lc-margin-safety__risk { margin-top: 10px; font-size: 12px; color: oklch(42% 0.018 165); }
  </style>
  <h2 class="lc-margin-safety__title" id="lc-margin-safety-title">Margin of safety evidence</h2>
  <div class="lc-margin-safety__grid">
    <div class="lc-margin-safety__panel"><h3>Price-based downside</h3><p>Latest close is 18.4% above the returned 52-week low.</p></div>
    <div class="lc-margin-safety__panel"><h3>Fundamental evidence</h3><p>PB is below the peer median on 20260515.</p></div>
  </div>
  <p class="lc-margin-safety__risk">Scenario evidence is not a guarantee and is not a target price.</p>
</section>
```

## Missing Data Behavior

Do not fabricate downside ranges, fundamental context, target prices, or return promises. If price or fundamental evidence is unavailable, show an empty state for that subsection and record the missing dataset or metric.

## Example

Use this panel only after the needed prices and explicit fundamental metrics have been fetched and dated.
