# Personas - Prediction Market Platform

> Built from: research.md · strategy.md · ux-patterns.md · live-research F1–F3 (June 2026) · post-persona research F4–F6 (June 2026)
> Ground rules: confirmed data cited with source. Where evidence is absent - marked **(?)** and framed as a hypothesis, not a fact.
> Last updated: June 13, 2026 (post-persona research pass)

---

## Why 3 personas (and why this order)

The research defines 3 segments explicitly (strategy.md - Audience). The primary is decided: News Junkie confirmed as the highest-priority segment across 3 research iterations. Crypto Native is secondary - already in the market, needs less hand-holding. Crossover Bettor is post-MVP scope, included here as a planning reference. A 4th persona (Loss-Prone User) emerges from live research finding F3 - included as a risk overlay, not a target segment.

No personas were invented. Where we have no data on a dimension - that gap is marked.

---

## Persona 1 · Alex · NEWS JUNKIE · ⭐ PRIMARY

**28–38 · follows news daily · no crypto wallet · has opinions about everything**

### Why primary

Largest reachable audience. Directly aligned with JTBD J2 - "follow events with real skin in the game." Confirmed primary across all 3 research iterations.

**⚠️ Updated June 2026 (F4):** The earlier claim that "fiat on-ramp removes the only structural barrier" is substantially refuted. Kalshi (fiat-native, no crypto) saw a 93% DAU collapse after the 2024 US election regardless of easy onboarding. Manifold Sweepcash: play-money users did not convert to real money even when friction was removed. The fiat on-ramp is necessary but not sufficient. The real barrier is motivation activation - helping Alex identify his informational edge before presenting a deposit screen. The barrier is motivation AND friction together, not friction alone.

*Source: strategy.md - Audience · research.md §1 Key Conclusions #1 · research.md §9 F4*

---

### Context

Alex reads the news every morning - newsletters, Twitter/X, maybe a podcast. When Trump won, when Bitcoin crashed, when a controversial bill passed - Alex had an opinion before most people even knew what was happening. He discusses it in chats, shares takes on social media, sometimes texts friends "I told you this would happen."

He's heard of Polymarket. Maybe saw a screenshot on Twitter. Went to sign up - saw MetaMask, USDC, a wall of wallet icons - and closed the tab.

**⚠️ Updated June 2026 (F6):** The claim "he doesn't think of himself as a bettor" is partially true but the copy implication is more nuanced than previously stated.

The **identity tension is confirmed** - a Forecaster/Analyst cluster (~8–18% of PM users, per casino.org 10,000+ survey) genuinely resists the "gambler" label and frames activity as knowledge-validation. This is exactly the Alex segment. The closest real-world example found: Chioneso Bakr (Brooklyn musician, Polymarket): *"I said it's definitely not going to be Taylor Swift. I just knew that."* Knowledge-pride, not gambling frame.

**BUT: vocabulary still uses "bet."** Even the most analytical users - Domer (#1 Polymarket trader), Prophet (full-time Polymarket bettor, Substack), campaign staffers with non-public polling - say "I bet", "placing bets", "I'm a full-time bettor." Nobody in the research corpus used "I predicted" as a first-person action verb.

**The split: identity = analyst, action = bet.** Copy implication: use "predict/forecast" in marketing and profile framing (aspiration/identity layer). Accept "bet/position" in functional UI (action layer). The emotional payoff to activate: "I was right / I called it" - not "I predicted."

*Source: research.md §9 F6 · casino.org April 2026 · Reynolds Center April 2026 · ChinaTalk Domer · Polymarket News Prophet · research.md §4 Competitor gaps · benchmark.md C6*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 (primary) | Prove he was right about an event - with money on the line | "When I follow events that matter to me, I want real skin in the game - not just a hot take" |
| J2 | Check whether the market agrees with his opinion | "I already have a view - I want to see what the crowd thinks" |
| J3 | Share a win publicly - confirm he was smarter than the crowd | "I told you so" - make it visible |
| J4 (?) | Earn money from his knowledge of current events | Hypothesis - not confirmed as primary driver vs. J1 |

*Source: CLAUDE.md JTBD J2 primary · ux-patterns.md "Knowledge validation" · ux-patterns.md "Social sharing"*

---

### Pains with current products

- **Crypto wall at signup.** MetaMask + USDC + 8+ wallet icons before seeing a single market. He closes the tab. *(screens/polymarket-signup-mobile.png · benchmark.md C6: 2/5)*
- **No context inside the market.** "Will X happen - YES / NO" with a probability number and nothing else. He doesn't understand why the price is 67%, what affects it, or what "resolves" means. *(research.md §4 - "No 'why this price?'" gap)*
- **Markets feel disconnected from the news he's reading.** The event exists in isolation. There's no story around it. *(ux-patterns.md Story-driven Discovery - Reason 2)*
- **He doesn't know what happens to his money.** No clear explanation of funds protection before the first deposit. *(benchmark.md C2: Futuur 1/5, Polymarket 1/5)*
- **After a loss - nothing.** No context, no "here's what happened," no next step. Just gone. *(research.md §4 - "Post-resolution experience is undesigned" gap · live-research F3)*

---

### Trust triggers

**What convinces:**
- Product is immediately understandable - he gets what it is in 3 seconds without signing up *(benchmark.md C5 - Bet365 5/5 as reference)*
- One clear sentence about funds before he deposits: "Your USDC is held 1:1. We never lend it." *(benchmark.md Top 3 mechanisms #2 - Revolut C2: 5/5)*
- Sees a number of resolved markets - evidence the platform delivers on its promise *(benchmark.md Top 3 mechanisms #3)*
- Understands the fee before he bets - no surprises *(hypothesis H6 · aarrr.md Revenue transparency)*

**What scares:**
- "What happens to my money?" - primary fear at first deposit *(benchmark.md C2 · hypothesis H4)*
- Platform looks like crypto - he associates crypto with scams *(?)* - hypothesis, no direct data
- Losing the first bet and not understanding why *(live-research F3 · aarrr.md Retention - first-bet loss)*
- Having to learn a new financial product before he can do anything *(benchmark.md C5 cognitive anxiety)*

---

### Quote · mood

> "There'll be a big winning streak at the beginning, which happened to me - then bam, everything's gone."

- 24-year-old engineer, Kalshi user, 2026. Lost $10,000+ in 8 days, took a loan to recover.

*Source: live-research F3 · AOL journalistic report 2026. Single verified real-user quote in research.*

**Note:** this quote comes from a loss-escalation case, not from Alex specifically. It illustrates what happens when the post-loss experience is undesigned. Use as a risk signal, not as Alex's typical experience.

---

### Open gaps for this persona

- **(?)** Does Alex actually want to bet real money - or just watch? The Riskiest Assumption is untested. *(research.md §8 - Riskiest Assumption)*
- **(?)** What minimum bet feels "real" to him without being scary? No data. *(live-research Q3)*
- **(?)** Which specific event type first brings him to the platform? Elections? Crypto? No verified data. *(live-research Q5)*

---

## Persona 2 · Dan · CRYPTO NATIVE · 🥈 Secondary

**23–34 · DeFi user · has MetaMask · follows crypto + politics · wants to profit from knowledge**

### Why secondary

Already inside the ecosystem - no crypto barrier to remove. Arrives without the main friction we're solving. Still valuable: provides early liquidity and activity that makes the platform feel alive for News Junkies. But designing for Dan first would make us "another Polymarket" - against our core differentiator.

*Source: strategy.md - Audience · research.md §1 Key Conclusions - "differentiator is being more understandable"*

---

### Context

Dan uses Polymarket already - or at least has tried it. He tracks crypto prices, follows on-chain analytics, and thinks about market probabilities naturally. He placed a few bets on the 2024 election, made some money on Bitcoin ETF approval odds. He knows what AMM and CLOB mean. He doesn't need a tutorial.

What frustrates him: Polymarket's liquidity on smaller markets is thin. Spreads are bad on niche events. He can't always get the size he wants. He's looking for better markets with fairer pricing.

*Source: research.md §4 Competitor analysis - Polymarket "CLOB + thin liquidity on smaller markets" · competitors.md*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 | Monetize superior knowledge of crypto and macro events | "I understand this better than the market - I want to convert that into money" |
| J2 | Find markets where the probability is mispriced | "Value hunting" - where is the crowd wrong? |
| J3 (?) | Diversify beyond pure crypto trading into event prediction | Hypothesis - no direct data |

*Source: strategy.md - Crypto Native motivation · ux-patterns.md "Value hunting"*

---

### Pains with current products

- **Thin liquidity on anything not major.** Big markets (US election, BTC price) are fine. Anything smaller - wide spreads, hard to get size. *(research.md §4 - CLOB liquidity problem · competitors.md Q2)*
- **Polymarket's trust score is 19/40** - lowest of all benchmarked products. Funds protection is 1/5. Even Dan is nervous about large positions. *(benchmark.md total scores)*
- **No explanation of resolution.** For complex events - who decides the outcome? Team multisig? He wants to know. *(research.md §7 Q5 - "Resolution without regulation")*
- **(?)** Hypothesis: fees on crypto markets feel high - Polymarket charges up to 1.80% on crypto category. He may prefer platforms with taker rebates. *(competitors.md - Polymarket Fee V2)*

---

### Trust triggers

**What convinces:**
- On-chain settlement - he can verify every resolved market himself *(research.md §5 - "on-chain transparency as alternative to FSCS")*
- Maker rebates (20–25%) to incentivize liquidity - he could be a maker, not just a taker *(research.md §3 Business Model · Polymarket model reference)*
- Public track record - resolved markets count, verifiable on-chain *(benchmark.md Top 3 mechanisms #3)*

**What scares:**
- Regulatory risk - will the platform be shut down? *(research.md §4 - Polymarket CFTC complaint June 2026)*
- Team multisig resolution on disputed outcomes - who arbitrates? *(research.md §7 Q5)*
- **(?)** Low liquidity at launch = bad prices. He won't use a market where he can't get fair execution. Hypothesis.

---

### Quote · mood

**(?)** No verified direct quote for this persona survived research. Hypothesis of likely sentiment:

> "Polymarket works for big markets but the spreads on anything below $1M volume are brutal. Looking for something with better liquidity on geopolitics."

*Framed as hypothesis based on competitors.md liquidity findings. Not a verified user quote.*

---

## Persona 3 · Maria · CROSSOVER BETTOR · 🥉 Secondary · Post-MVP scope

**29–42 · bets on sports (Bet365, DraftKings) · wants "smarter" markets · analysis over luck**

### Why secondary / post-MVP

Research explicitly marks this segment as "Later." Sports = post-MVP decision. Including here as a planning reference because Maria will be the primary acquisition driver once sports markets are added (Kalshi's 89% revenue from sports confirms the size of this segment). Design for MVP should not block her future entry.

*Source: strategy.md - Crossover Bettor · research.md §1 Key Conclusions #6 - Sports post-MVP*

---

### Context

Maria places bets on football, tennis, Formula 1. She uses Bet365 or a local bookmaker. She's comfortable with odds, money on the line, and the emotional rhythm of following an event she has a stake in. She's good at reading form and context - she doesn't bet randomly.

She finds sports betting limiting: the house always sets the odds, and she can't bet on things that matter outside sports. She saw a headline about prediction markets during the US election and thought "that's basically what I do, but for news."

*Source: strategy.md - Crossover Bettor segment description · research.md §4 Competitor analysis - Bet365 as SOFT competitor*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 | Apply her analytical skills to a new domain | "I'm good at reading a situation - I want an arena where that matters, not just luck" |
| J2 | Bet on events beyond sports - politics, culture, crypto | "Sports is what I know, but I want more" |
| J3 (?) | Find better odds than the bookmaker | Hypothesis - she knows the house edge, may be looking for fairer pricing |

*Source: strategy.md - Crossover Bettor motivation*

---

### Pains with current products

- **Bet365 trust is 33/40 - the reference bar is high.** Whatever we build, Maria will compare it to Bet365's polish, 20-year brand, and clear odds. *(benchmark.md total scores - Bet365 33/40 vs. our analog Futuur 14/40)*
- **Prediction markets feel unregulated.** She's used to licensed bookmakers with responsible gambling tools. Curacao license means little to her. *(benchmark.md C1 - Polymarket 2/5, Futuur 1/5)*
- **Crypto friction.** Like Alex, she has no crypto wallet. But unlike Alex, she's less motivated by the "proving I'm right" angle - she wants to bet, not to validate a worldview. *(?)*
- **No parlays / combos yet in PM space** - DraftKings added combos in May 2026, prediction markets haven't. *(?)*  hypothesis based on her sports betting background.

---

### Trust triggers

**What convinces:**
- Clear resolution rules before betting - who decides, what evidence counts *(benchmark.md C8)*
- Responsible gambling tools - she's used to them, their absence is a red flag *(benchmark.md - Bet365 reference)*
- Familiar UX - bottom tab bar, live odds movement, position tracking *(research.md §4 - "3 common patterns present in all")*

**What scares:**
- No regulatory badge. She knows what FSCS means. "Blockchain verifiable" is not the same to her. *(benchmark.md - "1 mechanism that won't work")*
- **(?)** Fear of complex crypto mechanics before she can place a simple bet. Hypothesis.

---

### Quote · mood

**(?)** No verified direct quote. Hypothesis:

> "I've been betting on football for years. Prediction markets seem interesting but I have no idea if they're legit or how I'd even get started."

*Hypothesis based on Crossover Bettor segment description (strategy.md) and benchmark.md trust gap findings.*

---

## Risk overlay: the Loss-Prone User

This is not a persona to design for - it is a behavioral pattern that can emerge from **any** of the three personas above, especially Alex (News Junkie).

**Pattern (confirmed, F3+F5 - HIGH confidence ↑ upgraded from medium):**
1. **First WIN** → overconfidence ← **trigger revised: it is the WIN, not the first loss**
2. Escalating bet sizes → systematic losses
3. Loss-chasing → catastrophic exit (loan, $10,000+ lost in days)
4. Quit only via external force (partner confrontation, lawsuit, account block) - not self-regulation

**Updated June 2026 (F5):** Multiple independent case studies confirmed and trigger revised. K.A. (24yo Kalshi engineer): early Counter-Strike wins → escalated to $1,000+ wagers → $10,000+ lost in 8 days → took out loans. Quit after partner found out. Lorenzo Miro (Polymarket): first bet won $100+ → lost $1,700+ over 2 months → quit via lawsuit. "Poly Hell" author: won early markets → deposited $10,000 MORE after losing $7,500. beachboy4 trader: 51% win rate, still lost $2.36M from position-sizing escalation.

**Three behavioral archetypes (new in F5):**

| Archetype | Pattern | Evidence |
|---|---|---|
| Loss Chaser | First win → overconfidence → escalation → chasing. External force required to stop. | Named case studies (journalism) |
| Casual Experimenter | Deposits small amount (<$10), goes dormant after first loss or when triggering event ends. Never documents. | ~50% of 2M Polymarket wallets made/lost <$10 (PYMNTS 2026) |
| Platform-Betrayal Quitter | Won or should have won, platform failed them (frozen withdrawal, wrong payout, resolution dispute). Leaves angrily. Writes Trustpilot review. | Kalshi 1.9/5 · Polymarket 1.4/5, 90% one-star |

**Product implication (updated):**
- The **post-resolution WIN screen** needs design attention equal to the loss screen. Early wins set the overconfidence that fuels later escalation. Confetti or "you were right!" copy without friction may accelerate the pattern.
- The **post-resolution LOSS screen** remains the intervention point - but it should primarily speak to the Casual Experimenter (re-entry path) rather than only to the escalation case.
- **Platform betrayal** (frozen funds, wrong payouts, opaque resolution) is the documented #1 churn driver - more than losing a bet. Transparent on-chain resolution + instant withdrawal = trust infrastructure, not UX polish.
- No competitor designs either of these moments. We must.

**Evidence:** 24-year-old Kalshi user, 2026. 19 federal lawsuits against Kalshi by Jan 2026. 70–84% of all PM traders lose money (F2). PMC/NCB academic study 2024: 52.5% of subjects in loss condition continued playing vs 47.5% in control.

*Source: live-research F3+F5 · AOL 2026 · Substack "Poly Hell" · beincrypto.com · PYMNTS/Bloomberg 2026 · PMC/NCB 2024 · Trustpilot Kalshi + Polymarket · research.md §9*

---

## What we still don't know about any of these personas

| Gap | Status | Affects |
|---|---|---|
| Does Alex actually want to bet, or just watch? (Riskiest Assumption) | **SUBSTANTIALLY ANSWERED (F4):** Motivation is the primary barrier, not friction alone. Fiat on-ramp is necessary but not sufficient. Kalshi + Manifold Sweepcash both confirm this. The product must activate informational-edge motivation BEFORE the deposit step. | Persona 1 - core acquisition strategy |
| What trust signals work in their own words? | **PARTIALLY ANSWERED (F5):** Platform betrayal (frozen funds, wrong payout, opaque resolution) is the #1 documented trust killer. On-chain resolution + fast withdrawal = most actionable trust signals. | All 3 personas |
| When exactly does the Loss-Prone pattern activate? | **REVISED (F5):** Trigger is first WIN (overconfidence), not first loss. Sequence: first win → escalation → losses → chasing. | Risk overlay |
| Min bet size that feels real without triggering harm escalation | [?] No data. | All personas, especially Persona 1 |
| Which specific event brings Alex to the platform for the first time | [?] No verified data. | Persona 1 - acquisition |
| Non-US TAM for Personas 1 and 3 | [?] Poll data (casino.org, Morning Consult) is US-only. Non-US identity and motivation frames unknown. | Market sizing |

*Source: research.md §8–9 - Open questions Q1, Q3, Q5, Q7 · live-research F3–F6*

---

*Compiled from: research.md · strategy.md · ux-patterns.md · benchmark.md · competitors.md · live-research findings F1–F3 (June 2026)*
