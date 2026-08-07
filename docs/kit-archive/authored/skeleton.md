# skeleton

## Sources

- The 19 painted screens that carry it, all of them a loading state: `active-bets-loading`, `event-detail-loading`, the eight `event-feed-*-loading` pairs, `favorites-loading`, `notifications-loading`, `wallet-loading`.
- `voice/docs/microcopy.md` L968 and L1030, where the loading state of a feed and of a detail screen are both recorded as *silent skeleton, no text* with the verdict "Microcopy/loading: silent is correct".
- `ui-kit/_levels.py` STATIC: "the loading mark. It stands where a control will be and is replaced by it".
- `ui-kit/specimens.map.json`, the `card-loading` and `position-loading` entries, whose notes say the loading state is the card and the row rather than a component beside them.
- `components/skeleton.css`, where every rule is written as `.card.skeleton .sk-line` rather than as a skeleton of its own.

## Purpose

The shape of what has not arrived. Five grey marks that stand exactly where the real thing will stand, so a screen that is waiting keeps its layout and a person's eye keeps its place: the card does not jump when the data lands, because the card was already the right size.

It is a MODIFIER, not a component beside the one it replaces. Every rule is scoped under the thing it is standing in for, and the specimen for a loading card is registered to `card` rather than here for the same reason. What this page shows is the vocabulary; where it actually lives is on the component that is waiting.

## Anatomy

- `.sk-line` - a line of text that has not arrived. Width varies by line, because a paragraph of identical bars reads as a table.
- `.sk-head` - the heavier first line, standing in for a question or a title.
- `.sk-thumb` - the block where the event photograph goes.
- `.sk-btn` - the mark where a control will be, so the row keeps its height.
- `.sk-row` - the arrangement of the four above inside one waiting card or one waiting position.

## When to use

Only where the shape is KNOWN before the data is. A feed knows it is about to hold cards, a position list knows it is about to hold rows, an event detail knows its head: those three get a skeleton and they are the only three that have one.

Where the shape is not known, or where the wait is the answer rather than a pause, the screen takes a `state-block` instead: an empty Active bets is not a slow Active bets, and drawing five grey cards for a person who has never placed a bet promises something that is not coming.

It is silent on purpose. No spinner, no "Loading...", no count. That is a copy decision and it is recorded, not assumed: `voice/docs/microcopy.md` marks the loading state of both families as silent and correct.

## Rule

Draw the shape that is arriving and nothing else: a skeleton with more marks than the real thing has parts is a promise the data will break.

## Anti-rule

Never use it for an empty state or an error: nothing is arriving there, and both belong to `state-block`, which has a title, a sentence and a way out.

Seen: `wireframes/_critique.md`, the dead-end finding on the eight category empty screens, which is the same confusion one step further on: a screen that shows a person a shape with no exit. The distinction between "waiting" and "empty" is why those two states are two files.

## States

None, and it is declared: `ui-kit/_levels.py` STATIC says "the loading mark. It stands where a control will be and is replaced by it", so it answers no pointer. Its own animation is the shimmer, which the reduced-motion block in `components/base.css` turns off for the whole system in one place.
