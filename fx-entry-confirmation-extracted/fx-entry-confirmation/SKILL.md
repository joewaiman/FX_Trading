---
name: fx-entry-confirmation
description: >
  Use this skill whenever the user wants to confirm whether to enter a trade after a TradingView
  alert fires or when price approaches a mapped zone. Triggers include: "is price at the zone?",
  "has the trigger formed?", "should I enter?", "confirm my entry", "check the entry", "is there
  a pin bar at the level?", "did the alert fire — is it valid?", "is the pattern there?", or any
  request to assess whether a candlestick entry signal is present at a mapped S&R level.
  This is Step 4 of the FX Strategy workflow — it runs AFTER fx-technical-analysis has produced
  a bias, key levels, and RSI readings. It reads live price and candles from TradingView, checks
  zone proximity, validates the candlestick trigger (pin bar, engulfing, inside bar), scores
  confluence, and outputs either a waiting status, a zone-watch alert, or a full trade setup
  (entry/SL/TP/R:R). Always use this skill when the user has a TA output in hand and wants to
  know whether conditions are right to act.
---

# FX Entry Confirmation

This skill determines whether it is time to act on a trade setup. It sits between the
**fx-technical-analysis** output (bias + key levels + RSI already known) and actual execution.

It does three things:
1. **Checks whether price has reached the entry zone** identified in the TA output
2. **Validates a candlestick trigger** at that zone (pin bar, engulfing, inside bar)
3. **Produces either a wait status, a zone alert, or a full trade setup**

> Pattern validation logic is based on the same criteria as `fx-candlestick-patterns`.
> This skill wraps that logic and adds zone proximity checking and trade setup construction.

---

## Inputs Required from the User

Before reading TradingView, confirm you have the following from the TA skill output:

| Input | Source |
|---|---|
| Currency pair | TA output |
| Overall bias (Bullish / Bearish) | TA output |
| Key levels (support and resistance prices) | TA output |
| RSI reading + zone (Daily and 4H) | TA output |
| Channel alignment (Weekly / Daily / 4H) | TA output |
| Divergence status (none / bullish / bearish) | TA output |

If any of these are missing, ask the user to paste the TA skill output before proceeding.

---

## Step 0a — Position Limit Check (blocking gate)

Ask the user how many trades are currently open before proceeding.

If the answer is **4 or more**: output the block below and stop. Do not proceed to the macro check or chart analysis.

```
═══════════════════════════════════════════════════
ENTRY CONFIRMATION  |  [PAIR]  |  [Date]
═══════════════════════════════════════════════════
STATUS: 🚫 BLOCKED — Maximum open trades reached (4)

You already have [X] trades open. No new entries until one closes.

Current open trades to monitor instead:
[List any pairs the user has mentioned as open]
═══════════════════════════════════════════════════
```

---

## Step 0b — Macro Calendar Check (blocking gate)

**This runs before any chart data is read. It can block the entire entry.**

Search the economic calendar for **both currencies** in the pair being analysed.
Use Trading Economics (`https://tradingeconomics.com/calendar`) or the daily briefing scorecard.

### Events that trigger this gate

- Central bank rate decisions (ECB, Fed, BoE, RBA, RBNZ, BoC, BoJ, SNB, Riksbank, MAS)
- CPI / inflation releases
- Non-farm payrolls or equivalent employment reports
- GDP flash estimates
- Any event flagged as high-impact (🔴) in the daily briefing

### Decision rules

| Time to event | Action |
|---|---|
| ≤ 24h | **BLOCK** — output Stage 0 (see below). Do not proceed. |
| 24–72h | **WARN** — flag the event. Continue to Step 1 but carry the warning through to the trade setup: halve position size, widen SL by 10 pips. |
| > 72h | **CLEAR** — proceed to Step 1 normally. |

Apply the gate to **either** currency in the pair. If EUR/SGD is being assessed, check EUR events AND SGD/MAS events.

### Stage 0 output — Entry Blocked

```
═══════════════════════════════════════════════════
ENTRY CONFIRMATION  |  [PAIR]  |  [Date]
═══════════════════════════════════════════════════
STATUS: 🚫 BLOCKED — High-impact macro event within 24h

Event:     [e.g. ECB Rate Decision]
Currency:  [e.g. EUR]
Time:      [e.g. 13:15 UTC, 5 Jun 2026 — 18h from now]

No entry until after this event and the initial reaction has cleared.
Re-run entry confirmation after [event time + 4 hours].
═══════════════════════════════════════════════════
```

### Stage 0 warning — Reduced sizing

If event is 24–72h away, prepend this block to whichever Stage (A/B/C) applies:

```
⚠️ MACRO WARNING: [Event name] for [Currency] in [X]h ([date/time UTC])
   Position size: halve normal size
   Stop loss: widen by 10 pips beyond calculated level
   Re-evaluate full size after event clears.
```

---

## Step 1 — Read Live Data from TradingView

### 1a. Confirm the symbol is correct

Before reading data, always verify the chart symbol matches the pair being analysed:
- Call `chart_get_state` and check the symbol field
- If it doesn't match, switch via keyboard: `ui_keyboard("/")` → `ui_type_text("EURUSD")` → `ui_keyboard("Enter")`
- Then take a `capture_screenshot` to confirm the chart has updated visually

> **Known issue:** `chart_set_symbol` may update the internal model but fail to re-render visually
> (`chart_ready: false`). Always use the keyboard workaround if `chart_ready` is false.

### 1b. Get the current price

```
quote_get(symbol)
```

Read: `last` (current price), `bid`, `ask`.

### 1c. Get recent 4H candles

```
data_get_ohlcv(symbol, timeframe="240", count=10, summary=false)
```

This returns individual OHLCV bars. You need the last 2 **completed** candles (not the currently
forming candle). The most recent complete candle is `bars[-2]`; the one before it is `bars[-3]`.

> Always request at least 10 bars. The last bar (`bars[-1]`) is the currently forming candle —
> exclude it from pattern analysis.

---

## Step 2 — Zone Proximity Check

Compare `current_price` from Step 1 against the key levels from the TA output.

Find the **nearest entry zone** given the bias:
- If **Bullish bias**: the entry zone is the nearest **support** level below or near current price
- If **Bearish bias**: the entry zone is the nearest **resistance** level above or near current price

Calculate the distance in pips:
- For JPY pairs: 1 pip = 0.01 (multiply price difference by 100)
- For all other pairs: 1 pip = 0.0001 (multiply price difference by 10000)

**Decision gate:**

| Distance to zone | Action |
|---|---|
| > 20 pips away | → Output Stage A (Waiting). Stop here. |
| ≤ 20 pips | → Proceed to Step 3 (candlestick check) |

The 20-pip threshold is a practical filter. If price is still 30–50 pips from the level, there
is no entry to evaluate yet — tell the user what to watch for and when to re-run the skill.

---

## Step 3 — Candlestick Pattern Check

Check the last 2 completed 4H candles for a valid trigger pattern. Use the bars from Step 1c:
- `candle_1` = `bars[-3]` (the prior candle)
- `candle_2` = `bars[-2]` (the most recent completed candle)

Apply all three pattern checks. A pattern is valid if it meets its mandatory criteria AND
aligns with the bias from the TA output.

### Pin Bar Check (single candle — check `candle_2`)

For a **bullish** pin bar (use when bias is Bullish):
- Rejection wick = `candle_2.open − candle_2.low`
- Body size = `|candle_2.close − candle_2.open|`
- Opposite wick = `candle_2.high − candle_2.close`

For a **bearish** pin bar (use when bias is Bearish):
- Rejection wick = `candle_2.high − candle_2.close`
- Body size = `|candle_2.close − candle_2.open|`
- Opposite wick = `candle_2.open − candle_2.low`

**Valid pin bar:** All 4 criteria must pass:
1. Entire candle (high to low) within prior candle's range (`candle_1.low` to `candle_1.high`)
2. Rejection wick ≥ 2× body size
3. Opposite wick ≤ 25% of body size (very small or absent)
4. Bias-aligned direction (bullish pin in a bearish leg, bearish pin in a bullish leg)

### Engulfing Check (two candles — `candle_1` → `candle_2`)

For a **bullish** engulfing (bias is Bullish):
- `candle_1` is bearish (close < open)
- `candle_2` is bullish (close > open)
- `candle_2.open < candle_1.close` AND `candle_2.close > candle_1.open`

For a **bearish** engulfing (bias is Bearish):
- `candle_1` is bullish (close > open)
- `candle_2` is bearish (close < open)
- `candle_2.open > candle_1.close` AND `candle_2.close < candle_1.open`

Additional quality checks:
- `candle_2` closes near its extreme (small wick on the signal side)
- `candle_1` is relatively small vs `candle_2`

### Inside Bar Check (two candles — `candle_1` → `candle_2`)

- `candle_2.high < candle_1.high` AND `candle_2.low > candle_1.low`
- Signal: consolidation after a move — trade the breakout in the direction of the bias
- Entry: break above `candle_2.high` (long) or below `candle_2.low` (short) + 2–5 pip buffer

### Pattern Result

If no pattern is found → Output **Stage B** (at zone, awaiting trigger).
If a valid pattern is found → Proceed to Step 4.

---

## Step 4 — Confluence Scoring

Score out of 6. Derive from the TA output the user provided + current chart data + Step 0b macro check:

| Factor | Source | Pass condition |
|---|---|---|
| Price at mapped S&R level | Step 2 | ≤ 20 pips from level |
| RSI aligned with bias | TA output | RSI in bias-appropriate zone |
| Candlestick pattern present | Step 3 | Valid pin bar, engulfing, or inside bar |
| Daily + 4H channels aligned | TA output | Both timeframes show same direction |
| No divergence (or divergence supports entry) | TA output | No conflicting divergence |
| No high-impact event ≤ 24h for either currency | Step 0b | Calendar clear OR event > 24h away |

**Score thresholds:**
- 6/6 → High conviction — proceed confidently
- 4–5/6 → Standard setup — proceed with normal sizing
- < 4/6 → Skip — wait for better alignment

---

## Step 5 — Construct Trade Setup (Stage C only)

Only proceed here if: price is at the zone (Step 2) + pattern confirmed (Step 3) + confluence ≥ 3/5 (Step 4).

### Entry Price
- Pin bar or engulfing: open of the **next** 4H candle after the trigger candle closes
- Inside bar: break of `candle_2.high` (long) or `candle_2.low` (short) + 2–5 pip buffer

### Stop Loss
Place at the **nearest structural level that invalidates the thesis** — not just beyond the trigger candle or the immediate S&R zone.

| Setup | Stop Loss Placement |
|---|---|
| Long at support | Below the structural swing low / support zone bottom that, if broken, means the bullish thesis is wrong + 5–10 pip buffer |
| Short at resistance | Above the structural swing high / resistance zone top that, if broken, means the bearish thesis is wrong + 5–10 pip buffer |

The trigger candle's wick is the minimum SL distance. The structural level overrides it if further away — and it usually is.

**Validity check:** If the structural invalidation level is more than 50 pips away on a 4H setup or more than 80 pips on a Daily setup, the zone is too loose — flag this and recommend the user reassess or skip. Do not silently set an oversized stop.

### Take Profit Targets
Use the key levels from the TA output:
- **TP1:** First key S&R level beyond entry direction (close 50% here)
- **TP2:** Second key S&R level or channel boundary (close remaining 50%)

### R:R Calculation
```
Risk (pips) = |Entry − Stop Loss|
Reward TP1  = |TP1 − Entry|
R:R TP1     = Reward ÷ Risk

Minimum acceptable: 1.5:1 (prefer 2:1 or better)
```

If TP1 does not offer at least 1.5:1, flag the setup as **insufficient reward** — do not recommend entry.

---

## Output Formats

### Stage A — Waiting (price not yet at zone)

```
═══════════════════════════════════════════════════
ENTRY CONFIRMATION  |  [PAIR]  |  [Date]
═══════════════════════════════════════════════════
STATUS: ⏳ WAITING — Not at zone

Current Price:  x.xxxxx
Entry Zone:     x.xxxxx  ([level type, e.g. "Daily support / 50 SMA"])
Distance:       [X] pips away

Bias:           BULLISH / BEARISH
Watch for:      Price to reach [level]. Re-run when within 20 pips.
Pattern to look for: [Bullish pin bar / Bearish engulfing] on 4H close at [level]
═══════════════════════════════════════════════════
```

### Stage B — At Zone, No Pattern Yet

```
═══════════════════════════════════════════════════
ENTRY CONFIRMATION  |  [PAIR]  |  [Date]
═══════════════════════════════════════════════════
STATUS: 👀 AT ZONE — Awaiting trigger candle

Current Price:  x.xxxxx
Zone:           x.xxxxx  ([level type]) ✅ REACHED

No confirming candlestick pattern on 4H yet.

Last completed candle:
  Open: x.xxxxx  High: x.xxxxx  Low: x.xxxxx  Close: x.xxxxx
  Assessment: [e.g. "Body too large — not a pin bar. No engulfment of prior candle."]

Wait for: [Bullish pin bar / Bearish engulfing / Inside bar breakout] on next 4H close.
RSI:       [value] — [aligned / neutral / conflicting] with [Bullish / Bearish] bias
═══════════════════════════════════════════════════
```

### Stage C — Trigger Confirmed + Full Trade Setup

```
═══════════════════════════════════════════════════
ENTRY CONFIRMATION  |  [PAIR]  |  [Date]
═══════════════════════════════════════════════════
STATUS: ✅ TRIGGER CONFIRMED

Current Price:  x.xxxxx
Zone:           x.xxxxx  ([level type]) ✅
Pattern:        [Pin bar / Bullish engulfing / Inside bar] on 4H ✅
Pattern grade:  A / B / C  (see below)
Confluence:     [X]/5

CONFLUENCE DETAIL
─────────────────────────────────────────────────
Price at S&R level:          ✅ / ❌
RSI aligned with bias:       ✅ / ❌  ([RSI value], [zone])
Candlestick pattern:         ✅ / ❌
Channels aligned (D+4H):     ✅ / ❌
No conflicting divergence:   ✅ / ❌
Macro calendar clear:        ✅ / ⚠️ [event name, Xh away]

TRADE SETUP
─────────────────────────────────────────────────
Direction:   LONG / SHORT
Entry:       x.xxxxx  (open of next 4H candle)
Stop Loss:   x.xxxxx  ([X] pips — beyond [level] + buffer)
TP1:         x.xxxxx  ([X] pips → [level type])  R:R [X.X]:1  ← close 50% here
TP2:         x.xxxxx  ([X] pips → [level type])  R:R [X.X]:1  ← close 50% here

R:R CHECK:   ✅ Acceptable (≥ 1.5:1) / ❌ Skip — insufficient reward

PATTERN DETAIL
─────────────────────────────────────────────────
[Pin bar: wick X pips, body X pips, ratio X.X× — Grade A/B/C]
[Engulfing: C2 body X pips engulfs C1 body X pips, ratio X.X×]
[Inside bar: range X pips, entry trigger at x.xxxxx]
═══════════════════════════════════════════════════
```

**Pattern grade reference (embedded in Stage C):**
- Grade A — All criteria met, strong ratios: trade with conviction
- Grade B — All criteria met, borderline ratios: valid but watch
- Grade C — Mandatory criteria met, quality is marginal: lower confidence, tighter sizing

---

## Known TradingView Issues

### `chart_set_symbol` — visual update fails silently
After calling `chart_set_symbol`, check `chart_ready` in the response. If `false`, switch via
keyboard: `ui_keyboard("/")` → `ui_type_text("EURUSD")` → `ui_keyboard("Enter")`. Then confirm
with `capture_screenshot` before reading any data.

### RSI blocked on Basic plan (2-indicator limit)
If `chart_manage_indicator` for RSI fails, calculate RSI(14) manually from OHLCV using Wilder's
smoothing — but note that RSI is already available from the TA output passed in by the user.
Only re-calculate if you need to verify or update it for the current candle.

### Currently forming candle
`data_get_ohlcv` always includes the candle currently forming as the last bar (`bars[-1]`).
Never use this candle for pattern validation — it has not closed yet and its shape will change.
Always use `bars[-2]` as the most recently completed candle.

---

## FX Workflow Position

```
Step 1: Fundamental Analysis      (fx-fundamental-analysis)
Step 2: Channel + S&R + RSI       (fx-technical-analysis)
Step 3: S&R Zone Mapping          (fx-support-resistance)
Step 4: Entry Confirmation ← HERE (fx-entry-confirmation)
Step 5: Trade execution           (user's own broker)
```

This skill is the final gate before execution. If Stage C is not reached, do not enter.
