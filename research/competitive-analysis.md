# Competitive Analysis

## Screens Index

| File | Platform | Screen | Access |
|---|---|---|---|
| `polymarket-home-mobile.png` | Polymarket | Home — market feed, categories, YES/NO cards | Public |
| `polymarket-home-scroll-mobile.png` | Polymarket | Home — scrolled, live sports markets | Public |
| `polymarket-event-detail-mobile.png` | Polymarket | Event detail — multi-outcome, chart, volume | Public |
| `polymarket-event-bet-mobile.png` | Polymarket | Bet interface — Buy Yes/No in cents | Public |
| `polymarket-signup-mobile.png` | Polymarket | Sign Up — Google + Email + 8 wallet icons | Public |
| `kalshi-home-mobile.png` | Kalshi | Home + auto-modal signup | Public |
| `kalshi-home-browse-mobile.png` | Kalshi | Home after dismissal — LIVE hero card | Public |
| `kalshi-market-detail-mobile.png` | Kalshi | Market detail — candlestick chart, price brackets | Public |
| `manifold-home-mobile.png` | Manifold | Home — question list, play money | Public |
| `manifold-market-detail-mobile.png` | Manifold | Market detail — % chance, Bet YES/NO, comments | Public |
| `futuur-home-mobile.png` | Futuur | Home — multi-outcome with probability bars | Public |
| `futuur-market-detail-mobile.png` | Futuur | Market detail — chart, outcomes | Public |
| `futuur-market-bet-mobile.png` | Futuur | Bet interface — Yes/No per outcome | Public |
| `metaculus-home-mobile.png` | Metaculus | Home — question feed, gauge charts | Public |
| `metaculus-question-detail-mobile.png` | Metaculus | Question detail — 65% gauge, Predict, comments | Public |
| Portfolio / My Bets | Polymarket | Open positions, P&L | **[? behind login]** |
| Portfolio / My Bets | Kalshi | Portfolio, history | **[? behind login]** |
| Deposit flow | Polymarket | Crypto deposit, on-ramp | **[? behind login]** |
| Deposit flow | Kalshi | Fiat deposit, ACH/card | **[? behind login]** |
| Deposit flow | Futuur | Crypto + fiat choice | **[? behind login]** |
| Leaderboard | Futuur | User ranking | **[? behind login]** |

---

## Comparison Table

| Axis | Polymarket | Kalshi | Manifold | Futuur | Metaculus |
|---|---|---|---|---|---|
| **Audience** | Crypto natives, DeFi users, global (not US) | US, TradFi audience, mainstream | Global, everyone — no real-money barrier | Global, crypto + fiat hybrid | Analysts, researchers, policy community |
| **Product foundation** | CLOB on Polygon, pUSD (USDC) | CFTC-regulated exchange, USD fiat | Play money (Mana Ṁ), user-created markets | Crypto + fiat hybrid, multi-currency | No money — pure forecasting + reputation |
| **Key mechanics** | Conditional Token Framework, YES/NO binary tokens, order book matching | Order book, price in cents (82¢/19¢), regulated settlement | AMM for market-making, AI-generated context, community resolution | Probability bars per outcome, Yes/No on each option | Aggregated community forecast, calibration scoring |
| **Trust** | On-chain transparency, UMA decentralized resolution, $7.5B+ volume | CFTC regulation — highest institutional trust | No real-money risk — trust through openness | Less known, small track record | Academic accuracy (~4% deviation), partnerships |
| **Monetization** | ~2% fee on winnings + maker/taker rebates | Exchange fees (maker/taker), like a classic exchange | Prize pool drawings in USDC, no fees on Mana trades | Commission on bets (% not public) | Grants, institutional partnerships, premium |

---

## 3 Common Patterns

**1. Horizontal category navigation at the top + bottom tab bar**
Every single platform uses the same pattern: horizontal scroll categories (Trending, Politics, Crypto…) and a bottom nav with 3–5 tabs. This is the de-facto genre standard.

**2. Probability percentage as the main number**
On every card and every detail screen — % probability is the central element. It sits above the event name, above the volume. It's the market "price" and the "game state" at once.

**3. Probability-over-time chart**
All platforms (except Metaculus partially) show how the price moved — from a simple line (Manifold) to a candlestick chart (Kalshi). Movement = engagement. People come back to see if their position is "in the green."

---

## 3 Key Differences

**1. Pricing mechanics: CLOB vs AMM vs Community**
- Polymarket and Kalshi: order book — price is formed by matching orders
- Manifold: AMM — liquidity is automatic, there's always a market
- Metaculus: aggregate of community forecasts, no trading
→ **Implication:** CLOB gives "fairer" prices but requires liquidity. AMM always works but may give a worse rate.

**2. Real money vs Play money vs Crypto**
- Kalshi: fiat USD, CFTC regulation — greatest trust, but geographically limited
- Polymarket: crypto (USDC on Polygon) — global, but with a Web3 barrier
- Manifold: play money — zero barrier, but also zero stakes
→ **Implication:** Each approach attracts a different audience. Hybrid (Futuur) is theoretically the broadest.

**3. Who creates markets**
- Polymarket, Kalshi: platform team — quality control, fewer markets
- Manifold: any user — thousands of markets, but quality varies
- Metaculus: mix — moderated questions + community
→ **Implication:** Platform-created = curated and trustworthy. User-created = scale but also noise.

---

## 3 Open Questions

**1. How to solve the first-bet problem without a Web3 wallet?**
Polymarket technically requires USDC on Polygon. Kalshi requires a US bank account. Futuur is the most hybrid, but it's unclear exactly how. None of them have solved onboarding for the "ordinary user" flawlessly. Can a fiat card → stablecoin on-ramp be our competitive advantage?

**2. CLOB or AMM for MVP?**
CLOB gives a better price but requires liquidity from day one (the chicken-and-egg problem). AMM always works but is harder to explain to users. What's more realistic for launching from scratch?

**3. How to build trust in resolution without regulation and without a large track record?**
Kalshi solves it through CFTC. Polymarket through UMA (decentralized arbitration). Both solutions are complex for MVP. Is transparent rules + team multisig enough at launch — or will that immediately deter users?
