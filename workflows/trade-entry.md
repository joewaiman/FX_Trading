# Trade Entry — Technical Analysis to Entry Confirmation

Run this for each pair selected from the weekly scan.
Output: either a full trade setup (entry/SL/TP/R:R) or a "waiting" status with an alert level.

---

## Prerequisites

Before starting:
- Confirm the fundamental bias for this pair from the weekly scorecard (`fundamental-analysis/YYYY-WXX.md`)
- TradingView must be open with SMA(20), SMA(50), and RSI(14) visible on the chart
- Note: SMA periods must be configured manually in TradingView — they cannot be set programmatically

---

## Step 1 — Technical Analysis

**Skill:** `fx-technical-analysis`

Work top-down: Weekly → Daily → 4H.

Check on each timeframe:
- Channel direction: Bullish (HH/HL) / Bearish (LH/LL) / Sideways
- SMA position and slope (20 SMA vs 50 SMA)
- RSI reading and zone

**Blocking conditions — do not proceed if:**
- RSI > 70 on 4H in a bearish setup (overbought — wait for reset)
- RSI < 30 on 4H in a bullish setup (oversold — wait for reset)
- Weekly and Daily channels conflict (reduce conviction, consider skipping)

Save output to: `analysis/YYYY-MM-DD-PAIR-technical.md`

---

## Step 2 — S&R Zone Mapping

**Skill:** `fx-support-resistance`

Map the key zones that will define the entry, stop, and targets.

- Draw the channel (body-line to wick-line band defines the buy/sell zone)
- Map horizontal S&R zones — big swings only, 6-month lookback, rate 1–3 stars
- Map diagonal S&R zones if applicable
- Check for Head & Shoulders pattern
- Note confluence areas (where two or more zones overlap — these are the highest priority)

The channel buy/sell zone is your primary entry target.
The opposing channel boundary is your TP2 target.

---

## Step 3 — Set a TradingView Alert

Set an alert at the edge of the entry zone (e.g. 20 SMA level or channel support/resistance line).

```
TradingView → Alert → Condition: [PAIR] crosses [price level]
Alert message: "[PAIR] entry zone reached — run entry confirmation"
```

Once the alert is set, you do not need to watch the chart continuously.

---

## Step 4 — Entry Confirmation (when alert fires)

**Skill:** `fx-entry-confirmation`

Run this when the TradingView alert fires or when you check the chart and see price approaching the zone.

Inputs needed (from Step 1 output):
- Overall bias (Bullish / Bearish)
- Key levels (support and resistance prices)
- RSI readings (Daily and 4H)
- Channel alignment summary
- Divergence status

The skill outputs one of three stages:

| Stage | Meaning | Action |
|-------|---------|--------|
| A — Waiting | Price > 20 pips from zone | Check back later, alert already set |
| B — At zone, no trigger | Price in zone, no pattern yet | Monitor next 4H candle close |
| C — Trigger confirmed | Pattern + confluence ≥ 3/5 | Execute (see trade-management workflow) |

**R:R check before executing:**
- Minimum 1.5:1 to TP1 required (prefer 2:1 or better) — if below, skip the trade
- Maximum stop width: 50 pips on 4H setup, 80 pips on Daily setup — if wider, zone is too loose, skip

---

## Entry Methods by Pattern

| Pattern | Entry |
|---------|-------|
| Pin bar | Open of next 4H candle after pin bar closes |
| Engulfing | Open of next 4H candle after engulfing candle closes |
| Inside bar | Break of inside bar high (long) or low (short) + 2–5 pip buffer |

---

## If the Setup Is Invalidated

A setup is invalidated (close the file, do not trade) if:
- Price blows through the entry zone without forming a trigger pattern
- RSI divergence directly contradicts the bias
- A new fundamental release materially changes the currency's score
- Price has already moved to TP1 without you entering — R:R is gone
