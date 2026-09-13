# 8. Strategy 5 — The Pullback to the Rising Moving Average

## Buying strength on sale

The first four strategies are **breakout**-style: they buy *new* strength. This fifth strategy is the **pullback** style: it buys strength that has *paused*. In an established uptrend, price frequently pulls back toward a rising moving average before resuming — and that pullback is often a lower-risk entry than the breakout itself.

## The idea

Trends do not move in a straight line. An uptrend advances in waves: up, small retreat, up again. The retreat (the **pullback**) shakes out weak holders and offers a better entry — *if* the trend is intact. The pullback strategy is therefore: **identify an uptrend, wait for a pullback to a rising moving average, and enter as the trend resumes.**

The moving average here is the *anchor* — a level of dynamic support in an uptrend. Because the strategy only trades *with* the trend (never against it), it has a higher win rate than breakout entries, at the cost of occasionally missing the move entirely if the pullback never reaches the MA.

## The rules

**Universe and timeframe:** liquid stocks or index instruments in a *defined uptrend*. Daily timeframe.

**Step 1 — Define the trend:** price must be **above a rising longer-term MA** (e.g., the 50-day or 200-day MA sloping up). Only uptrends qualify.

**Step 2 — Wait for the pullback:** price pulls back **toward** (and often touches) a shorter MA — commonly the **20-day EMA** — while the longer-term trend remains intact.

**Step 3 — Enter on the resume:** enter when the pullback shows a **reversal back up** — e.g., a bullish candle off the 20-day EMA, or a close back above a short-term level. (Some implementations simply enter at the first touch of the MA and rely on the stop.)

**Step 4 — Stop and exit:**
- **Stop:** below the pullback low (or below the MA by a defined buffer), so a genuine trend failure exits the trade.
- **Exit:** a close below the longer-term MA (the trend filter), or a trailing stop as the trend progresses.

**Position sizing:** risk a fixed fraction of capital between entry and stop.

## Historical context

"Buy the dip in an uptrend" is one of the oldest and most widely practised momentum techniques, and its logic is the same as the momentum factor's: a trend that is intact is more likely to continue than reverse. Pullback entries are the practical expression of *trend continuation* — the observation that, in a trending market, retracements tend to be temporary and followed by new highs. (It is the mirror image of mean-reversion, which would *fade* the same pullback; the distinction — trend vs. range — is everything.)

## A worked example (a liquid NSE stock)

- A stock is in a clear uptrend, trading above a **rising 50-day MA**. The 20-day EMA is rising beneath it.
- The stock advances from ₹500 to ₹600, then **pulls back over two weeks to ₹560**, touching the rising 20-day EMA, which is now at ₹565.
- The 50-day MA is still rising (uptrend intact), and a **bullish candle** forms off the 20-day EMA. **Entry** at ₹570.
- **Stop** placed at ₹540 (below the pullback low of ₹545).
- The trend resumes, and the stock climbs to ₹680. The trader holds, trailing the stop up under each new pullback low, eventually exiting at ₹650.

Result: entry ₹570 → exit ₹650 = **+14%**, entered near a low-risk point with a tight, well-defined stop — versus buying the ₹600 breakout and absorbing the pullback.

## Risks and limitations

- **Trend failure.** The defining risk: the "pullback" turns out to be the start of a reversal, not a pause. The stop below the pullback low is what converts this into a small, defined loss.
- **Missing entries.** In strong trends, price may *not* pull back to the MA, and the trader waits (or misses the move). This is the cost of demanding a better price.
- **Ambiguity.** "Trend intact" and "pullback to the MA" are judgement calls; the strategy is more discretionary than the mechanical breakout systems. Clear written rules reduce this.
- **Requires an existing trend.** In a range, there is no uptrend to pull back to, and the strategy should simply not trade.

## Summary

- Buy pullbacks to a rising MA within an established uptrend; stop below the pullback low.
- Higher win rate, better entry price — but requires an existing trend and clear discipline.
- The mirror image of mean reversion; the trend-vs-range distinction is everything.
- More discretionary than breakout systems; write the rules down.

Next: the part that matters most — risk management and position sizing.
