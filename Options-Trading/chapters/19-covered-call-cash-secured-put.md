# 19. The Covered Call and the Cash-Secured Put

## The income foundations

These two strategies are where most traders first meet option *selling*. Crucially, both are **covered** — the seller holds an offsetting asset, so the risk is not the naked, unbounded risk of a bare short call. They are the "asset-backed" way to collect premium.

## The covered call

- **Structure:** own the underlying (or a long future) **and** sell a call against it, typically above the current price.
- **Market view:** mildly bullish to neutral — you expect the underlying to stay flat or rise modestly, *not* to surge past the short strike.
- **Maximum profit:** limited. Achieved if the underlying is at or above the short strike at expiry: (K − entry price) + premium received.
- **Maximum loss:** large — you still own the underlying, so you bear its full downside, less the premium collected (premium reduces, but does not cap, the loss).
- **Breakeven:** entry price − premium received.
- **Greeks:** net short vega (and short call gamma), but with the underlying's delta offsetting much of the short call's delta — the net position is still net long the market, just less so than holding the asset naked.

### Why it is used

A covered call converts a stagnant holding into one that also pays a "rent." If the underlying stays below the strike, the call expires worthless and you keep the premium (income). If it rises past the strike, your upside is capped — you effectively agree to "sell" at the strike.

The honest trade-off: you **give up upside beyond the strike in exchange for premium now**, while *retaining all the downside* (only slightly cushioned). It is not a free lunch; it is a decision to accept a cap in return for income, on an asset you already hold.

## The cash-secured put

- **Structure:** sell a put at strike K while holding enough cash to buy the underlying at K if assigned (i.e., the put is "cash-secured," not naked).
- **Market view:** mildly bullish to neutral — you expect the underlying to stay above K, and are willing to buy it at K if it falls.
- **Maximum profit:** the premium received (if the put expires worthless).
- **Maximum loss:** large — if the underlying falls, you are obligated to buy at K, and your loss is (K − underlying at expiry) − premium, bounded only by the underlying reaching zero.
- **Breakeven:** K − premium.
- **Greeks:** short vega, short put gamma; net long the market (a short put is a bullish position).

### Why it is used

The cash-secured put is a way to **get paid to place a limit-buy order**. A trader willing to buy the underlying at a lower price sells a put at that strike; if the market never falls there, they keep the premium; if it does, they buy at a price they had already decided was attractive (effectively at K − premium).

This is the classic "buy the dip, and get paid to wait" structure — used by long-term investors who want to accumulate an asset at a better level.

## The two strategies compared

| | Covered call | Cash-secured put |
|---|---|---|
| Requires holding | Underlying (or future) | Cash (or margin) |
| Collects | Call premium | Put premium |
| Wins if | Underlying stays below/around strike | Underlying stays above strike |
| Gives up | Upside above strike | Buys at strike if market falls |
| Net direction | Mildly bullish | Mildly bullish |

Both are **short volatility** (short vega), both are **mildly bullish**, and both carry **large (though not unbounded) downside**. The covered call carries downside because you own the asset; the cash-secured put carries downside because you may be forced to buy a falling asset.

## The risk that hides in the "safe" label

Because these are covered, they are often called "safe" or "conservative." The safety is relative — it removes the *unbounded* loss of a naked short call, but it does not remove loss. A covered call can still lose badly in a market crash (the underlying falls, the premium only partly cushions). A cash-secured put can lose badly in a sharp decline (you buy at a strike far above the new price).

The disciplined view: **these are still short-volatility positions.** They win in calm, sideways-to-up markets and lose in sharp down-moves. The premium is compensation for that tail risk, not a dividend.

## When each fits (historically)

- Covered call: flat-to-mildly-up markets, moderate-to-high IV (you collect richer premium), on a holding you intend to keep.
- Cash-secured put: a trader with cash who wants to accumulate at a lower price; high IV makes the premium more attractive for the obligation taken.

Both are most forgiving in the environments where IV is elevated (rich premium) and the market is not crashing.

## Summary

- Covered call: own the asset, sell a call; income now, capped upside, uncapped downside (slightly cushioned).
- Cash-secured put: sell a put against cash; paid to place a limit-buy, but may buy a falling asset.
- Both are covered (no unbounded naked risk), short vega, mildly bullish.
- "Covered" removes unbounded risk, not risk; both lose in sharp declines.

Next: vertical spreads — the defined-risk way to express a directional view.
