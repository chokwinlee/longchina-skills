# Candlestick Report Recipe

Use this recipe when the user asks for K line, K线, candlestick, 蜡烛图, TradingView-style report, stock trend visualization, technical indicators, MACD, KDJ, RSI, or a professional A-share chart report.

## When To Use

- "帮我可视化一下中国平安的行情."
- "画一下 601318 的 K 线和 MACD."
- "Generate an offline candlestick report for 000001.SZ."
- "Show price, volume, valuation, and technical indicators."

## Datasets To Query

Use `longchina-data` and fetch:

- `stock-basic` for `ts_code`, `name`, `industry`, `exchange`, `market`, `list_date`.
- `daily` for `ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `pct_chg`, `vol`, `amount`.
- `daily-basic` when tooltip, valuation, turnover, market value, or comparison metrics are requested.
- `trade-cal` when the user gives natural dates that may not be trading days.

## Data Contracts

Fill:

- `SecurityProfile` for listing metadata.
- `CandlePoint` for every valid `daily` row.
- `OverlaySeries` for MA and BOLL overlays.
- `IndicatorPaneSeries` for volume, MACD, KDJ, and optional RSI.
- `TooltipSnapshot` by ISO date.
- `SourceDisclosure` for the final footnote.

## Components

Compose:

1. `candlestick-chart.md`.
2. `indicator-pane.md` for volume, MACD, KDJ, and optional RSI.
3. `chart-tooltip.md`.
4. `sortable-table.md` for the latest OHLCV and selected daily-basic metrics when useful.
5. `source-footnote.md`.

## Missing Data Behavior

- If no `daily` OHLC rows are returned, show an empty state and still include source disclosure.
- If `daily-basic` is unavailable, omit valuation fields from the tooltip and state that only price/volume fields were returned.
- If the selected range is too short for MA60, KDJ, RSI, or BOLL, omit the unavailable series and state the warmup requirement.
- Do not interpolate missing trading dates.

## Required Footnote Details

Include dataset names, fields, filters, returned row counts, actual trading-date range, generation time, chart engine name, indicator parameters, missing-data notes, and the risk note from `references/compliance.md`.

## Example

Use `examples/candlestick-report-input.json` as the normalized data shape and `examples/candlestick-report.html` as the complete offline output model.
