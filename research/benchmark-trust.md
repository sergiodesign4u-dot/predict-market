# Benchmark: Trust & First-Time Credibility

**Why this dimension?**
Trust is the #1 value for our audience (20–40). This is fintech with real money: without trust, there's no product. This is exactly where competitors are weakest, and exactly where decisions for wireframes grow from.

---

## Evaluation Criteria (scale 1–5)

| # | Criterion | What it measures |
|---|---|---|
| **C1** | Regulatory transparency | Whether the platform's legal status is immediately visible — license, jurisdiction, who regulates |
| **C2** | Funds protection | Whether it's explained how and where the user's money is stored, and what won't be done with it without permission |
| **C3** | Fee transparency before action | Whether the cost of an action is visible BEFORE the user confirms |
| **C4** | Social proof | Number of users, volumes, awards, media — and how they're presented |
| **C5** | Clarity of first impression | Whether it's clear from the first screen who this is, for whom, and why |
| **C6** | Onboarding friction | Number of steps to first value (the fewer, the higher the score) |
| **C7** | Risk communication | Whether what can go wrong is explained honestly and clearly |
| **C8** | Resolution / rules clarity | Whether it's clear how disputes are resolved and what happens on a win/loss |

---

## Products for Evaluation

| Product | Category | Why chosen |
|---|---|---|
| **Revolut** | Fintech / neo-bank | The benchmark for trust design in mobile fintech — 75M+ users, regulated in 30+ countries |
| **Coinbase** | Crypto exchange | The largest public crypto company — the benchmark for trust in Web3 |
| **Robinhood** | Investing app | "Commission-free" — the benchmark for fee transparency and first impression |
| **Kalshi** | Regulated PM | The only regulated prediction market — best trust in the genre |
| **Polymarket** | Crypto PM | Our main competitor — for contrast |

---

## Scores (1–5)

| Criterion | Revolut | Coinbase | Robinhood | Kalshi | Polymarket |
|---|:---:|:---:|:---:|:---:|:---:|
| C1 Regulatory transparency | **5** | **5** | 4 | **5** | 2 |
| C2 Funds protection | **5** | **5** | 4 | 4 | 1 |
| C3 Fee transparency | 4 | 3 | **5** | 3 | 2 |
| C4 Social proof | **5** | **5** | 4 | 3 | 4 |
| C5 Clarity of first impression | 4 | 4 | **5** | 4 | 3 |
| C6 Onboarding friction | 3 | 3 | 3 | 2 | 2 |
| C7 Risk communication | 3 | 4 | 3 | 4 | 3 |
| C8 Resolution clarity | 3 | 4 | 3 | 3 | 2 |
| **Total** | **32** | **33** | **31** | **28** | **19** |

---

## Key Observations by Product

**Revolut:** The benchmark for social proof — "75+ million customers" + Trustpilot 4.7 + 5 awards in a single block. FSCS PROTECTED badge right over the product screenshot. Trust through scale and regulation.

**Coinbase:** The only crypto platform with public reporting. "1:1 asset holdings — we never lend your assets without permission" — a concrete promise. Bug Bounty program as a signal of engineering maturity.

**Robinhood:** "Commission-Free" — the primary trust signal right in the headline. The user's first concern ("are they making money off me?") is addressed immediately. SIPC, FINRA, CFTC — regulatory badges in the footer, but they're there.

**Kalshi:** Automatic signup modal on entry — aggressive, but clean: Google / Apple / Email, 3 options. "CFTC-regulated" — the strongest trust signal in prediction markets. Downside: US-only restriction breaks the experience for international users.

**Polymarket:** 8 wallet and social icons on signup = cognitive overload. Zero explanation of how funds are protected. "Not regulated by CFTC" is visible in the Privacy Policy, but not on the homepage. Trust rests entirely on $7.5B in volume — and that's a weak foundation.

---

## Top 3 Mechanisms to Carry Into Our MVP

### 1. Concrete promise of funds protection (Coinbase)
**Mechanism:** "Your USDC is held 1:1. We never lend it without your permission."
**Where to use:** First deposit screen and the "How it works" section. Not legal text — one simple sentence.
**Why it works:** Closes the new user's primary fear before they even voice it.

### 2. Social proof as a block on the homepage (Revolut)
**Mechanism:** Number of users + volume + rating/award — in one compact block below the hero section.
**Where to use:** Homepage (after the hero, before the market list). Format: "$X traded · N users · Rating Y".
**Why it works:** Social proof reduces the newcomer's anxiety — "if so many people trust it, it must be okay."

### 3. Fee transparency at the moment of action (Robinhood)
**Mechanism:** Show the exact commission amount before confirming the bet. "The platform earns $0.40 if you win."
**Where to use:** Confirmation screen before submitting the bet.
**Why it works:** Transparency at the moment of highest anxiety = trust. Hidden fees are the #1 cause of churn.

---

## 1 Mechanism That Will NOT Work — and Why

### Regulatory badges like FSCS / SIPC / FDIC (Revolut, Robinhood)
**Mechanism:** Official regulator shields directly on the homepage or deposit screen.
**Why it won't work for us:** We are not and will not be a bank or broker in the classical sense. These badges are not decorations — they are legal obligations. If we display similar elements without the real backing, it won't just fail to build trust — it will destroy it the moment a user tries to verify. FTX built a "banking look" without banking guarantees, and the result is well known.

**Alternative:** Instead of regulatory badges — on-chain transparency: "All settlements are on the blockchain. You can verify every transaction." This is the honest equivalent for a crypto-native platform.
