# Chart Tooltip Component

## Purpose

Display exact daily values while the user hovers over candlesticks or lower panes. The tooltip is driven by `subscribeCrosshairMove` and a precomputed `TooltipSnapshot` map, not by recomputing values from rendered pixels.

## Input Schema

```json
{
  "snapshots": {
    "2026-05-15": {
      "time": "2026-05-15",
      "trade_date": "20260515",
      "open": 51.2,
      "high": 52.8,
      "low": 50.9,
      "close": 52.2,
      "pct_chg": 2.71,
      "vol": 874512.34,
      "amount": 998231.12,
      "macd": 0.22,
      "dif": 0.68,
      "dea": 0.46,
      "pe_ttm": 8.91,
      "pb": 0.96
    }
  }
}
```

Required: `snapshots[time].time`, `open`, `high`, `low`, `close` for candlestick tooltips.

Optional: `trade_date`, `pct_chg`, `vol`, `amount`, indicator fields, daily-basic metrics.

## Configuration

- Anchor the tooltip near the pointer but clamp it inside the chart wrapper.
- Hide when `param.time` is missing.
- Show formatted values while keeping raw values in the data map.
- Use the same date key format as chart series: ISO `YYYY-MM-DD`.

## HTML Snippet

```html
<div id="lc-tooltip" class="lc-tooltip" hidden aria-live="polite"></div>
<script>
(() => {
  const tooltip = document.querySelector("#lc-tooltip");
  const snapshots = window.__LC_REPORT_DATA__.tooltip;

  function updateTooltip(param, sourceElement) {
    if (!param.time) {
      tooltip.hidden = true;
      return;
    }
    const snapshot = snapshots[String(param.time)];
    if (!snapshot) {
      tooltip.hidden = true;
      return;
    }
    tooltip.hidden = false;
    tooltip.innerHTML = `<strong>${snapshot.time}</strong>`;
  }
})();
</script>
```

The full example in `examples/candlestick-report.html` expands this into OHLCV, MACD, KDJ, and valuation rows.

## Missing Data Behavior

Render `--` for missing optional fields. If required OHLC fields are missing, do not draw a candle for that date and disclose the omitted row count.

## Example

Use with `components/candlestick-chart.md`. Every chart instance that participates in hover inspection should call the shared tooltip update function from its own `subscribeCrosshairMove` handler.
