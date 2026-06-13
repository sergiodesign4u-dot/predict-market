# Personas — Prediction Market Platform

> Built from: master-research.md · strategy.md · ux-patterns.md · live-research F1–F3 (June 2026)
> Ground rules: confirmed data cited with source. Where evidence is absent — marked **(?)** and framed as a hypothesis, not a fact.
> Last updated: June 13, 2026

---

## Why 3 personas (and why this order)

The research defines 3 segments explicitly (strategy.md — Audience). The primary is decided: News Junkie confirmed as the highest-priority segment across 3 research iterations. Crypto Native is secondary — already in the market, needs less hand-holding. Crossover Bettor is post-MVP scope, included here as a planning reference. A 4th persona (Loss-Prone User) emerges from live research finding F3 — included as a risk overlay, not a target segment.

No personas were invented. Where we have no data on a dimension — that gap is marked.

---

## Persona 1 · Alex · NEWS JUNKIE · ⭐ PRIMARY

**28–38 · follows news daily · no crypto wallet · has opinions about everything**

### Why primary

Largest reachable audience. Fiat on-ramp removes the only structural barrier between them and the product. Directly aligned with JTBD J2 — "follow events with real skin in the game." Confirmed primary across all 3 research iterations.

*Source: strategy.md — Audience · master-research.md §1 Key Conclusions #1*

---

### Context

Alex reads the news every morning — newsletters, Twitter/X, maybe a podcast. When Trump won, when Bitcoin crashed, when a controversial bill passed — Alex had an opinion before most people even knew what was happening. He discusses it in chats, shares takes on social media, sometimes texts friends "I told you this would happen."

He's heard of Polymarket. Maybe saw a screenshot on Twitter. Went to sign up — saw MetaMask, USDC, a wall of wallet icons — and closed the tab.

He doesn't think of himself as a "bettor." He thinks of himself as someone who understands how the world works.

*Source: master-research.md §4 Competitor gaps — "Onboarding assumes prior knowledge" · benchmark-trust.md C6 Onboarding friction · screens/polymarket-signup-mobile.png*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 (primary) | Prove he was right about an event — with money on the line | "When I follow events that matter to me, I want real skin in the game — not just a hot take" |
| J2 | Check whether the market agrees with his opinion | "I already have a view — I want to see what the crowd thinks" |
| J3 | Share a win publicly — confirm he was smarter than the crowd | "I told you so" — make it visible |
| J4 (?) | Earn money from his knowledge of current events | Hypothesis — not confirmed as primary driver vs. J1 |

*Source: CLAUDE.md JTBD J2 primary · ux-patterns.md "Knowledge validation" · ux-patterns.md "Social sharing"*

---

### Pains with current products

- **Crypto wall at signup.** MetaMask + USDC + 8+ wallet icons before seeing a single market. He closes the tab. *(screens/polymarket-signup-mobile.png · benchmark-trust.md C6: 2/5)*
- **No context inside the market.** "Will X happen — YES / NO" with a probability number and nothing else. He doesn't understand why the price is 67%, what affects it, or what "resolves" means. *(master-research.md §4 — "No 'why this price?'" gap)*
- **Markets feel disconnected from the news he's reading.** The event exists in isolation. There's no story around it. *(ux-patterns.md Story-driven Discovery — Reason 2)*
- **He doesn't know what happens to his money.** No clear explanation of funds protection before the first deposit. *(benchmark-trust.md C2: Futuur 1/5, Polymarket 1/5)*
- **After a loss — nothing.** No context, no "here's what happened," no next step. Just gone. *(master-research.md §4 — "Post-resolution experience is undesigned" gap · live-research F3)*

---

### Trust triggers

**What convinces:**
- Product is immediately understandable — he gets what it is in 3 seconds without signing up *(benchmark-trust.md C5 — Bet365 5/5 as reference)*
- One clear sentence about funds before he deposits: "Your USDC is held 1:1. We never lend it." *(benchmark-trust.md Top 3 mechanisms #2 — Revolut C2: 5/5)*
- Sees a number of resolved markets — evidence the platform delivers on its promise *(benchmark-trust.md Top 3 mechanisms #3)*
- Understands the fee before he bets — no surprises *(hypothesis H6 · aarrr.md Revenue transparency)*

**What scares:**
- "What happens to my money?" — primary fear at first deposit *(benchmark-trust.md C2 · hypothesis H4)*
- Platform looks like crypto — he associates crypto with scams *(?)* — hypothesis, no direct data
- Losing the first bet and not understanding why *(live-research F3 · aarrr.md Retention — first-bet loss)*
- Having to learn a new financial product before he can do anything *(benchmark-trust.md C5 cognitive anxiety)*

---

### Quote · mood

> "There'll be a big winning streak at the beginning, which happened to me — then bam, everything's gone."

— 24-year-old engineer, Kalshi user, 2026. Lost $10,000+ in 8 days, took a loan to recover.

*Source: live-research F3 · AOL journalistic report 2026. Single verified real-user quote in research.*

**Note:** this quote comes from a loss-escalation case, not from Alex specifically. It illustrates what happens when the post-loss experience is undesigned. Use as a risk signal, not as Alex's typical experience.

---

### Open gaps for this persona

- **(?)** Does Alex actually want to bet real money — or just watch? The Riskiest Assumption is untested. *(master-research.md §8 — Riskiest Assumption)*
- **(?)** What minimum bet feels "real" to him without being scary? No data. *(live-research Q3)*
- **(?)** Which specific event type first brings him to the platform? Elections? Crypto? No verified data. *(live-research Q5)*

---

## Persona 2 · Dan · CRYPTO NATIVE · 🥈 Secondary

**23–34 · DeFi user · has MetaMask · follows crypto + politics · wants to profit from knowledge**

### Why secondary

Already inside the ecosystem — no crypto barrier to remove. Arrives without the main friction we're solving. Still valuable: provides early liquidity and activity that makes the platform feel alive for News Junkies. But designing for Dan first would make us "another Polymarket" — against our core differentiator.

*Source: strategy.md — Audience · master-research.md §1 Key Conclusions — "differentiator is being more understandable"*

---

### Context

Dan uses Polymarket already — or at least has tried it. He tracks crypto prices, follows on-chain analytics, and thinks about market probabilities naturally. He placed a few bets on the 2024 election, made some money on Bitcoin ETF approval odds. He knows what AMM and CLOB mean. He doesn't need a tutorial.

What frustrates him: Polymarket's liquidity on smaller markets is thin. Spreads are bad on niche events. He can't always get the size he wants. He's looking for better markets with fairer pricing.

*Source: master-research.md §4 Competitor analysis — Polymarket "CLOB + thin liquidity on smaller markets" · competitive-analysis.md*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 | Monetize superior knowledge of crypto and macro events | "I understand this better than the market — I want to convert that into money" |
| J2 | Find markets where the probability is mispriced | "Value hunting" — where is the crowd wrong? |
| J3 (?) | Diversify beyond pure crypto trading into event prediction | Hypothesis — no direct data |

*Source: strategy.md — Crypto Native motivation · ux-patterns.md "Value hunting"*

---

### Pains with current products

- **Thin liquidity on anything not major.** Big markets (US election, BTC price) are fine. Anything smaller — wide spreads, hard to get size. *(master-research.md §4 — CLOB liquidity problem · competitive-analysis.md Q2)*
- **Polymarket's trust score is 19/40** — lowest of all benchmarked products. Funds protection is 1/5. Even Dan is nervous about large positions. *(benchmark-trust.md total scores)*
- **No explanation of resolution.** For complex events — who decides the outcome? Team multisig? He wants to know. *(master-research.md §7 Q5 — "Resolution without regulation")*
- **(?)** Hypothesis: fees on crypto markets feel high — Polymarket charges up to 1.80% on crypto category. He may prefer platforms with taker rebates. *(competitive-analysis.md — Polymarket Fee V2)*

---

### Trust triggers

**What convinces:**
- On-chain settlement — he can verify every resolved market himself *(master-research.md §5 — "on-chain transparency as alternative to FSCS")*
- Maker rebates (20–25%) to incentivize liquidity — he could be a maker, not just a taker *(master-research.md §3 Business Model · Polymarket model reference)*
- Public track record — resolved markets count, verifiable on-chain *(benchmark-trust.md Top 3 mechanisms #3)*

**What scares:**
- Regulatory risk — will the platform be shut down? *(master-research.md §4 — Polymarket CFTC complaint June 2026)*
- Team multisig resolution on disputed outcomes — who arbitrates? *(master-research.md §7 Q5)*
- **(?)** Low liquidity at launch = bad prices. He won't use a market where he can't get fair execution. Hypothesis.

---

### Quote · mood

**(?)** No verified direct quote for this persona survived research. Hypothesis of likely sentiment:

> "Polymarket works for big markets but the spreads on anything below $1M volume are brutal. Looking for something with better liquidity on geopolitics."

*Framed as hypothesis based on competitive-analysis.md liquidity findings. Not a verified user quote.*

---

## Persona 3 · Maria · CROSSOVER BETTOR · 🥉 Secondary · Post-MVP scope

**29–42 · bets on sports (Bet365, DraftKings) · wants "smarter" markets · analysis over luck**

### Why secondary / post-MVP

Research explicitly marks this segment as "Later." Sports = post-MVP decision. Including here as a planning reference because Maria will be the primary acquisition driver once sports markets are added (Kalshi's 89% revenue from sports confirms the size of this segment). Design for MVP should not block her future entry.

*Source: strategy.md — Crossover Bettor · master-research.md §1 Key Conclusions #6 — Sports post-MVP*

---

### Context

Maria places bets on football, tennis, Formula 1. She uses Bet365 or a local bookmaker. She's comfortable with odds, money on the line, and the emotional rhythm of following an event she has a stake in. She's good at reading form and context — she doesn't bet randomly.

She finds sports betting limiting: the house always sets the odds, and she can't bet on things that matter outside sports. She saw a headline about prediction markets during the US election and thought "that's basically what I do, but for news."

*Source: strategy.md — Crossover Bettor segment description · master-research.md §4 Competitor analysis — Bet365 as SOFT competitor*

---

### Jobs

| # | Job | Format |
|---|---|---|
| J1 | Apply her analytical skills to a new domain | "I'm good at reading a situation — I want an arena where that matters, not just luck" |
| J2 | Bet on events beyond sports — politics, culture, crypto | "Sports is what I know, but I want more" |
| J3 (?) | Find better odds than the bookmaker | Hypothesis — she knows the house edge, may be looking for fairer pricing |

*Source: strategy.md — Crossover Bettor motivation*

---

### Pains with current products

- **Bet365 trust is 33/40 — the reference bar is high.** Whatever we build, Maria will compare it to Bet365's polish, 20-year brand, and clear odds. *(benchmark-trust.md total scores — Bet365 33/40 vs. our analog Futuur 14/40)*
- **Prediction markets feel unregulated.** She's used to licensed bookmakers with responsible gambling tools. Curacao license means little to her. *(benchmark-trust.md C1 — Polymarket 2/5, Futuur 1/5)*
- **Crypto friction.** Like Alex, she has no crypto wallet. But unlike Alex, she's less motivated by the "proving I'm right" angle — she wants to bet, not to validate a worldview. *(?)*
- **No parlays / combos yet in PM space** — DraftKings added combos in May 2026, prediction markets haven't. *(?)*  hypothesis based on her sports betting background.

---

### Trust triggers

**What convinces:**
- Clear resolution rules before betting — who decides, what evidence counts *(benchmark-trust.md C8)*
- Responsible gambling tools — she's used to them, their absence is a red flag *(benchmark-trust.md — Bet365 reference)*
- Familiar UX — bottom tab bar, live odds movement, position tracking *(master-research.md §4 — "3 common patterns present in all")*

**What scares:**
- No regulatory badge. She knows what FSCS means. "Blockchain verifiable" is not the same to her. *(benchmark-trust.md — "1 mechanism that won't work")*
- **(?)** Fear of complex crypto mechanics before she can place a simple bet. Hypothesis.

---

### Quote · mood

**(?)** No verified direct quote. Hypothesis:

> "I've been betting on football for years. Prediction markets seem interesting but I have no idea if they're legit or how I'd even get started."

*Hypothesis based on Crossover Bettor segment description (strategy.md) and benchmark-trust.md trust gap findings.*

---

## Risk overlay: the Loss-Prone User

This is not a persona to design for — it is a behavioral pattern that can emerge from **any** of the three personas above, especially Alex (News Junkie).

**Pattern (confirmed, F3 — medium confidence):**
1. Early wins → overconfidence
2. Systematic losses → loss-chasing
3. Escalating bet sizes → catastrophic exit (loan, $10,000+ lost in days)

**Evidence:** 24-year-old Kalshi user, 2026. 19 federal lawsuits against Kalshi by Jan 2026. 70–84% of all PM traders lose money (F2).

**Product implication:** the post-resolution loss screen is the intervention point. Before the chasing loop starts. No competitor designs this moment today. We must.

*Source: live-research F3 · AOL 2026 · live-research F2 · Yahoo Finance / DeFi Oasis*

---

## What we still don't know about any of these personas

| Gap | Affects |
|---|---|
| Does Alex actually want to bet, or just watch? (Riskiest Assumption) | Persona 1 — entire value proposition |
| Min bet size that feels real without triggering loss-chasing | All personas, especially Persona 1 |
| Which specific event brings Alex to the platform for the first time | Persona 1 — acquisition |
| What trust signals actually work in their own words (no verified quotes) | All 3 personas |
| Non-US TAM for Personas 1 and 3 | Market sizing |
| When exactly does the Loss-Prone pattern activate — after how many losses? | Risk overlay |

*Source: master-research.md §8 — Open questions Q1, Q3, Q5, Q7, Q8*

---

*Compiled from: master-research.md · strategy.md · ux-patterns.md · benchmark-trust.md · competitive-analysis.md · live-research findings F1–F3 (June 2026)*
