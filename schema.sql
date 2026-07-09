-- ══════════════════════════════════════════════════════════════
-- FX Trading Database Schema
-- Run once in Supabase SQL Editor (Dashboard → SQL Editor → New query)
-- ══════════════════════════════════════════════════════════════

-- Enable UUID extension
create extension if not exists "uuid-ossp";


-- ─────────────────────────────────────────────
-- 1. FUNDAMENTAL ANALYSIS
--    One row per currency per analysis run
-- ─────────────────────────────────────────────
create table if not exists fundamental_analysis (
    id                  uuid primary key default uuid_generate_v4(),
    analysis_date       date not null,
    currency            varchar(6) not null,
    policy_rate         numeric,
    cpi_yoy             numeric,
    cpi_vs_target       varchar(10),   -- bullish / neutral / bearish
    rate_bias           varchar(10),   -- bullish / neutral / bearish
    unemployment        numeric,
    unemployment_score  varchar(10),
    gdp_qoq             numeric,
    gdp_score           varchar(10),
    pmi_manufacturing   numeric,
    pmi_services        numeric,
    retail_sales_mom    numeric,
    retail_sales_score  varchar(10),
    trade_balance       numeric,
    trade_balance_score varchar(10),
    te_commentary_score varchar(10),
    overall_score       integer,       -- 0–9
    overall_bias        varchar(20),   -- strong_bullish / mild_bullish / neutral / mild_bearish / strong_bearish
    notes               text,
    created_at          timestamptz default now()
);

create index if not exists idx_fa_currency_date
    on fundamental_analysis (currency, analysis_date desc);


-- ─────────────────────────────────────────────
-- 2. TECHNICAL ANALYSIS
--    One row per pair per analysis run
-- ─────────────────────────────────────────────
create table if not exists technical_analysis (
    id                uuid primary key default uuid_generate_v4(),
    analysis_date     date not null,
    pair              varchar(10) not null,
    weekly_channel    varchar(10),    -- bullish / bearish / sideways
    daily_channel     varchar(10),
    h4_channel        varchar(10),
    overall_bias      varchar(10),
    sma_20            numeric,
    sma_50            numeric,
    rsi_daily         numeric,
    rsi_h4            numeric,
    divergence        varchar(20),    -- none / bullish / bearish
    key_resistance_1  numeric,
    key_resistance_2  numeric,
    key_support_1     numeric,
    key_support_2     numeric,
    entry_zone        numeric,
    entry_pattern     varchar(30),    -- pin_bar / engulfing / inside_bar / none
    confluence_score  integer,        -- 0–5
    entry_status      varchar(20),    -- triggered / waiting / no_setup
    direction         varchar(5),     -- long / short
    entry_price       numeric,
    stop_loss         numeric,
    tp1               numeric,
    tp2               numeric,
    rr_tp1            numeric,
    rr_tp2            numeric,
    trade_status      varchar(20),    -- watching / active / closed / invalidated
    notes             text,
    created_at        timestamptz default now()
);

create index if not exists idx_ta_pair_date
    on technical_analysis (pair, analysis_date desc);


-- ─────────────────────────────────────────────
-- 3. TRADES (live)
--    One row per trade taken
-- ─────────────────────────────────────────────
create table if not exists trades (
    id                    uuid primary key default uuid_generate_v4(),
    technical_analysis_id uuid references technical_analysis(id),
    pair                  varchar(10) not null,
    direction             varchar(5),     -- long / short
    entry_date            timestamptz,
    entry_price           numeric,
    stop_loss             numeric,
    tp1                   numeric,
    tp2                   numeric,
    exit_date             timestamptz,
    exit_price            numeric,
    exit_reason           varchar(20),    -- tp1 / tp2 / stop / manual
    pips_result           numeric,
    rr_achieved           numeric,
    outcome               varchar(10),    -- win / loss / breakeven
    notes                 text,
    created_at            timestamptz default now()
);

create index if not exists idx_trades_pair
    on trades (pair, entry_date desc);

create index if not exists idx_trades_open
    on trades (exit_date) where exit_date is null;


-- ─────────────────────────────────────────────
-- 4. BACKTEST SESSIONS
--    One row per backtest run (metadata + aggregate stats)
-- ─────────────────────────────────────────────
create table if not exists backtest_sessions (
    id               uuid primary key default uuid_generate_v4(),
    created_date     date not null,
    pair             varchar(10),
    strategy_name    varchar(50),
    date_range_start date,
    date_range_end   date,
    timeframe        varchar(5),
    total_trades     integer,
    wins             integer,
    losses           integer,
    win_rate         numeric,          -- percentage, e.g. 64.3
    avg_rr_achieved  numeric,
    expectancy       numeric,          -- (win_rate * avg_win) - (loss_rate * avg_loss)
    notes            text,
    created_at       timestamptz default now()
);


-- ─────────────────────────────────────────────
-- 5. BACKTEST TRADES
--    One row per trade within a backtest
-- ─────────────────────────────────────────────
create table if not exists backtest_trades (
    id                   uuid primary key default uuid_generate_v4(),
    session_id           uuid references backtest_sessions(id),
    pair                 varchar(10),
    direction            varchar(5),
    entry_date           date,
    entry_price          numeric,
    stop_loss            numeric,
    tp1                  numeric,
    tp2                  numeric,
    exit_price           numeric,
    exit_reason          varchar(20),
    pips_result          numeric,
    rr_achieved          numeric,
    outcome              varchar(10),   -- win / loss / breakeven
    weekly_channel       varchar(10),
    daily_channel        varchar(10),
    h4_channel           varchar(10),
    entry_pattern        varchar(30),
    confluence_score     integer,
    fundamental_aligned  boolean,
    notes                text,
    created_at           timestamptz default now()
);

create index if not exists idx_bt_session
    on backtest_trades (session_id);

create index if not exists idx_bt_pair_pattern
    on backtest_trades (pair, entry_pattern);


-- ─────────────────────────────────────────────
-- 6. WEEKLY FX PERFORMANCE
--    One row per currency per weekly report
-- ─────────────────────────────────────────────
create table if not exists weekly_fx_performance (
    id                 uuid primary key default uuid_generate_v4(),
    week_ending        date not null,        -- Friday of the report week
    week_label         varchar(10) not null, -- e.g. W21-2026
    currency           varchar(6) not null,
    spot_vs_usd        numeric,              -- spot rate vs USD at Friday close
    weekly_change_pct  numeric,              -- % change vs USD that week (+ = strengthened)
    created_at         timestamptz default now(),
    unique (week_ending, currency)
);

create index if not exists idx_wfx_week
    on weekly_fx_performance (week_ending desc);

create index if not exists idx_wfx_currency
    on weekly_fx_performance (currency, week_ending desc);


-- ─────────────────────────────────────────────
-- 7. WEEKLY INDEX PERFORMANCE
--    One row per index per weekly report
-- ─────────────────────────────────────────────
create table if not exists weekly_index_performance (
    id                 uuid primary key default uuid_generate_v4(),
    week_ending        date not null,
    week_label         varchar(10) not null,
    currency           varchar(6) not null,
    index_name         varchar(30) not null, -- e.g. S&P 500
    ticker             varchar(15),          -- e.g. SPX
    close_price        numeric,
    weekly_change_pts  numeric,
    weekly_change_pct  numeric,
    created_at         timestamptz default now(),
    unique (week_ending, ticker)
);

create index if not exists idx_widx_week
    on weekly_index_performance (week_ending desc);
