# Analysis Routing

Use this file to choose Longchina datasets and downstream skills after the intake plan is clear.

## Fundamental And Value Frameworks

Use `analysis-frameworks.md` for value, fundamentals, technical analysis, business quality, growth, cash flow, financial health, industry cycle, catalyst, peer comparison, margin of safety, and how-to-analyze requests.

Use `public-reference-sources.md` when a responsible answer needs official public evidence outside Longchina, such as company filings, exchange market statistics, Stock Connect shareholding context, macro liquidity, macro cycle data, bond-yield assumptions, or index methodology.

Use current Longchina datasets only as available evidence:

- `prices` for price path, returns, volatility, drawdown, volume, and range position.
- `daily-metrics` for available market value, float market value, liquidity, and valuation context.
- `securities` for symbol resolution, listing status, lifecycle data, and peer universe construction.
- `trading-calendar` for open-date alignment.
- `adjustments` for adjustment assumptions.

Mark income statement, balance sheet, cash-flow statement, industry, announcement, catalyst, and external research evidence as data gaps when unavailable. Do not fabricate missing fundamental data.

Keep public reference evidence separate from Longchina data. Include source name, URL, retrieved date, publication date when visible, evidence used, and limitations. Do not map public reference values into Longchina rows unless a tested adapter exists.

## Industry Or Sector Review

Use this route for requests such as "分析中国白酒行业", "China liquor sector analysis", or broad A-share sector research.

Use `longchina-data` with:

- `securities` to build a listed universe by industry, exchange, market, and listing status.
- `prices` for peer price paths, returns, volatility, drawdown, volume, and range position.
- `daily-metrics` for market value, float market value, liquidity, and available valuation context.
- `trading-calendar` when sector windows need open-date alignment.

Use `analysis-frameworks.md` for industry cycle, sector structure, peer comparison, value, quality, and risk framing. Mark product prices, channel inventory, revenue, profit, cash flow, policy, news, and external research as data gaps unless available from explicit inputs or future datasets.

## Proactive Visualization Handoff

Use `stock-visualization` by default for a broad industry or sector review after `securities`, `prices`, and `daily-metrics` produce enough peer rows for comparison. Do not ask whether visualization is needed first unless the user requested text-only output or durable memory says to avoid visuals.

For the visual plan, prefer `recipes/framework-research-report.md` with `peer-factor-heatmap.md`, `peer-rank-table.md`, `framework-scorecard.md`, and `data-gap-notice.md`. Use `recipes/stock-compare.md` for a smaller explicit peer set and `recipes/metric-table.md` when the main output is a sortable table.

Carry stock-visualization delivery defaults into the handoff: open the finished offline HTML in the Codex in-app Browser first, use the user's system default browser only as a fallback, with no automatic Playwright or screenshot validation unless the user explicitly asks for render debugging or the report fails to open.

## Trend Review

Use `longchina-data` with:

- Dataset: `prices`
- Filters: `symbol`, `date` range
- Fields: `symbol`, `date`, `previous_close`, `percent_change`, `volume`

Use `stock-visualization` only when the user asks for a chart, K-line, candlestick, or HTML report, or when durable memory says visual reports are the default and the user has not opted out.

## Technical Analysis

Use this route for requests such as "看技术面", "MACD 怎么样", "支撑位和压力位在哪里", or chart-structure questions.

Use `longchina-data` with:

- Dataset: `prices`
- Filters: `symbol`, enough `date` history for the requested lookback
- Fields: `symbol`, `date`, `open`, `high`, `low`, `close`, `previous_close`, `percent_change`, `volume`, `amount`
- Dataset: `trading-calendar` when natural dates need open-date alignment

Read `analysis-frameworks.md` for Technical Analysis. Calculate MACD, moving averages, RSI/KDJ/BOLL only from returned rows. Derive support and resistance from swing-high and swing-low clusters; if the returned period is too short, label the level evidence unavailable instead of inventing a level.

Use `stock-visualization` by default for technical analysis after enough OHLC rows are returned. Prefer `candlestick-report.md` with MA overlays, MACD, optional RSI/KDJ/BOLL, `technical-state-table.md`, `technical-levels-panel.md`, `capital-flow-panel.md` when amount or turnover evidence is requested, and `relative-strength-panel.md` when a benchmark or peer comparison is part of the question. Do not ask whether visualization is needed first; skip only when the user asks for text-only output, durable memory says to avoid visuals, or returned OHLC data is too sparse for a truthful chart.

## Capital Flow And Liquidity Review

Use this route for requests such as "看资金面", "量能怎么样", "换手是否放大", "北向资金怎么看", "是否放量", or liquidity participation questions.

Use `longchina-data` with:

- Dataset: `prices`
- Filters: `symbol`, enough `date` history for the requested lookback
- Fields: `symbol`, `date`, `open`, `high`, `low`, `close`, `previous_close`, `percent_change`, `volume`, `amount`
- Dataset: `daily-metrics`
- Fields: `symbol`, `date`, `turnover_rate`, `free_float_turnover_rate`, `volume_ratio`, `total_market_value`, `float_market_value`
- Dataset: `trading-calendar` when natural dates need open-date alignment

Read `analysis-frameworks.md` for Capital Flow And Liquidity. Use amount, volume, turnover, and volume ratio as liquidity proxies only. If the user asks for Stock Connect, ETF, fund, macro liquidity, or investor-type evidence that Longchina does not return, read `public-reference-sources.md` and cite official public references as external context.

Use `stock-visualization` by default for capital-flow technical reviews when enough rows are returned. Prefer `candlestick-report.md` with `capital-flow-panel.md`, `technical-state-table.md`, and a source footnote that separates Longchina rows from public references.

## Relative Strength Review

Use this route for requests such as "是否跑赢行业", "相对强弱", "和指数比", "行业热度", or peer strength questions.

Use `longchina-data` with:

- Dataset: `prices`
- Filters: `symbol`, `date` range for the subject and benchmark or peer set
- Fields: `symbol`, `date`, `close`, `previous_close`, `percent_change`, `volume`, `amount`
- Dataset: `securities` for peer universe construction when the comparison is industry or sector based
- Dataset: `daily-metrics` for market value, float market value, turnover, and available valuation context
- Dataset: `trading-calendar` for open-date alignment

Read `analysis-frameworks.md` for Relative Strength. Use public index methodology or constituents from `public-reference-sources.md` only when the benchmark definition is material and not already explicit.

Use `stock-visualization` when two or more peer rows, an explicit pair comparison, or a benchmark comparison are present. For explicit pair comparisons, prefer `recipes/stock-compare.md`, `relative-strength-panel.md`, `benchmark-comparison.md`, a compact metric table, and `source-footnote.md`. For larger peer sets, add `peer-rank-table.md` when the ranking signal is meaningful.

## Valuation Review

Use `longchina-data` with:

- Dataset: `daily-metrics`
- Filters: `symbol`, `date` range
- Fields: `symbol`, `date`, `total_market_value`, `float_market_value`

Combine with `prices` when the user also asks about price movement.

## Risk And Drawdown Review

Use `prices` to compute return, drawdown, volatility, and recent movement from returned rows. Use `trading-calendar` when natural date ranges need open-date alignment.

## Peer Comparison

Use `securities` to resolve names, lifecycle data, and listing status. Use `prices` and `daily-metrics` for comparable price and metric windows. Use `listing_status` when filtering active securities.

When a peer comparison has two or more securities, include a `stock-visualization` handoff unless the user asks for text-only output or durable memory says to avoid visuals. For two-security comparisons, keep the visual compact: side-by-side comparison cards, relative strength, return windows, valuation or liquidity rows when available, and clear data-gap notes.

## Annual Performance

Use `prices` for the annual price path and `daily-metrics` for valuation context. Use `trading-calendar` to align the actual open trading range. Route to `stock-visualization` only when the user asks for a visual annual report or durable preference enables one.

## Adjustments

Use `adjustments` and `adjustment_multiplier` when the user asks about adjustment factors or adjusted series assumptions.

## Table-Only Screening

Use `securities` and `daily-metrics` with explicit limits. Prefer text or CSV output unless visualization is requested.

## Visualization Report

When the plan calls for a visual report, use `stock-visualization` after fetching authoritative data. The report should include source datasets, filters, fields, date ranges, missing-data notes, and risk notes.
