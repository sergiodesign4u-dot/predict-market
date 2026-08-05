# quick

## Sources

- `components/input.css`, where these chips lived until 2026-08-05. A field and a group of chips are not one thing: `input` is a label, a field and the row that holds them, and this is a ROW OF CHIPS a person chooses between.
- `ui-kit/_worn.py`, which had already filed them under a different ROLE from everything else in that file: a quick amount is a **selector**, and a field is not. 480 placements over 105 screens.
- `ui-kit/docs/defects.md` row 63 and `ui-kit/docs/backlog.md` S41 - the pass that split them. `input` had an EMPTY containment, so `ui-kit/_levels.py` called it an atom with nothing to go on.
- `DESIGN.md`, twice: "active is a brass tint" under Chips, and the One-Accent Rule. Both decide the selected state below.
- `ui-kit/docs/backlog.md` S38, which owns the gap this control shares with every other selected chip in the product.

## Purpose

Four amounts a person can take instead of typing one. It stands under the field it fills, in the deposit sheet and in the bet panel, and it is the fastest path through the one screen where speed matters and a typo costs money.

## Anatomy

- `.quick` - the row. A wrapping flex line, pushed right in a bet panel because the field it fills is right-aligned, and left in a dialog because the label above it is.
- `.quick button` - the chip: graphite ground, hairline edge, 10px corner, 12px label.
- `.quick button.sel` - the chosen one. A brass TINT, a brass edge and a brass label, and the state is a class rather than a pseudo because the selection survives the pointer leaving.

## When to use

Under a field a person types a number into, when a small set of amounts covers most of what they would type. Two places: the deposit sheet and the bet panel with its sheet.

Not as a way of offering every value. Four chips and a field is a shortcut; twelve chips and a field is a menu that has forgotten it has a field.

## Rule

**A selected chip is a tint, never a fill.** A solid brass gradient is the primary action's own face, and a deposit sheet had a lit brass $20 sitting directly above a lit brass Add funds until 2026-08-04: the chip was as loud as the commitment. 107 placements moved to `--tint-brass-16`, which `components/tokens.css` names, in its own words, "from: a selected quick amount".

## Anti-rule

Never dress it as a button. It is a selector: it carries a value, and the reason its selected state is visible is that the value stays chosen. A chip lifted out of its row is the half that carries no information, which is the argument `ui-kit/authored/button.md` makes in its own anti-rule.

**And this file is not the merge it looks like.** `.seg`, `.ed-range button`, `.cat-nav button` and `.load-more` are the same graphite chip drawn in four other files, and giving one of them a file of its own does not consolidate them. What it does is make the shape of the merge visible: four files, one control, and the same measurement that ended five button names is what would end these.

Seen: `ui-kit/docs/backlog.md` S41, and `ui-kit/docs/defects.md` row 63, which is the pass that found this file had been filed as part of an atom.

## States

- `button @dialog.app-dialog` - A quick-amount chip, unselected: the graphite chip, hover on the ground and press on the pressed stone.
- `button.sel @dialog.app-dialog` - **The same chip SELECTED, and it is ONE group where it was two.** Brass tint, brass edge, brass label, bold. Until 2026-08-04 the deposit sheet's copy was a solid brass GRADIENT and the bet sheet's was the tint, so the capture photographed two, and the caption that stood here described the tint on the group that was not wearing it. The gradient is gone, the two faces measure identical, and the grouping merged them without being asked. **A caption that had been quietly wrong for a stage is the sentence the merge made true.**
