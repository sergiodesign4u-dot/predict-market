# button

## Sources

- `ui-kit/docs/inventory.md` - three rows file this component: Auth entries (L1), Provider buttons (L1), Primary CTA brass (L1). Two of the three claim 104 screens and the third 34.
- The 105 painted screens, counted: `.provider-btn` 444 uses on 105, `.confirm-btn` 130 on 105, `.state-btn` 66 on 40, `.auth-btn` 64 on 32. Six further classes were deleted on 2026-08-03 for standing on none.
- Rules of use R1, the only rule that names this component.
- `voice/docs/microcopy.md` - the same-thing rows: Deposit against Add funds, Log in against Sign in. Both still open.
- `ui-kit/docs/backlog.md` S16 and S11, which is where the four names being one anatomy was measured rather than asserted.
- `components/button.css`, read for what each scope actually paints.

## Purpose

The control a person presses to do the thing the screen is for. It stands on all 105 painted
screens and it is written 704 times, under four names that are one anatomy: a graphite plate, a
hairline edge, a 10px corner, and the label in the body face. Two skins and no third. The quiet one
is every action that is not the point of its zone; the brass one is the action the zone exists for,
and there is exactly one of those per zone.

The four names are not four components. They are the four PLACES the same control stands in, and
each carries the geometry its place needs: a header entry is small and inline, an action inside a
state block has room to breathe, and anything inside a sheet is the full width of the sheet because
a sheet has one column.

## Anatomy

- `.auth-btn` - The two entries in the header a logged-out visitor sees, Log in beside Sign up. 64 uses on 32 screens, and it is the smallest member of the family: 12px label, 8px of padding.
- `.state-btn` - The action inside a state block, where a screen has nothing to show yet: Browse events on an empty Active bets, Notify me of new events on an empty category. 66 uses on 40 screens.
- `.provider-btn` - A full-width row inside a sheet, carrying a mark and a label: Continue with Google, a payment method, a wallet. 444 uses on 105 screens, which makes it the one a person meets most.
- `.confirm-btn` - The brass action at the foot of a sheet, a panel or the mobile dock: Confirm bet, Add funds. 130 uses on 105 screens.
- `.primary` - Not a button, a modifier. It takes a quiet `.auth-btn` or `.state-btn` and makes it the brass one, and it is the only way this component becomes brass by choice rather than by place.
- `.prov-x` - The brand mark of X inside a provider row, filled with the current colour rather than stroked, because a logotype is not an icon.
- `.prov-apple` - The same for Apple.

## When to use

**There is one button here and it has three axes. Pick the three, then read off the name.** The
five names are five PLACES, and a place is not a design decision: `.auth-btn` in the header,
`.state-btn` in a state block, `.provider-btn` and `.confirm-btn` inside a sheet or a panel, and an
unnamed `button` inside `.cta-bar`. Asking "which of the five components do I want" is the wrong
question and it is the question the names invite, so the matrix answers the right one:

| | **size** | **width** | **emphasis** |
|---|---|---|---|
| | 12 / 13 / 14px over four paddings | shrink-to-fit, or the full width of what holds it | brass, or quiet |
| `.auth-btn` | 12, padding 8-8 | fit | `.primary` for brass |
| `.state-btn` | 12, padding 8-12 | fit, and **full inside `.resolved-panel`** | `.primary` for brass |
| `.provider-btn` | 13, padding 12 | **full** | quiet only |
| `.cta-bar button` | 13, padding 12 | shared, `flex:1` from the pattern | **POSITION: the first child is brass** |
| `.confirm-btn` | 14, padding 12 (16 in `.bet-sheet`) | full, and **fit on `.bet-dock`** | **the name itself is the emphasis** |

**Read the bold cells as the debt they are, not as the design.** Emphasis is expressed three
different ways in one family - a modifier, a position, and a name - and the width and size of two of
the five are decided by the scope they stand in rather than by the control. `ui-kit/docs/backlog.md`
**S24** carries the whole measurement and the condition for closing it. Until then: **take the row
whose three cells match, and use the class in the left column.** A control that fits none of the
rows is probably not a button of this family, and the anti-rule below is the commonest way that
goes wrong.

Then decide brass or quiet, and that decision is not free: **one brass action per zone**, which is
the constraint quoted below this section. In practice the brass one is the thing the sheet was
opened to do (Add funds in the deposit dialog, Confirm bet in the panel) and everything beside it
is quiet, including the actions a person is more likely to press. Cancel is quiet. Not now is quiet.

Two labels in this family are still two names for one thing and it is a known defect, not a
decision: the funding action is *Deposit* on My Profile and in the wallet, and *Add funds* in the
header and the dialog; the auth entry is *Log in* in the header and *Sign in* in the dialog. Both
are open in `voice/docs/microcopy.md` under same-thing. Copy the label from the row there rather
than from the nearest screen.

## Rule

Take the name of the PLACE, and let the scope give it its skin: the same four declarations paint
all four names, so a button that looks wrong is almost always a button in the wrong scope rather
than a button that needs a new rule.

## Anti-rule

Never dress an outcome as an action: a YES or a NO is `yesno`, tinted green and red because those
two colours mean an outcome in this product and nothing else, and a quiet chip that filters, sorts
or loads more is `filters`, `catnav` or `loadmore`, which are one graphite chip family with a
lighter press than this one.

Seen: `ui-kit/docs/backlog.md` S16, where five names of one control were measured, and
`components/account.css`, which painted a button of this family for three stages because the
component that owned the BAR was the one holding the pen.

## States

- `button.auth-btn @button-family` - The quiet header entry. The ground steps one stone darker under the pointer, the edge goes brass at 45 per cent, and the label lifts to the strong ink; held down it settles onto the pressed stone. The focus ring is the system's one ring, brass, 2px, offset 2px.
- `button.state-btn @button-family` - The same control with more padding, in the middle of an empty screen. Identical answers, which is the point: two names, one behaviour.
- `button.auth-btn.primary @button-family` - Sign up, the brass one. Hover takes the lit brass to both stops so the whole face comes up and adds a soft glow under it; the press turns the gradient over to 315 degrees so the light falls to the bottom right, which is what a plate pushed in looks like. The glow goes with it, because the glow is the lift.
- `button.state-btn.primary @button-family` - Browse events, the brass action of a state block. Same three-step.
- `button.provider-btn @dialog.signin-dialog` - A provider row inside a sheet. Quiet, full width, and the only member that also lifts one pixel on hover, because a row that wide needs a second signal that it is a target at all.
- `button.confirm-btn @dialog.app-dialog` - Add funds, brass, the width of the sheet, no edge at all: an edge on a lit plate that wide reads as a seam. This is also the one control the product ever disables, and a disabled one neither lights up nor presses.
- `button @.cta-bar` - The first child of an action bar, brass by position rather than by class. Its ink stays dark on the lit plate under the pointer, which the family's quiet hover would otherwise take to white.
- `button @.cta-bar (2)` - The second child of the same bar, quiet, and the answer is the family's.
