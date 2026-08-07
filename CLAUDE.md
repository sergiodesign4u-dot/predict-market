# CLAUDE.md - Prediction Market Platform

**This file is the rules.** It is loaded in full into every session, so it carries only what has to be
true next time: invariants, who owns what, and the reason each one exists. Budget: 200 lines.

**There are no build gates any more, and that changes what this file is for.** Until 2026-08-07 the
repository held 54 Python scripts, 9 browser scripts and 41 gates that failed the build, and a rule
was allowed to leave this file the moment a gate held it. The gates were deleted, with the vitrine
that fed them, because the measurement had become a machine that was re-paid on every edit: a
one-line change to a stylesheet cost a regeneration, a re-capture, 41 gates, 525 snapshots and an
audit. **So every rule below is now kept by being READ, and each one carries the reason it exists**,
because a rule with no reason is a rule that gets argued away by whoever meets it next. The full
account is in `docs/decisions.md` and `docs/kit-archive/README.md`.

Everything else has an owner. A fact written here *and* there is a fact that will drift, so when one
appears twice the copy here is the one to delete.

| Question | Where it is answered |
|---|---|
| What the product is - JTBD, audience, market types, MVP scope, business model, compliance | `PRODUCT.md` |
| What was done and why | `docs/decisions.md` - dated, newest first, never edited |
| What is still open | `docs/backlog.md` |
| Which stage is done | the status table in `README.md`, and nowhere else |
| Where a file lives | `STRUCTURE.md` |
| The shipped visual system (Vault) | `DESIGN.md` |
| Screens, navigation, flows, SEO, system nodes | `ia/docs/sitemap.md`, `ia/docs/flows.md`, `ia/docs/pages/` |
| What a page of a given TYPE is made of, before one is drawn | `ia/docs/blocks.md` - banked by type, never by node |
| Every UI string | `voice/docs/microcopy.md` |
| What the deleted kit had already worked out | `docs/kit-archive/` - prose, read by nothing |

---

## Design principles

1. **Clarity first** - every screen is self-explanatory; a new user is never lost.
2. **Trust is stated, not implied** - transparent odds, a named resolution rule, an audit trail, one
   plain provable sentence rather than borrowed authority.
3. **Engagement is about events, not money** - notify a person about what they bet on, never about
   topping up a balance.

Mobile-first is not on that list because it is a stance, and it is written once, below.

---

## Information architecture

`ia/docs/sitemap.md` (entities, screens, navigation, desktop layer, depth map) and `ia/docs/flows.md`
(the four user flows: MJ, FJ2, FJ5+EJ3, SJ1) are the source of truth, with `ia/docs/pages/seo.md` and
`system.md` for the Detailed layer. The HTML in `ia/` renders them and the markdown wins if they ever
diverge. **Do not copy a nav table, a screen hierarchy or a flow into another file.** Two copies of one
map is the defect this repo has paid for more than once, and the second copy is always the one that is
wrong.

Three decisions govern every page-level node:

- **Mobile-first, fully adaptive.** Responsive both ways, but mobile is the priority: block priority
  and the first screen are reasoned from mobile (base 360px). Desktop is designed deliberately, not
  derived from a wide layout.
- **Two IA layers.** Global (concept map + flows) answers "where can the user go"; per-page answers
  "what is on this page and how it behaves" - blocks, states, components, SEO.
- **SEO-ahead.** The structural SEO layer (URL/slug, H1/H2, breadcrumbs, schema.org, indexation,
  internal linking) is decided in IA. The wireframe validates layout only; production supplies final
  content and real query volumes. The three are never mixed, so finding that a block is missing never
  means redrawing a wireframe.

---

## The two screen trees

`wireframes/` is grey (104 screens) and owns **structure and copy**. `ui-visual/` is painted (106
screens) and owns **the visual layer only** (colour, type, radius, photography, texture). The build
contract is `wireframes/_conventions.md`; the defect log is `wireframes/_critique.md`.

- **Never paint `wireframes/`**, and never invent a block in `ui-visual/`: a new block, control or
  section is decided in grey and the colour copy follows. The trees must say the same thing inside
  `<main>`, `<header>`, the bottom nav, `<footer>` and the sheet body of an invoked overlay. The six
  differences that ARE the layer boundary (plate wrappers, icon mechanism, photograph, chart data,
  the `TBD` chip, the page behind an overlay) are declared in `_conventions.md`. **A check used to
  fail the build on this and no longer does**, so it is now read before the edit rather than after.
- **A state is the grey tree's; a shape is the paint's.** Inside the chrome neither tree is simply the
  source: the paint owns what the header IS, the wireframe owns which state it is IN (auth variant,
  active bottom-nav slot, empty notifications). Reconcile in that order, or the wrong answer travels
  into 104 files at once.
- **A screen has a twin, and the two trees do not name it the same way** (`politics.html` in grey,
  `event-feed-politics.html` in colour). That map used to live in `_twins.py`; the script is gone and
  the pairing is now done by reading. An unpaired page is silent, which is why five hand-written
  copies of that map once left 32 grey category screens standing against 4 painted ones.
- **Every screen carries its full state set** (loading / empty / error / success, plus whatever is
  particular to it), and the browse screens carry logged-in and logged-out variants. A state is a page.
- **Grey means grey:** neutral greys only, monochrome outline icons, no colour, type, shadow or
  finished UI.
- **A change to many screens is made by hand or with a throwaway script, and the script is not kept.**
  36 generators lived in `wireframes/_generators/` and every one of them was a standing hazard: the
  voice rewrite was applied to the HTML by hand and never back-ported, so regenerating any screen
  silently reverted it. A tool that must never be run is a tool that should not exist.

---

## Copy

The voice is rules, not a mood: `voice/docs/voice.md` is the contract - five principles, the lexicon
(one concept, one word), the forbidden list, and per-element rules - and every rule there carries an
example, an anti-example and the research line it derives from, so a line comes out the same whoever
writes it.

**A UI string gets a row in `voice/docs/microcopy.md` before it ships**, then goes into both trees.
That table is the source of truth for copy, and for one whole stage it was not: 43 shipped lines had
no row in it. User-written content (event questions, comments, usernames, sample figures) is never
rewritten.

---

## The design system

`components/` holds `tokens.css` plus one css file per component (51 files, 5,651 lines), all reached
through `components/index.css`. **That is the whole system.** It is what the 210 screens read and it
was not touched when the vitrine was deleted.

The visual language is **Vault** and it is specified in `DESIGN.md`. The one rule from it that decides
other things: **green and red are outcome semantics (YES / NO), brass is the brand.** An accent never
borrows the win/lose colour, and a candidate in a multi-outcome chart is not an outcome.

**`ui-kit/` is being rebuilt** and holds one page saying so. The plan, in order: a census of five
anchor screens with their states, read in a browser at two widths in both themes; atomic levels
declared once in an inventory; one consolidation pass where a value is allowed to change; one
hand-written page per component with its states in both themes; one audit run as a report. The five
anchors are event feed, event detail, active bets, deposit and sign in, with their loading, empty,
error and logged-out variants: 41 screens.

### Contributing to the system

- **New goes into the SYSTEM first and onto a screen second, never the other way round.** A screen
  that grows a part every time it meets a new page has not been tested by that page, it has been
  edited by it.
- **A value** goes to the token of its own level in `components/tokens.css`: a colour is a **semantic
  role** in section 2, a raw value is a **primitive** in section 1. A component reads a role and never
  a colour primitive, and never writes a raw scale value. **A state token has a value in both themes
  or it is not one**, because a theme with a hole in it rots quietly and is handed over broken.
- **Two token levels, not three.** Primitive + semantic. Colour is the only thing with a second level,
  because a radius or a gap has nothing for a theme to override.
- **A component** = css in `components/` + an `@import` in its own level group + a page in `ui-kit/`
  + a row in the inventory. **A composition** = three screens or more, in `components/patterns/`. Two
  screens is a candidate, not a pattern, and it stays markup.
- **New on a screen with none of the three is forbidden.** It is not an exception for the screen, it
  is an order for the system.

### The rule for a change

- **Markup** goes to two places and only two: the component's page in `ui-kit/`, and the screens in
  `ui-visual/` where it stands. Never to a third copy. **A dialog that also has a standalone page is
  one markup, not two**: the canonical copy is the one in `ui-visual/event-feed.html`, and only the
  head, the wiring and the state screens may differ.
- **Never on the element.** A `style=` attribute is a rule in the one place the system cannot see.
  Three things are not styling and may stay: a datum (a bar drawn to a width), the event photograph,
  and a value the page script writes at run time.
- **A heading level is structure**, so it is decided in `wireframes/` and the colour copy follows.
  Exactly one `<h1>` per screen, no skipped level, in both trees: reading only the copy can pass
  while the original is wrong.
- **A sample photograph is content**, so it goes on the element as `style="background-image:..."`. A
  shared image asset lives in `assets/` at the root, owned by neither layer.
- **A part is imported before the whole that holds it.** The cascade decides which of two rules of
  equal specificity wins, so the order of the `@import`s in `components/index.css` is a rule, not
  formatting: a card may restyle the odds bar it contains, an odds bar may not quietly restyle every
  card.
- **A level is a decision and not a reading.** Level 1 contains nothing from the system, level 2
  contains atoms, level 3 contains molecules or is a shell. A component built out of its own class
  names reads as containing nothing, and seven of seventeen such readings were once the whole atom
  shelf and none of them was an atom. So a level is DECLARED, with a reason, in the inventory.
- **A font is served from this repo.** No page may call a font host: the request carries a visitor's
  IP to a third party before the consent banner has asked anything. Faces are woff2 in
  `assets/fonts/`, declared once in `components/fonts.css`, imported first by `index.css`.
- **Quiet is a colour, not an opacity.** `opacity` fades text into its background and no sweep that
  reads `getComputedStyle().color` can see it: `--chrome-muted` is 5.03:1 on the panel and 2.37:1 at
  `opacity:.55`. Depth is a colour role, so the value being chosen is the value being checked.
- **Reading the source is not reading the page.** "0 non-neutral hex in the wireframes" was true while
  992 links rendered in the browser's blue, and "the chart is ported" was true while it drew as a
  black rectangle, because an SVG with no `fill` is black. **A missing value is a value.** Measure the
  computed result, in a browser, at both widths and in both themes.
- **A measurement is an act, not a machine.** Walk the screens, write down what was found, decide, and
  keep the report. The moment a measurement becomes a permanent check, every later edit pays for it
  again, and that is what cost this repository seven days and 145 MB.
