# 2. The Greeks That Drive Adjustments

The Greeks describe how an option's price responds to its inputs. You do not need to compute them — you need to know what each one *means* for a position, because every adjustment in this book is a deliberate change to one of these exposures.

| Greek | Measures | What it means for you |
|---|---|---|
| **Delta** | Change in option price per 1-point move in the underlying | Directional exposure; ~+1 for a deep in-the-money call, ~−1 for a deep in-the-money put, ~±0.5 at-the-money |
| **Gamma** | Rate of change of delta | How *fast* your directional exposure changes as the market moves — highest at-the-money and near expiry |
| **Theta** | Change in price per day of time passing | Time decay; **positive** for option sellers, negative for buyers |
| **Vega** | Change in price per 1% change in implied volatility | Volatility exposure; short options are **short vega** (hurt by rising IV), long options are long vega |

**How to read a position through the Greeks:**

- A **short strangle / iron condor** is *short gamma and short vega, long theta*. It profits from time passing and calm; it loses when the market moves fast or volatility spikes. Adjustments to these strategies are usually about **managing the directional (delta) drift** after a move.
- A **long straddle** is *long gamma and long vega, short theta*. It profits from a big move or a volatility pop; it bleeds time. Its "adjustment" is usually *not* to hold it too long.
- A **covered call** is net long delta (the stock) with positive theta from the short call; it is a *reduce-upside, add-income* trade.
- A **bull call spread** is long delta with a defined risk; its adjustment is about *locking in* or *rolling up* when the view proves right.
