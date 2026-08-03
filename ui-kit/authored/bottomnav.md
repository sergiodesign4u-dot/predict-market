# bottomnav

## Sources

- `ui-kit/docs/inventory.md` L66 - "Bottom nav (mobile, 4 slots)", filed L3, on all header screens, states "per-slot current; logged-out (Sign in slot)".
- R9 in `ui-kit/docs/architecture.md`, the rule that exists to stop a later correction: the bar stands on 104 of 104 screens, once each, **including all 17 whose content IS an invoked overlay**, and the row says in as many words that the textbook rule "a tab bar is hidden on the sign-in screen" is false here.
- `voice/docs/microcopy.md` L141 to L144 - the four labels as shipped: *Events*, *My Bets*, *Favorites*, *Portfolio*, with the second carrying the bet-vs-position flag and the third the Bookmark-vs-save-vs-Favorites flag.
- `ia/docs/sitemap.md` L325 - the wireframe pass MOVED Favorites into the mobile bottom bar, swapping it with Notifications. The four slots are a decision that was changed once, not a default.
- The 105 painted screens, and `ui-kit/shell.html`, which composes this specimen with the header rather than holding markup of its own.

## Purpose

The product's whole navigation at 360px. Four slots, a mark on the one you are standing in, and nothing else: no menu, no overflow, no fifth thing behind a chevron. At the width most of this product is read at, this bar is not a convenience over the header, it is the only way to get anywhere.

The fourth slot carries a figure, and that is the one decision in it worth defending. The balance rides in the nav because a person about to back an opinion needs to know whether they can, not because the product wants them looking at it: nothing in the bar changes when the number does, and no notification in this product is ever about topping it up.

## Anatomy

- `.bottom-nav` - the bar. Four `<li>`, each an anchor around a button, and the current slot is marked on the `<li>` with `aria-current="page"` rather than on the control, so what is highlighted and what is announced are the same fact.
- `.bn-bal` - the balance figure in the fourth slot, above its label. It is the only slot whose content changes at run time.

## When to use

Never by choice. The bar is chrome: it is emitted with the header on every screen, and a screen that has it is not opting in, it is simply a screen.

The judgement it does need is the one R9 protects. Seventeen screens in this product ARE overlays - deposit, sign-in, win, loss - and every instinct says a modal should trap a person until they answer. These do not. A person who opened Add funds and changed their mind leaves through the same four slots as everywhere else, and the day someone "fixes" that, the product will have taught a person that money screens are harder to leave than to enter.

The logged-out variant changes the fourth slot and nothing else. The other three are browsable without an account, because the account is asked for at submit and not at the door.

## Rule

Four slots, on every screen, one of them marked: if a screen wants a fifth destination, that is an argument about the product's shape and not about this bar.

## Anti-rule

Never use it to switch what is on the screen you are already on: a bar that changes the panel below it is `tabs`, which is a control inside a page, while this one is the page's exit. The two look alike at 360 and mean opposite things, and the difference a person feels is whether the back button now does something.

Predicted: it has not happened in this product, and R9 exists because it is expected to. The rules table gives that row its own sentence - "this row exists so that nobody later fixes the product into the textbook" - which is the same class of prediction, made about the same bar, from the other direction. See `ui-kit/docs/architecture.md`, R9.

## States

- `button @bottomnav` - The slot you are standing in. Brass ink and a lit mark, and the state lives on the list item rather than on the button, which is why the pressed and hovered faces below are the same control in a different place rather than a different control.
- `button @bottomnav (2)` - A slot you are not standing in: at rest, under the pointer, held, and focused. Quiet ink, the ground answers, and the mark does not grow. A tab bar that animates under a thumb is a tab bar that is hard to aim at.
