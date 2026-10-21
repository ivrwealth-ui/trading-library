# 4. Screener 2 — Earnings Power (EPS & Revenue Growth)

## The strategy

**Earnings-power investing** holds that what ultimately drives a stock over time is the *growth of its earnings* — and research suggests the market often under-reacts to accelerating earnings. This screener flags companies whose **earnings and revenue are growing** at a meaningful rate, and whose **forward estimate** points to continued growth.

This is a *fundamental-momentum* screen: it does not care how cheap a stock is, only whether its profit engine is expanding.

## The logic

Pull three growth-related fundamentals and test them against thresholds:

- **EPS growth (year-over-year)** — `EARNINGS_PER_SHARE_BASIC_ONE_YEAR_GROWTH` (TTM).
- **Revenue growth (year-over-year)** — `REVENUE_ONE_YEAR_GROWTH` (TTM).
- **Forward estimate above trailing EPS** — `EARNINGS_ESTIMATE` (FY) greater than trailing EPS (TTM), i.e., the market expects growth to continue.

The signal fires when EPS and revenue growth exceed their thresholds, and the forward estimate confirms (or estimate data is unavailable, in which case that sub-check is skipped rather than failing).

## The code

```pine
//@version=6
indicator("Earnings Power (EPS & Revenue Growth)", overlay = false)

// ---- Inputs ----
float minEpsGrowth = input.float(15.0, "Min EPS growth % YoY")
float minRevGrowth = input.float(10.0, "Min revenue growth % YoY")

// ---- Fundamentals ----
float epsGrowth = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC_ONE_YEAR_GROWTH", "TTM", ignore_invalid_symbol = true)
float revGrowth = request.financial(syminfo.tickerid, "REVENUE_ONE_YEAR_GROWTH", "TTM", ignore_invalid_symbol = true)
float epsEst    = request.financial(syminfo.tickerid, "EARNINGS_ESTIMATE", "FY", ignore_invalid_symbol = true)
float epsTtm    = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC", "TTM", ignore_invalid_symbol = true)

// ---- Screen condition ----
bool epsOk  = not na(epsGrowth) and epsGrowth >= minEpsGrowth
bool revOk  = not na(revGrowth) and revGrowth >= minRevGrowth
// Forward estimate above trailing EPS → expected continued growth (skipped if no estimate data)
bool estOk  = (na(epsEst) or na(epsTtm) or epsTtm <= 0) ? true : epsEst > epsTtm

bool cond = epsOk and revOk and estOk

// ---- Output ----
plot(epsGrowth, "EPS Growth YoY %", color = color.teal)
plot(revGrowth, "Revenue Growth YoY %", color = color.olive)
plot(cond ? 1 : 0, "Earnings Power Signal", color = cond ? color.green : color.red, style = plot.style_columns)

alertcondition(cond, "Earnings power candidate", "EPS and revenue growing above thresholds")
```

## How to read the columns

- **"EPS Growth YoY %"** and **"Revenue Growth YoY %"** — sortable; sort descending to surface the fastest growers.
- **"Earnings Power Signal"** — `1` = passes, `0` = fails. Filter on `== 1`.

## Honest limitations

- **Four `request.financial()` calls** — well within the Pine Screener's 40-call ceiling, so there is room to add a benchmark for relative strength; just remember that every extra fundamental condition is another chance for missing data to block the signal.
- **Growth quality vs. quantity** — a high growth rate can be a one-off (an acquisition, a base effect). The screen flags the number, not the *quality* of the growth; review each result.
- **Data availability** — same caveat as Screener 1: missing data means no signal.

Next: Screener 3 — Momentum.
