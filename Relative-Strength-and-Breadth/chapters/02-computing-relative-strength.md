# 2. Computing Relative Strength

## The RS ratio, step by step

1. Choose a benchmark (Nifty 50 for large-caps, Nifty 500 for broader).
2. Normalise both to a common base: `Normalised price = Price ÷ Price at start of window`.
3. Compute the ratio: `RS ratio = Normalised stock ÷ Normalised benchmark`.
4. Plot the ratio over time.

**How to read the ratio line:**

- A **rising** RS line while the index is flat or down = genuine leadership (the stock is doing it on its own, not just drifting up with the tide).
- A **falling** RS line while the index rises = the stock is a laggard in a rising market — it is *underperforming* even as it goes up in price.
- A **breakout in the RS line** (ratio making a new high) often *precedes or coincides with* a price breakout — it is a confirmation that the move is leadership, not just beta.

## The RS rank, step by step

1. Compute the return of every stock in the universe over the chosen window (e.g. 6 months).
2. Sort all returns.
3. Assign a percentile to each (0 = worst, 100 = best).

**How to read the rank:**

- Above ~80th percentile = strong relative strength (leadership).
- Below ~20th percentile = weak relative strength (laggard).
- The **middle** is where most stocks live and where the signal is weakest.

## Choosing the window

The window changes what the RS is measuring:

| Window | What it captures | Use for |
|---|---|---|
| 1–3 months | Short-term momentum | Tactical rotation, trend confirmation |
| 6 months | Intermediate trend | Core ranking, most-used window |
| 12 months | Sustained leadership | Positional / long-horizon selection |

**How to read:** long-horizon RS (12-month) is the most stable and least noisy; short-horizon RS flips quickly. Many practitioners rank on 6-month RS and confirm with 3-month and 12-month to avoid whipsaw.
