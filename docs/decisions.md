# Decisions

What was done, why it was done that way, what was rejected and on what grounds.
Entries carry a date, newest first.

**This file is not loaded into a session.** `CLAUDE.md` holds the rules that must act next
time; this holds the record of how they were arrived at. An entry is written once and is
not edited afterwards: a later entry supersedes an earlier one rather than rewriting it,
so a claim here is true as of its own date and nowhere else.

Open items are not here either. They are in [`backlog.md`](./backlog.md).

---

## 2026-08-15 - The stand was 62 pixels narrower than the product at every width, and the cure it had already been given was one it was already taking

**BACKLOG 158 OPENED THE SAME DAY IT CLOSED AND ITS OWN CAUSE WAS WRONG.** The row read "a cell two
themes wide is narrower than any placement" and pointed at the fix this kit had used before: stack
the themes below 640. **Both cells were already stacked.** `header.html` and `betpanel.html` carry
`.tk-stack` on every figure in question, so the remedy the row named was not available to be applied,
which is the tell that the diagnosis was a symptom.

**THE CAUSE IS THAT A COMPONENT AS WIDE AS THE WINDOW CANNOT BE SHOWN IN A CELL THAT HAS MARGINS.**
`.tk-theme-fig` has 16px of padding and stands inside a `.tk-wrap` with 14 more below the desk and 20
above it. Measured in both engines: the header specimen's `.row` is **258 / 298 / 328 where the
product's is 320 / 360 / 390**, short by 62 at every width, and no rung reaches that because it is
not a rung, it is an inset.

**AND THE COST WAS NOT COSMETIC, WHICH IS WHY IT IS A DEFECT AND NOT A COMPROMISE.** `.auth-btns` is
**INTRINSIC at 141 in the product at every width from 320 upward**; in the cell it was squeezed to
114 and 133, so `Sign in` and `Sign up` painted on two lines at 320 and at 360. **A reader who had
never opened the product would have learned a wrapping header from the one page built to teach it**,
which is the same sentence this kit already wrote about a `.btn-md` measuring 68 instead of 47.
`Confirm bet` did it in a 258px dock against the product's 320.

**THE HALF FIX IS THE PART WORTH KEEPING.** Zeroing the cell's own 16px gives **290 / 330 / 360**:
360 stops wrapping and 320 does not. A sweep run at one width, or at the two widths every audit in
this repository used to read, would have called that finished. The cell has to cancel the PAGE's
inset as well, and the negative margin is written at both of the wrap's values rather than one,
because a single number would be right on one side of the desk and wrong on the other. After:
`.row` reads the viewport less this cell's own 2px border at every width to 900, and `.auth-btns`
reads **141**, the product's number, at every width.

**THE CELLS ARE CHOSEN BY ASKING THE DOM, AND THE FIRST PASS PROVES WHY.** Matching `class="app-header"`
as text marked 14 figures, missed 2, and marked ones that did not need it, because a class attribute
is a LIST and a component is rarely alone in it. Asking the rendered tree which figures contain a
`.app-header` or a `.bet-dock` gives 16 over 4 pages, and the sweep then asserts **both directions**:
0 bled cells without a full-bleed component and 0 full-bleed components in an unbled cell. **A
one-directional check would have passed the first pass too.**

**THE CHANGE CANNOT REACH THE PRODUCT AND THAT WAS CHECKED RATHER THAN ASSUMED.** `_page.css` is
linked by the 57 kit pages and by exactly one document in `ui-visual/`, `overview.html`, which is the
index of the tree rather than a screen in it and borrows `.tk-hero`, `.tk-sec`, `.tk-jump`,
`.tk-note` and `.tk-wrap` deliberately. It holds **0 `.tk-theme-fig` and 0 `.tk-bleed`**, and it
renders identically at 320, 390, 640 and 1280 in both engines with 0 errors. The sentence in
`CLAUDE.md` that every painted SCREEN links `index.css` and nothing else is still exact, because
`overview.html` is not one of the 105.

**Verified**: 912 kit renders at eight widths in Chromium 151 and WebKit 26.5, **0 wrapped labels, 0
horizontal scroll, 0 duplicate ids, 0 page errors**, both directions of the bleed assertion at 0.

---

## 2026-08-15 - The bar was short by four fifths of a pixel, and the keyword that fixed it was one letter from the keyword that would have broken the page

**BACKLOG 154 SAID "THE BAR SPLITS THE ROW AND NEITHER HALF IS WIDE ENOUGH FOR ITS OWN WORDS", AND
MEASURING IT FIRST IS WHAT CHANGED THE FIX.** At 320 in both engines: `Browse events` needs
**125.83** and has **125.00**; `Open Wallet` needs **108.61** and has **108.00**. **Each is short by
less than one pixel while its neighbour has thirty and twelve to spare**, and both stop wrapping at
**322**, two pixels above the narrowest width anybody reads. Neither half being wide enough was never
the case. One half is, by a rounding error, because `flex-basis:0` divides the row before asking what
is in it.

**SO THE ROW'S TWO OPTIONS WERE BOTH ANSWERS TO A QUESTION NOBODY HAD.** It offered stack or shrink.
Stacking three screens below 640 would change 360 and 390, which are the widths this project designs
from and where nothing wraps today; shrinking the labels is the type scale paying for a layout. The
third answer is a **floor**: line breaking in flex uses the hypothetical main size, which is the flex
base size CLAMPED BY `min-width`, so a floor reaches a decision `flex:1` alone cannot, while growth
still starts from 0 and **the halves stay exactly equal whenever both fit.** Measured identical to
the old tree at 360, 390, 640 and 1280 on all three screens, 145/145, 160/160, 285/285, 457/457, and
at 320 only the pair that could not fit moves, 125/125 to 126/124.

**AND THE CHOICE BETWEEN TWO KEYWORDS IS THE WHOLE OF IT.** `min-width:max-content` and
`min-width:fit-content` fix today's five buttons identically, to the pixel, on every screen and at
every width. They differ only in a case the product does not have yet: **`max-content` sets a floor
no container can refuse**, so a 40-character label in this bar puts the page into **12px of
horizontal scroll and a 44-character one into 60px**, measured in both engines by writing the label
in and reading `scrollLeft` back. That is trading a wrapped two-word label for the defect this
repository has spent more days on than any other. `fit-content` is `max-content` capped by the space
available, so the same label stacks the bar into two full-width rows at 258 and scrolls nothing.
**Two candidates that agree on every reading of the current tree and disagree on the one that has not
happened yet: the way to tell them apart was to write the input that has not happened.**

**A THIRD CANDIDATE WAS MEASURED AND DID NOTHING, AND THAT IS WORTH THE LINE.**
`min-width:min(100%,max-content)`, which reads as the safe form of `max-content`, left the tree
byte-identical: 125/2 at 320, unchanged. A percentage inside `min()` resolves against a container
whose size is not definite during intrinsic sizing, so the floor never engages. **A guard that
computes to nothing looks exactly like a guard that works.**

**THE CONTROL BROKE BECAUSE THE FIX WORKED, WHICH IS ITS OWN KIND OF READING.** The wrap probe was
proved by squeezing a `.cta-bar` child to `flex:0 0 46px`, which forced two lines before the change
and forces none after it: `min-width:fit-content` overrides the basis, which is the entire point. The
control was re-made to squeeze the BAR instead, 80px, and reads 2 of 2 in both engines with 0
unsqueezed. **When a fix lands, the control that proved the defect may stop being a control**, and a
sweep that keeps running it will report success from an instrument that has gone blind.

**WHAT WAS LEFT ALONE, NAMED.** Two labels in the product still wrap at 320 and neither is in a bar:
`Notify me of new events in this category` is 40 characters in a 226px button on the two empty feeds,
and a label that long is meant to wrap. That is a copy question and it stays one.

**THE SWEEP FOUND A SECOND THING AND IT IS THE STAND, NOT THE PRODUCT.** `ui-kit/header.html` wraps
`Sign in` and `Sign up` at 320 AND 360, and `ui-kit/betpanel.html` wraps `Confirm bet` at 320, in
both engines, while the product wraps none of the three at any width. That is the kit's own rule
about a cell narrower than any placement, met from the other side, and it is backlog 158.

**Verified**: 4,288 renders over 268 documents in all three trees at eight widths in Chromium 151 and
WebKit 26.5: **0 wrapped labels inside a `.cta-bar`**, 0 horizontal scroll, 0 duplicate ids, 0 page
errors, with the control re-made and proved at 2 of 2 before the zero was believed.

---

## 2026-08-15 - The grey tree was one screen short of the tree it decides, and the missing one was the document the product links to most

**THE HOLE WAS CLOSED BY WRITING THE PAGE RATHER THAN BY DECLARING IT A BOUNDARY**, which was the
other option and the cheaper one. `ui-visual/terms.html` had shipped with 882 lines, 25 sections and
a route of its own, **320 anchors in the painted tree reached it**, and this tree had no file and
pointed the same anchors at `#`. Backlog 157. **A destination is structure and structure is decided
here**, so the grey tree owing the paint a page is the one direction the layer rule forbids, and the
repair is the page and not an exemption written into the conventions.

**IT IS BUILT FROM THE GREY `how-it-works.html` AND THAT CHOICE IS THE ARGUMENT.** That is this
tree's own static-content screen: the same chrome, the same logged-out header down to the two
affordances that route to sign-in, the same footer. Building from the painted twin would have ported
the paint's shape into the grey tree, which is the direction the tree exists to prevent; building
from a feed page would have brought a feed. **The base decides which tree the page belongs to.**

**STRUCTURE WAS READ AGAINST THE PAINT RATHER THAN ASSUMED**, in Chromium 151 and WebKit 26.5, at
320, 390, 640, 899, 900, 901 and 1280: **1 `h1`, 25 `h2`, 0 `h3`, 14 `section[id]`, and all 14
contents links resolving to an id on the page**, both trees agreeing on every count. The rail
arrives at **900 and not at 899**, sticky, 214px, with the disclosure head hidden above it, which is
the RAIL rung read at the rung and one pixel either side rather than at two round numbers.

**THE SIX DIFFERENCES WERE CHECKED ONE BY ONE AND ONE OF THEM IS NOT WHAT THE TABLE SAYS.**
`.feed-inner` is dropped and `.cat-layout` is kept, because the table lists all three plate wrappers
together and the 2026-08-13 restoration already ruled that `.cat-layout` and `.cat-main` are a flex
parent rather than a stone: the grey tree lost them in a port and got them back in 76 files. 0
`<img>` and 0 `background-image`; 23 raw `<path>` and 0 `<use>`; and the four sibling documents that
are not built carry a **`TBD` chip**, which is the chip's whole job and the reason it is a declared
difference. **0 non-neutral hex on the page**, and the instrument was proved against brass before the
zero was believed, because a greyness test that cannot see `#c7a24e` reports grey for everything.

**THE PAGE INSET HAD TO BE DECLARED, AND THAT IS THE PRICE OF THE PLATE BEING A DIFFERENCE.** The
paint takes its gutter from `.feed-inner`, so removing the plate removes the inset with it: measured
before, first text at **x=2 against the paint's x=31**, a 316px legal column running into both edges
at 320. The grey page declares its own 12px and reads 14. **This is the shape of every one of the six
differences**: dropping a paint-only wrapper is never only a deletion, because a wrapper that draws
also spaces, and the tree that drops it inherits the second job.

**AND THE TREE WAS WIRED, NOT ONLY GIVEN A FILE.** 196 dead `#` Terms anchors repointed across 105
files, a `Legal` section added to all 105 screen trees mirroring the group the painted sidebar
already had, and a row in `wireframes/_screens.md`. **The grey tree is 105 screens now**, and every
current statement of 104 moved with it in `CLAUDE.md`, `README.md` three times, `STRUCTURE.md`,
`wireframes/CLAUDE.md` and `_conventions.md`; the three that are dated measurements of 104 files were
left alone, because a reading is true as of its own date.

**Verified**: 3,752 renders over 268 documents in all three trees at seven widths in both engines, **0
horizontal scroll, 0 duplicate ids, 0 page errors, 0 HTTP errors**, positive control seen 2 of 2;
**0 broken of 34,950 links over 297 documents**; and the only painted screen with no grey twin is
`overview.html`, which is the index of the tree rather than a screen in it. **12 documents do not
carry exactly one `h1` and none of them is new**: 8 are kit pages, where a stand drawing a page hero
in two themes has several by construction, and 4 are the event-detail loading states in BOTH trees,
where nothing has loaded to be a heading yet and the two trees agree.

---

## 2026-08-15 - The kit had eight links that went nowhere and they were put there yesterday, and the two trees do not agree on the name of 32 screens

**THE LINK CHECK WAS RUN BECAUSE A FILE HAD BEEN RENAMED THIS WEEK AND NOBODY HAD RE-READ THE
LINKS.** 296 live documents, **34,396 internal references**, and 8 broken, all of them in
`ui-kit/dialog.html` and `ui-kit/organisms.html`, all of them mine, all of them one day old.

**THE HOW-IT-WORKS SHEET WAS PUT ON THE STAND ON 2026-08-14 WITH THE PRODUCT'S MARKUP COPIED
VERBATIM, WHICH IS THE RULE, AND ITS TWO HREFS ARE RELATIVE TO A FOLDER THE STAND IS NOT IN.**
`href="sign-in.html"` and `href="event-feed.html"` resolve from `ui-visual/` and resolve to nothing
from `ui-kit/`. Checked against the commit before: `git show 1cc154b~1` has **0** occurrences of
either in both files, so this was not an old defect the sweep finally reached, it was written the
day before it was found. **The kit's own convention was already there to be copied**: 59 anchors on
the stand read `../ui-visual/event-feed.html` and 43 read `../ui-visual/event-detail.html`. The
eight now do too, and the live tree reads **0 broken of 34,396**.

**AND IT NAMES THE COST OF THE RULE IT OBEYED.** "Markup goes to two places and only two" is what
put correct product markup on a page where one of its attributes is wrong, the same way the id rule
did: a document-unique id copied twice is a collision, and a document-relative href copied sideways
is a dead link. **An id and an href are both markup that means something about WHERE it stands**, so
both have to be re-pointed when the markup moves, and the kit had already learned the first half.

### The 32 screens with two names

**THE TWO TREES WERE ASKED FOR THEIR FILE LISTS AND THEY AGREE ON 72 SCREENS OF 104.** The paint
calls them `event-feed-politics.html`, the grey tree calls the same screen `politics.html`, and that
holds for all four categories in all eight states. **Filename is not one of the six declared
differences in `wireframes/_conventions.md`**, so by that file's own definition this is drift, and
every cross-tree comparison this repository runs needs a translation table for exactly those 32.

**IT IS FILED RATHER THAN FIXED BECAUSE BOTH NAMES HAVE AN ARGUMENT.** The conventions file says
logged-in pages keep the base names `event-feed*.html`, which the grey files do not, but that
sentence stands in a section about logged-out variants and is a glob rather than a ruling. Against
it, the IA gives the category its OWN route, `/c/{category}`, which makes it a screen rather than a
state of the feed and makes `politics.html` the truer name. That is a naming decision with an owner,
and the owner is not a stylesheet.

**THE COST WAS MEASURED AND THE FIRST MEASUREMENT WAS THE INSTRUMENT.** A `\b` word boundary matches
inside `event-feed-politics.html`, so the first sweep reported **9,866** references and 4,776 of them
were the paint's own filenames being counted as references to the grey ones. Anchored so that a match
cannot be preceded by a word character or a hyphen: **5,012**, of which 4,940 are inside
`wireframes/` and self-contained. The control is one painted screen, **48 naive against 0 anchored**.

### The one screen the grey tree never drew

**320 ANCHORS IN THE PAINTED TREE REACH `terms.html` AND THE GREY TREE HAS NO FILE FOR IT**, while
its copy of every one of those anchors reads `<a href="#">Terms</a>`. The painted screen is 882 lines
and 25 sections and has an SEO section of its own at `/legal/terms`. **The mirror is clean**: every
screen the grey tree links to exists in the paint, 0 exceptions, so this is one hole rather than a
pattern, and `overview.html` is the other name the diff returns and is correctly paint-only, being
the index of the tree rather than a screen in it.

**It is the one direction the layer rule forbids.** A destination is structure, the grey tree owns
structure, and here the paint decided a route the grey tree was never told about. **And the grey
footer does not mark it TBD either**: its five chips are Tagline, Language, Help Center, FAQ and
Contact, so Terms does not read as unbuilt, it reads as a link that goes nowhere. Backlog 157 carries
the two ways out and they are different sizes.

**Verified**: 296 live documents and 34,396 references, 8 broken before and 0 after, with the checker
proved against a target that does not exist; both file sets read from disk; the reference count taken
twice, once naive and once anchored, and the difference explained before either was used.

---

## 2026-08-15 - A census of who wrote the argument is not a census of who uses the unit, and the tidy answer would have deleted a cap

**THREE THINGS WERE LOOKED FOR AND THE ONE THAT WAS FOUND WAS NOT ON THE LIST.** The phone laid on
its side was swept for the first time, the width-query registry was re-counted, and a viewport-unit
census was taken because the first two needed one. The sweep found nothing, the count found two
stale sentences, and the census found a defect two days old inside a backlog row that was marked
closed.

### The drawer that never joined the discussion

**BACKLOG 124 CLOSED ON 2026-08-13 BY NAMING THE THREE FILES THAT HAD WRITTEN THE `svh` ARGUMENT AND
THE ONE FULL-PAGE SHELL THAT HAD NOT**, and it was right about all four. `betpanel.css` writes it
twice, `toc.css` three times, `catnav.css` twice, and `base.css` wrapped all 106 painted screens in
`min-height:100vh` while mentioning `svh` zero times. **That is a census of who had SPOKEN, plus the
shell**, and `course-chrome.css` is neither of those, so `.sidebar{height:100vh}` stood untouched.
Re-taken from the comment-stripped source: **seven viewport-height sites in `components/`, six of
them `svh` or a pair, and the seventh is the roadmap drawer.**

**AND IT IS THE HARDER OF THE TWO CASES, WHICH IS WHY IT IS WORTH THE LINE.** The row it was missed
by said so itself about the shell: `min-height` only ever ADDS room, so the cost there is a page that
can be scrolled by the height of the retracting bar and nothing worse. **`height` on a fixed SCROLL
CONTAINER puts the container's own bottom edge off screen**, and a fixed panel is not what scrolling
the document moves. Measured in both engines at 390x640 with the drawer open, its transition killed
and its height forced to 700 to stand in for a 60px browser bar, scrolled to its own maximum: **the
last link in the roadmap, `ui-kit` in the closing note, sits 38px below the visible edge with no
scroll left to reach it.** At 640 nothing is cut and at 700 one link is, in Chromium 151 and WebKit
26.5 alike, **which is the reading moving when the input moved** and the only reason to believe a
number the shipping instrument cannot produce: headless has no retracting bar, so `vh`, `lvh` and
`svh` are one number and this edit measures as zero on every sweep in the repository.

### The pair that cannot be written for a token

**THE OBVIOUS NEXT MOVE WAS TO MAKE THE FIVE SITES AGREE, AND MEASURING IT FIRST IS WHAT STOPPED
IT.** `tokens.css` deleted the `vh` half beside `--sheet-cap` on 2026-08-14 on the measured ground
that `CSS.supports` for `svh` is true in both engines here; `base.css` still carries the paragraph
arguing the opposite, that "a browser that has not learned `svh` takes the first". Both are argued
and they disagree, and the tree has been one day out of step with its own newer decision in four
places since.

**THE PAIR WORKS BECAUSE BOTH HALVES ARE DECLARATIONS, AND A CUSTOM PROPERTY IS NOT PARSED THAT
WAY.** A declaration whose unit the engine cannot read is thrown out at parse time and the one above
it survives. A custom property accepts any token sequence, so the unit is never rejected. Measured in
both engines: `max-height:92vh` computes to **588.8px** at 640; `--cap:92zzh` with
`max-height:var(--cap)` computes to **`none`**; and `max-height:92vh` FOLLOWED by
`max-height:var(--cap)` also computes to **`none`**, because `var()` is valid at parse time, wins the
cascade, and fails only at computed-value time, where the fall is to the property's initial value and
never to the declaration above it.

**So "add the pair everywhere" does not add a fallback, it takes the cap off three sheets**,
`dialog.css`, `betpanel.css` and the filters sheet, from 92 per cent of the small viewport to no
maximum at all. **The inconsistency is load-bearing**, and it is written beside the token rather than
removed, because the paragraph is the only thing standing between the next reader and the tidy
version. What is left is a question about audience and not about CSS, `svh` having landed in Safari
15.4 in March 2022 and Chrome 108 in November 2022, and it is backlog 155 rather than a call made in
a stylesheet. The drawer takes the PAIR for now, so all five sites still say one thing and the
decision moves them together.

### The phone on its side, and two findings that were the instrument

**THE SWEEP FOUND NOTHING, AND THAT IS THE RESULT.** 106 documents at 390x844 plus the four common
landscapes, 667x375, 740x360, 844x390 and 932x430, in both engines: **1,060 renders, 0 sideways
scroll, 0 content outside a clip that cannot be reached.** Docked chrome takes **13.6 to 16.4 per
cent of viewport height** at every landscape width, worst case a 59px header, so the rungs reasoned
from a wide window cost the short window nothing. Backlog 125(c) had closed orientation as a width
fact and this is the shape half of the same question, taken and agreeing.

**BUT IT REPORTED THREE FINDINGS FIRST AND TWO OF THEM WERE THE PROBE.** `.plate-head` was reported
clipping 52px across and 69 down on 15 documents at every width, and it is `.plate-head::after`, a
210px brass glow at `top:-72px;right:-52px` that the `overflow:clip` is FOR: **`scrollWidth` counts a
pseudo-element, so decoration reads as a defect.** Then the outcome dialog was reported putting
buttons up to 434px past its own cut on 13 screens, in both engines, with identical numbers, which is
exactly what a real defect looks like. Every one of them was inside `.sheet-body`. **Scroll every
scroller to its maximum and re-read: 86 hits become 0.** That is this repository's own sentence about
culprits already standing inside a scrolling container, met again by a different road, and the road
does not make it a new lesson.

**AND THE CONTROL FAILED FIRST, FOR A REASON WORTH KEEPING.** The injected box was
`overflow:hidden` and was correctly not seen, because **a `hidden` box is still scrollable from
script and a `clip` box is not**, which is the whole distinction the probe is built on. A control has
to be made of the thing being looked for, or its silence means nothing. With `clip` it reads 2 of 2
in both engines.

### The two stale counts

`ui-kit/docs/inventory.md` and `ui-kit/docs/responsive.md` both stated in the present tense that
`components/` holds **33** width queries, inside the classification of 52 selectors that backlog 129
took on 2026-08-13. Re-counted from the comment-stripped source: **34**, 16 at the desk in 13 files,
6 at the detail in 6, 6 at the rail in 5, 2 at the 1140 harness and 4 one-offs. The finding is
date-stamped rather than renumbered, **because rewriting 33 to 34 would move a measurement onto a
tree it was never taken on**, and the one query added since is a control's own narrow-side block
inside a group the classification already counts.

**Verified**: 1,060 renders over 106 documents at 5 viewports in Chromium 151 and WebKit 26.5, 0
sideways scroll, 0 unreachable content, positive control 2 of 2; 53 stylesheets parsing with 0 page
errors after both edits, `--sheet-cap` resolving to `92svh` and the outcome dialog capping at 588.8px
of 640 exactly as before; the drawer measured at two heights in both engines with the cut link named.

---

## 2026-08-15 - The tree had never drawn a person who backed NO, and a face with no placement is not a component with no face

**TWO ROWS WERE LEFT OPEN BY THE CONSISTENCY REPORT AND THEY HAD OPPOSITE ANSWERS.** One was a real
gap in the product that a stylesheet had been carrying the evidence of for months. The other should
never have been opened, because the product owner had answered it two days earlier.

### The chosen NO

**`.sel` AND `.no` HAD NEVER ONCE STOOD ON THE SAME ELEMENT.** Read in the DOM across all three
trees: 127 chosen sides in the paint, 24 in the grey and 39 on the stand, and every one of them YES.
Five rules in `yesno.css` drew the other half of a symmetric control and not one of them could fire,
so half of this control had never been rendered and therefore had never been measured, **which is
this repository's whole method switched off for one component.**

**IT WAS THE SCREENS, AND THE GREY TREE IS WHAT PROVES IT.** A colour layer that had lost a state
would show that state in grey and not in colour. Both trees showed only YES, so this was not paint
dropping something, it was a tree depicting one path. **And the route already existed**: backlog 143
gave every card `?side=yes` and `?side=no`, 212 anchors each, so the product had been promising an
arrival that no screen drew.

**ONE SCREEN, IN BOTH TREES, AND THE CHOICE OF SCREEN IS MEASURED RATHER THAN TASTE.**
`event-detail-bet-processing.html`, because **its panel is mid-submit and carries no payout figure**,
so nothing has to be kept in arithmetic step with the pick except the sticky dock, which goes from
`$5 to win $13.20` to **`$5 to win $8.06`**: five dollars at 62 per cent pays that. The YES pick
inside the how-it-works sheet on the same screen **stays YES**, because it is a picture in an
explainer that ships identically on 105 screens and not this person's bet.

**AND DRAWING IT FOR THE FIRST TIME IS WHAT LET IT BE MEASURED.** The chosen NO is `--text-on-no` on
`--outcome-no` at **4.64:1**, against the chosen YES at **6.42:1**. Both clear AA for body text, the
NO side is the tighter of the two, and that is a number now instead of an assumption. **A rule that
cannot be rendered cannot be checked, and it will be wrong the day it first draws** rather than the
day it was written.

**THE FIFTH SELECTOR IS DELETED AND THE DELETION IS A STATEMENT ABOUT THE COMPONENT.**
`.yesno > a.sel:active` still matches nothing after the placement, and it should: **a chosen side is
a `<button>` and never an `<a>`**, 16 chosen buttons and 0 chosen anchors over all three trees. The
anchor half is the SPECTATOR's pair on a card, which states a market and records no choice; the
button half is the chooser. That is `yesno.css`'s own sentence about a side being a POSITION IN THE
PAIR, read one level further out.

**The stand carries it too**, in both themes: a NO-taken chooser and a NO-taken row in the outcome
list on `ui-kit/yesno.html`, because a face the product places once is a face a reader has to be able
to compare against its twin.

### `.icon-btn-lift`

**THIS ROW SHOULD NOT HAVE BEEN OPENED.** The face had 525 placements until 2026-08-13, when backlog
144 took the footer's five social marks out of every screen: five anchors a screen at `href="#"` for
accounts that do not exist, standing directly under the trust strip. **A social account can never
become an internal route, so it was not a link waiting for a screen**, which is what separated it
from the two kinds of placeholder the footer's rules already covered.

**AND THE KEEP-OR-DELETE QUESTION WAS ANSWERED IN THAT SAME COMMIT, WITH THE RIGHT DISTINCTION.**
`account.css` was deleted for having no FACE left, its two rules being another component's stone.
This is a face with no PLACEMENTS, and its placements return on a date somebody chooses. **A
component with no face is a name; a face with no placement is a face.** The audit read the second as
the first because both compute to zero, and zero is where two different things look alike.

**What was actually wrong was one number.** `ui-kit/iconbtn.html` still published 525 in its touch
table. It reads 0 now with the reason beside it, so the one row in that table worn by nothing says so
rather than reading as a face nobody measured.

**Verified**: 267 documents at 16 widths in Chromium 151 and WebKit 26.5, 8,544 renders, 0 horizontal
scroll, 0 duplicate ids, 0 page errors, positive control seen at 2,680. The chosen NO measured in the
panel and in the dock at 390 and 1280 in both themes: `--outcome-no` solid with `--text-on-no`, and
the explainer's picture still YES.

---

## 2026-08-15 - The dead rules were the evidence, and one of them had been the sheet's scroll container

**THE AUDIT FILED THE HOW-IT-WORKS SHEET AS A PRODUCT QUESTION AND IT WAS NOT ONE.** `.hiw-body`,
`.hiw-full`, `.hiw-arrow` and `.hiw-hero` stood at 0 placements in the product and 43 on the stand,
which reads as a stand that invented markup. `git log -S` answered it in one line: **`d214184`,
2026-08-14**, the day the sheet was rebuilt from two explainer sections plus a FAQ plus a way back to
its own page into three steps with a picture each, where the third one is a way IN. A dated, argued
decision, and the markup went out of all three trees with it. **What stayed was its stylesheet.**

**AND ONE OF THOSE EIGHT ORPHANED RULES HAD BEEN DOING THE SHEET'S MOST IMPORTANT JOB.** `.hiw-body`
was the SCROLL CONTAINER, and the new sheet had none. Measured with the sheet open, the entrance
animation finished and reduced motion asserted, in both engines:

- **320 x 480: the sheet caps at 441 against 562 of content, 121px outside the clip, `scrollTop`
  reads back 0, and the whole step navigation, Next and the dots, is below the cut and unreachable.**
- **360 x 568: 40px, same navigation, same 0.**
- 360 x 640 and above: nothing.

**A FRAME THAT CLIPS CANNOT ALSO BE THE SCROLL CONTAINER**, which is the rule `dialog.css` already
writes for `.sheet-body` twenty lines above the one that broke, and this sheet had lost its half of
the pair for a day. The rule names `.hiw-steps` now, which is what this sheet's body is called.
After it: 121 and 40 pixels of scroll where there were none, the navigation reachable at every size
in Chromium 151 and WebKit 26.5, and **0 at 640 and above, where nothing was wrong.**

**READ THE ENTRANCE ANIMATION FIRST OR THE NUMBER IS ABOUT NOTHING.** The same probe run without
`getAnimations().forEach(a => a.finish())` put the dialog's top at **428 in a 480px viewport**, which
is the sheet caught mid-slide and reads exactly like a modal rendering below the fold. That is a
second defect report about a page that does not have one, and this folder's rule caught it: finish
the animations before reading a box.

**WHAT WENT.** Eight rules in `dialog.css` - the body wrapper's padding and column, the brass link
out to the full guide, its arrow, its hover, its press and the 3px nudge - and two in `hiw.css`,
`.hiw-hero` and its heading size. Four class names off two `Classes:` lines. **`.hiw-hero` had been
superseded TWICE before anybody read it again**: backlog 105 split the page hero out as `.hiw-page`
on 2026-08-11, taking the padding, the edge, the corner and the heading size with it, and the
2026-08-14 rebuild took the sheet's copy. Checked rather than assumed: `how-it-works.html` renders
its h1 at 30px on a phone and 38px on a desk, from `--display-hiw` through `.hiw-page`.

**`.hiw-hero-inner` STAYS WITH ITS ONE PLACEMENT AND THAT IS NOT AN OVERSIGHT.** Its one job is to
sit above the two absolute layers `platehead.css` paints behind it, the wave in `::before` and the
glow in `::after`, neither of which carries a z-index. **A wrapper that exists only to hold a
stacking position is still doing the work**; the class it used to be named after is not.

**THE STAND WAS THREE PAGES, NOT ONE.** `ui-kit/hiw.html` had been updated on the day of the rebuild;
`dialog.html` and `organisms.html` still drew the old sheet and carry the shipped markup now, with
ids and radio names suffixed per cell, because a radio group is keyed by `name` and two cells sharing
one are one group. `vitrine.html` and `platehead.html` showed `.plate-head.hiw-hero` as one of the
face's hosts and show the page hero there instead.

**`platehead.css` WAS WRITTEN BECAUSE FOUR COMPONENTS WORE ONE FACE AND IT IS THREE TODAY, AND THAT
COSTS A COUNT AND NOT A RULE.** 228 plain sheet heads, 1 page hero, 10 outcome heads. The list in
that file is kept at four with the one struck rather than renumbered, because the fourth-host
argument is what decided the SHAPE of the file, an anatomy plus a default skin, and it was true when
it was made. **Losing a wearer is the test that argument was built to pass.**

**Verified**: 106 painted screens with the sheet shut, **78,245 elements**, 26 computed properties
each, base tree against live, **0 differing rows**, control 0 first. 267 documents at 16 widths in
both engines: 0 horizontal scroll, 0 duplicate ids, 0 page errors, positive control seen at 2,680.
The sheet open at four viewports in both engines, scroll and reachability as above.

---

## 2026-08-15 - Seventeen rules that drew nothing, and the print sheet was partly aimed at nothing

**THE SYSTEM WAS READ AGAINST THE PRODUCT FOR THE FIRST TIME**, rather than the product being read
against itself. 1,282 style rules taken out of the browser's own CSSOM, 1,144 distinct selector
parts, asked of 163 documents in two passes: once with the pseudo-classes a static page cannot
satisfy stripped, and once with every state pseudo and attribute selector stripped as well, so that a
rule waiting on a checked radio is not confused with a rule waiting on an element that does not
exist. The report is `ui-kit/docs/consistency.md`.

**THE CONTRACT HELD EVERYWHERE IT WAS CHECKED.** 53 imports against 53 files with no orphan and no
duplicate. 47 components each with a stylesheet, a kit page, an inventory row and a route. 0 media
queries in the 106 painted screens. 387 `style=` attributes carrying 435 declarations, **every one of
them the photograph, the odds-bar datum or the chart's `--v`, and 0 of them styling**. 24
`!important` and none in a component. 24 raw colours outside `tokens.css` and **0 of them a theme
colour**. Six raw ladder-step px on a sizing property and, read in context, **0 of them drift**: a
`right:18px` is not an icon size.

**WHAT WAS DELETED, AND IT CHANGED NOTHING BY DESIGN.** `pre`, `kbd`, `samp` and `select` came off
two reset lines in `base.css` at 0 elements each; `.tbd,.placeholder-line` and `.groove-sep` went
whole. `strong` came off `.protect` and `b` off `.reconcile-box`, **each block naming both tags and
shipping only one**. Both `.chart-svg text` rules went, and with them the last raw px `font-size` in
the system, which was the exception a census had wanted to sweep up and turned out to be an exception
about a node that is not there. `.theme-switch-inline` and its ring went on the `account.css`
precedent. `.bottom-nav .badge-dot` went, and **a count of the class would have said it was alive**:
`.badge-dot` has 86 placements and every one of them stands in `.bell-wrap`, so the pair has never
met and the question a descendant selector asks is about the PAIR.

**THE COMMENT THAT KEPT `.tbd` ALIVE HAD OUTLIVED ITS OWN SUBJECT.** It said the frozen kit still
carries the wireframe's chips and must keep rendering the way it did. `docs/kit-archive/` holds **0
HTML files**: what was kept of the deleted kit is prose. And a grep says the class is alive at 364
occurrences while the DOM of all 106 screens says 0, because every one of them is in
`ui-visual/old/`, which links no stylesheet. **A rule kept alive by a sentence about a folder is a
rule nobody re-reads when the folder changes.**

**PRINT WAS THE REAL FINDING AND IT WAS NOT A DELETION.** Four of `print.css`'s rules named
`.action-bar`, `.notice`, `.seo-plate` and `.bets-table`, which are COMPONENT names, and **0 elements
in any of the three trees wear any of them.** `.action-bar` was pure redundancy, with `.cta-bar` in
the same list, and it was deleted. The other three were repaired, because the intent is legible and
correct: `.notice` and `.seo-plate` became the seven classes the markup actually wears, so **250
blocks that were printing with no grey edge now have one and no longer split across a fold**.

**`.bets-table` IS THE ONE WORTH READING TWICE.** Renaming it to `.ptable` was tried first and
MEASURED, and `.ptable` computes `overflow:visible` on paper with the rule and without it, **because
that component declares no scroller at all**. A rule that applies and changes nothing is the same
defect one step further along. What scrolls in that block is the two tab bars, `.ed-tabbar` and
`.ptab-bar`, and they were still `auto` on paper. **The component name was wrong and so was the
component**, which is what a name written from a folder listing buys.

**THREE OF THE SEVEN FINDINGS WERE THE INSTRUMENT, AND TWO OF THEM ARE STRUCK RATHER THAN FIXED.**
The pass first reported four tokens read by nobody, `--bone-200`, `--brass-220`, `--ink-700` and
`--space-56`, and all four are read by `ui-kit/_page.css`, which draws the palette and the spacing
ladder: **a value's reader can be the thing whose job is to show it**, and a sweep for dead values
that does not read the vitrine deletes the swatches first. It also reported `hiw.css` naming six
colour roles it never reads, and the six stand inside a parenthetical in that line saying they LEFT
for `platehead.css` on 2026-08-11. **379 of 379 tokens are read and 52 of 53 contract lines are
exact.** The one that was not is `bets-table.css` naming `.sel`, which it writes no rule for and
which no element inside a `.ptable`, an `.act-list` or a `.hold-cols` wears.

**And the reachability instrument lied twice before it was believed.** A stylesheet read from
`file://` has no `cssRules`, because every document from disk has its own opaque origin, so the first
run reported **0 style rules and then scanned 163 documents against nothing and printed 0 dead
selectors**, which reads exactly like a pass. That is the fourth time the disk origin has cost this
repository. Then the pseudo-stripper listed `focus` before `focus-visible` in an alternation, so
`.chip-nav:focus-visible` became `.chip-nav-visible` and every focus rule in the system was filed as
dead: **a selector that is not a selector any more still parses**, which is why the count came back
plausible instead of zero.

**WHAT WAS NOT TOUCHED, AND EACH IS A PRODUCT QUESTION RATHER THAN A CLEANUP.** `.sel` and `.no`
never appear on the same element in any tree, so the outcome pair has a chosen-YES face everywhere
and its chosen-NO twin has never been rendered: that may be a defect in the SCREENS. `.hiw-body`,
`.hiw-full`, `.hiw-arrow` and `.hiw-hero` have 0 placements in the product and 43 on the stand, so
eight rules in two files draw a how-it-works sheet that was designed and never shipped.
`.icon-btn-lift` is a face with 0 placements and 9 specimens, which is `account.css` again.
`.hold-name` prints truncated with an ellipsis and no way to see the rest.

**Verified**: base tree against live tree over 163 documents and **114,754 elements**, 26 computed
properties each, **0 differing rows**, with the control at 0 first and the absolute asset URL
normalised because two servers cannot agree on a port. On paper: `.protect` from a brass edge to the
grey hairline and gaining `break-inside:avoid`, `.feed-seo` from no border at all to the hairline,
the two tab bars from `auto` to `visible`, and the screen unchanged at `auto`.

---

## 2026-08-15 - The switcher that was meant was the other one, and setting its height alone would have changed nothing

**THE PREVIOUS ENTRY ANSWERED THE WRONG CONTROL.** "Make the switching buttons smaller on a phone,
say 44" was read as the chart's range rail and it meant the CATEGORY STRIP, the row of Trending,
Politics and Crypto that is the first thing under the header on every feed screen. The reading that
settled it was a screenshot: **the reply had been true, measured and about something else.** Both
changes stand, because the range rail's frame was a real ten pixels; only the second one is the
answer to what was asked.

**`.chip-nav` WAS `--control-48`, THE PRODUCT'S MOST COMMON CONTROL, AND ON A PHONE IT WAS 48 OF THE
70 THE WHOLE BAND COST.** 44 is the touch floor's own number, declared once in `base.css` for the
family, so below the desk rung the chip stands exactly on it.

**AND `--control-h:var(--control-44)` ON ITS OWN WOULD HAVE DRAWN NOTHING.** This chip's content box
is **47** before any floor is consulted: 21 of line box at 14 on 1.5, 24 of vertical padding, 2 of
border. `min-height:44px` against a 47px content box is present, correct and consulted by nothing,
which is **exactly the inert declaration `components/loadmore.css` had already found and named** in
the merge of 2026-08-07 - it listed `min-height:44px` first among the four differences that turned
out to be nothing. **The padding is what decides the box.** At `--space-8` the content is 39 and the
floor becomes the thing that sets the height instead of a leftover.

**THE SIDES CAME DOWN WITH THE HEIGHT BECAUSE THE STRIP IS A SCROLLER AND THE COMPLAINT WAS
HORIZONTAL.** 20 a side and 12 between mark and word put two chips and a sliver into the 298px this
row gets at 360. Measured after, both engines: **131.1 to 111.1 and 122.2 to 102.2**, band **70 to
66**, and the third category is a word instead of an edge. At 640 and above nothing moved: 48 and 78,
before and after, at 640, 641 and 1280.

**ALL 294 PLACEMENTS MOVED AND THAT IS THE POINT RATHER THAN THE COST.** A census over the 106
painted screens puts 285 in the category strip and **9 on `Load more events`**, and
`components/loadmore.css` settled on 2026-08-07 that those nine ARE this chip: one control keeping
what the other 285 gave up is precisely the exception that file deleted, and re-opening it on a phone
would have been the same mistake with a rung in front of it. Load more's width comes from a
three-word label, so 16 fewer pixels of padding is the whole of what it feels, and it stands on the
same floor as everything else a thumb hits. **The drop is 20 in the strip and 16 on load more, and
the difference is arithmetic rather than inconsistency**: the padding loses 16 everywhere and the
strip's chips lose 4 more because they carry a mark and a gap.

**WHAT WAS NOT DONE: THE PLATE.** 22 of the 66 are chrome around one row - 16 of plate padding, 4 of
list padding, 2 of hairline - and `base.css` already trims that padding from 12 to 8 below the rung.
Taking more is a decision about the plate that wraps the strip, not about the chip, and it is not
smuggled in under a request about the buttons.

**THE COUNTS THIS MOVED, RE-TAKEN FROM THE COMMENT-STRIPPED SOURCE RATHER THAN INCREMENTED.** The
system holds **34 width queries**, 16 at the desk in 13 files, 6 at the detail in 6, 6 at the rail in
5, 2 at the 1140 harness and 4 one-offs in 3. It had been published as 32 in `README.md` and
`components/CLAUDE.md` and as **33 in three places in `ui-kit/docs/responsive.md`**, whose registry
table had gone stale on 2026-08-14 when `catnav.css` gave up its desk block: the table's DETAIL row
said 4 and the source said 3. **That table's own paragraph had bragged about being "right for the
third time by accident"**, and the fourth time it was not.

**AND THE RECOUNT FOUND TWO HOLES IN A CONVENTION, WHICH IS WHY IT IS WORTH DOING BY GREP.** The
"What it does with width" section is supposed to stand on every kit page whose component owns a width
query. It was published as 21 pages and reads **25** now: `options` and `yesno` had each owned a desk
query since 2026-08-12 **and neither page said so**, because the two queries were added, the total
was updated, and the convention hanging off the total was not. `tabs` took one the day `.ed-range`
grew its first query. The other two are deliberate: `card` keeps its section to record the query that
LEFT, and `responsive` is a foundation page whose subject is width. **A convention that names a count
has to be re-counted, or the count quietly becomes the convention.**

**Verified**: 267 documents (106 painted, 57 kit, 104 grey) at 16 widths in Chromium 151 and WebKit
26.5, **8,544 renders** - 0 horizontal scroll read by writing `scrollLeft` and reading it back, 0
duplicate ids, 0 page errors, with a positive control first: a box wider than the window is seen at
2,680 in both engines and the clean page reads 0.

**AND THE FIRST RUN OF THAT SWEEP SAID 382 DOCUMENTS SCROLLED SIDEWAYS, ON SCREENS NOTHING HAD
TOUCHED.** It read the page in the same turn as `setViewportSize`, so it measured the 1280 layout
against a 320 window: **a resize is not a layout, and it needs a frame.** Two `requestAnimationFrame`s
later the identical run reads 0. **The tell was the arithmetic rather than the size of the number**:
138 at 320 and 98 at 360 is one constant of 458, and a defect that is the same box at every width is
usually not a defect. The elements it named were the header's utility group at 458 and an `svg` at
520, which are the wide layout still standing. Written into the root `CLAUDE.md` beside the rule it
is an instance of.

---

## 2026-08-15 - The chart's range switcher was 54 tall and the ten pixels were never the buttons

**ASKED: MAKE THE SWITCHER SMALLER ON A PHONE, DOWN TO 44. MEASURED FIRST: THE BUTTONS ARE ALREADY
EXACTLY 44 x 44.** On a coarse pointer at 320, 360, 390, 640 and 1280, every one of the four chips is
44 x 44, which is this project's own touch floor and an invariant `base.css` declares once for the
whole control family.

**THE ROW WAS 54 AND THE TEN PIXELS BELONGED TO THE GROUP'S FRAME**: 4px of padding and a hairline on
each side, `44 + 8 + 2`. The width is the same arithmetic, `4 x 44 + 3 x 4 + 8 + 2 = 198`. So below
the desk rung the well, the edge and the corner come off and the row is **44**, which is the number
that was asked for and **the only ten pixels there were to give**.

**THE FOUR CHIPS STILL READ AS ONE CONTROL**, because the chosen one carries a brass ground and the
other three carry none: **a segmented control is told apart by its selection, and the frame around it
is what a desk has room for.** Above 640 nothing moved, measured: 198 x 54 at 640 and 1280, before and
after.

**ANYTHING BELOW 44 WOULD BE THE FLOOR'S DECISION AND NOT THIS COMPONENT'S**, and it is not taken
here. `base.css` raises every member of the family under `pointer:coarse`, once, and this folder's
rule is that a floor is the family's and is declared in one place. A component that shrank under it
would be the `.btn-md` defect again: the same control 48 under a mouse and 47 under a finger, because
a floor out-specified the component and the content then held the box. **If the switcher should be
smaller than the floor, the floor is the thing to argue with, and the argument is `backlog.md` 40.**

**Verified**: 267 documents in both engines, 0 horizontal scroll, 0 duplicate ids, 0 page errors.

---

## 2026-08-14, the chart - The detail drew a bare polyline while the feed drew a filled chart, in the same product

**THE SCREEN A PERSON COMES TO IN ORDER TO READ THE PRICE HAD THE WORSE CHART.** `hero.css` has drawn
a filled chart since the day it was written: an area under the line with a gradient from the outcome
colour to nothing, four quiet grid lines, a legend. The event **detail** drew a 1.6px polyline in an
empty well with three grid lines at 25, 50 and 75, a dashed vertical sitting on the well's own border,
and nothing else. **One product, two charts, and the better one was on the screen that is only passing
through.**

**REFERENCES WERE READ FIRST AND THE LESSON WAS SUBTRACTION.** Wealthsimple's dark price chart has no
frame, no grid, and **one** dotted horizontal, the previous close, labelled at its right end. The
takeaway is not a style, it is a rule: **label the line you want read, and draw no line you do not.**

**THE AREA IS THE DATUM HERE AND NOT ORNAMENT.** Under a stock price a fill is decoration, because
the zero it falls to is arbitrary. Under a **probability** the line runs 0 to 100 and the area is how
much of the way to certain the market has come. It is the hero's own gradient, so the two charts in
this product are now one idea drawn twice rather than two ideas.

**ONE REFERENCE LINE INSTEAD OF THREE.** 25 and 75 are arithmetic; **50 is the only number on this
axis that means anything**, because above it the market says yes. Three lines of equal weight said all
three were equal. **And the label that line needs is the one the y-axis already carries**: a floating
`Even` was built, screenshotted and deleted in the same pass, because it was the same fact written
twice and it was written ON TOP OF THE LINE at the one place a reader is looking. The y-axis keeps all
five numbers, because that is the SCALE and a scale is not a grid.

**THE DOT IS A DOM ELEMENT AND NOT AN SVG CIRCLE, AND THE REASON IS THE viewBox.** The chart is
`viewBox="0 0 300 100"` with `preserveAspectRatio="none"` drawn into about 900 x 160, so the
horizontal and vertical scales differ by about six and a `<circle>` renders as an ellipse six times
wider than it is tall. **The strokes survive that because they carry `vector-effect:non-scaling-stroke`,
which is a property about STROKES and does nothing for a shape.** So the dot stands in `.ed-plot`,
which was already positioned, and its height is a percentage, the same datum the odds bar writes as a
width and one of the three things allowed on the element.

**AND THE AREA'S `fill` IS A PRESENTATION ATTRIBUTE IN THE MARKUP, WHICH IS THE ONE PLACE THIS
COMPONENT DISAGREES WITH `hero.css` ON PURPOSE.** That file writes `.hf-area{fill:url(#hfyes)}` and is
safe only because the hero stands once in a document. **This chart stands twice on
`ui-kit/chart.html`.** The kit suffixes every id a cell redefines together with every `url(#id)`
pointing at it, and a `url()` in a stylesheet is not in the cell and cannot be suffixed, so a CSS rule
would have left the second cell filling from the first cell's gradient. **That is exactly the defect
the tab panels paid for**, ids suffixed and rules not, and a specimen that draws its bar and none of
its panels. Two kit pages had their second gradient suffixed in the same pass.

**The multi-outcome chart takes the reference line and nothing else**: five lines cannot share one
area and have five endpoints. Measured after: 5 lines, 1 reference, 0 areas, 0 dots, 0 old grid.

**AND THE DOT WAS OFF THE LINE, WHICH IS THE PART OF THIS WORTH KEEPING.** It looked right and it was
not: measured against the polyline's last point transformed into page coordinates with
`getScreenCTM`, the centre stood **3.76px above the line and 1.00px to the right of it**, identically
in both engines at both widths. **Two mistakes of one species: an edge-anchored box pretending to be a
point.**
The vertical one was a margin that could not apply. The rule read
`margin:calc(size / -2) ... 0 0`, a negative margin-TOP, and **a negative margin-top does nothing to a
box positioned by `bottom`**: the box's bottom edge sat on the line and its centre was half a dot
above it. `translate(50%,50%)` anchors the centre whatever the size becomes, and writes the halving
nowhere.
The horizontal one was the border. `right:0` is the PLOT's border box and the line's last point is at
the SVG's CONTENT right edge, one hairline inside it.
**And the datum stopped being a length.** It was `style="bottom:38%"`, which is 38 per cent of the
border box while the line is drawn in the content box, an error of `hairline * (1 - 2v/100)`. The
element carries `--v:38`, the probability itself, and the rule does the geometry. **A datum should be
the number the product knows, not a length somebody has already done arithmetic on.**
Re-measured, all four ranges, both engines: **0.00 on x and 0.02 on y**, and the y remainder is one
`calc`'s rounding. It is written here as it was read rather than as 0.

**Verified**: 267 documents in both engines, 0 horizontal scroll, 0 duplicate ids, 0 page errors, and
the area path, the fill reference, the dot and the dash pattern read identically in Chromium 151 and
WebKit 26.5.

---

## 2026-08-14, one label - A bracket that repeats the sentence above it is the same sentence at a smaller size

**ONE BUTTON WRAPPED ONTO TWO LINES ON 105 SCREENS AND THE BRACKET WAS BOTH HALVES OF WHY.**
`How it works (what happens to my money)` stands in the deposit dialog, and two lines above it the
`.protect` sentence already says **"Your USDC is held 1:1 - we do not lend or invest your funds"**,
which IS what happens to your money, in one plain sentence, which is voice principle 2. **The bracket
promised an answer the screen had already given.**

**AND IT MEANT ONE DESTINATION HAD TWO NAMES, 105 PLACEMENTS EACH.** The header's control has said
plain `How it works` since the day it was written; the deposit dialog's said the long form. That is
the `same-action / label varies` flag `microcopy.md` already carries for the go-to-events button, met
on a second control, and neither label was wrong on its own.

**THE MEASUREMENT THAT FOUND IT IS THE POINT.** Reading the tree for bracketed strings turns up 12
and most are prose. Reading it for **buttons whose LABEL wraps** turns up one, and the difference
between the two sweeps is that the second counts the rects of the button's TEXT NODES rather than of
the button: an icon beside a label sits at its own top, so a whole-element read reports every provider
button and every amount chip as two rows. **A count of rectangles is not a count of lines.**

After, over all 106 screens in both engines at 320, 360 and 390: **not one button in the product wraps
its label at 360 or 390.** Four do at 320 and they are `backlog.md` 154, because two of them are a
narrow box rather than a long label and that is a layout decision, not a copy one.

---

## 2026-08-14, the 25th case - The window and the event head move in opposite directions, so the head stopped asking the window

**THE EVENT HEAD ON A PHONE WAS THE WORST BLOCK IN THE PRODUCT AND THE MEASUREMENT SAYS WHY.** It is
a row: a 72px thumbnail, a 12px gap, and 100px of padding reserved on the right for three absolutely
positioned actions. **That is 184px of overhead in a column 291 wide at 320**, leaving the title
127px to wrap in. Title lines by viewport before: **6 at 320, 5 at 360, 4 at 390 and 430**, the
category broken across two lines at every one of them, `YES 38% NO 62%` wrapping so `62%` sat alone
under `NO`, and the odds bar drawing 127px inside a 331px head.

**AND IT WAS WORSE AT 760 THAN AT 430, WHICH IS THE WHOLE ARGUMENT.** `.ed-head` against the
viewport: 611 at 640, 645 at 700, **341 at 760**, 381 at 800, 481 at 900, 681 at 1100, **501 at
1140**. The two drops are the bet panel arriving and the review sidebar docking. **At each of them
the window gets WIDER and the head gets NARROWER**, and the title goes from 2 lines to 6 across one
rung.

**SO THIS IS THE 25th CASE, AND `backlog.md` 129 IS THE REASON IT COUNTS.** That row refused
container queries on a measurement rather than a preference: of the 25 selectors standing on both
sides of their own rung, **24 would have resolved identically at every placement**, so a window query
was doing the same work and a container query would have been ceremony. This is the one that would
not. **A window query cannot say "the head is narrow" here without naming the bet panel's rung and
the review chrome's dock**, which are facts about other components, and every one of those numbers
would go stale the day either moved.

`patterns/detail-shell.css` declares `container-type:inline-size` and `container-name:ed` on
`.ed-main`, and `event-detail.css` asks it. **The declaration is the pattern's because place is not a
property of the brick**: the pattern is what puts the content column beside the panel, so it is what
knows the column is a context. `inline-size` and not `size`, because nothing here asks about height.
**Measured in both engines before a line was written**: `CSS.supports` is true and a test rule
actually changed a computed colour, which is the reading that separates a feature that parses from
one that applies.

**THE THRESHOLD IS THE CONTENT'S AND NOT A DEVICE'S.** Below 460px of column the row cannot hold a
72px picture, 100px of gutter and a readable measure at once. After, title lines: **3 at 320, 2 at
360, 390, 430 and 760**, category on one line everywhere, the odds bar 251 at 320 and 291 at 360, and
the head 35px shorter at 360. **Unchanged at 560, 640 and every width from 900 up**, which is the
control: the rule fires only where the column is narrow. The 3 lines that remain at 1140 are
`text-wrap:balance` choosing evenness at a 279px measure, not a squeeze, and the same measure gives 2
lines at 900.

`order` rather than a markup change, and it is safe here for a reason worth stating: **the only
focusable elements in this head are the three actions**, so visual order and focus order cannot
disagree about anything a keyboard can reach.

**A container threshold is not a token**, because it is local to one placement and no other component
can be asked to honour it. It is registered in `ui-kit/docs/responsive.md` beside the transcript that
said `@container` was 0 in the product, which is now 1 and 1 and says so.

**Verified**: 267 documents in both engines at 16 widths, 0 horizontal scroll, 0 duplicate ids, 0
page errors. The 30 `.ed-head-txt` placements were named across all three trees, including the four
loading skeletons and the three kit pages that write the head in a different shape.

---

## 2026-08-14, the last of the three - Two strips said the same five words, and the repair is the label the row never had

**THE FEED CARRIES A CATEGORY STRIP AT THE TOP AND A CATEGORY SUB-FILTER UNDER ITS HEADING, AND THEY
SAID THE SAME FIVE WORDS.** `Trending / Politics / Crypto / Culture / General` against
`All / Politics / Crypto / Culture / General`. **The strip ROUTES to a category page; the sub-filter
NARROWS the list already on screen.** Both are true, both are useful, and neither is visible from the
words.

**THE FACES ALREADY DIFFERED AND IT WAS NEVER ENOUGH.** A strip chip carries a mark and stands on a
plate; a sub-filter chip is bare. The two rows are a hundred pixels apart, so a person compares them
by READING and not by looking, and reading gives the same answer twice.

**THE REPAIR IS `Show:` IN FRONT OF THE ROW, AND THE ARGUMENT FOR IT IS THAT IT IS NOT A NEW IDEA.**
This feed has three filters. Two of them have carried a label since the day they were written,
`Sort:` and `How often:`. **The third had none at all**, and that asymmetry is the whole defect: a
labelled control announces what it acts on, and an unlabelled row of category words beside a category
navigation announces that it is one.

**WHAT WAS REFUSED: RENAMING THE CHIPS.** The words are the four categories the product has, and
giving them a second set of names to say the same four things would make the product speak twice
about one taxonomy. **The label costs one word and no vocabulary.**

**THE LABEL STANDS OUTSIDE THE SCROLLER**, so `.feed-subfilter` is the flex row and the `<ul>` is the
item that scrolls: **a label inside a scroller is a label that leaves.** `min-width:0` on the item,
because a flex item's default `min-width:auto` refuses to shrink below its content and the row would
have pushed the label off the edge instead of scrolling.

**Measured at seven widths in both engines**: the label is 35px, pinned at x=31 at every phone width,
the row is one course everywhere, and **the band from the heading to the first card is 112.0 at 320,
360, 390 and 430, which is exactly what it was before the label.** The name of the group moved with
the visible text, `Filter events by category` to `Show events by category`, so the accessible name
still contains the word a person can see.

**Verified**: 267 documents in both engines at 16 widths, 0 horizontal scroll, 0 duplicate ids, 0
page errors.

---

## 2026-08-14, the reader's word - `Frequency` was the vocabulary of whoever built the market, and four viewport caps turned out to be two questions

**TWO THINGS WERE WAITING ON A DECISION RATHER THAN ON WORK, AND BOTH ARE TAKEN.**

**`Frequency` IS A REAL ATTRIBUTE AND WAS THE WRONG WORD FOR IT.** Markets are one-time or recurring
at an Hourly / Daily / Weekly / Monthly cadence, every cadence instance is its own Event, and the
filter filters by the series attribute: decided 2026-08-10 and carried by `PRODUCT.md`,
`ia/docs/sitemap.md` and backlog 11. None of that is in question. **The label was.**
`voice/docs/voice.md` principle 3 says it in one line: *we use the words a news-follower already
owns*, and **`frequency` is the vocabulary of whoever built the market**, not of somebody who came
to bet on a shutdown. It reads `How often` now, and the default value went `All` to `Any` with it,
because `How often: All` is not a sentence and `How often: Any` is.

**THE MODEL KEEPS ITS WORD AND THE READER GETS THEIRS.** The Event attribute is still `Frequency` in
`PRODUCT.md` and in the sitemap's entity table, the radio group is still `name="freq"`, and the
script comment says which is which. **A label and a field are allowed to differ, and pretending they
must be the same is how a product ends up speaking its own database.** Both documents now carry the
split explicitly rather than leaving the next reader to find two words for one thing and assume one
of them is stale.

Changed: **88 documents in both trees**, the summary label, the radiogroup name, the default value,
the `aria-label`, and the `How often` row in the event detail's facts list on 9 screens per tree.
Plus 3 kit pages and 3 groups in `microcopy.md`. `Frequency` survives in the two trees **209 times
and every one is inside the same script comment**, which names the attribute on purpose.

**AND THE FOUR VIEWPORT CAPS WERE TWO QUESTIONS.** The row asked whether the product wants one number
instead of four. It wants one number for one of the two things it was asking about. **A sticky RAIL
caps at the viewport minus its own top offset** and the three rails already share one formula with a
parameter, `calc(100svh - X - var(--space-16))`. **A modal SHEET caps at a fraction of the viewport**
and the three sheets did not: `92vh`, `88dvh`, `92svh`, two numbers and two units, and only one of
the three had an argument written beside it. They read `--sheet-cap:92svh` now. **92** because it was
already two of three and 88 was the one with nothing to defend it. **`svh`** because it is the SMALL
viewport, the one measured with the browser's own bar shown, so a sheet capped in it always fits and
never resizes under a reader's thumb: `dvh` grows and shrinks as that bar retracts, which for a fixed
modal means the surface moves while somebody is reading it, and `vh` is the LARGE viewport and lets
the tail sit behind the bar.

**The `vh` fallback beside two of them is deleted rather than carried.** `CSS.supports` for `svh` is
true in Chromium 151 and WebKit 26.5, measured before deleting, so it protected nothing here and cost
one number written in two places. **Unifying the sheets with the rails would have been a fifth number
and not fewer**, and the token's comment says so, because the next reader will see four `max-height`
rules and reach for the same tidy-up.

**Verified** in both engines: the cap computes 736px at a 800px viewport, the label reads
`How often: Any`, choosing `Daily` prints `Daily` and lights the dot, and `Reset` returns `Any` and
`Trending`.

---

## 2026-08-14, paying up - A property assignment fires no event, a label is not a tab stop, and a boundary borrowed from another file has to be borrowed in that file's unit

**EVERY ROW THIS SESSION OPENED IS CLOSED EXCEPT THE ONE IT CORRECTED.** 150, 151 and 153 are struck,
and one defect nobody had filed was found on the way.

**150, THE FOCUS TRAP, WAS WORTH THE MOST AND COST THE MOST, BECAUSE THE TAB WALK THAT CLOSED IT
FOUND TWO DEFECTS THE ROW HAD NOT NAMED.** `inert` on every SIBLING along the path from the sheet up
to `<body>` and nothing else, because inert INHERITS DOWN and setting it on an ancestor takes the
sheet with it, which is the `aria-hidden`-over-an-operable-band shape again. Three elements are
skipped on purpose and they are the ones that close it: the toggle, which Space still has to reach,
and the two labels pointing at it. **Sealing the way out along with the room is how a trap becomes a
cage.**

Then the walk said two things the row never had. **The first build listened for `change`, and Escape
sets `checked` from script: a property assignment fires no event**, so the sheet closed and left 26
elements inert behind it, on every screen, silently. That is the same sentence this file wrote about
Reset and the printed value four hours earlier, met again in a different costume, and it is the
argument for **one function that every path in and out goes through**. **The second: `Show results`
and the close were `<label>`s.** A label is exactly right for a pointer and is **not a tab stop**, so
a 262px brass primary was a control a keyboard could not reach and no rule in the system could say
so. Both are `<button>`s now, closed by the same function.

**Verified by a 40-press Tab walk in both engines, which is the only instrument that reads this.**
Every stop is inside the sheet or is the toggle itself. Focus moves in on open, inside a
`requestAnimationFrame` because **activating a label moves focus to its input AFTER the handler
runs**, so a `focus()` called directly is overwritten and the sheet opens with the caret outside it.
Focus goes back where it came from on close, and `inert` reads 0 after Escape.

**AND THE DEFECT NOBODY HAD FILED: A RUNG BORROWED IN THE WRONG UNIT.** `course-chrome.css` lifts the
review toggle below `759.98px` and its own comment says why, that this is where `betpanel.css` docks
the panel. **The dock is cut at `47.5rem`.** The two were written the same day to be one rung and
they are equal only at a 16px root. Measured with `Page.setFontSizes`, the only thing that moves a
rung because a length in a media query resolves against the INITIAL font size: at a **20px** default
the toggle crosses the dock by **4px at 760, 860 and 900**; at **24** by **4px from 760 to 1000 and
5px at 640**. It is `47.49875rem` now and the 132px lift is `8.25rem`, because the furniture it
clears is sized by the type inside it. **0 overlap at all three defaults and seven widths after, and
at the default nothing moved at all.** The 220px sidebar stays in px and that argument still holds:
it is a WIDTH of chrome, not a rung of the product.

**151** is deleted rather than guarded: the whole `uv-subfilter` block is gone from the 40 screens
that carry no such markup and untouched on the one that does. **153** is the pair `92vh` then
`92svh`, which the rails in three files have always had and this sheet never did. The broader
question, whether the product wants one number instead of four, stays open in the row as a decision
rather than a repair.

**And the width-query registry is 32, not 33.** Re-counted from the comment-stripped source, as it is
every time it is written down: 25 rungs, 2 harness, 4 one-offs each carrying its reason, and the
course chrome's, which is the one this rule nearly missed.

**Verified**: 267 documents in both engines at 16 widths, 0 horizontal scroll, 0 duplicate ids, 0
page errors. Desk control at 640, 760, 900 and 1280 identical to every pass this session. The Reset
cycle still returns `Trending` and `All`, hides itself and clears the dot.

---

## 2026-08-14, closing - The `Reads:` line registers colour and nothing else, and the answer was already written under it in all 49 files

**BACKLOG 152 OPENED AND CLOSED THE SAME DAY, WHICH IS UNUSUAL HERE AND IS THE POINT.** The cheap
half was one script. The expensive half was deciding what the line is FOR, and the row was filed
rather than swept because of it. The decision turned out to be already written: **every header in
this folder closes with `Colour goes through a role, geometry straight from a primitive`**, and the
`Reads:` line sits directly above that sentence. It registers the semantic roles. Geometry is not
registered because a radius or a gap has nothing for a theme to override, which is the same argument
`tokens.css` gives for why there is no semantic level for either.

**43 OF 43 COMPLETE, 0 STALE**, rewritten from each file's own body with comments stripped, sorted,
and wrapped at 96 characters. Before: 0 complete, `hero.css` missing 48 of 84, `hiw.css` 42 of 57,
`course-chrome.css` 35 of 46. **The folder had also disagreed with itself about what the line meant**:
`seo-plate.css` listed 21 tokens and every one was a colour, while `logo.css` listed `--space-8` and
`--weight-bold` beside its inks, so half the folder read it one way and half the other and neither
reading made any file correct.

**THE PUBLISHED NUMBER WAS 44 AND THE TRUE ONE IS 43.** The sweep that opened the row matched the
STRING `Reads:` anywhere in a file, and `tokens.css` carries those six characters in a comment on
line 1184, so **the file that DEFINES the roles was filed as the worst offender at failing to declare
them**, 121 of 121. It has no `Reads:` header at all and never should. **A count taken by matching a
string is a count of the string**, which is this repository's own lesson about a selector agreeing
with every hypothesis, met from the other side, and it is corrected here rather than left standing.

**ELEVEN FILES CARRY NO SUCH LINE AND EVERY ONE IS RIGHT TO.** `tokens.css` defines the roles; the
other ten read **0 roles between them**, measured rather than assumed. Six of the ten are the whole
of `patterns/`. **So the rung's invariant that a pattern carries no colour is now visible as the
ABSENCE of a line** rather than as a claim in prose that nothing checks, which is a better shape than
the one this rule had before.

**AND THE INVARIANT UNDER ALL OF IT WAS MEASURED ONCE, AS AN ACT.** A component may read a colour
only through a role, never a colour primitive: `tokens.css` section 1 holds **113 colour primitives**
and **0 of the 49 component files reads one of them**. That is the check the two-line `Reads roles:` /
`Reads scale:` shape was proposed to make permanent, and it is not built, because a measurement is an
act and not a machine.

**THE CONTROL IS THE WHOLE PROOF FOR THIS ONE.** A comment-only change across 40 files must render
exactly nothing, so it is the cleanest instrument this repository has had: three documents,
`event-feed`, `event-detail` and the kit's `filters` page, full-page, animations finished, at 360 and
1280, in a fresh browser per pass. **Six hashes before, six hashes after, identical to the byte.**

---

## 2026-08-14, last - An exit that only exists in the mechanism is not an exit

**THE SHEET HAD THREE WAYS OUT AND A PERSON COULD SEE NONE OF THEM.** The scrim closes it, Escape
closes it, and the cross in the head closes it. The first two are invisible by definition. The third
is 44px in a corner and, in the review build, it is **covered by the course chrome's own toggle**,
which sits at `--z-chrome-top` above every product surface on purpose so the panel stays reachable
while its drawer is open. So the sheet ended in a band of empty surface with nothing in it, and an
empty band under two settings reads as a screen that has not finished loading rather than as a choice
that has been made.

**IT ENDS IN A ROW NOW.** `Show results` is a `<label for>` and not a `<button>`, and it says `Show
results` rather than `Apply` for a reason that is about this product and not about wording: **every
radio in the sheet is live**, so the list behind the scrim has already changed by the time a person
reads the row. `Apply` would name a step that does not exist, which is the same defect as an
accessible name that promises a destination the element does not have.

**`Reset` IS THE OTHER HALF OF THE DOT, AND IT APPEARS ONLY WHEN THERE IS SOMETHING TO RESET.** The
dot added an hour earlier announces that the list is not the default one, and until now the only way
back was to open the sheet and find `Trending` and `All` again in two separate lists. **A signal with
no route out of the state it signals is half a control.** It is the one thing on this component that
has to be script: one `<label>` checks one radio, and a reset checks two. It dispatches `change`
rather than only setting `checked`, because the word printed beside each row is written by the page's
own change listener and **a property assignment fires nothing**; without the dispatch the sheet would
reset the filter and go on showing the old word.

**THE CONDITION IS WRITTEN TWICE AND THAT IS DELIBERATE.** The dot and the reset button need
different `display` values, so one rule cannot serve both. The alternatives are a custom-property
space toggle, which states the condition once and hides what it does, or a class written by script,
which puts a state the DOM already holds into a second place that can disagree with it. **A
duplicated CONDITION is cheaper than either; a duplicated FACE would not be**, and that is the
distinction this folder's rule about doubled selectors is actually making.

**Verified end to end**, both engines: with Sort at `New` and Frequency at `Hourly` the dot is
`block` and `Reset` is `inline-flex`; pressing `Reset` returns the printed values to `Trending` and
`All`, hides itself and clears the dot. 267 documents at 16 widths: 0 horizontal scroll, 0 duplicate
ids, 0 page errors.

---

## 2026-08-14, later still - A chip face is a padding and an icon button is a box, and a sheet row is not a pill on a panel

**BOTH HALVES OF THE FIRST BUILD WERE THE RIGHT MECHANISM WEARING THE WRONG FACE, and neither was
visible in a stylesheet.**

**THE CONTROL.** It shipped as a pill reading `Filters` with a chevron: 93px wide, standing beside a
display-face heading, and the heaviest object in a row whose subject is the heading. It is an
`icon-btn` now, the same circle the header's bell and avatar wear, so the phone's three round
controls are one control. **The first icon-only cut had no drawing at all**: the class was still in
the summary's chip face, so `iconbtn.css` set a 36 x 36 box and `filters.css`, imported later as a
molecule over an atom, set `padding:8px 20px` inside it. **40px of padding in a 36px box leaves a
negative content box**, and the mark rendered as a two-pixel dot in a circle that still looked like
a button. Nothing errored and the control was there; it just had nothing in it. **A chip face is a
PADDING and an icon button is a BOX**, and putting both on one element runs it past every selector
written for either.

**AND AN ICON GIVES UP THE ONE THING THE TWO PILLS WERE GOOD AT**, which is saying what the filter
is set to without being opened. The dot buys back the half that matters: `:has()` reads the radios
already in the document, `[data-default]` marks the two the feed ships with, and the dot appears the
moment either group leaves its default, so a feed sorted by Volume says so on the closed control.
The ring around it is `--bg-plate`, the surface the head stands on, so the brass reads as a separate
object rather than as a bite out of the button's own edge.

**THE SHEET.** It was two full-width pills floating in a padded box with nothing to say what the box
was: no title, no close, 11px rows, and a second tap needed before a single option was visible. **A
control's face is a decision about the SURFACE it stands on**, and a pill that is right in a toolbar
is wrong as a row of a sheet. The sheet has a head now, `Filters` and a close, and its rows are
full-bleed with the hairline they share as their only edge. **The value moved to the far side with no
markup change at all**: `<span>Sort: <span id="sortCurrent">Trending</span></span>` is a text node and
an element, and turning the outer span into a flex row makes the text node an ANONYMOUS FLEX ITEM, so
`space-between` puts the label left and the value right. It reads as a settings list because it now
is one. Type went from 11 to 14 on the rows and on the options under them: eleven is right for a chip
in a toolbar and small for the only two lines on a surface a person came to read.

**KEPT DELIBERATELY: THE TRAILING COLON.** `Sort:` with its value pushed to the far side is slightly
odd punctuation, and the fix is to drop the colon from the markup and put it back at the desk with
`content:':'`. **That moves a character a person reads into a stylesheet**, where `voice/docs/microcopy.md`
cannot own it and no inventory of the product's strings can see it. The dangling colon is the smaller
cost and it is a choice rather than an oversight.

**WHAT WAS ASKED AND NOT ANSWERED: `Frequency`.** It is a real, decided product attribute, not stray
jargon: markets are one-time or recurring at an Hourly / Daily / Weekly / Monthly cadence, every
cadence instance is its own Event, and the filter filters by the series attribute. `PRODUCT.md`,
`ia/docs/sitemap.md` and `backlog.md` 11 all carry it, decided 2026-08-10. **The word is the
question, not the feature.** `Frequency` is the vocabulary of whoever built the market, and this
product's first principle is that a new user is never lost. Renaming it is a voice change across
`microcopy.md`, `sitemap.md`, `PRODUCT.md` and 88 documents in two trees, so it is a decision to take
rather than a tidy-up to slip in, and it is not taken here.

**Verified** on all 267 documents in both engines at 16 widths: 0 horizontal scroll, 0 duplicate ids,
0 page errors. Desk unchanged: every rectangle at 640, 760, 900 and 1280 identical to the pass before
this one.

---

## 2026-08-14, later - The band above the first card was 253px on a phone and the width this project designs from was the only one paying for all of it

**THE COMPLAINT WAS THAT THE HEADING, THE TWO FILTERS AND THE CHIPS EAT THE SCREEN AT 360. Measured
before anything was written, heading to first card, on a coarse pointer: 253.4 at 320 and 360, 201.4
at 390, 149.4 at 430.** Three numbers for four phone widths, and 360 was the worst of them. The
composition: the heading 34.5, the two menus **77** because they stack, the chip row **83** because
it wraps, and the gaps.

**BOTH HALVES BREAK BETWEEN THE WIDTHS EVERY AUDIT HERE READS.** The menus carry their own value, so
they measure 152 and 154; at 360 the feed column offers 298 and the pair needs 314, so they stand one
above the other, and at 390 they do not. The five chips need 332px of row, so the row wraps at every
width below 430. **390 and 1280 are the two widths this repository has always read, and one of them
is on the far side of both breaks.** That is the rung-adjacent shape `CLAUDE.md` already names, met
twice in one band.

**THE FILTERS BECAME ONE BUTTON AND A SHEET, AND THE CHIPS BECAME ONE SCROLLING COURSE.** After:
**112.0 at all four widths.** The band is the same number at every phone width now, which is the part
that matters more than the 141px: a wrapping row grows a whole course when the sixth category
arrives, and a scrolling row grows nothing.

**WHY A CHECKBOX AND NOT A `<dialog>`, AND THIS IS THE DECISION THE REST FOLLOWS FROM.** The two radio
groups have to exist ONCE. A dialog would need its own copy of them, and **a radio group is keyed by
`name`**, so two copies in one document are one group with two sources of `checked` and two sets of
ids: the kit already pays for that with its per-theme suffixes. A checkbox leaves the panels exactly
where they are and moves the BOX they stand in, so the desk keeps the two pills it has and the phone
gets a sheet, out of one markup. **A second form of a control is a second PLACEMENT, never a second
copy of the controls.**

**WHAT THAT COSTS, STATED RATHER THAN HIDDEN.** A checkbox has no Escape and no focus trap. Escape is
bought back by nine lines of script; the trap is not, and it is `backlog.md` 150. **Rejected: a grab
handle.** A handle draws a gesture nobody implemented, which is the same shape as the accessible name
that promised a destination the element did not have, closed here yesterday.

**REJECTED: TWO SHORTER PILLS.** Dropping the words `Sort:` and `Frequency:` fits the pair on one
course at 320 and saves 42px against the sheet's 78, and it costs the sentence: a pill reading
`Trending` under a heading reading `Trending` is one word twice, and the second filter this feed grows
will not fit either.

**THE FADE READS THE SCROLL AND NOT THE PAINT.** A permanent edge fade is the usual answer and it is
wrong twice: it fades the last chip once the row is scrolled to its end, and it fades empty space on a
row that fits. `animation-timeline:scroll(self inline)` binds progress to the row's own scroll, and
**when the row does not overflow the timeline is inactive and the element falls back to its base
style**, which declares no mask at all. So a row that fits has no fade, and it costs neither a query
nor a class to say so.

**THE INSTRUMENT WAS READ BEFORE THE FINDING, BECAUSE A MASK HAS COST THIS SYSTEM TWICE.**
`CSS.supports` is true for the timeline in Chromium 151 and WebKit 26.5; the computed `mask-image`
MOVED when the row was scrolled, in both; and the row was screenshot with the mask live and with
`mask-image:none` forced, **which differ in both engines, while the same shot taken twice unchanged is
byte-identical**. That third reading is the control and the first two prove only that a property
parses. One layer and no `mask-composite`, because the two-layer mask drew nothing in WebKit.

**AND THE SCROLLER FOUND A LIVE DEFECT NOBODY HAD FILED.** `.cat-nav>ul` has been a one-line scroller
all along, and **on 3 of the 5 category pages at 360 the chip carrying `aria-current` stood off the
right edge**: Crypto by 92px, Culture by 223, General by 356, which is the whole chip. A person landed
on a page whose navigation showed nothing selected. `scroll-start-target` is the CSS answer to exactly
this and **neither engine supports it**, measured before reaching for a script, so it is nine lines on
the 57 screens that carry the strip and the script's first comment says why it is not CSS. **0 of 106
now.**

**TWO SMALLER THINGS WERE MEASURED WRONG FIRST AND ARE WRITTEN DOWN BECAUSE OF IT.** The scroller's
focus ring needed room, and block padding with an equal negative margin does not hand the height back
in a block container, it hands it to the neighbours: **4px above the row and 12 below, where the file
declares 2 and 16.** The ring turns inward instead and costs no geometry. And the sheet's backdrop was
`--scrim`, whose own comment in `tokens.css` says it is the COURSE DRAWER's: 30 per cent of black over
graphite darkened nothing and the surface did not read as modal. It is `--shadow-ink-45`, which is
what `dialog.app-dialog::backdrop` already is. **Picking the nearest-sounding token is how a product
grows two answers to one question.**

**A DEAD RULE WITH A LIVE SENTENCE BESIDE IT IS WORSE THAN A DEAD RULE.** The block this replaced was
`@media(max-width:39.99875rem){.filter-menu{position:relative}}`, restating at a rung the exact value
the first line of `filters.css` declares unconditionally. It could not change a pixel at any width,
and `ui-kit/filters.html` carried the prose version of it for as long as it stood. The rule is what
gets deleted; the sentence is what the next reader believes.

**Verified**, 106 painted screens, both engines, at 16 widths including every rung and one pixel
either side: 0 horizontal scroll, 0 duplicate ids, 0 page errors, 0 screens with the active chip off
screen. Touch floor asserted: the new button measures 44 on a coarse pointer and 34.5 on a fine one,
the same pair as the summary it stands in for.

---

## 2026-08-14, after the push - The dialog and the page stopped being one markup, and the picture of a component is the component with every control replaced by an element that is not one

**THE ROOT RULE THAT A DIALOG WITH A STANDALONE PAGE IS ONE MARKUP AND NOT TWO IS DELIBERATELY SPENT
HERE.** It is a good rule and it was earned: the two copies drift, and this repository has the scars.
It is spent because the two hosts stopped answering the same question. A person who taps How it works
in a header wants to know what the thing IS in fifteen seconds and then to be let in; a person who
opens the full guide already has a question and wants the answer. The dialog is three steps with a
picture each and a way in at the end; `how-it-works.html` keeps the prose, the FAQ and the sentence
about money being held 1:1, which is the only place that sentence is written out. `hiw.css` said "one
block with two hosts" at its head since 2026-08-11 and now says two blocks with one host each, and
the file keeps its name for the reason backlog 18 gave it: **a component is not named after one of
its places**, even when only one of its two blocks now stands in a dialog.

**THE STAGE IS THE PRODUCT AND NOT A DRAWING OF IT.** Each step stands on a still built from the
classes the screens ship: `.card` with its `.thumb`, `.q`, `.why` and `.yesno`, then `.bet-panel`
with `.bp-dir`, `.bp-side` and `.line.total`, then `.pos` with a won side. Nothing is redrawn, which
is why `hiw.css` reads none of their tokens and why the inventory still counts none of their elements
as this component's. **The alternative was three generated illustrations in the Vault grade, and it
was refused on the same grounds the trust drawings were re-encoded on**: `assets/` went from
9,690,253 bytes to 985,277 over two days, and a picture of a card that is not the card goes stale the
first time the card changes.

**NOT ONE ELEMENT IN A STILL IS FOCUSABLE, and that is what makes it a picture rather than a fake
control.** An `<a>` with no `href` is not a link and not a tab stop, and it still matches every `a`
in `card.css` and `yesno.css`, so **the face arrives and the behaviour does not**. `.btn` and
`.yesno-pick` are class-keyed and take a `<span>`. The one control that could not be made inert, the
card's bookmark button, is simply not in the still. The stage is `aria-hidden` on top of that, and
that is safe to write ONLY because there is nothing focusable inside it: aria-hidden over a focusable
element is a defect and not a decoration. Measured across all 107 steppers in both trees, at 390 and
1280, in Chromium and WebKit: **0 focusable elements inside a stage.**

**THE BET PANEL IS A WIDTH-ONLY FACE AND THE STILL TAKES THE BARGAIN**, which is the rule
`ui-kit/CLAUDE.md` already states for `.tk-show-panel`: the test is whether the placement SAYS what
it changed. Three declarations, and they are exactly the three about where the panel stands rather
than what it is. `.bet-panel` is `display:none` below DETAIL 760 and `flex:0 0 322px` above it, so
inside a 464px dialog the still would have drawn **nothing at all on a phone** and held a 322px
column inside a 296px stage on a desk. The plate, the ground, the border and every rule `.bp-inner`,
`.bp-dir` and `.line.total` take from being inside a panel are untouched.

**THE STEP IS SWITCHED BY A RADIO, THE RULES ARE KEYED TO `:nth-of-type`, AND THE KIT SUFFIXES THE
NAME AS WELL AS THE ID.** Same bargain `tabs.css` made on 2026-08-10 and for the same two reasons: an
id in a selector is a promise that the component stands once in a document and this one stands twice
on its own kit page, and **a radio group is keyed by `name`, so two cells sharing one are one group
and the light cell's checked step unchecks the dark cell's**. There is no script: a `<label for>` is a
real control with a real target, and this tree is read from disk where a script is one more thing
that can fail to arrive.

**THE SHEET DOES NOT RESIZE UNDER A THUMB, AND 39px OF IT STILL DOES.** Measured before the floors,
at 390 and 1280: the three steps stood **552, 641 and 506** tall, so pressing Next moved the button
89px down and then 135 up. With a 280px stage floor and a 172px text floor: **564, 564 and 603**. The
280 is the tallest of the three stills plus its shadow, measured, so no still is clipped by its own
floor, and the still is CENTRED in the stage rather than stretched to it, because three pictures of
three different components are three different shapes and it is the frame that has to be constant.
**The 39 that is left is step 3 carrying one more control**, the quiet way out under the primary one,
and reserving that row on the first two steps would buy an identical height with 39px of empty sheet
on two screens out of three.

**Where it leads, and it is the product's own stance rather than the reference's.** Step 3 gives
`Create account` to `sign-in.html`, whose own heading is "Sign in or create account", and under it
`Browse events first` to the feed, because this product lets a person build a bet before connecting a
wallet and a single funnel-shaped exit would contradict a sentence the same dialog just made.

**Swept and checked.** 105 painted screens, 87 grey ones and 2 kit cells: **107 steppers, 0 with a
wrong step count, 0 with a `<label for>` pointing at nothing, 0 focusable elements in a stage, 0
duplicate ids, 0 pages scrolling sideways, 0 page errors**, at 390 and 1280 in Chromium and WebKit.
One new token, `--display-step`, and the copy is in `voice/docs/microcopy.md` with the eight lines it
replaces struck rather than moved.

---

## 2026-08-14, last thing - The rule was not redundant, it was over-broad by 400px, and the width it is really about is not on the ladder

Supersedes the entry below on backlog 149, which it filed as open. It closed the same hour, and the
measurement that closed it is the one nobody had taken.

**THE QUESTION LOOKED BINARY AND WAS NOT.** `header.css` hides `.hiw-btn` below DETAIL 760, cut on a
measurement that is still in the file: at 641 the signed-in desk row asked 694px against a 641px
window and 73 of 106 painted screens took horizontal scroll from 641 to 652. **36 of that 694 was the
hamburger and 8 was its gap**, and the hamburger was deleted an hour earlier, so the row was filed as
"the justification expired, flip it or leave it". Both of those answers are wrong. **The rule is
still doing real work; it is simply cut about 400px too high.**

**Walking it found the width, and three snapshots would not have.** Forced visible at 641, 652, 660,
700 and 759 the label is free: 0 pages scrolling sideways, 0 header rows overflowing, worst intrinsic
row demand 535.8 at 641 against the 694 above. Walked DOWN at 4px steps from 320 instead: **32 of the
105 screens overflow their header row, by 38px at 320 falling exactly 4px per 4px of width to 2px at
356, and 0 of 105 from 358 up.** A linear ramp to zero is what a single unshrinkable row looks like,
and the bisection lands on 358.

**The 32 are the mirror of the original 73.** They are exactly the logged-out screens, every one
carrying `.auth-btns`, and the file's own paragraph says the 73 were the signed-in ones because "the
other 33 carry `.auth-btns` where the balance figure stands and are narrower". The narrower pair is
now the wider of the two, because what left the row was 44px shared by both and what remains differs.
**A population that was the safe half of a measurement can become the failing half without anything
changing about it.**

**358 DOES NOT BECOME A RUNG, AND THAT IS THE DECISION RATHER THAN THE NUMBER.** The system holds
three widths, 40rem, 47.5rem and 56.25rem, and the registry exists so that a fourth cannot be
introduced quietly. **A number bought for one control is the exact purchase it was written to stop**,
and 358 would also be a rung with 2px of slack at 356, which is an edge rather than a margin. The
rule moves to DESK 640, a rung the system already declares, and the band from 641 to 759 comes back:
119px where the label was hidden for a reason that had stopped being true. Below the desk it stays
hidden and nothing is unreachable, because every feed carries a second trigger for the same dialog
and `how-it-works.html` is a page of its own.

**As shipped, both engines, all 105 screens:** hidden 0 of 105 below 640, shown 105 of 105 from 640
up, and 0 pages scrolling sideways at 320, 390, 639, 640, 641, 759, 760 and 1280. The width-query
registry is unmoved at 34; `47.49875rem` goes 3 to 2 and `39.99875rem` 8 to 9.

---

## 2026-08-14, end of the day - A button whose accessible name was a destination and whose element had none, and a control reserved for a future that had not arrived on 105 screens

Two asks, both of them turning out to be defects with a paper trail.

**THE HEADER'S LOCKUP ANNOUNCED A DESTINATION AND DID NOT HAVE ONE.** It was
`<button type="button" class="logo logo-btn" aria-label="Yonder - go to Events home">` on all 105
painted screens, with **no `href`, no `form` and no handler anywhere in the tree**. Below 640 it is
the only target on the left of the row, and `header.css` says so in a comment that opens "the
wordmark is a button that goes home". Nothing did. The footer's lockup and the two plate signatures
were `<span>`, which is the quieter half of the same thing: they went nowhere and did not claim to.
**All 221 product placements are `<a href="event-feed.html">` now**, plus 36 in the kit pointing one
folder over, and the face gained the one property an anchor brings that a button and a span do not,
`text-decoration:none`. The `background`, `border` and `padding` resets stay, because a face that
only resets what the CURRENT element brings is a face waiting for the next element.

**`footer.css` had to be narrowed rather than overridden, and that is the general rule for this.**
Four selectors there paint links: rest `--text-muted`, hover brass, an underline, and a pressed
ground. Every one is (0,1,1) or better against `.logo`'s (0,1,0), so the footer would have repainted
a face it does not own the moment the lockup became an anchor. They carry `:not(.logo)` now. **A
placement file narrows its own rule; it does not override somebody else's face**, which is the same
move `.bt-by` and `.seo-by` already make by declaring no ink at all. The lockup does take the press
ground the header gives it, so the two read as one control on two ends of the page.

**THE HAMBURGER WAS RESERVED FOR A FUTURE THAT NEVER ARRIVED AND IT COST MORE THAN ITSELF.** A
`<button>` labelled "Menu (reserved for future scaling)" with no handler and no drawer behind it,
`display:none` below the desk on top of that, so on a phone it was a control that did not exist and
on a desk it was a control that did nothing. Deleted from **105 painted screens, 87 grey ones and 10
kit specimens**. What went with it is the interesting part:

- **`.app-header .left > .icon-btn{display:none}`**, and then the whole `max-width:39.99875rem`
  block in `header.css`, which held nothing else but two headstones. **A rule that hides a control
  below the desk is a rule whose entire content is an opinion about that control**; with the control
  gone it is a selector matching nothing, and an `@media` block with no declaration is the same
  thing one level up. The width-query registry goes 35 to 34.
- **`l-menu` out of `assets/icons.js`.** Its only remaining reader was `ui-kit/icons.html`, which
  draws the shape from its own inline path rather than through `<use>`, so the symbol had zero
  readers at all. **A symbol whose only reader is the page that documents the sprite is a glyph with
  no placement**, which is what `account` was deleted over. 35 symbols to 34, 30 filled and 4 line,
  and the page's "34 glyphs" badge had been one short against 35 for as long as it had stood,
  disagreeing with the two badges beside it.
- **The icon-button atom is down to two marks.** The plain circle goes from 242 placements to 137,
  all of them in the header's utility group, and `iconbtn.html`'s specimen led with the hamburger
  until today, which was already filed here as the case where a count is right and the picture under
  it is one third of the thing. Now it would have been a picture of nothing.

**AND THE 1,361 IN THE INVENTORY DOES NOT REPRODUCE.** Re-measured by the column's own stated
method, every element wearing one of `iconbtn.css`'s eight declared classes read from the rendered
DOM of all 105 screens: **731**, at 390 and at 1280 alike, of which `#l-close` takes 333 and
`#i-bookmark-b` 198. The old figure is left named beside the new one rather than quietly replaced,
because **a number measured by an unrecorded method cannot be corrected, only re-taken.**

**WHAT THE DELETION GAVE BACK, AND WHY IT IS A ROW RATHER THAN AN EDIT.** `header.css` cuts the
DETAIL rung to hide "How it works" below 760, and it states the measurement it was cut on: at 641
the signed-in desk row asked 694px against a 641px window and 73 of 106 screens took horizontal
scroll from 641 to 652. **36 of that 694 was the hamburger and 8 was its gap.** Re-measured, not
re-derived: with `.hiw-btn` forced visible across all 105 screens at 641, 652, 660, 700 and 759,
**0 pages scroll sideways and 0 header rows overflow**, and the worst intrinsic row demand at 641 is
**535.8px**. The rule now hides a control for a reason that expired. It is left standing and filed as
backlog 149, because **a rule whose SUBJECT is gone is a defect and a rule whose JUSTIFICATION
expired is a decision**, and whether that label belongs in the header at 700px is a decision about
the band.

**Checked, both engines, from disk.** 163 documents: **257 lockups, every one an `<a>` with an
`href`, no underline, its mark painting and a real box; 0 burgers left; 0 dangling `<use>`; 0 page
errors.** Fourteen widths at the rungs and one pixel either side: 0 pages scrolling sideways, 0
overflows.

---

## 2026-08-14, after that - The footer's stylesheet promised in prose what one of its own declarations was breaking, and the lockup now has two faces divided by what it is DOING

Supersedes the two entries below on the counts: the signature size is worn by **116 placements** and
not 11, and `logo` in the footer is **FIXED 95.6** and no longer FILLS.

**THE FOOTER LOOKED UNCHANGED BECAUSE IT WAS, AND LOOKING AT IT FOUND A DEFECT OLDER THAN TODAY.**
`footer.css` carries this comment thirty lines under the brand block, and it has since the file was
written: *the same inset as every other band, so the first footer column starts on the same x as the
logo above it*. It did not. `.footer-logo` read `justify-content:center`, so the lockup was centred
inside a 240px brand column while the tagline and the language menu under it were flush left, at 14
on a phone and 260 at 1280. **The file promised the alignment in prose and broke it in a
declaration**, which is the shape this repository keeps meeting: a comment has no reader, so a rule
that contradicts one costs nothing until somebody looks at the page.

**It was the only text-bearing thing in the footer that was centred.** Walked over every element of
the footer at 390 and at 1280 reading `text-align`, `justify-content` and `align-items`: two boxes
came back centred, this lockup and `.footer-trust`, which is a row of three tiles and a different
kind of centring. **A centring with no majority is a leftover**, and this one was left over from a
phone footer that centred everything and has not for two stages. `logo.css` had even written the
leftover down as a fact about the system, "the centring under a phone footer is `footer.css`", which
made a defect read as a division of responsibility.

**The stretch went with it, and that is why the published FILLS was never about this component.**
`.footer-logo` was a flex child taking its column's full width, 292 at 320 and 611 at 639 and 240
from 640 up, and the width was doing exactly one thing: giving `justify-content:center` something to
centre inside. With the centring gone the width does nothing, so the lockup shrink-wraps and reads
**FIXED 95.6 at all thirteen widths**. `ui-kit/docs/inventory.md` had this filed as the second of two
answers on width; it was a fact about a slot wearing the component's name, which is the verdict rule
this repository already wrote for `navitem` and `chip`.

**TWO FACES NOW, AND THE LINE BETWEEN THEM IS WHAT THE LOCKUP IS DOING.** In the header it is a
control in a 44px row: default 16px, 86.1 wide, untouched. In the **116** places where it SIGNS a
block, the footer of all 105 screens plus the eleven plate signatures, it runs `--logo-size:
var(--text-20)` and measures 95.6. It is still one drawing and one proportion; a slot asks for a size
and the mark, the gap and the tracking follow. **The rule is not "the footer is bigger", it is "a
signature is bigger than a control"**, which is a sentence somebody can apply to the next slot.

**And the footer aligns by INK like the two plates do.** `margin-left:var(--logo-bleed)`, measured
after: the mark's ink lands on 14.0 at 390, 40.0 at 900 and 260.0 at 1280, against a tagline at 14.0,
40.0 and 260.0. Exact at every width. The box now hangs 3.84px into the footer's own gutter, which is
14px at 390 and 20 above the desk, so nothing is clipped and nothing overflows: re-checked across
163 documents on two engines, **0 pages scrolling sideways, 0 signatures failing to paint, 0 page
errors**, and across fourteen widths at the rungs and one pixel either side, 0 overflows.

---

## 2026-08-14, last - The mark's ink is 17.08 per cent of its box in from each side, so a lockup that is aligned by its box is aligned 3px wrong, and the size that had no placement now has one

Supersedes the entry below on two numbers: the signature is **FIXED 95.6** and not 78.1, because it
runs at 20px type and not at 16.

**THE LOCKUP LOOKED MISPLACED AND WAS PLACED EXACTLY WHERE IT WAS PUT.** Its box sat on the same left
edge as the quote above it, to the pixel, and it still read as indented. The mark is a 24x24 SVG whose
ink does not reach its own edges: painted at 480px on a canvas and read for the leftmost and rightmost
pixel above 8 alpha, the ink runs **82 to 397 of 480**, so it stands **17.08 per cent of the box in
from each side** and 14.58 from the top and the bottom. **The reader sees ink and the layout sees the
box.** Centred in a row of its own, which is what the header and the footer do with it, the symmetric
bearing is correct and invisible. Aligned against a COLUMN OF TYPE it is neither: at the 22.5px box
the mark's ink began 3.84px right of the headline standing over it.

**The distance is a fact about the drawing, so `logo.css` states it and spends none of it.**
`--logo-bleed` is `calc(var(--logo-mark) * -0.1708)`, and the two signature slots are the only things
that write `margin-left:var(--logo-bleed)`, because they are the only two placements that have to
line up with type. Measured after, on both plates, at 390 and 1280, in Chromium and WebKit: the ink
lands **0.01px** from the headline's left edge, eight readings out of eight. This is the same shape as
the `getBBox` finding on the icon set, one folder over: **a mask is invisible to a box measurement,
and so is a side bearing.**

**THE SIZE VARIANT THE ANTI-RULE RESERVED NOW HAS A PLACEMENT.** `ui-kit/logo.html` has carried
"never give the mark a size variant it does not wear" since the file was written, and the rule was
never "one size", it was "no size with no placement". The signature is the placement. What it got is
a **RATIO and not a second face**: `--logo-size` is the type, the mark box is `calc(var(--logo-size) *
1.125)`, and at the default 16px that is the 18px box this component has always drawn, so **the
header and the footer are byte-for-byte where they were** - re-measured across all thirteen widths,
86.1 in the header and 292 / 332 / 362 / 611 / 240 in the footer, identical to the reading taken an
hour earlier. The signature asks for `--text-20` and the mark, the gap and the tracking all follow it.
There is still one drawing and one proportion, and changing the proportion changes all 221 placements
at once, which is the argument for a ratio over a variant.

**Why 20 and not 24.** The tile's quote is `--display-quote`, a clamp that computes 20px at 390 and
23.68 at 1280, and the SEO tagline is larger again. A signature at 24 would have met the quote at its
own size on a phone, and a signature is subordinate to the statement it signs or it is a second
headline. 20 is the largest step that stays under the quote at every width.

---

## 2026-08-14, later - A margin below a flex child is added to the gap and never merged with it, and the two plates that exist to name the brand were the only two naming it without its mark

Three findings from one reading of the phone, all of them raised by looking at a screenshot rather
than at a file.

**THE CATEGORY STRIP CHARGED A PHONE 126px TO SHOW A 48px CHIP, AND HALF OF THAT WAS BOOKED TWICE.**
Measured at 360 and 390 before anything moved: 16px of `.feed-inner` margin, a 78px plate around the
strip, and **32px under it against 16 at 640, 900 and 1280**. The 32 is the finding. `.feed .feed-inner`
is `display:flex;flex-direction:column;gap:var(--space-16)`, so every child of that column already
has 16px under it at every width; `catnav.css` carried a mobile-only block adding
`margin-bottom:var(--space-16)` on top of it. **A margin on a flex child is ADDED to the container's
gap, never merged with it** - that is the difference between flex and the adjacent-margin collapse
everybody has the intuition for - so the narrow screen paid double for the same rhythm and the wide
one paid once. The block is deleted and nothing replaces it, because the column already says the
number. The plate's own vertical padding goes 12 to 8 below the desk in `base.css`, which is the
other 8: the plate is the page frame's business and `catnav.css` has said so since it was written.
**126 to 102 on a phone, the desk unmoved at 78 + 16.**

**AND THE OVERRIDE HAD TO STAND AFTER THE DECLARATION, NOT INSIDE THE BLOCK ALREADY CUT AT THAT RUNG.**
`base.css` opens the section with a `max-width:39.99875rem` block for the page frame, and putting the
plate's padding there would have rendered nothing at all: **a media query adds no specificity**, and
`.feed-inner>.cat-nav` is (0,2,0) in both places, so the later one wins whatever the width is. Two
blocks at one rung in one file is the cost of that, and the alternative is a rule that silently never
applies. The registry is unmoved at **35 width queries**, because `catnav.css` lost one and `base.css`
gained one.

**THE BRAND TILE WAS A POSTER PINNED TO THE TOP OF ITS OWN FRAME.** `.hero-promo.brand-tile` was
`display:block`, so the stack sat on the top padding and every pixel the tile had beyond its content
fell out of the bottom. Measured on both tiles at 390, 900 and 1280: **25.0px above the mark against
53.8 under the signature on the feed, and 25.0 against 101.5 on how-it-works**, where the side column
asks for a 250px minimum and nothing was using it. Four to one. What made it visible rather than
merely true is the brass frame `::before` draws at `inset:var(--space-12)`: the frame does not move,
so the emptiness has an edge to be measured against by eye. It is a flex column centred on its cross
axis now, `align-items:flex-start` because a two-line poster centred against itself reads as ragged,
and the two gaps are equal to the tenth of a pixel at every width in both engines. **The left inset
is 32 against 24 on the other three sides**, so the type starts 20px inside the frame on the left and
12 on the right, which is a book's gutter and fore-edge and not an accident.

**ELEVEN PLACEMENTS SPELLED THE WORDMARK BY HAND, AND THEY WERE THE ELEVEN WHOSE WHOLE JOB IS THE
BRAND.** `hero.css` declared `.bt-by` and `seo-plate.css` declared `.seo-by` as the body face at 13px
in brass, each with the letters "Yonder" written into the markup and **no mark at all**. `logo.css`
is the file that already refuses this from the other end: a brand mark is not in the system, it keeps
its own drawing, and no generic glyph may stand in for it. The two plates carrying those classes are
the brand tile (2 placements) and the SEO plate (9) - the only two things in the product that exist
to name the brand, and therefore the only two places where naming it wrong costs anything. They carry
`class="logo bt-by"` and `class="logo seo-by"` now, and the two placement files were cut back to what
they own, which is WHERE the lockup stands: a `margin-top` in one, a `margin-top` and an `align-self`
in the other. **Neither declares a font, an ink or a letterspacing, so the files cannot fight over the
face whichever order they are imported in.** `logo` goes from 210 placements to 221.

**The third placement is a third answer on width, and it corrects the published number for the first
one.** The signature measures **FIXED 78.1 at all thirteen widths** in both slots. The header's
published 86.1 is the same lockup plus 4px of press padding on each side: 78.1 is the component and
86.1 was always the component plus its slot. `ui-kit/docs/inventory.md`, behaviour on width.

**The ink went UP and that is worth saying because it looks like a colour change.** The signature was
`--text-brass-lit` and is `--text-primary`, which is the same ink as the tagline standing directly
above it on the same ground in both themes, so nothing new had to be measured for contrast: the
signature is now exactly as safe as the line it signs.

**What was checked, and the instrument first.** All 163 documents in `ui-visual/` and `ui-kit/`, at
390 and 1280, in Chromium 151 and WebKit 26.5, from disk: **46 signature placements per engine, 0
failing to paint their mark, 0 pages scrolling sideways, 0 page errors.** Side-scroll was read as
`document.scrollingElement.scrollLeft = 9999` and then read back, never as `scrollWidth >
clientWidth`, which is the rule this repository wrote for itself the day before. The two changed
plates were then read at the rungs and one pixel either side - 320, 360, 390, 639, 640, 641, 759,
760, 761, 899, 900, 901, 1280, 1600 - for the quote overflowing its own tile, because the tile went
from `display:block`, where the quote filled the width, to a flex column, where it shrinks to fit:
**0 overflows, 0 tiles scrolling internally, in both engines.**

**What was NOT done, and it is a look decision rather than a defect.** The generic zigzag above the
quote stays on both plates. With a real mark now standing below it the tile carries two marks, and
whether that is one too many is a question about the poster and not about the system.

---

## 2026-08-14 - The same origin rule had a third victim and it was the type, and the sweep that opened the horizontal-scroll row could not tell a page that scrolls from a page that cannot

Four open rows worked in one pass, and three of the four turned out to be about a premise rather than
about the thing in the title.

**147, the type, is the third time `file://` has cost this repository something, and it is the
largest.** `assets/icons.js` had to be a script because an external `<use>` is a cross-document
reference and a disk page drew 0 of 34 glyphs. The trust drawings had to become `data:` URIs because
a mask image is a CORS-enabled fetch. **A font is a CORS-mode fetch too, even from its own origin**,
which `components/fonts.css` has said out loud since the day the preload was written, as the reason
`crossorigin` was not optional on it. Nobody followed the sentence through. Measured on 2026-08-14 by
rendering a probe string at 40px from disk rather than by reading the file: in WebKit
`'DM Sans',serif` came back at **369px, which is the serif fallback to the pixel**, and so did
`'Space Grotesk',serif`, against 410 and 435 in Chromium. Only IBM Plex Mono arrived, through the one
`local()` in the file. **So the product read from disk in Safari was set in a fallback face, whole**,
and every reading anybody has ever taken here of type, measure, line length, wrapping or layout shift
on a disk page in that engine was taken of something else.

**Only four of the eight faces were ever fetched by anything, which is what made the fix small
enough to take.** All 163 documents were rendered and their font requests counted: `dm-sans-var-latin`
163, `space-grotesk-var-latin` 163, `ibm-plex-mono-600-latin` 109, `ibm-plex-mono-500-latin` 104, and
the four `-latin-ext` files **0 times each**, because the product contains no extended-latin
character. The four that are used are `data:` URIs in `fonts.css` now, 79,480 bytes raw and 105,980
as base64; the four that are not stay as file references, and on the day a European name appears they
will work over http and fail from disk in WebKit, which is written into the file rather than left to
be discovered.

**And the 326 `<link rel="preload">` lines went with them, along with the comment block above each
pair, so no document in this repository now says anything about a font.** A preload exists to start a
fetch early; a `data:` URI has no fetch to start and the face is ready the instant the stylesheet
parses. The 0.0000 layout shift those lines bought was re-measured at 400 Kbps over a quarter of the
painted tree, 27 screens, before and after: **mean 0.0000 both ways, worst 0.0000 against 0.0001, 0
screens above 0.0005.** `docs/backlog.md` 141 named the 163 documents as a dependent that had to be
managed by re-measurement; the dependent is deleted instead.

**The price is named and it is real: +38,605 bytes on the mean screen.** Every response body on all
106 painted documents, mean CSS 877,387 to 984,717 against mean fonts 68,725 to 0. The 53 documents
that never use the mono carry it now anyway, and that is the genuinely worse half of the trade. What
it buys is the type system working in both engines over both protocols, and a whole class of edit
that no longer touches 163 files.

**148, the last placement of the trust drawings, is a mask now too.** `.ht-art` was six `<img>`
elements across two documents, the fourth and most visible placement at `opacity:.6`, and it is
`.hero-trust::after` taking `--trust-art-column` and `--trust-art-globe`. **Which drawing is a
decoration's question and not a screen's**, so it is keyed on `nth-of-type` the way the footer strip
keys its three. That is the OPPOSITE call `card.css` makes about the event photograph, and the
difference is the test: a photograph names the event and somebody editing the feed chooses it, while
a column and a globe behind a trust claim are the component saying the same thing twice and nobody
chooses between them. Measured on both engines at 390 and 1280 with a control of 0.00: 13 to 30 per
cent of the hero region's pixels differ at a mean of 1.58 to 2.59 of 255, the largest of the four
placements because it is the least faded, and the drawing reads slightly cleaner rather than worse.
`assets/` is **985,277 bytes in 23 tracked files**, from 9,690,253 two days ago.

**146 was wrong about the mechanism in two ways at once, and the second one matters more than the
row.** It said four course documents scroll horizontally and blamed tables, with the fix named as
`overflow-x:auto` per table. Every element the opening sweep called a culprit was already inside a
scrolling container. The real overflowers are **four pieces of `white-space:nowrap` on prose and one
flex row**: `.funnel-step-metric` and `.gap-item .source` in `research/research.html`,
`.evidence-source` in `user-research/jtbd.html` at 264px of unbreakable filename, `.legend span` in
`ia/sitemap.html` at 359px, and `concept/concept.html`'s seven-item `.appbar` needing 370. **A
filename is exactly the string that has to be allowed to break.** After: `scrollWidth` equals
`clientWidth` exactly on jtbd at 320, 360 and 390, on sitemap and concept at 320 and 360.

**And none of those documents ever scrolled.** Set `document.scrollingElement.scrollLeft = 9999` on
any of the four, before the fix or after it, and it reads back **0**. The content stood past the right
edge with no way to reach it, which is a worse thing than scrolling and a different one.
**`scrollWidth > clientWidth` is not a page that scrolls sideways**, and it is the predicate behind
every horizontal-scroll number this repository has published, including the 1,335 readings that
proved the product trees clean. What is left is 15px on `research/research.html` at 320 alone,
bisected leaf by leaf to no single element, the largest contributor a `<p>` of ordinary wrapping prose
worth 8px.

**The sweep after all of it says the product did not move, and getting to that sentence needed the
review panel taken out of the frame.** 163 documents, both engines, 390 and 1280, against the
pre-change tree, control 0.00 and 0 size mismatches outside `ui-kit/typography.html`, whose prose
this change rewrote. Read whole, 127 of 326 readings differ in Chromium and 100 in WebKit, with a
worst channel delta of **198** spread thinly over dozens of product screens, which reads like a
regression and is not one. **Every one of those pixels is at x below 220**, inside the review
sidebar, and it is the panel's text sitting one device pixel lower: the panel scrolls its active row
into view, and with the faces now ready at first layout that scroll lands on final metrics instead
of on metrics that were still arriving. Re-diffed from x=220 rightwards, the product is **0.000 per
cent differing, worst 0, on every screen in both engines** except `event-feed.html`, which is the one
screen `.ht-art` stands on and moves 0.51 to 0.56 per cent at a worst of 46 in Chromium and 89 in
WebKit. **The review chrome is 220 physical pixels and it is inside the frame of every full-page
comparison taken here**, so a whole-page sweep reports the instrument's own furniture as a finding.

**139 is now the smallest it will get without a design decision.** The byte objection that blocked a
bigger export is gone, because the drawing is a q20 mask and a bigger one costs almost nothing. What
blocks it is that **the shipped 520x600 frame is not in the 1254x1254 master.** Searched three ways:
horizontal-only at the shipped aspect gave a flat curve, best 30.02 of 255 against a worst of 32.23;
a full two-dimensional sweep over offset and scale found signal but no match, best 18.66; and a local
refinement fitting the best gamma and gain at every candidate, which is the mapping that would explain
an alpha plane made from a luminance one, only reached **15.94 at gamma 1.2** where a true alignment
would be single digits. These four shipped frames are not a crop of these masters. **There is a
cheaper answer that touches no artwork**: the demand comes from `mask-size:auto 122%` tying the
drawing to a plate that grows with the page, and `.card::after` asks 168x194 of the same drawing and
needs nothing. The plate is asking for too much; the drawing is not too small.

## 2026-08-13, last - A mask image is fetched with CORS and a background image is not, so the thing that broke the trust strip was reading the page from disk

**The rollback four hours ago named the wrong cause, and the entry that recorded it is the one this
entry supersedes.** It said `mask-mode:luminance` parses without being honoured and that `@supports`
is blind to exactly that. **Both halves are false.** A second rendering engine went into the harness
today, WebKit 26.5, which is the same WebKit as the Safari on this machine, and the mechanism was
put to it directly: **Chromium 151 and WebKit 26.5 both honour `mask-mode:luminance`, both honour a
per-layer `luminance, alpha` list, and both honour `mask-composite:intersect`.** The `@supports`
guard was not blind. It was guarding a door that was never the one being forced.

**What actually failed is a fetch.** The reverted commit was checked out into its own tree and
opened for real, both engines, both protocols. Over `http://` all four mask files load and the
strip draws. Over `file://` **all four requests fail, in Chromium and in WebKit alike**, and the
screenshot of WebKit reading it from disk is the product owner's screenshot pixel for pixel. A
mask image is a CORS-enabled fetch and a background image is not, so on a page opened from disk,
where every file is its own opaque origin, the mask is blocked. Proven on a stand where the SAME
FILE stands twice in one document: as `mask-image` the request fails and nothing paints, as
`background-image` it loads and draws. **And the reason the failure looked like a rectangle rather
than like nothing is the two-layer mask**: the drawing died and the gradient beneath it survived, so
`intersect` had one opaque layer left to intersect with and it painted a flat brass fade over 46 per
cent of every tile.

**This is the trap that made `assets/icons.js` a script instead of an `.svg`, four days ago, in this
repository, written down in `STRUCTURE.md`.** An external `<use>` is a cross-document reference and a
disk page drew 0 of 34 glyphs. Same origin rule, second victim, and it was not recognised because
the first one was filed under icons. **It has a third victim standing today and the second engine is
what found it**: over `file://` WebKit loads neither DM Sans nor Space Grotesk, only the mono face,
which resolves through the one `local()` in `fonts.css`. Chromium loads all of them from disk and
WebKit does not, so the whole product read from disk in Safari is set in a fallback face.
`docs/backlog.md` 147.

**So the drawings are inlined.** `components/trust-art.css` holds four `--trust-art-*` custom
properties, each a `data:` URI, and `trustbar.css`, `card.css` and `seo-plate.css` reach the drawing
through them. A `data:` URI is not a fetch, so it cannot be blocked, cannot 404 and cannot arrive
late: the mechanism cannot degrade to a rectangle because there is nothing left to fail. It is not a
component and it has no page in the kit; it is the drawings themselves, kept out of the three
stylesheets so that a stylesheet a person reads stays one.

**THE SECOND FINDING IS THE ONE THAT WOULD HAVE SHIPPED, AND IT WAS CAUGHT BY VARYING THE INPUT
RATHER THAN BY LOOKING AT THE PAGE.** The first build kept the fade as a second mask layer under
`mask-composite:intersect`. Measured against the shipped tree it looked plausible on both engines,
13 to 55 per cent of pixels differing at a mean under 6 of 255, which is inside the band this repo
had already accepted. It was wrong. **The bottom layer of a mask list has nothing beneath it, and
WebKit intersects it with the transparent black underneath, which empties the entire mask**: the
decorations were ABSENT on WebKit, and the reading that looked like an approximation was the
difference between the shipped decoration and no decoration at all. What exposed it was rendering
the mask at q20 and at q82 and diffing those two against each other: **Chromium moved 10.57 per cent
of its pixels and WebKit moved 0.00**, four times the data through the same pipe with a bit-identical
result. **A reading that does not move when the input moves is not a reading of the page**, which is
the same rule as the one about a number that moves when nothing moved, standing on its other foot.
Both engines are defensible here, so the answer was not to pick one: a drawing needs ONE mask layer,
and the fade moved out of the mask and into the paint, which is a gradient of `--color-trust` now
instead of a flat fill. No compositing operator anywhere. Both engines identical after.

**The quality was chosen by measurement and the measurement said the knob does not matter.** The
composite was compared against the shipped tree at q20, q35, q50 and q82, two engines, two widths,
three placements, control 0.00 per cent on all twelve readings each time. **The mean error moves from
1.06 to 1.01 of 255 across that entire range.** The difference between a mask and the picture it
replaces is the colour variation a flat brass cannot carry, and the codec is nowhere near it, so
paying four times the bytes for 0.05 of 255 would have been paying for the wrong thing. q20 it is:
worst single channel delta 11 to 68 of 255, and over `file://` on both engines the same numbers with
a control of 0.00.

**What it costs and what it saves.** The three footer tiles go from **346,492 bytes to 87,558**, and
the fourth drawing, which used to load on 23 screens, joins them for 26,184 because all four now
ship together. As base64 in the stylesheet that is **153,439 bytes on every screen**, against 346,492
on 105 screens and 488,842 on the feed: **a 55.7 per cent cut on the median screen and 68.6 on the
heaviest**. `assets/` goes from 1,474,119 bytes to **1,193,741**, because `trust-source.webp` and
`trust-column-full.webp` are asked for by nothing now and moved to `visuals/masters/` beside the
originals they came from.

**Two placements of these drawings are deliberately left as pictures**, and they are the reason
`trust-column.webp` and `trust-globe.webp` stay in `assets/`: `.ht-art` on `event-feed.html` and on
`ui-kit/feed.html` is an `<img>` in the markup at `opacity:.6`, the largest and most visible of the
four placements, and converting it means editing two documents rather than one stylesheet. It is a
row, not an oversight. **208,464 bytes on one product screen instead of on 105 is already the whole
shape of the win.**

**AND THE FULL SWEEP FOUND A DEFECT THAT HAD BEEN STANDING SINCE BEFORE ANY OF THIS, ON THE TWO
PAGES NOBODY WOULD HAVE LOOKED AT.** All 163 documents were re-rendered on both engines at 390 and
1280 against the pre-change tree, control 0.00 on every reading, **0 size mismatches outside the
three kit pages whose prose this change rewrote**. Over the 106 painted documents the worst single
channel delta is **41 of 255 in Chromium and 85 in WebKit**, the most any page moves is 6.24 per cent
of its pixels, and every mean is under 0.32. The outlier is 181, and it is on `ui-kit/card.html`
and `ui-kit/profile.html`: the gallery card's little brass arrow, which is `.gallery .card::after`
reusing the decoration's pseudo-element and resetting `background` but not `mask-image`. **It has
been wearing the decoration's mask ever since the decoration had one.** While that mask was a
left-to-right gradient the glyph was merely faded on one side and nobody read it as anything; the
moment the mask carried a drawing it went pale, 63 pixels of it. `mask-image:none` fixes both, and
the pixels that still differ afterwards are the arrow no longer being partially erased. **A
pseudo-element reused for a second purpose has to reset every channel the first purpose wrote, and
the mask is a channel.** Two kit pages caught it and 106 product screens did not.

**And the weight, which is what the question that started all this was about.** Every response body
on all 106 documents in `ui-visual/`, at 1280, before and after: the **median screen goes from
1,211,758 bytes to 1,020,959**, the mean from 1,256,081 to 1,041,480, and the heaviest, the feed,
from 1,589,778 to 1,466,943. **The image payload of the mean screen goes from 387,427 bytes to
15,283**, a 96 per cent cut, and most screens now load no image at all. The stylesheet grows by
157,543 on every screen, which is the honest half of the trade and is why the median moves by 15.7
per cent rather than by the 55.7 the images alone would suggest.

**The instrument, since it is now part of the record.** `playwright@1.62.0` is installed globally and
resolves at `/opt/homebrew/lib/node_modules/playwright`; the browsers were always global, in
`~/Library/Caches/ms-playwright/`, which is why adding WebKit added nothing to any project. **One
engine is one reading**, and every sweep in this repository until today was one engine reading a
product that is delivered from disk.

## 2026-08-13, later still - There was no bolder plus in the design system, there was a catalogue drawing the same plus at 3.18 times life size

The product owner pointed at `ui-kit/icons.html`, where the plus is a fat confident mark, and asked
why the header does not simply use it. **There is no second drawing.** It is the same path,
`M12 5v14M5 12h14`, now the same symbol. The catalogue draws its specimens in cells of 70, 94 and
262px with `vector-effect:none`, so the stroke scales with the box and a mark declared at 1.6 units
renders **4.67px there against 1.65px in the header**. Put the two at 22px side by side and they are
the same mark, and the product's is 12% heavier in PROPORTION, 7.5% of its box against 6.67%. **The
catalogue's look does not exist at 22px**: in that proportion the stroke would be 1.47px, thinner
than what ships. A reader inferred a drawing from a magnification, which is a property of the page
and not a mistake by the reader, so the page now says its own scale out loud.

**AND THE THING BEHIND THE QUESTION WAS REAL, SO IT IS FIXED.** `.bal-add` is the only control in
this product standing on a SOLID brass ground. Its mark is not a mark beside a word, it IS the
button, and a 1.65px stroke on a filled disc reads as unfinished between the Solar mass of the swap
and the bookmark either side of it. The system's rule, "a movement is a line", was written for a
mark on a transparent ground next to a label, and this placement is not that. So the deposit control
takes `#i-plus-b`, a filled plus of two rounded rects, **on the same optical grid as the line it
replaces**: paint 16.2 x 16.2 and field 3.9, the numbers this page audits, so only the WEIGHT
differs, 2.6 units against 1.8. **The exception is a NAME and not a stroke override in a component**,
which is the same shape as the `#i-` / `#l-` split itself.

**THE DECISION WAS TAKEN ON A NUMBER THAT WAS WRONG, AND THE CORRECTION MAKES IT BIGGER RATHER THAN
SMALLER.** It was offered as "filled on this control, line on the other 84", and there are no other
84: **all 85 plus marks in the product stand on `.bal-add`**. So the product's plus is filled, full
stop, and `#l-plus` became a symbol nothing references. It is deleted rather than kept waiting: a
`<use>` that finds nothing fails without a word, which is the hazard the head of `assets/icons.js`
names, and this repository has twice deleted a face nothing wore. The sprite is 35 symbols, 30
filled and 5 line.

**Measured: 78 of the 119 documents change and 77 of them carry `.bal-add`.** The 78th is
`ui-kit/icons.html`, whose prose changed in the same pass. Nothing else in the two painted trees
moved. Whole-tree sweep after: 1,475 readings over 295 documents at five widths, 0 page or console
errors, 0 responses at 400 or above.

---

## 2026-08-13, later - The plus was never in the icon file, because the rule that reads the icon file said a mark from it is a filled mark

Reported by the product owner, looking at the header: the plus does not come from the kit. **It does
not, and it never did.** `assets/icons.js` held 29 Solar filled symbols and no cross, no chevron, no
plus, no tick, no arrow and no hamburger, so those six stood as hand-written `<path>` elements in the
markup of **119 documents, 983 placements**, four of the seven marks in the product header among
them.

**FIRST, WHAT WAS NOT WRONG, because the report was that it had CHANGED.** It had not. A worktree at
`a9edf6a`, the commit this session started from, was served beside the current tree on a second
port: the `.bal-add` screenshot at ratio 3 is **byte-identical**, and across **85 placements** in
`ui-visual/` and `ui-kit/` the computed reading is one single value in both trees, 32x32 button,
22x22 svg, stroke 1.65px, `non-scaling-stroke`, brass gradient ground. The product and the kit's own
`header.html` and `iconbtn.html` agree exactly. **What the eye had caught was true and older than
the session**: in a row of four filled sprite glyphs the plus is the only stroked mark and the only
inverted one, and it is not in the file the other four come from.

**WHY IT COULD NOT BE, AND IT IS ONE DECLARATION.** `components/base.css` carried
`svg.ic:has(use){fill:currentColor!important;stroke:none!important}`, which says "a mark that comes
from the one file is a FILLED mark". That was true only because the file held nothing else, and it
was a floor with an `!important`, so a two-stroke drawing arriving through it gets no area and no
stroke and **paints nothing**. The rule that made the sprite safe is the rule that kept half the
marks out of it. It asks for `#i-` now, and the line family is `#l-`, so **a family is a property of
the GLYPH and is carried by its name** rather than by a class in a document, which is the same
argument backlog 133 used against a class per icon rung: a class in the markup is a decision taken
in the one place the system cannot see.

**`vector-effect` IS AN ATTRIBUTE IN THE SYMBOL AND NOT A RULE, and that is the one thing that had
to be got right.** It is not an inherited property, and CSS from the outer document does not reach
into a `<use>` shadow tree, so `.ic *{vector-effect:non-scaling-stroke}` cannot touch a symbol's
paths. Without the attribute the stroke scales with the box and a 22px mark in a 24 viewBox renders
**1.51 instead of the 1.65 the system declares**. Everything else, the fill, the stroke, the width
and the caps, IS inherited and arrives from `.ic` exactly as it did when the paths were written out
by hand. Proved on one placement before the sweep ran: same `getBBox`, **pixel-identical at ratio
4**.

**THE STAND STOPPED THE SWEEP ONCE, AND IT WAS RIGHT TO.** Two cross drawings stand in this
repository, `M6 6l12 12M18 6L6 18` on 348 placements and `M5 5l14 14M19 5L5 19` on 4, the second 17%
larger across the same box, and the pass unified them as drift. `ui-kit/icons.html` had already ruled
on exactly that pair: **the second is the X brand mark of the footer social row and it stays a brand
mark.** Backlog 144 cut that row, so it has 0 product placements and 4 on the stand, which are now
the only copies of it anywhere. They are written out by hand on purpose and the page says why.
**Two drawings that look alike are not evidence of drift, and the page that already decided is the
place to look before unifying anything.** The pixel diff is what surfaced it: 236 of 238 identical
and the two that moved were that page.

**IT BUYS ONE SOURCE AND NOT BYTES, and the number is written down rather than dressed up.** The
markup lost 4,947 bytes and the sprite gained 2,334, a net **2,613 over 163 documents**, because
`<use href="#l-chevron-down"/>` is longer than the chevron it replaces. What it buys is that each of
these six drawings now has one place to be wrong in, which is the whole reason the file exists: the
note at its head records `i-bookmark-b` having been two different drawings, the product's on 111
documents and an older one on 3 kit pages, invisible because every copy is internally consistent.

**PROOF: 238 full-page screenshots over the 119 documents that carry these marks, at 1280 and 390,
ratio 2, animation frozen and the cold pass thrown away. 0 differing of 238, against a control of 0
of 238 taken the same way before anything was edited.** Then the whole-tree sweep: 1,475 readings
over 295 documents at five widths, 0 page or console errors, 0 responses at 400 or above.

**WHAT IS LEFT, NAMED RATHER THAN IMPLIED.** Two families are still hand-written. The **16 line
specimens on `ui-kit/icons.html`** are the last copies of those six drawings, and they stay because
that page draws its specimens at 70, 94 and 262px with `vector-effect:none`, so a `<use>` there would
render the product's 1.65px hairline instead of a proportional stroke: **that is a decision about how
a catalogue shows a mark**, and it is written into the page rather than taken quietly. The **three
brand logos**, `prov-x`, `prov-google` and `prov-apple`, stand at 111, 111 and 109 placements as raw
paths; they are filled, so they need no new mechanism at all and would drop straight into `#i-`.
Neither is in this pass because neither is what was reported.

---

## 2026-08-13, one hour later - The luminance mask painted a brass rectangle in the browser the product is actually read in, and `@supports` is blind to exactly that failure

**Rolled back whole**, the same hour it shipped. `assets/trust-*-mask.webp` deleted, the four
original `trust-*.webp` restored, and the mask blocks in `components/trustbar.css`, `card.css`,
`seo-plate.css` and `hero.css` reverted with the `<img class="ht-art">` markup that went with them.
Backlog **139 and 140 are open again**. What is NOT rolled back is the `.hf-photo` box fix, which
shares a row with none of this and was never in question.

**WHAT BROKE.** A mask image is read as ALPHA unless `mask-mode` says otherwise, and these files
are opaque by design, so a browser that treats the mask as alpha paints the entire mask box: a flat
brass rectangle over 46 per cent of every footer tile, over the corner of every feed card, and over
the whole seo plate, shaped only by the fade gradient that was the second mask layer. That is
exactly the failure the entry above says the `@supports` guard was written to prevent, and
**the guard could not see it**, because `@supports (mask-mode: luminance)` asks whether the property
PARSES and not whether the mode is HONOURED, and there is a browser where those two answers differ.

**AND THE INSTRUMENT AGREED WITH THE BROKEN PAGE THAT NOTHING WAS WRONG.** Chromium computed
`mask-mode: luminance, alpha` and `mask-composite: intersect` on the real elements over `http://`
and over `file://` alike, the composite diff came back with the numbers the decision was taken on,
and the screenshots I read were Chromium's. **A rendering engine is part of the instrument, and one
engine is one reading.** This repository already wrote that sentence once, on 2026-08-09, when an
external `<use>` drew 0 of 34 glyphs from disk and the fix was to stop being clever about how the
asset is reached. It did not occur to me to apply it to a mask.

**WHAT SURVIVES, AND IT IS THE WHOLE POINT OF WRITING THIS DOWN.** The measurement is not wrong and
is now in row 140 rather than in a deleted branch: all five `visuals/masters/trust-*.png` are 100
per cent opaque brass line art on black, the shipped alpha plane was MANUFACTURED from that
luminance drawing, and the two agree at 23.8 against 22.3. That is why no encoder reaches those
bytes, and it is a fact about the artwork rather than about CSS. **The row now asks for a mechanism
rather than for a measurement**, and names the condition the next attempt has to meet: degrade to
NOTHING rather than to a rectangle. Three candidates are written into it, and the first thing any of
them needs is a second engine in the harness.

**THE COST OF THE ROLLBACK, stated rather than smoothed over.** `assets/` is 1,339,606 bytes and not
1,107,186; the trust strip is 488,842 bytes on 105 screens again; the seo plate upscales its
decoration by 1.21 to 1.25 again; and the hero tiles hold the second encoding of a drawing the
footer already loads. Five open rows rather than three. **The featured hero keeps its fix** and is
still showing its photograph for the first time.

---

## 2026-08-13 - The alpha plane held a drawing that had been made in luminance, and the featured hero had been showing empty sky since the day it landed

Backlog 138, 139, 140, 117, 128, 137 and 77 closed, 146 opened. Nine open rows become three, and the two that remain belong to Stage 11, which has not run. **Proof over all three product trees plus the thirteen course documents: 1,475 readings over 295 documents at five widths, 0 page or console errors, 0 responses at 400 or above, and 0 horizontal scroll in the 1,335 readings that are product.** The five that are not are row 146.

**140, AND IT IS A RE-EXPORT AFTER ALL, WHICH THE ROW HAD RULED OUT IN ITS OWN TEXT.** The trust decorations were the heaviest thing left on 105 screens, 488,842 bytes, and the row had established why no encoder would reach them: the drawing lives in the ALPHA channel, 65 to 73 per cent of each file, and WebP codes alpha with a lossless coder. It named two ways out, a flat colour behind a mask and the unused vectors, and called both **re-authoring rather than re-exporting**, which is a design decision and therefore a row rather than a fix. **The masters say the conversion had already happened, in the other direction.** All five `visuals/masters/trust-*.png` are 1254x1254 and **100 per cent opaque, 0 pixels below alpha 255**: brass line art on black, which is a LUMINANCE drawing. The alpha plane was manufactured from it on the way to the shipped file, and the two agree where it counts, mean master luminance 23.8 against mean shipped alpha 22.3. So this is not a new authoring of anything; it is the drawing going back into the plane it was drawn in, where a DCT codec can reach it. `mask-image` with `mask-mode:luminance` over a flat `--color-trust`, and **488,842 bytes become 256,422**.

**WHAT IT COSTS, MEASURED BEFORE IT WAS CHOSEN AND NOT AFTER.** The colour plane carried one thing the alpha did not, the drawing's internal shading, and a flat brass loses it. Composited and diffed at ratio 2 over the three placements, two widths and two themes, with the instrument's control proved 0 of 12 first: **9 to 33 per cent of pixels differ, mean 2.5 to 6.7 of 255, maximum 11 to 42.** The error is `coverage x (was - is)` and the ground cancels, so it is the same in the Vault and in daylight, which is the property that made this variant the one to offer. **Two cheaper-looking variants were built and rejected on their numbers.** Splitting each file into an opaque colour plane plus a mask reproduces the composite exactly and costs MORE than today, 95,438 against 90,158 for one of them, because the un-premultiplied colour at low alpha is noise and noise is expensive to code. Folding the shading into the mask as `alpha x Y(colour)/Y(brass)` is smaller still and better in the dark, mean 2.5 against 6.4, and worse in daylight, 8.6 against 6.3, because that fold assumes a black ground and the light theme has none.

**AND THE SAME DRAWING WAS SHIPPING TWICE.** `trust-column` and `trust-globe` stand in the footer strip as backgrounds and again inside two hero tiles as `<img class="ht-art">`, and while the second pair were `<img src>` they held the old alpha-plane files alive at 208,464 bytes for one screen. The element stays and is a `<span>` now, because what it carries is a colour and a coverage rather than a picture, and pointed at the two masks the footer has already fetched **the hero tiles cost nothing at all**.

**THE FIRST `@supports` IN THIS SYSTEM, and it is there for a failure that would be loud.** A mask image is read as ALPHA unless `mask-mode` says otherwise, and these files are opaque, so a browser that takes the mask and drops the mode paints a flat brass rectangle over 46 per cent of every tile and over the corner of every card. Nothing is the correct degradation for a decoration and a rectangle is not, so the colour and the mask stand together inside the query or neither stands.

**139, AND ITS FIRST HALF WAS A BOX DEFECT WEARING A BYTE DEFECT'S CLOTHES.** The row read `hero-capitol.webp` at ratio 1, 1400x788 drawn at 1400x788 CSS px, and filed it as a soft photograph. The reading was right and the cause was not: **an absolutely positioned REPLACED element with `left` and `right` both given and a width of `auto` does not stretch.** It takes its intrinsic width, which is the `width="1400" height="788"` on the markup, and the over-constrained `right` is dropped, so the photograph drew at its full size inside an `.hf-info` that is 360x301 at 390 and 301x368 at 1280, and `overflow:clip` cut the rest. **The featured hero of this product has been showing the top-left 9.8 per cent of a frame composed to be seen whole, which is empty sky, since 2026-07-23.** `object-fit:cover` and `object-position:center top` were inert the entire time, and `.hf-veil` on the identical inset stretched correctly because a `<div>` is not replaced. Two lengths fix it. Sized to its box the same file scales to between 0.381 and 0.518 over seven widths and the three pages that carry it, so it is exact at ratio 2, worst case 1.04, and 1.14 to 1.56 short at ratio 3: roughly twice as sharp as it was, and whole. The second half was exactly as filed, `.seo-brand::after` asking 629x726 of a 520x600 file at every width from 760 up, and it closed inside 140's edit, because the mask that replaced that file is **640x738 and still lighter than the 520 was**. One file, two placements pulling opposite ways, and the card asks 168x194 of it and needed nothing.

**138, A MOVE THAT MAKES THE README TRUE, AND A CENSUS THAT FOUND THREE MORE.** The five 1254x1254 masters and the two unused SVGs sat in `assets/`, the folder the screens load, referenced by nothing outside the row that filed them, while `visuals/README.md` declared that masters live in `visuals/masters/`. They are there now, with the SVGs named in the README as the refused vector alternative rather than as masters of anything. `grey-ed.png` at the repository root was **deleted rather than moved**: 405x3109 is a full-page screenshot of the grey event detail, committed by accident in `e5d60c0`, and a screenshot from a sweep is a throwaway like the sweep that made it. **`assets/` goes from 9,690,253 bytes to 1,107,186.** The census that proved the eight also found three the row had never counted: `event-sports.jpg`, `spare-newspapers.jpg` and `spare-reader.jpg`, 486,949 bytes, reached ONLY from `concept/old/` and `ui-visual/old/`. They stay, because moving them breaks eleven references in documents kept to be read, and they are written into the row so the next reader knows what is there.

**117, THE ROADMAP IS ONE REGISTRY, AND THE KIT HAD WRITTEN THE ARGUMENT A WEEK EARLIER.** The course outline stood as hand-written markup in 28 documents across five folders, so the edit that turned one planned row into a link cost 27 repetitions at two path depths and missed the 28th, which had silently stood four rows behind since stage 09. `assets/_roadmap.js` holds the route once. **A page declares neither its name nor its depth**, because the active row is computed from the path and the prefix from the script's own `src`, and those are the two things a hand-copied panel gets wrong. What a page still declares is its own section anchors, which are headings of that document and are not route. **890 lines of markup out, 69 in, and the rendered panel is identical on 28 of 28**, against a control that gave 0 differing pages when nothing had changed.

**AND THE OUTLINE TURNED OUT TO BE A TREE THAT NOBODY HAD WRITTEN DOWN.** A stage you are not inside is one row; a stage you are inside opens, and it opens in one of three shapes the 28 copies had settled between them: the label becomes a divider and its pages become rows (User Research), the same with the pages in named groups of their own and the stage's own label staying quiet (Information Architecture), or the stage stays a link and its pages become sub-links (Wireframe Annotations). The registry names all three. **The active stage is the DEEPEST directory that matches**, because `ia/annotations/` lives inside `ia/` and is its own stage, and a shortest-match rule would have opened Information Architecture on all fifteen annotation pages.

**IT NEARLY BROKE THIRTEEN PAGES IN SILENCE, AND THE INSTRUMENT CAUGHT IT.** Thirteen of the 28 carry an inline scrollspy at the foot of the body that takes `[...document.querySelectorAll('.sidebar-sub-link')]` ONCE, at parse time. A panel written on `DOMContentLoaded` hands that spy a list of elements no longer in the document, and the section highlight dies with nothing in the console to say so. The first snapshot after the change showed it: 27 pages identical and one page's first sub-link no longer lighting. It renders at parse time now, directly under the `<aside>` it fills. **Scrollspy alive on 13 of 13 after, checked by scrolling each page to four depths and requiring at least two different rows to light.**

**128 CLOSES ON THE FIRST OF THE TWO ANSWERS IT NAMED FOR ITSELF: the section headings do not count anything any more.** They drifted a fourth time in the very pass that closed the row, and in the shape of all four: seven of the eight were right and *Component boundaries* said 6 closed over 10 closed rows, **the same section that was wrong the time before**. A count in a heading is not a fact about the rows, it is a copy of one, and the answer that was tried twice, moving the copy into a paragraph, moved WHERE it is written twice rather than THAT it is. One number is left in that file, **Open**, at the top, and it is the only one that has never drifted because it is the one every pass has to edit in order to do its work.

**137 CLOSES AS A BOUNDARY RATHER THAN AS A CONTROL.** 44x44 governs CONTROLS; a navigation list is held by WCAG 2.5.8 AA. All three footer link families pass the binding criterion and all three miss 44, and the row was right that the distance between the two numbers was a stance nobody had written down. It is in `DESIGN.md` now with its reason: 44 is the size of a thing you press to make something happen, a footer column is a table of contents you read and occasionally follow, and putting eleven links on a 44 floor adds 330px to a phone footer to buy nothing any criterion asks for.

**77 IS KEPT, SCOPED, AND DECIDED ON THE DAY ITS PHOTOGRAPH WAS FOUND NOT TO BE DRAWING.** The featured slot is MVP; it stands on the Trending feed and nowhere else; and what fills it is the highest 24-hour volume among open markets, a figure the product already holds, so MVP needs no editorial queue and no admin screen and the slot can never feature a resolved event. It adds no node to the map and no state to the feed, because **the absent slot IS the feed's empty state**. `wireframes/_conventions.md` gains S7 and `ia/docs/sitemap.md` gains the paragraph; the row had been open since 2026-08-03 because the block had arrived by being BUILT, back-ported into the grey tree so a gate would pass. **The decision was taken with the fact that nobody had noticed its photograph in three weeks, rather than against it.**

**146 IS WHAT THE SWEEP FOUND ONCE IT WALKED DOCUMENTS THAT NOTHING HAD EVER GOVERNED.** The product trees are clean, 1,335 readings over 267 documents at five widths with 0 horizontal scroll. The thirteen course documents that carry the roadmap give **5 readings that scroll**, four of them at 320 and one at 390, and none of it is the panel or the system: each page carries its own inline stylesheet and what overflows is content, a 643px table inside a 390px viewport on `jtbd.html` above all. They are review artefacts rather than product, which is why no rule here has ever reached them, and that is the finding: **a document nobody declared to be in scope is a document every measurement silently excludes.**

---

## 2026-08-13 - Three rows that were product and IA decisions, taken, and one of them orphaned a whole icon face

Backlog 142, 143 and 144. All three were measured to a standstill and then waited on a choice that is not a measurement, which is what a row is for. **267 documents in all three trees at four widths after: 0 horizontal scroll, 0 console or page errors.**

**142, THE BAND THAT COULD NOT OPEN: the markup is out of the 48 that could not open it.** The sticky strip is revealed by an observer that watches `.feed-inner > .cat-nav` and returns early where there is none, so on 48 painted screens and 30 grey twins the band could not open at any width and carried **240 anchors in the paint and 150 in the grey** that no eye saw and no keyboard reached. The alternative, another anchor for the observer, would put a category route on the wallet, the deposit, the profile and the error screens, **which is an addition to the navigation model rather than a repair**, and it stays refused until `ia/docs/sitemap.md` asks for it. The 57 with a main band keep the strip, and **it opens on 57 of 57**, measured by scrolling each to 1200px at 390.

**143, THE SIDE IS IN THE URL.** Both halves of every pair sent the reader to the same address, **126 pairs of 126**, so a card offered three tab stops to one destination, and once backlog 103 had made each control say which side it takes, the accessible name promised a distinction the link did not make. It is `?side=yes` and `?side=no` now: **212 anchors in `ui-visual/`, 212 in `wireframes/` and 72 in `ui-kit/`**, and 0 pairs left where both halves share a destination. **The reason it is an IA line and not a markup one is what a URL buys**: a pre-selection that lives in the address survives a share, a bookmark and a back button, and one that lives in a click does not.

**144, THE SOCIAL MARKS ARE OUT UNTIL THE ACCOUNTS EXIST.** 525 anchors in the paint and 435 in the grey, five per screen, pointing at accounts that do not exist and standing directly under the footer trust strip. They were a third kind of placeholder that neither of the rules settling this footer reached: row 27 cut a link the map REFUSES, row 28 kept a link the map registers with no screen yet, **and a social account can never become an internal route, so it cannot be waiting for one**. `href="#"` in `ui-visual/` goes from 1,059 to 534.

**AND TAKING THEM OUT ORPHANED AN ENTIRE ICON FACE, WHICH IS THE CONSEQUENCE WORTH WRITING DOWN.** `.icon-btn-lift` had 525 placements and has **0 in the product and 9 on the stand**. It is kept rather than deleted, and the difference from `account.css`, which was deleted for having no face left, is that this is a face whose placements are coming back on a date somebody chooses. **It also moved a number this repository had published four hours earlier**: backlog 120's "568 of 576 already agreed at 20 per cent" counted `.icon-btn-lift:hover` as 525 of the 568, so the standing population is 43 of 57 and the majority is `.cmt-av` alone. The decision does not move with it, because it never rested on the majority: three of its five distinctions do not exist at all. **A measurement is true as of its own hour, and this file is where that gets said rather than quietly restated.**

## 2026-08-13 - The grey tree had never once put its rail beside the content, and three of these five rows had been closed by an edit and left open

Backlog 126, 127, 141, 113 and 45. **Three of the five were already done and the file did not know**, which is item 74 arriving for the sixth and seventh time and is worth more than the fixes: a row is closed by an EDIT and struck by a HAND, and the hand is the half that gets forgotten.

**113 IS THE ONE THAT WAS REAL, AND ITS OWN STYLESHEET IS WHAT DECIDED IT.** `<!-- /cat-main --><!-- /cat-layout -->` stood in **76 grey files with no opening tag above it**, and the row said it could not choose between its two answers by guessing: either the tree lost the wrapper in a port, or the paint invented an arrangement the structure never asked for, in which case 77 painted screens are the ones that are wrong. **The proof was in the grey files themselves**: 92 of them style `.cat-main { flex: 1 }` and, at the RAIL rung, `.subcat { flex: 0 0 210px }`, and **both need a flex parent that was not there**. So the sub-category rail has never once stood beside the content in this tree at any width, on any screen: two flex children of a block box, stacked. A closing comment with no opening tag is evidence; a stylesheet written against the missing element is proof. Both tags are back in all 76, **33 of them around a rail**, with the `.cat-layout` rule added to the 92 that already style its children. Measured after: 104 grey files at six widths, **0 horizontal scroll, 0 page errors, and 0 files where a rail that renders is not beside the content**.

**126 AND 127 WERE BOTH CLOSED BY COMMIT `ea508d0` ON 2026-08-12 AND NEITHER WAS STRUCK.** `_nav.js` lists all five reports and carries a comment recording that the fifth was unreachable for a day; the fifteen colour roles the row named have swatches on `colour.html`, added in the same commit; and the three leftover classes it also named, `tk-brand`, `tk-pair` and `tk-plain`, were deleted the same day and survive only in the comments that record their deletion. Re-measured in a browser over all 57 kit pages: **294 `.tk-*` classes declared and 294 worn, 0 by nothing.** **What the re-measurement then found is bigger than the row and is a different claim**: `colour.html` draws **66 of the 128 product roles**, and the 62 it does not are bevels, gradient stops, shadows, veils, masks, grain textures and two opacities, which are not flat colours and would teach the wrong thing as a square. Two of the 62 were created the same day by backlog 120 and are flat grounds, so they are drawn now. The rest is a row rather than a sweep.

**141 ASKED FOR A RE-MEASUREMENT AND THE RE-MEASUREMENT IS ONE COMMAND.** The two font paths are the second literal in this repository repeated across a whole tree, after the grey harness width, and the failure mode is silent in the same way: rename a face and the CSS follows while 163 preloads point at a file that is gone, the page still renders, and a 404 preload costs one request and one warning nobody reads. There is no build step to catch it, on purpose. Resolved every `href` on every `<link rel="preload">` in both trees against the file system: **two distinct paths, 163 documents each, 326 references, 0 missing.** The check and its date are in `components/fonts.css`, which is the file a rename would go through.

**45 HAD ALREADY LOST SIX OF ITS NINE DECLARATIONS ON 2026-08-10** to the pass that moved `tabs.css` off document-unique ids and onto `:nth-of-type`, and the row stayed open for three days. What is left is **two SVG paint references in `hero.css` and four `#rm*` in the harness that the row itself calls correct**, and **the fix the row proposed for the two is not available**: an SVG `fill` takes a paint server, a paint server is an element referenced by id, and `linear-gradient()` is not a legal value there. So the constraint is declared in the file instead: a document may hold one hero chart. Measured over **267 documents in all three trees: 0 with any duplicate id.**

## 2026-08-13 - The rungs follow the reader now, the grey harness derives, and the two rules a container query would answer differently are the two that belong to the window most

Backlog 124, 119, 136, 135 and 145, closed in one pass because all five are the width axis. **The load-bearing measurement is 6,300 readings over all 105 screens at twenty widths and three browser default font sizes: 0 horizontal scroll, 0 readings with anything other than exactly one navigation carrier, and 0 differing readings of 2,100 at the default against the tree before the change.**

**135, THE RUNGS, IS THE ONE THAT MATTERS AND ITS FIRST INSTRUMENT MEASURED NOTHING.** The stage kept them in px on a stated ground: a rung in `rem` while every word is a fixed size switches the layout at a different window width and changes nothing a reader can see. That was true and it was an argument about the TYPE, and the type moved on 2026-08-12, so the argument was spent the same hour and the rungs were held by nothing except that nobody had decided. They are **40rem, 47.5rem and 56.25rem** now, with the three one-offs at 35, 38.75 and 61.25rem, and **the narrow side written exactly rather than rounded**, 39.99875rem and 47.49875rem, because the pair rule is what stops both sides of a rung matching at once and this repository has already paid for that with 73 of 106 documents in horizontal scroll for a day. **The 1140 harness stays in px** with the review toggle beside it: a docked panel is 220 physical pixels of chrome whatever the reader's font is. What it buys, measured: at a 24px browser default the desk arrives at **960** instead of 640 and the rail at 1350, so a reader whose words are half as wide again keeps the one-column layout until the window is half as wide again. **The first sweep set `html{font-size:24px}` and reported the rungs not moving at all**, the bottom bar still going at 640 on all 105 screens at every root, which is correct CSS and a useless measurement: **a length in a media query resolves against the INITIAL font size and ignores every declaration on the root element**, including the one the sweep had just written. A reader does not set `html{font-size}`, they set the browser default, and only CDP `Page.setFontSizes` moves both. The same injection was the right instrument for item 115 and the wrong one here, and the two agree at the default, 0 of 2,100, which is what says they are one instrument and not two opinions. The probe was then shown a deliberate 2,000px box on five screens and saw it 5 of 5.

**145 WAS OPENED BY 129'S FIX AND CLOSES AS A REFUSAL, WITH NON-SEPARABILITY AS THE REASON TO KEEP THE WINDOW.** Forced into the inline layout at every width from 320 to 1600: **the outcome pair's two halves measure 46 and 42.7px at every container width from 251 to 628.** They are content-sized inline and the name absorbs the rest, so **the container tells you nothing about what the pair gets.** What the container decides is whether the NAME fits, and it clips at 251 and not at 271, so a container query would have to be keyed near 260 and would put the inline layout on every phone in the product, where the pair's halves are 42.7 against this rule's 268 and one of the two is under the 44px floor this project set itself. **The rule is not about the box, it is about the pointer, and a pointer is a screen fact.** So the test 129 settled on is necessary and not sufficient in BOTH directions: a separable rule may still belong to the window, and a non-separable one may belong to it more.

**119, THE GREY HARNESS, WAS THE ARITHMETIC AND NOT THE NUMBER.** 1140 is `900 + 220 + 20`, the RAIL rung plus the review sidebar plus its inset, which is why it is a harness and not an invention. The grey screen-tree rail is 250px, so the same derivation gives **1170**, and 1440 was 270px of window that no rung, no rail and no gutter asked for. Moved in all 104 grey files, **312 occurrences, three per file**, because a grey file writes the number in its media query, in its drawer script and in the sentence above it, which is also why a grey file cannot hold a token. **A harness width that does not derive is a preference wearing a harness's name.**

**136 SAID EVERY CANDIDATE FIX MOVES THE DEFAULT RENDERING, AND THE ONE THAT DOES NOT IS THE MECHANISM THE LADDER PUTS FIRST.** `repeat(3,1fr)` is `repeat(3,minmax(auto,1fr))`, so a track cannot shrink below its content, and the figure's min-content is **3.875em at every root**: three of them plus two gaps need 303px in a container of 224 at a 24px default, which is the 23px of horizontal scroll the row found on one screen of 105. `auto-fit` counts columns from a floor and not from content, so a 62px floor in an 888px container gives twelve. What the summary wants is as many of its three figures per row as fit and never more than three, and **with exactly three items a wrapping flex line is that**: `flex:1 1 0` makes them equal thirds when all three fit, and `min-width:min-content` is what makes the line wrap rather than overflow. **At a 16px default all eighteen figure widths are identical to the grid's, 320 included**, because free space distributed from a zero basis over three items with different minimums is what `minmax(auto,1fr)` computes.

**124 IS THE SMALLEST AND THE ONLY ONE WHOSE FIX NO SWEEP HERE CAN SEE.** `.device` is the shell all 106 painted screens stand in and it declared `min-height:100vh` while three other files wrote the `svh` argument down: on a mobile browser `vh` is the LARGEST viewport, the one with the URL bar retracted. It rendered acceptably and that is why it survived, because `min-height` only ever adds room, so the cost is not a clipped page but a page that can always be scrolled by the height of the retracting chrome. Both declarations are written, the fallback then the fix, and **headless Chromium has no retracting chrome, so this edit measures as zero on every instrument in this repository**: the thing it fixes cannot be read by the sweeps that guard it, which is why the argument is written in the file rather than left as a value.

## 2026-08-13 - Five rows inside `components/`, and three of the five asked for a fix that would have been wrong

Backlog 131, 133, 120, 132 and 114, closed in one pass because all five live in this folder and none of them touches a screen. **Every value change in the product is accounted for: 90 differing properties over 210 documents, against a control of 0 of 363,636.**

**131, THE DEAD ROLE, WAS EXACTLY WHAT IT SAID.** `--text-icon-strong` was drawn for the notification bell, which was the one FILLED mark in a row of stroked ones and was lifted a step so it did not read heavier than its neighbours. The row is filled now, so the exception went with its reason and the role stayed. **Zero readers in `components/`, `ui-visual/` and `wireframes/`**, and the only thing still drawing it was its own swatch on `colour.html`: a page showing a role that nothing wears. Deleted in both themes, with the swatch and its `.tk-c-*` class. **And the count beside it had drifted in both directions**: `colour.html` said 133 roles for dark and 93 for light, and the light block held **96** the day that sentence was written, so its section heading counted forty single-valued roles where there were thirty-seven and the three it invented were never in the table underneath. It is 134 and 97 now, read out of the source.

**133 ASKED FOR A CLASS PER ICON RUNG AND THE ANSWER IS THAT A CLASS WOULD BE THE DEFECT.** The row is right that `--icon-16` and `--icon-18` are reachable only by writing a width and a height: `base.css` gives `.ic` the 22 and `.ic-sm` the 12 and everything else is a placement sizing the mark itself. **That is the correct mechanism.** A class in the markup would put a SIZE in a document, and the size of a mark is a fact about where it stands, which is the same rule that says `container-type` is declared by whoever places a component. Counted: **13 rules resize a mark and 8 of them read the two rungs the row called unreachable**, and `.ic-sm` renders at 12 on 354 of 358 placements and at 18 and 22 on the other four, because `toast.css` resizes it. **What was actually wrong is one level up: three placements sized a mark off another ladder or off none at all** - `.nav-slot .ic` at `--size-20`, `.state-block .ic` at `--size-28` twice, and `.market-title .ic` at a raw `13px` on 9 placements, one pixel off a rung that already existed. The ladder is six rungs now, `--icon-20` and `--icon-28` are drawn on `geometry.html`, and the 13 reads `--icon-12`. **The instrument was wrong before the finding was, for the fourth pass running**: a sweep over 105 screens reported marks at 13, 28 and 40 and 362 placements off the ladder, and 40px is a 22px mark inside a padded tile, because it was reading `getBoundingClientRect()`. **A mark's size is its declared width and never the box around it.**

**120 WAS SIX EYEBALL DECISIONS AND THE MEASUREMENT SAYS THREE OF THE FIVE DISTINCTIONS DO NOT EXIST.** Ten brass `color-mix` declarations in seven files, two jobs: brass into `--bg-control` at 11, 15, 16, 20, 20 and 22, and brass into `--border-hairline` at 30, 30 and 42. Resolved in a browser in both themes: **15 and 16 are 0.0045 apart in oklab lightness**, the two 20s are the same number, and **the 42 edge and the 30 edge are 0.001 apart in DAYLIGHT**, because the light hairline is already close to brass in lightness, so the one value that reads as a deliberate emphasis is invisible on half the product. Counted by placement, **568 of 576 already agreed at 20 per cent**. It is one role per job now, `--bg-control-brass` and `--border-hairline-brass`, and it can be a role precisely because row 14's objection does not apply here: **all six blends end in the SAME base**, and what varied was only the amount. Declared in both theme blocks rather than once, because a theme here is an attribute on any element and a custom property holding a `var()` resolves against the element that declares it, so a single `:root` copy would bake the dark base into a light figure on the kit; verified across all 57 kit pages, 0 mismatches. **And the 11 per cent, the value furthest from every other, was reported as having no placement at all and has six**: `.gallery .card` sits inside the Past wins tab panel on two profile screens, and a sweep that walks a page as it loads sees the tab that is open. Same lesson as the shut `<dialog>` and the odds bar a script writes.

**132 ASKED FOR ONE RULE KEYED TO A FAMILY, AND THE FAMILY IS NOT A SELECTOR.** `base.css` shortens every duration under `prefers-reduced-motion`, which makes a movement instant without removing it, so five files each carried their own `:hover{transform:none}`. The obvious fix was censused before it was written: **the system holds 20 transform declarations and only 5 are movement.** Nine are rest geometry, two are a STATE that carries meaning rather than motion, and the rest are the harness drawer and two keyframes. **`*:hover{transform:none}` would flatten `.market-chevron` while the pointer is on it**, so an open market would point its chevron the wrong way for exactly as long as you looked at it; pseudo-elements survive that rule and `.market-chevron` is an element, which is the whole difference and is why the count had to come first. The floor is a value instead: every moving transform multiplies its distance by `--motion`, 1 normally and 0 under the query. Proved directly: `--motion` reads 0 under reduce and 1 without it, `translateY(calc(-3px * var(--motion)))` resolves to the identity matrix and to `-3` respectively, and **0 of 40,404 computed transforms moved in the product at the default.** Five blocks deleted, and one of the lines inside them was inert anyway: `card.css` re-declared `transition:box-shadow var(--dur-base)` under a global block that already writes `transition-duration:.01ms!important` on `*`.

**114 IS ANSWERED WITH A SENTENCE AND NOT A TOKEN, WHICH IS WHAT IT ASKED FOR.** The four sheet-body gaps are three, and reading the bodies rather than the rules shows what sets them: **8 for a stack of PARTS** (the deposit body, six children of four kinds), **12 for a stack of CONTROLS** (sign-in, three provider buttons and a fine line; the outcome body, a figure block and two actions), **16 for a stack of SECTIONS** (how-it-works, three `.hiw-sec` each carrying an icon, a label and a paragraph). The gap grows with the size of the thing on either side of it, which is the only rule a gap can honestly follow. It is written in `dialog.css` rather than tokenised because a token would say these are rungs any body may pick from, and they are not: a body has one of three shapes and the shape decides.

## 2026-08-13 - Container queries stay refused, the threshold was the wrong test, and the defect was the window and the container moving in opposite directions

Backlog 129. The row said the stage's own condition for revisiting `@container` had been met by 35 of 47 components, and it had. **The condition is necessary and was read as sufficient, and the measurement that decides the question is a different one.**

**35 OF 45 COMPONENTS FILL THEIR CONTAINER AND HAVE NO WIDTH BEHAVIOUR AT ALL**, which is the table this repository already keeps in `ui-kit/docs/inventory.md`. A component with no rule has no branch that can fire wrongly, so counting how many stand in slots of different widths counts a population that would not use a container query if it were handed one. The population that can misfire is the queries themselves. Taken from the comment-stripped source: **52 selectors inside 33 width queries - 14 are the page frame, the shell or the harness, where the window IS the subject; 2 set a positioning context, which has no width in it; 36 are a component in a slot.** The 25 of those that stand in the product on both sides of their own rung were read against their PARENT'S CONTENT BOX on all 105 screens at the rung and one pixel either side, and tested for the only thing that decides this: **does ANY container width divide the placements the way the rung does, in either direction.** **24 of 25 did.** For every one of them a container query resolves identically at every placement, which is exactly the sentence the stage wrote, and the count of 35 of 47 never touched it. **The two selectors whose containers genuinely disagree between placements, `.chip-nav` at 119 to 537 and `.filter-menu` at 314 to 611, are the two that set a positioning context.**

**OF THE THREE COMPONENTS THE ROW NAMED, ONE CARRIED THE CASE AND TWO DID NOT.** `navitem` has 995 placements and **no width rule at all**, so there is nothing for a query of either kind to get wrong. The rail separates: `.subcat`'s container reads 761 on one side of RAIL and 214 on the other. `card` carried it, and for none of the reasons the row gave.

**THE DEFECT WAS ONE TOKEN, AND IT WAS THE OPPOSITE OF WHAT WAS BEING LOOKED FOR.** Both page insets STEPPED at DESK 640: `--gutter` 14 to 40 and `--plate-inset` 16 to 28, **38px a side and 76px in total, spent at the pixel where the window grew by ONE.** The content column went 611 to 560 and the feed card 577 to 502, and the card did not reach 577 again until the window was 715. **Nine component rules are keyed to that rung and every one of them fires at the moment its own box gets smaller**: the bookmark pull in `card.css`, the outcome wrap in `options.css` and `yesno.css`, the four-column figures in `position.css` and three rules in `footer.css`. **A rule asking the window a question about a container needs no container query to expose it, only a reading one pixel either side of the rung.** Both insets ramp now, DESK 640 to DETAIL 760, and **the length of the ramp is derived rather than chosen**: 38px a side has to be spent at no more than half a pixel per pixel of window or the column still goes backwards, so it cannot be shorter than 76px, and 760 is the next rung on the ladder, so no width was added to the system. Below 640 and at 760 and above, **0 geometry readings of 18,660 differ**.

**AND `card`'s ONE QUERY WAS NEVER ABOUT THE WINDOW.** The bare icon button pulls its own invisible 44px target back by `(44 - 16) / 2 = 14px`; a card has **13px** from its content edge to its clip edge and is `overflow:clip`. So above the rung, where `card.css`'s rule switched off, **one pixel of a 44px target was cut off 84 cards at every width from 640 to 1600**, and below the rung this rule's 8px was hiding it. Measured on `event-feed.html`: the button's right edge is 603 against a card edge of 608 at 639, and was 610 against 609 at 640, unchanged at 900 and at 1440. The rule is unconditional now. **The answer to "container query or media query" was neither**, and the cost is that a desk card is 12px taller, its meta row going 25 to 37, which is the number a phone card has always had.

**PROOF.** All 105 screens at twelve widths: **boxes overflowing 247 to 163 at every width at and above 640**, which is what the tree already read below it; **controls cut by the card they stand in 84 to 0**, worst overhang 5px to 0; **horizontal scroll 0 before and after**. The instrument was proved first: the same tree measured twice gave **0 differing readings of 18,660**. Two width queries left the registry, 35 to 33, **and nothing replaced either**: a query that leaves with no replacement was answering a question its subject never asked.

**THE FIX MADE THE FIRST REAL CONTAINER-QUERY CASE THIS SYSTEM HAS EVER HAD, and that is the result nobody was going to guess.** Separability re-run after the ramp reads **22 of 25, not 25**: by taking the discontinuity out of the column at 640 it also took away the thing that let a container threshold stand in for the window there. `.opt-row` and `.yesno.compact` now sit in a container measuring 551 to 570 at 639 and 552 to 571 at 640, continuous through the rung, while the rule still flips the outcome pair from 268px a half to 46 and 42.5 across that one pixel. They are filed as **145** rather than converted, because declaring `container-type` changes what an element's width MEANS rather than what it measures, and that needs its own measurement. The third, `.icon-btn.icon-btn-tile` at the 560 one-off, was the single exception before the fix as well: its container is **92 on both sides**, so no threshold divides anything and the window is the honest owner.

## 2026-08-13 - Six zeros, two of them defects, and the one that looked like an orientation problem was a width

Backlog 125. The row banked six responsive concerns that were each **0 rather than a wrong number**, which is why none had ever been a finding. Measured one at a time, **two were defects and four were already answered**. `components/print.css` is written and `overflow-wrap` is on the page frame.

**(a) PRINT WAS A DEFECT AND THE ROW UNDERSTATED IT.** Rendered at A4, 794 x 1123, with the medium emulated as print: the sticky header printed at 794 x 59 and still `position:sticky`, the footer trust strip printed **714 x 183 of decorative photography**, four elements were still sticky or fixed, and **the largest thing on the sheet was the review chrome sidebar at 220 x 1123, a full page of harness on every page, which the row did not name at all.** The bottom nav, which it did name, does not print: it is off above the desk rung and A4 is 794px wide. **A sweep for `@media print` finds a stylesheet that is missing; only a render finds what that costs.** After: chrome, toggle, trust strip, social row and header controls gone, 0 sticky or fixed elements, ink #111 on white, and `terms.html` went 5,756px to 5,482, `how-it-works.html` 2,308 to 1,965, the wallet 1,438 to 1,123.

**AND THE PRINT PALETTE WAS WRITTEN TWICE, BECAUSE THE FIRST ONE WAS A LIST.** It re-pointed `--bg-canvas`, `--bg-surface`, `--bg-control` and `--bg-chip` at white, and the sheet came out graphite anyway: the plates are gradients on `--bg-plate-from`, `--bg-plate-to`, `--bg-slab-from` and `--bg-slab-to`. **A list of grounds is only as complete as the person writing it; `*` is a rule.** The same lesson arrived a second time on the ink: setting the brass ROLE took `terms.html` and the wallet to zero brass-on-white and left two words on `how-it-works.html` at `#e6c877`, because a hero writes its lit brass straight from the primitive. The seven brass primitives are set for paper now, and brass goes DARK rather than black so the brand still makes its mark: 0 brass-on-white on four of five screens checked, 1 left on `my-profile.html`.

**(e) THE LONG TOKEN WAS A DEFECT AND THE PROPERTY THAT FIXES IT IS NOT THE OBVIOUS ONE.** The longest unbroken string the painted tree ships is 23 characters, so nothing overflows and nobody had looked. A wallet address is 42. Injected with `overflow-wrap:normal`, the wallet row grew the document by **107px at 320 and 37 at 390**, which is horizontal scroll on a phone from one string a person is entitled to type. `anywhere` is the stronger fix and was written first; screenshotted over **269 full pages**, it left **all 212 product readings identical and moved 23 kit pages, four of them changing height**. Exempting `<code>` took that to 12, and the pages still moving printed **no long token at all** - the tell that `anywhere` was not breaking their words, it was resizing their tracks. **A rule that changes intrinsic sizing changes layout in places that have nothing long in them.** `break-word` re-measured over the same 269: **259 identical, 0 page-size changes, and every differing pixel at the instrument's own floor**, proved by shooting the same tree twice and reproducing the single worst page exactly. Nine of ten injection points hold at 320 and ten of ten at 390; the one that does not is a numeric column, where a 42-character address is a data defect and not a wrapping one.

**(c) THE ORIENTATION CONCERN WAS A WIDTH CONCERN, AND ONE CONTROL SETTLED IT.** A landscape phone at 844 x 390 showed **86 clipped boxes against 3 in portrait**, which looks exactly like the row's fear. The same width at a tall viewport, 844 x 900, shows **86**. **The number does not move with height, so it is a fact about width and orientation is not the axis.** And the 86 are not content loss: every one is a `.card` losing exactly **2px**, to the bookmark button's 44px touch floor standing 1px past a fractional card width. No orientation query is needed and none was written.

**(b), (d) AND (f) WERE ALREADY ANSWERED.** The height half of WCAG 1.4.10 reads **44.9 per cent of the viewport at 320 x 256** with 0 horizontal scroll, so it passes; the worst screen is `404.html` and not the `event-feed.html` the row named, which is the same number on a different document. The scrollbar-less instrument the row confesses to was re-run by the row itself at 280 to 310 and found 0. And **`srcset` was answered on 2026-08-13 by backlog 99**: the event photograph's box does not change with the viewport, so a set of sources buys nothing, and what shipped is one correctly sized asset.

## 2026-08-13 - The one legal page this product has built was linked from the review sidebar 106 times and from the product once

Backlog 48. **1,902 placeholder anchors were 1,272 before this pass and are 1,059 now**, and the row's 23 distinct labels are 15. Three things changed and only one of them is the thing the row was written about.

**THE COUNT WAS 630 STALE AND THE ROW SAID SO WOULD HAPPEN.** It was taken on 2026-08-08 against rows 27 and 28, which both closed on 2026-08-10 by cutting the eight destinations the map refuses. Re-measured today in a browser, by accessible name so that an anchor with nested markup is not missed: **1,272 anchors, 105 documents, 17 labels** in `ui-visual/`, **1,086 on 104** in `wireframes/`, **327 on 25** in `ui-kit/`. The row's own list of what they are is obsolete in the same move: Sports, Leaderboard, API, Status, Help Center, FAQ, Careers, Press, Brand and Geo restrictions are gone.

**AND THE LARGEST GROUP IS ONE THE ROW NEVER NAMED.** 525 of the 1,272, five per screen on 105, are the social marks: X, Discord, Telegram, Instagram, TikTok. They are not registered map nodes and no screen will ever be built for them, so they are not the same kind of placeholder as the four beside them and are not fixed by the same decision. `docs/backlog.md` 144.

**THE THING WORTH FIXING WAS NOT IN THE ROW AT ALL.** `Terms` was one of the five the footer keeps at `#` "because they are registered nodes with screens still to build", and **`ui-visual/terms.html` was built on 2026-08-03**. Measured: **1 link to it from anywhere in the product, on `overview.html`, which is the index of the tree rather than a screen in it, against 106 from the review sidebar.** Meanwhile **213 anchors labelled Terms sat at `#`**, 105 in the footer's legal strip and 108 in the sign-in and deposit fine print, on screens that were offering a document the repository already had. **A placeholder is a promise with a date on it, and nothing goes back to the list when the date passes.** 213 anchors in `ui-visual/` and 7 kit specimens point at `terms.html` now, 221 product links, 0 broken. The grey tree keeps its 194 at `#` and that is correct: `ia/docs/sitemap.md` records that Terms of Service is the first screen in this product with no grey twin.

**THE COPY DEFECT THE ROW DID NAME IS REAL AND IT IS NOT THE ONE IT DESCRIBED.** The row says `Privacy` and `Privacy Policy` are the same destination under two names in the footer. **The footer carries only `Privacy`**, and it shortens every legal node the same way: the map's nodes are `Terms of Service`, `Privacy Policy`, `Cookie Policy`, `Responsible betting`, `Contact / Support`, and the strip says `Terms`, `Privacy`, `Responsible play`, `Contact`. That is a register, not a drift. The other spelling stands in the sign-in fine print, where the full legal name is right. **What is a drift is the case**: the cookie banner wrote `Privacy policy` and `Cookie policy` while 109 other instances and the map itself write `Privacy Policy`, and `terms.html` writes `Cookie Policy`. 10 labels on 3 documents across all three trees, normalised to the map's names.

**AND THE INSTRUMENT REPRODUCED THE ROW'S OWN SEVENTH FAULT.** The label reader returned `Privacy Policynot built` and `Cookie Policynot built`, exactly as the audit of 2026-08-08 did before withdrawing them: the markup on `terms.html` is `<span class="rel-q">Privacy Policy</span><span class="rel-odds">not built</span>` inside one anchor, and reading `textContent` joins the two spans. **A defect that a previous pass documented and withdrew will be found again by the next reader who builds the same instrument**, which is the argument for writing the withdrawal down rather than only the finding.

Verified over 267 documents in all three trees: **0 console errors, 0 horizontal scroll, 0 broken links to `terms.html`.**

## 2026-08-13 - Favorites was 96 tab stops deep on a phone, and the walk that found it had to open the menus first

Backlog 130. **Favorites moved from tab stop 96 to tab stop 11 at 390, on every screen, and it stopped depending on how long the page is.** It is a sixth row in the account dropdown, beside My Bets. Nothing moved into the phone header, the bottom bar keeps all four slots, and the header with the menu closed is pixel identical in all three trees at both widths.

**THE INSTRUMENT WAS WRONG TWICE BEFORE THE READING WAS, AND THE SECOND TIME IT WAS WRONG IN THE ROW'S FAVOUR.** The first Tab walk returned the same three numbers for every screen, which is the giveaway: it was walking the **review chrome**, `#rmSidebar` and its toggle, 109 stops that stand in these documents and in no product. Excluding them, the second walk put My Bets and Portfolio at 84 and 99 in the bottom bar and the footer, which made the row look like an understatement. It was not: **a closed disclosure is one tab stop and its contents are not reachable until it is activated**, so a walk that only presses Tab never sees the account menu's rows. Pressing Enter on each `<summary>` as focus lands on it is what a keyboard actually does, and it puts My Profile at 9, My Bets at 10 and Wallet at 12. **The row was right about the shape and its numbers were taken from a different walk than mine**: 84 against my 96, the difference being the skip link and the rows the opened menus inject.

**AND WHAT THE CORRECTED WALK SHOWS IS THAT THE DEPTH IS THE PAGE.** Favorites' only phone route is the bottom bar, and the bottom bar is the last thing in the document, so its depth is however long the screen is: **18 on Wallet, 51 on Event Detail, 64 on Favorites, 96 on the feed.** At 1280 the heart carries `.desk-only` and Favorites is stop 7, so the defect never existed on a desktop. **One of four top-level destinations was reachable at a number that changes with the content above it, and the other three were not.**

**THE ANSWER CHOSEN WAS THE ONE THAT MOVES NO PIXEL.** Three were on the table: the heart loses `.desk-only`, which reopens the thumb-zone tradeoff 03a recorded deliberately and costs 44px of phone header; a second skip link, which fixes the general defect but leaves Favorites unlike its peers; or the dropdown row. The dropdown already holds **two of the four top-level destinations**, My Profile and My Bets, and Favorites was the only one of the four it did not hold, so the row closes an inconsistency rather than inventing an affordance. It is not a fourth affordance either, it is **the keyboard's**: a thumb slot is reached by a thumb, and by a Tab key only after the entire page.

**MEASURED AFTER.** The menu is 6 rows, 196x271 at both widths, no overflow right or bottom; the Favorites row is 194x44 and **the shortest row in the painted menu is 44.0px**, so the family floor holds on the new one. The grey menu's rows are 31.4px and were 31.4px before, on all six, because `wireframes/` links no stylesheet and the 44 floor has never reached it. Over 534 readings across all three trees at both widths: **0 console errors, 0 horizontal scroll, 0 menus overflowing, and the closed header identical on 8 of 8 shots.**

**A COUNT MOVED AND IT IS WRITTEN DOWN IN BOTH PLACES IT LIVES.** `components/navitem.css` said the account menu is **365 placements**, which is 73 signed-in screens times five. Recounted in a browser rather than multiplied: **438 over 73 screens, 6.0 each.** `ui-kit/docs/inventory.md` carries a `navitem` figure of 249 measured over "the 41 screens", and **that sample is not written down anywhere in the file**, so the number is dated there rather than guessed at: a number invented to look current is worse than a number that says when it was taken.

## 2026-08-13 - A name is as long as the thing it names, and 130 controls were called YES

Backlog 103. **130 bare "YES" and "NO" accessible names are 0, and 232 of 232 controls in the `.yesno` family now carry the outcome they act on.** No new copy was written, no route changed and no control moved.

**THE ROW ASKED FOR A VOICE AND IA DECISION AND THE REPOSITORY HAD ALREADY TAKEN IT.** Row 96 settled the multi-outcome rows by pointing `aria-labelledby` at the outcome span and then at the control, and `voice/docs/microcopy.md` wrote down why: **the wording stays in the one place that file owns it and is not typed into the markup a second time.** That rule decides this row too. The binary card's outcome is not a word, it is the card's question, so the name is the question: **"Will Bitcoin close above $150,000 before October 1, 2026? YES"**, 61 characters against row 96's 11. The row treated that length as the reason a different answer was needed. It is not a defect, it is the measurement: **a name is as long as the thing it names**, and the alternative is inventing a short title for every market, which is a second string per event that then has to be kept true.

**WHAT THE COUNT ACTUALLY WAS.** 116 pairs and 232 controls over 14 screens, in four placements: **126 on binary cards, 84 on multi rows, 20 on the event detail, 2 in the feed hero.** The row said 126 per tree and that is exactly right for the binary card. What it did not name is that **12 documents had two or more controls sharing one accessible name**, five "YES" and five "NO" on a single category feed, which is the reading that turns "unhelpful" into "indistinguishable". It is 0 now.

**AND THE MEASUREMENT FOUND A STRAGGLER OF ROW 96 THAT ROW 96 COULD NOT SEE.** Four controls stayed bare after the card fix, on `event-detail-multi.html` and `event-detail-logged-out-multi.html` in both trees: **the SELECTED outcome row**, whose `.opt-name` holds a nested `<span class="opt-sel-tag">selected</span>` and so did not match the pattern that named its four siblings. It is the row a person is most likely to act on and it was the one the sweep skipped. **A pattern written against the ordinary case leaves the special case bare, and the special case is usually the important one.** Named `opt-jd-vance-sel` rather than a number, because the four numbers beside it are positional and this row is not, and renumbering four ids in four documents to make room would be churn for nothing.

**THE HERO PAIR WAS THE FOURTH PLACEMENT AND ITS NAMES ONLY LOOKED FINE.** `.hf-cta.yesno` reads "Back YES" and "Back NO", which is a verb and an answer with no event attached, and it is the largest, first control on the feed. It takes the same treatment from `a.hf-title`.

**WHAT THIS FOUND AND DID NOT ACT ON.** Every pair's two controls point at the same href: **116 of 116, 0 differing**, including the multi rows row 96 already named. So the accessible name now promises a distinction the link does not make. That is a property of a static prototype with no query parameters rather than a naming defect, and it was true before this edit for the 100 controls row 96 had named. It is `docs/backlog.md` 143.

Verified over 420 readings across both trees at both widths: **0 console errors, 0 horizontal scroll, 0 duplicate ids in any document, 0 aria-labelledby pointing at an id that does not exist.**

## 2026-08-13 - The row had the two halves of its own population the wrong way round, and the marking it defended was redundant where it was needed and harmful where it was not

Backlog 118. **285 focus stops that a screen reader was told did not exist, at 390 and at 1280, are 0.** The condensed category strip is `<nav aria-label="Categories (sticky header)">` in all 105 painted and 87 grey documents, and it carries no `aria-hidden` anywhere.

**THE ROW FILED THIS AS A NAVIGATION-MODEL QUESTION FOR 03a AND IT IS A MARKUP FIX.** Its reasoning was that the marking is arguably right on the 57 screens that also carry the main band, because announcing five categories twice is noise, and wrong on the other 48, where the strip would be the only route to a category. Both halves are backwards, and one measurement settles both. **The strip is revealed by an `IntersectionObserver` that observes `.feed-inner > .cat-nav` and returns early when there is none**, so on the 48 screens without a main band the header never gains `.scrolled` and **the band cannot open at all**: measured after scrolling to 1200px on every screen at both widths, `.scrolled` appeared on **57 of 106** and the strip painted on **57 of 106, and on 0 of the 48**. So on the 48 the marking cost nothing, and on the 57 it was the whole defect: **54px tall, five links painted, five reachable by Tab, and the container saying the band does not exist.**

**AND THE ATTRIBUTE WAS NEVER THE THING DOING THE HIDING.** With `aria-hidden` gone, the accessibility tree over all 106 screens holds `Categories (sticky header)` on exactly **57** documents and on none of the other 49, because `visibility:hidden`, added by the earlier half of this row, removes a subtree from that tree as surely as it removes it from the eye. **`aria-hidden` was redundant exactly where the band is hidden and harmful exactly where it is shown**, which is the same shape as the defect the first half fixed: `max-height`, `overflow` and `opacity` each take away a different thing and none of them takes away a tab stop.

**THE FIX IS AN ELEMENT AND A NAME, AND THE NAME IS WHY IT IS NOT A MODEL DECISION.** The strip repeats the five categories of the main band once that band has scrolled away, so the two have to be tellable apart rather than one of them claiming not to exist. It is a `<nav>` now, as the band it duplicates already was, and it is named for the PLACE a person will find it. Over 106 screens the tree reports **0 unnamed navigation landmarks and 0 documents where two navigation landmarks share a name**. No item changed, no route changed, and 03a's rule that the navigation model is decided there is untouched.

**THE PAINTED TREE IS PIXEL IDENTICAL AND THE GREY TREE GREW TWO PIXELS, WHICH IS THE GREY TREE WORKING.** The scrolled header, screenshotted on four painted and two grey screens at both widths against a control of 12 of 12 identical: **all eight painted readings identical**, and the two grey screens went 99 to 101 at 390 and 103 to 105 at 1280. That is `header, nav, main, section, article, footer, aside{border:1px solid #999}` in the grey inline block, drawing a box around a landmark because the strip has become one. **The grey tree is a drawing of the structure, so a structural change that does not show there would be the defect.**

**WHAT WAS FOUND AND NOT FIXED.** Those 48 documents ship a category strip that no code path can open, seven lines each, and their grey twins do too. Deleting it and giving those screens a real category route are opposite answers and both are 03a's, which is what this row was right about all along, just about the other half of its population. `docs/backlog.md` 142. Left alone as well: `aria-current="page"` sits on the `<li>` and not on the `<a>` in both bands, which is a consistent house convention rather than this row's defect, and changing it is 192 documents for a reason nobody has written down yet.

## 2026-08-13 - Two lines of head markup took every layout shift in the product to zero, and the technique the row asked for by name made it four times worse

Backlog 100. **106 of 106 screens at 390 read exactly 0.0000, from a worst of 0.0438 and a mean of 0.0021**, and the same at 1280, over a link throttled to 1.6 Mbps and again at 400 Kbps. The row named two causes and one of them was the fix; the other was built, measured and thrown away.

**THE ROW'S MECHANISM WAS RIGHT, ITS 1280 NUMBERS WERE EXACT AND ITS 390 NUMBERS WERE 4.7 TIMES TOO HIGH.** Everything structural reproduced: **0 of 163 documents carried a preload**, the chain really is HTML then `index.css` then `@import fonts.css` then the woff2, and `fonts.css` is the FIRST of 51 imports so nothing about the order was hiding it. **The 17 screens that open `dialog#outcomeDialog` at load really are the shifters**, six of the six worst, and 3 of the 17 sit at zero, so it is a modal whose content rewraps and not a modal. But the split is **11.3x and not 65**, the worst screen is `sign-in-provider-conflict.html` at **0.0438** rather than `sign-in-error.html` at 0.2050, and **no screen in the product was ever over Google's 0.1**. At 1280 the row's own two readings, 0.0002 and 0.0003, came back to the digit, which is what makes the 390 figures a measurement taken under conditions the row did not write down rather than an error of reasoning.

**AND THE FIRST INSTRUMENT SAID 0.0000 EVERYWHERE, WHICH WAS TRUE AND USELESS.** On localhost the two faces arrive inside `font-display:swap`'s 100ms block period, so there is no swap, so there is nothing to shift. **A performance defect measured on a link with no latency is a defect measured out of existence.** Everything below is at 1.6 Mbps with 100ms of latency, the reading is stable to four decimal places over five runs, and two independent passes agreed exactly.

**THE FIX IS TWO `<link rel="preload">` LINES IN 163 DOCUMENTS AND NOTHING ELSE.** DM Sans latin and Space Grotesk latin, 59 KB of the 669 KB of CSS they were queued behind, with `crossorigin` because a font is fetched in CORS mode even from its own origin and without it the preload is discarded and the file fetched twice. It removes the swap rather than softening it: **106 of 106 at 0.0000 at 390 and at 1280**, and it still holds at 400 Kbps with 400ms of latency, where the font would have had every reason to lose. Verified across all 163 documents: **0 console errors, 0 "preloaded but not used" warnings, 0 fonts fetched twice, 0 documents without exactly two preload links.** And the zero was proved rather than reported: stripping the preload from one screen brought **0.0438 straight back while its sibling stayed at 0**.

**WHAT WAS BUILT AND REFUSED, WHICH IS THE HALF OF THE ROW WORTH KEEPING.** `size-adjust` and `ascent-override` are what every guide recommends and what the row asked for by name. Both faces were written, with metrics measured from this product's own render rather than copied: one real sentence from the trust strip at 100px, DM Sans 7557.4 against Arial 7439.2 for **101.59%**, Space Grotesk 7970.0 for **107.14%**, ascent and descent divided by the same ratio. Measured with the preload removed so the swap would actually happen, over all 106 screens: **mean CLS 0.0021 to 0.0076, worst 0.0438 to 0.1793, and 43 screens worse against 7 better.** It put two screens over 0.1 that had been at 0.0003 and 0.0002. Dropping `size-adjust` and keeping only the vertical overrides fixed those two, 0.1793 to 0.0017, and left `terms.html` at 0.0036 to 0.0275 and `loss.html` at 0.0219 to 0.0370.

**THE REASON IS STRUCTURAL AND IT IS WHY THE ADVICE DOES NOT TRANSFER.** The shift is not the fallback being wrong, it is the fallback being REPLACED, so anything that changes the fallback's box changes what has to move. **Matching one sentence's average advance does not match any particular string's wrapping**, and a rewrapped block moves a great deal more than a line that changes height. The technique earns its place where a fallback is on screen for a long time, and the preload means it is on screen for no time at all. The measurement is written into `components/fonts.css` beside where the rules would have gone, because the next person to read that file will otherwise reach for the same tool.

**A THIRD THING THIS FOUND AND DID NOT FIX.** The preload path is written out 163 times, once per document, and it has to be: a preload that is not in the HTML head is not early, so no token, component or pattern can own it. That makes it the second thing in this repository, after the 1440 in the grey tree, that is a literal repeated across a whole tree. It is `docs/backlog.md` 141.

## 2026-08-12 - The photographs were 5.8 times too wide and not 14, and the decorations were not too wide at all: the drawing was in the alpha plane

Backlog 99. **2,062,090 bytes of artwork became 604,892**, a 70.7% cut, and the feed screen went from 2,922 KB to 1,499 KB. Averaged over all 106 documents in `ui-visual/`, a screen went from **1,591 KB to 1,174 KB and its artwork from 883 KB to 465 KB**. The two halves of the row needed opposite fixes and the row proposed the same one for both.

**THE FIRST HALF WAS TRUE AND ITS NUMBER WAS A FACT ABOUT ONE SLOT.** The row said the event photograph is drawn at 56x88 at 390 and at 1280, and it is, on the feed card. Walking every placement of every asset over all 106 screens at both widths found **four boxes and not one**: 56x88 on the feed card, 56x91.8 on the category feeds, **72x72 on `.ed-thumb`** and **46x46 on `.rel-thumb`**, across 15 screens. And the box is not the demand. **`cover` consumes more source than the box it fills**: 1600x1073 into 56x88 draws **131x88** of source, because the wide side is cropped away after the scale. So the true demand is **137x92**, the true excess is **5.8 times at device pixel ratio 2 and not the 14 the row computed** from 1600 over 56 times 2, and a number taken from a CSS box will always understate what an image is asked for. Re-exported from `visuals/masters/` at **440x295, JPEG q82**, which is ratio 3 of the measured demand with headroom: **1,158,832 bytes to 116,050, a 90.0% cut**, and the composited thumbnail at ratio 3 is indistinguishable from the one it replaces.

**THE SECOND HALF NAMED THE RIGHT FILES, THE RIGHT BYTES AND THE WRONG CAUSE, AND THE COMPARISON THAT PROVED IT WAS BETWEEN TWO DIFFERENT KINDS OF IMAGE.** The row set the trust decorations at 0.72 to 0.92 bytes per pixel against `hero-capitol.webp` at 0.041 and called that eighteen times the density. **`hero-capitol.webp` has no alpha channel and all four decorations do.** Re-encoding one with the alpha discarded takes `trust-column.webp` from 181,828 to 49,242, so **the alpha plane is 65 to 73 per cent of every one of those files**. And the alpha is not an edge: the mean alpha is **25.5 to 55.2 of 255 and three of the four have 0.0% fully opaque pixels**, which means the whole picture is a translucent wash and **the drawing itself lives in the alpha channel**. WebP stores alpha with the lossless coder unless told otherwise, and a halftone stored losslessly is the most expensive thing that can be put in one.

**THE FIRST FIX WAS THE WRONG AXIS, IT SCORED BETTER, AND THE EYE IS WHAT CAUGHT IT.** Resizing all four to ratio 2 of their measured demand gave **82.5%**, better than what shipped. The before-and-after showed why it could not ship: the third trust item is a **halftone globe**, and its dot pattern went blotchy the moment it was resampled, at ratio 3 and at ratio 2 alike. **A halftone cannot be resampled at any scale, because the destruction is in the resampling and not in the ratio.** What shipped instead leaves every dimension untouched and quantises only the alpha plane, `-q 92 -alpha_q 10 -alpha_filter best -sharp_yuv`: **903,258 bytes to 488,842, 45.9%**. Measured against the same baseline, the worst channel delta on the trust strip fell from **40 to 73 down to 10 to 21** and on the visible `.ht-art` from 43 to 70 down to 19 to 25, while the saving only halved. **The cheaper edit was worse in the one place a byte count cannot look.**

**THE INSTRUMENT WAS WRONG TWICE BEFORE THE FINDING WAS, WHICH IS NOW THE FOURTH PASS RUNNING.** The byte counter read **0 KB for all 106 screens** on its first run, because it trusted `content-length` and the local server does not send one; rebuilt on the decoded body it separates `overview.html` at 843 KB from the next lightest at 1,409 KB, which is the row's own proof that the trust strip is the payload. And **`.hf-photo` reported 1.3 to 2.7% of its pixels changed on a file that is byte-identical to its backup**: it is a 1400x788 `<img>` clipped to an 812x407 container, so an element screenshot captures the whole 1400x788 of which most is never painted and is filled by whatever else the page draws at those coordinates. `.hero-feature`, the box that is actually visible, reads IDENTICAL. **An element screenshot is not a screenshot of what the element shows.** The control was two boxes of 66 at a maximum channel delta of 2, proved before any of it was read.

**WHAT WAS REFUSED.** `assets/trust-column.svg` and `assets/trust-globe.svg` are vector line art in brass, 4,086 and 24,385 bytes, and they are unreferenced, so the obvious move is to swap 411 KB of raster for 28 KB of vector. They are an **earlier and simpler schematic** of the same subject, dated an hour before the renders that replaced them, not vectors of what ships. Swapping them is a redesign of the trust strip and not a fix to its weight, so it is `docs/backlog.md` 140 with its number beside it rather than an edit made because it was available.

## 2026-08-12 - Four instruments failed their own control and pointed in opposite directions, and the row that asked to repaint 1,913 controls was answered by repainting three

Backlog 121, and this is the entry about the measuring rather than the fix.

**THE ROW ASKED FOR A DECISION ABOUT THE VISUAL LANGUAGE AND THE CRITERION WAS NEVER ASKING FOR ONE.** WCAG 1.4.11 requires 3:1 from the visual information **required to identify** a component, not from every line drawn around one. A chip carries a word, a button carries a word, a menu carries a word and a mark, an icon button carries a mark. Where the content identifies the control, the edge is decoration and the criterion does not reach it. The row measured the edge, which is 1.23:1 and true, and never asked what was inside the box.

**AND THE ANSWER TO THE QUESTION IT DID NOT ASK IS THAT EVERYTHING IS IDENTIFIED EXCEPT A FIELD.** Sampled from the render at device pixel ratio 3, taking the modal colour of a control's box as its face and the colour furthest from that in luminance as its ink: **no icon-only control in this product is under 3:1 in either theme.** `.icon-btn-lift` reads 8.44 and 5.38, base `.icon-btn` 9.43 and 5.19, `.icon-btn-tile` 5.49 both ways. Every labelled control is carried by its label, and this repository had already measured **0 text contrast failures over 29,929 and 29,984 elements per pass**, so that half was settled before the row was written.

**THE EXCEPTION IS THE CRITERION'S OWN TEXTBOOK CASE AND THERE ARE THREE OF THEM.** `.amount-input` measured **1.32 in graphite and 2.11 in daylight**. A field is the one control whose content is the PERSON'S text, and a person's text says nothing about the box it sits in, so the edge is the only thing on the screen that says typing is possible here. It reads `--border-field` now, **a second role rather than a stronger hairline**, and that distinction is the row's own question answered rather than dodged: a hairline SEPARATES two areas and 1.4.11 does not reach it, and raising it would have repainted every plate, card and divider in the product to fix three fields. 6.35 and 4.32 after; `--border-hairline` is still `#2b2f38` and `#acaaa4`.

**FOUR OF THE FIVE INSTRUMENTS FAILED, AND THEY FAILED IN OPPOSITE DIRECTIONS, WHICH IS THE ONLY REASON ANY OF IT WAS CAUGHT.** The row's own read one screen and said 468. A computed-style census over 105 screens in both themes said 1,913 and 968, **and was blind to `background-image`**, so every gradient-filled control in the product read as having no fill at all. The content pass built on it reported labelled controls at **1.05:1**, which contradicts an audit in this same file, and it was the contradiction rather than the number that exposed the shared cause. A pixel sampler fixed the gradient and introduced two of its own: it required a control to be fully inside the viewport, so it saw **101 controls of about 1,900**, and it read content along a single horizontal line through the middle of the box, **which passes between the strokes of most glyphs and returns 1.00 for a link**. A fifth, aimed at icons alone, reported `.icon-btn-lift` at **2.64 in daylight**, and a direct read of the same element gave 4.33 and the pixels gave 5.38.

**THE READING THAT HELD IS THE ONE THAT LOOKED AT WHAT A PERSON LOOKS AT**, which is the same lesson this file recorded for the icon that measured 24x24 through `getBBox` and 20x20 in paint, and for the SVG with no `fill`. A computed style is a declaration and a screenshot is the product. **A number that four instruments disagree about is not a finding, it is a queue of bugs in the instruments**, and the discipline that mattered here was refusing to repaint 1,913 controls while that queue was still open. Three fields is a smaller answer than the row wanted and it is the one the measurement supports.

## 2026-08-12 - A floor is a rule with a precondition, and this one had gone two years without its precondition being written down or ever mattering

Backlog 122 and 123 closed, 137 opened, 121 corrected and left open. **843 WCAG 2.5.8 AA failures to 0**, and none of the four things worth keeping is that number.

**`min-height` DOES NOT APPLY TO A NON-REPLACED INLINE BOX, AND THE 44px FAMILY FLOOR IS BUILT ENTIRELY OUT OF `min-height`.** Every member of the list in `base.css` had a box by accident of what it is: `.btn`, `.chip`, `.icon-btn`, the tab labels and the menu summaries are all inline-flex or flex already. So the day a bare `<a>` joined the list, the computed style read `min-height:44px` and the box read **39.6 x 21**, which is a rule that applies and does nothing. **That is the same defect as the `pattern` attribute on a field in a document with no `<form>`, and the `aria-hidden` on an operable band**: present, correct, and consulted by nothing. The precondition is now a rule beside the floor with the reason on it, because it is the FLOOR that needs a box and not the component that wants a display.

**THE ROW COUNTED THREE AND THE POPULATION IS 2,904, AND THE INTERESTING PART IS WHICH NUMBER IS THE RIGHT ONE.** Neither. Of the 2,904 controls under 44 x 44 at 390 with the pointer asserted coarse, **569 are the four `.icon-btn-*` exclusions `base.css` names on purpose** and **2,309 are the footer**, which the row never mentioned at all. The number that decides anything is the one measured against the criterion that actually binds: **`.footer-col a` at 36.5 x 14 and 20.5px centre to centre fails WCAG 2.5.8 AA twice over**, once on the 24 x 24 minimum and once on the spacing escape that excuses a small target when nothing else is within 24px of it. 1,154 links on 105 screens, and not one earlier pass had read them, because every earlier pass measured against 44 and reported a number so large that nobody could act on it.

**THREE CANDIDATE FIXES, MEASURED, AND THE CHEAPEST TWO COST THE SAME AND BUY DIFFERENT THINGS.** `padding-block:var(--space-4)` gives 36 x 25 at 28.5 apart and costs 88px of footer at 390. Raising the list gap from 4 to 12 costs the same 88px and also passes, **on the spacing escape alone, leaving the target 14px tall**. `--space-8` gives 36 x 33 for exactly twice the height and no additional compliance. **A rule that satisfies the criterion without making the target easier to hit has answered the audit and not the person**, so the padding won. `padding-block` rather than `min-height` because the box has to grow off the ladder the way every other control here grows, and because a second `min-height` would sit beside the 44 floor arguing with it.

**AND THE LAST FAILURE STANDING IS EXEMPT, WHICH THE INSTRUMENT COULD NOT KNOW.** `sign-in-error.html` has `Privacy Policy` at 69.2 x 15.4 inside the sentence "By continuing you agree to the Terms and Privacy Policy". 2.5.8 carries an explicit **Inline** exception for a target in a sentence or constrained by the line height of non-target text. A probe that implements a criterion's arithmetic and not its exceptions returns a defect that is not one, which is the same shape as every instrument error recorded above it: **the reading was right and the question was wrong.**

**123 WAS CLOSED BY REFUSING THE FIX THE ROW ASKED FOR.** The row said "the fix is a level and not a face", and a level does not fix it: an `<h2>` would still stand before the `<h1>` and would still open the outline at the second level, and the `<h1>` cannot move because it is the feed's own heading and the hero is physically above it. So "Hot right now" stopped being a section and became what it always was, **the name of the list under it**, carried by `aria-labelledby` on the `<ol>`. **The grey tree needed one edit the paint did not**: it styles the heading by TAG inside its own inline block, so the type had to be re-declared for the new element or the tree that owns structure would have lost the label's face to a structural fix.

**121 IS NOT FIXED AND ITS CENSUS IS NOW FOUR TIMES ITS OWN.** Re-read over all 105 screens in both themes with every ground composited: **1,913 controls under 3:1 in graphite and 968 in daylight**, against the row's 468. The largest class is `.chip` at 641, which the row had excluded; `.icon-btn` is 605 and not 1,361, because on the feed it computes `border-width:0` and draws no boundary, which 1.4.11 exempts. **The correction makes the decision bigger rather than smaller**: clearing 3:1 on graphite needs an edge near `rgb(105,105,105)` where the hairline is `rgb(43,47,56)`, and that is not a token raised a step, it is a visible edge on 1,913 controls and a different Vault. It stays open because it is a decision about the visual language and not a defect with a fix.

## 2026-08-12 - The type is in rem, and the thing worth keeping is that the REASON a rule gives is what expires, not the rule

Backlog 115, open since 2026-08-11, closed here. The question that started it was whether the rungs should be in `rem`. **The answer to the question asked was no and the answer to the question underneath it was yes**, and the four things this pass taught are none of them the token values.

**A CONDITIONAL ARGUMENT READS EXACTLY LIKE AN UNCONDITIONAL ONE ONCE IT IS WRITTEN DOWN.** Three files said the rungs stay px because a rung in rem while the type is px would switch the layout at a different window width while every word stayed the same size. That is correct and it is an argument about the TYPE, stated as a conclusion about the RUNGS. Once the type moved it stopped defending anything, and the rungs are now held by px because nobody has decided otherwise, which is a different reason and has to be written as one. **The rungs were deliberately NOT converted in the same pass**, though the arithmetic is exact and free: 640 = 40rem, 760 = 47.5rem, 900 = 56.25rem. Taking that decision inside the sweep that removed its objection would have been the fourth time in this repository that a rule outlived its reason and nothing noticed. It is `backlog.md` 135.

**THE ROW'S OWN PREMISE WAS WRONG BY AN ORDER OF MAGNITUDE AND THE CORRECTION IS WHAT MADE THE WORK POSSIBLE.** It said "40 type tokens, 46 stylesheets and 106 screens", written as though the sizes were scattered. Counted from the comment-stripped source: **229 `font-size` declarations in `components/`, 213 of them through a `--text-*` token, 8 through a `--display-*` one, 5 the deliberate `font-size:0`, and exactly one a raw literal.** The ladder is ten steps, not eighteen and not forty; eighteen is ten plus the eight display clamps. **The edit is 18 declarations in one file.** A ladder exists so that a scale can be changed in one place, and the row had estimated the cost as if there were no ladder.

**AND THE ONE RAW LITERAL IS NOT A FONT SIZE.** `.chart-svg text{font-size:7px}` sits in `viewBox="0 0 300 100"` with `preserveAspectRatio="none"` drawn into `height:160px;width:100%`, so 7 is a user unit in a coordinate system stretched to fill its box by a different factor on each axis. In rem it would follow the reader's browser setting while the chart it labels went on following the viewBox, and the label would grow out of its own plot. **A unit is only a unit inside the coordinate system that reads it**, and a census that greps for `font-size` cannot tell the difference. It stayed px with the reason beside it.

**WHAT THE DEFECT ACTUALLY WAS, STATED BETTER THAN THE ROW STATED IT.** The row said the product ignores the browser's font setting entirely. Nothing here sets `font-size` on `html`, `:root` or `body`, so the root has always been the reader's own number and `rem` has always responded; 717 of 3,120 computed sizes did move at a 24px root. **They were containers with no text of their own.** The reading that says it is the page: a reader with a 24px default got a document **0.2 per cent taller and not one additional word**, on all 105 screens. Afterwards the same reader gets **38.4 per cent** on a phone and every word. The instrument was the preference itself, CDP `Page.setFontSizes`, not a page writing `html{font-size}`.

**THE MOVE WAS PROVED INERT BEFORE IT WAS PROVED USEFUL.** Every step divides by 16 exactly, 13/16 = 0.8125, so the default must not move at all: **0 differing font sizes and 0 differing line heights of 44,547 readings over 210 screen-and-width pairs**, 0 documents changing height, 0 gaining horizontal scroll. Four readings differ by 0.01px of height, three of them on `*-loading.html`, which is the entrance-animation noise this repository has already paid for twice. Four controls ran before any of it: the same screen read twice at root 16 giving 0 of 3,120; the root demonstrably moving 16 to 24; the rem ladder simulated at root 16 giving 0 of 3,120; and a 400px block dropped into a 60px clipped card taking the vertical probe from 6 spilling elements to 28.

**THE SWEEP THAT LOOKED CLEAN WAS MEASURING THE WRONG AXIS, WHICH IS THE FIFTH INSTRUMENT ERROR IN A ROW.** The first pass over 105 screens at three roots returned identical numbers in all four conditions, which is what a broken instrument looks like. It was not broken: it read HORIZONTAL overflow, and larger text does not overflow sideways, it wraps and grows downward. Re-read on the vertical axis the difference appeared at once. **A probe that cannot move is either a page that did not change or a question that was not asked**, and the two are told apart by asking a different question, not by re-running the same one.

**WHAT IT COST, IN ONE ELEMENT.** Of 105 screens at five widths and three roots, exactly one reading gains horizontal scroll: `my-profile.html`, 320px, 24px root, 23px. The cause is `repeat(3,1fr)` in the portfolio summary, and `1fr` is `minmax(auto,1fr)`, so a track cannot shrink below its content and the grid overflows instead. **That is the same defect class this repository deleted from 104 grey files as backlog 116**, a hard-coded column count where the system's own answer is a track that counts. It was latent because at 16px the figures happen to fit. It is filed as 136 rather than fixed, because every candidate fix moves the default rendering and this pass had just spent 44,547 readings proving the default does not move. The only other thing that changes is `.why`, 15 clipped to 60, and `card.css` gives it `-webkit-line-clamp:2`: **a line clamp hiding more words at a larger size is the clamp doing its job.**

## 2026-08-12 - The product already answered this on the card above it, and the compact pair was the one place the same decision wore a second geometry

Backlog 134, opened by the inset fix an hour earlier and closed here. **The row that inset did not clear was never a width problem.**

**52 OF 52 IS THE READING, AND IT IS WHAT TURNS A COMPLAINT INTO A DECISION.** `.yesno.compact` measured 42.7 to 46px wide at 320, 360 and 390 alike, on every placement it has: 42 in cards on 12 screens and 10 in the detail list on 2. Its halves are `flex:0 0 auto`, so the pair cannot grow or shrink anywhere, at any width, in any container. **A number that does not move when the window moves is not a symptom of a narrow window.** The complaint that started this was "the cards do not lay out well on a phone", which sounds like a width, and the plate inset under it was a real defect and was the SMALLER half.

**AND THE FLOOR HAD BEEN MET ON ONE AXIS AND MISSED ON THE OTHER, EVERYWHERE, FOR AS LONG AS THE COMPONENT HAS EXISTED.** `min-height:var(--control-44)` is declared on every variant including this one and nothing unsets it, and the file carried a comment explaining that there is no media block here because "the target is not a mobile concern". The comment was right about the axis it was about. **42.7 x 44 passes every check this repository has ever run**, because the touch floor was written as a height and read as a height, on both trees, in six lists and then in one rule.

**THE ANSWER WAS ALREADY IN THE PRODUCT, ONE CARD UP.** A binary card's `.yesno` is a full-width pair of two buttons. A multi-outcome row states the same decision about one named outcome and was drawing it as two 42.7px chips pressed against the card edge. So the fix is not a new shape, it is the removal of a second one: below rung DESK the row wraps, the name and the percentage take the first line, the pair takes the second and fills it. **The button is 103px at 320, 123px at 360 and 138px at 390, and nothing here names a size** - it is a flex item of a full-width row, so the number is the row's.

**WHERE IT IS WRITTEN, AND WHY IT IS TWO FILES.** `options.css` owns the wrap, because whether the row has a second line is the row's decision; `yesno.css` owns what the pair does with the line once it exists. Neither file names a width the other has to agree with. `min-width:0` on the name is what lets a long outcome shrink rather than push the percentage off the first line, and it truncates nothing: 0 names cut at 320, 330, 340, 360 and 390 across all nine feed screens.

**MEASURED AFTER, ON THE LIVE TREE, 105 SCREENS AT NINE WIDTHS.** Clipped elements: **61 at 1280, 641, 640, 639, 390, 360, 340, 330 and 320**, the identical set at every one, which is the material that bleeds on purpose. The 12 that were still clipped at 320 after the inset are gone. Horizontal scroll 0 everywhere. 104 compact buttons painted at every width, so nothing vanished. Smallest button **42.7 x 44 at 640 and above and 103 x 44 at 320**, which is the rung doing exactly what it says. The desk is untouched: 1280, 641 and 640 read what they read before the edit.

**THE COST IS NAMED RATHER THAN HIDDEN.** The card grows 69px and the feed is 3.2 per cent longer, so fewer cards fit on a screen. That is a real loss and it was the product owner's call to take it, which is why the row was filed instead of fixed when the inset landed: **it changes how the product looks, not how much of it fits, and those are two different decisions with two different owners.**

## 2026-08-12 - A comment that said "the ONE responsive token" is the reason the inside of the plate kept a desktop inset on a phone, and the defect it caused was invisible to every sweep because a card clips

The question was whether mobile paddings could come down so the cards lay out better. The answer is a token, and the way it was missed is the part worth keeping.

**TWO GUTTERS ARE NESTED AND ONLY THE OUTER ONE STEPPED.** `--gutter` is the page gutter outside the two-stone plate and it goes 40 to 14 at rung DESK. `.feed-inner>.cat-layout` holds the inset INSIDE the plate and it was a literal, `var(--space-28)`, at every width there is. So on a 360 phone the chrome took **42px a side, 84 of 360, 23.3 per cent of the window before a card began**, and with the card body and the outcome row under it, **67px a side and 37 per cent before the first letter**. It stands on 77 of 105 painted screens. The token that stepped carried a comment reading "this is the one responsive token", which was true when it was written and became the sentence that stopped anyone looking for a second.

**AND THE SWEEPS COULD NOT SEE THE DAMAGE, BECAUSE `.card` IS `overflow:clip`.** At 320 the multi-outcome row is wider than the card it sits in and the NO button is cut off, **32 clipped elements on 8 feed screens, worst 28.9px**. A horizontal-scroll sweep reads the DOCUMENT, the document does not scroll, and every pass returned zero. It was found by looking at a rendered picture. **A clip is not the absence of overflow, it is overflow with the evidence removed**, and this is the second time in this repository that a numeric pass came back clean over a defect a screenshot showed at once.

**THE INSTRUMENT COST TWO CORRECTIONS BEFORE IT WAS BELIEVED.** First the icon sprite: `icons.js` injects into a 0x0 host, so every screen at every width reported a 300px clipped SVG and the 1280 control was not zero, which means the whole first reading was discarded unread. Then the detail tab strip, reported as clipped on 9 screens: `.ed-tabbar` is `overflow-x:auto` and holding more than it shows is its job, and the probe was walking PAST the scroller and blaming the next clip above it. **A scroll container is allowed to hold more than it shows.** With both fixed the control reads empty at 1280 and still catches a deliberately injected 900px block, and the tree holds exactly one narrow-only defect rather than 105.

**WHAT WAS CHANGED.** `--plate-inset:28px` beside `--gutter`, stepping to 16px in the media block that already existed, read in one place by the SIDES of the plate only: vertical space has nothing above it competing for the same 360px. No new rung, both values on the space ladder, and the comment that said "one" now says "two" and says what it cost. Measured after: the rung is clean at 640 / 639, the identical 61 clipped elements at 1280, 390, 360, 340 and 330 are the same set at every width and are material bleeding on purpose, and 0 horizontal scroll across 105 screens.

**WHAT IT DID NOT FIX, SAID PLAINLY.** At 320 there are still **12 clipped on 6 screens**: the inset alone was never going to clear it, and the measurement said so before the edit. The rest is the shape of the outcome row, not the width of the plate, and it is a separate decision because it changes how the product LOOKS rather than how much of it fits. **The reading that argues it is a statement about the whole set of placements**: `.yesno.compact` is 42.7 to 46px wide across **52 of 52 placements**, 42 in cards on 12 screens and 10 in the detail list on 2, at 320, 360 and 390 alike, because its children are `flex:0 0 auto` and cannot grow anywhere. That is a property of the component, not a symptom of a narrow screen, and 42.7 also misses the 44px target rule on the axis nobody checked. It is in `backlog.md`.

## 2026-08-12 - Four critics read the finished work and six repairers fixed it, and the thing worth keeping is that almost every finding was an ARGUMENT that had gone stale rather than a value that was wrong

Ten agents over one afternoon: four reading with a lens each and no permission to edit, then six repairing with disjoint file ownership so no two could touch the same line. Forty-eight distinct findings, four of them corroborated independently by two critics. **What follows is not the list, which is in `backlog.md` and in the commit. It is the four things the pass taught that no single finding says.**

**A RULE OUTLIVES ITS REASON, AND NOTHING NOTICES.** `button.css` required `.btn` on every selector and justified it by `ui-kit/kit.html`, a file deleted on 2026-08-07. `catnav.css` justified an exception by the same dead file, and the exception turned out to be about a different class than the one it named. `profile.css` explained that its ring does not move in daylight "because `--tint-brass-60` is the one rung tokens.css leaves unshifted", which was a statement about a HOLE dressed as a statement about a ring. `colour.html` argued that `--line-brass-strong` was not a theme hole because "an alpha over a theming ground is theme-aware by construction", which is true of the colour and says nothing about the strength. **In every one of the four the value was defensible and the sentence beside it had rotted**, and this repository keeps its rules by having them read, so a rotted sentence is a rotted rule. The constraint on `.btn` was re-derived from the tree and now says the thing that is true: `.btn` is the anatomy and every modifier is an adjective declaring none of it, so a bare `.btn-primary` would paint brass on a shapeless control, and requiring `.btn` makes that unwritable rather than discouraged.

**A LADDER THAT IS ONLY EVER PRINTED IS A LADDER WITH MISSING RUNGS.** `geometry.html` stated the control heights and the icon sizes as a `<dl>` of prose. Drawing them for the first time found that the control ramp held **3 of 6 rungs** and that two icon sizes, `--icon-16` and `--icon-18`, are reachable only by a component writing a width and a height by hand. The kit's own rule already said it, "a page about a rule with nothing under it cannot be checked by reading it", and the page that had been breaking it was the one whose whole subject is dimension. The same act placed **15 colour roles that had a class and no swatch**, and the reason they were missed is worth the sentence: **8 of the 15 are lines**, and a page that draws every role as a filled rectangle cannot show a border role at all.

**TWO CORRECT EDITS CAN BREAK EACH OTHER, AND ONLY ONE OF THEM HAS TO BE A LITERAL.** `seo-plate.css` carried `max-width:60ch` on the plate's text column, written as the TIGHTER number, measured, argued, and winning on specificity over the family rule. `--measure` moved from `66ch` to `46ch` the same afternoon. The literal went on winning and what it now won was **89 characters against 66**, so a rule written to pull the plate in was holding it out, on nine screens, silently. Neither edit was wrong. The rule is deleted rather than restated, because a second cap that agrees with the first is one number with two spellings.

**AND THE STAGE'S OWN HEADLINE TOKEN WAS CAPPING IN THE WRONG UNIT.** `--measure:66ch` was justified as being inside the 60 to 75 band `DESIGN.md` states. **`ch` is the advance of the digit zero, and in DM Sans that is 1.48 average prose characters**, so 66ch bought about 98 characters and the cap that was supposed to land inside the band landed 30 per cent over it. The census could never see it because it computed `width / chWidth` and compared the answer to a band written in characters. It is `46ch` now, which is `67.5 / 1.48`, and it was swept as well as derived: the window in which every capped placement sits inside 60 to 75 is 45ch to 48ch, so two instruments agree. `--container-read` and `--container-doc` were carrying the same confusion in prose and now state both numbers. **The improvement the old cap bought was real and it stopped short**, which is a different thing from being wrong, and it is the thing a measurement written in the wrong unit will always look like.

**WHAT THE CRITICS FOUND IN THE PRODUCT, as opposed to in the record.** Twenty-four contrast failures, all of them one class, `.bp-pct`, quieting text with `opacity` in defiance of a rule this folder wrote itself: 3.93:1 and 4.37:1 and 4.39:1 at 10 and 11px. **And under them a twenty-fifth the audit could not have seen**, because every shipped screen opens with YES chosen and the NO side only takes `.sel` when a person picks it: that state measured **3.64**. Worst of 160 readings is 5.49 now. A theme hole collapsing four brass roles into one in daylight, closed by giving the alpha ladder a seventh rung, `--brass-a75`, calibrated by holding a ground fixed and sweeping the alpha until one rendered step matched: **one rung is worth 1.09 of edge contrast on chalk and 1.31 on graphite**, which is the "about a third" the light theme has always claimed, finally as a number. **No skip link anywhere on 210 screens**, WCAG 2.4.1 level A, with the feed's first main-content stop at number 4 of 113 and the bottom bar's first slot at 82. Fifty-six native radios parked off-canvas with `pointer-events:auto`, in both trees. A chart glow that did not theme while its own line did.

**THE INSTRUMENT WAS WRONG BEFORE THE FINDING WAS, FOR THE FIFTH PASS RUNNING, AND THIS TIME IT WAS WRONG IN THE PUBLISHED WORK.** `context.newPage({viewport})` silently ignores the viewport, because in Playwright those options belong to `newContext`. Three verifications of the Responsive stage therefore measured 1280 while reporting six different widths, and one of the wrong numbers, `.resolution` at 92ch, had been written into a component file where a maintainer would read it. **An option that is ignored rather than rejected is the same class of defect as a media query that reads a variable**, and this repository now has both written down beside each other. Two more of the same shape were found by the critics: `getComputedStyle` called in the same turn as a synthetic `Tab` returns the pre-focus values, and `getComputedStyle` before and after `setAttribute('data-theme')` inside ONE evaluation returns the old value both times.

**AND THE WIDTH TABLE THIS STAGE PUBLISHED WAS BUILT ON ONE PLACEMENT PER COMPONENT.** Re-measured across every placement: `navitem`, published as FIXED at 258px, is **79px at 320 and 159 at 639** in the bottom bar, which is 420 of its 995 placements; `chip`, published as FIXED at 81px, measures nine different widths in one document; `logo` is fixed in the header and FILLS the footer brand. The verdict vocabulary went from four words to six, every row now carries pixels as well as a relation, and the one sentence that had been merging three readings is three sentences. **The consequence is filed rather than acted on**: the container-query refusal was written with a threshold, "the first component placed in two columns of different widths", and **35 of 47 components meet it**. The stage had looked for that case among the organisms and it was among the atoms.

---

## 2026-08-12 - Responsive is closed, and the two numbers the stage is proudest of are the ones it took back

Steps 4, 5 and 6. The stage ends with 33 width queries, 0 in a screen file, three rungs kept as a
registry, four tokens added and four refused. **What is worth writing down is not that, it is that
the stage corrected its own findings twice and its own instrument five times.**

**THE REGISTRY HOLDS AND IT WAS CHECKED RATHER THAN TRUSTED.** Every `@media` in `components/` read
and every number compared: 639.98 and 640 (8 and 6 rules), 759.98 and 760 (4 and 3), 900 (6), the
three named one-offs 560, 620 and 980, and 1140 which is the harness. **0 media queries in any of the
106 painted screen files.** The three one-offs were not taken on trust either: each says in a comment
what collapsing it to the nearest rung would cost, in pixels, and two of them cost a control or a
card going backwards.

**STEP 1 SAID 38 OVER-LONG LINES AND THE NUMBER IS 12.** The step-1 pass measured the element's BOX,
and `.related-list li` is a flex row of a 46px thumbnail, a question clamped to two lines and an odds
figure: **a 106ch box with no 106ch line in it**, 27 times, which was 27 of the 38. The corrected
filter is the finding and it lives beside the token: of 775 candidate blocks it throws out 261 that
stand on one line, 40 that are line-clamped, **27 whose child is laid out as a row**, and 3 that hold
a block of their own. `--measure` is placed on three classes, `.resolution` (9 at up to 106ch, the
named resolution rule, which is this product's second design principle written as a sentence),
`.sys-note` (154ch, the longest line in the product) and `.protect-page`. **15 over the measure
becomes 3**, and the 3 are `.feed-seo`, which `--container-read` decided long ago.

**AND A CAP WAS WRITTEN AND TAKEN OFF WITHIN THE HOUR.** The walk reported one `dd` at 89ch and the
only `dd` family the how-it-works page has is `.hiw-faq dd`, so the rule went there with a paragraph
of reasoning about the icon column. Read by ancestor chain rather than by tag name, the element is
`dd < dl < section.feed-seo` on `event-feed-logged-out.html`: a family already decided, measuring
inside its own rule. **A selector is not an identification.** The reverted rule keeps its comment in
`hiw.css` so the next reader does not repeat it.

**BACKLOG 116: THE GREY TREE COMPUTES ITS COLUMNS NOW.** Three rules and two unnamed widths, 960 and
1280, deleted from all 104 grey files and replaced by the one fluid track the paint already used.
Counted in a browser rather than read: painted 1/1/1/1/2/2/2/3/3/4/4 and grey 1/2/2/2/2/2/3/3/4/4/4
from 360 to 1600. **The mechanism agrees and the container does not**, which is a different sentence
from the one the row opened with, and it is not invented by this edit: the grey content column is
wider at the same window and its gap is 10px against the painted 16.

**BACKLOG 43: DO THE RAW LAYOUT PX NEED A SCALE OF THEIR OWN? NO, AND IT IS NOT A SHRUG.** Censused
with comments and media queries excluded: **88 genuine layout literals in 51 values, not 81.** The
row's 81 had counted **127 box-shadow numbers and 6 filter numbers**, and a shadow offset is not a
layout dimension. A ladder is for values standing in a RELATION, which is what makes `--space-8` and
`--space-12` two steps of one thing; 214, 300, 196, 322 and 160 stand in no relation at all, and a
shared scale would invent an arithmetic nobody measured. **What some of them needed was a name, and
the test is how many files use one.** 44 of the 88 stand in exactly one file and stay there. Of the
15 shared values exactly two are one fact: `--rail-width:214px`, which `toc.css` and `catnav.css` had
already agreed on **in prose**, the comment reading "the same 214px" while nothing held it, and
`--menu-min:196px`. A `--sticky-gap` was refused for the reason `--grid-gap` was refused, and the
16px is `var(--space-16)` now. Tokenisation proved inert: **0 differing rows of 30**.

**WHAT EACH COMPONENT DOES WITH WIDTH, AND THE THREE WAYS THAT READING WAS WRONG.** 35 of 45
components have **no width behaviour of their own at all**: they fill what they are given. 5 are
fixed, 3 change their share, 2 go in a band. Getting there took three corrections. Measured against
the WINDOW, **33 of 43 read as stepping at 640**, because the page gutter goes 14 to 40 there and
takes 51px out of the content column: the frame's behaviour arriving in every row. Measured against
the parent's BORDER box, seven more read as changing their share, because the parent's own padding
steps at the same pixel. **A component that is fluid inside a container that steps is still fluid.**
And the probe first picked `.sel` for three different components, because a class named by two
component files is nobody's, and read `button` as "gone in a band" because the widest `.btn` in the
product is `.hiw-btn`, one face of eight. The column is in `inventory.md` for all 45; the
"What it does with width" section is on the **21** pages whose component owns a width query and on no
others, because a section saying "nothing" on 24 pages is noise the column already carries once.

**STEP 5 IS ANSWERED IN THE SHORT FORM AND THAT IS AN ANSWER.** The audit named no new behaviour, and
the stage does not invent one to fill a step. The product has exactly one list-and-detail pair, Event
Detail is a mandatory context screen carrying growth zone 2 from `cjm-as-is.md`, and a split view
would halve exactly the screen the product exists to widen. No new state, no focus management, no
history handling, and no microcopy for an empty pane.

**STEP 6, THE SWEEP, AND THE CONTROL THAT HAD TO COME FIRST.** 320 to 1600 at 40px, 10px within 20 of
each rung, one pixel either side: **50 widths**. Painted tree 5,300 readings, grey tree 5,200,
carriers 5,250. **0 chasm widths and 0 carrier disagreements.** Below 640 the bar stands and every
`.desk-only` is off; from 640 up the mirror, at every one of the 50 widths. **The control ran first
because 0 is also what a blind probe reports**: a 2000px block injected into five screens was seen in
**20 of 20** readings, and only then was the zero worth writing down.

**AND THE INSTRUMENT FAILURE THAT WAS MINE, WHICH INVALIDATED THREE EARLIER VERIFICATIONS.**
`ctx.newPage({viewport})` silently ignores the viewport: in Playwright those options belong to
`newContext`, not to `newPage` on a context. Three runs therefore measured **1280 while reporting six
different widths**, including the tree smoke test that closed step 3. Re-run with `setViewportSize`,
the measure numbers held and the column comparison turned out to have been nonsense: the container
read 1142px at a nominal 360. **An option that is ignored rather than rejected is the same class of
defect as a media query that reads a variable**, and this repository now has both written down.

---

## 2026-08-11 - The shell was already right and the way it hid one band was not, and three properties that remove a thing from the eye remove it from nothing else

Responsive step 3. The step's job was a fork with three legal answers, and the fork turned out to
have been decided a stage earlier and built two stages ago, so the work became a proof. **The proof
is what found the defect, and no reading of the stylesheet could have.**

**The fork is A and it is read off 03a rather than argued here.** The stage decides the form of the
navigation and never its items, so the three questions go to `ia/docs/sitemap.md`: four top-level
items, no second level that has to stay visible, and no side space wanted for new behaviour, which
the audit had already put at zero. Four items and no permanent second level is branch A, the items
move into the header, and the product's version of A is the lean header that D-desktop-1 describes:
Events becomes the logo, My Bets and Profile fold into the avatar menu, Favorites and Notifications
become icons, the balance is the cluster's swap. **No rail, and no destination the phone does not
have.**

**The swap itself measures clean on three instruments.** Over all 106 painted screens at 360, 639,
640, 641, 759, 760, 761, 899, 900, 901, 1280 and 1440: `.bottom-nav` is painted on 105 below the rung
and `display:none` on all 105 above it; all 178 `.desk-only` elements go `none` to `flex` at the same
pixel; the bar holds 4 tab stops below and 0 above; and `Primary (mobile)` is in the accessibility
tree below and gone above. **The carrier that leaves leaves the paint, the tab order and the
accessibility tree together**, which is the property the step exists to check, because a carrier
hidden the wrong way stays reachable after the eye has stopped seeing it.

**"Exactly one carrier" is true of the PRIMARY one and the page also has a footer, and that is
written down rather than waved past.** Counting rendered links to the four destinations by region:
below the rung it is the bottom nav plus the footer on 73 screens and the footer alone on 32; above
it, the header plus the footer on 73 and the footer alone on 32. The footer never changes at a rung
and carries Events and My Bets on all 105, and the 32 are the logged-out screens. Two of the four
destinations are one interaction deeper on the desk, My Bets and Portfolio, both inside the avatar
menu; that tradeoff is stated and accepted in D-desktop-1 and is not this stage's to reopen.

**THE FINDING: 440 FOCUS STOPS ON CONTROLS NOBODY CAN SEE, ON 88 SCREENS, AT EVERY WIDTH.** All of
them are the five links of the condensed category band. The band is hidden by `max-height:0`,
`overflow:clip` and `opacity:0`, which between them take it off the page, away from the pointer and
out of the ink, and **not one of the three touches the tab order**. Every one of the five also sits
under `aria-hidden="true"`, so a person tabbing landed on a control the eye cannot see and a screen
reader will not name, which is the pairing that makes it worse than either half.

`visibility` is the property that closes it and `display:none` is the one that cannot be used: the
band exists to transition, and `display` collapses the box the transition needs. `visibility` is
animatable discretely, so it holds `visible` for the whole collapse and flips at the end. It is in
`components/header.css` and in the 87 grey files that carry their own copy of the rule, because the
tab order is structure and the grey tree owns structure. **440 to 0 in the paint and 0 in the grey,
the band still opening on all 87, and the layout control at 0 differing rows of 24**, which it had to
be, since `visibility` reserves the box it hides.

**Half of it is deliberately not fixed, and the half is named.** With `.scrolled` forced on, the band
is 54px of visible, operable links still carrying `aria-hidden="true"`. On the 57 screens that also
carry the main `.cat-nav` that is arguably right, because announcing five categories twice is noise.
**On the other 48 it is not right at all: those screens carry the condensed band and no main band, so
the only route to a category is the one marked as not existing.** The two answers are opposite, the
choice is about the navigation model rather than about a header, and the stage's own rule is that the
model belongs to 03a. `backlog.md` 118.

**FOUR INSTRUMENT ERRORS, AND THE STEP IS THE FOURTH PASS RUNNING WHERE THE INSTRUMENT WAS WRONG
BEFORE THE FINDING WAS.**

1. A rect plus a `display` walk called a shut dropdown painted, **1,752 times**. A closed `<details>`
   puts its children in `::details-content` at `content-visibility:hidden`, where they keep a box and
   a computed `display` and are never rendered. This repository had already written that down, in the
   step 5 audit, about a different element.
2. The first Tab walk was **capped at 120 stops** and never reached the bottom bar, which sits after
   the footer in the DOM. It reported 0 stops in a carrier that has 4. The bar's first stop on the
   event feed is number **87 of 118**, which is itself worth knowing about a phone's primary
   navigation.
3. The `ui-visual` harness arrived in the accessibility tree as a fifth navigation landmark. **That
   is the fifth reading this chrome has entered in this stage alone.**
4. The ghost census called **1,063** controls ghosts by counting everything invisible, which swept in
   every `display:none` control the rungs correctly turn off. **`display:none` is the RIGHT way to
   hide, because it takes the control out of the tab order with it.** Filtered by focusing each
   candidate and asking where focus landed: 446, of which 440 are the band and 6 are `.ptab-in`, the
   visually hidden radio of the CSS-only profile tabs, whose ring `tabs.css` already forwards to the
   visible label.

**And 18 of the 105 were hiding behind a modal.** The deposit, sign-in, win and loss screens ship
with a `<dialog>` shown, which makes the rest of the document inert, so they read 0 ghosts while
carrying five each. The honest pair of numbers is **440 on 88 screens with the sheets as they ship,
and 525 on 105 the moment a sheet is shut**, and a single number would have been a claim about the
sheet rather than about the band.

## The stage numbers in this file are the old ones

The project used to count thirteen stages and ran one number ahead of the course from Information
Architecture onward. It was renumbered to twelve on 2026-08-02, and the entries below were
deliberately **not** rewritten: an entry is true as of its own date, and renumbering it would make
it disagree with the commit message it describes. Read them through this key.

| Written here | Means, in course numbering | Stage |
|---|---|---|
| Stage 01 | 01 | Foundation Research |
| Stage 02 | 02 | User Research |
| Stage 03 | 02+ | CJM, inside User Research |
| Stage 04 | 03a / 03b | Information Architecture |
| Stage 05 | 04 | Wireframes |
| Stage 06 | 05 | Voice |
| Stage 07 | 06 | Concept |
| Stage 08 | 07 | UI + Visual |
| Stage 09 | 08 | Tokens + Components |
| Stage 10 | 09 | Design System |
| Stage 11 | 10 | Responsive |
| Stage 12 | 11 | Animation |
| Stage 13 | 12 | Handoff |

01 and 02 did not move, so a number below 03 means the same thing either way. Everything from
Information Architecture on is one higher than the course. References that point FORWARD, at work
not yet done, were renumbered wherever they live, because those are the ones a reader acts on:
`README.md`, `STRUCTURE.md`, `CLAUDE.md`, `backlog.md` and the two documents in `ui-kit/docs/`.

Per-stage detail lives with its stage: `docs/kit-archive/docs/architecture.md` (the full Stage-09
record, moved there on 2026-08-07), `wireframes/_critique.md` (the wireframe defect tables),
`voice/docs/microcopy.md` (the copy rewrite log).

---

## 2026-08-11 - The head that was filed as not a wearer was the fourth wearer, and the ring rule was a shape rule the whole time

The tail of the plate-head chain: backlog **109, 110, 111 and 112**, all four opened that
morning by the pass that wrote `components/platehead.css`. Three of the four had a premise
that did not survive being measured again, which over two passes is five rows of nine.

### 109. A face turns out to be an anatomy plus a default skin, and it took a fourth host to say so

The row asked a real question and offered two answers: either the anatomy is a third thing,
or the face should have been split into an anatomy and a skin from the start. **The measured
answer is the option it did not list.** Read against `.plate-head` with both overlays open:

| what | identical | what differs |
|---|---|---|
| the box, 15 properties | **13** | the ground, and the content's own height |
| the wave `::before`, 15 | **13** | one opacity, `.16` against `.2` |
| the win glow `::after`, 15 | **12** | colour, opacity, and a blur two apart |
| the heading, 11 | **10** | one `ch` count, 16 against 15 |

And the wave's data URI was **byte-identical**, md5 `c87f8063`: the same 300 bytes standing
twice, for the second time in one week.

The row's stated objection was that folding it in would cost two classes where backlog 108
found one. **It cost none.** `.outcome-dialog`, `.win-dialog` and `.loss-dialog` already sit
on the element's ancestors, so the scope was there the whole time and only the markup had to
say `plate-head`. `dialog.css` went from six rules carrying anatomy and skin together to
seven carrying skin only, and `.plate-head` is on **10 more elements**, 6 painted and 4 in
the kit.

**The loss head is the one plate head with no glow, and it now has to say so out loud**,
because inheriting the face means inheriting a brass one, and brass on a loss head is the
brand borrowing an outcome's place. `content:none` rather than `opacity:0`: a transparent
210px blurred circle is still a composited layer.

One number went with it. The win glow blurred at **44** here and at **42** on the face, and
it blurs at 42 now, which is backlog 98's finding rather than a decision. Collapsed and then
measured rather than the other way round: **0 differing pixels of 27,160, control 0.** The
glow is anchored outside the box and clipped, so two pixels of blur radius never reached a
pixel anybody could see. A number can be wrong for months and cost nothing, and that is not
an argument for leaving it: it is the reason nobody found it.

The file's own `Stand:` line was wrong in both halves, `plate-head.html` and `#plate-head`
against the real `platehead.html` and `#platehead`. **The folder's note that a pointer is a
claim and nothing checks a comment was written the same week a file was born with two broken
ones.** Corrected by opening both.

The placement count moved 339 to **359** and was re-taken in a browser rather than by grep,
because `class="plate-head` inside a `<code>` block is markup to a regex and not an element
to the page: 334 in `ui-visual`, 25 in `ui-kit`, 0 in `wireframes`.

### 110. A body shares its head's horizontal padding, and the gap is a different question

The sentence the row said was missing is written now, beside the placement. Measured over all
four sheets in both themes at 390 and 1280, **identical at all eight readings**:

| sheet | head | body, before | step | body, after |
|---|---|---|---|---|
| bare, 115 elements | 24 / 20 / 20 | 20 all round | +0 since backlog 104 | unchanged |
| sign-in, 110 | 24 / 20 / 20 | **16 all round** | **-4** | 16 / 20 |
| outcome, 12 | 24 / 20 / 20 | 20 all round | +0 | unchanged |
| how-it-works, 111 | 32 / 24 / 28 | **20 all round** | **-4** | 20 / 24 |

That was a 4px step between a title and the content beneath it on **221 of 348 sheets**, and
not the same 4px twice. **Neither was an optical correction**, which is the argument the row
left open: an optical correction is one value applied on purpose, and these were two
different values arrived at by accident, a small sheet padding all four sides equally and the
generic body value standing under a hero that pads 24 because a hero is bigger.

**The vertical padding and the gap are deliberately untouched.** An edge is shared with
another element and has to agree; a gap is between siblings of one body and says how dense
that body's content is. Four bodies at 8, 12, 12 and 16 may be four densities or may be
drift, and nothing in the system says which, so it is filed as item 114 rather than swept.
Half a row closed on purpose beats a whole row closed on a guess.

### 111. The first reading said zero, and the zero was the instrument

**Read the instrument before you read the finding, for the third pass running.** The first
measurement focused anchors from script and reported that nothing changed shape. Two things
were wrong with it and the control found both: `:focus-visible` matches a scripted `focus()`
only when the last interaction was keyboard, so **2,689 anchors were focused and 17 matched**;
and the query asked for a descendant of `.hiw-full` when the element in question **is**
`a.hiw-full`, so the rule's loudest victim was never in the list.

Re-read with CDP `CSS.forcePseudoState`, which does not guess:

| what | count | at rest | focused |
|---|---|---|---|
| the close disc, `.icon-btn.sheet-close` | 17 | **100px** | 6px |
| `.hiw-full` block links | 17 | 10px | 6px |
| `.btn` blocks that are anchors | 14 | 10px | 6px |
| class-less text links | 40 | 0px | 6px |

So the row's "one control on six overlays" is **48 shaped controls on 17 pages**, plus the 40
the rule was actually written for. **An outline follows its element's `border-radius`**, so
the only way to round a ring is to round the element, and a rule that reads as being about a
ring was silently a rule about every shape in a sheet. The disc is the worst of them because
`showModal()` autofocuses the first focusable child, which makes it the **first paint** of
every one of those sheets rather than a rare state. Contrast is unaffected either way, 3.53:1.

**The fix is the scope and not a second selector**, and not a list either.
`dialog.app-dialog a:not([class]):focus-visible` is one condition and it is the rule's own
sentence: an anchor with no component on it has no shape, so the ring gets one. A list of the
three components being overwritten fails in the wrong direction, silently catching the fourth
shaped anchor to arrive; this fails in the right one, because a new component brings a class
and keeps its shape with no edit here. After, with the control proving the rule fires at all
(**2,706 anchors read, the ring changes on 2,706**): 40 still take the corner, 48 keep their
own.

### 112. The grey tree, at three addresses, and the third one is only half a styling question

| what | the paint | the grey tree, before | after |
|---|---|---|---|
| `.hiw-btn` | hidden below 760, `header.css` | **no rule at all**, shipped to 320 | hidden below 759.98 in 87 files |
| `.chart-svg` | 160, steps to 280 at 760 | **130 at every width** | 160, steps to 280 at 760, in 92 files |
| the `.subcat` rail | pinned at **900**, `catnav.css` | **640 in 92 files, 900 in one** | 900 in all 92 |

`.hiw-btn` is the 88px control that put 73 painted screens into horizontal scroll from 641 to
652 before it was moved, which is why the grey tree shipping it at 320 mattered more than its
own width did. The chart's base moved 130 to 160 as well, so both ends of the rung tell the
paint's story rather than only the top one.

The rail is the interesting one: **the tree held the right rule and the wrong rule for one
component**, one file at 900 and 92 at 640. The `.cat-layout` declarations went with the fix
because **0 grey files carry that markup** and a rule for absent markup is a fossil. What is
left is markup rather than styling, and it is item 113: `<!-- /cat-main --><!-- /cat-layout -->`
closes in **76 grey files with nothing opening it**, while the paint has the wrapper on 77
screens. That has two opposite answers, the grey tree lost it in a port or the paint invented
it, and a closing comment with no opening tag is evidence of the first rather than proof of
it, so it is filed rather than guessed.

### What was measured, and what the control said first

- **The four rows, computed style, every dialog opened.** A `<dialog>` with no `open` is
  `display:none`, so this is the only instrument that can see 222 of the 225 plain plate heads
  and all 10 outcome heads.
- **The blur collapse, pixels.** Control 0 over 27,160, comparison 0.
- **Row 111 by forced pseudo-state**, after the scripted-focus reading was proved to be
  measuring 17 elements out of 2,689.
- **All three trees smoked at the rungs and one pixel either side** - 359, 360, 361, 639, 640,
  641, 694, 759, 760, 761, 899, 900, 901, 1280 - after 92 grey files had a rung moved:
  **3,724 readings, 0 horizontal scroll, 0 console errors.** 694 is in the list because it is
  the width the desk header asks for.
- **The comment integrity of every stylesheet touched**, because a note that closes its own
  comment early cost this repository a day: 29 properly paired comments in `dialog.css` and 0
  unclosed, with the naive grep count of 30 explained by one `/*` quoted inside a comment.

Sweeps were throwaways in the scratchpad and are deleted.

## 2026-08-11 - One face was written down twice, and the instrument that was supposed to prove it could not see 222 of its 225 placements

Five rows closed in one pass, 104, 105, 106, 107 and 108, and **two of the five had a premise that
did not survive being measured again**. That is the shape of the day rather than an aside: every one
of these rows was written by an earlier pass of this same week, and three of them were arithmetic
taken on trust.

### The face is a file now, and it is the first component here found by comparing two stylesheets

`components/platehead.css`, level 1, four rules. **The brass-cornered head of a plate** is a
two-stone ground with a brass hotspot at `120% 96% at 100% 0%`, a five-line wave masked away from
that corner at `opacity:.2`, a 210px glow anchored OUTSIDE the box at `-72 / -52` and blurred 42 at
`.42`, and a display-face heading over all three. It is worn by three components:

| host | elements | width | what it keeps for itself |
|---|---|---|---|
| the plain sheet head, `.sheet-head` in a dialog that is not an outcome overlay | 225 | 418 | padding 24/20/20, `--display-sheet`, 15ch |
| the how-it-works sheet head, `.hiw-hero` | 111 | 462 | padding 32/24/28, `--display-hiw` |
| the how-it-works page hero, `.hiw-page` | 3 | 922 | padding 32/24, an edge, a 16px corner, a 20px bottom margin, an inset lit lip, `--display-hiw` |

**339 placements in the painted tree and the kit, and 0 in the grey tree**, which links no
stylesheet and takes the copy rather than the class, the rule the Yonder rename set the same day.
**28 declarations that stood twice stand once.**

**WHAT MADE IT FINDABLE WAS A FIX FROM THE SAME MORNING.** Backlog 98 had walked six numbers on the
how-it-works copy so it would agree with the sheet head's: the glow 224 to 210, its blur 40 to 42,
its opacity .5 to .42, its inner mix 65 to 60 per cent, the wave .24 to .2 and the ground radial's
vertical stop 92 to 96. Every one of those was the right value. **Six numbers moved by hand to make
two rules agree is one rule written twice**, and the seventh edit would have drifted again, because
the three heads are never on one screen and nothing in this repository had ever put them beside each
other. That is what the component page is for.

**THE RENAME 98 ASKED FOR IS STILL REFUSED, and this is why it was the wrong shape.** `.hiw-hero` to
`.sheet-head` moves the duplication rather than removing it: the head's paint lands in `dialog.css`
for the sheet, and the page hero, which is not and cannot be a sheet head, has all six rules written
out again. What removes it is a FACE that is a thing, with each host saying only where it sits and
how loud its heading is. The precedent was already twice in `components/`: four controls in the
header band wear one hover and no component file could own it, and the brand lockup stands in the
header and the footer and became `logo.css` four days ago. This is the same move one floor up, and
it loads at level 1 for the lockup's reason word for word - it holds nothing from the system, and
both wholes that hold it load at level 3, so on a tie the host wins.

**THE GLOW WAS AN ELEMENT IN ONE HOST AND A PSEUDO IN THE OTHER, DRAWING THE SAME CIRCLE.**
`<span class="hiw-glow" aria-hidden="true">` carried **200 copies across the three trees** - 106
painted, 6 in the kit, 88 in the grey tree - with a rule in the system to size it and a second one
inline in every grey wireframe that still said 224, while the sheet head next door drew it with
`::after` and no markup at all. In the grey tree it carried no background, so **88 of the 200 painted
nothing at any width and had never painted anything.** A glow is not content. The span is deleted in
all three trees and the pseudo is the mechanism.

### 105 was the precondition and it landed as one edit, and it found the same defect one tree over

`.hiw-hero.hiw-page` was a modifier on a class that means "the head of a sheet", on a box that is
922 x 161.89 at 1280 against a sheet head's 462, at DOM depth 9 rather than 3, with an edge, a
corner, a margin and a lit lip that no sheet head has, an `<h1>` rather than an `<h2>`, and a tagline
at 16px/44ch against 14px/32ch. Four elements. It is `.hiw-page` now and it wears the face directly
like the other two. **A face cannot be shared by three heads while one of them is spelled as a
modifier on another**, which is why the two rows are one edit and are recorded as one.

**AND THE GREY TREE HAD THE SAME DEFECT WITHOUT THE MODIFIER.**
`wireframes/_generators/port_chrome.py`, deleted with the other generators, had flattened
`.hiw-hero.hiw-page` to a bare `.hiw-hero` when it ported the chrome, so **five page-only rules stood
UNSCOPED in 87 grey files and 86 of those files have no page at all**: the page hero's 32/24 padding,
its 20px bottom margin, its 16px/44ch tagline and its 14px FAQ have been landing on the how-it-works
SHEET head on every grey screen that carries one. **430 rules deleted in the 86 files with no page,
12 re-keyed to `.hiw-page` and `.hiw-cols` in the one that has.** A generator that flattens a
compound selector writes a rule that is right about the values and wrong about the element, and
**no sweep in this repository reads a grey stylesheet**, which is the second time this week that the
second system has been the one carrying the older defect.

### 106: the exception was measured once, against a glow that stopped existing, and it is the rule

The close disc on the how-it-works head took `.icon-btn-ring-strong`, which replaces the system's
brass focus ring with `--text-strong`, because `.hiw-glow` put a brass radial in exactly the corner
the ring lands in: 2.88:1 average, 2.52:1 at the brightest point, under the 3:1 floor for an
indicator, in the Vault only. Re-measured at the button's own corner, in the annulus the ring
actually covers, DPR 2, both widths, both themes:

| head | Vault, worst | daylight, worst | with `--text-strong` |
|---|---|---|---|
| how-it-works | **2.93** at 390, 2.90 at 1280 | 4.61 | 6.21 / 6.14 |
| plain sheet | **2.89** at 390, 2.86 at 1280 | 4.61 | 6.12 / 6.05 |
| win outcome | 3.53 at 390, 3.49 at 1280 | 4.48 | 7.48 / 7.40 |

**The head that was carrying the exception is the better of the two brown heads by 0.04, and the 222
that were not carrying it are worse.** Neither branch the row wrote down fires: the class cannot come
off, and adding it to the others is not an addition but the same mistake with a bigger membership,
because **a class on 105 of 333 discs is a LIST** and this folder has already paid for a list - the
44px touch floor stood in six files as six lists and two of five chips had it. So it is **one rule
keyed to the family**, `dialog.app-dialog .sheet-close:focus-visible{outline-color:var(--text-strong)}`,
in the file that owns the surface, for the reason `course-chrome.css` already writes over its own
ring: **a ring answers to what it stands on**, and what these 333 discs stand on is a sheet head.
`.icon-btn-ring-strong` is deleted from `iconbtn.css` and from **198 class tokens in 195 files**.

The win head at 3.53 would pass without this and takes it anyway. Half a point of contrast is not a
reason, and six discs kept on the other value would be the list again with a different membership.

**TWO NUMBERS IN THE RECORD WERE CORRECTED RATHER THAN QUIETLY REPLACED.** The row's "it goes onto
the other 117" is an arithmetic slip: 222 is the plain-head count, so 327 discs stand on a brass
glow and 333 on a sheet head of some kind. And `dialog.css`'s own 3.76 / 4.58 for the win head is
**the declared recipe computed rather than the page read**: 42 per cent `--result-won` over
`--result-won-stone` gives exactly 3.75 and 4.59, and the head's own green `::after` at `.34` then
lightens that corner to rgb(48,95,65), which costs 0.26. The paint is 3.53 and 4.48. A number that
can only be reproduced by re-deriving it is a reading of the stylesheet and not of the paint, which
is this repository's own rule arriving from a direction it had not come from before.

### 107: the hole does not exist, and the divergence that does is worse than the row thought

The row said the grey tree hides the dock at 640 while the panel arrives at 760, leaving 120px where
a screen cannot be bet from. **The grey panel arrives at 640, in the same four-line block that hides
the dock.** Measured at ten widths on all 16 event-detail documents in both trees, the set of widths
where neither control is visible is **empty on every one of them**.

What is real is the other half. The two trees put the same reflow at two different rungs, so from
640 to 759 the grey tree draws a second column the product does not have - and **halves its own
content column to do it: `.ed-main` 635 to 322.73 in one pixel of viewport, and the chart 569 wide to
255.7**. `DESIGN.md` decides the number by name: 760 is where the event detail gains its second
column, and 640 is "the one divide, below it a single column with a bottom nav and a mobile dock".
So the grey block moves, in all 92 files, **and the WHOLE block moves rather than just the dock,
because moving the dock alone is what would create the hole this row was filed about.** The paint
needs no change. Forcing the paint the other way was measured too and it is the worse trade: the
panel fits at 640, its `min-content` is 274.22, and it leaves a **244px** content column for the
chart, the market block, the tabs and the comments.

**AND THE PAIR TRAP WENT IN THE SAME SWEEP.** `@media(max-width:640px)` in 57 grey files and
`@media(max-width:760px)` in 87 both match on the same pixel as their `min-width` twin, which is the
defect `CLAUDE.md` says this repository has been bitten by twice. Read at exactly 760 the grey footer
trust strip computes one column where the paint computes three. **153 conditions are `639.98` and
`759.98` now.**

### 104: the row argued from the siblings, and the answer is the head directly above

"Every decided body is 16 or 20 and the only 8 is the one nobody decided" is true and is a
comparison between siblings. What decides a body's horizontal padding is the head above it, because
those two edges are the one vertical line a person reads down the middle of a sheet. The bare
`.sheet-body` stands on **115 elements across the painted tree and the kit and every one of them is
`#depositDialog`**, a bare `app-dialog` with no skin, under a head at 24/20/20. **So the title stood
20px in while the amount field, the payment widget, both paragraphs and both full-bleed buttons
stood at 8.** It is `--space-20` now, in both copies of the rule. The gap stays at 8: one change per
element, and the four gaps for one rhythm are filed as 110 with the two 4px insets this leaves
standing.

### The instrument, and it was wrong three times before it was right

**A `<dialog>` WITH NO `open` ATTRIBUTE IS `display:none`, SO 222 OF THE 225 PLATE HEADS LIVE INSIDE
A BOX THE BROWSER NEVER PAINTS.** A full-page pixel diff over all 106 painted screens is structurally
blind to almost every placement of the thing being changed, and it would have reported a clean zero
while saying nothing at all. This is `ui-kit/CLAUDE.md`'s own "a count cannot tell an open dialog
from a shut one" arriving on the measurement side. The real instrument OPENS each dialog with
`showModal()`, reads the computed style of every element in its subtree with the **properties
sorted** (Chrome enumerates custom properties out of a hash map and their order shuffles between runs
of the same page), and screenshots the DIALOG ELEMENT rather than the page.

**Three instrument defects, each caught by the control rather than by a reading:**

1. **The course chrome poisoned it, for the second time in this repository.** The first pass reported
   66 non-zero readings over 47 documents. Running the same tree AGAINST ITSELF reproduced the
   identical box on 28 of those 47: **44 x 44 at `button.rm-toggle`, 26 pixels**, the design-system
   panel's toggle, `position:fixed`, composited non-deterministically into a full-page capture. It is
   not the product. Hidden for the read, and the 220px inset `base.css` writes is keyed to
   `#rmSidebar` EXISTING rather than to its display, so nothing under it moves.
2. **An image that has not decoded is a region that differs, and `document.fonts.ready` does not wait
   for one.** The control then returned **60,671 differing pixels over a 274 x 247 box** on
   `how-it-works.html` at 390, on the same tree against itself: the brand tile in the side column.
   `networkidle` plus an explicit `decode()` of every `<img>` collapses it to 0.
3. **The residual floor is stated rather than rounded away.** After both fixes the full-page control
   still reads **6 non-zero of 376, maximum 46 pixels**, scattered antialiasing on a grain texture.
   The element-level instrument does not have it: control **0 differing rows and 0 differing pixels
   over 124 readings and 3,468 elements**.

**What the clean instrument then said.** Before against after, every dialog opened, 3,500 elements
walked: **the only differing property in the whole tree is one, `outline-color` on the close disc,
brass to white** - which is 106 landing, and which is visible at all because `showModal()`
autofocuses that button, so the ring is live on the first paint of every sheet rather than in a rare
state. The how-it-works head reads **0 pixels** with one element fewer, the deleted glow span. The
plain sheet head reads **0 differing properties** and 357 pixels, and 357 is the perimeter of a 2px
ring at a 2px offset around a 32px disc.

### What was found and not fixed

**109**, the outcome head has this face's anatomy to the declaration and a different ground and glow,
so it shares the skeleton and not the skin and there is no word in the system for that, 10 elements.
**110**, three of the four sheet bodies do not share a left edge with their own head, and after 104
the two that are left are 4px rather than 12: signin 16 under 20 on 110 elements, the how-it-works
body 20 under 24 on 111, and only the outcome sheet aligns. **111**, the close disc on the six
outcome overlays is an `<a>`, and `dialog.app-dialog a:focus-visible{border-radius:var(--radius-6)}`
beats `.icon-btn`'s pill, so the disc **stops being a circle the moment it takes focus** - and
`showModal()` focuses it, so that is the first paint. **112**, the grey tree disagrees with the paint
at three more addresses, and one is `.hiw-btn`, the 88px control `DESIGN.md` records as the reason 73
painted screens scrolled horizontally from 641 to 652; the paint hides it below 760 and the grey tree
ships it down to 320.

The kit is **56 pages and 44 components**: `ui-kit/platehead.html` and the twelfth entry on
`vitrine.html`. `components/` is 52 stylesheets and 7,440 lines.

---

## 2026-08-11 - The product is called Yonder, and its mark was one shape written down twice

**THE NAME.** `Predict Market` was a description of the category standing in the place a name goes.
It could not be searched for, could not be owned, and argued nothing to a user whose documented fear
is "this looks like crypto, so it is a scam". **The product is `Yonder`**: over there, further on,
out where you cannot quite see yet, which is the one thing this product actually sells. Plain
English, no finance in it and no crypto in it.

**What was checked before it was chosen, and what it cost.** Six candidates were carried to a
lockup. `Bellwether` led the set on meaning, the county whose result calls the election, and was
dropped for its mark: the obvious drawing is a bell, and the header already carries a notification
bell 44px from the logo. `Callit` was the best-sounding of the six and is **taken in this exact
category**, callitmarket.com. `Augur`, `Omen`, `Oracle` and `Delphi` are all live in prediction
markets. `Stake` is unusable on its own because stake.com is a casino and the adjacency alone
contradicts the trust position. `Yea` was the sharpest idea and was **refused on a system rule**: the
brand would be standing on one of the two outcomes, and green and red belong to YES and NO while the
brand stays brass. A name that quietly breaks a load-bearing rule is not a name that got away.

**THE MARK IS A FORK.** A line rises, splits, and one branch is lit while the branch not taken stays
at 30 per cent: the event, the two outcomes and the choice, in two strokes. Butt caps and a mitred
shoulder, so it reads as cast rather than drawn. **With this name the same shape is also the Y**, so
the mark is a monogram and a fork at once and has to be explained as neither. It replaced an
up-trend tick, which is the mark every prediction market in the category already has.

**Ten candidate marks were generated as vectors and none of them shipped.** They came back in gold
rather than brass, with gradients, stray inner lines and silhouettes that dissolve under 40px. Two
were worth the run as ideas, an ingot and a keystone, and the seven cuts that followed were drawn by
hand against the system's own geometry. **A generator is an idea source and not a drawing**, which is
the same finding this repository has already written down about measurement machines, arriving from
the other side.

### The defect the rename uncovered: one lockup, two files, and only one of them could be themed

`header.css` and `footer.css` each drew a mark before a wordmark, and the two were not the same
thing. The footer's read `--mark-logo` and followed the theme. **The header's carried its own inline
data URI with `%23c99e3f` typed inside it**, and a colour written inside a data URI is a value no
custom property can reach, so on all 105 painted screens in daylight the header wore the night
theme's brass while the footer beside it wore the deep bronze. Nothing looked broken: the two marks
are a page apart, and a mark that renders is a mark nobody re-reads.

**So the lockup is a component now**, `components/logo.css`, level 1, imported above both shells
because both hold it. It owns the FACE: the mark, the gap, the display face, the size, the tracking,
the ink, and the reset that makes a `<button>` in the header and a `<span>` in the footer render
identically. It owns nothing about WHERE it stands: the padding that carries the touch target and
the press ground stay in `header.css`, the centring stays in `footer.css`. **The reset is part of the
face rather than of either place**, because the two elements do not start from the same place and
would have been one face only for as long as nobody put them beside each other.

Two more rules died with the move, one per file: `::first-letter` set the ink to exactly the value
the element already inherited, in both copies. **It rendered nothing and read as a decision**, which
is worse than either.

**Measured after, in a browser, at 390 and 1280 in both themes**: both marks resolve to
`#c99e3f` on graphite and `#684f18` on chalk, the box is 18x18 in all four readings, the face is
Space Grotesk 700 at 16px with an 8px gap in all four, and page scroll is 0. The mark is carried
twice on purpose in `tokens.css`, `--logo-y` and `--logo-y-dark`, because a data URI can only be
themed by having a second one, and the two are edited together.

**The sweep**: 711 occurrences of the old name across 106 painted screens, 387 across the grey tree,
52 in the kit, 38 in `ia/`, 8 in `voice/`, plus one address that spelled it as a host. `docs/` was
not swept and neither was `ui-visual/old/`: **a record says what was true when it was written**, and
28 archived pages were reverted after the first pass caught them. The grey tree took the copy and not
the class, because it links no system stylesheet and a system class there would be a promise nothing
keeps. The script was written in the scratchpad and deleted.

The stand: `ui-kit/logo.html`, `ui-kit/vitrine.html#logo`, and the row in `ui-kit/docs/inventory.md`.
The kit is 55 pages and 43 components.

---

## 2026-08-11 - A component is not named after one of its places, and 818 controls were two controls each

**EIGHT ROWS CLOSED, ONE ANSWERED IN THE OTHER DIRECTION, SIX OPENED.** 15 and 18 were one edit and
it is made. 87 is reconciled and took three defects in the paint with it. 89 is done in all three
trees with the system widened first, and it carried 96 and 97. 101 and 102 went with them. **98 is
answered and the rename it asked for is refused rather than deferred**, which is written out below,
because a row talked out of its own plan has to say why.

### The instrument was wrong three times before one number about the product was believed

**A CONTROL THAT READS ZERO ON AN UNCHANGED TREE IS THE ONLY THING THAT MAKES A COMPARISON WORTH
READING.** Three defects were found in this session's own instrument, and each one has the same
shape: a value the measurement was choosing without saying so.

- **Chrome enumerates an element's custom properties out of a hash map.** The 78 `--tokens` on an
  element come back in a different ORDER on two runs of the same page while every value stays put.
  Unsorted, the control read **28,234 differing rows of 28,258** on a tree nothing had touched. The
  rows are sorted before hashing.
- **`localStorage` is per ORIGIN and shared by every page in a browser context.** The harness set
  `pm-theme` only for the light pass, so a worker that had measured one light page rendered every
  later DARK page in daylight. **Six `.dark` files read as light**, in the after pass and not in the
  before pass, because the two runs spread pages over workers differently. It is written for both
  themes now, which is the same lesson as the touch pass that measured the product with a mouse: an
  unasserted condition is a value the instrument picked.
- **`getComputedStyle` resolves `url()` to an ABSOLUTE url.** Comparing against HEAD means serving
  HEAD from a second port, so the same page differs in every `background-image` it has: **86 of 322
  files read as differing on one property, the port number inside
  `url(.../trust-column-full.webp)`.** The origin comes out of every value before hashing.

And a fourth reading that was not a defect and had to be told apart from one: **two browser fleets
running at once produce transient sub-pixel differences that do not repeat.** 87 files differed on
the concurrent run; re-measured serially with the origin normalised, **87 of 88 were identical and
the 88th was identical on a third reading**, with the same tree measured twice against itself
returning 0. A number that moves when nothing moved is a reading of the instrument.

### 15 and 18: one block, two hosts, and ten rules that were about neither

`hiw-dialog.css` held three things and was being read as one component, which is why its level was
the last in the kit that had to be DECLARED: not because the arithmetic read too low, but because
nobody could say what the component WAS.

**The cut is 10 rules out and 34 staying together**, and it is the same cut both rows arrive at from
opposite sides. The ten are about being a dialog: the sheet's width and its clip, its body as the
scroll container and that body's padding, and the brass link out to the full guide with its arrow,
its hover and its press. **107 elements, every one inside a sheet, and `.hiw-full` cannot stand on
the page at all, because the page IS the full guide.** The file is `components/hiw.css` now, 134
lines, and the name went with the rules: a dialog is one of the places this block can stand and a
component is not named after one of its places. `dialog.css` gained `.hiw-arrow`, `.hiw-body`,
`.hiw-dialog` and `.hiw-full` on its `Classes:` line and `--text-on-brass` on its `Reads:`, which is
exactly the one role `hiw.css` dropped.

**A stale objection went with them rather than being left standing.** `dialog.css` carried a
paragraph saying `.hiw-body` must not come here because `coverage.md` is computed and would
disagree. `coverage.md` is in `docs/kit-archive/`, is read by nothing, and the generators that
computed it were deleted with the vitrine on 2026-08-07. **An objection whose instrument has been
deleted is not an objection, it is a fact about a tree that no longer exists**, and it kept a
dialog's own rule out of the dialog's own file.

**Verified: 0 differing rows.** 161 documents x 2 themes, the three rungs and one pixel either side
(389/390/391, 639/640/641, 759/760/761, 899/900/901, 1279/1280/1281), `#howitworksDialog` opened by
`showModal()`, animation and transition frozen, layout settled, the cold pass thrown away, the tree
at `018a721` in a git worktree on a second port. 314 files in the strict set, **599,370 rows on the
first comparison and 194,700 on the re-measurement, 0 differing on both**. Four files changed by
intent and say so: `dialog.html` gained the fourth-variant section, `hiw-dialog.html` is `hiw.html`.

### 87: the grey tree was behind its own contract

The painted mobile dock CHOOSES and raises a sheet; the grey dock CONFIRMED a stake the user never
entered. **The sheet is not a paint invention.** `ia/docs/sitemap.md` and `wireframes/_conventions.md`
have both specified "a bottom dock that expands to a sheet on mobile" since before either tree was
built; the grey file's own HTML comment says so directly above a dock that did not do it; and the
grey stylesheet has carried `.bet-sheet .bp-amount-row` with **0 elements wearing it** the whole
time, which is the sheet's outline left behind after the markup was never written. So the grey tree
came up to its own contract on the four screens that diverged, and the four bet-state screens were
left alone, where the confirmer is correct in both trees.

**Three defects in the paint went with it**, all found by reading the two trees against each other:
the sheet's Confirm called `showModal()` on the sign-in dialog unconditionally, so on the screen
where the bottom nav renders a balance a signed-in person confirmed a bet and was asked to sign in;
the binary sheet read a `$0.20` fee against the panel's `$0.40` five lines above it, a survivor of a
template whose label used to say "only if you win"; and `YES selected` was the one string in that
block with no row in `voice/docs/microcopy.md`.

### 89: the button became the anchor, and three of the properties were the element's own defaults

818 buttons wrapped in an anchor: 326 grey, 324 painted, 168 kit, on 77 screens per product tree.
An anchor's content model is transparent with one prohibition and interactive content is the
prohibition, so a screen reader announced a control that was two controls and every one of them was
two tab stops on one visual object.

**THE SYSTEM WENT FIRST AND NOTHING WAS DELETED UNTIL THE MARKUP HAD MOVED.** 24 widenings across
`base.css`, `button.css`, `tabs.css`, `yesno.css` and `dialog.css`, every one a strict superset, and
nine wrapper-only rules deleted afterwards once `a > button` read **0 in all 264 documents**. That
order is `yesno.css`'s own record of what removing a selector half early costs: four screens shipped
a YES with no colour.

**THREE PROPERTIES WERE THE `<button>` ELEMENT'S OWN DEFAULTS AND NOBODY HAD WRITTEN THEM DOWN.**
`.btn` had no `text-decoration`, so 166 controls would have taken the User Agent's underline;
`.yesno` and `.tabs` had no `text-align`, so 614 labels would have gone left the moment the button
stopped centring them; `.tabs` had no `display`, so the row would have collapsed to its own text the
way `navitem.css` records from 2026-08-07. **That is the third time this system has paid for the
same discovery**, after `.chip` and `.icon-btn` on the same day last week.

**And the grey tree is a second half nobody had counted.** It links no stylesheet at all: 104 inline
`<style>` blocks and **1,605 occurrences of a selector keyed to the tag**, of which seven reach these
controls. Widening `components/` protects 90 of 264 documents and none of the other 104, so eight
grey rules had to move in 103 files before a single grey element could.

**F5 was not a mechanical unwrap.** `role="tablist"` requires its owned elements to be tabs; here the
tabs were one level down inside the links, so the tablist owned nothing on 9 screens per tree. Two
more things were true at once: there is no `role="tabpanel"` anywhere in that family, so the tabs
controlled nothing, and they navigate to another document, which a tab does not do. Moving the role
up would have fixed the ownership and left a tab with no panel that leaves the page. **The roles came
OFF**, the container is a `<nav>` so its label still names something, and the state is
`aria-current="page"`, the idiom this product already writes 1,228 times.

**One consequence is worth stating because it is the grey tree working as designed**: the wireframe
stylesheet outlines every landmark, `header, nav, main, section, article, footer, aside`, so the tabs
row gained a 1px box and the page 2px. A row that became a navigation landmark gets a landmark
outline. And on the painted 404 the only pixels that moved were **385 of them inside a 72 x 9 box**,
the label of one control, at a maximum channel delta of 34: the same text re-antialiased because it
is laid out in a flex container now instead of inside a `<button>`. The control's box is identical.

### 96 and 97, which ran on whichever element survived

**96's population is 100 per product tree, not 104.** Read from real element trees rather than by
regex: 50 `.opt-row` on 14 screens per tree, 100 controls, 38 rows and 76 controls in the kit. The
name is built out of what is already written: `aria-labelledby` takes a LIST of ids, so pointing at
the outcome span and then at the control gives **"Sweden YES"** with the wording staying in the one
place `voice/docs/microcopy.md` owns it. An `aria-label` would have been a second copy of every
outcome name in the markup, and a second copy is what drifts. 0 duplicate ids and 0 dangling
references over 264 documents. The accessibility tree on `event-feed.html` went from **32 links
containing a control and 30 bare YES/NO names to 0 and 18**, and the 18 that are left are the feed
card's own pair, which is a different question and is row 103.

**97's destination is the screen the overlay is invoked over**, which is the rule the six controls
that already agreed were following. Eleven pointed at `event-detail.html` in grey and
`event-feed.html` in paint; they point at `event-detail.html` in both now. **And the name stops
saying Close**, because on these pages there is nothing to close: the page IS the overlay. It is
`Back to the event` and `Back to My Bets`, 34 controls over the two trees. The 105 in-page dialogs
keep `Close`, because theirs is a button that closes.

### 101 and 102

**Two of row 101's eleven were not missing specimens at all: they were specimens that dropped the
anchor.** `ui-kit/betpanel.html` shipped the confirmer's Confirm bare where every screen wraps it,
and `ui-kit/dialog.html` shipped the deposit body without either of its two trailing controls, which
is why `dialog.app-dialog .sheet-body>a` had no stand anywhere. That is the card with its photograph
left out and the dialog shown shut, a third time: **a specimen with one element missing looks
finished.** Two more were the second half of a rule whose first half already had a stand.

**102 deleted five rules that reach elements and decide nothing**, and the consequence is not
cosmetic: three of them were the only reason `.skeleton`, `.w40` and `.w70` were on `position.css`'s
`Classes:` line, and the only reason its `Stands on:` said 36. By the classes it owns it stands on
**23**, and the 14 screens in the gap carry no position at all.

### 98: the row asked for a rename and the answer is four numbers and a refusal

Re-measured after the cut, with both sheets open on one page in both themes, 823 computed properties
per element: **the head is 812 of 823 identical, the pattern 822 of 823, the glow 813 of 823 and the
body 813 of 823.** The row's five differences are six.

Four are settled, each to the value the FAMILY agrees on rather than the one written first. The
radial stop goes 92 to **96**, because two rules and 434 elements say 96 and one rule and 196 say 92,
and the win head says 96 as well. The pattern opacity goes .24 to **.2**, because an opacity answers
to the GROUND under it, the outcome head has its own ground and its own .16, and this head has the
plain head's two roles exactly in both themes. The glow goes to **210 / blur 42 / .42 / 60 per
cent**: the 224 was a compensation for a wider sheet, holding the wash at 37.2 per cent of a 462px
head against 37.8 of a 418px one, and at **18.7 per cent** on the 922px page hero. A compensation
that fails on the block's other host is not a compensation, it is a second number.

**The rename is refused, and it is refused rather than deferred, because it moves the duplication
instead of removing it.** The head's paint is six rules, written once and drawn by one class in both
of the block's hosts. Rename the sheet head to `.sheet-head` and those six live in `dialog.css` for
the sheet, while the page hero, which is not and cannot be a `.sheet-head`, has to have them written
again. That is a duplication against the plain sheet head traded for a duplication against the page
hero, at a cost of **1,004 class tokens across 195 files** measured with whole-token matching (a
`\bhiw-hero\b` regex returns 268 in `ui-visual` where the true count is 106, because `-` is not a
word character). What it actually is: **one FACE worn by three heads under three names**, at 418, 462
and 922 pixels. The system already has that move and has written it down, a skin belonging to a
SURFACE rather than to a component, with the header band as the precedent. It is row 108, after row
105 gives the page hero a name of its own.

### What was swept and what it read

Every sweep was a throwaway script in the scratchpad, run once and deleted. **264 documents at
389/390/391, 639/640/641, 652, 759/760/761, 899/900/901 and 1279/1280/1281: 4,224 renders, 0
horizontal scroll, 0 console errors.** `a > button` 818 to 0. `role="tab"` inside `.tabs` 40 to 0.
Duplicate ids 0, dangling `aria-labelledby` 0. Every href on every page is the href that was there
before, multiset for multiset, so the navigation the wrapper was doing is the navigation the anchor
does now.

## 2026-08-10 - A comment is not inert, and a divider keyed to a tag name had never once drawn where it was needed

**THE LARGEST THING IN THIS ENTRY IS A DEFECT THIS SESSION PUT THERE ITSELF, ONE COMMIT EARLIER.**
The note written into the header of `components/yesno.css` on 2026-08-10, recording that the outcome
pair is told apart by a class rather than by DOM order, was closed with a comment terminator of its
own. That left the file's `Reads:`, `Stand:`, `Stands on:` and closing lines **outside any comment**,
and CSS error recovery discards a bad construct up to and including the next block: the parser
swallowed those four lines together with the rule that followed them. **`.yesno` lost `display:flex`,
its `gap` and its bottom margin.** Measured before and after over the 122 documents that carry the
class, at 390 and 1280, control 0: **438 readings computing `display:block`, and on the feed cards
the YES / NO pair was stacking VERTICALLY**, two full-width buttons at 278x44 each where the design
is two at 135x44 side by side. On the compact pair the container measured 89 wide against 97.

It shipped in `bad47ec` and it was live for a day. **Nothing that reads the source could have found
it**, because the source says `display:flex` and says it in the right place; nothing reading a
screenshot would have called it wrong either, because a stacked pair of outcome buttons is a
plausible drawing. It was found by a pass counting screens per component that read the **CSSOM** and
noticed a declared rule that was not in it. The repair carries its own second lesson: **the first
attempt at the repair note quoted the terminator, which closed the comment again.** A note that has
to name the marker names it in words. Every stylesheet was then re-read the same way: **0 header
lines outside a comment and 0 stray markers across 51 files.**

**AND THE SAME SHAPE, ONE LAYER OUT, IN `seo-plate.css`.** Backlog 62 said 22 `.feed-seo` sections
and 14 divs carry identical prose, and that a `<section>` with a heading is a landmark while a
`<div>` with one is a heading in the middle of nothing. Both halves needed correcting. **A bare
`<section>` is not a landmark either**: it maps to `generic` until it has an accessible name, so the
element and the name move together or nothing moves. All 14 are on **one screen**, `ui-visual/
terms.html`, they are the clauses of the Terms document, `wireframes/terms.html` does not exist, and
each already carried the `id` its table of contents jumps to. They are `<section id aria-label>` now,
the label taken verbatim from the clause's own `<h2>`, which is what the 43 painted sections beside
them already do. After: 57 sections in the painted tree, **0 unnamed**, 14 landmarks on the one
screen where jumping between clauses is the whole point, and **0 of the 14 table-of-contents targets
broken**. The kit's four unnamed specimens on `seo-plate.html` took the label too.

**THE ELEMENT CHANGE MOVED 15px AND THAT IS WHAT FOUND THE REAL DEFECT.** `.feed-seo` carried a
`border-top` divider with `.feed-seo:first-of-type` taking it off the first block, and
**`:first-of-type` does not mean first in the stack: it means first among siblings with the same tag
name**. On the nine feed screens every block is a `<section>` and the first is also the first
section, so the rule fired and nobody looked again. On `terms.html` the same blocks were `<div>` with
a `.protect` div above them, so it matched **none** of them: the first clause of the Terms document
drew a divider above it with nothing above to divide from, and lost the stack's 28px lead-in at the
same time. `:first-child` is not the repair either, measured: the first block is the first child on
9 screens of 11 and is not on the other 2. **A divider goes between two blocks, so it is written
between them**, `.feed-seo + .feed-seo`, which asks the actual question and is right whatever tag
anybody reaches for next. Same species as the outcome pair told apart by DOM order. After, over the
14 documents that carry the class at 390, 760 and 1280 with a control of 0: **every screen has
exactly n-1 bordered blocks and the first has none**, and `terms.html` is the only document that
moved.

**THE EIGHT ERROR BLOCKS ARE ANNOUNCED NOW, AND THE TWO AXES STAYED TWO.** Backlog 24 and 25.
`.inline-error` stands on the same 8 screens in both trees plus 4 kit specimens, every one a bare
`<div>` with no `id`, so nothing could point at it: `aria-invalid` 0 of 105 and `aria-describedby` 0
of 105. **(a) FIELD-BOUND, 2 screens.** The message is about a field a person is typing in, so the
block takes an `id` and the field takes `aria-invalid="true"` with `aria-describedby` at it:
`deposit-minimum-not-met` and `event-detail-bet-insufficient`. Both screens carry a SECOND
`.amount-input` inside a closed deposit dialog and it is untouched; they are told apart by value and
by class, and the sweep asserted exactly one match per screen before writing. **(b) STATUS, the other
6 plus the kit's 4.** Nothing is wrong with a field, the block is the RESULT of an action, so the
block itself takes `role="alert"`. They are not both, deliberately: a described-by target that is
also an alert is read twice. **24 edits over 18 documents**, verified from the rendered page rather
than the source: `role="alert"` on 16 blocks, `aria-describedby` resolving to a real element on 2 of
2, and the field's own `validity.rangeUnderflow` true on the one that is under its minimum.

**AND THE FIELD'S GUARD WAS WRONG ON THE OTHER RAIL, WHICH IS ROW 94 ONE SCREEN OVER.** Row 94 took
the 35 bet fields from `min="0"` to `min="1"` when the $1 minimum was decided. The deposit rail was
not looked at: **217 fields carried `min="0"` beside a visible `Minimum $10` on 134 screens**, and
`PRODUCT.md` has said the deposit minimum is $10 since the same day. `min="10"` on all 217, over 210
documents. The withdraw field and the kit's two unscoped specimens keep `min="0"` because no rule
names them.

**WHICH MADE ROW 65 WORTH WRITING PROPERLY, BECAUSE `min` IS `pattern` ARRIVING A SECOND TIME.** The
row asked for one line of contract at handoff. What the attribute buys is a validity STATE:
`:invalid` matches and `validity.rangeUnderflow` is true, and **nothing consults either**, because
this product still contains **0 `<form>` elements** and no page script calls `checkValidity()`. It
does not stop a person typing 4. Measured by TYPING rather than by assigning, which are two different
paths through the value sanitiser and only one of them is what a person does: `abc12` gives `12`,
`1.2.3` gives `1.23`, `+5` gives `5`, **`-5` gives `-5`**, **`1e5` gives `1e5` and is VALID**, and
**`5e` gives the empty string with `badInput` true**. That last one is item 95 in a new costume: the
field shows two characters and reads as nothing, and only `badInput` can tell it from a field nobody
touched. The contract is two lines now, in `components/input.css` and on `ui-kit/input.html`: **digits
and at most one dot, no exponent, no sign**, and **read `badInput` before reading `value`**.

**THE SECOND ALPHA LADDER IS GONE AND WHAT LOOKED LIKE THE REST OF IT IS A DIFFERENT OPERATION.**
Backlog 14 said 20 declarations build a colour with `color-mix` at 16 percentages beside the declared
`--brass-a*` one. Counted today: **0 `color-mix` on `--color-action` ends in `,transparent)`**. What
is left is 34 mixes of which 28 end in a SOLID, and **an alpha and a blend are not the same thing**:
an alpha is one ink at a depth and belongs on a ladder because the ground is whatever the element
stands on, while brass mixed into `--bg-control` at 11 per cent IS a ground, and the number that is
right depends on the surface being tinted. A shared ladder there would be a rung fitted to one
surface and applied to another. The six that do end in transparent are three other roles, one
gradient each, and three values inside one gradient are not steps.

**`50%` IS THE SIXTH CORNER SHAPE AND IT IS LEGAL ON A SQUARE.** Backlog 43, the shape half. On a
square `50%` and `--radius-pill` draw the same circle; on a rectangle one is an ellipse and the other
a stadium, so the rule is the box and not the value. Read from the paint at 390 and 1280 across six
screens: **all 7 in `components/` stand on a box whose two axes are equal, 0 on a rectangle**, so the
ambiguity the row was filed for does not arise anywhere. Written beside the radius ladder so the
first rectangle to reach for it is caught rather than counted. The row's other half, 81 raw px that
are genuine layout dimensions, is Responsive's and stays open.

**ROW 52'S PREMISE WAS RIGHT ABOUT THE TREE AND WRONG ABOUT THE REPAIR.** Sixteen component headers
say the painted tree is 105 screens and it is 106. Measured from the rendered DOM of all 106, per
screen and not per occurrence, with a control of 0 over 465 distinct classes: **15 of the 16 are
correct.** Every product component stops at 105 and the one it misses is the same each time,
`overview.html`, a contact sheet carrying no product chrome at all. The sixteenth,
`course-chrome.css`, is the only file here standing on all 106. Two other headers were wrong for a
different reason and **both were a shared class counted as a placement**: `oddsbar` said 9 and stands
on 21, because the header counted `.ed-oddsbar` and missed `.oddsbar` on twelve feeds; `seo-plate`
said 11 and stands on 9, because `.feed-seo` is declared by `patterns/browse-shell.css` too, as the
SLOT, and on two screens the slot is there with no plate in it. **Three headers edited, aggregate
error 15 screens.** Under the naive reading, counting every declared class including the shared ones,
9 headers would read as wrong and the error would be 315, and the gap between 15 and 315 is exactly
what the row meant by "cannot be fixed by substitution". `.footer-soon` was painted by `footer.css`
and missing from its own class list, and is in it now.

**`.fine` IS A PART AND THE PART BELONGS TO `dialog`, AND THE QUESTION HAD A NUMBER NOBODY HAD
TAKEN.** Backlog 19 said it is a typographic role rather than a part of the dialog. Measured over the
106 painted screens with every dialog **opened**, which is the whole difficulty, because 216 of the
placements sit in one that is shut at load and a computed-style pass that skips them reads 27
elements and reports 248: **248 placements, 239 inside a `<dialog>`, 9 not, and deleting the one bare
rule changes exactly those 9.** The role governs nine elements and the dialog governs the other 239.
What decides it is what the system already does rather than a preference: **all 66 purely typographic
classes here live in the file of the block they are part of**, there is no `components/
typography.css`, and the closest twin is `.field-label` in `input.css` at 245 placements in the same
five containers, which nobody has ever proposed a type file for. The threshold for a class no
component owns is three files or more, compounded onto each owner's own class rather than written
bare, which is what `.sel` is in seven; this is written by two, and the second is `betpanel.css`
restyling what it contains. **Three of the row's supporting facts had expired**: its count (246 was
right on 2026-08-02 and the tree has said 248 since 2026-08-03, and `ui-kit/dialog.html` already said
so), its "only one file writes it", and its "three rules name another container", which is one rule
and that rule decides nothing.

**16d WAS FOUR ROWS, NOT FIVE, AND ALL FOUR ARE ONE COMPONENT.** `account` stopped being a row on
2026-08-08 when row 63 deleted the file, its import, its shelf section, its inventory row and its kit
page together. **And the machine all of them were opened to protect is gone**: every one was filed
because the level arithmetic had to work around it, `ui-kit/_levels.py` went with the other 62
scripts on 2026-08-07, and that was verified independently of the prose rather than taken from it.
So none of the four splits would change a level, a cascade order or a rendered pixel, while each
would still cost what item 17 cost. **Each is therefore closed with the sentence that closes it, in
its own file**, because this repository's rule is that a rule with no reason is a rule somebody
argues away: `card` is one component with two contents, 63 binary holding `.yesno` and 21 multi
holding `.options` out of the same fourteen classes; `notice` is six faces and one job, and **0 of
them hold a control except the permission banner, which holds two of `button`'s**, which is that
page's own rule proved rather than asserted; `position` is one row in three arrangements, and the
list already left to `patterns/position-list.css` with 16a; `filters` names `toggle` as its second
component and **the toggle left on 2026-08-05**, so the row was describing a file that had stopped
existing in that shape.

**AND A SELECTOR NAMED A CONTROL THIS PRODUCT DOES NOT HAVE.** `filters.css` hid its inputs with
`.filter-panel input[type=radio],.filter-panel input[type=checkbox]`, and the second half matched
**0 elements on all 106 painted screens and all 54 kit pages**: there are three checkboxes in the
whole product and all three are on `cookie-consent.html`, none in a filter panel. Every input in
every filter panel is a radio. The paragraph above the rule said "the sort radiogroup and the
category checkboxes", so the rule and the prose that justified it named the same thing that is not
there, and both are corrected rather than one quietly deleted. Verified after: `ui-kit/filters.html`,
`cookie-consent.html`, `my-profile.html` and `event-detail.html` all read **0 changed elements** at
both widths with every `<details>` and `<dialog>` opened, control 0, and the 16 filter inputs on the
feed are 16 radios with 16 still hidden. **A selector that matches nothing agrees with every
hypothesis**, which is the same trap the survey met one layer down: a `deleteRule` sweep over
`document.styleSheets` reaches nothing in this system, because every component sheet is an `@import`
living on `CSSImportRule.styleSheet`, and its first run reported "0 removed, 0 pages differ" for
every rule tested, which reads exactly like proof that the rules are inert. Recursed properly it
removed 318 to 530 instances a pass. **Always print what the instrument removed.**

**THE LAST UNREAD SURFACE WAS READ, AND MORE THAN HALF OF WHAT THIS PRODUCT SHIPS IS ARTWORK.**
Backlog 5, open since 2026-07-28 and never a defect list: it named a place where a bug would be
invisible because nothing had ever looked. 106 painted screens, 390 and 1280, both themes, 424
renders per pass, 16 passes, against a FROZEN copy of the tree because the live one was under edit
throughout and **the control caught it moving**, +7,431 bytes on every one of the 424 renders, all of
it stylesheet. **1,367,334 bytes and 58 requests per screen on a cold cache, 48.4 per cent of it the
same bytes every time.** The split is image **53.0** per cent, stylesheet 37.5, font 4.5, document
3.7, script 1.4.

**THE EVENT PHOTOGRAPH IS 1600 x 1073 AND IT IS DRAWN AT 56 x 88.** Four JPEGs totalling 1,158,832
bytes, and the box measured in a browser is 56 x 88 at 390 **and** 56 x 88 at 1280. **That is not a
`srcset` problem and calling it one would send the fix the wrong way**: the box does not change with
the viewport, so what is wanted is one correctly sized asset rather than a set of them. The painted
tree carries 0 `srcset` and five `<img>` elements in total; everything else is a CSS background, and
the event photograph is one of the three things the rules allow on a `style=` attribute, so the 111
inline background declarations are correct and are not the finding. **And the footer decoration is
encoded at eighteen times the density of the one photograph that was exported properly**: three
640px webp totalling 646,804 bytes painting into a 137 x 94 box at `opacity:.5` behind a mask, which
is 0.72 to 0.92 bytes per pixel against `hero-capitol.webp` at 1400 x 788 and **0.041**. The proof
that the strip is the payload is a screen: `overview.html` is the only one without the trust strip
and it is 608 KB lighter than the next lightest. Row 99.

**THE STRUCTURAL LAYOUT SHIFT IS 0.0000 AND THE ENTRANCE ANIMATION CONTRIBUTES EXACTLY 0**, which is
worth writing down because the animation was the prime suspect and this repository has already paid
once for believing it: the 3,587 differing rows that turned out to be entrances caught mid-flight.
**Every shift that exists is the font.** 616 of 616 shift entries landed at or after the moment the
delayed face arrives; the sum before it is exactly zero. `font-display:swap` on all 8 faces and the
behaviour is FOUT and never FOIT, proven by ink painted at 60 to 90ms while `fonts.status` still read
loading. The swap **moves a median 70 per cent of the laid-out text**, 3,488 elements of 6,492, and
the document height moves 20 to 21px on the feed and the detail. It is late enough to be seen because
**0 of 106 screens carry a `<link rel="preload">`** and the face is discovered three levels down, and
because there is no `size-adjust` and no `ascent-override` anywhere, so the fallback is not
metric-matched.

**AND THE AMPLIFIER LIVES AT ONE WIDTH, WHICH IS THE RUNG LESSON ARRIVING ON A NEW AXIS.** 17 screens
open `dialog#outcomeDialog` with `showModal()`. At 390 the sheet fills the viewport, so when the swap
shrinks its content the modal RE-CENTRES and the whole sheet moves with an impact fraction near 1.
Mean CLS at 390 is **0.0260 for those 17 and 0.0004 for the other 89, a factor of 65**, worst
`sign-in-error.html` at **0.2050**; the same document at 1280 reads **0.0002**. An audit reading only
1280, or averaging the two widths, would report nothing. Theme changes none of it: 390 dark and 390
light both sum to 0.4793. Row 100. **The warm-cache control was not 0 and the cause was found before
the number was quoted**, a race between applying a cached face and first paint, nondeterministic, and
it is recorded rather than counted.

**A SAFE FIELD STOPPED BEING A PROPERTY OF THE DRAWING, AND NOBODY HAD RE-READ IT.** Backlog 30.
The rule is that a mark keeps 2 modules of its 24-unit cell clear of ink. While the stroke was 2.2
USER UNITS it scaled with the box, so half of it was 1.10 modules at every size and each mark had ONE
field. `vector-effect:non-scaling-stroke`, taken on 2026-08-10 to close row 29, makes 1.65 a SCREEN
width, so half of it is 0.825px, which is **1.65 modules in a 12px box and 0.90 in a 22px one**: the
same drawing now has a different field at every size it stands in. Measured by INK rather than by the
path, painted at device scale 10 and summed by opaque pixel over the eleven stroked marks, at 12 / 16
/ 18 / 22: close and chevron 4.20 / 4.65 / 4.80 / 5.02, six marks at 3.20 / 3.75 / 3.87 / 4.04, the
tick at 2.20 / 2.70 / 2.80 / 3.05, and **menu and send at 1.20 / 1.65 / 1.87 / 2.07**. So **two marks
fall inside the rule and only below 22px**, and they fall together because both paths sit 3 modules
from the edge. The row named one and its number, 1.9, is the 18px column: **right for one box of four
and blind to the second mark**, which is what a single figure does to a quantity that has stopped
being single. **The rule is restated on the PATH and not on the ink**, because the path is what a
person draws and the overhang is arithmetic anybody can redo, and on that reading all eleven clear 2
with the smallest at 3, so nothing is redrawn. What is left over is a different question and it is
named rather than answered: a 12px mark carries the same 1.65px of ink as a 22px one, so it reads
heavier and stands nearer its own edge, and whether a 12px stroked mark should exist is optical
sizing's to decide.

**THE PROOF FOR THE WHOLE PASS, TAKEN AT THE RUNGS AND ONE PIXEL EITHER SIDE OF EACH.** 160
documents in `ui-visual/` and `ui-kit/`, twelve widths, both the tree at `bad47ec` and the tree
after: **360, 390, 639, 640, 641, 652, 759, 760, 899, 900, 901, 1280**, which is every rung, the
pixel below it and the band that once put 73 screens into horizontal scroll. **1,920 renders per
tree. Horizontal scroll 0 before and 0 after, page errors 0 before and 0 after, 0 introduced and 0
removed.** So the `.yesno` restoration moved the layout of 122 documents, put a stacked pair of
buttons back on one line across every feed card, and cost nothing at any width. The element-level
comparisons behind each finding above were taken separately and each one proved its own control
first: 0 of 8,744 rows on the aria pass, 0 on the `.feed-seo` pass over 14 documents at three
widths, 0 on the `.yesno` pass.

**THE COMPONENT-BOUNDARY ROWS THAT WERE ALREADY ANSWERED AND NEVER STRUCK.** 16a: all five
compositions are in `components/patterns/` and have been since the patterns step, six files; the page
frame keeps the plate that `.feed-inner` and `.ed-main` stand on, deliberately, and
`patterns/detail-shell.css` already says so in its own header. 16c: `.tc-page` is in `base.css` with
its reason and `toast.css` carries the pointer. Both are item 74's shape again, a fix that landed
with its row left open. 16b is the one that needed work and it was a page rather than an edit:
`ui-kit/patterns.html` carries **the register of what stands below the threshold** now,
`.ptab-panel` at 2 screens and `.read-col` at 1, with the reason the threshold counts SCREENS and not
occurrences.

---

## 2026-08-10 - An error is an object and an empty is an absence, and the stand for trust was showing three claims nobody ships

**13 WAS TWO ROWS AND ONE OF THEM WAS FREE.** The row read, in full: "Error state vs empty state are
not differentiated. Two different situations reading as one block." Surveyed independently first,
then measured: `.state-block` stands on **38 painted screens, 15 empty and 20 an error**, and the two
differ in the MARK, the HEADING and the ACTION LABEL and **in nothing else** - same ground, same
edge, same radius, same padding, same brass mark ink, same title and body ink. The words already
carry the whole difference and `voice/docs/microcopy.md` sets it as a rule: every empty reads "No ...
yet", every error "Couldn't ...".

**The literal half of the row was the silent one.** **30 of the 38 blocks carried no `role` at all**,
so for a screen reader the two situations really were one block. `role="alert"` on the 21 errors,
`role="status" aria-live="polite"` on the 16 empties, in both trees, which is what the eight that
already had one were doing. `event-detail-resolved` is left alone in both trees because it is neither.

**The face is the error toast's, verbatim, and that is the point rather than a coincidence:** the
same failure should look the same whether it arrives as a toast or as a page.
`.state-block.state-problem` takes `--bg-control`, `--border-notice` and `--bevel-notice`, with the
mark and the message at `--text-primary` and the message semibold. `--border-notice` is declared in
`tokens.css` as "the neutralised error toast, warm grey, **never red**", which is the only way to
raise an error in a product whose one rule is that red means NO. **No new token and no new colour.**

**It is written AFTER `.cat-main .state-block`, and that placement is the design.** That rule takes
the box away, because a feed with nothing in it should read as an empty page rather than as a card
about emptiness. Both selectors are (0,2,0), so source order decides, and an error is the one case
where the box comes back. Written before it, the modifier would have rendered nothing on the feed
errors, which are most of them.

**Measured after, both themes**: 21 problem blocks, ground rgb(36,40,47) and edge rgb(90,84,74) in
graphite, rgb(252,250,244) and rgb(172,170,164) in daylight; the message ink goes **6.85 to 12.01**
in graphite and **7.41 to 15.78** in daylight; the 17 empties unchanged and boxless; overflow 0 and
page errors 0 over 264 documents. **The survey's own counter-argument was answered rather than
ignored**: it said a ground modifier reintroduces the card exactly where errors mostly happen, and
that is the intent and not the cost.

**92. THE COPY HALF WAS NOT A QUESTION EITHER.** The row split it: the mark half is the system's, the
copy half might be `voice/`'s and deliberate. It is not. `voice/docs/microcopy.md` carries the trust
strip as three rows with the claim and its source split, and the stand's three - "Odds move with
money", "One named source", "Public settlement" - **appear in no microcopy row and on no screen**,
which is the defect row 82 closed for eighteen other strings. The stand's own closing line already
points at microcopy as the source of its sentences. Four blocks replaced, marks and copy together;
measured after, **200 of each claim across 196 documents, one set of three**, every kit and painted
mark `ic tr-ic` with a `<use>`.

**And the fix exposed the next one.** The product's claims are longer than the invented ones, so in a
half-width theme cell each wrapped to one word a line: the kit's own trap, a specimen measured in a
cell narrower than any placement. The section is a vertical pair now, the trade `organisms.html` had
already taken by hand. **A stand that invents shorter copy will fit in a cell the real component does
not.**

## 2026-08-10 - The rule that decides all the others was being stored in the order of two siblings

**26. WHICH HALF IS GREEN IS A CLASS NOW, NOT A POSITION.** Sixteen selectors in `yesno.css` bound
the outcome semantics to DOM order: `:first-of-type` painted green, `:last-of-type` red, on the
control this product is named after. `CLAUDE.md` says the one rule that decides others is that
**green and red are outcome semantics**, and that rule was being kept in the one place nothing
checks, the order of two siblings across 226 documents. Move the buttons and the meaning inverts
silently.

`.yes` and `.no` go on the control, which is the idiom `hero.css` already uses for the same two
meanings on `.hf-tag`, so this is a pattern the system had and had not applied to its own name.
**778 controls tagged across three trees.** Every selector kept its specificity exactly, so no
cascade tie could move: `.yesno > a:first-of-type button` and `.yesno > a > button.yes` are both
(0,2,2); `.opt-list .yesno.compact button:first-child` and `...button.yes` are both (0,4,1).

**Measured before and after: 1,504 readings on 226 documents in both themes, 0 colour differences.**
And the before-and-after earned its keep on the first pass, which reported **16 controls that had
lost their paint entirely**: the hero's call to action reads `class="hf-cta yesno"`, the sweep
matched only a class attribute STARTING with `yesno`, so those buttons lost the positional rule
without gaining the class. A sweep that matches a class list by its first word is a sweep that has
not read the markup it is sweeping.

**The row's own test, run afterwards**: reverse the pair in the DOM. "Back YES" stays green,
"Back NO" stays red. Before today that reversal would have swapped them. The skeleton placeholders
are deliberately left with no side, because a grey box has no outcome.

**76. THE UNSCOPED AMOUNT FIELD WAS ALREADY FIXED, by a pass aimed at something else.** The row was
written when every rule in `input.css` was scoped to a dialog or a panel, so an unscoped field took
its ground and its ink from the User Agent: a white box with black text in the dark theme. `.app-case`
came off 415 selectors on 2026-08-08 and this rule came with it. **Verified rather than assumed**, by
rendering the atom outside every dialog and every panel in both themes: graphite gives ground
`rgb(13,15,18)` and ink `rgb(237,231,218)`, daylight `rgb(253,251,245)` and `rgb(33,31,25)`, and the
box is 44 tall in both. The bet face is transparent on purpose and is not the same defect. **A row
that was true when it was written can be closed by a pass aimed elsewhere, and the only way to know
is to render the thing again.**

## 2026-08-10 - Two accessibility rows, both bigger than their own text, and the fix one of them proposed was illegal

**56. THE TWO SKELETON HOSTS ARE HIDDEN, AND SIX MORE WERE LOADING IN SILENCE.** The row was exact
about the two: `<article class="card skeleton">` on `event-detail-loading` and its logged-out twin,
in both trees, **4 attributes**, and all 88 others already said `aria-hidden="true"`, so the fix was
to match the file next door. Measured after in a browser rather than in the source: 180 rendered
hosts over the 38 screens that draw one, **0 still reaching the accessibility tree**.

**The same reading found what the row could not see.** A host that is `aria-hidden` is silent, which
is correct, so the LOADING has to be announced by the region around it. On `my-profile-loading`,
`public-profile-loading` and `wallet-loading`, in both trees, **one host of four stood outside every
`aria-busy` container**: the balance card's placeholder sits above the list and only the list was
marked, so those six screens said "busy" about three quarters of what was loading. `aria-busy` is
raised to the region that holds all four, `.cat-main` in the paint and `main.feed` in the grey.
After: **180 of 180 hosts inside an announced region, 0 screens with a skeleton outside one.** A
count of hosts is not a count of what a person is told.

**61. THE ROW'S TITLE WAS RIGHT AND ITS FIX WAS ILLEGAL, which is why it went out for review first.**
It proposed `aria-checked` or `aria-selected` on `.opt-row`. Neither is legal there: the row is a
`<div>`, HTML-AAM maps a div to `generic`, and **a state is only valid on a role that supports it** -
`aria-selected` belongs to gridcell, option, row and tab, `aria-checked` to checkbox, option, radio
and switch. Written on a generic they enter no accessibility tree at all, which is the **worst** of
the candidates: the markup then reads as though the state is handled and the next person stops
looking. And every role that would make them legal is **Children Presentational: True** - option,
radio, checkbox, switch, tab - so it deletes the two real buttons inside the row. That is the same
finding that made row 23 reject `role="button"` on this element, arriving again under a different
attribute name.

**What is legal is `aria-current`**, which is GLOBAL in WAI-ARIA 1.2 and therefore supported by
`generic` with no role, no required parent and no effect on descendants. `aria-current="true"` on the
chosen row, on the 2 interactive screens per tree and the 4 kit specimens, **12 rows**. Unchosen rows
get nothing: `false` is the default, it is announced by nothing, and four of them per screen is noise.

**AND THE HALF THE ROW MISSED IS THE BIGGER HALF.** It filed the accessibility tree. The same reading
shows that with the word hidden the painted chosen state is a background, a border-color and a soft
green swapped for a solid one: **no shape, no weight, no mark, no text. Colour alone, which is 1.4.1
and costs a sighted low-vision user too.** `.opt-sel-tag{display:none}` is deleted and the word
"selected" renders again. **The rule was unscoped, so it reached further than the screens**:
`ui-kit/options.html` and `ui-kit/molecules.html` carry the span in their specimens, so the stand
whose job is to show the chosen face was hiding it. The grey tree kept the word the whole time,
because it links nothing from `components/`.

**The state had to be taught to move.** Both click handlers moved the class and the word and not the
attribute, so the prototype would have told the truth until the first click and lied after it. 17
call sites over 13 documents move all three now. Verified: at rest the chosen row carries class, word
and `aria-current` in all three trees; after clicking the third row all three moved to it; overflow 0
and page errors 0 over 264 documents.

**WHAT THE REVIEW COST AND WHAT IT BOUGHT.** One independent pass, no file writes, before any edit.
It overturned the attribute, found the 1.4.1 half, found that the hiding rule reaches the kit, and
opened row **96**: on the 14 screens with an outcome list there are **188 controls per tree whose
entire accessible name is "YES" or "NO"**, with the outcome in a sibling the button does not
reference. A person tabbing hears "YES button, NO button" ten times with nothing to tell one row from
the next. That is 4.1.2, it is not what 61 was about, and it is entangled with row 89, so it is filed
rather than taken. **The review was worth it for the attribute alone: the fix the row proposed would
have shipped as markup that looks handled and does nothing.**

## 2026-08-10 - Landing this morning's decisions found a control that had been clearing the field it was built to fill

Three rows, and the third was not on any list: it fell out of clicking a chip that the other two had
just been rewritten around.

**94. THE BET LADDER IS $1 / $5 / $10 / $25, and the row's own number was wrong by 197.** It said the
chips start at $5 on **216 documents**; that counted every `.chip-amount` in the trees, and the
product has **two different chip sets**. The DEPOSIT dialog carries $10 / $20 / $50 / $100 on 97
painted and 96 grey documents, where $10 is right because the deposit minimum is $10. The BET panel
carries the set the row was about, on **19 documents**. **A count of a class is not a count of a
decision**, and I wrote that row an hour after taking the count, which is exactly when a number is
least likely to be re-read. Applied: 27 chip sets over 21 documents, $5 still selected, and the two
insufficient-funds screens keep $25 selected because that is the state they show. **And the field's
own guard was wrong too**: `min="0"` on 35 bet inputs became `min="1"`, so this morning's decision is
enforced by the browser and not only by a sentence in a document.

**95. EVERY QUICK-AMOUNT CHIP CLEARED THE FIELD INSTEAD OF FILLING IT.** The handler is
`input.value = money(num(chip.textContent))` and `money()` returns `'$' + x.toFixed(2)`, so it wrote
**`$5.00` into an `<input type="number">`** - which the browser rejects, leaving the field EMPTY and
taking the fee and payout lines to $0.00 with it. Every chip on every bet panel, and the blur
handler on the same call. **It has been dead since the amount fields became `type="number"` on
2026-08-08**, which is the change that closed row 65: a fix to one property broke a handler written
against the property it replaced, two days apart, in the same file.

**Nothing had caught it, and the reason is the one this repository keeps meeting.** A source read
sees a handler that assigns the value. A rendering read at rest sees the markup's own `value="5.00"`.
Every sweep here reads a page as it loads; this needed a page **after a click**. Fixed by writing the
NUMBER into a number field, `num(...).toFixed(2)`, leaving `money()` for the display lines it was
written for: 17 documents, 4 handler variants, **0 `x.value = money(` left in any tree**. Verified by
clicking: $1 to 1.00, $5 to 5.00, $10 to 10.00, $25 to 25.00, typing 3 and blurring gives 3.00, and
the fee follows at $0.01 for a $1 bet. **A control is not tested by reading the page it stands on.**

**28. THE FOOTER'S COMPONENT HALF, which could only be answered once 27 had said which of the sixteen
survive.** The row named three things. **A link that goes nowhere is not an `<a>`** - the rule the
side panel has had since it was written and this component never got - so the three destinations the
MAP REFUSES, declared `[ORPHAN]` in `ia/docs/sitemap.md` meaning do not build until a job is
confirmed, are `<span class="footer-soon">` now: **582 rows over 194 documents**, one step quieter
than a live label so the difference is visible rather than only true. **The sixteen labels are one
markup repeated**, which is what made both halves cheap. **The trust strip makes a dead row
expensive**, and that is why the five that stay `<a href="#">` are the five with registered map nodes
and screens still to build: a promise being kept slowly is not the same as a promise the map has
declined. Dead footer anchors **2,534 to 1,952**, page overflow 0, page errors 0 over 264 documents.

## 2026-08-10 - The brief has no unwritten mechanic left, and a footer stopped promising eight places that do not exist

Three more decisions on the same day, and with them `docs/backlog.md` "Product research not done"
is empty for the first time since the project started.

**9. THE CHAIN IS BASE.** Chosen on the three things this product actually needs from a chain rather
than on a general preference. **Native USDC issued by Circle** rather than a bridged representation,
because "your USDC is held 1:1" is the product's first trust line and a bridged token is a second
claim underneath it. **L2 fees low enough that the $1 minimum decided this morning is not eaten by
gas** - a minimum and a gas price are one decision, not two. And **the shortest fiat on-ramp**, since
the card path is Coinbase's own and a fiat on-ramp is in the first release. Polygon is the proven
alternative and is what Polymarket runs on, but its USDC is bridged; Ethereum mainnet is out on fees
alone at a $1 minimum.

**11. EVERY CADENCE INSTANCE OF A RECURRING MARKET IS ITS OWN EVENT.** "BTC above $150k this week"
is one Event with one window, one price and one resolution; next week is a different Event. The
cadence is a **series** the instances belong to, and the Frequency filter filters by the series
attribute. **Nothing new enters the model, which is the whole reason to choose it**: Active Bets,
notifications, the win and loss screens and the resolution record all keep working on the Event they
already work on. The alternative, one long-lived event that resolves repeatedly, needs a second kind
of position, a second kind of notification and a payout rule per cycle. `ia/docs/sitemap.md` had
already sketched this in a parenthesis - "each cadence instance resolves on its own schedule" - and
the parenthesis is the rule now. **This was the last unwritten mechanic in the brief.**

**27. THE EIGHT FOOTER DESTINATIONS ARE CUT.** Each was either a node the map had to gain or a label
the footer had to lose, and the label goes: `Sports`, `Trending topics`, `API / Developers`,
`Status`, `Careers`, `Press`, `Brand`, `Geo restrictions`. **`Sports` is why it went that way**: the
four categories are locked for MVP and Sports is post-MVP, so a fifth in the footer contradicted the
category decision and not only the map. Applied by a throwaway sweep over the live trees, **283
document-edits over 264 documents**: 105 painted footers, 87 grey, 2 kit.

**Cutting eight links changed the composition and the composition had to be answered too.** Three of
the four `Company` links were among the eight, so the column is gone and `About` sits in `Support`:
a heading over one link is not a column. `By topic` held one item once `Trending topics` went, so the
sub-label is gone and `View all events` joined the category list. After: **0 of the eight remain, 0
empty lists, 0 footers with fewer than three columns, page overflow 0 and page errors 0 over 264
documents at two widths.**

**THE SWEEP TOOK A DESTINATION IT SHOULD NOT HAVE, and that is the lesson of the pass.** The grey
tree marks a dead link with a `<span class="tbd">post-MVP</span>` badge after the anchor, which the
painted tree does not, so the first pass matched 105 painted footers and missed 87 grey ones. The
second pass widened the pattern to swallow the badge - and with it swallowed the `View all events`
link that shared the block, on all 87 grey footers and one kit page. Caught by counting the label
across trees afterwards, restored from `HEAD` on 88 documents. **A sweep written against one tree's
markup is a sweep tested on one tree**, and the check that finds it is counting what should NOT have
moved, not counting what should.

**WHAT IS LEFT DEAD IN THE FOOTER IS ROW 28's**: five registered nodes awaiting screens, three the
map declares `[ORPHAN]`, and five social links, 2,534 anchors in all. And **`Geo restrictions` is the
one of the eight to re-read when compliance is written**: the requirement is real and stays in
`PRODUCT.md`; if it needs a page, it gets a node on the map first and a footer label second, in that
order. That order is the whole point of the row.

## 2026-08-10 - Four product decisions carried since the brief, and one of them had been shipping a number nobody chose

`docs/backlog.md` 6, 7, 8 and 10 have been open since the project brief. They are the product
owner's to make and they were made today; this entry is what they are, what they replace, and what
moved in the tree because of them. **11 stays open** and is now the last unwritten mechanic.

**6. THE COMMISSION IS 1.5% OF THE STAKE.** The research to answer it was already in this repository
and had never been read against the product: Kalshi charges `0.07 x p x (1-p)`, which is **1.75% of
notional at a 50/50 midpoint**; Polymarket **0.8% to 1.8%** on crypto and **0.30% flat** in the US;
Hyperliquid HIP-4 **0%**. **And a rate was already shipping**: `fee = 0.03 * payout`, in the page
scripts of 13 painted screens, 17 constants, which is about **6% of the stake at even odds** and
3.4x the dearest competitor. Nobody chose it, nothing pointed at it, and the row that owned the
question said "% still TBD". **The basis moved from the payout to the stake** because a person can
check a percentage of the number they typed and cannot check a percentage of a number that does not
exist yet, and "explain the number" is the product's own differentiator. Applied: 17 constants and 13
labels, `Fee (only if you win)` to `Fee (1.5% of your bet)`. A $5 bet reads **$0.07** where it read
$0.39.

**7. THE BET MINIMUM IS $1 AND THERE IS NO MAXIMUM.** The question had **three different written
answers in three places**: `PRODUCT.md` said "$1 / $5 sizing", the microcopy said "No minimum or
maximum", and the deposit dialog said "Minimum deposit $10", while the chips on screen start at $5.
The minimum exists so the fee line is never absurd against the stake; $1 is the try-it size the MVP
scope already names; the $10 deposit minimum stays, which is a few bets of headroom rather than one.
Applied: **21 strings across all three trees** and the row in `voice/docs/microcopy.md` that is their
source.

**8. KYC IS THE FIAT RAIL'S ONLY, and no copy changed, which is the finding.** Card deposits are
verified, where the on-ramp provider does it anyway; a crypto-only user is never asked. It keeps the
product's core inversion intact - the wallet and the verification arrive at Confirm, not at entry -
and it is what Polymarket does. **The deposit dialog has read "KYC is required for card deposits;
crypto-only users can connect a USDC wallet instead" since the voice pass**, so the product had been
promising this in words for weeks while the decision behind it was open. A promise in the interface
is a decision somebody made without writing it down. It is a compliance question with a legal
component, and what is recorded here is the design default rather than legal advice.

**10. THE PAYOUT IS SHARES AT A LOCKED PRICE.** You buy YES or NO at the price on screen, that price
is locked at Confirm, and a winning share pays $1. **Timing matters because the PRICE moves, not
because the payout rule computes differently.** That is the whole reason the number can be said in
one line, and it makes the Confirm reconcile (S5) the thing it already looked like: the price moved,
here is the new one, commit or not. It replaces "AMM-style dynamic pricing, payout depends on when
the bet was placed", which was never specified and could not be explained to a newcomer - and an
unexplainable mechanic in a product whose differentiator is explaining the number is a contradiction
carried in the brief since the beginning.

**WHAT IT COST AND WHAT IT OPENED.** 13 painted screens, 4 grey screens, 3 kit pages, `PRODUCT.md`
and `voice/docs/microcopy.md`. Verified in a browser: the fee row renders `Fee (1.5% of your bet)
$0.07` against a `Potential payout $13.16`, page errors 0. **Opened 94**: the amount chips are
$5 / $10 / $25 / $50 on **216 documents** and the minimum is now $1, so the smallest size the product
allows is a size its own control cannot express. That is a sweep across a frozen tree and a shape
worth choosing rather than assuming, so it is a row.

## 2026-08-10 - The brass ladder was never a ladder, and the role standing on the floor now says how far the floor is

Two rows about brass, `docs/backlog.md` 33 and 32, both left alone by the consolidation on the
grounds that they were design decisions. They are, and a design decision is still made by measuring
first.

**33 OFFERED TWO ANSWERS AND THE MEASUREMENT GIVES A THIRD.** The row read four brass ink roles at
8.98, 11.68, 13.20 and 10.58 against the page in graphite and 7.40 for all four in chalk, and asked:
is the ladder real in both themes, or is it one role with three aliases? Re-read against the **real
composited ground** on all 106 painted screens rather than against a page swatch, which is a
different question and the one that matters: in graphite the four resolve to four values and stand at
**5.70 to 8.98, 11.13 to 11.33, 9.86 to 11.79 and 10.08**; in chalk they resolve to one value on
**704 placements, worst 5.24, best 7.40**.

**The steps in graphite are not emphasis, they are the same ink compensating for four different
grounds** - a brass-tinted chip, a photograph under a veil, a plate, bare stone. On the pale stone one
value clears every one of those grounds with 0.74 to spare over the 4.5 floor, so daylight needs no
compensation and the roles share a value. That is not a hole; **two roles may share a value as long as
each says so**, which is the rule twenty-seven other groups in `tokens.css` already live under. What
was missing was the saying, and it is written at the chalk block now with the numbers.

**THE FOURTH NAME IS DELETED.** `--text-brass-vol` had **one placement in the entire product**,
`.hf-tag.vol`, the volume tag on the featured hero. In daylight it was byte-identical to the other
three; in graphite it was 10.08 against the eyebrow's 11.13 on the same hero plate, a step of 1.05 in
contrast that nobody chose and nothing else uses. The tag takes `--text-brass-lit`, the role its own
plate already carries: measured after, rgb(216,191,127) to rgb(230,200,119) in graphite and unchanged
in daylight. It came out of `tokens.css` twice, `hero.css`, `ui-kit/colour.html` (two matrix rows, ten
cells) and `_page.css`. **A role is a reason, not a value, and "it is on the hero" is a reason that
already had a name.**

**32 IS CLOSED AS A CONSTRAINT WRITTEN WHERE THE RAMP IS, and the row had the direction backwards.**
It said "any card ground made one step lighter puts it under". A lighter stone RAISES the ratio; it is
a DEEPER stone that kills it, and the chalk ramp numbers its deeper steps lower, which is where the
wrong word came from. Computed against every step: **3.43 at chalk-940, 3.40 at 930 (the page), 3.31
at 920, 3.28 at 910 (the plate), 3.20 at 900 (the card it stands on), 3.14 at 880, 3.06 at 870 and
exactly 3.00 at chalk-860.** Three steps of headroom and the eighth lands on the floor. Measured in a
browser against real grounds, `--icon-brass` is **4 placements in daylight, all the saved bookmark on
a card, all at 3.20**, and nothing else in this system is within 0.5 of a floor. A constraint that
lives only in a backlog row is a constraint the next person to lighten a card will not read.

**AFTER.** 160 documents at 390 in graphite and 1280 in daylight: page overflow **0**, page errors
**0**, and the colour page's matrix is 34 rows where it was 36.

## 2026-08-10 - Three rows closed in one pass, and each had been filed for a reason that had stopped being true

**44: THE DRAWER BUTTON IS 44 NOW, AND IT WAS UNBLOCKED BY AN EARLIER PASS RATHER THAN BY AN
ARGUMENT.** The row filed it instead of fixing it, and said why: the button stood fixed over the TOP
LEFT of every screen, so 8px more of it moved onto a header laid out around 36. It stands in the
bottom right since this morning, in a corner measured empty on 147 of 160 documents, so the 8px lands
on nothing. It was the **last control in the repository under the project's own floor**, and it is
the one control a person has no alternative to below the dock. Verified 44x44 on **1,440 readings**:
160 documents at 390, 700 and 900, three scroll positions each, page overflow 0.

**And growing a control moved a clearance nobody re-read.** At 36 the button fitted inside the 52px
strip `.bet-dock` reserves under itself; at 44 it did not, and it crossed the dock's bottom edge by
4px in **16 readings of 960** the moment the floor was applied. The lift moved from the DESK rung to
the DETAIL rung, where the dock actually goes, and the count returned to 0.

**36: THE MONO WEIGHT WAS NOT A TRAP, IT WAS LIVE, and the row missed it by reading declarations
instead of the page.** IBM Plex Mono ships two weights, 500 and 600, in four files. The row checked
the five mono declarations in `components/`, found them all on medium or semibold, and filed it as a
trap. **Font-weight inherits.** An element that sets the mono family and no weight takes the body's
400, and there is no 400 face either: measured over 160 documents, **1,041 mono elements in the
painted tree compute 400 and 34 compute 700**, against 310 at 500 and 262 at 600. **1,075 of 1,647
ask for a face that is not there.** Nothing renders wrong and nothing is synthesised, because CSS
font matching resolves 400 onto the 500 face and 700 onto the 600, which is exactly what the original
pixel counts showed: 5380 / 5380 / 5993 / 5993 at 400 / 500 / 600 / 700, two faces wearing four
names. **So the 700 face is not added** - 33 KB for a step no screen can show is missing - and what
is fixed is the silence. `fonts.css` said `--weight-bold` was "documented as unavailable here",
pointing at a token line that said nothing, and called two weights in four files "four static faces".
**A pointer is a claim, and nothing checks a comment.**

**90: THE FOUR CLIPPED KIT CELLS WERE A SYMPTOM, and the decision the row named was the wrong pair.**
It offered: either the cell declares itself width-conditional, or the specimen is cut to what a 360
cell holds. Neither, because the specimen was not too big for the cell - **the component overflows
itself**. Measured on the four painted screens that carry holdings, with the panel's radio CHECKED:
`.hold-cols` stood 275 wide at 360 and 305 at 390 against a scrollWidth of **377**, overflowing by
**102px and 72px**. `.hold-col` declares `flex:1`, and a flex item's `min-width` is `auto`, so it may
not shrink below its content's intrinsic minimum: **the file already knew the fix and had written it
three lines up**, `.act-txt{flex:1;min-width:0}`. That halved it. The rest was one word - a username
like `polly_predicts` is an unbreakable 88px token - answered with the ellipsis `.hh-name` already
gives the same datum one component over. **After: overflow 0 at 360, 390 and 640, and the kit's four
clipped cells are 0.**

**WHY NO SWEEP HAD SEEN IT is the part worth keeping.** The holdings panel is behind a CSS radio tab,
so at rest it measures zero and every overflow pass in this repository skipped it. That is the third
costume of one trap, after the closed `<details>` and the shut `<dialog>`: **a state that is a page
is measurable, and a state that is a checked input has to be checked first.**

## 2026-08-10 - The icon set had one geometric weight that slid, so it had no optical weight at all

`docs/backlog.md` 29 said the stroke is a constant in user units and renders at six different
weights. **The row was right and its numbers were stale**: `.ic` went 1.6 to 2.2 after it was
written and nobody re-read it.

**RE-MEASURED over 2,044 stroked marks**, at two widths, against the svg's CONTENT box rather than
its border box, because two of these rules use `box-sizing:content-box` with 8px of padding and the
border box is 40 where the viewport is 22. **And split by tree, which is the part that decides what
the row was actually about.** In the product: **1,818 marks at four weights**, 1.20 at 12 on 550,
1.47 at 16 on 34, 1.65 at 18 on 1,056, 2.02 at 22 on 178. **1.68 to 1 between the ends**, which is
the number `ui-kit/icons.html` had already worked out and written down, and which this pass did not
read first. The two extremes worth quoting are both in the KIT: a **3.67 slab** on a 40px
demonstration figure, and **0.92 on six `ui-kit/trustbar.html` specimens** that had no declaration at
all and took the SVG default of 1, under one device pixel at DPR 1.

**THE FIX IS ONE TOKEN AND ONE PROPERTY.** `--stroke-mark:1.65`, paired with
`vector-effect:non-scaling-stroke` on the shapes, so the declared number is the rendered number and
the weight stops depending on the box. 1.65 because 1,122 of the 2,044 already rendered there: the
set keeps the weight it was drawn against and the other 900 come to it. `vector-effect` is a
presentation attribute on the shape and does not inherit, so it goes on the children rather than on
the svg, which is a fact about SVG that a rule written on the wrong element would have hidden.

**FOUR FILES OWNED A STROKED MARK AND EACH DECLARES THE TOKEN NOW.** Two were hand-computing the
house weight in user units and getting it right by accident: `toast.css` said 2.2 in a box of 18,
which is 1.65 on screen. One was a number nobody reconciled: `market.css` said 1.8 in a box of 16,
which is 1.20, the second lightest mark in the product. And one had **never declared anything at
all**: `.tr-ic` is not `.ic`, so the family's declaration never reached it and it took the SVG
default of 1.

**AFTER: all 1,818 product marks render at exactly 1.65, ratio 1.0**, and 2,018 of the 2,044 across
both trees. It is verified against the PAINT rather than
against the formula - a straight bar screenshotted at device scale 10 and summed by pixel coverage
gives **1.65px at boxes 12, 18, 22 and 40**, with a half-intensity width of 1.60. The other 26 are
`ui-kit/icons.html`'s blow-up specimens at 70 and 94px, and that is the one deliberate exclusion: a
drawing shown at four times its size wants its stroke at four times too. `.tk-glyph` carries no
`.ic`, so the rule never reaches it and the exclusion costs nothing to keep.

**THE INSTRUMENT HAD TO BE READ TWICE, and both times it lied in a different direction.** The first
census took the svg's border box, which over-reported the padded marks by 1.8x. The second, after the
fix, still computed `declared x box / 24` - the right formula for a stroke that scales and the wrong
one for a stroke that does not - and **reported that the whole set had got thinner**. A formula is an
instrument, and an instrument that was correct before a change is not automatically correct after it.

**WALKED INTO.** The twelve marks rendering at 0.92 were not the product's. In the painted tree the
trust marks are `class="ic tr-ic"` with a `<use>`, filled, and a stroke width can never reach them;
the only stroked `.tr-ic` in the repository is six specimens on `ui-kit/trustbar.html` carrying
`tr-ic` alone with hand-written paths, beside three items of copy the product does not have either.
The first version of the comment in `trustbar.css` blamed the product for it and was corrected before
it shipped. `docs/backlog.md` 92.

## 2026-08-10 - One job, two drawings was wrong by half a per cent, and the three treatments belonged to the stand that was reporting them

`docs/backlog.md` 75 and 88 both said this product draws its close cross more than one way. 75 had
already had its premise corrected once, by attempting the fix and being told no by a measurement.
This closes both, and the second half of 75 was wrong too.

**THE CHARGE WAS "ONE JOB, TWO DRAWINGS", filed beside the warning mark that really was a circle on
16 screens and a triangle on 4.** Read in a browser: `.sheet-close` is a 12-unit cross in a 24
viewBox at stroke 2.2, rendered in a **16px svg inside a 32px button**, so its ink spans **9.47px,
29.6% of the button**. `.icon-btn-small` draws two bars of 8 x 2 rotated 45 degrees in a **24px
button**, so their ink spans **7.07px, 29.5%**. **Two techniques, one mark, the same optical size to
within half a per cent.** `iconbtn.css` had argued the geometry correctly when it was written - 12 in
24 would be an X pressed against its own edge - and nobody had checked the arithmetic against the
other control. The technique differs because one control carries an svg and the other carries the
letter `x`, which is inert under `font-size:0` in the paint and is **the whole drawing in the grey
tree**, where the button has no pseudo-element and an emptied one measures 16 x 8.

**WHAT WAS ACTUALLY WRONG WAS THE STAND, and it was markup.** Across all three trees there are **28
small close controls, and the product ships one markup on all of them**, 4 painted and 4 grey. The
kit shipped **three**: 10 with the letter, **6 empty** on `vitrine.html`, and **4 on `toast.html`
with an `svg.ic-sm` cross inside the button**. That last is not a variant but a defect with a
picture: the bars draw from `::before` and `::after` whatever the content is, so those four drew the
mark **twice, a brass 9.47px path over a grey 7.07px pair of bars**, in the theme figure whose one
job is to show what ships. **The page's own anti-rule says "never redraw the dismiss here."** And the
vitrine's label read "the cross is two pseudo-elements, no glyph", which is the sentence that made
the empty specimens look deliberate.

**AFTER.** All 20 kit specimens carry the product's markup: **28 of 28 in three trees are one
treatment**, measured after the edit, 0 with an svg and 0 empty. The two drawings stay, with the
number that says why written beside the rule. The vitrine's label is corrected, the toast page's
anti-rule now records that this page broke it, and `ui-kit/iconbtn.html` keeps the paragraph that
called this a defect, with both of its errors marked: a specimen page that quietly deletes its own
wrong reading teaches nothing.

**AND ONE COUNT WAS WRONG.** Row 78 has said **CLOSED** in its text since 2026-08-09 and its number
was never struck, so this file counted it as open for a day. That is item 74 arriving a fourth time.
The fix it describes is present and verified: `svg.ic:has(use),svg.ic-sm:has(use){fill:currentColor
!important;stroke:none!important}` in `base.css`.

## 2026-08-10 - The harness moves and the product does not, and this time what it was taking was paint rather than width

`docs/backlog.md` 91 was opened by the ladder pass an hour earlier and is closed here. The review
drawer's button is `position:fixed` at top 12 left 12, 36 square, so it occupies x 12 to 48 on all
**160 documents below the dock**. The header row's padding-left computes 14 on a phone, so the logo
starts at x=14: **the button covered 34px of the brand mark on 88 pages, at every width from 360 to
1139**, and it has done so in every screenshot ever taken of this repository.

**THE RULE WRITTEN TO PREVENT IT HAD NEVER ONCE APPLIED.** `header.css` carried
`.app-header .row{padding-left:var(--space-56)}` inside its mobile block, and the same selector is
set again at the same (0,2,0) thirty-four lines below with `padding-left:var(--gutter)`. Equal
specificity is decided by source order, so the later rule took the property back every time. Its
scope was wrong even alive: the block stops at the desk rung and the button exists to 1139.

**THE DECISION IS THE ONE THE DOCK TOOK THIS MORNING, applied to paint instead of to width.**
Reviving the indent was rejected: it is the product paying for the harness, and it would have pushed
the brand **42px off the column every line under it aligns to**, in the review build only, for a
tool. So the chrome moves, and which corner it moves to was measured rather than argued: **160
documents at 390, 700 and 1280, five candidate boxes, classifying what sits under each of five
points of the 36px square.** At 700: **bottom right is empty on 147 of 160 pages**, against top-left
covering the brand on 88 and top-right a control on 89. Bottom right is also the corner a 220px left
drawer never reaches, so the button is clickable with the panel open - which at top-left it was not,
because it drew ON the panel it had opened.

**BELOW THE DESK RUNG IT LIFTS TO 132, and the number is what the product stacks on that edge.**
`.bottom-nav` is `position:sticky;bottom:0` and measures 56 tall on the 39 screens that carry one;
`.bet-dock` is `position:sticky;bottom:52px` and measures **68 tall in all 48 readings of it**, so
its top sits **exactly 120 from the bottom edge**. 132 is that 120 and the same 12 gap the button
uses everywhere else. From the rung up the lift is dropped: the nav is gone, and the dock reserves
52px under itself for a nav that is not there, so the bottom strip is free.

**THE FIRST NUMBER WAS 68 AND IT WAS WRONG, and how it was wrong is the lesson.** 68 is 56 plus 12:
correct arithmetic for one of the two bars and blind to the other. It was blind because the first
measurement read every page **at scroll 0**, where a sticky dock has not stuck yet, and a bar that is
not at the bottom of the viewport is invisible to a probe that asks what is at the bottom of the
viewport. Re-read at the top, the middle and the end of every page: a lift of 68 lands on the bet
dock in **32 readings of 960** and a lift of 12 on a nav item in **63**. **Reading a sticky element
without scrolling is reading the source again**, which is this repository's oldest rule wearing a
different coat.

**IT STILL CANNOT BE PERFECT, and the number is not the best one measured, on purpose.** A sticky nav
sits at the viewport's bottom on a long page and at the CONTENT's bottom on a short one, so no fixed
offset tracks it, and about ten readings of 960 land on a nav item that stopped short of the edge.
What is NOT done about that is tune the number until they go: **120 measured slightly better than 132
and is refused**, because it is a height fitted to today's content, which is exactly the mistake the
entry below this one closed at 520, in the same pass, an hour earlier.

**AFTER.** The button overlaps the header on **0 of 160 documents** at 360, 390, 639, 640, 700, 900
and 1139, and it is gone at 1140 as it always was. Read again scrolled, 160 documents at 390 and 700
at the top, the middle and the end of each, **960 readings**: page overflow **0**, header overlap
**0**, the bet dock under it **0**, a nav item under it **10**, a page control **46**, and the other
**904 are surface or text**. At 700 the whole count is three controls. It is the topmost thing at its
own centre on **858 of 960**, and the missing 102 are exactly the 17 screens that ship with a modal
sheet open, times two widths times three scroll positions: a modal is in the top layer, so it covered
this button wherever it stood and the page behind it was inert in both positions. The dead
declaration is **deleted** rather than revived, with the reason kept where it stood, so the product's
header now owes the harness nothing.

**KNOWN AND ACCEPTED.** The button is first in the DOM of every page and now renders in the bottom
right, so a keyboard reaches the roadmap before it reaches the product while the eye finds it last.
That is markup on 160 documents to change and the tool is not the product, so it stays as it is and
is written down here rather than filed.

## 2026-08-10 - A rung is one pixel and it belongs to the wide side, and the pair that wrote it twice was hiding a header that asks for 694

`docs/backlog.md` 72 was half closed this morning: the ladder was named, the harness rung was moved
off the product's widths, and **the fourth question was left open on purpose** - whether 520, 560,
620 and 980 collapse onto it. That question is a measurement and not a rename, so this is the
measurement.

**ONE OF THE FOUR COLLAPSES AND THREE STAY, and every answer is a number.**

**520 is gone.** It was never a decision: it is the width at which four columns first FIT, not the
width at which they first read. Measured one width at a time on both profiles and the kit's stand:
from **520 to 555** the four cells are 102.5 to 108.8 wide, "Member since" takes two lines, and every
figure in the row stands **91 tall instead of 80.5**. Thirty-six widths of a wrapped label in the row
that says what a person's record is. Two columns hold to 639 at 213 to 272.5 with nothing wrapping,
and four arrive at DESK at 132.5. A width out of the system and the wrap band with it.

**560 stays, because collapsing it runs a floor backwards.** Applied to 639 it takes the three
detail tiles from 36 to 28 on **79 widths of window that has room for them**, and this system's own
invariant is that a floor raises a short control and never lowers a tall one. What the block is FOR
was measured with it: the head's content box crosses the actions' left edge by 4px below 560 and by
24 above, because three 36px tiles 8 apart at a 16 offset ask 140 of clearance and the padding gives
118 - and **no line of the question has ever crossed them**, the nearest ending 31px short at 561 and
110px short at 640. The padding does its job at both sizes; the 22 it is short of the arithmetic has
never reached the ink.

**620 and 980 stay, because they are one card folding and not the page frame arriving.** The hero is
the only three-level grid in the product. Taking 980 to RAIL lands the feature's two columns at 251
and 256 **on a 901px window**, which is 28px under the 279.5 the same card already takes at 641 - and
that 279.5 is set by the gutter going 14 to 40, not by the card. Taking 620 to DESK costs 19 widths
and 288px of height, 346 tall in two columns against 634 in one, and closes nothing, because at 621
the columns are 295.5 each, wider than the minimum the card already lives with.

**AND THE MEASUREMENT FOUND WHAT THE ROW COULD NOT SEE, for the second time in one day.**

**A rung was written as a PAIR.** `max-width:640px` in eight files, `min-width:640px` in five, and
**both match at exactly 640**. So the rung rendered a page that exists at no other width: measured on
ten screens, **nine of them showed the desk utility, the balance figure and its icon button, standing
on a 14px mobile gutter under a mobile header with no bottom nav**, matching neither 639 nor 641. The
same pair stood at 760. Below a rung is `max-width:639.98px` now. **The .98 is not ceremony**: a
zoomed window reports a fractional width, 639.4 has to be mobile, and an integer bound would leave a
gap where NEITHER branch applies, which is worse than the overlap it fixes.

**What the pair was hiding is worse than the pair.** The desk header asks for **694px** - 40 of
gutter, then 36 + 8 + 149 + 8 + 88 down the left, then 8, then a 317px utility, then 40 of gutter -
and it turned on at 641. So **73 of the 106 painted screens took horizontal scroll from 641 to 652**,
and kept a right gutter under its 40 until 693. The 73 are **exactly** the signed-in screens: the
other 33 carry two auth buttons where the balance figure stands, and are narrower. Every audit in
this repository reads 390 and 1280, and yesterday's rule was to read AT the rungs and one pixel
either side; one pixel either side is what found this.

**`.hiw-btn` waits for DETAIL now.** It is 88 of the 694 and the only control in that row carrying a
word rather than a mark. Without it the row asks 598 and fits from 641 on; at 760 it asks 694 with 66
to spare. Nothing is lost in the band: every feed carries a second trigger for the same dialog and
`how-it-works.html` is a page of its own.

**WHAT IT COST, and where.** Overflow **73 pages to 0**, at every one of ten widths over all 160
documents. No rung is a state of its own any more, at 640, 760 or 900. The element sweep over ten
screens at 29 widths differs **at 520 to 639 (the record, three pages), at 640, at 641, at 700 and at
760, and at no other width**: the change is contained in the bands it was wrong in. The touch floor
was re-read under a coarse pointer at six widths on four screens: **0 controls short of 44 on either
axis**, including at 641 and 700 where the header moved.

**THE STAND HAD THE SAME PAIR, in its own chrome.** `ui-kit/_page.css` wrote four rules at
`max-width:640px` and one at `min-width:640px`, so at exactly 640 the kit printed "not rendered from
640px up" under a bottom nav while its own frame was still on the 14px mobile inset. It also already
knew the answer in one place and not the others: `.tk-below-760` was written `max-width:759px`. All
nine are exclusive now, with the reason beside them. Re-read after: **54 kit pages at 639, 640, 641,
759, 760 and 761, 0 overflow**.

**REJECTED.** Moving the header's divide up to DETAIL, which would have fitted: the bottom nav and
the gutter both pivot at DESK, so the band 641 to 759 would have had a mobile header with no bottom
nav under it. Writing `max-width:639px` instead of 639.98, for the fractional-viewport reason above.
Collapsing 620 or 980 for tidiness, which the numbers refuse.

**THE INSTRUMENT.** Animation and transition frozen, 220ms to settle, the cold pass evaluated and
thrown away, and the control taken twice unchanged: **0 of 580 keys differ**. The theme was proved
irrelevant to this measurement rather than assumed: **0 of 1,600 dark/light pairs differ** across all
160 documents at ten widths on the before pass, which is why the after pass ran in one theme and says
so. A fresh port, 8934, because a cached stylesheet has cost this repository six readings.

**WALKED INTO AND NOT FIXED.** `header.css` carries `.app-header .row{padding-left:var(--space-56)}`
to hold the row clear of the review drawer's fixed button, and **that declaration has never once
applied**: the same selector is set again at equal specificity thirty-four lines below, and source
order decides. Measured: the toggle covers **34px of the logo on 107 pages at every width from 360 to
1139**. It is `docs/backlog.md` 91, kept and marked rather than deleted, because where a review tool's
button lives is the harness's decision and there is no free corner to move it to.

## 2026-08-10 - The height pass had fixed the axis the font decided; the axis a WORD decides was still open, and a label is not in anybody's query selector

The floor of 2026-08-08 declared `min-height` for fourteen families and `min-width` for the five
that carry a mark and no label. **2.5.5 asks for both on every target**, and a label does not make a
control exempt: it only means the width arrives from a word instead of from a declaration.

**MEASURED FIRST, AT 390, WITH `matchMedia('(pointer:coarse)')` ASSERTED TRUE BEFORE EVERY READ**,
after the height pass had already moved 1,133 controls onto the ladder. 4,560 product controls, the
review chrome and inline text links excluded, the four named icon-button exclusions counted apart:
**401 short of 44x44, and 165 of them short on WIDTH ALONE**, standing a clean 44 tall.

| family | was | placements |
|---|---|---|
| `.btn-bare`, the comment actions | **31** x 44 | 72 |
| `.chip-rail`, the chart's range | 36 x 44 | 36 |
| `.rules-tab` | 36 x 44 | 9 |
| `.chip-amount`, the quick amounts | 37 x 44 | 9 |
| `.yesno.compact` YES / NO | 43 x 44 | 52 |
| `a.q`, the card's question | 210 x **30** | 32 |
| `.opt-more` | 278 x **26** | 18 |
| `.hh-name`, `.hh-all`, the hot list | 213 x **20** | 6 |
| `.toggle` | **40 x 24** | 3 |

**A WORD DECIDES A CHIP'S WIDTH THE WAY THE FONT USED TO DECIDE A CONTROL'S HEIGHT.** It is the same
defect one axis over, a dimension nobody chose arriving from the content, and it is why the answer is
a second family rule rather than a width typed into six components.

**ONE OF THE ROWS WAS MINE, WRITTEN THE DAY BEFORE.** `.opt-more` went into the system on 2026-08-10
for backlog 81 and stood 278x26 on 18 placements, because **a new control does not join a floor by
existing**. This file already records "a floor written six times and every copy named a LIST"; this
is the same trap arriving from inside rather than from a legacy file, and the list is still assembled
by hand, so it is only ever as complete as the last walk.

**WHY EACH LINK COUNTS AS A CONTROL**, since that was the real decision and not the chips: `a.q` is
the card's question and the **only** way into an event from the feed, because the card is an
`<article>` and nothing wraps it, so the primary target of the primary screen stood 30 tall; 52 of
its 84 already cleared 44 by wrapping to two lines, so this gives the single-line ones the height the
wrapped ones had. `.hh-name` is a row of a list and every row of a list is a target. `.hh-all` and
`.opt-more` are standalone actions at the foot of a block. **Deliberately excluded**: the cookie
policy link inside its sentence, which is 2.5.8's inline exception, and the 115 jump links on
`ui-visual/overview.html`, which are the painted tree's contents page and not the product.

**THE SWITCH KEPT ITS DRAWING AND GAVE UP ITS BOX.** `toggle.css` had already ruled on the method:
the fix is the control's own box and **not** an invisible pseudo stretched over it, "because a hit
area no measurement in this repository can see is a fix nobody can check". Those two arrangements are
not the same thing. A pseudo over a 40x24 button leaves the button 40x24 and every instrument still
reads a failing control; a **44x44 button with the track drawn on `::before`** reads 44x44 to
anything that measures it, the focus ring included, which now shows the target rather than the
drawing. Verified under both pointers: box 44x44, track 40 x 24, knob at 14 / 6 and 22 checked, the
same 19px inner offset it always had. A pill 44 tall is not a switch, and it did not become one.

**AND THEN THE INSTRUMENT ADMITTED IT HAD NEVER LOOKED AT LABELS.** Backlog 64 named `.ed-tablabel`,
36 placements, the main navigation of the event detail, standing 36 with a finger. It is a `<label>`,
and **every sweep in this repository queries `a, button, input, select, textarea, summary`**, so the
control was invisible to the measurement as well as to the floor. It was found by walking one
component's page. **A control is what a person taps, not what the query selector returns.**

**PUTTING `label` INTO THE QUERY THEN REPORTED 1,012 MORE, AND 1,012 WAS THE INSTRUMENT AGAIN.** They
are the language menu's options, and a closed `<details>` puts its content in `::details-content`
with `content-visibility:hidden`: each has a box, a computed `display:block`, and is never painted.
The Stage-09 audit was caught by exactly this once, on overflow, and it was caught again here inside
the same day the rule about it was written. Asked with `checkVisibility({contentVisibilityAuto:true})`
instead of by reading a rectangle: **0 as the pages ship, and 455 real options at 140x33 with every
menu opened.** `.filter-panel li label` is in the floor now; the panel is `position:absolute`, so the
dropdown got taller and no page content moved. **455 to 0.**

**WHAT IT COST, MEASURED, CONTROL 0 OF 212 CELLS BEFORE ANY OF IT WAS BELIEVED:**

- **401 short controls to 120**, and the 120 are 115 harness jump links, 5 boxes at 43.5 rounding to
  44, and 1 link inside a sentence.
- **21 of 106 pages changed height, +647px in total at 390.** The largest single page is
  `event-feed.html` at **+202 of 7,678, which is 2.6 per cent**. The nine event-detail screens grew
  8 to 9px and every pixel of it is the tab labels.
- **0 pages gained horizontal scroll** at 390 or 1280, and **0 of the kit's 884 specimen cells.**

**TWO FILES WERE STATING DECISIONS NOBODY WAS MAKING ANY MORE, AND BOTH ARE CORRECTED IN PLACE.**
`comments.css` argued that 44 "would make the comment row taller than the comment"; the row had been
44 tall since the day AFTER that was written, and the fear was about the wrong axis, because growing
the box sideways cost the row nothing. `iconbtn.css` had the largest exclusion in the system, the
footer's five social marks at 28x28 on **525 placements**, living nowhere but a `:not()` chain. **A
control excluded from a floor is not a control nobody measured**, so the argument is written where
the rule is: they clear 2.5.8 with four to spare, they are the last row of the page with nothing
under them to mis-hit, and five 44px plates across a 390 phone is 220 of solid furniture under the
site's sign-off.

**WHAT THE PASS WALKED INTO AND DID NOT FIX**, both filed with their numbers: **818 buttons wrapped
in anchors** across all three trees, `<a href="..."><button>NO</button></a>`, which is invalid markup
and two stacked targets on one visual object, consistent in every tree and therefore invisible to
every tree-against-tree comparison this repository has run (backlog 89); and **four kit cells that
clip sideways** on `bets-table.html`, proved to pre-date this pass by measuring with the change
stashed, and missed because the sweep that took 6 clipped figures to 0 read only `scrollHeight`
(backlog 90).

**Closed: 50, 55, 59, 64.** The sweep was a throwaway script in the scratchpad, run seven times, and
deleted.

---

## 2026-08-10 - The breakpoint the product does not own was 40px below the one it does, and 73 pages scrolled sideways at exactly one width

Backlog 72 said the system takes eight widths as a breakpoint and declares none of them. The census
to answer it found something the row had not asked about, and the finding is worth more than the
tidying it interrupted.

**THE ROW ASKED FOR A TOKEN AND CSS CANNOT GIVE ONE.** A media query condition does not read a
custom property: `@media(min-width:var(--bp-rail))` is invalid, `@custom-media` is unimplemented in
every browser, and this repository has no build step to compile either. Writing `--bp-rail:900px`
into `tokens.css` would have put a value in the one place that lies, usable-looking and unusable,
which is the same defect as a class that paints nothing. So the ladder is declared the way every
other rule here has been declared since the gates were deleted: **by being read.** It is a table in
the page-frame section of `tokens.css`, and **each of the 31 media rules in `components/` carries one
line naming its rung or saying it is not one.**

**THE EIGHT WIDTHS WERE NEVER EIGHT DECISIONS.** Read by what happens at them rather than by their
number, they are three rungs, four one-offs and one thing that is not the product:

| width | rules | what arrives |
|---|---|---|
| **640** | 13 in 13 files | DESK. The one divide: below it a single column, a bottom nav and a mobile dock |
| **760** | 5 | DETAIL. The event detail's second column: `.bet-panel` docks, `.bet-dock` goes, the chart takes full height |
| **900** | 6 | RAIL. A vertical rail beside the content: sub-categories, the table of contents, the how-it-works side column |
| 520, 560, 620, 980 | 5 | NOT RUNGS. One rule each doing one local job, and each says so where it stands |
| **860** | 2 | **not the product**. The review sidebar, and the rest of this entry |

**A MEDIA QUERY READS THE WINDOW AND A LAYOUT GETS THE CONTAINER.** `course-chrome.css` declares in
its first line that it is "Not product": it is the roadmap panel every page of this repository is
read through. It docked at 860 and `base.css` gave the body a 220px inset at the same width. 860 is
**40px below the widest product rung**, so from 860 up every painted screen ran a branch chosen for a
window 220px wider than the box that branch landed in. Measured over 160 pages at nine widths, both
trees, control 0 differing cells of 1,440:

- `.cat-main`, the browse content column, fell **530 to 297** crossing 900, and stayed under 530
  until 1134. 297 is narrower than the 360px phone this product is designed from, so the wide layout
  was being served into less room than the narrow one had.
- `.ed-main` fell **430 to 211 across ONE pixel**, 859 to 860, because `.bet-panel` is
  `flex:0 0 322px` and a fixed basis does not hand the space back when the room goes.
- **73 of 160 pages took horizontal scroll at 860, and at no other width.** The overflowing elements
  were `.utility` and `.avatar-menu`, the header's right cluster, 25px past the edge.

**EVERY AUDIT IN THIS REPOSITORY MISSED IT, AND THEY MISSED IT THE SAME WAY.** They read 390 and
1280. This rung is between them, and so is everything that goes wrong at it. "0 pages with
horizontal scroll" was true at both widths it was measured at and false at a third, which is the
same shape as "0 non-neutral hex in the wireframes" being true while 992 links rendered blue. The
rule is in `CLAUDE.md` now: **measure AT the rungs and one pixel either side of each**, because a
defect can live entirely between the two widths everybody reads.

**THE FIX IS 1140 AND THE NUMBER IS DERIVED, NOT PICKED.** 900 + 220 + 20: the widest product rung,
this sidebar, and the gutter between them. The chrome docks only once the product still has its
widest layout's worth of room, so it can no longer answer a question the product was asked. Below
1140 it is the drawer it already was below 860. Two rules, both in the harness, **0 lines of product
CSS changed.** After:

- horizontal scroll **73 cells to 0**
- content columns under 360 outside the phone **59 cells to 0**
- `.ed-main` at 860 **222 to 442**, at 900 **262 to 482**; `.cat-main` at 900 **308 to 528** (minimum
  across the pages that carry each)
- **0 differences at 360, 640, 859, 1140 and 1280.** The change is contained in the band it was
  wrong in, which is the proof that it was a harness rung and not a product one.

**WHAT WAS REJECTED.** Moving 860 UP to 900 was the obvious collapse and it is the worst of the
options: the panel would dock at exactly the pixel the browse rail arrives at, so the two would take
the width from each other in the same frame. Taking the inset off and letting the panel overlay the
product was considered and put aside, because the panel is how these screens are navigated and a
review tool that covers what is being reviewed is a different problem, not a smaller one.

**AND ONE COMMENT WAS WRONG IN THE WAY THE ROW DESCRIBES.** `navitem.css` argued that `.subcat
button` measures "a 10px full-width row above 860". `.subcat` changes at 900, in `catnav.css`, and
nothing about it happens at 860. It is the row's own thesis arriving as a specimen: a file reaching
for whichever breakpoint its author had in mind. Corrected to 900.

**Backlog 72 is half closed.** What stays open is only the fourth question: whether 520, 560, 620 and
980 collapse onto the ladder. Each moves layout in a real band, so that is a measurement at nine
widths in two themes, and it belongs to Stage 10 with the rest of Responsive.

**The sweep.** One throwaway script in the scratchpad, run four times: two control passes on the
unchanged tree, one after the rung moved, one after the annotations landed. Animation and transition
frozen, layout settled, the cold pass thrown away, and the control proved 0 of 1,440 before any
comparison was believed. Deleted after.

---

## 2026-08-10 - 1,133 controls stopped taking their height from the font, and one of the seven was already right

Six families stood at heights nobody had chosen: padding plus border plus whatever DM Sans returns
for `line-height:normal` at that size. **Every one of them now declares a rung**, and the numbers are
the whole argument:

| family | was | is | placements |
|---|---|---|---|
| `.nav-row`, the account panel's rows | **32.5** | **44** | 365 |
| `.chip-lane`, the sub-category filter | 40.5 | 44 | 339 |
| `.chip-nav`, the category chip | 47 | 48 | 294 |
| `.btn-bare`, the comment action | 24.5 | 28 | 72 |
| `.chip-rail`, the range rail | 26 | 28 | 63 |

**`.nav-row` was the one that mattered and it was two holes with one cause.** It stood 32.5 with a
mouse AND 32.5 with a finger, because `.nav-item` was not one of the fourteen families in the touch
floor and nothing had declared a height, so there was nothing for the floor to raise. It fails WCAG
2.5.5 at 32.5. It is 44 now, the family is the floor's fifteenth, and **the cost was measured before
it was taken**: the account panel goes 169 to 226 and stands clear of a 900 viewport at both widths.

**The three chips were each TWO controls depending on the pointer.** The floor already took them to
44 under a finger, so `.chip-lane` was 40.5 with a mouse and 44 with a thumb, `.chip-nav` 47 and 44,
`.chip-rail` 26 and 44. A control that changes height with the input device is not a control the
ladder describes.

**And the seventh was already right, which is why it was tried and put back.** `.nav-slot` stands 55
inside a bottom bar that stands 56, and that reads as one more unchosen number. It is not: the bar
carries a top border, so **the bar IS the slot plus one, and 56 is the rung on the box that touches
the edge of the screen**. Declaring 56 on the slot moved the bar to 57 and took the ladder value off
the thing that had it. Reverted, with the reason kept in the file. **The interior of a floored box is
not a control height.**

`.nav-row-stack` is left at 49: two lines of content, already above the floor, and its box comes from
what is in it.

Verified over 20 screens at 390 and 1280: **one height per family, every one on the ladder, 0 pages
with horizontal scroll.** Two elements overflow a hidden axis on every page at both widths and are
unrelated to any of this, a name in the profile hero and one unclassed div; they predate the change
and are not part of it.

---

## 2026-08-10 - The card says how much of the market it is not showing, and the number is the smallest the arithmetic allows

Every multi-outcome card in this product shows exactly two rows, 21 of 21 in both trees, and the two
do not add up to the market. **One card in the set does**: Republicans 52 and Democrats 48 make 100,
and that is precisely the pair a person had to be able to tell apart from a truncated one and could
not. A shortlist and a complete market looked identical.

**The word is the product's own.** `.ed-cat` prints "5 outcomes" and the detail section is headed
Outcomes, against `4 options` in the Related list, 24 placements of one string. One word for one
thing: the Related list says **4 outcomes** now.

**The number is the smallest the arithmetic forces**, the remainder over the smallest percentage
already shown, rounded up, because that is the only count the data supports. Eurovision leaves 39
against Italy's 27, so two. The stablecoin market leaves 8, so one. **And one market overrides the
formula, which is the rule worth keeping**: the UK election is named in the Related list as four
outcomes, so its card says two more where the arithmetic alone would have said one. **A count the
product states beats a count the product implies.**

`.opt-more` is a link and not a label, and it goes where the card goes: a person told that two
outcomes are missing needs the place they are. **18 cards in each tree carry it, 3 do not**, and the
3 are the complete market.

Grey first, and the grey tree needed its own rule for it, because `wireframes/` has no
`components/index.css` and a bare `<a>` there would have drawn in the browser's blue. That is the
992-links trap, and it is now the reason 12 grey stylesheets carry one line each.

Verified over 24 feed screens in both trees, with a checker that recomputes the count from the
percentages rather than reading the string: **21 option lists per tree, 18 with the row, 3 without,
0 with the wrong number and 0 with the wrong plural.**

---

## 2026-08-10 - A wire soldered to the wrong pin, a document describing gates that were deleted, and a defect that turned out to be the grey tree's only drawing

Three rows in one pass, and the third one failed and is the most useful of them.

**83, and it was a wire and not a design.** Every `Confirm bet` in the desktop panel and the phone
dock carried `data-open="signin"`. On the two logged-out detail screens that is right. On the other
six it was not: `event-detail.html`, `event-detail-multi.html` and the four bet-state screens all
show a balance plate reading $142.00 and `$42.00 cash` inside the panel, **and pressing the one
button the whole screen is built around asked the person to sign in.** The right destination already
existed and was already linked from the same block: the bet-error panel's own `Try again` goes to
`event-detail-bet-processing.html`. **14 controls rewired across both trees**, the boxes unchanged,
288x48 in the panel and 108x48 in the dock at both widths.

**73, and the fix was not a deletion.** `DESIGN.md` told its reader that the build fails on gates 12,
9, 13 and 20, and all 41 gates were deleted on 2026-08-07. Each of those sentences names a real
invariant, so **each one now carries the reason it exists**, which is the thing a gate never told
anybody: a raw number is a decision nobody can find again; a spacing step used as a width says a gap
and the side of a thing are the same kind of number; a raw `z-index` is a claim about every layer
made by somebody who could see one; a rule on a screen is a rule the system cannot see; a primitive
named directly is a colour that cannot turn with the theme. Two stale pointers went with them, a
script deleted with the other 62 and an architecture document that moved to the archive.

**75 failed, and here is what it taught.** The row said the toast dismiss "holds 0 `<svg>` and its
content is the text character `x` with nothing on `::before` or `::after`". The first half is true.
The second is not: `iconbtn.css` draws that cross with **two rotated bars on `::before` and
`::after`**, `--size-8` in a 24 box, with a comment arguing the geometry, and the button carries
`font-size:0`. So the letter draws nothing in the painted tree and always did.

It was removed on that reading, and **the measurement said no. In the GREY tree the letter is the
whole drawing**: `wireframes/` styles `.toast-close` as a bordered box at font-size 11 with no
pseudo-element cross, so an empty button measured **16 x 8 with nothing in it**. Put back, all 22
elements, byte-identical to where they started.

**The same markup was inert in one tree and load-bearing in the other**, and no reading of one tree
could have found that. It is the strongest argument the two-tree discipline has produced yet, and it
arrived from an attempted deletion rather than from a sweep.

What survives of the row is smaller and real: **this product draws a close cross two ways**, a
stroked path at 32 and 24 and two CSS bars at 24, and the file argues its geometry rather than being
unaware of the other. That is a decision to confirm, not a defect to fix, and the row says so now.

**Two of my own rows have now been wrong in two days**, 85's `prov-google` and this one, and both
were answered in a file comment before the sweep ran. The lesson is not to sweep less. It is that
**a finding against a file that argues its own case is a finding against the argument, and the
argument has to be read before the row is written.**

---

## 2026-08-10 - The chart's legend item came home, and the flat kit is what settled that it had one

`.ed-legend` was declared and drawn in `chart.css` and `.lg-item` inside it in `bets-table.css`,
which draws a table of holders. One part, two owners, and the part is written at run time, so no
reading of the markup finds it.

**The row asked for the reason before the move, and the reason was findable.** `git log -S` puts
`.lg-item` into `bets-table.css` on 2026-07-26, the day the flat kit was split into 38 component
files. Reading the flat kit at the commit before that split: the three rules sit **directly under
`.ed-legend`, beneath a comment reading "multi-outcome chart: one line per outcome (stroke/width/opacity
set by JS) + legend"**. So it was a mechanical misfile at the split and not a home the rule had ever
earned. That is the difference between moving a rule and guessing.

Moved back, with the comment on both sides saying what happened. `bets-table.css` is four classes
lighter in its own declaration, `chart.css` one heavier.

**And the instrument needed one more repair before the proof was worth taking.** With animation
frozen the control still gave 165 differing rows of 15,802 on the first pair of passes, and 0 on
every pair after. **The first pass through a fresh page is a cold pass**: fonts, stylesheet and
layout are being resolved for the first time, and it reads differently from every pass that follows.
So the protocol now has a warm-up pass that is taken and thrown away. Control after the warm-up:
**0 of 15,802.** The real comparison, over 17 documents that carry the legend or the table:
**0 rows differing.**

Two repairs in two days, and they are the same shape: **the instrument has to be proved on a
question whose answer you already know before it is asked one whose answer you do not.**

---

## 2026-08-10 - Every word in the kit is now a word the product says, and the first count of it was wrong because it read the file instead of the page

The row said 18 invented strings on 9 pages. Read from the rendered DOM instead of the source it was
**78 on 22 pages**, and the difference is the same lesson this repository keeps buying: a screen
ships `Volume: $84,200` as one string and a script splits it into `.m-label` and `.m-val`, so a
source-reading sweep calls every split half an invention. The first list also missed everything the
kit had put on a page the row had not thought to check.

**174 strings replaced across 23 pages. 0 of 1,102 kit content strings are invented now**, measured
against 402 distinct product strings from all 106 painted screens.

They were four kinds of wrong, and only the first is what the row was about:

- **Copy the product never wrote.** "Will the state board certify the count before March 1", "Will
  the festival announce its headliner before June?", "Eurovision 2027 final decided by jury vote",
  "Gavin Newsom", the comment users `m_kovac` and `rina_s`. Every one replaced with the question,
  the outcome or the user the screens ship.
- **Copy trimmed to fit.** `"Funding talks have stalled twice this quarter."` against the product's
  `"Funding talks have stalled twice this quarter, but past deadlines settled late."` on five pages.
  **The clause that was cut is the one that makes the block wrap to two lines**, so the specimen was
  the wrong height wherever it stood.
- **Invented LABELS, which is worse than invented values.** `position.html` printed
  `Now worth` and `Paid out` in the figure grid. The product says `Current value` and `Payout`.
  A number that is wrong is a datum; **a label that is wrong is the component teaching the wrong
  vocabulary**, and this one was on the page whose whole subject is that grid.
- **Structure dressed as content.** `molecules.html` gave the market-depth head row the same
  `.md-amt` / `.md-price` / `.md-get` classes as its data rows, so the words "Bet", "Price" and "You
  get" were being measured as figures. The product's head row is three plain spans reading
  "Bet", "Avg YES price", "You receive if YES".

**The measurement itself had to be taken from the page, not the source**, and doing it that way also
removed 30 false positives the first list had, every one of them a value a script writes at run
time. **The rule stands where it always did: reading the source is not reading the page, and it is
as true of words as it is of colours.**

Proof after: **884 specimen cells, 0 empty, 0 duplicate ids, 0 horizontal scroll, 0 radio groups
with other than one checked, 308 glyphs all resolved, 0 sections left unclosed.**

---

## 2026-08-10 - Five class names left the markup of both trees, three stayed and were declared as script hooks, and the instrument had to be repaired before either could be proved

Eight classes stood in the product markup and no rule reached them. They split three ways once each
was read rather than counted:

- **Five were inert.** `ed-act` (27 placements on 9 screens), `load-more` (9), `ed-market` (9),
  `cmt-post` (7), `toast-wrap` (1). Every one of them sits beside classes that already draw the
  element: `.ed-act` is a third name on a button that is already `.icon-btn.icon-btn-tile`, and
  `.icon-btn.icon-btn-tile` is what carries the 10px corner, the ground and the 18px mark.
  `.ed-actions` beside it positions the container and does nothing to the buttons. **Deleted from all
  three trees: 129 class tokens across 46 files**, painted, grey and kit together.
- **Three were script hooks and are now declared as such.** `.ed-chart` and `.ed-chart-multi` in
  `chart.css`, `.rules-panel` in `tabs.css`, under a new `Script hooks:` line that says what reads
  them and why they carry no rule. `.ed-chart-multi` is the class that decides five polylines
  instead of one, and the kit's chart specimen wears it now, because the specimen it draws IS the
  multi chart.
- **One was a false finding and the file had already answered it.** `prov-google`, 107 placements on
  105 screens, is documented in `button.css`: a logotype in four colours cannot take
  `fill:currentColor` the way the Apple and X marks do, so it correctly has no rule. Corrected in the
  backlog rather than dropped.

**The proof needed the instrument repaired first, and that is the part worth keeping.** The
before-and-after snapshot reported 31 files with a difference. Every sampled difference was an
opacity mid-animation and a document height one pixel apart. **So the same tree was measured twice
with no edit at all: 3,587 of 18,390 rows differed.** The instrument, not the change. The pages carry
entrance animations and a 110ms settle catches them mid-flight.

Repaired by injecting `animation:none;transition:none` into each frame before reading and giving the
layout 450ms. The control then ran clean: **same tree twice, 0 of 18,409 rows differing.** Only then
was the real comparison worth anything, and it was taken by stashing the change and re-reading HEAD
through the same instrument: **18,409 element readings over 19 screens, 0 rows differing.**

**A number that moves when nothing moved is not a measurement, it is a reading of the instrument.**
This repository has now paid for that lesson twice: once when `getBBox` was compared against CSS
pixels, and once here.

Proof after: **439 declarations, 0 holes, 0 invented, 442 specimen cells with 0 empty, 0 duplicate
ids, 0 scroll, 0 radio groups with other than one checked, 308 kit glyphs and 1,930 product glyphs
all resolved, and 0 of the five removed names left anywhere.**

---

## 2026-08-10 - Every file now declares what it owns, and the declaration immediately found four more faces the kit was missing

The header line of a component file, `Classes: .btn, .btn-bare, ...`, is the only machine-readable
statement of what that file owns. **Six of the seven patterns had no such line at all**, and about
nineteen classes were styled inside a component and claimed by no header anywhere. So the
whole-system sweep the day before was reading an incomplete map, and **under-reporting by exactly
that much**.

Closed. 45 files carry a class list, **436 declarations, 0 unclaimed**. The patterns got theirs from
what they actually style, and the loose classes went to the file that draws them: the shared `sel`
state to each of the five files that style it compound (`.chip.sel`, `.opt-row.sel`), the width
utilities to the three that use them, `.win-dialog` and `.loss-dialog` to dialog, `.notif-drop` and
`.scrolled` to header, `.ed-rules` to tabs.

**And the point of doing it was proved within the minute.** Re-running the same sweep against the
corrected map opened **four new holes that had been invisible because nobody had declared the
classes**:

- **`.scrolled`, on the live header of 57 screens.** A page script adds it when the full category
  bar leaves the viewport, and what it does is open `.cat-condensed`, the small icon-less strip that
  keeps the categories reachable. **That strip was in the markup of every header specimen on the
  page and every one of them drew it shut**, so the class was correct, measurable and invisible.
- **`.win-dialog`, on 4 screens.** The kit had the loss face and not the win face of the one dialog
  that opens itself, and green and red are the whole point of that pair.
- **`.ed-rules`** on 9 screens, the section the rules strip stands in.
- **`.read-col`** on 1 screen, a column this kit already measured in a table and had never drawn.

**One row was wrong and the file it accused had already answered it.** Backlog 85 named
`prov-google` as the worst of the unreached classes, 107 placements on 105 screens. `button.css`
says, in writing, above the rule: *"`.prov-google` carries its own brand colours in the markup and
correctly has no rule."* A logotype that is red, yellow, green and blue cannot take
`fill:currentColor` the way the Apple and X marks do. **It is not a defect, it is a decision, and it
was in the file the whole time.** The row is corrected rather than quietly dropped, because a sweep
that flags a documented decision is a sweep whose next finding is trusted less.

Proof over 160 documents at both widths: **884 specimen cells, 0 empty, 0 duplicate ids, 0
horizontal scroll, 0 radio groups with other than one checked, 308 kit glyphs and 1,930 product
glyphs all resolved, 436 declared classes, 0 holes, 0 invented.**

---

## 2026-08-10 - 30 classes stood in the product and on no page of the kit, and closing the last of them found the reason the kit could never have shown two of them

**The measurement first.** 160 documents rendered in a browser, 106 painted screens and 54 kit
pages, and every class taken from the live DOM rather than from the file. Against the 400 classes
the component files declare:

- **0 classes the kit shows that the product does not ship.** Nothing invented.
- **0 classes declared and used nowhere.** Nothing dead.
- **30 classes on 13 components stood in the product and on no page of the kit.** That is the hole,
  and it is closed: **0 of 30 now.**

They were not decoration. The whole `.ptab*` family and the plain `.tabs` strip, so **two of this
product's three tab families had never been drawn in the kit**. `.resolution`, `.args` and
`.arg-col`, so the paragraph that says what makes a market pay out had no picture anywhere.
`.ed-chart-head`, `.ed-chart-now`, `.ed-chart-foot` and `.ed-legend`, so **the chart stood without
its frame**. `.outcome-dialog` on 6 screens, the only dialog in the product that opens by itself.
`.cc-page`, on a page whose whole argument is "these two things are drawn alike and mean different
things" - **an argument that cannot be made without both drawings**.

**And the last two of the thirty could not be drawn at all, which is what this pass was really
for.** Both tab families were selected by document-unique id: `#edtab-comments:checked ~
.ed-panel-comments`, and the labels by `label[for="edtab-comments"]`. That works on a screen, which
holds one tab set. **It makes the component impossible to stand twice in one document**, which is
exactly what a stand must do, one cell per theme. The kit had already suffixed the light cell's ids
to keep the document valid, and **the cost of that was total and invisible: no rule matched the
suffixed ids, so the light cell of every tab specimen had been drawing its bar and none of its
panels.** Nobody had looked, because a cell with a tab bar in it is not an empty cell.

`components/tabs.css` now keys all four switches to POSITION: `.ed-tabwrap > .ed-tabradio:nth-of-type(1):checked ~ .ed-panel-comments`.
The ids stay in the markup, because a `<label for>` needs one and a screen reader follows it. Six
rule groups, 0 id-keyed selectors left in the file. Verified on the 9 screens that carry the event
set and the 2 that carry the profile set: exactly one panel visible, exactly one label lit, before
and after.

**Then the same defect arrived through its other door.** A radio group is keyed by `name`, and two
theme cells sharing `name="edtab"` are ONE group across both: the light cell's checked radio
unchecks the dark cell's. Five kit pages had it, `tabs`, `event-detail`, `feed`, `filters` and
`footer`, and it had been hidden behind the id bug on two of them. Every light cell suffixes its
`name` now. Checked over all 54 pages: **every named group has exactly one checked radio per cell,
and every tab family shows exactly one panel per cell.**

**The rule this pays for: an id in a selector is a promise that the component stands once in a
document, and no component in a design system may make that promise.** It is item 45's argument
arriving from the far side: the kit does not suffix ids to be tidy, it suffixes them because a
specimen is a second copy, and a stylesheet that cannot survive a second copy is a stylesheet that
cannot be shown.

Proof, both widths and both trees: **0 holes, 0 empty specimens, 0 duplicate ids, 0 horizontal
scroll, 300 kit glyphs and 1,930 product glyphs all resolved, 0 unresolved.**

Three rows opened rather than swept: **84**, the chart legend's item is declared and drawn in
`bets-table.css`; **85**, nine classes in the product markup that no rule anywhere reaches, one of
them 107 times; **86**, six of seven patterns declare no classes at all and about nineteen classes
are styled and claimed by no component.

---

## 2026-08-09 - Four specimens counted 39 elements each and painted none of them, because a shut dialog measures the same as an open one

`ui-kit/dialog.html` and `ui-kit/betpanel.html` both opened with a section titled "whole" and both
drew **an empty band at 390 and at 1280**, in both themes, since 2026-08-08.

**The cause is one attribute and the instrument is the reason it survived.** The rebuild sliced the
sheet out of the product whole, and in the product a sheet is SHUT until a script opens it: a
`<dialog>` with no `open` attribute is `display:none`. So each page held 39 correct elements inside
a box the browser never painted, **and the gap sweep that declared 0 of 38 pages poorer than the
product counted those 39 and passed**. An element count cannot tell an open dialog from a shut one.
It is the same trap as the SVG with no `fill` and the 992 links in the browser's blue: a missing
value is a value, and the only instrument that sees it is paint.

**So the sweep was rewritten to measure paint, and re-run over the whole kit**: every
`.tk-theme-fig` on all 54 pages, at 1280 and at 390, flagging any cell whose children all measure
zero. Four cells on two pages were empty. **It is 0 of 54 at both widths now.**

Three more things were wrong on `betpanel.html`, and none of them was visible as a gap:

- **The section titled "The panel, whole" was a sheet.** `.bet-panel` itself was on no page in the
  kit. It stands there now, sliced from `event-detail-multi.html`, the richest of the eleven at 38
  elements, and it measures **322 x 559 against the product's 322 x 559**.
- **The dock was argued away.** The page said a dock cannot stand where the page is also read at
  1280, because it is `display:none` above 760. That is equally true of the panel in the opposite
  direction, and the kit had already answered it once: `.tk-show-nav` pins the bottom bar visible on
  the page where the bar is not the subject. Both faces take that bargain now and both say what it
  costs.
- **And "the richest instance" was the wrong question for the dock**, which the first pass got wrong
  and the second corrected. Counted across the eight: **four docks CHOOSE and four CONFIRM**, and
  they are not a long form and a short form of one thing. The chooser is two sides carrying
  `data-open-sheet`, and pressing one of them is **the only way a phone reaches the bet panel at
  all**; the confirmer stands on the four bet-state screens where the amount is already set and
  carries the stake, the payout and its own Confirm. Picking the fuller one on element count alone
  would have shown the dock **without the thing the dock is for**. Both stand now, chooser first,
  4 elements and 7, both **68 tall, the product's**. **A count ranks two shapes of one component; it
  cannot tell you they do different jobs.**
- **The sheet splits the same way the card does.** 39 elements on the two multi screens and **34 on
  the two binary ones**, the difference being the "Your outcome" row and its Change link, which is
  the same five elements the panel adds for the same reason: with one question there is nothing to
  choose between and nothing to go back to.
- **The sheet specimen was composed rather than copied.** "Your stake" against the product's
  "Amount", one line called "If YES" against three, three quick chips against four, and a sentence
  about fees that is on no screen. Six differences, every one of them plausible, which is the whole
  argument for copying.

**And the panel brought a lesson about its container.** `.bet-panel` sizes itself with
`flex:0 0 322px`, and **a flex basis is a width in a row and a height in a column**. Dropped into
the stand's own column cell it drew **353 x 322 with `overflow:clip` cutting the rest off**. The
container is `.ed-layout` here, the product's, held in the row direction by the modifier: the same
answer `.bp-dir` got when the pair was measured 4px short in `.tk-pair`.

**One product defect was found and filed rather than fixed**, because it is a flow decision:
**"Confirm bet" opens the SIGN-IN sheet on six screens where the person is already signed in** and
the header is showing their balance. Row 83.

---

## 2026-08-09 - The card page invented a third outcome, and a specimen written from the component is not the component

`ui-kit/card.html` drew a multi-outcome card with three rows, Sweden, Italy and Ukraine. **The
product has never shipped three.** Counted by parsing every screen in both trees: **21
multi-outcome cards, 21 of 21 carrying exactly two rows**, painted and grey, on 12 screens each.

**The rebuild of the day before is what let it through**, and the reason is worth keeping. The
method that fixed 22 pages was "render all 106 screens, find the richest instance, slice it out".
For `card` that method never ran: the page already HAD a specimen, so it was judged on whether it
showed the component's parts rather than on whether it was a card the product draws, and the missing
part it was given, the action row, was written **from `card.css` and `options.css`** instead. A
stylesheet says a row exists. It does not say how many stand in a card, so the number came from
whoever was typing.

Three things were wrong once the feed's own first cards were put in beside it, and only the first
was visible:

- **The third row.** Two rows is what every multi card ships.
- **The question and its reason.** "Will the state board certify the count before March 1?" is on
  no screen in either tree. The feed's binary card 1 asks about a government shutdown.
- **The meta row was drawing in one colour.** The screens ship `Volume: $84,200` as a single string
  and a page script splits it into `.m-label` and `.m-val`; `card.css` colours the label muted and
  the value primary. A specimen that writes the string whole gets **neither rule**, and nothing
  fails: it just draws flat and looks fine. `.prob-line` and the odds bar are the same shape of
  fact, and the page now says so in place of implying the bar is markup.

Proof, both themes and both widths: `.opt-row` **54**, the compact button **44**, `.oddsbar`
**30**, the pair button **44**, `.meta` **25** at 1280 and **37** at 390 - **every height identical
to the feed's**, the widths differing only by the cell. 0 horizontal scroll, 0 clipped cells, 0
duplicate ids, 0 console messages, 4 of 4 glyphs resolved.

**Two rows were opened rather than swept.** The card is a **shortlist and never says so** (81):
Sweden and Italy leave 39 per cent unaccounted, the detail page lists five outcomes, and the Related
list one block away already prints `4 options` for exactly this case. And the invention is a class,
not a case (82): comparing every `.q`, `.ed-q`, `.pos-q`, `.rel-q`, `.opt-name` and `.why` string in
`ui-kit/` against both trees found **18 strings on 9 pages that no screen ships**, four of them the
quieter kind - `"Funding talks have stalled twice this quarter."` against the product's
`"Funding talks have stalled twice this quarter, but past deadlines settled late."` **A specimen
trimmed to fit a cell has stopped being the specimen**, because the clause that was cut is the one
that makes the block wrap.

**The rule this pays for: a specimen is copied from a screen, never written from a stylesheet.** The
stylesheet is the thing being demonstrated, so using it as the source of the demonstration proves
only that the file agrees with itself.

---

## 2026-08-09 - All 38 component pages now show what the product ships, and putting a component in twice needed the id rule the kit already knew

The gap measured earlier the same day was **22 of 38 pages poorer than the product**. It is **0 of
38** now. The method did not change once across the 22: **take the container and the markup the
screens ship, and where the product writes something with a script, write it by hand and say so.**

**The winning instance was picked by rendering, not by reading.** For each component, every one of the
106 painted screens was rendered and the richest subtree wearing that component's own declared
classes was found, then that block was sliced out of the source and put on the page. So `footer`
comes from `404.html`, `hiw-dialog` from `how-it-works.html`, `event-detail` and `tabs` and `market`
and `comments` from `event-detail-bet-error.html`, `betpanel` and `chart` and `options` and `dialog`
from `event-detail-logged-out-multi.html`, `catnav` from `event-feed-politics-empty.html`, `toc` from
`terms.html`. A hand-picked screen would have picked the one somebody remembered.

| | page before | page after | product |
|---|---|---|---|
| `feed` | 0 | **630** | 630 |
| `tabs` | 4 | **186** | 186 |
| `event-detail` | 5 | **186** | 186 |
| `footer` | 17 | **161** | 161 |
| `header` | 8 | **72** | 72 |
| `hiw-dialog` | 19 | **61** | 61 |

and `toc` 13 to 45, `comments` 21 to 50, `dialog` 9 to 39, `bets-table` 24 to 44, `betpanel` 18 to
39, `catnav` 16 to 38, `options` 16 to 31, `filters` 14 to 30, `seo-plate` 15 to 29, `cookie-consent`
22 to 28, `toast` 14 to 22, `market` 46 to 51, `chart` 6 to 17, `state-block` 9 to 14, `position` 10
to 13, `notice` 4 to 6, `button` 2 to 5, `bottomnav` 20 to 21.

### The feed is the case that says what a container page is for

`feed.css` declares ONE class and the shell is all it is: a column, a gutter and a maximum. It had
**no specimen at all**, which for a container is the worst of the twenty-two: **a container with
nothing in it is invisible.** It carries the whole feed now, and reaching parity took writing out
what three separate page scripts do at run time, because a stand does not run them: **18 odds bars
with their `.prob-line` left in place and hidden, exactly as the script leaves it**, and **48 meta
values split into a label and a figure**. Faking two of those and forgetting the third is how a
specimen ends up 66 elements short and looking right.

### Putting a component in twice is the id problem this kit had already written down

`ui-kit/CLAUDE.md` records it from `organisms.html`: **nine declarations in the system are keyed to a
document-unique id**, so `tabs.css` and `hero.css` work once per document, and the shelf therefore
draws those two ONCE on purpose. Every specimen here is drawn twice, once per theme, so the moment
the product's own markup arrived it brought its ids with it: **16 duplicates over 8 pages**, and on
`event-detail.html` and `tabs.html` that means one radio set driving two panels.

The shelf's answer was to draw the component once. **The pages' answer is to make the ids unique per
cell**, which keeps both themes and keeps the tabs working in both: every id defined inside a cell
that the page has already seen is suffixed, along with every `for`, `aria-controls`,
`aria-labelledby`, `href="#id"` and `url(#id)` that points at it, and nothing that points at a sprite
symbol is touched. **16 duplicates to 0**, and `header.html` needed a second pass because it carries
the header in three sections and the collision was between two DARK cells, not between a dark and a
light one.

### Verified

**320 renders over both trees at both widths, over http and over `file://`, identical on both:**
3,439 glyphs drawn, **0 empty, 0 unpainted**, 316 menus opened and **0 mis-placed**, **0 horizontal
scroll, 0 clipped cells, 0 duplicate ids, 0 failed requests**. And the gap sweep re-run: **0 of 38
pages poorer than the product.** Backlog 79 closed.

Written: 22 pages in `ui-kit/`, `docs/backlog.md`, `ui-kit/CLAUDE.md`.

---

## 2026-08-09 - Opening the header's menu on a stand found it opening off the edge of the window on 105 screens

The header's page got a section that opens the notification menu, because **the panel is the part
`header.css` genuinely draws**: the band is the surface's, the circles are the icon button's, the
rows are the nav item's. A panel is invisible while its menu is shut, so a page about this component
that never opens one is a page about its neighbours.

**Two things came out of opening it, and the second is the product's.**

### The stand was distorting the component to show a part of it

The panel was first pinned `position:static`, which is the bargain `.tk-dlg` takes for a dialog and
the filter menu takes for its panel. **It is the wrong bargain here and the reason is worth keeping.**
Those two ARE the whole specimen; this one hangs off ONE control inside a BAND. Static puts it in the
flow, the `<details>` grows to 244px, the row grows with it, and **the header draws 440px tall with a
wordmark floating in the middle of it**. A specimen that has to distort its own component in order to
show a part of it is showing neither.

So the panel keeps the product's position and **the cell makes room**: `overflow:visible`, because
`.tk-theme-fig` carries `overflow-x:auto` for the category rail and CSS resolves the other axis to
`auto` with it, which is exactly what scrolls an absolute panel out of sight; and a reserved strip
below the band, the panel's own measured height plus its 4px offset. **The band is 59px on the stand
and 59px in the product.**

### And then the panel was in the wrong place, in the product

`components/header.css` positions the dropdown **twice**. Lines 22 and 36 say `right:0`, which is the
only thing that can work for two controls sitting at the right end of a band. A later rule at the
same specificity, (0,2,0), restated `position:absolute` and added `left:0`; it comes later, so `left`
won. With both offsets resolved and a fixed width, LTR takes `left`, so **both header menus opened
RIGHTWARDS from their control instead of being right-aligned to it.**

Measured in the product, not on the stand:

| | notification panel | account menu |
|---|---|---|
| at 390 | **142px past the right edge** of a 390px window, 55% of it off-screen | 126px past |
| at 1280 | 116px past | 100px past |

On all 105 screens that carry a header, in both auth states.

**Nothing had ever opened them.** Every sweep this repository runs reads the document as it loads,
and a `<details>` is shut then: the panel has no box to measure, no contrast to check, no target to
size. The 460-render audit of 2026-08-08 did not see it, and could not have. **It took building the
component's own page and opening the menu on purpose**, which is the one thing a stand does that a
sweep does not, and it is the strongest argument yet for the pages being rebuilt.

The fix is one word: the later rule carries the skin, and the position stays where it was declared
first.

**Verified: 320 renders over both trees at both widths, over http and over `file://`, identical:
3,251 glyphs drawn, 0 empty, 0 unpainted, 316 menus opened and 0 off-window or mis-aligned, 0
horizontal scroll, 0 failed requests.** Backlog 80.

Written: `components/header.css`, `ui-kit/header.html`, `ui-kit/_page.css`, `docs/backlog.md`.

---

## 2026-08-09 - Twenty-two component pages show less of their component than the product does

Four reports in a row, each a screenshot of a different kit page: the header, the footer, the how-it-
works sheet, the tab strips, the event detail head, the bet panel. **So the instance was stopped and
the CLASS was measured.** No hand-written selector list: each `components/*.css` declares its own
classes in its header line, so those were taken, and for every component the biggest subtree wearing
any of them was counted on its own kit page, on its level shelf, and across all 106 painted screens.

**22 of 38 pages are poorer than the best specimen elsewhere**, and the six worst are not close:

| | its own page | shelf | product |
|---|---|---|---|
| `feed` | 0 | 16 | **630** |
| `tabs` | 4 | 48 | **186** |
| `event-detail` | 5 | 48 | **186** |
| `footer` | 17 | 124 | **161** |
| `header` | 8 | 60 | **72** |
| `hiw-dialog` | 19 | 33 | **61** |

then `toc` 32 short, `dialog` 30, `comments` 29, `catnav` 22, `betpanel` 21, `bets-table` 20,
`filters` 16, `options` 15, `seo-plate` 14, `chart` 11, and seven more under 10.

**This is upside down against the kit's own rule**, which is in `ui-kit/CLAUDE.md` in those words: a
shelf gives every component ONE specimen, and a component page exists because taking one apart needs
room a shelf has not got. A page that shows a third of what the shelf shows is not a deeper look, it
is a shallower one with more prose around it.

### header.html rebuilt as the first, to check the approach before the other 21

Its specimen was a wordmark, a How it works and a balance figure: **8 elements against the product's
72**, and the note under it described two dropdowns and three circles that were not in the cell. It
is the product's own header now, verbatim from `event-feed.html`: **72 kids, 31 classes, 59px tall,
the same three numbers the product measures.**

Two sections were added rather than one, because the count is not the only thing that was missing.
**The panel is the part `header.css` genuinely draws** (the band is the surface's, the circles are
the icon button's, the rows are the nav item's), and a panel is invisible while its menu is shut, so
there is now a section with the menu OPEN. That needed the third instance of a bargain this kit has
already made twice: `.dropdown` is `position:absolute`, so it is pinned static under its summary and
the one difference is declared. It is a MODIFIER, `.tk-open-menu`, because the header also stands in
cells where the menu is correctly shut and a bare descendant rule would have moved a panel nobody
opened. And section 5 makes a claim about two auth states measured across 105 screens and had no
specimen under it, so it has the logged-out bar now.

**The themes stack rather than standing side by side**, which is the rule written earlier the same
day applied to its own case: at 1280 a `.tk-pair2` cell is 477 wide and the product's header is
1,060, and a header cut to half a cell is not a header. Stacked it measures 986, the same as the
shelf.

### And the rebuild found a trap the sprite change had left behind

The script tag for `assets/icons.js` had been added to **the 121 documents that carried a glyph at
that moment**, and to no others. `header.html` was one of the 39 that carried none, so the moment it
gained the product's header its 20 references resolved to nothing: **20 of 20 empty, and the console
said nothing**, because a `<use>` with no target fails silently. That is the exact failure the sprite
file's own header comment warns about, arriving from the other direction.

**Every document carries the loader now**, all 160, whether it draws a glyph today or not. A page
that gains an icon later is the normal case in a kit that is still being written, and a loader that
is added per-need is a trap set for the next edit rather than a saving.

**Verified on the rebuilt page:** 72 kids and 31 classes against the product's 72 and 31, 20 of 20
glyphs drawn, both dropdowns pinned static at 260x185 in both themes, 6 figures with 0 clipped, 0
horizontal scroll, 0 console errors, at 390 and at 1280.

**21 pages remain and they are listed above.** Backlog 79.

Written: `ui-kit/header.html`, `ui-kit/_page.css`, 39 documents, `docs/backlog.md`.

---

## 2026-08-09 - The one file had to be a script, because these pages are read from disk

**Reported, not found: "after we fixed the icons, the icons started having problems".** The report
was right, the cause was an entry below this one, and the price it named out loud is the price that
came due.

Backlog 69 made the sprite one file, `assets/icons.svg`, reached as
`<use href="../assets/icons.svg#i-name">`. That is a **cross-document reference**, and the entry
below states the consequence and calls it a stated price: `file://` gives every file its own opaque
origin, so a page opened by double-clicking it resolves none of them. Measured again today, the same
pages over both protocols in the same browser:

| | over http | over `file://` |
|---|---|---|
| `ui-kit/iconbtn.html` | 10 of 10 drawn | **0 drawn, 10 empty, 10 console errors** |
| `ui-kit/navitem.html` | 6 of 6 | **0 drawn, 6 empty** |
| `ui-visual/event-feed.html` | 34 of 34 | **0 drawn, 34 empty, 39 errors** |

The stroked inline marks drew fine in every case, which is exactly what the screenshots showed: a
hamburger and a plus and a cross where there should also have been a bell, a bookmark, a clock and a
chat.

**What was wrong was not the one file, it was the FORMAT.** Everything the earlier entry argued for
holds: one file, no drift, 20 KB against 1,756. What it got wrong is a fact about how this repository
is used, and no measurement of bytes could have surfaced it: **these pages are opened from disk.**
The price was written into the head of all 121 documents, which is the right way to state a price and
is not the same thing as a price being acceptable.

**`assets/icons.js`**, then: the same 29 symbols, injected as the first child of `<body>` by a classic
script. A script has no cross-origin rule of that kind, so it loads from `file://` and from a server
alike, and every `<use href="#i-name">` is same-document again. `<use>` is live, so a reference that
found nothing at parse time updates the moment the symbol is inserted. **2,211 references repointed,
121 script tags added, 121 pointer comments rewritten**, and `icons.svg` is gone rather than kept
beside it, because two copies is the drift this whole thread exists to end.

### And the paint test found two glyphs that had never been visible

`getBBox` says a reference resolved. It does not say anything paints, which is the trap this
repository already wrote down about a mask, one layer up. Reading `fill` and `stroke` on the `<use>`
instead:

**`.footer-trust .tr-ic` and `.toast .ic-sm` both declare `fill:none`** for the stroked mark they
were written for, at (0,2,0), and the floor `svg.ic:has(use){fill:currentColor}` is (0,1,2). So the
component won on fill, `stroke:none!important` won on stroke, and **the glyph had no paint at all**:
three trust marks per screen and the toast's error mark, invisible everywhere they stand, since the
day the filled family arrived. It is `fill:currentColor!important` now, beside the stroke that was
already important. **692 unpainted references across the tree went to 0.**

### The four other things the same reading turned up

- **The nav bar was a narrow strip.** Fixed as a row two hours earlier, but the cell is a flex ROW,
  so the bar shrank to its content instead of filling the cell the way it fills a phone. The cell is
  a column now.
- **Two buttons on `state-block` were underlined.** They are `<a class="btn">`, and **the product
  never once uses an anchor as a `.btn`**: all of them are a `<button>` inside an `<a>`, which is why
  no underline was ever seen and why `.btn` has no `text-decoration` rule to lose. The specimen was
  the only place in either tree doing it. Fixed as the specimen, not as a rule, because a rule for a
  case the product does not have is a face with no placement.
- **`bets-table` was missing `.hold-col`.** `.hold-cols` is a flex ROW of two columns, each with a
  heading and its rows; the specimen put the rows straight into it, so two rows sat side by side and
  read as one line of noise. **And the dark and light halves of the same figure had drifted**: the
  same two activity rows in a different order. One figure, two contents.
- **`card.html` showed neither of the product's two cards whole.** No action row at all, so the page
  about the card was missing the one control a person presses on the feed, and no multi-outcome
  variant. Counted on `event-feed.html`: **9 binary cards with `.yesno`, 3 with `.options`**. Both
  are on the page now, and the structural difference is named: the odds-bar script skips any card
  holding `.options`, because one bar cannot say three probabilities.

The "How it works" sheet was read and is correct: `.hiw-label` is a kicker above the tagline rather
than a heading, and its marks were among the invisible ones.

### The measurements

**320 renders over both trees at both widths, over http AND over `file://`, identical on both**:
3,221 glyphs drawn, **0 empty, 0 unpainted**, sprite present on every page, 0 horizontal scroll, 0
failed requests, 0 underlined `.btn`. The one console error over http is the browser's own favicon
probe, which has no matching response event and is the case lesson 7 of the deleted instrument was
written about.

Written: `assets/icons.js` (new), `assets/icons.svg` (deleted), 121 documents, `components/base.css`,
`ui-kit/card.html`, `ui-kit/bets-table.html`, `ui-kit/navitem.html`, `ui-kit/state-block.html`,
`DESIGN.md`, `STRUCTURE.md`, `NOTICE.md`, `docs/backlog.md`.

---

## 2026-08-09 - Four pages of the kit were showing an arrangement with the arrangement taken out

Asked in four separate sentences and it turned out to be one fault four times: **the nav slots are
broken, some icons on `iconbtn` are gone, the patterns are practically empty, and the card-grid card
has no photograph and no odds bar.** All four were read in a browser before anything was touched.

### The bar was three loose anchors, and the first thing checked was whether it was mine

`.tk-stack{flex-wrap:nowrap}` had gone in an hour earlier, so the first move was to put the old value
back with `addStyleTag` on the same loaded page: **the layout came back byte for byte identical**, and
the cell is not a `.tk-stack` at all. Not a regression, and worth the two minutes.

What it is: `.nav-item` is `display:block;width:100%`, and its own file says *width:100% is the whole
reason this class exists as a row*. **The width it fills belongs to the `<li>`**, and `.bottom-nav li`
is `flex:1` inside a `ul` that is `display:flex`. The specimen had no list. So each anchor filled the
whole cell instead: **477px each, three of them wrapping onto three lines**, and the current one
squeezed to **41px** because the `<div aria-current>` around it was a flex item that shrank to its own
text. The page even explained the wrapper, correctly, as the way `aria-current` is reached from an
ancestor; it just used a `<div>` where the product uses `<li>`.

**This is the same fault as the bet pick two hours earlier**, and the second instance is what makes it
a rule rather than an incident: a stand class standing in for a product container does not show the
atom, **it shows the atom with its arrangement removed**. It is `<nav class="bottom-nav"><ul><li>` now.
One thing differs and is declared: the bar is `display:none` from 640 up and `position:sticky`, so
`.tk-show-nav` pins it visible and static. As a modifier, not as `.tk-theme-fig .bottom-nav`, because
on `bottomnav.html` the bar IS the subject and its absence above 640 is the fact that page teaches.

### The icon page: one real finding, one instrument defect of my own, corrected before it was reported

**The instrument was wrong first.** Four glyphs were flagged as clipped, `i-bookmark-b` at 18x20 in a
16x16 box and `i-chat-b` at 20x20 in 18x18. **`getBBox` returns USER units and a bounding rect returns
CSS pixels**: 18 of 24 units inside a 16px box is 12px. Comparing the two is comparing nothing, and it
is the same family of error as the mask that `getBBox` could not see. There are no clipped glyphs.

What is real, over 18 icon buttons read against 13 in the product:

- **The plain circle carries three marks and the cell showed one.** The hamburger on 105, the bell on
  32, the bookmark on 105, which is the 242 the page already had written under it. **A count can be
  right while the picture under it is a third of the thing.** The third one wears `.desk-only`, so on a
  phone the header's Favorites circle is not there at all and the bar's slot is.
- **The photo close was missing the class all 333 of its placements carry**, `.sheet-close`. The prose
  above it already said "all 333 are a sheet close"; the markup did not.
- **`.toast-close` holds no mark at all, and neither does the product's.** 24x24, 0 `<svg>`, content
  the text character `x`, nothing on `::before`. **333 close controls in the same family draw a real
  stroked cross.** One job, two drawings, the same shape as the circle-against-triangle row, and it is
  the product's to fix: backlog 75.

### Four of the six pattern pages had no specimen at all

Counted rather than eyeballed: `.tk-theme-fig` on `card-grid`, `browse-shell`, `detail-shell` and
`position-list` was **0, 0, 0, 0**. They are prose with a rule and an anti-rule and nothing rendering
underneath. `patterns.html` had cells, and `action-bar` and `list-head` had two each.

The kit's own note says this rung "has almost nothing to look at", and that is true of the rung and
is not the same claim as four pages showing nothing. **A pattern that carries only arrangement still
has an arrangement, and a page about a rule with nothing under it cannot be checked by reading it.**
Each of the four now opens with the real thing: `.grid` with three cards, `.cat-layout` with its rail
and column, `.ed-layout` with the panel beside the reading column, `.pos-list` with three rows, both
themes, the markup the screens ship.

### The card had no photograph and no bar, and the two have different causes

**The photograph is a datum and the specimens had dropped it.** The product writes
`<span class="thumb" style="background-image:url(../assets/event-politics.jpg)">`, one of the three
inline styles the rules allow. Ten cards on `patterns.html` and four on `organisms.html` carried the
`<span class="thumb">` and not the value, so **14 of 14 rendered a grey box**. Measured as
`backgroundImage === "none"` rather than by reading the markup.

**The odds bar is in no screen's markup.** A page script reads `.prob-line .prob`, builds
`<div class="oddsbar">`, hides the line and inserts the bar before `.yesno`. The product's feed has
**one occurrence of the word in its source and nine bars in its DOM**. A stand does not run the
product's scripts, so it writes what the browser renders, which is what `card.html` had already been
doing by hand. Now the shelf does too.

That is the third component of three whose visible content is not in its markup, and the browse
shell's rail is the second, so the new `browse-shell` specimen writes that by hand as well and says
so.

### The backlog's own numbers, item 74

Closed the same day it was opened. **The rule used to resolve it: a number belongs to the row that
documents OUTSIDE the backlog cite.** Grepped: `consolidation.md` and this file cite 29 for the icon
stroke and 52 for the component headers, and **nothing outside cites 25 or 26 at all**. So the two open
collisions were split with the later-written row taking a fresh number and saying so in its own text,
`.amount-input` 25 to 76 and the featured hero 26 to 77. The two closed collisions keep their numbers,
because renumbering a closed row rewrites the record for a reader who will never act on it. **Every
number is unique now and the highest is 77**, so the count is something a reader can check.

### The measurements

| | |
|---|---|
| renders, both trees at 390 and 1280 | **320** |
| horizontal scroll / failed requests / console errors | **0 / 0 / 0** |
| glyphs drawn, blank | **3,217 / 0** |
| thumbnails with no photograph | **14 before, 0 after** |
| pattern pages with no specimen | **4 before, 0 after** |
| nav slots, at 1280 / at 390 | 3 on 3 rows, one 41px wide, before; **3 on one row, both widths, after** |
| odds bars on the pattern shelf | **0 before, 10 after** |
| control heights the stand draws and the product does not | **0**, unchanged by any of this |

Written: `ui-kit/navitem.html`, `ui-kit/iconbtn.html`, `ui-kit/card-grid.html`,
`ui-kit/browse-shell.html`, `ui-kit/detail-shell.html`, `ui-kit/position-list.html`,
`ui-kit/patterns.html`, `ui-kit/organisms.html`, `ui-kit/_page.css`, `ui-kit/CLAUDE.md`,
`docs/backlog.md`.

---

## 2026-08-09 - A control's parity was being decided by the font, and the shelf was drawing a button the product does not have

Two findings, one question. Asked plainly: **why is a button on the patterns shelf so much taller
than any button in the product, and why is a control 47 tall rather than 48 or 46.** Both were
looked at in a browser: **160 pages of both trees at 1280 with a mouse and at 390 with a real touch
context, 320 renders, 13,021 controls.**

### The stand was participating in the specimen, on six classes

`.btn-md` renders **47** on all 575 of its placements and **68** on the two pages whose only job is
to show what a `.btn-md` is. The chain, read rather than guessed: `.tk-pair2` is a grid, so the cell
is as tall as the taller theme (218px); `.tk-theme-fig.tk-stack` is a **column flex container that
inherited `flex-wrap:wrap` from the row cell**, and a multi-line column container with a definite
height hands its free space to its items instead of leaving it at the bottom; that pushed `.cta-bar`
from 55 to 76, and the bar's own `align-items:normal` is stretch, so the button went to 68. **Proved
by toggling one property at a time**: `flex-wrap:nowrap` gives back 55 and 47, and every other
candidate moved the width and left the height at 68.

Five more, and they are three different causes wearing one symptom:

| class | product | stand | the cause |
|---|---|---|---|
| `btn-md` | 47 | 68 | the wrap above |
| `yesno-pick bp-side` | 70.5 | 66.5 | **two causes at once**, and the first hid the second |
| `nav-row-stack` | 49 at 258 wide | 65.5 at **148** | at 390 the shelf's two theme columns leave each specimen ~143px, and no placement is that narrow |
| `yesno-pick-bar` | 51 | 52.5 | the same 143px, and the missing container below |
| `chip-nav` | 47 | 48.5 | the specimen wears a count **no `.chip-nav` in the product has** |
| `chip-lane` | 40.5 | 37.5 | the specimen is missing the count **every `.chip-lane` in the product has**, and is an `<a>` where the product ships a `<button>` |

**The bet pick is the one worth writing down.** Capped to the placement's width, 288 for the pair,
each pick came out 140 wide, the product's own number, **and still drew 66.5 against 70.5.** The
other 4px is `betpanel.css:57`, `.bp-dir .bp-side .bp-pct{margin-top:4px}`, a rule keyed to the
container the product puts the pair in. The specimen sat in `.tk-pair`, so **the component's own
stylesheet could not reach it.** A stand class standing in for a product class is a copy of the
markup, which is the one thing this kit is not allowed to hold. It is `.bp-dir` now, and the dock
pair is `.bet-dock`, exactly as the screens ship them. The dock is `display:none` from 760 up, so
that cell gets the third `.tk-gone` modifier, `.tk-above-760`; the file's own sentence said "a third
would be a face with no placement", and a third placement turned up, so the sentence was answered
rather than argued with.

**And the chips are the sharper half.** `chip.html`, `catnav.html` and `patterns.html` all put the
count on `.chip-lane` as a `<button>`, which is what the product does. Only `vitrine.html` put it on
`.chip-nav` and left the lane bare. **The atom shelf disagreed with the product and with the four
other places in the kit that show the same component**, and the disagreement was 1.5px, which is
exactly the size that never gets noticed by eye.

Below 640 the two theme cells stop standing side by side. That is a real cost, taken on purpose:
side by side is the reason this vitrine exists rather than a set of screenshots, but **a component
measured in a cell narrower than any placement is not the component**, it is that label at that
width, and comparing two of those against each other compares nothing. `organisms.html` had already
taken the same bargain by hand for the same reason.

**After: 5 stand-only heights at 1280 and 6 at 390 both go to 0.**

### The height had no scale, and the parity was the font's decision

Twenty distinct heights on 5,004 controls at 1280, and **the split is total: every height that
landed on the 4px grid came from a token, and every height that did not was accumulated** out of
padding plus a border plus a line box. 2,907 readings of 5,607 accumulated.

**The part that decides parity is the one part this system never declared.** Padding and border are
on the ladder. `line-height` on a control is `normal`, which is the font's opinion, and DM Sans
returns **21px at 14px, 18px at 12px, 16.5px at 11px**. So from the same padding ladder `.btn-md`
came out 12+12+2+21 = **47** and `.btn-sm` 8+8+2+18 = a clean **36**. The parity was flipping on the
font size, and **no value in `--space-*` could have fixed it**, because 21 is odd and the padding is
symmetric. Every fractional height in the product says the same thing out loud: 32.5, 34.5, 37.5,
40.5 are the line boxes 16.5, 19.5 and 22.5.

**Decided: the height is the token and the padding is what is left over.** `--control-28 / 48 / 56`
join `32 / 36 / 44`, and a size sets `--control-h`. **The rungs are values the product already draws
on 105, 575 and 6 placements**, which is the answer to this block's own standing argument: 52 was
removed on 2026-08-03 under "a ramp is not a reason to keep a step", and that was right about a rung
nobody drew and says nothing about a rung everybody draws. `.btn-md` goes 47 to 48 and `.btn-lg` 55
to 56: **one pixel on 581 placements**, against a geometry axis that finally has a scale.
`.btn-bare` is the one member left out, and the file already said why: it has no box, so a height on
it would be inventing one.

**A floor is not an assignment, and declaring a height is what proved it.** The 44px touch floor in
`base.css` is `(0,5,1)` on purpose, so it out-specified `.btn-md`'s new 48 and replaced it with 44;
the content then held the box at 47, and **the same button stood 48 under a mouse and 47 under a
finger** - the exact defect the ladder was declared to end. It reads
`max(var(--control-44),var(--control-h))` now, which is what the surrounding paragraph always said in
words. `--control-h` is declared with `@property ... inherits:false` and a 0px initial, for two
reasons: the unset case is `max(44px,0px)`, the floor unchanged for the fourteen families that set
nothing, and **a control's height is not something the boxes inside it are entitled to claim.**

### The measurements

| | before | after |
|---|---|---|
| stand-only heights, 1280 / 390 | 5 / 6 classes | **0 / 0** |
| `.btn-md` | 47 fine, 47 coarse, 68 on the shelf | **48 / 48** |
| `.btn-lg` | 55 fine, 55 coarse, 76 on the shelf | **56 / 56** |
| product controls on the 4px grid, 1280 | 56% | **68%** |
| product controls on the 4px grid, 390 | 66% | **78%** |
| distinct heights, the whole kit at 390 | 18 | **15** |

Verified after: **320 renders over both trees at both widths, 0 horizontal scroll, 0 failed
requests, 0 console errors, 3,211 glyphs drawn and 0 blank**, and the absence labels read at
**fifteen widths including every boundary the system declares, 180 readings, 0 contradictions**.

**Two records were wrong and are corrected rather than left.** `button.css` said the touch floor's
effect here was "sm 36 on 137 placements and xs 25 on 72, 209 boxes": **25 is `.btn-bare`'s height
and 72 is `.btn-bare`'s count**, so the paragraph was never measuring `xs` at all. It is xs 28 on
105, sm 36 on 138 and bare 24.5 on 72, **315 boxes**. And `ui-kit/geometry.html` section 06 still
carried the 10-screen census of 2026-08-07, three declared heights against twelve rendered; it is
re-read against 106 screens.

**What is left, and it is named rather than rounded off: 1,738 of 5,004 controls still accumulate.**
`.nav-row` 32.5 on 365, `.chip-lane` 40.5 on 312, `.chip-nav` 47 on 285, `.nav-row-stack` 49 on 210,
a bare `<summary>` 34.5 on 193, `.btn-bare` 24.5 on 72, `.chip-rail` 26 on 63. Backlog 40 stays open
on exactly those, re-measured.

Written: `components/tokens.css`, `components/button.css`, `components/base.css`,
`ui-kit/_page.css`, `ui-kit/vitrine.html`, `ui-kit/geometry.html`, `DESIGN.md`,
`components/CLAUDE.md`, `ui-kit/CLAUDE.md`, `docs/backlog.md`.

---

## 2026-08-09 - The sprite becomes one file, and the copy in 112 places had already drifted

Backlog 69 asked whether the icon sprite is a shared block every screen carries whole or a per-screen
thing that something has to trim. **Costed in a browser before deciding, not argued:**

| | sprite | painted tree | what it costs |
|---|---|---|---|
| inline, as it was | **1,756.7 KB** | 7,530.7 KB | nothing, and 23.2 per cent of every page is icons |
| trimmed per screen | 921.4 KB, 52 per cent | 6,695.4 KB | a machine, or a silent failure on every future edit |
| **one external file** | **18.8 KB, 1 per cent** | **5,834.5 KB** | the tree must be served |

29 symbols are defined on a screen and **14.0 are used on average**, so half the bytes on any given
page were for glyphs that page does not draw.

### The second reason, which a byte count does not show

Building the one file found that **`i-bookmark-b` was two different drawings**: the product's on 111
documents and an older one on 3 kit pages, `bottomnav`, `card` and `navitem`. **A block copied into
112 places drifts, and nothing can see it, because every copy is internally consistent.** The stand
had been showing a bookmark the product does not ship, and it survived the pass that removed seven
such glyphs two days earlier precisely because it is not an extra glyph, it is a wrong one under the
right name. The one file keeps the version on 111 documents.

### What was verified before committing to it

**`currentColor` crosses the document boundary.** An external `<use>` is a reference into another
document, and the whole icon system takes its ink from a role token through `currentColor`. Measured
on a test page: a brass ancestor gives the external glyph `rgb(199, 162, 78)` and a green ancestor
gives `rgb(74, 222, 128)`, both painting 32.8 x 36.7. `getBBox` also still works through the
reference, so the ink instrument survives.

### The price, stated rather than discovered later

**`file://` treats every file as its own origin and blocks the reference.** A screen opened from disk
draws **0 of 34 glyphs and fills the console with 39 errors**, while its fonts, its panel and its
photographs are unaffected. Before this change the tree was fully openable from disk.

It is the right trade for this artefact and the reason is not only the bytes: the canonical way these
screens are read is **served**, on GitHub Pages, which is what `README.md` links to, and every
measurement in this campaign has been taken over `python3 -m http.server`. **The requirement is made
self-announcing rather than filed**: the pointer comment at the head of all 121 documents says the
page must be served, why, what it looks like when it is not, and the one command that fixes it.
`STRUCTURE.md`, `DESIGN.md` and `NOTICE.md` carry it too, and the CC BY attribution moved into the
head of `assets/icons.svg` rather than being dropped when the inline block left.

**Proof.** 121 documents rewritten, 121 sprite blocks removed, **2,086 references repointed**. 92
renders over both trees at both widths: **917 of 917 visible glyphs drawn, 0 blank, 0 failed
requests**. Four stale comments about symbols "spliced rather than retyped" went with the blocks they
described. The 19 archived screens under `ui-visual/old/` keep their inline sprites, because frozen
provenance has to render as it was. One throwaway script in the scratchpad, run and deleted.

Backlog 70 said `i-clock-circle-b` paints **24 x 24 at field 0** where the rule is 2, and asked for a
smaller drawing from the same set. **It paints 20 x 20 at field 2, centre 0.0 / 0.0**, the same box
as `i-sort-b` standing beside it in the same filter row. **No swap was needed and none was made.**

### A mask is invisible to getBBox

Solar delivers this glyph as a **full-cell rectangle behind a mask**:

```svg
<path fill="currentColor" d="M0 0h24v24H0z" mask="url(#SVGnNgsclOC)"/>
```

`getBBox()` returns the geometry of the painted path and never the mask, so it answered 24 x 24, and
it was right about the path and wrong about the drawing. **This is the same defect as the stroke that
closed a knockout, one layer up**: an instrument that reads the drawing instead of the paint. It is
the eleventh of the pass.

The replacement instrument is **ink**: paint each symbol into a canvas at 20x, find the opaque
pixels, convert back to user units. It sees masks, holes, strokes and antialiasing, because it is
looking at what a person looks at.

### What ink found once it was looking

Read across the filled family of 20: **field 2.0 on 17, 3.0 on one, 3.3 on two, and one glyph inside
the rule.** Not the clock. **`i-magnifer-o` painted 21.5 x 21.5 at field 1.23**, while its own caption
on the page claimed 19.4 and 2.3, a number that matched neither the geometry nor the paint and was
left over from the drawing it replaced two days earlier. It is **bigger** than the set, not smaller:
everything else paints 20.

### Both taken

- **The clock is one `evenodd` path**, Solar's two published subpaths composed with a fill rule
  instead of a mask. Compared pixel for pixel at 40x: **834 of 921,600 differ, 0.09 per cent**, all
  of them the antialiased edge of the hand. What went with the mask is a **document-unique id in the
  sprite on 112 files**, which is backlog 45's family.
- **The magnifier is placed at `scale(.9294)` about the cell centre**, landing at 20 x 20, field
  2.0, centre 0.0 / 0.0. **No path data is altered in either case**, which is the line CC BY asks
  about, and `NOTICE.md` now states exactly what was recomposed and what was placed.

Filled family after: **2.0 on 17, 3.0 on one, 3.3 on two, 0 inside the rule**, 18 of 20 centred at
0.0 / 0.0. The line marks re-read by ink at 2.2 come back **unchanged**: 4.9 on two, 3.9 on two, 2.9
on one, 1.9 on the menu, so the page's line arithmetic was right all along.

**Proof.** 112 files rewritten, both symbols, one distinct string each. 48 product renders at both
widths: **0 unresolved `<use>`, 0 masks anywhere, 0 failed requests**, and the CSS boxes unmoved at
12x12 and 28x28, because what changed is the ink inside the box and not the box. Backlog 70 closed,
row 30 corrected, open 49 to 48. One throwaway script in the scratchpad, run and deleted.

Reported by looking at the stand: on `ui-kit/filters.html` the section titled **"the menu, OPEN"**
showed a summary, 21px of panel and a scrollbar.

### One axis was declared and two were taken

`.tk-theme-fig` writes **only** `overflow-x:auto`, added so `.chip-nav` could scroll sideways in a
fixed cell rather than be clipped. **CSS resolves `visible` to `auto` on the other axis whenever one
axis scrolls**, and the cell computes to `overflow: auto / auto`. Then the geometry: `.filter-panel`
is `position:absolute`, so in the flow it contributes **nothing**, the cell measured itself against
the `<summary>` alone at **67px**, and the specimen needs **213**. The panel was not overlapping the
prose below, it was **scrolled out of sight inside a 67px box**: 146 of 213 hidden, with a scrollbar
as the only sign that anything was there.

Pinned static on the stand, the same bargain `.tk-dlg` already makes for dialogs, and **one thing
differs from the product, the position**. Everything inside the panel is `filters.css` untouched.
**146 hidden to 0, the cell 67 to 229**, both themes, both widths.

### Then the sweep reported five more, and all five were the instrument

The same read found `betpanel` and `organisms` hiding 213 to 475px inside their dialog cells. Four
candidate causes were tested in the browser and **all four changed nothing**: `overflow:visible` on
the cell, `min-height:min-content`, `align-items:start` on the two pair containers, and `flex:0 0
auto` on the dialog holder. A fix that does not move the number is a fix for a defect that is not
there.

**The readings were also unstable, 316 then 279 then 254 then 242 for the same cell**, which is the
tell. Reading the same page four times with `getAnimations().forEach(a => a.finish())` before the
measurement: `scrollHeight` **681 immediately and 402 settled**, against a `clientHeight` of 402.
**The dialog specimen was still animating in.** Across all 54 pages at both widths: **6 figures read
as clipped before the animations finish and 0 after.**

**This repository already knew.** Finishing transitions before reading computed geometry is written
into the campaign's own method, and it was dropped from this one sweep. It is the tenth instrument
defect of the pass and the second whose signature was a number that would not repeat: the first was
a whole-page style hash that reported 45 of 68 pages different when run twice against no change at
all. **An unstable number is not noise to average, it is the instrument telling you what it is
measuring.**

**Verification.** 108 kit renders, 688 figure readings, animations finished before every read: 0
figures clipping their own content, and the filters cell reads 229 with 0 hidden at 390 and at 1280.

"Couldn't load" stood under a circle on 16 screens and a triangle on 4, same sentence, same kind of
screen. **The triangle wins.** The count said circle, 16 against 4, and the convention said triangle,
which is the error mark a person already knows and the one already on the loudest two surfaces, the
main feed error and the 500. A convention beats a count when the count is an accident of the order
things were built in.

### The row's premise was one layer short

It was filed against `ui-visual/` as a paint defect. **Both trees carry the same split, on the same
files**: `wireframes/` draws a circle on the same 16 and a triangle on the same 3. So it is structure,
not paint, and the fix went **grey first**: 16 inline drawings in the grey tree, then 16 `<use>` in
the painted one. Two trees agreeing with each other and disagreeing with themselves is a defect that
neither tree's own audit can see, because every comparison between them passes.

### A shape census can only find a duplicate that looks like one

Section 07 of `icons.html` found **seven** jobs drawn twice, by reading path data for shapes that
resemble each other. **A circle and a triangle do not resemble each other**, so the two warning marks
read as two different glyphs doing two different jobs and sat under the same sentence for weeks. This
one was found by reading what the mark stands NEXT to. The section is eight now, and it carries both
halves of the lesson: a census that reads geometry and not meaning files a logo as a duplicate
(the X mark, Discord) and misses a duplicate that is drawn differently.

### The swap emptied a glyph, so the glyph left

After 16 placements moved, `i-danger-circle-b` had **0**. It went from the sprite on **105 painted
screens and 6 kit pages**, from the stand's gallery, and from the counts: the set is **34 glyphs**,
the filled family **20**, and the sprite is 26.13 symbols per screen against 27.13. The stand keeps
the name in one place, the row in section 07 that says why it is gone. **A glyph with no placement is
not a spare, it is weight**, and the stand offering it would be the same defect fixed two days ago,
when seven drawings the product does not ship came off the shelf.

**Proof.** 212 renders over the 106 painted screens at both widths, 3,860 `<use>`: 0 unresolved, 0
circles, 40 triangle uses. Both trees read a triangle on all 20 error surfaces, painted and resolved,
titles verified one by one. 108 kit renders: gallery 34 figures, badges 34 / 20 / 6 / 8, heading
"ALL 34", 0 unresolved, 0 empty figures, 0 horizontal scroll, 0 console errors, 0 failed requests.
`DESIGN.md` and `NOTICE.md` carry the new count with the reason. Backlog 71 closed, open 50 to 49.

The sweep was three throwaway scripts in the scratchpad, run and deleted: a census of both trees'
error blocks, the grey-first replacement, and the symbol removal.

---

## 2026-08-09 - The stand printed the number under an empty plate, and the number it printed was somebody else's

"Why is the bottom bar empty" was asked about one cell on `ui-kit/bottomnav.html` at desktop width.
The cell is empty because `bottomnav.css` carries `@media(min-width:640px){.bottom-nav{display:none}}`
and the reader is at 1280. **The page already knew**: two lines below the empty plate its own note
read "Measured on a screen: 379x56 at 390, and 0x0 at 1280". The measurement was taken, written
down, and never carried the twelve lines up to the specimen it describes.

### Six empty cells, failing in both directions

Every one of the 54 kit pages was read at 390 and at 1280, every `.tk-theme-fig`, `.tk-fig` and
`.tk-photo`, counting figures that hold markup and paint **nothing**. Six, on three pages, and they
do not all fail the same way:

| page | specimen | the rule | empty at |
|---|---|---|---|
| `bottomnav.html` | `.bottom-nav` | `bottomnav.css`, `min-width:640` hides it | 640 and up |
| `organisms.html` | `.bet-panel` | `betpanel.css`, base `none`, `min-width:760` shows it | below 760 |
| `button.html` | `.hiw-btn` | `header.css:160`, `max-width:640` hides it | 640 and down |

**The kit already owned the device and it was in the wrong places.** `.tk-absent` and `.tk-wide-only`
put a sentence in a cell that is empty on purpose, and they stood in six figures on two pages,
`molecules.html` and `vitrine.html`. Neither of the three pages above carried one.

### The number in the sentence was a real number and the wrong one

Both classes were written at **900px**. 900 is a genuine breakpoint here, six declarations across
`chip`, `hiw-dialog`, `catnav`, `browse-shell` and `toc`, and **it belongs to neither component the
labels describe.** That is why nobody caught it by eye: a borrowed number reads exactly like the
right one, because it is one of the system's own. Read at eight widths, it had bought two live bands
on the pages that did carry the label:

- **`molecules.html`, 640 to 899.** The bar is gone from 640 and the sentence starts at 900: **260px
  of silently empty cell**, the exact defect the class exists to prevent, produced by the class.
- **`vitrine.html`, 761 to 899.** The panel is drawn from 760 and the sentence stops at 900: **139px
  of a label arguing with the specimen underneath it**, reading "not rendered below 900px" beside a
  rendered panel.

**A number in a sentence is a second copy of that number**, and this one had drifted with nothing to
notice. The pair is one family now, `.tk-gone`, with the threshold in the modifier
(`.tk-above-640`, `.tk-below-760`), so the number stands in the markup next to the sentence and in
one media query, and a reader trips over a mismatch instead of having to go looking. Two modifiers
and not three, because the system has two components that do this and a third would be a face with
no placement.

### The two numbers are not mirrors, and only a boundary read says so

Written as the obvious pair, 641 and 759, the first left a **one pixel hole at exactly 640** where
the cell was empty and silent again. `min-width:640px` **hides** the bar, so the bar is gone AT 640;
`min-width:760px` **shows** the panel, so the panel is gone at 759. The two rules point in opposite
directions and their labels are 640 and 759, not 640 and 760. Found by reading 12 widths instead of
8, and it is the argument for reading the boundary rather than the middle.

### The button page had no missing label, it had a class it should not have carried

`button.html`'s ghost specimen wore `.hiw-btn`. That class has **exactly one declaration in the whole
system**, `display:none` below 640 in `header.css`, and **no face at all**: no ground, no ink, no
border, no size. It was carried onto the stand for fidelity to the header placement, and the only
thing it did there was empty the cell on a phone, so **the ghost was the one emphasis of five a
reader at 390 could not see**. A placement is not an emphasis. The class came off, the page says so,
and no label was needed.

**Proof.** 486 renders over 54 pages at nine widths including all six boundaries, 3,150 figure
readings: **0 figures holding markup and painting nothing**. The truth of every label read at 19
widths from 320 to 1440, 190 figure readings: **0 widths where the sentence and the specimen are
both showing or both hidden**, and the two flips land exactly on 640 and 760. Final pass at 390 and
1280 over all 54: 108 renders, 700 figure readings, **0 empty, 0 horizontal scroll, 0 console errors,
0 failed requests, 0 unresolved `<use>`**.

**The cache cost this repository a sweep for the sixth time.** The mid-work verification reported
every edit missing, on a port that had already served the old files. A fresh port every time, or the
measurement is of the browser.

### The same sweep found a regression from the day before, in the band nobody reads at

`icons.html` scrolled sideways from **761 to about 1025** and nowhere else. The cause is a caption:
`.tk-anat`'s left column is `auto` so the 24 x 24 cell can be exactly that, a `figcaption` has no
natural width, and **one 117-character line added to it on 2026-08-09** measured **601px on a single
line**. The grid computed `601px 0px`, the numbered steps in the second column stood **92px past the
page**, and below 760 the stacking rule hides it while above about 1100 there is room. **The page was
verified at 390 and at 1280, which are the two widths either side of the band.** Fixed as
`.tk-anat .tk-gl figcaption{max-width:34ch}`, a measure rather than a pixel, on the caption rather
than on the column, because what has no natural width here is the prose.

It is the second thing this entry records that was measured at two widths and wrong between them,
and both were found by reading the boundary instead of the middle.

### What it opened

The breakpoint census taken to check the 900: **31 media rules across 24 files at eight distinct
widths** (520, 560, 620, 640 ×13, 760 ×5, 860, 900 ×6, 980). Filed as backlog 72 for Responsive,
which owns the question of whether that is a scale or a pile.

### And then the page itself, read against what it measures

`icons.html` was rewritten section by section on 2026-08-08 and 2026-08-09, and **the newest section
corrected the older ones without the older ones saying so**. Sections 01, 04, 05 and 08 carried the
pre-consolidation numbers in the present tense while section 06 carried the post-consolidation ones
and knew it, so the page contradicted itself in writing: rule 3 said a stroke puts "0.8 of paint past
the geometry" while section 06 said 1.1 for the same rule; section 05 opened "for all 52" under a
heading that reads "ALL 35"; and section 05 sent three glyphs away to be redrawn that section 06
says are gone.

**The correction was a measurement, not a find-and-replace, and it found a bigger thing than the
stale numbers.** Read on all 106 painted screens, every svg that actually paints a stroke, **998 of
2,399**:

| box | declared | renders | placements |
|---|---|---|---|
| 12 | 2.4 `.ic-sm` | 1.20px | 266 |
| 16 | 1.8 `.market-chevron` | 1.20px | 9 |
| 16 | 2.2 `.ic` | 1.47px | 17 |
| 18 | 2.2 | 1.65px | 528 |
| 22 | 2.2 | 2.02px | 178 |

**Four boxes, not six, and 1.68 to 1 between the lightest and the heaviest, not 2.98.** The page and
backlog row 29 had both said the ratio was "exactly what it was, because the fault is the unit and
not the value", and row 29 went further and offered a multiplier: "multiply every figure in this row
by 1.375". Neither holds. `.ic-sm` went 1.8 to 2.4, a different factor from `.ic`'s, and **nothing
strokes at 20 or at 40 any more**, so the two boxes that were the extremes left the set. **An
argument whose evidence has moved is not a smaller argument, it is a different one**, and the sharp
end of this one went with the evidence: 0.90px is under one device pixel at DPR 1 and smears, and
1.20px is not.

**Two things the page had never named.** `market.css` writes its own `stroke-width:1.8` for the
chevron at a 16px box, 9 placements, painting **1.20px**: the same weight as the 12px marks, from a
different number, at a different size, in a file the icon rules do not reach. Two declarations
agreeing by accident is not one weight, it is two that have not disagreed yet. And `.ic-sm` **is not
a size**: of **358 placements, 354 are 12px and four are not**, all four on the toast, where
`toast.css` rewrites the box to 18 and the stroke to 2.2 and then again to 22 and 2.4 on the error
face. A class a component re-declares from scratch is a name the markup carries, not a size the
system owns.

Corrected in place: section 01 rule 3, section 04 heading, premise, measured range and the `.ic-sm`
note, section 05 opening and method note, the centre paragraph now says it is the hand-drawn set's
reading and points at section 06, and the consolidation plan's items 1, 2 and 6 are re-read against
the set that exists. Backlog rows 29 and 30 carry the same re-measure, including the correction of
row 29's own multiplier written earlier the same day. **The old numbers are kept everywhere and
labelled**, because this page's method is the reading and what it was.

**Verification.** 540 kit renders at ten widths, 3,500 figure readings: 0 horizontal scroll, 0 empty
figures, 0 label contradictions, 0 unresolved `<use>`, 0 failed requests. One console 404 appeared in
the stream and **did not reproduce** under 28 renders with response capture at `networkidle`, which
is the fourth time that phantom has been chased and not caught; it is written here as not reproduced
rather than as zero.

---

## 2026-08-09 - The set shipped as blobs for a day, and the stand is structurally blind to it

Three things were reported by looking at the product: the magnifier is a solid disc, the warning on
the screen is not the warning in the design system, and the trust marks look strange. **They are one
defect, one design choice and one leftover.**

### A stroke closes a knockout

Solar Bold draws detail as a **hole**: the exclamation inside the warning triangle, the tick inside
the shield, the meridians on the globe and the lens of the magnifier are subpaths cut out of one path
with `fill-rule:evenodd`. **A stroke outlines every subpath, including the holes.** 2.2 units of brass
drawn around a 2 unit exclamation closes it completely, and what ships is a solid blob.

`svg.ic:has(use){stroke:none}` was already there and it lost. It computes to **(0,1,2)**, and
**fifteen component rules paint an icon with `stroke:` at two classes, (0,2,0)**. So on every surface
that gives its icons a colour, and only there, the glyph went solid: the state block, the trust
tiles, the toast, the nav slot, the hiw sheet.

**And the kit drew all of them correctly the whole time.** A specimen stands in `.tk-cell`, where no
component rule reaches it, so the one place the defect was visible is the one place nobody was
looking. **A stand is structurally blind to a defect that lives in the container.** That is the
sharpest limit of the vitrine found so far, and it is worth more than the fix.

It is `stroke:none!important` now, in `base.css`, with the reason above it. `!important` is right for
the same reason as the other four in that file: it is a floor the system declares and no component
may argue with, not a patch for a selector somebody wrote badly.

### The magnifier had no hole, and that one was a choice rather than a bug

`minimalistic-magnifer-bold` is a solid disc with a handle **by design**: Solar's Bold weight fills
the lens. Asked for a lens with a hole, the answer is Solar's **Outline** style, `magnifer-outline`,
which is still a filled glyph with no stroke and therefore still obeys the rule. **The set is Solar
Bold plus one Outline**, said out loud rather than quietly: `i-magnifer-o` is named for its style so
the next reader does not "correct" it back.

### The third trust mark was a line among two filled ones

The footer trust row said its third claim with the bare tick, which is a **movement** and correctly a
line by the rule written yesterday. Beside a filled shield and a filled globe it read as a different
set. A tick that is a claim rather than an action has an object form: `i-check-circle-b`, **105
placements swapped**, and the row is three marks of one family.

### And the warning is still drawn twice

With the stroke fixed, the triangle matches the stand. What remains is that **the product says
"Couldn't load" with two different marks**: `i-danger-circle-b` 16 times and `i-danger-triangle-b` 4,
for the same sentence on the same kind of screen. That is the defect this whole pass exists to
remove, found one layer in. **It is filed rather than taken**, because the count says circle and the
convention says triangle, and that is a choice rather than a measurement. Backlog 71.

---

## 2026-08-09 - The icon set consolidates, and "make them all filled" turns out not to be available

Backlog 31, and it was the one item the consolidation pass would not take alone, because it is a
product decision rather than a value. The decision taken was **filled**. What shipped is filled for
everything that can be, and the difference between those two sentences is the entry.

### 33 stroked marks were read against Solar Bold and six of them have no filled form

Not for want of a library. **A cross, a chevron, a plus, a tick and a hamburger are movements, not
things**: they have no interior, so there is nothing to fill. What a filled set offers instead is a
disc or a plate with the mark knocked out of it, which is why Solar names them `close-circle-bold`
and `add-circle-bold` rather than `close-bold` and `add-bold`. **A disc inside a round icon button is
a disc inside a disc**, and the sheet close stands in exactly that. Material and SF Symbols draw the
same six as lines inside their filled sets.

**So the rule is: an object is filled, a movement is a line, and what holds them together is WEIGHT
rather than style.** 21 filled glyphs over **1,517** placements, 6 line marks over **990**. The
stroke was 1.6 against the solid mass of Solar Bold, and that gap is what the eye reads as "two icon
sets": it is **2.2** at 22px and 2.4 at 12px, chosen by standing a line mark next to a filled one at
both sizes rather than by picking a number.

**The set is 35 glyphs where it was 52**, and 17 of the 17 that left were a second drawing of
something already there.

### The row named four crossed pairs and two of them were logos

`close` had a "second drawing" and it is the **X mark in the footer**; `chat` had one and it is
**Discord**. Both were filed as duplicates by a census that reads path data, and **a shape census
cannot tell a logo from a control**. The five social marks and the three sign-in providers keep their
own drawing, take no system ink, and no generic glyph may stand in for one, **because a paper plane
is not Telegram**. That is written down now rather than assumed.

### The ink was the other half of the defect, and it was invisible

A stroked mark takes its ink from `stroke`; a filled one takes it from `fill:currentColor`, which
resolves to `color`. **Nine `:has(use)` rules already existed** for the first filled handful, and
three of them disagreed with the stroke beside them. So the header's bookmark shipped at
`--text-primary` on the screens where it was filled and `--text-icon` on the screens where it was
stroked: **the same mark, the same job, the same header, two inks**, and nothing that reads a
stylesheet would ever have found it.

Fifteen rules now name both properties, and three places were levelled to one ink: the bottom-nav
slot to muted, which is what its own label takes; the header cluster to the icon token; and the
account-menu bell, whose exception was written because it was the one filled mark in a stroked row
and left with the reason.

### The licence was being relied on and not honoured

Solar had been shipping in this repository since the Vault pass under a comment reading "Solar Bold
icon sprite" and **no attribution anywhere**. It is **CC BY 4.0**, by **480 Design**, which asks for
the author, the licence and whether the work was changed. **Naming an asset is not crediting it.**
`NOTICE.md` is new and holds every bought-in asset: the icons, the three OFL type families, and the
photographs, which are placeholders cleared for nothing and are filed as a handoff question rather
than assumed. The credit also stands in `DESIGN.md` and in the sprite comment on all 105 screens,
which is the place a person reading the markup actually meets it.

### The proof

Two trees on two origins, the before tree exported from `3282cf6`. **40 painted screens at 390 and
1280 in both themes, 5,064 icon readings** of box, kind and ink.

**0 boxes moved.** Not one icon changed position or size, which is what a swap of glyph for glyph
inside the same `viewBox` and the same `.ic` box is supposed to do.

**Every ink difference that remains is one of the three levellings above**, named and counted, and
there are no others.

### THE STAND WAS NOT REBUILT WITH THE SYSTEM, AND THAT IS THE WORSE HALF OF THIS ENTRY

The first pass swept `ui-visual/` and six kit pages and **deliberately skipped
`ui-kit/icons.html`**, on the grounds that a foundation page is written by hand. Its prose was then
rewritten to say 35 glyphs, 21 filled, one rule. **Its galleries were not touched, so the page went
on drawing the 52 hand-made glyphs it had always drawn while claiming the opposite in the paragraph
above them.**

That is worse than leaving it alone. A stand that lags the system is a stand nobody can trust; a
stand that lags the system **and says so in the past tense** actively misinforms. It was caught by
being asked what had changed in the design system, and the answer was: on that page, nothing.

Rebuilt, and measured rather than typed. Every glyph rendered in a 24 cell and read with `getBBox`
plus the half-stroke that paints outside the contour: **21 filled, 6 line, 8 brand, 35 figures with
their painted extent and their safe field**. Sections 01, 02, 04 and 05 too, which were still
standing the old drawings and quoting numbers taken at 1.6.

**And 15 of the 21 filled figures rendered EMPTY on the first attempt**, because a kit page carries
its own sprite and the new symbols were never added to it. Same defect as the swap itself, one level
up: `<use>` fails silently. The page now asserts it, and so does the check that runs over the tree.

### AND THE STAND WAS STILL OFFERING FOUR GLYPHS THAT SHIP NOWHERE

Section 03 kept the four crossed pairs as **live specimens**, stroked twin beside filled one, under a
caption reading "as they stood until 2026-08-09", with a paragraph under it saying all four now
stand as the filled glyph only. It was read, by the person the stand is for, as a stroked bookmark
and a stroked bell still being in the design system.

**They were right and the caption was not a defence.** A reader who scans a grid of glyphs is reading
the pictures, not the label above them. The path data is a record and belongs in a table; the drawing
was an offer. The four are written now and not drawn, in the same shape `trustbar.html` used when the
strip was deleted: a table of what was there, and no specimen of it.

**And asking that question of the whole kit found six more, five of them older than this pass.**
Every glyph any kit page draws was compared against every glyph the painted tree ships, with the
markup normalised so that `<path></path>` and `<path/>` count as one:

| page | it drew | it should have drawn |
|---|---|---|
| `iconbtn.html` | the stroked swap | `i-transfer-horizontal-b`, and it was missed by the sweep itself because the markup is written `<path></path>` and the pattern was not |
| `hiw-dialog.html` | a plus and a bar chart | `i-check-circle-b` and `i-graph-up-b`, the marks the sheet actually carries on 106 screens |
| `state-block.html` | a three-line list | `i-inbox-b` |
| `toast.html` | a tick at other coordinates, and its own warning triangle | the product's tick, and `i-danger-triangle-b` |
| `vitrine.html` | its own exclamation | `i-danger-triangle-b` |

**A stand that draws its own glyph is a second icon set with one placement.** Five of these predate
the consolidation and none had ever been noticed, because nothing compares the stand to the product.
That comparison is now an act somebody can repeat, and it reads **0**.

### What the rebuilt audit found

**The centre drift this page opened with is gone, and the consolidation removed it.** `sort` at -2.0
across, `trend-up` at -2.0 down and `music` at -1.7 / -0.8 were three drawings to correct; they are
not drawings any more, and **19 of the 21 filled glyphs sit at 0.0 / 0.0**, the other two off by 0.2
and 0.3 of a module. Taking a set from a grid bought more than three hand corrections would have.

**One filled glyph paints the whole cell and it is the clock.** `i-clock-circle-b` is 24 x 24, field
**0**, where 17 of 21 sit at exactly 2.0. Beside `i-sort-b` in the same filter row it reads a size
larger. Backlog 70, filed rather than fixed, because choosing the replacement is a look at four
candidates and not a measurement.

**The line marks keep the arithmetic the page named in rule 3.** Their fields all end in `.9`, being
a whole-module contour plus the 1.1 of stroke that paints outside it, exactly as they ended in `.2`
at 1.6. The menu is the one under the floor, at 1.9, by a tenth.

### And the cache was paid for a fifth time

The first ink reading reported the hiw marks, the state blocks and the market title still wrong after
they had been fixed, because the browser was holding the old component stylesheets while serving the
new base. A fresh port, and they read correct. This repository now has five entries that end the same
way.

---

## 2026-08-08 - The action bar becomes one face, a component is deleted for it, and the outcome becomes a modifier

Backlog 63 and 66, measured together and shipped together.

### 63. Three placements, three faces, and the declared one was worn by nobody

`.cta-bar` stands on three painted screens and that is the pattern threshold exactly. Read on those
screens: the pattern declared `position:sticky` and **0 placements used it**; `.static` was worn by
the wallet and `.flat` by how-it-works and my-profile. So **two modifiers between them covered every
placement in the product, and the thing they modified was the thing nobody used.**

The row put it as a binary: either the plate is the face and two screens are wrong, or the flat row
is the face and the plate is the variant. **What answered it was the shape of the stone rather than
the count.** The stone is what a bar needs when it FLOATS, a ground and a top edge against content
scrolling underneath, and the rule said so itself: `border-radius` on the **top two corners only**
and a border on the **top side only**. An open-bottomed dock. Nothing in this product docks, so on
the wallet it was a dock shape sitting mid-column with its bottom cut off, under a card and above a
line of small print. Spreading it to the other two would have meant redrawing it, because the same
open bottom would have been wrong twice more.

**So the bar is one face: static, no stone, padding above.** `.flat` and `.static` are gone.

### The consequence I did not see when I recommended it, and it is the whole of a component

`components/account.css` was **two rules**: the stone, and the three declarations `.flat` removed it
with. With the stone deleted the file was comments. **A component with no face left is not a
component with a small stylesheet, it is a name**, so it went with its `@import`, its shelf section
on `molecules.html`, its row in the inventory and its page in the kit. **The vitrine is 54 pages, not
55**, and the tally in the panel is computed from `_nav.js` so it said so on its own.

Its writing is not lost: `ui-kit/action-bar.html` absorbed it, which is where the rest of the bar
already was. The bar had been two components and two stylesheets since the pattern cut, and both kit
pages complained about the split in prose. **The exception that cut declared, that a component keeps
its own paint, has nothing left to except.**

**What this costs is named rather than hidden: there is no sticky action bar in the system any
more.** The day a screen needs one it is designed rather than inherited, and it will need the stone
back with it, because the two were always one decision. A capability nothing used, against a default
nobody wore.

### 66. The last container scope, and the argument for it was real

`.outcome-dialog`, `.win-dialog` and `.loss-dialog` recoloured the reconcile box from outside: **six
rules in `notice.css` and one in `input.css`, three container scopes across two files**, not the two
in one file the row recorded. And there was a genuine argument for keeping them, which the row itself
made: a face lent by a container is a defect, but a dialog's OUTCOME reaching its content is a state
flowing the right way.

**Two readings ended it.** The painted tree drew 4 won boxes, 1 lost and 2 plain; **the grey tree
carried 6 and not one had an outcome variant**, because a grey page has no colour to say it with. A
state that exists in one tree only is not a state, it is a paint job. And **a specimen on the kit
cannot be put inside a win dialog**, so two of the component's three faces could not be stood by
anybody. A face that cannot be stood cannot be checked, which is the same argument that closed 67.

It is `.reconcile-box.rec-won` and `.reconcile-box.rec-lost` now, in both trees, grey first, the
habit `position.css` already had with `.pos-side.pos-won`. **The centred arrangement came with them
and that is a reading rather than a guess**: `.outcome-dialog .reconcile-box` centred every box in an
outcome sheet, every box in an outcome sheet has an outcome, and the two sets matched exactly, 5 and
5. Compound selectors rather than a bare `.rec-won`, **because a single-word modifier in the global
namespace is what `.flat` was**, and `.flat` is the other thing this day deleted.

### The proof

Two trees on two origins, the before tree exported from `ee21d7a`: **106 painted screens at 390 and
1280 in both themes, 424 page pairs, 428,864 element readings** over 33 computed properties and the
box.

**Three files differ and they are the three that carry a bar.** how-it-works and my-profile change
**one element each and nothing visible**: `bottom` from `0px` to `auto` and `z-index` from `4` to
`auto`, both inert on a static element, and the box stays 293x55 and 259x55 to the pixel. The wallet
changes **202 elements**, which is the bar and everything under it: **293x72 to 293x55 at 390 and
911x72 to 911x55 at 1280**, ground `rgb(21,23,27)` to transparent, a 1px top hairline to none, the
corners from `10px 10px 0 0` to 0, padding 12 to `8px 0 0`, and the page 17px shorter.

**The outcome boxes read 0 differences on all five screens**, which is what a modifier that
reproduces a container's face exactly is supposed to do.

### 60. The row was measured and there was nothing there

The row said four related rows of 31 have no thumbnail and that a row without one "starts 58px
further left than the rows above it". Measured at both widths: **all four are on `terms.html`, they
are the whole of that list, and every question in it starts at the same 68 at 390 and the same 586.5
at 1280.** None of the four is a market: the block is headed "The other documents" and the rows read
*Privacy Policy / not built*.

**A count without a grouping is a defect looking for a screen.** "4 of 31" was read from the source
and was true; what it left out is that the 4 are four of four on one screen and the 27 are 27 of 27
on nine others.

The 58px is real and was built to check it: cloning one row into the terms list and giving it a
thumbnail puts that row's question at 126 against 68, and at 644.5 against 586.5, at both widths.
**That arrangement exists nowhere in the product.** So the close is a contract rather than a rule:
the thumbnail is optional and **the list decides**, every row or no row. A rule for the mixed case
would be a rule with no reader, and the day a market genuinely has no photograph the placeholder is
something to design rather than to guess now. Written into `components/related.css` and
`ui-kit/related.html`; **no CSS changed.**

### And the patterns rung was re-counted, because it had to be

`patterns.html` published 59 declarations, 16 properties and 181 lines across the six files. The
action bar went from 13 declarations to 7, so the totals had to move, and re-reading them with every
`prop:value` outside a comment counted, media queries included, gives **53 declarations, 18 distinct
properties, 218 lines**. The 16 does not reconcile with any reading of the old file either, so the
page now names the reader beside the number. **A count is only as good as the reader named beside
it.**

---

## 2026-08-08 - The trust strip leaves, and the screen was carrying the argument against the stylesheet

Backlog 57. `.feed-trustbar` stood in the markup of **105 of the 106 painted screens**, 210 items
inside them, and the last line of `components/trustbar.css` was `.feed-trustbar{display:none}`. So
the component was present 105 times and drawn 0 times, and the only record of that decision was one
line at the bottom of a file.

### The line was not the whole story, because the markup argued the other way

Above the block, on all 105, in a comment: *"Trust cue near the action (critique P2): trust is the
persona's #1 driver, surfaced above the feed and on the logged-out first paint, **not only in the
footer**."* One hand added the strip because the footer was judged not to be enough; another hand
switched it off. **Neither hand wrote the second decision down, so the file and the markup disagreed
in writing for as long as both were there**, and a reader meeting either one alone would have
believed it.

### Two readings in the row were wrong, and the measurement corrected both

The row said the rules were not dead code because **the grey tree still drew the strip**. It did
not: `wireframes/` carries **0** `.feed-trustbar`. The grey tree answers the same question with two
`hero-trust` tiles inside the hero, so the strip existed in one tree and rendered in neither.

And the row put the decision as "either the line becomes a comment or the rules go", as though the
strip's content were unique to it. It is not. **The same two sentences are said, drawn, on the same
screens, twice**: the three tiles in the footer carry both plus a third, on all 105 in both trees,
and on `event-feed.html` the hero carries both again, **using the same two sprite marks the strip
used**, `#i-shield-b` and `#i-verified-b`. On the main feed the strip would have been the third copy
of one sentence on one page.

That is this repository's own test for a thing switched off, and it is the test `.opt-sel-tag`
passes and the strip fails: **does the same screen say it another way.** The tag stays off because
the paint says "chosen" in colour and there is nowhere else it is said; the strip goes because the
footer says it in words twelve inches lower.

### What left, and the proof it took nothing with it

11 rules and 2 icon rules from `trustbar.css`, and the block plus its comment from 105 files, swept
with a throwaway script written in the scratchpad and deleted. Five classes stopped existing:
`.feed-trustbar`, `.ft-inner`, `.ft-item`, `.ft-ic`, `.ft-sep`, all of them **100 per cent in
`ui-visual/` and 0 in the kit and the grey tree**.

Measured with two trees, the pre-change one served from a second origin: **106 painted screens at
390 and 1280 in both themes, 424 page pairs, 428,864 element readings** over 38 computed properties
and the box. **0 differences.** And in the before tree, over 420 renders, **4,200 strip elements,
every one of them a 0x0 box**: the component was as absent from the page as it now is from the file.

### The instrument defect, and it is the ninth of this campaign

The first run reported **92 pages different** and the samples looked identical. They were not:
`backgroundImage` computes to an **absolute** URL, so every element with an image differed by the
port the tree was served from. A before-and-after across two origins has to normalise the origin,
or it measures its own instrument. Normalised, the same 424 pairs read 0.

Two symbols in each page's sprite, `#i-shield-b` and `#i-verified-b`, are now defined and unused on
104 screens and used on one. That is the sprite's existing shape rather than a new defect:
`#i-seo-chart` was already defined and unused on 104, and five category marks on 48 each. Filed as
backlog 69 so the sprite is decided once rather than per component.

---

## 2026-08-08 - The frame class comes off the dialog, and the row that opened it undercounted by 22

Backlog 68, opened by the wrapper sweep and closed here. The row said "two attributes in one file".
**It was 24: 21 painted screens across 21 files, and 3 specimens across 2 kit pages.**

Every one of the 24 is a screen, or a stand, **whose subject IS a dialog**: the deposit family, the
sign-in family, the win and loss overlays, the bet sheet, the bet sheet specimen. A rule scoped to
`.app-case` could not reach a dialog, and **a descendant selector does not match the element that
carries the class**, so the wrapper could not go around the dialog either. It went ON it. That is
not a shortcut somebody took once; it is a convention 23 files followed, and it worked, which is why
nothing ever asked about it.

### It was not inert either, and this file had already written the bill

`components/dialog.css` records it in full: `.app-case` declares `position:relative`, the user agent
gives `dialog:modal` `position:fixed`, and the class took it back. **The sheet scrolled with the page
behind it: on `win.html` at 380 the page sat 412px down and the sheet's top edge was 313px above the
screen.** The answer at the time was a second rule, `dialog.app-dialog:modal{position:fixed}`, to put
back what the first one had removed.

**A workaround that has to be worked around is the shape of a scope that was never true.** The class
is off all 24 now. The counter-rule stays, because this repository does not leave a value to the user
agent when it can name it, and its comment says that rather than the old reason.

### Measured

Two trees, not two stylesheets: the pre-change markup was served from a second origin with its own
copy of `components/` and `assets/`, and each page was read twice, once per origin, element for
element. **106 painted screens and 55 kit pages, at 390 and 1280, in dark and light: 322 page pairs,
190,258 element readings**, 29 computed properties and the box.

**0 differences in the product. 0 on the kit.** The only movement in any run is the course panel's
own rows on the y axis, which is the stand's sidebar scrolling to its active row and is not the
product. On the painted tree the geometry noise appears at 390 and thins at 1280; on the kit there is
none at all, at either width in either theme.

**Why zero rather than something.** The class had exactly two live effects left, and both were
already answered: the scoped rules it existed for are gone, and the position it broke is put back by
a rule one file away. **A workaround is invisible on the day it stops being needed**, which is why
this one would still have been in the markup in six months if the sweep had not counted it.

---

## 2026-08-08 - A refactor that leaves the old layer on top has not replaced it, and the stand is what proved it

Backlog 67, opened by the wrapper sweep earlier the same day and closed here. `hiw-dialog.css` was
refactored on step 7f under a sentence it wrote out in full: THE BLOCK, NOT THE DIALOG, the hero and
the section rhythm belong wherever the block stands, and **what stays scoped is the part that is
genuinely about being a dialog, its width, its close disc and the body padding of a sheet**.

**Eight rules of the shape `dialog.app-dialog .hiw-*` were left at the TOP of the file**, above that
comment and above the new layer, and none of them is one of those three. At (0,2,2) they
out-specified every one of the block's own rules, so **inside a sheet the block never once wore its
own face**, on 105 screens, while the file read as though it did.

| what the block declares | what the sheet rendered | elements |
|---|---|---|
| `.hiw-label` 14px display bold, `text-transform:none` | **11px UPPERCASE** with label tracking | 315 |
| `.hiw-faq dt` semibold, 12 above and 4 below | bold, 8 above and 2 below | 315 |
| `.hiw-faq dl` an 8px lead-in | 0 | 105 |
| `.hiw-sec p` no top margin | 4px | 210 |
| `.hiw-body` the sheet's 8px padding | nothing, the rule was already dead | 0 |

**The file said so itself and nobody read it back.** The block's own label carries
`text-transform:none`, a declaration that exists only to cancel something. A rule cancels what
something else is doing, so whoever wrote the new layer knew the old one was there and expected it
to go. Two of the eight were `.hiw-full`, which stands only in the sheet and only needed unscoping.

### The count was eight and the finding was nine

The file's remaining `.app-case` rules had to go with them, and the reason is the sharpest thing in
this entry: **the wrapper was right about the product and wrong about the stand.** It meant "the page
rather than the sheet", which is true on 106 painted screens, and **a kit page carries `app-case` on
its BODY**. So the specimen on `ui-kit/hiw-dialog.html` was a sheet wearing the page's hero edge, the
page's 16px tagline, the page's section separators and the page's 44px FAQ indent, with the sheet's
11px label on top of it: **neither of the two things this component draws**. No screen was wrong, so
nothing but a stand could ever have shown it, which is the argument for the stand in one sentence.

The split is a class now: **`.hiw-page` on the page's hero, and `.hiw-cols` for everything else**,
which stands on one document in each tree and on no stand at all. One class added, grey first and
the colour copy after. `hiw-dialog.css` carries **0 `.app-case`**, so the system now has none outside
the class's own two rules in `base.css`.

### Measured

Same instrument as the wrapper sweep: the candidate served from a second origin and swapped into
each page in place of `index.css`, both readings in one page load. 106 painted screens and 55 kit
pages at 390 and 1280, 190,156 element readings.

**On the painted tree, 10 changes and every one inside the 105 sheets.** The How-it-works PAGE is
untouched, which is what says the class reproduces the wrapper exactly. **On the kit, the specimen
picks up 16 more**: it loses the hero's 1px edge and 16px corner, its tagline drops 16 to 14, its
sections lose a 20px separator and its FAQ loses a 44px indent. That is the stand correcting itself.

**One instrument note, and it is the fourth time in two days.** The first run of the class-based
candidate reported the page's hero losing its edge, which would have meant the class had not
matched. It had not: the server was started before the markup edit and the browser was answering
from cache with the old HTML. Fresh port, and the page reads 0 changes. **The cache does not care
that this repository has already written the rule down three times.**

---

## 2026-08-08 - The wrapper comes off 415 selectors, and it was protecting nothing

`.app-case` was the last container scope in the system and by far the largest: **415 selectors in 36
of the 50 imported files, 31 per cent of the 1,326 this folder declares.** Its own rule is
`position:relative;background:transparent;border:0`, so it painted nothing; it existed to keep the
product's rules off the course chrome the painted screens carry.

**It does not do that.** Measured in a browser across all 106 painted screens with every dialog
forced open, at 1280 with the pointer asserted fine: of the **375 unique selector tails** behind the
wrapper, **13 match anything at all outside it**, and every one of those 13 is a region of the
PRODUCT.

| what stands outside `.app-case` and an `.app-case` rule reaches | matches | verdict |
|---|---|---|
| the How-it-works sheet, 8 tails | 1,680 | **by design**, and `hiw-dialog.css` says so out loud: a page is not a bigger dialog |
| the deposit sheet's amount chips, 4 tails | 1,050 | defect |
| the footer's language chooser, 1 tail | 105 | defect, backlog 58 |
| **the course chrome: sidebar, toggle, overlay** | **0** | the only thing the wrapper was for |
| the bottom nav | **0** | |

**A scope that changes the outcome for 13 of 375 tails, eight of them in one file on purpose, and
that matches zero elements of the thing it was written to exclude, is not a scope.** It is a hole
with three of the product's own regions in it, and this repository has now paid for that hole eight
times: the amount field, the widget slot, the reassurance box, the chip's amount face, the close
disc, the load-more chip, the sign-in prompt and the provider button.

### The defect it was hiding, and it renders

The selected amount chip in the deposit sheet, against its identical twin in the bet panel, on 105
screens:

| | bet panel, inside | deposit sheet, outside |
|---|---|---|
| ground | `rgba(199,162,78,.09)` brass tint | `rgb(36,40,47)` plain control |
| ink | `rgb(231,214,166)` brass | `rgb(237,231,218)` plain |
| weight | 700 | **400** |
| halo | `0 0 10px -8px` brass | **none** |
| cursor | pointer | **default** |
| edge | `rgba(199,162,78,.45)` | the same |

Only the edge survived. The amount chip had already been fixed once on 2026-08-08, **by writing the
selector twice**: `.app-case .chip-amount, dialog.app-dialog .chip-amount`. The REST state was
doubled and the CHOSEN state was not. **A doubled selector is a face maintained in two places, and
it took under a day for the second place to be forgotten** by the same person on the same component.
That is the argument for removing the wrapper rather than naming the second place, written by the
fix that named the second place.

### What actually changed, measured before and after

The candidate was served from a second origin and swapped into each page in place of
`components/index.css`, so both readings happen in ONE page load against the same DOM. **106 painted
screens plus 55 kit pages, at 390 and 1280, in dark and light: 8 configurations, 380,232 element
readings of 76 computed properties and 4 box numbers each.** Transitions were finished rather than
paused before each reading, after a first pass caught the same chip reporting two different grounds
on two runs because it was measured mid-transition.

**28 distinct changes, identical in all four configurations, and every one is in one of five
families:**

1. **The deposit sheet's chips**, 420 a render: ground, ink, weight, halo and cursor on the chosen
   one, `cursor:pointer` on all of them. The fix.
2. **The footer's language chooser**, 105: padding 4/8 to 8/20, a gap, a transition, and 90x27 to
   122x35. Backlog 58 closed. Its hover and press were then verified by hovering and pressing, in
   both themes: identical to the sort menu in the feed.
3. **The first row of the holders table and the activity list**, 16 and 9. `.hold-row:first-of-type
   {border-top:none}` was written to keep a line off the first row and had never fired, because the
   painted rule tied with it at (0,2,0) and came later. **The wrapper was defeating the file's own
   exception.** Dropping it to (0,1,0) lets the exception win, which is what it is for.
4. **The comment avatars**, 18 of 36. Two placeholder photographs sat in `comments.css` and the
   brass face was `.app-case .cmt-av` at (0,2,0), which BEAT the first at (0,2,0) on order and LOST
   to `.cmt-list .cmt:nth-child(even) .cmt-av` at (0,4,0). So odd rows drew brass initials and even
   rows drew a photograph with the initials printed over it. Nobody chose that. **An avatar is a
   datum and a datum is written on the element**, the rule this repo already applies to the event
   photograph, so the two placeholders are deleted and all 36 wear the face a person with no
   photograph gets.
5. **One "Browse more events" link on `terms.html`**: 16px above and 2px below to 0. It stands in
   `.read-col`, whose pattern writes `.read-col>*{margin-block:0}` because the column supplies the
   rhythm with a gap. The wrapper was out-specifying the pattern.

**Two cascade flips were caught by the before-and-after and fixed in the candidate before it
shipped**, which is the whole reason the measurement exists: the comment avatar above, and
`.app-case .ed-head .sk-thumb`, which tied with `.card.skeleton .sk-thumb` at (0,3,0) and won on
order alone. Unscoped it would have LOST and the detail head's loading thumb would have fallen from
72 to 56. It says `.card.skeleton .ed-head .sk-thumb` now, which is the place it actually stands and
out-specifies rather than ties.

**Nothing else moved.** No change in the course chrome, none in the bottom nav, none on any of the
55 kit pages beyond families 3 and 4 above. The shipped tree was then diffed against the measured
candidate and found byte-identical before the prose was written.

### What is left, and it is the one honest use of the wrapper

`hiw-dialog.css` keeps its 16 `.app-case` rules, because there the wrapper means **the page rather
than the sheet**: the guide has room, so its hero takes an edge of its own, its label is 18px rather
than 11, and its reading column takes the page text size. The file already carried that argument in
prose. Everything else that survives is `.app-case{position:relative}` and `body.app-case{background}`,
which are the class's own two rules and not a scope.

### What was rejected

**Fixing the chip and the footer alone**, which was the smaller of the two options put up. It leaves
410 selectors carrying a qualifier that has produced eight corrections in two days, and the next
control to stand outside the wrapper finds it the ninth time. The reason to do the whole thing is
that the count is knowable and the risk is measurable, and both were measured.

### One instrument note, and it is the third time

**The first verification run of the shipped tree reported the changes in the wrong direction**, which
is only possible if the browser was serving the pre-edit stylesheet. It was: the server had been
started before the edit and the cache answered. Fixed by restarting on a fresh port, the same fix
this repository has now paid for with CSS, with HTML and with this. A verification that cannot be
wrong in a direction you can check is a verification that cannot be checked.

---

## 2026-08-08 - The button family names its sixth face, and it turns out to be 36 per cent of the family

The last container scope in `components/button.css`, and the biggest one anybody had left: the
sign-in sheet's provider rows were written `dialog.app-dialog.signin-dialog .btn`.

**Measured across all 106 painted screens: 322 placements on 105 of them, every one carrying a
provider mark, 0 of them outside that sheet, and 322 of the 902 buttons in the product.** The
sign-in sheet is in the markup of every screen, so **the face nobody had named was the second most
worn one in the family** and its whole existence depended on being inside one dialog.

**What makes it a face rather than a place**: a logotype is not an icon. The mark is filled rather
than stroked, two of the three are monochrome and take the brand ink, and Google carries its own four
colours in the markup and correctly has no rule. None of that is a fact about a dialog. It is
`.btn-provider` now, one form across all 322, `secondary md block provider`.

### And it was the one lifted control in the system with no press

Four things in this product lift under a pointer, and that was measured rather than assumed by
searching every stylesheet for a hover that moves an element:

| | lift | settles on press |
|---|---|---|
| `.card` | -3px | yes |
| `.icon-btn-lift` | -2px | yes |
| `.hero-trust` | -2px | yes |
| **the provider button** | **-1px** | **no** |

`card.css` had already written the reason down: **a HELD control settles instead of hanging in mid
air.** This one lifted and stayed lifted for as long as a finger was on it. The press is the rest
position restated and it cost no new value. Verified by pressing it: rest `none`, hover
`translateY(-1px)`, press back to `0`, against the card's -2.95 and -0.03 in the same test.

### Verified

The kit's specimen and the product's button are the same ground, edge, corner, ink, transition and
mark, compared like with like. **0 selectors anywhere still scope a button to the sign-in dialog**,
and `components/button.css` is at 0 scoped selectors from the eleven it once carried. Across all 55
kit pages at 390 and 1280 with the pointer asserted fine: 0 horizontal scroll, 0 console errors, 149
unique hrefs and 0 broken, one active row per page, 0 collapsed figures.

**Seventh time this correction has been made**, and the four remaining container rules in the system
are all placement or a documented host treatment.

---

## 2026-08-08 - Two more faces come off their containers, and the kit is what rendered them

Asked what other nuances the kit has, so the same question was put to every component file rather
than guessed at: **which rules give a component its FACE only under another component's container.**
Fifty-six rules came back. Most are legitimate, a container saying where a control sits or lending a
documented second treatment. **Two were the input defect again**, and both were found the way input's
was: by comparing what the kit renders against what the product renders.

| | product | the kit, before |
|---|---|---|
| `.widget-box` | control ground, 10px corner, muted ink | **transparent, 0px corner, primary ink** |
| `.protect` | a TRUST tint, 113 of 116 | **a BRASS tint**, which is the other 3 |

**`.widget-box` had its box unscoped and its face under `dialog.app-dialog`.** All 110 stand in a
dialog, so no screen was ever wrong and the stand was the only place it showed. One rule now, on the
class.

**`.protect` had two real faces and no class for either**, kept apart by nothing but the fact that a
`<dialog>` sits outside the `.app-case` wrapper: `dialog.app-dialog .protect` reached 113 and
`.app-case .protect` reached the other 3. Measured, then made explicit: the trust face is the
default and the page face is `.protect-page`, three elements in the painted tree and none in the
grey one, because the grey tree has no page-standing reassurance box at all and two of the three
stand on a screen the grey tree does not carry.

**It is the sixth time this correction has been made**, and the list is now long enough to be a rule
rather than a habit: the signed-out prompt, the fetch control, the toast dismiss, the dialog close
disc, the money field, and these two. **A face is a class, and a container may only say where the
control sits.**

### What was deliberately NOT changed

`.win-dialog .reconcile-box` is the last container scope in the file and it is arguably a different
thing: **a face lent by a container is a defect, and a STATE flowing from a screen to its content is
how an outcome screen is supposed to work.** What decides it is a reading nobody has taken: the
painted tree carries 4 win boxes, 1 loss and 2 plain, and **the grey tree carries 6 with no outcome
variant at all**, so the two trees disagree about whether this box has three faces or one. Backlog
66, with the repo's own precedent noted: `position.css` writes `.pos-side.pos-won` as a modifier.

### Verified

At 390 and 1280 with the pointer asserted fine: **14 of 14 widget slots and 20 of 20 reassurance
boxes render correctly across twelve screens**, the kit's specimen and the product's element are now
the same colour, edge and corner in both faces, and across all 55 kit pages 0 horizontal scroll, 0
console errors, 149 unique hrefs and 0 broken, 0 responses over 400, one active row per page, 0
collapsed figures. Open 51 to 52.

---

## 2026-08-08 - The currency mark leaves the value, and the money field stops accepting letters

The first thing found by READING the finished kit rather than by building it. Two complaints about
`ui-kit/input.html`, and the second one turned out to be about the product.

### What was measured before anything moved

All 121 amount fields in the painted tree carried
`type="text" inputmode="decimal" value="$20.00"`. The mobile keyboard was right and everything else
was not: **a text input accepts letters, so a person on a hardware keyboard could type
`twenty dollars` into the field a bet is placed with.**

**And the guard that looked like one was inert.** 113 of the 121 carried `pattern="[0-9.$]*"`.
A pattern is only consulted at form validation, and **this product contains 0 `<form>` elements**,
measured across all 106 painted screens. It validated nothing at any moment, on any screen. The
other 8 did not carry it, all of them in the bet PANEL, **and the two trees disagreed about which**:
the painted tree had four bet fields with it and the grey tree had none. Absent and inert are the
same amount of nothing, which is why the divergence had gone unnoticed.

### What changed, and why the mark had to move first

`$` inside the value is the reason the field could not be a number: a number input rejects a value
it cannot parse and would have rendered empty. So the order was forced.

| | before | after |
|---|---|---|
| the mark | inside the value | **a sibling, `.amount-cur`** |
| the element | `type="text"` | **`type="number"`**, with `step="0.01" min="0"` |
| the value | `$20.00` | `20.00`, a number a machine can read |
| the guard | a pattern that never fired, on 113 of 121 | **the browser**, on 121 of 121 |
| the two trees | disagreed on 8 fields | **identical markup**, 116 grey and 121 painted |

**System first, then grey, then the painted twin**, which is the order the two trees exist under.
`components/input.css` gained the mark and two spinner-suppression rules, both written against the
CLASS rather than the type so that if the field ever stops being a number they do nothing and say
so. The sweep was a throwaway script in the scratchpad, run twice as a dry run and twice for real,
then deleted.

### Verified by typing into it

On the kit's own specimen, at 1280: **`abc12x3.45qq` leaves `123.45`** and `50.25` leaves `50.25`.
Across a 50-screen sample of the painted tree: **66 of 66 fields are `type="number"`, 66 carry the
mark, 0 have a `$` in the value**, and the grey tree matches on every screen checked. The 44px height
did not move on any of them; the field lost 19px of width to the mark and the gap, 331 to 312 at 390.

**The honest limit is written on the page rather than implied**: `1e5` is still accepted, measured,
and so are a leading `+` and `-`. Markup cannot close a field completely, so the last of the
filtering is the implementation's and `docs/backlog.md` 65 carries the one-line contract it needs.

### And then the plate was taken away, because it was the defect and not the presentation

The other complaint was a rounded plate behind the field on the kit page with no equivalent
elsewhere. The first answer was to explain it: it is a dialog, and every rule the face had was
scoped `dialog.app-dialog .amount-input`, so a specimen standing anywhere else showed the User
Agent's white box. **That answer was wrong, and the second reading of the same screenshot is what
corrected it.**

**A stand that has to reproduce an ORGANISM in order to show an ATOM is the stand reporting a defect
in the system.** The whole sheet face was written against a dialog and the whole bet face against
four ancestors, so this atom had no face of its own, only faces its containers lent it, **and
`ui-kit/vitrine.html` had already written that sentence down as a finding a day earlier without
anybody acting on it.**

| | before | after |
|---|---|---|
| the sheet face | `dialog.app-dialog .amount-input` | **`.amount-input`**, the default, 110 of 122 |
| the bet face | `.app-case :is(.bet-panel,.bet-sheet) .bp-amount-row .amount-input` | **`.amount-input.amount-bet`**, a modifier on the element, 12 |
| the address | `dialog.app-dialog .amount-input.addr` | **`.amount-input.addr`**, 1 |
| what the row keeps | everything | **two declarations** in `betpanel.css`: the width the field takes of the bet row, and the auto margin that pulls the field and its mark to the right edge |
| the specimen | a rebuilt dialog around every field | **the field** |

**It is the same correction this repository has now made five times**, and every one of them says one
sentence: a face is a CLASS and a container may only say WHERE the control sits. The signed-out
prompt became `.btn.btn-prompt`, the fetch control became `.chip.chip-nav`, the toast dismiss and the
dialog close disc both became `.icon-btn`, and now the money field. **Naming the second place a
control stands, which is what this file did and what saved it from the chip's defect, was the smaller
mistake rather than the answer.**

The markup cost was 12 elements: the bet fields take `amount-bet` in all three trees, keyed on the
ROW rather than on the label so the sweep could not pick the wrong field. Everything else changed by
deleting ancestors from selectors. **Measured after, at both widths: 19 of 19 product fields painted
correctly, 19 with the mark, the address still mono, and the kit specimens render with 0 dialogs
inside them.**

`ui-kit/input.html` was rebuilt around **three kinds split by what a person is doing** rather than
two faces plus a footnote: the sheet field a person fills in (110), the bet field a person is about
to commit (12), and the address a person only checks (1, and not an input at all). The atoms shelf's
specimen was brought in line with the product in the same pass, because a shelf that ships different
markup from the screens is the thing this kit exists to prevent. Open 50 to 51.

---

## 2026-08-08 - Six pattern pages, and the kit closes at 55 of 55

**Every component in `components/` has a page.** Four foundations, four shelves, ten atoms, seventeen
molecules, thirteen organisms, six patterns and an overview. The panel reads 55 of 55 and drops its
own sentence about rows with no page, because that sentence only exists while there is one.

### The six pattern headers were right, and that is worth recording

Every `Stands on:` count in the six files was verified in a browser across all 106 painted screens
and **every one of them matched to the number**: action bar 3, browse shell 77, card grid 23, detail
shell 11, list head 71 with 44 carrying controls, position list 13. These are the only headers in
`components/` whose counts have been checked this way, and they held. **The 16 component headers that
say 105 where the tree is 106 are still open as backlog 52**, and this pass is the argument that the
check is worth doing rather than assuming either way.

### What the pattern pages found

**The action bar's declared face is worn by nobody.** Three placements: two wear `.flat` and one
wears `.static`, so **`position:sticky`, the pattern's own default, has never once applied**, and
0 of 3 carry the bar as written. Read together with `account`'s page, which counts the surface from
the other side, the bar's whole declared face is theory. It strengthens backlog 63 rather than
opening a new row.

**The card grid's `!important` was arguing with four dead rules.** Three breakpoints losing to the
fluid track on source order, and a category variant outranked only by the shout. The shipped grid has
always been one rule; deleting the four made the shout removable **without moving a card**. Measured
today: 1 column at 390 and **2 at 1280**, where the file says "one column to four" - three columns
need 932px of grid and the widest column at 1280 is 911, so two thirds of that range is off the end
of the widest reading this kit takes. The page says so.

**Both stale provenance lines in the folder were found by building this shelf.** The browse shell's
`Assembled from` named a PARENT: `<main class="feed">` opens at line 361 and `<div class="cat-layout">`
at 469, so the feed holds the shell. The position list's named a file that had stopped owning the
block five days earlier, when the record moved to `position.css`. **Neither line is read by anything,
which is exactly why both survived a move and a rename.** The kit is the instrument that reads them,
and it is a person writing down what a pattern holds rather than a script.

### Verified

All 55 kit pages at 390 and 1280 with the pointer asserted fine: **0 horizontal page scroll, 0
console errors, 149 unique hrefs and 0 broken, 0 responses over 400**, one active row per page,
**0 planned rows left in the panel**, 0 collapsed specimen figures. All six `Stand:` lines repointed
and every section of `patterns.html` links to its page.

### What the whole rebuild cost and what it found

Five batches in one day, 43 component pages plus the three the atoms had already: **eleven backlog
rows opened by writing them**, 54 to 64. Every page was measured in a browser at 390 and 1280 before
a word of it was written, and the instrument had to be corrected or reset **five times**: once for a
census that counted markup inside a script string, once for a fix comment that reported zeros without
asking whether their host was rendered, and three times for a viewport or pointer override left on
from a previous pass.

---

## 2026-08-08 - Thirteen organism pages, the last unmeasured component, and four zeros that had to be challenged

Every atom, molecule and organism in the system now has a page: **49 of 55**, and the six left are
the patterns. Every number read in a browser at 390 and 1280 with `window.innerWidth` and
`matchMedia('(pointer:coarse)')` asserted before each pass, dialogs and disclosures forced open, and
**every tab radio cycled**, which turned out to matter more than anything else in this batch.

### `profile` was the sixth and last of the unmeasured

The identity row holds one `.btn` and the gallery holds **three `.card`**, so it holds an organism
and it is level 3. The organisms shelf carried it as unmeasured since the rebuild began; that word
is now gone from the repository. Six components came off it in three batches, and in every case the
refusal had been right: **the level formula answers 1 for an atom and 1 for a file nobody has read,
and the two are indistinguishable in the output.**

### Four zeros, and every one of them needed its condition asserted

This batch produced more false readings than any other, and they are all the same mistake in
different clothes.

- **Three of four event-detail panels read 0x0 at both widths**, and all three are correct: the tabs
  are CSS-only, driven by radios, so a static reading sees one panel and reports the rest as missing.
  The whole of `bets-table` is behind two of them. Measured by setting each radio in turn.
- **The profile gallery reads 0x0**, for the same reason and behind its own strip.
- **The bet dock reads 0x0 at 1280 and the bet panel reads 0x0 at 390**, which is one control at two
  widths with each face absent where the other stands.
- **Every chart grid line reads 0 tall, and that one is geometry**: a horizontal `<line>` has a
  bounding box of 300x0 and its stroke is painted OUTSIDE it. Read properly it carries a white stroke
  at 6 per cent. This is the only zero in the kit that is a property of the shape rather than of a
  hidden host.

**And the specimen for the dock was removed rather than shipped empty.** A component that is
`display:none` above 760 cannot have a specimen on a page read at 1280; the page says so and shows
the sheet the dock opens instead.

### What the pages found

- **36 event-detail tab labels stand 36 tall with a finger**, on the strip that is that screen's main
  navigation. The floor names `.tabs button`, `.ptab-lbl` and `.rules-tab`, all three of which
  measure 44; `.ed-tablabel` is a `<label>`, so the tag-based half of the selector misses it.
  Backlog 64.
- **The footer already knew what backlog 58 says, and had fixed it for one control.** Its language
  picker's hover and press are written in `footer.css` with a comment saying the footer stands outside
  `.app-case`. That is 105 of 193 filter menus, and the workaround hid the count.
- **`hero` is 166 lines and 44 class names for ONE placement**, the largest stylesheet-to-placement
  ratio in the system, and it is where the two worst contrast numbers of the whole pass were found: a
  hover colour at **1.71:1 in daylight**, and a hover that painted **14.85:1 over 14.85:1**, which is
  a state that exists in one theme only.
- **`feed` is 11 lines and one class**, the smallest file in the system, and its page is the list of
  where everything else on a browse screen comes from. Three files are now nearly empty, `feed`,
  `loadmore` and `quick`, and each page says why its file is still kept.
- **`hiw-dialog` scoped its whole block to a dialog**, so the page it links to as "the full guide"
  rendered as four bare headings: not one rule could reach it. **Scope describes where a thing may
  stand, not where somebody first put it.**
- **`dialog`: 337 dialogs on 105 screens, three per screen and shut.** That is the whole explanation
  for the `.app-case` scope defect the system keeps meeting: a `<dialog>` is outside the wrapper, and
  a closed dialog is where a defect waits.

### The instrument, a fourth time

The verification pass over all 49 pages returned `pointer:coarse` at both widths, left over from this
batch's own touch reading. The pass was re-run from a fresh browser at `pointer:fine`. **Four times
in one day, and the guard is now written into every script rather than remembered**: assert the
width and the pointer, print them, and treat two columns that agree where they should not as the tell.

### Verified

All 49 kit pages at 390 and 1280, fine pointer asserted: **0 horizontal page scroll, 0 console
errors, 130 unique hrefs and 0 broken, 0 responses over 400**, one active row per page, 0 collapsed
specimen figures. All thirteen `Stand:` lines repointed, every section of `organisms.html` links to
its page, and `ui-kit/docs/inventory.md` carries a reading for the last of the six.

Backlog 49 to 50.

---

## 2026-08-08 - The word "unmeasured" comes off three components, and it came off by walking

`ui-kit/docs/inventory.md` filed six components as **outside the core, unmeasured**: they stand on
none of the five anchor screens the kit was rebuilt from, so nobody had read them on a rendered page.
Three of the six are molecules, `account`, `cookie-consent` and `toc`, and the molecules shelf
carried a section called "Three that are not here, and why that is a statement" rather than a
specimen for each.

**That refusal was right and this entry is not overturning it.** The level formula answers 1 for a
component built out of its own class names, and it answers 1 for a component nobody has read at all,
**and the two are indistinguishable in the output**. A level printed without a reading is a guess
wearing a declaration's clothes.

### The walk

Six screens, containment read from the DOM rather than from the class names, at 390 and at 1280 and
in both pointer branches.

| | placements | holds | level |
|---|---|---|---|
| `account` | 3 bars on 3 screens | **`button`, 6 of them** | 2 |
| `cookie-consent` | 1 banner on 1 screen | **`button`, 3 of them, plus its own rows** | 2 |
| `toc` | 1 rail, 14 rows, on 1 screen | **its own rows, and they are anchors** | 2 |

All three hold something. The shelf gained three sections, each with a live specimen in both themes,
and each of the three now has a page. **The molecules shelf reads 17 measured and 0 unmeasured**, and
`_nav.js` moves NEXT to `header`, the first organism.

### What the walk found

**`account`'s own face is worn once of three.** `.cta-bar` is a stone, a hairline along its top edge
and two rounded corners; `.cta-bar.flat` is three declarations that take all of it away. Measured:
293x72 against 293x55 at 390. **The plate stands once, on the wallet, and the flat row stands twice.**
Either the plate is the face and two screens are wrong, or the flat row is the face and the plate is
the variant, and nothing in the repository says which. Backlog 63.

**`cookie-consent` is the strongest case in the kit for a component page.** It stands once, so there
is no second placement to compare it against and no state a screen shows you: everything that matters
about it is in the stylesheet or in a law. Which control may go dead (none, and a Reject that could
would be the dark pattern the banner exists to answer), what Necessary means (**LOCKED ON, which is
not unavailable**, so it is kept out of both pointer rules), why the row is the target and not the
18x18 box, and **why a native checkbox cannot take the system's pressed ground at all**: the browser
draws it and `background-color` never reaches it, so the press is written in `accent-color`, the one
property that can.

**`toc` is a rail on a desktop and a disclosure on a phone, and both halves were measured rather than
assumed.** It was built OPEN first to check whether the IA was being cautious: at 360 the fourteen
rows pushed the document's H1 entirely below the fold. And its sticky top is 66px where the other two
rails use 120px, because 120 is the header plus a condensed category strip that a document page never
shows, measured at 0px tall at scroll 1200. The rail was clearing 61px of chrome that does not exist
and starting 24px below the heading beside it.

### The instrument had to be reset again, and this is the third time

The first measurement pass of this batch returned **identical numbers at 390 and at 1280**, which is
the signature this session has now produced three times: a CDP `setDeviceMetricsOverride` and touch
emulation left on from the previous batch, which `setViewportSize` cannot override and which cannot
be turned off through CDP. The pass was thrown away and re-run from a fresh browser. **The tell is
not an error message, it is two columns of a table agreeing where they should not**, and the only
reliable guard is asserting `window.innerWidth` and `matchMedia('(pointer:coarse)')` before reading
anything.

### Verified

All 36 kit pages at 390 and 1280: **0 horizontal page scroll, 0 console errors, 89 unique hrefs and
0 broken**, one active row per page, 0 collapsed specimen figures, and the three new shelf anchors
resolve. `ui-kit/docs/inventory.md` gained a reading for all three, and for `toggle`, which had been
carrying the same word.

Backlog 48 to 49.

---

## 2026-08-08 - Fourteen molecule pages, and six of the fourteen found something the shelf could not show

The second batch under the rule set the same day: a level is a shelf and a component is a page. All
fourteen molecules that stand on the molecules shelf now have one, so the kit is **33 of 55 stand
pages**. Every number in them was read in a browser at 390 and at 1280, dialogs and disclosures
forced open, and re-read with touch emulation on wherever a pointer branch was in question.

### Three findings of one shape, and it is the shape this repository keeps meeting

A rule that reaches some of a component's placements and not the others.

- **`.feed-trustbar` is in the markup of 105 screens and drawn on none of them.** The last line of
  its file is `display:none` under `.app-case`, and every painted screen carries `app-case`. Eleven
  rules and 210 items are maintained for a face the painted tree has never shown. It is not dead
  code, because the grey tree still draws it, and it is not a decision either, because nothing says
  why the footer won. Backlog 57.
- **105 of 193 filter menus stand outside `.app-case`**, all of them the footer's language chooser,
  because the footer is outside the app-case wrapper. They get a surface, a hairline and a pill
  corner from the unscoped rules and **no padding of their own, no transition, no hover and no
  press**: 90x27 against 152x35. The touch floor is unaffected, because `base.css` names
  `.filter-menu summary` without a scope, so both kinds reach 44 with a finger. Backlog 58.
- **`.opt-sel-tag` is switched off the same way and is CORRECT**, which is what makes the first two
  findings legible. The word "selected" is the grey tree's way of saying a row is chosen; the paint
  says it with a tint, a brass edge and a chosen YES. **The test is whether the hidden thing has a
  replacement on the same screen.** What it still costs is a screen reader hearing nothing, because
  the row carries a class and no state attribute. Backlog 61.

### And three more

- **`comments.css` explains at length why its actions are not 44 tall, and they are 44.** They carry
  `btn btn-bare`, and the one touch floor written the same morning names `.btn`. Neither half is
  wrong: a family floor stops six files each remembering a different part of the product, and a
  written per-control argument stops a floor breaking a layout nobody re-read. **What cannot stand is
  a file stating a decision the product has stopped making.** Backlog 59.
- **Four related rows of 31 have no thumbnail**, and the rule draws a fixed 46 square, so those rows
  lose their left column entirely rather than showing an empty one. Backlog 60.
- **36 elements carry `.feed-seo`: 22 sections and 14 divs.** The drawing does not care and the
  document outline does. Backlog 62.

### What the fourteen are

`trustbar`, `market`, `comments`, `notice`, `filters`, `bottomnav`, `catnav`, `related`,
`state-block`, `position`, `quick`, `options`, `seo-plate`, `loadmore`. Their `Stand:` lines were
repointed and every section of `molecules.html` now links to its page, the same way the atoms shelf
does.

**Two of them are honest about being nearly empty, and that is the point of writing them.**
`loadmore` is two rules and its page is mostly the four declarations that once separated it from the
category chip, with what each turned out to be worth: three inert and one an unargued exception.
`quick` is four declarations, and its page says out loud that a file holding one layout rule is a
candidate for folding, kept for now because the row really does two different things in two places.

### Verified

All 33 kit pages at 390 and 1280: **0 horizontal page scroll, 0 console errors, 80 unique hrefs and
0 broken**, one active row per page and the correct one. Every specimen re-read for a real box and a
real colour across the fourteen new pages, 0 missing and 0 collapsed.

Backlog 42 to 48.

---

## 2026-08-08 - A level is a shelf and a component is a page, and the atom shelf now has ten pages behind it

**The rule this kit was rebuilt under said the opposite**, in `CLAUDE.md` and in `ui-kit/_nav.js`:
*a page per LEVEL, not per component, because forty pages of one component each are forty
navigations to compare two chips*. Three components had been let past it on 2026-08-08 under a
counted threshold: the product's three largest control families, 902, 1,361 and 1,679 placements,
and the comment in `_nav.js` said out loud that **a component with one face does not get a page
here, however often it is worn**.

**The reason was right and it was a reason for the SHELF, not against the pages.** Comparing ten
atoms is what a level page is for and it keeps that job. Taking ONE apart needs room a shelf does not
have, because a shelf gives every component one specimen and one rule. The two answer different
questions, and the old rule read one of them as an argument against the other.

**The counted threshold is dead, and two components killed it.**

- **`toast`: four placements on one screen**, the smallest inventory in the product. Its page carries
  where the boundary with its own dismiss runs (one declaration stayed, `flex:0 0 auto`, a fact about
  a two-item flex row), why the error face is not red, and the fact that most of the component is a
  behaviour no static page can draw. None of that is a function of how often it is worn.
- **`toggle`: three placements, and FOUR of its five faces have no placement anywhere.** Every
  `.toggle` in `ui-visual/` is `aria-checked="false"` and none is disabled, so the ON face, the ON
  hover, the ON press and the disabled face exist only in the stylesheet. **A stand built by walking
  screens would show one grey oval and call it the component.**

### What was written

Seven pages, one per remaining atom, so the atom shelf is now ten components with ten pages:
`navitem`, `oddsbar`, `input`, `yesno`, `toast`, `skeleton`, `toggle`. Every number in them was read
in a browser at 390 and at 1280 on 2026-08-08, dialogs forced open, and re-read with touch emulation
on where a pointer branch was in question.

`ui-kit/_nav.js` was restructured to match: the `Components` group and the `In depth` group are gone,
and there is a group per LEVEL whose first row is the level page itself, named `All atoms` and so on.
**Every component in the system now has a row**, done or not, because a row with no page renders as a
`<span>` with a badge and that is the whole reason the panel lists things that do not exist yet.
**19 of 55 stand pages written**, from 12 of 12, which is the first honest denominator the panel has
carried. The three existing component pages had their opening section rewritten, because each one
argued for itself against a rule that no longer holds.

### The instrument was wrong once, and this is the entry that records it

**`oddsbar` cannot be counted in the source, and a file-reading census said 0.** The feed builds its
cards at run time, so the markup lives in a string in a page script and the bar's class is assigned
with `bar.className = 'oddsbar'`, never as an attribute. A census that scans HTML files reported
**0 placements of a component the product wears 63 times**, and **114 tracks on 105 screens** where
the DOM holds 72 on 21, because one line of JavaScript is counted once per file whether the screen
draws nine bars or none.

**The FACT was already known and the SIZE of it was not.** Building `vitrine.html` on 2026-08-07
turned up that this component exists in no screen's markup, and `ui-kit/CLAUDE.md` records it as one
of two things a rendered page caught that the census and the inventory had both missed. What was
never taken is what the wrong numbers actually were, so the component's own page now carries them
side by side: 0 against 63, 114 against 72, 105 screens against 21.

The same instrument was right about `button`, `iconbtn` and `chip`: all three counts were re-taken in
a browser on this pass and came back identical to the character, 902, 1,361 and 1,679. **An
instrument that agrees three times is not a verified instrument, it is an instrument that has not yet
met the case it cannot see.** The three existing pages keep their numbers because the numbers held.

**A second instrument correction, in the opposite direction.** `skeleton.css` records that 52 of 482
marks once drew at zero size. Re-measured today: **0 of 482 at 1280, and 6 of 482 at 390** - and the
six are correct. They stand inside `.bet-panel`, whose computed display is `none` below 760, because
the panel is the desktop face of the bet control and the sheet is the phone one. The mirror case
proves it: **16 of the trader's dock buttons read 0x0 at 1280** and nothing is wrong with them
either. So the criterion is not *is the box zero*, it is **is the box zero while its host is on the
screen**, which is the same shape as the touch-floor reading of the same day: a criterion the system
answers CONDITIONALLY had its condition left unasserted.

### What the pages found

Three rows opened, 54, 55 and 56, and all three are things a level page could not have shown.
**365 account-menu rows stand 194x33 with a finger on them**, at both widths, and `.nav-item` is not
one of the fourteen families in the one touch floor. **The switch is 40x24**, which clears 2.5.8 with
nothing to spare and fails 44, and nobody has ever argued 44 either way for it. **88 of 90 skeleton
hosts declare themselves decoration**, and the two that do not are on the two detail loading screens.

One finding needed no row and is worth keeping: **the `nav-row-stack` specimen is the only one on any
of these pages that stands inside its container, and it had to.** Lifted out of `.notif-drop` the
same markup renders 33 tall instead of 49, because the title and the detail take their
`display:block` from the dropdown's file. The boundary those pages describe is therefore visible in
the specimen rather than only stated in it.

### Verified

All 19 kit pages at 390 and 1280: **0 horizontal page scroll, 0 console errors, 0 broken links**, one
active row per page and the correct one, every wide table scrolling inside its own container. Every
specimen re-read for a real box and a real colour, because a specimen that renders as nothing is the
failure mode this whole stand exists to avoid. The seven `Stand:` header lines in `components/` were
repointed at the new pages, so all ten atoms name their own page and the shelf anchor beside it.

---

## 2026-08-08 - The cookie row becomes the target, and the stand's stylesheet loses nine dead rules

Two rows closed, 51 and 53, and the second one broke the file on the first attempt.

### 51: the last target under the AA floor

Three checkboxes on `cookie-consent.html` rendered **18x18**, and they were the only targets in the
product that a finger has to HIT rather than read and that fell under WCAG 2.5.8's 24x24. Everything
else under 24 is a text link, which the criterion exempts.

**The fix is markup and the structure was decided in grey first**, which is the rule the two trees
exist under. `<div class="cc-cat-main">` is `<label class="cc-cat-main">` in
`wireframes/cookie-consent.html` and in `ui-visual/cookie-consent.html`, identically, so the name, the
box and the space between them are one target.

| | before | after |
|---|---|---|
| the target, fine pointer at 390 | 18x18 | **233x36** |
| the target, coarse pointer at 390 | 18x18 | **233x44** |
| at 1280, coarse | 18x18 | **851x44** |

The checkbox is still 18x18 and that is correct: **it is a part inside the target now rather than the
target**.

**The accessible NAME did not move, and that was deliberate.** A wrapping `<label>` would normally
name the input from its own text, but `aria-label` wins over it and the existing one says "Analytics
cookies, off by default" where the visible word says only "Analytics". The name is `voice/`'s
property and this pass changed a target, not a string. So the attribute stays and the label does the
one job it was added for.

`.cc-cat-main` joined the one touch floor in `base.css`, which is where its 44 comes from, and
`cookie-consent.css` gives it `--control-36` and a pointer because **it is a control now**. It is the
only member of that list that was not a control when the rule was written.

**Re-measured over ten screens under a coarse pointer: 8 targets remain under 24x24 and every one is
a text link.** 0 controls that a finger has to hit are under the AA floor.

### 53: the count was of classes, the file has rules, and the first delete broke it

Six dead CLASSES turned out to be **nine dead rules**, because three of them are compound and carry a
live class beside the dead one: `.tk-mc.tk-fail`, `.tk-mc.tk-fail i`, `.tk-bar.tk-bar-off>u`.

**The first removal was line-based and it broke the stylesheet.** `.tk-rul` is written over three
lines; deleting the line that opens it left the continuation and the closing brace behind. **361 open
braces against 362 close**, which the check ran straight after the edit caught, and the file was
restored from git and done again brace-aware.

That is the third time in two days that a first count or a first edit was wrong in the same way, and
the pattern is now specific enough to name: **a CSS file is a list of rules and a markdown file is a
list of lines, and a tool that reads either one as text will be right often enough to be trusted and
wrong exactly where it matters.** The defence is not care, it is a second reading that cannot fail
the same way. Here it was a brace count; on the anti-rules it was reading the page instead of the
class; on `.tk-onlight` it was stripping comments before matching.

`_page.css` is **680 lines from 686, 77 classes defined and 0 dead, 0 worn and undefined**, and all
twelve kit pages render at 390 and 1280 with 0 horizontal scroll, 0 overflow and the right active
row.

Third and last of the in-depth pages. `ui-kit/chip.html`, eleven sections.

### The measurement

**1,679 placements on 106 screens**, the largest family of any kind in the product. **869 are
`<button>` and 810 are `<a>`**, and **0 of the 1,679 wear a bare `.chip`**. That last number is the
one worth having: the file's oldest rule is *a base class is the atom or it is a face, never both*,
written the day one face was put on `.chip` itself and 722 elements took values nobody had chosen.
Until now that rule was a principle. It is a check now, and it passes.

| face | worn | screens | where |
|---|---|---|---|
| `.chip-quiet` | 530 | 105 | the header strip, 525 of them |
| `.chip-amount` | 480 | 105 | a dialog, 448 of them |
| `.chip-lane` | 312 | 32 | the sub-category rail |
| `.chip-nav` | 294 | 57 | the category strip, and 9 are Load more |
| `.chip-rail` | 63 | 9 | 36 the chart range, 27 the comment sorter |

### The finding: four of five faces move, and until yesterday one did

| face | fine | coarse |
|---|---|---|
| quiet | 38 | **44** |
| amount | 36 | **44** |
| lane | 41 | **44** |
| nav | 47 | 47, already above |
| rail | 26 | **44** |

`chip.css` carried its own floor and it named `.chip-quiet` and `.chip-nav`, **one of which did not
need it**. So under a finger the amount rendered 36, the lane 41 on 312 placements over 32 screens,
and the rail 26. The consolidation of the touch floor into `base.css` earlier the same day is what
moved them, and this page is where that change stops being a diff and becomes a picture.

**Set against `iconbtn.html`, where one face of eight moves and four are excluded by name, the two
pages together say what the floor is**: a family-wide rule with a short list of argued exceptions,
rather than six per-file lists that each remembered a different part of the product. Neither page
could say that alone.

### The lane, measured at both widths because a specimen has one

| | at 390 | at 1280 |
|---|---|---|
| width | content: 81, 114, 131, 106 | **206, all ten** |
| corner | 100px, a pill | 10px |
| the count | 37px in, after the label | **166px in, at the far side** |
| the rail | a horizontal scroller | a column beside the content |

**A specimen has one width, so the wide face is four numbers rather than a picture**, and printing
them is the honest alternative to showing half a control and calling it the control. Reading only one
of the two is what put this chip in `navitem` for a day.

### Why this component needed a page more than the other two

A chip's subject is **its group and the chosen one in it**. Lift one out of its rail and what is left
is a padding, which is why the deleted stand showing two lone chips on the button page was worse than
not listing them. Every specimen here stands with its siblings and one of them chosen, and the
anti-rule now says so out loud: **never show one alone.**

### The registry closes its own sentence

The panel reads **12 of 12 stand pages written**, and `_nav.js` drops its second sentence, "A row
with no page is a row that says so", because there is no such row. That was written into the render
on 2026-08-07 as a rule about not looking finished; it is the first time it has had to take itself
out, and it did.

Second of the three in-depth pages. `ui-kit/iconbtn.html`, eight sections, every face a live pair in
both themes, and **the page paid for itself twice**.

### What it measured

**1,361 placements on 106 painted screens**, over eight faces. The split matters more than the
total: **763 are `<button>` and 598 are `<a>`**, against this component's neighbour on the
in-depth list, `button`, where all 902 are buttons and none is a link. That is the difference
between a control family and a mark that is often a destination.

| face | worn | where |
|---|---|---|
| `.icon-btn-lift` | 525 | the footer's social row, five per screen |
| plain `.icon-btn` | 242 | the header, and only the header |
| `.icon-btn-photo` | 228 | a sheet close |
| `+ .icon-btn-ring-strong` | 105 | the How-it-works sheet's close |
| `.icon-btn-bare` | 84 | a card's caption row |
| `.bal-swap` / `.bal-add` | 73 / 73 | the header's balance cluster |
| `.icon-btn-tile` | 27 | the event head's toolbar |
| `.icon-btn-small` | 4 | a toast |

### The first finding: one face of eight answers the pointer

Read at 390 in both branches with every dialog forced open. **Only the plain circle moves, 36 to
44.** `.icon-btn-bare` is 44 in both because it sets the floor itself; the other six do not move at
all, four of them because the touch floor in `base.css` excludes them by name.

**Every face clears WCAG 2.5.8's 24x24 and four of the eight do not clear this project's 44.** That
is backlog 39 and it is open on purpose, but the shape of it was not legible before: it reads as an
oversight when the faces are apart and as a decision when they are together, because the four are
exactly the four whose ground would be resized by it.

### The second finding: a face named for a ground it does not stand on

**All 333 `.icon-btn-photo` are `.sheet-close` inside a `<dialog>`, and what is behind them is
`.sheet-head`, which paints a brass radial gradient.** Not one of them stands on a photograph.

The name is deliberate and `components/iconbtn.css` says why: what defines the face is the three
on-photo roles it reads, `--scrim-photo`, `--line-on-photo` and `--text-on-photo`, and a dialog head
is the same problem, a ground the control cannot predict. **The page states both halves rather than
leaving it as a smell**, because the next person to meet the class will read the name before the
comment. The specimen therefore stands on the event photograph and not on the plate: a face defined
by an unpredictable ground cannot be shown on a predictable one.

### The sentence the eight faces turned out to be for

**A face here is an answer to the GROUND, not a variation on a circle.** Six grounds, eight faces,
and the two extra are modifiers that change one value each. That sentence was already in the
stylesheet from the migration of 2026-08-06; what the page adds is that it can be checked, because
the eight stand side by side and the reader can see that the tile has a ground and the bare mark has
none for reasons that are about what is underneath them.

### Two corrections in the registry, made because the page forced a recount

`_nav.js` said "The kit has seven pages and will have nine" and its tally comment used a worked
example of 10 of 12. Both were true when written and neither is now. They say eleven and twelve, and
**the first one now records that it has been corrected twice**, which is the argument for writing a
count down at all standing up on its own.

`chip.html` is the last of the three and is not started.

The question that produced the entry below produced this one too: where did the per-component pages
go. The pointers were the defect; **this is the part of the question that was a real gap.**

### The rule stands and it was too coarse at one end

A page per LEVEL and not per component is right, and the reason has not changed: forty pages of one
component each are forty navigations to compare two chips. **What it leaves out is a family whose
faces cannot be shown by one specimen.** `vitrine.html` gives each atom one box and one rule, and for
eight of the ten atoms that is the whole story.

The threshold is counted rather than felt. Measured on the 106 painted screens: `button` **902**
placements, `iconbtn` **527**, `chip` **466**, and the fourth largest a long way behind. Each of the
three paints more faces than a level page can stand side by side. **A component with one face gets no
page here however often it is worn**, which is the half of the rule that keeps this from becoming the
deleted vitrine again.

### What the page holds that the level page cannot

`ui-kit/button.html`, twelve sections. Five emphases as live pairs in both themes with their counts;
the four sizes with what they RENDER at both pointers; the width axis; the states, including the
three a static page cannot show and says so; the 22-form census; the combinations the product does
not have, each with a verdict; the one surviving scope; the rule and the anti-rule.

**Every number was re-measured and several had moved.** The archive says 710 placements and 505
secondary; today it is **902 and 509**. That is the point of re-measuring rather than copying: the
archive is good writing about a system two consolidations ago.

What the measurement found, beyond the totals:

- **All 902 are `<button>`. Zero are `<a>`**, which is what makes the anti-rule about tags checkable.
- **`.btn-xs` is 105 placements and 0 of them render at 390.** The control is the header's and the
  header hides it below 640. A size that exists on a desk and nowhere else is still a size, and a
  placement count that does not say so reads as coverage.
- **One form is 35 per cent of the component**: the provider row in the sign-in sheet, 315 of 902 on
  105 of 106 screens, and it is why the one surviving scope exists.
- **526 of the 559 buttons inside a `<dialog>` are in a dialog that does not carry `app-case`.** That
  is the measurement behind this file writing no `.app-case`, and it is the same fact that made the
  amount chip's fix on 2026-08-08 name `dialog.app-dialog` instead.
- The X brand mark is worn 108 times against 107 for Google and Apple, and the odd one has a reason:
  `sign-in-provider-conflict.html` carries a second X row. **A count that came out uneven and had a
  reason is the only kind worth printing.**

### The registry gained a group and two rows with no page

`_nav.js` now carries `In depth` with Button written, Icon button marked next and Chip marked soon.
Both empty rows render as a `<span>` with a badge, which is the registry's own rule: a route that
lists only what is finished looks finished. The tally reads 10 of 12.

### Two things filed rather than done

**Backlog 53**, six rules in `ui-kit/_page.css` painting classes nothing wears. The number is worth a
sentence of its own: the first count said seven and included `.tk-onlight`, which has **no rule at
all** and was matched inside a comment. A deletion made on that reading would have removed a line of
prose. Counted again with comments stripped, it is six. **The same loose reading that produced the
anti-rule mistake this morning produced a second one before lunch**, which is the argument for taking
the count twice rather than for being more careful.

`iconbtn.html` and `chip.html` are next and are not started.

Asked where the per-component pages went, the answer turned out to be measurable rather than a matter
of taste, and the measurement is the entry.

**Every file in `components/` opens with a `Stand:` line. All 42 that carry one named a file that does
not exist**, and they had done since 2026-08-07. They pointed at `ui-kit/button.html`,
`ui-kit/chip.html`, `ui-kit/header.html` and 39 more: the **generated per-component pages**,
one per component, which went with the 65 pages, 18 scripts, 41 gates and 145 MB deleted that day.
Nothing noticed for a day, and nothing was going to, because **a comment has no reader**. It is the
third time in three days the same species has surfaced here: a pattern file's `Assembled from` line,
a status table nothing cross-checks, and now a path.

### Where they point now

37 of the 42 have a specimen on a level page and the section ids already matched the file names one
for one, so `components/button.css` says `ui-kit/vitrine.html#button`. **The five that do not are not
given one**, because inventing a destination is what put the wrong one there in the first place:
`base` and `course-chrome` are the frame every kit page stands in rather than a specimen on one, and
`account`, `cookie-consent` and `toc` point at `ui-kit/molecules.html#unmeasured`, which is where the
kit says out loud that nobody has read them rendered.

**Verified by opening all 44 anchors in a browser**, not by grepping for the id: each one resolves,
is visible and lands its section. The one that failed the first check, `#unmeasured`, failed the
CHECK and not the anchor: it is the last section on its page, so the browser cannot scroll it to the
top, and it sits fully in the viewport at 492 to 680 of 900. **An instrument that assumes a target
can always reach the top of the window is an instrument that has never met the bottom of a page.**

### What is not fixed, and it is filed rather than left quiet

The other half of the same header block, `Stands on: N ui-visual screens`, is stale on **16 files
that say 105 against a tree of 106**. It was left because **it cannot be fixed by substitution**: a
real count means asking which screens carry each component's classes, rendered, and
`ui-kit/patterns.html` already showed what a typed count costs. **Backlog 52**, and it goes to the
handoff pass that has to read every header anyway.

### The decision behind the question, restated because it was asked twice

The kit has a page per LEVEL and not per component, and `ui-kit/CLAUDE.md` carries the reason.
**What cost this repository seven days was the GENERATOR, not the idea of a page per component**: a
one-line change to a stylesheet paid for a regeneration, a re-capture, 41 gates and 525 snapshots. A
page written by hand pays none of that. `docs/kit-archive/authored/` holds **48 per-component
documents** with anatomy, rule, anti-rule and states, read by nothing, which is the material for
per-component pages if and when the components that earn one get them: `button` at 687 placements,
`iconbtn` at 527, `chip` at 466. That is a decision still open and it is not this entry's.

---

## 2026-08-08 - Design System closed as a stage, and the status table stops disagreeing with the tree

The work of stage 09 was finished on 2026-08-08 and the one place that records a stage's status still
said **Not started**. Closing the stage is therefore mostly a documentation act, and the reason it is
its own entry is that **the table was wrong in a way nothing could catch**: `README.md`'s status table
is the single source for stage status by rule, so nothing cross-checks it, and a source of truth with
no reader is the same species of defect `patterns.html` found in the pattern files' `Assembled from`
lines two days earlier.

### What was measured before anything was written

| | |
|---|---|
| `components/*.css` | **45** files: 3 infrastructure (`index`, `tokens`, `fonts`), 2 substrate (`base`, `course-chrome`), **40 components** |
| `components/patterns/` | **6** |
| placed on a kit level page | **43** = 37 components + 6 patterns |
| not placed, and named as unmeasured on the molecules page | **3**: `account`, `cookie-consent`, `toc` |
| painted screens | **106** |
| open backlog items whose OWNER is Design System | **2**: 28, blocked on IA's 27, and 51 |

### The level split in the status table was the arithmetic, not the declaration

The row read **6 atoms, 13 molecules, 21 organisms, computed from the markup**. That is the reading
`ui-kit/docs/inventory.md` replaced with a DECLARED level and a reason each: **10 atoms, 14
molecules, 13 organisms, 6 patterns**. The old numbers are not a typo, they are the blind spot
`components/CLAUDE.md` names out loud: a component built from its own class names reads as containing
nothing, so `trustbar` and `market` computed as atoms. **The status table was still publishing the
answer the kit was built to correct**, and the correction had been written down for a day.

### The counts markers came out with it

The row carried `<!-- counts:start -->` and `<!-- counts:end -->`. **Nothing writes between them.**
The script that did went with the 63 deleted on 2026-08-07, and grepping every `.py`, `.js` and `.sh`
in the repository for the marker returns nothing. A marker for a machine that no longer exists is an
instruction to a reader to keep their hands off a number that no longer updates.

### What else disagreed, found by sweeping for the phrase rather than by remembering

`README.md` said the vitrine was being rebuilt and `ui-visual/` held 105 screens; `STRUCTURE.md` said
the same two things; the root `CLAUDE.md` said it twice, in the folder table and in the shape of the
work. All five now say what is there. `ui-kit/CLAUDE.md` said it in its own title. **The one place
`105` was left standing is `ui-kit/CLAUDE.md`'s account of the pattern headers**, because that
sentence is about what was true when those headers were typed and correcting it would make it false.

### The mistake worth recording, because it is this repository's own rule

Before this pass I told the user that **41 of the 43 components on the level pages carry a rule and
no anti-rule**, and offered to write the missing ones. That was wrong. I had counted the CSS class
`.tk-bad` in the markup, found 2, and reported a gap. **Every one of the 43 carries both**, written
as prose and labelled `<b>Anti-rule.</b>`, which a class-name count cannot see.

It is the same error the audit made with `pointer:fine` and the same one this repository has written
down twice about pages: **reading the source is not reading the page.** Counting a class is reading
the source. The count that mattered was of a sentence, and it took one measurement of the right thing
to find that the work was already done. It is recorded because the offer had been accepted and the
next pass would otherwise have gone looking for 41 things that are not missing.

`docs/kit-archive/authored/` turns out to hold an `## Anti-rule` section for all 48 components as
well, which is what `components/CLAUDE.md` means by keeping the archive: the same measurement is not
taken twice.

---

## 2026-08-08 - The audit's eighth defect: it measured the product with a mouse, and the floor was six lists

Direction B was approved and this pass went to execute it. **It did not survive the first
measurement, and what replaced it is better and smaller.** The record of the direction is the entry
below this one; this is what happened when it was read against the page.

### The premise was false, and the six files that said so had been saying it for a day

B was chosen on the strength of one sentence in the audit: *a control that read a height token would
be one edit away from 44; a control that computes its height from three other values is 317 edits
away.* Before touching 106 screens on the strength of that, the floor was looked for. It was already
there. **`components/button.css`, `header.css`, `iconbtn.css`, `tabs.css`, `filters.css` and
`chip.css` each carried an `@media(pointer:coarse)` block raising their controls to
`var(--control-44)`**, and `button.css`'s carried the rule in capitals: TARGET SIZE FOLLOWS THE
POINTER AND NOT THE VIEWPORT.

**Headless Chromium reports `pointer:fine` and `maxTouchPoints:0`.** The audit asserted no pointer,
so all 460 of its renders measured the 36px branch, and its one product finding was the fine-pointer
product measured against a floor only a finger raises. Re-read with
`Emulation.setTouchEmulationEnabled` on and `matchMedia('(pointer:coarse)')` asserted true before
every read, 106 screens at 390: **1,790 targets, 1,361 already clearing 44x44, 262 short.** Against
1,787.

**This is a worse instrument defect than the load race that produced 434 phantom contrast failures,
and it is worth saying why.** The race read the page at the wrong TIME, and time passes: another run
would have caught it. This read the page on the wrong DEVICE, and no number of re-runs turns a mouse
into a finger. It was found by going to fix the finding and reading the comments that had been
explaining the floor to nobody. **An instrument nobody disbelieves twice has stopped being
disbelieved**, which is the one thing this repository was supposed to have learned already.

The general form, and it is narrower than "test on a device": **a criterion the system answers
CONDITIONALLY has to have its condition asserted.** A media query is a condition. An unasserted
condition is a value the instrument chose without saying so, and a missing value is a value. That
rule was written here about pages. It applies to instruments.

### What was actually wrong: a floor written six times, and every copy a list

Not one file was wrong. Every one of the six named a LIST of its own controls, and **what a list
leaves out, nothing says**. `chip.css` named `.chip-quiet` and `.chip-nav` out of five chips, so
`.chip-lane` rendered 40.5 on 104 placements over 32 screens under a finger and `.chip-rail` 26 on
63. `tabs.css` named two tab faces of three and left `.rules-tab` at 31, in its own file.
`.market-head` is a `<summary>` a person taps to open a market and rendered 18. `.toc-link` rendered
36. **None of the three had a floor anywhere in the system**, and nothing had ever asked.

`button.css` had already written the argument and then applied it only to itself: *a floor is the
family's, not a size's: a seventh step added later gets it without anybody remembering.* The
correction is that sentence applied to every family instead of one.

**One rule, in `components/base.css`, beside the focus ring**, which is the same species of rule and
whose own comment says why: a person navigating by keyboard is not asking each component separately.
Neither is a thumb. The six blocks are gone and each file keeps a comment saying where the
declaration went and what its own list had left out.

**The selector names classes and not tags, deliberately.** `a` and `button` would catch the card
question, the hero title, the bet panel's change link and the cookie prose link. Those are text: a
title that wraps to two lines does not become a target by growing an empty box under it, and
`card.css` had already written why `.card a.q` stays bare. **A family is something the system
declared; a tag is what the markup happened to be.**

**The four exclusions travelled unchanged, with their reason**, and they are the icon button's:
photo dismiss, tile, toast dismiss, social mark. Whether they should be 44 is backlog 39 and it is
still open. They now sit in the one place instead of in the middle of one component's file.

### The tie, which is the part that would have shipped broken

Written as `:not(a,b,c,d)`, the rule is (0,2,1). **`.app-case .tabs button` in `tabs.css` is also
(0,2,1)**, `base.css` is imported first, and source order gave the tab its 36px back: measured, 18
tab buttons over the nine active-bets screens still reading `min-height:36px` with the floor in place
and the pointer coarse. Four chained `:not()`s count four times, the rule is (0,5,1), and it
out-specifies every nominal height in the system rather than tying with one. **A floor a component
can tie with is not a floor.** `iconbtn.css` had written the chain long and literal for a different
reason and it turned out to be load-bearing.

### Measured after

| | before | after |
|---|---|---|
| short of 44 at 390, coarse | 262 | **68** |
| short of 44 at 1280, coarse | 542 | **98** |
| clearing 44x44 at 390, coarse | 1,361 | **1,474 then 1,510** |
| under 44 at 390, FINE | 1,028 | **1,028** |
| pages gaining horizontal scroll | | **0 of 106** |

**Every one of the 68 is text or a named exclusion**: 27 tiles and 4 toast dismisses are two of the
four exclusions, 21 are the card question, 13 are prose, related and hero links, and 3 are native
checkboxes. The fine branch was measured on purpose, to prove a floor inside
`@media(pointer:coarse)` cannot reach a mouse. It did not move by one target.

Verified by eye as well as by number, at 390 with a coarse pointer: the event-detail range rail, the
market disclosure and the rules tabs all stand at 44 and the page is 93px taller for it.

### What was left out, and it is two rows rather than a silence

**Width is not floored, and that is a decision.** 212 targets at 390 stand 44 tall and under 44 wide,
and they are short words: `NO` at 42.7, `1d` at 35.9, `Reply` at 35.9, `All` at 42.2. A word's box
comes from the word, and widening every one to 44 changes what a rail and a tab row look like. That
is a layout decision about six components, not a floor. **Backlog 50**, owner Responsive.

**Three native checkboxes on `cookie-consent.html` render 18x18**, and they are the only targets in
the product that a finger has to hit rather than read and that fall under WCAG 2.5.8's 24x24. They
took no floor because the rule names families the system declared and a bare checkbox is not one. The
fix is a `<label>` wrapping the row, which is markup plus a component and therefore goes into the
system first. **Backlog 51.**

### What this does to item 40

**It stops being what the floor depends on, and stays open on its own terms.** The 317-edits argument
was wrong about the mechanism: `min-height` on the family out-specifies whatever the control
computed, so the floor cost one rule. What item 40 actually complains about is untouched and is still
true: twelve rendered heights with three tokens behind them is a scale the geometry does not have,
and 38 still has 60 readings with no token behind it under a fine pointer. A floor does not give a
scale.

---

## 2026-08-08 - Three of the audit's findings closed, and the 44px floor takes direction B

The audit's own follow-up, done the same day. **Three closed, one direction decided, one left open on
purpose.**

### 42, the amount chip: the second place it stands is now named

`chip.css` scoped four rules to `.app-case` and nothing else, so a `.chip-amount` inside a `<dialog>`
matched no rule at all. **Confirmed rather than reasoned**: opening the deposit dialog on
`event-feed.html` gave the User Agent's `2px outset` border, an `rgb(239,239,239)` ground and square
corners, in a graphite product.

**The fix is the idiom the file next door already used.** `input.css` scopes the amount FIELD as
`dialog.app-dialog .amount-input`, which is why the field in that same sheet was always correct and
the chip beside it was not. The four chip rules gained `dialog.app-dialog .chip-amount` beside
`.app-case .chip-amount`. **A scope is kept rather than dropped**, so the chip still cannot leak onto
a course page, and `dialog.app-dialog` at 0,1,1 sits one step above `.app-case` at 0,1,0, which is the
right way round: a chip in a sheet is more specific than a chip in the case.

**Why not the markup.** Every dialog that is actually shown already carries `app-case` on itself and
every one that does not is shut, which is the only reason nothing rendered wrong. Adding the class to
the other three dialog types on 106 screens would be **a workaround applied three hundred times**, and
it would still require whoever opens a dialog at run time to remember a wrapper class for its contents
to be painted.

**Measured after, over all 106 painted screens: 420 User-Agent-painted controls to 0 with dialogs
closed, and 0 with EVERY dialog forced open**, which is the state the defect needed and had never been
put in. 480 chips checked, 0 changed that were already right.

### 47, the primitive ramps: the first fix was measured and rejected

The obvious fix was a second ink, dark on the pale swatches and light on the dark ones, and the page
already had the mechanism. **Measuring all 72 cells against both killed it**: 69 clear 4.5:1 with one
of the two and **three cannot clear it with either**, because a mid-tone has no good ink.
`p-bone-650` tops out at 4.36, `p-green-700` at 3.99, `p-ink-300` at 3.97. A per-swatch class would
have fixed 69 and left three defects wearing a fix.

**So the number came off the swatch.** `.tk-rc` is a column, the colour is a `::before` block and the
step number stands under it on the page ground, where `--text-muted` is a pairing this page's own
matrix already measures in both themes. It is better for the ramp as well: **a swatch with a number
printed on it is a swatch whose colour cannot be read clean.** `.tk-onlight` went with it and its 30
usages, because a class that paints nothing is what cost the previous stylesheet 800 lines.

**37 and 58 readings under floor, to 0 and 0.** What remains on the page is 15 per theme, and they are
the contrast matrix's own `icon-quiet` and `icon-brass` specimens: a graphical role held to the text
floor by a general instrument, whose floor is 3:1 and which clear it.

### 46, two of three: a prose claim now carries the correction beside it

`browse-shell.css` no longer claims `feed` and says in its place that the containment runs the other
way, with the two line numbers. `position-list.css` no longer claims `profile` and names the
2026-08-03 move that ended it. Both screen counts corrected, each keeping the number it was written
with so the drift is visible rather than erased. **`.read-col` at one screen stays open**, because it
is not a stale sentence but a slot below the threshold, and what it needs is a second and a third long
document rather than an edit.

### 49, the 44px floor: direction B

Two answers and no third. **(A)** drop the standard to what the system builds, 36 and 38, and write
that down as a decision rather than leave it as a forgetting. **(B)** make every control take its
height from a token, so the floor is one value in one place.

**B is chosen.** It is not done here and that is deliberate: it changes how every control is written,
reaches 106 painted screens, and the audit has to be re-run after it. That is its own pass, not the
tail of a rebuild. Until it runs, **the standard and the system disagree and the backlog is the record
of that** rather than a claim that it is fine.

---

## 2026-08-08 - Step 5, the audit, and it found six defects in itself and one in the product

The last step of the rebuild. **115 documents at two widths in two themes, 460 renders**: contrast,
overflow, focus, accessible names, alt text, duplicate ids, controls the User Agent is still
painting, broken links and touch targets. The full account is
[`ui-kit/docs/audit.md`](../ui-kit/docs/audit.md). The instrument was written in the scratchpad, run
once and deleted; nothing runs any of it on a schedule.

**The ratio is the report.** Six of the seven findings were in the instrument, and three of the six
were at a scale that would have been believed.

### The three that would have been believed

**434 daylight contrast failures.** The batch waited with
`await new Promise(r => { f.onload = r; setTimeout(r, 900) })`, which resolves on **whichever fires
first**, so a page slower than 900ms was measured mid-load and the theme attribute was set on a
document about to be replaced. `.btn-secondary` came back at 2.40:1 on a hundred screens. Measured on
one of them with the load awaited: **13.93:1**. The button was never wrong. Fixed by awaiting
`onload` with a guard rather than racing it, writing the theme to `localStorage` before the load so
the page's own boot agrees instead of being corrected afterwards, and settling two frames.

**212 overflows.** Every screen reported `.dropdown` past the right edge while the page scroll was 0,
which is the contradiction that gave it away. Chrome puts a closed `<details>`'s content in
`::details-content` with `content-visibility:hidden`: **the child still computes `display:block`,
still returns a 260x185 rectangle, and is never painted**, and nothing in its own computed style says
so.

**14,377 undersized touch targets.** The course panel's own rows, 107 per page. The panel is chrome
and not the product.

### The three smaller ones

A `feTurbulence` noise texture is not a gradient, and bailing on any `background-image` left **191 of
452** text elements on one page unmeasured. Text at `font-size:0` is a placeholder label, not text,
and it produced 12 failures at 1:1. And the CSSOM walk found **0** `:focus-visible` rules in a system
that writes 18, because `index.css` is nothing but `@import` and an imported sheet's rules live on
`.styleSheet.cssRules` rather than on `.cssRules`.

### What held

| | |
|---|---|
| contrast failures in the product, both themes, both widths | **0** of 29,929 and 29,984 text elements per pass |
| text the instrument could not measure | **0** |
| elements past the right edge that cannot scroll | **0** |
| documents with horizontal page scroll | **0** of 115 |
| focusables inside `.app-case` taking the ring, walked with real focus | **56 of 56** |
| `:focus-visible` selectors that REMOVE a ring without replacing it | **0** of 18, in 9 files |
| links, buttons or summaries with no accessible name | **0** |
| images without `alt`, documents with a duplicated id | **0**, **0** |
| internal links / broken | **15,880** / **0** |

**Focus is one rule.** `base.css` writes a bare `:focus-visible{outline:2px solid var(--focus-ring);
outline-offset:2px}`, which has no subject and therefore matches everything, so coverage is 100 per
cent **by construction rather than by enumeration**. Thirteen of the eighteen selectors draw, five
refine an offset or a radius, and none removes.

### The one product finding, and it is a decision rather than a bug

**WCAG 2.5.8 AA is met and the project's own floor is not.** 2,692 of 2,709 product touch targets at
390 clear 24x24; **1,787 of 2,709 miss 44x44**, which is this project's own standard from the
Stage-08 critique. The 17 below AA are wide short rows, not small dots.

The 1,787 are **one decision repeated**: `.chip-quiet` renders 38px tall on 530 elements,
`.chip-lane` 41px on 312, `<summary>` 35 to 36px on 234, `.logo-btn` 40px on 105. **The system builds
to 36 and 38 and the standard says 44**, and that is backlog 40's question in another form: three
control heights are declared and twelve render, because 192 of 317 boxed controls take their height
from padding plus font size plus a border. A control that read a height token would be one edit from
44; a control that computes its height from three other values is 317 edits away. Backlog 49, filed
pointing at 40.

### Two things it confirmed rather than found

**420 controls per render wear a system class and the User Agent's `2px outset` and
`rgb(239,239,239)`, and 0 of them are visible.** All are `.chip-amount` in closed dialogs outside
`.app-case`, which is backlog 42 read from the source and now counted across the whole tree. And
**0 of the 13 document-unique ids the system depends on appears twice on any screen**, which is the
other half of what `organisms.html` found: the coupling exists and has never fired. Backlog 45.

**And one it re-measured upward.** The dead footer promises are **23 distinct labels over 1,902
anchors**, 17 of them on 105 screens each, against the 16 labels and 1,664 links item 27 records.
Two of the 23 are the same destination under three spellings, `Privacy`, `Privacy Policy` and
`Privacy policy`. Backlog 48.

> **Corrected the same day.** This entry first named a fourth, `Privacy Policynot built`, and called
> it a broken string. It is not: `terms.html` writes `<span class="rel-q">Privacy Policy</span>` and
> `<span class="rel-odds">not built</span>` inside one anchor, four times, and the label extractor
> joined the siblings. **That is the audit's seventh instrument defect and the only one that reached a
> document**, which is the report's own argument arriving one step late.

**With this the rebuild is done**: five steps, nine hand-written pages, four foundation pages and a
page per level for all four rungs, no generator, no gate, and a report at the end of each step.

---

## 2026-08-08 - Step 4d, the patterns, and a prose claim with no reader

**The fourth rung, and the only one whose criterion is repetition rather than nesting.** Six files,
181 lines, and `ui-kit/patterns.html` is a page about a measurement rather than about a specimen,
because a pattern has almost nothing to look at: what it contributes is printed beside each
arrangement instead of photographed.

### The contract holds where it counts

**59 declarations across the six files, 16 distinct properties, and not one of them is a colour, a
face, a border or a surface.** No `color`, no `background`, no `border`, no `fill`, no `box-shadow`,
no `opacity`, no `font-family`, no `font-size`, no `font-weight`. What is there is `display`, `flex`,
`flex-direction`, `grid-template-columns`, `gap`, `align-items`, `justify-content`, `flex-wrap`,
`padding`, `margin`, `min-width`, `max-width`, `position`, `bottom`, `width` and `z-index`. **Every
one an arrangement.**

**Five of seven screen counts in the file headers are exact and two are one light**, `.cat-layout` 76
claimed against 77 measured and `.feed-head` 70 against 71, because the headers were typed when the
painted tree was 105 screens and it is 106. **That drift is the accepted price of the rule that a
measurement is an act rather than a machine**, and the price is one screen against the seven days the
machine cost.

### What it found: a prose claim with no reader goes stale

Each file opens with an `Assembled from` line and nothing reads it. Read from the screens instead, by
taking every element inside each pattern's own box across the 106 and asking which file owns its
class, **two of the six are wrong**:

**`browse-shell` claims `feed`, and the containment runs the other way.** On `event-feed.html`,
`<main class="feed">` opens at line 361 and `<div class="cat-layout">` at line 469: the feed HOLDS the
browse shell. Nothing renders wrong, and it is still worth correcting, because **an "assembled from"
line that names a parent is the level arithmetic's blind spot written down by hand.**

**`position-list` claims `profile`, and that stopped being true on 2026-08-03.** The record block in
the stack is `.pos-record` with its `.pos-figures` and `.pos-fig`, and those moved to `position.css`
in the pass that closed backlog 17. The block is still in the stack; the file that owns it is not.
`profile.css` owns seven classes today and none of them stands in a position list.

**And one slot in a pattern file stands on one screen.** `.read-col`, eight declarations over three
rules in `browse-shell.css`, on `ui-visual/terms.html` and nowhere else, two short of the threshold
this rung exists to enforce. **The reason it was written there is good and it is a different
question**: "the container owns the distance, not the block" answers WHERE the rule goes if it
exists, and the threshold answers WHETHER it exists yet. The two were answered as one. It is named
rather than moved, because deleting eight correct declarations to put them back on the third screen
is tidiness that costs more than it returns. Backlog 46.

### A third component whose visible content is not in its markup

The browse shell's rail ships as `<nav class="subcat" id="subcatRail" hidden></nav>` and a page
script fills it from a table of sub-categories. After the card's odds bar (found by the vitrine,
which counted 213 uses of something in no HTML file) and the chart's empty polyline (found by the
organisms page), **that is three, and all three were found by putting the thing on a stand rather
than by reading a file.**

### One rule was corrected on two pages before it shipped

The declaration counts were first drawn as bars, and **all six bars came out the same length**,
because `.tk-bar>u` has no width of its own and fills its track. A bar chart whose bars do not
represent their values is worse than a table, and the same shape was already on `organisms.html` for
the id counts. Both are tables now. That is the page's own rule applied to itself: a missing value is
a value, and the missing value here was the width.

**The kit is now a page per level, all four rungs**, on top of the four foundation pages. Verified at
390 and 1280 over the nine pages: 12 panel rows each, the active row always the page itself, 200
theme figures with 0 lacking an explicit `data-theme`, 0 blank cells, 0 duplicated ids, 4 distinct
radio group names where two copies of one specimen would have shared one, 13 link targets and 0
broken, 0 horizontal page scroll at either width, 0 console errors.

---

## 2026-08-08 - Step 4c, the organisms, and the thing a level page exists to find

**Thirteen at level 3, twelve measured and one named as unmeasured.** `ui-kit/organisms.html`, the
markup the screens ship, painted by `components/index.css`, with what each holds, its rule and its
anti-rule. `profile` stands on no anchor and gets no level rather than a guessed one, the same
treatment `account`, `cookie-consent` and `toc` got a page earlier.

**The themes stack instead of sitting side by side, and that is the subject deciding the shape for
the third time.** The vitrine's three-column table works for a control; the molecules page moved the
label above and split the width because a trust strip does not fit in 400px; an organism is the width
of a screen, and **a header cut to 430px is not a header**. What a shell IS is the decision it takes
about the full width, so a two-column pair would be measuring something else and calling it the
component.

### The finding: nine declarations are keyed to a document-unique id

**A class can appear a thousand times. An id is unique by definition**, so a rule written against one
is not a rule about a component, it is a rule about **one instance** of it. Counted across all 51
stylesheets:

| File | Keyed to an id | Ids |
|---|---|---|
| `tabs.css` | **6 rules** | `#edtab-comments`, `#edtab-holders`, `#edtab-positions`, `#edtab-activity`, `#ptab-record`, `#ptab-wins`, `#ptab-resolved`, `#p-record`, `#p-wins`, `#p-resolved` |
| `hero.css` | **2 paints** | `url(#hfyes)`, `url(#hfvol)` |
| `base.css` | **1 rule** | `#rmSidebar`, and it is correct: there really is one panel per document |

**Measured over the 106 painted screens: 0 of the 13 ids appears more than once.** One hero per feed,
one tab set per detail page. Nothing renders wrong today, the coupling has never fired, and **the
stand is the first thing that ever asked**, because a page that shows a component in both themes
shows it twice in one document by construction.

**Both are drawn once, on purpose, with the reason in the empty cell.** The alternatives were both
worse. Keeping the ids would make the daylight tab set share `name="edtab"` with the graphite one and
uncheck it, and would make a daylight hero paint its area with the graphite copy's gradient, because
`url(#hfyes)` resolves to the first `#hfyes` in the document and the stops read `var(--outcome-yes)`
against the theme of the copy that DEFINES them. Renaming the ids would leave the CSS pointing at the
other copy and the area would not render at all. **A stand that quietly shows a component painting
with another copy's values is worse than one that says it cannot show it**, because the first kind
looks plausible. Backlog 45, and it is the same family as `.app-case`: a dependency the system
requires and never declares.

### The one specimen that is not exactly what the product renders, said out loud

In the product a sheet is opened with `showModal()` and the browser lifts it into the **top layer**:
fixed, centred, over a `::backdrop`, one at a time per document. Four of them on one page cannot do
that. So the stand opens them with the plain `open` attribute and `.tk-dlg` pins them static, and
**exactly two things differ, the position and the backdrop**. Everything inside is the rule
`dialog.css` writes, untouched. It is written on the page rather than left for a reader to notice.

### Two more components whose paint is not in their markup

The chart ships `<polyline points=""/>` and a page script writes the points at load, so the specimen
carries the points that script produces for the "all" range. That is the second after the card's odds
bar, which the vitrine found by counting 213 uses of something that appears in no HTML file. Both are
written by hand into their specimens, and both say so. **"The chart is ported" was once true here
while it drew as a black rectangle**, because an SVG with no fill is black, and a missing value is a
value.

### And the honest answer to "is a shell a component"

`feed.css` is **eleven lines and three rules, two of which are a reset**. The whole of what it
contributes is `margin:0;flex:1`, the display face for the heading in its head, and a rule removing
its own background inside `app-case`. It is level 3 by the declaration and by the arithmetic, and it
has fewer rules than the smallest atom on the vitrine. **A level says what a thing HOLDS and has
never said anything about how much a thing draws.** It is shown with the emptiness drawn rather than
described, because a blank rectangle reads as a page that failed to load.

**Verified** at 390 and 1280: 13 sections, 26 theme figures, 0 blank, 0 duplicated ids in the
document, 0 elements past their figure that cannot scroll, 0 horizontal page scroll, 0 console
errors. Sweeps written in the scratchpad, run once and deleted.

---

## 2026-08-08 - The kit got a route back, and the deleted `_nav.js` was not what was wrong

**A registry was rebuilt under a name that had just been deleted, and the distinction is the whole
entry.** `ui-kit/_nav.js` went out with the instrument on 2026-08-07 and it deserved to: it was the
OUTPUT of `_gen_component_pages.py`, which wrote 38 pages and then wrote the route, and the rule it
lived under is stated out loud in the archive, "`_nav.js` is rebuilt, not edited". **A generated file
cannot be corrected by hand, because the next run puts it back**, which is how a hand-applied voice
rewrite was reverted here. The new file writes nothing and nothing writes it. **What the kit's rule
forbids ("a page is written by hand, no generator, ever") is a script that WRITES the tree**, and a
list read by a browser at load is furniture, not a machine.

**The measurement that decided it.** Both screen trees already carry their route hand-copied into
every page: **106 copies in `ui-visual`, 1,339 KB**, and **104 in `wireframes`, 1,247 KB**. Neither
has drifted (one distinct shape each, 107 and 127 rows, 0 dead targets, and all 106 painted screens
light exactly themselves), and neither could have stayed in step by hand: `_resync_sidebar.py` held
them and was deleted too. **The kit is seven pages and the drift was already there**, at that size,
with no script involved: six pages carried a hand-written jump row and the six had diverged into
five different sets, `vitrine.html` naming ten links including the three reports and `colour.html`
naming six and no report at all. All six now carry one empty `<div id="kitJump">`.

**It cost no CSS.** `components/course-chrome.css` was already imported by `index.css`, already
loaded by every kit page and used by none of them, and `base.css` already insets any body containing
`#rmSidebar` by 220px. The panel is the same chrome the 106 painted screens wear, drawer below 860px
and rail above. Two rules were added, both with their reason at the rule: the count slot on the right
of a row, and the dashed unclickable chip for a jump-row entry with no page.

**Two things taken from the same panel in the Stack repository, because both were paid for there.**
The active row is **computed from the file name and never declared**: every page there hand-wrote a
`KIT_ACTIVE` constant, one page was built from another and inherited its value, and the panel lit one
component while showing a different one. A file name cannot be a stale copy, because it IS the page.
And **a row with no page is visible**, as a `<span>` with the `.planned` badge, because a route that
lists only what is finished looks finished. **One thing not taken**: that panel writes
`style="opacity:.45"` on the rows it dims, and never on the element, and it is not needed, because
`.sidebar-page-link.planned` is the muted ROLE plus a badge and the reason is at the rule.

**A dead reference the consolidation could not see.** All **106** painted screens carried
`/* the kit side panel is rendered by _nav.js after this fires */` in their theme boot, naming a file
that had not existed for a day. Step 3e swept 37 such references and every one of them was in
`components/`. The line stays, because `wire()` is idempotent and the guard is free, but it now says
what it is: a guard and not a fix, since all 106 carry a `.theme-switch` in static markup.

**What it cost, stated rather than hidden.** The kit now loads one script, so the "0 scripts" badge
on three pages became **"0 generators"**, which is what was true all along. The route is not in
`view-source` without running JS; the repository already answers that one, "reading the source is not
reading the page".

**And one thing the switch found on its way past.** The categorical series was the only ramp on
`colour.html` drawn in a single theme, and its five roles DO theme (`cyan-400` to `cyan-700` and so
on, the light values carrying measured ratios of 6.1 to 7.3 in `tokens.css`). A ramp that themes and
is drawn once shows whichever theme the reader is in and says nothing about it. It is a pair now.
Verified after: **162 theme figures across the seven pages, 0 without an explicit `data-theme`**, so
the page switch moves the stand around the specimens and never a specimen.

---

## 2026-08-07 - The instrument was deleted, and the product was not touched

**What was deleted.** `ui-kit/` in full: 65 generated pages, 18 Python scripts, 9 browser scripts,
41 build gates in 109 checks, a state-capture instrument, 288 tracked files and 145 MB of
screenshots. With it, `wireframes/_generators/` (36 scripts), `ui-visual/*.py` (18), five scripts at
the repository root and four elsewhere. **The repository now contains zero Python** outside
`figmosha2/`, which is a Figma bridge and has nothing to do with the design system.

**What was not touched.** `components/` (51 stylesheets, 5,651 lines), `ui-visual/` (106 painted
screens), `wireframes/` (104 grey screens), `ia/`, `voice/`, `research/`, `concept/`, `DESIGN.md`,
`PRODUCT.md`. Not one pixel of the product moved, because the product reads
`components/index.css` and nothing in that path was edited. The single reference the screens had
into the deleted tree was one sidebar line per file pointing at `ui-kit/overview.html`, and that
page still exists.

**Why.** The measurement had become a machine. A one-line change to a stylesheet cost a
regeneration of 42 pages, a re-capture of the state readings in a browser, 41 gates, 525 snapshots
and an audit run: minutes of compute and an hour of care, for an edit that moved one value. Seven
days of work in the last stage produced 14 closed backlog rows and an atom-map distance of 0, and
every one of those closes was real - and the same seven days produced no new screen, no new
component and no answer to the product's own open questions. **An instrument that costs more than
what it measures is not rigour, it is overhead wearing rigour's clothes.**

**What the comparison said.** `Stack sportpit`, the same author's project one stage behind, holds
71 components in 5,349 lines of CSS and 35 hand-written kit pages, with **zero scripts and zero
gates**. Project One held 51 components in 5,651 lines - the same system, to within five per cent -
behind 63 scripts and 41 gates. The census in that project is a one-off report in `census.md` and
`consolidation.md`: walked once, written down, decided, done. Here the same census became a
permanent check that every later edit re-paid.

**What was kept, and where.** `docs/kit-archive/` holds the eight documents and the 48 authored
component pages, read by nothing. The four things worth taking forward are named in its README: the
level formula, the S34 size measurement (9,648 readings, 66 distinct faces of one control kind), the
rule and anti-rule per component, and the defect log. **What was rejected** is keeping any of it
running: a gate that is kept "just in case" is the whole cost with none of the decision.

**What replaces it**, in order: a census of five anchor screens with their states, read in a browser
at two widths in both themes; atomic levels declared once in an inventory; one consolidation pass
where a value is allowed to change and every change is measured; one hand-written page per component
carrying its states in both themes; one audit run as a report. The five anchors are event feed,
event detail, active bets, deposit and sign in, with their loading, empty, error and logged-out
variants: 41 screens of the 106.

**And `CLAUDE.md` inverted its own rule.** It used to say a rule may leave that file once a gate
holds it. With no gates, nothing holds anything except reading, so every rule in it now carries the
reason it exists rather than the number of the check that enforced it.

---

## 2026-08-04 - How much the instrument was missing, measured, and why the merge comes after the shot

**S27 closed, and the useful number is not the one it opened on.** It opened at 64 duplicate
pictures across five components. That was an arithmetic assumption, not a count: it multiplied the
redundant groups by 8, and three of them do not hold 8 pictures. A `card` group holds 6, because a
card is not focusable; a `tabs` group holds 4, because a hidden radio raises no hover and no press.
**The real upper bound was 56**, and the pair list was right in every case. The correction was
reported before anything was deleted, which is the only reason it mattered: the number was in four
documents and none of them was load-bearing, but a count nobody re-derives is how the false zero got
printed fifteen times.

**The result per component, because the verdict is the deliverable and not the total.** `card`:
two pairs, both duplicates, 12 pictures. `hero`: one pair, duplicate, 8. `event-detail`: one pair,
duplicate, 8. `header`: one group of four, duplicate, 24. `tabs`: **nothing merged**, and the pair
became a defect instead. **44 of the 56 were duplicates, 4 were a defect, and 8 were a real
difference the old instrument could not see.** System 766 pictures to 714, 94 groups over 24
components, `NOT_RECAPTURED` empty, gate 36 now unconditional.

**HOW MUCH THE OLD FACE WAS MISSING, which is the measurement worth keeping.** A face was five
values and it is nine now. What the five could not see, found by re-capturing:

- **`card`'s entire hover.** `.card:hover` is `translateY(-3px)` plus a shadow, and neither
  `transform` nor `box-shadow` was among the five, so the recorded value under the hover picture was
  **the same string** as the value under the rest picture. The pictures were right; the number
  printed under them, which is the thing that makes a picture checkable rather than decorative, said
  nothing had moved. On a component that stands on every browse screen.
- **`header`'s `.bal-add`.** It merged into the group of four under the old reading and does not
  under the new one: the plus that opens Add funds gives a different answer from the three ghost
  circles beside it. **8 pictures that would have been deleted as duplicates are evidence.**
- **`tabs`'s two hidden radios.** They differ by `opacity`, 1 against 0, which the old five could
  not see either.

That is the answer to "how much was the instrument missing": one component's whole interaction
layer, one real difference that a merge would have destroyed, and one defect that could not have
been found at all.

**AND THIS IS WHY THE MERGE HAPPENS AFTER THE SHOT AND NEVER IN THE KEY.** The cheap implementation
is to drop the element selector out of the grouping key, which is decided at rest, before a pointer
has touched anything. `card` is the proof that it is wrong: at rest a loaded card and a skeleton
card and, under the old face, a hovered card are all one string. Key on rest and one of a pair is
never photographed, so the difference is not merged away, **it is never measured**, and the page
then shows a single gallery with nothing to say it is missing anything. Everything is shot, and only
then does what agrees in all four states in both themes become one picture. It costs pictures that
are immediately deleted and it is the only order that can be checked afterwards.

**`tabs` is the pass's third verdict, and the pass is worth more for having one.** Its pair is not a
duplicate and not a real difference: `components/tabs.css` hides a CSS-only tab's radio twice,
differently. Line 12 parks `.ed-tabradio` at `left:-9999px`, measured as a 13x13 box at x = -9941;
line 18 gives `.ptab-in` a 1x1 box at `opacity:0`. The file's own comment says the first painted the
focus indicator off the left edge of the document, and that the second was written so the ring lands
in the right place and is then painted at zero alpha, "which is the same nothing". **The second
mechanism exists because the first one failed, and the first one is still there.** Nothing merged,
the pictures stay, and it is `ui-kit/docs/defects.md` row 48 with a closing condition written as
something a check could ask: one hiding idiom per repository, declared once, and any second one
fails.

**The warning about `header` was checked directly and the answer was the opposite.** A group of
four, three of them a button holding one mark and the fourth a `<summary>` holding a wrapper with a
mark AND a count badge, which is an extra zone and a different element. It merged anyway, and the
evidence is in the stylesheet rather than in a reading: `components/header.css` gathers `.icon-btn`,
`.notif-menu summary` and `.avatar-menu summary` into one rest declaration, one hover and one press,
after measuring the shape across all 105 screens at 360 and 1440. What differs is the ELEMENT,
because a summary opens a dropdown and a button does not. The same comment records that the
logged-in against logged-out reading was investigated from a screenshot and rejected. The badge is
content inside the circle, carries no state rule of its own, and is live on the page in the
logged-in specimen.

**Nothing was merged without asking what evidence it deletes**, and in three cases the answer was
the same: the thing that would be lost is live on a page. The skeleton card's own look is
`skeleton.html` with `skeleton-grid` in a frame; the bell with its badge is `header.html` with
`header-in` in a frame; `.hh-name`'s size is `hero.html`. Where the answer would have been "nothing
shows this", the pair stays.

**One finding that was not a merge at all.** `event-detail`'s two groups were split by `.ed-act`, a
class written 27 times in each tree and read by **no stylesheet and no script**: the rule that paints
the row is `.ed-actions button`, which matches with the class and without it. So the two faces were
identical by construction and dead markup was the only thing telling them apart. `ui-kit/docs/backlog.md`
S28. Checked and deliberately not filed with it: `.prov-google` is read by no rule either and
correctly so, because that mark carries its own brand colours while `.prov-x` and `.prov-apple` are
filled with the current colour and need one.

**Browser, 360 and 1440, both themes, over the five touched pages: 0 findings after one repair.**
20 combinations, every state picture forced eager and waited for, 188 pictures loaded, 0 broken, 0
console errors, every live specimen driven with a real pointer. The repair is its own commit and was
not this pass's doing: `tabs.html` pushed the document 22px sideways at 360, and measuring the rest
of the vitrine found feed +46 and footer +27 with the same cause, a path or a selector inside prose
with nothing in it to break at. One element rule, three selectors after the two that matched nothing
were removed, `pre` deliberately excluded. **4 of 56 stand pages overflowed at 360, now 1**, and the
one left is a different cause with a number and a closing condition rather than a guess: S29.

**One false negative caught in the instrument rather than reported as a defect.** The first browser
pass said `tabs.html`'s live specimens do not answer a pointer. They do: the script had hovered the
tab that was already current, whose ink is already at the strong value. Driven on a non-current tab,
both specimens move from `rgb(164, 157, 143)` to `rgb(237, 231, 218)`. A clean result about the
wrong object is the shape this repository keeps finding, and it is worth noting that this time it
was found in the checking script within the same hour rather than in a document fifteen printings
later.

## 2026-08-04 - The unit of a picture is a difference, not an occurrence

**What was on the page.** `ui-kit/button.html` carried **eight state galleries** for a component
that makes **five decisions**. The three extra were `.state-btn` beside `.auth-btn`,
`.state-btn.primary` beside `.auth-btn.primary`, and the second child of `.cta-bar`, and the
authored source names all three as the same answer in its own prose: "Identical answers, which is
the point", "Same three-step", "the answer is the family's". **24 of that component's 64 pictures
existed to show that two things look the same.** Every gate was green.

**Why a page like that gets worse as the product grows, which is the actual reason to fix it.** A
gallery per PLACE tracks the markup: add a sixth place for the same control and the page grows a
sixth gallery and says nothing new. A gallery per DIFFERENCE tracks the system: add a sixth place
and the page does not move, because no decision was taken. The same inversion runs through the whole
page, which is why the axis matrix was rebuilt at the same time and in the same direction: **the
page specifies the axes and the five names are a column**, not five sections.

**THE MECHANISM, and it is the part worth carrying forward.** The capture keyed a group on
`element selector | rest face`, so the class name was part of the identity and one control under two
names was two groups by construction. The selector is out of the key now. The merge deliberately
happens AFTER the shooting rather than before it, and that is not an implementation detail: a
difference is free to live in any of the four states, so keying at rest means one of a pair is never
shot at all. That does not merge a difference away, it stops it being measured.

**And the instrument could not see the difference it was being asked about.** A face was five
values. The two things that make this family's members differ are a one-pixel lift and a glow -
`transform` and `box-shadow` - and neither was among the five. So `.provider-btn` read as identical
to `.auth-btn` while both `components/button.css` and the authored page said it is not, and a merge
on that reading would have deleted the picture of a real difference. **The list was also written in
three places** (twice in `browser.cjs`, once in `states.cjs`) and had already drifted by a property.
It is one function now, in `browser.cjs`, and it carries transform, box-shadow and opacity. Size
stays out on purpose: a different padding is the same face at a different size. This is the fourth
time this run that the finding was "the check was clean about something it never looked at".

**Result, measured.** button: **8 groups to 5, 64 pictures to 40, 24 deleted**, which is exactly the
three groups the source itself called identical. The system: **792 pictures to 766**, the other two
being `tabs` focus pictures that belonged to no group at all and had been sitting in the tree behind
a check that only ever asked whether a NAMED file was still there. The five that remain are one base
set plus one named difference each: the modifier, the one-pixel lift, the missing edge, and the dark
ink on the first child of an action bar.

**Gate 36, proved in three directions.** Forward: putting one occurrence back as its own group turns
it red, and gate 32 goes red beside it, which is the pair working as intended - 32 asks whether every
group is described, 36 asks whether the group should exist. Backward: a declared not-re-captured
entry that holds no duplicate fails as idle, and a picture copied into the tree with nothing pointing
at it fails as an orphan. **Five components still hold the same defect** - `card`, `header`,
`event-detail`, `hero`, `tabs`, 64 pictures - and they are declared rather than fixed, because they
were shot under the old five-value face and their count is an upper bound that only a re-capture can
settle. `ui-kit/docs/backlog.md` **S27**, and the list clears itself.

**The size axis has no rule, and the page says so in those words.** This is the one place the work
was asked to derive a rule from the product and the product refused. Measured in Chrome at 1440 and
360: container height does not predict the font step (the state block is 245 tall and takes the
smallest, the action bar is 70 and takes the middle one), and the share of the container looks
monotone until two placements break it in both directions - `.resolved-panel .state-btn` is full
width at 12 and `.bet-dock .confirm-btn` is fit width at 14. **The step follows the NAME.** Worse,
one class carries two steps: `.provider-btn` is 13 in its own rule and **14 inside the sign-in and
outcome sheets, which is 322 of its 444 uses**, so the size a person meets is not the size the
stylesheet declares first. The page prints "a fact without a rule" rather than a plausible sentence,
because an invented rule is worse than a missing one: a missing rule sends the next person to look,
an invented one sends them away satisfied. `ui-kit/docs/backlog.md` **S25**.

**The other three axes do have rules, and each was tested rather than asserted.** WIDTH: full when
the control owns its row, shared when the row is split evenly, fit otherwise - **0 exceptions in 710
placements**, and the two that look like exceptions are the rule being applied by the container.
EMPHASIS: one brass action per zone - **zones carrying more than one, 0**, counted over every dialog
and action bar in the painted tree. ICON, which is the fourth axis and did not exist on the page
before: a mark only where the label names a third party - **322 of 710 carry one and every one is a
brand mark on a Continue with row**, the other 388 carry none. The mark had been written up as a
private detail of one place, so "a button with an icon" was not something the system had declared.

**Every empty cell carries a verdict and a source.** Three are FORBIDDEN with a product counter
behind them - icon with brass (0 of 710), icon at fit width (0), full width in the header (0, and it
is the width rule applied rather than a separate ban) - and two are UNCLOSED ZONE with a backlog
number: a disabled control anywhere but `.confirm-btn`, which the product has simply never had, and a
marked control at fit width inside a sheet, which two rules each half-forbid and neither settles.
`ui-kit/docs/backlog.md` **S26**. A blank cell is neither, and there are none.

**S24 is not closed and was not touched.** It is the CSS consolidation and its closing condition is
still the markup thaw: the stylesheet is unchanged, the 13 reconciliation rules are still 13. What
its row gained is one sentence saying the page now answers with axes instead of a list of places.

**Asked of a browser: 360 and 1440, both themes.** 5 galleries, 2 covers notes, 40 pictures, 0 broken
images, 0 horizontal overflow on the page and 0 inside the live frame, and the specimen driven with a
real pointer and a real focus: the quiet ground moves on hover, the brass one takes its glow, the
ring is solid 2px. **0 console errors** on three of the four combinations; the fourth is Chrome asking
the static server for `/favicon.ico`, which this repo does not ship and which appears on the first
context of any launch. Watched at the network layer instead, the page makes **0 failed requests**.

## 2026-08-04 - 104 marks of markdown on four pages, and every gate green

**What was there.** `ui-kit/_gen_docs.py` renders the stage's seven documents as pages of the
vitrine. It does not implement links. Markdown links were therefore printed rather than rendered:
**102 of them**, in 97 rows of `inventory.html` where `](../header.html)` sat in the open beside
the word it was meant to be a link on, and in three paragraphs of `architecture.html`,
`history.html` and `backlog.html`. Two more marks were `**` from a bold span that never fired. 104
literal marks on four shipped pages, and the build was green on all 34 gates.

**Why nothing saw them, and this is the part that generalises.** Gate 21 re-renders each document
in memory and compares the result with the page. That certifies the page is what the generator
makes and nothing else, which is the right question about drift and the wrong question about
correctness: **a defect in the renderer is reproduced identically on both sides and reads as
agreement.** A generator compared with itself is a tautology. It is the same shape as row 42 in
`ui-kit/docs/defects.md` - a check reporting clean about the wrong object - and the same answer as
gate 22, which asks the panel where it is rather than asking the shell.

**Three defects, not one, and the second is the one worth the entry.**

**1. Links were not implemented.** Now they are, and the order inside `inline()` is the whole of it:
after the code-span lift-out, so the label of ``[`history.md`](./history.md)`` is already a
placeholder and the backtick cannot be read as anything else; after `esc()`, so the address arrives
attribute-safe and is not escaped a second time. Inside a link label, FILEREF linking is
**suppressed**, and that is named in the code because the markup it prevents is invalid rather than
merely ugly: the label of ``[`history.md`](./history.md)`` is a code span whose text FILEREF
matches, so left alone it would have produced `<a>` inside `<a>`. It also settles a subtler one the
same way. In ``[`docs/backlog.md`](../../docs/backlog.md)`` the label's TEXT resolves through the
mirror map to this stage's backlog page while the ADDRESS means the root document, so linking the
label sent the reader somewhere the author did not write. The address is the link; the label is
what it is called.

**2. Every address was one directory off, and that is where the real defect was hiding.** The
sources are in `ui-kit/docs/` and the pages are written in `ui-kit/`, one level up, so an address
carried across unchanged points somewhere else: `../position.html` in the markdown means
`ui-kit/position.html` and from the page has to be `position.html`, and `../../docs/decisions.md`
has to become `../docs/decisions.md`. `rebase()` moves each address from the document's directory
to the page's and **fails the build** on one that does not resolve from the directory the page is
in. That is deliberate and it is gate 4's idiom moved one step earlier: a generator that can prove
an href before writing it should not leave a dead link for a gate to find afterwards. Proved by
changing one address to `../history.md`: the generator exits 1 naming the document, the address and
what it resolved to, and `_check_kit.py` exits 1 with it.

**3. A number that ends a sentence is not a list.** These documents wrap at 100 columns, so
`history.md` has lines beginning `17. The port wrote...` and `1400. Measured at 1920...` - the tail
of "on every one of the 17." and of "stopped at 1400." The paragraph ended at the digits, the next
block was read as an ordered list, and a `**bold span**` that straddled the break was opened in a
`<li>` and closed in a `<p>`, so neither half fired and the asterisks printed. The rule that
settles it is CommonMark's, and it is the rule because it exists for exactly this: **an ordered
marker may interrupt a paragraph only when its number is 1.** At the top of a block any number
still starts a list. That one-character change rewrote nothing but the two pages that carried the
defect, which is the evidence that it is a rule and not a patch.

**A link to a `.md` with no mirror stays a `.md`, and it is a named exception.** A document this
stage renders is linked at its PAGE - that map already exists and gate 21 keeps it current. The
root `docs/decisions.md` and `docs/backlog.md` have no page to be linked at: they belong to the
project rather than to the stage, nothing renders them, and the documents genuinely cite them, so
the choice is an honest `.md` href or a sentence that names a file and cannot reach it. Gate 21's
"no link into a raw `.md`" now exempts those **two addresses** rather than any page, because
whether a mirror exists is a property of the target and of nothing else, and it carries the control
every declared list in this repo carries.

**Gate 35, proved in both directions.** Forward: disabling the link substitution and re-rendering
turns gate 35 red on all 102 marks **while gate 21 stays green**, which is the tautology
demonstrated rather than argued; reverting the ordered-marker rule alone turns it red on the 2
remaining `**`, again with gate 21 green. Backward: a declared exception that covers nothing fails
as loudly as an undeclared defect - a `MD_LITERAL` entry for a page with no literal markdown and a
`MIRRORLESS` address nobody links both failed on the first run. The corpus is **every generated
page**, 132 of them, not the seven documents, for the same reason the SCENES comment gives at the
top of `_check_kit.py`: `inline()` is imported by the component and pattern generators too, so a
link authored into a rule or an authored section is rendered by the same code and belongs to the
same question. Measured before and after: **104 marks -> 0.**

**And it went red on the document that describes it**, which is how it learned the last rule it was
missing. The `defects.md` row written for this gate quotes both marks inside `code` spans, so the
first green build after the row was added was not green. A quotation is not a survival: the scan now
strips `<code>` and `<pre>` first, using the same `QUOTED` that gate 4 has used since prose about a
path was reported as a path. That is the **fourth** checker in this file to have to learn to stop
reading a sentence as the thing the sentence is about, and it costs the gate nothing here, because
all 104 marks were in running text - a table cell and a paragraph break - and not one of them was
inside a quotation. The two-way proof was re-run with the strip in place before it was kept.

**Asked of a browser as well, because a checker that reads the source does not read the page.**
Seven document pages at 360 and at 1440, Chrome, and the question asked of `innerText` with every
`<code>` and `<pre>` removed first, so the instrument asks what the gate asks: **0 visible markdown,
0 nested anchors, 0 dead hrefs resolved from the page's own directory, 0 horizontal overflow, 0
console errors** over all 14 renders. **225 `a.tk-doc-ref` anchors** per width, 102 of them the
links this entry is about and the rest the file references the vitrine already drew, and every one
of the 225 carries its border in the computed style, which is the difference between an `<a>` and a
word that used to be sitting next to a bracket.

**Two stale counts corrected while the row was added**, both hand-written and neither gated:
`ui-kit/docs/defects.md` said "34 gates over 80 checks" when the file held 82, and its PROVEN table
said 25 classes over 26 rows. They are 35 gates, 85 checks and 27 rows now. The README's two spans
are computed by `_fill_inventory.py` and were right, which is the difference the computed span buys.

## 2026-08-04 - Step 8, and the six things a taxonomy could not have told us

The inherited plan for this step was eighteen classes of defect, hunted by hand, over 105 screens in
two themes at two widths. What it became is `ui-kit/docs/defects.md`, whose first column is not a
category but **which gate catches it**, because a green gate is a proof and a manual pass over a
gated class is a second, worse instrument reporting on the same thing. The table opened at 23
proven, 7 measured and 15 open; it closes this step at **26 proven, 7 measured, 11 open**.

Four gates were added or grown, and every one of them was proved in both directions and given the
control this repo puts on every declared list: an entry that covers nothing fails as loudly as an
undeclared item.

### The five things that were found by fixing, not by looking

**1. The contrast defect was never a token value question.** `oddsbar.css` put `--outcome-yes` and
`--outcome-no`, the FILL roles of a 4px band, onto 12px bold TEXT. Surfaces answer to 3:1 and take
it; text answers to 4.5:1 and did not, on 266 elements across 105 painted screens. The text roles
already existed. **The fix is one word in each of two declarations**, no token moved and no value
edited, and all four measurements changed including the one that already passed, because leaving it
on the fill role would mean one component reading a different token per theme for the same word.
`ui-kit/docs/history.md` records this as the run's best evidence for having a semantic token level
at all: without a separate text role the only repair available would have been the VALUE, and the
bar would have moved with the label.

**2. Two of the three keyboard findings were not defects, and the real one was already written
down.** The test that settles it is the RESULT, not the handler. `.rules-panel` is not a control at
all - the control is `.rules-tab`, a real `<button>` on all 18 instances - and the four
`<span class="bp-side">` are skeleton placeholders on two loading screens, which must not be
focusable. `.opt-row` has a working keyboard route: Enter and Space on the inner button produce a
state identical to a mouse click in every field measured. **The one real blocker was
`docs/backlog.md` 22**, which had been sitting there since step 2: 16 filter inputs at
`display:none`, so three radiogroups on 104 screens could be operated by a mouse and by nothing
else. Closed with the idiom the system had already chosen twice, and the "eight or so new tab stops
per screen" objection in the original row is answered with a number: **zero when the menu is closed,
one when it is open**, because a radiogroup is one tab stop by construction.

**3. Both new gates failed on the defect they were written for, and that is why they are gates.**
Gate 33's two-way proof reverted each of the five trader-term placements one at a time and demanded
a red for each. Two came back GREEN: `holder` was not in the lexicon at all, because the list held
`position` and not the person who has one; and the scanner could not see inside an element whose
parent it had already consumed, because `finditer` does not overlap. Gate 34's idle control found
**eight dead rows of forty one** in the hand-written half of the inventory map, which is the same
half both false file cells had come from.

**4. Two hand-written cascade cycles were made of misfiled classes.** Moving 17 rules to the files
that own them took `_levels.ORDER_BREAK` from four entries to two, because `(comments, tabs)` and
`(betpanel, event-detail)` were not real nestings - they were `.seg` living in `tabs.css` and
`.rp-inner` living in `event-detail.css`. **A hand-written tie-break is a place where the map
stopped agreeing with the files**, so an entry there is now readable as a finding waiting to be
closed rather than as a setting. 525 snapshots at three widths, 0 differ, 0 elements changed.

**5. The instrument was cropping the subject of its own photograph**, and fixing it found two more
instrument defects underneath. 36 of 790 state pictures were short, every one a FOCUS picture -
the single state whose whole subject is a ring drawn outside the box. The pad is now DERIVED from
the element being photographed, in the state it is in. Underneath: a frame past the last pixel of
the document took the whole run down (a bet sheet is `position:fixed` and is not in the document's
scroll extent), and the clip and `boxAt()` had never agreed on a coordinate system - which was
invisible for as long as every specimen was too short to scroll.

### The two things that were measured and deliberately not paid

**The button family is not consolidated.** 5 names, 3 axes, 30 rules of which 13 are reconciliation.
The measurement is the decision: the axes do not fit inside `components/button.css` (the position
mechanism belongs to a pattern and the width to a `state-block` context), and the right answer for
emphasis is `.primary` in markup that is frozen. What is paid instead is the PAGE, which now opens
with the axis matrix. `ui-kit/docs/backlog.md` **S24**, closing condition written in: with the
markup thaw, not before.

**The inventory's `#f` column is not computed and cannot be yet.** 38 of the 54 rows whose classes
are findable disagree with a count of the files carrying them, and the disagreement is not all
error: some cells mean "files that carry the markup" and some mean "screens where a person sees it",
and a dialog emitted into 105 screens and opened on 4 is both. **S23**: a definition first, a column
second.

### The taxonomy re-run, with the caveat it has to carry

`node ui-kit/_verify/audit.cjs --screens` after every edit above: **106 pages, 2 themes, 2 widths =
424 renders, 0 findings**, 720 pinned boxes measured at 640px of window, 660 unmeasurable through a
blend or a filter and 380 painting no glyph, both counted apart. That instrument's zero is the one
that stood in three documents fifteen times while 378 elements measured under the floor, so it is
written here with its date and its corpus and not as a claim: it is not gated, and it is only as
good as its next audit.

## 2026-08-03 - The rail is a slot, and it took a real screen to find out

**What happened.** Step 7 of the Design System stage set out to test whether the system is
self-sufficient: build `ui-visual/terms.html`, a page of a TYPE the system had never drawn, out of
`components/` alone and count what was missing. It did that, and it also did something that was not
on the plan. It changed what `browse-shell` IS.

**The pattern stands on 77 screens** and had been read, correctly, as "a sub-category rail beside a
content column". Every one of the 76 screens that existed before Terms put the SAME component in the
rail: `catnav`'s `.subcat`. So the rail and the category rail were one idea, and nothing in the
product could tell them apart, because nothing in the product had ever put anything else there.

Terms put a table of contents there. After that the pattern reads differently: **the rail is a SLOT,
and the shell does not know which component is standing in it.** `components/toc.css` is a new
component that stands in the same place at a different sticky offset (66px against 120px, measured
rather than assumed, because a document page has no category bar for the header strip to condense
into), and `browse-shell` needed no change at all to hold it.

**Why this is recorded on its own, apart from the four backlog rows Terms opened.** The rows (S1,
S2, S5 closed the same day; S3, S4, S6, S7, S8 left open) are what the step promised: a list of what
the system does not have. This is not that. It is a correction to what the system already had, on
its most-used arrangement, and **it was not derivable from the 76 screens** - not because anybody
read them carelessly, but because a set of 76 identical answers cannot show you which part of the
answer was the question.

**The decision this settles for the stages after.** A demo screen tests whether the parts exist. A
real screen of an unseen type tests whether the parts mean what their names say. The two are not
the same exercise, and only the second one can rewrite a definition. Step 7 was scoped as the first
and delivered the second, so the next stage that wants to test the system should be scoped as the
second on purpose: **one real page nobody has drawn, not five variations of one that exists.**

**What it cost to get there:** no new class, no new token, no new state and no new rule on the page
itself, and 104 screens at two widths with 84,836 element boxes compared before and after, 0 moved.
The definition changed; the product did not.

---

## 2026-08-02 - Four states, three press mechanisms, and the hovers that were only true in one theme

Step 2 of the Design System stage: the states roll-out. The reference component was accepted in the
browser, and the format went out to the rest of the system through subagents, one round per level,
bottom up.

### The estimate, in three columns and not two

The pack assumes no component has states yet. This one had them in **24 of 36 files**, all of them
`:hover`, so the roll-out had to align a format rather than write one. The census, taken by asking
each file which of its selector SUBJECTS is an interactive element in the shipped markup:

| | count | |
|---|---|---|
| already had states | 24 | every one of them `:hover` only. One `:active` in the whole system (`loadmore`), three `:disabled`, four `:focus-visible` |
| interactive, no state at all | 3 | `market` (a `<summary>`), `bottomnav` (the tab bar, touched more than any other control), `position` (a card-link on 15 rows, which read as static because the anchor is written with `:has()`) |
| not interactive, gets none | 9 | declared in `_levels.STATIC`, one line of reason each |

The format audit of the first column found exactly three things, and only three: six
`filter:brightness()` hovers, no `:active` anywhere but one file, and no `:disabled` on the one
control the product actually disables.

### Rounds by the computed order, and only the css fanned out

Rounds came from `python3 ui-kit/_levels.py --order`, which gate 23 already enforces, not from a list
written by hand: atoms, molecules, then organisms in two batches, the ones containing another
organism last. Within a level the subagents ran in parallel; between levels, sequentially, because a
card that adds a hover before its button has one will draw the button a second answer.

**The fanout is narrower than the pack's and that is a strength.** The pack gives each agent its own
css AND its own page. Here the pages are generated and the states table is read out of the css, so an
agent touches exactly `components/<name>.css` and the parent regenerates every page in one pass. The
conflict disappears by construction and the page stays a projection of the code rather than a second
copy of it. `tokens.css`, `index.css`, `base.css` and `_nav.js` stayed with the parent, and an agent
short of a token stopped and said so rather than inventing one. Two did, and both were right.

### Three roles, and no component level

- `--bg-pressed`, the ground a held control settles onto. It existed as `--bg-chip-pressed` with a
  single consumer; the roll-out gave it twenty. Renamed for the STATE, because the icon button in the
  header is not a chip and settling it onto a chip's ground is a category error the next reader
  inherits.
- `--color-action-pressed`, brass held down, and it is needed by exactly the controls that are FLAT
  brass: the filter switch that is ON and a ticked cookie checkbox. Everything else brass is a
  gradient and presses by geometry.
- `--chrome-pressed`, the same step for the course panel. It cannot borrow the product role: section 3
  overrides that one and does not touch the chrome, so a shared role would press a graphite row to
  chalk on a daylight page.

**No component-level tokens.** The stage before this one deferred the decision to here with a
criterion: a component token is justified only where a state lands on no semantic role. Every state in
this pass landed on one, so the answer is none, and an empty component level "so it exists" would be a
third round of renaming with no flexibility bought.

### Three press mechanisms, each forced by a number

A press had to be answered three different ways, and the third one is the interesting one.

1. **A quiet control** settles onto `--bg-pressed`.
2. **A brass gradient** reverses its own angle, 135deg to 315deg, and drops its glow. The light falls
   to the bottom right, which is what a plate pushed IN looks like. It reads the two roles the rest
   state already reads and costs no value at all.
3. **A filled outcome control presses by DEPTH, not colour.** `--text-on-no` on a flat `--outcome-no`
   is 4.64:1, the floor with 0.14 to spare, and darkening the ground through the only role available
   costs 4.48:1 at 92 per cent and 4.29:1 at 82. A mix small enough to pass is a mix nobody notices.
   So the fill does not move: an inset shade at the top edge does, `--edge-shade-strong`, the same
   role every lifted stone in this system uses, and the ground the ink was measured on stays exactly
   where it was. Half a pair was refused on the way: YES has the room and NO does not, and a YES that
   darkens beside a NO that does not reads as a broken NO.

The same measurement fixed a second surface later: `--bg-pressed` LIGHTENS a `--bg-card-quiet` row in
the Vault and resolves to the same chalk step in daylight, so a position row also pays for its press
out of depth.

### Focus is a substrate answer, and this is the deliberate deviation from the pack

The pack asks for `:focus-visible` on every component. `base.css` declares it once for all 36 files,
and a browser sweep of 153 pages in both themes had already found 0 of 179 ring kinds without a
visible ring. Fourteen component files used to carry their own copy of that rule and twenty-four did
not, and gathering it was the whole point of the previous stage; adding twenty more copies would undo
it. **A component speaks up only when its GROUND needs something different**, which is the rule
committed earlier the same day.

Four did, and one of them was a real hole nobody had seen: the Event Detail tab strip and the profile
tab strip are radio groups, so the ring was being painted on the visually hidden `<input>` and a
person tabbing through either strip saw nothing at all. It moves to the label. The other three are
clipping: the category strip and both tab bars are scroll containers that cut an outset ring, and the
sheet grab sits flush at the top of a sheet that clips its own corners. All four take an inset offset
and keep the ring colour. The fifth is the how-it-works close disc, which sits inside a brass radial
glow where the brass ring measures 2.52:1 at the brightest point: it reads `--text-strong` instead,
5.33:1 and 10.13:1.

### Seven defects that only a press could find

Giving a control a state means reading its rest state, and that is where these came from.

| what | measured |
|---|---|
| `.bet-dock .confirm-btn` had no `background` anywhere | the rule names the panel and the sheet and not the dock, so Confirm bet rendered in the user agent's own ButtonFace grey on the four screens where a person places money |
| `confirm-btn[aria-disabled="true"]` on `deposit-minimum-not-met` | styled exactly like an enabled button |
| `.hh-all:hover` read `--color-action-lit` | 9.57:1 on graphite, **1.71:1 on chalk**. A pale brass meant to sit UNDER dark ink, used as ink: in daylight the link vanished at the moment a person pointed at it |
| `.hf-title:hover` and `.hh-name:hover` read `--text-strong` | which IS `--text-primary` on chalk: 14.85 over 14.85, a state that existed in one theme only |
| `.bp-side:hover` read `--bevel-strong` | a lit LIP role that section 3 raises to 70 per cent white: 1.02:1 as a border on a chalk control. A lip is not an edge |
| `.notif-all` had no hover | it is a sibling of the dropdown list rather than a member, so it fell out of the selector and out of every later reading of the file |
| `.hiw-full` had no hover | the only brass action in the system without one: the arrow nudged and nothing under it moved |

Six `filter:brightness()` hovers are gone with them. A filter multiplies whatever is beneath it, so no
theme and no role can reach it, and the same 1.08 is a different decision on each of the two stones.

### What was found and NOT fixed, and why

Three, all in the backlog as items 22 to 24. The filter panel hides every option with `display:none`,
which takes it out of the tab order and out of the accessibility tree, so the sort radiogroup on 104
screens works with a mouse and nothing else; the fix is css-only but it changes behaviour, and that is
a product decision rather than a state. A multi-outcome row is a `<div>` with a click handler and no
keyboard path, and the fix is markup, which the grey tree owns. And the `aria-live` row turned out to
rest on a premise that does not hold, below.

### The aria-live row was re-measured, and the count was right while the conclusion was not

The entry gate for this step asked whether gate 18 compares ATTRIBUTES or only structure, because a
live region is an attribute on a shipped screen. It compares structure only: `shape()` in
`_check_kit.py` builds `tag.firstclass` per element and reads no other attribute, and gate 19 uses the
same function. So the edit was clear.

The premise was not. Measured in BOTH trees: the 9 screens with a live region are identical in grey
and in colour, and the toast on `toasts.html` already carries `role="status" aria-live="polite"` and
`role="alert" aria-live="assertive"` on its two groups. There is no missing toast announcement to add.
What IS missing is the form-error axis, `aria-invalid` and `aria-describedby` at 0 of 105 while three
screens ship a visible error tied to no field, and that is a markup change the grey tree owns.
`aria-expanded` at 0 is correct rather than a gap, because every disclosure here is a native
`<details>`. Item 4 is struck and replaced by item 24.

### The gate, and the instrument

**Gate 25**, three checks: a component not on `_levels.STATIC` declares hover and press, a component
on it declares neither, and no state carries a colour value. The second check is the one that matters,
for the reason gate 24 already carries: an exception list that can absorb a component quietly is not a
declaration, it is a way of switching the check off.

**Measured at rest: 14 of 36,150 elements moved** over 25 screens in both themes, against a **noise
floor of 10** taken by diffing the same version against itself. Four of the fourteen are real and both
are named in the table above. **Focus: 0 of 128 ring kinds flagged** over 33 pages in both themes.

Two instrument bugs were found and fixed on the way, and both were caused by this pass adding
transitions. A control mid-transition between themes reports the tween rather than the value, which
produced 17 false flags in one run. And a ring was being measured against the control's own fill
rather than the surface it stands on: with `outline-offset` positive the ring is painted OUTSIDE the
border box, so a brass ring on a selected YES read 1.37:1 against a green it never touches. **A ring
answers to what it stands on** is not only a design rule; it is how the ring has to be measured.

## 2026-08-02 - A regex cannot read a colour, and one of the three defects it found did not exist

Two measurement bugs in one day, in the same sweep, and the second one invented a defect. Both are
worth the entry because the conclusion is the same and it is a rule: **the tool that reads the page
has to be checked as hard as the page.**

- **A closed `<dialog>` is inert, and a scripted `.focus()` on it fails silently.** The element does
  not become `document.activeElement`, `getComputedStyle` returns its resting style, and a sweep
  that measures the outline reads NO RING. The dialog amount field was reported broken by that
  sweep AFTER it had been fixed, and it was pressing Tab by hand that showed the ring was there. The
  sweep skips inert subtrees now.
  **What that invalidates:** every earlier "no ring" verdict on an element inside a closed dialog.
  There were two, both from the first pass over `event-feed.html` on 2026-08-02, `a.notif-all` and
  one unclassed `<button>`, and both were reported in chat only. Nothing in the repo carries them:
  the only "no ring" verdict written to a file was `.kit-field` in backlog item 21, and `.kit-field`
  is not in a dialog, so it stood, and it has since been fixed. No file needed correcting. That is
  luck rather than process: a verdict from a tool with a known blind spot was one commit away from
  being written down as a fact.
- **A regex cannot read a colour, and `color-mix(in oklab, ...)` is the case where it silently
  lies.** `getComputedStyle().backgroundColor` returns that function verbatim, and pulling numbers
  out of it with `/[\d.]+/g` yields the oklab components, 0.95 and 0.0005 and 0.016, which the
  contrast maths then treats as sRGB bytes. **A pale brass-tinted banner measured as near black.**
  On that reading the focus ring on the push banner's buttons came out at 2.72:1 against a 3:1
  floor, on three screens, and it was written into the backlog as a defect to fix.
  It is not a defect. Measured with the browser doing the parsing, the same ring is **6.95:1 in the
  Vault and 6.73:1 in daylight**. The fix is to stop parsing: a 2D canvas resolves any css colour
  string to sRGB bytes, so `ctx.fillStyle = <whatever the computed style says>` and read the pixel.
  The ancestor stack is then composited in order, alpha by alpha, instead of guessed at.
- **What that invalidates, and it is more than one number.** Every contrast figure this repo has
  taken with the regex sweep, wherever the ground came through `color-mix`. Two were written into
  `tokens.css` beside `--focus-ring` and are corrected in the same commit: the true spans are
  **6.67:1 to 9.06:1** in the Vault and **5.71:1 to 7.46:1** in daylight, measured over every
  focusable control on 153 pages. The direction of the error is the interesting part: it made
  things look WORSE, not better, so nothing shipped on a false pass. The next one might not be so
  kind.
- **What survives, and it is the useful half.** Two of the three rings were real and both are fixed.
  The one that was not real would have cost a new token and a new role, invented to solve a number
  that a canvas could have disproved in ten seconds. **A finding is not a finding until the
  instrument has been checked**, and the check is cheap: measure something whose answer you already
  know. A pale banner is pale.

---

## 2026-08-02 - The two "now, or never" surfaces are closed as NEVER, and that is the decision

`architecture.md` has carried a table of five unread surfaces since the close of Tokens and
Components. Three of them name a later stage as their owner. Two named no owner at all, only "now,
or never", and a row that says "now, or never" is not a decision, it is a decision postponed in a
form that never comes back up. Both are closed here, as NEVER, with the reason.

- **The 28 course pages' own content: 203 KB of inline css nothing has read.** Not read, and not
  going to be. Those pages are the course frame around the work, not the product: the one thing in
  them that a reader of this repo interacts with is the roadmap panel, and step 9 already took that
  out into `components/course-chrome.css` and holds the 28 pages to it with a generator and gate 22.
  What is left is 203 KB describing lesson pages, and a finding in it would be a finding about the
  frame.
- **The grey tree's inline css: 34 distinct `<style>` bodies over 104 pages, the largest 52 KB.**
  This one is closed by a rule we made ourselves and would have to break in order to act. The grey
  tree is frozen: `wireframes/` owns structure and copy, it is never painted, and the generators
  that would rewrite it are the ones `CLAUDE.md` forbids running because the voice rewrite was
  applied to the HTML by hand and never back-ported. **Every finding in those 34 bodies would be a
  finding we have already forbidden ourselves to act on**, and gate 14 was deliberately narrowed
  away from that stylesheet in step 7e for exactly this reason. Reading it would produce a list
  whose only possible next line is "not fixed, by rule".

The distinction worth keeping is between a surface nobody has read and a surface nobody may act on.
The first is a risk. The second is a boundary, and writing it down as an open item makes the
boundary look like neglect. Three rows of that table stay open with a stage against each; these two
stop being rows.

---

## 2026-08-02 - The audit thread closes with a gate, and the defect it found gets fixed behind it

Two things in one day, in that order on purpose: the gate first, on a clean base, then the product
change so the new gate is what checks it.

- **Eight components stayed short, and none of the eight is a thin stand.** Four own a page-level
  plate (`catnav`, `feed`, `event-detail`, `toast`) so on a screen the whole page is their
  descendant; one owns a tab PANEL (`tabs`), so a profile tab holds a card gallery; two carry two
  components on one element (`dialog` with `hiw-dialog`, and with the bet sheet); and two are `.pos`
  used as a generic plate. Eleven entries in `_levels.SPECIMEN_DEBT`, each a line with its reason.
- **Every entry says it is a DEBT and what closes it.** Without that sentence the list reads as
  configuration in six months, and a page plate living inside a component file becomes a legitimate
  arrangement rather than something nine of these eleven lines name a backlog item for. Closing means
  splitting the component, never widening the line. A part of `*` is used only where the cause is a
  CONTAINER, because there the contents churn with every screen and today's list is noise; a named
  part is used where the cause is one element or one class in the wrong file, because there a new
  name is a new fact.
- **Gate 24 is the comparison the audit already made, narrowed.** What a component contains in its
  stand against what it contains on the 105 painted screens, both from one function, minus the
  eleven. It fails at the moment a component gains a case nobody stages, which is the moment its
  level stops being computed and becomes a guess held up by a floor. One second, 105 documents.
- **Its second half is the one that matters, and it is the reason the list can be trusted.** An
  exception list that can be quietly extended is not part of a gate, it is the switch that turns one
  off: the cheapest way past the first check would always be one more line. So an entry covering no
  real difference fails just as loudly. Proved in three directions rather than one: gutting the
  loading scene out of the card stand turned the first check red and named `card contains skeleton`;
  restoring it turned it green; two fictitious exceptions, one wildcard on a component with no gap
  and one named pair that exists nowhere, turned the second red and named both.
- **Six declarations now, and a reader is told they exist.** `NOT_A_COMPONENT` 3, `SHARED` 5,
  `MODIFIER` 1, `RAISE` 13, `ORDER_BREAK` 4, `SPECIMEN_DEBT` 11. Most of what this system says about
  itself is computed, and the part that is not is now in one table in
  `ui-kit/docs/architecture.md`, with what each is for and who closes it. Someone surprised by a
  level or an `@import` position should find the surprise declared.
- **Then item 20, and the fix had to be css.** 52 of 482 skeleton marks drew at zero size on five
  loading screens. The tempting fix is the markup, and it is closed to us: a painted screen has a
  grey twin frozen since stage 04, and gate 18 compares the two trees inside `<main>`. So
  `<span class="sk-line">` stays a span and eight lines of BASE rules give it a box, `display` first
  because it is the property that decides whether height and width mean anything. They win nothing:
  every scoped rule below reaches the same element with more classes, so a card mark and a position
  mark keep the treatment they had.
- **Measured on the 19 screens that carry a mark, three widths.** Only `.sk-*` selectors were added,
  so only those 19 could move, and that is an argument rather than a sample. Fourteen came out
  identical to the property. The five that changed are the five the item named: on the feed screens
  exactly 12 elements each, changing `display`, `width` and the box and nothing else; on the two
  detail screens the 8 bars gained height, margin and a fill, and 176 more boxes moved down because
  a bar that was 601x0 is now 601x8. **0 of 482 marks now render at zero.**

---

## 2026-08-02 - A state is not a component, and five stands were showing less than the product ships

The specimen audit of the day before compared what each component contains in its stand against what
it contains on the 105 painted screens, using one reading for both. Eleven components came out
short. This entry is what was done about them.

- **The ownership map knew components and did not know states.** `.skeleton` is a subject in
  `position.css` (`.app-case .pos.skeleton{gap:...}`) and only ever an ancestor in `skeleton.css`
  (`.card.skeleton .sk-thumb`), so "fewest ancestors" handed the word to `position`. Both rules are
  correct where they stand. What was wrong is that a state word had to be given to somebody at all:
  every `<article class="card skeleton">` on nineteen loading screens then read as a POSITION root,
  and position came out containing card, account, event-detail and hiw-dialog. Four phantom edges
  from one misplaced word. Fixed in the map, not in the css: `_levels.MODIFIER`, one entry with its
  reason, skipped by the reader in **both** directions, because skipping it only at the root leaves
  the same phantom one element higher (the feed holds the card, so the feed would then contain
  position). Stage 09 brings hover, focus-visible and disabled, which are the same species.
- **It was checked for company before it was declared.** A sweep over all three trees asked which
  classes stand as a second class on another component's element: 20 in the painted screens, 16 in
  the specimens, 18 in the grey tree, the same list every time. Nineteen of the twenty are something
  else, and the distinction is what the word NAMES. `.tr-ic` and `.prov-x` are a component's own
  decoration of a shared atom; `.lang-menu` on `.filter-menu` is the footer skinning the filter
  dropdown; `.hiw-dialog` beside `.app-dialog` is two components on one element (item 16);
  `.rp-inner`, `.ed-tabs` and `.bet-sheet` are classes in the wrong file (item 17). The two the
  guess had named, `.scrolled` and `.resolved`, were neither: `.scrolled` is never a subject in any
  file, so the map has never held it and the reader has never seen it, and `.resolved` does not
  exist (the class is `.resolved-panel`, and that is item 17). One entry, and the mechanism is now
  there for the five that Stage 09 will bring.
- **The five thin stands were filled from the screens, not from the kit.** `kit.html` is frozen
  provenance and it stages an earlier product: its skeleton card is missing a line, its detail plate
  is a `div` where the product ships an `article` and carries three sections the product's card does
  not. So the blocks were copied out of `ui-visual/event-feed-loading.html`, `event-detail.html`,
  `active-bets-loading.html`, `event-detail-{multi,loading,resolved}.html` and `win.html`, each
  named at its block in `specimens.extra.html`. Every one keeps the real ancestor chain above the
  component's own root and adds nothing around it: a reconcile box outside the dialog is a grey
  rectangle, because three of the four rules that draw it are scoped under `.app-case`,
  `.outcome-dialog` and `.win-dialog`.
- **Three cycles appeared, and a cycle is not a defect in the reading.** `card` holds `.ed-head`
  because the detail page's header IS a card, and `event-detail` holds the card: both halves are in
  the markup. `betpanel` holds `event-detail` only through `.rp-inner`, and `notice` holds `dialog`
  only through `.fine`. All three were declared in `ORDER_BREAK`, which drops an edge for ORDERING
  and keeps it for the level, with the direction decided by which file restyles the other's insides.
  Two of the three name a backlog item as their reason, which is the point of writing the reason
  down: the declaration says how long it should live.
- **One level moved, and one line of `index.css` moved with it.** `notice` L2 -> L3, because `.fine`
  is attributed to `dialog`. `notice.css` therefore sorts into the organisms and moves from #17 to
  #23, behind `cookie-consent`, `bottomnav`, `hiw-dialog`, `hero`, `comments` and `catnav`. None of
  those six writes a selector `notice.css` also writes, and none of them has a rule that reaches a
  class `notice` owns, so the move is inert by reading. It was measured anyway, the way the cascade
  reorder was: 8 screens carrying a notice, three widths, 35 computed properties and the box per
  element. **0 of 16,662 elements changed.** Whether `.fine` should belong to `dialog` at all is a
  new question and is backlog item 19.
- **The floors were revised mechanically, one at a time.** Each of the fourteen `RAISE` entries was
  removed and the whole level table recomputed: thirteen changed an answer, one did not. `footer`
  holds a language menu and a trust bar, so the arithmetic reaches L3 without help, and its floor
  had been carrying nothing. Deleted, with the reason in its place. `hiw-dialog` keeps its floor and
  gets a new reason: the old one said the frame is not a descendant, and the markup says otherwise.
  It is backlog item 18 now, and the only one of the thirteen that a split would remove.
- **A generated file was corrected in the wrong copy, and re-running the generator proved it.** The
  dialog merge had removed the dangling `signin` reference from `specimens/index.json`, which is
  OUTPUT. `specimens.map.json`, which is the source, still said `"component": "signin"`, so the
  first extractor run after the merge brought the deleted component straight back and gate 8 failed.
  Fixed at the source, with the mistake written into the entry's note.
- **README said 36 components and broke them down into 34.** Both numbers were right and the
  sentence was not: 36 is every component file, 34 is how many are COMPOSED, because `base` and
  `course-chrome` are the substrate a screen stands on and a substrate has no level. It is written
  by `_fill_inventory.py` from `_levels.py` now, between two markers, and gate 2 fails when the span
  goes stale. A generated span is only single sourced while something fails when it drifts; the
  gate was proved by breaking the number and watching it go red.

---

## 2026-08-02 - Two dialog skins were never components, and the merge risk was one line of the cascade

`signin.css` held 2 rules. `outcome-dialog.css` held 2. The outcome dialog is made of 26 rules and
**24 of them were already inside `dialog.css`**, along with 3 for `.signin-dialog`, 3 for
`.bet-sheet`, 2 for `.win-dialog` and 1 for `.loss-dialog`: 33 of that file's 59 rules were about a
variant. The merge had already happened in the css and only the file boundary pretended otherwise.

- **The test was anatomy, and anatomy was read from the DOM.** Zone for zone the shared sheet, the
  sign-in sheet and the win overlay are the same object: a top band carrying the title, a body, and
  nothing else. What differs is what stands in a zone (an h1 and a link instead of an h2 and a
  sub-line) and a width, and a width is a value. **Nobody in the family has an action row**, which
  was a claim on the record until the markup was read: the confirm button sits inside the body in
  every one of them, and an earlier reading had scored the how-it-works dialog as different for
  losing a row that does not exist. A selector says who STYLES a thing; only the DOM says what it is
  MADE OF, and the first pass had asked the css.
- **The containment graph said the same thing independently.** `outcome-dialog` CONTAINS `dialog`
  and so does `signin`. A variant that contains its own base is the signature of a skin.
- **The whole risk of the move was four lines, and it was real.** `dialog.app-dialog:modal` in the
  mobile block is (0,2,1) and so is `dialog.app-dialog.signin-dialog`, so between 411px and 640px
  the two contest `max-width` at EQUAL specificity and **only source order decides**. As separate
  files these rules loaded after `dialog.css` and won. Appended to the end of `dialog.css` they
  still win; moved to the top they would lose and the sheet would go full bleed. So they are at the
  end, and the file says why on the line above them.
- **Measured, and calibrated against the failure it was looking for.** Seven screens where the family
  is actually painted, at 360, **500** and 1280, element by element on 35 computed properties plus
  the box, old tree against new: **0 of 15,585 elements changed**. Then the same four rules were put
  at the TOP of the file on purpose: the win overlay at 500px went from `[40,159,420,741]` to
  `[0,176,500,724]`, 420px inset to 500px full bleed. **At 360 and at 1280 that same break measured
  zero.** The width that could see it was the one added because the specificity tie predicted it,
  which is the argument for deriving the test from the mechanism rather than from habit. A repeat run
  on the unchanged tree moved 162 elements on `sign-in`, all of them inside the `<aside>` and none
  carrying a dialog class: the panel artifact from the cascade pass, still there, still not the
  product.
- **What it cost the system.** 41 css files to 39, 38 components to 36, 40 imports to 38, 49 stand
  pages to 47, 40 rows in `_nav.js` to 38. The two specimens do not disappear, because each variant
  still has to be shown: they re-point at `dialog` in `specimens/index.json`, and gate 8 caught the
  cross-reference left behind when only one of the two was repointed. `inventory.md` healed itself,
  because it derives the file and page cells from the classes named in each row.
- **Levels and order did not move.** `CONTAINS(dialog)` is unchanged, so `dialog` stays an organism;
  nothing holds `signin` or `outcome-dialog`, so no other level shifts. `index.css` was rewritten
  from `_levels.py --order` and gate 23 re-derives it.
- **Not merged, with the reason on the record.** `bet-sheet` has no top band, no close button and a
  `.sheet-grab` instead: a different zone set, so a different component, and the 3 rules for it
  inside `dialog.css` are now a misplacement rather than a variant. `toast` and `notice` do not merge
  either, and in both directions: the toast has a close and no actions, the push banner has actions
  and no close. `hiw-dialog` has the same anatomy and is still separate, because folding it moves 52
  rules across nine files rather than four across none, and that deserves its own measurement.

---

## 2026-08-02 - The level, the cascade order, and the panel that was grouped by the wrong question

Three artifacts had the same missing input. `components/index.css` was ordered by insertion, the
vitrine's side panel was grouped by purpose, and `ui-kit/docs/inventory.md` had no level column. All
three want one fact: what is this component made of. It is now computed once, in
**`ui-kit/_levels.py`**, and read by all three.

- **A level is arithmetic, not an opinion.** `level = 1 + the highest level of what the component
  CONTAINS`, ceiling 3, so a dialog holding a form stays an organism instead of inventing a fourth
  level. **36 components: 6 atoms, 9 molecules, 21 organisms**, plus two that are not composed of
  anything (`base` is the page frame, `course-chrome` is the course sidebar, which the inventory had
  already said on its own row). Typing that into the markdown would have made the table a second
  source for a fact the markup answers, which is the pair step 7c closed between coverage.md and the
  css headers, so `_fill_inventory.py` writes the column and the level never has to be maintained.
- **Containment is read from the specimen DOM, and only from the DESCENDANTS of the component's own
  root.** The first cut scanned class attributes flat and returned **33 organisms out of 38**, which
  is the tell that the measurement is wrong rather than the product. A specimen wraps its subject in
  the context it needs in order to render: the YES/NO pair sits inside a card inside the grid inside
  `main.feed`. **A flat scan reads ANCESTORS as contents.** The question is what stands inside the
  element this component owns, not what the page around it is.
- **Two things arithmetic cannot see**, declared in `RAISE`, one reason each, in the shape `SHARED`
  already uses: a block whose parts are all its own classes (the hero band is four blocks and 51
  classes, none of them another component's, so containment reads zero and it looks like an atom),
  and a **screen shell**, which is an organism because of what it is (the bottom nav holds nothing
  and is still the tab bar of every screen). A floor propagates, and it only ever goes up, because an
  error downward breaks the cascade and an error upward only makes a group less homogeneous. Raising
  the YES/NO pair to a molecule is what moved the option row that holds it to an organism.
- **The cascade was loading twenty five wholes ahead of their parts.** header before button, feed
  before card, card before both of the controls it holds. The order was the order the rules had been
  layered in inside the flat kit the system was read out of. **Nothing rendered wrong**, because step
  7b deleted every pair of files that write the same selector, and that is exactly why no sweep could
  see it: **a cascade defect is invisible until the day someone adds the rule that collides**, and
  then it presents as "my override does not work" three files away from its cause. The order is now a
  topological sort of containment, and among files that no constraint separates it keeps the order
  the file already had, because the smallest reordering that satisfies the rule is the one least
  likely to move a pixel. **Gate 23** re-derives it and compares, the way gate 21 does with the
  documents: a file can be newer than its source and still be wrong.
- **One cycle had to be declared rather than resolved.** The tab strip holds the comments panel and
  the comments panel holds a segmented switcher, and every switcher in the product is written in
  `tabs.css`. A cycle has no topological order, so `ORDER_BREAK` drops that one edge with its reason.
  It is dropped **for ordering only**: the edge is real, so it still counts toward the level and
  comments stays an organism. Which is the other half of a finding already on the record - `.seg` is
  a control that lives in the tab file because that file owns every switcher, and the same is true of
  `.grid-l`, the CHART's grid line, declared in `feed.css`.
- **The panel was grouped by purpose, which is the right way to group a product and the wrong way to
  group a system.** A group named for where a thing is used answers a question the screens already
  answer, and it put a button next to a sign-in dialog because both appear in a form. Grouped by
  level it answers the question a system has instead, which is what may be built out of what, and
  reading it top to bottom is reading `index.css`. Derived from the same map, so there is no second
  list to keep in step.
- **The column had to go in the generator, and where it goes in the row is a rule too.** `Level`
  sits after `Page`. Before `CSS file` it would have broken the file exactly the way step 7c did: the
  header strip tests `cells[1] == "CSS file"`, the test would stop matching, and the header would
  grow two cells a run. The strip is now written by SHAPE rather than by counting, because the table
  shipped for a whole stage with two generated columns and a run that assumes three eats the first
  real cell of every row.
- **Verified.** Product **503 of 520 snapshots identical to the property, 0 elements changed**;
  vitrine specimens **305 of 310 identical**. The rest are the mobile sheet caught mid-rise, and they
  differ by the same amount between two snapshots of an **unchanged** tree, which is how that was
  established rather than assumed. The OWNER map does not move under the new cascade (the cascade is
  its tie-break, so a reorder could have changed which file owns a class, and therefore the levels
  themselves; measured: 0 classes change owner). Gate 23 tested by injecting drift. All generators
  reach a fixed point in one round. **Gates: 23.**
- **Measured again on the screens where the moved components are actually painted.** The first
  verification ran on the five densest product screens, and the components the reorder moved furthest
  are exactly the ones those screens do not show: a dialog is present in the markup of all 104 screens
  and closed on nearly all of them, so **a class in the markup proves nothing**. Method: two passes,
  `git show HEAD:components/index.css` against the new file, full height, 360 and 1280, first as
  full-page pixels and then element by element on 35 computed properties plus the box. Result, the
  five base screens: **10 of 10 pairs pixel identical**, and `active-bets` **0 of 624 elements
  changed** at both widths. Result, nine state screens chosen so that each of the eight most-moved
  components is *painted* on at least one of them (`sign-in` and `win` for the dialog skin,
  `how-it-works` for the how-it-works dialog, `win` for the outcome dialog, `event-feed-loading` for
  the skeleton, `deposit` and `event-detail-bet-reconcile` for the notice family, `toasts`,
  `event-feed-empty` for the state block, plus `cookie-consent`): **0 of 11,914 measured elements
  changed**. Visibility was asked of the rendered box, not of the class attribute, for the reason
  above.
- **The one difference that showed up was in the capture, not in the product.** The first pass
  reported `active-bets` at 360 differing by 7,814 pixels. Shooting the SAME file twice reproduced
  the same 7,814 in the same rectangle, and the old file then matched a later shot of the new file at
  zero, which is what turned it from a finding into an artifact. The cause: `aside.sidebar` is
  `position:fixed` and is assembled by a run-time script, and a full-page capture paints a fixed
  element once, so a frame taken mid-build lands the panel half assembled. The cure is a **600 ms
  settle after `document.fonts.ready`**, applied identically to both passes. Written here because the
  next run needs to know it; the twenty screenshots were deleted, since every pair was byte identical
  and a picture proves nothing a row of numbers does not.

---

## 2026-07-28 - Stage 09, step 9: one panel, and the region no gate could see into

Started as a question about looks, why the two side panels look and work differently, and the answer
was not in the stylesheet: they are painted by one file and share every class name. **Twenty
findings, all closed.** Full record in `ui-kit/docs/architecture.md`, "What step 9 settled".

- **A gate that masks a region cannot see into it.** Gate 1 masks the `<aside>` when it asks whether
  a painted screen moved, correctly, because the panel is chrome and not the screen, and that made
  the panel the one thing nothing read. **Forty screens marked the wrong page as "you are here":**
  every category page and every feed state said `Event Feed -> success`. The cause is the shape this
  repo keeps meeting, `_apply_theme.py` and `_gen_category.py` build a screen from the finished
  Event Feed and swap the regions that differ, so **a new screen arrives carrying the shell's idea
  of where it is** and nobody re-ran `_resync_sidebar.py` after step 8. **Gate 22** is four checks:
  every screen marks its own file, every panel is what its generator would write today, every stand
  page names itself against the registry, and a page off the tree is still linked.
- **The thing that navigates was drawn quieter than the thing that does not.** A family name was a
  `.sidebar-page-link` with no href (13px, hover highlight, pointer cursor, no destination, 14 per
  screen on 105 screens) and the screen it named was a quiet nested row; in the vitrine those two
  classes mean the opposite. One vocabulary now: a **label** names a run of rows and opens nothing
  (`.sidebar-divider`, `.sub` when nested; `.sidebar-sub-head` deleted, and it had been drawn HEAVIER
  than the label above it, so depth read backwards), a **row** that opens a page is a link, the page
  you are **on** is `.active` at either level in one colour, and the group you are **in** is marked
  on its label, which the vitrine did not have at all.
- **Quiet is a colour, not an opacity.** Both labels, the note and a planned stage were dimmed with
  `opacity`, and opacity fades text INTO its background: `--chrome-muted` is 5.03:1 on the panel and
  the same value at `opacity:.55` is **2.37:1**. Five places under AA for as long as the panel has
  existed, and **no sweep this repo has run could see them, because they all read
  `getComputedStyle().color`, which does not carry opacity.** The step-6b lesson one level deeper: a
  checker that reads the computed colour is still not reading the rendered one.
- **One behaviour, two machines, one string.** Marking the row and never showing it is most of the
  way to not marking it (4066px of tree in a 900px panel; on `toasts.html` the brass row sat 3813px
  down). Both panels reveal it on load from one string in `ui-visual/_panel_reveal.py`.
  **`scrollTop`, not `scrollIntoView`**: the panel is `position:fixed` and asking an element inside a
  fixed box to scroll itself into view lets the browser scroll THE PAGE. The script lives inside the
  `<aside>`, which is the span gate 1 masks, so a panel can gain behaviour without 105 screens
  reading as product changes.
- **One component, seven descriptions.** The 28 course pages never linked the system file: 41 to 43
  rules each in **five distinct copies**, plus a sixth block injected by `_unify_sidebar.py` to force
  a violet palette. That is also why the four `.planned` rules had no markup in any tree
  `course-chrome.css` reaches: **the only panel with a planned row was the one it did not paint.**
  `_course_chrome.py` deletes the copies and the override, renames the drawer to the system's classes
  (its script addresses the elements by id, so only the paint moves) and links `fonts.css`,
  `tokens.css`, `course-chrome.css` last in `<head>`. `_unify_sidebar.py` deleted. Two things
  checked and not assumed: the course pages declare 14 variables against tokens.css's 348 and the
  sets **do not intersect at all**, so linking tokens cannot repaint their content; and the z ladder
  had to move together, because their 199/200/201 against the system's 8/9/10 would have opened the
  panel behind its own scrim.
- **A component that changes with the page it stands on is not a component**, so `.sidebar` names its
  own font instead of inheriting Inter on a course page.
- **A comment is not a rule, and a quotation is not an element.** Writing those comments broke the
  vitrine's own coverage table and exposed two defects in it: `parse_component` cut only the header
  comment, so `.css` and `.color` sat in the deletion-candidate list harvested out of the words
  "components/index.css" and "Colour goes through a role", and the kit bucket read the specimens and
  `kit.html` but not the 46 stand pages, so a class carried only by the vitrine's chrome fell through
  every bucket. **Deletion candidates: 28 to 2**, on a list step 7 acted on.
- Also: `.ck-note-link` moved from `ui-kit/_page.css` into `.sidebar-note a`, because a link in the
  note is the panel's own and it had been rendering in the browser's blue everywhere the vitrine's
  stylesheet is not loaded; a planned stage is a `<span>`; the tree is a named `<nav>` in all three
  panels; the note's mention of ui-kit is a link, so the way in exists in both directions, with no
  new copy written; `resync_sidebar.py` stops writing panel css, which it had been inserting into the
  page's own sheet reading `var(--accent)`, that page's violet; and `mark_group` lives in one file
  and is imported by the other, because for one turn the two tools each had their own idea of the
  mark and undid each other for ever.
- **One checker's own defect, recorded:** the light-theme sweep reported 105 failures at 1.12:1 and
  they were the `<script>` the reveal added inside the `<aside>`, counted as text. On graphite a
  script inherits light ink and passes; the moment the ground inverts it reads dark on dark. **A
  checker with a missing guard fails in one theme and looks exactly like a finding.**
- **Verified:** the panel in both trees and both themes, 308 loads, **18028 text pairs, 0 below AA**
  with opacity composited, 0 browser-blue, 0 overflow, 0 page errors, on a sweep calibrated first
  against a pair whose answer is known; the reveal on 153 panels at two viewport heights, **0 with
  the mark out of view, 0 documents scrolled**; the course pages, **795 text pairs, 0 below AA, 0
  dead anchors, 0 violet left**, one shape on all 28; their own content compared element by element
  against a worktree of HEAD, **28 of 28 identical**; **348 pages, 35773 internal links, 0 broken**.
  Gate 22 tested by injecting each of its four kinds of drift; all six generators reach a fixed point
  together over three rounds. **Gates: 22.**

### Where the audit passes stopped (written 2026-07-28)

Nine passes ran over this stage (7, 7b, 7c, 7d, 7e, 7f, 8, 8b, 9), yielding 34, 14, 24, 11, 10, 8,
15, 9 and 20 findings. **That sequence does not decay, and that is the argument for stopping rather
than running a tenth.** A pass re-reading a region it had already read would tail off; each of these
instead found a region nobody had read. Yield tracked unread surface, not effort, and the surfaces
with nothing pointed at them are now countable. That list moved to [`backlog.md`](./backlog.md).

Not a defect list: no entry is a known bug, each is a place a bug would be invisible. And not a
claim that accessibility is undone, which was checked before the table was written because a large
hole there would have changed the answer: **0 buttons without an accessible name** across 105
screens, every `<img>` with `alt`, native `<dialog>` supplying `aria-modal` and inerting the page,
tab strips as radio groups that arrow keys already drive. The one real gap is the announcement, and
a toast is a state, so Stage 10 owns it.

---

## 2026-07-28 - Stage 09, step 8b: the documents, the skin, and the sheet that could not scroll

One item was on a list and two came from looking at the product. **Nine findings, all closed.** Full
record in `ui-kit/docs/architecture.md`, "What step 8b settled".

- **A document nobody can open is not documentation.** Every stage renders its reasoning
  (`ia/docs/sitemap.md` -> `ia/sitemap.html`); Stage 09 was the one that did not, and its four
  documents are 144 KB. Worse, the vitrine already LINKED one: **39 component pages pointed at
  `docs/coverage.md`**, a href into a file the browser downloads instead of drawing. They are pages of
  the vitrine now (`ui-kit/_gen_docs.py`), painted by the system they describe, with a contents rail,
  a swatch beside every colour literal and a link on every file name the vitrine has a page for.
  Generated, because these documents change every step and a hand copy is stale by the next one;
  **gate 21** re-renders in memory and compares, because a file can be newer than its source and still
  be wrong, and fails on any link into a raw `.md`. Run `_gen_component_pages.py` first: it writes
  `docs/coverage.md`. The long read also found that **a section label is not a heading** - `.tk-sec>h2`
  is small brass capitals, right over a specimen and wrong seventeen times down a page.
- **A gate that compares the body certifies the body.** Gate 19 has guarded the Sign In / Deposit fork
  since step 7f by comparing the sheet BODY, and the fork left was on the element the body hangs from:
  all 17 standalone overlay pages carried `outcome-dialog`, which is the RESULT skin (`dialog.css`
  splits the head on it and only `:not(.outcome-dialog)` gets the brass-lit plate). **The sign-in sheet
  a person actually opens had the flat result head while the same sheet on the other 75 screens had
  the lit one.** A skin is named for what the sheet IS: sign-in and deposit take the shared dialog's
  own class list, win and loss keep theirs. Computed in `_unify_dialogs.py` from the canonical dialog,
  with the family read from the page NAME, because **a rule that can only recognise its own input
  before it has run once is not idempotent**. Gate 19 compares the skin now.
- **A modal is bounded by the viewport, so it has to be able to scroll.** The user agent gives
  `dialog:modal` both `max-height` and `overflow:auto`; `dialog.app-dialog{overflow:clip}` took the
  second away. At 1280x620 the deposit sheet was cut with its **Add funds** button 116px past the edge
  and nothing to scroll; the how-it-works sheet was unreachable below 900px of viewport at any width.
  This is step 7's finding read backwards: there `overflow:hidden` was wrong for making a decorative
  box a scroll container, here `overflow:clip` is wrong for stopping a box that has to be one. **Clip
  decoration, or contain content** - one question, one property. The frame clips and the BODY scrolls,
  so the head and the close stay put. Verified as the question a person asks: **64 sheet-and-viewport
  combinations, last control reachable in all 64.**
- **Three checkers were reading text as markup**, all surfaced by the documents: the renderer left the
  quote unescaped, so a code block quoting `<link ... href="_theme.css">` failed gates 4 and 9; gate 4
  also read a `url()` inside a `<pre>` (**text inside `<code>` or `<pre>` is a quotation, not a
  reference**, which the component pages needed too, since each ends with its own source); and gate 20
  searched the whole text for a font host, so the page explaining why the host was dropped failed the
  gate that exists because of it (**a mention is not a call** - ask a `src`/`href` attribute and an
  `@import`).
- **A colour follows the surface it stands on.** The course sidebar keeps one dark palette in both
  grounds, and `.ck-note-link` inside it read `--text-brass`, which in daylight is the dark brass for a
  pale surface: **2.39:1 in the light theme on every page of the vitrine**. One role, `--chrome-accent`.
  The vitrine's sub-AA pairs went 434 to 158, all that is left being `kit.html` (frozen) and the value
  labels drawn ON their own swatches in `tokens.html`.
- Also: `ui-kit/fonts.html` existed because step 8 taught gate 2 that fonts is not a component with a
  stand and did not teach the page generator; the `Stands on:` header of 24 component files still said
  76 screens; and `.outcome-dialog a{text-decoration:none}` had been paying for another skin's markup
  (**a link that wraps a control is not a text link**, now in `dialog.css` for both trees).
- **One measure for the page** (reported by eye at a wide window). `--container-max` is 1400 and only
  the footer obeyed it: at 1920 the content ran 1620 while the footer under it stopped at 1400. Five
  bands carried `max-width:none` from the colour pass and read the token now, so the band spans the
  window and what is inside it (header row, category strip, trust bar, content, footer) shares one
  left edge.
- **An empty box is invisible to every sweep we run.** The four category pages and two feed states had
  a 56px photograph box with no photograph, because step 7c moved the picture out of
  `.grid > .card:nth-of-type(N) .thumb` onto the element and reached the pages that exist as files,
  not the cards a generator writes. **A missing picture passes a contrast sweep, an overflow sweep and
  a link check alike**; gate 9 asks for it now. The library has one photograph per category, so what
  varies on a single-category page is the CROP of it. And **a photograph is not one declaration**: the
  port stripped `background-image` on the way into grey and let `background-position` through, which
  is the framing of a picture that is not there.
- **A control is named by what it does.** The Event Feed had two controls doing the same thing: the
  top band navigates (a category is its own indexed URL), and the chip row labelled "Filter events by
  category" was five more links to the same pages, so pressing Politics inside Trending left Trending.
  It filters in place now (`wireframes/_generators/subfilter.py`, both trees, `data-cat` read out of
  the photograph each card already carries). Three shapes came with it: **hidden is a state, not a
  style** (the attribute was set and nothing moved, because `.card{display:flex}` beats the user
  agent's `display:none` whatever the specificity, so `base.css` carries the one `!important` in
  `components/`); **a checker that reads the attribute does not read the page** (the first run
  reported success while twelve cards were on screen); and **two generators writing into one sheet
  have to know where each other's work ends**, the step-7e lesson, paid for again when `port_chrome`
  and `subfilter` rewrote the same page back and forth forever.
- **A container holds its inset at every width.** Centring the content band by turning
  `margin:var(--gutter)` into `margin:var(--gutter) auto` spent the horizontal gutter on the centring,
  so under 1400 the plate sat against the window edge. The inset is padding; above the cap the auto
  margin centres. Measured at eight widths from 1920 to 380: header, content, plate and footer on one
  x at every one, gutter 40 above 640 and 14 below.
- **Half of twelve is six.** The two bars of the close X sat at `calc(50% - 7px)`, one pixel left of
  the disc, on every close button in the product. The vertical half was right, which is what made it
  hard to see.
- **Verified:** painted **420 page loads x 2 themes, 86534 text pairs, 0 below AA, 0 overflow, 0 page
  errors**; the vitrine 196 loads in both themes, every remaining failure present at HEAD; standalone
  dialog against shared, matched by class, **0 differences that paint**. Gates 19 and 21 tested by
  injecting the drift they exist to catch. **Gates: 21.**

---

## 2026-07-28 - Stage 09, step 8: the coverage pass, and the family no gate could see

Run against the three things step 7f left open (an overlay contradicting its own convention, a font
host called before consent, a note that the trees disagreed about how many category screens exist),
and the third one turned out to be the largest hole this stage has found. **Fifteen findings, all
closed.** Full record in `ui-kit/docs/architecture.md`, "What step 8 settled".

- **A pair that does not exist is not a pair that agrees.** Gate 18 pairs the trees by FILENAME, and
  one family does not share filenames: a category page is `politics.html` in grey and
  `event-feed-politics.html` in colour. The gate skipped every unpaired page in silence, so **32 grey
  category screens sat against 4 painted ones** and the family drifted through two stages with every
  gate green. Zero drift out of zero pairs reads exactly like zero drift out of all of them. The map
  is now **`_twins.py`** at the root, one copy for six tools and the gate; it had existed in FIVE
  hand-written copies, and the four that only knew the BASE pages are why nobody noticed. Gate 18
  gained **every screen has a twin**, one declared exception (`overview.html`). The 28 missing
  screens are built by `ui-visual/_apply_theme.py`, generalized from the Event Feed's state
  generator: a category page is the same listing with one filter on it, so it is the same machine
  with a different shell, not a second generator.
- **An anchor another tool can remove is not an anchor.** `_apply_theme.py` built the stone plate by
  finding `<div class="feed-inner">` in the grey fragment, and step 7d's port unwraps plate wrappers
  on the way into grey, so the anchor had stopped matching and the next run would have shipped eight
  state pages with no plate. `_gen_category.py` had the same defect one function away and it had
  already fired: its heading substitution read `<h2 id="feedHeading">` and step 7b made that an
  `<h1>`, so one re-run put the shell's **"Trending"** on all four category pages and silenced the
  sub-category rail, which picks its list by the heading's text.
- **A category page owes its own SEO body, not the home page's.** `seo.md` section 3B lists "About
  {category} events" as the category template's fourth H2; the painted pages had inherited the feed's
  two generic sections instead, the same text on all five URLs, which section E of the same spec
  forbids. The copy is read out of the grey twin at generation time, because a generator that types a
  sentence is a second source for it.
- **A listing does not change its contents when nobody is signed in.** The logged-out category state
  was built from a grey card set drawn in Stage 05: no `.top-txt`, so no story-led "why", and YES/NO
  a logged-out person could not press, in a product whose whole inversion is that you browse and
  build a bet before the gate. And **nobody signed in has saved anything**: a pressed bookmark shipped
  on five logged-out screens in both trees, the filled brass mark meaning "this is in your
  Favorites", to a visitor whose header offers them Sign up.
- **A missing colour is a colour, on a control this time.** Every colour in `yesno.css` hung off
  `> a`, so a `.yesno` whose buttons are not wrapped in an anchor fell back to the user agent's
  `buttontext`: near black on graphite, **1.42:1**. **A side is a POSITION IN THE PAIR, not a fact
  about being wrapped in a link.**
- **A frame rule reached a dialog.** `.app-case{position:relative}` in `base.css` took back the user
  agent's `position:fixed` for `dialog:modal` on the 17 standalone overlay pages, which put the app
  frame class on the `<dialog>` itself, so the sheet scrolled off the top with the page behind it.
- **The bottom sheet came back, and it is geometry, not markup.** Under 640px an invoked dialog is
  full width on the bottom edge, top corners rounded, rising into place, head fixed and body
  scrolling; above 640px nothing changed. **`:modal`, not `[open]`**, because a standalone overlay
  page opens its dialog as the page it IS and a sheet that rises over nothing is a page that jumps on
  load, and because **an author declaration beats a UA one whatever the specificity**, so a bare
  `display:flex` would have opened every dialog on 76 screens at once. No grab handle: the grey tree
  draws one and drag-to-dismiss is not built. (This closes the step-7e note that "bottom sheet on
  mobile ships only in grey".)
- **Where a font comes from is a decision.** The three families are served from this repo now: 18
  woff2 files (latin + latin-ext, `font-display:swap`) in `assets/fonts/`, declared once in
  `components/fonts.css`. **Gate 20 is three checks**, because the defect returns three ways: a page
  re-adding the tag, a GENERATOR re-adding it to every page it writes (five had it in a template),
  and an `@font-face` naming a file nobody committed. (This closes the step-7b note that self-hosting
  was "an open decision, not a silent default".)
- **Verified:** painted 105 screens x 2 themes x {380, 1280} = **420 page loads, 86534 text pairs, 0
  below AA, 0 overflow, 0 page errors**; grey 104 x 2 widths, **0 overflow, 0 errors, 0 non-neutral
  colour** (its 1212 sub-AA pairs are the screen-tree drawer's own notes and the identical count comes
  off a worktree of the previous commit). **16770 grey + 15535 painted links, 0 broken.** The sweep's
  first cut reported 116 sub-AA pairs and 4690 overflowing elements; calibrating it on three
  known-good pages returned 0 and 438, so the overflow question is asked of the DOCUMENT now and the
  116 turned out to be real. **A measurement not checked against a known-good case is a claim, not a
  proof. Gates: 20.**

---

## 2026-07-28 - Stage 09, step 7f: one dialog, one copy, and scope as a place

Found by looking at the product instead of the build: the sign-in dialog on `ui-visual/sign-in.html`
did not look like the sign-in dialog on every other screen. **A screen can disagree with its grey
twin, and it can also disagree with its own second copy in the same tree, and only the first of those
was ever checked.** Full record in `ui-kit/docs/architecture.md`, "What step 7f settled".

- **A dialog that also has a page has two copies.** Sign In and Deposit each exist as the shared
  `<dialog>` on all 76 painted screens AND as the standalone page that IS that dialog. Stage 08
  painted the shared copy and left the standalone on the grey generator's markup, so **the page a
  person actually opens carried the wireframe placeholders, the one standing in for Google being a
  circle with a plus in it**, while the shared dialog carried the real brand marks. Four copies of
  that body existed in the repo and all four differed.
- **"The newer copy wins" would have deleted the best thing on the screen.** The standalone Deposit
  had three things the shared one had lost: a label over the payment widget, the sentence saying card
  payments are converted via Transak, and **an exit to How It Works, which is the trust affordance
  that screen exists to earn**. Merged element by element, then one markup from there
  (`ui-visual/_unify_dialogs.py`). **Gate 19** fails the build when it drifts again, in either tree,
  and checks the marks by name, because `shape()` drops `<path>` and `<circle>` and so cannot see
  that a button is drawing the wrong logo.
- **Scope is where a block may stand.** The How It Works page rendered as an unstyled document
  because every rule for the hero, the icon chips and the FAQ list began `.app-dialog.hiw-dialog`:
  the page the dialog links to as "the full guide" could not reach one of them. A rule that describes
  a BLOCK is now written unscoped; only what is about being a dialog keeps the ancestor.
- **A page is not a bigger dialog.** The page was composed, not re-marked: page text size instead of
  a sheet's 13px, sections apart instead of stacked, and the brand tile and the resolved-events count
  moved into a side column, because **a claim and its proof belong beside the argument, not after
  it**. It also gained what a page called How It Works owed a reader and did not have: how to place a
  bet. One line of copy written (Step 27 in `microcopy.md`), the rest already shipped.
- Also: the heading `Proven, not promised` had been sitting in a `<section>` **with nothing in it**,
  above three numbers in a different element; `.app-case .hiw-sec > :is(h2,h3)` from step 7c stopped
  matching the moment the heading moved, a fossil created by the fix for a fossil; and `.hiw-sec`
  joined `port_structure.RESTYLE`, because **"already styled" is the wrong question when the markup
  changed shape** and the wireframe was drawing the chip above the heading in a layout that puts it
  beside.
- **Two checkers reported their own defects**, both mine: gate 19's first cut asked for "the first
  `<dialog>` in the document" and got the shared sign-in sheet that every standalone page embeds
  first, so **a page with several of a thing has to be asked by id**; and `_unify_dialogs.py` had to
  be told that a button with no mark keeps none, since swapping a placeholder for the real logo ends
  a fork but putting a logo on a control that never had one starts a design decision.
- **Verified:** both trees at 380 and 1280, grey 0 overflow / 0 errors / 0 colour outside the
  palette, painted 0 below AA in both themes, 0 broken links either side. Gate 19 tested by injecting
  each of its three kinds of drift. **Gates: 19.**

---

## 2026-07-28 - Stage 09, step 7e: the other three regions, and a gate that certified one

Step 7d put a gate behind "wireframes/ owns structure", and that gate compared `<main>`. **A gate
that reads one region of a page certifies one region of a page**: the header, the bottom nav and the
footer stayed the one place two trees could drift with every gate green, and they had. Ten findings,
all closed, two of them the tools' own. Full record in `ui-kit/docs/architecture.md`, "What step 7e
settled".

- **The drift ran both ways, so the fix is two tools in a fixed order.** The paint got the SHAPE
  right and the STATE wrong; the grey tree got the state right and the shape wrong. Reading that as
  "one tree is behind" is what makes a one-directional port write the wrong answer into 104 files.
  **The paint owns the shape of the chrome; the grey tree owns which state it is in.**
  `ui-visual/_reconcile_chrome.py` gives the paint back three state facts, then
  `wireframes/_generators/port_chrome.py` copies the corrected shape back.
  The paint had `aria-current="page"` on the **Events** slot of all 76 painted screens whatever
  screen it was (the grey tree marks 54 Events / 9 My Bets / 3 Favorites / 6 Portfolio / 15 none, and
  the painted Wallet screen was announcing "Events, current page"); a logged-in header over a bottom
  nav pointing home at `event-feed-logged-out.html` on ten screens, one chrome disagreeing with
  itself about whether anybody is signed in; and three unread notifications in the dropdown of the
  three screens whose whole subject is that a new user has nothing yet. The grey tree had no
  `.cat-condensed` at all (the category strip that slides into the sticky header, a whole navigation
  control, on 68 painted screens and 0 grey), the footer trust block as three bare sentences, and a
  `<span>` pretending to be the deposit amount field.
- **An auth variant was not a fact to read, it was a decision to make.** Ten screens disagreed and
  neither tree is a copy of the other, so each is answered by a reason, written once: `how-it-works`
  + `public-profile` x4 logged OUT (documented as pre-auth since Stage 08), `cookie-consent` because
  a consent banner IS a first visit, `maintenance` because the app is down and there is no session to
  read; `404`, `500`, `toasts` logged IN, because showing a signed-in person Sign in / Sign up turns
  "this page is missing" into "you were logged out".
- **A port copies markup, and a href IS markup.** The category pages are `event-feed-politics.html`
  in colour and `politics.html` in grey, and step 7d carried the painted hrefs across with the
  markup: **110 links in the grey tree pointed at files that do not exist there**, while the link
  check run at the time counted links instead of resolving targets.
- **A missing colour is a colour**, twice, and both are the step-6b theme lesson from the other side:
  a checker that reads the source cannot see a value the browser supplies. The grey sheet styles a
  link in fourteen scoped places and never as a bare element, so every `<a>` outside them rendered in
  the user agent's `#0000EE`: **992 computed colour values** in a tree whose contract opens with
  "neutral greys only" and whose source has 0 non-neutral hex. And `fill`/`stroke` are not in the
  port's KEEP list, so **the feed hero chart has been a solid black rectangle since step 7d**, since
  an SVG with no fill is black.
- **Where a rule may reach, part two.** Gate 14 counted `wireframes/*.html` as markup for
  `components/`, which cannot apply to it (the grey tree has its own inline css and never links
  `index.css`). Four rules lived on that mistake and are deleted. **A class carried only by the tree a
  stylesheet cannot see is a class it does not have.**
- **Two boundaries added, six now** (`wireframes/_conventions.md`): the `TBD` chip, because a
  wireframe is obliged to mark an unbuilt destination and a product must not show a user the
  bookkeeping; and the page behind an invoked overlay, which convention 5 has specified since the
  wireframes were built. That sixth one is **checked rather than skipped**: grey must carry no chrome
  on those 17 screens and the paint must carry all of it.
- **Two tool bugs, one shape.** An idempotent generator has to be idempotent about whitespace: **the
  removal has to be the exact inverse of the insertion**, and getting it approximately right cost 74
  pages on one re-run and 13 on the next. And a painted overlay page carries four dialogs with the
  shared ones first, so "the first `.sheet-body`" is the sign-in provider list on all 17: the port
  wrote sign-in buttons into the grey Win, Loss and Deposit wireframes, caught by eye in a
  screenshot. A screen's own overlay has an id, and the tool now checks both trees give the sheet the
  same `aria-label` before copying. Also: two generators writing into one `<style>` have to know
  where each other's work ends, or one silently deletes the other (72 pages).
- **Not fixed, on purpose:** the paint made the invoked overlay a centred modal at BOTH breakpoints,
  so "bottom sheet on mobile" ships only in grey. A product decision, recorded beside the convention
  it contradicts. *(Closed in step 8: the sheet came back as geometry.)*
- **Verified:** grey 208 page loads at 380 and 1280 (**0 overflow, 0 page errors, 992 colour leaks ->
  0**); painted 308 page loads across both themes (**61956 text pairs, 0 below AA, 0 overflow**);
  **16597 grey links, 110 broken -> 0**. Gate 18 tested by injecting drift into each of the five
  compared regions in turn. All five tools reach their fixed point in one run. **Gates: 18.**

---

## 2026-07-28 - Stage 09, step 7d: the readiness pass, and the rule that had no gate

Run against the course's own "done when" list rather than as a defect hunt, which is why it found a
different kind of defect. **Eleven findings, nine closed, two of them my own measurement error.**
Full record in `ui-kit/docs/architecture.md`, "What step 7d settled".

- **A rule with no gate behind it is a preference.** `wireframes/` owns structure and copy has been
  written here since Stage 08 and nothing checked it, so Stage 08 **redesigned the Event Detail while
  painting it** and the redesign never came back: an AMM market panel with a price-by-size table, a
  chart rebuilt as head / plot / axis / range, a rules-and-context tab split, a share-and-save
  cluster, an odds bar, and a real `<input>` where the grey tree had a `<span>` pretending to be a
  field. 55 of 72 twinned `<main>` elements differed, Event Detail by 222 elements. Ported back by
  `wireframes/_generators/port_structure.py` (idempotent, reads the painted twin, never writes to
  `ui-visual/`), which derives the grey-box rules from `components/` by keeping what a rule PLACES
  and dropping every colour: **a grey box is the painted component with its finish scraped off.**
  **Gate 18** fails the build when the two trees disagree; the four differences that ARE the
  boundary are declared in `wireframes/_conventions.md` (plate wrappers, icon mechanism, photograph,
  and chart data, because a wireframe draws its data and a product computes it).
- **The copy inventory was not the source of truth for a whole stage.** 43 strings the product had
  been shipping since Stage 08 had no row in `voice/docs/microcopy.md`, including every label of the
  market panel and the line that keeps the context tab from being read as the resolution rule. Logged
  as Step 24. Two lines were opened as defects and closed as correct, and the first is the useful
  one: `Closes: Sep 1, 2027` looks like the product's only stray colon and the colon is a
  **delimiter** the feed script splits the meta row on. **A style rule that would break a script is a
  style rule with a missing fact in it.**
- **Four bugs in my own generator, each one a rule.** Splitting a selector list on commas cuts
  `:is(h2,h3)` in half, and a browser drops an unparseable rule AND everything after it in the sheet
  (the symptom was a chart axis rendering as running text). Deleting `@media` before reading a file
  deletes the layout, so the feed came out 14px wider than the phone it was drawn for. "Already
  styled" is the wrong question when the markup moved. A selector naming a scope the target tree does
  not have can never match.
- **A photograph travels two ways.** `background-image` was stripped and `<img>` was not, so four
  pictures entered a tree with zero image elements across 104 pages, one of them 1400px wide.
- **Two findings were my own measurement error**, recorded because a false positive costs the same
  attention as a real one: a case-sensitive scan called six documented token coincidences
  undocumented. **A checker that has not been run against a case it should pass is not a checker.**
- **Gate 17**, the other direction of gate 3: 14 marks stood on screens and were on no sheet,
  including the chevron at 176 uses and the three sign-in brand marks, because step 7c collected
  icons with a regex wanting `class="ic"` as the first attribute. An `<svg>` on a screen is either a
  MARK or a drawing of DATA; there are two drawings. One checkmark drawn two ways is now drawn one.
- Also: the eleven `--z-*` tokens are now a section of `tokens.html`, drawn as a stack written
  **highest first** so only the tokens can produce the right picture; the field gained a rendered
  state set (`input-states`), and its first cut on the bare canvas rendered four white boxes because
  every rule in `input.css` is scoped under `dialog.app-dialog`; the roadmap sidebar was true in
  `LAYOUT` and false on 21 pages that keep their own copy, fixed by `_resync_roadmap.py`; and
  `.chart-wrap` / `.chart-cap` died the moment the port took the last markup they could match, which
  is a fossil pair working as intended.
- **Verified:** 104 grey pages at 380 and 1280, **0 horizontal overflow, 0 page errors, 0 colour
  outside the wireframe palette**, against the same sweep run on a worktree of the previous commit.
  Structural parity 55 of 55. Gate 18 was tested by injecting drift and confirming it fails.
  **Gates: 18.** (The colour claim was read out of the SOURCE and step 7e re-read it out of the
  BROWSER, where it was false; see the step-7e entry.)

---

## 2026-07-28 - Stage 09, step 7c: the third audit, on a build where every gate was green

Run against `components/`, `ui-kit/` and all 77 painted screens, plus `/impeccable audit` (16/20
Good, no AI tells). **24 findings, 23 closed, 1 recorded as a decision.** Full record with the
reasoning in `ui-kit/docs/architecture.md`, "What step 7c settled". What changed a rule:

- **A generator that is not idempotent on all of its row kinds is not idempotent.**
  `_fill_inventory.py` stripped its own columns from data rows and not from headers, so the header
  grew two cells a run: seven runs later every table in `inventory.md` had a 21-cell header over
  9-cell rows and none of them rendered.
- **A class a file mentions is not a class it owns.** `coverage.md` said 76 screens for 34 of 36
  components, because `market.css` styles `.market-title .ic` and `.ic` is on every screen. Ownership
  is now the file that styles a class with the fewest ancestors (ties to cascade order) plus a
  five-word hand-checked SHARED list. The same map writes the `Classes:` and `Stands on:` lines in
  each css header, which were prose someone typed once and had been telling the truth while
  coverage.md said 76. **Two artifacts of one system disagreeing is the defect; one computation
  feeding both is the fix.**
- **A distance is not a measurement.** The rule was written in step 6 and 57 declarations broke it,
  because the measurement scale shipped with two steps (56, 72) and the product needs twelve. A rule
  with no scale behind it cannot be followed. `--size-2 .. --size-72` now, and **gate 12 fails on a
  `--space-*` step in a width, height or flex basis**, which the raw-value check cannot see.
- **Removing an `!important` means ending the argument, not deleting the word.** `.grid` carried one,
  and dropping it let `.cat-main .grid` win: the category pages would have changed their column
  track. Four rules above it were already dead (three breakpoints losing on source order, the
  category variant losing to the shout). Deleting the four made the shout removable without moving a
  card.
- **A rule applied to two files is not applied.** Step 7 moved touch targets to `pointer:coarse` and
  reached `catnav` and `header`; six components still bound 44px to `max-width:640px`, so a touch
  tablet above 640px got the 36px control, the exact device the rule was written for. Measured after:
  coarse pointer at 380 and at 1280, every control 44px; fine pointer 36, which clears 2.5.8.
- **Structure is owned by `wireframes/`, so fixing only the paint leaves the owner wrong.** Step 7b
  reported "heading skips across the painted tree: 0" and the grey tree, which owns structure, still
  had an h1-to-h3 jump on 46 pages and no `<h1>` on 19. **Gate 15 reads both trees.** Footer columns
  went h3 to h2 in both; the Event Detail column heads went h4 to h3, which made them match the
  `.ed-section` label rule, so that rule became a CHILD selector (**a section label is the section's
  own heading, not any heading inside it**); the 17 dialog-host screens took the `<h1>` from the
  heading their own dialog already carries, so no copy was invented. The two Event Detail loading
  skeletons keep none on purpose and gate 15 names them.
- **A UI string is not a style hook.** `[aria-label="Track record"]` carried seven rules, so the
  profile reputation grid hung off an English phrase owned by `voice/`. Now `.pos-record`.
  `[aria-current="page"]` stays: a state attribute is a state.
- **A promise made component by component is not made.** 14 files carried the identical
  `:focus-visible` rule, 24 did not, and there was no default. One rule in `base.css`, one new role
  (`--focus-ring`, split from `--text-brass`), three exceptions that say why.
- **Where the system layer may reach.** `components/` held 24 `url(../ui-visual/assets/...)`: the
  system depended on the product's screen folder. Assets are `assets/` at the root now. Sixteen of
  those were worse than a path: `.grid > .card:nth-of-type(1..12) .thumb` encoded WHICH feed card
  shows which photograph, and the event photograph belongs on the element by this file's own rule.
- Also: three stale comments in `tokens.css` (a note that outlived the defect it described, a pointer
  at a primitive merged away in step 6, a role promising a difference it never had, deleted); 12 of
  the 27 same-value role groups now say so; motion moved onto the declared duration scale (21 raw
  timings, none of which was a step); the vitrine's `_page.css` dropped 93 frozen Vault hex values;
  **`icons.html` gained the 29 icons the product DRAWS inline** beside the 15 it references from the
  sprite, because a vitrine that documents one of two mechanisms describes the smaller one; every
  stand page gained a `<main>` landmark; and gate 9's "nothing loads the flat kit" was repointed,
  since `kit.css` had already been deleted when it was written and it could not fail.
- **Gate 16 exists because this pass shipped a broken declaration.** A note appended to a token
  without its comment markers put bare prose inside `:root`; the browser dropped every declaration
  after it and the NO side of the outcome palette went transparent on 28 screens. Fifteen gates saw
  nothing; a 380-page snapshot did. Gate 16 walks every block in `components/` and fails on anything
  inside it that is not a declaration.
- **Recorded as a decision, not fixed:** 20 declarations build a colour with `color-mix(in oklab,
  var(--color-action) N%, ...)` at 16 different percentages, an undeclared second alpha ladder beside
  the declared `--brass-a*` one. Gate 13 is satisfied (all of them read a role). Which steps that
  ladder should have is a states question, and rounding them now would move hover and selected states
  for the legibility of the file rather than of the product. *(Open; see backlog.md.)*
- **Verified:** both trees, 5 widths, before and after, compared by what the browser reports as
  visible. 380 product snapshots, **0 with a different visible element count**; what moved was the
  asset URLs (same files) and two chart polylines caught mid-transition. 175 vitrine pages changed
  element count, all of them the corrected screen lists and the new icon section. Target size
  measured, not reasoned about: coarse pointer 44px at 380 and at 1280, fine pointer 36px. Then the
  whole product in both themes at 380 and 1280: **54774 text pairs, 0 below AA, 0 page errors, 0
  horizontal overflow.** Two earlier runs of that sweep were wrong (950 failures that were gradient
  buttons the checker could not read, then 405 that were a theme swap measured mid-transition):
  **a measurement not checked against a known-good case is a claim, not a proof.** **Gates: 16.**

---

## 2026-07-27 - Stage 09, step 7: the deletion pass, the defect table, the finish

Audited `components/` + `ui-kit/` + all 77 painted screens against the step-7 checklist and
`/impeccable audit` (16/20 Good). **34 findings, all closed.** The ones that changed a rule and not
just a line:

- **`overflow:hidden` makes a box scrollable, it only hides the bar.** Thirteen stones clip a
  decorative pseudo; one was actually scrolled (`.sheet-head`, `scrollLeft:52`), which dragged the
  win overlay heading out of its box and clipped it to "u were right" in both themes on 4 screens.
  All thirteen are `overflow:clip` now, which creates no scroll container. Sweep: 0 scrolled.
- **Target size follows the POINTER, not the viewport.** 44px was bound to `max-width:640px`, so a
  touch laptop got 36px. Now `@media(pointer:coarse)`; a fine pointer keeps 36, which clears
  2.5.8 (24x24). The card bookmark was 16x16 (fails both bars) and now carries a 44px box with a
  negative margin, so the target grew and not one pixel moved.
- **Reduced motion, once, in `base.css`** (3 of 23 components had a block; a promise is not made
  component by component).
- **A candidate is not an outcome:** the multi-outcome series drew line 1 in the YES green and
  line 3 in the lit brand brass. Green, red and gold are reserved; the series moved into the arc
  they leave free (cyan 187 -> magenta 328 + one neutral), all five >= 4.5:1 in both themes.
- **Two roles may share a value** (27 groups do): a role is a reason, not a value. The rule is
  written above section 2 and the coincidences are declared where they happen.
- **A third copy is a fork:** `shell.html` held its own hand-kept header next to `header.html` and
  76 screens; it composes the specimens now and holds no markup.
- Also: `.opt-row.sel` side-stripe -> tint (an impeccable absolute ban), 13px/19px icons onto the
  scale (`--icon-12` added), `--brass-800` orphan deleted with its gate exception, `.uv-bar` +
  its wireframe-era grey gone from 76 screens, the Favorites category bar restored from the grey
  twin (and its now-duplicate Category dropdown dropped), `<img>` given `width`/`height`/`lazy`.
- **Deleted:** `ui-visual/_theme.css` + `_theme-vault.css` (132 KB, unloaded since step 5) and the
  empty `tokens-components/`.
- **Living documents:** `inventory.md` gained **CSS file** and **Page** columns, filled for all 87
  component rows by `ui-kit/_fill_inventory.py` (class-matched against each file's `Classes:`
  header, so it stays true when a class moves); `coverage.md` records the decision on the six
  kit-only classes (all six stay, with the reason); `architecture.md` gained "What step 7 settled";
  `DESIGN.md` gained the two-level token section + the both-theme contrast table; `STRUCTURE.md`,
  `README.md` and the roadmap sidebar mark 08 and 09 Done.

---

## 2026-07-27 - Stage 09, step 7b: the second audit, and what a passing build hides

Run against `components/` and every painted screen on the premise that a system passing its own
gates is where the interesting defects live. **14 findings, all closed.** Contrast was already clean
in both themes and stayed clean; what the gates could not see was where the styling lived.

- **One element, one rule.** Step 1 read the styling off the painted product, and the product had
  TWO stylesheets on it: the grey-box skeleton written inline by the wireframe generator, and the
  Vault theme loaded after it. The extraction concatenated them, so **116 selectors were written
  twice and 200 declarations in the first layer rendered nowhere** (`loadmore.css` described one
  button twice over, nine properties apart). Deleted by `ui-kit/_unfork.py`, whose argument is that
  `.app-case S` is S plus one class and therefore always wins. **Five exceptions, measured not
  assumed:** the footer language menu and the shared `<dialog>`s live OUTSIDE `.app-case` (a dialog
  is appended at the end of the body, so it is a sibling), and for those the unprefixed rule is the
  shipped one. The first cut deduced instead of measuring, deleted the footer menu's padding, and
  the diff caught it in one run.
- **An attribute is a rule.** Gate 9 asked about `<style>` blocks, gate 12 looked inside
  `components/`, so **110 style attributes on 30 screens** were the one place neither looked: type,
  geometry (`width:72px` beside an existing `--size-72`), layout variants, and twelve places where a
  component was undone on the element. Half were already dead. Two explain an `!important`:
  `profile.css` and `state-block.css` were shouting to beat an inline style, and both stopped.
  **An `!important` is usually a fossil of something no longer there.** Gate 9 reads attributes now
  (`ui-visual/_destyle.py`).
- **Hidden is not gone.** Every painted screen carried the wireframe's screen-tree drawer, about
  150 links hidden by one `display:none`: **1024 KB, 16 per cent of all HTML in `ui-visual/`**, a
  second and invisible navigation on a page that has its own. `base.css` was carrying 25 rules to
  style a drawer it also hid, plus `.device` four times and `body` three, each undoing the last;
  117 lines to 66. Removed by `ui-visual/_strip_wireframe.py`; the record stays in `wireframes/`,
  which owns structure.
- **A stacking order is a list, so it is written as one.** 0 1 2 3 4 5 6 10 40 49 50 60 199 200 201
  across twelve files became **eleven named layers** in `tokens.css` (`--z-under` to
  `--z-chrome-top`). Three of the old numbers did one job; **199 next to 201 is the shape of a value
  picked to win an argument rather than to sit in an order.**
- **Every screen has exactly one `<h1>`.** 74 of 77 had none, while `ia/docs/pages/seo.md` has
  specified one per indexed page since stage 03b. Only the tag moved, grey tree first
  (`wireframes/_generators/page_heading.py`); the 19 overlay-only screens keep none, because
  inventing a heading is inventing copy. Three section headings went h3 to h2 to close the skip the
  promotion opened. **Heading skips across the painted tree: 0.**
- **A system stylesheet names the font it needs; the document loads it.** `base.css` `@import`ed the
  Google Fonts URL every page already `<link>`ed: one dependency declared twice, and the CSS copy
  three hops from discovery. It is also the wrong place for the decision, since the call sends a
  visitor's IP to a third party before consent in a product that ships a GDPR cookie banner.
  **Self-hosting the three families is the production answer and is now an open decision, not a
  silent default.** *(Closed in step 8.)*
- Also: the bet amount field took `outline:none` and gave back a 1.5px underline colour change, the
  only control in the product without a focus indicator and the field a person types a bet size
  into; `<meta charset>` sat at byte 2064 on all 77 screens because the theme boot was inserted
  ahead of it; 21 selectors nothing on any page could match; the four how-it-works section headings
  had no rule at all (18.72px is what a browser gives an unstyled h3); 15 half-pixel type sizes in
  the vitrine's own chrome; a comment naming `_theme.css`, deleted in step 7, on 76 screens.
- **Two things this pass got wrong and had to come back for**, both the same shape. `.sidebar-divider`
  is written at run time by `ui-kit/_nav.js` out of a template string, so a scan that read only
  `class="..."` in HTML called it dead; deleting it left every group heading in the vitrine's side
  panel as unstyled text. **A class inside a template string is markup**, and gate 14 reads the
  scripts now. The reason nobody noticed is worse than the bug: `_verify/snap.cjs` walked
  `ui-visual/` and nothing else, so a pass editing `components/` could prove the product and say
  nothing about the vitrine the same file paints. It takes `--kit` now, and re-running it against a
  worktree of the pre-pass tree found two more: `kit.html` has `<body class="app-case">` and
  `.app-case` is transparent by design, so the body stopped painting the page; and one label took an
  inline margin the removed `!important` had been out-shouting. **Removing an `!important` is only
  safe once you have found what it was arguing with.**
- **Three new gates**, so none of it grows back: **9** now fails on a style attribute, **12** owns
  the stacking order, **14** fails on a selector no markup can match (the other half of gate 11).
- **How it was verified, and a tool that had to exist.** `_verify/diff.cjs` walks two snapshots in
  step, which is right while the DOM is fixed and useless the moment a pass removes markup: every
  index after the removal points at a different element. **`_verify/visible.cjs`** keeps only what
  the browser reports as visible and compares those sequences, so a `display:none` deletion proves
  itself and a real side effect (a moved sibling, a renumbered `:nth-child`) still shows. Across the
  whole pass, at 76 screens x 5 widths, what moved: four dock buttons and one CTA bar lost 2px of
  padding (14px and 10px were never on the 4px grid, and an attribute never went through step 6),
  six section labels took the system's `.1em` tracking, and four headings went 18.72px to 18px.
  Everything else identical to measure; 0 text pairs below AA in either theme.

---

## 2026-07-27 - Stage 09, step 6b: the theme, as the proof of the semantic layer

The product is dark, so its theme is a LIGHT one and the attribute says what it is:
`[data-theme="light"]`, section 3 of `components/tokens.css`. It exists as a proof, not as a feature
(`ui-visual/_theme_switch.py --strip` removes the harness in one command); whether daylight ships is
a separate decision. A rebrand would prove nothing, because swapping primitives works on a flat file
with no roles at all. A theme is the test that needs the second level: the ground inverts, the ink
inverts, light and shade swap places, and the action still has to read as the action.

**Roles only, 89 of them; not one primitive redefined.** Daylight's values are their own primitives
at the end of section 1 (chalk ramp, warm ink ramp + alphas, one dark brass, darker green/red, five
chalk veil alphas, the Vault's own grain, a second logo mark). 265 -> 320 tokens, growth that buys a
second theme rather than harvest. The semantic selector is now `:root,[data-theme="dark"]`, so any
element can be marked and its subtree renders in that theme: `tokens.html` shows every role in both
grounds at once, live, and its contrast table has a column per theme.

**What the theme found, twelve holes, all fixed:** the stone grain read straight from a primitive
(11 declarations in 10 files -> `--surface-grain`); the brass logo mark, same category
(`--mark-logo`); the drawer backdrop reading the emboss shade instead of the scrim; the close disc
on a photographic head reading the ink of a drop shadow (-> `--scrim-photo`); a SELECTED state
painted with the focus-ring role (`tabs.css` x2, `options.css`); **five hex literals drawing the
multi-outcome chart from inside the page script on 13 screens** (a whole categorical palette the
token file could not see -> `--series-1..5`, handed to the SVG as `var()` so it follows the theme
live); a wireframe-era grey in a style attribute; **nine `mask-image` stops reading `--shadow-ink`
for "opaque"** (a mask keeps only the ALPHA, so every masked photograph faded to a third in daylight
-> `--mask-solid` / `--mask-mid`, never themed); and `--bg-brand-mark`, a role named for the plate
under the X and Apple marks that is really the colour of the marks (1.06:1 on a pale button, now
`--ink-900`); **a hover fill and a chart grid line both painted with the LIT LIP of an emboss**
(`--bevel-faint` did three jobs; on chalk a hover cannot reach for more light and a white grid line
on a white chart is not there -> `--tint-hover`, `--line-grid`); and **a filled glyph taking a text
role** (the bookmark: the reflection kept its contrast, 6.7:1 -> 7.2:1, and doubled its weight,
because light on dark spreads and ink on paper sits solid -> `--icon-quiet` 4.3:1, `--icon-brass`
3.2:1; the text-safe brass also reads brown at 16px, so the saved state stopped meaning gold).
Also found: `_rescale.py`'s duplicate-role sweep was file-wide and ate 8 theme
overrides, now per block.

**The sharpest lesson:** a veil is not a dark colour over a picture, it is the layer that
guarantees the words, so it follows the INK, not the photograph. `--scrim-photo` and
`--veil-photo-*` look like one idea and are two.

**Five corrections the first cut needed** (all user-caught by eye, then measured): the stone was
yellow (chalk warmed with depth, +8 to +36; the graphite is faintly COOL at -4..-8 and all the
warmth is in the ink, bone +19 - now a constant +8 at unchanged luminance); the blocks went flat
(the shade ladder was scaled as a unit, right for a 1px inset edge and wrong for a blurred drop -
now split, edge .10/.16, drop .32/.44); the grain vanished (dropped to a third on a backwards
reading of `overlay`, which above mid grey behaves like screen and bites LESS - now the Vault's own
0.9/0.8); and **the ramp was translated, not reflected**, the deepest of the four. The first cut
inverted the ORDER and not the DIRECTION: the page sat mid-ramp at L* 85.6 and every surface still
came forward by getting LIGHTER, so daylight was a generic grey theme for a structural reason, and
it ran a third too loud (graphite fills span 11.7 L*, that chalk ramp 15.5; a category chip stood
9.5 L* off its bar where the Vault puts it at 4.0). Daylight is now the graphite ramp **reflected
about its own ground**, computed not picked: `chalk L* = page L* - (graphite step L* - graphite
page L*)`. The page becomes the lightest thing on screen, every surface settles onto it, every
separation keeps the Vault's size with the sign flipped; 12 steps, each within 0.2 L* of target,
and a chalk step carries the number of the graphite step it answers to (`--chalk-850` answers
`--graphite-850`), so the theme block is checkable line by line against section 2. The reflection
is TOTAL, gradients included: a graded face then reads as lit from below, which is the right trade,
because reflecting the fills but not the gradients loses the ground under anything sitting on a
gradient's light end (that is where the chip problem came back). Fifth: **the reflection went one
role too far.** Lightness on graphite carries depth AND presence, and only depth can invert:
reflecting a control puts the most present thing in the system 11 L* under the page, which reads as
dirt, and it is the exact grey the grey-box wireframes used. So six roles (surface, slab-from,
control, control-hover, chip, chip-pressed, dialog-head) leave the reflection and sit at the top of
the ramp in the Vault's own order and direction, and the EDGE carries what the fill gave up
(daylight's hairline is 2.2:1 against its surface, the Vault's 1.1:1). The chalk ramp is now 8
steps + 1 hairline, as long as the stone is. **Area is the tell:** a chip 6.5 L* under white is a
quiet pill, a header band the same 7 L* under white is a dirty field - depth is read against how
much of the screen it covers, which no token file can see.

**Switch:** above the tree in both panels, single-source markup + boot in
`ui-visual/_theme_switch.py` (imported by `_resync_sidebar.py` and `_gen_component_pages.py`);
inline in `<head>` so daylight never flashes graphite; `localStorage` key `pm-theme`. Gate 1 masks
it as chrome, like the sidebar. **Gate 13** is new: colour goes through a role (a component reading
a colour or material primitive fails the build) + every screen can switch.

**A frame is a document.** The first cut of the theme lied in the vitrine: every stand page went
pale while every `<iframe>` inside it stayed graphite, because a specimen is its own page and
`data-theme` does not cross into it. Fixed both ways - the boot block is now in every specimen and
in `selftest.html` (so a frame is right at its own first paint), and the parent tells every frame
by `postMessage` on toggle and on `load` (so an open frame follows the switch). postMessage, not
`contentDocument`, for the reason `_frames.js` already had: from `file://` every document has an
opaque origin. Gate 13 gained "every frame follows"; gate 5 had to start its search at `<body>`,
since a head script now exists and its slice was coming out empty.

**Verified:** 77 screens x 2 themes x {380, 1280} - 0 below AA, 0 overflow, 0 console errors;
selftest "all pass" in both themes. Pre-existing defect found, NOT theme-related, logged for step
7: the win overlay h2 renders 52px left of its content box and `overflow:hidden` clips it to "u
were right" in both themes. *(Closed in step 7.)*

---

## 2026-07-27 - Stage 09, step 6: the primitives became scales

The token file had been READ out of the product, which is right for a colour role and wrong for a
scale: every literal anyone had typed became a token, 348 of them. Space had 25 steps with 1 2 3 4 5
6 7 8 9 10 in a row, text had five half pixels left from rem arithmetic, radius had two names for one
pill, and the graphite ramp had 46 pairs no eye can separate. Now **265 tokens**: space 25 -> 11 on a
4px grid (plus `--hairline`, since 1px is a line and not a distance), radius 12 -> 5, control and icon
value named with no odd sizes, text 21 -> 10 with the half pixels rounded UP, display 5 declared and
unused -> 7 wired (nine literal `clamp()` gone), leading 8 -> 6, graphite 24 -> 15, alphas 54 -> 28.
The whole map is data in **`ui-kit/_rescale.py`** (idempotent, `--dry-run`), which is both the
migration and its own test. Rules now written down in `architecture.md`: round to the nearest step and
break a tie toward the heavier neighbour; a number is a step only up to 64px; a colour merges only
under deltaE 1.5 AND when the two never meet on screen. Two new gates stop the harvest growing back:
**11** no orphan token, **12** no raw scale value.

**Deliberate, measured pixel movement.** This is the one pass that moves the product on purpose. Every
change was checked against the map with `_verify/`: 1274 distinct property changes, all of them
layout or type or a colour under deltaE 1.5, except `#e88a84` -> `#e79087` (two quiet reds for one
job, the pair the file had already marked). No touch target fell below 44px (the deposit amount field
now says `min-height:var(--control-44)` instead of reaching 45px by accident).

---

## 2026-07-26 - Stage 09, step 5: one source of css, and Stage 08's navigation restored

**Step 5.** Every painted screen dropped its inline `<style>` (25 to 42 KB of grey-box skeleton, 7
distinct copies across the 76 pages) and its `_theme.css` link, and links exactly
**`../components/index.css`** and nothing else. The migration is `ui-visual/_use_system.py`
(idempotent). Gate 9 in `ui-kit/_check_kit.py` enforces the one-source rule from here on. Proof
tooling lives in `ui-kit/_verify/` (snapshot every screen at five widths, diff by element and
property, group by cause). `ui-visual/_theme.css` and `_theme-vault.css` were left on disk unloaded
and deleted in step 7.

*Provenance, how it worked before:* `ui-visual/_theme.css` was the Vault colour layer; it
`@import`ed `ui-visual/_theme-vault.css` (base Vault tokens + component skin) and was linked AFTER
each page's inline `<style>` so it overrode by source order (owning colour/type/surface only). Vault
tokens sat in `:root` (graphite/brass, `--groove-*` engraved edges, `--stone-dark` grain), and it hid
the grey-box scaffolding + the wireframe screen-tree.

**NAVIGATION RESTORED, a Stage-08 defect.** The colour pass had flattened **every** product `.html`
link to `#` (`neutralize()` in `_apply_theme.py` / `_apply_family.py`, plus hard-coded `#` in the
`_gen_category.py` card templates), so all 76 painted screens looked finished and went nowhere while
the grey wireframes stayed clickable end to end. **9633 links restored** by `ui-visual/_relink.py`
(idempotent, six passes: aligned against the grey twin, by key in the twin, shared chrome donated
between painted screens, cards by their own kind, by key across the painted tree, then a 3-entry
table for the blocks that exist only in colour). Only `href` values changed - the 76 files are
byte-identical otherwise, so nothing moved a pixel. 17372 internal links, 0 broken; the 1604 anchors
still dead are dead in the wireframes too (footer placeholders marked "to be built"). The three
generators no longer flatten a link whose destination has been painted, and **gate 10** runs
`_relink.py --dry-run` so a re-broken link fails the build.

---

## 2026-07-18 - Concept + DESIGN.md synced to Vault

`concept/concept.html` matches the shipped card (thin odds bar, tinted YES/NO) + a new **Controls**
panel showing the chip family; `DESIGN.md` fully rewritten Signal -> Vault.

Also on this date: `_apply_theme.py` began injecting the themed category bar and wrapping the head +
state content in the shared `.cat-layout` stone plate, so a state reads as "the feed minus the cards"
(the `.state-block` goes borderless on the plate).

---

## 2026-07-16 - Concept locked: Vault. UI + Visual, the Event Feed family

**Direction: Vault** (superseded the earlier Signal exploration). Graphite canvas (page `#0f1013`,
device `#141619`), matte **brass** brand (`#c7a24e`, text-safe `#d7ac53`) + **bronze** `#6e5a2e`;
**green = YES / red = NO reserved as outcome semantics only** (brass never collides with the
win/lose colour); real event photography + **two-stone embossed plates** with inset brass hairlines +
notched corners, cards that float. Fonts: **Space Grotesk** (display), **DM Sans** (body), **IBM Plex
Mono** (numbers/mono). Binary feed card = **treatment B** (odds bar), multi-outcome = **treatment D**
(option rows). Reference screen for the colour pass = `event-feed.html`. All accent/text-on-graphite
pairs contrast-checked WCAG AA on the stand. The shipped system is `DESIGN.md`.

The visual language was decided as **rules traced to data + taste**, not a mood. Sources in
`concept/docs/`: `references.md` (Refero research, dark base) and `concept.md` (designer taste
captured verbatim + 5 attribute pairs A1-A5, each traced to a data line and a borrowed technique +
the locked decisions). Explored across contrasting directions (Newsroom after dark / Signal / Arena,
then a Signal refinement); those exploration stands were archived to `concept/old/pre-vault-3d/` when
Vault won.

**The reference screen** `ui-visual/event-feed.html`: 12 event cards, JS-injected **odds bar**
(renders treatment B from the `.prob` text, thin 5px), multi-outcome option rows (D), **tinted-not-fill
YES/NO buttons** (the odds bar carries the outcome colour, buttons stay quiet - "spectator, not
trader"), a redesigned **How-it-works `<dialog>`** (brass-tinted hero + icon chips), a **trust bar**
(USDC 1:1 + resolved count) + a footer **trust-cards strip**, the **graphite chip control family**
(cat-nav chips with icons + a condensed sticky strip, filters, Load-more - one `#1b1e23` chip, 12px,
brass on active), and the roadmap-sidebar course chrome.

**8 state pages** (`event-feed-empty/-error/-loading/-push-permission-missing`, `-logged-out` +
logged-out empty/error/loading) generated by **`ui-visual/_apply_theme.py`** with a **"shell + swap"**
strategy: start from the finished `event-feed.html` shell, swap in only the regions that differ
(always `<main>`; for logged-out also `<header>` + `<nav.bottom-nav>`), then run two voice-safe
transforms on the grafted fragment (a product link is kept when its destination is painted, Favorites
heart -> bookmark) + a `distill()` pass. Idempotent; never edits `wireframes/`, never regenerates the
base.

**Category pages:** the top category nav is page-level - `event-feed-{politics,crypto,culture,general}.html`
(generated by `_gen_category.py`; each drops the trending hero + sub-filter and shows only that
category's events, ~6). Trending stays `event-feed.html`. Nav wired on both levels; the old
client-side category-switch handler was removed so tabs navigate. **Order:** run `_gen_category.py`
then `_resync_sidebar.py`. `_resync_sidebar.py` is the single source of the ui-visual left screen-tree
and gained a **Categories** group under Event Feed, active-marked per page.

**Critiqued with `/impeccable critique` (dual-agent), snapshots in `.impeccable/critique/`. Score 33
-> 34 / 40** (Signal-era pass; the P1/P2 hardening carried into Vault; the whole-stage score at the
end of Stage 08 was 31 -> 38 / 40). P1/P2 hardened: NO-button contrast 3.41 -> 5.48:1, footer 3.37 ->
6.04:1, 44px touch targets (bet/bookmark/bell + cat-nav/filters), `:focus-visible` rings, tinted
YES/NO (spectator not trader), trust bar near the action, distilled controls (dropped the duplicate
Category dropdown, "Volatile" jargon, reverse toggle). Presentation-clean: `.uv-bar` + `.tbd`/placeholder
chips hidden, footer shows a real "Predict Market" wordmark. **P3 deferred** (live odds-delta
animation, error-vs-empty differentiation) - see backlog.md.

---

## 2026-07-12 - Stage 04: the wireframe reconcile against the IA Detailed layer + CJM

The 99 wireframes predated the IA Detailed layer (03b) and the CJM, so Stage 04 ran as a targeted
reconcile that rendered the newly-specced IA and closed two CJM gaps, all voice-safe (new pages
hand-authored; shared/global changes by idempotent in-place post-processors; `gen_*.py` never
re-run). Added: the 5 system pages (from `system.md`); a footer trust strip (USDC 1:1) + "Popular
right now" SEO block + real hrefs + Cookie-preferences re-entry (all 87 footer pages,
`footer_reconcile.py`); a per-card story-led "why" + below-fold SEO sections on the feed
(`feed_reconcile.py`) and category pages (`category_reconcile.py`); a Related-events block on Event
Detail (`related_events.py`); and the Win F5 overconfidence-friction ("Before the next one", no "bet
again"). Course Stage-04 infra (`screens.md`/`_nav.js`/`_wf.css`/`index.html`) was skipped as
EQUIVALENT to ours (`_screens.md` + `_shell.py nav_tree`/`resync.py` + inlined CSS + the per-page
screen-tree). New copy logged in `voice/docs/microcopy.md` (Steps 15-20); the reconcile audit + fixes
are in `wireframes/_critique.md`. Gates: 104 pages, 16061 internal links, 0 broken, 0 em-dash.

Result: 104 pages - every screen in the IA screen tree, each state its own page, plus the Favorites
view (`favorites.html` + empty + loading) and the 5 system/global pages (`404` / `500` / `maintenance`
/ `cookie-consent` / `toasts`). Orphans `[SIROTA]` (Settings, Leaderboard, Help/FAQ) unbuilt by
design; the standalone Bet Screen is dissolved into the inline Event Detail bet panel.

---

## 2026-07-12 - IA Detailed layer (Stage 03b), as a targeted reconcile

**Scope = targeted reconcile, not the full node-by-node build.** The 99 wireframes already exist and
ARE the per-page B/W render, so we did NOT redraw pages, write a `pages/*.md` per screen, add an
`ia/_nav.js`, or renumber the sitemap to X.Y (all would duplicate the wireframes or
`resync_sidebar.py`). We built only what the wireframes deliberately omit and a launch needs:

- the **A-E SEO structural layer** for the indexed public pages (Event Feed, Event Detail, Category,
  How It Works, Public Profile); every private/transactional zone is `noindex`, no schema;
- the **footer** as an SEO / internal-linking node;
- the **system / global nodes** (404, 500, maintenance 503, cookie-consent grounded in law, toasts).

New sources live in `ia/docs/pages/` (`seo.md`, `system.md`); rendered B/W as `ia/seo.html`,
`ia/system.html`. The shared sidebar stays single-source via `resync_sidebar.py` (not `_nav.js`); new
IA pages register there.

**Built.** `seo.md` carries the indexation policy (every screen family index vs noindex) + the A-E
template + full A-E for Event Feed, Event Detail (with the per-event schema decision: `WebPage` +
`BreadcrumbList`, `schema.org/Event` rejected), Category, How It Works, Public Profile, and the footer
node. `system.md` carries 404 / 500 / 503 / cookie-consent (grounded in GDPR + ePrivacy + UA Law
2297-VI, cited) / toasts; Search stays deferred. Both render to `ia/seo.html` + `ia/system.html`,
wired into the shared sidebar under IA > Detailed layer (SEO layer, System nodes) on all pages.
`sitemap.md` registers the system + footer/legal destinations (SYSTEM AND GLOBAL). Link check: 27
pages, 743 links, 0 broken. Deliberately not done (would duplicate the wireframes): per-screen B/W
redraws, `pages/*.md` per screen, `ia/_nav.js`, X.Y renumbering.

---

## 2026-07 - Voice: the interface copy rewritten (Steps 05-14)

Every UI line was edited line-by-line against `voice/docs/voice.md` (five principles + lexicon +
forbidden + per-element rules). `voice/docs/microcopy.md` holds the read-only text inventory it was
edited from plus the full rewrite log (all screen families done, incl. the step-13 "rest of the
screens" pass).

**Event Detail content tabs** were rewritten from trader vocabulary (Top Holders / Positions / shares
/ "bought N YES at $X") to spectator language in the step-14 pass: below the event content, a
Polymarket-style tab strip (CSS-only radio switch, no JS) - **Comments** (sort + composer with
likes/replies; logged-out prompts sign-in), **Biggest bets** (YES/NO columns), **Bets** (table
Bettor/Side/Amount; your bet highlighted when logged in), **Activity** (recent-bets feed). On binary +
multi + resolved, logged-in and logged-out.

**Chrome wiring** landed in the same period: header (Favorites -> Favorites view, bell ->
Notifications, avatar dropdown -> Profile/My Bets/Wallet/How It Works/Logout) and the mobile bottom
nav are real links, not dead buttons; logged-out controls open the sign-in dialog. A `How it works`
button sits in the header next to the logo and opens a native `<dialog>` quick-explainer (the feed's
three explainer sections + a link to the full How It Works page); self-contained `.hiw-*` styling, on
all 87 header pages via the idempotent `howitworks.py` post-processor (Step 21 in `microcopy.md`).
Applied by the idempotent `fixpack.py` post-processor.

**Status at close:** Lesson 05 steps 1-7 done; the step-7 finalization audit (Step 14 in the log) is
clean - 0 lexicon/forbidden violations in product copy across all 99 pages (excluding the brand name
"Predict Market", the voice-sanctioned "the market resolved YES/NO", and the AMM mechanics gloss).

---

## 2026-07-07 - Wireframes: the finalization trio

Three audits, all recorded in `wireframes/_critique.md`:

- a **flow-wiring audit** (step 7) that verified every edge against `ia/docs/flows.md` and fixed the
  last naked recovery buttons (`Try again` on the Event Feed + Category error pages, `Try another
  card` on `deposit-error-card`);
- a **99/99 coverage audit** (step 8) against `ia/docs/sitemap.md` - every sitemap screen + state has
  a page, deliberate exclusions documented;
- a final **six-category defect pass** (step 9: style leak / placeholders / missing states /
  dead-ends / zone-without-action / off-map) - all clean.

Earlier passes in the same log: Krok 8 (consistency reconciled across all families), Krok 9, and the
**2026-06-29 multi-agent re-critique** (all 99 pages across five families - clean bar one minor
clarity fix on `event-detail-resolved.html`, live "now" odds reframed as "Trading closed / at close").
Standing gates: 0 em-dash, 0 broken internal links, 0 style leaks.

---

## 2026-07-03 - Wireframe annotations moved out of the wireframes

The wireframes became clean grey-box UI only. The inline `zone:` chips and the bottom `.side` block
(the `zone -> job / finding` annotation list + nav-tree / header-model / responsive / variant notes)
were extracted into a dedicated IA visualization at **`ia/annotations/`** - one HTML page per screen
family, every state inside it, each state showing a nested zone map + its annotations + a link to the
live wireframe, plus shared structure/flow notes. Entry point: `ia/annotations/index.html`. Styled in
the dark research/IA-viz theme and wired into the shared left sidebar as "Wireframe Annotations"
(under the Plan section, after Wireframes) on all root viz pages; the annotation pages carry that same
sidebar (with a sub-link per screen). Generated + stripped idempotently by
`wireframes/_generators/ia_annotations.py` (`build` then `strip`; run `build` before `strip`).
