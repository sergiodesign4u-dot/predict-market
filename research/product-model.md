# Product Model

> v_refresh - June 2026
> Changelog: Objectives section updated with Kalshi/DraftKings sports revenue evidence (Q3 challenge to events-first thesis). Segment 1 (Crypto Native) updated with Polymarket embedded wallet progress. Segment 2 (News Junkie) confirmed as primary with new evidence. AIDA channels updated. Prior version preserved below each changed section.

> Alternative source of truth. Describes WHAT we're building and FOR WHOM, how we attract attention and what actions we expect.

---

## Objectives

| # | Goal | How we measure | v_refresh status |
|---|---|---|---|
| 1 | Become the trusted platform for prediction markets outside the US | MAU, NPS, retention 30d | **CONFIRMED.** The global non-US gap remains real. Polymarket is the only scaled player here, but its trust score (19/40 in benchmark) and crypto-first UX leave room for a clearer entrant. Source: [competitive-analysis.md - trust column] |
| 2 | Make Web3 betting accessible for people without crypto experience | % of users without a prior wallet who completed their first bet | **CONFIRMED with new nuance.** Polymarket's embedded wallets (2025) reduced crypto friction, but fiat on-ramp is still a 3rd-party handoff (MoonPay/Transak). The gap is not fully closed. Source: [Polymarket vs Kalshi UX comparison 2026](https://judgemarket.com/blog/polymarket-vs-kalshi) |
| 3 | Build an engaged community around events | DAU/MAU ratio, shares per user | **CHALLENGED.** Manifold (community-first) returned to play-money-only in March 2025 after its real-money experiment failed to retain users. Community does not equal revenue. We need to define what "engaged community" means in a real-money context before treating this as an objective. Source: [Manifold Markets stats 2025](https://manifold.markets/stats) |
| 4 | Generate stable trading volume | Monthly trading volume, revenue per user | **CHALLENGED.** Kalshi's data shows 89% of 2025 fee revenue came from sports markets. Polymarket shifted to sports > 60% of open interest by October 2025. Our events-first thesis (politics, crypto, culture) targets the remaining 10-40% of volume. This is a real risk to revenue timeline. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) |

> Hypothesis added: consider an explicit objective O5 - "Launch at least one sports category in Month 3 of MVP to ensure volume floor." This is not confirmed, but the sports revenue data makes it worth deciding explicitly rather than leaving as implicit.

---

## Audience Segments

### Segment 1 - Crypto Native

| | |
|---|---|
| **Age** | 22-35 |
| **Profile** | Already in Web3. Has MetaMask or another wallet. Understands DeFi, stablecoins, AMM. Follows crypto news. |
| **Motivation** | Earn from market knowledge. Diversify activity beyond trading. |
| **Pain points** | Already knows Polymarket but wants more markets. Or doesn't trust centralized platforms. |
| **JTBD** | Use crypto knowledge to earn from predictions |

**v_refresh note:** CONFIRMED as secondary segment. Polymarket's embedded wallet UX (2025) has improved, reducing the "friction advantage" we could have offered this user. Our edge with Crypto Native is now more about market selection and community than onboarding simplicity. Source: [Polymarket vs Kalshi 2026 comparison](https://www.sportsbookreview.com/best-sportsbooks/kalshi-vs-polymarket/)

---

### Segment 2 - News Junkie

| | |
|---|---|
| **Age** | 25-40 |
| **Profile** | Actively follows the news: politics, geopolitics, tech. Has an opinion on everything. Not necessarily into crypto. |
| **Motivation** | Prove they're right. Earn from their knowledge. |
| **Pain points** | Nowhere to "put money" on their opinion simply and legally. A crypto wallet is a barrier. |
| **JTBD** | Monetize knowledge of current events without the complexity of trading |

**v_refresh note:** CONFIRMED as primary segment and differentiator. No competitor has solved this user's onboarding. Kalshi is the best at trust but US-only. Polymarket is global but crypto-first. Futuur is hybrid but small. Story-driven UX + fiat on-ramp remains our clearest opening. Source: [competitive-analysis.md - gap table]

---

### Segment 3 - Crossover Bettor

| | |
|---|---|
| **Age** | 28-42 |
| **Profile** | Already bets on sports (Bet365, 1xBet). Looking for more intellectual markets. Understands betting mechanics. |
| **Motivation** | More diverse markets. The feeling that it's skill, not just luck. |
| **Pain points** | Sports betting got boring or is blocked. Wants to bet on "serious" events. |
| **JTBD** | Find a new betting arena where analysis matters, not just luck |

**v_refresh note:** CHANGED priority upward. Sports revenue data (Kalshi 89% from sports, Polymarket sports > 60% open interest by October 2025) confirms this user converts at higher volume. If we add sports markets in MVP, this segment becomes secondary rather than post-MVP. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html)

---

## AIDA by Segment

### Attention - How we attract attention

| Segment | Channel | Message | v_refresh status |
|---|---|---|---|
| Crypto Native | Twitter/X, crypto media, Discord | "The market says 34% - what do you think? Put your money where your mouth is." | CONFIRMED. Crypto Twitter/X remains the primary discovery channel. |
| News Junkie | SEO, Twitter, news aggregators | "Who will win the election? The market already knows - and you can earn if you're right." | CONFIRMED. SEO via individual market pages remains the clearest acquisition lever. |
| Crossover Bettor | SEO, betting communities, referrals | "Betting on real events - not just sports. More markets, more skill." | UPDATED: if we add sports markets, the message shifts to "prediction markets + sports, one platform." |

### Interest - What holds attention and drives action

| Segment | What hooks them | Key element | v_refresh status |
|---|---|---|---|
| Crypto Native | Trading volume, liquidity, AMM mechanics | Technical market details, price movement chart | CONFIRMED. Volume and chart are table stakes. |
| News Junkie | Live events, current questions, explanation of mechanics | Event context + transparent explanation of how odds work | CONFIRMED. No competitor provides this. |
| Crossover Bettor | Variety of markets, clear rules, understandable payouts | Market list by category, visual percentages | CONFIRMED. Bet365 UX is their reference point. |

### Desire - What creates the desire to register and bet

| Segment | Trigger | Mechanic | v_refresh status |
|---|---|---|---|
| Crypto Native | High volume + favorable YES/NO price | Show volume and unbalanced market as an opportunity | CONFIRMED. |
| News Junkie | An event they're already discussing + simple onboarding | "Place a $10 bet right now - takes 2 minutes" | CONFIRMED. Fiat-first is the unlock. |
| Crossover Bettor | Comparison with bookmaker odds + greater transparency | Show that our odds are fairer because they're market-driven | CONFIRMED. Bet365's opaque house margin vs our transparent probability is a real message. |

### Actions - Specific actions we want to generate

| Action | Segment 1 | Segment 2 | Segment 3 |
|---|---|---|---|
| **First visit** | Come in from Twitter/X | Come in from Google | Come in from referral |
| **Registration** | Connect wallet | Google / Email | Google / Email |
| **Activation** | Deposit USDC and bet | Deposit by card and bet | Deposit by card and bet |
| **Retention** | Track price, open a new market | Bet on the next event | Browse the leaderboard |
| **Referral** | Share a market in a crypto chat | Share opinion on Twitter | Invite a friend who bets |

**v_refresh note:** Action paths are CONFIRMED. No change needed. The key tension remains: Segment 1 (wallet connect) vs Segment 2-3 (fiat card). Onboarding must serve both paths without adding friction to either.

---

## Segment Priority for MVP

| Priority | Segment | Why | v_refresh status |
|---|---|---|---|
| Primary | News Junkie | Largest potential market. Fiat on-ramp removes the barrier. Directly aligned with JTBD J2. | CONFIRMED |
| Secondary | Crypto Native | Faster to activate (already has a wallet). Smaller audience but higher quality traffic. | CONFIRMED |
| Secondary (elevated) | Crossover Bettor | Sports revenue data suggests this segment drives volume earlier than expected. Consider adding one sports category at MVP. | CHANGED from "Later / post-MVP" |

---

## Connection to AARRR

| AIDA | AARRR | Focus |
|---|---|---|
| Attention | Acquisition | SEO, Twitter, media |
| Interest | Acquisition to Activation | Onboarding, first market |
| Desire | Activation | Guided first bet, fiat on-ramp |
| Actions | Activation to Retention to Referral | First bet, notifications, share card |

---

## v_refresh Prior Version (preserved)

> Original segment priority table before refresh:
>
> | Priority | Segment | Why |
> |---|---|---|
> | Primary | News Junkie | Largest potential market. Fiat on-ramp removes the barrier. Directly aligned with JTBD J2. |
> | Secondary | Crypto Native | Faster to activate (already has a wallet). Smaller audience but higher quality traffic. |
> | Later | Crossover Bettor | Needs more markets and reputation. Better to onboard after MVP. |
