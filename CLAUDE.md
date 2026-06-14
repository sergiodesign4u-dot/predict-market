# CLAUDE.md - Prediction Market Platform

## Project Overview
A mobile-first prediction market platform where users bet YES/NO on real-world events.
Users stake crypto on whether an event will happen or not, and earn/lose based on the outcome.

## JTBD - Jobs To Be Done

**Primary:**
> "When I follow events that matter to me - I want to have real skin in the game, so it's not just news, but my personal stake with a real outcome"

**Secondary:**
> "And if I understand the situation better than others - I want that to convert into money, simply and without the complexity of trading"

**Product implications:**
- First page - live events happening now, not "sign up"
- Onboarding: event → mechanics → bet (not the other way around)
- Retention: notifications about events, not about topping up balance
- Profile: prediction track record as reputation

---

## Core Differentiator
**Clarity and accessibility for new users.** Competitors (Polymarket, Kalshi, Manifold) can feel opaque to newcomers. This platform prioritizes transparency - users always understand what they're doing, why, and what happens next.

## Target Audience
- Age: 20–40
- Primary driver: **Trust** - the platform must feel credible, transparent, secure
- Secondary: Engagement - users come back to follow events they bet on

## Platform
- **Mobile-first web** → then responsive desktop
- Web3 / blockchain-based

---

## Product

### Market Types (MVP)
- **Binary markets** - YES / NO on a single event
- **Multi-outcome markets** - multiple options, each with YES / NO

### Event Resolution
- Events are real-world occurrences
- Platform team creates and resolves events (MVP)
- Resolution mechanism: AMM-style dynamic pricing - payout depends on *when* the bet was placed, not just the outcome
- If you bet YES and event doesn't happen → you lose (partial loss based on timing of stake)

### Categories
- MVP: Politics, Crypto, Culture, General
- Post-MVP: Sports and expansion based on interest/demand

### MVP Feature Scope
- Binary YES/NO markets
- Multi-outcome markets
- User account (social login - Google, X, etc.)
- Crypto wallet (stablecoins primary, multi-token support)
- Fiat on-ramp (card → crypto)
- Leaderboard
- Notifications (event outcomes, position updates)
- Staking system - TBD / to research

---

## Business Model
- **Commission per bet** (primary) - exact % TBD, needs competitive research
- Spread - possible secondary model
- No subscriptions
- No min/max bet limits at launch (Polymarket uses $0.01 minimum - research needed)

---

## Financials & Compliance
- **All transactions in crypto** - stablecoins (USDC, USDT) as primary
- Fiat on-ramp supported (user converts fiat → crypto on platform)
- **KYC**: Required for fiat deposits; crypto-only users - KYC TBD (Polymarket operates without KYC for crypto)
- **Geo**: Global, with geo-restrictions based on regulatory requirements (no US for real-money prediction markets)

---

## Competitors & Research
| Platform | Notes |
|---|---|
| Polymarket | AMM model, good mobile UX, 3-level nav can be complex for new users |
| Kalshi | US-regulated, fiat-based |
| Manifold Markets | Play money, social focus |
| Metaculus | Forecasting community, no real money |

**Research still needed:**
- Commission rates across competitors
- Min/max bet limits
- KYC thresholds
- Specific blockchain/chain selection (Ethereum, Polygon, Base, etc.)
- AMM mechanism specifics

---

## Design Principles
1. **Clarity first** - every screen should be self-explanatory; new users should never feel lost
2. **Trust signals everywhere** - transparent odds, clear resolution rules, audit trail
3. **Mobile-first** - design for thumb, test on mobile before desktop
4. **Engagement loops** - notify users about events they care about, show live odds movement

---

## Tech Stack (TBD)
- Frontend: Web (mobile-first)
- Blockchain: Web3, specific chain TBD (likely Polygon, Base, or Arbitrum for low fees)
- Wallet connection: WalletConnect / MetaMask + social login
- Smart contracts: AMM-based market resolution

---

## Timeline
~3 months to MVP

## Team
Solo - product, design, and development
