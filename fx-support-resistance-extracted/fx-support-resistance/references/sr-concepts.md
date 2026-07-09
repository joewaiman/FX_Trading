# S&R Concepts Reference — Anatomy, Rules & Pattern Diagrams

## The Zone Principle

Support and resistance do **not** operate at a single price. They operate within a **zone** —
a band of price defined by the overlap between candle bodies and wicks at a significant level.

```
RESISTANCE ZONE (horizontal)
┌─────────────────────────────────────────────────────┐
│                        ↑ Highest wick in zone        │  ← upper boundary
│   ┌──┐  ┌──┐          │                             │
│   │  │  │  │  ━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━  │  ← lower boundary
│   └──┘  └──┘          ↓ Lowest body in zone         │
└─────────────────────────────────────────────────────┘
Price enters the zone → expect rejection / reversal

SUPPORT ZONE (horizontal)
┌─────────────────────────────────────────────────────┐
│   ┌──┐  ┌──┐          ↑ Highest body in zone        │  ← upper boundary
│   │  │  │  │  ━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━  │  ← lower boundary
│   └──┘  └──┘          ↓ Lowest wick in zone         │
│                                                      │
└─────────────────────────────────────────────────────┘
Price enters the zone → expect bounce / buyers appear
```

---

## Channel Drawing — Body & Wick Rules

### Why bodies and wicks are treated differently

- **Candle body** = where price actually committed (open to close). This is the zone.
- **Candle wick** = price explored but was rejected. Wicks mark extremes, not zones.

Zones are defined by bodies. Extremes are marked by wicks. You can draw through a wick.
You must never draw through a body.

### Channel Support — Wick to Body Rule

```
Step 1: Anchor at the LOWEST WICK  (absolute low)
         │
         │ ← draw line upward
         ▼
Step 2: Connect to the HIGHEST BODY you can reach without crossing any bodies
         ▲
         │ ← this is the aggressive support line
         │
Step 3: From that body, repeat — connect to the next lowest wick
         │
         ▼ ← this creates the channel support zone band
```

Aggressive support line = the inner (higher) of the two lines
Conservative support line = the outer (lower) line touching the wicks

### Channel Resistance — Body to Wick Rule

```
Step 1: Anchor at the HIGHEST BODY  (the top of a candle body, not the wick)
         │
         │ ← draw line downward
         ▼
Step 2: Connect to the LOWEST WICK you can reach without crossing any bodies
         ▲
         │ ← this is the aggressive resistance line
         │
Step 3: From that wick, repeat — connect to the next highest body
         │
         ▼ ← this creates the channel resistance zone band
```

---

## Nested Channels

Channels form within channels. A larger macro channel (Weekly) can contain a smaller
micro channel (Daily) moving in the same or opposite direction.

```
MACRO CHANNEL (Weekly — Bullish)
╔══════════════════════════════════════════════════╗
║  ▔▔▔▔▔▔▔▔▔▔  MACRO RESISTANCE ZONE  ▔▔▔▔▔▔▔▔▔ ║
║                                                  ║
║    MICRO CHANNEL (Daily — Bearish pullback)      ║
║    ┌─────────────────────────────┐               ║
║    │  micro resistance zone      │               ║
║    │                             │               ║
║    │   price moving down within  │               ║
║    │   the larger bullish macro  │               ║
║    │                             │               ║
║    │  micro support zone         │               ║
║    └─────────────────────────────┘               ║
║                                                  ║
║  ▁▁▁▁▁▁▁▁▁▁  MACRO SUPPORT ZONE  ▁▁▁▁▁▁▁▁▁▁▁  ║
╚══════════════════════════════════════════════════╝

Interpretation: Daily bearish channel = pullback within a larger Weekly uptrend
Trade implication: Look for longs when Daily micro channel reaches macro support zone
```

---

## Head & Shoulders — Full Pattern Anatomy

### Standard Head & Shoulders (Bearish — appears in uptrend)

```
           HEAD
            ▲
           /│\
          / │ \
L.SHOULDER  │  R.SHOULDER
    ▲        │        ▲
   /│\       │       /│\   ← Right shoulder should be LOWER than left
  / │ \      │      / │ \
 /  │  \     │     /  │  \
/   │   \    │    /   │   \
    │    \   │   /    │
    │     ▼  │  ▼     │
    │    NECKLINE──────────── ← connect these two lows
    │                         ← flat or slightly sloped
    │                ↓ neckline break = entry signal
    │
UPTREND BEFORE PATTERN
```

**Critical detail (your rule):** The right shoulder must form a **lower low** in the pullback
before it rises. This breaking of the previous pullback low signals the uptrend is weakening.
A breaking low in an uptrend = good selling area.

**Target calculation:**
```
Distance = Head high – Neckline
Target   = Neckline breakout point – Distance
```

---

### Inverse Head & Shoulders (Bullish — appears in downtrend)

```
DOWNTREND BEFORE PATTERN
    │
    │    NECKLINE──────────── ← connect these two highs
    │   ▲                ▲
    │  /│\              /│\
    │ / │ \            / │ \
    │/  │  \          /  │  \
        │   \        /   │
L.SHOULDER  ▼        ▼  R.SHOULDER
             \      /        ← Right shoulder should be HIGHER than left
              \    /
               \  /
                \/
               HEAD  ← lowest point of entire pattern

                ↑ neckline break above = entry signal
```

**Critical detail:** The right shoulder forms a **higher low** than the head. This signals
selling pressure is weakening and buyers are stepping in earlier each time.

**Target calculation:**
```
Distance = Neckline – Head low
Target   = Neckline breakout point + Distance
```

---

## Neckline Types

| Neckline | Appearance | Signal Quality |
|---|---|---|
| Horizontal | Flat line | Standard — reliable |
| Upward sloping | Tilts up-right | Moderate — still valid |
| Downward sloping (H&S) | Tilts down-right | Strong bearish signal — more powerful |
| Downward sloping (Inverse) | Tilts down-right | Weaker — approach with caution |

---

## S&R Flip Rule

When a resistance zone is broken, it often becomes support. When a support zone is broken,
it often becomes resistance. This is called a **flip**.

```
BEFORE BREAK:     [──────RESISTANCE ZONE──────]
                  price approaches from below ↑

AFTER BREAK:      price breaks above and closes above zone ↑
                  zone now acts as:
                  [──────SUPPORT ZONE──────]
                  price retests from above ↓ then bounces up ↑
```

This is why breakout retests are often the best entry points — the old enemy becomes
the new friend.

---

## Confluence — Why Overlapping Zones Matter

When two or more of the following align at the same price area, the signal strength multiplies:

- Horizontal S&R zone (major, score 3)
- Channel boundary (support or resistance)
- Diagonal trendline zone
- Round number (1.2000, 150.00 etc.)
- H&S neckline level
- 20 or 50 SMA level

**Confluence of 3+ factors = highest probability zone on the chart.**
This is where you look for your entry trigger.

---

## Common Mistakes to Avoid

| Mistake | Why it's wrong |
|---|---|
| Drawing too many S&R levels | Creates confusion — only mark big swings |
| Using a single line, not a zone | Price reacts to areas, not exact pips |
| Including small pullbacks in horizontal S&R | Small swings are not significant |
| Entering on wick break of neckline | Always wait for a candle body close |
| Ignoring timeframe hierarchy | Weekly zones override Daily zones |
| Treating broken zones as still active | Mark them as flipped or remove them |
