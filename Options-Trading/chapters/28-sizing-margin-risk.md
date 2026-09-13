# 28. Position Sizing, Margin, and Risk Management

## The chapter that keeps you in the game

Options are unforgiving of poor risk management. A strategy can be sound and still be ruined by *sizing it wrong, holding it too long, or ignoring its tail*. This chapter covers the three pillars of survival: **position sizing**, **margin**, and **risk management discipline**.

## Position sizing: how much per trade

The single most important rule in trading is to **size each position so that no single loss can meaningfully hurt you**. The standard implementation is to risk a fixed, small fraction of capital per trade — commonly **1–2%** of the account per trade.

The formula is simple and applies to every defined-risk strategy in this book:

Position size = (Account × Risk % per trade) / (Maximum loss per unit)

For defined-risk positions (a long option, a vertical spread, an iron condor), the **maximum loss per unit is known at entry** — so sizing is mechanical:

- If you risk 1% of a ₹10,00,000 account (₹10,000) and the maximum loss per contract is ₹100 × lot size, you size to lose at most ₹10,000 in the worst case.

The beauty of options for risk management is exactly this: **defined-risk positions have a computable worst case.** You can know, *before entry*, the most you can lose. The discipline is to actually use that number.

### Sizing the naked (undefined-risk) positions

For the positions without a hard cap — a naked short call, a ratio spread, a short straddle — the "maximum loss per unit" is not fixed, so you cannot use the simple formula. The discipline instead is:

- **Assume a stressed scenario** — e.g., "what if the underlying gaps 10%?" — and size so that the stress-scenario loss fits the 1–2% rule.
- **Or simply avoid naked risk** until you have the experience and capital to survive it.

Most retail traders are better served by defined-risk spreads, which make sizing exact. Naked short positions are the place where accounts are most often destroyed, and almost always by a sizing error rather than a strategy error.

## Margin: the mechanics of leverage

Margin is the collateral the exchange/broker requires to hold a position. For options, it is more nuanced than for equities:

- **Buying an option** requires paying the premium in full (no additional margin) — this is one reason long options are so clean from a risk view: the premium *is* the maximum loss.
- **Selling an option** requires margin, computed under the exchange's **SPAN** system (Standard Portfolio Analysis of Risk), which models the position's worst-case loss across scenarios. Short options and spreads tie up margin until the position is closed or expires.
- **Credit spreads** are margin-efficient relative to naked shorts: the required margin is roughly the *spread width* (the max loss), not the full notional — which is why a defined-risk spread is not just safer but *cheaper to hold* than its naked equivalent.

Margin is not a cost; it is **capital locked against risk**. The practical point is that your account must have enough *free* margin to hold the position through adverse moves — a position that is "right" can still force a margin call (and an involuntary exit) if a short-term move spikes the margin requirement. **Never use all your margin.** Keep a buffer so you cannot be forced out at the worst moment.

## Risk management discipline

Sizing and margin are the *arithmetic*; discipline is the *behaviour*. The following are the rules that separate survivors from the ruined:

### 1. Define the worst case before entry

Every position — long or short — has a worst case. State it in rupees before you trade. For defined-risk positions it is the premium or the spread width; for undefined-risk positions it is a stress-scenario estimate. If you cannot state it, do not trade it.

### 2. Set a stop (or a plan) — and honour it

- For **long options**, the "stop" is often the premium itself (a total loss is bounded), but many traders still set a partial stop (e.g., exit at −50% of premium) to preserve capital for the next trade.
- For **short options and spreads**, a stop is not optional. The standard rule: *close the position when the loss reaches a pre-set multiple of the credit or the spread width* — commonly exiting a credit spread when the underlying breaches the short strike, or when the loss hits ~2× the credit.

### 3. Respect the tail

Short-volatility strategies win often and lose big. The discipline is not to *avoid* them but to **size them so the rare big loss is survivable**, and to **exit at the pre-defined point** rather than hoping for a recovery. The single most common account-destroying behaviour in options is *refusing to close a losing short position and watching it become catastrophic.*

### 4. Position-level, not just trade-level, risk

A portfolio of many "safe" small positions can still be dangerous if they are all *correlated* — e.g., five different bullish trades all express the same NIFTY-up view. The discipline is to manage **net exposure** (net delta, net vega — Chapters 11 and 25) across the whole book, not just each trade in isolation.

### 5. Size for the tail, not the expectation

The expected value of a trade can be positive while its tail is ruinous. Risk management means *sizing for the worst plausible outcome*, not the average one. This is the entire point of the 1–2% rule: it is not about maximising return, it is about *never being removed from the game.*

## The honest bottom line

Options give you the rare ability to **know your maximum loss in advance** — and the rare ability to **ignore that knowledge**. Most losses that end trading careers are not from bad strategies; they are from oversized positions, undefined exit plans, and short-vol tail risk left unmanaged. The trader who sizes correctly and honours a plan has already won the most important battle — the battle to keep playing.

## Summary

- Size each trade to risk ~1–2% of capital; defined-risk positions make this exact.
- Margin is capital locked against risk; buyers pay premium only, sellers post SPAN margin, spreads are margin-efficient.
- Keep a margin buffer so adverse moves cannot force you out.
- Define the worst case before entry; set and honour stops/exit plans, especially on short options.
- Manage net exposure across the portfolio; size for the tail, not the expectation.

Next: the psychology of options trading — the behaviour that undoes the best arithmetic.
