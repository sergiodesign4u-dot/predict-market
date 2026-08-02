# Backlog - what is open

Everything decided but not done, and everything not yet decided. One row per item, with the stage
that owns it and where it came from.

**This file is not loaded into a session.** `CLAUDE.md` holds the rules; [`decisions.md`](./decisions.md)
holds the record of what was done. This holds what is not.

Unlike `decisions.md`, this file is edited: a row is struck when the item closes, with the date and
the entry in `decisions.md` that closed it.

**Open: 17.**

---

## Unread surfaces (5)

Not a defect list. No entry here is a known bug; each is a place where a bug would be invisible,
because nothing has ever read it. Written 2026-07-28 after nine audit passes over Stage 09, which
yielded 34, 14, 24, 11, 10, 8, 15, 9 and 20 findings - a sequence that does not decay, which is the
argument that yield tracked unread surface rather than effort. Measurements are from that date.

| # | Surface | Size | Owner |
|---|---|---|---|
| 1 | The 28 course pages' own content | 203 KB inline css, unread (step 9 took only the panel) | now, or never |
| 2 | `wireframes/` inline css | 34 distinct `<style>` bodies over 104 pages, largest 52 KB; gate 14 was narrowed away from it in step 7e | now, or never |
| 3 | The page scripts as code | 15 distinct bodies in 810 blocks; every sweep reads their output, never the code | Stage 12 (Animation) |
| 4 | What a screen reader is told on change | `aria-live` / `role="status"` on 9 screens of 105 | Stage 10 (Design System) |
| 5 | Page weight, font swap, layout shift | never measured, at any width, in either theme | Stage 13 (Handoff) |

Accessibility was checked before that table was written, because a large hole there would have
changed the answer: **0 buttons without an accessible name** across 105 screens, every `<img>` with
`alt`, native `<dialog>` supplying `aria-modal` and inerting the page, tab strips as radio groups
that arrow keys already drive. The one real gap is the announcement, and a toast is a state, so
Stage 10 owns it.

---

## Product research not done (5)

Carried since the project brief; none of it has been answered.

| # | Question | Why it blocks something |
|---|---|---|
| 6 | Commission rates across competitors | The business model is "commission per bet" with the % still TBD |
| 7 | Min / max bet limits | Launch position is "no limits"; Polymarket uses a $0.01 minimum and the reason is unknown |
| 8 | KYC thresholds | Required for fiat deposits; crypto-only users undecided (Polymarket operates without KYC for crypto) |
| 9 | Blockchain / chain selection | Ethereum vs Polygon vs Base vs Arbitrum; picked on fees, and nothing has been measured |
| 10 | AMM mechanism specifics | The payout rule ("payout depends on when the bet was placed") is stated but not specified |

---

## Product decisions deferred (1)

| # | Item | Note |
|---|---|---|
| 11 | Resolution mechanics for recurring markets | Markets are one-time or recurring (Hourly / Daily / Weekly / Monthly) and the Frequency filter ships on the feed, but how each cadence instance resolves on its own schedule is unwritten. See `ia/docs/sitemap.md`, Event entity |

---

## Design defects deferred (3)

| # | Item | Source | Note |
|---|---|---|---|
| 12 | Live odds-delta animation | `/impeccable critique` P3, 2026-07-16 | Deferred at the time as P3; Stage 12 (Animation) is its natural owner |
| 13 | Error state vs empty state are not differentiated | `/impeccable critique` P3, 2026-07-16 | Two different situations reading as one block |
| 14 | The undeclared second alpha ladder | Stage 09 step 7c, 2026-07-28 | 20 declarations build a colour with `color-mix(in oklab, var(--color-action) N%, ...)` at 16 different percentages, beside the declared `--brass-a*` one. Gate 13 is satisfied (all read a role). Recorded as a decision, not fixed: which steps that ladder should have is a **states** question, and rounding them now would move hover and selected states for the legibility of the file rather than of the product. Stage 10 owns it |

---

## Component boundaries, named and not decided (3)

Found while computing the level of every component from its markup (Stage 09 step 10). Each is a
question about where one component ends and the next begins, and none of the three is a defect that
renders wrong today. They are here because the level arithmetic had to work around all three, and a
workaround that is not written down is a workaround that gets re-derived.

| # | Item | Source | Note |
|---|---|---|---|
| 15 | The dialog family: four files or one with variants | Stage 09 step 10, 2026-08-02 | `signin.css` (2 own classes) and `outcome-dialog.css` (1) have the same zone set as `dialog.css`, so by the anatomy rule they are variants, not components. `hiw-dialog.css` (17 own classes) is the doubtful one: same skeleton, every zone renamed, and the action row is gone, which the same rule reads as a different component. `notice.css` / `toast.css` do NOT merge, and the finding there is the reverse: `notice.css` is six unrelated blocks in one file |
| 16 | Seven rows that are two components each | Stage 09 step 10, 2026-08-02 | A row that lands in two levels at once is the signal. `card` (binary B is a molecule, multi D an organism), `tabs` (an L1 switcher and an L3 tab strip in one file), `catnav` (a nav band plus the `.cat-layout` page plate), `notice` (six blocks), `position` (row / list / portfolio summary / resolved history), `filters` (menu plus toggle), `account` (CTA bar plus transaction list, and only one of the two has a specimen) |
| 17 | Three classes declared in the wrong file | Stage 09 step 10, 2026-08-02 | Each distorts the level it feeds: `.pos-status`, a position-list divider, is owned by `profile.css`, which makes `position` an organism through `profile`; `.grid-l`, the CHART's grid line, is declared in `feed.css`, which makes `chart` contain `feed`; `.seg`, a segmented switcher, sits in `tabs.css`, and that is the cycle `_levels.ORDER_BREAK` has to declare by hand |

---

## Closed

| Item | Closed by |
|---|---|
| Self-hosting the three font families (opened step 7b as "an open decision, not a silent default") | Stage 09 step 8, 2026-07-28 - 18 woff2 in `assets/fonts/`, gate 20 |
| The bottom sheet on mobile shipping only in the grey tree (recorded step 7e as a product decision) | Stage 09 step 8, 2026-07-28 - `:modal` geometry under 640px |
| The win overlay h2 clipped to "u were right" (found in step 6b, logged for step 7) | Stage 09 step 7, 2026-07-27 - `overflow:clip` on thirteen stones |
