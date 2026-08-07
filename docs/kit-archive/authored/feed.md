# feed

## Sources

- `ui-kit/docs/inventory.md` L82 - "Responsive card grid", filed under `components/feed.css`, on feed, category and favorites, states "populated / skeleton", 23.
- R5 and R7 in `ui-kit/docs/architecture.md` - both are rules about what may and may not stand in this grid: the full outcome list never inside a card, and no bet control on any screen that carries one. R7's counter is the sharpest description of this component's job: 23 screens carry the grid and 0 of them a bet panel or dock.
- R8 in `ui-kit/docs/architecture.md` - the five system screens carry the shell and 0 grids, which is what makes the grid a content decision rather than part of the frame.
- `ui-kit/_levels.py` STATIC - "the grid the cards stand in. Every control inside it belongs to card, catnav or loadmore".
- `components/patterns/browse-shell.css` and `components/patterns/card-grid.css` - the two compositions that actually arrange a browse screen. This file is what is left after both of them exist.
- The 105 painted screens, which is where the surprise is: the class is on all of them and the GRID is on 23.

## Purpose

The content column of a browse screen: the region cards stand in, and the heading above it. Two rules and almost nothing else, because everything that could leave this file has left it.

The emptiness has a specific history. The arrangement of a grid went to `components/patterns/card-grid.css`; the shell around it went to `browse-shell`; the plate under it belongs to `catnav`, which owns `.cat-layout` and `.cat-main`; the cards are `card` and the control at the foot is `loadmore`. What is left is the column itself and the one type rule that makes a feed heading a feed heading.

## Anatomy

- `.feed` - the column. It is a flex child that takes the remaining space and carries no ground of its own inside `.app-case`, because the plate under it is the frame's.
- `.feed-head` - the heading row above the list. The rule here is on the `h1` or `h2` inside it, in the display face, and it is why the feed's title reads as the page's title rather than as a section label.

## When to use

You do not reach for this file; you build a browse screen from `browse-shell` and `card-grid`, and this arrives with them. The one judgement it carries is the heading: the feed's title echoes the active category rather than saying "Live events", so what a person filtered to is what the page is called.

The grid it holds is where two rules of use bite. A screen with a grid of cards has no amount field and no Confirm on it, because a card's YES / NO routes to the detail with a side pre-selected and does not place a bet. And a card in it carries at most two option rows, because the full list belongs to the detail column.

Not on a system screen. 404, 500 and maintenance have a content column and nothing to put in it, and what stands there instead is a `state-block`.

## Rule

Nothing that commits money stands in this column: a browse screen is where a person chooses what to open, and every control in the grid routes rather than confirms.

## Anti-rule

Never treat the column as the plate: the two-stone surface under a browse screen is `catnav`'s `.cat-layout` and `.cat-main`, and painting a ground onto `.feed` would put a second stone inside the first on 23 screens, visible as a seam wherever the column is narrower than its plate.

Seen: `components/feed.css` itself carries the counter-declaration `.app-case .feed{background:transparent;padding:0}`, which exists because the vitrine's own feed specimen needs a ground and the product's must not have one. A rule written to REMOVE a background is a rule that was added after somebody found the seam.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC: this is the region cards stand in, and every control inside it belongs to `card`, `catnav` or `loadmore`, each photographed on its own page.

**One thing in this file should not have been here, and on 2026-08-03 it left.** `.grid-l` is the grid line of the price chart: the rule is `.app-case .chart-svg .grid-l`, it drew nothing on any feed, and it was in `components/feed.css`. The ownership map was not wrong about it - that was the file styling it with the fewest ancestors, so the map handed it here correctly - which is exactly why no check could see it, and why `coverage.md` reported the feed as owning a chart class while the level arithmetic read a chart part inside the feed. It is now in `components/chart.css`. The move was a cascade change and was proved as one, not assumed: `chart` loads at the end of level 3 and `feed` in the middle, so the rule now resolves later, and the full snapshot sweep is what says nothing moved.
