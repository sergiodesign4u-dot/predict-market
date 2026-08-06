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

1. **Same ROLE.** `ui-kit/_worn.py` files every control as action, selector, nav or
   stand, because a `<button>` is a tag and not a role. Two controls in different roles
   are never one atom, however alike they look.
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
| `button` | a press with a LABEL, that does a thing | the button family **710**, how it works **105**, post a comment **11**, load more **9**, cookie consent **3**, edit on the profile **1** = **839** | `.btn` already holds 710 of them, with emphasis, size and block. The other four are the same control redrawn in four files: same radius-10 or pill, same semibold label, same 44 floor |
| `iconbutton` | a press whose whole content is a MARK | header icons **388**, sheet close **333**, bookmark on a card **84**, a comment's action **72**, an event's action row **27**, toast close **4** = **908** | six files, six names, one idea: a square or a disc sized to the finger with an icon in it. It is a separate atom from `button` and not a modifier of it, because it has no label to size and its whole box is a target |
| `chip` | a label you PICK BETWEEN, that carries a value | category chip **815**, quick amount **480**, quiet chip in a rail **63** = **1358** | the largest family and the most divided. `components/chip.css` exists and holds 63. The differences are pill against radius-10, 13px against 12px, and the ground at rest, which are modifiers |
| `tab` | a selector whose selection swaps a PANEL rather than carrying a value | the tab row **36** | its own atom since 2026-08-06, and the measurement recorded below is what made it one. `.ed-tablabel` and `.ptab-lbl` are the same control again as labels, so they join it when the non-button controls are counted |
| `outcome` | the YES / NO pair, where the COLOUR states a result | YES/NO buttons **230**, the outcome side of a bet **40**, the hero's featured pair **2** = **272** | genuinely its own atom and must never fold into `chip`. `DESIGN.md` decides it: green and red are outcome semantics, brass is the brand, and an accent never borrows the win or lose colour |
| `switch` | one setting, on or off, answered on the spot | toggle **3** | already `components/toggle.css`, already correct, and it stays one because a switch is not a chip with two states: it says yes or no to one thing rather than choosing among several |
| `navitem` | a thing you tap that GOES somewhere | social marks **525**, bottom nav slot **420**, account dropdown row **365**, a sub-category row **234** = **1544** | four files. A slot with a mark over a label, a row with a label, a bare mark and a full-width row with a count are one control at four sizes. The active state is a state of the item, not a fifth control |

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

## The decision this document still does not settle

- **Is a social mark a `navitem` or an `iconbutton`?** It is an `<a>` with an icon and no
  label, so it draws like an icon button and behaves like navigation. The map follows the
  ROLE, which is rule 1, and puts all 525 in `navitem`. Rule 1 is the one that has never
  been wrong here.
