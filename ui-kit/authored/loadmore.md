# loadmore

## Sources

- `ui-kit/docs/inventory.md` L91 - "Load-more control", filed L1, on feed and category, states rest / hover, 20+ screens claimed.
- The painted screens, counted: 9 carry it, all of them a feed or a category in its full state. It is absent from every empty, error and loading variant, which is the decision this page is mostly about.
- `voice/docs/microcopy.md`, where the label is *Load more events* and not "Show more", "Next" or a page number.
- `components/loadmore.css`, whose hover reads `--bg-control-hover` and `--line-brass-soft`: the graphite chip family's answer, not the button family's.

## Purpose

The end of the list, and the offer to have more of it. One quiet chip under the last card, centred, wide enough to hit with a thumb and quiet enough that it does not compete with the cards above it.

It is the visible half of a decision the product made about pagination: the feed does not number its pages and it does not load as you scroll. A person asks for more, once, and the screen keeps its scroll position. That is why this is a control and not a sentinel.

## Anatomy

- `.load-more` - the chip. Graphite ground, hairline edge, pill corners, the label in the body face.
- `.load-more-wrap` - the band it is centred in, which is what keeps it from reading as the last card in the grid.

## When to use

At the foot of a list that has more behind it, and only there. Nine screens: the four categories and the general feed, each logged in and logged out.

It does not belong under a list that is complete, and it does not belong under a list that is empty. Both of those already have their own answers: a complete list simply ends, and an empty one takes a `state-block`, whose sentence says why there is nothing and whose control offers a way out. Putting a Load more under an empty feed asks a person to fetch more of nothing.

## Rule

One per list, at the foot, and the label names what is being loaded: *Load more events*, not "Load more".

## Anti-rule

Never use it as the action of an empty screen: nothing is behind it there, and the control that belongs under an empty list is the `state-block` one, which says what happened before it offers anything.

Seen: `wireframes/_critique.md` L14, the dead-end finding on the eight category empty screens, where the empty state's own CTA led nowhere. The same screens are the ones this component is deliberately absent from.

## States

- `button.load-more @button-outcome-row` - Rest is the graphite chip: a quiet ground inside a hairline. Hover takes the ground one step and the edge to the soft brass, the same pair the category chips and the filter chips answer with, which is what makes those three one family to a person's eye. Held down it settles onto the pressed stone. The focus ring is the system's, unchanged, because the ground it stands on is the ordinary one.
