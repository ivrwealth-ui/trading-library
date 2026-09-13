# 23. Ratio, Calendar, and Diagonal Spreads

## Beyond direction and range

The strategies so far traded direction (verticals, long options) or magnitude (straddles, condors). Three further families trade **time** and **relative volatility** — the dimensions that only options have.

## Ratio spreads: uneven legs

A **ratio spread** is any spread where the two legs are of *unequal size* — typically buying one option and selling *more* of another at a different strike, same expiry and type.

The common example is the **call ratio spread** (e.g., buy 1 ATM call, sell 2 OTM calls) or the **put ratio spread** (buy 1 ATM put, sell 2 OTM puts).

- **View:** mildly directional to a *specific zone*, then flat — you expect a modest move toward the short strikes, but *not* a blow-off past them.
- **Payoff shape:** profits rise to a peak at the short strike, then *fall* as the extra naked short leg goes against you beyond it.
- **The defining risk:** the uneven leg means the position is **naked on one side** — a ratio spread has an **unbounded loss** on the over-short side. This is the price of entering the trade cheap (often for a net credit or near-zero debit).

Ratio spreads are an advanced tool precisely because of the naked tail. They are used to *finance* a directional view cheaply, but the trader must understand that beyond the short strike, the extra sold option behaves exactly like a naked short.

### Why they are used

- To **enter a directional trade for free or for a credit** when a modest move is expected.
- To **express a view that the market will not blow through a level** (sell the extra leg above resistance, say).

The trade-off is explicit: *cheap (or paid) entry in exchange for a naked tail.* They are not for beginners.

## Calendar (time) spreads: trading time

A **calendar spread** (also *time spread* or *horizontal spread*) is the same strike, same type, *different expiries*: typically **sell the near-dated option, buy the far-dated option** at the same strike.

- **View:** the market will stay *near the strike* over the near expiry — you are trading the *shape of time decay*, not direction.
- **The mechanic:** the near option decays *faster* than the far option (theta is higher near expiry). If the market stays put, the near option you sold loses value faster than the far option you own, and the spread widens in your favour.
- **Maximum profit:** realised if the underlying is *exactly* at the strike at the near expiry (the near option expires worthless, the far option retains maximum time value).
- **Maximum loss:** limited to the net debit paid (for a long calendar).
- **Greeks:** near-zero net delta (strike is ATM), **long vega** — a calendar is a *long-volatility* position that profits from stillness *at one price* and from rising volatility. It is unusual in combining "profit from no movement" with "likes higher vol."

Calendars are a subtle, low-risk, low-reward tool for expressing "the market will consolidate around this level." Their chief enemy is a *large move away* from the strike, which crushes the far option's time value while the near option's decay advantage has already been captured.

## Diagonal spreads: time + strike

A **diagonal spread** combines the two ideas: same type, but **different strikes and different expiries**. (E.g., buy a longer-dated call at a lower strike, sell a nearer-dated call at a higher strike.)

- **View:** mildly directional, with a time-decay component — you expect a *gradual* move in one direction, and want the near-dated short leg to decay faster.
- **The mechanic:** the short near-dated leg finances the long far-dated leg, and the position profits from the *differential* decay plus a modest directional move.
- **Why used:** diagonals are a cheaper way to hold a directional view than a plain long option, while retaining some time-value flexibility — they are the "income + direction" hybrid.

The family of calendar/diagonal spreads is the advanced trader's toolkit for *fine-tuning exposure across both strike and time simultaneously*. They are mechanically more complex than verticals and require understanding how theta differs across expiries.

## The common thread: trading the *structure* of the curve

All three families in this chapter exploit the same underlying fact: **different options decay, and respond to volatility, at different rates.** A vertical spread exploits the *strike* dimension; a calendar exploits the *time* dimension; a diagonal exploits both; a ratio spread exploits the *quantity* dimension (uneven legs). The sophisticated options trader is, at bottom, someone who sees the whole volatility surface (Chapter 17) and chooses where to be long and where to be short on it.

## Risk realism

A closing note on risk, because these are the strategies most likely to be underestimated:

- **Ratio spreads** carry a **naked** leg — unbounded risk on the over-sold side.
- **Calendars** can look "safe" but lose to a large move (and to a vol *crash*, despite being long vega, if the market gaps away).
- **Diagonals** carry directional risk from the offset strikes.

Each is a tool for a specific, well-understood view. None is a shortcut.

## Summary

- Ratio spreads: uneven legs, cheap entry, naked tail risk on the over-sold side.
- Calendar spreads: same strike, different expiry; trade the shape of time decay; long vega; profit from consolidation.
- Diagonal spreads: different strike and expiry; income + direction hybrid.
- All three trade the *structure* of time decay and volatility across the curve.
- None is risk-free; ratio spreads in particular are naked on one side.

Next: protective puts and collars — options as portfolio insurance.
