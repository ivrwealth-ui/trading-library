# 2. The Framework Lifecycle

## The machine, end to end

A systematic framework is best understood as a **cycle** — a loop that an idea travels, again and again. Understanding the loop is more important than any single component, because most failures are failures to *complete the loop* — to carry an idea all the way around, honestly, and then to feed what is learned back in.

## The eight-stage loop

```
1. Idea
2. Hypothesis (a testable claim)
3. Data
4. Signal
5. Backtest
6. Paper trade
7. Live (small → scaled)
8. Review & retire (→ back to 1)
```

### 1. Idea

A *why-based* claim about a pattern: "investors under-react, so winners keep winning." The idea is the raw material — necessary, but not yet testable.

### 2. Hypothesis

The idea, made **falsifiable**: "ranking stocks by 12-1 return and holding the top decile, rebalanced monthly, produces positive risk-adjusted returns after costs." A hypothesis is a claim that can be *shown wrong* — and a good framework *tries* to show it wrong.

### 3. Data

The clean, complete, **point-in-time** inputs (Chapter 4). This is where most retail systems quietly fail: survivorship bias, look-ahead, and corporate-action errors corrupt everything downstream.

### 4. Signal

The rule that turns data into a *decision*: what to hold, when to enter, when to exit (Chapter 5).

### 5. Backtest

Running the signal over history and *attacking the result* (Chapter 7). The backtest is an attempt to **disprove**, not prove.

### 6. Paper trade

Running the system live, in real time, with no (or tiny) money — to test the *engineering*: execution, fills, costs, and the daily operational discipline.

### 7. Live

Going live **small**, then scaling only after live results *track* the backtest and paper results. Live is where the tail events and the psychology (Risk Management book) show up.

### 8. Review & retire

Measuring live against expectation, watching for **edge decay**, and *retiring* the system when it stops behaving as it should — then feeding the lessons back into the next idea.

## The two properties that make it work

### Each stage is a gate

A stage is not a formality; it is a **kill-point**. An idea that fails the hypothesis does not proceed; a strategy whose paper trading diverges from its backtest does not go live; a live system that stops tracking is retired. The stages exist to **kill bad ideas cheaply** — the earlier, the cheaper. The single most common failure is *skipping a stage* — going from idea straight to money, or trusting an unattacked backtest.

### The loop closes

The final stage feeds back into the first. Every retired system teaches something — a regime where momentum fails, a cost you under-estimated, a data error — and that lesson becomes the seed of the *next* idea. A framework is not a pipeline that ends; it is a loop that *compounds* learning.

## A mental model to carry

Think of the framework as a **quality filter**: it takes in raw ideas and, at each stage, lets through only the fraction that survive honest scrutiny. The fraction that reaches live is small — and that is the point. The framework's value is not in *finding* ideas; it is in **not letting bad ideas through.**

## Summary

- The loop: idea → hypothesis → data → signal → backtest → paper → live → review/retire → back to idea.
- Each stage is a gate; the loop kills bad ideas cheaply, early.
- The loop closes: every retirement feeds the next idea.
- The framework is a quality filter, not an idea-generator.

Next: the first real stage — turning an idea into a testable hypothesis.
