# Notion Reference — Weekly FX Overview

## Weekly FX Overview Database

- **Database URL**: https://www.notion.so/f682c75e0a264f6392c1acc92b0212b8
- **Data Source ID**: f1e168c7-1f0e-447d-b185-de215949d17f
- **Parent page**: FX Fundamental Analysis — 19 Currency Basket (April 2026)
- **Parent page ID**: 344f5490-1aec-819e-87e3-e0efc16e651d

## Adding a New Weekly Row

Use `notion-create-pages` with:
```
parent: { type: "data_source_id", data_source_id: "f1e168c7-1f0e-447d-b185-de215949d17f" }
```

Properties to set per row:
| Property | Type | Example |
|----------|------|---------|
| Week | TITLE | "W17 — Apr 14–17 2026" |
| date:Date:start | DATE | "2026-04-17" |
| GitHub Link | URL | "https://github.com/joewaiman/FX_Trading/blob/main/weekly-reports/2026-W17.md" |
| Top Gainer vs USD | TEXT | "BRL +1.2%" |
| Top Loser vs USD | TEXT | "CAD -0.8%" |
| Key Events | TEXT | "Fed held rates at 3.75%; US CPI beat at 3.3%" |
| Status | SELECT | "Published" |
