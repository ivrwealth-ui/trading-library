# 4. Moneyness: In-the-Money, At-the-Money, Out-of-the-Money

## Where is the strike, relative to the market?

**Moneyness** describes the relationship between an option's strike price and the current price of the underlying. It is the first question to ask about any option, because it determines whether the option has *intrinsic value* (explored next chapter) and how it will behave as the market moves.

The three states:

- **In-the-Money (ITM)** — the option would currently have value if exercised now.
- **At-the-Money (ATM)** — the strike is at (or nearest to) the current market price.
- **Out-of-the-Money (OTM)** — the option would be worthless if exercised now.

Crucially, *ITM/ATM/OTM means different things for calls and puts*, because a call is about buying and a put is about selling.

## For calls (right to buy)

A call is valuable when the underlying is *above* the strike — you can buy at the strike and it is worth more in the market.

| Condition | Moneyness |
|-----------|-----------|
| Underlying > Strike | ITM |
| Underlying ≈ Strike | ATM |
| Underlying < Strike | OTM |

With NIFTY at 25,000:
- A **24,800 call** is ITM (you could buy at 24,800 and sell at 25,000).
- A **25,000 call** is ATM.
- A **25,200 call** is OTM (buying at 25,200 when the market is 25,000 makes no sense today).

## For puts (right to sell)

A put is valuable when the underlying is *below* the strike — you can sell at the strike when the market is lower.

| Condition | Moneyness |
|-----------|-----------|
| Underlying < Strike | ITM |
| Underlying ≈ Strike | ATM |
| Underlying > Strike | OTM |

With NIFTY at 25,000:
- A **25,200 put** is ITM (you could sell at 25,200 when the market is 25,000).
- A **25,000 put** is ATM.
- A **24,800 put** is OTM.

Notice the mirror image: for calls, ITM strikes are *below* the market; for puts, ITM strikes are *above* the market.

## Degrees of moneyness

Moneyness is not just three buckets; it is a spectrum. Traders often speak of:

- **Deep ITM** — far from the market; the option behaves almost like the underlying itself (delta close to 1 for calls, −1 for puts).
- **Near/just ITM or OTM** — close to the market; the option is highly sensitive to small moves.
- **Deep OTM** — far from the market; the option is cheap but has a low probability of finishing ITM.

Some trading platforms and the NSE itself use a label grid: ATM, ITM1/ITM2/… and OTM1/OTM2/… counting steps away from the at-the-money strike. "ITM2" means "two strikes in-the-money."

## Why moneyness matters

1. **Probability.** An OTM option has a smaller chance of finishing ITM — which is why it is cheap, and why it usually expires worthless. An ITM option has a larger chance — which is why it is expensive.
2. **Cost vs. leverage.** OTM options cost less but have a lower win probability. ITM options cost more but behave more predictably (more "stock-like").
3. **Behavior of the price.** The three regions respond differently to market moves, time, and volatility — this is the entire subject of the Greeks (Part II).

Moneyness is also the reason an option chain is symmetric: for any strike, there is a call *and* a put, and one of them is ITM whenever the other is OTM (at the same strike, above the market the call is OTM and the put is ITM; below, the reverse).

## Moneyness and the two ways options are used

- **Speculation** gravitates toward OTM options: cheap, leveraged, lottery-like but low probability.
- **Hedging and income** gravitate toward ATM and ITM options: more predictable, more insurance-like.

Neither is "better" — they serve different purposes and different views. Understanding moneyness is what lets you *choose deliberately* rather than default to whatever looks cheapest.

## Summary

- Moneyness = where the strike sits relative to the market.
- Calls: ITM when underlying > strike. Puts: ITM when underlying < strike.
- At any strike, the call and put have opposite moneyness.
- ITM = higher cost, higher probability; OTM = lower cost, lower probability.

Next: the distinction between *intrinsic value* (what an option is worth now) and *time value* (what it is worth for the future it still has).
