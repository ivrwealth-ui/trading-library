# 21. Straddles and Strangles

## Trading magnitude, not direction

Every strategy so far bet on *direction*. Straddles and strangles bet on **magnitude** — a large move in *either* direction. They are the entry point to **volatility trading**, where the view is not "up" or "down" but "the market will move a lot (or a little)."

## The long straddle

- **Structure:** buy a call and a put at the *same* strike K (usually ATM), same expiry.
- **View:** the underlying will make a **large move**, direction unknown. (E.g., ahead of a major event.)
- **Maximum profit:** unlimited on the upside (call), large on the downside (put, capped at K).
- **Maximum loss:** the total premium paid (call + put) — the risk is fully defined.
- **Breakevens:** two — K − total premium, and K + total premium.
- **Greeks:** long gamma, long vega, short theta (twice, since two options are bought).

### Example

NIFTY at 25,000. Buy the 25,000 call for ₹150 and the 25,000 put for ₹140. Total premium = ₹290.

- Breakevens: **24,710** and **25,290**.
- Profit if NIFTY is outside that range at expiry; maximum loss of ₹290 if NIFTY is exactly 25,000 (both expire worthless).

The straddle is a pure "big move" bet: you lose only if the market does *not* move much, and you profit roughly linearly once it moves beyond either breakeven.

## The long strangle

- **Structure:** buy an OTM call at K₂ and an OTM put at K₁ (different strikes), same expiry.
- **View:** a large move, direction unknown, but you are willing to accept a *wider* required move for a *cheaper* entry.
- **Maximum profit:** unlimited on the upside, large on the downside.
- **Maximum loss:** total premium paid (call + put) — cheaper than the straddle because both legs are OTM.
- **Breakevens:** K₁ − total premium, and K₂ + total premium (a wider range than the straddle).

### Example

NIFTY at 25,000. Buy the 25,200 call for ₹80 and the 24,800 put for ₹70. Total = ₹150.

- Breakevens: **24,650** and **25,350**.
- Cheaper than the straddle (₹150 vs ₹290), but requires a larger move from spot to profit: NIFTY must move 350 points from 25,000 to reach a breakeven, versus 290 points for the straddle (each strangle breakeven sits only 150 points — its own premium — beyond the nearer strike).

**Straddle vs. strangle** is a cost-versus-move trade-off: the straddle costs more but profits sooner; the strangle costs less but needs a bigger move.

## The short straddle and short strangle

Selling these positions (short straddle, short strangle) is the mirror: **collect premium and profit from a *small* move** (stillness).

- **Short straddle:** sell a call and put at the same strike. Collect both premiums; profit if the underlying stays within K ± premium. **Maximum loss: unlimited** on the upside, large on the downside.
- **Short strangle:** sell an OTM call and OTM put. Collect both; profit if the underlying stays between the two strikes (plus premium). Loss beyond the breakevens.

Short vol positions like these have **negative gamma** — the risk accelerates against you as the market moves. They collect steady theta but carry the classic "steamroller" tail risk. They are generally reserved for experienced traders with strict loss rules (and are often converted to defined-risk versions like iron condors — next chapter).

## The volatility view, made explicit

Straddles and strangles are where the book's volatility framework becomes concrete:

- **Buy** a straddle/strangle when you expect the market to move *more than the premium implies* — i.e., when **implied volatility is cheap** (low IV rank/percentile) relative to your expectation, or ahead of an event you believe is under-priced.
- **Sell** a straddle/strangle when you expect the market to move *less than the premium implies* — when **IV is expensive** and likely to mean-revert.

The premium of a straddle is effectively the market's *price of a move*: it approximates the expected move (Chapter 16). Buying means "I think the move will be bigger than priced"; selling means "smaller than priced." This is volatility trading in one sentence.

## The event-day trap (volatility crush)

The most common way beginners lose money on long straddles is buying them **ahead of a scheduled event** (budget, election, earnings). Implied volatility is usually **elevated before the event and collapses after it**. The result: even a correct directional move can lose money, because the *premium you paid* was inflated by pre-event fear that vanishes once the uncertainty resolves.

The lesson: for event-driven straddles, the move must exceed *the move already priced in*, and the *post-event IV collapse* is an additional headwind on top of the required move. This is the single most important caveat about buying volatility.

## Summary

- Straddle = same-strike call + put; strangle = OTM call + OTM put.
- Long straddle/strangle = bet on a big move; defined risk (premium), unlimited/large reward, long gamma/vega.
- Short straddle/strangle = bet on stillness; collect premium, negative gamma, unbounded (straddle) tail risk.
- Buying vol means "move bigger than priced"; selling vol means "move smaller than priced."
- Beware the pre-event IV crush on long straddles.

Next: iron condors and butterflies — defined-risk ways to trade a range.
