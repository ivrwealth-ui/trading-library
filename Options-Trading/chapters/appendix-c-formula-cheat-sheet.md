# Appendix C. Formula & Cheat Sheet

## The core identity

**Premium = Intrinsic value + Time value**

- Call intrinsic value = max(S − K, 0)
- Put intrinsic value = max(K − S, 0)

## Breakevens (per unit, at expiry)

| Position | Breakeven |
|----------|-----------|
| Long call / short call | K + premium |
| Long put / short put | K − premium |
| Bull call spread | Lower strike + net debit |
| Bear put spread | Higher strike − net debit |
| Bull put spread (credit) | Short strike − net credit |
| Bear call spread (credit) | Short strike + net credit |
| Long straddle | K ± total premium |
| Long strangle | Lower strike − total premium; higher strike + total premium |

## The Greeks (first order)

| Greek | Meaning | Sign (long / short) |
|-------|---------|---------------------|
| Delta (call) | Δ price per 1 pt of underlying | + / − |
| Delta (put) | Δ price per 1 pt of underlying | − / + |
| Gamma | Δ delta per 1 pt of underlying | + / − |
| Theta | Δ price per 1 day (decay) | − / + |
| Vega | Δ price per 1 pt of IV | + / − |
| Rho (call) | Δ price per 1 pt of rate | + / − |
| Rho (put) | Δ price per 1 pt of rate | − / + |

## Black-Scholes (European, no dividends)

C = S·N(d₁) − K·e^(−rT)·N(d₂)

P = K·e^(−rT)·N(−d₂) − S·N(−d₁)

d₁ = [ ln(S/K) + (r + σ²/2)T ] / (σ√T)

d₂ = d₁ − σ√T

where N(·) is the cumulative standard normal distribution. Key outputs: **N(d₁) = call delta**, **N(d₂) = risk-neutral P(ITM)**.

## The √time rule

Expected 1σ move ≈ Price × σ × √(T / 252)

- σ = annualised volatility (decimal), T = trading days to expiry, 252 = trading days/year.

## Volatility context

- **IV Rank** = (IV − IV_min) / (IV_max − IV_min)
- **IV Percentile** = % of past observations below current IV
- 0–25 = cheap (favour buying vol); 75–100 = expensive (favour selling vol) — historical tendency, not a promise.

## Position sizing

Position size = (Account × Risk % per trade) / (Max loss per unit)

- Standard risk % per trade: **1–2%**.
- For defined-risk positions, max loss per unit is known at entry.

## Rules of thumb worth memorising

1. Buyers are long gamma and long vega, short theta; sellers are the mirror.
2. ATM options have the highest gamma, theta, and vega.
3. Time value is maximum at ATM and zero at expiry; decay accelerates near expiry.
4. OTM puts are structurally richer than OTM calls (skew) in equity/index markets.
5. IV spikes on shocks and crushes after scheduled events.
6. Right direction is not enough: the move must exceed what IV prices, before expiry.
7. If you cannot draw the payoff diagram, you do not understand the position.
8. Defined-risk ≠ safe; size for the tail, never for the expectation.
