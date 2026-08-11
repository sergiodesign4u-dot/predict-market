# Responsive - what the product does with width

Stage 10. Written 2026-08-11 from two measured passes and no opinions: a **transcript** of every
place the look already depends on width, and an **audit** giving one answer per screen.

The visible half of this file is [`ui-kit/responsive.html`](../responsive.html). This is the record;
that is the stand.

**The order matters and it is the reason this stage starts here.** An audit taken without a
transcript adds a third breakpoint beside two nobody noticed, and the product ends up with five
numbers of which none is a decision. So the transcript came first, and it found three numbers
already living in the product that no one had named.

---

## The ladder of three ways, and the point is last

Read top down. Take the first one that works, and a point is only allowed once the two above it
physically cannot.

| | Fluid | Container | Point |
|---|---|---|---|
| The question | will the content stretch by itself? | is the line too long? | is the behaviour different? |
| The mechanism | `clamp()`, `%`, `minmax(auto-fit)`, `flex-wrap` | `max-width`, and the measure in `ch` | `@media` for the shell, `@container` for a component |
| How many | no limit | one or two | **three rungs, and they are named** |
| Proved by | pull the width and nothing breaks | a measured line length in `ch` | a line in the audit saying why fluid could not |

"It is easier to write that way" is not a reason. The reason goes in the audit row.

---

## Part A. The transcript: what already depends on width

Mechanical, by grep, over four corpora, because their fates differ.

| corpus | `@media` | `@container` | fluid | container | fate |
|---|---|---|---|---|---|
| **`components/` THE HOME** | **38**, of which **33 are about width** | **0** | clamp 8, minmax 12, auto-fit 1, flex-wrap 31, vw 9, `%` 37 | max-width 28, min-width 32, margin-inline 3, `ch` 6 | **stays** |
| **`ui-visual/` THE SCREENS** | **0** | 0 | **0** | **0** | **nothing to move** |
| **`ui-kit/` THE STAND** | 11, all in `_page.css` | 0 | clamp 10, minmax 13, auto-fit 4 | max-width 12, `ch` 15 | stays in `_page.css`, not a product rule |
| **`wireframes/` THE GREY TREE** | **1,386 in 104 files** | 0 | minmax 431, auto-fill 92, flex-wrap 2,142 | max-width 1,265, `ch` 90 | the corpus of evidence |

**The stage's most expensive trap is already closed on the painted side.** A screen file may not carry
a media query, and `ui-visual/` carries none: 0 `@media`, 0 `@container`, 0 `max-width`, 0 `clamp`.
The only width sign in the whole painted tree is 46 percentages, and **all 46 sit inside a `style=`
attribute** with values like `88%`, `58%`, `30%` and `12%`. Those are odds-bar fills, which is a
datum, and a datum is one of the three things `CLAUDE.md` allows on the element.

**What is genuinely new: `@container` is 0 and `container-type` is 0 in all four corpora.** No
component in this system measures its own place. Every adaptive rule here asks about the window.

### The headline number: twelve distinct widths

| px | `components` | `wireframes` | `ui-kit` | `ui-visual` | what it is |
|---|---|---|---|---|---|
| 560 | 2 | 9 | 0 | 0 | one-off, named in `tokens.css` |
| 620 | 1 | 1 | 0 | 0 | one-off, named |
| 639.98 | 8 | 57 | 4 | 0 | DESK, narrow side |
| **640** | 6 | **401** | 1 | 0 | **DESK, the one divide** |
| 759.98 | 4 | 183 | 5 | 0 | DETAIL, narrow side |
| **760** | 3 | 184 | 1 | 0 | **DETAIL, the second column** |
| **900** | 6 | 94 | 0 | 0 | **RAIL, a rail beside the content** |
| **960** | 0 | **104** | 0 | 0 | **on no ladder** |
| 980 | 1 | 1 | 0 | 0 | one-off, named |
| 1140 | 2 | 0 | 0 | 0 | HARNESS, not the product |
| **1280** | 0 | **104** | 0 | 0 | **on no ladder** |
| **1440** | 0 | **104** | 0 | 0 | **on no ladder** |

The nine in the system are really **five**: three rungs each written twice for its two sides, plus
the harness, plus three named one-offs. The stand invents nothing.

**The three that are on no ladder are all in the grey tree and all in all 104 files.** 960 and 1280
hard-code `repeat(3,...)` and `repeat(4,...)`, a column count the paint computes with `auto-fit` and
no query at all. 1440 is the grey harness, the twin of the paint's 1140 standing at a different
number. They are this stage's own backlog, item 116.

---

## Part B. The audit: one answer per screen

Corpus: all 104 `wireframes/*.html`, read against `user-research/docs/jtbd.md` and
`user-research/docs/cjm-as-is.md`. The question is not how to stretch a phone layout. It is **what a
wider screen gives the person in the job they came to do**.

| family | screens | the job | answer | by what | where it already stands |
|---|---|---|---|---|---|
| Event feed | 9 | FJ1, find the event before the moment passes | **WIDER / GRID** | fluid | `patterns/card-grid.css`, no query at all |
| Category feeds x4 | 32 | FJ1 within a theme | **WIDER / GRID** | fluid + RAIL 900 for the rail | `catnav.css`, `patterns/browse-shell.css` |
| Favorites | 3 | FJ1 over what was saved | **WIDER / GRID** | fluid | the same track |
| Event detail | 13 | **FJ2, MVP job 1: why this number** | **WIDER** | DETAIL 760 | `patterns/detail-shell.css`, `betpanel.css`, `chart.css` |
| Active bets | 9 | MJ and FJ5, watch the open positions | **WIDER** | DESK 640 | `bets-table.css` |
| Notifications | 5 | FJ1, do not miss the moment | **WIDER / AIR** | container | nothing yet |
| Wallet | 3 | FJ4, what happens to my money | **WIDER / AIR** | container | nothing yet |
| Profiles | 7 | SJ2, a record that can be checked | **WIDER** | fluid | `position.css` at DESK |
| How it works | 1 | EJ2, is this a serious place | **WIDER / AIR** | container + RAIL 900 | `hiw.css`, `toc.css` |
| Deposit | 7 | FJ3, pay with a card | **SAME** | nothing | the sheet caps at 464 |
| Sign in | 4 | get in | **SAME** | nothing | the sheet caps at 410 |
| Win and loss | 6 | EJ1, SJ1, FJ5, EJ3 | **SAME** | nothing | the sheet caps at 420 |
| System | 5 | 404, 500, maintenance, cookie, toasts | **SAME** | nothing | - |

**The estimate: SAME 22, WIDER 82** (of which GRID 44 and AIR-or-point 38), **NEW BEHAVIOUR 0.**

### New behaviour is refused, and not on taste

The product has exactly one list-and-detail pair, feed to detail, and `ia/docs/flows.md` says what
that pair is for: *"Both land on Event Detail, so FJ2 (context before the bet) is preserved for
everyone. There is no Feed to bet edge: nothing bypasses the context screen."*

Event Detail is not the next screen after the feed. It is a **mandatory context screen**, and it
carries growth zone 2 from `cjm-as-is.md`, "explain the number, tell the story", which is the barrier
at phase 4 and MVP job 1. A split view would halve exactly the screen the product exists to widen.

None of the five named growth zones is "I lose my place going back and forth". There is no second
pair: bets, notifications and the wallet have no detail screen at all. Step 5 is therefore answered
in the short form, and that is an answer.

### What the audit found instead: 38 lines that run too long

Measured at 1440 over all 106 painted screens with every dialog open, counting **only text that
actually wraps**, because a box is not a line. `DESIGN.md` section 3 states the band: 60 to 75ch.

| n | worst | element |
|---|---|---|
| 27 | **117ch** | `.related-list p`, event detail |
| 9 | **106ch** | `.rules-panel .resolution` |
| 1 | **154ch** | `.sys-note` in `.cat-main` |
| 1 | **166ch** | `.protect-page` in `.cat-main` |
| 2 | 89ch | `.feed-seo p` - **already decided**, `--container-read` says why |
| 1 | 89ch | one unclassed paragraph |

**The loudest of them is the 106ch one.** `.resolution` is the named resolution rule, which is the
second design principle of this product written as a sentence, and it runs 40 per cent over the
measure on the screen where trust is decided.

---

## The registry of points

Three rungs, each named by what arrives at it. The full argument, including why a breakpoint cannot
be a token, is in `components/tokens.css` under "the breakpoint ladder".

| rung | what arrives | rules |
|---|---|---|
| **640 DESK** | the one divide: one column, a bottom nav and a mobile dock below; the desk above | 13 in 13 files |
| **760 DETAIL** | the event detail gains its second column, the bet panel docks, the chart takes full height | 5 |
| **900 RAIL** | a vertical rail arrives beside the content: sub-categories, the table of contents, the how-it-works side column | 6 |

And one that is not the product's: **1140 HARNESS**, where the review panel docks. It is 900 + 220 +
20 on purpose, so the chrome can never take width the widest product rung is counting on.

**A rung is one pixel and it belongs to the wide side.** Below a rung is `max-width:639.98px`, never
`max-width:640px`, because both match at exactly 640 and the rung then renders a page that exists at
no other width. That cost this repository 73 screens for a day.

**The registry is the instrument.** A media query cannot read `var()`, so the literal has to be
repeated in every rule, and the only possible check is to read every `@media` in the product and ask
whether its number is on the list above. No number may appear in a product media query that is not.

### Why the rungs are in px and not in rem

The argument for rem is real: a rung in px reads the window only, so a person who has enlarged their
browser font sits at a desk width with a phone's worth of text in the line. It was measured before it
was believed, root font 16px against 24px, control first.

| | 16px root | 24px root |
|---|---|---|
| `10rem` measures | 160px | **240px**, so rem does respond |
| `body` | 16px | 24px, because nothing sets it |
| heading | 36px | **36px** - `clamp(28px,4vw,38px)`, vw not rem |
| feed prose | 13px | **13px** - `--text-13` |
| footer legal | 11px | **11px** - `--text-11` |

**The whole type scale is px.** Eighteen size tokens are px literals, the display sizes are `clamp()`
of px and vw, and 222 of the 228 font-size declarations in the system resolve to a number the user's
setting cannot move.

So putting the rungs in rem would be **worse** than leaving them: the layout would switch at a
different window width for that person while every word on it stayed exactly the same size. A
breakpoint answering a question the product does not ask anywhere else looks like accessibility and
does nothing. The rungs stay px and the real finding is filed as `docs/backlog.md` item 115.

---

## The tokens this stage added

| token | value | why |
|---|---|---|
| `--measure` | `66ch` | the line measure for continuous text, in `ch` so one number caps an 11px legal line and a 16px paragraph at the same character count. 66 is inside the 60-75 band `DESIGN.md` states and agrees with `--container-doc`, measured at 67ch |
| `--grid-col-min` | `300px` | the card floor, moved out of `patterns/card-grid.css` where it stood as a literal |

**There is no `--grid-gap`, and that is a decision.** The track gaps at `var(--space-16)`, and the
space ladder is already the gap ladder; a second name for 16px would be one number with two
spellings. **The column count is not a token either**: `auto-fit` counts the columns, which is why
the track works at 1100px, a width nobody designed for.

`--container-max`, `--container-read` and `--container-doc` already existed and are not renamed: the
page frame was decided at stage 08 and this stage adds to it rather than restating it.

**None of these tokens has a theme pair, and that is not an oversight.** A `:root` / `[data-theme]`
pair is a property of the semantic level, which is colour. Width and spacing are geometry.

---

## The shell

To be filled by step 3. The fork is already half decided upstream: `ia/docs/sitemap.md` records that
the mobile bottom nav is replaced on desktop by the lean header, and `bottomnav.css` already does it
at DESK 640. What is missing is the proof that exactly one top-level navigation carrier stands at any
width, by computed style and a tab pass.

## Component behaviour on width

To be filled by step 4, together with the placements of `--measure` on the four classes named above.

## Container thresholds

To be filled by step 4. There are none today: `@container` and `container-type` are both 0.

---

## What is not taken

`docs/backlog.md` items 115 and 116, opened by this stage.
