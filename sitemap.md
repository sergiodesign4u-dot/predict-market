# Sitemap - Prediction Market Platform

> Status: pre-wireframe refinement complete. Navigation structure and screen depth TBD (navigation design pass).
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

**Event Detail** - one event, full view: probability, chart, narrative context (why this price), resolution conditions, source. CTA: YES / NO. This screen is our primary differentiator - no competitor has context at this depth (FJ2 confirmed gap).
States: loading (event data fetching) - error (load failure, T2 in MJ flow / T10 in FJ2 flow - user exits).

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
States: in-progress (OAuth redirect pending, wallet connect prompt open) - error (auth failed - T4, wallet connect failed - T7).

**Deposit** - fiat card to USDC via Transak (primary), MoonPay (fallback). KYC runs inside the Transak widget - the user completes identity verification there, not on this platform. Risk block displayed inline before the user submits: "Your USDC is held 1:1 - we do not lend or invest deposited funds." Fee shown before submit. Also reachable standalone from Wallet for top-ups.
States: in-progress (Transak widget loading, KYC pending inside widget) - error-card (card declined - T5) - error-KYC (KYC rejected - T6).

---

### BET - place and confirm a bet

Reached from Event Detail when the user taps YES or NO. No auth required to reach it - the user is still logged out at this point (Variant B).
Auth and deposit happen only at the confirm step, via the activation gate.

```
Bet Screen                                   (MJ · FJ3)     ⭐ PRIMARY + 🥈 SECONDARY
```

**Bet Screen** - direction (YES/NO, pre-set from tap on Event Detail), amount input with default $5 pre-fill, quick-select ($5/$10/$25/$50), fee displayed before confirm ("platform earns $X if you win"), potential payout shown. Confirm button triggers the activation gate for logged-out users. Single screen: intent and confirmation in one place.
States: intent (logged out - user builds the bet, no auth yet) - S5-reconcile (price moved during gate: shows old price vs new price, user must re-confirm) - error (bet registration failed on-chain - T9).

---

### RESOLUTION - what happened after the event closes

Triggered by a notification or by the user opening an Active Bet that has resolved.

```
Win Screen                                   (EJ1 · SJ1)    ⭐ PRIMARY + 🥈 SECONDARY
Loss Screen                                  (FJ5 · EJ3)    ⭐ PRIMARY + 🥈 SECONDARY
```

**Win Screen** - "You were right." Amount won, resolution summary (what happened and why), Share Card auto-generated. CTA: Share · See next events. Design rationale: no confetti loop, no persistent celebration animation. Research finding F5 (master-research.md): first WIN is the trigger for overconfidence and escalation, not loss. The win screen must celebrate the outcome without feeding the loop. Celebratory but measured - one moment, then move on.
States: loading (Share Card generation in progress) - error (Share Card not generated, SJ1 blocked - T14 in flows).

**Loss Screen** - "Here's what happened." Plain-language resolution note (what resolved and why), amount lost, one clear next step (not "bet again" promo). This screen is undesigned by every competitor - it is our primary retention intervention against loss-chasing (FJ5 + EJ3 confirmed gap).
States: loading (resolution note fetching).

---

### MY BETS - follow active positions and history

User returns to check how their positions are moving (position monitoring behavioral pattern).

```
Active Bets                                  (EJ1 - position monitoring)   ⭐ PRIMARY + 🥈 SECONDARY
Bet History                                  (SJ2 · EJ1)                   ⭐ PRIMARY + 🥈 SECONDARY
```

**Active Bets** - list of open positions: event name, direction, current market value vs entry, deadline. Drives hot-return behavior (check odds, aarrr.md retention D1–D3).
States: loading (fetching positions) - empty (no active bets - new user or all bets resolved).

**Bet History** - all resolved bets: won/lost, payout, event outcome. Feeds the public profile track record (SJ2). Could be the same screen as Active Bets with a tab - depth decision deferred to step 3.

---

### NOTIFICATIONS - return trigger

Discovered in tracing: FJ1, FJ5, EJ3 depend on delivery via notification - entity without a screen. Without a list screen, users see alerts in OS only (no in-app history, no way to recover a missed alert).

```
Notifications                                (FJ1 · FJ5)    ⭐ PRIMARY + 🥈 SECONDARY
```

**Notifications** - list of unread and recent alerts: odds moved significantly · event deadline approaching · position resolved · new event in followed category. Tapping any item navigates to the relevant screen (Event Detail or Active Bets). Notification types map directly to the hot/warm return signals in aarrr.md retention model (D1–D3).
States: loading (fetching list) - empty (no notifications yet - new user or no events followed).

Note: Settings / Notification Preferences remains `[SIROTA]` - configuring which notifications you receive is not a confirmed job. The list screen (above) is sufficient for MVP. [?] S11 open question: does the user need per-event mute controls, or is category-level preference sufficient? Cannot be derived from current research - defer to user testing.

---

### WALLET - money in and out

Standalone money management, reached outside the betting flow.

```
Wallet                                       (FJ4)          ⭐ PRIMARY + 🥈 SECONDARY
```

**Wallet** - available balance, in-play balance, transaction history (deposits, payouts, fees, withdrawals), deposit again (same Deposit screen). Funds protection message visible here too (EJ2 secondary). Single screen at this depth.

Withdrawal flow (not a separate screen - a flow inside Wallet): enter amount, enter destination USDC address (MVP) or PIX (Phase 2 Brazil), confirm, states: pending/confirmed/failed. Withdrawal is always in crypto (USDC) for MVP - no fiat payout rail at launch.

---

### PROFILE - public reputation

The "I called it" identity surface. Accessible to others, not just the account owner.

```
My Profile                                   (SJ1 · SJ2)    ⭐ PRIMARY + 🥈 SECONDARY
Public Profile (another user)                (SJ2)          🥈 SECONDARY > ⭐ PRIMARY
```

**My Profile** - prediction track record: total bets, win rate, history of resolved bets (public). Share card gallery (past wins). Editable display name and avatar.

**Public Profile** - same data, read-only, for another user. Dan uses this more (reputation-first behavior). Alex arrives here via a shared win card or leaderboard - secondary path for him.

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

*Next: navigation structure and depth (step 3) - pending tracing review.*

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

**No confirmed orphans.** Matrix is closed: all 14 screens have a job (Onboarding removed), all 11 jobs have a screen. BH x SJ2 corrected - Bet History now carries EJ1 only (1 job, lowest coverage, merge candidate in navigation pass).

One systemic gap was found and closed during tracing: FJ1 / FJ5 / EJ3 depended on the Notification entity with no screen of its own. Notifications (NT) added to sitemap and matrix - gap resolved.

**Remaining decisions for navigation design pass:**

| Action | What to do |
|---|---|
| **Merge or keep** | Bet History + Active Bets - verify a tab in one screen covers EJ1 only (SJ2 removed from BH) |
| **Backlog** | Settings / Notification Preferences - remains `[SIROTA]` until a job is confirmed |
