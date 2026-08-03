# position

## Sources

- `ui-kit/docs/inventory.md` L162 - "Position row (`.pos`: question, figures, status)", filed L3, on active-bets, notifications, wallet and profile, states "active / resolved / skeleton".
- `ui-kit/docs/inventory.md` L160 - "Portfolio summary (`.pos` 3-figure grid: total / cash / in-play + inline CTA)", on my-profile and wallet.
- `ui-kit/docs/inventory.md` L159 - "Resolved-predictions history (`.pos-side.pos-won` green / `.pos-lost` red)", on my-profile, public-profile and active-bets-history.
- `ui-kit/docs/inventory.md` L141 - the loading face, `.pos.skeleton`, shared with `components/card.css`.
- `voice/docs/voice.md`, the Lexicon - **"Not allowed in the UI (trader jargon): ... position (for the user's own bet)"**, and the row above it: your bets collected are *My Bets*, not *My Positions*, because "'Position' is Dan's trader word". This component's NAME is the word the product's own dictionary bans for the thing this component draws.
- `voice/docs/microcopy.md` Step 14 - where that rename was carried out in the copy: *See your position* became *See your bet*, "in open positions" became "in open bets", the tab *Positions* became *Bets*. The screens changed; the file did not.
- `ui-kit/_levels.py` MODIFIER - `.skeleton` is declared a state word here, because `components/position.css` writes it as a subject and `components/skeleton.css` only as an ancestor, and without the declaration nineteen loading screens read as position roots.
- The 36 painted screens.

## Purpose

A bet a person already has, as a row. The question, what they put on it, which side, what it is worth now, and whether it has resolved. The same rows make My Bets, the wallet's list, the notifications that reference a stake, and the public track record on a profile.

It is the product's memory. Everything else here is about an event that might happen; this is the only component that reports what a person already did, which is why it is the one place where green and red are allowed on a figure: `.pos-won` and `.pos-lost` are outcomes, and an outcome is exactly what the two colours mean.

## Anatomy

- `.pos` - one row, and the same class as the three-figure portfolio grid.
- `.pos-top` - the row's head.
- `.pos-q` - the question the bet was on. User-written content, whole.
- `.pos-side` - which way it went, with `.pos-yes` and `.pos-no` for the two sides.
- `.pos-won`, `.pos-lost` - the resolved faces, in the outcome colours. This is a report and never a control.
- `.pos-figures`, `.pos-fig` - the numbers: stake, current value, payout.
- `.pos-record` - the summary line above a list.
- `.pos-note` - the line a row adds when the figure needs explaining, which is principle 1 at row size.
- `.skeleton` - the loading face. It is a state word rather than a part, and `ui-kit/_levels.py` declares it as one.

## When to use

Wherever a person's own bets are listed: My Bets in both its tabs, the wallet, the profile's public record, and any screen that references a stake a person holds.

Read-only, always. A row reports; it does not close, sell or change anything. There is no cash-out control in this product, and a row that grew one would be the first place the product started behaving like an exchange.

The public and the private list are the same component. A track record on somebody else's profile is these rows with the figures a person chose to make public, and building a second version for the public case is what `profile`'s anti-rule exists to stop.

**And there is a thing to know before opening the file.** This component is called `position`, and *position* is on the banned list in `voice/docs/voice.md` for exactly the meaning drawn here. The screens were rewritten in Step 14 and the file was not, so the product says *bet* in every visible string and the system says *position* in every class name. Nothing is broken by it; a person reading `.pos-won` in the css and *Bets* on the screen simply has to know they are the same thing.

## Rule

A row reports and never acts: the figures are what happened, the outcome colours are a result, and nothing in it commits or reverses money.

## Anti-rule

Never let a row's outcome colours reach a control: green and red here are the settled result of a bet, and the tinted pair a person presses is `yesno`, which is the only place in the system the outcome colours are allowed on something pressable. A resolved row drawn with the same treatment as a live control would offer a bet on an event that has already ended.

Seen: `wireframes/_critique.md` L77, the resolved-detail finding, where a resolved screen reused the live body verbatim and went on offering the mechanics of a bet nobody could still place. The rows are the other half of that screen, and this is the same mistake at row scale.

## States

The gallery below is empty, and that is a gap rather than a decision. This component is NOT in `ui-kit/_levels.py` STATIC and `components/position.css` declares two hover rules, both of them real: `.app-case a:has(>.pos):hover>.pos` and the question inside it.

Nothing was photographed because of what those selectors are. The element that CHANGES is the row; the element that is HOVERED is the anchor wrapped around it, and the states pass points at the subject of the rule. So the pass hovered a row that does not answer a pointer and recorded no difference. The row does answer, in the product, at 36 screens' worth of lists.

This is written here rather than fixed because it is an instrument gap and the instrument is shared: `ui-kit/_verify/states.cjs` would need to read `:has()` and hover the ancestor, which changes what every component's gallery is measuring. Until then, a reader should take an empty gallery on this page as "not photographed", and the file above as the answer.
