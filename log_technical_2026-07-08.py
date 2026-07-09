"""Log the three high-conviction technical analyses (2026-07-08) to Supabase."""
import sys
sys.path.insert(0, r"C:\Users\joewa\Projects\FX_Trading")
from db import insert_technical

d = "2026-07-08"

rows = [
    {
        "analysis_date": d, "pair": "NOKSEK",
        "weekly_channel": "bullish", "daily_channel": "bullish", "h4_channel": "bullish",
        "overall_bias": "bullish",
        "sma_20": 0.9872, "sma_50": 0.9974, "rsi_daily": 54.8, "rsi_h4": 73.0,
        "divergence": "none",
        "key_resistance_1": 1.000, "key_resistance_2": 1.022,
        "key_support_1": 0.985, "key_support_2": 0.978,
        "entry_zone": 0.985, "entry_pattern": "none", "confluence_score": 4,
        "entry_status": "waiting", "direction": "long",
        "entry_price": 0.9855, "stop_loss": 0.977, "tp1": 1.000, "tp2": 1.022,
        "rr_tp1": 1.7, "rr_tp2": 4.4, "trade_status": "watching",
        "notes": "Top pick. All 3 TFs bullish + fundamentals aligned (oil-bull NOK vs dovish SEK). "
                 "Weekly HH/HL off 0.905; daily corrected to higher low 0.978, RSI turned up 38->55; "
                 "4H broke out of base, RSI 73 o/b. Buy dip 0.985 (20 SMA) or break >1.000.",
    },
    {
        "analysis_date": d, "pair": "USDSEK",
        "weekly_channel": "sideways", "daily_channel": "bullish", "h4_channel": "bullish",
        "overall_bias": "bullish",
        "sma_20": 9.612, "sma_50": 9.437, "rsi_daily": 64.5, "rsi_h4": 65.8,
        "divergence": "none",
        "key_resistance_1": 9.795, "key_resistance_2": 9.90,
        "key_support_1": 9.61, "key_support_2": 9.50,
        "entry_zone": 9.66, "entry_pattern": "none", "confluence_score": 3,
        "entry_status": "waiting", "direction": "long",
        "entry_price": 9.66, "stop_loss": 9.585, "tp1": 9.795, "tp2": 9.90,
        "rr_tp1": 1.8, "rr_tp2": 3.2, "trade_status": "watching",
        "notes": "Weekly reversal (year-long 11.32->8.74 downtrend turned up). Daily bullish pullback-and-resume "
                 "off 20 SMA 9.61. 4H reclaimed both SMAs, RSI near o/b. Buy dip 9.66 or break >9.80.",
    },
    {
        "analysis_date": d, "pair": "SEKJPY",
        "weekly_channel": "bearish", "daily_channel": "bearish", "h4_channel": "bearish",
        "overall_bias": "bearish",
        "sma_20": 16.762, "sma_50": 16.900, "rsi_daily": 44.6, "rsi_h4": 44.5,
        "divergence": "none",
        "key_resistance_1": 16.80, "key_resistance_2": 16.90,
        "key_support_1": 16.505, "key_support_2": 16.30,
        "entry_zone": 16.80, "entry_pattern": "none", "confluence_score": 3,
        "entry_status": "waiting", "direction": "short",
        "entry_price": 16.80, "stop_loss": 16.90, "tp1": 16.505, "tp2": 16.30,
        "rr_tp1": 3.0, "rr_tp2": 5.0, "trade_status": "watching",
        "notes": "Expresses LONG JPY/SEK as SHORT SEKJPY. Weekly topping (17.66 high rolling over), daily downtrend, "
                 "4H bounce failed into lower high. ILLIQUID cross (Capital.com feed, wide spreads). "
                 "Sell bounce into 16.80; poor R:R from spot.",
    },
]

for r in rows:
    res = insert_technical(r)
    print(f"OK {r['pair']}: id={res[0]['id']}")
