# 10. The Six Factors That Move an Option's Price

## Six inputs, one output

An option's premium is not a mystery — it is a function of six identifiable inputs. Change any one, and the premium changes in a predictable way.

| # | Factor | Symbol | Effect on call price | Effect on put price |
|---|--------|--------|----------------------|---------------------|
| 1 | Underlying price | S | ↑ | ↓ |
| 2 | Strike price | K | ↓ | ↑ |
| 3 | Time to expiry | T | ↑ | ↑ |
| 4 | Volatility | σ | ↑ | ↑ |
| 5 | Risk-free rate | r | ↑ | ↓ |
| 6 | Dividends (stocks) | q | ↓ | ↑ |

Three of these — underlying, strike, and time — are *known* at any moment. One — volatility — is *estimated* and is the only input you cannot look up. The interest rate is observable and small; dividends apply to single stocks and not to indices (for index pricing, the index dividend yield plays a parallel role).

## Factor by factor

### 1. Underlying price (S)

The most obvious driver. A call is a right to buy, so a higher underlying makes it more valuable. A put is a right to sell, so a higher underlying makes it *less* valuable. This relationship is quantified by **delta** (Chapter 11).

### 2. Strike price (K)

A call with a lower strike (buy cheaper) is worth more than a call with a higher strike. A put with a higher strike (sell dearer) is worth more than a put with a lower strike. Strike is fixed when you enter the trade — it is the *choice* you make, not a market driver — but comparing across strikes is how you read the chain (moneyness, Chapter 4).

### 3. Time to expiry (T)

More time means more opportunity for the underlying to move in your favour — and more uncertainty for the seller to be paid for. Hence, *all else equal*, longer-dated options cost more. As time passes, this premium erodes; the erosion is **theta** (Chapter 12). Time affects both calls and puts the same way: more time, higher price.

### 4. Volatility (σ)

The estimated *size* of future price swings. Higher volatility means a wider range of possible future prices, which increases the option's value for the buyer — for both calls and puts. Volatility is the input you cannot observe directly; you must **imply** it from the option's market price (implied volatility, Chapter 16), or **estimate** it from history (historical volatility). Its sensitivity is **vega** (Chapter 13). Volatility is arguably the *most important* of the six for the active options trader, because it is the one input where mispricing — and therefore opportunity — most often lives.

### 5. Risk-free rate (r)

A higher interest rate makes a call slightly more valuable and a put slightly less. The intuition: a call lets you defer the cash outlay for the underlying, so you earn interest on the money in the meantime; a put delays the cash you would receive. This effect is small for short-dated options and is usually the least important input in practice — which is why its sensitivity, **rho** (Chapter 14), is the least-watched Greek.

### 6. Dividends / carry (q)

For a single stock, an expected dividend reduces the call's value (the stock price drops by roughly the dividend on the ex-date) and increases the put's. For index options, the analogous factor is the index's dividend yield. This matters most for long-dated single-stock options; for near-dated index options it is typically negligible.

## The point: which inputs you control

The elegant part is *what is fixed versus what you choose*:

- **You choose** the strike (K) and the expiry (T) — that is the entire "which contract?" decision.
- **The market sets** the underlying (S), the rate (r), and dividends (q).
- **Volatility (σ) is the battleground** — the one input everyone is forced to estimate, and therefore the one where skill (or luck) actually shows up.

This is why experienced options traders say they trade *volatility*, not just direction. Direction (the underlying) is one input; volatility is another, and it is the one that separates options from every other instrument.

## From factors to sensitivities

Each factor's influence has a name and a number — the **Greeks**, the partial derivatives of the option price with respect to each input:

- Underlying price → **delta** (and **gamma**, its rate of change).
- Time → **theta**.
- Volatility → **vega**.
- Rate → **rho**.

The next four chapters take each in turn. The mental model to carry forward: *the option price is a smooth function of six inputs, and the Greeks are simply its slopes and curvatures.*

## Summary

- Six inputs determine an option's price: S, K, T, σ, r, q.
- Only volatility must be estimated; it is the battleground of options trading.
- More time and more volatility raise both calls and puts.
- The Greeks are the sensitivities of price to each input — the subject of the next chapters.
