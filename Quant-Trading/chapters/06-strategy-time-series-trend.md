# 6. Strategy 3 — Time-Series Trend Following

## An asset's own past, as the signal

Cross-sectional momentum ranks assets *against each other*. **Time-series momentum** (also called *trend following* or *absolute momentum*) asks a different question: **is this asset above its own past?** It holds an asset when it is trending up *relative to its own history*, and steps aside (or goes short) when it is not.

## The idea

The mechanism is the same under-reaction as cross-sectional momentum, applied to an asset's *own* history: an asset that has risen over the past 6–12 months has, historically, tended to keep rising — and an asset that has fallen has tended to keep falling. Time-series momentum formalises this with a single, robust rule: **be long when the asset is above its trend, out when below.**

Its greatest practical virtue is **drawdown avoidance**: it keeps you out of the market (or defensive) during sustained downtrends, which is where most long-term damage happens.

## The rules (the canonical form)

**Universe:** any asset you intend to hold — a broad index (NIFTY), a set of sector indices, or a basket of assets (Indian equities, global equities, gold, bonds).

**Signal:** the asset's price relative to its **200-day (or 10-month) simple moving average**:

- Price **above** the MA → **long**.
- Price **below** the MA → **cash** (or defensive asset).

**Rebalance:** check the signal **monthly** (at month-end). Checking daily adds whipsaw without much benefit.

**Position:** fully in, or fully out. (A multi-asset version applies the same rule to each asset, holding only those above their trend.)

## Pseudocode

```
for each asset in basket:
    state[asset] = "long" if close > sma(close, 200) else "cash"

every month_end:
    for each asset:
        if state[asset] == "long" and not invested(asset):
            buy(asset)
        if state[asset] == "cash" and invested(asset):
            sell(asset)
```

## Historical context

Time-series momentum is among the most documented effects in finance. The "above the 200-day MA = in, below = out" rule — and its equivalents — has been shown, across many markets and long periods, to deliver much of the market's return while materially reducing maximum drawdown. The mechanism is *avoidance* rather than prediction: the rule misses the worst stretches of bear markets, and because losses are asymmetric (a 50% loss needs a 100% gain to recover), avoiding them is worth more than catching every up-move.

Framed honestly: *historically, a simple trend filter has tended to produce equity-comparable long-run returns with smaller drawdowns, at the cost of whipsaw in range-bound markets and late entries/exits at turning points.*

## Risks and limitations

- **Whipsaw in ranges.** In a choppy, sideways market, price crosses the 200-day MA repeatedly, generating a string of small losing round-trips. This is the strategy's known cost, and it is why the monthly (not daily) check matters.
- **Late entries and exits.** The rule acts only *after* the trend has visibly broken, so it always gives up the first leg of recoveries and the last leg of bull markets. The investor must accept being "late."
- **Lag in one-way markets.** In a long, steady bull run, a trend filter occasionally steps out on a dip and misses a leg, underperforming buy-and-hold during that stretch.
- **Single-asset concentration.** Applied to one index, the strategy is fully in or fully out — no diversification of the timing decision. A multi-asset version smooths this.

## Summary

- Long above the 200-day MA, cash below; check monthly.
- Time-series momentum: an asset's own past predicts its own future.
- The value is drawdown avoidance, not prediction.
- Costs: whipsaw in ranges, lateness at turns, lag in one-way markets.
- A multi-asset version diversifies the timing decision.

Next: Strategy 4 — factor tilts.
