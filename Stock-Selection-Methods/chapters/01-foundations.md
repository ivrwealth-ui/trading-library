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
