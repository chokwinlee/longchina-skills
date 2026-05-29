---
name: stock-visualization
description: Use when turning longchina A-share market data into visual outputs, including OHLC candlestick reports, technical-indicator views, benchmark comparisons, valuation charts, sortable tables, or offline HTML artifacts.
---

# Stock Visualization

Use this skill to convert real `longchina` A-share data into offline, single-file HTML reports and reusable visualization components.

For stock price movement, default to an interactive candlestick report, not a close-price line. Use the vendored `lightweight-charts` browser bundle for shareable single-file HTML when OHLC rows are available.

For one-year or annual stock performance requests, use `recipes/annual-performance-report.md` and calculate report-level metrics from `references/annual-report-calculations.md`. These reports should combine candlesticks with return windows, drawdown, valuation context, benchmark comparison, relative strength, capital-flow/liquidity evidence, event timeline, technical state, support/resistance levels, and an agent brief.

This skill is for visualization, not data retrieval and not default investment advice. Use `longchina-data` first whenever the user needs real prices, indicators, security names, trading dates, or usage metadata.

## Invocation Gate

Do not generate a visual report merely because stock data was fetched.

Use this skill only when:

- The user explicitly asks for visualization, chart, graph, K-line, candlestick, HTML report, visual comparison, or a visual table.
- `stock-research-intake` has produced a task plan that includes a visual artifact.
- `stock-research-intake` has produced industry or sector visual plans, peer comparison visual plans, technical-analysis visual plans, or multi-metric framework visual plans where a compact visual artifact is the default.
- Durable user memory says broad stock analysis should include visual reports by default and the user did not opt out.

For broad stock analysis where output format is unclear, return to `stock-research-intake` before creating HTML.

## Required Workflow

1. Use `longchina-data` to verify runtime status and fetch real data.
2. Read `references/data-contracts.md` before reshaping rows.
3. Read `references/indicator-rules.md` before calculating derived indicators.
4. Read `references/annual-report-calculations.md` before filling annual performance reports or return, drawdown, valuation, benchmark, volatility, and technical-state fields.
5. Read `references/html-constraints.md` before writing HTML.
6. Read `references/chart-engine.md` before creating an interactive candlestick report.
7. Read `references/rendering-helpers.md` before drawing fallback chart coordinates, formatting numbers, or writing sortable tables.
8. Choose component specs from `components/` and optional composition guides from `recipes/`.
9. For daily A-share OHLC data, prefer `components/candlestick-chart.md` with volume, MACD, optional KDJ panes, and `components/technical-levels-panel.md` when the user asks for support/resistance or technical analysis.
10. Use `components/capital-flow-panel.md` when a report includes amount, volume, turnover, volume ratio, Stock Connect reference evidence, or liquidity participation analysis.
11. Use `components/relative-strength-panel.md` when a report compares a subject against a benchmark, peer median, industry, or explicit peer set.
12. Use `components/price-trend.md` only for non-OHLC series, indexed comparisons, or fallback static output.
13. Generate one offline, self-contained HTML file unless the user explicitly asks for a fragment.
14. Include the Source Footnote component on every generated page.
15. Include data source, fields, filters, date range, generation time, missing-data notes, public reference disclosures, and risk notes.

## Delivery Defaults

After writing the HTML report, open the finished local file in the Codex in-app Browser first. Prefer the built-in browser so the user can inspect the offline report inside the agent workspace. Navigate to the `file://` URL for the absolute report path when Browser is available.

Use the user's system default browser only as a fallback when the built-in browser is unavailable, cannot load the `file://` URL, or the user explicitly asks for an external browser. On macOS, the fallback command is `open`:

```bash
open "/absolute/path/to/report.html"
```

Do not run screenshot or browser automation checks by default. Do not start a local static server for a single-file offline report. The report must be usable directly from `file://`.

Keep default verification lightweight: confirm the file was written, required source/risk notes are present, no remote runtime assets are referenced, and the output path is clear. Use Browser, Playwright, screenshots, or a local server only when the user explicitly asks for render debugging, the file fails to open, or you are changing shared visualization components and need deeper regression testing.

For Longchina generated report artifacts, this delivery rule overrides generic frontend visual-regression habits. Do not call Playwright as a post-generation acceptance step. No automatic desktop/mobile screenshot pass, console-warning sweep, or pixel check should run after ordinary report generation.

If another skill suggests screenshot verification, ignore that suggestion for this skill unless the user explicitly asks for visual regression/debugging or the report fails to open. In that exceptional case, run one targeted check and do not create screenshot artifacts unless needed to explain a rendering bug.

## Component Model

Components are reusable HTML/CSS/JS snippets, not fixed templates. Agents may arrange them freely as long as the data contracts, source disclosure, and offline HTML constraints are preserved.

Wrap every chart, heatmap, matrix, bubble or scatter plot, and chart-like visual table in `components/chart-frame.md` so it uses shared fullscreen behavior, edge-safe label padding, and consistent chart actions.

P0 components:

- `components/chart-frame.md`
- `components/candlestick-chart.md`
- `components/indicator-pane.md`
- `components/chart-tooltip.md`
- `components/price-trend.md`
- `components/metric-series.md`
- `components/performance-summary-strip.md`
- `components/return-window-table.md`
- `components/drawdown-panel.md`
- `components/valuation-band-chart.md`
- `components/benchmark-comparison.md`
- `components/event-timeline.md`
- `components/technical-state-table.md`
- `components/technical-levels-panel.md`
- `components/capital-flow-panel.md`
- `components/relative-strength-panel.md`
- `components/agent-brief.md`
- `components/comparison-card.md`
- `components/comparison-matrix.md`
- `components/sortable-table.md`
- `components/source-footnote.md`
- `components/framework-scorecard.md`
- `components/fundamental-evidence-panel.md`
- `components/margin-of-safety-panel.md`
- `components/data-gap-notice.md`
- `components/peer-factor-heatmap.md`
- `components/peer-rank-table.md`
- `components/scenario-assumption-table.md`
- `components/scenario-range-panel.md`

## Recipes

Recipes are composition guides inside this skill:

- `recipes/candlestick-report.md` for K-line, 蜡烛图, TradingView-style, or technical-indicator stock reports with optional support/resistance, capital-flow/liquidity, and relative-strength panels.
- `recipes/annual-performance-report.md` for 最近一年, one-year performance, annual review, and full stock performance reports.
- `recipes/stock-compare.md` for two-stock or multi-stock light fundamental comparisons.
- `recipes/trend-report.md` for price and metric movement reports.
- `recipes/metric-table.md` for sortable metric tables over a user stock pool or constrained market subset.
- `recipes/framework-research-report.md` for industry, sector, and stock visual reports that combine value, fundamental, peer, scenario, margin-of-safety, and data-gap evidence after `stock-research-intake` selects a visual artifact.

Recipes do not limit composition. If the user asks for a custom page, combine the needed components directly.

## Guardrails

- Do not fabricate prices, names, financial values, trading dates, returned rows, or usage data.
- Do not hide missing data. Show it locally and explain it in the source footnote.
- Do not depend on CDN libraries, external scripts, remote fonts, remote images, or remote stylesheets.
- Do not use a line chart as the primary view for OHLC stock prices when candle rows are available.
- Do not put strategy logic inside visualization components.
- Do not produce buy, sell, or hold recommendations by default.
- If the user explicitly asks for an investment view, label assumptions, source dates, and risks. Do not promise returns or certainty.

## Useful References

- `references/data-contracts.md`: standard input shapes.
- `references/indicator-rules.md`: calculations agents perform before rendering.
- `references/annual-report-calculations.md`: formulas for annual returns, benchmark alignment, drawdown, volatility, valuation percentiles, and technical states.
- `references/html-constraints.md`: offline HTML and product UI design rules.
- `references/chart-engine.md`: vendored `lightweight-charts` usage and inlining rules.
- `references/rendering-helpers.md`: data-to-SVG, table sorting, and display formatting rules.
- `references/compliance.md`: source disclosure and investment-view rules.
- `examples/candlestick-report-input.json`: normalized OHLCV and indicator example input.
- `examples/candlestick-report.html`: complete offline interactive candlestick example.
- `examples/stock-compare-input.json`: normalized example input.
- `examples/stock-compare.html`: complete offline example output.
