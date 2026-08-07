# market

## Sources

- `ui-kit/docs/inventory.md` L106 - "AMM market panel (`.market-box` collapsible + `.market-depth` price by bet size table)", filed L2, on event-detail, states collapsed / open. Its screen count is a dash, and the 9 painted screens that carry it are the correction.
- The 9 screens: every Event Detail variant including the four bet states, the resolved one and both logged-out ones.
- `voice/docs/microcopy.md` L11 and L29 - the *event vs market* same-thing row: the product says *event* almost everywhere and *market* in the footer and here. This component's own name is on the wrong side of an open defect.
- `wireframes/_critique.md` L77, the resolved-detail finding: the resolved body reused the live binary detail verbatim, so a panel that describes a live price stood on a screen where the price no longer moves.
- `DESIGN.md` L3, the product's own description: "a mobile-first prediction market that is not a trader's terminal".

## Purpose

The mechanics, for the person who wants them. How the price is made, what a stake of a given size would actually get, and where the money on each side sits. It is the one block in this product that talks like an exchange, and it is collapsed by default for exactly that reason.

The whole design of it is one decision repeated: a spectator must never be made to read this, and a person who wants it must never be denied it. So it is a `<details>`, closed, at the foot of the detail column, under a head that says what is inside rather than "More". Opening it is a choice a person makes once.

## Anatomy

- `.market-box` - the `<details>`. Its open state is the element's own attribute, so it survives without script and a keyboard reaches it.
- `.market-head` - the summary: the title and the chevron, and the whole row is the target.
- `.market-title` and `.market-chevron` - the label and the mark that says which way it is.
- `.market-body` - what is inside.
- `.market-stats`, `.ms-label`, `.ms-val`, `.ms-yes`, `.ms-no`, `.ms-up` - the figure grid: volume, liquidity, the two sides. `.ms-yes` and `.ms-no` are the only two places the outcome colours appear in this file, and they appear on FIGURES rather than on controls.
- `.market-depth` and `.md-table` - the price-by-bet-size table, which answers the one question a stake actually has: if I put this in, what do I get out.
- `.md-row`, `.md-row-head`, `.md-amt`, `.md-price`, `.md-get`, `.md-bar`, `.md-sub`, `.md-title` - one row of that table: the amount, the price it would fill at, what it returns, and the bar that makes the slippage visible without arithmetic.

## When to use

On an Event Detail screen, collapsed, below the chart and the bet panel. That is the only place it belongs, and the nine screens it stands on are all of that one screen's variants.

Never on a feed, a card or a grid. A person scanning forty markets is not choosing between depth curves, and the product's own description rules it out in a sentence: not a trader's terminal.

On a resolved event this panel is describing something that no longer happens. The critique found the resolved body reusing the live one verbatim; the depth table is the part of that where the defect is worst, because a price by bet size on a settled market is a quote for a trade nobody can make.

## Rule

It opens closed and it says what is inside on the outside: the head names the mechanics so a person can decide without opening, because the cost of this block is the reading, not the pixels.

## Anti-rule

Never let its figures borrow the control colours: `.ms-yes` and `.ms-no` tint NUMBERS, and the tinted pair a person actually presses is `yesno`, so a stat block drawn as two green and red buttons would offer a bet where it is reporting one.

Seen: `CLAUDE.md`, where the separation is stated as the rule from `DESIGN.md` that decides other things, and `ui-kit/docs/inventory.md` L79, the row for the tinted pair, which is the control this file's figures sit next to on the same screen.

## States

- `summary.market-head @market-depth` - Closed, hovered, held and focused. The head takes the quiet control ground under the pointer and the pressed stone under a finger, and the chevron turns when the element opens. The open state is not photographed as a state of the head, because it is not one: it is the `<details>` attribute, and what changes is that a body appears below.
