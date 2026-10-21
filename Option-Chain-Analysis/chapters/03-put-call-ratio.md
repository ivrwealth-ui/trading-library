# 3. The Put-Call Ratio and Its Two Faces

## One number, two readings

The **put-call ratio (PCR)** is the most famous single number in option chain analysis: the ratio of put activity to call activity. It condenses the market's *bearish vs. bullish* option positioning into one figure — and it has **two readings that point in opposite directions**, which is exactly why it is both powerful and dangerous.

## The definition (and the two versions)

There are two standard PCRs, and they answer different questions:

- **PCR (OI-based)** = total put open interest ÷ total call open interest. It measures *positioning* — where capital sits, persistently.
- **PCR (volume-based)** = total put volume ÷ total call volume. It measures *flow* — what is being traded today.

The OI version is the more stable, "conviction" measure (this book's focus); the volume version is the more reactive, "mood-of-the-day" measure. Both are useful; know which you are looking at.

## The two faces: trend vs. contrarian

Here is the crux. The PCR can be read in two opposite ways:

### Face 1 — the "positioning" reading (trend-following)

A **high PCR** (more puts than calls) means the market is positioned bearishly — investors are buying protection or betting on a decline. Read *straight*, a rising PCR = growing bearishness = a bearish signal.

### Face 2 — the "contrarian" reading (mean-reversion)

A **very high PCR** can also mean *everyone has already* bought their puts — the bearishness is *exhausted*, the "sell" is done, and the market is ripe to reverse *up*. Read *contrarian*, an extreme PCR is a *bullish* signal (and an extremely low PCR is a *bearish* one).

Both readings are legitimate; the difference is **the level**:

- **Mid-range PCR** — read it *with the trend* (a rising PCR = building bearishness).
- **Extreme PCR** — read it *contrarian* (a very high PCR = crowded bearishness, likely to snap back).

The practical problem — and the reason PCR alone is a weak signal — is that "extreme" is **regime-dependent**: a PCR of 1.3 might be extreme in a calm bull market but normal in a stressed bear market. PCR only becomes meaningful when read **relative to its own recent history** (its percentile), not as an absolute number.

## Building a usable PCR signal

A disciplined PCR model therefore does three things:

1. **Normalise** — compute the PCR's *percentile* (or z-score) over a rolling window (e.g., 60–250 days), so "extreme" is defined against the market's *own* behaviour, not a fixed number.
2. **Combine the two faces** — read the *level* for the trend signal and the *extreme* for the contrarian signal, explicitly rather than ambiguously.
3. **Confirm with price** — a PCR extreme that coincides with price action (a high PCR at a market *low*, a low PCR at a market *high*) is far more meaningful than a PCR extreme in isolation.

## The honest limitations

Three things PCR does *not* do, stated plainly:

1. **It does not know *why*.** A high PCR could be speculation (bearish bets) or *hedging* (investors buying puts to protect long stock). The hedging case is not bearish at all — it is *protective*. PCR conflates the two, which is why it is a weak signal on its own.
2. **It is not directional on its own.** The two-faces problem means a raw PCR number, without its percentile, is ambiguous — and ambiguity is not a signal.
3. **It is a positioning gauge, not a forecast.** PCR describes *where sentiment is*; it does not reliably predict *where price goes next*. It is a *context* input, to be combined with other signals (Chapter 13), not a standalone call.

## Summary

- PCR = puts ÷ calls; OI-based measures positioning, volume-based measures flow.
- Two faces: trend-following (mid-range) vs. contrarian (extreme).
- "Extreme" is regime-dependent — normalise to the PCR's own percentile.
- A usable signal: normalise, combine both faces, confirm with price.
- PCR does not know *why*, is not directional alone, and is a context input, not a forecast.

Next: implied volatility — skew and term structure.
