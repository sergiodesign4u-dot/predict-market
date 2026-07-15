# Lean UX Canvas - Prediction Market Platform

> Framework: Jeff Gothelf, Lean UX Canvas v2.
> One-page view of the strategy. This is a compile, not a new source: every block is pulled from existing research and cites where it comes from. The narrative detail lives in [research.md](./research.md); this canvas is the assumptions-first summary a team can read in one pass.
> No new facts are introduced here. Target metrics are hypotheses until validated post-launch. Unknown values are marked [?].

---

## 1. Business problem

No prediction market has solved onboarding for the ordinary, non-crypto user outside the US. Polymarket is a CLOB on Polygon reached through MetaMask or 8+ wallet icons (cognitive overload at signup). Kalshi is clear and trusted but US-only, on a CFTC licence we cannot replicate. Futuur is the closest structural analog (global, crypto+fiat, no US regulation) and scores worst on trust in our benchmark (14/40). Across all competitors the same four gaps stay open: nobody explains why the price is what it is, markets sit isolated from the news that drives them, funds-protection copy is buried or absent, and the post-resolution moment (especially a loss) is undesigned.

The business problem: capture the global non-US, non-MiCA "middle" (Latin America, Southeast Asia, Middle East, non-EU Eastern Europe) by being the most understandable and most trustworthy prediction market for a user who follows the news but does not hold a crypto wallet, before an incumbent (Polymarket relaunched, Betfair Predicts, DraftKings Predictions) closes the clarity gap.

*Source: [research.md](./research.md) §1 Introduction (What We're Solving) and §4 Competitors (What's Missing gap table); [competitors.md](./competitors.md).*

---

## 2. Business outcomes

Measurable goals. All targets are hypotheses to validate after MVP launch.

| # | Outcome | Metric | Target (hypothesis) |
|---|---|---|---|
| O1 | Trusted prediction market for non-US audiences | MAU, NPS, 30-day retention | NPS > 40, D30 retention > 15% |
| O2 | First-bet activation achievable without prior crypto experience | % of no-prior-wallet users who complete a first bet | > 40% first bet within 24 hrs |
| O3 | An engaged base around events, not just a trading pool | DAU/MAU ratio, shares per user | DAU/MAU > 0.25 |
| O4 | Trading volume sufficient for a fee-based business | Monthly volume, revenue per active user | Monthly volume > $[?] (validate post-launch) |

Status carried from the research: O1 and O2 confirmed as the real, unserved gap; O3 challenged (Manifold proved community mechanics alone do not retain, so "engaged" must be defined through events + stakes + resolution); O4 challenged (Kalshi earns 89% of fee revenue from sports, so an events-first launch accepts a lower near-term volume ceiling as the deliberate trade-off for scope and clarity).

*Source: [research.md](./research.md) §2 Strategy - Objectives O1-O4 (folded from the retired strategy.md).*

---

## 3. Users

Three segments, one primary.

- **News Junkie (PRIMARY), 25-40.** Follows politics, geopolitics, tech; has an opinion on everything; not necessarily into crypto; smartphone-first. Pain: nowhere to put money on an opinion simply and legally, a crypto wallet is a barrier, existing markets feel like trading platforms. This is the segment no global competitor owns, and the reason for the whole product. Persona: Alex.
- **Crypto Native (SECONDARY), 22-35.** Already in Web3, has MetaMask, understands DeFi and AMM. Faster to activate, smaller but higher-quality early traffic, reachable via crypto media and X. Our edge here is now market selection and context quality, not onboarding simplicity (Polymarket embedded wallets closed most of that gap). Persona: Dan.
- **Crossover Bettor (POST-MVP), 28-42.** Bets on sports today, wants markets where analysis beats luck. Deferred because it needs sports markets, which are out of MVP scope. Persona: Maria.

Note: the addressable base is the non-US, non-MiCA middle. EU MiCA enforcement (July 2026) geo-blocks Curacao-licensed platforms in FR, DE, NL, PL, BE, so European targeting is out at launch.

*Source: [research.md](./research.md) §2 Strategy - Audience Segments (folded from the retired strategy.md); personas.md (Alex, Dan, Maria).*

---

## 4. User outcomes and benefits

What the user is trying to make progress on, in JTBD language. The main job is the reason the product exists; the functional jobs are the steps to it; emotional and social jobs sit on top of every step.

- **MJ (main job).** When an event I follow nears its outcome, I want a real stake in the result, so it is not just news but my personal participation with real consequences. Persona: Alex.
- **FJ1 - find it in time.** Find the event among active markets while the topic is still live.
- **FJ2 - understand the number.** See the probability and understand why the market reads it that way and what could move it, so I decide consciously, not blind. This is the one confirmed differentiator: no competitor closes it.
- **FJ3 - deposit without crypto.** Put money in with ordinary money, no unfamiliar technology, so the barrier is the event, not the infrastructure. The main drop-off point.
- **FJ4 - know my money is safe.** Get a clear answer to "what happens to my funds" before I deposit, so my risk is the event, not the platform.
- **FJ5 - survive the first loss.** When I lose, understand what happened and see one honest next step, so I leave feeling it was fair, not chasing the loss.
- **EJ1 / EJ3 (emotional).** Feel I understand the world better than most when I am right; leave a loss having learned something, not wanting to win it back.
- **SJ1 / SJ2 (social).** Show people I called it; build a public, verifiable track record so "the one who gets it" is a fact, not a claim.

The three MVP-core jobs (Alex-critical and unserved by the market): FJ2, FJ3, FJ5+EJ3.

*Source: [jtbd.md](../../user-research/docs/jtbd.md) - MJ, FJ1-FJ5, EJ, SJ, and the "3 jobs in MVP core" conclusion.*

---

## 5. Solutions

MVP scope: the features we believe deliver those user outcomes and drive the business outcomes.

**Core UX pattern - Story-driven Discovery.** Each event is a narrative unit: context + why it matters + what the market says + resolution conditions + YES/NO. Chosen because it aligns directly with the MJ, closes the confirmed competitor gap (FJ2), and builds trust through content transparency instead of regulatory badges we cannot hold. Return-visit surface shifts to an Event Feed once there are > 30 active markets and the user has placed a first bet.

**Product decisions (decided, not hypotheses):**
- **D1 - Market mechanism: AMM (not CLOB).** Instant liquidity at any bet size from day 1; a $1 bet fills like a $1,000 bet. CLOB's thin cold-start orderbook would produce the worst first impression (bet placed, not filled). LMSR-style or constant-product pool per market.
- **D2 - Resolution: team multisig for MVP, on-chain oracle as target.** Every resolution documented publicly (source + criteria written before the market opens + team signature). UMA-style token-holder governance explicitly rejected: whale manipulation is the #1 Trustpilot complaint on Polymarket.
- **D3 - Geography: English-first global, Brazil as first localized market.** Accessible to all non-blocked geographies from day 1 via Transak (169 countries). Brazil localization (PT-BR + PIX) at month 2-3; priority stack Brazil, UAE, Philippines, Mexico, Turkey. Avoid Indonesia and Vietnam (active enforcement).

**Supporting MVP features:** fiat on-ramp on the first screen after registration (Transak primary, MoonPay fallback); one-line funds-protection promise on the deposit screen; exact fee shown before every confirmation; a designed post-resolution loss screen and a friction-aware win screen; auto-generated share card after resolution; public prediction track record; $1 technical minimum bet with a $5 default pre-fill and $5/$10/$25/$50 quick-select.

*Source: [research.md](./research.md) §2 Strategy - Product Decisions (D1-D3) and §6 UX Patterns (Story-driven Discovery); §10 for on-ramp, KYC, and bet-size detail.*

---

## 6. Hypotheses

Format: We believe [business outcome] will be achieved if [user] attains [benefit] with [feature]. Derived from research.md §7 hypotheses H1-H6.

- **H1.** We believe first-bet activation (O2, > 40% within 24 hrs) will be achieved if the News Junkie attains the ability to go from card to first bet without a crypto wallet with a fiat on-ramp on the first screen after registration.
- **H2.** We believe higher new-user-to-first-bet conversion than Polymarket or Kalshi (O2) will be achieved if the News Junkie attains an understanding of why the odds read as they do before betting with a story-driven event unit (context + what the market says + resolution conditions).
- **H3.** We believe lower early churn after the first bet (O1) will be achieved if the new bettor attains a first bet that does not feel taxed at entry with a 0% fee entry category (politics/geopolitics) inside the decided Option A tiered fee model. Note: the original H3 tested "fee on winnings"; the fee decision moved to Option A (fee per trade), and the free-entry category now carries H3's "do not tax the entry" insight.
- **H4.** We believe higher deposit completion (O1, O2) will be achieved if the first-time depositor attains certainty about what happens to their money with a one-line funds-protection promise on the deposit screen ("Your USDC is held 1:1. We never lend it without your permission").
- **H5.** We believe > 20% of new users arriving via sharing (O3, referral) will be achieved if the winning bettor attains an easy way to show they called it with an auto-generated share card after every resolution.
- **H6.** We believe fewer complaints and refund requests (O1, trust) will be achieved if the bettor attains knowing the exact fee before committing with the exact fee shown before every confirmation ("The platform earns $0.40 if you win").

*Source: [research.md](./research.md) §7 Conclusions - Hypotheses H1-H6.*

---

## 7. Riskiest assumption

The single value-risk assumption the whole idea depends on. If false, no execution quality saves it.

> News Junkies (25-40, follow events, no crypto background) will deposit real money and place real bets on news events once the onboarding friction is removed. In other words: the barrier is FRICTION, not MOTIVATION.

This is a value risk, not a feasibility risk. We can build the fiat on-ramp and the story-driven UX. The open question is whether a non-gambler, non-trader adult deciding to stake money on a news event is a behavior that exists in a large enough segment to build a business on. H1 tests the friction side; this assumption tests the motivation side. Both must be true: great onboarding plus no desire to bet still equals failure.

Current evidence (honest status): §9 research substantially REFUTED the friction-only framing. Kalshi is fiat-native and still saw a 93% DAU collapse after its trigger event resolved; Manifold's play-money users did not convert when real money was offered; the documented conversion trigger is a perceived informational edge on a specific event, not ease of onboarding. Friction acts as a multiplier on already-weak motivation, not the root cause. Implication: the product must help the user feel "I know something worth staking" before the deposit step, or a smooth on-ramp only grows the under-$10 casual-experimenter cohort.

*Source: [research.md](./research.md) §2 Strategy - Riskiest Assumption (folded from the retired strategy.md) and §9 F4.*

---

## 8. First test

The least work needed to learn whether the riskiest assumption holds.

**A/B test of landing-page intent.** Drive 500-1000 News-Junkie-profile users (SEO / X, tied to a specific real election or event) to a page that explains the bet mechanics and shows a card-to-bet flow. Measure:
- % who click "I want to bet"
- % who complete the fiat deposit flow to the point of first bet
- % who return within 7 days after their first resolution

**Read the signal (first-bet completion from cold News Junkie traffic):**
- Above 20%: friction was the primary barrier and we have effectively solved it. The assumption holds enough to build on.
- 5-15%: friction plus motivation mix.
- Below 5-10%: the barrier is primarily motivation. The assumption is refuted and must be addressed before building more product.

Two metrics decide it and cannot be learned from desk research: first-bet completion rate, and day-7 retention after a first loss.

*Source: [research.md](./research.md) §2 Strategy - The Smallest Test (folded from the retired strategy.md), §7 H1 test signal, and §9 F4 revised thresholds.*

---

*Compiled from: [research.md](./research.md) (§1-§10) - [jtbd.md](../../user-research/docs/jtbd.md) - [competitors.md](./competitors.md) - [benchmark.md](./benchmark.md). Attribution: Jeff Gothelf, Lean UX Canvas v2.*
