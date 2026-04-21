# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is an FX trading analysis workspace. It is not a software project — there is no build system, tests, or linting. The primary work here is running analytical skills, generating reports, and maintaining reference data.

## Skills

Two Claude Code skills are registered from this repo:

| Skill | Trigger | File |
|-------|---------|------|
| `fx-fundamental-analysis` | Analyse a currency pair, screen for FX setups, assess macro fundamentals | `fx-fundamental-analysis.skill` |
| `weekly-fx-overview` | Generate the weekly FX report (runs every Friday 21:00 UTC) | `weekly-fx-overview.skill` |

The `.skill` files are zip archives. The extracted source lives in `fx-skill-extracted/` and `weekly-fx-overview-extracted/` — edit SKILL.md files there, then repack if needed.

## Workflow Architecture

### FX Fundamental Analysis (Step 1 of FX strategy)

Scores 8 major currencies (USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF) across 7 indicators — inflation vs target, rate bias, unemployment, GDP, manufacturing PMI, services PMI, retail sales, and trade balance — then ranks them long/short and constructs pairs by conviction differential.

Data source hierarchy: **Trading Economics** → central bank publications → Bloomberg/Reuters.

Reference files:
- `fx-skill-extracted/fx-fundamental-analysis/references/central-banks.md` — per-currency rate targets, meeting cadence, hawkish/dovish language glossary
- `fx-skill-extracted/fx-fundamental-analysis/references/data-sources.md` — Trading Economics URL patterns and web search query templates

### Weekly FX Overview (automated Friday report)

Covers 19 currencies. Produces a structured `.md` report with: economic highlights, upcoming calendar, FX performance vs USD, and stock index weekly performance.

Output destinations:
- **GitHub**: `weekly-reports/YYYY-WXX.md` in repo `joewaiman/FX_Trading`
- **Notion**: new row in the Weekly FX Overview database (`f1e168c7-1f0e-447d-b185-de215949d17f`), parent page ID `344f5490-1aec-819e-87e3-e0efc16e651d`

Reference files:
- `weekly-fx-overview-extracted/weekly-fx-overview/references/indices.md` — full index-to-currency mapping (tickers, exchanges)
- `weekly-fx-overview-extracted/weekly-fx-overview/references/notion.md` — Notion database/page IDs and property schema
- `weekly-fx-overview-extracted/weekly-fx-overview/references/sources.md` — data source URLs and search templates

### GitHub publish command

```bash
gh api repos/joewaiman/FX_Trading/contents/weekly-reports/YYYY-WXX.md \
  --method PUT \
  --field message="Add weekly FX overview W{XX} {YYYY}" \
  --field content="$(base64 -i YYYY-WXX.md)"
```

## Data Files

| File | Contents |
|------|----------|
| `Files/SimplifiedTracker.csv` | Month-by-month unemployment rates (Mar 2022 → Dec 2026) for G8 + EM currencies, with 3.5%–4.5% gauge band |
| `Files/FXPAIRS - FXPAIRS.csv` | 19×19 cross-rate matrix (spot rates between all basket currencies) |
| `csv/` | Additional CSV output — currently empty |

## Currency Universe

- **Fundamental analysis (8 majors):** USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF
- **Weekly overview basket (19):** above + CNY, INR, BRL, MXN, NOK, SEK, DKK, PLN, HUF, SGD, ILS

## Tools Used

| Task | Tool |
|------|------|
| Fetch economic data pages | `web_fetch` (Trading Economics URLs) |
| Search for latest releases | `web_search` |
| Push reports to GitHub | `gh` CLI (Bash) |
| Update Notion database | Notion MCP (`notion-create-pages`, `notion-update-page`) |
