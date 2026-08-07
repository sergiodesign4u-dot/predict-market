# notice

## Sources

- `ui-kit/docs/inventory.md` L114, L124, L125, L132, L133, L134 and L143 - seven rows for one file: the bet sub-state boxes, the funds-protection line, the on-ramp widget box, the inline error, the spinner box, the S5 reconcile box and the push-permission banner. No other component in the system is inventoried seven times.
- `voice/docs/microcopy.md` L1008 and the Step 09 / Step 12 records - the copy these boxes carry: the funds line "USDC held 1:1", the reconcile box that must show the NEW price, and the error lines the Forbidden list rewrote away from "Something went wrong".
- `ui-kit/docs/backlog.md` S6 - "A neutral page-level callout. Nothing says *read this before the page* without a meaning attached." The Terms page wore `.spinner-box`, `.reconcile-box` and `.protect` for three blocks that are none of those things, and the row calls it a naming debt.
- `ui-kit/docs/backlog.md` S7 - `.protect` is 11px, and block B7, the money answer, is now the smallest text on the page that most needs it.
- `ui-kit/_levels.py` STATIC - the entry that says what a person will ask first: these boxes look interactive and their buttons are `.state-btn`, which belongs to `button`.
- The 105 painted screens.

## Purpose

The product's inline answers: the small boxes that stand where something needs saying at the moment it happens, without taking the screen. Funds are safe. The price moved while you were deciding. This did not register and no money was taken. Notifications are switched off at the operating system, here is how.

They are one component because they are one decision, not because they look alike: **a thing a person must read but must not be stopped by**. A dialog stops. A toast disappears. These stay on the page, in the flow, until the situation that raised them is over.

## Anatomy

- `.protect` - the funds line. The plainest sentence in the product and the one it is most often judged on, at 11px.
- `.inline-error` - an error inside a flow, in neutral stone rather than red, because red in this product means an outcome and a failed deposit is not one.
- `.spinner-box` - the waiting box: something is happening and it is this.
- `.reconcile-box` - the S5 box, where the odds moved between deciding and confirming. It is the only one of the seven that must show a number a person has not agreed to yet.
- `.widget-box` - the on-ramp placeholder, and its load-failure face.
- `.push-banner`, `.push-msg`, `.push-actions` - the in-app banner for permission the browser has refused. It appears on 2 screens and it is the only member with actions of its own.

## When to use

Where the fact belongs, not where there is room. Every one of these sits inside the flow it describes: the funds line under the amount, the reconcile box above Confirm, the error where the action failed.

When a person must be able to find it again. This is the whole boundary against `toast`: a toast is safe to miss and goes away on a timer, and everything in this file is something a person may need to re-read after they have looked away.

Not as the screen's whole answer. When there is nothing else to show at all - no events match, the load failed, the list is empty - that is `state-block`, one per screen, with the screen's only exit in it.

Not as a neutral callout, however tempting. There is no member of this family that means "read this first" with no situation attached, and backlog S6 is the row that says so. Three blocks on the Terms page are wearing these names for jobs they do not have, and the file is honest about it rather than quietly widened.

## Rule

Every box in this file names a situation, and the situation is why it is on the screen: a box that would carry general information has no member here, and adding one is a system decision rather than a screen's.

## Anti-rule

Never use one of these as a screen's empty or error state: that is `state-block`, which stands at most once and carries the screen's only way out, and a notice put in its place leaves a person on a page with nothing to press.

Seen: R2 in `ui-kit/docs/architecture.md` and the two rows behind it in `wireframes/_critique.md` - the state block shipped twice with a dead exit, eight category empty states with bare `<button>` CTAs and then `Try again` bare on the feed error and all eight category error screens. The rule's own sentence names the confusion from this side: "if a screen shows two blocks that each have a title, a message and a pair of actions, one of them is a notice".

## States

None, and it is declared in `ui-kit/_levels.py` STATIC: the banners and boxes carry no interaction of their own, and everything a person presses in one of them - *Try again*, *Check wallet*, *Enable notifications*, *Confirm at new price* - is a `.state-btn` and is photographed on `button`'s page.

The distinction that entry protects is worth stating, because a reader looking at `.push-banner` will doubt it: the banner HAS actions, and it does not OWN them. What this file draws is the box, the stone and the sentence; what answers a pointer inside it belongs to another component and has its states there.
