# 4. Method 2 — Momentum

## 4.1 The philosophy

Momentum is the empirical observation that **stocks that have outperformed recently tend to keep outperforming** over the next 3–12 months — and underperformers keep underperforming. It is one of the most robust, cross-market anomalies ever documented (the "momentum premium").

It works for a mix of behavioral (under-reaction to news, herding) and structural (slow diffusion of information) reasons. In India's retail-heavy, trend-following market, **momentum in the midcap space has historically been strong.**

## 4.2 The core construction rules

The canonical momentum measure (popularized by Jegadeesh & Titman, 1993; 12-1 is the standard academic convention) is:

> **Return over months t-12 to t-1** — the last **12 months, excluding the most recent month.**

The "skip the last month" detail matters: short-term reversal (the last ~4 weeks) is negatively correlated with momentum, so including it actually *hurts*.

| Variant | Window | Character |
|---|---|---|
| **12-1 momentum** | 12 mo, skip last 1 | The classic, most robust |
| **6-month** | 6 mo | Faster, more turnover |
| **3-month** | 3 mo | Fast, high turnover, more reversal risk |
| **52-week high proximity** | price / 52-wk high | Simple, surprisingly strong |
| **Dual momentum** | absolute + relative | Adds a market-timing overlay |

## 4.3 Dual momentum

Two conditions must both hold:

1. **Absolute momentum:** the asset's own trailing return > 0 (or > risk-free rate). If the whole market is falling, sit in cash.
2. **Relative momentum:** rank the asset against its peers; own only the top.

Absolute momentum is designed to keep you out of 2008-style crashes; relative momentum is what puts you in the leaders.

## 4.4 Confirmation filters (reduce whipsaws)

- **Price above 200-day MA** (long-term uptrend intact)
- **Price above 50-day MA** (intermediate uptrend)
- **Volume expansion** on the breakout (not just a price drift)
- **Liquidity floor:** minimum average daily traded value (e.g., ₹10–20 crore) so you can actually exit

## 4.5 A concrete momentum screen (example)

```
Universe        : Nifty 500
Compute         : 12-1 month total return, rank all names
Filters         :
  - Absolute 12-mo return     > 0
  - Price                     > 200-DMA
  - Price / 52-week high      > 0.85
  - Avg daily turnover        > ₹10 cr (liquidity)
  - Not stuck at a circuit (price-band) limit
Rank            : descending 12-1 return
Action          : top 20 names, equal weight, rebalance monthly
```

## 4.6 The momentum crash — and how to survive it

Momentum's Achilles' heel is the **momentum crash**: when the market rebounds sharply after a decline, recent *losers* (by then often high-beta) surge hardest while recent *winners* lag. These crashes are fast, violent, and follow volatile down-markets.

Mitigations:

- Keep the **absolute-momentum filter** (cash out when the market trend breaks).
- Combine momentum with a **value or low-volatility factor** (see Method 3) — pure momentum has the worst crash profile, mixed momentum is far smoother.
- Avoid over-concentration in high-beta names at the top of the momentum ranking.
