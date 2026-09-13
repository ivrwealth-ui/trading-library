# Appendix — Chart-Type Quick Reference

This table is a summary, not a substitute for the full chapters.

| Chart | Keeps | Axis | Best for | Watch out |
|-------|-------|------|----------|-----------|
| Line / Area | Close only | Time | Clean long-term trend, closing S/R | Hides intra-period battle |
| Bar (OHLC) | O, H, L, C | Time | Precise full record, volatility | Slower to read than candles |
| Candlestick | O, H, L, C | Time | Fast reading, rejection/indecision, patterns | Noisy over long horizons |
| Heikin-Ashi | Averaged OHLC | Time | Smooth trend ribbon | Not real prices — no exact entries |
| Renko | Bricks (fixed move) | Movement | Pure trend, mechanical reversals | No time; reversal lag |
| Point & Figure | X/O columns | Movement | Levels, 45° trendlines, price targets | No time/volume; counts are estimates |
| Line break | 3-line close breaks | Movement | Confirmed close-based trend | Reversal confirmed late |
| Kagi | Thick/thin lines | Movement | Strength vs. weakness | Depends on reversal amount |

## The scale

- **Linear** = equal points. Use for short horizons, narrow ranges, absolute levels.
- **Log** = equal percentages. Use for long horizons, wide ranges, trendlines, and any price that has moved several multiples.

## The unifying idea

Every chart type is the same move — **discard the irrelevant dimension** — applied to a different axis:

- **Renko, P&F, line break, Kagi** discard *time* to leave pure **movement**.
- **The log scale** discards *absolute price* to leave pure **relative change**.

A chart is a filter; the master chooses which filter to look through.
