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
- **Frequency**, orthogonal to type (added in the wireframe pass) - markets are one-time or recurring (Hourly / Daily / Weekly / Monthly). Powers the Frequency filter on the Event Feed. See `ia/docs/sitemap.md`, Event entity. *Resolution mechanics for recurring markets are still unwritten - `docs/backlog.md` #11.*

## Event resolution
- Events are real-world occurrences
- Platform team creates and resolves events (MVP)
- Resolution mechanism: AMM-style dynamic pricing - payout depends on *when* the bet was placed, not just the outcome
- If you bet YES and the event does not happen you lose (partial loss based on the timing of the stake)

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
- **Commission per bet** (primary) - exact % TBD, needs competitive research (`docs/backlog.md` #6)
- Spread - possible secondary model
- No subscriptions
- No min/max bet limits at launch (Polymarket uses a $0.01 minimum - `docs/backlog.md` #7)

## Financials and compliance
- **All transactions in crypto** - stablecoins (USDC, USDT) as primary
- Fiat on-ramp supported (user converts fiat -> crypto on platform)
- **KYC**: required for fiat deposits; crypto-only users TBD (Polymarket operates without KYC for crypto)
- **Geo**: global, with geo-restrictions per regulatory requirements (no US for real-money prediction markets)

## Tech stack (TBD)
- Frontend: web (mobile-first)
- Blockchain: Web3, specific chain TBD (likely Polygon, Base or Arbitrum for low fees - `docs/backlog.md` #9)
- Wallet connection: WalletConnect / MetaMask + social login
- Smart contracts: AMM-based market resolution

## Timeline and team
~3 months to MVP. Solo - product, design and development.

## Competitors
Full comparison in `research/docs/competitors.md` (HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, open questions); the trust benchmark in `research/docs/benchmark.md`. Short version: Polymarket (AMM, good mobile UX, 3-level nav complex for newcomers), Kalshi (US-regulated, fiat), Manifold (play money, social), Metaculus (forecasting community, no real money).
