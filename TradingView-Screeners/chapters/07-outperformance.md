# 7. Screener 5 — Outperformance (Relative Strength vs. Benchmark)

## The strategy

**Relative strength** (not the RSI oscillator — here, *relative performance*) measures whether a stock is *outperforming its benchmark*. The idea is that **leadership persists**: research suggests a stock that has beaten the index over the last several months has historically tended to keep leading. This screener ranks stocks by their return *minus* the benchmark's return over a trailing window.

The classic benchmark for Indian equities is **NIFTY 50** (`NSE:NIFTY` in TradingView).

## The logic

For the scanned symbol and the benchmark:

- **Stock return** = `ta.roc(close, lookback)`.
- **Benchmark return** = `ta.roc(benchmark close, lookback)`, where the benchmark close is pulled via `request.security()`.
- **Relative strength** = stock return − benchmark return.

The signal fires when relative strength is positive (or above a threshold) — the stock is beating the benchmark.

## The code

```pine
//@version=6
indicator("Outperformance (Relative Strength vs Benchmark)", overlay = false)

// ---- Inputs ----
string benchmark = input.symbol("NSE:NIFTY", "Benchmark")  // input.symbol() returns a string ticker id, not a `symbol` type
int rsLookback = input.int(126, "RS lookback (bars)", minval = 1)   // ~6 months
float minRs = input.float(0.0, "Min relative return %")

// ---- Benchmark data (1 request.security call) ----
float benchClose = request.security(benchmark, timeframe.period, close, ignore_invalid_symbol = true)

// ---- Returns and relative strength ----
float stockRet = ta.roc(close, rsLookback)
float benchRet = ta.roc(benchClose, rsLookback)
float rs = stockRet - benchRet

// ---- Screen condition ----
bool cond = not na(rs) and rs >= minRs

// ---- Output ----
plot(rs, "Relative Strength (6M) %", color = cond ? color.teal : color.gray)
plot(stockRet, "Stock 6M Return %", color = color.blue)
plot(benchRet, "Benchmark 6M Return %", color = color.purple)
plot(cond ? 1 : 0, "Outperform Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Outperformer", "Stock outperforming benchmark over 6 months")
```

## How to read the columns

- **"Relative Strength (6M) %"** — sort descending to surface the biggest outperformers.
- **"Stock 6M Return %"** and **"Benchmark 6M Return %"** — the two components, so you can see *why* a stock is an outperformer (strong stock vs. weak benchmark).
- **"Outperform Signal"** — `1` = beating the benchmark, `0` = lagging.

## Honest limitations

- **Relative, not absolute.** A stock can be a "relative outperformer" while still *falling* (if it falls less than the benchmark). Pair with an absolute trend filter (Screener 4's Stage 2, or simply price > 200-day MA) to require actual strength.
- **Benchmark mismatch.** Relative strength vs. NIFTY 50 is less meaningful for small-caps (whose benchmark is really the broader market). Choose the benchmark that matches the watchlist you scan.
- **Benchmark input is fixed in the Pine Screener.** The Pine Screener does not support `input.symbol()`: it ignores any benchmark chosen in the settings and uses the script's default (`NSE:NIFTY`). To scan against a different benchmark, change the default in the code.
- **Crowding.** The most obvious outperformers are often the most crowded, and crowded names reverse sharply when leadership rotates.

Next: Screener 6 — Price Contraction (VCP).
