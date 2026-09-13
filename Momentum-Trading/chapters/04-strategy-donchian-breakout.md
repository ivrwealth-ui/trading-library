# 4. Strategy 1 — The Donchian Channel Breakout

## The classic "trend is your friend" system

The Donchian channel breakout is the archetypal momentum strategy, made famous by the "Turtle" traders trained by Richard Dennis and William Eckhardt in the 1980s. Its genius is its brutal simplicity: **buy when price makes a new high, exit when it makes a new low.** No forecasting, no opinion — only rules.

## The idea

The strategy bets that a market breaking to a new high has begun a trend that will continue. It *wants* to miss the early, uncertain part of a move and catch the confirmed middle. Its famous motto: *"you cannot know how high a market will go, but you can know it is going."*

Because most breakouts fail (and quickly), the system relies on the asymmetry of trend-following: **many small losses, a few very large winners.** The large winners more than pay for the small losses — *if* the trader cuts the losers fast and lets the winners run.

## The rules

**Universe and timeframe:** liquid instruments — NIFTY/BankNIFTY (via index funds/ETFs or futures) or large, liquid NSE stocks. Daily timeframe.

**Entry (buy):** when price **closes above the 20-day high** (the highest high of the prior 20 days).

**Exit (sell):** when price **closes below the 10-day low** (the lowest low of the prior 10 days).

**Position sizing (the Turtle way):** size each position so that a fixed fraction of capital (e.g., 1%) is at risk if the exit triggers. This equalises risk across trades.

**Filters (optional, from later refinements):**
- A longer-term trend filter: only take *long* breakouts when price is above the 200-day MA (trade with the bigger trend).
- Minimum volume on the breakout day (confirmation).

## Historical context

The Turtle experiment is one of the most famous demonstrations that a simple rules-based momentum system, executed with discipline, can produce exceptional returns across many markets. The core insight it popularised — *enter on new highs, exit on new lows, and size positions for risk* — remains the foundation of systematic trend-following. As always, historical results describe what happened; they are not a promise of what will happen next.

## A worked example (NIFTY)

Suppose NIFTY is range-bound between 24,000 and 24,500 for several weeks. Then it breaks out:

- Day 1: NIFTY **closes at 24,550**, above its 20-day high of 24,520. **Entry** at 24,550.
- The 10-day low at entry is 24,300. **Initial stop** at 24,300 (exit if price closes below it).
- NIFTY trends to 25,800 over six weeks, then pulls back. The trailing 10-day low ratchets up with the trend, eventually reaching 25,200.
- NIFTY closes at 25,180 — **below the 10-day low of 25,200**. **Exit** at 25,180.

Result: entry 24,550 → exit 25,180 = **+630 points**, captured with a mechanical rule and a trailing stop that protected the open profit.

The mirror case is equally instructive: if NIFTY had reversed immediately after the breakout and closed below 24,300, the trader exits for a small, defined loss. That is the trade-off — and it is the whole point.

## Risks and limitations

- **Whipsaw in ranges.** In a sideways market, breakouts repeatedly trigger and fail, producing a string of small losses. This is *the* cost of the strategy, and it is why the 200-day filter and disciplined sizing matter.
- **Gap risk.** An overnight gap can jump past the exit level, making the actual loss larger than planned. Stops are not guarantees.
- **Late entries.** Buying a 20-day high means entering *after* a chunk of the move. The strategy gives up the first leg to gain confirmation.
- **Patience required.** Long periods of small losses are psychologically hard, and many traders abandon the system exactly before the big winner arrives.

## Summary

- Buy a close above the 20-day high; exit on a close below the 10-day low.
- Size positions to risk a fixed fraction of capital.
- Many small losses, a few large winners — the trend-following asymmetry.
- Suffers in choppy markets; thrives in sustained trends.
- Rules and discipline, not prediction, are the edge.

Next: Strategy 2 — moving-average trend following.
