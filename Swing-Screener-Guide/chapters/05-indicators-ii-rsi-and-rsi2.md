# 5. Indicators II — RSI and RSI-2

## Oscillators measure the extreme

From *Swing Trading*, Chapter 2: an **oscillator** measures whether price is stretched too far to one side. The one this framework uses is the **Relative Strength Index (RSI)**, which is bounded between 0 and 100. Readings near the top are "overbought", near the bottom "oversold".

Crucially — and the book is blunt about this — overbought/oversold only reliably means "likely to pause" **in a range**. In a strong trend, RSI can stay extreme for a long time. That is why RSI is the engine of the *reversion* family, not the trend family, and why our reversion screen (Chapter 8) adds a second filter to keep it out of downtrends.

## The one function

Add this function to `screener.py`:

```python
def rsi(series, period):
    """
    Relative Strength Index over `period` bars, using simple averages.
    RSI-2 (period=2) is the Connors & Alvarez short-reversion oscillator.
    """
    delta = series.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi_vals = 100.0 - (100.0 / (1.0 + rs))
    return rsi_vals.replace([float("inf")], 100.0).fillna(50.0)
```

Read it line by line — this is the most "mathematical" block in the whole book, and it is only eight lines:

- **`series.diff()`** is the day-over-day change: today's close minus yesterday's. A list of moves.
- **`delta.clip(lower=0.0)`** keeps only the *up* moves (any negative change is set to zero) — these are the "gains". **`-delta.clip(upper=0.0)`** keeps only the *down* moves, made positive — the "losses".
- **`gain.rolling(period).mean()`** and its loss twin are the average gain and average loss over the last `period` days.
- **`rs = avg_gain / avg_loss`** is the "relative strength": how much the stock rose, on average, versus how much it fell.
- **`100 - (100 / (1 + rs))`** squeezes that ratio onto the 0–100 scale. If gains and losses are equal (`rs = 1`), RSI is 50. If there are no losses at all, RSI is 100.
- The last line handles two edge cases: no losses at all gives `rs` of infinity (RSI should read 100), and a completely flat two days gives 0 ÷ 0 (we call that neutral 50).

For **RSI-2** you call the same function with `period=2`. A two-day window makes it jump to its extremes fast, which is exactly what makes it useful for spotting short-term stretch — and exactly why the reversion screen uses it. A conventional RSI-14 is the same function with `period=14`, and we compute it too, as a gentler reference value. (Because this function uses simple averages rather than Wilder's smoothing, its readings will not exactly match the RSI on TradingView or your broker's charts.)

## Compute them for one stock

Replace the bottom of `screener.py` again, this time to print both RSIs alongside the close:

```python
df = fetch("RELIANCE")
close = df["Close"]

rsi2 = rsi(close, 2)
rsi14 = rsi(close, 14)

print(f"last close:   {close.iloc[-1]:.2f}")
print(f"RSI-2:        {rsi2.iloc[-1]:.1f}")
print(f"RSI-14:       {rsi14.iloc[-1]:.1f}")
```

Run it:

```bash
python3 screener.py
```

You should see something like:

```
last close:   1226.40
RSI-2:        18.2
RSI-14:       42.0
```

Notice the difference in *behaviour* between the two windows: RSI-2 moves far more than RSI-14. A stock down three days in a row can push RSI-2 into the single digits while RSI-14 stays near the middle. That volatility is a feature for the reversion setup and a nuisance elsewhere — which is why the book's discipline is to use RSI at *extremes in ranges*, not as a free-floating signal.

## Summary

- RSI maps recent gains versus losses onto a 0–100 scale; 50 is neutral, high is overbought, low is oversold.
- RSI-2 is the same formula with a 2-day window — a fast, sensitive short-term oscillator.
- Overbought/oversold is meaningful in ranges; in trends it can simply mean "strong".
- The function is one general formula called with different `period` values.

Next: the concept that ties the whole framework together — is the stock trending or ranging?
