# state-block

## Sources

- `ui-kit/docs/inventory.md` L140 - "State block (`.state-block`: icon + title + message + action)", filed L3, on feed, category, detail, active-bets, notifications, wallet, profile, 404, 500 and maintenance, states empty / error, 38.
- R2 in `ui-kit/docs/architecture.md` - one per screen, at most one `.state-actions` in it, and the sentence that makes the count load-bearing: the single block is then the screen's ONLY exit.
- `wireframes/_critique.md` - the two rows R2 cites, and they are the reason this component is written about rather than described. Row 1 of the step-4 pass: eight category empty states whose CTAs were bare `<button>`s. Row 1 of the flow pass: `Try again` bare on the feed error and all eight category error screens, while every other error screen already linked it.
- `voice/docs/voice.md`, Forbidden - "AI-cliche error copy. No *Oops*, no *Something went wrong*, no filler", with the before and after taken from the real Event Feed and My Bets errors. Every message in this component is written against that line.
- `voice/docs/microcopy.md` Step 15 - the system nodes, where `.sys-links`, `.sys-link-list` and `.sys-note` were added so a 404 offers somewhere to go rather than an apology.
- R8 in `ui-kit/docs/architecture.md` - on the five system screens this block is the whole content, because those screens carry the frame and not the navigation.
- The 40 painted screens.

## Purpose

What a screen says when it has nothing to show. A mark, a title, one sentence, and the way out: no events matched the filters, the load failed, there are no active bets yet, this page does not exist.

Its shape follows from one thing being true at once: this block is the screen. There is nothing else on the page to click, so whatever it offers is the only thing a person can do, and a block that states a problem without offering that is a dead end with a title on it.

## Anatomy

- `.state-block` - the block itself, centred in the content column.
- `.state-title` - the title. It names what happened in the product's own words: "No events match your filters", not "Nothing here".
- `.state-msg` - one sentence saying what to do about it.
- `.state-actions` - the exit, at most one per block, and its buttons are `.state-btn` from `components/button.css`.
- `.sys-links`, `.sys-link-list` - the extra destinations a system screen offers, because a 404 has no filter to relax and no request to retry.
- `.sys-note` - the small line under those, where a system screen says the thing that is true but not actionable.

## When to use

When the screen's content is absent, failed, or has not happened yet, and only then. This is not a banner on a working page: if there is a list and one thing about it needs saying, the list stays and the thing is a `notice`.

Once. R2 is a count and the count is the point: two blocks on one screen means a person has two "only" exits, which is not twice as helpful, it is a screen that does not know what state it is in.

On a system screen it is the whole body. 404, 500 and maintenance carry the chrome, this block, and nothing to browse, and the extra link list exists because those three are the cases where "try again" is not an answer.

## Rule

Every block leaves by a real destination: the action is a link or a route that works, not a bare button, because on this screen it is the only thing there is to press.

## Anti-rule

Never let its action ship as a bare `<button>`: the exit is a `.state-btn` from `button` wrapped in something that actually navigates, and a bare element here looks identical, passes every visual check, and strands a person on the one screen in the product that has nothing else on it.

Seen: `wireframes/_critique.md`, twice. Row 1 of the step-4 pass found eight category empty states whose CTAs were bare `<button>`s, and row 1 of the flow pass found `Try again` bare on the feed error and all eight category error pages, while every other error screen in the product already linked it. It shipped twice, in two different passes, on sixteen screens, which is why R2 quotes the critique rather than the counter.

## States

None of its own, and it is not a STATIC declaration but an ownership one: everything a person can press in this block is a `.state-btn` or a link inside `.sys-link-list`, and both are photographed where they are declared. The block is a mark, a title and a sentence, and none of the three has a face to change.

One state IS declared here and produced no photograph: `.sys-link-list a:hover`. The specimens this component stands in are the empty and error blocks of a browse screen, and none of them carries a system screen's link list, so the states pass had nothing to open. That is a gap in the stand rather than in the component, and it is named here because a gallery with no pictures reads as "this has no states" when the file says otherwise.
