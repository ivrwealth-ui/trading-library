# 26. Gamma Scalping

## Turning movement into income

**Gamma scalping** is a technique for *harvesting* the movement that a long-gamma position is exposed to. It is the practical bridge between the abstract Greeks and a concrete, mechanical trading method — and it explains why a delta-neutral long-options position can make money even without a volatility rise, *if the market moves enough.*

## The setup: long gamma, delta-neutral

Start with a **long-gamma, delta-neutral** position — the classic example is a long straddle (long call + long put at the same strike), which has roughly zero delta and positive gamma.

Recall the Greeks of such a position:

- **Delta ≈ 0** — it does not care, at this instant, which way the market goes.
- **Gamma > 0** — as the market moves, delta *grows in the direction of the move*.
- **Theta < 0** — it pays a daily cost for holding this convexity.

The position is a bet that *movement* (gamma) will overcome *decay* (theta). Gamma scalping is the discipline of capturing that movement systematically.

## The mechanics of scalping

Because the position is long gamma, any market move pushes it *off* delta-neutral — and always in the profitable direction:

1. The market **rises**. The straddle's delta becomes positive (the call gains delta faster than the put loses it). The position is now *long* — and the rise has already helped it.
2. You **sell** enough of the underlying (or a delta-equivalent) to bring delta back to zero — *locking in* the gain from the rise.
3. The market **falls** back. The straddle's delta now becomes negative. The position is *short* — and the fall helps it again.
4. You **buy** enough underlying to bring delta back to zero — locking in the gain from the fall.

Repeat. Each round trip — **"buy low, sell high" on the hedge itself** — captures a small profit. The more the market oscillates, the more of these small profits you bank. This is the "scalp": you are not trading the option; you are *trading the hedge* around a convex option position.

## Why it works: the long-gamma edge

The reason gamma scalping is profitable (when it is) is that a long-gamma position is **long convexity**: it gains more on a move in its favour than it loses on an equal move against it. The rebalancing discipline *realises* that convexity as cash.

The condition for the whole exercise to be profitable over a holding period is:

**Realised volatility > implied volatility** (roughly — the realised movement, squared and summed, must exceed what the option's price implied).

This is the deep connection: a long straddle is a bet that *realised* volatility will exceed *implied*. If the market moves more than was priced in, gamma scalping captures the excess; the daily theta is the cost, and the scalps are the revenue.

## The flip side: short gamma is the mirror

The same mechanic, reversed, explains what happens to a **short-gamma** position (a short straddle, an iron condor):

- As the market moves, delta grows *against* the seller — to stay hedged, the seller must **buy high and sell low** on the hedge, locking in *losses* on every oscillation.

This is the precise, mechanical meaning of "picking up pennies in front of a steamroller": the short-gamma trader collects theta steadily, but every adverse oscillation forces a losing hedge trade, and a big move forces many of them. Gamma scalping is the *long* trader harvesting exactly what the *short* trader pays.

## Practical realities and costs

Gamma scalping is elegant in theory and expensive in practice, for three reasons:

1. **Transaction costs.** Every rebalance is a trade. In the Indian market, each round trip carries brokerage, STT, exchange charges, and the bid-ask spread. These eat the small scalp profits directly. Scalping is only viable where costs are low and liquidity is high (NIFTY/BankNIFTY near-the-money).
2. **Discrete rebalancing.** The theory assumes continuous rebalancing; reality is discrete. You choose a rebalance trigger — e.g., "rebalance when delta exceeds ±X" — and the choice of X trades off cost (smaller X = more trades) against risk (larger X = more unhedged drift).
3. **Gap risk.** Overnight gaps cannot be scalped — the market jumps past your rebalance point, and you rebalance *at the post-gap price*, having missed the move. Gaps are the long-gamma trader's friend (they help the option) but they make the *scalping* imperfect.

## When gamma scalping fits

Gamma scalping is a tool for a specific situation:

- A **long-gamma, delta-neutral** position you intend to *actively manage* rather than hold to expiry.
- **High realised volatility** (the market is choppy and moving) — the fuel for scalping.
- **Low transaction costs and high liquidity** — which in India means the index options, near the money.
- A willingness to be **active**: scalping is a *process*, not a set-and-forget position.

It is not a beginner technique, but it is the technique that *completes* the picture — once you understand gamma scalping, you understand what long gamma, short gamma, realised vs. implied, and theta all *mean* in cash terms.

## Summary

- Gamma scalping harvests movement from a long-gamma, delta-neutral position by repeatedly rebalancing delta to zero.
- Each rebalance locks in a small "buy low, sell high" profit on the hedge.
- Profitable when realised volatility exceeds implied; the daily theta is the cost.
- Short-gamma positions suffer the mirror: forced to buy high and sell low when hedging.
- Costs, discrete rebalancing, and gap risk make real-world scalping harder than theory — it needs liquid index options and an active hand.

Next: open interest, put-call ratio, and max pain — reading the market's positioning.
