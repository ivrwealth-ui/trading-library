# 2. Price, Time, and Scale: The Foundations

## The three axes every chart rests on

Every chart, whatever its type, is built from the same raw material — **price** — arranged along a **time** axis on a particular **scale**. Before any chart type can be understood, these three foundations must be clear, because every chart type in this book is a *variation* on how these three are used.

## Price: the four data points

For any trading period, price is captured as four numbers — **O, H, L, C**:

- **Open (O)** — where the period started.
- **High (H)** — the highest price reached.
- **Low (L)** — the lowest price reached.
- **Close (C)** — where the period ended.

These four points are the complete price record of any period. Different chart types use different subsets:

- A **line** chart uses only **C**.
- A **bar** or **candlestick** chart uses all **four**.
- A **Renko** or **P&F** chart uses only the **extremes that matter** (H and L, filtered by a move threshold).

So the first question for any chart type is simply: **which of O, H, L, C does it keep?**

## Time: the axis most charts take for granted

Most charts are **time-based**: they draw a new mark for every fixed period — one bar per day, per hour, per minute, per week. Time is the horizontal axis, and every period is *equally wide*, whether or not anything interesting happened in it.

This is so universal that we forget it is a *choice* — and it has a real cost: **a time-based chart gives equal space to a quiet day and a violent day.** In a choppy market, most of the chart is "empty" movement — and the noise drowns the signal.

The reversal-based charts in this book (Renko, P&F, line break, Kagi) reject this assumption: they draw a new mark **only when price has moved enough to matter**, so the horizontal axis becomes *movement*, not time. That is the single most important difference between chart families.

## Scale: linear vs. logarithmic

The vertical axis has a scale, and the scale is a profound choice:

- **Linear scale** — equal *price points* get equal vertical distance (₹100 to ₹200 is the same height as ₹1,100 to ₹1,200).
- **Logarithmic scale** — equal *percentage* changes get equal vertical distance (a 20% move is the same height whether it is ₹100 → ₹120 or ₹1,000 → ₹1,200).

The scale matters enormously for two reasons:

1. **Over long horizons and wide price ranges, linear charts distort.** A stock that grew from ₹100 to ₹2,000 shows a meaningless, compressed early history and an exaggerated recent history on a linear chart. The log chart shows the *true* relative journey.
2. **Price action is fundamentally *relative*, not absolute.** Support, resistance, trendlines, and patterns all operate on *percentage* moves — a 10% pullback means the same thing at ₹500 as at ₹5,000. The log scale captures this; the linear scale hides it.

This is the "one-dimensional" insight developed fully in Chapter 10 — for now, hold the idea: **the log scale removes the absolute-price dimension and leaves only relative change, which is what price action actually is.**

## The three questions for any chart

So, to understand any chart type, ask three questions:

1. **Which of O, H, L, C does it keep?** (How much price information is retained?)
2. **Is it time-based or movement-based?** (Is the horizontal axis time, or significant price moves?)
3. **What scale is it on?** (Linear, or logarithmic?)

Every chapter in this book answers these three questions for its chart type — and they are the key to understanding *why* each chart is good at what it is good at.

## Summary

- Price is captured as O, H, L, C; different charts keep different subsets.
- Time-based charts give every period equal space; movement-based charts only draw on significant moves.
- Linear scale = equal points; log scale = equal percentages — and percentage is what price action actually operates on.
- Three questions for any chart: which OHLC, time- or movement-based, what scale?

Next: the simplest chart of all — the line chart.
