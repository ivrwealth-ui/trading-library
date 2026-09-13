# 2. The Math of Ruin and Drawdown

## The numbers that make risk management non-negotiable

This chapter puts numbers on the ideas from Chapter 1. Three concepts — **drawdown**, **risk of ruin**, and **the recovery problem** — turn "risk matters" from a slogan into arithmetic.

## Drawdown: how deep the hole goes

A **drawdown** is the peak-to-trough decline in your equity. It is the number that actually *hurts* — the distance your account falls from its high before recovering.

Drawdown is not merely uncomfortable; it interacts with compounding in a way most people do not feel until it is too late. Because recovery is asymmetric (Chapter 1), the depth of a drawdown determines not just how you *feel* but how long it takes — and whether it is possible — to get back to even.

The recovery table is the single most important table in risk management:

| Loss | Gain needed to recover |
|------|------------------------|
| 5% | 5.3% |
| 10% | 11.1% |
| 20% | 25% |
| 30% | 42.9% |
| 50% | 100% |
| 70% | 233% |
| 90% | 900% |

The rule that falls out of it: **protect against the deep drawdowns.** The difference between a 20% and a 50% drawdown is not "a bit worse" — it is the difference between recovering in a reasonable time and possibly never recovering at all.

## Risk of ruin: the probability of being wiped out

**Risk of ruin** is the probability that, over a long sequence of trades, your account is drawn down to (or near) zero. It is a function of three things: your **win rate**, your **payoff ratio**, and — critically — your **position size**.

The brutal insight is that risk of ruin is dominated by position size, not by edge:

- With a fixed risk of **1% per trade**, even a modest edge survives long losing streaks: a 10-trade losing streak costs ~10%, and you are still in the game.
- With a fixed risk of **10% per trade**, a 10-trade losing streak costs ~65% — and a 20-trade streak is near-total ruin, *even if the underlying strategy has a positive edge.*

The mathematical point: **over-betting is how positive-expectancy strategies get ruined.** Risk of ruin is not about whether your edge is real; it is about whether your sizing lets you survive the *inevitable* losing streaks long enough for the edge to pay.

## The losing streak is not a bug

Here is the fact most traders resist: **losing streaks are guaranteed.** A strategy that wins 55% of the time will, over a long career, experience long runs of losses — 10, 15, even 20 in a row — purely by chance. This is not the strategy "breaking"; it is the normal behaviour of any probabilistic process.

Risk management is built for exactly this: **the point is not to avoid losing streaks (impossible); it is to make them survivable.** A 1% risk per trade turns the worst realistic streak into a survivable drawdown; a 10% risk turns it into ruin.

## The recovery problem, quantified

Combine drawdown with the time it takes to recover, and the asymmetry compounds again:

- From a **10%** drawdown, a trader earning a modest 20% annual return needs roughly **half a year** to recover.
- From a **50%** drawdown, the same trader needs **~3.8 years** of unbroken 20% returns just to get back to even.

Time is the hidden cost of drawdown. Every deep drawdown is not just a loss of money; it is a loss of *years* — and those are years in which the edge could have been compounding from a higher base.

## The practical conclusions

1. **Size small enough that the worst realistic streak is survivable** — the 1–2% rule (next chapter) is a direct consequence of risk-of-ruin math, not an arbitrary convention.
2. **Protect against deep drawdowns** — a rule that halves your worst drawdown is worth more than one that adds a point of return.
3. **Treat the losing streak as normal** — it is coming; the only question is whether your sizing survives it.
4. **Never over-bet** — risk of ruin rises steeply with position size, far faster than expected return does.

## Summary

- Drawdown is the peak-to-trough fall in equity; recovery is asymmetric.
- Risk of ruin is dominated by position size, not by edge.
- Losing streaks are guaranteed, not a sign of a broken strategy.
- Deep drawdowns cost years, not just money.
- Size for survival: small enough that the worst streak is survivable.

Next: the risk-per-trade foundation — the 1–2% rule and why it is the load-bearing decision.
