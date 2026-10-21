# 9. The Implied Probability Distribution

## Recovering the market's forecast, in full

Every model so far reduced the chain to a *single number* (a ratio, a level, a net exposure). The **implied probability distribution** goes the other way: it recovers, from the entire chain, the market's **full probability distribution of where the underlying will be at expiry** — not a point forecast, but the whole curve of probabilities.

This is the deepest read the chain offers: it is, literally, the market's *complete* view of the future, extracted from option prices.

## The idea: options price probabilities

An option's price is, at heart, the market's answer to "what is the probability-weighted value of the payoff?" Reversed, this means: **if you know all the option prices, you can recover the probability distribution they imply.** The chain of prices *encodes* a distribution; the model just *decodes* it.

The result is the **risk-neutral density** — the probability distribution such that, if you discount expected payoffs at the risk-free rate, you reproduce all the option prices. It is called "risk-neutral" because it is the distribution *implied by prices*, not necessarily the *true* distribution (the two differ by the risk premium — Chapter 10's subject).

## The construction: butterflies and the second derivative

The cleanest way to see the construction is through **butterflies** (from *The Complete Options Trader*). A butterfly spread — buy a call at K−ΔK, sell two at K, buy one at K+ΔK — pays off **only if the underlying expires near K**, and its payoff is a narrow spike around K.

The price of that butterfly is therefore the market's price for the event "the underlying lands near K." Divide by the spike's width, and you get the **probability density** at K.

Formally (the Breeden–Litzenberger result), the risk-neutral density f(K) is the **second derivative of the call price with respect to strike**:

f(K) ≈ e^(rT) × [ C(K − ΔK) − 2·C(K) + C(K + ΔK) ] / (ΔK)²

where C(K) is the call price at strike K, and ΔK is the strike spacing. The numerator is exactly the butterfly price (one call at K−ΔK, minus two at K, plus one at K+ΔK); dividing by (ΔK)² (and the discount factor) converts a "price of a spike of width ΔK" into a "probability density."

## What the distribution shows

The recovered curve is a rich object, and each of its *features* is a signal:

1. **The mode / centre** — where the market thinks price is *most likely* to land (its best single guess). Often near spot, but not always.
2. **The width** — the market's uncertainty: a wide, flat distribution = a big expected range; a narrow, peaked one = a confident, range-bound view.
3. **The skew (asymmetry)** — a distribution with a fat *left* tail (downside) and a thin right tail is the visual form of the *skew* from Chapter 4: the market thinks a large *fall* is more likely than a large *rise*.
4. **The tails** — the probability of *extreme* moves. Fat tails = the market is pricing crash risk; thin tails = it is pricing calm.
5. **Kinks and bumps** — the distribution is often *not* smooth; a bump at a particular level corresponds to a strike with unusual demand (an OI wall, a psychological level) — the chain's fingerprint of a *specific* level the market is watching.

## How it is used

The implied distribution is the single most versatile object in this book, because it answers, directly, the questions every other model gestures at:

- **"What is the probability NIFTY closes above 25,000?"** → integrate the density above 25,000.
- **"What is the market pricing as a 1-in-10 (or 1-in-20) move?"** → read the 5th/95th (or 2.5th/97.5th) percentiles of the distribution.
- **"Is the market pricing a crash?"** → look at the left tail's weight.
- **"Where are the levels the market is watching?"** → look at the kinks and bumps.

It is, in effect, the **"expected move" (Chapter 11) generalised from a single number to the entire curve.**

## The honest caveats

1. **It is risk-neutral, not the true distribution.** The implied distribution is *risk-adjusted*: because investors pay up for crash protection (the risk premium), the left tail is *fatter* in the implied distribution than in the market's *true* (unobservable) belief. The implied distribution *overstates* the probability of extreme moves — which is precisely the variance risk premium of the next chapter.
2. **It is noisy.** The second derivative amplifies noise: small pricing errors in individual options become large wiggles in the density. The curve must be *smoothed* (interpolated) before it is readable, and the smoothing is a modelling choice.
3. **It is only as good as the chain.** Thin OI, wide spreads, and missing strikes in the wings make the tail of the implied distribution unreliable (Chapter 14).

## Summary

- The chain of option prices *encodes* a full probability distribution; the model decodes it.
- The density is the second derivative of call price w.r.t. strike (the butterfly / Breeden–Litzenberger result).
- Features: mode (best guess), width (uncertainty), skew (asymmetry), tails (crash risk), kinks (watched levels).
- It answers "probability of closing above X", "the 1-in-10 move", "is a crash priced?", "where are the watched levels?"
- It is risk-neutral (overstates tails) and noisy (needs smoothing) — and only as good as the chain.

Next: the variance risk premium — what the distribution's bias is worth.
