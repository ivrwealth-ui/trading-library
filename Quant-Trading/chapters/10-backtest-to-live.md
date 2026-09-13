# 10. From Backtest to Live

## The gap where honest strategies still fail

An honest, out-of-sample-tested backtest with a real edge can still lose money live — because the live world differs from the backtest in ways that are easy to forget. This chapter covers the gap, and how to cross it.

## The four gaps

### 1. The execution gap

The backtest assumes you trade at the signal price, instantly, with no slippage. Live, you trade at **the market's price**, which is different:

- **Slippage** — the difference between the price you expected and the price you got, especially in fast markets or illiquid names.
- **Latency** — the delay between the signal firing and the order reaching the market.
- **Partial fills** — not getting the full order filled at one price.

**The fix:** pad the backtest with realistic slippage, trade liquid instruments, and measure live execution against the backtest's assumption — if you consistently fill worse than modelled, the edge is smaller than you thought.

### 2. The cost gap

The backtest estimated costs; live, the real costs — brokerage, STT, stamp duty, the spread, and impact — are often larger, and they arrive in places the backtest ignored (a strategy that rebalances at the close, for example, pays the *close-auction* spread).

**The fix:** over-estimate costs in the backtest. If the edge survives *pessimistic* costs, it is robust; if it needs optimistic costs to survive, it is fragile.

### 3. The data gap

The backtest used clean, adjusted, complete data. Live data is **messy**: it arrives late, contains errors, misses corporate actions, and sometimes simply is not there. A strategy that depends on data that is only available *after* the fact is backtesting with look-ahead it does not even know about.

**The fix:** build the live data pipeline *separately* from the backtest data, and reconcile the two — if the live signals differ from the backtest signals on the same day, find out why before trusting either.

### 4. The psychological gap

The backtest is a line on a screen; live is real money, and it *feels* different. A 20% drawdown that was an abstract number in a backtest becomes a crisis live — and the trader responds by abandoning the strategy (usually at the drawdown's bottom).

**The fix:** the Risk Management book's framework — size small, know the drawdown in advance, and pre-commit to staying the course. The strategy's worst drawdown should be *known and accepted* before going live, not discovered at the bottom.

## The live protocol

A disciplined path from backtest to live:

1. **Paper trade first.** Run the strategy live, in real time, with no (or tiny) money, for weeks to months. This is where execution, cost, and data gaps surface — cheaply.
2. **Go live small.** Even after paper trading, start at a fraction of intended size. Live reveals what paper could not.
3. **Reconcile live vs. backtest.** Track the live performance against what the backtest *predicted* for the same period. A persistent gap means a modelling error, not bad luck.
4. **Monitor for decay.** Edges decay. Watch for the point where the strategy's live behaviour stops matching its historical behaviour — and be willing to retire it.
5. **Retire gracefully.** The hardest decision in quant is retiring a strategy that *used to* work. Pre-commit to the conditions (a drawdown threshold, a tracking-error threshold, a regime change) under which you stop.

## The honest bottom line

Quant trading is a *process*, not a product. The strategy is the least important part of it; the discipline — test honestly, paper trade, go live small, reconcile, monitor, retire — is what determines whether any strategy, from this book or anywhere, actually makes money. The trader who masters the process can turn a modest edge into years of compounding; the one who skips the process will lose money even with a good strategy.

## Summary

- Four gaps: execution, cost, data, and psychology.
- Paper trade before live; go live small; reconcile against the backtest.
- Costs are usually larger live than modelled — over-estimate them.
- Edges decay; pre-commit to retirement conditions.
- The process matters more than the strategy.

This completes the main text. The appendix collects the metrics and strategies into a reference table.
