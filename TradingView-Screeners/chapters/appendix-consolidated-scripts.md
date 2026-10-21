# Appendix — Consolidated Scripts

## The eight screeners at a glance

The full code for each script is in its chapter (3–10). This appendix is the index and the shared template. A composite that merges all eight screens into one indicator (a 0–8 score) is supplied alongside this book as `consolidated-8-factor-screener.pine`.

| # | Screener | Signal (what makes it pass) | Key columns | Chapter |
|---|----------|------------------------------|-------------|---------|
| 1 | Valuation | P/E ≤ max and P/B ≤ max (positive EPS) | P/E (TTM), P/B | 3 |
| 2 | Earnings Power | EPS growth ≥ min, revenue growth ≥ min, estimate > trailing | EPS Growth %, Revenue Growth % | 4 |
| 3 | Momentum | 12M return ≥ min, near 52-week high | 12M Return %, Dist from 52W High % | 5 |
| 4 | Stage Analysis | Price > rising 30-wk MA; 10-wk MA > 30-wk MA | Stage 2, Dist from 30W MA % | 6 |
| 5 | Outperformance | Relative strength ≥ min vs. benchmark | RS %, Stock %, Benchmark % | 7 |
| 6 | Price Contraction | Tight range + dry volume in uptrend | Range Contraction, Volume Ratio | 8 |
| 7 | Dow Theory | Primary uptrend + HH/HL + volume confirm | 3 sub-signals | 9 |
| 8 | Multi-Timeframe | Weekly uptrend + daily uptrend + daily trigger | Weekly/Daily sub-signals | 10 |

## The shared skeleton

Every script follows the same template — learn it once, and you can read and modify any of them:

```pine
//@version=6
indicator("Your Screener Title", overlay = false)

// ---- Inputs ----
// thresholds and lengths as input.*() calls

// ---- Data ----
// request.financial() / request.security() / ta.* calculations

// ---- Condition ----
bool cond = <your boolean logic, guarded against na>

// ---- Output ----
plot(<metric 1>, "Metric 1", color = color.blue)
plot(<metric 2>, "Metric 2", color = color.purple)
plot(cond ? 1 : 0, "Signal", color = cond ? color.green : color.red, style = plot.style_columns)

// ---- Filter ----
alertcondition(cond, "Signal name", "Human-readable message")
```

## The three rules that keep them working

1. **Guard every `na`** — `ignore_invalid_symbol = true` on every `request.*` call, and `not na(x)` in every condition. Missing data must produce *no signal*, not a crash.
2. **Stay within limits** — ≤40 `request.*` calls, ≤500-bar lookback, standard timeframes.
3. **Keep the signal binary and named** — one clearly titled `1`/`0` plot, plus the metric columns that let you sort.

## A reminder

These scripts are **educational and illustrative** — not guaranteed to compile on every plan, not a recommendation, and not a substitute for your own review of each result. A screener shortlists; you decide.
