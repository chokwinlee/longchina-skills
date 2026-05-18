---
name: longchina-data
version: 0.1.2
description: Use when a user needs authoritative P0 A-share prices, daily metrics, security metadata, adjustments, or trading calendar data through the longchina CLI/API.
---

# longchina Data

Use the longchina CLI as the source of truth for A-share structured data.

## Runtime verification

Before data work, verify the current runtime:

```bash
longchina status --json --skill-version 0.1.2
```

If `longchina` is unavailable, stop and tell the user that the longchina CLI is required before data work. This skill does not install software, modify shell profile files, write skill files, or perform authentication setup.

`status` performs the periodic CLI/skill version policy check. If the JSON response contains `version.cli.update_required: true` or `version.skill.update_required: true`, reinstall the CLI and this skill before continuing. Minor-version updates may be reported as available but are not blocking.

The CLI defaults to `https://longchina.vercel.app/api`. For local development or preview deployments, pass `--api-url URL` on `status`, `datasets`, or `query`, or set `LONGCHINA_API_URL`.

## Required workflow

1. Run `longchina status --json --skill-version 0.1.2` before data work, and obey any required update in the returned `version` block before querying.
2. Inspect available datasets with `longchina datasets --json` when the requested dataset or field is unclear.
3. Fetch data with `longchina query ...`; prefer narrow `--fields`, explicit `--symbol`, and bounded `--start`/`--end`.
4. Prefer `--format json` for machine parsing and `--format csv` for user-facing tables.
5. Use the CLI option `--order-by` for sorting when needed; do not use the API field name `order_by` as a command-line option.
6. Report the returned data and include dataset name, filters, date range, fields, and cache/usage metadata when available.
7. If the user asks for 可视化, 图表, 走势, chart, plot, graph, comparison report, trend report, or metric table output, fetch the authoritative data first and then use `stock-visualization` for rendering.
8. Do not fabricate prices, financial values, trading dates, returned rows, ratings, or usage numbers. If the CLI/API returns no rows, say that no rows were returned for the filters.
9. Do not ask users to manually sync server data. If a query returns no rows or partial rows, report the exact filters, row counts, and available metadata instead of inventing or implying unavailable data.

## Agent command contract

- Use `longchina query prices` for daily OHLCV data.
- Use `longchina query daily-metrics` for valuation, turnover, market cap, and share-count indicators.
- Use `longchina query securities` for names, exchange, lifecycle dates, and universe construction.
- Use `longchina query trading-calendar` before assuming a natural date was an open trading day.
- Use `longchina query adjustments` when the task needs raw adjustment factors.
- Do not use unlisted dataset names. Run `longchina datasets --json` first when the requested dataset is not covered by the commands above.
- Treat every CLI result as authoritative only for the requested filters and returned rows.

## Dataset references

- Read `references/datasets.md` when choosing fields, filters, or dataset names.
- Read `references/examples.md` when composing CLI commands.

## Guardrails

- This skill provides data access, not investment advice.
- Prefer CSV output for tabular user-facing answers and JSON output for downstream code or agent processing.
- For large date ranges or all-market requests, warn that the API may return an export job instead of inline rows.
- Do not request, print, or configure secrets. This skill only runs read-only longchina status, dataset, and query commands.
- Platform data is not investment advice. Do not produce buy/sell/hold recommendations unless the user explicitly asks for an analysis workflow and the appropriate disclaimers/risk rules are available.
