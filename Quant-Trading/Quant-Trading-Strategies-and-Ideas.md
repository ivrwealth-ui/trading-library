# Quant Trading: Strategies and Ideas

## Five systematic strategies, the pipeline that turns them into code, and the discipline that keeps them honest — with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading and investing involve substantial risk of loss, including the possible loss of principal. Past performance never guarantees future results, and backtested performance is especially prone to overstatement.
- All strategies, examples, and historical observations are illustrative. A strategy that *backtests* well may still lose money live, for reasons this book explains in detail.
- Data, costs, taxes, and regulatory details change over time. Always verify current rules and consult a qualified adviser before acting.
- Nothing in this book should be read as a promise of return or a guarantee that any strategy will be profitable.

By reading this book, you agree that you are solely responsible for your own trading and investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches **quant trading** — the discipline of expressing trading ideas as *systematic, testable rules*, implemented in code. It presents five strategy ideas and the process that surrounds them.

- **Chapters 1–3** build the foundation: what quant trading is, the pipeline (idea → data → backtest → paper → live), and the evaluation metrics you will use to judge any strategy.
- **Chapters 4–8** are the five strategy ideas — the heart of the book. Each is presented with its logic, its rules (in prose and language-agnostic pseudocode), and its known risks.
- **Chapters 9–10** cover the two things that decide whether a quant strategy actually works: avoiding backtesting pitfalls, and surviving the journey from backtest to live.

A note on language: this book describes what a strategy *is* and what it has *historically* tended to do — never what you "should" do. Where results are discussed, they are framed as historical observations, not promises. You are responsible for your own decisions.

---

## Table of Contents

1. What Is Quant Trading?
2. The Quant Pipeline
3. The Toolkit and Evaluation Metrics
4. Strategy 1 — Cross-Sectional Momentum
5. Strategy 2 — Mean Reversion and Pairs
6. Strategy 3 — Time-Series Trend Following
7. Strategy 4 — Factor Tilts
8. Strategy 5 — Volatility Targeting and Seasonality
9. Backtesting Pitfalls
10. From Backtest to Live

Appendix — Metrics and Strategy Reference

---


# 1. What Is Quant Trading?

## Rules over judgement

**Quant trading** is the practice of turning a trading idea into a *precise, testable set of rules*, and executing those rules *systematically* — by hand against a checklist, or by computer. The defining feature is not the use of computers; it is the **explicitness**: a quant strategy can be written down unambiguously, and therefore *tested* against history before a single rupee is risked.

Where a discretionary trader might say "I like this stock because the story is improving," the quant trader says: "rank the universe by trailing 12-month return, hold the top 10%, rebalance monthly." The difference is not sophistication — it is **falsifiability.** A rule can be backtested; a feeling cannot.

## The spectrum, not a binary

"Quant" and "discretionary" are ends of a spectrum, not two camps:

- **Fully systematic** — every decision (what, when, how much, when to exit) is a rule.
- **Quant-assisted** — a human makes the final call, but with systematic inputs (a screener, a risk model, a backtest).
- **Discretionary** — judgement drives everything.

Most of this book's ideas sit at the systematic end, because that is where the *testability* — the whole point of quant — lives.

## The three promises of quant

Quant trading exists for three reasons, and each is a real advantage:

1. **Testability.** An explicit rule can be backtested. You can learn — *before* risking money — how it would have behaved, how deep its drawdowns were, and whether the edge survives costs. Discretionary judgement cannot be tested this way.
2. **Emotion removal.** A systematic rule is executed the same way whether you are euphoric or terrified. The rule, not the mood, makes the decision (the psychology chapters of this series explain why that matters).
3. **Scale and repeatability.** A systematic process can be run across hundreds of instruments, consistently, day after day — something no human judgement can do.

## The honest caveats

Quant trading is not a shortcut to certainty, for three reasons the book returns to:

1. **Backtests overstate.** A backtest is an *upper bound* on reality, not a forecast. Overfitting, look-ahead bias, survivorship bias, and ignored costs can make a worthless strategy look wonderful (Chapter 9).
2. **The past is not the future.** A rule that worked historically can stop working — markets adapt, and edges decay. This is why quant is a *process* (build, test, monitor, retire), not a one-time discovery.
3. **Quant is not "code magic."** The hardest part is not the programming; it is the *idea* and the *discipline* to test it honestly. The code is just the unambiguous expression of the idea.

## What a quant strategy actually is

Strip away the jargon and every quant strategy is four things:

1. **A universe** — what you trade (NIFTY 500, a basket of ETFs, a list of futures).
2. **A signal** — a rule that says *when and what* to act on (momentum rank, mean-reversion extreme, trend state).
3. **A sizing rule** — *how much* (fixed fraction, volatility targeting — the Risk Management book covers this).
4. **An exit** — *when to leave* (a stop, a rebalance, a time rule).

Everything in this book is a variation on those four knobs. Master the structure, and each strategy is a matter of "which settings."

## Summary

- Quant trading is explicit, testable rules — not necessarily computers.
- It promises testability, emotion removal, and scale.
- It is not a shortcut: backtests overstate, edges decay, and the idea matters more than the code.
- Every strategy = universe + signal + sizing + exit.

Next: the pipeline — the process that turns an idea into a live strategy.


# 2. The Quant Pipeline

## Idea to live, in six stages

Every quant strategy, whether it works or not, travels the same path. Knowing the stages — and *not skipping* them — is most of the discipline. This chapter walks the pipeline.

## Stage 1 — Idea

Everything starts with a *hypothesis about why* a pattern should exist. The best ideas are not "random backtest hits" but **economically motivated** claims:

- *"Investors under-react to news, so recent winners keep winning"* → a momentum idea.
- *"Short-term overshoots revert"* → a mean-reversion idea.
- *"Cheap, high-quality companies outperform over time"* → a factor idea.

The test of a good idea: **can you explain, in a sentence, *why* it should work** — not just *that* it worked in one backtest? An idea with a mechanism survives; an idea with only a backtest is a coin-flip.

## Stage 2 — Hypothesis → rules

Turn the idea into **unambiguous rules**. This is where vague becomes precise:

- *Universe:* which instruments, what liquidity filter.
- *Signal:* the exact condition (e.g., "12-month return, skip the last month, top decile").
- *Sizing:* equal-weight, or risk-based.
- *Rebalance/exit:* the schedule and the stop.

If two people could implement your idea *differently*, the rules are not precise enough.

## Stage 3 — Data

A strategy is only as good as its data. The requirements:

- **Clean** — no survivorship bias (use the *historical* universe, not today's survivors), no look-ahead (no using data not yet available at decision time), no survivorship in delisted names.
- **Aligned** — prices, corporate actions (splits, dividends, bonuses) adjusted correctly; in India, adjustment for splits/bonuses/rights matters enormously.
- **Complete** — enough history to span *different regimes* (a strategy tested only in a bull market has learned nothing about bear markets).

Data quality is where most retail quant efforts quietly fail.

## Stage 4 — Backtest

Run the rules over history and measure the result. But treat the backtest as an **experiment**, not an answer. The goal is to learn:

- *Is there an edge?* (positive expectancy after costs.)
- *How deep are the drawdowns?* (Can I survive them?)
- *Is the edge robust?* (Does it survive small changes to the parameters, or is it fragile?)

Chapter 9 covers the traps that make backtests lie; Chapter 3 covers the metrics that tell you what you are looking at.

## Stage 5 — Paper trading

Run the strategy **live, but without real money** (or with tiny size), for weeks to months. This stage tests the things a backtest cannot:

- *Does the execution match the assumption?* (Slippage, fills, latency.)
- *Do the costs match the estimate?* (Real brokerage, STT, impact.)
- *Does the *process* work?* (Can you run it every day, reliably, without mistakes?)

Paper trading is where the *engineering* gets tested — and it is the cheapest place to find bugs.

## Stage 6 — Live (small, then scale)

Go live **at small size first**, and only scale after the live results *track* the backtest and paper results within reason. Live is where the psychological reality (Chapter 10) and the tail events (Risk Management book) show up.

## The pipeline as discipline

The pipeline's most important property is that **each stage is a gate, not a formality.** A strategy that fails the backtest does not proceed; a strategy whose paper trading diverges from the backtest does not go live; a live strategy that stops tracking its backtest is retired. The stages exist to *kill bad ideas cheaply* — the earlier, the cheaper.

The single most common quant failure is **skipping a stage** — going from idea straight to real money, or trusting a backtest that was never stress-tested. The pipeline is the antidote.

## Summary

- The pipeline: idea → rules → data → backtest → paper → live.
- Ideas need a *mechanism*, not just a backtest.
- Rules must be unambiguous; data must be clean, aligned, and complete.
- Each stage is a gate: kill bad ideas cheaply, early.
- The biggest failure is skipping a stage.

Next: the metrics — how to tell whether a backtest is telling the truth.


# 3. The Toolkit and Evaluation Metrics

## The vocabulary for judging a strategy

A backtest produces a wall of numbers. This chapter explains the metrics that actually matter — and, crucially, *what they can and cannot tell you*.

## Returns and risk

### CAGR (Compound Annual Growth Rate)

The annualised return, smoothing out the compounding. It answers "how fast did the equity grow?" — but it is a *single number* that hides the path.

### Volatility (standard deviation of returns)

How much the returns swing. High volatility means a bumpy ride for the same CAGR. Volatility is *risk* in the quantitative sense.

### Maximum drawdown (Max DD)

The worst peak-to-trough fall. This is the number that matters most emotionally — and practically, because of the recovery asymmetry (a 50% drawdown needs a 100% gain to recover). A strategy is only as good as its worst drawdown, because that is what decides whether you survive to collect the returns.

## Risk-adjusted return

### Sharpe ratio

Sharpe = (Return − risk-free) ÷ volatility.

It measures return *per unit of risk*. A high Sharpe means the return was earned *efficiently* — without excessive volatility. A Sharpe above ~1 is good; above ~2 is excellent (and often too good — a red flag for overfitting, Chapter 9).

### Sortino ratio

Like Sharpe, but only penalises *downside* volatility (the part you actually dislike). It is a fairer measure for strategies with asymmetric returns.

## The trade-level metrics

### Win rate

The fraction of trades that won. **Important:** win rate alone is meaningless — it must be read with the payoff ratio. A 30% win rate with 4:1 winners is excellent; an 80% win rate with 1:4 losers is ruinous.

### Profit factor

Gross profit ÷ gross loss. A profit factor above 1 means the strategy made more than it lost; above ~1.5 is usually considered solid. It is a quick, robust summary of edge.

### Payoff ratio (avg win ÷ avg loss)

How big winners are relative to losers. Combined with win rate, it determines expectancy:

Expectancy = (Win rate × Avg win) − (Loss rate × Avg loss)

A positive expectancy is the *minimum* bar for a strategy — and you should be able to compute it from these two numbers.

## Robustness metrics (the ones that catch lies)

### Number of trades

A backtest with 20 trades proves almost nothing; one with 2,000 is far more credible. **Small samples lie.** Look at the trade count before believing any other metric.

### Parameter sensitivity

Does the edge survive if you change the lookback from 12 months to 10, or 14? A robust edge is *insensitive* to small parameter changes; a fragile one (the signature of overfitting) collapses the moment you nudge anything. Plot performance against parameter — a smooth, flat-topped surface is good; a single sharp spike is a warning.

### Out-of-sample / walk-forward performance

The gold-standard test: fit nothing, or fit on one period and *test on a later, unseen period*. A strategy that only works in-sample is overfit. Real edges persist out-of-sample.

### Regime coverage

Did the strategy make money across *different* market conditions (bull, bear, range) — or only in one? A strategy that only works in a bull market is a bet on the bull market, not a strategy.

## The honest reading order

When you see a backtest, read the numbers in this order:

1. **Trade count** — is the sample big enough to mean anything?
2. **Max drawdown** — could I survive it?
3. **Profit factor / expectancy** — is there actually an edge?
4. **Sharpe/Sortino** — is the edge worth the risk?
5. **Robustness** — does it survive parameter changes and out-of-sample?

Most people read the CAGR first — which is exactly backwards, because CAGR is the number most easily inflated by a lucky, overfit, or costless backtest.

## Summary

- Return metrics (CAGR, vol, max DD) describe the path; max DD is what decides survival.
- Risk-adjusted metrics (Sharpe, Sortino) measure return per unit of risk.
- Trade-level metrics (win rate, payoff, profit factor, expectancy) describe the edge.
- Robustness metrics (trade count, parameter sensitivity, out-of-sample, regime coverage) catch lies.
- Read trade count and drawdown before you read CAGR.

Next: Strategy 1 — cross-sectional momentum.


# 4. Strategy 1 — Cross-Sectional Momentum

## The canonical quant strategy

Cross-sectional momentum is the most replicated strategy in quantitative finance: **rank a universe of assets by their recent returns, hold the strongest, and rebalance on a schedule.** It is the direct implementation of the momentum factor, and it is the natural first strategy for any quant trader because it is simple, well-documented, and testable.

## The idea

The mechanism (from the companion books in this series): investors *under-react* to information, so prices adjust gradually rather than instantly. The result is that assets which have risen recently tend to *keep* rising for a while — and assets which have fallen tend to *keep* falling. Cross-sectional momentum captures this by **always holding the recent winners.**

Crucially, it is *cross-sectional*: it ranks assets *against each other*, so it is always fully invested in *something* — the best of the available options.

## The rules

**Universe:** a liquid stock universe (the NIFTY 500, or a liquid subset), with a liquidity filter (minimum average daily turnover).

**Signal (the ranking):** for each asset, compute its **trailing 12-month total return, skipping the most recent month** (the "12-1" convention — the last month is skipped because it is dominated by short-term *reversal*, which is the opposite of momentum).

**Selection:** rank by this signal and hold the **top decile** (or, practically, the top 10–20 names), equal-weighted.

**Rebalance:** **monthly** (canonical) or quarterly (lower turnover).

**Exit:** an asset is sold when it falls out of the top group at a rebalance. There is no stop — the rebalance *is* the exit.

## Pseudocode

```
universe = liquid_stocks(min_avg_turnover = X)

every month:
    for each stock in universe:
        signal[stock] = total_return(stock, skip=1, window=12_months)

    rank = sort(universe, by=signal, descending)
    holdings = rank[0 : top_N]

    # rotate: sell what dropped out, buy what entered
    sell(previous_holdings not in holdings)
    buy(holdings not in previous_holdings)
    size each holding equal-weight (or 1/top_N of capital)
```

## Historical context

This is the strategy that *defined* the momentum literature — the "buy winners, sell losers" construction documented across markets and decades, including Indian equities. The long-only version (hold winners, hold cash/benchmark rather than shorting losers) retains most of the benefit with far less risk, because it avoids the short side's crash exposure.

Framed honestly: *historically, a diversified portfolio of the strongest 12-1 performers, rebalanced monthly, has tended to outperform the broad market over multi-year horizons — punctuated by sharp reversals in which the prior losers recover fastest.*

## Risks and limitations

- **Momentum crashes.** After a sharp market bottom, prior *losers* snap back hardest, and the portfolio (holding prior winners) lags sharply for a period. This is the known, unavoidable risk.
- **Turnover and costs.** Monthly rotation generates trading; in India, STT, brokerage, and impact costs on frequent churn can consume the edge. A quarterly schedule or a slightly larger top-N reduces this.
- **Concentration and style drift.** Holding 10–20 names is concentrated, and can become heavily tilted to one or two sectors that happened to lead.
- **Parameter fragility.** The exact lookback (12 vs. 9 vs. 6 months) and skip (1 vs. 0 months) shift results; a robust implementation should show an edge across a *range* of these, not a single lucky setting (Chapter 9).

## Summary

- Rank by 12-1 trailing return; hold the top decile / top N; rebalance monthly.
- The canonical momentum strategy, replicated across markets including India.
- Long-only, equal-weighted version retains the edge with less crash risk.
- Risks: momentum crashes, turnover costs, concentration, parameter fragility.

Next: Strategy 2 — mean reversion and pairs trading.


# 5. Strategy 2 — Mean Reversion and Pairs

## Betting that extremes snap back

Mean reversion is the *opposite* of momentum: it bets that **prices that have moved too far, too fast will snap back toward their average.** Where momentum buys strength, mean reversion fades it. This chapter covers the two canonical forms: single-asset mean reversion and **pairs trading**.

## The idea

The mechanism: markets *overshoot*. In the short term, a sharp move is often driven by temporary flows — panic, euphoria, forced selling — that push price beyond where fundamentals or normal behaviour justify. The overshoot then *reverts*.

The essential caveat is that mean reversion is a **short-horizon** phenomenon: it works over days to weeks, and it works *against* the longer-term trend. A stock that is rising in a genuine uptrend is not "overbought"; it is strong. Fading a trend is the classic way to lose money — which is why every serious mean-reversion strategy includes a **trend filter**.

## Single-asset mean reversion

**The rules:**

- **Universe:** liquid stocks (or a liquid index).
- **Trend filter:** only take *longs* when the asset is **above its long-term MA** (e.g., 200-day) — i.e., only buy dips *within an uptrend*.
- **Signal:** a short-term oversold extreme — e.g., the **2-period RSI (RSI-2) closing below 5** (a deeply oversold reading after a sharp drop).
- **Entry:** at the close of the oversold day.
- **Exit:** when price closes back **above the 5-day MA** (or after a fixed few days).
- **Stop:** below the entry day's low, for the times the bounce never comes.

**Pseudocode:**

```
for each stock in liquid_universe:
    if close > sma(close, 200):            # trend filter: only dip-buy in uptrends
        rsi2 = rsi(close, length=2)
        if rsi2 < 5 and no open position:   # deeply short-term oversold
            enter_long(close)
        if in_position and close > sma(close, 5):  # bounce confirmed
            exit_long()
        if in_position and close < entry_day_low:  # failed bounce
            exit_long()   # stop
```

## Pairs trading

Pairs trading is mean reversion applied to **two assets** rather than one: it bets that a *spread* between two related assets will revert, regardless of the market's overall direction.

**The idea:** two highly *correlated* assets (e.g., two large banks, or an index and its constituents) tend to move together. When their spread diverges abnormally far, it tends to come back together. A pairs trader goes long the underperformer and short the outperformer, profiting from the convergence.

**The rules:**

- **Pair selection:** find two fundamentally related, highly correlated assets (e.g., correlation > 0.8 over a long window), ideally co-integrated (a statistical test that their spread is stationary — meaning it *reverts*, not just moves together).
- **Signal:** compute the **spread** = price ratio (or log-ratio) of the two assets. When the spread is more than `k` standard deviations from its own mean, the pair is "stretched."
- **Entry:** long the cheap leg, short the rich leg (market-neutral — the market's direction is largely cancelled).
- **Exit:** when the spread reverts back to its mean (or a stop if it diverges further).

**Pseudocode:**

```
for each candidate pair (A, B) in related_universe:
    spread = log(price_A) - log(price_B)      # or price ratio
    mean, sd = rolling(mean, sd, spread, window)
    z = (spread - mean) / sd

    if z > +2 and no position:   # A rich vs B, expect convergence
        enter(short A, long B)
    if z < -2 and no position:   # A cheap vs B
        enter(long A, short B)
    if z crosses 0:              # converged
        exit()
    if |z| > 4:                 # diverged further (stop)
        exit()
```

## Historical context

Mean reversion is one of the oldest and most documented trading patterns — the short-horizon "reversal" effect is the mirror image of momentum, and both coexist at *different horizons* (reversal at days-to-weeks, momentum at months). Pairs trading has been a staple of statistical-arbitrage desks for decades. The unifying truth: **reversion works at short horizons, *with* the trend, and against temporary overshoots** — not against genuine trends.

## Risks and limitations

- **Catching falling knives.** Without the trend filter, single-asset mean reversion buys every crash and loses badly. **The trend filter is the strategy.**
- **Correlation breakdown.** Pairs that were correlated can *de-correlate* (a merger, a shock, a regime change), and the spread never reverts — the classic pairs-trading loss. Co-integration testing and a divergence stop are the defences.
- **Shorting constraints in India.** Pairs trading requires shorting one leg, which for retail is constrained for stocks (and clean only via index derivatives). This limits the practical universe.
- **Frequent small losses.** Mean reversion has a high win rate but occasional larger losses; costs and strict stops matter.

## Summary

- Mean reversion fades short-term overshoots, against the longer trend.
- Single-asset: RSI-2 < 5 below the 200-day MA, exit above the 5-day MA, stop below entry low.
- Pairs: trade a correlated pair's spread back to its mean, market-neutral.
- Reversion works at short horizons *with* the trend — never against a genuine trend.
- Risks: falling knives, correlation breakdown, shorting constraints, cost.

Next: Strategy 3 — time-series trend following.


# 6. Strategy 3 — Time-Series Trend Following

## An asset's own past, as the signal

Cross-sectional momentum ranks assets *against each other*. **Time-series momentum** (also called *trend following* or *absolute momentum*) asks a different question: **is this asset above its own past?** It holds an asset when it is trending up *relative to its own history*, and steps aside (or goes short) when it is not.

## The idea

The mechanism is the same under-reaction as cross-sectional momentum, applied to an asset's *own* history: an asset that has risen over the past 6–12 months has, historically, tended to keep rising — and an asset that has fallen has tended to keep falling. Time-series momentum formalises this with a single, robust rule: **be long when the asset is above its trend, out when below.**

Its greatest practical virtue is **drawdown avoidance**: it keeps you out of the market (or defensive) during sustained downtrends, which is where most long-term damage happens.

## The rules (the canonical form)

**Universe:** any asset you intend to hold — a broad index (NIFTY), a set of sector indices, or a basket of assets (Indian equities, global equities, gold, bonds).

**Signal:** the asset's price relative to its **200-day (or 10-month) simple moving average**:

- Price **above** the MA → **long**.
- Price **below** the MA → **cash** (or defensive asset).

**Rebalance:** check the signal **monthly** (at month-end). Checking daily adds whipsaw without much benefit.

**Position:** fully in, or fully out. (A multi-asset version applies the same rule to each asset, holding only those above their trend.)

## Pseudocode

```
for each asset in basket:
    state[asset] = "long" if close > sma(close, 200) else "cash"

every month_end:
    for each asset:
        if state[asset] == "long" and not invested(asset):
            buy(asset)
        if state[asset] == "cash" and invested(asset):
            sell(asset)
```

## Historical context

Time-series momentum is among the most documented effects in finance. The "above the 200-day MA = in, below = out" rule — and its equivalents — has been shown, across many markets and long periods, to deliver much of the market's return while materially reducing maximum drawdown. The mechanism is *avoidance* rather than prediction: the rule misses the worst stretches of bear markets, and because losses are asymmetric (a 50% loss needs a 100% gain to recover), avoiding them is worth more than catching every up-move.

Framed honestly: *historically, a simple trend filter has tended to produce equity-comparable long-run returns with smaller drawdowns, at the cost of whipsaw in range-bound markets and late entries/exits at turning points.*

## Risks and limitations

- **Whipsaw in ranges.** In a choppy, sideways market, price crosses the 200-day MA repeatedly, generating a string of small losing round-trips. This is the strategy's known cost, and it is why the monthly (not daily) check matters.
- **Late entries and exits.** The rule acts only *after* the trend has visibly broken, so it always gives up the first leg of recoveries and the last leg of bull markets. The investor must accept being "late."
- **Lag in one-way markets.** In a long, steady bull run, a trend filter occasionally steps out on a dip and misses a leg, underperforming buy-and-hold during that stretch.
- **Single-asset concentration.** Applied to one index, the strategy is fully in or fully out — no diversification of the timing decision. A multi-asset version smooths this.

## Summary

- Long above the 200-day MA, cash below; check monthly.
- Time-series momentum: an asset's own past predicts its own future.
- The value is drawdown avoidance, not prediction.
- Costs: whipsaw in ranges, lateness at turns, lag in one-way markets.
- A multi-asset version diversifies the timing decision.

Next: Strategy 4 — factor tilts.


# 7. Strategy 4 — Factor Tilts

## Owning the characteristics that outperform

Factor investing is a different *kind* of quant strategy: instead of timing or ranking on price alone, it **tilts a portfolio toward the measurable characteristics that have historically been associated with higher returns** — value, quality, size, and momentum. It is the systematic implementation of the classic "what makes a stock good" insights.

## The idea

In modern finance, a **factor** is a measurable characteristic that explains differences in returns across stocks. The four most established equity factors:

- **Value** — cheap stocks (low P/E, P/B, P/CF) have historically outperformed expensive ones.
- **Quality** — profitable, low-debt, high-return-on-capital businesses have outperformed weak ones.
- **Size** — smaller companies have historically earned a premium over larger ones (with caveats).
- **Momentum** — recent winners outperform recent losers (the subject of the last three chapters).

A **factor tilt** is a portfolio that *overweights* stocks scoring high on one or more factors and *underweights* (or avoids) the rest. It is the systematic version of "buy good, cheap, trending companies" — done as a ranking and rebalancing problem.

## The rules (a quality + value + momentum tilt)

**Universe:** a liquid stock universe (the NIFTY 500).

**Scoring:** for each stock, compute a composite score from factor metrics:

- **Value:** inverse P/E, inverse P/B (higher = cheaper).
- **Quality:** ROE, low debt-to-equity, stable margins.
- **Momentum:** trailing 12-1 return.

Standardise each metric (convert to a z-score or percentile rank) so they are comparable, then combine:

Composite score = w₁·Value + w₂·Quality + w₃·Momentum

**Selection:** hold the **top decile (or quintile)** by composite score, equal- or score-weighted.

**Rebalance:** **quarterly or semi-annually** (factor premia are slow-moving; high frequency adds cost, not edge).

## Pseudocode

```
universe = liquid_stocks(min_avg_turnover = X)

every quarter:
    for each stock in universe:
        value_score  = zscore(-1 * pe_ratio) + zscore(-1 * pb_ratio)
        qual_score   = zscore(roe) + zscore(-1 * debt_to_equity)
        mom_score    = zscore(trailing_12m_return, skip=1)

        composite = w1*value_score + w2*qual_score + w3*mom_score

    rank = sort(universe, by=composite, descending)
    holdings = rank[0 : top_N]
    rebalance to holdings, equal-weight
```

## Historical context

Factor premia — value, quality, size, momentum — are among the most extensively documented phenomena in academic finance, replicated across markets and decades. The honest nuance, well established in the literature: **individual factors go through long periods of underperformance** (value, in particular, has had extended dry spells), and **combining factors** (which are often uncorrelated) has historically produced a smoother, more robust premium than any single factor alone.

Framed honestly: *historically, portfolios tilted toward cheap, high-quality, positive-momentum companies have tended to outperform the broad market over long horizons — but any single factor can lag for years, and the premium is compensation for real risk.*

## Risks and limitations

- **Factor droughts.** A factor can underperform for a decade (value in the 2010s). A single-factor tilt requires unusual patience; combining factors reduces this.
- **Data and definition risk.** The result depends heavily on *how* you define value, quality, and momentum, and on the quality of the fundamental data. In India, reliable historical fundamental data (especially point-in-time, restated correctly) is harder to obtain than price data.
- **Turnover vs. persistence.** Factor premia are slow-moving; over-trading (monthly) adds cost without edge. But too-infrequent rebalancing lets the tilt drift.
- **Crowding.** Popular factors (quality, momentum) can become crowded, compressing their premium in certain regimes.

## Summary

- Factor tilts overweight measurable characteristics: value, quality, size, momentum.
- Combine standardised factor scores into a composite; hold the top decile; rebalance quarterly.
- Factors are well-documented but go through long droughts; combining them smooths the ride.
- Risks: factor droughts, data/definition sensitivity, turnover, crowding.

Next: Strategy 5 — volatility targeting and seasonality.


# 8. Strategy 5 — Volatility Targeting and Seasonality

## Two overlay ideas that improve almost anything

The first four strategies are *alpha* ideas — ways to pick what to hold. These last two are *overlay* ideas: they do not pick assets, they **adjust the size or timing** of whatever you already hold. They are valuable precisely because they can be bolted onto any strategy.

## Volatility targeting

**The idea:** risk is not constant — the market's volatility rises and falls. A fixed position size therefore means *variable* risk: you are risking far more in a volatile market than a calm one, without intending to. **Volatility targeting** fixes this by **scaling position size inversely to volatility**, so that the *risk* is constant even as volatility moves.

**The mechanism:** estimate current volatility (e.g., the trailing 20-day standard deviation of returns, or the ATR), set a target volatility, and size accordingly:

Position size = (Target volatility ÷ Realised volatility) × base size

When volatility rises, size shrinks; when it falls, size grows — automatically de-risking in turbulent markets and re-risking in calm ones.

**Why it works:** it stabilises the *risk* of the portfolio, which (as the Risk Management book explains) is what determines survival. Historically, volatility-targeted portfolios have tended to show smoother returns and smaller drawdowns than fixed-size portfolios, for the same underlying holdings.

**Pseudocode:**

```
target_vol = 10% (annualised)
realised_vol = std(daily_returns, window=20) * sqrt(252)

leverage = target_vol / realised_vol        # >1 in calm, <1 in volatile
position_size = base_size * leverage         # capped at some max
```

## Seasonality

**The idea:** markets exhibit **calendar patterns** — returns that are systematically stronger or weaker in specific periods. The best-documented include:

- **Month-end / turn-of-month effects** — returns concentrated around month boundaries.
- **Specific months** — certain months have historically been stronger or weaker in specific markets.
- **The pre-holiday effect** — returns around holidays.
- **Payday / SIP flows** — in India, systematic monthly inflows (SIPs, NPS) create recurring liquidity patterns.

**The mechanism:** seasonality effects are driven by *recurring flows* (payroll/SIP contributions, tax-related selling, window-dressing by funds). They are weak and fragile — far weaker than the factor premia — but they have been repeatedly documented.

**How it is used:** not as a standalone strategy, but as a **tilt** — slightly over-weight positions during historically favourable periods, or adjust entry timing to avoid known weak windows. A seasonality overlay is a *small* adjustment to a real strategy, not a strategy in itself.

## The honest caveat

Both overlays are real but modest, and both carry a specific warning:

- **Volatility targeting** is robust and broadly useful — but it does not create alpha; it stabilises risk. It can *reduce* returns in a strong bull market (because it de-risks as volatility rises) in exchange for smoother drawdowns.
- **Seasonality** is weak and fragile; it is the kind of pattern that looks strong in a backtest and evaporates live, and it is a notorious source of overfitting (Chapter 9). Treat any seasonality result with scepticism unless it survives out-of-sample testing.

Framed honestly: *historically, scaling positions to target a constant volatility has tended to smooth returns and reduce drawdowns, while calendar effects have been weak, recurring, and easy to overstate.*

## Summary

- Volatility targeting scales size inversely to volatility, holding risk constant.
- Seasonality overlays tilt toward historically favourable calendar periods.
- Both are overlays that improve an existing strategy, not standalone alpha.
- Volatility targeting is robust and stabilises risk; seasonality is weak and overfit-prone.

Next: the backtesting pitfalls that make every strategy in this book look better than it is.


# 9. Backtesting Pitfalls

## The ways a backtest lies

Every strategy in this book — indeed, every quant strategy ever written — will look better in a backtest than it performs live. The gap is not random; it is caused by a specific, well-understood set of **biases and errors**. This chapter names them, because the entire point of quant trading is to *test honestly* — and an honest test requires knowing how tests lie.

## The seven deadly pitfalls

### 1. Look-ahead bias

Using information that was **not available at decision time**. Example: ranking on a company's *today's* market capitalisation when backtesting *last year's* decision — but last year the market cap was different.

**The test:** for every data point, ask "did I *actually know* this on the day the trade was made?" If not, the backtest is fantasy. Look-ahead bias is the single most common source of inflated results.

### 2. Survivorship bias

Backtesting on the universe of companies that **exist today**, ignoring those that delisted, went bankrupt, or merged away. The survivors are, by definition, the ones that did well — so the backtest inherits an upward bias.

**The fix:** use a **point-in-time universe** — the actual list of tradeable names *on each historical date*, including the ones that later disappeared.

### 3. Overfitting (curve-fitting)

Tuning the strategy's parameters until it fits the *historical* data perfectly — and therefore fits the *future* not at all. An overfit backtest has a beautiful equity curve and no predictive power.

**The signs:** a Sharpe that is *too* good (a Sharpe of 3+ is suspicious), an edge that appears only for one specific parameter value, and a strategy with no economic rationale.

**The fix:** keep the strategy *simple* (few parameters), demand an economic mechanism (not just a fit), and test **robustness** — does the edge survive if you nudge every parameter? A robust edge is flat-topped; an overfit one is a single sharp spike.

### 4. Ignoring transaction costs

Backtesting on prices alone, forgetting that every trade costs brokerage, STT, stamp duty, and the **bid-ask spread** (which is often the largest cost of all, especially in illiquid names).

**The test:** re-run the backtest *with* realistic costs, including slippage. In India, STT and the spread on churning strategies are frequently enough to turn a "profitable" strategy negative — especially for high-turnover strategies like monthly momentum rotation.

### 5. Ignoring liquidity and capacity

Backtesting as if you could trade any size, in any name, at the last price. In reality, an illiquid small-cap cannot absorb your order without moving the price against you.

**The fix:** impose a **liquidity filter** (minimum average turnover) in the backtest, and estimate *impact* — the price you would actually get, not the printed price.

### 6. Small samples and regime luck

A backtest over a short period — or over a single market regime — proves almost nothing. A strategy tested only in a bull market has learned nothing about bear markets; a strategy with 20 trades is statistically indistinguishable from noise.

**The fix:** demand a **large trade count** and **multi-regime coverage** (bull, bear, and range), and prefer longer histories. If the history is short, treat the result as a hypothesis, not an answer.

### 7. Multiple-testing (data snooping)

Testing hundreds of strategies and reporting the one that happened to work. By pure chance, *some* of hundreds of random strategies will look good — and you have selected exactly those. This is the silent killer of quant credibility.

**The fix:** account for the number of tests. If you tried 100 strategies, expect ~5 to look good by luck alone. The honest question is: **does this one survive out-of-sample testing it was never fit on?**

## The one test that catches most of them: out-of-sample

The single most valuable defence is the **out-of-sample test**: develop the strategy on one period, and *then* — without further tweaking — test it on a later, unseen period. A strategy whose edge persists out-of-sample is worth something; one that collapses out-of-sample was overfit.

Closely related is **walk-forward testing**: repeatedly fit on a rolling window and test on the *next* window, mimicking how you would actually use the strategy.

## The honest mindset

The purpose of a backtest is not to *prove* a strategy works; it is to **try to prove it does not**. A backtest that you have attacked with every pitfall in this chapter — costs added, survivorship removed, look-ahead hunted down, parameters stressed, out-of-sample tested — and that *still* shows an edge, is the only backtest worth trusting.

The default assumption must be: **my backtest is lying.** The work is finding out how.

## Summary

- Seven pitfalls: look-ahead, survivorship, overfitting, ignored costs, ignored liquidity, small samples, multiple-testing.
- Look-ahead and survivorship are the most common and most damaging.
- Ignored costs (STT, spread, impact) frequently erase retail edges.
- Overfitting and data-snooping make backtests look better than reality.
- Out-of-sample / walk-forward testing is the single best defence.
- Treat the backtest as an attempt to *disprove* the strategy, not prove it.

Next: from backtest to live — the gap where even honest strategies go wrong.


# 10. From Backtest to Live

## The gap where honest strategies still fail

An honest, out-of-sample-tested backtest with a real edge can still lose money live — because the live world differs from the backtest in ways that are easy to forget. This chapter covers the gap, and how to cross it.

## The four gaps

### 1. The execution gap

The backtest assumes you trade at the signal price, instantly, with no slippage. Live, you trade at **the market's price**, which is different:

- **Slippage** — the difference between the price you expected and the price you got, especially in fast markets or illiquid names.
- **Latency** — the delay between the signal firing and the order reaching the market.
- **Partial fills** — not getting the full order filled at one price.

**The fix:** pad the backtest with realistic slippage, trade liquid instruments, and measure live execution against the backtest's assumption — if you consistently fill worse than modelled, the edge is smaller than you thought.

### 2. The cost gap

The backtest estimated costs; live, the real costs — brokerage, STT, stamp duty, the spread, and impact — are often larger, and they arrive in places the backtest ignored (a strategy that rebalances at the close, for example, pays the *close-auction* spread).

**The fix:** over-estimate costs in the backtest. If the edge survives *pessimistic* costs, it is robust; if it needs optimistic costs to survive, it is fragile.

### 3. The data gap

The backtest used clean, adjusted, complete data. Live data is **messy**: it arrives late, contains errors, misses corporate actions, and sometimes simply is not there. A strategy that depends on data that is only available *after* the fact is backtesting with look-ahead it does not even know about.

**The fix:** build the live data pipeline *separately* from the backtest data, and reconcile the two — if the live signals differ from the backtest signals on the same day, find out why before trusting either.

### 4. The psychological gap

The backtest is a line on a screen; live is real money, and it *feels* different. A 20% drawdown that was an abstract number in a backtest becomes a crisis live — and the trader responds by abandoning the strategy (usually at the drawdown's bottom).

**The fix:** the Risk Management book's framework — size small, know the drawdown in advance, and pre-commit to staying the course. The strategy's worst drawdown should be *known and accepted* before going live, not discovered at the bottom.

## The live protocol

A disciplined path from backtest to live:

1. **Paper trade first.** Run the strategy live, in real time, with no (or tiny) money, for weeks to months. This is where execution, cost, and data gaps surface — cheaply.
2. **Go live small.** Even after paper trading, start at a fraction of intended size. Live reveals what paper could not.
3. **Reconcile live vs. backtest.** Track the live performance against what the backtest *predicted* for the same period. A persistent gap means a modelling error, not bad luck.
4. **Monitor for decay.** Edges decay. Watch for the point where the strategy's live behaviour stops matching its historical behaviour — and be willing to retire it.
5. **Retire gracefully.** The hardest decision in quant is retiring a strategy that *used to* work. Pre-commit to the conditions (a drawdown threshold, a tracking-error threshold, a regime change) under which you stop.

## The honest bottom line

Quant trading is a *process*, not a product. The strategy is the least important part of it; the discipline — test honestly, paper trade, go live small, reconcile, monitor, retire — is what determines whether any strategy, from this book or anywhere, actually makes money. The trader who masters the process can turn a modest edge into years of compounding; the one who skips the process will lose money even with a good strategy.

## Summary

- Four gaps: execution, cost, data, and psychology.
- Paper trade before live; go live small; reconcile against the backtest.
- Costs are usually larger live than modelled — over-estimate them.
- Edges decay; pre-commit to retirement conditions.
- The process matters more than the strategy.

This completes the main text. The appendix collects the metrics and strategies into a reference table.


# Appendix — Metrics and Strategy Reference

## The metrics that matter

| Metric | Formula / meaning | What it tells you |
|--------|-------------------|-------------------|
| CAGR | Annualised compound return | Growth rate (single number) |
| Max drawdown | Worst peak-to-trough fall | The risk that decides survival |
| Volatility | Std dev of returns | The bumpiness of the ride |
| Sharpe | (Return − risk-free) ÷ vol | Return per unit of risk |
| Sortino | Downside-only Sharpe | Return per unit of *bad* risk |
| Win rate | Wins ÷ total trades | Meaningless without payoff |
| Profit factor | Gross profit ÷ gross loss | Robust edge summary |
| Expectancy | (Win% × AvgWin) − (Loss% × AvgLoss) | The minimum bar |

## The five strategies at a glance

| # | Strategy | Signal | Position / exit |
|---|----------|--------|-----------------|
| 1 | Cross-sectional momentum | Rank by 12-1 return | Hold top decile; rebalance monthly |
| 2 | Mean reversion / pairs | RSI-2 oversold in uptrend; or pair spread z-score | Bounce / convergence; stop on failure |
| 3 | Time-series trend | Price vs. 200-day MA | Long above, cash below; check monthly |
| 4 | Factor tilts | Composite of value/quality/momentum z-scores | Hold top decile; rebalance quarterly |
| 5 | Vol targeting / seasonality | Scale to target vol; calendar tilt | Overlays on an existing strategy |

## The universal rules

- Every strategy = **universe + signal + sizing + exit**.
- An idea needs a **mechanism**, not just a backtest.
- **Test to disprove**: add costs, remove survivorship, hunt look-ahead, stress parameters.
- **Out-of-sample** is the single best test.
- **Paper trade → live small → reconcile → monitor → retire.** The process is the edge.
