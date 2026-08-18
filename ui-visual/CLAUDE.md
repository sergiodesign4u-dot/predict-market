# ui-visual/ - the painted tree

114 documents, 113 of them screens, the colour copies of `wireframes/`. It was 110 and 109 until 2026-08-18, when the four Type 1 static documents arrived in both trees, and 109 and 108 until
2026-08-17, when the state a bet is actually in got a page of its own, `docs/backlog.md` 185. This tree owns **the visual
layer**: colour, type, radius, photography, texture. It does not own what is on the page.

**AND SINCE 2026-08-16 IT OWNS ONE THING THAT IS NOT VISUAL, WITH A REASON.** 63 of the 113 screens
carry a `<script type="application/ld+json">`, the structured-data half of the head that
`ia/docs/pages/seo.md` specifies. The meta-tag half stays in the IA, because it is a fact written
once and never derived from the page, and 110 copies of it would be 110 places to drift. Structured
data is the opposite: it RESTATES what a reader sees, so it can disagree with the page, and
disagreement is measurable only here. Every node is checked against the render, and **a state may
show less, never something different**: an empty feed carries no `ItemList` and a loading detail
carries no schema at all. `docs/backlog.md` 171.

## The invariants

- **A screen carries no styles of its own.** One link, `../components/index.css`, and nothing else.
- **AND THAT INCLUDES A MEDIA QUERY. NEVER, IN ANY SCREEN FILE.** Adaptation lives in a token, a
  component, a pattern or the shell, and nowhere else. It is written here as well as in
  `components/CLAUDE.md` because the day it breaks is not the day it is written: this tree is
  assembled by many hands at once, and twenty hands each adding one honest little breakpoint is how
  the adaptive layer ends up scattered across twenty files that no rung and no registry can see, the
  same way inline CSS scattered across this tree once before. Measured at Responsive step 4, over all
  106 screens: **0**. The registry that makes the check possible is in `components/tokens.css`, page
  frame, and the reason a query cannot simply read a token is that `@media` resolves before the
  variable cascade and fails silently.
  A `<style>` block or a `style=` attribute is a rule in the one place the system cannot see. Three
  things are not styling and may stay: a datum (a bar drawn to a width), the event photograph as
  `style="background-image:..."`, and a value the page script writes at run time.
- **Never invent a block here.** A new block, control or section is decided in grey and the colour
  copy follows. The two trees must say the same thing inside `<main>`, `<header>`, the bottom nav,
  `<footer>` and the sheet body of an invoked overlay. The six differences that ARE the layer
  boundary are declared in `../wireframes/_conventions.md`.
- **A state is the grey tree's; a shape is the paint's.** Inside the chrome the paint owns what the
  header IS and the wireframe owns which state it is IN (auth variant, active bottom-nav slot, empty
  notifications). Reconcile in that order or the wrong answer travels into 104 files at once.
- **A dialog that also has a standalone page is one markup, not two.** The canonical copy is the one
  in `event-feed.html`; only the head, the wiring and the state screens may differ. A screen can
  drift from its own second copy inside this tree, and only the twin was ever checked.
- **A screen has a twin and since 2026-08-15 it has the same NAME**, backlog 156: the 32 grey
  category screens were `politics.html` and are `event-feed-politics.html`, so a diff of the two file
  lists is now the pairing rather than a table beside it. **The table is what hid the hole**: pairing
  by filename cannot see an unpaired page, which is how 32 grey category screens stood against 4
  painted ones for two stages, in silence. The one document with no twin is `overview.html` here, and
  it is the index of this tree rather than a screen in it.
- **A shared image asset lives in `../assets/`**, owned by neither tree, **and since 2026-08-17 one
  shared SCRIPT does too.** `assets/icons.js` was the only one and the rule it set is the reason:
  a `<script src>` resolves from disk and from a server alike, where anything fetched in CORS mode
  over `file://` has no origin to match. `assets/search.js` is the second, and it is the one place
  a script here may be shared rather than inline. **The test is whose question it answers.** Every
  other script in this tree is about the screen it stands in: the sub-category rail reads the cards
  on its own page, and a copy per screen is correct because each copy has a different page under it.
  Search is the opposite - it answers from all 108 screens about events that are on none of them, so
  the catalog cannot be read out of the document it is asked in, and 108 copies of it would be 108
  places to drift. **The cost is named in the file rather than found later**: the catalog is
  extracted from this tree by hand, so an event added here and not re-taken there is an event search
  cannot find.

## What is here

- 15 families with their full state sets: loading, empty, error, success, plus logged-in and
  logged-out on the browse screens. **A state is a page**, not a class.
- `overview.html` is the index and is the one page in this folder that is a stand rather than a
  screen. It links `../ui-kit/_page.css` for its own furniture, which is why that file exists.
- `old/` holds the pre-Vault directions. Nothing links into it and its internal links are broken;
  it is provenance, not a tree.

## Editing many screens at once

There are no generators any more: 18 scripts that used to write into this folder were deleted on
2026-08-07, and one of them, the theme applier, was how the whole tree was painted. **Write a
throwaway script in the scratchpad, run it, delete it, and describe the sweep in the commit.** A
script kept in the repo is a script somebody runs later against a tree that has moved on, which is
exactly how a hand-applied voice rewrite was silently reverted here once.

## Where the record is

`../docs/decisions.md` for why, `../wireframes/_critique.md` for the defect passes, `../DESIGN.md`
for the visual language.
