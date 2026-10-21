# 8. Screen 2 — RSI-2 Mean Reversion

## Fade the extreme, but only in a healthy stock

From *Swing Trading*, Chapter 7: the **RSI-2 mean reversion** is the opposite of the pullback. Instead of favouring strength, it looks for a stock that has been *punished* — pushed down so hard, so fast, that the short-term move is stretched — but which is still healthy over the long term. The book's two rules are:

1. **RSI-2 closes below 5** — the short-term stretch, measured with the fast oscillator from Chapter 5.
2. **Price above the 200-day MA** — the long-term filter that keeps the setup out of broken, downtrending stocks.

The second rule is the one beginners miss, and the one that matters. An oversold reading on a stock that is also *below* its 200-day MA is not a dip — it is a downtrend. The 200-day filter is what separates "stretched within a long-term uptrend" (the setup) from "falling knife" (not the setup).

## The code

Add the threshold constant up with the config, and the screen below:

```python
RSI2_OVERSOLD = 5           # RSI-2 below this = the reversion setup


def rsi2_setup(close, rsi2, ma200):
    """True when a stock is short-term oversold but still above its 200-day MA."""
    price = close.iloc[-1]
    oversold = rsi2.iloc[-1] < RSI2_OVERSOLD
    above_long_term = price > ma200.iloc[-1]
    return oversold and above_long_term
```

Read it — it is deliberately short, because the idea is two filters and nothing else:

- **`rsi2.iloc[-1] < RSI2_OVERSOLD`** is the stretch test: today's RSI-2 is below 5.
- **`price > ma200.iloc[-1]`** is the health test: price is still above its 200-day moving average.
- Both must be true (`and`), or the screen returns `False`.

Notice there is **no regime check here**, unlike the pullback. That is faithful to the book: RSI-2 reversion is a *range and healthy-uptrend* play, not a trend play. The 200-day MA filter does the same job the regime gate did for the pullback — it keeps the setup out of the wrong conditions — just expressed differently.

## Wire it into the run

Extend the loop to compute RSI-2, the 200-day MA, and this second screen:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        continue

    close = df["Close"]
    ema20 = ema(close, 20)
    ma50 = sma(close, 50)
    ma200 = sma(close, 200)
    rsi2 = rsi(close, 2)

    regime = detect_regime(close, ma50)
    pullback = pullback_setup(close, ema20, regime)
    oversold = rsi2_setup(close, rsi2, ma200)

    flags = []
    if pullback:
        flags.append("Pullback setup")
    if oversold:
        flags.append("Oversold (RSI-2)")
    flag = " · ".join(flags) if flags else "—"

    print(f"{symbol}: {regime:10s} {flag}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

Now each stock can show one of three outcomes: a single flag, *both* flags (a stock can, in principle, be both in a pullback *and* short-term oversold), or `—`. A stock flagged "Oversold (RSI-2)" is one the book's reversion family would describe as stretched-but-healthy — nothing more.

## What the two screens together mean

You now have one screen from each family, which is the whole point of the framework:

- **Pullback continuation** fires in **uptrends** — it trades *with* the trend.
- **RSI-2 reversion** fires on **stretched, healthy dips** — it fades the *extreme*.

Both are gated so they can only fire in the conditions the book says they belong in. The regime read from Chapter 6 is what keeps them apart: the pullback needs an uptrend; the reversion needs long-term health regardless of the short-term label. That one-two structure — read the regime, then pick the matching setup — *is* the framework, and it is now running.

## Summary

- RSI-2 reversion = RSI-2 below 5 **and** price above the 200-day MA.
- The 200-day filter is what stops an oversold reading from being mistaken for a "dip" inside a downtrend.
- No regime gate here — the 200-day MA does the equivalent filtering job.
- The two screens are one from each family: trend-following and mean-reversion.

Next: stop printing to the terminal and build the actual dashboard.
