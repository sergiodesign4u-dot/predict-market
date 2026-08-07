# list-head

## Sources

- **71 painted screens**, which makes this the second most-used pattern in the system after the browse shell, and the one whose contents vary most: 26 of the 71 carry a title and nothing to sort, and the row is correct with the control side empty.
- R4 in `ui-kit/docs/architecture.md` - one category band, one level of sub-categories, **and the sort control is not part of the band**. Counted: `.cat-nav` on 57 screens, `.subcat` on 33, maximum 1 each.
- `ia/docs/sitemap.md` L318 - the wireframe pass that produced this row: "categories are second-level navigation in a sub-nav band directly under the header ... The heading row carries a Kalshi-style filter cluster (**feed controls, not navigation**), each a dropdown whose label shows the current value".
- `ia/docs/sitemap.md` L318 also settles the title: "The feed heading echoes the active category (for example \"Trending\"), not a generic \"Live events\" label, and updates when another category is chosen."
- `components/feed.css` - where the heading's type lives, and deliberately not here: `.feed-head :is(h1,h2)` in the display face is what the block LOOKS like.

## Purpose

A title on one side, the controls that act on the list on the other, wrapping to two rows when there is no room for one. It is a row and nothing else: what it decides is that a list's name and a list's controls belong together and above the list, and that neither squeezes the other.

## Parts

- `filters` - what usually stands in the control side: the sort and frequency dropdowns, each showing its current value in its own label.
- `feed` - the heading. Its display face and its colour are in `components/feed.css` because they are what the block looks like; this file only decides where it sits and what happens beside it.

## When to use

When a list needs a name and the list needs controls, and both belong to the list rather than to the page. The feed, the eight category pages, My Bets, the wallet, the notifications screen, both profiles.

With the control side empty, freely. Twenty six of the seventy one screens have a title and nothing to sort, and the row is right for them: the point is that the title has a settled place, so a list that later gains a sort does not move its own heading.

By hand: when the heading is the PAGE's and not a list's. A document's `<h1>`, a dialog's head, the event question on a detail screen - all of those are the subject of the screen rather than the name of a set below them, and they carry no controls because there is no list for a control to act on. The test is whether a control on that row would act on something directly underneath.

## Rule

The sort control lives here and not in the category band: categories are navigation and a sort acts on THIS list, and a sort inside the band makes it look like a place a person can go.

## Anti-rule

Never build the control side out of `catnav` chips. A chip in the band navigates and lands you on a page with its own URL; a control here changes the order of what is already in front of you, and it is a `filters` dropdown whose label shows its current value precisely so a person can see what it did without pressing it again.

Seen: `ia/docs/sitemap.md` L318, where the wireframe pass MOVED these controls off the band and onto this row, and the parenthesis it added is the record of what had been wrong - "feed controls, not navigation". R4 states the same separation from the band's side, and it exists because the two had been one strip.

## Arrangement

`flex-wrap` with `space-between`, so the controls drop under the title instead of squeezing it, and the control side is a wrapping row of its own, because two controls that do not fit should sit under each other rather than shrink. Source order at every width: title first, controls second, which is also the stacked order.

No states of its own. What answers a pointer is a `filters` dropdown, and its rest, hover, press and focus are photographed on that component's page.
