# 11. Delta and Gamma

## Delta: the option's speed

**Delta (Δ)** measures how much an option's price changes for a **one-point move in the underlying**. It is the first and most-used Greek.

Formally, delta is the partial derivative of the option price with respect to the underlying price. Informally, it is three things at once:

1. **A rate of change** — how sensitive the option is to the underlying.
2. **An approximate probability** — the market's estimate of the chance the option finishes in-the-money (a 0.25 delta option is often read as "25% chance of expiring ITM").
3. **An equivalent exposure** — a 0.50 delta option moves like *half* a share (or half a unit of the underlying).

## Delta ranges

- **Calls**: delta runs from **0 to +1**.
  - Deep ITM call → delta ≈ +1 (moves nearly one-for-one with the underlying).
  - ATM call → delta ≈ +0.50.
  - Deep OTM call → delta ≈ 0.
- **Puts**: delta runs from **−1 to 0**.
  - Deep ITM put → delta ≈ −1.
  - ATM put → delta ≈ −0.50.
  - Deep OTM put → delta ≈ 0.

A NIFTY ATM call with delta 0.50 gains about **₹0.50 of premium per 1-point** rise in NIFTY (per unit of the contract). A deep ITM call with delta 0.90 gains about ₹0.90 per point — it behaves almost like holding the index itself.

## Using delta to read your position

- **Directional exposure:** a long call is bullish (positive delta); a long put is bearish (negative delta). Your *net* delta across a position tells you your directional tilt. A portfolio with net delta ≈ 0 is **delta-neutral** — it does not care (much) which way the market moves.
- **Probability shorthand:** delta doubles as a rough "probability ITM." An OTM call with 0.20 delta is a ~20% shot. This is an approximation, not a guarantee, but it is the market's own consensus estimate, and it is invaluable for choosing strikes.
- **Hedging:** to offset the directional risk of a long position, you can short a delta-equivalent amount of the underlying (or of another option). This is the foundation of **delta hedging** and **gamma scalping** (Chapter 26).

## Gamma: the option's acceleration

**Delta is not constant.** As the underlying moves, delta itself changes. **Gamma (Γ)** measures *how much delta changes* for a one-point move in the underlying — the acceleration of the option's price.

Formally, gamma is the second derivative of price with respect to the underlying (the derivative of delta). It is **always positive for option buyers** (long calls and long puts) and **always negative for option sellers**.

- **ATM options have the highest gamma** — delta changes fastest right at the money, where an option is most uncertain about finishing ITM.
- **Deep ITM and deep OTM options have near-zero gamma** — their delta is already settled (≈1 or ≈0) and barely moves.

## Why gamma matters: the long vs. short experience

Gamma explains the *feel* of holding options.

- **Long gamma (you bought options):** as the market moves in your favour, delta grows — you become *more* exposed to the move as it goes your way. Losses decelerate and gains accelerate. This is a pleasant, convex profile.
- **Short gamma (you sold options):** as the market moves against you, delta grows against you — you become *more* exposed the worse it gets. This is why short-option positions can unravel violently: the seller's risk accelerates.

Concretely: a long ATM straddle has positive gamma — a big move in either direction helps *more than proportionally*. A short ATM straddle has negative gamma — a big move in either direction hurts *more than proportionally*. Gamma is the reason the "pennies in front of a steamroller" description of option selling is literally accurate.

## The delta-gamma relationship in one picture

Think of driving a car:

- **Delta** is your speed.
- **Gamma** is your acceleration.

A long option is a car that speeds up as it goes the direction you want. A short option is a car that speeds up in the *wrong* direction. This is why a delta-neutral but gamma-negative position can still lose money fast when the market moves a lot — the neutral delta only holds *at one point*; gamma pulls it away from neutral the moment the market moves.

## Practical rules of thumb

- Want a "stock-like" option? Buy high delta (deep ITM).
- Want cheap leverage with low probability? Buy low delta (deep OTM).
- Want maximum responsiveness? Trade ATM (highest gamma).
- Want to be directionally neutral *and* profit from movement? Be long gamma (own options).
- Want to be directionally neutral *and* profit from stillness? Be short gamma (sell options) — and understand the tail risk.

## Summary

- Delta = rate of change of price w.r.t. underlying; also ≈ probability ITM and an exposure measure.
- Calls: 0 to +1. Puts: −1 to 0.
- Gamma = rate of change of delta; positive for buyers, negative for sellers; peaked at ATM.
- Long gamma accelerates gains; short gamma accelerates losses.
- Net delta tells you your directional tilt; delta-neutrality is the basis of hedging and scalping.

Next: theta — the cost of the clock.
