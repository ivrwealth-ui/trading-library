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
