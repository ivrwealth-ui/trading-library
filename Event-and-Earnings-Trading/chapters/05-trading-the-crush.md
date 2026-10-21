# 5. Trading the Crush

## The two sides, and their trade-offs

**Selling premium (short vega):**

- **Pros:** you collect inflated premium; the crush works for you; time decay works for you.
- **Cons:** a genuine surprise (a 10% gap on a stock priced for 4%) can hurt far more than the premium collected. This is undefined or wide-defined risk.
- **Suits:** range-bound expectations and high IV, using only a defined-risk structure — an iron condor (see *Options Trading Adjustments*), sized small. A short strangle is undefined risk and does not belong here. *Options Trading Adjustments* cautions against holding short premium through a known event; selling the crush is the deliberate exception — it knowingly accepts the gap risk in exchange for the crush, which is exactly why the risk must be defined and the size small.

**Buying premium (long vega):**

- **Pros:** defined risk; a big surprise pays disproportionately.
- **Cons:** you are fighting the crush — you must be *right about magnitude*, not just direction.
- **Suits:** a specific, under-priced catalyst where you expect a move *larger* than the implied move.

## The decision that makes or breaks an event trade

> **Only buy premium when your expected move is *larger* than the implied move; only sell premium when the implied move is *larger* than you believe the move will be.**

This single comparison — **your move estimate vs the market's implied move** — is the entire edge in IV trading. If you have no view on the *size* of the move, you have no event trade; the premium is already efficiently priced.

## Practical notes for the NSE

- **Weekly-expiry options concentrate the crush** into a short window: the event premium is largest in the near-dated options and collapses hardest. Since SEBI's November 2024 rules each exchange has only one weekly index expiry — currently Nifty on the NSE (Tuesday, moved from Thursday in September 2025) and Sensex on the BSE (Thursday); Bank Nifty and the other indices are monthly only, as are all single-stock options. Check the current weekly-expiry convention before trading weeklies (it has been revised by SEBI/NSE).
- **Liquidity thins into events** in the far strikes; the bid-ask spread can be wider than the edge you are chasing. Always price the *spread*, not the mid.
- **Index events (budget, RBI)** are often better approached with **index** options (deep and liquid) than with a basket of thin single-stock options.
