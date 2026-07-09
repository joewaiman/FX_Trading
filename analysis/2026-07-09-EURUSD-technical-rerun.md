# EUR/USD Technical Re-run — 2026-07-09 (W28)

**Time of read:** ~15:15 UTC | **Feed:** OANDA | **Analyst:** Claude Code
**Supersedes the EUR/USD section of:** `analysis/2026-07-09-W28-technical.md` (read ~11:00 UTC, ICE feed)

---

## Verdict Up Front

**Still Stage A. No valid trigger fired — and the setup is now weaker than it was this morning.**

Two things changed since the 14:04 write-up:

1. **Price reached the entry zone and was rejected.** The 05:00 UTC 4H bar spiked to **1.14494** — inside
   the 1.14480–1.14530 zone — and closed back at 1.14267. A limit order at the specified entry of
   **1.14500 would not have filled**, by 0.6 pips.
2. **The 4H structure has quietly turned against the short.** The falling swing-high sequence broke
   (1.14481 on 08 Jul → 1.14494 today), swing lows are rising, and the 4H 20 SMA is now *above* the 50 SMA.

The Weekly and Daily bearish thesis is intact and unchanged. The *entry timeframe* no longer supports it.

---

## Data Integrity Notes

- `chart_set_symbol` returned `chart_ready: false` as always (Bug 1). Used the `/` → type → Enter
  workaround and confirmed `OANDA:EURUSD` in the chart header before reading data.
- **Feed differs from this morning's report** (OANDA vs ICE). Cross-check is close — Daily 20 SMA
  1.14532 vs 1.14524, Weekly RSI 42.02 vs 42.09 — so structure is not feed-dependent. Levels below are
  OANDA; expect ~1 pip drift against your broker.
- RSI legend on the chart read 54.82; **that is a crosshair artifact** (Bug 2). All SMA and RSI figures
  below are computed from raw OHLCV with Wilder smoothing.
- **The forming 4H bar (13:00–17:00 UTC) is excluded from every reading.** Its high so far is 1.14461.

---

## EUR/USD — SHORT ⏳ Stage A (deteriorating)

```
═══════════════════════════════════════════════════
PAIR: EUR/USD (OANDA)  |  Date: 2026-07-09 15:15 UTC
═══════════════════════════════════════════════════

CHANNEL ANALYSIS
─────────────────────────────────────────────────
Weekly:  🔴 Bearish  — unchanged
         Price below both SMAs, both falling.

Daily:   🔴 Bearish  — unchanged
         Swing highs falling: 1.16857 → 1.16220 → 1.14730.
         Price below both SMAs, both falling. 20 SMA < 50 SMA.
         ⚠️ Swing lows now RISING: 1.13246 → 1.13618 → 1.13912.
            Third consecutive higher low. Base-building.

4H:      🟡→🟢 Turning bullish  ← THIS IS THE CHANGE
         Swing highs: 1.14622 → 1.14481 → 1.14494 (LH sequence BROKEN)
         Swing lows:  1.13912 → 1.14142 → 1.14212 (rising)
         20 SMA (1.14221) now ABOVE 50 SMA (1.14180); 50 SMA sloping UP.
         Price above both.

OVERALL BIAS: BEARISH on W+D, but the 4H entry frame no longer confirms.

SMA STATUS
─────────────────────────────────────────────────
Weekly  20 SMA: 1.16112  ↓    50 SMA: 1.16574  ↓   price BELOW both
Daily   20 SMA: 1.14532  ↓    50 SMA: 1.15723  ↓   price BELOW both
4H      20 SMA: 1.14221  ↓    50 SMA: 1.14180  ↑   price ABOVE both

KEY LEVELS
─────────────────────────────────────────────────
[Resistance 3]  1.15723   Daily 50 SMA — thesis dead above here
[Resistance 2]  1.14730   Daily swing high (02 Jul) — structural invalidation
[Resistance 1]  1.14532   Daily 20 SMA (falling)   ← ENTRY ZONE
[Resistance 1]  1.14494   4H swing high (today, 05:00 UTC) ← ENTRY ZONE
>>> CURRENT PRICE: 1.14309 <<<
[Support 1]     1.13912   4H swing low (08 Jul)
[Support 2]     1.13618   Daily swing low (01 Jul)
[Support 3]     1.13246   Major Daily swing low (24 Jun)

RSI STATUS
─────────────────────────────────────────────────
Weekly RSI: 42.02   Bearish zone
Daily  RSI: 40.80   Bearish zone  ✅ ideal 35–50 for a short
4H     RSI: 52.02   Neutral       ✅ reset, not exhausted

RSI vs Bias: ✅ Aligned on W + D.
Divergence:  None. But Daily price is making higher lows while RSI sits at 40 —
             momentum is not confirming new lows. Watch it.

ENTRY TRIGGER
─────────────────────────────────────────────────
Entry Zone:    1.14490 – 1.14535  (4H swing high + Daily 20 SMA confluence)
Zone reached:  ✅ YES — high of 1.14494 at 05:00 UTC today
Pattern:       ❌ NONE VALID

  The 05:00 UTC rejection bar (O 1.14268 / H 1.14494 / L 1.14256 / C 1.14267):
    • rejection wick 22.6 pips, body 0.1 pips → gravestone doji
    • C1 rejection wick ≥ 2× body ......... ✅ PASS
    • C2 opposite wick ≤ 25% of body ...... ❌ FAIL (1.1 pips vs 0.025 pips)
    • C3 within prior candle's range ...... ❌ FAIL (1.14494 > prior high 1.14304)

  C2 fails only because the near-zero body makes the test degenerate — this is a
  real rejection, not a non-event. C3 is a genuine miss: it is an outside-range
  spike, not a contained pin bar. Under CLAUDE.md's criteria this is NOT a
  confirmed pattern, and the pattern is mandatory.

Confluence:    3.5 / 6
  1. Price at mapped S&R (≤20 pips) ....... ✅  (17 pips from zone)
  2. RSI aligned with bias ................ ✅
  3. Candlestick pattern present .......... ❌  ← mandatory, missing
  4. Daily + 4H channels aligned .......... ❌  ← 4H now opposes
  5. No conflicting divergence ............ ⚠️  Daily higher lows
  6. No high-impact event within 24h ...... ✅  US CPI is 5 days out

STATUS: ⏳ STAGE A — no valid trigger. Setup quality falling.

TRADE SETUP (unchanged on paper; do NOT execute)
─────────────────────────────────────────────────
Direction:   SHORT
Entry:       1.14500  — never filled (today's high 1.14494)
Stop Loss:   1.14800  → 30 pips
TP1:         1.13910  → 59 pips → R:R 1.97:1
TP2:         1.13250  → 125 pips → R:R 4.17:1

R:R CHECK:    ✅ 1.97:1 clears the 1.5:1 minimum
SETUP STATUS: ⏳ Awaiting a valid trigger that may no longer come
═══════════════════════════════════════════════════
```

---

## Macro Event Gate

| Date | Days out | Event | Affects |
|---|---|---|---|
| **14 Jul** | **5** | **US CPI (June)** — 08:30 ET | **USD** |
| 23 Jul | 14 | ECB decision (pause expected) | EUR |
| 28–29 Jul | 19–20 | FOMC | USD |

✅ Nothing inside 72h. Entry is **not** blocked today.

⚠️ The 11 July deadline from this morning's report still stands: a trigger on or after **11 Jul** falls
inside the 24–72h window before CPI, which halves size and widens the stop to 1.1490 — dropping TP1 to
**1.48:1**, below the 1.5:1 minimum. In that case, skip and wait for CPI to clear.

**You now have roughly 36 hours of clean window.** After that the setup is gated regardless of what
price does.

---

## Recommendation

**No trade. And this is now closer to "abandon" than to "wait."**

1. The zone was tested and held, which is what you wanted — but it produced no valid entry pattern, and
   the specified entry never filled.
2. The 4H has broken its lower-high sequence and rolled its 20 SMA above the 50. The frame you were going
   to enter on is no longer bearish. Continuing to wait for a short trigger on a 4H that is turning up is
   how you get the CHFJPY outcome.
3. The Daily higher-low sequence (three now: 1.13246 → 1.13618 → 1.13912) is the tell. The Weekly and
   Daily are still bearish by structure, but the momentum underneath them is not confirming.
4. Per `CLAUDE.md`: *"Don't re-run entry confirmation repeatedly on the same pair. If Stage A or B is
   returned, give the watch level and wait."* This is the second read today. **Do not run a third.**

**Watch level:** a 4H close back **below 1.14180** (the rising 50 SMA) re-opens the short. A Daily close
above **1.14730** kills it outright.

**If nothing has re-broken lower by 11 Jul, stand down until after US CPI.**

---

*Analysis only. No position sizing or leverage recommendations. FX trading carries significant risk of loss.*
*Source: TradingView MCP, OANDA feed, retrieved 2026-07-09 ~15:15 UTC. Indicators computed from raw bars
with Wilder smoothing; forming bar excluded.*
