"""
Push W21 (22 May 2026) fundamental analysis for all 19 currencies to Supabase.
Run: python log_fundamental_analysis.py
"""
import sys
sys.path.insert(0, r"C:\Users\joewa\projects\FX_Trading")
from db import insert_fundamental

analysis_date = "2026-05-22"

rows = [
    # ── USD ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "USD",
        "policy_rate":         3.75,
        "cpi_yoy":             3.8,
        "cpi_vs_target":       "bullish",    # above 2% target
        "rate_bias":           "neutral",    # FOMC hold, no urgency to cut
        "unemployment":        4.3,
        "unemployment_score":  "bullish",    # within 3.5–4.5% band
        "gdp_qoq":             None,         # no Q1 print this week
        "gdp_score":           "neutral",
        "pmi_manufacturing":   55.3,
        "pmi_services":        50.9,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bearish",    # structural deficit
        "te_commentary_score": "neutral",
        "overall_score":       4,
        "overall_bias":        "mild_bullish",
        "notes":               "FOMC hold at 3.75%. Initial jobless claims 209K beat. DXY flat ~99.32. Labour market resilient. No urgency to cut.",
    },
    # ── EUR ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "EUR",
        "policy_rate":         2.15,
        "cpi_yoy":             3.0,
        "cpi_vs_target":       "bullish",    # above 2% target
        "rate_bias":           "bearish",    # cutting cycle ongoing
        "unemployment":        6.2,
        "unemployment_score":  "bearish",    # above 5.5% threshold
        "gdp_qoq":             0.1,
        "gdp_score":           "neutral",    # near stall
        "pmi_manufacturing":   51.4,
        "pmi_services":        46.4,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "bearish",    # services contraction, energy inflation
        "overall_score":       1,
        "overall_bias":        "strong_bearish",
        "notes":               "Services PMI 46.4 — firmly in contraction. Energy inflation 10.8% YoY. GDP near stall. ECB cutting. EUR/USD 1.1594.",
    },
    # ── GBP ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "GBP",
        "policy_rate":         3.75,
        "cpi_yoy":             2.8,
        "cpi_vs_target":       "bullish",    # above 2% target (but falling)
        "rate_bias":           "neutral",    # BoE holding, CPI drop reduces pressure
        "unemployment":        5.0,
        "unemployment_score":  "neutral",    # 4.5–5.5% neutral band
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   53.7,
        "pmi_services":        47.9,
        "retail_sales_mom":    -1.3,
        "retail_sales_score":  "bearish",
        "trade_balance":       None,
        "trade_balance_score": "bearish",    # structural deficit
        "te_commentary_score": "bearish",
        "overall_score":       2,
        "overall_bias":        "mild_bearish",
        "notes":               "CPI dropped to 2.8% from 3.3% — largest monthly drop recently. Services PMI 47.9 contraction. Retail sales -1.3% MoM. GBP week's standout performer despite weak data.",
    },
    # ── JPY ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "JPY",
        "policy_rate":         0.75,
        "cpi_yoy":             1.4,
        "cpi_vs_target":       "bearish",    # below 2% BoJ target
        "rate_bias":           "neutral",    # BoJ held, hike cycle paused
        "unemployment":        2.7,
        "unemployment_score":  "bullish",    # below 3.5% — very tight (flag overheating)
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   54.5,
        "pmi_services":        50.0,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       302.0,        # billions JPY
        "trade_balance_score": "bullish",    # positive trade balance
        "te_commentary_score": "neutral",
        "overall_score":       3,
        "overall_bias":        "neutral",
        "notes":               "BoJ held at 0.75%. CPI 1.4% below 2% target — no urgency to hike. Manufacturing PMI 54.5 strong. Trade balance positive +¥302B. JPY marginally weaker on risk-on flows.",
    },
    # ── AUD ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "AUD",
        "policy_rate":         4.35,
        "cpi_yoy":             4.6,
        "cpi_vs_target":       "bullish",    # above 2–3% RBA band
        "rate_bias":           "neutral",    # high rates, but cuts off table for now
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   50.2,
        "pmi_services":        47.7,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       -1841.0,      # millions AUD
        "trade_balance_score": "bearish",
        "te_commentary_score": "neutral",
        "overall_score":       3,
        "overall_bias":        "neutral",
        "notes":               "CPI 4.6% well above RBA 2–3% band — rate cuts subdued. Services PMI contracted 47.7. AUD/USD top G8 performer at 0.7118 on Middle East de-escalation hopes.",
    },
    # ── NZD ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "NZD",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "bearish",    # RBNZ in cutting cycle
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "bearish",    # weak recent GDP prints
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "neutral",
        "overall_score":       2,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. NZD tracked AUD higher on risk sentiment, closing near 0.5870. RBNZ in cutting cycle weighs on medium-term outlook.",
    },
    # ── CAD ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "CAD",
        "policy_rate":         2.25,
        "cpi_yoy":             2.8,
        "cpi_vs_target":       "bullish",    # within 1–3% target band but above midpoint
        "rate_bias":           "bearish",    # BoC cutting amid GDP contraction
        "unemployment":        6.9,
        "unemployment_score":  "bearish",    # above 5.5% threshold
        "gdp_qoq":             -0.2,
        "gdp_score":           "bearish",
        "pmi_manufacturing":   None,
        "pmi_services":        49.2,
        "retail_sales_mom":    0.6,
        "retail_sales_score":  "bullish",
        "trade_balance":       1780.0,       # millions CAD
        "trade_balance_score": "bullish",
        "te_commentary_score": "bearish",
        "overall_score":       3,
        "overall_bias":        "mild_bearish",
        "notes":               "GDP contracted -0.2% QoQ. Unemployment rose to 6.9%. BoC at 2.25% with cutting bias. Retail sales +0.6% sole bright spot. CAD effectively flat on week.",
    },
    # ── CHF ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "CHF",
        "policy_rate":         0.25,
        "cpi_yoy":             0.3,
        "cpi_vs_target":       "bearish",    # well below SNB 0–2% band midpoint
        "rate_bias":           "neutral",    # SNB near zero, limited room
        "unemployment":        None,
        "unemployment_score":  "bullish",    # historically ~2.5%, tight labour market
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bullish",    # structural surplus
        "te_commentary_score": "neutral",
        "overall_score":       3,
        "overall_bias":        "mild_bullish",
        "notes":               "No major releases W21. CHF firmed modestly as safe haven. CPI 0.3% near bottom of SNB band. USDCHF near 0.785. SNB rate at 0.25%.",
    },
    # ── CNY ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "CNY",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",    # PBOC on hold
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bullish",    # structural surplus
        "te_commentary_score": "neutral",
        "overall_score":       3,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. USDCNY stable near 6.81. PBOC-managed — policy discretion overrides fundamentals. Markets watched US-China trade rhetoric.",
    },
    # ── INR ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "INR",
        "policy_rate":         6.0,
        "cpi_yoy":             4.0,
        "cpi_vs_target":       "bullish",    # at 4% midpoint of 2–6% RBI band
        "rate_bias":           "neutral",    # RBI holding
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "bullish",    # India growth story intact
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bearish",    # structural trade deficit
        "te_commentary_score": "neutral",
        "overall_score":       4,
        "overall_bias":        "mild_bullish",
        "notes":               "USDINR at 95.97 (H.10 May 15). INR -0.8% on week. RBI rate 6.00%, CPI 4.0% at midpoint of target band. India growth story remains positive.",
    },
    # ── BRL ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "BRL",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",
        "unemployment":        6.1,
        "unemployment_score":  "bullish",    # below 8% bullish threshold for BRL
        "gdp_qoq":             0.1,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bearish",    # CA deficit widened to -$6.04B
        "te_commentary_score": "bearish",    # fiscal concerns, Ibovespa -2.25%
        "overall_score":       5,
        "overall_bias":        "mild_bullish",
        "notes":               "Unemployment 6.1% (bullish for EM). GDP Q1 +0.1% QoQ. CA deficit widened to -$6.04B vs -$5.8B forecast. Ibovespa -2.25% on fiscal concerns.",
    },
    # ── MXN ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "MXN",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "bearish",    # Banxico cutting cycle
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       5930.0,       # millions USD, beat significantly
        "trade_balance_score": "bullish",
        "te_commentary_score": "neutral",
        "overall_score":       3,
        "overall_bias":        "mild_bearish",
        "notes":               "Trade surplus beat at $5.93B vs $3.8B forecast. Peso broadly stable, USDMXN near 17.36. Banxico cutting cycle weighs on MXN outlook.",
    },
    # ── NOK ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "NOK",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bullish",    # oil ~50% above pre-conflict levels
        "te_commentary_score": "neutral",
        "overall_score":       2,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. Oil prices ~50% above pre-Middle East conflict levels — ongoing NOK support. No major macro data this week.",
    },
    # ── SEK ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "SEK",
        "policy_rate":         2.0,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "bearish",    # Riksbank cutting
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "bearish",
        "overall_score":       4,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. Riksbank rate 2.00% — in cutting cycle. SEK tracking EUR broadly. Conflicted signals.",
    },
    # ── DKK ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "DKK",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "bullish",    # mirrors EUR — CPI above ECB 2% target
        "rate_bias":           "bearish",    # mirrors ECB — cutting cycle
        "unemployment":        None,
        "unemployment_score":  "bearish",    # mirrors EUR unemployment ~6.2%
        "gdp_qoq":             0.1,          # mirrors EUR GDP
        "gdp_score":           "neutral",
        "pmi_manufacturing":   51.4,         # mirrors EUR manufacturing PMI
        "pmi_services":        46.4,         # mirrors EUR services PMI
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "bearish",
        "overall_score":       1,
        "overall_bias":        "strong_bearish",
        "notes":               "DKK mirrors EUR (ERM II peg — independent scoring not applicable). EUR/DKK peg intact. Scores identical to EUR.",
    },
    # ── PLN ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "PLN",
        "policy_rate":         5.75,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",    # NBP on hold
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "neutral",
        "overall_score":       1,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. PLN stable. NBP rate 5.75%. Data-limited week — insufficient signals.",
    },
    # ── HUF ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "HUF",
        "policy_rate":         6.5,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",    # NBH on hold
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "neutral",
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "neutral",
        "overall_score":       2,
        "overall_bias":        "neutral",
        "notes":               "No major releases W21. HUF tracking regional EM flows. NBH rate 6.50%. Data-limited — insufficient signals for directional bias.",
    },
    # ── SGD ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "SGD",
        "policy_rate":         None,         # MAS uses S$NEER slope, not rate
        "cpi_yoy":             None,         # Core inflation data due W22
        "cpi_vs_target":       "neutral",
        "rate_bias":           "neutral",    # MAS stance unchanged
        "unemployment":        None,
        "unemployment_score":  "bullish",    # SGD typically 2–3%, tight labour market
        "gdp_qoq":             None,
        "gdp_score":           "bullish",    # GDP YoY 4.6% (W22 final — strong)
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "bullish",    # Singapore structural surplus
        "te_commentary_score": "bullish",
        "overall_score":       6,
        "overall_bias":        "mild_bullish",
        "notes":               "No major releases W21. Core inflation data due W22. MAS stance unchanged — S$NEER slope held. SGD/USD at 0.7407. Strong GDP YoY ~4.6% expected.",
    },
    # ── ILS ─────────────────────────────────────────────────────────────────
    {
        "analysis_date":       analysis_date,
        "currency":            "ILS",
        "policy_rate":         None,
        "cpi_yoy":             None,
        "cpi_vs_target":       "neutral",
        "rate_bias":           "bearish",    # BoI cutting to support economy
        "unemployment":        None,
        "unemployment_score":  "neutral",
        "gdp_qoq":             None,
        "gdp_score":           "bearish",    # conflict impact on economy
        "pmi_manufacturing":   None,
        "pmi_services":        None,
        "retail_sales_mom":    None,
        "retail_sales_score":  "neutral",
        "trade_balance":       None,
        "trade_balance_score": "neutral",
        "te_commentary_score": "bearish",    # geopolitical risk elevated
        "overall_score":       1,
        "overall_bias":        "mild_bearish",
        "notes":               "No major releases W21. Geopolitical sensitivity elevated (Middle East focus). ILS broadly stable. BoI cutting to support war-impacted economy.",
    },
]

print(f"Inserting {len(rows)} fundamental analysis rows for {analysis_date}...")
results = []
for row in rows:
    try:
        r = insert_fundamental(row)
        results.append(r)
        print(f"  OK  {row['currency']:4s}  {row['overall_bias']}")
    except Exception as e:
        print(f"  ERR {row['currency']:4s}  {e}")

print(f"\nDone. {len(results)}/{len(rows)} rows inserted.")
