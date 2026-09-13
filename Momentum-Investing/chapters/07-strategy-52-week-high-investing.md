# 7. Strategy 4 — 52-Week High Investing

## The year's most salient price

The **52-week high** is the highest price an asset has traded at in the past year — and it is one of the most psychologically *salient* numbers in a stock's history, because it is printed everywhere and watched by everyone. The 52-week high strategy turns that salience into a systematic selection rule.

## The idea

Conventional intuition says a stock at a new 52-week high is "expensive" and likely to fall. The evidence says the opposite: stocks *near* their 52-week high have historically been among the strongest performers going *forward*. The reason is behavioural — the 52-week high acts as an **anchor**. Investors under-react to a stock reaching new highs, mentally comparing it to the lower prices they remember; that sluggishness means the stock's rise is not fully priced, and it tends to continue.

This strategy was formalised by **George and Hwang (2004)** in *The 52-Week High and Momentum Investing*, which showed that a stock's **proximity to its 52-week high** predicts future returns about as well as — and in some tests better than — the standard 12-month momentum measure.

## The rules

**Universe:** a liquid stock universe (the NIFTY 500, or a liquid subset).

**Signal — the "52-week high ratio":** for each stock, compute

`52-week high ratio = current price ÷ 52-week high`

A ratio of **1.0** means the stock is *at* its 52-week high; 0.80 means it is 20% below it.

**Selection:** rank the universe by this ratio and hold the stocks **closest to (or at) their 52-week high** — e.g., the top decile, or all stocks within 5% of their high.

**Rebalancing:** **monthly or quarterly**, re-ranking by the ratio.

**Exit / rotation:** a stock is sold when it falls away from its high — i.e., when it drops out of the "near the high" group at a rebalance. (A stop or a longer MA can be added for downside protection.)

## Historical context

George and Hwang's finding is one of the strongest in the momentum literature: nearness to the 52-week high captures momentum *without* needing a specific return window, and it has been shown to hold internationally. The intuitive appeal is that it is a *simple, robust* single-number signal — you do not need to compute trailing returns or choose a lookback; you just ask "how close is it to its year high?"

Framed honestly: *historically, stocks trading at or near their 52-week highs have tended to outperform the broader market over the following months — a statistical tendency, not a guarantee for any individual name.*

## A worked example (NIFTY 500)

- **Universe:** NIFTY 500. **Signal:** price ÷ 52-week high. **Hold:** stocks with a ratio ≥ 0.95 (within 5% of their high). **Rebalance:** quarterly.
- At the quarter's start, ~40 stocks qualify. The investor holds them, equal-weighted.
- Over the quarter, some of those stocks break to *new* highs (strength confirmed) while others pull back 10–15% (dropping below the 0.95 threshold).
- At the **next rebalance**, the laggards are **sold** (they no longer qualify) and the new qualifiers are **bought**.

The result is a portfolio that is *always* concentrated in stocks demonstrating the strongest form of momentum — proximity to new highs — with the rebalance doing all the selection.

## Risks and limitations

- **The signal is a ranking, not a timing rule.** Holding "near the high" stocks in a broad bear market still loses money — the strategy needs an absolute filter (Strategy 2) to step aside in downtrends.
- **Failed breakouts.** Some stocks at new highs reverse immediately (especially on news-driven gaps). Diversification across many names, not one bet, is essential.
- **Concentration and churn.** A tight threshold (≥ 0.95) yields a small, shifting portfolio; a looser one dilutes the signal. There is a trade-off to manage.
- **Market dependence.** The effect is far stronger in rising markets than falling ones.

## Summary

- Buy stocks at or near their 52-week high; rotate quarterly by the 52-week-high ratio.
- Grounded in George & Hwang (2004) — a robust, simple momentum signal.
- The 52-week high is an anchor investors under-react to.
- Needs an absolute filter for bear markets and diversification for failed breakouts.

Next: Strategy 5 — sector and index momentum rotation.
