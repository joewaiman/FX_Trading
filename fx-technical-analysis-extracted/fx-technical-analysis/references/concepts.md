# Entry Trigger Patterns & RSI Divergence — Reference

## Entry Trigger Candlestick Patterns

### Pin Bar

A single candle with a small body and a long wick, showing price rejection at a level.

```
Long setup (at support):       Short setup (at resistance):
    │  ← small upper wick           ┌─┐ ← long upper wick
   ┌┴┐                              │ │
   └─┘ ← small body near top        └┬┘ ← small body near bottom
    ║  ← long lower wick             │  ← small lower wick
```

**Valid when:**
- Wick is at least 2× the length of the body
- Body closes in the upper third (bullish) or lower third (bearish) of the candle's range
- Forms at a clearly defined S&R level

---

### Engulfing Candle

A two-candle pattern where the second candle's body fully covers the first candle's body.

```
Bullish engulfing (at support):    Bearish engulfing (at resistance):
  ┌─┐  small bearish candle          ┌─┐  large bearish candle
  └─┘                                └─┘
 ┌───┐ large bullish candle          ┌─┐  small bullish candle
 └───┘                               └─┘
```

**Valid when:**
- The engulfing candle's body fully covers the prior candle's body (wicks do not need to be covered)
- Volume is visibly higher on the engulfing candle (if volume data available)
- Forms at a key S&R level

---

### Inside Bar Breakout

A two-candle pattern where the second candle's range is fully contained within the first (the "mother bar").

```
 ┌──────┐  ← mother bar (larger range)
 │ ┌──┐ │  ← inside bar (smaller range, fully inside)
 │ └──┘ │
 └──────┘
```

**Entry:** Place a buy stop above the mother bar high (long) or sell stop below the mother bar low (short).
**Trigger fires** when price breaks out of the mother bar's range in the direction of the bias.

**Valid when:**
- Inside bar forms after a clear impulse move (consolidation before continuation)
- The breakout direction aligns with the channel bias

---

## RSI Divergence

Divergence occurs when price and RSI disagree — a sign of weakening momentum and potential reversal.

### Bullish Divergence (potential reversal up)

Price makes a **lower low**, but RSI makes a **higher low**.
Bearish momentum is exhausting — buyers are absorbing the new lows.

```
Price:   LL₁ ————— LL₂  (LL₂ < LL₁)
RSI:     HL₁ ————— HL₂  (HL₂ > HL₁)
```

### Bearish Divergence (potential reversal down)

Price makes a **higher high**, but RSI makes a **lower high**.
Bullish momentum is exhausting — sellers are capping the new highs.

```
Price:   HH₁ ————— HH₂  (HH₂ > HH₁)
RSI:     LH₁ ————— LH₂  (LH₂ < LH₁)
```

**Use divergence as a warning signal, not a standalone entry.** Confirm with a trigger candle at S&R before acting.
