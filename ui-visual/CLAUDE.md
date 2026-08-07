# ui-visual/ - the painted tree

106 screens, the colour copies of `wireframes/`. This tree owns **the visual layer only**: colour,
type, radius, photography, texture. It does not own what is on the page.

## The invariants

- **A screen carries no styles of its own.** One link, `../components/index.css`, and nothing else.
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
- **A screen has a twin and the names differ**: `politics.html` in grey is `event-feed-politics.html`
  here. Pairing by filename cannot see an unpaired page, which is how 32 grey category screens stood
  against 4 painted ones for two stages, in silence.
- **A shared image asset lives in `../assets/`**, owned by neither tree.

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
