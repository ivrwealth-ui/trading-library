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
