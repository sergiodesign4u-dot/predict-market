# chart

## Sources

- `ui-kit/docs/inventory.md` L102 - "Price chart (`.ed-chart` SVG plot + y/x axis + `.ed-range` switcher; multi adds `.ml-line` legend)", filed jointly under `components/tabs.css` and `components/chart.css`, states "binary / multi / range", 11.
- `ia/docs/sitemap.md` L83 - the entity field it renders: "Probability chart: history of odds movement over time". It is one field, not a workspace.
- `ui-kit/_levels.py` STATIC - "the plot. Its time-range switch is `.ed-range` and lives in `components/tabs.css`, which does have states". The one sentence a reader needs before asking why a chart has no states.
- `CLAUDE.md`, the last rule under "The rule for a change" - "the chart is ported" was true while it drew as a black rectangle, because **an SVG with no `fill` is black**. A missing value is a value, and this component is the case that produced the rule.
- `voice/docs/microcopy.md` Step 24 - the caption pattern this product uses on a plot: "Live odds & volume - last 30 days", logged with the reason "says what the chart is measuring and over what window". The feed hero's chart is a different component and the same rule.
- `voice/docs/voice.md`, principle 1 - explain the number rather than showing it. A plot with no axis and no window is the bare figure at a larger size.
- The 11 painted screens, all Event Detail variants.

## Purpose

The odds over time, drawn. An area under a line for a binary event, one line per option for a multi-outcome one, with both axes labelled and a mark on now.

The reason it is small and quiet is that it answers one question - has this moved, and when - and refuses the next one. There is no zoom, no crosshair, no tooltip reading a value off the curve, and no second series a person can add. A chart that could be interrogated would be the trader's terminal the product's own description rules out, and the question a spectator has is answered by the shape.

## Anatomy

- `.chart-svg` - the SVG itself.
- `.ed-plot` - the plotting area.
- `.ed-chart-head`, `.ed-chart-foot` - what the plot is and over what window, above and below it.
- `.ed-chart-area` - the fill under the line on a binary event.
- `.ed-yaxis`, `.ed-xaxis` - the two axes. They are labelled, because an unlabelled axis makes a 3-point move and a 30-point move look the same.
- `.ed-chart-now`, `.nowline` - the mark on the present moment, which is what makes the rest of the curve read as history.
- `.ml-line` - one option's line on a multi-outcome event, and `.ed-legend` the key to them.

## When to use

On an Event Detail screen, once, under the head and above the analysis. Its 11 screens are that one screen's variants.

Never on a card or in a grid. A sparkline in a feed would be a shape too small to read attached to a number that is already exact, and the feed's own answer to "has this moved" is the one-line why on each card.

The multi-outcome case is where it stops being decorative. Four candidates with four lines is the only place in this product where the relationship between options is visible at all, and it is the reason the legend exists rather than colour-coded labels on the plot.

**A colour in the legend is not an outcome.** Green and red belong to YES and NO; a candidate in a multi-outcome chart is one of several options and takes a neutral series colour, and that distinction is the rule from `DESIGN.md` that `CLAUDE.md` promotes because it decides other things.

## Rule

Every plot says what it measures and over what window, in words, beside it: a curve with no caption and no axis is a shape, and a shape is not an explanation.

## Anti-rule

Never build its range switch here: *24h / 7d / 30d / All* is `.ed-range` and belongs to `tabs`, which owns every segmented switcher in this product, and a second implementation inside the chart would put the same three-segment control in two files that have to be kept in step by hand.

Seen: `ui-kit/docs/backlog.md` S16 and S17, both closed on 2026-08-03 and both exactly that - one shape declared in five places and then in two, kept in step by hand until somebody measured it. `ui-kit/docs/inventory.md` L102 files this component's own row under two css files for the same reason, and the split is deliberate: the plot here, the switch there.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC. A plot is a datum: it reports the odds and answers no pointer, there is no hover readout, no crosshair and no selectable series. The only control on the chart is its time range, which is `.ed-range` from `components/tabs.css` and is photographed there.

**The one warning this component earns is not about states, and it is in `CLAUDE.md` because of this file.** An SVG element with no `fill` is black, not invisible and not inherited. The port of this chart passed every check that read the source - the markup was there, the classes were there, the file was ported - while the thing in the browser was a black rectangle, because a missing value is a value. Everything drawn here has to be measured as a computed result in a browser, in both themes, and never read out of the markup.
