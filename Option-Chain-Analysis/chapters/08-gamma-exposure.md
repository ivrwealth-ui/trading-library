# 8. Gamma Exposure (GEX)

## The reflexivity model

**Gamma exposure (GEX)** is the most discussed positioning model in modern options analysis — and the most abused. It measures the **net gamma of the dealer book**, and its sign tells you whether dealer hedging is **stabilising** or **amplifying** market moves. It is, in a precise sense, the chain's answer to "how *reflexive* is this market right now?"

## The building block: option gamma

Gamma (from *The Complete Options Trader*) is the rate of change of delta — the option's *convexity*. It is:

- **Positive** for option *buyers* (both calls and puts) — their delta grows in the direction of a move.
- **Negative** for option *sellers* — their delta grows *against* them as the market moves.
- **Highest at the money** and near expiry — where uncertainty is most concentrated.

The chain's gamma, combined with OI, tells you how *much* convexity is embedded in the market, and on which side.

## The formula

Under the same dealer-short convention as DEX (dealers are net writers), the dealer's gamma on each contract is the *negative* of the holder's:

GEX at strike K = **− OI(K) × Γ(K) × lot × spot² × 0.01**

Net GEX = **Σₖ [ − OI_call(K) × Γ_call(K) − OI_put(K) × Γ_put(K) ] × lot × spot² × 0.01**

The result is a single number — the total dealer gamma, in **rupees per 1% move of the underlying**. (The "spot² × 0.01" term turns "gamma per point" into "rupees of hedging flow per 1% move": a 1% move is 0.01 × spot points, which changes delta by Γ × 0.01 × spot, and each unit of delta is worth spot rupees.)

## Reading the sign: the two regimes

The sign of GEX is the whole story, because it determines *how dealers hedge* — and dealer hedging is a real, self-reinforcing force:

### GEX > 0 (dealers net *long* gamma)

When dealers are long gamma, they hedge **counter-cyclically**: they **buy when the market falls and sell when it rises** (to stay delta-neutral). This behaviour **dampens** moves — the market is *stabilised*, volatility is suppressed, and price tends to **pin** around heavy-OI strikes.

**Signature: low realised volatility, range-bound trading, "quiet" markets.**

### GEX < 0 (dealers net *short* gamma)

When dealers are short gamma, they hedge **pro-cyclically**: they **buy when the market rises and sell when it falls** (chasing the move). This behaviour **amplifies** moves — every move is *reinforced* by dealer hedging, and volatility can expand rapidly, especially if price moves into a region of concentrated negative gamma.

**Signature: high/rising realised volatility, "violent" markets, and the potential for sharp, self-reinforcing moves.**

## The "gamma flip" level

A refinement that makes GEX *spatially* useful: plot **GEX against strike** (or against the underlying's price), and find where it **flips sign**. That level — where dealer hedging switches from dampening to amplifying (or vice versa) — is a meaningful zone:

- Price *above* the flip (in positive-GEX territory) is stabilised; price falling *below* it into negative-GEX territory can accelerate.
- The flip level often acts as a **magnet or a cliff** — a level the market is drawn toward, and where behaviour can change abruptly.

The flip level is, in effect, the chain's estimate of "where the market's character changes."

## How GEX is used

1. **As a regime indicator** — is the market currently in a dampening (GEX > 0) or amplifying (GEX < 0) regime? This frames *how* to trade (e.g., fade moves in a dampening regime, respect trends in an amplifying regime).
2. **As a volatility forecast** — negative GEX is associated with *rising* realised volatility; positive GEX with *suppressed* volatility.
3. **Via the flip level** — as a support/resistance reference (the level where behaviour changes).
4. **Via its *change*** — a sharp drop in GEX (dealers flipping from long to short gamma) is often a warning of an impending volatility expansion.

## The honest caveats

1. **The sign rests on the dealer-short assumption** (Chapter 6, Rule 4) — the same caveat as DEX, and equally important here. In a buyer-dominated OI regime, the sign flips.
2. **GEX is not a crystal ball.** It describes the *reflexivity* of the current positioning; it does not predict the direction of the next move, and it is most informative at *extreme* levels and at *flips*, not in the middle.
3. **It is point-in-time sensitive.** GEX uses *live* gamma and *end-of-day* OI; mixing them (a backtest using today's OI for an intraday signal) is look-ahead (Chapter 6, Rule 2).
4. **It is one input.** GEX is powerful precisely *in combination* — with DEX (direction), PCR (sentiment), and skew (fear) — into a composite model (Chapter 13).

## Summary

- GEX = net dealer gamma, in ₹ per 1% move: −Σ (OI × Γ) × lot × spot² × 0.01.
- GEX > 0: dealers long gamma → counter-cyclical hedging → dampening, pinning, low vol.
- GEX < 0: dealers short gamma → pro-cyclical hedging → amplification, high vol.
- The "gamma flip" level is where market behaviour changes — a magnet or a cliff.
- Sign rests on the dealer-short assumption; it is a reflexivity/regime read, not a direction forecast.

Next: the implied probability distribution.
