---
name: stock-research-intake
description: Use when a user asks for broad A-share stock or industry/sector research, fundamental/value/technical analysis, frameworks, how to analyze a stock or sector, or when the analysis intent, output format, or visualization need is unclear.
---

# Stock Research Intake

Use this skill before data retrieval or visualization when a stock, A-share industry, or sector request is open-ended.

This skill plans the work. It does not fetch data, render charts, or produce buy, sell, or hold recommendations.

## Required Workflow

1. Read local memory with `scripts/longchina_memory.py read` before planning.
2. Classify the user request as trend review, technical analysis, valuation review, fundamental or value framework review, risk review, peer comparison, industry or sector review, annual performance, table-only screening, visualization report, teaching request, or custom research.
3. Read `references/analysis-frameworks.md` when users ask about value, fundamentals, technical analysis, MACD, support/resistance, moving averages, capital flow, liquidity, relative strength, market breadth, business quality, growth, cash flow, financial health, industry cycle, sector structure, catalysts, peer comparison, margin of safety, or how to analyze a stock or sector.
4. Read `references/public-reference-sources.md` when Longchina data is not enough and the user asks for official public evidence such as filings, exchange market statistics, Stock Connect, macro liquidity, macro cycle data, yield curves, or index methodology.
5. Prefer stored preferences and sensible defaults over repeated clarification questions.
6. Ask at most one clarification question when the missing information blocks a responsible plan.
7. Use `longchina-data` after symbol, scope, and dataset needs are clear enough.
8. Use `stock-visualization` only when the user explicitly asks for visualization, chart, K-line, candlestick, HTML report; when durable memory says visual reports are the default; or when the request is a default-visual case below.
9. Do not route to `stock-visualization` only because data rows were fetched; route when the analysis structure is chart-worthy.
10. At task end, save stable preferences with `scripts/longchina_memory.py` and briefly report material memory updates.

## Default Plan For Broad Requests

For a broad single-security request, default to:

- User's stored language preference, or Chinese when the user writes in Chinese.
- Recent one-year range.
- Two to four relevant frameworks from `references/analysis-frameworks.md`, usually valuation, technical analysis, risk, peer comparison, or margin of safety when data supports them.
- Concise conclusion first, followed by evidence.
- Text and compact tables first for non-technical analysis.
- No HTML visualization for broad non-technical single-security analysis unless requested or stored as a durable preference. Use `stock-visualization` by default for single-security technical analysis when OHLC rows are available.

For a broad industry or sector request, default to:

- Treat the request as China A-share industry research when the user names a China industry such as 白酒行业.
- Use `securities` to define the listed peer universe when possible.
- Use `prices` and `daily-metrics` for market performance, valuation, market value, liquidity, and peer dispersion.
- Use `references/analysis-frameworks.md` for industry cycle, peer comparison, value, quality, risk, and data-gap framing.
- Label missing industry operating data, channel data, policy data, financial statements, news, or external research as data gaps.
- Use `stock-visualization` by default for broad industry or sector reviews after fetching enough peer rows for comparison.
- Do not ask whether visualization is needed before routing these default-visual cases.
- Skip the visual only when the user asks for text-only output, durable memory says to avoid visuals, or returned data is too sparse for a truthful chart.

## Default Proactive Visualization

Default to a compact visual artifact, without asking for permission, when the request naturally needs comparison or structure:

- Broad industry or sector reviews.
- Peer comparisons with two or more securities, including explicit pair comparisons such as 茅台 vs 五粮液.
- Single-security technical analysis where OHLC rows support K-line, MACD, moving averages, support/resistance, or volume-price structure.
- Capital-flow or liquidity reviews where amount, volume, turnover, volume ratio, or official public reference evidence needs to be separated from price action.
- Relative-strength reviews where benchmark or peer comparison is central to the answer.
- Multi-metric framework analysis with valuation, performance, risk, and missing-evidence dimensions.
- Annual performance reviews where price path, drawdown, return windows, and valuation context are all present.

For these cases, plan one visual handoff to `stock-visualization` after data retrieval. For explicit pair comparisons, prefer `recipes/stock-compare.md` with side-by-side comparison cards, a relative-strength panel, a compact metric table, and a data-gap notice. For larger peer sets, prefer visual reports that combine a peer heatmap, rank table, scorecard, and data-gap notice. Keep the text answer concise and let the visual artifact carry the dense comparison.

For technical-analysis default-visual cases, use `stock-visualization` with `recipes/candlestick-report.md`, `components/technical-state-table.md`, `components/technical-levels-panel.md`, `components/capital-flow-panel.md` when liquidity or capital-flow evidence is requested, and `components/relative-strength-panel.md` when benchmark comparison is requested. Do not ask whether visualization is needed before routing these default-visual cases; skip the visual only when the user requests text-only output, durable memory says to avoid visuals, or returned OHLC data is too sparse for a truthful chart.

The visual handoff must preserve stock-visualization delivery defaults: open the finished offline HTML in the Codex in-app Browser first, use the user's system default browser only as a fallback, and do no automatic Playwright or screenshot validation unless the user explicitly asks for render debugging or the report fails to open.

## One-Question Policy

Ask only when blocked:

- The security is missing or ambiguous.
- The industry or sector label cannot be mapped to a usable listed universe and no sensible default exists.
- The user requests comparison but provides no comparison target and no stored benchmark preference exists.
- The user requests personalized holding or portfolio analysis but no relevant profile context exists.
- The request is high impact and the analysis framing cannot be inferred.

Use `references/question-patterns.md` for concise question text.

## Memory Rules

Read `references/memory-policy.md` before writing memory.

Use the memory helper command contract from `references/memory-policy.md` for `read`, `summarize`, user preference entries, agent memory entries, and fact ledger updates.

Save stable preferences proactively:

- Communication style and output format.
- Analysis angle and default period.
- Visualization default.
- Investment horizon, risk tolerance, capital context, and holding context when the user states them clearly.

Do not save credentials, raw data dumps, temporary task progress, or automated trading instructions.

## Routing Rules

Read `references/analysis-routing.md` when deciding which datasets or downstream skills are needed.

For value, fundamentals, technical analysis, capital flow, liquidity, relative strength, market breadth, quality, growth, cash flow, financial health, industry cycle, sector structure, catalysts, peer comparison, margin of safety, or teaching requests, read `references/analysis-frameworks.md`. Use available Longchina data as evidence and label missing financial-statement, industry, announcement, investor-flow, or external evidence as data gaps.

For official public reference evidence outside Longchina, read `references/public-reference-sources.md`. Keep those references separate from Longchina rows and include source name, URL, retrieved date, publication date when visible, evidence used, and limitation.

Use Longchina public dataset names:

- `prices`
- `daily-metrics`
- `securities`
- `trading-calendar`
- `adjustments`

Use public field and filter names such as `symbol`, `date`, `previous_close`, `percent_change`, `volume`, `total_market_value`, `float_market_value`, `listing_status`, `previous_open_date`, and `adjustment_multiplier`.

## References

- `references/memory-policy.md`: local memory save, skip, replace, and forget rules.
- `references/question-patterns.md`: concise intake questions and default statements.
- `references/analysis-routing.md`: intent-to-dataset and downstream skill routing.
- `references/analysis-frameworks.md`: value, fundamental, industry, sector, peer, scenario, data-gap, and teaching frameworks.
- `references/public-reference-sources.md`: official public reference source selection and disclosure rules.
