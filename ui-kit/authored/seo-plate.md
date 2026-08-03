# seo-plate

## Sources

- `ui-kit/docs/inventory.md` L88 - "Feed SEO plate (below fold, `.feed-seo-wrap` brand statement)", filed L2, on feed and category pages.
- The 9 painted screens that carry it: the general feed and the four categories, each logged in and logged out. It is absent from every empty, error and loading state of the same screens.
- `CLAUDE.md`, the SEO-ahead decision: the structural layer (URL, H1/H2, breadcrumbs, schema.org, indexation, internal linking) is decided in IA, and the wireframe validates layout only.
- `ia/docs/pages/seo.md`, which owns the H2 this block carries and the query it answers.
- `ui-kit/docs/backlog.md` S3, the row that says no component styles an `a` inside a paragraph, and that the link was moved OUT of the sentence rather than a link style being invented.
- `ui-kit/_levels.py` STATIC, where it is declared "the reading block at the foot of a feed: prose and a brand column, with no link inside it on any of the 105 screens".

## Purpose

The block a feed carries for the reader who arrived from a search engine. Below the fold, after the cards, in prose: what this category is, what a person can do here, and who is saying it. It is the only place on a browse screen where the product speaks in full sentences.

Two audiences, one block. A search engine needs an H2 and body text on the same URL as the cards, or the page is a list of questions with nothing to index. A person who scrolled past forty cards is at the bottom for a reason, and the reason is usually "what is this". Both get the same answer, which is why the block is prose and not a marketing panel.

## Anatomy

- `.feed-seo-wrap` - the plate, below the last card and above the footer.
- `.seo-text` - the body. Two or three paragraphs, and the H2 above them is structural: `ia/docs/pages/seo.md` decides it, not this file.
- `.seo-brand` - the brand column beside the prose.
- `.seo-tagline` - the one line under the mark.
- `.seo-tick` and `.seo-h-ic` - the marks in the brand column and in the heading.
- `.seo-by` - the attribution line, which is what makes the block a statement by somebody rather than an anonymous paragraph.

## When to use

At the foot of a browse screen that has content: the feed and the four categories. Nowhere else, and not on the empty, error or loading variants of the same screens, which is why nine screens carry it and thirty-two do not. A person looking at an empty category does not need a paragraph about what the category is for; they need the way out that `state-block` gives them.

Not on an Event Detail screen. That page has its own prose in `event-detail`, written about one event, and a second block explaining the category would compete with the thing the person came to read.

The heading is not this component's to write. The structural SEO layer is decided in IA before a wireframe is drawn, so the H2 comes from `ia/docs/pages/seo.md` and this file decides only how the paragraph and the brand column sit together.

## Rule

It is prose and it stays prose: no control, no card, no second trust claim, because a block that a person scrolled to the bottom to read has to be readable rather than scannable.

## Anti-rule

Never let a link live inside a sentence here: the system styles no `a` in body prose, so a link in this paragraph renders in the browser's own blue, and the answer the product already chose is a standalone control after the text, the way `related` does it with Browse more events.

Seen: `ui-kit/docs/backlog.md` S3, which is exactly this, found while building the Terms page: no component styles an `a` inside a paragraph, and the link was moved out of the sentence rather than a link style being invented for one block.

## States

None, and it is declared: `ui-kit/_levels.py` STATIC carries the line "the reading block at the foot of a feed: prose and a brand column, with no link inside it on any of the 105 screens". The second half of that line is the reason there is nothing to hover.
