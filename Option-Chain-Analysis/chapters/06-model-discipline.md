# 6. The Model-Building Discipline

## Before any model, the rules of the game

The next several chapters build *models* from the chain — delta exposure, gamma exposure, the implied distribution, the variance risk premium. Before building any of them, you need the **discipline** that keeps a model honest. This chapter is that discipline: the six rules every chain-based model must obey.

## Rule 1 — A model needs a mechanism, not just a correlation

A model is only worth building if you can answer **why** it should work, in a sentence:

- *"Max pain works because writers' hedging pulls price toward heavy-OI strikes."*
- *"GEX works because dealers' gamma hedging amplifies or dampens moves."*
- *"The variance risk premium works because investors pay up for crash protection."*

A model with a mechanism is *robust* — it will tend to keep working, because the underlying force is structural. A model without a mechanism (a pattern that "just shows up in the data") is a coin-flip waiting to fail. (This is the same discipline as the hypothesis rule of *How to Build a Framework for Systematic Trading*, applied to chain data.)

## Rule 2 — Point-in-time, or nothing

The single most common way chain models lie is **look-ahead bias** — using data that was not available at the time the signal was "generated." For the chain, the specific traps:

- **OI is *end-of-day*.** Intraday, OI is an estimate; the true, settled OI is only known after the close. A model that "trades on today's OI intraday" is using data that does not exist yet.
- **IV and the Greeks are *live*.** They change every tick; a backtest that uses the *final* IV to "predict" the *same day's* move is looking ahead.
- **Strikes come and go.** A chain today contains strikes that did not exist last month; a backtest must use the *point-in-time* chain (the strikes that actually existed on each date).

The universal test, from *How to Build a Framework for Systematic Trading*: **for every input, "did the market actually know this on this date?"**

## Rule 3 — Account for costs and the spread

Chain models are often *high-frequency* in spirit (they respond to daily OI/IV changes), which means **costs dominate**. In India, a model that churns options daily pays brokerage, STT, and — critically — the **bid-ask spread**, which on all but the most liquid contracts is a large cost. A model that ignores the spread is optimising an illusion. Always test with costs included, pessimistically.

## Rule 4 — Handle the OI attribution assumption honestly

Almost every positioning model (DEX, GEX, max pain) rests on a single, unverifiable assumption: **that OI represents positions held by option *writers* (or their market-makers).** This is a *model choice*, not a fact — OI itself does not record who is long or short. The assumption is *reasonable* (dealers are typically net writers), but it is not always true:

- In a market where retail is aggressively *buying* options, OI is *buyer* OI, not writer OI — and the model's sign flips.

The honest approach: **state the assumption explicitly, know its failure mode, and treat the model's *sign* with appropriate caution** (the *magnitude* and *structure* are usually more robust than the precise sign).

## Rule 5 — Normalise, don't read absolutes

Raw values (PCR = 1.3, GEX = +₹500 cr) are meaningless without context. A model must **normalise** its output — against the signal's own recent history (a percentile or z-score), or against a benchmark (the index's typical level). "GEX is in its lowest 5% of the last year" is a statement; "GEX is +₹500 cr" is not.

## Rule 6 — Backtest honestly, and expect decay

A chain model must be backtested with the full discipline of *Quant Trading* and *How to Build a Framework for Systematic Trading*: out-of-sample testing, parameter stress, costs included, and a clear eye on **decay**. Option-derived edges are commonly observed to be *especially* prone to decay, because they are the kind of signal that, once widely known, gets arbitraged away (a crowded max-pain trade tends to stop working). Expect any chain edge to erode, and monitor for the erosion.

## The mindset

The chain is *information-rich* — arguably the richest single data source in markets — but information-rich data is exactly where it is easiest to fool yourself. A disciplined chain modeller treats the chain as a **map of positioning** (which is honest) and is *sceptical* of every claim that it is a **map of the future** (which is where the lies creep in). The next chapters build the models; this chapter's six rules are what keep them honest.

## Summary

- A model needs a mechanism ("why"), not just a correlation.
- Point-in-time or nothing: OI is end-of-day; IV/Greeks are live; strikes come and go.
- Account for costs and the spread — chain models churn, and churn is expensive.
- The OI-attribution assumption (writers hold OI) is a model choice — state it, know its failure mode.
- Normalise against history; read percentiles, not absolutes.
- Backtest honestly, and expect decay.

Next: delta exposure and dealer positioning.
