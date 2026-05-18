# Trend Report Recipe

Use this recipe when the user asks for price movement, valuation movement, turnover, volume, or indicator changes for one or more securities.

## When To Use

- "Generate a trend report for 601318.SH."
- "Show close price and PE changes over the last month."
- "Make an HTML report with MA and MACD."

## Datasets To Query

Use `longchina-data` and fetch:

- `prices` for close, OHLCV, percentage change, and volume.
- `daily-metrics` for PE, PB, PS, market value, turnover, and dividend metrics.
- `adjustments` only when the user asks for adjusted price behavior or the price series requires raw adjustment factors.
- `trading-calendar` to validate date ranges when needed.

## Data Contracts

Fill:

- `SecurityProfile` when security metadata is shown.
- `PricePoint` with calculated indicators such as MA or MACD.
- `MetricPoint` for each displayed metric series.
- `SourceDisclosure`.

## Components

Compose:

1. `price-trend.md`.
2. `metric-series.md`, repeated for selected indicators.
3. Plain text interval summary when useful.
4. `source-footnote.md`.

## Missing Data Behavior

- If a derived indicator cannot be calculated because too few rows were returned, omit the indicator line and state why.
- If a metric series has sparse values, plot only returned values and note missing dates.
- If price and metric datasets have different latest dates, show both dates in the footnote.

## Required Footnote Details

Include indicator configuration, dataset fields, filters, row counts, date range, generation time, and risk note.
