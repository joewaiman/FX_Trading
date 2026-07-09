# FX Fundamental Analysis — Data Sources

## Trading Economics URLs

Use `web_fetch` on these URLs. Replace `{country}` with the lowercase country name.

### Country Indicators Dashboard — Full 19-Currency Universe

**G8 Currencies:**
```
https://tradingeconomics.com/united-states/indicators      (USD)
https://tradingeconomics.com/euro-area/indicators          (EUR)
https://tradingeconomics.com/united-kingdom/indicators     (GBP)
https://tradingeconomics.com/japan/indicators              (JPY)
https://tradingeconomics.com/australia/indicators          (AUD)
https://tradingeconomics.com/new-zealand/indicators        (NZD)
https://tradingeconomics.com/canada/indicators             (CAD)
https://tradingeconomics.com/switzerland/indicators        (CHF)
```

**Extended Universe (SEK, NOK, SGD, PLN, HUF, DKK, MXN, INR, CNY, BRL, ILS):**
```
https://tradingeconomics.com/sweden/indicators             (SEK)
https://tradingeconomics.com/norway/indicators             (NOK)
https://tradingeconomics.com/singapore/indicators          (SGD)
https://tradingeconomics.com/poland/indicators             (PLN)
https://tradingeconomics.com/hungary/indicators            (HUF)
https://tradingeconomics.com/denmark/indicators            (DKK)
https://tradingeconomics.com/mexico/indicators             (MXN)
https://tradingeconomics.com/india/indicators              (INR)
https://tradingeconomics.com/china/indicators              (CNY)
https://tradingeconomics.com/brazil/indicators             (BRL)
https://tradingeconomics.com/israel/indicators             (ILS)
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
"{country} CPI inflation latest {current year}"
"{country} unemployment rate latest"
"{country} GDP growth Q{n} {current year}"
"{country} manufacturing PMI {month} {current year}"
"{country} services PMI {month} {current year}"
"{country} retail sales {month} {current year}"
"{country} trade balance latest"
"{central bank name} rate decision {current year} outlook"
"MAS monetary policy statement {current year} S$NEER slope"  (SGD only)
"PBOC fixing rate yuan {current year}"                        (CNY only)
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
| SEK | S&P Global Sweden PMI | Mfg + Services available |
| NOK | S&P Global Norway PMI | Mfg primarily; services less regular |
| SGD | S&P Global Singapore PMI | Mfg PMI well-covered; services patchy |
| PLN | S&P Global Poland Manufacturing PMI | Manufacturing only (no services PMI) |
| HUF | S&P Global Hungary Manufacturing PMI | Manufacturing only (no services PMI) |
| DKK | S&P Global Denmark PMI | Limited — use EUR as proxy if unavailable |
| MXN | S&P Global Mexico Manufacturing PMI | Manufacturing only |
| INR | S&P Global India PMI | Both Mfg and Services available |
| CNY | Caixin China PMI (S&P Global) | Use Caixin (private sector), not NBS official PMI, for market signals |
| BRL | S&P Global Brazil Manufacturing PMI | Manufacturing only; services less covered |
| ILS | S&P Global Israel PMI | Manufacturing; services less regular |

> **If PMI data is unavailable** for an extended currency, mark the field as N/A and adjust the
> score denominator accordingly (score out of 8 instead of 9 if one PMI is missing, 7 if both missing).

## Economic Calendar

For upcoming releases: `https://tradingeconomics.com/calendar`
For consensus forecasts: `https://investing.com/economic-calendar`
