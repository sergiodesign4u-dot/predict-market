# event-detail

## Sources

- `ui-kit/docs/inventory.md` L98 - "Event head (`.ed-head`: thumb, category, question, big prob, thin `.ed-oddsbar`, actions)", filed L3, states binary / multi, 11.
- `ui-kit/docs/inventory.md` L103, L104 and L105 - the facts strip, the why-this-price arguments (`.args`: a YES column and a NO column) and the resolution block with its `.ed-rules` tabs.
- `voice/docs/microcopy.md` Step 24 - the line this component exists to protect, logged as "the sharpest line of the redesign": **"Background from the Predict Market team to explain the odds. It plays no role in how this market resolves."** And the two tabs it sits between, *Rules* and *Market Context*, "because what decides the outcome and what explains the odds are different promises".
- `voice/docs/voice.md`, principles 1 and 2 - explain the number rather than showing it, and state trust with a named resolution rule and an audit trail rather than borrowed authority. `.args` is the first; `.resolution` is the second.
- `ia/docs/sitemap.md` L84 to L86 - the entity fields this screen renders: "Context / narrative ... key arguments for YES and NO **our differentiator (FJ2)**", "Resolution conditions: what counts as YES, what source is authoritative", and Status.
- `wireframes/_critique.md` L77 - the resolved-detail finding: the resolved body reused the live binary detail verbatim.
- The 11 painted screens.

## Purpose

The parts of an event screen that are the event itself: the head a person lands on, the facts, the two-sided argument about why the odds are where they are, and the rule that will decide it.

The differentiator of this whole product lives in two of those blocks. Every competitor shows a percentage; `ia/docs/sitemap.md` marks the arguments block as the differentiator in as many words, and `.resolution` is the trust principle drawn: a named rule and a named source, before the bet, not after the dispute.

## Anatomy

- `.ed-head` - the head plate: photograph, category, question, the large probability and its thin bar.
- `.ed-thumb` - the event photograph, which is content and rides on the element.
- `.ed-cat` - the category, linking back to where the person came from.
- `.ed-q` - the question. The `<h1>` of the screen, and the one heading level that is decided in the grey tree.
- `.ed-prob-big` - the probability, at the largest size it appears anywhere in the product.
- `.ed-actions` - save and share, beside the head rather than in it.
- `.ed-facts` - the facts strip: the small certainties (closes, volume, type) in one row.
- `.args`, `.arg-col` - the argument, in two columns. YES on one side, NO on the other, at equal width and equal weight, because a layout that gives one side more room has taken a position.
- `.resolution`, `.rules-note` - what will decide this event, and the note that keeps the context tab from being mistaken for it.
- `.ed-section` - a section of the detail column.
- `.resolved-panel`, `.rp-inner` - what the head becomes once the event is settled.

## When to use

On the Event Detail screen, all of it, once. This is not a component a person chooses; it is the screen, minus the parts that belong to `card`, `chart`, `tabs`, `market`, `related` and `betpanel`.

The one real judgement in it is the boundary the rules note draws. Two tabs sit next to each other, one saying what decides the outcome and one explaining why the odds moved, and they are different promises: the first is a commitment, the second is the product's opinion. The note between them exists because a person who confuses the two believes the platform is going to judge the event.

On a resolved event the head becomes `.resolved-panel` and the arguments become history. The critique found the resolved body reusing the live one verbatim, which is worth reading as a warning about this component specifically: a screen assembled from ten blocks resolves the whole screen at once, and any block that keeps speaking in the present tense is now saying something untrue.

## Rule

The rule that resolves the event and the story that explains the odds never share a surface: they are two tabs, and the note between them says the second decides nothing.

## Anti-rule

Never let the mechanics migrate up into this column: how the price is made, what a stake of a given size returns and where the money sits are `market`, collapsed, at the foot, and a spectator must never have to read them. Pulling a depth figure into `.ed-facts` would make the trader's view the default on the screen the product's own description says is not a trader's terminal.

Seen: `ui-kit/docs/inventory.md` L106 files the AMM panel as a separate component with a collapsed state, and `voice/docs/microcopy.md` Step 24 records `.market-title` as *Market* against `.ed-q`, the event's own question, on the same screen. The two vocabularies stand one above the other in one column, and the collapse is what keeps them apart.

## States

- `button @event-detail` - A control in the detail column, at rest, hovered, held and focused. It is the quiet face the whole column shares, so nothing between the head and the resolution block competes with the bet panel beside it.
- `button.ed-act @card-detail-head` - Save and share, beside the head. All four faces, and they stay ghost circles rather than filled chips: the head already carries the largest number on the screen, and two filled controls next to it would read as the thing to do.
