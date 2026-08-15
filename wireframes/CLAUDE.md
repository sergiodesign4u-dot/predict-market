# wireframes/ - the grey tree

105 screens. This tree owns **structure and copy**. It decides what is on a page, in what order, and
what it says. The painted tree follows it.

## The invariants

- **Grey means grey.** Neutral greys only, monochrome outline icons. No colour, no type choice, no
  shadow, no finished UI. The moment a wireframe looks decided, it stops being read as a question.
- **Never paint this tree**, and never let a block arrive here from the paint. Structure flows one
  way: decided here, followed there.
- **A heading level is structure**, so it is decided here and the colour copy follows. Exactly one
  `<h1>` per screen and no skipped level, in both trees: reading only the copy can pass while the
  original is wrong.
- **Every screen carries its full state set** - loading, empty, error, success, plus whatever is
  particular to it - and the browse screens carry logged-in and logged-out. **A state is a page.**
- **A UI string gets a row in `../voice/docs/microcopy.md` before it ships**, then goes into both
  trees. For one whole stage that was not true and 43 shipped lines had no row.
- **THE BROWSE SHELL WAS MISSING FROM THIS TREE UNTIL 2026-08-13, AND ITS OWN STYLESHEET IS WHAT
  PROVED IT.** `docs/backlog.md` 113. `<!-- /cat-main --><!-- /cat-layout -->` stood in **76 files
  with no opening tag above it**, and 92 files styled `.cat-main { flex: 1 }` and, at the RAIL rung,
  `.subcat { flex: 0 0 210px }`. **Both need a flex parent and the parent was not there**, so the
  sub-category rail had never once stood beside the content in this tree at any width: two flex
  children of a block box. The row could not choose between its two answers by reading, because a
  closing comment with no opening tag is evidence and not proof; **a stylesheet written against the
  missing element is the proof**, and it says the tree lost the wrapper in a port rather than the
  paint inventing an arrangement. Both tags are back in all 76, 33 of them around a rail, with the
  `.cat-layout` rule in the 92 that style its children. Measured after: 104 files at six widths, **0
  horizontal scroll, 0 page errors, and 0 files where a rail that renders is not beside the
  content**. **A grey file cannot hold a token, so every number in it is written as many times as it
  is used**: the harness width moved the same day and cost 312 edits across 104 files for one
  number, which is `docs/backlog.md` 119.

## The contract and the log

`_conventions.md` is the build contract and holds the six differences that ARE the layer boundary
between this tree and the paint: plate wrappers, the icon mechanism, the photograph, chart data, the
`TBD` chip, and the page behind an overlay. `_critique.md` is the defect log, two full critiques and
a flow-wiring audit.

## The generators are gone, and this is the folder that paid for them

`_generators/` held 36 scripts and was deleted on 2026-08-07. The reason is worth keeping: **the
voice rewrite was applied to this HTML by hand and never back-ported**, so re-running any `gen_*.py`
silently reverted it. For two stages the rule was "never run these", which is a tool that must not be
used, which is a tool that should not exist.

**A change to many screens is a throwaway script in the scratchpad, run once and deleted**, with the
sweep described in the commit. What the deleted post-processors did is now done that way: porting a
block back, reconciling the chrome, wiring a flow, resyncing a sidebar.

## Where the record is

`../docs/decisions.md`, and `../ia/docs/` for what a screen is supposed to contain: `sitemap.md`,
`flows.md`, `blocks.md` banked by page type, and `pages/` for the detailed layer.
