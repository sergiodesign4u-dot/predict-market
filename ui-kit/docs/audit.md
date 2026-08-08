# The audit - one run, and what it found in itself first

Step 5 of the rebuild, 2026-08-08, and the last step. **115 documents at two widths in two themes,
460 renders.** Contrast, overflow, focus, accessible names, alt text, duplicate ids, controls the
User Agent is still painting, broken links and touch targets.

**Read once, written down, done.** Nothing runs any of this on a schedule and no check reads this
file. The instrument was written in the scratchpad, run, and deleted.

The reports before it: [`census.md`](./census.md), [`inventory.md`](./inventory.md),
[`consolidation.md`](./consolidation.md).

---

## The headline

**The audit found six defects in itself and one in the product.**

That ratio is the report. Every one of the six made the instrument report something that was not
there, three of them at a scale that would have been believed: 434 daylight contrast failures, 212
overflows, 14,377 undersized targets. All three were the instrument. **The one product finding is
that the project's own 44px touch floor is not what the system builds to**, and it is a decision
rather than a bug.

> **CORRECTED 2026-08-08, and the headline was wrong twice over: the count is EIGHT, and the one
> product finding was the eighth.** The touch pass measured the product with a mouse. The full
> account is [correction 8](#8-the-touch-pass-measured-the-product-with-a-mouse-and-it-was-the-one-product-finding)
> below and the numbers in the touch-target section are struck rather than deleted. What the audit
> got right is unchanged and is most of it: contrast, overflow, focus, names, alt, ids and links all
> still hold. **The paragraph above is left standing because it is what the report claimed**, and a
> report whose headline is quietly rewritten is a report that cannot be checked. Seven of the eight
> corrections were found by disbelieving the instrument; the eighth was found by a later pass, which
> is the part worth keeping: **an instrument nobody disbelieves twice is an instrument that has
> stopped being disbelieved.**

---

## What was measured

| | |
|---|---|
| documents | **115**: 106 painted screens + 9 kit pages |
| widths | 390 and 1280 |
| themes | Vault (graphite) and Daylight |
| renders | **460** |
| text elements measured for contrast, per pass | **29,929** at 1280, **29,984** at 390 |
| text elements the instrument could not measure | **0** |

**The grey tree is not in this.** `wireframes/` is frozen, carries no colour and no theme, and the
rules forbid running anything that could act on a finding there. An audit whose every result arrives
with "not fixed, by rule" attached is a report nobody can use.

---

## The eight corrections, in the order they were found

**A before-and-after needs an instrument that returns the same answer twice.** So does an audit. Each
of these was caught by disbelieving a number, and each is recorded because the next person to write
one of these will meet all eight.

**Six were found before this report was written, the seventh the same day, and the eighth two hours
later by the pass that went to fix what the seventh had left standing.** The heading said six for
most of a day, which is the honest shape of it: the count of an instrument's defects is a lower
bound and never a total.

### 1. A noise texture is not a gradient

The first ground-walker bailed on any ancestor with a `background-image`, because a gradient cannot be
composited naively. **191 of 452 text elements on the feed came back unmeasured**, 42 per cent.

Reading what those images actually were settles it: `.device`, `.cat-nav`, `.hero-feature`,
`.hero-trust`, `.hero-promo` and `.hero-hot` carry
`url("data:image/svg+xml,...feTurbulence...")`, a **fractal-noise grain**, which is the Vault
material and not a colour. The fix distinguishes the two: a background-image with no gradient stop is
a texture and the colour underneath still decides; a real gradient is parsed and the text is tested
against **every stop**, worst case wins. **Unmeasured went to 0 on all 460 renders.**

### 2. A closed `<details>` has a box and paints nothing

Every screen reported two elements past the right edge, `.dropdown` and `.dropdown.notif-drop`, at
x 1125 to 1385 on a 1269px document. **212 findings across the tree, and the page scroll was 0 on
every one of them**, which is the contradiction that gave it away.

Chrome puts a closed `<details>`'s content in `::details-content` with `content-visibility:hidden`.
The child still computes `display:block`, still returns a 260x185 rectangle from
`getBoundingClientRect()`, and **is never painted**. Nothing in `getComputedStyle` on the element
itself says so. The visibility test now asks whether an ancestor is a shut `<details>` or a shut
`<dialog>`.

### 3. Text at `font-size:0` is not text

12 contrast failures on the feed at 1:1, all of them the string "thumbnail placeholder" inside
`.thumb`. It is a label set to zero and never seen. **119 across the tree.** Skipped now, and
counted separately so the number is not silently lost.

### 4. The batch raced the load, and this is the one that would have been believed

```js
await new Promise(r => { f.onload = r; setTimeout(r, 900); });   // resolves on WHICHEVER fires first
```

A page slower than 900ms was measured mid-load, and the theme attribute was set on a document about
to be replaced. It reported **434 contrast failures in Daylight and 0 in Vault**, with
`.btn-secondary` at 2.40:1 on 100-odd screens.

Measured on one of those screens with the load awaited: **13.93:1.** The button was never wrong.
The fix awaits `onload` with a 6s guard rather than a race, writes the theme to `localStorage`
*before* the load so the page's own boot agrees instead of being corrected afterwards, and settles
two animation frames. **Product failures went to 0 in both themes at both widths.**

### 5. The drawer is not an overflow, and the chrome is not the product

`.sidebar` sits at -220 to 0 on every narrow render: that is the course drawer at
`translateX(-100%)`, the idiom, on **115 renders**. Overflow is measured to the right only now, and
the left edge is left to the page-scroll number, which is what a person actually feels.

And **14,377 undersized touch targets** were the course panel's own rows, 107 per page. The panel is
chrome. Targets are counted inside `.app-case` now, and the chrome is counted separately so it is
not hidden: `.sidebar-sub-link` is 219x26 and there are 11,028 of them.

### 6. The system's own shape hid its focus rules from the CSSOM

The focus pass found **0 `:focus-visible` rules in any stylesheet**, which is impossible:
`course-chrome.css` writes two and `tabs.css` writes seven.

`components/index.css` is nothing but `@import`, so the document has **one** stylesheet with **50
rules, every one a `CSSImportRule`**, and an imported sheet's rules live on `.styleSheet.cssRules`
rather than on `.cssRules`. A walker that follows only the second sees an empty system. Read from the
source files instead, and confirmed in the browser with real focus.

### 7. The label extractor invented a string that is not on the page

Recorded 2026-08-08 in the links section below, where the withdrawn finding is quoted in full.
`Privacy Policynot built` was reported as a broken footer label; `terms.html` writes
`<span class="rel-q">Privacy Policy</span><span class="rel-odds">not built</span>` inside one anchor,
four times, and the extractor joined the siblings. **The only one of the eight that reached a
document before it was caught.**

### 8. The touch pass measured the product with a mouse, and it was the one product finding

**The instrument never asserted the thing its own criterion is about.** WCAG 2.5.5 is about a finger,
this system binds its 44px floor to `@media(pointer:coarse)` and has since step 7, and
`components/button.css`, `header.css`, `iconbtn.css`, `tabs.css`, `filters.css` and `chip.css` each
carried a coarse block saying so in a comment. Headless Chromium reports `pointer:fine` and
`maxTouchPoints:0`. Nothing in the run read `matchMedia`, so **all 460 renders measured the 36px
branch** and the result was filed as a product defect: 1,787 of 2,709 targets under 44.

Read again with `Emulation.setTouchEmulationEnabled` on and `matchMedia('(pointer:coarse)')` asserted
true before every read, over the same 106 screens at 390: **262 short, not 1,787.** The finding was
one sixth of what was reported and it was not the shape the report gave it.

**This is the same species as correction 4 and it is the worse one.** Correction 4 raced the load, so
the instrument read the page at the wrong TIME. This one read the page on the wrong DEVICE, and it is
worse because a load eventually finishes and a mouse never becomes a finger: no amount of re-running
would have found it. What found it was going to fix the finding and reading the six comments that had
been explaining the floor to nobody.

**The lesson is narrower than "test on a device".** The system's rule was written down, in six files,
in prose, in the exact words `TARGET SIZE FOLLOWS THE POINTER AND NOT THE VIEWPORT`. An audit that
measures a criterion the system answers CONDITIONALLY has to assert the condition, or it is not
measuring the criterion. A media query is a condition, and an unasserted condition is a value the
instrument chose without saying so. **A missing value is a value**, which is this repository's oldest
rule and it turns out to apply to the instrument's inputs and not only to the page's.

---

## The results

### Contrast: 0 failures in the product, in either theme, at either width

Composited grounds, alpha resolved up the ancestor stack, gradients tested against every stop.
4.5:1 for a word, 3:1 for text at 24px or at 18.66px bold.

| | Vault | Daylight |
|---|---|---|
| product, 1280 | **0** of 29,929 | **0** |
| product, 390 | **0** of 29,984 | **0** |
| the kit's own pages | 37 | 58 |

**Every one of the 37 and 58 is on `colour.html`, and every one is the primitive ramp.** The ramps
print each step's number on the swatch that IS that colour: `600` on `p-bone-600` reads 1.36:1,
`930` on `p-graphite-930` reads 2.38:1 in Daylight. A 9px label on its own colour cannot clear 4.5
and **should not**: the swatch is the specimen and the number is its name. It is still worth fixing,
because a number nobody can read is a number that gets copied wrong. **Backlog 47.**

The other kit readings are the contrast matrix's own cells, `icon-quiet` at 4.32 and `icon-brass` at
3.40, which are **specimens of a graphical role held to the text floor by a general instrument**. An
icon's floor is 3:1 and `colour.html` says so beside them.

### Overflow: 0, on all 460 renders

| | |
|---|---|
| elements past the right edge that cannot scroll | **0** |
| documents with horizontal page scroll | **0** of 115, at either width |

### Focus: one rule, and it reaches everything

`base.css` line 67, and it is the whole answer:

```css
:focus-visible{outline:var(--ring) solid var(--focus-ring);outline-offset:var(--ring)}
```

A bare `:focus-visible` with no subject matches every element, so **coverage is 100 per cent by
construction** rather than by enumeration. Across the system:

| | |
|---|---|
| files writing a `:focus-visible` rule | **9** |
| selectors | **18** |
| drawing an outline or a shadow | **13** |
| refining one that already exists (offset, radius, colour) | **5** |
| removing one without replacing it | **0** |

Confirmed with real focus rather than from the source, on `event-detail.html`:
**56 of 56 focusables inside `.app-case` take a 2px ring**, 51 at `+2px` offset and 5 inset at
`-2px`, and the five are the ones whose own files ask for an inset ring and say why. **0 naked.**

`input.css` is the only place that writes `outline:none`, on the bet amount field, and it
out-specifies itself back with a `box-shadow` glow on `:focus-visible`. The reason is written above
the rule.

### Names, alt, ids: 0

| | |
|---|---|
| links, buttons or summaries with no accessible name | **0** over 460 renders |
| `<img>` without `alt` | **0** |
| documents with a duplicated id | **0** of 115 |

The last one is worth pausing on, because [`organisms.html`](../organisms.html) found that
**nine declarations in the system are keyed to a document-unique id**. This confirms the other half
of that finding: the coupling exists and **it has never fired**, because no shipped screen carries
any of the 13 ids twice. Backlog 45.

### The User Agent is still painting 420 controls, and none of them is visible

Measured as the symptom rather than as the cause: an element wearing a system class whose computed
border is `outset` or whose ground is the User Agent's `rgb(239,239,239)`.

| | |
|---|---|
| found, per render | **420** |
| visible | **0** |

All of them are `.chip-amount` inside closed `<dialog>` elements, outside `.app-case`, which is
exactly what [`consolidation.md`](./consolidation.md) found by reading and what backlog 42 records.
**The audit turns "28 chips in closed dialogs" into a number the whole tree agrees on, and confirms
that nothing renders wrong today.** It is latent, and latent is not fixed.

### Links: 0 broken, and 1,902 that go nowhere on purpose

| | ui-visual | ui-kit |
|---|---|---|
| internal links | **15,880** | 26 |
| broken (target does not exist) | **0** | **0** |
| `href="#"` | 2,427 | 123 |
| in-page anchors | 878 | 118 |

**The `href="#"` count is backlog 27 and 28 re-measured, and it grew.** The record says 16 distinct
labels over 1,664 links; today it is **23 distinct labels over 1,902 anchors**, and **17 of them
stand on 105 screens each**: Sports, Trending topics, Leaderboard, API / Developers, Status, Help
Center, FAQ, Contact, About, Careers, Press, Brand, Terms, Privacy, Privacy Policy, Responsible play,
Geo restrictions.

Two of those are the same destination under three spellings: **Privacy** and **Privacy Policy** in
the footer, and **Privacy policy** on `cookie-consent.html`. **Backlog 48.**

> **Corrected 2026-08-08, and it is the seventh instrument defect and the only one that reached a
> document.** This section first reported a fourth label, `Privacy Policynot built`, and called it a
> broken string. It is not. The markup on `terms.html` is
> `<a href="#"><span class="rel-q">Privacy Policy</span><span class="rel-odds">not built</span></a>`,
> a Related card whose odds slot says "not built" on purpose, and the tag-stripper that extracts a
> label joined the two spans. Four cards there do the same. **A label extractor that concatenates
> siblings invents strings that are not in the page**, which is the same species as everything in the
> six above, and it is written here rather than quietly deleted because the report's whole argument is
> that an instrument has to be disbelieved first.

### Touch targets: the one product finding

> **EVERY NUMBER IN THIS SECTION WAS READ WITH A MOUSE. Corrected 2026-08-08, see correction 8.** The
> 44px floor is bound to `@media(pointer:coarse)`, this run never asserted a coarse pointer, and
> headless Chromium reports `pointer:fine` with `maxTouchPoints:0`. So the table below is the
> product's FINE-pointer branch measured against a floor that only a finger was ever meant to raise.
> The section is kept as written, because what it measured it measured correctly and the reader has
> to be able to see what the mistake looked like from inside.

At 390, inside `.app-case`, every link, button, field, select and summary that is not an inline run
of prose.

| | |
|---|---|
| targets | **2,709** over 106 screens |
| clearing **24x24**, the WCAG 2.5.8 AA floor | **2,692** |
| below it | **17** |
| clearing **44x44**, this project's own floor | **922** |
| below it | **1,787** |
| of those: short but wide enough | 1,413 |
| narrow but tall enough | 94 |
| both | 280 |

**AA is met and the project's own standard is not.** The 17 below 24 are all wide rows that are
short, not small dots: `.market-head` at 310x18 on 9 screens, `.hh-name` at 202x20 on 5, `.hh-all`
at 110x20, two prose links at 83x23. Not one of them is a control a thumb has to find.

The 1,787 are one decision repeated, not a hundred mistakes:

| Control | Rendered | Count |
|---|---|---|
| `.chip .chip-quiet` | 38px tall | 530 |
| `.chip .chip-lane` | 41px tall | 312 |
| `<summary>` (the filter menus) | 36 and 35px | 234 |
| `.logo-btn` | 40px tall | 105 |
| `.btn-primary` / `.btn-secondary` | 36px tall | 138 |
| `.btn-bare` | 25px tall | 72 |
| `.chip .chip-rail` | 26px tall | 63 |
| `.icon-btn` | 36px tall | 32 |
| `.icon-btn-tile` | 28px tall | 27 |

**The system builds to 36 and 38. The standard says 44.** That is one number in one place and it is
the same question backlog 40 already asks: three control heights are declared and twelve render,
because 192 of 317 boxed controls get their height from padding plus font size plus a border rather
than from a token. **A control that read a height token would be one edit away from 44; a control
that computes its height from three other values is 317 edits away.** So this is not a separate fix,
it is the argument for the one already open. **Backlog 49, pointing at 40.**

#### What the same measurement says with a finger

Same 106 screens, same 390, touch emulation on and `matchMedia('(pointer:coarse)')` asserted true
before every read. The target rule is slightly tighter than the run above (a control inside a closed
`<details>` is not a target until it opens, which is correction 2 applied to this pass as well), so
the totals are not the same instrument and only the two columns may be compared with each other.

| | fine pointer | coarse pointer |
|---|---|---|
| targets | 1,790 | 1,790 |
| clearing 44x44 | 762 | **1,361** |
| short | 934 | **262** |
| narrow but tall enough | 94 | 212 |
| under 24x24 | 20 | 11 |

**The floor exists, it works, and 599 targets crossed it the moment the pointer changed.** What was
actually wrong is smaller and different in kind: the floor was written **six times**, and every copy
named a LIST rather than a family, so `.chip-lane`, `.chip-rail`, `.rules-tab`, `.market-head` and
`.toc-link` had no floor at all. That was fixed the same day: one rule in `components/base.css`,
beside the focus ring, keyed to the family. **262 short to 68, and 542 to 98 at 1280.** Every one of
the 68 is text or one of the icon button's four named exclusions. The fine branch was measured to
prove it had not moved: 1,028 under 44 before and after.

The final line of the original finding survives the correction and is worth keeping: the argument
that a control computing its height from three values is 317 edits from 44 was **wrong about the
mechanism**. A `min-height` on the family out-specifies whatever the control computed. It was one
edit.

---

## What is open after this

| | |
|---|---|
| 47 | the primitive ramp prints its step number on the colour it names, 37 and 58 readings under 4.5:1 on `colour.html` |
| 48 | 23 labels and 1,902 anchors behind `href="#"`, two of them the same destination under two names and one a broken string |
| ~~49~~ | ~~1,787 of 2,709 product touch targets under the project's own 44px floor~~ **CLOSED 2026-08-08.** The number was the instrument's. What was real is that the floor stood in six files as six lists; it is one rule in `base.css` now, and 262 short became 68 |
| 50 | 212 targets stand 44 tall and under 44 wide, and 2.5.5 asks for both. They are short words, so the fix is a layout decision about six components rather than a floor. Owner: Responsive |
| 51 | three native checkboxes at 18x18 on `cookie-consent.html`, the only targets under the 24x24 AA floor that a finger has to hit rather than read |

And the three the audit confirmed rather than found: **42** (420 latent User Agent controls, 0
visible), **45** (13 document-unique ids the system depends on, 0 duplicated today), **44** (the
36px drawer toggle).

## What was not measured, and why

**Page weight, font swap and layout shift.** Never measured at any width in either theme, and it is
backlog 5, owned by Handoff. It needs a network profile rather than a DOM walk and it would have made
this a different instrument.

**The grey tree.** Frozen, no colour, no theme, and nothing may act on a finding in it.

**Motion and reduced-motion.** Stage 11's, and there is nothing on these screens to measure yet.

**Anything a mouse does.** Hover and press are live on the kit pages, where a person raises them with
a pointer, and that is where they belong: a frozen copy of a state is a second place the value lives
and it is the one that goes stale.
