# 12. Code Best Practices and Disclaimers

## Writing screeners that behave

This closing chapter covers the practices that keep a screener script *correct* and *honest* — and the disclaimers that must accompany any code that touches trading decisions.

## Best practices

### 1. Guard every `na`

Fundamental data is often missing; benchmarks may not exist for every symbol; a fresh listing may not have 252 bars of history. Every script in this book therefore guards against `na`:

- `ignore_invalid_symbol = true` on every `request.financial()` / `request.security()` call.
- Explicit `not na(x)` checks in conditions.
- Ternary expressions that default to `na` rather than dividing by zero (e.g., `epsTtm > 0 ? close / epsTtm : na`).

The result: a symbol without data simply produces **no signal** — it never crashes the script, and never produces a false positive from garbage input.

### 2. Respect the screener limits

Keep every script within the Pine Screener's constraints: **≤40 `request.*` calls**, **≤500-bar lookback**, **standard timeframes only**. If you extend a script, count the calls and check the lookback — a 750-bar momentum window will silently misbehave in the screener.

### 3. Keep the signal binary and named

A screener is easiest to use when the pass/fail output is a single, clearly named plot:

```pine
plot(cond ? 1 : 0, "Signal", color = cond ? color.green : color.red, style = plot.style_columns)
```

Name the plot what it *is* ("Stage 2 Signal", "Value Signal"), because the plot title becomes the column name.

### 4. Plot the metrics, not just the verdict

The most useful screeners report *why* a stock passes, not just *that* it passes. Plotting the P/E, the momentum %, and the relative strength — alongside the signal — lets you **sort** the shortlist and spot *degree*, not just direction.

### 5. Prefer simple, explainable logic

Every strategy here can be explained in a sentence. If a screener needs fifty inputs and a dozen conditions to "work", it is almost certainly overfit to past data and will fail live. Keep it simple enough to explain.

## The disclaimers (why they matter)

These scripts sit at the boundary between code and trading decisions, so they carry three specific warnings — restated from the front of the book, because they are the part that protects you:

1. **A screener is a filter, not a signal.** It shortlists; it does not recommend. Every result is a *candidate for your own review*, never an instruction.
2. **The code is illustrative and comes without warranty.** It has not been certified against every plan, version, or market; it may need adjustment for your data subscription; and it may produce no results (rather than wrong results) when data is missing. Test in the Pine Editor, and on paper, before any reliance.
3. **Historical patterns are not promises.** Valuation, momentum, stage analysis, VCP, Dow Theory — all describe *tendencies*, and all fail at times. A screener operationalises a tendency; it does not guarantee the tendency will hold tomorrow.

Framed as this book always frames such things: *these are recognised, widely discussed strategies, encoded for education. Historically, such conditions have tended to precede continued moves — but the tendency is probabilistic, not certain, and you are responsible for every decision you make from a screen's output.*

## Summary

- Guard every `na`; respect the 40-call/500-bar/standard-timeframe limits.
- Keep the signal binary and clearly named; plot the metrics too.
- Prefer simple, explainable logic — complexity is a symptom of overfitting.
- A screener is a filter, not a signal; the code is illustrative and comes without warranty; historical patterns are tendencies, not promises.

This completes the main text. The appendix indexes all eight scripts.
