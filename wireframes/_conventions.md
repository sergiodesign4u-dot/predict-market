# Wireframes - Conventions (Step 02)

This is the wireframe rulebook for Yonder. Every screen and every state
page built in Steps 03 to 08 follows these rules. Wireframes are grey-box, low
fidelity, structure only: layout and content order are the deliverable, not
visuals.

---

## The 7 base conventions

### 1. Fidelity: structure only

Show structure, hierarchy, and zones. Grey box. No color, no fonts, no brand,
no images, no finished UI. The layout and the order of content on the page are
what we are designing here. If a decision is about how something looks rather
than where it sits and what it says, it does not belong in a wireframe. The
grey-box layout is now responsive: structure and zones reflow across
breakpoints (see convention 7), while still grey with no color, fonts, icons,
or shadows.

### 2. Markup: semantic HTML

Build with semantic elements: `header`, `nav`, `main`, `section`, `article`,
`form`, `button`, `label`, `ul`/`li`. Not a wall of `div`. Each screen must
read as a real document outline, so the heading and landmark structure alone
tells you what the screen is.

### 3. Text: real domain text, never lorem ipsum

Every label and string is real Yonder content, pulled from
`ia/docs/sitemap.md` where the phrasing already exists. Examples of the exact
phrasings to reuse:

- Event questions in the form "Will X happen before [date]?"
- Categories: Politics, Crypto, Culture, General.
- The price-context narrative (why this price, key arguments for YES and NO):
  our FJ2 differentiator.
- Resolution conditions (what counts as YES, what source is authoritative).
- The fee line: "platform earns $X if you win".
- The funds-protection line: "Your USDC is held 1:1 - we do not lend or invest
  deposited funds."
- The plain-language resolution note on the Loss screen (what resolved and why).

Never lorem ipsum. If a real string exists in the sitemap, use it verbatim.

### 4. File names: base page per screen, one page per state

Pattern only (the actual list is produced in Step 03):

- Base page per screen: `wireframes/<screen>.html`
- One page per state: `wireframes/<screen>-<state>.html`
- Lower kebab-case. The `<state>` suffix matches the state name exactly as
  written in `wireframes/_screens.md` (for example `-empty`, `-error`,
  `-loading`, `-reconcile`, `-insufficient-balance`, `-resolved`, `-pending`).

Do not enumerate the file list here. That is Step 03's job.

**A CATEGORY PAGE IS A STATE OF THE FEED IN ITS NAME, DECIDED 2026-08-15, backlog 156.** The 32
category screens were `politics.html` here and `event-feed-politics.html` in the paint, and the two
trees carried one screen under two names for two stages. **Filename is not one of the six
differences below**, so that was drift by this document's own definition, and it cost every
cross-tree reading a translation table. They are `event-feed-<category>[-state].html` in both trees
now, which is what the naming line further down this file had always asked for.

**The argument for the shorter name was read and refused rather than ignored.** `ia/docs/pages/seo.md`
gives the category its own route, `/c/{category}`, which is a real argument that it is a screen
rather than a state. Against it: the same file gives it the H1 "{Category} events" and a description
that begins "Bet YES or NO on live {category} events", the screen ships the feed's shell, the feed's
cards and the feed's eight states, and **a flat directory makes `politics.html` a name that says
nothing about what the page is**. A route and a filename answer different questions. The rename cost
**5,046 references** and was one sweep; `docs/decisions.md` carries the account and is not rewritten,
because a claim there is true as of its own date.

### 5. States: every state is a separate page

Each state is its own page, never a toggle or a variant inside one file. Same
structure, different content.

- The base page is the success or representative state.
- Each additional real state from `_screens.md` gets its own page: the
  canonical states (`-empty`, `-error`, `-loading`) and the product-specific
  states (such as `-reconcile`, `-insufficient-balance`, `-resolved`,
  `-pending`).
- Every real state listed for a screen in `_screens.md` must become its own
  page when that screen is built. Nothing listed there is dropped or merged.
- For invoked screens (Bet Screen, Sign In / Register, Deposit, Win Screen,
  Loss Screen), the base and state pages render as modal or bottom-sheet
  overlay content, not as a full-page layout. Their states are still separate
  pages, exactly as above.
  > **Enforced since step 7e.** This is the sixth declared boundary in the table
  > at the end of this file, and gate 18 checks it in both directions: 17 grey
  > pages carry no header, bottom nav or footer, and their painted twins carry
  > all three, because a scrim needs something to be a scrim over. What IS
  > compared is the sheet body, where the grey tree had a `<span>` pretending to
  > be the deposit amount field and the paint had a real `<input>`.
  > **Settled in step 8.** The paint had made the overlay a centred modal at
  > BOTH breakpoints, so the "bottom sheet on mobile" half of this line shipped
  > only here. It ships in colour now: under 640px an invoked dialog is full
  > width, sits on the bottom edge, rounds its top two corners and rises into
  > place; at 640px and up the centred modal is unchanged. It is geometry, in
  > `components/dialog.css`, and no markup moved, so this stays a rendering
  > difference between the layers and not a structural one.
  > **No grab handle in colour.** The grey tree draws one (`.grab`, 17 pages)
  > and drag-to-dismiss is not built. A wireframe may draw the affordance it
  > expects; a product that ships a handle for a gesture that does nothing is
  > showing a control that lies. Listed here rather than in the boundary table
  > because it is one element inside an already-declared boundary.
  > The same pass found that `.app-case{position:relative}` was reaching the
  > dialog on those 17 standalone pages (they put the app frame class on the
  > `<dialog>` itself), which took away the user agent's `position:fixed` and let
  > the modal scroll off the top of the screen with the page behind it.
- Every state is a separate page, navigated from the **left screen-tree drawer**
  (which lists each screen family with its auth variants and states). On screens
  with the auth axis (S5) the states span a 2D matrix: Auth (Logged in / Logged
  out) x State (success / empty / ...), so any auth/state combination is one click
  away in the tree. Same structure and zones as the base page, only the content
  area (and, across auth, the header) changes.
  > **Top bars removed (2026-07-07):** the in-page `.state-switch` bar (Auth /
  > State chip rows) and the `.page-label` status caption that used to sit above
  > the device were deleted from all 99 pages - they duplicated the screen-tree.
  > The state *inventory* below is unchanged (it documents which states each screen
  > has); only the redundant top navigator is gone. See `_critique.md`.

  Empty and error states must show a visible exit action
  (not a dead end), verified against `ia/docs/flows.md`. UI copy on state pages is
  real English text (project rule: all files English), never lorem.
- **Event Feed auth x state matrix built (Step 5, revised in the auth pass):**
  logged-in `event-feed.html` (success base), `-empty`, `-error`, `-loading`,
  `-push-permission-missing`; logged-out `event-feed-logged-out.html` (success),
  `-logged-out-empty`, `-logged-out-error`, `-logged-out-loading`
  (push-permission-missing is logged-in only). Empty exit = Clear filters +
  "Notify me of new events in this category" (`flows.md` T6 subscribe edge).
  Error exit = Try again (mirrors `flows.md` T8 retry). Loading = grey skeleton
  cards. Push = the success feed plus the in-app "Enable notifications" banner
  (sitemap push-permission-missing).
- **Step 6 - remaining spine screens built (the rest of the `_screens.md`
  table).** Every state in that table is now its own page, following the Event
  Feed standard (shared shell, S6 screen tree, state-switcher, real domain text,
  grey-box, no em dash). The auth axis (S5) applies only to the browse screens
  (Event Feed, Event Detail); the activation-gate and Bet screens are invoked
  overlays (modal on desktop, bottom sheet on mobile) and Active Bets is
  account-bound, so those carry a 1D state-switcher only.
  - **Event Detail** (auth axis): logged-in `event-detail.html` (success /
    pre-selected base), `-error` (T8, retry returns here), `-loading`,
    `-resolved` (resolved-while-reading, logged-in only); logged-out
    `event-detail-logged-out.html` + `-error`, `-loading`. Body is identical
    across auth; only the header differs.
  - **Bet Screen** (invoked overlay, base = intent): `bet-screen.html` (intent,
    logged out), `-reconcile` (S5 price moved, T16 cancel), `-insufficient-balance`,
    `-event-closed`, `-error` (on-chain T3), `-processing` (execute moment). No
    separate `-success` page (success is the move to Active Bets).
  - **Sign In / Register** (invoked overlay, base = form): `sign-in.html`,
    `-loading` (OAuth), `-error` (T5), `-provider-conflict`.
  - **Deposit** (invoked overlay, base = form): `deposit.html`, `-loading`,
    `-error-card` (T2), `-error-kyc` (T1), `-widget-load-failure` (S3 fallback),
    `-pending`, `-minimum-not-met`.
  - **Active Bets** (account-bound, logged-in only): `active-bets.html`
    (success / open positions, MJ terminal T14), `-empty-new` (CTA to feed),
    `-empty-resolved` (CTA to History), `-error`, `-loading`.
  - The screen tree (S6) now links these five screens (was `planned`) on every
    page; Win, Loss, Notifications, Wallet, Profile, How It Works, and the Bet
    History tab stay `planned`. Generators: scratchpad `_shell.py` +
    `gen_event_detail.py` / `gen_active_bets.py` / `gen_overlays.py` / `resync.py`.

### 5b. Wireframe revision pass (post Step 6, design-led)

Decisions taken while reviewing the built screens, superseding the matching
earlier rules:

- **Bet entry is an inline sticky panel on Event Detail, not a modal.** The
  standalone Bet modal (the old `bet-screen*.html`) is removed. The bet panel is
  a sticky right rail on desktop and a sticky bottom dock on mobile (taps expand
  to a confirm sheet), so an informed user can stake while scrolling the context.
  Confirm fires the gate; **Sign In and Deposit stay modals**. The bet states are
  now built as panel states on Event Detail: `event-detail.html` (intent),
  `-bet-insufficient` (inline guard -> Deposit dialog), `-bet-reconcile` (S5 price
  moved, re-confirm / T16), `-bet-processing` (execute on-chain), `-bet-error`
  (T3); event-closed is the `-resolved` state. Supersedes the "Bet Screen =
  invoked overlay" line in convention 5.
- **Event Detail has binary and multi-outcome success views.** Binary = one
  YES / NO; multi (`event-detail-multi.html`, + logged-out) lists the outcomes in
  the main column and the panel becomes "pick an outcome" -> YES / NO on it. The
  Event Detail state-switcher is 3 rows: Auth, View (Binary / Multi / Error /
  Loading / Resolved), Bet (Intent / Insufficient / S5 reconcile / Processing /
  On-chain error).
- **Event Detail content order:** event header, then the schematic price chart and
  facts row, then Why this price (FJ2) lower, then Resolution. The bet panel leads
  visually; the narrative is below the fold.
- **Price chart fidelity:** a drawn schematic line (still grey, no color), a
  deliberate step up from the labeled-placeholder rule in Addition A for this one
  element (design call). Money values and the % stay real sample numbers.
- **Category pages (second-level nav -> own page).** Each category opens its own
  page (`politics.html`, `crypto.html`, `culture.html`, `general.html`), not an
  in-feed toggle. Layout: a sub-category side rail (left sticky on desktop,
  scrolling chips on mobile) with sample counts, plus Sort + Frequency on the
  heading row and the category-scoped card grid. The grid is `auto-fill`
  (minmax 240px) so it fits the width left by the rail (no fixed-4-col overflow).
  Sub-category taxonomy and counts are illustrative sample data (Polymarket /
  Kalshi-modelled). Each category is a browse screen with the **auth axis** and a
  2D state-switcher: logged-in and logged-out x success / empty / error / loading
  (32 pages: `politics*`, `crypto*`, `culture*`, `general*`). Empty exit = Clear
  filters + "Notify me of new <category> events" (T6 subscribe edge); error exit =
  Try again + Back to Trending; loading = skeleton grid; logged-out swaps the
  header (Log in / Sign up open the Sign In dialog over the page). Open: the
  `sitemap.md` update (category pages + sub-categories).
- **Sign In / Deposit dialogs: hybrid (decided + built).** A shared native
  `<dialog>` (Sign In and Deposit) is defined once in the shell and emitted on
  every page; triggers (`data-open="signin"` on the logged-out Log in / Sign up /
  Favorites / Notifications / mobile Sign-in slot, and the Event Detail bet-panel
  Confirm / dock Bet) open it over the current page, and Close / backdrop / Esc
  keep you on that page. Providers chain Sign In -> Deposit (`data-flow`). The
  standalone `sign-in-*.html` / `deposit-*.html` pages are kept as the per-state
  design reference (in the tree + switcher); the live dialog covers the happy
  path. Single-source in `_shell` (no per-page hand-duplication); the feed pages,
  authored earlier, are patched by `inject_signin.py`. Native `<dialog>`, minimal
  JS, no libraries.
- **Resolution screens built (Win / Loss).** Both are invoked overlays (modal on
  desktop, bottom sheet on mobile) over a dimmed Active Bets / notification
  context, reached 1 tap from a resolution notification (G1 / G1-equivalent) or
  from a resolved item in My Bets. Account-bound, **no auth axis**. Generated by
  scratchpad `gen_resolution.py`. Win Screen (`win.html` + `-loading` / `-error` /
  `-payout-pending`, 4 pages): "You were right", amount won, plain resolution
  summary, auto-generated Share Card; **Share is the primary CTA, "see next
  events" is deliberately secondary** (research F5: the first win drives
  overconfidence, so celebratory-but-measured, no confetti loop); `-error` =
  Share Card not generated (T11) with a text-share fallback; `-payout-pending` =
  on-chain settlement delay, sharing not gated. Loss Screen (`loss.html` +
  `-loading`, 2 pages): "Here's what happened", **plain resolution note shown
  first** then the amount lost, and **one calm next step with no "bet again"
  promo** (the primary retention intervention against loss-chasing, FJ5 + EJ3); no
  error / payout state at MVP (cancelled-event refunds deferred). The screen tree
  (S6) now links Win / Loss (was `planned`); still `planned`: Notifications,
  Wallet, My Profile, Public Profile, How It Works, Bet History tab.
- **Notifications built (return-trigger list screen).** A full screen (not an
  overlay), reached from the header bell on both breakpoints (not a bottom-nav
  slot, so no bottom slot is marked current). Account-bound, logged-in only, **no
  auth axis**, 1D state-switcher. Generated by `gen_notifications.py`, modelled on
  the Active Bets full-screen pattern (header + main list + bottom nav + footer).
  The list shows the four confirmed alert types (ia/docs/sitemap.md entity 8) grouped
  Unread / Earlier: **position resolved** (taps to Win / Loss - the 1-tap G1 path),
  **odds moved significantly** and **event deadline approaching** (to Event
  Detail), **new event in a followed category** (to the category / Event Detail).
  Each row is a link to its target. States: success, empty (no alerts yet -&gt;
  follow events), error (retry), loading (skeleton), push-permission-missing
  (reuses the `.push-banner` from Event Feed: OS push denied -&gt; in-app banner +
  system-settings deep-link, in-app list still shown). 5 pages
  (`notifications.html` + `-empty` / `-error` / `-loading` / `-push`). Serves the
  return trigger FJ1 / FJ5 / EJ3 (aarrr.md D1-D3). Screen tree now links
  Notifications (was `planned`); still `planned`: Wallet, My Profile, Public
  Profile, How It Works, Bet History tab.
- **Wallet built (money hub).** A full screen reached from the avatar dropdown
  (desktop) and the Portfolio account hub (mobile), so the **Portfolio bottom slot
  is the current marker**. Account-bound, logged-in only, **no auth axis**.
  Generated by `gen_wallet.py`. Shows the balance split (Portfolio = Cash
  available + In-play locked), Deposit (opens the **shared Deposit dialog** via
  `data-open="deposit"` - "deposit again, same Deposit screen"), the
  funds-protection line (held 1:1, EJ2 secondary), and the transaction history
  (deposits, payouts, fees, stakes, withdrawals with signed amounts + status).
  **Withdrawal is a flow inside Wallet, not a screen** (per ia/docs/sitemap.md): a
  native `<details>` expands amount -&gt; destination USDC address -&gt; confirm,
  with a note for the pending / confirmed / failed sub-states; USDC-only at MVP (no
  fiat payout; PIX is Phase 2). The withdraw `<details>` uses a small page-local
  `<style>` injected before `</head>` (scoped to Wallet, not added to the shared
  shell). States: success, loading (skeleton), error (retry) - balance-syncing
  deferred. 3 pages (`wallet.html` + `-loading` / `-error`). Serves FJ4 (primary),
  EJ2 (secondary). Still `planned`: My Profile, Public Profile, How It Works, Bet
  History tab.
- **My Profile + Public Profile built (reputation surface).** One layout, two
  modes; generated by `gen_profile.py` with a small page-local `<style>` (avatar
  row + share-card gallery) injected before `</head>`. **My Profile**
  (`my-profile.html` + `-loading` / `-error`, 3 pages): the mobile **Portfolio
  account hub** - it leads with a portfolio summary (Portfolio = Cash + In-play,
  Deposit opens the shared dialog, Open Wallet links to `wallet.html`), then the
  identity row with **Edit name &amp; avatar**, then the public track record (total
  bets, win rate, resolved), the share-card gallery (past wins, SJ1), and the
  resolved-predictions history (WON / LOST). Reached from the avatar dropdown
  (desktop) / Portfolio slot (mobile) -&gt; **Portfolio slot is the current
  marker**; account-bound, logged-in only, no auth axis. empty-state deferred.
  **Public Profile** (`public-profile.html` + `-loading` / `-error` /
  `-not-found`, 4 pages): the same track record + gallery **read-only** for another
  user - no portfolio summary, no edit, no private data. Reached via an external
  shared win card / leaderboard link (in-app discovery deferred post-MVP, G3); SJ2,
  Dan's primary surface. Carries the **logged-out header** (Log in / Sign up, no
  balance / avatar) because the primary entry is an external shared-card link where
  the viewer is often logged out; no bottom slot is current (`bottom_out("none")`);
  no auth axis built (single representative variant). Extra state **not-found /
  link-expired** routes a stale link back to the Event Feed. Both serve SJ1 / SJ2.
  Still `planned`: How It Works, Bet History tab.
- **How It Works + Bet History built - planned-screens block complete.**
  **How It Works** (`how-it-works.html`, 1 static page; `gen_howitworks.py`, small
  page-local `<style>` for the trust sections): a trust *declaration*, not a FAQ -
  a lead promise then four sections (USDC held 1:1; how events resolve: conditions
  up front, platform team vs public evidence, on-chain proof; pricing / payout:
  AMM timing, fee only on a win, no subscription; "proven not promised" with a
  resolved-markets social-proof stat), CTAs Browse events / Add funds (shared
  dialog), and a note that it is reachable before any deposit (menu / footer /
  Deposit "learn more"). Serves FJ4 + EJ2. No loading / error / empty (static).
  Carries the **logged-out header** (Log in / Sign up, no balance / avatar) since
  the primary entry is a pre-deposit / pre-signup new user; the body is identical
  whatever the auth state, so no auth axis is built; no bottom slot is current
  (`bottom_out("none")`).
  **Bet History (History tab)** (`active-bets-history.html` + `-empty` / `-error` /
  `-loading`, 4 pages; `gen_history.py`): the History tab inside My Bets (G5 - not
  a standalone screen), a private list of resolved bets (won / lost, stake, payout,
  your side, outcome); **tapping a resolved item routes to Win / Loss** (SJ1
  win-share / FJ5 + EJ3 loss entries start here). empty -&gt; Event Feed; account-
  bound, logged-in only, My Bets bottom slot current, no auth axis. The Active /
  History **tabs are now real links** (shared `S.tabs(active)` in the shell;
  `gen_active_bets.py` regenerated to match), so the two tabs navigate. With these,
  every screen in the S6 tree is built; nothing remains `planned` (orphans
  `[SIROTA]` - Settings, Leaderboard, Help / FAQ - stay unbuilt by design, no
  confirmed job).
- **Flow linking pass (Krok 7) - the main flow is clickable end to end.** Each
  screen's main action is now a real `<a href>` along the ia/docs/flows.md routes, only
  to screens / states that exist, with branch exits both ways and no dead ends.
  Wired: Event Feed / category **card question and YES / NO trigger-entries** ->
  the correct Event Detail (binary -> `event-detail.html`, multi -> `-multi`;
  logged-out feeds -> the `-logged-out` Event Detail), via the idempotent
  `wire_flow.py` (re-run after regenerating feed / category pages, like
  `wire_catnav.py`). Bet panel happy path: **S5 reconcile Confirm -> processing ->
  Active Bets** (T14), reconcile Cancel -> Event Detail (T16); on-chain error (T3)
  **Try again -> processing**, **Check wallet -> Wallet**. Gate reference pages are
  traversable too: **sign-in.html providers -> deposit.html** (authOk -> DEP),
  **deposit.html Add funds -> S5 reconcile** (depOk -> S5), and a **How it works ->
  how-it-works.html** link (moreInfo -> HIW; HIW Add funds -> Deposit). The live
  shared dialogs remain the quick happy path (Confirm -> Sign In -> Deposit over
  the page); the reference pages give the full step-through to Active Bets. State
  exits were already wired (empty -> feed, error -> retry, T1 / T2 deposit
  recovery, notifications -> Win / Loss, Bet History rows -> Win / Loss, Win / Loss
  CTAs). Verified by clicking the whole spine in the browser and a broken-link
  audit (0 broken internal links across all pages).
- **Whole-product reconciliation (Krok 8) - the set is consistent.** Coverage:
  every sitemap screen has a wireframe family (99 pages); orphans `[SIROTA]`
  unbuilt by design; the standalone Bet Screen is dissolved into the Event Detail
  panel. A parallel consistency audit (one subagent per screen family, same
  11-point checklist: tree nav, zones, header-by-auth, bottom-nav slots, state
  switcher, grey-box, no em-dash, real text, naming, flow links, page-label) found
  three deviations, all resolved: (1) four logged-out Event Feed pages had a
  bottom-nav zone-tag reading "slot 4 = Portfolio" while slot 4 is Sign in -
  corrected; (2) `active-bets-empty-resolved` History CTA was a bare button -
  wrapped in `<a href="active-bets-history.html">`; (3) **Public Profile and How
  It Works carried the logged-in header (balance) though both are commonly reached
  logged out** - switched both to the **logged-out header** (decision recorded in
  their rows above). All other families (Event Detail, Categories, Gate,
  Resolution + Notifications, Wallet, My Profile, Active Bets / Bet History) audited
  CONSISTENT. Result: 0 em-dash, 0 broken links, consistent zones / naming /
  navigation across all 99 pages.

### 6. Deferred to later phases (Concept onward), not allowed in wireframes

Not part of the wireframe deliverable and not to appear on any wireframe page:
color, typography, shadows, icons, finished UI, motion. These belong to the
Concept phase and later, never here.

### 7. Responsive build (mobile-first)

The product is responsive and built mobile-first. The mobile layout is the
base; desktop is a min-width expansion of the same screen. Wireframes build one
responsive screen, not a separate desktop mock.

**Mobile-to-desktop mapping** (from `ia/docs/sitemap.md`, Desktop layer section,
restated here so a builder does not need to cross-read):

- **Navigation:** bottom nav with 4 slots on mobile; on desktop the same lean
  header (S2) is used, the bottom nav is hidden, and primary destinations are
  reached via the logo (Events), the avatar dropdown (My Bets, Profile), and the
  utility-cluster icons (Notifications, Favorites). No destination is removed.
- **Notifications badge:** on the Notifications item, in the bottom nav on
  mobile, in the top nav on desktop. Always visible on both.
- **Event Feed:** single column on mobile, a responsive card grid up to 4 per
  row on desktop. The per-card context snippet is never dropped to fit more
  columns (snippet hard-lock, minimum card width around 280px).
- **Invoked screens** (Bet Screen, Sign In / Register, Deposit, Win Screen,
  Loss Screen): presented as an overlay in context on both breakpoints, a
  centered modal on desktop, a full-height bottom sheet on mobile. They are
  never a separate full-page destination and never a nav slot.

**Breakpoint thresholds** (set here, since `ia/docs/sitemap.md` left the exact
pixels as a conventions detail):

- mobile, base: 1 column, bottom nav.
- min-width 640px: 2-column feed grid, and the mobile bottom nav is hidden at
  this first desktop breakpoint (the lean header is present at all widths).
- min-width 960px: 3-column feed grid.
- min-width 1280px: 4-column feed grid.

Each threshold is the width where one more ~280px card column fits with gaps
without crowding out the context snippet. These are the feed-grid thresholds;
other screens reflow at the same mobile-first base but do not need a column
count.

This stays grey-box: the layout reflows across breakpoints, but everything is
still grey, with no color, fonts, icons, or shadows.

---

## Shared patterns and axes (from the revised IA)

These are reusable elements defined once here, so every later screen reuses them
rather than reinventing them. All trace to the revised `ia/docs/sitemap.md` (Desktop
layer, Event Feed card, Favorites view, Auth-state axis) and `ia/docs/flows.md`
(trigger-entry edge). They stay grey-box like everything else.

### S1. Footer (global element, product footer)

Every screen carries the same footer, defined once here and reused on every
screen. Grey-box like the rest. This is a multi-column product footer (not a
flat link strip), structured from a prediction-market competitor scan
(Polymarket, Kalshi, Manifold, Limitless). Composition:

- **Brand block:** logo placeholder, a tagline placeholder (TBD), a social-icon
  row, and a language selector.
  - Social icons: X / Twitter and Discord are the mandatory pair (present on
    every competitor); Instagram and TikTok added for consumer reach; Telegram
    for the crypto audience.
  - Language selector: wired as a working dropdown (same `details` + radio
    pattern as the feed filters, updates its own label on choose), but it is a
    placeholder (TBD). No competitor exposes one in the footer and MVP is
    English-only (see memory `feedback-language`); the slot and its language list
    are reserved for future localization, not an MVP feature.
- **Markets column:** by category (Politics, Crypto, Culture, General now;
  Sports is post-MVP) and by topic (Trending topics, dynamic / data-driven, plus
  "View all markets"). Only Polymarket puts market links in the footer and they
  are dynamic trending topics, not fixed buckets; we follow that for the topic
  group while still listing the fixed MVP categories.
- **Product column:** How It Works, Leaderboard, Wallet, My Bets (the real MVP
  destinations), plus API / Developers (post-MVP) and Status (TBD).
- **Support column:** Help Center, FAQ, Contact (all TBD, no support infra at
  MVP) and How It Works.
- **Company column:** About, Careers, Press, Brand (all TBD company pages).
- **Legal strip (bottom):** Terms, Privacy, Responsible play (the reserved
  D-logic slot from `ia/docs/sitemap.md`), Geo restrictions (TBD); a one-line honest
  risk disclaimer ("Prediction markets involve risk of loss", no invented
  statistic); a regulatory / licensing labeled placeholder (no invented license
  number or regulator name; notes no-US real-money and geo + KYC per regulation);
  and a copyright line.

TBD convention: anything not in MVP carries a small dashed `TBD` (or `post-MVP`
/ `dynamic`) tag rather than being omitted, so the footer doubles as a roadmap.
Skipped deliberately (no competitor uses them in the footer and they are not MVP):
app-store badges and a newsletter signup.

### S2. Header (shared component, lean header)

The header is the same lean component across screens, reused on every screen,
and is the same at all widths.

- **Left:** a hamburger icon (reserved for future scaling, no primary items at
  MVP) and the brand logo. The logo is Events / home: clicking it returns to the
  Event Feed.
- **Right utility cluster (desktop):** a balance shown as a Portfolio / Cash
  swap (one figure at a time + a swap icon: Portfolio = Cash + In-play, default,
  toggles to Cash = available; not two figures like competitors), Favorites
  (heart icon, opens the Favorites view), Notifications (bell icon with a permanent
  unread badge), and the avatar. The avatar opens a dropdown, collapsed by
  default, opening on click: My Profile, My Bets, Wallet / Deposit, How It Works,
  Logout. There is no standalone Deposit button in the header.
- **Second-level navigation:** a category sub-nav band sits directly under the
  header (Trending default, Politics, Crypto, Culture, General). Categories are
  navigation; the feed sort control is a feed control on the feed heading row,
  not in this band.
- **Mobile:** the same lean header, but the right side keeps the Notifications
  bell (with badge) and the avatar (the balance is removed: no room at 360px).
  Bottom nav, 4 slots with icons: Events, My Bets, Favorites, and Portfolio.
  Notifications and Favorites are swapped vs the cluster: Notifications is the
  header bell at both breakpoints; Favorites is the mobile bottom slot (and a
  desktop header heart). The Portfolio slot replaces Profile, shows the portfolio
  balance figure in place of the icon (label "Portfolio"), and opens the account
  hub (My Profile extended with a portfolio summary). Profile is reached there,
  not as its own slot.
- **Icons:** simple monochrome outline icons (grey stroke, no color, no fill),
  drawn at a consistent size so the element footprint is realistic. Use an icon
  or a text label per element as space dictates; both stay grey-box.
- **Logged-out delta:** the right cluster (and the mobile Portfolio slot) show a
  "Sign in" entry instead of the balance, Favorites, Notifications, and the
  avatar; the logo, the category sub-nav, and the body are unchanged.

### S3. Event card (shared pattern, two layouts)

The event card is a reusable pattern. Composition:

- Thumbnail placeholder image.
- Event question (the primary hook).
- Compact probability %, which does not dominate the card.
- YES / NO controls that act as a trigger-entry: a tap routes to Event Detail
  with the side, and for multi-outcome the option, pre-selected. It does NOT
  place a bet on the card and does not bypass Event Detail.
- Small meta: volume and closing date.
- Bookmark control, placed as a small element in the meta row (see S4).
- No category badge, no context snippet.
- No "Open event detail" button. The card has no footer and no full-width open
  button; the event question itself is the link to Event Detail (neutral entry).
  This keeps the card compact and the list quick to scan.

Two layouts:

- **Binary:** one question, the % of one side, large YES / NO controls.
- **Multi-outcome:** rows of option plus % plus compact YES / NO controls, but
  the feed card shows at most the two leading positions (the options with the
  highest probability / most stake at that moment) and no "+N more" line. The
  full option list is shown only after the user opens the event (via the question
  link). Omitting the extra line keeps multi-outcome cards close to the height of
  a binary card, so meta rows line up across the grid instead of leaving tall,
  empty cards next to short ones.

Multi-outcome is a normal `Event.Type` layout, not the rejected trading-board
view. Note: this card pattern supersedes the earlier "context snippet on the
card" and snippet hard-lock framing in convention 7 and Addition C; the card is
now clean and the FJ2 context block lives on Event Detail only.

### S4. Bookmark / saved (pattern)

Cards carry a bookmark control. Saved events are reached through the Favorites view
under Events (a filter over the feed) and via the Favorites (heart) entry in the
desktop header. Favorites is a view, not a new destination or screen, so it is not
a separate wireframe screen.

### S5. Auth-state axis (top-level page axis)

Logged-out versus logged-in is a TOP-LEVEL axis of the page states, sitting
above the screen states. Each browse screen exists as a logged-in and a
logged-out variant, and under each, the screen states (success / empty / error /
loading / ...). It is a real page variant, not a header-only delta appended to
one page, because the logged-out header is materially different (no account).

- **Logged-in header (S2):** balance (Portfolio / Cash swap), Favorites,
  Notifications (with unread badge), avatar dropdown.
- **Logged-out header:** the balance figure and the avatar dropdown are removed
  and replaced by Log in + Sign up entries. Favorites (heart) and Notifications
  (bell) are kept as affordances, but tapping either while logged out routes to
  Sign In (saving and alerts need an account), and the bell shows no unread
  badge. On mobile the Portfolio bottom-nav slot becomes a Sign in entry.
- The logo (Events home), the second-level category nav, the feed body, and all
  cards are identical and browsable in both auth states; only the header (and the
  mobile slot 4) differ.
  **THIS LINE WAS TRUE OF NINETEEN PAIRS OF TWENTY AND FALSE OF THE TWENTIETH UNTIL
  2026-08-16, and the twentieth is the one a visitor lands on.** Measured across the
  whole auth matrix: 19 pairs identical in the body, and `event-feed.html` against
  `event-feed-logged-out.html` differing by the entire hero band (`feed-hero`,
  `hero-feature`, two `hero-trust`, the brand tile, `hero-hot`), by four cards, by the
  sub-filter and its twelve `data-cat` attributes, by the load-more row, by the SEO
  wrapper and by the sub-category rail. **The trust proof is what it cost**: "1,284
  events resolved on-chain" sat at y=846 on a phone for a signed-in reader and at
  **y=4,095 for a visitor**, 4.8 times further down, and the visitor is the one it was
  written for. The bodies are identical now, in both trees, and the one delta that
  remains is correct: a signed-out visitor has no saved event, so the bookmarked card
  resets to `aria-pressed="false"`. Verified by measuring `main.feed`: **the same
  height to the pixel at 390 and at 1280 in both trees**, and the only box that moves
  is the header, which is what this line says.
- **Naming:** logged-in pages keep the base names (`event-feed*.html`);
  logged-out pages add a `-logged-out[-state]` suffix. `push-permission-missing`
  is logged-in only (account-bound), so it has no logged-out counterpart.
- The auth/state combinations span a 2D matrix (Auth x State); the screen tree
  (S6) nests the states under a Logged in / Logged out sub-group per screen, and is
  now the only navigator between them (the in-page state-switcher bar was removed,
  see above).
- The real auth branch still lives at the activation gate (Bet Screen Confirm ->
  Sign In -> Deposit); that is unchanged. (This supersedes the earlier
  "header-level delta, no separate logged-out page" containment rule.)

### S6. Screen-tree nav (global wireframe element)

Every wireframe page carries the same left navigation panel, a tree of the whole
screen inventory, so the full structure is visible from any page and you can jump
anywhere. Same grey-box styling as the rest; no color.

- **Structure (source of truth, nothing invented):** section -> screen -> its
  states, indented to show nesting. Sections and screens are the groups from
  `ia/docs/sitemap.md` Screens (Events, Activation gate, Bet, Resolution, My Bets,
  Notifications, Wallet, Profile, How It Works, Orphans). States per screen come
  from that screen's States line in the sitemap and the screen x state table in
  `_screens.md` (loading / empty / error / success plus the notable
  product-specific ones). On screens with the auth axis (S5), the states are
  nested under a Logged in / Logged out sub-group (S5 is the top level), so the
  tree reads section -> screen -> auth -> state.
- **Links and current:** each screen node links to its page (planned pages are
  tagged `planned` until built); the current page and its current state are
  marked active.
- **Responsive:** a fixed left rail at >= 1440px (body gets a left padding so the
  device clears it); below that it is a toggle-button drawer that slides over the
  content (overlay), so it never reduces the responsive device width or disturbs
  the feed grid. Same drawer pattern the project's IA pages use, restyled
  grey-box.
- **Every new wireframe screen gets this same panel**, with its own node marked
  active. Keep the tree in sync when screens or states are added.

### S7. Featured slot (one screen, decided 2026-08-13)

The Trending feed opens with a **featured event**, above the grid: `.feed-hero` in both trees,
one occurrence on `event-feed.html` and nowhere else. It was in the markup for three weeks
before it was in any document, which is `docs/backlog.md` 77 and the reason this section exists:
**a block that arrives by being built is a block nobody has decided.** It is kept.

- **Scope: one slot, on the Trending feed only.** Not on the four category feeds, not on
  Favorites, not on any logged-out variant of them, and not on a screen that is not a feed.
  A second featured slot is a new decision, not an extension of this one.
- **What fills it: the event with the highest 24-hour volume among open markets.** A measurement
  the product already holds, so the slot needs no editorial queue and no admin screen for MVP,
  and it cannot show an event that has resolved. If the feed is empty the slot is absent, which
  is why the empty, error and loading states of `event-feed.html` do not carry it.
- **It is a bigger card, not a different object.** The question, the odds, the volume, the close
  date and the two outcome buttons are the card's, in the card's order; what it adds is room, a
  chart of the last 30 days, and the event photograph. Nothing in it is reachable only there.
- **It is not a state.** There is no "no featured event" copy, because the absent slot is the
  feed's own empty state.
- **The photograph is the paint's**, S3's rule, and the grey tree carries the slot without it.
  On 2026-08-13 the painted photograph was found to have drawn the top-left 9.8% of its frame
  since the day it landed, so what the featured slot has actually been showing for three weeks
  is empty sky. `components/hero.css` holds the cause. **Nobody noticed, and that is the fact
  this decision was taken with**, not against.

---

## Three additions (Yonder needs these beyond the base 7)

### A. Grey-box rule for data

Yonder screens carry data the generic demo product does not: a
probability chart, the % number, fees, payouts, and USDC amounts. The grey-box
rule still holds, with two clarifications:

- A chart is a labeled placeholder zone, for example a bordered box captioned
  "probability chart". Never a drawn, plotted, or faked chart.
- The % number and money amounts are real, labeled sample values (for example
  "67%", "$5", "$8.50 potential payout"), never lorem and never an empty box.
  A number that carries meaning is shown as a number, because the layout cannot
  be judged without it.

### B. Sample-content honesty

Example events, names, and amounts in the wireframes are illustrative sample
data. They are realistic so the layout reads true, but they are not a real
market and not a finding from research.

- Realistic domain content is allowed as a sample.
- It is never labeled or implied to be a real event or a verified fact.

This keeps the "never invent" rule intact while the screens stay legible: the
content looks like the product, but no page claims a sample event is real.

### C. Annotations and on-page navigation tree (moved out of the wireframes)

Per the Phase B roadmap, every wireframe ties back to the research through two
elements: **light annotations** (each major block links to the job / research
finding it serves, e.g. "context narrative -> FJ2 differentiator") and an
**on-page navigation tree** (where the screen sits on the main-flow spine).

**These no longer live inside the wireframe pages.** The wireframes are now kept
clean grey-box UI only. The inline `zone:` chips, the `.side` block (the
`zone -> job / finding` annotation list and the nav-tree / header-model /
responsive / variant notes) were extracted into a dedicated IA visualization:

- **`ia/annotations/` (one HTML page per screen family, all states inside).**
  Each page shows, per state: a **zone map** (the ordered layout zones, with
  sub-region labels nested under their parent zone), the **annotations** list
  (zone -> job / finding), a link to the live wireframe, plus shared
  **structure / flow** notes (main-flow spine, header model, responsive
  behavior, documented variants, rollout status). `ia/annotations/index.html`
  is the entry point. Category pages (Politics / Crypto / Culture / General)
  share one template doc.
- **Generated, idempotent.** Built by `wireframes/_generators/ia_annotations.py`
  (`build` extracts to `ia/annotations/`; `strip` removes the blocks from the
  wireframes; `all` does both). To re-derive after any wireframe edit that still
  carries the blocks, run `build` **before** `strip`. IA source of truth stays
  `ia/docs/sitemap.md` + `ia/docs/flows.md`.

---

## Two scope notes

### Bet Screen base page is the intent state

The Bet Screen base page (`wireframes/bet-screen.html`) is the intent state, the
representative view of the screen. Its success is the transition into Active
Bets, so the Bet Screen does NOT get a separate `-success` page. Every other
spine screen uses success as its base page, per Rule 5.

### Every product-specific state stays its own page

Keeping every product-specific state as its own page is deliberate. For the Bet
Screen this means several pages (intent as the base, then `-reconcile`,
`-insufficient-balance`, `-event-closed`, `-error`). Each one resolves a
distinct moment of the money flow, so none is dropped or collapsed. Recording
this here so the page count is expected, not a surprise, in Step 03.

---

## Shared chrome wiring (2026-06-28)

Header and bottom-nav controls are real navigation, not dead buttons:

- **Logged-in header:** Favorites heart -> `favorites.html`, Notifications bell ->
  `notifications.html`, avatar dropdown -> My Profile / My Bets (`active-bets.html`)
  / Wallet / How It Works / Logout (`event-feed-logged-out.html`).
- **Logged-out header:** Favorites + Notifications + Log in / Sign up open the
  sign-in dialog (no account to navigate to yet).
- **Bottom nav (mobile):** logged-in Events / My Bets / Favorites / Portfolio ->
  feed / active-bets / `favorites.html` / my-profile; logged-out Events -> logged-out
  feed, My Bets + Favorites -> sign-in dialog, Sign in -> sign-in dialog.
- **Dialog CSS:** any page that carries the sign-in / deposit `<dialog>` markup
  must also carry the `dialog.app-dialog` CSS, or the dialog renders unstyled.

Wiring is applied by the idempotent post-processor `fixpack.py` (run after the
generators). The **Favorites view** (`favorites.html` + empty + loading) is the logged-in
"filter over the feed" target for the Favorites control.

### Header dropdowns + in-context deposit + logged-out redirect (`chrome2.py`)

- **Notifications bell (logged-in)** is a native `<details>` dropdown (no chevron):
  click shows a mini-list of recent notifications plus a `See all` link to
  `notifications.html`, so it does NOT navigate the user away from the current page.
- **"+" by the desktop balance** opens the deposit dialog directly
  (`data-open="deposit"`), so a user can top up in context (e.g. while on an event)
  instead of leaving for the Wallet / Profile and losing their place.
- **Logged-out redirect:** logged-out pages carry `body[data-loggedin-target]` (the
  logged-in counterpart, e.g. `event-feed-logged-out.html` -> `event-feed.html`).
  After sign-in (a provider choice), closing OR funding the deposit dialog navigates
  to that target, because the user is now authenticated. Closing the sign-in dialog
  *before* choosing a provider still keeps you on the page (not signed in).

Applied by `chrome2.py` (idempotent, run after `fixpack.py`).

- **Empty notifications dropdown:** on logged-in empty-state pages (`*-empty*`)
  the bell dropdown is itself empty (no badge, "No notifications yet") and its
  `See all` link points at `notifications-empty.html`, so the empty flow stays
  consistent instead of previewing notifications that lead to the populated page.
  Applied by `chrome3.py` (run after `chrome2.py`).

### Event Detail content tabs

Below the event content (chart, why-this-price, resolution) Event Detail carries a
Polymarket-style tab strip: **Comments**, **Top Holders**, **Positions**,
**Activity**. It is a CSS-only switch (hidden radio inputs + `:checked ~` sibling
selectors), no JS. Comments has a sort segment and a composer (logged-out shows a
"Sign in to join the discussion" prompt); Positions highlights the user's own row
when logged in (logged-out prompts sign-in); Top Holders and Activity are public.
Present on binary / multi / resolved, logged-in and logged-out. Built in
`gen_event_detail.py` with a page-local `<style>` (the `.ed-tab*` / `.cmt-*` /
`.hold-*` / `.ptable` / `.act-*` classes), so the tab CSS lives only on Event Detail.
On multi-outcome markets all four tabs are outcome-aware: Top Holders is one
ranked list tagged by outcome, Activity names the outcome (e.g. "bought 500 JD
Vance YES"), Positions swaps the Side column for an Outcome column, and the comment
holder badges name the outcome ("Holds 320 JD Vance"). Binary keeps the YES / NO
form.

**Multi bet panel focus:** the sticky bet panel does NOT repeat the outcome list
(which can run 10-20 long). The left column lists every outcome with YES / NO
triggers and marks the selected one; the right panel stays focused on that single
chosen outcome (name + %, YES / NO, amount, payout, Confirm) with a "Change" link
back to the list (`#edOutcomes`). This keeps the panel fixed-size regardless of how
many outcomes the market has.

## What comes next

The per-screen file list and the screens themselves are produced from Step 03
onward, with each later step reading this file before building anything.

## The boundary with the colour tree (2026-07-28, Stage 09 step 7d)

`wireframes/` owns structure and copy. `ui-visual/` owns the visual layer. That
rule had no check behind it for two stages, and Stage 08 broke it quietly: the
Event Detail was **redesigned** while it was being painted, and the redesign never
came back here. Measured on `<main>`, 55 of 72 twinned screens differed; Event
Detail carried 792 elements in colour against 570 in grey, and the extra 222 were
an AMM market panel, a rebuilt chart, a rules-and-context tab split, a share-and-
save cluster, an odds bar, and a real `<input>` where this tree had a `<span>`
pretending to be a field. The tree that owns structure was the one that was wrong.

The structure was ported back by `wireframes/_generators/port_structure.py`
(idempotent, reads the painted twin, never writes to `ui-visual/`). From here the
two trees have to agree, and **gate 18** in `ui-kit/_check_kit.py` fails the build
when they do not.

**Seven differences are the boundary itself, not drift.** They are declared, and the check is
blind to exactly these and nothing else. **It was six until 2026-08-15**, when the Animation stage
added motion, and the sentence below about `ui-kit/_check_kit.py` names a gate that was deleted with
the generated vitrine on 2026-08-07: what compares the trees now is a diff of two file lists and a
reading taken by hand, which is this repository's rule about measurements rather than machines.

| what | grey | colour | why it is not drift |
|---|---|---|---|
| plate wrappers | absent | `.cat-layout`, `.cat-main`, `.feed-inner` | a div whose only job is to draw a stone plate is paint. Porting it would put an empty box in the wireframe to record a shadow |
| icons | raw `<path>` | `<use href="#id">` against an inline sprite | one mechanism per tree. The port resolves every `use` back into the paths it points at |
| photography | the box, empty, **with the words `thumbnail placeholder` in it** | `<img>` and `background-image`, **and no words** | a wireframe draws a box where a picture goes. 105 pages, zero image elements, and it stays that way. **The LABEL half of this was only half ported until 2026-08-16**: the paint carried the grey tree's `thumbnail placeholder` text inside every `.thumb` and `.ed-thumb`, hidden from the eye by `color:transparent;font-size:0` and standing in the accessibility tree, 24 `StaticText` nodes on `event-feed.html` alone and 198 across the painted tree. A label for an empty box is the wireframe's job and there is no empty box in the paint. It stays on 21 grey files and is gone from 105 painted ones and 9 kit pages |
| the busy region | **NOT a difference. The same element in both trees, always** | the same element in both trees, always | **This row said the opposite for one day and the premise under it was false.** It read the divergence on `my-profile-loading`, `public-profile-loading` and `wallet-loading` as the plate-wrapper row above showing its consequence: the grey tree has no inner container, so it marks `<main>`. **Measured 2026-08-16: `.cat-main` exists in BOTH trees on all three screens**, so nothing forced the grey tree's hand and the two had simply chosen differently. `<main class="feed">` also holds the category rail, which is not loading, so marking it busy tells a reader that navigation is unavailable; `.cat-main` is the column that carries the skeletons. The grey moved to the paint on all three. Verified on both engines over both trees: every busy region is now the same element with `.sk-status` as its first child. **A plate wrapper that exists in both trees is not a plate wrapper**, and the row above is the one to check before blaming it. The status line still goes INSIDE the busy region rather than onto it, for the reason this row always gave: a `role="status"` on a landmark takes the landmark away |
| chart data | typed into the markup | empty, filled by a script on load | a wireframe DRAWS its data, a product COMPUTES it. The series is read out of the painted script and written in statically, so the wireframe shows a chart without borrowing the product's JS |
| the `TBD` chip | 14 `span.tbd` and one `p.placeholder-line` per footer | none | a wireframe is obliged to mark a destination nobody has built; a product that shows a user the word TBD is showing them the bookkeeping. Added in step 7e |
| the page behind an invoked overlay | absent: the sheet on a plain backdrop | header, feed, bottom nav and footer behind the dialog | convention 5, below. A wireframe of an overlay draws the overlay; a scrim has to be a scrim over something. Added in step 7e, and it is the one boundary that is CHECKED rather than skipped: the gate asserts that grey has no chrome on those 17 screens and the paint has all of it, so neither side can drift into the other by accident |
| motion | one declaration, `transition: transform .2s ease` on the drawer, written into all 105 inline blocks | two duration tokens, two curves, and a reduced-motion block that redeclares them | **Added 2026-08-15 by the Animation stage, and it is the SEVENTH.** Six were declared here and motion was not among them, so the day the paint took its durations from tokens the two trees began to disagree about something nobody had written down, which is drift by this document's own definition. It is a declared difference and not a port for a mechanical reason: **a grey file links no stylesheet, so it cannot hold a token**, and the numbers would have to be written 105 times, which is exactly what one width change already cost this folder in 312 edits. The drawer moves so the tree can be clicked through, and its `.2s` is scaffolding rather than a claim about the product |

**And the seventh difference has a cost that the other six do not, so it is named rather than
implied: the grey tree does not answer `prefers-reduced-motion` at all.** Measured 2026-08-15 with
the setting emulated in Chromium 151 and WebKit 26.5: **105 elements above 1ms over 105 of 105
documents**, every one of them that same drawer. The paint answers it on every element of every
screen; this tree cannot, because the mechanism is a token and there is nowhere here to declare one.
A person who has asked their operating system for less movement still gets a sliding drawer in the
grey tree, and that is a known and accepted cost of the tree linking nothing, not an oversight. The
record is `../ui-kit/docs/motion.md`, under what the token override does not reach.

## All four regions are compared (2026-07-28, Stage 09 step 7e)

Step 7d compared `<main>` and nothing else, which left the header, the bottom nav
and the footer as the one place where the two trees could drift with every gate
green. They had:

- `.cat-condensed`, the category strip that slides into the sticky header once
  the full bar scrolls away: on 68 painted screens and **0** grey ones. A whole
  navigation control, and the painted logged-out header did not have it either;
- the footer trust block, rewritten in paint on 55 screens (see Step 26 in
  `voice/docs/microcopy.md`);
- `aria-current="page"` on the **Events** slot of all 76 painted screens whatever
  screen it was, where the grey tree marks the slot the page actually is;
- the logged-in header over a logged-out bottom nav on ten screens.

Two tools, in this order, because the drift ran both ways:
`ui-visual/_reconcile_chrome.py` gives the painted chrome back the state the grey
tree owns, then `wireframes/_generators/port_chrome.py` copies the corrected
shape back. **The paint owns the shape of the chrome; the grey tree owns which
state it is in.** The one exception is the auth variant on the ten screens that
disagreed: there was no fact to read, so it was decided page by page with a
reason each, written once in `_reconcile_chrome.py`, and both trees follow it.

## One dialog, one copy (2026-07-28, Stage 09 step 7f)

Sign In and Deposit each exist twice in each tree: as the shared `<dialog>`
embedded on every screen, and as the **standalone page that IS that dialog**.
Gate 18 compares a screen with its grey twin and never with its own second copy,
so the two drifted from Stage 08 until step 7f: the shared dialog carried the
real Google, X and Apple marks and the page a person actually opens carried the
wireframe placeholders, the one standing in for Google being a circle with a plus
in it.

One markup now, kept by `ui-visual/_unify_dialogs.py` and checked by **gate 19**.
The canonical copy is the one in `ui-visual/event-feed.html`; every other screen
gets it byte for byte, and the standalone page gets its body and its sub-line.
**Three differences are context, not drift:**

| what | in a dialog | on the page | why |
|---|---|---|---|
| the heading level and the close | `<h2>`, closes with `data-close-dialog` | `<h1>` (gate 15), closes with a link back | a dialog is opened over a page that has already spent its h1. Only these two: the sentence under the title is copy and belongs to both |
| the wiring | `data-flow` / `data-open` open the next sheet over the screen you are on | each control wrapped in `<a href>` | there is nothing behind a page to stay on. The table of hrefs is in `_unify_dialogs.py`, the one place either wiring is written |
| the state screens | n/a | `sign-in-error` and the rest have their own bodies | a state is not a copy, so only the BASE page of each family is compared |

Neither copy simply won. Reading both is what showed why: the standalone Deposit
had three things the shared one had lost, a label over the payment widget, the
sentence that says card payments are converted via Transak, and the exit to How
It Works, which is the trust affordance that screen exists to earn. Those were
merged into the canonical copy (Step 27 in `voice/docs/microcopy.md`) before the
tool was written.

The three shared dialogs are ported between trees as well, like the header. The
how-it-works one had drifted furthest of anything in the repo, 42 elements in
grey against 64 in colour, because Stage 08 rebuilt it with a hero, icon chips
and an FAQ list and the tree that owns structure never heard.

**Scope is where a block may stand.** The same pass found the How It Works page
rendering as an unstyled document, and the cause was one word in a selector:
every rule for the hero, the icon chips and the FAQ list began
`.app-dialog.hiw-dialog`, so none of them could reach a page. A rule that
describes a BLOCK is written unscoped; only what is about being a dialog (its
width, its close disc, a sheet's body padding) keeps the ancestor.

## Search is a surface, and grey draws the state rather than simulating it (2026-08-17)

Search stopped being a destination on 2026-08-17. The mark in the header used to
be a link to a page where the field stood **at y=221 on a phone**, unfocused,
under a category rail and an h1; it is a **surface** now, and which surface is a
question about width. Below the RAIL rung it is a full-bleed sheet; at 56.25rem
and above the field stands in the header row itself and the mark is
`display:none`. The rung is a measurement rather than a preference: the free
middle of that row is **69px at 640, 137 at 760 and 277 at 900**, and 640 is the
tightest width on the whole ladder because DESK turns on the balance pill, the
heart and How it works at once.

**In this tree the mark stays a LINK and no sheet is simulated.** All 91 grey
screens that carry the mark get the inline header field, and exactly **one** of
them carries the sheet: `event-feed-search.html`, with the `<dialog>` statically
`open`, because a state is a page here. A closed `<dialog>` on the other 90 would
be markup with no state, which is the thing this tree has spent two stages taking
out of itself. The paint carries the sheet on all 108 screens because the paint
has the script that opens it, and that is the difference between a tree that owns
structure and a tree that owns behaviour.

**The two result pages keep their own field and lose it at the rung.** A page is
where a link lands, so `event-feed-search-results` and `-empty` still hold a field
a person can retype into; above 56.25rem the header carries one and the in-plate
copy is `display:none`, because two fields for one query on one screen is the same
defect as a magnifier linking to the page it stands on.

**What the grey sheet shows and why it is not the reference's shape.** Categories,
five tiles, and Popular right now, four rows. The reference this was drawn against
puts a row of sort modes above the topics; that product has thousands of markets
and Yonder has 25, and two rows of five chips in one sheet would have been the
fourth and fifth controls made of the same five words on a screen where three had
already been counted. The four popular rows are the highest volume in the catalog,
which is a fact the product already prints on every card.
