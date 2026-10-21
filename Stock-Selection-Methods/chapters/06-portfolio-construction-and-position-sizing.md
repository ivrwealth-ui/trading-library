# 6. Portfolio Construction & Position Sizing

A stock list is not a portfolio. How you size and hold positions determines whether your edge survives real trading.

## 6.1 How many stocks?

| Count | Diversification | Tracking to index | Best for |
|---|---|---|---|
| 10–14 | Low | High deviation | Conviction portfolios; accept high vol |
| 15–25 | Moderate | Moderate | The sweet spot for active factor portfolios |
| 30–50 | Good | Tracks index closely | Factor-neutral / near-index portfolios |

Beyond ~25–30 names in one strategy, you mostly dilute the active edge into a quasi-index fund (which you could own for roughly 0.2% a year or less).

## 6.2 Position sizing methods

1. **Equal weight** — 1/N. Simple, robust, forces rebalancing (which itself harvests a reversal premium). Default choice.
2. **Score-weighted** — weight ∝ factor score. More edge if scores are informative, more concentration risk.
3. **Volatility targeting** — weight ∝ 1/σ so each position contributes equal risk. Use 3–6 month realized vol. Particularly useful for the low-vol factor.
4. **R-multiple risk sizing** — size each position by *risk*, not capital: **position size = (portfolio × risk %) / (entry − stop)**. This is the trading-oriented approach from Tharp's school; it caps per-trade loss at a fixed % of capital.

## 6.3 Basic position-sizing math

```
Position value = Total capital × target_weight
Shares         = Position value / price

Risk-based:
  Risk per trade  = Capital × 1%          (e.g. ₹1 lakh on ₹1 cr)
  Position size   = Risk per trade / (entry − stop_loss)
```

**Rule of thumb:** no single position > ~7% of capital at cost (10% for a high-conviction value name), and never risk > 1% of capital on any single trade.

## 6.4 Rebalancing and taxes

In India, rebalancing is *taxable*:

- **Held ≤ 12 months → STCG 20%** on gains.
- **Held > 12 months → LTCG 12.5%** on gains above ₹1.25 lakh/year.

This means **high-turnover strategies (momentum) are tax-disadvantaged in taxable accounts.** Practical fixes:

- Run momentum in a structure where churn doesn't trigger annual STCG (or accept the drag and size it in).
- Prefer **quarterly rebalancing** for value/multi-factor to push most positions past the 1-year LTCG mark.
- Tax-loss harvesting at year-end: realize losers to offset STCG, then re-buy (respect wash-sale/anti-avoidance intent).
