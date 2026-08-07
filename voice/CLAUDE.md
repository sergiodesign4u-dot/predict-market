# voice/ - what the product says

Two documents and one rule. `docs/voice.md` is the contract: five principles, the lexicon (one
concept, one word), the forbidden list, and per-element rules. Every rule there carries an example,
an anti-example and the research line it derives from, so a line comes out the same whoever writes
it. `docs/microcopy.md` is the inventory: every UI string in the product, with its screen.

## The invariants

- **A UI string gets a row in `docs/microcopy.md` before it ships**, then goes into both screen
  trees. That table is the source of truth for copy, and for one whole stage it was not: 43 shipped
  lines had no row in it, which means the table said the product was smaller than it was.
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
