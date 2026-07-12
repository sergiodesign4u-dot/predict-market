# Wireframes - Critique pass (Krok 9)

Rigorous defect audit of all `wireframes/*.html` (96 pages) against
`_conventions.md`, `ia/docs/sitemap.md`, and `ia/docs/flows.md`. Method: mechanical greps
(appearance, placeholders, palette, off-map), a state-coverage cross-check against
`_screens.md` / sitemap state lists, and a dead-end / zone-without-action check.
Done 2026-06-28, after the Krok 7 flow-linking and Krok 8 reconciliation passes
(so the set entered this pass already clean on most axes).

## Defect table (screen -> what's wrong -> how to fix)

| # | Screen(s) | Category | What was wrong | Fix | Priority | Status |
|---|---|---|---|---|---|---|
| 1 | `politics/crypto/culture/general-empty` + their `-logged-out` (8 pages) | Dead end (state without working exit) | The empty-state CTAs "Clear filters" and "Notify me of new X events" were bare `<button>`s - the state's own action zone did not navigate (only the global header / bottom nav offered a way out) | Wrapped "Clear filters" in `<a href>` to the cleared (unfiltered) category view, auth-aware (`politics.html` for logged-in, `politics-logged-out.html` for logged-out). "Notify me" stays a button (T6 subscribe is an in-place action, by decision). Fixed in `gen_category.py` (threaded `clear_href` through `build -> main_for -> grid_for`), regenerated | HIGH (dead-ends first) | FIXED |
| 2 | All pages (global footer) | Zone with non-functional links (optional) | Footer columns use `href="#"` even where a built target exists (How It Works, Wallet, My Bets, categories) | By decision, left as-is: the footer is a global element intentionally carrying placeholder / TBD links (with visible TBD markers). Not a defect under the conventions | LOW (optional) | NOT CHANGED (by decision) |

## Clean - no defects found (per category)

- **Leaked appearance**: none. No color, no font-family overrides, no box/text
  shadows, no emoji / pictographs. The whole palette is greyscale (`#111` .. `#fff`,
  near-greys like `#9a9a9a` / `#bdbdbd`); the only `rgba()` is a black overlay dim
  (`rgba(0,0,0,.35/.4)`) for dialogs / sheets. Icons are monochrome outline SVG only.
- **Placeholders / lorem**: none. No "lorem", "ipsum", "Heading N", "TODO", etc.
  Every "placeholder" string is an intentional grey-box element label (thumbnail
  placeholder, logo placeholder, tagline placeholder, image placeholder) - allowed
  by the conventions, not lorem-as-content. Real domain text throughout (event
  questions, USDC, $ amounts, track records, transaction types).
- **Missing states**: none. Every state in `_screens.md` / the sitemap state lists
  is built. Deferred states are intentional per sitemap (Wallet balance-syncing,
  My Profile empty-state) - not defects.
- **Off-map screens**: none. All 96 pages map to a sitemap screen / state. Orphans
  `[SIROTA]` (Settings, Leaderboard, Help / FAQ) are correctly unbuilt; the
  standalone Bet Screen is dissolved into the Event Detail panel.

## Health after the pass

- 0 em-dash across all pages.
- 0 broken internal links across all pages.
- Zones / naming / navigation consistent (carried from the Krok 8 reconciliation).

Net: one real defect (a dead-end in 8 category empty-states), fixed; one optional
footer item left by decision. The wireframe set is clickable end to end with no
dead-ends in any built state.

## Follow-up fix pass (2026-06-28, user review)

A later visual review surfaced three more defects, all in the shared chrome:

| # | Screen(s) | Category | What was wrong | Fix | Status |
|---|---|---|---|---|---|
| 3 | 9 event-feed family pages (`event-feed*.html`) | Leaked / broken appearance | The sign-in / deposit `<dialog>` markup + JS were injected on these hand-authored pages, but the dialog CSS rules were not, so the dialog opened as an unstyled broken box | Inject a self-contained dialog CSS block (`dialog.app-dialog` scoped) before `</style>` (idempotent, `fixpack.py`) | FIXED |
| 4 | All logged-in pages (header) | Dead controls | The Favorites heart, Notifications bell, and the 5 avatar-dropdown items were bare `<button>`s with no navigation | Wired: heart -> `favorites.html`, bell -> `notifications.html`, avatar -> my-profile / active-bets / wallet / how-it-works / event-feed-logged-out (Logout) | FIXED |
| 5 | All pages (bottom nav) | Dead controls | The mobile bottom-nav slots (Events / My Bets / Favorites / Portfolio, and logged-out Events) were bare `<button>`s | Wired per auth: logged-in -> feed / active-bets / favorites / my-profile; logged-out Events -> logged-out feed, My Bets + Favorites -> sign-in dialog | FIXED |

New screen built to remove the Favorites dead-end: **Favorites view** (`favorites.html` +
`favorites-empty.html` + `favorites-loading.html`) - the logged-in "filter over the feed"
the IA always described, now a real destination with empty / loading states. Added
to the screen tree (`_shell.nav_tree`). Total pages: 96 -> 99.

Health after this pass: 0 em-dash, 0 broken internal links, 0 dead bottom-nav /
header controls across all 99 pages. Wiring applied by the idempotent post-processor
`fixpack.py` (header + bottom nav + dialog CSS) and `gen_favorites.py`.

## Re-critique pass (2026-06-29, fresh multi-agent audit)

A second full critique, this time fanned out across five parallel auditors (one per
screen family: Event Feed + Favorites, Category pages, Event Detail, Bet-flow +
dialogs, Account + utility). Each checked the same six categories - style leak,
placeholder, missing state, dead-end, zone-without-action, off-map - against
`_conventions.md`, `_screens.md`, `ia/docs/sitemap.md`, `ia/docs/flows.md`.

Result: the set held up. Across all 99 pages exactly one genuine (minor, clarity)
defect, plus one false positive that was verified and dismissed.

| # | Screen | Category | What was wrong | Fix | Verdict |
|---|---|---|---|---|---|
| 6 | `event-detail-resolved.html` | Clarity (not a dead-end) | The resolved-while-reading body reused the live binary detail verbatim, so the meta line and chart caption framed the odds as live ("YES 38% now") on a market that had already closed. The top state-block already said betting was closed and the bet panel / dock were correctly omitted, so this was a wording mismatch, not a trap. | In `gen_event_detail.py` `main_resolved()`, post-process the reused body: meta line gains " &middot; Trading closed" and the chart caption reads "YES 38% at close" instead of "now". The live `event-detail.html` is untouched (the swap is local to the resolved builder). Regenerated + idempotent pipeline re-run. | FIXED |
| - | `event-detail-logged-out-error.html` | Missing state (claimed) | An auditor reported the logged-out Event Detail error variant as missing. | Verified false: the file exists (state-block + "Try again" -> logged-out detail + "Back to feed"). No action. | FALSE POSITIVE |

Clean families (no defects): Event Feed + Favorites (12), Category pages (32),
Bet-flow + dialogs (26), Account + utility (16), and the rest of Event Detail (the
tab strip is outcome-aware on multi, the multi bet panel focuses the selected
outcome with a "Change" anchor, and all bet sub-states are present).

Health after this pass: 0 em-dash, 0 broken internal links across all 99 pages; one
clarity fix applied via the generator (not hand-edited).

## Flow-wiring audit (2026-07-07, step 7 - user path)

Full audit of the clickable user path against `ia/docs/flows.md`: every screen's
primary action must be a real `<a href>` to the next screen, state transitions
(loading -> success, error -> try again, empty -> filled) must be wired, branches
must go both ways, and no dead-ends - only routes drawn in `flows.md`. Method: a
chrome-stripped parser (drops the left screen-tree, header, footer, state-switch)
extracting the actionable controls inside `<main>` + the `wf-overlay` invoked
screens + the shared `<dialog>`s, cross-referenced edge-by-edge to the four flows
(MJ, FJ2, FJ5+EJ3, SJ1).

Result: the main chain held up end to end - EF -> ED (card body / YES / NO)
-> bet panel (intent) -> Confirm gate fires the **Sign In dialog** -> **Deposit
dialog** -> "Add funds" -> **S5 reconcile** -> execute (`bet-processing`)
-> "View your bet" -> **Active Bets**. Branch edges verified both ways: ED error
`Try again` <-> `Back to feed`; bet on-chain error (T3) `Try again` (execute) +
`Check wallet` (-> Wallet); S5 reconcile `Confirm at new price` (execute) +
`Cancel and re-evaluate` (-> ED); insufficient-balance `Add funds` (deposit
dialog). Deposit success -> reconcile; KYC error (T1) `Browse events` -> feed;
`How it works` -> How It Works page and back. Sign In providers -> Deposit dialog
(the SI -> DEP chain). Loss `Back to your bets` (-> Active Bets) + `Browse events`
(-> feed), no "bet again". Win close -> Active Bets, `Browse events` -> feed.
Notifications route to `win.html` / `loss.html` / `event-detail.html` (G1 fast
paths). My Bets History and the Active-tab resolved rows -> Win / Loss.

Two genuine gaps found and fixed (naked buttons where `flows.md` requires an edge;
each matched to the pattern its sibling screens already used):

| # | Screen(s) | Element | Was | Became | Flow edge |
|---|---|---|---|---|---|
| 1 | `event-feed-error`, `event-feed-logged-out-error`, and all 8 Category error pages (`{politics,crypto,culture,general}-error` + `-logged-out-error`) | `Try again` | bare `<button>` (dead) | wrapped in `<a href="{success}.html">` -> the page's own success state | error -> retry -> loaded (T8-style recovery). Every *other* error screen (Event Detail, My Bets, Wallet, My/Public Profile, Notifications) already linked `Try again`; the feed + category errors were the only ones left naked. |
| 2 | `deposit-error-card` | `Try another card` | bare `<button>` (dead) | wrapped in `<a href="deposit.html">` -> the Deposit form | MJ T2: card declined -> "try another card" -> back to **DEP**. |

Deliberately NOT changed (verified non-navigational actions, not dead-ends - each
screen has other real exits): `Share` / `Share as text` (OS share sheet, SJ1
"shares yes" leaves the app), `Enable notifications` / `Open system settings` /
`Not now` (OS permission prompts), `Clear filters` / `Notify me of new ... events`
(in-page filter / subscribe, and the empty pages also carry `Browse events` ->
feed), `Open Transak directly` (external), `Confirm withdrawal` (Wallet withdrawal
is P3-6 deferred, not a built flow), `Add funds` on `deposit-minimum-not-met` (the
validation-blocked confirm), and `Connect a USDC wallet ...` on the deposit errors
(the Crypto-Native wallet-connect surface is abstracted - kept naked on purpose,
consistent across both deposit error pages). Footer/dialog `Terms` / `Privacy`
stay `href="#"` grey-box placeholders.

Also confirmed as intentional (not a gap): resolved bets are reached through the
My Bets **History tab** (which links each row to Win / Loss), not from a
"recently-resolved" block on the Active tab - this matches the existing
`active-bets-empty-resolved` copy "See resolved bets (History tab)". The FJ5
"finds the resolved item -> Loss Screen" intent is satisfied via History.

Health after this pass: 0 em-dash, 0 broken internal links across all 99 pages;
11 files edited (10 `Try again` + 1 `Try another card`), link wrappers only - no
copy, structure, or chrome changed.

## Coverage audit (2026-07-07, step 8 - roll out to the whole product)

The main flow was wired in step 7; step 8 verifies the roll-out is complete -
every screen and every state in `ia/docs/sitemap.md` "## Screens" has a wireframe, with
nothing left orphaned. For our project this is a **coverage verification**, not new
construction: the wireframe build already produced the full set (99 pages), so
fanning out builder agents would rebuild what exists. Method: extract the canonical
screen + state inventory from `sitemap.md`, diff it against the files on disk.

Result: full coverage, 99/99, zero gaps.

| Sitemap screen | States required (sitemap) | Wireframes | ✓ |
|---|---|---|---|
| Event Feed (× auth) | loading, empty, error, push-permission-missing (logged-in only) | `event-feed{,-empty,-error,-loading,-push-permission-missing}` + `-logged-out{,-empty,-error,-loading}` (9) | ✓ |
| Category page ×4 (× auth) | success, empty, error, loading | `{politics,crypto,culture,general}{,-empty,-error,-loading,-logged-out,-logged-out-empty,-logged-out-error,-logged-out-loading}` (32) | ✓ |
| Event Detail (× auth) | loading, error, resolved-while-reading, pre-selected entry; views binary/multi; bet-panel intent/insufficient/reconcile/processing/on-chain-error | `event-detail{,-multi,-resolved,-loading,-error,-bet-processing,-bet-reconcile,-bet-insufficient,-bet-error}` + `-logged-out{,-multi,-error,-loading}` (13) | ✓ |
| Favorites view | (feed chrome) empty, loading | `favorites{,-empty,-loading}` (3) | ✓ |
| Sign In / Register | in-progress, error, error-provider-conflict | `sign-in{,-loading,-error,-provider-conflict}` (4) | ✓ |
| Deposit | in-progress, error-card, error-KYC, widget-load-failure, pending, minimum-not-met | `deposit{,-loading,-error-card,-error-kyc,-widget-load-failure,-pending,-minimum-not-met}` (7) | ✓ |
| Win Screen | loading, error, payout-pending | `win{,-loading,-error,-payout-pending}` (4) | ✓ |
| Loss Screen | loading | `loss{,-loading}` (2) | ✓ |
| Active Bets + Bet History (History tab) | AB: loading, empty-new, empty-resolved, error; History: loading, empty, error | `active-bets{,-empty-new,-empty-resolved,-error,-loading,-history,-history-empty,-history-error,-history-loading}` (9) | ✓ |
| Notifications | loading, empty, error, push-permission-missing | `notifications{,-empty,-error,-loading,-push}` (5) | ✓ |
| Wallet | loading, error | `wallet{,-error,-loading}` (3) | ✓ |
| My Profile | loading, error | `my-profile{,-error,-loading}` (3) | ✓ |
| Public Profile | loading, error, not-found | `public-profile{,-error,-loading,-not-found}` (4) | ✓ |
| How It Works | (single state) | `how-it-works` (1) | ✓ |

**Correctly absent (sitemap says "do not build" - not gaps, per "don't invent states not in the table"):**
- **Bet Screen** - dissolved into the Event Detail bet panel (build pass #3); its states live as Event Detail bet-panel states.
- **Pre-selected entry variant** (Event Detail) - a variant of the bet-panel *intent* state (panel opens with the side pre-selected), not a separate page. Folded into intent, as designed.
- **Orphans `[SIROTA]`** - Settings / Notification Preferences, Leaderboard, Help/FAQ: no confirmed job maps to them; sitemap says "do not build until a job is confirmed".
- **Deferred cosmetic states** - Wallet `balance-syncing` and My Profile `empty-state`: sitemap marks both "deferred to wireframe spec". The Wallet withdrawal is a flow inside Wallet (states pending/confirmed/failed), not a separate screen.

Consistency after this pass: the set is unchanged since the 2026-06-29 re-critique
except the step-6 microcopy edits (text) and the step-7 flow-wiring edits (link
wrappers on 11 files); both were re-verified at 0 em-dash / 0 broken internal links
across all 99 pages. No screen is orphaned; nothing new invented.

## Final defect pass (2026-07-07, step 9 - check and finalize)

The closing sweep across all six defect categories - style leak, placeholders,
missing states, dead-ends, zone-without-action, off-map - run after the step-6
microcopy rewrite (text) and the step-7 flow-wiring edits (link wrappers), to catch
any regression before finalizing. Method: mechanical greps over all 99 pages plus
the step-7/8 audit tooling re-run.

Result: no new defects; the set is clean in every category. Dead-ends and missing
states (the priority categories) were already closed in steps 7 and 8 and re-verify
clean here.

| Category | Check | Verdict |
|---|---|---|
| Style leak | non-grey hex colors (R!=G!=B), gradients, colored shadows, emoji | **clean** - 0 non-grey colors, 0 gradients, 0 emoji; the only `box-shadow` is `inset 0 -2px 0 #777` (a grey 2px underline affordance, no blur/elevation, palette-compliant) |
| Placeholders / leaked codes | internal codes (T1/T2/T3/S5), spec-notes, dev jargon, TODO/lorem | **clean** - the only remaining `(T11)` is inside `<nav class="state-switch">` ("Card failed (T11)"), the wireframe state-switcher tooling, not product copy. The `*placeholder` / `licensing line` / `Tagline` / `Sample wireframe content` strings are the intentional honest grey-box stand-ins kept by design (footer + card thumbnails + win share-card image) |
| Missing states | sitemap state list vs files on disk | **clean** - 99/99 coverage confirmed in the step-8 coverage audit; deliberate exclusions (Bet Screen dissolved, `[SIROTA]` orphans, deferred cosmetic states) are correct |
| Dead-ends | broken internal links; naked flow-edge buttons | **clean** - 0 broken internal links; 0 naked `Try again` / `Try another card` (fixed in step 7) |
| Zone without action | interactive-looking zones with no handler | **clean** - actionable zones wired (step-7 flow audit); the only action-free zones are the intentional grey-box placeholders |
| Off-map | files not mapping to a `sitemap.md` screen | **clean** - all 99 files map to a sitemap screen family; no orphan pages (`[SIROTA]` screens correctly unbuilt) |

Health: 0 em-dash, 0 broken internal links, 0 style leaks, 0 leaked codes across
all 99 pages. The wireframe set is final. No files changed in this pass (verification
only).

## Status-line removal (2026-07-07)

Removed the `.page-label` meta bar from the top of every wireframe - the tooling
caption reading `Wireframe: {screen} | {auth} - state: {state} | responsive
(mobile-first) | file: wireframes/{file}.html`. It was scaffolding, not part of the
screen, and cluttered the top of the page. Deleted the `<div class="page-label">`
block from all 99 pages (the now-unused `.page-label` CSS rule is left in place,
harmless).

Because that bar had `padding-left: 104px` that housed the fixed "Screens"
drawer-toggle, removing it let the toggle overlap the first `.state-switch` chip at
widths below 1440px (where the toggle floats; at >=1440px the screen-tree is a
permanent sidebar and the toggle is hidden, so the desktop view was already clean).
Fix: `body { padding-top: 44px }` at narrow widths, reset to `0` in the
`@media (min-width:1440px)` block - a clean top strip for the floating toggle.
Verified clean at 1280px and 1600px. The `.state-switch` state navigator is kept.

**Follow-up: state-switch removed too (same day).** The top `.state-switch`
navigator (the `Auth: Logged in / Logged out` and `State: Success / Empty / Error /
...` chip rows) was also removed from all 99 pages - it duplicated the left
screen-tree, which already lists every screen family with its auth variants and
states. Removing both bars leaves a clean top: just the floating "Screens"
drawer-toggle (in its 44px strip), then the product screen. All state / auth
navigation stays reachable via the screen-tree drawer. The `.state-switch` CSS is
left in place (unused, harmless). 0 broken links, 0 em-dash.

---

## Stage-04 reconcile (2026-07-12) - wireframes vs the new IA Detailed layer + CJM

The 99 wireframes predate the IA Detailed layer (03b) and the CJM, so course Stage 04 was run
as a targeted reconcile (audit first, then fix the real gaps), not a rebuild. A subagent audit
compared the set against the new IA nodes (`ia/docs/pages/seo.md` + `system.md`), the CJM To-Be,
and the Stage-04 checklist. All fixes are voice-safe: new pages hand-authored from an existing
shell, and shared/global changes applied by idempotent in-place post-processors (the `fixpack.py`
pattern) - `gen_*.py` was NEVER run (it holds pre-voice copy and would revert the rewrite).

Content gaps (wireframes did not render newly-specced IA):
- System / global nodes were absent. Built 5 new pages: `404` / `500` / `maintenance` (503) / `cookie-consent` / `toasts` (from the `how-it-works.html` shell + `system.md` copy). Registered in `_shell.py` `nav_tree` ("System and global"); `resync.py` stamped the tree onto all 104 pages. Set grew 99 -> 104.
- Footer had no trust strip and no SEO internal-linking, and its links were `href="#"`. `footer_reconcile.py` stamps a trust strip (USDC 1:1 + resolution + resolved-count), a "Popular right now" crawlable block, real category / How It Works / Wallet / My Bets hrefs, and a "Cookie preferences" re-entry - on all 87 footer pages.
- Feed cards carried plain odds but no story-led "why", and the below-fold SEO sections were missing. `feed_reconcile.py` adds a one-line why under each of the 8 feed cards (3 feed pages) plus How betting works here / Why the odds move / Common questions (2 success pages).
- Event Detail had no Related-events block. `related_events.py` adds a crawlable Related events block to the 9 full-content Event Detail pages (loading / error skipped).
- Category pages had no story-led why and no About text. `category_reconcile.py` adds a per-card why + an "About {category} events" block on the 8 category success pages; shared events reuse the same why as the feed.

CJM misalignments:
- Win screen lacked the F5 overconfidence-friction. Added a "Before the next one" grounding note (no "bet again") on `win` / `win-error` / `win-payout-pending`, between Share and Browse events.
- Feed story-led framing lived only on Event Detail; the per-card why (above) now puts it on the feed and category cards too. No-wallet-until-Confirm and the non-chasing Loss screen were already aligned.

Deliberately not done (Stage-04 infra is EQUIVALENT to ours, no functional loss): the course
`docs/screens.md` / `conventions.md` / `critique.md` map to our `_screens.md` / `_conventions.md`
/ `_critique.md`; `_nav.js` -> `_shell.py nav_tree` + `resync.py`; `_wf.css` -> CSS inlined from
`event-feed.html`; the `index.html` coverage map -> the per-page left screen-tree + `_screens.md`.

New copy logged in `voice/docs/microcopy.md` (Steps 15-20). New post-processors
(`footer_reconcile` / `feed_reconcile` / `related_events` / `category_reconcile`) are idempotent
with an em-dash guard. Final gates: 104 pages, 16061 internal links, 0 broken, 0 em-dash.
