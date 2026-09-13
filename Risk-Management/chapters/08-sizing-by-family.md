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
