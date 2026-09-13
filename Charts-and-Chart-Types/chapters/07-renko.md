# 7. Renko Charts

## The chart that removes time

**Renko** (from the Japanese *renga*, "brick") is the first chart type in this book that **abandons time entirely**. It draws a new "brick" only when price has moved by a fixed amount in one direction — and otherwise draws nothing. The result is a chart made purely of *movement*, where the horizontal axis is no longer time but **significant price change**.

This is the chart type most people misunderstand, and the misunderstanding is usually about a single word: **time.** Renko has no time axis. A Renko chart of a fast-moving day and a slow month can look identical, if the *total movement* is the same. That is the point.

## How Renko is built

Two parameters define a Renko chart:

1. **Brick size** — the fixed price movement required to draw a brick (e.g., ₹10, or 1%, or an ATR multiple).
2. **Reversal amount** — how many bricks price must move *against* the trend to draw a reversing brick (classically **2 bricks**).

The construction rules:

- **A new up-brick** is drawn only when price rises by one full brick size above the previous brick's top.
- **A new down-brick** is drawn only when price falls by one full brick size below the previous brick's bottom.
- **A reversal** happens only when price moves *2× the brick size* in the opposite direction — this is why Renko filters out small pullbacks: a reversal must be *significant*.

If price does not move by a full brick size, **nothing is drawn** — the chart simply waits. This is what removes the noise: countless small wiggles that would clutter a candlestick chart never appear on a Renko chart at all.

## What Renko shows

Because it discards time and small moves, Renko shows **the trend, and only the trend**:

- **Clean trends** — a string of same-coloured bricks is an unambiguous trend, with none of the choppiness a candlestick chart shows.
- **Support and resistance** — horizontal bands where bricks repeatedly reverse or stall are natural, obvious levels.
- **Reversals** — a brick appearing in the *opposite* colour is a clean, mechanical signal that the trend has turned (at least by the reversal amount).

This is why Renko is often described as a **pure price-action** tool: it strips away *when* something happened and leaves only *what* happened (the move), making the trend impossible to miss.

## How Renko is used

A simple, classic Renko workflow:

1. **Trend:** the direction of the current brick colour *is* the trend. Trade with it.
2. **Entry:** enter in the trend direction when a *new brick* prints in that direction (a fresh up-brick in an uptrend).
3. **Exit/reversal:** exit when a **reversal brick** prints (a brick in the opposite colour), which requires a move of 2× the brick size against you.

Because every brick is a fixed-size move, the system is naturally *mechanical* — no judgement about "is this a real trend?" is needed; the bricks answer it.

## The parameter choice: the hidden decision

The entire behaviour of a Renko chart is set by the **brick size**, and the choice is consequential:

- **Small bricks** — more sensitive; capture smaller moves, but more reversals (whipsaw) and more noise.
- **Large bricks** — less sensitive; capture only big trends, but late to enter and exit (give back more of each move).

The right brick size is a *trade-off between responsiveness and noise* — and the honest guidance is that a **volatility-scaled brick** (e.g., a fixed multiple of ATR) is more robust than a fixed rupee amount, because it adapts as the market's volatility changes. A fixed ₹10 brick means something very different on a ₹200 stock than a ₹2,000 stock; an ATR-scaled brick means the same *relative* move in both.

## The critical caveat

Two honest caveats about Renko:

1. **No time axis means no time information.** A Renko chart cannot tell you *how long* a trend took, or how *fast* it is moving. If timing (days, volatility-per-time) matters to you, Renko hides it.
2. **Reversal lag.** A 2-brick reversal means you exit *after* price has already moved 2 bricks against you — the reversal is confirmed only after the fact. This is the price of noise-reduction: certainty about the trend *after* it has turned, not before.

## Renko in the chart-type family

Renko is the clearest expression of the idea that runs through the back half of this book: **movement is more important than time.** It keeps only significant price moves, discards time and noise, and leaves the trend. The next chart — Point & Figure — is its older, more powerful cousin, which adds target-projection to the same idea.

## Summary

- Renko draws a brick only on a fixed-size move; reversal requires a 2-brick move; nothing is drawn otherwise.
- It removes time and noise, leaving only the trend, support/resistance, and clean reversals.
- Trade with the brick colour; enter on new bricks; exit on reversal bricks.
- Brick size is the hidden decision — ATR-scaled bricks are more robust than fixed rupees.
- It shows movement, not time; and it confirms reversals after the fact.

Next: Point & Figure — the oldest and most powerful noise-free chart.
