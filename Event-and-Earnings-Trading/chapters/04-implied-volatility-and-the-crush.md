# 4. Implied Volatility and the Crush

*Part II — IV Crush*

## What implied volatility is

**Implied volatility (IV)** is the market's expectation of future price movement, *priced into an option's premium*. It is not realised volatility (what actually happens); it is what the option market is *charging* for the risk of what might happen. When an event is approaching, IV rises — the options get more expensive because the market knows a repricing is coming.

## The crush

After the event, the uncertainty resolves. The result — whatever it is — is now known, and the *reason for the elevated premium is gone*. **Implied volatility collapses, and option premiums fall even if the underlying price barely moves.** This is the **IV crush**.

**The core asymmetry:**

- A trader who **buys** a straddle before earnings is *long vega*: they paid an inflated premium, and after the event they lose the crush on *both* legs. The stock must move *more* than the inflated premium implied, or the trade loses even if the stock moves.
- A trader who **sells** premium before earnings is *short vega*: they collect the inflated premium, and after the event they *profit from the crush* — but they carry the risk of a huge move against them.

## Why the crush matters more than the direction

The most common and painful error in event trading is buying a straddle "because earnings is coming and it will move", and then losing on a *correct directional call* — the stock moved, but not *enough* to overcome the premium that the crush then destroyed. Before any event trade, you must ask: **"How much does the market already expect this to move?"** The premium tells you. If the market has already priced in a 6% move and you think the stock moves 4%, you are on the wrong side of the crush whether you realise it or not.

## How to read IV around events

- **IV rises into the event** (the run-up) and **collapses after** (the crush). The shape is the classic "IV ramp."
- The **expected move** is encoded in the at-the-money straddle price: `ATM straddle price ÷ underlying` approximates the market's implied move. As a rule of thumb, the straddle is about 0.8× the one-standard-deviation (1σ) move, so 1σ ≈ 1.25 × the straddle. Compare that to your own estimate of the likely move.
- **Compare IV to its own history** (IV rank/percentile): an event with IV already at a multi-year high is a different proposition from one with IV near its lows.
