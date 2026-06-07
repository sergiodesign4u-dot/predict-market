# UX Patterns Analysis

## Audience Behavioral Patterns

| Pattern | Description | Segment |
|---|---|---|
| **Event-triggered arrival** | User arrives when something happens — elections, a crypto move, a scandal. News is the trigger. | News Junkie, all |
| **Knowledge validation** | User already has an opinion — and comes to check whether the market agrees with them | News Junkie, Crypto Native |
| **Position monitoring** | User has already bet — and comes back to watch whether the price is moving their way | All after the first bet |
| **Value hunting** | User looks for where the market is "wrong" — finds an undervalued outcome and enters | Crypto Native, Crossover |
| **Social sharing** | User wants to show their prediction/win — shares it as confirmation of being right | All, especially News Junkie |

**Key pattern: Event-triggered arrival** — the entry point for all segments. How we greet a user "from the news" determines activation, the first bet, and return visits.

---

## 5 Fundamentally Different UX Patterns

### 1. Event Feed (Reactive Scroll)
**How it works:** Algorithmic or chronological feed of event cards. The user scrolls, stops on something that hooks them, acts directly from the card.
**Where it's used:** Polymarket, Kalshi, Twitter, TikTok
**When it fits:** Mobile context, large number of varied events, user wants to browse rather than search for something specific
**When it breaks:** Without curation — noise. New users don't understand the sorting logic. With fewer than 20 active markets it looks empty and dead.

---

### 2. Market Board (Trading Grid)
**How it works:** Table or grid of all markets with numbers — price, volume, 24h change. Filters and sorting are the primary navigation.
**Where it's used:** Kalshi (advanced), Polymarket (desktop), Bloomberg, Binance
**When it fits:** Experienced users with financial literacy, J3 segment (value hunting)
**When it breaks:** Newcomers see a table of numbers and leave. Kills the emotional connection to the event. The opposite of J2.

---

### 3. Story-driven Discovery
**How it works:** Every event is a narrative unit: context + why it matters now + what the market says + resolution conditions → CTA to bet. Event = article + market.
**Where it's used:** Nowhere in prediction markets fully. Partially — Metaculus (question descriptions), The Athletic (sports + context)
**When it fits:** News Junkie segment, first contact with a new user, when context before betting is important
**When it breaks:** More space and time before action. Hard to scale without an editorial team or AI. Returning users want to go straight to betting.

---

### 4. Portfolio / Position-first
**How it works:** First screen — active positions, P&L, deadlines. New markets — in a separate section.
**Where it's used:** Robinhood, Binance, trading apps for experienced users
**When it fits:** Retention phase, user already has bets and comes back to monitor them
**When it breaks:** Empty state for new users = demotivation. Does not solve acquisition and activation.

---

### 5. Guided Challenge (Game Loop)
**How it works:** "Bet of the day" or featured market — minimal choice, one offer, two buttons. After action — result and next challenge.
**Where it's used:** Duolingo, HQ Trivia, DraftKings Pick'em, Wordle
**When it fits:** Onboarding, reducing cognitive load, casual segment
**When it breaks:** Limits the experienced user. Doesn't scale — becomes annoying after 5–7 sessions.

---

## Choice for Our Context

### ✅ Best fit: Pattern 3 — Story-driven Discovery

**Reason 1 — Direct alignment with J2 JTBD.**
"Following events with real skin in the game" — this is about context, not numbers. The user arrives via a news story and wants to understand what's happening. Story-driven delivers that context inside the product.

**Reason 2 — Closes the main gap of competitors.**
No competitor explains why the price is what it is and what will affect the outcome. Markets are isolated questions without context. This is our differentiator.

**Reason 3 — Builds trust without regulatory badges.**
A clear event description + resolution conditions + source = the platform knows what it's talking about. Trust through content transparency — our alternative to FSCS/SIPC.

---

### 🔀 Under condition X: Pattern 1 — Event Feed
**Condition X:** > 30 active markets and the user has already made their first bet (understood the mechanics).
Event Feed is the ideal retention pattern for repeat sessions.
**Decision:** Story-driven for first contact and onboarding → Feed for return visits.

---

### ❌ Not a fit: Pattern 2 — Market Board (Trading Grid)
CLAUDE.md: audience 20–40, trust-first, clarity for new users, J2-first (engaged spectator). Market Board requires financial literacy that the News Junkie doesn't have. A table with prices in cents is the language of a trader, not a spectator. It would make us just another Polymarket, whereas our differentiator is being more understandable.
