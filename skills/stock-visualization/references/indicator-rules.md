# Indicator Rules

Agents calculate indicators before rendering components. Component snippets display prepared values and do not own financial calculations.

Use returned `longchina` rows only. Sort time-series input ascending by `trade_date` before calculation.

## Simple Moving Average

For a window `n`, the moving average at index `i` is the arithmetic mean of the previous `n` close values including the current point:

```text
ma_n[i] = sum(close[i - n + 1] ... close[i]) / n
```

The value is unavailable until `n` valid close values exist. Use `null` for unavailable values.

## Interval Return

Use the first and last valid close in the selected interval:

```text
interval_return_pct = (last_close - first_close) / first_close * 100
```

If `first_close` is missing or zero, mark the interval return unavailable. Do not substitute another date unless the component footnote says which trading dates were used.

## Volume Change

For a chosen window `n`, compare the latest `n` valid volume values with the immediately preceding `n` valid volume values:

```text
latest_avg = average(vol[last n points])
prior_avg = average(vol[previous n points])
volume_change_pct = (latest_avg - prior_avg) / prior_avg * 100
```

If either window is incomplete or `prior_avg` is zero, mark the value unavailable.

## MACD

Use close price and these spans unless the user explicitly asks for a different configuration:

- Short EMA span: 12
- Long EMA span: 26
- Signal EMA span: 9

EMA smoothing factor:

```text
alpha = 2 / (span + 1)
ema[i] = close[i] * alpha + ema[i - 1] * (1 - alpha)
```

Initialize the first EMA value with the first valid close. Then:

```text
dif = ema12 - ema26
dea = ema9(dif)
macd = dif - dea
```

Label the histogram as `macd`. If the user expects the common doubled histogram convention, make the multiplier explicit in the chart label and source note.

## Missing Values

If a calculation cannot be performed:

- Store `null`.
- Do not interpolate, backfill, or fabricate.
- Explain the affected metric in the Source Footnote when the omission changes interpretation.

## Rounding

Keep raw numeric values in data objects. Round only during display:

- Price: 2 decimals unless the source precision requires more.
- Percent: 2 decimals plus `%`.
- PE/PB/PS: 2 decimals plus `x`.
- Market value: compact display such as `227.7B CNY`, while retaining raw values in table attributes when sorting.
