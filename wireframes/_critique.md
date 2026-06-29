# Wireframes - Critique pass (Krok 9)

Rigorous defect audit of all `wireframes/*.html` (96 pages) against
`_conventions.md`, `IA/sitemap.md`, and `IA/flows.md`. Method: mechanical greps
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
`_conventions.md`, `_screens.md`, `IA/sitemap.md`, `IA/flows.md`.

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
