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
