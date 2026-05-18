# Technical State Table Component

## Purpose

Summarize derived technical states without turning them into recommendations: moving-average alignment, MACD cross state, KDJ zone, RSI zone, BOLL position, and volume behavior.

## Input Schema

```json
{
  "states": [
    { "label": "MA20/60/120", "state": "neutral", "value": "MA20 above MA60, below MA120", "evidence": "Calculated from returned daily rows." }
  ]
}
```

Required: `label`, `state`, `value`.

Optional: `evidence`.

## Configuration

- Use `lc-technical-state-table`.
- State values should be `positive`, `negative`, `neutral`, or `warning`.
- Do not output buy, sell, or hold language.
- Include evidence text for each derived state.

## HTML Snippet

```html
<table class="lc-technical-state-table">
  <tbody>
    <tr><td>MACD</td><td>neutral</td><td>DIF remains below DEA</td></tr>
  </tbody>
</table>
```

## Missing Data Behavior

If a state cannot be computed because of warmup limits, show `insufficient rows` and disclose the required lookback.

## Example

Use after the indicator chart or in the right rail of an annual report.
