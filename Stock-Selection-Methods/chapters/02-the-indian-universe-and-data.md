# 2. The Indian Universe & Data

## 2.1 The universe ladder

India has a clean, liquid tiered index system. Pick your universe deliberately — it defines both your opportunity and your execution cost.

| Universe | Constituents | Liquidity | Notes |
|---|---|---|---|
| Nifty 50 | 50 large caps | Excellent | Mostly institutional; momentum is weaker, value plays classic |
| Nifty Next 50 | 51–100 | Very good | Sweet spot for quality compounding + multi-factor |
| Nifty Midcap 150 | 101–250 | Good | Higher growth, higher vol, momentum works well |
| Nifty Smallcap 250 | 251–500 | Mixed | High returns, high illiquidity/impact risk |
| **Nifty 500** | 1–500 | Broad | Best default universe for systematic methods |
| Nifty Total Market | ~750+ | Variable | Adds microcaps; treat with caution |

**Recommendation:** start with **Nifty 500** for backtesting and screening, then tilt execution toward the top ~200–300 names where impact cost is tolerable. Avoid the microcap tail unless you have a dedicated illiquidity risk budget.

## 2.2 Data you'll need (and where to get it)

| Data | Why | Sources |
|---|---|---|
| Prices (EOD OHLCV) | Returns, momentum, vol | NSE/BSE bhavcopy, broker APIs (Zerodha Kite), `yfinance`, Chartink |
| Fundamentals | Value & quality factors | Screener.in, Tijori Finance, Trendlyne, exchange filings; Capitalmind (a PMS/mutual-fund house whose public research is useful context, not a data feed) |
| Corporate actions | Adjust for bonus/split/rights | NSE announcements, bhavcopy metadata |
| Index membership | Universe definition | NSE indices page, monthly rebalance lists |
| Delistings/mergers | Survivorship-bias correction | NSE, SEBI orders, MCA |
| Ownership | Promoter/pledge/FII-DII | BSE shareholding pattern (quarterly) |

**See Appendix B (Indian Data Sources & Tools) for a full tool list.**

## 2.3 Adjustments you must never skip

Indian companies issue **bonus shares, stock splits, rights issues, and buybacks** frequently. Raw price data will show phantom drops that ruin both momentum and volatility calculations. Three rules:

1. **Use adjusted (split/bonus-adjusted) prices** for anything involving multi-period returns.
2. **For total return**, add dividends back — India's market dividend yield has historically run at roughly 1–1.5%, which compounds materially over a decade. (Dividends are taxable in the investor's hands since FY21.)
3. **Never mix standalone and consolidated financials.** For companies with meaningful subsidiaries, always use **consolidated** figures; standalone hides the real picture for holding structures and diversified groups.

## 2.4 Point-in-time discipline

For an honest backtest, every factor value must be the value *known on that date*:

- Earnings: use the most recent **announced** quarter, not simply the latest quarter to have ended.
- Index membership: use the membership list *as of that month*.
- Shareholding: listed companies must file the quarterly pattern within 21 days of quarter-end (SEBI LODR Regulation 31) — use the filing date, not the quarter-end date.
