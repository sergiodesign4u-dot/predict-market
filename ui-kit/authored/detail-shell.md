# detail-shell

## Sources

- **11 painted screens**: every Event Detail variant, including the four bet-flow states, the resolved one and both logged-out ones.
- `ui-kit/docs/inventory.md` L97 - "Two-plate layout (`.ed-layout`: content + sticky bet panel)", on event-detail and event-detail-bet, states binary / multi. **Its screens column says 10 and the count is 11.** R3 and R7 both say 11 in `ui-kit/docs/architecture.md`, and `.ed-layout` is in 11 of the painted files, so the inventory row is one behind. It is the third number in that table found not matching the product, after L163 and L155.
- `docs/backlog.md` item 16a - `.ed-layout` and `.ed-main`, declared in `components/event-detail.css`, counted on 11 screens, which cleared the threshold and moved them to `components/patterns/`.
- R3 in `ui-kit/docs/architecture.md` - one bet control, and the WIDTH decides which: 11 screens with a panel, 8 with a dock, 8 with both in the markup and never both on screen, and the swap is a media query inside `components/betpanel.css`.
- R7 in `ui-kit/docs/architecture.md` - the panel stands on the logged-out detail as well, 3 of the 11, because the account is asked for at submit and not at the door.
- `ui-kit/docs/backlog.md` S12 - the panel's `top:120px` is one of the three hand-typed rail clearances, and the row says why no token can hold it: the header's 59px is CONTENT height.

## Purpose

A content column beside a sticky side panel, stacked under 760px and side by side above it. The panel is the bet panel today and the pattern does not know that: what this file decides is that one subject fills the screen and one action stays reachable while a person reads about it.

## Parts

- `event-detail` - the content column's own blocks: the head, the facts, the two-sided argument and the resolution rule.
- `betpanel` - the side panel, and the dock it becomes at 360. Its stickiness, its offset and its six states are all its own.
- `card` - the plate the column's sections stand on, which on this screen is `.card` doing its substrate job rather than its event-card one.
- `tabs` - the strip below the analysis, and the four panels it switches between.
- `market` - the collapsed mechanics at the foot of the column, which is the one block here a spectator must never be made to read.

## When to use

When one subject fills the screen and one persistent action must stay reachable while a person reads about it, and that action needs its own column on a desktop and its own dock at the foot of a phone.

The eleven screens are one screen's variants, which is worth saying plainly: this pattern has exactly one use in the product today, and it is a pattern rather than a component because the arrangement is stable while what stands in the column is not - eleven different content sets, including a resolved one where half the blocks are describing something that no longer happens.

By hand: when the side column is a second SET rather than one action about the main one. A rail of sub-categories, a table of contents, a list of related links - those belong beside a content column too, and they are `browse-shell`, whose rail is navigation and whose breakpoint is 900. The test is whether the side column's contents change when the main column's do: here they always do, because the panel is about the subject; in a browse shell they never do, because the rail is about the set.

## Rule

The breakpoint is 760 and it is the panel's own, not this pattern's: at 760 the bet panel appears and the dock disappears, which is one swap in `components/betpanel.css`, and two arrangements changing at two different widths would leave a band of widths where the page has both or neither.

## Anti-rule

Do not reach into the column from here. `.ed-main` gets `flex:1;min-width:0` and nothing else: its plate, its clip and its dropped right edge are in `components/base.css` with the rest of the frame, and a pattern that starts styling what it holds has become a component with a layout attached.

Predicted: it has not happened, and the pair most likely to produce it is this pattern against `browse-shell`. Two shells, two columns each, two breakpoints, and each is the obvious wrong answer for the other - which is exactly why the line is worth writing and exactly why it carries no incident. The two have never been confused on a screen; they have different breakpoints for different reasons and the reasons are recorded in R3 and R4 rather than in a defect log.

## Arrangement

Column at 360, row at 760 and up, content first and panel second in source order, so the stacked order puts the reading before the action. The panel sticks at 120px from the top and that number belongs to `betpanel`; this file does not know it.

No states of its own. Everything that answers a pointer belongs to `betpanel`, `tabs`, `event-detail`, `card` or `market`, and each is photographed on its own page. What this pattern owns is two flex declarations and a media query.
