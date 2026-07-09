"""
log_open_trades.py — One-time script to log current open trades into Supabase.
Run once: python log_open_trades.py
"""

from db import insert_technical, insert_trade

print("Logging open trades...")

# ══════════════════════════════════════════════════════
# 1. CHF/JPY — Short
# ══════════════════════════════════════════════════════

ta_chfjpy = insert_technical({
    "analysis_date":    "2026-05-22",
    "pair":             "CHFJPY",
    "weekly_channel":   "bearish",
    "daily_channel":    "bearish",
    "h4_channel":       "bearish",
    "overall_bias":     "bearish",
    "sma_20":           201.781,
    "sma_50":           201.667,
    "rsi_daily":        48.60,
    "rsi_h4":           47.31,
    "divergence":       "none",
    "key_resistance_1": 202.578,
    "key_resistance_2": 203.000,
    "key_support_1":    200.800,
    "key_support_2":    200.000,
    "entry_zone":       202.500,
    "entry_pattern":    "bearish_engulfing",
    "confluence_score": 4,
    "entry_status":     "triggered",
    "direction":        "short",
    "entry_price":      202.318,
    "stop_loss":        202.578,
    "tp1":              200.800,
    "tp2":              200.000,
    "rr_tp1":           5.8,
    "rr_tp2":           9.1,
    "trade_status":     "active",
    "notes":            "Re-entry short. Near-stop spike to 202.566 on entry day. Bounce to 202.300 — aggressive warning sign. Trail stop recommended.",
})

chfjpy_ta_id = ta_chfjpy[0]["id"]
print(f"  ✅ CHFJPY technical analysis logged: {chfjpy_ta_id}")

trade_chfjpy = insert_trade({
    "technical_analysis_id": chfjpy_ta_id,
    "pair":        "CHFJPY",
    "direction":   "short",
    "entry_date":  "2026-05-22T14:00:00Z",
    "entry_price": 202.318,
    "stop_loss":   202.578,
    "tp1":         200.800,
    "tp2":         200.000,
    "notes":       "Stop 26 pips. TP1 R:R 5.8:1. TP2 R:R 9.1:1. Watch 202.15 as trail target.",
})

chfjpy_trade_id = trade_chfjpy[0]["id"]
print(f"  ✅ CHFJPY trade logged:               {chfjpy_trade_id}")


# ══════════════════════════════════════════════════════
# 2. AUD/NZD — Long
# ══════════════════════════════════════════════════════

ta_audnzd = insert_technical({
    "analysis_date":    "2026-05-24",
    "pair":             "AUDNZD",
    "weekly_channel":   "bullish",
    "daily_channel":    "bullish",
    "h4_channel":       "bullish",
    "overall_bias":     "bullish",
    "sma_20":           1.21855,
    "sma_50":           1.21226,
    "rsi_daily":        50.75,
    "rsi_h4":           42.00,
    "divergence":       "none",
    "key_resistance_1": 1.21855,
    "key_resistance_2": 1.22414,
    "key_support_1":    1.21100,
    "key_support_2":    1.20800,
    "entry_zone":       1.21470,
    "entry_pattern":    "pin_bar",
    "confluence_score": 4,
    "entry_status":     "triggered",
    "direction":        "long",
    "entry_price":      1.21593,
    "stop_loss":        1.21100,
    "tp1":              1.21855,
    "tp2":              1.22414,
    "rr_tp1":           0.5,
    "rr_tp2":           1.7,
    "trade_status":     "active",
    "notes":            "Bullish pin bar confirmed: body 4 pips, lower wick 14 pips (3.5x). TP1 at 20 SMA weak R:R — consider skipping to 1.22000 round number or TP2 direct.",
})

audnzd_ta_id = ta_audnzd[0]["id"]
print(f"  ✅ AUDNZD technical analysis logged: {audnzd_ta_id}")

trade_audnzd = insert_trade({
    "technical_analysis_id": audnzd_ta_id,
    "pair":        "AUDNZD",
    "direction":   "long",
    "entry_date":  "2026-05-24T00:00:00Z",
    "entry_price": 1.21593,
    "stop_loss":   1.21100,
    "tp1":         1.21855,
    "tp2":         1.22414,
    "notes":       "Stop 49 pips. TP2 R:R 1.7:1. Consider skipping TP1 (0.5:1) and targeting 1.22000 or TP2 direct.",
})

audnzd_trade_id = trade_audnzd[0]["id"]
print(f"  ✅ AUDNZD trade logged:               {audnzd_trade_id}")


# ══════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════

print()
print("Save these IDs — you'll need them to close the trades later:")
print(f"  CHFJPY trade ID:  {chfjpy_trade_id}")
print(f"  AUDNZD trade ID:  {audnzd_trade_id}")
print()
print("To close a trade when it exits, run:")
print('  from db import close_trade')
print(f'  close_trade("{chfjpy_trade_id}", exit_price=200.80, exit_reason="tp1", pips_result=151.8, rr_achieved=5.8, outcome="win")')
