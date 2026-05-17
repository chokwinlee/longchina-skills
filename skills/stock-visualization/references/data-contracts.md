# Data Contracts

Normalize `longchina` rows into these contracts before rendering components. Use `null` for known missing values. Do not invent data to fill a contract.

Dates use `YYYYMMDD` unless a component explicitly formats them for display. Numeric fields should remain numbers until final rendering. Units must be carried next to values when a value can be ambiguous.

## SecurityProfile

Use for company and listing metadata from `stock-basic`.

```json
{
  "ts_code": "000001.SZ",
  "symbol": "000001",
  "name": "Example Bank",
  "exchange": "SZSE",
  "market": "主板",
  "industry": "银行",
  "area": "深圳",
  "list_status": "L",
  "list_date": "19910403",
  "delist_date": null
}
```

Required: `ts_code`, `name`.

Optional: `symbol`, `exchange`, `market`, `industry`, `area`, `list_status`, `list_date`, `delist_date`.

Missing behavior: render unavailable metadata as `--` and explain material omissions in `SourceDisclosure.notes`.

## PricePoint

Use for daily price series from `daily`. Add derived fields only after calculating them from returned rows.

```json
{
  "ts_code": "000001.SZ",
  "trade_date": "20260511",
  "open": 11.2,
  "high": 11.58,
  "low": 11.06,
  "close": 11.42,
  "pre_close": 11.18,
  "pct_chg": 2.15,
  "vol": 874512.34,
  "amount": 998231.12,
  "ma5": 11.18,
  "ma20": null
}
```

Required: `ts_code`, `trade_date`, `close`.

Optional: `open`, `high`, `low`, `pre_close`, `pct_chg`, `vol`, `amount`, calculated indicator fields such as `ma5`, `ma20`, `dif`, `dea`, `macd`.

Units: `vol` follows the upstream dataset unit, `amount` follows the upstream dataset unit, `pct_chg` is percentage points.

## MetricPoint

Use for time-series valuation, turnover, market value, or volume metrics.

```json
{
  "ts_code": "000001.SZ",
  "trade_date": "20260511",
  "metric": "pe_ttm",
  "label": "PE TTM",
  "value": 5.82,
  "unit": "x",
  "source_dataset": "daily-basic"
}
```

Required: `ts_code`, `trade_date`, `metric`, `label`, `value`, `source_dataset`.

Optional: `unit`.

Missing behavior: omit points where the source value is null; if the whole series is empty, render the Metric Series component empty state.

## MetricSnapshot

Use for latest-value cards, comparison matrices, and sortable tables.

```json
{
  "ts_code": "000001.SZ",
  "trade_date": "20260515",
  "metrics": {
    "close": { "label": "Close", "value": 11.73, "unit": "CNY", "source_dataset": "daily" },
    "pe_ttm": { "label": "PE TTM", "value": 5.94, "unit": "x", "source_dataset": "daily-basic" },
    "pb": { "label": "PB", "value": 0.62, "unit": "x", "source_dataset": "daily-basic" },
    "total_mv": { "label": "Total market value", "value": 227680000000, "unit": "CNY", "source_dataset": "daily-basic" }
  }
}
```

Required: `ts_code`, `trade_date`, `metrics`.

Each metric requires `label`, `value`, and `source_dataset`. `unit` is optional only when the label is self-evident.

## ComparisonRow

Use for comparison matrices and sortable tables.

```json
{
  "ts_code": "000001.SZ",
  "name": "Example Bank",
  "industry": "银行",
  "trade_date": "20260515",
  "values": {
    "close": 11.73,
    "pe_ttm": 5.94,
    "pb": 0.62,
    "total_mv": 227680000000,
    "turnover_rate": 0.81
  },
  "units": {
    "close": "CNY",
    "pe_ttm": "x",
    "pb": "x",
    "total_mv": "CNY",
    "turnover_rate": "%"
  }
}
```

Required: `ts_code`, `name`, `values`.

Optional: `industry`, `trade_date`, `units`.

Missing behavior: render missing values as `--`; do not sort missing numeric values ahead of real values.

## SourceDisclosure

Required for every generated page.

```json
{
  "generated_at": "2026-05-16T16:30:00+08:00",
  "data_sources": [
    {
      "dataset": "daily",
      "fields": ["ts_code", "trade_date", "close", "vol"],
      "filters": { "ts_code": "000001.SZ", "start": "20260511", "end": "20260515" },
      "row_count": 5
    },
    {
      "dataset": "daily-basic",
      "fields": ["ts_code", "trade_date", "pe_ttm", "pb", "total_mv"],
      "filters": { "ts_code": "000001.SZ", "start": "20260511", "end": "20260515" },
      "row_count": 5
    }
  ],
  "notes": ["Example output uses illustrative values."],
  "risk_note": "This visualization is not investment advice."
}
```

Required: `generated_at`, `data_sources`, `risk_note`.

Each source requires `dataset`, `fields`, `filters`, and `row_count` when available. If usage or cache metadata is available, include it in an additional `usage` object.
