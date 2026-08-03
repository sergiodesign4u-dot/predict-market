# The system backlog

What the SYSTEM is missing, as opposed to what the product has not decided. The product's open
questions are in [`docs/backlog.md`](../../docs/backlog.md); this file holds the gaps a person hits
while assembling a screen out of `components/` and `components/patterns/`.

**It exists because of one rule and one test.** The rule is that nothing is added to the system in
the middle of building a screen: a missing component, state, token or microcopy line becomes a row
here and the screen is assembled from what is already there. The test is step 7 of the Design System
stage, which built `ui-visual/terms.html`, the first page of a TYPE the system had never drawn. A
system that grows a part every time it meets a new page has not been tested by that page; it has
been edited by it.

Every row says what was missing, what the screen did instead, and what the substitute cost, measured
where a measurement was possible.

**Standing today: fourteen rows opened, three closed, eleven open.** The three closed the same
afternoon they were written, and by the same fix, because they were one gap seen from three sides:
the system had no reading layout. Of the eleven that remain, S9 and S12 are answers rather than
gaps and S14 is a carried finding, so the real count is **eight**, and they belong to stages 10 to
12 rather than to this one.

---

## Opened by step 7, building Terms of Service (2026-08-03)

Fourteen sections, 1,611 words of body, assembled from `feed`, `notice`, `related`, `button`,
`header`, `footer`, `bottomnav`, `trustbar` and the `browse-shell` pattern. **No new class, no new
token, no new state, no new rule.** The page passes every gate and measures clean in both themes at
360 and 1440, including all 18 tab stops. What follows is what it cost to get there.

**Then the cost was paid, in the system.** S1, S2 and S5 were fixed the same day and the screen was
rebuilt onto the result by changing CLASSES and nothing else: `components/toc.css` is a new
component, `components/patterns/browse-shell.css` grew a reading column and learned that its rail is
a SLOT rather than a category rail, and `components/tokens.css` gained one primitive. `terms.html`
carries no style of its own, which was the test of whether the fix was in the right place. **Nothing
else in the product moved: 104 screens at two widths, 84,836 element boxes compared against the
previous stylesheet, 0 moved.**

| # | What the system does not have | What the screen did instead | The cost, measured |
|---|---|---|---|
| ~~S1~~ | ~~A reading measure~~ | **CLOSED 2026-08-03** by the reading layout | The number in the original row was wrong and is corrected here: 792px holds **89 characters**, not 122. `1ch` of the 13px prose face measures **8.89px** in the browser, and the first figure came from the 0.5em rule of thumb instead of the browser. Both are over the 60-75 `DESIGN.md` decided, so the finding stood, but a measured row may not carry an estimated number. Closed by `--container-doc` (600px, a NEW primitive beside `--container-read` rather than a correction of it, because that one is a two-column plate on ten feed screens and moving it would change ten shipped pages to fix one) and by `.read-col` reading it. **Measured after: 592px, 67 characters.** |
| ~~S2~~ | ~~Paragraph rhythm in a prose block~~ | **CLOSED 2026-08-03** by the reading layout | Two levels, and both are owned by a CONTAINER rather than by a block, which is the whole point: a margin on `.feed-seo` would be a fact about that block, so the next block dropped into the stack would arrive with no distance again. `.read-col` gives 16px between the fourteen blocks and resets their own vertical margins; `.read-col .feed-seo` gives 8px between paragraphs inside a section. The diagnosis that found it is worth keeping: the chain declares its rhythm once, in `base.css` on `.feed-inner`, and on this page `.feed-inner` had **one child**, so the declaration reached nothing |
| S3 | **An inline link style for body prose.** No component styles `a` inside a paragraph | Moved the link OUT of the sentence into a standalone `.related-more` below the box | Measured at **1.8:1** in the browser's own blue before it was moved, and reported by `audit.cjs` as "link with no rule". The product has 992 links and every one of them lives inside a component that styles it; a paragraph is the first place that was not true |
| S4 | **A breadcrumb.** No class, no component, nowhere in `components/` | Block B2 was **not built** | `ia/docs/blocks.md` banks B2 as MVP and `ia/docs/pages/seo.md` section 6 requires `BreadcrumbList` schema for this type. Both are unsatisfied. The five static pages are a SET and a breadcrumb is how a reader learns that |
| ~~S5~~ | ~~A sticky table of contents~~ | **CLOSED 2026-08-03, in full**, by `components/toc.css` | All three halves of block B5 now exist: anchored rows that are real `<a>` (so the internal-linking plane in `seo.md` section 6 is satisfied), sticky at 214px from 900px up, and collapsed above the body on mobile. The last one was built open first to test whether the bank was being cautious, and it was not: at 360 the fourteen rows pushed the document's own H1 entirely below the fold. **One thing in it is not driven:** `.toc-link[aria-current="true"]` is styled and nothing sets it at run time, because marking the section a reader is inside is a scroll position, which is Stage 11's question and not B5's |
| S6 | **A neutral page-level callout.** Nothing says "read this before the page" without a meaning attached | Used `.spinner-box` for the prototype marker, `.reconcile-box` for the effective dates and `.protect` for the money answer | Three blocks are wearing a component named for something else: a loading placeholder, a price reconcile and a funds-protection line. It renders correctly and it reads correctly, and the class names now lie on this page. That is a naming debt, not a paint defect |
| S7 | **A prominent trust paragraph.** `.protect` is fine print at **11px** | Used it for block B7, the money answer | B7 is the differentiator of this page type: the bank puts it above the contents because our two closest competitors score 1 of 5 on the funds question. It is now the smallest text in the document. The block is in the right PLACE and the wrong SIZE, and there is no larger variant |
| S8 | **Microcopy for a document page.** `voice/docs/microcopy.md` has no rows for this type | The six labels shipped as document CONTENT, not as interface strings, and none was added to the table | The six: `On this page`, `The other documents`, `Last updated`, `Effective ...`, `What changed`, `A question about this document`. `CLAUDE.md` says a UI string gets a row before it ships; these are headings inside a document rather than control labels, which is the reading that let the page ship, and it is a reading a second static page will test |
| S9 | **A registered slug.** `seo.md` gives `/legal/terms`; the painted tree is flat | The file is `ui-visual/terms.html` | Not a defect, recorded so the two are never taken for a disagreement. The slug is production's answer and the filename is the prototype's, the same split every screen in this tree already has |

### What did NOT need anything, and is worth saying

Six of the ten MVP blocks landed with no substitute at all: the header in its logged-out variant
(B1), the H1 (B3), the document sections (B6), the sibling documents (B9), the contact line (B10),
and the footer plus bottom nav (B11). The two-stone plate, the display face, the groove between
sections, the theme, the focus ring and the four bottom-nav slots all arrived by linking one
stylesheet. **The shell of a page type the system had never seen cost nothing.** Everything in the
table above is about the BODY of a long document, which is the one thing this product had never
asked for.

### The two LATER blocks, not built and not forgotten

B12 (download / print) and B14 (region note) are marked LATER in the bank, so their absence is a
plan and not a gap. B13 and B20 were refused by the bank's own rule 1 and are recorded there.

---

## Opened by step 7, in the instrument

| # | What was wrong | Where it is now |
|---|---|---|
| S10 | **A gradient is not a background-colour.** `ground()` composites `backgroundColor` up the ancestor stack, and an element painted with `background-image:linear-gradient()` computes `backgroundColor` to transparent, so the walk went straight past it and measured the label against what was BEHIND the button | Fixed in `ui-kit/_verify/browser.cjs` as lesson 8, with the case that produced it. `.auth-btn.primary` reported **1.18:1** and the flat `.cta-bar` button **1.05:1** against a brass gradient that actually measures about 5.5:1. Both false, both on a page that has shipped for two stages. Marked UNMEASURABLE rather than failing, the same answer lesson 7 gave for `mix-blend-mode`. Checked against a known real defect afterwards: `ui-kit/overview.html` still reports its 3.51:1 |

---

## Opened by the pinned-box check (2026-08-03)

Lesson 9 of `ui-kit/_verify/browser.cjs` was written for one rail and found three, then two more
things worth writing down. What it looks for: a `sticky` or `fixed` box that needs more window
height than `SHORTEST_VIEWPORT` (640px, the 1366x768 laptop less its browser chrome) and has no
scroll of its own. The three rails are fixed; these are what the fix left behind.

| # | What the system does not have | Where it stands |
|---|---|---|
| S12 | **One place that says how far a rail clears the chrome.** `top:120px` is typed into three components: `catnav.css` `.subcat`, `betpanel.css` `.bet-panel` and, until today, `toc.css` `.toc` | **It cannot be derived, and the system has already decided that.** The number is the app header (59px) plus the condensed category strip (54px, `header.css:126`) plus 7px of air, and neither of the first two is a token: the strip is a literal in `header.css`, and the header's 59px is CONTENT height, so no token could hold it. `ui-kit/docs/architecture.md` line 121 already rules this case out of the scale in words: "a number is a step only up to 64px; above that it is a layout position and it stays literal". So it stays literal, and this row is the reason rather than a comment beside each copy. What the row is FOR: the three copies can drift, and today they were already meant to differ. `.toc` is now 66px because a document page has no category bar for the strip to condense, which was measured and not assumed |
| S13 | **A specimen frame is a window, so a component capped to the window caps inside it.** | The vitrine sizes each `.ck-frame` to its content and the content now sizes itself to the frame, which settles (four identical loads agree) but settles SHORT: the `catnav` rail specimen went 499px to 430px and the `betpanel` one 554px to 516px, so the vitrine shows those two components with their feet behind an internal scroll. It is truthful, since a frame that size IS a short window, and it is a worse showcase. The answer belongs to the vitrine (a declared height for a rail specimen), not to the component, which is why nothing was changed in `components/` for it. 25 snapshots across 5 pages, no product screen among them |
| S14 | **`--outcome-no` on a card is 4.35:1**, against a 4.5 floor | Found by the same product-wide run, on every feed card that carries a NO percentage: `span.l-no` in `oddsbar.css:14`. Pre-existing and nothing to do with this pass, recorded here because a finding that is seen and not written down is a finding that gets found again. It is 0.15 under, so it is a token value question and not a layout one, and `DESIGN.md` owns the answer |

---

## Older, carried

| # | Item | Where it came from |
|---|---|---|
| S11 | `.app-case .cta-bar button` is styled by `account.css`, not `button.css` | Found by the pattern extraction in step 4, when a bare `<button>` with no class made the class map unable to see the action bar's contents. It is the same species as items 16d and 17 in `docs/backlog.md` and it is listed here too because it is what a person assembling a bar actually hits |
