---
name: longchina-data
version: 0.1.1
description: Use when a user needs authoritative P0 A-share market, daily indicator, adjustment factor, stock master, or trading calendar data through the longchina CLI/API. The skill must fetch real data via `longchina` and must not invent investment data.
---

# longchina Data

Use the longchina CLI as the source of truth for A-share structured data.

## Install and verification

If `longchina` is not installed, read the machine install guide at `/install.txt` for the current site. Do not fetch the homepage for installation. The recommended CLI installer is:

```bash
curl -fsSL https://longchina.vercel.app/install.sh | sh
```

If the skills CLI is unavailable, use the manual skill install fallback in `/install.txt` instead of asking the user to install Node.js as the first remedy. That fallback installs into the shared agent skill root `~/.agents/skills/longchina-data`, which is the supported manual fallback path for Codex, Claude Code, and Cursor.

Before data work, verify the current runtime:

```bash
longchina status --json --skill-version 0.1.1
```

`status` performs the periodic CLI/skill version policy check. If the JSON response contains `version.cli.update_required: true` or `version.skill.update_required: true`, reinstall the CLI and this skill before continuing. Minor-version updates may be reported as available but are not blocking.

The CLI defaults to `https://longchina.vercel.app/api`. For local development or preview deployments, pass `--api-url URL` on `status`, `datasets`, or `query`, or set `LONGCHINA_API_URL`.

If the environment provides an API key, token login is optional:

```sh
if [ -n "${LONGCHINA_API_KEY:-}" ]; then
  echo "$LONGCHINA_API_KEY" | longchina login --with-token --json
  longchina status --json --skill-version 0.1.1
fi
```

## Required workflow

1. Run `longchina status --json --skill-version 0.1.1` before data work, and obey any required update in the returned `version` block before querying.
2. Inspect available datasets with `longchina datasets --json` when the requested dataset or field is unclear.
3. Fetch data with `longchina query ...`; prefer narrow `--fields`, explicit `--ts-code`, and bounded `--start`/`--end`.
4. Prefer `--format json` for machine parsing and `--format csv` for user-facing tables.
5. Use the CLI option `--order-by` for sorting when needed; do not use the API field name `order_by` as a command-line option.
6. Report the returned data and include dataset name, filters, date range, fields, and cache/usage metadata when available.
7. If the user asks for 可视化, 图表, 走势, chart, plot, graph, comparison report, trend report, or metric table output, fetch the authoritative data first and then use `stock-visualization` for rendering.
8. Do not fabricate prices, financial values, trading dates, returned rows, ratings, or usage numbers. If the CLI/API returns no rows, say that no rows were returned for the filters.
9. Do not ask users to manually sync server data. If a query returns no rows or partial rows, report the exact filters, row counts, and available metadata instead of inventing or implying unavailable data.

## Agent command contract

- Use `longchina query daily` for daily OHLCV data.
- Use `longchina query daily-basic` for valuation, turnover, market cap, and share-count indicators.
- Use `longchina query stock-basic` for names, exchange, lifecycle dates, and universe construction.
- Use `longchina query trade-cal` before assuming a natural date was an open trading day.
- Use `longchina query adj-factor` when the task needs raw adjustment factors.
- Use `longchina query income`, `balancesheet`, `cashflow`, `fina-indicator`, `forecast`, `express`, `dividend`, `fina-audit`, `fina-mainbz`, and `disclosure-date` for fundamental research data.
- Use `longchina query moneyflow`, `margin`, `margin-detail`, `stk-limit`, `top-list`, `top-inst`, `block-trade`, `repurchase`, and `hk-hold` for stock-pool review signals.
- Use `longchina query top10-holders`, `top10-floatholders`, `stk-holdernumber`, `stk-holdertrade`, `pledge-stat`, and `pledge-detail` for shareholder and pledge-risk context.
- Treat every CLI result as authoritative only for the requested filters and returned rows.

## Dataset references

- Read `references/datasets.md` when choosing fields, filters, or dataset names.
- Read `references/examples.md` when composing CLI commands.

## Guardrails

- This skill provides data access, not investment advice.
- Prefer CSV output for tabular user-facing answers and JSON output for downstream code or agent processing.
- For large date ranges or all-market requests, warn that the API may return an export job instead of inline rows.
- Never request or expose upstream vendor credentials; users authenticate to longchina, and longchina handles upstream sources.
- Platform data is not investment advice. Do not produce buy/sell/hold recommendations unless the user explicitly asks for an analysis workflow and the appropriate disclaimers/risk rules are available.
