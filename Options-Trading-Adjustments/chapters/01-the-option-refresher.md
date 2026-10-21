# 1. The Option Refresher

*Part I — Foundations*

An **option** is a right, but not an obligation, to buy (a **call**) or sell (a **put**) an underlying at a fixed **strike price** on or before **expiry**. On the NSE, index options (Nifty, BankNifty) are the most liquid instruments and are **cash-settled**.

## The premium

The price of an option is its **premium**, which has two parts:

- **Intrinsic value** — the amount the option is in-the-money (`spot − strike` for a call, `strike − spot` for a put). Zero for out-of-the-money options.
- **Time value** — everything else; the market's price for *time* and *uncertainty* remaining until expiry.

**The single most important fact for every strategy in this book:** time value decays to **zero at expiry**. An option at expiry is worth *exactly* its intrinsic value, nothing more. Every payoff diagram here is drawn **at expiry**, which is where all the time value has vanished.

## Buying vs selling

- **Buying an option** gives you the right; your loss is capped at the premium, your profit is theoretically large. You *pay* time decay.
- **Selling (writing) an option** obligates you; you *collect* the premium, and you *earn* time decay — but your risk can be large (or, for an uncovered option, unbounded).

Almost all "adjustments" in this book exist to manage the risk of the **sold** side, because that is where the obligations live.
