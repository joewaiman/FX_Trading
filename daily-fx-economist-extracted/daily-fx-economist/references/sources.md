# Data Sources — Daily FX Economist Briefing

## Economic Calendar (Today's Releases)
- Primary: `https://tradingeconomics.com/calendar`
- Secondary: `https://investing.com/economic-calendar`
- Search: `"economic calendar {date} {year} releases"`

Filter to today's date. Prioritise: rate decisions > CPI > employment > GDP > PMI > retail sales.

---

## Overnight Economic Releases (Past 24h)
- Trading Economics by country (see table below)
- Search: `"{country} {indicator} {date} actual result"`
- Search: `"{country} economic data {date} {year}"`

**Country indicator pages:**
| Currency | Trading Economics URL |
|----------|-----------------------|
| USD | tradingeconomics.com/united-states/indicators |
| EUR | tradingeconomics.com/euro-area/indicators |
| GBP | tradingeconomics.com/united-kingdom/indicators |
| JPY | tradingeconomics.com/japan/indicators |
| AUD | tradingeconomics.com/australia/indicators |
| NZD | tradingeconomics.com/new-zealand/indicators |
| CAD | tradingeconomics.com/canada/indicators |
| CHF | tradingeconomics.com/switzerland/indicators |
| CNY | tradingeconomics.com/china/indicators |
| INR | tradingeconomics.com/india/indicators |
| BRL | tradingeconomics.com/brazil/indicators |
| MXN | tradingeconomics.com/mexico/indicators |
| NOK | tradingeconomics.com/norway/indicators |
| SEK | tradingeconomics.com/sweden/indicators |
| DKK | tradingeconomics.com/denmark/indicators |
| PLN | tradingeconomics.com/poland/indicators |
| HUF | tradingeconomics.com/hungary/indicators |
| SGD | tradingeconomics.com/singapore/indicators |
| ILS | tradingeconomics.com/israel/indicators |

---

## 24h FX Moves vs USD
- Trading Economics: `https://tradingeconomics.com/{country}/currency`
- Search: `"{currency pair} 24 hour change {date}"`

**Quote convention (all expressed as currency strength vs USD):**
| Direct (CCY/USD) | Inverted (USD/CCY — negate for CCY strength) |
|-----------------|---------------------------------------------|
| EURUSD, GBPUSD, AUDUSD, NZDUSD | USDJPY, USDCHF, USDCAD, USDCNY, USDINR, USDBRL, USDMXN, USDNOK, USDSEK, USDDKK, USDPLN, USDHUF, USDSGD, USDILS |

For inverted pairs: if USDJPY +0.3%, JPY is −0.3% vs USD.

---

## Central Bank Statements & Policy News
- Search: `"{central bank name} statement {month} {year}"`
- Search: `"{central bank name} rate decision {date}"`
- Fed: federalreserve.gov/newsevents
- ECB: ecb.europa.eu/press/pr
- BoE: bankofengland.co.uk/news

---

## GitHub Push
- Repo: `joewaiman/FX_Trading`
- Folder: `daily-briefings/`
- CLI: `gh api repos/joewaiman/FX_Trading/contents/daily-briefings/{filename}`
