# Notion Reference — Daily FX Economist Briefing

## Parent Page

- **Parent page**: FX Fundamental Analysis — 19 Currency Basket (April 2026)
- **Parent page ID**: `344f5490-1aec-819e-87e3-e0efc16e651d`

## Daily FX Economist Briefing Database

- **Database URL**: https://www.notion.so/212dc8759ae649e8841d91a2f6ed9923
- **Data Source ID**: d814e60d-a915-4474-84af-8559aa84b0af
- **Database name**: "Daily FX Economist Briefing"

**Schema (properties):**
| Property | Type | Notes |
|----------|------|-------|
| Date | TITLE | "Mon 19 May 2026" |
| date:Date:start | DATE | ISO date e.g. "2026-05-19" |
| Strongest | TEXT | Top 3 currencies e.g. "GBP, AUD, BRL" |
| Weakest | TEXT | Bottom 3 currencies e.g. "JPY, CAD, SEK" |
| Key Release | TEXT | Most important release of the day |
| Economist Bias | TEXT | 1-sentence macro narrative |
| GitHub Link | URL | Link to .md file on GitHub |
| Status | SELECT | "Published" |

## Adding a New Daily Row

Use `notion-create-pages` with:
```
parent: { type: "data_source_id", data_source_id: "d814e60d-a915-4474-84af-8559aa84b0af" }
```

Properties to set per row:
| Property | Type | Example |
|----------|------|---------|
| Date | TITLE | "Mon 19 May 2026" |
| date:Date:start | DATE | "2026-05-19" |
| Strongest | TEXT | "GBP, AUD, BRL" |
| Weakest | TEXT | "JPY, CAD, SEK" |
| Key Release | TEXT | "US CPI: 3.1% vs 3.0% forecast — Beat" |
| Economist Bias | TEXT | "USD hawkish bias holds; EUR pressure mounts on weak PMI" |
| GitHub Link | URL | "https://github.com/joewaiman/FX_Trading/blob/main/daily-briefings/2026-05-19.md" |
| Status | SELECT | "Published" |

## First-Run Setup

Database already exists — no creation step needed. Use the Data Source ID above directly.
