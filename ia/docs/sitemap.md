# Sitemap - Prediction Market Platform

> Status: wireframe build complete (2026-06-28). Navigation design complete; the
> wireframe build pass (below) revises several structural decisions. Every screen in
> the S6 screen tree is built (orphans [ORPHAN] excepted, by design).
> Built from: personas.md · jtbd.md · research.md

---

## Wireframe build pass - structural revisions (current, authoritative)

> The wireframes (`wireframes/*.html`, rulebook `wireframes/_conventions.md`) are
> the live build. The decisions here revise earlier sitemap structure. Where this
> section and an older passage disagree, **this section is authoritative**; the
> older text is kept for history, annotated where practical.

1. **Category pages are real screens (second-level nav -> own page).** Tapping a
   category (Politics, Crypto, Culture, General) opens its own page, not an
   in-feed filter toggle. Each category page = a sub-category side rail (left
   sticky rail on desktop, horizontal scrolling chips on mobile) + Sort / Frequency
   on the heading + the category-scoped card grid. Trending stays the main Event
   Feed (`event-feed.html`). Each category page is a browse screen with the auth
   axis and success / empty / error / loading states (logged-in and logged-out).
   Built: `politics*`, `crypto*`, `culture*`, `general*`.

2. **Sub-category is a NEW Event attribute.** Within a category, events carry a
   sub-category (Politics: Trump, Midterm Elections, Primaries, Congress, Courts,
   Epstein, Government Shutdown, ...; Crypto: Bitcoin, Ethereum, Solana, ETFs,
   Stablecoins, Memecoins, ...; etc.). The category page's left rail filters by
   sub-category, each with a count. Taxonomy and counts are illustrative sample
   data at wireframe stage (Polymarket / Kalshi-modelled), pending a real taxonomy.

3. **Betting is an inline panel on Event Detail, not a standalone Bet Screen.**
   The bet intent and all bet states live in a sticky bet panel on Event Detail
   (right rail on desktop; a bottom dock that expands to a sheet on mobile). The
   standalone "Bet Screen" is dissolved: its states become Event Detail panel
   states - intent, insufficient-balance (inline guard -> Deposit), S5-reconcile,
   execute processing, on-chain error (T3); event-closed is the Event Detail
   resolved state. Event Detail now has two success views: **binary** (one YES / NO)
   and **multi-outcome** (pick an outcome, then YES / NO on it). Confirm fires the
   gate.

4. **Sign In / Register and Deposit are shared in-page dialogs.** Native
   `<dialog>`, opened over the current page; Close / backdrop / Esc keep the user on
   that page. One dialog markup is defined once and emitted on every page; the
   providers chain Sign In -> Deposit. The standalone `sign-in-*.html` /
   `deposit-*.html` pages are kept as the per-state design reference. This refines
   D-desktop-5: the bet is no longer a separate invoked overlay; only Sign In and
   Deposit remain overlays, now as dialogs.

5. **Consequences for older sections** (revised by the above): "Under Question ->
   Category" (Category is now a screen with its own page, not only an Event field);
   "BET - Bet Screen" (dissolved into the Event Detail panel); D-desktop-5 (bet
   inline; gate = dialogs over the page); "Not navigation destinations" (Bet Screen
   removed as a screen); the Tracing **BS** column now represents the Event Detail
   bet panel (MJ / FJ3 coverage unchanged).

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
| Category | Politics · Crypto · Culture · General. Each category is now a screen with its own page (see Wireframe build pass #1), not only a filter on the feed. |
| Sub-category | NEW (wireframe build pass). A finer tag within a category (e.g. Politics: Trump, Midterm Elections, Primaries, Congress, Courts, Epstein, Government Shutdown). Powers the sub-category rail on the category page. Taxonomy is illustrative sample data at wireframe stage. |
| Frequency / recurrence | One-time or recurring. Recurring cadence: Hourly · Daily · Weekly · Monthly. NEW (wireframe pass): introduces recurring markets, and powers the Frequency filter on the Event Feed. **DECIDED 2026-08-10** (`docs/backlog.md` #11): every cadence instance is its OWN Event, with its own window, its own price and its own resolution, and the cadence is a SERIES the instances belong to. The Frequency filter filters by the series attribute. No new entity: Active Bets, notifications and the resolution record keep working on the Event they already work on. |
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
| Saved / followed events | Bookmarks: events the user chose to follow. Powers the Favorites view under Events. NEW relationship, added in the Event Feed revision pass. |
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
| **Category** | Events are grouped by Politics / Crypto / Culture / General | RESOLVED in the wireframe build pass (#1): Category is promoted to a navigation screen - each category opens its own page with a sub-category rail, sort/frequency, and the auth axis + states. It is both an Event field and a browse screen. Sub-category was added as a new Event attribute. |
| **Leaderboard** | Listed in CLAUDE.md MVP features | No explicit job in jtbd.md. SJ2 (public track record) is served by Profile. Leaderboard is a view over Profiles - a feature, not a distinct entity. Revisit if social competition mechanics are confirmed. |
| **Odds Chart** | Every competitor has it; part of Event detail | Attribute of Event (probability history), not a standalone entity. Lives inside Event. |
| **Fiat Transaction** | Deposit/withdrawal via Transak/MoonPay | Currently modeled as sub-object of Wallet. Promote to standalone entity only if on-ramp flow reveals complexity that can't fit inside Wallet (e.g., multi-step KYC state machine per transaction). |

---

## Concept sitemap (by intent)

Screens grouped by what Alex is trying to do (not by site section). Each screen carries its job tag; a screen with no job is `[ORPHAN]`. States (empty / error / loading) live in the flows, not here; page contents live in the detailed layer. This is the concept view rendered in `ia/concept-map.html`. Clusters A to D mirror the CJM To-Be journey (Find -> Stake -> Follow / settle -> Share).

- **A. Find an event worth a stake:** Event Feed (FJ1), Category pages (FJ1), Favorites (FJ1), Event Detail (FJ2 / MJ)
- **B. Put real skin in the game:** Event Detail bet panel (MJ), Sign In / Register (MJ gate), Deposit (FJ4), Wallet (FJ4), Confirm / processing (MJ)
- **C. Follow and settle my stake:** Active Bets, Active + History (EJ1), Win Screen (MJ), Loss Screen (FJ5 + EJ3), Notifications (EJ1)
- **D. Prove I was right, share:** Win Screen share (SJ1), Public Profile (SJ2), Share Card (SJ1)
- **E. Understand and trust the platform:** How It Works (EJ2), My Profile / account hub (EJ2)
- **`[ORPHAN]`** (no job): Settings, Leaderboard, Help / FAQ

The section-grouped screen inventory below stays as the fuller reference; this intent view is the concept map the flows and the detailed layer build on.

## Screens

> Notation:
> Job in `(parentheses)` = job from jtbd.md this screen closes. No job = `[ORPHAN]`.
> ⭐ PRIMARY = Alex (News Junkie). 🥈 SECONDARY = Dan (Crypto Native).
> Screens without persona mark serve both.
> States (empty, error, loading) are NOT screens - they are states of the screens below.

---

### EVENTS - what to bet on

The user arrives because something happened in the world (FJ1).
This group is the entry point for both personas.

```
Event Feed                                   (FJ1)          ⭐ PRIMARY + 🥈 SECONDARY
Category page (Politics/Crypto/Culture/General) (FJ1)       ⭐ PRIMARY + 🥈 SECONDARY   NEW (wireframe build pass)
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

**Featured slot (DECIDED 2026-08-13, `docs/backlog.md` 77).** The Trending feed opens with one featured event above the grid. **Trending only** - not the four category pages, not Favorites, not any logged-out variant of them. **What fills it is the highest 24-hour volume among open markets**, a figure the product already holds, so MVP needs no editorial queue and no admin screen, and the slot can never show a resolved event. It is the event card with room, a 30-day chart and the photograph; **nothing is reachable only there**, so it adds no node to this map and no state to the feed: when there is nothing to feature the slot is absent, which is the feed's own empty state. It had stood in both trees since 2026-07-23 and in no document, which is the whole reason it is written here rather than left to the markup. Block-level structure is `wireframes/_conventions.md` S7.

Controls placement (revised in the wireframe pass): categories are second-level navigation in a sub-nav band directly under the header (Trending default, then Politics, Crypto, Culture, General). The feed heading echoes the active category (for example "Trending"), not a generic "Live events" label, and updates when another category is chosen. The heading row carries a Kalshi-style filter cluster (feed controls, not navigation), each a dropdown whose label shows the current value:
- **Sort:** Trending, Volatile, New, Closing soon, Volume, 50-50, plus a Reverse sort toggle.
- **How often:** Any, One-time, Hourly, Daily, Weekly, Monthly (filters by the Event **Frequency** attribute, recurring markets). **The control was labelled `Frequency:` with a default of `All` until 2026-08-14**, when voice principle 3 was applied to it: we use the words a news-follower already owns, and `frequency` is the vocabulary of whoever built the market. **The entity keeps its name and the reader gets theirs**, which is the same split this map already makes between a screen and the field behind it.
- **Category:** the full category list. This is redundant-by-design with the second-level chip nav: the chips are quick access to the main categories, the dropdown is the full list that scales as categories grow. The dropdown, the chips, and the heading stay in sync (selecting in one updates the others).

Exact sort and filter labels are a wireframe detail. Categories stay the locked four for MVP; the category mechanism is built to scale to more categories later without rework. Do not add empty categories now.

Favorites view: a filter / view over the Event Feed showing only saved events. It is a view within Events, the same way categories filter the feed, not a separate screen. Reached from the bookmark control on cards, from the Favorites (heart) entry in the desktop header, and from the Favorites bottom-nav slot on mobile (the wireframe pass moved Favorites into the mobile bottom bar, swapping with Notifications). See Saved events for the relationship and the alert hypothesis.

**Category page** (NEW, wireframe build pass) - a category opened as its own page: Politics, Crypto, Culture, General. Same card pattern as the Event Feed, scoped to one category, with a sub-category side rail (left sticky rail on desktop, horizontal scrolling chips on mobile) listing the category's sub-categories with per-sub-category counts, plus Sort and Frequency on the heading row. The second-level category nav routes here (links, not in-feed toggles); Trending stays the main Event Feed. Browse screen with the auth axis.
States: success (grid) - empty (no events match the sub-category / filters: Clear filters + "Notify me of new <category> events", T6 subscribe edge) - error (failed to load: Try again + Back to Trending) - loading (skeleton grid). Built as the full auth x state matrix (logged-in and logged-out).

**Event Detail** - one event, full view: probability, schematic price chart, narrative context (why this price), resolution conditions, source. This screen is our primary differentiator - no competitor has context at this depth (FJ2 confirmed gap). With the card snippet removed, this context block is the sole home of the FJ2 differentiator. **Betting happens here** in a sticky bet panel (right rail on desktop; a bottom dock that expands to a sheet on mobile), so an informed user can stake while scrolling the context. Two success views: **binary** (one YES / NO) and **multi-outcome** (the outcomes are listed in the main column and the panel becomes "pick an outcome", then YES / NO on it). Content order: header -> chart + facts -> why this price -> resolution; the panel leads. Confirm in the panel fires the activation gate (Sign In then Deposit, as dialogs over the page). This replaces the standalone Bet Screen (see Wireframe build pass #3).
States (page-level): loading (event data fetching) - error (load failure, T8 in MJ and FJ2 flows - retry returns to Event Detail) - resolved-while-reading / event-closed (this event just resolved: navigate to Win/Loss Screen if user holds a position, else to Event Feed) - pre-selected entry variant (arrived from a card YES/NO tap with a side and, for multi-outcome, an option pre-selected).
Bet-panel states (migrated from the old Bet Screen): intent (default) - insufficient-balance (inline guard: bet up to balance or open the Deposit dialog) - S5-reconcile (price moved during the gate: old vs new, re-confirm or cancel, T16) - execute processing (registering on-chain) - on-chain error (T3, retry). The Event Detail state-switcher is built as three axes: Auth, View (binary / multi / error / loading / resolved), Bet panel (intent / insufficient / reconcile / processing / on-chain error).

#### Saved events (NEW addition)

This is a new addition to the IA, stated plainly as new, not a pre-existing job.

- **Relationship:** User saves / follows Event (a bookmark). Added to the User entity (Saved / followed events) and the Event entity (Related to: User).
- **Favorites view:** a filter / view over the Event Feed showing only saved events. NOT a new bottom-nav slot and NOT a new top-level destination; a view within Events, like a category filter. In the wireframes this view is realized as `favorites.html` (reusing the feed chrome, with empty / loading states) so the Favorites control has a concrete destination - it is still the feed filtered to saved events, not separate chrome.
- **Affordances:** a bookmark control on each event card; a Favorites (heart) entry in the desktop header utility cluster; and a Favorites bottom-nav slot on mobile (wireframe pass), all opening the Favorites view (see Desktop layer D-desktop-4 and the bottom-nav table). **A Favorites row in the avatar dropdown as well, from 2026-08-13**, which is the keyboard's route and exists on both breakpoints: the heart is desktop-only and the bottom bar sits after the footer in the document, so on a phone Favorites had no reach earlier than tab stop 96 on the feed, against 9 and 10 for its two peers in that same dropdown. It is stop 11 now. `docs/backlog.md` 130.
- **Alert on a saved event moving significantly: [hypothesis].** Not a confirmed job, not wired as a confirmed Notification type. The confirmed Notification types stay as they are (entity 8). A proactive "your saved event moved" alert is flagged for later validation only.
- **Rationale:** saving improves convenience and retention; every benchmarked competitor exposes a bookmark on the card. The confirmed job backing is partial (retention, FJ1 return), so the save relationship is added now, but the proactive saved-event alert stays a hypothesis until validated.

#### Auth-state axis

Logged-out versus logged-in is a TOP-LEVEL axis of the page states on the browse screens (Event Feed, Event Detail), sitting above the screen states. Each browse screen is built as a logged-in and a logged-out variant, and under each, its screen states (success / empty / error / loading / ...). Revised in the wireframe pass: this is a real page variant, not a header-only delta tacked onto one page, because the logged-out header is materially different (no account).

- **Logged-in header:** balance (Portfolio / Cash swap), Favorites, Notifications (with unread badge), avatar dropdown. The dropdown carries My Profile, My Bets, **Favorites**, Wallet, How It Works and Logout: six rows since 2026-08-13, and Favorites sits beside My Bets because those two plus My Profile are the three top-level destinations the dropdown holds.
- **Logged-out header:** the balance figure and the avatar dropdown are removed and replaced by Log in + Sign up entries. Favorites (heart) and Notifications (bell) are kept as affordances, but tapping either while logged out routes to Sign In (saving and alerts need an account), and the bell shows no unread badge. On mobile the Portfolio bottom-nav slot becomes a Sign in entry.
- **Identical in both:** the logo (Events home), the second-level category nav, the feed body, and all cards are identical and browsable; only the header (and the mobile slot 4) differ. `push-permission-missing` is logged-in only (account-bound), so it has no logged-out counterpart.
- **The real auth branch still concentrates at the activation gate** (Bet Screen Confirm -> Sign In / Register -> Deposit), which exists as its own screens and states. Edge cases (logged-out at confirm; registered with no balance -> Deposit) live there, per Variant B, already locked.
- **Why the change:** the earlier "header-level delta, no separate logged-out page" rule under-modeled how different the logged-out header is (no profile, no balance, login entries). Treating auth as the top page axis is the honest structure; the body is still shared, so only the header markup duplicates.

---

### ACTIVATION GATE - bet-first, gate at confirm (Variant B)

> REVISED (wireframe build pass #4): Sign In / Register and Deposit are shared
> in-page **dialogs** (native `<dialog>`) opened over the current page; closing
> keeps the user on that page, and the providers chain Sign In -> Deposit. The
> standalone `sign-in-*.html` / `deposit-*.html` pages remain as the per-state
> design reference.

The user browses and builds a bet logged out. The gate fires only when they tap "Confirm" in the Event Detail bet panel - not at YES/NO tap.
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

> REVISED (wireframe build pass #3): the standalone **Bet Screen is dissolved**.
> Betting is an inline sticky panel on Event Detail (right rail desktop / bottom
> dock mobile), and its states are Event Detail bet-panel states (see the Event
> Detail screen above). The text below is kept for history; "Bet Screen" now means
> "the Event Detail bet panel". The flow is unchanged in substance: build the bet
> in the panel, Confirm fires the activation gate (Sign In then Deposit dialogs).

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

**Win Screen** - "You were right." Amount won, resolution summary (what happened and why), Share Card auto-generated. CTA: Share · See next events. Design rationale: no confetti loop, no persistent celebration animation. Research finding F5 (research.md): first WIN is the trigger for overconfidence and escalation, not loss. The win screen must celebrate the outcome without feeding the loop. Celebratory but measured - one moment, then move on.
Per F5, the first win is the stronger escalation trigger (overconfidence). Share / mark the moment is the default next action; "see next events" is a deliberate secondary CTA, not the primary. Symmetric with the Loss intervention, shaped for overconfidence rather than impulse. Modeled in ia/docs/flows.md SJ1: share path is the primary edge, secondary "see next events" edge is labeled with the overconfidence risk.
States: loading (Share Card generation in progress) - error (Share Card not generated, SJ1 blocked - T11 in flows) - payout-pending (your payout will arrive in a few minutes, on-chain settlement delay).

**Loss Screen** - "Here's what happened." Plain-language resolution note (what resolved and why), amount lost, one clear next step (not "bet again" promo). This screen is undesigned by every competitor - it is our primary retention intervention against loss-chasing (FJ5 + EJ3 confirmed gap).
Design rationale: the resolution note is the default beat before any re-bet (intervention against loss-chasing, per product strategy O1 trust over O4 volume). Friction is calm, non-punitive, and non-blocking - the user can always proceed. The escalation branch in ia/docs/flows.md FJ5 routes through an explicit pause node before reaching Bet Screen. Reserved: session-aware chasing check (C-logic), post-MVP, not built in this pass.
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

Note: Settings / Notification Preferences remains `[ORPHAN]` - configuring which notifications you receive is not a confirmed job. The list screen (above) is sufficient for MVP. [?] Q-notif-prefs open question: does the user need per-event mute controls, or is category-level preference sufficient? Cannot be derived from current research - defer to user testing.

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

**How It Works** - funds protection (one sentence: "Your USDC is held 1:1"), resolution process (who decides, what evidence, on-chain proof), resolved markets count as social proof (benchmark.md Top 3 mechanisms). Not a FAQ - a trust declaration, written as a promise.

---

### ORPHANS `[ORPHAN]` - no confirmed job maps here

Screens referenced in product docs but not derived from any jtbd.md job.
Do not build until a job is confirmed.

```
Settings / Notification Preferences         [ORPHAN]        - notification prefs are adjacent to FJ1 return path but no job in jtbd.md requires a settings screen
Leaderboard                                 [ORPHAN]        - no confirmed job; SJ2 is served by Profile; leaderboard is a view, not a job-closing screen
Help / FAQ                                  [ORPHAN]        - EJ2 is served by Deposit + How It Works; a generic FAQ adds friction without closing a job
```

### SYSTEM AND GLOBAL - out-of-cluster nodes (Detailed layer)

Global system nodes and the footer / legal destinations, specified in the IA Detailed layer
(`ia/docs/pages/system.md`, rendered `ia/system.html`). Registered here so the footer and the
cookie banner never promise a destination the map omits. The SEO structural layer for the
indexed pages lives in `ia/docs/pages/seo.md` (rendered `ia/seo.html`).

```
404 Not Found            page       HTTP 404, noindex,follow    full page, never a dead-end (quick links + home)
500 Server Error         page       HTTP 500, noindex           static template, funds reassurance + retry
503 Maintenance          page       HTTP 503 + Retry-After       planned downtime, bets and funds safe
Cookie consent           component  banner, prior opt-in         reject as easy as accept, no pre-ticked, reopen from footer
Toast / notification     component  aria-live, transient         action result, auto-dismiss + manual close
```

Footer and legal destinations, promised by the footer node (`seo.md`); the destination is
registered here so map and footer stay in sync. **AND ON 2026-08-10 THE FOOTER STOPPED PROMISING
WHAT THIS LIST OMITS** (`docs/backlog.md` 27): eight labels stood in the footer of every screen and
on this map nowhere - `Sports`, `Trending topics`, `API / Developers`, `Status`, `Careers`, `Press`,
`Brand`, `Geo restrictions` - and they were cut rather than registered. `Sports` is the sharpest of
the eight and the reason the decision went that way: the four categories are locked for MVP and
Sports is post-MVP, so a fifth in the footer contradicted the category decision and not only the
map. Three of the four `Company` links were in the eight, so that column is gone and `About` sits in
`Support`. **`Geo restrictions` is the one to re-read when compliance is written**: the requirement
is real and stays in `PRODUCT.md`, and if it needs a page, it gets a node here first and a footer
label second, in that order. **What each is MADE of is no longer an open
question:** `ia/docs/blocks.md` banks them as Type 1, the static content page, with two body
profiles - DOCUMENT for the four legal pages and STATEMENT for About - and `ia/docs/pages/seo.md`
section 6 carries their A-E. The bank is by TYPE, so one pass covered five nodes.

```
Terms of Service         page       index,follow                legal; BUILT 2026-08-03, ui-visual/terms.html
Privacy Policy           page       index,follow                legal; linked from the cookie banner
Cookie Policy            page       index,follow                legal; linked from the cookie banner
Responsible betting      page       index,follow                trust and legal
About                    page       index,follow                company
Contact / Support        page       [?]                         support entry; NOT type 1 (it carries a form); Help / FAQ stays [ORPHAN]
```

**Terms of Service is the first screen in this product with no grey twin**, and that is a result
rather than an omission: IA gave the node, the block bank gave the composition, `voice/` gave the
register and `components/` gave every class, so a grey pass would have transcribed decisions
already made. The exception is declared in `_twins.SYSTEM_BUILT` in its own category, apart from
`NOT_A_SCREEN`, so the two facts never share a bucket.

The URL in `seo.md` is `/legal/terms`; the file is `ui-visual/terms.html` because the painted tree
is flat by convention (`STRUCTURE.md`). The slug is the production answer and the filename is the
prototype's.

**Still open for IA, and named here rather than assumed:** which of the six ship at MVP. This block
says "post-MVP where marked" and marks only Contact, which leaves the other five undecided rather
than decided. See `docs/backlog.md` item 27 for the eight footer destinations that are on no map at
all.

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

**Notifications placement (revised in the wireframe pass):** Notifications is now a header bell with a permanent badge on both breakpoints, NOT a bottom-nav slot. The earlier reasoning (the badge must sit in the bottom thumb zone) was reconsidered: the unread badge drives hot/warm return (FJ1, FJ5, EJ3; aarrr.md D1-D3) by being VISIBLE, and a top-right bell with a count is visible too. The thumb slot is more valuable for a destination users actively navigate to, so it was given to Favorites. Notifications and Favorites were swapped: Notifications to the header, Favorites to the bottom bar on mobile.

| Slot | Label | Opens | Jobs served | Why it earns a top-level slot |
|---|---|---|---|---|
| 1 | **Events** | Event Feed | FJ1, FJ2, MJ | The entry point. Users open the app because something happened in the world. Every session starts here. |
| 2 | **My Bets** | Active Bets (two tabs: Active / History) | EJ1, MJ, FJ5, EJ3 | The position monitor. Users return specifically to track odds movement and see resolved bets. History tab implements G5: Bet History becomes a tab inside Active Bets, not a standalone screen. EJ1 coverage is preserved. |
| 3 | **Favorites** | Favorites view (a filter over the Event Feed) | FJ1 (return / watchlist) | Revised in the wireframe pass. The mobile thumb slot for actively filtering to saved events (your watchlist). On desktop, Favorites is a heart icon in the header instead. Notifications, which used to hold this slot, is now a header bell on both breakpoints (its badge stays visible, so its retention role is preserved). Caveat: Favorites is a newer, partially-confirmed feature; revisit this slot if usage data is low. |
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
| **Favorites (heart)** | Header heart icon on desktop; bottom-nav slot on mobile; **a row in the avatar dropdown on both** | Opens the Favorites view. On mobile it earns the thumb slot for active filtering to the watchlist; on desktop it is a header utility. **The dropdown row was added 2026-08-13 and it is not a fourth affordance, it is the keyboard's**: the thumb slot is reached by a thumb, and by a Tab key only after the whole page, because the bottom bar is the last thing in the document. Measured at 390 on the signed-in feed, Favorites stood at stop 96 while My Bets and My Profile stood at 10 and 9 through this dropdown; it is 11 now. The thumb-zone decision below is untouched: nothing moved into the phone header. `docs/backlog.md` 130. |

### Not navigation destinations

These screens are reached only inside a flow, triggered by a user action. They are never a bottom-nav slot and cannot be reached by tapping the nav bar:

- **Bet panel (Event Detail)** - not a screen: the inline sticky panel on Event Detail where the bet is built (replaces the old standalone Bet Screen, wireframe build pass #3).
- **Win Screen** - invoked when a bet resolves with a win (via notification or resolved item in Active Bets).
- **Loss Screen** - invoked when a bet resolves with a loss (G1 direct: 1 tap from resolution notification; or via resolved item in Active Bets).
- **Sign In / Register** - shared in-page dialog, opened at the activation gate (Confirm in the Event Detail bet panel), never before the user has bet intent.
- **Deposit** - shared in-page dialog, opened at the activation gate (News Junkie path, chained after Sign In) and from Wallet (standalone top-up).

### Deferred

| Item | Status | Reason |
|---|---|---|
| **Public Profile** | Deferred to post-MVP (G3) | Reachable only via external shared-card link for MVP. No in-app discovery at 10-20 curated markets: users do not browse others' track records unprompted. In-app path added when leaderboard or social discovery is confirmed. |
| **Search** | Deferred until catalog scale | At 10-20 curated markets, users scan the Event Feed; they do not search. Search does not close a confirmed job at this scale. When added, it attaches to the Events tab under FJ1 - not a bottom slot. |
| **Leaderboard** | [ORPHAN] | No confirmed job. SJ2 is served by My Profile and Public Profile. Leaderboard is a view over profiles, not a job-closing destination. |
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
  - **Favorites** (Favorites view) is a heart icon in the utility cluster.
  - A **hamburger** icon sits at the left, reserved for future scaling; it holds
    no primary items at MVP (Events is the logo, My Bets is in the avatar menu).
- **Second-level navigation:** the categories (Trending default, Politics,
  Crypto, Culture, General) are a second-level sub-nav band directly under the
  header. Categories are navigation (second level); the feed sort control is a
  feed control on the "Live events" heading row, not navigation. See the Event
  Feed screen description.
  **THE CATEGORY BAND IS ON THE SCREENS THAT HAVE ONE, AND NOWHERE ELSE, decided 2026-08-13,
  `docs/backlog.md` 142.** The sticky header repeats the band once the main one has scrolled away,
  and it is revealed by an observer that watches the main band: **on the 48 painted screens with no
  main band it could not open at any width**, so those screens carried five named category links
  that no eye saw and no keyboard reached. The markup is out of those 48 and their 30 grey twins;
  the 57 that have a main band keep it, and it opens on 57 of 57, measured. **The alternative was to
  give the observer another anchor, which would put a category route on the wallet, the deposit,
  the profile and the error screens**, and that is an addition to the navigation model rather than a
  repair: it stays refused until this file asks for it.
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
  control (Favorites). This overturns the earlier "Notifications must be
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
  the Favorites view), **Notifications** (bell icon + permanent badge, see
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
  Leaderboard (it is [ORPHAN]), Rewards, or APIs (not our product).
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

> REVISED (wireframe build pass #3-4): the **bet is no longer an invoked overlay**
> - it is the inline panel on Event Detail. Of the invoked screens, **Sign In /
> Register and Deposit** are now shared in-page `<dialog>` overlays opened over the
> current page (close stays on the page; providers chain Sign In -> Deposit). Win
> and Loss Screens are also invoked overlays, now built (modal on desktop, bottom
> sheet on mobile, over a dimmed Active Bets / notification context; reached 1 tap
> from a resolution notification or a resolved item in My Bets). The rest of this
> section stands as the overlay-presentation rationale for the remaining overlays.

- **Decision:** the invoked screens (Sign In / Register, Deposit, Win Screen,
  Loss Screen) are presented as an overlay in context, not as a separate full-page
  destination, on both breakpoints. Desktop: a centered modal over the page.
  Mobile: a full-height bottom sheet. The user stays in context; they are not
  thrown across separate screens. (The bet itself is the inline Event Detail panel,
  not an overlay.)
- **Multi-step stack:** the activation gate (Sign In then Deposit) and the S5
  reconcile step on Bet Screen run as a multi-step stack inside the same overlay.
- **Mobile-to-desktop mapping:** in-context overlay on both breakpoints -
  centered modal on desktop, full-height bottom sheet on mobile.
- **Consistency with locked IA:** this aligns with the G1 nav decision already
  in ia/docs/sitemap.md and ia/docs/flows.md, where a notification tap "opens target
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
    Favorites view (a filter over the Event Feed)
  Portfolio (mobile slot 4; on desktop via the avatar + the header balance swap)
    My Profile, extended with a portfolio summary (Portfolio / Cash + Deposit) above the track record

Level 1 - one tap below a Level 0 screen
  under Events:
    Category page (tap a category in the second-level nav: Politics/Crypto/Culture/General)
    Event Detail (tap any event card on Event Feed or a category page)
  via the header (available at Level 0):
    Notifications list (header bell, both breakpoints)
    Wallet / Deposit (avatar dropdown, or inside the Portfolio hub)
    How It Works (avatar dropdown and footer, also linked from Deposit)

Flow / invoked - reached only inside a flow, not via nav bar
  Bet panel         inline on Event Detail (not a separate screen; replaces the old Bet Screen)
  Win Screen        invoked: bet resolves as win (notification tap or Active Bets resolved item)
  Loss Screen       invoked: bet resolves as loss (G1: notification tap direct; or Active Bets resolved item)
  Sign In / Register   dialog: activation gate (Confirm in the Event Detail bet panel)
  Deposit           dialog: activation gate (chained after Sign In) or Wallet top-up button
  Public Profile    invoked: external shared-card link only (no in-app nav at MVP)
```

### Depth check - primary persona (Alex, News Junkie)

**MJ main job: Event Feed → Event Detail → bet panel (inline)**
- Events tab (Level 0) → tap event card → Event Detail (1 tap). The bet panel is already on Event Detail, so building the bet is in-place (set side/amount, 0 extra navigation) → Confirm in the panel fires the activation gate (2 taps total, the gate opens as the Sign In dialog over the page).
- Result: bet intent is reachable in 1 tap (Event Detail), the gate fires at 2 taps. Better than the old 3-tap path (the standalone Bet Screen was removed). Within the 3-tap rule. Confirmed.

**G1 retention path: resolution notification → Loss Screen**
- Tap resolution notification (OS banner or Notifications list item) → Loss Screen directly (1 tap).
- Matches the G1 edge in ia/docs/flows.md FJ5: `triggerNotif -->|"G1: direct to Loss Screen"| LS`.
- The manual fallback path (My Bets → tap resolved item → Loss Screen) is 2 taps. G1 cuts this to 1 tap so the resolution note reaches the user before the impulse to chase.
- Result: 1 tap from notification. Confirmed.

**Win Screen retention path: win resolution notification → Win Screen**
- Tap win resolution notification (OS banner or Notifications list item) → Win Screen directly (1 tap).
- Matches the G1-equivalent edge in ia/docs/flows.md SJ1: `triggerNotif -->|"direct: 1 tap to Win Screen"| WS`.
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
EF = Event Feed · ED = Event Detail · SI = Sign In / Register · DEP = Deposit · BS = Bet panel on Event Detail (was the standalone Bet Screen; wireframe build pass #3) · WS = Win Screen · LS = Loss Screen · AB = Active Bets · BH = Bet History · WA = Wallet · MP = My Profile · PP = Public Profile (another user) · HIW = How It Works · NT = Notifications

> Note (wireframe build pass): the **BS** column is now the Event Detail bet panel, not a standalone screen. Its MJ / FJ3 coverage is unchanged. Category pages (new browse screens) inherit EF's FJ1 row and are not added as a separate column, to keep the matrix stable.

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
- Settings / Notification Preferences - remains `[ORPHAN]` until a job is confirmed.
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
