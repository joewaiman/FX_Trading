# FX Pair Screener — 2026-07-09 (W28)

**Time of scan:** ~15:40 UTC | **Analyst:** Claude Code
**Fundamentals:** `fundamental-analysis/2026-W28.md` | **EUR/USD status:** `analysis/2026-07-09-EURUSD-technical-rerun.md`

---

## Verdict Up Front

**No trade. The technical scan and the fundamental scan point in opposite directions, and every
candidate fails one gate or the other.**

- The technicals say **short JPY**. JPY is the weakest currency in the basket on price action (−4).
- The fundamentals say **long JPY**. JPY is the *second strongest* currency in the basket (🟢 Mild
  Bullish, #2 of 18), and `fundamental-analysis/2026-W28.md` lists it as a **valid long leg**.

Under `CLAUDE.md`'s entry gate — *"Do not enter a trade where either leg is Conflicted"* — you cannot
short a currency that your own fundamental scorecard rates bullish. Every technically attractive pair
on this board is a short-JPY expression. **All of them are blocked.**

Meanwhile the only non-EUR pairs whose *both legs pass the fundamental gate* — USD/CNH, USD/ILS,
USD/HUF — all have **bearish Weekly charts** that oppose the long. Blocked from the other side.

---

## Data Integrity Notes

This scan could not use the skill's specified data source, and the workaround is worth recording.

1. **`data_get_study_values` is broken — worse than Bug 2 describes.** On EUR/USD Daily it returned only
   **2 of 4 studies** (RSI and one SMA missing entirely), and the single MA value it did return
   (`1.15664`) matched neither the true 20 SMA (`1.14532`) nor the 50 SMA (`1.15723`). It is not merely
   reading at the crosshair — it is returning an incomplete and incorrect study set. **Do not use it.**

2. **Replacement:** indicators were computed via `ui_evaluate`, reading the chart model's own bar array
   (`mainSeries().bars()`) and computing SMA/RSI in-page with Wilder smoothing. This was **validated
   against an independent Python calculation** on EUR/USD Daily — SMA20, SMA50 and RSI(14) matched to
   five decimal places, and the newest daily swing high (`1.14730`) matched too.

3. **`chart_set_symbol` returns `chart_ready: false` on every switch** (Bug 1), but **bar data does
   follow the model.** Verified: after switching to GBPUSD, `data_get_ohlcv` immediately returned
   1.33–1.34 range bars. Only the visual render and the study values are stale. Every read below
   carries its own `ticker` field and was checked against the intended symbol.

4. **Weekly bars were resampled from 300 daily bars** (Monday-anchored, 604800s buckets) rather than
   fetched separately. Validated exactly against real Weekly bars for EUR/USD: last close `1.14376`,
   SMA20 `1.16112`, SMA50 `1.16574`, both slopes DOWN — identical.

5. **The forming bar is excluded from every reading.** Swing pivots require two bars of confirmation, so
   the most recent swing may not yet appear (e.g. EUR/USD's 1.13912 low of 08 Jul).

6. **Mixed feeds.** OANDA (majors, HUF, DKK, PLN, SGD, SEK, NOK, GBPPLN), `FX:` (MXN, CNH),
   `FX_IDC:` (INR, CNY, BRL, BRLJPY, GBPINR), `FOREXCOM:` (ILS, CNHJPY). **`FX_IDC` is an indicative
   rate, not a dealable price** — treat those levels as directional only.

---

## Phase 1 — Currency Strength Rankings

Scanned: 18/18 USD pairs, plus USD/CNH as an extra (the flagged non-EUR candidate).

```
🟢 Bullish (+1/+2):        BRL (+2), GBP (+1), CNY (+1), [CNH (+1)]
🟡 Neutral (0):            HUF, ILS
🔴 Bearish (−1/−2):        AUD (−1), NZD (−1), CHF (−1), CAD (−1), NOK (−1),
                           SEK (−2), SGD (−2), MXN (−2)
🔴 Strong Bearish (−3/−4): EUR (−3), INR (−3), DKK (−3), JPY (−4), PLN (−4)
```

**Read this as a USD chart, not a basket.** Fifteen of eighteen currencies score negative against the
dollar. This is the compressed-spread condition the skill warns about: the signal is *USD strength*, and
the "bullish" legs (BRL +2, GBP +1, CNH +1) are weak residuals, not genuine strength.

**Sanity check passed:** DKK scored −3, matching EUR's −3. DKK is pegged to EUR, so the two must agree.
They do. That is independent confirmation the scoring and inversion logic are working.

**Note on NZD.** The RBNZ hiked on 8 July and NZD is the #3 fundamental currency — yet NZD/USD scores
**−1 (Bearish)**. Rising rates have not yet reached the chart. Same divergence that killed EUR/NZD this
morning.

---

## Phase 2–4 — Candidates, Liquidity Gate, Cross Confirmation

Top 3 bullish: **BRL (+2), GBP (+1), CNH/CNY (+1)**
Bottom 3 bearish: **JPY (−4), PLN (−4), INR (−3)**

> EUR (−3) and DKK (−3) were excluded from the short group by your constraint (no more EUR expressions)
> and by the skill's rule that DKK is a EUR proxy, not an independent signal.

| # | Pair | Dir | Weekly | Daily | Daily RSI | Conviction | Outcome |
|---|---|---|---|---|---|---|---|
| 1 | **CNH/JPY** | LONG | 🟢 clean HH/HL | 🟢 20>50, both up | 61.3 rising | ★★★ | ❌ **fundamental gate** |
| 2 | **GBP/JPY** | LONG | 🟢 | 🟢 | 66.8 rising | ★★★ | ❌ **fundamental gate** + extended |
| 3 | **GBP/INR** | LONG | 🟢 | 🟡 falling swing highs | 59.2 rising | ★★ | ❌ **fundamental gate** |
| 4 | **BRL/JPY** | LONG | 🟢 weak (falling W highs) | 🟡 20<50, 50 down | 53.3 | ★★ | ❌ **fundamental gate** |
| 5 | **GBP/PLN** | LONG | 🟢 | 🟢 | **84.3** ⚠️ | ★ | ❌ overbought + gate |
| — | CNH/PLN | — | — | — | — | — | ❌ no TradingView data |
| — | BRL/PLN | — | — | — | — | — | ❌ no TradingView data |
| — | CNH/INR, BRL/INR | — | — | — | — | — | ❌ eliminated: both legs thin/managed, `FX_IDC` indicative only |

**Concentration warning.** Four of the five survivors (CNH/JPY, GBP/JPY, BRL/JPY, and by extension any
XXX/JPY) are the **same trade in different costumes** — short JPY. GBP appears in three of five. This is
structurally identical to the W28 short-SEK book: three tickets, one risk. Even if the gate allowed it,
you would take **one**.

---

## The Fundamental Gate — why every candidate dies

From `fundamental-analysis/2026-W28.md`:

> **Valid long legs:** USD, JPY, NZD, SGD, INR, NOK ⚖️, BRL ⚖️
> **Valid short legs:** EUR, CNY ⚖️, ILS ⚠️, HUF ⚖️
> **Blocked (Conflicted):** SEK, AUD, CHF, CAD, **GBP**, MXN, **PLN**, DKK

| Pair | Long leg | Short leg | Verdict |
|---|---|---|---|
| CNH/JPY long | CNY = 🔴 Mild Bearish → **not a valid long** | JPY = 🟢 Bullish → **cannot short** | ❌ both legs fail |
| GBP/JPY long | GBP = 🟡 Conflicted → **blocked** | JPY = 🟢 Bullish → **cannot short** | ❌ both legs fail |
| GBP/INR long | GBP = **blocked** | INR = 🟢 valid *long* leg → **cannot short** | ❌ both legs fail |
| BRL/JPY long | BRL ⚖️ = valid long ✅ | JPY = 🟢 Bullish → **cannot short** | ❌ short leg fails |
| GBP/PLN long | GBP = **blocked** | PLN = 🟡 Conflicted → **blocked** | ❌ both legs fail |
| *USD/JPY long* | USD = valid long ✅ | JPY = 🟢 Bullish → **cannot short** | ❌ short leg fails |

**USD/JPY deserves a note.** It is by some distance the cleanest chart in the basket — Weekly and Daily
both textbook bullish (HH/HL on both, 20>50 rising on both, price above), Daily RSI 66.1 rising, deepest
liquidity in FX. It is the purest expression of the one real signal here. **And it is exactly the trade
your fundamental scorecard forbids**, because the BoJ is the only G8 central bank with a mapped path to a
higher neutral rate. Chart says short JPY; policy says long JPY. That is not a trade, that is a coin flip
with a stop.

---

## The other side: fundamentally valid, technically dead

Only three non-EUR pairs have **both legs passing** the fundamental gate. All three fail on the Weekly.

| Pair | Fundamental | Weekly | Daily | Why blocked |
|---|---|---|---|---|
| **USD/CNH** long | USD ✅ / CNY ⚖️ ✅ | 🔴 **Bearish** — LH/LL, 20<50 both falling, price below | 🟡 20<50, 50 falling, price above rising 20 SMA | Weekly opposes the long |
| **USD/HUF** long | USD ✅ / HUF ⚖️ ✅ | 🔴 Bearish — price 308.97 vs SMA20 317.42 / SMA50 326.17, both falling | 🟢 Strong — 315.17, 20>50 both up, RSI 62.1 rising | Weekly opposes the long |
| **USD/ILS** long | USD ✅ / ILS ⚠️ ✅ | 🔴 Bearish — 20<50 both falling, price below | 🟢 Strong — HH/HL, 20>50 both up, RSI 68.4 rising | Weekly opposes the long |

Per `fx-technical-analysis`: *"Never take a 4H trade that contradicts the Weekly channel."* Here the
**Daily** contradicts the Weekly, which is worse.

**USD/CNH specifically: drop it.** It was carried as the ⭐⭐ non-EUR candidate on fundamentals alone. Its
Weekly is in a clean bearish channel — falling swing highs (6.94362 → 6.92689 → 6.84921) *and* falling
swing lows (6.82662 → 6.80586 → 6.75373), price below both falling SMAs. CNH is **strengthening** against
the dollar. The chart says the opposite of the thesis.

---

## What is actually forming (watch, do not trade)

The three tables above describe one phenomenon: **USD strength is appearing on the Daily against the
managed and emerging currencies — HUF, ILS, CNH, PLN, INR — while their Weeklies still carry the old USD
downtrend.**

That is what an early weekly trend reversal looks like. It is *not yet* a trade — the Weekly has not
turned, and by definition you cannot know it will. But if USD/HUF or USD/ILS puts in a Weekly close back
above its falling 20 SMA, the fundamental gate is already open on both and the setup becomes real.

**This is the thing to watch next week**, and it is uncorrelated with anything EUR.

---

## Macro Event Gate

| Date | Days out | Event | Affects |
|---|---|---|---|
| **14 Jul** | **5** | US CPI (June) — 08:30 ET | **USD — i.e. every pair above** |
| 15 Jul | 6 | Bank of Canada + MPR | CAD |
| 23 Jul | 14 | ECB decision | EUR |
| 28–29 Jul | 19–20 | FOMC | USD |

✅ Nothing inside 72h. But the **11 July line applies to every USD pair on this board**, not just EUR/USD:
anything triggering on or after Saturday sits inside the 24–72h CPI window (halve size, widen SL 10 pips).

⚠️ **No BoJ meeting date was verified for this scan.** Before any JPY-leg trade — should the gate ever
open — confirm the next BoJ decision. The W28 fundamental sources cite the 16 June decision; the next one
is not recorded in this repo.

---

## Recommendation

**Nothing to trade. This is a valid and, this week, the correct output.**

1. **The basket has one real signal — USD strength — and you cannot trade it.** Every clean USD-long
   chart shorts a currency the fundamentals rate bullish (JPY, INR, SGD, NOK) or blocked (PLN, SEK, CAD,
   CHF, MXN, DKK). The three that pass fundamentally (CNH, HUF, ILS) have bearish Weeklies.
2. **Do not take a short-JPY trade this week.** JPY is the weakest chart and the second-strongest
   fundamental. That is a disagreement, not an edge. Four of five screener survivors were short-JPY;
   treat the count as a warning, not a confirmation.
3. **Drop USD/CNH from the candidate list.** Its Weekly opposes the thesis outright.
4. **EUR/USD remains the only fundamentally unambiguous short** — and it is Stage A and decaying (4H
   turned up, no valid pattern). See the re-run. It is still the best of a bad board.
5. **Watch USD/HUF and USD/ILS for a Weekly turn.** Both legs already pass the fundamental gate. Neither
   is a EUR expression. Neither is tradeable today.
6. **Zero open trades is the right position** when the two screens disagree this completely.

---

*Analysis only. No position sizing or leverage recommendations. FX trading carries significant risk of loss.*
*Source: TradingView MCP, retrieved 2026-07-09 ~15:40 UTC. Indicators computed from chart-model bars via
`ui_evaluate` (Wilder smoothing), validated against independent Python calculation; forming bar excluded.
`FX_IDC` quotes are indicative, not dealable.*
