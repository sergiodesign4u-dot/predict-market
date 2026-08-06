# header

## Sources

- `ui-kit/docs/inventory.md` L55 to L61 - seven rows: the lean app header, the logo, the balance swap, the notifications bell and its dropdown, the avatar menu, the how-it-works button and the ghost icon button. The header row itself carries the state pair "logged-in / logged-out; rest / `.scrolled` (condensed)".
- R1 in `ui-kit/docs/architecture.md` - one primary action per ZONE, written per zone because per screen it is false on 14 of 104, and all 14 carry `.auth-btn primary` in this component and `.state-btn primary` in the body.
- R6 in `ui-kit/docs/architecture.md` - the logged-out header carries no account, and the counter partitions the tree exactly: 31 screens with `.auth-btns`, 73 with `.bal-toggle`, 0 with both and 0 with neither. The bell and the heart stay as affordances that route to sign-in.
- `ui-kit/docs/backlog.md` S17, closed 2026-08-03 - the icon circle was declared twice and is now one block naming `.icon-btn` and the two `<summary>` elements; each keeps its own geometry, because a 36px square and an inline-flex row with a gap are not the same thing.
- `ui-kit/docs/backlog.md` S12 - this component is where two of the three hand-typed rail clearances come from: the header's 59px is CONTENT height and the condensed strip's 54px is a literal in `components/header.css`, so no token can hold either.
- `CLAUDE.md` - the chrome reconcile order: "the paint owns what the header IS, the wireframe owns which state it is IN", `ui-visual/_reconcile_chrome.py` then `wireframes/_generators/port_chrome.py`, or a port carries the wrong answer into 104 files.
- The 105 painted screens.

## Purpose

The band every screen wears, and the product's account in one row. A logo home, the how-it-works opener beside it, and on the right the utility cluster: the balance with its swap and its plus, the bell, the heart, the avatar.

Its shape is decided by one fact: this is a product where money sits behind an account, and the account is asked for at submit rather than at the door. So the header has two materially different variants rather than one variant with pieces hidden, and R6 measures that as a clean partition of the tree - never both, never neither.

## Anatomy

- `.app-header` - the band, and `.left`, `.row`, `.utility` its three regions.
- `.logo-btn` - home, which in this product means Events.
- `.hiw-btn` - the how-it-works opener, next to the logo because that is where a person hesitates.
- `.bal-toggle`, `.bal-figure`, `.bal-label`, `.bal-amt` - the balance. The label is part of the figure, not decoration: a bare number in a header is the kind of thing this product's first principle exists to forbid.
- `.icon-btn` - the ghost circle, shared by every utility control, and since 2026-08-06 it is not this file's. It left for `components/iconbtn.css` with its two modifiers, the balance swap and the plus that opens Add funds, because it is an ATOM the whole product wears and this file is a band. What stays here is where it sits: the band hides one of them below the breakpoint, and hiding a control in a band is the band's decision.
- `.bell-wrap`, `.notif-menu`, `.badge-dot`, `.notif-empty`, `.notif-all` - notifications: the bell, its dropdown, the unread mark, the empty face and the way through to the full screen.
- `.avatar-menu`, `.dropdown` - the account menu, built on `<summary>` so it opens without script.
- `.auth-btns` - the logged-out pair, Sign in and Sign up, and the one place `.primary` is allowed inside this band.
- `.cat-condensed` - the strip the category band becomes when the page scrolls, declared here because its height is what every sticky rail below clears.

## When to use

Never by choice; it is emitted with the shell. What a person building a screen decides is which VARIANT the screen is in, and that decision belongs to the grey tree: `wireframes/` owns whether a screen is logged in or out, whether the bell is empty, and which bottom-nav slot is current, while what the band is made of belongs to the paint.

That order is not a convention, it is a repair. Reconciling the other way round - taking the state from the paint - carried a wrong answer into 104 files once, and `CLAUDE.md` now names the two scripts in the order they must run.

The one judgement left inside the band is R1: at most one filled brass button in it. On 14 screens there is also a brass button in the body, and both are correct, because the header's job and the page body's job are different.

## Rule

Logged out means no account in the band: no balance, no avatar menu, no notifications dropdown, and the bell and the heart stay as affordances that route to sign-in rather than disappearing.

## Anti-rule

Never draw the utility circles from the `button` family: `.icon-btn` and the two `<summary>` elements are a transparent ground with a hairline and a pill radius, while `button` gives a quiet control `--bg-control` and a 10px radius. Painting one from the other puts a filled chip in a band whose whole material is the absence of one.

Seen: `ui-kit/docs/backlog.md` S17, opened by a browser reading and closed on 2026-08-03. The circle had been declared twice inside this file and kept in step by hand, which is one step away from being declared a third time in `components/button.css` - and S16, closed the same day, is what that looks like when it happens: one quiet button under five names.

## States

- `button.logo-btn @.app-header` - Home, at rest, hovered, held and focused. The mark does not change colour under a pointer; only the ground answers, because the logo is the one thing in the band that must look identical on all 105 screens.
- `button.hiw-btn @.app-header` - The how-it-works opener, all four faces. It sits beside the logo and wears the same quiet circle as the utility cluster, so nothing in the band claims to be the primary action.
- `summary @.app-header` - **The bell and the avatar, and they are the ghost circle drawn on a different ELEMENT.** A `<summary>` opens a dropdown and a `<button>` does not, which is why they stayed here when `.icon-btn` left for `components/iconbtn.css` on 2026-08-06: the two files now say the same three declarations, each about the element it owns. The count badge the bell carries is content inside the circle and not a state of it, and it is live on this page in the logged-in specimen.
- `button @.app-header` - A plain control inside an open dropdown: the quiet row a person lands on when the avatar menu is down.
- `a @.app-header` - A link inside the band, at rest and under the pointer. Every link in this product lives inside a component that styles it, and this is that rule holding in the chrome.
- `a.notif-all @.app-header` - The way from the bell's dropdown to the full Notifications screen. It is the dropdown's only exit, so it is underlined at rest rather than on hover.
