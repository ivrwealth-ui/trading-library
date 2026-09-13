# 3. The Momentum Trader's Toolkit

## The few tools that do the work

Momentum trading does not require a wall of indicators. The five strategies in this book use a small, standard toolkit. Understanding these tools first means each strategy chapter can focus on *how* they are combined rather than *what* they are.

## Trend and momentum indicators

### Moving averages (MA)

A **moving average** is the average closing price over the last N periods, plotted as a smooth line that follows price. The two most common are:

- **Simple moving average (SMA)** — the plain average; slower, smoother.
- **Exponential moving average (EMA)** — weights recent prices more; faster, more responsive.

The two canonical uses:

1. **A trend filter.** Price above a long MA (e.g., the 200-day) = uptrend; below = downtrend. The MA is a *regime switch*, not a precise signal.
2. **A crossover.** When a faster MA crosses above a slower one, momentum is turning up; below, turning down.

Common pairs: 20/50, 50/100, 50/200. Longer pairs trade less often and capture bigger trends; shorter pairs are more responsive but whipsaw more.

### Donchian channels

A **Donchian channel** plots the highest high and lowest low over the last N periods — e.g., the 20-day high and 20-day low. It is the backbone of breakout trading:

- A close **above the 20-day high** is a breakout (new strength).
- A close **below the 20-day low** is a breakdown (new weakness).

Donchian channels answer the simplest possible momentum question: *is price making a new high or a new low over the lookback window?*

### The 52-week high

The **52-week high** is a special, widely-watched level. Because it is the highest price of a full year, it carries psychological weight — and, empirically, stocks near their 52-week high have historically outperformed (the basis of Strategy 3). It is, effectively, a Donchian channel with a one-year window.

### Relative strength (RS)

**Relative strength** compares one asset to another (or to an index): RS = asset return ÷ benchmark return over a window. An asset *outperforming* the index has positive relative strength. This is different from the RSI oscillator — here "relative strength" means *relative performance*, not the Relative Strength Index. Ranking a universe by RS and holding the strongest is the core of Strategy 4.

### Volume

**Volume** is the fuel of a trend. A breakout on *rising* volume is more trustworthy than one on thin volume, because it shows genuine participation. Volume is rarely a standalone signal in momentum trading, but it *confirms* — a breakout without volume is a weaker breakout.

## The concepts that hold it together

Beyond the indicators, three *concepts* are used everywhere:

### Trend structure: higher highs and higher lows

An uptrend is, by definition, a sequence of **higher highs (HH)** and **higher lows (HL)**. A downtrend is lower lows and lower highs. The simplest momentum read is to ask: *is price still making higher highs and higher lows?* When it stops doing so, the trend is weakening — even before any indicator turns.

### Breakout vs. pullback entry

Momentum strategies enter one of two ways:

- **Breakout entry** — buy *as* price makes a new high (aggressive, early, more failed breakouts).
- **Pullback entry** — wait for a *retracement* against the trend and enter as the trend resumes (conservative, later, fewer but better entries).

Strategies 1, 3, and 4 in this book are breakout-style; Strategy 5 is the pullback-style complement.

### The exit: trail or time

Every momentum strategy must define *when to leave*. Two families of exits:

- **Trend-based exit** — exit when the trend filter breaks (e.g., price closes below the 20-day low, or below the 50-day MA). Lets winners run.
- **Time-based exit** — exit after a fixed holding period regardless. Controls risk in strategies (like RS rotation) that rebalance on a schedule.

Most momentum systems combine both: a trend-based stop to cut losers, and a time or rebalance rule to keep the portfolio fresh.

## A mental model before the strategies

Hold these three ideas together and the five strategies become variations on one theme:

1. **Define strength** with a rule (breakout, crossover, new high, relative ranking).
2. **Enter on strength**, not on hunches.
3. **Exit on weakness**, with a rule — never on emotion.

The strategies differ only in *which* rule defines strength and *which* defines weakness.

## Summary

- Moving averages: trend filters and crossovers (20/50, 50/100, 50/200).
- Donchian channels: N-period high/low for breakouts and breakdowns.
- 52-week high: a psychologically and empirically important level.
- Relative strength: performance relative to a benchmark, for ranking.
- Volume confirms; trend structure (HH/HL) is the underlying read.
- Entries are breakout or pullback; exits are trend-based or time-based.

Next: Strategy 1 — the Donchian channel breakout.
