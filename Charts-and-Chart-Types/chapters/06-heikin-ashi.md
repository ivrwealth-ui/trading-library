# 6. Heikin-Ashi Charts

## Candles, smoothed for trend

**Heikin-Ashi** ("average bar" in Japanese) is a variation of the candlestick chart that *recalculates* each candle from averages, smoothing out the noise. It is the bridge between candlesticks and the reversal-based charts that follow — it keeps the familiar candle *look*, but transforms what each candle *shows*.

## How it differs from a candlestick

A Heikin-Ashi candle is not plotted from the raw OHLC. Instead, each of its four values is a **running average**:

- **Close** = average of (open + high + low + close) — the "centre" of the period.
- **Open** = the midpoint of the *previous* Heikin-Ashi candle's open and close.
- **High** = the highest of (high, open, close).
- **Low** = the lowest of (low, open, close).

Because the open is derived from the *previous* candle, the whole chart becomes a **smoothed, connected** series — the wicks shrink, the bodies flow into one another, and the chart looks like a smooth ribbon of colour rather than a jagged set of individual candles.

## What smoothing buys you

The smoothing does one thing superbly: **it makes the trend unmistakable.**

- In an **uptrend**, Heikin-Ashi candles are predominantly *green*, with small lower wicks and few or no upper wicks — a smooth upward ribbon.
- In a **downtrend**, they are predominantly *red*, with small upper wicks — a smooth downward ribbon.
- A **trend change** shows up as a candle with a small body and wicks on *both* sides (indecision) — a visible pause before the colour flips.

This is the central benefit: **Heikin-Ashi removes the choppiness that makes a candlestick chart look like noise, and leaves the trend naked.**

## The critical caveat: it does not show true prices

The trade-off is real and must be understood:

> **Heikin-Ashi candles do not show the actual open, high, low, or close.**

Because each value is averaged, the chart's *visual* prices are not the market's real prices. This has two consequences:

1. **Do not use Heikin-Ashi for exact entries/exits.** The "close" you see is an average, not the price you would actually trade at. Your order should be based on the *real* price, not the smoothed one.
2. **Do not mix it with price-exact analysis.** If you place a stop "at the Heikin-Ashi low", you are placing it at an averaged, imaginary level — wrong.

Heikin-Ashi is therefore a **trend-visualisation tool**, not an **execution tool**. Use it to *see* the trend and to *time* entries in the direction of that trend (entering on the real chart when the Heikin-Ashi ribbon turns), but execute on real prices.

## How to use Heikin-Ashi well

A clean workflow:

1. **Use Heikin-Ashi to identify the trend** — is the ribbon green (up) or red (down)?
2. **Enter only in the direction of the ribbon** — buy pullbacks in a green ribbon, avoid shorting it.
3. **Watch for the indecision candle** (small body, two wicks) as the early warning of a trend change.
4. **Execute on real prices** — switch to a regular candlestick (or use the actual last price) for the actual entry, stop, and target.

## Heikin-Ashi vs. the reversal-based charts

Heikin-Ashi smooths *within* the time-based framework — it keeps time on the horizontal axis, but averages the prices. The next three chapters (Renko, P&F, line break) go further: they **abandon time** entirely, drawing a new mark only when price has *moved* by enough. Heikin-Ashi is the natural stepping stone to that idea — it is the first chart in this book whose whole purpose is *removing noise to reveal trend*.

## Summary

- Heikin-Ashi recalculates candles from running averages, smoothing the chart into a trend ribbon.
- It makes the trend unmistakable: green ribbon = up, red = down, indecision candle = change.
- Critical caveat: it does not show real prices — use it for *seeing* the trend, not for exact entries/exits.
- It is a bridge to the reversal-based charts, which abandon time entirely.

Next: Renko — the first chart that removes time.
