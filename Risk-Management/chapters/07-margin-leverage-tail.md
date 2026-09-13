# 7. Margin, Leverage, and Tail Risk

## The forces that turn a bad day into a catastrophe

Per-trade and portfolio risk are, at bottom, about *sizing*. This chapter covers the forces that can **multiply** whatever sizing decision you made — margin, leverage, and tail risk — and why they deserve their own discipline, especially in Indian markets.

## Leverage: the multiplier of everything

**Leverage** is using borrowed money (or a derivative's built-in leverage) to control more exposure than your capital. It multiplies *everything* — gains *and* losses — and it is the single most common way traders turn a survivable drawdown into ruin.

The key insight: **leverage interacts multiplicatively with your risk-per-trade.**

- Risking 1% of capital *unlevered* = a 1% loss on a failed trade.
- Risking 1% of capital but controlling 5× notional via leverage = the same stop produces a **5%** loss if the underlying moves one stop-distance against you.

In other words, leverage silently inflates your *actual* risk per trade far above what you intended. A trader who thinks they are risking 1% can, through leverage, actually be risking 5–10%. This is how "disciplined" traders get destroyed: the sizing was right, but the leverage was invisible.

The rule: **risk must be computed on the *levered* exposure, not the cash outlay.** If leverage multiplies your notional, divide your intended risk by the leverage to find the correct position size — or simply size on notional, never on margin.

## Margin: capital locked against risk

In Indian derivatives, **margin** is the collateral the exchange/broker requires to hold a position, computed under the **SPAN** risk model:

- **Buying options** requires only the premium (the premium *is* the maximum loss — no extra margin).
- **Selling options** (and futures) requires SPAN margin that models the position's worst-case loss.
- **Spreads** are margin-efficient: a defined-risk spread requires roughly the *spread width* in margin, not the full notional.

Two margin disciplines matter:

1. **Keep a margin buffer.** Margin requirements *change* — they rise when volatility rises or the market moves against you. A position that is "right" can still force a margin call (and an involuntary exit at the worst price) if a volatility spike inflates the requirement. Never be fully margined.
2. **Understand that margin is not risk.** Margin is the *collateral*; your real risk is the *notional* and the *stop*. Sizing to the margin (rather than to the risk) is how traders accidentally take on far more exposure than they meant to.

## Tail risk: the rare, catastrophic move

**Tail risk** is the risk of a *large, rare* move — the kind that sits in the "tail" of the probability distribution, far beyond normal. It is the thing that makes backtests look safe and reality look brutal:

- **Gaps** — price opening far from the close (overnight news, global shocks, budget announcements). A gap can jump *past* your stop, so the realised loss exceeds the planned loss. Stops are limits, not guarantees.
- **Volatility spikes** — a sudden surge in volatility that both moves price violently *and* raises margin requirements (a double squeeze on short positions).
- **Liquidity vanishings** — in a panic, the bid-ask spread widens and you cannot exit where you want.

Tail risk is why **backtests overstate the safety** of a strategy and why **short-volatility positions (naked shorts, condors, credit spreads) are dangerous** despite their high win rates: they earn small, steady profits and then lose it all — and more — in one tail event.

## Defending against the tail

The defences are structural, not predictive:

1. **Size for the tail, not the expectation** — assume the stop might be gapped past; size so that even a *worse-than-stop* outcome is survivable.
2. **Avoid oversized positions through binary events** — earnings, budgets, elections, policy decisions on the underlying.
3. **Cap aggregate short-vol exposure** — a portfolio that is short volatility everywhere is one tail event from a blow-up; bound the total.
4. **Keep a margin buffer** — so a volatility spike cannot force an involuntary exit.

## The Indian-specific notes

- **STT and charges** apply on the sell side and on exercise; they add to the cost of every exit, so a "tight" stop is a little less tight in reality. Factor them into the risk distance.
- **Index options are cash-settled** (clean, no delivery risk); **stock options are physically settled** — an ITM stock option held to expiry results in delivery, which can force an unwanted, oversized position if not managed. Square off before expiry.
- **Retail short-selling of stocks is constrained** in India; the clean short-side is via index derivatives, which carry their own margin and gap risk.

## Summary

- Leverage multiplies risk silently; compute risk on notional, not cash outlay.
- Margin is collateral (SPAN), not risk; it changes with volatility, so keep a buffer.
- Tail risk — gaps, vol spikes, liquidity vanishing — makes stops limits, not guarantees.
- Defend structurally: size for the tail, avoid binary events, cap short-vol exposure.
- Indian specifics: costs, settlement (cash vs physical), and constrained shorting shape the risk.

Next: sizing for different strategy families — one size does not fit all.
