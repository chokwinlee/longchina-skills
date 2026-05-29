# Metric Table Recipe

Use this recipe when the user asks for a sortable table over a stock pool or a constrained market or industry subset.

## When To Use

- "Make a sortable table for these 30 stocks by PE and PB."
- "Rank this industry by market value and turnover."
- "Create an HTML screening table with current valuation metrics."

## Datasets To Query

Use `longchina-data` and fetch:

- `securities` for names, industries, exchange, market, and lifecycle status.
- `daily-metrics` for valuation, turnover, shares, and market value.
- `prices` only when the table includes close price or recent return.
- `trading-calendar` when translating a natural date into latest trading date.

## Data Contracts

Fill:

- `SecurityProfile` for display names and industries.
- `MetricSnapshot` for latest metrics.
- `ComparisonRow` for table rows.
- `SourceDisclosure`.

## Components

Compose:

1. `chart-frame.md` when the table is visual, dense, or benefits from fullscreen inspection.
2. `sortable-table.md`.
3. Plain text metric definitions when needed.
4. Plain text scope note for stock pool, industry, row limit, or date.
5. `source-footnote.md`.

## Missing Data Behavior

- Require explicit limits for all-market or industry requests.
- Keep missing numeric values visible as `--`.
- Sort missing numeric values after real values in ascending order.
- If the dataset would produce too many rows, ask for a limit or generate a summarized table with an export note.

## Required Footnote Details

Include stock pool definition, limit, dataset fields, filters, row count, latest trading date, generation time, and risk note.
