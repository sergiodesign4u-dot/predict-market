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

**40 of the 46 component files stand on the five anchors.** Six do not: `account`, `cookie-consent`,
`profile`, `toc`, `toggle`, `patterns/action-bar`. They are not deleted and not wrong; they are
**unmeasured by this pass**, and "holds nothing" is not a reading that was taken about them. They
get a level when the screens that carry them are walked.

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

### Level 2, molecules

| Component | Uses | Declaration |
|---|---|---|
| `trustbar` | 451 | **HOLDS its own items**, three of them, each a mark and a line. The arithmetic reads 1 because every class in it is its own. Filed as an atom in `index.css` and it is not one |
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
| `account` | 3 | **HOLDS** `button`, 6 of them. Walked 2026-08-08 on the three screens that carry it; two of the three bars wear `.flat`, which removes everything the file draws |
| `cookie-consent` | 1 | **HOLDS** `button`, 3 of them, plus its own rows. Walked 2026-08-08. One banner on one screen, three categories, one locked ON and none disabled |
| `toc` | 1 | **HOLDS its own rows**, 14 of them, and they are anchors rather than buttons. Walked 2026-08-08. A rail above 900 and a disclosure below it |

### Level 3, organisms

| Component | Uses | Declaration |
|---|---|---|
| `header` | 668 | **HOLDS** `button`, `chip`, `iconbtn`, `navitem`, `toast`. A shell |
| `footer` | 615 | **HOLDS** `filters`, `iconbtn`, `toast`, `trustbar`. A shell |
| `hiw-dialog` | 574 | **HOLDS** `dialog`, `iconbtn` |
| `dialog` | 291 | **HOLDS** `button`, `chip`, `iconbtn`, `input`, `notice`, `quick` |
| `betpanel` | 120 | **HOLDS** `yesno`, `chip`, `button`, `input`, `quick`, `notice`, `state-block` |
| `tabs` | 153 | **HOLDS** `bets-table`, `comments`, `position`, `button`, `chip` |
| `event-detail` | 126 | **HOLDS** fourteen, and it is the screen's own shell |
| `bets-table` | 89 | **HOLDS** `comments`, `position` |
| `chart` | 84 | **HOLDS** `chip`, `tabs` |
| `card` | 58 | **HOLDS** `yesno`, `oddsbar`, `options`, `iconbtn`, `skeleton` |
| `hero` | 55 | **HOLDS** `yesno` |
| `feed` | 41 | **HOLDS** everything a browse screen stands on. A shell |
| `profile` | - | outside the core, unmeasured |

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
