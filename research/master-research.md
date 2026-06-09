# Master Research - Prediction Market Platform

> Synthesis of all research phases. Source of truth before wireframes.
> v_refresh - June 2026. All three core documents refreshed with new competitor data.
> Sources: [product-model.md](./product-model.md) - [aarrr.md](./aarrr.md) - [competitive-analysis.md](./competitive-analysis.md) - [benchmark-trust.md](./benchmark-trust.md) - [ux-patterns.md](./ux-patterns.md) - [research.md](./research.md) - [CLAUDE.md](../CLAUDE.md) - screens in `screens/`

---

## v_refresh Summary (June 2026)

Three things changed meaningfully since the original research:

**1. Sports markets are dominant in the category - earlier than expected.**
Kalshi earned $263.5M in fee revenue in 2025, with 89% from sports. Polymarket shifted to sports > 60% of open interest by October 2025. DraftKings Predictions launched December 2025 (CFTC-regulated, 38 US states), also sports-adjacent. Our events-first thesis is still correct for the News Junkie segment, but volume data suggests sports categories are needed for financial viability earlier than the original post-MVP plan assumed. Action: reconsider adding one sports category at MVP launch.

**2. The competitor landscape now has three tiers - not one.**
Prior analysis treated all competitors as one pool. New structure: HARD (Polymarket, Kalshi, Futuur, DraftKings Predictions, Azuro), SOFT (Bet365, Betfair Predicts, eToro, Manifold, DraftKings DFS), ASPIRATIONAL (Revolut, Coinbase, Robinhood, Cash App, Duolingo). Betfair launched a prediction market beta in April 2026, signaling incumbent betting exchanges are converging on our format. Manifold returned to play-money-only in March 2025 - community mechanics without real stakes do not retain users.

**3. Fee model is an open decision - industry moved to fee-per-trade.**
Our original model (2% fee on winnings) is psychologically softer but earns less per trade. Polymarket shifted to taker fees by category (0.75-7% at 50/50) in March 2026, crossing $1M/day in fee revenue two days later. DraftKings uses $0.01 per contract flat fee. The "fee on win" approach may underperform. This must be decided before building fee logic.

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
5. CLOB vs AMM - still open [?]. Azuro's decentralized AMM model documented; for cold start AMM avoids liquidity problem.
6. NEW: Sports markets needed for volume. Kalshi/Polymarket data shows sports drives 60-89% of revenue. Decide whether to include sports at MVP.
7. NEW: Fee model unresolved. Industry moved to fee-per-trade. "Fee on win" may underperform vs fee-per-contract.

---

## 2. Product Model

*Source: [product-model.md](./product-model.md)*

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

### AIDA by Segment

```
ATTENTION  →  INTEREST  →  DESIRE  →  ACTION
```

| | Crypto Native | News Junkie ★ | Crossover Bettor |
|---|---|---|---|
| **Attention** | Twitter/X, crypto media | SEO, news aggregators | Betting communities, referrals |
| **Message** | "The market says 34% — what do you think?" | "Who will win? The market knows — and you can earn" | "More markets, more skill" |
| **Interest** | Volume, liquidity, chart | Live events, context, how odds work | Variety of markets, clear rules |
| **Desire** | High volume + favorable YES/NO rate | An event they're already discussing + "2 minutes" | Comparison with bookmaker odds |
| **Action** | Connect wallet → USDC → bet | Google/Email → fiat card → bet | Google/Email → fiat card → bet |

---

### AIDA ↔ AARRR Connection

| AIDA | AARRR | Product Focus |
|---|---|---|
| Attention | Acquisition | SEO, Twitter, media |
| Interest | Acquisition → Activation | Onboarding, first market |
| Desire | Activation | Guided first bet, fiat on-ramp |
| Actions | Activation → Retention → Referral | First bet, notifications, share card |

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

**HARD** (same product, same audience): Polymarket, Kalshi, Futuur, DraftKings Predictions (launched Dec 2025), Azuro Protocol
**SOFT** (same JTBD, different product): Bet365, Betfair Predicts (beta April 2026), eToro, Manifold, DraftKings DFS
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

*Source: [benchmark-trust.md](./benchmark-trust.md) · screenshots: coinbase-trust.png · revolut-trust.png · robinhood-trust.png*

### Why Trust as a Dimension

Trust is the #1 value for the audience (20–40, real money, fintech). This is exactly where competitors are weakest (Polymarket: 19/40). This is exactly where decisions for wireframes come from. *[CLAUDE.md]*

### Scores (1–5, 8 criteria × 5 products)

| Criterion | Revolut | Coinbase | Robinhood | Kalshi | Polymarket |
|---|:---:|:---:|:---:|:---:|:---:|
| C1 Regulatory transparency | 5 | 5 | 4 | 5 | 2 |
| C2 Funds protection | 5 | 5 | 4 | 4 | 1 |
| C3 Fee transparency before action | 4 | 3 | **5** | 3 | 2 |
| C4 Social proof | **5** | **5** | 4 | 3 | 4 |
| C5 Clarity of first impression | 4 | 4 | **5** | 4 | 3 |
| C6 Onboarding friction | 3 | 3 | 3 | 2 | 2 |
| C7 Risk communication | 3 | 4 | 3 | 4 | 3 |
| C8 Resolution / rules clarity | 3 | 4 | 3 | 3 | 2 |
| **TOTAL** | **32** | **33** | **31** | **28** | **19** |

*Kalshi is weak on C6 (onboarding friction) — auto-modal on entry is aggressive. Polymarket is weak on C2 (funds protection) — no explanation of where and how USDC is stored.*
*Screenshots: [screens/coinbase-trust-signals.png](./screens/coinbase-trust-signals.png) · [screens/revolut-trust.png](./screens/revolut-trust.png)*

---

### Top 3 Mechanisms for MVP

**1. Concrete promise of funds protection (from Coinbase, C2: 5/5)**
> "Your USDC is held 1:1. We never lend it without your permission."

Where to use: first deposit screen + "How it works." Not legal text — one simple sentence.
Why it works: closes the new user's primary fear before they even voice it.
*Screenshots: [screens/coinbase-trust-signals.png](./screens/coinbase-trust-signals.png)*

**2. Social proof as a block on the homepage (from Revolut, C4: 5/5)**
> "$X traded · N users · Rating Y"

Where to use: homepage, after hero, before market list. Compact block.
Why it works: "if so many people trust it — it must be worth trying" — reduces newcomer anxiety.
*Screenshots: [screens/revolut-trust.png](./screens/revolut-trust.png) — 75M+ customers, Trustpilot 4.7, 5 awards in one block*

**3. Fee transparency at the moment of action (from Robinhood, C3: 5/5)**
> "The platform earns $0.40 if you win"

Where to use: confirmation screen before submitting the bet.
Why it works: hidden fees are the #1 cause of churn. Transparency at the moment of highest anxiety = trust.
*Screenshots: [screens/robinhood-trust.png](./screens/robinhood-trust.png)*

---

### 1 Mechanism That Will NOT Work

**Regulatory badges FSCS / SIPC / FDIC / CFTC**

Revolut (FSCS), Robinhood (SIPC/FINRA), Kalshi (CFTC) — all have official regulator shields on their homepage.
We are not a bank or broker — these badges are unavailable without a real license.
Displaying similar elements without the backing will destroy trust the moment it's checked. FTX built a "banking look" without banking guarantees — the outcome is well known.

**Alternative:** on-chain transparency: "All settlements are on the blockchain. You can verify every transaction." This is the honest equivalent for a crypto-native platform.
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

**H1 — Fiat on-ramp will increase activation**
_If_ we provide the ability to deposit by card without a Web3 wallet from the first screen after registration,
_then_ the % of users who placed their first bet within 24 hrs will exceed 40%,
_because_ the main barrier for the News Junkie is needing MetaMask and USDC before the first bet. Polymarket solves this through MoonPay/Transak [?], but it's not highlighted as a UX priority.
*Data: [aarrr.md: Activation — "Fiat first"] · [competitive-analysis.md: open question 1]*

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
| Q8 | NEW: Should we add sports markets at MVP? | Sports = 89% of Kalshi revenue, 60%+ of Polymarket open interest. Without sports, volume floor may be too low for sustainability. | NEW OPEN QUESTION |
| Q9 | NEW: Fee on win vs fee per trade? | Industry moved to fee-per-trade (Polymarket March 2026, DraftKings Dec 2025). Fee on win is psychologically softer but earns less per trade. | NEW OPEN QUESTION |

---

*Compiled from: [product-model.md](./product-model.md) - [aarrr.md](./aarrr.md) - [competitive-analysis.md](./competitive-analysis.md) - [benchmark-trust.md](./benchmark-trust.md) - [ux-patterns.md](./ux-patterns.md) - [research.md](./research.md)*
*Screenshots: `research/screens/` (26 files, including 5 new from v_refresh: DraftKings Predictions, Azuro, Bet365, eToro, Betfair Predicts)*
*v_refresh sources: [Kalshi 2025 revenue](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) - [Polymarket fee docs](https://docs.polymarket.com/trading/fees) - [Polymarket $1M/day](https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html) - [DraftKings Predictions](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Betfair Predicts](https://www.casino.org/news/betfair-eyes-prediction-market-growth-with-betfair-predicts/) - [Manifold stats](https://manifold.markets/stats)*
