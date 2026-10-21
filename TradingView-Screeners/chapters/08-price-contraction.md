# 8. Screener 6 — Price Contraction (VCP)

## The strategy

The **Volatility Contraction Pattern (VCP)** — associated with Mark Minervini's work — describes a specific, high-quality setup: a stock in an **uptrend** that is forming a **tight base**, with **successive contractions** in price range and a **dry-up in volume**. The logic is that a tightening range with shrinking volume marks a period of quiet accumulation after a rise, which is often cited as a precursor to the *next* leg up.

This screener encodes VCP as three measurable conditions: uptrend, range contraction, and volume dry-up.

## The logic

- **Uptrend** — price above the 200-day MA (the stock has been rising).
- **Range contraction** — the current ATR is a *fraction* of the ATR some time ago (the price range has tightened). Computed as `ta.atr(14) / ta.atr(14)[lookback]`.
- **Volume dry-up** — the recent average volume is a *fraction* of the average volume some time ago (trading has quieted). Computed as `ta.sma(volume, 20) / ta.sma(volume, 20)[lookback]`.

When the range has tightened below a threshold *and* volume has dried up below a threshold *within an uptrend*, the VCP condition is present.

## The code

```pine
//@version=6
indicator("Price Contraction (VCP: Tight Base + Volume Dry-up)", overlay = false)

// ---- Inputs ----
int shortAtr  = input.int(14, "ATR length")
int lookback  = input.int(60, "Contraction lookback (bars)")
float maxContraction = input.float(0.60, "Max range contraction (ATR now/prev)")
float maxVolRatio    = input.float(0.75, "Max volume ratio (now/prev)")

// ---- Range contraction ----
float atrNow  = ta.atr(shortAtr)
float atrPrev = ta.atr(shortAtr)[lookback]
float contraction = atrNow / atrPrev        // < 1 → range tightened

// ---- Volume dry-up ----
float volNow  = ta.sma(volume, 20)
float volPrev = ta.sma(volume, 20)[lookback]
float volRatio = volNow / volPrev           // < 1 → volume dried up

// ---- Uptrend filter ----
float ma200 = ta.sma(close, 200)

// ---- Screen condition ----
bool uptrend = close > ma200
bool tight   = not na(contraction) and contraction < maxContraction
bool dryUp   = not na(volRatio) and volRatio < maxVolRatio

bool cond = uptrend and tight and dryUp

// ---- Output ----
plot(contraction, "Range Contraction (ATR now/prev)", color = color.blue)
plot(volRatio, "Volume Ratio (now/prev)", color = color.purple)
plot(cond ? 1 : 0, "VCP Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "VCP contraction", "Tightening range and drying volume in an uptrend")
```

## How to read the columns

- **"Range Contraction (ATR now/prev)"** — lower = tighter; sort ascending.
- **"Volume Ratio (now/prev)"** — lower = drier; sort ascending.
- **"VCP Signal"** — `1` = tight, dry, and in an uptrend.

## Honest limitations

- **VCP is a *setup*, not a *trigger*.** The screen flags the *condition* (a coiled spring); it does not tell you *when* the next leg begins. The traditional trigger is the *breakout* from the tight base — which this screen deliberately leaves for you to time.
- **A contraction can precede a *breakdown*, not just a breakout.** A tight base near the top of an extended run can resolve downward. Review the trend context before acting.
- **Parameter sensitivity.** "Tight" and "dry" are thresholds; the pattern is better read *visually* (on a chart) than by any single numeric cut. Use this as a shortlister, not a verdict.

Next: Screener 7 — Dow Theory.
