# oddsbar

## Sources

- `ui-kit/docs/inventory.md` L78 - "Odds bar (thin, green YES on red track)", filed L1, on feed, category and detail cards, and the value column says *injected from prob* rather than a number.
- The 105 painted screens: `.oddsbar`, `.track` and `.fill` are on every one that carries a card, and `.ed-oddsbar` is the thin variant in the event head.
- `ui-kit/docs/backlog.md` S14, which is this component's open defect and was re-measured on 2026-08-03: 378 elements below the contrast floor, all of them `.l-yes` and `.l-no`.
- `ui-kit/_levels.py` STATIC, where this component is declared non-interactive with the reason "a datum drawn to a width. It reports the market and answers no pointer".
- `components/oddsbar.css`, and the feed script that builds the bar out of the probability text.

## Purpose

The market's answer, drawn as a length. A bar of two colours whose split IS the probability: green for YES, red for NO, and the position of the join is the number. It is the one thing on a card that a person reads without reading, and it is the reason a card can be scanned in a list.

It is a DATUM and not a control. Nothing here answers a pointer, and that is declared rather than forgotten: `_levels.STATIC` names it, gate 25 holds it, and the check runs both ways so this file may not quietly grow a hover either.

## Anatomy

- `.oddsbar` - the bar itself, on a card. Built by the feed script from the probability text, which is why no screen file contains the element and gate 30 has a declared line for it.
- `.track` - the ground the fill runs on, the NO side.
- `.fill` - the YES side, drawn to a width that is the probability.
- `.lbls` - the row under the bar that says the two numbers in words.
- `.l-yes` - the YES label. On graphite it clears the floor; in daylight it measures 2.62:1 against a 4.5 floor, on every card of twelve feed screens.
- `.l-no` - the NO label, 4.35:1 on graphite and 3.76:1 in daylight. Both halves of S14.
- `.ed-oddsbar` - the same bar, thinner, in the head of an Event Detail screen, where the big number is already printed beside it and the bar is confirming rather than reporting.

## When to use

Wherever a binary market has to be readable at a glance and there is no room for a chart: the card in a feed, the card in a grid, the head of a detail screen. It carries no interaction, so it never needs a target size and never competes with the card's own tap area.

Do not reach for it to show a multi-outcome market. A market with four candidates is four rows and the system draws that with `options`, because a stacked bar of four colours would put green and red on candidates, and in this product green and red mean an OUTCOME and nothing else.

## Rule

The width is the datum: the fill is drawn to the probability and nothing else may set it, which is why `style="width:NN%"` on the fill is one of the three things gate 9 lets through.

## Anti-rule

Never let this bar carry a candidate or a category colour: a multi-outcome market is `options`, whose rows are neutral, because green and red are the outcome semantics of this product and a candidate is not an outcome.

Seen: `DESIGN.md`, where the rule is written as the one that decides other things, and `ui-kit/docs/inventory.md` L78, where this component's own row is described by its two colours.

## States

None, and it is declared rather than missing: `ui-kit/_levels.py` STATIC carries the line "a datum drawn to a width. It reports the market and answers no pointer", and gate 25 fails the build both ways, so a component on that list may not grow a hover without the declaration going first.
