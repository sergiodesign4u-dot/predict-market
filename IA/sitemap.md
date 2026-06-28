# Sitemap - Prediction Market Platform

> Status: navigation design complete. Ready for wireframes.
> Built from: personas.md · jtbd.md · master-research.md

---

## Entities

Inventory of objects the user directly interacts with to close their jobs.
Each entity exists only if at least one confirmed job (MJ/FJ/EJ/SJ) requires it.

---

### 1. Event (Market)

The central object. The thing a user finds, reads about, and bets on.
Without it, no job is closable.

**Jobs served:** MJ · FJ1 · FJ2

| Field | Notes |
|---|---|
| Question / title | "Will X happen before [date]?" |
| Type | Binary (YES/NO) · Multi-outcome (multiple options, each with YES/NO). The card must render both layouts, see Event Feed card composition. This is the existing Type field, no new field is added for it. |
| Thumbnail image | Per-event image used on the card as a visual differentiator. Real field; renders as a grey-box placeholder in wireframes (conventions Addition A), a sample image in concept and a real image in production. |
| Category | Politics · Crypto · Culture · General |
| Frequency / recurrence | One-time or recurring. Recurring cadence: Hourly · Daily · Weekly · Monthly. NEW (wireframe pass): introduces recurring markets, and powers the Frequency filter on the Event Feed. Resolution mechanics for recurring markets are to be detailed later (each cadence instance resolves on its own schedule). |
| Current probability (%) | The "price" - primary display number on every card |
| Probability chart | History of odds movement over time |
| Context / narrative | Why this event matters, what drives the odds, key arguments for YES and NO ← **our differentiator (FJ2)** |
| Resolution conditions | What counts as YES, what source is authoritative |
| Status | Active · Resolved · Cancelled |
| Resolution deadline | When the event closes for new bets |
| Volume | Total USDC staked across all positions |
| Created by | Platform team (MVP) |

**Related to:** Bet · Resolution · Notification · User (a user can save / follow this event, a bookmark, see Saved events)

---

### 2. Bet (Position)

The user's stake on one side of an event. Created the moment a user places a bet.
This is the MJ itself - the "real stake with real consequences."

**Jobs served:** MJ · FJ3 · FJ5 · EJ1 · EJ3

| Field | Notes |
|---|---|
| Direction | YES · NO |
| Amount staked (USDC) | What the user put in |
| Entry probability | Odds at the moment of placing - AMM determines this |
| Fee amount | Shown before confirmation ("platform earns $X if you win") - H6 |
| Potential payout | Calculated at entry, shown pre-confirmation |
| Current value | Mark-to-market as odds move |
| Status | Active · Won · Lost · Cancelled |
| Placed at | Timestamp |
| Resolution payout | Actual amount received after event resolves |

**Related to:** User · Event · Resolution (triggers status change + payout) · Wallet (deducts stake, credits payout)

---

### 3. User (Account)

The authenticated person. Required for every job that involves memory, state, or money.

**Jobs served:** all (actor in every job)

| Field | Notes |
|---|---|
| Social login | Google · X (OAuth) - no password at MVP |
| Display name | Shown on Profile |
| Wallet | Custodial (platform-managed) or connected self-custody |
| KYC status | None · Level-1 via on-ramp (name+address up to $20K) · Platform-level (if triggered at $2K cumulative) |
| Notification preferences | Which event types trigger alerts |
| Saved / followed events | Bookmarks: events the user chose to follow. Powers the Saved view under Events. NEW relationship, added in the Event Feed revision pass. |
| Joined date | - |

**Related to:** Bet · Wallet · Profile · Notification · Event (saves / follows, a bookmark, see Saved events)

---

### 4. Wallet (Balance)

The user's financial state on the platform. Separate from User because it has its own lifecycle: deposit, lock, payout, withdrawal.

**Jobs served:** FJ3 · FJ4 · EJ2

| Field | Notes |
|---|---|
| Available balance (USDC) | Ready to bet. Displayed as **Cash** in the UI. |
| In-play balance (USDC) | Locked in active bets |
| Total deposited (lifetime) | For KYC threshold tracking |
| Transaction history | Deposits · Withdrawals · Payouts · Fees |
| Connected address | If self-custody wallet; empty if custodial |

**Display labels (UI framing, not new fields):**
- **Portfolio** = all money on the platform = Available (Cash) + In-play. The total value, including funds in active events.
- **Cash** = Available balance = the amount ready for new entries.
Competitors show both at once; we show one figure at a time with a swap control on desktop (Portfolio default), and surface the Portfolio figure in the mobile Portfolio bottom slot. See Desktop layer D-desktop-4 and the Navigation bottom-nav table.

**Transaction sub-object:**

| Field | Notes |
|---|---|
| Type | Deposit · Withdrawal · Payout · Fee |
| Amount | - |
| Status | Pending · Confirmed · Failed |
| On-chain hash | For crypto-path transactions |
| KYC applied | Tier used at this transaction |
| On-ramp provider | Transak · MoonPay (for deposit transactions) |

**Related to:** User · Bet (deducts/credits) · Resolution (credits payout)

---

### 5. Resolution

The act of determining an event's outcome. Separate from Event because it has its own lifecycle, evidence, and on-chain proof.
This is the moment that triggers payouts, post-resolution screens, and share cards.

**Jobs served:** FJ5 · EJ1 · EJ3 · SJ1

| Field | Notes |
|---|---|
| Outcome | YES · NO (or which option in multi-outcome) |
| Evidence / source | URL or description of what determined the outcome |
| Resolved by | Team multisig (MVP) → oracle (post-MVP) |
| On-chain transaction hash | Public verifiability |
| Timestamp | - |
| Resolution note | Plain-language explanation of what happened and why ← FJ5 "what happened" |

**Related to:** Event (one-to-one) · Bet (triggers status + payout for all positions on this event)

---

### 6. Profile (Public)

The public-facing reputation of a user. Separate from Account because it is visible to other users, not just the account holder.
Serves the "I called it" social identity.

**Jobs served:** SJ1 · SJ2

| Field | Notes |
|---|---|
| Display name | - |
| Avatar | - |
| Total predictions | Count of resolved bets placed |
| Win rate | % correct on resolved bets |
| Prediction history | List of resolved bets (event, direction, outcome, profit/loss) - public |
| Notable calls | (?) Could surface "biggest wins" or "most accurate category" - hypothesis, no confirmed job yet |

**Related to:** User · Bet (resolved) · Share Card

---

### 7. Share Card

Auto-generated artifact after a resolution. The "I told you so" object - created without user effort, immediately shareable.
Serves SJ1 directly. Without this, sharing requires manual effort, which kills the social loop.

**Jobs served:** SJ1

| Field | Notes |
|---|---|
| Event question | Pulled from Event |
| User's call | YES or NO |
| Outcome | What actually happened |
| Result | Won · Lost |
| Profit/Loss | Amount |
| Generated image | OG-image for social sharing (Twitter/X card, WhatsApp preview) |

**Related to:** Resolution (created on resolution) · User · Profile

---

### 8. Notification

Alert that brings the user back to an event they care about.
Not in jtbd.md as a direct job, but directly enables FJ1 (find the event while it's still relevant) for return visits, and is the primary retention mechanism for hot/warm/cold return (aarrr.md).

**Jobs served:** FJ1 (return path) · Retention (aarrr.md)

| Field | Notes |
|---|---|
| Type | Odds moved significantly · Deadline approaching · Event resolved · New event in followed category |
| User reference | - |
| Event reference | - |
| Position reference | (if about the user's active bet) |
| Read / unread | - |
| Sent at | - |

**Related to:** User · Event · Bet

---

## Under Question

Objects mentioned in product docs but not mapped to a confirmed job. Included here for review - not in the main entity list.

| Object | Why it's here | Why it's in question |
|---|---|---|
| **Category** | Events are grouped by Politics / Crypto / Culture / General | Taxonomy attribute of Event, not an object with its own lifecycle. No job requires "interacting with a category" as a standalone object. Could remain a field on Event. |
| **Leaderboard** | Listed in CLAUDE.md MVP features | No explicit job in jtbd.md. SJ2 (public track record) is served by Profile. Leaderboard is a view over Profiles - a feature, not a distinct entity. Revisit if social competition mechanics are confirmed. |
| **Odds Chart** | Every competitor has it; part of Event detail | Attribute of Event (probability history), not a standalone entity. Lives inside Event. |
| **Fiat Transaction** | Deposit/withdrawal via Transak/MoonPay | Currently modeled as sub-object of Wallet. Promote to standalone entity only if on-ramp flow reveals complexity that can't fit inside Wallet (e.g., multi-step KYC state machine per transaction). |

---

## Screens

> Notation:
> Job in `(parentheses)` = job from jtbd.md this screen closes. No job = `[SIROTA]`.
> ⭐ PRIMARY = Alex (News Junkie). 🥈 SECONDARY = Dan (Crypto Native).
> Screens without persona mark serve both.
> States (empty, error, loading) are NOT screens - they are states of the screens below.

---

### EVENTS - what to bet on

The user arrives because something happened in the world (FJ1).
This group is the entry point for both personas.

```
Event Feed                                   (FJ1)          ⭐ PRIMARY + 🥈 SECONDARY
Event Detail                                 (FJ2 · MJ)     ⭐ PRIMARY + 🥈 SECONDARY
```

**Event Feed** - cards of active markets. The product home, the entry of every session. Default sorted view is Trending (not a neutral "All"); recency is the alternate sort. No sign-in required to browse.
States: loading (initial data fetch) - empty (no events match current filter or category) - error (network fail, API unreachable).
Note: push-permission-missing banner also surfaced on Event Feed when OS push is denied (see Notifications states).

Card composition (revised, decluttered):
- Thumbnail placeholder image next to the event question (visual differentiator, Event.Thumbnail image field).
- Event question (the primary hook).
- Current probability %, compact, must not dominate the card.
- YES / NO controls as a trigger-entry (routes to Event Detail with a pre-selected side, see flow change below), not a bet placed on the card.
- Small meta: volume and closing date (a light liquidity and relevance signal, FJ1).
- Bookmark control (save / follow the event, see Saved events), placed as a small element in the meta row.
- Card entry: the event question itself is the link to Event Detail (neutral entry). There is NO "Open event detail" button and no card footer (removed in the card pass); the card stays compact and the list scans faster.
- REMOVED from the card: the category badge (category lives in the filter, not on the card), the context snippet, and the full-width "Open event detail" button / card footer. The card is now clean; the price context lives on Event Detail only, where FJ2 closes. Removing the snippet concentrates the FJ2 differentiator on Event Detail, so the Event Detail context block must be strong when that screen is built. (This supersedes the earlier "context visible on card" and "snippet hard-lock" framing; the card teaser is retired in favour of a clean card plus a strong Event Detail context block. The first-visit story-driven vs return denser distinction is no longer the card's job.)

Two card layouts, both built (Event.Type already supports this, no new field):
- Binary: one question, the % of one side, large YES / NO controls.
- Multi-outcome: N options, each row is an option plus its % plus compact YES / NO controls. On the feed card only the two leading positions are shown (the options with the highest probability / most stake at that moment), with no "+N more" line; the full option list appears after the user opens the event (via the question link). Omitting the extra line keeps multi-outcome cards close to binary-card height so the meta rows line up across the grid and the feed reads evenly. The two-position cap is a feed preview rule only, it does not change Event.Type or how many options the event actually has.
- Multi-outcome is a normal event type from Event.Type, NOT the rejected "Market Board / trading view" pattern (jtbd.md "features to cut"). It is a card layout for events with more than two options, not a trader terminal.

Controls placement (revised in the wireframe pass): categories are second-level navigation in a sub-nav band directly under the header (Trending default, then Politics, Crypto, Culture, General). The feed heading echoes the active category (for example "Trending"), not a generic "Live events" label, and updates when another category is chosen. The heading row carries a Kalshi-style filter cluster (feed controls, not navigation), each a dropdown whose label shows the current value:
- **Sort:** Trending, Volatile, New, Closing soon, Volume, 50-50, plus a Reverse sort toggle.
- **Frequency:** All, One-time, Hourly, Daily, Weekly, Monthly (filters by the Event Frequency attribute, recurring markets).
- **Category:** the full category list. This is redundant-by-design with the second-level chip nav: the chips are quick access to the main categories, the dropdown is the full list that scales as categories grow. The dropdown, the chips, and the heading stay in sync (selecting in one updates the others).

Exact sort and filter labels are a wireframe detail. Categories stay the locked four for MVP; the category mechanism is built to scale to more categories later without rework. Do not add empty categories now.

Saved view: a filter / view over the Event Feed showing only saved events. It is a view within Events, the same way categories filter the feed, not a separate screen. Reached from the bookmark control on cards, from the Favorites (heart) entry in the desktop header, and from the Favorites bottom-nav slot on mobile (the wireframe pass moved Favorites into the mobile bottom bar, swapping with Notifications). See Saved events for the relationship and the alert hypothesis.

**Event Detail** - one event, full view: probability, chart, narrative context (why this price), resolution conditions, source. CTA: YES / NO. This screen is our primary differentiator - no competitor has context at this depth (FJ2 confirmed gap). With the card snippet removed, this context block is now the sole home of the FJ2 differentiator and must be strong.
States: loading (event data fetching) - error (load failure, T8 in MJ and FJ2 flows - retry returns to Event Detail) - resolved-while-reading (this event just resolved: [outcome] - navigate to Win/Loss Screen if user holds a position, else to Event Feed) - pre-selected entry variant (arrived from a card YES/NO tap with a side and, for multi-outcome, an option pre-selected; the bet is still placed here, FJ2 context shown first; to be detailed when Event Detail is built).

#### Saved events (NEW addition)

This is a new addition to the IA, stated plainly as new, not a pre-existing job.

- **Relationship:** User saves / follows Event (a bookmark). Added to the User entity (Saved / followed events) and the Event entity (Related to: User).
- **Saved view:** a filter / view over the Event Feed showing only saved events. NOT a new bottom-nav slot and NOT a new top-level destination; a view within Events, like a category filter.
- **Affordances:** a bookmark control on each event card; a Favorites (heart) entry in the desktop header utility cluster; and a Favorites bottom-nav slot on mobile (wireframe pass), all opening the Saved view (see Desktop layer D-desktop-4 and the bottom-nav table).
- **Alert on a saved event moving significantly: [hypothesis].** Not a confirmed job, not wired as a confirmed Notification type. The confirmed Notification types stay as they are (entity 8). A proactive "your saved event moved" alert is flagged for later validation only.
- **Rationale:** saving improves convenience and retention; every benchmarked competitor exposes a bookmark on the card. The confirmed job backing is partial (retention, FJ1 return), so the save relationship is added now, but the proactive saved-event alert stays a hypothesis until validated.

#### Auth-state axis

Logged-out versus registered is a cross-cutting axis across the browse screens (Event Feed, Event Detail) and the gate, not a per-screen state column on every screen.

- **Default render of browse screens (Event Feed, Event Detail) is registered.** Logged-out is a header-level delta on those screens: the utility cluster shows a "Sign in" entry instead of Balance plus avatar; the feed body and cards are identical and browsable in both. Do NOT create a full duplicate logged-out page for each browse screen.
- **The real auth branch concentrates at the activation gate** (Bet Screen Confirm -> Sign In / Register -> Deposit), which already exists as its own screens and states. Edge cases (logged-out at confirm; registered with no balance -> Deposit) live there, per Variant B, already locked.
- **Effect:** the auth edge cases stay localized at the gate, not spread across browse screens. No page explosion.

---

### ACTIVATION GATE - bet-first, gate at confirm (Variant B)

The user browses and builds a bet logged out. The gate fires only when they tap "Confirm" on the Bet Screen - not at YES/NO tap.
Two branches at the gate: News Junkie (social login then fiat deposit) and Crypto Native (connect existing USDC wallet, no fiat, no KYC on platform).
After the gate, a mandatory AMM price reconcile step (S5) checks whether the price moved during auth/deposit before executing the bet.
Teaching formerly in Onboarding swipes is redistributed to live screens: Event Detail explains odds context, Bet Screen shows fee and payout inline, Deposit explains fund safety.

```
Sign In / Register                           (FJ3)          ⭐ PRIMARY · 🥈 SECONDARY (wallet connect path)
Deposit                                      (FJ3 · FJ4 · EJ2)   ⭐ PRIMARY
```

**Sign In / Register** - social login (Google, X) for the News Junkie path. Crypto Native connects an existing USDC wallet here instead of using fiat. One screen, two branches. Triggered only at gate, never before the user has built bet intent.
States: in-progress (OAuth redirect pending, wallet connect prompt open) - error (auth failed - T5, wallet connect failed - T15) - error-provider-conflict (account exists under a different provider, e.g. registered via X, trying Google: prompt to use the original provider or link accounts).

**Deposit** - fiat card to USDC via Transak (primary), MoonPay (fallback). KYC runs inside the Transak widget - the user completes identity verification there, not on this platform. Risk block displayed inline before the user submits: "Your USDC is held 1:1 - we do not lend or invest deposited funds." Fee shown before submit. Also reachable standalone from Wallet for top-ups.
States: in-progress (Transak widget loading, KYC pending inside widget) - error-card (card declined - T2) - error-KYC (KYC rejected - T1) - widget-load-failure (Transak iframe blocked or network error: fallback to "open Transak directly" or "connect a USDC wallet" - S3 fix) - pending (payment under review, usually under 5 min) - minimum-not-met (inline error before submit, shown against amount input).

---

### BET - place and confirm a bet

Reached from Event Detail when the user taps YES or NO. No auth required to reach it - the user is still logged out at this point (Variant B).
Auth and deposit happen only at the confirm step, via the activation gate.

```
Bet Screen                                   (MJ · FJ3)     ⭐ PRIMARY + 🥈 SECONDARY
```

**Bet Screen** - direction (YES/NO, pre-set from tap on Event Detail), amount input with default $5 pre-fill, quick-select ($5/$10/$25/$50), fee displayed before confirm ("platform earns $X if you win"), potential payout shown. Confirm button triggers the activation gate for logged-out users. Single screen: intent and confirmation in one place.
States: intent (logged out - user builds the bet, no auth yet) - S5-reconcile (price moved during gate: shows old price vs new price, user must re-confirm) - error (bet registration failed on-chain - T3) - insufficient-balance (inline: "you have $X, can bet up to $X or deposit more" with options to change amount or go to Deposit) - event-closed (this event just resolved while on screen: navigate to Win/Loss Screen if user holds a position, else to Event Feed).

---

### RESOLUTION - what happened after the event closes

Triggered by a notification or by the user opening an Active Bet that has resolved.

```
Win Screen                                   (EJ1 · SJ1)    ⭐ PRIMARY + 🥈 SECONDARY
Loss Screen                                  (FJ5 · EJ3)    ⭐ PRIMARY + 🥈 SECONDARY
```

**Win Screen** - "You were right." Amount won, resolution summary (what happened and why), Share Card auto-generated. CTA: Share · See next events. Design rationale: no confetti loop, no persistent celebration animation. Research finding F5 (master-research.md): first WIN is the trigger for overconfidence and escalation, not loss. The win screen must celebrate the outcome without feeding the loop. Celebratory but measured - one moment, then move on.
Per F5, the first win is the stronger escalation trigger (overconfidence). Share / mark the moment is the default next action; "see next events" is a deliberate secondary CTA, not the primary. Symmetric with the Loss intervention, shaped for overconfidence rather than impulse. Modeled in IA/flows.md SJ1: share path is the primary edge, secondary "see next events" edge is labeled with the overconfidence risk.
States: loading (Share Card generation in progress) - error (Share Card not generated, SJ1 blocked - T11 in flows) - payout-pending (your payout will arrive in a few minutes, on-chain settlement delay).

**Loss Screen** - "Here's what happened." Plain-language resolution note (what resolved and why), amount lost, one clear next step (not "bet again" promo). This screen is undesigned by every competitor - it is our primary retention intervention against loss-chasing (FJ5 + EJ3 confirmed gap).
Design rationale: the resolution note is the default beat before any re-bet (intervention against loss-chasing, per product strategy O1 trust over O4 volume). Friction is calm, non-punitive, and non-blocking - the user can always proceed. The escalation branch in IA/flows.md FJ5 routes through an explicit pause node before reaching Bet Screen. Reserved: session-aware chasing check (C-logic), post-MVP, not built in this pass.
States: loading (resolution note fetching).
Note: Cancelled-event refund flow is deferred to post-MVP, so no refund/payout state exists on this screen at MVP.

---

### MY BETS - follow active positions and history

User returns to check how their positions are moving (position monitoring behavioral pattern).

```
Active Bets                                  (EJ1 - position monitoring)   ⭐ PRIMARY + 🥈 SECONDARY
Bet History                                  (EJ1)                          ⭐ PRIMARY + 🥈 SECONDARY
```

**Active Bets** - list of open positions: event name, direction, current market value vs entry, deadline. Drives hot-return behavior (check odds, aarrr.md retention D1–D3).
States: loading (fetching positions) - empty-new (new user, no bets placed yet: CTA to Event Feed to find events) - empty-resolved (all positions closed: CTA to History tab to see resolved bets) - error (failed to load positions - retry CTA).

**Bet History** - private view of one's own resolved bets: won/lost, payout, event outcome. The public track record lives on My Profile and Public Profile, not here. G5 resolved: Bet History is now the History tab inside My Bets (Active Bets screen), not a standalone screen.
States: loading (fetching resolved bets) - empty (no resolved bets yet: CTA to Event Feed to find events) - error (failed to load resolved bets - retry CTA).

---

### NOTIFICATIONS - return trigger

Discovered in tracing: FJ1, FJ5, EJ3 depend on delivery via notification - entity without a screen. Without a list screen, users see alerts in OS only (no in-app history, no way to recover a missed alert).

```
Notifications                                (FJ1 · FJ5)    ⭐ PRIMARY + 🥈 SECONDARY
```

**Notifications** - list of unread and recent alerts: odds moved significantly · event deadline approaching · position resolved · new event in followed category. Tapping any item navigates to the relevant screen (Event Detail or Active Bets). Notification types map directly to the hot/warm return signals in aarrr.md retention model (D1–D3).
States: loading (fetching list) - empty (no notifications yet - new user or no events followed) - error (notifications failed to load - retry CTA) - push-permission-missing (OS push denied: show in-app banner "Enable notifications to get live updates" with system settings deep-link).

Note: Settings / Notification Preferences remains `[SIROTA]` - configuring which notifications you receive is not a confirmed job. The list screen (above) is sufficient for MVP. [?] Q-notif-prefs open question: does the user need per-event mute controls, or is category-level preference sufficient? Cannot be derived from current research - defer to user testing.

---

### WALLET - money in and out

Standalone money management, reached outside the betting flow.

```
Wallet                                       (FJ4)          ⭐ PRIMARY + 🥈 SECONDARY
```

**Wallet** - available balance, in-play balance, transaction history (deposits, payouts, fees, withdrawals), deposit again (same Deposit screen). Funds protection message visible here too (EJ2 secondary). Single screen at this depth.
States: loading (initial balance fetch) - error (wallet data failed to load - retry CTA).
Deferred state: balance-syncing (cosmetic, momentary sync delay between on-chain confirmation and UI update) - deferred to wireframe spec.

Withdrawal flow (not a separate screen - a flow inside Wallet): enter amount, enter destination USDC address (MVP) or PIX (Phase 2 Brazil), confirm, states: pending/confirmed/failed. Withdrawal is always in crypto (USDC) for MVP - no fiat payout rail at launch.

---

### PROFILE - public reputation

The "I called it" identity surface. Accessible to others, not just the account owner.

```
My Profile                                   (SJ1 · SJ2)    ⭐ PRIMARY + 🥈 SECONDARY
Public Profile (another user)                (SJ2)          🥈 SECONDARY > ⭐ PRIMARY
```

**My Profile** - prediction track record: total bets, win rate, history of resolved bets (public). Share card gallery (past wins). Editable display name and avatar.
States: loading (profile data fetching) - error (profile failed to load - retry CTA).
Deferred state: empty-state (cosmetic, first-time user with no predictions yet) - deferred to wireframe spec.

**Public Profile** - same data, read-only, for another user. Dan uses this more (reputation-first behavior). Alex arrives here via a shared win card or leaderboard - secondary path for him.
States: loading (profile data fetching) - error (failed to load: retry CTA or return to Event Feed) - not-found / link-expired (this profile no longer exists or the link has expired: CTA to Event Feed).

---

### HOW IT WORKS - trust anchor

Pre-bet trust signal for new users who want to understand before committing money.
Reachable from Deposit screen ("learn more" link) and from main navigation - accessible before the user has deposited anything. FJ4 closes here for users who need reassurance before their first deposit.

```
How It Works                                 (FJ4 · EJ2)    ⭐ PRIMARY
```

**How It Works** - funds protection (one sentence: "Your USDC is held 1:1"), resolution process (who decides, what evidence, on-chain proof), resolved markets count as social proof (benchmark-trust.md Top 3 mechanisms). Not a FAQ - a trust declaration, written as a promise.

---

### ORPHANS `[SIROTA]` - no confirmed job maps here

Screens referenced in product docs but not derived from any jtbd.md job.
Do not build until a job is confirmed.

```
Settings / Notification Preferences         [SIROTA]        - notification prefs are adjacent to FJ1 return path but no job in jtbd.md requires a settings screen
Leaderboard                                 [SIROTA]        - no confirmed job; SJ2 is served by Profile; leaderboard is a view, not a job-closing screen
Help / FAQ                                  [SIROTA]        - EJ2 is served by Deposit + How It Works; a generic FAQ adds friction without closing a job
```

---

---

## Navigation

> Desktop note: the mobile navigation below is the source of truth and keeps all
> 4 bottom-nav slots (slot 4 is Portfolio after the wireframe pass, see the
> bottom-nav table). Its desktop mapping is a lean header (Events as the logo,
> My Bets and Profile in the avatar dropdown, Notifications and Favorites as icons
> in the utility cluster, a Portfolio / Cash balance swap, a reserved hamburger,
> and a second-level category nav under the header). Full detail in the Desktop layer
> (responsive, mobile-first) section directly after Navigation. The mobile content
> here is unchanged.

### User-model rationale

Navigation is derived from the user's job sequence, not from a competitor tab bar. The primary path is: **follow an event** (find what is happening in the world) → **place a stake** (confirm your opinion with real money) → **watch the position move** (return to track odds) → **return for the resolution** (see what happened and how you did) → **build reputation** (show you were right). The original mapping gave each bottom slot one loop phase. The wireframe pass refined this: the mobile bottom bar is now Events, My Bets, Favorites, and Portfolio. Notifications moved to a header bell (its badge still drives return, see the Notifications placement note). Money and reputation are no longer a separate "never a top slot" rule on mobile: they are merged into the Portfolio account hub, which surfaces a balance but opens the identity / account hub rather than a bare trading wallet, so the feed stays the event-first hero (G4 spirit, see D-desktop-4 and the Wallet / Deposit row).

### Bottom navigation - 4 slots

**Notifications placement (revised in the wireframe pass):** Notifications is now a header bell with a permanent badge on both breakpoints, NOT a bottom-nav slot. The earlier reasoning (the badge must sit in the bottom thumb zone) was reconsidered: the unread badge drives hot/warm return (FJ1, FJ5, EJ3; aarrr.md D1-D3) by being VISIBLE, and a top-right bell with a count is visible too. The thumb slot is more valuable for a destination users actively navigate to, so it was given to Favorites (Saved). Notifications and Favorites were swapped: Notifications to the header, Favorites to the bottom bar on mobile.

| Slot | Label | Opens | Jobs served | Why it earns a top-level slot |
|---|---|---|---|---|
| 1 | **Events** | Event Feed | FJ1, FJ2, MJ | The entry point. Users open the app because something happened in the world. Every session starts here. |
| 2 | **My Bets** | Active Bets (two tabs: Active / History) | EJ1, MJ, FJ5, EJ3 | The position monitor. Users return specifically to track odds movement and see resolved bets. History tab implements G5: Bet History becomes a tab inside Active Bets, not a standalone screen. EJ1 coverage is preserved. |
| 3 | **Favorites** | Saved view (a filter over the Event Feed) | FJ1 (return / watchlist) | Revised in the wireframe pass. The mobile thumb slot for actively filtering to saved events (your watchlist). On desktop, Favorites is a heart icon in the header instead. Notifications, which used to hold this slot, is now a header bell on both breakpoints (its badge stays visible, so its retention role is preserved). Caveat: Saved is a newer, partially-confirmed feature; revisit this slot if usage data is low. |
| 4 | **Portfolio** | My Profile, extended with a portfolio summary on top (Portfolio = Cash + In-play, plus Deposit / Wallet), above the track record. Combined account / identity hub. | SJ1, SJ2, FJ4 | Revised in the wireframe pass. The slot shows the portfolio balance figure instead of an icon (label "Portfolio"); it opens the account hub, identity plus money. Reputation (SJ1/SJ2) stays first-class here; the balance is surfaced because the mobile header drops the balance for space. |

> Slot 4 change (wireframe pass): the mobile slot 4 was **Profile** (My Profile, SJ1/SJ2). It is now **Portfolio**, a combined account hub that opens My Profile extended with a portfolio summary (Portfolio / Cash + a Deposit / Wallet entry) above the track record. This is a deliberate, documented partial override of G4: the slot surfaces a balance, but the destination is the identity / account hub, not a bare trading wallet, so the platform still reads event-first rather than terminal-like. Profile is no longer a separate slot; reputation is reached inside this hub (and via the desktop avatar). My Bets (positions / history) is untouched, so there is no duplication.

> Bottom-nav icons (wireframe pass): all four slots carry an icon. Slot 4 (Portfolio) shows the balance figure in place of the icon, with the label below.

### Header and second-level

| Entry | Where | Why NOT a bottom slot |
|---|---|---|
| **Wallet / Deposit** | Avatar dropdown (desktop) and inside the Portfolio hub (mobile); re-deposit also invoked in context from the Bet Screen | Money is not why users open the app. Re-deposit is solved in context: Bet Screen insufficient-balance state invokes Deposit directly (1 step). G4 holds on desktop (money is a utility, not a slot). Mobile nuance (wireframe pass): the balance is surfaced in the Portfolio slot, but that slot opens the account / identity hub, not a bare Wallet, so the event-first read is preserved. A pure standalone Wallet bottom slot is still rejected. |
| **How It Works** | Header info icon accessible from Events; also linked from Deposit | Pre-bet trust signal for new users, reachable before deposit and before sign-in. Not a recurring destination - a one-time reassurance step inside FJ4/EJ2. A bottom slot would waste a scarce position on a screen most users visit once. |
| **My Profile (avatar)** | Header avatar dropdown (desktop); on mobile, My Profile is reached via the Portfolio bottom slot (account hub) | Quick identity access without leaving the Events context. After the wireframe pass there is no separate Profile bottom slot; reputation (SJ1/SJ2) is reached via the Portfolio account hub on mobile and the avatar on desktop. |
| **Notifications (bell)** | Header bell with a permanent unread badge, both breakpoints | Revised in the wireframe pass: moved out of the bottom bar. The badge stays permanently visible (retention anchor, FJ1/FJ5/EJ3), and the thumb slot it vacated went to Favorites. The bell opens the Notifications list for in-app recovery of missed alerts. |
| **Favorites (heart)** | Header heart icon on desktop; bottom-nav slot on mobile | Opens the Saved view. On mobile it earns the thumb slot for active filtering to the watchlist; on desktop it is a header utility. |

### Not navigation destinations

These screens are reached only inside a flow, triggered by a user action. They are never a bottom-nav slot and cannot be reached by tapping the nav bar:

- **Bet Screen** - invoked when user taps YES or NO on Event Detail.
- **Win Screen** - invoked when a bet resolves with a win (via notification or resolved item in Active Bets).
- **Loss Screen** - invoked when a bet resolves with a loss (G1 direct: 1 tap from resolution notification; or via resolved item in Active Bets).
- **Sign In / Register** - invoked at the activation gate (Confirm tap on Bet Screen), never before the user has bet intent.
- **Deposit** - invoked at the activation gate (News Junkie path post-auth) and from Wallet (standalone top-up).

### Deferred

| Item | Status | Reason |
|---|---|---|
| **Public Profile** | Deferred to post-MVP (G3) | Reachable only via external shared-card link for MVP. No in-app discovery at 10-20 curated markets: users do not browse others' track records unprompted. In-app path added when leaderboard or social discovery is confirmed. |
| **Search** | Deferred until catalog scale | At 10-20 curated markets, users scan the Event Feed; they do not search. Search does not close a confirmed job at this scale. When added, it attaches to the Events tab under FJ1 - not a bottom slot. |
| **Leaderboard** | [SIROTA] | No confirmed job. SJ2 is served by My Profile and Public Profile. Leaderboard is a view over profiles, not a job-closing destination. |
| **Responsible-play slot (D-logic)** | Reserved, post-MVP, not built | Account-level deposit and loss limits, cooldown period, self-exclusion. Mandatory for Brazil Phase 2 (Law 14.790 / Ordinance 1,231 self-exclusion and responsible-gambling requirements). Do not discover this late. |

---

## Desktop layer (responsive, mobile-first)

The product is mobile-first and responsive. The mobile layer above is unchanged
and remains the structural source of truth: the same 4 destinations, the same
header utilities, the same jobs. The desktop layer below is the same IA derived
from the same jobs, expanded at wider widths via min-width. It introduces no new
destination, no new job, and no new entity. Each decision below resolves a
desktop question; none of them changes a mobile decision.

### D-desktop-1: Primary navigation

> Revised in the wireframe pass (lean header). The earlier "3 destinations in a
> center top nav" framing is superseded by the lean-header model below. Mobile is
> unchanged.

- **Mobile (revised in the wireframe pass):** bottom nav, 4 slots with icons, in
  the thumb zone: Events, My Bets, Favorites, and Portfolio. Notifications is not
  a bottom slot (it is the header bell, see D-desktop-2); Profile is not a bottom
  slot (reached via the Portfolio account hub). Slot 4 (Portfolio) shows the
  portfolio balance in place of an icon.
- **Desktop (lean header):** the desktop header does not carry a center row of
  text nav items. Primary destinations are placed as follows:
  - **Events** is the logo: clicking the brand returns to the Event Feed (home).
  - **My Bets** lives in the avatar dropdown (see D-desktop-4).
  - **Notifications** is a bell icon with a permanent unread badge in the right
    utility cluster (see D-desktop-2).
  - **Profile** is the avatar in the utility cluster (resolves the earlier
    Profile duplication; the avatar is Profile's home on desktop).
  - **Favorites** (Saved view) is a heart icon in the utility cluster.
  - A **hamburger** icon sits at the left, reserved for future scaling; it holds
    no primary items at MVP (Events is the logo, My Bets is in the avatar menu).
- **Second-level navigation:** the categories (Trending default, Politics,
  Crypto, Culture, General) are a second-level sub-nav band directly under the
  header. Categories are navigation (second level); the feed sort control is a
  feed control on the "Live events" heading row, not navigation. See the Event
  Feed screen description.
- **Final desktop header composition:** left: hamburger (reserved) + logo (=
  Events home). Right utility cluster: Portfolio / Cash balance swap, Favorites
  (heart), Notifications (bell + badge), avatar (dropdown). Second-level category
  nav under the header.
- **Mobile-to-desktop mapping:** mobile bottom bar (Events, My Bets, Favorites,
  Portfolio) plus header bell and avatar -> lean desktop header where Events is
  the logo, My Bets and Profile fold into the avatar menu, Notifications and
  Favorites are icons in the cluster, and the Portfolio balance is the cluster
  swap. No destination is lost.
- **Job rationale:** keeps the header short and event-first (the feed is the
  hero), consistent with G4 (do not signal a trading terminal). Tradeoff to note:
  My Bets on desktop is one level deeper (inside the avatar menu) than the locked
  bottom-nav slot it keeps on mobile; the user accepted this for a lean header,
  and the hamburger is reserved to surface more nav as the app scales.

### D-desktop-2: Notifications badge

- **Decision (revised in the wireframe pass):** on desktop, Notifications is a
  bell icon in the right utility cluster, carrying a permanent unread badge. The
  earlier rule (keep it as a text item in a center primary nav, not a bell) is
  superseded by the lean-header model in D-desktop-1.
- **Requirement that is preserved:** the badge is permanently visible. It rides
  on the bell icon, so the retention anchor is kept even though the item is now
  an icon, not a labeled nav item.
- **Header bell on both breakpoints (revised in the wireframe pass):** the bell
  with its badge lives in the header at all widths. Notifications no longer holds
  a bottom-nav slot; it was swapped with Favorites (which took the mobile slot).
  The badge is visible whether at the top or the bottom, so the retention anchor
  is preserved; the scarce thumb slot is spent on a more actively-navigated
  control (Favorites / Saved). This overturns the earlier "Notifications must be
  a bottom slot" decision (see the bottom-nav table note).
- **Mobile-to-desktop mapping:** bell icon with badge in the header, the same at
  both breakpoints. Not duplicated anywhere.
- **Job rationale:** the locked retention requirement is that the unread badge is
  permanently visible to drive hot and warm return (FJ1, FJ5, EJ3; aarrr D1-D3).
  The badge-on-bell satisfies "always visible". The label-versus-icon treatment
  was a wireframe detail; the user chose the icon for a lean header, and the
  required property (a permanently visible badge) is unchanged.

### D-desktop-3: Event Feed grid

- **Mobile:** single column.
- **Desktop:** a responsive card grid, mobile-first. Columns are determined by
  how many cards fit at a minimum card width that still guarantees the context
  snippet line on the card (target minimum card width around 280px). This yields
  up to 4 cards per row on a wide desktop, 3 at medium width, 2 below that, 1 on
  mobile.
- **Hard lock:** the per-card context snippet (the one-line teaser of "why this
  price") is never dropped to fit more columns. The snippet is the single
  differentiator that separates our card from a competitor's bare-percentage
  card; full context still lives on Event Detail where FJ2 closes, but the card
  teaser is what makes the feed ours. Density is achieved by the responsive
  grid, not by removing the snippet. Competitors reach 4-per-row precisely
  because their card carries nothing but the percentage; matching their density
  must not cost us the snippet.
- **Job rationale:** FJ2 differentiator (master-research gap, no competitor
  explains the price). Density up to 4 per row is desired and allowed; the
  min-width rule is the guardrail that keeps the snippet, not a cap on density.

### D-desktop-4: Header utilities

- **Mobile (revised in the wireframe pass):** the lean header right side holds
  the Notifications bell (with badge) and the avatar. Favorites moved to the
  bottom bar (swapped with Notifications). Balance is not in the mobile header
  (it is in the Portfolio bottom slot); How It Works lives in the avatar dropdown
  and the footer; Deposit lives in the avatar dropdown and the Portfolio hub.
  Money is still not a header destination (G4 spirit preserved).
- **Desktop (revised in the wireframe pass):** a right-hand utility cluster,
  visually secondary, holds: **Balance as a Portfolio / Cash swap** (one figure
  at a time, a swap icon toggles Portfolio = Cash + In-play, default, and Cash =
  available; not two figures like competitors), **Favorites** (heart icon, opens
  the Saved view), **Notifications** (bell icon + permanent badge, see
  D-desktop-2), and the **avatar** (dropdown). A standalone Deposit button is
  NOT in the header; Deposit is reached from the avatar dropdown (Wallet /
  Deposit) and in context from the Bet Screen insufficient-balance state.
- **Mobile:** the balance is removed from the header (no room at small widths;
  a large figure would overflow at 360px) and is surfaced in the Portfolio bottom
  slot instead (see the Navigation bottom-nav table). The bell is also removed
  from the mobile header (Notifications is the bottom-bar slot there).
- **Avatar dropdown (desktop):** collapsed by default, opens on click. Populated
  from OUR IA only, not from competitor menus: My Profile (SJ1/SJ2), My Bets
  (EJ1), Wallet / Deposit (FJ4), How It Works (FJ4/EJ2), Logout. Do NOT add
  Leaderboard (it is [SIROTA]), Rewards, or APIs (not our product).
- **How It Works placement:** removed from any persistent header bar position; it
  lives in the footer and in the avatar dropdown. Pre-deposit access is preserved
  (footer plus dropdown, both reachable before deposit).
- **Mobile-to-desktop mapping:** mobile header icons (wallet/balance, info,
  avatar) -> desktop utility cluster (Balance, Favorites, Notifications bell,
  avatar with dropdown), with How It Works in the footer and the dropdown, and
  My Bets folded into the dropdown.
- **Job rationale:** G4 carries over intact: money is a utility (Balance text,
  Deposit in the avatar menu), not a primary destination; promoting Wallet to a
  primary slot would signal a trading terminal and is rejected.
- **Deferred / folded utilities:**
  - Language switcher: deferred to Phase 2 (Brazil, Portuguese). English-first
    MVP needs no switcher.
  - Swap / transfer icon: folded into Wallet (withdrawal and transfer are a
    Wallet flow), not a standalone header icon.

### D-desktop-5: Invoked screens as modal overlays (both breakpoints)

- **Decision:** the invoked screens (Bet Screen, Sign In / Register, Deposit,
  Win Screen, Loss Screen) are presented as an overlay in context, not as a
  separate full-page destination, on both breakpoints. Desktop: a centered modal
  over the feed. Mobile: a full-height bottom sheet. The user stays in context;
  they are not thrown across separate screens.
- **Multi-step stack:** the activation gate (Sign In then Deposit) and the S5
  reconcile step on Bet Screen run as a multi-step stack inside the same overlay.
- **Mobile-to-desktop mapping:** in-context overlay on both breakpoints -
  centered modal on desktop, full-height bottom sheet on mobile.
- **Consistency with locked IA:** this aligns with the G1 nav decision already
  in IA/sitemap.md and IA/flows.md, where a notification tap "opens target
  modally over the current tab". Modal presentation of invoked screens extends
  G1, it does not contradict it. The invoked screens remain non-navigation
  destinations (they are still never a nav slot), exactly as the locked "Not
  navigation destinations" list states.
- **Job rationale:** preserves the feed context during the bet, sign-in, and
  deposit steps; matches the in-context routing already chosen for
  notifications.

### Breakpoint principle

Mobile is the base; desktop is a min-width expansion. The exact pixel thresholds
are a wireframe and convention detail (to be set in wireframes/_conventions.md),
not fixed here. Only the relative order is fixed: the Event Feed grid goes from 1
column on mobile, to 2, to 3, and up to 4 on a wide desktop, per D-desktop-3, and
the mobile bottom nav is replaced on desktop by the lean header (logo, avatar
dropdown, and utility-cluster icons) per D-desktop-1.

---

## Depth Map

Navigation depth for each screen in the inventory. Used to verify the 3-tap rule for the primary persona (Alex, News Junkie).

### Hierarchy

```
Level 0 - bottom nav destinations (1 tap from anywhere in the app)
  Events
    Event Feed
  My Bets
    Active Bets (Active tab - default view)
    Bet History (History tab inside My Bets - G5 merge)
  Favorites (mobile slot 3; on desktop a header heart icon)
    Saved view (a filter over the Event Feed)
  Portfolio (mobile slot 4; on desktop via the avatar + the header balance swap)
    My Profile, extended with a portfolio summary (Portfolio / Cash + Deposit) above the track record

Level 1 - one tap below a Level 0 screen
  under Events:
    Event Detail (tap any event card on Event Feed)
  via the header (available at Level 0):
    Notifications list (header bell, both breakpoints)
    Wallet / Deposit (avatar dropdown, or inside the Portfolio hub)
    How It Works (avatar dropdown and footer, also linked from Deposit)

Flow / invoked - reached only inside a flow, not via nav bar
  Bet Screen        invoked: tap YES or NO on Event Detail
  Win Screen        invoked: bet resolves as win (notification tap or Active Bets resolved item)
  Loss Screen       invoked: bet resolves as loss (G1: notification tap direct; or Active Bets resolved item)
  Sign In / Register   invoked: activation gate (Confirm tap on Bet Screen)
  Deposit           invoked: activation gate (News Junkie path) or Wallet top-up button
  Public Profile    invoked: external shared-card link only (no in-app nav at MVP)
```

### Depth check - primary persona (Alex, News Junkie)

**MJ main job: Event Feed → Event Detail → Bet Screen**
- Events tab (Level 0) → tap event card → Event Detail (1 tap) → tap YES or NO → Bet Screen (2 taps) → Confirm (3 taps, activation gate fires here).
- Result: 2 taps to reach Bet Screen, 3 taps to trigger the gate. Within the 3-tap rule. Confirmed.

**G1 retention path: resolution notification → Loss Screen**
- Tap resolution notification (OS banner or Notifications list item) → Loss Screen directly (1 tap).
- Matches the G1 edge in IA/flows.md FJ5: `triggerNotif -->|"G1: direct to Loss Screen"| LS`.
- The manual fallback path (My Bets → tap resolved item → Loss Screen) is 2 taps. G1 cuts this to 1 tap so the resolution note reaches the user before the impulse to chase.
- Result: 1 tap from notification. Confirmed.

**Win Screen retention path: win resolution notification → Win Screen**
- Tap win resolution notification (OS banner or Notifications list item) → Win Screen directly (1 tap).
- Matches the G1-equivalent edge in IA/flows.md SJ1: `triggerNotif -->|"direct: 1 tap to Win Screen"| WS`.
- The manual fallback path (My Bets → History tab → tap won item → Win Screen) is 2 taps. The notification path ensures the share impulse window is not missed (SJ1).
- Result: 1 tap from notification. Confirmed.

**Returning-user re-deposit**
- Bet Screen insufficient-balance state shows inline: "you have $X, can bet up to $X or deposit more" with a direct CTA to Deposit.
- Result: invoked in context from Bet Screen, 1 step. Not a multi-tap trip to Wallet. Confirmed.

**Proactive top-up (revised in the wireframe pass)**
- Desktop: avatar dropdown → Wallet / Deposit → Deposit (2 taps). Mobile: Portfolio bottom slot → Deposit / Wallet entry in the hub → Deposit (2 taps). 2 taps, acceptable. (There is no standalone header wallet icon anymore; Deposit lives in the avatar dropdown and the Portfolio hub.)

### Depth risks

No depth risks for the primary persona's confirmed jobs at this navigation structure. All primary-persona paths reach their destination in 3 taps or fewer, with contextual shortcuts where the job depends on speed (G1, re-deposit).

Flag for wireframes: the manual path to Loss Screen via My Bets depends on the user noticing the resolved item in Active Bets. Consider a resolved-bets badge or a "recently resolved" section above the fold in Active Bets so the item is not missed below active positions.

---

## Tracing

> Jobs: 11 confirmed (MJ + FJ1-5 + EJ1-3 + SJ1-2). HJ1-4 excluded - hypotheses without data, not confirmed jobs.
> ✓ = screen genuinely participates in closing the job. Empty = does not.
> Column codes defined in legend below.

### Coverage Matrix

OB (Onboarding) column removed - screen removed in Step 2. BH x SJ2 corrected: Bet History is a private view, SJ2 requires public visibility.

| Job | EF | ED | SI | DEP | BS | WS | LS | AB | BH | WA | MP | PP | HIW | NT |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **MJ** - real stake on an event | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | |
| **FJ1** - find the event while it is still relevant | ✓ | ✓ | | | | | | | | | | | | ✓ |
| **FJ2** - understand why the market prices it that way | ✓ | ✓ | | | | | | | | | | | | |
| **FJ3** - bet without a crypto barrier | | | ✓ | ✓ | ✓ | | | | | ✓ | | | | |
| **FJ4** - feel confident the money is safe | | | | ✓ | | | | | | ✓ | | | ✓ | |
| **FJ5** - survive a loss without chasing | | | | | | | ✓ | ✓ | | | | | | ✓ |
| **EJ1** - feel I understand better than most | | ✓ | | | | ✓ | | ✓ | ✓ | | ✓ | | | |
| **EJ2** - feel safe before the first deposit | ✓ | | | ✓ | | | | | | | | | ✓ | |
| **EJ3** - exit a loss consciously | | | | | | | ✓ | ✓ | | | | | | |
| **SJ1** - show that I was right | | | | | | ✓ | | | | | ✓ | | | |
| **SJ2** - build a public track record | | | | | | | | | | | ✓ | ✓ | | |
| **Coverage (jobs)** | 4 | 4 | 2 | 4 | 2 | 3 | 3 | 4 | 1 | 2 | 3 | 1 | 2 | 2 |

**Column legend:**
EF = Event Feed · ED = Event Detail · SI = Sign In / Register · DEP = Deposit · BS = Bet Screen · WS = Win Screen · LS = Loss Screen · AB = Active Bets · BH = Bet History · WA = Wallet · MP = My Profile · PP = Public Profile (another user) · HIW = How It Works · NT = Notifications

**Row coverage (screens per job):**
MJ 8 · FJ1 3 · FJ2 2 · FJ3 4 · FJ4 3 · FJ5 3 · EJ1 5 · EJ2 3 · EJ3 2 · SJ1 2 · SJ2 2

---

### Non-trivial checkmark rationale

| Cell | Why checked, not empty |
|---|---|
| FJ2 + EF | Event Feed in story-driven mode shows context on the card (not just %), partially closes "why this probability" before the user even taps into detail |
| EJ2 + EF | First impression of the product (benchmark-trust C5: 5/5 Bet365) is Event Feed without registration. Cognitive clarity on the first screen = first layer of EJ2 |
| FJ3 + BS | Bet Screen has $5 default pre-fill, quick-select buttons, and fee display - this is "bet without learning unfamiliar technology" at the confirm step |
| EJ1 + ED | Knowledge validation: user sees the probability and compares it to their own forecast - "market thinks 67%, I know better." The sense of edge emerges here |
| EJ1 + AB | Tracking price movement of their position (position monitoring) - intermediate confirmation that "I was right, price is moving my way" |
| FJ3 + WA | Wallet "Deposit again" button - re-entry into the top-up flow without a crypto barrier, for returning users |

---

### Defects

#### SCREEN ORPHANS - columns with no checkmarks

**No orphans.** All 14 screens are covered by at least one confirmed job.

Minimally covered screens (1-2 jobs) - not orphans, but worth attention:

| Screen | Jobs | Risk |
|---|---|---|
| **Public Profile** | SJ2 (1 job) | Weakest coverage. Justified: SJ2 requires other users to see the track record - without this screen the job physically cannot close. Keep. |
| **Bet Screen** | MJ + FJ3 (2 jobs) | Narrow role - a focused action, not a multi-purpose hub. Normal for an action screen. Keep. |
| **Bet History** | EJ1 (1 job) | BH x SJ2 removed: Bet History is a private view, SJ2 requires public-facing visibility. Corrected to EJ1 only. Lowest coverage in matrix - review merge with Active Bets in navigation pass. |
| **Wallet** | FJ3 + FJ4 (2 jobs) | Financial hub with a narrow role. Justified: without it there is nowhere to see balance or initiate withdrawal. Keep. |
| **How It Works** | FJ4 + EJ2 (2 jobs) | Pre-deposit access confirmed: reachable from main nav before deposit, not restricted to gate flow. Restriction from prior tracing note (modal only from Deposit + Onboarding) reversed - Onboarding removed, HIW now open. |

---

#### JOB ORPHANS - rows with no checkmarks

**No orphans.** All 11 confirmed jobs are covered by at least one screen.

Minimally covered jobs (2 screens) - not orphans, but worth attention:

| Job | Screens | Risk |
|---|---|---|
| **FJ1** - find the event while still relevant | EF + ED | Coverage exists, but FJ1 heavily depends on Notification (entity, not a screen). If notification does not fire, FJ1 does not close for returning users. Gap closed: Notifications screen added to sitemap and matrix (NT column). |
| **FJ5** - survive a loss without chasing | LS + AB | 2 screens are sufficient, but both depend on the user opening Loss Screen. If notification does not route to AB then LS, the job does not close. Same dependency on Notifications - gap closed by NT. |
| **EJ3** - exit a loss consciously | LS + AB | Same gap as FJ5. Both jobs resolved by the same solution: Notifications leads to Active Bets. |

---

### Tracing conclusion

**No confirmed orphans.** Matrix is closed: all 14 matrix columns have a job (Onboarding removed), all 11 jobs have a screen. BH x SJ2 corrected - Bet History now carries EJ1 only (1 job, lowest coverage). G5 resolved: Bet History is now a History tab inside My Bets, not a standalone screen. Standalone screen count is 13 (matrix columns unchanged at 14 - BH column preserved, now represents the History tab).

One systemic gap was found and closed during tracing: FJ1 / FJ5 / EJ3 depended on the Notification entity with no screen of its own. Notifications (NT) added to sitemap and matrix - gap resolved.

**Navigation design decisions (resolved in navigation pass):**

| Code | Decision |
|---|---|
| **G1 nav** | Deep-link routing: notification tap opens target (Loss Screen, Event Detail) modally over the current tab. Back returns to prior context. 1 tap from OS banner or Notifications list item to Loss Screen (G1 direct path). |
| **G3** | Public Profile reachable only via external shared-card link for MVP. No in-app discovery. Added when leaderboard or social features are confirmed. |
| **G4** | Wallet and Deposit live in the header, not a bottom-nav slot. Re-deposit is invoked from Bet Screen insufficient-balance state - 1 step in context. Refined in the wireframe pass: Deposit is in the avatar dropdown and the Portfolio hub (no standalone wallet icon); a Portfolio balance is surfaced on mobile via the account hub, not a bare Wallet slot. See D-desktop-4 and the Wallet / Deposit row. |
| **G5** | Bet History merged as History tab inside My Bets. EJ1 coverage preserved (private resolved bets view). Standalone screen count drops from 14 to 13; matrix column BH retained. |
| **S11** | Simultaneous resolutions: show a sequence of separate Win/Loss screens, swipeable. No aggregated Resolution Summary screen at MVP. Wireframe-spec detail, not a navigation slot. |

**Backlog (open):**
- Settings / Notification Preferences - remains `[SIROTA]` until a job is confirmed.
- Search - deferred until catalog scale (see Navigation - Deferred section).

---

## Navigation Design Pass - Resolved

All items deferred to the navigation pass are now resolved. See Navigation section and Depth Map above for full rationale.

| Code | Item | Decision |
|---|---|---|
| **G1 nav** | Notification routing nav pattern | Resolved. Notification tap opens target modally over the current tab; back returns to prior context. 1 tap from notification to Loss Screen (G1 direct path confirmed in FJ5 flow and Depth Map). |
| **G3** | In-app path to Public Profile | Resolved. MVP: external shared-card link only. No in-app discovery. In-app path deferred until leaderboard or social discovery is confirmed. |
| **G4** | Wallet and Deposit navigation placement | Resolved, then refined in the wireframe pass. Deposit lives in the avatar dropdown and the Portfolio hub (no standalone header wallet icon); re-deposit invoked from Bet Screen insufficient-balance state in context (1 step). A Portfolio balance is surfaced on mobile via the account hub, not a bare Wallet bottom slot. See D-desktop-4. |
| **G5** | Bet History placement and merge | Resolved. Bet History merged as History tab inside My Bets. EJ1 coverage preserved. Standalone screen count: 13. Matrix column BH retained. |
| **S11** | Aggregation of simultaneous resolutions | Resolved. Sequence of separate Win/Loss screens, swipeable. No aggregated Resolution Summary screen at MVP. Wireframe-spec detail. |
