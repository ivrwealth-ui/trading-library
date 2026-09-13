# Risk Management and Position Sizing: The Discipline That Keeps You in the Game

## A complete guide to sizing positions, managing drawdown, and surviving the tail — for traders and investors in Indian markets — with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading and investing involve substantial risk of loss, including the possible loss of principal. No position-sizing method can eliminate risk or guarantee profitability.
- All examples, figures, and historical observations are illustrative. Historical performance never guarantees future results.
- Margin, leverage, taxes (STT, stamp duty), brokerage, and regulatory details change over time. Always verify current rules and costs before trading.
- Nothing in this book should be read as a promise of profit or a guarantee that any method will prevent loss.

By reading this book, you agree that you are solely responsible for your own trading and investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book is about the one part of trading and investing that you can actually *control*: **risk**. Strategy gives you an edge; risk management decides whether you are still around to collect it.

- **Chapters 1–2** make the case: why risk management is the real edge, and the mathematics of ruin and drawdown that make it non-negotiable.
- **Chapters 3–5** cover the per-trade layer: the risk-per-trade foundation, position-sizing methods, and stop-loss design.
- **Chapters 6–8** cover the portfolio layer: aggregate risk, margin/leverage/tail risk, and sizing for different strategy families.
- **Chapter 9** assembles it all into a written risk framework.
- The **appendix** collects every formula in one place.

A note on language: this book describes methods and their historical behaviour — never what you "should" do. Every method is framed honestly, with its failure modes. You are responsible for your own decisions.

---

## Table of Contents

1. Why Risk Management Is the Real Edge
2. The Math of Ruin and Drawdown
3. The Risk-Per-Trade Foundation
4. Position Sizing Methods
5. Stops: Types and Placement
6. Portfolio-Level Risk
7. Margin, Leverage, and Tail Risk
8. Sizing for Different Strategy Families
9. Building a Risk Framework

Appendix — Sizing Formulas

---


# 1. Why Risk Management Is the Real Edge

## The part of trading you can control

Most of trading is uncontrollable. You cannot control whether the market goes up or down, whether a breakout succeeds or fails, or whether the next event is a calm day or a crash. You cannot control the *outcomes*.

There is exactly one thing you *can* control: **how much you risk on each decision, and how much you are willing to lose before you stop.**

That single controllable — risk — is the difference between traders who compound for decades and traders who are gone in a year. It is, in a precise sense, the *real* edge: a mediocre strategy with excellent risk management survives and compounds; an excellent strategy with poor risk management eventually blows up.

## The asymmetry that defines everything

Compounding is asymmetric, and that asymmetry is brutal:

- A **10% loss** requires an **11% gain** to recover.
- A **25% loss** requires a **33% gain**.
- A **50% loss** requires a **100% gain**.
- A **90% loss** requires a **900% gain** — effectively unrecoverable.

The lesson is inescapable: **large losses are not merely bad; they are nearly permanent.** You can recover from many small losses; you cannot recover from one that halves or quarters your account. Risk management exists for one reason above all: to keep losses *small enough to recover from*.

## What "edge" actually requires

A trading edge is a statistical advantage — a win rate and a payoff ratio that, over many trades, produce positive expectancy. But an edge only *expresses itself* over a large number of trades. The moment you are removed from the game — by one oversized loss — the edge becomes irrelevant, because you can no longer take the next trade.

Risk management is therefore not a separate discipline bolted onto strategy; it is the **precondition** for any strategy to work. An edge is a promise about the *distribution* of outcomes; risk management is what lets you live long enough to *collect* that distribution.

## The three jobs of risk management

Risk management, done properly, does three things:

1. **Survival** — it caps the worst case so no single trade, day, or streak can end you.
2. **Compounding** — it keeps losses small and recoverable, so the good periods build on a base that is still intact.
3. **Psychology** — it removes the emotion from the decision, because the risk is decided *in advance* and the worst case is *known* before entry.

Notice what is *not* on the list: risk management does not predict, does not pick winners, and does not eliminate loss. It *bounds* loss — which, given the asymmetry above, is the highest-value job there is.

## The honest framing

Framed as this book always frames such things: *historically, traders and investors who sized positions to a small, fixed fraction of capital — and who honoured their stops — survived long enough for their edge to express itself, while those who sized by conviction alone were frequently removed by a single adverse streak.* The discipline is not glamorous; it is simply what makes everything else possible.

## Summary

- You can control only one thing: how much you risk.
- Losses are asymmetric: big losses are nearly permanent.
- Risk management is the precondition for any edge to express itself.
- It does three jobs: survival, compounding, and emotional discipline.
- It bounds loss — it does not predict or eliminate it.

Next: the mathematics of ruin and drawdown — why small losses are the entire game.


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


# 4. Position Sizing Methods

## Five ways to set the size

The 1–2% rule says *how much to risk*; the sizing methods say *how to translate that risk into a number of shares or contracts*. This chapter presents five methods, from the simplest to the most sophisticated, with their logic and their failure modes. All are variants of the same principle: **size from risk, not from conviction.**

## Method 1 — Fixed fraction

Risk a **constant percentage** of current equity on every trade.

Position size = (Equity × Risk%) ÷ (Entry − Stop)

This is the default method, and it has a crucial property: **it scales with the account.** As equity grows, positions grow (compounding); as equity shrinks, positions shrink (automatic de-risking after losses). Fixed-fraction is self-stabilising — after a losing streak, it automatically reduces size, which is exactly the correct behaviour.

- **Strength:** simple, self-correcting, ruin-resistant.
- **Weakness:** after a large loss, it reduces size so much that recovery is slow (the "shrinking bet" effect).

## Method 2 — Fixed ratio

Increase position size by a **fixed unit** for each fixed profit increment, rather than continuously. The idea (popularised by Ryan Jones) is to grow positions *stair-step-wise* as equity grows, but to *never* reduce below the current step on a loss.

- **Logic:** a steadier, less jumpy growth path than raw fixed-fraction, and a deliberate anti-shrinkage bias.
- **Strength:** protects capital while growing, without the aggressive drawdown of aggressive compounding.
- **Weakness:** more parameters to choose (the "delta" per step), and it can still over-leverage in a fast run-up if the steps are set too large.

## Method 3 — Volatility / ATR sizing

Size positions **inversely to volatility**, so that a volatile asset gets a smaller position and a calm asset gets a larger one — equalising the *expected* swing, not just the stop distance.

Position size = (Equity × Risk%) ÷ (k × ATR)

where ATR (Average True Range) measures the asset's typical daily range, and `k` is a multiplier (commonly 2–3) setting how many "days of range" you are risking.

- **Logic:** a ₹500 stock that moves ₹50/day is a different animal from a ₹500 stock that moves ₹5/day. Volatility sizing equalises them, so each position carries the same *market risk*.
- **Strength:** risk is normalised across volatile and calm assets; essential when trading across very different instruments.
- **Weakness:** ATR changes over time, so position size drifts; and in a volatility spike, size shrinks sharply (which is protective, but can feel like missing moves).

## Method 4 — Kelly criterion

The Kelly formula gives the **fraction of equity that maximises long-run growth** for a known edge:

Kelly fraction = (p·W − q·L) / W  (or the more general: f = p − q / (W/L))

where `p` = win rate, `q` = 1 − p, `W` = average win, `L` = average loss.

- **Logic:** the mathematically optimal bet size for compounding, given perfect knowledge of your edge.
- **Strength:** maximises long-run growth *in theory*.
- **Weakness:** it assumes you *know* your true edge precisely — which no trader does. Full Kelly is wildly aggressive (it routinely recommends risking 20–40%), and any error in estimating your edge makes it over-bet and increases ruin risk. This is why full Kelly is a theoretical ideal, not a practical rule.

## Method 5 — Fractional Kelly

Use a **fraction of the Kelly size** — commonly **half-Kelly or quarter-Kelly** — to capture most of the growth benefit while cutting the ruin risk dramatically.

- **Logic:** the growth curve near full Kelly is flat at the top (a bit less than Kelly is nearly as good), but the ruin risk is steeply lower. Half-Kelly gives roughly three-quarters of the growth for a fraction of the volatility and ruin risk.
- **Strength:** the best practical compromise between growth and safety — *if* you can estimate your edge.
- **Weakness:** still depends on estimating win rate and payoff; and for most retail traders, a simple fixed-fraction (Method 1) at 1–2% is both simpler and safer than any Kelly variant.

## Choosing a method

The honest guidance:

- **Start with fixed fraction (Method 1)** at 1–2%. It is sufficient, simple, and ruin-resistant.
- **Add volatility sizing (Method 3)** when you trade across assets of very different volatility (e.g., NIFTY futures and a small-cap stock).
- **Treat Kelly (Methods 4–5) as a diagnostic, not a rule** — use it to understand what your edge *implies*, but size far below it (quarter-Kelly at most), because your edge estimate is almost certainly too optimistic.

Every method fails the same way — **over-betting** — and the defence is always the same: size from risk, prefer smaller, and let compounding do the work over time rather than leverage.

## Summary

- Fixed fraction: constant % of equity; self-stabilising; the default.
- Fixed ratio: stair-step growth, anti-shrinkage; more parameters.
- Volatility/ATR: size inversely to volatility; equalises market risk.
- Kelly: theoretical optimum; assumes perfect edge knowledge; too aggressive in practice.
- Fractional Kelly: most of the growth, far less ruin risk; still needs an edge estimate.

Next: stops — the other half of "risk = entry − stop".


# 5. Stops: Types and Placement

## The stop is the risk

The stop-loss is not an optional accessory to a trade; **it is the trade's definition of risk.** Recall: risk = (entry − stop) × size. The stop is half of that equation. A position without a stop has no defined risk — and therefore no correct size.

This chapter covers the types of stops, how to place them, and the discipline of honouring them.

## What a stop is (and is not)

A **stop** is a pre-committed price at which you exit a losing position. Its purpose is not to *avoid* loss — losses are inevitable — but to **bound** it: to make the loss *known and small* rather than *open-ended and growing*.

Three truths about stops:

1. **A stop is a commitment made in a calm state** — set at entry, before the position exists, when judgment is clean.
2. **A stop is not a guarantee** — a gap can jump past it (Chapter 7 covers this), so the realised loss can exceed the planned loss.
3. **A stop's only job is to keep losses small.** It does not predict; it enforces.

## Types of stops

### 1. The structural stop

Placed at a level that **invalidates the setup** — below the pullback low, below the breakout level, below the range floor, below the reversal low. This is the *most meaningful* stop, because it is tied to *why you entered*: if price reaches it, the reason for the trade is gone.

- **Strength:** exits exactly when the setup is proven wrong.
- **Weakness:** can be wide (and therefore force a smaller position); requires correctly identifying the structural level.

### 2. The volatility stop

Placed a fixed multiple of **ATR** (or a percentage) from entry, sized to the asset's normal noise so you are not stopped out by ordinary movement.

- **Strength:** adapts to how wild the asset is; robust across instruments.
- **Weakness:** ignores structure — it can sit at a level that has no meaning, or be too tight for the trade's actual invalidation point.

### 3. The trailing stop

A stop that **moves with the trade** — e.g., a close below a rising 20-day or 50-day MA, or a fixed distance behind the most recent high. It lets winners run while locking in open profit.

- **Strength:** the mechanism behind "let winners run"; converts an open gain into a protected one.
- **Weakness:** can be too tight (whipsawed out of good trades) or too loose (gives back large open profit).

### 4. The time stop

Exit after a fixed **holding period** regardless of price — e.g., "if the move has not happened in 10 days, leave." It is a stop on *time*, not price.

- **Strength:** enforces an exit when a trade is simply not working (dead money is a real cost).
- **Weakness:** can exit a trade that was about to work; best used as a *supplement* to a price stop, not a replacement.

## How to place the stop

The placement principle is: **the stop goes at the level that would prove the setup wrong — and then you size to it.**

1. Identify the setup's invalidation level (structural stop).
2. Measure the distance from entry to that level.
3. Size the position so that this distance = your fixed risk (the Chapter 3 formula).

In other words: **you do not choose the stop to fit a desired position size; you choose the stop for its logic, and let it dictate the size.** A stop that is "just far enough to not be hit" is a stop that is not doing its job — it is wide enough to give back real money.

## The discipline: honour the stop

The most common and most destructive failure is **moving the stop**. A losing trade gets "a little more room," then a little more, until a planned 1% loss becomes an unplanned 10% loss. The stop is only meaningful if it is honoured *at the pre-set level, without negotiation.*

The reason this is so hard is psychological (loss aversion, hope) — but the fix is mechanical: **decide the stop at entry, write it down, and treat "moving the stop" as breaking the trade's contract.** The stop is the one place where discipline is truly binary: you either honour it or you don't.

## Summary

- The stop is the trade's definition of risk — half of "risk = entry − stop."
- Types: structural (invalidation), volatility (ATR), trailing (lock profit), time (dead-money).
- Place the stop at the level that proves the setup wrong, then size to it.
- The stop is a commitment made in a calm state; honouring it is binary.

Next: portfolio-level risk — the danger that lives across trades, not within one.


# 6. Portfolio-Level Risk

## The danger that lives across trades

Per-trade risk management is necessary but not sufficient. A portfolio can be full of individually "safe" 1%-risk positions and still be dangerous — because **risk is not additive when positions are correlated.** This chapter covers the risk that exists *between* trades, not within one.

## The correlation problem

Suppose you hold ten positions, each risking 1% with its own stop. Naively, your total risk is 10%. But if all ten are *long the same market* — ten Indian large-caps, say — then they are not ten independent bets; they are **one bet on the broad market, expressed ten times.**

In a market crash, all ten hit their stops together. Your "10% of diversified risk" is actually a single concentrated 10% loss, because the positions moved as one.

The principle: **your portfolio's real risk is your net exposure, not your number of positions.** Ten correlated positions are one position, sized ten times too large.

## Measuring the exposure that matters

Three aggregate numbers summarise portfolio risk:

1. **Net delta / net direction** — the sum of all positions' directional exposure. If everything is long, net direction is fully long; a market down-move hurts everything at once.
2. **Net exposure to a single factor** — a portfolio of all large-caps is exposed to the *large-cap* factor; all banks are exposed to the *financials* factor; all momentum names to the *momentum* factor (and its crash risk). Concentration in one factor is hidden risk.
3. **Correlation between positions** — if your "diversified" book is all driven by the same macro driver, diversification is illusory.

## Portfolio-level rules

A handful of rules manage this:

### 1. Cap total open risk

Limit the **sum** of open risk (e.g., total at-risk across all positions ≤ 6–10% of equity). If every position risks 1%, do not hold more than 6–10 concurrent positions. This caps the worst-case simultaneous drawdown.

### 2. Diversify across drivers

Hold positions that are driven by *different* things — different sectors, different sizes, different styles (momentum + value + quality), or different asset classes. True diversification is diversification of *drivers*, not of tickers.

### 3. Watch net exposure, not just positions

If the market is below its 200-day MA, and your entire book is long, you have one large short-the-trend bet — regardless of how many names it is spread across. A broad **regime filter** (reduce long exposure in downtrends) is portfolio-level risk management.

### 4. Rebalance correlation

Periodically check: *if the market fell 10% tomorrow, what would this portfolio do?* If the honest answer is "fall ~10%," it is not diversified — it is one bet. Rebalance toward genuinely different drivers.

## The concentration traps

Three specific traps to name:

- **Sector concentration** — ten banks is one financials bet, not ten bets.
- **Style concentration** — ten momentum names all crash together in a momentum reversal.
- **Correlated "hedges"** — a hedge that is itself correlated with the portfolio (e.g., hedging Indian stocks with an asset that falls when they do) is not a hedge; it is more of the same.

## The honest bottom line

Portfolio-level risk is the answer to the question "where could I lose a lot, all at once?" Per-trade rules answer "in any one trade" (small); portfolio rules answer "across the book" (potentially large). Both questions must be answered. A trader who sizes each trade perfectly but holds ten copies of the same bet has solved only the easy half of the problem.

## Summary

- Risk is not additive when positions are correlated; ten correlated positions are one bet.
- Real risk is net exposure (direction, factor, correlation), not position count.
- Rules: cap total open risk, diversify across drivers, watch net exposure, rebalance correlation.
- Concentration traps: sector, style, and correlated "hedges".
- Manage risk both per-trade and across the book.

Next: margin, leverage, and tail risk — the forces that turn a bad day into a catastrophe.


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


# 8. Sizing for Different Strategy Families

## One size does not fit all

The 1–2% risk-per-trade rule is universal, but *how* it is applied varies by strategy family, because different families have **different win rates, different payoff shapes, and different tail profiles.** This chapter sizes each family correctly.

## The four families and their risk profiles

| Family | Win rate | Payoff shape | Tail | Sizing implication |
|--------|----------|--------------|------|--------------------|
| Trend / momentum | Low (~35–45%) | Few large winners | Crashes in reversals | Small size, strict stops, let winners run |
| Mean reversion | High (~60–70%) | Many small winners | Occasional blow-ups | Small size *because* of the tail, not the win rate |
| Short volatility | Very high (~75%+) | Steady small wins | One catastrophic loss | Smallest size; hard loss limits; defined-risk only |
| Long options / convexity | Low (~30%) | Small losses, rare huge wins | Favourable (bounded loss) | Premium is the risk; can size on premium |

The lesson in one line: **size by the tail, not the win rate.** The high-win-rate families (mean reversion, short vol) *feel* safe precisely because their losses are rare — and that rarity is exactly why those losses must be small when they arrive.

## Trend / momentum: many small losses, few big winners

Trend-following loses more often than it wins, and pays for it with the occasional large winner. The sizing discipline:

- **Small, fixed risk per trade (1%).** The many small losses must stay small.
- **Strict stops, and *let winners run*** — a trend strategy that caps its winners has no edge, so the exit must be trailing, not a target.
- **Survive the whipsaw streaks** — trend strategies can lose 10+ in a row in choppy markets; sizing must make that survivable.

## Mean reversion: high win rate, but a hidden tail

Mean-reversion strategies win often (fading extremes works most of the time) but lose big when the "extreme" turns out to be a genuine move. The trap is that the high win rate invites over-sizing.

- **Small size *despite* the win rate** — the occasional blow-up is the risk that dominates.
- **A trend filter** (only fade *with* the longer trend) materially improves the odds.
- **A hard stop** on every trade, because the "bounce" sometimes never comes.

## Short volatility: the most dangerous family

Short-vol (naked shorts, condors, credit spreads, covered calls) collects premium with a very high win rate — and carries the risk of one catastrophic, unbounded loss.

- **The smallest size of all**, and **prefer defined-risk structures** (spreads, condors) over naked shorts.
- **Hard loss limits** — a pre-set exit when the loss reaches a multiple of the credit, honoured without exception.
- **Cap aggregate short-vol exposure** at the portfolio level — many small short-vol positions are still one tail event from a blow-up.

## Long options / convexity: the friendly tail

Long options have a *bounded* downside (the premium) and an *unbounded* upside — the friendliest tail of the four families. But they lose most of the time (time decay).

- **The premium is the risk** — a long option's maximum loss is known and fixed at entry.
- **Size on the premium** — treat the entire premium as the "risk," and size it to your 1–2% rule (you *can* lose 100% of it).
- **Budget for the low win rate** — buying options is a high-variance, low-win-rate activity; the winners must be allowed to be large.

## The universal thread

Whatever the family, the same three questions size the position:

1. **What is the worst realistic loss** (including the tail, not just the stop)?
2. **What fraction of capital is that?** (Cap it at 1–2%.)
3. **Does the family's win rate invite over-betting?** (If so, resist it — the tail, not the win rate, sets the size.)

Families differ in *how dangerous they are*; the sizing question is the same, and its answer is always "small enough to survive the tail."

## Summary

- Size by the tail, not the win rate.
- Trend: small size, strict stops, let winners run.
- Mean reversion: small size despite the high win rate; use a trend filter.
- Short vol: the most dangerous; defined-risk, hard limits, smallest size.
- Long options: the premium is the risk; size the premium to 1–2%.
- The same three questions size every family.

Next: assembling it all into a written risk framework.


# 9. Building a Risk Framework

## From rules to a system you actually follow

The previous chapters are a toolkit. This chapter assembles the toolkit into a **risk framework** — a written, repeatable system that turns risk management from a set of good intentions into a set of non-negotiable, checkable rules.

## The framework, in five parts

### 1. The per-trade rule

The foundation, in writing:

- **Risk per trade = 1–2% of equity**, computed as (Account × Risk%) ÷ (Entry − Stop).
- **The stop is set at entry**, at the level that invalidates the setup, and is **never moved** after entry.
- **The size is derived from the stop**, never from conviction.

### 2. The portfolio rule

- **Cap total open risk** (e.g., sum of at-risk ≤ 6–10% of equity).
- **Cap exposure to any one driver** (sector, style, factor) — diversify across genuinely different drivers.
- **Watch net direction** — if the book is net-long into a downtrend, reduce it.

### 3. The leverage-and-margin rule

- **Compute risk on notional, not cash outlay** — if leverage is involved, divide size by the leverage.
- **Keep a margin buffer** (never fully margined), so volatility spikes cannot force an involuntary exit.
- **Prefer defined-risk structures** over naked short positions.

### 4. The tail rule

- **Size for the worst plausible gap**, not just the stop.
- **No oversized positions through binary events** (earnings, budgets, policy).
- **Cap aggregate short-volatility exposure** at the portfolio level.

### 5. The review rule

- **Review every closed trade** against its plan: *was the stop honoured? Was the size correct? Was the exit by rule, not emotion?*
- **Review the drawdown** periodically: *is the current drawdown within what this strategy should produce, or is something broken?*
- **Adjust rules only through a pre-committed process**, never reactively mid-drawdown.

## A written template

A one-page framework document, filled in and kept where you trade:

```
Per-trade:
  Risk % per trade: ____ (1-2%)
  Stop: set at entry, at the setup's invalidation level, never moved
  Size = (Equity × Risk%) ÷ (Entry − Stop)

Portfolio:
  Max total open risk: ____ % of equity
  Max per-driver (sector/style/factor) exposure: ____ %
  Net-direction check: reduce longs when market < 200-day MA

Leverage/margin:
  Risk computed on notional: yes
  Margin buffer: always hold > ____ % free margin
  Naked shorts: allowed / not allowed

Tail:
  Size assumes a ____ % gap is possible
  Binary-event rule: ____
  Max aggregate short-vol exposure: ____ %

Review:
  Trade review cadence: every trade
  Drawdown review cadence: weekly / monthly
  Rule changes: only via scheduled review, never reactively
```

Filling this in — and keeping it visible — is the difference between *knowing* risk management and *doing* it.

## Why a written framework works

A written framework works for a specific reason: **it moves the decisions out of the emotional moment and into the calm one.** The stop is set *before* the loss is happening; the size is computed *before* the conviction kicks in; the rule change is decided *before* the drawdown is screaming at you.

Every failure of risk management is, at root, a failure to honour a decision that was only ever in your head. Writing it down — and treating the document as binding — is the mechanical fix for a psychological problem.

## The honest bottom line

Risk management is not complicated, and it is not exciting. It is the quiet discipline of *never betting so much that you can be removed from the game.* Every strategy, every edge, every clever idea in trading is downstream of that single commitment. The trader who sizes small, honours stops, and survives the tail has done the hard part; everything else is detail.

## Summary

- The framework has five parts: per-trade, portfolio, leverage/margin, tail, and review.
- Write it down; the document moves decisions out of the emotional moment.
- The per-trade 1–2% rule, set at entry and never moved, is the foundation.
- Portfolio, leverage, and tail rules prevent the correlated, multiplied, catastrophic loss.
- The review rule is how the framework improves rather than decays.

This completes the main text. The appendix collects every sizing formula in one place.


# Appendix — Sizing Formulas

## The core formulas, in one place

### The foundation

**Risk = (Entry − Stop) × Position size**

**Position size = (Account equity × Risk%) ÷ (Entry − Stop)**

### The recovery table

| Loss | Gain needed to recover |
|------|------------------------|
| 5% | 5.3% |
| 10% | 11.1% |
| 20% | 25% |
| 30% | 42.9% |
| 50% | 100% |
| 70% | 233% |
| 90% | 900% |

### The sizing methods

| Method | Formula / rule |
|--------|----------------|
| Fixed fraction | size = (Equity × Risk%) ÷ (Entry − Stop) |
| Fixed ratio | grow size by a fixed unit per fixed profit increment |
| Volatility (ATR) | size = (Equity × Risk%) ÷ (k × ATR) |
| Kelly | f = (p·W − q·L) / W |
| Fractional Kelly | size at half- or quarter-Kelly |

### Risk of ruin intuition

Risk of ruin rises steeply with position size, regardless of edge. Fixed-fraction sizing at 1–2% keeps the worst realistic losing streak survivable.

### The load-bearing rules (memorise these)

1. **Risk 1–2% per trade.** Compute it on notional (not cash outlay), from the stop distance.
2. **Set the stop at entry, at the invalidation level, and never move it.**
3. **Size by the tail, not the win rate** — the high-win-rate families carry the sharpest tails.
4. **Cap total open risk and per-driver exposure** — ten correlated positions are one bet.
5. **Keep a margin buffer** — a volatility spike must not force an involuntary exit.
6. **Protect against deep drawdowns** — a 50% loss needs a 100% gain to recover.
