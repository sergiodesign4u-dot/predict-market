# chip

## Sources

- `components/comments.css` and `components/tabs.css`, where this control lived until 2026-08-05 and where it lived TWICE. `.cmt-controls .seg button` and `.ed-range button` were the same declaration block byte for byte, property order and all, plus the same hover, the same press and the same `.sel`.
- `ui-kit/_states/index.json`, which had measured both and printed the answer on two different pages without anyone putting the two readings side by side: `rgba(0, 0, 0, 0)` ground, `rgb(164, 157, 143)` edge and ink, 10px corner, and both selected states at `rgba(199, 162, 78, .16)` on `rgb(215, 172, 83)`.
- `ui-kit/_worn.py`, which filed them as two kinds of one role: **chip, a sort segment** at 27 placements and **chip, a chart range** at 36. Same role, same face, two names.
- `ui-kit/docs/backlog.md` S41, which owns the chip family and says this merge needs the shape the buttons got rather than a file move.
- `DESIGN.md`, twice: "active is a brass tint" under Chips, and the One-Accent Rule. Both decide the selected state below.

## Purpose

A label a person picks between, when the choice is small, immediate and does not leave the screen. Four time ranges under a chart, three sort orders over a comment thread. It carries a value rather than doing a thing, so what it looks like afterwards matters more than what it looks like while it is pressed.

## Anatomy

- `.chip` - the control: no edge, no ground, `--text-muted` ink, a 10px corner, 12px semibold, 4 by 12 of padding. It is quiet on purpose, because a rail of five chips with five grounds is five buttons.
- `.chip.sel` - the chosen one. A brass TINT, brass ink, bold, and the state is a class rather than a pseudo because the selection survives the pointer leaving. `.sel` is the shared modifier declared in `ui-kit/_levels.py`, so the same word means the same thing on every chip in the product.

## When to use

For a set of two to five values a person switches between on the spot, inside a container that gives them their ground: a trough, a rail, a segment. Both of today's placements are exactly that.

Not as a way of navigating. A chip that takes you somewhere is a link wearing a control's clothes, and the product already has a tab for a switch that changes a panel and a category chip for a rail that changes a page.

Not for a set that has to be scrolled. Five is a rail, twelve is a menu that has forgotten it has one.

## Rule

**A selected chip is a tint, never a fill.** A solid brass ground is the primary action's own face, and a rail of chips is not asking anybody to commit to anything. `DESIGN.md` decides it twice, under Chips and under the One-Accent Rule, and `components/quick.css` records what it cost the one time a chip took the fill: a lit brass $20 sitting directly above a lit brass Add funds.

**The container gives the ground, not the chip.** Every rule in `components/chip.css` is scoped to `.app-case`, and none of them paints a ground at rest. That is what lets one control stand in a `--bg-well` trough and on a bare section without either looking wrong, and it is why the stand shows both rails rather than the chip on the canvas.

## Anti-rule

Never draw it again in the file of whatever holds it. That is exactly how it came to exist twice: `comments.css` owned the sort segment because the segment stands in the comment controls, `tabs.css` owned the chart range because the range stands under the chart, and each file was right about its container and wrong about the control. If a third rail needs this chip, it takes `.chip`; if the third rail needs a chip that is genuinely different, the difference goes here as a modifier, next to `.sel`.

Never confuse it with the raised chip. `.load-more` and `.feed-inner .cat-nav button` are the other one: `--bg-chip` ground, a bevel edge, 14px semibold, and they are four declarations apart from each other rather than zero. That family is not merged yet and this file does not pretend it is.

Seen: `ui-kit/docs/backlog.md` S41, and `ui-kit/docs/defects.md`, which records the measurement that ended the duplicate.

## States

- `button.chip.chip-amount @dialog.app-dialog` - **The amount face, and it arrived on 2026-08-06 from `components/quick.css`.** A chip on a hairline over `--bg-control` with a 10 corner: what a chip looks like when it is one of the things you fill in on a sheet rather than a way of filtering what you are reading. The deposit sheet's copy and the bet panel's measured identical at rest and are one face. **Its hover was decided rather than carried**: the deposit sheet had one and the bet panel had none, the same face on the same control, so the face took the hover and both places answer now. That change lives entirely inside `:hover`, so no before-and-after in this repo can see it and this gallery is the only thing that can.
- `button.chip.chip-amount.sel @dialog.app-dialog` - **The chosen amount, wearing the family's one selected recipe.** Until S35 was answered the day before, this control had been through two of them in two days: a full brass gradient until 2026-08-04, then `--tint-brass-16`, and now the `--tint-brass-09` inside a `--tint-brass-45` edge that 815 category chips already wore. It answers no press, which is not this face's decision: **no selected chip anywhere in this product answers a press**, and `ui-kit/docs/backlog.md` S38 owns that uniformly rather than one file inventing an answer.
- `button.chip.chip-rail @chip-rails` - The chip at rest: no ground, no edge, muted ink. Hover brings the ink up to `--text-primary` and nothing else moves, which is the whole idea of a quiet control. **This one block is five buttons in two different rails**, three in the comment sorter's trough and two in the chart range, and the capture merged them without being asked: they measure identical in all four states in both themes. That merge is the proof the two files were drawing one control, taken by an instrument rather than by a person reading two stylesheets.
- `button.chip.chip-rail.sel @chip-rails` - **The same chip chosen**, and again one block for both rails: a brass tint, brass ink, bold. A tint and not a fill, for the reason under Rule.
