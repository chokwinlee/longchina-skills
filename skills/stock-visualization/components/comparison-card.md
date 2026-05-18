# Comparison Card Component

## Purpose

Show a compact security snapshot for comparison pages. This component is for 1 security at a time and should be repeated for each compared security.

## Input Schema

```json
{
  "profile": {
    "symbol": "000001.SZ",
    "name": "Example Bank",
    "industry": "银行",
    "exchange": "SZSE",
    "listing_date": "19910403"
  },
  "snapshot": {
    "date": "20260515",
    "metrics": {
      "close": { "label": "Close", "value": 11.73, "unit": "CNY" },
      "pe_ttm": { "label": "PE TTM", "value": 5.94, "unit": "x" },
      "pb": { "label": "PB", "value": 0.62, "unit": "x" },
      "total_market_value": { "label": "Market value", "value": 227680000000, "unit": "CNY" }
    }
  }
}
```

Required: `profile.symbol`, `profile.name`, `snapshot.metrics`.

Optional: `profile.industry`, `profile.exchange`, `profile.listing_date`, `snapshot.date`.

## Configuration

- `primary_metrics`: recommended `close`, `pe_ttm`, `pb`, `total_market_value`.
- `compact_market_value`: render large CNY values as `227.7B CNY`.
- `show_listing`: default true when `listing_date` exists.

## HTML Snippet

```html
<article class="lc-comparison-card">
  <style>
    .lc-comparison-card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); border: 1px solid oklch(88% 0.018 165); border-radius: 8px; padding: 16px; background: oklch(99% 0.005 165); }
    .lc-comparison-card__name { margin: 0; font-size: 15px; font-weight: 700; }
    .lc-comparison-card__code { margin-top: 3px; color: oklch(48% 0.018 165); font-size: 12px; }
    .lc-comparison-card__meta { display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0; }
    .lc-comparison-card__pill { border: 1px solid oklch(88% 0.018 165); border-radius: 999px; padding: 3px 8px; color: oklch(38% 0.018 165); font-size: 11px; }
    .lc-comparison-card__metrics { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 14px; }
    .lc-comparison-card__label { display: block; color: oklch(48% 0.018 165); font-size: 11px; }
    .lc-comparison-card__value { display: block; margin-top: 2px; font-size: 14px; font-weight: 650; }
  </style>
  <h3 class="lc-comparison-card__name">Example Bank</h3>
  <div class="lc-comparison-card__code">000001.SZ, latest 20260515</div>
  <div class="lc-comparison-card__meta">
    <span class="lc-comparison-card__pill">银行</span>
    <span class="lc-comparison-card__pill">SZSE</span>
    <span class="lc-comparison-card__pill">Listed 19910403</span>
  </div>
  <div class="lc-comparison-card__metrics">
    <span><span class="lc-comparison-card__label">Close</span><span class="lc-comparison-card__value">11.73 CNY</span></span>
    <span><span class="lc-comparison-card__label">PE TTM</span><span class="lc-comparison-card__value">5.94x</span></span>
    <span><span class="lc-comparison-card__label">PB</span><span class="lc-comparison-card__value">0.62x</span></span>
    <span><span class="lc-comparison-card__label">Market value</span><span class="lc-comparison-card__value">227.7B CNY</span></span>
  </div>
</article>
```

## Missing Data Behavior

Render missing profile fields as omitted pills. Render missing metrics as `--` and keep their labels visible when they are important to the comparison.

## Example

Use two to five cards at the top of `recipes/stock-compare.md`.
