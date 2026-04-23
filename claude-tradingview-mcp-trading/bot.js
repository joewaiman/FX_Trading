/**
 * FX Trading Bot — Claude + OANDA/MetaTrader data + IB/FXCM/MT execution
 *
 * Runs hourly. For each pair in the watchlist:
 *   1. Fundamental pre-screen  — reads fundamental-scores.json (populated by fx-fundamental-analysis skill)
 *   2. Multi-timeframe check   — RSI(14) + SMA(40) + SMA(60) across Monthly, Weekly, Daily, 4H
 *   3. Execute                 — via IB, FXCM, or MetaTrader if all conditions pass
 *   4. Log                     — trades.csv (tax-ready) + safety-check-log.json (full decision audit)
 *
 * Local:  node bot.js
 * Cloud:  deploy to Railway — set env vars, cron runs automatically
 */

import "dotenv/config";
import { readFileSync, writeFileSync, existsSync, appendFileSync } from "fs";

// ─── Config ──────────────────────────────────────────────────────────────────

const CONFIG = {
  dataSource: process.env.DATA_SOURCE || "oanda",   // oanda | metatrader
  broker: process.env.BROKER || "ib",               // ib | fxcm | metatrader
  portfolioValue: parseFloat(process.env.PORTFOLIO_VALUE_USD || "10000"),
  maxTradeSizeUSD: parseFloat(process.env.MAX_TRADE_SIZE_USD || "1000"),
  maxTradesPerDay: parseInt(process.env.MAX_TRADES_PER_DAY || "5"),
  riskPerTrade: parseFloat(process.env.RISK_PER_TRADE || "0.01"),
  paperTrading: process.env.PAPER_TRADING !== "false",
  oanda: {
    apiKey: process.env.OANDA_API_KEY,
    accountId: process.env.OANDA_ACCOUNT_ID,
    baseUrl: process.env.OANDA_BASE_URL || "https://api-fxpractice.oanda.com",
  },
  ib: {
    baseUrl: process.env.IB_BASE_URL || "https://localhost:5000/v1/api",
    accountId: process.env.IB_ACCOUNT_ID,
  },
  fxcm: {
    apiKey: process.env.FXCM_API_KEY,
    accountId: process.env.FXCM_ACCOUNT_ID,
    baseUrl: process.env.FXCM_BASE_URL || "https://api-demo.fxcm.com",
  },
  mt: {
    baseUrl: process.env.MT_REST_URL || "http://localhost:8080",
    apiKey: process.env.MT_API_KEY,
  },
};

const TIMEFRAMES = ["M", "W", "D", "H4"];
const LOG_FILE = "safety-check-log.json";
const CSV_FILE = "trades.csv";

// ─── Onboarding ───────────────────────────────────────────────────────────────

function checkOnboarding() {
  if (!existsSync(".env")) {
    console.log("\n⚠️  No .env file found. Copy .env.example to .env and fill in your credentials.\n");
    process.exit(0);
  }

  if (!existsSync("fundamental-scores.json")) {
    console.log("\n⚠️  fundamental-scores.json not found.");
    console.log("   Run the fx-fundamental-analysis skill first to generate scores,");
    console.log("   or copy fundamental-scores.json.example to fundamental-scores.json.\n");
    process.exit(0);
  }

  const csvPath = new URL("trades.csv", import.meta.url).pathname;
  console.log(`\n📄 Trade log: ${csvPath}\n`);
}

// ─── Fundamental Pre-Screen ───────────────────────────────────────────────────

const BIAS_SCORE = {
  "Strong Long":  2,
  "Mild Long":    1,
  "Neutral":      0,
  "Mild Short":  -1,
  "Strong Short": -2,
};

function loadFundamentalScores() {
  return JSON.parse(readFileSync("fundamental-scores.json", "utf8"));
}

function fundamentalPreScreen(baseCcy, quoteCcy, scores) {
  const baseEntry = scores[baseCcy];
  const quoteEntry = scores[quoteCcy];

  if (!baseEntry || !quoteEntry) {
    return { pass: false, reason: `No score for ${baseCcy} or ${quoteCcy}` };
  }

  const baseVal  = BIAS_SCORE[baseEntry.bias]  ?? 0;
  const quoteVal = BIAS_SCORE[quoteEntry.bias] ?? 0;
  const diff = baseVal - quoteVal;

  // Long pair: base strong/mild long, quote neutral or weaker, net positive diff
  if (baseVal >= 1 && quoteVal <= 0 && diff >= 1) {
    return {
      pass: true,
      direction: "long",
      reason: `${baseCcy} ${baseEntry.bias} (${baseVal > 0 ? "+" : ""}${baseVal}) vs ${quoteCcy} ${quoteEntry.bias} (${quoteVal}) — diff ${diff > 0 ? "+" : ""}${diff}`,
    };
  }

  // Short pair: quote strong/mild long, base neutral or weaker
  if (quoteVal >= 1 && baseVal <= 0 && diff <= -1) {
    return {
      pass: true,
      direction: "short",
      reason: `${quoteCcy} ${quoteEntry.bias} (${quoteVal > 0 ? "+" : ""}${quoteVal}) vs ${baseCcy} ${baseEntry.bias} (${baseVal}) — diff ${Math.abs(diff)}`,
    };
  }

  return {
    pass: false,
    reason: `${baseCcy} ${baseEntry.bias} vs ${quoteCcy} ${quoteEntry.bias} — no qualifying bias differential`,
  };
}

// ─── Indicator Calculations ───────────────────────────────────────────────────

function calcSMA(closes, period) {
  if (closes.length < period) return null;
  const slice = closes.slice(-period);
  return slice.reduce((a, b) => a + b, 0) / period;
}

function calcRSI(closes, period = 14) {
  if (closes.length < period + 1) return null;
  let gains = 0, losses = 0;
  for (let i = closes.length - period; i < closes.length; i++) {
    const diff = closes[i] - closes[i - 1];
    if (diff > 0) gains += diff;
    else losses -= diff;
  }
  const avgGain = gains / period;
  const avgLoss = losses / period;
  if (avgLoss === 0) return 100;
  return 100 - 100 / (1 + avgGain / avgLoss);
}

// ─── Multi-Timeframe Safety Check ─────────────────────────────────────────────

function runMultiTFCheck(tfData, direction) {
  const results = [];
  const tfLabels = { M: "Monthly", W: "Weekly", D: "Daily", H4: "4-Hour" };

  const check = (label, required, actual, pass) => {
    results.push({ label, required, actual, pass });
    console.log(`  ${pass ? "✅" : "🚫"} ${label}`);
    console.log(`     Required: ${required} | Actual: ${actual}`);
  };

  for (const tf of TIMEFRAMES) {
    const data = tfData[tf];
    const label = tfLabels[tf] || tf;

    if (!data) {
      results.push({ label: `${label} data`, required: "available", actual: "missing", pass: false });
      console.log(`  🚫 ${label} — no data`);
      continue;
    }

    const { price, sma40, sma60, rsi14 } = data;

    if (tf === "H4") {
      // Entry timeframe: RSI pullback/extension signal
      if (direction === "long") {
        check(
          `${label} RSI(14) pullback — entry in uptrend`,
          "< 45",
          rsi14 != null ? rsi14.toFixed(2) : "N/A",
          rsi14 != null && rsi14 < 45
        );
      } else {
        check(
          `${label} RSI(14) extension — entry in downtrend`,
          "> 55",
          rsi14 != null ? rsi14.toFixed(2) : "N/A",
          rsi14 != null && rsi14 > 55
        );
      }
    } else {
      // Trend timeframes: price and SMA alignment
      const fmt = (v) => v != null ? v.toFixed(5) : "N/A";
      if (direction === "long") {
        check(`${label} price above SMA(40)`, `> ${fmt(sma40)}`, fmt(price), sma40 != null && price > sma40);
        check(`${label} price above SMA(60)`, `> ${fmt(sma60)}`, fmt(price), sma60 != null && price > sma60);
        check(`${label} SMA(40) > SMA(60) — uptrend structure`, `SMA40 > SMA60`, `${fmt(sma40)} vs ${fmt(sma60)}`, sma40 != null && sma60 != null && sma40 > sma60);
      } else {
        check(`${label} price below SMA(40)`, `< ${fmt(sma40)}`, fmt(price), sma40 != null && price < sma40);
        check(`${label} price below SMA(60)`, `< ${fmt(sma60)}`, fmt(price), sma60 != null && price < sma60);
        check(`${label} SMA(40) < SMA(60) — downtrend structure`, `SMA40 < SMA60`, `${fmt(sma40)} vs ${fmt(sma60)}`, sma40 != null && sma60 != null && sma40 < sma60);
      }
    }
  }

  return { results, allPass: results.every(r => r.pass) };
}

// ─── Data Sources ──────────────────────────────────────────────────────────────

const OANDA_GRANULARITY = { M: "M", W: "W", D: "D", H4: "H4" };
const MT_GRANULARITY    = { M: "43200", W: "10080", D: "1440", H4: "240" };

// Candle counts — enough for SMA(60) with headroom
const CANDLE_COUNT = { M: 80, W: 80, D: 80, H4: 100 };

async function fetchOandaCandles(instrument, granularity, count) {
  const oandaInstrument = instrument.replace("/", "_");
  const url = `${CONFIG.oanda.baseUrl}/v3/instruments/${oandaInstrument}/candles?granularity=${granularity}&count=${count}&price=M`;

  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${CONFIG.oanda.apiKey}` },
  });
  if (!res.ok) throw new Error(`OANDA ${res.status}: ${instrument} ${granularity}`);
  const data = await res.json();

  return data.candles
    .filter(c => c.complete)
    .map(c => ({
      time: new Date(c.time).getTime(),
      open:   parseFloat(c.mid.o),
      high:   parseFloat(c.mid.h),
      low:    parseFloat(c.mid.l),
      close:  parseFloat(c.mid.c),
      volume: c.volume,
    }));
}

async function fetchMTCandles(instrument, granularity, count) {
  const symbol = instrument.replace("/", "");
  const url = `${CONFIG.mt.baseUrl}/candles?symbol=${symbol}&timeframe=${granularity}&count=${count}`;

  const res = await fetch(url, {
    headers: { "X-API-Key": CONFIG.mt.apiKey },
  });
  if (!res.ok) throw new Error(`MT ${res.status}: ${instrument} ${granularity}`);
  const data = await res.json();

  return data.candles.map(c => ({
    time: c.time, open: c.open, high: c.high, low: c.low, close: c.close, volume: c.volume,
  }));
}

async function fetchCandles(instrument, tf) {
  const count = CANDLE_COUNT[tf];
  if (CONFIG.dataSource === "oanda") {
    return fetchOandaCandles(instrument, OANDA_GRANULARITY[tf], count);
  }
  return fetchMTCandles(instrument, MT_GRANULARITY[tf], count);
}

async function fetchAllTimeframes(instrument) {
  const tfData = {};
  for (const tf of TIMEFRAMES) {
    try {
      const candles = await fetchCandles(instrument, tf);
      const closes = candles.map(c => c.close);
      tfData[tf] = {
        price: closes[closes.length - 1],
        sma40: calcSMA(closes, 40),
        sma60: calcSMA(closes, 60),
        rsi14: calcRSI(closes, 14),
      };
    } catch (err) {
      console.log(`  ⚠️  ${tf} fetch failed: ${err.message}`);
      tfData[tf] = null;
    }
  }
  return tfData;
}

// ─── Broker Execution ──────────────────────────────────────────────────────────

// IB contract IDs for FX pairs (extend as needed)
const IB_CONIDS = {
  "EUR/USD": 12087792, "GBP/USD": 12087797, "USD/JPY": 15016062,
  "AUD/USD": 14433401, "NZD/USD": 39408899, "USD/CAD": 15016015,
  "USD/CHF": 15016017, "EUR/GBP": 12087793, "EUR/JPY": 12087794,
  "EUR/AUD": 14433406, "EUR/NZD": 14433404, "EUR/CAD": 14433408,
  "EUR/CHF": 12087795, "GBP/JPY": 12087800, "GBP/AUD": 14433410,
  "GBP/NZD": 14433412, "GBP/CAD": 14433414, "GBP/CHF": 14433416,
  "AUD/JPY": 14433403, "AUD/NZD": 14433418, "AUD/CAD": 14433420,
  "AUD/CHF": 14433422, "NZD/JPY": 39408902, "NZD/CAD": 39408904,
  "NZD/CHF": 39408906, "CAD/JPY": 15016020, "CAD/CHF": 15016022,
  "CHF/JPY": 15016024, "USD/NOK": 37928772, "USD/SEK": 37928774,
  "USD/DKK": 37928770, "USD/SGD": 37928776, "USD/MXN": 15016060,
  "USD/PLN": 15016056, "USD/HUF": 15016028, "USD/CNH": 106648028,
};

function calcLotSize(sizeUSD, price) {
  // Round to nearest 1,000 units (micro lot), minimum 1,000
  const units = Math.floor((sizeUSD / price) / 1000) * 1000;
  return Math.max(units, 1000);
}

async function placeIBOrder(instrument, direction, sizeUSD, price) {
  const conid = IB_CONIDS[instrument];
  if (!conid) throw new Error(`No IB contract ID for ${instrument}`);
  const quantity = calcLotSize(sizeUSD, price);

  const res = await fetch(`${CONFIG.ib.baseUrl}/iserver/account/${CONFIG.ib.accountId}/orders`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify([{
      conid,
      orderType: "MKT",
      side: direction === "long" ? "BUY" : "SELL",
      quantity,
      tif: "GTC",
    }]),
  });
  if (!res.ok) throw new Error(`IB order failed: ${res.status}`);
  const data = await res.json();
  return { orderId: data[0]?.order_id };
}

async function placeFXCMOrder(instrument, direction, sizeUSD, price) {
  const symbol = instrument.replace("/", "");
  const quantity = calcLotSize(sizeUSD, price);

  const body = new URLSearchParams({
    account_id: CONFIG.fxcm.accountId,
    symbol,
    is_buy: direction === "long" ? "true" : "false",
    rate: 0,
    amount: quantity,
    order_type: "AtMarket",
    time_in_force: "GTC",
  });

  const res = await fetch(`${CONFIG.fxcm.baseUrl}/trading/open_trade`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${CONFIG.fxcm.apiKey}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });
  if (!res.ok) throw new Error(`FXCM order failed: ${res.status}`);
  const data = await res.json();
  return { orderId: data.data?.orderId };
}

async function placeMTOrder(instrument, direction, sizeUSD, price) {
  const symbol = instrument.replace("/", "");
  const lots = (calcLotSize(sizeUSD, price) / 100000).toFixed(2);

  const res = await fetch(`${CONFIG.mt.baseUrl}/order`, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-API-Key": CONFIG.mt.apiKey },
    body: JSON.stringify({ symbol, type: direction === "long" ? "buy" : "sell", volume: parseFloat(lots), comment: "fx-bot" }),
  });
  if (!res.ok) throw new Error(`MT order failed: ${res.status}`);
  const data = await res.json();
  return { orderId: data.ticket };
}

async function placeOrder(instrument, direction, sizeUSD, price) {
  switch (CONFIG.broker) {
    case "ib":          return placeIBOrder(instrument, direction, sizeUSD, price);
    case "fxcm":        return placeFXCMOrder(instrument, direction, sizeUSD, price);
    case "metatrader":  return placeMTOrder(instrument, direction, sizeUSD, price);
    default: throw new Error(`Unknown broker: ${CONFIG.broker}`);
  }
}

// ─── Trade Log ─────────────────────────────────────────────────────────────────

function loadLog() {
  if (!existsSync(LOG_FILE)) return { trades: [] };
  return JSON.parse(readFileSync(LOG_FILE, "utf8"));
}

function saveLog(log) {
  writeFileSync(LOG_FILE, JSON.stringify(log, null, 2));
}

function countTodaysTrades(log) {
  const today = new Date().toISOString().slice(0, 10);
  return log.trades.filter(t => t.timestamp.startsWith(today) && t.orderPlaced).length;
}

// ─── Tax CSV ───────────────────────────────────────────────────────────────────

const CSV_HEADERS = [
  "Date", "Time (UTC)", "Broker", "Instrument", "Direction",
  "Units", "Price", "Trade USD", "Risk USD", "Order ID", "Mode", "Notes",
].join(",");

function initCsv() {
  if (!existsSync(CSV_FILE)) {
    writeFileSync(CSV_FILE, CSV_HEADERS + "\n");
    console.log(`📄 Created ${CSV_FILE}`);
  }
}

function writeTradeCsv(entry) {
  const now  = new Date(entry.timestamp);
  const date = now.toISOString().slice(0, 10);
  const time = now.toISOString().slice(11, 19);
  const mode = !entry.allPass ? "BLOCKED" : entry.paperTrading ? "PAPER" : "LIVE";

  let notes = "";
  if (!entry.allPass) {
    const failed = (entry.conditions || []).filter(c => !c.pass).map(c => c.label);
    notes = `Failed: ${failed.join("; ")}`;
  } else if (entry.error) {
    notes = `Order error: ${entry.error}`;
  } else {
    notes = "All conditions met";
  }

  const row = [
    date, time,
    CONFIG.broker,
    entry.instrument,
    entry.direction || "",
    entry.lotSize || "",
    entry.price?.toFixed(5) ?? "",
    entry.tradeSize?.toFixed(2) ?? "",
    entry.riskUSD?.toFixed(2) ?? "",
    entry.orderId || (entry.allPass ? "" : "BLOCKED"),
    mode,
    `"${notes}"`,
  ].join(",");

  appendFileSync(CSV_FILE, row + "\n");
}

function generateTaxSummary() {
  if (!existsSync(CSV_FILE)) { console.log("No trades.csv found."); return; }
  const lines = readFileSync(CSV_FILE, "utf8").trim().split("\n");
  const rows  = lines.slice(1).map(l => l.split(","));
  const live    = rows.filter(r => r[10] === "LIVE");
  const paper   = rows.filter(r => r[10] === "PAPER");
  const blocked = rows.filter(r => r[10] === "BLOCKED");
  const vol  = live.reduce((s, r) => s + parseFloat(r[7] || 0), 0);

  console.log("\n── Tax Summary ──────────────────────────────────────────\n");
  console.log(`  Decisions logged  : ${rows.length}`);
  console.log(`  Live trades       : ${live.length}`);
  console.log(`  Paper trades      : ${paper.length}`);
  console.log(`  Blocked           : ${blocked.length}`);
  console.log(`  Total volume (USD): $${vol.toFixed(2)}`);
  console.log(`\n  Full record: ${CSV_FILE}\n`);
}

// ─── Main ──────────────────────────────────────────────────────────────────────

async function run() {
  checkOnboarding();
  initCsv();

  console.log("═══════════════════════════════════════════════════════════");
  console.log(`  FX Bot — ${CONFIG.dataSource.toUpperCase()} data → ${CONFIG.broker.toUpperCase()}`);
  console.log(`  ${new Date().toISOString()}`);
  console.log(`  Mode: ${CONFIG.paperTrading ? "📋 PAPER TRADING" : "🔴 LIVE TRADING"}`);
  console.log("═══════════════════════════════════════════════════════════");

  const rules       = JSON.parse(readFileSync("rules.json", "utf8"));
  const fundamentals = loadFundamentalScores();
  const log         = loadLog();

  const todayCount = countTodaysTrades(log);
  if (todayCount >= CONFIG.maxTradesPerDay) {
    console.log(`\n🚫 Daily trade cap reached: ${todayCount}/${CONFIG.maxTradesPerDay}. Stopping.`);
    return;
  }

  console.log(`\nStrategy : ${rules.strategy.name}`);
  console.log(`Pairs     : ${rules.watchlist.length}`);
  console.log(`Trades    : ${todayCount}/${CONFIG.maxTradesPerDay} today\n`);

  for (const instrument of rules.watchlist) {
    const [baseCcy, quoteCcy] = instrument.split("/");

    console.log(`\n─── ${instrument} ${"─".repeat(Math.max(0, 47 - instrument.length))}`);

    // Step 1: Fundamental pre-screen
    const fundamental = fundamentalPreScreen(baseCcy, quoteCcy, fundamentals.scores);
    if (!fundamental.pass) {
      console.log(`  ⏭  Skipped — ${fundamental.reason}`);
      continue;
    }

    const { direction } = fundamental;
    console.log(`  ✅ Fundamental: ${fundamental.reason}`);
    console.log(`  Direction: ${direction.toUpperCase()}`);

    // Step 2: Multi-timeframe data
    console.log(`  Fetching M / W / D / H4 from ${CONFIG.dataSource.toUpperCase()}...`);
    const tfData = await fetchAllTimeframes(instrument);

    const price = tfData["H4"]?.price;
    if (!price) { console.log("  ❌ No 4H price — skipping"); continue; }
    console.log(`  4H price: ${price.toFixed(5)}`);

    // Step 3: Technical check
    console.log(`\n── Technical check (${direction.toUpperCase()}) ────────────────────────────`);
    const { results, allPass } = runMultiTFCheck(tfData, direction);

    const riskUSD  = CONFIG.portfolioValue * CONFIG.riskPerTrade;
    const tradeSize = Math.min(riskUSD, CONFIG.maxTradeSizeUSD);
    const lotSize  = calcLotSize(tradeSize, price);

    const logEntry = {
      timestamp: new Date().toISOString(),
      instrument,
      direction,
      price,
      fundamentalReason: fundamental.reason,
      indicators: Object.fromEntries(
        Object.entries(tfData)
          .filter(([, v]) => v)
          .map(([tf, v]) => [tf, { price: v.price, sma40: v.sma40, sma60: v.sma60, rsi14: v.rsi14 }])
      ),
      conditions: results,
      allPass,
      tradeSize,
      riskUSD,
      lotSize,
      orderPlaced: false,
      orderId: null,
      paperTrading: CONFIG.paperTrading,
    };

    console.log("\n── Decision ─────────────────────────────────────────────\n");

    if (!allPass) {
      const failed = results.filter(r => !r.pass).map(r => r.label);
      console.log(`🚫 BLOCKED — ${failed.length} condition(s) failed:`);
      failed.forEach(f => console.log(`   - ${f}`));
    } else {
      console.log(`✅ ALL CONDITIONS MET`);

      if (CONFIG.paperTrading) {
        console.log(`\n📋 PAPER — ${direction.toUpperCase()} ${instrument}  ${lotSize.toLocaleString()} units  ~$${tradeSize.toFixed(2)}`);
        logEntry.orderPlaced = true;
        logEntry.orderId = `PAPER-${Date.now()}`;
      } else {
        console.log(`\n🔴 LIVE — ${direction.toUpperCase()} ${instrument}  ${lotSize.toLocaleString()} units  via ${CONFIG.broker.toUpperCase()}`);
        try {
          const order = await placeOrder(instrument, direction, tradeSize, price);
          logEntry.orderPlaced = true;
          logEntry.orderId = order.orderId;
          console.log(`✅ ORDER PLACED — ${order.orderId}`);
        } catch (err) {
          console.log(`❌ ORDER FAILED — ${err.message}`);
          logEntry.error = err.message;
        }
      }
    }

    log.trades.push(logEntry);
    writeTradeCsv(logEntry);
  }

  saveLog(log);
  console.log(`\nLog saved → ${LOG_FILE}`);
  console.log("═══════════════════════════════════════════════════════════\n");
}

if (process.argv.includes("--tax-summary")) {
  generateTaxSummary();
} else {
  run().catch(err => {
    console.error("Bot error:", err);
    process.exit(1);
  });
}
