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
