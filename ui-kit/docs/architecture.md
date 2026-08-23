# System architecture

**The contract of `components/`, written for the person who will build on it.** How the system is
entered, what it is made of, what may be added and what may not. Every number here was measured
against the repository on 2026-08-18 and each says how.

**This is not a second copy of `CLAUDE.md`, and the split is deliberate.** The two `CLAUDE.md` files
in `/` and in `components/` are the ACCOUNT: what went wrong, what it cost, how it was measured, and
the date. They are loaded by whoever edits the repository and they are long because a rule with no
reason gets argued away by whoever meets it next. **This document is the CONTRACT**: the same rules
stated once, short, in the imperative, in the order a person needs them, with a pointer to where
the evidence lives. When the two disagree the repository is right, and the way to check is at the
bottom of this file.

There is no build step and no gate anywhere in this repository. **What you write is what ships.**

---

## 1. Three trees and one system

| folder | what it is | links |
|---|---|---|
| `wireframes/` | 119 grey documents, counted 2026-08-23. Owns STRUCTURE and COPY. A block is decided here first | no stylesheet at all, an inline `<style>` each |
| `ui-visual/` | 120 documents, 119 of them screens and `overview.html` the index of the tree, counted 2026-08-23 | exactly `components/index.css` |
| `ui-kit/` | 61 pages. The vitrine: two entry pages, six foundations, a shelf per level, a page per component | `components/index.css` plus its own `_page.css` |
| `components/` | the system. 56 stylesheets, 11,652 lines: 50 here and 6 in `patterns/` | is the thing being linked |

**A painted screen carries no styles of its own.** Measured by reading every `<link rel=stylesheet>`
in the tree: **119 of the 120 documents in `ui-visual/` link `../components/index.css` and nothing
else**, re-counted 2026-08-23, and the one that links a second file is `overview.html`, which is the index of the tree
rather than a screen in it and borrows the stand's `_page.css` for its own furniture.

**A state is a page**, in both trees. The **seven** differences that ARE the layer boundary between
grey and painted are declared in `wireframes/_conventions.md`, motion being the seventh since
2026-08-15. **This line read as six plus one until 2026-08-23**, which is arithmetically the same
and is read as six by anybody skimming.

---

## 2. The entry point, and the order is the rule

`components/index.css` is the only file a document links. It imports everything, and **a part is
imported before the whole that holds it**, so a rule written later can always out-specify a rule
written earlier without either of them raising specificity.

```
faces first        fonts.css, tokens.css, trust-art.css     values, not parts
substrate          base.css, course-chrome.css              what a screen stands on
level 1, atoms     14 files
level 2, molecules 16 files
level 3, organisms 13 files
patterns           6 files in patterns/
last               print.css
```

`print.css` is last because it re-states selectors every file above it has already written, and the
one that wins is the one that comes last. **Moving a file between groups is a level decision, not a
tidy-up**, and section 8 says what a level is.

**Seven files are not components** and never get a page in the vitrine: `fonts`, `tokens`,
`trust-art`, `base`, `course-chrome`, `index`, `print`. The other 43 here plus the 6 in `patterns/`
are the **49 components**, and every one of them has a page.

---

## 3. Two token levels, and the theme is the proof

`components/tokens.css` holds **370 distinct custom properties in 470 declarations**, in three
sections.

1. **PRIMITIVE.** A raw value with no opinion about where it is used: `--graphite-*`, `--brass-*`,
   `--chalk-*`, `--bone-*`, `--green-*`, `--red-*`, and every geometry scale in section 5.
2. **SEMANTIC.** A colour ROLE: `--bg-*`, `--text-*`, `--border-*`, `--icon-*`, `--outcome-*`.
   **A component reads a role and never a colour primitive.**
3. **THEME.** `:root` and `[data-theme="dark"]` carry the Vault, which is the default and the one
   the product is designed in. `[data-theme="light"]` carries Daylight and re-declares ONLY the
   roles.

**The theme is the proof that the semantic layer is real**, because a second theme can only be
written by re-declaring roles. If a component reads a primitive, the second theme cannot reach it,
and the failure is silent: the component simply keeps its dark colour on a pale ground.

**A page boots its theme from `localStorage` under the key `pm-theme`, and the boot script REMOVES
`data-theme` when the key is absent.** Setting the attribute in a test is therefore not setting the
theme, and any reading taken in both themes needs a control that the page ground actually differed.

---

## 4. States are tokens, and a state token answers in both themes

`:hover`, `:active`, `:focus-visible` and a chosen state each read a token. **A value typed into a
class is a state that exists in one theme only**, and nothing reports it, because the class still
renders.

**A state token has a value in both themes or it is not one.**

**A floor is the family's and is declared once.** Measured from comment-stripped source:

- The focus ring is **one rule** in `base.css`: `:focus-visible{outline:var(--ring) solid
  var(--focus-ring);outline-offset:var(--ring)}`, at `--ring:2px` and `--focus-ring` brass 400 in
  the Vault, brass 700 in Daylight. Eleven other files carry a `:focus-visible` rule and every one
  of them is an EXCLUSION or a shape adjustment, never a second ring.
- The 44px touch floor is **one `@media(pointer:coarse)` block, in `base.css`, and there is exactly
  one in the whole system**. It stood in six files as six lists until 2026-08-08, and what a list
  leaves out nothing says.
- The third floor is motion, and it is a VALUE rather than a rule: see section 7.

**A component speaks up only to be excluded, and an exclusion carries its reason next to it.**

---

## 5. The scales

Geometry comes straight from a primitive. Colour goes through a role. There is no third way.

| scale | steps | values |
|---|---|---|
| `--space-*` | 11 | 2, 4, 8, 12, 16, 20, 24, 28, 32, 40, 56 |
| `--size-*` | 12 | the same eleven plus 72 |
| `--radius-*` | 5 | 2, 6, 10, 16, and `pill` at 100px |
| `--control-*` | 6 | 28, 32, 36, 44, 48, 56 |
| `--icon-*` | 6 | 12, 16, 18, 20, 22, 28 |
| `--text-*` | 10 | 0.625rem to 1.875rem, ten steps, **in `rem` since 2026-08-12** |
| `--display-*` | 9 | `clamp()` ratios to the root, one per named display role |
| `--leading-*` | 6 | 1, 1.05, 1.15, 1.3, 1.5, 1.6 |
| `--weight-*` | 4 | 400, 500, 600, 700 |
| `--track-*` | 8 | -.03em to .1em |
| `--container-*` | **5** | max 1400, read 800, dialog 464, sheet 420, sidebar 220. **It was 6 and `doc 600` is deleted, 2026-08-19**: the reading column of a long document was a container 600px wide holding prose capped again at 409px by `--measure`, which is one question answered twice at two different numbers, and the 191px between them was the ragged edge a reader saw. `.read-col` takes `--measure` itself now, at `--text-16`, so the column IS the measure and every block in it fills it |

Four lengths are named rather than stepped, because each answers one question: `--measure:46ch`
(`ch` is the advance of a zero, not of a character, which is why it is 46 and not 66),
`--grid-col-min:300px`, `--rail-width:214px`, `--menu-min:196px`.

Two ramp rather than step, and they are the reason `card.css` no longer has a width query:
`--gutter` and `--plate-inset` are `clamp()`s that grow from the desk rung to the detail rung. Both
used to STEP at 640, spending 38px a side at the pixel where the window gained one.

---

## 6. The ladder, and a component may not invent a width

**Three rungs, named by what ARRIVES at them**, plus one harness that is not the product's:

| rung | width | what arrives |
|---|---|---|
| DESK | `40rem` | 640px at the default root |
| DETAIL | `47.5rem` | 760px |
| RAIL | `56.25rem` | 900px |
| harness | `1140px` | the review chrome, not the product |

They are in `rem`, so they MOVE with the reader's browser font: a 24px default reaches the desk at
960. **A length in a media query resolves against the INITIAL font size and ignores every
declaration on the root element**, so a test that writes `html{font-size:24px}` is measuring
nothing.

`tokens.css` keeps the ladder as a REGISTRY under `page frame`, and the registry is the instrument:
**`@media` cannot read a `var()`**, so the literal in every query must be a number on the list.
Counted 2026-08-18 from comment-stripped source: **35 width queries in the system, 32 in
`components/` and 3 in `patterns/`**, of which 16 name the desk, 5 the detail, 8 the rail, 2 the
1140 harness, and 4 are one-offs carrying their reason beside themselves. **0 in any of the 110
documents in `ui-visual/`.**

**A rung is one pixel and it belongs to the wide side.** A rung written as a PAIR,
`max-width:640px` and `min-width:640px`, matches on both sides at once and renders a page that
exists at no other width.

**A component asks the WINDOW unless the window and its column move in opposite directions.** There
is exactly **one container query in the system**: `.ed-main` carries the only `container-type`,
declared by `patterns/detail-shell.css` because **place is not a property of a brick**, and
`event-detail.css` asks it at 460px. A container threshold is not a token, because it is local to
one placement, and it is registered in `responsive.md`.

---

## 7. The motion register, and three jobs

**Two durations, not three, and the count is a finding rather than a shortfall.**

| token | value | job |
|---|---|---|
| `--dur-fast` | `.16s` | RESPONSE: a control answering a finger |
| `--dur-slow` | `.25s` | ARRIVAL: an element saying it is here |
| `--pulse-period` | `1.4s` | STATUS: a process still running. A PERIOD, not a rung of the ladder |
| `--ease-standard` | `ease` | |
| `--ease-enter` | `cubic-bezier(.2,.7,.2,1)` | |
| `--motion` | `1` | the amplitude multiplier every travelling distance is written against |

**A moment for which none of the three jobs can be named does not get a movement.** "It feels more
alive" is not a job.

`@media (prefers-reduced-motion: reduce)` re-declares `--dur-fast:1ms`, `--dur-slow:1ms` and
`--motion:0` in `tokens.css`, and a component that reads the tokens obeys without knowing the
setting exists. **There is no blanket `*` net and there will not be one**: under `!important` on
`*`, a component that reads no token is indistinguishable from one that reads every token, so the
net makes the check unable to fail.

**Motion lives in a token, a component or a pattern.** Measured over the trees:
`transition`, `animation` and `@keyframes` stand **0 times in the painted screens** and 0 times
on the 60 kit pages, all 6 `@keyframes` are in `components/`, `transition: all` is **0**, and there
is **one** bare easing keyword, a deliberate `linear` on a longhand in `catnav.css`.

**A `transition` declaration REPLACES the one it out-specifies rather than extending it**, so a
face that re-declares the list drops every property the atom had named. The response belongs to the
CONTROL: one declaration on the atom, carrying the union of everything any face changes.

**A `@keyframes` NAME is document-wide and its DECLARATION is not**, so one written inside a media
query exists at one width only.

---

## 8. Levels, and the stacking order

**A level is a decision, not a reading**, and it is about CONTAINMENT.

| level | rule | count today | where |
|---|---|---|---|
| 1, atom | contains nothing from the system | 14 | `components/` |
| 2, molecule | contains atoms, or its own parts | 16 | `components/` |
| 3, organism | contains molecules, or is a screen shell. This is the ceiling | 13 | `components/` |
| pattern | a composition standing on THREE screens or more | 6 | `components/patterns/` |

Counted 2026-08-18 from the `@import` groups of `index.css` and from the pages of the vitrine,
which agree. **Two screens is a candidate, not a pattern, and it stays markup.**

**A pattern adds no styles of its own, carries no colour, and imports nothing.** The six carry
arrangement only: 56 declarations over 19 properties in 28 rules, and not one colour, face, border
or surface among them.

The paint order is a scale as well, in `tokens.css`, and **no rule may write a raw `z-index`**:

```
--z-under      0   the thing something else is read against
--z-content    1   content lifted above its own decoration
--z-float      2   a frame or a control floating over a card
--z-close      3   the close control on a photographic head
--z-dock       4   fixed furniture at the foot of the window
--z-nav        5   the mobile bottom nav, over the dock it meets
--z-header     6   the sticky app header
--z-menu       7   what opens from the header or the toolbar
--z-chrome-*  8-10 the review chrome, which is not the product
```

**A lift belongs to the box a fade turns into a stacking context, not to the panel inside it.** A
box whose `opacity` is under 1 IS a stacking context, so a panel fading in has its own `z-index`
resolved inside that group rather than against the page, for exactly as long as the fade runs.

---

## 9. Every stylesheet carries a header contract

The first comment of each file is read by a person and by nothing else, and it carries fixed keys:

| key | what it says |
|---|---|
| `Component:` or `Pattern:` | the name, and `Classes:` lists every class the file styles |
| `Reads:` | every token the file reads, complete |
| `Stand:` | the page in `ui-kit/` where the component is taken apart |
| `Stands on:` | how many screens carry it, and the first few by name |
| `Script hooks:` | classes that carry NO rule on purpose, because a page script reads them |

**`Script hooks:` is an allow-list and it is the only licence a class has to draw nothing.** Four
files declare one on 2026-08-18, covering `.ed-chart` and `.ed-chart-multi` in `chart.css`,
`.rules-panel` in `tabs.css`, `.prov-google` in `button.css` and `.filters-close` in `filters.css`.
The last two were moved onto that line the day this document was written: they had been standing in
their file's `Classes:` line, which says the file STYLES them, and neither has a rule. **A class in
the markup that is on no such list and answers to no selector is a defect**, because it falls back
to the browser's own styling, which is a different colour in each engine.

**A `Stands on:` number is a DATED reading, not a property of the component.** The 16 that read 105
were exact when the tree was 105 screens.

---

## 10. Rules of use

The prohibitions, which are the most expensive thing in this document. Each names where the
measurement that produced it lives.

1. **New goes into the SYSTEM first and onto a screen second.** A screen that grows a part every
   time it meets a new page has not been tested by that page, it has been edited by it.
2. **No `@media` in a screen file. Ever.** Adaptation lives in a token, a component, a pattern or
   the shell. `components/CLAUDE.md`, adaptation.
3. **No `transition`, `animation` or `@keyframes` in a screen file. Ever.** Same shape, same
   reason. `ui-kit/docs/motion.md`.
4. **No `style=` on an element.** Three things are not styling and may stay: a datum, the event
   photograph, and a value a page script writes at run time.
5. **No colour primitive in a component.** Read the role. A primitive cannot be re-themed.
6. **No raw `z-index`.** Take a step off the scale in section 8.
7. **No duration or easing literal in a component.** Two durations, a period, two curves, all
   tokens. A `0s` DELAY is not a duration and there is exactly one, in `filters.css`, with its
   reason beside it.
8. **No `transition: all`.** It animates what nobody asked for and drags expensive properties with
   it. Name the properties.
9. **No width a rung does not name.** Three rungs and a harness; a fourth is a decision taken out
   loud with a row in `responsive.md`, not a side effect.
10. **No font from a host.** Every face is served from this repository, and the four the product
    uses are `data:` URIs inside `fonts.css`, because a font request carries a visitor's IP to a
    third party. It is also the only spelling that survives being read from `file://`.
11. **No `opacity` used as a colour.** Quiet is a role. `opacity` fades text into whatever is
    behind it and no contrast reading of the token can see it.
12. **Green and red are OUTCOME semantics, YES and NO. Brass is the brand.** An accent never
    borrows an outcome colour, and a success message is not green here.
13. **Markup goes to two places and only two**: the component's page in `ui-kit/`, and the screens
    in `ui-visual/` where it stands. Never a third copy.
14. **A class in the markup is a promise that a selector answers it**, unless the owning stylesheet
    declares it a script hook in its header.
15. **A state the system styles gets a placement, in both trees, or the styling is a claim nobody
    can test.** A rule that cannot be rendered cannot be checked and will be wrong the day it first
    draws.

---

## 11. How to add a component

Five things, and it is not a component until all five exist.

1. `components/<name>.css`, with the header contract from section 9.
2. An `@import` in `index.css`, **in its own level group**, positioned by what it contains.
3. A page at `ui-kit/<name>.html`: what it IS, its anatomy, every state, and its rule.
4. A row in `ui-kit/_nav.js`, which is the ONE registry of the stand and is edited by hand.
5. A row in `ui-kit/docs/inventory.md`, including the behaviour-on-width column.

**Write the page from the browser, not from the file.** Every page in this vitrine was measured at
390 and 1280 before it was written, and eleven backlog rows were found by the writing.

**A verdict about a component is a statement about the SET of its placements.** A reading taken on
one placement and printed as a property of the component is a fact about a slot wearing the
component's name. Where placements disagree, say so; do not pick one.

## 12. How to add a pattern

Four things, not five, because a pattern has no face to show.

1. `components/patterns/<name>.css`, arrangement only, no colour and no surface.
2. An `@import` in the patterns group of `index.css`.
3. A page at `ui-kit/<name>.html` showing the composition on the screens it stands on.
4. A row in `_nav.js` and a row in the inventory.

**The threshold is three screens and it is counted, not judged.** The pattern declares
`container-type` for anything it PUTS somewhere, because the place is the pattern's knowledge and
not the brick's.

---

## 13. Where a change goes

| what changed | where it goes |
|---|---|
| a value used in more than one place | `tokens.css`, as a primitive or a role |
| how one component looks or behaves | that component's file, and its page |
| how several components sit together on three screens or more | `components/patterns/` |
| how one screen sits | the screen's markup in `ui-visual/`, never a stylesheet in it |
| what a screen SAYS | `wireframes/` first, then `voice/docs/microcopy.md`, then the paint |
| where a reader can go | `ia/docs/`, and the trees follow |
| a rule you had to state twice | `CLAUDE.md`, with the measurement that produced it |

**A ring answers to what it STANDS ON, not to the component it belongs to.** A focus ring, a
divider and a shadow are facts about the surface underneath.

---

## 14. How to check the system without a build

There are no gates. Everything below is an ACT: run it, write down what it said, and delete the
script. A check kept in the repository is a check re-paid on every edit, and that cost this
repository seven days and 145 MB.

- **Read the computed page, never the source.** A missing value is a value: an SVG with no `fill`
  is black, and "0 non-neutral hex in the source" was true while 992 links rendered in the
  browser's blue.
- **Two engines, and `file://` as well as `http://`.** Chromium agreed with a page that was visibly
  broken three times here. Under `file://` every document has its own opaque origin, so anything
  fetched in CORS mode never arrives: a mask, an external `<use>`, a `@font-face` source.
- **Read the instrument before the finding.** Measure the same thing twice unchanged and the
  difference has to be zero. Throw the first pass away: a cold pass resolves fonts and stylesheets
  for the first time and differs from every pass after it.
- **A reading that cannot come back red is a reading of the guard.** Give every sweep a positive
  control it must see.
- **Freeze `transition` and `animation` before any probe that writes CSS**, because injecting a
  stylesheet starts a transition and the value at t=0 is the value the page is leaving.
- **Assert the branch you are measuring is on.** A headless browser is `pointer:fine`, so a
  tap-target sweep without `hasTouch` measures a product with the 44px floor switched off.
- **Measure AT the rungs and one pixel either side**, not at 390 and 1280. A defect can live
  entirely between the two widths everybody reads.
- **Crop the review chrome out.** It is 220 physical pixels and it is inside the frame of every
  full-page comparison taken here.
- **Read the set, not the document.** Three markets were Open on one screen and WON on the tab
  beside it, and 868 renders reported zero, because every instrument reads one document.

---

## 15. What this document does not own

| question | owner |
|---|---|
| what the product is, and the market catalog | `PRODUCT.md` |
| the visual language, and why each decision was taken | `DESIGN.md` |
| what was done, dated, newest first | `docs/decisions.md` |
| what is still open | `docs/backlog.md` |
| which stage is done | the status table in `README.md`, rendered by two registries |
| every component's level, placements and behaviour on width | `ui-kit/docs/inventory.md` |
| the ladder, the audit per screen, the shell fork | `ui-kit/docs/responsive.md` |
| the motion transcript, the moments and the rulings | `ui-kit/docs/motion.md` |
| the system read against the product | `ui-kit/docs/consistency.md` |
| every UI string | `voice/docs/microcopy.md` |
| where a file lives | `STRUCTURE.md` |
| what it cost to learn each rule above | `CLAUDE.md` and `components/CLAUDE.md` |

---

*Written 2026-08-18. It replaces the frozen `docs/kit-archive/docs/architecture.md`, which was true
on 2026-08-07 and whose second half describes 41 build gates and 54 generators that no longer
exist. Nothing reads that file and nothing reads this one either: it is prose, and its only check
is a person opening the repository beside it. Every count here says the day it was taken, because a
count that is typed is a count that goes stale.*
