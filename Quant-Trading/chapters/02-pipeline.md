# 2. The Quant Pipeline

## Idea to live, in six stages

Every quant strategy, whether it works or not, travels the same path. Knowing the stages — and *not skipping* them — is most of the discipline. This chapter walks the pipeline.

## Stage 1 — Idea

Everything starts with a *hypothesis about why* a pattern should exist. The best ideas are not "random backtest hits" but **economically motivated** claims:

- *"Investors under-react to news, so recent winners keep winning"* → a momentum idea.
- *"Short-term overshoots revert"* → a mean-reversion idea.
- *"Cheap, high-quality companies outperform over time"* → a factor idea.

The test of a good idea: **can you explain, in a sentence, *why* it should work** — not just *that* it worked in one backtest? An idea with a mechanism survives; an idea with only a backtest is a coin-flip.

## Stage 2 — Hypothesis → rules

Turn the idea into **unambiguous rules**. This is where vague becomes precise:

- *Universe:* which instruments, what liquidity filter.
- *Signal:* the exact condition (e.g., "12-month return, skip the last month, top decile").
- *Sizing:* equal-weight, or risk-based.
- *Rebalance/exit:* the schedule and the stop.

If two people could implement your idea *differently*, the rules are not precise enough.

## Stage 3 — Data

A strategy is only as good as its data. The requirements:

- **Clean** — no survivorship bias (use the *historical* universe, not today's survivors), no look-ahead (no using data not yet available at decision time), no survivorship in delisted names.
- **Aligned** — prices, corporate actions (splits, dividends, bonuses) adjusted correctly; in India, adjustment for splits/bonuses/rights matters enormously.
- **Complete** — enough history to span *different regimes* (a strategy tested only in a bull market has learned nothing about bear markets).

Data quality is where most retail quant efforts quietly fail.

## Stage 4 — Backtest

Run the rules over history and measure the result. But treat the backtest as an **experiment**, not an answer. The goal is to learn:

- *Is there an edge?* (positive expectancy after costs.)
- *How deep are the drawdowns?* (Can I survive them?)
- *Is the edge robust?* (Does it survive small changes to the parameters, or is it fragile?)

Chapter 9 covers the traps that make backtests lie; Chapter 3 covers the metrics that tell you what you are looking at.

## Stage 5 — Paper trading

Run the strategy **live, but without real money** (or with tiny size), for weeks to months. This stage tests the things a backtest cannot:

- *Does the execution match the assumption?* (Slippage, fills, latency.)
- *Do the costs match the estimate?* (Real brokerage, STT, impact.)
- *Does the *process* work?* (Can you run it every day, reliably, without mistakes?)

Paper trading is where the *engineering* gets tested — and it is the cheapest place to find bugs.

## Stage 6 — Live (small, then scale)

Go live **at small size first**, and only scale after the live results *track* the backtest and paper results within reason. Live is where the psychological reality (Chapter 10) and the tail events (Risk Management book) show up.

## The pipeline as discipline

The pipeline's most important property is that **each stage is a gate, not a formality.** A strategy that fails the backtest does not proceed; a strategy whose paper trading diverges from the backtest does not go live; a live strategy that stops tracking its backtest is retired. The stages exist to *kill bad ideas cheaply* — the earlier, the cheaper.

The single most common quant failure is **skipping a stage** — going from idea straight to real money, or trusting a backtest that was never stress-tested. The pipeline is the antidote.

## Summary

- The pipeline: idea → rules → data → backtest → paper → live.
- Ideas need a *mechanism*, not just a backtest.
- Rules must be unambiguous; data must be clean, aligned, and complete.
- Each stage is a gate: kill bad ideas cheaply, early.
- The biggest failure is skipping a stage.

Next: the metrics — how to tell whether a backtest is telling the truth.
