# 9. Line Break and Kagi Charts

## The other two reversal-based charts

Renko and P&F are the most famous noise-free charts, but they have two cousins worth knowing: **line break** and **Kagi**. Both, like Renko, abandon time and only draw when price *reverses* by a meaningful amount. They complete the family of "movement, not time" charts.

## Line break charts

A **line break** chart draws a vertical line in the direction of the trend, but — and this is the key — a **new line is drawn only when price closes beyond a prior extreme**, otherwise nothing is drawn.

### The 3-line break rule (the default)

- In an **uptrend**, a new *up* line is drawn only when price **closes above the high of the previous 3 lines**. If it does not, no line is drawn.
- In a **downtrend**, a new *down* line is drawn only when price **closes below the low of the previous 3 lines**.
- A **reversal** occurs when price closes beyond the 3-line extreme in the opposite direction — flipping the chart from up-lines to down-lines.

The "3-line break" is what gives the chart its noise-filtering power: a move is only *recorded* if it is strong enough to break through three prior lines. Small, weak moves are simply not drawn. The result is a chart of **significant, confirmed moves** — cleaner than candlesticks, but (unlike Renko) still based on *closing prices*, not fixed bricks.

### What line break is good for

- **Confirmed trend** — the lines only advance when price genuinely pushes to new extremes, so an uptrend on a line break chart is a *confirmed* uptrend, not a choppy one.
- **Reversal signals** — a flip from up-lines to down-lines is a clear, mechanical "the trend has broken" signal.

### The caveat

Like Renko, a line break reversal is *confirmed after the fact* — you see the trend change only once price has already broken the 3-line extreme. And the "3" is a parameter: a 2-line break is more sensitive (more whipsaw); a 5-line break is slower but more certain.

## Kagi charts

**Kagi** (Japanese for "key") is a chart that switches between **thick and thin vertical lines** to signal trend, and it has no time axis and no fixed brick size — instead, it reverses on a **set reversal amount** (a fixed rupee value, a percentage, or an ATR multiple).

### How Kagi works

- Price moving in the current direction extends the current **vertical line**.
- When price reverses by the **reversal amount**, the line changes direction (a "shoulder") and the chart begins a new segment.
- The line is drawn **thick ("yang")** when price rises above the prior high, and **thin ("yin")** when it falls below the prior low — the thickness showing whether the market is making new highs (strength) or new lows (weakness).

### What Kagi is good for

- **Trend and its health** — the thick/thin distinction tells you at a glance whether the market is in a phase of strength (thick line, new highs) or weakness (thin line, new lows).
- **Support/resistance and reversals** — the shoulders (where the line changes direction) are natural swing points, and a thick-to-thin flip is a trend-change signal.

### The caveat

Kagi's behaviour is entirely determined by the **reversal amount**, and there is no consensus default — a percentage or ATR-scaled reversal is more robust than a fixed rupee amount, for the same reason as Renko's brick size. As with all the reversal charts, reversals are confirmed only after price has already moved the reversal amount.

## The family, completed

Together, the four reversal-based charts — Renko, Point & Figure, line break, and Kagi — make a coherent family:

| Chart | Drawn on | Reversal | Unique strength |
|-------|----------|----------|-----------------|
| Renko | Fixed brick | 2 bricks | Cleanest trend |
| P&F | Fixed box | 3 boxes | Trendlines + price targets |
| Line break | 3-line close | 3-line break | Confirmed (close-based) trend |
| Kagi | Reversal amount | Set amount | Thick/thin strength signal |

They all share the same core idea — **movement matters more than time** — and they differ in *how* they define a "significant" move. Knowing all four lets you choose the lens that matches what you are trying to see.

## Summary

- Line break draws only on a close beyond the prior 3 lines; reversal = a 3-line break.
- Kagi switches thick/thin lines on a set reversal amount; thick = new highs (strength), thin = new lows.
- Both remove time and small moves; both confirm reversals after the fact.
- Together with Renko and P&F, they form the "movement, not time" family.

Next: the logarithmic scale — the insight that unifies all of it.
