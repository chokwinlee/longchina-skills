# Benchmark Comparison Component

## Purpose

Compare indexed stock performance against a benchmark such as 沪深300, industry index, or a user-supplied peer basket.

## Input Schema

```json
{
  "benchmark": {
    "name": "沪深300",
    "points": [
      { "trade_date": "20260518", "stock_index": 112.4, "benchmark_index": 104.1 }
    ]
  }
}
```

Required: `name`, `points[].trade_date`, `points[].stock_index`, `points[].benchmark_index`.

Optional: benchmark code, benchmark source disclosure.

## Configuration

- Use `lc-benchmark-comparison`.
- Index both series to 100 at the first shared trading date.
- Use copper for the stock and blue or dim neutral for the benchmark.
- Include `lc-series-legend` above the chart with `lc-series-legend__swatch` line markers for each visible series.
- Label series with human names such as company name and benchmark name, not generic `stock` and `benchmark` alone.
- Do not use uncolored in-SVG words as the only legend; SVG text can look like axis annotation and loses the color binding.
- Include latest excess return when the aligned benchmark return exists.

## HTML Snippet

```html
<section class="lc-benchmark-comparison">
  <h2>相对基准</h2>
  <div class="lc-series-legend" aria-label="Indexed series legend">
    <span><span class="lc-series-legend__swatch"></span>中国平安</span>
    <span><span class="lc-series-legend__swatch lc-series-legend__swatch--benchmark"></span>沪深300</span>
  </div>
  <svg role="img" aria-label="Indexed stock and benchmark returns"></svg>
</section>
```

## Missing Data Behavior

If no benchmark is supplied, omit the comparison and avoid claiming excess return.

## Example

Use in annual reports after the return window table.
