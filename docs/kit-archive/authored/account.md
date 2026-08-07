# account

## Sources

- `ui-kit/docs/inventory.md` L161 - "CTA bar (`.cta-bar`: Add funds + Open Wallet / Withdraw)", filed L2, on how-it-works, my-profile and wallet, 3 screens. That row is true.
- `ui-kit/docs/inventory.md` L163 - "Transaction list (deposits/payouts/fees/stakes)", filed under `components/account.css`, L2, wallet, states list / loading / error. **That row is false as of 2026-08-03**: this file has two rules and neither of them is a transaction list. What draws that list is `components/position.css`, whose `.pos` rows carry it, and the inventory has not been told.
- The 3 painted screens, and `components/patterns/action-bar.css`, which holds the arrangement of the same bar.
- `ui-kit/docs/backlog.md` S11, closed on 2026-08-03: eight rules that painted this bar's BUTTON moved to `components/button.css`, and one line of arrangement moved to the pattern.
- `ui-kit/_levels.py` STATIC, where the entry written that day says what is left: a stone, a hairline, two corners, and the three declarations `.flat` takes them away with.

## Purpose

The surface an action bar stands on, and nothing else. Two rules: the bar's own stone with a hairline along its top edge and two rounded top corners, and the variant that takes all three away where the page has no scroll to hold the bar against.

It is a component with almost nothing in it ON PURPOSE, and the emptiness is the record of a decision. The arrangement of an action bar is a composition and went to `components/patterns/action-bar.css`; the buttons in it are buttons and went to `components/button.css`; the page plate under it is the frame's and went to `components/base.css`. What could not go anywhere is the stone, because a pattern may carry no colour and the frame does not know this bar exists. So the exception was declared rather than forced, and this file is the exception.

## Anatomy

- `.cta-bar` - the bar's surface: `--bg-card-quiet`, a hairline along the top edge, and two rounded top corners, so a bar sitting at the foot of a scrolling column reads as a shelf the content slides under.
- `.flat` - the same bar where the page does not scroll. Border off, background off, corners off: on how-it-works the bar is the end of the page rather than a shelf over it, and a stone there would be a shadow with nothing behind it.

## When to use

You do not reach for this file. A person building an action bar takes the `action-bar` pattern, which says how the row is arranged and where it sticks; the surface arrives with it because `components/index.css` loads both.

The one decision this component leaves to a person is `.flat`, and the question is whether the bar has anything to hold itself against. A column that scrolls under it: keep the stone. A page that ends where the bar is: take it away.

The transaction list on the wallet screen is NOT this component, whatever the inventory says. It is `position`, and the row that claims otherwise is the oldest thing in this file's source list.

## Rule

The bar's material stays here and everything else leaves: an arrangement goes to the pattern, a control goes to its own component, and a page plate goes to the frame.

## Anti-rule

Never paint the bar's button from this file: a control in an action bar is `button`, and painting it here gives it a rule the button page has never heard of and a class map that cannot see it, because the markup is a bare element with no class of its own.

Seen: `ui-kit/docs/backlog.md` S11, which was exactly that for three stages, found by the pattern extraction in step 4 when a bare `<button>` made the class map unable to see the bar's contents, and closed on 2026-08-03 by moving eight rules out of this file.

## States

None, and it is declared: `ui-kit/_levels.py` STATIC carries the line written when the button left, "the bar answers no pointer because a bar is not a control". Everything a person presses in an action bar belongs to `button` and is photographed on its page.
