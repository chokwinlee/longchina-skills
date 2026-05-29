# Analysis Frameworks

Use this reference when a user asks for value, fundamentals, technical analysis, MACD, support and resistance, capital flow, liquidity, relative strength, market breadth, business quality, growth, cash flow, financial health, industry cycle, sector structure, catalyst, peer comparison, margin of safety, how to analyze a stock, or how to analyze an industry or sector.

Select two to four relevant frameworks by default. Use the full list only when the user asks for a comprehensive review or asks how to analyze a stock.

Do not fabricate missing fundamental data. If a framework needs unavailable financial-statement, industry, announcement, or external evidence, label it as a data gap.

## Data Availability Boundary

Current Longchina data can support:

- `prices`: price path, return, volatility, drawdown, volume, and recent movement.
- `daily-metrics`: market value and available daily valuation or liquidity metrics.
- `securities`: symbol resolution, listing status, lifecycle data, and peer universe construction.
- `trading-calendar`: open-date alignment.
- `adjustments`: adjustment assumptions and adjusted-series checks.

Current Longchina data does not fully support income statement, balance sheet, cash-flow statement, segment, dividend, buyback, announcement, news, or industry-cycle evidence unless future datasets provide those fields.

Use `public-reference-sources.md` when the analysis needs official exchange, regulatory, company-filing, Stock Connect, macro-liquidity, macro-cycle, yield-curve, or index-methodology evidence outside Longchina. Keep those sources as dated public references and do not mix them into Longchina rows.

## Professional Fundamental Stack

For a professional single-security or industry review, separate market evidence from business evidence. Use the full stack only when the user asks for a comprehensive report; otherwise select the two to four parts that match the request and available data.

This stack covers business model, competitive advantage, earnings quality, capital allocation, valuation, industry structure, and technical market structure as separate evidence buckets.

- **Business model**: revenue drivers, pricing power, customer concentration, cost structure, and operating leverage. Current Longchina data usually cannot prove these; mark missing revenue, segment, and product evidence as data gaps.
- **Competitive advantage**: brand, network effects, cost advantage, switching costs, licenses, distribution, or supply-chain control. Treat unsupported moat claims as assumptions or external research needs.
- **Growth quality**: revenue growth, profit growth, cash-flow growth, unit economics, reinvestment runway, and whether growth depends on leverage or one-off items.
- **Profitability and DuPont**: ROE split into margin, asset turnover, and leverage when financial-statement data exists. Do not calculate DuPont from market data.
- **ROIC and reinvestment**: return on invested capital, incremental ROIC, reinvestment rate, and capital intensity when balance-sheet and cash-flow fields exist.
- **Earnings quality**: recurring vs one-off profit, accruals, receivables, inventory, provisions, goodwill, and operating cash-flow conversion.
- **Financial health**: leverage, liquidity, debt maturity, working-capital pressure, pledge or guarantee risk, and refinancing sensitivity.
- **Capital allocation**: dividends, buybacks, capex, acquisitions, debt reduction, and whether management reinvests at attractive returns.
- **Valuation**: relative multiples, historical percentile, peer spread, DCF, and SOTP. Use DCF or SOTP only when assumptions are explicit and the user understands they are scenario tools, not facts.
- **Industry structure**: supply-demand, pricing cycle, regulation, substitution, channel inventory, market share, and Porter Five Forces when evidence exists.

## Framework Selection

Use this table to choose the analysis path:

| User intent | Primary frameworks | Current evidence | Data gaps |
| --- | --- | --- | --- |
| "估值贵不贵", "value", "valuation" | value and valuation, margin of safety, peer comparison | `daily-metrics`, `prices`, `securities` | earnings, book value, normalized profit, full valuation ratios when unavailable |
| "成长性", "growth" | growth, catalyst, industry cycle | price and market value context | revenue, profit, cash flow, product, order, or industry data |
| "基本面质量", "quality" | quality, financial health, cash flow | market and trading evidence only | ROE, margin, turnover, leverage, receivables, goodwill, operating cash flow |
| "风险", "下行", "回撤" | risk, margin of safety, financial health | `prices`, `daily-metrics`, `securities` | debt maturity, pledge, balance-sheet stress, event risk |
| "技术面", "MACD", "支撑位" | technical analysis, risk, trend review, relative strength | `prices`, `daily-metrics`, `trading-calendar` | intraday order book, real-time turnover, unreturned historical windows |
| "资金面", "量能", "换手", "北向" | capital flow and liquidity, volume-price confirmation, public reference review | `prices`, `daily-metrics`; optional public references from `public-reference-sources.md` | true net inflow, order-size flow, investor type, real-time Stock Connect flow when unavailable |
| "相对强弱", "跑赢", "行业热度" | relative strength, peer comparison, market breadth | `prices`, `securities`, `daily-metrics`, `trading-calendar` | official benchmark constituents, sector breadth, historical constituent membership unless public reference evidence exists |
| "同行比较" | peer comparison, value and valuation, quality, risk | `securities`, `prices`, `daily-metrics` | financial quality and industry-specific operating metrics |
| "白酒行业", "industry", "sector" | industry cycle, peer comparison, value and valuation, quality, risk | `securities`, `prices`, `daily-metrics` | product prices, channel inventory, market share, revenue, profit, cash flow, policy, and external research |
| "怎么分析" | framework teaching mode | explain available datasets | explain missing evidence |

## Value And Valuation

Purpose: judge whether market pricing looks high, low, or inconclusive relative to available evidence.

Look at:

- Market value and float market value.
- Price trend and return windows.
- Available valuation metrics from `daily-metrics`.
- Valuation percentile only when enough history exists.
- Peer comparison when comparable symbols are available.

Output:

- State whether evidence suggests valuation pressure, valuation discount, or insufficient evidence.
- Do not infer intrinsic value or target price from price data alone.
- Mark missing earnings, book value, or normalized profit as data gaps.

## Growth

Purpose: judge whether business scale and earnings power are expanding.

Look at:

- Revenue, profit, operating cash flow, and unit economics when future datasets provide them.
- Market value and price reaction only as market evidence, not growth proof.
- Catalyst evidence only when the user supplies it or reliable data exists.

Output:

- Explain that price rise is not proof of growth.
- Mark missing financial-statement evidence as a data gap.

## Quality

Purpose: judge business durability and profitability quality.

Look at:

- ROE, margin quality, asset turnover, asset quality, and earnings consistency when available.
- Listing status and trading liquidity as weak supporting evidence only.

Output:

- Do not calculate ROE, margin, or turnover without financial-statement data.
- Use "quality evidence unavailable" rather than substituting price movement.

## Financial Health

Purpose: judge solvency, balance-sheet pressure, and resilience.

Look at:

- Leverage, liquidity, debt maturity, receivables, inventory, goodwill, and contingent liabilities when available.
- Listing status and trading stress as market-side risk evidence.

Output:

- Label missing balance-sheet data clearly.
- Do not infer balance-sheet strength from market value alone.

## Cash Flow

Purpose: judge whether earnings convert into cash and whether the company funds growth sustainably.

Look at:

- Operating cash flow, free cash flow, capex, cash conversion, and dividend capacity when available.

Output:

- Mark cash-flow statement evidence as unavailable when missing.
- Do not use volume or price movement as a cash-flow proxy.

## Risk

Purpose: judge market, liquidity, data, and downside risk.

Look at:

- Return volatility, max drawdown, recent price movement, volume changes, listing status, and missing data.
- `trading-calendar` alignment when date ranges are natural-language ranges.

Output:

- Separate market risk from business risk.
- State missing business-risk evidence when financial or event data is unavailable.

## Technical Analysis

Purpose: summarize price trend, momentum, volatility, volume-price confirmation, and support and resistance without turning chart patterns into trading recommendations.

Look at:

- Trend structure: MA5, MA10, MA20, MA60, MA120 alignment and close position relative to these averages.
- Momentum: MACD(12,26,9), DIF/DEA cross state, MACD histogram direction, RSI zones, KDJ zones, BOLL band position, recent gap behavior, and range position when enough OHLC rows exist.
- Support and resistance: recent swing lows and swing highs, clustered price levels, touches, recency, and distance from latest close.
- Volume-price confirmation: whether upward or downward moves are accompanied by higher volume or amount versus the prior comparable window.
- Liquidity and turnover: amount, volume, turnover rate, free-float turnover rate, and volume ratio when returned.
- Relative strength: return spread versus an explicit benchmark, peer median, or selected peer group after aligning open dates.
- Risk context: maximum drawdown, annualized volatility, recent range position, and whether a level is based on too few observations.

Output:

- State technical facts as current structure, not prediction: for example, "MACD remains below DEA" or "latest close sits near the nearest resistance cluster."
- Label nearest support below the latest close and nearest resistance above it only when derived from returned OHLC rows.
- Do not label support and resistance as buy, sell, stop-loss, breakout, or target-price instructions.
- Mark support/resistance unavailable when the returned range is too short or has too few swing points.
- Say "liquidity evidence" when only amount, volume, or turnover is available; do not call it net inflow or main-fund flow.
- Keep technical analysis separate from fundamental value; a technically strong chart does not prove business quality.

## Capital Flow And Liquidity

Purpose: describe whether recent participation and tradability are expanding or contracting, while separating observable liquidity proxies from unavailable true fund-flow evidence.

Look at:

- `prices.amount` and `prices.volume`: latest level, rolling average change, spike days, and whether changes line up with price direction.
- `daily-metrics.turnover_rate`, `daily-metrics.free_float_turnover_rate`, and `daily-metrics.volume_ratio` when returned.
- Public reference evidence from `public-reference-sources.md` for Stock Connect shareholding snapshots, ETF or fund context, exchange market statistics, or macro-liquidity data when the user asks for northbound, fund, or market-wide capital context.

Output:

- Separate "observable liquidity" from "capital-flow reference evidence."
- Do not label volume, amount, turnover, or volume ratio as true net inflow, main-fund inflow, smart money, or institutional buying.
- State the date and source for every public reference value.
- If only Longchina price and metric rows are available, say the answer covers liquidity and participation, not investor identity or true flow.

## Relative Strength

Purpose: compare recent performance against an explicit benchmark, sector, peer median, or selected peer group.

Look at:

- Aligned return windows from `prices`.
- Peer universe from `securities` when the user asks for industry or sector comparison.
- Market value, float market value, and available valuation context from `daily-metrics`.
- Index methodology or constituents from public references only when the benchmark definition matters.

Output:

- Show subject return, comparison return, spread, date range, and whether the benchmark is a formal index, peer median, or user-selected set.
- Do not infer future leadership from past relative strength.
- Mark benchmark or peer-universe uncertainty as a data gap when the source is not explicit.

## Market Breadth And Sentiment

Purpose: judge whether a move is broad, narrow, liquid, or concentrated across a peer universe.

Look at:

- Count and share of peers with positive returns over aligned windows.
- Median and dispersion of peer returns.
- Peer volume or amount expansion when available.
- Public exchange market statistics when the user asks for market-wide breadth outside a Longchina peer universe.

Output:

- Separate universe construction from conclusions.
- Show sample size and filtering rules.
- Do not generalize from a small or convenience peer set to the whole A-share market.

## Peer Comparison

Purpose: judge relative valuation, scale, liquidity, and risk against comparable securities.

Look at:

- Peer universe from `securities`.
- Price and return windows from `prices`.
- Market value and available metrics from `daily-metrics`.
- Listing status and latest available date per row.

Output:

- Use row-level dates when peers have different latest data.
- Do not rank peers on unavailable financial quality metrics.
- Mark missing peer fields with explicit data-gap notes.

## Industry Cycle

Purpose: judge where the business sits in policy, supply-demand, and pricing cycles.

Look at:

- Industry, policy, supply-demand, product-price, or external research data when available.
- For China sector requests, use `securities` to define the listed universe, then use `prices` and `daily-metrics` to describe market performance, valuation, scale, liquidity, and peer dispersion.

Output:

- Treat industry-cycle claims as external research unless supported by data.
- Do not infer industry cycle from one security's price alone.
- For requests like 白酒行业, separate listed-market evidence from missing operating evidence such as channel inventory, wholesale prices, product mix, market share, revenue, profit, and cash flow.

## Catalyst

Purpose: identify events that could change market expectations.

Look at:

- Earnings releases, dividend, buyback, policy, product, capacity, litigation, or other event evidence when available.

Output:

- Do not invent announcements, news, or events.
- If no event data is available, say catalyst evidence is unavailable.

## Margin Of Safety

Purpose: judge whether downside risk appears cushioned by valuation, business resilience, and evidence quality.

Look at:

- Valuation discount when valuation data exists.
- Drawdown and range position from `prices`.
- Financial health and business quality only when fundamental evidence exists.
- Data gaps as negative evidence quality.

Output:

- Do not promise returns or a target price.
- Distinguish price-based downside evidence from fundamental safety evidence.

## Teaching Mode

When the user asks how to analyze a stock, explain:

1. What the selected frameworks answer.
2. Which Longchina datasets can support them.
3. Which evidence is missing.
4. What conclusion is supported and what remains unknown.

Keep teaching concise. Do not turn every stock answer into a textbook unless the user asks for a full framework walkthrough.

## Visualization Handoff

Do not trigger visualization from framework selection alone. Use `stock-visualization` only when the user explicitly asks for visualization, chart, K-line, candlestick, or HTML report, or when durable memory says visual reports are the default and the user has not opted out.

When a visual artifact is allowed, prefer framework visual components that show both available evidence and missing evidence.
