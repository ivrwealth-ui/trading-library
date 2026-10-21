# 5. Method 3 — Multi-Factor

## 5.1 The philosophy

No single factor works in every regime. Value works when momentum doesn't, and vice versa. A **multi-factor** approach combines several uncorrelated return drivers so that the portfolio is never wholly dependent on one of them being "in season." The aim — and the historical tendency — is a smoother equity curve and higher risk-adjusted return than any single factor alone.

## 5.2 The four-factor foundation

For Indian equities, four factors capture most of the actionable premium:

| Factor | Definition (cross-sectional) | Why it has worked |
|---|---|---|
| **Value** | Cheap = earnings yield, book-to-price, EV/EBITDA | Mean reversion of mispricing |
| **Momentum** | 12-1 month return | Under-reaction, trends |
| **Quality** | ROE/ROA, low debt, stable margins, low accruals | Compounding, survivability |
| **Low volatility** | Low beta / low realized vol | Retail preference for lottery-like stocks leaves low-vol underpriced |

## 5.3 How to combine factors: z-score ranking

The clean, standard way to combine factors is **cross-sectional z-scoring**:

1. For each factor, compute every stock's raw value.
2. Standardize within the universe: **z = (x − mean) / std**.
3. Flip sign where needed so *higher = better* (e.g., low vol → negative z is good, so invert).
4. Take a weighted average of the z-scores (this book uses 30/30/25/15, as below).
5. Rank by composite score; own the top 25–30 names.

```
composite_score = 0.30 * z_value
                + 0.30 * z_momentum
                + 0.25 * z_quality
                + 0.15 * z_lowvol
```

## 5.4 Sector neutrality (optional but valuable)

Indian sectors are highly concentrated (a single IT or bank rally can dominate). Raw factor scores can load you 40% into one sector. Two fixes:

- **Sector-relative scoring:** z-score within each sector, then combine. (Keeps you factor-pure, may still over-weight a hot sector.)
- **Sector cap:** after ranking, cap any single sector at 20% and re-normalize.

## 5.5 A concrete multi-factor screen (example)

```
Universe        : Nifty 500
Factors         :
  - Value     : earnings yield + book-to-price (banks/NBFCs: book-to-price only, see §3.3)
  - Momentum  : 12-1 return
  - Quality   : ROE (5y avg), Net Debt/EBITDA (ex-banks/NBFCs), gross-margin stability (low gross-margin volatility)
  - Low vol   : 1-yr realized volatility (inverted)
Method          : cross-sectional z-scores, weighted 30/30/25/15 (value/momentum/quality/low vol)
Filters         : liquidity floor (₹10 cr/day), no pledge > 20%
Rank            : descending composite score
Action          : top 25–30 names, equal weight (or score-weight), rebalance quarterly
```

## 5.6 Rebalancing cadence

- **Momentum-heavy blends:** rebalance **monthly** (momentum decays fast).
- **Value-heavy blends:** rebalance **quarterly** (value is slow).
- Mixed 4-factor (as above): **quarterly** is a good balance of signal freshness vs turnover cost.
