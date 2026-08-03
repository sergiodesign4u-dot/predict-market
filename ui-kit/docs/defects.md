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
| 24 | Contrast under the floor | `audit.cjs` | **378 elements below 4.5:1**, in three equal groups of 126, on 12 screens at both widths. `ui-kit/docs/backlog.md` S14. The light theme is the bad half and `span.l-yes` at **2.62:1** is not a rounding question. **And this row is also finding 42 below**: two passes in `ui-kit/docs/history.md` record "0 below AA" over 308 painted page loads for the same question |
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
| 42 | **A recorded measurement that was false when it was written** | `ui-kit/docs/history.md`, the Verified blocks of two passes: "Painted: 308 page loads across both themes, 61956 text pairs, **0 below AA**, 0 overflow", and the same claim again one pass later. `ui-kit/docs/backlog.md` S14 measures **378 elements below 4.5:1** and says explicitly "Pre-existing: measured identical at HEAD before this pass and after it", so the 378 were there on both of those dates | Nothing checks a document against a measurement. And this one cannot be closed by editing: `history.md` is written once and never edited on purpose, so a false entry stays readable forever and the correction has to be a LATER entry that names it. S14 is that correction living in a different file, where a person reading the passes will not meet it. **This is the sharpest shape in the table, because the stale claim is a zero**: a wrong count invites a recount, a zero invites nobody |

**Twelve open classes.** Two of them (31 and 32) are mechanisable now and should become gates rather
than a pass; five (33, 34, 38, 39 and 42) need a person, because each is a JUDGEMENT about where a
thing belongs or about a record nobody can edit, not a fact a checker can read; three (35, 36, 37) belong to owners outside this stage
and are already assigned in `docs/backlog.md`; two (40, 41) are hygiene with a measured size and a decision
still to take, and the last of those five, 42, cannot be closed by an edit at all.

### Deferred by owner, and not this stage's hunt

`docs/backlog.md` items 3 (page scripts as code), 5 (page weight, font swap, layout shift) and 12
(odds-delta animation) are assigned to Stages 11 and 12. They are in no status above because they
are not open findings, they are work with a date on it.

---

## What this table changes about the run

The inherited plan was eighteen classes, hunted by hand, over 105 screens in two themes at two
widths. The count that matters is different: **23 classes are proven, 7 are measured and need a
re-run rather than a search, and 12 are open** - and of the twelve, five are the ones that actually
need eyes.

That is the whole argument for putting the gate in the first column. A pass that re-hunts a gated
class is not more thorough than the gate; it is a person doing by hand, once, on the screens they
remembered to open, what a machine does completely on every commit. The gates were written over nine
audit passes precisely so that this step would be short.
