# 3. The Toolkit and Evaluation Metrics

## The vocabulary for judging a strategy

A backtest produces a wall of numbers. This chapter explains the metrics that actually matter — and, crucially, *what they can and cannot tell you*.

## Returns and risk

### CAGR (Compound Annual Growth Rate)

The annualised return, smoothing out the compounding. It answers "how fast did the equity grow?" — but it is a *single number* that hides the path.

### Volatility (standard deviation of returns)

How much the returns swing. High volatility means a bumpy ride for the same CAGR. Volatility is *risk* in the quantitative sense.

### Maximum drawdown (Max DD)

The worst peak-to-trough fall. This is the number that matters most emotionally — and practically, because of the recovery asymmetry (a 50% drawdown needs a 100% gain to recover). A strategy is only as good as its worst drawdown, because that is what decides whether you survive to collect the returns.

## Risk-adjusted return

### Sharpe ratio

Sharpe = (Return − risk-free) ÷ volatility.

It measures return *per unit of risk*. A high Sharpe means the return was earned *efficiently* — without excessive volatility. A Sharpe above ~1 is good; above ~2 is excellent (and often too good — a red flag for overfitting, Chapter 9).

### Sortino ratio

Like Sharpe, but only penalises *downside* volatility (the part you actually dislike). It is a fairer measure for strategies with asymmetric returns.

## The trade-level metrics

### Win rate

The fraction of trades that won. **Important:** win rate alone is meaningless — it must be read with the payoff ratio. A 30% win rate with 4:1 winners is excellent; an 80% win rate with 1:4 losers is ruinous.

### Profit factor

Gross profit ÷ gross loss. A profit factor above 1 means the strategy made more than it lost; above ~1.5 is usually considered solid. It is a quick, robust summary of edge.

### Payoff ratio (avg win ÷ avg loss)

How big winners are relative to losers. Combined with win rate, it determines expectancy:

Expectancy = (Win rate × Avg win) − (Loss rate × Avg loss)

A positive expectancy is the *minimum* bar for a strategy — and you should be able to compute it from these two numbers.

## Robustness metrics (the ones that catch lies)

### Number of trades

A backtest with 20 trades proves almost nothing; one with 2,000 is far more credible. **Small samples lie.** Look at the trade count before believing any other metric.

### Parameter sensitivity

Does the edge survive if you change the lookback from 12 months to 10, or 14? A robust edge is *insensitive* to small parameter changes; a fragile one (the signature of overfitting) collapses the moment you nudge anything. Plot performance against parameter — a smooth, flat-topped surface is good; a single sharp spike is a warning.

### Out-of-sample / walk-forward performance

The gold-standard test: fit nothing, or fit on one period and *test on a later, unseen period*. A strategy that only works in-sample is overfit. Real edges persist out-of-sample.

### Regime coverage

Did the strategy make money across *different* market conditions (bull, bear, range) — or only in one? A strategy that only works in a bull market is a bet on the bull market, not a strategy.

## The honest reading order

When you see a backtest, read the numbers in this order:

1. **Trade count** — is the sample big enough to mean anything?
2. **Max drawdown** — could I survive it?
3. **Profit factor / expectancy** — is there actually an edge?
4. **Sharpe/Sortino** — is the edge worth the risk?
5. **Robustness** — does it survive parameter changes and out-of-sample?

Most people read the CAGR first — which is exactly backwards, because CAGR is the number most easily inflated by a lucky, overfit, or costless backtest.

## Summary

- Return metrics (CAGR, vol, max DD) describe the path; max DD is what decides survival.
- Risk-adjusted metrics (Sharpe, Sortino) measure return per unit of risk.
- Trade-level metrics (win rate, payoff, profit factor, expectancy) describe the edge.
- Robustness metrics (trade count, parameter sensitivity, out-of-sample, regime coverage) catch lies.
- Read trade count and drawdown before you read CAGR.

Next: Strategy 1 — cross-sectional momentum.
