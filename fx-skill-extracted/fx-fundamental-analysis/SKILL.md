---
name: fx-fundamental-analysis
description: >
  Use this skill whenever the user wants to analyse currency pairs or identify FX trading opportunities
  based on economic fundamentals. Triggers include: requests to screen currencies, analyse economic data
  for a country, find long or short FX setups, assess macro conditions, compare currency strength,
  or evaluate whether a currency is bullish/bearish based on fundamentals. Also use when the user
  asks about inflation, interest rates, unemployment, GDP, PMI, retail sales, or trade balance in the
  context of FX or forex trading. This is Step 1 of the FX Strategy workflow — fundamental screening
  before technical analysis. Use proactively whenever the user mentions a currency, country economy,
  central bank decision, or asks which FX pairs look interesting — even if they don't explicitly ask
  for "fundamental analysis".
---

# FX Fundamental Analysis Skill

This skill systematically evaluates currencies using 8 core economic indicators to identify
**long candidates** (strong fundamentals) and **short candidates** (weak fundamentals) for FX trading.

---

## Workflow Overview

```
1. Select currencies to analyse
2. Gather all 8 indicators per currency
3. Score each indicator (Bullish / Neutral / Bearish)
4. Aggregate into an overall fundamental bias
5. Output a ranked watchlist with commentary
```

---

## Step 1 — Currency Universe

Default universe — always analyse all of these unless the user specifies otherwise.

**Tier 1 — G8 Majors (always scored fully):**
`USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF`

**Tier 2 — EM & Commodity Currencies (best-effort):**
`NOK, SEK, SGD, PLN, HUF, DKK, MXN, INR, CNY, BRL, ILS`

Tier 2 currencies are scored on the same 10-point framework wherever data is available.
If fewer than 4 indicators can be sourced, flag the currency as ⚠️ Data-limited and note
which indicators are missing. Always include Tier 2 in the output — never omit a currency
due to missing data. A partial score is better than no score.

**Important:** Gather data for **all currencies in the universe first** before proceeding to
scoring or analysis. Do not score or rank mid-collection. Complete Step 2 fully across all
currencies, then move to Step 3.

---

## Inflation Targets Reference (verify monthly — targets can change)

| Currency | Central Bank | Inflation Target | Measure | Notes |
|---|---|---|---|---|
| USD | Federal Reserve | 2.0% | PCE (primary) / CPI | |
| EUR | European Central Bank | 2.0% | HICP | |
| GBP | Bank of England | 2.0% | CPI | |
| JPY | Bank of Japan | 2.0% | CPI | |
| AUD | Reserve Bank of Australia | 2.0–3.0% (mid 2.5%) | CPI | Band target |
| NZD | Reserve Bank of New Zealand | 1.0–3.0% (mid 2.0%) | CPI | Band target |
| CAD | Bank of Canada | 2.0% (1–3% control range) | CPI | |
| CHF | Swiss National Bank | 0–2% (price stability) | CPI | Avoids negative rates |
| SEK | Riksbank (Sweden) | 2.0% | CPIF | CPIF = CPI with fixed mortgage rate |
| NOK | Norges Bank (Norway) | 2.0% | CPI-ATE (core) | Oil-linked economy |
| SGD | MAS (Singapore) | ~2% implicit | CPI | ⚠️ Uses S$NEER slope — see EM notes |
| PLN | National Bank of Poland | 2.5% (±1% = 1.5–3.5%) | CPI | Band target |
| HUF | National Bank of Hungary | 3.0% (±1% = 2–4%) | CPI | Band target |
| DKK | Danmarks Nationalbank | n/a (EUR peg) | Mirrors ECB | ⚠️ ERM II peg — see EM notes |
| MXN | Banco de Mexico (Banxico) | 3.0% (±1% = 2–4%) | CPI | Band target |
| INR | Reserve Bank of India | 4.0% (±2% = 2–6%) | CPI | Wide band target |
| CNY | People's Bank of China | ~3% (informal) | CPI | ⚠️ Managed currency — see EM notes |
| BRL | Banco Central do Brasil | 3.0% (±1.5% = 1.5–4.5%) | IPCA | Band target |
| ILS | Bank of Israel | 1.0–3.0% (mid 2.0%) | CPI | Band target |

> **Band target scoring rule**: Score 🟢 if CPI is above the upper bound, 🟡 if within the band, 🔴 if below the lower bound.

---

## Step 2 — The 8 Indicators

### Data Collection Protocol

Fetch all currencies **in parallel** — do not wait for one to complete before starting the next.
For each currency, follow this sequence:

**1. Primary fetch (covers most indicators in one call):**
```
web_fetch → https://tradingeconomics.com/{country}/indicators
```
This single page returns CPI, rate, unemployment, GDP, PMI, retail sales, and trade balance
for the country. Extract all available values before making additional calls.

**2. Targeted web search (only if a value is missing or looks stale):**
```
web_search → "{country} {indicator} latest {current year}"
```
Use the query templates in `references/data-sources.md`.

**3. Rate bias confirmation (always run this):**
```
web_search → "{central bank name} rate decision outlook {current year}"
```
This captures the forward guidance signal (hike / hold / cut) which is not always on the
indicators page.

Batching note — for 19 currencies, launch all 19 `web_fetch` calls in one batch, then
follow up with targeted searches only where needed. If context limits apply, prioritise
Tier 1 (8 majors) as batch 1, then Tier 2 (11 EM/commodity) as batch 2.

**4. Weekly FX performance vs USD (run once, covers all 19 currencies):**
```
web_fetch → https://tradingeconomics.com/currencies
```
This page shows weekly % change for all major currency pairs vs USD. Extract the 7-day
% change for each of the 19 basket currencies. If a currency is not listed (some EM pairs),
use a targeted search:
```
web_search → "{currency}/USD weekly performance {current date}"
```
Record each value as a signed % (e.g. +1.2% or −0.8%). Run this fetch **once** alongside
the 19 indicator fetches — do not re-fetch per currency. Store all 19 values before
proceeding to Step 3.

---

For each currency, gather the following. Source priority: **Trading Economics** → central bank publications → Bloomberg/Reuters.

### i. Inflation & Interest Rates
| Data point | Where to find |
|---|---|
| CPI (actual YoY %) | Trading Economics / national stats |
| Central bank target (%) | Central bank website |
| Policy rate (current %) | Trading Economics |
| Market-implied next move | Futures pricing / central bank guidance |

**Scoring:**
- 🟢 Bullish: Inflation above target AND rate hikes expected (or hiking cycle ongoing)
- 🔴 Bearish: Inflation below target AND rate cuts expected (or cutting cycle ongoing)
- 🟡 Neutral: Inflation at/near target, rates on hold

### ii. Unemployment Rate
Target band: **3.5% – 4.5%**

**Scoring:**
- 🟢 Bullish: Rate within 3.5–4.5% (tight labour market, supports consumption)
- 🟡 Neutral: Rate 4.5–5.5% (softening but not alarming)
- 🔴 Bearish: Rate above 5.5% (slack) OR trending sharply higher MoM
- ⚠️ Also flag: Rate below 3.5% (overheating risk, may force aggressive hikes)

### iii. Wages / Average Hourly Earnings
| Data point | Where to find |
|---|---|
| Wage growth (YoY %) | Trading Economics / national stats / NFP report (USD) |
| Real wage growth (wage growth minus CPI) | Calculate from above |

Wage growth is a leading indicator for future inflation and consumer spending. Central banks watch it closely for second-round inflation effects.

**Scoring:**
- 🟢 Bullish: Wage growth accelerating OR real wages positive (wage growth > CPI) — supports consumption, signals labour market strength
- 🟡 Neutral: Wage growth stable and roughly in line with inflation
- 🔴 Bearish: Wage growth decelerating OR real wages negative (wage growth < CPI) — consumer squeeze, headwind for spending

**EM note:** Wages data is often unavailable or infrequent for Tier 2 currencies. If unavailable, mark as ⚠️ Data-limited and skip this row — do not guess.

**Key series by currency:**
| Currency | Series |
|---|---|
| USD | Average Hourly Earnings (NFP report, monthly) |
| EUR | Negotiated Wages (ECB, quarterly) |
| GBP | Average Weekly Earnings (ONS, monthly) |
| JPY | Labour Cash Earnings (monthly) |
| AUD | Wage Price Index (quarterly) |
| CAD | Average Hourly Wages (monthly) |
| Others | Trading Economics → {country}/wages |

### iv. GDP Growth
| Metric | Threshold |
|---|---|
| QoQ annualised | >2% Bullish / 0–2% Neutral / <0% Bearish |
| YoY | Positive trend = Bullish; declining trend = Bearish |

Note: Two consecutive negative QoQ prints = technical recession → strong Bearish signal.

### v. PMI — Manufacturing & Services (two numbers)
Use the **S&P Global / Markit** PMI series (or ISM for USD).

| Level | Signal |
|---|---|
| >52 | 🟢 Expansion (Bullish) |
| 50–52 | 🟡 Marginal expansion (Neutral) |
| 48–50 | 🟡 Marginal contraction (Neutral) |
| <48 | 🔴 Contraction (Bearish) |

Score Manufacturing and Services separately. If they diverge significantly (e.g. Services strong / Manufacturing weak), note in commentary.

### vi. Retail Sales
| Monthly MoM change | Signal |
|---|---|
| >+0.5% | 🟢 Bullish |
| 0 to +0.5% | 🟡 Neutral |
| Negative | 🔴 Bearish |

Also note the YoY trend and whether the latest print beat or missed consensus.

### vii. Balance of Trade
| Condition | Signal |
|---|---|
| Surplus and growing | 🟢 Bullish (net demand for currency) |
| Surplus but shrinking | 🟡 Neutral |
| Deficit and narrowing | 🟡 Neutral |
| Deficit and widening | 🔴 Bearish (net selling pressure on currency) |

Note: For commodity-linked currencies (AUD, NZD, CAD, NOK, BRL, MXN), cross-reference terms of trade. NOK/BRL/MXN are particularly sensitive to oil prices; AUD/NZD/BRL to iron ore and agricultural commodities.

### viii. Trading Economics Commentary
Fetch the country page from tradingeconomics.com (e.g. `tradingeconomics.com/united-states/indicators`).

Extract:
- Analyst outlook / forecasts
- Any recent rating changes or revisions
- Notable upcoming events or risks flagged
- Central bank forward guidance summary

Use `web_fetch` with the Trading Economics country URL. Key pages:
```
https://tradingeconomics.com/{country}/indicators
https://tradingeconomics.com/{country}/interest-rate
https://tradingeconomics.com/{country}/inflation-cpi
```

---

## EM Currency Special Considerations

The 11 non-G8 currencies require modified scoring rules in some areas.

### Unemployment Benchmarks (EM-adjusted)

The 3.5–4.5% "healthy" band is calibrated for G10 economies. Use these adjusted thresholds:

| Currency | Typical Range | Healthy (Neutral) Band | Bullish | Bearish |
|---|---|---|---|---|
| SEK | 7–10% | 7–8.5% | <7% | >10% |
| NOK | 3–5% | 3–4.5% (use G10 band) | <3.5% | >5.5% |
| SGD | 2–3.5% | 2–3% | <2%⚠️ overheating | >3.5% |
| PLN | 3–6% | 4–6% | <4% | >7% |
| HUF | 3–6% | 4–6% | <4% | >7% |
| DKK | 4–7% | 4–6% | <4% | >7% |
| MXN | 3–5% | 3.5–5% | <3.5% | >5.5% |
| INR | 4–8% | 4–6% (survey data infrequent) | <4% | >8% |
| CNY | 5–6% (official) | 5–6% | — | >6% |
| BRL | 6–14% | 8–10% | <8% | >12% |
| ILS | 3–5% | 3.5–5% | <3.5% | >5.5% |

### SGD — Exchange Rate Policy (Not Interest Rate Policy)

The MAS uses the **S$NEER slope** as its only policy tool — not a policy rate. Standard rate
bias scoring is replaced with:
- 🟢 Bullish: MAS steepened the S$NEER slope or re-centred upward (tightening)
- 🟡 Neutral: MAS held slope and width unchanged
- 🔴 Bearish: MAS flattened or eased the slope (loosening)

Search query: `"MAS monetary policy statement {year} S$NEER slope"`

### DKK — EUR Peg (ERM II Band ±2.25%)

DKK is pegged to EUR. **Score DKK identically to EUR** — no independent analysis needed.
Flag in output: *"DKK mirrors EUR (ERM II peg — independent scoring not applicable)."*

### CNY — Managed / Partially Convertible Currency

The PBOC sets a daily fixing rate with a ±2% intraday band. Fundamentals are less
predictive of CNY moves than for free-floating currencies. Score as normal but add flag:
*"CNY: PBOC-managed — policy discretion may override fundamental signals."*

### Pair Construction — Liquidity Constraints

When building pairs from the full 19-currency universe:
- **Prefer EM vs USD or EUR** for adequate liquidity (spreads, hedging)
- **Avoid EM-vs-EM crosses** — spreads are wide (e.g. BRL/MXN, INR/HUF are illiquid)
- **Liquid EM FX pairs**: USD/MXN, USD/BRL, USD/INR (NDF), USD/CNH, EUR/PLN, EUR/HUF, USD/ILS, USD/SGD
- **Semi-liquid DM crosses**: EUR/NOK, EUR/SEK, NOK/SEK, USD/NOK, USD/SEK
- DKK pairs: EUR/DKK has minimal range due to the peg — skip unless flagging peg stress

Flag any low-liquidity pair recommendations in the output.

---

## Step 3 — Scoring Matrix

After gathering all indicators, score each one and produce a table:

```
Currency: [XXX]
┌─────────────────────────┬─────────┬──────────────────────────────┐
│ Indicator               │ Score   │ Key Data                     │
├─────────────────────────┼─────────┼──────────────────────────────┤
│ Inflation vs Target     │ 🟢/🟡/🔴 │ CPI x.x% vs target x.x%     │
│ Interest Rate Bias      │ 🟢/🟡/🔴 │ Rate x.xx%, next move: hike  │
│ Unemployment            │ 🟢/🟡/🔴 │ x.x%, trend: ↑/↓/→          │
│ Wages                   │ 🟢/🟡/🔴 │ YoY x.x%, real: +/-x.x%     │
│ GDP Growth              │ 🟢/🟡/🔴 │ QoQ x.x%, YoY x.x%          │
│ PMI Manufacturing       │ 🟢/🟡/🔴 │ xx.x                         │
│ PMI Services            │ 🟢/🟡/🔴 │ xx.x                         │
│ Retail Sales            │ 🟢/🟡/🔴 │ MoM +x.x%, YoY x.x%         │
│ Trade Balance           │ 🟢/🟡/🔴 │ $xB surplus/deficit          │
│ TE Commentary           │ 🟢/🟡/🔴 │ Summary sentence             │
├─────────────────────────┼─────────┼──────────────────────────────┤
│ OVERALL BIAS            │ BULL/BEAR/NEUTRAL │ X/10 bullish       │
└─────────────────────────┴─────────┴──────────────────────────────┘
```

### Multi-currency Comparison Table

When analysing a basket of currencies, present a single comparison table with the following column order:

```
│ Currency │ Rate (%) │ Inflation (%) │ CPI vs Target │ Rate Bias │ Unemployment │ Wages YoY │ GDP ann. │ Mfg PMI │ Svcs PMI │ Retail MoM │ Trade Balance │ Score │
```

- **Rate (%)**: Current central bank policy rate
- **Inflation (%)**: Latest CPI YoY % (raw figure, not scored)
- **CPI vs Target**: 🟢/🟡/🔴 scored against the central bank's inflation target
- Remaining columns scored as per indicators above

The Inflation (%) column is a raw data column — it provides the actual figure so the CPI vs Target score can be read in context.

**Aggregate scoring — net score N = (🟢 count) − (🔴 count) across the 10 indicators:**
- **N ≥ +5** = **Strong Bullish** → Long candidate
- **N +2 to +4** = **Mild Bullish** → Tentative long
- **N −1 to +1** = **Conflicted** → Neutral / avoid (do not trade either leg)
- **N −2 to −4** = **Mild Bearish** → Tentative short
- **N ≤ −5** = **Strong Bearish** → Short candidate

Direction comes from the **sign** of N (matches the entry gate in `CLAUDE.md`); Strong vs Mild from its **magnitude**. Yellows count as neither — they widen the Conflicted band, which is correct: a currency scoring mostly 🟡 has no clear thesis. Note N uses the net, so a 5🟢/5🔴 currency is **Conflicted (N=0)**, not Bullish — the green count alone is never the classifier.

---

## Step 4 — Pair Construction

Once you have biases for all analysed currencies, construct all valid pairs.

**Entry eligibility rule — applies before building the pair list:**

A currency is only eligible as a trade candidate if its score is **clearly directional**:

| Score | Long eligible? | Short eligible? |
|---|---|---|
| Strong Bullish (N ≥ +5) | ✅ Yes | ❌ No |
| Mild Bullish (N +2 to +4) | ✅ Yes | ❌ No |
| Conflicted (N −1 to +1, incl. mostly 🟡) | ❌ No — exclude from pairs | ❌ No — exclude from pairs |
| Mild Bearish (N −2 to −4) | ❌ No | ✅ Yes |
| Strong Bearish (N ≤ −5) | ❌ No | ✅ Yes |

**Conflicted currencies must be excluded from all pair recommendations.** A Conflicted score means the data is sending mixed signals — the thesis has not resolved clearly enough to support a trade. Flag Conflicted currencies in the output as "watch — not yet tradeable."

**Long/short combinations — using only eligible currencies:**
```
Strong Bullish vs Strong Bearish = Highest conviction pair
Strong Bullish vs Mild Bearish   = Medium conviction
Mild Bullish   vs Strong Bearish = Medium conviction
Mild Bullish   vs Mild Bearish   = Lower conviction — flag as such
```

**Thesis deterioration flag:** For any pair currently in a live trade, explicitly compare this week's score against last week's. If the short leg's score is moving toward Conflicted (gap narrowing), flag it as ⚠️ Thesis deteriorating and recommend reassessing the position.

Present **all** valid pairs ranked by conviction differential.
Group by conviction tier (High / Medium / Low) for readability.

---

## Step 5 — Output Format

### Summary Watchlist Table
```
┌──────────┬──────────────────┬───────────────────────────────────────────┐
│ Currency │ Fundamental Bias │ Key Drivers                               │
├──────────┼──────────────────┼───────────────────────────────────────────┤
│ USD      │ 🟢 Strong Bull   │ Rates 5.25%, CPI above target, low unemp │
│ EUR      │ 🔴 Mild Bear     │ PMI in contraction, GDP stalling          │
│ GBP      │ 🟡 Neutral       │ Mixed signals, services PMI resilient     │
│ ...      │ ...              │ ...                                       │
└──────────┴──────────────────┴───────────────────────────────────────────┘
```

### Weekly Performance vs USD

Immediately after the Summary Watchlist Table, present this ranked performance table.
Sort by weekly % change descending (strongest to weakest). USD is the baseline (0.0%).

```
┌──────────┬─────────────────┬──────┐
│ Currency │ Weekly % vs USD │ Rank │
├──────────┼─────────────────┼──────┤
│ AUD      │ +1.8%           │  1   │
│ NZD      │ +1.3%           │  2   │
│ EUR      │ +1.2%           │  3   │
│ GBP      │ +0.4%           │  4   │
│ USD      │  0.0%           │  —   │
│ JPY      │ −0.3%           │ 12   │
│ ...      │ ...             │ ...  │
└──────────┴─────────────────┴──────┘
```

### Top Pairs
```
1. SHORT EUR/USD — Strong USD bull vs Mild EUR bear (conviction: HIGH)
2. LONG USD/JPY — USD bull vs JPY bear (BoJ still dovish)
3. ...
```

### Per-Currency Detail
For each currency with a non-neutral bias, provide a 3–5 sentence narrative
summarising the fundamental case. Reference specific data points.

---

## Data Freshness Rules

- Always state the date of each data point used
- Prefer the most recent release (check if more recent data is available via web search)
- Flag if any indicator is >45 days old — data may be stale
- Note scheduled releases that could change the picture (use economic calendar)
- **Tier 2 data gap rule:** If >2 indicators are missing or stale for a Tier 2 currency, mark its score ⚠️ and list the gaps explicitly. Still include the currency in the output.

---

## Tools to Use

| Task | Tool |
|---|---|
| Fetch Trading Economics pages | `web_fetch` |
| Search for latest data releases | `web_search` |
| LSEG / FactSet data (if connected) | MCP tools |
| Present final analysis | Inline tables + narrative |

See `references/data-sources.md` for specific URLs and search query templates.
See `references/central-banks.md` for rate targets and central bank details per currency.

---

## Important Notes

- This skill covers **Step 1: Fundamental Screening only**
- Step 2 (Technical Analysis) follows separately once the fundamental watchlist is built
- Never recommend position sizes or leverage — this is analysis only
- Always note that FX trading carries significant risk
