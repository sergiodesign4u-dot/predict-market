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
  `components/index.css`. **Every PAINTED screen links that one file and nothing else, and the grey
  tree links no stylesheet at all**: 106 of 106 in `ui-visual/` and 57 of 57 in `ui-kit/` link it,
  **0 of the 104 in `wireframes/` do**, and those 104 carry an inline `<style>` block each. Counted
  2026-08-12. The sentence here said "every screen" until then, and the folder file it contradicted
  is the one that had it right. The visual language is
  **Vault**, specified in `DESIGN.md`, and its one rule that decides others: **green and red are
  outcome semantics (YES / NO), brass is the brand.**
- **One vitrine.** `ui-kit/` shows the system to a person, and it was rebuilt by hand between
  2026-08-07 and 2026-08-08 from five anchor screens: event feed, event detail, active bets, deposit,
  sign in, with their loading, empty, error and logged-out variants. **A level is a SHELF and a
  component is a PAGE**, and the two answer different questions: comparing ten atoms is the shelf's
  job, and taking one apart needs room a shelf does not have, because a shelf gives every component
  one specimen and one rule. **The threshold is not a placement count** - `toast` has four and
  `toggle` has three, and four of the toggle's five faces have no placement in the product at all, so
  a stand built by walking screens would show one grey oval and call it the component. **57 of 57 pages written**, one route in `_nav.js`, 0 generators and 0 gates. **The panel computes the tally from `_nav.js` and this line was typed by hand, which is why it said 55 while 57 files stood on disk**: 1 overview, 5 foundations, 4 shelves, 12 atoms, 16 molecules, 13 organisms, 6 patterns, counted 2026-08-12 by listing `ui-kit/*.html` and by parsing the registry, and the two agree. It was 54 until 2026-08-11, when three pages landed the same day: `logo` with the rename to Yonder, `platehead` by backlog 108, and `responsive.html`, the FIFTH foundation, which is the page every enumeration in this repository was still leaving out. And it had been 55 before that until `account` was deleted on 2026-08-08, a component whose whole stylesheet was a face nothing wore.

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
- **ONE ENGINE IS ONE READING, AND THE PROTOCOL IS PART OF THE READING TOO.** Every sweep here until
  2026-08-13 was Chromium, and Chromium agreed with a page that was visibly broken. **These pages are
  read from DISK**, and `file://` gives every file its own opaque origin, so anything fetched in CORS
  mode has no origin to match: a `mask-image`, a `@font-face` source, an external `<use>`. A
  `background-image` is not fetched that way and loads from the same folder in the same document,
  which is why the failure looks like one property misbehaving instead of one rule applying. It has
  cost this repository three times now: 0 of 34 glyphs from an external sprite, a brass rectangle
  over every trust tile, and **WebKit rendering all 163 documents in a fallback face because DM Sans
  and Space Grotesk never arrive**. Measure over `file://` as well as `http://`, and in more than one
  engine. WebKit is installed: `playwright@1.62.0` is global, and `webkit` in the harness is the same
  build as the Safari on this machine.
- **THE REVIEW PANEL IS 220 PHYSICAL PIXELS AND IT IS INSIDE THE FRAME OF EVERY FULL-PAGE
  COMPARISON TAKEN HERE.** A whole-page sweep over 163 documents on two engines reported a worst
  channel delta of 198 spread thinly over dozens of product screens, which reads exactly like a
  regression. Every one of those pixels was at x below 220: the panel's own text, one device pixel
  lower, because it scrolls its active row into view and the scroll now lands on final font metrics.
  Re-diffed from x=220 rightwards the product was **0.000 per cent differing on every screen**.
  **Crop the chrome out before believing a page-level number**, the same way a media query that
  reads the window has to be read against a layout that gets the container.
- **`scrollWidth > clientWidth` IS NOT A PAGE THAT SCROLLS SIDEWAYS**, and that predicate is behind
  every horizontal-scroll number this repository has published. Four course documents were filed as
  scrolling on a phone; set `document.scrollingElement.scrollLeft = 9999` on any of them, before the
  fix or after, and it reads back **0**. Content standing past the right edge with no way to reach
  it is a worse defect and a different one, and the fix it asks for is different too: the culprits
  were four pieces of `white-space:nowrap` on prose and one flex row, not the tables the row named,
  because **every element that sweep called a culprit was already inside a scrolling container**.
- **A reading that does not move when the input moves is not a reading of the page**, and it is the
  twin of the rule above about a number that moves when nothing moved. A two-layer mask measured
  against the shipped tree gave 13 to 55 per cent of pixels differing at a mean under 6 of 255 on
  both engines, which looked like an approximation and was WebKit drawing nothing at all. What
  exposed it was rendering the same mask at two qualities and diffing THOSE: Chromium moved 10.57 per
  cent of its pixels and WebKit moved 0.00. **Vary the input by something you know must show, and
  check the instrument saw it, before you believe what it says about the page.**
- **"Both widths" is not a measurement of a responsive system: measure AT the rungs and one pixel
  either side of each.** A defect can live entirely between the two widths everybody reads. The
  system breaks at 40rem, 47.5rem and 56.25rem and the review chrome docked at 860, and every audit here read
  390 and 1280, so for a day **73 of 160 pages scrolled horizontally at exactly one width** and every
  sweep reported zero. The same rung took the browse content column from 530 to 297 and `.ed-main`
  from 430 to 211 between 859 and 860. **A media query reads the WINDOW and a layout gets the
  CONTAINER**, so anything that eats width outside the product, a docked panel most of all, makes
  every branch above it a branch chosen for a page that is not there. **And one pixel either side
  found the next one the day after**: a rung written as a PAIR, `max-width:640px` in eight files and
  `min-width:640px` in five, matches on both sides at once, so 640 rendered a page that existed at no
  other width, and the desk header it turned on asks for 694px, which put **73 of the 106 documents
  in `ui-visual/` into horizontal scroll from 641 to 652**. A rung is one pixel and it belongs to the
  wide side. The ladder is named in `components/tokens.css`, page frame, **and it is in `rem` since
  2026-08-13**: 40rem, 47.5rem and 56.25rem are 640, 760 and 900 at the default browser font and MOVE
  WITH IT, so a reader who set a 24px default reaches the desk at 960 and keeps one column until
  then. **A length in a media query resolves against the INITIAL font size and ignores every
  declaration on the root element**, so a sweep that writes `html{font-size:24px}` reports the rungs
  not moving and is measuring nothing; only the browser's own default setting, CDP
  `Page.setFontSizes`, changes both the type and the rung. The 1140 harness stays in px, because a
  docked panel is 220 physical pixels whatever the reader's font is. **106 and 105 both name a
  true thing and every number in this repository has to say which**: `ui-visual/` holds 106
  documents, 105 of them screens, and `overview.html` is the index of the tree rather than a screen
  in it.
- **A verdict about a component is a statement about the SET of its placements.** A reading taken on
  one placement and printed as a property of the component is a fact about a slot wearing a
  component's name: `navitem` was published FIXED at 258px, the width of the third of its three
  slots, while 420 of its 995 placements run 79 to 159 and are fully fluid, and `chip` was published
  FIXED at 81px while standing at nine widths from 18 to 206 in one document. **Where placements
  disagree, say so; do not pick one.** The measurement is `ui-kit/docs/inventory.md`, behaviour on
  width.
- **A RULE THAT CANNOT BE RENDERED CANNOT BE CHECKED, AND IT WILL BE WRONG THE DAY IT FIRST DRAWS.**
  Every instrument in this file reads the COMPUTED page, so a face the product never places is
  covered by none of them, and a clean sweep over a tree that omits a state is a clean sweep over
  nothing. Five rules in `yesno.css` drew the chosen NO, and `.sel` and `.no` had never once stood on
  the same element: **127 chosen sides in the paint, 24 in the grey and 39 on the stand, and every
  one of them YES**. Half of a symmetric control had therefore never been measured, which is this
  repository's whole method switched off for one component. Drawing it once, on
  `event-detail-bet-processing.html` on 2026-08-15, is what produced the number: the chosen NO is
  **4.64:1** against the chosen YES at 6.42:1, the tighter of the two and an assumption until that
  day. So a state the system styles gets a placement, in both trees, or the styling is a claim nobody
  can test.
- **A COMPONENT WITH NO FACE IS A NAME; A FACE WITH NO PLACEMENT IS A FACE**, and before deleting on
  a zero, ask WHICH zero it is: the CSS is gone, or the markup is. `account.css` was deleted on
  2026-08-08 for having no face left, its two surviving rules being another component's stone.
  `.icon-btn-lift` reads 0 placements since 2026-08-13, when backlog 144 took the footer's five
  social marks off every screen because a social account can never become an internal route; its
  rules are whole and its placements return on a date somebody chooses. **The consistency audit read
  the second as the first and put a live face on a deletion list, because both compute to zero and
  zero is where two different things look alike.** A zero that is worn by nothing says so, next to
  the reason, rather than reading as a face nobody measured.
- **Read the instrument before you read the finding: measure the same thing twice, unchanged, and
  the difference has to be zero.** A before-and-after over 19 screens reported 31 files changed by an
  edit that could not change anything; re-reading the unchanged tree gave **3,587 differing rows of
  18,390**, every one an entrance animation caught mid-flight. Freeze animation and transition, let
  the layout settle, **and throw the first pass away**: a cold pass, resolving fonts and stylesheet
  for the first time, differs from every pass after it and cost another 165 rows of noise. Prove the
  control is 0 before believing the comparison. **A number that moves when nothing moved is a
  reading of the instrument, not of the page.**
- **A RESIZE IS NOT A LAYOUT: give it a frame, or a sweep over widths reads the width it left
  behind.** The same probe that had reported 0 reported **382 horizontally scrolling documents** on
  2026-08-15, over screens whose markup had not been touched, and every one of them was a read taken
  in the same turn as `setViewportSize`. Two `requestAnimationFrame`s later the identical run reads
  **0 of 8,544 renders**, and the culprits it had named, an `svg` at 520 and the header's utility
  group at 458, are the 1280 layout still standing while the window is already 320. **The tell was
  the arithmetic**: 138 at 320 and 98 at 360 is one constant width of 458, and a defect that is the
  same box at every width is usually not a defect. So a width sweep gets a settle AND a positive
  control: inject a box wider than the window and prove the probe sees it, because 0 is also what a
  blind probe reports.
- **No em dash**, anywhere.
