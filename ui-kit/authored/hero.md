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
- `.hf-cta` - the row that holds Back YES and Back NO. The pair itself is `.yesno` since 2026-08-06 and belongs to `components/yesno.css`; this file had been drawing a second copy of it, and what it keeps now is where the row sits. This is still the only place the verb is written out - the cards keep bare YES and NO.
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

Predicted: R5 in `ui-kit/docs/architecture.md` is the same boundary measured from the other side, and its counter is clean - 161 cards across the painted tree with exactly two option rows each, and `.opt-list` never once inside a card. A clean counter is what a rule of use IS in this repo: the thing that never happened although it easily could have. So this line has no incident behind it and says so.

## States

- `a.hf-title @hero-band` - The featured question, at rest, hovered, held and focused. The type does not move and the photograph behind it does not brighten: the whole block is already the loudest thing on the screen, so the pointer is answered by ink and nothing else. **The answer is the same on `a.hh-name`**, a row of the hot list, and the file already said so twice in its own margin: brass on hover, muted ink held down, at 13px instead of the display step. Size is the one thing a face is deliberately not made of, because splitting on it would put one answer on the page twice. The row moves nothing but its own ink either, so a list of eight does not ripple.
- The featured pair is no longer captured here. It measured as the card's YES / NO pair in every value a face has - `rgba(79,169,107,.12)` on `rgb(63,125,85)` with `rgb(119,209,155)` ink, at 10px and 700 - and its markup was the same shape too, so it went to `components/yesno.css` and its picture is on the yesno page. Two placements took the family's size on the way: 14px to 12, a 40 floor to 44, and the hover from `--outcome-yes-fill-strong` to the 32 per cent mix the other 230 answer with.
- `article.hero-trust @hero-band` - A trust card under the pointer. It answers because the whole card is a link, and it answers quietly, because a claim about trust that lights up under a finger is asking to be clicked rather than believed.
- `a.hh-all @hero-band` - *See all hot events*, the list's exit, in the graphite chip family every other way-out in this product uses.
