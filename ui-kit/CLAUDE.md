# ui-kit/ - the vitrine, rebuilt by hand 2026-08-07 to 2026-08-08

**All five steps are done and the plan below is the record of how, not a to-do list.** What is on the
stand today: **54 pages**, `_page.css`, `_nav.js`, and five reports in `docs/`.
**0 generators, 0 gates, 0 screenshots.** Every one of the 42 components placed on a level page
carries its live specimen in both themes, its classes, its declaration, its rule and its anti-rule.

**It was 55 and 43 on 2026-08-08 and it is 54 and 42 the same day.** `account` was walked, given a
level, and deleted within hours of each other: its whole stylesheet was the action bar's stone and
the three declarations `.flat` removed it with, and reading it on the rendered screens showed the
stone stood once of three placements in the shape of a dock on a product that does not dock. **A
component with no face left is not a component with a small stylesheet, it is a name.** Its page and
its writing are on `action-bar.html`. The panel's tally is computed from `_nav.js`, so it said 54 of
54 without anybody typing a number.

**A LEVEL IS A SHELF AND A COMPONENT IS A PAGE**, and the two answer different questions. Comparing
ten atoms against each other is what a level page is for and it keeps that job. Taking ONE apart
needs room a shelf does not have, because a shelf gives every component one specimen and one rule.

**This file said the opposite until 2026-08-08** - *a page per LEVEL, not a page per component,
because forty pages of one component each would be forty navigations to compare two chips* - and the
reason was right and was a reason for the shelf, not against the pages. Three components had been let
past it under a counted threshold, the three largest control families. **Two components killed that
threshold.** `toast` has FOUR placements on ONE screen and its page still carries where the boundary
with its own dismiss runs, why its error face is not red, and the fact that most of the component is
a behaviour no static page can draw. `toggle` has THREE, and **four of its five faces have no
placement in the product at all**: every `.toggle` in `ui-visual/` is `aria-checked="false"` and none
is disabled, so a stand built by walking screens would show one grey oval and call it the component.

**And a component page earns its place by finding something.** `button.html` found that the size ramp
has a step, `xs`, whose 105 placements render on no phone at all. `iconbtn.html` found that **one
face of eight moves when the pointer changes**, and that `.icon-btn-photo` is named for a ground it
does not stand on. `chip.html` found the mirror: **four of its five faces move**, and until
2026-08-08 only one did. `navitem.html` found **365 rows standing 33 tall with a finger on them**, on
an atom the one touch floor never named. `oddsbar.html` found that a source census reports **0
placements of a component the product wears 63 times**, because a script assigns the class.
`skeleton.html` corrected the fix's own comment: **0 marks of 482 draw at zero where their host is
rendered**, and the six that read 0x0 at 390 stand in a panel that is `display:none` there.
`toggle.html` found the four faces above. None of these was visible from a level page, because a
level page shows one specimen and every one of them is a fact about a set.

The kit shows the system to a person and it holds no product code. It holds 54 pages plus its
stylesheet and its registry: `overview.html`, which says what is happening, **all four foundation
pages** (`icons.html`, `colour.html`, `typography.html`, `geometry.html`), **a shelf per rung, all
four** (`vitrine.html` for the ten atoms, `molecules.html` for the fourteen at level 2,
`organisms.html` for the thirteen at level 3 and `patterns.html` for the six on the fourth rung), and
**ten atom pages, one per atom** (`button`, `iconbtn`, `chip`, `navitem`, `oddsbar`, `input`,
`yesno`, `toast`, `skeleton`, `toggle`) and **sixteen molecule pages** (`trustbar`, `market`,
`comments`, `notice`, `filters`, `bottomnav`, `catnav`, `related`, `state-block`, `position`,
`quick`, `options`, `seo-plate`, `loadmore`, `cookie-consent`, `toc`) and **thirteen organism pages**
(`header`, `footer`, `dialog`, `hiw-dialog`, `tabs`, `event-detail`, `betpanel`, `bets-table`,
`chart`, `card`, `hero`, `feed`, `profile`) and **six pattern pages** (`action-bar`, `browse-shell`,
`card-grid`, `detail-shell`, `list-head`, `position-list`). `_page.css` is the stand furniture they all share and
`_nav.js` is the route.

**Every component has a ROW whether or not it has a page.** `_nav.js` groups by level, the level page
is the first row of its own group (`All atoms`, `All molecules`), and a row with no page renders as a
`<span>` with a badge. There are no rows waiting any more, so the panel says **54 of 54** and drops its own
sentence about rows with no page: that sentence only exists while there IS one.

**The route is written once, in `_nav.js`, and a page declares no part of it**, not even its own
name. A page carries an empty `<aside class="sidebar" id="rmSidebar">` and loads the file; the rows,
the groups, the counts, the row that lights and the hub row on `overview.html` are all computed from
the one list. **This is not the generated `_nav.js` that was deleted on 2026-08-07.** That one was
written BY `_gen_component_pages.py`, which is why the archive states the rule it lived under out
loud, "`_nav.js` is rebuilt, not edited": a generated file cannot be corrected by hand, because the
next run puts it back. This one writes nothing and nothing writes it, which is the whole difference
between a machine and a piece of furniture. **The active row is computed from the file name and
never declared**, because a declared name is a copy and a copy drifts; **a row with no page is
visible**, as a `<span>` with the `.planned` badge, because a route that lists only what is finished
looks finished.

**It costs no CSS.** Every class it writes is `components/course-chrome.css`, which `index.css`
already imports and every kit page already loaded and used nothing of, and the 220px inset is
`base.css` insetting any body that contains `#rmSidebar`. One rule was added to the chrome for the
count on the right of a row, and one `.tk-jump span` to `_page.css` for the dashed unclickable chip.

**A swatch never carries a value.** `_page.css` holds one class per role and per primitive,
`.c-bg-plate{--sw:var(--bg-plate)}`, and the page wears the class. That is why there is not a single
`style=` attribute on `colour.html`: a colour written inline is a value this stylesheet cannot see,
and a colour page whose colours are invisible to the system is the exact thing being audited.

**The foundations are `colour`, `typography`, `geometry` and `icons`, one flat page each**, and they
are the visible half of step 3. A value may only change in that step, and it changes in the page and
in `components/` together.

## What was here and why it is not

65 generated pages, 18 Python scripts, 9 browser scripts, 41 build gates in 109 checks, a
state-capture instrument and 145 MB of screenshots. Deleted in one commit. The reason, in one
sentence: **the measurement had become a machine, so a one-line change to a stylesheet cost a
regeneration, a re-capture, 41 gates, 525 snapshots and an audit.** The full account is in
`../docs/decisions.md`, dated 2026-08-07, and the writing that was worth keeping is in
`../docs/kit-archive/`.

## The rules for the rebuild

- **A page is written by hand.** No generator, ever. If two pages share furniture, that is a rule in
  `_page.css`, not a script that stamps both.
- **A measurement is an act, not a machine.** Walk the screens, write down what was found, decide,
  keep the report. The moment a measurement becomes a permanent check, every later edit pays for it
  again.
- **A stand page may never style a product class.** `_page.css` is `.tk-*` only and grows one rule at
  a time, as a page actually needs it. The previous one reached 854 lines of which 800 painted
  classes nothing rendered.
- **The kit reads the system and never a copy of it.** A page links `../components/index.css`. If a
  specimen needs markup, the markup is the same markup the screen ships.
- **A cell that scrolls one axis scrolls both, and a specimen that takes no room in the flow
  disappears into it.** `.tk-theme-fig` declares only `overflow-x:auto`, for `.chip-nav`, and CSS
  resolves `visible` to `auto` on the other axis whenever one axis scrolls: the cell computes
  `auto / auto`. `.filter-panel` is `position:absolute`, so the cell measured itself against the
  `<summary>` alone at 67px while the open menu needs 213, and **146px was scrolled out of sight
  with a scrollbar as the only sign**. A section titled "the menu, OPEN" showed a summary and 21px
  of panel. It is pinned static on the stand now, the same bargain `.tk-dlg` makes, and one thing
  differs from the product, the position.
- **Finish the animations before reading a box, or the page reports a defect it does not have.** The
  same sweep flagged five more clipped cells on `betpanel` and `organisms`. Four candidate fixes
  moved the number by nothing, and the readings would not repeat: 316, then 279, then 254, then 242
  for one cell. With `getAnimations().forEach(a => a.finish())` before the read, `scrollHeight` goes
  681 to 402 against a `clientHeight` of 402, and **6 clipped figures across the kit become 0**. The
  dialog specimens were still animating in. **An unstable number is the instrument telling you what
  it is measuring.**
- **A cell that is empty on purpose carries the component's OWN number, and the number lives in the
  class name.** `.tk-gone.tk-above-640` and `.tk-gone.tk-below-760` are the two, and they replaced a
  pair written at 900px, which is a real breakpoint in this system belonging to five other
  components. **A borrowed number reads exactly like the right one**, so it stood for a day beside a
  bar that goes at 640 and a panel that arrives at 760: 260px of silently empty cell on
  `molecules.html`, and 139px on `vitrine.html` where the sentence said "not rendered below 900px"
  next to a rendered panel. And the two numbers are not mirrors: `min-width:640` HIDES the bar so the
  label starts AT 640, `min-width:760` SHOWS the panel so the label stops at 759. Written as the
  obvious 641/759 pair it left a one pixel hole. **Read the boundary, not the middle.**
- **A stand shows a component at ONE width and the component decides at which width it exists**, so a
  specimen can be `display:none` while the page around it looks finished. Six figures on three pages
  drew nothing and three of them were found only by counting painted descendants: a page that says
  "0x0 at 1280" two lines under an empty plate has measured the thing and not carried the measurement
  to the specimen. And the mirror of it: `button.html`'s ghost wore `.hiw-btn` for fidelity, a class
  with **one declaration in the whole system and no face**, `display:none` below 640, so the one
  emphasis of five a reader at 390 could not see was the one the section was about. **A placement is
  not a face.**
- **A caption is prose, and prose in an `auto` grid column eats its neighbour.** One 117-character
  line added to the anatomy figcaption measured 601px on one line, took the whole column, and left
  `.tk-anat` computing `601px 0px`, so the steps beside it stood 92px past the page **from 761 to
  about 1025 and nowhere else**: below 760 the stacking rule hides it and above 1100 there is room.
  The page had been verified at 390 and 1280, the two widths either side of the band. **Two widths
  is not a responsive reading**; read the boundaries the system actually declares.
- **A page carries states, in both themes, side by side.** That is the whole reason this vitrine
  exists rather than a Figma frame: a hover, a press and a focus ring are things a person raises with
  a pointer and a Tab. Each `.tk-theme-fig` carries its own `data-theme`, so both themes resolve in
  one document with no screenshots and no switching.

## The plan, in order

1. **Census.** Five anchor screens with their states, walked in a browser at 390 and 1280 in both
   themes, computed values rather than written rules. Output: `docs/census.md`.
2. **Levels.** Atom, molecule, organism declared once with a reason each. Output: `docs/inventory.md`.
2.5 **The vitrine, atoms.** DONE 2026-08-07, `vitrine.html`. Built BEFORE the consolidation on
   purpose: it is the picture of the system to compare the next pass against, and a change to a
   value that nobody can look at is a diff rather than a decision. It found two things the census
   and the inventory both missed, because both read markup and this one renders it: **the unscoped
   `.amount-input` takes its ground and its ink from the User Agent and shows as a white box in the
   dark theme**, and **the card odds bar exists in no screen's markup at all**, being written by a
   page script at run time, which is where its 213 uses came from.
3. **Consolidation. DONE 2026-08-08, `docs/consolidation.md`.** The four foundation pages are
   `icons.html`, `colour.html`, `typography.html` and `geometry.html`, all done, and 3e is the one
   pass where a value was allowed to change. What changed: the **import order**, nine files, proved
   inert rather than compared (59 file pairs flipped, 2,131 same-property same-specificity
   candidates, **0 elements matched by both halves of any of them** over 26 screens); **148 borders**
   now read `--hairline`, which was declared and used ten times against 148 literals; ten
   ladder-step literals; **`--weight-regular:400`**, the weight 192 of 260 elements render at and the
   only step the ramp never named; **eight tracking tokens** over 61 declarations, 14 values moved,
   none by more than .02em, 0 text clipped; **fonts 18 files and 373 KB to 8 and 131 KB**, verified
   by painted-pixel counts identical on all twelve weights; and **37 dead gate and script references
   in 20 files**, each now naming what was found rather than what found it.

   **The first instrument was useless and that is written down.** A whole-page computed-style hash
   over 68 renders reported **45 of 68 different when run twice with no change at all**, because the
   screens carry scripts that write at run time. A before-and-after needs an instrument that returns
   the same answer twice; that one did not, and it was replaced by a static proof for the reorder
   and by narrow per-axis measurements for the values.

   **What was left alone, with the reason**: the icon set (a redrawing, not a value), control height
   (a change to how every control is written), the brass ladder in daylight (a design decision), and
   the 81 layout dimensions (Responsive's question). The two theme-hole candidates `colour.html`
   named turned out **not** to be holes, and the page is corrected rather than the file.
4. **The pages, by level.** A live specimen, its states in both themes, its classes, its rule and
   its anti-rule. **4a atoms is `vitrine.html`** (done as step 2.5, ten atoms, 50 faces). **4b
   molecules is DONE 2026-08-08, `molecules.html`**: fourteen at level 2, 36 theme pairs, the real
   markup the screens ship. Two of the fourteen were filed as atoms and hold their own named parts,
   which is the case the declaration exists for. Three more (`account`, `cookie-consent`, `toc`)
   stand on no anchor screen and are marked **unmeasured** rather than given a level. **4c organisms
   is DONE 2026-08-08, `organisms.html`**: thirteen at level 3, twelve measured and `profile`
   unmeasured, the themes stacked rather than side by side because a header cut to 430px is not a
   header.

   **4c found the thing a level page exists to find, and it is a system defect rather than a stand
   problem. NINE DECLARATIONS IN THE SYSTEM ARE KEYED TO A DOCUMENT-UNIQUE ID**, and two components
   therefore cannot be placed twice in one document by anybody. `tabs.css` writes six rules of the
   shape `#edtab-comments:checked ~ .ed-panel-comments`, over ten ids, so the event tab set and the
   profile tab set work once per document; `hero.css` writes `.hf-area{fill:url(#hfyes)}`, so the
   hero chart takes its gradient from whichever `#hfyes` the document defines first. The one in
   `base.css` is `#rmSidebar` and it is correct. **Measured over the 106 painted screens: 0 of the 13
   ids appears more than once, so nothing is broken today** and nothing ever asked until a stand
   tried to show a component twice. Both are drawn **once, on purpose, with the reason in the empty
   cell**, because a stand that quietly shows a component painting with another copy's values is
   worse than one that says it cannot. Backlog 45.

   **A dialog is the one specimen on the kit that is not exactly what the product renders**, and the
   page says so. In the product it is `showModal()` and the top layer: fixed, centred, over a
   backdrop, one per document. Four on a page cannot do that, so the stand uses the plain `open`
   attribute and `.tk-dlg` pins it static. **Exactly two things differ, the position and the
   backdrop.**
   **4d patterns is DONE 2026-08-08, `patterns.html`**, and it is a page about a measurement rather
   than about a specimen, because the rung has almost nothing to look at. **The contract holds where
   it counts: 59 declarations across the six files, 16 properties, and not one of them is a colour, a
   face, a border or a surface.** Every property is an arrangement. Five of seven screen counts in
   the file headers are exact and two are one screen light, because they were typed when the painted
   tree was 105 screens and it is 106; that is the price of the rule that a measurement is an act,
   and it is one screen against the seven days the machine cost.

   **What it found: a prose claim with no reader goes stale.** Each pattern file opens with an
   `Assembled from` line and nothing checks it. Read from the screens instead, **two of the six are
   wrong**: `browse-shell` names `feed`, and `main.feed` is its PARENT (line 361 against line 469 on
   `event-feed.html`), which is the level arithmetic's blind spot written down by hand;
   `position-list` names `profile`, and the record block's classes moved to `position.css` on
   2026-08-03 in the pass that fixed five misfiled classes. And **`.read-col` is a slot in a pattern
   file standing on ONE screen**, two short of the threshold the rung exists to enforce, because the
   argument for WHERE the rule goes was answered as if it were the argument for WHETHER it exists
   yet. Backlog 46.

   **A third component whose visible content is not in its markup.** The browse shell's rail ships as
   `<nav class="subcat" id="subcatRail" hidden></nav>` and a page script fills it. After the card's
   odds bar and the chart's polyline, that is three, and all three were found by putting the thing on
   a stand rather than by reading a file.
5. **One audit run, as a report. DONE 2026-08-08, `docs/audit.md`.** 115 documents at two widths in
   two themes, **460 renders**: contrast, overflow, focus, accessible names, alt, duplicate ids,
   controls the User Agent is still painting, links and touch targets.

   **It found six defects in itself and one in the product, and that ratio is the report.** Three of
   the six would have been believed: **434** daylight contrast failures (the batch resolved on
   `onload` OR a 900ms timeout, whichever came first, so slow pages were measured mid-load; the same
   button measures 13.93:1 when the load is awaited), **212** overflows (a closed `<details>` puts
   its content in `::details-content` with `content-visibility:hidden`, so the child has a box, a
   computed `display:block` and is never painted), and **14,377** undersized targets (the course
   panel's own rows, which are chrome and not the product). The other three: a `feTurbulence` noise
   texture is not a gradient and left 42 per cent of one page unmeasured; text at `font-size:0` is a
   placeholder; and the CSSOM found **0** `:focus-visible` rules because `index.css` is nothing but
   `@import` and an imported sheet's rules live on `.styleSheet.cssRules`.

   **What held.** Contrast **0 failures in the product** in either theme at either width, over 29,929
   and 29,984 text elements per pass, with **0 unmeasured**. Overflow **0**, page scroll **0** on all
   115. Focus is **one universal rule** in `base.css` and 56 of 56 focusables inside `.app-case` take
   the ring, with **0** of the system's 18 `:focus-visible` selectors removing one. Names **0**, alt
   **0**, duplicated ids **0**. Links **0 broken** of 15,880.

   **The one product finding: the project's own 44px touch floor is not what the system builds to.**
   WCAG 2.5.8 AA is met (2,692 of 2,709 clear 24x24), and **1,787 of 2,709 miss 44x44**, dominated by
   a 38px chip on 530 elements. It is backlog 40's question in another form and it is filed pointing
   at it. Backlog 47, 48, 49.

   **CORRECTED THE SAME DAY, AND THE COUNT IS EIGHT, NOT SIX. The one product finding was the eighth
   defect in the instrument: the touch pass measured the product with a mouse.** The 44px floor is
   bound to `@media(pointer:coarse)` and has been since step 7, six component files carried a coarse
   block saying so, and headless Chromium reports `pointer:fine` with `maxTouchPoints:0`. Nothing in
   the run asserted a pointer, so all 460 renders read the 36px branch. With touch emulation on and
   `matchMedia('(pointer:coarse)')` asserted true before every read: **262 short, not 1,787.**

   **It is a worse defect than the load race, and that is the reason it is written here as well as in
   the report.** The race read the page at the wrong TIME and would eventually have been caught by a
   re-run; this read it on the wrong DEVICE, and a mouse never becomes a finger. **An audit that
   measures a criterion the system answers conditionally has to assert the condition**, because an
   unasserted condition is a value the instrument picked without saying so, and this repository
   already knows that a missing value is a value. It knew it about the page and not about the
   instrument.

   **What the correction found instead was real and smaller: the floor was written six times and
   every copy named a list.** `chip.css` named two of five chips, `tabs.css` two of three tab faces,
   and `.market-head`, `.rules-tab` and `.toc-link` were named by nobody. It is one rule in
   `components/base.css` now, beside the focus ring, keyed to the family, carrying the icon button's
   four exclusions unchanged. **262 to 68 at 390 and 542 to 98 at 1280, the fine branch unmoved at
   1,028 both ways, 0 pages gaining horizontal scroll.** Backlog 49 closed, 50 and 51 opened.

The five anchors: event feed, event detail, active bets, deposit, sign in, with their loading, empty,
error and logged-out variants. 41 screens of the 106.
