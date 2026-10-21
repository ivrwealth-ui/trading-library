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
