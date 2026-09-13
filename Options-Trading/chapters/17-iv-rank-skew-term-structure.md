# 17. IV Rank, IV Percentile, Skew, and the Term Structure

## IV in context: don't compare to nothing

A raw IV number is hard to act on. NIFTY ATM IV of 12% is "high" or "low" only relative to *NIFTY's own history*. This chapter gives you the three lenses for reading IV in context: **IV rank**, **IV percentile**, and the two structural patterns — **skew** and the **term structure**.

## IV Rank vs. IV Percentile

Both answer "where is today's IV relative to the recent past?", but they compute it differently.

**IV Rank** positions today's IV between the *minimum and maximum* of the past year (a common window):

IV Rank = (IV_now − IV_min) / (IV_max − IV_min)

- It runs 0 to 100.
- A rank of 80 means IV is in the top 20% of its recent *range*.
- Weakness: one extreme day (a crash) sets IV_max and can permanently compress the rest of the year's ranks to low numbers.

**IV Percentile** measures *what fraction of past days* had IV *lower* than today:

IV Percentile = (% of past observations below IV_now)

- Also 0–100, but robust to outliers: a single crash day barely moves the percentile.
- A percentile of 80 means IV is higher than 80% of the past year's observations.

**Use percentile for ranking, rank for range.** Both are shown by most platforms; the distinction matters mainly so you do not misread one as the other. In practice, most traders treat either as: *"0–25 = IV cheap, 75–100 = IV expensive."*

## Why rank/percentile matter

They turn "volatility" into an actionable **entry/exit filter**:

- **High IV rank/percentile** → options are historically expensive → the environment has historically favoured *premium-selling* strategies (credit spreads, condors, covered calls).
- **Low IV rank/percentile** → options are historically cheap → the environment has historically favoured *premium-buying* strategies (long calls/puts, straddles, calendars).

The honest caveat, stated as this book always states it: *historical conditions are a guide, not a promise.* But the pattern is one of the most robust in options — cheap volatility tends to precede periods of larger-than-priced moves, and expensive volatility tends to mean-revert lower.

## Skew: IV across strikes (the smile)

Plot IV against strike for a single expiry, and you usually do **not** get a flat line. You get a **skew** — a curve where OTM puts carry *higher* IV than ATM or OTM calls.

- In **equity and index markets**, the standard shape is a *smile* or *smirk*: OTM puts are more expensive (in IV terms) than equidistant OTM calls.
- **Why:** investors systematically buy downside protection (puts), bidding up their price — and therefore their IV. The market prices crashes as more likely than a normal distribution would suggest (the "fat tail" left side).

Skew has practical uses:

- **A steep skew** means downside protection is expensive; upside calls are comparatively cheap.
- **Skew changes** signal shifts in fear — a sudden steepening (puts repricing sharply higher) can precede or accompany market stress.
- **Relative-value trades** (e.g., risk reversals, put-spread vs. call-spread pricing) exploit skew differences.

For a NIFTY or BankNIFTY trader, the everyday takeaway is simple: *OTM puts are not priced symmetrically to OTM calls — downside is structurally more expensive.*

## Term structure: IV across expiries

Plot IV against expiry, and you get the **term structure**:

- **Contango** (the normal state in calm markets): longer-dated options have *higher* IV than shorter-dated ones. Uncertainty compounds with time.
- **Backwardation** (during stress): near-dated IV *spikes above* far-dated IV — fear is concentrated in the immediate future. This is a classic sign of an event or panic.

Term structure informs expiry choice:

- **Selling premium** is often more attractive in the near expiry where IV is highest in backwardation (but gamma risk is highest there too).
- **Buying premium** may be more efficient in a later expiry where IV is lower, or when contango means the longer-dated option is "cheaper" relative to its time.

## Putting the three lenses together

A complete IV read combines all three:

1. **Level (rank/percentile):** are options historically cheap or expensive *right now*?
2. **Skew:** how is fear distributed across *strikes* — is downside unusually expensive?
3. **Term structure:** how is fear distributed across *time* — is it concentrated near-term or spread out?

Example reading: *"NIFTY IV percentile is 85 (expensive), the term structure is in backwardation (fear concentrated near-term, likely ahead of an event), and skew is steep (heavy put buying). Options are rich; the market is bracing for a near-term downside shock."* That single sentence — assembled from three standard numbers — is more information than most traders extract from a full day of headlines.

## Summary

- IV rank and percentile position today's IV against its own history; 0–25 = cheap, 75–100 = expensive.
- High IV favours premium-selling strategies; low IV favours premium-buying strategies (historically).
- Skew: OTM puts are structurally more expensive than OTM calls in equity/index markets.
- Term structure: contango = far IV higher (calm); backwardation = near IV spiking (stress).
- Read all three together for a complete volatility picture.

This completes Part II. Next, Part III turns theory into positions: the strategy playbook.
