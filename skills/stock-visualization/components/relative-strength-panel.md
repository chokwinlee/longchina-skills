# Relative Strength Panel Component

## Purpose

Compare one security or peer group against a benchmark, sector, or explicit peer set over dated return windows. Use this component for A-share technical, industry, and peer reports where the key question is whether performance is leading, lagging, or moving with the comparison set.

## Input Schema

```json
{
  "subject": "000001.SZ",
  "benchmark": "explicit benchmark or peer median",
  "windows": [
    {
      "label": "20 open dates",
      "subject_return_pct": 6.4,
      "benchmark_return_pct": 3.1,
      "spread_pct": 3.3,
      "start": "2026-04-16",
      "end": "2026-05-15",
      "source": "prices"
    }
  ]
}
```

Required: `subject`, `benchmark`, `windows[].label`, `windows[].subject_return_pct`, `windows[].benchmark_return_pct`, `windows[].spread_pct`, `windows[].start`, `windows[].end`, `windows[].source`.

Optional: `windows[].rank`, `windows[].sample_size`, `windows[].evidence`.

## Configuration

- Use `lc-relative-strength-panel`.
- Calculate returns from returned `prices` rows after aligning open dates.
- Use `trading-calendar` when natural date windows must be mapped to open dates.
- Label the benchmark explicitly: index, peer median, selected peers, or user-supplied comparison.
- Do not imply that relative strength predicts future returns.
- Do not output buy, sell, or hold language.

## HTML Snippet

```html
<section class="lc-relative-strength-panel" aria-labelledby="lc-relative-strength-title">
  <style>
    .lc-relative-strength-panel { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; color: oklch(24% 0.012 165); }
    .lc-relative-strength-panel__title { margin: 0 0 10px; font-size: 15px; font-weight: 700; }
    .lc-relative-strength-panel__wrap { overflow-x: auto; border: 1px solid oklch(88% 0.018 165); border-radius: 8px; }
    .lc-relative-strength-panel table { width: 100%; min-width: 560px; border-collapse: collapse; font-size: 12px; }
    .lc-relative-strength-panel th, .lc-relative-strength-panel td { padding: 9px 10px; border-bottom: 1px solid oklch(91% 0.014 165); text-align: right; }
    .lc-relative-strength-panel th:first-child, .lc-relative-strength-panel td:first-child { text-align: left; }
    .lc-relative-strength-panel th { color: oklch(45% 0.018 165); background: oklch(97% 0.006 165); font-weight: 700; }
    .lc-relative-strength-panel tr:last-child td { border-bottom: 0; }
    .lc-relative-strength-panel__note { margin: 10px 0 0; color: oklch(42% 0.018 165); font-size: 12px; line-height: 1.45; }
  </style>
  <h2 class="lc-relative-strength-panel__title" id="lc-relative-strength-title">Relative strength</h2>
  <div class="lc-relative-strength-panel__wrap">
    <table>
      <thead>
        <tr><th>Window</th><th>Subject</th><th>Benchmark</th><th>Spread</th><th>Date range</th></tr>
      </thead>
      <tbody>
        <tr><td>20 open dates</td><td>6.4%</td><td>3.1%</td><td>3.3pp</td><td>2026-04-16 to 2026-05-15</td></tr>
      </tbody>
    </table>
  </div>
  <p class="lc-relative-strength-panel__note">Returns are aligned to returned open dates and are not a forecast.</p>
</section>
```

## Missing Data Behavior

Do not fabricate benchmark rows, peer medians, ranks, date ranges, or return values. If the subject and benchmark windows cannot be aligned, show the unavailable window and disclose the mismatch in `source-footnote.md`.

## Example

Use after `benchmark-comparison.md` in annual reports, inside `framework-research-report.md` for sector comparisons, or beside `technical-state-table.md` when the user asks whether a stock is stronger than its benchmark.
