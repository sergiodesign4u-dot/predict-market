# course-chrome

## Sources

- `ui-kit/docs/inventory.md` L69 - "Screen-tree drawer / roadmap sidebar", filed with no level, on "every page (course chrome)", 104 screens.
- All 105 painted screens and all 58 stand pages carry it, and none of them is the product: it is the panel this REPOSITORY wraps around every page it holds.
- `ui-kit/docs/history.md`, "What step 9 settled", where the two panels were found to be one file speaking two vocabularies, and forty screens were marking the wrong page as the one you are on.
- `ui-kit/_adoption.py`, whose declared list carries this file's three not-the-product classes: `.next`, `.planned` and `.theme-switch-inline`.
- `components/course-chrome.css`, which is the only component file in this system that may not read a themed role.

## Purpose

The panel down the left of every page in this repository: where you are in the course, what is built, what is next. It ships inside `components/` for one reason only, and the reason is not that it is part of the product: the painted screens render it, so it has to be painted by the same stylesheet they load.

It is the one place in the system where a rule about the PRODUCT would be wrong. The panel does not follow the theme, because it is chrome around a screen that does, and a panel that changed colour with the product would make it impossible to tell which of the two you were looking at.

## Anatomy

- `.sidebar` - the panel. Fixed on desktop, a drawer on mobile.
- `.rm-toggle` - the three-line control that opens the drawer, and `.rm-overlay` is the scrim behind it.
- `.sidebar-back` - the row that leaves the system for the thing the system is for, with `.bk-arrow` in front of it.
- `.sidebar-brand` and `.sidebar-project-name` - the head of the panel.
- `.sidebar-divider` - a LABEL. It names a run of rows and opens nothing, and it takes `.active` for the group you are in.
- `.sidebar-page-link` - a ROW. It opens a page. That is the whole vocabulary and it took a stage to get there.
- `.sidebar-sub` and `.sidebar-sub-link` - the second level, indented, same rule: a row that navigates is a link.
- `.active` - the page you are ON, at whichever level it sits, in one colour rather than brass in one panel and grey-plus-a-dot in the other.
- `.planned` and `.next` - roadmap states, carried only by the 28 course pages, which have their own inline copy of this panel and never load this sheet.
- `.theme-switch`, `.ts-swatches`, `.ts-sw`, `.ts-dark`, `.ts-light`, `.ts-label` - the theme control, above the tree because the tree is forty rows long and a control at its foot needs scrolling to reach.

## When to use

Never as part of a screen. This component is applied by the tooling that writes the pages, and a person building a product screen has nothing to do with it. It is on this vitrine because deleting a rule here breaks forty pages in silence, which is exactly what happened when a class that looked dead turned out to be built by `_nav.js` at run time.

The one thing worth reading here before touching it: the vocabulary. A label names, a row opens. That distinction is the whole of step 9, and it was learned the expensive way, with a family name drawn heavier than the page under it and pointing nowhere.

## Rule

A label names and a row opens: if it has an href it is a link and it is drawn like one, and if it does not it is a label and it is drawn quieter than the rows it names.

## Anti-rule

Never let this panel read a themed role: every colour here is literal on purpose, and reaching for the roles that `base` and the components use would make the chrome change with the product it is wrapped around.

Seen: `ui-kit/docs/history.md`, "What step 9 settled", where a link class inside this panel was styled from `ui-kit/_page.css` and therefore rendered in the browser's blue on all 105 painted screens and every specimen, because the vitrine's stylesheet is not loaded there.

## States

- `a.sidebar-back @course-chrome` - The way out. Quiet at rest, ground and ink answer the pointer, and the arrow does not move, because a row that slides is a row you cannot aim at.
- `a.sidebar-page-link @course-chrome` - An ordinary row on a painted screen's panel: hover on the ground, press on the pressed stone.
- `a.sidebar-page-link.active @course-chrome-system` - The page you are on, in this vitrine.
- `a.sidebar-sub-link @course-chrome` - A second-level row, smaller and quieter than its parent, and the indent rather than the weight is what says it is under something.
- `a.sidebar-sub-link.active @course-chrome` - The same row marked, and the mark is the same one the first level uses.
- `a @course-chrome-system` - A row in the panel's note, which is the only prose in the panel and the one place a link inside it appears.
- `a.sidebar-page-link.planned @course-chrome-roadmap` - A stage that is not built yet, on a course page. Muted, with its badge.
- `a.sidebar-page-link.planned.next @course-chrome-roadmap` - The one that is next, which is the only planned row that is allowed to be louder than the others.
- `button.theme-switch @course-chrome` - The two-swatch control that flips the product between Vault and Daylight. Its own focus ring is inset, because the panel's edge is against the window.
