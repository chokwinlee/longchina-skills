# longchina CLI Examples

List datasets:

```bash
longchina datasets --json
```

Fetch daily OHLCV:

```bash
longchina query prices --symbol 000001.SZ --start 20260511 --end 20260515 --fields symbol,date,open,high,low,close,volume,amount --order-by date --format json
```

Fetch forward-adjusted daily OHLCV:

```bash
longchina query prices --symbol 000001.SZ --start 20260511 --end 20260515 --adjust qfq --fields symbol,date,open,high,low,close,adjust --order-by date --format json
```

Fetch daily indicators:

```bash
longchina query daily-metrics --symbol 000001.SZ --start 20260511 --end 20260515 --fields symbol,date,pe,pb,total_market_value --order-by date --format json
```

Fetch stock master data:

```bash
longchina query securities --symbol 601318.SH --fields symbol,name,exchange,listing_date,industry --order-by symbol --format json
```

Fetch trading calendar:

```bash
longchina query trading-calendar --exchange SSE --start 20260501 --end 20260531 --fields exchange,date,is_open,previous_open_date --order-by date --format csv
```

Fetch adjustment factors:

```bash
longchina query adjustments --symbol 601318.SH --start 20260511 --end 20260515 --fields symbol,date,adjustment_multiplier --order-by date --format csv
```
