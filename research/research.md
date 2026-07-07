# Competitive Research

> Note: Competitor groupings in this file are the original v1 draft. The authoritative, updated three-group structure (HARD / SOFT / ASPIRATIONAL) with full analysis and screens is in [competitive-analysis.md](./competitive-analysis.md) (v_refresh June 2026). The raw findings below (navigation patterns, signup flows, market card patterns) remain valid.

## Competitor Groups (v1 - superseded by competitive-analysis.md)

### Group 1 - Hard (same product, same audience, same market)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Polymarket** | Crypto PM, global, USDC/Polygon | Largest crypto prediction market, closest competitor | Bet UX, onboarding, navigation |
| 2 | **Futuur** | Crypto + fiat, global | Hybrid model, global scope, similar to our concept | Fiat on-ramp, multi-outcome UI, probability bars |
| 3 | **Azuro** | Decentralized protocol, Web3 | Fully Web3, no central operator | Market architecture, liquidity UX |
| ~~4~~ | ~~Zeitgeist~~ | ~~Polkadot-based PM~~ | Low activity, low relevance | Removed |
| ~~5~~ | ~~Hedgehog~~ | ~~Newer crypto PM~~ | Closed 2024, irrelevant | Removed |

### Group 2 - Soft (different product, same JTBD)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Bet365** | Traditional sports betting | Mass market betting, same JTBD | Odds explanation, live mode, trust signals, brand |
| 2 | **Betfair Predicts** | P2P exchange + prediction market wrapper (beta Apr 2026) | Converging on our format | Yes/No UI on exchange liquidity |
| 3 | **eToro** | Social copy trading | Same "follow smart money" JTBD | CopyTrader, social proof, trust |
| ~~4~~ | ~~dYdX / Hyperliquid~~ | ~~Crypto derivatives~~ | Different JTBD (leverage trading, not events) | Removed |
| 5 | **DraftKings DFS** | Daily fantasy sports | Skill-based real-money, same engagement loop | Onboarding, retention |

### Group 3 - Aspirational (international benchmarks)
| # | Name | Type | Why here | What to study |
|---|---|---|---|---|
| 1 | **Revolut** | Mobile fintech, 50M+ users | Best trust UX in mobile fintech | Trust signals, funds protection copy, onboarding |
| 2 | **Coinbase** | Crypto exchange, Nasdaq listed | Best crypto onboarding for mainstream | "1:1 assets" promise, educational layer |
| 3 | **Robinhood** | Investing app, $100B valuation | Best "democratized finance" onboarding | 4-screen "swipeys," fee transparency, first experience |
| ~~4~~ | ~~PredictIt~~ | ~~Regulated political markets~~ | US-only, shut down 2023 | Removed |
| ~~5~~ | ~~Good Judgment Open~~ | ~~Professional forecasting~~ | No product UX to study | Removed |

---

## Screens Captured

| File | What it shows |
|---|---|
| `polymarket-home-mobile.png` | Home feed - categories, market cards, YES/NO buttons |
| `polymarket-home-scroll-mobile.png` | Scrolled home - live sports markets |
| `polymarket-event-detail-mobile.png` | Multi-outcome event - chart, odds, volume |
| `polymarket-event-bet-mobile.png` | Bet interface - Buy Yes/No per outcome with ¢ prices |
| `polymarket-signup-mobile.png` | Sign Up - bottom sheet, Google + 8 wallet options |
| `kalshi-home-mobile.png` | Home + auto-shown signup modal |
| `kalshi-home-browse-mobile.png` | Home after dismiss - LIVE event hero card |
| `manifold-home-mobile.png` | Home - dense list, community questions |
| `futuur-home-mobile.png` | Home - multi-outcome with probability bars |

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

**Insight:** Kalshi's signup is the cleanest (3 clear options). Polymarket's 8+ wallet icons is confusing for newcomers - mixing social login with Web3 wallets creates cognitive overload.

---

### Market card patterns

| Platform | Binary markets | Multi-outcome |
|---|---|---|
| Polymarket | YES/NO pill buttons with % | Separate YES/NO per outcome, price in ¢ |
| Kalshi | % pill badge, click to bet | List of outcomes with % badges |
| Manifold | Progress bar + % + "Bet" button | Same bar pattern |
| Futuur | Progress bars per outcome | Visual bars with % - best multi-outcome UI |

**Insight:** Futuur's probability bars for multi-outcome are the clearest visual approach. Polymarket's cent-based pricing (Buy Yes 37¢) is accurate but abstract for new users.

---

### What's missing across all competitors

1. **No clear "why this number?" explanation** - odds show % or ¢ but never explain WHY that's the market price or what drives changes
2. **Weak onboarding for new users** - no guided first bet, no explanation of CLOB/AMM mechanics inline
3. **No narrative around events** - markets exist as isolated questions, not connected to news context
4. **Trust signals are buried** - resolution rules, dispute processes exist but are hard to find
5. **Portfolio clarity is poor** - understanding your P&L, position, and potential payout is complex

---

## Our Differentiators (confirmed after research)

Based on JTBD (J2 primary: engaged spectator with skin in the game):

1. **Events as stories, not just questions** - each market connected to live news context
2. **Transparent mechanics inline** - explain why odds move, how CLOB pricing works, right on the market page
3. **Guided first experience** - walk new user through first bet with real money context
4. **Cleaner signup than Polymarket** - 3 options max (Google, Apple, Wallet). Separate social from Web3 onboarding
5. **Clearer payout display** - show "if YES wins, you get $X" not just abstract ¢ prices

---

## Open Questions (still to research)

- [ ] Commission rates: Polymarket takes ~2% fee on winnings - verify and benchmark others
- [ ] Minimum bet: Polymarket $0.01 - what's the sweet spot for UX?
- [ ] KYC thresholds: at what deposit amount does KYC trigger?
- [ ] Blockchain/chain: Polymarket uses Polygon (low fees). Base and Arbitrum also viable
- [ ] AMM mechanism: LMSR vs CPMM - which to implement?
- [ ] Fiat on-ramp providers: MoonPay, Transak, Stripe (crypto) - pricing and UX comparison needed
- [ ] Futuur's crypto + fiat hybrid - how exactly do they handle currency switching?

---

## Competitor language (Мова конкурентів)

> Added 2026-07-03 to ground the product voice guide (`voice/voice.md`). Verbatim interface + marketing copy pulled from competitor sites (web fetch, July 2026) plus the prior screen captures and `benchmark-trust.md`. The value is the shared pattern at the end: where every competitor writes the same, our difference is voice.

### Polymarket (polymarket.com, verbatim)
- Tagline: **"The World's Largest Prediction Market™"**
- Sort / nav: "Browse · New · Trending · Popular · Liquid · Ending Soon · Competitive"
- Bet interface: **"Buy Yes / No"** priced in cents (e.g. "Buy Yes 37¢"); card meta "$5M Vol"
- Risk (footer only): "Trading involves substantial risk of loss."

### Manifold (manifold.markets/about, verbatim)
- Tagline: **"Manifold is the world's largest social prediction market."**
- Sub: "Get accurate real-time odds on politics, tech, sports, and more."
- CTA: **"Get Ṁ1,000 to start trading!"**
- Explainer: **"Our probabilities are created by users buying and selling shares of a market."**
- Mission: "Combat misleading news by incentivising traders to be fast and correct."
- Note: "Many people who don't like betting still use Manifold to get reliable news."

### Metaculus (metaculus.com, verbatim)
- Tagline: **"Clarity in a complex world"**
- Sub: "Collective intelligence for the public good"
- Descriptor: "...an online forecasting platform and aggregation engine working to improve human reasoning and coordination..."
- Metric: "3.99M+ Predictions"; primary action button: **"Predict"**

### Kalshi (prior captures + `benchmark-trust.md`; site rate-limited on refetch)
- CFTC-regulated badge as the headline trust signal (C1: 5/5)
- Prices shown in cents; "LIVE" hero card; auto-modal signup fired on entry
- Interface density trending toward a "Bloomberg Terminal" look

### Adjacent tone models (from `benchmark-trust.md` / `competitive-analysis.md`)
- Bet365: "world's favourite online sports betting company"; responsible-gambling line **"When the fun stops, stop."**
- Coinbase: **"Your crypto is safe here"** (funds-protection copy)
- Robinhood: "commission-free"; plain-English errors; **confetti on first trade**
- Cash App: **"No jargon"**

### The shared pattern - where everyone writes the same
1. **Lead with the naked number** (%, cents, a gauge) and no reason beside it. "The % is the language of the genre" (`competitive-analysis.md`); no competitor answers "why this price?".
2. **Superlative scale as the headline** - "world's largest / world's favourite / collective intelligence." At launch we cannot honestly compete on this claim.
3. **Trading-desk vocabulary** - "Buy Yes shares", "cents", "liquidity", Bloomberg density. Trader's language, not a spectator's.
4. **Trust / funds copy buried or absent** - Polymarket has no "where is my USDC" line; risk sits in the footer.
5. **The loss moment is undesigned** - nobody has a "here's what happened, here's your next step" screen after a resolution.

**Our difference is voice, not features:** the sentence next to the number, one plain trust line before the ask, spectator words, honest specifics over superlatives, and a designed loss. Turned into rules in `voice/voice.md`.
