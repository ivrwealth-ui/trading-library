# 5. Strategy 2 — Moving-Average Trend Following

## Riding the trend with a single line

If the Donchian breakout is the "new high" way to follow a trend, **moving-average trend following** is the "staying on the right side of the trend" way. It uses a moving average (or two) as both an entry and an exit signal — a smoother, slower, and more patient approach than breakout trading.

## The idea

The core rule is simple: **be long when price is above a long moving average, and out (or short) when below.** The moving average acts as a *trend filter* — it does not predict, it merely classifies *which regime we are in*. Most of the strategy's returns come from avoiding large drawdowns: when the market is in a sustained downtrend, price is below the MA and the trader is safely out of the market.

This is why trend following is often described as "participation with a brake": you participate in the good times and sit out the bad ones.

## The rules

**Universe and timeframe:** broad index exposure (NIFTY/BankNIFTY) or a diversified basket of liquid stocks. Daily timeframe.

**The signal (two equivalent forms):**

1. **Price vs. MA:** long when price is **above the 200-day MA**; exit when price closes **below the 200-day MA**.
2. **MA crossover:** long when a faster MA (e.g., 50-day) crosses **above** a slower MA (e.g., 200-day) — the "golden cross"; exit on the opposite ("death cross").

**Entry:** at the close of the day the signal fires.

**Exit:** at the close of the day the opposite signal fires. There is no profit target — the position runs until the trend filter breaks.

**Position sizing:** a fixed fraction of capital per position; or, for a portfolio, hold the basket only while the index itself is above its 200-day MA (a "regime gate" that de-risks everything at once).

## Historical context

The 200-day moving average is among the most studied rules in finance. In well-known research on tactical asset allocation (most prominently associated with Meb Faber's work), a simple "above the 200-day MA = invested, below = cash" rule has historically delivered much of the market's return while meaningfully reducing maximum drawdown, across many markets and long periods. The pattern is broadly documented: *being out of the market during sustained downtrends is worth more than being early during recoveries.*

## A worked example (NIFTY)

- NIFTY has been below its 200-day MA for months, in a downtrend. The trader is in cash (or short), preserving capital.
- A recovery begins. NIFTY **closes above its 200-day MA at 22,800**. **Entry** at 22,800.
- NIFTY trends higher for a year, reaching 25,500, staying above the 200-day MA throughout. The trader simply holds — no target, no top-calling.
- A correction follows; NIFTY **closes below the 200-day MA at 24,900**. **Exit** at 24,900.

Result: entry 22,800 → exit 24,900 = **+2,100 points** over a year, with one trade, one entry, one exit. The strategy gave up the first ~5% of the recovery (waiting for the crossover) and the last ~2% (waiting for the breakdown), but captured the reliable middle — and, crucially, was out of the market for the prior downtrend.

## Risks and limitations

- **Lag.** The MA is slow by design; it always gives up part of every move at both the top and bottom. Trend followers must accept being "late."
- **Whipsaw in ranges.** In a sideways market, price crosses back and forth over the MA, generating repeated false signals and small losses. This is the same cost as the Donchian system, just slower.
- **Drawdowns during entry/exit.** The system exits *after* a decline has begun (price must close below the MA). You never exit at the top — only after the trend has visibly broken.
- **Single-instrument concentration.** Applied to one index, the strategy is exposed to that market's specific behaviour; a diversified basket smooths this.

## Summary

- Long above the 200-day MA (or on a 50/200 golden cross); exit on the opposite signal.
- The MA is a regime classifier, not a predictor.
- Most of the value is in *avoiding* large drawdowns.
- Lags by design; whipsaws in ranges; exits after the top, not at it.
- A patient, low-turnover strategy that rewards discipline over activity.

Next: Strategy 3 — the 52-week high breakout.
