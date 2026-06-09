# AARRR Analysis - Prediction Market Platform

> v_refresh - June 2026
> Changelog: Each stage updated with evidence from the refreshed competitor analysis. Sources cited for all changed hypotheses. Prior version decisions preserved inline. Targets remain hypotheses unless marked with a source.

> Base version: Hypothetical analysis at the start of the product. Metrics and approaches require validation after MVP launch.

---

## Acquisition
*How people discover the platform and arrive for the first time*

**Channels:**
- **SEO via events** - each market = a separate page. "Who will win US elections 2026", "Will Bitcoin hit 100k" - ready landing pages with organic traffic
- **Twitter/X** - prediction markets live in this community. Primary channel for the crypto audience
- **Crypto media** - CoinDesk, Decrypt, The Block cover major markets
- **Word-of-mouth** - wins and public predictions spread organically

**v_refresh - what changed:**
- **NEW channel: sports news and sports media.** Kalshi ($263.5M in 2025, 89% sports) and Polymarket (sports > 60% open interest by October 2025) both show sports-adjacent SEO and media driving more volume than politics/crypto. If we add a sports category, sports news keywords become a real SEO vector. Source: [Kalshi 2025 revenue](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html)
- **DraftKings Predictions (launched Dec 2025) validated mainstream brand-to-prediction-market funnel.** They converted existing DFS users. Referral from sports betting communities is a real channel if we position against bookmaker opacity. Source: [DraftKings Predictions launch](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform)
- **CONFIRMED: SEO per market page remains primary.** No change to mechanics.

**Unknowns:**
- Which channel will deliver the lowest CAC [?]
- Whether we can compete with Polymarket on SEO from day one [?]
- What portion of our SEO traffic should target sports keywords vs events keywords [?]

**Metric:** `new registered users / week`

**Product decisions:**
- Each market is a standalone SEO page with meta tags and og:image showing live odds
- One-click market sharing directly from the card
- **NEW: add sports category landing pages to SEO architecture even if sports is not in MVP v1**

---

## Activation
*When the user first feels value - the "aha moment"*

**Aha moment:** the user placed their first bet and sees their position is live - price moving in real time.

**Path to first bet:**
```
Arrived > Registered > Verified email
> Connected wallet / deposited > Found a market
> Understood the mechanics > Placed a bet <- aha moment
```
Every step = drop-off. Competitors fail exactly here.

**Hypotheses:**
- **Fiat first** - card top-up immediately, no Web3 wallet required for the first bet
- **Guided first bet** - onboarding flow: trending market > odds explanation > "bet $5?"
- **Demo bet** - stake without money to understand mechanics, then convert to a real bet

**v_refresh - what changed:**
- **CONFIRMED: fiat-first is the right call.** Polymarket's embedded wallets (2025) reduced crypto friction but still rely on MoonPay/Transak handoff. Kalshi's fiat onboarding is acknowledged as "easier for beginners" vs Polymarket. No competitor has built a fully owned fiat-to-first-bet experience. This gap remains. Source: [Kalshi vs Polymarket 2026](https://judgemarket.com/blog/polymarket-vs-kalshi)
- **UPDATED: Robinhood's "swipeys" onboarding model is the right mental framework.** Before building any screen, write 4 screens that explain value to a new user. If you can't convince on 4 screens, the product isn't ready. This is our activation design constraint. Source: [Robinhood product strategy](https://aakashgupta.medium.com/how-robinhood-hit-100b-inside-product-strategy-that-actually-works-79c5bd0c1603)
- **UPDATED: DraftKings Predictions chose a $0.01/contract flat fee.** Simpler than Polymarket's dynamic fee. May be easier to explain to new users. Consider whether our 2% fee model needs a simpler framing at the moment of activation. Source: [DraftKings Predictions fees](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform)
- **UNCHANGED: demo bet hypothesis is still unvalidated [?].** Manifold's play-money-to-real-money conversion attempt failed (sunset March 2025). This suggests play-money as an activation step may not convert. Lean toward real-money first bet with a small minimum stake instead.

**Unknowns:**
- What % of users drop off at the deposit step [?]
- Whether a demo bet increases or decreases conversion to a real bet [?] - Manifold data suggests it does not help
- Optimal minimum first bet amount - psychological anchor vs barrier [?]

**Metric:** `% of users who placed their first bet within 24 hours of registration`

**Product decisions:**
- Onboarding flow with progress bar (4 screens max, Robinhood "swipeys" model)
- Inline mechanics explanation directly in the market card
- Fiat on-ramp on the first screen after registration
- **NEW: skip demo bet - go straight to real-money first bet with minimum stake of $1-5**

---

## Retention
*Why the user comes back tomorrow, next week, next month*

**Built-in hook:** an open position - the user can't forget about the platform until the event resolves. But between the bet and the result there's an engagement gap.

**Three retention levels:**

| Stage | When | What happens | Notification |
|---|---|---|---|
| Hot | Day 1-3 | Watching odds movement | "YES price moved from 45% to 61%" |
| Warm | Day 4-14 | New event in a favorite category | "New market: Will Zelensky meet Trump?" |
| Cold | Day 15+ | Leaderboard, streak, resolution | "Your position resolved. You won $47" |

**Retention risk:** if the user lost their first bet - high chance they won't return. That's why the first market during onboarding should have the **nearest deadline** (not "end of year", but "end of this week").

**v_refresh - what changed:**
- **CONFIRMED: position monitoring is the core built-in retention hook.** Every HARD competitor (Polymarket, Kalshi, Futuur) shows a probability-over-time chart specifically because it pulls users back. Source: [competitive-analysis.md - 3 common patterns]
- **NEW INSIGHT: sports markets have naturally higher daily retention cadence.** Sports events resolve daily or weekly, not monthly. Kalshi's sports dominance (89% of revenue) is partly explained by this: sports creates daily return triggers. If we add sports, retention mechanics become easier to trigger. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html)
- **NEW: Duolingo's streak + loss-aversion model is the aspirational retention benchmark.** Daily streak = reason to return even without an open position. Loss-aversion framing ("your streak is at risk") is more powerful than reward framing. Consider a prediction streak (consecutive correct predictions) as a retention mechanic.
- **UNCHANGED: first-bet loss is the biggest churn risk.** No competitor has solved the "I lost my first bet, why return?" moment. This is our differentiation opportunity - design the post-resolution loss screen explicitly.

**Unknowns:**
- Optimal notification frequency (too many = unsubscribe) [?]
- Whether a loss brings the user back or drives them away [?]
- Whether a streak mechanic works in a market where you can only bet occasionally [?]

**Metrics:** `% of users active on day 7` and `% active on day 30`

**Product decisions:**
- Smart notifications tied to price movement and approaching deadlines
- Personalized feed based on categories where the user has already bet
- Leaderboard with weekly reset
- **NEW: explicit post-resolution screen for losses - "Here's what happened, here's a similar market to consider"**
- **NEW: prediction streak mechanic - track consecutive markets where user beat the initial odds**

---

## Revenue
*How the platform earns*

**Primary model - Trading fee on win (2%):**

| Option | When taken | Psychology |
|---|---|---|
| A: on entry | Bet $100 > $98 in play | Hurts immediately |
| **B: on win (exit)** | Won $150 > receive $147 | **Pay only when you earned** |

Recommendation: Option B - less pain, more loyalty.

**Additional sources:**

| Source | When | % | Transparency |
|---|---|---|---|
| Trading fee | On win | ~2% | Shown explicitly before confirmation |
| On-ramp | On deposit | affiliate from provider | Not our commission |

**v_refresh - what changed:**
- **CONFIRMED: Polymarket adopted dynamic taker-only fee model in March 2026** - fees by category (0.75% sports to 7% crypto at 50/50 midpoint), geopolitics free, maker rebates 20-25%. Their daily revenue crossed $1M/day after this change. This validates fee-on-trade (not just fee-on-win). Source: [Polymarket fee docs](https://docs.polymarket.com/trading/fees) and [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html)
- **CHALLENGED: our "fee on win" model.** Polymarket charges on every trade (taker fee), not just on winning. Kalshi charges on contract purchase. DraftKings charges $0.01 per contract bought or sold. The industry has moved toward fee-per-trade, not fee-per-win. Fee-on-win is psychologically softer for users but may underperform in revenue per trade. This is a real trade-off to decide explicitly.
- **UPDATED: consider a tiered model.** Free geopolitics markets (Polymarket model) as a hook, fees on higher-volume categories (sports, crypto). Gives us a "free entry" marketing message while monetizing high-frequency users. Source: [Polymarket fee structure by category](https://docs.polymarket.com/trading/fees)
- **NEW: maker rebates as a liquidity mechanic.** Polymarket gives makers 20-25% of collected fees as daily USDC rebates. This creates a self-funding liquidity pool. Relevant for our cold-start liquidity problem. Consider from MVP launch.

**Unknowns:**
- What % delivers acceptable LTV at our CAC [?]
- At what trading volume does the platform become profitable [?]
- Fee on win vs fee on trade: which creates less churn at our scale [?]

**Metrics:** `revenue per active user / month` and `total trading volume`

**Product decision:** show the fee explicitly and honestly before bet confirmation. "Platform earns $0.40 if you win" - transparency as a competitive advantage. Consider free markets in one category (geopolitics or politics) as an entry hook.

---

## Referral
*How users bring other users*

**Built-in referral mechanic:** people naturally want to share predictions. "I told you so" - a social instinct.

**Three types of organic sharing:**

| Type | Message | When |
|---|---|---|
| Position share | "I bet $50 on YES. Market says 34%, I think everyone is wrong" | Before resolution |
| Win share | "Won $340 on the French election. Called it 3 weeks ago" | After resolution |
| Market share | "What does everyone think? Here's a market where you can put money on it" | Anytime |

**Mechanics:**

| Mechanic | How it works | Reference |
|---|---|---|
| Share card | Beautiful card with position for Twitter/Telegram | Robinhood, Spotify Wrapped |
| Referral bonus | Bring a friend > both get $5 on first bet | Fintech standard |
| Public profile | Prediction track record is open > user builds reputation | Metaculus, Manifold |
| Market embed | Any market can be embedded on a site or article | Polymarket (partially) |

**v_refresh - what changed:**
- **CONFIRMED: share card after resolution is must-have.** No change. Robinhood's confetti + shareable win card remains the benchmark. The "I told you so" instinct is universal.
- **NEW: eToro's social layer is the aspirational referral model.** eToro's CopyTrader mechanic turned user track records into a referral engine: "look how much this person made, copy their trades." Our equivalent: "look how accurate this predictor is, follow their markets." Public profile as social proof drives acquisition. Source: [eToro social trading](https://www.etoro.com/trading/social/)
- **NEW: post-win share is more valuable than pre-bet share.** Manifold's data shows community posts around resolved markets (right/wrong calls) generate more engagement than pre-market discussion. Design the post-resolution win moment for virality first.
- **CONFIRMED: referral bonus ($5 for both) is table stakes.** DraftKings DFS and Kalshi both use welcome bonuses. Not a differentiator, but the absence of one is a negative signal.

**Unknowns:**
- Which sharing channel will drive the highest conversion to registration [?]
- Whether a referral bonus justifies CAC [?]
- Whether a public prediction track record increases or decreases referral (some users prefer privacy) [?]

**Metrics:** `% of new users who came via sharing` and `viral coefficient (k-factor)`

**Product decision:** after every resolution - automatically generate a share card with the result. Win > wants to brag > free traffic. Add public profile with accuracy track record from day one - this is our eToro-style referral loop.

---

## Summary Metrics

| Stage | Key metric | Target (hypothesis) | v_refresh status |
|---|---|---|---|
| Acquisition | New registrations / week | - | Unchanged [?] |
| Activation | % first bet within 24h | >40% | Unchanged hypothesis |
| Retention | % active on day 7 | >30% | Unchanged hypothesis |
| Retention | % active on day 30 | >15% | Unchanged hypothesis |
| Revenue | Trading volume / month | - | Unchanged [?] |
| Referral | % users via sharing | >20% | Unchanged hypothesis |

*All targets are hypotheses, require validation after MVP launch.*

---

## Key Product Takeaways

1. **Activation is the biggest risk.** The long path to the first bet = primary drop-off. Fiat first + 4-screen Robinhood-style onboarding - MVP priority. Demo bet is likely counterproductive (Manifold evidence).
2. **Sports markets may be necessary sooner than planned.** Kalshi and Polymarket data both show sports driving retention and volume. Consider one sports category at MVP rather than post-MVP.
3. **Fee on trade vs fee on win is an unresolved decision.** Industry moved toward fee-per-trade. Fee on win is softer psychologically but earns less per active user. Decide before building fee logic.
4. **Post-resolution experience is undesigned in every competitor.** Loss screen + win share card are our differentiation moments. Design these before the bet flow.
5. **Referral = public track record.** eToro proved this. Users with visible prediction histories bring other users. Build public profiles from day one, not as a later feature.
