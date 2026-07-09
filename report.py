"""
report.py — FX Trading Session Startup Report
Run at the start of each session for a quick state-of-play.

Usage:
    python report.py
    python report.py CHFJPY          # filter to one pair
"""

import sys
sys.stdout.reconfigure(encoding="utf-8")
from datetime import datetime, timezone
from db import (
    get_open_trades,
    get_trades,
    get_technical,
    get_latest_fundamental_all,
    win_rate_by_pattern,
    win_rate_by_confluence,
    win_rate_by_pair,
    fundamental_alignment_edge,
)

PAIR_FILTER = sys.argv[1].upper() if len(sys.argv) > 1 else None

LINE  = "─" * 62
DLINE = "═" * 62


def fmt_date(iso: str) -> str:
    if not iso:
        return "—"
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.strftime("%d %b %Y")
    except Exception:
        return iso[:10]


def pips_sign(val) -> str:
    if val is None:
        return "—"
    return f"+{val:.1f}" if val >= 0 else f"{val:.1f}"


def rr_sign(val) -> str:
    if val is None:
        return "—"
    return f"+{val:.2f}R" if val >= 0 else f"{val:.2f}R"


def bias_icon(bias: str) -> str:
    if not bias:
        return "—"
    b = bias.lower()
    if "strong_bull" in b or b == "bullish":
        return "🟢 " + bias
    if "mild_bull" in b:
        return "🟡 " + bias
    if "strong_bear" in b or b == "bearish":
        return "🔴 " + bias
    if "mild_bear" in b:
        return "🟠 " + bias
    return "⚪ " + bias


def channel_icon(ch: str) -> str:
    if not ch:
        return "—"
    ch = ch.lower()
    if ch == "bullish":   return "🟢"
    if ch == "bearish":   return "🔴"
    if ch == "sideways":  return "🟡"
    return "⚪"


# ══════════════════════════════════════════════════════
# 1. OPEN TRADES
# ══════════════════════════════════════════════════════

open_trades = get_open_trades()
if PAIR_FILTER:
    open_trades = [t for t in open_trades if t.get("pair") == PAIR_FILTER]

print()
print(DLINE)
print(f"  FX SESSION REPORT  —  {datetime.now(timezone.utc).strftime('%d %b %Y  %H:%M UTC')}")
print(DLINE)

print()
print(f"  OPEN TRADES ({len(open_trades)})")
print(LINE)

if not open_trades:
    print("  No open trades.")
else:
    print(f"  {'Pair':<8} {'Dir':<6} {'Entry':>8} {'SL':>8} {'TP1':>8} {'TP2':>8}  Opened")
    print(LINE)
    for t in open_trades:
        print(
            f"  {t.get('pair','—'):<8}"
            f" {(t.get('direction') or '—').upper():<6}"
            f" {t.get('entry_price') or 0:>8.3f}"
            f" {t.get('stop_loss') or 0:>8.3f}"
            f" {t.get('tp1') or 0:>8.3f}"
            f" {t.get('tp2') or 0:>8.3f}"
            f"  {fmt_date(t.get('entry_date'))}"
        )
        if t.get("notes"):
            print(f"  {'':8}  ↳ {t['notes'][:55]}")

# ══════════════════════════════════════════════════════
# 2. RECENT CLOSED TRADES (last 10)
# ══════════════════════════════════════════════════════

closed = get_trades(pair=PAIR_FILTER, limit=10)
closed = [t for t in closed if t.get("exit_date")]

print()
print(f"  RECENTLY CLOSED  (last {len(closed)})")
print(LINE)

if not closed:
    print("  No closed trades yet.")
else:
    print(f"  {'Pair':<8} {'Dir':<6} {'Result':>8} {'R:R':>7} {'Exit reason':<12}  Closed")
    print(LINE)
    for t in closed:
        outcome = t.get("outcome") or "—"
        icon = "✅" if outcome == "win" else ("❌" if outcome == "loss" else "⚪")
        print(
            f"  {icon} {t.get('pair','—'):<8}"
            f" {(t.get('direction') or '—').upper():<6}"
            f" {pips_sign(t.get('pips_result')):>8}"
            f" {rr_sign(t.get('rr_achieved')):>7}"
            f" {(t.get('exit_reason') or '—'):<12}"
            f"  {fmt_date(t.get('exit_date'))}"
        )

# ══════════════════════════════════════════════════════
# 3. LIVE TRADE STATS
# ══════════════════════════════════════════════════════

all_closed = get_trades(pair=PAIR_FILTER, limit=500)
all_closed = [t for t in all_closed if t.get("exit_date")]

if all_closed:
    total   = len(all_closed)
    wins    = sum(1 for t in all_closed if t.get("outcome") == "win")
    losses  = sum(1 for t in all_closed if t.get("outcome") == "loss")
    wr      = wins / total * 100 if total else 0
    rr_vals = [t["rr_achieved"] for t in all_closed if t.get("rr_achieved") is not None]
    avg_rr  = sum(rr_vals) / len(rr_vals) if rr_vals else 0

    win_rr  = [t["rr_achieved"] for t in all_closed if t.get("outcome") == "win"  and t.get("rr_achieved")]
    loss_rr = [abs(t["rr_achieved"]) for t in all_closed if t.get("outcome") == "loss" and t.get("rr_achieved")]
    avg_win  = sum(win_rr)  / len(win_rr)  if win_rr  else 0
    avg_loss = sum(loss_rr) / len(loss_rr) if loss_rr else 0
    loss_rate = losses / total if total else 0
    expectancy = (wr / 100 * avg_win) - (loss_rate * avg_loss)

    print()
    label = f"  LIVE STATS{' — ' + PAIR_FILTER if PAIR_FILTER else '  (all pairs)'}"
    print(label)
    print(LINE)
    print(f"  Trades: {total}   Wins: {wins}   Losses: {losses}   Win rate: {wr:.1f}%")
    print(f"  Avg R:R achieved: {avg_rr:.2f}R   Expectancy: {expectancy:+.3f}R per trade")

# ══════════════════════════════════════════════════════
# 4. LAST TECHNICAL ANALYSIS PER PAIR
# ══════════════════════════════════════════════════════

# Collect all pairs seen in technical analysis table
from db import _get
all_ta = _get("technical_analysis", {"order": "analysis_date.desc", "limit": 500})
if PAIR_FILTER:
    all_ta = [r for r in all_ta if r.get("pair") == PAIR_FILTER]

seen_pairs = {}
for row in all_ta:
    p = row.get("pair")
    if p and p not in seen_pairs:
        seen_pairs[p] = row

if seen_pairs:
    print()
    print(f"  LAST ANALYSIS PER PAIR")
    print(LINE)
    print(f"  {'Pair':<8} {'Date':<12} {'W':^3} {'D':^3} {'4H':^3} {'Bias':<18} {'Status':<14} {'Score'}")
    print(LINE)
    for pair, r in sorted(seen_pairs.items()):
        w  = channel_icon(r.get("weekly_channel"))
        d  = channel_icon(r.get("daily_channel"))
        h4 = channel_icon(r.get("h4_channel"))
        bias   = (r.get("overall_bias") or "—")[:16]
        status = (r.get("trade_status") or "—")[:13]
        score  = r.get("confluence_score")
        score_str = f"{score}/5" if score is not None else "—"
        print(
            f"  {pair:<8}"
            f" {fmt_date(r.get('analysis_date')):<12}"
            f" {w:^3} {d:^3} {h4:^3}"
            f" {bias:<18}"
            f" {status:<14}"
            f" {score_str}"
        )

# ══════════════════════════════════════════════════════
# 5. LATEST FUNDAMENTAL BIAS (all currencies)
# ══════════════════════════════════════════════════════

if not PAIR_FILTER:
    fa_rows = get_latest_fundamental_all()
    if fa_rows:
        print()
        print(f"  FUNDAMENTAL BIAS  (latest per currency)")
        print(LINE)
        print(f"  {'CCY':<6} {'Score':^7} {'Bias':<22} {'Rate%':>6} {'CPI%':>6} {'Date'}")
        print(LINE)
        for r in fa_rows:
            score = r.get("overall_score")
            score_str = f"{score}/9" if score is not None else "—"
            print(
                f"  {r.get('currency','—'):<6}"
                f" {score_str:^7}"
                f" {bias_icon(r.get('overall_bias')):<22}"
                f" {(r.get('policy_rate') or 0):>6.2f}"
                f" {(r.get('cpi_yoy') or 0):>6.1f}"
                f"  {fmt_date(r.get('analysis_date'))}"
            )

# ══════════════════════════════════════════════════════
# 6. EDGE STATS (backtest)
# ══════════════════════════════════════════════════════

bt_patterns = win_rate_by_pattern("backtest")
bt_confluence = win_rate_by_confluence("backtest")
fa_edge = fundamental_alignment_edge("backtest")

has_bt_data = any(r["total"] > 0 for r in bt_patterns)

if has_bt_data:
    print()
    print(f"  BACKTEST EDGE STATS")
    print(LINE)

    if bt_patterns:
        print("  By pattern:")
        for r in bt_patterns:
            bar = "█" * int(r["win_rate"] / 5)
            print(f"    {r['entry_pattern']:<22} {r['win_rate']:>5.1f}%  {bar}  ({r['wins']}W / {r['losses']}L)")

    if bt_confluence:
        print()
        print("  By confluence score:")
        for r in bt_confluence:
            bar = "█" * int(r["win_rate"] / 5)
            print(f"    Score {r['confluence_score']}/5   {r['win_rate']:>5.1f}%  {bar}  ({r['wins']}W / {r['losses']}L)")

    fa_a = fa_edge["fundamental_aligned"]
    fa_n = fa_edge["not_aligned"]
    if fa_a["total"] > 0 or fa_n["total"] > 0:
        print()
        print("  Fundamental alignment edge:")
        print(f"    Aligned:     {fa_a['win_rate']:>5.1f}%  ({fa_a['wins']}W / {fa_a['total'] - fa_a['wins']}L)")
        print(f"    Not aligned: {fa_n['win_rate']:>5.1f}%  ({fa_n['wins']}W / {fa_n['total'] - fa_n['wins']}L)")

print()
print(DLINE)
print()
