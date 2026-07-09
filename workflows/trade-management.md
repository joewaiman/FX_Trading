# Trade Management — After Entry

Run this once a trade is live. Covers stop management, partial closes, and logging the outcome.

---

## Immediately After Entry

Update the trade file (`analysis/YYYY-MM-DD-PAIR-technical.md`) with:
- Entry price (actual fill, not the planned level)
- Stop loss price
- TP1 price and pip distance
- TP2 price and pip distance
- R:R at entry
- Trade status: **OPEN**

---

## Stop Management

| Condition | Action |
|-----------|--------|
| Trade immediately moves against you | Hold — stop is already placed beyond the zone |
| Price reaches 1:1 R (profit = initial risk) | Move stop to breakeven (entry price) |
| Price reaches TP1 | Move stop to entry or just beyond entry — protect the gain |
| Price shows a strong reversal candle at a key level | Consider closing early — do not wait for stop to be hit |

**Never widen a stop.** If price is approaching your stop, it means the setup was wrong — do not move the stop further away to avoid the loss.

---

## TP1 — First Partial Close (50%)

Close 50% of the position when price reaches TP1.

After closing 50%:
- Log TP1 hit in the trade file
- Move stop to breakeven if not already done
- Let remaining 50% run to TP2

---

## TP2 — Final Close (remaining 50%)

Close remaining 50% when price reaches TP2 or hits the trailing stop.

After final close:
- Update trade file with exit price, pips won/lost, and outcome
- Change trade status to **CLOSED**
- Note anything that differed from the plan (early exit, stop tightened, entry missed)

---

## If Stopped Out

Update the trade file:
- Exit price (stop-out level)
- Pips lost
- Trade status: **CLOSED — STOPPED OUT**
- Note: did price respect the zone and bounce, or blow straight through? (useful for reassessing the level)

Was the stop-out avoidable?
- If price wicked through your stop and reversed — normal, no action
- If fundamentals changed and you ignored them — note for next scan
- If the entry zone was too wide — adjust how zones are drawn

---

## Reassessing After a Stop-Out

A stopped trade does not automatically invalidate the pair for the week. Ask:
1. Is the fundamental bias still intact?
2. Has price reset to a better entry level?
3. Is RSI now in a more favourable zone?

If yes to all three — the setup may be valid again. Re-run the **trade-entry** workflow from Step 1 with fresh eyes, not with the assumption the previous analysis was correct.

---

## Correlation Risk Monitoring

If you have more than one open trade:
- List all open positions and the currencies involved
- Flag any currency that appears on both sides of two different trades (e.g. long SEK in SEKJPY + long SEK in EURSEK short)
- If correlated: size down both positions, or close the weaker setup

Correlation doubles your real exposure — treat two correlated trades as one oversized position.
