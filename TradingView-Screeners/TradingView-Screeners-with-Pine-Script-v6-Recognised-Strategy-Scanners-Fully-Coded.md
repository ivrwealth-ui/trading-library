# TradingView Screeners with Pine Script v6: Recognised-Strategy Scanners, Fully Coded

## Valuation, earnings power, momentum, stage analysis, outperformance, price contraction, Dow Theory, and multi-timeframe screeners — each a complete Pine v6 script — with clear disclaimers.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading and investing involve substantial risk of loss, including the possible loss of principal. Past performance never guarantees future results.
- The strategies encoded here are well-known, widely discussed approaches; they are described and coded for *education*, not as a claim that any of them will be profitable.

## Code Disclaimer

The Pine Script® code in this book is **illustrative and provided "as is", without warranty of any kind.** Specifically:

- It has **not been guaranteed to compile on every TradingView plan or version**, and TradingView's language, functions, and data availability change over time. Always paste into the Pine Editor and resolve any warnings or errors before relying on it.
- **Fundamental-data functions (`request.financial()`, `request.earnings()`) require the relevant data subscription/plan** and may return `na` (no data) for many symbols — especially on NSE/BSE names. Scripts are written to fail *silently* (no signal) when data is unavailable.
- A **screener is a filter, not a trade signal.** Every result must be reviewed independently; the screen merely shortlists candidates for *your own* analysis and decision.
- **Test on paper or demo before any live use.** Screener output is not a recommendation to buy or sell.
- Pine Screener availability, the one-indicator-per-screen limit, the 40-request-call limit, and the 500-bar lookback limit are TradingView features that may change; verify current behaviour in your account.

"Pine Script" and "TradingView" are trademarks of TradingView, Inc. This book is not affiliated with, endorsed by, or sponsored by TradingView.

By reading this book, you agree that you are solely responsible for your own trading decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches you to build **TradingView screeners** using **Pine Script v6**, encoding strategies that are widely considered *substantive* — valuation, earnings power, momentum, stage analysis, outperformance, price contraction, Dow Theory, and multi-timeframe analysis — rather than trivial moving-average crossovers.

- **Chapters 1–2** explain the *types* of TradingView screeners and the Pine v6 essentials (including how to pull fundamental data) that every script uses.
- **Chapters 3–10** are eight screener scripts, each a complete, copy-pasteable Pine v6 script. Every chapter follows the same pattern: the strategy's idea, the exact logic, the full code, and how to read its columns.
- **Chapters 11–12** cover how to load and use the screeners, and the code best practices and disclaimers that govern them.
- The **appendix** indexes all eight scripts and points to the consolidated eight-factor script.

A note on language: this book describes what a screen *is* and what a strategy has historically been understood to do — never what you "should" buy. Screeners are filters; decisions are yours.

---

## Table of Contents

1. TradingView Screener Types
2. Pine Script v6 Essentials
3. Screener 1 — Valuation (P/E, P/B)
4. Screener 2 — Earnings Power (EPS & Revenue Growth)
5. Screener 3 — Momentum (12-Month Return, 52-Week High)
6. Screener 4 — Stage Analysis (Weinstein Stage 2)
7. Screener 5 — Outperformance (Relative Strength vs. Benchmark)
8. Screener 6 — Price Contraction (VCP)
9. Screener 7 — Dow Theory (Trend Structure + Volume)
10. Screener 8 — Multi-Timeframe (Weekly Trend + Daily Trigger)
11. Loading and Using Your Screeners
12. Code Best Practices and Disclaimers

Appendix — Consolidated Scripts

---


# 1. TradingView Screener Types

## Three ways to screen

TradingView offers three distinct ways to filter the market, and they are easily confused. Understanding the difference is the prerequisite to using the scripts in this book.

## Type 1 — The built-in screeners

TradingView ships **built-in screeners** for stocks, ETFs, crypto, and forex (under *Products → Screeners*). Each has a large set of **preset filters** — market, sector, market cap, price, volume, performance, valuation ratios, and a library of built-in technical indicators.

- **Strengths:** fast, no code, covers a huge universe with ready-made filters.
- **Limits:** you are restricted to the *preset* filters. You cannot express custom, multi-condition logic like "the stock is in Weinstein Stage 2 *and* its volume is drying up." That is exactly where custom Pine comes in.

## Type 2 — Custom Pine indicators as screener columns

This is the workhorse for this book. Any Pine `indicator()` you write can be **loaded into the Pine Screener** (Type 3), where its plots become columns and its `alertcondition()` calls become filters. The built-in screeners (Type 1) do not accept custom scripts, so custom logic runs only in the Pine Screener or on a chart. The screener reads the **value your script plots on the last bar**, for each symbol.

The pattern is simple:

1. Write an `indicator()` that computes a **boolean condition** ("is this a value candidate?") and **plots it** — typically as `1` when true and `0` when false.
2. Load the script in the Pine Screener.
3. Filter on the plot ("Signal == 1").

Because every `plot()` in your script becomes a column, you can also plot the *metrics themselves* (P/E, momentum %, relative strength) and **sort** the screener by them. A well-written screener script therefore does two jobs at once: it provides a **pass/fail signal** and **sortable metric columns**.

## Type 3 — Pine Screener (the newer, script-driven scanner)

TradingView's newer **Pine Screener** (*Products → Screeners → Pine*) is a dedicated scanner that runs a single Pine script over one of **your watchlists** (or an index's constituents) and produces a table of results, with each plot as a column and each `alertcondition()` as a filter.

Its key mechanics (which constrain how you write scripts; these are the limits at the time of writing — check TradingView's current Pine Screener help page):

- **One indicator per scan.**
- The script must output at least one **plot** or **`alertcondition()`**.
- **Only plots become columns**; `alertcondition()` entries become filters.
- **At most 40 `request.*()` calls** per script.
- **Lookback limited to ~500 bars.**
- **Only standard timeframes** are supported (no custom timeframes).
- **`input.symbol()`, `input.timeframe()` and `input.time()` are not adjustable** — the screener ignores your settings and uses the script's defaults.

All eight scripts in this book are written to work in the Pine Screener (and as ordinary indicators on a chart) — they use few `request.*` calls, modest lookbacks, and output both plots and `alertcondition()`.

## The mental model

A Pine screener script is just an indicator that answers, for the symbol currently being scanned, a **yes/no question** — and optionally reports the **numbers behind the answer**. Everything else (the scanning, the table, the sorting) is TradingView's job. Your job is to encode the question *well*.

## Summary

- Three types: built-in screeners (preset filters only), custom Pine indicators whose plots become columns, and the Pine Screener that runs them.
- A screener script computes a boolean condition and plots it (1/0), plus metric columns.
- Pine Screener limits: one indicator, ≤40 request calls, ~500-bar lookback, standard timeframes.
- Every script in this book is written within those limits.

Next: the Pine v6 essentials every script uses — including how to pull fundamental data.


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


# 3. Screener 1 — Valuation (P/E, P/B)

## The strategy

**Value investing** holds that stocks trading cheaply relative to their earnings and book value tend to outperform expensive ones over long horizons — a pattern research suggests has held historically, though not in every period. This screener encodes the classic two-ratio value screen: a reasonable **price-to-earnings** and **price-to-book**.

Note the important boundary: this is a *filter for cheapness*, not a buy signal. A cheap stock can stay cheap (the "value trap"). In practice, pair this screen with a technical trigger (an uptrend or a reversal — see the *Techno-Funda* book in this series) before acting.

## The logic

For the symbol being scanned, pull three fundamentals and compute two ratios:

- **P/E (TTM)** = `close / EPS (TTM)`.
- **P/B** = `close / book-value-per-share`, where book value per share = `TOTAL_EQUITY / TOTAL_SHARES_OUTSTANDING`.

The signal fires when **both** P/E and P/B are positive and below their thresholds. Positive EPS is required implicitly: P/E is only ever computed (never `na`) when EPS is positive, so a loss-making company can never pass this screen. When fundamental data is missing, the ratios are `na` and the signal simply does not fire.

## The code

```pine
//@version=6
indicator("Valuation Screen (P/E, P/B)", overlay = false)

// ---- Inputs ----
float peMax  = input.float(25.0, "Max P/E (TTM)")
float pbMax  = input.float(3.0,  "Max P/B")

// ---- Fundamentals (ignore_invalid_symbol = true → na when no data) ----
float epsTtm = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC", "TTM", ignore_invalid_symbol = true)
float totEq  = request.financial(syminfo.tickerid, "TOTAL_EQUITY", "FY", ignore_invalid_symbol = true)
float shares = request.financial(syminfo.tickerid, "TOTAL_SHARES_OUTSTANDING", "FQ", ignore_invalid_symbol = true)

// ---- Derived ratios ----
// Positive EPS is required here, not via a separate toggle: a loss-making
// company (epsTtm <= 0) makes pe na, which the condition below excludes.
float pe   = epsTtm > 0 ? close / epsTtm : na
float bvps = (totEq > 0 and shares > 0) ? totEq / shares : na
float pb   = bvps > 0 ? close / bvps : na

// ---- Screen condition ----
bool cond  = not na(pe) and pe > 0 and pe <= peMax and not na(pb) and pb > 0 and pb <= pbMax

// ---- Output: metric columns + signal column ----
plot(pe, "P/E (TTM)", color = color.blue)
plot(pb, "P/B", color = color.purple)
plot(cond ? 1 : 0, "Value Signal", color = cond ? color.green : color.red, style = plot.style_columns)

// ---- Filter ----
alertcondition(cond, "Value candidate", "P/E and P/B at or below their thresholds")
```

## How to read the columns

When you add this to the screener and scan a watchlist:

- **"P/E (TTM)"** and **"P/B"** — sortable numeric columns; sort ascending to surface the cheapest.
- **"Value Signal"** — `1` = passes the screen, `0` = fails. Filter on "Value Signal == 1".

## Honest limitations

- **Data availability** — fundamental data is often missing for smaller NSE/BSE names; those simply show no signal.
- **Value trap** — cheap ≠ about-to-rise; pair with a technical trigger.
- **One ratio is not a thesis** — a low P/E can be a warning (deteriorating business), not an opportunity; review each result.

Next: Screener 2 — Earnings Power.


# 4. Screener 2 — Earnings Power (EPS & Revenue Growth)

## The strategy

**Earnings-power investing** holds that what ultimately drives a stock over time is the *growth of its earnings* — and research suggests the market often under-reacts to accelerating earnings. This screener flags companies whose **earnings and revenue are growing** at a meaningful rate, and whose **forward estimate** points to continued growth.

This is a *fundamental-momentum* screen: it does not care how cheap a stock is, only whether its profit engine is expanding.

## The logic

Pull three growth-related fundamentals and test them against thresholds:

- **EPS growth (year-over-year)** — `EARNINGS_PER_SHARE_BASIC_ONE_YEAR_GROWTH` (TTM).
- **Revenue growth (year-over-year)** — `REVENUE_ONE_YEAR_GROWTH` (TTM).
- **Forward estimate above trailing EPS** — `EARNINGS_ESTIMATE` (FY) greater than trailing EPS (TTM), i.e., the market expects growth to continue.

The signal fires when EPS and revenue growth exceed their thresholds, and the forward estimate confirms (or estimate data is unavailable, in which case that sub-check is skipped rather than failing).

## The code

```pine
//@version=6
indicator("Earnings Power (EPS & Revenue Growth)", overlay = false)

// ---- Inputs ----
float minEpsGrowth = input.float(15.0, "Min EPS growth % YoY")
float minRevGrowth = input.float(10.0, "Min revenue growth % YoY")

// ---- Fundamentals ----
float epsGrowth = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC_ONE_YEAR_GROWTH", "TTM", ignore_invalid_symbol = true)
float revGrowth = request.financial(syminfo.tickerid, "REVENUE_ONE_YEAR_GROWTH", "TTM", ignore_invalid_symbol = true)
float epsEst    = request.financial(syminfo.tickerid, "EARNINGS_ESTIMATE", "FY", ignore_invalid_symbol = true)
float epsTtm    = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC", "TTM", ignore_invalid_symbol = true)

// ---- Screen condition ----
bool epsOk  = not na(epsGrowth) and epsGrowth >= minEpsGrowth
bool revOk  = not na(revGrowth) and revGrowth >= minRevGrowth
// Forward estimate above trailing EPS → expected continued growth (skipped if no estimate data)
bool estOk  = (na(epsEst) or na(epsTtm) or epsTtm <= 0) ? true : epsEst > epsTtm

bool cond = epsOk and revOk and estOk

// ---- Output ----
plot(epsGrowth, "EPS Growth YoY %", color = color.teal)
plot(revGrowth, "Revenue Growth YoY %", color = color.olive)
plot(cond ? 1 : 0, "Earnings Power Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Earnings power candidate", "EPS and revenue growing above thresholds")
```

## How to read the columns

- **"EPS Growth YoY %"** and **"Revenue Growth YoY %"** — sortable; sort descending to surface the fastest growers.
- **"Earnings Power Signal"** — `1` = passes, `0` = fails. Filter on `== 1`.

## Honest limitations

- **Four `request.financial()` calls** — well within the Pine Screener's 40-call ceiling, so there is room to add a benchmark for relative strength; just remember that every extra fundamental condition is another chance for missing data to block the signal.
- **Growth quality vs. quantity** — a high growth rate can be a one-off (an acquisition, a base effect). The screen flags the number, not the *quality* of the growth; review each result.
- **Data availability** — same caveat as Screener 1: missing data means no signal.

Next: Screener 3 — Momentum.


# 5. Screener 3 — Momentum (12-Month Return, 52-Week High)

## The strategy

**Momentum** is the well-documented tendency of recent winners to keep winning. This screener encodes the two most common momentum measures at once: a **12-month rate of change** (the classic lookback) and **proximity to the 52-week high** (a psychologically salient anchor that research suggests has historically been associated with continued outperformance).

This is a pure *price* screen — no fundamental data required, so it works on any symbol with price history.

## The logic

- **12-month return** = `ta.roc(close, 252)` — the rate of change over ~252 trading days.
- **Distance from the 52-week high** = `(close / ta.highest(close, 252)) * 100 - 100` — 0% means *at* the high; −10% means 10% below it.

The signal fires when the 12-month return exceeds a threshold **and** the stock is within a small distance of its 52-week high (strength confirmed by being near the top of its range).

## The code

```pine
//@version=6
indicator("Momentum Screen (12M Return + 52W High)", overlay = false)

// ---- Inputs ----
float minReturn = input.float(15.0, "Min 12-month return %")
float maxFromHigh = input.float(-10.0, "Max distance below 52W high (%)")  // negative number: -10 means "within 10% of the high"; entering a positive value will silently match nothing

// ---- Signals (252 bars ≈ 12 months; within the ~500-bar screener limit) ----
float roc = ta.roc(close, 252)
float high52 = ta.highest(close, 252)
float pctFromHigh = high52 > 0 ? (close / high52) * 100 - 100 : na

// ---- Screen condition ----
bool momOk     = not na(roc) and roc >= minReturn
bool nearHigh  = not na(pctFromHigh) and pctFromHigh >= maxFromHigh

bool cond = momOk and nearHigh

// ---- Output ----
plot(roc, "12M Return %", color = color.blue)
plot(pctFromHigh, "Dist from 52W High %", color = color.purple)
plot(cond ? 1 : 0, "Momentum Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Momentum candidate", "Strong 12M return and near the 52-week high")
```

## How to read the columns

- **"12M Return %"** — sort descending for the strongest momentum.
- **"Dist from 52W High %"** — sort descending (closest to 0, i.e., nearest the high).
- **"Momentum Signal"** — `1` = passes both, `0` = fails.

## Honest limitations

- **Momentum reverses sharply.** After market bottoms, prior winners lag the sharp recovery in prior losers; the momentum premium arrives in lumps.
- **No trend filter.** This screen does not check whether the *broad market* is trending up; a momentum screen in a bear market surfaces the least-bad names, not necessarily good ones.
- **No fundamental context.** A momentum screen will happily flag a falling-quality stock that happens to be rallying; pair with a valuation/earnings screen for a techno-funda combination.

Next: Screener 4 — Stage Analysis.


# 6. Screener 4 — Stage Analysis (Weinstein Stage 2)

## The strategy

**Stage Analysis** (Stan Weinstein's methodology) holds that stocks move through four *stages* — basing (Stage 1), advancing (Stage 2), topping (Stage 3), and declining (Stage 4) — and that **Stage 2**, the *advancing* stage, is often cited as the highest-probability period to own a stock: it is where price is above a rising long-term moving average and the trend is up.

This screener encodes the classic Stage 2 definition on a daily chart, using the 30-week and 10-week moving averages (150 and 50 daily bars).

## The logic

Weinstein's Stage 2, expressed as rules:

1. **Price is above the 30-week (150-day) MA** — the primary trend is up.
2. **The 30-week MA is rising** — the trend is *advancing*, not just flat.
3. **The 10-week (50-day) MA is above the 30-week MA** — the shorter-term trend is leading the longer-term trend (an orderly uptrend).

When all three hold, the stock is in the advancing stage.

## The code

```pine
//@version=6
indicator("Stage Analysis (Weinstein Stage 2)", overlay = false)

// ---- Inputs ----
int longMa  = input.int(150, "30-week MA (daily bars)", minval = 1)
int shortMa = input.int(50,  "10-week MA (daily bars)", minval = 1)

// ---- Moving averages ----
float ma30 = ta.sma(close, longMa)
float ma10 = ta.sma(close, shortMa)

// ---- Stage 2 conditions ----
bool aboveLong     = close > ma30          // price above 30-week MA
bool longRising    = ma30 > ma30[1]        // 30-week MA rising
bool shortAboveLong = ma10 > ma30          // 10-week MA above 30-week MA

bool stage2 = aboveLong and longRising and shortAboveLong

// ---- Output ----
plot(stage2 ? 1 : 0, "Stage 2 Signal", color = stage2 ? color.green : color.red, style = plot.style_columns)
plot(close / ma30 * 100 - 100, "Dist from 30W MA %", color = color.blue)

alertcondition(stage2, "Stage 2 (Weinstein)", "Price above a rising 30-week MA, with the 10-week MA above the 30-week MA")
```

## How to read the columns

- **"Stage 2 Signal"** — `1` = in the advancing stage, `0` = not.
- **"Dist from 30W MA %"** — how far price is above the 30-week MA; a very large positive value means the stock is *extended* (a caveat — see below).

## Honest limitations

- **Lateness by design.** Stage 2 is confirmed only *after* the advance has begun; the screen never catches the exact bottom of Stage 1.
- **Extension risk.** A stock far above its 30-week MA (large "Dist from 30W MA %") has run up fast and is due for a pullback; use the distance column to distinguish *early* Stage 2 (near the MA) from *late* Stage 2 (extended).
- **No volume check in this version.** Weinstein also emphasised volume on the breakout; that refinement is left out here to keep the script within the screener's simplicity, but can be added.

Next: Screener 5 — Outperformance (relative strength).


# 7. Screener 5 — Outperformance (Relative Strength vs. Benchmark)

## The strategy

**Relative strength** (not the RSI oscillator — here, *relative performance*) measures whether a stock is *outperforming its benchmark*. The idea is that **leadership persists**: research suggests a stock that has beaten the index over the last several months has historically tended to keep leading. This screener ranks stocks by their return *minus* the benchmark's return over a trailing window.

The classic benchmark for Indian equities is **NIFTY 50** (`NSE:NIFTY` in TradingView).

## The logic

For the scanned symbol and the benchmark:

- **Stock return** = `ta.roc(close, lookback)`.
- **Benchmark return** = `ta.roc(benchmark close, lookback)`, where the benchmark close is pulled via `request.security()`.
- **Relative strength** = stock return − benchmark return.

The signal fires when relative strength is positive (or above a threshold) — the stock is beating the benchmark.

## The code

```pine
//@version=6
indicator("Outperformance (Relative Strength vs Benchmark)", overlay = false)

// ---- Inputs ----
string benchmark = input.symbol("NSE:NIFTY", "Benchmark")  // input.symbol() returns a string ticker id, not a `symbol` type
int rsLookback = input.int(126, "RS lookback (bars)", minval = 1)   // ~6 months
float minRs = input.float(0.0, "Min relative return %")

// ---- Benchmark data (1 request.security call) ----
float benchClose = request.security(benchmark, timeframe.period, close, ignore_invalid_symbol = true)

// ---- Returns and relative strength ----
float stockRet = ta.roc(close, rsLookback)
float benchRet = ta.roc(benchClose, rsLookback)
float rs = stockRet - benchRet

// ---- Screen condition ----
bool cond = not na(rs) and rs >= minRs

// ---- Output ----
plot(rs, "Relative Strength (6M) %", color = cond ? color.teal : color.gray)
plot(stockRet, "Stock 6M Return %", color = color.blue)
plot(benchRet, "Benchmark 6M Return %", color = color.purple)
plot(cond ? 1 : 0, "Outperform Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Outperformer", "Stock outperforming benchmark over 6 months")
```

## How to read the columns

- **"Relative Strength (6M) %"** — sort descending to surface the biggest outperformers.
- **"Stock 6M Return %"** and **"Benchmark 6M Return %"** — the two components, so you can see *why* a stock is an outperformer (strong stock vs. weak benchmark).
- **"Outperform Signal"** — `1` = beating the benchmark, `0` = lagging.

## Honest limitations

- **Relative, not absolute.** A stock can be a "relative outperformer" while still *falling* (if it falls less than the benchmark). Pair with an absolute trend filter (Screener 4's Stage 2, or simply price > 200-day MA) to require actual strength.
- **Benchmark mismatch.** Relative strength vs. NIFTY 50 is less meaningful for small-caps (whose benchmark is really the broader market). Choose the benchmark that matches the watchlist you scan.
- **Benchmark input is fixed in the Pine Screener.** The Pine Screener does not support `input.symbol()`: it ignores any benchmark chosen in the settings and uses the script's default (`NSE:NIFTY`). To scan against a different benchmark, change the default in the code.
- **Crowding.** The most obvious outperformers are often the most crowded, and crowded names reverse sharply when leadership rotates.

Next: Screener 6 — Price Contraction (VCP).


# 8. Screener 6 — Price Contraction (VCP)

## The strategy

The **Volatility Contraction Pattern (VCP)** — associated with Mark Minervini's work — describes a specific, high-quality setup: a stock in an **uptrend** that is forming a **tight base**, with **successive contractions** in price range and a **dry-up in volume**. The logic is that a tightening range with shrinking volume marks a period of quiet accumulation after a rise, which is often cited as a precursor to the *next* leg up.

This screener encodes VCP as three measurable conditions: uptrend, range contraction, and volume dry-up.

## The logic

- **Uptrend** — price above the 200-day MA (the stock has been rising).
- **Range contraction** — the current ATR is a *fraction* of the ATR some time ago (the price range has tightened). Computed as `ta.atr(14) / ta.atr(14)[lookback]`.
- **Volume dry-up** — the recent average volume is a *fraction* of the average volume some time ago (trading has quieted). Computed as `ta.sma(volume, 20) / ta.sma(volume, 20)[lookback]`.

When the range has tightened below a threshold *and* volume has dried up below a threshold *within an uptrend*, the VCP condition is present.

## The code

```pine
//@version=6
indicator("Price Contraction (VCP: Tight Base + Volume Dry-up)", overlay = false)

// ---- Inputs ----
int shortAtr  = input.int(14, "ATR length")
int lookback  = input.int(60, "Contraction lookback (bars)")
float maxContraction = input.float(0.60, "Max range contraction (ATR now/prev)")
float maxVolRatio    = input.float(0.75, "Max volume ratio (now/prev)")

// ---- Range contraction ----
float atrNow  = ta.atr(shortAtr)
float atrPrev = ta.atr(shortAtr)[lookback]
float contraction = atrNow / atrPrev        // < 1 → range tightened

// ---- Volume dry-up ----
float volNow  = ta.sma(volume, 20)
float volPrev = ta.sma(volume, 20)[lookback]
float volRatio = volNow / volPrev           // < 1 → volume dried up

// ---- Uptrend filter ----
float ma200 = ta.sma(close, 200)

// ---- Screen condition ----
bool uptrend = close > ma200
bool tight   = not na(contraction) and contraction < maxContraction
bool dryUp   = not na(volRatio) and volRatio < maxVolRatio

bool cond = uptrend and tight and dryUp

// ---- Output ----
plot(contraction, "Range Contraction (ATR now/prev)", color = color.blue)
plot(volRatio, "Volume Ratio (now/prev)", color = color.purple)
plot(cond ? 1 : 0, "VCP Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "VCP contraction", "Tightening range and drying volume in an uptrend")
```

## How to read the columns

- **"Range Contraction (ATR now/prev)"** — lower = tighter; sort ascending.
- **"Volume Ratio (now/prev)"** — lower = drier; sort ascending.
- **"VCP Signal"** — `1` = tight, dry, and in an uptrend.

## Honest limitations

- **VCP is a *setup*, not a *trigger*.** The screen flags the *condition* (a coiled spring); it does not tell you *when* the next leg begins. The traditional trigger is the *breakout* from the tight base — which this screen deliberately leaves for you to time.
- **A contraction can precede a *breakdown*, not just a breakout.** A tight base near the top of an extended run can resolve downward. Review the trend context before acting.
- **Parameter sensitivity.** "Tight" and "dry" are thresholds; the pattern is better read *visually* (on a chart) than by any single numeric cut. Use this as a shortlister, not a verdict.

Next: Screener 7 — Dow Theory.


# 9. Screener 7 — Dow Theory (Trend Structure + Volume)

## The strategy

**Dow Theory** — the oldest formal framework of technical analysis — holds that a genuine uptrend is defined by **structure** and **confirmation**:

- **Primary trend up** (the stock's primary trend is up).
- **Higher highs and higher lows** (the defining structure of an uptrend).
- **Volume confirmation** (rising volume on up-moves, falling on down-moves).

This screener encodes those three ideas into a single pass/fail condition.

## The logic

- **Primary trend up** — the stock is above its 200-day MA, and its 50-day MA is above its 200-day MA (an orderly uptrend).
- **Higher highs and higher lows** — the recent N-day *high* is higher than the prior N-day high, and the recent N-day *low* is higher than the prior N-day low. (Using `ta.highest()`/`ta.lowest()` over a swing window, compared to the same window one swing ago.)
- **Volume confirmation** — the average volume on up-days exceeds the average volume on down-days over the last 20 bars.

## The code

```pine
//@version=6
indicator("Dow Theory (Trend Structure + Volume)", overlay = false)

// ---- Inputs ----
int swingLen = input.int(30, "Swing window (bars)")

// ---- Moving averages (primary trend) ----
float ma200 = ta.sma(close, 200)
float ma50  = ta.sma(close, 50)
bool primaryUp = close > ma200 and ma50 > ma200

// ---- Higher highs and higher lows ----
float recentLow = ta.lowest(low, swingLen)
float priorLow  = ta.lowest(low, swingLen)[swingLen]
bool higherLow  = recentLow > priorLow

float recentHigh = ta.highest(high, swingLen)
float priorHigh  = ta.highest(high, swingLen)[swingLen]
bool higherHigh  = recentHigh > priorHigh

bool structure = higherHigh and higherLow

// ---- Volume confirmation ----
float upVol   = close > close[1] ? volume : 0.0
float downVol = close < close[1] ? volume : 0.0
bool volConfirm = ta.sma(upVol, 20) > ta.sma(downVol, 20)

// ---- Screen condition ----
bool cond = primaryUp and structure and volConfirm

// ---- Output ----
plot(cond ? 1 : 0, "Dow Uptrend Signal", color = cond ? color.green : color.red, style = plot.style_columns)
plot(primaryUp ? 1 : 0, "Primary Trend Up", color = color.blue, style = plot.style_columns)
plot(structure ? 1 : 0, "HH+HL Structure", color = color.purple, style = plot.style_columns)

alertcondition(cond, "Dow theory uptrend", "Primary uptrend with higher highs/lows and volume confirmation")
```

## How to read the columns

Three sub-columns, so you can see *which* condition a failing stock is missing:

- **"Primary Trend Up"** — above the 200-day MA with the 50-day above it.
- **"HH+HL Structure"** — making higher highs and higher lows.
- **"Dow Uptrend Signal"** — `1` = all three (primary trend, structure, and volume) confirm.

## Honest limitations

- **The swing window is a simplification.** True Dow Theory reads *significant* swing points, not a fixed 30-bar window; the fixed window is a tractable proxy, not a faithful implementation.
- **Confirmation is late.** "Higher highs/lows + volume confirmation" is only confirmable *after* the fact; the screen identifies an uptrend that is *already* established, not an early entry.
- **No fundamental layer.** Dow Theory is purely technical; pair with a valuation or earnings screen if you want a techno-funda combination.

Next: Screener 8 — Multi-Timeframe.


# 10. Screener 8 — Multi-Timeframe (Weekly Trend + Daily Trigger)

## The strategy

**Multi-timeframe analysis** holds that signals are stronger when **two timeframes agree**. The classic construction: the **weekly** timeframe defines the *trend* (are we in an uptrend?), and the **daily** timeframe provides the *trigger* (is the daily structure also aligned?). A stock is most attractive when *both* point the same way.

This screener encodes that: a **weekly uptrend** (price above the 30-week MA) combined with a **daily uptrend** (price above the 50-day MA, with the 50-day above the 200-day) and a **daily trigger** (a fresh up-close).

## The logic

- **Weekly trend** — the weekly close is above the 30-week (30-bar weekly) MA. Pulled via `request.security(syminfo.tickerid, "W", ...)`.
- **Daily trend** — price above the 50-day MA, and the 50-day above the 200-day.
- **Daily trigger** — the daily close is above the 50-day MA *and* is a fresh up-close today (`close > close[1]`), suggesting momentum is turning up *now*.

The signal fires when all three align — the higher timeframe agrees, and the lower timeframe is confirming.

## The code

```pine
//@version=6
indicator("Multi-Timeframe (Weekly Trend + Daily Trigger)", overlay = false)

// ---- Weekly (higher timeframe) trend ----
float weeklyClose = request.security(syminfo.tickerid, "W", close, ignore_invalid_symbol = true)
float weeklySma30 = request.security(syminfo.tickerid, "W", ta.sma(close, 30), ignore_invalid_symbol = true)

bool weeklyUptrend = not na(weeklyClose) and not na(weeklySma30) and weeklyClose > weeklySma30

// ---- Daily (lower timeframe) trend + trigger ----
float dailySma50  = ta.sma(close, 50)
float dailySma200 = ta.sma(close, 200)

bool dailyUptrend = close > dailySma50 and dailySma50 > dailySma200
bool dailyTrigger = close > dailySma50 and close > close[1]

// ---- Screen condition ----
bool cond = weeklyUptrend and dailyUptrend and dailyTrigger

// ---- Output ----
plot(cond ? 1 : 0, "Multi-TF Alignment", color = cond ? color.green : color.red, style = plot.style_columns)
plot(weeklyUptrend ? 1 : 0, "Weekly Uptrend", color = color.blue, style = plot.style_columns)
plot(dailyUptrend ? 1 : 0, "Daily Uptrend", color = color.purple, style = plot.style_columns)

alertcondition(cond, "Multi-timeframe alignment", "Weekly and daily trends aligned with a daily up-close")
```

## How to read the columns

- **"Weekly Uptrend"** — the higher-timeframe trend.
- **"Daily Uptrend"** — the lower-timeframe trend.
- **"Multi-TF Alignment"** — `1` = both timeframes agree *and* the daily trigger fired.

## Honest limitations

- **The trigger is a single bar.** `close > close[1]` is a weak "trigger"; in a real workflow it is replaced by something more specific (a breakout, a reversal off a level). It is kept simple here for clarity.
- **Two `request.security()` calls** — well within the 40-call limit, leaving ample headroom if you want to add a benchmark too.
- **Timeframe is fixed to weekly.** The Pine Screener supports standard timeframes, so weekly is fine — but you cannot switch to a *custom* higher timeframe within the scan.

Next: loading and using your screeners.


# 11. Loading and Using Your Screeners

## From code to a working scan

A screener script is useless until it is running against a real watchlist. This chapter walks the exact steps, from the Pine Editor to the Pine Screener, and shows how the built-in screener fits in.

## Step 1 — Create and save the script

1. Open the **Pine Editor** (bottom panel of any chart).
2. Paste one of this book's scripts (replacing the default template).
3. Click **Save** and give it a clear name (e.g., "Stage 2 Screener").
4. Resolve any warnings the compiler shows. Two common fixes:
   - **"The function 'ta.sma' should be called on each calculation for consistency"** — a consistency warning, not a performance hint: it appears when a `ta.*` call sits inside a conditional branch, so its history (and result) can be wrong. Move the call out of the branch into the global scope. None of this book's scripts trigger it.
   - **`na` comparisons or type errors** — check the script against the exact code here; a stray character is usually the cause.

## Step 2 — Make it available to the screener

TradingView's help page says the Pine Screener uses scripts saved **in your favourites**; a later update lets you pick any script from the full Indicators dialogue. Adding it to favourites does no harm and makes it easy to find:

1. Open the **Indicators** dialogue.
2. Go to **My scripts**.
3. Find your saved script and click the **star** to add it to favourites.

## Step 3 — Narrow the universe in the built-in screener (optional)

The built-in screeners do not accept custom Pine scripts as columns or filters (at the time of writing), but they are still useful as a first pass:

1. Open **Products → Screeners → Stock Screener** (or your market).
2. Apply preset filters (market, sector, market cap, liquidity) to narrow the universe.
3. Add the results to a **watchlist**.
4. Scan that watchlist with your script in the Pine Screener (Step 4).

This two-step route gives you the full preset-filter universe plus your custom signal.

## Step 4 — Use it in the Pine Screener (script-driven scan)

1. Build a **watchlist** of the symbols you want to scan (e.g., the NIFTY 500, or a custom list). The Pine Screener scans one source at a time — a watchlist or an index's constituents — not the whole market.
2. Open **Products → Screeners → Pine**.
3. Select your **watchlist** (or an index) and your **script** from the dropdowns.
4. Set the **timeframe** (daily is the default for these scripts).
5. Click **Scan**. Each plot appears as a column; each `alertcondition()` appears as a filter. Sort, filter, and export the results.

Remember the limits (Chapter 1): one script per scan, ≤40 `request.*` calls, ~500-bar lookback, standard timeframes.

## Step 5 — Read the results as a shortlist, not a signal

This is the most important step. A screener returns **candidates**, not decisions. The correct workflow is:

1. **Scan** → get a shortlist.
2. **Open each candidate's chart** and *look* at it — confirm the pattern visually, check the trend context, check for events (earnings, corporate actions).
3. **Apply your own risk rules** (the *Risk Management and Position Sizing* book in this series) before any decision.

A screener that is used as a *substitute* for judgment is a trap; used as a *shortlister*, it is a powerful time-saver.

## Summary

- Save the script; resolve compiler warnings; add it to your **favourites**.
- Built-in screener: narrow the universe with preset filters and save it as a watchlist; it does not run custom scripts.
- Pine Screener: build a watchlist, select the script, scan; plots = columns, alertconditions = filters.
- Treat results as a shortlist, not a signal — always review each candidate on the chart.

Next: code best practices and the disclaimers that govern these scripts.


# 12. Code Best Practices and Disclaimers

## Writing screeners that behave

This closing chapter covers the practices that keep a screener script *correct* and *honest* — and the disclaimers that must accompany any code that touches trading decisions.

## Best practices

### 1. Guard every `na`

Fundamental data is often missing; benchmarks may not exist for every symbol; a fresh listing may not have 252 bars of history. Every script in this book therefore guards against `na`:

- `ignore_invalid_symbol = true` on every `request.financial()` / `request.security()` call.
- Explicit `not na(x)` checks in conditions.
- Ternary expressions that default to `na` rather than dividing by zero (e.g., `epsTtm > 0 ? close / epsTtm : na`).

The result: a symbol without data simply produces **no signal** — it never crashes the script, and never produces a false positive from garbage input.

### 2. Respect the screener limits

Keep every script within the Pine Screener's constraints: **≤40 `request.*` calls**, **≤500-bar lookback**, **standard timeframes only**. If you extend a script, count the calls and check the lookback — a 750-bar momentum window will silently misbehave in the screener.

### 3. Keep the signal binary and named

A screener is easiest to use when the pass/fail output is a single, clearly named plot:

```pine
plot(cond ? 1 : 0, "Signal", color = cond ? color.green : color.red, style = plot.style_columns)
```

Name the plot what it *is* ("Stage 2 Signal", "Value Signal"), because the plot title becomes the column name.

### 4. Plot the metrics, not just the verdict

The most useful screeners report *why* a stock passes, not just *that* it passes. Plotting the P/E, the momentum %, and the relative strength — alongside the signal — lets you **sort** the shortlist and spot *degree*, not just direction.

### 5. Prefer simple, explainable logic

Every strategy here can be explained in a sentence. If a screener needs fifty inputs and a dozen conditions to "work", it is almost certainly overfit to past data and will fail live. Keep it simple enough to explain.

## The disclaimers (why they matter)

These scripts sit at the boundary between code and trading decisions, so they carry three specific warnings — restated from the front of the book, because they are the part that protects you:

1. **A screener is a filter, not a signal.** It shortlists; it does not recommend. Every result is a *candidate for your own review*, never an instruction.
2. **The code is illustrative and comes without warranty.** It has not been certified against every plan, version, or market; it may need adjustment for your data subscription; and it may produce no results (rather than wrong results) when data is missing. Test in the Pine Editor, and on paper, before any reliance.
3. **Historical patterns are not promises.** Valuation, momentum, stage analysis, VCP, Dow Theory — all describe *tendencies*, and all fail at times. A screener operationalises a tendency; it does not guarantee the tendency will hold tomorrow.

Framed as this book always frames such things: *these are recognised, widely discussed strategies, encoded for education. Historically, such conditions have tended to precede continued moves — but the tendency is probabilistic, not certain, and you are responsible for every decision you make from a screen's output.*

## Summary

- Guard every `na`; respect the 40-call/500-bar/standard-timeframe limits.
- Keep the signal binary and clearly named; plot the metrics too.
- Prefer simple, explainable logic — complexity is a symptom of overfitting.
- A screener is a filter, not a signal; the code is illustrative and comes without warranty; historical patterns are tendencies, not promises.

This completes the main text. The appendix indexes all eight scripts.


# Appendix — Consolidated Scripts

## The eight screeners at a glance

The full code for each script is in its chapter (3–10). This appendix is the index and the shared template. A composite that merges all eight screens into one indicator (a 0–8 score) is supplied alongside this book as `consolidated-8-factor-screener.pine`.

| # | Screener | Signal (what makes it pass) | Key columns | Chapter |
|---|----------|------------------------------|-------------|---------|
| 1 | Valuation | P/E ≤ max and P/B ≤ max (positive EPS) | P/E (TTM), P/B | 3 |
| 2 | Earnings Power | EPS growth ≥ min, revenue growth ≥ min, estimate > trailing | EPS Growth %, Revenue Growth % | 4 |
| 3 | Momentum | 12M return ≥ min, near 52-week high | 12M Return %, Dist from 52W High % | 5 |
| 4 | Stage Analysis | Price > rising 30-wk MA; 10-wk MA > 30-wk MA | Stage 2, Dist from 30W MA % | 6 |
| 5 | Outperformance | Relative strength ≥ min vs. benchmark | RS %, Stock %, Benchmark % | 7 |
| 6 | Price Contraction | Tight range + dry volume in uptrend | Range Contraction, Volume Ratio | 8 |
| 7 | Dow Theory | Primary uptrend + HH/HL + volume confirm | 3 sub-signals | 9 |
| 8 | Multi-Timeframe | Weekly uptrend + daily uptrend + daily trigger | Weekly/Daily sub-signals | 10 |

## The shared skeleton

Every script follows the same template — learn it once, and you can read and modify any of them:

```pine
//@version=6
indicator("Your Screener Title", overlay = false)

// ---- Inputs ----
// thresholds and lengths as input.*() calls

// ---- Data ----
// request.financial() / request.security() / ta.* calculations

// ---- Condition ----
bool cond = <your boolean logic, guarded against na>

// ---- Output ----
plot(<metric 1>, "Metric 1", color = color.blue)
plot(<metric 2>, "Metric 2", color = color.purple)
plot(cond ? 1 : 0, "Signal", color = cond ? color.green : color.red, style = plot.style_columns)

// ---- Filter ----
alertcondition(cond, "Signal name", "Human-readable message")
```

## The three rules that keep them working

1. **Guard every `na`** — `ignore_invalid_symbol = true` on every `request.*` call, and `not na(x)` in every condition. Missing data must produce *no signal*, not a crash.
2. **Stay within limits** — ≤40 `request.*` calls, ≤500-bar lookback, standard timeframes.
3. **Keep the signal binary and named** — one clearly titled `1`/`0` plot, plus the metric columns that let you sort.

## A reminder

These scripts are **educational and illustrative** — not guaranteed to compile on every plan, not a recommendation, and not a substitute for your own review of each result. A screener shortlists; you decide.
