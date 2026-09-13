# 1. The Option: A Right, Not an Obligation

## What a derivative is

Before there is an option, there is a *derivative*. A derivative is a financial instrument whose value is *derived* from something else — the *underlying asset*. For the options in this book, the underlying is usually an index (NIFTY, BankNIFTY) or a stock (RELIANCE, HDFCBANK).

There are two families of exchange-traded derivatives in India: **futures** and **options**. Both bind two parties to a contract tied to a future price of the underlying. The difference is the nature of that binding.

## The contract in plain language

An **option** is a contract between two parties:

- The **buyer** of the option *pays a price today* and acquires a **right** — the right, but *not the obligation* — to buy or sell the underlying at a fixed price on or before a fixed date.
- The **seller** (also called the *writer*) of the option *receives that price today* and accepts an **obligation** — the obligation to deliver or take the underlying if the buyer chooses to exercise their right.

That asymmetry — *right for one side, obligation for the other* — is the single most important idea in options. It is why the buyer's maximum loss is capped at the price they paid, while the seller's risk is a mirror image: the seller keeps the price received but carries an obligation whose cost can grow far beyond it.

## The price of the contract: the premium

The price the buyer pays (and the seller receives) is called the **premium**. Think of it like an insurance premium:

- The buyer is the insured: paying a known, limited amount to protect against an unknown, potentially large event.
- The seller is the insurer: collecting the premium and taking on the risk that the event happens.

This insurance analogy is not decorative. Options and insurance are mathematically cousins — both are about *pricing the transfer of risk*. An airline buys fuel-price options the way a car owner buys theft insurance: a small, known cost today to remove a large, unknown cost later.

## The two basic kinds of rights

There are exactly two fundamental option types, and every strategy in this book is built from them:

1. **A Call option** gives the buyer the right to **buy** the underlying at a fixed price.
2. **A Put option** gives the buyer the right to **sell** the underlying at a fixed price.

Every "sophisticated" strategy — straddles, condors, butterflies, ratio spreads — is simply a combination of calls and puts, bought or sold, at various prices and dates. Master these two, and you have the raw material for everything that follows.

## Why the buyer's and seller's risk profiles differ so sharply

Consider a NIFTY call option. The buyer pays a premium of, say, ₹150 per unit of the contract. The buyer's worst case is that NIFTY never moves favourably and the option expires worthless — a total loss of ₹150 per unit, and *nothing more*.

The seller of that same option receives ₹150 up front. If NIFTY rallies strongly, the seller must deliver value that grows with the rally. The seller's profit is capped at the ₹150 premium, but the loss is open-ended — it grows as the underlying moves against the seller, with **no theoretical ceiling** on a naked (uncovered) short call.

This asymmetry is not a design flaw; it is the core economic function of the option. The buyer is paying to *cap* a risk. The seller is being paid to *absorb* it. Both sides get exactly what they signed up for.

## Key terms introduced

| Term | Meaning |
|------|---------|
| Underlying | The asset the option is based on (NIFTY, a stock, etc.) |
| Option | A contract giving a right to buy or sell the underlying at a fixed price |
| Call | The right to buy |
| Put | The right to sell |
| Buyer / Holder | The party that owns the right |
| Seller / Writer | The party that owes the obligation |
| Premium | The price of the option, paid by buyer to seller |
| Exercise | The act of using the right (buying/selling the underlying) |

## Summary

- An option is a *right* for its buyer and an *obligation* for its seller.
- The buyer's maximum loss is the premium paid; the seller's maximum loss can be much larger (and, for naked calls, theoretically unlimited).
- The premium is the price of transferring risk — an insurance premium for the financial markets.
- There are only two option types — calls and puts — and every strategy is a combination of them.

In the next chapter we take the contract apart piece by piece: strike, expiry, lot size, and premium.
