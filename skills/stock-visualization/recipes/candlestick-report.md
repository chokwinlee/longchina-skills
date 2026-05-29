# Candlestick Report Recipe

Use this recipe when the user asks for K line, K线, candlestick, 蜡烛图, TradingView-style report, stock trend visualization, technical indicators, MACD, KDJ, RSI, capital flow, liquidity, relative strength, or a professional A-share chart report.

## When To Use

- "帮我可视化一下中国平安的行情."
- "画一下 601318 的 K 线和 MACD."
- "看一下 601318 的技术面、支撑位和压力位."
- "看一下 000001.SZ 的资金面和换手有没有放大."
- "这只股票最近是否跑赢行业或指数."
- "Generate an offline candlestick report for 000001.SZ."
- "Show price, volume, valuation, and technical indicators."

## Datasets To Query

Use `longchina-data` and fetch:

- `securities` for `symbol`, `name`, `industry`, `exchange`, `market`, `listing_date`.
- `prices` for `symbol`, `date`, `open`, `high`, `low`, `close`, `previous_close`, `percent_change`, `volume`, `amount`.
- `daily-metrics` when tooltip, valuation, turnover, market value, or comparison metrics are requested.
- `trading-calendar` when the user gives natural dates that may not be trading days.
- Public references from `stock-research-intake/references/public-reference-sources.md` only when explicit external evidence is needed, such as Stock Connect shareholding context, macro liquidity, or index methodology.

## Data Contracts

Fill:

- `SecurityProfile` for listing metadata.
- `CandlePoint` for every valid `prices` row.
- `OverlaySeries` for MA and BOLL overlays.
- `IndicatorPaneSeries` for volume, MACD, KDJ, and optional RSI.
- `TechnicalLevelSet` for nearest support and nearest resistance when enough OHLC rows exist.
- `CapitalFlowEvidence` for amount, volume, turnover, volume ratio, and public reference notes when requested.
- `RelativeStrengthWindow` for benchmark or peer return spreads when requested.
- `TooltipSnapshot` by ISO date.
- `SourceDisclosure` for the final footnote.

## Components

Compose:

1. `chart-frame.md` around the interactive chart panes.
2. `candlestick-chart.md`.
3. `indicator-pane.md` for volume, MACD, KDJ, and optional RSI.
4. `technical-state-table.md` for current MA, MACD, RSI/KDJ/BOLL, and volume-price states.
5. `technical-levels-panel.md` for support/resistance levels when requested or useful.
6. `capital-flow-panel.md` for amount, volume, turnover, and public reference liquidity context when requested.
7. `relative-strength-panel.md` when benchmark, sector, or peer return spread is requested.
8. `chart-tooltip.md`.
9. `sortable-table.md` for the latest OHLCV and selected daily-metrics metrics when useful.
10. `source-footnote.md`.

## Missing Data Behavior

- If no `prices` OHLC rows are returned, show an empty state and still include source disclosure.
- If `daily-metrics` is unavailable, omit valuation fields from the tooltip and state that only price/volume fields were returned.
- If the selected range is too short for MA60, KDJ, RSI, or BOLL, omit the unavailable series and state the warmup requirement.
- If the selected range has too few swing highs or swing lows, show support/resistance as unavailable rather than inventing levels.
- If amount, turnover, volume ratio, benchmark rows, or public reference evidence is unavailable, show the affected capital-flow or relative-strength item as unavailable rather than replacing it with price movement.
- Do not interpolate missing trading dates.

## Required Footnote Details

Include dataset names, fields, filters, returned row counts, actual trading-date range, generation time, chart engine name, indicator parameters, public reference disclosures, missing-data notes, and the risk note from `references/compliance.md`.

## Example

Use `examples/candlestick-report-input.json` as the normalized data shape and `examples/candlestick-report.html` as the complete offline output model.
