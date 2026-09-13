# 27. Open Interest, Put-Call Ratio, and Max Pain

## Reading the market's positioning

So far the book has treated options as *pricing and strategy* problems. This chapter turns to **market intelligence** — reading the option chain's aggregate data to understand where capital is positioned and what it implies about likely price behaviour. These are the techniques StratLab-style analytics are built on, and they are accessible to any trader with a chain in front of them.

## Open interest: the footprint of capital

**Open interest (OI)** is the number of outstanding contracts. It is the market's *positioning footprint* — a map of where the "big money" has written options and where it has bought them.

Three OI readings matter most:

1. **OI concentration / walls** — unusually large OI at specific strikes. A heavy wall of call OI above the market, or put OI below it, marks a level where many option *writers* are positioned. Because writers profit from the option expiring worthless, these levels often act as **magnet or resistance/support zones** — the market is "pulled toward" or "blocked at" them. A large put OI wall *below* spot is often read as support; a large call OI wall *above* spot as resistance.
2. **OI change with price** — the four-quadrant read from Chapter 7 (rising price + rising OI = new longs, etc.) is the daily "money flow" signal.
3. **OI vs. volume** — high volume with flat OI is churn (day-trading); high volume with rising OI is genuine positioning.

The disciplined caveat: OI tells you *where capital is*, not *where price will go*. A wall is not a guarantee — walls break. But OI is the best public proxy for the *stakes* at each level.

## The put-call ratio (PCR)

The **put-call ratio** is total put OI divided by total call OI (a volume-based version also exists). It summarises, in one number, the balance of bearish versus bullish option positioning.

- **PCR > 1** — more puts than calls are open (or traded): positioning leans bearish.
- **PCR < 1** — more calls than puts: positioning leans bullish.

The subtlety — and it is important — is *how to interpret an extreme*:

- A **very high PCR** (heavy put buying) can be read two ways. It may be *genuinely bearish* (the crowd is hedging or betting on a fall). Or it may be **contrarian-bullish**: when everyone has already bought protection, the "sell" is exhausted and the market is ripe to reverse. Extreme readings are often treated as contrarian.
- A **very low PCR** (heavy call buying) is similarly ambiguous — bullish positioning, or a crowded long that is vulnerable.

The honest guidance: **PCR is a positioning gauge, not a crystal ball.** It is most useful as a *context* input — confirming or questioning a view — and at *extremes*, where mean-reversion arguments carry more weight. It should never be traded in isolation.

## Max pain

**Max pain** is the strike price at which the *largest number of options would expire worthless* — equivalently, the price at which option *writers* (in aggregate) lose the least, and option *buyers* (in aggregate) lose the most.

It is computed from the open interest across strikes: for each possible expiry price, total the intrinsic value that must be paid out across all ITM options; the price that *minimises* that payout is max pain.

The empirical observation is that, in liquid index options, the underlying often **gravitates toward max pain as expiry approaches** — a "pinning" effect, plausibly driven by the hedging behaviour of the large writers who benefit from the price settling there.

**How to use it:** as an *expiry-day* reference point. A trader holding a position into the final days can look at max pain as the level the market is "pulled toward," and frame expectations accordingly. It is not a daily trading signal and not reliable far from expiry.

### A worked illustration (simplified)

Suppose NIFTY has heavy OI concentrated as follows: large call OI at 25,200 and 25,400, large put OI at 24,800 and 24,600. Computing the payout-minimising price might yield a max pain of **25,000** — the level where all those OTM calls and puts expire worthless, and writers across the chain collect maximum premium. The market "pinning" near 25,000 into expiry would then be the expected, not the surprising, outcome.

## Putting the three together

These three tools — OI, PCR, max pain — are a coherent *positioning* read, not three separate gadgets:

1. **OI walls** show the *levels* that matter (support/resistance/magnets).
2. **PCR** shows the *balance* of bullish/bearish positioning (and its extremes).
3. **Max pain** shows the *expiry gravity* — where the market is pulled as the clock runs out.

A complete positioning read might run: *"Heavy call OI above 25,200 suggests resistance; PCR has climbed to 1.3 (crowded bearish, watch for a squeeze); max pain sits at 25,000, pulling the market down toward that level into expiry."*

## The discipline

These are **descriptive analytics**, not trade commands. They describe *where the crowd is and what would hurt it most*. A disciplined trader uses them to understand the landscape, confirm or question a thesis, and set expectations — never as a standalone buy/sell signal. Used this way, they are among the most powerful free tools an options trader has.

## Summary

- OI maps where capital is positioned; walls mark support/resistance/magnet levels; OI+price change reveals flow.
- PCR summarises bullish/bearish option balance; extremes are ambiguous and often read contrarian.
- Max pain is the strike where most options expire worthless — the expiry "gravity" level.
- Together they form a positioning read: levels (OI), balance (PCR), and expiry pull (max pain).
- All are descriptive, not prescriptive.

Next: position sizing, margin, and risk management — the discipline that keeps you in the game.
