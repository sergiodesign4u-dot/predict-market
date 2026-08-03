# card

## Sources

- `ui-kit/docs/inventory.md` L76 and L77 - the binary card (treatment B, 36 screens, states rest / hover) and the multi card (treatment D, 20 screens, "2 leading options").
- `ui-kit/docs/inventory.md` L75 - and this is the row that changes how the file reads: "Two-stone plate / surface system (`.cat-layout`, `.feed-inner` inset plates, notched brass frames, groove edges, trust-column watermark `card::after`)", filed under `components/card.css`, location "every color page (the substrate)". The class is the event card AND the product's general plate.
- `ui-kit/docs/inventory.md` L80 and L81 - the probability figure, and the meta row with its bookmark.
- `voice/docs/microcopy.md` Step 18 - "Feed story-led reconcile: per-card *why* + below-fold SEO sections", which is where `.why` came from and why it is not optional decoration.
- `voice/docs/microcopy.md` Step 24 - `Closes: Sep 1, 2027`, opened as a defect and closed as correct: the colon is a DELIMITER the feed script splits the meta row on into `.m-label` and `.m-val`, so removing it stops the row splitting.
- R5, R7 and R8 in `ui-kit/docs/architecture.md` - two option rows and never the full list, no bet control on a screen that carries cards, and 0 cards on the five system screens.
- `ia/docs/sitemap.md` L315 - the two-option preview rule, and its reason: the meta rows line up across the grid and the feed reads evenly.
- `voice/docs/voice.md`, principle 1 - "Explain the number, never just show it", derived from `research.md:95` and `ux-patterns.md:67`: no competitor explains why the price is what it is. `.why` is that principle at card size.
- The 36 painted screens.

## Purpose

One event, at a glance, repeated down a grid. A photograph, the category, the question, the probability with its bar, one line of why, and the meta row with volume, closing date and the save control.

The line that makes it this product's card rather than a generic one is `.why`. Every competitor puts a percentage on a tile; principle 1 exists because none of them says what is holding it there, and a card without that line is a card from a different product with our colours on it.

## Anatomy

- `.card` - the card, and also the product's plate. See the note at the end of When to use: the same class is the substrate of every painted screen, and that is declared rather than accidental.
- `.thumb` - the event photograph. Content, so it goes on the element as a background image, which is one of the three things gate 9 lets through.
- `.top`, `.top-txt` - the category row above the question.
- `.q` - the question. The whole question, wrapped: this is user-written content and it is never rewritten and never clamped.
- `.prob`, `.prob-line` - the probability figure and the line it sits on. The bar beside it is `oddsbar` and belongs to that file.
- `.why` - the one-line reason the number is where it is. Story-led, per card, added in Step 18.
- `.card-body` - the column the text stands in.
- `.meta`, `.meta-txt`, `.m-label`, `.m-val` - the foot: volume and closing date. The label and the value are separate elements because the feed script splits them at run time, which is why `coverage.md` lists both as built at runtime.
- `.bookmark-btn` - Save, into Favorites. One verb, one shelf, settled in the lexicon.

## When to use

In a grid, on a browse screen, as the repeatable unit. Feed, category pages and Favorites, which is the same feed filtered.

Never with more than two option rows. A multi-outcome card shows the two leading options and says nothing about the rest, and R5 files that as a rule about PLACE: the two-row display is the card's own anatomy, not a smaller version of the detail's list.

Never as a place to bet from. The YES / NO on a card routes to the detail with the side pre-selected, and R7 counts it: 23 screens carry a grid and none of them an amount field or a Confirm.

**And then there is the second job.** `.card` is also the two-stone plate the whole painted product is built on, on every colour page, declared in inventory L75. So two of this component's six photographed faces are not event cards at all: one is the detail head, one is a section plate on the detail column. It works, it is written down, and it means the word "card" in this system answers two questions. A person reading `coverage.md` and seeing 36 screens is reading the EVENT card; the plate is everywhere.

## Rule

Every card carries its why: the figure and the one line that explains it ship together, because a bare percentage is exactly the competitor behaviour this product was specified against.

## Anti-rule

Never let the meta row's controls come from `button`: Save is `.bookmark-btn` and it is a mark that toggles, not a chip that presses, and giving it the quiet control ground would put a filled rectangle in a row whose whole design is that it is the lightest thing on the card.

Predicted: it has not happened here. What HAS happened is the same mistake one level up and in the other direction - `ui-kit/docs/backlog.md` S16, where one quiet button had accumulated five names, and S11, where the action bar's button was painted by `components/account.css` for three stages because the markup was a bare element with no class of its own. `.bookmark-btn` has a class, which is the only reason this one is a prediction rather than a finding.

## States

- `article.card @feed-grid` - The card in a grid, at rest and under the pointer. The whole card answers, the photograph does not move, and the question does not shift: a grid where every card lifts a different amount is a grid that flickers as a thumb crosses it.
- `a.q @feed-grid` - The question, which is the card's real link. All four faces, and the focus ring is the one every screen shares from `base`.
- `button.bookmark-btn @feed-grid` - Save, at rest, hovered, held and focused. The mark fills rather than the ground: it is a state of the event, not a state of a control.
- `article.card.skeleton @skeleton-grid` - The loading card. It stands exactly where the real one will and holds the same height, so the grid does not jump when the data arrives.
- `article.card @card-detail-head` - The same class as the head plate of an Event Detail. Not an event card: the plate.
- `div.card @event-detail` - And the same class again as a section plate inside the detail column. Three of these six faces are the component and three are the substrate, which is the clearest picture in the system of what inventory L75 is saying.
