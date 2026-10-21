# Appendix C — Example Screens

## C.1 Value screen (ex-financials)

```
P/E (TTM)              < 15
P/B                    < 1.5
Net Debt/EBITDA        < 2
ROE (5-yr avg)         > 10%
Operating CF           positive 3 yrs
Promoter pledge        < 20%
→ rank by EV/EBITDA ascending, take top 20
```

## C.2 Financials (banks/NBFCs) value screen

```
P/B                    < 1.5  (PSU)  /  < 2.5 (private)
ROA                    > 1.0%
ROE                    > 12%
Gross NPA trend        stable or falling
Capital adequacy       > regulatory floor
→ rank by P/B ascending
```

## C.3 Momentum screen

```
12-1 total return      > 0
Price                  > 200-DMA
Price / 52w-high       > 0.85
Avg daily turnover     > ₹10 cr
Exclude                < 12 months listed, circuit-stuck
→ rank by 12-1 return descending, take top 20, monthly
```

## C.4 Multi-factor screen

```
z_value      = z(earnings yield) + z(book-to-price)
z_momentum   = z(12-1 return)
z_quality    = z(ROE 5y) − z(Net Debt/EBITDA; ex-banks/NBFCs) − z(gross-margin volatility)
z_lowvol     = −z(1y realized vol)
composite    = 0.30*z_value + 0.30*z_momentum + 0.25*z_quality + 0.15*z_lowvol
→ rank composite descending, top 25–30, quarterly, sector cap 20%
```
