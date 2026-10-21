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
