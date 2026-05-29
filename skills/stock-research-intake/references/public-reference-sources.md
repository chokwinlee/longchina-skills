# Public Reference Sources

Use this reference when Longchina data is not enough for the requested analysis and the user would benefit from a cited public source. These sources supplement Longchina evidence; they do not replace Longchina dataset names, field names, row counts, or source metadata.

## Selection Rules

- Prefer official exchanges, regulators, company disclosure platforms, central-bank or statistics agencies, and index publishers.
- Record source name, URL, retrieval date, publication date when visible, and the exact evidence used.
- Treat each public source as dated external evidence. Do not merge it into Longchina rows unless a local adapter has a tested mapping.
- Never fabricate source values, coverage, update cadence, or historical availability.
- If a source has disclaimers, lagged release timing, license restrictions, or paid redistribution limits, state that limitation in the answer or visual footnote.
- Use the Chinese original when an English translation says the Chinese version prevails.

## Source Map

| Need | Preferred public sources | Use for | Cautions |
| --- | --- | --- | --- |
| Exchange prices, listings, trading mechanisms, market statistics | Shanghai Stock Exchange, Shenzhen Stock Exchange | Cross-check security status, exchange market pages, market statistics, trading rules, disclosed data-service coverage | Some real-time and historical products require licensed access; do not imply unrestricted bulk access |
| Company announcements and filings | Exchange announcement pages, CNINFO, CSRC disclosure rules | Annual reports, interim reports, dividends, buybacks, major asset events, ownership changes, risk warnings | Cite the filing date and document title; do not summarize financial statements without reading the relevant report |
| Stock Connect and northbound context | HKEX Stock Connect pages and HKEXnews shareholding search | Eligibility, quota context, northbound/southbound shareholding snapshots, cross-boundary market access notes | Shareholding search carries HKEX disclaimers; real-time or near-real-time flow data may be unavailable or restricted |
| Macro liquidity and credit | People's Bank of China statistical releases | Money supply, aggregate financing, credit impulse, policy-report context | Macro liquidity is market context, not proof of single-stock capital inflow |
| Macro cycle and sector demand context | National Bureau of Statistics of China | GDP, CPI, PPI, industrial production, fixed-asset investment, industrial profits, retail sales | Use as macro or sector context only; do not infer one company's results from macro aggregates |
| Risk-free rate and discount-rate context | ChinaBond yield curves | Scenario assumptions, valuation discount-rate cross-check, bond-market context | Record curve date, tenor, unit, and whether the value is a yield-to-maturity curve |
| Index composition and methodology | China Securities Index, exchange index pages | Benchmark choice, constituent universe, sector or style classification | Confirm methodology date; do not assume historical constituents unless the source provides them |

## Canonical Access Points

Use these official entry points first. If the page structure changes, search within the same official domain before falling back to a broader web search.

| Source | Entry point | Typical evidence | Notes |
| --- | --- | --- | --- |
| Shanghai Stock Exchange | `https://english.sse.com.cn/news/publications/monthly/` | Monthly market statistics, listed company and market tables | The monthly publication page says it provides statistics covering market quotation, members, listed companies, and exchange announcements. |
| Shenzhen Stock Exchange | `https://www.szse.cn/English/services/dataServices/index.html` | Data-service coverage, delayed or end-of-day fields, market-data service descriptions | Use as a coverage reference; do not imply free bulk redistribution for licensed feeds. |
| HKEX Stock Connect | `https://www.hkex.com.hk/mutual-market/stock-connect?sc_lang=en` | Eligible securities, Stock Connect statistics, trading arrangements, reference materials | Use for program context and eligibility; cite the exact subpage or downloaded file when used. |
| HKEX Stock Connect shareholding search | `https://www2.hkexnews.hk/Shareholding-Disclosures/Stock-Connect-Shareholding?sc_lang=en` | Northbound or southbound shareholding snapshots by date | Disclose the HKEX disclaimer and retrieval date; this is reference evidence, not Longchina row data. |
| People's Bank of China | `https://www.pbc.gov.cn/en/3688247/3688978/3709140/48b09237-2.html` | Aggregate financing reports and macro-liquidity releases | The English site states that the Chinese original prevails when translations differ. |
| National Bureau of Statistics of China | `https://www.stats.gov.cn/english/` | GDP, CPI, PPI, industrial production, fixed-asset investment, retail sales, industrial profits | Prefer the dated release or database page used for the exact value. |
| ChinaBond yield curves | `https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US` | Government-bond yield curve and tenor-specific yield assumptions | Record curve date, curve name, tenor, and unit. |
| China Securities Index | `https://www.csindex.com.cn/` | Index methodology, constituent files, benchmark definitions | If using a PDF or download, cite the document title and publication or retrieval date. |

## Analysis Use

Use public reference data in these cases:

- A valuation, DCF, or scenario answer needs a risk-free-rate assumption.
- A capital-flow answer needs Stock Connect shareholding context, ETF/fund context, or market-wide liquidity context that Longchina does not return.
- An industry-cycle answer needs macro demand, policy, production, price, or inventory evidence.
- A fundamental answer needs filings, annual reports, dividends, buybacks, management discussion, or risk warnings.
- A peer or benchmark answer needs official index methodology or constituent definitions.

Keep these sources out of the Longchina evidence bucket. Label them as `public reference` in prose and `external_references` or source footnotes in visual artifacts.

## Output Contract

When using a public source, include:

```json
{
  "source_type": "public reference",
  "source_name": "Source name",
  "url": "https://example.org/path",
  "retrieved_at": "YYYY-MM-DD",
  "published_at": "YYYY-MM-DD or unavailable",
  "evidence_used": "Short description of the exact row, table, report, or statement used",
  "limitation": "Lag, disclaimer, license, translation, or coverage note"
}
```

If the answer is a visual report, pass the same fields to `stock-visualization` so `source-footnote.md` can disclose them.
