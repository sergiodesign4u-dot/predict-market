# ui-kit/ - the vitrine, being rebuilt from 2026-08-07

The kit shows the system to a person and it holds no product code. Right now it holds seven pages
plus its stylesheet and its registry: `overview.html`, which says what is happening, **all four
foundation pages** (`icons.html`, `colour.html`, `typography.html`, `geometry.html`), and the
component pages by level, `vitrine.html` for the ten atoms and `molecules.html` for the fourteen at
level 2. `_page.css` is the stand furniture they all share and `_nav.js` is the route.

**A page per LEVEL, not a page per component.** Forty pages of one component each would be forty
navigations to compare two chips. A level is the unit a person actually reads, and the level is where
the shared rule lives: what an atom is, what a molecule holds, why the declaration exists.

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
   is open**: header, footer, dialog, hiw-dialog, betpanel, tabs, bets-table, card, hero, chart,
   feed, event-detail, profile.
5. **One audit run**, as a report.

The five anchors: event feed, event detail, active bets, deposit, sign in, with their loading, empty,
error and logged-out variants. 41 screens of the 106.
