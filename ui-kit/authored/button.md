# button

## Sources

- `ui-kit/docs/inventory.md` - three rows file this component: Auth entries (L1), Provider buttons (L1), Primary CTA brass (L1). Two of the three claim 104 screens and the third 34.
- The 106 painted screens, every button of this family classified by all four axes and counted: **710 placements**, 704 under four names and 6 with no class of their own inside `.cta-bar`.
- The browser, at 360 and at 1440: the font step, the box, the border and the share of its container that each of the five placements actually takes. The size axis has no rule because of what those numbers say, not because nobody looked.
- Rules of use R1, the only rule that names this component.
- `voice/docs/microcopy.md` - the same-thing rows: Deposit against Add funds, Log in against Sign in. Both still open.
- `ui-kit/docs/backlog.md` S16, S11 and S24, which is where the four names being one anatomy was measured rather than asserted, and S25, which is the size axis this page could not give a rule.
- `components/button.css`, read for what each scope actually paints.

## Purpose

The control a person presses to do the thing the screen is for. It stands on all 106 painted
screens and it is written 710 times, under four names that are one anatomy: a graphite plate, a
hairline edge, a 10px corner, and the label in the body face. Two skins and no third. The quiet one
is every action that is not the point of its zone; the brass one is the action the zone exists for,
and there is exactly one of those per zone.

**This page specifies the four axes, not the five places.** The names are places, and a place is
not a design decision: asking "which of the five components do I want" is the wrong question and it
is the question the names invite. Pick four values, read the class off the row. Each axis carries
the rule for choosing its value, and where the product does not support a rule the page says so
rather than inventing one.

## Anatomy

- `.auth-btn` - The two entries in the header a logged-out visitor sees, Log in beside Sign up. 64 uses on 32 screens, and it is the smallest member of the family.
- `.state-btn` - The action inside a state block, where a screen has nothing to show yet: Browse events on an empty Active bets, Notify me of new events on an empty category. 66 uses on 40 screens.
- `.provider-btn` - A full-width row inside a sheet: Continue with Google, a payment method, a wallet. 444 uses on 105 screens, which makes it the one a person meets most.
- `.confirm-btn` - The brass action at the foot of a sheet, a panel or the mobile dock: Confirm bet, Add funds. 130 uses on 105 screens.
- `.primary` - Not a button, a modifier. It takes a quiet `.auth-btn` or `.state-btn` and makes it the brass one, and it is the only way this component becomes brass by choice rather than by place.
- `.ic` - The 18px box a leading mark stands in. It is the ICON AXIS made real, and until this page was rebuilt it was written up as a private detail of one place.
- `.prov-x`, `.prov-apple`, `.prov-google` - The three brand marks that stand in that box, filled with the current colour rather than stroked, because a logotype is not an icon.

## When to use

**Four axes. Pick the four values, then read the class off the row.** The five names are five
PLACES and they are a COLUMN here, not five sections: a place is where a combination happens to
stand, and it is the combination that is the decision.

| size | width | emphasis | icon | where it stands | uses | screens |
|---|---|---|---|---|---|---|
| 14 | full | quiet | **leading mark** | `.provider-btn` in the sign-in and outcome sheets | 322 | 105 |
| 14 | full | **brass** | none | `.confirm-btn` in a dialog, panel or sheet | 126 | 105 |
| 13 | full | quiet | none | `.provider-btn` everywhere else | 116 | 105 |
| 12 | fit | **brass** | none | `.auth-btn.primary` (32), `.state-btn.primary` (39) | 71 | 58 |
| 12 | fit | quiet | none | `.auth-btn` (32), `.state-btn` (25) | 57 | 47 |
| 14 | full | quiet | none | `.provider-btn` in a sheet, unmarked | 6 | 6 |
| 14 | **fit** | **brass** | none | `.confirm-btn` on `.bet-dock` | 4 | 4 |
| 13 | **shared** | **brass** | none | first child of `.cta-bar` | 3 | 3 |
| 13 | **shared** | quiet | none | second child of `.cta-bar` | 3 | 3 |
| 12 | **full** | **brass** | none | `.state-btn.primary` in `.resolved-panel` | 1 | 1 |
| 12 | **full** | quiet | none | `.state-btn` in `.resolved-panel` | 1 | 1 |

### The rule for each axis

**WIDTH: the container decides, and the rule holds with no exception in 710 placements.** Full when
the control is the only thing in its row; shared when the row is split evenly between peers; fit
when it stands in a row it does not own. That is measurable and it was measured: `.cta-bar` is
`display:flex` with `flex:1` on each child, so both children are shared; `.bet-dock` is a row that
also carries the odds meta and two side buttons, so `.confirm-btn` there is `width:auto` and fit;
`.resolved-panel` is one column, so the `.state-btn` inside it is `width:100%` and full, at the same
12px step it has everywhere else. **The two apparent exceptions are the proof**: both are a control
whose usual width is overridden by the shape of the container, and in both the container is what the
rule already asks about.

**EMPHASIS: one brass action per zone.** Counted over every dialog and every action bar in the
painted tree: **zones carrying more than one brass control, 0.** The brass one is the thing the
sheet was opened to do, and everything beside it is quiet, including the actions a person is more
likely to press. Cancel is quiet. Not now is quiet. The axis is expressed three different ways in
one family, and that is debt rather than design: a modifier on `.auth-btn` and `.state-btn`, the
NAME on `.confirm-btn`, and POSITION on the first child of `.cta-bar`. `ui-kit/docs/backlog.md`
**S24** carries the whole measurement and the condition for closing it.

**ICON: a mark only when the label names a third party.** 322 of the 710 carry one and every single
one is a brand mark on a row that reads Continue with Google, Continue with Apple or Continue with
X. The other 388 carry none, and that includes every other provider row in the same sheet: Connect a
USDC wallet, How it works, Contact support. **A mark here is identification, not decoration**, which
is why the box is 18px and the mark is filled rather than stroked. A button that wants an icon to
explain what it does is a button with the wrong label.

**SIZE: a fact without a rule, and it is written as one rather than dressed up.** The three steps
are 12, 13 and 14, and nothing in the product predicts which one a place gets. Measured in a
browser, at 1440 and at 360:

| place | font | container | the container's height | the share the button takes |
|---|---|---|---|---|
| `.auth-btn` | 12 | header row | 59 | 4 to 17 per cent |
| `.state-btn` | 12 | state block | 245 | 10 to 41 per cent |
| `.cta-bar button` | 13 | action bar | 70.5 | 44 to 49 per cent |
| `.provider-btn` | 13 or 14 | sheet body | 264 | 90 to 92 per cent |
| `.confirm-btn` | 14 | sheet body | 574 | 95 to 96 per cent |

Container height does not predict it: the state block is 245 tall and takes the smallest step while
the action bar is 70 and takes the middle one. The share of the container looks monotone in that
table and **two measured placements break it in both directions**: `.resolved-panel .state-btn` is
full width and stays at 12, and `.bet-dock .confirm-btn` is fit width and stays at 14. So the step
does not follow the container, the density or the width. It follows the NAME. The same class also
carries two steps at once: `.provider-btn` is 13 in its own rule and **14 inside the sign-in and
outcome sheets**, which is 322 of its 444 uses, so the size a person actually meets is not the size
the stylesheet declares first. `ui-kit/docs/backlog.md` **S25**. Until it is closed, take the step
from the row above and do not reason about it, because there is nothing there to reason with.

### The combinations the product does not have

Every cell not in the table above is one of two things, and a blank is neither. The last column is
where the verdict comes from, because a prohibition with no source is an opinion.

| combination | in the product | verdict | where the verdict comes from |
|---|---|---|---|
| icon + brass | 0 of 710 | **FORBIDDEN** | product counter. A brass control is the one action of its zone and its label already says what it is; a mark on it is a second claim on the same attention, and the one thing the mark means here (this is your Google account) is never the thing a zone was opened to do |
| icon + fit width | 0 of 710 | **FORBIDDEN** | product counter, plus the width rule. A marked row is an identity to be picked out of a list, a list is one column, and one column means full width. A marked control at fit width would be a brand mark used as decoration, which the icon rule already refuses |
| full width in the header | 0 of 710 | **FORBIDDEN** | the width rule. The header row is shared with the logo, the balance and the utility icons, so nothing in it owns its row. This is the width rule applied, not a separate ban |
| disabled anywhere but `.confirm-btn` | 1 disabled control in each tree, and it is a `.confirm-btn` | **UNCLOSED ZONE** | `ui-kit/docs/backlog.md` **S26**. Not forbidden and not decided: the product simply has never disabled anything else, so there is no answer to what a disabled quiet button looks like. `--opacity-disabled` would apply and nobody has looked at it on a 1px edge |
| icon + quiet + fit, in a sheet | 0 of 710 | **UNCLOSED ZONE** | `ui-kit/docs/backlog.md` **S26**. The two rules above each rule out half of it and neither rules out the whole, so it is left named rather than settled |

## Rule

Take the four values, and let the scope give the control its skin: the same four declarations paint
all four names, so a button that looks wrong is almost always a button in the wrong scope rather
than a button that needs a new rule.

Two labels in this family are still two names for one thing and it is a known defect, not a
decision: the funding action is *Deposit* on My Profile and in the wallet, and *Add funds* in the
header and the dialog; the auth entry is *Log in* in the header and *Sign in* in the dialog. Both
are open in `voice/docs/microcopy.md` under same-thing. Copy the label from the row there rather
than from the nearest screen.

## Anti-rule

Never dress an outcome as an action: a YES or a NO is `yesno`, tinted green and red because those
two colours mean an outcome in this product and nothing else, and a quiet chip that filters, sorts
or loads more is `filters`, `catnav` or `loadmore`, which are one graphite chip family with a
lighter press than this one.

Seen: `ui-kit/docs/backlog.md` S16, where five names of one control were measured, and
`components/account.css`, which painted a button of this family for three stages because the
component that owned the BAR was the one holding the pen.

## States

Five galleries, and the count is not a coincidence: **one base set plus one named difference each**.
The eight that were here before were eight PLACES, and three of them were photographed only to show
that they look the same as another three. What decides a gallery now is a difference measured across
all four states in both themes, so a picture on this page is a picture of a decision.

- `button.auth-btn @button-family` - **The family's answer, and it covers three placements.** `.state-btn` is the most used of them, 66 uses on 40 screens against `.auth-btn`'s 64 on 32 and 3 in an action bar; the camera points at `.auth-btn` because the specimen puts the header pair first, and the merge is the proof that which one it points at does not matter. The ground steps one stone darker under the pointer, the edge goes brass at 45 per cent, and the label lifts to the strong ink; held down it settles onto the pressed stone. The focus ring is the system's one ring, brass, 2px, offset 2px.
- `button.auth-btn.primary @button-family` - **The difference is the modifier**, and it covers `.state-btn.primary` too. Hover takes the lit brass to both stops so the whole face comes up and adds a soft glow under it; the press turns the gradient over to 315 degrees so the light falls to the bottom right, which is what a plate pushed in looks like. The glow goes with it, because the glow is the lift. The 1px edge stays and turns brass, which is what separates this from the brass below it.
- `button.provider-btn @dialog.signin-dialog` - **The difference is one pixel of lift.** Everything else about it is the family's answer, which is why the instrument used to merge it away: `transform` was not one of the five values a face was made of, so a control that moves was read as a control that does not. A row that wide needs a second signal that it is a target at all.
- `button.confirm-btn @dialog.app-dialog` - **The difference is that there is no edge**, and an edge on a lit plate the width of a sheet reads as a seam. This is also the one control the product ever disables, once in each tree, and a disabled one neither lights up nor presses.
- `button @.cta-bar` - **The difference is the ink.** The first child of an action bar is brass by position rather than by class, and its label stays dark on the lit plate under the pointer, which the family's quiet hover would otherwise take to white. The second child of the same bar carries no difference and is in the base set above.
