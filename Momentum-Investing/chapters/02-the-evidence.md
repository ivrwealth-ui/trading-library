# 2. The Evidence: Why the Momentum Factor Persists

## The most studied anomaly in finance

Momentum is arguably the most thoroughly documented pattern in empirical finance. Understanding *how strong* the evidence is — and *why* the premium has not been arbitraged away — is essential, because a long-term investor must believe in the factor enough to hold it through its inevitable painful periods.

## The landmark studies

The modern momentum literature begins with **Jegadeesh and Titman (1993)**, *Returns to Buying Winners and Selling Losers*. They showed that ranking US stocks by their past 3–12 month returns and buying the winners while selling the losers produced persistent, economically significant excess returns over subsequent months. The canonical implementation — rank on the past 12 months, skip the most recent month, hold for 3–12 months — has become the reference "12-1 momentum" (also written 12-1 or 12_1) that practitioners still use.

The result has been replicated at extraordinary scale:

- **Across time** — momentum has been documented in data going back a century.
- **Across geographies** — the effect appears in developed and emerging markets alike, including Indian equities.
- **Across asset classes** — momentum exists in stocks, indices, sectors, currencies, commodities, and government bonds.

Subsequent landmark work sharpened the picture:

- **George & Hwang (2004)** showed that a stock's *nearness to its 52-week high* is a strong, robust momentum signal in its own right.
- **Moskowitz, Ooi & Pedersen (2012)** documented **time-series momentum** — the tendency of an asset's *own* past return to predict its *own* future return — across dozens of markets and asset classes.
- **Antonacci (2014)** popularised **dual momentum**, combining relative and absolute momentum into a single, practical framework.

## Why it works: behaviour and risk

The premium survives for two reinforcing reasons — one behavioural, one structural.

### The behavioural story

Investors are human, and systematically so:

- **Under-reaction.** Markets incorporate news gradually, not instantly. Investors *under-react* to information, then catch up — which is precisely what creates a trend a momentum investor can ride.
- **Herding.** Once a trend is visible, investors pile in, extending it beyond fundamentals.
- **Anchoring.** Investors anchor on old prices and are slow to update their view of what an asset is "worth."
- **The disposition effect.** Investors sell winners too early and hold losers too long, which *dampens* the natural selling pressure on winners (helping them keep rising) and *delays* the recovery of losers (keeping them falling).

### The structural story

- **Institutional herding and career risk.** Fund managers, judged on short-term relative performance, buy what has worked — reinforcing momentum.
- **Slow-moving capital.** Large investors trade gradually to limit market impact, spreading their buying over time and *creating* the trend they are following.
- **Risk compensation.** Momentum is not pure inefficiency; it is partly *payment for risk*. Momentum strategies crash during sharp market reversals — and that tail risk is why the premium has not been arbitraged away. Investors demand compensation for bearing it.

## The elephant in the room: momentum crashes

The most important thing to know about momentum is its **failure mode**. Momentum portfolios are systematically long recent winners and (in the academic long-short version) short recent losers. After a sharp market *bottom*, the losers snap back hardest — and the momentum portfolio, positioned exactly the wrong way, suffers a violent, concentrated loss. This is the **momentum crash**.

Two facts follow:

1. The premium is **real but lumpy** — long calm stretches punctuated by sharp drawdowns.
2. **Long-only momentum** (holding winners, holding cash/benchmark instead of shorting losers) sidesteps much of the crash risk, which is why most practical momentum strategies in this book are long-only, with an absolute filter.

## The honest framing

This book describes momentum as "historically proven" in a precise and limited sense: the factor has been *documented and replicated* across long periods, many markets, and multiple asset classes. That is strong evidence — but it is not a guarantee, for three reasons:

- Historical persistence is evidence of a tendency, not a law of nature.
- The specific implementation (universe, lookback, rebalancing, costs) changes the realised result materially.
- The premium is compensation for *risk*, and the risk is real and periodically shows up.

Framed as this book always frames such things: *historically, portfolios tilted toward recent winners have tended to outperform over multi-year horizons — but that tendency is punctuated by sharp reversals, and the investor must be able to survive them to collect the premium.*

## Summary

- Momentum is the most replicated anomaly in finance (Jegadeesh & Titman, 1993).
- Documented across time, geographies, and asset classes — including India.
- Driven by under-reaction, herding, anchoring, and the disposition effect; sustained by institutional herding, slow capital, and risk compensation.
- Momentum crashes are the known failure mode; long-only + absolute filter mitigates them.
- The premium is real but lumpy — and it is paid for bearing risk.

Next: the toolkit — the concepts and metrics the strategies use.
