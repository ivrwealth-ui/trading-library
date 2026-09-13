# 7. Strategy 4 — Relative Strength Rotation

## Trade the strongest, ignore the weakest

The three strategies so far buy *individual* breakouts or trends. **Relative strength (RS) rotation** takes a portfolio view: it *ranks* a universe of instruments by recent performance and holds the **strongest** few, rotating into them on a schedule. It is momentum applied as a *selection* problem rather than a *timing* problem.

## The idea

At any moment, some sectors and stocks are leading and others are lagging. RS rotation formalises an old truth: **leadership persists.** The stocks that led over the last few months have historically tended to keep leading over the next few — so a portfolio that *owns the leaders and re-ranks periodically* systematically holds strength and drops weakness.

The mechanics come straight from the academic momentum factor (Jegadeesh & Titman): rank on past returns (often 3–12 months), hold the top decile, rebalance. RS rotation is that factor, applied to a practical, manageable universe.

## The rules

**Universe:** a set of liquid instruments — e.g., the NIFTY 500, or a defined list of ~20–50 liquid stocks, or a basket of sector/theme indices. Fewer positions than the full universe.

**Ranking window:** compute each instrument's **trailing return over the lookback** (commonly 3, 6, or 12 months).

**Selection:** rank by trailing return and hold the **top N** (e.g., the top 10, or the top quartile).

**Rebalancing:** repeat the ranking **on a fixed schedule** — monthly is common — replacing the instruments that fell out of the top with those that entered.

**Exit / rotation rule:** an instrument is sold *when it falls out of the top group* at the rebalance — not on a price stop. The strategy is always "holding the strongest."

**Optional absolute filter:** hold cash (or the index) when the *broad market* is itself below its 200-day MA — because momentum rotation is a long-only strategy that suffers in broad bear markets.

## Historical context

Relative-strength ranking *is* the cross-sectional momentum factor in its purest form, and that factor is among the most replicated in finance. The canonical result: buying past winners and selling past losers has historically earned a persistent premium across markets and decades. In Indian markets specifically, "buying the outperformers and rotating monthly" has been a standard, widely-used quant construction — though, as always, costs and the specific universe matter greatly.

## A worked example (NIFTY sectors)

- Universe: 12 NSE sector indices. Lookback: 6-month trailing return. Hold the top 4.
- At the January rebalance, the top 4 by 6-month return are Banking, IT, Auto, and Capital Goods. The portfolio holds these four, equal-weighted.
- Over the next month, IT weakens and Pharma surges. At the **February rebalance**, Pharma has entered the top 4 and IT has dropped out.
- The portfolio **sells IT, buys Pharma** — mechanically following strength — and continues this monthly rotation.

The result is a portfolio that is *always* tilted toward whatever is working, without the trader needing any opinion about *why*.

## Risks and limitations

- **Turnover and costs.** Monthly rotation means frequent trades; STT, brokerage, and impact costs eat returns. The strategy must be run on *liquid* instruments and with cost discipline, or the edge is lost to fees.
- **Whipsaw at the boundary.** Instruments hovering near the "top N" cutoff get repeatedly bought and sold. A slightly larger N (or a small buffer) reduces this.
- **Bear markets.** Long-only momentum rotation loses in broad downturns — everything falls, just at different speeds. The absolute (200-day) filter is the standard defence.
- **Crowding.** As momentum rotation became popular, the strongest names became crowded, which can compress or reverse the edge in certain regimes.

## Summary

- Rank a universe by trailing return; hold the strongest N; rebalance monthly.
- Pure cross-sectional momentum — the most replicated factor in finance.
- Always tilted toward leadership, with no opinion on *why*.
- Turnover costs and bear markets are the two main risks; filter and cost discipline are the fixes.

Next: Strategy 5 — the pullback to the rising moving average.
