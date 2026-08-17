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

**`navitem`'s figure below was taken before 2026-08-13 and is now short by one row per account
menu.** Favorites joined that menu on that date (`docs/backlog.md` 130), taking it from five rows
to six, and over all of `ui-visual/` the count went from 365 to 438, recounted in a browser. It is
not corrected here because the 41-screen sample this column is measured over is not written down
anywhere, and **a number guessed to look current is worse than a number dated**. Whoever
re-measures this table should re-derive the sample first.

### Level 1, atoms

| Component | Uses | Declaration |
|---|---|---|
| `button` | 687 | **ONE CONTROL.** Four emphases and four sizes are faces of one thing, not four things |
| `iconbtn` | 527 | **ONE CONTROL.** Six faces, all of them an answer to the surface it stands on. **The plain circle went from 242 placements to 137 on 2026-08-14**, all 137 of them now in the header's utility group: the 105 that left were the left group's hamburger, and with them the atom is down to two marks in the product, a bell on 32 and a bookmark on 105 |
| `chip` | 466 | **ONE CONTROL.** The rail, the nav, the amount and the quiet chip are one box under four scopes |
| `oddsbar` | 213 | **ONE CONTROL.** A track and a fill; the fill is a datum, which is why its width is on the element |
| `input` | 123 | **ONE CONTROL** |
| `navitem` | 249 | **ONE CONTROL.** A row that goes somewhere and draws nothing until pointed at. The arithmetic put it at 2 through a cycle with `bottomnav`, resolved below |
| `yesno` | 56 | **ONE CONTROL, and the pair is the control.** The two halves state one market's two sides and cannot exist apart. The arithmetic put it at 6 through a cycle with `betpanel` |
| `toast` | 41 | **ONE CONTROL.** Filed as a molecule in `index.css` and it holds nothing |
| `skeleton` | 34 | **ONE CONTROL.** A shape that stands where a thing will be, plus `.sk-status` since 2026-08-16: one hidden sentence per busy region, because a shape says nothing to a screen reader and `aria-busy` is a property rather than a message |
| `toggle` | 3 | **ONE CONTROL.** Walked 2026-08-08: three placements, all the same switch, all `aria-checked="false"`, so four of its five faces have no placement in the product |
| `search` | 46 | **ONE CONTROL WITH TWO CONTAINERS.** A field that holds a query, the mark inside it, the control that empties it, the mono line that answers, and the body that answers IN PLACE: five category tiles, four popular events, the result rows and the seam to the full grid. Written 2026-08-16 as a page you went to and **rebuilt 2026-08-17 as a control you use**, because the page it went to put the field at y=221 on a phone, unfocused, under a category rail and an h1, and kept a header magnifier whose `href` was the page it stood on. Below RAIL the body is a sheet, at RAIL and above it is a panel under a header field, and **the markup is written once and cloned**, so the two cannot drift. It is not a variant of `input` on three counts of anatomy: the mark is INSIDE this control and beside that one, the value is a query rather than a quantity, and this is the only field in the product a person can empty |
| `crumb` | 6 | **HOLDS nothing.** Filed as an atom, written 2026-08-16. **The number worth reading is 3 of 6**: `ia/docs/pages/seo.md` specifies a trail on six page types and `ia/docs/blocks.md` files it as block B2, MVP, and the product rendered zero. It went onto How It Works, Terms and the public profile with its four states, and NOT onto the event detail or the category page, because those two already carry the trail twice over as the category nav: the rail on the plate and the condensed strip in the header, five links each, the reader's own category marked, the strip at y=77 on a phone and y=71 on the desk. **A visible `Home > Politics > this event` there would have been a FOURTH control made of the same five words**, and the critique of the same morning had counted three. Behaviour on width: FLUID, and the link measures **33x44 at 390 with the pointer asserted coarse and 33x18 at 1280** because `.crumb a` joined `base.css`'s 44px list at birth rather than after a sweep, with the `display:inline-flex` precondition in the same edit. The `Legal` level is a `<span>` and not a link: this product has no legal index screen and a crumb pointing at nothing is a broken link. **No `BreadcrumbList` is emitted**, because the product carries 0 `application/ld+json` of any kind on 108 screens, which is `docs/backlog.md` 171 rather than a gap in this component. |
| `logo` | 221 | **ONE THING, and it is not a control in half of its placements.** The brand lockup: the mark, a gap, the wordmark. Written 2026-08-11 with the rename to Yonder, out of the two copies that were living in `header.css` and `footer.css`. It holds nothing, and it is the one component whose drawing is not made of system ink, which is the rule this folder already states from the other end: a brand mark keeps its own drawing and no generic glyph may stand in for it. **It is a `<button>` in the header and a `<span>` in the footer**, so the reset that makes those two render identically is part of the face rather than of either place. **210 until 2026-08-14, when the two files that had never been asked gave it eleven more**: `hero.css` and `seo-plate.css` each spelled "Yonder" by hand in the body face at 13px, mark omitted, on the brand tile and the SEO plate - the two plates in the product whose entire job is to name the brand, and the only two places naming it without it. The markup carries `class="logo bt-by"` and `class="logo seo-by"`, and the placement files were cut back to the one thing they own, where the lockup stands |
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
| `options` | 34 | **HOLDS** `yesno`. Filed as an organism. **The whole field is in the markup since 2026-08-17** and the phone is the only place any of it is hidden, so `.opt-more` counts what the LAYOUT hides rather than what the DATA omits, which is the difference between a fact a sweep can check and arithmetic on percentages |
| `search` | none | 46 on 108 | **TWO BEHAVIOURS ON ONE RUNG, AND THE RUNG IS A MEASUREMENT.** The free middle of the header row is **69px at 640, 137 at 760 and 277 at 900**, so the inline field cannot enter at DESK and enters at RAIL, 56.25rem, where it is `flex:1 1 auto` and **fully fluid: 281 at 900, 441 at 1060, 761 at 1380**. Below RAIL the field is the sheet's, at the width of the screen less 32. Read at 320, 360, 390, 639, 640, 641, 759, 760, 761, 899, 900, 901, 1000, 1140, 1280 and 1600 on both engines: exactly one way in at every width. **`.search-clear` is FIXED 44x44**, the base floor and not this file's number, and `.search-ic` FIXED 18; the panel is the width of the field it hangs from, both edges from the same box |
| `seo-plate` | 9 | **HOLDS its own prose blocks** |
| `loadmore` | 1 | **HOLDS** `chip` |
| `position` | 43 | **HOLDS** `skeleton`. Filed as an organism; it is a row in a list, not a shell. `.pos-fig-lead` since 2026-08-16, which is the record's emphasised figure moving off `:nth-child(2)`: which number matters is a screen's decision and it had been stored in the order of four siblings |
| `notice` | 96 | **HOLDS** `button`. Filed as an organism. **`.inline-error` joined the error family on 2026-08-16 and had never been in it**: `.state-block.state-problem` and `.toast.toast-error` both took `--border-notice`, one danger triangle and a 600 message, and this box took the plain hairline, 0 marks and 400, on the surface where a bet fails  **AND `.quiet-box` GAINED ITS FIRST FACE ON 2026-08-16, `.qb-working`, AFTER THE PLACEMENTS WERE COUNTED RATHER THAN THE NAME READ.** The box is worn by three jobs: FIVE are a process running with an unknown end (the OAuth redirect, the share card, the resolution fetch, the on-chain register, and the Transak wait, which was wearing `.widget-box`), TWO are an out-of-band pending state where nothing is running in this tab (`deposit-pending`, `win-payout-pending`), and TWO are a DISCLAIMER that never finishes (the prototype note on `terms.html` and `ui-kit/browse-shell.html`). So the cycle is on a compound selector: a progress bar on a legal notice is what the bare class would have drawn. The mark is a 2px rule at `--size-2` sweeping on `--pulse-period`, the SAME period as `sk-pulse` because a spinner and a skeleton are the same STATUS job, and at `prefers-reduced-motion` it stops and becomes full width rather than shortening. Measured on both engines: translate moves 0 to ~77-82 per cent inside 350ms normally, and reads `animation:none` with a 346px bar under the setting, while the four quiet placements gained no `::before` at all. The NAME is still wrong for four of nine placements and that is `docs/backlog.md` 170. |
| ~~`account`~~ | 3 | **HOLDS** `button`, 6 of them. Walked 2026-08-08 on the three screens that carry it; two of the three bars wear `.flat`, which removes everything the file draws. **DELETED the same day.** The walk that gave it a level is the walk that ended it: the file's whole content was the action bar's stone plus the three declarations `.flat` removed it with, the stone stood once of three placements, and its shape, a top border and two top corners, is the surface of a bar that FLOATS over content scrolling under it. Nothing in this product docks. The bar is one face now and the whole of it is `components/patterns/action-bar.css`; the page is `ui-kit/action-bar.html`. Backlog 63 |
| `cookie-consent` | 1 | **HOLDS** `button`, 3 of them, plus its own rows. Walked 2026-08-08. One banner on one screen, three categories, one locked ON and none disabled |
| `toc` | 1 | **HOLDS its own rows**, 14 of them, and they are anchors rather than buttons. Walked 2026-08-08. A rail above 900 and a disclosure below it |

### Level 3, organisms

| Component | Uses | Declaration |
|---|---|---|
| `header` | 668 | **HOLDS** `button`, `chip`, `iconbtn`, `navitem`, `toast`. A shell. **One of its controls left on 2026-08-14 and it is worth naming because nothing was broken by it standing there**: the left group's hamburger, a `<button>` labelled "Menu (reserved for future scaling)" with no handler, no drawer and no destination, `display:none` below the desk on top of that. 105 painted screens, 87 grey ones, 10 kit specimens, one sprite symbol and this file's whole DESK block |
| `footer` | 615 | **HOLDS** `filters`, `iconbtn`, `toast`, `trustbar`. A shell. **AND ITS THREE LINK LISTS TOOK THE 44px FLOOR ON 2026-08-16, `docs/backlog.md` 165, WHICH IS THE LARGEST FAMILY THAT FLOOR HAS EVER TAKEN.** Censused over all 108 documents at 390 with the pointer asserted coarse and the assertion read back in the page: **6,218 targets, 2,566 under 44x44**, and 2,375 of those were three lists here. `.footer-col a` stood **1,187 times at 36x25**, `.popular-links a` **756 at 80x16**, `.legal-links a` **432 at 31x14**. Two of the three are under the 24x24 of WCAG 2.5.8 as well, not only the 44x44 of 2.5.5. Every one is a `<ul><li><a>` of navigation, so the inline exception does not reach them; the 6 links that ARE in a sentence, in `.fine`, stayed out. **Two of the three needed the DISPLAY as well as the floor** (`display:inline`, where `min-height` does not apply), and `.logo` joined in the same edit for its 121 placements at 96x30 outside the header. After: **64 under 44x44, 1.0 per cent**, identical on both engines, and the remainder is the three icon-button faces excluded by name, the 6 inline links, and the sheet grab at 390x24. **The cost is 334px of footer on a phone**, 1,276 to 1,610 mean over 108 screens, and it is entirely below the fold: the mean document grew by the same 335px and nothing above the footer moved. Measured 0 overlapping targets: the boxes are 44x44 with a 4px gap. Behaviour on width: the floor is inside `@media(pointer:coarse)`, so a mouse still reads 36x25 and a touch screen reads 44x44 at any width |
| `hiw` | 1,604 | **HOLDS** `hero` (`.brand-tile` and its six parts) and `position` (`.pos` and its four), which is the arithmetic saying what the ceiling rule already says: level 3 also means the shell of a screen. **This was the last level in the kit that had to be DECLARED, and it is computed since 2026-08-11.** It was filed as `hiw-dialog` at 574 while the file was one block with two hosts plus ten rules about a sheet; the ten are `dialog`'s now and the name stopped saying dialog with them. The 574 is the 41-screen census of 2026-08-07 and the 1,604 is every element wearing one of the thirteen remaining classes across the 105 painted screens on 2026-08-11: **the two are not on one scale**, because the instrument that read 41 screens went with the vitrine, and a figure nobody can reproduce is worse than a figure that says what it counted. **AND IT HOLDS THREE MORE COMPONENTS SINCE 2026-08-14, as PICTURES rather than as parts**: the dialog's stepper stands each of its three steps on a still built from `card`, `betpanel` and `position`, using their own classes with every control replaced by an element that is not one. That does not raise the level, because a picture of a component is not a component held: nothing here reads their tokens, nothing here redraws them, and not one element in the three stages is focusable |
| `dialog` | 291 | **HOLDS** `button`, `chip`, `iconbtn`, `input`, `notice`, `quick`. **It gained `.hiw-dialog`, `.hiw-body`, `.hiw-full` and `.hiw-arrow` on 2026-08-11**, 420 elements over the same 105 screens, with backlog 15 and 18. It does not HOLD the how-it-works block: the sheet host is one element WEARING two component classes, and what it genuinely holds is `.sheet-close` |
| `betpanel` | 120 | **HOLDS** `yesno`, `chip`, `button`, `input`, `quick`, `notice`, `state-block` |
| `tabs` | 153 | **HOLDS** `bets-table`, `comments`, `position`, `button`, `chip` |
| `event-detail` | 128 | **HOLDS** fourteen, and it is the screen's own shell. **126 until 2026-08-17**, when `.ed-result` and its two sides arrived to put a settled market's outcome in the head: the resolved panel that had been announcing it sits at y=167 on the desk and **y=2,227 of a 4,566px document on a phone**, so the reader met the odds explainer, a price-by-bet-size table and the rules first. `.ed-result` is y=344 on the phone. **`.ed-result-no` has 0 placements and is drawn on the stand anyway**, which is the chosen-NO rule: half a symmetric face went unmeasured in this system once already |
| `bets-table` | 89 | **HOLDS** `comments`, `position` |
| `chart` | 84 | **HOLDS** `chip`, `tabs` |
| `card` | 58 | **HOLDS** `yesno`, `oddsbar`, `options`, `iconbtn`, `skeleton` |
| `hero` | 55 | **HOLDS** `yesno` **AND THE STAND SHOWED 7 OF ITS 53 CLASSES UNTIL 2026-08-16**, `docs/backlog.md` 162: `ui-kit/hero.html` carried the brand tile and described the other four blocks in prose, so the chart that gained a scale the same morning had nowhere to be looked at. The whole `.feed-hero` band is on the page now, the same markup the feed carries, in both themes. **Coverage measured against `hero.css` with its comments stripped: 53 of 53**, and the one specimen covers every class because the band is one block. Verified on both engines at 390 and 1280: two bands rendering at identical heights, the chart drawn, five mono axis labels per copy, the photograph loaded, **0 duplicate ids** after the light copy's six ids took the stand's `-lt` suffix, 0 sideways scroll. |
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

Added 2026-08-12 by Responsive step 4 and **RE-MEASURED THE SAME DAY, because the first reading
measured one placement per component and three of its five FIXED verdicts were wrong.** The first
pass took each component's widest single placement at 1440 and read only that one, so the number in
the row was a fact about one slot printed as a fact about the component. `navitem` was published
`FIXED, 258px`, the width of the third most common of its three slots, while the dominant one, 420
of its 995 placements, runs 79 to 159 and is fully fluid. `chip` was published `FIXED, 81px` and is
intrinsic, standing at nine different widths from 18 to 206 in one document. `filters` was published
`FIXED, 152px` and is fixed at five different numbers. Only `logo` and `toggle` survived, and `logo`
survived by half: 86.1 is the header's placement and the footer's fills.

**The table is now a statement about the SET of a component's placements, and where they disagree
the row says so** rather than choosing one. Every element wearing a class that only that component's
file declares was measured, on all 105 screens of `ui-visual/` (`overview.html` is an index and not
a screen), at thirteen widths: **320, 360, 639, 640, 641, 759, 760, 761, 899, 900, 901, 1280,
1440**, three rungs and one pixel either side of each, plus the two phone widths and two desks.
Placements are grouped by the container they stand in, and the row names the container when the
containers disagree.

**The column measures the component against its PARENT'S CONTENT BOX and not against the window**,
and that is the one thing the first pass got right and is kept unchanged. Measured against the
window, 33 of the 43 rows it then had read as stepping at 640, because the page gutter goes 14 to 40
there and takes 51px out of the content column: that is the frame's behaviour arriving in every row.
Measured against the parent's BORDER box, seven more read as changing their share, because the
parent's own padding steps at the same pixel.
**A component that is fluid inside a container that steps is still fluid.**

**A class named by two component files belongs to nobody and is excluded**, or the probe measures
the wrong thing: `.sel` is declared by `bets-table`, `chip`, `options`, `tabs` and `yesno`, and the
other eight are `.feed-seo`, `.no`, `.subcat`, `.toc`, `.w40`, `.w60`, `.w80` and `.yes`. That is 9
of 426 declared class names. Every one of the 47 components still has at least one class of its own
after the exclusion, so no component lost its measurement to it.

**How the state was set, because a state that is not set is a value the instrument picked.** The
review harness (`#rmSidebar`, `#rmOverlay`, `#rmToggle`) was removed before every read, since
`base.css` insets any body that contains it by 220px and a media query reads the window while the
layout gets the container. Every `<dialog>` was opened and every `<details>` expanded, or 337 sheets
measure zero. Animations were finished with `getAnimations().forEach(a => a.finish())` before each
read. **And a second pass cycled every tab radio**, which is the only reason `bets-table` has a row
at all: all ten of its slots live in a panel that is `display:none` until its radio is checked, so
the first reading saw 0 painted placements of a component that is 469 elements on 9 screens.

**The instrument was proved before the finding was believed.** The tree was frozen to a snapshot at
01:44 on 2026-08-12 first, because `components/*.css` was being edited by other hands while the
probe ran and a control taken across those edits reported **13 differing cells, every one of them
`.ed-tabradio` reading 13px in one pass and 1px in the next**, which is an edit to `--hairline` and
not a reading. Against the frozen snapshot, two identical passes gave **0 differing cells of
4,238**. The five verdicts that carry the corrections, `navitem`, `chip`, `filters`, `logo` and
`toggle`, were then re-read against the live tree after those edits landed and are unchanged.

**Three verdicts are not one.** `FILLS` says the box is as wide as its container's content box and
says nothing about how wide that is: `navitem` FILLS in all three of its slots and measures 79, 194
and 258 at one viewport width. So every row carries the pixels as well as the relation.

| Verdict | What it means |
|---|---|
| **FILLS** | as wide as the parent's content box at every width. The pixels are the parent's |
| **CONSTANT SHARE** | a fixed fraction of the parent below 1, unchanged across the ladder |
| **INTRINSIC** | sized by its content: the same value at every width, different values per instance |
| **FIXED** | one number, at every width and in every instance of that slot |
| **CHANGES its share** | the fraction of the parent moves across the ladder |
| **GONE in a band** | not painted at some widths and painted at others |

**47 rows for 47 components.** The first table had 45 and claimed to be filled for every one:
`bets-table` and `bottomnav` had no row at all, and both are measurable, one of them only with the
tabs cycled. Placements are elements wearing a class no other component file declares, counted over
the 105 screens.

| Component | Its own width query | Placements | What it does with width |
|---|---|---|---|
| `action-bar` | 0, and one floor | 3 on 3 | **FILLS** both its containers, 200 to 1,228. Three placements is the pattern threshold exactly, and one face. **Its two halves are equal whenever both fit and unequal only when one cannot**, since 2026-08-15: `min-width:fit-content` on the children plus `flex-wrap:wrap`, which is a floor rather than a query, so the bar has no width behaviour keyed to the window at all. Measured identical at 360, 390, 640 and 1280 and moving only at 320, where 125/125 becomes 126/124. Backlog 154 |
| `betpanel` | 760 | 240 on 11 | **Three faces that never coexist, and the third one was missing from four screens until 2026-08-16.** `.bet-panel` is GONE below 760 and FILLS a 320px column above it; `.bet-dock` is GONE at 760 and above and is a CONSTANT 49 per cent of the dock below it; `.bet-sheet` is what the dock opens, and it was on 4 screens against the panel's 11 because the four bet-state screens had none, so every state of the core act rendered on desktop only. **8 sheets now.** Inside: `.bp-inner` FILLS 280 to 520, `.bp-dir` a constant 49 per cent, `.bp-head` INTRINSIC 54.9-107.3 |
| `bets-table` | 640 | 469 on 9 | **Measured only with the tab radios cycled**, which is why the first table had no row: all ten slots are `display:none` until their radio is checked. The panels and `.act-list` FILL, 285 at 760 to 925 at 1440; `.hold-col` FILLS its column; `.hold-row` and `.hold-name` are INTRINSIC (12-821.6, 36.8-74.8); `.act-row` CHANGES its share |
| `bottomnav` | 640 | 178 on 105 | **FILLS the viewport below 640** (320, 360, 639) and is **GONE at 640 and above**, on all 105 screens. `.bn-bal` inside it is FIXED 36.3 |
| `browse-shell` | 900 | 154 on 77 | **FILLS** both slots. The 900 rule is spent on what the rail takes out of `.cat-layout`, not on the shell's own width |
| `button` | none | 1,224 on 105 | **Six behaviours across fifteen slots.** FILLS in `.sheet-body` (368 to 597) and `.bp-inner`; FIXED 18 for the provider mark, 51.8 in the compose row, 135.8 in the identity row; FIXED 88.4 for the desk-only header button, which is GONE below 760; INTRINSIC in `.cmt-actions` 30.7-36.8, `.auth-btns` 64-69.2 and `.state-actions` 59.9-380; CHANGES its share in `.cta-bar` (96 to 627) and `.cc-actions`. The old row's "GONE in a band, then fixed" describes 105 of the 1,224 |
| `card` | **none**, was 640 | 1,501 on 36 | **FILLS `.grid`, and the box it fills is not monotonic in the window**: 232 at 320, 500 at 640, 300.5 at 759, 371-527 at 900, 368-444 at 1280 and **301.5-330 at 1440**. A card is narrower at 1440 than at 640. Inside: `.top` and `.meta` CHANGE their share, `span in .meta-txt` INTRINSIC 42-72, `.gallery` FIXED 172. **`.prob-line`, 63 placements, is painted at no width**: a page script hides it. **The 640 in this row went on 2026-08-13**: it moved the bookmark's negative margin below the desk and above the desk left one pixel of a 44px target outside the card's clip edge on 84 cards, so the rule is unconditional and the column reads none. The card at 640 is 578 now and not 502, because the page insets ramp: backlog 129 |
| `card-grid` | none | 23 on 23 | **FILLS** `.cat-main`, 234 to 1,262. The column count is a token, not a query, which is why the file has none |
| `catnav` | **900**, was 640, 900 | 90 on 57 | **FILLS all three slots, and one of them changes what filling means**: `.subcat` is 761 wide at 899 and **214 at 900**, because its own 900 rule turns it into the rail. **The 640 went on 2026-08-14**: all it did was add `margin-bottom:var(--space-16)` below the desk, and `.feed .feed-inner` is a flex column with `gap:var(--space-16)`, so a phone got 32px under the strip while a desk got 16. The column already says the number. The rung is still cut for this strip, in `base.css`, where the plate that wraps it trims its vertical padding on the same side of it **And on 2026-08-14 the sub-filter stopped wrapping, with no query at all**: five chips need 332px of row against 298 at 360, so the row stood in two courses and cost 83.0px where one course costs 37.5, at 320, 360 and 390 alike and not at 430. It is `flex-wrap:nowrap` with `overflow-x:auto` now, which is what `.cat-nav` above it has always been, and all three scrollers in the file took a scroll-driven edge fade the same day: `animation-timeline:scroll(self inline)`, so a row that does not overflow has an inactive timeline, falls back to a base style that declares no mask, and shows no fade. |
| `chart` | 760 | 132 on 11 | **FILLS** `.ed-chart`, `.ed-plot` and `.chart-svg`; `.ed-chart-area` CHANGES its share; `.ed-legend` 49-95.2 and `.ed-chart-head` 85.8-124.8 are INTRINSIC |
| `chip` | 640, 900 | 2,276 on 105 | **INTRINSIC, and the published 81px was one instance of one slot.** At a single viewport it stands at 18 (the count inside a nav chip), 24.6-44.4 (the count inside a lane chip), 28.7-45.1 (quick amounts), 36-39.3 (`.ed-range`), 42.2-75.2 (`.feed-subfilter`), 45-68 (the segmented control), 81.4-200 (the lane), 119-132.4 (`.cat-nav`) and 162.3 (load more). **One of the nine moves with width**: the lane chip is 81.4-200 to 899 and 206 at 900, by `.chip-lane{width:100%}` in its own 900 rule. **525 placements are painted at none of the thirteen widths**, the five condensed-band chips per screen: `.cat-condensed` is `visibility:hidden` until `.app-header.scrolled`, and forced open it measures 69.7-82.1 at every width. **A SECOND of the nine moves with width from 2026-08-15, and it is the one this table called INTRINSIC without qualification**: below DESK the nav chip is 44 tall against 48 and its `.cat-nav` band is 99-112.4 against 119-132.4, load more 146.3 against 162.3. All 294 placements, both engines, 0 change at 640 and above. The drop is not the same number in both slots and that is the arithmetic rather than an inconsistency: the padding loses 16 everywhere and the strip's chips lose 4 more because they carry a mark and a gap, which load more does not |
| `comments` | none | 435 on 9 | **FILLS** `.cmt-body`, `.cmt-list` and the panel; `.cmt`, `.cmt.reply` and `.cmt-compose` CHANGE their share; `.cmt-meta` INTRINSIC 50.9-122.4; `.cmt-controls` FIXED 197.8; the avatar FIXED 28 in the holders and activity panels, which need the tabs cycled |
| `cookie-consent` | none | 33 on 2 | **FILLS** eight of eleven slots; `.cc-ph` is a CONSTANT 90 per cent of its row; `.cc-actions` and `.cc-cat-main` CHANGE their share |
| `detail-shell` | 760 | 22 on 11 | `.feed-inner` FILLS; **`.ed-layout` CHANGES its share at 760**, 611 at 639 to 342 at 760, which is the second column arriving |
| `dialog` | 640 | 1,902 on 105 | The sheet **FILLS a box the sheet itself caps**: 292.4-318 at 320, 408 to 462 from 640 up and never wider. Against the body's content box it CHANGES its share, 294.4 at 320 to 410-464 above 640. `.sheet-head` INTRINSIC 32-325.6; `.hiw-full` FIXED 18 |
| `event-detail` | 560, 640 | 162 on 11 | `.ed-main` **FILLS**, 291 at 320 to 981 at 1440; `.rules-panel` CHANGES its share and caps at 586.9; `.ed-head` CHANGES its share, **and since 2026-08-14 it is the one component in this system that asks its CONTAINER rather than the window**: below 460px of `.ed-main` it stacks, because the head is 645 at a 700px viewport and 341 at 760 where the bet panel arrives, so the window and the column move in opposite directions and no window number can name the column. `ui-kit/docs/responsive.md`, the registry of container thresholds. **`.args`, 18 placements, is painted at no width** |
| `feed` | none | 105 on 105 | **FILLS the viewport**, 320 to 1440, one slot and one behaviour. The only component of the 47 whose container is the page |
| `filters` | 640 | 389 on 105 | **FIXED, at five different numbers, none of which moves at any of the thirteen widths**: 121.6 in the footer brand, 150 for the language menu, 152.4-153.5 in `.feed-controls`, 194 for the open panel, 196 for the filter menu. The published 152 named one of the five **BELOW DESK 640 THE PAIR NO LONGER STANDS AT ALL, since 2026-08-14**: 152 and 154 need 314 and the feed column offers 298 at 360, so they stacked, and 360 was the only one of four phone widths paying for the second course. One `.filters-btn` stands in the head instead, **93 wide and 44 tall on a coarse pointer against 34.5 on a fine one**, which is the same pair as the summary it stands in for, because the two are one face in four rules rather than two copies. The pair returns inside a fixed bottom sheet. |
| `footer` | 640 | 2,100 on 105 | `.app-footer` FILLS the viewport to 1280 and **caps at 1400**; `.footer-cols` is 611 at 639 and **120 from 640 up**; `.footer-top` CHANGES its share; `li in .footer-col` INTRINSIC 20.5-65.2; five more slots FILL |
| `header` | **640**, was 640 and 760 | 1,570 on 105 | `.app-header` FILLS the viewport and **caps at 1400**; `.left`, `.row` and `.utility` CHANGE their share; the balance figure is **GONE below 640**; the two menus FILL at 196 and 256-260 and neither moves |
| `hero` | 620, 980 | 76 on 2 | **Eighteen slots on two screens and no majority.** `.hf-info`, `.hero-main` and `.hero-side` FILL; `.feed-hero`, `.hero-duo` and `.hero-feature` CHANGE their share, at 980 and 620 rather than at any rung. **`.hf-graph` was published as a CONSTANT 91 per cent and it is not one since 2026-08-16**: the chart grew a numeral gutter, so the plot is 78.2 to 84.3 per cent of `.hf-chart` and 87.9 to 91.7 of `.hf-graph-wrap`, read at 320, 390, 640, 760, 900, 1280 and 1600. It CHANGES its share, and the 91 was the value of the widest of those readings. **`.hf-axis` is the one slot here that does not move with the window at all**: FIXED 23.1 at every one of the seven, because it is `3.5ch` of IBM Plex Mono at 11px and a `ch` follows the type rather than the viewport. **`.hf-split` is a rule inside the chart's own coordinate system and has no width of its own.** The 76 is re-taken with the two new classes in the set, by the stated method, and comes back 76 at 390 and at 1280 |
| `hiw` | 900 | 1,391 on 105 | `.hiw-sec` 32-717 and `.hiw-faq` are INTRINSIC; `.hiw-cols` CHANGES its share at 900, where the side column arrives. **`.hiw-body` is gone from the dialog on 2026-08-14 and so is the "FILL at 414 from 640 up" that named it**: the dialog is a three-step stepper now, `.hiw-steps` FILLS the sheet at every width, and the two floors under it are FIXED, a 280px stage and a 172px text block, so the sheet stands 564, 564 and 603 on the three steps instead of 552, 641 and 506. **The stage is the one place in the system where three other components stand as PICTURES**, `card`, `betpanel` and `position`, with no focusable element in any of them, so this row still counts none of their elements as this component's |
| `iconbtn` | 560 | **731 on 105**, was 1,361 | **FIXED, at five numbers**: 24 in a toast, 28 in the social row, 32 in a plate head, 36 in the utility row, 44 in the card meta. **ONE slot is GONE below 640**, `.icon-btn.desk-only`, 105 of the 731, and it was two until 2026-08-14: the header's hamburger was the other, and it is deleted rather than hidden. **One placement moves**: `.ed-actions` steps 28 to 36 between 360 and 639, which is this file's own 560 rule. **The published 1,361 does not reproduce and 731 is what the stated method gives**: every element wearing one of this file's eight declared classes, read from the rendered DOM of all 105 screens at 390 and at 1280, both widths agreeing at 731, of which `#l-close` takes 333 and `#i-bookmark-b` 198. The old figure is left named rather than quietly replaced, because a number measured by an unrecorded method cannot be corrected, only re-taken |
| `input` | none | 598 on 105 | **FILLS** the sheet row; `.amount-row` CHANGES its share, 10.9 to 378; `.bp-amount-row` INTRINSIC 18.2-150; the two reconcile boxes FIXED at 158.8 and 39.1 |
| `list-head` | none | 115 on 71 | **FILLS** `.cat-main`; `.feed-head` CHANGES its share, 234 at 320 and 313.9 from 639 up |
| `loadmore` | none | 9 on 9 | **FILLS** `.cat-main`, 234 at 320 to 1,262 at 1440. One slot |
| `logo` | none | 221 on 105 | **Three placements, TWO answers, and the published 86 and the published FILLS were both about a slot rather than about this.** FIXED 86.1 in the header at all thirteen widths, a `<button>` shrink-wrapped in a flex row, and **FIXED 95.6 at all thirteen widths in the other 116**: the footer of every screen, the brand tile and the SEO plate. Those 116 are where the lockup SIGNS a block rather than standing as a control in a bar, and they run `--logo-size:var(--text-20)` with the mark box following at 22.5, because the box is a ratio of the type and not a number. **The footer's FILLS, 292 at 320 and 611 at 639 and 240 from 640 up, was a box being stretched so that a `justify-content:center` had something to centre inside**, which put the lockup in the middle of a 240px column while the tagline under it was flush left; with the centring gone the width does nothing and it shrink-wraps. At the default 16px the lockup measures 78.1, and **the header's published 86.1 is that same lockup plus 4px of press padding on each side** - the number had been carrying the slot all along without saying so |
| `market` | none | 369 on 9 | **FILLS** six of eight slots; `.md-row` CHANGES its share; `.market-head` INTRINSIC 16-177.4 |
| `navitem` | none | 995 on 105 | **FLUID, not fixed, and the published 258 is the third of three slots.** It FILLS its `<li>` in all three, and the three are three widths: in `.bottom-nav`, **420 placements on 105 screens**, `li{flex:1}` gives **79.3 at 320, 89.3 at 360 and 159 at 639**, and the bar is GONE at 640 and above; in the avatar menu, 365 placements, **194** at every width; in the notification menu, 210 placements, **254 at 320 and 258 from 360 up** |
| `notice` | none | 254 on 105 | **FILLS** the sheet body, 368-597; one slot in `.bp-inner` is GONE below 760; `.push-banner` CHANGES its share |
| `oddsbar` | none | 405 on 21 | **FILLS** the card body and the detail head; `.track` is a CONSTANT 38 per cent, and the fill on top of it is a datum written on the element; `.lbls` INTRINSIC 42.9-50.9 |
| `options` | **639.98** | 203 on 14 | **FILLS** `.options` and the card body; `.opt-row` CHANGES its share; `.bp-sel-name` FIXED 23.4 and `.opt-name` FIXED 52. **The query arrived 2026-08-12 and it is a query about the ROW'S NUMBER OF LINES, not about any width in it**: below the desk `.opt-row` is `flex-wrap:wrap`, so the name and the percentage take the first line and the pair takes the second. It was written because the row's min-content is the sum of its parts and it had nothing to give back, so it overflowed a card that clips **AND SINCE 2026-08-17 IT IS TWO QUERIES, THE SECOND ONE ABOUT HOW MANY ROWS THERE ARE.** The card carries its whole field now, 4 rows for two markets and 3 for three more, all summing to 100; below **40rem** the third row onwards is `display:none` and `.opt-more` says how many, at 40rem and above the field is whole and the link is gone. **Measured with animation frozen: the affected grid row 317 to 407 and the feed 1,756 to 1,936 at 1280, +10.3 per cent**, against 386 to 546 at 390, which is 65 per cent of the viewport for one card in a single-column scroll and is why the phone keeps two. The rung is DESK and NOT the width where the grid gains a column: that is **744**, computed by `auto-fit` from `--grid-col-min`, and it belongs to no rung. Read at nine widths on both engines in both trees: **shown plus claimed equals the markup at every one** |
| `platehead` | none | 334 on 105 | **FILLS all six of its slots**, 292.4 at 320 and 408 to 462 from 640 up: the head is exactly as wide as the plate wearing it and has no width of its own anywhere. The cleanest FILLS in the table |
| `position` | 640 | 303 on 23 | **FILLS four containers of four different widths at one viewport**: `.pos-list` 1,142, the tab panel 925, `.cat-main` 1,262 and `.hiw-col-side` 483.9, all at 1440. `.pos-top` and `.pos-figures` CHANGE their share; the table cells are INTRINSIC. Four of thirteen slots need the tabs cycled |
| `position-list` | none | 13 on 13 | **FILLS** `.cat-main` and the profile tab panel |
| `profile` | none | 13 on 2 | `.who` FILLS; `.idrow` CHANGES its share, 72 to 234 at 320. Thirteen placements on two screens is the whole of it |
| `quick` | none | 120 on 105 | **FILLS** both slots: the sheet's row at 378 and the panel's at 288-520 |
| `related` | none | 119 on 10 | `.related-events` and `.feed-inner` FILL; the list's anchors are INTRINSIC, 46 to 1,145.4 |
| `seo-plate` | 760 | 73 on 9 | `.seo-brand` and `.feed-inner` FILL; **`.feed-seo-wrap` CHANGES its share at 760**, where one column becomes two; the heading FIXED 22 |
| `skeleton` | none | 614 on 19 | **CONSTANT shares, which is not the same as changing one.** `.sk-head` 80 per cent, `.sk-row` 49, `.pos.skeleton` 40, `.ed-section` 80; the card body FILLS; `.top` CHANGES its share; one slot is GONE below 760. The published "CHANGES its share" named the one slot of nine that does |
| `state-block` | none | 156 on 40 | Three slots FILL; **the block itself CHANGES its share and caps at 380**: 79.5-250 at 320, 79.5-380 from 639 up |
| `tabs` | **640**, was none | 220 on 20 | **FILLS** `.ed-main`, `.ed-section` and `.cat-main`; the bar and the wrap are INTRINSIC; `.ed-chart-foot` FIXED 172.5 and `.ed-tablabel` FIXED 15.7. The 1px readings in the wrap are the visually hidden radios at `width:var(--hairline)` and are not a defect. **It took its first width query on 2026-08-15** and it changes no button: `.ed-range` drops its well, its hairline and its corner below DESK, so the group is 182 x 44 against 198 x 54, and each of its four chips is exactly 44 x 44 at every width on a coarse pointer, before and after. The ten pixels were the frame |
| `toast` | none | 15 on 1 | **FILLS the group**, which is the page column, so a toast is 234 wide at 320 and 1,262 at 1440 and has no cap of its own. Its inner parts CHANGE their share. Fifteen placements on one screen |
| `toc` | 900 | 31 on 1 | **FILLS, and the container is what moves**: 234 at 320, 761 at 899 and **214 from 900 up**, which is the rail arriving. The link marker is FIXED 13.2 |
| `toggle` | none | 3 on 3 | **FIXED 44** at all thirteen widths, one slot, three placements. The published 44 holds, and it is one of only two components whose every placement holds one number at every width |
| `trustbar` | 760 | 1,260 on 105 | `.footer-trust` and `.footer-inner` FILL; **`.trust-items` CHANGES its share hard at 760**, 631 at 759 and 200 at 760; `.trust-item` CHANGES its share with it |
| `yesno` | **639.98** | 160 on 22 | **FILLS** the card body; `.bp-dir` is a CONSTANT 49 per cent; the dock's pair is GONE at 760 and above. **The compact pair in `.opt-row` was FIXED 96.7 at every width and is now two verdicts either side of the desk**, changed 2026-08-12: FIXED 96.7 at 640 and above, FILLS its row below it, which puts the half at 103 at 320, 123 at 360 and 138 at 390 against 42.7 before. The row it was published under was true and was a statement about a component that could not grow anywhere, since `flex:0 0 auto` was on the halves: **it met the 44px floor on height and missed it on width, at every width there is**, and no reading had asked that axis |

### What the 47 rows add up to, and it is three numbers rather than one

The old summary sentence merged them, and the two files disagreed about which it was: this file said
"33 of the 43" and `components/CLAUDE.md` said "35 of 43 components have no width behaviour of their
own at all". Neither is a reading anybody can reproduce, because 35 was the count of rows that read
FILLS in a table with one placement per component. Measured over every placement:

- **10 of 47 have EVERY painted placement filling its container**: `catnav`, `feed`, `loadmore`,
  `navitem`, `platehead`, `quick`, `action-bar`, `browse-shell`, `card-grid`, `position-list`. And
  `navitem` is in that list while running 79 to 258, which is the reason FILLS alone is not a
  verdict.
- **26 of 47 declare no width query of their own.**
- **8 of 47 are both**, and they are the only components of which "no width behaviour of its own at
  all" is true without a footnote: `feed`, `loadmore`, `navitem`, `platehead`, `quick`,
  `action-bar`, `card-grid`, `position-list`.
- **36 of 47 have placements that disagree with each other**, which is what the one-placement method
  could not see and is the whole reason this section was re-measured.
- **45 of 47 have at least one placement whose pixels move across the ladder.** The two that do not
  are `filters` and `toggle`.
- **9 of 47 have a placement that is GONE in a width band**, and **3 have a placement painted at no
  width at all**: `card` (`.prob-line`), `chip` (the condensed band) and `event-detail` (`.args`).

### The refusal of container queries does not hold on the ground it was refused

Responsive refused them because "a container query with one placement is a media query wearing a
different name", and named the threshold to revisit: **the first component placed in two columns of
different widths.** Measured at a single viewport width, counting only slots with five placements or
more and more than 25 per cent apart:

- **35 of 47 stand in two or more materially different containers**, 22 in three or more, 15 in
  four or more and 10 in five or more. The threshold is not met once, it is met thirty-five times.

**The refusal is answered, and three components carry the case:**

1. **`card` is the decisive one, because its own query is keyed to a window that does not predict
   its box.** `card.css` has one rule, `max-width:639.98px`. The card measures 232 at viewport 320
   (branch on), 500 at 640 (branch off), **300.5 at 759 (branch off)** and **301.5 at 1440 (branch
   off)**. The box at 1440 is within 70px of the box at 320 and 200px away from the box at 640, so
   the branch fires on the one hand and not on the other for boxes of the same size. This is not a
   preference, it is the media query answering a question about the wrong element.
2. **The rail is one container change written as a window query in two files.** `.subcat` goes 761
   at 899 to 214 at 900 by `catnav.css`, and `chip.css` carries its own `@media(min-width:900px)`
   to make `.chip-lane` `width:100%` for the same event. Two files, one number, one cause, and the
   cause is the container.
3. **`navitem` has no query at all and stands at 79-159, 194 and 254-258 in one document**, 995
   placements over 105 screens. Its own stylesheet argued about a control's shape "above 860" in a
   comment until the rung ladder was written. This is exactly the component the threshold described.

**No container query is written here and none may be**: this file does not own `components/*.css`.
The finding is filed as a measurement so the Responsive stage can act on it, and the honest
statement of it is that the refusal was correct when it was made about a table with one placement
per component, and is not correct about this one.

**ANSWERED 2026-08-13, AND THE COUNT ABOVE IS TRUE AND DECIDES NOTHING.** `docs/backlog.md` 129 was
closed by measuring the other half of the same question, and the correction belongs here because
this section is where the count was made. **Standing in two columns of different widths is a
NECESSARY condition and was read as a sufficient one.** It says nothing about whether the component
has anything to say about width, and the table above this section says **35 of 45 fill their
container with no width behaviour of their own at all**: a component with no rule has no branch that
can fire wrongly, so thirty-five of the thirty-five are components that would not use a container
query if they had one. The population that can misfire was taken from the queries instead - **52
selectors inside the 33 width queries `components/` held on 2026-08-13, of which 14 are the page
frame, the shell or the harness, 2 set a positioning context and 36 are a component in a slot** - and
the reading is stamped rather than restated because **the registry has moved three times since and
stands at 34**, so a present-tense 33 here would date a finding to a tree that no longer exists. What
the added query does not change is the verdict: it is one control's own narrow-side block, in the
group already classified as a component in a slot - and the 25 that stand
on both sides of their own rung were read against their PARENT'S CONTENT BOX on all 105 screens.
**24 of 25 are separable**: some container width divides the placements exactly the way the rung
does, so a container query would resolve identically everywhere. **Of the three components named
above, `card` carried the case and the rail and `navitem` did not.** `navitem` has no width rule at
all and a component with no rule cannot answer wrongly; the rail's container reads 761 on one side
of RAIL and 214 on the other, which separates. `card`'s rule was the bookmark pull, and it was never
a phone fact: the bare icon button pulls its 44px target back by 14px, a card has 13px from content
edge to clip edge, and **one pixel of that target was being cut off 84 cards at every width from 640
to 1600** while the query hid it below the rung. It is unconditional now. The account is in
`responsive.md`, container thresholds.

## Motion

Added 2026-08-15 by Animation step 3. **The column is the list the Rollout stage checks against**:
a new screen inherits movement from `components/index.css` and reads the row of its component
rather than inventing a transition.

**A movement does one of three jobs and there is no fourth.** RESPONSE, a control answering a
finger. CONNECTION, an element arriving and saying where from. STATUS, a process still running. A
moment for which none of the three can be named does not enter the register, so it never gets
movement, and "it livens up the interface" is not a job.

**Two durations carry all of it**, `--dur-fast` at .16s and `--dur-slow` at .25s, with
`--pulse-period` at 1.4s beside them as a PERIOD rather than a rung. Two curves,
`--ease-standard` and `--ease-enter`. There are no literals: measured from the comment-stripped
source, **0 duration literals and ONE bare easing keyword in 54 stylesheets**: `linear` on
`animation-timing-function` in `catnav.css`, deliberate and declared, where a scroll timeline needs
the identity. **It was published as 0 and the closing audit corrected it**, because the check that
produced the zero read the shorthand and never looked at the longhand.

### 26 of 47 move, and the other 21 are not an oversight

| component | job | what moves |
|---|---|---|
| `betpanel` | response + connection | the grab handle answers; the sheet rises from the bottom edge, `betSheetUp` |
| `button` | response | border, ground, ink and shadow on hover and press; the provider face also lifts |
| `card` | response | the hover lift and its shadow. **It was `.3s` until 2026-08-15**, the slowest hover in the product against the button's .16, which is the textbook drift this stage exists to find |
| `chart` | response | a market line brightens and thickens under the pointer |
| `chip` | response | ground and ink across the whole chip family |
| `cookie-consent` | response | the policy link's underline. **The checkbox beside it is deliberately not given one**: its state moves `accent-color`, which is not animatable, so a transition there would be a rule that never fires |
| `course-chrome` | connection | the review drawer slides in. Harness, not product |
| `dialog` | connection | `sheet-rise`, and on the phone it is 337 dialogs across 105 screens |
| `filters` | response | the summary chips and every row of the sheet |
| `footer` | response | link ink and ground. **`text-decoration` is not in the list on purpose**: an underline fading in from nothing reads as a rendering fault rather than as an answer |
| `header` | connection | the condensed category band opening under the header |
| `hero` | response | the trust and feature tiles lift. **Also `.25s` until 2026-08-15**, a second hover on a third number |
| `hiw` | response | the step dot |
| `iconbtn` | response | five of its eight faces, 14 declarations, the largest single reader of `--dur-fast` |
| `input` | response | the amount field's edge, glow and quiet |
| `market` | response | the head's ground and the chevron turning over |
| `navitem` | response | the row's ground. **1,068 placements on 105 screens and it had no transition at all until 2026-08-15**, the largest silent surface in the product |
| `options` | response | the "more" link's ink |
| `position` | response | the plate and its question. **996 placements, silent until 2026-08-15** |
| `related` | response | the "more" control |
| `skeleton` | **status** | `sk-pulse`, 482 marks on 19 loading screens. **The only place this product performs the status job, and it performed it zero times until 2026-08-15** |
| `state-block` | response | the recovery link. 152 placements, silent until 2026-08-15, and every one of them is the way out of a state a person did not want |
| `tabs` | response | both tab families |
| `toc` | response | the contents rail and its head. Silent until 2026-08-15 |
| `toggle` | response | the knob and its track |
| `yesno` | response | both sides of the outcome control and the pick |

`catnav` is the twenty-seventh and it is held apart: it carries `edge-fade`, a mask bound to the
element's own scroll position rather than to time. **None of the three jobs describes it**, because
it is an affordance and not a moment, and the ruling on whether it stays is Animation step 4.

**The 20 with no motion, and the reason is the same for all of them: nothing about them changes.**
`action-bar`, `bets-table`, `bottomnav`, `browse-shell`, `card-grid`, `comments`, `detail-shell`,
`event-detail`, `feed`, `list-head`, `loadmore`, `logo`, `notice`, `oddsbar`, `platehead`,
`position-list`, `profile`, `quick`, `seo-plate`, `trustbar`. Six of them are the whole of
`patterns/`, which carry arrangement only, and a rung whose invariant is that it holds no colour
and no face holds no movement either. **A blank here is a component with no state to move between,
not a component nobody measured**, which is the distinction this repository has already paid for
once at a zero.

**`toast` is the one blank that is an order rather than an answer.** A toast arriving and leaving
is the clearest connection moment in the inventory and the component has no state for it: nothing
in the system says "entering" or "leaving", and drawing one here would be a class the product never
wears. It is a component order, not work for this stage, and it sits in `backlog.md` with
Load more, which has the same shape.

**No per-page motion subsection was written, on the same ground the width one was refused.** The
systematic answer is one table read in one place; 26 fragments scattered over 26 pages is 26 things
to keep in step and one place for them to disagree. The exception is `skeleton.html`, which gained
a section because the component itself changed on 2026-08-15 and its page would otherwise describe
a still box that no longer exists.
