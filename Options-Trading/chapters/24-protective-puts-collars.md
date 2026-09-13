# 24. Protective Puts and Collars

## Options as insurance

Hedging was the first motive listed in Chapter 9, and it is the oldest reason derivatives exist. This chapter covers the two canonical hedges for a long portfolio: the **protective put** and the **collar**.

## The protective put

- **Structure:** hold the underlying (or a portfolio of holdings) **and** buy a put against it.
- **View:** you are not necessarily bearish — you want to **keep the upside while capping the downside**. It is insurance on an asset you intend to keep.
- **Maximum loss:** capped at (entry price − strike) + premium paid. No matter how far the market falls, the put's gain offsets the holding's loss below the strike.
- **Maximum profit:** effectively unlimited — if the market rises, you keep the gains, less the premium (the "insurance cost").
- **Greeks:** the put's short delta *partially* offsets the holding's long delta (net: reduced but still long), and the put adds long gamma and vega — exactly what you want in a crash.

### How it works

Imagine holding NIFTY exposure (via a portfolio or an index fund) at 25,000, and buying a 24,500 put for ₹60.

- **Above 24,500:** the put is worthless; you lose the ₹60 premium, but keep all upside.
- **Below 24,500:** the put gains 1-for-1 with the fall, offsetting the portfolio's loss. Your maximum loss is 25,000 − 24,500 + 60 = **₹560** (a ~2.2% cap), no matter how far the market crashes.

This is the essence of hedging: **a known, bounded worst case in exchange for a premium.**

### The cost of insurance

The honest trade-off is that insurance is *not free*, and over time it is *expensive*: if you buy a protective put every month and the market does not crash, the premiums steadily reduce your returns. This is the same variance-risk-premium dynamic from Chapter 16 — systematically buying protection costs money on average, because the market prices puts slightly rich relative to what usually happens.

For this reason, protective puts are used *selectively* — when risk is elevated (ahead of a major event, at high valuations, during high volatility), or by investors for whom a hard floor is worth the cost. It is a choice about *risk tolerance and time horizon*, not a permanent overlay.

## The collar

- **Structure:** hold the underlying, **buy a protective put** (below) **and sell a covered call** (above) to *finance* it. A "zero-cost collar" sells a call whose premium equals the put's premium.
- **View:** protect against a large decline, accept a **cap on the upside** to pay for it.
- **Maximum loss:** capped at (entry − put strike) ± net premium.
- **Maximum profit:** capped at (call strike − entry) ± net premium.

The collar is the protective put made **cost-neutral**: the premium from the call you sell pays for the put you buy. In exchange, you give up the upside beyond the call strike.

### Why a collar

A collar answers the classic dilemma: *"I want the protection of a put, but I don't want to pay for it."* By selling the call, you accept a ceiling on gains in return for a floor on losses, at roughly zero net cost.

The collar is most attractive when:
- You are worried about a near-term decline but do not expect a strong rally.
- Implied volatility is elevated (you sell the call into rich premium, subsidising the put).
- You hold a concentrated position with limited willingness to sell.

## Hedging an Indian index portfolio

For an investor holding a diversified Indian equity portfolio, the practical hedge is **NIFTY (or BankNIFTY) index puts**, not stock puts — because index puts hedge *market* risk (beta), which is the risk a diversified portfolio mostly faces. The mechanics:

1. Estimate the portfolio's **NIFTY-equivalent exposure** (its beta-adjusted notional).
2. Compute how many NIFTY put lots cover that exposure (each lot covers lot size × strike of index value).
3. Buy the puts at a strike that reflects the maximum acceptable drawdown.

This is a standard, mechanical exercise in *sizing* — the same risk-management discipline as Chapter 28, applied to protection rather than speculation. (An index hedge hedges market risk, not the idiosyncratic risk of a single stock, so concentrated positions need stock-specific hedges instead.)

## The psychology of hedging

Hedging is psychologically hard for two reasons:

1. **It costs money in the good times** — the premium feels like a loss every time the market does *not* crash.
2. **It only "works" in the bad times** — and by then, if you did not already own it, it is expensive or unavailable.

This is the same logic as fire insurance on a house: you pay for years of "nothing happening" so that the one fire does not destroy you. The disciplined hedger accepts the drag as the price of *surviving* to keep compounding.

## Summary

- Protective put: keep the asset, buy a put; caps downside at (entry − strike + premium), preserves upside, costs premium.
- Collar: protective put financed by a short call; cost-neutral, caps both downside and upside.
- Index puts hedge market (beta) risk; stock puts hedge single-name risk.
- Hedging is insurance: it costs in calm times and pays in crashes — and only works if bought *before* the crash.

This completes Part III. Next, Part IV turns to the advanced topics: volatility trading, gamma scalping, and market intelligence.
