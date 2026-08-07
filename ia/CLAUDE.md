# ia/ - where the user can go, and what is on each page

`docs/sitemap.md` (entities, screens, navigation, desktop layer, depth map) and `docs/flows.md` (the
four user flows: MJ, FJ2, FJ5+EJ3, SJ1) are the source of truth. `docs/pages/seo.md` and
`docs/pages/system.md` carry the detailed layer, and `docs/blocks.md` banks what a page of a given
TYPE is made of, before one is drawn.

**The HTML in this folder renders the markdown. The markdown wins if they diverge.**

## The one rule that matters most here

**Do not copy a nav table, a screen hierarchy or a flow into another file.** Two copies of one map is
the defect this repo has paid for more than once, and the second copy is always the one that is
wrong. If a screen needs to know its place, it links here.

## The three decisions that govern every page-level node

- **Mobile-first, fully adaptive.** Responsive both ways, but mobile is the priority: block priority
  and the first screen are reasoned from mobile at 360px. Desktop is designed deliberately, not
  derived from a wide layout.
- **Two IA layers.** Global (concept map and flows) answers "where can the user go". Per-page answers
  "what is on this page and how it behaves": blocks, states, components, SEO.
- **SEO-ahead.** URL and slug, H1 and H2, breadcrumbs, schema.org, indexation and internal linking
  are decided here. The wireframe validates layout only; production supplies final content and real
  query volumes. The three are never mixed, so finding that a block is missing never means redrawing
  a wireframe.

## `blocks.md` is banked by TYPE, never by node

A block bank per page type is what lets a new screen be assembled rather than invented. The test of
it was `ui-visual/terms.html`, the first page of a type the system had never drawn: it shipped with
no new class, no new token and no new rule, and what it lacked became rows in a backlog rather than
edits to the system in the middle of building a screen.

## The sidebars here are static markup

Three scripts used to keep every page's roadmap panel in step and they were deleted on 2026-08-07. A
change to the roadmap is now a sweep by hand across the pages that carry it, or a throwaway script in
the scratchpad that is not kept.
