# 7. Backtesting Done Right

## The discipline of trying to disprove

A backtest is the moment of truth — but only if it is run *honestly*. The default posture of a systematic framework must be: **my backtest is lying; my job is to find out how.** This chapter covers the discipline that turns a backtest from a sales pitch into an experiment.

## The mindset: test to disprove, not prove

Most people backtest to *confirm* their idea — they want the backtest to say "yes." The result is that they unconsciously tune, filter, and cherry-pick until it does. A framework inverts this: it backtests to **try to kill the idea**, and only ideas that survive honest attack are worth proceeding with.

The practical form of this inversion:

- **Add the costs you wish you could ignore** (they are real live).
- **Remove the survivorship bias** you would rather not see.
- **Stress the parameters** rather than showing only the best one.
- **Test out-of-sample** rather than reporting in-sample.

## The attacks, in order

### 1. Add realistic costs

Brokerage, STT, stamp duty, and — above all — the **bid-ask spread and slippage**. In India, the spread and STT on churning strategies are frequently enough to turn a "profitable" backtest negative. Rule: **run the backtest with pessimistic costs.** If the edge needs optimistic costs to survive, it is fragile.

### 2. Remove survivorship bias

Backtest on the **point-in-time universe** — the names that actually existed on each date, including those that later delisted or failed (Chapter 4). Today's survivor list flatters every result.

### 3. Hunt look-ahead bias

For every input, verify it was *known at decision time* (Chapter 4's universal test). Restated fundamentals, adjusted prices used pre-action, and any use of the future are all look-ahead.

### 4. Stress the parameters

Show performance *across a range* of each parameter, not just the best value. A robust edge has a flat-topped surface; a single sharp spike is the fingerprint of overfitting.

### 5. Test out-of-sample

The gold standard: fit nothing, or fit on one period and test on a *later, unseen* period. A strategy whose edge persists out-of-sample — without further tweaking — is worth something. One that collapses out-of-sample was overfit.

### 6. Demand a large sample and regime coverage

A backtest with 20 trades proves little; one with 2,000 is far more credible. And a strategy tested only in a bull market has learned nothing about bear markets. Prefer long histories spanning **multiple regimes**.

## Reading the output honestly

When the backtest prints its numbers, read them in the order that matters (from the Quant Trading book's metrics chapter):

1. **Trade count** — is the sample big enough?
2. **Max drawdown** — could I survive it?
3. **Profit factor / expectancy** — is there actually an edge?
4. **Sharpe / Sortino** — is the edge worth the risk?
5. **Robustness** — does it survive the attacks above?

CAGR — the number everyone reads first — is the one most easily inflated by a lucky, overfit, costless backtest. Read it last.

## The pre-registration discipline

The single strongest defence against self-deception is **pre-registration** (Chapter 3): commit to the hypothesis, the rule, and the success/failure criteria *before* running the backtest. After you have seen the result, every change you make is a step toward overfitting — and pre-registration is the record that keeps you honest about that.

## The honest bottom line

A backtest is not a *prediction* of future returns; it is a **stress test of an idea's robustness**. Its value is negative: it cannot tell you the strategy *will* work, but it can tell you — if you let it — that the strategy *probably won't*. The framework's entire backtesting discipline is built to extract that negative value honestly.

## Summary

- Test to disprove, not prove; default to "my backtest is lying."
- Attacks: add costs, remove survivorship, hunt look-ahead, stress parameters, test out-of-sample, demand sample size and regime coverage.
- Read trade count and drawdown before CAGR.
- Pre-register before testing to resist post-hoc tweaking.
- A backtest is a stress test, not a prediction.

Next: execution, costs, and monitoring — the gap between backtest and live.
