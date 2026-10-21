# 11. The Expected Move and Event Pricing

## The chain's single best forecast

If the implied distribution (Chapter 9) is the *full* forecast, the **expected move** is its most useful *summary*: the market's estimate of how far the underlying is likely to move over a given period. It is the chain's answer to the question every trader asks — *"how big a move is priced in?"* — and it is the foundation for judging whether a view, or an event, is fairly priced.

## The definition

The expected move is the market-implied **one-standard-deviation move** over the period to expiry — the range within which the underlying is expected to land about two-thirds of the time.

There are three standard ways to read it, in increasing sophistication:

### 1. The ATM straddle price

The simplest: the price of the **at-the-money straddle** (call + put at the money) is approximately the expected move. The straddle's price is, in effect, the market's fee for betting on "a move of at least this size in either direction" — so it *is* the market's move estimate.

Expected move ≈ ATM call price + ATM put price

(More precisely, the ATM straddle is worth about 0.8 of the 1σ move — √(2/π) ≈ 0.8 — so 1σ ≈ 1.25 × straddle. The straddle alone slightly understates the 1σ range.)

### 2. The √time formula (from IV)

From the ATM **implied volatility** (Chapter 4), the 1σ move scales by the square root of time:

Expected move (1σ) ≈ S × IV × √(T / 252)

where S is the underlying price, IV is the annualised ATM implied volatility (decimal), T is trading days to expiry, and 252 is trading days per year.

### 3. The full-distribution percentiles

Most precisely, read the expected move off the **implied distribution** (Chapter 9): the 1σ move is the distance from the centre to the 16th/84th percentiles; the "1-in-10" move is the 5th/95th percentiles (10% of outcomes fall outside that range, 5% in each tail), and so on. This captures the *skew* that the symmetric √time formula ignores.

## Why the expected move matters

The expected move is the *benchmark* against which every view must be judged. Its core use:

> **A view is only worth acting on if the move you expect is *different from* the move already priced in.**

- If you expect a 300-point NIFTY move and the chain prices a 200-point move, your edge is 100 points — *that* is worth expressing.
- If you expect a 300-point move and the chain *already prices* 400 points, you have no edge — the market expects more than you do.

This is the single most valuable habit in option analysis: **before any directional or event trade, ask what the chain is already pricing.** The expected move is the number that answers it.

## Event pricing: the expected move around an event

The expected move reaches its peak usefulness around **events** (budgets, elections, rate decisions, earnings). The chain prices the event *in advance*:

- **Before the event**, IV — and therefore the expected move — rises (the market is pricing uncertainty).
- **After the event**, IV collapses back (the "volatility crush" of *The Complete Options Trader*), because the uncertainty resolved.

This produces the classic, recurring pattern: **the expected move before an event is the market's estimate of "how big will this event's move be?"** — and a trader buying options into the event must beat *that* estimate, not just "be right about the direction."

### A worked example (conceptual)

NIFTY at 25,000, one day before a major budget, weekly expiry 2 trading days away:

- ATM IV is 25% (annualised). Expected 1σ move over 2 days ≈ 25,000 × 0.25 × √(2/252) ≈ 25,000 × 0.25 × 0.089 ≈ **556 points**.

So the chain prices a ~556-point (1σ) move around the budget. A trader who expects a *smaller* move believes options are overpriced (a case for selling); one who expects a *larger* move believes they are cheap (a case for buying). The number converts "is the event priced in?" into a concrete, answerable question.

## The honest caveats

1. **The expected move is a *range*, not a target.** 1σ means "within this range ~68% of the time" — the market will move *more* than the expected move about a third of the time. It is not a promise; it is a central tendency.
2. **It is the *risk-neutral* expectation** (Chapter 9's caveat) — slightly biased by the risk premium. For practical purposes it is an excellent estimate, but it is not the *true* expected move.
3. **It is a snapshot.** The expected move changes as IV changes; an event's pricing evolves as the event approaches. Read it *at decision time*, not from memory.

## Summary

- The expected move is the market-implied 1σ move over the period to expiry.
- Read it via the ATM straddle price, the √time formula, or the distribution's percentiles.
- It is the benchmark: a view is only worth acting on if your move ≠ the priced move.
- Around events, IV (and the expected move) rises before and collapses after — the "is it priced in?" question, made numeric.
- It is a range (1σ ≈ 68% of the time), risk-neutral, and a snapshot — not a target.

Next: option-implied support and resistance.
