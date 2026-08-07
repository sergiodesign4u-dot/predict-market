# action-bar

## Sources

- `ui-kit/docs/inventory.md` L161 - "CTA bar (`.cta-bar`: Add funds + Open Wallet / Withdraw)", filed L2, on how-it-works, my-profile and wallet.
- **3 painted screens**, which is the pattern threshold exactly and not one more. This is the only pattern in the system that clears the bar by a margin of one, and it is said rather than rounded up: if any of the three loses its bar, this stops being a pattern.
- `ui-kit/docs/architecture.md`, "What was measured and deliberately not written down" - `.cta-bar` stands on three screens and on none of the 17 overlays, and that was deliberately NOT made a rule of use: "Three is the pattern threshold, not the prohibition threshold."
- `ui-kit/docs/backlog.md` S11, closed 2026-08-03 - eight rules that painted this bar's BUTTON moved to `components/button.css`, and the one line that was arrangement rather than paint came here.
- `ui-kit/_levels.py` STATIC, the `account` entry - "the bar answers no pointer because a bar is not a control", written the day the button left.

## Purpose

One or two actions held at the foot of a column, sticky by default and flat where the page has no scroll to hold them against. It is the arrangement and nothing else: how the actions share the row, where the row sits, and what happens when there is only one of them.

## Parts

- `account` - the bar's surface: the stone, the hairline along the top edge and the two rounded corners, plus the `.flat` variant that takes all three away. It is what the bar is MADE of; this file is where it stands.
- `button` - the actions. Each is an `<a>` at `flex:1` holding a button at `width:100%`, so two actions split the row evenly and one fills it without either button learning a width of its own.

## When to use

When a screen has one action that is the reason a person came to it, and the content above is long enough that the action would otherwise scroll away. The wallet, the profile and How It Works are the three, and each has exactly one such action.

Never twice on a screen. A sticky bar is the loudest thing on a phone, and a screen with two has told a person nothing about which one to press.

By hand: when the action is not the reason the screen exists. Two actions in a row at the foot of a card, a pair of links under a form, an inline confirm inside a panel - all of those are a flex row and two buttons, written where they stand. Reaching for this pattern makes them sticky, which is a claim about their importance that the screen has not earned. The test is whether the action should follow a person down the page; if the answer needs thought, it should not.

## Rule

The bar holds the actions and the buttons stay themselves: the row decides the split, and no button in it gains a width, a radius or a colour it would not have anywhere else.

## Anti-rule

Never use it as the bet control. A sticky bar at the foot of a phone that commits money is `betpanel`'s dock, which the width swaps against a panel at 760 and which R3 counts at most one of; this bar is a way ONWARD from a screen, not a way to spend on it. They look identical at 360 and the difference is whether pressing costs anything.

Predicted: it has not happened. The two have never met on a screen, and R3 and R7 are why - a bet control does not stand on a list, and this bar's three screens are a wallet, a profile and a document. Recorded because the shapes are the same and the screens are one product decision apart.

## Arrangement

Sticky to the foot of the column, above the bottom nav, with the actions in source order and no reordering at any width. The `.flat` variant is the same bar where the page does not scroll, and choosing between them is the one decision this pattern leaves to a person: a column that scrolls under the bar keeps the stone, a page that ends where the bar is takes it away.

Nothing here has a state. What answers a pointer is the `button` inside it, photographed on that component's page, and the `account` surface behind it is declared static because a bar is not a control.
