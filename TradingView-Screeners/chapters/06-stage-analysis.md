# 6. Screener 4 — Stage Analysis (Weinstein Stage 2)

## The strategy

**Stage Analysis** (Stan Weinstein's methodology) holds that stocks move through four *stages* — basing (Stage 1), advancing (Stage 2), topping (Stage 3), and declining (Stage 4) — and that **Stage 2**, the *advancing* stage, is often cited as the highest-probability period to own a stock: it is where price is above a rising long-term moving average and the trend is up.

This screener encodes the classic Stage 2 definition on a daily chart, using the 30-week and 10-week moving averages (150 and 50 daily bars).

## The logic

Weinstein's Stage 2, expressed as rules:

1. **Price is above the 30-week (150-day) MA** — the primary trend is up.
2. **The 30-week MA is rising** — the trend is *advancing*, not just flat.
3. **The 10-week (50-day) MA is above the 30-week MA** — the shorter-term trend is leading the longer-term trend (an orderly uptrend).

When all three hold, the stock is in the advancing stage.

## The code

```pine
//@version=6
indicator("Stage Analysis (Weinstein Stage 2)", overlay = false)

// ---- Inputs ----
int longMa  = input.int(150, "30-week MA (daily bars)", minval = 1)
int shortMa = input.int(50,  "10-week MA (daily bars)", minval = 1)

// ---- Moving averages ----
float ma30 = ta.sma(close, longMa)
float ma10 = ta.sma(close, shortMa)

// ---- Stage 2 conditions ----
bool aboveLong     = close > ma30          // price above 30-week MA
bool longRising    = ma30 > ma30[1]        // 30-week MA rising
bool shortAboveLong = ma10 > ma30          // 10-week MA above 30-week MA

bool stage2 = aboveLong and longRising and shortAboveLong

// ---- Output ----
plot(stage2 ? 1 : 0, "Stage 2 Signal", color = stage2 ? color.green : color.red, style = plot.style_columns)
plot(close / ma30 * 100 - 100, "Dist from 30W MA %", color = color.blue)

alertcondition(stage2, "Stage 2 (Weinstein)", "Price above a rising 30-week MA, with the 10-week MA above the 30-week MA")
```

## How to read the columns

- **"Stage 2 Signal"** — `1` = in the advancing stage, `0` = not.
- **"Dist from 30W MA %"** — how far price is above the 30-week MA; a very large positive value means the stock is *extended* (a caveat — see below).

## Honest limitations

- **Lateness by design.** Stage 2 is confirmed only *after* the advance has begun; the screen never catches the exact bottom of Stage 1.
- **Extension risk.** A stock far above its 30-week MA (large "Dist from 30W MA %") has run up fast and is due for a pullback; use the distance column to distinguish *early* Stage 2 (near the MA) from *late* Stage 2 (extended).
- **No volume check in this version.** Weinstein also emphasised volume on the breakout; that refinement is left out here to keep the script within the screener's simplicity, but can be added.

Next: Screener 5 — Outperformance (relative strength).
