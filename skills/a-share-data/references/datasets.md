# longchina Dataset Reference

## daily

CLI: `daily`

Primary key: `ts_code`, `trade_date`

Common fields: `ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`, `adjust`

Filters: `ts_code`, `start`, `end`, `adjust`

Use for daily OHLCV price series. Treat returned rows as the source of truth for the requested filters; if rows are missing, report the row count and filters.

## daily-basic

CLI: `daily-basic`

API dataset: `daily_basic`

Primary key: `ts_code`, `trade_date`

Common fields: `ts_code`, `trade_date`, `close`, `turnover_rate`, `turnover_rate_f`, `volume_ratio`, `pe`, `pe_ttm`, `pb`, `ps`, `ps_ttm`, `dv_ratio`, `dv_ttm`, `total_share`, `float_share`, `free_share`, `total_mv`, `circ_mv`

Filters: `ts_code`, `start`, `end`

Use for valuation, turnover, market cap, and share-count indicators.

## stock-basic

CLI: `stock-basic`

API dataset: `stock_basic`

Primary key: `ts_code`

Common fields: `ts_code`, `symbol`, `name`, `area`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`, `is_hs`, `act_name`, `act_ent_type`

Filters: `ts_code`, `market`, `list_status`, `exchange`

Use for security master data and universe construction.

## trade-cal

CLI: `trade-cal`

API dataset: `trade_cal`

Primary key: `exchange`, `cal_date`

Common fields: `exchange`, `cal_date`, `is_open`, `pretrade_date`

Filters: `exchange`, `start`, `end`, `is_open`

Use for trading-day validation and scheduling.

## adj-factor

CLI: `adj-factor`

API dataset: `adj_factor`

Primary key: `ts_code`, `trade_date`

Common fields: `ts_code`, `trade_date`, `adj_factor`

Filters: `ts_code`, `start`, `end`

Use when the task needs raw adjustment factors.

## financial statements and indicators

CLI datasets:

- `income`
- `balancesheet`
- `cashflow`
- `fina-indicator`
- `forecast`
- `express`
- `dividend`
- `fina-audit`
- `fina-mainbz`
- `disclosure-date`

Common filters: `ts_code`, `start`, `end`. Some datasets also support exact filters such as `ann_date`, `end_date`, `period`, `type`, `record_date`, or `ex_date`.

Use these datasets for fundamental research reports: revenue and profit trends, balance sheet risk, cash flow quality, financial ratios, dividend history, audit result, business segment breakdown, performance forecasts, performance express reports, and disclosure schedule checks.

## review signals

CLI datasets:

- `moneyflow`
- `margin`
- `margin-detail`
- `stk-limit`
- `top-list`
- `top-inst`
- `block-trade`
- `repurchase`
- `hk-hold`

Use these datasets for one-off stock-pool review reports, anomaly checks, market behavior context, financing/margin review, limit-price context, block-trade review, buyback review, and Northbound holding context. Prefer bounded date filters.

## shareholder and governance

CLI datasets:

- `top10-holders`
- `top10-floatholders`
- `stk-holdernumber`
- `stk-holdertrade`
- `pledge-stat`
- `pledge-detail`

Use these datasets for shareholder concentration, holder count changes, major holder trades, and pledge-risk context. Treat missing rows as no returned records for the requested filters, not as proof that the event never happened outside the queried range.
