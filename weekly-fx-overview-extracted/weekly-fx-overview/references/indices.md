# Stock Index Reference — Weekly FX Overview

One index per currency in the 19-currency basket.

| Currency | Country | Index Name | Ticker | Exchange | Notes |
|----------|---------|-----------|--------|----------|-------|
| USD | United States | S&P 500 | SPX | NYSE/NASDAQ | Primary US benchmark |
| USD | United States | S&P 100 | OEX | NYSE | Large-cap subset of S&P 500 |
| EUR | Euro Area | Euro Stoxx 50 | SX5E | Euronext | Pan-eurozone blue chips |
| EUR | Euro Area | DAX | DAX | Frankfurt | German benchmark — often used as EUR proxy |
| GBP | United Kingdom | FTSE 100 | UKX | London | UK large-cap benchmark |
| JPY | Japan | Nikkei 225 | NI225 | Tokyo | Japan's primary benchmark |
| AUD | Australia | ASX 200 | AS51 | Sydney | Australian benchmark |
| NZD | New Zealand | NZX 50 | NZ50 | Wellington | New Zealand benchmark |
| CAD | Canada | TSX Composite | OSPTX | Toronto | Canadian benchmark |
| CHF | Switzerland | SMI | SMI | Zurich | Swiss Market Index (20 largest) |
| CNY | China | Shanghai Composite | SHCOMP | Shanghai | Mainland China benchmark |
| INR | India | Nifty 50 | NIFTY | NSE | Indian benchmark |
| BRL | Brazil | Ibovespa | IBOV | B3 São Paulo | Brazilian benchmark |
| MXN | Mexico | IPC | MXX | BMV Mexico City | Mexican benchmark |
| NOK | Norway | OBX | OBX | Oslo | Norway's top 25 liquid stocks |
| SEK | Sweden | OMX Stockholm 30 | OMX | Nasdaq Stockholm | Sweden's 30 most-traded stocks |
| DKK | Denmark | OMX Copenhagen 20 | OMXC20 | Nasdaq Copenhagen | Denmark's 20 largest stocks |
| PLN | Poland | WIG20 | WIG20 | Warsaw | Poland's top 20 blue chips |
| HUF | Hungary | BUX | BUX | Budapest | Hungary's benchmark index |
| SGD | Singapore | Straits Times Index | STI | SGX | Singapore's 30 largest stocks |
| ILS | Israel | TA-125 | TA125 | Tel Aviv | Israel's 125 largest companies |

## Data Sources

- Primary: `https://tradingeconomics.com/{country}/stock-market`
- Secondary: Yahoo Finance, Bloomberg, Reuters
- Search template: `"{index name} weekly close {date} performance"`
