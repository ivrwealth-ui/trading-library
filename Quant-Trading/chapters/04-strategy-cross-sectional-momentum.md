# 4. Strategy 1 — Cross-Sectional Momentum

## The canonical quant strategy

Cross-sectional momentum is the most replicated strategy in quantitative finance: **rank a universe of assets by their recent returns, hold the strongest, and rebalance on a schedule.** It is the direct implementation of the momentum factor, and it is the natural first strategy for any quant trader because it is simple, well-documented, and testable.

## The idea

The mechanism (from the companion books in this series): investors *under-react* to information, so prices adjust gradually rather than instantly. The result is that assets which have risen recently tend to *keep* rising for a while — and assets which have fallen tend to *keep* falling. Cross-sectional momentum captures this by **always holding the recent winners.**

Crucially, it is *cross-sectional*: it ranks assets *against each other*, so it is always fully invested in *something* — the best of the available options.

## The rules

**Universe:** a liquid stock universe (the NIFTY 500, or a liquid subset), with a liquidity filter (minimum average daily turnover).

**Signal (the ranking):** for each asset, compute its **trailing 12-month total return, skipping the most recent month** (the "12-1" convention — the last month is skipped because it is dominated by short-term *reversal*, which is the opposite of momentum).

**Selection:** rank by this signal and hold the **top decile** (or, practically, the top 10–20 names), equal-weighted.

**Rebalance:** **monthly** (canonical) or quarterly (lower turnover).

**Exit:** an asset is sold when it falls out of the top group at a rebalance. There is no stop — the rebalance *is* the exit.

## Pseudocode

```
universe = liquid_stocks(min_avg_turnover = X)

every month:
    for each stock in universe:
        signal[stock] = total_return(stock, skip=1, window=12_months)

    rank = sort(universe, by=signal, descending)
    holdings = rank[0 : top_N]

    # rotate: sell what dropped out, buy what entered
    sell(previous_holdings not in holdings)
    buy(holdings not in previous_holdings)
    size each holding equal-weight (or 1/top_N of capital)
```

## Historical context

This is the strategy that *defined* the momentum literature — the "buy winners, sell losers" construction documented across markets and decades, including Indian equities. The long-only version (hold winners, hold cash/benchmark rather than shorting losers) retains most of the benefit with far less risk, because it avoids the short side's crash exposure.

Framed honestly: *historically, a diversified portfolio of the strongest 12-1 performers, rebalanced monthly, has tended to outperform the broad market over multi-year horizons — punctuated by sharp reversals in which the prior losers recover fastest.*

## Risks and limitations

- **Momentum crashes.** After a sharp market bottom, prior *losers* snap back hardest, and the portfolio (holding prior winners) lags sharply for a period. This is the known, unavoidable risk.
- **Turnover and costs.** Monthly rotation generates trading; in India, STT, brokerage, and impact costs on frequent churn can consume the edge. A quarterly schedule or a slightly larger top-N reduces this.
- **Concentration and style drift.** Holding 10–20 names is concentrated, and can become heavily tilted to one or two sectors that happened to lead.
- **Parameter fragility.** The exact lookback (12 vs. 9 vs. 6 months) and skip (1 vs. 0 months) shift results; a robust implementation should show an edge across a *range* of these, not a single lucky setting (Chapter 9).

## Summary

- Rank by 12-1 trailing return; hold the top decile / top N; rebalance monthly.
- The canonical momentum strategy, replicated across markets including India.
- Long-only, equal-weighted version retains the edge with less crash risk.
- Risks: momentum crashes, turnover costs, concentration, parameter fragility.

Next: Strategy 2 — mean reversion and pairs trading.
