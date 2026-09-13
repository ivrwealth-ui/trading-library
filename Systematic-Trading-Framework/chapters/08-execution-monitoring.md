# 8. Execution, Costs, and Monitoring

## The gap between backtest and live

A strategy that survives an honest backtest can still lose money live — because live differs from the backtest in ways that are easy to forget. This chapter covers the three differences: **execution**, **costs**, and **monitoring**.

## Execution: the price you actually get

The backtest assumed you traded at the signal price, instantly. Live, you trade at **the market's price**:

- **Slippage** — the gap between expected and actual fill, especially in fast markets or illiquid names.
- **Latency** — the delay between the signal firing and the order reaching the market.
- **Partial fills** — not getting the whole order at one price.

The discipline: **pad the backtest with realistic slippage**, trade liquid instruments, and — critically — **measure live fills against the backtest's assumption**. If you consistently fill worse than modelled, the edge is smaller than you thought, and the model must be updated to reflect reality.

## Costs: larger than you estimated

The backtest estimated costs; live costs are usually **larger**, and they appear in places the backtest ignored:

- A strategy that rebalances at the close pays the **close-auction spread**.
- A strategy that trades illiquid small-caps pays **market impact** — your own order moves the price.
- **Taxes** (STT, capital gains) on realised turnover reduce the net return in ways a costless backtest cannot show.

The discipline: **over-estimate costs in the backtest** (Chapter 7), and reconcile live costs against the estimate. A strategy whose live costs are persistently above the estimate is a strategy with a smaller (or no) edge.

## Monitoring: is the system still itself?

A live system must be **monitored**, not just run. The monitoring has three jobs:

### 1. Track live against backtest

Compare live performance to what the backtest *predicted* for the same period. A persistent gap is a **modelling error** (a cost, a data difference, a look-ahead you missed), not bad luck. Find it.

### 2. Watch for edge decay

Edges decay — markets adapt, competitors arrive, the anomaly gets arbitraged. The signature is live performance *drifting away* from the backtest's behaviour over time. Monitoring's job is to notice the drift **early**, before it costs real money.

### 3. Watch for operational failures

The unglamorous but critical work: did the data arrive on time? Did the orders fill? Did the position sizes match the rules? An operational error — a missed rebalance, a duplicated order, a stale price — can cost more than a bad signal. Monitoring is the safety net.

## The operational discipline

Running a system is an *operating* job, and it deserves operating discipline:

- **A runbook** — a written procedure for each daily/weekly task (pull data, generate signals, place orders, reconcile).
- **Reconciliation** — every day, compare what *should* have happened (per the rules) against what *did* happen (per the fills and positions). Any difference is investigated, not ignored.
- **A kill switch** — pre-defined conditions under which you stop the system (a drawdown threshold, a tracking-error threshold, a data failure). Decided in advance, not in the panic of the moment.

## Summary

- Execution: pad for slippage, trade liquid, and reconcile live fills against the model.
- Costs: over-estimate in the backtest; reconcile live costs against the estimate.
- Monitoring: track live vs. backtest, watch for edge decay, catch operational failures.
- Run with operating discipline: a runbook, daily reconciliation, and a pre-defined kill switch.

Next: risk management and governance — the layer that keeps the system alive.
