# Competitive Analysis

> v_refresh - June 2026. Restructured into three competitor groups (HARD / SOFT / ASPIRATIONAL).
> Updated June 12, 2026 with fresh web research: Hyperliquid HIP-4 added to HARD group (launched May 2, 2026); Azuro removed from HARD (no 2026 data, retained as tech-reference note). Polymarket: volume declining, US relaunch complete, ICE $2B investment at $9B valuation. Kalshi: now volume leader ($17.9B May 2026), $22B Series F valuation (May 2026). EU MiCA enforcement active July 2026 - new geo question for our platform. Key numbers updated throughout.
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
| **Polymarket** | Crypto prediction market, CLOB on Polygon | Formerly the largest non-US prediction market ($21.5B volume in 2025). Now declining: volume fell to $7.1B in May 2026 after Kalshi overtook it. Relaunched in the US in December 2025 with a CFTC license (QCEX infrastructure, 0.30% flat fee for US users). $2B investment from ICE (NYSE parent) at $9B valuation. Fee V2 launched March 30, 2026: tiered taker fees by category (0% geopolitics to 1.80% crypto). Primary benchmark for crypto-native UX. | Fee V2 mechanics by category, US relaunch UX, embedded wallet post-ICE, insider trading trust issue |
| **Kalshi** | Fiat prediction market, CFTC-regulated, now the volume leader | Overtook Polymarket in April 2026 ($5.42B vs $1.99B). May 2026: $17.9B volume. $1B Series F at $22B valuation (May 2026); investors include Coatue, Sequoia, a16z, Paradigm, Morgan Stanley, ARK Invest. Annualized revenue $600M-700M. 90% of volume from sports. 150+ insider trading investigations in Q1 2026. Building institutional "Bloomberg Terminal" interface. | Sports-led growth model, institutional trust building, insider trading governance, fee structure at scale |
| **Futuur** | Crypto + fiat hybrid, global (Curacao license) | Closest structural analog to our model: AMM, USDC, no US/UK/AU/FR/ES/NL users. 1,000+ live markets. No 2026 funding or major feature announcements found. Stagnant growth signals. Still the most relevant reference for a global, non-regulated, hybrid platform - including what NOT to do on trust. | Hybrid onboarding explanation, trust gap (14/40 in benchmark), commission model, what stagnation looks like |
| **DraftKings Predictions** | CFTC-regulated prediction market, US only | $1.3B annualized consumer volume in May 2026 (up 24% MoM). Launched Combos (parlay-style multi-event bundles) May 11, 2026. Building in-house exchange "Railbird." Part of a "Super App" merging sportsbook + predictions + iGaming. 38 US states. Investing $200-300M in 2026. | Super App integration, Combos mechanic UX, fiat-first onboarding, brand leverage to prediction markets |
| **Hyperliquid HIP-4** | Zero-fee on-chain prediction market, launched May 2, 2026 | New entrant with explicit zero-fee strategy as attack on Polymarket and Kalshi. Fully on-chain binary and multi-outcome contracts. First 24h: 6.05M contracts. Integrates natively with Hyperliquid perps/spot wallet - structurally closest analog to our Web3 AMM vision. Small but growing and directly competes on fees. | Zero-fee sustainability model, integration with existing DeFi wallet, cold-start liquidity approach, whether "free" is a moat or a trap |

> Note on Azuro Protocol: Removed from HARD group due to no 2026 updates or public data. Azuro remains relevant as a tech-architecture reference (decentralized vAMM, 30+ apps on its infrastructure) but is not an active UX competitor we can study. Referenced in Q1 (CLOB vs AMM decision) below.

Sources: [Polymarket Fee V2 docs](https://docs.polymarket.com/trading/fees) - [Polymarket volume decline](https://bitcoinnews.com/bitcoin-trading/polymarket-trading-volume-decline-2026/) - [Kalshi Series F $22B](https://sacra.com/research/kalshi/) - [Kalshi volume leader April 2026](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html) - [DraftKings Predictions Combos](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Hyperliquid HIP-4 launch](https://bitcoinnews.com/defi/hyperliquid-hip-4-prediction-markets-2026/) - [Polymarket ICE investment](https://financialcontent.com/marketscreener/polymarket-ice-investment-2026)

---

## Group 2 - SOFT Competitors

> Different product, but the same JTBD: "when I follow events that matter to me, I want real skin in the game."

| Name | Type | Why it belongs here | What to study |
|---|---|---|---|
| **Bet365** | Traditional sports bookmaker (fiat, global) | 80M+ registered users globally. The mental model our Crossover Bettor segment already has. Same JTBD on sports events, executed through a classic bookmaker product. | Bottom-tab nav, live betting UX, bet slip design, trust via brand and license badges |
| **Betfair Predicts** | Betting exchange + prediction market UI wrapper (beta, April 2026) | Incumbent with £84bn exchange volume in 2025 is actively wrapping its exchange in a Yes/No prediction market UX. Signals that the betting world is converging on our format. | How they translated exchange liquidity into a simpler Yes/No interface, what stayed complex |
| **eToro** | Social copy trading platform (stocks, crypto, ETFs) | 35M+ users, IPO on Nasdaq May 2025. Same JTBD for financial events: "prove I'm right about macro/crypto - and follow smart money." CopyTrader mechanic = prediction + social proof. | Social proof as a product feature, how they surface "popular opinions," trust through public listing |
| **Manifold Markets** | Play-money prediction markets | Returned to play-money-only in March 2025 after sunsetting sweepcash. Good reference for community mechanics and market creation UX - but the absence of real stakes means different motivation. | Comment/community layer, user-created markets UX, why play-money users are hard to convert to real money |
| **DraftKings DFS** | Daily fantasy sports - skill-based real-money wagering (distinct from DraftKings Predictions which is in HARD) | 9M+ active users. Established brand trust, proven onboarding for real-money skill-based products. Shares the "follow events with skin in the game" loop. Users understand contracts and scoring. | How they frame skill vs luck, onboarding to first lineup/deposit, engagement notifications |

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
| **Audience** | Crypto natives, DeFi users, global + US (relaunched Dec 2025). ~840K monthly unique wallets (Feb 2026). High risk tolerance. 30%+ of trading from AI agents. | US-first, TradFi-adjacent, mainstream. Sports bettors + growing institutional layer. Bloomberg Terminal interface in development. | Global, crypto + fiat hybrid. Smaller and less defined. Same geo-blocks. No growth signals in 2026. | US (38 states), mainstream sports fans. DFS base as on-ramp. Part of sports betting super app. | Global, 80M+ registered. Sports fans, 25-50, fiat-only, strong brand trust baseline. |
| **Product foundation** | CLOB on Polygon. USDC collateral. Conditional Token Framework. Embedded wallets. US relaunch via QCEX infrastructure (Dec 2025). $2B investment from ICE (NYSE parent) at $9B valuation. | CFTC-regulated exchange. USD fiat, ACH/card deposit. Order book matching. $1B Series F at $22B valuation (May 2026). $600-700M annualized revenue. Sports = 90% of volume. | Crypto + fiat hybrid. AMM model. USDC support. Curacao license. 1,000+ live markets. No recent updates or new funding. | CFTC-regulated event contracts. $1.3B annualized consumer volume (May 2026, up 24% MoM). Building in-house exchange "Railbird." $200-300M investment in 2026. | Classic bookmaker. Decimal/fractional odds. Fiat only. 4.6/5 Play Store. Live streaming built in. |
| **Key mechanism** | Conditional tokens: YES/NO shares priced 0-$1. Fee V2 (March 30, 2026): tiered taker fee 0% (geopolitics) to 1.80% (crypto) at 50/50 midpoint. Maker rebate 20-25%. Volume declining: ~$7.1B May 2026, down from $10.5B peak. | Order book, prices in cents. Fee: 0.07 x p x (1-p), max ~1.75% at 50c. 89% of revenue from sports. $17.9B volume May 2026 (new leader). 150+ insider trading investigations Q1 2026. | Probability bars per outcome (multi-outcome native). AMM-based. Pricing mechanism not fully transparent [?]. | Event contracts. $0.01 per contract each side + exchange fee. Combos (parlay-style bundles) launched May 11, 2026. Familiar sportsbook UX wrapping contract trading. | Fixed odds from the house. Bet slip aggregation. Cash Out. Acca builder. House always sets prices. |
| **Trust** | On-chain transparency. UMA resolution. ICE ($9B valuation) adds institutional credibility. Volume ($21.5B in 2025) as social proof. US CFTC license now held. Insider trading complaint filed June 2026. Weak on "where is my USDC?" copy. | CFTC = highest institutional trust. Banking partners. $22B valuation + blue-chip VCs (Sequoia, a16z, Paradigm, Morgan Stanley). Employer-disclosure required for high-risk markets. Strong but US-only. | No regulatory badge. No notable investors. Funds protection unclear. Benchmark score: 14/40 - worst in our trust scorecard. Shows the floor of global, unregulated, hybrid. | DraftKings brand (publicly traded NASDAQ). CFTC regulation. Young product (Dec 2025), limited track record. | 20+ year brand. Licensed in 30+ jurisdictions. Responsible gambling tools visible. Trust through recognition. |
| **Monetization** | Tiered taker fees by category: 0% geopolitics, ~0.80% politics, ~1.80% crypto at 50/50 midpoint. Maker rebates 20-25%. US users: flat 0.30% taker fee. Volume declining in 2026. | Variable fee formula: 0.07 x p x (1-p). $600-700M annualized revenue run rate (May 2026). 90% from sports. | Commission on bets [? exact % not public]. | $0.01 per contract each side + exchange fee per trade. Combo legs add per-leg fees. $1.3B annualized consumer volume. | House margin ~4-7% baked into odds. Promotions as acquisition cost. |

Sources: [Polymarket Fee V2 docs](https://docs.polymarket.com/trading/fees) - [Polymarket declining volume](https://bitcoinnews.com/bitcoin-trading/polymarket-trading-volume-decline-2026/) - [Kalshi $22B valuation May 2026](https://sacra.com/research/kalshi/) - [Kalshi volume leader April 2026 CNBC](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html) - [DraftKings Combos May 2026](https://www.gamblinginsider.com/news/159764/draftkings-combos-fee-structure-predictions-platform) - [Polymarket ICE $9B](https://financialcontent.com/marketscreener/polymarket-ice-investment-2026)

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

**1. US market is now saturated - global non-US is our defensible position**
As of June 2026, there are 13 federally regulated US prediction market platforms (DraftKings, FanDuel Predicts, Fanatics Markets, Robinhood, Gemini Predictions, OG.com, Sporttrade, Pariflow, and others). Polymarket even relaunched in the US (December 2025) with a CFTC license. The US market is locked behind regulation and already crowded. For a new entrant without US regulatory infrastructure, the global non-US market (where Futuur operates without quality) is the only viable lane. This confirms our strategic positioning. Source: [MetaMask News - 13 US regulated platforms](https://metamask.io/news/prediction-markets-us-2026/)

**2. Pricing mechanics split the field: CLOB vs AMM vs fixed odds - and now zero-fee on-chain**
Polymarket and Kalshi use order books (CLOB): price reflects actual matching supply and demand. Azuro uses AMM (vAMM): always liquid, but price may be worse. Bet365 uses house-set fixed odds: simplest to explain, but no "market discovery." Hyperliquid HIP-4 (May 2026) adds a fourth model: zero-fee on-chain binary contracts integrated into an existing DeFi wallet. For our MVP from scratch, CLOB has the chicken-and-egg liquidity problem; AMM avoids this but is harder to explain; zero-fee is not sustainable without alternative monetization. This choice directly affects onboarding clarity and cold-start viability.

**3. Sports vs events: bifurcation is accelerating, events-first window is shrinking**
Kalshi's May 2026 volume was 90% from sports ($17.9B, the new monthly record). Polymarket sports is 39%+ of open interest as of 2026. DraftKings Predictions, Betfair Predicts, FanDuel Predicts are all sports-focused. The prediction market space is bifurcating into sports-first (Kalshi, DraftKings, FanDuel, Betfair) and events-first (Polymarket's original positioning, Futuur). Our events-first thesis targets the underserved direction - but this direction has lower near-term volume. World Cup 2026 identified as a $5-10B catalyst (Bernstein). Decision: sports post-MVP stands, but events-first launch means accepting a lower volume ceiling while the sports wave grows around us. Source: [Kalshi volume leader CNBC 2026](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html)

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
| No platform explicitly serves the global non-EU, non-US market with clear jurisdiction transparency | News Junkie outside US and EU | EU MiCA enforcement (July 2026) is making Europe more restricted; 13 US regulated platforms crowd US. Global middle (Latin America, Southeast Asia, Africa) is unaddressed. |
| Insider trading risk is unaddressed by any non-regulated platform | All users | Kalshi launched investigations, employer-disclosure, whistleblower tools. Polymarket faced CFTC complaint. Unregulated platforms have no mechanism for this at all. |

---

## 3 Open Questions

**1. CLOB or AMM for MVP - with Hyperliquid zero-fee as a third option**
CLOB (Polymarket model) gives real market prices but needs liquidity from day one. AMM (Azuro/Futuur model) always works but may produce a worse user price and is harder to explain. Hyperliquid HIP-4 (May 2026) launched zero-fee on-chain contracts - free to use but revenue model unclear (relies on existing Hyperliquid ecosystem fees elsewhere). For a cold start with 10-20 curated markets: AMM remains the most viable for liquidity at launch. Zero-fee is not a model we can copy without Hyperliquid's existing ecosystem. CLOB is the ideal but requires seeding liquidity. [?]

**2. How do we build resolution trust without CFTC and without a track record - and is insider trading risk a new consideration?**
Kalshi solves it through CFTC regulation but now has 150+ insider trading investigations (Q1 2026) and requires employer-disclosure for high-risk markets. Polymarket solved it through volume and UMA arbitration but now faces a CFTC insider trading complaint (June 2026 - Army soldier, $400K+ profit from classified intel). The implication: resolution trust is not just "who controls this?" but "can this be gamed?" On-chain transparency + clear resolution rules must address both questions. [?]

**3. EU MiCA enforcement active July 2026 - which markets are we actually accessible in?**
EU MiCA grandfathering ends July 2026. CASP license required. Country-specific blocks confirmed for FR, DE, NL, PL, BE. Futuur already blocks these countries. For our global non-US positioning, this means Europe is becoming more restricted, not less. If we are Curacao-licensed like Futuur, we face the same blocks. Decision needed: which jurisdictions does our MVP explicitly serve (and exclude)? This affects market selection (e.g., EU election markets) and fiat on-ramp options. [?]

**4. Sports markets: DECIDED post-MVP - but pressure has intensified**
Kalshi's May 2026 volume was 90% from sports ($17.9B). DraftKings $1.3B annualized in US sports-adjacent markets. World Cup 2026 is a $5-10B industry catalyst starting June 2026. Decision stands: events-first MVP, sports post-MVP. But the volume gap between sports and events has widened further. At some point, not having sports is not a niche choice - it is a significant revenue ceiling. Mark the post-MVP sports milestone as a 3-month decision checkpoint after launch data. Source: [Kalshi volume CNBC 2026](https://www.cnbc.com/2026/05/kalshi-polymarket-volume-comparison.html)
