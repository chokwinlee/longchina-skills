# Scenario Range Panel Component

## Purpose

Show explicit scenario ranges and their assumptions without implying a guarantee, target price, or certain outcome. Use it for bounded sensitivity views based on user-supplied or returned inputs.

## Input Schema

```json
{
  "ranges": [
    { "label": "Conservative", "assumptions": ["Revenue growth 2%"], "output": "Value indicator below peer median", "source": "User supplied" },
    { "label": "Base", "assumptions": ["Revenue growth 5%"], "output": "Value indicator near peer median", "source": "User supplied" }
  ],
  "risk_note": "Scenario ranges are assumptions, not forecasts or guarantees."
}
```

Required: `ranges[].label`, `ranges[].assumptions`, `ranges[].output`, `ranges[].source`.

Optional: `risk_note`.

## Configuration

- `lc-scenario-range-mode`: `assumption_range`.
- `show_risk_note`: default true.
- `allow_probability`: default false unless probabilities are explicitly supplied.

## HTML Snippet

```html
<section class="lc-scenario-range" aria-labelledby="lc-scenario-range-title">
  <style>
    .lc-scenario-range { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-scenario-range__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-scenario-range__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px; }
    .lc-scenario-range__item { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 10px; background: oklch(99% 0.005 165); }
    .lc-scenario-range__item h3 { margin: 0 0 6px; font-size: 13px; }
    .lc-scenario-range__item p { margin: 0; font-size: 12px; line-height: 1.45; color: oklch(42% 0.018 165); }
    .lc-scenario-range__risk { margin: 10px 0 0; font-size: 12px; color: oklch(42% 0.018 165); }
  </style>
  <h2 class="lc-scenario-range__title" id="lc-scenario-range-title">Scenario range</h2>
  <div class="lc-scenario-range__grid">
    <article class="lc-scenario-range__item"><h3>Conservative</h3><p>Revenue growth 2%; value indicator below peer median.</p></article>
    <article class="lc-scenario-range__item"><h3>Base</h3><p>Revenue growth 5%; value indicator near peer median.</p></article>
  </div>
  <p class="lc-scenario-range__risk">Scenario ranges are assumptions, not forecasts or guarantees.</p>
</section>
```

## Missing Data Behavior

Do not fabricate ranges, probabilities, outputs, or assumptions. If a range depends on missing assumptions, show the range as unavailable and point to `scenario-assumption-table.md`.

## Example

Use after the Scenario Assumption Table when all displayed ranges trace back to explicit assumptions.
