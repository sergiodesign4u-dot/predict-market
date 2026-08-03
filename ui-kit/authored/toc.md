# toc

## Sources

- `ui-kit/docs/inventory.md` L89 - "Contents rail (`.toc`, a document's own sections)", filed L1, on `terms`, states rest / hover / press / current, one screen.
- The one screen: `ui-visual/terms.html`, fourteen sections and 1,611 words, the first page of a TYPE the system had never drawn.
- `ui-kit/docs/backlog.md` S5, the row this component closed, and S12, which is the row its `top` value opened.
- `ui-kit/specimens.map.json`, the `toc-rail` entry, whose note explains why it is shown at 900 and why its rows are anchors.
- `components/toc.css` and `components/patterns/browse-shell.css`: the rail is a SLOT in the browse shell, and this component is what stands in that slot on a document page.

## Purpose

A document's own table of contents, pinned beside the reading column, so a person who came for one clause can reach it without reading the fourteen above it and can see where they are while they scroll.

It exists because a system that had drawn feeds, cards, panels and dialogs had never drawn a page of PROSE, and the test of that was building one. This is the component that came out of the test, and it was built by taking the slot the sub-category rail already stood in rather than by inventing a second rail.

## Anatomy

- `.toc-d` - the `<details>` wrapper. Below 900px the contents is a disclosure above the text; at 900 and up it is the rail and the summary goes away.
- `.toc-head` - the "On this page" summary, which is the control on mobile and is hidden on desktop, because a rail beside the text does not need a label saying it is a rail.
- `.toc-list` - the fourteen rows.
- `.toc-link` - one row: a section title and its number. It is an anchor and it always was, because it navigates INSIDE this page, which is the whole difference between this and `catnav`.
- `.toc-n` - the two-digit number at the end of a row, in the mono face, so the eye can count sections without reading them.

## When to use

On a document: a page whose subject is text with named sections, long enough that a person will want a specific one. Terms, and the privacy and cookie documents when they are built.

Not on a feed, not on a detail screen, not anywhere the rail slot is already holding a category list. The slot is the same 214px in the same shell, and only one thing can stand in it.

The rail is capped to the window and scrolls inside itself, which is not decoration: at a 640px window and a 14-row list the last two rows sat below the fold with no way to reach them, and the cap is what fixed it. Any list that will grow past a short window has to carry the same three declarations.

## Rule

The rows are anchors to sections of THIS page: if a row would navigate to another document, the block is not a contents and does not belong in this slot.

## Anti-rule

Never use it for the category strip or the sub-category rail: those are `catnav`, whose rows leave the page, and putting a contents in that slot would give a person two things that look identical and go to different kinds of place.

Seen: `ui-kit/specimens.map.json`, the `toc-rail` note, which records that the two stand in the same slot at the same width and had to be told apart by what their rows DO. `ui-kit/docs/backlog.md` S12 is the other half: three components type the same clearance number and this one is deliberately different, because a document page has no category strip to condense.

## States

- `a.toc-link @toc-rail` - A row at rest and under the pointer. Quiet muted ink on the plate; hover brings the ink up and the row's ground with it, and the press settles it. The whole row is the target, not the words, so the number at the far end is inside the same hit area.
- `a.toc-link @toc-rail (2)` - The row you are ON, marked with `aria-current`. Brass ink and a brass edge on the left, and it is the only row in the rail that carries colour, because a rail where two rows are marked answers the question twice.
