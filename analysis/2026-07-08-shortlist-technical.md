# Shortlist Technical Analysis — 2026-07-08 (W28)

> ⚠️ **Reconstructed 2026-07-09, not written contemporaneously.** The 2026-07-08 session produced no
> markdown file. This document is rebuilt from `log_technical_2026-07-08.py`, which is the only
> surviving record of that session's numbers.
>
> The script was written to insert these rows into Supabase. It almost certainly never did —
> `hjjwwtziixfxojypyyhp.supabase.co` does not resolve (NXDOMAIN), and the script has no error
> handling, so it would have raised on the first `insert_technical` call. **Treat the script as the
> source of truth and assume no DB rows exist.**
>
> Everything below is the logged field values plus the `notes` string for each pair. Chart reasoning
> beyond those notes was not preserved and has not been invented here.

Method: `fx-technical-analysis`, top-down W → D → 4H. Prices as read on 2026-07-08 and **now stale** —
re-check spot, SMAs and RSI against live data before acting on any level.

**Bottom line: no trigger confirmed on any pair. `entry_pattern: none` and `entry_status: waiting`
across all three. Nothing to enter at market.**

---

## 🔴 Concentration risk — these are one trade, not three

Long NOKSEK, long USDSEK and short SEKJPY are each a **short-SEK** expression. The confluence scores
read as three independent convictions, but the correlation is near-total: a hawkish Riksbank surprise
or a SEK short-squeeze hits all three simultaneously.

**Size as one position.** If taking more than one, cut size proportionally. Per `CLAUDE.md`
("Correlation risk"), simultaneous same-currency exposure across pairs must be flagged and sized down.

---

## Ranking (as logged)

1. **NOKSEK** — top pick, confluence 4, all three timeframes bullish
2. **USDSEK** — confluence 3
3. **SEKJPY** — confluence 3, illiquid, poor R:R from spot

---

## 1. NOKSEK — LONG · entry zone 0.985

- **Channel:** W 🟢 / D 🟢 / 4H 🟢. Bias BULLISH, all three aligned.
- **SMA:** SMA20 0.9872, SMA50 0.9974.
- **RSI:** Daily 54.8, 4H **73.0 (overbought)**. Divergence: none.
- **Key levels:** R 1.000, 1.022. S 0.985, 0.978.
- **Entry trigger:** Zone 0.985 (20 SMA). Pattern none yet. Confluence 4.
- **Trade setup:** LONG · Entry 0.9855 · SL 0.977 · TP1 1.000 (**R:R 1.7:1**) · TP2 1.022 (4.4:1).

**Logged rationale:** Top pick. All 3 TFs bullish + fundamentals aligned (oil-bull NOK vs dovish SEK).
Weekly HH/HL off 0.905; daily corrected to higher low 0.978, RSI turned up 38→55; 4H broke out of base,
RSI 73 overbought. Buy dip 0.985 (20 SMA) or break >1.000.

---

## 2. USDSEK — LONG · entry zone 9.66

- **Channel:** W 🟡 sideways / D 🟢 / 4H 🟢. Bias BULLISH.
- **SMA:** SMA20 9.612, SMA50 9.437.
- **RSI:** Daily 64.5, 4H 65.8 (both approaching overbought). Divergence: none.
- **Key levels:** R 9.795, 9.90. S 9.61, 9.50.
- **Entry trigger:** Zone 9.66. Pattern none yet. Confluence 3.
- **Trade setup:** LONG · Entry 9.66 · SL 9.585 · TP1 9.795 (**R:R 1.8:1**) · TP2 9.90 (3.2:1).

**Logged rationale:** Weekly reversal (year-long 11.32→8.74 downtrend turned up). Daily bullish
pullback-and-resume off 20 SMA 9.61. 4H reclaimed both SMAs, RSI near overbought. Buy dip 9.66 or
break >9.80.

---

## 3. SEKJPY — SHORT · entry zone 16.80

- **Channel:** W 🔴 / D 🔴 / 4H 🔴. Bias BEARISH, all three aligned.
- **SMA:** SMA20 16.762, SMA50 16.900.
- **RSI:** Daily 44.6, 4H 44.5 (neutral). Divergence: none.
- **Key levels:** R 16.80, 16.90. S 16.505, 16.30.
- **Entry trigger:** Zone 16.80. Pattern none yet. Confluence 3.
- **Trade setup:** SHORT · Entry 16.80 · SL 16.90 · TP1 16.505 (**R:R 3.0:1**) · TP2 16.30 (5.0:1).

**Logged rationale:** Expresses LONG JPY/SEK as SHORT SEKJPY. Weekly topping (17.66 high rolling over),
daily downtrend, 4H bounce failed into lower high. **ILLIQUID cross (Capital.com feed, wide spreads.)**
Sell bounce into 16.80; poor R:R from spot.

---

## Rule compliance check (added 2026-07-09)

Checking the logged setups against the rules in `CLAUDE.md`. **None of this was recorded on 07-08.**

### ❌ Two of three fail the minimum R:R rule

`CLAUDE.md` → Trade Management: *"Minimum R:R: 1:2 to TP1 required to take the trade."*

| Pair | R:R to TP1 | Passes ≥ 2.0? |
|------|-----------|---------------|
| NOKSEK | 1.7:1 | ❌ No |
| USDSEK | 1.8:1 | ❌ No |
| SEKJPY | 3.0:1 | ✅ Yes |

The top pick and the second pick are both **below the repo's own entry threshold to TP1**. Note this is
the same objection that blocked NOKSEK in W26 — CONTEXT.md records it as *"⏳ WAITING — R:R blocking …
1:2 minimum not met."* The zone moved; the arithmetic did not.

### ⚠️ SEKJPY's stop is 10 pips — repeat of the CHFJPY mistake

SEKJPY is a JPY cross, so 1 pip = 0.01. Entry 16.80, stop 16.90 → **a 10-pip stop**, on the pair the
notes themselves describe as an illiquid Capital.com feed with wide spreads.

The repo already has a post-mortem on precisely this failure mode. From CONTEXT.md on CHFJPY:

> *a 26-pip stop on a pair with a ~130-pip daily range was noise-width, not structure-width. Direction
> was right … the stop was too tight to survive the path.*

That trade lost −1.00R with the thesis correct. This stop is **less than half as wide**, on a less
liquid pair. `CLAUDE.md` requires the stop sit at *"the nearest structural level that invalidates the
thesis,"* not at the trigger candle's wick. 16.90 is the SMA50 — plausibly structural — but 10 pips of
room on a wide-spread cross means the spread itself is a meaningful fraction of the risk budget.
**Re-derive this stop from structure and daily range before entry.**

### ⚠️ NOKSEK stop width may breach the max

Entry 0.9855 → stop 0.977 is 0.0085. On the conventional 0.0001 = 1 pip for NOKSEK that is **85 pips**,
against a `CLAUDE.md` limit of *"50 pips on a 4H setup / 80 pips on a Daily setup."* Confirm the pip
convention on your broker's NOKSEK feed; if it is 0.0001, this setup is over the limit and the zone is
too loose.

### ⚠️ No macro calendar check was recorded

`CLAUDE.md` → Entry Confirmation: the pre-entry macro check *"runs before any other gate"* and must be
*"the first item in any Stage A / B / C entry confirmation output."* No calendar check appears in the
script or in any 07-08 artefact. Riksbank, Norges Bank, Fed and BoJ all need clearing within 72h of any
entry here.

### ⚠️ 4H RSI 73 on NOKSEK

`CLAUDE.md` → blocking conditions: *"RSI < 30 on 4H in a bullish setup → oversold, wait for reset."* The
inverse — 73 overbought on a **long** — is not literally a listed blocker, but it is the reason the
logged plan says "buy the dip to 0.985" rather than entering at spot. Do not chase.

---

## Verdict

Three setups, all `waiting`, all the same short-SEK risk, two of them below the minimum R:R to TP1, one
with a stop too tight for its own spread, and no macro check on record.

Per `CLAUDE.md`: *"'Nothing to trade' is always a valid output."* On the logged numbers, that is the
correct read of 2026-07-08. If the SEK thesis is to be traded at all, it should be **one position,
sized once**, entered on a dip to a zone that produces ≥ 1:2 to TP1 — and only after the W28
fundamental scan confirms the Riksbank is still dovish and the macro calendar is clear.
