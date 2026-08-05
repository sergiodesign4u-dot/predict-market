# input

## Sources

- `ui-kit/docs/inventory.md` L122 - "Amount field + quick-amount chips", filed L1, on the Deposit dialog and the deposit pages, states rest / selected / focus; and L123, "Field label", on dialogs and forms.
- The 105 painted screens carry the label and the field, because the deposit sheet is on every one of them; the quick chips stand in the deposit dialog and in the bet sheet.
- `voice/docs/microcopy.md` - the funding rows: the field's own label is *Amount to add*, and the two names for the action around it (*Deposit* against *Add funds*) are an open same-thing defect.
- `ui-kit/specimens.map.json`, the `input-states` entry, whose note says why hover and focus are NOT staged there: faking them with a stand class would make the specimen describe itself.
- `components/input.css`, and `DESIGN.md` L99, which is where the 1px hairline is specified as a line rather than a distance.

## Purpose

The two places a person types a number into this product: how much to deposit, and how much to stake. One field, one label above it, and a row of chips beside it that fill the field with a common amount so most people never type at all.

Everything about it is built for a thumb and a hurry. The figure is 18px, larger than any other text a person enters, because it is money and it is being confirmed at a glance. The chips are the fast path and the field is the exact one, and the two write to the same value.

## Anatomy

- `.field-label` - the small caps label above a field. On its own it is the only part of this component that appears outside a money context.
- `.amount-row` - the row that holds the currency mark and the field, so the mark reads as part of the field rather than as a word before it.
- `.amount-input` - the field. 18px figure, hairline edge, and the one control in this system whose focus ring has to out-specify its own `outline:none`.
- `.addr` - the same field carrying a wallet address instead of a figure: mono face, smaller, because an address is read character by character and a proportional face makes that harder.

## When to use

Where a person enters an amount, and that is two flows: funding and staking. Both are money, both are confirmed by a brass action next to them, and both put the field inside a sheet.

For anything that is not money, this is the wrong component and the system does not currently have the right one. A search box, a comment box and a form field are not here, and the honest answer when one is needed is a row in `ui-kit/docs/backlog.md`, not a fifth use of the amount field.

The label is not optional and it is not a placeholder. A placeholder disappears the moment a person types, which is exactly when they most need to know what they are typing into.

## Rule

The chips and the field write the same value, so whatever a chip sets, the field shows: a person who taps 50 and then edits it is editing 50, not starting again.

## Anti-rule

Never build a quick-amount chip out of the button family: those chips are `quick`'s, which left this file on 2026-08-05, and a `.btn` in that row would answer a pointer with the brass edge of an ACTION rather than with a selection. The two names in the sentence that used to stand here, `.state-btn` and `.auth-btn`, were retired the same day.

Predicted: no screen has made this mistake. It is named because the chip row LOOKS like a row of small buttons and is the nearest thing in the system to one, and because the button family's own page now says the opposite thing about chips.

## States

- `input.amount-input @dialog.app-dialog` - The field at rest, hovered and focused, in the deposit sheet. Rest is the well: a darker ground than the sheet, a hairline, and the figure in the primary ink. Focus is the system ring plus a brass edge, and it is the one place a component reaches past `:focus-visible` on purpose.
- `input.amount-input @dialog.app-dialog (2)` - The same field on the states specimen, where the markup ships the attribute rather than a stand class.
- `input.amount-input.addr @dialog.app-dialog` - The address variant. Same well, mono face, and the figure size drops because an address is not a figure.
- `input.amount-input @.bet-panel` - The stake field in the bet panel. Same anatomy on a different plate, which is why it measures as its own face.
- `input.amount-input @dialog.bet-sheet` - The stake field inside the mobile bet sheet, and it is not the well the other three are: no ground, no edge and a square corner, with the focus signal carried entirely by a 3px brass ring drawn outside the box. The sheet is 360 wide and a boxed field inside a boxed sheet is two frames deep, which is the reading this measurement supports and does not prove.
