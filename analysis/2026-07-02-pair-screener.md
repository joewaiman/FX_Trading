# FX Pair Screener — 2026-07-02 (W27)

Basket: 19 currencies | Scanned: 18/18 USD pairs
Method: `fx-pair-screener` skill — technical strength vs USD (Weekly + Daily), candidate generation, liquidity gate, cross-pair confirmation.

> ⚠️ USD in a broad uptrend this week — almost everything scored bearish vs USD, compressing the spread. Phase 4 cross-pair confirmation corrects for this by measuring relative strength directly between the two currencies.

## Currency Strength Rankings (vs USD)

| Band | Currencies |
|------|-----------|
| 🟢 Bullish (+1/+2) | CNY +2, GBP +1, MXN +1, HUF +1 |
| 🟡 Neutral (0) | BRL, ILS |
| 🔴 Bearish (−1/−2) | EUR, NZD, CHF, CAD, NOK, SGD, PLN, DKK (−1); AUD, SEK (−2) |
| 🔴 Strong Bearish (−3/−4) | INR −3, JPY −3 |

Full per-currency detail (raw score, inversion, W/D notes, Daily RSI) captured in session.

- **Top 3 bullish:** CNY +2, GBP +1, MXN +1 (HUF +1 tied)
- **Bottom 3 bearish:** JPY −3, INR −3, SEK −2 (AUD −2 tied)

## Candidates → Gate → Confirmation

Generated 9 · Passed liquidity gate 9 · Confirmed on cross chart 9 (0 rejected).
All 9 loaded in correct orientation with ~15mo history.

| Pair | Dir | Loaded | Weekly | Daily | D-RSI | Conviction |
|------|-----|--------|--------|-------|-------|-----------|
| CNYJPY | LONG | CNYJPY | 🟢 | 🟢 | 54.8 | ★★★ |
| CNYSEK | LONG | CNYSEK | 🟢 | 🟢 | 65.6 | ★★★ |
| MXNSEK | LONG | MXNSEK | 🟢 | 🟢 | 62.5 | ★★★ |
| CNYINR | LONG | CNYINR | 🟢 | 🟡 | 54.9 | ★★ |
| GBPJPY | LONG | GBPJPY | 🟢 | 🟡 | 56.8 | ★★ |
| GBPINR | LONG | GBPINR | 🟢 | 🟡 | 54.8 | ★★ (not shortlisted) |
| MXNJPY | LONG | MXNJPY | 🟢 | 🟡 | 45.2 | ★★ (not shortlisted) |
| MXNINR | LONG | MXNINR | 🟢 | 🟡 | 47.0 | ★★ (not shortlisted) |
| GBPSEK | LONG | GBPSEK | 🟡 | 🟢 | 72.7 | ★ (not shortlisted) |

## Shortlist (handed to fx-technical-analysis)

1. **CNYJPY** LONG ★★★ — CNY +2 vs JPY −3, W+D aligned bullish
2. **CNYSEK** LONG ★★★ — clean stacked uptrend both TFs
3. **MXNSEK** LONG ★★★ — clean stacked uptrend both TFs
4. **CNYINR** LONG ★★ — strong differential, Daily SMAs tangled (pullback setup)
5. **GBPJPY** LONG ★★ — cleanest freely-floating major divergence, Daily rangebound

## Caveats

- **All three ★★★ setups involve a managed currency** (CNY = PBOC daily fixing; INR = RBI intervention). Signals valid but gap-prone. GBP is the only clean freely-floating major on the bullish side.
- Purely technical strength-vs-USD — does **not** yet incorporate a W27 fundamental view (CONTEXT.md fundamentals are from W26).

See: `2026-07-02-shortlist-technical.md` for the follow-on technical analysis.
