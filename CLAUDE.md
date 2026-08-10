# CLAUDE.md - Prediction Market Platform

**This file is the rules.** It is loaded in full into every session, so it carries only what has to
be true everywhere: the map, the principles, and the handful of rules that cross folders.

**Each folder carries its own `CLAUDE.md`, loaded when you work in it**, and that is where the
detail lives: what the folder IS, its invariants, and the traps it has already paid for.

| Folder | Its file says |
|---|---|
| `components/` | the system itself: token levels, import order, the traps a stylesheet here has cost |
| `ui-visual/` | the painted tree: no styles of its own, what the paint owns and what it does not |
| `wireframes/` | the grey tree: structure and copy, states as pages, why the generators are gone |
| `ui-kit/` | the vitrine, rebuilt by hand: what each page is, the rules it was rebuilt under, the plan |
| `voice/` | what the product says: the contract, the inventory, and the row-before-ship rule |
| `ia/` | where the user can go: the sources of truth and the one-copy rule |
| `docs/kit-archive/` | frozen, read by nothing, and what is worth taking out of it |

**There are no build gates any more, and that changes what this file is for.** Until 2026-08-07 the
repository held 63 scripts and 41 gates that failed the build, and a rule was allowed to leave this
file the moment a gate held it. They were deleted with the vitrine that fed them, because the
measurement had become a machine that was re-paid on every edit. **So every rule is now kept by
being READ, and each one carries the reason it exists**, because a rule with no reason is a rule
that gets argued away by whoever meets it next. The account is in `docs/decisions.md`.

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
| Screens, navigation, flows, SEO | `ia/docs/` |
| Every UI string | `voice/docs/microcopy.md` |
| What the deleted kit had already worked out | `docs/kit-archive/` |

---

## Design principles

1. **Clarity first** - every screen is self-explanatory; a new user is never lost.
2. **Trust is stated, not implied** - transparent odds, a named resolution rule, an audit trail, one
   plain provable sentence rather than borrowed authority.
3. **Engagement is about events, not money** - notify a person about what they bet on, never about
   topping up a balance.

**Mobile-first, fully adaptive.** Block priority and the first screen are reasoned from mobile at
360px; desktop is designed deliberately, not derived from a wide layout. It is not in the list above
because it is a stance rather than a principle, and it is written once, here.

---

## The shape of the work

- **Two screen trees.** `wireframes/` is grey and owns structure and copy; `ui-visual/` is painted
  and owns the visual layer only. A block is decided in grey and the colour copy follows. **A state
  is a page**, in both trees. The six differences that ARE the layer boundary are declared in
  `wireframes/_conventions.md`.
- **One system.** `components/` holds `tokens.css` plus one file per component, reached through
  `components/index.css`. Every screen links that one file and nothing else. The visual language is
  **Vault**, specified in `DESIGN.md`, and its one rule that decides others: **green and red are
  outcome semantics (YES / NO), brass is the brand.**
- **One vitrine.** `ui-kit/` shows the system to a person, and it was rebuilt by hand between
  2026-08-07 and 2026-08-08 from five anchor screens: event feed, event detail, active bets, deposit,
  sign in, with their loading, empty, error and logged-out variants. **A level is a SHELF and a
  component is a PAGE**, and the two answer different questions: comparing ten atoms is the shelf's
  job, and taking one apart needs room a shelf does not have, because a shelf gives every component
  one specimen and one rule. **The threshold is not a placement count** - `toast` has four and
  `toggle` has three, and four of the toggle's five faces have no placement in the product at all, so
  a stand built by walking screens would show one grey oval and call it the component. **54 of 54 pages written**, one route in `_nav.js`, 0 generators and 0 gates. It was 55 until `account` was deleted on 2026-08-08, a component whose whole stylesheet was a face nothing wore.

---

## The rules that cross folders

- **New goes into the SYSTEM first and onto a screen second, never the other way round.** A screen
  that grows a part every time it meets a new page has not been tested by that page, it has been
  edited by it. New on a screen with no component, no token and no pattern behind it is not an
  exception for the screen, it is an order for the system.
- **A component** = css in `components/` + an `@import` in its own level group + a page in `ui-kit/`
  + a row in the inventory. **A composition** = three screens or more, in `components/patterns/`.
  Two screens is a candidate, not a pattern, and it stays markup.
- **Markup goes to two places and only two**: the component's page in `ui-kit/`, and the screens in
  `ui-visual/` where it stands. Never a third copy.
- **Never on the element.** A `style=` attribute is a rule in the one place the system cannot see.
  Three things are not styling and may stay: a datum, the event photograph, and a value the page
  script writes at run time.
- **A measurement is an act, not a machine.** Walk the screens, write down what was found, decide,
  and keep the report. The moment a measurement becomes a permanent check, every later edit pays for
  it again, and that is what cost this repository seven days and 145 MB.
- **A sweep is a throwaway script.** Write it in the scratchpad, run it, delete it, and describe the
  sweep in the commit. A script kept in the repo is a script somebody runs later against a tree that
  has moved on: that is how a hand-applied voice rewrite was silently reverted here.
- **Reading the source is not reading the page.** "0 non-neutral hex in the wireframes" was true
  while 992 links rendered in the browser's blue, and "the chart is ported" was true while it drew as
  a black rectangle, because an SVG with no `fill` is black. **A missing value is a value.** Measure
  the computed result, in a browser, at both widths and in both themes.
- **"Both widths" is not a measurement of a responsive system: measure AT the rungs and one pixel
  either side of each.** A defect can live entirely between the two widths everybody reads. The
  system breaks at 640, 760 and 900 and the review chrome docked at 860, and every audit here read
  390 and 1280, so for a day **73 of 160 pages scrolled horizontally at exactly one width** and every
  sweep reported zero. The same rung took the browse content column from 530 to 297 and `.ed-main`
  from 430 to 211 between 859 and 860. **A media query reads the WINDOW and a layout gets the
  CONTAINER**, so anything that eats width outside the product, a docked panel most of all, makes
  every branch above it a branch chosen for a page that is not there. The ladder is named in
  `components/tokens.css`, page frame.
- **Read the instrument before you read the finding: measure the same thing twice, unchanged, and
  the difference has to be zero.** A before-and-after over 19 screens reported 31 files changed by an
  edit that could not change anything; re-reading the unchanged tree gave **3,587 differing rows of
  18,390**, every one an entrance animation caught mid-flight. Freeze animation and transition, let
  the layout settle, **and throw the first pass away**: a cold pass, resolving fonts and stylesheet
  for the first time, differs from every pass after it and cost another 165 rows of noise. Prove the
  control is 0 before believing the comparison. **A number that moves when nothing moved is a
  reading of the instrument, not of the page.**
- **No em dash**, anywhere.
