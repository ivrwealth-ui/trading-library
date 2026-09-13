# 7. Strategy 4 — RSI-2 Mean Reversion

## Fading the short-term extreme

The first three strategies were *continuation* — they buy strength and follow the trend. This chapter switches to the second engine of swing trading: **mean reversion**. The RSI-2 strategy buys when a stock is *short-term oversold* and expects a snap-back. It is the most famous documented short-term mean-reversion system.

## The idea

Markets overshoot. In the short run, a sharp sell-off often pushes a stock *too far, too fast* — and prices tend to **snap back** toward the average, even if the longer-term trend is down. The RSI-2 strategy captures these bounces.

The key instrument is the **2-period RSI (RSI-2)** — an *extremely* short-term oscillator that flips to deeply oversold (near 0) very quickly on a sharp drop. The strategy, documented by Larry Connors and Cesar Alvarez in their book *Short Term Trading Strategies That Work*, buys those deeply oversold moments and exits a few days later on the bounce.

## The rules

**Universe and timeframe:** liquid stocks (or liquid index instruments). Daily timeframe.

**Step 1 — The long-term trend filter (critical).** Only trade in the direction of the longer trend. The classic version: take **longs only when the stock is above its 200-day MA** (an uptrend). In a downtrend, the same setup is used for shorts (or the trade is simply skipped). This filter is *why the strategy works* — buying oversold bounces in an uptrend is high-probability; buying them in a downtrend is catching falling knives.

**Step 2 — The trigger.** Enter a **long when RSI-2 closes below 5** (some use below 10), signalling a deeply oversold short-term extreme.

**Step 3 — Exit.** Exit when price **closes above the 5-day MA** (the classic rule), or after a fixed number of days (e.g., 2–5), or at a fixed small profit target. The trade is a *short* bounce, held only days.

**Step 4 — Stop.** A stop below the entry day's low (or a fixed small percentage), for the times the bounce does not come.

**Position sizing:** standard small risk per trade; the strategy trades frequently, so costs matter.

## Historical context

Connors and Alvarez published extensive historical results for RSI-2 mean reversion across US equities, showing that a simple "buy RSI-2 < 5, exit above the 5-day MA" rule — *crucially, filtered by the 200-day trend* — produced a high win rate over many years. The mechanism is well understood: short-term liquidity-driven overshoots revert, and the trend filter keeps the trader from fighting a genuine downtrend. The pattern generalises: *short-term extremes tend to revert, especially with the longer-term trend.*

Framed honestly: *historically, buying deeply short-term-oversold conditions in assets above their long-term trend has tended to produce frequent small wins — with occasional larger losses when the "bounce" turns out to be a breakdown, which the stop is there to cap.*

## A worked example (a liquid NSE stock)

- A large-cap stock is in an uptrend, trading **above its 200-day MA** at ₹800.
- Over three days it **drops sharply to ₹740** on broad market weakness. Its **RSI-2 closes at 3** — deeply oversold. **Entry** at ₹742.
- The 200-day MA is still well below — the longer trend is intact; this is a dip, not a reversal.
- Over the next three days the stock **bounces and closes above its 5-day MA at ₹775**. **Exit** at ₹775.

Result: entry ₹742 → exit ₹775 = **+4.4% in a few days**, a short, high-probability bounce captured with a defined stop and a mechanical exit.

## Risks and limitations

- **Catching falling knives.** Without the 200-day filter, this strategy buys every crash and loses badly. **The trend filter is not optional — it is the strategy.**
- **Frequent small losses.** Bounces sometimes fail; the stop caps each loss, but the strategy can string together several small losers. It relies on a high win rate *with the filter* to stay net positive.
- **Transaction costs.** RSI-2 trades frequently (often holding only days), so brokerage and STT on each round trip matter more than for slower strategies. Run it on liquid names.
- **False confidence in high win rates.** A high win rate can hide a few larger losses; risk per trade must remain small and disciplined.

## Summary

- Buy RSI-2 closes below 5 (or 10), exit above the 5-day MA — held only days.
- The 200-day trend filter is what makes it work; without it, you are catching knives.
- Documented by Connors & Alvarez; short-term extremes revert.
- High win rate, frequent small trades — costs and stop discipline matter.

Next: Strategy 5 — the range fade.
