---
name: fx-support-resistance
description: >
  Use this skill whenever the user wants to identify, draw, or analyse support and resistance
  levels or zones on an FX chart. Triggers include: drawing channels, identifying S&R zones,
  locating swing highs and lows, analysing diagonal or horizontal support/resistance, spotting
  Head & Shoulders or Inverse Head & Shoulders patterns, assessing where price is likely to
  pause or reverse, or determining channel boundaries on Weekly or Daily timeframes.
  This is Step 2 of the FX Technical Analysis workflow — S&R mapping after channel direction
  has been identified. Also use when the user asks "where is support?", "where is resistance?",
  "is this a H&S pattern?", "how do I draw the channel?", or wants to identify trade zones.
---

# FX Support & Resistance Skill

This skill identifies and maps Support & Resistance zones using a structured **top-down approach**
across the Weekly and Daily timeframes. It follows Step 1 of the FX Technical Analysis skill
(channel direction identification).

> 📖 For background on S&R zone theory, channel drawing rules, and pattern definitions —
> read `references/sr-concepts.md`

---

## Core Principle

> **S&R operates by ZONES, not specific prices.**
> Price does not react at an exact pip level — it reacts within a zone defined by candle bodies
> and wicks. Always think in terms of areas, not lines.

---

## Workflow Overview

```
Weekly Chart  →  Major horizontal S&R zones + channel boundaries (6 months back)
Daily Chart   →  Secondary S&R zones + diagonal S&R + channel zones (6 months back)
               ↓
Step A: Draw the Channel & Channel Zones (body→wick / wick→body rules)
Step B: Map Horizontal S&R Zones (big swings only)
Step C: Map Diagonal S&R Zones
Step D: Check for Head & Shoulders Formations
Step E: Identify the Three Primary Trade Signals
Step F: Produce the Zone Output Summary
```

---

## Step A — Draw the Channel & Channel Zones

**Objective:** Define the channel boundaries using the body→wick and wick→body drawing rules.
Channel zones are wider areas of S&R, not precise lines.

**The one non-negotiable rule:** You may draw through a wick. You must NEVER cross through
a candle body. This applies to every line in every channel.

---

### Bullish Channel

In a bullish channel price makes higher lows. The trade is to buy in the buy zone on
pullbacks and target the resistance line.

```
Step 1 — Draw the primary floor line:
  Using the Parallel Channel tool, draw the base line through the BODY BOTTOMS
  of the swing lows (the rising sequence of higher lows).
  Rule: never cross through a candle body. You may pass through wicks.

Step 2 — Drag outward to create the outer boundary:
  Drag the parallel copy DOWNWARD to touch the lowest WICK tip.
  This is the conservative floor — the outer/lower edge of the buy zone.

  BUY ZONE = the band between the primary body-bottoms line (inner/upper)
             and the dragged wick-lows line (outer/lower)

Step 3 — Drag a copy of the primary line to the resistance target:
  Take the primary line, drag a parallel copy UPWARD to touch the highest WICK
  on the opposite side of the channel.
  This is the take-profit target for long positions.
```

---

### Bearish Channel

In a bearish channel price makes lower highs. The trade is to sell in the sell zone on
rallies and target the support line.

```
Step 1 — Draw the primary ceiling line:
  Using the Parallel Channel tool, draw the base line through the BODY TOPS
  of the swing highs (the declining sequence of lower highs).
  Rule: never cross through a candle body. You may pass through wicks.

Step 2 — Drag outward to create the outer boundary:
  Drag the parallel copy UPWARD to touch the highest WICK tip.
  This is the conservative ceiling — the outer/upper edge of the sell zone.

  SELL ZONE = the band between the primary body-tops line (inner/lower)
              and the dragged wick-highs line (outer/upper)

Step 3 — Drag a copy of the primary line to the support target:
  Take the primary line, drag a parallel copy DOWNWARD to touch the lowest WICK
  on the opposite side of the channel.
  This is the take-profit target for short positions.
```

---

**Nested channels:** Price can form channels within channels. If a smaller channel is visible
inside the larger one, draw and label it separately. Inner channels are often the more
immediate trade signal.

### What the Zones Mean

| Zone | Definition | Signal |
|---|---|---|
| Bullish — buy zone | Between body-bottoms line (inner/upper) and wick-lows line (outer/lower) | Enter LONG on pullback into zone |
| Bullish — resistance target | Parallel dragged to highest wick on opposite side | Take-profit for longs |
| Bearish — sell zone | Between body-tops line (inner/lower) and wick-highs line (outer/upper) | Enter SHORT on rally into zone |
| Bearish — support target | Parallel dragged to lowest wick on opposite side | Take-profit for shorts |
| Mid-channel | Price between the zones | In transit — no signal |

---

## Step B — Map Horizontal S&R Zones

**Objective:** Identify major horizontal zones from the last 6 months of price history.
Focus ONLY on big swings — small swings are not significant and should be ignored.

### What Makes a "Big Swing"

A big swing is one that:
- Started a significant directional move (price moved substantially after leaving this level)
- The zone was clearly respected (price reversed sharply, not gradually)
- Visible and obvious on the Weekly or Daily chart without zooming in

Ignore small consolidations, minor retracements, and brief pauses.

### Horizontal Resistance Zone

```
Upper boundary = HIGHEST WICK in the zone (the maximum rejection point)
Lower boundary = LOWEST BODY in the zone (the last body before the move up)

Price reaching resistance = touches the zone, then swings away downward
The size of the previous swing OFF this zone predicts the likely size of the next swing
```

### Horizontal Support Zone

```
Upper boundary = HIGHEST BODY in the zone (the last body before the move down)
Lower boundary = LOWEST WICK in the zone (the maximum rejection point)

Price reaching support = touches the zone, then moves upward
The zone will be tested — watch how price reacts on the first test
```

### Zone Strength Scoring

Rate each zone 1–3 based on:

| Criteria | Points |
|---|---|
| Zone held price for 2+ touches | +1 |
| Previous swing off zone was large (100+ pips on Daily) | +1 |
| Zone aligns with a round number (1.2000, 150.00 etc.) | +1 |

- Score 3 = Major zone (mark in red/green, highest priority)
- Score 2 = Secondary zone (mark in orange)
- Score 1 = Minor zone (note but deprioritise)

### Look-back Period

- **Weekly chart:** 6 months — mark only 2–4 major zones. More than 4 = too cluttered.
- **Daily chart:** 6 months — mark the 4–6 most significant zones near current price.

---

## Step C — Map Diagonal S&R Zones

**Objective:** Identify diagonal trendline-based S&R zones using the same body/wick rules
as the channel drawing method.

### Diagonal Resistance Zone

```
1. Connect the HIGHEST WICK to the LOWEST BODY
   — do not cross any candle bodies in between
2. Then draw a parallel line: from the HIGHEST BODY to the HIGHEST WICK
3. The diagonal RESISTANCE ZONE = the band between these two lines
```

### Diagonal Support Zone

```
1. Connect the LOWEST WICK to the HIGHEST BODY
   — do not cross any candle bodies in between
2. Then draw a parallel line: from the LOWEST BODY to the LOWEST WICK
3. The diagonal SUPPORT ZONE = the band between these two lines
```

**The zone, not the line:** The crossover area between the two parallel lines is the zone
where price is expected to react. This is identical in principle to the horizontal zones —
always treat as an area, not a precise price.

### TradingView Drawing Tools for Diagonal S&R

- Use `Trend Line` tool for each individual diagonal line
- Draw both the aggressive and conservative line — the zone is the gap between them
- Use a semi-transparent fill or a contrasting colour to mark the zone

---

## Step D — Head & Shoulders Formations

**Objective:** Check if price is forming a trend reversal pattern at key S&R zones.
Head & Shoulders patterns are most significant when they form at major S&R zones identified
in Steps B and C.

> See `references/sr-concepts.md` for full pattern anatomy diagrams.

### Standard Head & Shoulders (Bearish Reversal)

**Context:** Forms after an uptrend. Signals potential reversal to the downside.

```
Left Shoulder  →  Price rises to a peak, then pulls back
Head           →  Price rises to a HIGHER peak (higher than left shoulder), then pulls back
Right Shoulder →  Price rises to a LOWER peak than the head — key signal
Neckline       →  Drawn connecting the two pullback lows (between shoulders and head)
```

**Your rule:** A good H&S should have a **lower low for the second shoulder** — this is a
strong signal that the uptrend is breaking. A breaking low in an uptrend is a good selling area.

**Confirmation signal:** Price breaks and **closes below the neckline**

**Target:** Measure head height to neckline → project that distance downward from breakout point

**Stop loss:** Above the right shoulder high

**Watch for:** False breakouts below the neckline that recover — wait for a confirmed close

### Inverse Head & Shoulders (Bullish Reversal)

**Context:** Forms after a downtrend. Signals potential reversal to the upside.

```
Left Shoulder  →  Price drops to a low, then rises
Head           →  Price drops to a LOWER low (lower than left shoulder), then rises
Right Shoulder →  Price drops to a HIGHER low than the head — key signal (higher low)
Neckline       →  Drawn connecting the two rally highs (between shoulders and head)
```

**Confirmation signal:** Price breaks and **closes above the neckline**

**Target:** Measure head depth to neckline → project that distance upward from breakout point

**Stop loss:** Below the right shoulder low

### Neckline Notes

- Neckline can be horizontal, upward sloping, or downward sloping — all valid
- A **downward sloping neckline** on a standard H&S produces a stronger bearish signal
- Always wait for a **confirmed candle close** beyond the neckline, not just a wick touch
- After breakout, price often **retests the neckline** — this can be the entry point

### H&S Validity Checklist

```
☐ Forms at or near a major S&R zone identified in Step B or C
☐ Clear prior trend exists before the pattern (uptrend for H&S, downtrend for inverse)
☐ Right shoulder is lower than the head (H&S) or higher than the head (inverse)
☐ Neckline is clearly drawable with two obvious touch points
☐ Neckline break is confirmed by a candle close, not just a wick
☐ Pattern is visible on Daily or Weekly — 4H patterns are lower conviction
```

---

## Step E — The Three Primary Trade Signals

**All three signals are equally weighted.** Assess which is present in the current setup.

### Signal 1 — Price Reaching the Channel Boundary

Price has moved from mid-channel to either the support zone or resistance zone boundary.

```
AT CHANNEL RESISTANCE ZONE → Potential short / sell signal
  — Look for bearish rejection candle (long upper wick, close near low)
  — Confirm: RSI overbought, price at horizontal resistance too (confluence)
  — Stronger if H&S right shoulder is forming here

AT CHANNEL SUPPORT ZONE → Potential long / buy signal
  — Look for bullish rejection candle (long lower wick, close near high)
  — Confirm: RSI oversold, price at horizontal support too (confluence)
  — Stronger if Inverse H&S right shoulder is forming here
```

### Signal 2 — Price Bouncing Off an Internal S&R Zone

Price is inside the channel but has reached a horizontal or diagonal S&R zone identified
in Steps B or C.

```
AT INTERNAL RESISTANCE → Pause or reversal zone
  — Assess zone strength score (1–3)
  — Score 3: high probability rejection — treat as primary signal
  — Score 1–2: watch for confirmation before acting

AT INTERNAL SUPPORT → Bounce zone
  — Same strength scoring logic applies
  — Look for test-and-hold behaviour (wick touches zone, body closes above it)
```

### Signal 3 — Price Breaking Out of the Channel

Price closes beyond the channel boundary (either support or resistance zone), not just
a wick through it.

```
BREAKOUT ABOVE RESISTANCE ZONE
  — Wait for confirmed close ABOVE the resistance zone (body close, not wick)
  — Watch for retest of the broken resistance zone (it may flip to support)
  — Enter long on successful retest if price holds above
  — Failed retest = fakeout — do not chase

BREAKOUT BELOW SUPPORT ZONE
  — Wait for confirmed close BELOW the support zone (body close, not wick)
  — Watch for retest of the broken support zone (it may flip to resistance)
  — Enter short on successful retest if price holds below
  — Failed retest = fakeout — do not chase
```

---

## Step F — Zone Output Summary

Produce the following after completing Steps A–E:

```
═══════════════════════════════════════════════════════════
PAIR: [e.g. EUR/USD]  |  Date: [today's date]
S&R ZONE ANALYSIS — Following: Channel = [Bullish/Bearish/Sideways]
═══════════════════════════════════════════════════════════

CHANNEL ZONES (from Step A)
───────────────────────────────────────────────────────────
Channel Resistance Zone:  x.xxxxx – x.xxxxx  [Weekly/Daily]
Channel Support Zone:     x.xxxxx – x.xxxxx  [Weekly/Daily]
Inner Channel (if any):   x.xxxxx – x.xxxxx  [label]

HORIZONTAL S&R ZONES (from Step B — big swings only, 6M lookback)
───────────────────────────────────────────────────────────
[★★★] MAJOR RESISTANCE   x.xxxxx – x.xxxxx  [reason, e.g. "3x tested Weekly high"]
[★★ ] RESISTANCE         x.xxxxx – x.xxxxx  [reason]
>>> CURRENT PRICE: x.xxxxx <<<
[★★ ] SUPPORT            x.xxxxx – x.xxxxx  [reason]
[★★★] MAJOR SUPPORT      x.xxxxx – x.xxxxx  [reason]

DIAGONAL S&R ZONES (from Step C)
───────────────────────────────────────────────────────────
Diagonal Resistance Zone: x.xxxxx – x.xxxxx  [slope: rising/falling]
Diagonal Support Zone:    x.xxxxx – x.xxxxx  [slope: rising/falling]

HEAD & SHOULDERS CHECK (from Step D)
───────────────────────────────────────────────────────────
Pattern detected:  YES / NO / FORMING
Type:              H&S (bearish) / Inverse H&S (bullish) / N/A
Status:            Forming / Neckline not yet broken / Confirmed breakout
Neckline:          x.xxxxx  [horizontal/sloping]
Target (if conf.): x.xxxxx  (+/- [N] pips from neckline break)
Validity score:    [X/6 checklist items met]

ACTIVE TRADE SIGNALS
───────────────────────────────────────────────────────────
Signal 1 (Channel boundary): [Active / Not active] — [brief note]
Signal 2 (Internal S&R):     [Active / Not active] — [zone, strength score]
Signal 3 (Breakout):         [Active / Not active] — [brief note]

CONFLUENCE NOTE
───────────────────────────────────────────────────────────
[Note where multiple zones / signals overlap — these are the highest priority areas]
[e.g. "Channel resistance zone + major horizontal resistance + H&S right shoulder all
at x.xxxxx–x.xxxxx — strong confluence for short setup"]

NEXT STEP
───────────────────────────────────────────────────────────
Proceed to Step 3: RSI & momentum indicator readings
[Refer to fx-technical-analysis skill for next steps]
═══════════════════════════════════════════════════════════
```

---

## TradingView Drawing Checklist

```
☐ Primary channel line drawn through body edges (body bottoms for bullish / body tops for bearish)
☐ Parallel copy dragged outward to wick extremes on same side → zone outer boundary
☐ Parallel copy of primary line dragged to opposite-side wick extremes → take-profit target
☐ Buy zone (bullish) or sell zone (bearish) shaded between the two same-side lines
☐ Inner channels drawn separately if visible
☐ Horizontal resistance zones marked as rectangles (red, semi-transparent)
☐ Horizontal support zones marked as rectangles (green, semi-transparent)
☐ Diagonal S&R lines drawn as Trend Lines (two lines per zone)
☐ Neckline drawn for any H&S pattern (dashed horizontal or diagonal line)
☐ All zones labelled with price range and timeframe origin
```

---

## Key Rules Summary

| Rule | Detail |
|---|---|
| Zones not lines | Always define S&R as a price band, never a single level |
| Body beats wick | Candle bodies define zone boundaries; wicks define extremes |
| Big swings only | Ignore small pullbacks when mapping horizontal S&R |
| 6 months lookback | Both Weekly and Daily — no further back |
| Confluence wins | Where two or more zones overlap = highest priority trade area |
| No fakeouts | Always wait for a candle body close beyond a zone before calling breakout |
| Timeframe weight | Weekly zones override Daily zones when they conflict |

---

## Important Notes

- This skill covers **Step 2: S&R Zone Mapping** of the FX Technical Analysis workflow
- It follows the **fx-technical-analysis skill** (channel direction, Step 1)
- Always complete channel direction first — S&R zones are meaningless without knowing the trend
- This is analysis only — no position sizing or leverage recommendations are provided
- FX trading carries significant risk of loss
