# PRODUCT.md - Yonder

What the product is and what it sells. The rules for *working on* it are in `CLAUDE.md`;
the record of what was built is in `docs/decisions.md`; what is still open is in `docs/backlog.md`.

## Register
product (app UI - design serves the product, not the other way around). Mobile-first web, later responsive desktop. Web3 / blockchain.

## What it is
A mobile-first prediction market where users bet YES / NO on real-world events (Politics, Crypto, Culture, General). Users stake stablecoins (USDC/USDT) on whether an event will happen; you buy shares at the price quoted on screen and a winning share pays $1, so **what changes with timing is the PRICE and not the payout rule**. This sentence said "payout depends on the AMM price when the bet was placed" until 2026-08-19, which the Event resolution section of this same file had replaced on 2026-08-10: a fact written twice in one file is a fact that drifts, and the copy that drifted is the one that is not the owner. Platform team creates and resolves events (MVP).

## Primary job (JTBD)
"When I follow events that matter to me, I want real skin in the game, so it's not just news but my personal stake with a real outcome." Secondary: "If I understand the situation better than others, I want that to convert into money, simply, without the complexity of trading."

**What the job implies for the product:**
- First page = live events happening now, not "sign up"
- Onboarding order: event -> mechanics -> bet, never the reverse
- Retention = notifications about events, not about topping up a balance
- Profile = a prediction track record, read as reputation

## Audience
Age 20-40. Primary persona: **Alex, a News Junkie** - follows events, wants a stake, NOT a trader. Primary driver is **Trust** (the platform must feel credible, transparent, secure). Core documented fear: "this looks like crypto, so it's a scam" - platform betrayal is the #1 churn driver.

## Core differentiator
Clarity and accessibility for newcomers. Competitors (Polymarket, Kalshi, Manifold) feel opaque. This platform makes users always understand what they are doing, why, and what happens next. Browse and form a bet with no wallet upfront; the auth / crypto gate fires at Confirm, not at entry.

## Brand personality
Credible, calm, transparent - a spectator's clarity, not a trader's terminal. High-contrast and alive, not muddy or flat. Energy from contrast + one loud accent, never from casino shine. Trust is stated as one plain provable sentence, never borrowed authority.

## Voice (from voice/docs/voice.md)
Five rules: (1) explain the number, never just show it; (2) one plain sentence of trust before the ask; (3) speak to a spectator with an opinion, not a trader; (4) design the loss, mark the win without lighting a fuse; (5) say the specific provable thing, not a superlative. Lexicon: event (not market), bet (not position), Add funds (not Deposit), Sign in, Confirm bet. Forbidden: "Something went wrong" / "Welcome" / "Congratulations" / "successfully" / exclamations / emoji / apologies / internal codes / motivational tone.

## Anti-references (what this is NOT)
- NOT a trader terminal: no order books, leverage sliders, PNL ranks, ticker walls, gamified loot.
- NOT beige / warm / soft-pastel / AI-cliche palettes.
- NOT low-contrast (the Kalshi complaint) or muddy navy (the rejected Hedgehog look).
- The green/red "wall of YES/NO buttons" trader-floor look is a standing risk to pull back from, not a goal.

## Platform
web (mobile-first, base 360-390px, then responsive desktop).

---

## Market types (MVP)
- **Binary markets** - YES / NO on a single event
- **Multi-outcome markets** - multiple options, each with YES / NO
- **Frequency**, orthogonal to type (added in the wireframe pass) - markets are one-time or recurring (Hourly / Daily / Weekly / Monthly). Powers the feed's cadence filter, **labelled `How often` since 2026-08-14** while the attribute keeps the name Frequency: the model's word and the reader's word are allowed to differ, and `voice/docs/voice.md` principle 3 decides the reader's. See `ia/docs/sitemap.md`, Event entity.
- **Recurring resolution: EVERY CADENCE INSTANCE IS ITS OWN EVENT** (decided 2026-08-10,
  `docs/backlog.md` #11). "BTC above $150k this week" is one event with one window, one price and
  one resolution; next week is a different event. The cadence is a **series** the instances belong
  to, and the Frequency filter filters by the series attribute, not by anything an instance has to
  carry. **Nothing new is entered into the model**: Active Bets, notifications, the win and loss
  screens and the resolution record all keep working on the same Event they already work on. The
  alternative - one long-lived event that resolves repeatedly - would have needed a second kind of
  position, a second kind of notification and a payout rule per cycle.

## Event resolution
- Events are real-world occurrences
- Platform team creates and resolves events (MVP)
- **Payout mechanism: SHARES AT A LOCKED PRICE** (decided 2026-08-10, `docs/backlog.md` #10). You buy
  YES or NO at the price shown on screen and that price is locked at Confirm; a winning share pays
  $1. **Timing matters because the PRICE moves, not because the payout rule computes differently** -
  which is the whole reason the number can be explained in one line, and the reason the Confirm
  reconcile (S5) exists: if the price moved between the panel and Confirm, the person sees the new
  price before they commit. This is the Polymarket and Kalshi model. It replaces "AMM-style dynamic
  pricing, payout depends on when the bet was placed", which was never specified and could not be
  said in a sentence a newcomer would follow.
- If you bet YES and the event does not happen, your shares settle at $0

## Categories
- MVP: Politics, Crypto, Culture, General
- Post-MVP: Sports, and expansion based on interest / demand

## Catalog size
**About 25 events open at once, curated.** Decided 2026-08-17, closing backlog 164, and it is
here because that row could not be settled anywhere else: every question about reachability,
search, paging and the category rail resolves against this number and the repository had never
written one down. At 25 a person can scan the feed and search is a convenience; at 250 search
would be the only way in and the navigation model of `ia/docs/sitemap.md` would need re-deciding.

Two things follow and both are already true in the trees. **Search indexes the OPEN set only** -
a settled market is reached from your own history, never from the field - which is why the
catalog in `assets/search.js` can be kept by hand at this size. And **a market is open or
settled, never both**: the settled examples the product ships are four markets that stand
outside the open set, three of them prior instances of markets it still runs, because a
recurring market settling and reopening is the real shape of this. `docs/decisions.md`
2026-08-17.

## MVP feature scope
Sharpened by the CJM To-Be backlog (`user-research/docs/cjm-to-be.md`, Alex x main job). One list, ordered by the To-Be path. The motivation features (story-led entry, explain the number) are co-equal MVP with the friction fixes, since the riskiest assumption "the barrier is friction, not motivation" was substantially refuted (research section 9, F4).

- Story-led event feed as the first page (live events, not a signup) - the motivation entry
- "Explain the number": plain-language odds + one-line why + the news story, spectator language (not trader)
- Browse and form the bet intent with no wallet upfront; the auth / crypto gate fires at Confirm, not at entry (the core clarity inversion)
- User account via social login (Google, X)
- Fiat on-ramp (card -> stablecoin); a crypto wallet stays available for crypto-native users but is not required until Confirm
- One plain funds-safety line before deposit ("USDC held 1:1, we never lend it") + the fee shown before Confirm
- Confirm with a price reconcile if the price moved (S5)
- Binary YES/NO and multi-outcome markets (multi is product scope, not CJM-derived)
- $1 / $5 bet sizing (low min, $5 default); the size that feels "real but not scary" is a `[?]` to test
- Active Bets + outcome / position notifications (retention anchor)
- Win screen ("You were right") + share, with overconfidence friction; Loss screen ("Here's what happened") with context and a next step that is NOT "bet again"
- Transparent resolution + a resolved-markets count (against the #1 trust killer: platform betrayal)

**Post-MVP / later:** Leaderboard, Staking (TBD) - orphans relative to this CJM; Sports (needs Maria's own CJM).

## Business model
- **Commission per bet, 1.5% OF THE STAKE** (decided 2026-08-10, `docs/backlog.md` #6). Shown as a
  line before Confirm. **The basis is the stake and not the payout**, because a person can check a
  percentage of the number they typed and cannot check a percentage of a number that does not exist
  yet. Benchmark it was chosen against: Kalshi `0.07 x p x (1-p)` = 1.75% of notional at a 50/50
  midpoint, Polymarket 0.8% to 1.8% on crypto and 0.30% flat in the US, Hyperliquid HIP-4 at 0%.
  **What was shipping until this decision was `fee = 0.03 * payout` in the page scripts**, which is
  ~6% of the stake at even odds, about 3.4x the dearest competitor, and nobody had chosen it.
- Spread - possible secondary model
- No subscriptions
- **Bet limits: $1 minimum, no maximum** (decided 2026-08-10, `docs/backlog.md` #7). The minimum
  exists so that the fee line is never absurd against the stake, and $1 is the "try it" size the MVP
  scope already names. The deposit minimum stays $10, which is a few bets of headroom rather than
  one.

## Liquidity and risk
**Who is on the other side of the bet, what that costs, and what it is worth.** Decided 2026-08-19.
This section did not exist until then, and its absence is what let four places in this file go on
saying AMM after the mechanism had been decided elsewhere: **a question nobody owns is a question
every file answers differently.**

**COUNTERPARTY: THE PLATFORM IS THE ONLY MARKET MAKER.** There is no peer to match against. A book
needs two-sided flow and this product has 25 curated events, a $1 minimum, a $5 default and an
audience `Audience` above defines as explicitly not traders; an order book under that load is an
empty book, and a parimutuel pool cannot quote a price before the pool exists, which would break the
locked price the Event resolution section decided and the Win and Loss screens are written on. So the
platform quotes both sides and takes the other side of every bet. **This is the one structural cost
of the model and it is stated rather than hidden**: when a person loses, the house is the winner, and
`voice/docs/voice.md` principle 5 says the provable thing gets said. The published form is the
subsidy cap below, which is a number no order book has.

**THE SCREENS HAD ALREADY DECIDED THE FILL, AND IT IS NOT AN AMM's.** Measured over both trees on
2026-08-19: **18 placements over 18 documents print `shares = stake / price` exactly, 0 of them with
any slippage**, and the sentence under them says the price is locked at Confirm so it cannot move
against you. Every automated market maker fills a bet ALONG its curve, so a $5 bet at 38 cents buys
fewer than 13.16 shares. **The product therefore quotes a price, fills the whole bet at the quote,
and moves the quote between bets.** The curve still exists, as the rule that decides where the quote
goes next; what it does not do is price the bet you are placing.

**THE PARAMETER IS `b`, AND TWO SHIPPED PROMISES PULL IT IN OPPOSITE DIRECTIONS.** Under a logarithmic
market scoring rule, `b` is how much money it takes to move the number. Measured 2026-08-19, from a
50 / 50 book:

| `b` | three $5 bets one side | forty $5 bets one side | worst-case subsidy per binary market, `b x ln 2` |
|---|---|---|---|
| $50 | 63.0% | 99.9% | $34.66 |
| $167 | 54.4% | 85.1% | $115.61 |
| $300 | 52.4% | 71.1% | $207.94 |
| $1,000 | 50.7% | 56.7% | $693.15 |

Small `b` is what makes the number a market: at $1,000 a person betting $5 moves it by a quarter of a
point and the price on screen is the opening quote wearing a crowd's clothes. **But filling at the
quote costs the house the slippage it just gave away, and that cost falls as `b` rises**, so the
locked-price promise wants `b` LARGE and price discovery wants it SMALL. The two cross at a closed
form: at a fee of `f` on the stake, a bet of `S` filled at the quote breaks even at

> **`b = S / (2f)`**, which at `f = 1.5%` is **`b = 33.3 x S`**: $167 for a $5 bet, $833 for a $25
> bet, $3,333 for a $100 bet.

**AND `Bet limits` ABOVE DECIDED THERE IS NO MAXIMUM**, so at any `b` there is a bet size above which
the locked-price promise is sold at a loss, and the product has promised to accept it. That is an
open row rather than a repair: `docs/backlog.md` 216.

**WHAT THE COMMISSION HAS TO CARRY.** At 1.5% of the stake and a $5 bet, one bet earns 7.5 cents.
Computed 2026-08-19:

| to net | stake volume per month | bets of $5 | per day | **per market per day, over 25** |
|---|---|---|---|---|
| $500 | $33,333 | 6,667 | 222 | 8.9 |
| $1,000 | $66,667 | 13,333 | 444 | **17.8** |
| $3,000 | $200,000 | 40,000 | 1,333 | 53.3 |

And to earn back the worst-case subsidy once, at `b = $1,000` across 25 markets ($17,329), takes
**$1,155,245 of stake volume**. **This is the number that decides the launch, and it is arithmetic
rather than an opinion**: the real-money version is not blocked by a licence first, it is blocked by
needing eighteen bets per market every day before it pays one person a salary.

**SO THE FIRST LAUNCH CARRIES NO MONEY, AND THAT IS WHAT MAKES THE MECHANISM FREE.** The only real
cost in everything above is the subsidy, and the subsidy is a number in a table when the currency is
points. **The play-money build is therefore not a smaller product, it is the same product with its
one risk parameter priced at zero**, which is the only condition under which `b` can be LEARNED from
live flow instead of guessed: start it small enough that a person's bet visibly moves the number, and
raise it as flow arrives. Commission is 0 while the currency is points, because a fee on play money
buys nothing and costs the trust line that says what the fee is for. The business model above is what
turns on with real money, not what ships first.

**Launch scope: 7 events, no commission, no chain. The seven are named, with their resolvers, in
`docs/launch-catalog.md`.** The 25 in `Catalog size` is what the navigation model is DESIGNED against
and it stays; 7 is what one person can source, write a resolution rule for, watch, close on time and
resolve without the catalog going stale, which is the failure this product cannot survive because a
late or disputed resolution is the #1 churn driver in `Audience`.

**THIS LINE SAID `one-time only` UNTIL 2026-08-20 AND ITS REASON HAD BEEN REMOVED THE DAY IT WAS
WRITTEN.** The argument was this file's own `Market types` rule, that every cadence instance is its
own event, so five weekly series are 260 resolutions a year. **That is an argument against 260 HAND
resolutions**, and the automation decision taken hours earlier on the same day makes a machine-read
series cost one template and zero. What actually forced the reversal is a second axis the resolver
classification had missed: **2 of the 25 shipped markets resolve within a month and 1 of those is
machine-resolvable**, so a launch built from the shipped catalog alone gives a reader one resolution
in the first month and then a gap, and a resolution is this product's only trust event and its only
notification. **Recurring is in, on one condition: a recurring market must be machine-resolved.** A
hand-resolved series is the newsroom the whole exercise exists to avoid.

**Jurisdiction: `[?]`.** `Financials and compliance` below says global with geo-restrictions, which
names who is kept out and not what the product operates under. A points product with no deposit, no
withdrawal and no cash redemption is the one form of this that needs no answer, and the answer is
required before the first real dollar, not before the first user. *Not legal advice.*

## Financials and compliance
- **All transactions in crypto** - stablecoins (USDC, USDT) as primary
- Fiat on-ramp supported (user converts fiat -> crypto on platform)
- **KYC: on the fiat rail only** (decided 2026-08-10, `docs/backlog.md` #8). Required for card
  deposits, where the on-ramp provider performs it anyway; **a crypto-only user is never asked**.
  This is what Polymarket does, and it is what keeps the product's core inversion intact: the wallet
  and the verification are not conditions of browsing or of forming a bet intent, they arrive at
  Confirm. Geo-restrictions are unchanged and are the other half of compliance. *A compliance
  decision with a legal component: this is the design default, and it is not legal advice.*
- **Geo**: global, with geo-restrictions per regulatory requirements (no US for real-money prediction markets)

## Tech stack
**The v1 build is specified in `docs/build-plan.md`**: Astro over the existing tree, Supabase for
Postgres, Google and X sign-in and the resolver job, Cloudflare Pages, **$0 a month to start and $25
when the database has to stop pausing**. The rows below are the REAL-MONEY product and they turn on
with it, not before. This heading said `(TBD)` until 2026-08-20.

- Frontend: web (mobile-first)
- **Blockchain: Base** (decided 2026-08-10, `docs/backlog.md` #9). Chosen on the three things this
  product actually needs from a chain: **native USDC issued by Circle** rather than a bridged
  representation, which matters when the funds-safety line says "held 1:1"; **L2 fees low enough
  that a $1 bet is not eaten by gas**, which is the minimum decided in #7; and **the shortest fiat
  on-ramp**, since the card path is Coinbase's own and the MVP scope puts a fiat on-ramp in the
  first release. Polygon is the proven alternative and is what Polymarket runs on, but its USDC is
  bridged; Ethereum mainnet is out on fees alone at a $1 minimum.
- Wallet connection: WalletConnect / MetaMask + social login
- **Pricing and counterparty: see Liquidity and risk below.** This line said "Smart contracts: AMM-based market resolution" until 2026-08-19 and it was wrong in two ways at once: resolution is not what an AMM does, and **the arithmetic the screens print is not an AMM's**. Measured over both trees on 2026-08-19: **18 placements over 18 documents compute `shares = stake / price` to the cent and 0 of them carry any slippage**, beside a line that says the price cannot move against you between the panel and the bet. An AMM fills a bet along a curve; these screens fill it at the quote

## Timeline and team
Solo: product, design and development. **~3 months was the estimate for `MVP feature scope` above, and
that scope is not what ships first.** Measured 2026-08-19: the repository holds 509 commits, 115
painted documents, 114 grey, 61 kit pages, 49 components, and **0 lines of product code**. Against the
launch scope in `Liquidity and risk` (7 one-time events, points, no chain, no fiat rail, no KYC, and a
slice of feed, event detail, sign-in, balance, confirm, my bets and one admin page) the estimate holds
at roughly 8 to 12 weeks of evenings. Against the full list above it does not, and the difference is
every line of that list that touches a wallet, a chain, a fiat rail or a regulator. The stage that
would own this does not exist in the README table: `docs/backlog.md` 218.

## Competitors
Full comparison in `research/docs/competitors.md` (HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, open questions); the trust benchmark in `research/docs/benchmark.md`. Short version: Polymarket (**CLOB on Polygon**, good mobile UX, 3-level nav complex for newcomers), Kalshi (US-regulated, fiat, order book), Manifold (play money, social), Metaculus (forecasting community, no real money). **This line called Polymarket an AMM until 2026-08-19 while `research/docs/competitors.md` said CLOB on Polygon in four places**: the research was right and the summary was the copy that drifted, which is the same shape as the What it is line above. Polymarket left its AMM for a central limit order book in late 2022.
