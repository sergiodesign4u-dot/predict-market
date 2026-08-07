# browse-shell

## Sources

- **77 painted screens**, the most-used pattern in the system: the feed, the eight category pages and their states, Favorites, My Bets, the wallet, notifications, both profiles, the system screens and the Terms document.
- `docs/backlog.md` item 16a - `.cat-layout` and `.cat-main`, declared in `components/catnav.css`, counted on 76 screens by the containment reader, which is what moved them to `components/patterns/`.
- `ui-kit/docs/backlog.md` S1, S2 and S5, all closed 2026-08-03 - building `ui-visual/terms.html`, a page of a TYPE the system had never drawn, taught this pattern two things: it grew a reading column (`--container-doc`, 600px, measured after at 592px and 67 characters), and **its rail learned that it is a SLOT rather than a category rail**.
- `ui-kit/docs/backlog.md` S13 - a specimen frame is a window, so a component capped to the window caps inside it: this pattern's rail specimen settles at 430px from 499px and shows its feet behind an internal scroll. Truthful and a worse showcase, and the answer belongs to the vitrine rather than to the pattern.
- R4 in `ui-kit/docs/architecture.md` - `.subcat` at most once, and a rail never nests inside a rail.
- R8 in `ui-kit/docs/architecture.md` - the five system screens carry this shell and none of `.cat-nav`, `.subcat`, `.grid` or `.card`, which is what proves the shell is frame and its contents are not.

## Purpose

A narrow rail beside a content column, stacked under 900px and side by side above it. It owns none of what it holds and paints none of it: what it says is where the two columns are, in which order they stack, and that the content column may not be pushed off the screen by its own contents.

## Parts

- `catnav` - the sub-category rail, on a category page. Its chips, its counts and its sticky offset are its own.
- `toc` - the same slot on a document page, holding a table of contents instead. This is the thing Terms taught: the rail is a SLOT, and the pattern does not know which component is standing in it.
- `filters` - the controls that stand in the content column's head on most of the 77.
- `state-block` - what stands in the content column when there is nothing to show, on 38 of them.
- `button` - the exit inside that block, because on an empty screen it is the only thing to press.

## When to use

When a screen browses a set - a category, a list of bets, a wallet ledger, a profile, a document - and there is a second, narrower axis that belongs BESIDE the content rather than above it.

Fourteen different sets of content stand in the column across the 77 screens, and that is the argument for a pattern rather than a component: the arrangement is stable and what it holds is not.

With the rail empty, freely. The variant `:not(:has(.subcat))` gives the column the full height instead of hanging it at the top of a row it is the only member of, and it is decided by specificity (0,3,0 against 0,1,0) rather than by file order.

By hand: when the two columns are about ONE subject rather than a set and its axis. A screen where the side column acts on what the main column is showing - a bet panel beside an event, a preview beside a form - is `detail-shell`, and the difference is not the widths, it is what the side column is FOR. The test: if the side column's contents change when the main column's contents change, it is not this pattern.

## Rule

The rail goes first in the markup and the column second, at every width: the stacked order under 900px is the source order, so a rail written after the column would land under it on a phone and beside it on a desktop.

## Anti-rule

Do not put the page's own surface on it. The two-stone plate under this shell is in `components/base.css` with the rest of the frame, because it is what the PAGE is made of and not what this arrangement is, and a pattern that carries a background is a component with the label filed off.

Seen: gate 23 in `ui-kit/_check_kit.py` fails the build on a pattern that carries a colour, and it exists because the pattern extraction had to decide, file by file, which declarations were arrangement and which were paint. `ui-kit/docs/backlog.md` S11 is the same question answered the other way in a component: eight rules that were paint had been living in `components/account.css` beside one line that was arrangement, for three stages.

## Arrangement

Column at 360, row at 900 and up, with the gap changing with the direction, because the distance between two columns is not the distance between two stacked blocks. The content column takes `flex:1;min-width:0`, and the `min-width` is the load-bearing half: without it a long word inside a card pushes the rail off the screen.

The rail's own sticky offset is NOT here. `top:120px` belongs to `catnav`, and `ui-kit/docs/backlog.md` S12 records why that number cannot be a token and why the three copies of it were already meant to differ: `toc` sits at 66px in this same slot, because a document page has no category bar for the header strip to condense into.

No states of its own. Everything that answers a pointer in this shell belongs to `catnav`, `filters`, `toc` or `button`, and each is photographed on its own page.
