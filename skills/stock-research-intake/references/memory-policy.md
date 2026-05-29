# Memory Policy

The skill uses local Longchina memory files:

```text
~/.longchina/memories/
  USER.md
  MEMORY.md
  facts.jsonl
```

`USER.md` stores compact natural-language user preferences. `MEMORY.md` stores agent-side operating facts. `facts.jsonl` stores structured evidence for preference updates.

## Save Proactively

Save stable preferences when they will reduce repeated questions:

- Preferred language and response length.
- Preferred answer shape, such as concise conclusion first, table first, or evidence first.
- Default stock-analysis period.
- Preferred analysis angle, such as trend, valuation, risk, peer comparison, annual performance, or table-only screening.
- Visualization preference, such as ask before HTML or generate visual report by default.
- Investment profile details when the user states them clearly: horizon, risk tolerance, capital context, holding context, and watchlist or holding symbols.

A visualization preference that changes routing must be clearly stated by the user before saving. Do not infer a durable visual-report default from occasional chart or HTML requests.

## Do Not Infer Investment Profile From Weak Behavior

Do not infer investment profile from weak behavior.

- Repeated questions about one industry do not prove a concentrated holding.
- Asking about volatile securities does not prove high risk tolerance.
- Asking about a security does not mean the user holds it.
- Comparing two securities does not prove either is in the user's portfolio.

Only save holding, capital, risk tolerance, or horizon details when the user states them clearly.

## Helper Command Contract

The memory helper writes JSON responses and supports these commands:

- `read`: return current user preferences, agent memory, and recent facts.
- `summarize`: return a compact natural-language memory summary.
- `add-user <entry>`: append a stable user preference.
- `replace-user <match> <entry>`: replace matching user preference text.
- `remove-user <match>`: remove matching user preference text.
- `add-memory <entry>`: append a stable agent-side operating fact.
- `replace-memory <match> <entry>`: replace matching agent memory text.
- `remove-memory <match>`: remove matching agent memory text.
- `append-fact <json>`: append one structured evidence object to `facts.jsonl`.
- `remove-fact <match>`: remove facts whose `raw`, `canonical`, or `type` contains the match.

Fact objects use this shape:

```json
{
  "type": "presentation.language",
  "canonical": "zh-CN",
  "raw": "User prefers Chinese responses.",
  "source": "explicit_user_statement",
  "confidence": 0.95,
  "updated_at": "2026-05-22T00:00:00Z"
}
```

Use `updated_at` only when the helper or caller has a trustworthy timestamp.

## Never Save Credentials

Never save credentials, account identifiers, API keys, tokens, authentication details, raw data dumps, large tables, logs, temporary task progress, or automated trading instructions.

## Replace Or Consolidate

When a new preference updates an older preference, replace or consolidate the old entry. Do not append duplicates.

Good:

```md
User prefers Chinese stock-analysis responses with concise conclusion first, then evidence.
```

Bad:

```md
User likes Chinese.
User likes concise answers.
User likes evidence.
```

## Task-End Summary

At task end, briefly report material memory updates.

Do not interrupt every low-risk memory write. At the end of the task, briefly report material memory changes:

```text
已更新偏好：默认中文；股票分析先给结论；不自动生成 HTML 可视化报告。
```

If the user says not to remember something, skip the write. If the user asks to forget something, remove the matching memory entry and matching facts when present.
