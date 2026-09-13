# 5. Candlestick Charts

## The market's default language

The **candlestick chart** is the most widely used chart type in the world — and for good reason: it renders the same OHLC data as a bar chart, but in a form that the human eye reads *instantly*. It is the language most of trading's written tradition (patterns, psychology, "the battle between buyers and sellers") is expressed in.

## Anatomy of a candle

A candle has two parts:

- **The body** — a filled rectangle between the **open** and the **close**. If the close is above the open, the body is "bullish" (usually green); if below, "bearish" (usually red).
- **The wicks (or shadows)** — thin lines above and below the body, marking the **high** and **low**.

So a single candle encodes all four prices, *and* colour-codes the direction, *and* shows the body-vs-wick proportions — three layers of information at a glance.

## Reading the body and wicks

The real power of candles is that the **proportions** tell a story about who controlled the period:

- **Long body, small wicks** — decisive; one side dominated from open to close.
- **Small body, long wicks** — indecision; price swung far but settled near where it started.
- **Long lower wick, small body near the top** — sellers pushed price down, but buyers rejected the low and drove it back up (a "hammer", if it comes after a decline).
- **Long upper wick, small body near the bottom** — buyers pushed up, sellers rejected it ("shooting star", if after a rise).

The general principle: **the wicks show rejection; the body shows conviction.** A candle with a long wick in one direction and a body in the other is a *rejection* of that direction — a potential reversal.

## The classic patterns

A handful of well-known patterns (all *reversal* signals, and all probabilistic — not guarantees):

- **Doji** — open and close are nearly equal; a small body with wicks. Complete indecision; often marks a pause or turn.
- **Hammer / hanging man** — long lower wick, small body near the top. After a *decline*, a hammer suggests buyers are stepping in; after a *rise*, the same shape (hanging man) suggests sellers may be.
- **Shooting star / inverted hammer** — long upper wick, small body near the bottom; a potential top after a rise.
- **Engulfing** — a candle whose body *fully engulfs* the prior candle's body, in the opposite direction; a strong reversal signal.
- **Marubozu** — a body with almost no wicks; maximum conviction in one direction.

The honest caveat about all patterns: **they are tendencies, not certainties.** A hammer is a *hypothesis* ("buyers may be stepping in"), to be confirmed by the next candle and by the broader context — never a standalone buy signal.

## What candlesticks are good for (and not)

**Good for:**
- Fast visual reading of direction, volatility, and the intra-period battle.
- Spotting *rejection* and *indecision* at key levels (support/resistance) — which is where patterns are most meaningful.
- The entire body of candlestick-pattern literature.

**Not good for:**
- **Clean trend** over long horizons — candles are noisy; for a decade-long trend, a line or log chart is clearer.
- **Objective signals** — individual candles are *visual* and partly subjective; for a purely mechanical signal, the reversal-based charts (Renko, P&F) are more precise.

## Candles and the foundations

To connect back to Chapter 2's three questions: a candle keeps **all four prices**, is **time-based**, and can be plotted on **linear or log scale**. Its special virtue is that it is the richest *time-based* presentation of the full price record — which is why it is the default.

## Summary

- A candle = body (open–close) + wicks (high–low), colour-coded for direction.
- Body shows conviction; wicks show rejection; proportions tell who controlled the period.
- Classic patterns (doji, hammer, engulfing, etc.) are probabilistic reversal *hypotheses*, not certainties.
- Best for fast visual reading and rejection/indecision at levels; noisy for very long horizons.

Next: Heikin-Ashi — candles, smoothed for trend.
