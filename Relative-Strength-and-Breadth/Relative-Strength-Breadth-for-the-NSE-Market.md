# Relative Strength & Breadth for the NSE Market

## Ranking Stocks, Rotating Sectors and Reading the Health of the Tape

---

**Published by StratLab**

---

**A practical reference for Indian equity-market participants.**

---

> **Disclaimer.** This book is for **education only**. It is not investment advice, not a recommendation to buy or sell any security, and the author is not a SEBI-registered investment adviser. Historical relative-strength and breadth behaviour does not guarantee future results. All figures, ranks and thresholds are illustrative and must be re-checked against current data.

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading involves substantial risk of loss and is not suitable for everyone. You can lose part or all of your trading capital.
- All examples, figures, and historical observations are illustrative. Historical performance never guarantees future results. Strategies described here have worked *historically* in certain conditions; that does not mean they will work in the future or in your specific situation.
- Margin, taxes (STT, stamp duty), brokerage, and other regulatory details change over time. Always verify current rules and costs before trading.
- Nothing in this book should be read as a promise of profit or a guarantee that any strategy will be profitable.

By reading this book, you agree that you are solely responsible for your own trading decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## Table of Contents

1. What Relative Strength Is
2. Computing Relative Strength
3. Relative Strength vs the Market and vs Peers
4. Sector Relative Strength and Rotation
5. Where to Source Relative Strength in India
6. What Breadth Is and Why It Matters
7. The Core Breadth Indicators
8. Breadth Divergences
9. Where to Source Breadth in India
10. The Top-Down Process: Breadth → Sector → Stock
11. Combining RS, Breadth and Price
12. The One-Page Reference

Glossary

---


# 1. What Relative Strength Is

*Part I — Relative Strength*

Relative Strength (RS) is a measure of how one instrument is performing *relative to another* — most often a stock relative to its benchmark (Nifty 50, Nifty 500) or relative to its peers. It is entirely different from the "Relative Strength Index (RSI)", which is a bounded oscillator; the RS in this book is a **ranking of performance**, not a momentum oscillator.

The core idea is elegant: in a market where most stocks follow the index, the stocks that *outperform* the index are the ones attracting sustained institutional demand. RS is the objective, numbers-only way to find them.

## Why RS matters

- **It isolates leadership.** A stock can be falling while its sector rises, or rising while the index falls. RS cuts through the noise of the market's overall direction and tells you *who is leading* and *who is lagging*.
- **It is persistent.** Relative strength is one of the more durable anomalies in markets (the momentum effect documented by Jegadeesh & Titman, 1993, *Journal of Finance*) — stocks that have led tend to keep leading, and stocks that have lagged tend to keep lagging, over intermediate horizons.
- **It respects the market's own verdict.** RS is not your opinion or a story; it is what the market has already voted for with real money.

## The two ways to express RS

1. **RS ratio (price ratio).** Divide the stock's price by the index's level (both normalised to a common start). A rising ratio means the stock is outperforming; a falling ratio means it is lagging. The slope of this ratio line is the visual form of RS.
2. **RS rank / percentile.** Compute each stock's return over a window (commonly 3, 6 or 12 months) and rank all stocks; express the result as a percentile (0–100). A stock in the 90th percentile beat 90% of the market. This is the ranking form used by most screeners.

**How to read:** the *ratio* is best for watching a single stock over time; the *rank* is best for comparing across the whole universe. Use both — the ratio for the story, the rank for the shortlist.


# 2. Computing Relative Strength

## The RS ratio, step by step

1. Choose a benchmark (Nifty 50 for large-caps, Nifty 500 for broader).
2. Normalise both to a common base: `Normalised price = Price ÷ Price at start of window`.
3. Compute the ratio: `RS ratio = Normalised stock ÷ Normalised benchmark`.
4. Plot the ratio over time.

**How to read the ratio line:**

- A **rising** RS line while the index is flat or down = genuine leadership (the stock is doing it on its own, not just drifting up with the tide).
- A **falling** RS line while the index rises = the stock is a laggard in a rising market — it is *underperforming* even as it goes up in price.
- A **breakout in the RS line** (ratio making a new high) often *precedes or coincides with* a price breakout — it is a confirmation that the move is leadership, not just beta.

## The RS rank, step by step

1. Compute the return of every stock in the universe over the chosen window (e.g. 6 months).
2. Sort all returns.
3. Assign a percentile to each (0 = worst, 100 = best).

**How to read the rank:**

- Above ~80th percentile = strong relative strength (leadership).
- Below ~20th percentile = weak relative strength (laggard).
- The **middle** is where most stocks live and where the signal is weakest.

## Choosing the window

The window changes what the RS is measuring:

| Window | What it captures | Use for |
|---|---|---|
| 1–3 months | Short-term momentum | Tactical rotation, trend confirmation |
| 6 months | Intermediate trend | Core ranking, most-used window |
| 12 months | Sustained leadership | Positional / long-horizon selection |

**How to read:** long-horizon RS (12-month) is the most stable and least noisy; short-horizon RS flips quickly. Many practitioners rank on 6-month RS and confirm with 3-month and 12-month to avoid whipsaw.


# 3. Relative Strength vs the Market and vs Peers

## Stock vs benchmark

The most common comparison is the stock against the broad index. But this can mislead in one important way: a stock can show high RS simply because its *whole sector* is strong, not because the stock itself is special.

## Stock vs sector (the missing comparison)

To find true leadership, compare the stock to **its own sector or industry** as well. A stock that is the *strongest in a strong sector* is the true leader; a stock that merely rides a strong sector is a beta bet, not a selection edge.

**How to read the two-layer comparison:**

- **Strong vs market AND strong vs sector** = the genuine leader. Highest conviction.
- **Strong vs market, weak vs sector** = riding the sector's coattails; be sceptical.
- **Weak vs market but strong vs sector** = a relative winner within a weak group (a "best house on a bad street" — sometimes the early sign of a sector turn).
- **Weak vs both** = a laggard; avoid for strength-based selection.

## Building the ranking funnel

A robust top-down funnel ranks in three layers:

1. **Market** (is the index itself healthy? — use breadth, Part II).
2. **Sector** (which sectors are outperforming the index? — sector RS).
3. **Stock** (which stocks lead their sector? — stock RS vs sector).

This is the core process of the entire book, expanded in Part III.


# 4. Sector Relative Strength and Rotation

## Sector RS

Sector RS ranks the NSE's sectoral indices (or sector baskets) by their relative performance. The Nifty sectoral indices — Bank, IT, Auto, FMCG, Metal, Pharma, Realty, PSU Bank, Capital Goods, Oil & Gas, and others — together with thematic indices such as Energy and Infrastructure, are the natural building blocks.

**How to read sector RS:**

- Rank sectors by RS over the chosen window. The **top 2–3 sectors** are where leadership currently resides; the **bottom 2–3** are the laggards.
- **Rotation** is the migration of leadership from one group to another. It is not random — money tends to rotate in a rough economic order: early-cycle leaders (autos, banks, industrials) → mid-cycle (consumption, infra) → late-cycle/defensive (FMCG, pharma, IT in some regimes).
- A sector **rising in the RS ranking** while the market is flat is often the earliest sign of the next leadership group.

## Using sector RS in practice

- **Overweight leaders, underweight laggards.** The simplest application: concentrate attention (and, for active traders, capital) in the top-ranked sectors and avoid the bottom-ranked ones.
- **Watch the RS rank *change*, not just the level.** A sector moving from 8th to 3rd is a more actionable signal than one that has been 1st for a year. Change is where opportunity lives.
- **Confirm with the sector's own price.** A sector's RS means more when the sector's own price is also breaking out or making new highs — RS *and* price together are the strongest statement.


# 5. Where to Source Relative Strength in India

Relative strength is a *computed* metric — few exchanges publish it directly, but the Indian ecosystem offers several tools that calculate it for you.

| Tool | RS capability | Link |
|---|---|---|
| **Tickertape** | Stock vs sector and vs index performance; relative charts | https://www.tickertape.in |
| **Trendlyne** | Relative performance vs Nifty and peers; rankings | https://trendlyne.com |
| **TradingView** | Built-in Compare tool (overlay the index on a percentage scale) and spread/ratio charts (enter a ratio symbol such as `STOCK/NIFTY` to plot the RS line) | https://www.tradingview.com |
| **Chartink** | RS-style scan builders over the full NSE universe | https://chartink.com |
| **Screener.in** | Raw multi-year returns (which you can rank yourself) | https://www.screener.in |
| **NSE India** | Index data and constituents for building your own RS | https://www.nseindia.com |

**How to do it yourself (spreadsheet):** download daily adjusted prices for a stock and for Nifty (from NSE or a data provider), normalise both to 100 at the start of your window, and divide. The slope of that ratio *is* relative strength. It takes ten minutes in a spreadsheet and teaches you more than any ready-made tool.


# 6. What Breadth Is and Why It Matters

*Part II — Breadth*

Breadth measures **how many stocks are participating** in a market move, rather than how far the *index* has moved. The index is a weighted average of a few large names; breadth is the unweighted vote of the whole market. The two can disagree — and when they do, the disagreement is the signal.

**The core insight:** a rising index driven by many stocks is *healthy*; a rising index driven by a handful of heavyweights while everything else falls is *unhealthy*. Breadth is how you tell them apart.

## Why breadth matters

- **It reveals internal strength or weakness** invisible in the index. A new high in Nifty made on *fewer* new highs than the prior peak is a warning.
- **It leads at turning points.** Breadth often peaks or troughs *before* the index does — the participation starts to fade before the top, or broadens before the bottom.
- **It disciplines the trend.** A trend confirmed by breadth is more durable than one running on fumes.


# 7. The Core Breadth Indicators

## 7.1 The Advance-Decline (A/D) Line

The most fundamental breadth measure: each day, count **advancers** (stocks up) and **decliners** (stocks down).

- **Advance-Decline ratio** = `Advancers ÷ Decliners` (or advancers as a % of total).
- **A/D Line** = cumulative running total of `Advancers − Decliners`.

**How to read:** the A/D line should *confirm* the index — making new highs when the index does. A **divergence** (index new high, A/D line not) is the classic early warning of a top; a positive divergence (index lower low, A/D higher low) is the classic sign of a bottom forming. The A/D line is most meaningful over the *broad* universe (all of NSE or Nifty 500), not just Nifty 50.

## 7.2 Breadth ratio / % advancers

The percentage of stocks advancing on a day. When this is persistently high (say, consistently above 60%), the market is broadly healthy; persistently low (below 40%) signals broad weakness.

**How to read:** the *smoothed* version matters more than any single day. A multi-day streak of high breadth is a genuine risk-on signal; a streak of low breadth while the index holds up is distribution.

## 7.3 New Highs vs New Lows

Each day, count stocks making **52-week highs** and stocks making **52-week lows**.

- **High-Low differential** = `New highs − New lows`.
- **High-Low ratio** = `New highs ÷ New lows`.

**How to read:** a market making many new highs and few new lows is in a confirmed uptrend. A market where new highs shrink on each rally is losing momentum. A widely watched bearish breadth signal is a *negative* high-low differential while the index is near its highs. (New highs/lows are best counted over the broad NSE or Nifty 500 universe.)

## 7.4 The McClellan Oscillator and Summation Index

The McClellan family smooths the raw daily A/D data to give a cleaner signal.

- **McClellan Oscillator** = `EMA(19) of (A−D) − EMA(39) of (A−D)`, where A−D is advances minus declines.
- **McClellan Summation Index** = the cumulative total of the oscillator.

**How to read:** the oscillator swings above and below zero and captures the short-term ebb and flow; the summation index is the *trend* of that oscillator and behaves like a smoothed A/D line. Divergences between the summation index and the price index are watched the same way as A/D divergences, but with less noise.

## 7.5 % of stocks above their moving average

The percentage of the universe trading **above its 50-day** (and **200-day**) moving average.

**How to read:** this is one of the cleanest and most intuitive breadth gauges. Above ~60% on the 200-day = broad uptrend; below ~40% = broad downtrend. Extreme readings (above 80% or below 20%) are often short-term overbought/oversold — but in strong trends they can persist, so treat extremes as context, not automatic reversal signals.

## 7.6 Up/Down volume

Breadth of *volume*, not just of price: how much volume went into advancing stocks versus declining stocks.

**How to read:** price breadth shows *how many* stocks; volume breadth shows *how much conviction* is behind them. A rally on rising up-volume is healthier than one on falling up-volume. This is the breadth measure most closely tied to institutional participation.

## The breadth dashboard (what to track daily)

| Indicator | Bullish reading | Bearish reading |
|---|---|---|
| A/D line | New highs with the index | Diverging (lower highs) |
| % advancers (smoothed) | > 60% | < 40% |
| New highs − new lows | Positive and expanding | Negative near index highs |
| McClellan summation | Rising | Falling, diverging |
| % above 200-DMA | > 60% | < 40% |
| Up/down volume | Up-volume dominant | Down-volume dominant |


# 8. Breadth Divergences

The highest-value use of breadth is spotting **divergences** — cases where the index tells one story and breadth tells another.

## The two divergences that matter

- **Bearish divergence (the top warning):** the index makes a *new high*, but breadth (A/D line, new-highs count, % above the 200-DMA) makes a *lower high*. The rally is narrowing — fewer and fewer stocks are carrying it. This is often cited as one of the most historically reliable warnings of a topping market.
- **Bullish divergence (the bottom signal):** the index makes a *new low*, but breadth makes a *higher low*. The decline is losing participation — fewer stocks are making new lows even as the index falls. This often precedes a durable bottom.

**How to read divergences correctly:**

- One divergence reading is a *flag*, not a *trade signal*. Breadth divergences can persist for weeks before the index actually turns.
- Confirm with **price structure** (from Book 1): a breadth divergence plus a price-level break or a failed breakout is the high-confidence combination.
- Divergences are most reliable at **extremes** (after a long advance or decline), and least reliable in the middle of a range.


# 9. Where to Source Breadth in India

Breadth data for the NSE is widely available, though the *quality of the universe* matters (broad NSE or Nifty 500 is better than Nifty 50).

| Tool | Breadth capability | Link |
|---|---|---|
| **Chartink** | Advance/decline, new highs/lows, % above MA scans, custom breadth | https://chartink.com |
| **Trendlyne** | Market breadth dashboard (A/D, new highs/lows, % above MA) | https://trendlyne.com |
| **NSE India** | Advance/decline, new highs/lows, and bhavcopy for DIY breadth | https://www.nseindia.com |
| **Moneycontrol** | Market breadth and advance/decline data | https://www.moneycontrol.com |
| **Investing.com India** | Market breadth and % above moving averages | https://in.investing.com |
| **BSE India** | Advance/decline and breadth data (BSE universe) | https://www.bseindia.com |

**How to do it yourself:** NSE publishes the daily bhavcopy (OHLC and volume for every listed stock). From it you can compute every breadth indicator in this book in a spreadsheet — advancers/decliners, new highs/lows, and % above any moving average. It is the most reliable, and free, primary source.


# 10. The Top-Down Process: Breadth → Sector → Stock

*Part III — Putting It Together*

The power of RS and breadth is in combining them into one funnel. Each layer filters the one below.

## Step 1 — Read the market with breadth

Start with the broadest question: *is the market healthy?*

- Bullish breadth (A/D confirming, new highs expanding, % above 200-DMA > 60%) → a favourable environment for long-side selection.
- Bearish or divergent breadth → a cautious environment; favour defensives, raise the bar for every long, or stand aside.

**How to read:** this is a *regime* decision, not a stock decision. It sets the tilt (risk-on vs risk-off) for everything that follows.

## Step 2 — Pick the sector with sector RS

Within the market regime, rank sectors by RS.

- In a risk-on regime, overweight the **top 2–3 sectors** by RS — the leaders.
- In a risk-off regime, the top-ranked *defensive* sectors (FMCG, pharma, IT) are where relative safety is.

## Step 3 — Pick the stock with stock RS vs its sector

Within the leading sectors, rank stocks by RS **against their own sector** (not just the index). The genuine leaders are the stocks that are strong *within* strong sectors.

## The complete funnel, in one line

> **Breadth confirms the market → sector RS picks the group → stock-vs-sector RS picks the leader.**

## A worked example (illustrative)

1. **Breadth:** % of Nifty 500 stocks above the 200-DMA is 68% and rising; new highs expanding. → Risk-on.
2. **Sector RS:** over 6 months, the top-ranked sectoral indices are Auto and Capital Goods. → Overweight Auto, Capital Goods.
3. **Stock RS:** within Auto, rank by 6-month RS vs the Auto index; shortlist the top-decile names that are also strong vs Nifty. → The shortlist.

The same funnel, run in reverse, is the **avoid** list: a weak-market regime, a bottom-ranked sector, and a stock weak within that sector.


# 11. Combining RS, Breadth and Price

RS and breadth are not a standalone system; they are a **filter** and a **confirmation** layer on top of price action (Book 1). The best results come from using all three together.

## The rules of combination

1. **Breadth sets the regime; price sets the timing.** Breadth tells you *whether* to be aggressive; price levels and structure (Book 1) tell you *when*.
2. **RS picks the candidates; price confirms the entry.** High RS narrows the field to leaders; a price breakout or break-and-retest on a high-RS stock is the entry. High RS alone (without a price trigger) is a watchlist, not a trade.
3. **Divergences between breadth and price are the exits.** A topping breadth divergence is the reason to lighten exposure even when price looks fine; a bottoming divergence is the reason to stop being bearish.

## The warning that ties it all together

The classic late-stage market is one where **Nifty makes a new high, breadth diverges (narrowing), but a handful of high-RS leaders keep climbing.** Everything looks fine on the index, but under the surface the participation has thinned to a few names. That is precisely when the strength filter is most valuable — and when the breadth filter is screaming caution.


# 12. The One-Page Reference

**The funnel (run top-down, every week):**

1. **Breadth** — A/D line, new highs/lows, % above 200-DMA. Risk-on or risk-off?
2. **Sector RS** — rank sectoral indices by RS. Which 2–3 lead, which lag?
3. **Stock RS** — rank stocks within leading sectors by RS vs their sector. Shortlist the leaders.

**The signals:**

- **Leadership** = strong RS vs market *and* vs sector, confirmed by price.
- **Topping warning** = index new high + breadth divergence (narrowing).
- **Bottoming signal** = index new low + breadth higher low (broadening).

**The rules:**

- Rank on 6-month RS; confirm with 3-month and 12-month.
- Overweight leaders, underweight laggards.
- RS without a price trigger is a watchlist, not a trade.
- Breadth sets the regime; price sets the timing.
- Always re-check with current data — ranks and thresholds drift.


# Glossary

**A/D line** — the cumulative advance-decline line; a running total of advancing minus declining stocks.

**Advancer / Decliner** — a stock that closed up / down on the day.

**Breadth** — the participation (count) of stocks in a market move, as opposed to the index level.

**Breadth divergence** — index and breadth moving in opposite directions (a topping or bottoming warning).

**McClellan Oscillator** — the difference between the 19-day and 39-day EMAs of the daily advance-decline number.

**McClellan Summation Index** — the cumulative total of the McClellan Oscillator.

**New high / new low** — a stock making a 52-week high / low.

**Relative Strength (RS)** — one instrument's performance relative to another (a benchmark or a peer), expressed as a ratio or a percentile rank.

**RS ratio** — the normalised price of a stock divided by the normalised price of the benchmark.

**RS rank / percentile** — where a stock's return ranks among the universe (0–100).

**Sector RS** — the relative performance of a sectoral index versus the broad market.

**Sector rotation** — the migration of market leadership from one sector to another over the cycle.

**% above the 200-DMA** — the share of the universe trading above its 200-day moving average.
