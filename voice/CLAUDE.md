# voice/ - what the product says

Two documents and one rule. `docs/voice.md` is the contract: five principles, the lexicon (one
concept, one word), the forbidden list, and per-element rules. Every rule there carries an example,
an anti-example and the research line it derives from, so a line comes out the same whoever writes
it. `docs/microcopy.md` is the inventory: every UI string in the product, with its screen.

## The invariants

- **A UI string gets a row in `docs/microcopy.md` before it ships**, then goes into all THREE trees
  that carry it. That table is the source of truth for copy, and for one whole stage it was not: 43
  shipped lines had no row in it, which means the table said the product was smaller than it was.
  **THIS LINE SAID "both screen trees" UNTIL 2026-08-20 AND THAT SENTENCE IS WHY THE STAND WENT
  STALE.** `ui-kit/` carries the product's markup by the two-places rule, so it carries the product's
  STRINGS, and no voice pass has ever been measured over it: backlog 217 turned 217 placements over
  `ui-visual/` and `wireframes/` on 2026-08-19 and **0 in the kit**, which left the stand promising a
  mechanism the product had stopped claiming. Measured across all 61 kit pages against the paint,
  **31 strings on 19 pages** disagreed. A pass that names two trees will be run over two trees.
- **User-written content is never rewritten.** Event questions, comments, usernames and sample
  figures are the product's content, not its interface. Editing them makes the prototype lie about
  what a user would see.
- **One concept, one word.** The lexicon exists because two words for one thing is two things to a
  reader. If a new word is needed, it goes in the lexicon before it goes on a screen.
- **No em dash**, anywhere in this repository.

## Where a change goes

A string changes here first, then in `../wireframes/` (which owns copy), then in `../ui-visual/`.
Three copies of one sentence is the shape this repo has paid for more than once, and the row in the
table is the one that decides.

## Where the record is

`../docs/decisions.md` for why the voice is what it is, `../research/docs/` for the competitor
language the principles were drawn against.
