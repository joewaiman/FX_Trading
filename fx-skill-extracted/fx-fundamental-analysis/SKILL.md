---
name: fx-fundamental-analysis
description: >
  Use this skill whenever the user wants to analyse currency pairs or identify FX trading opportunities
  based on economic fundamentals. Triggers include: requests to screen currencies, analyse economic data
  for a country, find long or short FX setups, assess macro conditions, compare currency strength,
  or evaluate whether a currency is bullish/bearish based on fundamentals. Also use when the user
  asks about inflation, interest rates, unemployment, GDP, PMI, retail sales, or trade balance in the
  context of FX or forex trading. This is Step 1 of the FX Strategy workflow — fundamental screening
  before technical analysis.
---

# FX Fundamental Analysis Skill

This skill systematically evaluates currencies using 7 core economic indicators to identify
**long candidates** (strong fundamentals) and **short candidates** (weak fundamentals) for FX trading.

---

## Workflow Overview

```
1. Select currencies to analyse
2. Gather all 7 indicators per currency
3. Score each indicator (Bullish / Neutral / Bearish)
4. Aggregate into an overall fundamental bias
5. Output a ranked watchlist with commentary
```

---

## Step 1 — Currency Universe

Default universe (majors + liquid crosses):
`USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF`

The user may expand to include: `NOK, SEK, SGD, HKD, CNH, MXN, ZAR, TRY`

---

## Step 2 — The 7 Indicators

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

### iii. GDP Growth
| Metric | Threshold |
|---|---|
| QoQ annualised | >2% Bullish / 0–2% Neutral / <0% Bearish |
| YoY | Positive trend = Bullish; declining trend = Bearish |

Note: Two consecutive negative QoQ prints = technical recession → strong Bearish signal.

### iv. PMI — Manufacturing & Services (two numbers)
Use the **S&P Global / Markit** PMI series (or ISM for USD).

| Level | Signal |
|---|---|
| >52 | 🟢 Expansion (Bullish) |
| 50–52 | 🟡 Marginal expansion (Neutral) |
| 48–50 | 🟡 Marginal contraction (Neutral) |
| <48 | 🔴 Contraction (Bearish) |

Score Manufacturing and Services separately. If they diverge significantly (e.g. Services strong / Manufacturing weak), note in commentary.

### v. Retail Sales
| Monthly MoM change | Signal |
|---|---|
| >+0.5% | 🟢 Bullish |
| 0 to +0.5% | 🟡 Neutral |
| Negative | 🔴 Bearish |

Also note the YoY trend and whether the latest print beat or missed consensus.

### vi. Balance of Trade
| Condition | Signal |
|---|---|
| Surplus and growing | 🟢 Bullish (net demand for currency) |
| Surplus but shrinking | 🟡 Neutral |
| Deficit and narrowing | 🟡 Neutral |
| Deficit and widening | 🔴 Bearish (net selling pressure on currency) |

Note: For commodity-linked currencies (AUD, NZD, CAD, NOK), cross-reference terms of trade.

### vii. Trading Economics Commentary
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
│ GDP Growth              │ 🟢/🟡/🔴 │ QoQ x.x%, YoY x.x%          │
│ PMI Manufacturing       │ 🟢/🟡/🔴 │ xx.x                         │
│ PMI Services            │ 🟢/🟡/🔴 │ xx.x                         │
│ Retail Sales            │ 🟢/🟡/🔴 │ MoM +x.x%, YoY x.x%         │
│ Trade Balance           │ 🟢/🟡/🔴 │ $xB surplus/deficit          │
│ TE Commentary           │ 🟢/🟡/🔴 │ Summary sentence             │
├─────────────────────────┼─────────┼──────────────────────────────┤
│ OVERALL BIAS            │ BULL/BEAR/NEUTRAL │ X/8 bullish        │
└─────────────────────────┴─────────┴──────────────────────────────┘
```

### Multi-currency Comparison Table

When analysing a basket of currencies, present a single comparison table with the following column order:

```
│ Currency │ Rate (%) │ Inflation (%) │ CPI vs Target │ Rate Bias │ Unemployment │ GDP ann. │ Mfg PMI │ Svcs PMI │ Retail MoM │ Trade Balance │ Score │
```

- **Rate (%)**: Current central bank policy rate
- **Inflation (%)**: Latest CPI YoY % (raw figure, not scored)
- **CPI vs Target**: 🟢/🟡/🔴 scored against the central bank's inflation target
- Remaining columns scored as per indicators above

The Inflation (%) column is a raw data column — it provides the actual figure so the CPI vs Target score can be read in context.

**Aggregate scoring:**
- 6–8 🟢 = **Strong Bullish** → Long candidate
- 4–5 🟢 = **Mild Bullish** → Tentative long
- Mix of 🟢🔴 = **Conflicted** → Neutral / avoid
- 4–5 🔴 = **Mild Bearish** → Tentative short
- 6–8 🔴 = **Strong Bearish** → Short candidate

---

## Step 4 — Pair Construction

Once you have biases for all analysed currencies, construct pairs:

**Best long/short combinations:**
```
Strong Bullish vs Strong Bearish = Highest conviction pair
Strong Bullish vs Mild Bearish   = Medium conviction
Mild Bullish   vs Strong Bearish = Medium conviction
```

Present the top 3–5 pairs ranked by conviction differential.

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
