# 9. Why Trade Options: Hedging, Income, and Speculation

## Three motives, one instrument

Options are used for three broad purposes, and a great deal of confusion dissolves once you identify which one you are actually pursuing.

1. **Hedging** — using options to *protect* an existing position or portfolio against adverse moves.
2. **Income** — using options to *collect* premium over time.
3. **Speculation** — using options to *express a directional or volatility view* with leverage.

Most of this book's strategies map cleanly onto one of these three. The discipline is in knowing which one you are doing — because mixing them up is the source of most beginner mistakes.

## Hedging: the insurance use

The classic hedge is the **protective put** (Chapter 24): an investor who owns a portfolio buys index puts, so that if the market falls sharply, the puts gain in value and offset the loss.

Options are a uniquely precise hedging tool for three reasons:

- **They cap the loss at a known level** — the investor knows the maximum downside, just as an insurance policy has a deductible.
- **They preserve upside** — unlike selling the position, a hedge keeps the position's gains if the market rises.
- **They can be sized exactly** — one can buy just enough put protection to match the exposure one wants to insure.

Hedging is the most "grown-up" use of options, and it is what derivatives were originally designed for. Note that hedging is *not* free: the premium paid is the cost of the insurance, and over long periods the cost of repeated hedges can meaningfully reduce returns — which is precisely why options are a trade-off, not a free lunch.

## Income: the rent-collection use

Selling options — covered calls, cash-secured puts, credit spreads (Chapters 19–20, 22) — is a way to *collect premium* as a form of income. The seller is effectively earning "rent" on a position they hold or are willing to hold.

The income use is attractive because, statistically, most OTM options **expire worthless** — the seller wins the "most of the time" bet. But the income is collected *in exchange for* the risk of the rare large loss, which is why income strategies are described as "picking up pennies in front of a steamroller": the steady small gains can be wiped out by one outsized move.

This is not an argument against income strategies — it is the reason they must be **defined-risk** (spreads) or **asset-backed** (covered) rather than naked, and why their practitioners care deeply about the tail risk that the "most of the time" framing hides.

## Speculation: the leveraged-view use

Options allow a trader to express a view — up, down, or "volatile" — with **defined risk and leverage**. A long call lets a trader participate in a rally while risking only the premium; a straddle lets a trader profit from a large move *without predicting its direction*.

Two features make options uniquely suited to speculation:

- **Leverage with a floor** — unlike futures or margin equity (where losses can exceed the initial stake), a long option's loss is capped at the premium.
- **Views on volatility, not just direction** — options are the only instrument where you can profit from *how much* the market moves, independent of *which way*.

The flip side of speculation is time decay: the option is a *wasting* asset. A directional view that is right but arrives *late* (or is right but arrives *with low volatility*) can still lose money. Speculating with options demands being right about direction, magnitude, *and* timing — or explicitly trading volatility (Chapter 25).

## The honest framing

This book repeatedly makes a distinction worth stating plainly here:

- **Hedging** transfers risk you already have.
- **Income** sells risk you are willing to absorb, for a premium.
- **Speculation** buys risk you want exposure to, for a premium.

None is morally or mathematically superior; they are different contracts with different risk profiles. The skilled trader is the one who *chooses deliberately* which role to play in each trade — and who never accidentally becomes a naked seller while thinking they are a hedger.

## Which motive is right for you?

This is a question only you can answer, but the question itself is the point. A useful self-check before any trade:

- Am I **protecting** something I own? → hedging.
- Am I **earning a premium** I believe will decay to zero? → income.
- Am I **betting** on a price or volatility move? → speculation.

Each motive implies different instruments, different sizing, and different risk limits. Returning to this question is the single best guard against the most common error in options: *using the wrong tool for the view you actually hold*.

## Summary

- Three motives: hedging (protect), income (collect premium), speculation (leveraged view).
- Hedging caps downside while preserving upside, at the cost of premium.
- Income strategies win "most of the time" but carry tail risk — manage it with defined risk.
- Speculation uses defined risk and leverage, but must overcome time decay.
- Know which role you are playing before you place the trade.

This completes Part I. Next, Part II turns to the analytical engine: what actually moves an option's price.
