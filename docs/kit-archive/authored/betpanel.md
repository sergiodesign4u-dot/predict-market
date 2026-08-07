# betpanel

## Sources

- `ui-kit/docs/inventory.md` L99 - "Bet panel (`.bet-panel`: `.bp-dir` filled-selected side, amount, quick chips, payout line, Confirm)", filed L3, states "intent / insufficient / reconcile / processing / error / resolved".
- `ui-kit/docs/inventory.md` L100 - "Bet dock (mobile sticky, `.bet-dock`)", state "collapsed -> expand to confirm", 8.
- R3 in `ui-kit/docs/architecture.md` - one bet control, and the WIDTH decides which. 11 screens with a panel, 8 with a dock, 8 with both in the markup and never both on screen; the swap is in `components/betpanel.css` itself at the 760px breakpoint.
- R7 in `ui-kit/docs/architecture.md` - it never stands on a screen with a grid of cards, and the auth axis does not move that: the panel stands on the logged-out detail as well, 3 of the 11, because the account is asked for at submit and not at the door.
- `voice/docs/microcopy.md` L333 to L338 and L1008 - the panel's copy: the heading *Place your bet*, the button *Confirm bet*, the insufficient-balance fallback *Bet $3.00 instead*, the S5 label *Confirm at new price (41%)*, and the reconciliation verdict that these are three different moments rather than one label written three ways.
- `ia/docs/sitemap.md` L399 - the panel's own state list from the IA: intent (logged out, no auth yet), S5-reconcile (the price moved during the gate and the person must re-confirm), error, insufficient-balance, event-closed.
- `ui-kit/docs/backlog.md` S12 - the panel is one of the three components with a hand-typed `top:120px`, and the row says why no token can hold it.
- The 11 painted screens.

## Purpose

Where money is actually committed. A side, an amount, what it would return, and one button that does it. On a wide screen it is a sticky panel beside the event; at 360 it is a dock at the foot that expands into a sheet.

Everything in this product routes here and nothing else commits. A card's YES / NO chooses a side and opens the event; the odds bar reports; the market panel explains. This is the only component where a number a person typed turns into a stake, which is why it carries more states than anything else in the system and why every one of them is about doubt: not enough funds, the price moved, it did not register, the event closed while you were reading.

## Anatomy

- `.bet-panel` - the sticky panel, above 760px.
- `.bet-dock` - the same control at 360, collapsed at the foot of the screen, and `.dock-meta` the line it shows while collapsed.
- `.bet-sheet` - what the dock expands into. It is a `dialog`, so the sheet material is not this component's.
- `.sheet-grab` - the grab handle at the top of that sheet.
- `.bp-head`, `.bp-inner` - the panel's head and body.
- `.bp-dir` - the side chooser, and `.bp-side` one side of it. The selected side is filled; the other is not, so the panel always says out loud which way the bet goes.
- `.bp-pct` - the side's current probability, inside the control that chooses it.
- `.bp-selected`, `.bp-sel-name`, `.bp-change` - on a multi-outcome event: which option is being backed, and the way to change it without leaving the panel.
- `.bp-amount-row`, `.bp-amount-lbl` - the amount. The field itself is `input`.
- `.bp-cash` - what is available, next to what is being spent.
- `.line`, `.total` - the payout line: the arithmetic, then the figure it produces.
- `.bp-hint` - the sentence under the total. It is where principle 1 lands in this component: the number never stands alone.

## When to use

On an Event Detail screen, once, and never anywhere else. R7 is the rule and it is measured rather than asserted: 23 screens carry a grid of cards and none of them has an amount field or a Confirm on it.

At most one of the panel and the dock is visible, and the width decides. Both are in the markup on 8 screens and that is correct: the swap is a media query in the component, not a choice a screen makes.

It stands on the logged-out detail too. A person may build a whole bet before the product asks who they are, because asking at the door costs more people than asking at the till, and the sign-in that arrives is a `dialog` over this panel rather than a redirect away from it.

## Rule

Every state of it says what happened to the money: no funds were taken, the price is now this, you can bet this much instead. A panel state that reports a failure without saying where the stake stands is the one thing this component may never ship.

## Anti-rule

Never draw the side chooser from `yesno`: that pair is a routing control that opens an event with a side pre-selected, and `.bp-side` is a chooser inside the thing that commits. They look nearly identical and mean opposite things, and the difference is whether pressing it costs anything.

Predicted: and the downgrade from Seen is deliberate. R7 in `ui-kit/docs/architecture.md` exists to keep exactly these two apart and `wireframes/_conventions.md` S3 states it from the markup side, but a rule of use in this repo is defined as "what never happened once although it easily could have", so citing one as evidence would be reading a prohibition as an incident. It has not happened; both documents say it is the thing most likely to.

## States

- The two sides are no longer captured here. They went to `components/yesno.css` on 2026-08-06 as the outcome atom's TRADER face: neutral at rest because a chooser states the CHOICE and not the market, which is this file's own argument and travelled with the rules. Their gallery is on the yesno page. What this file still owns about them is `flex:1`, how two sides divide a row, and the odds figure inside each one, because a percentage is this panel's datum the way an event photograph is a card's content.
- `button.sheet-grab @dialog.bet-sheet` - The grab at the top of the expanded sheet. It is a real control with all four faces rather than a decorative bar, because at 360 it is how the sheet is dismissed by hand.
- `a.bp-change @.bet-panel` - *Change*, on a multi-outcome bet: the way back to the option list without losing the amount. Underlined at rest, because it is a small link doing a large job next to a filled button.
