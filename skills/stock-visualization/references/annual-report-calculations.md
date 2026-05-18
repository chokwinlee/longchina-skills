# Annual Report Calculations

Agents calculate annual report metrics before rendering components. HTML examples are display models only; they are not the source of truth for financial calculations.

Use returned `longchina` rows only. Sort all time-series inputs ascending by `trade_date`. Keep raw numeric values in the normalized data object and round only during display.

## Input Preconditions

- Use `daily` rows for price, volume, amount, and candlestick-derived metrics.
- Use `daily-basic` rows for valuation metrics such as `pe_ttm` and `pb`.
- Use benchmark rows only when the user supplies them or the runtime exposes them.
- Do not fabricate missing trading dates, benchmark values, filing events, ratings, or valuation values.
- If adjusted prices are used, state the adjustment method in `SourceDisclosure.notes`; otherwise calculate from the returned raw OHLC rows.

## Actual Trading Range

Natural calendar requests such as "recent one year" must resolve to the actual returned trading range:

```text
first_row = first valid daily row >= requested_start
last_row = last valid daily row <= requested_end
period_return_pct = (last_close - first_close) / first_close * 100
```

Set `period.start`, `period.end`, and `period.trading_rows` from the actual rows used for calculation, not from unavailable calendar dates.

## Return Windows

Default report windows:

- `1M`: 21 trading rows.
- `3M`: 63 trading rows.
- `6M`: 126 trading rows.
- `1Y`: the selected annual range, or the latest 252 trading rows when the source contains more than the annual range.

For a window with offset `n`:

```text
window_start = rows[max(0, row_count - 1 - n)]
stock_return_pct = (last_close - window_start_close) / window_start_close * 100
```

If the requested window is longer than available data, either use the earliest available row and label the actual start date, or mark the window unavailable. Do not silently substitute a shorter period.

Calculate each window's drawdown from rows inside that same window.

## Benchmark Alignment

Benchmark calculations must use stock and benchmark rows aligned by `trade_date`. Use an inner join by date by default.

```text
stock_return_pct = (aligned_last_stock_close - aligned_first_stock_close) / aligned_first_stock_close * 100
benchmark_return_pct = (aligned_last_benchmark_close - aligned_first_benchmark_close) / aligned_first_benchmark_close * 100
excess_return_pct = stock_return_pct - benchmark_return_pct
```

`excess_return_pct` is a percentage-point difference. Do not calculate benchmark or excess returns when aligned benchmark rows are missing.

## Indexed Benchmark Series

For benchmark comparison charts, normalize both series to `100` at the first aligned date:

```text
stock_index[i] = aligned_stock_close[i] / aligned_stock_first_close * 100
benchmark_index[i] = aligned_benchmark_close[i] / aligned_benchmark_first_close * 100
```

The benchmark component should show indexed relative performance, not raw price levels from different instruments.

## Maximum Drawdown

Calculate drawdown from close prices across the selected rows:

```text
running_peak_close[i] = max(close[0] ... close[i])
drawdown_pct[i] = (close[i] - running_peak_close[i]) / running_peak_close[i] * 100
max_drawdown_pct = min(drawdown_pct)
```

`peak_date` is the date of the running peak that was active when the trough was reached. `trough_date` is the date of `max_drawdown_pct`.

## Recovery Date

After finding the max-drawdown trough, scan forward:

```text
recovery_date = first date after trough_date where close >= peak_close
```

Use `null` when the price has not recovered to the prior peak within the selected rows.

## High And Low

Use intraday high and low when available:

```text
high = max(high)
low = min(low)
```

If `high` or `low` is missing across the selected range, fall back to close-price high or low and disclose the fallback in `SourceDisclosure.notes`.

## Average Amount And Volume

Average amount uses valid numeric `amount` rows in the selected range:

```text
avg_amount = average(amount)
avg_vol = average(vol)
```

Keep source units in normalized data. Convert display units, such as CNY to `亿元`, only when the source unit is known and stated in the footnote.

## Annualized Volatility

Calculate close-to-close daily returns:

```text
daily_return[i] = (close[i] - close[i - 1]) / close[i - 1]
volatility_pct = standard_deviation(daily_return) * sqrt(252) * 100
```

Use sample standard deviation with denominator `n - 1`. Mark volatility unavailable when fewer than two valid daily returns exist.

## Valuation Range And Percentile

For each valuation metric, use valid values in the report period:

```text
current_value = latest non-null value
min_value = min(values)
max_value = max(values)
percentile = count(values <= current_value) / count(values) * 100
```

If the latest row is missing but an earlier valid value exists, use the latest valid value and state its date. If no values exist, omit the valuation block and disclose the missing dataset or field.

## Technical State

Technical state is a factual classification, not a trading recommendation.

- MA alignment is `positive` when `close > MA20 > MA60 > MA120`, `negative` when `close < MA20 < MA60 < MA120`, and `neutral` otherwise.
- MACD is `positive` when `DIF > DEA` and `MACD > 0`, `negative` when `DIF < DEA` and `MACD < 0`, and `neutral` otherwise.
- KDJ is `high` when `K`, `D`, or `J` is above `80`, `low` when below `20`, and `neutral` otherwise.
- BOLL position is `above_upper`, `below_lower`, `inside_band`, or `unavailable`.
- RSI is `high` above `70`, `low` below `30`, and `neutral` otherwise.

Do not map these states to buy, sell, hold, overweight, or underweight language unless the user explicitly asks for an investment opinion.

## Agent Brief Inputs

The agent brief may use only calculated factual metrics, supplied event rows, and explicitly stated assumptions. It must separate fact from interpretation and include the risk note from `references/compliance.md`.

## Missing And Invalid Values

If a calculation cannot be performed:

- Store `null` or omit the block according to `references/data-contracts.md`.
- Do not interpolate, backfill, forward-fill, or fabricate values by default.
- Explain affected metrics in `SourceDisclosure.notes`.

## Output Checklist

Before rendering `AnnualPerformanceReport`, verify:

- `period` uses the actual row range.
- `performance_summary` includes latest close, period return, max drawdown, high, low, average amount, and volatility when calculable.
- `return_windows` uses the stated trading-row windows.
- `benchmark` and excess returns use aligned benchmark rows only.
- `drawdown` includes peak, trough, recovery date, and drawdown points.
- `valuation` includes current, min, max, percentile, and valuation points when `daily-basic` data exists.
- `technical_state` cites the calculated evidence for each state.
- `source_disclosure` states datasets, row counts, period boundaries, units, benchmark source, missing values, and risk note.
