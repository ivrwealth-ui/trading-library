# Appendix — Formula Reference and Signal Table

## The formulas, in one place

**Put-Call Ratio (OI-based):** PCR = Σ(put OI) ÷ Σ(call OI)

**Max pain:** the strike K that minimises

Total pain(K) = Σᵢ [ OI_call(Kᵢ)·max(K − Kᵢ, 0) + OI_put(Kᵢ)·max(Kᵢ − K, 0) ]

**Risk reversal (skew):** 25Δ risk reversal = IV(25Δ call) − IV(25Δ put)

**Delta exposure (DEX), dealer-short convention:**

DEX = − Σₖ [ OI_call(K)·Δ_call(K) + OI_put(K)·Δ_put(K) ] × (spot × lot)

**Gamma exposure (GEX), dealer-short convention:**

GEX = − Σₖ [ OI_call(K)·Γ_call(K) + OI_put(K)·Γ_put(K) ] × lot × spot² × 0.01   (in ₹ per 1% move)

**Implied probability density (Breeden–Litzenberger):**

f(K) ≈ e^(rT) × [ C(K − ΔK) − 2·C(K) + C(K + ΔK) ] / (ΔK)²

**Variance risk premium:** VRP = Implied volatility − Realised volatility (quoted here in volatility terms)

**Expected move (1σ):**

- ATM straddle: Expected move ≈ C(ATM) + P(ATM) (the straddle ≈ 0.8σ, so 1σ ≈ 1.25 × straddle)
- From IV: Expected move ≈ S × IV × √(T / 252)

## The signals, at a glance

| Signal | Measures | Best read as |
|--------|----------|--------------|
| OI + price change | Flow (longs/shorts entering) | Four-quadrant read |
| OI walls | Where capital sits | Support / resistance |
| PCR (percentile) | Bearish/bullish positioning | Trend at mid-range, contrarian at extremes |
| Risk reversal | Fear / tail demand | Steepening = fear building |
| Term structure | When uncertainty is | Backwardation = event near |
| Max pain | Expiry gravity | Expiry-day reference |
| DEX | Directional tilt | Direction of hedging flows |
| GEX | Reflexivity / regime | Dampening vs. amplifying |
| Implied distribution | Full forecast | Probability of ranges, tails, levels |
| VRP | Insurance premium | Cheap vs. expensive vol |
| Expected move | Priced-in move size | Benchmark for every view |
| Implied S/R | Positioned levels | OI + gamma walls + distribution kinks |

## The universal rules

1. **Point-in-time or nothing** — OI is end-of-day, IV is live, strikes change.
2. **State the dealer-short assumption** — the positioning models' sign rests on it.
3. **Normalise to history** — read percentiles, not absolutes.
4. **Know each model's home regime** — max pain and walls are range-bound tools; GEX and PCR matter at extremes.
5. **Combine, don't cherry-pick** — a composite read, honestly assembled, beats any single signal.
6. **A map, not a prophecy** — the chain shows positioning and behaviour, not the next price.
