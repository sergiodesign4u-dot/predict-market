# position-list

## Sources

- `docs/backlog.md` item 16a - counted with the containment reader over the painted tree: `.pos-list`, declared in `components/position.css`, on **13** screens, which cleared the three-screen threshold and moved it into `components/patterns/`.
- **13 painted screens**: My Bets in both tabs and their states, the wallet, the notifications list and both profiles.
- `ui-kit/docs/inventory.md` L162 - "Position row (`.pos`: question, figures, status)", states "active / resolved / skeleton", and L159, the resolved-predictions history on the two profile screens.
- `ui-kit/docs/inventory.md` L141 - `.pos.skeleton`, the loading face, which stacks in this list exactly where a real row will.
- `docs/backlog.md` item 17 - `.pos-status`, this stack's own section divider, is declared in `components/profile.css`, which is why the containment reader shows this pattern holding `profile`.
- `ui-kit/docs/backlog.md` S20 - the name. This pattern carries *position* in its filename, and `voice/docs/voice.md` puts that word on the **Not allowed in the UI** list for exactly what these rows contain. The screens all say *bet*; the file does not, and the row records that as measured and deliberately unpaid.

## Purpose

A vertical stack of bet rows at one distance. Two declarations and one gap, and that is the whole pattern: what stacks, how far apart, and the fact that the distance belongs to the list rather than to the row.

## Parts

- `position` - the row, whole. Its stone, its edge, its figures and its resolved faces are all its own; this file decides only that rows stack.
- `profile` - the section divider that separates one run of rows from the next, `.pos-status` with its brass tick. It is drawn in `components/profile.css` and stands in this stack, which is item 17 in the product backlog and the reason the containment reader files `profile` inside this pattern.
- `skeleton` - the loading face that stacks in the same list at the same distance, so the page does not move when the rows arrive.

## When to use

Wherever rows of one kind stack and the distance between them is the only thing to decide: My Bets in both tabs, the wallet, the notifications list, the public track record.

What stacks is not always a bet row. The same list holds the loading skeletons and the resolved record block, and it holds them at the same gap, because a list whose spacing changes with its contents reads as two lists.

By hand: when the rows are not of one kind. A stack of mixed blocks - a notice, then a summary, then a list - is a column with its own spacing decisions, and giving it this gap would say the three are peers when they are not. Two rows is also by hand: this pattern buys nothing until the third, and `docs/backlog.md` item 16a is explicit that the threshold is three SCREENS and not three occurrences.

## Rule

The gap is the list's and never the row's: a row carrying its own bottom margin would double the distance the moment two lists sat one under the other, and the last row would push the plate's padding out by a step.

## Anti-rule

Never use it where the items reflow by width: things of one shape that should become two and three columns as the window grows are `card-grid`, which is `auto-fit` arithmetic with no media query at all. This stack is one column at every width on purpose, because a bet row is a sentence and a sentence in three columns is unreadable.

Predicted: no screen has tried it. The two have never been confused because the contents differ so plainly, and the line is recorded for the case where somebody wants the wallet's history "to use the space" on a desktop.

## Arrangement

A column flex box with one gap, at every width, in source order. Nothing sticks, nothing wraps, nothing reorders.

No states of its own: what answers a pointer is the `position` row, and that component's own file records why its gallery is empty - the hovered element is the anchor around the row and the changed element is the row, so the states pass photographed nothing. The gap this pattern owns has no face to change.
