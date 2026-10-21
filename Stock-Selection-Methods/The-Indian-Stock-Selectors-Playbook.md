# The Indian Stock Selector's Playbook

## Three systematic methods for picking stocks on the NSE — Value, Momentum, and Multi-Factor

---

**Published by StratLab**

---

*Written as a structured reference book. Educational content only — not investment advice. Do your own research; consult a SEBI-registered adviser before acting.*

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading involves substantial risk of loss and is not suitable for everyone. You can lose part or all of your trading capital.
- All examples, figures, and historical observations are illustrative. Historical performance never guarantees future results. Strategies described here have worked *historically* in certain conditions; that does not mean they will work in the future or in your specific situation.
- Margin, taxes (STT, stamp duty), brokerage, and other regulatory details change over time. Always verify current rules and costs before trading.
- Nothing in this book should be read as a promise of profit or a guarantee that any strategy will be profitable.

By reading this book, you agree that you are solely responsible for your own trading decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## Table of Contents

1. Foundations
2. The Indian Universe & Data
3. Method 1 — Value Investing
4. Method 2 — Momentum
5. Method 3 — Multi-Factor
6. Portfolio Construction & Position Sizing
7. Backtesting & Validation
8. Risk & Position Management
9. Pitfalls in Indian Markets
10. The Master Workflow

Appendix A — Formulas & Metrics Reference
Appendix B — Indian Data Sources & Tools
Appendix C — Example Screens
Appendix D — Glossary

---


# 1. Foundations

## 1.1 What a stock selection method actually is

A stock selection method is a **repeatable, rule-based process** that ranks or filters a universe of stocks down to a shortlist you can act on. The three methods in this book — **value**, **momentum**, and **multi-factor** — are three different lenses on the same question: *"which stocks, out of the ~2,000 tradeable names on the NSE, are most likely to deliver outsized risk-adjusted returns over my holding period?"*

A good method has five properties:

| Property | What it means | Why it matters |
|---|---|---|
| **Systematic** | Rules you can write down and re-run | Removes mood, ego, and hindsight |
| **Ranking-based** | Produces an ordered list, not a yes/no | Lets you pick a portfolio size, not a binary |
| **Testable** | Can be backtested on historical data | You can estimate edge *before* risking money |
| **Survivable** | Works across market regimes | Not curve-fit to one bull market |
| **Tradeable** | Considers liquidity and costs | A screen that can't be traded isn't a strategy |

## 1.2 The uncomfortable truth: why most screens fail

Before we build anything, understand the three silent killers of retail screens:

1. **Survivorship bias.** You backtest on today's Nifty 500 — but today's list already *excludes* every company that got delisted, merged, or went bankrupt over the test window. Your historical returns are inflated because you only tested survivors. **Always use point-in-time universes.**

2. **Look-ahead bias.** Using data that wasn't available at the decision time. Classic example: screening on FY25 earnings in March 2025, before results are announced. In India, a company's FY is April–March; results for Q4 (Jan–Mar) typically land in April–May. Screening on "TTM earnings" that silently includes a just-announced quarter is look-ahead.

3. **Costs & impact.** A beautiful 25% CAGR backtest that ignores brokerage, STT, GST, stamp duty, and — critically — *impact cost* (the price you actually get in an illiquid small-cap) can turn negative in live trading.

## 1.3 The core formula everything is built on

Every method in this book reduces to the same equation — **expected return**:

> **E[return] ≈ (win rate × avg win) − (loss rate × avg loss) − costs**

A method's job is to tilt this equation in your favor. Value tilts the *average win* (buy cheap, mean-revert up). Momentum tilts the *win rate* (ride confirmed trends). Multi-factor tries to do both while smoothing the ride.

## 1.4 A word on the Indian context

India is a **retail-heavy, structurally growing, but cyclical and governance-sensitive** market:

- **Long runway.** Nominal GDP growth that has historically run at roughly 10%+ means corporate earnings *can* compound at double digits — a tailwind most developed markets don't offer.
- **Wide quality dispersion.** The gap between a clean compounding franchise and a value trap / fraud is enormous. Screening that works in the US often needs Indian adaptation.
- **Concentrated ownership.** Promoter (founder-family) holdings of roughly 50–70% are common. Promoter behavior — pledging, related-party transactions, dilution — matters more than in the US.
- **Different cost & tax regime.** STT, stamp duty, and short-term capital gains (20%) vs long-term (12.5% over ₹1.25 lakh) (rates as of 2026 — check the current Finance Act) directly affect which methods are tradeable.


# 2. The Indian Universe & Data

## 2.1 The universe ladder

India has a clean, liquid tiered index system. Pick your universe deliberately — it defines both your opportunity and your execution cost.

| Universe | Constituents | Liquidity | Notes |
|---|---|---|---|
| Nifty 50 | 50 large caps | Excellent | Mostly institutional; momentum is weaker, value plays classic |
| Nifty Next 50 | 51–100 | Very good | Sweet spot for quality compounding + multi-factor |
| Nifty Midcap 150 | 101–250 | Good | Higher growth, higher vol, momentum works well |
| Nifty Smallcap 250 | 251–500 | Mixed | High returns, high illiquidity/impact risk |
| **Nifty 500** | 1–500 | Broad | Best default universe for systematic methods |
| Nifty Total Market | ~750+ | Variable | Adds microcaps; treat with caution |

**Recommendation:** start with **Nifty 500** for backtesting and screening, then tilt execution toward the top ~200–300 names where impact cost is tolerable. Avoid the microcap tail unless you have a dedicated illiquidity risk budget.

## 2.2 Data you'll need (and where to get it)

| Data | Why | Sources |
|---|---|---|
| Prices (EOD OHLCV) | Returns, momentum, vol | NSE/BSE bhavcopy, broker APIs (Zerodha Kite), `yfinance`, Chartink |
| Fundamentals | Value & quality factors | Screener.in, Tijori Finance, Trendlyne, exchange filings; Capitalmind (a PMS/mutual-fund house whose public research is useful context, not a data feed) |
| Corporate actions | Adjust for bonus/split/rights | NSE announcements, bhavcopy metadata |
| Index membership | Universe definition | NSE indices page, monthly rebalance lists |
| Delistings/mergers | Survivorship-bias correction | NSE, SEBI orders, MCA |
| Ownership | Promoter/pledge/FII-DII | BSE shareholding pattern (quarterly) |

**See Appendix B (Indian Data Sources & Tools) for a full tool list.**

## 2.3 Adjustments you must never skip

Indian companies issue **bonus shares, stock splits, rights issues, and buybacks** frequently. Raw price data will show phantom drops that ruin both momentum and volatility calculations. Three rules:

1. **Use adjusted (split/bonus-adjusted) prices** for anything involving multi-period returns.
2. **For total return**, add dividends back — India's market dividend yield has historically run at roughly 1–1.5%, which compounds materially over a decade. (Dividends are taxable in the investor's hands since FY21.)
3. **Never mix standalone and consolidated financials.** For companies with meaningful subsidiaries, always use **consolidated** figures; standalone hides the real picture for holding structures and diversified groups.

## 2.4 Point-in-time discipline

For an honest backtest, every factor value must be the value *known on that date*:

- Earnings: use the most recent **announced** quarter, not simply the latest quarter to have ended.
- Index membership: use the membership list *as of that month*.
- Shareholding: listed companies must file the quarterly pattern within 21 days of quarter-end (SEBI LODR Regulation 31) — use the filing date, not the quarter-end date.


# 3. Method 1 — Value Investing

## 3.1 The philosophy

Value investing buys assets for **less than their intrinsic worth** and waits for the market to correct the mispricing. The payoff comes from the gap between *price* and *value* — the **margin of safety** — closing over time.

It is the oldest, most-studied anomaly. In India it works best in:

- Deep market corrections (everyone's fearful, everything's cheap)
- Sectors temporarily out of favor (cyclicals at trough earnings, not peak)
- Neglected mid/small caps with real assets and earnings

It underperforms in long speculative bull runs — which is exactly when it *should* feel uncomfortable to hold.

## 3.2 The metrics

| Metric | Formula | What it captures | Watch out |
|---|---|---|---|
| **P/E** | Price / EPS (TTM) | Cheapness of earnings | Cyclical peak earnings → false cheap |
| **P/B** | Price / Book value | Asset-based cheapness | Best for **financials**; misleading for asset-light tech |
| **EV/EBITDA** | Enterprise value / EBITDA | Operating cheapness, debt-aware | Better than P/E across capital structures |
| **Earnings yield** | EPS / Price (=1/P/E) | Direct comparable to bond yield | Compare vs 10-yr G-sec yield |
| **Dividend yield** | DPS / Price | Income + discipline signal | High yield can signal distress |
| **Graham number** | √(22.5 × EPS × BVPS) | Quick intrinsic-value ceiling | Conservative; few large caps pass |
| **P/S** | Price / Sales | For early/unprofitable growth | Ignores profitability |

## 3.3 India-specific adaptations

1. **Use P/B for banks and NBFCs, not P/E.** Provisioning, NPA cycles, and tax treatment make P/E noisy for financials. Screen banks on P/B (historically roughly 0.8–1.5× for PSU, 2–3× for quality private) **plus** ROA (>1%), ROE (>12%), and NPA trend.

2. **Beware the commodity value trap.** A steel or chemical company at 6× P/E is often at **peak-cycle earnings** — the P/E is low *because* earnings are about to fall. Always check whether current margins are above the 10-year average. Value ≠ cheap on a cyclical high.

3. **Beware the governance discount.** Some Indian "cheap" stocks are cheap for good reason: promoter pledging, opaque related-party deals, chronic dilution. A 5× P/E with a questionable promoter is not a bargain — it's a terminal-value bet.

4. **Consolidated earnings only.** Holding companies and diversified groups routinely trade at a "conglomerate discount" that *looks* like value but is structurally persistent.

## 3.4 A concrete value screen (example)

Rank the Nifty 500 on a composite value score, excluding financials (handled separately):

```
Universe        : Nifty 500 (ex-banks/NBFCs)
Filters         :
  - TTM P/E          < 15
  - P/B              < 1.5
  - Debt/Equity      < 1.0  (or Net Debt/EBITDA < 2)
  - ROE (5-yr avg)   > 10%  (value-trap guard)
  - Positive operating cash flow, last 3 yrs
  - Promoter pledge  < 20%  (governance guard)
Rank            : ascending EV/EBITDA
Action          : top 15–25 names, equal weight, review quarterly
```

**The value-trap guard is non-negotiable.** Cheap + deteriorating = a trap; cheap + stable/improving = a candidate.

## 3.5 When value works, and when to abandon it

- **Works:** post-crash recoveries, sector rotation into out-of-favor industries, mean-reversion regimes.
- **Struggles:** long momentum bull markets, deflationary credit events (cheap gets cheaper), fraud-heavy microcaps.


# 4. Method 2 — Momentum

## 4.1 The philosophy

Momentum is the empirical observation that **stocks that have outperformed recently tend to keep outperforming** over the next 3–12 months — and underperformers keep underperforming. It is one of the most robust, cross-market anomalies ever documented (the "momentum premium").

It works for a mix of behavioral (under-reaction to news, herding) and structural (slow diffusion of information) reasons. In India's retail-heavy, trend-following market, **momentum in the midcap space has historically been strong.**

## 4.2 The core construction rules

The canonical momentum measure (popularized by Jegadeesh & Titman, 1993; 12-1 is the standard academic convention) is:

> **Return over months t-12 to t-1** — the last **12 months, excluding the most recent month.**

The "skip the last month" detail matters: short-term reversal (the last ~4 weeks) is negatively correlated with momentum, so including it actually *hurts*.

| Variant | Window | Character |
|---|---|---|
| **12-1 momentum** | 12 mo, skip last 1 | The classic, most robust |
| **6-month** | 6 mo | Faster, more turnover |
| **3-month** | 3 mo | Fast, high turnover, more reversal risk |
| **52-week high proximity** | price / 52-wk high | Simple, surprisingly strong |
| **Dual momentum** | absolute + relative | Adds a market-timing overlay |

## 4.3 Dual momentum

Two conditions must both hold:

1. **Absolute momentum:** the asset's own trailing return > 0 (or > risk-free rate). If the whole market is falling, sit in cash.
2. **Relative momentum:** rank the asset against its peers; own only the top.

Absolute momentum is designed to keep you out of 2008-style crashes; relative momentum is what puts you in the leaders.

## 4.4 Confirmation filters (reduce whipsaws)

- **Price above 200-day MA** (long-term uptrend intact)
- **Price above 50-day MA** (intermediate uptrend)
- **Volume expansion** on the breakout (not just a price drift)
- **Liquidity floor:** minimum average daily traded value (e.g., ₹10–20 crore) so you can actually exit

## 4.5 A concrete momentum screen (example)

```
Universe        : Nifty 500
Compute         : 12-1 month total return, rank all names
Filters         :
  - Absolute 12-mo return     > 0
  - Price                     > 200-DMA
  - Price / 52-week high      > 0.85
  - Avg daily turnover        > ₹10 cr (liquidity)
  - Not stuck at a circuit (price-band) limit
Rank            : descending 12-1 return
Action          : top 20 names, equal weight, rebalance monthly
```

## 4.6 The momentum crash — and how to survive it

Momentum's Achilles' heel is the **momentum crash**: when the market rebounds sharply after a decline, recent *losers* (by then often high-beta) surge hardest while recent *winners* lag. These crashes are fast, violent, and follow volatile down-markets.

Mitigations:

- Keep the **absolute-momentum filter** (cash out when the market trend breaks).
- Combine momentum with a **value or low-volatility factor** (see Method 3) — pure momentum has the worst crash profile, mixed momentum is far smoother.
- Avoid over-concentration in high-beta names at the top of the momentum ranking.


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


# 6. Portfolio Construction & Position Sizing

A stock list is not a portfolio. How you size and hold positions determines whether your edge survives real trading.

## 6.1 How many stocks?

| Count | Diversification | Tracking to index | Best for |
|---|---|---|---|
| 10–14 | Low | High deviation | Conviction portfolios; accept high vol |
| 15–25 | Moderate | Moderate | The sweet spot for active factor portfolios |
| 30–50 | Good | Tracks index closely | Factor-neutral / near-index portfolios |

Beyond ~25–30 names in one strategy, you mostly dilute the active edge into a quasi-index fund (which you could own for roughly 0.2% a year or less).

## 6.2 Position sizing methods

1. **Equal weight** — 1/N. Simple, robust, forces rebalancing (which itself harvests a reversal premium). Default choice.
2. **Score-weighted** — weight ∝ factor score. More edge if scores are informative, more concentration risk.
3. **Volatility targeting** — weight ∝ 1/σ so each position contributes equal risk. Use 3–6 month realized vol. Particularly useful for the low-vol factor.
4. **R-multiple risk sizing** — size each position by *risk*, not capital: **position size = (portfolio × risk %) / (entry − stop)**. This is the trading-oriented approach from Tharp's school; it caps per-trade loss at a fixed % of capital.

## 6.3 Basic position-sizing math

```
Position value = Total capital × target_weight
Shares         = Position value / price

Risk-based:
  Risk per trade  = Capital × 1%          (e.g. ₹1 lakh on ₹1 cr)
  Position size   = Risk per trade / (entry − stop_loss)
```

**Rule of thumb:** no single position > ~7% of capital at cost (10% for a high-conviction value name), and never risk > 1% of capital on any single trade.

## 6.4 Rebalancing and taxes

In India, rebalancing is *taxable*:

- **Held ≤ 12 months → STCG 20%** on gains.
- **Held > 12 months → LTCG 12.5%** on gains above ₹1.25 lakh/year.

This means **high-turnover strategies (momentum) are tax-disadvantaged in taxable accounts.** Practical fixes:

- Run momentum in a structure where churn doesn't trigger annual STCG (or accept the drag and size it in).
- Prefer **quarterly rebalancing** for value/multi-factor to push most positions past the 1-year LTCG mark.
- Tax-loss harvesting at year-end: realize losers to offset STCG, then re-buy (respect wash-sale/anti-avoidance intent).


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


# 8. Risk & Position Management

## 8.1 The risk pyramid

1. **Systemic (market) risk** — you can't diversify it away. Manage with: absolute-momentum filter, cash allocation, index hedges (for advanced users).
2. **Idiosyncratic (stock) risk** — diversifiable. Manage with: N holdings, position caps, stop-losses.
3. **Behavioral risk** — *your own* over-trading, panic-selling, revenge-trading. Managed only by written rules and discipline. This is the biggest risk of all (Tharp stresses that the trader is the most important factor in any system).

## 8.2 Position-level controls

- **Stop-loss:** a pre-committed exit price. For trend/momentum: below the 50-DMA or a trailing 8–10%. For value: a stop based on *thesis break* (fundamentals changed), not just price.
- **Max drawdown circuit-breaker:** if the portfolio falls X% (say 15%) from peak, halve position sizes; if it falls 2X, go to cash and review. Write these numbers down *before* the drawdown happens.
- **Concentration limits:** max ~7% per name at cost (10% for a high-conviction value name), max 20–25% per sector.

## 8.3 The Kelly question (conceptual)

Kelly says the optimal bet fraction ≈ edge / odds. Full Kelly is wildly aggressive and assumes you know your edge exactly (you don't). **Practical rule: use a small fraction (⅛ to ¼ Kelly)** or, more simply, fixed-fractional risk of 0.5–1% per trade. Survival beats optimization.


# 9. Pitfalls in Indian Markets

These bite Indian retail investors more than the textbook factors.

| Pitfall | What happens | Defense |
|---|---|---|
| **Value trap (cyclical)** | Cheap at peak earnings, gets cheaper | Check margin vs 10-yr average; avoid "cheap" cyclicals at peak |
| **Value trap (governance)** | Cheap because fraud/dilution/pledge | Pledge < 20%, related-party check, promoter history |
| **Illiquidity** | Can't exit at quoted price | Avg daily turnover floor; avoid < ₹5 cr |
| **Circuit filters** | 2/5/10/20% price bands freeze trading | Avoid names routinely hitting circuits |
| **Survivorship in data** | Backtests look too good | Point-in-time universes |
| **Overtrading (STCG)** | 20% STCG eats momentum edge | Quarterly+ rebalancing; tax-aware sizing |
| **Holding-company discount** | "Cheap" conglomerate never re-rates | Use consolidated; know structural discounts persist |
| **PSU trap** | Cheap, high yield, but policy-dependent & capital-unfriendly | Treat PSUs as a distinct factor, not classic value |
| **FII/DII flow chasing** | Buying what's already crowded | Don't chase a factor at its 90th-percentile valuation |
| **Reversal after IPO/lock-in** | New listings distort short-term momentum | Exclude < 12 months listed from backtests |


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


# Appendix A — Formulas & Metrics Reference

| Metric | Formula |
|---|---|
| EPS (TTM) | Net profit (consolidated, TTM) / weighted shares |
| P/E | Price / EPS (TTM) |
| Book value/share | (Equity − preference) / shares |
| P/B | Price / Book value/share |
| EV | Market cap + total debt − cash & equivalents |
| EV/EBITDA | EV / EBITDA (TTM) |
| Earnings yield | EPS / Price |
| Dividend yield | DPS (TTM) / Price |
| ROE | Net profit / average equity |
| ROA | Net profit / average total assets |
| Net Debt/EBITDA | (Total debt − cash) / EBITDA |
| Current ratio | Current assets / current liabilities |
| Interest coverage | EBIT / interest expense |
| 12-1 momentum | (P[t-1] / P[t-12]) − 1 |
| 52-wk proximity | Price / 52-week high |
| Realized vol (1y) | std of daily returns × √252 |
| Beta | cov(stock, index) / var(index) |
| Graham number | √(22.5 × EPS × BVPS) |
| Z-score | (x − μ) / σ |


# Appendix B — Indian Data Sources & Tools

| Category | Tools |
|---|---|
| **Screening & fundamentals** | Screener.in, Tijori Finance, Trendlyne, StockEdge, Tickertape (Capitalmind publishes research commentary but is a PMS/mutual-fund house, not a screener) |
| **EOD / historical prices** | NSE/BSE bhavcopy, Zerodha Kite API, Upstox API, `yfinance`, `nselib`, `jugaad-data`, `nsepython` |
| **Charts & technical** | TradingView, Chartink, GoCharting |
| **Corporate actions / filings** | NSE & BSE announcement feeds, MCA, company IR pages |
| **Shareholding & pledge** | BSE quarterly shareholding pattern, Trendlyne pledge tracker |
| **Index data** | NSE indices (Nifty 50/Next 50/Midcap/Smallcap/500), Nifty rebalance lists |
| **Institutional flows** | NSE FII/DII provisional data (daily), NSDL/CDSL FPI reports |
| **Screen automation** | Python (pandas) + broker APIs, or no-code: Chartink, Screener.in exports |


# Appendix C — Example Screens

## C.1 Value screen (ex-financials)

```
P/E (TTM)              < 15
P/B                    < 1.5
Net Debt/EBITDA        < 2
ROE (5-yr avg)         > 10%
Operating CF           positive 3 yrs
Promoter pledge        < 20%
→ rank by EV/EBITDA ascending, take top 20
```

## C.2 Financials (banks/NBFCs) value screen

```
P/B                    < 1.5  (PSU)  /  < 2.5 (private)
ROA                    > 1.0%
ROE                    > 12%
Gross NPA trend        stable or falling
Capital adequacy       > regulatory floor
→ rank by P/B ascending
```

## C.3 Momentum screen

```
12-1 total return      > 0
Price                  > 200-DMA
Price / 52w-high       > 0.85
Avg daily turnover     > ₹10 cr
Exclude                < 12 months listed, circuit-stuck
→ rank by 12-1 return descending, take top 20, monthly
```

## C.4 Multi-factor screen

```
z_value      = z(earnings yield) + z(book-to-price)
z_momentum   = z(12-1 return)
z_quality    = z(ROE 5y) − z(Net Debt/EBITDA; ex-banks/NBFCs) − z(gross-margin volatility)
z_lowvol     = −z(1y realized vol)
composite    = 0.30*z_value + 0.30*z_momentum + 0.25*z_quality + 0.15*z_lowvol
→ rank composite descending, top 25–30, quarterly, sector cap 20%
```


# Appendix D — Glossary

- **Alpha** — return above what the market (beta) explains.
- **Beta** — sensitivity to the market index.
- **Circuit filter** — NSE price band (2/5/10/20%) halting trades beyond the limit.
- **Consolidated financials** — includes all subsidiaries; the correct view for groups.
- **Drawdown** — peak-to-trough decline in portfolio value.
- **EBITDA** — earnings before interest, tax, depreciation, and amortization.
- **EV** — enterprise value = market cap + debt − cash.
- **FII / DII** — foreign / domestic institutional investors.
- **Impact cost** — the price penalty for trading a stock, worst for illiquid names.
- **LTCG / STCG** — long / short-term capital gains (12-month threshold; 12.5% / 20% for listed equity; rates as of 2026 — check the current Finance Act).
- **Margin of safety** — the discount between price and intrinsic value.
- **Momentum crash** — violent underperformance of recent winners vs recent losers when the market rebounds after a sharp decline.
- **Pledge** — promoter shares pledged as loan collateral; high pledge = risk flag.
- **Relative strength** — a stock's return vs its benchmark.
- **Sharpe ratio** — excess return per unit of volatility.
- **STT** — securities transaction tax, levied on buys/sells.
- **Survivorship bias** — overestimating returns by only testing stocks that still exist.
- **Walk-forward** — rolling out-of-sample validation to prevent overfitting.
- **z-score** — a value standardized to a distribution's mean and standard deviation.

---

> **Disclaimer:** This document is for educational purposes only and does not constitute investment advice, a recommendation, or an offer to buy or sell any security. Past performance of any factor or strategy does not guarantee future results. Indian equity investing involves risk, including loss of principal. Please consult a SEBI-registered investment adviser before making investment decisions.
