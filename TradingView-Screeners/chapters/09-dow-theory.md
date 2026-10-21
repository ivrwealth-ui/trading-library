# 9. Screener 7 — Dow Theory (Trend Structure + Volume)

## The strategy

**Dow Theory** — the oldest formal framework of technical analysis — holds that a genuine uptrend is defined by **structure** and **confirmation**:

- **Primary trend up** (the stock's primary trend is up).
- **Higher highs and higher lows** (the defining structure of an uptrend).
- **Volume confirmation** (rising volume on up-moves, falling on down-moves).

This screener encodes those three ideas into a single pass/fail condition.

## The logic

- **Primary trend up** — the stock is above its 200-day MA, and its 50-day MA is above its 200-day MA (an orderly uptrend).
- **Higher highs and higher lows** — the recent N-day *high* is higher than the prior N-day high, and the recent N-day *low* is higher than the prior N-day low. (Using `ta.highest()`/`ta.lowest()` over a swing window, compared to the same window one swing ago.)
- **Volume confirmation** — the average volume on up-days exceeds the average volume on down-days over the last 20 bars.

## The code

```pine
//@version=6
indicator("Dow Theory (Trend Structure + Volume)", overlay = false)

// ---- Inputs ----
int swingLen = input.int(30, "Swing window (bars)")

// ---- Moving averages (primary trend) ----
float ma200 = ta.sma(close, 200)
float ma50  = ta.sma(close, 50)
bool primaryUp = close > ma200 and ma50 > ma200

// ---- Higher highs and higher lows ----
float recentLow = ta.lowest(low, swingLen)
float priorLow  = ta.lowest(low, swingLen)[swingLen]
bool higherLow  = recentLow > priorLow

float recentHigh = ta.highest(high, swingLen)
float priorHigh  = ta.highest(high, swingLen)[swingLen]
bool higherHigh  = recentHigh > priorHigh

bool structure = higherHigh and higherLow

// ---- Volume confirmation ----
float upVol   = close > close[1] ? volume : 0.0
float downVol = close < close[1] ? volume : 0.0
bool volConfirm = ta.sma(upVol, 20) > ta.sma(downVol, 20)

// ---- Screen condition ----
bool cond = primaryUp and structure and volConfirm

// ---- Output ----
plot(cond ? 1 : 0, "Dow Uptrend Signal", color = cond ? color.green : color.red, style = plot.style_columns)
plot(primaryUp ? 1 : 0, "Primary Trend Up", color = color.blue, style = plot.style_columns)
plot(structure ? 1 : 0, "HH+HL Structure", color = color.purple, style = plot.style_columns)

alertcondition(cond, "Dow theory uptrend", "Primary uptrend with higher highs/lows and volume confirmation")
```

## How to read the columns

Three sub-columns, so you can see *which* condition a failing stock is missing:

- **"Primary Trend Up"** — above the 200-day MA with the 50-day above it.
- **"HH+HL Structure"** — making higher highs and higher lows.
- **"Dow Uptrend Signal"** — `1` = all three (primary trend, structure, and volume) confirm.

## Honest limitations

- **The swing window is a simplification.** True Dow Theory reads *significant* swing points, not a fixed 30-bar window; the fixed window is a tractable proxy, not a faithful implementation.
- **Confirmation is late.** "Higher highs/lows + volume confirmation" is only confirmable *after* the fact; the screen identifies an uptrend that is *already* established, not an early entry.
- **No fundamental layer.** Dow Theory is purely technical; pair with a valuation or earnings screen if you want a techno-funda combination.

Next: Screener 8 — Multi-Timeframe.
