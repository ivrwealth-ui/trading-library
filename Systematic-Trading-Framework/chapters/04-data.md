# 4. Data: Sourcing, Cleaning, and Integrity

## Where most systems silently fail

A systematic framework is only as honest as its data. Every stage downstream — signal, backtest, live — inherits whatever is wrong upstream. This chapter covers the three data disciplines: **sourcing**, **cleaning**, and **integrity**.

## The three data requirements

Before any analysis, your data must be:

1. **Clean** — free of errors, gaps, and bad ticks.
2. **Aligned** — prices adjusted correctly for corporate actions (splits, bonuses, rights, dividends).
3. **Point-in-time** — containing only the information that was *actually available* on each historical date.

The first two are about correctness; the third is about **not cheating** (look-ahead bias).

## Sourcing

For Indian equities, the data landscape is roughly:

- **Price/volume data** — daily OHLCV for NSE/BSE equities and indices, from your broker's API, a commercial data vendor, or exchange-derived sources.
- **Fundamental data** — financial statements and ratios; *point-in-time* fundamentals are much harder to obtain than current snapshots, and this gap matters.
- **Corporate actions** — splits, bonuses, rights issues, dividends; essential for correct adjustment.

The sourcing rule: **prefer data that is documented, auditable, and point-in-time** over data that is convenient but opaque. A beautiful backtest on bad data is worthless.

## Cleaning

Cleaning catches the errors that corrupt results:

- **Duplicate or missing bars** — a stock with a 10-day gap in its history will produce garbage momentum signals there.
- **Bad ticks** — a spurious price of ₹0.01 or ₹99,999 that is a data error, not a trade.
- **Zero or negative prices** — nonsense values that must be removed (and their cause understood).

The rule: **never silently drop data.** When you clean, record *what* you dropped and *why* — a data-removal log is an audit trail, and it is the only defence against the accusation (including your own) that you deleted data to make the backtest look better.

## Alignment (corporate actions)

This is the subtle one. A stock that did a 1:1 bonus (a 2-for-1 split) shows a price that *halved overnight* — but nothing about the company changed. If your data is not adjusted:

- A momentum signal will see a phantom −50% move and mis-rank the stock.
- A backtest will record a phantom −50% loss (or gain) that never happened to the holder.

The rule: **use adjusted prices** (adjusted for splits, bonuses, and rights) for *all* return calculations — and understand exactly what your vendor's "adjusted" means (some adjust for dividends too, which changes total return).

## Point-in-time integrity

This is where look-ahead bias lives. Three classic violations:

1. **Survivorship bias** — using today's universe (the companies that *survived*) to backtest the past. The delisted, merged, and bankrupt names are missing — and their absence flatters every result. Use a **point-in-time universe**: the actual tradeable list on each date.
2. **Restated fundamentals** — using today's *restated* earnings to rank stocks *last year*. Last year, the market only knew last year's (pre-restatement) numbers. Using restated data is look-ahead.
3. **Future corporate actions** — using a split-adjusted price on a date *before* the split happened.

The universal test: **for every data point, ask "did the market actually know this on this date?"** If not, it must not enter the signal.

## The discipline

Data integrity is a *process*, not a one-time task:

- **Document the source** and its known biases (every vendor has some).
- **Log every cleaning step** — what was dropped and why.
- **Use point-in-time universes and un-restated fundamentals** for anything historical.
- **Reconcile live vs. historical data** (Chapter 8) — if they disagree on the same day, find out why before trusting either.

## Summary

- Data must be clean, aligned, and point-in-time.
- Prefer documented, auditable, point-in-time sources.
- Clean with a log — never silently drop data.
- Use corporate-action-adjusted prices for all returns.
- The universal test: "did the market know this on this date?"

Next: signal generation — turning data into decisions.
