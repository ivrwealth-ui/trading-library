# 4. NSE Specifics That Matter

Before the strategies, the practical Indian context:

- **Instruments.** Nifty and BankNifty index options are the deep, liquid core. Individual stock options exist but are thinner and physically settled — check the contract before trading.
- **Expiries.** Since SEBI's November 2024 rules, each exchange may offer only **one weekly** index expiry. On the NSE that is Nifty (weekly expiry on **Tuesday** since September 2025, previously Thursday); BankNifty and the other NSE indices now have **monthly** expiries only. Weekly-expiry conventions (which day, which index) have been revised by SEBI/NSE over time — **confirm the current weekly expiry day** before trading weeklies.
- **Lot sizes.** Index option lot sizes have changed over the years (and differ between Nifty and BankNifty). **Check the current lot size** and multiply the point-based P&L diagrams here by the lot size to get rupee P&L.
- **Margins.** Buying an option costs only the premium. **Selling** an option requires margin (SPAN + exposure). Covered positions (covered call on a futures/stock position) attract lower margin than naked shorts. Margin is a first-class constraint in every short-option strategy in this book.
- **Settlement.** Index options are European and cash-settled at expiry — no early exercise, no delivery worry. Payoff at expiry is exactly what the diagrams show.

**A note on the diagrams.** All payoff diagrams are drawn **at expiry, in points** (not rupees). To convert: `rupee P&L = point P&L × lot size`. The illustrative spot is 22,000 with strikes around it; substitute your own spot and strikes in real use.
