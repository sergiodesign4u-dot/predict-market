# tabs

## Sources

- `ui-kit/docs/inventory.md` L107 - "Content tab strip (Comments / Biggest bets / Bets / Activity, CSS radio)", filed L3, on event-detail and its bet variants, state "per-tab active".
- `ui-kit/docs/inventory.md` L67 - "Active / History tabs (`.tabs`)", on My Bets, 9.
- `ui-kit/docs/inventory.md` L113 - "Segmented switcher (`.seg` / `.rules-tabs` / `.ed-range`)", on the event's comments, rules and chart, state "active segment", 9.
- `ui-kit/docs/inventory.md` L102 - the chart's time-range switch, filed jointly under `components/tabs.css` and `components/chart.css`, which is the seam between the two components.
- `voice/docs/microcopy.md` Step 14 - the labels this strip carries, and the rewrite that produced them: *Top Holders* to **Biggest bets**, *Positions* to **Bets**.
- `voice/docs/microcopy.md` Step 25 - "The switch that said its own state (19 screens, both trees)", found by re-measuring contrast rather than by reading: a control carried the word `off` inside the pill at 1.42:1 because it was never meant to be read. The lesson is this component's, since a switch is what a segment becomes when there are two of them.
- `ui-kit/docs/backlog.md` S16 and S17 - the shape this component keeps out of other files: one control declared more than once and kept in step by hand.
- The 20 painted screens, and the profile redesign's CSS-only Track-record / Past-wins / Resolved tabs, whose structure stayed in the grey tree.

## Purpose

Every place in this product where one region shows one of several things. Four content tabs on an event, two on My Bets, three segments on the profile, and the small segmented switchers for comment sort, the resolution rules and the chart's time range.

They are one component because they are one mechanism, and the mechanism is the decision: a hidden radio input and a label, so the state lives in the DOM rather than in a script. Nothing here needs JavaScript to remember which tab you are on, which is why the tabs survive on a page loaded from a file, in a print, and with scripting off.

## Anatomy

- `.ed-tabs`, `.ed-tabwrap`, `.ed-tabbar` - the event's tab strip and the region under it.
- `.ed-tabradio` - the hidden input that IS the state. It is a real form control, so the arrow keys and the tab order come from the browser.
- `.ed-tablabel` - what a person actually presses, and `.ed-tab-count` the number beside a label when the tab has one.
- `.ed-tabpanel` - one panel, and `.ed-panel-comments`, `.ed-panel-holders`, `.ed-panel-positions` and `.ed-panel-activity` the four of them.
- `.tabs` - the My Bets pair, Active and History. Two tabs, a different mechanism, because these are two screens with two URLs rather than two panels.
- `.ptabs`, `.ptab-bar`, `.ptab-in`, `.ptab-lbl`, `.ptab-panel` - the profile's three, on the same radio mechanism as the event's.
- `.rules-tabs`, `.rules-tab` - *Rules* and *Market Context*, the one pair in this product where the two segments make different promises.
- `.ed-range` - the chart's time range. It is here rather than in `components/chart.css` on purpose, and the STATIC entry on the chart names it.

**One class left this file on 2026-08-03** and it is named here rather than quietly dropped. The small segmented switcher went to `components/comments.css` (`docs/backlog.md` 17). It lived here because this file "owns every switcher", and that sentence was the defect: all seven rules are scoped `.cmt-controls`, so the ownership was a CATEGORY and not a containment, and it cost `_levels.ORDER_BREAK` a hand-written cycle - the tab strip holds the thread, and the thread held a piece of the tab strip. The cycle went with the rules.

## When to use

When one region on a screen has several contents and a person picks between them without leaving. That is the whole test, and it is what separates this from every navigation control in the product: after pressing a tab you are still on the same page.

Two or more panels, never one. A single tab is a heading.

Not for a filter. A tab shows a different SET; `filters` narrows the one you are looking at, and it announces its current value in its own label because that is the thing a person forgets.

The chart's range switch belongs here even though it lives on the chart. That is why `components/chart.css` is in `_levels.STATIC` with a line pointing at `.ed-range`: the plot answers no pointer, and the only thing on it that does is one of these.

## Rule

The state is in the markup: a hidden radio and a label, so which tab is open survives a reload, a keyboard and a browser with no script running.

## Anti-rule

Never draw a tab strip as a row of `button` controls: the family in `components/button.css` is for things that DO something, and a filled chip in a tab bar makes the current panel look like an action that has been taken. What a tab needs is a label and a state, and the label is the control.

Seen: `voice/docs/microcopy.md` Step 25, where exactly this confusion had already shipped in the other direction - a switch was built with its state written INSIDE the control as the word `off`, drawn in the browser's default black at 1.42:1 on graphite, on 19 screens in both trees. It was never meant to be read; a control that has to say its own state in words is a control wearing the wrong mechanism.

## States

- `input.ed-tabradio @tabs-detail` - The input that holds the state. It is off-screen rather than `display:none`, which is why it can be focused at all, and the focus it takes is what draws the ring on the label beside it.
- `label.ed-tablabel @tabs-detail` - The open tab: brass ink and a lit edge under it. All four faces, and the label is what receives the pointer because the input is not where a person is looking.
- `label.ed-tablabel @tabs-detail (2)` - A tab that is not open, at rest, hovered, held and focused. Quiet ink, ground answers, and the strip does not reflow: four tabs that change width as a thumb crosses them are four moving targets.
**The two `.ed-range` faces left this block on 2026-08-05**, and the sentence that stood on one of them is what sent them: "the same quiet ground as every other unchosen segment in the product, which is the point of there being one switcher shape rather than three". It was not one shape, it was one shape written twice - this file and `components/comments.css` held the same four painted rules byte for byte - and the chip is `chip` now, in `components/chip.css`. This file keeps the rail, `.ed-range`, which is the container.
- `input.ptab-in @profile-identity` - The profile's radio, the same mechanism on a different screen.
- `label.ptab-lbl @profile-identity` - The profile's open tab.
- `label.ptab-lbl @profile-identity (2)` - A profile tab that is not open. It is worth comparing this face with the event's: same mechanism, different ground, and the difference between them is the plate underneath rather than the control.
- `button @tabs-mybets` - Active or History, whichever you are on. Two tabs that are also two pages, which is why they are anchors around buttons rather than labels around inputs.
- `button @tabs-mybets (2)` - The one you are not on, all four faces.
