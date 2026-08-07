# trustbar

## Sources

- `ui-kit/docs/inventory.md` L148 - "Trust bar / trust cards (`.footer-trust`)", filed L2, on feed and footer (all), 87 screens; and L170, "Footer trust strip (Built on trust cards, gold art bleed)", on every footer screen.
- All 105 painted screens carry it, because the footer strip is on every one of them and the feed band is on the browse family.
- `CLAUDE.md`, design principle 2: "Trust is stated, not implied - transparent odds, a named resolution rule, an audit trail, one plain provable sentence rather than borrowed authority."
- `ui-kit/docs/backlog.md` L30, where this component is one of the nine the Terms page was assembled from without a new class.
- `ui-kit/_levels.py` STATIC: "three trust statements. A claim, not a destination".

## Purpose

The product's second design principle, made into a block. This platform asks a person to put real money on an opinion, and the whole argument for doing that is not "we are trustworthy" but "here is how you can check": transparent odds, a named resolution rule, an audit trail. Those three sentences are this component.

It carries no link and no control, and that is the decision rather than an omission. A trust claim that is also a button asks a person to leave the page they were about to act on; a trust claim that is a sentence can be read in the second and a half a person actually gives it. `_levels.STATIC` records it as "a claim, not a destination", and gate 25 holds that both ways.

## Anatomy

- `.feed-trustbar` - the band under a feed, where the claims stand in a row.
- `.trust-head` - the heading of that band.
- `.trust-items` and `.trust-item` - the three claims and their arrangement.
- `.tr-ic` and `.tr-txt` - one claim: its mark and its sentence. The mark is an outline icon and never a badge, because a badge is borrowed authority and a sentence is a claim you can check.
- `.footer-trust` - the same three claims in the footer, on every screen. The strip is quieter than the band, because on a screen that is not a feed it is a reminder rather than an argument.
- `.ft-inner`, `.ft-item`, `.ft-ic`, `.ft-sep` - the footer strip's own row, mark and separator.

## When to use

Where a person is deciding whether this product is one they will put money into. That is two places and the component ships in both: under a feed, where a first-time visitor is still reading, and in the footer, where somebody who has scrolled the whole way is deciding.

Nowhere else, and particularly not on a screen where the person has already decided. A trust strip beside a Confirm bet button is not reassurance, it is a doubt introduced at the worst moment; the bet panel says what will happen to the money instead, which is a fact rather than a claim.

The three claims are the product's, not this component's. Changing what they say is a change to `voice/docs/microcopy.md` and to the argument the product is making, and the component only decides how three sentences stand next to each other.

## Rule

Every claim here has to be checkable by the person reading it: name the resolution source, show the odds, point at the trail, and never write a sentence whose only evidence is that we wrote it.

## Anti-rule

Never turn a claim into a control: if a person is meant to go somewhere, that is `footer` navigation or a `notice` with an action, and a trust claim that clicks is asking for a decision at the moment it is trying to earn one.

Seen: `CLAUDE.md` design principle 2, which states the rule the other way round ("one plain provable sentence rather than borrowed authority"), and `ui-kit/_levels.py` STATIC, where this component's line had to be written because a file with no `:hover` reads identically whether that was decided or forgotten.

## States

None, and it is declared: `ui-kit/_levels.py` STATIC says "three trust statements. A claim, not a destination". Gate 25 fails the build in both directions, so a hover cannot appear here without the declaration being removed first, and removing it would be the decision to make trust clickable.
