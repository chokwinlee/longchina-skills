# Capital Flow Panel Component

## Purpose

Show capital-flow and liquidity evidence without pretending that price and turnover are true fund-flow data. Use this component for A-share technical or framework reports that need amount, volume, turnover, volume ratio, Stock Connect shareholding context, or macro-liquidity reference notes.

## Input Schema

```json
{
  "as_of": "2026-05-15",
  "rows": [
    {
      "label": "成交额变化",
      "value": "+18.4%",
      "state": "positive",
      "date": "2026-05-15",
      "source": "prices",
      "evidence": "Latest five-row average amount is above the prior five-row average."
    },
    {
      "label": "换手率",
      "value": "1.32%",
      "state": "neutral",
      "date": "2026-05-15",
      "source": "daily-metrics",
      "evidence": "Latest returned turnover metric."
    }
  ],
  "external_references": [
    {
      "source_type": "public reference",
      "source_name": "HKEX Stock Connect shareholding search",
      "retrieved_at": "2026-05-26",
      "evidence_used": "Northbound shareholding snapshot by date",
      "limitation": "Public reference only; not merged into Longchina rows."
    }
  ]
}
```

Required: `rows[].label`, `rows[].value`, `rows[].date`, `rows[].source`, `rows[].evidence`.

Optional: `as_of`, `rows[].state`, `external_references`.

## Configuration

- Use `lc-capital-flow-panel`.
- State values should be `positive`, `negative`, `neutral`, or `warning`.
- Keep Longchina evidence and public reference evidence visually distinct.
- Use `prices.amount`, `prices.volume`, `daily-metrics.turnover_rate`, `daily-metrics.free_float_turnover_rate`, and `daily-metrics.volume_ratio` only when returned.
- Do not label amount, volume, turnover, or volume ratio as net inflow, main-fund inflow, smart money, or institutional buying.
- Do not output buy, sell, or hold language.

## HTML Snippet

```html
<section class="lc-capital-flow-panel" aria-labelledby="lc-capital-flow-title">
  <style>
    .lc-capital-flow-panel { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-capital-flow-panel__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-capital-flow-panel__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px; }
    .lc-capital-flow-panel__item { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 10px; background: oklch(99% 0.005 165); }
    .lc-capital-flow-panel__item span { display: block; color: oklch(45% 0.018 165); font-size: 12px; }
    .lc-capital-flow-panel__item strong { display: block; margin-top: 4px; font-size: 18px; font-variant-numeric: tabular-nums; }
    .lc-capital-flow-panel__item p { margin: 8px 0 0; color: oklch(42% 0.018 165); font-size: 12px; line-height: 1.45; }
    .lc-capital-flow-panel__references { margin: 10px 0 0; color: oklch(42% 0.018 165); font-size: 12px; line-height: 1.5; }
  </style>
  <h2 class="lc-capital-flow-panel__title" id="lc-capital-flow-title">Capital flow and liquidity</h2>
  <div class="lc-capital-flow-panel__grid">
    <article class="lc-capital-flow-panel__item">
      <span>成交额变化 · prices · 2026-05-15</span>
      <strong>+18.4%</strong>
      <p>Latest five-row average amount is above the prior five-row average.</p>
    </article>
    <article class="lc-capital-flow-panel__item">
      <span>换手率 · daily-metrics · 2026-05-15</span>
      <strong>1.32%</strong>
      <p>Latest returned turnover metric.</p>
    </article>
  </div>
  <p class="lc-capital-flow-panel__references">Public references, if used, are disclosed separately in the source footnote.</p>
</section>
```

## Missing Data Behavior

Do not fabricate amount, volume, turnover, volume ratio, public reference values, dates, or direction labels. If only price/volume data exists, call the section "liquidity evidence" rather than "capital flow". If no flow-related fields are returned, show an empty state and add a `data-gap-notice.md` entry.

## Example

Use with `technical-state-table.md` in candlestick reports and with `framework-scorecard.md` in industry or sector visual reports. Wrap any chart-like flow timeline or heatmap in `chart-frame.md`.
