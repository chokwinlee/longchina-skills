# Scenario Assumption Table Component

## Purpose

Show user-supplied or otherwise explicit assumptions used in scenario analysis. This component documents assumptions; it must not invent missing values to complete a scenario.

## Input Schema

```json
{
  "assumptions": [
    { "name": "Revenue growth", "value": "5%", "source": "User supplied", "date": "20260515", "required": true }
  ]
}
```

Required: `assumptions[].name`, `assumptions[].value`, `assumptions[].source`.

Optional: `assumptions[].date`, `assumptions[].required`, `assumptions[].notes`.

## Configuration

- `lc-scenario-assumption-source`: require `User supplied`, `Returned data`, or another explicit label.
- `show_required`: default true.
- `show_notes`: default true.

## HTML Snippet

```html
<section class="lc-scenario-assumptions" aria-labelledby="lc-scenario-assumptions-title">
  <style>
    .lc-scenario-assumptions { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-scenario-assumptions__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-scenario-assumptions__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; }
    .lc-scenario-assumptions table { border-collapse: collapse; width: 100%; min-width: 560px; }
    .lc-scenario-assumptions th, .lc-scenario-assumptions td { border-bottom: 1px solid oklch(90% 0.012 165); padding: 9px 10px; text-align: left; font-size: 12px; }
    .lc-scenario-assumptions th { background: oklch(96% 0.008 165); color: oklch(42% 0.018 165); }
  </style>
  <h2 class="lc-scenario-assumptions__title" id="lc-scenario-assumptions-title">Scenario assumptions</h2>
  <div class="lc-scenario-assumptions__wrap">
    <table>
      <thead><tr><th>Assumption</th><th>Value</th><th>Source</th><th>Date</th></tr></thead>
      <tbody><tr><td>Revenue growth</td><td>5%</td><td>User supplied</td><td>20260515</td></tr></tbody>
    </table>
  </div>
</section>
```

## Missing Data Behavior

Do not fabricate assumptions, dates, or sources. If a required assumption is missing, show it as missing and prevent downstream scenario panels from presenting calculated outputs that depend on it.

## Example

Place before `scenario-range-panel.md` so the reader can inspect each explicit scenario input first.
