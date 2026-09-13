# 6. Portfolio-Level Risk

## The danger that lives across trades

Per-trade risk management is necessary but not sufficient. A portfolio can be full of individually "safe" 1%-risk positions and still be dangerous — because **risk is not additive when positions are correlated.** This chapter covers the risk that exists *between* trades, not within one.

## The correlation problem

Suppose you hold ten positions, each risking 1% with its own stop. Naively, your total risk is 10%. But if all ten are *long the same market* — ten Indian large-caps, say — then they are not ten independent bets; they are **one bet on the broad market, expressed ten times.**

In a market crash, all ten hit their stops together. Your "10% of diversified risk" is actually a single concentrated 10% loss, because the positions moved as one.

The principle: **your portfolio's real risk is your net exposure, not your number of positions.** Ten correlated positions are one position, sized ten times too large.

## Measuring the exposure that matters

Three aggregate numbers summarise portfolio risk:

1. **Net delta / net direction** — the sum of all positions' directional exposure. If everything is long, net direction is fully long; a market down-move hurts everything at once.
2. **Net exposure to a single factor** — a portfolio of all large-caps is exposed to the *large-cap* factor; all banks are exposed to the *financials* factor; all momentum names to the *momentum* factor (and its crash risk). Concentration in one factor is hidden risk.
3. **Correlation between positions** — if your "diversified" book is all driven by the same macro driver, diversification is illusory.

## Portfolio-level rules

A handful of rules manage this:

### 1. Cap total open risk

Limit the **sum** of open risk (e.g., total at-risk across all positions ≤ 6–10% of equity). If every position risks 1%, do not hold more than 6–10 concurrent positions. This caps the worst-case simultaneous drawdown.

### 2. Diversify across drivers

Hold positions that are driven by *different* things — different sectors, different sizes, different styles (momentum + value + quality), or different asset classes. True diversification is diversification of *drivers*, not of tickers.

### 3. Watch net exposure, not just positions

If the market is below its 200-day MA, and your entire book is long, you have one large short-the-trend bet — regardless of how many names it is spread across. A broad **regime filter** (reduce long exposure in downtrends) is portfolio-level risk management.

### 4. Rebalance correlation

Periodically check: *if the market fell 10% tomorrow, what would this portfolio do?* If the honest answer is "fall ~10%," it is not diversified — it is one bet. Rebalance toward genuinely different drivers.

## The concentration traps

Three specific traps to name:

- **Sector concentration** — ten banks is one financials bet, not ten bets.
- **Style concentration** — ten momentum names all crash together in a momentum reversal.
- **Correlated "hedges"** — a hedge that is itself correlated with the portfolio (e.g., hedging Indian stocks with an asset that falls when they do) is not a hedge; it is more of the same.

## The honest bottom line

Portfolio-level risk is the answer to the question "where could I lose a lot, all at once?" Per-trade rules answer "in any one trade" (small); portfolio rules answer "across the book" (potentially large). Both questions must be answered. A trader who sizes each trade perfectly but holds ten copies of the same bet has solved only the easy half of the problem.

## Summary

- Risk is not additive when positions are correlated; ten correlated positions are one bet.
- Real risk is net exposure (direction, factor, correlation), not position count.
- Rules: cap total open risk, diversify across drivers, watch net exposure, rebalance correlation.
- Concentration traps: sector, style, and correlated "hedges".
- Manage risk both per-trade and across the book.

Next: margin, leverage, and tail risk — the forces that turn a bad day into a catastrophe.
