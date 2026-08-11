# Component inventory - what each part IS, and which level it stands on

Step 2 of the rebuild, 2026-08-07. Read once from the five anchor screens, declared here, and
**read by nothing**. The census that precedes it is `census.md`; the consolidation that follows it
is `consolidation.md`.

## The formula, and why a declaration is still needed

**A level is one plus the highest level of what a component CONTAINS.** Level 1 holds nothing from
the system, level 2 holds atoms, level 3 holds molecules or is the shell of a screen. Three is the
ceiling: the fourth rung is patterns, whose criterion is repetition rather than nesting.

Containment was read from the **41 anchor screens** rather than from a specimen, because a specimen
is a claim and a screen is the product. Ownership of a class is taken from **the subject of a
selector** and not from the whole of it: `.app-case .chip{...}` styles a chip and merely stands in a
case. Counting every class in the selector made `.app-case` a component, owned by whichever file
mentioned it most, and that file then "contained" the entire page. **Levels came out at twenty.**

A class written by three files or more is scaffolding rather than any component's own, and nobody
owns it.

**The formula has one blind spot and it is the reason this file exists.** A component built out of
its own class names reads as containing nothing, so the arithmetic answers 1 for a control and 1 for
a whole row of them. In the deleted kit, seven of seventeen such readings had never been examined
and they were the entire atom shelf. So every entry below carries a declaration:

- **ONE CONTROL** - there is nothing inside me. A person points at this and it is a single thing.
- **HOLDS** - here is what is inside me, named, even where the arithmetic could not see it.

## The core, and what is outside it

**41 of the 47 component files stand on the five anchors.** Six do not: `account`, `cookie-consent`,
`profile`, `toc`, `toggle`, `patterns/action-bar`. They were not wrong; they were
**unmeasured by this pass**, and "holds nothing" is not a reading that was taken about them. They
get a level when the screens that carry them are walked.

**All six were walked on 2026-08-08 and one of them did not survive it.** `account` was deleted the
same day it was given a level: the reading that shows what a component holds is the reading that can
show it has nothing left to draw. Its row below carries the account.

## The declaration

Uses are elements carrying one of the component's own classes across the 41 screens.

### Level 1, atoms

| Component | Uses | Declaration |
|---|---|---|
| `button` | 687 | **ONE CONTROL.** Four emphases and four sizes are faces of one thing, not four things |
| `iconbtn` | 527 | **ONE CONTROL.** Six faces, all of them an answer to the surface it stands on |
| `chip` | 466 | **ONE CONTROL.** The rail, the nav, the amount and the quiet chip are one box under four scopes |
| `oddsbar` | 213 | **ONE CONTROL.** A track and a fill; the fill is a datum, which is why its width is on the element |
| `input` | 123 | **ONE CONTROL** |
| `navitem` | 249 | **ONE CONTROL.** A row that goes somewhere and draws nothing until pointed at. The arithmetic put it at 2 through a cycle with `bottomnav`, resolved below |
| `yesno` | 56 | **ONE CONTROL, and the pair is the control.** The two halves state one market's two sides and cannot exist apart. The arithmetic put it at 6 through a cycle with `betpanel` |
| `toast` | 41 | **ONE CONTROL.** Filed as a molecule in `index.css` and it holds nothing |
| `skeleton` | 34 | **ONE CONTROL.** A shape that stands where a thing will be |
| `toggle` | 3 | **ONE CONTROL.** Walked 2026-08-08: three placements, all the same switch, all `aria-checked="false"`, so four of its five faces have no placement in the product |
| `logo` | 210 | **ONE THING, and it is not a control in half of its placements.** The brand lockup: the mark, a gap, the wordmark. Written 2026-08-11 with the rename to Yonder, out of the two copies that were living in `header.css` and `footer.css`. It holds nothing, and it is the one component whose drawing is not made of system ink, which is the rule this folder already states from the other end: a brand mark keeps its own drawing and no generic glyph may stand in for it. **It is a `<button>` in the header and a `<span>` in the footer**, so the reset that makes those two render identically is part of the face rather than of either place |
| `platehead` | 359 | **ONE FACE, AN ANATOMY PLUS A DEFAULT SKIN, and it is worn by four different components.** The brass-cornered head of a plate: the ground, the wave masked out of the corner, the 210px glow anchored outside the box, and the display heading. Written 2026-08-11 out of two copies that agreed to the byte, in `dialog.css` for the plain sheet head and in `hiw.css` for the how-it-works head and the page hero. **They agreed because six numbers had been moved by hand on one of them that morning**, by backlog 98, which is the finding rather than the fix. It holds nothing and it loads at level 1 for the lockup's reason: both wholes that hold it load at level 3 and must win a tie. **The `.hiw-glow` span went with it**, 200 elements over three trees drawing what the other host drew with a pseudo. Backlog 105 and 108 | **THE FOURTH HOST ARRIVED THE SAME DAY, BY BACKLOG 109**, and it is the one that names what this file is. The outcome head was filed as "not a wearer, and that is deliberate" in the morning; measured in the afternoon it had 13 of 15 box properties identical, 13 of 15 on the wave, 12 of 15 on the win glow and 10 of 11 on the heading, with the wave's data URI byte-identical. The row feared folding it in would cost a second class and it cost none, because `.outcome-dialog`, `.win-dialog` and `.loss-dialog` were already on the element's ancestors. So this is an ANATOMY PLUS A DEFAULT SKIN rather than a face, and the loss head is the one plate head with no glow and has to say so, since inheriting the face now means inheriting a brass one.

### Level 2, molecules

| Component | Uses | Declaration |
|---|---|---|
| `trustbar` | 451 | **HOLDS its own items**, three of them, each a mark and a line. The arithmetic reads 1 because every class in it is its own. Filed as an atom in `index.css` and it is not one. **The count above is 2026-08-07 and the component lost a face on 2026-08-08**: `.feed-trustbar` with `.ft-inner`, `.ft-item`, `.ft-ic` and `.ft-sep`, 7 elements on every anchor screen, stood in the markup and was `display:none` on all of them. The number is left as it was read rather than corrected, because a real one is a measurement and not a subtraction. Backlog 57 |
| `market` | 200 | **HOLDS its own rows.** Same blind spot: a block of question, rule and source, built from its own names |
| `comments` | 119 | **HOLDS** `button`, `chip` |
| `filters` | 91 | **HOLDS** its own panel, its list and the labelled options |
| `bottomnav` | 75 | **HOLDS** `navitem`, 164 readings of it. Filed as an organism in `index.css` |
| `catnav` | 64 | **HOLDS** `chip` |
| `related` | 48 | **HOLDS its own list.** Reads 1, filed as a molecule already, and the file is right |
| `state-block` | 48 | **HOLDS** `button`. Filed as an organism |
| `quick` | 41 | **HOLDS** `chip` |
| `options` | 30 | **HOLDS** `yesno`. Filed as an organism |
| `seo-plate` | 9 | **HOLDS its own prose blocks** |
| `loadmore` | 1 | **HOLDS** `chip` |
| `position` | 43 | **HOLDS** `skeleton`. Filed as an organism; it is a row in a list, not a shell |
| `notice` | 96 | **HOLDS** `button`. Filed as an organism |
| ~~`account`~~ | 3 | **HOLDS** `button`, 6 of them. Walked 2026-08-08 on the three screens that carry it; two of the three bars wear `.flat`, which removes everything the file draws. **DELETED the same day.** The walk that gave it a level is the walk that ended it: the file's whole content was the action bar's stone plus the three declarations `.flat` removed it with, the stone stood once of three placements, and its shape, a top border and two top corners, is the surface of a bar that FLOATS over content scrolling under it. Nothing in this product docks. The bar is one face now and the whole of it is `components/patterns/action-bar.css`; the page is `ui-kit/action-bar.html`. Backlog 63 |
| `cookie-consent` | 1 | **HOLDS** `button`, 3 of them, plus its own rows. Walked 2026-08-08. One banner on one screen, three categories, one locked ON and none disabled |
| `toc` | 1 | **HOLDS its own rows**, 14 of them, and they are anchors rather than buttons. Walked 2026-08-08. A rail above 900 and a disclosure below it |

### Level 3, organisms

| Component | Uses | Declaration |
|---|---|---|
| `header` | 668 | **HOLDS** `button`, `chip`, `iconbtn`, `navitem`, `toast`. A shell |
| `footer` | 615 | **HOLDS** `filters`, `iconbtn`, `toast`, `trustbar`. A shell |
| `hiw` | 1,604 | **HOLDS** `hero` (`.brand-tile` and its six parts) and `position` (`.pos` and its four), which is the arithmetic saying what the ceiling rule already says: level 3 also means the shell of a screen. **This was the last level in the kit that had to be DECLARED, and it is computed since 2026-08-11.** It was filed as `hiw-dialog` at 574 while the file was one block with two hosts plus ten rules about a sheet; the ten are `dialog`'s now and the name stopped saying dialog with them. The 574 is the 41-screen census of 2026-08-07 and the 1,604 is every element wearing one of the thirteen remaining classes across the 105 painted screens on 2026-08-11: **the two are not on one scale**, because the instrument that read 41 screens went with the vitrine, and a figure nobody can reproduce is worse than a figure that says what it counted |
| `dialog` | 291 | **HOLDS** `button`, `chip`, `iconbtn`, `input`, `notice`, `quick`. **It gained `.hiw-dialog`, `.hiw-body`, `.hiw-full` and `.hiw-arrow` on 2026-08-11**, 420 elements over the same 105 screens, with backlog 15 and 18. It does not HOLD the how-it-works block: the sheet host is one element WEARING two component classes, and what it genuinely holds is `.sheet-close` |
| `betpanel` | 120 | **HOLDS** `yesno`, `chip`, `button`, `input`, `quick`, `notice`, `state-block` |
| `tabs` | 153 | **HOLDS** `bets-table`, `comments`, `position`, `button`, `chip` |
| `event-detail` | 126 | **HOLDS** fourteen, and it is the screen's own shell |
| `bets-table` | 89 | **HOLDS** `comments`, `position` |
| `chart` | 84 | **HOLDS** `chip`, `tabs` |
| `card` | 58 | **HOLDS** `yesno`, `oddsbar`, `options`, `iconbtn`, `skeleton` |
| `hero` | 55 | **HOLDS** `yesno` |
| `feed` | 41 | **HOLDS** everything a browse screen stands on. A shell |
| `profile` | 2 | **HOLDS** `button` and `card`: the identity row holds one, the gallery holds three. Walked 2026-08-08 on the two screens that carry it, tabs cycled. The sixth and last of the unmeasured |

### Patterns

`patterns/browse-shell`, `patterns/detail-shell`, `patterns/card-grid`, `patterns/list-head`,
`patterns/position-list` all stand on the anchors and hold organisms or molecules.
`patterns/action-bar` does not appear on any of the 41.

## The five cycles, and how each was resolved

The arithmetic found five pairs that contain each other. Every one is decided by the count and by a
reason, not by whichever direction the walker met first.

| Pair | Counts | Resolution |
|---|---|---|
| `bottomnav` / `navitem` | 164 vs 34 | **The bar holds the slot.** The 34 are elements carrying both classes |
| `dialog` / `notice` | 97 vs 5 | **The dialog holds the notice.** The 5 are one screen where a notice wraps a sheet |
| `betpanel` / `yesno` | 68 vs 34 | **The panel holds the pair.** The 34 are `.bp-side.yesno-pick`, one element wearing both, which is the trader face of the atom |
| `event-detail` / `position` | 54 vs 2 | **The screen holds the row** |
| `card` / `event-detail` | 50 vs 30 | **Neither.** A card links TO the detail screen and the detail screen shows cards; the shared names are the question and the odds. Both are organisms and the cascade does not have to separate them |

## A correction to the census, and it matters

`census.md` reports that **58 per cent of the controls carry no class** and calls four of the nine
jobs unowned. The count is right. **The conclusion was wrong**, and reading the markup is what says
so: every one of them is owned by a parent's class through an element selector.

```
.app-footer a        .popular-links a       the footer's 26 links per screen
.yesno button        the outcome pair, both halves
.filter-panel li label   the 304 filter options
.app-case .tabs button   the segmented Active / History pair
.notif-menu summary  .avatar-menu summary   .filter-menu summary
```

**A component owning its children by element selector is correct exactly when the child cannot
stand outside the parent**, and a defect when the child is a control that also stands elsewhere. So
the census's finding survives in a smaller and sharper form, as four decisions:

1. **The footer link is fine.** It cannot stand outside a footer. **A link in running prose is not**,
   and it has no rule at all: the deleted backlog measured one at **1.8:1 in the browser's own
   blue**. `link` is a level 1 atom that does not exist yet and has to be written.
2. **The filter option is a chip and is not called one.** Measured 33px, 10px radius, 8px pad, and
   its selected state is the same brass tint `chip.css` already declares. Adopting the class moves
   the padding 8/8 to 8/12 and the height 33 to 38 on **304 readings**, so it is a consolidation
   decision and is written down in `consolidation.md`, not taken here.
3. **The segmented tab is a chip too.** `.app-case .tabs button` renders at 38px with a 100px
   radius, which is the quiet chip's box exactly. 18 readings.
4. **The outcome pair's halves are told apart by DOM ORDER**, `:first-of-type` and `:last-of-type`.
   Move the two buttons and green becomes red. That is the one finding here that is a latent bug
   rather than a naming debt, and it is 81 readings of the control this product is named after.

## The import order disagrees with the declaration in eight places

`components/index.css` groups its imports by level, and that order is load bearing: two rules of
equal specificity are decided by which file was read last. Measured against the declaration above:

| Component | Filed in `index.css` | Declared here |
|---|---|---|
| `toast` | molecule | **atom** |
| `navitem` | molecule | **atom** |
| `yesno` | molecule | **atom** |
| `trustbar` | atom | **molecule** |
| `market` | atom | **molecule** |
| `bottomnav` | organism | **molecule** |
| `state-block`, `options`, `position`, `notice` | organism | **molecule** |

**Nothing is reordered in this step.** A move in that file changes which of two equal rules wins,
which is exactly the class of change that renders identically until the day it does not. The reorder
belongs in `consolidation.md` with a before-and-after measurement over the 41 screens, and it is the
first thing that pass does.

## Behaviour on width

Added 2026-08-12 by Responsive step 4, and **filled for every component**, because an empty cell
here would mean nobody knows what the part does on a wide screen. Read from the product at twelve
widths, three rungs and one pixel either side of each, on the screen where each component stands
widest, with every dialog opened.

**The column measures the component against its PARENT'S CONTENT BOX and not against the window**,
and that is the whole reason the numbers are worth anything. Measured against the window, 33 of the
43 read as stepping at 640, because the page gutter goes 14 to 40 there and takes 51px out of the
content column: that is the frame's behaviour arriving in every row. Measured against the parent's
BORDER box, seven more read as changing their share, because the parent's own padding steps.
**A component that is fluid inside a container that steps is still fluid.**

| Component | Its own width query | What it does with width |
|---|---|---|
| `action-bar` | none | **FILLS** its container |
| `betpanel` | 760 | **CHANGES** its share |
| `browse-shell` | 900 | **FILLS** its container |
| `button` | none | **GONE in a band**, then fixed |
| `card` | 640 | **FILLS** its container |
| `card-grid` | none | **FILLS** its container |
| `catnav` | 640, 900 | **FILLS** its container |
| `chart` | 760 | **FILLS** its container |
| `chip` | 640, 900 | **FIXED**, 81px |
| `comments` | none | **FILLS** its container |
| `cookie-consent` | none | **FILLS** its container |
| `detail-shell` | 760 | **FILLS** its container |
| `dialog` | 640 | **CHANGES** its share |
| `event-detail` | 560, 640 | **FILLS** its container |
| `feed` | none | **FILLS** its container |
| `filters` | 640 | **FIXED**, 152px |
| `footer` | 640 | **FILLS** its container |
| `header` | 640, 760 | **FILLS** its container |
| `hero` | 620, 980 | **FILLS** its container |
| `hiw` | 900 | **FILLS** its container |
| `iconbtn` | 560 | **GONE in a band**, then fixed |
| `input` | none | **FILLS** its container |
| `list-head` | none | **FILLS** its container |
| `loadmore` | none | **FILLS** its container |
| `logo` | none | **FIXED**, 86px |
| `market` | none | **FILLS** its container |
| `navitem` | none | **FIXED**, 258px |
| `notice` | none | **FILLS** its container |
| `oddsbar` | none | **FILLS** its container |
| `options` | none | **FILLS** its container |
| `platehead` | none | **FILLS** its container |
| `position` | 640 | **FILLS** its container |
| `position-list` | none | **FILLS** its container |
| `profile` | none | **FILLS** its container |
| `quick` | none | **FILLS** its container |
| `related` | none | **FILLS** its container |
| `seo-plate` | 760 | **FILLS** its container |
| `skeleton` | none | **CHANGES** its share |
| `state-block` | none | **FILLS** its container |
| `tabs` | none | **FILLS** its container |
| `toast` | none | **FILLS** its container |
| `toc` | 900 | **FILLS** its container |
| `toggle` | none | **FIXED**, 44px |
| `trustbar` | 760 | **FILLS** its container |
| `yesno` | none | **FILLS** its container |
