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
| **`ui-kit/` THE STAND** | 11, all in `_page.css` | **1**, with 1 `container-type` | clamp 10, minmax 13, auto-fit 4 | max-width 12, `ch` 15 | stays in `_page.css`, not a product rule |
| **`wireframes/` THE GREY TREE** | **1,386 in 104 files** | 0 | minmax 431, auto-fill 92, flex-wrap 2,142 | max-width 1,265, `ch` 90 | the corpus of evidence |

**The stage's most expensive trap is already closed on the painted side.** A screen file may not carry
a media query, and `ui-visual/` carries none: 0 `@media`, 0 `@container`, 0 `max-width`, 0 `clamp`.
The only width sign in the whole painted tree is 46 percentages, and **all 46 sit inside a `style=`
attribute** with values like `88%`, `58%`, `30%` and `12%`. Those are odds-bar fills, which is a
datum, and a datum is one of the three things `CLAUDE.md` allows on the element.

**What is genuinely new: `@container` and `container-type` are 0 in the three corpora that are the
product**, `components/`, `ui-visual/` and `wireframes/`. No component in this system measures its
own place. Every adaptive rule here asks about the window.

**The fourth corpus is not 0, and this table said it was until 2026-08-12.** `ui-kit/_page.css`
declares one `container-type` and one `@container`, both of them `.tk-cq` and the box it wraps on
`responsive.html`, and **they were added by step 2 of this same stage, after this grep was taken and
before this file was read again**. A transcript is a measurement with a date on it, and the one thing
that can invalidate it is the work it was taken for. The claim it made about the product still holds;
the claim it made about all four corpora did not. The caption under the specimen on the stand hedged
correctly the whole time, "the system declares 0 of these today", which is how the disagreement was
found.

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

**The transcript is not restated and the system has moved three times since it was taken.**
`ui-kit/` gained its `container-type` at step 2, recorded above; on **2026-08-12 `components/` went
from 33 width queries to 35**, `options.css` and `yesno.css` each taking one at 639.98 so the
outcome row could wrap below the desk; and on **2026-08-13 it went back to 33**, because backlog 129
deleted two. Counted from the comment-stripped source of all 53 stylesheets: **33 width queries, of
which 14 at the desk in 13 files, 7 at the detail in 7, 6 at the rail in 5, 2 at the 1140 harness
and 4 one-offs**. The registry did not move and no rung was added or removed by any of the three,
which is the only thing the transcript was taken to protect. **The two that went are worth naming,
because neither was replaced**: `tokens.css` held the page gutter and the plate inset at one pair of
values below the desk and another above, and both are a `clamp()` now; `card.css` held the bookmark
pull for phones alone, and it holds it for every card now. **A query that leaves with nothing put in
its place is a query that was answering a question its subject never asked.**

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
| **640 DESK** | the one divide: one column, a bottom nav and a mobile dock below; the desk above | 16 in 15 files |
| **760 DETAIL** | the event detail gains its second column, the bet panel docks, the chart takes full height | 7 in 7 files |
| **900 RAIL** | a vertical rail arrives beside the content: sub-categories, the table of contents, the how-it-works side column | 6 in 5 files |

**The three counts were 13, 5 and 6 when this table was written and two of the three were already
wrong**, re-taken 2026-08-12 from the comment-stripped source of all 52 stylesheets. The desk gained
two on that date, `options.css` and `yesno.css`, when the outcome row was given a second line below
it; the detail's 7 was never 5. **A rule count is a claim like any other**, and this one had no
reader between the day it was typed and the day something forced it to be taken again.

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

**AND THE FINDING WAS ACTED ON, 2026-08-12: THE TYPE IS IN REM AND THIS SECTION'S ARGUMENT IS SPENT.**
Everything above is left standing because it is the argument the stage made, because it was correct,
and because it is the reason the type moved at all. What it may no longer be read as is a defence of
the rungs. Ten `--text-*` steps and eight `--display-*` clamps are ratios to the root now; the move
was proved inert at the default with **0 differing font sizes and 0 differing line heights of 44,547
readings over 210 screen-and-width pairs**, and at a 24px root the phone page grows 38.4 per cent and
carries every word. **The rungs stayed px in the same pass, deliberately and on a different ground**:
the old ground was about the type, and a rule whose reason has expired is what this repository keeps
paying for, so the rung question is open on its own merits as `docs/backlog.md` 135 rather than
answered as a side effect of something else. Item 115 is closed.

---

## The tokens this stage added

| token | value | why |
|---|---|---|
| `--measure` | `46ch` | the line measure for continuous text, in `ch` so one number caps an 11px legal line and a 16px paragraph at the same character count. **It was `66ch` here and in the token until 2026-08-12, on the stated ground that 66 is inside the 60-75 band `DESIGN.md` states, and the ground was a unit error**: `ch` is the advance of the digit zero and a lining digit is one of the widest glyphs a prose face draws, so in DM Sans 1ch is 1.48 mean prose advances and 66ch bought about 98 characters. The census could not see it because it computed `width / 1ch` and compared the answer to a band written in characters, which is asking the token its own question. 46 is `67.5 / 1.48`, and it was swept as well as derived: the window in which every capped placement sits inside 60 to 75 is 45ch to 48ch |
| `--grid-col-min` | `300px` | the card floor, moved out of `patterns/card-grid.css` where it stood as a literal |
| `--plate-inset` | `clamp(16px, …, 28px)`, ramping DESK to DETAIL | the inset INSIDE the two-stone plate, added 2026-08-12. It is the second half of a step the first half had been taking alone: `--gutter` is the page gutter OUTSIDE the plate and went 40 to 14 at the rung, and this one held 28 at every width, so the two nested gutters took 42px a side on a phone, 84 of 360, before a card began. Read in one place, `base.css`, the two-stone plate, and only by the SIDES: vertical space has nothing above it competing for the same 360px. **Both STEPPED at DESK until 2026-08-13 and both RAMP now**, 640 to 760, because a step of 38px a side against a window that has grown by one pixel takes 76px out of the content column at the rung: backlog 129 |

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

Step 3, 2026-08-11. **The fork is answered A, and it was answered at 03a rather than here.** This
stage decides the FORM of the navigation and never its items, so the three questions are asked of
`ia/docs/sitemap.md` and the answers are read off it.

| the question | the answer | where it is written |
|---|---|---|
| how many top-level items | **four**: Events, My Bets, Favorites, Portfolio | bottom-nav table, `sitemap.md` |
| a second level that must stay visible | **no**: the categories band is a second level and it is not permanent, it rides the sticky header and only on the browse screens | D-desktop-1 |
| does a wide screen take side space for new behaviour | **no**: the audit named 0 new behaviour | Part B above |

Four items and no permanent second level is branch **A**, the items move into the header. The
product's version of A is the **lean header**: Events becomes the logo, My Bets and Profile fold into
the avatar menu, Favorites and Notifications become icons in the utility cluster, and the balance is
the cluster's swap. No vertical rail arrives, and the desktop introduces no destination the phone
does not have.

**It was already built, and step 3 is therefore a proof rather than a design.** `bottomnav.css` hides
the bar from DESK 640 up and `base.css` turns `.desk-only` on at the same rung.

### The proof, on three instruments, over 106 painted screens

| what was read | below 640 | at 640 and above |
|---|---|---|
| `.bottom-nav` computed | **painted on 105 of 106** | **`display:none` on all 105** |
| `.desk-only` computed, 178 elements | `none` on all 178 | `flex` on all 178 |
| tab stops inside the bar | **4** | **0** |
| `Primary (mobile)` in the accessibility tree | **present** | **absent** |
| header tab stops | 3 | 7 at 640, **8 from 760** where `.hiw-btn` returns |

So the swap happens at one pixel, in one direction, and the carrier that leaves leaves the paint,
the tab order and the accessibility tree together. **A hidden carrier does not linger here**, which is
the whole reason the check is a Tab walk and not a stylesheet read.

The one screen of the 106 that has neither carrier is `overview.html`, which is the tree's own index
and not a product screen.

### What "exactly one carrier" is actually true of, stated rather than assumed

Counting every rendered link to one of the four destinations, by the region that holds it:

| width | carriers offering a top-level destination |
|---|---|
| 360, 639 | **bottom nav + footer** on 73 screens, footer alone on 32 |
| 640 to 1440 | **header + footer** on 73 screens, footer alone on 32 |

**There is exactly one PRIMARY carrier at every width and there is a footer at every width**, and the
footer is not a defect: it is secondary navigation, it never changes at a rung, and it carries Events
and My Bets on all 105. The 32 screens with the footer alone are the logged-out ones, where the bar
and the cluster have nothing to point at. Saying "one carrier" without saying this would be true of
the primary and false of the page.

**Two of the four destinations are one interaction deeper on the desk**, My Bets and Portfolio, both
inside the avatar menu, so neither is a rendered link until it is opened. That is not a finding of
this stage: `sitemap.md` D-desktop-1 states the tradeoff and records that it was accepted for a lean
header, with the hamburger reserved to surface more as the app scales.

### What the tab pass found that the stylesheet could not

**440 focus stops on invisible controls, on 88 screens, at every width**, all of them the five links
of the condensed category band. `max-height:0` takes a band off the page, `overflow:clip` takes it
away from the pointer, and `opacity:0` takes its ink, and **not one of the three touches the tab
order**. Every one of the five also sits under `aria-hidden="true"`, so the stop was invisible to the
eye and unnamed to a screen reader at the same time.

`visibility` is the property that closes it, and it is now in both trees: the collapsed band is
`visibility:hidden` and the `.scrolled` band is `visibility:visible`, in `components/header.css` and
in the 87 grey files that carry their own copy of the rule. **440 to 0 in the paint and 0 in the
grey, with the band still opening on all 87.** The layout control is 0 differing rows of 24, which it
had to be: `visibility` reserves the box it hides.

**The open state is left, on purpose, as `docs/backlog.md` 118.** With `.scrolled` forced on, the
band is 54px tall with five visible operable links and still says `aria-hidden="true"`, and on **48 of
the 105 screens it is the only category navigation in the document**. Which way that resolves is a
question about the navigation model, and this stage may not answer it.

### Three instrument errors, recorded because each one changed a number

- **`getBoundingClientRect` plus a `display` walk called a shut dropdown painted**, 1,752 times. A
  closed `<details>` puts its children in `::details-content` at `content-visibility:hidden`: they
  keep a box and a computed `display` and are never rendered. `checkVisibility` is the only one of
  the three instruments that caught both this and the `opacity:0` band, so it is the one the numbers
  above are taken with.
- **The first Tab walk was capped at 120 stops and never reached the bottom bar**, which sits after
  the footer in the DOM: it reported 0 stops in a carrier that has 4. The bar's first tab stop on the
  event feed is number **87 of 118**.
- **The harness counted as product navigation**, `.wf-nav` arriving in the accessibility tree as a
  fifth landmark. That is the fifth reading this chrome has entered in this stage, so it is removed
  before the walk rather than subtracted after it.

And the census that had to be corrected twice: a first pass called 1,063 controls ghosts by counting
anything invisible, which swept in every `display:none` control the rungs turn off. **`display:none`
is the RIGHT way to hide, because it takes the control out of the tab order with it.** A ghost is
only a control that is invisible AND still has a box, and it is proved by focusing it and asking
where focus landed. 1,063 became 446, of which 440 were the band and 6 are `.ptab-in`, the visually
hidden radio of the CSS-only profile tabs, whose ring `tabs.css` already forwards to the label.

**And 18 of the 105 were hiding behind a modal.** The sheet screens read 0 ghosts not because the
band is fixed there but because a `<dialog>` shown modally makes the rest of the document inert. The
honest pair of numbers is 440 on 88 screens now and 525 on 105 the moment a sheet is shut.

## Component behaviour on width

Step 4, 2026-08-12.

### The registry holds, and it was checked rather than trusted

Every `@media` in `components/` read and every number compared against the ladder:

| number | rules | verdict |
|---|---|---|
| 639.98 / 640 | 8 / 6 | DESK, both sides |
| 759.98 / 760 | 4 / 3 | DETAIL, both sides |
| 900 | 6 | RAIL |
| 560, 620, 980 | 2, 1, 1 | **named one-offs**, and each carries its own measurement beside it, closed by backlog 72 |
| 1140 | 2 | HARNESS, not the product |

**33 width queries, every number on the registry, and 0 `@media` in any of the 106 screen files.**
It read 33 when this table was drawn, 35 from 2026-08-12 when `options.css` and `yesno.css` each
took one at the desk rung so the outcome row could wrap, and 33 again from 2026-08-13, when backlog
129 deleted the one in `tokens.css` and the one in `card.css`. **The table above was not edited on
either day and is right for the third time by accident**, which is the argument for reading a count
out of the source and not out of a paragraph: the prose beside it said 16 at the desk for a day
while the table said 14, and only one of them was ever recounted.
The three one-offs were not taken on trust either: each one says in a comment what collapsing it to
the nearest rung would cost, in pixels, and 560 and 980 both cost a control or a card going backwards.

### The measure, placed on three classes, and the audit's own number corrected

| | before | after |
|---|---|---|
| continuous wrapping text blocks | 775 | 777 |
| **over 75ch** | **15** | **3** |

The three that remain are the `.feed-seo` family, two paragraphs and a `dd`, and they are an existing
decision: `--container-read` is 800px and `tokens.css` says why.

| placed on | file | was |
|---|---|---|
| `.resolution` | `event-detail.css` | 9 elements at up to **106ch** |
| `.sys-note` | `state-block.css` | 1 at **154ch**, the longest line in the product |
| `.protect.protect-page` | `notice.css` | 2 at 77ch, and one 117-character line that never wrapped |

**Step 1 said 38 and the number is 12.** The step-1 pass measured the element's box, and
`.related-list li` is a flex row of a 46px thumbnail, a question clamped to two lines and an odds
figure: **a 106ch box with no 106ch line in it**, 27 times, which was 27 of the 38. The corrected
filter is itself the finding, and it is written into `tokens.css` beside the token: of 775 candidates
it throws out 261 standing on one line, 40 line-clamped, **27 whose child is laid out as a row**, and
3 holding a block of their own.

**A cap was also written and taken off within the hour.** The walk reported one `dd` at 89ch, and the
only `dd` family the how-it-works page has is `.hiw-faq dd`, so the cap went there with a paragraph
about the icon column. Reading the ancestor chain rather than the tag name, the element is
`dd < dl < section.feed-seo` on `event-feed-logged-out.html`: a family already decided, measuring
inside its own rule. **A selector is not an identification**, and the reverted rule keeps its four
lines in `hiw.css` so the next reader does not repeat it.

### Backlog 116 closed: the grey tree computes its columns now instead of declaring them

104 grey files carried `@media (min-width:960px){repeat(3,...)}` and `@media
(min-width:1280px){repeat(4,...)}` plus a two-column rule at 640, against a painted tree that says
the same thing with `repeat(auto-fit,minmax(min(100%,var(--grid-col-min)),1fr))` and no query at all.
**Three rules and two unnamed widths deleted from all 104, replaced by the one fluid track.**

Counted in a browser rather than read, one column count per width:

| | 360 | 639 | 640 | 641 | 760 | 900 | 960 | 1100 | 1280 | 1440 | 1600 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| painted | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 |
| grey | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 4 |

**The mechanism agrees and the container does not**, which is a different statement from the one the
row opened with. Both trees now compute from a 300px floor and neither declares a count; the grey
reaches each step earlier because its content column is wider at the same window and its gap is 10px
against the painted `--space-16`. The row asked for the hard-coded count to go, and it is gone. The
column-width difference between the trees is not this row and is not invented by this edit.

## Container thresholds

**Still none in the product, and the reason is a measurement rather than a preference.** `@container`
and `container-type` are both 0 in `components/`, in `ui-visual/` and in `wireframes/`, and 1 each in
`ui-kit/_page.css`, where `.tk-cq` gives the third mechanism a specimen a reader can drag. A
container query earns its place when one
component stands in two materially different slots, because that is the case a media query answers
wrongly. The three families the audit marked "container" (Notifications, Wallet, How it works) each
stand in exactly one place in this product, so a query on their container would resolve the same as a
query on the window, every time, in more syntax. **A container query with one placement is a media
query wearing a different name.** The threshold to revisit is the first component placed in two
columns of different widths.

**THE THRESHOLD WAS CROSSED, AND IT HAD ALREADY BEEN CROSSED WHEN THIS SECTION WAS WRITTEN.**
Re-measured 2026-08-12 over every placement of all 47 components on the 105 painted screens at
thirteen widths: **35 of 47 meet the test stated above**, 22 standing in three or more slots more
than 25 per cent apart, 15 in four, 10 in five. **The reason the stage missed it is worth more than
the number**: it went looking for the case among the organisms its own audit had marked AIR, and the
case was in the atoms, which the audit had no row for. Three components carry it. `card` declares one
rule, `max-width:639.98px`, while its box measures 232 at 320, 500 at 640, 300.5 at 759 and 301.5 at
1440, so the branch fires and does not fire for boxes of the same size, which is the one question a
window cannot answer. The rail is a single container change, `.subcat` going 761 to 214 at RAIL,
written as a WINDOW query in two files. `navitem`, 995 placements, has no rule at all and stands at
79 to 159 in the bottom bar, 194 in the avatar menu and 254 to 258 in the notification menu.
**The refusal above is left standing rather than rewritten, because it is the argument that was
made and the record is of what was decided**; what is corrected is the belief that its own condition
had not been met. Whether the answer is a container query or placements that stop disagreeing is a
design decision and not a measurement, and it is `docs/backlog.md` 129.

### Backlog 129 answered, 2026-08-13: neither query, and the threshold was the wrong test

**The answer is that no container query is written, and the ground is a third measurement rather
than either of the two above.** The threshold the stage named, one component in two columns of
different widths, is a NECESSARY condition and was read as a sufficient one. It says nothing about
whether the component has anything to say about width: the table further down this page reads **35
of 45 filling their container with no width behaviour of their own at all**, and a component with
no rule has no branch that can fire wrongly. So the count of 35 of 47 is true and does not decide
anything. **The population that CAN misfire is the 21 components that own a width query**, and it
was measured directly instead: every selector standing inside a width query in `components/`, read
against its PARENT'S CONTENT BOX on all 105 screens at each rung and one pixel either side.

| the 52 selectors that stand inside the 33 width queries | n |
|---|---|
| the page frame, the shell and the harness, where the window IS the subject | 14 |
| a positioning context, `position:relative` under a dropped panel, which has no width in it | 2 |
| a component in a slot | 36 |

**Of the 36, 25 stand in the product on both sides of their own rung and were tested for the only
thing that decides this question: SEPARABILITY.** A container query can stand in for a window query
exactly when some container width T divides the placements the same way the rung does, in either
direction. Measured before the two fixes below: **24 of 25 separable.** For every one of those a
container query would resolve identically at every placement on all 105 screens, which is the
sentence the stage wrote, and the count of 35 of 47 never touched it. The two selectors with a
genuinely large spread between placements, `.chip-nav` at 119 to 537 and `.filter-menu` at 314 to
611, are exactly the two that set a positioning context: they are the only rules whose container
really does disagree, and a containing block has no width in it to get wrong.

**What the measurement did find is the opposite defect, and it was one token.** Both page insets
STEPPED at DESK 640, `--gutter` 14 to 40 and `--plate-inset` 16 to 28: **38px a side, 76px in
total, spent at the pixel where the window got ONE pixel wider.** The content column went 611 to 560
and the card on `event-feed.html` went 577 to 502 and did not reach 577 again until 715. Nine
component rules are keyed to that rung and every one of them fires on the wrong side of its own box:
the bookmark pull in `card.css`, the outcome wrap in `options.css` and `yesno.css`, the four-column
figures in `position.css` and three rules in `footer.css`. **That is what a rule asking the window a
question about a container looks like, and it needed no container query to show it, only a reading
taken one pixel either side of the rung.** Both insets ramp now, DESK 640 to DETAIL 760, and the
length of the ramp is derived: 38px a side has to be spent at no more than half a pixel per pixel of
window or the column still goes backwards, so it cannot be shorter than 76px, and 760 is the next
rung on the ladder. Below 640 and at 760 and above, **0 geometry readings of 18,660 differ.**

**And `card`, the component the row put first, carries the case exactly as the row said and for none
of the reasons it gave.** Its one rule is the bookmark pull, and the pull is not a phone fact: the
bare icon button pulls its own invisible 44px target back by `(44 - 16) / 2 = 14px`, a card has 13px
from its content edge to its clip edge, and `.card` is `overflow:clip`, so **one pixel of a 44px
target was cut off 84 cards at every width from 640 to 1600** while the query hid it below the rung.
The rule is unconditional now. **The answer to "container query or media query" was neither**, and
the card is 12px taller at the desk because its meta row finally reserves the target that mobile has
always reserved: 25px to 37px, which is the phone's number.

Measured after both edits, all 105 screens at twelve widths: **boxes overflowing 247 to 163 at every
width at and above 640, which is the number the tree already read below it; controls cut by the card
they stand in 84 to 0, worst overhang 5px to 0; horizontal scroll 0 before and after.** The control
for the instrument was an unchanged tree measured twice: **0 differing readings of 18,660.**

**AND THE RAMP MADE THE FIRST REAL CONTAINER-QUERY CASE THIS SYSTEM HAS EVER HAD, which is the one
result nobody was going to guess.** Re-running separability after the fix gives **22 of 25**, not 25:
by taking the discontinuity out of the column at 640 it also took away the thing that let a container
threshold stand in for the window there. The three that a container query can no longer reproduce are
named rather than converted:

- **`.icon-btn.icon-btn-tile` at the 560 one-off**, and it was the one exception before the fix as
  well. Its container measures **92 on both sides of the rung**, so no threshold divides anything:
  the rule is about the screen the control is on and not about its box, which is the honest reason a
  window query owns it.
- **`.opt-row` in `options.css` and `.yesno.compact` in `yesno.css`**, the pair that makes the
  outcome buttons take a row of their own below the desk. Their container now reads **551 to 570 at
  639 and 552 to 571 at 640**: continuous, which is what the ramp was for. So two rows of the same
  width, one at 639 and one at 640, lay their outcome pair out completely differently, and the pair
  goes from 268px a half to 46 and 42.5 at one pixel of window. **That is the case the stage was
  looking for, and it did not exist until this file made the column honest.**

They are filed and not converted, because converting them means declaring `container-type` on the
row's container, and size containment is a change to what an element's width MEANS rather than to
what it measures. That needs its own measurement and its own day: `docs/backlog.md` 145.

### What each component does with width, filled for all 45

`inventory.md` carries the column now, read from the product at twelve widths on the screen where
each component stands widest, with every dialog opened.

| verdict | n | what it means |
|---|---|---|
| **FILLS its container** | 35 | no width behaviour of its own at all |
| **FIXED** | 5 | chip 81px, filters 152, logo 86, navitem 258, toggle 44 |
| **CHANGES its share** | 3 | betpanel, dialog, skeleton |
| **GONE in a band, then fixed** | 2 | button through `.hiw-btn`, iconbtn through the hamburger |

**35 of 45 have nothing to say about width**, which is the system working: adaptation lives in the
shell, the patterns and the page frame, and the bricks take what they are given. So the
"What it does with width" section was written on the **21** pages whose component owns a width query,
and on no others, because a section saying "nothing" on 24 pages is noise that the inventory column
already carries once.

**The column reads the component against its PARENT'S CONTENT BOX, and that correction is the
finding.** Measured against the window, **33 of 43 read as stepping at 640**, because the page gutter
goes 14 to 40 there and takes 51px out of the content column: that is the frame's behaviour arriving
in every row. Measured against the parent's BORDER box, seven more read as changing their share,
because the parent's own padding steps at the same pixel. **A component that is fluid inside a
container that steps is still fluid.** The same pass first picked `.sel` as the probe class for three
different components, because a class named by two component files is nobody's, and it read `button`
as "gone in a band" because the widest `.btn` in the product is `.hiw-btn`, which is one face of
eight and `display:none` below DETAIL.

### The ban is written in two places

**No `@media` in a screen file, ever.** It is in `components/CLAUDE.md` and in `ui-visual/CLAUDE.md`
both, because a rule kept in one place is a rule half the hands never meet, and this tree is
assembled by many hands at once. Measured: 33 width queries in the system, **0 in any of the 106
painted screens**.

### Backlog 43, and the answer is no

The row had been open since 2026-08-08 waiting for this stage by name: **do the raw layout px need a
scale of their own?** Censused with comments and media queries excluded, because prose is not a rule
and a rung is registered elsewhere: **88 genuine layout literals in 51 distinct values, not 81.** The
row's 81 had counted **127 box-shadow numbers and 6 filter numbers**, and a shadow offset is not a
layout dimension.

**No, and it is not a shrug.** A ladder is for values standing in a RELATION, which is what makes
`--space-8` and `--space-12` two steps of one thing. 214, 300, 196, 322 and 160 stand in no relation
at all: each is one measurement of one part, and a shared scale would invent an arithmetic nobody
measured and send every later reader looking for meaning in the gaps.

**What some of them needed was a name, and the test is how many files use one.**

| | |
|---|---|
| in exactly one file | **44 literals**, 36 values, 18 files. Each is that component's own measurement and stays there |
| shared by two files or more | **44 literals**, 15 values, of which only **two are one fact** |
| `--rail-width:214px` | `toc.css` and `catnav.css` had already agreed **in prose**: the comment says "the same 214px" and nothing held it |
| `--menu-min:196px` | the floor of any panel hanging off a control, in `header.css` and `filters.css` |
| refused | a `--sticky-gap`. The 16px at the foot of the three sticky columns is `var(--space-16)` now, for the reason `--grid-gap` was refused |
| left raw | the three sticky top offsets, 120, 120 and 66: they measure what stands above each column, and that differs |

Tokenisation proved inert: **0 differing rows of 30** computed readings, six elements over five widths.

---

## Step 5. New behaviour, in the short form

The audit named none, and the stage does not invent one to fill a step. The full argument is under
"New behaviour is refused" above and it rests on `ia/docs/flows.md`: the product has exactly one
list-and-detail pair, and Event Detail is a **mandatory context screen** carrying growth zone 2 from
`cjm-as-is.md`, "explain the number, tell the story". A split view would halve exactly the screen the
product exists to widen, and none of the five named growth zones is "I lose my place going back and
forth". There is no second pair: bets, notifications and the wallet have no detail screen at all.

**A step answered in the short form with a reason is an answer.** No new state, no focus management,
no history handling, and no microcopy for an empty pane that would have needed writing.

## Step 6. The width sweep

The instrument of the whole stage, because **a defect lives between the points**: three snapshots at
three widths prove three widths, and the worst width is the one where something no longer fits and no
rung has fired yet.

**320 to 1600 at 40px, 10px within 20 of each rung, and one pixel either side of each rung: 50
widths.** Each screen is loaded once and resized, so the reading is of the layout rather than of
10,000 page loads.

| | readings | result |
|---|---|---|
| painted tree, horizontal scroll | 106 x 50 = **5,300** | **0 chasm widths** |
| grey tree, horizontal scroll | 104 x 50 = **5,200** | **0 chasm widths** |
| carriers and `.desk-only` | **5,250** | **0 disagreements** |

Below 640 the bar stands and every `.desk-only` is off; from 640 up the mirror. At every one of the
50 widths, on every screen that carries both.

**The control came first, because 0 is the answer a blind probe gives too.** A 2000px block injected
into five screens was seen in **20 of 20** readings at 320, 640, 900 and 1600. The probe is not blind,
and only then was the 0 worth reporting.

---

## What is not taken

`docs/backlog.md` items 115 and 116, opened by this stage.
