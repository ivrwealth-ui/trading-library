# 7. Strategy 4 — Factor Tilts

## Owning the characteristics that outperform

Factor investing is a different *kind* of quant strategy: instead of timing or ranking on price alone, it **tilts a portfolio toward the measurable characteristics that have historically been associated with higher returns** — value, quality, size, and momentum. It is the systematic implementation of the classic "what makes a stock good" insights.

## The idea

In modern finance, a **factor** is a measurable characteristic that explains differences in returns across stocks. The four most established equity factors:

- **Value** — cheap stocks (low P/E, P/B, P/CF) have historically outperformed expensive ones.
- **Quality** — profitable, low-debt, high-return-on-capital businesses have outperformed weak ones.
- **Size** — smaller companies have historically earned a premium over larger ones (with caveats).
- **Momentum** — recent winners outperform recent losers (the subject of the last three chapters).

A **factor tilt** is a portfolio that *overweights* stocks scoring high on one or more factors and *underweights* (or avoids) the rest. It is the systematic version of "buy good, cheap, trending companies" — done as a ranking and rebalancing problem.

## The rules (a quality + value + momentum tilt)

**Universe:** a liquid stock universe (the NIFTY 500).

**Scoring:** for each stock, compute a composite score from factor metrics:

- **Value:** inverse P/E, inverse P/B (higher = cheaper).
- **Quality:** ROE, low debt-to-equity, stable margins.
- **Momentum:** trailing 12-1 return.

Standardise each metric (convert to a z-score or percentile rank) so they are comparable, then combine:

Composite score = w₁·Value + w₂·Quality + w₃·Momentum

**Selection:** hold the **top decile (or quintile)** by composite score, equal- or score-weighted.

**Rebalance:** **quarterly or semi-annually** (factor premia are slow-moving; high frequency adds cost, not edge).

## Pseudocode

```
universe = liquid_stocks(min_avg_turnover = X)

every quarter:
    for each stock in universe:
        value_score  = zscore(-1 * pe_ratio) + zscore(-1 * pb_ratio)
        qual_score   = zscore(roe) + zscore(-1 * debt_to_equity)
        mom_score    = zscore(trailing_12m_return, skip=1)

        composite = w1*value_score + w2*qual_score + w3*mom_score

    rank = sort(universe, by=composite, descending)
    holdings = rank[0 : top_N]
    rebalance to holdings, equal-weight
```

## Historical context

Factor premia — value, quality, size, momentum — are among the most extensively documented phenomena in academic finance, replicated across markets and decades. The honest nuance, well established in the literature: **individual factors go through long periods of underperformance** (value, in particular, has had extended dry spells), and **combining factors** (which are often uncorrelated) has historically produced a smoother, more robust premium than any single factor alone.

Framed honestly: *historically, portfolios tilted toward cheap, high-quality, positive-momentum companies have tended to outperform the broad market over long horizons — but any single factor can lag for years, and the premium is compensation for real risk.*

## Risks and limitations

- **Factor droughts.** A factor can underperform for a decade (value in the 2010s). A single-factor tilt requires unusual patience; combining factors reduces this.
- **Data and definition risk.** The result depends heavily on *how* you define value, quality, and momentum, and on the quality of the fundamental data. In India, reliable historical fundamental data (especially point-in-time, restated correctly) is harder to obtain than price data.
- **Turnover vs. persistence.** Factor premia are slow-moving; over-trading (monthly) adds cost without edge. But too-infrequent rebalancing lets the tilt drift.
- **Crowding.** Popular factors (quality, momentum) can become crowded, compressing their premium in certain regimes.

## Summary

- Factor tilts overweight measurable characteristics: value, quality, size, momentum.
- Combine standardised factor scores into a composite; hold the top decile; rebalance quarterly.
- Factors are well-documented but go through long droughts; combining them smooths the ride.
- Risks: factor droughts, data/definition sensitivity, turnover, crowding.

Next: Strategy 5 — volatility targeting and seasonality.
