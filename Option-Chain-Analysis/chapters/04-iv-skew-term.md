# 4. Implied Volatility: Skew and Term Structure

## The chain's most information-dense field

The **implied volatility (IV)** at each strike is the single most information-dense number in the chain: it is the volatility that makes the option's *market price* equal its model price (Black-Scholes, from *The Complete Options Trader*). Because it is a *standardised* price of uncertainty, IV can be compared across strikes and expiries — and the *pattern* of IV across the chain is a rich signal in its own right. This chapter covers the two dimensions of that pattern: **skew** and **term structure**.

## Skew: IV across strikes (one expiry)

Plot IV against strike for a single expiry, and you do *not* get a flat line. In equity/index markets, you get a **skew** — a curve, typically shaped like a *smile* or *smirk*:

- **OTM puts carry higher IV** than equidistant OTM calls. Downside protection is *expensive*; upside calls are comparatively *cheap*.

**Why:** investors systematically buy downside protection (puts), bidding up their price — and therefore their IV. The market prices crashes as more likely than a normal (lognormal) distribution would suggest: the "fat left tail." This is not an inefficiency to be arbitraged away; it is a *persistent structural feature* of the market, reflecting the real, rational demand for crash protection.

### A quantitative skew measure: the risk reversal

The standard way to *measure* skew in one number is the **risk reversal** — the difference between the IV of an OTM call and an OTM put at a fixed delta (commonly 25-delta):

Risk reversal (25Δ) = IV(25Δ call) − IV(25Δ put)

- **Negative risk reversal** (puts richer than calls) is the *normal* state in equity/index markets — the market is structurally paying up for downside protection.
- A risk reversal that *steepens* (more negative) = growing fear/hedging demand.
- A risk reversal that *flattens or flips positive* = rising bullishness (calls bidding up).

The risk reversal is a clean, single-number read of *where the fear is concentrated* — and of how it changes over time.

## Term structure: IV across expiries (one strike)

Plot IV against expiry, and you get the **term structure**:

- **Contango (normal, calm):** longer-dated options have *higher* IV than shorter-dated. Uncertainty compounds with time, so more time = more priced-in uncertainty.
- **Backwardation (stress):** near-dated IV *spikes above* far-dated IV. Fear is concentrated in the *immediate* future — the classic signature of an event or a panic.

The term structure tells you *when* the market expects the uncertainty to be:

- **Contango** = "things are calm; uncertainty is spread evenly into the future."
- **Backwardation** = "something is about to happen *now*."

## Why skew and term structure matter for models

Both are inputs to the deeper models in this book, and both are *signals* in their own right:

1. **Skew measures *tail risk demand*.** A steepening skew means the market is paying up for downside protection — a real-time measure of fear, arguably more informative than a headline sentiment survey.
2. **Term structure measures *event concentration*.** Backwardation flags an imminent, priced-in event (a budget, an election, a rate decision) — and it tells you the event is *near*, not far.
3. **Both feed the implied distribution (Chapter 9) and the variance risk premium (Chapter 10).** The surface's shape is the raw material those models consume.

## Reading the surface: a routine

A disciplined IV read of the chain:

1. **Level** — is IV (at the money) high or low relative to its own history (IV rank/percentile, from *The Complete Options Trader*)?
2. **Skew** — what is the risk reversal, and is it steepening (fear building) or flattening (fear easing)?
3. **Term structure** — contango (calm) or backwardation (event near)?

Together these three answer: *is the market cheap or expensive to insure (level), where is the fear concentrated (skew), and when is the uncertainty expected (term structure)?* That is a remarkably complete picture of market expectation, recovered entirely from the chain's IV field.

## Summary

- IV is a standardised price of uncertainty, comparable across strikes and expiries.
- Skew = IV across strikes; equity markets show a skew (smirk) — OTM puts richer than OTM calls.
- The risk reversal (25Δ call IV − 25Δ put IV) measures skew in one number; steepening = growing fear.
- Term structure = IV across expiries; contango = calm, backwardation = event near.
- Level + skew + term structure = a complete picture of market expectation.

Next: max pain and expiry pinning.
