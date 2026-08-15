# Consistency - what the system declares against what the product wears

2026-08-15. **1,282 style rules read out of the browser's own CSSOM, 1,144 distinct selector parts,
tested against 163 documents: 106 painted screens and 57 kit pages.** Plus a static pass over the 53
stylesheets for tokens, literals and the contract lines each file carries in its own header.

**Read once, written down, done.** Nothing runs any of this on a schedule and no check reads this
file. Every instrument was written in the scratchpad, run, and deleted. The reports before it:
[`census.md`](./census.md), [`inventory.md`](./inventory.md),
[`consolidation.md`](./consolidation.md), [`audit.md`](./audit.md),
[`responsive.md`](./responsive.md).

---

## The headline

**The contract holds and the edges have rotted.** Every structural promise this system makes is
intact: 53 stylesheets against 53 imports with no orphan and no duplicate, 47 components each with a
page, an inventory row and a route, 0 media queries in the 106 painted screens, 0 inline styling,
**0 unread tokens of 379**, and 1 contract line of 53 that over-claims.

**What is wrong is 22 selector parts that draw nothing anywhere in any state, and a stand that no
longer agrees with the product in nine places.** The largest single finding is that **four of
`print.css`'s rules name classes that appear on zero elements in the whole tree**, so a stylesheet
whose whole job is a medium nobody looks at was aimed partly at nothing.

**The second is the shape of the finding rather than its size**: of the nine disagreements between
the stand and the product, **six are the stand drawing MORE than the product ships**, which is the
opposite of the failure mode this kit was rebuilt to prevent. A stand that shows less is caught by
looking at it. A stand that shows more looks finished.

---

## 1. What could not be faulted

| question | answer |
|---|---|
| `index.css` against the folder | **53 imports, 53 files, 0 on disk unimported, 0 imported and missing, 0 duplicated** |
| the component contract | **47 of 47** have a `components/` file, a page in `ui-kit/`, a row in `inventory.md` and a route in `_nav.js` |
| `@media` in a screen file | **0** of the 106 painted screens |
| `style=` on an element | **387 attributes carrying 435 declarations**, and every declaration is one of the three allowed kinds: **277 the event photograph** (`background-image`, `background-position`, `background`), **151 the odds-bar and depth-bar datum** (`width:NN%` on `.fill` and `.md-bar`), **7 the chart's `--v`**. **0 are styling** |
| custom properties | **379 declared, 379 read**, once `ui-kit/_page.css` is counted as a reader, which it is: showing a value is what the vitrine is for. One is read and never declared, `--v`, and that is correct: it is a datum the markup writes on the element |
| `!important` | **24, and none is in a component.** 9 in `base.css`, 14 in `print.css`, 1 in the course chrome. Each of the three is a place where overriding is the job |
| raw colour outside `tokens.css` | **24, and 0 of them are a theme colour.** 18 are `print.css`'s own greyscale, which a print sheet is entitled to; 6 are `#000` in `catnav.css`, where the value is a mask ALPHA and not ink, and the file says so |
| a ladder step written as a raw px on a sizing property | **6**, and reading each in context, **0 are drift**. `right:18px` is not an icon size and `left:22px` is not one either; they collide with `--icon-18` and `--icon-22` by arithmetic |

---

## 2. Twenty-two selector parts that draw nothing, anywhere

Tested as: strip the pseudo-classes a static page cannot satisfy, ask `querySelector` on all 163
documents, and then ask a SECOND time with every state pseudo and attribute selector removed as
well. **A part that matches nothing even with its state stripped away has no element to reach.**
That second pass is what separates the dead from the merely unpressed: 30 more parts match nothing
today only because a radio is not checked, a `<details>` is not open or a tab is not selected, and
those are not on this list.

### 2a. `print.css` names four classes the tree does not have

```
.action-bar   .notice   .seo-plate   .bets-table
```

**Zero elements wear any of them**, in `ui-visual/`, in `ui-kit/` or in `wireframes/`. They are the
COMPONENT names, and the markup wears the class names those components declare, which are different
words. So four print rules were written by reading the folder listing instead of the screens.

**This is the exact defect this repository has already paid for twice**, and both times in a place
nobody looks: an `aria-hidden` on an operable band, and a `min-height` on an inline box. A
declaration that is present, correct and consulted by nothing. Print is the medium where it can
stand longest, because the failure is only visible on paper.

### 2b. `header.css` reaches for the badge in the wrong parent

```
.bottom-nav .badge-dot
```

`.badge-dot` has **86 placements in the product** and every one of them stands in `.bell-wrap`, in
the header. It is never inside the bottom bar. **A count of the class would have said the badge is
alive**; the question is about the PAIR.

### 2c. `yesno.css` draws a face for a losing side that is never selected

```
.opt-list .yesno.compact button.sel.no
.opt-list .yesno.compact button.sel.no:active
.yesno > a.sel:active
.yesno-pick.sel.no
.yesno-pick-bar.sel.no
```

**`.sel` and `.no` never appear on the same element**, in any of the three trees. The outcome pair
has a chosen-YES face everywhere and its chosen-NO twin has never been rendered. This is not
obviously a defect in the stylesheet: it may be a defect in the SCREENS, which have never shown a
person who backed NO. It is the one finding here that is a product question rather than a cleanup.

**Answered the same day and it was the screens. Section 10.** Four of the five draw now; the fifth,
`.yesno > a.sel:active`, is deleted, and that deletion is a statement about the component.

### 2d. `base.css` resets seven things that are not there

```
pre   kbd   samp   select   .tbd   .placeholder-line   .groove-sep
```

`.tbd` and `.placeholder-line` have 364 and 28 occurrences in the repository and **all of them are in
`ui-visual/old/`**, the pre-Vault archive. A grep says the class is alive; the DOM of all 106 screens
says 0. `pre`, `kbd`, `samp` and `select` are element resets for elements the product does not use.

### 2e. Four more, one per file

```
.protect strong          notice.css     no <strong> inside a .protect block
.reconcile-box b         notice.css     no <b> inside one either
.chart-svg text          chart.css      the chart svg carries no <text>
.theme-switch-inline     course-chrome  and its focus rule with it
```

**Not counted as dead, deliberately:** `.sidebar-page-link.planned` and its three companions match
nothing because there are no rows waiting any more, which `ui-kit/CLAUDE.md` states out loud; and
`.rm-overlay.open`, `.sidebar.open` and `.sidebar-divider.sub.active` are set by script at run time.
A rule whose state a script sets is not a rule with no reader.

---

## 3. Nine places where the stand and the product disagree

The kit's own rule is that a component page may not show less than the shelf does, and that a
specimen is copied from a SCREEN and never written from a stylesheet. Both halves are broken now,
and the second one more often than the first.

### 3a. The stand draws MORE than the product ships, six times

| class | product | stand |
|---|---|---|
| `.hiw-body` | **0** | 7 |
| `.hiw-full` | **0** | 7 |
| `.hiw-arrow` | **0** | 4 |
| `.hiw-hero` | **0** | 25 |
| `.icon-btn-lift` | **0** | 9 |
| `.grid-l` / `.nowline` | **0** | 6 / 2 |

**The how-it-works sheet is the biggest of these and it costs rules in two files.** The product's
sheet is `.app-dialog.hiw-dialog` holding `.sheet-close` and `.hiw-steps`, on all 105 screens that
carry it. It has no body wrapper, no full-width link and no arrow. `dialog.css` writes seven rules
for those three and `hiw.css` writes the hero, and **none of the eight can fire on any screen in the
product.** The stand is drawing a sheet that was designed and never shipped.

**`.icon-btn-lift` is the `account` case again**: a face with no placement. `account.css` was deleted
on 2026-08-08 for exactly this, and its whole argument applies here word for word.

**`.grid-l` and `.nowline` are five hours old.** The chart was redrawn on 2026-08-15 as an area, one
reference line and an end dot; the grid and the now-line came out of the product markup and stayed on
the stand. **A change made in the product and not carried to the kit is the drift this vitrine exists
to make visible, and it took a class census to see it rather than a look at the page.**

### 3b. The stand draws LESS than the product ships, three times

| class | product | stand |
|---|---|---|
| `.filters-scrim` / `.filters-head` / `.filters-foot` | **44 each** | 0 |
| `.filters-head h2` / `.filters-done` / `.filters-reset` | 44 to 101 | 0 |
| `.state-block.state-problem` (+ 2 children) | **21** | 0 |
| `dialog.app-dialog .sheet-body .quick` | **105** | 0 |

The filter sheet is the same age as the chart finding and has the same cause: the face was built into
the product on 2026-08-14 and the kit page describes it in prose without rendering it. **A page that
names a part in a sentence and does not draw it is a page that cannot be checked by looking at it**,
which is the whole argument for a vitrine over a document.

`.state-block.state-problem` is 21 placements of a face the stand has never had.

---

## 4. Zero tokens nobody reads, and the first answer was four

**379 declared, 379 read.** The first pass of this section reported four dead primitives,
`--bone-200`, `--brass-220`, `--ink-700` and `--space-56`, and **all four were the instrument.** It
looked for readers in `components/` and in the markup, and the reader of those four is
`ui-kit/_page.css`: `.tk-p-bone-200`, `.tk-p-ink-700`, `.tk-p-brass-220` and `.tk-sp-56`, which draw
the palette on `colour.html` and the spacing ladder on `geometry.html`.

**A value's reader can be the thing whose job is to show it.** That is what the vitrine IS, and a
sweep for dead values that does not read the vitrine will delete the swatches first. The four were
one edit away from being deleted on that report.

---

## 5. Contract lines that over-claim

Each stylesheet opens with two promises about itself: `Classes:`, the vocabulary it owns, and
`Reads:`, the colour roles it consumes. Both were checked against the file's own body.

- **`bets-table.css` `Classes:` named `.sel` and the file writes no rule for it AND no element inside
  a `.ptable`, an `.act-list` or a `.hold-cols` wears it**, in either tree, read in the DOM. `.sel`
  is the shared chosen-state class that five components declare; this was the sixth naming it
  without owning it or wearing it. **It is the only real over-claim of the 53.**
- **`hiw.css` looked like the worst one and was not.** Its `Reads:` line appears to name six roles it
  never reads, and the six stand inside a parenthetical that says in full that they LEFT for
  `platehead.css` on 2026-08-11. The line is correct and the sweep read the note as part of the
  list. **A contract line that carries its own history is a contract line a naive parser will fail
  on**, and the fix is to the parser.
- **Two more look like over-claims and are not, for a third reason.** `button.css` names
  `.prov-google` and says in the same breath that it "carries its own brand colours in the markup and
  correctly has no rule"; `filters.css` names `.filters-close`, which wears `.icon-btn` and needs
  nothing of its own. **The `Classes:` line is the component's markup vocabulary, not the list of
  selectors it writes**, and that reading is stated in `button.css` and nowhere else. It should be
  stated where the convention is, or these lines will keep being audited against the wrong question.

---

## 6. What is used where

Placements per component across the 106 painted screens, counted in the DOM rather than in the
source, with the number of screens each stands on and its count on the stand beside it. The full
per-class table is [`inventory.md`](./inventory.md); this is the shape.

**The five largest are `button` 5,798, `hiw` 4,542, `chip` 3,752, `card` 2,866 and `navitem` 2,346**,
and four of the five stand on all 105 screens. `hiw` is in that list because its sheet ships on every
screen whether or not anybody opens it.

**The five smallest are `toggle` 3, `action-bar` 3, `loadmore` 9, `profile` 13 and `position-list`
13.** None of the five is a candidate for deletion and each is small for its own reason: the toggle
has three placements and five faces, the action bar is a pattern standing at exactly its threshold of
three screens, and `profile` and `position-list` live on two screens because there are two profiles.

**Nineteen components stand on fewer than 25 screens and twenty-five stand on all 105**, which
leaves three in between. The middle is almost empty, and that is what a system looks like when it has
a shell that is everywhere and a set of specialist blocks that are each on one family of screens.

---

## 7. The instrument, read before the findings

**The first run of the reachability pass reported 73 dead selectors and about half of them were the
instrument.** Two faults, both worth writing down.

**A stylesheet read from `file://` has no `cssRules`.** Every document read from disk gets its own
opaque origin, so the linked sheet is cross-origin to the page that links it and `sheet.cssRules`
throws. The first run reported **0 style rules and then went on to scan 163 documents against
nothing**, and printed 0 dead selectors, which reads exactly like a pass. It is the fourth time this
repository has paid for the disk origin. The pass was rerun over `http://127.0.0.1`.

**An alternation puts the shorter name first and eats the longer one.** The pseudo-stripper listed
`focus` before `focus-visible`, so `.chip-nav:focus-visible` became `.chip-nav-visible`, which
matches nothing, and every `:focus-visible` rule in the system was filed as dead. **A selector that
is not a selector any more still parses**, which is why the count came back plausible instead of
zero.

**And the comma split has to count parentheses.** Splitting `:is(a, button)` on every comma produced
14 fragments with unbalanced brackets, each of which `querySelector` threw on. Those throws were
visible; the two faults above were not, and that is the difference that matters.

**What the corrected instrument still cannot do**, stated rather than hidden: 13 selector parts of
1,144 cannot be asked at all, because stripping their attribute selectors leaves an empty `:not()`.
All 13 are hover or disabled states of controls that are demonstrably alive.

**And two whole findings of this report were the instrument and are struck**, both in section 5 and
section 4 above: the four dead tokens had a reader the sweep did not look at, and `hiw.css`'s
`Reads:` line was correct all along. **Three of the seven findings this pass produced were about
itself**, which is the same ratio [`audit.md`](./audit.md) reported in 2026-08-08 and the reason
neither report leads with its own numbers.

---

## 8. What was acted on, 2026-08-15

The clean deletions first, then the how-it-works sheet, then the last two rows. **Nothing from this
report is left open**: the chosen-NO face and `.icon-btn-lift` are section 10.

| where | what |
|---|---|
| `base.css` | `pre`, `kbd`, `samp`, `select` off two reset lines; `.tbd,.placeholder-line` and `.groove-sep` deleted |
| `notice.css` | `strong` off `.protect`, `b` off `.reconcile-box`, each block naming both tags and shipping one |
| `chart.css` | both `.chart-svg text` rules, and with them the last raw px `font-size` in the system |
| `course-chrome.css` | `.theme-switch-inline` and its ring |
| `header.css` | `.bottom-nav .badge-dot` |
| `bets-table.css` | `.sel` off the `Classes:` line |
| `print.css` | `.action-bar` deleted; `.notice` and `.seo-plate` REPAIRED to the seven classes the markup wears; `.bets-table` repaired to `.ed-tabbar` and `.ptab-bar` |

**`print.css` is the only place where deleting would have thrown away intent**, so three of its four
names were repaired instead. `.bets-table` is the one worth reading twice: renaming it to `.ptable`
was tried first and measured, and `.ptable` computes `overflow:visible` on paper with the rule and
without it, **because that component declares no scroller at all.** The things that scroll in that
block are the two tab bars. **The component name was wrong and so was the component.**

**Proof that the deletions deleted nothing**: 163 documents, **114,754 elements**, 26 computed
properties each, base tree against live tree, **0 differing rows**, with the control (the same tree
read twice) at 0 first and the absolute asset URL normalised because two servers cannot agree on a
port. On paper, measured under `emulateMedia({media:'print'})`: `.protect` goes from a brass edge to
the grey hairline and gains `break-inside:avoid`, `.feed-seo` from **no border at all** to the
hairline, and the two tab bars from `auto` to `visible`, with the screen unchanged at `auto`.

**Left open and named:** `.hold-name` prints truncated with an ellipsis, which is a real paper defect
and a decision about what a printed table is for rather than a repair.

---

## 9. The how-it-works sheet, and the dead rules were the evidence

**The finding in 3a was not a stand that invented markup. It was a rebuild whose stylesheet was not
cleaned up, and it had left a live defect behind.** `git log -S` puts the change at `d214184`,
2026-08-14: the sheet went from two explainer sections plus a FAQ plus a way back to its own page,
into three steps with a picture each where the third one is a way IN. A dated, argued product
decision. `.hiw-body`, `.hiw-full`, `.hiw-arrow` and `.hiw-hero` went out of the markup with it and
their rules stayed.

**One of those rules was doing the sheet's most important job.** `.hiw-body` was the SCROLL
CONTAINER, and the new sheet had none. Measured with the sheet open, the entrance animation finished
and reduced motion asserted:

| viewport | sheet | content | outside the clip | `scrollTop` reads back | step navigation |
|---|---|---|---|---|---|
| 320 x 480 | 441 | 562 | **121px** | **0** | **unreachable** |
| 360 x 568 | 522 | 562 | **40px** | **0** | **unreachable** |
| 360 x 640 | 566 | 566 | 0 | 0 | reachable |
| 390 x 844 | 562 | 562 | 0 | 0 | reachable |

**A frame that clips cannot also be the scroll container**, which is the rule `dialog.css` already
writes for `.sheet-body` twenty lines above the one that broke. The rule names `.hiw-steps` now, and
after it the two short viewports scroll their 121 and 40 pixels and the navigation is reachable at
every size, with 0 at 640 and above where nothing was wrong.

**READ THE ENTRANCE ANIMATION FIRST OR THE NUMBER IS ABOUT NOTHING.** The same probe run without
`getAnimations().forEach(a => a.finish())` put the dialog's top at **428 in a 480px viewport**, which
is the sheet caught mid-slide and reads exactly like a modal rendering below the fold. That would
have been a second defect report about a page that does not have one.

**Deleted with it:** eight rules in `dialog.css` (the body wrapper, the brass link out, its arrow,
its hover, its press and the 3px nudge) and two in `hiw.css` (`.hiw-hero` and its heading size),
plus the four class names off two `Classes:` lines. `.hiw-hero-inner` STAYS with its one placement,
because its one job is to sit above the two absolute layers `platehead.css` paints behind it.

**And the stand was three pages, not one.** `ui-kit/hiw.html` had already been updated on 2026-08-14;
`dialog.html` and `organisms.html` still drew the old sheet and now carry the shipped markup, ids and
radio names suffixed per cell. `vitrine.html` and `platehead.html` showed `.plate-head.hiw-hero` as
one of the face's hosts, and it is the page hero there now. **`platehead.css` was written because
FOUR components wore one face and it is three today**, which costs that file a count and not a rule:
the list is kept at four with the one struck rather than renumbered, because the fourth-host argument
is what decided the shape of the file and it was true when it was made.

---

## 10. The chosen NO, and `.icon-btn-lift`

The two rows left open by section 8, both answered on 2026-08-15.

### 10a. The chosen NO was the SCREENS, and the grey tree is what proves it

**`.sel` and `.no` had never once stood on the same element**: 127 chosen sides in the paint, 24 in
the grey and 39 on the stand, and every one of them YES. Five rules in `yesno.css` drew the other
half of a symmetric control and not one of them could fire.

**A colour layer that had lost a state would show the state in grey and not in colour. Both trees
showed only YES**, so this was not a paint that dropped something, it was a tree that depicted one
path. And the route already existed: backlog 143 gave every card `?side=yes` and `?side=no`, 212
anchors each, so the product had been promising an arrival the screens never drew.

**One screen, in both trees:** `event-detail-bet-processing.html`. It was chosen for a measured
reason rather than a taste one, **its panel is mid-submit and carries no payout figure**, so the
pick moves and nothing has to be kept in arithmetic step with it except the sticky dock, which goes
from `$5 to win $13.20` to **`$5 to win $8.06`**, because five dollars at 62 per cent pays that. The
YES pick inside the how-it-works sheet on the same screen **stays YES**: it is a picture in an
explainer that ships identically on 105 screens, not this person's bet.

**And rendering it for the first time is what let it be measured.** The chosen NO is
`--text-on-no` on `--outcome-no` at **4.64:1**, against the chosen YES at **6.42:1**. Both clear AA
for body text and the NO side is the tighter of the two, which is now a number instead of a guess.

**The stand carries it too**, because a face the product places once is a face a reader should be
able to compare: `ui-kit/yesno.html` gains a NO-taken chooser and a NO-taken row in the outcome list,
in both themes.

**The fifth selector is deleted and the deletion is a statement about the component.**
`.yesno > a.sel:active` still matches nothing, and it should: **a chosen side is a `<button>` and
never an `<a>`**, 16 chosen buttons and 0 chosen anchors across all three trees. The anchor half is
the SPECTATOR's pair on a card, which states a market and records no choice. That is the file's own
sentence about a side being a POSITION IN THE PAIR, read one level further out.

### 10b. `.icon-btn-lift` was decided two days before this report asked

**This row should not have been opened.** The face had 525 placements until 2026-08-13, when backlog
144 took the footer's five social marks out of every screen: five anchors at `href="#"` for accounts
that do not exist, standing directly under the trust strip. **A social account can never become an
internal route, so it was not a link waiting for a screen**, which is what separated it from the two
kinds of placeholder the footer's rules already covered.

**The keep-or-delete question was answered in the same commit, by the product owner, and the
distinction it drew is the right one.** `account.css` was deleted for having no FACE left, its two
rules being another component's stone. This is a face with no PLACEMENTS, and its placements return
on a date somebody chooses. **A component with no face is a name; a face with no placement is a
face.**

What was actually wrong was a number: `ui-kit/iconbtn.html` still published **525** in its touch
table. It reads 0 now, with the reason beside it, so the one row in that table worn by nothing says
so rather than reading as a face nobody measured.
