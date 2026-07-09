# AUD/CAD — Candlestick Pattern Scan — 2026-05-04

Step 4 of FX Strategy workflow. Follows: fundamental analysis (HIGH conviction LONG AUD/CAD, 2026-04-30).
Skill: fx-candlestick-patterns

---

## Context Summary

**Pair:** AUD/CAD  
**Fundamental bias:** LONG (HIGH conviction — AUD 7/8, CAD 3.5/9, widest divergence in basket)  
**Current price:** ~0.9780  
**Key catalyst ahead:** RBA rate decision May 5 — 3rd consecutive hike widely expected

---

## Weekly Scan

**Channel bias:** BULLISH — strong 8-week rally from ~0.948 to 0.987  
**Recent weekly bars:**

| Bar | O | H | L | C | Note |
|-----|---|---|---|---|------|
| W-7 (≈Apr 6) | 0.9697 | 0.98687 | 0.96953 | 0.98145 | Big bullish |
| W-8 (≈Apr 13) | 0.9754 | 0.98118 | 0.97482 | 0.97714 | Tiny body, upper wick |
| W-9 (≈Apr 20) | 0.97512 | 0.98342 | 0.97228 | 0.97889 | Small bullish |
| W-10 (current) | 0.98056 | 0.98104 | 0.97604 | 0.97801 | Incomplete |

**Pattern check:**
- W-8 has a 17.4-pip body with a 40.4-pip upper wick (ratio 2.3×) — resembles a shooting star, but the body is BULLISH (close > open), making it invalid as a bearish pin bar. Opposite wick (5.8 pips) fails C3 vs the tiny body.
- W-9: No discernible pattern. Small body, wicks both sides.

**Result: ❌ No valid weekly pattern**

---

## Daily Scan

**Recent key bars:**

| Bar | Date | O | H | L | C | Note |
|-----|------|---|---|---|---|------|
| D-11 | Apr 28 | 0.97877 | 0.98329 | 0.97725 | 0.98265 | Bullish |
| D-12 | Apr 29 | 0.98206 | 0.98342 | 0.97228 | 0.97376 | **Big bearish** |
| D-13 | Apr 30 | 0.97366 | 0.98004 | 0.97295 | 0.97814 | Bullish recovery |
| D-14 | May 1 | 0.97769 | 0.98062 | 0.97548 | 0.97889 | Small bullish |
| D-15 | May 4 | 0.98056 | 0.98104 | 0.97604 | 0.97801 | Bearish (today) |

**Pattern checks:**

**D-12 as bearish pin bar?**
- Body = 83 pips (O:0.98206 → C:0.97376, bearish)
- Upper wick = 13.6 pips, Lower wick = 14.8 pips
- Not a pin bar — body is too large, wicks too small. This is a momentum candle.

**D-11 + D-12 as bearish engulfing?**
- C1 (D-11): bullish body O:0.97877 → C:0.98265 (38.8 pips)
- C2 (D-12): bearish body O:0.98206 → C:0.97376 (83 pips)
- C2 Open (0.98206) > C1 Close (0.98265)? → **NO** — fails by 5.9 pips
- ❌ Not a valid bearish engulfing (body engulfment not met on upper side)

**D-12 + D-13 as bullish engulfing?**
- C1 (D-12): bearish body O:0.98206 → C:0.97376 (83 pips)
- C2 (D-13): bullish body O:0.97366 → C:0.97814 (44.8 pips)
- C2 Close (0.97814) > C1 Open (0.98206)? → **NO** — C2 doesn't close above C1 open
- ❌ Not a valid bullish engulfing

**D-15 (today) as bullish pin bar developing?**
- O:0.98056, H:0.98104, L:0.97604, C:0.97801 (current)
- Body = 25.5 pips (bearish so far), Lower wick = 19.7 pips
- No pin bar formation — bar is still bearish and not close to a valid pattern

**Result: ❌ No valid daily pattern**

---

## 4H Scan

**Recent 4H bars around today's lows:**

| Bar | O | H | L | C | Note |
|-----|---|---|---|---|------|
| 4H-17 | 0.97960 | 0.98038 | 0.97890 | 0.97952 | Small bearish |
| 4H-18 | 0.97952 | 0.97986 | 0.97790 | 0.97858 | Small bearish |
| 4H-19 | 0.97858 | 0.97928 | 0.97604 | 0.97874 | **Doji with lower wick** |
| 4H-20 | 0.97866 | 0.97918 | 0.97747 | 0.97794 | Current |

**4H-19 as bullish pin bar?**

```
═══════════════════════════════════════════════════════
PIN BAR VALIDATION  |  Pair: AUD/CAD  |  TF: 4H  |  Date: 2026-05-04
═══════════════════════════════════════════════════════
Type:              Bullish (attempted)

OHLC Data:
  Open:  0.97858    Close:  0.97874
  High:  0.97928    Low:    0.97604

Previous Candle (4H-18):
  High:  0.97986    Low:    0.97790

MEASUREMENTS (in pips):
  Body size:          1.6 pips  (|0.97858 − 0.97874|)
  Rejection wick:     25.4 pips (Low 0.97604 → Open 0.97858)
  Opposite wick:       5.4 pips (Close 0.97874 → High 0.97928)
  Wick-to-body ratio: 15.9×  (≥ 2× ✅)

CRITERIA CHECK:
  ☑ C1 — Entire candle within previous candle range?   YES ✅
           Pin H (0.97928) ≤ Prev H (0.97986) ✅
           Pin L (0.97604) ≥ Prev L (0.97790)? → NO ❌ (0.97604 < 0.97790)
  ☒ C2 — Rejection wick ≥ 2× body?                    YES ✅ (ratio 15.9×)
  ☒ C3 — Opposite wick very small or absent?           NO ❌ (5.4 pips vs 1.6 pip body = 3.4× body, far exceeds 25% rule)
  ☑ C4 — Forms at end of clear directional move?       YES ✅ (after 3-bar bearish sequence today)
  — C5 — Clear chart space (optional)?                 N/A — not assessed without visual

RESULT:  ❌ INVALID — FAILS C1 (low breaches prior range) AND C3 (doji body, both wicks too large relative to body)

Note: The 1.6-pip body makes this effectively a gravestone doji, not a readable pin bar.
Naked eye rule: if you can't clearly see a pin bar body with a decisive close — skip it.
═══════════════════════════════════════════════════════
```

**Result: ❌ No valid 4H pattern**

---

## Signal Summary

```
╔══════════════════════════════════════════════════════╗
║  PATTERN SIGNAL SUMMARY                              ║
╠══════════════════════════════════════════════════════╣
║  Pair:        AUD/CAD                                ║
║  Pattern:     None confirmed                         ║
║  Type:        —                                      ║
║  Timeframe:   Weekly / Daily / 4H all checked        ║
║  Date:        2026-05-04                             ║
║  Quality:     D (no valid pattern found)             ║
╠══════════════════════════════════════════════════════╣
║  KEY LEVELS AT SIGNAL                                ║
║  Support zone:   0.9720 – 0.9760  (Apr 29 lows)      ║
║  Resistance:     0.9800 – 0.9830  (prior range top)  ║
║  Channel:        Bullish (Weekly, confirmed)          ║
║  Alignment:      Weekly: Bullish / Daily: Pullback    ║
╠══════════════════════════════════════════════════════╣
║  SIGNAL VERDICT                                      ║
║  Trade:       ❌ NO — No valid entry trigger yet     ║
║  Entry zone:  Not established                        ║
║  Stop loss:   Not applicable                         ║
╚══════════════════════════════════════════════════════╝
```

---

## What Happened and What to Watch

**Why no signal:** The Apr 29 sell-off created a sharp bearish day (83-pip body, small wicks) that doesn't satisfy pin bar anatomy. The recovery candles (Apr 30 – May 1) don't close above the big bearish day's open (0.98206), so no bullish engulfing is confirmed. Today's 4H intraday test of 0.97604 looked promising but resolved as a doji — not a clean rejection candle.

**RBA catalyst (May 5):** The RBA is widely expected to hike for the 3rd consecutive meeting tomorrow. A hike + hawkish guidance could produce a sharp AUD spike. **Watch for a valid pin bar or engulfing pattern forming on the Daily chart on May 5** after the announcement — that would be the ideal Step 4 entry trigger aligned with all prior steps.

**Key watch levels:**
- Bullish pin bar / engulfing at **0.9720 – 0.9760** support zone = high-conviction long entry
- Bullish daily close above **0.9830** with clean pin bar = breakout entry
- If RBA hikes and AUD/CAD gaps up past **0.9850**: wait for a retest pattern, don't chase

---

*Screenshots saved:*
- `AUDCAD_Weekly_CandleScan_2026-05-04.png`
- `AUDCAD_Daily_CandleScan_2026-05-04.png`
- `AUDCAD_4H_CandleScan_2026-05-04.png`
