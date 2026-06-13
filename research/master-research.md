# Master Research - Prediction Market Platform

> Synthesis of all research phases. Source of truth before wireframes.
> v_refresh - June 2026. Updated June 12, 2026 with: (1) fresh competitor data - Hyperliquid HIP-4, Polymarket declining, Kalshi volume leader $22B valuation, EU MiCA enforcement; (2) Product Model migrated to Strategy (AIDA retired, Business Model + Riskiest Assumption added); (3) AARRR one-metric-per-stage clarified.
> Sources: [strategy.md](./strategy.md) - [product-model.md](./product-model.md) (preserved for history) - [aarrr.md](./aarrr.md) - [competitive-analysis.md](./competitive-analysis.md) - [benchmark-trust.md](./benchmark-trust.md) - [ux-patterns.md](./ux-patterns.md) - [research.md](./research.md) - [CLAUDE.md](../CLAUDE.md) - screens in `screens/`

---

## v_refresh Summary (June 2026)

Five things changed meaningfully since the original research:

**1. Sports markets are dominant and the gap is widening - decision: post-MVP with 3-month checkpoint.**
Kalshi earned $263.5M in fee revenue in 2025 (89% sports), then grew to $17.9B monthly volume in May 2026 (90% sports). Polymarket is now declining in volume. Sports is the dominant category by a growing margin. Decision: events-first MVP with a 3-month checkpoint after launch - if core mechanics are validated, sports enters as month-4 priority.

**2. The competitor landscape now has three tiers - and a new HARD entrant.**
Prior analysis treated all competitors as one pool. New structure: HARD (Polymarket, Kalshi, Futuur, DraftKings Predictions, Hyperliquid HIP-4), SOFT (Bet365, Betfair Predicts, eToro, Manifold, DraftKings DFS), ASPIRATIONAL (Revolut, Coinbase, Robinhood, Cash App, Duolingo). Hyperliquid HIP-4 launched May 2, 2026 with zero-fee on-chain prediction markets - the most structurally similar to our Web3 vision. Betfair Predicts beta April 2026.

**3. Product Model retired - Strategy is the new structure.**
AIDA is retired. The new strategy.md holds: Objectives, Audience Segments, Business Model (fee options, pricing hypothesis), Riskiest Assumption. The Riskiest Assumption is new: "News Junkies will deposit real money and bet once the fiat barrier is removed" - and specifically that the barrier was friction, not motivation.

**4. Fee model is an open decision - industry moved to tiered taker fees per trade.**
2026 standard: Polymarket (0% geopolitics to 1.80% crypto), Kalshi (0.07xpx(1-p)), DraftKings ($0.01 flat). "Fee on win" (our original model) is softer but earns less. Consider free-entry category (0% fee) as activation hook. Decide before building fee logic.

**5. EU MiCA enforcement is active July 2026.**
Curacao-licensed platforms face geo-blocks in FR, DE, NL, PL, BE starting July 2026. Our accessible global market shrinks to: Latin America, Southeast Asia, Middle East, non-EU Eastern Europe. Acquisition, market selection, and fiat on-ramp must account for this.

---

## 1. Introduction

### Purpose of the Research

The product is a prediction market platform (YES/NO bets on real-world events, crypto collateral). Target audience: 20-40, mobile-first, trust is the #1 value. MVP scope: mobile web, 10-20 curated markets, fiat on-ramp.

Research goal: understand WHAT and FOR WHOM we're building, what solutions already exist and where the gap is, what to carry into MVP from best-in-class products, and which UX architecture to choose.

### What We're Solving

**Problem:** no existing prediction market has solved onboarding for the "ordinary" user without a Web3 wallet. Polymarket - CLOB on Polygon, entry via MetaMask or 8+ wallet icons. Kalshi - USD fiat, but US-only. Others are either play money or niche.

**Our answer:** become the most understandable prediction market for the News Junkie (25-40, follows the news, not necessarily into crypto). Differentiator - story-driven UX, fiat on-ramp without a Web3 barrier, and trust through transparency rather than regulatory badges.

### How We're Solving It

- JTBD J2 primary: "engaged spectator with skin in the game" - follow events with a real stake
- UX architecture: Story-driven Discovery - event = narrative unit (context + mechanics + bet)
- Trust strategy: concrete promise of funds protection + on-chain transparency (instead of FSCS/SIPC, which are unavailable)
- Revenue: fee per trade (model TBD - fee on win vs fee per contract) - [? see v_refresh #3 above]

### What We Decided (Key Conclusions) - Updated June 2026

1. News Junkie - primary segment. CONFIRMED. Largest audience, fiat on-ramp removes the barrier, directly aligned with JTBD J2.
2. No competitor explains "why is the price this?" - CONFIRMED as our differentiator and the reason for Story-driven UX.
3. Activation - the biggest risk. CONFIRMED. Fiat first + 4-screen Robinhood-style onboarding (not demo bet) - MVP priority.
4. Regulatory badges (FSCS/SIPC) unavailable to us. CONFIRMED. Replaced with on-chain transparency.
5. CLOB vs AMM - still open [?]. Hyperliquid HIP-4 (zero-fee on-chain) added as a new reference model. AMM remains best for cold-start liquidity.
6. Sports markets = post-MVP. CONFIRMED with 3-month checkpoint added. Kalshi 90% sports in May 2026. Events-first launch, sports as month-4 decision post-launch data.
7. Fee model unresolved. Industry moved to tiered taker fees. "Fee on win" may underperform vs fee-per-contract. Decide before building fee logic.
8. NEW: Riskiest Assumption identified. "News Junkies will deposit real money and bet once the fiat barrier is removed." If false (barrier is motivation, not friction), no UX fix works. First-bet completion rate from cold traffic is the test signal.
9. NEW: EU MiCA enforcement active July 2026. Curacao-licensed platforms blocked in FR, DE, NL, PL, BE. Accessible markets: Latin America, Southeast Asia, non-EU Eastern Europe, Middle East.

---

## 2. Strategy

*Source: [strategy.md](./strategy.md) - Prior file [product-model.md](./product-model.md) preserved for history*

### Objectives

| # | Goal | Metric |
|---|---|---|
| O1 | Trusted platform for PM outside the US | MAU, NPS, retention 30d |
| O2 | Web3 betting for users without crypto experience | % of users without a prior wallet who completed their first bet |
| O3 | Engaged community around events | DAU/MAU ratio, shares/user |
| O4 | Stable trading volume | Monthly trading volume, revenue per user |

---

### Audience — 3 Segments

```
┌─────────────────────────────────────────────────────────────────┐
│                        OUR AUDIENCE                             │
├──────────────────┬──────────────────┬───────────────────────────┤
│   Crypto Native  │  News Junkie ★   │   Crossover Bettor        │
│     22–35        │     25–40        │        28–42              │
├──────────────────┼──────────────────┼───────────────────────────┤
│ Already in Web3. │ Follows the      │ Bets on sports.           │
│ Has MetaMask.    │ news. Crypto not │ Looking for more          │
│ Knows DeFi.      │ required.        │ intellectual markets.     │
├──────────────────┼──────────────────┼───────────────────────────┤
│ Monetize         │ Prove they're    │ New arena where           │
│ crypto knowledge │ right on current │ analysis matters,         │
│                  │ events           │ not luck                  │
├──────────────────┼──────────────────┼───────────────────────────┤
│ 🥈 Secondary     │ 🥇 PRIMARY       │ 🥉 Later (post-MVP)       │
└──────────────────┴──────────────────┴───────────────────────────┘
```

---

### Business Model Summary

- **Primary fee:** trading fee per resolved bet (Option B: ~2% on win) or per trade (Option A: tiered taker fee 0%-1.8% by category). Decision required before build.
- **Industry direction 2026:** tiered taker fees per trade (Polymarket, Kalshi, DraftKings). Free entry in one category (geopolitics/politics) is an activation lever.
- **No subscription, no account tiers at MVP.** Maker rebates (20-25% of collected fees) to incentivize liquidity - consider from launch.
- **Value exchange:** users bring capital and knowledge. Platform earns from volume, not house edge.
- **Free-entry hook hypothesis:** 0% fee on one category to lower the first-bet psychological cost.

*Full detail: [strategy.md - Business Model](./strategy.md)*

---

### Riskiest Assumption

> News Junkies will deposit real money and bet once the fiat barrier (no crypto wallet required) is removed. The assumption is that the barrier is FRICTION, not MOTIVATION.

- If false: no UX improvement works. Motivation gap is not fixable with onboarding.
- Test signal: first-bet completion rate from cold News Junkie traffic. Below 10% = motivation problem.
- H1 (fiat on-ramp increases activation) tests friction. The Riskiest Assumption tests motivation. Both must be true.

*Full detail: [strategy.md - Riskiest Assumption](./strategy.md)*

---

## 3. AARRR Model

*Source: [aarrr.md](./aarrr.md)*

### Funnel

```
ACQUISITION ──────────────────────────────────────── new registrations/week
     │
     ↓  [ risk: dropout at registration ]
     │
ACTIVATION ───────────────────────── goal: >40% first bet within first 24 hrs
     │
     │  PATH TO AHA MOMENT:
     │  Arrived → Registered → Verified email
     │  → Fiat on-ramp → Found a market
     │  → Understood the mechanics → Placed bet ★ AHA
     │
     ↓  [ risk: losing first bet → doesn't return ]
     │
RETENTION ──────────── day 7: >30% active │ day 30: >15% active
     │
     │  Three levels of return:
     │  Hot (1-3 days): odds movement → notification
     │  Warm (4-14 days): new event in category
     │  Cold (15+ days): resolution + win
     │
     ↓
REVENUE ─────────────────────────────────── ~2% fee on winnings (option B)
     │
     │  Why on winnings, not on entry:
     │  Entry: bet $100 → in play $98 → pain immediately
     │  Exit: won $150 → received $147 → pay when you earned ✓
     │
     ↓
REFERRAL ────────────────────── goal: >20% new users via sharing
          │
          Share card    Referral bonus    Public profile
          (Robinhood)   ($5 for both)     (Metaculus-style)
```

---

### Summary Metrics Table

| Stage | Key Metric | Goal | v_refresh status |
|---|---|---|---|
| Acquisition | New registrations / week | - [?] | Unchanged |
| Activation | % first bet within 24 hrs | >40% | Unchanged hypothesis |
| Retention D7 | % active on day 7 | >30% | Unchanged hypothesis |
| Retention D30 | % active on day 30 | >15% | Unchanged hypothesis |
| Revenue | Trading volume / month | - [?] | Unchanged |
| Referral | % new users via sharing | >20% | Unchanged hypothesis |

*Goals are hypotheses, require validation after MVP launch. [aarrr.md](./aarrr.md)*

---

### Product Decisions by Stage - v_refresh

| Stage | MVP Decision | v_refresh |
|---|---|---|
| Acquisition | Every market = SEO page with dynamic og:image odds | NEW: add sports category landing pages to SEO even if sports not in MVP v1 |
| Activation | Fiat on-ramp on first screen + 4-screen Robinhood "swipeys" onboarding | UPDATED: drop demo bet (Manifold evidence); minimum stake $1-5 real money instead |
| Retention | Smart notifications (price movement + deadline) + personal feed by category | NEW: post-resolution loss screen + prediction streak mechanic |
| Revenue | Commission shown before confirmation: "The platform earns $0.40 if you win" | OPEN: fee on win vs fee per trade - decide before building fee logic |
| Referral | Share card after every resolution (auto-generated) | NEW: public prediction track record from day one (eToro CopyTrader model) |

---

## 4. Competitors

*Sources: [competitive-analysis.md](./competitive-analysis.md) - screens in `screens/`*
*v_refresh: Restructured into HARD / SOFT / ASPIRATIONAL groups. Matrix refreshed with new data.*

### Competitor Groups

**HARD** (same product, same audience): Polymarket (declining, US relaunch, ICE $9B), Kalshi (volume leader $17.9B/month, $22B valuation), Futuur (stagnant, closest analog), DraftKings Predictions ($1.3B annualized), Hyperliquid HIP-4 (zero-fee, May 2026)
**SOFT** (same JTBD, different product): Bet365, Betfair Predicts (beta April 2026, UK), eToro (IPO May 2025), Manifold (play-money only), DraftKings DFS
**ASPIRATIONAL** (best-in-class UX benchmarks): Revolut, Coinbase, Robinhood, Cash App, Duolingo

*Full tables with rationale: [competitive-analysis.md](./competitive-analysis.md)*

### Matrix by Axis - v_refresh (5 most relevant)

| Axis | Polymarket | Kalshi | Futuur | DraftKings Predictions | Bet365 |
|---|---|---|---|---|---|
| **Audience** | Crypto natives, DeFi, global (not US) | US-first, TradFi, sports bettors | Global, crypto + fiat hybrid | US (38 states), mainstream sports fans | Global, 80M+ registered, fiat only |
| **Product foundation** | CLOB on Polygon, USDC, embedded wallets | CFTC-regulated exchange, USD fiat | Crypto + fiat hybrid, multi-currency | CFTC event contracts, launched Dec 2025 | Classic bookmaker, decimal odds |
| **Key mechanics** | Conditional tokens, taker fee 0.75-7% by category, maker rebate 20-25% | Order book, variable fee by probability, $263.5M fee revenue 2025 | Probability bars per outcome [? fee %] | $0.01/contract fee, combos (parlays) added May 2026 | House-set fixed odds, cash out, live streaming |
| **Trust** | On-chain + UMA resolution, $9B+ volume, weak on fund protection copy | CFTC = highest institutional trust, US banking partners | Less known, no regulatory badge, small track record | DraftKings brand + CFTC regulation, new = limited history | 20+ year brand, 30+ licenses, responsible gambling visible |
| **Monetization** | Taker fees by category, $1M+/day revenue April 2026 | Exchange fees variable by probability, $1.5B annualized 2026 | Commission [? exact % not public] | $0.01 per contract each side | House margin ~4-7% baked into odds |

*Sources: [Polymarket fees](https://docs.polymarket.com/trading/fees) - [Kalshi 2025 revenue](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) - [Polymarket daily revenue April 2026](https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html) - [DraftKings Predictions fees](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform)*

*Screenshots: [polymarket-home-mobile.png](./screens/polymarket-home-mobile.png) - [kalshi-home-mobile.png](./screens/kalshi-home-mobile.png) - [futuur-home-mobile.png](./screens/futuur-home-mobile.png) - [draftkings-predictions-home-mobile.png](./screens/draftkings-predictions-home-mobile.png) - [bet365-home-mobile.png](./screens/bet365-home-mobile.png)*

---

### 3 Common Patterns (present in all)

**1. Horizontal category navigation + bottom tab bar**
Polymarket (4 tabs), Kalshi (4 tabs), Manifold (5 tabs), Futuur (3 tabs), Bet365, DraftKings - all use this pattern. De-facto genre standard across both prediction markets and sports betting. Absence = unrecognizable platform.

**2. Probability percentage (or equivalent) as the primary number**
On every card and detail screen the % (or price in cents, or odds) sits above everything. It is the market "price" and "game state" simultaneously. Even Bet365 makes live odds the dominant card element.

**3. Probability-over-time chart**
From simple line (Manifold) to candlestick (Kalshi) to live odds movement. Movement = engagement. Users return to check position. DraftKings Predictions added charting for the same reason.

---

### 3 Key Differences

**1. Regulation defines the product more than any UX choice**
Kalshi = CFTC + US fiat + $1.5B annualized revenue in 2026. Polymarket = no US + crypto (USDC) + global. DraftKings = CFTC + 38 US states. For a global non-US product, Polymarket and Futuur are the structural analogs. Kalshi proves the model scales, but its license is not replicable.

**2. Sports vs events: the space is bifurcating**
Kalshi 89% sports revenue in 2025. Polymarket sports > 60% of open interest by October 2025. The sector is splitting into sports-first (Kalshi, DraftKings Predictions, Betfair Predicts) and events-first (Polymarket's original positioning, Futuur). Our events-first thesis targets the underserved direction, but at lower volume in the near term.

**3. CLOB vs AMM vs fixed odds**
Polymarket + Kalshi = order book (CLOB). Azuro = decentralized AMM. Bet365 = house-set fixed odds. For cold start, CLOB has the liquidity chicken-and-egg problem. AMM avoids this but prices may be worse. Fixed odds require a pricing team. [? unresolved for MVP]

---

### What's Missing Across All Competitors (our gap)

| Gap | Who suffers | Status |
|---|---|---|
| No "why this price?" - zero in-product context for odds | News Junkie, every new user | CONFIRMED - unchanged |
| Onboarding assumes prior knowledge of the product type | All new users | CONFIRMED - Polymarket embedded wallets helped but fiat handoff still 3rd party |
| Markets exist in isolation from news that drives them | News Junkie | CONFIRMED - unchanged |
| Trust signals are buried, funds protection unexplained | New user making first deposit | CONFIRMED - Polymarket trust 19/40 |
| Post-resolution experience is undesigned - especially for losses | All new users | NEW - no competitor has a "here's what happened, here's next" loss screen |
| Fiat on-ramp not owned - still a 3rd-party handoff | News Junkie | CONFIRMED - unchanged |

---

## 5. Benchmark: Trust & First-Time Credibility

*Source: [benchmark-trust.md](./benchmark-trust.md) · screenshots in `screens/`*
*v_refresh: Products changed from (Revolut/Coinbase/Robinhood/Kalshi/Polymarket) to (Polymarket/Kalshi/Futuur/Bet365/Revolut). New set is specific to our market: top 3 HARD competitors + 1 SOFT + 1 ASPIRATIONAL.*

### Why Trust as a Dimension

Trust is the #1 value for the audience (20-40, real money, fintech). This is exactly where direct competitors are weakest. This is where decisions for wireframes grow from.

### Scores (1-5, 8 criteria x 5 products) - v_refresh

| Criterion | Polymarket | Kalshi | Futuur | Bet365 | Revolut |
|---|:---:|:---:|:---:|:---:|:---:|
| C1 Regulatory transparency | 2 | **5** | 1 | **5** | **5** |
| C2 Funds protection | 1 | 4 | 1 | 4 | **5** |
| C3 Fee transparency before action | 2 | 3 | 2 | 3 | 4 |
| C4 Social proof | 4 | 3 | 2 | **5** | **5** |
| C5 Clarity of first impression | 3 | 4 | 3 | **5** | 4 |
| C6 Onboarding friction | 2 | 2 | 2 | 3 | 3 |
| C7 Risk communication | 3 | 4 | 1 | 4 | 3 |
| C8 Resolution clarity | 2 | 3 | 2 | 4 | 3 |
| **TOTAL** | **19** | **28** | **14** | **33** | **32** |

**Key insight:** Futuur (our closest structural analog - global, crypto+fiat, no US regulation) scores 14/40 - worse than Polymarket. Our market has a trust floor of 14-19/40. The Crossover Bettor's reference (Bet365) scores 33/40. That is a gap of 14-19 points we need to close through design decisions, not licensing.

*Screenshots: [polymarket-home-mobile.png](./screens/polymarket-home-mobile.png) - [kalshi-home-mobile.png](./screens/kalshi-home-mobile.png) - [futuur-home-mobile.png](./screens/futuur-home-mobile.png) - [bet365-home-mobile.png](./screens/bet365-home-mobile.png) - [revolut-trust-mobile.png](./screens/revolut-trust-mobile.png)*

---

### Top 3 Mechanisms for MVP - v_refresh

**1. Immediate product clarity at first impression (Bet365, C5: 5/5)**
> Show a live market with context on the homepage. No signup required to see it. Event + probability + brief context + YES/NO. The user should understand the product in 3 seconds.

Why it works: the first trust failure is cognitive anxiety ("what even is this?"). Bet365 eliminates it instantly. We must do the same for prediction markets.

**2. Concrete promise of funds protection (Revolut, C2: 5/5)**
> "Your USDC is held 1:1. We never lend it without your permission."

Where: first deposit screen + "How it works." One sentence, not legal text.
Why it works: Futuur scores 1/5 on this criterion while being our closest structural analog. The gap is completely open. This is the new user's primary fear - close it proactively.

**3. Resolved markets as social proof (Bet365 + Polymarket, C4)**
> "N markets resolved correctly - since [date] - all on-chain verifiable."

Our equivalent of "80M users" or "$9B+ traded." At launch we have zero of either. Resolved market count is a signal we can build from day one and display honestly.
Why it works: users need evidence the platform has delivered on its core promise. Resolved markets prove it.

---

### 1 Mechanism That Will NOT Work

**Regulatory badges (FSCS/SIPC/FDIC/CFTC) or simulating Bet365's brand authority.**

These badges require real licenses we do not hold. Bet365 scores 33/40 through 20 years + 30 licenses - that track record is not copyable at launch.

**Alternative:** on-chain transparency + non-bank disclosure: "All settlements are on the blockchain. Any user can verify every resolved market." This is the honest equivalent.
*[benchmark-trust.md]*

---

## 6. UX Patterns

*Source: [ux-patterns.md](./ux-patterns.md)*

### Audience Behavioral Patterns

| Pattern | Description | Key for us |
|---|---|---|
| **Event-triggered arrival** | User arrives when something happens — elections, a crypto move, a scandal | ★ KEY |
| Knowledge validation | User already has an opinion and comes to check whether the market agrees | News Junkie + Crypto Native |
| Position monitoring | Comes back to see if the price is moving their way | After the first bet |
| Value hunting | Looking for where the market is "wrong" | Crypto Native, Crossover |
| Social sharing | Wants to show their prediction/win — confirmation of being right | All, especially News Junkie |

**Event-triggered arrival — key for all segments.** Entry point. How we greet the user "from the news" determines activation and the first bet.

---

### 5 Fundamentally Different UX Patterns

| # | Pattern | How it works | When it fits | When it breaks |
|---|---|---|---|---|
| 1 | **Event Feed** | Algorithmic/chronological card feed. User scrolls. | Mobile, > 20 markets, repeat session | < 20 markets = looks empty. New user doesn't understand sorting |
| 2 | **Market Board** | Table of all markets: price, volume, 24h change. Filters are the primary navigation | Experienced users, J3 segment | Newcomers leave. Kills emotional connection to the event |
| 3 | **Story-driven Discovery** | Event = narrative unit: context + why it matters + what market says + CTA | News Junkie, first contact | Longer path to action. Requires editorial or AI |
| 4 | **Portfolio-first** | First screen — active positions, P&L, deadlines | Retention phase, experienced user | Empty state for new users = demotivation |
| 5 | **Guided Challenge** | "Bet of the day" — one choice, two buttons, game loop | Onboarding, reducing cognitive load | Gets annoying after 5–7 sessions. Limits experienced users |

---

### Chosen Pattern: Story-driven Discovery

**✅ Best fit — 3 reasons:**

**Reason 1 — Direct alignment with J2 JTBD.**
"Following events with real skin in the game" — this is about context, not numbers. Story-driven delivers that context inside the product. *[CLAUDE.md: JTBD J2 primary]*

**Reason 2 — Closes the main gap of competitors.**
No competitor explains why the price is what it is and what will affect the outcome. Markets are isolated questions without context. This is our differentiator. *[research.md: What's missing — "No clear why this number?"]*

**Reason 3 — Builds trust without regulatory badges.**
A clear event description + resolution conditions + source = the platform knows what it's talking about. Trust through content transparency — our alternative to FSCS/SIPC. *[benchmark-trust.md: 1 mechanism that won't work]*

---

### Under Condition X: Event Feed

**Condition X:** > 30 active markets + user has already made their first bet.
Event Feed is the ideal retention pattern for repeat sessions.
**Decision:** Story-driven for first contact and onboarding → Feed for return visits.

---

### ❌ Not a Fit: Market Board

Audience 20–40, trust-first, J2-first (engaged spectator). Market Board requires financial literacy that the News Junkie doesn't have. A table with prices in cents is the language of a trader, not a spectator. It would make us just another Polymarket, whereas our differentiator is being more understandable.
*[CLAUDE.md: Design Principles — "clarity over completeness"]*

---

## 7. Conclusions: Gaps and Hypotheses

### Identified Gaps

| Gap | Where confirmed |
|---|---|
| No PM has solved onboarding without a Web3 wallet | [competitive-analysis.md: open question 1] |
| No one explains "why this price" | [research.md: What's missing] |
| Markets are isolated from news context | [research.md: What's missing] |
| Polymarket trust score — 19/40 (lowest) | [benchmark-trust.md: scores] |
| Polymarket signup: 8+ wallet icons = cognitive overload | [screens/polymarket-signup-mobile.png] |
| CLOB vs AMM for MVP: CLOB requires liquidity from day 1 | [competitive-analysis.md: open question 2] |
| Resolution trust without regulation and track record | [competitive-analysis.md: open question 3] |

---

### Hypotheses in Format: if / then / because

> Note on Riskiest Assumption: H1 is the closest proxy for the Riskiest Assumption but tests the friction side. The Riskiest Assumption tests the motivation side - whether News Junkies will bet at all, not just whether they can bet without a crypto wallet. Both must be true. H1 is the MOST TESTABLE hypothesis and the FIRST to validate. See [strategy.md - Riskiest Assumption](./strategy.md).

**H1 — Fiat on-ramp will increase activation** ← CLOSEST TO RISKIEST ASSUMPTION
_If_ we provide the ability to deposit by card without a Web3 wallet from the first screen after registration,
_then_ the % of users who placed their first bet within 24 hrs will exceed 40%,
_because_ the main barrier for the News Junkie is needing MetaMask and USDC before the first bet. Polymarket solves this through MoonPay/Transak [?], but it's not highlighted as a UX priority.
_Test signal:_ if completion rate from cold News Junkie traffic is below 10%, the barrier is motivation, not friction - the Riskiest Assumption is false.
*Data: [aarrr.md: Activation — "Fiat first"] · [competitive-analysis.md: open question 1] · [strategy.md: Riskiest Assumption]*

**H2 — Story-driven UX will increase conversion of new users to first bet**
_If_ every event has a narrative unit (context + what the market says + resolution conditions),
_then_ conversion from first visit to bet will be higher than Polymarket / Kalshi,
_because_ no competitor provides context inside the product — the News Junkie arrives "from the news" and doesn't understand isolated questions without background.
*Data: [research.md: What's missing — "No narrative around events"] · [ux-patterns.md: Story-driven Discovery — Reason 2]*

**H3 — Fee on winnings (not on entry) reduces churn**
_If_ the fee is charged on winnings (~2%) and not on entry,
_then_ early churn after the first bet will be lower,
_because_ "paid and lost" is the most painful scenario. "Only pay when you earn" is psychologically softer.
*Data: [aarrr.md: Revenue — "Option B"] · logic confirmed by Polymarket's model (source: docs.polymarket.com [?])*

**H4 — Concrete promise of funds protection will increase trust**
_If_ the first deposit screen shows: "Your USDC is held 1:1. We never lend it without your permission",
_then_ deposit completion rate will increase,
_because_ the new fintech user's primary fear is "what happens to my money." Coinbase solves it exactly the same way and has C2: 5/5 in our benchmark.
*Data: [benchmark-trust.md: Top 3 mechanisms — Coinbase] · [screens/coinbase-trust-signals.png]*

**H5 — Share card after resolution will drive >20% organic traffic**
_If_ after every resolution a share card with the result is automatically generated,
_then_ >20% of new users will come via sharing,
_because_ "I told you so" is a powerful social instinct. A win makes people want to show it off. Robinhood and Spotify Wrapped confirmed this pattern in other verticals.
*Data: [aarrr.md: Referral — "Win sharing"] · [ux-patterns.md: Social sharing]*

**H6 — Fee transparency before confirmation will reduce complaints**
_If_ the exact fee amount is shown before every bet confirmation ("The platform earns $0.40 if you win"),
_then_ the number of complaints and refund requests will be lower,
_because_ hidden fees are the #1 cause of churn and negative reviews in fintech. Robinhood made "Commission-Free" their main message and got the highest C3 (5/5) in the benchmark.
*Data: [benchmark-trust.md: Top 3 mechanisms — Robinhood] · [aarrr.md: Revenue — transparency]*

---

### Open Questions (before wireframes) - v_refresh

| # | Question | Why it matters | v_refresh status |
|---|---|---|---|
| Q1 | CLOB vs AMM for MVP? | Affects pricing mechanics, bet UX, and cold-start liquidity | UPDATED: Azuro vAMM documented as the decentralized AMM path; still unresolved [?] |
| Q2 | Fiat on-ramp provider? MoonPay vs Transak vs Stripe | Affects onboarding UX and commission | Unchanged [?] |
| Q3 | KYC threshold? At what deposit amount does verification trigger | Activation friction | Unchanged [?] |
| Q4 | Minimum bet? | Psychological barrier vs UX | UPDATED: lean toward $1-5 as first-bet minimum; demo bet likely counterproductive |
| Q5 | Resolution without regulation - is team multisig enough at launch? | Core trust problem | Unchanged [?] |
| Q6 | Does a demo bet increase or decrease conversion? | Activation decision | UPDATED: Manifold sunsetting sweepcash March 2025 suggests play-money does not convert. Lean toward skipping demo bet. |
| Q7 | Futuur: how exactly is crypto+fiat hybrid structured? | Reference for our model | Unchanged [? still not fully public] |
| ~~Q8~~ | ~~Sports markets at MVP?~~ | DECIDED: post-MVP with 3-month checkpoint. Events-first launch, sports as month-4 decision after launch data. | CLOSED |
| Q9 | Fee on win vs fee per trade? | Industry 2026 standard: tiered taker fees (Polymarket 0%-1.80% by category, Kalshi formula, DraftKings $0.01 flat). Fee on win is softer but earns less. Consider Option B + free category at MVP, migrate to Option A at scale. | OPEN - decide before build |
| Q10 | NEW: Which jurisdictions are accessible under our expected license? | EU MiCA enforcement July 2026 blocks FR, DE, NL, PL, BE for Curacao-licensed platforms. Non-US, non-EU accessible market must be defined explicitly before market selection and acquisition planning. | NEW OPEN QUESTION |
| Q11 | NEW: How do we address insider trading risk without CFTC enforcement tools? | Kalshi: 150+ investigations, employer-disclosure, whistleblower tools. Polymarket: CFTC complaint filed June 2026. On-chain settlement provides verification but not market integrity governance. | NEW OPEN QUESTION |

---

## 8. Live User Research — June 2026

*Source: Deep web research, June 13, 2026. 111 search agents, 28 sources fetched, 116 claims extracted → 4 confirmed after adversarial 3-vote verification. 21 claims killed.*
*Angles searched: friction vs. motivation / post-loss behavior / bet sizing & play-money conversion / event-driven spikes / trust signals / non-US TAM / time-to-first-bet funnel.*

---

### Confirmed findings (survived adversarial verification)

**F1 — Play-money → real-money conversion: does not work.** `HIGH confidence`

Manifold's sweepstakes model (real money parallel to play-money mana) was sunset March 28, 2025. From Manifold's own blog post (February 2025): *"unfortunately haven't met our usage goals and they've been drawing focus away from building out the core platform."* Contributing factors: low volume that could not cover compliance overhead and support costs.

→ **Confirms decision: no demo bet in MVP.** Play-money is not a path to real-money activation — tested at scale and failed.

*Sources: [Manifold blog Feb 2025](https://news.manifold.markets/p/focusing-on-mana-bringing-sweepstakes) (primary) · [Gambling911](https://www.gambling911.com/gambling/manifold-eliminates%20sweepstakes-model)*

---

**F2 — 70–84% of prediction market traders lose money.** `HIGH confidence`

Four independent analyses 2025–2026, all converging:

| Study | Date | Sample | Loss rate |
|---|---|---|---|
| DeFi Oasis | Dec 2025 | 1.7M addresses | 70% |
| Wall Street Journal | May 2026 | 1.6M accounts | >70% |
| Academic study | Nov 2022 – Mar 2026 | — | 68.8% |
| Andrey Sergeenkov | Apr 2026 | 2.5M addresses | 84.1% |

**Implication for Riskiest Assumption:** removing friction (fiat on-ramp) is necessary but not sufficient. Even users who clear the crypto barrier predominantly lose money. The market is structurally tilted toward sophisticated traders. If News Junkies arrive and lose their first bets quickly — retention becomes the real problem, not activation.

*Sources: [Yahoo Finance / DeFi Oasis Dec 2025](https://finance.yahoo.com/news/70-polymarket-traders-lost-money-192327162.html)*

---

**F3 — After a first loss: users don't leave — they chase losses.** `MEDIUM confidence`

Journalistic case (2026): a 24-year-old engineer lost over $10,000 in 8 days on Kalshi, escalating from small bets to $1,000+ wagers, then taking out a loan to recover. Direct quote: *"There'll be a big winning streak at the beginning, which happened to me — then bam, everything's gone."*

Pattern: early wins → overconfidence → systematic losses → loss-chasing → catastrophic exit.

Context: 19 federal lawsuits against Kalshi by January 2026. Class-action from a user who lost tens of thousands in a single month. Confidence is medium — single anecdote, not a population study — but directionally credible given the lawsuit volume.

→ **The post-resolution loss screen is not a UX detail.** It is the moment where we can intervene before the chasing loop begins. No competitor currently designs this moment.

*Source: [AOL journalistic report 2026](https://www.aol.com/news/bam-everythings-gone-two-young-102401794.html)*

---

### What we still do not know (no data survived verification)

| Question | Status |
|---|---|
| Do News Junkies without crypto actually convert when friction is removed? | [?] No verified case. The Riskiest Assumption remains untested in the wild. |
| Minimum bet size that feels "real" without triggering harm escalation | [?] No data. Manifold-experiment failed but said nothing about optimal amount. |
| Which specific events cause the biggest signup/activation spikes? | [?] All candidate claims failed adversarial verification. No verified data. |
| Time from landing to first bet — funnel benchmark | [?] No verified data survived. |
| What trust signals actually work, in users' own words? | [?] No verified quotes or reviews survived verification. |
| TAM for non-US News Junkie segment | [?] All market-size projections were refuted. Genuinely unknown. |

---

### Key implication from this research

The central question shifted: not "will News Junkies come?" but **"what happens after their first loss, and do they stay?"**

This cannot be answered by research — only by real traffic data. First-bet completion rate and day-7 retention after a first loss are the two metrics that will tell us whether the Riskiest Assumption is true or false.

The post-resolution loss screen is the highest-priority untested retention intervention. Design it before launch. Measure it as the first post-launch signal.

---

*Compiled from: [strategy.md](./strategy.md) - [product-model.md](./product-model.md) (history) - [aarrr.md](./aarrr.md) - [competitive-analysis.md](./competitive-analysis.md) - [benchmark-trust.md](./benchmark-trust.md) - [ux-patterns.md](./ux-patterns.md) - [research.md](./research.md)*
*Screenshots: `research/screens/` (26 files, including 5 new from v_refresh: DraftKings Predictions, Bet365, eToro, Betfair Predicts, Azuro)*
*v_refresh sources June 2026: [Kalshi $22B Series F](https://sacra.com/research/kalshi/) - [Kalshi volume leader CNBC](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html) - [Polymarket Fee V2 docs](https://docs.polymarket.com/trading/fees) - [Polymarket ICE $9B](https://financialcontent.com/marketscreener/polymarket-ice-investment-2026) - [Hyperliquid HIP-4](https://bitcoinnews.com/defi/hyperliquid-hip-4-prediction-markets-2026/) - [DraftKings Predictions Combos](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Betfair Predicts](https://www.casino.org/news/betfair-eyes-prediction-market-growth-with-betfair-predicts/) - [EU MiCA enforcement](https://trmlabs.com/post/mica-enforcement-2026)*
