# Backlog - what is open

Everything decided but not done, and everything not yet decided. One row per item, with the stage
that owns it and where it came from.

**This file is not loaded into a session.** `CLAUDE.md` holds the rules; [`decisions.md`](./decisions.md)
holds the record of what was done. This holds what is not.

Unlike `decisions.md`, this file is edited: a row is struck when the item closes, with the date and
the entry in `decisions.md` that closed it.

**Open: 21.**

The Owner column carries the **new** stage numbers (the project renumbered from thirteen stages to
twelve on 2026-08-02, and an owner is a pointer at work not yet done). The Source column keeps the
number the record was written under, because it cites an entry in [`decisions.md`](./decisions.md)
whose header holds the old-to-new key.

---

## Unread surfaces (3 open, 2 closed)

Not a defect list. No entry here is a known bug; each is a place where a bug would be invisible,
because nothing has ever read it. Written 2026-07-28 after nine audit passes over Stage 09, which
yielded 34, 14, 24, 11, 10, 8, 15, 9 and 20 findings - a sequence that does not decay, which is the
argument that yield tracked unread surface rather than effort. Measurements are from that date.

| # | Surface | Size | Owner |
|---|---|---|---|
| 52 skeleton marks rendering at zero size on 5 loading screens (opened item 20 the same day) | Stage 09 step 13, 2026-08-02 - css only, eight lines of base rules in `skeleton.css`. The markup could not be the fix: a painted screen has a grey twin frozen since stage 04 and gate 18 compares them, so `<span class="sk-line">` stays a span and `display:block` makes it a box. **0 of 482 marks now draw at zero.** Measured on all 19 screens that carry a mark, three widths: 14 of 19 identical to the property, and the 5 that changed are the 5 the item named |
| ~~1~~ | ~~The 28 course pages' own content~~ | 203 KB inline css | **Closed as NEVER**, 2026-08-02: the course frame, not the product, and the one part a reader touches is already out in `course-chrome.css` |
| ~~2~~ | ~~`wireframes/` inline css~~ | 34 `<style>` bodies over 104 pages, largest 52 KB | **Closed as NEVER**, 2026-08-02: the grey tree is frozen and the generators that could act on a finding are the ones `CLAUDE.md` forbids running, so every finding would arrive with "not fixed, by rule" attached |
| 3 | The page scripts as code | 15 distinct bodies in 810 blocks; every sweep reads their output, never the code | Stage 11 (Animation) |
| 4 | What a screen reader is told on change | `aria-live` / `role="status"` on 9 screens of 105 | Stage 09 (Design System) |
| 5 | Page weight, font swap, layout shift | never measured, at any width, in either theme | Stage 12 (Handoff) |

Accessibility was checked before that table was written, because a large hole there would have
changed the answer: **0 buttons without an accessible name** across 105 screens, every `<img>` with
`alt`, native `<dialog>` supplying `aria-modal` and inerting the page, tab strips as radio groups
that arrow keys already drive. The one real gap is the announcement, and a toast is a state, so
Stage 09 owns it.

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

## Design defects deferred (4)

| # | Item | Source | Note |
|---|---|---|---|
| 12 | Live odds-delta animation | `/impeccable critique` P3, 2026-07-16 | Deferred at the time as P3; Stage 11 (Animation) is its natural owner |
| 13 | Error state vs empty state are not differentiated | `/impeccable critique` P3, 2026-07-16 | Two different situations reading as one block |
| 14 | The undeclared second alpha ladder | Stage 09 step 7c, 2026-07-28 | 20 declarations build a colour with `color-mix(in oklab, var(--color-action) N%, ...)` at 16 different percentages, beside the declared `--brass-a*` one. Gate 13 is satisfied (all read a role). Recorded as a decision, not fixed: which steps that ladder should have is a **states** question, and rounding them now would move hover and selected states for the legibility of the file rather than of the product. Stage 09 owns it |
| 21 | Three focus rings that survive the cascade but not the contrast floor | Design System step 1, 2026-08-02 | Found by tabbing every focusable element on 153 pages in both themes and measuring the ring against the ground it stands on, rather than by grepping for `outline:none`. **Nine kinds flagged of 179 measured, and they are three defects.** (a) `.state-btn` and `.state-btn.primary` on the push banner: the ring is `--focus-ring`, which flips to `--brass-700` in daylight, and the banner is a trust-tinted panel, so it lands at **2.72:1** on 3 screens. (b) `.theme-switch-inline` on `ui-kit/overview.html`: the exact mirror of the sidebar defect just fixed. There a flipping role met a fixed ground; here a fixed role (`--chrome-accent`, which section 3 does not override) meets a ground that flips, and it lands at **2.03:1** in daylight. (c) `.kit-field` on `ui-kit/kit.html`, both themes: `outline:none` with a 16 per cent brass wash in its place, which is the same non-indicator the dialog field had. **Not fixed, and (c) is the one that needs a decision rather than a fix:** the rule lives in the inline `<style>` of `kit.html`, which is declared FROZEN provenance, so closing it means breaking a standing rule. The dead copy of the same rule in `ui-kit/_specimen.css` reaches nothing, since no specimen carries the class |

---

## Component boundaries, named and not decided (8)

Found while computing the level of every component from its markup (Stage 09 step 10). Each is a
question about where one component ends and the next begins, and none of them is a defect that
renders wrong today. They are here because the level arithmetic had to work around each one, and a
workaround that is not written down is a workaround that gets re-derived.

Item 16 was one row until the Design System stage's entry gate counted its members on the screens
and found three different jobs inside it. It is 16a to 16d now, because a single row
would have sent a pattern, a candidate and a misplaced class to the same place.

| # | Item | Source | Note |
|---|---|---|---|
| 15 | The how-it-works dialog: fold it in as well? | Stage 09 step 10, 2026-08-02; narrowed 2026-08-02 when `signin` and `outcome-dialog` folded in | Read from the DOM it has the SAME zone set as the shared sheet, zone for zone: a top band carrying the title (`.hiw-hero` for `.sheet-head`), a body, and a close button that is out of flow in both. Nobody in the family has an action row. So the anatomy rule says fold. What holds it back is not anatomy but cascade distance: `hiw-dialog.css` sits at #20 and `dialog.css` at #29, so folding moves **52 rules across nine files**, against four for the two already folded. Two of its shared classes were checked (`.brand-tile` at 0,3,0 beats hero's 0,2,0; every `.ic` rule is scoped under `.hiw-*`), so both known contests are decided by specificity rather than order. That is 2 rules of 52. Decide after the same measurement |

| 16a | Five compositions that are patterns, not component boundaries | Design System entry gate, 2026-08-02 | Counted with the containment reader over the 105 painted screens: `.feed-inner` (feed) on **104** screens, `.cat-layout` and `.cat-main` (catnav) on **76**, `.ed-layout` and `.ed-main` (event-detail) on **11**, plus `.grid` (feed) on **23** and `.pos-list` (position) on **13**. Every one clears the three-screen threshold, so none of them is a question about where a component ends: they are a stable composition living inside a component file, and step 3 of the Design System stage moves them to `components/patterns/`. **The last two are absent from `_levels.SPECIMEN_DEBT`, because they open no gap in the containment map, and that is the point: step 3 counts patterns FROM THE SCREENS, not from the debt list.** A debt list is a list of what distorted a level; a pattern list is a list of what repeats |
| 16b | Two components in one file, still below the pattern threshold | Design System entry gate, 2026-08-02 | `.ptab-panel` (tabs) stands on **2 screens, 6 times**. The threshold is three SCREENS and not three occurrences, so it is both things at once and neither is decided: a component boundary (`tabs` is an L1 switcher and an L3 tab panel in one file) and a pattern candidate waiting for a third screen. It goes on the step-3 "candidates, waiting for the third" list rather than into `patterns/` |
| 16c | A stand page's own class declared in a product component file | Design System entry gate, 2026-08-02 | `.tc-page` (toast) stands on **1 screen**: `toasts.html`, the catalogue of every toast. Neither a pattern (one screen) nor a boundary (there is no second component in `toast.css`), so it is a third kind: the page that DEMONSTRATES a component has its class in the component's own file, which is why the toast reads as containing the cookie banner. It closes by moving the class, not by splitting anything |
| 16d | The five remaining rows that are two components each | Stage 09 step 10, 2026-08-02; narrowed by the Design System entry gate, 2026-08-02 | What is left of the original item 16 once the three above are taken out of it: `card` (binary B is a molecule, multi D an organism), `notice` (six blocks), `position` (row / list / portfolio summary / resolved history), `filters` (menu plus toggle), `account` (CTA bar plus transaction list, and only one of the two has a specimen). These are boundary questions and nothing else: none of them is a composition that repeats across screens |
| 17 | Five classes declared in the wrong file | Stage 09 step 10, 2026-08-02; a fifth added 2026-08-02 | Each distorts the level it feeds: `.pos-status`, a position-list divider, is owned by `profile.css`, which makes `position` an organism through `profile`; `.grid-l`, the CHART's grid line, is declared in `feed.css`, which makes `chart` contain `feed`; `.seg`, a segmented switcher, sits in `tabs.css`, and that is the cycle `_levels.ORDER_BREAK` has to declare by hand. A fourth surfaced on 2026-08-02 and did NOT close with the merge: **`.bet-sheet` is styled by three rules inside `dialog.css`** while the bet sheet is a different component by the same anatomy rule that merged the other two (no top band, no close, a `.sheet-grab` instead), so those three rules belong in `betpanel.css`. The fifth is **`.rp-inner`**, the resolved bet panel's own wrapper, declared in `event-detail.css`: with the panel's resolved state now on the stand it makes `betpanel` read as containing `event-detail`, which is the second hand-written `ORDER_BREAK` this item has cost |
| 18 | `hiw-dialog` is the last level that is declared and not computed | Stage 09 step 12, 2026-08-02 | One of fourteen `RAISE` floors, and after the mechanical revision one of thirteen. Twelve of the thirteen are a component whose parts are all its own classes or a screen shell, which is a reason arithmetic cannot reach. This one is different: the floor is there because **nobody can say what the component IS**. Read from `ui-visual/how-it-works.html`, `.hiw-hero` and `.hiw-cols` are blocks of the standalone PAGE, five levels under `div.app-case` and inside `main.feed`, while the narrow shared sheet hangs under `body` as a separate closed `<dialog>`. Two components on one vocabulary, which is item 16. Until they are split, a specimen showing either one is a choice and not a reading, so the stand was deliberately left alone. **Splitting it removes the floor**, and it is the only one of the thirteen that a split would remove |
| 19 | `.fine` is a typographic role, not a part of the dialog | Stage 09 step 12, 2026-08-02 | The small print. `dialog.css` is the only file that writes it, so the ownership map gives it to `dialog`, and it stands on **246 elements** across dialogs, bet panels, spinner boxes and reconcile boxes, three of which `dialog.css` styles by name (`.app-case :is(.bet-panel,.bet-sheet) .fine`, `.app-case .spinner-box .fine`). The consequence is measurable: with the reconcile box on the stand, `notice` reads as containing `dialog` and moves L2 -> L3, the third `ORDER_BREAK` of the day. It is the same species as `.sel` in `_levels.SHARED` (a word no component owns) but not the same evidence, because `.sel` is written by six files and this by one. Deciding it means deciding whether a typographic role is a component at all, which is a **states and roles** question and therefore Stage 10's |

---

## Closed

| Item | Closed by |
|---|---|
| Self-hosting the three font families (opened step 7b as "an open decision, not a silent default") | Stage 09 step 8, 2026-07-28 - 18 woff2 in `assets/fonts/`, gate 20 |
| The bottom sheet on mobile shipping only in the grey tree (recorded step 7e as a product decision) | Stage 09 step 8, 2026-07-28 - `:modal` geometry under 640px |
| The win overlay h2 clipped to "u were right" (found in step 6b, logged for step 7) | Stage 09 step 7, 2026-07-27 - `overflow:clip` on thirteen stones |
| The dialog family, for `signin` and `outcome-dialog` (opened as item 15) | Stage 09 step 11, 2026-08-02 - folded into `dialog.css` as variants. 36 components, and the 4 rules land at the END of the file because two of them tie `dialog.app-dialog:modal` on specificity. 0 of 15,585 measured elements moved |
