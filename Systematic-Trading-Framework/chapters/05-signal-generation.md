# 5. Signal Generation

## Turning data into decisions

The **signal** is the heart of the system: the rule that turns clean data into a *decision* — what to hold, when to enter, when to exit. This chapter covers how to design a signal that is precise, robust, and honest.

## The anatomy of a signal

Every signal, however complex, answers three questions in a specific order:

1. **What** — which instruments are eligible? (a *filter*, not a timing decision.)
2. **When** — under what condition do we act? (the *entry* trigger.)
3. **When to leave** — under what condition do we exit? (the *exit* rule.)

A complete signal specifies all three. A signal that only says *what* to buy, with no exit, is half a system.

## The three families of signals

Signals fall into a small number of families, and knowing the family tells you how it will behave:

- **Momentum / trend** — buy strength, ride the trend, exit on weakness. Low win rate, large winners, suffers in ranges.
- **Mean reversion** — fade extremes, buy dips, exit on the snap-back. High win rate, occasional large loss, suffers in trends.
- **Cross-sectional / relative** — rank a universe and hold the best *relative* to the others. Always invested in something.

Most systems are one of these, or a combination (e.g., a trend filter gating a mean-reversion entry). The companion books in this series explore the specific strategies in each family.

## Designing for robustness

A good signal is **robust** — its edge survives small changes to its parameters. The design principles:

### 1. Few parameters

Every parameter is an opportunity to overfit. A signal with three parameters is testable; one with thirty is curve-fit. The discipline: **explain, in words, why each parameter is there** — and if you cannot, cut it.

### 2. Economically sensible values

Parameters should be *sensible*, not *optimised*. A 200-day trend filter has a reason (it approximates the long-term trend); a 137-day filter was almost certainly mined from the data. Prefer round, meaningful values (12 months, 200 days) over odd ones that only exist because they backtested well.

### 3. Insensitivity to small changes

The test of robustness: **does the edge survive if you change each parameter slightly** (10 vs. 12 months, 200 vs. 190 days)? A robust edge has a *flat-topped* performance surface — performance is similar across a neighbourhood of parameter values. A fragile edge is a single sharp spike at one lucky value.

### 4. A stated mechanism

The signal must have a *why* (Chapter 3's mechanism test). A signal with no economic rationale, however good its backtest, is a coin-flip wearing a spreadsheet.

## The exit deserves equal design effort

Most people over-design the entry and under-design the exit. That is backwards, because **the exit is where most of the risk lives.** A complete exit specifies:

- **The stop** — the level at which the thesis is wrong (structural) or the risk is exceeded (volatility-based).
- **The take-profit / target** — where the swing is exhausted (for bounded strategies).
- **The trail** — how open profit is protected (for trend strategies).
- **The time stop** — exiting dead-money trades after a fixed holding period.

An entry without a defined exit is not a strategy; it is a hope.

## Pseudocode for a complete signal

```
for each instrument in universe:                    # WHAT (filter)
    eligible = liquidity_filter(instrument)         #    tradable?

    if eligible:
        state = signal_state(instrument)            # momentum / reversion / relative

        if state == "enter" and no position:        # WHEN (entry)
            open_position(instrument)
            set_stop(instrument)                    #   exit rule defined AT entry
            set_target_or_trail(instrument)

        if position and exit_condition(instrument): # WHEN TO LEAVE
            close_position(instrument)
```

Note what the pseudocode makes explicit: **the exit is set at the moment of entry**, and the signal is *complete* — every decision point is covered.

## The honest test

A signal is finished when you can hand it to someone else — someone who has never seen the backtest — and they can run it and get the *same* decisions. If you have to explain "well, here I'd override it because…", the signal is not finished; it is discretionary trading wearing a rules costume.

## Summary

- A signal answers what, when, and when-to-leave — all three.
- Three families: momentum/trend, mean reversion, cross-sectional/relative.
- Design for robustness: few parameters, sensible values, insensitivity, a mechanism.
- The exit deserves equal design effort — and is set at entry.
- A finished signal is one someone else can run identically, with no overrides.

Next: portfolio construction and position sizing — the "how much" layer.
