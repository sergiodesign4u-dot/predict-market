# Benchmark: Trust & First-Time Credibility

> v_refresh - June 2026
> Changelog: Products changed. Original benchmark (Revolut, Coinbase, Robinhood, Kalshi, Polymarket) mixed prediction markets with unrelated fintech. New set: top 3 HARD competitors (Polymarket, Kalshi, Futuur) + 1 SOFT (Bet365) + 1 ASPIRATIONAL (Revolut). This gives a much more honest read of the trust gap in our specific market.

**Why this dimension?**
Trust is the #1 value for our audience (20-40, real money, fintech). This is exactly where our direct competitors are weakest, and exactly where wireframe decisions grow from.

---

## Evaluation Criteria (scale 1-5)

| # | Criterion | What it measures |
|---|---|---|
| **C1** | Regulatory transparency | Whether the platform's legal status is immediately visible: license, jurisdiction, who regulates it |
| **C2** | Funds protection | Whether it's explained how and where the user's money is stored, and what won't happen without their permission |
| **C3** | Fee transparency before action | Whether the cost of an action is visible BEFORE the user confirms |
| **C4** | Social proof | Volume, user count, resolved markets, awards - and how they're presented |
| **C5** | Clarity of first impression | Whether it's clear from the first screen who this is for and what to do |
| **C6** | Onboarding friction | Steps to first value - fewer is better |
| **C7** | Risk communication | Whether what can go wrong is explained honestly and clearly |
| **C8** | Resolution clarity | Whether it's clear how disputes are resolved and what happens on a win/loss |

---

## Products for Evaluation

| Product | Group | Why chosen |
|---|---|---|
| **Polymarket** | HARD | Our primary crypto PM competitor. Largest volume globally. Baseline for what the space looks like today. |
| **Kalshi** | HARD | Best trust in the prediction market space. CFTC-regulated. Gold standard for what a licensed PM achieves on trust. |
| **Futuur** | HARD | Our closest structural analog: crypto + fiat hybrid, global, no US regulation. Shows what the trust gap looks like for platforms similar to ours. |
| **Bet365** | SOFT | 80M+ registered users, 20+ year brand, licensed in 30+ jurisdictions. Shows what the Crossover Bettor's trust reference frame looks like. Same JTBD, much higher trust. |
| **Revolut** | ASPIRATIONAL | Best-in-class trust UX in mobile fintech. 50M+ users, 10-15 min onboarding, explicit funds protection copy. The aspirational bar for how a non-bank financial product builds trust. |

---

## Scores (1-5)

| Criterion | Polymarket | Kalshi | Futuur | Bet365 | Revolut |
|---|:---:|:---:|:---:|:---:|:---:|
| C1 Regulatory transparency | 2 | **5** | 1 | **5** | **5** |
| C2 Funds protection | 1 | 4 | 1 | 4 | **5** |
| C3 Fee transparency before action | 2 | 3 | 2 | 3 | 4 |
| C4 Social proof | 4 | 3 | 2 | **5** | **5** |
| C5 Clarity of first impression | 3 | 4 | 3 | **5** | 4 |
| C6 Onboarding friction | 2 | 2 | 2 | 3 | 3 |
| C7 Risk communication | 3 | 4 | 1 | 4 | 3 |
| C8 Resolution clarity | 2 | 3 | 2 | 4 | 3 |
| **Total** | **19** | **28** | **14** | **33** | **32** |

---

## Key Observations

**Polymarket (19/40):** Trust rests entirely on $9B+ in cumulative volume as social proof (C4: 4). Everything else is weak. C1 (regulatory): "not regulated" visible in Privacy Policy but not on the homepage. C2 (funds): zero explanation of what happens to your USDC - where it sits, who holds it, what happens if the platform fails. C3 (fees): taker fees introduced March 2026 but shown only at trade time, not as upfront transparency. 8 wallet icons on signup = cognitive overload. Our primary competitor's trust floor is very low. Source: [polymarket-signup-mobile.png] [competitors.md]

**Kalshi (28/40):** Strongest in the prediction market space because CFTC regulation does real work. C1 (regulatory: 5): CFTC-regulated badge is the headline trust signal. C2 (funds: 4): banking partners implied by USD fiat model. C7 (risk: 4): regulated settlement means risk disclosure is required. Weaknesses: C6 (onboarding: 2) - auto-modal signup on entry is aggressive and kills first impression. US-only creates a hard geographic wall. Not replicable without a US license. Source: [kalshi-home-mobile.png]

**Futuur (14/40):** The most important finding in the new benchmark. Futuur is our closest structural analog (global, crypto+fiat hybrid, no US regulation) - and it scores worse than Polymarket on trust. C1 (regulatory: 1): no licensing information visible on public pages. C2 (funds: 1): no explanation of custody, insurance, or what happens to user funds. C7 (risk: 1): no risk warnings on public pages. This is the clearest possible picture of what we look like to a new user if we don't actively address trust from the start. It also confirms that the gap we're trying to fill is real and unaddressed. Source: [futuur-home-mobile.png]

**Bet365 (33/40):** What 20+ years and 30+ licenses look like. C5 (clarity: 5): you know immediately - sports betting, here are the odds, here's the bet slip. No onboarding needed. C4 (social proof: 5): "world's favourite online sports betting company" backed by 80M+ users and massive sports sponsorships. C7 (risk: 4): responsible gambling tools are prominently featured because UK Gambling Commission requires it - "When the fun stops, stop." C8 (resolution: 4): sports settlement rules are crystal clear. This is the trust reference frame of our Crossover Bettor segment. When they arrive at our platform, this is their subconscious benchmark. Source: [bet365-home-mobile.png]

**Revolut (32/40):** The fintech aspirational bar. C2 (funds: 5): FSCS protection is front and center - the concrete promise of "your money is safe here" shown visually before anything else. C4 (social proof: 5): 75M+ customers + Trustpilot 4.7 + 5 awards in a single compact block. Real-time transaction animations, instant card freeze, fraud alerts visible = security as a product feature, not a footnote. Onboarding: 10-15 minutes. Note: FSCS protection is unavailable to us (see mechanism that won't work below). Source: [revolut-trust-mobile.png] [revolut-home-mobile.png]

---

## The Key Insight

The trust gap in our market is not just about Polymarket. Our closest structural analog, Futuur, scores 14/40. The two direct competitors we're building against score 14 and 19 out of 40. The benchmark for what users expect from a financial product (Bet365, Revolut) is 32-33/40. That is a gap of 13-19 points. Closing that gap is not a UI detail - it is a product strategy decision made in every design choice.

---

## Top 3 Mechanisms to Carry Into Our MVP

### 1. Immediate product clarity at first impression (Bet365, C5: 5/5)

**Mechanism:** Within 3 seconds of landing, the user knows: what this is, who it's for, and what to do next. Bet365: live sports, odds numbers, a clear bet slip. Zero ambiguity.

**Our equivalent:** Show a live, active market with context on the homepage - no signup required to see it. The event name + probability + brief context + YES/NO buttons. New users should understand the product before they are asked to register.

**Why it works:** Cognitive anxiety ("what even is this?") is the first trust failure. Bet365 eliminates it in 3 seconds. We need to do the same for prediction markets.

### 2. Concrete promise of funds protection (Revolut, C2: 5/5)

**Mechanism:** "Your USDC is held 1:1. We never lend it without your permission." Not legal text - one plain sentence.

**Where to use:** First deposit screen and the "How it works" section. Repeat it on any screen where a user is being asked to move money.

**Why it works:** Futuur scoring 1/5 on this criterion while being our closest structural analog proves the gap is wide open. The new user's primary fear is "what happens to my money if this platform disappears?" Coinbase answered it. We need to answer it too. This is especially important because we cannot use FSCS/SIPC/CFTC badges.

### 3. Resolved markets as social proof (Bet365 + Polymarket, C4: 5/5 and 4/5)

**Mechanism:** Volume and track record as trust signals. Bet365: "80M+ users, world's favourite." Polymarket: "$9B+ traded." Neither is available to us at launch.

**Our equivalent at MVP:** "N markets resolved correctly · since [date] · all on-chain verifiable." Resolved markets are more meaningful for a prediction market than user count - they prove the core promise (events resolve, winnings pay out) has been delivered. Start collecting this signal from day one.

**Why it works:** New users need evidence that the platform has operated and delivered on its promise. Resolved market count is a metric we can build from zero and display honestly from the first week of operation.

---

## 1 Mechanism That Will NOT Work

### Regulatory badges (FSCS, SIPC, FDIC, CFTC) or simulating Bet365's brand authority

**Why it won't work:** FSCS, SIPC, and CFTC regulation require real licenses we do not hold. Displaying similar elements without the legal backing destroys trust the moment a user checks. FTX built a "banking look" without banking guarantees.

Separately: Bet365 scores 33/40 through 20 years of operation and 30+ licenses. That track record is not copyable at launch. Attempting to match their authority signals (sponsorships, "world's favourite" claims) with no history reads as fake.

**Our honest alternative:**
- On-chain transparency: "All settlements are on the blockchain. Any user can verify every resolved market at [chain explorer URL]."
- Explicit non-bank disclosure: "We are not a bank or broker. Your USDC is held in a smart contract, not lent out."
- Transparency over authority: show the resolution source, the criteria, and the outcome for every resolved market. Let the track record build itself.
