# Competitive Analysis

> v_refresh - June 2026. Restructured into three competitor groups (HARD / SOFT / ASPIRATIONAL).
> Prior version findings preserved and folded into the new structure below.

---

## Screens Index

| File | Platform | Screen | Access |
|---|---|---|---|
| `polymarket-home-mobile.png` | Polymarket | Home - market feed, categories, YES/NO cards | Public |
| `polymarket-home-scroll-mobile.png` | Polymarket | Home - scrolled, live sports markets | Public |
| `polymarket-event-detail-mobile.png` | Polymarket | Event detail - multi-outcome, chart, volume | Public |
| `polymarket-event-bet-mobile.png` | Polymarket | Bet interface - Buy Yes/No in cents | Public |
| `polymarket-signup-mobile.png` | Polymarket | Sign Up - Google + Email + 8 wallet icons | Public |
| `kalshi-home-mobile.png` | Kalshi | Home + auto-modal signup | Public |
| `kalshi-home-browse-mobile.png` | Kalshi | Home after dismissal - LIVE hero card | Public |
| `kalshi-market-detail-mobile.png` | Kalshi | Market detail - candlestick chart, price brackets | Public |
| `manifold-home-mobile.png` | Manifold | Home - question list, play money | Public |
| `manifold-market-detail-mobile.png` | Manifold | Market detail - % chance, Bet YES/NO, comments | Public |
| `futuur-home-mobile.png` | Futuur | Home - multi-outcome with probability bars | Public |
| `futuur-market-detail-mobile.png` | Futuur | Market detail - chart, outcomes | Public |
| `futuur-market-bet-mobile.png` | Futuur | Bet interface - Yes/No per outcome | Public |
| `metaculus-home-mobile.png` | Metaculus | Home - question feed, gauge charts | Public |
| `metaculus-question-detail-mobile.png` | Metaculus | Question detail - 65% gauge, Predict, comments | Public |
| `draftkings-predictions-home-mobile.png` | DraftKings Predictions | Home - featured markets, categories | Public |
| `azuro-home-mobile.png` | Azuro | Homepage - protocol pitch, B2B | Public |
| `bet365-home-mobile.png` | Bet365 | Home - live sports feed, bet slip | Public |
| `etoro-home-mobile.png` | eToro | Home - social trading, CopyTrader CTA | Public |
| `betfair-predicts-home-mobile.png` | Betfair Predicts | Marketing page - Yes/No prediction wrapper | Public |
| Portfolio / My Bets | Polymarket | Open positions, P&L | **[? behind login]** |
| Portfolio / My Bets | Kalshi | Portfolio, history | **[? behind login]** |
| Deposit flow | Polymarket | Crypto deposit, on-ramp | **[? behind login]** |
| Deposit flow | Kalshi | Fiat deposit, ACH/card | **[? behind login]** |
| Deposit flow | Futuur | Crypto + fiat choice | **[? behind login]** |
| Leaderboard | Futuur | User ranking | **[? behind login]** |
| DraftKings Predictions bet flow | DraftKings | Contract buy flow, combo builder | **[? behind login]** |

---

## Group 1 - HARD Competitors

> Same product type (prediction markets), same audience, our direct market.

| Name | Type | Why it belongs here | What to study |
|---|---|---|---|
| **Polymarket** | Crypto prediction market, CLOB on Polygon | Largest global non-US prediction market by volume ($9B+ in 2024). Our primary benchmark. Direct competitor for the Crypto Native segment. | Onboarding friction, embedded wallet UX, fee transparency, market card design |
| **Kalshi** | Fiat prediction market, CFTC-regulated | #1 by fee revenue ($263.5M in 2025). Proof that prediction markets can scale with a mainstream fiat audience. Benchmark for institutional trust and sports market dominance. | Trust signals, sports-led growth, beginner-friendly UX, fee structure |
| **Futuur** | Crypto + fiat hybrid, global | Closest structural analog to our model: supports both crypto and fiat globally without US regulation. Smaller but reveals hybrid model trade-offs. | Fiat+crypto onboarding, how the hybrid is explained to users, commission model |
| **DraftKings Predictions** | CFTC-regulated prediction market, launched Dec 2025 | Major brand (sports betting, DFS) entering prediction markets. Demonstrates mainstream onboarding to event contracts. Available in 38 US states. | Mainstream brand leverage, $0.01/contract fee model, combo mechanic |
| **Azuro Protocol** | Decentralized prediction market infrastructure (AMM, on-chain) | B2B protocol + B2C apps; shows the decentralized AMM path vs CLOB. 30+ apps on its infrastructure. Relevant for our tech architecture choice. | AMM mechanics, vAMM vs CLOB UX differences, liquidity pool model |

Sources: [Polymarket volume and fee revenue](https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html) - [Kalshi revenue 2025](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) - [DraftKings Predictions fee launch](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Azuro protocol overview](https://dappradar.com/dapp/azuro) - [Polymarket docs fees](https://docs.polymarket.com/trading/fees)

---

## Group 2 - SOFT Competitors

> Different product, but the same JTBD: "when I follow events that matter to me, I want real skin in the game."

| Name | Type | Why it belongs here | What to study |
|---|---|---|---|
| **Bet365** | Traditional sports bookmaker (fiat, global) | 80M+ registered users globally. The mental model our Crossover Bettor segment already has. Same JTBD on sports events, executed through a classic bookmaker product. | Bottom-tab nav, live betting UX, bet slip design, trust via brand and license badges |
| **Betfair Predicts** | Betting exchange + prediction market UI wrapper (beta, April 2026) | Incumbent with £84bn exchange volume in 2025 is actively wrapping its exchange in a Yes/No prediction market UX. Signals that the betting world is converging on our format. | How they translated exchange liquidity into a simpler Yes/No interface, what stayed complex |
| **eToro** | Social copy trading platform (stocks, crypto, ETFs) | 35M+ users, IPO on Nasdaq May 2025. Same JTBD for financial events: "prove I'm right about macro/crypto - and follow smart money." CopyTrader mechanic = prediction + social proof. | Social proof as a product feature, how they surface "popular opinions," trust through public listing |
| **Manifold Markets** | Play-money prediction markets | Returned to play-money-only in March 2025 after sunsetting sweepcash. Good reference for community mechanics and market creation UX - but the absence of real stakes means different motivation. | Comment/community layer, user-created markets UX, why play-money users are hard to convert to real money |
| **DraftKings DFS** | Daily fantasy sports - skill-based real-money wagering | 9M+ active users. Established brand trust, proven onboarding for real-money skill-based products. Shares the "follow events with skin in the game" loop. Users understand contracts and scoring. | How they frame skill vs luck, onboarding to first lineup/deposit, engagement notifications |

Sources: [Betfair Predicts launch](https://www.casino.org/news/betfair-eyes-prediction-market-growth-with-betfair-predicts/) - [eToro IPO May 2025](https://www.etoro.com/news-and-analysis/press-releases/etoro-leverages-ai-to-redefine-social-investing/) - [Manifold play-money sunset](https://manifold.markets/stats) - [Bet365 UX review](https://www.sportsbettingdime.com/sportsbooks/bet365/)

---

## Group 3 - ASPIRATIONAL Competitors

> International best-in-class benchmarks for mobile UX, onboarding, and trust in the fintech/crypto category.

| Name | Type | Why it belongs here | What to study |
|---|---|---|---|
| **Revolut** | Mobile-first neobank (50M+ users) | Best-in-class fintech trust UX. Trustpilot 4.7, 5 awards displayed as social proof. Onboarding in 10-15 minutes. Sets the bar for how a financial product earns trust without a traditional bank license. | Trust block on homepage (users + rating + awards), real-time transaction notifications, instant card freeze, security as a visible feature |
| **Coinbase** | Crypto exchange, Nasdaq listed | Best mainstream crypto onboarding: bank link to first trade in under 5 minutes. Nasdaq listing = institutional trust signal. Strong educational layer for new crypto users. | "Your crypto is safe here" messaging, integrated learn-to-earn, fund protection copy, verification UX |
| **Robinhood** | Retail investing, commission-free ($100B valuation) | Disrupted TradFi with one message: commission-free. Made investing accessible to first-timers. "Swipeys" onboarding method: 4 screens that must explain value before any product is built. Fee transparency as a trust mechanic (C3: 5/5 in our benchmark). | 4-screen onboarding script, plain-English errors, confetti on first trade, commission shown explicitly |
| **Cash App** | P2P payments + crypto (Square/Block) | Simplest crypto UX ever shipped: buy Bitcoin in 3 taps. Backed by Block/Square institutional trust. Set the standard for removing all friction from a financial first action. | "No jargon" copy, 3-tap buy flow, trusted brand transfer from payments to crypto |
| **Duolingo** | Language learning app (500M+ users) | Best-in-class engagement loop: daily streak, push notifications, loss-aversion mechanics, gamified progress. Prediction markets have the same retention problem (daily return after first bet). | Streak design, notification copywriting, loss-aversion framing ("don't break your streak"), habit formation |

Sources: [Revolut trust UX](https://kota.co.uk/blog/how-fintech-brands-like-revolut-and-monzo-use-ux-to-build-trust) - [Coinbase onboarding](https://builtformars.com/case-studies/how-coinbase-works) - [Robinhood product strategy](https://aakashgupta.medium.com/how-robinhood-hit-100b-inside-product-strategy-that-actually-works-79c5bd0c1603) - [Fintech UX best practices](https://www.eleken.co/blog-posts/fintech-ux-best-practices)

---

## Comparison Matrix - 5 Most Relevant Competitors

> Selected for maximum strategic range: the two largest direct competitors, one hybrid analog, one mainstream new entrant, and one SOFT benchmark.

| Axis | Polymarket | Kalshi | Futuur | DraftKings Predictions | Bet365 |
|---|---|---|---|---|---|
| **Audience** | Crypto natives, DeFi users, global (not US). Skews male 25-35, high risk tolerance. | US-first, TradFi-adjacent, mainstream. Sports bettors converting to event contracts. | Global, crypto + fiat hybrid. Smaller and less defined. | US (38 states), mainstream sports fans and bettors. DFS user base as on-ramp. | Global, 80M+ registered. Sports fans, 25-50, fiat-only, strong brand trust baseline. |
| **Product foundation** | CLOB (order book) on Polygon. USDC collateral. Conditional Token Framework. Embedded wallets reduced crypto friction. | CFTC-regulated exchange. USD fiat, ACH/card deposit. Order book matching. $263.5M fee revenue in 2025. | Crypto + fiat hybrid. Multi-currency support. Probability bars per outcome. Commission % not public [?]. | CFTC-regulated event contracts. Launched Dec 2025. $0.01 per contract fee. Combos (parlays) added May 2026. | Classic bookmaker. Decimal/fractional odds. Fiat only. 4.6/5 Play Store rating. Live streaming built in. |
| **Key mechanism** | Conditional tokens: YES/NO shares priced 0-$1. Taker fee: 0.75-7% by category (dynamic, highest at 50/50). Geopolitics free. Maker rebate 20-25%. | Order book, prices in cents (contract = $1 at resolution). Variable fee based on probability. $1.5B annualized revenue in 2026. 89% of revenue from sports. | Probability bars per outcome (multi-outcome native). Yes/No per option. Pricing mechanism not fully transparent [?]. | Event contracts at $0.01 fee each. Binary + combo (parlay) structure. Familiar sportsbook-like UX wrapping contract trading. | Fixed odds from the house. Bet slip aggregation. Cash Out feature. Acca builder. No market-discovery - the house sets prices. |
| **Trust** | On-chain transparency. UMA decentralized resolution. Volume ($9B+ in 2024, $6B+ first half 2025) as social proof. Still weak on funds protection explanation (no "where is my USDC?"). | CFTC regulation = highest institutional trust in the category. FDIC-like framing via banking partners. Auto-modal signup on entry = aggressive (friction). | Less known. Small track record. Funds protection unclear. No regulatory badge. | DraftKings brand trust (established DFS platform, publicly traded NASDAQ). CFTC regulation. New = limited track record. | 20+ year brand. Licensed in 30+ jurisdictions. Responsible gambling tools visible. Known globally - trust via recognition, not explanation. |
| **Monetization** | Taker fees by category (3-7% at 50/50 midpoint). Maker rebates. No deposit/withdrawal fees on USDC. Daily revenue crossed $1M/day April 2026. | Exchange fees variable by probability. $263.5M fee revenue 2025. No public maker rebate info. | Commission on bets [? exact % not public]. | $0.01 per contract bought or sold. Exchange fee stacked on top. "Combos" add per-leg fees. | House margin baked into odds (~4-7% across sports). Promotions + bonuses as acquisition cost. |

Sources: [Polymarket fees](https://docs.polymarket.com/trading/fees) - [Kalshi revenue](https://finance.yahoo.com/news/kalshi-fee-revenue-2025-263-145801350.html) - [DraftKings Predictions fees](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Polymarket daily revenue](https://finance.yahoo.com/markets/crypto/articles/polymarket-fee-overhaul-pushes-daily-054836739.html)

---

## 3 Common Patterns

**1. Horizontal category navigation at the top + bottom tab bar**
Every direct competitor uses the same structure: horizontal scroll categories (Trending, Politics, Crypto, Sports...) and a bottom nav with 3-5 tabs. Polymarket (4 tabs), Kalshi (4 tabs), Manifold (5 tabs), Futuur (3 tabs). Bet365 and DraftKings use the same nav pattern with sports categories. This is the de-facto genre standard across both HARD and SOFT groups. Its absence makes a platform unrecognizable.

**2. Probability percentage as the primary information element**
On every card and every detail screen, the % probability (or equivalent: price in cents, odds) is the central element. It sits above the event name, above the volume, above the deadline. It is simultaneously the "market price" and the "game state." Even Bet365 shows live odds as the dominant number on every market card. The % is the language of the genre.

**3. Probability-over-time chart**
All platforms (except Bet365, which shows current odds only) display how price/probability moved over time. From a simple line chart (Manifold) to a candlestick chart (Kalshi). Movement is engagement: users return to check if their position is "in the green." DraftKings Predictions added charting for the same reason. This pattern bridges both prediction markets and sports trading platforms.

---

## 3 Key Differences

**1. Regulation and geography define the product more than any UX choice**
Kalshi = CFTC, US fiat, highest revenue ($263.5M in 2025). Polymarket = no US users, crypto (USDC on Polygon), global. DraftKings Predictions = CFTC, 38 US states, fiat-first. The regulatory status determines which audience you can serve, which payment rails you use, and how you communicate trust. For a global non-US product, Polymarket and Futuur are the closest structural analogs. Kalshi's revenue proves the model scales - but its regulation is not replicable without a US license.

**2. Pricing mechanics split the field: CLOB vs AMM vs fixed odds**
Polymarket and Kalshi use order books (CLOB): price reflects actual matching supply and demand. Azuro uses AMM (vAMM): always liquid, but price may be worse. Bet365 uses house-set fixed odds: simplest to explain, but no "market discovery" - the house always has the edge. For our MVP from scratch, CLOB has the chicken-and-egg liquidity problem (no orders = no market); AMM avoids this but is harder to explain; fixed odds require a pricing team. This choice directly affects onboarding clarity and cold-start viability.

**3. Sports vs events: the dominant use case is splitting the sector**
Kalshi's 2025 fee revenue was 89% from sports. DraftKings Predictions is effectively a sports-adjacent product. Betfair Predicts is an exchange built on sports. The prediction market space is bifurcating into sports-first (Kalshi, DraftKings) and events-first (Polymarket, Futuur). Our thesis targets events-first (news, politics, crypto) for the News Junkie segment - this is the underserved direction, but also the lower-volume direction at present.

---

## What Is Missing Across All Competitors (our gap)

| Gap | Who suffers | Confirmed by |
|---|---|---|
| No one explains "why is the price this?" - zero in-product context for the odds | News Junkie, every new user | All competitor screens: price displayed, no explanation |
| Onboarding assumes prior knowledge of the product type | New users without prediction market experience | Kalshi auto-modal, Polymarket 8-wallet signup, Futuur no tutorial |
| Markets exist in isolation from the news that drives them | News Junkie - comes from a headline, finds a naked number | All competitor homepages: event name + %, no context |
| Trust signals are buried or absent for funds protection | New user making a first deposit | Polymarket: no "where is my USDC" explanation (trust score 19/40) |
| Loss experience is not designed for - first bet loss is a retention cliff | All new users | No competitor shows a "here's what happened, here's your next move" post-resolution screen |
| Fiat onboarding still requires 3rd-party handoffs (MoonPay, Transak) | News Junkie who has no crypto | Polymarket embeds MoonPay but does not own the experience |

---

## 3 Open Questions

**1. CLOB or AMM for MVP - and does it matter for UX?**
CLOB (Polymarket model) gives real market prices but needs liquidity from day one. AMM (Azuro model) always works but may produce a worse user price and is harder to explain honestly ("the algorithm sets the price" vs "the market sets the price"). Futuur's mechanism is unclear [?]. For a cold start with 10-20 curated markets, which is more realistic without misleading users about how pricing works?

**2. How do we build resolution trust without CFTC and without Polymarket's track record?**
Kalshi solves it through CFTC regulation. Polymarket through UMA decentralized arbitration and $9B+ of resolved volume. DraftKings through established brand equity. We have none of these at launch. Is transparent rules + team multisig + on-chain settlement enough at MVP, or does that immediately trigger "who controls this?" anxiety from users?

**3. Will sports markets be necessary for meaningful trading volume?**
Kalshi's data shows 89% of fee revenue from sports in 2025. Polymarket shifted to sports in H2 2025 (sports > 60% of open interest by October 2025). Our thesis is events-first (news, politics, crypto) - but if volume follows sports, we may face a volume floor that makes the economics unworkable unless we add sports markets earlier than planned.
