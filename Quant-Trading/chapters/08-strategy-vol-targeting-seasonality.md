# 8. Strategy 5 — Volatility Targeting and Seasonality

## Two overlay ideas that improve almost anything

The first four strategies are *alpha* ideas — ways to pick what to hold. These last two are *overlay* ideas: they do not pick assets, they **adjust the size or timing** of whatever you already hold. They are valuable precisely because they can be bolted onto any strategy.

## Volatility targeting

**The idea:** risk is not constant — the market's volatility rises and falls. A fixed position size therefore means *variable* risk: you are risking far more in a volatile market than a calm one, without intending to. **Volatility targeting** fixes this by **scaling position size inversely to volatility**, so that the *risk* is constant even as volatility moves.

**The mechanism:** estimate current volatility (e.g., the trailing 20-day standard deviation of returns, or the ATR), set a target volatility, and size accordingly:

Position size = (Target volatility ÷ Realised volatility) × base size

When volatility rises, size shrinks; when it falls, size grows — automatically de-risking in turbulent markets and re-risking in calm ones.

**Why it works:** it stabilises the *risk* of the portfolio, which (as the Risk Management book explains) is what determines survival. Historically, volatility-targeted portfolios have tended to show smoother returns and smaller drawdowns than fixed-size portfolios, for the same underlying holdings.

**Pseudocode:**

```
target_vol = 10% (annualised)
realised_vol = std(daily_returns, window=20) * sqrt(252)

leverage = target_vol / realised_vol        # >1 in calm, <1 in volatile
position_size = base_size * leverage         # capped at some max
```

## Seasonality

**The idea:** markets exhibit **calendar patterns** — returns that are systematically stronger or weaker in specific periods. The best-documented include:

- **Month-end / turn-of-month effects** — returns concentrated around month boundaries.
- **Specific months** — certain months have historically been stronger or weaker in specific markets.
- **The pre-holiday effect** — returns around holidays.
- **Payday / SIP flows** — in India, systematic monthly inflows (SIPs, NPS) create recurring liquidity patterns.

**The mechanism:** seasonality effects are driven by *recurring flows* (payroll/SIP contributions, tax-related selling, window-dressing by funds). They are weak and fragile — far weaker than the factor premia — but they have been repeatedly documented.

**How it is used:** not as a standalone strategy, but as a **tilt** — slightly over-weight positions during historically favourable periods, or adjust entry timing to avoid known weak windows. A seasonality overlay is a *small* adjustment to a real strategy, not a strategy in itself.

## The honest caveat

Both overlays are real but modest, and both carry a specific warning:

- **Volatility targeting** is robust and broadly useful — but it does not create alpha; it stabilises risk. It can *reduce* returns in a strong bull market (because it de-risks as volatility rises) in exchange for smoother drawdowns.
- **Seasonality** is weak and fragile; it is the kind of pattern that looks strong in a backtest and evaporates live, and it is a notorious source of overfitting (Chapter 9). Treat any seasonality result with scepticism unless it survives out-of-sample testing.

Framed honestly: *historically, scaling positions to target a constant volatility has tended to smooth returns and reduce drawdowns, while calendar effects have been weak, recurring, and easy to overstate.*

## Summary

- Volatility targeting scales size inversely to volatility, holding risk constant.
- Seasonality overlays tilt toward historically favourable calendar periods.
- Both are overlays that improve an existing strategy, not standalone alpha.
- Volatility targeting is robust and stabilises risk; seasonality is weak and overfit-prone.

Next: the backtesting pitfalls that make every strategy in this book look better than it is.
