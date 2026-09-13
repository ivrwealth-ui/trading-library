# 12. Theta: The Price of Time

## The wasting asset

An option is one of the few financial instruments that **loses value purely by the passage of time**. Everything else held constant — the underlying frozen, volatility unchanged — the option's premium erodes a little every day. **Theta (Θ)** measures this erosion: the change in an option's price as **one day passes**.

Formally, theta is the derivative of price with respect to time. It is conventionally quoted as a *negative* number for buyers (the option loses value each day) and *positive* for sellers (the position gains each day).

## The shape of decay

Time decay is **not linear**. It accelerates as expiry approaches:

- Far from expiry, an option loses time value slowly — there is still plenty of time for the underlying to move.
- Near expiry, time value collapses — and the rate of collapse steepens dramatically in the final days.

This is why the last week before expiry is when option sellers feel richest and option buyers feel the clock loudest. An ATM option with 30 days left might lose ₹X per day; the same option with 3 days left loses several times ₹X per day.

The mathematical form is a square-root relationship: roughly, time value scales with the **square root of time remaining**. Halving the time remaining does *not* halve the time value — it reduces it by only about 29% (1 − 1/√2). This is the same square-root law that appears in volatility (Chapter 13) and is a recurring theme: *option prices scale with √time.*

## Where theta is strongest

- **ATM options have the highest theta.** This is where time value is largest (Chapter 5), so the daily erosion is largest there too.
- **OTM options lose a higher *percentage* of their value** each day, even though the absolute amount is smaller. A cheap OTM option can decay to zero remarkably fast in the final days.
- **ITM options** have the lowest theta in absolute terms, because most of their price is intrinsic value, which does not decay.

## Theta for buyers vs. sellers

This is the hinge of the whole buyer/seller divide, made quantitative:

- A **buyer** pays theta every day. To profit, the position must overcome time decay — the underlying must move (delta/gamma) or volatility must rise (vega) by *more* than the daily theta cost. A buyer who is right about direction but *slow* can still lose.
- A **seller** collects theta every day. Time decay is the seller's "carry" — the reason income strategies work. But theta is compensation for risk (gamma and vega), not free money; the seller collects a steady stream while accepting the possibility of a large sudden loss.

A useful way to think about it: **theta is the rent.** Buyers pay rent for the chance of a move; sellers collect rent for the risk of one.

## The theta-gamma trade-off

Theta and gamma are intimately linked — you cannot have one without the other, and they pull in opposite directions for a hedged position.

- **Long options:** positive gamma (movement helps), negative theta (time hurts). The position *wants* the market to move and *pays* for the privilege daily.
- **Short options:** negative gamma (movement hurts), positive theta (time helps). The position *wants* stillness and *earns* for tolerating risk.

This is the fundamental tension of options: **you are either paying for movement or being paid for stillness.** There is no position that is both long gamma and long theta — the market prices the two against each other. A **gamma scalper** (Chapter 26) earns by harvesting the movement that a long-gamma position is exposed to, attempting to pay for (or exceed) the theta cost.

## Weekend and holiday theta

A common misconception: "theta pauses over the weekend." In practice, markets do *not* fully price the two non-trading days on Friday — meaning Monday's open often shows an outsized decay that accounts for the weekend. This is not a clean "weekend theta" credit but a practical observation that time value for Saturday and Sunday is effectively realised when trading resumes. Experienced traders account for this when holding short positions over the weekend.

## Practical rules of thumb

- If you are **buying**, prefer enough time to expiry that theta is not eating you alive — and know your daily "rent" cost.
- If you are **selling**, the final two weeks (especially the last few days) are where decay accelerates most — but also where gamma risk is highest.
- Compare theta as a *percentage* of premium, not just an absolute number, to judge how fast a position is melting.
- Never hold a short-option position through a known high-impact event purely for the theta — the gamma/vega risk on the event day usually dominates.

## Summary

- Theta = the daily erosion of an option's value; negative for buyers, positive for sellers.
- Decay accelerates near expiry and is strongest at the money.
- Time value scales with √time — halving time does not halve the premium.
- Buyers pay theta; sellers collect it — the "rent" framing.
- Theta and gamma are opposites; you are either paid for stillness or paying for movement.

Next: vega — the price of volatility.
