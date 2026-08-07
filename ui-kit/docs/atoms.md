# The atom map

**This is the target, not the registry.** `inventory.md` says what the system HAS;
this says what it is supposed to be, so that every migration has a distance to close and
the work can end. It was written on 2026-08-05, after four passes that each fixed a real
defect and none of which moved the system toward a stated shape.

Nothing here is a rewrite. Every value in `components/` stays: the two token levels proven
in both themes, the 378 contrast fixes, the target sizes, the focus ring now measured on
every focusable control, the voice table. **What moves is which file a rule lives in**, and
that is exactly the operation `ui-kit/_verify/snap.cjs` proves at 525 snapshots and zero
differences. It has been done four times this week at zero each.

---

## Why the shelf is wrong, measured

    40 css files, 1289 rules, 555 classes
    82 per cent of rules reach a control
    40 files of 40 style a control
    25 kinds of button-shaped control, 5281 placements, in 21 files

    L1 atoms  (6): button chip input loadmore oddsbar toggle
    L2       (13): account comments cookie-consent filters market quick related ...
    L3       (19): header footer card dialog betpanel feed profile event-detail ...

**That is not atomic design, it is a partition by screen region.** `hero.css` is 97 rules
and 52 classes, which is a whole band of one screen. `header.css` is 92 and styles four
different controls. The components were not designed, they were READ out of already
painted screens - `ui-kit/kit.html` says so about itself - so a component equals a css
FILE, and the files were cut by what happened to appear on a screen. `loadmore` looks
absurd on the atom shelf not because it is misfiled but because the whole shelf is an
artefact of that cut.

The second cause is one number doing two jobs. `ui-kit/_levels.py` computes containment
for the CASCADE, which is the only right answer to "a part is imported before the whole",
and the level was then read off the same number. Containment is arithmetic; a level is a
decision.

---

## What makes two controls one atom

Two rules, and both are already the house's:

1. **Same MEANING, which the role is how you check.** `ui-kit/_worn.py` files every
   control as action, selector, nav or stand, because a `<button>` is a tag and not a
   role. Two controls that LOOK the same and MEAN different things are not one atom:
   that is `tab` against `chip`, and `outcome` against `chip`.
   **This rule said something stronger until 2026-08-06** - *two controls in different
   roles are never one atom, however alike they look* - and the `navitem` migration
   measured a case where that is false. The social mark is nav by role and an icon
   button in every value a face has. An atom is what a set of RULES is shared by,
   because a set of rules is what a css file holds, so the FACE settles it and the role
   is the check that stops two identical faces meaning two different things.
2. **The difference is a MODIFIER, not a face.** If what separates them can be named as
   emphasis, size, or ground without inventing vocabulary, it is one atom with a
   modifier. If the difference carries MEANING, it is two atoms. Green and red are
   outcome semantics in this product, so a control whose colour states a result is not a
   variant of one whose colour states emphasis.

The test that settles an argument is the one that settled the buttons and the chips:
**measure both, then read the two declarations side by side.** Five button names ended
that way, and `.seg button` and `.ed-range button` turned out to be the same declaration
block byte for byte.

---

## The atoms

Seven control atoms and six that are not controls. Every placement the census counts is
covered exactly once; the numbers add to its 5281.

### Controls

| Atom | What it is | It absorbs, and the count | Today |
|---|---|---|---|
| `button` | a press with a LABEL, that does a thing | the button family **710**, how it works **105**, a comment's own action **72**, post a comment **11**, load more **9**, cookie consent **3**, edit on the profile **1** = **911** | `.btn` already holds 710 of them, with emphasis, size and block. The other four are the same control redrawn in four files: same radius-10 or pill, same semibold label, same 44 floor |
| `iconbutton` | a press whose whole content is a MARK | header icons **388**, sheet close **333**, social marks **525**, bookmark on a card **84**, an event's action row **27**, toast close **4** = **1361** | **one file since 2026-08-06**, and it was six. Six names, one idea: a square or a disc sized to the finger with an icon in it. It is a separate atom from `button` and not a modifier of it, because it has no label to size and its whole box is a target |
| `chip` | a label you PICK BETWEEN, that carries a value | category chip **815**, quick amount **480**, quiet chip in a rail **63** = **1358** | the largest family and the most divided. `components/chip.css` exists and holds 63. The differences are pill against radius-10, 13px against 12px, and the ground at rest, which are modifiers |
| `tab` | a selector whose selection swaps a PANEL rather than carrying a value | the tab row **36** | its own atom since 2026-08-06, and the measurement recorded below is what made it one. `.ed-tablabel` and `.ptab-lbl` are the same control again as labels, so they join it when the non-button controls are counted |
| `outcome` | the YES / NO pair, where the COLOUR states a result | YES/NO buttons **230**, the outcome side of a bet **40**, the hero's featured pair **2** = **272** | genuinely its own atom and must never fold into `chip`. `DESIGN.md` decides it: green and red are outcome semantics, brass is the brand, and an accent never borrows the win or lose colour |
| `switch` | one setting, on or off, answered on the spot | toggle **3** | already `components/toggle.css`, already correct, and it stays one because a switch is not a chip with two states: it says yes or no to one thing rather than choosing among several |
| `navitem` | a thing you tap that GOES somewhere and that draws NOTHING until it is pointed at | bottom nav slot **420**, account dropdown row **365**, a sub-category row **234** = **1019** | three files, and it was four: the social mark left on 2026-08-06 for `iconbutton`, measured rather than argued. What is left agrees at rest - transparent, no edge, no corner, as wide as its label - so a slot with a mark over a label and a row with a label are one control at two sizes. The active state is a state of the item, not a fourth control |

### Not controls, and still atoms

| Atom | Placements | Note |
|---|---|---|
| `mark` | **4007** svg on 105 screens | the icon. Already one sprite and one page, `ui-kit/icons.html`, and it is the atom every `iconbutton` and half the `navitem`s contain |
| `choice` | **1057** radio and checkbox | the labelled radio in a filter panel and the consent checkbox. Styled today inside `filters.css` and `cookie-consent.css` |
| `field` | **121** text inputs | already `components/input.css`, minus the chips that left it on 2026-08-05 |
| `label` | **245** `.field-label` | the word above a field. It stays with `field` unless a second consumer appears |
| `skeleton line` | **482** on 19 screens | a STATE rather than a control family, and `_levels.MODIFIER` already says so |
| `bar` | **9** odds bars in markup, the rest built at run time | already `components/oddsbar.css`, a datum drawn to a width |

### Deliberately not an atom

- **`logo`, 105.** A brand mark is not a control family: there is exactly one, it never
  varies, and giving it a modifier vocabulary would be inventing a system for a single
  element.
- **the sheet grab, 4.** A handle, not a press. It answers a drag.
- **the vitrine's own chrome, 212.** `course-chrome.css` is the panel this repo wraps
  around every page. It ships with the system and it is not the product.

---

## What the atoms leave behind

Everything else in `components/` is a **composition or a region**, and that is fine: a
region is allowed to exist, it is just not allowed to draw a control. `header.css` may say
where the icon buttons sit in the bar; it may not say what an icon button looks like. That
one sentence is the whole migration.

The line to hold, and it is already written in `CLAUDE.md`: new goes into the SYSTEM
first and onto a screen second. What was missing is the other direction - a region that
quietly redraws an atom - and that is what gate 40's shape can be turned into.

---

## The distance, and how it is closed

**The distance is 17, and the build prints it.** It is file-slots minus atoms: each
atom should be drawn in exactly one file, the six control atoms are drawn in twenty-three
today, and seventeen of those slots are somewhere an atom does not belong.

    41 the atom map    6 control atom(s) in 23 file-slot(s): distance 17, and it goes to 0
                       chip        1628 use(s), 4 kind(s), 5 file(s): catnav chip header quick tabs
                       navitem     1310 use(s), 3 kind(s), 3 file(s): bottomnav footer header
                       iconbutton  1013 use(s), 6 kind(s), 6 file(s): card comments dialog
                                                                      event-detail header toast
                       button       734 use(s), 5 kind(s), 5 file(s): button comments
                                                                      cookie-consent loadmore profile
                       outcome      272 use(s), 3 kind(s), 3 file(s): betpanel hero yesno
                       switch         3 use(s), 1 kind(s), 1 file(s): toggle

**A file counts when it DRAWS the control, not when it places the container**, and the
first cut of the metric got that wrong: asking which files mention the class put
`base.css` and `patterns/browse-shell.css` on the chip's list, because both style
`.cat-nav`, the plate the rail stands on. That is a region doing exactly what a region is
allowed to do. The test is on the selector's last simple-selector, and the number went 19
to 17 the moment it was fixed. That is the argument for computing the distance rather than
counting it by eye.

Each step is one atom:

1. **Declare the map in code.** Done 2026-08-05: `_worn.ATOM` names the atom of every
   kind, and **gate 41** holds it in three directions, each tested against a wrong state
   before being trusted - a kind that names no atom, an atom no kind names, and a row
   naming a kind the census no longer has. Nothing fails on the distance itself: a target
   you can fail is a target that gets widened, so it is a NOTE, and it goes down.
2. **One atom per pass**, largest first, because the largest are the ones a person sees:
   `chip` 1628, `navitem` 1310, `iconbutton` 1013, `button` 734, `outcome` 272.
3. **Each pass is proved the same way**: `snap.cjs` before and after, both trees, five
   widths, and the diff at zero. A migration that changes a pixel is a migration that
   made a decision it did not declare.
4. **The level then stops being read off containment.** With the atoms declared, the
   `RAISE` and `TRUE_ATOM` lists shrink to the handful of genuine surprises they were
   meant for.

---

## What the first migration refused, and the map was corrected instead

**2026-08-06. The chip migration was the next step and it did not run.** Before moving
about 1,565 buttons per tree, the family was read out file by file, and the reading refused
the target twice. Both corrections are in the table above, and neither would have been
found by executing the plan.

**`.subcat` is not a chip.** It sat in the category kind because of the family name.
`components/catnav.css` draws it `width:100%` with `justify-content:space-between`, which is
a full-width row with a label on the left and a count on the right, and its container is
`<nav aria-label="Sub-categories">`. **234 placements moved to `navitem`.** Reading it as a
chip was reading the family name, which is the same mistake as reading the tag.

**A `tab` is not a chip either, and the counter-argument written below is the one that
held.** The map placed 36 tabs in `chip` on the strength of the drawing, and the drawing
turned out not to agree with itself: `.rules-tab` is transparent, has no corner and carries
a 2px underline; `.tabs button` is a pill on `--bg-chip` at 13px. **An underline against a
pill is a face, not a modifier**, so they were never one chip. What the two share is what
they DO, and that is the atom.

**The distance did not move, and that is correct.** 17 before and 17 after: seven atoms in
twenty-four slots where there were six in twenty-three. No rule moved, so no progress was
made toward the target, and the number does not pretend otherwise.

**And the chip family carries a product decision the partition cannot take.** Its selected
state is spelled five ways: `--tint-brass-09` with a `--tint-brass-45` edge and a glow on
the category chips, `--tint-brass-16` on the quick amounts and the quiet chip,
`color-mix(--color-action 18%)` with an action edge on the sub-category row,
`color-mix(--color-action 16%)` on the tab row, and a full brass GRADIENT in the grey layer.
`DESIGN.md` says one thing: active is a brass tint. Migrating at zero difference means
carrying all five as named modifiers, which at least puts them in one file where the
question can be asked; unifying them is a visible change on about 1,100 placements and
belongs to `ui-kit/docs/backlog.md` S35, not to the partition.

---

## The first atom moved, 2026-08-06, and the distance did not fall

`components/iconbtn.css` exists. The largest of the six icon-button kinds, the header's own
row of circles, is in it: **`.icon-btn` with `.bal-swap` and `.bal-add`, 534 placements, and
not one byte of markup moved**, because those elements already carried the class. What
stayed in `components/header.css` is `.app-header .left > .icon-btn{display:none}`, since
hiding a control in a band is the band's decision. Three shared selectors were SPLIT rather
than moved, because each also styled the header's own `<summary>` disclosures. Proved:
**525 snapshots, five widths, both trees, 0 differ, 0 elements changed.**

**The distance went 17 to 18, and both halves of that are honest.** The move itself changed
it by nothing: `iconbutton` was drawn in six files before and is drawn in six after, because
the atom moved house rather than gaining a tenant. It falls when the other five kinds adopt
it, and that is the next five passes. The rise is the map getting more accurate again:
**`.hiw-btn` is not an icon button.** It sat in the census row called "icon only, in the
header" carrying the words *How it works* on 105 screens, so it is a labelled press and
belongs to `button`, and pulling it out put `header.css` into `button`'s column where it had
been hidden. That is the third correction the map has taken from a reading, after `.subcat`
and the tab, and all three were found by reading the family out before migrating it.

**A file counts when it DRAWS the control, and a rule that only PLACES one does not.** The
metric said 19 for a moment, because `.app-header .left > .icon-btn{display:none}` ends at
the control and the test was on the selector alone. Placement is where and whether; a face
is what it looks like; a rule now has to set at least one face property to count. That is
the second correction to the number in two days, and both were caught because the number
moved the wrong way.

---

## The first adoption, and the distance falls: 18 to 17

**`.sheet-close` is `.icon-btn.icon-btn-photo` since 2026-08-06.** 333 dismissals on 105
screens, the second of the six icon-button kinds, and the first migration in this run that
moved markup: every one of them now reads `class="icon-btn icon-btn-photo sheet-close"` in
both trees. What it is, what face it wears, and the hook the overlay positions it by.

**The face is a face and not a second control.** Everything separating the close disc from
the ghost circle is the SURFACE it stands on: an event photograph under a scrim. So the
ground is the scrim, the edge and the ink are the on-photo roles, and its two states deepen
the scrim rather than tinting brass, because a brass tint on a photograph is a colour nobody
chose competing with one nobody controls. `components/tokens.css` had already named all
three roles.

**`components/dialog.css` keeps where it sits and nothing else**: absolute, 12 in from the
corner, above the head. That is the line the whole migration is written on.

**One declaration nearly stayed behind, and moving it is what made the number fall.** The
overlay carried `dialog.app-dialog.hiw-dialog .sheet-close:focus-visible{outline-color:...}`
- the ring goes light on exactly one head, because `.hiw-glow` puts a brass radial in the
corner the ring lands in and a brass ring measures 2.52:1 there. **An outline-colour is what
a control looks like**, so by this document's own rule it could not stay in a region. The
fact is the overlay's and the vocabulary is the atom's: `.icon-btn-ring-strong` says what a
light ring IS, and the overlay asks for it by putting the class on the element, 192 of them
across both trees. Only then did `dialog` leave the icon button's column: **18 to 17**.

**And the proof asked for one line.** The first before-and-after came back 55 screens and
165 elements changed, all of them `lineHeight: 24px -> 0px`: the atom's base carries
`line-height:0`, which a button holding nothing but an svg wants, and this control never had
it. Nothing moved on screen, and a diff of 165 is still a diff, so the face takes back what
it inherited. **A partition that changes a computed value is a partition that made a
decision it did not declare.** Re-measured: 525 snapshots, five widths, both trees, 0 differ.

**The 44 floor deliberately does not reach this face**, and that is preserved rather than
decided. The dismiss is 32 under a coarse pointer today, which clears WCAG 2.5.8 and not
2.5.5, and the atom's floor excludes the photo face so that adopting it changes no pixel.
Whether it should be 44 is S39's question; a migration is not the place to answer it quietly.

**The census learned that order matters.** Its reader returns on the first row whose classes
match, which was harmless while every kind owned a name nothing else used. It stopped being
harmless the moment a control adopted an atom: the generic `.icon-btn` row would have
claimed all 333 closes and `close, a sheet` would have gone idle, which is what gate 38 said
out loud. A row naming a FACE is more specific than one naming the atom, so it comes first,
and every kind that adopts an atom from here on joins that block.

---

## Three more adopted, one refused, and the distance falls 17 to 15

**`.bookmark-btn` is `.icon-btn.icon-btn-bare`**, 84 placements, and it proved at **525
snapshots, 0 differ** on the first try. The bare face is the one with no ground and no edge
at all: it sits on a card's caption row beside a photograph, where a circle would be a
second object competing with the picture, so what answers the pointer is the MARK. Its whole
44 target is invisible and pulls itself back out of the flow, because an untouchable box
that spreads the row it sits in is the atom's problem wherever it stands, not the card's.

**`.cmt-actions button` is not an icon button, which is the fourth correction the map has
taken from a reading.** The two controls in a comment's meta row are
`<button><svg/>24</button>` and `<button>Reply</button>`: a mark beside a COUNT, and a word.
Neither is icon-only. 72 placements moved to `button`.

**`.ed-actions button` and `.toast-close` REFUSED, and the refusal is the useful part.**
Both set no `padding` and no `display`, so both took the user agent's: **1px 6px, and
`display:block`**. Adopting the atom hands them `padding:var(--space-4)` and
`display:inline-flex`, and on the event action row that is visible: **the 18px mark was
being squeezed to 14px wide by the 6px of UA padding**, so the atom un-squeezes it. 17,478
boxes changed, and 270 marks changed colour as well, because the atom hands a sprite
`--text-primary` where `.ed-actions` had handed it `--text-muted`.

**None of those values was decided by a person**, and the bookmark is the control for the
experiment: a face that WAS decided adopted the same atom at zero the same afternoon. Both
faces are written and reverted, so the adoption is a re-apply once three questions have
answers: is the event action mark 18 or 14, is it muted or primary, and is the toast
dismiss the same hover as every other outlined icon button. `ui-kit/docs/backlog.md` S44.

    41 the atom map   7 control atom(s) in 22 file-slot(s): distance 15, and it goes to 0
                      navitem     1544  4 kind(s), 4 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      button       911  7 kind(s), 6 file(s)
                      iconbutton   836  5 kind(s), 3 file(s)   <- was 6 files this morning
                      outcome      272  3 kind(s), 3 file(s)
                      tab           36  1 kind(s), 1 file(s)
                      switch         3  1 kind(s), 1 file(s)

**And the census learned the same lesson twice in one day.** Its reader returns on the first
matching row, so `bookmark, on a card` went idle the moment its elements also carried
`.icon-btn`, exactly as `close, a sheet` had that morning. Every kind that adopts an atom
moves into the specific block above the generic one, and gate 38 is what says so.

---

## The first atom closes: 15 to 13, and it cost three decisions

The last two icon-only kinds adopted on 2026-08-06, and they are the two that had been
refused the day before. Nothing about them had changed. What changed is that somebody
answered the three questions `ui-kit/docs/backlog.md` S44 was holding, and the whole of
this step is the re-apply.

**The refusal was the useful part.** `.ed-actions button` and `.toast-close` had never set
`padding` or `display`, so both were wearing the user agent's `1px 6px` and `display:block`
and neither value had ever been chosen by a person. Adopting the atom replaces them, and on
the event action row it shows: an 18px mark that a 28px tile was flex-shrinking to **14**.
A migration is allowed to move a rule between files. It is not allowed to answer a design
question on the way, and the difference between the two is exactly whether anybody was asked.

    the mark on the action row     18, because that is what the file has said all along
    its ink                        --text-muted, because it is a quiet toolbar on a photograph
    the toast dismiss's hover      the same as the other 388: tint the ground, brass the edge

**Measured after: 525 snapshots, 50 pages, 209 elements, and every one of them named.** 54
are the 27 marks and their `<use>` children growing 14 to 18 at 380px, which is the decision
being visible. 155 are `padding`, `display` and the two flex alignments, on boxes of fixed
size holding one centred child or nothing at all. No box moved. No colour changed.

    41 the atom map   7 control atom(s) in 20 file-slot(s): distance 13, and it goes to 0
                      navitem     1544  4 kind(s), 4 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      button       911  7 kind(s), 6 file(s)
                      iconbutton   836  5 kind(s), 1 file(s)   <- closed
                      outcome      272  3 kind(s), 3 file(s)
                      tab           36  1 kind(s), 1 file(s)
                      switch         3  1 kind(s), 1 file(s)

**One atom, 836 placements, five faces, one file** - and the five faces are the answer to the
question this document opened with. They are not five variations on a circle. Each one is an
answer to the GROUND it stands on: nothing (the header), a photograph under a scrim (an
overlay head), a caption row beside a picture (no ground at all, the mark alone answers), an
ordinary surface in a corner (a tile, so three of them read as a toolbar rather than a
control group), and a lifted card at 24 (the same circle, smaller). A face is a surface, and
that is worth carrying into the four migrations left.

**What the vitrine cost, and it was not free.** The three tiles in `ui-kit/kit.html` carry no
class, because `.ed-actions button` had reached them by tag. The helper that adopts an atom
matches a class, so it adopted 27 controls in the product and none of the three in the stand
that exists to show what the component is, and no gate noticed. `ui-kit/docs/defects.md` row
76. `outcome` will ask this again.

**And the stand was showing one face out of five.** Found while checking the above: the
iconbtn page staged the balance pill and nothing else, so four of the five faces this atom
now owns had no picture on the page that is supposed to BE the picture. Each of them already
stands in a specimen somebody else owns, so the fix is four words in the curation:
`dialog-shared`, `card-binary`, `toast` and `event-detail` are now `also` iconbtn, and each
face is shown in the surface it was designed against, which is the only place it means
anything. Containment is read from `component` and not from `also`, so the level is unmoved
and the atom is still an atom.

---

## The open question was answered by measuring it: 13 to 12

The `navitem` migration began the way the `chip` one did, by reading the family out before
moving anything, and it stopped on the first kind. **The map had one of the four in the
wrong atom**, and this document is where it said so: *"Is a social mark a `navitem` or an
`iconbutton`? The map follows the ROLE, which is rule 1, and rule 1 has never been wrong
here."* Rule 1 was wrong here.

`navitem` claimed that a slot with a mark over a label, a row with a label, and a bare mark
are **one control at three sizes**. Nobody had measured that sentence. Read in the browser
at 1440 and at 380:

| the four kinds | ground | edge | corner | shape |
|---|---|---|---|---|
| bottom nav slot, 420 | transparent | 0px | 0px | column, 10px bold, mark over label |
| account dropdown row, 365 | transparent | 0px | 0px | inline-block, 11px, label left |
| sub-category row, 234 | brass tint 18% | 1px brass | 10px / pill under 860 | label left, count right |
| **social mark, 525** | **`--bg-control`** | **1px hairline** | **10px** | **centred flex, 18px mark, no label** |
| `.icon-btn-tile`, for comparison | `--bg-control` | 1px hairline | 10px | centred flex, 18px mark, no label |

The first two agree with each other on every value a face has. The fourth agrees with
**none** of them and with the tile face on **all** of it: `rgb(36,40,47)` against
`rgb(36,40,47)`, `rgb(43,47,56)` against `rgb(43,47,56)`, 10px against 10px, 28 against 28
at mobile. A ground, an edge and a corner against transparent, none and none is a FACE, and
rule 2 says a face is not a modifier.

**So rule 1 is stated correctly now, and it is a smaller rule than it looked.** An atom is
what a set of RULES is shared by, because a set of rules is what a css file holds, and that
is settled by the face. The role is what catches the other case: two controls whose faces
agree and whose MEANINGS differ, which is `tab` against `chip` and `outcome` against `chip`.
Role had never actually partitioned anything here until it tried to, and when it did it was
wrong. The social mark stays filed `nav` in the census, because that is what it means; its
rules live with the atom it looks like.

    41 the atom map   7 control atom(s) in 19 file-slot(s): distance 12, and it goes to 0
                      navitem     1019  3 kind(s), 3 file(s)   <- was 1544 in 4
                      chip        1358  3 kind(s), 4 file(s)
                      button       911  7 kind(s), 6 file(s)
                      iconbutton  1361  6 kind(s), 1 file(s)   <- still one file
                      outcome      272  3 kind(s), 3 file(s)

**And it cost the markup this time, which is defect 76 arriving on schedule.** `.social-row a`
reached its 525 controls by TAG, so not one of them carried a class, so the helper that
adopts an atom by class could not see them. A second helper walks the CONTAINER and marks
the children of a given tag inside it; it is what `outcome` will need too.

**What the move did not settle is written down rather than decided.** This face and the tile
are the same picture at rest and answer the pointer differently: the tile brightens its ink,
the social mark lifts two pixels and tints its ground. 27 against 525. `ui-kit/docs/backlog.md`
S45, and the interesting answer there is probably not "pick one" but "a face answers the
pointer by its SURFACE", which is what all six faces of this atom have turned out to be.

---

## The second atom gets a file, and it is the first that never had one: 12 to 11

`navitem` was the only control atom on this map with no `components/*.css` of its own. Two of
its kinds measure exactly what the map says the atom is - **draws NOTHING until it is pointed
at** - and they came from two regions.

    the bottom nav slot         420 placements   components/bottomnav.css
    a row of the account menu   365 placements   components/header.css

Read at rest, at 1440 and 380, both themes: **transparent ground, 0px border, 0px corner, full
width, a press on `--bg-pressed`.** Every one of those agrees. What differs is a direction, a
size, an ink and an alignment, which are modifiers. So the shared line is written once and each
face keeps its own answer to the pointer: a neutral `--tint-hover` wash on the bar, the brass
wash the rest of the header uses in the menu. **525 snapshots, 0 differ, 0 elements changed.**

**That makes it three atoms in a row whose faces agree at rest and part on the pointer** - the
icon button's six, the tile against the social mark, and these two. S45 asks whether that is a
rule rather than a coincidence, and the evidence is now three for three.

**One rule in the new file is load-bearing and it is a specificity fact.** Each hover is written
`.nav-item.nav-slot:hover`, at the face's own two-class weight, because the current-page state is
`[aria-current="page"] .nav-item.nav-slot` at (0,3,0) and a hover at (0,2,0) would die on exactly
the slot a person taps most. `components/bottomnav.css` had bought the same weight by naming the
`<li>`, and its note said so; the note travelled with the rule.

**The cascade found a real cycle, and it is declared rather than broken.** The bar holds the
slots, and the Portfolio slot holds `.bn-bal`, the bar's own balance figure. `_levels.ORDER_BREAK`
now carries `("navitem", "bottomnav")`: the bar is the whole, so the slot loads first, and
`.bn-bal` is one `<span>` of content a region puts inside its own control.

    41 the atom map   7 control atom(s) in 18 file-slot(s): distance 11, and it goes to 0
                      iconbutton  1361  6 kind(s), 1 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      navitem     1019  3 kind(s), 2 file(s)   <- was 3 files
                      button       911  7 kind(s), 6 file(s)
                      outcome      272  3 kind(s), 3 file(s)

**Two kinds were left and each was left for a measured reason, not for time.** A sub-category row
measures as a hairline PILL at 380 and a 10px full-width row above 860, so it is neither this
atom's rest face nor a `chip`; it was filed here on the strength of the desktop rule alone, which
is the same half-measurement that put the social mark in the wrong atom. A notification row is the
account row with a different content and shares three declarations with it in one file under two
names, held back by a `display` and a `font-size` that nobody chose. Both are `ui-kit/docs/backlog.md`
S46, and together they take the distance to 9.

**And the leftover in `bottomnav` is not a rule at all, it is a markup defect.** Gate 41 still
counts that file because `.bottom-nav a{...color:inherit}` ends at an anchor inside the bar. Going
to look found that a slot is `<a><button>` on 73 screens and a bare `<button>` on 32 - interactive
content inside a link, twice in the tab order, and a third of the screens where the same slot
navigates nowhere. `ui-kit/docs/defects.md` row 78. A partition may not change what an element IS,
so it is written down and the count stays honest.

---

## `button` read out, and nothing in it adopts at zero: the distance holds at 11

The third migration was measured before it was written, and the measurement stopped it. Seven
kinds, 911 placements, six files. 710 are already `.btn`. Here is what the other 201 measure,
in the browser at 1440, dark, against `.btn` itself:

| kind, and where | ground | border | corner | ink | font | padding |
|---|---|---|---|---|---|---|
| `.btn` md primary, the reference | brass gradient | 1px transparent | 10 | on-brass 700 | 14 | 12 / 12 |
| `.cc-btn` **3**, cookie-consent | `--bg-control` | 1px hairline | 10 | primary 600 | **13** | 12 / 12 |
| `.cmt-post` **11**, comments | brass gradient | **0px** | 10 | on-brass 700 | 12 | 8 / 12 |
| `.edit` **1**, profile | `--bg-control` | 1px hairline | **pill** | primary 600 | **11** | 8 / 16 |
| `.load-more` **9**, loadmore | **`--bg-chip`** | 1px **`--bevel-notice`** | 10 | primary 600 | 14 | 12 / **24** |
| `.hiw-btn` **105**, header | **transparent** | 1px hairline | **pill** | **muted 400** | 12 | 4 / 8 |
| `.cmt-actions button` **72**, comments | **transparent** | **0px** | **0** | **muted 400** | 11 | 4 / 4 |

**The map's sentence about this atom was wrong and it is corrected.** It said *emphasis, size
and block are modifiers of it; nothing else in it is.* The last two rows are 177 placements
wearing an emphasis the family does not have: a transparent ground. That is a THIRD emphasis,
and `.hiw-btn` is a fourth thing again, because its transparent pill with a `--color-action` 14
per cent hover is the icon button's skin with a word inside it - the same declaration, written
in two files.

**And every one of the seven differs by a VALUE, not by a modifier.** That is the difference
between this family and the two migrated before it, and it is worth stating plainly:

    iconbutton   5 kinds   4 adopted at zero, 2 refused for a day, then answered
    navitem      2 kinds   both adopted at zero
    button       6 kinds   ZERO adopt at zero

`.cc-btn` is 13px against a ramp of 12 / 14 / 14. `.cmt-post` is `.btn.btn-primary.btn-sm`
except that it has no border at all, so the family's transparent 1px band would grow it **2px
in each dimension**. `.edit` is quiet emphasis at 11px in a pill. None of those is a rule in the
wrong file; each is a number somebody chose, or failed to choose, and a partition may not pick
one. `ui-kit/docs/backlog.md` S47 asks them the way S44 asked its three, and S44 took one
afternoon once it had answers.

**So the distance does not move this pass, and that is the honest outcome.** The alternative was
to adopt anyway and call 201 placements "no visible change", which is exactly the sentence
defect 77 was written about.

---

## `button` answered, and the family turned out to have four emphases: 11 to 10

S47's five questions were answered and applied the same day, which is the loop S44 established:
measure, refuse to choose, ask, apply. What the answers bought:

| kind | became | and it cost |
|---|---|---|
| `.hiw-btn` **105** | `.btn.btn-ghost.btn-xs` | **nothing at all** |
| `.cmt-actions button` **72** | `.btn.btn-bare` | **nothing at all** |
| `.cmt-post` **7** | `.btn.btn-primary.btn-sm` | 2px in each dimension, the family's band |
| `.cc-btn` **3** | `.btn.btn-secondary.btn-md` | the font, 13 to 14 |
| `.edit` **1** | `.btn.btn-secondary.btn-sm` | four values on one element |

**The two biggest moved no pixel, and that is the whole argument for naming a thing rather than
squeezing it.** `.hiw-btn` fitted nowhere on a two-emphasis, three-size family, so the family
grew a third emphasis and a fourth ramp step **at the values the product already drew**. A ramp
read off the product has to be re-read when the product's set of controls changes, and this one
had been read before `.hiw-btn` was in the family at all.

    ghost   keeps the box, gives up the fill: transparent on a hairline pill, quiet ink
    bare    gives up the box too: no ground, no edge, no corner, its padding a hit area
    xs      4 / 8 at 12px, the header band's own rhythm, 105 placements

**`bare` is the same rest face a `navitem` wears and it is not one.** What separates them is the
MEANING, which is exactly the check rule 1 was reduced to when the social mark moved. Reply does
a thing; it does not go anywhere. The rule earns its keep for the first time.

**525 snapshots, 431 differ, 2137 elements, and every property is named.** No `color`, no
`backgroundColor`, no `backgroundImage` moved anywhere in the product. The only boxes that moved
are the 55 readings of the three controls above plus the reflow around them. Everything else is
`display` block to flex, `gap` normal to 12 on single-child flex boxes, `justify-content` normal
to center, `border-style` none to solid under a 0px width, and `font-family` narrowing from
`"DM Sans", system-ui, sans-serif` to the `--font-body` role's `"DM Sans", sans-serif` - which
decides only which fallback would be used if a font served from this repo failed to load.

    41 the atom map   7 control atom(s) in 17 file-slot(s): distance 10, and it goes to 0
                      iconbutton  1361  6 kind(s), 1 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      navitem     1019  3 kind(s), 2 file(s)
                      button       911  7 kind(s), 5 file(s)   <- was 6, and the header is out
                      outcome      272  3 kind(s), 3 file(s)

**Five files still draw a button and each is a different kind of leftover**, which is worth
listing because the number alone reads as failure:

- `button` - its home.
- `comments` - `.cmt-signin`, a `--bg-well` ground with muted ink, which is not an emphasis this
  family has. The specimen corpus stages it nowhere, so it is also the reason `.cmt-post` was
  KEPT as a name after adoption: deleting it was tried and reverted within the hour.
- `loadmore` - S41 says that component should not exist and the chip family is blocked on S35.
- `cookie-consent` - one declaration, `min-width:96px`, so three answers divide a banner.
- `profile` - one declaration, `min-height:44` under a coarse pointer, which is S39's question
  and not a partition's.

The last two are the same shape and worth naming: **a floor is a size, and a size is the
control's, but the family has no coarse-pointer floor at all.** Giving it one would move 911
placements on touch, which is S39.

**And the migration made a new finding by splitting a selector.** Four controls in the header
band wear one skin - the icon button, the two `<summary>` disclosures and this pill - and after
two migrations that one declaration is written in three files, byte for byte, each copy
deliberate and each documented. The map has no word for a SKIN shared across atoms, and the two
disclosures are the test, because no atom can hold their half. `ui-kit/docs/backlog.md` S48.

---

## `outcome` had three kinds and has two: 10 to 9

The hero band was drawing its own copy of the product's most semantically loaded control, and
`components/hero.css` said so in its own comment: *every selector in yesno.css hangs off
`.yesno`, so not one of them reaches this button.* True, and the wrong conclusion. **The answer
to a control being out of a family's reach is to put it in reach, not to draw it again.**

Measured at 1440, dark, before anything moved:

| | ground | edge | ink | corner | weight |
|---|---|---|---|---|---|
| `.yesno button`, the card's pair, **230** | `rgba(79,169,107,.12)` | `rgb(63,125,85)` | `rgb(119,209,155)` | 10 | 700 |
| `.hf-btn`, the hero's pair, **2** | `rgba(79,169,107,.12)` | `rgb(63,125,85)` | `rgb(119,209,155)` | 10 | 700 |

Identical in every value a face has, and **the markup was identical too**: a flex row, a link
per side, a button inside it. So the container took the class it should always have carried and
the two buttons dropped theirs. `components/hero.css` went from thirteen declarations about that
pair to one about where the row sits.

**Two placements took the family's size on the way**, which is the `.edit` argument one step up:
14px to 12, a 40 floor to 44, the browser's 1/6 padding to a chosen 8, and the hover from
`--outcome-yes-fill-strong` to the 32 per cent mix over `--bg-control` that the other 230 answer
with. Two against 230. **The press needed no argument at all** - both files had already written
`color-mix(outcome 32%, --bg-pressed)`, byte for byte, which is the clearest sign the two were
one control all along.

**525 snapshots, 5 differ, and all five are `event-feed.html` at its five widths.** 74 heights
changed and 1,995 elements moved down the page; **zero widths changed and nothing moved
sideways.** No colour, no ground and no border moved anywhere in the product. The hero pair is
4px taller and everything under it on that one screen sits 4px lower.

    41 the atom map   7 control atom(s) in 16 file-slot(s): distance 9, and it goes to 0
                      iconbutton  1361  6 kind(s), 1 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      navitem     1019  3 kind(s), 2 file(s)
                      button       911  7 kind(s), 5 file(s)
                      outcome      272  2 kind(s), 2 file(s)   <- was 3 kinds in 3

**What is left of this atom is one control, and reading the files corrected the question the
same day it was asked.** `.bp-side`, 40 placements, rests NEUTRAL - `--bg-control` on a hairline
with muted ink - where the card and the hero state both sides before anybody presses anything,
and the first version of this paragraph called that a divergence. **It is a decision, written
twice.** `components/tokens.css` declares `--outcome-yes-fill` with the words *"the tinted YES
button (spectator, not trader)"*, and `components/betpanel.css` argues it out: *pressing it in
green would be inventing a colour the control does not have and telling the user the side is
chosen before it is.* A spectator's pair states the market's two sides; a trader's chooser
states the CHOICE. So `.bp-side` is a second FACE of this atom, and the measurement that found
it was not enough on its own.

**That is the mistake this document has now made in both directions.** The social mark was filed
by an argument nobody had measured; `.bp-side` was nearly refiled by a measurement whose reasons
nobody had read. The rule that survives both: **measure, then read what the files say about the
measurement, and only then decide.**

**One value is genuinely open.** The selected side is solid `--outcome-yes` under `--text-on-yes`
in the panel and the option list at 4.64:1, and `--outcome-yes-fill-strong` under
`--outcome-yes-text-lit` in the dock at 5.3:1. Both are measured, both clear the floor, and no
file says why the same control should differ at two widths when the dock IS the panel below
760px. `ui-kit/docs/backlog.md` S49 holds that one line, and `.bp-side` waits for it rather than
carrying the disagreement into the atom's own file.

---

## Two corrections and one adoption at zero, and the distance holds at 9

**The outcome question was corrected the same day it was asked, by reading instead of measuring
again.** The record above called `.bp-side`'s neutral rest a divergence. It is a decision,
written twice: `components/tokens.css` declares `--outcome-yes-fill` with the words *"the tinted
YES button (spectator, not trader)"*, and `components/betpanel.css` argues it out. A spectator's
pair states the market's two sides; a trader's chooser states the CHOICE. `.bp-side` is a second
FACE of the outcome atom, not a control that drifted, and the third rest spelling is not one
either - `--outcome-yes-fill-soft` and `--outcome-yes-fill` are both `var(--green-a12)`, two
names for one value, which `tokens.css` says itself with the words "for now".

**So this document has now made the same mistake in both directions**, and that is the finding
worth keeping:

    the social mark   filed by an argument nobody had measured
    .bp-side          nearly refiled by a measurement whose reasons nobody had read

**Measure, then read what the files say about the measurement, and only then decide.** One value
in that family is genuinely open and S49 now holds one line rather than three.

**The notification row adopted `navitem` at zero**, which closes half of S46. Its two blockers
were a `font-size` that nothing in the row reads - a `<strong>` and a `<span>`, both block, both
sized, no bare text node - and a `display` that does draw, so the first was taken and the second
got a modifier. 375 anchors in three trees. **525 snapshots, 0 differ, 0 elements changed.**

The state capture then did something better than the diff: it **merged the account row and the
notification row into one group**, because they measure identical in all four states and both
themes. Three selectors that had been one each before this migration split them are one again,
and a `_states.TIGHT` exception was paid off on the way, because the merged group is photographed
where there is room.

**The distance does not move for either**, and both are worth the pass anyway. One removed a
duplicate the census cannot see, because a `<a>` in a dropdown is not a button-shaped control;
the other stopped a wrong decision from being made on 40 placements of the control a bet is
actually placed with.

---

## S49 answered, and the outcome atom closes at one file: 9 to 8

**Solid, at both widths.** The chosen side in the mobile dock was `--outcome-yes-fill-strong`
under `--outcome-yes-text-lit`; it is now the solid `--outcome-yes` under `--text-on-yes` that
the panel and the option list already used. A person choosing a side on a phone and a person
choosing it on a desktop are choosing the same thing.

**525 snapshots, 16 differ, 32 elements, and all 32 are that decision**: 16 chosen sides and the
16 odds figures inside them taking the new ink. Nothing else in the product moved.

**The state gallery is the better proof, and it is the first time it has been one.** It groups a
face by what it MEASURES, and it carried three entries for a chosen side - the panel's, the
dock's, and a multi-outcome row's. It now carries **one**. Two groups did not disappear because
a caption was deleted; **they merged because the controls became the same control.** A gallery
that is computed can say that; a table of names cannot.

**Four semantic roles and four primitives went with the answer.** `--outcome-yes-fill-strong`,
`--outcome-no-fill-strong`, `--outcome-yes-text-lit` and `--outcome-no-text-lit` had nothing left
to paint and gate 11 said so; `--green-a20`, `--red-a20`, `--green-150` and `--red-250` went one
level down for the same reason. **A primitive exists because a role needs it**, so when the role
is retired the primitive is not kept in case.

Then `.bp-side` moved at zero, as the atom's **trader face**: `.yesno-pick` on the panel's plate
and `.yesno-pick-bar` in the sticky bar. Two faces and not one, because they stand on two
surfaces and never coexist - which is the same answer this map has now given six times.

    41 the atom map   7 control atom(s) in 15 file-slot(s): distance 8, and it goes to 0
                      iconbutton  1361  6 kind(s), 1 file(s)
                      chip        1358  3 kind(s), 4 file(s)
                      navitem     1019  3 kind(s), 2 file(s)
                      button       911  7 kind(s), 5 file(s)
                      outcome      272  2 kind(s), 1 file(s)   <- closed

**The proof caught one real regression on the way**, and it is defect 76's family again. The
markup helper matched `<button>`, and the panel renders its two sides as `<span class="bp-side">`
in the loading, processing and resolved states - the side as a STATEMENT rather than a control.
Twelve of them lost their box the moment the paint left `betpanel.css`: 140x50 to 140x24, no
ground, no edge. The before-and-after named them in one line. **A control is not always a
`<button>`, and the third helper this migration has needed is the one that reads the element the
rule ends at rather than the tag it usually wears.**

---

## S35: five spellings of "selected", and the loudest had never rendered

The chip family's selected state was the largest open value on the map: 1,358 placements in four
files, and `ui-kit/docs/backlog.md` counted five ways of saying *this one is chosen*. Measured in
the browser at 1440 in both themes, and then read for reasons, which is the order this document
settled on one pass earlier:

| what it says | placements | ground | edge | ink | halo |
|---|---|---|---|---|---|
| the category chips | **815** | `--tint-brass-09` | `--tint-brass-45` | `--text-brass-chip` | yes |
| the rail chip, the panel's amounts, the deposit sheet's | **543** | `--tint-brass-16` | `--tint-brass-45` or none | `--text-brass` | no |
| a full brass **gradient** | 0 | | | | |

**The loudest of the five had never rendered.** `.cat-nav li[aria-current] button` set a brass
gradient at (0,2,2), and every `.cat-nav` in the product AND in the vitrine sits inside
`.feed-inner`, whose rule is (0,4,2). The current chip measures `background-image: none`. A
`border-width:2px` beside it was dead the same way. **A spelling that cannot win is not a
divergence, it is dead code**, and the only way to tell the two apart is to open the page.

**Neither of the two live spellings had a reason written for it.** `tokens.css` gives each token a
provenance and not an argument - *the condensed category chip when active*, *a selected quick
amount* - which is what a value read off an already-painted screen looks like. That is exactly
the test `.bp-side` passed a pass earlier, where `--outcome-yes-fill` said **spectator, not
trader** and settled it. Here nothing said anything, so the majority won.

**One selected chip: `--tint-brass-09`, `--text-brass-chip`, bold, the halo, and a
`--tint-brass-45` edge WHERE THE CHIP HAS ONE.** It is also the safer pair in daylight, where the
two inks collapse to a single `--brass-700` and the losing ground is the deeper of the two. And
the recipe **colours what a chip already has rather than adding a part**: the rail chip is
borderless at rest and stays borderless when chosen, so no box moves.

**525 snapshots, 55 differ, 121 elements, and exactly three properties**: `color`,
`backgroundColor`, `boxShadow`. No box, no border width, no padding, no font, nothing outside a
chosen chip.

**A sixth spelling was found by the proof rather than by the reading.** `dialog.app-dialog .quick
button.sel` is a rule the first sweep missed because the selector starts with a tag, and the state
gallery split the deposit sheet's chip away from the bet sheet's the moment the other half of the
edit landed. It merged again when the sixth was fixed. **That is twice now that the gallery has
checked a caption a person wrote**, and the reason it can is that it groups a face by what the
face MEASURES.

The distance does not move: this was a value, not a partition. **The chip partition - four files
to one - is the next pass, and it is now a move at zero.**

---

## The chip partition, two files of three: 8 to 7

With S35 answered the chip family could finally move, and two of its three region files gave up
their chips. `components/chip.css` held ONE face and the atom has four; it now holds three of
them and the one rule they all have to agree on.

    rail     transparent, no edge, a 10 corner - a segmented control on a plate
    quiet    transparent on a TRANSPARENT 1px band, a pill - a scrolling strip in
             the header, where a ground would make a row of eight read as eight buttons
    amount   --bg-control on a hairline, a 10 corner - a form control in a sheet
    nav      --bg-chip on --bevel-notice - still in components/catnav.css, next pass

**Selected is one declaration now, for every face and for both ways the product says it.** A rail
chip and an amount carry `.sel`; a category chip sits inside `li[aria-current="page"]`, which is
the correct thing for navigation and is not going to be replaced by a class. Two selectors, one
rule, where there were four rules and six spellings a week ago.

**525 snapshots, 39 differ, 156 elements, and ONE property: `font-family`** - the `--font-body`
role narrowing a fallback chain from `"DM Sans", system-ui, sans-serif` to `"DM Sans", sans-serif`,
which decides only what would happen if a font served from this repo failed to load.

**The first cut of it was wrong and the proof said so in one line.** `.chip` was both the atom
and the rail face, so the moment every chip in the product carried `.chip`, the rail's border-0,
its transparent ground, its 4/12 padding and its semibold all landed on 480 amounts and 525
condensed chips: **722 elements, and the quick row changed height on 39 screens.** The fix is the
one this map keeps arriving at - **a base class is the atom or it is a face, never both** - so the
rail became `.chip-rail` and `.chip` kept two declarations that every chip shares.

    41 the atom map   7 control atom(s) in 14 file-slot(s): distance 7, and it goes to 0
                      chip        1358  3 kind(s), 3 file(s)   <- was 4
                      navitem     1019  3 kind(s), 2 file(s)
                      button       911  7 kind(s), 5 file(s)
                      iconbutton  1361  6 kind(s), 1 file(s)
                      outcome      272  2 kind(s), 1 file(s)

**`components/quick.css` is now a row and nothing else**: a flex line that wraps, and a bet panel
pushing it to the right. That is the shape S41 describes about `loadmore`, and this file has
joined it - a component that is one layout rule for one row is not a component.

**And `header` did not drop out, for the reason `bottomnav` did not.** Every rule that draws a
chip has left it; what still counts is `.cat-condensed a{text-decoration:none}`, the link wrapper
around each chip. It is `<a><button>` again - `ui-kit/docs/defects.md` row 78, now on a second
control - and the metric is right to count it until somebody decides what that element is.

**One thing was decided rather than carried and no snapshot can see it.** The deposit sheet's
amounts answered a pointer and the bet panel's, the same face on the same control, answered
nothing. The face took the hover. It lives entirely inside `:hover`, so the state gallery is the
only instrument in this repo that can check it.

## S46 answered, catnav gives up its last three controls, and the chip closes on defect 78: 7 to 6

`components/catnav.css` drew three controls and every one of them is a `chip`. They are gone, the
file is declared STATIC, and what is left of the distance on the two biggest atoms is **one defect
with one name**.

**The three, measured at 1440 and 380 in both themes before anything moved:**

    .cat-nav button       285 on 57 screens   --bg-chip on --bevel-notice, 10 corner, 14px 600,
                                              12/20, identical at both widths
    .feed-subfilter       5 on 1 screen       transparent on a transparent 1px band, 100px pill,
                                              13px 600, --text-muted, 4/12
    .subcat button        234 on 24 screens   380: 114x41 hairline PILL, 100px corner
                                              1440: 206x41 full-width ROW, 10px corner,
                                              transparent edge, space-between

**The sub-filter was not a face, it was four pixels.** Read against the 525 `quiet` chips in the
header it agrees on the ground, the transparent band, the corner, the size, the weight, the ink and
the side padding, to the same width in three decimals. It differs by **4px of vertical padding**
and nothing else. Five elements on one screen against 525 is an exception with no argument, so it
adopted: **30px tall to 38, and its chosen chip 600 to 700**, which is the family's recipe.

**The sub-category row is the finding, and S46 had it right that one width is not a measurement.**
It was filed under `navitem` on the strength of the desktop reading alone. A nav item is
transparent with **no edge and no corner**; this control carries a 1px band and a corner at BOTH
widths, so it was never that atom. It is a chip, and it is **the first control in this system whose
SURFACE changes with the window**: a horizontal scroller on a phone, a sticky 214px column above
900. Every face on this map so far has been an answer to a surface and each has had one surface.
This one has two, so **the face carries the media query** and `catnav.css` keeps only the rail.

**And it was the last of S35's five spellings of "selected".** It said chosen with 18 per cent of
`--color-action` in oklab, a solid brass edge and semibold, because on the day the other four were
unified it was filed under a different atom. It wears the one recipe now, and the recipe is now
written against the ATOM rather than a face: `.chip.sel, [aria-current="page"] .chip`, two
selectors for five faces and both ways the product says chosen.

    525 snapshots, 165 differ, and every property is named
      1560  fontFamily     the lane, --font-body narrowing "DM Sans", system-ui to "DM Sans"
       160  colour, ground, four border colours, boxShadow, weight   32 chosen lanes x 5 widths
       160  fontWeight on .chip-cnt   the count following its own label, 600 to 700
        25  paddingTop + 25 paddingBottom + 5 fontWeight   the 5 sub-filter chips
    ONE box resized that was not those: a chosen lane, 94px wide to 95, because bold is wider
    than semibold. Everything else that moved is reflow under those two.

**Gate 24 refused the first cut, and it was right.** `.cat-ic` and `.cnt` were left in
`catnav.css` on the `.bn-bal` precedent - a figure inside a nav slot stayed with the bottom nav -
and the map answered within the minute: `chip contains catnav`. It is a true reading of the DOM,
and with `catnav contains chip` already true it is a **cycle**: `chip` computed L1 from its own
stand and L3 from the product. **An atom that contains a component is not an atom.** The edge
could have been declared away; it was not, because the reading was right and the NAMES were wrong.
Both parts are sized by the control, take their colour from `currentColor` and change when the
control is hovered or current, which is what a part of a FACE does. `.chip-ic` and `.chip-cnt`,
580 and 589 spellings across four trees. `.bn-bal` stays where it is and the difference is
measurable rather than a matter of taste: **nothing anywhere changes it when its slot is hovered
or current.**

**The metric had a blind spot and this pass walked into it.** `atom_gap()` recognises a control by
the classes its census row NAMES, so a row that names only ANCESTORS is visible only while the
control is reached by its tag - `.cat-nav button` - which is exactly the spelling a migration
deletes. Four rows would have gone silent the moment they adopted, and the distance would have
fallen by two for a move that closed one. The rows name their faces now, which is the fix in the
direction of more truth: a row says both what a control is and where it stands. `navitem`'s two
rows got the same treatment and its own file became visible for the first time.

    41 the atom map   7 control atom(s) in 13 file-slot(s): distance 6, and it goes to 0
                      chip        1592  4 kind(s), 2 file(s): chip, header
                      iconbutton  1361  6 kind(s), 1 file(s): iconbtn
                      button       911  7 kind(s), 5 file(s)
                      navitem      785  2 kind(s), 2 file(s): bottomnav, navitem
                      outcome      272  2 kind(s), 1 file(s): yesno

**What is left on the two nav atoms is one defect with one name.** `chip` counts `header` because
of `.cat-condensed a{text-decoration:none}`; `navitem` counts `bottomnav` because of
`.bottom-nav a{display:block;text-decoration:none;color:inherit}`. Both are the wrapper around an
`<a><button>`, both exist only to undo the anchor's own look so the control inside shows through,
and both are `ui-kit/docs/defects.md` row 78. **Two of the six remaining file-slots are the same
markup question**, and it is a question for the grey tree rather than for a stylesheet.

**The chip's stand is the whole atom now.** Ten groups where there were four, and the five chosen
faces measure the same eight values with the corner as the only difference. The gallery also shows
what the stand cannot: `catnav-subcat` is framed at 900px, so the lane is photographed as a
desktop row and its phone pill has no picture. A specimen has one width; the two readings are
above.

## Defect 78, the navigation half: six of seven atoms reach one file, 6 to 4

The two file-slots left on the two biggest atoms were the same four words -
`<a href><button>...</button></a>` - and unwrapping them closed both.

**The defect's own framing was half wrong, and reading the markup is what showed
it.** The row said a nav slot is a `<button>` inside an `<a>` on 73 screens and a
bare `<button>` on 32, as though 32 screens were inconsistent. They are not: the
bare one carries `data-open="signin"` and opens a dialog. **A slot that navigates
is a link and a slot that opens a sheet is a button, and the product had that
right.** What it had wrong was a second control inside the first, going nowhere,
in the tab order, announced by a screen reader as a link containing a button.

    bottom-nav slot        324 painted, 255 grey    ->  <a class="nav-item nav-slot">
    header condensed strip 525 painted, 435 grey    ->  <a class="chip chip-quiet">
    category band          285 painted, 285 grey    ->  <a class="chip chip-nav">
                         1,134 painted, 975 grey, both trees in one change

**Three rules existed only to undo the wrapper's own look so the control inside
could show through**, and that is a control's rule written about the wrong
subject. `.nav-item` already had all three; `.chip` gained `text-decoration:
none`. A FOURTH was found by measuring rather than by reading: **`text-align:
center` is the `<button>` element's own default**, so the atom had worn it for
its whole life without anyone writing it down, and the first before-and-after
reported exactly one property changed on exactly the 810 controls that became
anchors. Nothing moved - an inline-flex box sized by its content has nothing to
distribute - and it is written down anyway, because **a face that depends on
which ELEMENT it is written on is not a face.**

    525 snapshots, aligned rather than indexed, because 1,134 elements were
    deleted and an index comparison has nothing to say about that

      5,670  wrapper anchors removed   (1,134 x 5 widths)
          0  elements added
          0  boxes resized
          0  boxes moved
          0  computed properties changed

**The census was reading a tag where it should read a control, and the fix
dissolved a mechanism rather than adding one.** `Census` counted `<button>`, so
1,134 named controls would have vanished in one commit and gate 38 would have
reported them as gone rather than as changed. It reads an `<a>` as a control when
it CARRIES one - when it wears a class a kind names - and that is the same test
the rest of the file uses. `ANCHOR_KINDS` existed for exactly this reason, one
row, the footer's five social marks matched by a regex over a container that had
to close with `</div>`. It is gone: `social` is an ordinary row now. The census
also stopped under-counting the notification rows, which were anchors all along:
the account-menu kind went 365 to 575.

    41 the atom map   7 control atom(s) in 11 file-slot(s): distance 4, and it goes to 0
                      chip        1592  4 kind(s), 1 file(s): chip
                      iconbutton  1361  6 kind(s), 1 file(s): iconbtn
                      navitem      995  2 kind(s), 1 file(s): navitem
                      button       911  7 kind(s), 5 file(s): button, comments,
                                                    cookie-consent, loadmore, profile
                      outcome      272  2 kind(s), 1 file(s): yesno

**Six of the seven atoms are drawn in one file. The whole remaining distance is
`button`**, and S41 already says what two of its four extra files are: `loadmore`
should not be a component and `cookie-consent` and `profile` count only because
of a 44px floor and a min-width that belong to the family's own ramp.

**What was deliberately left, and it is still defect 78.** The YES / NO pair on a
card (212), the sheet close inside `<a href="#">` (17) and the `.btn` family
inside an anchor (73). None of those is navigation by construction: YES on a card
MEANS place a bet and merely routes to the detail page in a prototype, so turning
it into a link would bake the prototype's routing into the structure. Each needs
a product answer, and a migration is not allowed to supply one.

## The 44 floor and the chip drawn twice: 4 to 1, and six atoms are done

Two of the four slots left were one missing declaration, and the third was a
component backlog S41 said should not exist on the day it was opened.

**THE FLOOR THE LARGEST FAMILY DID NOT HAVE.** `components/tabs.css` has stated
the rule since step 7 - target size follows the POINTER and not the viewport, 44
under a coarse one and 36 under a fine one - and six files carried it while
`components/button.css` did not. So two regions carried a copy for one control
each, and both copies were the last thing gate 41 read as drawing a button in
those files. Measured first, on 105 painted screens in a real touch context at
390px with `matchMedia('(pointer: coarse)')` asserted true before every read:

    before                                    after
    btn-primary/secondary sm   137 at 36      0 under 44
    btn-bare                    72 at 25      0 under 44 in HEIGHT
    md 47, lg 55                             unchanged
                               209 boxes, and that is the whole effect

`components/profile.css` gave its copy up. `components/cookie-consent.css` was
never carrying the floor at all: what it keeps is `.cc-btn{flex:1 1 auto;
min-width:96px}`, three answers dividing a banner row, and it counted only
because the metric read a WIDTH as a face. **A width is what a container decides,
the same as a flex basis; a height is not, because under a coarse pointer a
height is a target size.** That asymmetry is the point and it is why `min-height`
is deliberately absent from the placement list.

**THE CHIP THAT WAS DRAWN TWICE.** S41 said on the day it was opened that
`.load-more` measures as `.cat-nav button`, and named the four declarations in
the way. Three of them were nothing:

    min-height:44px       INERT. 12/24 at 14px is a 47px content box, so the
                          floor never bound, at any width, in either theme
    letter-spacing:.01em  the BUTTON family's tracking, worn because the control
                          was filed as a button. 0.14px on a 14px label
    padding 12/24         against the chip's 12/20, four pixels a side
    box-shadow inset      a lit top edge, and the only real one. The chip family
                          decided against a groove on purpose so that nothing is
                          lifted to flatten under a finger

Its STATES needed no decision at all, which is the strongest evidence the two
were one control: the hover was `--border-brass-hover` on `--bg-control-hover`
with `--text-strong`, in that order, in two files, and both pressed to
`--bg-pressed`. Byte for byte, the way `.seg` and `.ed-range` were.

    45 readings of the control, 9 screens x 5 widths
      173x47 -> 162x47   eleven pixels of width, and the height did not move,
                         which is the inert floor proving itself
      the groove, the tracking and 4px of side padding, and nothing else
    everything else on 525 snapshots: 0 resized, 0 moved, 0 properties

**AND THE STATE GALLERY MERGED THEM WITHOUT BEING ASKED.** The capture that used
to be `a.chip.chip-nav @catnav-chips (2)` is now one group spanning three
specimens - the button census, the load-more stand and the category strip -
because the two measure identical in all four states in both themes. That is the
third time this instrument has checked a person's caption, and it is the only
kind of proof a merge can have.

**THE ROLE DID NOT MOVE AND THE ATOM DID.** Load more FETCHES, so
`ui-kit/_worn.py` goes on calling it an `action`; its rules live in
`components/chip.css`. That is the social mark's split in the other direction -
`nav` by role, `iconbutton` by atom - and it is now the second instance, which
makes it a rule rather than an exception: **a role is what a control MEANS and an
atom is where its RULES live.**

    41 the atom map   7 control atom(s) in 8 file-slot(s): distance 1, and it goes to 0
                      chip        1601  5 kind(s), 1 file(s): chip
                      iconbutton  1361  6 kind(s), 1 file(s): iconbtn
                      navitem      995  2 kind(s), 1 file(s): navitem
                      button       902  6 kind(s), 2 file(s): button, comments
                      outcome      272  2 kind(s), 1 file(s): yesno
                      tab           36  1 kind(s), 1 file(s): tabs
                      switch         3  1 kind(s), 1 file(s): toggle

**SIX OF SEVEN ATOMS ARE DONE. THE WHOLE REMAINING DISTANCE IS ONE CONTROL**:
`.cmt-signin`, 4 placements on two screens, a full-width well on `--bg-well` with
muted centred text that says Sign in to comment. S47 looked at it and kept it,
and the reason still holds: **that ground and that ink are not an emphasis this
family has**, and the specimen corpus stages it nowhere. It is the last file-slot
and it is a question rather than a migration - whether a signed-out PROMPT is a
button at all, or a `notice` a person can press. Nothing else is in the way.

## The last file-slot: the distance is 0

`.cmt-signin` is `.btn.btn-prompt.btn-lg.btn-block`, and **every control atom in
this product is now drawn in exactly one file.**

    41 the atom map   7 control atom(s) in 7 file-slot(s): distance 0
                      chip        1601  5 kind(s), 1 file(s): chip
                      iconbutton  1361  6 kind(s), 1 file(s): iconbtn
                      navitem      995  2 kind(s), 1 file(s): navitem
                      button       902  6 kind(s), 1 file(s): button
                      outcome      272  2 kind(s), 1 file(s): yesno
                      tab           36  1 kind(s), 1 file(s): tabs
                      switch         3  1 kind(s), 1 file(s): toggle

**S47 was right about the reading and wrong about the conclusion.** It measured
this control in the button migration and kept it out with a sentence that still
holds - that ground and that ink are not an emphasis this family has - and then
left it in `components/comments.css`, which made the composer's own file the only
place the shape was written down. **The reading was the argument for naming it,
not for leaving it.**

**IT IS AN EMPHASIS AND NOT AN EXCEPTION, and the count says so.** The map forbids
naming a face for a SINGLE element, which is what it says about the logo. This is
four placements on two screens, and **two of them are on the same screen saying
different things**: "Sign in to join the discussion" over a comment thread, "Sign
in to place and track your bet" over a bets table. That is a kind.

**WHAT MAKES IT ITS OWN STEP RATHER THAN A QUIET SECONDARY.** Every other
emphasis in this family is an ACTION somebody has decided to take. This one is an
INVITATION to somebody who has decided nothing yet, and it stands exactly where
the thing they came for should have been. So it is the only one drawn on a WELL,
a recessed ground rather than a raised one, and the only one whose label is muted
at rest. It lights all three under a pointer - edge, ink and ground - which no
other emphasis does, because a control that starts quiet needs more than one step
to answer at all.

    20 readings of the control
      54 tall to 55, and 73 to 76 where the label wraps to two lines: the ramp's
      `lg` step taking the font 13 to 14, which is the single value this
      adoption changes and the same one `.cc-btn` cost a day earlier
    everything else on 525 snapshots: 0 properties, and 110 boxes of reflow
    under those two comment panels on 10 screens

**THE DIFF CAUGHT A BUG IN THE FIRST DRAFT, IN ONE LINE.** `.btn` sets no weight,
`secondary` sets 600 and `primary` 700, so a fifth emphasis that said nothing
inherited the body's 400: twenty readings went 600 to 400 and the before-and-after
named the property. **An emphasis in this family is a ground, an edge, an ink AND
a weight, and three of four is a bug.** No sweep of the source would have found
it, because nothing was missing from anything - the value simply was not there.

**AND `comments` WENT QUIET.** Its three controls all left for
`components/button.css` - Post on 2026-08-06, Reply and Like the same day as
`.btn-bare`, the prompt a day later - and each took its hover and its press with
it. The file is declared STATIC now: a thread is read, not pressed. The last
thing gate 41 read in it was `.cmt-signin{text-align:center}`, the unscoped grey
layer, which had never reached the wireframes either, because the nine grey
screens that carry the class link nothing from `components/` at all.

---

## A surface owns a skin, and a skin is a token: S48 and S45, 2026-08-07

Neither of these moves the distance, which is already 0. Both are the same
question the migration kept meeting from the other side. If a face is an answer
to the SURFACE a control stands on - and it was, six times, on every atom that
closed - **then what happens when the surface has an answer for controls that
are not the same atom?**

### S48: four controls, one skin, three files

    at 1440 and 380, dark and light, rest / hover / press

    .icon-btn            36x36   transparent, 1px --border-hairline, --radius-pill
    .notif-menu summary  40x36   the same three
    .avatar-menu summary 56x36   the same three
    .btn.btn-ghost       88x28   the same three

    hover, all four      the wash + a --color-action edge
    press, all four      --bg-pressed

**Counting is what turned this from a resemblance into a fact.** All 242 plain
`.icon-btn` in the painted tree stand in `<header>`, 105 in `.left` and 137 in
`.utility`; every icon button anywhere else carries a face modifier. All 105
`.btn-ghost` are the How-it-works pill, also in `<header>`; there is no ghost
anywhere else in the product. **The skin exists in one band and nowhere else.**

The one thing that parts the four is the rest INK. Three of them are a mark and
sit at `--text-primary`; the fourth is a word and sits at `--text-muted`, rising
to primary under the pointer, because a label at full ink beside the wordmark
competes with it and a mark at muted disappears.

**A SKIN IS A SET OF TOKENS, NOT A FILE AND NOT A CLASS, and gate 41 is what
decides it.** A fourth file drawing `.icon-btn`, `summary` and `.btn` is three
more file-slots on two atoms - the exact thing the last seven days took from 18
to 0. A shared class is that file with a name on it: a face's rules live in its
atom's file, and the day `.band-quiet` were named in a census row the metric
would start counting it in three places, correctly. **The two `<summary>`
disclosures are the proof it had to be a token.** A summary is neither `button`
nor `iconbutton`, so no atom could ever have held their half of the skin, and
any answer that only works for two of the four is not an answer.

So each of the three files keeps its own rule, saying that its control stands on
the band, and the band says once what it does to whatever stands on it.

### Naming the value is what let the ladder see it

The wash was `color-mix(in oklab,var(--color-action) 14%,transparent)`, typed out
in all three files. `ui-kit/_rescale.py` has mapped `--brass-a14` to
`--brass-a16` since the brass scale was declared, because **14 is not a rung**;
the ladder is 06, 09, 16, 30, 45, 60 and its own note says a step of .05 is below
what a screen shows. The map matches token NAMES. **A value spelled as a colour
function is invisible to the tool that exists to keep values on the ladder**, and
these three had been invisible for as long as they existed.

The rewrite came back within the minute of the token being named, unasked:

    --tint-brass-14  ->  --tint-brass-16   x4
    --brass-a14      ->  --brass-a16       x1

**So the hover moved a rung, and the light theme is where that matters.**
`--tint-brass-16` is `--brass-a16` on graphite and `--brass-a30` on chalk,
because every tint steps up one rung in daylight. Measured against its own band:

    dark    52,49,41 -> 55,52,43      1.27:1 -> 1.33:1
    light   241,234,217 -> 233,221,191  1.11:1 -> 1.25:1

A flat alpha does not read the same on two stones, which is the whole reason the
ladder shifts, and this wash had been flat in both. **The two themes answer a
pointer with the same strength now, for the first time.** The dark band moves
three units of sRGB to get there, under the ladder's own declared resolution; the
light band moves visibly, and that is the correction rather than the cost.

    16 readings changed, all of them backgroundColor, all of them :hover, on the
    four band controls and nothing else
    525 snapshots: 0 differ, 0 elements changed - the whole change lives inside
    a state no before-and-after in this repo can photograph

**Nine more longhand brass tints are still out there** at rungs 10, 14, 20, 34
and 55, in eight files, each invisible to the rescale map for the same reason.
One of them is this exact 14 per cent, on `.chip-cnt` under a current lane. They
are `ui-kit/docs/backlog.md` S50 and not a side effect of closing S48.

### S45: not one hover per atom, and not one per surface

`.icon-btn-tile` (27) and `.icon-btn-lift` (525) rest as the same picture and
part on the pointer. The tile firms its edge and brightens its ink; the lift
tints its ground with 20 per cent of the action role, takes a brass edge and
rises two pixels. 27 against 525, so the quiet one looks like the exception that
should give way.

**It is not, and the reason is a collision nobody had priced.** Raised the way a
person raises it - by clicking the bookmark on `ui-visual/event-detail.html`,
which carries the script that flips `aria-pressed` - a SAVED tile reads
`rgb(215, 172, 83)` for its mark. The lift's hover reads `rgb(215, 172, 83)` for
its mark. **The same value.** Give the tile the loud hover and pointing at an
unsaved bookmark paints it the exact ink that means saved, on the one control in
the product where those two answers sit a pixel apart.

**So the rule is neither "one hover per atom" nor "one hover per surface".** A
face answers the pointer with the accent unless the accent is already carrying a
state of its own, and then it answers with what is left: an edge and an ink. Two
of this atom's six faces spend brass on a state. The social row spends none, so
it may.

### The second finding, which nobody asked for

    saved rest    rgba(199,162,78,.09) / rgba(199,162,78,.45) / rgb(215,172,83)
    saved hover   rgba(199,162,78,.09) / rgba(199,162,78,.45) / rgb(215,172,83)

Byte for byte, in both themes. `.icon-btn-tile[data-fav][aria-pressed="true"]` is
(0,4,0) against the hover's (0,3,0), so it wins the pointer as well as the
finger. Winning the finger is deliberate and written down - brass leaving under a
press would read as the favourite coming off before the click had said so - and
winning the pointer was never decided at all. **A saved bookmark is a control
that has stopped saying it is one.** It is the same shape as a selected chip
answering no press, so it is filed with it: `ui-kit/docs/backlog.md` S38 owns
both now rather than one file inventing half an answer.

---

## The decision this document no longer has open

- ~~**Is a social mark a `navitem` or an `iconbutton`?**~~ **Answered 2026-08-06 and the
  answer is `iconbutton`,** by measuring both instead of arguing from the role. The
  reasoning it replaces is kept here because it is the shape of the mistake: *it is an
  `<a>` with an icon and no label, so it draws like an icon button and behaves like
  navigation; the map follows the ROLE, which is rule 1, and rule 1 has never been wrong
  here.* Every clause of that is true and the conclusion is not. The section above has the
  five values that settled it.
