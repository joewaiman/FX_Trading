# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is an FX trading analysis workspace. It is not a software project — there is no build system, tests, or linting. The primary work here is running analytical skills, generating reports, and maintaining reference data.

---

## Skills

Eight Claude Code skills are registered from this repo:

| Skill | Trigger | File | Extracted source |
|-------|---------|------|-----------------|
| `daily-fx-economist` | Daily economist briefing — overnight releases, scorecard update, trade setups (runs Mon–Fri 06:30 UTC) | `daily-fx-economist.skill` | `daily-fx-economist-extracted/daily-fx-economist/` |
| `fx-fundamental-analysis` | Analyse currencies, screen for FX setups, assess macro fundamentals | `fx-fundamental-analysis.skill` | `fx-skill-extracted/fx-fundamental-analysis/` |
| `weekly-fx-overview` | Generate the weekly FX report (runs every Friday 21:00 UTC) | `weekly-fx-overview.skill` | `weekly-fx-overview-extracted/weekly-fx-overview/` |
| `fx-pair-screener` | Screen all 19 currencies for cross pair trade opportunities — find strongest vs weakest, filter by TradingView liquidity, output a shortlist | `fx-pair-screener.skill` | `fx-pair-screener-extracted/fx-pair-screener/` |
| `fx-technical-analysis` | Top-down multi-timeframe technical analysis on a currency pair | `fx-technical-analysis.skill` | `fx-technical-analysis-extracted/fx-technical-analysis/` |
| `fx-support-resistance` | Map S&R zones, draw channels, identify H&S patterns | `fx-support-resistance.skill` | `fx-support-resistance-extracted/fx-support-resistance/` |
| `fx-candlestick-patterns` | Identify and validate pin bars and engulfing candles as entry triggers (Step 4) | `fx-candlestick-patterns.skill` | `fx-candlestick-patterns-extracted/fx-candlestick-patterns/` |
| `fx-entry-confirmation` | Confirm entry after a TradingView alert fires — zone check, candlestick trigger, full trade setup | `fx-entry-confirmation.skill` | `fx-entry-confirmation-extracted/fx-entry-confirmation/` |

The `.skill` files are zip archives. Edit SKILL.md files in the extracted source directories, then repack if needed.

---

## Full Strategy Workflow

This is the end-to-end pipeline from macro screening to trade execution. Each step uses a dedicated skill.

```
Step 0: Weekly Fundamental Scan   (fx-fundamental-analysis)
         ↓ Identify long/short candidates, score all 19 currencies
Step 1: Pair Selection
         — If no specific pair in mind → run fx-pair-screener (technical cross-pair scan)
         — If pair already known from fundamentals → skip screener, go to Step 2
         ↓
Step 2: Technical Analysis         (fx-technical-analysis)
         Weekly → Daily → 4H channel direction, SMA status, RSI readings, key levels
         ↓
Step 3: S&R Zone Mapping           (fx-support-resistance)
         Channel zones, horizontal S&R, diagonal S&R, H&S patterns
         ↓
Step 4: Entry Confirmation         (fx-entry-confirmation)
         Zone proximity check → candlestick trigger → trade setup (entry/SL/TP/R:R)
         ↓
Step 5: Execution                  (user's own broker)
         Set TradingView alert at entry zone. Re-run Step 4 when alert fires.
```

**When to run the pair screener vs going straight to technicals:**
- Run `fx-pair-screener` when no specific pair has been identified — it scans all 18 non-USD currencies against USD, filters by TradingView data availability, and outputs a ranked shortlist of 3–5 cross pairs.
- Skip the screener when the fundamental scan already produces a high-conviction pair (e.g. Strong Bullish vs Strong Bearish) — go directly to `fx-technical-analysis`.

---

## Workflow Architecture

### Daily FX Economist Briefing (automated daily report)

Covers all 19 currencies. Runs every weekday at 06:30 UTC before London open. Produces a
structured `.md` report with: overnight economic releases (with economist interpretation),
today's economic calendar, 24h FX moves vs USD, per-currency fundamental scorecard update,
and 2–3 top trade setups based on fundamental divergence.

Output destinations:
- **GitHub**: `daily-briefings/YYYY-MM-DD.md` in repo `joewaiman/FX_Trading`
- **Notion**: new row in the Daily FX Economist Briefing database (created on first run),
  parent page ID `344f5490-1aec-819e-87e3-e0efc16e651d`

Reference files:
- `daily-fx-economist-extracted/daily-fx-economist/references/scorecard.md` — per-currency scorecard baseline and scoring criteria
- `daily-fx-economist-extracted/daily-fx-economist/references/notion.md` — Notion database/page IDs and property schema
- `daily-fx-economist-extracted/daily-fx-economist/references/sources.md` — data source URLs and search templates

---

### FX Fundamental Analysis (Step 0 — Weekly scan)

Scores all 19 currencies across 10 indicators — inflation vs target, rate bias, unemployment, wages/average hourly earnings, GDP, manufacturing PMI, services PMI, retail sales, trade balance, and TE commentary — then ranks them long/short and constructs pairs by conviction differential.

- **Tier 1 (G8 majors):** USD, EUR, GBP, JPY, AUD, NZD, CAD, CHF — always scored fully
- **Tier 2 (EM/commodity):** NOK, SEK, SGD, PLN, HUF, DKK, MXN, INR, CNY, BRL, ILS — best-effort

Scoring: 7–9 bullish = Strong Bullish, 5–6 = Mild Bullish, mix = Neutral, 5–6 bearish = Mild Bearish, 7–9 = Strong Bearish.

Data source hierarchy: **Trading Economics** → central bank publications → Bloomberg/Reuters.

Output includes a **Weekly Performance vs USD** table ranked strongest to weakest (7-day % change). Informational only — for context when comparing currencies.

Output saved to: `fundamental-analysis/YYYY-WXX.md`

Reference files:
- `fx-skill-extracted/fx-fundamental-analysis/references/central-banks.md` — per-currency rate targets, meeting cadence, hawkish/dovish language glossary
- `fx-skill-extracted/fx-fundamental-analysis/references/data-sources.md` — Trading Economics URL patterns and web search query templates

---

### FX Pair Screener (Step 1 — optional)

Run when no specific pair has been identified. Scans all 18 non-USD currencies against USD for Weekly + Daily trend alignment, filters out pairs with no TradingView data, then confirms direction on the actual cross pair chart. Outputs a ranked shortlist of 3–5 pairs with conviction ratings (★★★ / ★★ / ★).

Skip this step if the fundamental scan already identifies a clear high-conviction pair.

---

### FX Technical Analysis (Step 2)

Top-down multi-timeframe analysis: Weekly → Daily → 4H.

**What it produces:**
- Channel direction on each timeframe (Bullish / Bearish / Sideways)
- SMA status: 20 SMA and 50 SMA values, slopes, price position relative to both
- Key S&R levels nearest to current price (4–6 levels)
- RSI(14) reading on Daily and 4H — zone classification and divergence check
- Overall bias and alignment summary
- Entry zone, provisional trade setup, R:R calculation

**Blocking conditions before entry:**
- RSI > 70 on 4H in a bearish setup → overbought, wait for reset
- RSI < 30 on 4H in a bullish setup → oversold, wait for reset
- Daily and 4H channels conflicting → reduce conviction or wait
- High-impact macro event ≤ 24h away for either currency in the pair → **block entry entirely**
- High-impact macro event 24–72h away → warn, halve position size, widen SL by 10 pips

Output saved to: `analysis/YYYY-MM-DD-PAIR-technical.md`

---

### S&R Zone Mapping (Step 3)

Maps support and resistance using the body/wick rule: lines may pass through wicks but must never cross candle bodies.

**What it produces:**
- Channel buy/sell zones (body-line to wick-line band)
- Horizontal S&R zones rated 1–3 stars (6-month lookback, Weekly and Daily)
- Diagonal S&R zones where applicable
- Head & Shoulders / Inverse H&S pattern check
- Three primary trade signals: channel boundary, internal S&R bounce, breakout retest
- Confluence note where multiple zones overlap (highest priority areas)

**Key rules:**
- Zones not lines — always a price band, never a single level
- Big swings only — ignore minor retracements when mapping horizontal S&R
- Weekly zones override Daily zones when they conflict
- Wait for a candle body close beyond a zone before calling a breakout

---

### Entry Confirmation (Step 4)

Final gate before execution. Requires the TA output (Step 2) to be in hand first.

**Pre-entry macro check (runs before any other gate):**

Before evaluating zone proximity or candlestick patterns, check the economic calendar for both currencies in the pair. Use Trading Economics or the daily briefing scorecard.

| Time to event | Action |
|---|---|
| ≤ 24h | **Block entry entirely** — no trade, regardless of setup quality |
| 24–72h | **Warn** — flag the event, halve position size, widen SL by 10 pips |
| > 72h | Proceed normally |

**High-impact events that trigger this gate:**
- Central bank rate decisions (ECB, Fed, BoE, RBA, RBNZ, BoC, BoJ, SNB, Riksbank, MAS)
- CPI / inflation releases
- Non-farm payrolls / employment reports
- GDP flash estimates
- Any event the daily briefing flags as market-moving

**Output the calendar check** as the first item in any Stage A / B / C entry confirmation output.

---

**Three-stage output:**

| Stage | Condition | Action |
|-------|-----------|--------|
| A — Waiting | Price > 20 pips from zone | Note distance, tell user when to re-run |
| B — At zone, no trigger | Price ≤ 20 pips from zone, no pattern yet | Monitor next 4H candle close |
| C — Trigger confirmed | Price at zone + candlestick pattern + confluence ≥ 3/5 | Full trade setup issued |

**Candlestick patterns checked (4H):**
- **Pin bar** — rejection wick ≥ 2× body, opposite wick ≤ 25% of body, within prior candle's range
- **Engulfing** — C2 fully engulfs C1 body in the bias direction
- **Inside bar** — C2 range within C1 range; trade the bias-direction breakout

**Confluence score (6 factors):**
1. Price at mapped S&R level (≤ 20 pips)
2. RSI aligned with bias
3. Candlestick pattern present
4. Daily + 4H channels aligned
5. No conflicting divergence
6. No high-impact event within 24h for either currency

Pattern grades: A (all criteria met, strong ratios) / B (all criteria met, borderline) / C (mandatory criteria only, marginal quality).

---

### Position Limits & Trading Discipline

- **Maximum open trades: 4.** If already at 4, do not present new setups — explicitly state the limit is reached and which existing trades to watch instead.
- **Screener output is a shortlist, not a trade list.** Present the top 3 candidates and let the user choose. Never recommend taking all of them.
- **Grade C patterns are not recommendations.** Flag them as marginal and default to "wait for a better setup" unless the user explicitly asks to proceed.
- **"Nothing to trade" is always a valid output.** When no setup meets the criteria, say so clearly. Do not manufacture setups or lower the bar to fill the analysis.
- **Don't re-run entry confirmation repeatedly on the same pair.** If Stage A or B is returned, give the watch level and wait — do not keep checking until a trigger appears.

**Fundamental score thresholds for entry:**

A trade should only be entered when **both legs have a clear directional score**:

| Leg | Minimum score required | Conflicted = ? |
|---|---|---|
| Short currency | Mild Bearish (more 🔴 than 🟢) | ❌ Do not short — wait for score to resolve |
| Long currency | Mild Bullish (more 🟢 than 🔴) | ❌ Do not long — wait for score to resolve |

A **Conflicted** score (roughly equal 🟢 and 🔴, e.g. 3 vs 3) means the market has mixed signals on that currency. Do not enter a trade where either leg is Conflicted — the thesis has not formed clearly enough to risk capital.

**Thesis deterioration rule (for open trades):**

If the weekly fundamental scan shows the short leg's score moving from Mild Bearish **toward** Conflicted (score improving, gap narrowing), flag it explicitly and reassess:
- Score still clearly Mild/Strong Bearish → hold
- Score now Conflicted → consider closing or tightening stop to breakeven
- Score flipped to Mild/Strong Bullish → close immediately, thesis is broken

---

### Trade Management (after entry)

- **TP1:** Close 50% of position at first key S&R level beyond entry
- **TP2:** Close remaining 50% at second key S&R level or channel boundary
- **Stop tightening:** Once price reaches 1:1 R, consider moving stop to breakeven
- **Minimum R:R:** 1.5:1 to TP1 required to take the trade (prefer 2:1 or better)
- **Stop placement:** SL must be at the nearest structural level that invalidates the thesis (e.g. above the swing high that would break the bearish channel), not just above the trigger candle's wick. The candle wick is the minimum — the structural level is the actual placement.
- **Max stop width:** 50 pips on a 4H setup / 80 pips on a Daily setup — if the structural invalidation level is further than this, the zone is too loose, skip or reassess
- **Correlation risk:** Avoid simultaneous exposure to the same currency on multiple pairs (e.g. SEKJPY long + EURSEK short = double SEK long). Flag and size down if correlation is unavoidable

---

### Weekly FX Overview (automated Friday report)

Covers 19 currencies. Produces a structured `.md` report with: economic highlights, upcoming calendar, FX performance vs USD, and stock index weekly performance.

Output destinations:
- **GitHub**: `weekly-reports/YYYY-WXX.md` in repo `joewaiman/FX_Trading`
- **Notion**: new row in the Weekly FX Overview database (`f1e168c7-1f0e-447d-b185-de215949d17f`), parent page ID `344f5490-1aec-819e-87e3-e0efc16e651d`

Reference files:
- `weekly-fx-overview-extracted/weekly-fx-overview/references/indices.md` — full index-to-currency mapping (tickers, exchanges)
- `weekly-fx-overview-extracted/weekly-fx-overview/references/notion.md` — Notion database/page IDs and property schema
- `weekly-fx-overview-extracted/weekly-fx-overview/references/sources.md` — data source URLs and search templates

---

### GitHub publish commands

```bash
# Weekly FX overview report
gh api repos/joewaiman/FX_Trading/contents/weekly-reports/YYYY-WXX.md \
  --method PUT \
  --field message="Add weekly FX overview W{XX} {YYYY}" \
  --field content="$(base64 -i YYYY-WXX.md)"

# S&R chart screenshots
gh api repos/joewaiman/FX_Trading/contents/charts/PAIR_YYYYMMDD_weekly.png \
  --method PUT \
  --field message="Add S&R chart: PAIR YYYY-MM-DD (Weekly)" \
  --field content="$(base64 -i /path/to/screenshot.png)"
```

---

## Trade Log Convention

All per-pair analysis files are saved in `analysis/` using this naming scheme:

| File pattern | Contents |
|---|---|
| `analysis/YYYY-MM-DD-PAIR-technical.md` | Full technical analysis output (Steps 2–4) for a single pair |
| `analysis/YYYY-MM-DD-W22-technical.md` | Week's batch technical analysis across all screened pairs |
| `fundamental-analysis/YYYY-WXX.md` | Weekly fundamental scorecard for all 19 currencies |
| `weekly-reports/YYYY-WXX.md` | Weekly FX overview report (auto-generated Friday) |

Each trade file records: entry price, stop loss, TP1, TP2, R:R, trade status (waiting / open / closed), and outcome (pips won/lost) when closed.

---

## TradingView MCP — Known Bugs & Workarounds

These bugs were root-cause diagnosed during live sessions. Apply these workarounds every time.

### Bug 1: `chart_set_symbol` — visual update fails silently

**Symptom:** `chart_set_symbol` returns `chart_ready: false`. The internal model updates (so `chart_get_state` reports the new symbol) but the chart does not visually re-render. All subsequent `data_get_ohlcv` and `data_get_study_values` calls return data for the OLD symbol.

**Workaround:**
1. Call `chart_set_symbol` as normal
2. Check `chart_ready` in the response — if `false`, do NOT read data yet
3. Switch via mouse: click the symbol button at approximately **(115, 22)** → `ui_keyboard("ctrl+a")` → `ui_type_text("SEKJPY")` → take a `capture_screenshot` to confirm the search results loaded → `ui_mouse_click` on the result row by pixel coordinate
4. Always take a `capture_screenshot` after switching and confirm the symbol shown in the chart header matches the intended pair before reading any data

**Screenshot is the only reliable source of truth** for confirming a symbol switch. Do not trust `chart_get_state` alone after `chart_set_symbol`.

---

### Bug 2: `indicator_set_inputs` — returns empty `updated_inputs`

**Symptom:** Passing `{ length: 20 }` to `indicator_set_inputs` returns `updated_inputs: {}` — inputs unchanged. The indicator input IDs are opaque (e.g. `"in_0"`), not human-readable names like `"length"`.

**Workaround:** Call `data_get_indicator` first to inspect the actual input IDs for the target indicator, then pass those exact IDs to `indicator_set_inputs`.

**Practical note:** SMA periods (20 and 50) should be configured manually in TradingView once and will persist across symbol switches. Do not attempt to set them programmatically each session.

---

### Bug 3: Currently forming candle included in `data_get_ohlcv`

**Symptom:** `data_get_ohlcv` always includes the candle currently forming as the last bar (`bars[-1]`). Its OHLC values change with every tick — using it for pattern analysis produces false results.

**Workaround:** Always exclude `bars[-1]` from pattern analysis. Use `bars[-2]` as the most recently completed candle and `bars[-3]` as the prior candle.

---

### Bug 4: Keyboard symbol search — Enter key behaviour unreliable

**Symptom:** After typing a symbol via `ui_keyboard("/")` → `ui_type_text("SEKJPY")`, pressing `ui_keyboard("Enter")` sometimes closes the search dialog without selecting the result, or selects the wrong row.

**Workaround:** Instead of pressing Enter, take a `capture_screenshot` to identify the pixel coordinates of the desired result row, then `ui_mouse_click` at that exact coordinate. Saxo results typically appear at y≈333 for the first result; adjust based on screenshot.

---

## Data Files

| File | Contents |
|------|----------|
| `Files/SimplifiedTracker.csv` | Month-by-month unemployment rates (Mar 2022 → Dec 2026) for G8 + EM currencies, with 3.5%–4.5% gauge band |
| `Files/FXPAIRS - FXPAIRS.csv` | 19×19 cross-rate matrix (spot rates between all basket currencies) |
| `csv/` | Additional CSV output — currently empty |

---

## Currency Universe

All skills use the same 19-currency basket: `USD, GBP, CHF, SEK, SGD, PLN, NOK, NZD, MXN, JPY, INR, HUF, EUR, DKK, CNY, CAD, BRL, AUD, ILS`

---

## Tools Used

| Task | Tool |
|------|------|
| Fetch economic data pages | `web_fetch` (Trading Economics URLs) |
| Search for latest releases | `web_search` |
| Push reports to GitHub | `gh` CLI (Bash) |
| Update Notion database | Notion MCP (`notion-create-pages`, `notion-update-page`) |
| Read live chart data | TradingView MCP (`data_get_ohlcv`, `data_get_study_values`, `quote_get`) |
| Switch chart symbol | TradingView MCP (`chart_set_symbol` + keyboard workaround — see bugs above) |
| Capture chart screenshots | TradingView MCP (`capture_screenshot`) |
