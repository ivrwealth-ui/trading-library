# 4. Indicators I — Moving Averages

## Why moving averages

From *Swing Trading*, Chapter 2: a **moving average** is the average of the last *N* closes, and it acts as *dynamic* support and resistance. In this framework we use three, and each has one specific job:

| Average | Window | Job |
|---|---|---|
| EMA-20 | 20 days | dynamic support in an uptrend (the "pullback magnet") |
| MA-50 | 50 days | the trend context — its *slope* is the regime tell |
| MA-200 | 200 days | the long-term trend context |

Two of these are **simple** moving averages (the plain average of the last N closes) and one is an **exponential** moving average (which weights recent days more heavily). Both are two lines of code with `pandas`.

## The two functions

Add these to `screener.py`, right after the `WATCHLIST` and `PERIOD`/`INTERVAL` lines:

```python
import pandas as pd


def sma(series, window):
    """Simple moving average: the plain average of the last `window` closes."""
    return series.rolling(window).mean()


def ema(series, span):
    """Exponential moving average. `adjust=False` matches most charting tools."""
    return series.ewm(span=span, adjust=False).mean()
```

- `series.rolling(50).mean()` takes the close series and, at every point, averages the previous 50 closes. That is an MA-50.
- `series.ewm(span=20, adjust=False).mean()` does the exponential version — same idea, but each day is weighted so the most recent day matters most. The `adjust=False` detail is what makes the number match TradingView and most charting platforms.

## Compute them for one stock

Replace the loop at the bottom of `screener.py` with a version that fetches **one** stock and prints its three averages. This is easier to check by eye before we scale back up to fifty:

```python
df = fetch("RELIANCE")
close = df["Close"]

ema20 = ema(close, 20)
ma50 = sma(close, 50)
ma200 = sma(close, 200)

price = close.iloc[-1]
print(f"last close:    {price:.2f}")
print(f"20-day EMA:    {ema20.iloc[-1]:.2f}")
print(f"50-day MA:     {ma50.iloc[-1]:.2f}")
print(f"200-day MA:    {ma200.iloc[-1]:.2f}")
```

Run it:

```bash
python3 screener.py
```

You should see four numbers, like:

```
last close:    1226.40
20-day EMA:    1249.10
50-day MA:     1251.30
200-day MA:    1300.50
```

These are the raw ingredients. Notice what you can *already* read from them, using nothing but the book: the price is below all three averages, which in *Swing Trading* Chapter 3 is the textbook signature of a downtrend. Two chapters from now you will teach the program to read that automatically.

## A first look at the arithmetic

To trust the tool, it helps to see that a moving average really is "the average of the last N closes". For a 3-day simple average of the closes `101, 103, 105`, the value is `(101 + 103 + 105) / 3 = 103`. `rolling(3).mean()` does exactly that, sliding the window forward one day at a time. The EMA is the same sliding idea, but with the newest close weighted most heavily — which is why the 20-day EMA sits *closer* to today's price than a 20-day SMA would after a sharp move.

You do not need to memorise the weighting formula. What matters is the *behaviour*: a rising average means the recent trend is up, a flat average means no trend, a falling average means down. That slope — not the level — is the whole basis of the next two chapters.

## Summary

- `rolling(window).mean()` = simple moving average; `ewm(span, adjust=False).mean()` = exponential moving average.
- We use EMA-20 (dynamic support), MA-50 (trend context), MA-200 (long-term context).
- Price above/below these averages is a first, rough regime read.
- The *slope* of an average — rising, flat, falling — matters more than its level.

Next: the second half of the toolkit — RSI and the short RSI-2 oscillator.
