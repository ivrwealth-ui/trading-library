# 3. Method 1 — Value Investing

## 3.1 The philosophy

Value investing buys assets for **less than their intrinsic worth** and waits for the market to correct the mispricing. The payoff comes from the gap between *price* and *value* — the **margin of safety** — closing over time.

It is the oldest, most-studied anomaly. In India it works best in:

- Deep market corrections (everyone's fearful, everything's cheap)
- Sectors temporarily out of favor (cyclicals at trough earnings, not peak)
- Neglected mid/small caps with real assets and earnings

It underperforms in long speculative bull runs — which is exactly when it *should* feel uncomfortable to hold.

## 3.2 The metrics

| Metric | Formula | What it captures | Watch out |
|---|---|---|---|
| **P/E** | Price / EPS (TTM) | Cheapness of earnings | Cyclical peak earnings → false cheap |
| **P/B** | Price / Book value | Asset-based cheapness | Best for **financials**; misleading for asset-light tech |
| **EV/EBITDA** | Enterprise value / EBITDA | Operating cheapness, debt-aware | Better than P/E across capital structures |
| **Earnings yield** | EPS / Price (=1/P/E) | Direct comparable to bond yield | Compare vs 10-yr G-sec yield |
| **Dividend yield** | DPS / Price | Income + discipline signal | High yield can signal distress |
| **Graham number** | √(22.5 × EPS × BVPS) | Quick intrinsic-value ceiling | Conservative; few large caps pass |
| **P/S** | Price / Sales | For early/unprofitable growth | Ignores profitability |

## 3.3 India-specific adaptations

1. **Use P/B for banks and NBFCs, not P/E.** Provisioning, NPA cycles, and tax treatment make P/E noisy for financials. Screen banks on P/B (historically roughly 0.8–1.5× for PSU, 2–3× for quality private) **plus** ROA (>1%), ROE (>12%), and NPA trend.

2. **Beware the commodity value trap.** A steel or chemical company at 6× P/E is often at **peak-cycle earnings** — the P/E is low *because* earnings are about to fall. Always check whether current margins are above the 10-year average. Value ≠ cheap on a cyclical high.

3. **Beware the governance discount.** Some Indian "cheap" stocks are cheap for good reason: promoter pledging, opaque related-party deals, chronic dilution. A 5× P/E with a questionable promoter is not a bargain — it's a terminal-value bet.

4. **Consolidated earnings only.** Holding companies and diversified groups routinely trade at a "conglomerate discount" that *looks* like value but is structurally persistent.

## 3.4 A concrete value screen (example)

Rank the Nifty 500 on a composite value score, excluding financials (handled separately):

```
Universe        : Nifty 500 (ex-banks/NBFCs)
Filters         :
  - TTM P/E          < 15
  - P/B              < 1.5
  - Debt/Equity      < 1.0  (or Net Debt/EBITDA < 2)
  - ROE (5-yr avg)   > 10%  (value-trap guard)
  - Positive operating cash flow, last 3 yrs
  - Promoter pledge  < 20%  (governance guard)
Rank            : ascending EV/EBITDA
Action          : top 15–25 names, equal weight, review quarterly
```

**The value-trap guard is non-negotiable.** Cheap + deteriorating = a trap; cheap + stable/improving = a candidate.

## 3.5 When value works, and when to abandon it

- **Works:** post-crash recoveries, sector rotation into out-of-favor industries, mean-reversion regimes.
- **Struggles:** long momentum bull markets, deflationary credit events (cheap gets cheaper), fraud-heavy microcaps.
