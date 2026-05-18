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

## CandlePoint

Use for daily candlestick charts from `daily`. Sort ascending by `trade_date` and convert `trade_date` to ISO `time` before passing rows to `lightweight-charts`.

```json
{
  "ts_code": "601318.SH",
  "trade_date": "20260515",
  "time": "2026-05-15",
  "open": 51.2,
  "high": 52.8,
  "low": 50.9,
  "close": 52.2,
  "pre_close": 50.82,
  "pct_chg": 2.71,
  "vol": 874512.34,
  "amount": 998231.12
}
```

Required: `ts_code`, `trade_date`, `time`, `open`, `high`, `low`, `close`.

Optional: `pre_close`, `pct_chg`, `vol`, `amount`.

Missing behavior: if any required OHLC field is missing or non-numeric, omit that candle and disclose the omitted row count in `SourceDisclosure.notes`.

## OverlaySeries

Use for lines that share the main price scale, such as MA and BOLL bands.

```json
{
  "kind": "ma",
  "label": "MA20",
  "period": 20,
  "points": [
    { "time": "2026-05-15", "value": 51.84 }
  ]
}
```

Required: `kind`, `label`, `points[].time`.

Optional: `period`, `points[].value`, style fields such as `color` and `lineStyle`.

Missing behavior: omit null points from the rendered series. Do not connect a line across unavailable warmup periods.

## IndicatorPaneSeries

Use for lower-pane indicators that should not share the price scale.

```json
{
  "pane": "macd",
  "title": "MACD(12,26,9)",
  "series": [
    { "kind": "histogram", "label": "MACD", "points": [{ "time": "2026-05-15", "value": 0.22 }] },
    { "kind": "line", "label": "DIF", "points": [{ "time": "2026-05-15", "value": 0.68 }] },
    { "kind": "line", "label": "DEA", "points": [{ "time": "2026-05-15", "value": 0.46 }] }
  ]
}
```

Required: `pane`, `series[].kind`, `series[].label`, `series[].points[].time`.

Optional: `title`, `height`, `series[].points[].value`, `series[].points[].color`.

Missing behavior: omit unavailable points and state warmup limits in the Source Footnote when a pane is materially incomplete.

## TooltipSnapshot

Use a per-date merged object for hover details. The key should match the chart `time` string exactly.

```json
{
  "time": "2026-05-15",
  "trade_date": "20260515",
  "open": 51.2,
  "high": 52.8,
  "low": 50.9,
  "close": 52.2,
  "pct_chg": 2.71,
  "vol": 874512.34,
  "amount": 998231.12,
  "turnover_rate": 0.81,
  "pe_ttm": 8.91,
  "pb": 0.96,
  "macd": 0.22,
  "dif": 0.68,
  "dea": 0.46,
  "k": 71.2,
  "d": 68.3,
  "j": 77.1
}
```

Required for candlestick tooltip: `time`, `open`, `high`, `low`, `close`.

Optional: `trade_date`, `pct_chg`, `vol`, `amount`, daily-basic metrics, and indicator values.

Missing behavior: show `--` for optional missing values and keep the tooltip visible if required OHLC values exist.

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

## AnnualPerformanceReport

Use for 最近一年, one-year performance, annual review, or full stock performance reports. This contract composes existing chart contracts with report-level analysis blocks.

Calculation source: use `references/annual-report-calculations.md` for every field under `performance_summary`, `return_windows`, `drawdown`, `valuation`, `benchmark`, and `technical_state`. This contract defines shape and missing-data behavior only.

```json
{
  "profile": { "ts_code": "601318.SH", "name": "中国平安", "industry": "保险" },
  "period": {
    "start": "20250519",
    "end": "20260518",
    "display": "2025-05-19 to 2026-05-18",
    "trading_rows": 242
  },
  "candles": [],
  "overlays": [],
  "panes": [],
  "tooltip": {},
  "performance_summary": {
    "latest_close": 52.2,
    "period_return_pct": 12.4,
    "benchmark_return_pct": 4.1,
    "excess_return_pct": 8.3,
    "max_drawdown_pct": -18.6,
    "high": { "trade_date": "20260210", "value": 58.4 },
    "low": { "trade_date": "20250821", "value": 41.2 },
    "avg_amount": 128.4,
    "volatility_pct": 22.8
  },
  "return_windows": [
    { "label": "1M", "stock_return_pct": 3.2, "benchmark_return_pct": 1.1, "excess_return_pct": 2.1, "max_drawdown_pct": -4.8 }
  ],
  "drawdown": {
    "max_drawdown_pct": -18.6,
    "peak_date": "20260210",
    "trough_date": "20260318",
    "recovery_date": null,
    "points": [{ "trade_date": "20260518", "value": -4.2 }]
  },
  "valuation": {
    "pe_ttm": { "current": 8.9, "min": 7.2, "max": 10.8, "percentile": 61 },
    "pb": { "current": 0.96, "min": 0.78, "max": 1.12, "percentile": 54 },
    "points": [{ "trade_date": "20260518", "pe_ttm": 8.9, "pb": 0.96 }]
  },
  "benchmark": {
    "name": "沪深300",
    "points": [{ "trade_date": "20260518", "stock_index": 112.4, "benchmark_index": 104.1 }]
  },
  "events": [
    { "trade_date": "20260320", "kind": "earnings", "title": "Annual report released", "summary": "Revenue and profit fields should cite returned filings data when available." }
  ],
  "technical_state": [
    { "label": "MA20/60/120", "state": "neutral", "value": "MA20 above MA60, below MA120", "evidence": "Calculated from returned daily rows." }
  ],
  "agent_brief": {
    "title": "Research brief",
    "points": ["Separate fact from interpretation and avoid buy/sell conclusions."],
    "assumptions": ["Benchmark series was supplied by the caller."]
  },
  "source_disclosure": {}
}
```

Required: `profile`, `period`, `candles`, `performance_summary`, `return_windows`, `drawdown`, `valuation`, `benchmark`, `events`, `technical_state`, `agent_brief`, and `source_disclosure`.

Missing behavior: omit unavailable blocks only when the source dataset is missing, then state the omitted block and dataset in `SourceDisclosure.notes`. Do not fabricate benchmarks, filing events, research ratings, or agent conclusions.

Required: `generated_at`, `data_sources`, `risk_note`.

Each source requires `dataset`, `fields`, `filters`, and `row_count` when available. If usage or cache metadata is available, include it in an additional `usage` object.
