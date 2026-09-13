# 5. Intrinsic Value and Time Value

## The two components of every option price

Every option premium can be split into exactly two pieces:

**Premium = Intrinsic Value + Time Value**

This decomposition is the foundation of option pricing. If you understand it, the entire second part of this book (the Greeks) becomes a set of elaborations on a single sentence: *an option is worth what you could get for it right now, plus what you might get from the time and uncertainty that remain.*

## Intrinsic value — what it is worth right now

**Intrinsic value** is the value the option would have if exercised *today*. It is the option's "cash now" value, and it can never be negative.

- For a **call**: `Intrinsic value = max(Underlying − Strike, 0)`
- For a **put**: `Intrinsic value = max(Strike − Underlying, 0)`

Only **ITM options have positive intrinsic value**. ATM and OTM options have zero intrinsic value — because exercising them now would produce no gain (an ATM option gains nothing, and you would never exercise an OTM option).

Example, NIFTY at 25,000:
- 24,800 call: intrinsic value = max(25,000 − 24,800, 0) = **200**.
- 25,000 call: intrinsic value = **0**.
- 25,200 call: intrinsic value = **0**.
- 25,200 put: intrinsic value = max(25,200 − 25,000, 0) = **200**.

## Time value — what it is worth for the future it still has

**Time value** (also called *extrinsic value*) is everything in the premium that is *not* intrinsic value. It is the price the market places on the possibility that the option becomes *more* valuable before expiry — because the underlying can move, and volatility can rise.

`Time value = Premium − Intrinsic value`

Example, NIFTY at 25,000, with 10 days to expiry:
- 24,800 call trading at ₹320 → time value = 320 − 200 = **₹120**.
- 25,000 call trading at ₹150 → time value = 150 − 0 = **₹150** (all time value).
- 25,200 call trading at ₹40 → time value = **₹40** (all time value).

Two observations:

1. **ATM options carry the most time value.** This is where uncertainty about the final price is greatest, so the "time and uncertainty" premium is largest.
2. **Deep ITM and deep OTM options carry less time value.** Deep ITM options are mostly intrinsic value (nearly certain); deep OTM options have low absolute time value (small chance, small price).

## The life cycle of time value

Time value does not decay in a straight line; it **erodes toward zero as expiry approaches**, and the erosion accelerates near the end. This is the phenomenon known as *time decay*, quantified by the Greek **theta** (Chapter 12).

At expiry, time value is exactly **zero**, and the premium equals intrinsic value alone. An option that finishes OTM is worth nothing; an option that finishes ITM is worth exactly its intrinsic value.

This has a profound consequence for the two sides of every trade:

- A **buyer** is fighting time decay — every day, a little of the premium's time value melts away, and the buyer needs the market to move (or volatility to rise) fast enough to overcome it.
- A **seller** is *collecting* time decay — every day, a little more of the premium becomes profit, provided the underlying does not move against the position.

This single dynamic is why many traders describe option buying as "paying rent for a chance" and option selling as "collecting rent while carrying risk."

## Why the split matters in practice

- When you see an ITM option, always subtract intrinsic value to find out how much "time and uncertainty" you are really paying for.
- When you compare two options' cost, compare their *time value*, not just their price — a ₹300 ITM option may be "cheaper" in time-value terms than a ₹150 ATM option.
- The intrinsic/time split is what the whole concept of an option's "fair value" (Chapter 15) is built upon: pricing models produce a theoretical premium, and that premium decomposes exactly this way.

## Summary

- Premium = intrinsic value + time value.
- Intrinsic value = what it is worth now = max(ITM amount, 0); never negative.
- Time value = the premium for time and uncertainty; maximum at ATM, zero at expiry.
- Buyers fight time decay; sellers collect it.

Next: the NSE mechanics — how these contracts actually list, expire, and settle.
