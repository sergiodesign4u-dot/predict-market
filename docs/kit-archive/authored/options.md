# options

## Sources

- `ui-kit/docs/inventory.md` L101 - "Multi outcome list (`.opt-list` + \"pick an outcome\")", filed L3, on event-detail-multi, states "selected marked (`.sel`), Change link", 2.
- R5 in `ui-kit/docs/architecture.md` - the full outcome list does not stand inside a card. Counted: 161 cards across the painted tree, 21 of them multi-outcome, **every one with exactly two rows**, `.opt-list` on 2 screens with 5 rows and 0 of them inside a card, and no "+N more" string anywhere.
- `ia/docs/sitemap.md` L315 - the reason the cap is two: only the two leading options are shown on a card, with no "+N more" line, so multi-outcome cards stay close to binary-card height and the meta rows line up across the grid. The row calls it "a feed preview rule only".
- `ia/docs/sitemap.md` L77 - the entity field: Type is Binary or Multi-outcome, "multiple options, each with YES/NO", and the card must render both layouts with no new field.
- `ui-kit/_levels.py` STATIC - the entry that says what the row is and is not: a `<div>` whose pressable part is the `yesno` pair inside it, and which also carries a JS click handler with no keyboard path.
- The 25 painted screens.

## Purpose

An event with more than two answers, as a list. One row per option: the name, its probability, and the pair of controls that back it. Two rows on a card, all of them on the detail.

The component exists because a multi-outcome event is not a different KIND of event in this product, it is the same event with more sides. Nothing about it gets its own screen, its own card treatment or its own vocabulary: the same question, the same odds figure, the same YES / NO, repeated per option.

## Anatomy

- `.options` - the block on a card: exactly two rows, the two leading options, and no line saying how many were left out.
- `.opt-list` - the same block on the detail, where every option is shown. It is a modifier on the same rows rather than a second component.
- `.opt-row` - one option, and `.sel` on it when it is the one being backed.
- `.opt-name` - the option. It is the only user-written content in the component and it is not truncated.
- `.opt-prob` - the option's probability, in the display face on a card and quieter in the list.
- `.opt-sel-tag` - the mark on the chosen row. It is hidden inside `.app-case`, because in the product the selection is carried by the row's own tint instead.

## When to use

Inside a multi-outcome card, capped at two rows, and inside the detail column, uncapped. Those are the two places, and R5 draws the line between them as a rule about PLACE rather than count: the two-row display is the card's own anatomy, not a smaller component.

The cap is a preview rule and not a fact about the event. An event with nine options still has nine; the card shows the two leading ones because a grid where multi-outcome cards are twice the height of binary ones stops reading as a grid.

Never as a general list of choices. This is not a radio group and not a settings list. Every row here is a market side with a price, and a row with no probability on it is not this component.

## Rule

The list never says how many it is hiding: no "+N more", no ellipsis row, no counter. A person who wants the full set opens the event, which is where the full set lives.

## Anti-rule

Never draw the row's controls from `button`: what a person presses in an option row is the `yesno` pair, which is the only place the outcome colours are allowed on a control, and a `.state-btn` tinted green here would put the win colour on a generic action and break the one rule in `DESIGN.md` that decides other things.

Seen: `ui-kit/docs/inventory.md` L79 against L126 - the tinted pair filed under `components/yesno.css` and the brass primary CTA filed under `components/button.css`, two adjacent rows of one table pointing at two different files for two things that both look like a button on a card. This component sits directly on top of that boundary, because its row contains one of them and is next to the other.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC. The row is a `<div>`: what a person actually presses is the `yesno` pair inside it, which has its own four faces on its own page, and the row's `.sel` tint is a fact about the event rather than an answer to a pointer.

The entry carries a second sentence that is not about styling and is the more useful half: **the row also carries a JS click handler and no keyboard path.** That is a real defect and it is a defect of the markup, so it belongs to the grey tree and to `docs/backlog.md`, not to a state rule here. Writing a `:hover` onto this row would make it LOOK operable to a pointer while staying unreachable from a keyboard, which is worse than the honest absence.
