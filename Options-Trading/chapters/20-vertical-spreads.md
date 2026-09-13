# 20. Vertical Spreads

## Defined risk in both directions

A **vertical spread** is a position of two options of the *same type* (both calls or both puts), *same expiry*, at *different strikes* — one bought and one sold. The "spread" caps both the profit *and* the loss, turning an unbounded option position into a **defined-risk** one.

There are four vertical spreads, and they form a complete toolkit for any directional view with controlled risk:

| Spread | Structure | View | Net premium | Type |
|--------|-----------|------|-------------|------|
| Bull call | Buy lower call, sell higher call | Bullish | Debit | Debit spread |
| Bear put | Buy higher put, sell lower put | Bearish | Debit | Debit spread |
| Bull put | Sell higher put, buy lower put | Bullish | Credit | Credit spread |
| Bear call | Sell lower call, buy higher call | Bearish | Credit | Credit spread |

The debit spreads (bull call, bear put) **pay** a net premium and profit from a directional move. The credit spreads (bull put, bear call) **collect** a net premium and profit from the market *not* moving against them.

## The bull call spread

- **Structure:** buy a call at strike K₁, sell a call at a higher strike K₂ (same expiry).
- **View:** moderately bullish — you expect a rise, but not necessarily a runaway one.
- **Maximum profit:** (K₂ − K₁) − net debit.
- **Maximum loss:** the net debit paid.
- **Breakeven:** K₁ + net debit.
- **Why:** the short call at K₂ finances part of the long call at K₁, lowering cost — in exchange for capping the upside at K₂.

### Example

NIFTY at 25,000. Buy the 25,000 call for ₹150, sell the 25,200 call for ₹60. Net debit = ₹90.

- Breakeven = 25,000 + 90 = **25,090**.
- Maximum profit = (25,200 − 25,000) − 90 = **₹110** (if NIFTY ≥ 25,200 at expiry).
- Maximum loss = **₹90** (if NIFTY ≤ 25,000 at expiry).

## The bear put spread

- **Structure:** buy a put at K₂, sell a put at a lower strike K₁.
- **View:** moderately bearish.
- **Maximum profit:** (K₂ − K₁) − net debit.
- **Maximum loss:** the net debit.
- **Breakeven:** K₂ − net debit.

The mirror of the bull call, on the downside: the short put at K₁ finances the long put at K₂, capping profit at the width of the spread.

## The bull put spread (credit)

- **Structure:** sell a put at K₂, buy a put at a lower strike K₁.
- **View:** mildly bullish to neutral — the market should stay *above* K₂.
- **Maximum profit:** the net credit received (if the underlying is above K₂ at expiry).
- **Maximum loss:** (K₂ − K₁) − net credit.
- **Breakeven:** K₂ − net credit.
- **Why:** a short put is bullish, but the long put at K₁ caps the downside — this is the *defined-risk* version of the cash-secured put.

### Example

NIFTY at 25,000. Sell the 24,800 put for ₹90, buy the 24,600 put for ₹40. Net credit = ₹50.

- Breakeven = 24,800 − 50 = **24,750**.
- Maximum profit = **₹50** (NIFTY ≥ 24,800).
- Maximum loss = (24,800 − 24,600) − 50 = **₹150** (NIFTY ≤ 24,600).

## The bear call spread (credit)

- **Structure:** sell a call at K₁, buy a call at a higher strike K₂.
- **View:** mildly bearish to neutral — the market should stay *below* K₁.
- **Maximum profit:** the net credit.
- **Maximum loss:** (K₂ − K₁) − net credit.
- **Breakeven:** K₁ + net credit.

The defined-risk version of the short call: the long call at K₂ caps the otherwise unbounded upside.

## Why spreads matter: the cap you accept, the cap you gain

Every vertical spread is a trade of *one* risk for another:

- You **cap the maximum loss** (versus a naked option) — the defining advantage.
- You **cap the maximum profit** (versus a single long/short option) — the price of that protection.
- You **reduce the net cost** of a directional bet (debit spreads) or **reduce the margin** required (credit spreads).

For a trader with a view and a fixed risk budget, the vertical spread is the natural instrument: you choose how much you are willing to lose (the net debit or the spread width minus credit), and the market takes it from there.

## The Greeks of a vertical spread

Spreads partially cancel the Greeks of their legs:

- **Debit spreads** are net **long vega** (they like volatility) and have *lower* net theta than a single long option (the short leg finances time decay).
- **Credit spreads** are net **short vega** (they like calm) and are net **long theta** (time decay works for them) — but less so than a naked short, because the long leg also decays.

The practical result: a credit spread is a "softer" way to be short volatility and collect theta, with a hard floor on the loss. A debit spread is a "cheaper" way to be long volatility, with a ceiling on the gain.

## Choosing width

The **width** (K₂ − K₁) is the spread's second decision, after direction:

- **Narrow spreads** behave more like a single option — higher leverage, more sensitive, closer breakeven.
- **Wide spreads** behave more like the underlying — less leverage, more "stock-like," but a larger max loss in a credit spread.

The width is where you express *how aggressive* the position is, given the same view.

## Summary

- A vertical spread = same-type, same-expiry options at two strikes, one bought and one sold.
- Bull call / bear put = debit spreads (pay, profit from a move). Bull put / bear call = credit spreads (collect, profit from no adverse move).
- All four are defined-risk: max loss and max profit are known at entry.
- Debit spreads are long vega; credit spreads are short vega / long theta.
- Width controls aggressiveness; direction controls the view.

Next: straddles and strangles — trading *volatility*, not direction.
