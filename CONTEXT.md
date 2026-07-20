# Session Context — FX Trading

This file is updated at the end of each working session so I can resume with full context.
Tell Claude: **"read CONTEXT.md and pick up where we left off"**

---

## Last Updated
**Date:** 2026-07-09 (W28) — session 5
**Session work:** Ran a full W28 fundamental scan across all 19 currencies (`fundamental-analysis/2026-W28.md`). It invalidated the entire W28 short-SEK shortlist. Two currencies re-rated (NZD and JPY upgraded to Mild Bullish; AUD downgraded to Conflicted). Three new high-conviction pairs identified, all short-EUR — then all three were taken through Step 2 technicals (`analysis/2026-07-09-W28-technical.md`). **Two were killed on the charts. Nothing is executable today.**

---

## 🔴 W28 Shortlist — STOOD DOWN (2026-07-09)

**The three setups from 2026-07-08 are cancelled. Do not enter.**

| Pair | Dir | Was | Status |
|------|-----|-----|--------|
| NOKSEK | LONG | Top pick, conf. 4 | ❌ **Invalid** — both legs failed |
| USDSEK | LONG | conf. 3 | ❌ **Invalid** — short leg failed |
| SEKJPY | SHORT | conf. 3 | ❌ **Invalid** — short leg failed; JPY now bullish |

None were ever triggered, so there is nothing to close.

**Why:** SEK moved from Mild Bearish → **Conflicted (green-leaning, 3🟢 vs 2🔴)**. `CLAUDE.md` forbids entering a trade where either leg is Conflicted.

The prior version of this file justified the short-SEK book with *"Riksbank cutting, PMI weak, export slowdown."* **All three claims were false**, and they also contradicted `fundamental-analysis/2026-W26.md`, which said the opposite. The actual W28 picture:

- **Riksbank is holding at 1.75% with a *raised* hike probability** — no cutting cycle exists. Next decision 20 Aug.
- **PMIs are the strongest in the whole 19-currency basket** — mfg 58.3, services 56.6, both improving.
- **Trade balance flipped from deficit to surplus** (+SEK 2.9B, May/26).
- GDP is +2.0% YoY. CPIF rose 0.8% → 1.3%.

NOK also softened independently (retail sales –2.1% MoM; PMI series still discontinued), so NOKSEK was weakening from both ends.

⚠️ **Lesson:** all three setups were the same short-SEK bet wearing different tickers. The confluence scores read as independent conviction. When the single shared leg re-rated, the whole book died at once. **Check the shared leg before the confluence score.**

---

## ⚠️ Unresolved — The Scoring Rule Contradicts Itself

`CLAUDE.md` defines the bias thresholds in two incompatible places; the skill defines them a third way:

| Source | Mild Bullish | Mild Bearish |
|---|---|---|
| `CLAUDE.md` line 88 | 5–6 🟢 | 5–6 🔴 |
| `CLAUDE.md` line 217 (entry gate) | more 🟢 than 🔴 | more 🔴 than 🟢 |
| `fx-fundamental-analysis` skill, Step 3 | 5–7 🟢 | 5–7 🔴 |

**This week it decides everything.** Under the strict count rule, **no currency reaches 5🔴** — there are no valid short legs and the correct output is *"nothing to trade."* Under the relative rule there are three good pairs.

W28 was scored under the **relative rule (line 217)**, since that is the one written into the entry gate. Currencies whose classification flips between rules are marked ⚖️ in the W28 file: NOK, BRL, CHF, SEK, HUF, CNY.

**Must be settled before the next scan.**

---

## Current Market Backdrop

- **Iran–US war energy shock** driving inflation above target across most economies; supply disruption now pushing the *periphery* into active tightening
- **RBNZ hiked to 2.50% on 8 July** — first rise in three years, unanimous, "further hikes appear likely." ~3.00% expected by year-end
- **BoJ** hiked to 1.00% in June (31-year high); guidance to 1.25% by year-end, neutral ~2%
- **Norges Bank** held at 4.25% with explicit signal to hike again this year; path just above 4.5% at end-2026
- **Riksbank** held at 1.75%, raised hike probability (not cutting)
- **ECB** hiked to 2.40% on 11 June — stagflation risk. July 23 pause expected; ~50% priced for September
- **Fed** on hold 3.50–3.75% under new Chair Kevin Warsh; hawkish dots, but weak jobs report cut July hike odds to ~22%
- **RBA** held at 4.35%; 3 of 4 major AU banks now call the peak
- **SNB** at 0% through end-2026, with stated willingness to **intervene against CHF strength**
- **MAS** steepened S$NEER slope in April — July MPS imminent

---

## W28 Fundamental Scores (2026-07-09)

Full detail in: `fundamental-analysis/2026-W28.md`

| Currency | Bias | Δ vs W26 | Notes |
|----------|------|----------|-------|
| USD | 🟢 Mild Bullish (6🟢) | ↑ | Hawkish Fed dots, GDP 2.7% YoY, retail +0.9% |
| JPY | 🟢 Mild Bullish (6🟢) | ⬆️ **upgraded** | BoJ hiking to neutral, real wages +1.7%, retail +1.9% |
| NZD | 🟢 Mild Bullish (6🟢) | ⬆️ **upgraded** | **RBNZ hiked 8 Jul**, more signalled; mfg PMI 59.7 |
| SGD | 🟢 Mild Bullish (5🟢) | → | MAS steepening, 6% GDP, composite PMI 57.4 |
| INR | 🟢 Mild Bullish (5🟢) | → | 7.8% GDP, both PMIs 54+ — ⚠️ NDF liquidity |
| NOK ⚖️ | 🟢 Mild Bullish (weak, 4🟢) | ↓ | Hawkish + oil surplus, but retail –2.1%; PMI data gap |
| BRL ⚖️ | 🟢 Mild Bullish (weak, 4🟢) | → | SELIC 14.25% carry — ⚠️ EM risk |
| CAD | 🟡 Conflicted | → | Surplus vs 6.6% unemployment, svcs PMI 47.1 |
| GBP | 🟡 Neutral | → | Real wages +1.6%, services contracting |
| CHF ⚖️ | 🟡 Conflicted | ↓ | Svcs PMI 59.8, but **SNB will sell CHF into strength** |
| SEK ⚖️ | 🟡 **Conflicted** | ⬆️ **upgraded** | Trade surplus, best PMIs in basket, hike-lean |
| AUD | 🟡 Conflicted | ⬇️ **downgraded** | **Trade → deficit**, real wages –0.7%, rate peaked |
| MXN | 🟡 Conflicted | → | Banxico cutting, GDP –0.6% QoQ |
| PLN | 🟡 Conflicted | → | Retail rebound vs mfg PMI 46.1 |
| HUF ⚖️ | 🔴 Mild Bearish (weak) | ↑ softened | CPI below band → cuts, but retail + trade improved |
| CNY ⚖️ | 🔴 Mild Bearish | ↓ deepened | **CPI 1.2% → 1.0%**, PBOC easing, retail –0.6% YoY |
| EUR | 🔴 Mild Bearish | ↑ softened | Still stagflating, but HICP 3.2→2.8, retail turned positive |
| ILS ⚠️ | 🔴 Mild Bearish | → | **BoI cut again to 3.50%**, GDP –0.8% QoQ, war overhang |
| DKK | ⚠️ EUR peg | — | ERM II — mirrors EUR |

---

## Candidate Pairs (W28) — Technicals Complete (2026-07-09)

Full detail in: `analysis/2026-07-09-W28-technical.md`

### 🔴 Concentration warning
**EUR is the only unambiguous short leg in the basket.** All three high-conviction pairs are short-EUR — one trade in three costumes. **Pick ONE.** A second position must avoid EUR entirely.

### High conviction (fundamentals) → technical verdict
| # | Pair | Dir | Conv. | Weekly | Daily | 4H | Verdict |
|---|------|-----|-------|--------|-------|-----|---------|
| 1 | EUR/NZD | SHORT | ★★★ | 🟡 Sideways | 🟢 Bullish | 🔴 RSI 30.5 | ❌ **No trade** |
| 2 | EUR/JPY | SHORT | ★★★ | 🟡 Coiling | 🟢 Bullish | 🟢 RSI 62 | ❌ **No trade** |
| 3 | EUR/USD | SHORT | ★★★ | 🔴 Bearish | 🔴 Bearish | 🟢 **Turned up** | ⚠️ **Abandon-leaning** (per 15:15 rerun) |

- **EUR/NZD** — ❌ Daily is a clean bullish channel (rising highs *and* lows, price above two rising SMAs). The RBNZ hike is real but the chart hasn't accepted it. The 4H entry is already gone — price fell ~90 pips to 4H RSI 30.5. Shorting here is the CHFJPY mistake in a new costume. **Re-check if the Daily closes below 2.00082.**
- **EUR/JPY** — ❌ All three timeframes bullish. Price above every SMA on every TF, 4H RSI 62 and rising. Weekly is a bull-flag coil near the highs, not a top. The BoJ story is policy *normalisation*, not inflation (CPI 1.5% vs 2.0% target) — and normalisation is slow. **Watch for a Weekly close below 182.04.**
- **EUR/USD** — ⚠️ **Was the only survivor at 11:00; a 15:15 re-run downgraded it to abandon-leaning.** Weekly + Daily still bearish, but the 4H turned up (lower-high sequence broken, 20 SMA rolled above 50), the zone was tested and produced no valid entry pattern, and the Daily is on its third higher low. See `analysis/2026-07-09-EURUSD-technical-rerun.md` (authoritative). **Watch: a 4H close back below 1.14180 re-opens the short; a Daily close above 1.14730 kills it.**

**⚠️ The fundamental ranking and the technical ranking disagree.** EUR/NZD was the best *story* and the worst *chart*; EUR/USD was the least improved fundamentally and the only one whose price action cooperates. Trade the chart that's ready, not the story that's best.

### EUR/USD — no live setup (authoritative read = the 15:15 rerun)

The 2026-07-09 11:00 write-up framed EUR/USD as "Stage A, wait for the zone, alert 1.1448." **The 15:15 re-run superseded that** (`analysis/2026-07-09-EURUSD-technical-rerun.md`): the zone was tested (high 1.14494), no valid entry pattern formed, and the 4H entry frame turned bullish. Verdict: **no trade, closer to abandon than wait.**

- **Watch level:** a 4H close back **below 1.14180** re-opens the short. A Daily close above **1.14730** kills it outright.
- **Do not set a "1.1448 short" alert** — that was the superseded framing.
- These levels are **12 days stale** (2026-07-09 → today 2026-07-21). W30 fundamentals confirm the EUR-short *thesis* is intact, but **the entry frame must be re-read from scratch** before any action. Do not act on the numbers above.

### 🚨 Gate update — CPI cleared, ECB now imminent

- **US CPI (14 Jul) has passed** — printed 3.5%, cooler than ~3.8% consensus. The old "stand down after 11 July" CPI trap is **resolved and no longer applies.**
- **ECB decision is 23 July — now the binding gate.** As of 2026-07-21 it is **2 days out (inside the 72h window)**, so any short-EUR entry today triggers the 24–72h gate (halve size, widen SL 10 pips). Market has a hold ~95% priced; the risk is a hawkish-hold EUR spike, not a cut. **Cleanest path: wait for the ECB to clear on 23 Jul, then re-read.**

### ✅ The R:R threshold conflict — RESOLVED (2026-07-21): floor is 1.5:1

This was the thread picked back up on 2026-07-21. It was **not a one-file typo** — the repo config had drifted:

- The **live** `fx-technical-analysis` skill (`~/.claude/skills/…`) always said **1.5:1 (prefer 2:1)** — and every actual analysis (AUDCAD Apr, SEKJPY/NOKSEK May–Jun, 02-Jul shortlist, both 09-Jul EUR/USD reads) validated against **1.5:1**.
- But the repo copies — `CLAUDE.md:236`, both `-extracted/SKILL.md`, `workflows/trade-entry.md` — had drifted to **1:2 (2.0:1)**, and today's edit pushed `fx-entry-confirmation` further that way.

**Decision (Joe): 1.5:1 is the real rule.** All repo config synced to **"1.5:1 (prefer 2:1 or better)"** to match the live skill — `CLAUDE.md:236`, `fx-entry-confirmation` SKILL.md (×3), `fx-technical-analysis-extracted` SKILL.md (×2), `workflows/trade-entry.md`. Past trades stand valid as recorded. The EUR/USD setup at **1.97:1 passes** (its abandonment was on 4H structure, not R:R).

⚠️ One inconsistency for the record: the **07-08 shortlist** analysis quoted the 1:2 rule to block two trades — but those were stood down for fundamental reasons anyway (short-SEK invalidated), so the floor change doesn't revive them.

### Medium conviction — none analysed technically
| # | Pair | Dir | Conv. | Note |
|---|------|-----|-------|------|
| 4 | USD/CNH | LONG | ★★ | **Only non-EUR pair of quality.** ⚠️ PBOC-managed. ⬅️ **Open thread** — the candidate for a second, uncorrelated position. Not yet charted. |
| 5 | EUR/SGD | SHORT | ★★ | ⚠️ MAS July MPS imminent — unpriced event |
| 6 | USD/HUF | LONG | ★★ | Non-EUR. Thin. Short leg weakened |

**Do not stack.** Even when EUR/USD triggers, it is the *single* EUR expression. Adding EUR/NZD or EUR/JPY later reconstructs the exact concentration error that killed the W28 short-SEK book.

### Watch, do not trade
- **NZD/AUD long** — cleanest divergence story on the board (RBNZ hiking unanimously vs RBA at peak, AU trade deficit, negative real wages). **Blocked**: AUD is Conflicted, not Bearish. One more bad AU print (svcs PMI <50, or another deficit) makes this the best pair available. **Set an August RBA reminder.**
- **NOK/SEK long** — now invalid, both legs moved. Was W26 #3 and W28 top pick.
- **Any CHF long** — SNB has stated it will intervene against appreciation.
- **ILS shorts** — weakest fundamentals, but ⚠️ no PMI data and war overhang makes it un-modelable.

---

## Macro Event Gate — Next 21 Days

≤24h to event **blocks entry**; 24–72h **halves size, widens SL 10 pips**.

| Date | Days out | Event | Affects |
|---|---|---|---|
| ~mid-Jul | 0–7 | **MAS July MPS** (date TBC) | SGD |
| 15 Jul | 6 | Bank of Canada + MPR | CAD |
| 23 Jul | 14 | **ECB** (pause expected) | EUR, DKK |
| 28–29 Jul | 19–20 | **FOMC** (~22% hike odds) | USD |
| 20 Aug | 42 | Riksbank (hike live) | SEK, NOK |
| Aug TBC | ~30+ | RBA | AUD |

**Nothing inside the 72h window today.** But all three high-conviction pairs carry the **23 July ECB**; two also carry the FOMC. Anything held past 21 July must be re-checked.

---

## Open Trades

None currently open **in reality** — but ⚠️ **Supabase still flags CHFJPY and AUDNZD as `active`.**

Both resolved in May 2026 and were never closed in the DB:

| Pair | Dir | Entry | Outcome | Result |
|------|-----|-------|---------|--------|
| AUDNZD | LONG | 1.21593 (24 May) | ✅ Win — TP2 hit 26 May | +54.2 pips / +1.10R |
| CHFJPY | SHORT | 202.318 (22 May) | ❌ Loss — stopped out | −26.0 pips / −1.00R |

Net: **+0.10R**.

**Action required:** run `python close_may_trades.py` (needs a network that resolves the Supabase host) to reconcile. Until then, any query of open trades — including Step 3 of `workflows/daily-check.md` — returns two phantom positions and wrongly consumes 2 of the 4 open-trade slots.

**CHFJPY post-mortem:** a 26-pip stop on a pair with a ~130-pip daily range was noise-width, not structure-width. Direction was right (price back at 201.3 by 2026-07-09, well below the 202.318 entry) — the stop was too tight to survive the path. See the max-stop-width and structural-stop rules in `CLAUDE.md`.

---

## Current Analysis File Index

| File | Contents |
|------|----------|
| `fundamental-analysis/2026-W28.md` | **Current scorecard** — all 19 currencies, 2026-07-09 |
| `analysis/2026-07-09-W28-technical.md` | **Current technicals** — EUR/NZD, EUR/JPY, EUR/USD. Only EUR/USD survives, Stage A |
| `analysis/2026-07-08-shortlist-technical.md` | W28 NOKSEK/USDSEK/SEKJPY technicals (**setups now stood down**) |
| `log_technical_2026-07-08.py` | Source of the W28 DB rows |
| `fundamental-analysis/2026-W26.md` | Prior scorecard (superseded) |
| `analysis/2026-07-02-*.md` | W27 screener + technicals (superseded) |
| `analysis/2026-06-24-*-technical.md` | W26 EUR/USD, EUR/NOK, NOK/SEK (superseded) |

---

## Next Steps

**Take no position today.** The chart selected EUR/USD; the chart has not yet triggered it.

1. **EUR/USD has no live setup** (the 15:15 rerun abandoned it; see above). If you want the EUR short, **re-read EUR/USD from scratch** after the 23 Jul ECB — watch for a 4H close below 1.14180. Do not use the old 1.1448 alert.
2. **Settle the scoring-rule conflict** in `CLAUDE.md` (line 88 vs line 217 vs skill Step 3). Too large a difference to leave open — it decides whether this week has three trades or zero.
3. **Reconcile Supabase** — `close_may_trades.py` still unrun; two phantom `active` rows wrongly consume 2 of 4 open-trade slots. Do this before logging anything new.
4. **Optional: chart USD/CNH** — the only non-EUR candidate, if you want a second uncorrelated position. Fundamentals done, technicals not.
5. **Set an August RBA reminder** — one more AUD deterioration unlocks NZD/AUD long.
6. **Re-check any open position against the ECB on 23 July.**
7. **Commit the W28 work** — `analysis/2026-07-09-W28-technical.md`, `analysis/2026-07-08-shortlist-technical.md` and `fundamental-analysis/2026-W28.md` are all still untracked.

---

## TradingView Notes (for next session)

- NOKSEK loads as `FOREXCOM:NOKSEK` — use this prefix when searching
- `chart_set_symbol` always returns `chart_ready: false` — use keyboard workaround (click header → Ctrl+A → type symbol)
- When searching for a pair in the symbol dialog and results show "not found in Stocks", check if symbol loaded in chart header — it often loads anyway. Press Escape and verify with screenshot.
- Always exclude `bars[-1]` from OHLCV analysis (currently forming candle)
