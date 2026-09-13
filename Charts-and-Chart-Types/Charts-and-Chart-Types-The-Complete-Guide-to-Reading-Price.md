# Charts and Chart Types: The Complete Guide to Reading Price

## From line to Renko, Point & Figure, and the log scale — what every chart type shows, why it matters, and how to use it — with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading and investing involve substantial risk of loss, including the possible loss of principal. Past performance never guarantees future results.
- All examples, figures, and historical observations are illustrative. A chart type is a *lens* on price — it does not predict, and no chart type guarantees any outcome.
- Data, costs, and regulatory details change over time. Always verify current figures and consult a qualified adviser before acting.
- Nothing in this book should be read as a promise of profit or a guarantee that any chart-reading method will be profitable.

By reading this book, you agree that you are solely responsible for your own trading and investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches **chart types** — the different ways of *visualising* the same underlying price data, and why the choice of chart changes what you see and how you should act. It is aimed especially at the chart types most people have never properly understood: **Renko**, **Point & Figure**, **line break**, **Kagi**, **Heikin-Ashi**, and the **logarithmic scale**.

- **Chapters 1–2** establish why charts matter at all, and the two foundations every chart rests on: *price* and *time* (and the *scale* that links them).
- **Chapters 3–6** cover the familiar time-based charts: line, area, bar, candlestick, and Heikin-Ashi.
- **Chapters 7–9** cover the *noise-reducing, reversal-based* charts: Renko, Point & Figure, line break, and Kagi — the ones that strip out time (and much of the noise) to reveal pure trend.
- **Chapter 10** is the insight that unifies it all: the **logarithmic scale**, and how it reduces price to a single, pure dimension.
- **Chapter 11** is the practical close: how to choose the right chart for the job.
- The **appendix** is a one-page reference of every chart type.

A note on language: this book describes what each chart type *shows* and how it is *used* — never what you "should" buy. You are responsible for your own decisions.

---

## Table of Contents

1. Why Charts Matter
2. Price, Time, and Scale: The Foundations
3. Line and Area Charts
4. Bar (OHLC) Charts
5. Candlestick Charts
6. Heikin-Ashi Charts
7. Renko Charts
8. Point & Figure (P&F) Charts
9. Line Break and Kagi Charts
10. Log Scale and the One-Dimensional Insight
11. Choosing the Right Chart for the Job

Appendix — Chart-Type Quick Reference

---


# 1. Why Charts Matter

## Price is information; a chart is how you read it

Every trading decision, in the end, is a decision about **price** — about what the market has done, what it is doing, and what that implies. A chart is simply the *visual language* for reading that price history. Understanding chart types matters because **the choice of chart changes what you see** — and what you see shapes what you conclude.

## The single most important fact about charts

Here is the fact that this whole book is built on:

> **A chart is not the data. A chart is a *decision about how to present* the data.**

The underlying reality is the same — a sequence of prices over time. But a line chart, a candlestick chart, a Renko chart, and a Point & Figure chart all *present* that sequence differently, because each makes a different **choice about what to keep and what to discard**:

- A **line chart** keeps only the closing prices and discards everything else.
- A **candlestick** keeps open, high, low, and close, and discards everything in between.
- A **Renko chart** keeps only "significant" price moves and discards *time itself*.
- A **Point & Figure chart** keeps only reversals of a certain size and discards time *and* most small moves.

Each of these is a *filter*. The skill of chart reading is knowing **what each filter keeps, what it throws away, and therefore what it is good for.**

## Why the choice of chart matters

Two reasons the choice is consequential, not cosmetic:

### 1. Charts decide what "counts" as a move

On a candlestick chart, every single price tick counts — so a noisy, choppy market looks like a wall of meaningless wiggles. On a Renko chart, only moves larger than a fixed "brick" size count — so the same noisy market looks like a clean trend. The *same data*, two different conclusions about whether there is a trend at all.

### 2. Charts encode your assumptions about time and scale

- **Time-based charts** assume that *time* is the meaningful axis — a new bar for every fixed period (minute, day, week).
- **Reversal-based charts** (Renko, P&F) assume that *movement* is the meaningful axis — a new mark only when price has actually *moved* by enough.
- **Log charts** assume that *percentage change* is what matters, not absolute points.

Each assumption is a lens, and the lens you choose determines what the chart can show you.

## The honest caveat

A chart is a *representation*, and every representation loses something. No chart type is "the truth"; each is a simplification that is *good at some things and blind to others*. The master is not the person who uses one chart type fanatically, but the person who knows **what each chart type is for** and chooses deliberately — which is exactly what the rest of this book teaches.

## Summary

- A chart is a *decision about how to present* price data, not the data itself.
- Every chart type keeps some information and discards the rest — it is a filter.
- The choice matters because charts decide what "counts" as a move and encode assumptions about time and scale.
- No chart is "the truth"; each is good at some things and blind to others.

Next: the two foundations — price and time — and the scale that links them.


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


# 3. Line and Area Charts

## The simplest lens: closing prices only

The **line chart** is the oldest and simplest chart type: it connects the **closing prices** of each period with a single continuous line. The **area chart** is the same line, with the space beneath it filled in.

Both are the answer to the three foundation questions (Chapter 2): keep **only Close**, plot on **time**, and (usually) on a **linear or log scale** as chosen.

## What a line chart keeps and discards

- **Keeps:** the close of each period — the single most important price, because it is where the market *settled*.
- **Discards:** the open, the high, the low, and everything that happened *within* the period.

That discarding is the point. A line chart is deliberately **minimalist**: it shows the *outcome* of each period (where it closed) and hides the *struggle* (the intra-period highs and lows). This makes it the clearest possible picture of **trend and closing-level structure**.

## What a line chart is good for

1. **The long view.** Over years or decades, the intra-period noise that bars and candles show is irrelevant — what matters is where price settled. A line chart of 20 years of a stock is the cleanest picture of its long-term compounding.
2. **Trend identification.** Because a line chart removes intra-period noise, the *direction* of the line is unmistakable. A rising line is an uptrend; a falling line, a downtrend.
3. **Support and resistance.** Connecting the *closing* lows and highs gives clean, meaningful levels — because a close is a more significant "touch" than an intraday wick.

## What a line chart hides

The price you pay for that clarity is **lost intra-period information**:

- A day that closed *unchanged* but swung 10% intraday shows as a flat line — the volatility is invisible.
- You cannot see **wicks, shadows, or the battle** between buyers and sellers within each period.

If you care about *how* price got to its close (rejections, intraday reversals, the psychology of the fight), a line chart will not show it — you need bars or candles (next chapters).

## The area chart

The **area chart** is a line chart with the region below the line shaded. It adds nothing analytically — it is a *visual* enhancement that makes the trend "feel" more like a mountain range. Its only real use is emphasis: the shaded area makes a long uptrend or downtrend more visually obvious at a glance.

## When to reach for a line chart

- You want the **cleanest possible trend** without intra-period noise.
- You are looking at a **long horizon** where closes are all that matter.
- You want **simple, unambiguous support/resistance** from closes.

When you instead need to see *how* price moved within each period — rejections, reversals, volatility — you move up to bars and candles.

## Summary

- Line/area charts keep only the close; area just shades below the line.
- Best for the long view, clean trend, and closing-level support/resistance.
- They hide intra-period volatility and the buyer/seller battle.
- Choose them for clarity of *outcome*; choose bars/candles for the *process*.

Next: the bar (OHLC) chart — keeping all four prices.


# 4. Bar (OHLC) Charts

## Keeping all four prices

The **bar chart** (also called an OHLC chart) keeps **all four** price points — Open, High, Low, Close — and displays them as a single vertical mark per period. It is the first chart type in this book that shows the *full* price record, not just the outcome.

## How to read a bar

Each bar is a vertical line connecting the period's **low** and **high**, with two small horizontal ticks:

- The **left tick** marks the **open**.
- The **right tick** marks the **close**.

So a single bar answers, at a glance: *where did price open, how high did it go, how low did it go, and where did it close?* If the close is above the open, the period finished higher; if below, lower.

## What a bar chart gives you over a line chart

The bar chart adds the **intra-period story** that a line chart discards:

1. **The range** — the distance between high and low is the period's *volatility*. A series of wide bars means a volatile market; narrow bars, a quiet one.
2. **The open-to-close direction** — whether the period *gained* or *lost*, and by how much.
3. **Position of the close within the range** — a close near the *high* suggests buyers were in control into the close; a close near the *low* suggests sellers were.

This last point is the seed of candlestick analysis (next chapter): *where* the close sits within the bar's range is a meaningful signal about who won the period.

## What a bar chart is good for

- **A complete price picture** without the visual weight of candles.
- **Reading volatility** — the width of the bars *is* the volatility, and patterns of widening/narrowing bars (volatility expansion and contraction) are visible directly.
- **Precision** — because the open and close are exact ticks, you can read exact levels where price opened and settled.

## What a bar chart is less good at

- **Visual speed.** Bars are *slower to read* than candles, because the bullish/bearish distinction is not colour-coded and the body (open-to-close) is not filled. The eye has to *decode* each bar rather than *see* it instantly.
- **Pattern recognition.** The classic candlestick patterns (hammer, engulfing, doji) are harder to spot as ticks than as filled bodies with shadows.

## Bar vs. candlestick: the honest comparison

A bar chart and a candlestick chart contain *exactly the same information* — both are OHLC. The only difference is **presentation**:

- The **bar** renders the OHLC as a line with ticks — precise, but the eye must work to read it.
- The **candlestick** renders the OHLC as a filled body with wicks — the bullish/bearish distinction and the "battle" are *visually instant*.

For most people, the candlestick is the better default (speed and pattern-recognition), while the bar is preferred when exact, unembellished precision is wanted. Both are valid; the information is identical.

## Summary

- A bar keeps all four prices: low–high line, left tick = open, right tick = close.
- It adds range (volatility) and open-to-close direction over a line chart.
- Position of the close within the range is the seed of candlestick analysis.
- Bar and candlestick carry identical data; they differ only in presentation.

Next: the candlestick chart — the market's default language.


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


# 8. Point & Figure (P&F) Charts

## The oldest, and the most powerful, noise-free chart

**Point & Figure (P&F)** is the grandparent of all the reversal-based charts — invented in the 19th century, before computers, when prices were read off a ticker tape and plotted by hand. It removes both **time** and **small moves**, and it adds something none of the other charts have: a **built-in method for projecting price targets.**

If Renko shows the trend naked, P&F shows the trend *and* the target.

## How P&F is built

Two parameters define a P&F chart:

1. **Box size** — the fixed price movement required to plot a mark (an **X** for rising, an **O** for falling).
2. **Reversal amount** — how many boxes price must move *against* the current column to start a new column (classically **3 boxes**).

The construction rules:

- In a **rising column**, each box of upward movement plots an **X**. Small downward moves are ignored (not plotted).
- In a **falling column**, each box of downward movement plots an **O**. Small upward moves are ignored.
- A **new column** begins only when price reverses by the **reversal amount** (3 boxes) in the opposite direction.

The chart is therefore a series of **alternating columns of X's and O's** — each column a swing, each swing at least 3 boxes. This is what makes P&F remarkable: it distils an entire price history into just the **significant swings**, with all the minor noise removed.

## The classic 3-box reversal logic

The "3-box reversal" is the heart of P&F's power: **only a move of 3 boxes (or more) against the trend is considered a "real" reversal.** Anything smaller is noise, deliberately ignored. The result is a chart that answers, with total objectivity, the question every trader asks: *is the trend still intact, or has it genuinely reversed?* A new column of O's after a column of X's means a genuine 3-box reversal — not a head-fake.

## What P&F is uniquely good at

### 1. Support and resistance, with total clarity

Because P&F ignores time and noise, horizontal levels are *crystal clear*. A price where columns repeatedly stop and reverse shows as a distinct horizontal line of tops or bottoms — far cleaner than on any time-based chart. P&F traders read support and resistance directly off the X/O columns.

### 2. Trendlines at 45 degrees

P&F has a native way of drawing trendlines: a **bullish support line** rising at 45° beneath a column of X's, and a **bearish resistance line** falling at 45° above a column of O's. A break of these lines is a clean trend-change signal — and because they are drawn at a fixed angle, they are objective, not a matter of where the analyst *chooses* to place them.

### 3. Price targets via "counts"

This is P&F's signature feature, and it has no equivalent in any other chart type: **the horizontal count.**

- Count the number of columns in a **congestion area** (a sideways band where columns alternate).
- Multiply by the **reversal amount** (3), then by the **box size**.
- The result is added to (for an upside break) or subtracted from (for a downside break) the breakout level — giving a **projected price target.**

The logic: a wide sideways base means a large "coil" of accumulated energy; when it breaks, the move tends to travel a distance proportional to the base's width. It is a simple, mechanical, and historically useful way to *estimate how far a move might go*.

## How P&F is used

A classic workflow:

1. **Trend:** a column of X's = uptrend; a column of O's = downtrend.
2. **Entry:** enter when a new column begins in your direction (e.g., the first X after a 3-box reversal up from an O column).
3. **Support/resistance:** trade around the clear horizontal levels.
4. **Target:** use the horizontal count to set a *projected* objective — but treat it as a *guide*, not a promise.

## The critical caveats

1. **No time, no volume.** P&F discards both; you cannot see *how long* a base took, or whether it formed on heavy or light volume.
2. **Counts are estimates, not certainties.** The horizontal count is a *tendency*, and it frequently overshoots or undershoots. Use it to frame expectations, never as a guarantee.
3. **Parameter sensitivity.** Box size and reversal amount change the chart profoundly — a 1×3 chart (1% box, 3-box reversal) is a different instrument from a 1×1 or a fixed-rupee chart. As with Renko, an ATR- or percentage-scaled box is more robust than a fixed rupee amount.

## P&F vs. Renko

| | Renko | Point & Figure |
|---|---|---|
| Mark | Bricks | X / O columns |
| Reversal | 2 bricks (typical) | 3 boxes (classic) |
| Time | Removed | Removed |
| Targets | No | Yes (horizontal count) |
| Trendlines | Horizontal only | Horizontal + 45° trendlines |

Renko is the cleanest *trend* picture; P&F is the more powerful *analytical* tool, adding objective trendlines and price-target projection to the same noise-free idea.

## Summary

- P&F plots X (up) and O (down) columns; a new column needs a 3-box reversal; small moves are ignored.
- It distils price into significant swings, with crystal-clear support/resistance.
- Native 45° trendlines give objective trend-change signals.
- The horizontal count projects price targets from congestion width.
- It removes time and volume; counts are estimates, not certainties.

Next: line break and Kagi — the other two reversal-based charts.


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


# 10. Log Scale and the One-Dimensional Insight

## The scale is a lens, and it changes everything

Every chart in this book sits on a **scale**, and the scale is the most under-appreciated choice in all of charting. This chapter develops the insight that has been hinted at throughout: **the logarithmic scale removes the absolute-price dimension and leaves price action as a single, pure dimension — relative change.**

## Linear vs. logarithmic, precisely

- **Linear scale:** equal *price points* get equal vertical distance. From ₹100 to ₹200 is the same height as from ₹1,100 to ₹1,200.
- **Logarithmic scale:** equal *percentage* changes get equal vertical distance. A 20% move — ₹100→₹120 or ₹1,000→₹1,200 — is the *same height* on a log chart.

The difference sounds academic; it is not. It is the difference between a chart that shows the *truth* and a chart that *distorts*, in three concrete ways.

## What the linear scale distorts

### 1. It hides the early years of a big winner

A stock that compounded from ₹100 to ₹2,000 (a 20-bagger) shows, on a linear chart, its first decade compressed into a flat line at the bottom, and its recent moves exaggerated at the top. The *most important* part of the story — the early compounding — is invisible. On a log chart, every 10× gain occupies the *same* vertical height, so the entire journey is visible and correctly proportioned.

### 2. It makes support/resistance and trendlines wrong

Support, resistance, and trendlines are **percentage** phenomena. A 10% pullback to support means the same thing at ₹500 as at ₹5,000 — but on a linear chart, a ₹50 pullback (10% of ₹500) and a ₹500 pullback (10% of ₹5,000) look completely different in size. A trendline drawn on a linear chart over a wide price range is measuring *points*, not *percentages* — and it will break for the wrong reasons.

### 3. It treats "equal price" as "equal importance"

On a linear chart, a ₹10 move at ₹100 looks enormous and a ₹10 move at ₹10,000 looks invisible. But to the *trader*, the question is always *percentage* — what does this move mean for my position? The linear scale keeps answering that question wrong.

## The one-dimensional insight

Here is the idea the whole book has been building toward:

> **Price action is fundamentally one-dimensional: it is about *relative* change, not absolute level.**

Every meaningful concept in technical analysis — trend, support, resistance, breakout, pullback, reversal — is a statement about **percentage moves**, not rupee amounts. A "breakout" is a move *above* a level by a meaningful *percentage*; a "pullback" is a retracement of a *fraction* of the prior move; a "trend" is a sequence of higher *percentage* swings.

The **logarithmic scale strips away the absolute-price dimension** — the raw rupee level — and leaves only that one dimension: **relative change.** This is why log charts are described as making price "one-dimensional" and "pure price action": they remove the distracting, meaningless magnitude and show exactly what price action is made of.

In this sense, the log scale does for the *vertical* axis what Renko and P&F do for the *horizontal* axis: Renko/P&F remove time to leave pure movement; the log scale removes absolute price to leave pure *relative* movement. Both are the same move — **discard the irrelevant dimension.**

## When to use log vs. linear

**Use the logarithmic scale when:**

- The chart spans a **wide price range** (a stock that has moved 5×, 10×, or more).
- You are looking at a **long horizon** (years) where compounding dominates.
- You are drawing **trendlines, support/resistance, or channels** that must reflect percentage behaviour.

**Linear scale is fine when:**

- The chart spans a **narrow range** over a **short horizon** (days to weeks), where the difference between points and percentages is negligible.
- You are trading *absolute* price levels (e.g., intraday points on an index) where the rupee amount genuinely is the unit.

The honest rule of thumb: **for anything longer than a few weeks, or any price that has moved more than a few multiples, default to log.**

## The unifying conclusion

Every chart type in this book is, at bottom, the same idea applied to a different axis:

- **Renko, P&F, line break, Kagi** discard *time* to leave pure **movement**.
- **The log scale** discards *absolute price* to leave pure **relative change**.

Both are acts of **removing the irrelevant dimension** so that the one dimension that matters — *relative price movement* — can be seen clearly. That is the deep unity of the whole subject: **a chart is a lens, and the master chooses the lens that removes exactly the right irrelevancies.**

## Summary

- Linear = equal points; log = equal percentages.
- Linear distorts: it hides early compounding, and it breaks trendlines/support for the wrong reasons.
- Price action is one-dimensional — relative change — and the log scale reveals that single dimension.
- Log discards absolute price, as Renko/P&F discard time; both remove the irrelevant dimension.
- Default to log for anything longer than weeks or any price that has moved several multiples.

Next: putting it all together — choosing the right chart for the job.


# 11. Choosing the Right Chart for the Job

## The master's skill: deliberate selection

Every chart type in this book is good at *some* things and blind to *others*. The difference between a beginner and a master is not knowing more chart types — it is **choosing the right one for the question you are actually asking.** This chapter is a practical decision guide.

## The three questions first

Before picking a chart, ask what you are trying to see:

1. **Am I asking about trend, or about the battle within each period?**
2. **Is time relevant to me, or is movement the only thing that matters?**
3. **Am I comparing percentage moves (relative) or rupee points (absolute)?**

The chart type follows from the answer.

## A decision guide

| What you want to see | Use | Why |
|----------------------|-----|-----|
| Clean long-term trend | Line (or log line) | Closes only; no intra-period noise |
| The full price record, fast | Candlestick | All four prices, colour-coded, instant |
| Precise OHLC, unembellished | Bar (OHLC) | Exact open/close ticks |
| Trend, smoothed | Heikin-Ashi | Averaged candles = naked trend |
| Pure trend, no time/noise | Renko | Bricks only on significant moves |
| Levels, trendlines, price targets | Point & Figure | Clear S/R, 45° lines, horizontal count |
| Confirmed (close-based) trend | Line break | Only draws on 3-line breaks |
| Strength vs. weakness | Kagi | Thick/thin lines = new highs/lows |
| Multi-year compounding correctly | Log scale (any type) | Equal % = equal height |

## The four most common mistakes

1. **Using a linear scale over a decade.** The early compounding is invisible and every trendline is wrong. Use log.
2. **Using Heikin-Ashi (or any averaged chart) for exact entries.** The "close" you see is not a real price. See the trend on Heikin-Ashi; execute on real prices.
3. **Using candlesticks for a multi-year trend.** Candles are noisy; a line or log chart shows a decade of trend far more clearly.
4. **Reading a Renko/P&F chart's horizontal axis as time.** It is *movement*, not time — a long flat stretch of a Renko chart does not mean "the market was quiet for long"; it means "price did not move enough to matter."

## A practical workflow

A disciplined sequence that most professional users follow, whether consciously or not:

1. **Start with the long view on a log scale** (line or candlestick) — establish the *big* trend and the *big* levels.
2. **Zoom in with candlesticks** — read the intra-period battle, rejection, and indecision at those levels.
3. **Switch to Renko or P&F when the market is choppy** — to see whether there is *actually* a trend under the noise, or only noise.
4. **Use P&F's count to frame a target** — as a guide, never a promise.
5. **Execute on real prices, on the real chart** — never on a smoothed or brick-based "price."

## The honest close

The entire subject of chart types reduces to one sentence: **a chart is a filter, and you are the one choosing what to filter.** There is no "best" chart — there is only the chart that *shows you what you are trying to see* and *hides what would mislead you*. The master is not the person who knows the most chart types, but the person who always knows *why* they are looking at the one in front of them.

## Summary

- Choose the chart by the question: trend vs. battle, time vs. movement, percentage vs. points.
- Four mistakes: linear over decades, Heikin-Ashi for entries, candles for long trends, reading Renko as time.
- A workflow: log long view → candlesticks at levels → Renko/P&F in chop → P&F count for targets → execute on real prices.
- A chart is a filter; the master chooses the filter deliberately.

This completes the main text. The appendix is a one-page reference of every chart type.


# Appendix — Chart-Type Quick Reference

This table is a summary, not a substitute for the full chapters.

| Chart | Keeps | Axis | Best for | Watch out |
|-------|-------|------|----------|-----------|
| Line / Area | Close only | Time | Clean long-term trend, closing S/R | Hides intra-period battle |
| Bar (OHLC) | O, H, L, C | Time | Precise full record, volatility | Slower to read than candles |
| Candlestick | O, H, L, C | Time | Fast reading, rejection/indecision, patterns | Noisy over long horizons |
| Heikin-Ashi | Averaged OHLC | Time | Smooth trend ribbon | Not real prices — no exact entries |
| Renko | Bricks (fixed move) | Movement | Pure trend, mechanical reversals | No time; reversal lag |
| Point & Figure | X/O columns | Movement | Levels, 45° trendlines, price targets | No time/volume; counts are estimates |
| Line break | 3-line close breaks | Movement | Confirmed close-based trend | Reversal confirmed late |
| Kagi | Thick/thin lines | Movement | Strength vs. weakness | Depends on reversal amount |

## The scale

- **Linear** = equal points. Use for short horizons, narrow ranges, absolute levels.
- **Log** = equal percentages. Use for long horizons, wide ranges, trendlines, and any price that has moved several multiples.

## The unifying idea

Every chart type is the same move — **discard the irrelevant dimension** — applied to a different axis:

- **Renko, P&F, line break, Kagi** discard *time* to leave pure **movement**.
- **The log scale** discards *absolute price* to leave pure **relative change**.

A chart is a filter; the master chooses which filter to look through.
