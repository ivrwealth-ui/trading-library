# 4. Position Sizing Methods

## Five ways to set the size

The 1–2% rule says *how much to risk*; the sizing methods say *how to translate that risk into a number of shares or contracts*. This chapter presents five methods, from the simplest to the most sophisticated, with their logic and their failure modes. All are variants of the same principle: **size from risk, not from conviction.**

## Method 1 — Fixed fraction

Risk a **constant percentage** of current equity on every trade.

Position size = (Equity × Risk%) ÷ (Entry − Stop)

This is the default method, and it has a crucial property: **it scales with the account.** As equity grows, positions grow (compounding); as equity shrinks, positions shrink (automatic de-risking after losses). Fixed-fraction is self-stabilising — after a losing streak, it automatically reduces size, which is exactly the correct behaviour.

- **Strength:** simple, self-correcting, ruin-resistant.
- **Weakness:** after a large loss, it reduces size so much that recovery is slow (the "shrinking bet" effect).

## Method 2 — Fixed ratio

Increase position size by a **fixed unit** for each fixed profit increment, rather than continuously. The idea (popularised by Ryan Jones) is to grow positions *stair-step-wise* as equity grows, but to *never* reduce below the current step on a loss.

- **Logic:** a steadier, less jumpy growth path than raw fixed-fraction, and a deliberate anti-shrinkage bias.
- **Strength:** protects capital while growing, without the aggressive drawdown of aggressive compounding.
- **Weakness:** more parameters to choose (the "delta" per step), and it can still over-leverage in a fast run-up if the steps are set too large.

## Method 3 — Volatility / ATR sizing

Size positions **inversely to volatility**, so that a volatile asset gets a smaller position and a calm asset gets a larger one — equalising the *expected* swing, not just the stop distance.

Position size = (Equity × Risk%) ÷ (k × ATR)

where ATR (Average True Range) measures the asset's typical daily range, and `k` is a multiplier (commonly 2–3) setting how many "days of range" you are risking.

- **Logic:** a ₹500 stock that moves ₹50/day is a different animal from a ₹500 stock that moves ₹5/day. Volatility sizing equalises them, so each position carries the same *market risk*.
- **Strength:** risk is normalised across volatile and calm assets; essential when trading across very different instruments.
- **Weakness:** ATR changes over time, so position size drifts; and in a volatility spike, size shrinks sharply (which is protective, but can feel like missing moves).

## Method 4 — Kelly criterion

The Kelly formula gives the **fraction of equity that maximises long-run growth** for a known edge:

Kelly fraction = (p·W − q·L) / W  (or the more general: f = p − q / (W/L))

where `p` = win rate, `q` = 1 − p, `W` = average win, `L` = average loss.

- **Logic:** the mathematically optimal bet size for compounding, given perfect knowledge of your edge.
- **Strength:** maximises long-run growth *in theory*.
- **Weakness:** it assumes you *know* your true edge precisely — which no trader does. Full Kelly is wildly aggressive (it routinely recommends risking 20–40%), and any error in estimating your edge makes it over-bet and increases ruin risk. This is why full Kelly is a theoretical ideal, not a practical rule.

## Method 5 — Fractional Kelly

Use a **fraction of the Kelly size** — commonly **half-Kelly or quarter-Kelly** — to capture most of the growth benefit while cutting the ruin risk dramatically.

- **Logic:** the growth curve near full Kelly is flat at the top (a bit less than Kelly is nearly as good), but the ruin risk is steeply lower. Half-Kelly gives roughly three-quarters of the growth for a fraction of the volatility and ruin risk.
- **Strength:** the best practical compromise between growth and safety — *if* you can estimate your edge.
- **Weakness:** still depends on estimating win rate and payoff; and for most retail traders, a simple fixed-fraction (Method 1) at 1–2% is both simpler and safer than any Kelly variant.

## Choosing a method

The honest guidance:

- **Start with fixed fraction (Method 1)** at 1–2%. It is sufficient, simple, and ruin-resistant.
- **Add volatility sizing (Method 3)** when you trade across assets of very different volatility (e.g., NIFTY futures and a small-cap stock).
- **Treat Kelly (Methods 4–5) as a diagnostic, not a rule** — use it to understand what your edge *implies*, but size far below it (quarter-Kelly at most), because your edge estimate is almost certainly too optimistic.

Every method fails the same way — **over-betting** — and the defence is always the same: size from risk, prefer smaller, and let compounding do the work over time rather than leverage.

## Summary

- Fixed fraction: constant % of equity; self-stabilising; the default.
- Fixed ratio: stair-step growth, anti-shrinkage; more parameters.
- Volatility/ATR: size inversely to volatility; equalises market risk.
- Kelly: theoretical optimum; assumes perfect edge knowledge; too aggressive in practice.
- Fractional Kelly: most of the growth, far less ruin risk; still needs an edge estimate.

Next: stops — the other half of "risk = entry − stop".
