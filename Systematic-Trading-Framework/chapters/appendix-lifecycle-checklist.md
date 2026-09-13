# Appendix — Lifecycle Checklist

## Run this against any system you build

This checklist is the framework's lifecycle, condensed to a series of yes/no gates. A system is ready to proceed to the next stage **only when every item in the current stage is honestly "yes".**

## Stage 1 — Hypothesis

- [ ] I can state the *mechanism* (why the edge exists) in one sentence.
- [ ] The universe is specified exactly, with a liquidity filter.
- [ ] The signal (entry **and** exit) is written unambiguously.
- [ ] The success/failure criteria (metric, benchmark, horizon) are committed *before* testing.

## Stage 2 — Data

- [ ] The data source is documented and auditable.
- [ ] Prices are adjusted for corporate actions (splits/bonuses/rights).
- [ ] The universe is point-in-time (includes delisted/failed names).
- [ ] Fundamentals (if used) are un-restated / point-in-time.
- [ ] A cleaning log records what was dropped and why.

## Stage 3 — Backtest

- [ ] Costs are included, pessimistically (brokerage, STT, spread, slippage).
- [ ] Survivorship bias is removed.
- [ ] Look-ahead bias has been hunted ("known on this date?").
- [ ] Parameters are stressed (edge shown across a range, flat-topped).
- [ ] The edge survives an out-of-sample test.
- [ ] The sample is large enough, and spans multiple regimes.

## Stage 4 — Paper trade

- [ ] The system runs live in real time with no (or tiny) money.
- [ ] Execution (fills, slippage) is reconciled against the model.
- [ ] Live costs match (or exceed) the backtest's estimate.
- [ ] The runbook and reconciliation process work without errors.

## Stage 5 — Live

- [ ] Going live at small size first.
- [ ] Live performance is tracked against the backtest's prediction.
- [ ] Edge decay is monitored against a threshold.
- [ ] The kill switch and drawdown policy are in place and pre-committed.

## Stage 6 — Review / retire

- [ ] The system is reviewed on the scheduled cadence (not reactively).
- [ ] Parameter/rule changes happen only through change control.
- [ ] The system is retired when it stops behaving as it should.
- [ ] The lessons are fed back into the next hypothesis.

## The one-line test

**Can someone else run the whole system — template, data, rules — and get the same decisions you would, without asking you a single question?**

If the answer is yes, you have a framework. If not, you have a discretionary trader with a spreadsheet.
