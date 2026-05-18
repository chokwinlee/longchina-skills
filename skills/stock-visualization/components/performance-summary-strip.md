# Performance Summary Strip Component

## Purpose

Show the first-screen facts for a one-year stock performance report: period return, benchmark return, excess return, max drawdown, yearly high/low, average amount, and volatility. Use this above the main chart so the reader can orient before inspecting details.

## Input Schema

```json
{
  "summary": {
    "latest_close": 52.2,
    "period_return_pct": 12.4,
    "benchmark_return_pct": 4.1,
    "excess_return_pct": 8.3,
    "max_drawdown_pct": -18.6,
    "high": { "date": "20260210", "value": 58.4 },
    "low": { "date": "20250821", "value": 41.2 },
    "avg_amount": 128.4,
    "volatility_pct": 22.8
  }
}
```

Required: `latest_close`, `period_return_pct`, `max_drawdown_pct`.

Optional: benchmark, high/low, average amount, volatility.

## Configuration

- Render as a dense grid separated by 0.5px or 1px lines, not separate decorative cards.
- Use `lc-performance-summary` for the wrapper.
- Use tabular numerals for values.
- Apply A-share red/up and green/down only to signed return or drawdown values.

## HTML Snippet

```html
<section class="lc-performance-summary" aria-label="Performance summary">
  <div><span>一年收益</span><strong class="lc-up">+12.40%</strong></div>
  <div><span>超额收益</span><strong class="lc-up">+8.30pct</strong></div>
  <div><span>最大回撤</span><strong class="lc-down">-18.60%</strong></div>
  <div><span>年内高点</span><strong>58.40</strong></div>
</section>
```

## Missing Data Behavior

Render `--` for optional missing values. If benchmark data is missing, omit excess return and disclose that no benchmark series was supplied.

## Example

Use this component at the top of `recipes/annual-performance-report.md`, directly below the report heading and period metadata.
