# The defect table

Step 8 of this stage is the check, and this is its first half: not a list of findings, but the map
of **where a finding could still be hiding**. The second half is the hunt, and it only has to run
where this table says nothing is holding.

**Why the first column is a gate and not a category.** The taxonomy this step inherits was written
for a project with no build check: eighteen classes of defect, each to be looked for by hand, on
every screen. This project has **37 gates over 90 checks**, and a green gate is not an audit result,
it is a **proof**. A class of defect covered by a gate does not need a person to go and look: it
needs a person to confirm the gate asks the right question, once, and then the answer holds on every
commit rather than on the day somebody checked. Running a manual pass over a gated class is not
thoroughness, it is a second, worse instrument reporting on the same thing.

So every row here is a class of defect, and the first column is what stands between the product and
that class today. Three statuses, and the third is the only one that costs time:

| status | meaning | what step 8 does with it |
|---|---|---|
| **PROVEN** | a gate in `ui-kit/_check_kit.py` asks it and is green | confirm the question is the right one; do not go looking |
| **MEASURED** | a browser instrument asks it and can exit 1, but it is not in the 1.5-second build | re-run it, record the number, and say it is not gated |
| **OPEN** | nothing asks it | **this is the hunt** |

The split of the instruments is deliberate and is written down in `ui-kit/_verify/README.md`:
`_check_kit.py` is Python that runs anywhere in about a second and a half, so everything in it runs
on every commit; `audit.cjs` needs a browser, a served tree and about a minute, so it runs when
asked. A check only some machines can run is a check nobody runs, which is why the two are separate
and why MEASURED is its own status rather than being counted as covered.

No em dash.

---

## The table

### PROVEN by a gate

| # | Class of defect | Gate | The question it actually asks |
|---|---|---|---|
| 1 | A declared class the product never wears | **30** | 105 painted screens as the corpus, 12 declared exceptions each with a reason, and an idle exception fails as loudly as an undeclared class |
| 2 | A selector with no markup anywhere | **14** | the reverse of 30, over every tree |
| 3 | A raw scale value in a component | **12** | plus: the stacking order is named, every consumer of a rescale moved, a distance is not a size |
| 4 | A colour that skips its semantic role | **13** | a component may not read a colour primitive; every screen can switch theme; every frame follows |
| 5 | An orphan token, or a `var()` with nothing behind it | **11** | both directions |
| 6 | A rule written on the element | **9** | `style=` fails, except the three declared non-styling cases: a datum, the event photograph, a run-time value |
| 7 | A whole imported before its part | **23** | the order is COMPUTED from specimen containment, not typed; a pattern carries no colour |
| 8 | A component with no stand, or a stand with no page | **2, 8, 24** | and the specimen shows everything the component contains |
| 9 | A missing interaction state | **25** | both directions against `_levels.STATIC`, and a state is a token, not a value |
| 10 | A generated page that no longer matches its generator | **29** | every generator still runs, 141 pages compared, and a second author is declared |
| 11 | A state photograph that is older than what it shows | **31** | a hash of the declared sources, not a pixel comparison; and a component with states and no picture is declared in `_states.NOT_SHOT` with the selector and the reason |
| 11a | **A state photograph whose frame is smaller than its subject** | **31** | the pad is derived from the element in the state being shot, and what the frame managed is written into the manifest beside what it needed, so a crop fails the build without a browser. Three declared tight frames, each with a reason, and an idle one fails |
| 12 | An authored page that is fluent and wrong | **32** | it exists or is declared absent; every section answered; every class and path it names is real; the anti-rule names a component and says Seen or Predicted |
| 13 | The two screen trees disagreeing | **18** | inside `<main>`, the header, the bottom nav, the footer and an invoked sheet, paired through `_twins.py`, with the six declared layer differences |
| 14 | One dialog with two markups | **19** | the canonical body is the one in `ui-visual/event-feed.html` |
| 15 | A heading level invented on a screen | **15** | one `<h1>`, no skipped level, read in BOTH trees |
| 16 | A path that goes nowhere | **4, 8, 21** | relative paths, registry pages, sidebar links, cross references, and no link into a raw `.md` |
| 17 | A request that leaves the repo before consent | **20** | no font host, every face committed, every page reaches them |
| 18 | An icon reference with no symbol | **3, 17** | and every mark is on the sheet |
| 19 | A rule of use with no source or no owner | **26** | and it is on the page of every component it names, in both directions |
| 20 | A pattern that is not one | **27** | three screens or it is a candidate; a page and a scene for each |
| 21 | A guide that invents its own sources | **28** | names every source, invents none, and is current |
| 22 | An em dash | **7** | the whole repo |
| 23 | A product edit that never got committed | **1** | `components/`, `wireframes/` and `ui-visual/` against HEAD, so a green build is a green build of what is actually in the tree |
| 23a | **A trader term where a person acts** | **33** | 13 terms crossed with 19 kinds of acting place, over both trees. Prose is not read at all, which is the invariant: the ban is about PLACE. Two declared exemptions, each a phrase rather than a location, and an idle one fails |
| 23b | **A document row that does not match the product** | **34** | the inventory's three computed columns are rebuilt and compared, and the hand-written half of the map fails on a row that matches nothing |
| 23c | **Markdown that survived the render** | **35** | every generated page, not the seven documents, because `inline()` is imported by the component and pattern generators too. Two marks that cannot be anything else on a rendered page: `](`, which only comes out of a link, and `**`, which only comes out of an emphasis that did not fire. It is here rather than under gate 21 because gate 21 re-renders the document and compares, so a defect in the RENDERER is reproduced on both sides and reads as agreement. It asks the markup and not the text - `<code>` and `<pre>` are stripped first, because this row quotes both marks and turned the gate red on the page describing it - and all 104 marks that shipped were in running text, so the strip costs nothing. Declared exceptions are pages that show markdown outside a quotation, and there are none; an idle one fails |
| 23d | **A gallery that is an occurrence rather than a difference** | **36** | no two state groups of one component may be the same answer, read across all four states in BOTH themes out of what each picture was taken at. That is the same sentence as "one base set plus one named difference each", in the form that can be computed: gate 32 already binds one caption to one group in both directions, so counting captions against groups is a count compared with itself. Two more directions: a picture that belongs to no group (it found two in `tabs`), and the five components still holding the defect, declared with what they carry so the debt is a register rather than a silence, and an entry that no longer holds a duplicate fails as idle |
| 23e | **A markdown table row that is not a row** | **37** | every body row of every table in every markdown in the repository must have its own head's cell count. A defect of FORM, which is why nothing here asked: every other check asks about meaning, and a row that is not a row resolves, exists, and matches. Two backlog entries written on one line rendered as ONE row of **7 cells against a 3-column head**, so `S28` was not an item at all and a reference to it by number resolved as text and not as structure; the neighbour was **2 cells** where the head has 3, the same defect the other way. **The corpus is every markdown, on gate 7's argument, and it earned that immediately**: scanning only the documents that have a page found the one it was written for, scanning everything found seven more in two files nobody would have opened. A blank line ends a table, so a data row rendering as a second head is caught by the same read. Declared ragged rows carry the usual idle control and there are none |

**29 classes, and none of them needs a person to go and look.** What step 8 owes each of these is one
question: does the gate ask the right thing. Two of the 23 have a known answer to that already, and
both are recorded rather than assumed: gate 14 missed `.signin-lead` and `.delta .row` because each
selector has a real ancestor, and gate 1 masks the `<aside>`, which is why gate 22 exists.

### MEASURED, and not gated

| # | Class of defect | Instrument | Standing |
|---|---|---|---|
| 24 | Contrast under the floor | `audit.cjs` | **FIXED 2026-08-03.** The 378 were one defect: `oddsbar.css` put the FILL roles on 12px bold text. `--outcome-yes-text` / `--outcome-no-text` already existed, so the repair is two words and no token moved. Re-measured in a browser, both themes: `span.l-yes` daylight 2.62 -> **7.23**, `span.l-no` daylight 3.76 -> **7.57**, `span.l-no` graphite 4.35 -> **7.54**, `span.l-yes` graphite 6.23 -> **9.82**. `ui-kit/docs/backlog.md` S14 is closed and `ui-kit/docs/history.md` records why it is the run's best evidence for the semantic token level. **The row stays MEASURED and does not become PROVEN**: nothing gates it, and the reason the same defect stood through five stages is finding 42 below |
| 25 | A link with no rule behind it | `audit.cjs` | 992 links, every one inside a component that styles it; the one exception became S3. **Re-run 2026-08-03 after this step's edits: 0 findings** |
| 26 | Horizontal overflow | `audit.cjs` | **Re-run 2026-08-03: 0 findings over 424 renders.** Not gated, so this sentence is true of that run and of nothing later |
| 27 | A request that 404s | `audit.cjs` | **Re-run 2026-08-03: 0 findings over 424 renders**, same caveat |
| 28 | A pinned box taller than the window it is pinned to | `audit.cjs`, second pass at 640px | three rails found and fixed; what the fix left behind is S12 and S13. **Re-run 2026-08-03: 720 pinned boxes measured at 640px of window, 0 findings** |
| 29 | The focus ring at every tab stop | `audit.cjs --focus` | 18 tab stops on the document page, all measured |
| 30 | A painted screen that moved when the system changed | `snap.cjs` | 525 of 525 identical across the button merge; 84,836 boxes unmoved across the pattern extraction |

**Seven classes that are true as of the last run and not on any commit.** Step 8 owed these a re-run
and a number, not a search, and the re-run happened on 2026-08-03 after every edit this step made:

> `node ui-kit/_verify/audit.cjs --screens` - **106 pages, 2 themes, 2 widths = 424 renders. 0
> findings.** 720 pinned boxes measured at 640px of window; 660 elements unmeasurable through a blend
> or a filter and 380 painting no glyph at all, both counted apart rather than passed.

**And that sentence is written with the caveat row 42 exists for.** A zero from this instrument is
what stood in three documents fifteen times while 378 elements measured under the floor. What is
different now is not the instrument's word, it is that the one thing it used to be wrong about was
found by hand, fixed at the role, and re-measured element by element in the browser - `span.l-yes`
2.62 to 7.23 and `span.l-no` 3.76 to 7.57 in daylight, 4.35 to 7.54 and 6.23 to 9.82 on graphite.
The zero above is only as good as its next audit, and it is not gated, which is why it carries a
date and a corpus instead of a claim.

### OPEN: nothing asks these, and this is the hunt

| # | Class of defect | Where it is already known to bite | Why no gate |
|---|---|---|---|
| ~~31~~ | ~~**Copy against the voice contract**~~ **CLOSED: it is gate 33.** | ~~`docs/backlog.md` 29: five placements of a trader term~~ - all five rewritten by `wireframes/_generators/voice_reconcile.py`, 97 replacements on 22 files across both trees, second run 0. `voice/docs/microcopy.md` Step 28 | **The gate's own two-way proof found what the rule could not.** Reverting each of the five one at a time demanded a red for each, and two came back GREEN: `Holders` was not in the lexicon at all, because the list held `position` and not the person who has one, and `Liquidity` and `(AMM)` were invisible to the scanner because `finditer` does not overlap and an enclosing `<div>` had swallowed its own children. Both are fixed, all five now go red one at a time, and `voice.md` gained `holder`. **A checker that cannot fail on the defect it was written for is row 42 in a new costume** |
| ~~32~~ | ~~**A document row that does not match the product**~~ **CLOSED: it is gate 34.** | ~~S21: inventory L163, L155 and L97~~ - all three corrected, and the MECHANISM closed rather than the instances: `stems_for()` took the first dot-separated part of a selector, so `p.pos-status` resolved to the tag and fell through to the hand map | **And the idle control found eight more the moment it was switched on.** Eight of forty one hand-map rows matched nothing, every one in the same hand-written half both false cells came from, and the rebuilt table is byte-identical without them. What is deliberately NOT gated is named in the code: the `#f` column, where 38 of 54 findable rows disagree with a count, because the cells carry two different definitions. `ui-kit/docs/backlog.md` S23 |
| ~~33~~ | ~~**A class declared in the wrong file**~~ **DONE 2026-08-03.** | ~~`docs/backlog.md` 17: five classes~~ - 17 rules moved across five pairs of files. `components/index.css` rebuilt from the computed order, four files moved. **525 snapshots, 105 pages at three widths, 0 differ, 0 elements changed** | **Still no gate, and now there is a reason to say so out loud.** The ownership map was never wrong: `.grid-l` in `feed.css` WAS the file styling it with the fewest ancestors, which is why nothing could see it and why this took a person. What the move bought is smaller than a gate and better than nothing: `_levels.ORDER_BREAK` lost two of its four hand-written cycles, because both were made OF a misfiled class rather than of a real nesting. **A hand-written tie-break is now readable as a finding waiting to be closed**, which is the nearest thing to a check this class can have |
| 34 | **A component boundary nobody has drawn** | `docs/backlog.md` 16b, 16d, 18, 19 | `card` is a molecule and an organism, `notice` is six blocks, `position` is four things, `hiw-dialog` is two components on one vocabulary. Arithmetic can count them; only a person can split them |
| 35 | **Keyboard reachability** | `docs/backlog.md` 22 (the filter panel) and 23 (a multi-outcome row is a `<div>` that answers a click) | `audit.cjs --focus` walks the tab order and measures the RING; it does not ask whether everything operable is IN the order |
| 36 | **What a screen reader is told when something changes** | `docs/backlog.md` 24 and 25 (eight error blocks announced to nobody) | Nothing in the build reads ARIA |
| 37 | **A promise the product cannot keep** | `docs/backlog.md` 27 and 28: 16 dead footer destinations on 104 screens, 1,664 links into nowhere, 8 of them on no map at all | Gate 4 resolves relative paths; `href="#"` resolves fine. A destination that exists as a page and not as a plan is an IA question |
| 38 | **A shipped block that no document describes** | `docs/backlog.md` 26: the featured hero, in both trees and in no document | Gate 18 pairs the trees and both carry it, so agreement is not evidence |
| ~~39~~ | ~~**One shape declared more than once**~~ **DONE 2026-08-03.** | S16, S17 and now S18: `--line-brass-soft` folded into `--border-brass-hover` through `ui-kit/_rescale.py` `ROLE_RENAME`, 9 rewrites across 8 files, one token gone, no value edited | **Still found by reading and not by a check, and the fourth instance says what a check would have to ask.** Two roles with the same value in every theme are not automatically one role - `--result-won` and `--outcome-yes` are the same green on purpose, and `tokens.css` says so at both declarations. What made this one a duplicate is that both DESCRIPTIONS said the same job. A gate would have to compare intent, which is the class of thing gate 32 can only check the shape of |
| 40 | **Repo weight and tracked artefacts** | `ui-kit/docs/backlog.md` S22: 19 MB of screenshots in git, in a 62 MB pack | The `.gitignore` rule that was written for exactly this cannot untrack what predates it and names one extension |
| 41 | **A number in a document that nothing computes** | S21's L97 is the instance; the class is larger | `_fill_inventory.py` computes three columns of the inventory and the screens column is not one of them |
| 42 | **A recorded measurement that was false when it was written** | **Fifteen separate "0 below AA" claims**, in three documents: `docs/decisions.md` (8), `ui-kit/docs/history.md` (6) and `voice/docs/microcopy.md` (1), over corpora up to "420 page loads x 2 themes, 86,534 text pairs". `ui-kit/docs/backlog.md` S14 measures **378 elements below 4.5:1** and says explicitly "Pre-existing: measured identical at HEAD before this pass and after it", so the 378 were there on every one of those dates | Nothing checks a document against a measurement, and this one cannot be closed by editing: `history.md` and `decisions.md` are written once and never edited on purpose, so the correction has to be a LATER entry that names the false lines. **WHY THE ZERO SURVIVED FIFTEEN PRINTINGS, and it is a rule rather than an episode.** The zero was printed by an instrument carrying three bugs this repo had already found and written down: a regex reading the components of `color-mix(in oklab, ...)` as sRGB bytes, a print limit that stopped at six findings per render (32 of 48 renders hit it exactly), and `mix-blend-mode`, which no computed style can resolve. Nobody lied. **A broken instrument that reports a DEFECT gets caught, because somebody goes to look and finds the instrument lying. A broken instrument that reports ALL CLEAR is caught by nobody, because there is nothing to go and look at.** The most dangerous output of a broken check is not a false alarm, it is a clean bill of health, and this is the one asymmetry that decides where verification effort belongs. **The sweep behind the number:** 79 claims of the "nothing was found" form across the repo's markdown - 29 gated today and therefore still true by construction (em dash to gate 7, broken links to 4, 8 and 21), 18 about contrast, and 30 measured by a browser and gated by nothing, true as of their run and unknown today |

| ~~43~~ | ~~**The instrument crops the subject of its own photograph**~~ **DONE 2026-08-03, and it is now the third half of gate 31.** | Measured, then fixed, then re-measured. **36 of 790 state pictures were short**, and every one of them was a FOCUS picture - the single state whose entire subject is a ring drawn OUTSIDE the box, `--ring` 2px at 2px offset, 4px a side. The pad is now DERIVED from the element being photographed, in the state it is in: `extentAt()` reads the computed outline and every non-inset shadow and returns the four sides, offset + spread + blur/2 being where the paint stops. **Over all 790 pictures the widest answer in the whole tree is 4px**, and no shadow on any photographed element reaches outside it - a number worth having measured rather than assumed, because the static reading of the stylesheet says 90px and the elements that carry those plate shadows are not the ones being photographed. The row gap is 24, which is twice the 12 `shoot()` asks for, so the halving caps nothing; the specimen page gained the 12px edge it never had. **36 -> 6 -> 0 undeclared**, the last 3 groups declared in `_states.TIGHT` with a reason each and an idle control | **Two more instrument defects fell out of fixing it, and both are the same shape.** A frame that ran past the last pixel of the document took the whole run down: a bet sheet is `position:fixed`, so it is painted in the viewport and is not in the document's scroll extent at all. And the clip and `boxAt()` had never agreed on a coordinate system - `boxAt()` returns DOCUMENT coordinates and a clip without `fullPage` is measured against the VIEWPORT image, which was invisible for as long as every specimen was too short to scroll. Giving the page a 12px edge made one scroll, and the API refused. Proved both ways before it was changed: the same clip fails without `fullPage` at scroll 0 and at scroll 138, and succeeds with it at both. **The bands are the other half of the fix**: two themes as full-width rules inside the gallery rather than two rounded boxes of a third ground, because a state picture is already a frame and a theme is a condition, not a card |

| ~~44~~ | ~~**One button under five names, and the size is encoded in the name of a PLACE**~~ **MEASURED, DECIDED, AND DELIBERATELY NOT CONSOLIDATED, 2026-08-03.** | The measurement is in `ui-kit/docs/backlog.md` **S24**, in full, as the system's largest open structural item: 5 names, 3 axes, 30 rules of which **13 are reconciliation**, 4 of those existing only to put an axis back and 1 re-declaring the whole anatomy in 16 declarations. 64 shots where the axes say 22 | **The measurement is the decision, and it argues against doing it.** Three axes do not fit inside `components/button.css`: the position mechanism belongs to `patterns/action-bar.css` and the `width:100%` to a `state-block` context, so consolidating touches a pattern and two components - a refactor of the centre of the system on the step that closes it. And the right answer for emphasis is `.primary` in the MARKUP, which is frozen, so the system would gain axes its own markup cannot express. **Closing condition: with the markup thaw, not before.** What is paid instead is the PAGE: `ui-kit/button.html` now opens with the axis matrix (size x width x emphasis, one row per name, the borrowed cells in bold), so a person who came for a button leaves knowing which one rather than reading a list of five places. The 42 shots stay, and that is the trade |
| 45 | **Six icon-buttons, six files, and none of them is the button file** | Counted over both trees, a `<button>` whose whole content is a mark: `.icon-btn` 388 (`header.css`), `.sheet-close` 228 (`dialog.css`), `.hiw-close` 105 (`hiw-dialog.css`), `.bookmark-btn` 84 (`card.css`), `.ed-act` 27 (`event-detail.css`), `.toast-close` 4 (`toast.css`). **709 in the painted tree, six classes, six files, and `components/button.css` draws none of them.** That is `ui-kit/docs/backlog.md` S11 at family scale, and S11 was one file. **And the letter is not a toast problem.** `.toast-close` ships `<button class="toast-close">x</button>` at 24x24 with `font-size:12` and `line-height:none`, so a glyph with its own baseline sits where a mark should - 4 buttons on 1 screen. `.sheet-close` ships the SAME letter on **123 buttons across 105 screens**, and ships an inline SVG on 105 others: one class, two answers, and in the painted tree every bare `dialog.app-dialog` gets the letter while `signin-dialog` gets the mark. Both trees agree on every count, so gate 18 is quiet and correct | **None, and the reason is the shape of 42.** Gate 3 asks that no icon reference is dead and gate 17 that every mark is on the sheet; **a letter used as an icon passes both by not being an icon.** The check is green because there is nothing for it to look at, which is the same asymmetry as the false zero |
| 46 | **A link wrapped around a button, 2,448 times** | Found while measuring row 35's reachability. `<a href="..."><button type="button">YES</button></a>` is the shipped shape of every YES/NO on a feed card, and of the header's portfolio and favourites controls: **2,448 occurrences on 133 painted screens and 1,629 on 104 grey ones**, both trees agreeing. `<button>` is interactive content and the HTML content model forbids interactive content inside `<a>`; the two elements also carry different roles, so what a screen reader announces for the pair is not defined by anything. The largest single shape is the bare `<a href="..."><button type="button">` at 1,712, and the loudest is `<a href="..." aria-label="Favorites, see saved events"><button type="button" class="icon-btn" aria-label="Favorites">` - **two accessible names on one target**, 89 times | **None, and no gate can be written for it here.** Gate 4 resolves the href, gate 18 pairs the trees and they agree, and nothing in the build parses the HTML content model. It is markup, so under the twin contract it belongs to the grey tree first and is a Stage 12 handoff item rather than a Design System edit. Named here because it was measured here |
| 47 | **The ring reader measures the element that has focus, not the element the ring was moved to** | `ui-kit/_verify/browser.cjs` `ring()` reads `document.activeElement`, its `outlineColor`, and the ground under it. Two components in this system deliberately put the ring somewhere else, because the focused element is a hidden input: `tabs.css` maps `#edtab-*:focus-visible ~ .ed-tabbar label[for=...]` and `filters.css` now uses `label:has(input:focus-visible)`. In both, `base.css`'s universal `:focus-visible` still draws an outline on the hidden input itself - offscreen in one case, on a 1x1 transparent box in the other - so `ring()` returns `visible:true` and a ratio for a ring **no person can see**, and would return exactly that even if the label rule were deleted | **None, and it is the third instance of 42's shape in this run.** The instrument reports a clean result about the wrong object. Both ring placements in this repo were measured by hand instead, with the composite ground computed through the translucent brass wash: the tab labels at 8.71 and 7.14, the filter labels at 8.31/7.80 on graphite and 4.48/7.14 in daylight. A gate would have to ask "if this element's outline is invisible, is there another element that gained one" |
| 48 | **One idea done two ways in one file, and the way that already failed was left in place** | Found 2026-08-04 by re-capturing `tabs` under the extended face, which is the third verdict gate 36's pass allows for: a pair that differs by something it should not. `components/tabs.css` hides a CSS-only tab's radio TWICE, differently. Line 12 parks `.ed-tabradio` at `left:-9999px` (measured: a 13x13 box at x = -9941, opacity 1, pointer-events auto) and line 18 gives `.ptab-in` a 1x1 box at `opacity:0` with pointer-events none. The file's own comment says the first one painted the focus indicator off the left edge of the document and that the second was written so the ring lands in the right place and is then painted at zero alpha, **which is the same nothing**. So the second mechanism exists because the first one failed, and the first one is still there, one file away, waiting for the next `:focus-visible` rule somebody forgets to map by hand. **What the state pass keeps of them is two pictures of nothing**: a screenshot of a box 9941px outside the document and a screenshot of a 1x1 transparent box. Row 47 is the instrument half of the same story | **None, and this is what makes it a class rather than an instance.** A gate would have to ask whether two rules in one file are two answers to one question, which is intent. What is checkable is narrower and worth writing down as the closing condition: **one hiding idiom per repository**, declared once, and any second one fails. Nothing measures that today. The pair also does not merge under gate 36 and must not: the difference is real, it is just a difference nobody decided |

**Twelve open classes**, three of them found while fixing the others, and six struck: **31 and 32 are
now gates 33 and 34**, so they are proofs rather than a pass; **33 and 39 are done** - both by a
person, because both are judgements no checker could reach; and **43 is done and became a gate**,
which is the one of the five that closed in both ways at once. Five (34, 38, 42, 45 and 47)
still need a person, and 44 is struck a sixth way - measured, decided, and deliberately not paid; four (35, 36, 37, 46) belong to owners outside this stage, three of them already
assigned in `docs/backlog.md` and the fourth a markup question the twin contract sends to the grey
tree first; two (40, 41) are hygiene with a measured size and a decision still to take.

**35 and 36 moved while this was being written.** 35's blocker was `docs/backlog.md` 22, and it is
closed: the filter panel is reachable, measured before and after with a real Tab walk. 36 is
narrower than it was for the same reason - the panel's three radiogroups were `display:none`, so a
screen reader was told there was a group of options and then given **0 of them**; the accessibility
tree now carries **5 radios with their names and their checked state** where it carried none. What
remains under 36 is the form-error axis, which is markup and is `docs/backlog.md` 24 and 25.
**42, 43 and 47 are one shape seen three times** - a broken instrument reporting a clean result, once
in a document, once in a photograph and once about a focus ring nobody can see. That is the argument
for where the next pass looks: not at what the checks report, but at what they are looking at.

**Row 35 moved while this table was being written**, and it is the reason the "which gate catches it"
column is worth the trouble. Of the three controls it named, two were not defects: `.rules-panel` is
not a control at all (the control is `.rules-tab`, a real `<button>` on all 18 instances), and the
four `<span class="bp-side">` are skeleton placeholders on two loading screens, which must not be
focusable. The third, `.opt-row`, is a control on 2 of its 14 screens and **has a working keyboard
route** - Enter and Space on the inner button produce a state identical to a mouse click, measured
field by field. The one real blocker was the one already written down as `docs/backlog.md` 22, and it
is now closed.

### Deferred by owner, and not this stage's hunt

`docs/backlog.md` items 3 (page scripts as code), 5 (page weight, font swap, layout shift) and 12
(odds-delta animation) are assigned to Stages 11 and 12. They are in no status above because they
are not open findings, they are work with a date on it.

---

## What this table changes about the run

The inherited plan was eighteen classes, hunted by hand, over 105 screens in two themes at two
widths. The count that matters is different: **29 classes are proven, 7 are measured and 12 are open** -
and of the eleven, five are the ones that actually need eyes. Two of the eighteen inherited classes
became gates in this step rather than a hunt, and both of the new gates found a defect the class
description had not known about, which is the argument for the column restated: a gate is not a
tidier way of looking, it is a different instrument.

That is the whole argument for putting the gate in the first column. A pass that re-hunts a gated
class is not more thorough than the gate; it is a person doing by hand, once, on the screens they
remembered to open, what a machine does completely on every commit. The gates were written over nine
audit passes precisely so that this step would be short.
