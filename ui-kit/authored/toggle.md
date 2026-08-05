# toggle

## Sources

- `components/filters.css`, where this control lived until 2026-08-05 and where it did not belong: a switch and a sort menu are two control families, and the only thing they shared was a file name.
- `ui-kit/docs/defects.md` row 63 and `ui-kit/docs/backlog.md` S41 - the pass that found it. `filters` had an EMPTY containment, so `ui-kit/_levels.py` called it an atom by arithmetic with no information in it, and the inventory and the vitrine's side panel printed that as a decision somebody had taken. Nobody had. **Gate 39** now asks the question once per component.
- `ui-kit/docs/backlog.md` S39, the target-size pass: this control was 40x22 under a coarse pointer, one of three in the product that failed WCAG 2.5.8.
- The painted screens, counted: 3 placements on 3 screens. Every one of them carries `role="switch"`, measured, with no exceptions, which is why the file has no rule for a `.toggle` that is not one.

## Purpose

One setting a person turns on or off, answered on the spot. A 40x24 track, a 16px knob, and nothing between the two states but the knob's travel and the ground's colour.

It is a **selector** and not an action: `ui-kit/_worn.py` files it that way because pressing it does not DO a thing, it chooses one, and the reason the choice is visible afterwards is that the control stays lit.

## Anatomy

- `.toggle` - the track, and it is only ever written with `role="switch"` on it: 40x24, a pill, a graphite ground and a hairline edge. The state is the ARIA attribute and not a class, because a switch that is on has to say so to something other than a stylesheet, and its knob is a `::after` at 16px, `--text-muted` when off and `--control-knob` when on, travelling by `left` rather than by `transform` so the 3px inset stays readable in the rule.

## When to use

For a setting that takes effect immediately and has exactly two states. Three placements today, all of them in a filter panel.

Never for a choice that needs confirming, and never as a way of asking a question: a switch whose label is a question ("Show closed events?") makes the OFF state read as "no", which is an answer a person did not give. Label the thing being switched, not the question about it.

For a choice between more than two values it is `filters`, the disclosure it stands inside: a list of labelled radios says what the options ARE, and a switch can only say yes or no to one of them. For a value a person picks off a rail rather than out of a menu it is `quick` or `catnav`, which are chips.

## Rule

The track takes the brand brass when it is on, never green. Green and red are outcome semantics in this product, and a switch is not an outcome.

The size is a floor and not a preference: 40x24 under any pointer, because a switch is a target you hit rather than one you aim at.

## Anti-rule

Never use it for a choice with more than two values. That is `filters`, the disclosure this control stands inside: a list of labelled radios says what the options ARE, where a switch can only say yes or no to one of them. A value picked off a rail rather than out of a menu is a chip, which is `quick` or `catnav`.

Never fake the knob with a hit area no measurement can see. The control's own box is 40x24, and an invisible pseudo stretched over a smaller track is a fix nobody in this repo can check, which is the reason S39 was fixed in the boxes rather than around them.

Never give the ON state `--bg-pressed` for its press. A switch that is on is a flat `--color-action` ground, so the quiet system press would read as "it turned itself off" and there is no gradient angle to reverse. It is the one control in the product that asked for a role of its own and got one, `--color-action-pressed`.

Seen: `ui-kit/docs/backlog.md` S39, where this control measured 40x22 under a coarse pointer, one of exactly three in the product below the WCAG 2.5.8 floor.

## States

- `span.toggle @filters-toggle` - The switch, off: a graphite track and a pale knob at the left.
- `span.toggle @filters-toggle (2)` - The switch, on: the track takes the brand brass and the knob travels. Brass rather than green on purpose, because green is an OUTCOME colour in this product and a switch is not an outcome.
- `button.toggle @filters-panel` - **The same switch in the panel it actually ships in**, which no stand held until 2026-08-05. Gate 24 is what asked for it: on the three screens that carry this control it stands inside `.filter-panel > .reverse-row`, and every specimen showed it on its own. It measures as its own face because the ground under it is the panel's surface rather than the page's, and that is the whole reason a stand that never puts two things in one document is how nine passes went by without anyone noticing this was not part of `filters`.
