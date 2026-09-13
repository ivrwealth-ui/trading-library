# 6. Strategy 3 — Dual Momentum

## Relative and absolute momentum, combined

**Dual momentum** — popularised by Gary Antonacci in his book *Dual Momentum Investing* (2014) — is the strategy that unites the two ideas from the previous chapters: use **relative momentum** to pick *what* to hold, and **absolute momentum** to decide *whether* to hold it. The combination is widely considered one of the most robust, practical momentum frameworks available to an individual investor.

## The idea

Each half of dual momentum solves a problem the other cannot:

- **Relative momentum** finds the strongest asset *among the options* — but it always holds *something*, so it cannot protect you when *everything* is falling.
- **Absolute momentum** steps to safety when an asset is below its own trend — but it does not tell you *which* asset to hold when conditions are good.

Dual momentum runs both: rank the assets by relative momentum, then apply an absolute-momentum filter so that if even the *strongest* asset is below its own trend, the portfolio moves to safety. The result is a strategy that **rides the strongest asset when markets are healthy and retreats to cash when they are not.**

## The rules (the canonical version)

**Universe:** a small set of distinct, liquid assets — classically, US equities, international equities, and (as the safety asset) bonds/cash. In an Indian context, a natural set is: **Indian equities (NIFTY), international equities (a global index/fund), gold, and short-duration debt/liquid funds.**

**Lookback:** trailing **12-month return** for relative momentum.

**Step 1 — Relative momentum:** each month, rank the "risk" assets (Indian equities, international equities, gold) by their trailing 12-month return and identify the **single strongest** one.

**Step 2 — Absolute filter:** compare that strongest asset's current price to its **12-month (or 200-day) moving average**. If it is **above** its trend, hold it. If **below**, hold the **safety asset** (short-duration debt / liquid funds).

**Rebalancing:** **monthly** — recompute the ranking and the filter.

**Hold:** one asset at a time. The portfolio is always in *exactly one* position: the strongest risk asset, or safety.

## Historical context

Antonacci's work — and the independent research on the two underlying components — documents that this combination has historically produced strong risk-adjusted returns across long periods and many markets, precisely because it attacks the two problems separately: relative momentum captures leadership, absolute momentum avoids bear markets. The framework has become one of the standard references for systematic tactical allocation.

Framed honestly: *historically, a dual-momentum allocation — strongest asset when it is trending up, safety when it is not — has tended to deliver equity-like returns with materially smaller drawdowns, over multi-decade horizons, across markets.*

## A worked example (an Indian allocation)

Universe: **NIFTY, a global equity index fund, gold, and liquid funds (safety).**

- At the January check, trailing 12-month returns: gold +22%, NIFTY +14%, global equities +8%.
- **Strongest risk asset:** gold. Is gold above its 12-month MA? **Yes.** → **Hold gold.**
- At the April check, the ranking has changed: NIFTY +18%, gold +9%, global +12%.
- **Strongest risk asset:** NIFTY. Above its 12-month MA? **Yes.** → **Rotate to NIFTY.**
- At the October check, markets have fallen: NIFTY −12%, global −9%, gold +3%.
- **Strongest risk asset:** gold. Above its 12-month MA? **No** (gold has also slipped below trend).
- → **Hold the safety asset (liquid funds)** — out of all risk assets during the downturn.

Result: the portfolio rode gold, then NIFTY, then stepped to safety before the worst of the decline — one asset at a time, decided monthly, with no discretion.

## Risks and limitations

- **Whipsaw and turnover.** The strategy changes position monthly, and in choppy markets it can switch frequently, each switch a small cost and a potential "buy high, sell low" on the transition.
- **Single-asset concentration.** The portfolio holds *one* asset at a time, so it is fully exposed to that asset's idiosyncratic risk in any given month.
- **The safety asset matters.** The strategy is only as good as its "safety" leg; if that leg is itself volatile, the downside protection is weakened.
- **Taxes in India.** Monthly switching between funds/ETFs can trigger short-term capital gains and exit loads, which materially affect net returns — the schedule and vehicle choice must be tax-aware.

## Summary

- Relative momentum picks the strongest asset; absolute momentum gates it behind a trend filter.
- One position at a time: the strongest risk asset, or safety.
- Historically equity-like returns with smaller drawdowns (Antonacci).
- Risks: whipsaw, concentration, the quality of the safety leg, and tax/exit-load costs in India.

Next: Strategy 4 — 52-week high investing.
