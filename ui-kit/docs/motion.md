# Motion - what moves, what job it does, and the two numbers it does it in

Written 2026-08-15, Animation stage. The transcript is measured, not remembered: every number
below was taken on that date from the comment-stripped source and from computed style in a
browser, and the two halves are reported separately because they disagree in one place that
matters.

**Two durations, not three, and the count is the finding.** The stage asks for three, named by
job. The inventory of moments found two jobs with movement in them. The third is a decision
somebody takes out loud on the day a row asks for it, not a rung written in advance.

---

## 1. The transcript, source half

Four corpora, and the fate of each is different.

| corpus | files | `transition` | `animation` | `@keyframes` | duration literals | `transition:all` | expensive props |
|---|---|---|---|---|---|---|---|
| **system** `components/` | 54 | 32 | 3 shorthand + 3 longhand | 3 | **2**, both `.01ms` | **0** | **8** |
| **paint** `ui-visual/` | 106 | **0** | **0** | **0** | **0** | **0** | **0** |
| **stand** `ui-kit/` | 58 | 1 | 0 | 0 | 2, both `.15s` | 0 | 0 |
| **grey** `wireframes/` | 105 | 105 | 0 | 0 | 105, all `.2s` | 0 | 0 |

**The stage's most expensive trap was already shut and no rule said so.** Motion in a screen
file: 0 of the 106 documents in `ui-visual/`. The pack argues that ban pays for itself at
Rollout, when twenty subagents each invent a duration. Rollout already happened here, so the
payment has been collected and the rule was never written down. It is written now, in
`components/CLAUDE.md`, and what it protects is the tree that already stands.

**The stand's `.15s` reaches one document of the painted tree.** `ui-visual/overview.html` links
`ui-kit/_page.css` as well as `components/index.css`, and it renders 114 elements at `.15s`.
That document is the index of the tree rather than a screen in it, which is the same 106-versus-105
distinction every count in this repository has to declare. **105 of 105 painted SCREENS render
zero duration literals.**

**The grey tree has exactly one moving thing**, `transition: transform .2s ease` on the
navigation drawer, in all 105 files, and 0 `@keyframes`. It is not ported and not tokenised: a
grey file links no stylesheet, so it cannot hold a token, and its drawer moves so the tree can be
clicked through. See section 8.

### The instrument caught itself twice before the number was believed

A naive count of the string `transform` in the grey tree returns 2,263, of which **1,750 are
`text-transform: uppercase`**. A naive count of `animation` returns 14 and the number of real
`animation` declarations is **0**: the rest sit inside words and prose. Both counts were taken
again with the property boundary anchored.

---

## 2. The transcript, output half

The half that matters, because a stylesheet says what was written and a browser says what
renders. 163 documents, Chromium 151 and WebKit 26.5, normal and `reduce`, **652 page loads**.

**Positive control first, in each of the four combinations.** An element carrying
`transition: opacity 1234ms linear` and `animation: __nope__ 4321ms linear 3` was injected and
read back before any page data was believed: `1.234s / 4.321s / 3` in the normal pass and
`1e-05s / 1` under `reduce`, in both engines. **4 of 4.** The probe moves when the input moves.

**The product, 105 painted screens: 4,904 moving elements, and the two engines agree element for
element.**

| rendered duration | slots | rendered easing | slots |
|---|---|---|---|
| `.16s` | 9,528 | `ease` | **12,821** |
| `.12s` | 2,346 | `cubic-bezier(.2,.7,.2,1)` | 585 |
| `.18s` | 743 | | |
| `.3s` | 636 | | |
| `.25s` | 63 | | |

### The three headline numbers

1. **Five distinct durations, and not one of them a literal.** The ladder was already tokenised
   before this stage opened. The question was therefore never "reduce eight loose numbers to
   three"; it was whether five roles exist to spend five numbers on.
2. **Two rendered curves, and 95.6 per cent of the slots read no token.** 12,821 of 13,406
   easing slots are the bare keyword `ease`, typed out 54 times in the source and defaulted the
   rest. **This is where the drift was**, not in the durations. One of the two declared curves,
   `--ease-inout`, renders 0 times in the product: its single reader is the review harness.
3. **Eight expensive properties, zero `transition:all`, zero `will-change`.** The eight are
   `box-shadow` five times (`button`, `card`, `hero`, `iconbtn`, `input`), plus `max-height` in
   `header`, `width` in `hiw` and `left` in `toggle`. The last three make the browser lay the
   page out again on every frame. They go to step 5 by name.

### One role wearing four numbers

Grouping by job is what finds this; reading the files does not.

| the same job, hover and press | duration today |
|---|---|
| `.btn`, `.chip`, `.yesno`, `.icon-btn`, `.amount-input`, `.market-head`, `.rules-tab` and 11 more | `.16s` |
| `.btn-provider` transform, `.filter-panel li label` | `.12s` |
| `.icon-btn-photo`, `.icon-btn-lift`, `.related-more`, `.ptab-lbl`, `.chart .ml-line` | `.18s` |
| `.hero-trust`, `.hero-feature` | `.25s` |
| `.card` | `.3s` |

A hover is 160ms on a button and 300ms on a card, in one product. This is the stage's textbook
defect and it was here in the textbook's own shape.

### Two animations do not render on load, and that is a fact about the probe

`sheet-rise` and `betSheetUp` returned 0 across all 163 documents, because **0 of the 105
screens ship an open `<dialog>`** and the state is opened by script. Recording that zero would
have been recording the sweep. They were opened with `showModal()` and read again:

| | duration | under `reduce` | fill mode | placements |
|---|---|---|---|---|
| `sheet-rise` | `.25s` | `1e-05s`, by the net | `both` | 337 dialogs on 105 screens |
| `betSheetUp` | `.3s` | `animation:none`, by its own block | `none` | 4 bet sheets |

One job, two numbers, two mechanisms for less motion, two fill modes, and two spellings of the
same movement (`translate:0 100%` against `transform:translateY(100%)`).

---

## 3. The inventory of moments

Corpus: all 105 grey screens, `ia/docs/flows.md`, and every state selector in `components/`.
Each moment carries exactly one of three jobs, named before any animation was chosen.

### Response, 23 moments, 16 already done

The state exists in all 23, so the gate for the Animation stage passes on every one of them.
Seven have the state and no movement:

| component | states declared | placements in the paint |
|---|---|---|
| `navitem` | hover 2, active 2, aria 3 | **1,068 on 105 screens** |
| `position` | hover 2, active 2 | **996 on 105 screens** |
| `state-block` | hover 1, active 1 | 152 on 38 |
| `footer` | hover 5, active 5 | every screen |
| `cookie-consent` | hover, active, disabled 2 | 33 on 2 |
| `toc` | hover 2, active 1 | 1 |
| `base` focus ring | focus 2 | everywhere |

`navitem` and `position` are 2,064 placements between them, and neither answers a finger today.

### Connection, 10 moments, 5 already done

Done: the dialog sheet, the bet sheet, the condensed category band, the phone filter sheet, the
market accordion.

| not done | placements | state |
|---|---|---|
| `<details>` expands with no transition | **349 in the paint, 403 in grey** | `[open]` exists |
| `toc` expands | 1 | exists |
| a toast arrives and leaves | 4 on 1 screen | **NEEDS A STATE** |
| Load more appends cards | 9 | **NEEDS A STATE** |
| `edge-fade` on the scrollers | 90 elements | exists, job not named |

### Status, 2 moments, 0 done

**The skeleton does not pulse.** `skeleton.css` is 55 lines of flat `background:var(--bg-control)`:
zero animations, zero transitions, zero states. It stands **482 times on 19 screens, identically
in both trees**. The job "show that a process is running" is performed nowhere in this product,
and there are nineteen loading screens.

The second row is `edge-fade`, and it needs a ruling rather than an implementation: a mask bound
to scroll position is an affordance, not a moment, and none of the three jobs describes it.

### The estimate

| job | moments | done | left |
|---|---|---|---|
| response | 23 | 16 | **7** |
| connection | 10 | 5 | **5** |
| status | 2 | **0** | **2** |
| **total** | **35** | 21 | **14** |

30 fall to components, 0 to patterns, 5 to the shell. **Two rows say NEEDS A STATE** (the toast
and Load more) and both are orders on the Tokens and Components stage rather than work for this
one. 35 moments over 47 components is under one each, so no moment here is decoration wearing
a job's name.

---

## 4. The register: two durations, two curves

| token | value | job | where it came from |
|---|---|---|---|
| `--dur-fast` | `.16s` | a control answers a finger | 20 declarations, 71 per cent of every slot the product renders |
| `--dur-slow` | `.25s` | an element arrives | `sheet-rise` on 337 dialogs decided it against `betSheetUp`'s `.3s` on 4 |
| `--ease-standard` | `ease` | most transitions | 12,821 slots already render it, and the value is deliberately unchanged |
| `--ease-enter` | `cubic-bezier(.2,.7,.2,1)` | an arrival: sharp start, long settle | 585 slots, 8 declarations, formerly `--ease-out` |

**Why there is no third duration.** The middle job the stage names, a change inside a component
already on screen, has exactly one member in the inventory: `.market-chevron` turning over when
its market opens, which is feedback for a click and therefore a response. A third rung would
have sat 20ms from the one above it and been indistinguishable from it. It arrives the day the
inventory hands it a row.

**Why `--dur-fast` is 160ms and not 150.** A response slower than roughly 150ms stops reading as
an answer. 18 of the 20 response declarations cross-fade a colour, a border or a ground, and two
move something; the ceiling is about a control that moves under the finger. The 10ms is taken
knowingly, and reversing it is one line in `tokens.css` that 9,528 slots follow.

**Why there is no `--ease-exit`.** Nothing in this product animates a departure. A dialog closes
at once, the condensed band collapses through the rule that opened it, and no state in
`ui-visual/` has a leaving face. A token with no reader fails the idle control as loudly as an
undeclared case.

**Why there is no `--move-sm` or `--move-md`.** The stage asks for two distance tokens. This
system already answered that question on 2026-08-13 with a census and a different shape: of its
20 `transform` declarations only 5 are movement, and the five are 3px on a card, 2 on a badge
and 1 on a provider button, which the token's own comment calls three decisions and not a
ladder. The distance stays in the file that makes it and is multiplied by `--motion`, which the
reduced-motion block sets to 0. Adding `--move-sm` would be a fourth answer to a settled
question, and this folder has a trap written about exactly that.

### The five names that are aliases for one step

41 declarations read `--dur-quick`, 14 `--dur-base`, 5 `--dur-slower`, 8 `--ease-out` and 1
`--ease-inout`. Moving all 69 belongs to step 3, which reads each declaration and decides its
job. Until then they alias, so the tree renders while the decision is taken. A token that
survives this stage with an alias for a name is a token that was never merged.

---

## 5. The cost of a frame, and the instrument that was hiding the check

### Eight expensive properties: two converted, one refused with its reason, five kept with a count

`transform` and `opacity` are the two properties a browser can animate without laying the page out
again. `transition: all` is **0** and `will-change` is **0**, measured, and both were 0 before this
stage as well.

| where | what | done |
|---|---|---|
| `toggle.css` | the knob travelled by `left` | **converted to `transform: translateX(16px)`.** 22 minus 6 is 16, and the geometry is identical to the pixel: the knob's left edge reads 6 off and 22 on, in both engines, with the animations finished before the box was read |
| `hiw.css` | the step dot grew by `width` | **converted to `transform: scaleX(1.75)`.** 28 over 16 is exactly 1.75, so the resting state, which is two dots of every three, stays undistorted. The cost is named: scaling a pill horizontally scales its end caps, so the selected dot's caps go from a 2px radius to 3.5 on a bar 4px tall |
| `header.css` | the condensed band collapses by `max-height` | **kept, and it is the one refusal.** There is no transform that removes a box from the flow, and this band's whole job is to stop taking room. `scaleY` leaves the room behind, taking it out of flow puts it over the content it exists to push, and `grid-template-rows` from `0fr` is the same layout pass under a different name. **The cost is one element, once**: one band per document, relaid for 250ms when the header condenses |
| `button`, `card`, `hero`, `iconbtn`, `input` | `box-shadow` | **kept, five of them, and the count is the argument.** `box-shadow` does not touch layout; it loads painting, and the case against it is a list of twenty cards painting at once. All five are on the element's own hover or focus, so **at most one element in the document is animating a shadow at any moment**. A pointer is in one place |

**And the two conversions were each misread once before they were believed.** The toggle read
`translateX(0)` in both faces, then 0.56px in Chromium and 3.82 in WebKit, because the probe was
reading a transition in flight; finished first, both engines read exactly 16. The dot read
`transform: none` on all nine of its placements on `how-it-works.html`, which looked like a rule
that had not applied and was **nine elements that render at no width at all**, because they live
inside the shut how-it-works dialog. On `ui-kit/hiw.html`, where six of them do render, the selected
one reads `matrix(1.75, 0, 0, 1, 0, 0)`. **A computed value on a box that was never laid out is not
a reading of the rule**, and this is the shut-dialog trap the kit has already paid for once.

### Less motion: the mechanism, and the net that was standing on top of it

The mechanism is one block in `tokens.css` that redeclares the tokens. Every component reading a
`var()` obeys without knowing the block exists, and so does the component nobody has written yet.

`1ms` and not `0s`: a duration of zero removes the transition rather than shortening it, so
`transitionend` never fires and a script waiting on it stalls. 1ms keeps the event and removes
the movement, and it is the value the step 5 check looks for. **Anything above 1ms is a rule that
is not reading these tokens.**

`@media` works here and could not at the Responsive stage, and that is not a contradiction. A
width query cannot READ a custom property, which is why the rung ladder is a registry. This query
does not read one, it redeclares one inside itself.

### The check was blind, and then it was not: the net is gone

`base.css` carried a blanket net from before this stage:

```
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{ animation-duration:.01ms !important;
                        transition-duration:.01ms !important; ... } }
```

Measured with it in place, over 163 documents in two engines: **6,555 moving elements per engine
in the normal pass against 115,028 under the setting**, the difference being every element in the
DOM taking a duration from that one rule, and **0 rows above 1ms out of 230,056**.

That green said the net was present and said nothing else. Under `!important` on `*`, a component
that reads no token is indistinguishable from one that reads every token. **A sweep that cannot
fail is not a sweep.**

**Taken off at step 5 and re-measured, with the positive control first.** An injected element
carrying `transition: opacity 999ms linear`, which reads no token of ours, read back **999ms in
both engines**: the probe can see a rule that does not obey. Then 163 documents, Chromium 151 and
WebKit 26.5, emulating the setting:

| pass | elements above 1ms | where |
|---|---|---|
| net removed, first reading | **1,392** | **0 in `components/`.** 690 per engine from one `.15s` literal in `ui-kit/_page.css`, over ten kit pages and `ui-visual/overview.html`; 6 per engine from the demonstration pulse on `motion.html` |
| both repaired at source, second reading | **0** | |

**Every rule in the system obeyed the token override on its own**, which is the fact the net had
been standing on top of for as long as it existed. The two that did not were the stand, and a
stand is not a product and IS read by a person, so both were fixed rather than covered.

**The net is not put back.** Its only remaining argument was code that does not exist yet, and this
system already has a rule about paying rent on a decision nobody has taken. What it never reached
anyway is in the list above: the grey tree links no stylesheet, and a cycle needs replacing rather
than shortening, which no duration can express.

### Reduction removes the movement and never the state, measured

The rule that matters more than any amount of unnecessary animation: an element that appears has to
appear under the setting too. Three sheets opened with `showModal()` at 390px, settled, both
engines, both settings:

| | normal, 60ms in | under the setting |
|---|---|---|
| sign in | `translate: 0 21.1%`, still climbing | `translate: 0 0%`, arrived, opacity 1 |
| deposit | `translate: 0 25.2%` | `translate: 0 0%`, arrived, opacity 1 |
| bet sheet | at rest, its own block sets `animation:none` | identical, on screen, opacity 1 |

**0 states lost.** The skeleton is the same answer in the other direction: the marks stop moving and
stay fully opaque rather than disappearing.

### What the token override will not reach

Three entries, and the section is closed. **The first arrived at step 3, by writing a rule rather
than by auditing for one.**

**1. A cycle, and it is the case the mechanism cannot answer.** Setting a duration to 1ms shortens
a transition into nothing, which is the whole point. Applied to a repeating cycle it does the
opposite: 1ms per period at infinite iterations is a **flicker**, worse than the still box the
skeleton shipped before this stage. A cycle is therefore REPLACED and never shortened.
`skeleton.css` carries its own block, and so does the demonstration pulse on `motion.html`, which
would otherwise have been the page explaining reduced motion while still moving under it. Measured
over three loading screens in both engines: 60 marks running at 1.4s infinite in the normal pass,
**0 running and every mark back at full opacity under the setting**.

**2. `wireframes/`, and it is 105 of 105.** The grey tree links no stylesheet at all, so no token
declared anywhere can reach it, and every one of its documents carries the same inline
`transition: transform .2s ease` on the navigation drawer. Measured with the setting emulated in
both engines: **105 elements above 1ms over 105 of 105 documents.** It is not repaired here. A grey
file cannot hold a token, the drawer moves so the tree can be clicked through, and the honest answer
is the seventh declared boundary difference in `wireframes/_conventions.md` rather than 105 copies
of a media query. Written at step 6.

**3. The thirteen course documents, of which six move.** `research.html`, `voice.html`,
`concept.html`, `ia.html`, `seo.html` and `system.html` carry their own inline `<style>` and their
own literals: `.15s`, `.2s` and one `.4s cubic-bezier(.2,.7,.2,1)`. Same cause as the grey tree,
different tree: they link nothing from `components/`, so no token declared there can reach them.
They are the record of how this product was made rather than the product, and the honest answer is
the same one: named here rather than repaired by copying two numbers into six more places.

**4. A cross-document view transition, which is why there is not one.** It reads no duration token,
so choosing it would have bought a fourth entry for this list in exchange for a cross-fade. Ruled
out at step 4 for four reasons, of which this was the third.

**And nothing else, proven rather than assumed.** See the next section.

---

## 6. Components

Done 2026-08-15. Three rounds bottom up, atoms then molecules then organisms, and **the rounds were
not gated separately** because the same 69 declarations are one rewrite: stopping between levels
would have left the tree half tokenised with five aliases still standing, which is a state nobody
could have reviewed usefully.

### The rewrite: 69 declarations read, given a job, and moved

| from | reads | to | why |
|---|---|---|---|
| `--dur-quick` .16s | 41 | `--dur-fast` | every one a response |
| `--dur-base` .18s | 14 | `--dur-fast` | every one a response as well, which is why the middle rung had nobody to spend it |
| `--dur-slower` .3s | 5 | `--dur-slow` for the two arrivals, `--dur-fast` for the card | the card's was a hover at 300ms |
| `--dur-slow` .25s | 5 | kept for the dialog, the header band and the harness drawer; `--dur-fast` for the hero | the hero's two were hovers at 250ms |
| `--ease-out` | 8 | `--ease-enter` for arrivals, `--ease-standard` for responses | |
| `--ease-inout` | 1 | `--ease-enter` | its one reader is the harness drawer, an arrival, so the harness curve changed and the product's did not |
| bare `ease` | 53 | `var(--ease-standard)` | same value, now a token |

**The rewrite skipped every comment**, so the six historical quotes in `card.css`, `chip.css` and
`docs/decisions.md` still say what was true when they were written. A record that a later sweep
rewrites is not a record.

The five aliases were deleted in the same step, after the last reader moved.

### Seven components had a state and no movement, and six were given one

The gate held on all seven: the hover and the press were already declared with tokens in both
themes, so nothing had to be invented and no `.is-hover` was drawn.

| component | placements | what it does now |
|---|---|---|
| `navitem` | **1,068 on 105 screens** | the ground fades |
| `position` | **996 on 105 screens** | the plate's ground and edge, and the question's ink, on two selectors because the hover is written on the anchor above them |
| `state-block` | 152 on 38 | ground and underline |
| `footer` | every screen | ink and ground, and NOT the underline |
| `cookie-consent` | 33 on 2 | the policy link's underline |
| `toc` | 1 | the rail's rows and its head |

**The seventh is the focus ring and it stays instant, deliberately.** A ring is the answer to
"where am I", and a person moving through a form at speed passes an element in less time than any
duration worth writing. A ring that fades in is a ring that is not there yet when it is needed.

### The status job, performed for the first time

`skeleton.css` gained `sk-pulse`, an `opacity` cycle at `--pulse-period`, on all 482 marks across
19 loading screens. Opacity because it is one of the two properties a browser animates without
laying the page out again, and a loading screen is exactly where twenty cards pulse at once.

`--pulse-period` is 1.4s and it is **not** a third rung of the duration ladder: the two durations
answer "how long does this change take" and a period answers "how often does it come round". It
carries a different prefix so the next reader reconciling the ladder does not find a number on it
that was never on it. The amplitude is shallow on purpose, .55 of full: a plate that goes nearly
invisible reads as content flashing in and out rather than as a wait.

### What the product renders after step 3

| | before the stage | after step 3 |
|---|---|---|
| moving elements, 105 screens | 4,904 | **9,084** |
| distinct durations | 5 | **2**: `.16s` 19,349 slots, `.25s` 171 |
| duration literals in the system | 0 | **0** |
| bare easing keywords | 54 | **0** |
| `transition: all` | 0 | **0** |
| animations rendering on load | `edge-fade` 90 | `edge-fade` 90, **`sk-pulse` 482** |
| components with movement | 20 of 47 | **26 of 47** |

Chromium 151 and WebKit 26.5 agree element for element on every line. 163 documents, 231,872
readings, 0 page errors and 0 HTTP errors.

## 7. Patterns, screen states, and the crossing between documents

Done 2026-08-15. Two of the three parts came back empty, and in both cases the emptiness is the
answer rather than a gap.

### A state is a PAGE, so state transitions do not exist in this product

This is the structural fact the whole step turns on, and it is not a shortcoming: `wireframes/`
and `ui-visual/` both hold one document per state, 105 each, by a convention that predates this
stage. Loading, empty, error and success are therefore not things a screen moves INTO. There is
nothing to transition, because there is no before and after inside one document.

The one state family that does live inside a document is the dialog, and the tone check is
therefore a check of five surfaces rather than of twenty.

### The tone check, four quantities against the line the screen says

`voice.md` sets the tone and this stage does not get to choose it. Four quantities: duration,
curve, amplitude, direction.

| state | the line the product says | duration | curve | amplitude | direction | verdict |
|---|---|---|---|---|---|---|
| loading | silent, a skeleton grid; or "Registering your bet on-chain..." | 1.4s period | `--ease-standard` | .55 opacity, no movement | none | **agrees.** The rule says stay silent or name the thing, never hype. A shallow, even breath with no travel is the visual form of staying silent |
| success, the win | "You were right. +$13.20." then "See next events" | `--dur-slow` .25s | `--ease-enter` | 100 per cent translate, one axis | up from the bottom edge | **agrees, and this is the row that mattered.** Principle 4 is "mark the win without lighting a fuse", and the anti-example is confetti. The win dialog arrives on exactly the same rule as every other sheet |
| the loss | "Here's what happened: ... The market resolved NO; you held YES." | `--dur-slow` .25s | `--ease-enter` | same | same | **agrees, and it agrees BY BEING IDENTICAL to the win.** Two different arrivals would have been the product having an opinion about your result before you had read it |
| error | "Couldn't load your wallet. Your funds are safe; this is a display issue." | none | none | none | none | **agrees.** The rule asks for short, no spring, small amplitude. Every error surface here is a page, so the amplitude is zero, and nothing is calmer than nothing |
| empty | "No active bets yet. ... Find an event you have an opinion on." | none | none | none | none | **agrees.** The rule against a shift from below is about not implying that something is still loading, and a page that simply IS cannot imply it |

**0 disagreements, and `microcopy.md` was not edited.** The one row that could have gone wrong is
the win, and it did not, because the rule that would have broken it was written down five stages
ago and the dialog never had a face of its own.

### Patterns: 0 of 6 get a transition, and the reason is what the rung IS

Read from the comment-stripped source of all six files: **not one of them declares a selector that
toggles at run time.** `action-bar`, `card-grid`, `detail-shell`, `list-head` and `position-list`
have no state selector at all; `browse-shell` has one, `:not(:has(.subcat,.toc))`, and that is a
structural presence check rather than a state that changes while a person looks at it.

So the composition never recomposes, and **an arrangement that never changes has nothing to move
between**. This is the same invariant that keeps colour out of `patterns/` seen from the other
side: a rung that carries arrangement only carries the movement of an arrangement only, and there
is none. 59 declarations over 16 properties, and after this stage still 16.

### Ruling 1: the crossing between documents is A, and B is one line away

Every screen here is a separate HTML document, so the move from a feed card to its detail, or
from a bet to its result, is a navigation and an ordinary `transition` cannot see it. Three honest
answers exist and one had to be chosen out loud.

**Measured before choosing**, because "the browser probably supports it" is not a reading.
`@view-transition { navigation: auto }` on two test documents, navigated for real, listening for
`pagereveal` and asking whether the event carried a `viewTransition`:

| | over `http://` | over `file://` |
|---|---|---|
| Chromium 151 | **fires** | **fires** |
| WebKit 26.5 | **fires** | **does not** |

**The answer is A, do not animate the crossing**, and the reasons are in this order:

1. **`navigation: auto` alone is a cross-fade, and a cross-fade points at no source.** The
   connection job is defined as showing WHAT came from WHAT, and the direction of the movement is
   how it says so. A page dissolving into another page says only that a page changed. That is
   movement with no row of the inventory behind it, which is the one thing this stage cuts.
2. **Doing the job properly is a markup change in two trees.** It needs `view-transition-name` on
   the card and on the detail head, the name has to be unique in its document, and a feed ships up
   to nine cards, so the name would have to be written at click time by a script. That is a real
   piece of work and it deserves a row rather than a side effect of a one-line rule.
3. **It would add an obligation the token mechanism cannot reach.** A view transition does not
   read `--dur-fast`, so reduced motion for it is a separate rule, and this stage already has one
   such case and does not need a second bought for a cross-fade.
4. **On the path this repository actually reads from, one engine of two would not show it.** These
   pages are opened from disk, and WebKit does not fire the transition there, so half the reviews
   would be of a feature the reviewer cannot see.

**What would change the answer**: a named pair with a measured before and after. The line is
`@view-transition { navigation: auto }` in `base.css` and nothing else, and the measurement above
is banked so the decision does not have to be re-taken from zero.

### Ruling 2: a rung does not animate its own rebuild

Default and answer are both no. A width rung fires while a person is dragging the edge of a
window, which is the one moment they are not looking at the content, and animating a grid rebuild
is expensive on exactly the device that can least afford it.

The exception the stage allows is a surface that did not exist at the narrow width at all, and
this product has two: `.bet-panel` arrives at the DETAIL rung and the `.subcat` rail at RAIL.
**Both are refused on the same ground**: they arrive only during a drag. A person who opens the
product on a desk never sees the arrival, and a person on a phone never has it. An entrance
nobody can be present for is not a connection, it is a frame that happens to differ.

### Ruling 3: the scroll edge fade is an affordance and stays out of the register

`edge-fade` binds a mask to the element's own inline scroll rather than to time. It has no
duration, it reads no duration token, and **it is driven by the reader's own hand**: it changes
only while they scroll, and it changes by exactly as much as they scrolled.

Measured on the feed's category rail, both engines, both settings, at three scroll positions:
the left edge closes from `0px` to `32px` and the right opens from `calc(100% - 32px)` to `100%`.
**The mask moves with the scroll in all four combinations, including under `prefers-reduced-motion`
where the blanket net forces `animation-duration` to `1e-05s`**, because a scroll timeline maps
progress from scroll distance and not from that duration. It therefore needs no reduced-motion
treatment and gets none: movement a person makes themselves is not movement done to them.

So it stays, it stays OUT of the inventory of moments, and it is declared here instead. None of
the three jobs describes it, and rather than widen the three to fit one rule, the rule is named as
what it is.

**And the first reading of it was wrong, in this stage's own signature way.** The probe set
`scrollLeft` and read the computed mask in the same task, and reported the mask identical at every
scroll position in both engines, which reads exactly like a feature that does not work. Two
animation frames later the same probe reports it moving in all four combinations. **A scroll is not
a paint any more than a resize is a layout**: give the engine a frame, or measure the state it left
behind.

---

## 8. Two rulings this stage owes

**The grey tree and motion.** `wireframes/_conventions.md` declares six differences that ARE the
boundary between the trees rather than drift: the plate wrappers, the icon mechanism, the
photograph, the chart data, the `TBD` chip, and the page behind an overlay. **Motion is not among
them.** The paint takes its durations from tokens and the grey tree keeps one literal `.2s ease`
on its drawer, so from this stage the two trees disagree about something nobody declared, which
is drift by that document's own definition. It is a seventh declared difference, not a port: a
grey file links no stylesheet and therefore cannot hold a token, and its drawer moves so the tree
can be clicked through. Written at step 6.

**Motion at a rung.** Ruled at step 4, section 7: no, including for the two surfaces that qualify
for the exception, because both arrive only during a drag and nobody is present for them.
