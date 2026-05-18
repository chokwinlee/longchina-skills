# Annual Performance Report Recipe

Use this recipe when the user asks for 最近一年表现, one-year performance, annual review, yearly stock report, or a full stock performance report.

## When To Use

- "生成中国平安最近一年的表现报告."
- "Show 601318.SH one-year performance with valuation and benchmark."
- "给我一份股票年度表现可视化报告."

## Datasets To Query

Use `longchina-data` and fetch:

- `stock-basic` for identity and listing metadata.
- `daily` for one year of OHLCV rows.
- `daily-basic` for PE TTM, PB, turnover, market value, and other available daily metrics.
- `trade-cal` to resolve natural start/end dates into trading days.
- Benchmark rows only when the user supplies a benchmark dataset or the longchina runtime exposes one. Do not fabricate benchmark values.
- Filing, dividend, or event rows only when those datasets are available or the user supplies them.

## Data Contracts

Read `references/annual-report-calculations.md` before filling summary, return-window, drawdown, valuation, benchmark, volatility, and technical-state values.

Fill:

- `AnnualPerformanceReport`.
- `SecurityProfile`.
- `CandlePoint`.
- `OverlaySeries` for MA5, MA10, MA20, MA60, and MA120.
- `IndicatorPaneSeries` for volume and optional MACD/KDJ.
- `TooltipSnapshot`.
- `SourceDisclosure`.

## Calculation Rules

- Calculate report-level values from returned rows according to `references/annual-report-calculations.md`.
- Resolve natural date ranges to the actual first and last returned trading rows.
- Calculate return windows from trading-row offsets, not calendar-day guesses.
- Align benchmark rows by `trade_date` before calculating benchmark returns, indexed benchmark series, or excess return.
- Use close-to-close running peaks for drawdown and recovery date.
- Calculate volatility from close-to-close daily returns and annualize with `sqrt(252)`.
- Calculate valuation current/min/max/percentile from valid `daily-basic` values inside the report period.
- Keep technical state factual. Do not turn MA, MACD, KDJ, BOLL, or RSI states into buy/sell/hold advice.
- Do not perform unit conversion for amount, volume, market value, or valuation fields unless the source unit is known and stated in the footnote.

## Components

Compose:

1. `performance-summary-strip.md`.
2. `candlestick-chart.md` with one-year candles, volume, and moving averages.
3. `return-window-table.md`.
4. `drawdown-panel.md`.
5. `valuation-band-chart.md`.
6. `benchmark-comparison.md` when benchmark data exists.
7. `event-timeline.md` when event data exists.
8. `technical-state-table.md`.
9. `agent-brief.md`.
10. `source-footnote.md`.

## Layout

Follow the repository design language:

- deep research-console background,
- serif report heading,
- mono metadata labels,
- copper section tags,
- 0.5px or 1px dividers,
- dense tables,
- chart first, explanation second,
- no decorative card grid.

Recommended page order:

1. Header: company, ts_code, one-year period, generated timestamp.
2. Summary strip: latest price, return, benchmark, excess, max drawdown, yearly range.
3. Main analysis band: candlestick chart on the left, yearly facts and technical state on the right.
4. Return windows and benchmark comparison.
5. Drawdown and valuation context.
6. Event timeline.
7. Agent brief.
8. Source footnote.

## Missing Data Behavior

- If benchmark data is missing, omit benchmark and excess-return claims.
- If `daily-basic` is missing, omit valuation context.
- If event datasets are missing, show a note that no events were supplied.
- If fewer than 120 trading rows are available, omit MA120 and disclose warmup limitations.
- Never turn technical state into buy, sell, or hold advice.

## Required Footnote Details

Include dataset names, fields, filters, returned row counts, period boundaries, chart engine name, indicator parameters, benchmark source if used, missing-data notes, and the risk note from `references/compliance.md`.

## Example

Use `examples/annual-performance-report-input.json` as the normalized data shape and `examples/annual-performance-report.html` as the complete offline output model.
