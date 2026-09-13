# 4. Strategy 1 — 12-1 Cross-Sectional Momentum

## The canonical momentum strategy

This is the strategy that *defined* the field: the Jegadeesh-Titman construction, adapted for a long-only investor. It is the purest expression of the momentum factor, and the reference point against which every other momentum strategy is measured.

## The idea

Rank a universe of stocks by their trailing return over a measured window, hold the strongest, and rebalance on a schedule. The "12-1" name encodes the exact settings: **rank on the past 12 months' return, skipping the most recent 1 month.** The skip is deliberate — the last month is dominated by short-term reversal, which would pollute the momentum signal.

## The rules

**Universe:** a liquid stock universe — e.g., the NIFTY 500, or a hand-picked list of the most liquid names. Liquidity matters, because the strategy rebalances regularly and must be able to trade without moving prices.

**Lookback:** trailing **12-month total return**, **excluding the most recent month** (12-1).

**Selection:** rank the universe and hold the **top decile** (top 10%) or, more practically for a retail investor, the **top 10–20 names**.

**Weighting:** equal-weight the selected names (simplest, and avoids over-concentration in one name).

**Rebalancing:** **monthly** is the canonical choice; quarterly is a reasonable lower-turnover alternative.

**Holding:** hold the selected names until the next rebalance, then re-rank and rotate — selling whatever dropped out of the top group and buying whatever entered.

## Historical context

This is the exact construction Jegadeesh and Titman documented in 1993, and it has been replicated across markets and decades since — including in Indian equities. The canonical result was a persistent premium to buying winners (in the long-short version, selling losers as well; the long-only version retains most of the benefit with much less risk). The premium is real but lumpy: it arrives in stretches and suffers sharp reversals, which is why the long-only, diversified, scheduled version is the sensible retail implementation.

Framed honestly: *historically, a diversified portfolio of the strongest 12-1 performers, rebalanced monthly, has tended to outperform the broad market over multi-year horizons — with periods of significant underperformance along the way.*

## A worked example (NIFTY 500)

- **Universe:** the NIFTY 500. **Lookback:** 12-month return, skip the last month. **Hold:** top 20, equal-weighted. **Rebalance:** monthly.
- At the January rebalance, compute each stock's trailing 12-1 return, rank, and hold the top 20.
- Over the next month, the top 20 drift. At the **February rebalance**, re-rank: a few names have dropped out (their momentum faded) and a few new ones have entered (their momentum accelerated).
- The investor **sells the drop-outs, buys the entrants** — mechanically rotating into the strongest names — and repeats monthly.

The result is a portfolio that is *permanently tilted toward strength*, without the investor ever forming an opinion about any individual company. The rebalance does the thinking.

## Risks and limitations

- **Momentum crashes.** After a sharp market bottom, prior *losers* recover fastest, and the portfolio — holding prior *winners* — can lag sharply for a period. This is the strategy's known, unavoidable risk.
- **Turnover and costs.** Monthly rotation generates trading; STT, brokerage, and impact costs must be low, or they consume the premium. (In India, this favours larger, liquid names and possibly a quarterly rather than monthly schedule.)
- **Concentration and style drift.** Holding only 10–20 names is concentrated; the portfolio can also become heavily tilted to one or two sectors that happened to lead.
- **Discipline burden.** The premium arrives in lumps; underperformance stretches test the investor's commitment (Chapter 10).

## Summary

- Rank on 12-1 trailing return; hold the top decile / top N; rebalance monthly.
- The canonical Jegadeesh-Titman strategy, replicated across markets including India.
- Long-only, equal-weighted, diversified version retains most of the edge with less risk.
- Main risks: momentum crashes, turnover costs, concentration, and discipline.

Next: Strategy 2 — absolute momentum, the 200-day filter that keeps you out of bear markets.
