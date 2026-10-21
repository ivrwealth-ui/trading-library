# Option Chain Analysis: Reading Positioning and Building Quant Models from the Chain

## From open interest, PCR, and max pain to gamma exposure, the implied probability distribution, and the variance risk premium — the complete guide to deriving quantitative models from the option chain, with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading in options and derivatives involves substantial risk of loss, including the possible loss of principal and (for short options) the potential for very large losses. Past performance never guarantees future results.
- All models, formulas, examples, and historical observations are illustrative. A model is a *simplification of reality* — it describes tendencies and probabilities, never certainties, and every model in this book has known failure modes (detailed in Chapter 14).
- Open interest, implied volatility, and derived signals are computed from data that can be delayed, incomplete, or point-in-time inconsistent; always verify against current exchange data before any decision.
- Nothing in this book should be read as a promise of profit or a guarantee that any model will predict the market.

By reading this book, you agree that you are solely responsible for your own trading and investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches **option chain analysis** — reading the option chain's data (open interest, volume, implied volatility, and the Greeks) as a *map of market positioning* — and then building **quantitative models** from that data. It is the natural companion to *The Complete Options Trader* in this series (which covers the instruments and strategies); this book covers the *information* the chain contains.

- **Chapters 1–5** build the reading layer: the chain as a data structure, open interest as a positioning map, the put-call ratio, implied-volatility structure (skew and term structure), and max pain.
- **Chapters 6–12** build the *models*: the model-building discipline, delta exposure and dealer positioning, gamma exposure (GEX), the implied probability distribution, the variance risk premium, the expected move, and option-implied support/resistance.
- **Chapters 13–14** put it together — combining signals into a composite model — and cover the data-quality pitfalls that make every such model fail if ignored.
- The **appendix** is a formula reference and a table of every chain-derived signal.

A note on language: this book describes what the chain *shows* and how models *are built* — never what you "should" trade. Every signal is framed as a tendency, not a promise. You are responsible for your own decisions.

---

## Table of Contents

1. The Option Chain as a Data Structure
2. Open Interest: The Positioning Map
3. The Put-Call Ratio and Its Two Faces
4. Implied Volatility: Skew and Term Structure
5. Max Pain and Expiry Pinning
6. The Model-Building Discipline
7. Delta Exposure and Dealer Positioning
8. Gamma Exposure (GEX)
9. The Implied Probability Distribution
10. Realised vs. Implied: The Variance Risk Premium
11. The Expected Move and Event Pricing
12. Option-Implied Support and Resistance
13. Combining Signals into a Composite Model
14. Data Quality, Pitfalls, and Failure Modes

Appendix — Formula Reference and Signal Table

---


# 1. The Option Chain as a Data Structure

## A spreadsheet of the market's expectations

Before it is a picture, an **option chain** is a *data structure*: a table with one row per strike, and columns holding, for each strike, the prices, open interest, volume, and Greeks of the calls and puts. Everything in this book — every model — is built by *transforming* that table. So the first step is to understand the raw material precisely.

## The columns that matter

For each strike (row), the chain holds, for the **call** and the **put**:

| Column | Meaning | What it measures |
|--------|---------|------------------|
| **LTP / bid / ask** | Last, bid, ask price | Cost, and the spread (a real cost) |
| **Open interest (OI)** | Outstanding contracts | *Positioning* — where capital sits |
| **Volume** | Contracts traded today | *Activity* — what is being traded now |
| **Implied volatility (IV)** | The vol that fits the price | The market's *expected move*, standardised |
| **Delta (Δ)** | d price / d spot | Directional exposure (≈ P(ITM)) |
| **Gamma (Γ)** | d delta / d spot | How delta changes (convexity) |
| **Vega (ν)** | d price / d IV | Sensitivity to volatility |
| **Theta (Θ)** | d price / d time | Time decay |

The chain is, in effect, the market's **full set of simultaneous expectations**: at every strike and expiry, the price *is* the market's consensus about the distribution of future prices. The entire art of this book is *recovering* that consensus from the table.

## OI vs. volume: the crucial distinction

The single most important distinction in the chain, and the one most models rest on:

- **Volume** counts contracts traded *during* a period — it is *activity*, and it resets each day.
- **Open interest (OI)** counts contracts *still outstanding* at the end of a period — it is *positioning*, and it accumulates and decays as positions are opened and closed.

The distinction matters because they answer different questions:

- **Volume** answers "what is being *traded* right now?" (flow, churn, day-trading activity).
- **OI** answers "where does *capital sit*?" (conviction, positioning, the "footprint" of the market).

Most of the models in this book — PCR, max pain, GEX, the positioning maps — are built on **OI**, precisely because OI is the *persistent* footprint, while volume is transient.

## The chain is a *surface*, not a line

A single expiry is one slice. The full option market is a **surface**: IV (and OI) as a function of *both* strike and expiry.

- **Across strikes** (one expiry): the **skew/smile** — how IV changes as you move from ITM to OTM.
- **Across expiries** (one strike): the **term structure** — how IV changes as you move from near to far expiry.

Chapter 4 treats both. For now, hold the mental model: **the chain is a two-dimensional surface of expectations, and every model in this book is a way of reading one slice or one aggregate of that surface.**

## From raw chain to derived signal

The models in this book share a common pipeline:

```
raw chain (price, OI, IV, Greeks per strike)
        ↓  aggregate / transform
derived signal (PCR, max pain, GEX, implied distribution, ...)
        ↓  interpret + combine
a positioning read or a forecast
```

The raw chain is *descriptive* (it is what it is); the derived signal is *analytic* (it is a summary with meaning); the interpretation is *judgement*. The rest of this book walks that pipeline, one derived signal at a time.

## The honest starting caveat

Two caveats frame everything that follows:

1. **The chain shows positioning, not intention.** OI tells you *where capital sits*, not *why* it sits there, and not *who* holds it (a large call OI could be speculation, or a hedge against short stock). The models read the *footprint*, not the *mind*.
2. **The chain is only as good as its data.** Expiries with sparse trading, stale IV, or thin OI produce garbage inputs — and garbage in means garbage out (Chapter 14 is devoted to this).

## Summary

- The chain is a table: per strike, the call/put prices, OI, volume, IV, and Greeks.
- OI = positioning (persistent footprint); volume = activity (transient flow). Most models use OI.
- The chain is a *surface* of expectations across strikes (skew) and expiries (term structure).
- The pipeline is always: raw chain → aggregate/transform → derived signal → interpret.
- The chain shows positioning, not intention; and it is only as good as its data.

Next: open interest — the positioning map.


# 2. Open Interest: The Positioning Map

## Where capital sits

**Open interest (OI)** is the number of outstanding contracts at each strike. Read as a whole, the OI *distribution* across strikes is a map of where the market's capital is positioned — a footprint of conviction. This chapter covers how to read that map, and the single most-used OI signal: **OI change combined with price.**

## The OI distribution: walls and valleys

Plot OI against strike for a single expiry, and you get a **distribution** — typically with distinct features:

- **OI "walls"** — strikes with unusually high OI (far above their neighbours). A wall is a level where a great deal of capital is *committed* — often because option *writers* have sold heavily there.
- **The ATM hump** — OI is naturally highest near the money, where most trading and writing happens, and thins out into the wings.

The walls are the interesting part, because they are *significant levels*:

- A **call OI wall above spot** is often read as **resistance** — a level where many call writers are positioned (profiting if price stays below), and where the market may struggle to push through.
- A **put OI wall below spot** is often read as **support** — a level where many put writers are positioned, and where the market may find a floor.

Chapter 12 treats these levels as a full model; for now, hold the idea: **high-OI strikes are levels the market is watching.**

## The four-quadrant OI + price read

The single most-used OI signal is the combination of **price direction** with **OI change**. For a given contract (or the index as a whole):

| Price | OI change | Interpretation |
|-------|-----------|----------------|
| Up | Up | New *longs* being added (bullish flow) |
| Up | Down | Short covering (positions unwinding) |
| Down | Up | New *shorts* being added (bearish flow) |
| Down | Down | Longs liquidating (bearish flow) |

The logic: rising OI means *new positions* are being opened (fresh money entering); falling OI means *existing positions* are being closed. Combine that with which way price moved, and you have a read on whether the new money (or the exiting money) is bullish or bearish.

**The honest caveat:** this is a *heuristic*, not a law. It reads the *net* change in OI, which is the sum of many individual decisions — and it says nothing about *who* (buyer vs. seller, hedger vs. speculator). It is a useful *first approximation* of flow, not a precise instrument-by-instrument accounting.

## OI change at the strike level

The four-quadrant read applies *per strike*, which is where it becomes actionable:

- A strike seeing **rising call OI with rising price** is being *bought* (bullish demand at that level).
- A strike seeing **rising put OI with falling price** is being *bought* (bearish demand / hedging at that level).
- A strike seeing **falling OI** is being *closed* — which, at a wall, can mean a level that was defended is being abandoned.

Scanning the *change* in OI across the strike ladder — not just the level — tells you *where new capital is flowing in* and *where it is leaving*. That is the difference between a static snapshot and a live read.

## OI as a magnet: the pinning effect

One of the most useful (and most widely reported) properties of OI is its **magnetic effect near expiry**: the market tends to *gravitate toward* strikes with the heaviest OI. The mechanism is the behaviour of option *writers* (and the market-makers who hedge them): they profit most if options expire worthless, and their hedging activity tends to *pull* price toward the levels where the most options would expire worthless.

This is the foundation of **max pain** (Chapter 5) and of the support/resistance models (Chapter 12). The practical upshot: **heavy OI is not just "where capital sits" — it is a force that can shape where price goes.**

## Reading the OI map: a routine

A disciplined OI read for a NIFTY expiry:

1. **Locate the walls** — the strikes with OI far above their neighbours (call walls above spot, put walls below).
2. **Note the ATM hump and the wing density** — is the OI concentrated near the money (a range-bound market) or spread into the wings (a market expecting a big move)?
3. **Read the day's OI *change*** — where is fresh capital entering, where is it leaving?
4. **Combine with price** — the four-quadrant read, at the index level and at the key strikes.

This routine turns the OI table from a wall of numbers into a *map of positioning and flow* — the raw material for every model that follows.

## Summary

- OI distribution across strikes is a positioning map; walls are significant levels (call wall = resistance, put wall = support).
- OI + price gives the four-quadrant flow read: price up/down × OI up/down = longs/shorts entering or leaving.
- OI change at the strike level shows where new capital flows in and out.
- Heavy OI has a magnetic "pinning" effect near expiry.
- The routine: walls → concentration → OI change → combine with price.

Next: the put-call ratio — sentiment, and its two faces.


# 3. The Put-Call Ratio and Its Two Faces

## One number, two readings

The **put-call ratio (PCR)** is the most famous single number in option chain analysis: the ratio of put activity to call activity. It condenses the market's *bearish vs. bullish* option positioning into one figure — and it has **two readings that point in opposite directions**, which is exactly why it is both powerful and dangerous.

## The definition (and the two versions)

There are two standard PCRs, and they answer different questions:

- **PCR (OI-based)** = total put open interest ÷ total call open interest. It measures *positioning* — where capital sits, persistently.
- **PCR (volume-based)** = total put volume ÷ total call volume. It measures *flow* — what is being traded today.

The OI version is the more stable, "conviction" measure (this book's focus); the volume version is the more reactive, "mood-of-the-day" measure. Both are useful; know which you are looking at.

## The two faces: trend vs. contrarian

Here is the crux. The PCR can be read in two opposite ways:

### Face 1 — the "positioning" reading (trend-following)

A **high PCR** (more puts than calls) means the market is positioned bearishly — investors are buying protection or betting on a decline. Read *straight*, a rising PCR = growing bearishness = a bearish signal.

### Face 2 — the "contrarian" reading (mean-reversion)

A **very high PCR** can also mean *everyone has already* bought their puts — the bearishness is *exhausted*, the "sell" is done, and the market is ripe to reverse *up*. Read *contrarian*, an extreme PCR is a *bullish* signal (and an extremely low PCR is a *bearish* one).

Both readings are legitimate; the difference is **the level**:

- **Mid-range PCR** — read it *with the trend* (a rising PCR = building bearishness).
- **Extreme PCR** — read it *contrarian* (a very high PCR = crowded bearishness, likely to snap back).

The practical problem — and the reason PCR alone is a weak signal — is that "extreme" is **regime-dependent**: a PCR of 1.3 might be extreme in a calm bull market but normal in a stressed bear market. PCR only becomes meaningful when read **relative to its own recent history** (its percentile), not as an absolute number.

## Building a usable PCR signal

A disciplined PCR model therefore does three things:

1. **Normalise** — compute the PCR's *percentile* (or z-score) over a rolling window (e.g., 60–250 days), so "extreme" is defined against the market's *own* behaviour, not a fixed number.
2. **Combine the two faces** — read the *level* for the trend signal and the *extreme* for the contrarian signal, explicitly rather than ambiguously.
3. **Confirm with price** — a PCR extreme that coincides with price action (a high PCR at a market *low*, a low PCR at a market *high*) is far more meaningful than a PCR extreme in isolation.

## The honest limitations

Three things PCR does *not* do, stated plainly:

1. **It does not know *why*.** A high PCR could be speculation (bearish bets) or *hedging* (investors buying puts to protect long stock). The hedging case is not bearish at all — it is *protective*. PCR conflates the two, which is why it is a weak signal on its own.
2. **It is not directional on its own.** The two-faces problem means a raw PCR number, without its percentile, is ambiguous — and ambiguity is not a signal.
3. **It is a positioning gauge, not a forecast.** PCR describes *where sentiment is*; it does not reliably predict *where price goes next*. It is a *context* input, to be combined with other signals (Chapter 13), not a standalone call.

## Summary

- PCR = puts ÷ calls; OI-based measures positioning, volume-based measures flow.
- Two faces: trend-following (mid-range) vs. contrarian (extreme).
- "Extreme" is regime-dependent — normalise to the PCR's own percentile.
- A usable signal: normalise, combine both faces, confirm with price.
- PCR does not know *why*, is not directional alone, and is a context input, not a forecast.

Next: implied volatility — skew and term structure.


# 4. Implied Volatility: Skew and Term Structure

## The chain's most information-dense field

The **implied volatility (IV)** at each strike is the single most information-dense number in the chain: it is the volatility that makes the option's *market price* equal its model price (Black-Scholes, from *The Complete Options Trader*). Because it is a *standardised* price of uncertainty, IV can be compared across strikes and expiries — and the *pattern* of IV across the chain is a rich signal in its own right. This chapter covers the two dimensions of that pattern: **skew** and **term structure**.

## Skew: IV across strikes (one expiry)

Plot IV against strike for a single expiry, and you do *not* get a flat line. In equity/index markets, you get a **skew** — a curve, typically shaped like a *smile* or *smirk*:

- **OTM puts carry higher IV** than equidistant OTM calls. Downside protection is *expensive*; upside calls are comparatively *cheap*.

**Why:** investors systematically buy downside protection (puts), bidding up their price — and therefore their IV. The market prices crashes as more likely than a normal (lognormal) distribution would suggest: the "fat left tail." This is not an inefficiency to be arbitraged away; it is a *persistent structural feature* of the market, reflecting the real, rational demand for crash protection.

### A quantitative skew measure: the risk reversal

The standard way to *measure* skew in one number is the **risk reversal** — the difference between the IV of an OTM call and an OTM put at a fixed delta (commonly 25-delta):

Risk reversal (25Δ) = IV(25Δ call) − IV(25Δ put)

- **Negative risk reversal** (puts richer than calls) is the *normal* state in equity/index markets — the market is structurally paying up for downside protection.
- A risk reversal that *steepens* (more negative) = growing fear/hedging demand.
- A risk reversal that *flattens or flips positive* = rising bullishness (calls bidding up).

The risk reversal is a clean, single-number read of *where the fear is concentrated* — and of how it changes over time.

## Term structure: IV across expiries (one strike)

Plot IV against expiry, and you get the **term structure**:

- **Contango (normal, calm):** longer-dated options have *higher* IV than shorter-dated. Uncertainty compounds with time, so more time = more priced-in uncertainty.
- **Backwardation (stress):** near-dated IV *spikes above* far-dated IV. Fear is concentrated in the *immediate* future — the classic signature of an event or a panic.

The term structure tells you *when* the market expects the uncertainty to be:

- **Contango** = "things are calm; uncertainty is spread evenly into the future."
- **Backwardation** = "something is about to happen *now*."

## Why skew and term structure matter for models

Both are inputs to the deeper models in this book, and both are *signals* in their own right:

1. **Skew measures *tail risk demand*.** A steepening skew means the market is paying up for downside protection — a real-time measure of fear, arguably more informative than a headline sentiment survey.
2. **Term structure measures *event concentration*.** Backwardation flags an imminent, priced-in event (a budget, an election, a rate decision) — and it tells you the event is *near*, not far.
3. **Both feed the implied distribution (Chapter 9) and the variance risk premium (Chapter 10).** The surface's shape is the raw material those models consume.

## Reading the surface: a routine

A disciplined IV read of the chain:

1. **Level** — is IV (at the money) high or low relative to its own history (IV rank/percentile, from *The Complete Options Trader*)?
2. **Skew** — what is the risk reversal, and is it steepening (fear building) or flattening (fear easing)?
3. **Term structure** — contango (calm) or backwardation (event near)?

Together these three answer: *is the market cheap or expensive to insure (level), where is the fear concentrated (skew), and when is the uncertainty expected (term structure)?* That is a remarkably complete picture of market expectation, recovered entirely from the chain's IV field.

## Summary

- IV is a standardised price of uncertainty, comparable across strikes and expiries.
- Skew = IV across strikes; equity markets show a skew (smirk) — OTM puts richer than OTM calls.
- The risk reversal (25Δ call IV − 25Δ put IV) measures skew in one number; steepening = growing fear.
- Term structure = IV across expiries; contango = calm, backwardation = event near.
- Level + skew + term structure = a complete picture of market expectation.

Next: max pain and expiry pinning.


# 5. Max Pain and Expiry Pinning

## Where the market's option writers lose the least

**Max pain** is the strike price at which the *largest number of options would expire worthless* — or, as defined below, the price at which option **writers** (in aggregate) lose the least, and option **buyers** (in aggregate) lose the most. It is the chain's answer to a specific question: *where would the market's option positioning most like price to settle?*

## The definition, precisely

For a candidate expiry price K, the total "pain" paid out to option holders is the sum of every ITM option's intrinsic value, weighted by its open interest:

Total pain(K) = Σᵢ [ OI_call(Kᵢ) × max(K − Kᵢ, 0) + OI_put(Kᵢ) × max(Kᵢ − K, 0) ]

where the sum is over all strikes Kᵢ, and `max(...)` is each option's *intrinsic value* if the underlying expires at K.

**Max pain** is the strike K that **minimises** total pain(K). It is the settlement price at which option writers (collectively) pay out the least — and therefore the price they would, if they could influence it, "prefer".

## Why it works: the pinning mechanism

The empirical observation behind max pain is **expiry pinning**: in liquid index options, the underlying often *gravitates toward max pain as expiry approaches*. The mechanism is the hedging behaviour of the large writers (and their market-makers):

- Option writers profit most when options expire worthless.
- The market-makers who hedge writers' positions buy and sell the underlying in ways that, in aggregate, **pull price toward the strikes with the heaviest OI** — i.e., toward max pain.

This is the same magnetic effect described in Chapter 2, made precise: max pain is the *single* strike that the OI-weighted payout structure most "wants" price to land on.

## How to compute and use it

The computation is mechanical (and covered in the appendix formula reference). Practically:

1. Compute total pain(K) for each strike in the chain.
2. Find the K that minimises it — that is max pain.
3. **Use it as an *expiry-day* reference point** — the level price is "pulled toward" as the clock runs out.

**The honest scope:** max pain is a *near-expiry* concept. Far from expiry, it is weak and unreliable; in the final days, the pinning effect is strongest and most usable.

## The honest limitations

Three caveats that prevent max pain from being over-trusted:

1. **It is descriptive, not prescriptive.** Max pain tells you where writers *would like* price to go; it does not *cause* price to go there. The pinning effect is a commonly observed tendency — but it is a *tendency*, frequently overridden by genuine news and flows.
2. **It is a single number that hides a lot.** The "pain" function is often *flat* around its minimum — a broad zone of near-minimal pain, not one sharp point. Max pain is a *zone*, not a precise target.
3. **It ignores the underlying's own direction.** A market with strong directional momentum will blow straight through max pain. Max pain matters most in *calm, range-bound* expiries; it is weakest exactly when the market is moving decisively.

## Max pain in a broader model

Max pain is best used **as one input among several**, not as a standalone forecast. In a composite model (Chapter 13), it contributes the *"expiry gravity"* term — the level the market is pulled toward — which is then read alongside the *directional* signals (delta exposure, GEX) and the *sentiment* signals (PCR, skew). Alone, max pain is a curiosity; combined, it is a useful reference for expiry-week positioning.

## Summary

- Max pain = the strike minimising the OI-weighted total intrinsic payout — where writers lose least.
- The pinning mechanism: writers/market-makers' hedging pulls price toward heavy-OI strikes.
- Compute total pain(K) per strike; find the minimum; use it as an expiry-day reference.
- It is descriptive, often a *zone* not a point, and weakest when the market is moving decisively.
- Use it as one input (expiry gravity), not a standalone forecast.

Next: the model-building discipline that frames everything that follows.


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


# 7. Delta Exposure and Dealer Positioning

## The directional tilt of the option book

The first model built directly from the chain's Greeks is **delta exposure (DEX)**: the *net directional exposure* of all outstanding options, attributed to the dealers (market-makers) who are their counterparties. It answers a precise question: *if the underlying moves, in which direction — and with how much force — will dealers be forced to trade to stay hedged?*

## The building block: option delta

Recall (from *The Complete Options Trader*) that every option has a **delta** — the rate of change of its price with respect to the underlying:

- Calls: delta runs **0 to +1** (ITM calls approach +1).
- Puts: delta runs **−1 to 0** (ITM puts approach −1).

A long call is *long* the market; a long put is *short* the market. The chain's OI, combined with these deltas, tells you the *net* directional position embedded in the option market.

## The dealer-short convention

OI does not record who is long and who is short. The standard model makes an assumption (Chapter 6, Rule 4): **dealers are the *net sellers* of options** — they write options to provide liquidity, and the OI represents, in aggregate, *dealer short* positions.

Under this convention, the dealer's delta on each contract is the *negative* of the holder's:

Dealer delta of a call at strike K = **− OI(K) × Δ_call(K)**

Dealer delta of a put at strike K = **− OI(K) × Δ_put(K)**  (and since Δ_put is negative, this is *positive*)

Summed over all strikes, and multiplied by the contract notional (spot × lot size), we get the **net delta exposure**:

DEX = **− Σₖ [ OI_call(K) × Δ_call(K) + OI_put(K) × Δ_put(K) ] × (spot × lot)**

The result is a single number, in rupees of notional: the market's *net directional exposure* from the dealers' perspective.

## Reading DEX

The sign and size of DEX describe the **directional tilt** of the dealer book — and, therefore, the *flows* that would result if price moves:

- **DEX strongly negative** (dealers net *short* delta — i.e., the market is net long calls): to stay neutral, dealers hold a **long** hedge in the underlying. If the market rises, their short calls gain delta and they must **buy** more of the underlying — adding *upward* fuel to the rally. If it falls, they sell (de-hedge), adding downward fuel.
- **DEX strongly positive** (dealers net *long* delta — the market is net long puts / short the market): dealers hold a **short** hedge in the underlying. Because they are short those puts, they are short gamma too: if the market falls, the puts gain delta and dealers must **sell** more — adding *downward* fuel to the decline; if it rises, they buy back part of their hedge, adding upward fuel.

In both cases DEX tells you the *size and direction* of the dealers' hedge; *how* that hedge changes as price moves — and whether the hedging amplifies or dampens the move — is gamma, the subject of Chapter 8.

More useful than the raw sign is the **change** in DEX: a sharp *shift* in delta exposure (e.g., from net short to net long) marks a change in the market's directional conviction, and a potential inflection point.

## DEX vs. GEX: two different questions

It is worth separating the two, because they are often confused:

- **DEX (delta exposure)** answers: *what is the market's net directional tilt, and therefore the direction of hedging flows?* It is a **first-order** measure — about *direction*.
- **GEX (gamma exposure, next chapter)** answers: *how does that tilt change as the market moves, and does dealer hedging amplify or dampen moves?* It is a **second-order** measure — about *reflexivity*.

DEX is the "position" read; GEX is the "how it behaves" read. Both are built from the same OI × Greek × notional machinery; they just multiply by delta (DEX) or gamma (GEX).

## A worked example (conceptual)

Consider a simplified NIFTY chain where the dominant feature is **heavy call OI above spot** (investors have bought calls; dealers are short those calls):

- Dealer delta from the short calls is **negative and large** (dealers are short the market via short calls).
- DEX is therefore **strongly negative**.
- Interpretation: the option book is *tilted bullish* (net long calls), and if NIFTY rallies, dealers will be **forced to buy** to hedge — which can *accelerate* the rally (the "short gamma/delta squeeze" dynamic, quantified in the next chapter).

This is the first taste of why positioning matters: the chain does not just *reflect* the market's view; it contains **latent buying or selling pressure** that can move the market when price reaches the relevant levels.

## The honest caveats

1. **The dealer-short assumption is a model, not a fact** (Chapter 6, Rule 4). If the OI is actually *buyer*-dominated (a retail buying frenzy), the sign flips. Treat the sign cautiously; the *structure* (where the exposure concentrates) is more robust.
2. **DEX is a snapshot, not a forecast.** It describes the *current* tilt; it does not, by itself, predict the direction of the next move — it predicts the direction of *hedging flows* *if* the market moves.
3. **It is one input.** DEX is most useful *combined* with GEX (next chapter) and the sentiment signals (PCR, skew) into a composite view (Chapter 13).

## Summary

- DEX = the net directional exposure of the option book, from the dealers' perspective, in ₹ notional.
- Built as −Σ (OI × delta) × spot × lot, over all strikes (dealer-short convention).
- Negative DEX = dealers short delta (market net long) → forced buying on rallies.
- DEX is first-order (direction); GEX is second-order (reflexivity).
- It is a snapshot of latent hedging pressure, not a forecast — and the sign rests on the dealer-short assumption.

Next: gamma exposure (GEX) — the reflexivity model.


# 8. Gamma Exposure (GEX)

## The reflexivity model

**Gamma exposure (GEX)** is the most discussed positioning model in modern options analysis — and the most abused. It measures the **net gamma of the dealer book**, and its sign tells you whether dealer hedging is **stabilising** or **amplifying** market moves. It is, in a precise sense, the chain's answer to "how *reflexive* is this market right now?"

## The building block: option gamma

Gamma (from *The Complete Options Trader*) is the rate of change of delta — the option's *convexity*. It is:

- **Positive** for option *buyers* (both calls and puts) — their delta grows in the direction of a move.
- **Negative** for option *sellers* — their delta grows *against* them as the market moves.
- **Highest at the money** and near expiry — where uncertainty is most concentrated.

The chain's gamma, combined with OI, tells you how *much* convexity is embedded in the market, and on which side.

## The formula

Under the same dealer-short convention as DEX (dealers are net writers), the dealer's gamma on each contract is the *negative* of the holder's:

GEX at strike K = **− OI(K) × Γ(K) × lot × spot² × 0.01**

Net GEX = **Σₖ [ − OI_call(K) × Γ_call(K) − OI_put(K) × Γ_put(K) ] × lot × spot² × 0.01**

The result is a single number — the total dealer gamma, in **rupees per 1% move of the underlying**. (The "spot² × 0.01" term turns "gamma per point" into "rupees of hedging flow per 1% move": a 1% move is 0.01 × spot points, which changes delta by Γ × 0.01 × spot, and each unit of delta is worth spot rupees.)

## Reading the sign: the two regimes

The sign of GEX is the whole story, because it determines *how dealers hedge* — and dealer hedging is a real, self-reinforcing force:

### GEX > 0 (dealers net *long* gamma)

When dealers are long gamma, they hedge **counter-cyclically**: they **buy when the market falls and sell when it rises** (to stay delta-neutral). This behaviour **dampens** moves — the market is *stabilised*, volatility is suppressed, and price tends to **pin** around heavy-OI strikes.

**Signature: low realised volatility, range-bound trading, "quiet" markets.**

### GEX < 0 (dealers net *short* gamma)

When dealers are short gamma, they hedge **pro-cyclically**: they **buy when the market rises and sell when it falls** (chasing the move). This behaviour **amplifies** moves — every move is *reinforced* by dealer hedging, and volatility can expand rapidly, especially if price moves into a region of concentrated negative gamma.

**Signature: high/rising realised volatility, "violent" markets, and the potential for sharp, self-reinforcing moves.**

## The "gamma flip" level

A refinement that makes GEX *spatially* useful: plot **GEX against strike** (or against the underlying's price), and find where it **flips sign**. That level — where dealer hedging switches from dampening to amplifying (or vice versa) — is a meaningful zone:

- Price *above* the flip (in positive-GEX territory) is stabilised; price falling *below* it into negative-GEX territory can accelerate.
- The flip level often acts as a **magnet or a cliff** — a level the market is drawn toward, and where behaviour can change abruptly.

The flip level is, in effect, the chain's estimate of "where the market's character changes."

## How GEX is used

1. **As a regime indicator** — is the market currently in a dampening (GEX > 0) or amplifying (GEX < 0) regime? This frames *how* to trade (e.g., fade moves in a dampening regime, respect trends in an amplifying regime).
2. **As a volatility forecast** — negative GEX is associated with *rising* realised volatility; positive GEX with *suppressed* volatility.
3. **Via the flip level** — as a support/resistance reference (the level where behaviour changes).
4. **Via its *change*** — a sharp drop in GEX (dealers flipping from long to short gamma) is often a warning of an impending volatility expansion.

## The honest caveats

1. **The sign rests on the dealer-short assumption** (Chapter 6, Rule 4) — the same caveat as DEX, and equally important here. In a buyer-dominated OI regime, the sign flips.
2. **GEX is not a crystal ball.** It describes the *reflexivity* of the current positioning; it does not predict the direction of the next move, and it is most informative at *extreme* levels and at *flips*, not in the middle.
3. **It is point-in-time sensitive.** GEX uses *live* gamma and *end-of-day* OI; mixing them (a backtest using today's OI for an intraday signal) is look-ahead (Chapter 6, Rule 2).
4. **It is one input.** GEX is powerful precisely *in combination* — with DEX (direction), PCR (sentiment), and skew (fear) — into a composite model (Chapter 13).

## Summary

- GEX = net dealer gamma, in ₹ per 1% move: −Σ (OI × Γ) × lot × spot² × 0.01.
- GEX > 0: dealers long gamma → counter-cyclical hedging → dampening, pinning, low vol.
- GEX < 0: dealers short gamma → pro-cyclical hedging → amplification, high vol.
- The "gamma flip" level is where market behaviour changes — a magnet or a cliff.
- Sign rests on the dealer-short assumption; it is a reflexivity/regime read, not a direction forecast.

Next: the implied probability distribution.


# 9. The Implied Probability Distribution

## Recovering the market's forecast, in full

Every model so far reduced the chain to a *single number* (a ratio, a level, a net exposure). The **implied probability distribution** goes the other way: it recovers, from the entire chain, the market's **full probability distribution of where the underlying will be at expiry** — not a point forecast, but the whole curve of probabilities.

This is the deepest read the chain offers: it is, literally, the market's *complete* view of the future, extracted from option prices.

## The idea: options price probabilities

An option's price is, at heart, the market's answer to "what is the probability-weighted value of the payoff?" Reversed, this means: **if you know all the option prices, you can recover the probability distribution they imply.** The chain of prices *encodes* a distribution; the model just *decodes* it.

The result is the **risk-neutral density** — the probability distribution such that, if you discount expected payoffs at the risk-free rate, you reproduce all the option prices. It is called "risk-neutral" because it is the distribution *implied by prices*, not necessarily the *true* distribution (the two differ by the risk premium — Chapter 10's subject).

## The construction: butterflies and the second derivative

The cleanest way to see the construction is through **butterflies** (from *The Complete Options Trader*). A butterfly spread — buy a call at K−ΔK, sell two at K, buy one at K+ΔK — pays off **only if the underlying expires near K**, and its payoff is a narrow spike around K.

The price of that butterfly is therefore the market's price for the event "the underlying lands near K." Divide by the spike's width, and you get the **probability density** at K.

Formally (the Breeden–Litzenberger result), the risk-neutral density f(K) is the **second derivative of the call price with respect to strike**:

f(K) ≈ e^(rT) × [ C(K − ΔK) − 2·C(K) + C(K + ΔK) ] / (ΔK)²

where C(K) is the call price at strike K, and ΔK is the strike spacing. The numerator is exactly the butterfly price (one call at K−ΔK, minus two at K, plus one at K+ΔK); dividing by (ΔK)² (and the discount factor) converts a "price of a spike of width ΔK" into a "probability density."

## What the distribution shows

The recovered curve is a rich object, and each of its *features* is a signal:

1. **The mode / centre** — where the market thinks price is *most likely* to land (its best single guess). Often near spot, but not always.
2. **The width** — the market's uncertainty: a wide, flat distribution = a big expected range; a narrow, peaked one = a confident, range-bound view.
3. **The skew (asymmetry)** — a distribution with a fat *left* tail (downside) and a thin right tail is the visual form of the *skew* from Chapter 4: the market thinks a large *fall* is more likely than a large *rise*.
4. **The tails** — the probability of *extreme* moves. Fat tails = the market is pricing crash risk; thin tails = it is pricing calm.
5. **Kinks and bumps** — the distribution is often *not* smooth; a bump at a particular level corresponds to a strike with unusual demand (an OI wall, a psychological level) — the chain's fingerprint of a *specific* level the market is watching.

## How it is used

The implied distribution is the single most versatile object in this book, because it answers, directly, the questions every other model gestures at:

- **"What is the probability NIFTY closes above 25,000?"** → integrate the density above 25,000.
- **"What is the market pricing as a 1-in-10 (or 1-in-20) move?"** → read the 5th/95th (or 2.5th/97.5th) percentiles of the distribution.
- **"Is the market pricing a crash?"** → look at the left tail's weight.
- **"Where are the levels the market is watching?"** → look at the kinks and bumps.

It is, in effect, the **"expected move" (Chapter 11) generalised from a single number to the entire curve.**

## The honest caveats

1. **It is risk-neutral, not the true distribution.** The implied distribution is *risk-adjusted*: because investors pay up for crash protection (the risk premium), the left tail is *fatter* in the implied distribution than in the market's *true* (unobservable) belief. The implied distribution *overstates* the probability of extreme moves — which is precisely the variance risk premium of the next chapter.
2. **It is noisy.** The second derivative amplifies noise: small pricing errors in individual options become large wiggles in the density. The curve must be *smoothed* (interpolated) before it is readable, and the smoothing is a modelling choice.
3. **It is only as good as the chain.** Thin OI, wide spreads, and missing strikes in the wings make the tail of the implied distribution unreliable (Chapter 14).

## Summary

- The chain of option prices *encodes* a full probability distribution; the model decodes it.
- The density is the second derivative of call price w.r.t. strike (the butterfly / Breeden–Litzenberger result).
- Features: mode (best guess), width (uncertainty), skew (asymmetry), tails (crash risk), kinks (watched levels).
- It answers "probability of closing above X", "the 1-in-10 move", "is a crash priced?", "where are the watched levels?"
- It is risk-neutral (overstates tails) and noisy (needs smoothing) — and only as good as the chain.

Next: the variance risk premium — what the distribution's bias is worth.


# 10. Realised vs. Implied: The Variance Risk Premium

## The chain's built-in bias — and what it is worth

The previous chapter's implied distribution has a known *bias*: it overstates the probability of extreme moves. That bias has a name and a value — the **variance risk premium (VRP)** — and it is the single most economically important model in this book, because it explains *why* selling options earns money on average, and *what* that money is really compensation for.

## The definition

**Realised volatility (RV)** is what the market *actually did* — the volatility computed from the underlying's actual price moves over a period.

**Implied volatility (IV)** is what the market *expected* — the volatility priced into the options (Chapter 4).

The **variance risk premium** is the systematic gap between them:

VRP = Implied volatility − Realised volatility (quoted here in volatility terms)

The widely reported empirical finding: **on average, IV exceeds RV.** Options are priced a little *rich* relative to what actually happens. The implied distribution's fat tails (Chapter 9) are, on average, *fatter than reality* — the market persistently overpays for the possibility of a crash.

## Why the premium exists

The VRP is not a free lunch or a market error; it is **compensation for bearing crash risk.** Three forces sustain it:

1. **Demand for protection.** Investors are *risk-averse* and systematically buy downside protection (puts), bidding up option prices above their "fair" actuarial value. This is the same force behind the skew (Chapter 4) — the market pays up for insurance, structurally.
2. **The asymmetry of crashes.** When the "overpriced" protection is needed (a crash), it pays off enormously; when it is not needed, it quietly expires worthless. Selling it earns a steady stream — *until* the crash.
3. **Short-vol capital.** Selling volatility to collect the VRP is a crowded, well-understood trade — which is why the premium persists but is *risky*: it is the "picking up pennies in front of a steamroller" trade, formalised.

## The model: harvesting (or measuring) the VRP

The VRP is used two ways, which must be kept distinct:

### 1. As a *signal* (measuring when options are cheap or expensive)

Compare IV to recent RV (or to its own history, the IV rank/percentile of *The Complete Options Trader*):

- **IV far above RV** → options are historically expensive → historically, this has favoured *reduced exposure to option buying* (or increased premium collection).
- **IV far below RV** → options are cheap → historically favoured the reverse.

This is the *entry filter* for volatility strategies: buy vol when it is cheap, sell vol when it is rich.

### 2. As a *trade* (collecting the premium directly)

A systematic short-volatility strategy — selling straddles, strangles, or condors across many expiries — is, in effect, **harvesting the VRP**: collecting the average excess of IV over RV. Its historical profile is the trade's defining fact:

- **Most of the time:** small, steady gains (the premium decays, and IV > RV).
- **Occasionally:** a large, sudden loss (a crash, when RV spikes *above* IV and the short-vol position loses far more than the accumulated premium).

## The honest framing

The VRP is the reason this book must be careful with language:

> *Historically, systematically collecting the variance risk premium has tended to earn a steady positive return — punctuated by sharp losses precisely when realised volatility spikes. The premium is compensation for bearing crash risk, not a free lunch; the trader who collects it is selling insurance, and insurance is paid out in exactly the scenarios the seller least wants.*

This is why every short-vol model (and every GEX-negative read, Chapter 8) carries the same discipline from *Risk Management and Position Sizing*: **size for the tail, cap the exposure, and never mistake a risk premium for a certainty.**

## The VRP and the rest of the book

The VRP ties the whole book together:

- It is *why* the implied distribution overstates tails (Chapter 9).
- It is *why* IV's level (rank/percentile) is a meaningful entry filter (Chapter 4).
- It is *why* GEX-negative markets (Chapter 8) — where dealers are short gamma and vol can spike — are the dangerous environments for premium collection.
- It is the *economic engine* behind income strategies, framed honestly rather than as "free money."

## Summary

- VRP = IV − RV; on average IV > RV — options are priced rich.
- It exists as compensation for crash risk: investors pay up for protection, structurally.
- Use it as a signal (IV vs. RV = cheap/expensive) or a trade (systematic short-vol harvests it).
- The short-vol profile: steady small gains, punctuated by sharp losses in crashes.
- It is a risk premium, not a free lunch — size for the tail.

Next: the expected move and event pricing.


# 11. The Expected Move and Event Pricing

## The chain's single best forecast

If the implied distribution (Chapter 9) is the *full* forecast, the **expected move** is its most useful *summary*: the market's estimate of how far the underlying is likely to move over a given period. It is the chain's answer to the question every trader asks — *"how big a move is priced in?"* — and it is the foundation for judging whether a view, or an event, is fairly priced.

## The definition

The expected move is the market-implied **one-standard-deviation move** over the period to expiry — the range within which the underlying is expected to land about two-thirds of the time.

There are three standard ways to read it, in increasing sophistication:

### 1. The ATM straddle price

The simplest: the price of the **at-the-money straddle** (call + put at the money) is approximately the expected move. The straddle's price is, in effect, the market's fee for betting on "a move of at least this size in either direction" — so it *is* the market's move estimate.

Expected move ≈ ATM call price + ATM put price

(More precisely, the ATM straddle is worth about 0.8 of the 1σ move — √(2/π) ≈ 0.8 — so 1σ ≈ 1.25 × straddle. The straddle alone slightly understates the 1σ range.)

### 2. The √time formula (from IV)

From the ATM **implied volatility** (Chapter 4), the 1σ move scales by the square root of time:

Expected move (1σ) ≈ S × IV × √(T / 252)

where S is the underlying price, IV is the annualised ATM implied volatility (decimal), T is trading days to expiry, and 252 is trading days per year.

### 3. The full-distribution percentiles

Most precisely, read the expected move off the **implied distribution** (Chapter 9): the 1σ move is the distance from the centre to the 16th/84th percentiles; the "1-in-10" move is the 5th/95th percentiles (10% of outcomes fall outside that range, 5% in each tail), and so on. This captures the *skew* that the symmetric √time formula ignores.

## Why the expected move matters

The expected move is the *benchmark* against which every view must be judged. Its core use:

> **A view is only worth acting on if the move you expect is *different from* the move already priced in.**

- If you expect a 300-point NIFTY move and the chain prices a 200-point move, your edge is 100 points — *that* is worth expressing.
- If you expect a 300-point move and the chain *already prices* 400 points, you have no edge — the market expects more than you do.

This is the single most valuable habit in option analysis: **before any directional or event trade, ask what the chain is already pricing.** The expected move is the number that answers it.

## Event pricing: the expected move around an event

The expected move reaches its peak usefulness around **events** (budgets, elections, rate decisions, earnings). The chain prices the event *in advance*:

- **Before the event**, IV — and therefore the expected move — rises (the market is pricing uncertainty).
- **After the event**, IV collapses back (the "volatility crush" of *The Complete Options Trader*), because the uncertainty resolved.

This produces the classic, recurring pattern: **the expected move before an event is the market's estimate of "how big will this event's move be?"** — and a trader buying options into the event must beat *that* estimate, not just "be right about the direction."

### A worked example (conceptual)

NIFTY at 25,000, one day before a major budget, weekly expiry 2 trading days away:

- ATM IV is 25% (annualised). Expected 1σ move over 2 days ≈ 25,000 × 0.25 × √(2/252) ≈ 25,000 × 0.25 × 0.089 ≈ **556 points**.

So the chain prices a ~556-point (1σ) move around the budget. A trader who expects a *smaller* move believes options are overpriced (a case for selling); one who expects a *larger* move believes they are cheap (a case for buying). The number converts "is the event priced in?" into a concrete, answerable question.

## The honest caveats

1. **The expected move is a *range*, not a target.** 1σ means "within this range ~68% of the time" — the market will move *more* than the expected move about a third of the time. It is not a promise; it is a central tendency.
2. **It is the *risk-neutral* expectation** (Chapter 9's caveat) — slightly biased by the risk premium. For practical purposes it is an excellent estimate, but it is not the *true* expected move.
3. **It is a snapshot.** The expected move changes as IV changes; an event's pricing evolves as the event approaches. Read it *at decision time*, not from memory.

## Summary

- The expected move is the market-implied 1σ move over the period to expiry.
- Read it via the ATM straddle price, the √time formula, or the distribution's percentiles.
- It is the benchmark: a view is only worth acting on if your move ≠ the priced move.
- Around events, IV (and the expected move) rises before and collapses after — the "is it priced in?" question, made numeric.
- It is a range (1σ ≈ 68% of the time), risk-neutral, and a snapshot — not a target.

Next: option-implied support and resistance.


# 12. Option-Implied Support and Resistance

## Where the market's own positioning says price will be held

Traditional support and resistance are drawn by hand (*Charts and Chart Types*, in this series). The option chain offers a *quantitative* alternative: **support and resistance levels derived from the market's own option positioning** — the strikes where capital is concentrated, and where the market's behaviour is most likely to change. This chapter builds that model.

## The three sources of option-implied levels

The chain provides three distinct, quantitative sources of levels:

### 1. OI walls

From Chapter 2: strikes with unusually heavy open interest. A **call OI wall above spot** is where many call writers are positioned (profiting if price stays below) — read as **resistance**. A **put OI wall below spot** is where put writers sit — read as **support**. The heaviest walls are the levels the market is most "defending".

### 2. Gamma walls and the flip level

From Chapter 8: the strikes where **gamma** concentrates, and where **GEX flips sign**. A large *positive-gamma* wall acts as a **magnet** (dealer hedging pins price near it); the **flip level** is where behaviour changes from dampened to amplified — a level where a break can accelerate. These are *dynamic* levels, computed from the Greeks rather than from OI alone.

### 3. The implied distribution's kinks

From Chapter 9: the **bumps and kinks** in the implied probability distribution — the strikes where option demand is unusual. A bump at a particular level is the market's fingerprint of a *specific* level it is watching (a psychological round number, a prior high/low, an expected event level).

## How to use option-implied levels

The power of these levels is that they are **objective and self-updating** — computed from the chain, they do not depend on where an analyst *chooses* to draw a line:

1. **Read the levels before the market reaches them.** The OI walls, gamma walls, and distribution kinks tell you *in advance* where the market is likely to be held, drawn, or accelerated.
2. **Treat them as zones, not points** (the same discipline as hand-drawn levels). A wall at 25,000 is really the "24,950–25,050 zone."
3. **Combine the sources.** A strike that is *simultaneously* a heavy OI wall, a positive-gamma wall, and a distribution kink is a *much* stronger level than any one of those alone — the three sources are *confirming* each other.
4. **Watch for their *break*.** An option-implied level that *breaks* is especially meaningful, because it means the positioning that was defending it has been overwhelmed — often the start of an accelerated move (the GEX-negative dynamic of Chapter 8).

## Option-implied vs. hand-drawn: the complement

The two approaches are complementary, not competing:

- **Hand-drawn levels** (charts) capture *historical* price structure — prior highs/lows, trendlines, chart patterns. They are *where price has turned before*.
- **Option-implied levels** capture *forward-looking* positioning — where capital is committed *now*, and where dealer hedging will act. They are *where the market expects price to be held*.

The strongest levels are the ones where the two **agree**: a prior chart resistance that is *also* a heavy call wall, a prior support that is *also* a put wall and a gamma magnet. When chart structure and option positioning coincide, the level is at its most meaningful.

## The honest caveats

1. **Walls break.** An OI wall is a *tendency*, not a guarantee — and it is most reliable in calm, range-bound expiries, and least reliable in strongly trending markets (the same caveat as max pain, Chapter 5).
2. **Levels expire.** Option-implied levels are tied to the *expiry* they come from. A wall in the current weekly expiry ceases to matter when that expiry passes; the *monthly* expiry's levels are the more persistent ones.
3. **The sign assumptions apply.** Gamma-based levels inherit the dealer-short assumption (Chapter 6, Rule 4).

## Summary

- Three quantitative level sources: OI walls (writers' stakes), gamma walls + the GEX flip, and the implied distribution's kinks.
- Option-implied levels are objective and self-updating — computed, not drawn.
- Combine sources; a multi-confirmed level is the strongest; a broken one often accelerates.
- They complement hand-drawn levels — strongest when chart structure and option positioning agree.
- Walls break, and levels expire with their expiry.

Next: combining the signals into a composite model.


# 13. Combining Signals into a Composite Model

## From many signals to one read

Every model so far — PCR, skew, max pain, DEX, GEX, the implied distribution, the VRP, the expected move — is a *single* signal, and each is weak on its own (each chapter's caveats). The power of option chain analysis comes from **combining** them into a *composite* — a single, coherent read of the market's positioning. This chapter shows how.

## Why combine? The signals are complements

The signals are weak individually because each measures only *one* aspect of the market, and each has a known blind spot:

| Signal | Measures | Blind spot |
|--------|----------|------------|
| PCR | Bearish/bullish positioning | Does not know *why* (hedging vs. speculation) |
| Skew | Fear / tail demand | Says nothing about *direction* |
| Max pain | Expiry gravity | Weak in trending markets |
| DEX | Directional tilt | Dealer-short assumption |
| GEX | Reflexivity / regime | Not a direction forecast |
| IV rank | Cheap vs. expensive | Not a timing signal |
| Expected move | Priced-in size | A range, not a target |

But they are *complementary*: one answers "what is the sentiment" (PCR), another "where is the fear" (skew), another "how reflexive is the market" (GEX), another "what is priced in" (expected move). **Combined, they answer the full question; alone, each answers only a slice.**

## The combining discipline

The right way to combine is not to *average everything* (which dilutes the signal), but to build a **layered read** — a small number of composite questions, each answered by a *subset* of signals:

### 1. The regime question — "is this market reflexive or stable?"

Answer with **GEX + IV rank**:

- GEX negative + IV rising = an *amplifying, expanding* regime (respect trends, expect volatility).
- GEX positive + IV low = a *dampening, stable* regime (fade moves, expect range).

### 2. The sentiment question — "which way is the crowd leaning?"

Answer with **PCR (percentile) + risk reversal + DEX**:

- High PCR + steeply negative risk reversal + negative DEX = *crowded bearish* positioning (watch for either continuation or a squeeze — confirm with price).

### 3. The level question — "where does it matter?"

Answer with **OI walls + gamma walls + max pain + the distribution's kinks**:

- A strike confirmed by several sources = a *strong level* (the support/resistance model, Chapter 12).

### 4. The price question — "is a move fairly priced?"

Answer with the **expected move + IV rank + VRP**:

- A large expected move *with* a high IV rank = the move is *already priced in* (be sceptical of chasing it).

The layered read is the composite: four questions, each answered by its subset of signals, together forming a complete positioning picture.

## A worked composite read (conceptual)

> *"GEX is deeply negative and IV is in its top decile (amplifying regime). PCR is at its 90th percentile and the risk reversal is steeply negative (crowded bearish). Heavy put OI sits at 24,500 and heavy call OI at 25,300 (levels). The expected move over the next week is 450 points (priced-in move)."*

Read together: a *volatile, reflexive* market, *crowded bearish*, with defined levels and a priced-in move — a completely different picture from any single number, and the kind of composite read that actually informs a decision.

## The two honest rules

1. **Keep it explainable.** A composite with three inputs is testable and explainable; one with thirty is overfit (a rule from *How to Build a Framework for Systematic Trading*). Every input in the composite should have a *reason* ("GEX tells us reflexivity"), not just "it improved the backtest."
2. **Test it as a whole.** A composite signal is a *model*, and it gets the full model discipline (Chapter 6): point-in-time data, costs included, out-of-sample testing, and — above all — an honest eye on **decay** (Chapter 14). A composite is not *more true* because it has more inputs; it is only as good as its weakest, most-overfit component.

## Summary

- Each signal is weak alone; they are *complements* (sentiment, fear, reflexivity, price, levels).
- Combine as a *layered read*, not an average: regime (GEX+IV), sentiment (PCR+skew+DEX), levels (OI+gamma+max pain), price (expected move+IV rank).
- Four questions, each answered by a subset, form the composite.
- Keep it explainable; test it as a whole; every input needs a reason.

Next: data quality, pitfalls, and failure modes — where every chain model breaks.


# 14. Data Quality, Pitfalls, and Failure Modes

## Where every chain model breaks

Every model in this book is only as good as its data, and only as honest as its user. This final chapter is the *honesty chapter*: the specific, recurring ways option-chain models fail, so that you can recognise them — in the data, in the model, and in yourself — before they cost you money.

## The data pitfalls

### 1. Look-ahead (the biggest one)

Chain models are uniquely vulnerable to look-ahead, because the "obvious" data is not always available when you think:

- **OI is end-of-day.** Intraday OI is an estimate; the true figure is only known after the close. A model that trades on "today's OI" intraday is trading on data that does not exist yet.
- **IV and the Greeks are live and path-dependent.** The IV at 3:15 pm was not the IV at 10 am. A backtest that pairs the *day's* IV with the *day's* move is partly look-ahead.
- **The strike set changes.** A chain today includes strikes that were not listed last month (and excludes some that were). Any backtest over "the current strike ladder" is survivorship-biased.

The fix (Chapter 6, Rule 2) is the universal test: **did the market know this on this date?**

### 2. Thin and stale data

The wings of the chain — far OTM options — are where the data is worst: **thin OI, wide bid-ask spreads, and stale prices**. Yet the wings are exactly where the models are most sensitive:

- The **implied distribution's tails** (Chapter 9) are built from wing prices — and wing prices are the least reliable.
- **GEX** integrates gamma across *all* strikes, including the thin wings, so it inherits their noise.

The fix: **use liquid, near-the-money data for the models that need it, and treat wing-derived quantities (tails, extreme GEX) with extra scepticism.**

### 3. Data that is inconsistent across sources

OI, IV, and the Greeks can differ *across data providers* — because of different timing (when OI is snapshotted), different models (which Black-Scholes variant), and different corporate-action adjustments. A model built on one source and run on another can silently produce different results.

The fix: **pin your data source, and reconcile it** (compare your computed IV/Greeks against a second source occasionally).

## The model pitfalls

### 4. The dealer-short assumption (the silent sign-flip)

Every positioning model (DEX, GEX) rests on the assumption that **OI is dealer-short**. When it is not — a retail buying frenzy, a market where options are heavily *bought* rather than *written* — the sign flips, and a "stabilising, positive GEX" read becomes exactly wrong. This is the most common way these models fail in practice, and it is why the *sign* should always be treated more cautiously than the *structure*.

### 5. Regime dependence

Every model in this book is *regime-conditional*, and they all degrade outside their home regime:

- **Max pain and OI walls** work in calm, range-bound expiries; they are weak in trending markets.
- **PCR contrarian reads** work at *extremes*; at mid-range they are trend-following — and "extreme" shifts with the regime.
- **GEX** is informative at *extreme* levels and *flips*; in the middle it says little.

The fix: **know each model's home regime, and do not apply it outside it.**

### 6. The reflexivity / decay problem

Option-derived edges are *self-defeating*: the more widely a signal is known and traded, the faster it is arbitraged away. The max-pain pinning trade, the GEX-flip trade, the PCR-extreme fade — each is commonly observed to weaken once it becomes popular. **Expect any chain edge to decay**, and monitor for the decay rather than assuming the backtest's edge will persist.

## The user pitfalls

### 7. Confirmation bias

The chain is information-rich, which makes it a *magnet for confirmation bias*: given a dozen signals, it is always possible to find *one* that supports the view you already hold. The composite model (Chapter 13) is the antidote — but only if you read it *as a whole* and let it *disagree* with you, rather than cherry-picking the one signal that agrees.

### 8. Mistaking a map for a forecast

The deepest error of all: reading a *positioning map* as a *price forecast*. The chain tells you where capital sits and how the market is likely to *behave* (reflexive vs. stable, cheap vs. expensive to insure). It does **not** tell you where price will go next. The models describe *the crowd and its exposure* — which is powerful — but a description of the crowd is not a prediction of the market.

## The honest close

Option chain analysis is, at its best, the richest single source of market information available — a live, self-updating map of *where capital is positioned, how the market is likely to behave, and what is already priced in*. Used with the discipline of this chapter — point-in-time data, known assumptions, regime awareness, and the humility to treat a map as a map, not a prophecy — it is a genuine edge. Used carelessly, it is a machine for manufacturing confident-sounding, data-dressed guesses. The difference is entirely the discipline.

## Summary

- Data pitfalls: look-ahead (OI is EOD, IV is live, strikes change), thin/stale wings, inconsistent sources.
- Model pitfalls: the dealer-short assumption (sign flips), regime dependence, and decay.
- User pitfalls: confirmation bias, and mistaking a positioning map for a forecast.
- Every model is regime-conditional; know its home regime.
- The chain is a map of positioning — powerful, but a map, not a prophecy.

This completes the main text. The appendix is the formula reference and signal table.


# Appendix — Formula Reference and Signal Table

## The formulas, in one place

**Put-Call Ratio (OI-based):** PCR = Σ(put OI) ÷ Σ(call OI)

**Max pain:** the strike K that minimises

Total pain(K) = Σᵢ [ OI_call(Kᵢ)·max(K − Kᵢ, 0) + OI_put(Kᵢ)·max(Kᵢ − K, 0) ]

**Risk reversal (skew):** 25Δ risk reversal = IV(25Δ call) − IV(25Δ put)

**Delta exposure (DEX), dealer-short convention:**

DEX = − Σₖ [ OI_call(K)·Δ_call(K) + OI_put(K)·Δ_put(K) ] × (spot × lot)

**Gamma exposure (GEX), dealer-short convention:**

GEX = − Σₖ [ OI_call(K)·Γ_call(K) + OI_put(K)·Γ_put(K) ] × lot × spot² × 0.01   (in ₹ per 1% move)

**Implied probability density (Breeden–Litzenberger):**

f(K) ≈ e^(rT) × [ C(K − ΔK) − 2·C(K) + C(K + ΔK) ] / (ΔK)²

**Variance risk premium:** VRP = Implied volatility − Realised volatility (quoted here in volatility terms)

**Expected move (1σ):**

- ATM straddle: Expected move ≈ C(ATM) + P(ATM) (the straddle ≈ 0.8σ, so 1σ ≈ 1.25 × straddle)
- From IV: Expected move ≈ S × IV × √(T / 252)

## The signals, at a glance

| Signal | Measures | Best read as |
|--------|----------|--------------|
| OI + price change | Flow (longs/shorts entering) | Four-quadrant read |
| OI walls | Where capital sits | Support / resistance |
| PCR (percentile) | Bearish/bullish positioning | Trend at mid-range, contrarian at extremes |
| Risk reversal | Fear / tail demand | Steepening = fear building |
| Term structure | When uncertainty is | Backwardation = event near |
| Max pain | Expiry gravity | Expiry-day reference |
| DEX | Directional tilt | Direction of hedging flows |
| GEX | Reflexivity / regime | Dampening vs. amplifying |
| Implied distribution | Full forecast | Probability of ranges, tails, levels |
| VRP | Insurance premium | Cheap vs. expensive vol |
| Expected move | Priced-in move size | Benchmark for every view |
| Implied S/R | Positioned levels | OI + gamma walls + distribution kinks |

## The universal rules

1. **Point-in-time or nothing** — OI is end-of-day, IV is live, strikes change.
2. **State the dealer-short assumption** — the positioning models' sign rests on it.
3. **Normalise to history** — read percentiles, not absolutes.
4. **Know each model's home regime** — max pain and walls are range-bound tools; GEX and PCR matter at extremes.
5. **Combine, don't cherry-pick** — a composite read, honestly assembled, beats any single signal.
6. **A map, not a prophecy** — the chain shows positioning and behaviour, not the next price.
