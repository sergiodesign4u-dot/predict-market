# The previous kit, kept for its reasoning and read by nothing

The vitrine that stood in `ui-kit/` was deleted on 2026-08-07: 65 generated pages, 54 Python
scripts, 9 browser scripts, 41 build gates, a state-capture instrument and 145 MB of screenshots.
The reason is in `CLAUDE.md` and in `docs/decisions.md`, and the short version is that the
measurement had become a machine that had to be re-paid on every edit, so a one-line change to a
stylesheet cost a regeneration, a re-capture, 41 gates, 525 snapshots and an audit.

**What was deleted is the instrument. What was kept is the product**: `components/` (51
stylesheets, unchanged), `ui-visual/` (106 painted screens), `wireframes/` (104 grey screens),
and the stage documents in `ia/`, `voice/`, `research/` and `concept/`.

**What is in this folder is the writing.** It is the part of the previous kit that cost thinking
rather than compute, and it is the input to the rebuild rather than a record of it.

| | |
|---|---|
| `docs/` | eight documents: `architecture.md`, `atoms.md`, `inventory.md`, `backlog.md` (51 rows, 28 closed), `defects.md`, `history.md`, `coverage.md`, `tokens-audit.md` |
| `authored/` | forty eight per-component pages: what each component IS, its rule, its anti-rule, and what was measured about it |

**Nothing reads these files.** No generator, no page, no check. They are prose, and the four
things worth taking out of them into the new kit are named here so the next reader does not have
to re-derive them:

1. **The level formula.** A component's level is one plus the highest level of what it contains,
   read out of the specimen DOM rather than out of a name. `atoms.md` has the reasoning and the
   list of what could not be read that way.
2. **S34, the size measurement.** 9,648 readings over all 105 painted screens at two widths: 66
   distinct faces of one kind of control, 17 paddings, 22 rendered heights, 7 font sizes, 4
   weights. That table is what the consolidation pass decides against, and it does not need to be
   taken again.
3. **The rule and anti-rule per component**, in `authored/`. Every one of them was written against
   the component as it actually renders, and each names the component that should have been used
   instead.
4. **The defects.** `defects.md` is a list of things that were true and looked fine, which is the
   only kind worth carrying forward.

Dated 2026-08-07. If a claim here disagrees with the repository, the repository is right: these
documents were true on the day they were written and nothing has kept them true since.
