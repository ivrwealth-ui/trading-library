# 25. Volatility Trading and Vega Management

## Making vega the point

Every options trade has a vega (Chapter 13), but *volatility trading* is the discipline of making vega the *deliberate* centre of the trade — neutralising direction (delta) so that what remains is a pure bet on whether volatility will rise or fall, or whether realised movement will exceed what was priced.

This chapter pulls together the vol framework that has run through the whole book: **IV rank/percentile, skew, term structure, and the variance risk premium.**

## The core decision: long vol or short vol?

At the highest level, every volatility position is one of two things:

1. **Long volatility** — you own options (or option-like convexity). You profit if volatility *rises* or if the market *moves more than priced*.
2. **Short volatility** — you sell options. You collect premium and profit if volatility *falls* or the market *moves less than priced*.

The decision is made by comparing **the volatility you can buy/sell** against **the volatility you expect**:

- **IV is cheap** (low rank/percentile) and you expect bigger moves → **long vol** (buy straddles, strangles, calendars, long gamma).
- **IV is expensive** (high rank/percentile) and you expect calmer markets → **short vol** (sell condors, credit spreads, covered calls, short strangles).

This is the entire strategy of volatility trading: **buy low IV, sell high IV** — the options-market version of "buy low, sell high."

## Isolating the vol bet: delta-hedging

To trade volatility *and nothing else*, you must remove the directional component. The standard technique is **delta-hedging**: combine an option position with an offsetting position in the underlying (or another option) so the net delta is zero.

- A **long straddle** is already roughly delta-neutral (the call's +0.5 and the put's −0.5 cancel). It is a *mostly-pure* long-vol position.
- A **short strangle** is delta-neutral but short vol.
- A single long call is *not* neutral — it is a directional bet with a vega component. To make it a vol trade, you short delta-equivalent underlying (delta-hedge it), leaving pure long vega + long gamma.

Once delta-neutral, the position's P&L is driven by two things: **vega** (does IV change?) and **gamma** (does the market move?). This is the doorway to gamma scalping (next chapter).

## Vega management across a portfolio

For a trader holding many options, **net vega** is the key aggregate number:

- **Net long vega** → you want volatility to rise; a vol spike helps, a vol crush hurts.
- **Net short vega** → you want volatility to fall; a vol spike hurts, a vol crush helps.
- **Vega-neutral** → your P&L is insulated from pure IV moves (though not from *realised* moves, which hit gamma).

Managing net vega is how professional desks express a volatility view *across* an entire book, not just trade-by-trade. The same tools — IV rank/percentile for level, skew for strike choice, term structure for expiry choice — apply.

## The two ways to profit from a vol view

There are two distinct profit engines in volatility trading, and they are often confused:

1. **Vega P&L** — you profit because *IV itself changes* (the option reprices). Buy before a vol spike, sell before a vol crush. This is a bet on the *market's expectation* changing.
2. **Gamma/theta P&L** — you profit because *realised* movement differs from priced movement. A long-gamma position, rebalanced (gamma scalping), profits when realised volatility exceeds implied; a short-gamma position profits when realised is below implied.

The distinction matters because a trade can be *right on vega* but *wrong on realised* (or vice versa). The most sophisticated vol traders think about *both* — the level of IV (vega) and the gap between IV and what will actually happen (gamma/theta).

## The variance risk premium, honestly

The book has repeatedly referenced the **variance risk premium**: on average, across markets and time, **implied volatility exceeds realised volatility** — options are priced a little rich relative to what actually happens. This is why systematic short-vol strategies have historically earned a premium.

The honest, compliant framing matters here: *historically, conditions of persistently elevated IV have favoured reduced exposure to option buying (or increased exposure to premium collection), and conditions of low IV have favoured the reverse — but the short-vol edge is a risk premium, not a certainty, and it is punctuated by sharp losses precisely when realised volatility spikes.* Any volatility strategy must be sized to survive those spikes.

## Practical checklist for a vol trade

1. **Level:** IV rank/percentile — is vol cheap or expensive?
2. **Shape:** skew (is downside rich?) and term structure (is fear near-term?).
3. **Direction:** neutralise delta to isolate the vol bet.
4. **Engine:** are you trading *vega* (IV will change) or *gamma/theta* (realised vs. implied)?
5. **Risk:** size for the tail — short vol needs hard loss limits; long vol needs time to be right.

## Summary

- Volatility trading makes vega the centre, neutralising delta.
- Long vol = buy options (own convexity); short vol = sell options (collect premium).
- Buy low IV, sell high IV — the options version of buy-low-sell-high.
- Delta-hedging isolates the vol bet; net vega summarises a portfolio's vol exposure.
- Two profit engines: vega P&L (IV changes) and gamma/theta P&L (realised vs. implied).
- The variance risk premium is real but it is a *risk* premium — size for the spikes.

Next: gamma scalping — harvesting the movement a long-gamma position is exposed to.
