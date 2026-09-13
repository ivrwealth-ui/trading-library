# 6. Strategy 3 — The 52-Week High Breakout

## The year's most watched level

The **52-week high** is the highest price a security has traded at in the past year. It is visible to everyone, carries strong psychological weight, and — empirically — stocks near their 52-week high have historically been *more*, not less, likely to keep rising. This strategy trades that observation directly.

## The idea

Conventional wisdom says "buy low." The 52-week high strategy says the opposite: a stock at a new 52-week high is demonstrating *genuine strength* — demand is overwhelming supply at the highest price anyone has paid in a year. Rather than being "too expensive," such a stock has historically been *strong*, because the forces that pushed it to new highs (earnings, news, institutional accumulation) tend to persist.

The academic foundation is the work of George and Hwang (2004), who showed that a stock's *proximity to its 52-week high* is one of the strongest and most robust momentum signals — in many tests, stronger than the classic trailing-return momentum measure. The 52-week high acts as an *anchor* that investors under-react to.

## The rules

**Universe:** a watchlist of liquid stocks (or the NIFTY 500 constituents), screened for tradability.

**Entry (buy):** when a stock **closes at a new 52-week high**. (A slightly more conservative variant waits for a close *above* the prior 52-week high by a small margin, or requires the high to be accompanied by rising volume.)

**Exit (sell):** any of —
1. **Trend stop:** a close below a trailing level (e.g., the 20-day low, or a fixed 8–10% below the entry).
2. **Moving-average stop:** a close below the 50-day MA.
3. **Time stop:** exit after a fixed holding period (e.g., 3–6 months) if the trend has not continued.

**Position sizing:** a fixed fraction of capital per position, with a hard stop defining the risk.

## Historical context

George and Hwang's "The 52-Week High and Momentum Investing" (2004) established that nearness to the 52-week high predicts future returns about as well as — and in some tests better than — the standard 12-month momentum factor, across US equities. The result has been replicated internationally. The mechanism is behavioural: the 52-week high is a *salient anchor* that investors are slow to update, so a stock breaking through it still has room to run.

Framed honestly: *historically, stocks breaking to new 52-week highs have tended to outperform over the following months — but the effect is a statistical tendency, not a certainty for any individual stock.*

## A worked example (an NSE stock)

- A large-cap stock has traded between ₹800 and ₹1,000 for a year. Its 52-week high is ₹1,000.
- On strong results, the stock **closes at ₹1,030** — a new 52-week high. **Entry** at ₹1,030.
- **Stop** placed at ₹950 (just below the breakout level / prior resistance, ~8% risk).
- Over the next four months the stock trends to ₹1,350 as more investors notice the breakout.
- A pullback follows; the stock **closes below its 50-day MA at ₹1,250**. **Exit** at ₹1,250.

Result: entry ₹1,030 → exit ₹1,250 = **+21%** over four months, with a defined stop that capped the risk if the breakout had failed.

## Risks and limitations

- **Failed breakouts.** Many 52-week highs fail immediately — the stock reverses and falls back. The hard stop is what keeps these failures small.
- **Gap-down risk on the entry.** A stock gapping up to a new high on news can reverse the same day. Buying *into* the gap is riskier than buying a clean close above the level.
- **Concentration.** Single-stock strategies are exposed to idiosyncratic (company-specific) risk; a basket of 8–15 positions, not one bet, is the way the strategy is meant to be run.
- **Market dependence.** Breakouts succeed far more often in a rising market than a falling one; a broad-market filter (e.g., the index above its 200-day MA) improves the odds.

## Summary

- Buy stocks closing at new 52-week highs; exit on a trend or time stop.
- Grounded in George & Hwang (2004): the 52-week high is a strong, robust momentum anchor.
- Many breakouts fail — the stop and diversification are what make the strategy survivable.
- Works best with a basket of positions and a bullish market filter.

Next: Strategy 4 — relative strength rotation.
