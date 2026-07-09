---
name: fx-pair-screener
description: >
  Use this skill whenever the user wants to find pair trading opportunities across the full 19-currency basket.
  Triggers include: screening for cross pair trades, finding the strongest and weakest currencies, building a
  trade shortlist, or identifying opportunities beyond the 8 major pairs.
  This skill scans all 18 non-USD currencies against USD for trend direction, filters by TradingView data
  availability, confirms cross pair chart alignment, and outputs a ranked shortlist of 3–5 candidates.
  Run before fx-technical-analysis when you do not have a specific pair in mind.
  Also trigger when the user asks "what pairs should I look at?", "which currencies are strong/weak?",
  "find me a trade", "what's moving?", or wants to explore cross pair opportunities across the full basket.
---

# FX Pair Screener

Scans the full 19-currency basket for pair trading opportunities using technical trend alignment.
Outputs a ranked shortlist of 3–5 cross pairs to hand off to `fx-technical-analysis` for entry timing.

> Currency symbols, quote conventions, and liquidity tiers → `references/symbols.md`

---

## Workflow Overview

```
Phase 0: Confirm prerequisites (SMA setup)
         ↓
Phase 1: Currency Strength Assessment
         Score all 18 non-USD currencies on Weekly + Daily (against USD)
         ↓
Phase 2: Candidate Pair Generation
         Pair top 3 bullish vs top 3 bearish → up to 9 candidates
         ↓
Phase 3: Liquidity Gate
         Verify TradingView data exists for each cross pair
         ↓
Phase 4: Cross Pair Confirmation
         Check trend direction on the actual cross pair chart
         ↓
Phase 5: Output — ranked shortlist with conviction ratings
```

---

## Phase 0 — Prerequisites

Same SMA setup as `fx-technical-analysis`. Before starting:

1. Ensure two **Simple Moving Averages** are on the chart: **Length 20** and **Length 50**
2. Ensure **RSI (14)** is visible
3. Run `chart_get_state` — record entity IDs for SMA(20), SMA(50), and RSI(14)
4. **Verify SMA periods:** confirm the returned inputs show `length: 20` and `length: 50`. If wrong, ask the user to correct them before proceeding.

> SMA periods cannot be set programmatically — they must be configured manually in TradingView once and will apply across all symbols as you switch charts throughout the scan.

---

## Phase 1 — Currency Strength Assessment

**Objective:** Score all 18 non-USD currencies as Strong Bullish / Bullish / Neutral / Bearish / Strong Bearish using Weekly and Daily chart structure against USD.

### Quote Convention (critical)

TradingView uses USD as both base and quote currency depending on the pair. A bullish chart does **not** always mean the first-named currency is strong.

- **XXX/USD pairs** (EURUSD, GBPUSD, AUDUSD, NZDUSD): bullish chart = XXX strong. **No inversion needed.**
- **USD/XXX pairs** (USDJPY, USDCAD, USDSEK, etc.): bullish chart = USD strong = XXX weak. **Invert the score.**

Full symbol table and inversion column → `references/symbols.md`.

### Scoring

For each currency, assess its USD pair on Weekly and Daily:

| Factor | Score |
|---|---|
| Weekly: clear bullish channel (HH/HL + 20 SMA > 50 SMA, both rising) | +2 |
| Weekly: sideways or no clear structure | 0 |
| Weekly: clear bearish channel (LH/LL + 20 SMA < 50 SMA, both falling) | −2 |
| Daily: clear bullish channel | +1 |
| Daily: sideways | 0 |
| Daily: clear bearish channel | −1 |
| Daily RSI 50–70 and rising | +1 |
| Daily RSI near 50 or flat | 0 |
| Daily RSI 30–50 and falling | −1 |

**Score range: −4 to +4**

> For USD/XXX pairs, calculate the raw score from the chart first, then **invert the sign** to get the currency score.
> Example: USDJPY chart scores +3 → JPY currency score = −3 (Strong Bearish).

### Classification

| Score | Label |
|---|---|
| +3 to +4 | 🟢 **Strong Bullish** |
| +1 to +2 | 🟢 **Bullish** |
| 0 | 🟡 **Neutral** |
| −1 to −2 | 🔴 **Bearish** |
| −3 to −4 | 🔴 **Strong Bearish** |

### Data Collection Sequence

For each of the 18 currencies in order (see `references/symbols.md` for full symbol list):

```
chart_set_symbol    symbol=[USD_PAIR]

chart_set_timeframe timeframe="W"
data_get_ohlcv      summary=true          ← swing structure (HH/HL or LH/LL)
data_get_study_values                     ← SMA(20), SMA(50)

chart_set_timeframe timeframe="1D"
data_get_ohlcv      summary=true
data_get_study_values                     ← SMA(20), SMA(50), RSI(14)
```

> Weekly RSI is not collected — Weekly is used for swing structure and SMA position only.
> Full Phase 1 scan = ~36 MCP calls. Collect all 18 currencies before scoring.

### Special Cases

| Currency | Note |
|---|---|
| DKK | Pegged to EUR (±2.25% band). USDDKK mirrors EURUSD. Score it, but treat as a EUR proxy — not an independent signal. |
| CNY | Managed float with daily PBOC fixing. Technical signals are valid but may gap on fixing changes. |
| INR | RBI intervenes actively to limit INR appreciation. Bullish USD/INR trends are persistent; sharp reversals uncommon. |

### Phase 1 Output

```
CURRENCY STRENGTH RANKINGS
─────────────────────────────────────────────────
🟢 Strong Bullish (+3/+4): [currency (+score), ...]
🟢 Bullish (+1/+2):        [currency (+score), ...]
🟡 Neutral (0):            [currency, ...]
🔴 Bearish (−1/−2):        [currency (−score), ...]
🔴 Strong Bearish (−3/−4): [currency (−score), ...]
```

---

## Phase 2 — Candidate Pair Generation

**Objective:** Generate candidate cross pairs by combining the most bullish currencies with the most bearish.

1. Select the **top 3** currencies by score — must be Bullish or Strong Bullish
2. Select the **bottom 3** currencies by score — must be Bearish or Strong Bearish
3. Generate all combinations: up to **9 candidate pairs**

**Direction:** Long the bullish currency, short the bearish.
**Naming:** Write the bullish currency first — e.g. EUR (+4) vs JPY (−4) → **EUR/JPY Long**.

**Edge cases:**
- Fewer than 3 qualifying on one side → reduce combinations accordingly
- Fewer than 2 qualifying on either side → output "No clear pair candidates — market is too mixed" and stop
- If USD appears in the top or bottom group → skip; USD is the measurement base, not a trade candidate here

> **USD trend note:** When USD is in a strong directional trend, many currencies will rank uniformly bullish or bearish against it, compressing score spread. Phase 4 cross pair confirmation corrects for this by measuring relative strength directly between the two candidate currencies.

---

## Phase 3 — Liquidity Gate

**Objective:** Eliminate cross pairs with no viable TradingView data before spending analysis time on them.

For each of the 9 candidate pairs:

```
chart_set_symbol  symbol=[CROSS_PAIR]
```

- Chart loads with valid price data and a reasonable bar history → **✅ pass**
- Symbol unknown, no data returned, or chart is sparse (< 6 months of bars) → **❌ eliminate**

**Practical notes:**
- Try standard ordering first (e.g. `EURJPY`). If that fails, try reversed ordering (`JPYEUR`) — TradingView only carries one direction.
- Pairs crossing two Tier 3 currencies (PLN, HUF, DKK, INR, BRL, ILS) almost always fail. Their USD pairs are available; their direct crosses typically are not.
- If data loads but spreads appear extreme, treat as eliminated.

After the gate, retain the **top 3 pairs** ranked by score differential (bullish score + |bearish score|, highest first). Do not output more than 3. These are options to analyse, not trades to take — the user decides which to pursue.

---

## Phase 4 — Cross Pair Confirmation

**Objective:** Verify that the cross pair chart itself confirms the expected trend direction.

A cross pair chart measures relative strength directly between the two currencies. Even when both USD legs point the right way, the cross rate can be in a range or trending against expectation due to different speeds of move. This phase catches those mismatches.

For each surviving pair:

```
chart_set_symbol    symbol=[CROSS_PAIR]

chart_set_timeframe timeframe="W"
data_get_ohlcv      summary=true
data_get_study_values                   ← SMA(20), SMA(50)

chart_set_timeframe timeframe="1D"
data_get_ohlcv      summary=true
data_get_study_values                   ← SMA(20), SMA(50), RSI(14)
```

Apply the same channel classification as `fx-technical-analysis`:

| Weekly | Daily | Conviction | Interpretation |
|---|---|---|---|
| 🟢 | 🟢 | ★★★ High | All aligned — strong candidate |
| 🟢 | 🟡 | ★★ Moderate | Daily retracing within Weekly trend — preferred entry setup |
| 🟢 | 🔴 | ★ Low | Daily pulling back hard; include only if no stronger alternatives |
| 🟡 | any | ★ Weak | No macro trend; flag and include only as a last resort |
| Trend **opposes** expected direction | | **Reject** | Score differential did not translate to the cross rate — eliminate |

**Reject condition:** If the cross pair is trending the *opposite* direction to what Phase 1 scores implied (e.g. EUR/JPY in a clear bearish channel when EUR scored +4 and JPY scored −4), eliminate the pair. The divergence exists in USD terms but not in direct terms — this is not a tradeable setup.

---

## Phase 5 — Output

```
═══════════════════════════════════════════════════
FX PAIR SCREENER  |  Date: [today's date]
Basket: 19 currencies  |  Scanned: [N]/18 USD pairs
═══════════════════════════════════════════════════

CURRENCY STRENGTH RANKINGS
─────────────────────────────────────────────────
🟢 Strong Bullish: [currency (+n), ...]
🟢 Bullish:        [currency (+n), ...]
🟡 Neutral:        [currency, ...]
🔴 Bearish:        [currency (−n), ...]
🔴 Strong Bearish: [currency (−n), ...]

CANDIDATE PAIRS
─────────────────────────────────────────────────
Generated: [N]  |  After liquidity gate: [N]  |  After cross confirmation: [N]

SHORTLIST
─────────────────────────────────────────────────
1. [PAIR]  LONG/SHORT  ★★★  [reason — e.g. "EUR +4 vs JPY −4, W/D cross aligned bullish, RSI 62 rising"]
2. [PAIR]  LONG/SHORT  ★★   [reason — note any caveats]
3. [PAIR]  LONG/SHORT  ★    [reason — flag weaknesses explicitly]

ELIMINATED
─────────────────────────────────────────────────
[PAIR] — no TradingView data
[PAIR] — cross chart opposes expected direction: [note]
[PAIR] — [other reason]

NEXT STEP
─────────────────────────────────────────────────
Run fx-technical-analysis on each shortlisted pair for 4H structure, entry trigger, and trade setup.
═══════════════════════════════════════════════════
```

---

## Timeframe Quick Reference

| Timeframe | TV Code | Used in |
|---|---|---|
| Weekly | `W` | Phase 1 (USD pairs), Phase 4 (cross pairs) |
| Daily | `1D` | Phase 1 (USD pairs), Phase 4 (cross pairs) |
| 4H | — | Not used here — handed off to `fx-technical-analysis` |

**Scope boundary:** This skill identifies *which* pairs to trade. Hand off to `fx-technical-analysis` for *when* and *where* to enter.
