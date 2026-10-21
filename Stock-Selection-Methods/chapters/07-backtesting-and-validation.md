# 7. Backtesting & Validation

## 7.1 The golden rules of an honest backtest

1. **Point-in-time data only.** See §2.4. If you can't reconstruct what was known on each date, your result is fiction.
2. **Survivorship-free universe.** Include delisted and merged names at their historical prices.
3. **Costs included.** Model STT (0.1% sell + buy on delivery), GST 18% on brokerage, stamp duty (~0.015%), exchange/SEBI charges, and **impact cost** (rule of thumb: 0.1–0.5% for small caps, less for large caps).
4. **No look-ahead in rankings.** Rank on day *t* using data through *t-1*; trade at *t+1* open.
5. **Out-of-sample discipline.** Never tune parameters on the full history and then declare victory. Reserve the last ~30% of the window as out-of-sample.

## 7.2 Key statistics to report

| Metric | What it tells you | Healthy signal (rule of thumb) |
|---|---|---|
| **CAGR** | Compound growth | > benchmark by a real margin |
| **Max drawdown** | Worst peak-to-trough loss | Within your emotional & survival tolerance |
| **Sharpe** | Return per unit of vol | > 0.8 is decent; > 1.2 strong |
| **Sortino** | Return per unit of *downside* vol | Preferable to Sharpe for equity |
| **Win rate** | % of winning trades | Informative, not decisive |
| **Turnover** | % of book traded per period | Drives costs & taxes |
| **Alpha / beta vs Nifty 500** | What's market, what's skill | Alpha > 0 net of costs |
| **Hit rate vs benchmark** | % of years beating index | > 60% is good |

## 7.3 Walk-forward validation

To guard against overfitting:

1. Split history into rolling windows (e.g., 5-year train, 1-year test).
2. Tune parameters only on the training window.
3. Apply unchanged to the test window.
4. Slide forward; repeat.
5. If the method is profitable *out-of-sample across most windows*, you have a robust edge — not a curve-fit.

## 7.4 Paper-trade before capital

Run the method live on paper for 1–2 quarters. Track: fill realism, impact cost vs model, slippage, and your own discipline in following the rules. If you can't follow your own system on paper, you won't follow it with money.
