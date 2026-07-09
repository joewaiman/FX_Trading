"""
db.py — FX Trading Database Helper
Uses the Supabase REST API directly via requests — no supabase-py client needed.

Usage:
    from db import insert_technical, get_open_trades, win_rate_by_pattern
"""

import requests
from datetime import datetime
from typing import Optional

SUPABASE_URL = "https://hjjwwtziixfxojypyyhp.supabase.co"
SUPABASE_KEY = "sb_publishable_ykuY0GX2lNnJXHGLStUtEg_iGEAy46x"

BASE = f"{SUPABASE_URL}/rest/v1"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",   # makes inserts/updates return the saved row
}


def _get(table: str, params: dict = None) -> list:
    r = requests.get(f"{BASE}/{table}", headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()


def _post(table: str, data: dict | list) -> list:
    r = requests.post(f"{BASE}/{table}", headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()


def _patch(table: str, filters: dict, data: dict) -> list:
    params = {k: f"eq.{v}" for k, v in filters.items()}
    r = requests.patch(f"{BASE}/{table}", headers=HEADERS, json=data, params=params)
    r.raise_for_status()
    return r.json()


# ══════════════════════════════════════════════════════
# FUNDAMENTAL ANALYSIS
# ══════════════════════════════════════════════════════

def insert_fundamental(data: dict) -> list:
    """
    Insert a fundamental analysis row.

    Example:
        insert_fundamental({
            "analysis_date": "2026-05-24",
            "currency": "CHF",
            "policy_rate": 0.25,
            "cpi_yoy": 0.3,
            "cpi_vs_target": "bearish",
            "rate_bias": "bearish",
            "overall_score": 3,
            "overall_bias": "mild_bearish",
        })
    """
    return _post("fundamental_analysis", data)


def get_fundamental(currency: str, limit: int = 5) -> list:
    """Get last N fundamental analyses for a currency."""
    return _get("fundamental_analysis", {
        "currency": f"eq.{currency.upper()}",
        "order": "analysis_date.desc",
        "limit": limit,
    })


def get_fundamental_by_date(analysis_date: str) -> list:
    """Get all currency rows for a specific date (YYYY-MM-DD), sorted by score."""
    return _get("fundamental_analysis", {
        "analysis_date": f"eq.{analysis_date}",
        "order": "overall_score.desc",
    })


def get_latest_fundamental_all() -> list:
    """
    Get the most recent fundamental analysis row per currency.
    Fetches recent rows and dedupes in Python (Supabase REST doesn't support DISTINCT ON).
    """
    rows = _get("fundamental_analysis", {
        "order": "analysis_date.desc",
        "limit": 200,
    })
    seen = set()
    result = []
    for row in rows:
        ccy = row["currency"]
        if ccy not in seen:
            seen.add(ccy)
            result.append(row)
    return result


# ══════════════════════════════════════════════════════
# TECHNICAL ANALYSIS
# ══════════════════════════════════════════════════════

def insert_technical(data: dict) -> list:
    """
    Insert a technical analysis row.

    Example:
        result = insert_technical({
            "analysis_date": "2026-05-24",
            "pair": "CHFJPY",
            "weekly_channel": "bearish",
            "daily_channel": "bearish",
            "h4_channel": "bearish",
            "overall_bias": "bearish",
            "sma_20": 201.781,
            "sma_50": 201.667,
            "rsi_daily": 48.60,
            "rsi_h4": 47.31,
            "entry_pattern": "bearish_engulfing",
            "confluence_score": 4,
            "entry_status": "triggered",
            "direction": "short",
            "entry_price": 202.318,
            "stop_loss": 202.578,
            "tp1": 200.800,
            "tp2": 200.000,
            "rr_tp1": 5.8,
            "rr_tp2": 9.1,
            "trade_status": "active",
        })
        analysis_id = result[0]["id"]
    """
    return _post("technical_analysis", data)


def get_technical(pair: str, limit: int = 5) -> list:
    """Get last N technical analyses for a pair."""
    return _get("technical_analysis", {
        "pair": f"eq.{pair.upper()}",
        "order": "analysis_date.desc",
        "limit": limit,
    })


def update_technical_status(analysis_id: str, trade_status: str, notes: str = None) -> list:
    """Update trade_status on an existing technical analysis row."""
    data = {"trade_status": trade_status}
    if notes:
        data["notes"] = notes
    return _patch("technical_analysis", {"id": analysis_id}, data)


# ══════════════════════════════════════════════════════
# TRADES (live)
# ══════════════════════════════════════════════════════

def insert_trade(data: dict) -> list:
    """
    Log a new live trade at entry. Returns the saved row including id.

    Example:
        result = insert_trade({
            "pair": "CHFJPY",
            "direction": "short",
            "entry_date": "2026-05-22T14:00:00Z",
            "entry_price": 202.318,
            "stop_loss": 202.578,
            "tp1": 200.800,
            "tp2": 200.000,
            "technical_analysis_id": "<uuid>",
        })
        trade_id = result[0]["id"]
    """
    return _post("trades", data)


def close_trade(trade_id: str, exit_price: float, exit_reason: str,
                pips_result: float = None, rr_achieved: float = None,
                outcome: str = None, exit_date: str = None, notes: str = None) -> list:
    """
    Close a trade with exit details.
    exit_reason: tp1 / tp2 / stop / manual
    outcome: win / loss / breakeven
    """
    data = {
        "exit_price": exit_price,
        "exit_reason": exit_reason,
        "exit_date": exit_date or datetime.utcnow().isoformat() + "Z",
    }
    if pips_result is not None:
        data["pips_result"] = pips_result
    if rr_achieved is not None:
        data["rr_achieved"] = rr_achieved
    if outcome:
        data["outcome"] = outcome
    if notes:
        data["notes"] = notes
    return _patch("trades", {"id": trade_id}, data)


def get_open_trades() -> list:
    """Get all currently open trades (no exit date)."""
    return _get("trades", {
        "exit_date": "is.null",
        "order": "entry_date.desc",
    })


def get_trades(pair: str = None, outcome: str = None, limit: int = 50) -> list:
    """Query trades, optionally filtered by pair and/or outcome."""
    params = {"order": "entry_date.desc", "limit": limit}
    if pair:
        params["pair"] = f"eq.{pair.upper()}"
    if outcome:
        params["outcome"] = f"eq.{outcome.lower()}"
    return _get("trades", params)


# ══════════════════════════════════════════════════════
# BACKTEST SESSIONS
# ══════════════════════════════════════════════════════

def create_backtest_session(data: dict) -> list:
    """
    Create a new backtest session. Returns the row including generated id.

    Example:
        result = create_backtest_session({
            "created_date": "2026-05-24",
            "pair": "CHFJPY",
            "strategy_name": "multi-tf-bearish-engulfing",
            "date_range_start": "2025-01-01",
            "date_range_end": "2026-05-01",
            "timeframe": "4H",
        })
        session_id = result[0]["id"]
    """
    return _post("backtest_sessions", data)


def update_backtest_session(session_id: str, data: dict) -> list:
    """Update aggregate stats after all trades are entered."""
    return _patch("backtest_sessions", {"id": session_id}, data)


def finalise_backtest_session(session_id: str) -> list:
    """
    Auto-calculate and save aggregate stats from backtest_trades rows.
    Call this once all trades for the session have been inserted.
    """
    trades = get_backtest_trades(session_id)
    if not trades:
        print("No trades found for session")
        return []

    total = len(trades)
    wins = sum(1 for t in trades if t.get("outcome") == "win")
    losses = sum(1 for t in trades if t.get("outcome") == "loss")
    win_rate = round(wins / total * 100, 1) if total > 0 else 0

    rr_values = [t["rr_achieved"] for t in trades if t.get("rr_achieved") is not None]
    avg_rr = round(sum(rr_values) / len(rr_values), 2) if rr_values else None

    win_rr = [t["rr_achieved"] for t in trades if t.get("outcome") == "win" and t.get("rr_achieved")]
    loss_rr = [abs(t["rr_achieved"]) for t in trades if t.get("outcome") == "loss" and t.get("rr_achieved")]
    avg_win = sum(win_rr) / len(win_rr) if win_rr else 0
    avg_loss = sum(loss_rr) / len(loss_rr) if loss_rr else 0
    loss_rate = losses / total if total > 0 else 0
    expectancy = round((win_rate / 100 * avg_win) - (loss_rate * avg_loss), 3)

    return update_backtest_session(session_id, {
        "total_trades": total,
        "wins": wins,
        "losses": losses,
        "win_rate": win_rate,
        "avg_rr_achieved": avg_rr,
        "expectancy": expectancy,
    })


def get_backtest_sessions(pair: str = None) -> list:
    """List all backtest sessions, optionally filtered by pair."""
    params = {"order": "created_date.desc"}
    if pair:
        params["pair"] = f"eq.{pair.upper()}"
    return _get("backtest_sessions", params)


# ══════════════════════════════════════════════════════
# BACKTEST TRADES
# ══════════════════════════════════════════════════════

def insert_backtest_trade(data: dict) -> list:
    """
    Add one trade to a backtest session.

    Example:
        insert_backtest_trade({
            "session_id": "<uuid>",
            "pair": "CHFJPY",
            "direction": "short",
            "entry_date": "2025-06-14",
            "entry_price": 168.450,
            "stop_loss": 169.200,
            "tp1": 167.200,
            "exit_price": 167.200,
            "exit_reason": "tp1",
            "pips_result": 125.0,
            "rr_achieved": 1.7,
            "outcome": "win",
            "weekly_channel": "bearish",
            "daily_channel": "bearish",
            "h4_channel": "bearish",
            "entry_pattern": "bearish_engulfing",
            "confluence_score": 5,
            "fundamental_aligned": True,
        })
    """
    return _post("backtest_trades", data)


def get_backtest_trades(session_id: str) -> list:
    """Get all trades for a backtest session, ordered by entry date."""
    return _get("backtest_trades", {
        "session_id": f"eq.{session_id}",
        "order": "entry_date.asc",
    })


# ══════════════════════════════════════════════════════
# ANALYTICS
# ══════════════════════════════════════════════════════

def _aggregate_by_field(rows: list, field: str) -> list:
    stats = {}
    for row in rows:
        key = row.get(field) or "unknown"
        outcome = row.get("outcome") or "unknown"
        if key not in stats:
            stats[key] = {"wins": 0, "losses": 0, "total": 0}
        stats[key]["total"] += 1
        if outcome == "win":
            stats[key]["wins"] += 1
        elif outcome == "loss":
            stats[key]["losses"] += 1
    result = []
    for key, s in stats.items():
        result.append({
            field: key,
            "total": s["total"],
            "wins": s["wins"],
            "losses": s["losses"],
            "win_rate": round(s["wins"] / s["total"] * 100, 1) if s["total"] > 0 else 0,
        })
    return sorted(result, key=lambda x: x["win_rate"], reverse=True)


def win_rate_by_pattern(source: str = "backtest") -> list:
    """Win rate grouped by entry_pattern. source: 'backtest' or 'live'"""
    table = "backtest_trades" if source == "backtest" else "trades"
    rows = _get(table, {"select": "entry_pattern,outcome"})
    return _aggregate_by_field(rows, "entry_pattern")


def win_rate_by_confluence(source: str = "backtest") -> list:
    """Win rate grouped by confluence_score (5 = highest conviction)."""
    table = "backtest_trades" if source == "backtest" else "trades"
    rows = _get(table, {"select": "confluence_score,outcome"})
    return sorted(_aggregate_by_field(rows, "confluence_score"),
                  key=lambda x: x["confluence_score"], reverse=True)


def win_rate_by_pair(source: str = "backtest") -> list:
    """Win rate grouped by pair."""
    table = "backtest_trades" if source == "backtest" else "trades"
    rows = _get(table, {"select": "pair,outcome"})
    return _aggregate_by_field(rows, "pair")


# ══════════════════════════════════════════════════════
# WEEKLY FX PERFORMANCE
# ══════════════════════════════════════════════════════

def insert_weekly_fx(rows: list) -> list:
    """
    Bulk insert weekly FX performance rows. Pass a list of dicts.
    If re-running the same week, delete first: delete_weekly_fx(week_ending) then re-insert.

    Example:
        insert_weekly_fx([
            {"week_ending": "2026-05-22", "week_label": "W21-2026",
             "currency": "EUR", "spot_vs_usd": 1.1594, "weekly_change_pct": -0.28},
            {"week_ending": "2026-05-22", "week_label": "W21-2026",
             "currency": "GBP", "spot_vs_usd": 1.3420, "weekly_change_pct": 0.66},
        ])
    """
    r = requests.post(f"{BASE}/weekly_fx_performance", headers=HEADERS, json=rows)
    r.raise_for_status()
    return r.json()


def delete_weekly_fx(week_ending: str) -> None:
    """Delete all FX rows for a given week (use before re-inserting corrected data)."""
    r = requests.delete(f"{BASE}/weekly_fx_performance",
                        headers=HEADERS,
                        params={"week_ending": f"eq.{week_ending}"})
    r.raise_for_status()


def get_weekly_fx(week_ending: str = None, currency: str = None, limit: int = 20) -> list:
    """
    Query weekly FX performance.
    - week_ending: filter to a specific Friday (YYYY-MM-DD)
    - currency: filter to a specific currency
    """
    params = {"order": "week_ending.desc,weekly_change_pct.desc", "limit": limit}
    if week_ending:
        params["week_ending"] = f"eq.{week_ending}"
    if currency:
        params["currency"] = f"eq.{currency.upper()}"
    return _get("weekly_fx_performance", params)


def get_weekly_fx_latest() -> list:
    """Get the most recent week's FX performance for all currencies, sorted strongest first."""
    # Find the latest week_ending
    latest = _get("weekly_fx_performance", {
        "select": "week_ending",
        "order": "week_ending.desc",
        "limit": 1,
    })
    if not latest:
        return []
    return get_weekly_fx(week_ending=latest[0]["week_ending"], limit=25)


# ══════════════════════════════════════════════════════
# WEEKLY INDEX PERFORMANCE
# ══════════════════════════════════════════════════════

def insert_weekly_index(rows: list) -> list:
    """
    Bulk insert weekly index performance rows.
    If re-running the same week, delete first: delete_weekly_index(week_ending) then re-insert.

    Example:
        insert_weekly_index([
            {"week_ending": "2026-05-22", "week_label": "W21-2026",
             "currency": "USD", "index_name": "S&P 500", "ticker": "SPX",
             "close_price": 7473, "weekly_change_pts": 30, "weekly_change_pct": 0.40},
        ])
    """
    r = requests.post(f"{BASE}/weekly_index_performance", headers=HEADERS, json=rows)
    r.raise_for_status()
    return r.json()


def delete_weekly_index(week_ending: str) -> None:
    """Delete all index rows for a given week (use before re-inserting corrected data)."""
    r = requests.delete(f"{BASE}/weekly_index_performance",
                        headers=HEADERS,
                        params={"week_ending": f"eq.{week_ending}"})
    r.raise_for_status()


def get_weekly_index(week_ending: str = None, limit: int = 25) -> list:
    """Get weekly index performance, optionally filtered to a specific Friday."""
    params = {"order": "week_ending.desc,weekly_change_pct.desc", "limit": limit}
    if week_ending:
        params["week_ending"] = f"eq.{week_ending}"
    return _get("weekly_index_performance", params)


def fundamental_alignment_edge(source: str = "backtest") -> dict:
    """
    Compare win rate when fundamental_aligned=True vs False.
    Shows the edge from combining fundamental + technical analysis.
    """
    table = "backtest_trades" if source == "backtest" else "trades"
    rows = _get(table, {"select": "fundamental_aligned,outcome"})

    aligned = {"wins": 0, "total": 0}
    not_aligned = {"wins": 0, "total": 0}

    for row in rows:
        fa = row.get("fundamental_aligned")
        outcome = row.get("outcome")
        bucket = aligned if fa is True else (not_aligned if fa is False else None)
        if bucket is None:
            continue
        bucket["total"] += 1
        if outcome == "win":
            bucket["wins"] += 1

    def stats(b):
        return {
            "total": b["total"],
            "wins": b["wins"],
            "win_rate": round(b["wins"] / b["total"] * 100, 1) if b["total"] > 0 else 0,
        }

    return {
        "fundamental_aligned": stats(aligned),
        "not_aligned": stats(not_aligned),
    }
