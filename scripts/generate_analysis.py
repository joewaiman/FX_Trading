#!/usr/bin/env python3
"""Generate weekly FX fundamental analysis using Claude with web search."""

import anthropic
import sys
from datetime import datetime, timezone
from pathlib import Path

CURRENCIES = ["USD", "AUD", "GBP", "JPY", "EUR", "CHF", "NZD", "CAD"]

SYSTEM_PROMPT = """You are a professional FX macro analyst. Your job is to produce a rigorous,
data-driven weekly fundamental analysis report covering 8 major currencies.

Scoring rubric (9 metrics, each worth 0/0.5/1.0):
1. Interest rate level        🟢 high/rising  🟡 moderate/hold  🔴 low/cutting
2. CPI vs central-bank target 🟢 above        🟡 at/near        🔴 below
3. Rate bias (CB forward guidance) 🟢 hiking  🟡 hold/hawkish   🔴 easing
4. Unemployment rate          🟢 <4.5%        🟡 4.5–6%         🔴 >6%
5. GDP annualised             🟢 >2%          🟡 0–2%           🔴 negative
6. Manufacturing PMI          🟢 >51          🟡 49–51          🔴 <49
7. Services PMI               🟢 >51          🟡 49–51          🔴 <49
8. Retail Sales MoM           🟢 positive     🟡 flat/missing   🔴 negative
9. Trade Balance              🟢 surplus      🟡 narrowing      🔴 widening deficit

Signal bands: ≥7.0 → 🟢 Strong Long | 5.0–6.9 → 🟡 Mild Long | 3.0–4.9 → 🟡 Neutral | <3.0 → 🔴 Strong Short

Always use the most recent official data releases. Note clearly when data is unavailable (score 🟡 Neutral).
"""

USER_PROMPT_TEMPLATE = """Today is {date}. Research the latest macro data for all 8 major currencies
(USD, AUD, GBP, JPY, EUR, CHF, NZD, CAD) and produce the full analysis report below.

Search for:
- Latest central bank rate decisions and forward guidance (Fed, RBA, BoE, BoJ, ECB, SNB, RBNZ, BoC)
- Latest CPI/inflation prints (YoY)
- Latest unemployment rates
- Latest GDP growth figures (annualised)
- Latest Manufacturing and Services PMI readings (S&P Global / ISM)
- Latest retail sales (MoM)
- Latest trade balance data
- Any major macro events from the past week

Output the report in EXACTLY this format (fill every cell, every section):

# FX Fundamental Analysis — {date}

## Summary Watchlist

| Currency | Rate (%) | Target (%) | CPI YoY (%) | CPI vs Target | Rate Bias | Unemployment | GDP ann. | Mfg PMI | Svcs PMI | Retail MoM | Trade Balance | Score /9 | Signal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| USD | … | … | … | 🟢/🟡/🔴 | 🟢/🟡/🔴 … | 🟢/🟡/🔴 …% | 🟢/🟡/🔴 …% | 🟢/🟡/🔴 … | 🟢/🟡/🔴 … | 🟢/🟡/🔴 … | 🟢/🟡/🔴 … | **x.x** | 🟢/🟡/🔴 … |
| AUD | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| GBP | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| JPY | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| EUR | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| CHF | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| NZD | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |
| CAD | … | … | … | … | … | … | … | … | … | … | … | **x.x** | … |

---

## Top Pairs

| Rank | Pair | Direction | Base Bias | Quote Bias | Conviction |
|---|---|---|---|---|---|
| 1 | **XXX/YYY** | LONG/SHORT | … (x.x) | … (x.x) | ⭐⭐⭐ Very High / ⭐⭐ Medium-High / ⭐ Medium |
| 2 | … | … | … | … | … |
| 3 | … | … | … | … | … |
| 4 | … | … | … | … | … |
| 5 | … | … | … | … | … |

> **Note on [currency if relevant]:** [any carry/rate-differential caveats]

---

## Per-Currency Detail

**USD — [Signal] (x.x/9)**
[2–4 paragraphs: current rate, inflation trajectory, CB guidance, key data, risks]

**AUD — [Signal] (x.x/9)**
[2–4 paragraphs]

**GBP — [Signal] (x.x/9)**
[2–4 paragraphs]

**JPY — [Signal] (x.x/9) — [carry caveat if applicable]**
[2–4 paragraphs]

**EUR — [Signal] (x.x/9)**
[2–4 paragraphs]

**CHF — [Signal] (x.x/9) — [structural note if applicable]**
[2–4 paragraphs]

**NZD — [Signal] (x.x/9)**
[2–4 paragraphs]

**CAD — [Signal] (x.x/9)**
[2–4 paragraphs]

---

## Data Notes

- All data as of {date}; [note which CPI/PMI figures are latest available]
- [Note any missing data scored as Neutral]
- [Note any major structural factors affecting all 8 currencies]
- Next key releases: [list upcoming CB decisions and major data releases in the next 2 weeks]

## Sources

- [Source 1 with URL]
- [Source 2 with URL]
- [… list all sources consulted]
"""


def generate_analysis() -> str:
    client = anthropic.Anthropic()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = Path(__file__).parent.parent / "analysis" / f"{today}.md"

    if output_path.exists():
        print(f"Analysis for {today} already exists at {output_path}, skipping.")
        return str(output_path)

    print(f"Generating FX analysis for {today} …")

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=8192,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        tools=[{"type": "web_search_20260209", "name": "web_search"}],
        messages=[{"role": "user", "content": USER_PROMPT_TEMPLATE.format(date=today)}],
    ) as stream:
        final = stream.get_final_message()

    analysis_text = ""
    for block in final.content:
        if block.type == "text":
            analysis_text += block.text

    if not analysis_text.strip():
        print("ERROR: Claude returned no text content.", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(analysis_text, encoding="utf-8")
    print(f"Saved: {output_path}")
    return str(output_path)


if __name__ == "__main__":
    generate_analysis()
