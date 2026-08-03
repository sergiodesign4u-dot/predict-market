# card-grid

## Sources

- `docs/backlog.md` item 16a - `.grid`, declared in `components/feed.css`, counted on **23** screens by the containment reader, which cleared the threshold and moved it to `components/patterns/`.
- **23 painted screens**: the feed, the eight category pages, Favorites, and the states of each.
- `ui-kit/docs/inventory.md` L82 - "Responsive card grid", states "populated / skeleton".
- R5 in `ui-kit/docs/architecture.md` - the full outcome list never inside a card. Counted: 161 cards across the painted tree, 21 of them multi-outcome, every one with exactly two option rows, and no "+N more" string anywhere.
- R7 in `ui-kit/docs/architecture.md` - no bet control on a screen that carries this grid: 23 screens with it, 0 with a panel or a dock.
- R8 in `ui-kit/docs/architecture.md` - 0 grids on the five system screens, which is what makes the grid content rather than frame.

## Purpose

A fluid track of event cards, one column to four, with no media query at all. `auto-fit` over `minmax(min(100%, 300px), 1fr)`, so the column count is arithmetic on the available width rather than a set of breakpoints somebody has to keep in step with the card.

## Parts

- `card` - the item. Its photograph, its question, its probability and its why are all its own; this pattern decides only how many of them fit across.
- `yesno` - the pair inside a binary card, which is the control the track has to leave room for at the narrowest column.
- `options` - the two option rows inside a multi-outcome card, capped at two so a multi card stays close to a binary card's height and the meta rows line up across the track.

## When to use

When a screen lists things of one kind and the number of them is decided by the data, and the items are the same shape, so a track that reflows beats a layout authored per width.

Once per screen. Two grids on one page means two different sets of one kind, which is a question about the screen rather than about the track.

By hand: when the items are not the same shape. A row of three blocks that happen to sit side by side - a summary, a chart and a note - is a flex row with its own sizes, and putting it in this track would let a narrow window stack them in an order nobody chose. The test is whether an item could be the first, the last or the only one without looking wrong.

## Rule

One grid per screen, and the column count is arithmetic: no breakpoint in this file, so a card that changes its minimum width changes the track by itself and nothing has to be edited in two places.

## Anti-rule

Never let a bet control into it. A screen that carries this track has no amount field and no Confirm on it: a card's YES / NO belongs to `yesno` and routes to the detail with the side pre-selected, while the thing that commits money is `betpanel`, which R3 keeps to one per screen and R7 keeps off every screen with a grid.

Seen: `wireframes/_conventions.md` S3 states it as a decision that had to be written into the grey tree's contract - "a tap routes to Event Detail with the side ... pre-selected. It does NOT place a bet on the card and does not bypass Event Detail" - which is a sentence written because the alternative was on the table. R7's counter is what confirms it held: 23 screens with a grid, 0 with a panel or a dock.

## Arrangement

`auto-fit` over `minmax(min(100%, 300px), 1fr)` with one gap, at every width. The `min(100%, 300px)` is what stops a 300px minimum from overflowing a 360px phone, and it is the reason there is no media query: below one column's worth of room the track takes the full width instead of scrolling sideways.

No states of its own. Everything in the track that answers a pointer is a `card`, and the whole-card hover, the question link and the save control are photographed on that component's page.
