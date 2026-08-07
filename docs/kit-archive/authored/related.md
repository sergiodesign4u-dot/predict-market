# related

## Sources

- `ui-kit/docs/inventory.md` L90 - "Related events plate (`.related-events`)", filed L2, on event-detail, state list, 9 screens, and its art column says *event*.
- The 10 painted screens that carry it, all of them an Event Detail variant, including the four bet-flow states and the resolved one.
- `voice/docs/microcopy.md` L1423 - the label `Browse more events` on `.related-more`, with the reason recorded: "same verb as the empty states, so leaving a dead end reads the same everywhere".
- `ui-kit/docs/backlog.md` S3, where the standalone control after prose was the answer to a link inside a sentence, and this component is the pattern that answer was taken from.
- `ui-kit/docs/backlog.md` L29, where this is one of the nine components the Terms page was assembled from without a new class.

## Purpose

The way out of an event that is not the way back. Three or four other markets at the foot of a detail screen, each a question with its odds, so a person who has finished reading one event has somewhere to go that is not the browser's back button.

It exists for the moment a screen has answered its question. An event that is resolved, a bet that is placed, a market a person decided against: all three end with a person on a page that has nothing left to do, and this is the block that stops that being a dead end.

## Anatomy

- `.related-events` - the plate at the foot of the detail column.
- `.related-list` - the rows.
- `.rel-thumb` - the event photograph, which is content and goes on the element as a background image, one of the three things gate 9 lets through.
- `.rel-q` - the question. The whole question, wrapped, not truncated: a market a person cannot read is not a suggestion.
- `.rel-odds` - the current probability, the one figure a row carries.
- `.related-more` - the standalone control under the list, labelled *Browse more events* because that is the verb every empty state in the product uses.

## When to use

At the foot of an Event Detail screen, and it is on all ten of them for a reason: the four bet states, the resolved state and the logged-out variants are exactly the moments when a person is most likely to be finished.

Not on a feed. A list of events at the foot of a list of events is the same list twice, and the browse screen's own way out is `loadmore`.

Not as a recommendation engine's slot. The rows are other markets in the same category, and the block says so by standing where it does rather than by claiming relevance it cannot prove; a heading like "You may also like" would be exactly the borrowed authority the product's second design principle rules out.

## Rule

Every row is a whole question and a real number: a truncated market or one with no odds is a suggestion a person cannot judge, which is worse than no suggestion.

## Anti-rule

Never put its way-out control inside a sentence: the system styles no `a` in body prose, so a link written into a paragraph renders in the browser's own blue, and the two blocks that carry prose in this product, `seo-plate` and this one, both answer it the same way, with a standalone control after the text.

Seen: `ui-kit/docs/backlog.md` S3, opened while building the Terms page, where the link was moved OUT of the sentence into a standalone control rather than an inline link style being invented, and this component's `.related-more` is what it was moved to look like.

## States

- `a @related` - A row at rest and under the pointer. The plate answers, the photograph does not move, and the question stays exactly where it was: a row that shifts under the pointer is a row a thumb misses.
- `a.related-more @related` - The way-out control: the graphite chip family's answer, the same one `loadmore` and the category chips give, because a person who has met one of them has met all three.
