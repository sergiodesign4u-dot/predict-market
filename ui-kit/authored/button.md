# button

## Sources

- `ui-kit/docs/inventory.md` - three rows file this component: Auth entries (L1), Provider buttons (L1), Primary CTA brass (L1). Two of the three claim 104 screens and the third 34.
- The 106 painted screens, every button of this family read and grouped by what the stylesheet decides about it: **710 placements in 16 forms**, 704 under four names and 6 with no class of their own inside `.cta-bar`. Counted by `ui-kit/_worn.py`, which is also the gate: a form worn and not staged fails the build, and so does a form staged and not worn.
- `ui-kit/specimens/button-matrix.html` and `ui-kit/specimens/button-matrix-dock.html`, where all 16 stand live, each in the smallest wrapper that paints it. Two documents because `components/betpanel.css` hides `.bet-dock` at min-width:760 and `.bet-panel` below it, so no single width can show both.
- The browser, at 360 and at 1440, on those two specimens: the padding, the font step, the weight and the border of every form. The size axis has no rule because of what those numbers say, not because nobody looked.
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

**This page shows every form and not every name.** The names are places, and a place is not a design
decision: asking "which of the four components do I want" is the wrong question and it is the
question the names invite. What a person actually chooses is a size, a padding, a width, an
emphasis and whether there is a mark, and the same name answers differently in four different
scopes. So the page opens with all sixteen forms standing live, reads the class off the row, and
where the product does not support a rule it says so rather than inventing one.

## Anatomy

- `.auth-btn` - The two entries in the header a logged-out visitor sees, Log in beside Sign up. 64 uses on 32 screens, and it is the smallest member of the family.
- `.state-btn` - The action inside a state block, where a screen has nothing to show yet: Browse events on an empty Active bets, Notify me of new events on an empty category. 66 uses on 40 screens.
- `.provider-btn` - A full-width row inside a sheet: Continue with Google, a payment method, a wallet. 444 uses on 105 screens, which makes it the one a person meets most.
- `.confirm-btn` - The brass action at the foot of a sheet, a panel or the mobile dock: Confirm bet, Add funds. 130 uses on 105 screens.
- `.primary` - Not a button, a modifier. It takes a quiet `.auth-btn` or `.state-btn` and makes it the brass one, and it is the only way this component becomes brass by choice rather than by place.
- `.ic` - The 18px box a leading mark stands in. It is the ICON AXIS made real, and until this page was rebuilt it was written up as a private detail of one place.
- `.prov-x`, `.prov-apple`, `.prov-google` - The three brand marks that stand in that box, filled with the current colour rather than stroked, because a logotype is not an icon.

## When to use

**Sixteen forms, and the list is counted rather than argued.** A form is what the stylesheet decides
about one control: the family class it carries, plus `.primary` or not, times the scoping classes
above it that `components/button.css` actually reads. Two controls that resolve to the same pair are
one form however many screens carry them. `ui-kit/_worn.py` reads that pair out of every button in
`ui-visual/` and out of the two matrix specimens and fails the build when either side has a row the
other does not, so this table cannot drift from the product in either direction.

Every one of these is staged, live, in `ui-kit/specimens/button-matrix.html` and its dock companion.
Padding, size and weight were measured in a browser on those specimens; width is what the
declaration says, because a control's rendered width is half its container's decision and the
declaration is not.

**Sixteen combinations, twelve controls, and the gap between those two numbers is worth the
paragraph.** Every form was compared field for field against the same markup with no scope above it,
in a container of the same width, over thirteen properties: background, gradient, edge, edge width,
ink, radius, padding, size, weight, justification, alignment, gap and min-height. **Twelve of the
sixteen came out identical**, which is to say the scope they ship in decides nothing about them.
`.confirm-btn` inside `dialog.app-dialog.outcome-dialog` differs from the bare one in nothing at all,
not even the width. So the matrix stages the CONTROL and not the combination: six rows stand on the
bare canvas, four keep their scope because the scope is what that row is about, and the six
combinations that collapse are listed with what was compared in `ui-kit/_worn.py` `SAME`, held by
gate 38 in both directions.

**A sentence outlived its fact by a day, and it cost this page its rhythm.** The first matrix put six
of these inside plates because `ui-kit/specimens.map.json` said `.provider-btn` and `.confirm-btn`
have no ground outside a sheet and would render in the user agent's grey. True until 2026-08-03, when
the merge in `components/button.css` put `background:var(--bg-control)` into the rule the whole
family shares. The note was not re-read after the merge that falsified it.

| form | scope | padding | size | weight | width | uses | screens |
|---|---|---|---|---|---|---|---|
| `.provider-btn` | `dialog.app-dialog.signin-dialog` | 12 | **14** | 600 | 100% | 324 | 105 |
| `.provider-btn` | `dialog.app-dialog` | 12 | 13 | 400 | 100% | 113 | 105 |
| `.confirm-btn` | `dialog.app-dialog` | 12 | 14 | 700 | 100% | 110 | 105 |
| `.state-btn.primary` | none | **8 12** | 12 | 700 | content | 39 | 39 |
| `.auth-btn` | none | **8** | 12 | 400 | content | 32 | 32 |
| `.auth-btn.primary` | none | **8** | 12 | 700 | content | 32 | 32 |
| `.state-btn` | none | **8 12** | 12 | 400 | content | 25 | 25 |
| `.confirm-btn` | `.bet-panel` | 12 | 14 | 700 | 100% | 8 | 8 |
| bare `button` | `.cta-bar` | 12 | 13 | 700 first, 600 second | `flex:1`, min-height 44 | 6 | 3 |
| `.confirm-btn` | `.bet-dock` | 12 | 14 | 700 | **auto** | 4 | 4 |
| `.confirm-btn` | `dialog.app-dialog.bet-sheet` | **16** | 14 | 700 | 100% | 4 | 4 |
| `.confirm-btn` | `dialog.app-dialog.outcome-dialog` | 12 | 14 | 700 | 100% | 4 | 4 |
| `.provider-btn` | `dialog.app-dialog.outcome-dialog` | 12 | 14 | **700** | 100% | 4 | 4 |
| `.provider-btn` | `.bet-panel` | 12 | 13 | 600 | 100% | 3 | 3 |
| `.state-btn.primary` | `.bet-panel.resolved-panel` | 8 12 | 12 | 700 | **100%** | 1 | 1 |
| `.state-btn` | `.bet-panel.resolved-panel` | 8 12 | 12 | 400 | **100%** | 1 | 1 |

710 placements, and the four smallest rows are the ones worth reading. **The `.bet-sheet` row is the
only padding of 16 in the family**, and no measurement of the rendered tree can reach it: the sheet
ships as a `<dialog>` with no `open` attribute, so a browser scores it at zero width and walks past.
It is staged open in the dock specimen and it is in this table because `_worn.py` reads markup.
**The two `.resolved-panel` rows are the only place a state button is full width**, they stand on one
screen, and a matrix assembled by reading the stylesheet and the screens by eye had missed both:
`_worn.py` found them on its first run.

### What the axes say, and where one of them has nothing to say

**WIDTH: the container decides, and the declaration says which way.** `.provider-btn` and
`.confirm-btn` declare `width:100%`, `.auth-btn` and `.state-btn` declare nothing and are as wide as
their label, and the three exceptions are all a container overriding one of those:
`.resolved-panel .state-btn` takes 100%, `.bet-dock .confirm-btn` takes `auto`, and
`.cta-bar > button` takes `flex:1` and shares the row with its neighbour. Each exception is a
container asserting the shape of its own row, which is the rule rather than a break in it.

**EMPHASIS: one brass action per zone.** Counted over every dialog and every action bar in the
painted tree: **zones carrying more than one brass control, 0.** The brass one is the thing the sheet
was opened to do, and everything beside it is quiet, including the actions a person is more likely to
press. Cancel is quiet. Not now is quiet. The axis is expressed three different ways in one family,
and that is debt rather than design: a modifier on `.auth-btn` and `.state-btn`, the NAME on
`.confirm-btn`, and POSITION on the first child of `.cta-bar`. `ui-kit/docs/backlog.md` **S24**
carries the whole measurement and the condition for closing it.

**MARK: only where the label names a third party.** Three controls in the family carry one and all
three are in the sign-in sheet: Continue with Google, Continue with Apple, Continue with X. Every
other provider row in the same sheet carries none, including Connect a USDC wallet, How it works and
Contact support. **A mark here is identification, not decoration**, which is why the box is 18px and
the mark is filled rather than stroked. A button that wants an icon to explain what it does is a
button with the wrong label.

**SIZE: a fact without a rule, and it is written as one rather than dressed up.** Three steps, 12, 13
and 14, and nothing in the product predicts which one a form gets. Measured in a browser at 1440 and
at 360: container height does not predict it, the state block is 245 tall and takes the smallest step
while the action bar is 70 and takes the middle one; the share of the container does not predict it
either, because `.resolved-panel .state-btn` is full width at 12 and `.bet-dock .confirm-btn` is
content width at 14. The step follows the NAME, and one name carries two steps at once:
`.provider-btn` is 13 in its own rule and **14 inside the sign-in and outcome sheets**, which is 328
of its 444 uses, so the size a person actually meets is not the size the stylesheet declares first.
`ui-kit/docs/backlog.md` **S25**. Until it is closed, take the step from the row above and do not
reason about it, because there is nothing there to reason with.

### The combinations the product does not have

Every pair not in the table above is one of two things, and a blank is neither. The last column is
where the verdict comes from, because a prohibition with no source is an opinion.

| combination | in the product | verdict | where the verdict comes from |
|---|---|---|---|
| a mark on a brass control | 0 of 710 | **FORBIDDEN** | product counter. A brass control is the one action of its zone and its label already says what it is; a mark on it is a second claim on the same attention, and the one thing the mark means here (this is your Google account) is never the thing a zone was opened to do |
| a mark on a content-width control | 0 of 710 | **FORBIDDEN** | product counter, plus the width rule. A marked row is an identity to be picked out of a list, a list is one column, and one column means 100%. A marked control at content width would be a brand mark used as decoration, which the mark rule already refuses |
| a full-width control in the header | 0 of 710 | **FORBIDDEN** | the width rule. The header row is shared with the logo, the balance and the utility icons, so nothing in it owns its row. This is the width rule applied, not a separate ban |
| disabled anywhere but `.confirm-btn` | 1 disabled control in each tree, and it is a `.confirm-btn` | **UNCLOSED ZONE** | `ui-kit/docs/backlog.md` **S26**. Not forbidden and not decided: the product simply has never disabled anything else, so there is no answer to what a disabled quiet button looks like. `--opacity-disabled` would apply and nobody has looked at it on a 1px edge |
| a mark on a quiet content-width control in a sheet | 0 of 710 | **UNCLOSED ZONE** | `ui-kit/docs/backlog.md` **S26**. The two rules above each rule out half of it and neither rules out the whole, so it is left named rather than settled |

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

**A `<button>` is a tag and not a role, and reading the tag as the answer is how this page came to
show a tab strip.** The census below sorts every button-shaped control in the product by what it
actually IS: an **action** is a press with nothing carried between presses, a **selector** carries a
value and its selected state is the whole point, **navigation** goes somewhere. Only the actions
stand here. The split is not a filing preference and the selector is what makes it load-bearing: a
chip's subject is its GROUP and its SELECTED one, so a single chip lifted out of its rail is the
half that carries no information, and a reader learns a padding and nothing about the only thing the
control does. Two of them stood live on this page before this pass, which was worse than listing
them. The counts are in the census and not repeated here, because a number written twice drifts.

Seen: `ui-kit/docs/backlog.md` S16, where five names of one control were measured, and
`components/account.css`, which painted a button of this family for three stages because the
component that owned the BAR was the one holding the pen.

## States

**Five faces over sixteen forms, and the gap between those two numbers is the point of this page.**
Sixteen is how many different controls the product paints; five is how many different ways they
ANSWER a pointer. A form is a size, a padding and a width, and a face is what moves when you touch
it, so a page that had one gallery per form would be saying eleven times that nothing new happens.
What decides a gallery is a difference measured across all four states in both themes, and the
grouping is computed rather than chosen: 25 occurrences were read and 20 of them are somebody else's
answer.

- `button.auth-btn @button-matrix` - **The family's answer, and it covers eleven of the sixteen forms.** Everything quiet answers this way whatever its size: `.state-btn` at 12, `.provider-btn` at 13 in a deposit sheet and at 14 in an outcome one, the second child of an action bar at 13, the full-width pair in the resolved panel. The ground steps one stone darker under the pointer, the edge goes brass at 45 per cent, and the label lifts to the strong ink; held down it settles onto the pressed stone. The focus ring is the system's one ring, brass, 2px, offset 2px. That eleven forms share one answer is the argument for the matrix above: the SIZES are the decision a person makes and the STATE is not.
- `button.auth-btn.primary @button-matrix` - **The difference is the modifier**, and it covers `.state-btn.primary` in all three of its places. Hover takes the lit brass to both stops so the whole face comes up and adds a soft glow under it; the press turns the gradient over to 315 degrees so the light falls to the bottom right, which is what a plate pushed in looks like. The glow goes with it, because the glow is the lift. The 1px edge stays and turns brass, which is what separates this from the brass below it.
- `button.provider-btn @dialog.signin-dialog` - **The difference is one pixel of lift**, and it is the only form in the family that moves. Everything else about it is the family's answer, which is why the instrument merged it away twice: first because `transform` was not one of the values a face is made of, and then again on 2026-08-04 because the face was keyed without its SCOPE, so the first provider row in a document was measured and the other three were skipped as copies of it. Staging four scopes in one specimen is what made that visible. A row that wide needs a second signal that it is a target at all.
- `button.confirm-btn @button-matrix` - **The difference is that there is no edge**, and an edge on a lit plate the width of a sheet reads as a seam. It covers every brass sheet action in the product, seven combinations including the two the wide matrix cannot show, and it is measured on the BARE canvas because none of those scopes changes it: `dialog.app-dialog`, `.outcome-dialog` and `.bet-panel` each give it a width and not one declaration more. This is also the one control the product ever disables, once in each tree, and a disabled one neither lights up nor presses.
- `button @.cta-bar` - **The difference is the ink.** The first child of an action bar is brass by position rather than by class, and its label stays dark on the lit plate under the pointer, which the family's quiet hover would otherwise take to white. The second child of the same bar carries no difference and is in the base set above.
