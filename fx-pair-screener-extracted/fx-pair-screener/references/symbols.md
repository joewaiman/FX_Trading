# Currency Symbols — USD Pairs, Quote Convention, and Liquidity Tiers

## Symbol Table

| Currency | USD Pair | Pair Type | Bullish chart means | Invert for currency score? |
|---|---|---|---|---|
| EUR | EURUSD | XXX/USD | EUR strong | No |
| GBP | GBPUSD | XXX/USD | GBP strong | No |
| AUD | AUDUSD | XXX/USD | AUD strong | No |
| NZD | NZDUSD | XXX/USD | NZD strong | No |
| JPY | USDJPY | USD/XXX | JPY weak | **Yes** |
| CHF | USDCHF | USD/XXX | CHF weak | **Yes** |
| CAD | USDCAD | USD/XXX | CAD weak | **Yes** |
| SEK | USDSEK | USD/XXX | SEK weak | **Yes** |
| NOK | USDNOK | USD/XXX | NOK weak | **Yes** |
| SGD | USDSGD | USD/XXX | SGD weak | **Yes** |
| PLN | USDPLN | USD/XXX | PLN weak | **Yes** |
| MXN | USDMXN | USD/XXX | MXN weak | **Yes** |
| INR | USDINR | USD/XXX | INR weak | **Yes** |
| HUF | USDHUF | USD/XXX | HUF weak | **Yes** |
| DKK | USDDKK | USD/XXX | DKK weak | **Yes** |
| CNY | USDCNY | USD/XXX | CNY weak | **Yes** |
| BRL | USDBRL | USD/XXX | BRL weak | **Yes** |
| ILS | USDILS | USD/XXX | ILS weak | **Yes** |

## Inversion Rule

For **USD/XXX pairs**, the Phase 1 raw score must have its sign flipped to get the currency score:

| Raw chart score | Currency score |
|---|---|
| +4 (chart strongly bullish) | −4 (currency Strong Bearish) |
| +2 | −2 (Bearish) |
| 0 | 0 (Neutral) |
| −2 | +2 (Bullish) |
| −4 | +4 (Strong Bullish) |

Example: USDJPY Weekly bullish (+2) + Daily bullish (+1) + RSI 60 rising (+1) = raw +4 → JPY score = **−4 (Strong Bearish)**.

For **XXX/USD pairs** (EUR, GBP, AUD, NZD), no inversion — the chart score is the currency score directly.

---

## Liquidity Tiers

| Tier | Currencies | USD pair reliability | Cross pair data on TradingView |
|---|---|---|---|
| 1 — Major | EUR, GBP, JPY, CHF, AUD, NZD, CAD | Deep, reliable | Always available |
| 2 — Liquid minor | SEK, NOK, SGD, MXN, CNY | Reliable | Usually available (EURSEK, AUDSGD, etc.) — verify at Phase 3 |
| 3 — Thin | PLN, HUF, DKK, INR, BRL, ILS | Available | Cross pairs vs non-USD rarely available — expect most Phase 3 failures here |

---

## Common Cross Pair Symbols

| Bullish / Bearish | TradingView Symbol |
|---|---|
| EUR / JPY | EURJPY |
| EUR / GBP | EURGBP |
| EUR / CHF | EURCHF |
| EUR / CAD | EURCAD |
| EUR / AUD | EURAUD |
| EUR / NZD | EURNZD |
| EUR / SEK | EURSEK |
| EUR / NOK | EURNOK |
| GBP / JPY | GBPJPY |
| GBP / CHF | GBPCHF |
| GBP / CAD | GBPCAD |
| GBP / AUD | GBPAUD |
| GBP / NZD | GBPNZD |
| AUD / JPY | AUDJPY |
| AUD / NZD | AUDNZD |
| AUD / CAD | AUDCAD |
| AUD / CHF | AUDCHF |
| AUD / SGD | AUDSGD |
| NZD / JPY | NZDJPY |
| NZD / CAD | NZDCAD |
| NZD / CHF | NZDCHF |
| CAD / JPY | CADJPY |
| CAD / CHF | CADCHF |
| CHF / JPY | CHFJPY |
| SGD / JPY | SGDJPY |
| MXN / JPY | MXNJPY |
| NOK / JPY | NOKJPY |
| SEK / JPY | SEKJPY |

> For combinations not in this table, try `XXXYYY` first, then `YYYXXX`. Confirm data is available via the Phase 3 liquidity gate before proceeding with analysis.
