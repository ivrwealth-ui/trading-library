# 18. The Long Call and the Long Put

## The two building blocks of directional trading

The long call and the long put are the simplest strategies in the playbook, and the foundation of every other position. They are the pure expression of the buyer's side of the contract: **defined risk, open-ended (or large) reward, and a race against time.**

This chapter gives each a complete profile. Every subsequent strategy chapter follows the same format, so a common template is worth establishing here.

## The template

For each strategy we report the same facts:

- **Structure** — what you buy or sell.
- **Market view** — what belief the position expresses.
- **Maximum profit** — the best possible outcome.
- **Maximum loss** — the worst possible outcome.
- **Breakeven** — the underlying level(s) at expiry where P&L is zero.
- **Greeks profile** — the net delta/gamma/theta/vega character.
- **When it fits** — the environment the position historically aligns with.

## The long call

- **Structure:** buy a call at strike K for premium C.
- **Market view:** bullish — the underlying will rise *above* the strike by more than the premium before expiry.
- **Maximum profit:** unlimited (the underlying can rise without bound).
- **Maximum loss:** the premium paid, C (× lot size). Occurs if the underlying is at or below K at expiry.
- **Breakeven:** K + C.
- **Greeks:** long delta (≈ N(d₁)), long gamma, long vega, short theta.
- **When it fits:** when you expect a *meaningful upward move* and want defined-risk leverage; historically more favourable when implied volatility is *low* (you pay less) and the expected move exceeds what IV prices in.

### Worked example (per unit, before costs)

NIFTY at 25,000. Buy the 25,200 call for ₹80.

- Breakeven = 25,200 + 80 = **25,280**.
- NIFTY at 25,500 at expiry: intrinsic value = 300; profit = 300 − 80 = **₹220**.
- NIFTY at 25,100 at expiry: worthless; loss = **₹80**.

The appeal is the asymmetry: ₹80 of risk for theoretically unlimited reward. The cost is that the market must rise *enough* (past 25,280) for the trade to pay, and it must do so *before time runs out*.

## The long put

- **Structure:** buy a put at strike K for premium P.
- **Market view:** bearish — the underlying will fall *below* the strike by more than the premium before expiry. (Or: protective — hedging an existing long position, Chapter 24.)
- **Maximum profit:** K − P (attained if the underlying falls to zero).
- **Maximum loss:** the premium paid, P.
- **Breakeven:** K − P.
- **Greeks:** short delta, long gamma, long vega, short theta.
- **When it fits:** when you expect a *meaningful decline* (or want downside insurance); historically more favourable when IV is low, and doubly useful when skew is steep — though steep skew means the put is expensive.

### Worked example

NIFTY at 25,000. Buy the 24,800 put for ₹70.

- Breakeven = 24,800 − 70 = **24,730**.
- NIFTY at 24,500 at expiry: intrinsic value = 300; profit = 300 − 70 = **₹230**.
- NIFTY at 25,000 at expiry: worthless; loss = **₹70**.

## The shared truth of long options

Both long positions are **long gamma and long vega**: they accelerate in your favour as the market moves, and they gain from a volatility rise. They are also both **short theta**: they bleed value every day. The trade is always the same bargain — *paying a known, limited cost for a convex payoff that needs movement to materialise.*

This is why the *timing* and *magnitude* of the view matter as much as its *direction*:

- Right direction + small move = loss (premium not recovered).
- Right direction + move arrives late = reduced profit (theta erosion).
- Right direction + move *larger than priced* = profit.
- Right direction + IV already rich = possible loss even on a correct move (vol crush).

## Choosing the strike

The strike choice expresses a trade-off between probability and payoff:

- **Deep ITM** (high delta): behaves like the underlying; high win probability, low leverage, most intrinsic value. The most "stock-like."
- **ATM** (delta ≈ 0.5): balanced; highest gamma and theta; the classic speculative middle.
- **Deep OTM** (low delta): cheap, low probability, maximum leverage; a "lottery ticket" that wins big when it wins and usually expires worthless.

There is no universally correct choice — the strike is where your view about *probability versus magnitude* becomes concrete. A trader confident in a large move buys OTM for leverage; a trader wanting a high-probability directional proxy buys ITM.

## Summary

- Long call: bullish, unlimited profit, risk = premium, breakeven = strike + premium.
- Long put: bearish (or protective), profit capped at strike, risk = premium, breakeven = strike − premium.
- Both are long gamma/vega and short theta — the "pay for a convex payoff" trade.
- Strike choice encodes the probability-versus-payoff trade-off.
- Right direction is not enough: the move must exceed what's priced, before expiry.

Next: the covered call and the cash-secured put — the two "income" foundations.
