# catnav

## Sources

- `ui-kit/docs/inventory.md` L63 to L65 - three rows, one component: the category band (57 screens, "per-category active; `.cat-condensed` strip on scroll"), the sub-category rail `.subcat` (32, category pages only), and the Trending sub-filter chips (5, marked UV).
- R4 in `ui-kit/docs/architecture.md` - one band, one level of sub-categories, a rail never nested in a rail, and **the sort control is not part of the band**. Counted: `.cat-nav` on 57 screens, `.subcat` on 33, maximum 1 each.
- R8 in `ui-kit/docs/architecture.md` - a system screen carries the frame and not the navigation: on the five system screens `.cat-nav` and `.subcat` are both 0.
- `ia/docs/sitemap.md` L318 and L327 - the wireframe pass made categories second-level NAVIGATION in a band under the header, routing to their own pages, and moved the feed's sort and frequency controls onto the heading row instead.
- `ui-kit/docs/backlog.md` S12 and S13 - the rail is a pinned box: its `top:120px` is one of three hand-typed clearances, and the vitrine shows this specimen 69px short because a frame that size IS a short window.
- `ui-kit/_levels.py` RAISE - this component owns `.cat-layout` and `.cat-main`, the page content plate, which is why it is a screen shell rather than a strip of chips.

## Purpose

Where you are in the product's own taxonomy, at two depths. A horizontal band of categories under the header on every browse screen, a vertical rail of sub-categories with counts beside a category page, and the same chips as a filter strip on Trending.

The decision inside it is that these are LINKS. A category in this product is a page with its own URL, its own About text and its own empty state, not a filter toggled in place, and the band is what makes that visible: you click a category and you arrive somewhere, with a back button that works.

## Anatomy

- `.cat-nav` - the band under the header. One per screen, and it condenses rather than disappearing when the page scrolls.
- `.cat-ic` - a category's mark. Outline, monochrome, and never the category's own colour, because a category is not an outcome.
- `.subcat`, `.subcat-head` - the rail on a category page: a heading and the sub-categories under it, sticky on desktop and a scrolling row of chips at 360.
- `.cnt` - the per-sub-category count. It is the rail's whole argument: a number tells a person which branch is worth opening before they open it.
- `.feed-subfilter` - the same chip family used as a filter on Trending, where there is no sub-category to navigate to.

## When to use

On a browse screen, once, directly under the header. The band belongs to screens whose job is to let a person choose an event; a screen a person reached by choosing one does not carry it.

The rail belongs to a category page and only there. It is the second level and there is no third: a sub-category with its own rail would be a taxonomy the product has not decided it has, and R4 says so with a count rather than a preference.

Never on a system screen. 404, 500, maintenance, the cookie screen and the toast catalogue carry the chrome and nothing to browse, and R8 measures that at 0 of 5 both ways: a system screen offers a way out, not a way around.

The sort control is not this component. It looks like the band, it sits near the band, and it belongs to `filters` on the heading row, because navigating and narrowing are different acts.

## Rule

One band, one rail, and both of them navigate: a chip in this component that changes the current page instead of leaving it is a filter wearing the navigation's clothes.

## Anti-rule

Never build the feed's sort or frequency control out of these chips: those belong to `filters`, which draws a dropdown whose label shows its current value, and a chip that looks like a category but silently re-sorts the list teaches a person that the band is unreliable.

Seen: `ia/docs/sitemap.md` L318, where the wireframe pass moved exactly these controls OFF the band and onto the heading row - "categories are second-level navigation in a sub-nav band directly under the header ... The heading row carries a Kalshi-style filter cluster (feed controls, not navigation)". The separation is in R4's own sentence too, and it is there because the two had been in one strip.

## States

- `button @catnav-chips` - The category you are in: brass ink, a lit mark, and the chip's ground answering. All four faces.
- `button @catnav-chips (2)` - A category you are not in, at rest, hovered, held and focused. One graphite chip family runs through this product, and this is its first member: the same face `loadmore` and the Load-more control wear.
- `button @catnav-subfilter` - A Trending sub-filter chip. Identical to the category chip on purpose, because it is the same control doing a narrower job on a screen that has no second level to navigate to.
- `button @catnav-subcat` - The active row of the sub-category rail, with its count. The count keeps its own quiet ink even when the row is active, so the number is read as data rather than as part of the label.
- `button @catnav-subcat (2)` - An inactive rail row, all four faces. The rail scrolls, so a row must answer a pointer without changing its height: a rail that reflows under the thumb loses the reader's place.
