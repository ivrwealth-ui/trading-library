# 2. Anatomy of an NSE Option Contract

## The five terms that define a contract

Every standardised option contract is described by a handful of fixed terms. On the National Stock Exchange (NSE), these are set by exchange rules so that buyers and sellers can trade with one another without negotiating bespoke terms.

1. **Underlying** — the asset (NIFTY, BankNIFTY, or a specific stock).
2. **Type** — call (CE) or put (PE).
3. **Strike price** — the fixed price at which the right can be exercised.
4. **Expiry** — the date on which the contract's life ends.
5. **Lot size** — the number of units of the underlying in one contract.

The **premium** is the sixth, market-determined number — the price the contract actually trades at.

## The underlying

NSE options trade on two broad categories of underlying:

- **Index options** — NIFTY 50, BankNIFTY, FINNIFTY, NIFTY MID SELECT, and NIFTY NEXT 50 (among others).
- **Stock options** — a select list of individual stocks that satisfy SEBI's eligibility criteria (based on liquidity and market capitalisation).

Index options are **European-style cash-settled** (exercised only on expiry, settled in cash — no physical delivery of shares). Stock options in India are now largely **physically settled** (delivery of actual shares on exercise) following SEBI's move away from cash settlement for single-stock derivatives.

## The strike price

The **strike price** (or simply *strike*) is the price at which the option's buyer can transact in the underlying. Strikes are listed at fixed intervals — for NIFTY, typically every 50 points near the current index level, widening to 100 points further out; for BankNIFTY, every 100 points near the money. Strikes are chosen so there is always a range above and below the current market price.

A trader does not pick any arbitrary strike; they choose from the listed grid. This grid is what you see scrolling down an option chain.

## Expiry

Every contract has a finite life that ends at **expiry**. After expiry the contract ceases to exist. Indian index options expire on a fixed schedule — weekly expiries on a designated weekday, plus a monthly expiry. (The precise days are covered in Chapter 6; note that they have changed over time by SEBI directive and should always be confirmed against the current NSE contract calendar.)

For a buyer, expiry is the deadline by which the market must move favourably. For a seller, expiry is when the obligation is finally discharged. Everything about option pricing is shaped by *how much time remains to expiry*.

## Lot size and contract value

Indian options trade in standardised **lots**. One NIFTY options contract represents a fixed number of NIFTY "units", not a single index point. Lot sizes are set so that the **contract value** (underlying price × lot size) stays above a SEBI-mandated minimum — currently ₹15 lakh for index derivatives.

Because lot sizes change when the underlying price moves a lot, treat any specific number as "current at the time of writing" and always verify. The important conceptual points:

- Your exposure is the **lot size × underlying price**, not the premium.
- The premium you see quoted is *per unit*; your actual cash outlay for one contract is **premium × lot size**.

### A worked example

Suppose NIFTY is at 25,000, and one lot is 75 units (a representative figure; verify current value).

- Contract value = 25,000 × 75 = ₹18,75,000.
- A NIFTY 25,000 call quoted at ₹150 premium costs ₹150 × 75 = ₹11,250 to buy (plus charges).

Notice the leverage: for ₹11,250, the buyer controls exposure to roughly ₹18.75 lakh of the index. This leverage is exactly why options are both powerful and dangerous — it cuts both ways.

## Reading a contract symbol

NSE option symbols are compact and encode everything:

`NIFTY 26 MAR 25000 CE`

- `NIFTY` — underlying
- `26 MAR` — expiry month/year
- `25000` — strike
- `CE` — call (European); `PE` would be a put

For BankNIFTY: `BANKNIFTY 26 MAR 52000 PE`. For stocks: `RELIANCE 26 MAR 3000 CE`. Brokers may also show a shorter alphanumeric code (the *instrument symbol*) used by trading APIs — but the human-readable form above always tells you the full contract identity.

## Standardisation and liquidity

Because contracts are standardised, they are *fungible*: any buyer can trade against any seller on the exchange without a direct relationship. The exchange's clearing corporation (NSE Clearing) stands between every buyer and seller, guaranteeing settlement and eliminating counterparty risk from the trader's perspective.

Standardisation also concentrates trading into a small number of highly liquid contracts — the near-month, near-the-money strikes. That liquidity is what makes tight bid-ask spreads and easy entry/exit possible, and it is why most trading happens in the closest expiry and the strikes nearest the current price.

## Summary

- A contract is defined by underlying, type, strike, expiry, and lot size; the premium is the market-determined price.
- Index options are cash-settled and European; stock options are now largely physically settled.
- One contract's real cost and exposure are **premium × lot size** and **underlying × lot size**, respectively.
- Standardisation creates liquidity, which is why most volume concentrates in the nearest expiry and near-the-money strikes.

Next, we distinguish the four fundamental roles: call buyer, call seller, put buyer, and put seller.
