-- ══════════════════════════════════════════════════════════════
-- Add weekly performance tables — run in Supabase SQL Editor
-- ══════════════════════════════════════════════════════════════

-- 6. Weekly FX Performance
create table if not exists weekly_fx_performance (
    id                 uuid primary key default uuid_generate_v4(),
    week_ending        date not null,
    week_label         varchar(10) not null,
    currency           varchar(6) not null,
    spot_vs_usd        numeric,
    weekly_change_pct  numeric,
    created_at         timestamptz default now(),
    unique (week_ending, currency)
);

create index if not exists idx_wfx_week
    on weekly_fx_performance (week_ending desc);

create index if not exists idx_wfx_currency
    on weekly_fx_performance (currency, week_ending desc);

alter table weekly_fx_performance disable row level security;


-- 7. Weekly Index Performance
create table if not exists weekly_index_performance (
    id                 uuid primary key default uuid_generate_v4(),
    week_ending        date not null,
    week_label         varchar(10) not null,
    currency           varchar(6) not null,
    index_name         varchar(30) not null,
    ticker             varchar(15),
    close_price        numeric,
    weekly_change_pts  numeric,
    weekly_change_pct  numeric,
    created_at         timestamptz default now(),
    unique (week_ending, ticker)
);

create index if not exists idx_widx_week
    on weekly_index_performance (week_ending desc);

alter table weekly_index_performance disable row level security;
