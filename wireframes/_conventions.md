# Wireframes - Conventions (Step 02)

This is the wireframe rulebook for Predict Market. Every screen and every state
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

Every label and string is real Predict Market content, pulled from
`IA/sitemap.md` where the phrasing already exists. Examples of the exact
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
- Every state page carries a state-switcher at the very top (above the device).
  On screens with the auth axis (S5) it is a 2D switcher: an Auth row
  (Logged in / Logged out) and a State row (success / empty / ...), each marking
  the current value, so any auth/state combination opens side by side. Same
  structure and zones as the base page, only the content area (and, across auth,
  the header) changes. Empty and error states must show a visible exit action
  (not a dead end), verified against `IA/flows.md`. UI copy on state pages is
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
  The list shows the four confirmed alert types (IA/sitemap.md entity 8) grouped
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
  **Withdrawal is a flow inside Wallet, not a screen** (per IA/sitemap.md): a
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
  Dan's primary surface. No bottom slot is current (`bottom_in("none")`); no auth
  axis (a public page; the viewer's login state does not change it). Extra state
  **not-found / link-expired** routes a stale link back to the Event Feed. Both
  serve SJ1 / SJ2. Still `planned`: How It Works, Bet History tab.

### 6. Deferred to later phases (Concept onward), not allowed in wireframes

Not part of the wireframe deliverable and not to appear on any wireframe page:
color, typography, shadows, icons, finished UI, motion. These belong to the
Concept phase and later, never here.

### 7. Responsive build (mobile-first)

The product is responsive and built mobile-first. The mobile layout is the
base; desktop is a min-width expansion of the same screen. Wireframes build one
responsive screen, not a separate desktop mock.

**Mobile-to-desktop mapping** (from `IA/sitemap.md`, Desktop layer section,
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

**Breakpoint thresholds** (set here, since `IA/sitemap.md` left the exact
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
rather than reinventing them. All trace to the revised `IA/sitemap.md` (Desktop
layer, Event Feed card, Saved view, Auth-state axis) and `IA/flows.md`
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
  D-logic slot from `IA/sitemap.md`), Geo restrictions (TBD); a one-line honest
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
  (heart icon, opens the Saved view), Notifications (bell icon with a permanent
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

Cards carry a bookmark control. Saved events are reached through the Saved view
under Events (a filter over the feed) and via the Favorites (heart) entry in the
desktop header. Saved is a view, not a new destination or screen, so it is not a
separate wireframe screen.

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
- **Naming:** logged-in pages keep the base names (`event-feed*.html`);
  logged-out pages add a `-logged-out[-state]` suffix. `push-permission-missing`
  is logged-in only (account-bound), so it has no logged-out counterpart.
- Every state page carries a 2D state-switcher (Auth row + State row) so the
  matching auth/state combinations open side by side, and the screen tree (S6)
  nests the states under a Logged in / Logged out sub-group per screen.
- The real auth branch still lives at the activation gate (Bet Screen Confirm ->
  Sign In -> Deposit); that is unchanged. (This supersedes the earlier
  "header-level delta, no separate logged-out page" containment rule.)

### S6. Screen-tree nav (global wireframe element)

Every wireframe page carries the same left navigation panel, a tree of the whole
screen inventory, so the full structure is visible from any page and you can jump
anywhere. Same grey-box styling as the rest; no color.

- **Structure (source of truth, nothing invented):** section -> screen -> its
  states, indented to show nesting. Sections and screens are the groups from
  `IA/sitemap.md` Screens (Events, Activation gate, Bet, Resolution, My Bets,
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

---

## Three additions (Predict Market needs these beyond the base 7)

### A. Grey-box rule for data

Predict Market screens carry data the generic demo product does not: a
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

### C. Annotations and on-page navigation tree

Per the Phase B roadmap, every wireframe ties back to the research. Two required
page elements:

- **Light annotations.** Each major block on a screen carries a short note
  linking it to the job or research finding it serves (for example "context
  narrative -> FJ2 differentiator", "fee line -> H6"). Keep annotations out of
  the layout flow: put them in a side note or a footnote list, so the grey box
  stays clean and the annotations do not get mistaken for UI.
- **On-page navigation tree.** Each wireframe page shows a short tree of where
  this screen sits among the others (the main-flow spine from `_screens.md`:
  Event Feed -> Event Detail -> Bet Screen -> Sign In / Register -> Deposit ->
  Active Bets), so any single page is readable in context. This is a required
  element of every page. It is described here, not built here.

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

## What comes next

The per-screen file list and the screens themselves are produced from Step 03
onward, with each later step reading this file before building anything.
