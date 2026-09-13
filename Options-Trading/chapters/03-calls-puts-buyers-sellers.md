# 3. Calls, Puts, Buyers, and Sellers

## Four roles, one contract each

Because there are two option types (call, put) and two sides (buy, sell), there are exactly **four basic positions** in options. Every strategy in this book is one of these, or a combination of them.

| Position | Right / Obligation | View | Maximum profit | Maximum loss |
|----------|-------------------|------|----------------|--------------|
| Long call | Right to buy | Bullish | Unlimited | Premium paid |
| Short call | Obligation to deliver | Bearish / neutral | Premium received | Unlimited |
| Long put | Right to sell | Bearish | Large (capped at strike) | Premium paid |
| Short put | Obligation to take delivery | Bullish / neutral | Premium received | Large (capped at strike) |

This single table contains more trading wisdom than most people absorb in years. Read it slowly.

## The long call — buying the right to buy

A **long call** is the classic first position. You pay the premium for the right to buy the underlying at the strike.

- **Why a trader takes it:** they expect the underlying to rise above the strike by more than the premium before expiry.
- **Best case:** the underlying rises far — profit is theoretically unlimited.
- **Worst case:** the underlying does not rise enough — the option expires worthless and the loss is exactly the premium paid.

The long call is the purest expression of *limited risk, unlimited reward* — the reason options are often a trader's first love, and the source of their reputation for leverage.

## The short call — selling the right to buy

A **short call** (also *writing a call*) is the mirror image. The seller receives the premium and is obligated to deliver the underlying at the strike if the buyer exercises.

- **Why a trader takes it:** they expect the underlying to stay flat or fall, so the option expires worthless and they keep the full premium.
- **Best case:** the premium is kept in full if the option expires worthless.
- **Worst case:** the underlying rises sharply — the obligation's cost grows without limit.

A naked short call is the riskiest single position in options. The premium received is fixed; the potential loss is not. This is why writing calls is almost always done against a hedge (a covered call, or a spread) rather than naked.

## The long put — buying the right to sell

A **long put** gives the right to sell the underlying at the strike. It profits when the underlying falls.

- **Why a trader takes it:** they expect a decline, or they already own the asset and want *downside protection* (a protective put — see Chapter 24).
- **Best case:** the underlying falls to zero in theory — profit approaches the full strike value minus the premium (large but finite).
- **Worst case:** the underlying does not fall — loss is the premium paid.

The long put is simultaneously a bearish speculation and an insurance policy. It is the most direct way to hedge a long portfolio against a market decline.

## The short put — selling the right to sell

A **short put** obligates the seller to take delivery of the underlying at the strike if the buyer exercises.

- **Why a trader takes it:** they expect the underlying to stay flat or rise, and are willing to buy it at the strike if it falls (the "cash-secured put" mindset — Chapter 19).
- **Best case:** the option expires worthless and the seller keeps the premium.
- **Worst case:** the underlying falls sharply; the seller buys at a strike well above the now-lower market price. The loss is capped only because the underlying cannot fall below zero.

## The symmetry that matters

Notice the pattern:

- **Buyers** (long call, long put) pay a premium and carry *limited risk, large reward*.
- **Sellers** (short call, short put) receive a premium and carry *limited reward, large risk*.

This is not a coincidence. Options are a **zero-sum transfer of risk** at the level of the premium (before transaction costs): the premium one side pays is the premium the other receives. What makes the market functional is that *both* sides often have a legitimate reason to be there — the buyer wants to cap a risk or speculate with leverage; the seller wants to earn income or acquire a position at a better price.

## A word on the four roles' risk-reward, stated honestly

Because this book exists to educate rather than to direct, here is what the four roles *imply* about the trader, stated neutrally:

- **Long call** — expresses a view that the underlying will rise; risk is capped.
- **Short call** — expresses a view that the underlying will not rise above the strike; risk is uncapped unless hedged.
- **Long put** — expresses a view that the underlying will fall (or hedges a long position); risk is capped.
- **Short put** — expresses a view that the underlying will not fall below the strike; risk is large but capped at the strike.

## Summary

- Four basic positions: long call, short call, long put, short put.
- Buyers pay premium for a right; sellers receive premium for an obligation.
- Long call and long put: limited risk. Short call and short put: limited reward.
- Every strategy in this book reduces to a combination of these four.

Next: moneyness — the language for describing where a strike sits relative to the market price.
