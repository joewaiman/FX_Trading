---
name: fx-candlestick-patterns
description: >
  Use this skill whenever the user wants to identify, validate, or analyse perfect pin bars or
  engulfing candles on an FX chart. Triggers include: "is this a pin bar?", "find me a pin bar",
  "check this engulfing candle", "identify reversal candles", "show me the pattern", "validate
  this setup", "is this a valid signal?", or any request to assess candlestick pattern quality
  across Weekly, Daily, or 4H timeframes. This is Step 4 of the FX Strategy workflow — entry
  trigger identification — and sits after fundamental screening (Step 1) and technical analysis
  (Steps 2–3). Always use this skill when the user references price action reversal candles,
  rejection wicks, or engulfing bars, even if they don't use the word "skill".
---

# FX Candlestick Patterns — Pin Bars & Engulfing Candles

This skill identifies and validates **perfect pin bars** and **perfect engulfing candles** as
reversal entry signals within the FX Strategy workflow. Both patterns signal **reversal only**
— never continuation. They are most powerful when they align with the channel direction and
key S&R levels identified in Steps 1–3.

> 📖 For pip measurement reference and pattern anatomy visuals — see `references/anatomy.md`

---

## Core Philosophy

The strength of bulls and bears is measured by **where candles close**, not just where they
spike. Momentum is shown by consecutive candles closing above (bullish) or below (bearish) the
previous candle's range. When that momentum slows — when price can no longer close outside the
previous candle's range — a reversal signal may be forming.

**We are always looking for reversals:**
- Price trending **down** → look for a **bullish** pin bar or engulfing candle
- Price trending **up** → look for a **bearish** pin bar or engulfing candle

**The naked eye rule:** If you can't see the pattern clearly at a glance, it's not worth trading.
Do not calculate your way into a mediocre signal. A perfect pattern is obvious.

---

## Pattern 1 — The Perfect Pin Bar

A pin bar is a single-candle reversal pattern showing decisive **price rejection** in one
direction. It signals that momentum has run out. The body is small; the rejection wick is large;
the opposite wick is tiny or absent.

### Anatomy

```
BULLISH PIN BAR                    BEARISH PIN BAR
(forms in a downtrend)             (forms in an uptrend)

     ┌─┐  ← Close                      │   ← High (tip of rejection wick)
     │ │  ← Body (Open → Close)        │
     │ │                               │
     └─┘  ← Open                      ┌─┐  ← Open
      │                               │ │  ← Body (Open → Close)
      │                               └─┘  ← Close
      │   ← Rejection wick (lower)
      ↓   ← Low (tip of rejection wick)
```

### ✅ Mandatory Criteria (all 4 must be met)

**Criterion 1 — Closes Within the Previous Candle's Range**

The pin bar's **entire candle** (high to low) must close within the previous candle's range
(high to low). If any part of the pin bar closes outside that range, the pin bar is **invalid**.

- Previous candle range = Previous High to Previous Low
- Pin bar high must be ≤ Previous High
- Pin bar low must be ≥ Previous Low
- This applies to both bullish and bearish pin bars

> Key insight: What matters is the *closing price* (body). The candle body closing within the
> prior range confirms that the momentum attempt failed — the market could not sustain a new
> directional push.

**Criterion 2 — Rejection Wick is At Least 2× the Body Size**

Measure in pips:
- **Bullish pin bar** → Rejection wick = Low of candle to Open (bottom of body)
- **Bearish pin bar** → Rejection wick = Close of body (top) to High of candle

Formula: `Rejection Wick (pips) ≥ 2 × Body Size (pips)`

The larger this ratio, the stronger the signal. A 3:1 or 4:1 ratio is excellent.

**Criterion 3 — Opposite Wick Must Be Very Small (or Absent)**

- **Bullish pin bar** → Opposite wick = Close to High of candle
- **Bearish pin bar** → Opposite wick = Low to Open of candle

This must be minimal. A large opposite wick creates a **spinning top** — that is indecision,
not a clear reversal. We want one-sided rejection.

Rule of thumb: Opposite wick should be no more than 25% of the body size. Smaller is better.
No opposite wick at all is a strong sign.

**Criterion 4 — Context: The Prior Move (Direction)**

The pin bar must form at the end of a clear directional move:
- Bullish pin bar → must follow a bearish leg / downtrend
- Bearish pin bar → must follow a bullish leg / uptrend

Do not trade pin bars in choppy, sideways price action.

### ⭐ Optional Criterion 5 — Clear Chart Space (Open Space to the Left)

A strong pin bar will have **clear, unobstructed space to the left** — meaning the rejection
wick protrudes beyond the surrounding price structure. No nearby candles at the same level.

This avoids false signals from choppy, overlapping price action. Open chart space = cleaner,
more decisive rejection. No chart space = likely noise.

### Pin Bar Measurement Table

When validating a pin bar, record the following:

```
═══════════════════════════════════════════════════════
PIN BAR VALIDATION  |  Pair: ______  |  TF: ______  |  Date: ______
═══════════════════════════════════════════════════════
Type:              Bullish / Bearish

OHLC Data:
  Open:    ______    Close:   ______
  High:    ______    Low:     ______

Previous Candle:
  High:    ______    Low:     ______

MEASUREMENTS (in pips):
  Body size:          ______ pips  (|Open − Close|)
  Rejection wick:     ______ pips
    Bullish: Low → Open
    Bearish: Close → High
  Opposite wick:      ______ pips
    Bullish: Close → High
    Bearish: Low → Open
  Wick-to-body ratio: ______× (must be ≥ 2×)

CRITERIA CHECK:
  ☐ C1 — Entire pin bar within previous candle range?   YES / NO
  ☐ C2 — Rejection wick ≥ 2× body size?                YES / NO → ratio: ____×
  ☐ C3 — Opposite wick very small or absent?            YES / NO → pips: ____
  ☐ C4 — Forms at end of clear directional move?        YES / NO
  ☐ C5 — Clear chart space to the left? (optional)      YES / NO

RESULT:  ✅ VALID PIN BAR  /  ❌ INVALID  /  ⚠️ WEAK (trades if context is strong)

Quality Grade:
  A — All 5 criteria met (including C5): trade with conviction
  B — C1–C4 met, no chart space: valid but watch for noise
  C — C1–C4 met but ratio is borderline (2–2.5×): lower confidence
  D — Any mandatory criterion failed: DO NOT TRADE
═══════════════════════════════════════════════════════
```

---

## Pattern 2 — The Perfect Engulfing Candle

An engulfing candle is a **two-candle reversal pattern**. The second candle completely
engulfs the body of the first candle, showing a decisive shift in control from one side to
the other.

### Anatomy

```
BULLISH ENGULFING                  BEARISH ENGULFING
(forms in a downtrend)             (forms in an uptrend)

Candle 1: Small bearish            Candle 1: Small bullish
     ┌─┐  ← Open                        ┌─┐  ← Close (top)
     │ │                                │ │
     └─┘  ← Close (low)                 └─┘  ← Open (bottom)

Candle 2: Large bullish — engulfs  Candle 2: Large bearish — engulfs
  ┌─────┐ ← Close (above C1 Open)    ┌─────┐ ← Open (above C1 Close)
  │     │                            │     │
  └─────┘ ← Open (below C1 Close)    └─────┘ ← Close (below C1 Open)
```

### ✅ Mandatory Criteria (all must be met)

**Criterion 1 — Body Engulfment (Standard Definition)**

The **body** (open-to-close) of the second candle must completely engulf the body of the
first candle. Wicks are not required to be engulfed.

- Bullish engulfing: C2 Open < C1 Close AND C2 Close > C1 Open
- Bearish engulfing: C2 Open > C1 Close AND C2 Close < C1 Open

The larger the second candle relative to the first, the stronger the signal.

**Criterion 2 — Direction Context (Reversal Only)**

- Bullish engulfing → must form after a bearish leg / downtrend
- Bearish engulfing → must form after a bullish leg / uptrend

Do not trade engulfing patterns in a sideways or choppy market. They must appear at a
momentum extreme — the end of a clear move.

**Criterion 3 — Second Candle Close Quality**

The engulfing candle should close near its extreme:
- Bullish: close should be near the top of its range (minimal upper wick)
- Bearish: close should be near the bottom of its range (minimal lower wick)

Large wicks on the engulfing candle weaken the signal — they suggest indecision crept back
in before the close.

**Criterion 4 — The First Candle Must Be Small**

The first candle represents the weakening of the prior trend. If Candle 1 is very large,
the engulfment requires an even larger second candle, which is rare and may be overextended.
A small first candle + large engulfing second candle = clean momentum shift.

### Engulfing Candle Measurement Table

```
═══════════════════════════════════════════════════════
ENGULFING CANDLE VALIDATION  |  Pair: ______  |  TF: ______  |  Date: ______
═══════════════════════════════════════════════════════
Type:              Bullish / Bearish

Candle 1 (prior candle):
  Open:  ______    Close:  ______
  Body:  ______ pips

Candle 2 (engulfing candle):
  Open:  ______    Close:  ______
  High:  ______    Low:    ______
  Body:  ______ pips
  Upper wick: ______ pips
  Lower wick: ______ pips

Body size ratio (C2 body ÷ C1 body): ______×

CRITERIA CHECK:
  ☐ C1 — C2 body fully engulfs C1 body?                YES / NO
  ☐ C2 — Forms after a clear directional move?          YES / NO
  ☐ C3 — C2 closes near its extreme (small wick)?       YES / NO
  ☐ C4 — C1 is relatively small vs C2?                 YES / NO

RESULT:  ✅ VALID ENGULFING  /  ❌ INVALID  /  ⚠️ WEAK

Quality Grade:
  A — All 4 criteria met, body ratio ≥ 2×: trade with conviction
  B — All 4 met, body ratio 1.2–2×: valid but moderate signal
  C — C1 & C2 met, close quality or C1 size is borderline: lower confidence
  D — C1 or C2 fails: DO NOT TRADE
═══════════════════════════════════════════════════════
```

---

## Multi-Timeframe Application

| Timeframe | What to Look For | Weight |
|---|---|---|
| **Weekly** | Major reversal signals at channel boundaries or key S&R | 🔴 Highest — signals lasting weeks to months |
| **Daily** | Primary entry signal confirmation | 🟠 High — core trading timeframe |
| **4H** | Precision entry refinement within daily signal | 🟡 Moderate — use to time entry, not standalone |

**Top-down rule:**
- A Daily pin bar or engulfing candle aligned with the Weekly channel = high conviction trade
- A 4H signal aligned with Daily AND Weekly = maximum conviction
- Never trade a 4H signal that contradicts the Daily or Weekly channel bias

---

## Pattern Comparison: Pin Bar vs Engulfing

| Feature | Pin Bar | Engulfing Candle |
|---|---|---|
| Candles required | 1 | 2 |
| Key measurement | Rejection wick vs body | C2 body engulfs C1 body |
| Directional signal | Long rejection wick = clear one-sided rejection | Large opposing candle = takeover of control |
| Indecision red flag | Spinning top (large opposite wick) | Large wick on C2 candle |
| Chart space | Optional but strengthens signal | Less relevant |
| Reversal only? | Yes | Yes |

Both patterns require:
- A clear prior directional move
- Closing within the prior candle's range (pin bar only, C1)
- Naked-eye visibility — if you have to squint, skip it

---

## Common Invalidity Reasons

| Issue | Pin Bar | Engulfing |
|---|---|---|
| Pin bar body closes outside prior candle range | ❌ Invalid | — |
| Wick-to-body ratio < 2× | ❌ Invalid | — |
| Large opposite wick (spinning top) | ❌ Invalid | — |
| C2 body does not fully cover C1 body | — | ❌ Invalid |
| Pattern forms in sideways/choppy market | ❌ Skip | ❌ Skip |
| Pattern forms against the Weekly channel | ⚠️ Low priority | ⚠️ Low priority |
| Large wick on the C2 engulfing candle | — | ⚠️ Weaker signal |
| Pattern not visible with naked eye | ❌ Skip | ❌ Skip |

---

## Output & Documentation Workflow

After identifying and validating a pattern, produce the following:

### 1. Pattern Summary Block

```
╔══════════════════════════════════════════════════════╗
║  PATTERN SIGNAL SUMMARY                              ║
╠══════════════════════════════════════════════════════╣
║  Pair:        ______                                 ║
║  Pattern:     Pin Bar / Engulfing                    ║
║  Type:        Bullish / Bearish                      ║
║  Timeframe:   Weekly / Daily / 4H                    ║
║  Date:        ______                                 ║
║  Quality:     A / B / C / D                          ║
╠══════════════════════════════════════════════════════╣
║  KEY LEVELS AT SIGNAL                                ║
║  Near S&R:    ______  (type: ______)                 ║
║  Channel:     Bullish / Bearish / Sideways (TF: __)  ║
║  Alignment:   Weekly ___ / Daily ___ / 4H ___        ║
╠══════════════════════════════════════════════════════╣
║  SIGNAL VERDICT                                      ║
║  Trade:       ✅ YES — High conviction               ║
║               ⚠️ POSSIBLE — Wait for confirmation    ║
║               ❌ NO — Pattern invalid or misaligned  ║
║  Entry zone:  ______                                 ║
║  Stop loss:   Above/Below wick tip: ______           ║
╚══════════════════════════════════════════════════════╝
```

### 2. Screenshots

Capture screenshots from TradingView at each relevant timeframe showing:
- The pattern candle(s) clearly visible
- Relevant S&R levels marked
- Channel drawn
- SMAs (20, 50) visible

**Naming convention:** `PAIR_TF_PATTERNTYPE_DATE.png`
Example: `EURUSD_Daily_BullishPinBar_2025-01-15.png`

### 3. Share to Notion

Use the connected **Notion MCP** to log the trade signal:
- Create or update a page in the FX Signals database
- Include: Pair, Pattern type, Timeframe, Quality grade, Signal verdict, Screenshot(s)
- Tag the entry with the relevant date and currency pair

### 4. Share to GitHub

Upload screenshots and the pattern summary to the FX project GitHub repository:
- Store under `/signals/YYYY-MM/`
- Use the naming convention above for all files
- Commit message: `Add [Pair] [Pattern] signal [Date]`

> Use the `gh` CLI or GitHub MCP to push screenshots to the repository.

---

## Integration with FX Workflow

```
Step 1: Fundamental Analysis     (fx-fundamental-analysis skill)
Step 2: Channel Identification   (fx-technical-analysis skill)
Step 3: S&R Levels + Indicators  (fx-technical-analysis skill)
Step 4: Entry Trigger ← YOU ARE HERE (fx-candlestick-patterns skill)
Step 5: Trade Setup & Risk       (to be developed)
```

This skill covers **Step 4** only. Do not enter a trade based on pattern alone — confirm
the Weekly channel bias and Daily S&R levels are aligned before proceeding.

---

## Quick Reference Card

```
PERFECT PIN BAR                    PERFECT ENGULFING
───────────────────────────────    ────────────────────────────────
✅ Whole candle within prev range  ✅ C2 body fully covers C1 body
✅ Wick ≥ 2× body (in pips)        ✅ Forms after clear directional move
✅ Opposite wick tiny or absent    ✅ C2 closes near its extreme
✅ Forms after clear move          ✅ C1 is relatively small
⭐ Clear chart space (optional)
───────────────────────────────    ────────────────────────────────
Bullish: Lower wick is rejection   Bullish: Big green candle eats small red
Bearish: Upper wick is rejection   Bearish: Big red candle eats small green
───────────────────────────────    ────────────────────────────────
If you can't see it — skip it.     If you can't see it — skip it.
```
