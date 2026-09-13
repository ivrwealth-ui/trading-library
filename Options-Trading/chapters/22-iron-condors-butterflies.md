# 22. Iron Condors and Butterflies

## Defined-risk range trades

A short straddle profits from stillness but has unbounded risk. The **iron condor** and the **butterfly** deliver the same "range" thesis with the risk *capped* — they are the disciplined way to sell volatility.

## The iron condor

- **Structure:** a four-legged position combining a **bull put spread** (below) and a **bear call spread** (above). Equivalently: sell an OTM put (K₁), buy a further OTM put (K₀), sell an OTM call (K₃), buy a further OTM call (K₄) — all same expiry.
- **View:** the market will stay **within a range** (between K₁ and K₃) until expiry.
- **Maximum profit:** the net credit received (both spreads' credits combined), realised if the underlying closes between the two *short* strikes (K₁ and K₃).
- **Maximum loss:** the width of one side minus the net credit — because at worst, only *one* of the two spreads is fully against you (the market cannot be simultaneously far above and far below).
- **Breakevens:** two — K₁ − net credit, and K₃ + net credit.
- **Greeks:** short vega, short gamma (from the two short options), net long theta — but all **bounded**.

### Example

NIFTY at 25,000. Sell the 24,800 put for ₹90, buy the 24,600 put for ₹40 (bull put spread, credit ₹50). Sell the 25,200 call for ₹80, buy the 25,400 call for ₹30 (bear call spread, credit ₹50). Net credit = ₹100.

- Maximum profit = **₹100** (NIFTY between 24,800 and 25,200).
- Maximum loss = (200 − 100) = **₹100** (one side fully breached; width of one side is 200).
- Breakevens: **24,700** and **25,300**.

Notice the elegance: the max loss equals the max profit here because each side is 200 wide and the total credit is ₹100 — the loss is capped at exactly one side's width minus the total credit.

## The butterfly

- **Structure:** buy one option at a low strike, **sell two** at a middle strike, buy one at a high strike — same type (calls or puts), same expiry, with the strikes equally spaced. (A "long call butterfly": buy 24,900 call, sell two 25,000 calls, buy 25,100 call.)
- **View:** the market will finish **at (or very near) the middle strike** — a precise, "pin" forecast.
- **Maximum profit:** the distance between strikes minus the net debit, achieved *exactly* at the middle strike.
- **Maximum loss:** the small net debit paid — defined and modest.
- **Breakevens:** two, just inside the outer strikes.
- **Greeks:** near-zero net delta (it is a *tight range* bet), short gamma overall (it profits from stillness at one point), long vega at the wings.

### Example (call butterfly, 100-point wings)

NIFTY at 25,000. Buy 24,900 call (₹180), sell two 25,000 calls (₹130 each = ₹260), buy 25,100 call (₹90). Net debit = 180 + 90 − 260 = **₹10**.

- Maximum profit = 100 − 10 = **₹90**, if NIFTY expires exactly at 25,000.
- Maximum loss = **₹10** (the net debit), if NIFTY is far from 25,000.
- Breakevens: 24,910 and 25,090.

The butterfly is a "low cost, precise target" trade: you risk a tiny amount for a specific payoff only if the market lands in a narrow zone. Its cheapness and small risk make it a popular way to express a precise level with a very favourable risk-reward *when it works* — but it demands a *specific* forecast.

## Condor vs. butterfly

| | Iron condor | Butterfly |
|---|---|---|
| Legs | 4 (calls + puts) | 3 (calls or puts) |
| Thesis | Range (stay inside) | Pin (land at one price) |
| Profit zone | Wide plateau between short strikes | Narrow peak at the middle strike |
| Max loss | Width − credit | Net debit |
| Vega | Short | Mixed (long wings) |

The iron condor is the **range** trade — comfortable if the market stays anywhere in a band. The butterfly is the **pin** trade — rewards a precise landing. Condors are wider and more forgiving; butterflies are tighter and cheaper.

## Why these are the "disciplined" short-vol trades

Both convert the naked short-vol bet (short straddle/strangle) into something with a **known, capped maximum loss**:

- The **iron condor** caps the loss by buying the wing options (K₀ and K₄) that would otherwise leave the loss unbounded.
- The **butterfly** caps the loss structurally — you own the outer options.

This is the single most important upgrade a short-volatility trader makes: *trade the range, but always buy the tail.* The cost is a slightly reduced credit (or a small debit), and the reward is that no single gap or spike can produce a catastrophic loss.

## The realistic caveat

Defined-risk does not mean *safe*. An iron condor still loses its maximum when the market gaps through one side — and because the profit is small and the loss can be several times larger (depending on width and credit), the *win rate* must be high to compensate. This is the same "pennies in front of a steamroller" arithmetic as naked selling, merely with the steamroller's damage capped. Risk management (Chapter 28) — sizing, and rules for cutting a breached side — remains essential.

## Summary

- Iron condor: bull put spread + bear call spread; range thesis; risk capped at width − credit.
- Butterfly: 1-2-1 strike structure; pin thesis; small debit, precise payoff.
- Both convert short-vol into defined-risk.
- Defined-risk ≠ safe: small frequent wins must outweigh occasional max losses.

Next: ratio, calendar, and diagonal spreads — trading time and relative volatility.
