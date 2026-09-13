# 16. Implied Volatility and Historical Volatility

## Two ways to measure volatility

"Volatility" is used loosely, but it comes in two distinct flavours, and confusing them causes real mistakes.

- **Historical volatility (HV)** — how much the underlying *has actually* moved in the past. It is computed from realised price changes (typically the annualised standard deviation of daily returns over a trailing window, e.g., 20 or 30 days).
- **Implied volatility (IV)** — how much the market *expects* it to move in the future. It is the volatility number that, plugged into Black-Scholes, makes the model price equal the option's market price.

The mnemonic: **HV looks backward; IV looks forward.**

## Implied volatility: the market's forecast

Because Black-Scholes has six inputs and the option's *price* is observed in the market, you can invert the equation: plug in price, underlying, strike, time, and rate, and solve for the σ that makes it fit. That solved σ is the **implied volatility**.

IV is enormously useful because it is a **standardised price**. Two options with different strikes, expiries, and premiums are hard to compare directly — but their IVs are comparable on a single scale. Saying "NIFTY ATM IV is 14%, while 30-day HV is 11%" immediately tells you options are pricing *more* future movement than the recent past has delivered.

### IV as a fear gauge

IV rises when uncertainty rises — before elections, budgets, rate decisions, and earnings, and during sell-offs. It is why IV is often described as a *fear gauge*: it spikes when investors rush to buy protection. A high IV means options are *expensive*; a low IV means they are *cheap*. "Expensive" and "cheap" here are literal — you are paying more (or less) for the same right.

## The IV vs. HV relationship, and what it means

The gap between IV and HV is a signal:

- **IV > HV** — the market expects more movement than the recent past shows. Common before events and during fear. Options are relatively expensive.
- **IV < HV** — the market expects less movement than recently realised. Options are relatively cheap.
- **IV ≈ HV** — expectations match recent reality.

A trading idea follows directly: historically, **realised volatility tends to be *lower* than implied** on average — the "variance risk premium" that option sellers collect. This is the statistical foundation of income strategies: IV systematically overstates what actually happens, so sellers earn a premium on average — *but* with occasional sharp underpayments when a true shock arrives. (Framed as the book's recurring caveat: conditions where IV is far above HV have historically favoured reduced exposure to option *buying*, but the tail risk to sellers remains.)

## Implied volatility is not the same as direction

A frequent beginner error is reading a high IV as a *bullish or bearish* signal. It is neither. IV measures *expected magnitude*, not *expected direction*. A stock can have high IV because the market expects a large move up, down, or simply a large move whose direction is unknown. Direction is delta; magnitude is vega/IV. Keep them separate.

## Using IV in practice

1. **To judge if options are cheap or expensive** — compare today's IV to its own history (via IV rank/percentile, next chapter) rather than to a fixed number.
2. **To size the expectation correctly** — an option is only a good buy if the move you expect is *larger than the move already priced in* (IV).
3. **To choose between strategies** — high IV favours strategies that *collect* premium; low IV favours strategies that *pay* it (Chapter 25 makes this precise).

## The annualisation convention

Both IV and HV are quoted as **annualised** percentages. But the number you usually care about is the *expected move over your holding period*, which scales by the square root of time:

Expected move (1σ) ≈ Price × IV × √(T/252)

For NIFTY at 25,000 with 10% IV and 30 days to expiry:

Expected 1σ move ≈ 25,000 × 0.10 × √(30/252) ≈ 25,000 × 0.10 × 0.345 ≈ **863 points**

This "expected move" is the single most practical use of IV: it tells you, before any event, the size of the move the market is already pricing. Chapter 30 and the cheat sheet return to it.

## Summary

- HV looks backward (realised); IV looks forward (priced-in expectation).
- IV is the σ that makes the model fit the market price — a standardised "price of uncertainty."
- IV > HV means options are expensive; the reverse means cheap; on average IV exceeds realised (the variance risk premium).
- IV is about magnitude, not direction.
- Convert annualised IV to an expected move with the √time rule.

Next: reading IV in context — rank, percentile, skew, and term structure.
