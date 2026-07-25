# UI Kit - Component Inventory

Read out of the whole product, not invented. Source: all `wireframes/*.html` (104 pages, every
screen and state) read together with `ia/docs/sitemap.md` and `wireframes/_conventions.md` (the
S1-S6 shared patterns), then re-read against the **shipped color layer** (`ui-visual/`, 76 pages +
`_theme.css` / `_theme-vault.css`). This table is the build-list for `ui-kit/kit.css` +
`ui-kit/kit.html`; the color language it is dressed in is root `DESIGN.md`.

**Deep pass (2026-07-23).** Re-audited after the whole product shipped in color (Stage 08). Two
things were added: a **Kit** column (is the component actually rendered as a live sample in
`ui-kit/kit.html`?) and the color-layer components that the wireframe-era inventory did not carry
(the featured hero band, the AMM market-depth panel, the graphic price chart, the redesigned
Profile, the Win/Loss overlays, the neutralized toast system). The Kit column is the source of the
Step-2 backlog at the bottom: the vitrine is a slice of the product, and this pass measures the gap.

## Inclusion rule

- A row is a component that recurs on **two or more pages** (measured as distinct files that carry
  the class). One-time blocks are listed under **One-off** at the end and are NOT pulled into the kit.
- Components concentrated in one screen family but spanning several of its pages/states (the Event
  Detail set, the shared dialog, the Win/Loss overlays) ARE kit components: the kit must render them
  identically across those pages.
- **Origin** column: `WF` = present in the grey wireframes (structure owned by `wireframes/`);
  `UV` = added only in the color layer (`ui-visual/_theme.css` / `_theme-vault.css`, not in the grey
  wireframes) and so documented from the painted screens + `DESIGN.md`. Both belong in the kit.
- **Photo** column: `-` none, `event` real event/news image, `portrait` a person, `art` decorative
  brand/trust art (shipped as webp/jpg in `ui-visual/assets/`). Feeds Step 04 (visuals).
- **Kit** column: `+` a live sample renders in `ui-kit/kit.html`; `~` a base/related sample renders
  but this variant or state is not shown; `-` no sample yet (a Step-2 gap).

`#f` = number of distinct wireframe files the component appears on (UV rows have no WF count).

---

## 1. Navigation and chrome

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| App header (lean) | all header screens (feed, category, detail, active-bets, notifications, wallet, profile, how-it-works) | logged-in / logged-out; rest / `.scrolled` (condensed) | 87 | WF | - | + |
| Logo (Events home) | every header screen | default | 87 | WF | - | + |
| Balance / Portfolio-Cash swap | logged-in header | swap Portfolio <-> Cash; "+" opens Deposit | 53 | WF | - | + |
| Notifications bell + mini-dropdown | logged-in header | populated / empty / badge on-off | 53 | WF | - | + |
| Avatar menu (dropdown) | logged-in header | closed / open | 53 | WF | portrait | + |
| How-it-works button | header (next to logo) | default; opens HIW dialog (dialog itself = group 4) | 87 | WF | - | + |
| Icon button (ghost) | header utility, event actions | rest / hover / focus | 87 | WF | - | + |
| Auth entries (Log in / Sign up) | logged-out header + gate | default; open Sign In dialog | 34 | WF | - | + |
| Category nav band | feed + category pages | per-category active; `.cat-condensed` strip on scroll | 57 | WF/UV | - | + |
| Sub-category rail (`.subcat`) | category pages (politics/crypto/culture/general) | active row + sample count | 32 | WF | - | + |
| Trending sub-filter chips (`.feed-subfilter`) | Trending feed | active | 5 | UV | - | + |
| Bottom nav (mobile, 4 slots) | all header screens | per-slot current; logged-out (Sign in slot) | 87 | WF | - | + |
| Active / History tabs (`.tabs`) | My Bets (active-bets, history) | active tab | 9 | WF | - | + |
| Footer language menu | every footer screen | closed / open (TBD) | 87 | WF | - | + |
| Screen-tree drawer / roadmap sidebar | every page (course chrome) | - | 104 | WF | - | n/a (course chrome, not product) |

## 2. Browse: feed and cards

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| Two-stone plate / surface system (`.cat-layout`, `.feed-inner` inset plates, notched brass frames, groove edges, trust-column watermark `card::after`) | every color page (the substrate) | - | - | UV | art | + |
| Event card, binary (treatment B) | feed, category, favorites, event-feed-push | rest / hover | 36 | WF | event | + |
| Event card, multi (treatment D) | feed, category, event-detail, favorites | rest; 2 leading options | 20 | WF | event | + |
| Odds bar (thin, green YES on red track) | feed / category / detail cards | injected from prob | - | UV | - | + |
| Tinted YES / NO buttons | every event card + bet panel | rest / hover / compact | 14 | WF | - | + |
| Probability figure | cards, detail | value | 21 | WF | - | + |
| Card meta row (Volume / Closes + bookmark) | every event card | bookmarked on / off | 23 | WF | - | + |
| Responsive card grid | feed, category, favorites | populated / skeleton | 23 | WF | - | + |
| Featured hero band (`.feed-hero`) | Trending feed | default | - | UV | event, art | + |
| - featured market (`.hero-feature` + `.hf-chart` SVG area/volume graph) | Trending feed | default | - | UV | event | + |
| - hero trust cards (`.hero-trust`, gold art bleed) | Trending feed | default | - | UV | art | + |
| - brand tile (`.hero-promo.brand-tile`, notched frame) | Trending feed | default | - | UV | art | + |
| - hot-right-now ranked list (`.hero-hot`) | Trending feed | default | - | UV | - | + |
| Feed SEO plate (below fold, `.feed-seo-wrap` brand statement) | feed + category pages | default | 14 | WF/UV | art | + |
| Related events plate (`.related-events`) | event-detail | list | 9 | WF | event | + |
| Load-more control | feed, category | rest / hover | 20+ | WF/UV | - | + |

## 3. Event Detail

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| Two-plate layout (`.ed-layout`: content + sticky bet panel) | event-detail, event-detail-bet | binary / multi | 10 | WF | - | + |
| Event head (`.ed-head`: thumb, category, question, big prob, thin `.ed-oddsbar`, actions) | event-detail (+ bet variants) | binary / multi | 11 | WF | event | + |
| Bet panel (`.bet-panel`: `.bp-dir` filled-selected side, amount, quick chips, payout line, Confirm) | event-detail (+ bet variants) | intent / insufficient / reconcile / processing / error / resolved | 10-36 | WF | - | + |
| Bet dock (mobile sticky, `.bet-dock`) | event-detail | collapsed -> expand to confirm | 8 | WF | - | + |
| Multi outcome list (`.opt-list` + "pick an outcome") | event-detail-multi | selected marked (`.sel`), Change link | 2 | WF | - | + |
| Price chart (`.ed-chart` SVG plot + y/x axis + `.ed-range` switcher; multi adds `.ml-line` legend) | event-detail (+ bet variants) | binary / multi / range | 11 | WF/UV | - | + |
| Facts strip (`.ed-facts`) | event-detail | default | 9 | WF | - | + |
| Why-this-price arguments (`.args`: YES col / NO col) | event-detail | default | 18 | WF | - | + |
| Resolution block (`.resolution`, `.ed-rules` tabs) | event-detail | default / resolved | 18 | WF | - | + |
| AMM market panel (`.market-box` collapsible + `.market-depth` "price by bet size" table) | event-detail | collapsed / open | - | UV | - | + |
| Content tab strip (Comments / Biggest bets / Bets / Activity, CSS radio) | event-detail (+ bet variants) | per-tab active | 9-36 | WF | - | + |
| Comment (`.cmt`: user, text, actions, badge, reply) | event-detail Comments tab | logged-in / logged-out (`.cmt-signin` prompt) | 36 | WF | portrait | + |
| Comment composer (`.cmt-compose`) | event-detail Comments tab | logged-in / logged-out | 7 | WF | - | + |
| Biggest bets columns (`.hold-col` / `.hold-row`) | event-detail Bets tab | binary / multi (outcome-tagged) | 16 | WF | - | + |
| Bets table (`.ptable`, "you" highlight) | event-detail Bets tab | logged-in (your row) / logged-out | 9 | WF | - | + |
| Activity feed (`.act-row`) | event-detail Activity tab | default | 9 | WF | - | + |
| Segmented switcher (`.seg` / `.rules-tabs` / `.ed-range`) | event-detail comments + rules + chart | active segment | 9 | WF | - | + |
| Bet sub-state boxes (`.protect` / `.inline-error` / `.reconcile-box` / `.spinner-box`) | bet panel + dock inline | funds-safe / insufficient / reconcile / processing | 10+ | WF/UV | - | + |

## 4. Forms, dialogs and inputs

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| Shared dialog shell (`dialog.app-dialog`, stone-plate material) | every page (emitted in shell) | open / close (backdrop, Esc); modal (desktop) / sheet (mobile) | 104 | WF/UV | - | ~ |
| Provider buttons (Google / X / Apple, real brand marks) | Sign In dialog + sign-in pages | rest / hover | 104 | WF/UV | - | + |
| Amount field + quick-amount chips | Deposit dialog + deposit pages | rest / selected / focus | 104 | WF | - | + |
| Field label | dialogs, forms | default | 104 | WF | - | + |
| Funds-protection line (`.protect`, "USDC held 1:1") | Deposit dialog, HIW, wallet, bet panel | default | 104 | WF | - | + |
| Widget box (`.widget-box` on-ramp placeholder) | Deposit dialog | default / load-failure | 104 | WF | - | + |
| Primary CTA (brass) - Confirm bet / Add funds | dialogs, states, HIW | rest / hover / focus | 104 | WF/UV | - | + |
| Bottom-sheet / modal overlay (grab, backdrop) | deposit, sign-in, win, loss | modal (desktop) / sheet (mobile) | 17 | WF | - | ~ |
| Sign-in dialog (`.signin-dialog`) | sign-in family | default / error / loading / provider-conflict | 4 | WF/UV | - | ~ |
| How-it-works dialog (`.hiw-dialog`: hero + icon chips + FAQ) | every header page | open | 87 | WF/UV | art | + |
| Filter menu (Sort / Frequency) | feed, category | closed / open | 44 | WF | - | + |
| Reverse-order toggle switch | feed controls | on / off | 44 | WF | - | + |
| Inline error line (`.inline-error`, neutral stone) | deposit, bet, sign-in, win | error | 8 | WF | - | + |
| Spinner box (`.spinner-box`) | deposit, bet, sign-in, win, loss | loading | 6 | WF | - | + |
| S5 reconcile box (`.reconcile-box`, price moved) | bet, win, loss | re-confirm / cancel | 6 | WF | - | + |

## 5. Feedback and states

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| State block (`.state-block`: icon + title + message + action) | feed, category, detail, active-bets, notifications, wallet, profile, 404, 500, maintenance | empty / error | 38 | WF | - | + |
| Skeleton cards / lines (`.card.skeleton` / `.pos.skeleton` shimmer) | feed, category, detail, active-bets, notifications, wallet, profile | loading | 19 | WF/UV | - | ~ |
| Empty list (`.pos-list` empty variant) | active-bets, favorites, notifications | empty | 3 | WF | - | + |
| Push-permission banner (`.push-banner`) | event-feed-push, notifications-push | in-app banner | 2 | WF | - | + |
| Toast (`.toast`: message + close, stacked) | toasts (spec page) | info / success (brass tick) / error (neutralized, no red) / undo | 4 | WF/UV | - | + |
| Win overlay (`dialog.outcome-dialog.win-dialog` + auto Share Card + F5 friction) | win family | win / loading / payout-pending / error | 4 | WF/UV | art | + |
| Loss overlay (`dialog.outcome-dialog.loss-dialog`, neutral, no celebration) | loss family | loss / loading | 2 | WF/UV | - | + |
| Share Card (auto-generated win visual, reused in profile gallery) | win overlay, my/public profile | populated | 5+ | UV | art / generated | + |
| Trust bar / trust cards (`.footer-trust`) | feed, footer (all) | default | 87 | WF/UV | art | + |

## 6. Profile and account (REDESIGNED in color - the whole cluster)

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| Identity row (`.idrow`: ringed 72px avatar `.av`, name, handle, Edit pill) | my-profile, public-profile | own (Edit) / read-only | 2 | WF/UV | portrait | + |
| Section divider (`p.pos-status`, brass tick) | my-profile, public-profile | default | 2 | UV | - | + |
| Reputation stat-grid (Track record: tiles, brass win-rate hero tile) | my-profile, public-profile | default | 2 | WF/UV | - | + |
| Profile tabs (`.ptabs` CSS-only radio: Track record / Past wins / Resolved) | my-profile, public-profile | per-tab active, focus ring | 2 | WF/UV | - | + |
| Share-card gallery (`.gallery` horizontal rail of win cards) | my-profile, public-profile | populated | 7 | WF/UV | art / generated | + |
| Resolved-predictions history (`.pos-side.pos-won` green / `.pos-lost` red) | my-profile, public-profile, active-bets-history | list / empty | 4+ | WF/UV | - | + |
| Portfolio summary (`.pos` 3-figure grid: total / cash / in-play + inline CTA) | my-profile, wallet | default | 3 | WF/UV | - | + |
| CTA bar (`.cta-bar`: Add funds + Open Wallet / Withdraw) | how-it-works, my-profile, wallet | default | 3 | WF | - | + |
| Position row (`.pos`: question, figures, status) | active-bets, notifications, wallet, profile | active / resolved / skeleton | 9+ | WF/UV | - | ~ |
| Transaction list (deposits/payouts/fees/stakes) | wallet | list / loading / error | 3 | WF | - | + |

## 7. Footer

| Component | Screens / families | States | #f | Origin | Photo | Kit |
|---|---|---|---|---|---|---|
| Product footer (brand, markets, product, support, company, legal) | every footer screen | default | 87 | WF | - | + |
| Footer trust strip ("Built on trust" cards, gold art bleed) | every footer screen | default | 87 | WF/UV | art | + |
| Social icon row (`.social-row`) | footer | rest / hover | 87 | WF | - | + |
| Popular / legal link lists (`.footer-popular`, `.footer-legal`) | footer | default | 87 | WF | - | + |

---

## One-off (single block, NOT pulled into the kit)

- **Cookie-consent panel** (`.cc-*`: category rows, accept / reject / manage) - `cookie-consent.html`
  only; a legal system page.
- **Withdraw `<details>` flow** (`.wd-flow`: amount -> USDC address -> confirm) - `wallet.html` only;
  a page-local flow, not a reusable component.
- **404 / 500 / maintenance bodies** - each is a single system page composed from the shared **State
  block** (already a kit row) + `.sys-links` quick links; the wrapper copy is per-page.
- **Provider-conflict / not-found / minimum-not-met** notices - one-line, single-page guards built
  from the inline-error + state-block rows.

## Photo needs (feeds Step 04, visuals)

- **event** - feed + category card thumbnails, Event Detail head thumb, featured-hero photo. One
  editorial event image per subject (politics / crypto / culture / general); shipped as
  `event-*.jpg` + `hero-capitol.webp`.
- **portrait** - profile avatar, comment avatars, the avatar-menu trigger. Neutral head-and-
  shoulders, one colorway; shipped as `avatar-1.jpg` / `avatar-2.jpg`.
- **art** - decorative gold trust art (column / source / globe), the brand-tile columns, the
  auto-generated Share Card; shipped as `trust-*.webp` + `brand-columns.webp`. Regenerate only if the
  colorway drifts.

## Not a component

Width utilities (`w40`/`w60`/`w70`/`w80`/`w90`), grey-box scaffolding (`wf-*`, `.device` frame,
`page-label`, `zone-*`, `.side`) and the roadmap sidebar (`rm-*`, `sidebar*`) are layout/scaffold,
not product components, and are excluded from the kit.

---

## Kit coverage and the Step-2 backlog

The vitrine (`ui-kit/kit.html`, 9 sections) renders the feed-and-dialog core well but is a **slice**
of the shipped product: whole screen families (Profile/account, Win/Loss, the deep Event Detail
tabs) never made it into the kit because the kit was built at the Event-Feed stage and the rest
shipped straight into `ui-visual/`. The `+ / ~ / -` column above is the gap. Grouped by build
priority for Step 2 (add the `-` and finish the `~`, each new sample sourced from the already
shipped `ui-visual/` page, values through `kit.css` variables, markup into `kit.html`):

1. **Profile / account cluster (group 6)** - DONE (2026-07-23). Added a `#profile` vitrine section:
   identity row, portfolio summary, the CSS-only Track record / Past wins / Resolved tabs (the tab
   mechanism is pulled into `kit.css` as section 2b, unique to my-profile), the reputation stat-grid
   with the brass win-rate hero, the share-card gallery, the `.pos-won`/`.pos-lost` WON/LOST resolved
   rows. The wallet transaction list was later added to the same section (priority 7 pass). The
   position row stays `~` (resolved rows shown, active/skeleton states not).
2. **Event Detail depth (group 3)** - DONE (2026-07-23). Expanded the `#detail` vitrine section with
   standalone specimens: the graphic price chart + range switcher (polyline hardcoded, the page's JS
   is not in the kit), facts strip, AMM market-depth panel, the Comments / Biggest bets / Bets /
   Activity content tabs (CSS-radio mechanism already in kit.css via the event-detail slice), the
   bet-panel states (funds line / insufficient / price-moved reconcile / processing), the mobile bet
   dock, and the multi-outcome selector + bet-panel summary. All CSS was already in kit.css; only
   markup was added. Not shown (state variants, not missing components): logged-out `.cmt-signin`,
   the resolved bet panel, the multi chart `.ml-line` legend.
3. **Feedback (group 5)** - DONE (2026-07-23). Added a `#feedback` vitrine section (data-n 08, after
   Shared dialogs): the toast set with the neutralized-error variant (success = brass tick, error =
   neutral stone, no red), the slim near-action trust bar, and the invoked Win overlay (green figure
   + auto Share Card + the "Before the next one" F5 friction) and Loss overlay (red figure, no
   celebration, next step is not "bet again"), rendered inline with `open`. The empty-list variant
   was later added to the States section (priority 7 pass); skeleton stays `~` (card skeleton shown,
   `.pos` skeleton not).
4. **Forms (group 4)** - DONE (2026-07-23). The inline error line, spinner box and S5 reconcile box
   came in with the Event Detail bet states (priority 2); the How-it-works dialog (brass hero + icon
   chips + FAQ) was added to the Shared dialogs section, shown inline with `open`. Still `~`: the
   sign-in state set and a distinct bottom-sheet/backdrop specimen (the shell already ships as both).
5. **Browse (group 2)** - DONE (2026-07-23). Expanded section 05 (renamed "Feed and cards") with the
   featured hero band (featured market + hardcoded `.hf-chart` area/volume graph, hero trust cards,
   brand tile, hot-right-now list), the trending sub-filter (wrapped in `.cat-main` so the
   `.cat-main .feed-subfilter` skin applies), the sub-category rail (rendered, since the shipped rail
   is JS-populated), and the below-fold SEO brand plate. All CSS already in kit.css; markup only.
   Remaining `-`: the two-stone surface/plate system as an explicit foundation panel (priority 7).
6. **Chrome / footer (groups 1, 7)** - DONE (2026-07-23). Expanded the Chrome section with the
   logged-out header (Sign in surface pill + Sign up brass gradient, in place of the balance and
   avatar), the My Bets Active / History tabs, and the full product footer (trust strip + brand +
   social row + language menu + the four link columns + popular links + legal), replacing the old
   trust-strip-only footer specimen. The `.tbd` and `.placeholder-line` chips stay hidden by the
   Vault theme, as they ship.
7. **Foundations** - DONE (2026-07-23). Added a **surface ramp** to the color section (page ->
   graphite -> content plate -> card -> surface, nested to show the embossed two-stone depth) and an
   **outcome-semantics** row (tinted YES/NO, the filled bet side, the `.pos-won`/`.pos-lost` WON/LOST
   chips) so the green/red-is-outcome-only rule is documented in one place.
