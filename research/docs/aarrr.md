# AARRR Analysis - Prediction Market Platform

> v_refresh - June 2026
> Changelog (Step 3 update, June 12, 2026): Folded in fresh competitor data (June 2026) and strategy.md insights (Riskiest Assumption, EU MiCA, tiered fee model, AI agents signal). ONE primary metric and ONE MVP decision per stage clarified. Prior version decisions preserved inline. Targets remain hypotheses unless marked with a source.

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
- **CONFIRMED: SEO per market page remains primary.** Each market = standalone SEO page with live og:image. No change to mechanics.
- **DraftKings Predictions (launched Dec 2025) validated mainstream brand-to-prediction-market funnel.** They converted existing DFS users via brand trust. Referral from sports betting communities is a real channel if we position against bookmaker opacity. Source: [DraftKings Predictions launch](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform)
- **Sports markets = post-MVP.** Kalshi data (90% of May 2026 volume from sports) confirms sports drives volume, but adding sports markets is out of MVP scope. Decision made. Source: [Kalshi volume CNBC 2026](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html)
- **EU MiCA enforcement (July 2026) is now a geo acquisition constraint.** If we operate under a Curacao-style license, we face blocks in FR, DE, NL, PL, BE. Acquisition via SEO must account for which countries traffic can actually convert. Target: Latin America, Southeast Asia, Eastern Europe (outside EU), Middle East. Source: [competitors.md - Q3 EU MiCA]
- **Industry grew 200x: ~4,000 active users (2024) to 800,000+ unique wallets/month (early 2026).** But 30%+ of trading volume is from AI agents. Human audience is smaller than headline wallet numbers suggest. Our SEO should target human News Junkies, not algorithmic traders. Source: [CoinDesk industry report 2026]

**Unknowns:**
- Which channel will deliver the lowest CAC [?]
- Whether we can compete with Polymarket on SEO from day one [?]
- Which geo regions are actually accessible post-MiCA with our expected license structure [?]

**Metric (ONE):** `new registered users / week`

**MVP Decision (ONE):** Each market is a standalone SEO page with meta tags and og:image showing live odds. One-click sharing from the market card.

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
- **CONFIRMED: no demo bet.** Manifold sunsetting sweepcash (March 2025) confirmed play-money does not convert. Go straight to real-money first bet with minimum stake of $1-5.
- **NEW: Riskiest Assumption context.** Activation is where the Riskiest Assumption is tested (see strategy.md). H1 (fiat on-ramp increases activation) tests the friction side. But the deeper risk is whether News Junkies are willing to put real money on outcomes at all - not just technically able to. If first-bet completion rate from cold News Junkie traffic is below 10%, the motivation gap exists and UX improvements alone cannot fix it.
- **NEW: Fee model for activation moment.** Tiered taker fees (Option A: 0% for some categories) may be better for activation than fee-on-win (Option B: 2% on winning payout). A "free first market" hook (like Polymarket's 0% geopolitics) reduces the psychological cost of the first bet. Consider for MVP design.

**Unknowns:**
- What % of users drop off at the deposit step [?]
- Optimal minimum first bet amount - psychological anchor vs barrier [?]
- Whether free category (0% fee) as first bet increases activation vs converting to a second paid bet [?]

**Metric (ONE):** `% of users who placed their first bet within 24 hours of registration`

**MVP Decision (ONE):** Fiat on-ramp on the first screen after registration. Skip demo bet - go straight to real-money first bet with minimum stake of $1-5. 4-screen Robinhood "swipeys" onboarding.

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
- **CONFIRMED: position monitoring is the core built-in retention hook.** Every HARD competitor (Polymarket, Kalshi, Futuur) shows a probability-over-time chart specifically because it pulls users back. Source: [competitors.md - 3 common patterns]
- **POST-MVP NOTE: sports markets have naturally higher daily retention cadence.** Sports events resolve daily or weekly, not monthly. Kalshi's sports dominance (89% of revenue) is partly explained by this. Sports = post-MVP but noting this as a retention argument for the post-MVP roadmap. Source: [Kalshi revenue breakdown](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html)
- **NEW: Duolingo's streak + loss-aversion model is the aspirational retention benchmark.** Daily streak = reason to return even without an open position. Loss-aversion framing ("your streak is at risk") is more powerful than reward framing. Consider a prediction streak (consecutive correct predictions) as a retention mechanic.
- **UNCHANGED: first-bet loss is the biggest churn risk.** No competitor has solved the "I lost my first bet, why return?" moment. This is our differentiation opportunity - design the post-resolution loss screen explicitly.

**Unknowns:**
- Optimal notification frequency (too many = unsubscribe) [?]
- Whether a loss brings the user back or drives them away [?]
- Whether a streak mechanic works in a market where you can only bet occasionally [?]

**Metric (ONE, primary):** `% of users active on day 7`

Secondary tracked: `% active on day 30`

**MVP Decision (ONE):** Smart notifications tied to price movement and approaching deadlines. Explicit post-resolution screen for losses: "Here's what happened, here's a similar market to consider."

Supporting mechanics (several allowed): personalized feed by category bet, leaderboard with weekly reset, prediction streak mechanic (consecutive correct predictions).

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

**v_refresh additional - June 12, 2026:**
- **Industry standard is now tiered taker fees (Option A), not fee on win (Option B).** Polymarket Fee V2 (March 30, 2026): 0% geopolitics to 1.80% crypto at 50/50 midpoint. Kalshi: 0.07 x p x (1-p), max ~1.75% at 50c. DraftKings: $0.01 flat per contract. Option B (fee on win) is a deliberate user-first choice that sacrifices revenue per trade for retention. Tradeoff must be explicitly decided.
- **Tiered approach unlocks "free entry" message.** 0% fee on one category = first bet has no cost. Powerful for News Junkie activation. Requires enough volume in other categories to generate revenue. Source: [Polymarket Fee V2 docs](https://docs.polymarket.com/trading/fees)

**Unknowns:**
- What % delivers acceptable LTV at our CAC [?]
- At what trading volume does the platform become profitable [?]
- Fee on win vs tiered fee per trade: which creates less churn at our user volume level [?]

**Metric (ONE):** `revenue per active user / month`

**MVP Decision (ONE):** Show the fee explicitly and honestly before bet confirmation. Fee model TBD (fee on win vs tiered per trade) - must decide before building fee logic. One free-entry category (politics or geopolitics) as activation hook.

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

**Metric (ONE):** `% of new users who came via sharing`

**MVP Decision (ONE):** Auto-generate a share card after every resolution. Public prediction track record from day one (eToro CopyTrader model - user accuracy history drives referrals).

---

## Summary Metrics (ONE primary per stage)

| Stage | Primary metric | Target (hypothesis) | v_refresh status |
|---|---|---|---|
| Acquisition | New registrations / week | - [?] | Unchanged - geo-restricted by EU MiCA from July 2026 |
| Activation | % first bet within 24h | >40% | Hypothesis. **Riskiest Assumption test: if below 10% from News Junkie cold traffic, motivation gap exists.** |
| Retention | % active on day 7 | >30% | Unchanged hypothesis |
| Revenue | Revenue per active user / month | - [?] | Fee model TBD - decide before build |
| Referral | % new users via sharing | >20% | Unchanged hypothesis |

*Secondary metrics tracked but not optimized for: Acquisition: CAC by channel; Activation: % complete deposit; Retention: % active on day 30 target >15%; Revenue: total trading volume. All primary targets are hypotheses, require validation after MVP launch.*

---

## Key Product Takeaways

1. **Activation is the biggest risk - and the Riskiest Assumption test.** Fiat first + 4-screen onboarding is the friction solution. But the deeper question is whether News Junkies will pay real money to bet - friction removal is necessary but may not be sufficient. Monitor cold-traffic first-bet rate as the primary Riskiest Assumption signal. Below 10% = motivation problem, not just friction.
2. **Sports = post-MVP. Decided. 3-month checkpoint.** Kalshi 90% of May 2026 volume from sports. Decision stands for MVP. But post-launch, add sports as a explicit 3-month checkpoint: if events-first retention validates the model, sports adds volume. If not, sports may need to come earlier.
3. **Fee model unresolved but industry direction is clear: tiered per-trade.** Option A (tiered taker fees, 0% in one category) is the 2026 standard. Option B (fee on win) is softer for users but earns less. Consider Option B for MVP + free category, then migrate to Option A with tiered pricing once volume justifies the explanation. Decide before building fee logic.
4. **Post-resolution experience is undesigned in every competitor.** Loss screen + win share card are our differentiation moments. Design these before the bet flow.
5. **Referral = public track record.** eToro proved this. Build public profiles from day one.
6. **EU MiCA from July 2026 restricts European markets.** Acquisition SEO must target accessible geos: Latin America, Southeast Asia, non-EU Eastern Europe, Middle East. Adjust market selection and copy accordingly.
