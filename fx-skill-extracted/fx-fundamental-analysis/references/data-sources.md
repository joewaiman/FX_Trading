# FX Fundamental Analysis — Data Sources

## Trading Economics URLs

Use `web_fetch` on these URLs. Replace `{country}` with the lowercase country name.

### Country Indicators Dashboard
```
https://tradingeconomics.com/united-states/indicators
https://tradingeconomics.com/euro-area/indicators
https://tradingeconomics.com/united-kingdom/indicators
https://tradingeconomics.com/japan/indicators
https://tradingeconomics.com/australia/indicators
https://tradingeconomics.com/new-zealand/indicators
https://tradingeconomics.com/canada/indicators
https://tradingeconomics.com/switzerland/indicators
```

### Specific Indicator Pages
| Indicator | URL pattern |
|---|---|
| Inflation (CPI) | `tradingeconomics.com/{country}/inflation-cpi` |
| Interest Rate | `tradingeconomics.com/{country}/interest-rate` |
| Unemployment | `tradingeconomics.com/{country}/unemployment-rate` |
| GDP Growth | `tradingeconomics.com/{country}/gdp-growth` |
| Manufacturing PMI | `tradingeconomics.com/{country}/manufacturing-pmi` |
| Services PMI | `tradingeconomics.com/{country}/services-pmi` |
| Retail Sales MoM | `tradingeconomics.com/{country}/retail-sales` |
| Balance of Trade | `tradingeconomics.com/{country}/balance-of-trade` |

## Web Search Query Templates

Use these for `web_search` when you need the latest data:

```
"{country} CPI inflation latest 2025"
"{country} unemployment rate latest"
"{country} GDP growth Q{n} 2025"
"{country} manufacturing PMI {month} 2025"
"{country} services PMI {month} 2025"
"{country} retail sales {month} 2025"
"{country} trade balance latest"
"{central bank name} rate decision latest"
```

## Supplementary Sources

| Source | Use case |
|---|---|
| `reuters.com` | Breaking economic data, central bank statements |
| `bloomberg.com` | Rate expectations, analyst consensus |
| `investing.com/economic-calendar` | Upcoming data releases |
| Central bank websites (see central-banks.md) | Official rate statements, minutes |

## PMI Data Sources by Currency

| Currency | PMI Provider | Notes |
|---|---|---|
| USD | ISM (Institute for Supply Management) | More widely followed than S&P Global for USD |
| EUR | S&P Global / HCOB Eurozone PMI | Composite covers major EZ economies |
| GBP | S&P Global / CIPS UK PMI | |
| JPY | au Jibun Bank / S&P Global | |
| AUD | Judo Bank / S&P Global | |
| NZD | BNZ / BusinessNZ | Published monthly |
| CAD | S&P Global Canada PMI | |
| CHF | procure.ch PMI | Manufacturing only; limited services data |

## Economic Calendar

For upcoming releases: `https://tradingeconomics.com/calendar`
For consensus forecasts: `https://investing.com/economic-calendar`
