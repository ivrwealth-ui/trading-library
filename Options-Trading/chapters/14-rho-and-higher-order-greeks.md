# 14. Rho and the Higher-Order Greeks

## The Greek alphabet, completed

The first-order Greeks — delta, theta, vega — cover the three inputs that dominate most positions: the underlying, time, and volatility. Two more first-order Greeks complete the set, and a family of *second-order* Greeks describes how the first-order ones change. None of them is as central as delta/theta/vega, but a complete trader recognises them.

## Rho: the interest-rate Greek

**Rho (ρ)** measures the change in an option's price for a **one-percentage-point change in the risk-free interest rate**.

- A **call** has positive rho: higher rates make calls worth more (a call lets you defer the cash outlay for the underlying, and you earn interest in the meantime).
- A **put** has negative rho: higher rates make puts worth less.

Rho is positive for long calls and short puts; negative for long puts and short calls.

**In practice, rho is the least important Greek for the short-dated trader.** For options a few weeks from expiry, a 1% rate move changes the price by an almost imperceptible amount. Rho matters only for **long-dated options** (months to years, e.g., LEAPS-style contracts) and for institutional rate-sensitivity management. Most retail traders can safely ignore rho day-to-day — but should know it exists so that a long-dated call's behaviour is not a mystery.

## Second-order Greeks: how the Greeks themselves change

The first-order Greeks are not constants. As the market, time, and volatility move, delta, theta, and vega change — and the second-order Greeks measure those changes.

### Gamma (Γ) — already met

Gamma is the rate of change of delta. It is the most important second-order Greek and was covered fully in Chapter 11.

### Vanna — how delta changes with volatility

**Vanna** measures how much **delta** changes when **implied volatility** changes. It tells you whether a volatility move will also change your directional exposure.

- A position with positive vanna becomes *more* directional (delta moves further from zero) as volatility rises.
- This matters for hedgers: a delta-neutral position can quietly drift out of neutral as volatility shifts, because vanna changes delta without the underlying moving.

### Vomma (volga) — how vega changes with volatility

**Vomma** (also *volga*) measures how much **vega** changes when implied volatility changes — the *curvature* of the position's vol exposure.

- A position with positive vomma gains vega as volatility rises (a "convex" vol position — like owning OTM options, whose vega grows in a vol spike).
- A position with negative vomma loses vega as volatility rises.

Vomma explains why **OTM options** can be such powerful tail hedges: not only are you long vega, but your vega *increases* as a crash drives volatility higher — a self-reinforcing benefit exactly when you need it.

### Charm — how delta changes with time

**Charm** (delta decay) measures how much **delta** changes as **time passes**.

- For an ITM option, delta *drifts toward ±1* as expiry approaches (the option becomes more stock-like).
- For an OTM option, delta *drifts toward 0* (it becomes more worthless).

Charm matters to anyone who maintains a delta-neutral position without rebalancing daily: their hedge slowly goes stale purely from the passage of time.

## Why these matter in practice

The second-order Greeks are the reason a position's *behaviour* can change even when the headline number (the underlying) does not:

- A **short straddle** you hedged to delta-neutral this morning may be meaningfully off-neutral this afternoon if volatility moved (vanna) — even with the index unchanged.
- A **long OTM put** bought as tail insurance becomes *more* protective exactly when a crash hits (positive vanna/vomma) — the "cheap insurance that pays off when you need it" effect.
- A **covered call** you were comfortable with grows more short-gamma as it ages (charm pulls delta toward 1 on the call), subtly changing the risk profile over the holding period.

None of these requires daily computation by a retail trader. The point is *awareness*: when a position "feels different" from what you set up, the second-order Greeks are usually the explanation.

## The sign conventions, at a glance

| Greek | Long option | Short option |
|-------|-------------|--------------|
| Delta (call) | + | − |
| Delta (put) | − | + |
| Gamma | + | − |
| Theta | − | + |
| Vega | + | − |
| Vanna | + | − |
| Vomma | + | − |

Notice the clean pattern: **all the second-order Greeks (gamma, vanna, vomma) are positive for option buyers and negative for sellers.** Buying an option is, universally, a *long-convexity* position; selling one is *short-convexity*. This single observation unifies the whole Greek story.

## Summary

- Rho = interest-rate sensitivity; positive for calls, negative for puts; material only for long-dated options.
- Gamma = d(delta)/d(underlying); vanna = d(delta)/d(vol); charm = d(delta)/d(time); vomma = d(vega)/d(vol).
- Buyers are long all second-order Greeks; sellers are short them.
- The second-order Greeks explain why positions "drift" from their intended exposure over time and through vol moves.

Next: the model that ties all the Greeks together — Black-Scholes.
