---
name: weekly-fx-overview
description: >
  Use this skill to produce a weekly FX and macro overview report. Triggers include:
  requests to generate the weekly report, run the Friday summary, produce the weekly
  FX wrap, or update the weekly Notion database. Runs automatically every Friday after
  market close. Covers: economic highlights per currency, upcoming economic calendar,
  all 19 currencies vs USD weekly performance, and major stock index weekly close.
---

# Weekly FX Overview Skill

Produces a structured weekly report covering economic highlights, FX performance, and
equity indices across the 19-currency basket. Output is pushed to GitHub as a `.md` file
and added as a new row to the Notion Weekly FX Overview database.

---

## Workflow Overview

```
1. Determine report week dates (Mon–Fri)
2. Fetch economic highlights — all 19 currencies
3. Fetch upcoming economic calendar — following week
4. Fetch FX performance vs USD — all 19 currencies
5. Fetch stock index weekly close + % change — one per currency
6. Format full report using output template
7. Push .md to GitHub → weekly-reports/YYYY-WXX.md
8. Add row to Notion Weekly FX Overview database
```

---

## Step 1 — Report Week

Determine the report dates:
- **Report week**: Monday to Friday of the current week
- **File name**: `YYYY-WXX.md` (ISO week number, e.g. `2026-W17.md`)
- **Report title**: `Weekly FX Overview — W{XX} | {Mon DD} – {Fri DD} {Mon} {YYYY}`

---

## Step 2 — Economic Highlights

For each of the 19 currencies, search for major economic releases during the report week.

**Currency → Country mapping:**
| Currency | Country / Region |
|----------|-----------------|
| USD | United States |
| EUR | Euro Area |
| GBP | United Kingdom |
| JPY | Japan |
| AUD | Australia |
| NZD | New Zealand |
| CAD | Canada |
| CHF | Switzerland |
| CNY | China |
| INR | India |
| BRL | Brazil |
| MXN | Mexico |
| NOK | Norway |
| SEK | Sweden |
| DKK | Denmark |
| PLN | Poland |
| HUF | Hungary |
| SGD | Singapore |
| ILS | Israel |

**For each currency, capture:**
- Any central bank rate decisions (outcome + forward guidance)
- CPI / inflation print (actual vs forecast vs prior)
- Employment / unemployment data
- GDP release (if any)
- PMI releases (manufacturing and/or services)
- Any other market-moving release

**Search query template:**
```
"{country} economic data {week date range} {year}"
"{country} central bank rate decision {month} {year}"
```

**Output per currency (if data released that week):**
```
**{CCY}** — {1–2 sentence summary of key releases and market reaction}
- {Release}: Actual X.X% | Forecast X.X% | Prior X.X%
```

Skip currencies with no major releases that week — note as "No major releases."

---

## Step 3 — Upcoming Economic Calendar

Fetch the following week's scheduled data releases.

**Source:** `https://tradingeconomics.com/calendar`

For each of the 19 currencies, list:
- Release name
- Scheduled date
- Forecast (if available)
- Prior reading

**Format:**
```
| Date | Currency | Release | Forecast | Prior |
```

Prioritise: rate decisions > CPI > employment > GDP > PMI > retail sales > trade balance

---

## Step 4 — FX Performance vs USD

Fetch the weekly % change for all 19 currencies against USD.

**Search query:** `"{currency pair} weekly performance {date range}"`
or fetch from `https://tradingeconomics.com/{country}/currency`

**Report the following for each:**
- Weekly % change vs USD (+ = currency strengthened vs USD, – = weakened)
- Current spot rate

**Output format:**
```
| Currency | Spot vs USD | Weekly Change |
|----------|-------------|---------------|
| EUR      | 1.0821      | +0.45%        |
| GBP      | 1.2734      | -0.21%        |
```

Sort by weekly change descending (strongest performer first).

---

## Step 5 — Stock Index Weekly Performance

One index per currency. Fetch weekly close price and % change.

**Index mapping:**
| Currency | Index | Ticker |
|----------|-------|--------|
| USD | S&P 500 | SPX |
| USD | S&P 100 | OEX |
| EUR | Euro Stoxx 50 | SX5E |
| EUR | DAX | DAX |
| GBP | FTSE 100 | UKX |
| JPY | Nikkei 225 | NI225 |
| AUD | ASX 200 | AS51 |
| NZD | NZX 50 | NZ50 |
| CAD | TSX Composite | OSPTX |
| CHF | SMI | SMI |
| CNY | Shanghai Composite | SHCOMP |
| INR | Nifty 50 | NIFTY |
| BRL | Ibovespa | IBOV |
| MXN | IPC | MXX |
| NOK | OBX | OBX |
| SEK | OMX Stockholm 30 | OMX |
| DKK | OMX Copenhagen 20 | OMXC20 |
| PLN | WIG20 | WIG20 |
| HUF | BUX | BUX |
| SGD | Straits Times Index | STI |
| ILS | TA-125 | TA125 |

**For each index, report:**
- Closing level (Friday close)
- Weekly % change
- Weekly absolute point change

**Output format:**
```
| Currency | Index | Close | Wk Chg (pts) | Wk Chg (%) |
|----------|-------|-------|--------------|------------|
| USD | S&P 500 | 5,412 | +87 | +1.63% |
```

Sort by weekly % change descending.

---

## Step 6 — Format Report

Use the following markdown template:

```markdown
# Weekly FX Overview — W{XX} | {Mon DD} – {Fri DD} {Mon} {YYYY}

*Generated: {Friday date} | Basket: 19 currencies | Source: Trading Economics, web search*

---

## 1. Economic Highlights

{Per-currency summaries from Step 2}

---

## 2. Upcoming Economic Calendar — W{XX+1}

| Date | Currency | Release | Forecast | Prior |
|------|----------|---------|----------|-------|
{rows from Step 3}

---

## 3. FX Performance vs USD

| Currency | Spot vs USD | Weekly Change |
|----------|-------------|---------------|
{rows from Step 4, sorted by weekly change desc}

---

## 4. Stock Index Weekly Performance

| Currency | Index | Close | Wk Chg (pts) | Wk Chg (%) |
|----------|-------|-------|--------------|------------|
{rows from Step 5, sorted by weekly % change desc}

---

*FX trading carries significant risk. This report is for informational purposes only.*
```

---

## Step 7 — Push to GitHub

Push the formatted `.md` file to the GitHub repo.

**Repo:** `joewaiman/FX_Trading`
**Path:** `weekly-reports/YYYY-WXX.md`
**Commit message:** `Add weekly FX overview W{XX} {YYYY}`

Use the GitHub MCP tool or `gh` CLI:
```bash
gh api repos/joewaiman/FX_Trading/contents/weekly-reports/YYYY-WXX.md \
  --method PUT \
  --field message="Add weekly FX overview W{XX} {YYYY}" \
  --field content="$(base64 -i YYYY-WXX.md)"
```

---

## Step 8 — Update Notion Database

Add a new row to the **Weekly FX Overview** Notion database.

**Database location:** FX Fundamental Analysis page in Notion workspace
**Database ID:** `f1e168c7-1f0e-447d-b185-de215949d17f` (see references/notion.md)

**Row properties to set:**
| Property | Value |
|----------|-------|
| Week | `W{XX} — {Mon DD}–{Fri DD} {Mon} {YYYY}` |
| Date | Friday of the report week |
| GitHub Link | URL to the `.md` file on GitHub |
| Top Gainer vs USD | Best performing currency that week |
| Top Loser vs USD | Worst performing currency that week |
| Key Events | 1–2 sentence summary of the week's biggest macro event |

**Row content (opened page):** Paste the full formatted markdown report into the page body.

---

## Tools to Use

| Task | Tool |
|------|------|
| Fetch economic data | `web_search`, `web_fetch` (Trading Economics) |
| Fetch FX rates | `web_search`, Trading Economics |
| Fetch index data | `web_search` |
| Push to GitHub | `gh` CLI via Bash |
| Update Notion | Notion MCP tools (`notion-create-pages`, `notion-update-page`) |

See `references/indices.md` for full index mapping details.
See `references/sources.md` for data source URLs and search templates.

---

## Scheduling

This skill runs automatically every **Friday at 21:00 UTC** (approximately 4–5pm EST,
after US market close).

Trigger type: Remote scheduled agent
Schedule: `0 21 * * 5` (cron — every Friday at 21:00 UTC)

---

## Important Notes

- Always state the data date for each figure
- If an index or FX rate is unavailable, note it as "N/A — market closed or data pending"
- Currency performance is vs USD only (not cross-rates)
- This report is informational only — not investment advice
