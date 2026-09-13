# 1. What Is Quant Trading?

## Rules over judgement

**Quant trading** is the practice of turning a trading idea into a *precise, testable set of rules*, and executing those rules *systematically* — by hand against a checklist, or by computer. The defining feature is not the use of computers; it is the **explicitness**: a quant strategy can be written down unambiguously, and therefore *tested* against history before a single rupee is risked.

Where a discretionary trader might say "I like this stock because the story is improving," the quant trader says: "rank the universe by trailing 12-month return, hold the top 10%, rebalance monthly." The difference is not sophistication — it is **falsifiability.** A rule can be backtested; a feeling cannot.

## The spectrum, not a binary

"Quant" and "discretionary" are ends of a spectrum, not two camps:

- **Fully systematic** — every decision (what, when, how much, when to exit) is a rule.
- **Quant-assisted** — a human makes the final call, but with systematic inputs (a screener, a risk model, a backtest).
- **Discretionary** — judgement drives everything.

Most of this book's ideas sit at the systematic end, because that is where the *testability* — the whole point of quant — lives.

## The three promises of quant

Quant trading exists for three reasons, and each is a real advantage:

1. **Testability.** An explicit rule can be backtested. You can learn — *before* risking money — how it would have behaved, how deep its drawdowns were, and whether the edge survives costs. Discretionary judgement cannot be tested this way.
2. **Emotion removal.** A systematic rule is executed the same way whether you are euphoric or terrified. The rule, not the mood, makes the decision (the psychology chapters of this series explain why that matters).
3. **Scale and repeatability.** A systematic process can be run across hundreds of instruments, consistently, day after day — something no human judgement can do.

## The honest caveats

Quant trading is not a shortcut to certainty, for three reasons the book returns to:

1. **Backtests overstate.** A backtest is an *upper bound* on reality, not a forecast. Overfitting, look-ahead bias, survivorship bias, and ignored costs can make a worthless strategy look wonderful (Chapter 9).
2. **The past is not the future.** A rule that worked historically can stop working — markets adapt, and edges decay. This is why quant is a *process* (build, test, monitor, retire), not a one-time discovery.
3. **Quant is not "code magic."** The hardest part is not the programming; it is the *idea* and the *discipline* to test it honestly. The code is just the unambiguous expression of the idea.

## What a quant strategy actually is

Strip away the jargon and every quant strategy is four things:

1. **A universe** — what you trade (NIFTY 500, a basket of ETFs, a list of futures).
2. **A signal** — a rule that says *when and what* to act on (momentum rank, mean-reversion extreme, trend state).
3. **A sizing rule** — *how much* (fixed fraction, volatility targeting — the Risk Management book covers this).
4. **An exit** — *when to leave* (a stop, a rebalance, a time rule).

Everything in this book is a variation on those four knobs. Master the structure, and each strategy is a matter of "which settings."

## Summary

- Quant trading is explicit, testable rules — not necessarily computers.
- It promises testability, emotion removal, and scale.
- It is not a shortcut: backtests overstate, edges decay, and the idea matters more than the code.
- Every strategy = universe + signal + sizing + exit.

Next: the pipeline — the process that turns an idea into a live strategy.
