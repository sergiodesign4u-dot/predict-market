# PRODUCT.md - Predict Market

What the product is and what it sells. The rules for *working on* it are in `CLAUDE.md`;
the record of what was built is in `docs/decisions.md`; what is still open is in `docs/backlog.md`.

## Register
product (app UI - design serves the product, not the other way around). Mobile-first web, later responsive desktop. Web3 / blockchain.

## What it is
A mobile-first prediction market where users bet YES / NO on real-world events (Politics, Crypto, Culture, General). Users stake stablecoins (USDC/USDT) on whether an event will happen; payout depends on the AMM price when the bet was placed, not only the outcome. Platform team creates and resolves events (MVP).

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
- **Frequency**, orthogonal to type (added in the wireframe pass) - markets are one-time or recurring (Hourly / Daily / Weekly / Monthly). Powers the Frequency filter on the Event Feed. See `ia/docs/sitemap.md`, Event entity.
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

## MVP feature scope
Sharpened by the CJM To-Be backlog (`user-research/docs/cjm-to-be.md`, Alex x main job). One list, ordered by the To-Be path. The motivation features (story-led entry, explain the number) are co-equal MVP with the friction fixes, since the riskiest assumption "the barrier is friction, not motivation" was substantially refuted (research section 9, F4).

- Story-led event feed as the first page (live events, not a signup) - the motivation entry
- "Explain the number": plain-language odds + one-line why + the news story, spectator language (not trader)
- Browse and form the bet intent with no wallet upfront; the auth / crypto gate fires at Confirm, not at entry (the core clarity inversion)
- User account via social login (Google, X)
- Fiat on-ramp (card -> stablecoin); a crypto wallet stays available for crypto-native users but is not required until Confirm
- One plain funds-safety line before deposit ("USDC held 1:1, we never lend it") + the fee shown before Confirm
- Confirm with AMM price reconcile if the price moved (S5)
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

## Tech stack (TBD)
- Frontend: web (mobile-first)
- **Blockchain: Base** (decided 2026-08-10, `docs/backlog.md` #9). Chosen on the three things this
  product actually needs from a chain: **native USDC issued by Circle** rather than a bridged
  representation, which matters when the funds-safety line says "held 1:1"; **L2 fees low enough
  that a $1 bet is not eaten by gas**, which is the minimum decided in #7; and **the shortest fiat
  on-ramp**, since the card path is Coinbase's own and the MVP scope puts a fiat on-ramp in the
  first release. Polygon is the proven alternative and is what Polymarket runs on, but its USDC is
  bridged; Ethereum mainnet is out on fees alone at a $1 minimum.
- Wallet connection: WalletConnect / MetaMask + social login
- Smart contracts: AMM-based market resolution

## Timeline and team
~3 months to MVP. Solo - product, design and development.

## Competitors
Full comparison in `research/docs/competitors.md` (HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, open questions); the trust benchmark in `research/docs/benchmark.md`. Short version: Polymarket (AMM, good mobile UX, 3-level nav complex for newcomers), Kalshi (US-regulated, fiat), Manifold (play money, social), Metaculus (forecasting community, no real money).
