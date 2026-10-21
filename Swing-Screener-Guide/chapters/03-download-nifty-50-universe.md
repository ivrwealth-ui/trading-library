# 3. Download the NIFTY 50 Universe

## From one stock to fifty

Last chapter you downloaded one stock. A screener is only useful when it looks at a *list*. This chapter replaces the single ticker with a list of fifty — the **NIFTY 50**, the fifty largest and most liquid names on the National Stock Exchange — and teaches the program to keep going when one of them fails.

## The watchlist

Create a new file called `screener.py` (you will keep growing this same file for the rest of the book). Start with the list and a small bit of setup:

```python
import time

import yfinance as yf

WATCHLIST = [
    "ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK",
    "BSE", "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BEL",
    "BHARTIARTL", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT",
    "ETERNAL", "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE",
    "HINDALCO", "HINDUNILVR", "ICICIBANK", "ITC", "INFY",
    "INDIGO", "JSWSTEEL", "JIOFIN", "KOTAKBANK", "LT",
    "M&M", "MARUTI", "MAXHEALTH", "NTPC", "NESTLEIND",
    "ONGC", "POWERGRID", "RELIANCE", "SBILIFE", "SHRIRAMFIN",
    "SBIN", "SUNPHARMA", "TCS", "TATACONSUM", "TMPV",
    "TATASTEEL", "TECHM", "TITAN", "TRENT", "ULTRACEMCO",
]

PERIOD = "1y"
INTERVAL = "1d"
```

This is the NIFTY 50 as of October 2026. NSE rebalances the index twice a year, so before you rely on it, refresh the list from the index constituents file on niftyindices.com.

Three things worth noticing:

- The list is **one place**, at the very top. If you want to screen your own ten stocks instead of fifty, you edit this list and nothing else in the program changes.
- `TMPV` is there, not `TATAMOTORS` — because Tata Motors was renamed Tata Motors Passenger Vehicles in late 2025 and the exchange changed its symbol. Tickers are not set in stone, which is the whole reason the next section exists.
- `import time` gives us `time.sleep`, which we use below.

## Download in a loop

Add a loop that walks down the list and prints each stock's last close:

```python
def fetch(symbol):
    """Download one year of daily history for a symbol. Returns None on failure."""
    ticker = symbol + ".NS"
    try:
        df = yf.Ticker(ticker).history(
            period=PERIOD, interval=INTERVAL, auto_adjust=False
        )
    except Exception:
        return None
    if df is None or len(df) < 201:
        return None
    return df[["Close"]]


for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        print(f"{symbol}: no data, skipped")
        continue
    last_close = df["Close"].iloc[-1]
    print(f"{symbol}: {last_close:.2f}")
    time.sleep(0.4)
```

Read the new pieces:

- **`def fetch(symbol):`** defines a *function* — a named block of code we can call again and again. Anything indented under it belongs to that function.
- **`try:` / `except:`** is error handling. If anything inside `try` raises an error (say the network drops, or the ticker no longer exists), the program runs the `except` block instead of crashing, and returns `None`.
- **`if df is None or len(df) < 201:`** guards against two things at once: a totally failed download, and a download so short it could not even compute a 200-day moving average later. `len(df)` counts the rows. We require at least 201 rows because Chapter 8 needs a 200-day average *plus* the current day.
- **`continue`** jumps to the next item in the loop, so a bad stock is skipped rather than breaking everything.
- **`df["Close"].iloc[-1]`** picks the `Close` column and takes its last row — the most recent close.
- **`f"{symbol}: {last_close:.2f}"`** is a formatted string: it inserts the symbol, then the price rounded to two decimals.
- **`time.sleep(0.4)`** pauses for four-tenths of a second between downloads. It makes the whole run a few seconds slower, but it is polite to the free data source and makes failures less likely.

## Run it

```bash
python3 screener.py
```

You should see fifty lines, one per stock, something like this (illustrative — your prices will differ):

```
ADANIENT: 3020.00
ADANIPORTS: 1824.00
APOLLOHOSP: 8944.50
...
ULTRACEMCO: 10826.00
```

Occasionally one line will instead read `SYMBOL: no data, skipped`. That is the program working as intended — a free data feed hiccup, handled quietly rather than crashing the whole run. (If *most* of the list says "no data", your internet connection is the likely culprit, not the program.)

## Summary

- A watchlist is one editable list at the top of the file.
- `def` defines a reusable function; `try`/`except` stops one bad download from crashing the run; `continue` skips it.
- `df["Close"].iloc[-1]` is "the most recent close".
- `time.sleep(0.4)` is politeness to the free data source.

Next: compute moving averages from that series of closes — the first real indicator.
