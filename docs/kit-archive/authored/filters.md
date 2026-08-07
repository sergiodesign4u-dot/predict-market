# filters

## Sources

- `ui-kit/docs/inventory.md` L130 - "Filter menu (Sort / Frequency)", filed L1, on feed and category, states closed / open; and L131, "Reverse-order toggle switch", states on / off.
- All 105 painted screens carry the menu, because the feed controls row is part of the browse shell every screen stands in.
- Rules of use R4, "One category band, one level of sub-categories", whose check ends "and the sort control in the row with them".
- `voice/docs/microcopy.md` L248, the row for *No events match your filters*, which is the sentence a person sees when this component has been used and the answer is empty.
- `wireframes/_critique.md` L14, the dead-end finding on the eight category empty screens: the state this component can produce had a CTA that went nowhere.

## Purpose

The two controls that change what a list SHOWS without changing where you are: a menu that sorts, and a switch that reverses. They sit in the feed controls row beside the category strip, and they are deliberately the quietest interactive things on a browse screen, because a person came to read events and not to configure a list.

Both are native. The menu is a `<details>` and the switch is a checkbox, so both work before any script does, and the open state of the menu is the element's own attribute rather than a class somebody has to remember to remove.

## Anatomy

- `.filter-menu` - the `<details>` that holds the sort choices. Its summary is the closed control and its panel is the open one.
- `.filter-panel` - the dropdown, aligned to the right edge of its summary so it never leaves the plate.
- `.reverse-row` - the row that holds the switch and its label together, so the label is part of the target.

## When to use

In the feed controls row, and only there. One menu and one switch per list, in the row under the category band, which is what R4 fixes in place: one band, one rail, and the sort control in the row with them.

The menu is for a choice that CHANGES THE ORDER of what is already there. It is not a place to hide navigation: a choice that takes a person to another screen belongs in `catnav`, whose rows are links and look like links.

When filtering empties the list, the screen owes an explanation and a way back, and neither is this component's: that is the `state-block`, with the sentence from microcopy and a control that clears the filter.

## Rule

The state a person chose has to survive the control closing: the menu shows the current sort in its own summary, so a closed menu still answers the question it asked.

## Anti-rule

Never put a destination in the sort menu: a row that navigates belongs to `catnav`, and mixing the two makes a menu where some choices reorder the page and some replace it, with nothing in the row to say which is which.

Predicted: no screen does this today. It is named because the menu is the only dropdown on a browse screen and is therefore the obvious place for the next person to put "Categories", and because the vocabulary lesson that separates a label from a row was already paid for once in the side panel.

## States

- `summary @catnav-chips` - The closed menu: the quiet chip family, hover on the ground and a brass edge, and the current sort printed inside it. Open is the same element with the panel below it, which is why the open state is the browser's attribute and not a class.
- `label @catnav-chips` - A choice inside the panel. The row is the target, ground answers the pointer, ink holds still.
- `label @catnav-chips (2)` - The choice that is currently in force, marked in brass, the same mark the rail uses for the page you are on.
