# The defect table

Step 8 of this stage is the check, and this is its first half: not a list of findings, but the map
of **where a finding could still be hiding**. The second half is the hunt, and it only has to run
where this table says nothing is holding.

**Why the first column is a gate and not a category.** The taxonomy this step inherits was written
for a project with no build check: eighteen classes of defect, each to be looked for by hand, on
every screen. This project has **32 gates over 76 checks**, and a green gate is not an audit result,
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

**23 classes, and none of them needs a person to go and look.** What step 8 owes each of these is one
question: does the gate ask the right thing. Two of the 23 have a known answer to that already, and
both are recorded rather than assumed: gate 14 missed `.signin-lead` and `.delta .row` because each
selector has a real ancestor, and gate 1 masks the `<aside>`, which is why gate 22 exists.

### MEASURED, and not gated

| # | Class of defect | Instrument | Standing |
|---|---|---|---|
| 24 | Contrast under the floor | `audit.cjs` | **FIXED 2026-08-03.** The 378 were one defect: `oddsbar.css` put the FILL roles on 12px bold text. `--outcome-yes-text` / `--outcome-no-text` already existed, so the repair is two words and no token moved. Re-measured in a browser, both themes: `span.l-yes` daylight 2.62 -> **7.23**, `span.l-no` daylight 3.76 -> **7.57**, `span.l-no` graphite 4.35 -> **7.54**, `span.l-yes` graphite 6.23 -> **9.82**. `ui-kit/docs/backlog.md` S14 is closed and `ui-kit/docs/history.md` records why it is the run's best evidence for the semantic token level. **The row stays MEASURED and does not become PROVEN**: nothing gates it, and the reason the same defect stood through five stages is finding 42 below |
| 25 | A link with no rule behind it | `audit.cjs` | 992 links, every one inside a component that styles it; the one exception became S3 |
| 26 | Horizontal overflow | `audit.cjs` | 0, last full run |
| 27 | A request that 404s | `audit.cjs` | 0, last full run |
| 28 | A pinned box taller than the window it is pinned to | `audit.cjs`, second pass at 640px | three rails found and fixed; what the fix left behind is S12 and S13 |
| 29 | The focus ring at every tab stop | `audit.cjs --focus` | 18 tab stops on the document page, all measured |
| 30 | A painted screen that moved when the system changed | `snap.cjs` | 525 of 525 identical across the button merge; 84,836 boxes unmoved across the pattern extraction |

**Seven classes that are true as of the last run and not on any commit.** Step 8 owes these a re-run
and a number, not a search. Nothing here has to be found; it has to be re-measured and the date
written next to it.

### OPEN: nothing asks these, and this is the hunt

| # | Class of defect | Where it is already known to bite | Why no gate |
|---|---|---|---|
| 31 | **Copy against the voice contract** | `docs/backlog.md` 29: five placements of a trader term, 9 screens per tree each, plus `(AMM)` on 4 | The invariant was only written down on 2026-08-03. Now that the rule is about PLACE, it is mechanisable: a term list crossed with an element list. **The strongest candidate for gate 33** |
| 32 | **A document row that does not match the product** | `ui-kit/docs/backlog.md` S21: inventory L163, L155 and L97, and the mechanism behind two of them | Three of the inventory's columns are computed and correct; the false cells are in the hand map and in a column nothing computes |
| 33 | **A class declared in the wrong file** | `docs/backlog.md` 17: five classes, each distorting the level it feeds | The ownership map is not wrong, so no check can see it: `.grid-l` in `feed.css` IS the file with the fewest ancestors. It needs a human to say the chart's grid line belongs to the chart |
| 34 | **A component boundary nobody has drawn** | `docs/backlog.md` 16b, 16d, 18, 19 | `card` is a molecule and an organism, `notice` is six blocks, `position` is four things, `hiw-dialog` is two components on one vocabulary. Arithmetic can count them; only a person can split them |
| 35 | **Keyboard reachability** | `docs/backlog.md` 22 (the filter panel) and 23 (a multi-outcome row is a `<div>` that answers a click) | `audit.cjs --focus` walks the tab order and measures the RING; it does not ask whether everything operable is IN the order |
| 36 | **What a screen reader is told when something changes** | `docs/backlog.md` 24 and 25 (eight error blocks announced to nobody) | Nothing in the build reads ARIA |
| 37 | **A promise the product cannot keep** | `docs/backlog.md` 27 and 28: 16 dead footer destinations on 104 screens, 1,664 links into nowhere, 8 of them on no map at all | Gate 4 resolves relative paths; `href="#"` resolves fine. A destination that exists as a page and not as a plan is an IA question |
| 38 | **A shipped block that no document describes** | `docs/backlog.md` 26: the featured hero, in both trees and in no document | Gate 18 pairs the trees and both carry it, so agreement is not evidence |
| 39 | **One shape declared more than once** | `ui-kit/docs/backlog.md` S16 and S17 (closed), S18 (open) | Every one was found by reading, not by a check. Two tokens with one value in every theme is the open case |
| 40 | **Repo weight and tracked artefacts** | `ui-kit/docs/backlog.md` S22: 19 MB of screenshots in git, in a 62 MB pack | The `.gitignore` rule that was written for exactly this cannot untrack what predates it and names one extension |
| 41 | **A number in a document that nothing computes** | S21's L97 is the instance; the class is larger | `_fill_inventory.py` computes three columns of the inventory and the screens column is not one of them |
| 42 | **A recorded measurement that was false when it was written** | **Fifteen separate "0 below AA" claims**, in three documents: `docs/decisions.md` (8), `ui-kit/docs/history.md` (6) and `voice/docs/microcopy.md` (1), over corpora up to "420 page loads x 2 themes, 86,534 text pairs". `ui-kit/docs/backlog.md` S14 measures **378 elements below 4.5:1** and says explicitly "Pre-existing: measured identical at HEAD before this pass and after it", so the 378 were there on every one of those dates | Nothing checks a document against a measurement, and this one cannot be closed by editing: `history.md` and `decisions.md` are written once and never edited on purpose, so the correction has to be a LATER entry that names the false lines. **WHY THE ZERO SURVIVED FIFTEEN PRINTINGS, and it is a rule rather than an episode.** The zero was printed by an instrument carrying three bugs this repo had already found and written down: a regex reading the components of `color-mix(in oklab, ...)` as sRGB bytes, a print limit that stopped at six findings per render (32 of 48 renders hit it exactly), and `mix-blend-mode`, which no computed style can resolve. Nobody lied. **A broken instrument that reports a DEFECT gets caught, because somebody goes to look and finds the instrument lying. A broken instrument that reports ALL CLEAR is caught by nobody, because there is nothing to go and look at.** The most dangerous output of a broken check is not a false alarm, it is a clean bill of health, and this is the one asymmetry that decides where verification effort belongs. **The sweep behind the number:** 79 claims of the "nothing was found" form across the repo's markdown - 29 gated today and therefore still true by construction (em dash to gate 7, broken links to 4, 8 and 21), 18 about contrast, and 30 measured by a browser and gated by nothing, true as of their run and unknown today |

| 43 | **The instrument crops the subject of its own photograph** | Every state picture in `ui-kit/_states/`. `ui-kit/_verify/browser.cjs` `shoot()` asks `boxAt(i, 12)`, and `boxAt` then SHRINKS the pad to half the distance to the nearest neighbour. `ui-kit/_specimen.css` sets `.kit-row{gap:14px}` and `.kit-row + .kit-row{margin-top:14px}`, so every facing side of every control in a specimen row is clipped at **7px**, whatever the 12 asked for. Measured against what has to fit: the focus ring is `outline:2px` at `outline-offset:2px` = **4px** on every side, and the brass hover glow `box-shadow:0 6px 18px -8px` reaches **7px** below the box by the blur/2 convention and **16px** if the whole blur has to be inside the frame. So the worst case has **zero margin** and the glow's tail is cut | Nothing asks it, and this is the sibling of 42: an instrument that produces a confident picture and says nothing about the part of the subject outside the frame. **And the fix is not where it looks.** The crop is in the PNG, not in the `.ck-shot-row` frame that displays it, so no change to `ui-kit/_page.css` can return a pixel that was never captured: the pad policy in `boxAt` and the 14px specimen gap that caps it both have to move, and all 766 pictures have to be taken again |

| 44 | **One button under five names, and the size is encoded in the name of a PLACE** | `components/button.css`, measured. Five names - `.auth-btn`, `.state-btn`, `.provider-btn`, `.confirm-btn` and `.cta-bar button` - carrying **three axes**: size (3 font steps 12/13/14 over 4 paddings), width (auto against 100%), and emphasis, which is encoded **three different ways** - a modifier (`.primary`), a name of its own (`.confirm-btn`), and a POSITION (`.cta-bar > *:first-child`). The file is **30 rules: 6 write the anatomy and the axes on a name, 11 are the state layer and have to be scoped, and 13 are RECONCILIATION**, a scope re-saying what a name already said. Three of those 13 exist ONLY to put an axis back (`.resolved-panel .state-btn{width:100%}`, `.bet-sheet .confirm-btn{padding:16}`, `.bet-dock .confirm-btn{width:auto;padding:12}`) and one re-declares the whole anatomy from nothing in **16 declarations** (`outcome-dialog .provider-btn`). The stand pays for it in pictures: **8 photographed faces x 4 states x 2 themes = 64 shots**, where the axes say there are **2 faces**, so a matrix page is 2x4x2 plus a rest strip of 3 sizes x 2 themes = **22, which is 42 fewer** | **None.** Gate 30 catches a name the product never wears and did (the six `.btn-*` classes, deleted); gate 24 catches a specimen that shows less than the component. Neither can ask whether five names are one component at three coordinates. **And the measurement argues against doing it inside the button**: the position mechanism belongs to `patterns/action-bar.css`'s arrangement and the `.resolved-panel` width belongs to a `state-block` context, so three axes do not fit in `components/button.css` without touching a pattern and two components |
| 45 | **Six icon-buttons, six files, and none of them is the button file** | Counted over both trees, a `<button>` whose whole content is a mark: `.icon-btn` 388 (`header.css`), `.sheet-close` 228 (`dialog.css`), `.hiw-close` 105 (`hiw-dialog.css`), `.bookmark-btn` 84 (`card.css`), `.ed-act` 27 (`event-detail.css`), `.toast-close` 4 (`toast.css`). **709 in the painted tree, six classes, six files, and `components/button.css` draws none of them.** That is `ui-kit/docs/backlog.md` S11 at family scale, and S11 was one file. **And the letter is not a toast problem.** `.toast-close` ships `<button class="toast-close">x</button>` at 24x24 with `font-size:12` and `line-height:none`, so a glyph with its own baseline sits where a mark should - 4 buttons on 1 screen. `.sheet-close` ships the SAME letter on **123 buttons across 105 screens**, and ships an inline SVG on 105 others: one class, two answers, and in the painted tree every bare `dialog.app-dialog` gets the letter while `signin-dialog` gets the mark. Both trees agree on every count, so gate 18 is quiet and correct | **None, and the reason is the shape of 42.** Gate 3 asks that no icon reference is dead and gate 17 that every mark is on the sheet; **a letter used as an icon passes both by not being an icon.** The check is green because there is nothing for it to look at, which is the same asymmetry as the false zero |
| 46 | **A link wrapped around a button, 2,448 times** | Found while measuring row 35's reachability. `<a href="..."><button type="button">YES</button></a>` is the shipped shape of every YES/NO on a feed card, and of the header's portfolio and favourites controls: **2,448 occurrences on 133 painted screens and 1,629 on 104 grey ones**, both trees agreeing. `<button>` is interactive content and the HTML content model forbids interactive content inside `<a>`; the two elements also carry different roles, so what a screen reader announces for the pair is not defined by anything. The largest single shape is the bare `<a href="..."><button type="button">` at 1,712, and the loudest is `<a href="..." aria-label="Favorites, see saved events"><button type="button" class="icon-btn" aria-label="Favorites">` - **two accessible names on one target**, 89 times | **None, and no gate can be written for it here.** Gate 4 resolves the href, gate 18 pairs the trees and they agree, and nothing in the build parses the HTML content model. It is markup, so under the twin contract it belongs to the grey tree first and is a Stage 12 handoff item rather than a Design System edit. Named here because it was measured here |
| 47 | **The ring reader measures the element that has focus, not the element the ring was moved to** | `ui-kit/_verify/browser.cjs` `ring()` reads `document.activeElement`, its `outlineColor`, and the ground under it. Two components in this system deliberately put the ring somewhere else, because the focused element is a hidden input: `tabs.css` maps `#edtab-*:focus-visible ~ .ed-tabbar label[for=...]` and `filters.css` now uses `label:has(input:focus-visible)`. In both, `base.css`'s universal `:focus-visible` still draws an outline on the hidden input itself - offscreen in one case, on a 1x1 transparent box in the other - so `ring()` returns `visible:true` and a ratio for a ring **no person can see**, and would return exactly that even if the label rule were deleted | **None, and it is the third instance of 42's shape in this run.** The instrument reports a clean result about the wrong object. Both ring placements in this repo were measured by hand instead, with the composite ground computed through the translucent brass wash: the tab labels at 8.71 and 7.14, the filter labels at 8.31/7.80 on graphite and 4.48/7.14 in daylight. A gate would have to ask "if this element's outline is invisible, is there another element that gained one" |

**Seventeen open classes**, two of them found while fixing the others. Two (31 and 32) are mechanisable
now and should become gates rather than a pass; nine (33, 34, 38, 39, 42, 43, 44, 45 and 47) need a
person, because each is a JUDGEMENT about where a thing belongs or about a record nobody can edit,
not a fact a checker can read; four (35, 36, 37, 46) belong to owners outside this stage, three of
them already assigned in `docs/backlog.md` and the fourth a markup question the twin contract sends
to the grey tree first; two (40, 41) are hygiene with a measured size and a decision still to take.
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
widths. The count that matters is different: **23 classes are proven, 7 are measured and need a
re-run rather than a search, and 15 are open** - and of the fifteen, eight are the ones that actually
need eyes.

That is the whole argument for putting the gate in the first column. A pass that re-hunts a gated
class is not more thorough than the gate; it is a person doing by hand, once, on the screens they
remembered to open, what a machine does completely on every commit. The gates were written over nine
audit passes precisely so that this step would be short.
