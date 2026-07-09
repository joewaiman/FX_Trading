# Daily Check — Pre-Session Routine

Run this each trading day before the London open (07:00 UTC).
Takes 5–10 minutes. Keeps you current without re-running a full analysis.

---

## Step 1 — Read the Daily Economist Briefing

The briefing auto-runs at 06:30 UTC (Mon–Fri). Check it in:
- Notion: Daily FX Economist Briefing database
- GitHub: `daily-briefings/YYYY-MM-DD.md`

What to look for:
- Any overnight releases that changed a currency's score (especially rate decisions, CPI, GDP)
- Today's economic calendar — note any high-impact releases that could move your open pairs
- The briefing's 2–3 top setups — do any overlap with your current watchlist?

If a release has materially changed the fundamental bias for a currency you're trading → review whether your trade is still valid before the session opens.

---

## Step 2 — Check Open Trades

For each open trade in `analysis/`:
- Where is price relative to TP1, TP2, and stop?
- Has any key level been broken since you last checked?
- Is RSI approaching an extreme that could signal a reversal before TP?

If price is within 20 pips of TP1 → be ready to close 50% manually if the market is moving fast.
If price is within 20 pips of your stop → do not widen it. Assess whether to close early.

---

## Step 3 — Check Waiting Setups

For each pair on your watchlist (not yet entered):
- Run `fx-entry-confirmation` quickly — has price reached the entry zone?
- If Stage B or C → act. If Stage A → note the current distance and move on.

---

## Step 4 — Note High-Impact Events for Today

Check the economic calendar (in the daily briefing or via web search):
- Any central bank decisions today?
- Any CPI, GDP, or NFP releases?

If a high-impact release is due during the session and you have an open trade in that currency → consider whether to hold through the release or close to avoid gap risk. Do not enter a new trade in the hours immediately before a major release.

---

## Quick Reference — Currency Event Risk

| Event | Currencies most affected |
|-------|-------------------------|
| FOMC / Fed decision | USD, and indirectly all pairs |
| ECB decision | EUR |
| BoJ decision | JPY |
| RBA / RBNZ decision | AUD, NZD |
| BoE decision | GBP |
| Riksbank decision | SEK |
| Norges Bank decision | NOK |
| US CPI / NFP | USD (major vol spike) |
| China PMI | AUD, NZD, CNY |

Avoid entering new positions within 2 hours either side of any event in the above table that affects your pair.
