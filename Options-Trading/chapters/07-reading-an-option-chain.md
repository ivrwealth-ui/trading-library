# 7. Reading an Option Chain

## The chain is the market's map

The **option chain** is the screen that lists, for a given underlying and expiry, every available strike with its calls on one side and puts on the other. It is where you will spend most of your time, so learning to read it fluently is non-negotiable.

A typical chain row shows, for each strike, a column of **call** data and a column of **put** data. The most important columns are below.

## The columns, explained

### LTP (Last Traded Price)

The price of the most recent trade in that contract. It is the headline number, but it is only one data point — use it alongside bid and ask, not instead of them.

### Bid and Ask

The **bid** is the highest price a buyer is currently willing to pay; the **ask** (or offer) is the lowest price a seller is willing to accept. The gap between them is the **spread**, and it is a transaction cost. In liquid contracts (NIFTY ATM) the spread is a rupee or two; in illiquid ones it can be wide.

A realistic entry price is closer to the *ask* (for a buyer) or the *bid* (for a seller), not the LTP.

### Open Interest (OI)

**Open interest** is the total number of *outstanding* (not yet closed) contracts at that strike. Unlike volume, which measures contracts traded *during* a period, OI measures contracts *still open* at the end of the period.

- Rising OI = new money entering; the contract is being added to.
- Falling OI = positions being closed; the contract is being unwound.

OI is the market's footprint of where capital is positioned, and it is the basis of much of the analysis in Chapter 27 (max pain, put-call ratio, OI walls).

### Change in OI

The day-over-day (or tick-over-tick) change in OI. Combined with price, it signals intent:

| Price | Change in OI | Interpretation |
|-------|--------------|----------------|
| Up | Up | New longs being added (bullish) |
| Up | Down | Short covering (position unwinding) |
| Down | Up | New shorts being added (bearish) |
| Down | Down | Longs liquidating (bearish) |

This is a heuristic, not a law — but it is the standard starting point for reading money flow in the chain.

### Volume

Contracts traded during the period. High volume with low OI means churn (day-trading); high volume with rising OI means genuine position building. On Indian index options, volume tends to concentrate in the current weekly expiry.

### IV (Implied Volatility)

Many chains display the implied volatility for each strike (see Chapter 16). In liquid markets, a *smile* is visible: IV is lowest at the money and rises for OTM options — a signature of the market pricing tail risk (Chapter 17).

### Greeks (delta, theta, vega, gamma)

Broker platforms often expose the Greeks per strike. They tell you how the option's price will respond to the underlying, time, and volatility — the entire subject of Part II.

## How to orient yourself in the chain

1. **Find the ATM strike** — the strike nearest the current underlying price (your broker usually highlights it, or shows the spot at the top of the chain).
2. **Read calls above the spot and puts below it** — or, depending on layout, calls to one side and puts to the other. Remember from Chapter 4: calls are ITM *below* spot, puts are ITM *above* spot.
3. **Look at the strike you actually care about** — the one matching your view and risk budget — not just the cheapest or the busiest.

## The chain's aggregate signals

Beyond individual contracts, the chain as a whole encodes sentiment:

- **Put-Call Ratio (PCR)** — total put OI divided by total call OI. A very high ratio (heavy put buying) is often read as bearish positioning — and, by some interpretations, as a contrarian sign. Chapter 27 treats this carefully.
- **Max Pain** — the strike at which the greatest number of options (by OI) would expire worthless, i.e., where option writers lose the least. Prices often gravitate toward it at expiry. Also Chapter 27.
- **OI concentration** — clusters of unusually high OI at particular strikes ("walls") mark levels the market is watching as support/resistance.

## A practical reading routine

For a NIFTY weekly expiry, a disciplined first pass might look like:

1. Note the spot and the ATM strike.
2. Note the **IV** level and whether it is higher or lower than recent days (cheap vs. expensive options).
3. Scan **OI** across strikes to see where capital is concentrated.
4. Note the **bid-ask spread** on the strikes you might trade.
5. Check the **PCR** and the **max pain** level for a quick sentiment snapshot.

This routine turns the chain from a wall of numbers into a structured picture of *price, time, volatility, and positioning*.

## Summary

- The chain lists every strike with calls and puts side by side.
- LTP, bid/ask, OI, OI change, volume, IV, and Greeks are the core columns.
- OI + price direction reveals whether money is entering long or short.
- Aggregate signals — PCR, max pain, OI walls — summarise market positioning.

Next: the payoff diagram, the tool for seeing any strategy's risk and reward at a glance.
