# 10. Screener 8 — Multi-Timeframe (Weekly Trend + Daily Trigger)

## The strategy

**Multi-timeframe analysis** holds that signals are stronger when **two timeframes agree**. The classic construction: the **weekly** timeframe defines the *trend* (are we in an uptrend?), and the **daily** timeframe provides the *trigger* (is the daily structure also aligned?). A stock is most attractive when *both* point the same way.

This screener encodes that: a **weekly uptrend** (price above the 30-week MA) combined with a **daily uptrend** (price above the 50-day MA, with the 50-day above the 200-day) and a **daily trigger** (a fresh up-close).

## The logic

- **Weekly trend** — the weekly close is above the 30-week (30-bar weekly) MA. Pulled via `request.security(syminfo.tickerid, "W", ...)`.
- **Daily trend** — price above the 50-day MA, and the 50-day above the 200-day.
- **Daily trigger** — the daily close is above the 50-day MA *and* is a fresh up-close today (`close > close[1]`), suggesting momentum is turning up *now*.

The signal fires when all three align — the higher timeframe agrees, and the lower timeframe is confirming.

## The code

```pine
//@version=6
indicator("Multi-Timeframe (Weekly Trend + Daily Trigger)", overlay = false)

// ---- Weekly (higher timeframe) trend ----
float weeklyClose = request.security(syminfo.tickerid, "W", close, ignore_invalid_symbol = true)
float weeklySma30 = request.security(syminfo.tickerid, "W", ta.sma(close, 30), ignore_invalid_symbol = true)

bool weeklyUptrend = not na(weeklyClose) and not na(weeklySma30) and weeklyClose > weeklySma30

// ---- Daily (lower timeframe) trend + trigger ----
float dailySma50  = ta.sma(close, 50)
float dailySma200 = ta.sma(close, 200)

bool dailyUptrend = close > dailySma50 and dailySma50 > dailySma200
bool dailyTrigger = close > dailySma50 and close > close[1]

// ---- Screen condition ----
bool cond = weeklyUptrend and dailyUptrend and dailyTrigger

// ---- Output ----
plot(cond ? 1 : 0, "Multi-TF Alignment", color = cond ? color.green : color.red, style = plot.style_columns)
plot(weeklyUptrend ? 1 : 0, "Weekly Uptrend", color = color.blue, style = plot.style_columns)
plot(dailyUptrend ? 1 : 0, "Daily Uptrend", color = color.purple, style = plot.style_columns)

alertcondition(cond, "Multi-timeframe alignment", "Weekly and daily trends aligned with a daily up-close")
```

## How to read the columns

- **"Weekly Uptrend"** — the higher-timeframe trend.
- **"Daily Uptrend"** — the lower-timeframe trend.
- **"Multi-TF Alignment"** — `1` = both timeframes agree *and* the daily trigger fired.

## Honest limitations

- **The trigger is a single bar.** `close > close[1]` is a weak "trigger"; in a real workflow it is replaced by something more specific (a breakout, a reversal off a level). It is kept simple here for clarity.
- **Two `request.security()` calls** — well within the 40-call limit, leaving ample headroom if you want to add a benchmark too.
- **Timeframe is fixed to weekly.** The Pine Screener supports standard timeframes, so weekly is fine — but you cannot switch to a *custom* higher timeframe within the scan.

Next: loading and using your screeners.
