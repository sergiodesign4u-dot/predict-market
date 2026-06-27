# Wireframes - Screen Order (Step 01)

**Purpose:** This file is the screen order for the Wireframes phase, main flow
only, primary persona Alex (News Junkie). It is pure synthesis from
`IA/sitemap.md`, `IA/flows.md`, and `research/jtbd.md`. It builds no HTML. Its
single output is the ordered 6-screen spine plus the screen x state map that
Step 02 and later wireframe steps build from. Nothing here is invented:
every screen, job, flow position, and state traces to one of those three files.

---

## Main flow definition

**Primary persona:** Alex (News Junkie), PRIMARY per `research/jtbd.md` (MJ
persona line).

**Main job (MJ):** "When an event I follow is approaching resolution, I want a
real stake on the outcome, so that it is not just news but my own
participation with real consequences." (`research/jtbd.md`, MJ.)

**Main-flow spine, in order (News Junkie branch only, from the MJ flow in
`IA/flows.md`):**

1. Event Feed
2. Event Detail
3. Bet Screen (intent -> S5 reconcile -> execute, one screen)
4. Sign In / Register
5. Deposit
6. Active Bets (MJ success terminal, T14)

This is the News Junkie branch of the MJ flow: gate fires at Confirm on the
Bet Screen, then Sign In / Register, then Deposit, then the S5 price reconcile,
then execute, landing on Active Bets (T14). The Crypto Native branch and all
non-main-flow screens are deferred (see the Deferred to Step 08 section).

---

## Per-screen blocks

### 1. Event Feed

- **Name (sitemap):** Event Feed
- **Jobs it closes:** FJ1 (sitemap group label) plus FJ2, MJ, EJ2 (tracing
  matrix row checks for EF).
  - FJ1: "When something important happens in the world and I have an opinion
    on the outcome, I want to quickly find that event among active bets, so I
    do not miss the moment while the topic is current."
  - FJ2 (partial, story-driven card): "When I see an event and its
    probability, I want to understand why the market prices it that way."
  - MJ: entry point of the main job.
  - EJ2: "When a platform asks me to trust it with money for the first time, I
    want to feel it is a serious and transparent organization." First
    impression layer, no registration required.
- **Place in the flow:** MJ entry. In `IA/flows.md` MJ, `triggerFeed --> EF`,
  then `found{"found a relevant event?"}`. Also the entry node of the FJ2 flow.
- **Canonical states:**
  - empty ✓ - T6 in MJ (`found -->|"no"| T6`): no events match the current
    filter or category.
  - error ✓ - network fail, API unreachable (sitemap state list).
  - loading ✓ - initial data fetch (sitemap state list).
  - success ✓ - active market cards (sitemap success view).
- **Product-specific states (sitemap, verbatim):**
  - loading (initial data fetch)
  - empty (no events match current filter or category)
  - error (network fail, API unreachable)
  - push-permission-missing banner (surfaced on Event Feed when OS push is
    denied; cross-referenced from Notifications states)
  - first-visit story-driven layout (context visible on card, not just %) vs
    return-visit denser feed. Naming deferred: P3-4 in `IA/flows.md`
    (first-visit vs return-visit layout naming on Event Feed).
- **Revised card and feed (IA propagation pass, supersedes the story-driven card
  framing above):**
  - Card composition: thumbnail placeholder image, event question (primary
    hook), compact probability % (does not dominate), YES / NO controls as a
    trigger-entry, small meta (volume and closing date), and a bookmark control.
    No category badge, no context snippet. The FJ2 context block now lives on
    Event Detail only.
  - Two layouts, both built: Binary (one question, the % of one side, large
    YES / NO) and Multi-outcome (rows of option plus % plus compact YES / NO).
    Multi-outcome is a normal `Event.Type` layout, not the rejected
    trading-board view.
  - Trigger-entry: tapping YES or NO on a card routes to Event Detail with the
    side, and for multi-outcome the option, pre-selected (`IA/flows.md` MJ). It
    does not place a bet and does not bypass Event Detail; no Feed to Bet edge is
    added. Tapping the card body or question opens Event Detail neutrally.
  - Default sorted view is Trending (not a neutral "All"); recency is the
    alternate. Sort and filter controls sit on the feed heading row ("Live
    events"), not a separate band. Categories stay the four locked ones
    (Politics, Crypto, Culture, General); the mechanism scales to more later
    without rework.
- **Saved view (not a spine screen):** Saved is a view / filter under Events
  (reached from the card bookmark and the desktop Favorites entry), not a new
  spine screen or destination. It is therefore not added to the spine or the
  state table.
- **Auth-state note (no separate logged-out page):** the browse screens (Event
  Feed, Event Detail) render registered by default; logged-out is a
  header-level delta (Sign in replaces Balance plus avatar), body identical and
  browsable in both. No separate logged-out page is added to the spine. The auth
  branch concentrates at the gate, already in the spine (Sign In / Register,
  Deposit).

---

### 2. Event Detail

- **Name (sitemap):** Event Detail
- **Jobs it closes:** FJ2 and MJ (sitemap group label) plus EJ1 (tracing matrix
  row check for ED).
  - FJ2: "When I see an event and its probability, I want to understand why the
    market prices it that way and what could change that number, so I make a
    conscious decision instead of betting blind." Primary differentiator: no
    competitor explains the price at this depth.
  - MJ: the screen where bet intent forms (taps YES or NO).
  - EJ1: "When my prediction turns out right, I want to feel I understand what
    is happening better than most." The sense of edge emerges here (market vs
    own forecast).
- **Place in the flow:** MJ, one node after Event Feed:
  `found -->|"yes"| ED`, then `ctxOk{"context loaded?"}`, then
  `wantsBet -->|"yes - taps YES or NO"| BS1`. Also the core node of FJ2.
- **Canonical states:**
  - empty - : a detail for an existing event always has content (probability,
    chart, narrative, resolution conditions). No empty state.
  - error ✓ - T8 in MJ and FJ2 (`ctxOk -->|"no"| T8`, `T8 -->|"retry"| ED`):
    load failure, retry returns to Event Detail.
  - loading ✓ - event data fetching (sitemap state list).
  - success ✓ - full event view with YES / NO CTA (sitemap).
- **Product-specific states (sitemap, verbatim):**
  - loading (event data fetching)
  - error (load failure, T8 in MJ and FJ2 flows, retry returns to Event Detail)
  - resolved-while-reading (this event just resolved: navigate to Win/Loss
    Screen if the user holds a position, else to Event Feed)

---

### 3. Bet Screen

- **Name (sitemap):** Bet Screen
- **Jobs it closes:** MJ and FJ3 (sitemap group label and tracing matrix).
  - MJ: the bet itself, the real stake with real consequences (intent ->
    reconcile -> execute, one screen).
  - FJ3: "When I have decided to bet, I want to do it with ordinary money
    without learning unfamiliar technology, so the entry barrier is about the
    event, not the infrastructure around it." Served by $5 default pre-fill,
    quick-select, fee and payout shown inline.
- **Place in the flow:** MJ, two stages. `BS1 ["Bet Screen (intent)"]` after
  the YES/NO tap, then the gate (`confirmedIntent -->|"yes - gate fires"|`),
  then post-gate the S5 reconcile, then `BS2 ["Bet Screen (execute)"]`, then
  `techOk{"bet registered on-chain?"}`. Success leads to Active Bets.
- **Canonical states:**
  - empty - : the screen always has a direction (pre-set from the YES/NO tap)
    and an amount input pre-filled at $5. Never empty.
  - error ✓ - T3 in MJ (`techOk -->|"no"| T3`, `T3 -->|"retry"| BS2`): bet
    registration failed on-chain. Also the inline insufficient-balance error.
  - loading - : intent is instant and pre-filled. The on-chain execute moment
    is captured under product-specific states (execute on-chain processing),
    not as the generic canonical loading state.
  - success ✓ - bet registered, leads to Active Bets (T14).
- **Product-specific states (sitemap, verbatim):**
  - intent (logged out, user builds the bet, no auth yet)
  - S5-reconcile (price moved during gate: shows old price vs new price, user
    must re-confirm; rejection routes to T16 in `IA/flows.md`)
  - error (bet registration failed on-chain, T3)
  - insufficient-balance (inline: "you have $X, can bet up to $X or deposit
    more" with options to change amount or go to Deposit)
  - event-closed (this event just resolved while on screen: navigate to
    Win/Loss Screen if the user holds a position, else to Event Feed)
  - execute on-chain processing (the transitional execute moment, BS2 ->
    success or T3)

---

### 4. Sign In / Register

- **Name (sitemap):** Sign In / Register
- **Jobs it closes:** FJ3 (sitemap group label and tracing matrix).
  - FJ3: "When I have decided to bet, I want to do it with ordinary money
    without learning unfamiliar technology." News Junkie path: social login
    (Google, X), no crypto wallet required.
- **Place in the flow:** MJ, the News Junkie branch of the gate:
  `personaType -->|"News Junkie"| SI`, then `authOk{"auth successful?"}`,
  `authOk -->|"yes"| DEP`. The Crypto Native branch (`walletOk`) is out of
  scope for this step.
- **Canonical states:**
  - empty - : a sign-in screen with provider buttons always has content.
  - error ✓ - T5 in MJ (`authOk -->|"no"| T5`): social auth failed. Note: T15
    (wallet connect failed) belongs to the Crypto Native branch, out of scope
    here.
  - loading ✓ - OAuth redirect pending (in-progress, sitemap state list).
  - success ✓ - authenticated, leads to Deposit (sitemap).
- **Product-specific states (sitemap, verbatim):**
  - in-progress (OAuth redirect pending, wallet connect prompt open)
  - error (auth failed, T5; wallet connect failed, T15 - Crypto Native, out of
    scope for this step)
  - error-provider-conflict (account exists under a different provider, e.g.
    registered via X, trying Google: prompt to use the original provider or
    link accounts)

---

### 5. Deposit

- **Name (sitemap):** Deposit
- **Jobs it closes:** FJ3, FJ4, EJ2 (sitemap group label and tracing matrix).
  - FJ3: "I want to do it with ordinary money without learning unfamiliar
    technology." Fiat card to USDC via Transak.
  - FJ4: "When I face an unfamiliar platform and I am about to put real money
    into it, I want a clear answer to 'what happens to it', so my risk is about
    the event, not the platform itself." Inline risk block: USDC held 1:1.
  - EJ2: "When a platform asks me to trust it with money for the first time, I
    want to feel it is a serious and transparent organization." Funds
    protection message shown before submit.
- **Place in the flow:** MJ, after Sign In / Register on the News Junkie path:
  `authOk -->|"yes"| DEP`, then `depOk{"deposit successful?"}`,
  `depOk -->|"yes"| S5`. From Deposit, `moreInfo -->|"yes"| HIW` then back to
  Deposit (How It Works is a detour, out of scope as a built screen this step).
- **Canonical states:**
  - empty - : the deposit form (amount input, provider widget) always has
    content.
  - error ✓ - T2 in MJ (`depOk -->|"card declined"| T2`), T1
    (`depOk -->|"KYC rejected"| T1`), and widget-load-failure.
  - loading ✓ - Transak widget loading / KYC pending inside the widget.
  - success ✓ - deposit confirmed, leads to S5 reconcile / execute.
- **Product-specific states (sitemap, verbatim):**
  - in-progress (Transak widget loading, KYC pending inside widget)
  - error-card (card declined, T2)
  - error-KYC (KYC rejected, T1)
  - widget-load-failure (Transak iframe blocked or network error: fallback to
    "open Transak directly" or "connect a USDC wallet", S3 fix)
  - pending (payment under review, usually under 5 min)
  - minimum-not-met (inline error before submit, shown against the amount
    input)

---

### 6. Active Bets

- **Name (sitemap):** Active Bets
- **Jobs it closes:** EJ1 - position monitoring (sitemap group label) plus MJ,
  FJ5, EJ3 (tracing matrix row checks for AB).
  - EJ1: "When my prediction turns out right, I want to feel I understand what
    is happening better than most." Tracking the position move my way.
  - MJ: success terminal. The just-placed bet appears here (T14).
  - FJ5 / EJ3: the resolved-bet entry point (route to Loss Screen), the
    non-main-flow part deferred to Step 08.
- **Place in the flow:** MJ success terminal. `techOk -->|"yes"| AB`, then
  `AB --> mjDone(["T14 - MJ closed: bet placed, user follows the event"])`.
- **Canonical states:**
  - empty ✓ - empty-new (real screen state for a new user with no bets, not on
    the MJ-success path) and empty-resolved (all positions closed).
  - error ✓ - failed to load positions (retry CTA, sitemap state list).
  - loading ✓ - fetching positions (sitemap state list).
  - success ✓ - open positions list; the just-placed bet appears (MJ terminal
    T14).
- **Product-specific states (sitemap, verbatim):**
  - loading (fetching positions)
  - empty-new (new user, no bets placed yet: CTA to Event Feed to find events)
  - empty-resolved (all positions closed: CTA to History tab to see resolved
    bets)
  - error (failed to load positions, retry CTA)

---

## Screen x state table

Legend: ✓ = state genuinely occurs for this screen. - = the scenario does not
produce this state.

| Screen | empty | error | loading | success | product-specific states (from sitemap) |
|---|:--:|:--:|:--:|:--:|---|
| Event Feed | ✓ | ✓ | ✓ | ✓ | push-permission-missing banner; first-visit (story-driven) vs return (denser) layout [P3-4 naming deferred] |
| Event Detail | - | ✓ | ✓ | ✓ | resolved-while-reading (event resolves while open: route to Win/Loss if position held, else Event Feed) |
| Bet Screen | - | ✓ | - | ✓ | intent (logged out) · S5-reconcile (price moved, old vs new, re-confirm; T16 if rejected) · insufficient-balance (inline) · event-closed (resolved while on screen) · execute on-chain processing (transitional to success or T3) |
| Sign In / Register | - | ✓ | ✓ | ✓ | provider-conflict (account exists under a different provider) |
| Deposit | - | ✓ | ✓ | ✓ | pending (payment under review) · minimum-not-met (inline before submit) |
| Active Bets | ✓ | ✓ | ✓ | ✓ | empty-new (no bets yet) vs empty-resolved (all positions closed) |

---

## Deferred to Step 08

These are explicitly out of scope for this step so nothing below reads as a gap
in the main-flow spine. They are real and will be built later; they are simply
not part of the News Junkie main-flow synthesis here.

- **Crypto Native branch of the gate** (wallet connect, terminal T15 in
  `IA/flows.md` MJ): secondary persona Dan (Crypto Native), not the main path.
  The `personaType -->|"Crypto Native"| walletOk` branch and its T15 terminal
  are deferred.
- **Non-main-flow screens** (from `IA/sitemap.md`, none on the MJ News Junkie
  spine):
  - Win Screen
  - Loss Screen
  - Notifications
  - Wallet
  - My Profile
  - Public Profile
  - How It Works
  - Bet History tab (History tab inside My Bets)

---

## Verification notes

What was checked, and against which source file:

- **Screen names matched to `IA/sitemap.md`:** all 6 spine names (Event Feed,
  Event Detail, Bet Screen, Sign In / Register, Deposit, Active Bets) are taken
  verbatim from the Screens section of the sitemap. No renaming or rephrasing.
- **Jobs matched to `research/jtbd.md`:** each job code (MJ, FJ1, FJ2, FJ3,
  FJ4, FJ5, EJ1, EJ2, EJ3) maps to a job defined in jtbd.md. The one-line
  formulations are English renderings of the jtbd.md formulations (the source
  states them in Russian; the MJ English line is the one fixed in the Step 01
  brief). Job-to-screen assignments cross-checked against the sitemap Tracing
  Coverage Matrix (rows MJ, FJ1-FJ5, EJ1-EJ3 vs columns EF, ED, SI, DEP, BS,
  AB).
- **Flow positions and terminal codes matched to `IA/flows.md`:** the spine
  order and each node citation (triggerFeed, EF, found, ED, ctxOk, wantsBet,
  BS1, confirmedIntent, gate, SI, authOk, DEP, depOk, S5, BS2, techOk, AB) and
  terminals (T6, T8, T3, T5, T2, T1, T16, T14) are taken from the MJ flow.
  Out-of-scope terminal T15 is named only to mark the Crypto Native boundary.
- **State cells matched to `IA/sitemap.md` state lists:** every product-specific
  state listed per screen is copied verbatim from that screen's States line in
  the sitemap. Canonical empty/error/loading/success marks were verified against
  both the sitemap state lists and the flow terminal codes (empty = T6 for
  Event Feed; error = T8/T3/T5/T2-T1; success terminals at T14).

**Contradictions found:** none. Every cell in the screen x state table agrees
with the sitemap state lists and the flow terminals. Two cells worth noting,
both consistent (not contradictions):

- Event Detail empty = - : the sitemap lists no empty state for Event Detail
  (loading, error, resolved-while-reading only). An existing event always has
  content, so empty does not occur. Consistent with source.
- Bet Screen loading = - : the sitemap does not list a generic loading state
  for the Bet Screen. Intent is instant and pre-filled; the on-chain execute
  moment is carried as a product-specific state (execute on-chain processing),
  not as canonical loading. Consistent with source.
