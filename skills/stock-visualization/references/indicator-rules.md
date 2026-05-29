# Indicator Rules

Agents calculate indicators before rendering components. Component snippets display prepared values and do not own financial calculations.

Use returned `longchina` rows only. Sort time-series input ascending by `date` before calculation.

## Simple Moving Average

For a window `n`, the moving average at index `i` is the arithmetic mean of the previous `n` close values including the current point:

```text
ma_n[i] = sum(close[i - n + 1] ... close[i]) / n
```

The value is unavailable until `n` valid close values exist. Use `null` for unavailable values.

Default stock overlays are `MA5`, `MA10`, `MA20`, and `MA60`. For short reports, render `MA5`, `MA10`, and `MA20` by default and calculate `MA60` when enough rows exist or when the user asks for a longer trend.

## Interval Return

Use the first and last valid close in the selected interval:

```text
interval_return_pct = (last_close - first_close) / first_close * 100
```

If `first_close` is missing or zero, mark the interval return unavailable. Do not substitute another date unless the component footnote says which trading dates were used.

## Volume Change

For a chosen window `n`, compare the latest `n` valid volume values with the immediately preceding `n` valid volume values:

```text
latest_avg = average(volume[last n points])
prior_avg = average(volume[previous n points])
volume_change_pct = (latest_avg - prior_avg) / prior_avg * 100
```

If either window is incomplete or `prior_avg` is zero, mark the value unavailable.

## Volume Bar Color

For A-share charts, default volume bar color follows the candle state:

- Up bar: `close >= previous_close` when `previous_close` exists, otherwise `close >= open`.
- Down bar: `close < previous_close` when `previous_close` exists, otherwise `close < open`.

Use the same red/up and green/down convention as the candlestick pane unless the report explicitly labels a different convention. Store the color class or final color on each volume point; do not derive it from rendered pixels.

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

Default P0 label: `MACD(12,26,9), histogram = DIF - DEA`.

## KDJ

Use the default `KDJ(9,3,3)` unless the user gives a different configuration.

For each index `i`, calculate RSV over the latest `9` valid candles including the current candle:

```text
rsv[i] = (close[i] - lowest_low_9[i]) / (highest_high_9[i] - lowest_low_9[i]) * 100
```

If `highest_high_9` equals `lowest_low_9`, set RSV to `50` for that point and disclose the flat-range condition if it affects a visible range. Initialize the first available `K` and `D` values at `50`, then:

```text
k[i] = k[i - 1] * 2 / 3 + rsv[i] / 3
d[i] = d[i - 1] * 2 / 3 + k[i] / 3
j[i] = 3 * k[i] - 2 * d[i]
```

Use `null` until 9 valid rows exist. Do not backfill KDJ values into earlier rows.

## RSI

Use default periods `RSI6`, `RSI12`, and `RSI24`.

For period `n`, calculate gains and losses from close-to-close changes:

```text
gain = max(close[i] - close[i - 1], 0)
loss = max(close[i - 1] - close[i], 0)
rsi_n = average_gain_n / (average_gain_n + average_loss_n) * 100
```

Use simple rolling averages unless the report explicitly states a Wilder smoothing variant. If both average gain and average loss are zero, set RSI to `50`.

## BOLL

Use default `BOLL(20,2)`.

```text
mid = MA20(close)
std = standard_deviation(close over 20 rows)
upper = mid + 2 * std
lower = mid - 2 * std
```

Render BOLL as three main-pane `OverlaySeries` lines. Use `null` until 20 valid close values exist.

## Support And Resistance Levels

Support and resistance levels are derived from returned daily OHLC rows. They are factual chart structure, not a forecast.

Default preconditions:

- Use at least 40 valid OHLC rows when available; with fewer rows, mark the level evidence as weak or unavailable.
- Sort rows ascending by `date`.
- Use a swing lookback of 2 rows on each side unless the user requests another lookback.

Swing candidates:

```text
swing low at i when low[i] <= low[i - 1], low[i - 2], low[i + 1], low[i + 2]
swing high at i when high[i] >= high[i - 1], high[i - 2], high[i + 1], high[i + 2]
```

Cluster candidates into levels when their prices are within this tolerance:

```text
median_range_pct = median((high - low) / close) over valid rows
tolerance_pct = max(0.5, median_range_pct * 100)
```

For each cluster, calculate:

- `level`: average candidate price in the cluster.
- `touches`: number of swing candidates in the cluster.
- `date_range`: first and last candidate dates.
- `distance_pct`: `(level - latest_close) / latest_close * 100`.
- `evidence`: short text describing touches, date range, and tolerance.

Classify support and resistance from the latest close:

- nearest support: highest clustered swing low level below or equal to the latest close.
- nearest resistance: lowest clustered swing high level above or equal to the latest close.

Rank candidates by touches first, then recency, then distance to latest close. If no candidate exists on one side of the latest close, mark that side unavailable rather than inventing a level.

Do not label support or resistance as a trading signal. Do not call a breakout, breakdown, stop-loss, or target price unless the user explicitly asks for a trading plan and the answer clearly separates assumptions from facts.

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
