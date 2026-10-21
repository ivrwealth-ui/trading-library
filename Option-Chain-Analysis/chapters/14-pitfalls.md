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
