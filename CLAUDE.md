# CLAUDE.md - Prediction Market Platform

**This file is the rules.** It is loaded in full into every session, so it carries only what has to be
true next time: invariants, who owns what, and the gate that holds each one. Budget: 200 lines.

Everything else has an owner. A fact written here *and* there is a fact that will drift, so when one
appears twice the copy here is the one to delete.

| Question | Where it is answered |
|---|---|
| What the product is - JTBD, audience, market types, MVP scope, business model, compliance | `PRODUCT.md` |
| What was done and why | `docs/decisions.md` - dated, newest first, never edited |
| What is still open (14 items) | `docs/backlog.md` |
| Which stage is done | the status table in `README.md`, and nowhere else |
| Where a file lives | `STRUCTURE.md` |
| The shipped visual system (Vault) | `DESIGN.md` |
| Screens, navigation, flows, SEO, system nodes | `ia/docs/sitemap.md`, `ia/docs/flows.md`, `ia/docs/pages/` |
| Every UI string | `voice/docs/microcopy.md` |
| The full Stage-08 reasoning, gate by gate | `ui-kit/docs/architecture.md` |

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

`wireframes/` is grey and owns **structure and copy**. `ui-visual/` is painted and owns **the visual
layer only** (colour, type, radius, photography, texture). The build contract is
`wireframes/_conventions.md`; the defect log is `wireframes/_critique.md`.

- **Never paint `wireframes/`**, and never invent a block in `ui-visual/`: a new block, control or
  section is decided in grey and the colour copy follows. **Gate 18** fails the build when the trees
  disagree inside `<main>`, `<header>`, the bottom nav, `<footer>` or the sheet body of an invoked
  overlay. The six differences that ARE the layer boundary (plate wrappers, icon mechanism,
  photograph, chart data, the `TBD` chip, the page behind an overlay) are declared in
  `_conventions.md`.
- **A state is the grey tree's; a shape is the paint's.** Inside the chrome neither tree is simply the
  source: the paint owns what the header IS, the wireframe owns which state it is IN (auth variant,
  active bottom-nav slot, empty notifications). Reconcile in that order -
  `ui-visual/_reconcile_chrome.py`, then `wireframes/_generators/port_chrome.py` - or a port carries
  the wrong answer into 104 files.
- **A screen has a twin, and the map is one file:** `_twins.py` at the root and nowhere else. The trees
  do not name every screen the same way (`politics.html` in grey, `event-feed-politics.html` in
  colour), and gate 18 pairs by filename, so an unpaired page is skipped in SILENCE - 32 grey category
  screens once sat against 4 painted ones behind five hand-written copies of that map. A new screen is
  built in both trees, or its absence is a declared exception.
- **Every screen carries its full state set** (loading / empty / error / success, plus whatever is
  particular to it), and the browse screens carry logged-in and logged-out variants. A state is a page.
- **Grey means grey:** neutral greys only, monochrome outline icons, no colour, type, shadow or
  finished UI.
- **Never run `wireframes/_generators/gen_*.py`.** The voice rewrite was applied to the HTML by hand
  and never back-ported, so regenerating silently reverts it. Shared changes go through the idempotent
  post-processors (`fixpack.py`, `port_structure.py`, `port_chrome.py`, ...), which are written to be
  run again.

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

`components/` holds `tokens.css` plus one css file per component, all reached through
`components/index.css`. `ui-kit/` is the vitrine that shows it and the gates that keep it honest:
`python3 ui-kit/_check_kit.py`, which exits non-zero on the first failure. Contract and full
reasoning: `ui-kit/docs/architecture.md`.

The visual language is **Vault** and it is specified in `DESIGN.md`. The one rule from it that decides
other things: **green and red are outcome semantics (YES / NO), brass is the brand.** An accent never
borrows the win/lose colour, and a candidate in a multi-outcome chart is not an outcome.

### The rule for a change, from here on

- **A value** goes to the token of its own level and reaches every screen by itself: a colour is a
  **semantic role** in section 2 of `components/tokens.css`, a raw value is a **primitive** in
  section 1. A component may never read a colour primitive (gate 13) and may never write a raw scale
  value (gate 12).
- **Markup** goes to two places and only two: the component's page in `ui-kit/`, and the screens in
  `ui-visual/` where it stands. Never to a third copy. **A dialog that also has a standalone page is
  one markup, not two** (gate 19): the canonical copy is the one in `ui-visual/event-feed.html`, and
  only the head, the wiring and the state screens may differ, for the reasons written in
  `wireframes/_conventions.md`.
- **Never on the element.** A `style=` attribute is a rule in the one place the system cannot see, so
  it fails gate 9. Three things are not styling and may stay: a datum (a bar drawn to a width), the
  event photograph, and a value the page script writes at run time.
- **A heading level is structure**, so it is decided in `wireframes/` and the colour copy follows.
  Exactly one `<h1>` per screen, no skipped level, **in both trees** (gate 15 reads both, because a
  check that reads only the copy can pass while the original is wrong).
- **Geometry has three scales and they are not interchangeable.** `--space-*` is the distance BETWEEN
  things, `--size-*` the side OF a thing, `--control-*` and `--icon-*` the box and the mark of an
  interactive element. Same numbers, different questions (gate 12).
- **A sample photograph is content**, so it goes on the element as `style="background-image:..."`,
  which is one of the three things gate 9 lets through. A shared image asset lives in `assets/` at the
  root, owned by neither layer.
- **A part is imported before the whole that holds it.** The cascade decides which of two rules of
  equal specificity wins, so the order of the `@import`s in `components/index.css` is a rule, not
  formatting: a card may restyle the odds bar it contains, an odds bar may not quietly restyle every
  card. The order is **computed** from what each component contains, read out of the specimen DOM:
  `python3 ui-kit/_levels.py --order` prints it and gate 23 fails the build when the file stops
  matching. That map is also the level (atom / molecule / organism) in `ui-kit/docs/inventory.md` and
  the grouping of the vitrine's side panel, all from `ui-kit/_levels.py` and nowhere else.
- **A new component** = css in `components/` + an `@import` at the position `--order` gives it + a
  page in `ui-kit/` + a row in `ui-kit/docs/inventory.md`. Its entry in `ui-kit/_nav.js` is derived,
  not typed. Then `python3 ui-kit/_check_kit.py` has to pass, every gate.
- **A document in `ui-kit/docs/` is a page of the vitrine.** It is rendered by `ui-kit/_gen_docs.py`
  and registered in `_gen_docs.PAGES`, which is also where `_gen_component_pages.py` reads the side
  panel group from; run the component generator first, because it writes `docs/coverage.md`. Nothing
  in `ui-kit/` or `ui-visual/` may link a raw `.md`: a browser downloads one instead of drawing it
  (gate 21).
- **A checker asks the markup, not the text.** A page that quotes markup is normal here (every
  component page ends with its own css, and the documents quote both), so a scan for a path, a
  `url()` or a font host has to skip what is inside `<code>` and `<pre>` and look at the attribute
  that would make the request. Three gates were reading a sentence as a reference.
- **`ui-kit/kit.html` is frozen.** It is the flat kit the system was read out of and it is kept as
  provenance; a component is never added to it. **`ui-kit/shell.html` composes** the header and
  bottom-nav specimens and holds no markup of its own.
- **Two token levels, not three.** Primitive + semantic. Colour is the only thing with a second
  level, because a radius or a gap has nothing for a theme to override; a component level is not
  part of this stage.
- **A dialog is bounded by the viewport and its BODY scrolls**, at every width. The frame keeps
  `overflow:clip` because it clips its own corners; a box cannot both clip decoration and contain
  content, and the answer is that the head stays and the body moves. A skin (`outcome-dialog`,
  `signin-dialog`) is named for what the sheet IS, and a standalone overlay page wears the shared
  dialog's own class list plus `app-case` (gate 19).
- **A font is served from this repo.** No page may call a font host: the request carries a visitor's
  IP to a third party before the consent banner has asked anything (gate 20). Faces are woff2 in
  `assets/fonts/`, declared once in `components/fonts.css`, imported first by `index.css`.
- **The side panel is one component with one vocabulary, in all three trees.** A **label** names a run
  of rows and opens nothing (`.sidebar-divider`, `.sub` when nested); a **row** that opens a page is a
  link (`.sidebar-page-link`, `.sidebar-sub-link` when nested under one); the page you are **on** is
  `.active` at whichever level it sits and the group you are **in** is `.active` on its label. A row
  that goes nowhere is not an `<a>`. The tree is a named `<nav>`. No page describes the panel in its
  own stylesheet: `ui-visual/` and `ui-kit/` reach it through `components/index.css`, the 28 course
  pages link `fonts.css` + `tokens.css` + `course-chrome.css` last in `<head>` (`_course_chrome.py`),
  and a panel's behaviour is one string in `ui-visual/_panel_reveal.py` emitted two ways.
- **Quiet is a colour, not an opacity.** `opacity` fades text into its background and no sweep that
  reads `getComputedStyle().color` can see it: `--chrome-muted` is 5.03:1 on the panel and 2.37:1 at
  `opacity:.55`. Depth is a colour role, so the value being chosen is the value being checked.
- **Gate 1 masks the `<aside>`, so nothing else reads it.** Gate 22 does: every screen's panel marks
  its own file, and every panel generator is at its fixed point, because a generator that copies a
  shell copies the shell's idea of where it is.
- **A checker that reads the source does not read the page.** "0 non-neutral hex in the wireframes"
  was true while 992 links rendered in the browser's blue, and "the chart is ported" was true while
  it drew as a black rectangle, because an SVG with no `fill` is black. **A missing value is a
  value.** Measure the computed result, in a browser, at both widths.
