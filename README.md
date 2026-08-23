# Yonder - a prediction market platform

A mobile-first web product where a person bets YES or NO on real-world events using stablecoins.
Outcomes resolve against reality, not against opinion.

**The bet:** better clarity and onboarding than the existing markets. **The audience:** people who
follow the news and are not traders. **The state:** a finished design deliverable and its
documentation. There is no product code yet, and that is deliberate.

---

## Start here

**New to this repository? Open [`handoff/handoff.html`](./handoff/handoff.html).** It is the one page
that replaces an explanation: what you are holding, where to start, how it behaves, what it is made
of, and how to add to it. Everything below is the index it leads into.

| Door | What it opens |
|---|---|
| [`ui-visual/event-feed.html`](./ui-visual/event-feed.html) | **the product**, painted, clickable end to end |
| [`ui-kit/why.html`](./ui-kit/why.html) | **the system**, in five minutes, and what will bite you |
| [`handoff/handoff.html`](./handoff/handoff.html) | **the handoff**, and the route to everything else |

Open any of them straight from disk. There is no build step and no server.

---

## What is in here

Three screen trees and one system. Counted on 2026-08-23; **a count in this file is dated or it is
computed, never typed as a live fact**, because that is the rule this repository has broken most
often and in the files that state it.

| Folder | What it is |
|---|---|
| [`ui-visual/`](./ui-visual/) | **the painted product.** 125 documents, 124 of them screens plus the index of the tree, counted 2026-08-23. Every one links exactly one stylesheet |
| [`wireframes/`](./wireframes/) | **the grey tree.** 124 screens, counted 2026-08-23. Owns structure and copy, links no stylesheet, frozen since the voice pass. Read it once to understand why every screen exists twice, then work in the paint |
| [`components/`](./components/) | **the system.** 49 components reached through one entry file, plus the substrate they stand on. Two token levels and two themes |
| [`ui-kit/`](./ui-kit/) | **the vitrine.** 61 hand-written pages: a shelf per level, a page per component, six foundations. No generators |
| [`handoff/`](./handoff/) | **the handoff.** Behaviour, the map, accessibility, the onboarding gaps, and the prompt for adding a screen |
| [`ia/`](./ia/), [`voice/`](./voice/), [`research/`](./research/), [`user-research/`](./user-research/), [`concept/`](./concept/) | the sources every one of the above was built from, each with its own rendered page |
| [`docs/`](./docs/) | the record, the open list, the build plan, and the first release's markets |

---

## Where each question is answered

Every fact has exactly one owner. When two documents disagree, **the repository is right**: measure
the thing, then believe the file that owns it, then believe the prose.

| Question | File |
|---|---|
| What the product is: job, audience, market types, money, compliance | [`PRODUCT.md`](./PRODUCT.md) |
| The rules of working here, and the reason each one exists | [`CLAUDE.md`](./CLAUDE.md), then the one in the folder you are in |
| What was done and why, dated, never edited | [`docs/decisions.md`](./docs/decisions.md) |
| What is still open | [`docs/backlog.md`](./docs/backlog.md) |
| How it gets built as software: stack, schema, routes, order | [`docs/build-plan.md`](./docs/build-plan.md) |
| Which markets the first release opens, and who resolves each | [`docs/launch-catalog.md`](./docs/launch-catalog.md) |
| Where a file lives | [`STRUCTURE.md`](./STRUCTURE.md) |
| The visual language | [`DESIGN.md`](./DESIGN.md) |
| How the system is architected | [`ui-kit/docs/architecture.md`](./ui-kit/docs/architecture.md) |
| What every component is, its level and its placements | [`ui-kit/docs/inventory.md`](./ui-kit/docs/inventory.md) |
| Where a reader can go | [`ia/docs/sitemap.md`](./ia/docs/sitemap.md) and [`ia/docs/flows.md`](./ia/docs/flows.md) |
| Every word the product says | [`voice/docs/microcopy.md`](./voice/docs/microcopy.md), and [`voice/docs/voice.md`](./voice/docs/voice.md) for which words are allowed |
| **What the product DOES** | [`handoff/docs/behaviour.md`](./handoff/docs/behaviour.md) |
| **If I change this token, what moves** | [`handoff/docs/map.md`](./handoff/docs/map.md) |
| **What is promised about accessibility, and how to check it** | [`handoff/docs/a11y.md`](./handoff/docs/a11y.md) |
| **How to add a screen** | [`handoff/docs/one-shot.md`](./handoff/docs/one-shot.md) |

---

## Status

**This table is the only place a stage status is decided.** It is RENDERED by two registries that
have to be turned by hand with it: [`assets/_roadmap.js`](./assets/_roadmap.js) on the course
documents and [`ui-kit/_nav.js`](./ui-kit/_nav.js) on the stand. A rendered status is the one a reader
sees, so it is the one to turn first: this registry once printed SOON on a stage that had shipped
three days earlier, while three files each said in so many words that a status lives here and nowhere
else.

**The account of how each stage got here is in [`docs/decisions.md`](./docs/decisions.md), dated and
newest first.** This table says what is done and what it produced; it does not retell it, because a
fact written twice drifts and the copy here is the one to delete.

| Stage | Status | What it produced |
|---|---|---|
| Foundation Research | Done | Competitors, benchmark, Lean UX Canvas, AARRR, UX patterns, and the synthesis. [`research/research.html`](./research/research.html) |
| User Research | Done | Personas, the job hierarchy, and the two journey maps. [`user-research/`](./user-research/) |
| Information Architecture | Done | Entities, the screen tree by intent, five user flows traced to jobs, the block bank, the metadata layer and the system nodes. [`ia/`](./ia/) |
| Wireframes | Done | The whole product in grey, every screen and every state its own page, flow-linked end to end. [`wireframes/`](./wireframes/) |
| Voice | Done | Five principles, a lexicon, a forbidden list, per-element rules, and every screen rewritten against them. [`voice/`](./voice/) |
| Concept | Done | The Vault visual language, chosen against three alternatives and locked. [`concept/concept.html`](./concept/concept.html) |
| UI + Visual | Done | Every screen painted, each linking exactly one stylesheet. [`ui-visual/`](./ui-visual/) |
| Tokens + Components | Done | Two token levels, one file per component, a second theme as the proof the roles are real. [`components/`](./components/) |
| Design System | Done | The vitrine rebuilt by hand: a shelf per level, a page per component, zero generators and zero gates. [`ui-kit/`](./ui-kit/) |
| Responsive | Done | Three rungs in `rem`, named by what arrives at them, kept as a registry because a media query cannot read a variable. [`ui-kit/responsive.html`](./ui-kit/responsive.html) |
| Animation | Done | Two durations and a period, every movement naming its job first, and a reduced-motion check that can fail. [`ui-kit/motion.html`](./ui-kit/motion.html) |
| Handoff | In progress, 2026-08-23 | Behaviour, the map, accessibility, and the page that replaces the explanation. [`handoff/handoff.html`](./handoff/handoff.html) |

---

## Published

The repository is served by GitHub Pages from `main` at the root, so every page above opens in a
browser without a clone. **Three addresses, and each one was requested on 2026-08-23 rather than
written from memory**, because a link nobody has opened is a claim and not a route.

| What | Address | Checked |
|---|---|---|
| The repository | <https://github.com/sergiodesign4u-dot/predict-market> | **200** |
| The product | <https://sergiodesign4u-dot.github.io/predict-market/ui-visual/event-feed.html> | **200** |
| The system | <https://sergiodesign4u-dot.github.io/predict-market/ui-kit/why.html> | **200** |
| The front door | <https://sergiodesign4u-dot.github.io/predict-market/> | **404 until the next push**, and it was 404 with no fix pending until this stage: see below |
| The handoff | <https://sergiodesign4u-dot.github.io/predict-market/handoff/handoff.html> | **404 until the next push** |

**The published root was dead, and the cause is worth keeping.** `.nojekyll` sits at the root because
without it Jekyll drops every path beginning with an underscore, which would take `assets/_roadmap.js`
off the course documents and `ui-kit/_nav.js` off the stand: the roadmap panel and the whole kit route
would vanish from the published site while both work perfectly from disk. With Jekyll off, nothing
turns `README.md` into an index either, and there was no `index.html`. So the one address a person is
handed answered 404 while every deep link answered 200. **A route is only a route where somebody has
walked it**, and no instrument in this repository reads an HTTP status, because all of them open files.
`index.html` is the front door now, and it holds no fact of its own.

---

## Working here

Four rules that decide the rest. The full set, each with the measurement that produced it, is in
[`CLAUDE.md`](./CLAUDE.md).

- **New goes into the system first and onto a screen second.** A screen that grows a part every time
  it meets a new page has not been tested by that page, it has been edited by it.
- **A measurement is an act, not a machine.** Walk the screens, write down what was found, decide,
  keep the report. A measurement that becomes a permanent check is re-paid on every later edit.
- **A sweep is a throwaway script.** Write it in a scratch folder, run it, delete it, describe it in
  the commit. A script kept in the repository is a script somebody runs later against a tree that has
  moved on.
- **Reading the source is not reading the page.** A missing value is a value. Measure the computed
  result, in a browser, at the rungs and one pixel either side, in both themes and in more than one
  engine.
