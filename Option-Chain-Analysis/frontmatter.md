# Option Chain Analysis: Reading Positioning and Building Quant Models from the Chain

## From open interest, PCR, and max pain to gamma exposure, the implied probability distribution, and the variance risk premium — the complete guide to deriving quantitative models from the option chain, with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading in options and derivatives involves substantial risk of loss, including the possible loss of principal and (for short options) the potential for very large losses. Past performance never guarantees future results.
- All models, formulas, examples, and historical observations are illustrative. A model is a *simplification of reality* — it describes tendencies and probabilities, never certainties, and every model in this book has known failure modes (detailed in Chapter 14).
- Open interest, implied volatility, and derived signals are computed from data that can be delayed, incomplete, or point-in-time inconsistent; always verify against current exchange data before any decision.
- Nothing in this book should be read as a promise of profit or a guarantee that any model will predict the market.

By reading this book, you agree that you are solely responsible for your own trading and investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches **option chain analysis** — reading the option chain's data (open interest, volume, implied volatility, and the Greeks) as a *map of market positioning* — and then building **quantitative models** from that data. It is the natural companion to *The Complete Options Trader* in this series (which covers the instruments and strategies); this book covers the *information* the chain contains.

- **Chapters 1–5** build the reading layer: the chain as a data structure, open interest as a positioning map, the put-call ratio, implied-volatility structure (skew and term structure), and max pain.
- **Chapters 6–12** build the *models*: the model-building discipline, delta exposure and dealer positioning, gamma exposure (GEX), the implied probability distribution, the variance risk premium, the expected move, and option-implied support/resistance.
- **Chapters 13–14** put it together — combining signals into a composite model — and cover the data-quality pitfalls that make every such model fail if ignored.
- The **appendix** is a formula reference and a table of every chain-derived signal.

A note on language: this book describes what the chain *shows* and how models *are built* — never what you "should" trade. Every signal is framed as a tendency, not a promise. You are responsible for your own decisions.

---

## Table of Contents

1. The Option Chain as a Data Structure
2. Open Interest: The Positioning Map
3. The Put-Call Ratio and Its Two Faces
4. Implied Volatility: Skew and Term Structure
5. Max Pain and Expiry Pinning
6. The Model-Building Discipline
7. Delta Exposure and Dealer Positioning
8. Gamma Exposure (GEX)
9. The Implied Probability Distribution
10. Realised vs. Implied: The Variance Risk Premium
11. The Expected Move and Event Pricing
12. Option-Implied Support and Resistance
13. Combining Signals into a Composite Model
14. Data Quality, Pitfalls, and Failure Modes

Appendix — Formula Reference and Signal Table

---
