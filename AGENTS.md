# AGENTS.md

## Skill Safety Policy

Skills in this repository must be low-permission instruction packs. Do not place software installation commands, remote shell execution, filesystem write fallbacks, token login flows, or secret-handling examples inside `SKILL.md`.

The `longchina-data` skill may run read-only longchina commands:

- `longchina status --json --skill-version ...`
- `longchina datasets --json`
- `longchina query ...`

It must not run or document commands such as remote installers, package-manager based skill installation, manual writes into agent skill directories, or token-login snippets. Installation belongs in README or the longchina website, not in the installed skill body.

## Public Naming Policy

Use longchina public names in all skill content:

- Datasets: `prices`, `daily-metrics`, `securities`, `trading-calendar`, `adjustments`.
- Fields and filters: `symbol`, `date`, `previous_close`, `percent_change`, `volume`, `total_market_value`, `float_market_value`, `listing_status`, `previous_open_date`, `adjustment_multiplier`.

Do not expose upstream provider names or provider-specific field/dataset names in public skill text.
