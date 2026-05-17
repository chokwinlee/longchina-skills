---
name: stock-visualization
description: Use when a user wants to turn longchina A-share data into offline HTML stock visualizations, comparison reports, trend reports, sortable metric tables, or reusable stock chart/table components.
---

# Stock Visualization

Use this skill to convert real `longchina` A-share data into offline, single-file HTML reports and reusable visualization components.

This skill is for visualization, not data retrieval and not default investment advice. Use `longchina-data` first whenever the user needs real prices, indicators, security names, trading dates, or usage metadata.

## Required Workflow

1. Use `longchina-data` to verify runtime status and fetch real data.
2. Read `references/data-contracts.md` before reshaping rows.
3. Read `references/indicator-rules.md` before calculating derived indicators.
4. Read `references/html-constraints.md` before writing HTML.
5. Read `references/rendering-helpers.md` before drawing chart coordinates, formatting numbers, or writing sortable tables.
6. Choose component specs from `components/` and optional composition guides from `recipes/`.
7. Generate one offline, self-contained HTML file unless the user explicitly asks for a fragment.
8. Include the Source Footnote component on every generated page.
9. Include data source, fields, filters, date range, generation time, missing-data notes, and risk notes.

## Component Model

Components are reusable HTML/CSS/JS snippets, not fixed templates. Agents may arrange them freely as long as the data contracts, source disclosure, and offline HTML constraints are preserved.

P0 components:

- `components/price-trend.md`
- `components/metric-series.md`
- `components/comparison-card.md`
- `components/comparison-matrix.md`
- `components/sortable-table.md`
- `components/source-footnote.md`

## Recipes

Recipes are composition guides inside this skill:

- `recipes/stock-compare.md` for two-stock or multi-stock light fundamental comparisons.
- `recipes/trend-report.md` for price and metric movement reports.
- `recipes/metric-table.md` for sortable metric tables over a user stock pool or constrained market subset.

Recipes do not limit composition. If the user asks for a custom page, combine the needed components directly.

## Guardrails

- Do not fabricate prices, names, financial values, trading dates, returned rows, or usage data.
- Do not hide missing data. Show it locally and explain it in the source footnote.
- Do not depend on CDN libraries, external scripts, remote fonts, remote images, or remote stylesheets.
- Do not put strategy logic inside visualization components.
- Do not produce buy, sell, or hold recommendations by default.
- If the user explicitly asks for an investment view, label assumptions, source dates, and risks. Do not promise returns or certainty.

## Useful References

- `references/data-contracts.md`: standard input shapes.
- `references/indicator-rules.md`: calculations agents perform before rendering.
- `references/html-constraints.md`: offline HTML and product UI design rules.
- `references/rendering-helpers.md`: data-to-SVG, table sorting, and display formatting rules.
- `references/compliance.md`: source disclosure and investment-view rules.
- `examples/stock-compare-input.json`: normalized example input.
- `examples/stock-compare.html`: complete offline example output.
