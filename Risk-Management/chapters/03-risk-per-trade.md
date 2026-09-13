# 3. The Risk-Per-Trade Foundation

## One number decides whether you survive

The foundational rule of risk management is simple to state and hard to internalise: **risk a fixed, small fraction of your capital on every trade** — conventionally **1–2%**.

This single number is the load-bearing wall of the entire discipline. Every position-sizing method in the next chapter is, at bottom, a way of implementing this one idea.

## The definition of "risk"

First, precision: **risk is not the size of the position; it is the distance from entry to your stop, times the size of the position.** Risk is the amount you lose *if the trade fails and you honour the stop.*

- A large position with a very tight stop can have *small* risk.
- A small position with a very wide stop can have *large* risk.

The 1–2% rule is about **risk**, not position size. A trader risks 1% of capital *per trade* — meaning if the stop is hit, the account falls by 1%, no more.

## The rule

**Risk per trade = 1–2% of account equity.**

In rupees, for a ₹10,00,000 account:

- 1% risk = ₹10,000 maximum loss per trade.
- 2% risk = ₹20,000 maximum loss per trade.

Why so small? Because of Chapter 2's mathematics:

- At 1% risk, a 10-trade losing streak costs ~10% — uncomfortable but survivable.
- At 1% risk, even a catastrophic 20-trade streak costs ~18% — you are still compounding.
- The small size is what converts "losing streaks are guaranteed" into "losing streaks are survivable."

## How risk translates into position size

The position size is derived from the risk, not the other way around:

Position size = (Account × Risk %) ÷ (Entry − Stop)

This is the single most important formula in the book. It does something remarkable: **it equalises risk across all trades**, regardless of how far each stop is. A trade with a tight stop gets a larger position; a trade with a wide stop gets a smaller one — so that both lose the *same* amount if stopped.

### Worked example

Account ₹10,00,000. Risk 1% = ₹10,000.

- Trade A: entry ₹500, stop ₹480. Distance = ₹20. Position size = 10,000 ÷ 20 = **500 shares**.
- Trade B: entry ₹500, stop ₹450. Distance = ₹50. Position size = 10,000 ÷ 50 = **200 shares**.

Both positions, if stopped, lose exactly ₹10,000. The stop distance — a property of the *setup* — determines the size, so that *risk* is constant.

## Why this is the foundation

Three reasons this rule is foundational rather than optional:

1. **It makes ruin nearly impossible by single trades.** No single trade can do more than 1–2% damage. Even a streak cannot destroy you.
2. **It removes emotion from sizing.** The position size is *computed* from the stop, not *chosen* by conviction. Conviction is exactly the thing that over-bets, and over-betting is exactly what causes ruin (Chapter 2).
3. **It makes the edge expressible.** An edge shows up only over many trades; fixed-fraction risk ensures you are *present* for enough trades to collect it.

## The hardest part

The rule is mathematically simple and psychologically brutal, because it requires accepting that **most individual trades do not matter.** A 1%-risk trade, won or lost, barely moves the account — and that is precisely the point. The trader who needs every trade to be significant will over-bet; the trader who accepts that the *distribution* matters, not any single trade, can keep risk at 1% and survive to collect the distribution.

The 1–2% rule is not a ceiling on ambition; it is a floor under survival.

## Summary

- Risk = (entry − stop) × position size; it is not the position size itself.
- Risk 1–2% of account equity per trade.
- Position size is *derived* from risk: (Account × Risk%) ÷ stop distance.
- Fixed-fraction risk equalises risk across trades and removes emotion from sizing.
- It makes ruin-by-streak survivable and lets the edge express itself over many trades.

Next: the position sizing methods — five ways to set that 1–2%.
