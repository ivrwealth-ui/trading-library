# 8. The Payoff Diagram

## A picture of risk and reward

The **payoff diagram** (or P&L chart) is a graph of a position's profit or loss against the price of the underlying at expiry. It is the single most valuable tool in options because it converts an abstract strategy into a shape you can see: where you make money, where you lose, and how much, in every possible future.

Every strategy in Part III is accompanied by one. Learning to *draw* them (even mentally) is what separates traders who understand their risk from those who only hope.

## The axes

- **X-axis** — the underlying price at expiry.
- **Y-axis** — profit or loss (positive up, negative down).
- **Zero line** — the horizontal line through the middle; profit above, loss below.

## The long call payoff

Consider a NIFTY 25,000 call bought for ₹150 premium.

At expiry, ignoring costs:

- NIFTY ≤ 25,000: the call is worthless. **Loss = ₹150** (the premium).
- NIFTY = 25,150: the call's intrinsic value is exactly 150, covering the premium. **Profit = 0**. This is the **breakeven**.
- NIFTY > 25,150: every point above breakeven is profit.

The shape: a flat line at **−150** for all prices below the strike, then a **45° line rising** past the strike, crossing zero at breakeven. *Loss is capped; profit is unlimited.*

## The long put payoff

A NIFTY 25,000 put bought for ₹150:

- NIFTY ≥ 25,000: worthless. **Loss = ₹150**.
- NIFTY = 24,850: intrinsic value 150 → **breakeven**.
- NIFTY < 24,850: profit, growing as NIFTY falls, bounded only by NIFTY reaching zero.

Shape: flat at −150 above the strike, rising to the left as price falls. *Loss capped; profit large but finite.*

## The short (written) option payoffs

A **short** position is the exact mirror image of the long, flipped over the zero line:

- **Short call**: flat at **+premium** below the strike, then falling without limit above it.
- **Short put**: flat at **+premium** above the strike, then falling (bounded at strike) below it.

This mirror symmetry is the visual form of the buyer/seller asymmetry from Chapter 3: the seller's diagram is the buyer's upside-down.

## Reading a breakeven from the diagram

The **breakeven** is where the payoff line crosses the zero line. It answers: "where does the underlying need to be at expiry for me to neither gain nor lose?"

- Long call breakeven = **strike + premium**.
- Long put breakeven = **strike − premium**.
- Short call breakeven = **strike + premium**.
- Short put breakeven = **strike − premium**.

For combinations (spreads, straddles, condors), there can be **two breakevens**, and the diagram shows both as the points where the line crosses zero.

## Why diagrams beat intuition

Human intuition about options is famously unreliable. The diagram imposes discipline:

- It forces you to state your **maximum loss** — the lowest point on the curve.
- It forces you to state your **maximum profit** — the highest point.
- It shows you the **range of prices where you lose**, not just the single outcome you are hoping for.

A trader who cannot draw the diagram of their own position does not fully understand the position. This book's rule of thumb: *if you cannot sketch the payoff diagram, do not place the trade.*

## The three canonical shapes

Almost every strategy's diagram falls into one of a few families:

1. **Directional** — the line rises (bullish) or falls (bearish) with price, with a flat "risk" floor/ceiling from the option's premium. (Long/short call/put.)
2. **Ranged** — the line peaks *inside* a price range and falls outside it (a "tent"), or the mirror: flat-topped profit inside a range with loss outside (a "table" or "plateau"). (Spreads, condors, butterflies.)
3. **Volatility** — the line is V-shaped, profiting from large moves in *either* direction (straddle, strangle), or the mirror: an inverted-V that profits from stillness.

Once you can place any strategy into one of these three families, you understand its essential bet — *direction, range, or magnitude of movement.*

## Beyond expiry: the "now" curve

The payoff diagram is strictly an *at-expiry* picture. But the same idea, drawn *before* expiry, produces a smooth curve (the position's value today across possible prices) rather than a kinked line. This "profit/loss today" curve is what the Greeks (Part II) describe point by point. The at-expiry diagram tells you the *destination*; the Greeks tell you the *path*.

## Summary

- The payoff diagram plots P&L against underlying price at expiry.
- Buyers: capped loss, open reward. Sellers: capped reward, open loss.
- Breakevens: call = strike + premium; put = strike − premium.
- Strategies fall into directional, range, or volatility shapes.
- If you cannot draw the diagram, you do not understand the position.

Next: the reasons people trade options at all — hedging, income, and speculation.
