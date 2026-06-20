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
| Type | Binary (YES/NO) · Multi-outcome (multiple options, each with YES/NO) |
| Category | Politics · Crypto · Culture · General |
| Current probability (%) | The "price" - primary display number on every card |
| Probability chart | History of odds movement over time |
| Context / narrative | Why this event matters, what drives the odds, key arguments for YES and NO ← **our differentiator (FJ2)** |
| Resolution conditions | What counts as YES, what source is authoritative |
| Status | Active · Resolved · Cancelled |
| Resolution deadline | When the event closes for new bets |
| Volume | Total USDC staked across all positions |
| Created by | Platform team (MVP) |

**Related to:** Bet · Resolution · Notification

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
| Joined date | - |

**Related to:** Bet · Wallet · Profile · Notification

---

### 4. Wallet (Balance)

The user's financial state on the platform. Separate from User because it has its own lifecycle: deposit, lock, payout, withdrawal.

**Jobs served:** FJ3 · FJ4 · EJ2

| Field | Notes |
|---|---|
| Available balance (USDC) | Ready to bet |
| In-play balance (USDC) | Locked in active bets |
| Total deposited (lifetime) | For KYC threshold tracking |
| Transaction history | Deposits · Withdrawals · Payouts · Fees |
| Connected address | If self-custody wallet; empty if custodial |

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

**Event Feed** - cards of active markets, sorted by recency / trending. For the first visit: story-driven format (context visible on card, not just %). For return visits: denser feed. No sign-in required to browse.
States: loading (initial data fetch) - empty (no events match current filter or category) - error (network fail, API unreachable).
Note: push-permission-missing banner also surfaced on Event Feed when OS push is denied (see Notifications states).

**Event Detail** - one event, full view: probability, chart, narrative context (why this price), resolution conditions, source. CTA: YES / NO. This screen is our primary differentiator - no competitor has context at this depth (FJ2 confirmed gap).
States: loading (event data fetching) - error (load failure, T8 in MJ and FJ2 flows - retry returns to Event Detail) - resolved-while-reading (this event just resolved: [outcome] - navigate to Win/Loss Screen if user holds a position, else to Event Feed).

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
Per F5, the first win is the stronger escalation trigger (overconfidence). Share / mark the moment is the default next action; "see next events" is a deliberate secondary CTA, not the primary. Symmetric with the Loss intervention, shaped for overconfidence rather than impulse. Modeled in flows.md SJ1: share path is the primary edge, secondary "see next events" edge is labeled with the overconfidence risk.
States: loading (Share Card generation in progress) - error (Share Card not generated, SJ1 blocked - T11 in flows) - payout-pending (your payout will arrive in a few minutes, on-chain settlement delay).

**Loss Screen** - "Here's what happened." Plain-language resolution note (what resolved and why), amount lost, one clear next step (not "bet again" promo). This screen is undesigned by every competitor - it is our primary retention intervention against loss-chasing (FJ5 + EJ3 confirmed gap).
Design rationale: the resolution note is the default beat before any re-bet (intervention against loss-chasing, per product strategy O1 trust over O4 volume). Friction is calm, non-punitive, and non-blocking - the user can always proceed. The escalation branch in flows.md FJ5 routes through an explicit pause node before reaching Bet Screen. Reserved: session-aware chasing check (C-logic), post-MVP, not built in this pass.
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

### User-model rationale

Navigation is derived from the user's job sequence, not from a competitor tab bar. The primary path is: **follow an event** (find what is happening in the world) → **place a stake** (confirm your opinion with real money) → **watch the position move** (return to track odds) → **return for the resolution** (see what happened and how you did) → **build reputation** (show you were right). Each bottom-nav slot maps directly to one phase of this loop. Service-layer concerns - money, history, other users, help - are not part of the active loop and live at the second level or are invoked in context, never given a scarce top-level slot.

### Bottom navigation - 4 slots

**Alternative considered and set aside:** a 3-slot version placing Notifications as a header bell icon, saving one bottom slot. Set aside because the unread badge is a retention anchor - it must be permanently visible in the thumb zone to drive hot/warm return (FJ1, FJ5, EJ3 depend on it; aarrr.md D1-D3). A header bell is easy to miss on mobile. The badge in the bottom bar earns its slot.

| Slot | Label | Opens | Jobs served | Why it earns a top-level slot |
|---|---|---|---|---|
| 1 | **Events** | Event Feed | FJ1, FJ2, MJ | The entry point. Users open the app because something happened in the world. Every session starts here. |
| 2 | **My Bets** | Active Bets (two tabs: Active / History) | EJ1, MJ, FJ5, EJ3 | The position monitor. Users return specifically to track odds movement and see resolved bets. History tab implements G5: Bet History becomes a tab inside Active Bets, not a standalone screen. EJ1 coverage is preserved. |
| 3 | **Notifications** | Notifications list | FJ1, FJ5, EJ3 | The return trigger. Badge drives hot/warm return (aarrr.md D1-D3). Without a permanent bottom slot with unread count, FJ1/FJ5/EJ3 depend on OS alerts only with no in-app recovery path for missed alerts. |
| 4 | **Profile** | My Profile | SJ1, SJ2 | Reputation is a first-class product value for the News Junkie: "I was right, publicly" is why they share. Not an account settings screen - earns a slot as the identity surface. |

### Header and second-level

| Entry | Where | Why NOT a bottom slot |
|---|---|---|
| **Wallet / Deposit** | Header icon (wallet icon), also accessible via Profile | Money is not why users open the app. Re-deposit for returning users is solved in context: Bet Screen insufficient-balance state invokes Deposit directly (1 step, no multi-tap trip to a Wallet tab). A Wallet bottom slot would signal "trading terminal"; this platform is event-first. (G4 decision) |
| **How It Works** | Header info icon accessible from Events; also linked from Deposit | Pre-bet trust signal for new users, reachable before deposit and before sign-in. Not a recurring destination - a one-time reassurance step inside FJ4/EJ2. A bottom slot would waste a scarce position on a screen most users visit once. |
| **My Profile (avatar)** | Header avatar shortcut in addition to Profile tab | Quick identity access without leaving the Events context. Does not replace the Profile bottom slot - the slot is the primary destination for SJ1/SJ2. |

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
  Notifications
    Notifications list
  Profile
    My Profile

Level 1 - one tap below a Level 0 screen
  under Events:
    Event Detail (tap any event card on Event Feed)
  under Profile (via header - available at Level 0):
    Wallet (tap header wallet icon)
    How It Works (tap header info icon, also linked from Deposit)

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
- Matches the G1 edge in flows.md FJ5: `triggerNotif -->|"G1: direct to Loss Screen"| LS`.
- The manual fallback path (My Bets → tap resolved item → Loss Screen) is 2 taps. G1 cuts this to 1 tap so the resolution note reaches the user before the impulse to chase.
- Result: 1 tap from notification. Confirmed.

**Win Screen retention path: win resolution notification → Win Screen**
- Tap win resolution notification (OS banner or Notifications list item) → Win Screen directly (1 tap).
- Matches the G1-equivalent edge in flows.md SJ1: `triggerNotif -->|"direct: 1 tap to Win Screen"| WS`.
- The manual fallback path (My Bets → History tab → tap won item → Win Screen) is 2 taps. The notification path ensures the share impulse window is not missed (SJ1).
- Result: 1 tap from notification. Confirmed.

**Returning-user re-deposit**
- Bet Screen insufficient-balance state shows inline: "you have $X, can bet up to $X or deposit more" with a direct CTA to Deposit.
- Result: invoked in context from Bet Screen, 1 step. Not a multi-tap trip to Wallet. Confirmed.

**Proactive top-up: header wallet icon → Wallet → Deposit**
- Tap header wallet icon → Wallet (1 tap) → Deposit CTA → Deposit (2 taps). 2 taps, acceptable.

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
| **G4** | Wallet and Deposit live in the header (wallet icon), not a bottom-nav slot. Re-deposit is invoked from Bet Screen insufficient-balance state - 1 step in context. |
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
| **G4** | Wallet and Deposit navigation placement | Resolved. Wallet/Deposit lives in the header (wallet icon), not a bottom-nav slot. Re-deposit invoked from Bet Screen insufficient-balance state in context (1 step). |
| **G5** | Bet History placement and merge | Resolved. Bet History merged as History tab inside My Bets. EJ1 coverage preserved. Standalone screen count: 13. Matrix column BH retained. |
| **S11** | Aggregation of simultaneous resolutions | Resolved. Sequence of separate Win/Loss screens, swipeable. No aggregated Resolution Summary screen at MVP. Wireframe-spec detail. |
