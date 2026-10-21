# 5. Screener 3 — Momentum (12-Month Return, 52-Week High)

## The strategy

**Momentum** is the well-documented tendency of recent winners to keep winning. This screener encodes the two most common momentum measures at once: a **12-month rate of change** (the classic lookback) and **proximity to the 52-week high** (a psychologically salient anchor that research suggests has historically been associated with continued outperformance).

This is a pure *price* screen — no fundamental data required, so it works on any symbol with price history.

## The logic

- **12-month return** = `ta.roc(close, 252)` — the rate of change over ~252 trading days.
- **Distance from the 52-week high** = `(close / ta.highest(close, 252)) * 100 - 100` — 0% means *at* the high; −10% means 10% below it.

The signal fires when the 12-month return exceeds a threshold **and** the stock is within a small distance of its 52-week high (strength confirmed by being near the top of its range).

## The code

```pine
//@version=6
indicator("Momentum Screen (12M Return + 52W High)", overlay = false)

// ---- Inputs ----
float minReturn = input.float(15.0, "Min 12-month return %")
float maxFromHigh = input.float(-10.0, "Max distance below 52W high (%)")  // negative number: -10 means "within 10% of the high"; entering a positive value will silently match nothing

// ---- Signals (252 bars ≈ 12 months; within the ~500-bar screener limit) ----
float roc = ta.roc(close, 252)
float high52 = ta.highest(close, 252)
float pctFromHigh = high52 > 0 ? (close / high52) * 100 - 100 : na

// ---- Screen condition ----
bool momOk     = not na(roc) and roc >= minReturn
bool nearHigh  = not na(pctFromHigh) and pctFromHigh >= maxFromHigh

bool cond = momOk and nearHigh

// ---- Output ----
plot(roc, "12M Return %", color = color.blue)
plot(pctFromHigh, "Dist from 52W High %", color = color.purple)
plot(cond ? 1 : 0, "Momentum Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Momentum candidate", "Strong 12M return and near the 52-week high")
```

## How to read the columns

- **"12M Return %"** — sort descending for the strongest momentum.
- **"Dist from 52W High %"** — sort descending (closest to 0, i.e., nearest the high).
- **"Momentum Signal"** — `1` = passes both, `0` = fails.

## Honest limitations

- **Momentum reverses sharply.** After market bottoms, prior winners lag the sharp recovery in prior losers; the momentum premium arrives in lumps.
- **No trend filter.** This screen does not check whether the *broad market* is trending up; a momentum screen in a bear market surfaces the least-bad names, not necessarily good ones.
- **No fundamental context.** A momentum screen will happily flag a falling-quality stock that happens to be rallying; pair with a valuation/earnings screen for a techno-funda combination.

Next: Screener 4 — Stage Analysis.
