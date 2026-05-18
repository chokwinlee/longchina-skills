# Stock Compare Recipe

Use this recipe when the user asks to compare two to five A-share securities using light fundamentals and recent price movement.

## When To Use

- "Compare 000001.SZ and 600000.SH."
- "Generate an HTML page comparing these bank stocks."
- "Show valuation, market value, and recent trend for this stock list."

## Datasets To Query

Use `longchina-data` and fetch:

- `securities` for `symbol`, `name`, `industry`, `exchange`, `market`, `listing_date`.
- `prices` for `symbol`, `date`, `close`, `percent_change`, `volume`, `amount`.
- `daily-metrics` for `symbol`, `date`, `pe`, `pe_ttm`, `pb`, `ps`, `ps_ttm`, `dividend_ratio`, `dividend_ttm`, `total_market_value`, `turnover_rate`.
- `trading-calendar` when the user gives natural dates that may not be trading days.

## Data Contracts

Fill:

- `SecurityProfile` for each security.
- `CandlePoint` for each valid OHLC row, or `PricePoint` when only close-price data is available.
- `MetricSnapshot` for the latest returned `prices` and `daily-metrics` values.
- `ComparisonRow` for the matrix.
- `SourceDisclosure` for the final footnote.

## Components

Compose:

1. `comparison-card.md`, repeated once per security.
2. `comparison-matrix.md`.
3. `candlestick-chart.md` as small panels when comparing two to three securities and OHLC rows are available.
4. `price-trend.md` only for four to five securities, non-OHLC data, or one combined indexed chart when the agent can normalize values clearly.
5. `source-footnote.md`.

## Missing Data Behavior

- If a security has no `securities` row, use the requested `symbol` as the visible label and note the missing profile row.
- If a metric is missing, show `--` in cards and matrix cells.
- If latest dates differ across securities, show each date in cards and matrix rows.
- If no `prices` rows are returned for a security, omit its candlestick or price trend and note the query filters.
- If OHLC fields are incomplete, fall back to an indexed close-price line and state why the candlestick panel was not rendered.

## Required Footnote Details

Include dataset names, fields, filters, date range, returned row counts, generation time, missing-data notes, and the risk note from `references/compliance.md`.
