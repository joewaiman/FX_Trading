# Data Sources — Weekly FX Overview

## Economic Calendar
- Primary: `https://tradingeconomics.com/calendar`
- Secondary: `https://investing.com/economic-calendar`
- Search: `"economic calendar week of {date} {year}"`

## FX Performance vs USD
- Trading Economics: `https://tradingeconomics.com/{country}/currency`
- Search template: `"{currency} USD weekly performance {date range}"`
- Pairs format: EURUSD, GBPUSD, USDJPY (note: JPY, CHF, CAD etc. are USD/{CCY})

## Economic Highlights by Country
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

## Stock Indices
- Trading Economics: `https://tradingeconomics.com/{country}/stock-market`
- Search: `"{index name} close {friday date}"`

## GitHub Push
- Repo: `joewaiman/FX_Trading`
- Folder: `weekly-reports/`
- CLI: `gh api repos/joewaiman/FX_Trading/contents/weekly-reports/{filename}`
