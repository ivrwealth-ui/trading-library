# 6. How Options Trade on the NSE

## The NFO segment

Options and futures in India trade on a dedicated segment of the exchanges — **NFO** on the NSE (and BFO on the BSE). When your broker shows "NFO", that is the derivatives segment. Index options (NIFTY, BankNIFTY, FINNIFTY, and others) and stock options both trade here.

The important practical distinction is the **trading hours**:

- Equity cash market: 09:15 to 15:30 IST.
- Derivatives segment: 09:15 to 15:30 IST for trading, with an additional window in some products (e.g., index futures/options may trade a short extended session on expiry days in specific circumstances). Always confirm current timings with your broker.

## The contract cycle: weekly and monthly expiries

Indian index options offer both **weekly** and **monthly** contracts, giving traders a choice of time horizon.

- **Monthly contracts** expire on the **last Thursday** of the month (or the previous trading day if that Thursday is a holiday). These are the longest-dated "standard" contracts.
- **Weekly contracts** expire on a fixed weekday, added on a rolling basis so there is always a short-dated contract available.

> **A note that matters:** SEBI has, over time, rationalised the weekly expiry schedule — the specific weekday assigned to each index has changed (for example, NIFTY's weekly expiry has moved from Thursday to Tuesday). The principles in this chapter are durable; the *exact current days* should always be confirmed against the live NSE contract calendar, because they are a regulatory detail that shifts.

The consequence of having both weekly and monthly expiries is a choice of **time horizon**: a trader expressing a two-day view can use the weekly; a trader expressing a three-week view can use the monthly. The shorter the time to expiry, the faster the time decay (and the higher the per-day sensitivity of the option's price).

## How the chain is built: strike intervals

For each expiry, the exchange lists a ladder of strikes at fixed intervals. Near the current index level, strikes are closer together; further away they widen. For NIFTY, this is typically 50-point intervals near the money; for BankNIFTY, 100-point intervals. New strikes are added dynamically as the index moves so that there is always a sufficient band both above and below the market.

The strike ladder is what the **option chain** displays, and it is where you will spend most of your screen time.

## Buying and selling: orders and the bid-ask spread

Options trade through the same order types as equities — market orders and limit orders — but the **liquidity profile** is different and matters more:

- **Liquid contracts** (nearest expiry, near-the-money strikes) have tight bid-ask spreads and deep order books. NIFTY and BankNIFTY weekly ATM options are among the most liquid instruments in the world.
- **Illiquid contracts** (far expiries, far OTM strikes, many stock options) have wide spreads. Crossing a wide spread is a real, hidden cost — you may pay more to enter and receive less on exit than the "last traded price" suggests.

The **bid-ask spread** is the difference between what buyers are offering (bid) and what sellers are asking (ask). For a trader, the spread is a transaction cost. Prefer liquid contracts where the spread is a small fraction of the premium.

## Settlement: cash vs. physical

- **Index options** are **cash-settled**: on exercise, no shares change hands. The ITM value is credited/debited in cash to the holder/writer's account on settlement day. For a NIFTY call, you never receive NIFTY shares — you receive (or pay) the difference in cash.
- **Stock options** have moved to **physical settlement**: an ITM stock option on expiry results in actual delivery of (or payment for) the underlying shares at the strike. This has practical implications — you need the funds to take delivery, or you should square off (close) the position before expiry if you do not want delivery.

For most short-term traders, these settlement mechanics are avoided simply by **squaring off** — closing the position before expiry by taking an offsetting trade — rather than holding to exercise.

## Exercise and assignment

- **Exercise** is the buyer's act of using the right. Index options are European-style and can be exercised only on expiry; stock options, as traded on NSE, are also effectively exercised at expiry in the normal course (auto-exercise of ITM options).
- **Assignment** is what happens to the seller: when a buyer exercises, the clearing system *assigns* a matching seller to fulfil the obligation.

In practice, exchanges **auto-exercise** options that are ITM at expiry (often at a defined threshold), so a trader who is ITM at the close of the last day does not need to take manual action — but should confirm their broker's exact cut-off policy.

## Costs of trading: the charges

Beyond the premium, a round-trip options trade attracts costs that materially affect profitability:

- **Brokerage** — per-order or flat-fee, depending on your broker.
- **STT (Securities Transaction Tax)** — levied on the sell side of options (and on exercise). Rates change by budget; always confirm current rates.
- **Exchange transaction charges, SEBI fees, stamp duty, and GST on charges.**

For strategies that involve frequent buying and selling, or many legs, these costs accumulate. A strategy that looks profitable before costs can be unprofitable after them. Always model costs into any plan.

## Summary

- NFO is the derivatives segment; index and stock options trade there.
- Weekly + monthly expiries give a choice of time horizon; confirm the exact current expiry weekdays.
- The option chain is a strike ladder; liquidity concentrates in near-expiry, near-the-money strikes.
- Index options are cash-settled; stock options are physically settled — most traders square off before expiry.
- Bid-ask spread and statutory charges are real costs that must be modelled.

Next: how to read the option chain — the screen where all of this comes together.
