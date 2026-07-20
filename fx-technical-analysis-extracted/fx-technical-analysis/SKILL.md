---
name: fx-technical-analysis
description: >
  Use this skill whenever the user wants to perform technical analysis on a currency pair or FX chart.
  Triggers include: identifying the trend or channel direction, analysing price action, locating support
  and resistance levels, reading candlestick patterns, interpreting SMA or RSI readings, assessing
  whether to enter a trade, or reviewing chart structure on any timeframe (Weekly, Daily, 4H).
  This is Step 2 of the FX Strategy workflow — technical analysis after fundamental screening.
  Also use when the user asks "where is price now?", "is this a good entry?", "what's the chart
  doing?", or wants to assess momentum, trend strength, or key price levels for any FX pair.
  Use proactively whenever a currency pair is mentioned alongside any chart or trade question.
---

# FX Technical Analysis Skill

Analyses FX price action using a structured **top-down, multi-timeframe** approach. Follows on from
the FX Fundamental Analysis skill. Technical analysis confirms *when* and *where* to act on a
fundamentally-biased pair.

> 📖 Entry trigger candlestick patterns → `references/concepts.md`

---

## Workflow Overview

```
Phase 0: Collect live data via TradingView MCP
         ↓
Weekly → Daily → 4H
         ↓
Phase 1: Identify the Channel (trend direction)
Phase 2: Map key Support & Resistance levels
Phase 3: RSI & momentum readings
Phase 4: Entry trigger — candlestick pattern confirmation
Phase 5: Trade setup — entry, stop loss, take profit, R:R
```

---

## Phase 0 — TradingView MCP Data Collection

Run this before any analysis. It replaces manual chart description with live data.

> **If TradingView MCP is unavailable:** ask the user to describe the chart (pair, timeframe, SMA positions, RSI level, recent swing highs/lows). Proceed from Step 1 using the described data, noting that values are user-reported rather than live.

### Prerequisites (one-time manual setup)

SMA periods **cannot be set programmatically** via MCP — `chart_manage_indicator` ignores the
`inputs` parameter for period/length. The user must set these once manually in TradingView:

1. Add two Simple Moving Averages to the chart
2. Set the first to **Length 20**, the second to **Length 50**
3. Add **RSI (14)** — this can be added automatically (see 0.2 below)

If the SMAs are already on the chart with correct periods, skip to 0.1.

### 0.1 — Confirm chart state and record original timeframe

```
chart_get_state
```

- Confirms the symbol and **current timeframe — record this to restore later**
- Returns entity IDs and names for all active indicators
- Identify the two SMAs by inspecting the returned indicator names. Match them by period:
  - Find the entity whose name or inputs show `length: 20` → this is **SMA20**
  - Find the entity whose name or inputs show `length: 50` → this is **SMA50**
  - Do not rely on position order — layout changes or saved templates can reorder indicators
  - **Verify SMA periods:** confirm the returned inputs show `length: 20` and `length: 50`. If the periods are wrong, ask the user to correct them in TradingView before proceeding.

### 0.2 — Ensure RSI is on the chart

If RSI is not in the `chart_get_state` output, add it:
```
chart_manage_indicator  action="add"  indicator="Relative Strength Index"
```

> Note: The `inputs` parameter works for RSI period but **not** for SMA period/length — SMA periods
> must be set manually in TradingView. Requires a TradingView plan with enough indicators per chart
> (Premium or above). If the add fails, ask the user to add RSI manually.

### 0.3 — Collect data across all three timeframes

For each timeframe (W, 1D, 4H), run in sequence:

```
chart_set_timeframe  timeframe="W"
data_get_ohlcv       summary=true          ← swing structure (highs/lows)
data_get_study_values                       ← SMA(20), SMA(50) values on weekly bars

chart_set_timeframe  timeframe="1D"
data_get_ohlcv       summary=true
data_get_study_values                       ← SMA(20), SMA(50), RSI(14) on daily bars

chart_set_timeframe  timeframe="240"
data_get_ohlcv       summary=true
data_get_study_values                       ← SMA(20), SMA(50), RSI(14) on 4H bars

quote_get                                   ← current bid/ask/last price
```

> The same SMA indicator displays values for the active timeframe's bars — SMA(20) on Weekly = 20-week
> MA; on Daily = 20-day MA. Values will differ significantly across timeframes; this is expected.

> Weekly RSI is not collected — the Weekly timeframe is used for swing structure and SMA position only.

> After collection, restore the original timeframe recorded in 0.1:
> `chart_set_timeframe  timeframe="[original]"`

### 0.4 — Optional: Screenshot

```
capture_screenshot  region="chart"
```

Useful for documenting the analysis or when sharing the output.

---

## Phase 1 — Identify the Channel

**Objective:** Determine trend direction on each timeframe using OHLCV swing structure + SMA position.

### Channel Types

| Channel | Price Structure | SMA Condition |
|---|---|---|
| 🟢 Bullish | Higher Highs (HH) + Higher Lows (HL) | 20 > 50, both rising, price above both |
| 🔴 Bearish | Lower Highs (LH) + Lower Lows (LL) | 20 < 50, both falling, price below both |
| 🟡 Sideways | No clear HH/HL or LH/LL | Price weaving through SMAs repeatedly |

### SMA Confirmation Rules

| SMA Condition | Signal |
|---|---|
| 20 > 50, both rising, price above both | 🟢 Strong bullish |
| 20 > 50, price pulling back to 50 SMA | 🟢 Bullish — watch for bounce at 50 |
| 20 < 50, both falling, price below both | 🔴 Strong bearish |
| 20 < 50, price pulling back to 50 SMA | 🔴 Bearish — watch for rejection at 50 |
| Price crossing SMAs frequently | 🟡 Range / sideways |
| 20 crossing 50 (recent crossover) | ⚠️ Potential trend change — treat with caution |

### Process

1. **Weekly** — identify macro bias from 12–18 months of swing structure. Note last clear HH/HL or LH/LL.
2. **Daily** — confirm primary trend. Check 20 & 50 SMA slope and price position.
3. **4H** — locate micro-channel for entry. A 4H trend opposing the Weekly/Daily = retracement only.

**Alignment rules:**
- **All three aligned** → high conviction. Enter on trigger at 4H S&R.
- **Weekly + Daily aligned, 4H opposing** → 4H is a retracement within the larger trend. This is the preferred entry scenario — wait for price to reach a 4H S&R level that coincides with the direction of the Weekly/Daily trend, then look for a trigger candle.
- **Weekly aligned, Daily + 4H opposing** → too early. Wait for Daily to confirm before acting.
- **All three conflicting or sideways** → no trade. Revisit after next major session close.

---

## Phase 2 — Map Key Support & Resistance Levels

> **Specialist skill available:** For detailed S&R zone drawing, channel boundary identification, or
> Head & Shoulders pattern analysis, invoke the `fx-support-resistance` skill. The summary below
> covers the essentials for a standard trade setup; use the specialist skill when deeper zone mapping
> is needed.

**Objective:** Identify price levels where reactions are most likely, ordered by strength.

### S&R Hierarchy (strongest → weakest)

1. **Weekly swing highs/lows** — major institutional levels; expect strong reactions
2. **Daily swing highs/lows** — mark the most recent 5–10; re-tested levels carry more weight
3. **Round numbers** — 1.1000, 150.00, 0.6500 etc. within 50–100 pips of current price
4. **Dynamic S&R** — 20 SMA (first level in trend) and 50 SMA (deeper level)
5. **Channel boundaries** — upper/lower lines of your identified channel
6. **Previous Day / Previous Week High & Low** — institutional reference points; breakouts attract momentum

### Key Level Output

List the nearest 4–6 levels to current price:

```
[Resistance 2]  x.xxxxx  Weekly swing high
[Resistance 1]  x.xxxxx  Daily swing high / round number
>>> CURRENT PRICE: x.xxxxx <<<
[Support 1]     x.xxxxx  50 SMA / daily low
[Support 2]     x.xxxxx  Weekly swing low / channel floor
```

---

## Phase 3 — RSI & Momentum Readings

**Objective:** Confirm whether momentum supports the channel bias, and flag exhaustion or divergence.

Use `data_get_study_values` values from Phase 0 for Daily and 4H RSI(14).

### RSI Interpretation

| RSI Level | Signal |
|---|---|
| > 70 | Overbought — pullback or consolidation likely |
| 50–70 | Bullish momentum zone |
| 50 | Neutral |
| 30–50 | Bearish momentum zone |
| < 30 | Oversold — bounce likely |

### Momentum Alignment Check

- **Bullish bias + RSI 50–70 and rising** → momentum confirms trend. Favour longs.
- **Bullish bias + RSI > 70** → trend intact but stretched. Wait for pullback before entry.
- **Bearish bias + RSI 30–50 and falling** → momentum confirms trend. Favour shorts.
- **Bearish bias + RSI < 30** → trend intact but stretched. Wait for bounce before entry.
- **RSI diverging from price** → weakening momentum. See divergence patterns in `references/concepts.md`.

### RSI Output

```
RSI STATUS
─────────────────────────────────────────────────
Daily  RSI(14): [value]  → [Overbought / Bullish zone / Neutral / Bearish zone / Oversold]
4H     RSI(14): [value]  → [same]
Momentum alignment: Confirms bias / Stretched — wait for pullback / Divergence detected
```

---

## Phase 4 — Entry Trigger

> **Specialist skill available:** The table below is a quick-reference only. For pattern validation
> (wick ratios, body position, multi-candle confirmation), invoke the `fx-candlestick-patterns` skill.
> This skill provides the gate logic — *where* and *when* to look for a trigger. The specialist skill
> validates *whether* the pattern qualifies.

**Objective:** Wait for a specific candlestick signal at a key S&R level before committing to a trade.

Do not enter on bias alone — a trigger candle is required. It provides a low-risk entry point and
defines the stop loss level precisely.

### Entry Trigger Rules

- The trigger candle must form **at or very near a key S&R level** from Step 2
- The trigger candle's direction must **align with the channel bias** from Step 1
- RSI must **not be stretched** in the opposite direction (i.e. don't go long when RSI > 75)
- Look for triggers on the **4H chart** (Daily for higher-conviction, wider-stop setups)

### Valid Trigger Patterns

| Pattern | Long Signal | Short Signal |
|---|---|---|
| **Pin Bar** | Long lower wick at support, small body near top | Long upper wick at resistance, small body near bottom |
| **Engulfing** | Bullish candle fully engulfs prior bearish candle body | Bearish candle fully engulfs prior bullish candle body |
| **Inside Bar Breakout** | Small candle inside prior bar; pending buy stop above mother bar high | Small candle inside prior bar; pending sell stop below mother bar low |

> For visual examples and pattern details → `references/concepts.md`

**Volume confirmation:** Phase 0 uses `summary=true` which returns aggregated data only — it does not include per-bar volume. For the volume check, call `data_get_ohlcv` on the trigger timeframe **without** `summary=true`. Check that the trigger candle's volume is visibly higher than the preceding 3–5 bars. Higher volume strengthens the signal; flat or falling volume reduces confidence.

### If No Trigger Yet

When no valid trigger has formed, do not wait passively. Instead:

1. Note the exact S&R level to watch (from Step 2)
2. Set an alert on TradingView:
   ```
   alert_create  symbol=[PAIR]  price=[S&R level]  condition="crossing"
                 message="[PAIR] approaching [level] — check for trigger candle"
   ```
3. Record the pair in the watchlist with status "Awaiting trigger at [level]"
4. Revisit when the alert fires

### No-Entry Conditions

- Channel is Sideways on Weekly AND Daily (no directional bias)
- Trigger candle forms away from any key S&R level
- RSI is deeply oversold (< 25) on a short setup, or deeply overbought (> 75) on a long setup
- Daily and Weekly channels are in direct conflict with no clear resolution
- A major scheduled release is due within 4 hours (NFP, CPI, central bank rate decision) — wait for the release before entering; the candle that forms immediately after the release is not a valid trigger (too much noise)

---

## Phase 5 — Trade Setup

**Objective:** Define the exact entry, stop loss, and take profit levels. Confirm the risk/reward is acceptable.

### Entry Price

- **Aggressive entry:** at close of the trigger candle
- **Conservative entry:** limit order at the 50% retracement of the trigger candle's body (slightly better price)

### Stop Loss

Place stop loss at the **nearest structural level that invalidates the trade thesis** — not just beyond the trigger candle's wick.

| Trade Direction | Stop Loss Placement |
|---|---|
| Long | Below the nearest swing low / support zone that, if broken, means the bullish thesis is wrong + 5–10 pip buffer |
| Short | Above the nearest swing high / resistance zone that, if broken, means the bearish thesis is wrong + 5–10 pip buffer |

**Structural invalidation means:** if price closes beyond this level, the reason for the trade no longer exists. Examples:
- Short thesis based on price being below Weekly SMA50 → SL above the Weekly SMA50
- Short from a resistance zone → SL above the top of that zone, not just above the trigger candle wick
- Long from a support zone → SL below the bottom of that zone

The trigger candle's wick sets the **minimum** SL distance. If the structural invalidation level is further away, use that instead — which it usually will be.

Never place stop loss at a round number (too obvious a target for stop hunts).

### Take Profit

Set take profit at the **next significant S&R level** in the direction of the trade:

- For longs: next resistance level (from Step 2 key levels)
- For shorts: next support level (from Step 2 key levels)
- Avoid placing TP beyond a major Weekly S&R level without strong conviction

### Risk / Reward

```
Stop distance  = |Entry price − Stop loss|
Target distance = |Take profit − Entry price|
R:R ratio = Target distance ÷ Stop distance
```

**Minimum acceptable R:R: 1.5:1** (risk 1 to make 1.5; prefer 2:1 or better). If R:R < 1.5:1, skip the trade.

> Position sizing and leverage are outside the scope of this skill. Apply your own risk management rules.

---

## Full Analysis Output Format

Produce this after completing all five steps:

```
═══════════════════════════════════════════════════
PAIR: [e.g. EUR/USD]  |  Date: [today's date]
═══════════════════════════════════════════════════

CHANNEL ANALYSIS
─────────────────────────────────────────────────
Weekly:  🟢/🔴/🟡  [Brief note — e.g. "HH/HL intact since Jan"]
Daily:   🟢/🔴/🟡  [Brief note — e.g. "20 SMA > 50 SMA, both rising"]
4H:      🟢/🔴/🟡  [Brief note — e.g. "Pulling back to 20 SMA"]
OVERALL BIAS: BULLISH / BEARISH / NEUTRAL
[Alignment note — e.g. "All timeframes aligned bearish — high conviction"]

SMA STATUS (Daily)
─────────────────────────────────────────────────
20 SMA: [value]  Slope: ↑/↓/→
50 SMA: [value]  Slope: ↑/↓/→
Price: above / below / at both SMAs

KEY LEVELS
─────────────────────────────────────────────────
[Resistance 2]  x.xxxxx  [type]
[Resistance 1]  x.xxxxx  [type]
>>> CURRENT PRICE: x.xxxxx <<<
[Support 1]     x.xxxxx  [type]
[Support 2]     x.xxxxx  [type]

RSI STATUS
─────────────────────────────────────────────────
Daily  RSI(14): [value]  → [zone]
4H     RSI(14): [value]  → [zone]
Momentum: Confirms / Stretched / Divergence

ENTRY TRIGGER
─────────────────────────────────────────────────
Trigger pattern: [Pin Bar / Engulfing / Inside Bar / None yet]
Location: [S&R level where it formed, or level to watch if None yet]
Timeframe: [4H / Daily]
Valid: Yes / No — [reason if No]
Next action: [Enter now / Alert set at x.xxxxx / Awaiting trigger / No trade — see notes]

TRADE SETUP
─────────────────────────────────────────────────
Direction:   LONG / SHORT
Entry:       x.xxxxx  ([aggressive/conservative])
Stop Loss:   x.xxxxx  ([X] pips risk)
Take Profit: x.xxxxx  ([Y] pips target)
R:R Ratio:   1:[Z]   → [Accept / Reject — below 1.5:1 minimum]

NOTES
─────────────────────────────────────────────────
[Any flags: conflicting timeframes, news risk, stretched RSI, etc.]
═══════════════════════════════════════════════════
```

---

## Timeframe Quick Reference

| Timeframe | TV Code | Purpose | Look-back |
|---|---|---|---|
| Weekly | `W` | Macro channel & major S&R | 12–18 months |
| Daily | `1D` | Primary trend + SMAs + RSI | 2–3 months |
| 4H | `240` | Entry zone & trigger candle | 2–3 weeks |

**Top-down rule:** Always Weekly → Daily → 4H. Never enter a 4H trade that contradicts the Weekly channel without explicit reason.
