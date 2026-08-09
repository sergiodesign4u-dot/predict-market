# Decisions

What was done, why it was done that way, what was rejected and on what grounds.
Entries carry a date, newest first.

**This file is not loaded into a session.** `CLAUDE.md` holds the rules that must act next
time; this holds the record of how they were arrived at. An entry is written once and is
not edited afterwards: a later entry supersedes an earlier one rather than rewriting it,
so a claim here is true as of its own date and nowhere else.

Open items are not here either. They are in [`backlog.md`](./backlog.md).

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
