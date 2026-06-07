# Competitive Research

## Competitor Groups

### Group 1 — Hard (same product, same audience, same market)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Polymarket** | Crypto PM, global, USDC/Polygon | Largest crypto prediction market, closest competitor | Bet UX, onboarding, navigation |
| 2 | **Futuur** | Crypto + fiat, global | Hybrid model, global scope, similar to our concept | Fiat on-ramp, multi-outcome UI, probability bars |
| 3 | **Azuro** | Decentralized protocol, Web3 | Fully Web3, no central operator | Market architecture, liquidity UX |
| 4 | **Zeitgeist** | Polkadot-based PM | Active Web3 PM, new market mechanics | Resolution UI, complex market display |
| 5 | **Hedgehog** | Newer crypto PM | Cleaner design, similar positioning | New user onboarding into Web3 PM |

### Group 2 — Soft (different product, same JTBD)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Bet365 / 1xBet** | Traditional sports betting | Mass market betting, same impulse | Odds explanation, live mode, engagement |
| 2 | **Betfair Exchange** | P2P betting exchange | Similar peer mechanics to AMM | How they show liquidity and opposing bets |
| 3 | **dYdX / Hyperliquid** | Crypto derivatives | Same audience, same motive (predict & earn) | Trust UI, wallet UX, risk explanation |
| 4 | **DraftKings** | Fantasy sports + betting | Legal betting with big UX budget | Leaderboard, retention, gamification |
| 5 | **Metaculus** | Forecasting community (no money) | Same psychology without stakes | Non-monetary motivation: reputation, accuracy |

### Group 3 — Aspirational (international benchmarks)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Kalshi** | CFTC-regulated, fiat, US | Gold standard for trust and compliance | Trust signals, regulated disclaimers, clean signup |
| 2 | **Manifold Markets** | Play money, user-created | Best UX for market creation and social layer | User-created events, discussion layer |
| 3 | **PredictIt** | Regulated, political markets | Long-standing, verified resolution mechanics | Resolution transparency, rule clarity |
| 4 | **Good Judgment Open** | Professional forecasting | Best-in-class event formulation | How to write clear, unambiguous resolution criteria |
| 5 | **Robinhood** | Fintech / investing | Best "democratized finance" onboarding | New user clarity, risk explanation, first experience |

---

## Screens Captured

| File | What it shows |
|---|---|
| `polymarket-home-mobile.png` | Home feed — categories, market cards, YES/NO buttons |
| `polymarket-home-scroll-mobile.png` | Scrolled home — live sports markets |
| `polymarket-event-detail-mobile.png` | Multi-outcome event — chart, odds, volume |
| `polymarket-event-bet-mobile.png` | Bet interface — Buy Yes/No per outcome with ¢ prices |
| `polymarket-signup-mobile.png` | Sign Up — bottom sheet, Google + 8 wallet options |
| `kalshi-home-mobile.png` | Home + auto-shown signup modal |
| `kalshi-home-browse-mobile.png` | Home after dismiss — LIVE event hero card |
| `manifold-home-mobile.png` | Home — dense list, community questions |
| `futuur-home-mobile.png` | Home — multi-outcome with probability bars |

---

## Key Findings

### Navigation patterns

| Platform | Mobile nav | Category nav |
|---|---|---|
| Polymarket | Bottom 4 tabs (Home, Search, Breaking, More) | Horizontal scroll tabs top (Trending, Breaking, New, Politics…) + topic chips |
| Kalshi | Bottom 4 tabs (Browse, Live 47, Search, Ideas) | Horizontal top (Trending, Elections, Politics, Sports, Culture) |
| Manifold | Bottom 5 tabs (Browse, Prize, Explore, About, Sign in) | Top categories + filter chips (Best, Hot, New) |
| Futuur | Bottom 3 tabs (Markets, Search, Leaderboard) | Top (Trending, New, All) + topic chips |

**Insight:** Polymarket and Kalshi both use 4-tab bottom nav. Futuur's 3-tab is cleanest. All use horizontal category scroll at top.

---

### Signup flows

| Platform | Options | First screen |
|---|---|---|
| Polymarket | Google + Email + 8 wallet/social options | Bottom sheet on demand |
| Kalshi | Google + Apple + Email | Auto-modal on page load |
| Manifold | Google + Email | On navigate to sign in |
| Futuur | Register button → separate page | Requires navigation |

**Insight:** Kalshi's signup is the cleanest (3 clear options). Polymarket's 8+ wallet icons is confusing for newcomers — mixing social login with Web3 wallets creates cognitive overload.

---

### Market card patterns

| Platform | Binary markets | Multi-outcome |
|---|---|---|
| Polymarket | YES/NO pill buttons with % | Separate YES/NO per outcome, price in ¢ |
| Kalshi | % pill badge, click to bet | List of outcomes with % badges |
| Manifold | Progress bar + % + "Bet" button | Same bar pattern |
| Futuur | Progress bars per outcome | Visual bars with % — best multi-outcome UI |

**Insight:** Futuur's probability bars for multi-outcome are the clearest visual approach. Polymarket's cent-based pricing (Buy Yes 37¢) is accurate but abstract for new users.

---

### What's missing across all competitors

1. **No clear "why this number?" explanation** — odds show % or ¢ but never explain WHY that's the market price or what drives changes
2. **Weak onboarding for new users** — no guided first bet, no explanation of CLOB/AMM mechanics inline
3. **No narrative around events** — markets exist as isolated questions, not connected to news context
4. **Trust signals are buried** — resolution rules, dispute processes exist but are hard to find
5. **Portfolio clarity is poor** — understanding your P&L, position, and potential payout is complex

---

## Our Differentiators (confirmed after research)

Based on JTBD (J2 primary: engaged spectator with skin in the game):

1. **Events as stories, not just questions** — each market connected to live news context
2. **Transparent mechanics inline** — explain why odds move, how CLOB pricing works, right on the market page
3. **Guided first experience** — walk new user through first bet with real money context
4. **Cleaner signup than Polymarket** — 3 options max (Google, Apple, Wallet). Separate social from Web3 onboarding
5. **Clearer payout display** — show "if YES wins, you get $X" not just abstract ¢ prices

---

## Open Questions (still to research)

- [ ] Commission rates: Polymarket takes ~2% fee on winnings — verify and benchmark others
- [ ] Minimum bet: Polymarket $0.01 — what's the sweet spot for UX?
- [ ] KYC thresholds: at what deposit amount does KYC trigger?
- [ ] Blockchain/chain: Polymarket uses Polygon (low fees). Base and Arbitrum also viable
- [ ] AMM mechanism: LMSR vs CPMM — which to implement?
- [ ] Fiat on-ramp providers: MoonPay, Transak, Stripe (crypto) — pricing and UX comparison needed
- [ ] Futuur's crypto + fiat hybrid — how exactly do they handle currency switching?
