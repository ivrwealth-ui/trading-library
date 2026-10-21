# 2. Pine Script v6 Essentials

## The subset you need to read the scripts

You do not need to learn all of Pine to use this book — only the subset that appears in the eight screeners. This chapter covers that subset, including the two parts that trip people up most: **fundamental data access** and **the screener-specific limits**.

## The skeleton

Every script in this book has the same skeleton:

```pine
//@version=6
indicator("Script Title", overlay = false)

// inputs
// data
// condition
// plots
// alert
```

- `//@version=6` declares Pine v6 (required as the first line).
- `indicator(title, overlay = ...)` declares an *indicator* (a study) — this is what screeners use (a `strategy()` is for backtesting, not screening).
- `overlay = false` puts the script in its own pane; for screeners, the chart is irrelevant — the *columns* are what matter.

## Variables and types

Pine is a typed language, but types are usually inferred:

```pine
float eps = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC", "TTM")
bool cond = close > ta.sma(close, 200)
int lookback = 252
```

The three you will see constantly: `float` (numbers), `bool` (true/false), `int` (whole numbers). Explicit type prefixes (`float`, `bool`, `int`) are good practice.

## The `ta.` namespace (built-in indicators)

Most technical calculations live under `ta.`:

| Function | Meaning |
|----------|---------|
| `ta.sma(src, len)` | Simple moving average |
| `ta.ema(src, len)` | Exponential moving average |
| `ta.rsi(src, len)` | Relative Strength Index |
| `ta.roc(src, len)` | Rate of change (%), over `len` bars |
| `ta.atr(len)` | Average True Range |
| `ta.highest(src, len)` | Highest value over `len` bars |
| `ta.lowest(src, len)` | Lowest value over `len` bars |

`close`, `high`, `low`, `volume`, `open` are built-in series; `close[1]` is the *previous* bar's close.

## The `request.` namespace (other data)

This is the part that enables most of this book's screeners — pulling data from **other symbols, other timeframes, and fundamental statements**:

- `request.security(symbol, timeframe, expression)` — data from another symbol/timeframe (e.g., the weekly close, or NIFTY's close for relative strength).
- `request.financial(symbol, financial_id, period, ...)` — **fundamental data** (from FactSet): balance sheet, income statement, and derived ratios.
- `request.earnings(ticker, field, ...)` — earnings data and estimates.

### `request.financial()` — the fundamental data

The signature: `request.financial(symbol, financial_id, period, gaps, ignore_invalid_symbol, currency)`.

- **`symbol`** — `syminfo.tickerid` (the symbol being scanned).
- **`financial_id`** — an uppercase string naming the metric. The ones this book uses:
  - `"EARNINGS_PER_SHARE_BASIC"` — basic EPS (supports TTM).
  - `"EARNINGS_PER_SHARE_BASIC_ONE_YEAR_GROWTH"` — EPS growth %, year over year.
  - `"EARNINGS_ESTIMATE"` — forward EPS estimate.
  - `"REVENUE_ONE_YEAR_GROWTH"` — revenue growth %, year over year.
  - `"TOTAL_EQUITY"`, `"TOTAL_DEBT"`, `"TOTAL_SHARES_OUTSTANDING"`, `"TOTAL_REVENUE"`, `"NET_INCOME"`, `"EBITDA"`.
  - `"DEBT_TO_EQUITY"`, `"DEBT_TO_EBITDA"` — pre-computed leverage ratios.
- **`period`** — `"FY"` (annual), `"FQ"` (quarterly), `"TTM"` (trailing twelve months), `"FH"` (semi-annual). Not every metric supports every period.
- **`ignore_invalid_symbol = true`** — tells Pine to return `na` instead of throwing an error when a symbol has no data (essential when scanning mixed watchlists).

**Critical caveat:** fundamental data requires the right TradingView plan/subscription, and **many NSE/BSE symbols have sparse or missing fundamental data.** When data is missing, `request.financial()` returns `na`, and the scripts in this book are written so `na` simply means "no signal" — never a crash, and never a false positive.

### `request.security()` — other symbols and timeframes

`request.security(symbol, timeframe, expression)` evaluates an expression in another context. This book uses it for two things:

- **A benchmark** (relative strength): `request.security("NSE:NIFTY", timeframe.period, close, ignore_invalid_symbol = true)`.
- **A higher timeframe** (multi-timeframe analysis): `request.security(syminfo.tickerid, "W", close, ignore_invalid_symbol = true)` — the weekly close.

## The screener limits (the rules that shape every script)

Because the scripts must work in the Pine Screener, they all respect these limits (at the time of writing):

1. **≤40 `request.*` calls** per script — the scripts here use at most four, well inside this limit.
2. **~500-bar lookback** — so 252-bar (12-month) momentum and 150-bar (30-week) moving averages are fine, but multi-year lookbacks are not.
3. **Standard timeframes only** — `"W"` (weekly) and `"D"` (daily) are fine; custom timeframes are not.

## Plots and alerts: the screener's output

Two things turn a calculation into a *screener*:

- **`plot(series, "Title", ...)`** — each plot becomes a **column** in the screener. For a pass/fail signal, plot `cond ? 1 : 0`.
- **`alertcondition(cond, "Title", "Message")`** — each one becomes a **filter** in the Pine Screener (and a condition you can alert on).

The scripts plot both: a **signal** (1/0) you can filter on, and the **metrics** (P/E, momentum %, relative strength) you can sort by.

## Summary

- The skeleton: `//@version=6`, `indicator()`, then inputs → data → condition → plots → alert.
- `ta.*` for technicals; `request.*` for other symbols/timeframes/fundamentals.
- `request.financial()` uses uppercase metric IDs and a period (`"FY"`, `"FQ"`, `"TTM"`, `"FH"`); set `ignore_invalid_symbol = true`.
- Screener limits: ≤40 request calls, ~500-bar lookback, standard timeframes.
- `plot()` = column; `alertcondition()` = filter.

Next: Screener 1 — Valuation.
