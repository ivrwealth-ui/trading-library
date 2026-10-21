# 7. Screen 1 — The Pullback Continuation

## Trade *with* the trend

From *Swing Trading*, Chapter 4: the **pullback continuation** is the classic trend-following entry. In an uptrend, price occasionally dips back toward its rising 20-day EMA before resuming higher. The setup is "reversal off the rising 20-day EMA in an uptrend" — the pause, not the top.

Screens are mechanical versions of that idea. We want to flag a stock when three things are true at once:

1. The stock is in an **uptrend** (from Chapter 6).
2. Its **20-day EMA is rising** (the trend is still alive).
3. Price has pulled back **close to** that EMA (the "pause" moment), rather than running far above it.

## The code

Add the tolerance constant up with the config, and the screen below:

```python
PULLBACK_TOLERANCE = 0.02   # "close to" the EMA = within +/-2% of it


def pullback_setup(close, ema20, regime):
    """True when an uptrending stock has pulled back to its rising 20-day EMA."""
    if regime != "UPTREND":
        return False

    ema20_rising = ema20.iloc[-1] > ema20.iloc[-6]
    dist = close.iloc[-1] / ema20.iloc[-1] - 1.0

    return ema20_rising and abs(dist) <= PULLBACK_TOLERANCE
```

Read it:

- **`if regime != "UPTREND": return False`** is the regime gate — the whole point of Chapter 6. The pullback setup only exists in an uptrend, so anything else is an immediate "no".
- **`ema20.iloc[-1] > ema20.iloc[-6]`** asks whether the 20-day EMA is higher today than it was five days ago — i.e. *rising*. A flat or falling EMA is not a valid pullback magnet.
- **`dist = close / ema20 - 1`** is how far price sits from the EMA, as a fraction. `dist = 0` means price is exactly on the EMA; `dist = +0.05` means 5% above it.
- **`abs(dist) <= PULLBACK_TOLERANCE`** is "within ±2%". We use `abs` (absolute value) because a stock can pull back slightly *through* the EMA and still count — the book treats levels as zones, not exact lines.

## Wire it into the run

Extend the loop so it computes the EMA and calls the screen for every stock:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        continue

    close = df["Close"]
    ema20 = ema(close, 20)
    ma50 = sma(close, 50)

    regime = detect_regime(close, ma50)
    match = pullback_setup(close, ema20, regime)

    flag = "Pullback setup" if match else "—"
    print(f"{symbol}: {regime:10s} {flag}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

Most lines will read `—`; a few (usually only a handful) will read `Pullback setup`. That scarcity is the point — a screen is only useful because it *filters*. If every stock matched, the list would be the whole market again.

## Why so few, and why that is good

On the single day this book's example was generated (an anecdote, not a statistic), exactly one NIFTY 50 stock matched the pullback setup. That is normal, not a bug. For a stock to qualify it must be in a genuine uptrend *and* currently sitting within 2% of a rising 20-day EMA — a narrow window in time. Most of the time a stock is either not trending up, or already extended well above the EMA (in which case the "pause" already happened and chasing it is late).

Notice what the screen has *not* said: it has not said anything is cheap, or good, or going up. It has only reported a *condition* — an uptrending stock currently near its dynamic support. That is a description, and it is yours to interpret or ignore.

## Summary

- The pullback setup = uptrend + rising 20-day EMA + price within a tolerance band of that EMA.
- The `regime` gate means the screen can only ever fire in an uptrend.
- The band uses `abs()` so a small dip through the EMA still counts — levels are zones, not lines.
- Scarcity of matches is a feature: a screen that filters nothing has no value.

Next: the mirror image from the other family — RSI-2 mean reversion.
