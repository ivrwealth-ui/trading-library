# 10. The Master Workflow

A complete weekly/quarterly operating loop for running any of the three methods:

## 10.1 Weekly (~30 minutes)

1. Download latest EOD prices + any corporate actions for your universe.
2. Update liquidity filters (average daily turnover).
3. Flag any stop-loss / thesis-break triggers on existing holdings.
4. Check the market regime (Nifty vs 200-DMA) for the absolute-momentum cash switch.

## 10.2 Monthly (momentum)

1. Recompute 12-1 momentum and 52-week-high proximity.
2. Re-rank; sell anything that fell out of the top 20 (or a buffer such as the top 30).
3. Buy replacements at next open; record fills.

## 10.3 Quarterly (value / multi-factor)

1. Pull latest quarterly fundamentals (announced, not estimates).
2. Recompute z-scores across the universe.
3. Re-rank, rebalance to targets, tax-aware (sell losers, hold > 12 months for LTCG).
4. Review governance flags (new pledges, related-party deals).

## 10.4 Annually

1. Full post-mortem: CAGR, drawdown, Sharpe, turnover, taxes paid.
2. Re-test on fresh out-of-sample data.
3. Decide: keep, adjust, or retire the method — on evidence, not emotion.

## 10.5 The decision journal

Log every trade: *why* you entered (which rule), *what* you expected, and *what* actually happened. After 20–30 trades the journal reveals whether you're failing at the *method* or at *execution* — the two failures need completely different fixes.
