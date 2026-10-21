# 6. Reading the Regime: Trending or Ranging?

## The decision that precedes every trade

From *Swing Trading*, Chapter 3: before any setup, the swing trader answers one question — **is this market trending or ranging?** The answer chooses the strategy family, because the two families are optimised for opposite conditions and using the wrong one is the fastest way to lose money.

This chapter teaches the program to answer that question automatically, stock by stock, using the **50-day MA slope** — one of the three tests the book names.

## The rule, in plain English

The book gives three ways to read the regime (structure, moving-average slope, and time). We implement the moving-average test because it is the one that translates cleanly into a few lines of code:

- **Uptrend** — price is *above* a *rising* 50-day MA.
- **Downtrend** — price is *below* a *falling* 50-day MA.
- **Range** — everything else: a flat MA, or price and slope disagreeing.

"Sloping" means the MA has moved by more than a tiny amount over the last few days. We measure that as a percentage: if the 50-day MA is **more than 0.5% higher** today than it was 10 days ago, it is rising; **more than 0.5% lower**, falling; anything in between, flat.

## The code

Add these two constants up with the other config (next to `PERIOD` and `INTERVAL`), and the function below:

```python
SLOPE_LOOKBACK = 10        # compare the 50-day MA to itself 10 days ago
SLOPE_THRESHOLD = 0.005    # a 0.5% move over that window = "sloping"


def detect_regime(close, ma50):
    """Label a stock UPTREND, DOWNTREND, or RANGE from its 50-day MA."""
    price = close.iloc[-1]
    ma50_now = ma50.iloc[-1]
    ma50_then = ma50.iloc[-1 - SLOPE_LOOKBACK]

    slope = ma50_now / ma50_then - 1.0
    rising = slope > SLOPE_THRESHOLD
    falling = slope < -SLOPE_THRESHOLD
    above = price > ma50_now

    if above and rising:
        return "UPTREND"
    if (not above) and falling:
        return "DOWNTREND"
    return "RANGE"
```

Read it:

- **`ma50.iloc[-1 - SLOPE_LOOKBACK]`** is the 50-day MA *ten days ago*. Comparing today's MA to that one tells us its slope.
- **`slope = ma50_now / ma50_then - 1.0`** turns that into a fraction: `+0.01` means "1% higher", `-0.01` means "1% lower".
- **`rising` / `falling`** are `True`/`False` flags against the 0.5% threshold.
- The three-way `if` is the plain-English rule above, written as code. The final `return "RANGE"` is the catch-all — when price and slope disagree, or the MA is flat, we refuse to call it a trend.

## Wire it into the run

Replace the bottom of `screener.py` with a version that computes the regime for every stock in the list:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        print(f"{symbol}: no data, skipped")
        continue

    close = df["Close"]
    ma50 = sma(close, 50)
    regime = detect_regime(close, ma50)

    print(f"{symbol}: {regime}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

You should see fifty lines like these (illustrative — the labels change from day to day):

```
ADANIENT: DOWNTREND
ADANIPORTS: RANGE
APOLLOHOSP: RANGE
ASIANPAINT: UPTREND
...
```

## Two honest notes from the book

The book makes two points worth keeping in view before you start *acting* on these labels:

1. **Downtrends are asymmetric in India.** Retail investors can *sell* what they own or use index instruments, but a clean, liquid short side is harder to access than the long side. Many Indian swing traders therefore simply stand aside in downtrends — which is itself a valid decision. A "DOWNTREND" label is information, not an instruction to do anything.
2. **Regimes change.** The single most dangerous moment is the *transition* — a range about to break out, or a trend about to reverse. A stock that has sat in RANGE for weeks is exactly the one to watch for a breakout, not the one to assume will stay quiet.

Our screener reports the label; it does not act on it. The next two chapters add the setups that *interpret* the label — and note how each setup only fires inside the regime it was designed for.

## Summary

- The regime test is price-vs-50-day-MA *plus* the slope of that MA.
- Uptrend = above a rising MA; downtrend = below a falling MA; range = anything else.
- Slope is measured as the MA's % change over 10 days, against a 0.5% threshold.
- The label is information, not an instruction — the book itself says standing aside is valid.

Next: the first setup — the pullback continuation, which only ever fires in an uptrend.
