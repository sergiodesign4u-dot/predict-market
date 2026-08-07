# loadmore

## Sources

- `ui-kit/docs/inventory.md` L91 - "Load-more control", filed L1, on feed and category, states rest / hover, 20+ screens claimed.
- The painted screens, counted: 9 carry it, all of them a feed or a category in its full state. It is absent from every empty, error and loading variant, which is the decision this page is mostly about.
- `voice/docs/microcopy.md`, where the label is *Load more events* and not "Show more", "Next" or a page number.
- `components/loadmore.css`, whose hover read `--bg-control-hover` and `--line-brass-soft`: the graphite chip family's answer, not the button family's. That line was written before the chip family had a file, and it is the whole finding this component was eventually closed by.
- `ui-kit/docs/backlog.md` S41, which said on the day it was opened that this control measures as `.cat-nav button` and that the component should not exist.

## Purpose

The end of the list, and the offer to have more of it. One quiet chip under the last card, centred, wide enough to hit with a thumb and quiet enough that it does not compete with the cards above it.

It is the visible half of a decision the product made about pagination: the feed does not number its pages and it does not load as you scroll. A person asks for more, once, and the screen keeps its scroll position. That is why this is a control and not a sentinel.

## Anatomy

- `.load-more-wrap` - the band the control is centred in, which is what keeps it from reading as the last card in the grid. **Since 2026-08-07 it is the whole of this component**, and the control inside it is a `chip`: `.chip.chip-nav`, because the two were one graphite chip drawn in two files. The name `load-more` is kept as a hook the feed's script reaches for and as what this vitrine's census calls the kind, and it draws nothing at all - declared in `ui-kit/_adoption.py` UNSTYLED, the same way `.cmt-post` is.

## When to use

At the foot of a list that has more behind it, and only there. Nine screens: the four categories and the general feed, each logged in and logged out.

It does not belong under a list that is complete, and it does not belong under a list that is empty. Both of those already have their own answers: a complete list simply ends, and an empty one takes a `state-block`, whose sentence says why there is nothing and whose control offers a way out. Putting a Load more under an empty feed asks a person to fetch more of nothing.

## Rule

One per list, at the foot, and the label names what is being loaded: *Load more events*, not "Load more".

**It wears the category chip and it is not a category.** Its ROLE is `action` - it fetches - and its ATOM is `chip`, which is the same split the footer's social marks have in the other direction. A role is what a control MEANS; an atom is where its RULES live, and there is exactly one file in this system that says what `--bg-chip` on `--bevel-notice` at a 10 corner looks like.

## Anti-rule

Never use it as the action of an empty screen: nothing is behind it there, and the control that belongs under an empty list is the `state-block` one, which says what happened before it offers anything.

Seen: `wireframes/_critique.md` L14, the dead-end finding on the eight category empty screens, where the empty state's own CTA led nowhere. The same screens are the ones this component is deliberately absent from.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC. Every state this component used to have was `.chip-nav`'s already: the hover was `--border-brass-hover` on `--bg-control-hover` with `--text-strong`, in that order, in two files, and both pressed to `--bg-pressed`. Four declarations separated the two at rest and three of them were nothing - an inert `min-height:44` on a control whose content box is 47, the button family's `.01em` of tracking on a 14px label, and four pixels a side of padding. The fourth was a lit top edge, and the chip family had decided against one on purpose so that nothing is lifted to flatten under a finger. The gallery is on the chip page.
