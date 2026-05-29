# Framework Research Report Recipe

## Purpose

Use this recipe only after the Invocation Gate is satisfied and `stock-research-intake` selects a visual artifact. Build a source-first stock, industry or sector visual report that combines value, fundamental, technical, capital-flow/liquidity, relative-strength, peer, scenario, margin-of-safety, and data-gap evidence without making investment recommendations.

## Required Components

Compose these components:

1. `chart-frame.md`
2. `framework-scorecard.md`
3. `data-gap-notice.md`
4. `fundamental-evidence-panel.md`
5. `technical-state-table.md` when price-derived technical evidence is part of the plan
6. `technical-levels-panel.md` when support/resistance evidence is requested or useful
7. `capital-flow-panel.md` when liquidity, turnover, amount, volume ratio, or public reference flow evidence is part of the plan
8. `relative-strength-panel.md` when benchmark or peer return-spread evidence is part of the plan
9. `peer-factor-heatmap.md`
10. `peer-rank-table.md`
11. `scenario-assumption-table.md`
12. `scenario-range-panel.md`
13. `margin-of-safety-panel.md`
14. `source-footnote.md`

## Input Contract

Fetch or receive explicit inputs before rendering:

- `securities` for `symbol`, `name`, `industry`, `exchange`, `market`, and `listing_status`.
- `prices` for `symbol`, `date`, `close`, `previous_close`, `percent_change`, and `volume`.
- `daily-metrics` for `symbol`, `date`, valuation metrics, `total_market_value`, and `float_market_value`.
- `trading-calendar` only when natural-language dates must be resolved to open dates.
- Public references selected by `stock-research-intake/references/public-reference-sources.md` only when the report needs filings, exchange statistics, Stock Connect context, macro liquidity, macro cycle data, yield curves, or index methodology.
- User-supplied or otherwise explicit scenario assumptions.

Every component input must keep row dates visible where values are compared or ranked.

## Layout

1. Report title, requested symbols, and analysis date range.
2. `framework-scorecard.md` for framework status.
3. `data-gap-notice.md` when any requested evidence is unavailable.
4. `fundamental-evidence-panel.md` for available and missing fundamental evidence.
5. Technical section with `technical-state-table.md` and `technical-levels-panel.md` when the plan includes chart structure.
6. Capital-flow and relative-strength section with `capital-flow-panel.md` and `relative-strength-panel.md` when those evidence buckets are selected.
7. Peer section with `chart-frame.md` around `peer-factor-heatmap.md` and a separate `peer-rank-table.md`.
8. Scenario section with `scenario-assumption-table.md` followed by `chart-frame.md` around `scenario-range-panel.md`.
9. Margin-of-safety section with `margin-of-safety-panel.md`.
10. `source-footnote.md` as the final block.

## Missing Data Behavior

Do not fabricate values, assumptions, peer sets, ranks, scenario outputs, downside ranges, flow values, benchmark rows, public reference values, or dates. Render missing evidence in the relevant component, add a `data-gap-notice.md` entry for material omissions, and repeat the limitation in `source-footnote.md`.

## Risk Language

Always state that the report is not investment advice. Do not provide buy, sell, or hold recommendations; guaranteed upside or downside; certainty language; or fabricated target prices or expected returns. Scenario ranges are allowed only when they are based on explicit user-supplied assumptions or clearly labeled assumptions, and they must be described as assumptions, not forecasts.

## Example

Use this recipe for a visual artifact selected by `stock-research-intake`, such as an industry or sector visual report over a listed peer universe, or a framework research HTML report comparing one requested symbol against an explicit peer set with dated evidence from `prices`, `daily-metrics`, and `securities`.
