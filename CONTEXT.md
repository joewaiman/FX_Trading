# Session Context — FX Trading

This file is updated at the end of each working session so I can resume with full context.
Tell Claude: **"read CONTEXT.md and pick up where we left off"**

---

## Last Updated
**Date:** 2026-07-08 (W28) — session 4
**Session work:** Three high-conviction technical analyses logged to Supabase via `log_technical_2026-07-08.py`. NOK/SEK is the top pick — all three timeframes bullish with fundamentals aligned. No triggers confirmed; all three watching.

⚠️ **This session produced no markdown analysis file.** The only record is the DB rows and the script itself. Reconstruct from `log_technical_2026-07-08.py` or query the `technical` table.

### W28 Shortlist status (2026-07-08)
| Pair | Dir | Entry | Stop | TP1 (R:R) | Conf. | Status |
|------|-----|-------|------|-----------|-------|--------|
| NOKSEK | LONG | 0.9855 | 0.977 | 1.000 (1.7:1) | 4 | ⏳ Top pick — buy dip to 0.985 (20 SMA) or break >1.000 |
| USDSEK | LONG | 9.66 | 9.585 | 9.795 (1.8:1) | 3 | ⏳ Buy dip 9.66 or break >9.80 |
| SEKJPY | SHORT | 16.80 | 16.90 | 16.505 (3.0:1) | 3 | ⏳ Sell bounce into 16.80. Illiquid, wide spreads |

🔴 **Concentration risk — all three setups are the same trade.** Long NOKSEK, long USDSEK and short SEKJPY are each a short-SEK expression. The confluence scores read as independent conviction but the correlation is near-total: a hawkish Riksbank surprise or a SEK short-squeeze hits all three at once. **Size as one position, not three.** If taking more than one, cut size proportionally.

⚠️ SEKJPY trades on an illiquid Capital.com feed with wide spreads, and R:R from spot is poor — it only works on a bounce into 16.80.

_(The W27 CNY/MXN shortlist — CNYJPY, CNYINR, MXNSEK, CNYSEK — is superseded by the above and was never triggered. Prior W26 EUR/USD, EUR/NOK, NOK/SEK setups below are older still.)_

---

## Current Market Backdrop

- **Iran–US war energy shock** driving global inflation above target across most economies
- **ECB** hiked to 2.40% on June 11 — stagflation risk (hiking into contraction)
- **Fed** on hold with hawkish lean — October 2026 hike possible
- **BoJ** hiked to 1.0% (highest since 1995) — JPY becoming less bearish
- **MAS** tightened S$NEER slope (April 2026) — SGD bullish

---

## W26 Fundamental Scores (2026-06-24)

Full detail in: `fundamental-analysis/2026-W26.md`

| Currency | Bias | Notes |
|----------|------|-------|
| SGD | 🟢 Strong Bullish | MAS tightening, inflation controlled, strong trade |
| USD | 🟢 Mild Bullish | Resilient labour, hold with hawkish lean |
| INR | 🟢 Mild Bullish | RBI easing from strength, services PMI solid |
| NOK | 🟢 Mild Bullish | Oil windfall, Norges Bank hawkish, low unemployment |
| BRL | 🟢 Mild Bullish | High rates, surplus, inflation converging |
| EUR | 🔴 Mild Bearish | Stagflation trap — ECB hiked but GDP contracting |
| SEK | 🔴 Mild Bearish | Riksbank cutting, PMI weak, export slowdown |
| HUF | 🔴 Mild Bearish | Inflation elevated but NBH cutting, weak growth |
| CNY | 🔴 Mild Bearish | PBOC easing, export slowdown, deflation risk |
| ILS | 🔴 Mild Bearish | War premium, fiscal pressures, BoI easing |
| GBP | 🟡 Conflicted | Services strong / manufacturing weak, split signals |
| JPY | 🟡 Conflicted | BoJ hiking but still ultra-low vs peers |
| CAD | 🟡 Conflicted | BoC cutting but oil supports |
| NZD | 🟡 Conflicted | RBNZ cutting cycle complete but no new catalyst |
| PLN | 🟡 Conflicted | NBP holding but mixed growth signals |
| MXN | 🟡 Conflicted | Banxico cutting, energy windfall partially offsets |
| AUD | 🟡 Conflicted | RBA cautious, commodity split (iron ore down, LNG up) |
| CHF | 🟡 Conflicted | SNB cutting, safe-haven demand offsetting fundamentals |
| DKK | 🟡 Mirrors EUR | ERM II peg — follows EUR score |

**Top 3 high-conviction pairs from fundamentals:**
1. SHORT EUR/USD ★★★ (EUR Mild Bearish vs USD Mild Bullish)
2. SHORT EUR/NOK ★★★ (EUR Mild Bearish vs NOK Mild Bullish)
3. LONG NOK/SEK ★★★ (NOK Mild Bullish vs SEK Mild Bearish)

---

## Active Technical Analysis (W26)

### EUR/USD — `analysis/2026-06-24-EURUSD-technical.md`

| Timeframe | Channel | SMAs | RSI |
|-----------|---------|------|-----|
| Weekly | 🔴 Bearish breakdown | Both well above price | 38.18 (bearish) |
| Daily | 🔴 Bearish | Both above price | ~27 ⚠️ oversold |
| 4H | 🔴 Bearish | SMA20: 1.14202 / SMA50: 1.15047 — both above price | **17.95 ⚠️ DEEPLY oversold** |

**Current price:** ~1.1342
**What happened:** Price pulled back into entry zone (1.1450–1.1500) today. A marginal bearish breakdown occurred (Bar 9: open 1.14549, close 1.14310, zero upper wick). Price has since fallen ~110 pips to 1.1342. 4H RSI hit 17.95 — extreme oversold. Entry opportunity passed without a clean Grade A/B trigger.

**Status:** ⏳ WAITING — DO NOT SHORT HERE. RSI 17.95 on 4H means bounce is highly likely before any further continuation.

**Watch for (Scenario A — shallow bounce):** Recovery to **1.1380–1.1430** + bearish 4H pin bar/engulfing
- Entry: ~1.1410 | Stop: 1.1470 | TP1: 1.1280 | R:R ~2:1 ✅

**Watch for (Scenario B — full retest):** Recovery back to **1.1450–1.1500** + bearish 4H trigger
- Entry: 1.1450–1.1500 | Stop: 1.1570 | TP1: 1.1280 | TP2: 1.1150

**Invalidation:** Daily close above 1.1560 — broken support reclaimed, thesis weakens

**⚠️ Macro check required before any entry:** Verify no USD or EUR high-impact events (PCE, Fed speakers, ECB) within 72h

---

### EUR/NOK — `analysis/2026-06-24-EURNOK-technical.md`

| Timeframe | Channel | SMAs | RSI |
|-----------|---------|------|-----|
| Weekly | 🟡 Transitional | SMA20: 11.03 (below) / SMA50: 11.45 (above) | ~49.71 (neutral) |
| Daily | 🟢 Bullish | Both well below price | ~68 approaching overbought |
| 4H | 🟢 Bullish | SMA20: 11.121 / SMA50: 11.081 — both below price | 65.94 (bullish) |

**Current price:** ~11.160
**What happened:** Price pulled back intraday to 11.063 (tested 4H SMA50 at 11.08), then recovered cleanly to 11.160. Classic bullish behaviour — buyers defended the SMA50. Uptrend firmly intact.

**Status:** ❌ NO TRADE — Daily and 4H channels both bullish, opposing the short thesis. ~280 pips from entry zone. No change from last session.

**Watch for:** Price approaches **11.40–11.50** (weekly SMA50 resistance) + bearish 4H candle
- Entry: 11.45–11.50 | Stop: 11.58 | TP1: 11.15 | TP2: 10.90
- Daily RSI breaking above 70 would confirm exhaustion approaching

**Key support to watch:** 4H SMA50 (~11.08) — a daily close below this signals trend weakening

---

### NOK/SEK — `analysis/2026-06-24-NOKSEK-technical.md`

*(Not reviewed this session — status carried forward from session 1)*

| Timeframe | Channel | SMAs | RSI |
|-----------|---------|------|-----|
| Weekly | 🟢 Correcting | Well below price (0.93 area) | 62.52 (bullish) |
| Daily | 🔴 Bearish correction | ~0.998 / ~0.996 — both above price | ~47.99 (neutral-bearish) |
| 4H | 🟢 Recovering | ~0.991 / ~0.989 — both below price | 63.62 (bullish) |

**Current price:** ~0.9941
**Status:** ⏳ WAITING — R:R blocking. Distance to TP1 (1.000) only ~60 pips from current; risk ~90 pips. 1.5:1 minimum not met.
**Watch for (option A):** Pullback to **0.985–0.990** with bullish 4H pin bar → entry 0.988, stop 0.980
**Watch for (option B):** Daily close above **0.99622** (daily SMA50) with RSI > 50 → confirms daily reversal

---

## Open Trades

None currently open.

---

## Current Analysis File Index

| File | Contents |
|------|----------|
| `log_technical_2026-07-08.py` | **W28 shortlist source of truth** — NOKSEK / USDSEK / SEKJPY rows |
| `analysis/2026-07-02-pair-screener.md` | W27 full 19-currency screener (superseded) |
| `analysis/2026-07-02-shortlist-technical.md` | W27 5-pair technicals (superseded) |
| `fundamental-analysis/2026-W26.md` | Last full scorecard for all 19 currencies |
| `analysis/2026-06-24-*-technical.md` | W26 EUR/USD, EUR/NOK, NOK/SEK (superseded) |

---

## Next Steps

1. **Refresh prices before acting on anything.** The W28 levels were read on 2026-07-08 and go stale fast — re-check spot, SMAs and RSI against live data.
2. **Decide the SEK exposure first, then the expression.** All three W28 setups are short-SEK. Pick one (NOKSEK has the best confluence and cleanest liquidity) rather than stacking correlated risk.
3. **Run a W28 fundamental scan.** The last full scorecard is W26 (2026-06-24) — two weeks old. The short-SEK thesis rests on a dovish Riksbank; confirm that still holds before sizing.
4. **Backfill the missing 07-08 analysis file.** Write `analysis/2026-07-08-shortlist-technical.md` from the script + DB rows so the reasoning survives outside Supabase.
5. **Macro-check** for Riksbank, Norges Bank, Fed and BoJ events within 72h of any entry.

---

## TradingView Notes (for next session)

- NOKSEK loads as `FOREXCOM:NOKSEK` — use this prefix when searching
- `chart_set_symbol` always returns `chart_ready: false` — use keyboard workaround (click header → Ctrl+A → type symbol)
- When searching for a pair in the symbol dialog and results show "not found in Stocks", check if symbol loaded in chart header — it often loads anyway. Press Escape and verify with screenshot.
- Always exclude `bars[-1]` from OHLCV analysis (currently forming candle)
