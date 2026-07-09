# Weekly Scan — Fundamental Screening & Pair Selection

Run this every week (Sunday evening or Monday morning before London open).
Output: a ranked shortlist of 1–3 pairs to watch for the week.

---

## Step 1 — Run Fundamental Analysis

**Skill:** `fx-fundamental-analysis`

Scores all 19 currencies across 10 indicators. Collect all data first, then score — do not score mid-collection.

What to look for when the output comes back:
- Top 3 bullish currencies (score 5+)
- Top 3 bearish currencies (score 5+ bearish)
- Any currency where the rate bias has changed since last week (hiking → hold, hold → cut)
- Flag stale data — any indicator >45 days old

Save output to: `fundamental-analysis/YYYY-WXX.md`

---

## Step 2 — Identify High-Conviction Pairs

From the scorecard:
- **Strong Bullish vs Strong Bearish** = highest conviction, go directly to Step 4
- **Mild Bullish vs Mild Bearish** = lower conviction, run pair screener first (Step 3)
- **Conflicted scores** = skip — no edge

Correlation check: if two pairs both require being long the same currency (e.g. SEKJPY long + EURSEK short both = long SEK), flag this. Size down or choose only one.

---

## Step 3 — Pair Screener (if needed)

**Skill:** `fx-pair-screener`

Run when no clear high-conviction pair emerges from fundamentals, or when you want to validate the fundamental pick technically before committing analysis time.

The screener checks:
- Weekly + Daily trend alignment for all 18 non-USD currencies against USD
- Cross pair chart confirmation

Output: ranked shortlist of 3–5 pairs with conviction rating (★★★ / ★★ / ★).

---

## Step 4 — Select Pairs for the Week

Pick 1–3 pairs to take to full technical analysis. Prioritise:
1. Highest conviction score differential (fundamental)
2. ★★★ or ★★ from screener
3. Pairs where the technical setup is likely to be at or near an entry zone (not already extended)

Log selected pairs in the weekly scorecard file.

---

## Next Step

For each selected pair → run the **trade-entry** workflow.
