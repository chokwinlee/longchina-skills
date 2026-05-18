# longchina Dataset Reference

## prices

CLI: `prices`

Primary key: `symbol`, `date`

Common fields: `symbol`, `date`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `percent_change`, `volume`, `amount`, `adjust`

Filters: `symbol`, `start`, `end`, `adjust`

Use for daily OHLCV price series. Treat returned rows as the source of truth for the requested filters; if rows are missing, report the row count and filters.

## daily-metrics

CLI: `daily-metrics`

Primary key: `symbol`, `date`

Common fields: `symbol`, `date`, `close`, `turnover_rate`, `free_float_turnover_rate`, `volume_ratio`, `pe`, `pe_ttm`, `pb`, `ps`, `ps_ttm`, `dividend_ratio`, `dividend_ttm`, `total_share`, `floating_share`, `free_float_share`, `total_market_value`, `float_market_value`

Filters: `symbol`, `start`, `end`

Use for valuation, turnover, market cap, and share-count indicators.

## securities

CLI: `securities`

Primary key: `symbol`

Common fields: `symbol`, `local_code`, `name`, `region`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `currency`, `listing_status`, `listing_date`, `delisting_date`, `connect_flag`, `controller_name`, `controller_type`

Filters: `symbol`, `market`, `listing_status`, `exchange`

Use for security master data and universe construction.

## trading-calendar

CLI: `trading-calendar`

Primary key: `exchange`, `date`

Common fields: `exchange`, `date`, `is_open`, `previous_open_date`

Filters: `exchange`, `start`, `end`, `is_open`

Use for trading-day validation and scheduling.

## adjustments

CLI: `adjustments`

Primary key: `symbol`, `date`

Common fields: `symbol`, `date`, `adjustment_multiplier`

Filters: `symbol`, `start`, `end`

Use when the task needs raw adjustment factors.

For any dataset not listed here, run `longchina datasets --json` and use only the dataset and field names returned by longchina.
