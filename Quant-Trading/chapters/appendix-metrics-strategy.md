# Appendix — Metrics and Strategy Reference

## The metrics that matter

| Metric | Formula / meaning | What it tells you |
|--------|-------------------|-------------------|
| CAGR | Annualised compound return | Growth rate (single number) |
| Max drawdown | Worst peak-to-trough fall | The risk that decides survival |
| Volatility | Std dev of returns | The bumpiness of the ride |
| Sharpe | (Return − risk-free) ÷ vol | Return per unit of risk |
| Sortino | Downside-only Sharpe | Return per unit of *bad* risk |
| Win rate | Wins ÷ total trades | Meaningless without payoff |
| Profit factor | Gross profit ÷ gross loss | Robust edge summary |
| Expectancy | (Win% × AvgWin) − (Loss% × AvgLoss) | The minimum bar |

## The five strategies at a glance

| # | Strategy | Signal | Position / exit |
|---|----------|--------|-----------------|
| 1 | Cross-sectional momentum | Rank by 12-1 return | Hold top decile; rebalance monthly |
| 2 | Mean reversion / pairs | RSI-2 oversold in uptrend; or pair spread z-score | Bounce / convergence; stop on failure |
| 3 | Time-series trend | Price vs. 200-day MA | Long above, cash below; check monthly |
| 4 | Factor tilts | Composite of value/quality/momentum z-scores | Hold top decile; rebalance quarterly |
| 5 | Vol targeting / seasonality | Scale to target vol; calendar tilt | Overlays on an existing strategy |

## The universal rules

- Every strategy = **universe + signal + sizing + exit**.
- An idea needs a **mechanism**, not just a backtest.
- **Test to disprove**: add costs, remove survivorship, hunt look-ahead, stress parameters.
- **Out-of-sample** is the single best test.
- **Paper trade → live small → reconcile → monitor → retire.** The process is the edge.
