# Technical Levels Panel Component

## Purpose

Show derived support and resistance levels next to a candlestick or technical report. The panel should explain nearest support, nearest resistance, distance from latest close, touches, and the calculation method. This is not a trading recommendation.

## Input Schema

```json
{
  "latest_close": 52.2,
  "levels": [
    {
      "kind": "support",
      "level": 49.8,
      "distance_pct": -4.6,
      "method": "swing low cluster",
      "touches": 3,
      "date_range": "2026-02-18 to 2026-04-09",
      "evidence": "Three returned daily lows clustered within 0.8%."
    },
    {
      "kind": "resistance",
      "level": 55.6,
      "distance_pct": 6.5,
      "method": "swing high cluster",
      "touches": 2,
      "date_range": "2026-03-12 to 2026-05-06",
      "evidence": "Two returned daily highs clustered within 0.7%."
    }
  ]
}
```

Required: `latest_close`, `levels[].kind`, `levels[].level`, `levels[].method`, `levels[].evidence`.

Optional: `levels[].distance_pct`, `levels[].touches`, `levels[].date_range`.

## Configuration

- Use `lc-technical-levels`.
- `kind` must be `support` or `resistance`.
- Show nearest support below the latest close and nearest resistance above it first.
- Include the method label so users can distinguish swing high/low clusters from other explicit assumptions.
- Do not output buy, sell, stop-loss, breakout, or target-price language.

## HTML Snippet

```html
<section class="lc-technical-levels" aria-labelledby="lc-technical-levels-title">
  <style>
    .lc-technical-levels { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-technical-levels__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-technical-levels__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px; }
    .lc-technical-levels__item { border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 10px; background: oklch(99% 0.005 165); }
    .lc-technical-levels__item h3 { margin: 0 0 6px; font-size: 13px; }
    .lc-technical-levels__item dl { display: grid; grid-template-columns: auto 1fr; gap: 4px 8px; margin: 0; font-size: 12px; line-height: 1.45; }
    .lc-technical-levels__item dt { color: oklch(45% 0.018 165); }
    .lc-technical-levels__item dd { margin: 0; font-variant-numeric: tabular-nums; }
    .lc-technical-levels__note { margin: 10px 0 0; font-size: 12px; color: oklch(42% 0.018 165); }
  </style>
  <h2 class="lc-technical-levels__title" id="lc-technical-levels-title">Technical levels</h2>
  <div class="lc-technical-levels__grid">
    <article class="lc-technical-levels__item">
      <h3>Nearest support</h3>
      <dl>
        <dt>Level</dt><dd>49.80</dd>
        <dt>Distance</dt><dd>-4.6%</dd>
        <dt>Touches</dt><dd>3</dd>
        <dt>Method</dt><dd>swing low cluster</dd>
      </dl>
    </article>
    <article class="lc-technical-levels__item">
      <h3>Nearest resistance</h3>
      <dl>
        <dt>Level</dt><dd>55.60</dd>
        <dt>Distance</dt><dd>6.5%</dd>
        <dt>Touches</dt><dd>2</dd>
        <dt>Method</dt><dd>swing high cluster</dd>
      </dl>
    </article>
  </div>
  <p class="lc-technical-levels__note">Levels are derived from returned daily OHLC rows and are not a trading recommendation.</p>
</section>
```

## Missing Data Behavior

Do not fabricate levels, touches, date ranges, or breakouts. If fewer than two valid support or resistance candidates exist, show the level as unavailable and state the required lookback or missing OHLC fields.

## Example

Use beside `technical-state-table.md` in candlestick and annual-performance reports. For fullscreen inspection of a level chart or matrix, wrap the surrounding visual with `chart-frame.md`.
