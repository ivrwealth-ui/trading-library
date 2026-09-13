# 10. A Working Framework Template

## Everything, on one page

The previous nine chapters built the framework piece by piece. This chapter assembles it into a **single working template** — the one-page document that turns the framework from an idea into a tool you can actually run.

## The framework template

```
============================================================
SYSTEMATIC TRADING FRAMEWORK
============================================================

1. HYPOTHESIS
   Mechanism:  [why the edge exists — behaviour/structure, in a sentence]
   Universe:   [exactly what is traded + liquidity filter]
   Signal:     [entry rule, in precise words]
   Exit:       [stop / target / trail / time rule]
   Claim:      [metric + benchmark + horizon]
   Falsify:    [result that would prove it wrong]

2. DATA
   Source:        [vendor / API, documented]
   Adjustment:    [splits/bonuses/rights — how adjusted]
   Point-in-time: [yes — historical universe, un-restated fundamentals]
   Cleaning log:  [what was dropped and why]

3. SIZING & PORTFOLIO
   Risk per trade:    [1-2%]
   Size rule:         [(Equity × Risk%) ÷ (Entry − Stop)]
   Weighting:         [equal-weight / signal-weight]
   Max per position:  [%]
   Max total at-risk: [%]
   Max exposure:      [%]
   Diversification:   [across what drivers]

4. BACKTEST DISCIPLINE
   Costs included:    [brokerage, STT, spread, slippage — pessimistic]
   Survivorship:      [removed — point-in-time universe]
   Look-ahead:        [hunted — "known on this date?" test]
   Parameter stress:  [edge shown across a range, flat-topped]
   Out-of-sample:     [tested on unseen period]
   Sample:            [trade count, regime coverage]

5. EXECUTION & MONITORING
   Runbook:         [daily/weekly procedure]
   Reconciliation:  [daily, planned vs. actual]
   Slippage pad:    [%]
   Live-vs-backtest: [tracked, deviation threshold]

6. GOVERNANCE
   Change control:     [how/when rules change — scheduled review only]
   Drawdown policy:    [action at each drawdown level]
   Kill switch:        [conditions that stop the system]
   Review cadence:     [how often, against what]
============================================================
```

## How to use the template

1. **Fill it in before you build.** The template *forces* the thinking (mechanism, falsification, exit) that most people skip.
2. **Fill it in before you backtest.** Pre-registration — the hypothesis and the success/failure criteria are committed *before* the numbers arrive.
3. **Use it as the live runbook.** The execution, monitoring, and governance sections are your operating manual, not a formality.
4. **Review it on schedule.** The governance section defines *when* — and the discipline is to review then, and only then, not reactively.

## The test of a working framework

A framework is "working" when it passes a single test: **you can hand the whole thing — the template, the data, the rules — to someone else, and they can run it and get the same decisions you would, without asking you a single question.**

If you have to explain, override, or interpret, the framework is not finished — it is discretionary trading wearing a spreadsheet. The entire discipline of this book reduces to that one test.

## The honest closing

A framework does not guarantee profit. What it guarantees is something more valuable: **that your decisions are explicit, your testing is honest, and your failures are small enough to learn from.** That is the entire game — survive long enough, with a process clean enough, that a real edge (if you find one) can actually compound. Everything in this book, and in the whole series, serves that single goal.

## Summary

- The template assembles hypothesis, data, sizing, backtest, execution, and governance on one page.
- Fill it in before building and before backtesting (pre-registration).
- It doubles as the live runbook and the governance document.
- The test: someone else can run it and get the same decisions, with no questions.
- The framework guarantees honesty and survival, not profit.

This completes the main text. The appendix is the lifecycle checklist.
