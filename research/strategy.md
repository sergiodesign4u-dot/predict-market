# Strategy

> v_refresh - June 2026
>
> Changelog:
> - Migrated from product-model.md. Structure updated: AIDA retired, Business Model added as explicit section, Riskiest Assumption added as a new section.
> - Objectives and Segments carry forward from product-model.md v_refresh (June 2026) with status updates from competitor evidence.
> - Prior file (product-model.md) preserved in place for history.
>
> This file owns: what we are trying to achieve (objectives), who we are building for (segments), how we sustain it (business model), and what must be true for any of it to matter (riskiest assumption).

---

## 1. Objectives

| # | Goal | How we measure | Target (hypothesis) | v_refresh status |
|---|---|---|---|---|
| O1 | Become the trusted prediction market platform for non-US audiences | MAU, NPS, 30-day retention | NPS > 40, D30 retention > 15% | **CONFIRMED.** The global non-US gap is real and unserved at the clarity level we target. Polymarket trust score 19/40 in benchmark. Source: [competitive-analysis.md - trust column] |
| O2 | Make first-bet activation achievable without prior crypto experience | % of users without a prior wallet who completed their first bet | > 40% first bet within 24 hrs | **CONFIRMED with nuance.** Polymarket embedded wallets (2025) reduced crypto friction but fiat on-ramp remains a 3rd-party handoff (MoonPay/Transak). The gap is not fully closed. Source: [Polymarket vs Kalshi 2026](https://judgemarket.com/blog/polymarket-vs-kalshi) |
| O3 | Build an engaged user base around events, not just a trading pool | DAU/MAU ratio, shares per user | DAU/MAU > 0.25 | **CHALLENGED.** Manifold (community-first) returned to play-money-only March 2025 after real-money experiment failed. Community mechanics alone do not retain users. "Engaged community" must be defined through events + stakes + resolution, not social features alone. Source: [Manifold Markets stats 2025](https://manifold.markets/stats) |
| O4 | Generate trading volume sufficient for a sustainable fee-based business | Monthly trading volume, revenue per active user | Monthly volume > $[?] (to validate post-launch) | **CHALLENGED.** Kalshi 2025 data shows 89% of $263.5M fee revenue from sports. Our events-first thesis (politics, crypto, culture) targets the remaining 10-40% of volume. Lower initial volume ceiling is the deliberate trade-off for reduced scope and clarity at launch. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) |

---

## 2. Audience Segments

### Segment 1 - News Junkie (PRIMARY)

| Attribute | Detail |
|---|---|
| **Age** | 25-40 |
| **Profile** | Actively follows the news: politics, geopolitics, tech. Has an opinion on everything. Not necessarily into crypto. Smartphone-first. |
| **Motivation** | Prove they are right. Earn from knowledge of current events. |
| **Pain** | Nowhere to "put money" on their opinion simply and legally. A crypto wallet is a barrier. Existing prediction markets feel like trading platforms, not event-following platforms. |
| **JTBD** | Monetize knowledge of current events without the complexity of trading. |
| **Priority** | PRIMARY |
| **Reason** | Largest potential market. Fiat on-ramp removes the single biggest barrier (no crypto wallet). Directly aligned with JTBD J2. No competitor has solved this user's onboarding globally outside the US. |

**v_refresh status:** CONFIRMED as primary segment and differentiator. Kalshi solves trust but US-only. Polymarket is now global + US (relaunched December 2025) but still crypto-first despite embedded wallets. Futuur is hybrid but underpowered on trust (14/40 in benchmark) and shows no 2026 growth signals. Story-driven UX plus fiat on-ramp is our clearest opening.

**EU MiCA note:** EU MiCA enforcement activates July 2026. If we operate under a Curacao license (like Futuur), we face geo-blocks in FR, DE, NL, PL, BE - covering major European markets. The global non-EU, non-US "middle" (Latin America, Southeast Asia, Africa, parts of Eastern Europe) becomes our actual addressable market at launch. This should be explicit in segment targeting, not assumed. Source: [competitive-analysis.md - EU MiCA open question Q3]

---

### Segment 2 - Crypto Native (SECONDARY)

| Attribute | Detail |
|---|---|
| **Age** | 22-35 |
| **Profile** | Already in Web3. Has MetaMask or another wallet. Understands DeFi, stablecoins, AMM. Follows crypto news. |
| **Motivation** | Earn from market knowledge. Diversify activity beyond trading. Find more markets than Polymarket offers. |
| **Pain** | Already knows Polymarket but wants more curated markets. Skeptical of centralized platforms. |
| **JTBD** | Use crypto knowledge to earn from predictions. |
| **Priority** | SECONDARY |
| **Reason** | Faster to activate (already has a wallet). Smaller audience but higher quality early traffic. Easier to reach via crypto media and Twitter/X. |

**v_refresh status:** CONFIRMED as secondary. Polymarket embedded wallets (2025) improved, reducing the friction advantage we could have offered this user. Our edge with Crypto Native is now market selection and context quality, not onboarding simplicity. Source: [Polymarket vs Kalshi 2026 comparison](https://www.sportsbookreview.com/best-sportsbooks/kalshi-vs-polymarket/)

---

### Segment 3 - Crossover Bettor (POST-MVP)

| Attribute | Detail |
|---|---|
| **Age** | 28-42 |
| **Profile** | Already bets on sports (Bet365, 1xBet). Looking for more intellectual markets. Understands betting mechanics. |
| **Motivation** | More diverse markets. The feeling that it is skill, not luck. |
| **Pain** | Sports betting got boring or is blocked. Wants to bet on "serious" events where analysis matters. |
| **JTBD** | Find a new betting arena where analysis matters, not just luck. |
| **Priority** | POST-MVP |
| **Reason** | Sports markets are scope out of MVP. Kalshi sports revenue data confirms this segment drives volume, but adding sports markets exceeds solo-team MVP scope. Revisit after launch with real retention data. |

**v_refresh status:** CONFIRMED as post-MVP. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html)

---

## 3. Business Model

**How the product earns and sustains itself.**

### Value Exchange

Users bring capital and knowledge. The platform provides the event markets, resolution mechanism, and the infrastructure for trade. The platform earns a share of every resolved trade as a fee.

- User wins: earns back their stake plus upside, minus platform fee
- User loses: platform does not take a fee on the losing side (option B - fee on win only) OR platform takes fee on every trade regardless of outcome (option A - fee per trade, industry standard as of 2026)
- Platform earns on volume, not on house edge - there is no house position

### Fee Model Options (unresolved - decide before building fee logic)

| Option | When taken | Psychology | Industry examples |
|---|---|---|---|
| A: tiered taker fee per trade | On every buy/sell, rate by category | Feels like a cost to participate, but variable rates allow "free" entry in low-risk categories | Polymarket Fee V2 (March 30, 2026): 0% geopolitics to 1.80% crypto at 50/50 midpoint. DraftKings: $0.01/contract. Kalshi: 0.07 x p x (1-p), max ~1.75% at 50c. |
| **B: fee on win** | On winning payout only | "Pay only when you earned" - softer psychologically | Our original model, no direct competitor using this in 2026 |

**Current industry direction:** Option A (tiered taker fee per trade) is the 2026 industry standard across all three major HARD competitors. Polymarket Fee V2 (March 30, 2026) tiered by category - the "geopolitics free" tier is an acquisition lever AND a proof of concept for category-tiered pricing. Maker rebates (20-25% of collected fees) are now standard on Polymarket and Kalshi - this creates liquidity incentives we should plan for.

**Key insight from fresh research:** Polymarket's daily revenue crossed $1M/day after the Fee V2 launch but volume has since declined. Kalshi's formula (0.07 x p x (1-p)) is elegant: fees are higher near 50/50 (genuine uncertainty, higher value to both sides) and lower near 0 or 100 (near-resolved market).

**Hypothesis:** Start with option B (fee on win, ~2%) as the softer entry to build trust with the News Junkie segment who has no prior prediction market experience. Revisit for tiered Option A once volume is established. Consider one free category (geopolitics or politics) as Polymarket does, to give a "no risk" entry message.

**Decision required before MVP build:** fee on win vs fee per trade.

### Pricing Hypothesis

| Fee | Rate | Notes |
|---|---|---|
| Trading fee | ~2% on win (Option B) or ~1-3% per trade (Option A) | To validate against competitor data and user tolerance |
| On-ramp fee | Passed through from provider | Affiliate from MoonPay/Transak/Stripe, not our commission |

### Free vs Paid Split

No subscription. No account tiers at MVP. Fee only applies to resolved bets (Option B) or active trades (Option A).

**Potential hook:** free markets in one category (geopolitics or politics) as an acquisition lever - Polymarket's geopolitics-free category model is referenced. This gives a "no fee" entry message while monetizing higher-frequency users. Consider from launch.

### No Min/Max Bet Limits at Launch

Following Polymarket's $0.01 minimum as a reference point. Actual minimum to be decided (lean $1-5 as psychological anchor without being a real barrier).

---

## 4. Riskiest Assumption

**The single assumption the whole idea depends on. If false, the idea fails regardless of execution quality.**

### The Assumption

> News Junkies (25-40, follows events, no crypto background) will deposit real money and place real bets on news events once the onboarding friction (fiat barrier, crypto complexity) is removed.

In other words: the barrier is **friction**, not **motivation**.

If this is false - if News Junkies are fundamentally unwilling to put real money on event outcomes even with a simple card-to-bet flow - then no amount of UX improvement, story-driven content, or fiat on-ramp fixes the product.

### Why This Is the Riskiest Assumption

This is a VALUE risk, not a feasibility risk. We can build the fiat on-ramp. We can build the story-driven UX. The question is whether the core behavior - a non-gambler, non-trader adult deciding to bet money on a news event - is a behavior that exists in a large enough segment to build a business on.

The competitive evidence is mixed:
- Polymarket exists and has volume, but its users skew crypto-native (they already accept financial risk in DeFi)
- Kalshi has real mainstream money but in the US, with CFTC regulation providing a trust scaffold we cannot replicate
- Manifold tried play-money as a gateway to real-money and failed (shut down sweepcash March 2025)
- Betfair Predicts and DraftKings Predictions are both entering the space in 2026, which signals incumbents believe demand exists - but their users already have sports betting habits

The missing data point: a non-US, non-crypto, non-gambling user who specifically wants to monetize their opinion on political/cultural/news events. This user is hypothesized but not confirmed at scale.

**Fresh research note (June 2026):** Industry monthly active users grew from ~4,000 (2024) to 800,000+ unique wallets (early 2026) - a 200x increase. But 30%+ of trading volume on major platforms is now from AI agents, not human users. This means much of the "user growth" may be algorithmic, not the human News Junkie we are targeting. The human user base for prediction markets may be smaller than top-line wallet numbers suggest. Source: [CoinDesk industry report 2026]

### The Smallest Test

**A/B test of landing page intent:** Drive 500-1000 "News Junkie" profile users (from SEO / Twitter for a specific election/event) to a page that explains the bet mechanics and shows a card-to-bet flow. Measure:
- What % click "I want to bet"
- What % complete the fiat deposit flow to the point of first bet
- What % return within 7 days after their first resolution

If activation (% first bet within 24 hrs) exceeds 20% from cold traffic on a real news event, the assumption holds enough to build on. If it is below 10%, the motivation gap is real and must be addressed before building more product.

### Relationship to Hypotheses (from master-research.md)

The Riskiest Assumption is the underlying condition for H1 (fiat on-ramp increases activation). H1 tests the friction side. The riskiest assumption tests the motivation side. Both must be true.

- H1 true + RA true = product works
- H1 true + RA false = great onboarding, no one wants to bet = failure
- H1 false + RA true = motivated users blocked by friction = fixable
- H1 false + RA false = both broken = start over

**The RA is the harder and more dangerous assumption to be wrong about.**

---

## Segment Priority Summary

| Priority | Segment | JTBD | Why |
|---|---|---|---|
| Primary | News Junkie | Monetize knowledge of current events simply | Largest potential market, fiat removes barrier, no global competitor owns this user |
| Secondary | Crypto Native | Use crypto knowledge to earn from predictions | Faster to activate, early quality traffic, crypto-native distribution |
| Post-MVP | Crossover Bettor | New betting arena where analysis matters | Needs sports markets, scope exceeds MVP, revisit after launch data |
