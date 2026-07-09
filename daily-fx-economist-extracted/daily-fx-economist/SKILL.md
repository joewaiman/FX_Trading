---
name: daily-fx-economist
description: >
  Use this skill to produce a daily FX economist briefing across the 19-currency basket.
  Triggers include: requests to run the daily briefing, morning FX report, economist update,
  check overnight moves, or update the daily Notion database. Runs automatically every weekday
  morning at 06:30 UTC (before London open). Covers: overnight economic releases, today's
  calendar, 24h FX moves vs USD, per-currency economist scorecard update, and top trade setups.
---

# Daily FX Economist Briefing Skill

Produces a structured daily economist briefing before each London open. The agent acts as a
macro economist — it does not just fetch data, it interprets releases with economic reasoning,
maintains a per-currency fundamental scorecard, and identifies currencies at inflection points.

Output is pushed to GitHub as a `.md` file and added as a new row to the Notion Daily FX
Economist Briefing database.

---

## Workflow Overview

```
1. Determine session dates and context
2. Fetch overnight economic releases — all 19 currencies
3. Fetch today's economic calendar — all 19 currencies
4. Fetch 24h FX moves vs USD — all 19 currencies
5. Update economist scorecard — revise only currencies with new data
6. Identify top trade setups — strongest vs weakest fundamental divergence
7. Format full briefing using output template
8. Push .md to GitHub → daily-briefings/YYYY-MM-DD.md
9. Add row to Notion Daily FX Economist Briefing database
```

---

## Step 1 — Session Context

Determine the date and active sessions:

- **Report date**: today (`YYYY-MM-DD`)
- **Active sessions at 06:30 UTC**: Asian session closing, London opening
- **File name**: `YYYY-MM-DD.md`
- **Report title**: `Daily FX Economist Briefing — {Weekday}, {DD} {Month} {YYYY}`

State which major central bank decisions or tier-1 data releases are due **today** in the
opening sentence — this sets the tone for the briefing.

---

## Step 2 — Overnight Economic Releases

Search for economic data released in the past 24 hours across all 19 currencies.

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

**For each currency with a release, capture:**
- Release name and actual vs forecast vs prior
- Whether it beat, missed, or matched consensus
- Economist interpretation: what does this mean for rate path / currency outlook?

**Search query template:**
```
"{country} economic data release {date} {year}"
"{country} {release name} {month} {year} actual result"
```

**Output per currency (economist-style):**
```
**{CCY}** — {1–2 sentence economist interpretation, not just the number}
- {Release}: Actual X.X% | Forecast X.X% | Prior X.X% | [Beat / Miss / In-line]
- *Implication*: {one sentence on what this means for {CB name} policy or currency bias}
```

Currencies with no overnight releases: group at the bottom as "No releases overnight."

---

## Step 3 — Today's Economic Calendar

Fetch today's scheduled data releases for all 19 currencies.

**Source:** `https://tradingeconomics.com/calendar`

Prioritise by market impact:
1. Central bank rate decisions (CRITICAL)
2. CPI / inflation prints (HIGH)
3. Employment / NFP / unemployment (HIGH)
4. GDP (HIGH)
5. PMI manufacturing / services (MEDIUM)
6. Retail sales, trade balance (MEDIUM)
7. Other (LOW — include only if market-moving)

**Output format:**
```
| Time (UTC) | Currency | Release | Forecast | Prior | Impact |
|------------|----------|---------|----------|-------|--------|
```

Add an **Economist's Watch** note below the table: 1–2 sentences on which release today
matters most and why, with context on the current policy stance.

---

## Step 4 — Overnight FX Moves vs USD

Fetch the 24-hour % change for all 19 currencies against USD as of report time.

**Pairs format:** EURUSD, GBPUSD, AUDUSD, NZDUSD (direct) vs USDJPY, USDCHF, USDCAD,
USDCNY, USDINR, USDBRL, USDMXN, USDNOK, USDSEK, USDDKK, USDPLN, USDHUF, USDSGD, USDILS
(inverted — convert to currency-strength perspective: +% means currency strengthened vs USD).

**Output format:**
```
| Currency | 24h Change vs USD | Spot Rate |
|----------|-------------------|-----------|
```
Sort descending by 24h change (strongest on top).

---

## Step 5 — Economist Scorecard Update

This is the core of the economist's role. Maintain a per-currency fundamental scorecard.
**Only update currencies where new data was released today (Step 2) or a policy shift occurred.**
For unchanged currencies, carry forward the prior score.

**Scorecard dimensions per currency:**
| Dimension | Scale | Description |
|-----------|-------|-------------|
| Rate Bias | Hawkish / Neutral / Dovish | Central bank's current policy direction |
| Inflation Trend | Rising / Stable / Falling | Direction of CPI vs target |
| Growth Outlook | Positive / Neutral / Negative | GDP trajectory, PMI trend |
| Labour Market | Tight / Neutral / Loosening | Employment conditions |
| Overall Bias | Bullish / Neutral / Bearish | Net fundamental verdict for currency |

**G8 currencies** (USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF): score all 5 dimensions.
**Non-G8 currencies** (CNY, INR, BRL, MXN, NOK, SEK, DKK, PLN, HUF, SGD, ILS): score
Rate Bias, Inflation Trend, and Overall Bias only.

**Output format (per updated currency):**
```
**{CCY}** [{Overall Bias}] ← UPDATED (was: {prior bias})
- Rate Bias: {Hawkish/Neutral/Dovish} | Inflation: {Rising/Stable/Falling} | Growth: {Positive/Neutral/Negative}
- *Change driver*: {what data or event caused the update}
```

For unchanged currencies:
```
**{CCY}** [{Overall Bias}] — no change
```

See `references/scorecard.md` for the starting scorecard baseline and scoring criteria.

---

## Step 6 — Top Trade Setups

Based on the updated scorecard from Step 5, identify the 2–3 strongest fundamental divergence
setups for today.

**Method:**
1. Rank all 19 currencies: Bullish (3 pts), Neutral (1 pt), Bearish (0 pts)
2. Pair the highest-ranked currency vs the lowest-ranked with confirmed liquidity
3. Only include pairs where:
   - Both currencies have G8 liquidity OR one is a major cross (NOK, SEK, PLN, HUF)
   - The fundamental gap is at least 2 score points

**Output per setup:**
```
**Long {CCY1} / Short {CCY2}** — Fundamental conviction: {High/Medium}
- {CCY1} case: {1 sentence on why this currency is fundamentally strong}
- {CCY2} case: {1 sentence on why this currency is fundamentally weak}
- Catalyst today: {any data release or event that could confirm or deny the setup}
- Pair to watch: {e.g., GBPJPY, EURNOK, AUDNZD}
```

---

## Step 7 — Format Report

Use the following markdown template:

```markdown
# Daily FX Economist Briefing — {Weekday}, {DD} {Month} {YYYY}

*Generated: {time} UTC | Basket: 19 currencies | Source: Trading Economics, web search*

---

## Session Context

{1–2 sentence framing: what matters today, which session is opening, key theme}

---

## 1. Overnight Economic Releases

{Per-currency summaries from Step 2}

**No releases overnight:** {list of currencies with nothing to report}

---

## 2. Today's Economic Calendar

| Time (UTC) | Currency | Release | Forecast | Prior | Impact |
|------------|----------|---------|----------|-------|--------|
{rows from Step 3}

**Economist's Watch:** {1–2 sentences on the most important release today}

---

## 3. Overnight FX Moves vs USD

| Currency | 24h Change vs USD | Spot Rate |
|----------|-------------------|-----------|
{rows from Step 4, sorted by 24h change desc}

---

## 4. Economist Scorecard

| Currency | Rate Bias | Inflation | Growth | Labour | Overall |
|----------|-----------|-----------|--------|--------|---------|
{full scorecard table — all 19 currencies}

*Changes today: {list updated currencies and what changed}*

---

## 5. Top Trade Setups

{2–3 setups from Step 6}

---

*FX trading carries significant risk. This briefing is for informational purposes only.*
```

---

## Step 8 — Push to GitHub

Push the formatted `.md` file to the GitHub repo.

**Repo:** `joewaiman/FX_Trading`
**Path:** `daily-briefings/YYYY-MM-DD.md`
**Commit message:** `Add daily FX economist briefing {YYYY-MM-DD}`

```bash
gh api repos/joewaiman/FX_Trading/contents/daily-briefings/YYYY-MM-DD.md \
  --method PUT \
  --field message="Add daily FX economist briefing {YYYY-MM-DD}" \
  --field content="$(base64 -i YYYY-MM-DD.md)"
```

---

## Step 9 — Update Notion Database

Add a new row to the **Daily FX Economist Briefing** Notion database.

**Database location:** FX Fundamental Analysis page in Notion workspace
**Parent page ID:** `344f5490-1aec-819e-87e3-e0efc16e651d`
See `references/notion.md` for database ID once created.

**Row properties to set:**
| Property | Type | Example |
|----------|------|---------|
| Date | TITLE | "Mon 19 May 2026" |
| date:Date:start | DATE | "2026-05-19" |
| Strongest | TEXT | "GBP, AUD, NOK" |
| Weakest | TEXT | "JPY, HUF, MXN" |
| Key Release | TEXT | "US CPI beats at 3.1%" |
| Economist Bias | TEXT | "USD hawkish bias extended; JPY under pressure" |
| GitHub Link | URL | URL to the `.md` file on GitHub |
| Status | SELECT | "Published" |

**Page content:** Paste the full formatted markdown report into the opened page body.

---

## Tools to Use

| Task | Tool |
|------|------|
| Fetch overnight releases | `web_search`, `web_fetch` (Trading Economics) |
| Fetch economic calendar | `web_fetch` (`tradingeconomics.com/calendar`) |
| Fetch 24h FX moves | `web_search`, Trading Economics |
| Push to GitHub | `gh` CLI via Bash |
| Update Notion | Notion MCP tools (`notion-create-pages`, `notion-update-page`) |

See `references/scorecard.md` for the scorecard baseline and scoring criteria.
See `references/sources.md` for data source URLs and search templates.
See `references/notion.md` for Notion database IDs.

---

## Scheduling

This skill runs automatically every **weekday (Mon–Fri) at 06:30 UTC** (before London open).

Trigger type: Remote scheduled agent
Schedule: `30 6 * * 1-5` (cron — Mon–Fri at 06:30 UTC)

---

## Economist Persona — Guiding Principles

- Lead with **interpretation**, not just numbers. "CPI beat means the Fed has less room to cut
  in H2 2026" is more useful than "CPI: 3.1% vs 3.0% forecast."
- Distinguish between **trend changes** (important) and **noise** (in-line prints, minor beats).
- Track **policy divergence** — the gap between two central banks' stances is the primary
  driver of FX direction.
- Flag **inflection risks** — currencies where one more data point could flip the bias.
- Be **concise and actionable** — traders read this before the London open.

---

## Important Notes

- Always state the data date for each figure
- If a rate or data point is unavailable, note "N/A — pending"
- Currency 24h change is vs USD only (not cross-rates)
- This briefing is informational only — not investment advice
- Scorecard reflects fundamental bias only — does not incorporate technical levels
