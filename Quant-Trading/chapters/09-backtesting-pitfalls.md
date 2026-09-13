# 9. Backtesting Pitfalls

## The ways a backtest lies

Every strategy in this book — indeed, every quant strategy ever written — will look better in a backtest than it performs live. The gap is not random; it is caused by a specific, well-understood set of **biases and errors**. This chapter names them, because the entire point of quant trading is to *test honestly* — and an honest test requires knowing how tests lie.

## The seven deadly pitfalls

### 1. Look-ahead bias

Using information that was **not available at decision time**. Example: ranking on a company's *today's* market capitalisation when backtesting *last year's* decision — but last year the market cap was different.

**The test:** for every data point, ask "did I *actually know* this on the day the trade was made?" If not, the backtest is fantasy. Look-ahead bias is the single most common source of inflated results.

### 2. Survivorship bias

Backtesting on the universe of companies that **exist today**, ignoring those that delisted, went bankrupt, or merged away. The survivors are, by definition, the ones that did well — so the backtest inherits an upward bias.

**The fix:** use a **point-in-time universe** — the actual list of tradeable names *on each historical date*, including the ones that later disappeared.

### 3. Overfitting (curve-fitting)

Tuning the strategy's parameters until it fits the *historical* data perfectly — and therefore fits the *future* not at all. An overfit backtest has a beautiful equity curve and no predictive power.

**The signs:** a Sharpe that is *too* good (a Sharpe of 3+ is suspicious), an edge that appears only for one specific parameter value, and a strategy with no economic rationale.

**The fix:** keep the strategy *simple* (few parameters), demand an economic mechanism (not just a fit), and test **robustness** — does the edge survive if you nudge every parameter? A robust edge is flat-topped; an overfit one is a single sharp spike.

### 4. Ignoring transaction costs

Backtesting on prices alone, forgetting that every trade costs brokerage, STT, stamp duty, and the **bid-ask spread** (which is often the largest cost of all, especially in illiquid names).

**The test:** re-run the backtest *with* realistic costs, including slippage. In India, STT and the spread on churning strategies are frequently enough to turn a "profitable" strategy negative — especially for high-turnover strategies like monthly momentum rotation.

### 5. Ignoring liquidity and capacity

Backtesting as if you could trade any size, in any name, at the last price. In reality, an illiquid small-cap cannot absorb your order without moving the price against you.

**The fix:** impose a **liquidity filter** (minimum average turnover) in the backtest, and estimate *impact* — the price you would actually get, not the printed price.

### 6. Small samples and regime luck

A backtest over a short period — or over a single market regime — proves almost nothing. A strategy tested only in a bull market has learned nothing about bear markets; a strategy with 20 trades is statistically indistinguishable from noise.

**The fix:** demand a **large trade count** and **multi-regime coverage** (bull, bear, and range), and prefer longer histories. If the history is short, treat the result as a hypothesis, not an answer.

### 7. Multiple-testing (data snooping)

Testing hundreds of strategies and reporting the one that happened to work. By pure chance, *some* of hundreds of random strategies will look good — and you have selected exactly those. This is the silent killer of quant credibility.

**The fix:** account for the number of tests. If you tried 100 strategies, expect ~5 to look good by luck alone. The honest question is: **does this one survive out-of-sample testing it was never fit on?**

## The one test that catches most of them: out-of-sample

The single most valuable defence is the **out-of-sample test**: develop the strategy on one period, and *then* — without further tweaking — test it on a later, unseen period. A strategy whose edge persists out-of-sample is worth something; one that collapses out-of-sample was overfit.

Closely related is **walk-forward testing**: repeatedly fit on a rolling window and test on the *next* window, mimicking how you would actually use the strategy.

## The honest mindset

The purpose of a backtest is not to *prove* a strategy works; it is to **try to prove it does not**. A backtest that you have attacked with every pitfall in this chapter — costs added, survivorship removed, look-ahead hunted down, parameters stressed, out-of-sample tested — and that *still* shows an edge, is the only backtest worth trusting.

The default assumption must be: **my backtest is lying.** The work is finding out how.

## Summary

- Seven pitfalls: look-ahead, survivorship, overfitting, ignored costs, ignored liquidity, small samples, multiple-testing.
- Look-ahead and survivorship are the most common and most damaging.
- Ignored costs (STT, spread, impact) frequently erase retail edges.
- Overfitting and data-snooping make backtests look better than reality.
- Out-of-sample / walk-forward testing is the single best defence.
- Treat the backtest as an attempt to *disprove* the strategy, not prove it.

Next: from backtest to live — the gap where even honest strategies go wrong.
