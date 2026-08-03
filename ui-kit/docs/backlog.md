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

---

## Opened by step 7, building Terms of Service (2026-08-03)

Fourteen sections, 1,611 words of body, assembled from `feed`, `notice`, `related`, `button`,
`header`, `footer`, `bottomnav`, `trustbar` and the `browse-shell` pattern. **No new class, no new
token, no new state, no new rule.** The page passes every gate and measures clean in both themes at
360 and 1440, including all 18 tab stops. What follows is what it cost to get there.

| # | What the system does not have | What the screen did instead | The cost, measured |
|---|---|---|---|
| S1 | **A reading measure.** `--container-read` is **800px**, and `.feed-seo` is the only block that reads it | Used it | **792px at 13px is about 122 characters.** `DESIGN.md` section 3 says body prose runs at 60-75ch, so the token and the rule disagree by a factor of about 1.7. The 60ch cap exists in exactly one place, `.feed-seo-wrap .feed-seo p`, a descendant selector inside the feed's SEO plate, so it has only ever applied on the feed. This is the largest single defect on the new page and it is a token, not a layout |
| S2 | **Paragraph rhythm in a prose block.** `.feed-seo p{margin:0}` | Shipped consecutive `<p>` with no space between them | A 14-section document reads as 14 walls. The SEO plate was written for one paragraph per heading and nothing ever asked it for two. Visible in the body screenshot; not measurable as contrast or overflow, which is why no gate saw it |
| S3 | **An inline link style for body prose.** No component styles `a` inside a paragraph | Moved the link OUT of the sentence into a standalone `.related-more` below the box | Measured at **1.8:1** in the browser's own blue before it was moved, and reported by `audit.cjs` as "link with no rule". The product has 992 links and every one of them lives inside a component that styles it; a paragraph is the first place that was not true |
| S4 | **A breadcrumb.** No class, no component, nowhere in `components/` | Block B2 was **not built** | `ia/docs/blocks.md` banks B2 as MVP and `ia/docs/pages/seo.md` section 6 requires `BreadcrumbList` schema for this type. Both are unsatisfied. The five static pages are a SET and a breadcrumb is how a reader learns that |
| S5 | **A sticky table of contents.** The only sticky rail is `.subcat`, whose rows are `<button>` | Contents shipped **in flow**, built from `related` | Two things lost. The desktop sticky position from block B5 (family 2 in the bank), and the semantics: `.subcat` rows cannot be `<a>`, so a contents built on it would not be crawlable, which the same file's own A-E checklist forbids. `related` is a styled anchor list and was used for both the contents and the sibling block |
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

## Older, carried

| # | Item | Where it came from |
|---|---|---|
| S11 | `.app-case .cta-bar button` is styled by `account.css`, not `button.css` | Found by the pattern extraction in step 4, when a bare `<button>` with no class made the class map unable to see the action bar's contents. It is the same species as items 16d and 17 in `docs/backlog.md` and it is listed here too because it is what a person assembling a bar actually hits |
