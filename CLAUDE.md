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
| Which stage is done | the status table in `README.md`. Two REGISTRIES render it as well, `assets/_roadmap.js` on the 28 course documents and `ui-kit/_nav.js` on the 60 stand pages, and this row said "and nowhere else" while `_roadmap.js` printed SOON on a stage that had shipped three days before. **A rendered status is the one a reader sees, so it is the one to turn first** |
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
  tree links no stylesheet at all**: 115 of 115 in `ui-visual/` and 61 of 61 in `ui-kit/` link it,
  **0 of the 114 in `wireframes/` do**, and those 114 carry an inline `<style>` block each. Counted
  2026-08-12 at 104 and re-counted 2026-08-15, when `terms.html` was written and the grey tree
  stopped being one screen short of the tree it decides. The sentence here said "every screen" until then, and the folder file it contradicted
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
  a stand built by walking screens would show one grey oval and call it the component. **61 of 61 pages written**, one route in `_nav.js`, 0 generators and 0 gates. **The panel computes the tally from `_nav.js` and this line was typed by hand, which is why it said 55 while 57 files stood on disk**: 2 entry pages, 6 foundations, 4 shelves, 14 atoms, 16 molecules, 13 organisms, 6 patterns, re-counted 2026-08-18 when `why.html` joined `overview.html` as the second page belonging to no group and the registry stopped starting its tally at a typed 1, and before that 2026-08-16 by listing `ui-kit/*.html` and by parsing the registry, and the two agree. It was 57 and five foundations until then: `motion.html` arrived with the Animation stage on 2026-08-15 as the SIXTH foundation and this line went on saying five, and `search.html` is the thirteenth atom, written 2026-08-16 for a control the IA had deferred, with `crumb.html` the FOURTEENTH later the same day for the opposite reason: the IA had DECIDED a trail on six page types and the product rendered none, and the component went onto three of the six because the other three already carry their trail as the category nav and a fourth control made of the same five words is what the critique had just counted three of. It was 54 until 2026-08-11, when three pages landed the same day: `logo` with the rename to Yonder, `platehead` by backlog 108, and `responsive.html`, the FIFTH foundation, which is the page every enumeration in this repository was still leaving out. And it had been 55 before that until `account` was deleted on 2026-08-08, a component whose whole stylesheet was a face nothing wore.

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
- **AN INSTRUMENT THAT CHANGES THE PAGE HAS TO WAIT FOR THE PAGE IT CHANGED, AND THIS SYSTEM MOVES
  NOW.** Since Stage 11 the components carry real transitions, so **injecting a stylesheet to
  measure a before-and-after STARTS one**, and the computed value at t=0 is the value the page is
  leaving. A census of outcome colour on the feed reported `ground 22 -> 22, edge 0 -> 0, painted
  area identical` over an edit that had taken a tint off 32 buttons, because two
  `requestAnimationFrame`s into a 150ms transition the background is still the old one: the probe
  read the AFTER state twice and called it no change. Freeze `transition` and `animation` on
  everything FIRST, then inject, then read, and the same census gives **ground 54 -> 22, edge 32 ->
  0, and 220,689 square pixels of outcome colour down to 18,025**. The same freeze the
  before-and-after rule above already demands for entrance animation is now required for any probe
  that writes CSS, which is most of them. **Two themes are the same trap in a different place**:
  these screens boot their theme from `localStorage`, and the boot script REMOVES `data-theme` when
  the key is absent, so setting the attribute is not setting the theme. A whole sweep came back with
  daylight identical to the Vault, on every value, and passed its own colour control. **Every
  theme-aware reading gets a theme control: the page ground has to differ between the two runs, or
  the run is one theme measured twice.**
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
  true thing and every number in this repository has to say which**: `ui-visual/` holds 115
  documents, 114 of them screens, and `overview.html` is the index of the tree rather than a screen
  in it. It was 106 and 105 until 2026-08-16, when the three search screens landed in both trees,
  and 109 and 108 until 2026-08-17, when `event-detail-bet-ready.html` landed in both trees with
  backlog 185, and 110 and 109 until 2026-08-18, when the four static content pages the IA had
  registered and nobody had built arrived in both trees at once. **This sentence said 109 and 108 while the bullet above it already said 110 of 110**,
  which is what a count written twice does even inside one file that is loaded whole.
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
- **AN EMULATED ENVIRONMENT HAS DEFAULTS, AND A DEFAULT IS A VALUE: A MEDIA QUERY THE PRODUCT DEPENDS
  ON CAN BE SWITCHED OFF BY THE HARNESS AND NOTHING FAILS.** `base.css` puts the whole 44px touch
  floor inside `@media(pointer:coarse)`, and **a headless browser is `pointer:fine`**, so every
  tap-target sweep taken here without `hasTouch` was measuring a product with the floor turned off.
  It reported the header controls at 36x36 and 32x32, under the number `tokens.css` cites, and each
  one was a rule that was present, correct and not applying. With `hasTouch` and `isMobile` set and
  `matchMedia('(pointer:coarse)').matches` asserted IN THE PAGE before the sweep, the floor applies
  and the real number is **190 of 496 targets under 44x44 over 8 screens, 176 of them one family**:
  the footer's bare `<a>` links at 36x25, which the floor's named list never included. The defect is
  a quarter of the size the broken instrument reported and it is somewhere else entirely. **The twin
  of "a missing value is a value": assert that the branch you are measuring is the branch that is
  on.** The same class covers `prefers-reduced-motion`, `prefers-color-scheme`, `forced-colors` and
  the theme attribute this file already warns about.
- **CONTRAST IS A PROPERTY OF THE THING THAT IDENTIFIES THE CONTROL, NOT OF EVERY EDGE IT HAS, AND
  MEASURING EVERY EDGE MANUFACTURES A DEFECT LIST.** A census of 46 interactive families on 18
  screens, both themes, both engines, reported **43 of 46 under 3:1** on fill-or-border and read like
  a system-wide accessibility failure. **24 of the 43 have no fill and no border at all**: they are
  text links, and 1.4.11 asks 3:1 of the visual information *required* to identify a control, which
  for a link is its words. For the rest the mark or the label does the identifying, and measured from
  the render: bordered icon controls **8.44 Vault / 5.38 Daylight**, `summary` 9.43 / 17.97, the card
  YES 8.01 / 7.69, the amount chip 12.01 / 15.78, the bare bookmark 6.73 / 4.32. **The quiet edge is
  the Vault material and it was never the identification.** `components/tokens.css` had already drawn
  this line beside `--border-field` and written the reason, and a field is in that role precisely
  because it has neither a glyph nor a label. The change was authorised and is not made: it would
  have repainted 108 screens in both themes to satisfy a criterion already satisfied. **Before
  raising a contrast number, name the thing whose contrast is doing the work.**
- **A SCREENSHOT CLIP IS IN PAGE COORDINATES AND `getBoundingClientRect()` IS IN VIEWPORT
  COORDINATES, SO A CLIP TAKEN AFTER A SCROLL SAMPLES SOMEWHERE ELSE AND RETURNS PLAUSIBLE COLOURS
  FROM IT.** This is how the pass above nearly published its own opposite: `.icon-btn-bare` read
  **1.24 in the Vault and 2.23 in Daylight**, both under the criterion, and both were a capture that
  contained no glyph at all. **An empty capture reads exactly like a mark identical to its ground**,
  which is a contrast failure that cannot be told from a real one by looking at the number. Use the
  element's own `screenshot()` rather than a page clip, and confirm the element is in view. **What
  caught it was the positive control**: a brass Confirm button that did not come back brass. Sample
  the same glyph from a second element of the same class and the true numbers appear, 6.73 and 4.32.
  **Every paint-sampled contrast figure gets a control whose colour is known before any of the
  figures are believed.** And a fourth reading in the same hour failed the other way: screenshotting
  the GLYPH's own box and taking its median as the ground measures the glyph against **its own
  antialiasing**, which returned 2.05 to 3.42 for marks that are 3.20 to 8.56 against the card they
  stand on. **The right shape is narrower than it looks: sample only to prove the token renders as
  declared, then do the arithmetic on computed values.** Here the painted colour equalled the
  computed colour on every row, `[164,157,143]` for `--icon-quiet` and `[215,172,83]` for
  `--icon-brass`, at which point sampling has done its whole job and any further pixel statistic is
  a new way to be wrong.
- **THE PRODUCT ON AN OVERLAY SCREEN IS THE DEVICE PLUS THE OPEN DIALOG, AND A CLOSED STATE IS NOT A
  MISSING STATE.** Two findings in one run, both of them would have shipped. Scoping a probe to
  `.device` reported **0 `<h1>` on five screens**, because `deposit`, `sign-in`, `win`, `loss` and
  `deposit-error-card` are the feed with a `<dialog>` over it and the dialog sits OUTSIDE `.device`:
  all five have their heading. And the same scope reported the money breakdown as desktop-only,
  because at 390 the panel computes `display:none` and the phone uses a sheet that a static file
  ships CLOSED; forced open it carries Fee $0.08, Total to pay $5.08 and Potential payout $13.16,
  identical to the desktop panel. **A third in the same run was one word wide**: `innerText` ran the
  AMOUNT label into the balance chip beside it and produced "AMOUNT $42.00" over figures computed on
  $5, which read as the one input nothing reads. The field is `value="5.00"` and $42.00 is the cash
  balance. **Read what the container excludes before believing what the probe counted, and open the
  state before calling it absent.** **AND THE INVERSE COST A WHOLE BACKLOG ROW**: a closed state can
  report a box that paints nothing. `getBoundingClientRect()` inside a shut `<details>` returned
  38 x 505 on three grey pages and a row was filed on it, while `checkVisibility()` read **false**
  and `elementFromPoint` at that box's own centre landed on the page behind. **The real defect was
  in the state nobody opened**: forced open, those three put the dropdown at `position:static` and
  took the header from **50 to 236 at 390 and 60 to 222 at 1280**. `getBoundingClientRect` is not a
  visibility test, `checkVisibility()` is, and a control's defect usually lives in the state a sweep
  never enters.
- **A MOVEMENT NAMES ITS JOB BEFORE IT IS WRITTEN, AND THERE ARE THREE JOBS.** A response, a control
  answering a finger. An arrival, an element saying it is here. A status, a process still running.
  A moment for which none of the three can be named does not enter the register and never gets a
  movement, which is the same rule that throws an orphan feature out of a To-Be map. Motion lives in
  a token, a component or a pattern; `transition`, `animation` and `@keyframes` may not stand in a
  screen file, exactly as `@media` may not. **The stage that wrote this found its own most expensive
  trap already shut and unwritten: 0 of the 106 documents in `ui-visual/` carried a movement of their
  own**, because the rollout it was meant to protect had already happened.
- **AN INSTRUMENT THAT CANNOT FAIL IS NOT AN INSTRUMENT, AND THE ONE THIS REPOSITORY HAD FOR REDUCED
  MOTION COULD NOT.** `base.css` carried `*,*::before,*::after{transition-duration:.01ms!important}`
  under `prefers-reduced-motion`, and under `!important` on `*` a component that reads no token is
  indistinguishable from one that reads every token. With it in place the sweep counted 6,555 moving
  elements normally and **115,028** under the setting, the whole DOM taking a duration from one rule,
  and reported 0 defects out of 230,056 rows. Taken off, with a positive control proving the probe
  could see a rule that does not obey, the same 163 documents gave 1,392 offending elements, **0 of
  them in the system and every one of them in the stand**. The net is deleted rather than restored:
  its only argument left was code that does not exist yet, and this repository already refuses to pay
  rent on a decision nobody has taken. **The twin of "a reading that does not move when the input
  moves": a reading that cannot come back red is a reading of the guard, not of the thing.**
- **A CONVENTION WITH NO READER IS A CONVENTION THAT ONE SCREEN WILL NOT OBEY, AND IT WILL BE THE
  BUSIEST ONE.** `wireframes/_conventions.md` has said since the auth axis was written that the two
  auth states share a feed body and differ only in the header. Measured across the whole matrix on
  2026-08-16: **19 pairs of 20 obeyed it and the twentieth was `event-feed` against
  `event-feed-logged-out`**, which differed by the entire hero band, four cards, the sub-filter and
  its twelve `data-cat` attributes, the load-more row, the SEO wrapper and the sub-category rail.
  **The cost was measured in pixels and it lands on the reader the block was written for**: "1,284
  events resolved on-chain" stood at y=846 on a phone for a signed-in reader and at **y=4,095 for a
  visitor**. Nothing read the rule, so nothing could report the one screen that broke it, and the
  screen that broke it is the one a person who has never signed in arrives on. **When a rule is
  stated over a SET, measure the set: 19 of 20 looks like compliance from any single file.**
- **A FACT THE PAGE RESTATES BELONGS BESIDE THE PAGE; A FACT THE PAGE NEVER DERIVES BELONGS IN ONE
  PLACE.** `ia/docs/pages/seo.md` specifies a whole document head per page type and the trees carried
  **0 of the five metadata classes on 217 documents**. The layer split on 2026-08-16 and the line is
  DRIFT rather than ownership. Meta tags are written once and never computed from the page, so 110
  copies would be 110 places to drift, and they stay in the IA; `{ROOT}` is `[?]` besides, so a
  canonical needs a domain nobody has chosen. **Structured data restates the visible page**, which
  makes it the one half that CAN disagree with what a reader sees, and disagreement is only
  measurable where both halves stand together: 59 painted documents carry an `@graph` whose every
  node is checked against the render, `name` against the `h1`, `ItemList` against the cards in order,
  `FAQPage` against the `<dt>` / `<dd>` text, `dateModified` against the date the page prints. **And
  a state may show less, never something different**: an empty feed carries no `ItemList` and a
  loading detail carries no schema at all, so a state's node set is a SUBSET of the success state's.
  The first check written asserted one URL, one shape, and flagged five families that were right:
  **that check encoded uniformity where the rule is truth.** The tell that neither tree owned this
  layer was in the one head element both of them do have: their `<title>` names the artefact, `UI
  Visual - Event Feed` and `Wireframe - Event Detail`, because each is a drawing with a label rather
  than a draft of a document.
- **EVERY INSTRUMENT HERE ASKS WHETHER A PAGE IS CORRECT AND NONE OF THEM ASKS WHETHER IT IS THE
  RIGHT PAGE.** Search shipped on 2026-08-16 through every sweep this file describes: 0 page errors,
  0 broken links, 0 sideways scroll, contrast clean in both themes on both engines, the touch floor
  asserted with the pointer coarse. **The user reported it the next day and the report was right.** A
  person tapped a magnifier and got a 5,661px document that was the feed they had just left, with the
  box they asked for as the FOURTH block on it at **y=221**, unfocused, with no `autofocus` in the
  file; the header of that page kept a 36px magnifier whose `href` was the page it stood on, on all
  three search screens, so on the results page it was a control that discarded your query to take you
  where you already were. **Not one of those is a rendering defect, and that is the whole point**: a
  destination and a control are different shapes, and no computed value can tell you which one a
  moment needed. The fix put the field where the hand is, on a rung that is itself a measurement -
  the free middle of the header row is **69px at 640, 137 at 760, 277 at 900**, so it enters at RAIL
  and the mark opens a sheet below it. **Ask what a control is FOR before measuring whether it
  renders**, because the sweeps will pass either way. **And a number a surface prints about another
  document is a claim that has to be read**: the seam counts from the catalog and said "See all 3
  results" while the page it points at filtered a 12-card subset and printed 2.
- **EVERY INSTRUMENT HERE READS ONE DOCUMENT, AND A FACT THAT STANDS ON TWO DOCUMENTS IS OWNED BY
  NEITHER.** The rule above says no instrument asks whether a page is the RIGHT page. This is its
  twin and it is worse, because the page IS right: **three markets were Open on `active-bets.html`
  and WON on `active-bets-history.html`**, which are two tabs of one screen in one reader's account,
  and **868 renders over two engines at two widths reported zero**. The bell shipped "your bet
  resolved, YES won" on **73 of 109 painted screens and 56 of 108 grey ones**, `event-feed.html`
  among them, where the same market is the hero at **YES 38%**. `win.html` had the government
  shutting down on Feb 18 2027 and `loss.html` had the same market resolving NO on Feb 27 2027, and
  the history dated it to Jun 27. The profile listed one bet under **Past wins** and as **LOST** in
  the tab beside it, mixed a payout and a net figure in one unlabelled column, and marked WON a row
  that held NO on the outcome that won. **Six contradictions, one fixture set, and every single
  document valid on its own.** The check that finds this is not a renderer: it is a SET read across
  documents, keyed on the thing they share, and the key here is a market's IDENTITY, which is why
  the same market wearing three names made it unfindable - search knew one of the three. So: **name
  the entity, give it exactly one identity and one lifecycle, and read the whole set for
  disagreement**, the same way a rule stated over a set is measured over the set. `PRODUCT.md`
  carries the catalog size now, because a count with no denominator is what let this stand.
- **EVERY READING HERE RUNS ACROSS THE PAGE AND NONE OF THEM RUNS DOWN IT.** Horizontal scroll at
  fifty widths, contrast, tap targets, computed style, duplicate ids, dead links, and **not one
  instrument has ever read `scrollHeight`**. So a `<dialog>` missing its `[open]` put an **844px
  sheet after the footer on 108 of the 109 documents in `ui-visual/`**, doubling `404.html` from
  1,011 to 1,855, and every sweep in this file passed it: it throws no error, duplicates no id, adds
  no sideways scroll, and sits below the last element anything measures. **Reported by the user, on a
  screenshot, which is the third time in two days.** Document height is one number per render and it
  is the cheapest check in this repository: **take it, and take it in both trees**, because the grey
  tree read 0 on the same defect and the disagreement between them was the finding.
- **EVERY INSTRUMENT THIS REPOSITORY HAS FOR MOTION READS A DURATION, AND A CONTROL WITH NO
  TRANSITION CONTRIBUTES NO ROWS TO ONE.** The Animation stage took the transcript from the source
  and from the computed output, grouped every duration by role, found one role wearing four numbers
  and closed with `0 duration literals, 0 transition:all, one role one number`. All of it true, and
  **the whole method was pointed away from the defect**: a component that declares nothing has
  nothing to group. **Reported by the user, on a screenshot, which is the fourth time in three
  days.** The inverse question is one line - does the element that CHANGES a painted property carry
  that property in its own `transition-property` - and read from the browser's parsed rules crossed
  with computed style on every placement it gave **77 declarations and 20,864
  property-on-placement readings changing with nothing between the two states**, against 6 and 654
  after. **The repeating shape was an ATOM that wrote no response while some of its FACES wrote
  their own**, in three files: `chip` answered on two of five faces, `iconbtn` on four of six, and
  `.btn-provider` REPLACED the atom's list to add a `transform`, which is what a `transition`
  declaration does, so the sign-in buttons lost `color` and `box-shadow`. **A face that writes its
  own response is a face that can disagree with the next one**, and the fix is smaller than what it
  replaces: one declaration on the atom, the union of everything any face changes. **And a zero has
  to say which zero it is**: 12,238 readings are a state written into the document and never
  changed, where a transition is a rule that cannot render; 5,758 are the `text-decoration`
  shorthand resolving to `currentColor` on links that draw no line; 3,178 are the focus ring, which
  stays instant on purpose. **Ask what a census cannot see before believing what it counted.**
- **A LABEL THAT NAMES THE TOOL THAT WROTE SOMETHING IS NOT A LABEL, AND THE THING IT HIDES IS
  WHETHER ANYTHING IS MISSING.** The grey tree copies its chrome into 108 inline stylesheets and the
  copies AGREE: **390 of the 412 selectors that stand in 50 documents or more carry identical source
  text**, and the markup-to-CSS contract holds on every shared family with 0 documents carrying the
  markup and not the rules. What had no owner was the PLACE. Four of the region names in those files
  named the SCRIPT that wrote the rules - `chrome ported ... by port_chrome.py` and its kind - so a
  rule's home is wherever a script's cursor happened to be, and **the notification block sat under
  `How it works` in 61 documents and under the port's name in three, which are exactly the three
  that carried 7 of its 12 rules**. A file that has LOST a shared block and a file that KEEPS it
  somewhere else are indistinguishable to anything that reads names, which is why nothing saw it,
  and **the fix made the day before landed in a fourth region and reproduced the mechanism it was
  closing**. The same parse found 17 documents carrying a second `<style>` block and 13 carrying the
  same 12 rules twice. **A shared block now states its own numbers - `SHARED (N of 108, R rules)` -
  so a reduced copy contradicts its own header**, which is the only kind of check a tree that links
  nothing can carry, and it is read rather than run. **Name a region for its SUBJECT and put the
  count in it**; a name that records provenance tells the next reader nothing about what should be
  there.
- **A COUNT THAT IS TYPED IS A LIVE CLAIM, AND OWNERSHIP DOES NOT PROTECT A FILE FROM ITSELF.** The
  ownership rule above was stated and never measured over its own set. Measured 2026-08-18: **six
  files carry a live count of the trees or the system and five disagreed with the disk.** `README.md`
  was four documents short on the grey tree, four on the painted and three on the kit, and named 47
  components where the `@import` groups of `index.css` give 49. **Three of the six contradicted their
  own text.** This file said `110 of 110 in ui-visual/` in one bullet and `109 documents, 108 of them
  screens` in another; `components/CLAUDE.md` gave **three tree sizes in five lines**; and
  `ui-kit/_nav.js`, whose header is an argument that a list written twice drifts and which records
  that its own sentence has been corrected three times, typed **57** about the array of **60** three
  feet underneath it. **So a count is COMPUTED, or it is DATED and says the day; it is never typed as
  a live fact.** The kit's tally is the one the panel computes from `_nav.js`, and a `Stands on:` line
  is a reading of the product on the day somebody took it rather than a property of the component.
  **AND A STATUS IS THE SAME SHAPE WITH A READER ATTACHED, 2026-08-18.** Three files said a stage
  status lives in the README table and nowhere else, and the two places that RENDER it were
  unowned: `assets/_roadmap.js` printed **SOON on Animation across all 28 course documents for the
  three days after it shipped**, while `ui-kit/_nav.js` had every one of its flags right, 67 rows carrying one on the day and 69 today. **The claim
  protected the copy nobody looks at and left the copy everybody looks at to go stale**, which is
  the opposite of what it was for. A registry is not prose and cannot be deleted into one owner, so
  it is TURNED with the table, and a status that renders is turned first.
- **`scrollLeft` IS BLIND UNDER CHROMIUM MOBILE EMULATION, AND THE REPOSITORY'S ONE APPROVED
  SIDEWAYS-SCROLL PROBE IS BUILT ON IT.** This file already says `scrollWidth > clientWidth` is not
  a page that scrolls sideways, and the fix was to set `document.scrollingElement.scrollLeft = 9999`
  and read it back. **Under `isMobile:true` Chromium widens the layout viewport instead of
  scrolling**: a control page with a box 120px past the edge reads back **0** while `innerWidth`
  reads 440 against a `clientWidth` of 320. WebKit reads 120 either way. So the row that filed the
  logged-out header defect said "WebKit reads 2, Chromium reads 0 either way, which is an emulated
  default being a value" - **and the second half of that sentence was the instrument, not the
  engine.** Read with `scrollWidth` as well, both engines agree exactly: **36 painted documents 2px
  over at 320, not four and not WebKit-only.** The cause was neither: `@media(pointer:coarse)` takes
  the two icon marks from 32 to 44, the logged-out cluster asks 213.72 against 306, and the auth
  pair was being SHRUNK to pay for it, `Sign in` at 49.27 against a natural 63.97. **A probe gets
  one control per engine AND per emulation mode**, because the mode changes which reading exists,
  and a signal that cannot come back positive is not a signal.
- **A REGISTRY THAT NAMES EVERY DOCUMENT STILL DOES NOT KNOW WHERE THE READER IS, AND AN
  OFF-CANVAS PANEL IS INVISIBLE TO EVERY INSTRUMENT IN THIS FILE.** The rule above is about a
  count going stale; this is its twin about a POSITION, and it is worse, because the count at
  least renders. **Ten documents marked a different page as the one you are on**: the three search
  screens were built by copying the feed and the four Type 1 pages by copying `terms`, and the
  current-page marker came with the copy both times, in both trees. Separately the grey panel had
  no row for search at all, so two states were reachable from **0 of 113** grey documents while the
  painted sidebar had listed all three from day one. **Nothing here could have caught it**: both
  panels are off-canvas, so a panel that is confidently wrong adds no height, no sideways scroll,
  no duplicate id and no page error, and 908 renders over two engines passed it. The check is one
  line and it is a SET read, like the fixture contradictions and the auth pairs: **the row a
  document marks current has to be the document, and the two trees' registries have to name the
  same set.** **And read the instrument twice here, because this one is cheap to get wrong in both
  directions**: counting one marker instead of two called 85 grey documents defective when 82 were
  right, since a panel marks the parent SCREEN and the state row separately; then a grep wanting an
  href and its label on one line in one order reported 109 painted sidebars as missing four rows
  they already had, and believing it duplicated the block on all 109. **What caught that was
  reading the rendered panel.** A filed defect can be the same mistake: `ui-kit/betpanel.html` was
  on this list as a broken link for a string that stands inside `<code>` as escaped text.
- **AN IDLE CONTROL TAKEN FROM THE SOURCE IS NOT AN IDLE CONTROL, AND IT IS THE ONE CHECK THIS
  SYSTEM LEANS ON HARDEST.** Every folder here promises the same two-sided reading: no rule without a
  placement, no markup without a rule. Taken as a grep it is **wrong in three directions at once**:
  it cannot tell a declared script hook from dead markup, it cannot see the classes a page script
  writes at run time, and it misparses a selector inside a media block. Run that way it called five
  live hooks orphans and reported the real defect nowhere. **Read from the browser's PARSED rules
  crossed with the rendered DOM, over the paint and the stand together: 818 declared, 820 standing,
  and every zero on both sides says which zero it is** - five hooks declared as hooks, three runtime
  state classes the script writes. **The ninth was a slippage ladder in seven classes standing on 0
  of its component's 9 placements and on the SHELF**, so the component's page drew the sentence the
  product draws, the shelf drew the ladder, and the page's hero text described the ladder while the
  page under it showed the sentence: **three artefacts, three stories, each internally consistent.**
  And it was not an unplaced face, it was a face `PRODUCT.md` rules out by name and that the block's
  own shipped sentence contradicts, "the price is locked when you confirm, so it cannot move against
  you". **Before placing a face nobody wears, read what the product says about it; before deleting
  one, ask which zero it is.**
- **A CONTROL PAGE IS A PAGE, SO IT NEEDS THE SAME HEAD THE PRODUCT HAS.** A positive control built
  with `setContent` and no `<meta name="viewport">` gets a **980px layout viewport** from Chromium
  under `isMobile`, so a box 300px past a 390px window fits inside it and the control reports blind.
  The sweep behind it would have returned a clean zero over three trees. Mobile emulation turned an
  instrument off twice in one day here, this and `scrollLeft`. **Build the control out of the same
  material as the page, or it is measuring a different document.**
- **A COMPONENT CARRIES ITS FIRST PLACEMENT'S TYPE SCALE INTO ITS SECOND, AND NO INSTRUMENT HERE
  ASKS WHETHER A SIZE FITS THE READING MODE.** The user reported the five document pages as too
  narrow, and the cause was not a width. `.feed-seo` is the SEO plate from the foot of a card grid
  and its prose is `--text-13`, the size of a paragraph a reader passes on the way somewhere else.
  `about`, `terms`, `privacy`, `cookies` and `responsible-betting` reuse the component, so **the only
  five surfaces in this product that are nothing but prose read end to end were set in the smallest
  prose size the product has**, and at 13px the 60-to-75-character band the system already enforces
  caps the column at 409px on a 1220px frame. Every sweep passed: the line length was INSIDE the
  band, the contrast was clean, nothing scrolled sideways. **The band was doing its job and the job
  was the wrong size.** The fix costs nothing because `--measure` is in `ch` and a `ch` scales with
  the face: swept over all five documents at 13, 14 and 16px against six caps from 38 to 48ch, the
  longest full line is the SAME count down every size column, 62 / 66 / 69 / 71 / 73 / 77. So 16px
  bought 409px to 503px of column at 70 to 73 characters, and `DESIGN.md` gained a Document rank
  rather than a wider Body. **Ask what reading mode a placement is, not only whether it renders**,
  which is the same sentence as asking what a control is FOR before measuring whether it draws.
- **AN AUTO MARGIN MEANS ONE THING IN A BLOCK AND THE OPPOSITE ON A FLEX ITEM, AND THE SAME
  DECLARATION THEREFORE INVERTS WHEN A COMPONENT MOVES.** `.feed-seo` carries
  `max-width:800px;margin-left:auto;margin-right:auto`, which centres an 800px block in the 1400px
  feed. Dropped into `.read-col`, a `display:flex;flex-direction:column`, **the auto inline margin
  cancels the `align-items:stretch` default**: the item stops filling the line, shrink-wraps to its
  content and centres what is left. Measured at 1440: 417px at an offset of 91 inside a 600px
  column, so a legal document's headings, notices and body had **three left edges where its grey
  twin has one**, and the 417 was the paragraph's own `46ch` cap sizing the block that holds it.
  `seo-plate.css` already carried the override for the OTHER re-placement and the flex column never
  got one. **Column width is not among the seven differences `wireframes/_conventions.md` declares**,
  so this was drift by that document's own definition, and it took a cross-TREE read to see it: every
  instrument here reads one document. **A slot with ONE placement is a slot nobody can disagree
  with** - `.read-col` stood on `terms.html` alone from the day it was written, `ui-kit/patterns.html`
  filed it as two screens short of the pattern threshold, and the four documents that arrived on
  2026-08-18 both closed the row and exposed six widths on one page. **And a measure written twice is
  a measure written wrong**: `--container-doc` capped the column at 600 while `--measure` capped the
  prose at 409, which is one question answered at two numbers, and the 191px between them was a
  ragged edge nobody had decided. The token is deleted; the column carries the measure once.
- **A SPACE THE IA HAS DECLARED WILL NOT BE FILLED MUST NOT HAVE A BORDER DRAWN AROUND IT.**
  `ia/docs/blocks.md` says of the document pages that desktop promotes the contents to a sticky left
  column and **"the body keeps its 60 to 75 character measure rather than filling the remaining
  width"**. The paint read the first half and not the second: `.cat-layout` is a browse plate sized
  for a card grid that wants every pixel of the 1400 band, and on a document it drew a border, a
  bevel and a shadow around the part the IA had just said would go unused - at 1440 a 1140px plate
  holding a 214px rail and a 600px column, 144px between them and 153px of nothing to the right; at
  1600 `about.html` ran 600 of 1140. The plate fits the document now in both trees. **The same read
  turned the IA's own rung**: that paragraph said the contents is promoted at `min-width 760px`, and
  forcing the rail on at four widths gives the column **388px at 760, 428 at 800, 488 at 860 and its
  full 503 at 900** - so promoting at 760 would make the reading column NARROWER than it is at 640
  with no rail, which is the one thing the sentence beside it forbids. RAIL 900 is the first width at
  which both halves of the declaration are true at once. **A declaration has two halves and a build
  can satisfy one of them.**
- **No em dash**, anywhere, and **"anywhere" is the repository rather than the folders somebody
  remembered.** It was measured over six on 2026-08-16, read 0, and was published as "the only file
  that carries any" while `concept/brand-toolkit/` carried 35 across four files. Those are gone;
  `concept/old/pre-vault-3d/` keeps 3 and is frozen, the way `docs/kit-archive/` is. **A rule stated
  over a set is measured over the set**, which is the same sentence as the convention nineteen auth
  pairs of twenty obeyed.
