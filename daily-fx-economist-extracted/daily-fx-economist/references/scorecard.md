# Economist Scorecard — Baseline & Scoring Criteria

## Purpose

This scorecard is the economist agent's persistent fundamental view on each currency.
It is updated only when new data changes the outlook — it is NOT recalculated from scratch
each day. Carry forward unchanged dimensions until new data warrants a revision.

---

## Scoring Criteria

### Rate Bias
| Score | Label | Definition |
|-------|-------|------------|
| Hawkish | H | CB is raising rates, has paused at high level with upside risk, or has explicitly pushed back on cuts |
| Neutral | N | CB is on hold with balanced two-way risks; no clear next move signal |
| Dovish | D | CB is cutting rates, has signalled cuts are coming, or has paused at low levels |

### Inflation Trend
| Score | Label | Definition |
|-------|-------|------------|
| Rising | ↑ | CPI is above target and/or accelerating |
| Stable | → | CPI is near target and moving sideways |
| Falling | ↓ | CPI is decelerating toward or below target |

### Growth Outlook (G8 only)
| Score | Label | Definition |
|-------|-------|------------|
| Positive | + | GDP growth above trend, PMIs in expansion territory (>50) |
| Neutral | = | GDP near trend, mixed PMI signals |
| Negative | − | GDP contraction or significant slowdown risk, PMIs contracting |

### Labour Market (G8 only)
| Score | Label | Definition |
|-------|-------|------------|
| Tight | T | Unemployment near cycle lows, wages elevated |
| Neutral | N | Unemployment near structural rate, wages normalising |
| Loosening | L | Unemployment rising, hiring slowing, wage growth fading |

### Overall Bias (summary)
| Score | Label | Definition |
|-------|-------|------------|
| Bullish | Bull | Net positive fundamentals — currency likely to outperform |
| Neutral | Neut | Mixed signals — no strong directional edge |
| Bearish | Bear | Net negative fundamentals — currency likely to underperform |

**Overall Bias Rule of Thumb (G8):**
- 3+ dimensions positive → Bullish
- 3+ dimensions negative → Bearish
- Mixed → Neutral

---

## Starting Scorecard Baseline (May 2026)

The agent updates this table as new data arrives. Last full review: May 2026.

| Currency | Rate Bias | Inflation | Growth | Labour | Overall |
|----------|-----------|-----------|--------|--------|---------|
| USD | Neutral | Stable | Neutral | Tight | Neutral |
| EUR | Dovish | Falling | Neutral | Neutral | Bearish |
| GBP | Neutral | Stable | Neutral | Loosening | Neutral |
| JPY | Hawkish | Rising | Neutral | Neutral | Neutral |
| AUD | Neutral | Stable | Neutral | Neutral | Neutral |
| NZD | Dovish | Falling | Negative | Neutral | Bearish |
| CAD | Dovish | Falling | Negative | Loosening | Bearish |
| CHF | Dovish | Falling | Neutral | Neutral | Bearish |
| CNY | Neutral | Falling | — | — | Neutral |
| INR | Neutral | Stable | — | — | Neutral |
| BRL | Hawkish | Rising | — | — | Bullish |
| MXN | Hawkish | Stable | — | — | Neutral |
| NOK | Neutral | Stable | — | — | Neutral |
| SEK | Dovish | Falling | — | — | Bearish |
| DKK | Dovish | Falling | — | — | Bearish |
| PLN | Neutral | Stable | — | — | Neutral |
| HUF | Neutral | Rising | — | — | Neutral |
| SGD | Neutral | Stable | — | — | Neutral |
| ILS | Neutral | Stable | — | — | Neutral |

*Note: "—" = dimension not tracked for non-G8 currencies.*

---

## Central Bank Meeting Calendar (approximate)

| Currency | Central Bank | Approx Meeting Frequency |
|----------|-------------|--------------------------|
| USD | Federal Reserve (FOMC) | ~8x per year (every 6–7 weeks) |
| EUR | European Central Bank (ECB) | ~8x per year |
| GBP | Bank of England (BoE) | ~8x per year |
| JPY | Bank of Japan (BoJ) | ~8x per year |
| AUD | Reserve Bank of Australia (RBA) | ~8x per year |
| NZD | Reserve Bank of New Zealand (RBNZ) | ~7x per year |
| CAD | Bank of Canada (BoC) | ~8x per year |
| CHF | Swiss National Bank (SNB) | 4x per year (quarterly) |
| CNY | People's Bank of China (PBOC) | Ongoing (no fixed schedule) |
| INR | Reserve Bank of India (RBI) | ~6x per year |
| BRL | Banco Central do Brasil (BCB) | ~8x per year |
| MXN | Banco de México (Banxico) | ~8x per year |
| NOK | Norges Bank | ~8x per year |
| SEK | Riksbank | ~6x per year |
| DKK | Danmarks Nationalbank | Follows ECB (peg policy) |
| PLN | Narodowy Bank Polski (NBP) | ~11x per year |
| HUF | Magyar Nemzeti Bank (MNB) | ~10x per year |
| SGD | Monetary Authority of Singapore (MAS) | 2x per year (semi-annual) |
| ILS | Bank of Israel | ~8x per year |

---

## How to Update the Scorecard

1. A new data release triggers an update for the affected currency only.
2. State what changed and why in the briefing under Step 5.
3. The updated table in the daily report IS the new baseline — carry it forward next session.
4. Never revert to a prior score without a data reason.
