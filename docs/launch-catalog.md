# Launch catalog - the seven markets the first release opens with

**This file is not loaded into a session.** `PRODUCT.md` says what the product IS and fixes the
catalog size at about 25 open at once; this says which markets the FIRST release actually opens,
and it carries the machine contract for each one. It is an operating document: it changes when a
market closes and another opens, and it is the only place a resolver is written down.

**It is not a cut of the product.** The 25 in `ia/docs/sitemap.md` and in both screen trees are the
designed catalog and they stay. This is the subset one person can run on day one, in the same way
`PRODUCT.md`'s Liquidity and risk says the business model is what turns ON with real money rather
than what ships first.

Decided 2026-08-20, closing `docs/backlog.md` 219. The reasoning is in `docs/decisions.md`, same date.

---

## The rule that picks them

**A market is not created without a resolver** (`ia/docs/sitemap.md`, Event entity, 2026-08-19):
`source`, `query`, `test`. `manual` is legal and has to be typed.

**And a launch catalog has a second axis the classification missed: HORIZON.** Measured over the 25
shipped questions on 2026-08-20: **2 of 25 resolve within a month and 1 of those two is
machine-resolvable.** Everything else is six weeks or more, and eleven are longer than six months.
So a launch built only from the shipped catalog gives a reader **one resolution in the first month
and then a gap**, and a resolution is this product's only trust event and its only notification.
`PRODUCT.md` says retention is a notification about the event you bet on; with nothing resolving
there is nothing to notify. **The catalog was written to be interesting to read, and a launch
catalog has to be interesting to WAIT for.**

## What that overturns, and it is a rule written the day before

`PRODUCT.md` said on 2026-08-19 that the first release is **one-time markets only**, on the ground
that every cadence instance is its own event (`docs/backlog.md` 11), so five weekly series are 260
resolutions a year. **That argument was written against HAND resolution and the automation decision
of the same day removes it**: a machine-resolved weekly series costs one template and zero manual
resolutions a year. The two decisions were taken hours apart and only one of them was true by the
end of the day. **Recurring is in, on one condition: a recurring market must be machine-resolved.**
A hand-resolved series is the newsroom the whole exercise exists to avoid.

---

## The seven

Four recurring series give the product a heartbeat; three one-time markets give it depth. **Six are
machine-resolved and one is editorial**, which is the ratio the automation pass proposed before the
catalog was measured.

| # | Market | Cadence | Resolver: source / query / test | First resolution |
|---|---|---|---|---|
| 1 | Will Bitcoin close above **$T** this week? | Weekly | CoinGecko or Binance / daily close, BTC-USD, Friday 16:00 ET / `close > T` | end of week 1 |
| 2 | Will Ethereum close above **$T** this week? | Weekly | CoinGecko or Binance / daily close, ETH-USD, Friday 16:00 ET / `close > T` | end of week 1 |
| 3 | Will a new monthly global temperature record be set in **{month}**? | Monthly | Copernicus ERA5 or NOAA NCEI / monthly global mean anomaly / `value > max(all prior same-month values)` | ~the 8th of the next month |
| 4 | Which chain holds the largest stablecoin supply at the end of **{month}**? | Monthly, **multi** | DefiLlama / stablecoin supply by chain at 00:00 UTC on the 1st / `argmax(supply)` | month end |
| 5 | Will Bitcoin close above $150,000 before October 1, 2026? | One-time | CoinGecko or Binance / any daily close in the window / `max(close) > 150000` | Oct 1, 2026 |
| 6 | Will a Category 5 hurricane form in the Atlantic during the 2026 season? | One-time | NOAA National Hurricane Center / storm classifications in the 2026 Atlantic season / `any(category == 5)` | Nov 30, 2026 |
| 7 | Will the US government shut down before March 1, 2027? | One-time | **`manual`.** OMB notices, read by a person / a funding gap beginning before 00:00 ET Mar 1 2027 | Mar 1, 2027 |

**Rows 5, 6 and 7 are taken from the shipped catalog unchanged**, so the trees, the search index and
the fixtures already describe them. Rows 1 to 4 are instances a template creates; row 4 is
deliberately the **multi** one, because the outcome family gained its multi half on 2026-08-20 and a
face with no placement is what this repository keeps paying for.

## The threshold is solved, not chosen

For rows 1, 2 and 5 the number in the question is not an opinion. The generator takes the spot price
and the realised volatility and solves for the strike that opens the market near 50 per cent:

> `K = S x exp(-o^2 T / 2)`

At a spot of $110,000, 60 per cent annualised volatility and a 90-day horizon that is **4.3 per cent
below spot**, and the band that keeps a market worth betting at all, roughly 20 to 80 per cent, runs
from **25.6 per cent below spot to 22.9 per cent above**. `docs/decisions.md` 2026-08-19.

## What is deliberately not here

- **The other 18 shipped markets.** Fourteen are `manual` and most are long-dated; they open as the
  operator has capacity, and each one is a decision rather than a default.
- **A second editorial market.** One is what a person can watch, write and defend. The number is a
  capacity statement and it is the one figure in this file worth arguing about.
- **Sports.** `PRODUCT.md` puts it post-MVP and nothing here changes that.

## Open

- **`b` per market.** `PRODUCT.md`, Liquidity and risk: it is free while the currency is points, and
  it should start small enough that a $5 bet visibly moves the number and rise with flow.
- **What a recurring series looks like in the feed.** The Frequency filter offers One-time, Hourly,
  Daily, Weekly and Monthly, and **20 of 20 frequency words in the painted tree say One-time**, with
  no cadence attribute on any card. Four of the five values match nothing the product draws.
  `docs/backlog.md` 224.
