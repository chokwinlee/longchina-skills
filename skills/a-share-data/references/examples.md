# longchina CLI Examples

List datasets:

```bash
longchina datasets --json
```

Fetch daily OHLCV:

```bash
longchina query daily --ts-code 000001.SZ --start 20260511 --end 20260515 --fields ts_code,trade_date,open,high,low,close,vol,amount --format json
```

Fetch daily indicators:

```bash
longchina query daily-basic --ts-code 000001.SZ --start 20260511 --end 20260515 --fields ts_code,trade_date,pe,pb,total_mv --format json
```

Fetch stock master data:

```bash
longchina query stock-basic --ts-code 601318.SH --fields ts_code,name,exchange,list_date,industry --format json
```

Fetch trading calendar:

```bash
longchina query trade-cal --exchange SSE --start 20260501 --end 20260531 --fields exchange,cal_date,is_open,pretrade_date --format csv
```

Fetch adjustment factors:

```bash
longchina query adj-factor --ts-code 601318.SH --start 20260511 --end 20260515 --fields ts_code,trade_date,adj_factor --format csv
```
