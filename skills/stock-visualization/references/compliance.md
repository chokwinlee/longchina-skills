# Compliance

This skill renders data and labeled observations. It does not turn a chart into investment advice by default.

## Default Output

Generated HTML should default to:

- Factual summaries.
- Visual comparisons.
- Data source notes.
- Missing-data notes.
- Neutral wording.

Examples of acceptable neutral language:

- `PE TTM is higher than the comparison group on the latest returned trading date.`
- `No daily-basic rows were returned for the selected interval.`
- `The two securities use different latest trading dates; inspect row-level dates before comparing values.`

## Investment Views

If the user explicitly asks for an investment view, the report may include a labeled analysis block. The block must include:

- Source datasets and date ranges.
- Assumptions.
- Data limitations.
- Risk notes.
- No promise of returns or certainty.

Do not write buy, sell, or hold language unless the user directly requested that level of opinion. Prefer phrasing like `analysis observation` or `scenario note` over absolute conclusions.

## Required Source Disclosure

Every page must disclose:

- Generation time.
- Dataset names.
- Fields requested.
- Filters and date ranges.
- Row counts when available.
- Cache, usage, or point metadata when available.
- Missing data that affects interpretation.
- A risk note.

## Missing Data

Use `--`, `null`, or an explicit empty state. Do not fill gaps by guessing. If a component omits a series or metric because of missing data, record that omission in the Source Footnote.
