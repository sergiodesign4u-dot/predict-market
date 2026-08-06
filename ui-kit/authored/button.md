# button

## Sources

- The 105 painted screens and the 104 grey ones, every button of this component read and grouped by what the stylesheet decides about it: **710 placements in 10 forms**, all of them wearing `.btn`. Counted by `ui-kit/_worn.py`, which is also the gate: a form worn and not staged fails the build, and so does a form staged and not worn.
- `ui-kit/specimens/button-matrix.html`, where all 10 stand live on one ground with no plate under any of them. ONE document, where there used to be two: `components/betpanel.css` hides `.bet-dock` above 760 and `.bet-panel` under it, so a form defined by its PLACE could not be shown beside the others. A form is a set of classes now.
- The browser, over all 105 painted screens at 1440 and at 360, every button-shaped control: **9,648 readings**. That is where the two emphases, the three sizes and every value below come from, and it is why the migration below is a measurement rather than a preference.
- `ui-kit/docs/backlog.md` S24, which measured the five names as one anatomy and set the closing condition this page has now met, and S25, the size axis that had no rule.
- `voice/docs/microcopy.md` - the same-thing rows: Deposit against Add funds, Log in against Sign in. Both still open.
- `components/button.css`, which is now 20 declarations where it was 30 rules.

## Purpose

The control a person presses to do the thing the screen is for. It stands on all 105 painted screens
and is written 710 times, under **one name with three modifiers**. A graphite plate, a hairline edge,
a 10px corner and the label in the body face; two skins and no third. The quiet one is every action
that is not the point of its zone, the brass one is the action the zone exists for, and there is
exactly one of those per zone.

**It was five names until 2026-08-05.** `.auth-btn`, `.state-btn`, `.provider-btn`, `.confirm-btn`
and a bare `<button>` inside an action bar were one component under five names, and the proof is
what they did not agree on: `.provider-btn` alone measured seven faces, and its four scopes agreed on
padding, radius, ground and edge while disagreeing on size, weight, justification and gap. Nothing in
the product predicted which a place got. The names are gone, both trees moved in the same change, and
the vocabulary is what a person choosing a button actually chooses.

## Anatomy

- `.btn` - The marker, and it carries the anatomy every button has: the corner, the body face, the box sizing, the transition, the centring, and a 1px band that is transparent until a skin gives it a colour. Nothing is a button in this system without it, and every selector in `components/button.css` requires it.
- `.btn-secondary` - The quiet skin, and it is three colours and nothing else: `--bg-control`, `--border-hairline` on the band the base already declared, `--text-primary`, semibold. 505 of the 710 placements.
- `.btn-primary` - The brass skin: the 135deg action gradient, `--text-on-brass`, bold, and the band left transparent, which `background-clip:border-box` paints the gradient straight through. 205 placements. One per zone.
- `.btn-sm` - 8/12 padding at 12px, and 36px tall on every one of its 194 single-line readings. The header's two entries and the action inside a state block: 130 placements.
- `.btn-md` - 12 padding at 14px, 47px tall on all 1,028 of its single-line readings. The row inside a sheet, the panel and the action bar: 576 placements, and by far the most of the product.
- `.btn-lg` - 16 padding at 14px, 55px tall. The mobile bet sheet's Confirm, 4 placements, and it exists as a size because it used to exist as a scope override nobody could ask for.
- `.btn-block` - The control owns its row. It replaces three separate scope rules that each put a width back, and it says so where the person placing the control can read it.
- `.prov-x`, `.prov-apple` - Two brand marks, filled with the current colour rather than stroked, because a logotype is not an icon. `.prov-google` carries its own brand colours in the markup and correctly has no rule.

## When to use

**Ten forms, and the list is counted rather than argued.** A form is the set of `btn-*` classes an
element carries, times the scoping classes above it that `components/button.css` actually reads, and
after the migration there is exactly one of those left. `ui-kit/_worn.py` reads both halves out of
the repo, compares the painted tree against the matrix specimen in both directions, and fails the
build when either side has a row the other does not.

| emphasis | size | width | placements | where a person meets it |
|---|---|---|---|---|
| secondary | md | block | 444 | every row inside a sheet: a provider, a payment method, a way out |
| primary | md | block | 122 | the brass action at the foot of a sheet or a panel |
| primary | sm | content | 71 | Sign up in the header, the action of a state block |
| secondary | sm | content | 57 | Sign in, Not now, Home |
| primary | md | content | 7 | Confirm bet in the mobile dock, the only brass action at content width |
| primary | lg | block | 4 | Confirm bet in the mobile bet sheet |
| secondary | md | content | 3 | the second answer of an action bar |
| primary | sm | block | 1 | See your bet, in a resolved panel |
| secondary | sm | block | 1 | Browse events, beside it |

The tenth is the same secondary/md/block inside `dialog.app-dialog.signin-dialog`, 324 of the 444,
and it is a form of its own for one reason given below.

### The combinations the product does not have

Two emphases times three sizes times block or not is twelve; the product wears nine. The three it
does not are named with a verdict rather than left as blank cells, which is the same control every
declared list in this repo carries:

- **secondary lg, block or not.** The large step exists for one control, the mobile sheet's Confirm, and that control is the brass one. A quiet button at 16 padding would be a secondary action given more room than the primary one beside it, which inverts what the sizes are for. Not forbidden, undecided: it needs a place before it needs a rule.
- **primary lg at content width.** Same shape of answer from the other side. The large size exists because a sheet's foot is the full width of the sheet; a brass control at 16 padding that does NOT own its row is a control asking for weight it has nowhere to spend.

### The one scope that is left

`components/button.css` had eleven scoped selectors and has one. The sign-in sheet's rows lift 1px
under the pointer, and that is the only provider row in the product that answers with a transform: a
row 380px wide needs a second signal that it is a target at all. Everything else that used to be
scoped there - the outcome sheet's sixteen re-declarations, the bet panel's three, the dock's two,
the sheet's padding, the resolved panel's width - said what the vocabulary now says in a class, and
is deleted rather than left to be read.

## Rule

Choose an emphasis, a size and a width. That is the whole of it, and it is three decisions where the
old page had five names and a question about which of them a place wanted.

**One brass action per zone.** `DESIGN.md` states it as the One-Accent Rule and this component is
where it is spent: if a screen has brass on more than the logo, the active chip and the primary
action, it is overspent.

Two labels in this component are still two names for one thing and it is a known defect, not a
decision: the funding action is *Deposit* on My Profile and in the wallet, and *Add funds* in the
header and the dialog; the auth entry is *Log in* in the header and *Sign in* in the dialog. Both are
open in `voice/docs/microcopy.md` under same-thing. Copy the label from the row there rather than
from the nearest screen.

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

**Three faces over ten forms, and the two numbers are the argument for the vocabulary.** Ten is how
many different controls the product paints; three is how many different ways they ANSWER a pointer.
It was five before the migration, and two of those five were the same answer written under two names.
What decides a gallery is a difference measured across all four states in both themes, and the
grouping is computed rather than chosen: 26 occurrences were read and 23 of them are somebody else's
answer.

- `button.btn.btn-ghost.btn-xs @button-matrix` - **The third emphasis, added 2026-08-06 because the product already wore it 105 times.** A transparent ground on a hairline pill with the quiet ink: it keeps the box and gives up the fill, which puts it a real step below secondary. Secondary has a ground and says *you may*; this has none and says *if you want*. Its hover is the 14 per cent `--color-action` wash the whole header band answers with, not `--bg-control-hover`, because a fill appearing out of nothing is not a quieter version of a ground moving - it is a different event. The ink lifts to primary, since ghost rests at muted and has somewhere to go.
- `button.btn.btn-bare @button-matrix` - **The fourth emphasis, and it gives up the box as well.** No ground, no edge, no corner: the like and reply pair under a comment, 72 placements. Its padding is a HIT AREA rather than a size, which is why the size axis does not reach it and it carries its own 4 and 11px; asking for `.btn-bare.btn-sm` would be asking a control with no box for a box. It has only the mark and the word to answer with, so the ink goes brass on hover and nothing else moves, and the press is the one time this control draws a shape at all. **It is the same rest face a `navitem` wears and it is not one**: what separates them is the MEANING, which is the check rule 1 of the atom map exists for. Reply does a thing; it does not go anywhere.
- `button.btn.btn-secondary.btn-sm @button-matrix` - **The quiet answer, and it covers every secondary button in the product at every size.** The ground steps one stone darker under the pointer, the edge goes brass at 45 per cent, and the label lifts to the strong ink; held down it settles onto the pressed stone. The focus ring is the system's one ring, brass, 2px, offset 2px. That size does not change any of it is the argument for the ramp being a ramp: `.btn-sm` and `.btn-md` are a padding and a font step, not two controls.
- `button.btn.btn-primary.btn-sm @button-matrix` - **The difference is the skin.** Hover takes the lit brass to both stops so the whole face comes up and adds a soft glow under it; the press turns the gradient over to 315 degrees so the light falls to the bottom right, which is what a plate pushed in looks like, and the glow goes with it because the glow is the lift. There is no edge to answer WITH, and there is still an edge to be: the band the small brass buttons used to carry was `--color-action` over a gradient whose first stop is `--color-action`, a line nobody could see, so the colour went and the 1px stayed. Taking both would have made `.btn-sm` mean 34px on a brass control and 36px on a quiet one, which is the size axis reading the emphasis axis and is the coupling this vocabulary exists to end. This is also the one control the product ever disables, and a disabled one neither lights up nor presses.
- `button.btn.btn-secondary.btn-md.btn-block @dialog.signin-dialog` - **The difference is one pixel of lift**, and it is the only form in the component that moves. Everything else about it is the quiet answer above. The instrument merged it away twice before it could be seen: first because `transform` was not one of the values a face is made of, and then because the face was keyed without its scope, so the first provider row in a document was measured and the others were skipped as copies of it.
