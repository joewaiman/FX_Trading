# Pattern Anatomy Reference

This file contains detailed pip measurement guides and anatomy notes for the
fx-candlestick-patterns skill. Read this when you need granular measurement detail.

---

## Candlestick Anatomy — Key Terms

```
                High
                 ↑
                 │  ← Upper wick (shadow)
              ┌──┴──┐
              │     │  ← Body (Open to Close)
              └──┬──┘
                 │  ← Lower wick (shadow)
                 ↓
                Low
```

| Term | Definition |
|---|---|
| Open | Price at the start of the period |
| Close | Price at the end of the period |
| High | Highest price reached during the period |
| Low | Lowest price reached during the period |
| Body | Range between Open and Close (the coloured rectangle) |
| Upper wick | Range between the top of the body and the High |
| Lower wick | Range between the bottom of the body and the Low |
| Range | Full span from Low to High |

**Bullish candle** = Close > Open (body is green/white)
**Bearish candle** = Close < Open (body is red/black)

---

## Pip Measurement Guide

### What is a pip?

In FX, a **pip** (percentage in point) is the smallest standard price movement:
- Most pairs (EUR/USD, GBP/USD, etc.): 1 pip = 0.0001
- JPY pairs (USD/JPY, EUR/JPY): 1 pip = 0.01

**Pip formula:** `(Price A − Price B) ÷ Pip value = Pips`

Example EUR/USD: (1.1050 − 1.1020) ÷ 0.0001 = **30 pips**
Example USD/JPY: (150.50 − 150.00) ÷ 0.01 = **50 pips**

---

## Pin Bar — Pip Measurements by Location

### Bullish Pin Bar

```
High ────────┐  ← Top of opposite wick
             │
    Close ───┤  ← Top of body
             │
    Open ────┤  ← Bottom of body
             │
    Low ─────┘  ← Tip of rejection wick
```

| Measurement | From → To | Formula |
|---|---|---|
| Body size | Open → Close | \|Open − Close\| ÷ pip value |
| Rejection wick | Low → Open | (Open − Low) ÷ pip value |
| Opposite wick | Close → High | (High − Close) ÷ pip value |
| Full range | Low → High | (High − Low) ÷ pip value |

**Ratio check:** Rejection wick ÷ Body size ≥ 2

---

### Bearish Pin Bar

```
High ────────┐  ← Tip of rejection wick
             │
    Open ────┤  ← Top of body
             │
    Close ───┤  ← Bottom of body
             │
    Low ─────┘  ← Bottom of opposite wick
```

| Measurement | From → To | Formula |
|---|---|---|
| Body size | Open → Close | \|Open − Close\| ÷ pip value |
| Rejection wick | Close → High | (High − Open) ÷ pip value |
| Opposite wick | Low → Open | (Close − Low) ÷ pip value |
| Full range | Low → High | (High − Low) ÷ pip value |

**Ratio check:** Rejection wick ÷ Body size ≥ 2

---

## Worked Example — Bullish Pin Bar (EUR/USD, Daily)

```
Open:   1.08500
Close:  1.08650
High:   1.08700
Low:    1.07800
```

**Step 1 — Body size:**
(1.08650 − 1.08500) ÷ 0.0001 = **15 pips**

**Step 2 — Rejection wick (bullish = Low to Open):**
(1.08500 − 1.07800) ÷ 0.0001 = **70 pips**

**Step 3 — Opposite wick (bullish = Close to High):**
(1.08700 − 1.08650) ÷ 0.0001 = **5 pips**

**Step 4 — Ratio check:**
70 ÷ 15 = **4.67×** ✅ (well above the 2× minimum)

**Step 5 — Opposite wick check:**
5 pips vs 15 pip body = 33% → borderline, but very small in absolute terms ✅

**Verdict:** Strong bullish pin bar. Rejection wick is nearly 5× the body. Opposite
wick is minimal. Would score Grade A if chart space is clear.

---

## Worked Example — Bearish Engulfing (GBP/USD, Daily)

```
Candle 1 (bullish):
  Open: 1.27200  Close: 1.27500  (body = 30 pips)

Candle 2 (bearish engulfing):
  Open: 1.27600  Close: 1.27000
  High: 1.27650  Low:  1.26950  (body = 60 pips)
```

**Body engulfment check:**
- C2 Open (1.27600) > C1 Close (1.27500) ✅
- C2 Close (1.27000) < C1 Open (1.27200) ✅
- C1 body fully inside C2 body ✅

**Body ratio:** 60 ÷ 30 = **2×** ✅

**C2 close quality:**
- Upper wick: (1.27650 − 1.27600) ÷ 0.0001 = 5 pips ✅
- Lower wick: (1.27000 − 1.26950) ÷ 0.0001 = 5 pips ✅

**Verdict:** Valid bearish engulfing. Grade A — closed near lows, clean body engulfment,
minimal wicks on the engulfing candle.

---

## Spinning Top — What to Avoid

A **spinning top** is a candle with a small body AND wicks on both sides of similar size.
It signals **indecision**, not reversal. Do not mistake for a pin bar.

```
     │  ← Upper wick (similar size to lower)
  ┌──┤
  │  │  ← Small body
  └──┤
     │  ← Lower wick (similar size to upper)
```

If your "pin bar" has a significant opposite wick that is more than 30-40% of the body
size, reconsider. We want one-sided rejection — not a battle still in progress.

---

## Chart Space — Visual Guide

**Good — Clear chart space to the left:**
```
                         │ ← Rejection wick protrudes clearly
                         │
Price level ─────────────┤ ← No candles at this level nearby
                         │
                      ┌──┤
                      │  │ Body
                      └──┤
```

**Poor — No chart space (choppy price):**
```
  ┌──┐    ┌─┐  ┌──┤
  │  │┌──┐│ │  │  │ Body  ← Pin bar buried in overlapping candles
  └──┘└──┘└─┘  └──┤
```

Clear space = the rejection wick reaches a level price has not visited recently.
This makes the rejection meaningful — price probed an area and was clearly pushed back.
