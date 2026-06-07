# AARRR Analysis — Prediction Market Platform

> Hypothetical analysis at the start of the product. Metrics and approaches require validation after MVP launch.

---

## Acquisition
*How people discover the platform and arrive for the first time*

**Channels:**
- **SEO via events** — each market = a separate page. "Who will win US elections 2026", "Will Bitcoin hit 100k" — ready landing pages with organic traffic
- **Twitter/X** — prediction markets live in this community. Primary channel for the crypto audience
- **Crypto media** — CoinDesk, Decrypt, The Block cover major markets
- **Word-of-mouth** — wins and public predictions spread organically

**Unknowns:**
- Which channel will deliver the lowest CAC
- Whether we can compete with Polymarket on SEO from day one

**Metric:** `new registered users / week`

**Product decisions:**
- Each market is a standalone SEO page with meta tags and og:image showing live odds
- One-click market sharing directly from the card

---

## Activation
*When the user first feels value — the "aha moment"*

**Aha moment:** the user placed their first bet and sees their position is live — price moving in real time.

**Path to first bet:**
```
Arrived → Registered → Verified email
→ Connected wallet / deposited → Found a market
→ Understood the mechanics → Placed a bet ← aha moment
```
Every step = drop-off. Competitors fail exactly here.

**Hypotheses:**
- **Fiat first** — card top-up immediately, no Web3 wallet required for the first bet
- **Guided first bet** — onboarding flow: trending market → odds explanation → "bet $5?"
- **Demo bet** — stake without money to understand mechanics, then convert to a real bet

**Unknowns:**
- What % of users drop off at the deposit step
- Whether a demo bet increases or decreases conversion to a real bet

**Metric:** `% of users who placed their first bet within 24 hours of registration`

**Product decisions:**
- Onboarding flow with progress bar
- Inline mechanics explanation directly in the market card
- Fiat on-ramp on the first screen after registration

---

## Retention
*Why the user comes back tomorrow, next week, next month*

**Built-in hook:** an open position — the user can't forget about the platform until the event resolves. But between the bet and the result there's an engagement gap.

**Three retention levels:**

| Stage | When | What happens | Notification |
|---|---|---|---|
| Hot | Day 1–3 | Watching odds movement | *"YES price moved from 45% to 61%"* |
| Warm | Day 4–14 | New event in a favorite category | *"New market: Will Zelensky meet Trump?"* |
| Cold | Day 15+ | Leaderboard, streak, resolution | *"Your position resolved. You won $47"* |

**Retention risk:** if the user lost their first bet — high chance they won't return. That's why the first market during onboarding should have the **nearest deadline** (not "end of year", but "end of this week").

**Unknowns:**
- Optimal notification frequency (too many = unsubscribe)
- Whether a loss brings the user back or drives them away

**Metrics:** `% of users active on day 7` and `% active on day 30`

**Product decisions:**
- Smart notifications tied to price movement and approaching deadlines
- Personalized feed based on categories where the user has already bet
- Leaderboard with weekly reset

---

## Revenue
*How the platform earns*

**Primary model — Trading fee on win (2%):**

| Option | When taken | Psychology |
|---|---|---|
| A: on entry | Bet $100 → $98 in play | Hurts immediately |
| **B: on win (exit)** | Won $150 → receive $147 | **Pay only when you earned** |

Recommendation: Option B — less pain, more loyalty.

**Additional sources:**

| Source | When | % | Transparency |
|---|---|---|---|
| Trading fee | On win | ~2% | Shown explicitly before confirmation |
| On-ramp | On deposit | affiliate from provider | Not our commission |

**Unknowns:**
- What % delivers acceptable LTV at our CAC
- At what trading volume does the platform become profitable

**Metrics:** `revenue per active user / month` and `total trading volume`

**Product decision:** show the fee explicitly and honestly before bet confirmation. *"Platform earns $0.40 if you win"* — transparency as a competitive advantage.

---

## Referral
*How users bring other users*

**Built-in referral mechanic:** people naturally want to share predictions. *"I told you so"* — a social instinct.

**Three types of organic sharing:**

| Type | Message | When |
|---|---|---|
| Position share | *"I bet $50 on YES. Market says 34%, I think everyone is wrong"* | Before resolution |
| Win share | *"Won $340 on the French election. Called it 3 weeks ago"* | After resolution |
| Market share | *"What does everyone think? Here's a market where you can put money on it"* | Anytime |

**Mechanics:**

| Mechanic | How it works | Reference |
|---|---|---|
| Share card | Beautiful card with position for Twitter/Telegram | Robinhood, Spotify Wrapped |
| Referral bonus | Bring a friend → both get $5 on first bet | Fintech standard |
| Public profile | Prediction track record is open → user builds reputation | Metaculus, Manifold |
| Market embed | Any market can be embedded on a site or article | Polymarket (partially) |

**Unknowns:**
- Which sharing channel will drive the highest conversion to registration
- Whether a referral bonus justifies CAC

**Metrics:** `% of new users who came via sharing` and `viral coefficient (k-factor)`

**Product decision:** after every resolution — automatically generate a share card with the result. User wins → wants to brag → free traffic.

---

## Summary Metrics

| Stage | Key metric | Target (hypothesis) |
|---|---|---|
| Acquisition | New registrations / week | — |
| Activation | % first bet within 24h | >40% |
| Retention | % active on day 7 | >30% |
| Retention | % active on day 30 | >15% |
| Revenue | Trading volume / month | — |
| Referral | % users via sharing | >20% |

---

## Key Product Takeaways

1. **Activation is the biggest risk.** The long path to the first bet = primary drop-off. Fiat first + guided onboarding — MVP priority
2. **Retention is built into the mechanics,** but needs support via notifications and the right choice of first market
3. **Revenue is transparent** — showing the fee explicitly is trust, not weakness
4. **Referral is organic** — share card after a win is a must-have, not a nice-to-have
