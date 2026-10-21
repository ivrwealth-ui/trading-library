# Event & Earnings Trading on the NSE

## The Results Calendar, IV Crush, Gap Rules — and When Not to Play

---

**Published by StratLab**

---

**A practical reference for trading scheduled catalysts in the Indian market.**

---

> **Disclaimer.** This book is for **education only**. It is not investment advice, not a recommendation to buy or sell any security, and the author is not a SEBI-registered investment adviser. Trading around events and earnings involves substantial risk — gaps, slippage, and volatility can produce losses far beyond expectations. Historical "gap fill" and volatility patterns are tendencies, not guarantees. Filing deadlines, circuit limits and exchange rules change: confirm current rules with SEBI and the NSE/BSE.

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading involves substantial risk of loss and is not suitable for everyone. You can lose part or all of your trading capital.
- All examples, figures, and historical observations are illustrative. Historical performance never guarantees future results. Strategies described here have worked *historically* in certain conditions; that does not mean they will work in the future or in your specific situation.
- Margin, taxes (STT, stamp duty), brokerage, and other regulatory details change over time. Always verify current rules and costs before trading.
- Nothing in this book should be read as a promise of profit or a guarantee that any strategy will be profitable.

By reading this book, you agree that you are solely responsible for your own trading decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## Table of Contents

1. What Event Trading Is
2. The Earnings Calendar
3. Other Scheduled Events
4. Implied Volatility and the Crush
5. Trading the Crush
6. What a Gap Is
7. Gap Rules and Tendencies
8. The Don't-Play List
9. The Decision Framework

Glossary

---


# 1. What Event Trading Is

*Part I — Events and the Calendar*

Most of the time, a stock's price moves on a mix of flows, sentiment and slow fundamentals. But around **scheduled events** — an earnings release, a budget, a policy decision, an index rebalance — the market is forced to *reprice* the stock all at once. Event trading is the discipline of positioning (or deliberately *not* positioning) around those repricing moments.

## The two faces of an event

- **The known date, unknown outcome.** The event is on the calendar, so everyone knows *when* it happens — but not *what* it will say. Uncertainty about the *outcome* is what inflates the option premiums ahead of it.
- **The priced vs the surprise.** The market does not react to the number; it reacts to the number *relative to expectations*. A "great" result can still fall if it was already priced in; a "bad" one can rally if it beats a low bar. The edge in event trading is almost never the headline — it is the *gap between the outcome and the expectation*.

## The core idea

Scheduled events are **the one time the market telegraphs its uncertainty in advance** — in the form of elevated implied volatility and wider bid-ask spreads. The entire art of event trading is deciding, before the event, whether that elevated uncertainty is an opportunity (to sell it, to buy it cheaply) or a trap (to be avoided).


# 2. The Earnings Calendar

Earnings (quarterly results) are the most frequent and most tradeable events on the NSE.

## How the Indian results season works

- **The rhythm.** Indian companies report on a financial year ending March. The results seasons are roughly: **Apr–May** (Q4 and full-year), **Jul–Aug** (Q1), **Oct–Nov** (Q2), and **Jan–Feb** (Q3). Each season runs about six to eight weeks, with a heavy concentration of large-caps first, then the mid- and small-caps.
- **The filing deadline.** Under SEBI's Listing Obligations and Disclosure Requirements (LODR), companies must publish their **quarterly results within 45 days of the quarter-end** (60 days for the fourth-quarter / annual audited results). This deadline is what compresses the season and creates the "results rush."
- **Advance intimation.** Listed companies must give **prior notice** of the board meeting where results will be approved. This means the *date* of most results is known days in advance — you can build a calendar.

## Building your results calendar

1. **Watch the exchange announcements.** NSE and BSE publish board-meeting intimations; these are the primary source of the calendar. (NSE: https://www.nseindia.com; BSE: https://www.bseindia.com.)
2. **Use an aggregator.** Screener and market-data platforms maintain results calendars:
   - **Screener.in** — company financials and results history: https://www.screener.in
   - **Moneycontrol** — results calendar and dates: https://www.moneycontrol.com
   - **Trendlyne** — results calendar and estimate trackers: https://trendlyne.com
3. **Note the time.** Results are typically released **after market close or during market hours**. India has no results-related trading halt, so results released intraday reprice the stock the instant the numbers reach the exchange (within its price band, if it has one). Know the convention for the specific stock.

## What the market actually cares about

The headline profit is not the whole story. Around an Indian earnings print, the market re-prices the stock on:

- **Revenue / profit vs expectations** — the top-line and bottom-line *surprise*.
- **Margins** (gross/operating) — the quality of the beat or miss.
- **Management commentary and guidance** — often moves the stock more than the numbers themselves.
- **Segment and one-off details** — the composition of the number (e.g., a tax write-back inflating profit).

**How to read:** always compare the result to the *consensus or prior trend*, not to the absolute. A company growing 15% when the market expected 20% is a *miss*; one growing 5% against a 2% expectation is a *beat*. The expectation, not the number, is the trade.


# 3. Other Scheduled Events

Earnings are only one kind of catalyst. The Indian calendar has several recurring, market-moving events:

| Event | What it is | Typical frequency | Impact |
|---|---|---|---|
| **RBI Monetary Policy** | Repo rate and stance decision | ~bi-monthly | Broad market, rate-sensitives (banks, NBFCs, autos, realty) |
| **Union Budget** | Fiscal policy, taxes, sector allocations | Annual (Feb) | Broad; sector-specific winners/losers |
| **Index rebalancing** | Nifty/other index constituent changes (semi-annual) | Twice yearly | Heavy flows into/out of the affected names |
| **Corporate actions** | Dividends, bonuses, splits, buybacks, rights | Ongoing | Price adjustments and ex-date effects |
| **M&A / deals** | Acquisitions, mergers, demergers | Ongoing | Large, stock-specific repricing |
| **Regulatory decisions** | SEBI rules, court rulings, sector policy | Ongoing | Sector-specific |

## How to think about them

- **Macro events (budget, RBI)** are *index-level* catalysts: they move everything and are usually approached via index options or broad positioning, not single-stock bets.
- **Stock-specific events (earnings, M&A, actions)** are where single-name event trades live.
- **Index rebalancing** is a *known, dated, mechanical* flow: funds tracking an index must buy the entrants and sell the deletions at the effective date. The market often positions days ahead, so the "obvious" trade is frequently already priced.


# 4. Implied Volatility and the Crush

*Part II — IV Crush*

## What implied volatility is

**Implied volatility (IV)** is the market's expectation of future price movement, *priced into an option's premium*. It is not realised volatility (what actually happens); it is what the option market is *charging* for the risk of what might happen. When an event is approaching, IV rises — the options get more expensive because the market knows a repricing is coming.

## The crush

After the event, the uncertainty resolves. The result — whatever it is — is now known, and the *reason for the elevated premium is gone*. **Implied volatility collapses, and option premiums fall even if the underlying price barely moves.** This is the **IV crush**.

**The core asymmetry:**

- A trader who **buys** a straddle before earnings is *long vega*: they paid an inflated premium, and after the event they lose the crush on *both* legs. The stock must move *more* than the inflated premium implied, or the trade loses even if the stock moves.
- A trader who **sells** premium before earnings is *short vega*: they collect the inflated premium, and after the event they *profit from the crush* — but they carry the risk of a huge move against them.

## Why the crush matters more than the direction

The most common and painful error in event trading is buying a straddle "because earnings is coming and it will move", and then losing on a *correct directional call* — the stock moved, but not *enough* to overcome the premium that the crush then destroyed. Before any event trade, you must ask: **"How much does the market already expect this to move?"** The premium tells you. If the market has already priced in a 6% move and you think the stock moves 4%, you are on the wrong side of the crush whether you realise it or not.

## How to read IV around events

- **IV rises into the event** (the run-up) and **collapses after** (the crush). The shape is the classic "IV ramp."
- The **expected move** is encoded in the at-the-money straddle price: `ATM straddle price ÷ underlying` approximates the market's implied move. As a rule of thumb, the straddle is about 0.8× the one-standard-deviation (1σ) move, so 1σ ≈ 1.25 × the straddle. Compare that to your own estimate of the likely move.
- **Compare IV to its own history** (IV rank/percentile): an event with IV already at a multi-year high is a different proposition from one with IV near its lows.


# 5. Trading the Crush

## The two sides, and their trade-offs

**Selling premium (short vega):**

- **Pros:** you collect inflated premium; the crush works for you; time decay works for you.
- **Cons:** a genuine surprise (a 10% gap on a stock priced for 4%) can hurt far more than the premium collected. This is undefined or wide-defined risk.
- **Suits:** range-bound expectations and high IV, using only a defined-risk structure — an iron condor (see *Options Trading Adjustments*), sized small. A short strangle is undefined risk and does not belong here. *Options Trading Adjustments* cautions against holding short premium through a known event; selling the crush is the deliberate exception — it knowingly accepts the gap risk in exchange for the crush, which is exactly why the risk must be defined and the size small.

**Buying premium (long vega):**

- **Pros:** defined risk; a big surprise pays disproportionately.
- **Cons:** you are fighting the crush — you must be *right about magnitude*, not just direction.
- **Suits:** a specific, under-priced catalyst where you expect a move *larger* than the implied move.

## The decision that makes or breaks an event trade

> **Only buy premium when your expected move is *larger* than the implied move; only sell premium when the implied move is *larger* than you believe the move will be.**

This single comparison — **your move estimate vs the market's implied move** — is the entire edge in IV trading. If you have no view on the *size* of the move, you have no event trade; the premium is already efficiently priced.

## Practical notes for the NSE

- **Weekly-expiry options concentrate the crush** into a short window: the event premium is largest in the near-dated options and collapses hardest. Since SEBI's November 2024 rules each exchange has only one weekly index expiry — currently Nifty on the NSE (Tuesday, moved from Thursday in September 2025) and Sensex on the BSE (Thursday); Bank Nifty and the other indices are monthly only, as are all single-stock options. Check the current weekly-expiry convention before trading weeklies (it has been revised by SEBI/NSE).
- **Liquidity thins into events** in the far strikes; the bid-ask spread can be wider than the edge you are chasing. Always price the *spread*, not the mid.
- **Index events (budget, RBI)** are often better approached with **index** options (deep and liquid) than with a basket of thin single-stock options.


# 6. What a Gap Is

*Part III — Gap Rules*

A **gap** is a discontinuity in price — the market opens (or trades) at a level away from the prior close, leaving a "hole" on the chart with no trades in between. Gaps are the physical signature of an event: the overnight (or sudden intraday) repricing that could not happen continuously.

## The four types of gap

1. **Common gap** — small, inside a range, no news behind it; tends to fill quickly and mean little.
2. **Breakaway gap** — breaks a level on high volume, starting a new move; often the *beginning* of a trend.
3. **Runaway (continuation) gap** — occurs mid-trend, confirming momentum; often *not* filled until much later, if at all.
4. **Exhaustion gap** — a final, often wide gap near the end of a move; frequently *reversed* (filled) soon after.

**How to read:** the *type* of gap matters more than the gap itself. A breakaway gap is a signal to *join*; an exhaustion gap is a signal to be wary; a common gap is noise.

## Earnings gaps vs ordinary gaps

Earnings gaps are special: they are driven by **fundamental news**, not just flow. A stock that gaps up 8% on a genuine earnings beat has been *re-valued*, not just re-flowed. This has two consequences:

- Earnings gaps are **less likely to "fill" quickly** — there is a fundamental reason for the new price.
- But a gap that reflects a **misread** (the market initially overreacts, then corrects) can reverse hard in the following days.


# 7. Gap Rules and Tendencies

These are **tendencies, not laws** — they describe what has historically happened more often than not, and they fail regularly. Use them as context, not as a system.

## The "gap fill" tendency

The most widely known gap rule: *many gaps get filled* — price returns to the pre-gap level at some point. This is strongest for **common gaps** and for **morning gaps** in liquid index futures that lack a fundamental driver.

**How to read the fill tendency:**

- **Common/emotion gaps** fill more often than **fundamental (earnings) gaps**.
- A gap **filled on low volume** is a weaker fill than one filled on high volume (which shows conviction behind the return to the old level).
- **Do not trade "gap fill" blindly.** A breakaway gap on a real catalyst is exactly the gap that *does not* fill — chasing a fill there means fighting the new trend.

## The continuation tendency

Gaps in the **direction of the prevailing trend and catalyst** tend to **continue** rather than fill — a bullish breakaway gap in an uptrend is more likely to be followed by further upside than by a fill.

## The half-gap / retracement rule

A practical middle-ground used by many traders: the **gap's midpoint** (or a 50% retracement into the gap) is a level to watch. If a gap is going to fill, it often stalls or finds reaction around its midpoint first; if that midpoint holds as support/resistance, the gap may be a continuation, not a fill.

## Gaps and circuits in India

- **Circuit limits** (price bands) apply to NSE stocks that are not in the F&O segment — 2%, 5%, 10% or 20% either way, depending on the stock. **Stocks with F&O contracts have no fixed circuit**, but they do have a dynamic price band (an operating range, initially 10%) that the exchange flexes as the price approaches it. A stock that opens at its circuit has "gapped" to its limit and may be frozen there if one-sided orders persist.
- **F&O stocks** therefore have no fixed cap on an event gap, so their gaps can be larger. Index constituents that are *not* in the F&O segment still carry ordinary price bands.
- **Know the circuit** for the specific stock before an event — it changes how much a gap *can* happen and how (or whether) you can exit.

## A gap checklist

- **Classify the gap** (common / breakaway / runaway / exhaustion) before acting.
- **Is there a fundamental driver?** Earnings and deals gap *and revalue*; flow gaps *and revert*.
- **Where is the gap in the trend?** Early-breakaway gaps continue; late-exhaustion gaps reverse.
- **What did volume do?** High volume supports continuation; low volume supports fill.
- **Where is the midpoint?** It is the first level to watch for reaction.


# 8. The Don't-Play List

*Part IV — When NOT to Play*

The most profitable "trade" in event trading is often the one you **do not take**. Events are seductive precisely because they *feel* like certain opportunities, and the biggest losses come from positions taken for excitement rather than edge.

## When to stand down

- **No edge on the move size.** If you cannot articulate whether the market's implied move is too high or too low *relative to your own estimate*, you have no edge. The premium is already efficiently priced; sitting out is correct.
- **Thin liquidity / wide spreads.** In the run-up to an event, far-strike options and small stocks develop wide bid-ask spreads. If the spread is wider than your expected edge, the house (the market maker) takes your edge before you can.
- **Binary, unhedgeable outcomes.** Court rulings, regulatory approvals, and M&A verdicts are *binary* — the stock either doubles or halves, with no in-between. These are not trades; they are coin flips with a vig. Avoid unless the payoff is genuinely asymmetric and you can size it as a lottery ticket you can afford to lose.
- **Oversized risk for the thesis.** A short-volatility position sized so that a normal surprise wipes out ten times the premium collected is not a strategy; it is a gamble. If you cannot survive the *worst plausible* gap, the position is too big.
- **Unclear or changing rules.** If you do not know the exact results time, the circuit limit, the expiry convention, or the margin requirement for the instrument, you do not know the trade. Confirm the mechanics first, or pass.
- **Emotional momentum.** "It always moves on results" or "I feel it will gap" is not a reason. If the trade is motivated by excitement rather than a measured move-size opinion, do not take it.
- **Trading the number you cannot predict.** The headline P&L is largely unpredictable and already gamed by expectations. If your "edge" is guessing whether the profit is slightly above or below consensus, you are playing a coin flip.

## The opportunity cost rule

Every event trade consumes **capital, margin and attention**. Ask: *is this the best use of all three right now?* If a boring, high-conviction setup in a liquid instrument is available, it is usually the better trade than a speculative event bet. Event trading should be the *exception*, sized small, and only when the edge is explicit.


# 9. The Decision Framework

For any event you are considering, run this checklist **before** the position:

1. **What is the event, and when exactly does it hit?** (Date, time, and the mechanics — circuit or price band, expiry.)
2. **What is the market's implied move?** Read it from the ATM straddle or the IV. Write it down.
3. **What is *my* expected move, and why?** If you cannot state a number and a reason, stop — there is no trade.
4. **Which side of the crush am I on?** Selling (short vega) or buying (long vega)? Is that consistent with my move estimate?
5. **What is the worst plausible outcome?** Can the position survive it? If not, size down or pass.
6. **Is the instrument liquid, and do I know its rules?** Spreads, circuit, expiry, margin — all confirmed?
7. **Is this the best use of my capital right now?** If not, pass.

## The one-page summary

- **Know the calendar:** results (45-day LODR deadline; 60 days for Q4), RBI policy, budget, rebalances.
- **Compare moves:** your expected move vs the market's implied move — this is the whole edge.
- **Respect the crush:** buyers of premium must beat it; sellers must survive the surprise.
- **Read the gap type:** breakaway continues, exhaustion reverses, common fills.
- **Stand down when:** no move-size edge, thin liquidity, binary outcomes, oversized risk, unclear rules, or emotional momentum.


# Glossary

**Breakaway gap** — a gap that breaks a level on volume and starts a new move.

**Circuit limit** — the maximum price band a stock may trade within a day (F&O stocks have no fixed circuit, only a dynamic price band that the exchange flexes).

**Common gap** — a small gap inside a range with no news driver; tends to fill.

**Expected move** — the market's implied size of a move, encoded in the ATM straddle price.

**Exhaustion gap** — a wide gap near the end of a move, often reversed.

**Gap** — a price discontinuity with no trades in between.

**Gap fill** — price returning to the pre-gap level.

**Implied volatility (IV)** — the market's forward volatility expectation priced into options.

**IV crush** — the collapse in implied volatility (and option premium) after an event resolves.

**IV rank / percentile** — where current IV sits relative to its own history.

**Long / short vega** — profiting from a rise / fall in implied volatility.

**Results season** — the concentrated period when most companies report quarterly results.

**Runaway (continuation) gap** — a gap mid-trend confirming momentum.

**Vega** — an option's sensitivity to changes in implied volatility.
