# 7. Alerts

## Let the market come to you

The single most under-used feature on TradingView is the **alert**. An alert watches a condition for you — a price level, an indicator crossing, a drawing being touched — and **notifies you the moment it happens** (on-screen, by email, by push notification, or via webhook). It turns "watching the chart" into "being told when something matters."

## The three kinds of alerts

### 1. Price alerts

The simplest: "tell me when NIFTY reaches 25,000" or "when RELIANCE crosses above ₹3,000". Set it once, and you no longer need to watch the price.

### 2. Indicator alerts

"Tell me when the RSI crosses below 30" or "when the price crosses above the 200-day MA". These attach to *indicators* (Chapter 5) — a way to be notified of *technical conditions*, not just prices.

### 3. Drawing alerts

"Tell me when price touches this trendline" or "breaks above this resistance line". Attach an alert to any **drawing** (Chapter 4), and the drawing becomes a passive monitor.

## The multi-condition alert

Beyond the single condition, TradingView supports **multi-condition alerts**: combine several conditions ("price above the 50-day MA *and* RSI below 40") and alert only when *all* are true. This is how you express an actual *setup* — not just "price reached X", but "my full entry condition is met."

The significance is hard to overstate: **an alert can encode your entire signal**, so that the platform monitors your strategy for you, and notifies you only when the setup is genuinely present.

## How to use alerts well

### 1. Alert on the condition, not the consequence

"Alert when price breaks resistance" is useful; "alert when price is *near* resistance" (a heads-up to get ready) is even more useful for a manual trader. Think about *what you actually need to know*, and alert on that.

### 2. Be specific about the message

An alert's message is customisable — include *why* it fired ("RELIANCE broke ₹3,000 on volume"). A vague alert ("something happened") forces you to open the chart to find out; a specific alert tells you in the notification itself.

### 3. Respect the plan's limits

The **free tier allows one active alert**; paid tiers allow many. If you are on the free tier, that single alert should be your *most important* condition — which is itself a useful discipline: *what is the one thing I most need to be told?*

### 4. Alerts are triggers, not instructions

An alert tells you *a condition is met*; it does not tell you *what to do*. The decision — and the risk rules — are still yours. An alert is the *notice*; your plan is the *response*. (And, as the Risk Management book stresses, the response should be pre-committed, not improvised in the moment.)

## Alerts in the broader workflow

Alerts are what make a *system* out of a *screen-and-chart* habit:

1. **Screener.in** produces the fundamental shortlist (companion book).
2. **Watchlists** (Chapter 6) hold the candidates.
3. **Alerts** watch the *technical* conditions (a breakout, a trendline, an indicator crossing) on each candidate.
4. **You** act — following your pre-committed plan — when an alert fires.

The result: you are *notified* of exactly the right moments, instead of *watching* for them. That is the difference between a tool you use and a tool that works for you.

## Summary

- Three kinds: price, indicator, and drawing alerts.
- Multi-condition alerts can encode an entire setup.
- Alert on what you need to know; make the message specific; respect plan limits.
- Alerts are triggers, not instructions — the plan is still yours.
- Alerts turn a screen-and-chart habit into a system that notifies you.

Next: bar replay — the feature that lets you practise.
