# 15. The Black-Scholes Model

## The equation that built an industry

Every Greek in the last five chapters descends from a single mathematical model: **Black-Scholes** (more properly Black–Scholes–Merton), published in 1973. It is not the final word on option pricing, and it is not perfectly accurate — but it is the *language* in which options are quoted, discussed, and hedged everywhere in the world. You cannot be fluent in options without knowing what it says and, just as importantly, what it assumes.

## What the model does

Black-Scholes answers one question: **what is the fair price of a European call option**, given the six inputs of Chapter 10 — underlying price S, strike K, time to expiry T, volatility σ, risk-free rate r (and, for completeness, dividend yield q)?

The answer is the familiar closed-form:

**Call price** C = S·e^(−qT)·N(d₁) − K·e^(−rT)·N(d₂)

**Put price** P = K·e^(−rT)·N(−d₂) − S·e^(−qT)·N(−d₁)

where

d₁ = [ ln(S/K) + (r − q + σ²/2)·T ] / (σ√T)

d₂ = d₁ − σ√T

and **N(·)** is the cumulative standard normal distribution — the probability that a normally distributed variable falls below a given value.

You do not need to memorise the algebra to trade. What you *should* take away is the *structure*:

1. The formula is **deterministic**: six inputs in, one price out. There is no judgment inside the formula — all judgment is pushed into the inputs, chiefly **σ**.
2. **N(d₁)** and **N(d₂)** turn out to *be* the Greeks: N(d₁) is the call's delta, and N(d₂) is the risk-neutral probability that the option finishes ITM. The Greeks are not separate ideas bolted onto the model — they fall out of it as derivatives.

## The one big insight: risk-neutral pricing

Black-Scholes rests on a profound idea: the price of an option is **the cost of a self-financing hedge that replicates it**. The model shows you can construct a portfolio of the underlying and cash that *exactly* reproduces the option's payoff — and the option's fair price is simply the cost of building that replicating portfolio.

This is why delta hedging works at all: the option's delta tells you exactly how much underlying to hold so that, rebalanced continuously, the hedged portfolio is riskless — and therefore must earn the risk-free rate. The model prices the option *from the hedge*, not from anyone's opinion about direction. Direction (the expected return of the underlying) drops out of the formula entirely; only volatility survives.

This is the deepest reason options are "about volatility": under the model, the *drift* of the underlying is irrelevant — only its *volatility* matters for pricing.

## The assumptions, and where reality disagrees

The model's elegance comes from assumptions that are only approximately true. Knowing them is knowing the model's limits:

1. **Log-normal returns with constant volatility.** The model assumes the underlying follows a random walk with *constant* σ. Reality: volatility changes over time and returns have "fat tails" (big moves happen more often than the normal distribution predicts). → *This is why the volatility smile exists* (Chapter 17).
2. **Continuous trading and frictionless markets.** The hedge must be rebalanced continuously, with no transaction costs. Reality: you rebalance discretely and pay costs. → *This is why perfect hedging is impossible in practice* (gamma risk remains).
3. **European exercise.** The model prices options exercisable only at expiry. American-style early exercise (relevant for stock options) is not handled by the plain formula. → *Most Indian index options are European, so this is fine there.*
4. **No dividends (in the simplest form), known constant rates.** Reality: dividends and changing rates must be added (the q and r terms).
5. **No jumps.** The underlying can move continuously. Reality: prices gap overnight and on news. → *Gap risk is unhedgeable and is why short options are dangerous over events.*

None of these invalidates the model for everyday use; they define *where* it needs correction, and the market itself supplies the correction — by trading options at prices that imply a different σ at every strike and expiry (the volatility surface, Chapter 17).

## From Black-Scholes to the Greeks

Because the formula is a smooth function of its inputs, its derivatives *are* the Greeks:

- **Delta** = ∂C/∂S = N(d₁) (call).
- **Gamma** = ∂²C/∂S² = N′(d₁) / (S·σ·√T).
- **Vega** = ∂C/∂σ = S·√T·N′(d₁) (per unit vol).
- **Theta** = ∂C/∂T (negative for buyers).
- **Rho** = ∂C/∂r.

Notice the recurring **√T** in vega and the **1/√T** in gamma: longer time raises vega and lowers gamma, the twin consequences of time spreading uncertainty out. And N′(d₁) — the bell curve — explains why gamma and vega both peak at the money and why deep-ITM/OTM options have little of either.

## The model in daily practice

Almost nobody calculates Black-Scholes by hand. Brokers and platforms compute it continuously and display the result as the **Greeks** and the **implied volatility**. Your job is to *interpret* those numbers, not to derive them. What the model buys you is a coherent mental framework:

- An option's price is a function of S, K, T, σ, r, q.
- The Greeks are its sensitivities.
- The only uncertain input — σ — is recovered by inverting the model: plug in the market price, solve for σ, and you have **implied volatility** (next chapter).

## Summary

- Black-Scholes prices a European option from six inputs; all judgment sits in σ.
- The formula's derivatives are the Greeks; N(d₁) = call delta, N(d₂) = risk-neutral P(ITM).
- The key insight is risk-neutral pricing: the option's value is the cost of its replicating hedge.
- Its assumptions (constant vol, no jumps, continuous trading) are why real markets show a volatility smile and why hedging is imperfect.
- You interpret the model's outputs; the platform does the arithmetic.

Next: the number the model is inverted to produce — implied volatility.
