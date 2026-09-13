# 6. Portfolio Construction and Position Sizing

## The "how much" layer

A signal tells you *what* and *when*; portfolio construction tells you **how much** — and *how much* is where a good signal becomes a good (or a ruined) system. This chapter covers the construction and sizing layer, in close partnership with the Risk Management book in this series.

## The two decisions

Portfolio construction is two decisions:

1. **How much per position** — the sizing rule (fixed-fraction, volatility, Kelly — see the Risk Management book).
2. **How much in total** — the aggregate exposure, and how it is spread across positions.

Both matter, and they are governed by different logics.

## Sizing per position

The universal foundation: **risk a fixed, small fraction of capital per trade** (the 1–2% rule), with size *derived* from the stop:

Position size = (Equity × Risk%) ÷ (Entry − Stop)

This equalises risk across trades regardless of stop distance, and — because it scales with equity — it self-stabilises: it compounds in wins and de-risks in losses. Every sizing method (fixed-fraction, fixed-ratio, ATR/volatility, Kelly, fractional-Kelly) is a variation on this one idea; the Risk Management book covers them in depth.

For a *systematic* framework, the key requirement is that **the sizing rule is as explicit as the signal** — written down, computed from the stop, and applied identically every time.

## Portfolio construction: how the positions combine

A portfolio is not just a list of sized positions; it is a *structure*, and the structure carries risk of its own:

### Equal-weight vs. signal-weight

- **Equal-weight** — every position gets the same allocation. Simple, robust, and the default for most factor and momentum systems.
- **Signal-weight** — positions are sized by the *strength* of the signal (e.g., stronger momentum = larger position). Captures more of the signal, but concentrates risk in the strongest (and often most crowded) names.

For most retail systems, **equal-weight** is the right starting point: it is robust and avoids the hidden concentration of signal-weighting.

### Diversification across drivers

Ten positions that are all large-cap banks are one bet, not ten (the Risk Management book's correlation point). Construction must **diversify across drivers** — sectors, sizes, styles, or asset classes — not just across tickers.

### The exposure cap

A systematic framework needs a **maximum total exposure** — a cap on how much of the account is deployed, and how much is at-risk in aggregate. The signal may say "buy 15 names"; the construction layer says "but never more than X% of equity in the market, and never more than Y% total at-risk."

## Volatility targeting as the portfolio-level control

A particularly useful portfolio-level tool is **volatility targeting**: scale the *entire* portfolio's size so that its expected volatility is roughly constant (see the Quant Trading book). This automatically de-risks the whole book when the market gets wild and re-risks it when it calms — a systemic, rather than per-trade, risk control.

## Pseudocode for the construction layer

```
capital = account_equity
risk_per_trade = 1% of capital

for each signal position:
    size = (capital * risk_per_trade) / (entry - stop)
    # cap: single-position size <= max_position_pct * capital

total_at_risk = sum(size_i * (entry_i - stop_i))
if total_at_risk > max_total_risk:
    scale_down_all_positions_to_fit(max_total_risk)

if net_exposure > max_exposure:
    reduce_to_fit(max_exposure)
```

The pseudocode makes the layers visible: per-trade sizing, a per-position cap, an aggregate at-risk cap, and an exposure cap. Each is a *rule*, checked every rebalance.

## The discipline

The construction and sizing layer is where **most systems are actually won or lost** — not because sizing is clever, but because sizing is where over-betting happens, and over-betting is how positive-expectancy systems get ruined (the Risk Management book's core argument). The framework's job here is to make over-betting *impossible* by writing the caps into the rules.

## Summary

- Two decisions: how much per position, and how much in total.
- Size per position from the stop (1–2% risk); the rule must be as explicit as the signal.
- Prefer equal-weight for robustness; diversify across drivers, not just tickers.
- Cap total at-risk and total exposure; consider volatility targeting at the portfolio level.
- Sizing is where over-betting happens — write the caps into the rules.

Next: backtesting done right — the discipline that keeps the framework honest.
