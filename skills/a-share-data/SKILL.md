---
name: longchina-data
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
longchina status --json
```

The CLI defaults to `https://longchina.vercel.app/api`. For local development or preview deployments, pass `--api-url URL` on `status`, `datasets`, or `query`, or set `LONGCHINA_API_URL`.

If the environment provides an API key, token login is optional:

```sh
if [ -n "${LONGCHINA_API_KEY:-}" ]; then
  echo "$LONGCHINA_API_KEY" | longchina login --with-token --json
  longchina status --json
fi
```

## Required workflow

1. Run `longchina status --json` before data work.
2. Inspect available datasets with `longchina datasets --json` when the requested dataset or field is unclear.
3. Fetch data with `longchina query ...`; prefer narrow `--fields`, explicit `--ts-code`, and bounded `--start`/`--end`.
4. Prefer `--format json` for machine parsing and `--format csv` for user-facing tables.
5. Report the returned data and include dataset name, filters, date range, fields, and cache/usage metadata when available.
6. Do not fabricate prices, financial values, trading dates, returned rows, ratings, or usage numbers. If the CLI/API returns no rows, say that no rows were returned for the filters.
7. Do not ask users to manually sync server data. If a query returns no rows or partial rows, report the exact filters, row counts, and available metadata instead of inventing or implying unavailable data.

## Agent command contract

- Use `longchina query daily` for daily OHLCV data.
- Use `longchina query daily-basic` for valuation, turnover, market cap, and share-count indicators.
- Use `longchina query stock-basic` for names, exchange, lifecycle dates, and universe construction.
- Use `longchina query trade-cal` before assuming a natural date was an open trading day.
- Use `longchina query adj-factor` when the task needs raw adjustment factors.
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
