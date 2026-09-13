# 13. Vega: The Price of Volatility

## The Greek most traders actually trade

**Vega (ν)** measures how much an option's price changes for a **one-percentage-point change in implied volatility**. If all the other Greeks describe how an option responds to the market's *direction* and the *clock*, vega describes how it responds to the market's *fear and uncertainty*.

Vega is the same sign for **both calls and puts**: higher volatility makes *all* options more valuable (Chapter 10). A vega of 0.20 means the option gains ₹0.20 per unit for every 1-point rise in implied volatility.

Because volatility is the one input every market participant must estimate, and because it changes meaningfully and often, **vega is the Greek that separates options from every other instrument** — and the one most active options traders are actually trading, whether they realise it or not.

## Where vega is strongest

- **ATM options have the highest vega.** At the money is where a change in the expected size of future moves matters most to the price.
- **OTM and ITM options have lower vega**, declining as you move away from the money — though OTM options still have meaningful vega because their entire value is "possibility."
- **Longer-dated options have higher vega than short-dated ones.** More time means more opportunity for a volatility change to compound. This is a √time relationship again: vega scales with the square root of time.

## Vega for buyers vs. sellers

- A **buyer is long vega**: if volatility rises, the option is worth more (a welcome windfall even if the underlying does not move).
- A **seller is short vega**: if volatility rises, the option they sold is worth more, and their short position loses.

This is why buying an option before a known event (an election, a budget, a Fed decision, an earnings release) can lose money *even if the underlying moves the "right" way*: implied volatility is typically **elevated before the event** and **collapses after it** (a "volatility crush"). The buyer overpays for vega-rich options, and after the event the vega deflates, dragging the option's price down even as the underlying moves. The buyer needs the move to be *bigger than the market already priced in*.

Conversely, a seller before an event collects high premium precisely *because* volatility is elevated — but takes on the risk that the move is larger than priced.

## Volatility crush and vol expansion

Two vega scenarios every trader should recognise:

1. **Volatility crush (post-event):** implied vol falls back toward normal after a scheduled event. Long-option holders suffer; short-option holders benefit. This is one of the most reliable, recurring vega effects.
2. **Volatility expansion (a shock):** an unexpected shock (a crash, a policy surprise) sends implied vol sharply higher. Long-option holders gain rapidly (this is what makes long puts and long straddles excellent "tail" hedges); short-option holders are hurt badly and quickly.

The asymmetry matters: vol tends to *fall* gradually and *spike* suddenly. This is why short-vol positions can be profitable for long stretches and then lose everything in a day — the classic "short vol" tail risk.

## Vega and the strategy choice

- **Directional traders** should know the vega of their position, because an adverse vol move can overwhelm a correct directional read.
- **Volatility traders** (Chapter 25) make vega the *point*: they buy options when volatility is cheap (low vega, low IV) and sell when it is expensive (high vega, high IV), often while neutralising delta to isolate the vol bet.
- **Spread traders** should know that debit spreads and credit spreads have *opposite* vega: a debit spread (paying premium) is typically net long vega; a credit spread (collecting premium) is net short vega — so the same directional view can carry very different vol exposure depending on how you express it.

## A caution: vega and implied vol are circular

Vega is the sensitivity *to implied volatility*, but implied volatility itself is the number that makes the model price match the market price (Chapter 16). So "vega" is really "how much the price moves when the market's vol estimate moves." It is a useful, practical measure — but it inherits whatever is uncertain about the IV estimate itself. Treat vega as a robust *relative* guide ("this position has more vol risk than that one") rather than a precise forecast.

## Practical rules of thumb

- Want to be insulated from vol swings? Trade near expiry (low vega) or hedge with an offsetting vol position.
- Want pure vol exposure? Trade ATM, longer-dated options (high vega).
- Check vega before any scheduled event — it will dominate the trade's behaviour over the next day.
- If you are long options, be wary of buying into elevated IV before a binary event (crush risk).

## Summary

- Vega = sensitivity to a 1-point change in implied volatility; positive for both calls and puts.
- Highest at ATM and in longer-dated options.
- Buyers are long vega; sellers are short vega.
- Volatility crushes after events and spikes on shocks — recognise both.
- Most "options traders" are really trading vega.

Next: rho and the minor Greeks, completing the Greek alphabet.
