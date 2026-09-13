# 30. Indian Market Mechanics

## The practical details that move real money

Theory is universal; *mechanics* are local. This final chapter covers the India-specific nuts and bolts that affect every real trade: contract specifications, costs, settlement, and regulation. **These details change, so treat every specific number here as "current at the time of writing" and verify against live NSE/SEBI circulars before trading.**

## Index options vs. stock options

The Indian options universe splits into two regimes with different behaviour:

| | Index options | Stock options |
|---|---|---|
| Examples | NIFTY, BankNIFTY, FINNIFTY, MIDCPNIFTY | RELIANCE, HDFCBANK, … (SEBI-eligible list) |
| Settlement | Cash-settled | Physically settled |
| Exercise | European (at expiry) | Auto-exercise at expiry (delivery) |
| Liquidity | Extremely high (NIFTY, BankNIFTY) | Variable — many are illiquid |
| Lot sizes | Set by SEBI contract-value rule | Set per stock |

For most retail traders, **NIFTY and BankNIFTY options are the workhorse**: deepest liquidity, tightest spreads, and cash settlement (no delivery worries). Stock options require attention to liquidity and to the risk of physical delivery if held to expiry.

## Lot sizes and contract value

SEBI mandates a **minimum contract value** for derivatives (currently ₹15 lakh for index options; a separate floor applies to stock derivatives). Lot sizes are set so that **underlying price × lot size ≥ the floor**, and are revised when the underlying moves enough to breach it.

The consequence is that lot sizes are **not fixed forever** — NIFTY's lot size has changed several times as the index rose. The rule of thumb: **always confirm the current lot size**, and remember that your actual premium outlay is *premium × lot size*, while your exposure is *underlying × lot size* (Chapter 2).

## Expiry conventions

- **Monthly expiries** for index options fall on the **last Thursday** of the month (shifted earlier if that Thursday is a holiday).
- **Weekly expiries** exist on a designated weekday per index. SEBI has rationalised this schedule over time — the specific weekday for each index's weekly expiry has changed (NIFTY's weekly, for example, has moved from Thursday to Tuesday in the current regime). **Confirm the current weekly expiry day for your instrument before trading**, as it is a regulatory detail, not a permanent fact.

The strategic takeaway from Chapter 6 holds: weekly expiries give short-horizon traders fast time-decay, while monthly expiries suit longer views.

## Settlement: cash vs. physical

- **Index options** are **cash-settled**: ITM positions at expiry are settled by cash debit/credit — no shares change hands. This is why index options are the cleanest instruments for speculation and hedging.
- **Stock options** are **physically settled**: an ITM stock option at expiry leads to delivery (or receipt) of shares. Two practical consequences: (1) you must have the funds/margin to take delivery, and (2) most traders **square off** (close) stock options before expiry to avoid delivery.

Auto-exercise is the default for options that are ITM at expiry beyond a threshold, but the exact cut-off and timing are broker-specific — confirm your broker's policy rather than assuming.

## Costs and taxes

The statutory and transactional costs of an options trade in India are several, and they matter — especially for strategies with many legs or frequent turnover:

- **STT (Securities Transaction Tax)** — levied on the *sell side* of options (on the premium) and on exercise (on intrinsic value). Rates are set by the Union Budget and have changed over time.
- **Stamp duty** — on the buy side, per contract.
- **Exchange transaction charges, SEBI fees, GST on charges** — smaller but real.
- **Brokerage** — per-order, per-lot, or flat-fee, depending on the broker.

The rule of thumb: **a strategy must clear these costs on top of the premium.** A "breakeven" computed from premium alone is optimistic; add the round-trip costs, and a surprising number of marginal trades turn negative. This is especially true for high-frequency approaches and multi-leg strategies.

## Margin (SPAN) and leverage

Selling options (or holding spreads) requires **margin**, computed under the exchange's **SPAN** risk model:

- **Buying** an option requires only the premium (the premium is the maximum loss).
- **Selling** an option requires SPAN margin that models the position's worst-case loss — and this margin *changes* as the market moves and volatility changes.
- **Spreads** are margin-efficient: a defined-risk spread requires roughly the spread width in margin, not the full notional.

The discipline from Chapter 28 applies with Indian-specific force: **keep a margin buffer**, because an adverse volatility spike raises margin requirements and can force an involuntary exit from an otherwise sound position.

## Exercise and assignment flow

For the trader who holds to expiry:

1. The exchange **auto-exercises** options that are ITM at expiry (per its threshold rules).
2. The clearing corporation **assigns** the obligation to a matching short holder.
3. For index options, the ITM value is cash-settled; for stock options, delivery is executed and settlement obligations arise.

For the vast majority of strategies in this book, the cleanest path is to **close the position before expiry** (square off), which sidesteps exercise, assignment, and delivery entirely.

## Regulation and your own obligations

A closing note that matters more than any contract detail:

- **StratLab is not SEBI-registered**, and this book is education, not investment advice.
- Options are leveraged instruments with the potential for loss (including, on naked shorts, very large losses).
- You are solely responsible for your trading decisions, and you should consult a SEBI-registered adviser where appropriate.

The mechanics in this chapter are the *how*; the discipline in Chapters 28–29 is the *whether*. Both are necessary. Neither, alone, is sufficient.

## Summary

- NIFTY/BankNIFTY are the liquid, cash-settled workhorses; stock options add liquidity and delivery considerations.
- Lot sizes follow SEBI's minimum-contract-value rule and change over time — always verify.
- Weekly and monthly expiries offer different time-horizons; confirm the current weekly expiry weekday.
- Costs (STT, stamp, charges, brokerage) and SPAN margin materially affect profitability — model them.
- Most strategies are cleanest if closed (squared off) before expiry.
- Education, not advice: you are responsible for your own decisions.

This completes the main text. The appendices that follow are your reference layer: a glossary, a strategy quick-reference table, and a formula cheat sheet.
