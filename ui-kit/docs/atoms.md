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

Six control atoms and six that are not controls. Every placement the census counts is
covered exactly once; the numbers add to its 5281.

### Controls

| Atom | What it is | It absorbs, and the count | Today |
|---|---|---|---|
| `button` | a press with a LABEL, that does a thing | the button family **710**, post a comment **11**, load more **9**, cookie consent **3**, edit on the profile **1** = **734** | `.btn` already holds 710 of them, with emphasis, size and block. The other four are the same control redrawn in four files: same radius-10 or pill, same semibold label, same 44 floor |
| `iconbutton` | a press whose whole content is a MARK | header icons **493**, sheet close **333**, bookmark on a card **84**, a comment's action **72**, an event's action row **27**, toast close **4** = **1013** | six files, six names, one idea: a square or a disc sized to the finger with an icon in it. It is a separate atom from `button` and not a modifier of it, because it has no label to size and its whole box is a target |
| `chip` | a label you PICK BETWEEN, that carries a value | category chip **1049**, quick amount **480**, quiet chip in a rail **63**, tab **36** = **1628** | the largest family and the most divided. `components/chip.css` exists and holds 63. The differences are pill against radius-10, 13px against 12px, and the ground at rest, which are modifiers |
| `outcome` | the YES / NO pair, where the COLOUR states a result | YES/NO buttons **230**, the outcome side of a bet **40**, the hero's featured pair **2** = **272** | genuinely its own atom and must never fold into `chip`. `DESIGN.md` decides it: green and red are outcome semantics, brass is the brand, and an accent never borrows the win or lose colour |
| `switch` | one setting, on or off, answered on the spot | toggle **3** | already `components/toggle.css`, already correct, and it stays one because a switch is not a chip with two states: it says yes or no to one thing rather than choosing among several |
| `navitem` | a thing you tap that GOES somewhere | social marks **525**, bottom nav slot **420**, account dropdown row **365** = **1310** | three files. A slot with an icon over a label, a row with a label, and a bare mark are one control at three sizes. The active state is a state of the item, not a fourth control |

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

**25 kinds today, 12 atoms at the end**, and the number in between is what the work has
left. Each step is one atom:

1. **Declare the map in code.** `ui-kit/_worn.py` already names every kind; each kind
   gains the atom it belongs to. A gate then fails in both directions: a kind that names
   no atom, and an atom that no kind names. The distance becomes a number the build
   prints, the way `_levels.py` prints the atom shelf.
2. **One atom per pass**, largest first, because the largest are the ones a person sees:
   `chip` 1628, `navitem` 1310, `iconbutton` 1013, `button` 734, `outcome` 272.
3. **Each pass is proved the same way**: `snap.cjs` before and after, both trees, five
   widths, and the diff at zero. A migration that changes a pixel is a migration that
   made a decision it did not declare.
4. **The level then stops being read off containment.** With the atoms declared, the
   `RAISE` and `TRUE_ATOM` lists shrink to the handful of genuine surprises they were
   meant for.

---

## The two decisions this document does not settle

Written down rather than assumed, because both change what gets merged:

- **Is a `tab` a `chip`?** Both are selectors, both are a label with a chosen state, and
  the product draws them alike: `--bg-chip` ground, pill, semibold, brass when chosen.
  What differs is what the selection does - a chip carries a VALUE, a tab swaps a PANEL -
  and the accessible role differs with it. The map above puts the 36 tabs in `chip` on the
  strength of the drawing. The counter-argument is that a tab strip is a molecule
  (`tablist` + `tab` + `tabpanel`) and only its `tab` is the atom.
- **Is a social mark a `navitem` or an `iconbutton`?** It is an `<a>` with an icon and no
  label, so it draws like an icon button and behaves like navigation. The map follows the
  ROLE, which is rule 1, and puts all 525 in `navitem`. Rule 1 is the one that has never
  been wrong here.
