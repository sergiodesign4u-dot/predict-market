# hero

## Sources

- `ui-kit/docs/inventory.md` L83 to L87 - five rows for one band: the band itself, the featured market with its `.hf-chart` SVG, the trust cards, the brand tile and the hot-right-now list. All five are marked **UV**, all five have a dash in the screens column, and the count is 2.
- `voice/docs/microcopy.md` Step 24 - "The copy the paint wrote and this table never saw". Eight of the fourteen lines logged there are this component's: `Back YES` / `Back NO`, `Every outcome is public and verifiable.` / `1,284 events resolved on-chain`, `Not just news.` / `Opinions have value.` / `The market decides.`, `Hot right now` / `See all hot events`, `Live odds & volume - last 30 days`, and the eyebrow `Trending now - Politics`, which was opened as a defect and closed as correct.
- `ui-kit/_levels.py` RAISE - the entry that names this component the case arithmetic cannot see: 51 classes, four blocks, and every class its own, so containment reads zero and the map would call it an atom.
- `CLAUDE.md`, design principle 2 - trust is stated, not implied, with one plain provable sentence rather than borrowed authority. The trust cards and the resolved count are that principle drawn.
- The 2 painted screens: `ui-visual/event-feed.html` and its push variant. This is the largest component in the system and it stands on the fewest screens of any organism.

## Purpose

The first screen of the product, and the only block in it that is allowed to make an argument. Four things in one band: a featured event with its own chart and a written-out Back YES / Back NO, two trust cards, a brand tile, and a ranked list of what is moving right now.

It is the answer to a specific problem the rest of the product deliberately does not solve. Every other block here reports: a card states odds, a panel states mechanics, a footer states links. A person arriving from a headline with no idea what this site is needs one place that says what the product is FOR, and this band is it, once, above the grid, and never again.

## Anatomy

- `.feed-hero` - the band, arranged by `.hero-main`, `.hero-side` and `.hero-duo`: the feature on one side, the ranked list on the other, the two smaller blocks paired below.
- `.hero-feature` - the featured event. `.hf-photo` and `.hf-veil` are its photograph and the wash that keeps type readable over it; `.hf-eyebrow` and `.hf-tag` say where you are; `.hf-title` and `.hf-why` are the question and its one-line why.
- `.hf-odds` - the odds. `.hf-odds-row`, `.hf-yes`, `.hf-no` and `.hf-bar` draw the two sides as a proportion, which is the one place in the product that happens outside a card's thin bar.
- `.hf-btn` - Back YES and Back NO, with `.hf-cta` around them. This is the only place the verb is written out; the cards keep bare YES and NO.
- `.hf-chart` - the feature's own plot: `.hf-graph`, `.hf-graph-wrap`, `.hf-area`, `.hf-line`, `.hf-vol-area` and `.hf-vol-line` draw odds and volume over 30 days, and `.hf-chart-cap`, `.hf-chart-legend`, `.hf-info` and `.hf-foot` say what is being measured and over what window.
- `.hero-trust` - a trust card: `.ht-body` the plain sentence, `.ht-badge` the number a person could go and check, `.ht-art` the bleed behind it.
- `.brand-tile` - the brand tile, inside `.hero-promo`. `.bt-photo` and `.bt-veil` are its ground, `.bt-quote`, `.bt-by` and `.bt-tick` the three short claims, and no superlative in any of them.
- `.hero-hot` - the ranked list: `.hh-head` and `.hh-list`, then `.hh-rank`, `.hh-name`, `.hh-prob` and `.hh-vol` per row, ending in `.hh-all`, because every block in this product gives a way out.

## When to use

Once, at the top of the Trending feed, and nowhere else. Its two screens are the reason: a band this size on a category page would push the category's own cards below the fold, and a person who has already chosen Politics has stopped asking what the product is.

Never on a screen a person reached by deciding something. The band argues; a person on Event Detail, My Bets or Wallet has already been argued into the product and needs the screen to answer rather than to persuade.

It is the one component in the system whose absence is normal. 103 of the 105 painted screens do not carry it, and none of them is missing anything.

## Rule

Every claim in it is checkable and every number is the product's own: a trust card with an adjective instead of a figure, or a figure nobody could verify, is the borrowed authority the second design principle exists to keep out.

## Anti-rule

Never let the featured block become a `card` with more paint on it: a card is a repeatable unit in a grid and its YES / NO routes to the detail with a side pre-selected, while this feature is a one-off argument with a written-out verb and a chart of its own. Copying the hero's treatment onto cards would put a thirty-day plot and a persuading verb on every row of the feed.

Seen: R5 in `ui-kit/docs/architecture.md`, which is the same boundary measured from the other side - `.opt-list` never appears inside `.card`, because the card's anatomy is its own and not a smaller copy of the detail. The counter behind that row is 161 cards across the painted tree with exactly two option rows each, against a hero that appears twice.

## States

- `a.hf-title @hero-band` - The featured question, at rest, hovered, held and focused. The type does not move and the photograph behind it does not brighten: the whole block is already the loudest thing on the screen, so the pointer is answered by ink and nothing else.
- `button.hf-btn.yes @hero-band` - **Back YES**, all four faces. This and its pair are the only outcome-coloured controls in the component, and the colour is the outcome's, never the brand's.
- `button.hf-btn.no @hero-band` - **Back NO**, the same four, in the other outcome colour and at the same weight. Neither side is the recommended one.
- `article.hero-trust @hero-band` - A trust card under the pointer. It answers because the whole card is a link, and it answers quietly, because a claim about trust that lights up under a finger is asking to be clicked rather than believed.
- `a.hh-name @hero-band` - A row of the hot list: rank, question, odds, volume. The row moves nothing but its own ink, so a list of eight does not ripple.
- `a.hh-all @hero-band` - *See all hot events*, the list's exit, in the graphite chip family every other way-out in this product uses.
