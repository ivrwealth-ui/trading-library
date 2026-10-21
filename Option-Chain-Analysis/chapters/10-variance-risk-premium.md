# 10. Realised vs. Implied: The Variance Risk Premium

## The chain's built-in bias — and what it is worth

The previous chapter's implied distribution has a known *bias*: it overstates the probability of extreme moves. That bias has a name and a value — the **variance risk premium (VRP)** — and it is the single most economically important model in this book, because it explains *why* selling options earns money on average, and *what* that money is really compensation for.

## The definition

**Realised volatility (RV)** is what the market *actually did* — the volatility computed from the underlying's actual price moves over a period.

**Implied volatility (IV)** is what the market *expected* — the volatility priced into the options (Chapter 4).

The **variance risk premium** is the systematic gap between them:

VRP = Implied volatility − Realised volatility (quoted here in volatility terms)

The widely reported empirical finding: **on average, IV exceeds RV.** Options are priced a little *rich* relative to what actually happens. The implied distribution's fat tails (Chapter 9) are, on average, *fatter than reality* — the market persistently overpays for the possibility of a crash.

## Why the premium exists

The VRP is not a free lunch or a market error; it is **compensation for bearing crash risk.** Three forces sustain it:

1. **Demand for protection.** Investors are *risk-averse* and systematically buy downside protection (puts), bidding up option prices above their "fair" actuarial value. This is the same force behind the skew (Chapter 4) — the market pays up for insurance, structurally.
2. **The asymmetry of crashes.** When the "overpriced" protection is needed (a crash), it pays off enormously; when it is not needed, it quietly expires worthless. Selling it earns a steady stream — *until* the crash.
3. **Short-vol capital.** Selling volatility to collect the VRP is a crowded, well-understood trade — which is why the premium persists but is *risky*: it is the "picking up pennies in front of a steamroller" trade, formalised.

## The model: harvesting (or measuring) the VRP

The VRP is used two ways, which must be kept distinct:

### 1. As a *signal* (measuring when options are cheap or expensive)

Compare IV to recent RV (or to its own history, the IV rank/percentile of *The Complete Options Trader*):

- **IV far above RV** → options are historically expensive → historically, this has favoured *reduced exposure to option buying* (or increased premium collection).
- **IV far below RV** → options are cheap → historically favoured the reverse.

This is the *entry filter* for volatility strategies: buy vol when it is cheap, sell vol when it is rich.

### 2. As a *trade* (collecting the premium directly)

A systematic short-volatility strategy — selling straddles, strangles, or condors across many expiries — is, in effect, **harvesting the VRP**: collecting the average excess of IV over RV. Its historical profile is the trade's defining fact:

- **Most of the time:** small, steady gains (the premium decays, and IV > RV).
- **Occasionally:** a large, sudden loss (a crash, when RV spikes *above* IV and the short-vol position loses far more than the accumulated premium).

## The honest framing

The VRP is the reason this book must be careful with language:

> *Historically, systematically collecting the variance risk premium has tended to earn a steady positive return — punctuated by sharp losses precisely when realised volatility spikes. The premium is compensation for bearing crash risk, not a free lunch; the trader who collects it is selling insurance, and insurance is paid out in exactly the scenarios the seller least wants.*

This is why every short-vol model (and every GEX-negative read, Chapter 8) carries the same discipline from *Risk Management and Position Sizing*: **size for the tail, cap the exposure, and never mistake a risk premium for a certainty.**

## The VRP and the rest of the book

The VRP ties the whole book together:

- It is *why* the implied distribution overstates tails (Chapter 9).
- It is *why* IV's level (rank/percentile) is a meaningful entry filter (Chapter 4).
- It is *why* GEX-negative markets (Chapter 8) — where dealers are short gamma and vol can spike — are the dangerous environments for premium collection.
- It is the *economic engine* behind income strategies, framed honestly rather than as "free money."

## Summary

- VRP = IV − RV; on average IV > RV — options are priced rich.
- It exists as compensation for crash risk: investors pay up for protection, structurally.
- Use it as a signal (IV vs. RV = cheap/expensive) or a trade (systematic short-vol harvests it).
- The short-vol profile: steady small gains, punctuated by sharp losses in crashes.
- It is a risk premium, not a free lunch — size for the tail.

Next: the expected move and event pricing.
