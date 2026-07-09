"""
close_may_trades.py — Close out the two May 2026 trades that are still flagged
`active` in Supabase but resolved weeks ago.

Verified 2026-07-09 against FXCM daily bars (TradingView):

  AUDNZD long  — entry 1.21593 (24 May), stop 1.21100, TP1 1.21855, TP2 1.22414
    25 May high 1.22212 -> TP1 hit (closed 50%)
    26 May high 1.22847 -> TP2 hit (closed remainder)
    Lowest low after entry 1.21715 — stop never threatened.
    WIN. Blended +54.2 pips / +1.10R.

  CHFJPY short — entry 202.318 (22 May), stop 202.578, TP1 200.800
    22 May bar high 203.01, 25 May high 203.477, ran to 204.196 by 29 May.
    Stop blown through; TP1 never reached beforehand (lowest low 201.841).
    LOSS. -26.0 pips / -1.00R.

Trade IDs are looked up by pair rather than hardcoded — the UUIDs were generated
by the original log_open_trades.py run and were never captured.

Run:  python close_may_trades.py
      (requires a network that resolves hjjwwtziixfxojypyyhp.supabase.co)
"""

import sys

sys.path.insert(0, r"C:\Users\joewa\Projects\FX_Trading")

from db import close_trade, get_open_trades, update_technical_status

# ══════════════════════════════════════════════════════
# Exit details
# ══════════════════════════════════════════════════════

EXITS = {
    "AUDNZD": {
        "exit_price":  1.22414,
        "exit_reason": "tp2",
        "outcome":     "win",
        "pips_result": 54.2,
        "rr_achieved": 1.10,
        "exit_date":   "2026-05-26T12:00:00Z",
        "notes": (
            "TP1 1.21855 hit 25 May (high 1.22212), TP2 1.22414 hit 26 May (high 1.22847). "
            "Stop never threatened (lowest low after entry 1.21715). "
            "pips_result is the blended 50/50 result: +26.2 on the TP1 half, +82.1 on the TP2 half. "
            "Exit timestamp approximate — reconstructed from daily bars on 2026-07-09."
        ),
    },
    "CHFJPY": {
        "exit_price":  202.578,
        "exit_reason": "stop",
        "outcome":     "loss",
        "pips_result": -26.0,
        "rr_achieved": -1.00,
        "exit_date":   "2026-05-25T07:00:00Z",
        "notes": (
            "Stopped out. Entry-day bar (22 May) printed a high of 203.01 and 25 May reached 203.477, "
            "running on to 204.196 by 29 May — the 26-pip stop at 202.578 was taken out well before "
            "TP1 200.800 was approached (lowest low in that window 201.841). "
            "Exit date may actually be 22 May: the daily bar cannot resolve whether the 203.01 print "
            "came before or after the 14:00Z entry; 25 May is the first unambiguous breach. "
            "Post-mortem: a 26-pip stop on a pair with a ~130-pip daily range was noise-width, not "
            "structure-width. Price is back at 201.3 as of 2026-07-09 — the direction was right, "
            "the stop was too tight to survive it."
        ),
    },
}


def main() -> int:
    print("Fetching open trades...")
    open_trades = get_open_trades()

    if not open_trades:
        print("No open trades returned — nothing to close.")
        return 0

    by_pair = {t["pair"].upper(): t for t in open_trades}
    print(f"  Found {len(open_trades)} open: {', '.join(sorted(by_pair))}\n")

    exit_code = 0

    for pair, exit_data in EXITS.items():
        trade = by_pair.get(pair)

        if trade is None:
            print(f"SKIP {pair}: not in open trades (already closed?)")
            continue

        trade_id = trade["id"]

        # Sanity-check we're closing the trade we think we are.
        entry = trade.get("entry_price")
        print(f"{pair}: id={trade_id} entry={entry}")

        try:
            close_trade(
                trade_id,
                exit_price=exit_data["exit_price"],
                exit_reason=exit_data["exit_reason"],
                pips_result=exit_data["pips_result"],
                rr_achieved=exit_data["rr_achieved"],
                outcome=exit_data["outcome"],
                exit_date=exit_data["exit_date"],
                notes=exit_data["notes"],
            )
            print(f"  OK closed as {exit_data['outcome'].upper()} "
                  f"@ {exit_data['exit_price']} ({exit_data['rr_achieved']:+.2f}R)")
        except Exception as exc:
            print(f"  FAILED to close {pair}: {exc}")
            exit_code = 1
            continue

        # Mirror the outcome onto the linked technical_analysis row.
        ta_id = trade.get("technical_analysis_id")
        if ta_id:
            try:
                update_technical_status(ta_id, "closed")
                print(f"  OK technical_analysis {ta_id} -> closed")
            except Exception as exc:
                print(f"  WARN could not update technical_analysis {ta_id}: {exc}")
        else:
            print("  WARN no technical_analysis_id on trade row")

    print("\nDone. Net across the two: +1.10R - 1.00R = +0.10R.")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
