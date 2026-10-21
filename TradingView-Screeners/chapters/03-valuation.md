# 3. Screener 1 — Valuation (P/E, P/B)

## The strategy

**Value investing** holds that stocks trading cheaply relative to their earnings and book value tend to outperform expensive ones over long horizons — a pattern research suggests has held historically, though not in every period. This screener encodes the classic two-ratio value screen: a reasonable **price-to-earnings** and **price-to-book**.

Note the important boundary: this is a *filter for cheapness*, not a buy signal. A cheap stock can stay cheap (the "value trap"). In practice, pair this screen with a technical trigger (an uptrend or a reversal — see the *Techno-Funda* book in this series) before acting.

## The logic

For the symbol being scanned, pull three fundamentals and compute two ratios:

- **P/E (TTM)** = `close / EPS (TTM)`.
- **P/B** = `close / book-value-per-share`, where book value per share = `TOTAL_EQUITY / TOTAL_SHARES_OUTSTANDING`.

The signal fires when **both** P/E and P/B are positive and below their thresholds. Positive EPS is required implicitly: P/E is only ever computed (never `na`) when EPS is positive, so a loss-making company can never pass this screen. When fundamental data is missing, the ratios are `na` and the signal simply does not fire.

## The code

```pine
//@version=6
indicator("Valuation Screen (P/E, P/B)", overlay = false)

// ---- Inputs ----
float peMax  = input.float(25.0, "Max P/E (TTM)")
float pbMax  = input.float(3.0,  "Max P/B")

// ---- Fundamentals (ignore_invalid_symbol = true → na when no data) ----
float epsTtm = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE_BASIC", "TTM", ignore_invalid_symbol = true)
float totEq  = request.financial(syminfo.tickerid, "TOTAL_EQUITY", "FY", ignore_invalid_symbol = true)
float shares = request.financial(syminfo.tickerid, "TOTAL_SHARES_OUTSTANDING", "FQ", ignore_invalid_symbol = true)

// ---- Derived ratios ----
// Positive EPS is required here, not via a separate toggle: a loss-making
// company (epsTtm <= 0) makes pe na, which the condition below excludes.
float pe   = epsTtm > 0 ? close / epsTtm : na
float bvps = (totEq > 0 and shares > 0) ? totEq / shares : na
float pb   = bvps > 0 ? close / bvps : na

// ---- Screen condition ----
bool cond  = not na(pe) and pe > 0 and pe <= peMax and not na(pb) and pb > 0 and pb <= pbMax

// ---- Output: metric columns + signal column ----
plot(pe, "P/E (TTM)", color = color.blue)
plot(pb, "P/B", color = color.purple)
plot(cond ? 1 : 0, "Value Signal", color = cond ? color.green : color.red, style = plot.style_columns)

// ---- Filter ----
alertcondition(cond, "Value candidate", "P/E and P/B at or below their thresholds")
```

## How to read the columns

When you add this to the screener and scan a watchlist:

- **"P/E (TTM)"** and **"P/B"** — sortable numeric columns; sort ascending to surface the cheapest.
- **"Value Signal"** — `1` = passes the screen, `0` = fails. Filter on "Value Signal == 1".

## Honest limitations

- **Data availability** — fundamental data is often missing for smaller NSE/BSE names; those simply show no signal.
- **Value trap** — cheap ≠ about-to-rise; pair with a technical trigger.
- **One ratio is not a thesis** — a low P/E can be a warning (deteriorating business), not an opportunity; review each result.

Next: Screener 2 — Earnings Power.
