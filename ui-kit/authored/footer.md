# footer

## Sources

- `ui-kit/docs/inventory.md` L68 - "Footer language menu", filed L3, on every footer screen, states "closed / open (TBD)". The TBD is the component's one unfinished thing and it is declared rather than hidden.
- `voice/docs/microcopy.md` Step 16 - "Footer reconcile (trust strip + SEO popular-links, stamped on all 87 footer pages)", and Step 26, "The footer trust block, and the last five strings the paint wrote alone".
- `wireframes/_critique.md`, the Stage-04 reconcile section - "Footer had no trust strip and no SEO internal-linking, and its links were `href=\"#\"`". `wireframes/_generators/footer_reconcile.py` stamped real hrefs, a trust strip, a crawlable "Popular right now" block and a Cookie preferences re-entry onto all 87 footer pages.
- `voice/docs/microcopy.md` L150 to L155 - the placeholder rows: the logo placeholder, the tagline placeholder and the language TBD, all three flagged **placeholder** in the inventory and all three still on the screens.
- `ia/docs/pages/seo.md` - the internal-linking plane this component's popular-links block exists to satisfy, which is why the block is markup and not a widget.
- The 105 painted screens.

## Purpose

The end of every page, doing three jobs the rest of the product cannot. It states trust once more where a person who scrolled the whole way will read it, it links out to the documents and the categories so a crawler can reach them, and it holds the small print - language, legal, social - that has to exist and must not be anywhere else.

The second of those is why the block looks over-built for a mobile-first product. "Popular right now" is not a recommendation feature; it is the internal-linking plane `ia/docs/pages/seo.md` requires, written as real anchors so it works with no script at all.

## Anatomy

- `.app-footer`, `.footer-inner`, `.footer-top` - the block and its stone.
- `.footer-brand`, `.footer-logo`, `.footer-tagline` - the brand column. Both the mark and the line are still placeholders, and `voice/docs/microcopy.md` says so in the inventory rather than in a comment.
- `.footer-cols`, `.footer-col`, `.sub-label` - the link columns and their headings.
- `.footer-popular`, `.popular-links` - the crawlable block of events and categories.
- `.lang-menu` - the language chooser, built on `<summary>`, and the only control here whose contents are TBD.
- `.social-row` - the outward links, as icons with real labels, because an icon with no name is not a link a screen reader can use.
- `.footer-legal`, `.legal-links` - the documents and the line that has to carry them.

## When to use

At the foot of a page a person can finish. It is on 87 of the 105 screens and its absence on the rest is the reason it is worth writing down: an overlay has no foot, because it is a thing a person is inside rather than a page they are at the end of.

Never as a place to put a control that has nowhere else to go. Everything here is either a destination, a document or a setting, and the test is whether a person would look for it after finishing rather than while doing something.

The trust strip in it is a repetition and is meant to be. A person who read the whole page is the person most likely to be deciding, and the same three statements they scrolled past at the top are the ones worth ending on.

## Rule

Every link in it is a real link to a real place: this block is the product's internal-linking plane, and an `href="#"` here is not a placeholder, it is a page that cannot be reached.

## Anti-rule

Never draw its trust strip from scratch: three trust statements in a row are `trustbar`, which is a declared component with its own no-states decision, and a second implementation in this file would be the same claim in two materials, drifting the first time one of them is edited.

Seen: `voice/docs/microcopy.md` Step 26, "The footer trust block, and the last five strings the paint wrote alone", where exactly this block arrived in the footer during the paint and its copy had never been through the table. The strip and the component now share one set of classes; before that step they were two.

## States

- `a @footer` - A link in a column, at rest, hovered, held and focused. Quiet ink that lifts to the strong role under a pointer, no underline until then: a footer with 30 underlined links reads as a wall.
- `summary @footer` - The language menu's opener, all four faces. It is the one control here that opens rather than navigates, and its contents are the declared TBD.
- `a.icon-btn.icon-btn-lift @footer` - **A social link, and since 2026-08-06 it is not this file's control.** It measured as an icon button in every value a face has, so its rules went to `components/iconbtn.css` and its picture is captured here because here is where it STANDS. The four faces answer in the GROUND rather than the mark, because the marks are brand shapes and must not be recoloured; what is left in this file is `.social-row`, one flex line with an 8 gap.
