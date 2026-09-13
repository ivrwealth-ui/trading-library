# 3. From Idea to Testable Hypothesis

## The difference between a hunch and a claim

Most "trading ideas" are actually **hunches** — vague, untestable, and unfalsifiable. The first job of a framework is to convert a hunch into a **hypothesis**: a specific, falsifiable claim that can be tested and, crucially, *shown to be wrong.*

This chapter covers that conversion.

## What makes a claim testable

A testable hypothesis has four properties. It states:

1. **The mechanism** — *why* the pattern should exist (not just *that* it appeared in a backtest).
2. **The exact rule** — the precise, unambiguous signal.
3. **The measurable claim** — what "working" would look like (a metric, a threshold, a benchmark).
4. **The falsification** — what would prove it *wrong*.

### A weak idea (a hunch)

*"Momentum seems to work."*

Untestable: no mechanism, no rule, no measure, no falsification. A framework cannot do anything with this.

### A strong idea (a hypothesis)

*"Because investors under-react to information (mechanism), ranking NIFTY 500 stocks by their 12-month return skipping the last month and holding the top decile, rebalanced monthly (rule), produces a positive annualised return after costs (measure) that is higher than the NIFTY 50 benchmark over the same period (falsification target)."*

Every word can be checked. This is what a framework consumes.

## The mechanism test

The single most important part is the **mechanism** — the "why". A hypothesis with a mechanism is *robust*: if the mechanism is a real, persistent feature of markets, the edge is likely to persist. A hypothesis without a mechanism is just a pattern — and a pattern with no explanation is the classic signature of overfitting.

The test is simple: **can you explain the edge in a sentence, in terms of human behaviour or market structure?**

- *"Investors under-react to news"* → a mechanism (behavioural).
- *"Funds rebalance at month-end"* → a mechanism (structural).
- *"It worked in my backtest"* → **not** a mechanism.

If you cannot articulate the mechanism, the idea is not ready.

## Stating the rule precisely

The rule must be **unambiguous** — so precise that two different people would implement it identically:

- *Universe:* exactly which instruments, with what liquidity filter.
- *Signal:* the exact condition, in the exact words.
- *Sizing:* how much, and by what rule.
- *Exit/rebalance:* when, and on what trigger.

Ambiguity is where look-ahead bias and hindsight creep in. Every vague phrase ("strong momentum", "cheap", "recently") must be replaced with a number and a window.

## Pre-registering the test

The most powerful discipline in systematic trading is **pre-registration**: write down the hypothesis, the rule, and the success/failure criteria *before* you run the backtest. This matters because after you see the backtest, you will be tempted to tweak — and every post-hoc tweak is a step toward overfitting.

Pre-registration forces the clean sequence: **claim → test → verdict.** Not: test → claim → tweak → test → claim.

## A hypothesis template

```
Mechanism: [why the edge should exist]
Universe:   [exactly what is traded, and the liquidity filter]
Signal:     [the exact entry/exit rule]
Sizing:     [how much, by what rule]
Claim:      [the measurable outcome: metric + benchmark + horizon]
Falsify:    [what result would prove it wrong]
```

Fill this in — honestly, before testing — and you have converted a hunch into something a framework can actually work with.

## Summary

- A testable hypothesis has a mechanism, an exact rule, a measurable claim, and a falsification condition.
- The mechanism ("why") is the most important part; no mechanism → likely overfit.
- State the rule unambiguously; vagueness invites hindsight bias.
- Pre-register the test before running it, to avoid post-hoc tweaking.
- Use the template: mechanism, universe, signal, sizing, claim, falsify.

Next: data — where most systems silently fail.
