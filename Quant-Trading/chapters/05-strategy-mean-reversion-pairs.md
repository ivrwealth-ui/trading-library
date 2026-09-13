# 5. Strategy 2 — Mean Reversion and Pairs

## Betting that extremes snap back

Mean reversion is the *opposite* of momentum: it bets that **prices that have moved too far, too fast will snap back toward their average.** Where momentum buys strength, mean reversion fades it. This chapter covers the two canonical forms: single-asset mean reversion and **pairs trading**.

## The idea

The mechanism: markets *overshoot*. In the short term, a sharp move is often driven by temporary flows — panic, euphoria, forced selling — that push price beyond where fundamentals or normal behaviour justify. The overshoot then *reverts*.

The essential caveat is that mean reversion is a **short-horizon** phenomenon: it works over days to weeks, and it works *against* the longer-term trend. A stock that is rising in a genuine uptrend is not "overbought"; it is strong. Fading a trend is the classic way to lose money — which is why every serious mean-reversion strategy includes a **trend filter**.

## Single-asset mean reversion

**The rules:**

- **Universe:** liquid stocks (or a liquid index).
- **Trend filter:** only take *longs* when the asset is **above its long-term MA** (e.g., 200-day) — i.e., only buy dips *within an uptrend*.
- **Signal:** a short-term oversold extreme — e.g., the **2-period RSI (RSI-2) closing below 5** (a deeply oversold reading after a sharp drop).
- **Entry:** at the close of the oversold day.
- **Exit:** when price closes back **above the 5-day MA** (or after a fixed few days).
- **Stop:** below the entry day's low, for the times the bounce never comes.

**Pseudocode:**

```
for each stock in liquid_universe:
    if close > sma(close, 200):            # trend filter: only dip-buy in uptrends
        rsi2 = rsi(close, length=2)
        if rsi2 < 5 and no open position:   # deeply short-term oversold
            enter_long(close)
        if in_position and close > sma(close, 5):  # bounce confirmed
            exit_long()
        if in_position and close < entry_day_low:  # failed bounce
            exit_long()   # stop
```

## Pairs trading

Pairs trading is mean reversion applied to **two assets** rather than one: it bets that a *spread* between two related assets will revert, regardless of the market's overall direction.

**The idea:** two highly *correlated* assets (e.g., two large banks, or an index and its constituents) tend to move together. When their spread diverges abnormally far, it tends to come back together. A pairs trader goes long the underperformer and short the outperformer, profiting from the convergence.

**The rules:**

- **Pair selection:** find two fundamentally related, highly correlated assets (e.g., correlation > 0.8 over a long window), ideally co-integrated (a statistical test that their spread is stationary — meaning it *reverts*, not just moves together).
- **Signal:** compute the **spread** = price ratio (or log-ratio) of the two assets. When the spread is more than `k` standard deviations from its own mean, the pair is "stretched."
- **Entry:** long the cheap leg, short the rich leg (market-neutral — the market's direction is largely cancelled).
- **Exit:** when the spread reverts back to its mean (or a stop if it diverges further).

**Pseudocode:**

```
for each candidate pair (A, B) in related_universe:
    spread = log(price_A) - log(price_B)      # or price ratio
    mean, sd = rolling(mean, sd, spread, window)
    z = (spread - mean) / sd

    if z > +2 and no position:   # A rich vs B, expect convergence
        enter(short A, long B)
    if z < -2 and no position:   # A cheap vs B
        enter(long A, short B)
    if z crosses 0:              # converged
        exit()
    if |z| > 4:                 # diverged further (stop)
        exit()
```

## Historical context

Mean reversion is one of the oldest and most documented trading patterns — the short-horizon "reversal" effect is the mirror image of momentum, and both coexist at *different horizons* (reversal at days-to-weeks, momentum at months). Pairs trading has been a staple of statistical-arbitrage desks for decades. The unifying truth: **reversion works at short horizons, *with* the trend, and against temporary overshoots** — not against genuine trends.

## Risks and limitations

- **Catching falling knives.** Without the trend filter, single-asset mean reversion buys every crash and loses badly. **The trend filter is the strategy.**
- **Correlation breakdown.** Pairs that were correlated can *de-correlate* (a merger, a shock, a regime change), and the spread never reverts — the classic pairs-trading loss. Co-integration testing and a divergence stop are the defences.
- **Shorting constraints in India.** Pairs trading requires shorting one leg, which for retail is constrained for stocks (and clean only via index derivatives). This limits the practical universe.
- **Frequent small losses.** Mean reversion has a high win rate but occasional larger losses; costs and strict stops matter.

## Summary

- Mean reversion fades short-term overshoots, against the longer trend.
- Single-asset: RSI-2 < 5 below the 200-day MA, exit above the 5-day MA, stop below entry low.
- Pairs: trade a correlated pair's spread back to its mean, market-neutral.
- Reversion works at short horizons *with* the trend — never against a genuine trend.
- Risks: falling knives, correlation breakdown, shorting constraints, cost.

Next: Strategy 3 — time-series trend following.
