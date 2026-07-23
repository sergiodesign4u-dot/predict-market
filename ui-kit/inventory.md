# UI Kit - Component Inventory

Read out of the whole product, not invented. Source: all `wireframes/*.html` (104 pages, every
screen and state) read together with `ia/docs/sitemap.md` and `wireframes/_conventions.md` (the
S1-S6 shared patterns). This table is the build-list for `ui-kit/kit.css` + `ui-kit/kit.html`;
the color language it is dressed in is root `DESIGN.md`.

## Inclusion rule

- A row is a component that recurs on **two or more pages** (measured as distinct wireframe files
  that carry the exact class). One-time blocks are listed under **One-off** at the end and are NOT
  pulled into the kit.
- Components concentrated in one screen family but spanning several of its pages/states (the Event
  Detail set, the shared dialog) ARE kit components: the kit must render them identically across
  those pages.
- **Origin** column: `WF` = present in the grey wireframes (structure owned by `wireframes/`);
  `UV` = added only in the color layer (`ui-visual/_theme.css`, not in the grey wireframes) and so
  documented from the painted screens + `DESIGN.md`. Both belong in the kit.
- **Photo** column: `-` none, `event` real event/news image, `portrait` a person, `art` decorative
  brand/trust art (already shipped as webp in `ui-visual/assets/`). Feeds Step 04 (visuals).

`#f` = number of distinct wireframe files the component appears on (UV rows have no WF count).

---

## 1. Navigation and chrome

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| App header (lean) | all header screens (feed, category, detail, active-bets, notifications, wallet, profile, how-it-works) | logged-in / logged-out | 87 | WF | - |
| Logo (Events home) | every header screen | default | 87 | WF | - |
| Balance / Portfolio-Cash swap | logged-in header | swap Portfolio <-> Cash; "+" opens Deposit | 53 | WF | - |
| Notifications bell + mini-dropdown | logged-in header | populated / empty / badge on-off | 53 | WF | - |
| Avatar menu (dropdown) | logged-in header | closed / open | 53 | WF | portrait |
| How-it-works button | header (next to logo) | default; opens HIW dialog | 87 | WF | - |
| Icon button (ghost) | header utility, event actions | rest / hover / focus | 87 | WF | - |
| Auth entries (Log in / Sign up) | logged-out header + gate | default; open Sign In dialog | 34 | WF | - |
| Category nav band | feed + category pages | per-category active; condensed on scroll | 57 | WF/UV | - |
| Sub-category rail | category pages (politics/crypto/culture/general) | active row + sample count | 32 | WF | - |
| Content sub-filter chips | Trending feed | active | 5 | UV | - |
| Bottom nav (mobile, 4 slots) | all header screens | per-slot current; logged-out (Sign in slot) | 87 | WF | - |
| Active / History tabs | My Bets (active-bets, history) | active tab | 9 | WF | - |
| Footer language menu | every footer screen | closed / open (TBD) | 87 | WF | - |
| Screen-tree drawer | every wireframe page | - | 104 | WF | - (course chrome, not product; kit uses its own nav) |

## 2. Browse: feed and cards

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| Event card, binary (treatment B) | feed, category, favorites, event-feed-push | rest / hover | 36 | WF | event |
| Event card, multi (treatment D) | feed, category, event-detail, favorites | rest; 2 leading options | 20 | WF | event |
| Odds bar (thin, green YES on red track) | feed / category / detail cards | injected from prob | - | UV | - |
| Tinted YES / NO buttons | every event card + bet panel | rest / hover / compact | 14 | WF | - |
| Probability figure | cards, detail | value | 21 | WF | - |
| Card meta row (Volume / Closes + bookmark) | every event card | bookmarked on / off | 23 | WF | - |
| Responsive card grid | feed, category, favorites | populated / skeleton | 23 | WF | - |
| Feed SEO block (below fold) | feed + category pages | default | 14 | WF/UV | - |
| Featured hero band (feature + trust + brand tile + hot list) | Trending feed | default | - | UV | event, art |
| Related events plate | event-detail | list | 9 | WF | - |
| Load-more control | feed, category | rest / hover | 20+ | WF/UV | - |

## 3. Event Detail

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| Two-plate layout (content + sticky bet panel) | event-detail, event-detail-bet | binary / multi | 10 | WF | - |
| Event head (thumb, category, question, big prob) | event-detail (+ bet variants) | binary / multi | 11 | WF | event |
| Bet panel (side, %, amount, payout, Confirm) | event-detail (+ bet variants) | intent / insufficient / reconcile / processing / on-chain error | 10-36 | WF | - |
| Bet dock (mobile sticky) | event-detail | collapsed -> expand to confirm | 8 | WF | - |
| Multi outcome list + "pick an outcome" | event-detail-multi | selected marked, Change link | 2 | WF | - |
| Price chart (schematic line) | event-detail (+ bet variants) | default | 11 | WF | - |
| Facts strip | event-detail | default | 9 | WF | - |
| Why-this-price arguments (YES col / NO col) | event-detail | default | 18 | WF | - |
| Resolution block | event-detail | default / resolved | 18 | WF | - |
| AMM Market depth panel (pool + price-by-size) | event-detail | collapsed / open | - | UV | - |
| Content tab strip (Comments / Biggest bets / Bets / Activity) | event-detail (+ bet variants) | per-tab active | 9-36 | WF | - |
| Comment (user, text, actions, badge, reply) | event-detail Comments tab | logged-in / logged-out (sign-in prompt) | 36 | WF | portrait |
| Comment composer | event-detail Comments tab | logged-in / logged-out | 7 | WF | - |
| Biggest bets (Holders) columns | event-detail Bets tab | binary / multi (outcome-tagged) | 16 | WF | - |
| Bets table (Positions, "you" highlight) | event-detail Bets tab | logged-in (your row) / logged-out | 9 | WF | - |
| Activity feed | event-detail Activity tab | default | 9 | WF | - |
| Segmented switcher (sort / chart range) | event-detail comments + chart | active segment | 9 | WF | - |

## 4. Forms, dialogs and inputs

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| Shared dialog shell (Sign In / Deposit) | every page (emitted in shell) | open / close (backdrop, Esc) | 104 | WF | - |
| Provider buttons (Google / X / Apple) | Sign In dialog + sign-in pages | rest / hover | 104 | WF/UV | - |
| Amount field + quick-amount chips | Deposit dialog + deposit pages | rest / selected / focus | 104 | WF | - |
| Field label | dialogs, forms | default | 104 | WF | - |
| Funds-protection line ("USDC held 1:1") | Deposit dialog, HIW, wallet | default | 104 | WF | - |
| Widget box (on-ramp placeholder) | Deposit dialog | default / load-failure | 104 | WF | - |
| Primary CTA (brass) - Confirm bet / Add funds | dialogs, states, HIW | rest / hover / focus | 104 | WF/UV | - |
| Bottom-sheet / modal overlay (grab, backdrop) | deposit, sign-in, win, loss | modal (desktop) / sheet (mobile) | 17 | WF | - |
| How-it-works dialog (hero + icon chips + FAQ) | every header page | open | 87 | WF/UV | - |
| Filter menu (Sort / Frequency) | feed, category | closed / open | 44 | WF | - |
| Reverse-order toggle switch | feed controls | on / off | 44 | WF | - |
| Inline error line | deposit, bet, sign-in, win | error | 8 | WF | - |
| Spinner box | deposit, bet, sign-in, win, loss | loading | 6 | WF | - |
| S5 reconcile box (price moved) | bet, win, loss | re-confirm / cancel | 6 | WF | - |

## 5. Feedback and states

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| State block (icon + title + message + action) | feed, category, detail, active-bets, notifications, wallet, profile, 404, 500, maintenance | empty / error | 38 | WF | - |
| Skeleton cards / lines | feed, category, detail, active-bets, notifications, wallet, profile | loading | 19 | WF | - |
| Empty list (notif-empty variant) | active-bets, favorites, notifications | empty | 3 | WF | - |
| Push-permission banner | event-feed-push, notifications-push | in-app banner | 2 | WF | - |
| Toast (message + close, stacked) | toasts (spec page) | info / success / error / undo | 4 | WF | - |
| Trust bar / trust cards | feed, footer (all) | default | 87 | WF/UV | art |

## 6. Profile and account

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| Identity row (avatar, name, handle) | my-profile, public-profile | own (Edit) / read-only | 2 | WF | portrait |
| Track record stats (bets, win rate, resolved) | my-profile, public-profile | default | 2 | WF | - |
| Share-card gallery | my-profile, public-profile | populated | 7 | WF | art / generated |
| Resolved-predictions history (WON / LOST) | my-profile, public-profile, active-bets-history | list / empty | 4+ | WF | - |
| Portfolio summary (Cash + In-play, Deposit) | my-profile, wallet | default | 3 | WF | - |
| CTA bar | how-it-works, my-profile, wallet | default | 3 | WF | - |
| Transaction list (deposits/payouts/fees/stakes) | wallet | list / loading / error | 3 | WF | - |

## 7. Footer

| Component | Screens / families | States | #f | Origin | Photo |
|---|---|---|---|---|---|
| Product footer (brand, markets, product, support, company, legal) | every footer screen | default | 87 | WF | - |
| Footer trust strip ("Built on trust" cards) | every footer screen | default | 87 | WF/UV | art |
| Social icon row | footer | rest / hover | 87 | WF | - |
| Popular / legal link lists | footer | default | 87 | WF | - |

---

## One-off (single block, NOT pulled into the kit)

- **Cookie-consent panel** (`cc-*`: category rows, accept / reject / manage) - `cookie-consent.html`
  only; a legal system page.
- **Withdraw `<details>` flow** (amount -> USDC address -> confirm) - `wallet.html` only; a
  page-local flow, not a reusable component.
- **404 / 500 / maintenance bodies** - each is a single system page composed from the shared
  **State block** (already a kit row); the wrapper copy is per-page.
- **Provider-conflict / not-found / minimum-not-met** notices - one-line, single-page guards built
  from the inline-error + state-block rows.
- **Sign-in "join the discussion" prompt** (`cmt-signin`) - the logged-out Comments variant; a
  content swap on the Comment composer row, not its own component.

## Photo needs (feeds Step 04, visuals)

- **event** - feed + category card thumbnails, Event Detail head thumb, featured-hero photo. One
  editorial event image per subject (politics / crypto / culture / general).
- **portrait** - profile avatar, comment avatars, the avatar-menu trigger. Neutral head-and-
  shoulders, one colorway.
- **art** - decorative gold trust art (column / source / globe) and the brand-tile columns; already
  shipped as `ui-visual/assets/trust-*.webp`. Regenerate only if the colorway drifts.

## Not a component

Width utilities (`w40`/`w60`/`w70`/`w80`/`w90`), grey-box scaffolding (`wf-*`, `.device` frame,
`page-label`, `zone-*`, `.side`) and the roadmap sidebar (`rm-*`, `sidebar*`) are layout/scaffold,
not product components, and are excluded from the kit.
