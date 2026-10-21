# 7. Delta Exposure and Dealer Positioning

## The directional tilt of the option book

The first model built directly from the chain's Greeks is **delta exposure (DEX)**: the *net directional exposure* of all outstanding options, attributed to the dealers (market-makers) who are their counterparties. It answers a precise question: *if the underlying moves, in which direction — and with how much force — will dealers be forced to trade to stay hedged?*

## The building block: option delta

Recall (from *The Complete Options Trader*) that every option has a **delta** — the rate of change of its price with respect to the underlying:

- Calls: delta runs **0 to +1** (ITM calls approach +1).
- Puts: delta runs **−1 to 0** (ITM puts approach −1).

A long call is *long* the market; a long put is *short* the market. The chain's OI, combined with these deltas, tells you the *net* directional position embedded in the option market.

## The dealer-short convention

OI does not record who is long and who is short. The standard model makes an assumption (Chapter 6, Rule 4): **dealers are the *net sellers* of options** — they write options to provide liquidity, and the OI represents, in aggregate, *dealer short* positions.

Under this convention, the dealer's delta on each contract is the *negative* of the holder's:

Dealer delta of a call at strike K = **− OI(K) × Δ_call(K)**

Dealer delta of a put at strike K = **− OI(K) × Δ_put(K)**  (and since Δ_put is negative, this is *positive*)

Summed over all strikes, and multiplied by the contract notional (spot × lot size), we get the **net delta exposure**:

DEX = **− Σₖ [ OI_call(K) × Δ_call(K) + OI_put(K) × Δ_put(K) ] × (spot × lot)**

The result is a single number, in rupees of notional: the market's *net directional exposure* from the dealers' perspective.

## Reading DEX

The sign and size of DEX describe the **directional tilt** of the dealer book — and, therefore, the *flows* that would result if price moves:

- **DEX strongly negative** (dealers net *short* delta — i.e., the market is net long calls): to stay neutral, dealers hold a **long** hedge in the underlying. If the market rises, their short calls gain delta and they must **buy** more of the underlying — adding *upward* fuel to the rally. If it falls, they sell (de-hedge), adding downward fuel.
- **DEX strongly positive** (dealers net *long* delta — the market is net long puts / short the market): dealers hold a **short** hedge in the underlying. Because they are short those puts, they are short gamma too: if the market falls, the puts gain delta and dealers must **sell** more — adding *downward* fuel to the decline; if it rises, they buy back part of their hedge, adding upward fuel.

In both cases DEX tells you the *size and direction* of the dealers' hedge; *how* that hedge changes as price moves — and whether the hedging amplifies or dampens the move — is gamma, the subject of Chapter 8.

More useful than the raw sign is the **change** in DEX: a sharp *shift* in delta exposure (e.g., from net short to net long) marks a change in the market's directional conviction, and a potential inflection point.

## DEX vs. GEX: two different questions

It is worth separating the two, because they are often confused:

- **DEX (delta exposure)** answers: *what is the market's net directional tilt, and therefore the direction of hedging flows?* It is a **first-order** measure — about *direction*.
- **GEX (gamma exposure, next chapter)** answers: *how does that tilt change as the market moves, and does dealer hedging amplify or dampen moves?* It is a **second-order** measure — about *reflexivity*.

DEX is the "position" read; GEX is the "how it behaves" read. Both are built from the same OI × Greek × notional machinery; they just multiply by delta (DEX) or gamma (GEX).

## A worked example (conceptual)

Consider a simplified NIFTY chain where the dominant feature is **heavy call OI above spot** (investors have bought calls; dealers are short those calls):

- Dealer delta from the short calls is **negative and large** (dealers are short the market via short calls).
- DEX is therefore **strongly negative**.
- Interpretation: the option book is *tilted bullish* (net long calls), and if NIFTY rallies, dealers will be **forced to buy** to hedge — which can *accelerate* the rally (the "short gamma/delta squeeze" dynamic, quantified in the next chapter).

This is the first taste of why positioning matters: the chain does not just *reflect* the market's view; it contains **latent buying or selling pressure** that can move the market when price reaches the relevant levels.

## The honest caveats

1. **The dealer-short assumption is a model, not a fact** (Chapter 6, Rule 4). If the OI is actually *buyer*-dominated (a retail buying frenzy), the sign flips. Treat the sign cautiously; the *structure* (where the exposure concentrates) is more robust.
2. **DEX is a snapshot, not a forecast.** It describes the *current* tilt; it does not, by itself, predict the direction of the next move — it predicts the direction of *hedging flows* *if* the market moves.
3. **It is one input.** DEX is most useful *combined* with GEX (next chapter) and the sentiment signals (PCR, skew) into a composite view (Chapter 13).

## Summary

- DEX = the net directional exposure of the option book, from the dealers' perspective, in ₹ notional.
- Built as −Σ (OI × delta) × spot × lot, over all strikes (dealer-short convention).
- Negative DEX = dealers short delta (market net long) → forced buying on rallies.
- DEX is first-order (direction); GEX is second-order (reflexivity).
- It is a snapshot of latent hedging pressure, not a forecast — and the sign rests on the dealer-short assumption.

Next: gamma exposure (GEX) — the reflexivity model.
