# yesno

## Sources

- `ui-kit/docs/inventory.md` L79 - "Tinted YES / NO buttons", filed L2, on "every event card + bet panel", states rest / hover / compact, 14 screens.
- The 14 painted screens: every feed and category in its full state, and the two multi-outcome detail screens.
- Rules of use R7, "A bet control does not stand on a list of events", whose check reads: on any screen with a grid of cards there is no amount field and no Confirm.
- `CLAUDE.md`: "green and red are outcome semantics (YES / NO), brass is the brand. An accent never borrows the win/lose colour, and a candidate in a multi-outcome chart is not an outcome."
- `voice/docs/microcopy.md`, where the labels are the bare words *Yes* and *No* and carry no price, because a price in the label is a number that goes stale between renders.
- `components/yesno.css` and `components/options.css`, which is the multi-outcome row this pair sits inside.

## Purpose

The two sides of a binary market, as a pair of tinted controls. Green YES on the left, red NO on the right, always both, always the same width. It is the only place in this product where green and red mean anything, and what they mean is an OUTCOME.

The pair is a declaration of intent, not a bet. Pressing one on a feed card opens the event with that side pre-selected; it does not stake anything and it does not ask for an amount. That is R7, and it is the reason a person can tap around a feed without ever being one accidental press from a transaction.

## Anatomy

- `.yesno` - the pair. One element holding two, so they cannot be used singly: a market with only a YES is not a market.
- `.compact` - the same pair at card size, where it sits under the odds bar and the two labels are the whole of it.

## When to use

Wherever a binary market is shown and a person might have an opinion: on every card in a feed or a grid, and inside the bet panel where the choice is confirmed.

Inside a multi-outcome market it is the row's control rather than the row: `options` draws the four candidates and each row holds a pair, because a candidate is a question with a yes and a no, not one of four colours.

Never as an accent, a status or a category tint. Green and red carry outcome and nothing else in this product, so a green chip that means "verified" or a red one that means "urgent" would spend a meaning the whole system depends on.

## Rule

The pair ships together and at equal weight: the same width, the same tint strength, the same type, so nothing about the control suggests which side the product would prefer a person took.

## Anti-rule

Never build one of these out of the button family: a `.state-btn` or a `.confirm-btn` tinted green would put an outcome colour on an ACTION, and the brass action beside it is what a person is actually pressing to spend money.

Seen: `ui-kit/docs/inventory.md` L79 against L126, where the tinted pair and the brass primary CTA are two rows of the same table with two different files, and `CLAUDE.md`, which states the separation as the one rule from `DESIGN.md` that decides other things.

## States

- `button.yesno-pick.bp-side.sel @.bet-panel` - **The chosen side, and since 2026-08-06 there is ONE of these where there were THREE.** This one group is now the selected side in the bet panel, in the mobile dock and in a multi-outcome row, because all three measure the same control. The selection is a class and not a pseudo, since it has to survive the pointer leaving, and it is the loudest either tint ever gets. It is filled in the outcome's colour and that fill is the panel's loudest statement: whatever else is on the screen, this says which way the money goes. **The dock's chosen side used to be its own group** - a lighter `--outcome-yes-fill-strong` under a brighter ink - and backlog S49 asked why the same control should differ at two widths when the dock IS the panel below 760px. It does not any more, and the proof is that this gallery merged: the capture groups by what a face MEASURES, so two entries becoming one is the answer arriving rather than being asserted. The press is by depth, because `--text-on-no` over `--outcome-no` is 4.64:1 and has 0.14 to spend, so moving the fill would spend contrast the label does not have.
- `button.yesno-pick.bp-side @.bet-panel` - **The side that is not chosen, all four faces.** It stays legible rather than being dimmed, because changing your mind is a normal thing to do at this point and a greyed alternative reads as unavailable. Its hover moves the edge and the ink and leaves the ground alone.
- `button.yesno-pick.yesno-pick-bar.bp-side @.bet-dock` - **The same control in the sticky bar, and the one difference left is what a hover moves.** The bar also takes `--bg-control-hover` and carries its label all the way to `--text-strong`, where the panel stops one stone short. That was added long after the panel's, on the argument that the bar is the control a bet is actually placed with below 760px, and S49 did not ask about it, so it stands. Photographed separately because a sticky bar over scrolling content is not a plate on a page.
- `span.yesno-pick.bp-side @.bet-panel` - **The side as a STATEMENT rather than a control**, in the states where the choice is already made and the panel is reporting: processing, error, resolved. Same face, no pointer, and the gallery shows the disabled reading as not-set, which is correct - it is a `<span>` and there is nothing to disable. It is also the one the first cut of this migration missed: the markup helper matched `<button>` and these 12 lost their box until the before-and-after named them.
- `button @button-outcome-row` - The YES side at rest, hovered and pressed. The tint deepens under the pointer and the edge takes the outcome line; held down it settles rather than lifting, because a control that lifts under a thumb reads as a toggle that has already answered.
- `button @button-outcome-row (2)` - The NO side, the same three answers in the other colour, and deliberately the same strength: the two tints are measured against each other rather than each against the plate.
- `a @button-outcome-row` - The anchor that wraps a side on a card, which is what makes the whole tile a target and is why a card can be tapped anywhere.
