# 5. Indicators and Strategies

## The tools that summarise price

**Indicators** are the calculations overlaid on the chart (moving averages, RSI, MACD, and thousands more). **Strategies** are indicators *plus* defined entry/exit rules that can be backtested. This chapter covers how to use indicators well — and the discipline that keeps them from becoming noise.

## The indicator library

TradingView ships with a **vast library** of built-in indicators, plus thousands more published by the community. Adding one is trivial: open the **Indicators** menu, search (e.g., "RSI", "200 SMA"), and click to apply.

The categories that cover most of what you will use:

- **Trend** — moving averages (SMA/EMA), MACD, ADX, Supertrend.
- **Momentum** — RSI, Stochastic, Rate of Change.
- **Volatility** — Bollinger Bands, ATR, Keltner Channels.
- **Volume** — Volume, On-Balance Volume, VWAP.

Each indicator is a *summary* of price in one dimension — trend, momentum, volatility, or volume. The skill is choosing the one that answers your current question (the Charts book's "choose the lens" discipline applies to indicators too).

## Configuring indicators

Every indicator has **parameters** you can change (e.g., the RSI's length from the default 14 to 2). The discipline is the same as everywhere else in this series:

- **Know why you are changing a parameter.** A 200-day MA has a reason (long-term trend); a 137-day MA was almost certainly mined from the data. Prefer round, meaningful values.
- **Fewer indicators, not more.** The classic beginner error is stacking 10 indicators until the chart is unreadable. The master starts with one or two (a trend filter and a momentum/volatility read) and adds only with a specific question in mind.

## Saving and favouriting

Two habits that pay off:

1. **Favourite the indicators you use** (the star next to each) — they then appear at the top of your list, one click away.
2. **Save a configured indicator as a template** (Chapter 3) — so your exact setup (e.g., "RSI with length 2 + 200 SMA") loads in one click rather than being rebuilt every time.

## Strategies (and their honest caveat)

A **Strategy** is an indicator with entry/exit rules, which TradingView can **backtest** on the chart — showing a simulated equity curve, win rate, and drawdown. It is a *fantastic learning tool* and a *dangerous source of false confidence*:

- **The good:** it forces you to make your idea *explicit* (entry rule, exit rule), and to see it tested — which is the entire discipline of systematic trading.
- **The danger:** a strategy backtest is subject to every pitfall of backtesting — overfitting, ignoring costs, look-ahead, survivorship (all covered in the Quant Trading and Systematic Trading Framework books). The equity curve it shows is almost always *better* than live reality.

The honest rule: **use strategies to *learn* and to *express* an idea — never to believe an equity curve at face value.** The backtest is a hypothesis, not an answer.

## Indicators are summaries, not signals

The most important discipline of all: **an indicator is a *summary of what has happened*, not a *prediction of what will happen*.** RSI above 70 does not "mean" the market will fall; it means the market *has been* strong. An indicator is a *question answered in numbers*, not an *instruction*. The master reads an indicator as *"this is what the trend/momentum/volatility currently is"* — and then makes a decision, rather than delegating the decision to the indicator.

## Summary

- Indicators summarise price in one dimension: trend, momentum, volatility, volume.
- Configure with reason; prefer fewer indicators; favourite and template your setups.
- Strategies backtest an explicit idea — a great learning tool, but subject to all backtesting pitfalls.
- An indicator is a summary, not a signal; it answers a question, it does not give instructions.

Next: watchlists and multi-chart layouts.
