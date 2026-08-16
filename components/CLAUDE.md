This folder IS the design system. **56 stylesheets, 11,320 lines**: 50 here and 6 in `patterns/`,
re-counted 2026-08-17 after search stopped being a page you go to and became a control you use: the field
grew a sheet face and a header face on one rung, and the rung was chosen by measuring the free middle of the
header row at **69px on 640, 137 on 760 and 277 on 900**, which is why it enters at RAIL and not at DESK.

**The line above read 55 and 10,948 and the tree held 56 and 11,134, which is one whole FILE missing from a
count taken the day that file was written.** `crumb.css` landed on 2026-08-16 and the figure beside it was
re-taken the same day and typed rather than counted, so the fourteenth atom is the one the enumeration walked
past. This is the same defect the kit's `N lines` badges were struck for the day before, one level up: **a
number kept in prose is re-derived by whoever reads it and by nobody who edits the folder.** It was 55 and
10,896 on 2026-08-16 after `search.css` was written,
and the error tone was given to the one surface that had never worn it. `search.css` was the first file
added to this folder for a control the IA had DECIDED against rather than for one it had specified. It was 54
and 10,805 earlier the same day, after the minor-observations pass gave the skeleton a hidden status line and
moved the profile's lead figure off an ordinal. It was 10,764 earlier the same day, after the
palette pass gave the hero chart a scale, took Volume off
brass and took the tint off the spectator's YES/NO pair. It was 10,613 earlier the same day, after
the critique pass took the bottom nav and the bet dock off `sticky` and
gave the sticky furniture three names. It was 10,381 on 2026-08-15 after the Animation stage's frame-cost pass took the knob and the step dot off
`left` and `width` and deleted the blanket reduced-motion net. It was 10,332 earlier the same day,
after the same stage rewrote 69 motion declarations, gave six silent
components a response and gave the skeleton the only status animation in the product. It was 10,140
earlier the same day, after the `vh` fallbacks went. It was 10,130 earlier the same day, after the
action bar took its floor. It was 10,101 earlier the same day, after
the viewport-unit census below. It was 10,067 on 2026-08-14 by `cat components/*.css components/patterns/*.css | wc -l` after the filters
sheet, its two later passes and the scroll-driven edge fade. It was 9,224 on 2026-08-13 after `trust-art.css`
was written (`docs/backlog.md` 140). It was 53 and 8,734 earlier the same day, after `print.css`
(`docs/backlog.md` 125). **`trust-art.css` is the first file here that is not a component and not a
level**: it holds four `--trust-art-*` custom properties, each a `data:` URI carrying one of the
trust drawings, and it has no selector, no page in the kit and no row in the inventory. It exists
because a mask image is a CORS-enabled fetch, and the trap it pays for is at the end of this file. It was 52 and 7,767 on 2026-08-12. The file count was
re-counted 2026-08-11 by listing them, after `platehead.css` was written the same day, and was
right; **the line count published beside it was 7,440 and was 327 short**, which is what a number
kept in prose costs even on the day it is re-taken. It said 50 and 7,034 the day before and 51 and 5,651 the day
before that, and the arithmetic behind each is gone, which is what a count kept in prose costs. The
one thing that is certain about the earlier numbers is that `account.css` was deleted on 2026-08-08
by backlog 63, `hiw-dialog.css` became `hiw.css` on 2026-08-11 by backlog 15, and `platehead.css`
was written the same day by backlog 108 out of six rules that stood in `dialog.css` and `hiw.css` at
once. `tokens.css` plus
one file per component, all reached through `index.css`.

**168 documents link `index.css` and nothing else, and they are not the ones this line used to
name.** Re-counted 2026-08-16: **109 of 109** documents in `ui-visual/` and **60 of 60**
pages in `ui-kit/`. **0 of the 108 in `wireframes/` link any stylesheet at all**, and they carry 108
inline `<style>` blocks instead, which this file already says out loud further down and said the
opposite of here for as long as both sentences stood. So **an edit here reaches every painted screen
and every kit page at once and none of them can override it, and it reaches the grey tree not at
all.** There is no build step and no gate: what you write is what ships.

**109 and 108 are both right and they count different things, so every number below says which.**
`ui-visual/` holds **109 documents**; **108 of them are screens** and `overview.html` is the index of
the tree rather than a screen in it, which is why about twenty `Stands on:` lines in this folder read
105 and are exact. A sweep over `ui-visual/*.html` reads 106. A statement about the product reads
105.

## The invariants

- **Two token levels, not three.** A raw value is a **primitive** in section 1 of `tokens.css`; a
  colour is a **semantic role** in section 2. A component reads a role and never a colour primitive,
  and never writes a raw scale value. Colour is the only thing with a second level, because a radius
  or a gap has nothing for a theme to override.
- **A state is a TOKEN, never a value typed into a class.** `:hover`, `:active`, `:focus-visible`
  and `:disabled` read a role. A literal in a state rule is a decision taken in the one place no
  theme and no later reader can find it.
- **A state token has a value in both themes or it is not one.** A theme with a hole in it rots
  quietly and is handed to a developer broken, and nobody sees it because the hole renders.
- **A pattern starts at three screens**, adds no styles of its own, carries no colour, and imports
  last. Two screens is a candidate and it stays markup.
- **A floor is the family's, and it is declared once.** The focus ring and the 44px touch floor are
  both one rule in `base.css`, because a person tabbing and a person tapping are not asking each
  component separately. The touch floor stood in six files as six LISTS until 2026-08-08, and what a
  list leaves out nothing says: two of five chips had it and `.market-head` had none. A component
  speaks up only to be excluded, and an exclusion carries its reason.
  **THE THIRD FLOOR IS MOTION AND IT IS A VALUE RATHER THAN A RULE, which is the shape to reach for
  when the family is not a selector.** `base.css` has always shortened every duration under
  `prefers-reduced-motion`, and shortening a transition never removes a `transform`, so five files
  each carried their own `:hover{transform:none}` until 2026-08-13. A blanket
  `*:hover{transform:none}` was refused by a census: **5 of the system's 20 transforms are movement**
  and one of the other 15 is `.market-chevron`, an element that turns over when its market opens and
  would have been flattened for as long as a pointer rested on it. So the distance is multiplied by
  `--motion`, 1 normally and 0 under the query, and each file keeps its own distance beside the rule
  that moves. **When a family cannot be selected, put the switch in the value the declaration already
  reads.** `docs/backlog.md` 132.
- **MOTION LIVES IN A TOKEN, A COMPONENT OR A PATTERN, AND `transition`, `animation` AND
  `@keyframes` ARE FORBIDDEN IN A SCREEN FILE, EXACTLY AS `@media` IS.** Two durations, `--dur-fast`
  for a control answering a finger and `--dur-slow` for an element arriving, plus `--pulse-period`
  beside them, which is a PERIOD and not a third rung of the ladder. Two curves. A literal duration
  or a bare `ease` in a component file is a defect, not a shorthand: measured 2026-08-15 from the
  comment-stripped source, **0 duration literals and ONE bare easing keyword in 54 stylesheets**,
  against 54 bare keywords the day the stage opened. **The one is `linear` on
  `animation-timing-function` in `catnav.css`, it is deliberate, and the published number was 0
  until the second instrument found it**: the stage's own check read `transition:` and `animation:`
  and never looked at a longhand. A scroll timeline maps progress from distance, so the identity is
  the only correct function there and a `--ease-linear` read once would be a name for a constant.
  The reason stands beside the rule. `transition: all` is 0 and stays 0, because it animates
  whatever a later rule adds, including the expensive. **A movement gets one of three jobs named
  before it is written**, a response, an arrival, or a process still running, and a movement with no
  job is deleted rather than kept because it already exists. The register is
  `../ui-kit/docs/inventory.md`, motion, and the argument is `../ui-kit/docs/motion.md`.
  **Less movement is the token override in `tokens.css` and nothing else.** The blanket net on `*`
  was deleted on 2026-08-15 after the check was run without it, with a positive control first: an
  injected `transition:opacity 999ms linear` read back 999ms in both engines, and then 163 documents
  gave **0 elements above 1ms**. Under `!important` on `*` a component that reads no token is
  indistinguishable from one that reads every token, so the net had been making the sweep unable to
  fail. **A cycle is REPLACED under the setting and never shortened**: 1ms per period is a flicker,
  which is worse than the still box it replaces.
- **Green and red are outcome semantics (YES / NO), brass is the brand.** An accent never borrows
  the win/lose colour, and a candidate in a multi-outcome chart is not an outcome. `DESIGN.md`
  decides this twice, which is why it is the one rule that overrules a local preference.
- **A part is imported before the whole that holds it.** The `@import` order in `index.css` is a
  rule, not formatting: the cascade breaks ties of equal specificity by source order, so a card may
  restyle the odds bar it contains and an odds bar may not quietly restyle every card. A new file
  goes into its own level group, never at the end.
- **A level is a decision, not a reading.** Level 1 contains nothing from the system, level 2
  contains atoms, level 3 contains molecules or is a shell. A component built out of its own class
  names reads as containing nothing, and seven of seventeen such readings were once the whole atom
  shelf and not one of them was an atom.
- **`vector-effect:non-scaling-stroke` IS ABOUT STROKES AND DOES NOTHING FOR A SHAPE.** The detail
  chart is `viewBox="0 0 300 100"` with `preserveAspectRatio="none"` drawn into about 900 x 160, so
  the two axes scale by different factors and a `<circle>` in that space renders as an ellipse six
  times wider than it is tall. The polylines look right because they carry the property; the moment
  the chart wanted a dot at the end of the line, it had to leave the SVG. It is a DOM element in the
  positioned plot with its height as a percentage, which is a datum.
- **A `url(#id)` IN A STYLESHEET CANNOT BE SUFFIXED AND ONE IN THE MARKUP CAN.** `hero.css` writes
  `.hf-area{fill:url(#hfyes)}` and is safe only because the hero stands once in a document. The
  detail chart stands twice on its kit page, and the kit's convention suffixes every id a cell
  redefines TOGETHER WITH every `url(#id)` pointing at it, which reaches markup and not a rule. So
  that one `fill` is a presentation attribute, and it is the one place a paint reference is allowed
  out of this folder. **The alternative is the tab defect again**: ids suffixed, rules not, second
  cell empty and nobody looking.
- **A COMPONENT ASKS THE WINDOW UNLESS THE WINDOW AND ITS COLUMN MOVE IN OPPOSITE DIRECTIONS, AND
  SINCE 2026-08-14 EXACTLY ONE DOES.** `backlog.md` 129 refused container queries on a measurement:
  of the 25 selectors standing on both sides of their own rung, **24 would have resolved identically
  at every placement.** This is the 25th. `.ed-head` measures 611 at a 640 viewport, 645 at 700 and
  **341 at 760**, because that is where the bet panel arrives and takes 322 of the row, and again 681
  at 1100 and 501 at 1140 where the review sidebar docks: **at both drops the window gets wider and
  the head gets narrower**, and the title goes from 2 lines to 6 across one rung. A window query
  could only say it by naming the panel's rung and the chrome's dock, which are facts about other
  components. `patterns/detail-shell.css` declares the container and `event-detail.css` asks it,
  because **place is not a property of the brick**: the pattern is what puts the column beside the
  panel. A container threshold is not a token and is registered in `../ui-kit/docs/responsive.md`.
- **A MEDIA QUERY MAY NOT STAND IN A SCREEN FILE, EVER**, and it is written here and in
  `ui-visual/CLAUDE.md` both, because a rule kept in one place is a rule half the hands never meet.
  Adaptation lives in a token, a component, a pattern or the shell. Measured at Responsive step 4:
  **34 width queries in this folder, 0 in any of the 106 documents in `ui-visual/`.** It was 33, then
  35 on 2026-08-12 when the outcome row and the outcome pair each took one at the desk rung, and 33
  again on 2026-08-13 when backlog 129 deleted the one in `tokens.css` and the one in `card.css`
  **and put nothing in either place**: the two page insets ramp with a `clamp()` now and the bookmark
  pull is unconditional. **A query that leaves with no replacement was answering a question its
  subject never asked.** It went to 32 on 2026-08-14 when the strip's own 640 block turned out to be
  paying a phone twice for the same rhythm, and to **34 on 2026-08-15**, both of them at the desk's
  narrow side and both of them a control that a desk sizes one way and a thumb another: the chart's
  range group drops its frame and the category chip drops from 48 to 44 with its padding. **Two
  queries arriving on one day is the shape to watch**, and neither invented a number. The counterpart
  reading used to say "35 of 43 components have no width behaviour of their own at all", **and that
  number was three numbers wearing one sentence, taken from a table with one placement per
  component.** Re-measured 2026-08-12 over every placement of all 47 components on the 105 painted
  screens, at thirteen widths: **10 of 47 have every painted placement filling its container, 26 of
  47 declare no width query of their own, and 8 of 47 are both** and are the only ones of which "no
  width behaviour of its own" is true without a footnote. **36 of 47 have placements that disagree
  with each other.** The rule still holds and for a smaller reason: a query appearing in a screen is
  almost never the screen discovering something, it is a component's rule written in the wrong file.
  The table and its method are in `../ui-kit/docs/inventory.md`, behaviour on width.
- **A component may not invent a width.** There are three rungs, named by what arrives at them:
  **40rem** the desk, **47.5rem** the detail's second column, **56.25rem** the rail beside the
  content, which are 640, 760 and 900 at the default browser font and MOVE WITH IT: at a 24px
  default the desk arrives at 960 and the rail at 1350, measured. **They went to `rem` on
  2026-08-13**, `docs/backlog.md` 135, once the type had moved and the old argument for px had
  expired with it. The narrow side of a rung is written exactly, `39.99875rem` and `47.49875rem`,
  and never rounded, because the pair rule is what stops both sides matching at once. **The 1140
  harness stays in px**, and so does the review toggle: the review sidebar is 220 physical pixels of
  chrome whatever the reader's font is. If a
  file needs a break that is not one of them it is a one-off and says so in a comment beside itself,
  or it is a fourth rung and gets named in the ladder in `tokens.css` FIRST. A breakpoint cannot be a
  token: a media query condition does not read a custom property and there is no build step here, so
  the ladder is kept by being read. **The move to 33 on 2026-08-16 is this pass taking one AWAY, not
  adding one**: the same comment-stripping script read 34 immediately before the critique fix and 33
  immediately after, when `course-chrome.css` lost the block carrying its toggle's lift and the lift
  became a sum of the two tokens it clears. Two readings by one script minutes apart are a delta that
  can be trusted; a delta against a sentence written on another tree is not, which is the whole
  reason this line keeps its own history. **There are 33 width rules, and this line has said 33, then 35,
  then 33, then 32**, counted each time from the comment-stripped source and never from the sentence
  before it:
  **25 name one of the three rungs, 2 name the 1140 harness, 4 name no rung** (560 in
  `event-detail.css` and `iconbtn.css`, 620 and 980 in `hero.css`) **and each of those four carries
  the one-off comment beside itself that this rule asks for**, verified by reading all four. **The
  32nd is the course chrome's and it is the one this rule nearly missed**: `course-chrome.css` cut
  the review toggle's lift at `759.98px` while the dock it exists to clear is cut at `47.5rem`, two
  numbers written the same day to be one rung and equal only at a 16px root. Measured with
  `Page.setFontSizes` on event-detail.html at seven widths: **at a 20px default the toggle crosses
  the dock by 4px at 760, 860 and 900; at 24 by 4px from 760 to 1000 and by 5px at 640.** It is
  `47.49875rem` now and the lift is `8.25rem`, and at the default nothing moved. **A boundary
  borrowed from another file has to be borrowed in that file's UNIT.** The 220px sidebar stays in px
  and that argument still holds, because it is a width of chrome and not a rung of the product. The alternative
  has already been paid for twice: a stand label written at 900 standing beside a bar that goes at
  640, and `navitem.css` arguing about a control's shape "above 860" when the rule that changes it is
  at 900. **A rung is one pixel and it belongs to the wide side**: below it is `max-width:639.98px`,
  never `max-width:640px`, because `max-width:640px` and `min-width:640px` BOTH match at 640 and the
  rung then renders a page that exists at no other width - nine of ten screens showed the desk
  utility on a mobile gutter under a mobile header with no bottom nav. The `.98` rather than 639 is
  because a zoomed window reports a fractional width, and an integer bound leaves a gap where neither
  branch applies.
- **Quiet is a colour, not an opacity.** `opacity` fades text into its background and no sweep that
  reads `getComputedStyle().color` can see it: `--chrome-muted` is 5.03:1 on the panel and 2.37:1 at
  `opacity:.55`.
- **A font is served from this repo.** No page may call a font host: the request carries a visitor's
  IP to a third party before the consent banner has asked anything. Faces are woff2 in
  `assets/fonts/`, declared once in `fonts.css`, imported first by `index.css`.
- **AND THE FOUR FACES THE PRODUCT USES ARE INSIDE `fonts.css` AS `data:` URIs SINCE 2026-08-14, SO
  NO DOCUMENT SAYS ANYTHING ABOUT A FONT ANY MORE.** It used to be a `<link rel="preload">` in the
  head of all **163** documents, two each, 326 lines, carrying `crossorigin` because a font is
  fetched in CORS mode even from its own origin. **That last clause is the whole story**: `file://`
  gives every file its own opaque origin, so from a disk page the CORS fetch has nothing to match,
  Chromium refuses the preload and loads the face through `@font-face` anyway, and **WebKit refuses
  both and renders the entire product in a fallback**. Measured by probe string at 40px from disk:
  `'DM Sans',serif` came back at **369px, the serif fallback to the pixel**, against 410 in
  Chromium, and 410 in both after the change. Inlining does what the preload did and does it
  earlier, because there is no fetch to start: CLS re-measured at 400 Kbps over a quarter of the
  painted tree is **0.0000 mean before and after, worst 0.0000 against 0.0001**. It costs
  **+38,605 bytes on the mean screen**, CSS 877,387 to 984,717 against fonts 68,725 to 0, and the
  53 documents that never use the mono now carry it. **The 163-document dependent of
  `../docs/backlog.md` 141 is not managed now, it is deleted.** Only the four `-latin` faces are
  inlined: the four `-latin-ext` files are requested **0 times** by any of the 163 documents,
  measured, and stay as files. And do not reach for `size-adjust`: it was built here with measured
  metrics and made the tree four times worse, with the reason written into `fonts.css`.

## The traps this folder has already paid for

- **A brass tint written as a colour function is invisible to every tool and to every reader.** Ten
  of them lived here as `color-mix(in oklab,var(--color-action) N%,transparent)`, seven at rungs the
  ladder does not have. Use `--tint-brass-06/09/16/30/45/60` and nothing else.
- **A skin can belong to a SURFACE rather than to a component.** Four controls in the header band
  wear one hover, and they are three different atoms plus two `<summary>` elements, so no component
  file could own it. The value is a token; each file says its control stands on the band.
- **Reading the source is not reading the page.** "0 non-neutral hex in the wireframes" was true
  while 992 links rendered in the browser's blue, because a link with no rule has one anyway and it
  is the User Agent's. A missing value is a value. Measure the computed result in a browser, at both
  widths and in both themes.
- **An attribute can be a guard that never fires.** 113 of the 121 amount fields carried
  `pattern="[0-9.$]*"` and the product contains **0 `<form>` elements**, measured across all 106
  documents in `ui-visual/`: a pattern is only consulted at form validation, so it validated nothing at any
  moment and read as a constraint to everyone who opened the markup. The other 8 did not carry it
  and the two trees disagreed about which. **Absent and inert are the same amount of nothing**, which
  is why the divergence went unnoticed. The field is `type="number"` now and the browser is the
  guard, verified by typing into it.
- **A scope is a claim about where the product IS, and it is the claim least likely to be checked.**
  `.app-case` opened **415 selectors in 36 of the 50 files, 31 per cent of everything declared here**,
  and it existed to keep these rules off the course chrome. Measured across all 106 documents in `ui-visual/` with
  every dialog open: it changed the outcome for **13 of 375 selector tails**, eight of them one file
  drawing a page differently from a sheet on purpose, and it matched **0 elements of the chrome**. The
  bottom nav, the footer and all 337 dialogs stand outside it (**341 since 2026-08-16**, when the four
  bet-state screens got the mobile sheet they never had), so what the wrapper actually did was
  hide three regions of the product from its own system, eight times in two days. **A wrapper that
  everything is inside is not a scope, it is a hole shaped like the exceptions.**
- **The fix for a scope is never a second selector.** The amount chip was repaired once by writing
  `.app-case .chip-amount, dialog.app-dialog .chip-amount`, and **the chosen state was not doubled
  the same day by the same hand**: 105 screens shipped a selected chip with a brass edge and no
  ground, no ink, no weight and no halo. A doubled selector is a face kept in two places and the
  second place is the one that gets forgotten. Take the container off.
- **A tie is not a hierarchy, and dropping a scope changes who wins.** Unscoping lowers specificity
  everywhere, so a rule that beat its neighbour on source order can start losing. Two did:
  `.app-case .ed-head .sk-thumb` tied with `.card.skeleton .sk-thumb` and would have fallen from 72
  to 56, and `.app-case .cmt-av` was beating one avatar rule and losing to another, so half the
  comment avatars drew a photograph with initials printed over it. **The reverse also happens and it
  is a fix**: `.hold-row:first-of-type{border-top:none}` had never once fired, because the scoped
  rule it was written to except tied with it and came later. Measure before and after, in a browser,
  or do not do it.
- **A line has no interior, so a filled set cannot fill it.** "Consolidate the stroked icons into
  filled" was measured against Solar Bold and **six of the 33 marks have no filled form**: a cross, a
  chevron, a plus, a tick and a hamburger are movements rather than things. What a filled set offers
  instead is a disc or a plate with the mark knocked out, and a disc inside a round icon button is a
  disc inside a disc. The set is **an object is filled, a movement is a line**, and what holds them
  together is **weight**: the stroke went 1.6 to 2.2 because 1.6 against the solid mass of Solar Bold
  is the gap the eye reads as "two icon sets".
- **A stroke closes a knockout, and a stand is structurally blind to it.** Solar Bold draws detail as
  holes cut from one path with `fill-rule:evenodd`. A stroke outlines every subpath including the
  holes, so 2.2 units of brass around a 2 unit exclamation fills it in: the warning triangle, the
  shield's tick, the globe's meridians and the magnifier's lens all shipped as **solid blobs** for a
  day. **The kit drew them correctly the whole time**, because a specimen stands where no component
  rule reaches it, so the one place the defect was visible is the one place nobody was looking. It is
  `stroke:none!important` on `svg.ic:has(use)` in `base.css` now: a floor the system declares, not a
  patch for a selector.
- **Two kinds of mark read two different properties, so every rule that paints an icon names both.**
  A stroked glyph takes its ink from `stroke` and a filled one from `fill:currentColor`. Nine
  `:has(use)` rules existed for the first filled handful and **three disagreed with the stroke beside
  them**, which is how one header shipped the same bookmark at `--text-primary` on one screen and
  `--text-icon` on the next. Name both or paint half of what you are pointing at.
- **A FLOOR IS NOT AN ASSIGNMENT, and the strength that makes a floor work is what breaks it.** The
  44px touch floor is `(0,5,1)` on purpose, so that no component can tie with it. The day `.btn-md`
  declared a height of 48, the floor out-specified it and wrote 44; the content then held the box at
  47, so **the same button stood 48 under a mouse and 47 under a finger**. A floor raises a short
  control and must never lower a tall one, which is `max(var(--control-44),var(--control-h))` and not
  `min-height:44px`. **The parity of a control was the FONT's decision until 2026-08-09**: padding
  and border are on the ladder, `line-height` on a control is `normal`, and DM Sans returns 21px at
  14px, so `.btn-md` was 12+12+2+21 = 47 while `.btn-sm` was a clean 36 from the same ladder. A
  component declares `--control-h` now; it is `@property ... inherits:false` because a control's
  height is not something the boxes inside it may claim.
- **A mask is invisible to `getBBox`, so measure the INK.** `i-clock-circle-b` was filed as a defect
  for painting 24 x 24 at field 0 where the rule is 2. It paints **20 x 20 at field 2**: Solar
  delivers it as a full-cell rectangle behind a `<mask>`, and `getBBox` returns the geometry of the
  path and never the mask. **This is the stroke-closing-a-knockout defect one layer up**, an
  instrument reading the drawing instead of the paint. Paint the symbol into a canvas at 20x and find
  the opaque pixels: it sees masks, holes, strokes and antialiasing, because it looks at what a
  person looks at. The same read found the glyph that WAS breaking the rule and that nobody had
  named, `i-magnifer-o` at field 1.23, painting 21.5 where the whole set paints 20.
- **A shape census files a logo as a duplicate every time.** Reading glyphs by their path data made
  the X mark "a second close" and Discord "a second chat", and both went into a backlog row as
  defects. **A brand mark is not in the system**: it keeps its own drawing, takes no system ink, and
  no generic glyph may stand in for it, because a paper plane is not Telegram.
- **Naming a third-party asset is not crediting it.** Fifteen Solar glyphs shipped under a comment
  reading "Solar Bold icon sprite" with **no attribution anywhere**, and the licence is CC BY 4.0,
  which asks for the author, the licence and whether it was changed. `../NOTICE.md` is where every
  bought-in asset now says what it requires.
- **A `<button>` SUPPLIES THREE PROPERTIES FOR FREE AND THIS FOLDER HAS NOW PAID FOR IT THREE
  TIMES.** `text-decoration:none`, `text-align:center` and `display:inline-block` are the element's
  own defaults, so a component whose control is a button wears them without declaring them, and the
  day the control becomes an `<a href>` all three go at once. `.chip` and `.icon-btn` wrote them out
  on 2026-08-07 after the header's Favorites crossed over; `.btn`, `.yesno` and `.tabs` wrote them
  out on 2026-08-11 when backlog 89 turned 818 wrapped buttons into anchors, and without them 166
  controls take the User Agent's underline and 614 labels go left. **Declare what the element is
  doing for you, or the next markup change is a regression you cannot see in the stylesheet.**
- **THE GREY TREE IS A SECOND SYSTEM AND WIDENING THIS ONE DOES NOT REACH IT.** `wireframes/*.html`
  link no stylesheet at all: 104 inline `<style>` blocks carrying **1,605 occurrences of a selector
  keyed to an element type**, including its own `.yesno button`, `.tabs button` and `.cta-bar
  button`. An edit here protects the **163** painted and kit documents, 106 plus 57, counted
  2026-08-12 with `grep -l`, and none of the other 104. **This line said 90 and the 90 counted
  nothing that exists**, which is the same defect as the sentence at the top of this file that this
  one was written to contradict. Any change to what a control IS is two edits, and the grey one is
  the one that gets forgotten.
- **A wrapper and its child are ONE control or they are two, and the accessibility tree is where you
  find out.** 818 anchors each held a button: two tab stops and two hit targets on one visual
  object, on 77 screens per tree, invisible to every sweep that reads the DOM as boxes. Read the
  tree, not the markup: `Accessibility.getFullAXTree` over CDP, and count links whose descendants
  include a button or a tab. It was 32 on one feed screen and it is 0.
- **HIDING A THING FROM THE EYE IS THREE DIFFERENT DECISIONS AND ONLY ONE OF THEM REACHES THE TAB
  ORDER.** `max-height:0` takes a band off the page, `overflow:clip` takes it away from the pointer,
  and `opacity:0` takes its ink; **none of the three makes a control unfocusable**, so the condensed
  category band handed a keyboard **440 focus stops on 88 painted screens at every width**, five per
  screen, each one invisible AND under `aria-hidden="true"`, which is a stop the eye cannot see and a
  screen reader will not name. `display:none` and `visibility:hidden` are the two that do reach it,
  and between them the difference is the box: `display:none` collapses it, so it cannot be used
  where a transition needs the box to stay, and `visibility` is animatable discretely so it holds
  `visible` through the whole collapse and flips at the end. **The mirror is just as easy to write
  and harder to see**: `aria-hidden` on a band that is open and operable tells a screen reader that a
  visible navigation does not exist. **Read this with a Tab walk, never with a stylesheet**, and
  filter the walk by focusing the element and asking where focus landed, because a census of
  everything invisible sweeps in every `display:none` control the rungs turn off and reports 1,063
  where there are 440.
- **A `url()` IN THIS FOLDER IS NOT ONE KIND OF THING, AND WHICH KIND DECIDES WHETHER IT LOADS AT
  ALL.** A `background-image` is fetched no-cors. A `mask-image`, a `@font-face` source and an
  external `<use>` are fetched in CORS mode, **even from their own origin**, and `file://` gives every
  file its own opaque origin, so on a page opened off the disk the CORS ones have nothing to match
  and are blocked. The same `.webp` in the same folder in the same document therefore loads as a
  background and fails as a mask, in Chromium and in WebKit alike, measured 2026-08-13. **The failure
  reads as a property misbehaving and it is a rule applying**, which is why it was diagnosed wrong
  the first time and blamed on `mask-mode:luminance` not being honoured, a thing both engines do
  honour. It has been paid for three times: `assets/icons.js` had to become a script because an
  external sprite drew 0 of 34 glyphs; the trust drawings became `data:` URIs in `trust-art.css`
  after painting a brass rectangle over every tile; and the two preloaded faces still fail this way
  in WebKit, so a disk page in Safari is set in a fallback (`../docs/backlog.md` 147). **If a
  declaration in this folder points outside the file, ask which fetch it is before you ask anything
  else.**
- **A MASK IS NOT A PICTURE AND MAY NOT BE ENCODED LIKE ONE, and a mask LIST is a third thing again.**
  The trust drawings are multiplied by a flat `--color-trust` and held at `opacity` .18 to .5, so the
  composite error is dominated by the colour variation a flat fill cannot carry and not by the codec:
  measured against the shipped tree at q20, q35, q50 and q82, the mean moves **1.06 to 1.01 of 255**,
  and q20 is a quarter of the bytes. **But do not reach for a second mask layer to keep a fade.** The
  bottom layer of a mask list has nothing beneath it, and WebKit intersects it with the transparent
  black there, which empties the whole mask: `mask-composite:intersect` over two layers draws
  correctly in Chromium and draws NOTHING in WebKit. Put the fade in the paint instead, as a gradient
  of the colour being masked, and the drawing keeps one mask layer and no compositing operator.
- **A pointer is a claim, and nothing checks a comment.** Every file here carries a `Stand:` line, and
  from 2026-08-07 to 2026-08-08 **all 42 of them pointed at a file that did not exist**: they named
  the generated per-component pages, which were deleted with the vitrine, and no reader noticed
  because a comment has none. They point at the level page and its anchor now, verified by opening
  all 44 in a browser rather than by grepping for the id. If a line here names a path, open it.

- **`position:sticky` STOPS BEING STUCK WHERE ITS OWN NORMAL-FLOW POSITION IS, AND FOR THE TWO BARS
  AT THE FOOT OF THIS PRODUCT THAT WAS INSIDE THE PAGE.** `.bottom-nav` and `.bet-dock` sat in flow
  between `.app-case` and the footer, so they were stuck only while the reader was above their own
  place in the document. Measured on event-detail.html at 390, document 3,852 tall: flush to the
  viewport bottom to scrollY 1613, **232px up at 2009, 623 at 2406 and 1,266 at the foot**, with the
  dock 56px above that and the sticky header already gone at -582. Three bars stacked in the upper
  third of a phone screen with the trust strip beneath them. The only navigation a phone has, and
  the product's primary action, sliding into the middle of the page. **A sticky element whose
  container also holds the footer is a fixed element that gives up at the end**, and nothing in a
  stylesheet says so: `position:sticky` reads as a promise and the containing block is where the
  promise is actually written. Both are `fixed` now, with `.device` padded and `scroll-padding`
  reserved by the same tokens.
- **THREE FILES WERE WRITING ONE NUMBER DOWN AND NONE OF THEM COULD SEE THE OTHER TWO.** The dock
  offset itself by `52px` to clear a nav measuring **56**, so the two overlapped on every phone; the
  nav is `display:none` from DESK up while the 52 stayed, so from 640 to 759 the dock hung over an
  empty band; and `course-chrome.css` lifted its toggle by `8.25rem`, arithmetic for a dock top at
  120 that was really at 124. Three numbers, one fact, and each was re-measured in its own file and
  correct there. They are `--header-h`, `--bottom-nav-h` and `--dock-h` now, **and each is zeroed by
  the rung block that hides its own bar**, which is what lets a reader ask "how much furniture is at
  the foot of THIS width" and get an answer. The chrome's width query is deleted: its lift is
  `calc(--bottom-nav-h + --dock-h + --space-12)` and is 12 at every width and every root. This is
  the same family as the `759.98px` against `47.5rem` defect two bullets down, met from the other
  side: **that one was a boundary borrowed in the wrong unit, this one was a height borrowed at all.**
- **A CLEARANCE IS PART PADDING AND PART TYPE, SO NEITHER `px` NOR `rem` IS RIGHT ON ITS OWN.**
  Measured with `Page.setFontSizes` at defaults 16 / 20 / 24 on event-detail.html: the nav is
  **56 / 64 / 73**, the dock **68 / 76 / 85**, the header **59 / 63 / 69**. A px token is exact at
  the default and 17px short at 24, which shows a strip of page between two bars that are supposed
  to touch; a `rem` token overshoots, because the padding half does not grow. Both fit a line with
  the same slope, 2.125 per pixel of root, so each token is its px half plus its type half:
  `calc(22px + 2.125rem)` reads 56 / 64.5 / 73 against a measured 56 / 64 / 73. **Verified after: the
  seam between dock and nav is 0.0 / 0.2 / 0.5px at the three roots**, and the chrome's gap is
  12 / 12.2 / 12.5. `course-chrome.css` had already met this and paid for it with an
  over-provision, which is what a single unit buys you when the thing you are clearing is two units.
- **`scroll-padding` DID NOT EXIST IN THIS FOLDER AT ALL, AND THAT IS WHY EVERY FOCUS AUDIT CAME
  BACK CLEAN.** Tab scrolls a target only just into view, so with a 56px bar pinned at the foot it
  lands controls UNDERNEATH it: four of them measured on event-detail.html at 390 at y 816 to 826 in
  an 844 viewport, `elementFromPoint` returning `a.nav-item` at all five sample points, and the
  focused and blurred screenshots of the control's clip **byte-identical**. Every instrument this
  repository had read `outline` and `box-shadow`, found a 2px brass ring on every control, and
  reported zero. **A ring is a claim about what is VISIBLE and the only instrument for it is the
  paint.** It is a floor on `:root` in `base.css` now, for the same reason the focus ring and the
  44px touch floor are floors, and the dock's extra 68 is added by `betpanel.css` through
  `html:has(.bet-dock)` so that a screen with no dock is not padded for one.
- **A TARGET UNDER 24px IS NOT A WCAG 2.5.8 FAILURE AND THIS FOLDER HAS NOW BEEN TOLD SO TWICE.**
  A critique filed 147 targets under 24x24 at 390 as a P1. Re-measured with the pointer asserted
  coarse, which is the first half of the correction `base.css` already carries in prose: **155 under
  24 by SIZE**. Then re-measured against the criterion instead of against the number, which is a
  24px circle centred on the target touching no other target's circle: **0 failures at 390 and 0 at
  1280.** The footer's popular row is 80x16 at 26.1 apart and its legal row 30.8x14 at 41.9, which
  is what `footer.css` measured on 2026-08-13 and wrote down to the tenth. Of the residue, seven are
  1x1 inputs whose target is their own `<label>` and one pair is a link inside a `:modal` dialog
  measured against a link on the inert page behind it. **Read the criterion, not the dimension**, and
  when a file in this folder already carries the measurement, the audit is what gets re-run.
- **AN ATTRIBUTE THAT LOOKS LIKE A MECHANISM IS READ AS ONE, AND THIS TREE HAS NOW SHIPPED TWO.**
  `pattern="[0-9.$]*"` stood on 113 amount fields in a product with 0 `<form>` elements, so it was
  consulted at no moment. **`?side=yes` and `?side=no` stood on 212 feed-card links and 0 of 106
  documents read `location.search`**, so every card in the product was passing a choice to a screen
  that threw it away and typed `sel yes` into its own markup instead. Both read as a working
  mechanism to anyone opening the file, and neither could be found by looking at the thing that
  carries it: the first needed a census of `<form>`, the second needed a census of the READER. **Ask
  what consumes an attribute before believing it does anything**, and if nothing does, it is either
  a defect to wire or a lie to delete.
- **A `role` IS A PROMISE ABOUT THE KEYBOARD AND A `<label>` CANNOT KEEP IT.** Three bars in
  `tabs.css` declared `role="tablist"` and the tree carried 0 `role="tab"` and 0 `aria-selected`.
  Only `.rules-tabs` could be repaired, because only it is made of `<button>`s; `.ed-tabbar` and
  `.ptab-bar` are `<label for>` over hidden radios, and a label is not focusable, which is the same
  fact that cost this folder a 262px brass primary no Tab could reach. **A wrong role is worse than
  no role**, and nothing in a stylesheet can see one. The third of the three was missed by the sweep
  that fixed the other two and caught by re-running the predicate, so **the check is the instrument
  and reading the markup is not**.
- **A MARGIN ON A FLEX CHILD IS ADDED TO THE CONTAINER'S GAP AND NEVER MERGED WITH IT.** This is the
  one place the intuition everybody has from adjacent-margin collapse gives the wrong answer, and it
  cost the narrowest screen double. `.feed .feed-inner` is a flex column with `gap:var(--space-16)`,
  so every child already has 16px under it at every width; `catnav.css` carried a mobile-only block
  putting `margin-bottom:var(--space-16)` on the category strip as well. Measured before it went:
  **32px under the strip at 360 and 390 against 16 at 640, 900 and 1280**, which is the phone paying
  twice for the rhythm the desk pays for once. Nothing replaced it. **Before writing a margin, ask
  what holds the element**: in a flex or grid container the answer is already declared, once, by the
  container.
- **A MEDIA QUERY ADDS NO SPECIFICITY, so an override at a rung has to stand AFTER the declaration it
  overrides and not merely inside a block cut at that rung.** `base.css` opens its page-frame section
  with a `max-width:39.99875rem` block, and the plate's mobile padding put there would have rendered
  nothing at all: `.feed-inner>.cat-nav` is (0,2,0) in both places and the later one wins at every
  width. The cost of getting it right is two blocks at one rung in one file; the cost of getting it
  wrong is a rule that never applies and never says so, which is this folder's most expensive shape
  of defect and the reason `@supports`, `@media` and `:is()` all get read for what they do to weight
  before they get read for what they do to the page.
- **NEVER SPELL A WORDMARK BY HAND, and the two files that did it are the two whose whole job is the
  brand.** `hero.css` and `seo-plate.css` each declared a signature as the body face at 13px in brass
  with the letters typed into the markup and **no mark at all**: 11 placements, the brand tile and the
  SEO plate. `logo.css` states the rule from the other end and had stated it since the day it was
  written, that a brand mark keeps its own drawing and no generic glyph may stand in for it, and the
  places that broke it were not the ones anybody would check. **A component that exists is not a
  component that is reached**: the test is to walk the things the system NAMES and ask which files
  redraw them, rather than to walk the files and ask what they read.

- **AN ACCESSIBLE NAME IS A CLAIM AND NOTHING CHECKS IT AGAINST THE ELEMENT.** The header's brand
  lockup was `<button type="button" aria-label="Yonder - go to Events home">` on all 105 painted
  screens, with no `href`, no `form` and no handler in the tree: it announced a destination and had
  none, and below 640 it is the only target on the left of the row. `header.css` even opened its
  state comment with "the wordmark is a button that goes home". **A name that describes behaviour is
  a test nobody wrote**, and the audits here checked that names EXIST and never that they are true.
  All 221 are `<a href>` now. Where a name says what a control does, read the element.
- **A CONTROL RESERVED FOR A FUTURE COSTS MORE THAN ITSELF, AND THE COST IS IN OTHER FILES.** The
  hamburger was a `<button>` labelled "Menu (reserved for future scaling)" with no handler and no
  drawer, `display:none` below the desk on top of that, so on a phone it did not exist and on a desk
  it did nothing. Deleting it took with it a `display:none` rule, the whole `max-width:39.99875rem`
  block in `header.css` that held nothing else, a symbol out of the one sprite every document loads,
  105 of `.icon-btn`'s 242 placements, the kit specimen that led with it, and a re-measurement of the
  DETAIL rung, which had been cut to buy back the 44px this control was eating. **A placeholder is
  not inert: every file that has to have an opinion about it is paying rent on a decision nobody
  took.**
- **A SECOND FORM OF A CONTROL IS A SECOND PLACEMENT, NEVER A SECOND COPY OF THE CONTROLS, AND THE
  THING THAT DECIDES IT IS `name`.** The phone's filter sheet was going to be a `<dialog>` holding the
  sort and frequency radios, which is one copy per form and therefore two: **a radio group is keyed by
  `name`, so two copies in one document are ONE group with two sources of `checked` and two sets of
  ids**, and the kit already pays for exactly that with its per-theme suffixes. A checkbox and three
  sibling selectors move the BOX the existing panels stand in and leave the panels alone, so the desk
  keeps its two pills and the phone gets a sheet out of one markup. **Ask which elements have to exist
  once before asking what the second form should look like.** The price of the checkbox is a focus
  trap and it is `../docs/backlog.md` 150, written at the moment it was paid rather than found later.
- **A SCROLL CONTAINER CLIPS ON BOTH AXES, AND THE OBVIOUS REPAIR MOVES THE NEIGHBOURS.**
  `overflow-y` computes `auto` the moment `overflow-x` stops being `visible`, so the first row turned
  into a scroller here cut its chips' focus rings, 2px wide at 2px offset, top and bottom. Block
  padding with an equal negative block margin looks like it hands the height back and does not: **the
  negative margin COLLAPSES THROUGH the wrapper in a block container**, so it is handed to the
  neighbours instead, and the row measured 4px from the head and 12 from the grid where the file
  declares 2 and 16. Turn the ring inward, which is what `filters.css` already does for a clipped
  panel. **This is the block-flow twin of the flex-gap trap above, and both are the same question:
  before writing a margin, ask what holds the element.**
- **A HINT ABOUT SCROLL THAT IS PAINTED ON IS A READING OF THE PAINT AND THE QUESTION WAS ABOUT THE
  SCROLL.** A permanent edge fade is wrong twice: it fades the last chip once the row is scrolled to
  its end, and it fades empty space on a row that fits. `animation-timeline:scroll(self inline)` binds
  progress to the element's own inline scroll, **and when the element does not overflow the timeline
  is INACTIVE and the element falls back to its base style**, so declaring the mask only inside the
  keyframes makes "no overflow, no fade" free, with no query and no class. Both engines have it,
  measured. The two colours in a gradient mask are ALPHA and not ink, which is the one place in this
  folder a raw colour is not a colour, and a gradient is the one mask safe from disk because it is
  generated rather than fetched. **And use the longhands**: the `animation` shorthand resets
  `animation-duration`, and a scroll-driven animation wants it left at `auto`.
- **A DEAD RULE WITH A LIVE SENTENCE BESIDE IT IS WORSE THAN A DEAD RULE.**
  `@media(max-width:39.99875rem){.filter-menu{position:relative}}` restated, at a rung, the exact
  value the first line of `filters.css` declares unconditionally: it could not change a pixel at any
  width. `ui-kit/filters.html` carried the prose version of it, *below DESK the panel takes
  position:relative so it opens in the flow rather than over it*, for as long as the rule stood. **The
  rule is what gets deleted and the sentence is what the next reader believes**, which is the same
  species as the `Stand:` lines that pointed at deleted files and the four-widths claim that had never
  been measured at a rung.
- **REACHING FOR THE NEAREST-SOUNDING TOKEN IS HOW A PRODUCT GROWS TWO ANSWERS TO ONE QUESTION.** The
  filters sheet's backdrop was `--scrim`, whose own comment in `tokens.css` says what it is for, the
  COURSE DRAWER, which is chrome. It is `--black-a30`, and 30 per cent of black over graphite darkened
  nothing: the page behind the sheet was visibly undimmed and the surface did not read as modal. The
  product answers this once already, in `dialog.app-dialog::backdrop`, at `--shadow-ink-45`. **Before
  taking a role by its name, find where the product already answers the same question.**
- **A CHIP FACE IS A PADDING AND AN ICON BUTTON IS A BOX, SO AN ELEMENT MAY NOT WEAR BOTH.** The
  phone's filter control was given `.filters-btn` in the summary's chip face and then `.icon-btn` as
  well: `iconbtn.css` sets 36 x 36, and `filters.css`, imported later as a molecule over an atom, set
  `padding:8px 20px` inside it. **40px of padding in a 36px box leaves a negative content box**, and
  the mark rendered as a two-pixel dot in a circle that still looked like a button. Nothing errored,
  nothing was empty, and no stylesheet reading finds it. This is the twin of the note below about a
  class running past every selector written for its element: **two faces on one element run it past
  both, and the one that loses is whichever the import order says.**
- **THE QUESTION THAT FINDS OLD DEFECTS IS "IS THIS NEW RULE TAKING ITS VALUES FROM THE REGISTER".**
  Auditing one new sheet against the system turned up two things older than it and invisible from
  inside either file. **The `Reads:` line was incomplete in 43 files of 43**, measured by stripping
  comments and diffing every `var()` in the body against the header, and the folder did not even
  agree what the line was FOR: `seo-plate.css` listed 21 tokens and every one a colour, while
  `logo.css` listed `--space-8` and `--weight-bold` beside its inks. **And the product has four
  answers to "a surface that must not exceed the viewport"**: `92vh`, `88dvh` and two rails at
  `calc(100svh - 120px - var(--space-16))`, of which only the rails carry the `vh` then `svh` pair
  that a phone needs. A new rule wrote a fifth, `80svh`, and gave it back. `../docs/backlog.md` 152,
  closed the same day, and 153.
- **`Reads:` IS THE COLOUR REGISTER AND NOTHING ELSE, AND THE ANSWER WAS ALREADY WRITTEN UNDER IT.**
  Every header in this folder closes with `Colour goes through a role, geometry straight from a
  primitive`, so the line above it lists the semantic roles the file reads and does not list
  `--space-*`, `--radius-*`, `--text-*` or `--z-*`: a radius has nothing for a theme to override, so
  there is nothing about it to register. **43 of 43 complete, 0 stale**, and **11 files carry no such
  line at all and every one is right to**: `tokens.css` defines the roles, and the other ten read 0
  roles between them. Six of the ten are the whole of `patterns/`, so **the rung's invariant that a
  pattern carries no colour is now visible as the ABSENCE of a line** rather than as a claim in prose.
- **A COUNT TAKEN BY MATCHING A STRING IS A COUNT OF THE STRING.** The sweep that opened the row above
  matched `Reads:` anywhere in a file, and `tokens.css` carries those six characters in a comment on
  line 1184, so **the file that DEFINES the roles was filed as the worst offender at failing to
  declare them**, 121 of 121. The published number was 44 and the true one was 43. Read the header
  block, not the file, and this is the same defect as a selector that matches nothing agreeing with
  every hypothesis, met from the other side.
- **TWO CONTROLS THAT SAY THE SAME WORDS ARE ONE CONTROL TO A READER, WHATEVER THEIR FACES DO.** The
  feed's category strip ROUTES and its category sub-filter NARROWS, and they carried the same five
  words a hundred pixels apart. The faces already differed, a mark on a plate against a bare chip,
  and it was never enough: **at that distance a person compares by reading.** The repair was the
  label the row never had, `Show:`, and the argument for it is that the feed's other two filters have
  been `Sort:` and `How often:` since the day they were written. **An unlabelled control announces
  nothing about what it acts on, so it is read as whatever it looks like.** Renaming the chips was
  refused: they are the product's four categories, and a second set of names for one taxonomy is the
  more expensive mistake.
- **BEFORE UNIFYING FOUR VALUES, CHECK THAT THEY ANSWER ONE QUESTION.** The product had four caps for
  "a surface that must not exceed the viewport" and it was two questions: a modal SHEET caps at a
  fraction of the viewport, a sticky RAIL caps at the viewport MINUS its own top offset. The three
  rails were already one answer, `calc(100svh - X - var(--space-16))`, one formula with a parameter.
  The three sheets were not: `92vh`, `88dvh`, `92svh`, two numbers and two units, of which one had an
  argument beside it. They read `--sheet-cap:92svh` now, and **`svh` is the unit a fixed modal wants**
  because it is the SMALL viewport and the surface then never resizes under a reader's thumb, where
  `dvh` moves as the browser bar retracts and `vh` lets the tail sit behind it. **Unifying the sheets
  with the rails would have been a fifth number, not fewer**, and the token says so where the next
  tidy-up will look.
- **CENSUS THE UNIT, NOT THE ARGUMENT, OR THE FILE THAT NEVER JOINED THE DISCUSSION IS THE ONE YOU
  MISS.** Backlog 124 closed by naming the three files that HAD written the `svh` argument and the
  one full-page shell that had not, and it was right about all four. It was a census of who had
  spoken plus the shell, and `course-chrome.css` is neither, so `.sidebar{height:100vh}` stood for
  two days after the row was marked closed. Taken from the comment-stripped source on 2026-08-15:
  **seven viewport-height sites in this folder, six of them `svh` or a pair, and the seventh was the
  drawer.** And it is the worse case of the two, because `min-height` only ADDS room while `height`
  on a fixed SCROLL CONTAINER puts the container's own bottom off screen: measured in both engines
  at 390x640 with the panel forced to 700 to stand in for a 60px browser bar, **the last link in the
  roadmap sits 38px below the visible edge with no scroll left to reach it**, and 0 links are cut at
  640, which is the reading moving when the input moved.
- **THE `vh` FALLBACK PAIR CANNOT BE WRITTEN FOR A TOKEN, AND THE OBVIOUS TIDY-UP DELETES A CAP.**
  Four sites write `vh` then `svh` as a pair and it works because both halves are DECLARATIONS: an
  engine that cannot read the second unit throws that declaration out at parse time and the first
  survives. **A custom property is not parsed that way.** It accepts any token sequence, so the unit
  is never rejected, and `max-height:92vh` followed by `max-height:var(--cap)` where `--cap` holds an
  unreadable unit computes to **`none`** in both engines, not to 92vh, because `var()` is valid at
  parse time, wins the cascade, and fails only at computed-value time, where the fall is to the
  property's initial value and never to the declaration above it. So a reader who meets `.device`'s
  pair and `--sheet-cap`'s single value and makes them agree in the obvious direction takes the cap
  off three sheets. **So the folder could be made to say one thing only by DROPPING the pair, never
  by adding it, and backlog 155 was closed that way on 2026-08-15**: five sites, one sentence, and
  the cost named rather than waved at, an engine older than Safari 15.4 of March 2022 or Chrome 108
  of November 2022 losing a minimum height on `.device` and a maximum on three rails that still
  scroll. `tokens.css` keeps the proof beside the token, because the trap is now a trap only for
  somebody putting a pair back.
- **A PROPERTY ASSIGNMENT FIRES NO EVENT, AND THIS FOLDER HAS NOW PAID FOR IT TWICE IN ONE DAY.**
  Setting `input.checked` from script updates the input and notifies nothing, so a `change` listener
  is not a listener for the script's own writes. The filters sheet reset a radio and went on printing
  the old word until the event was dispatched; the same sheet's focus trap closed on Escape and left
  **26 elements inert behind it**, on every screen, because Escape sets `checked` and the seal was
  lifted by a `change` handler. **Give every path in and out ONE function and call it, rather than
  hoping the DOM will tell you about a change you made yourself.**
- **A `<label>` IS NOT A TAB STOP.** It is exactly right for a pointer and invisible to a keyboard,
  so a 262px brass primary reading `Show results` was a control Tab never reached and no rule in the
  system could say so. Read it with a Tab walk; a stylesheet cannot see it and neither can a diff of
  the markup. **An action is a `<button>`; a `<label for>` is a pointer path to a control that
  already exists.**
- **A BOUNDARY BORROWED FROM ANOTHER FILE HAS TO BE BORROWED IN THAT FILE'S UNIT.**
  `course-chrome.css` lifts the review toggle below `759.98px` and says in its own comment that this
  is where `betpanel.css` docks the panel, and the dock is cut at `47.5rem`. Two numbers written the
  same day to be one rung, equal only at a 16px root: at a 20px default the toggle crosses the dock
  by 4px at three widths, at 24 by 4px at four and 5px at a fifth, measured with `Page.setFontSizes`
  because that is the only thing that moves a rung. **A shared boundary written twice in two units is
  a boundary that agrees by coincidence.**
- **AN EXIT THAT ONLY EXISTS IN THE MECHANISM IS NOT AN EXIT.** The filters sheet closed on the
  scrim, on Escape and on a cross in its head, and shipped with a band of empty surface under its two
  rows: the first two are invisible by definition, and the third is 44px in a corner that the course
  chrome's own toggle sits on top of. **An empty band under a control reads as a screen that has not
  finished rather than as a choice that has been made.** And name the control for what pressing it
  does: every radio in that sheet is live, so `Apply` would have named a step that does not exist,
  which is the same defect as an accessible name promising a destination the element does not have.
- **A SIGNAL WITH NO ROUTE OUT OF THE STATE IT SIGNALS IS HALF A CONTROL.** The dot that says a
  filter is off its default shipped an hour before the `Reset` that clears it, and in between the
  only way back was to open the sheet and find both defaults again in two separate lists.
- **A CONTROL'S FACE IS A DECISION ABOUT THE SURFACE IT STANDS ON.** The same two `<summary>` chips
  that are right in a toolbar row read as two large empty buttons floating on a panel the moment they
  are put in a sheet. A sheet row is full-bleed, its edge is the hairline it shares with its
  neighbour, the whole row is the target, and its type is not the toolbar's 11px, because a sheet is
  the surface a person came to READ. Reusing the markup was correct; reusing the face was not.
- **A TEXT NODE BESIDE AN ELEMENT BECOMES AN ANONYMOUS FLEX ITEM, WHICH IS A FREE LAYOUT WITH NO
  MARKUP CHANGE.** `<span>Sort: <span id="sortCurrent">Trending</span></span>` is a text node and an
  element; `display:flex` on the outer span makes the text an item, so `space-between` puts the label
  left and the value right on 88 documents without touching one of them. **Before adding a wrapper,
  ask whether the box you want already has two children.**
- **A PLACEMENT FILE NARROWS ITS OWN RULE; IT DOES NOT OVERRIDE SOMEBODY ELSE'S FACE.** The moment
  the lockup became an anchor, four selectors in `footer.css` reached it, all (0,1,1) or better
  against `.logo`'s (0,1,0): muted ink at rest, brass on hover, an underline, a pressed ground. The
  fix is `:not(.logo)` on the footer's four, not a repaint in the footer's voice, and it is the same
  shape `.bt-by` and `.seo-by` take by declaring no ink at all. **Adding a class to an element runs
  it past every selector in the system that was written for that element type**, which is the half of
  a markup change that a diff of the markup does not show.

- **A PAIR OF ORDINALS IS A CLAIM THAT THERE ARE TWO, AND A LONE ELEMENT IS BOTH OF THEM.**
  `card.css` painted `.ed-prob-big .prob:first-of-type` green and `:last-of-type` red, which is
  right for `YES 38% NO 62%` and is a trap for `Leading: JD Vance 41%`. One span matches both
  selectors at equal specificity, so source order decided it and the later rule won: **the market's
  leading candidate was drawn in the ink that means the losing side**, on the two multi screens
  where there is no second figure to compare it against. The fix is to make the outcome ink ask for
  a PAIR - `:first-of-type:not(:last-of-type)` - so no source order can reach a lone figure, and to
  give `:only-of-type` its own answer. **The stand could not have caught it**: all 8 placements of
  `.ed-prob-big` in `ui-kit/` carry the pair and 0 carry the single, so this is the chosen NO again
  in a different file. An ordinal selector is a statement about the SET, and the set has to be
  checked before the ordinal is written.
- **A GRID LINE IS A NUMBER OR IT IS DECORATION, AND DECORATION THAT LOOKS LIKE A SCALE IS THE
  WORST OF THE THREE.** The hero chart ruled four lines at y=40, 80, 120 and 160 of a 190-unit box.
  The mapping is solvable from two points the chart itself draws - the YES line is at 97 for 50 per
  cent and at 134.9 for 38 - so the lines stood at **68.05, 55.38, 42.72 and 30.05 per cent**.
  Nobody could read a value off them and the ruled paper said they could. Re-keyed so that
  y = 220 - 3p, the decades land on 10, 40, 70, 100 and 130 and every drawn point becomes an integer
  for the first time. **The tell was in the building the whole time**: the event-detail chart has
  carried a labelled y-axis since Stage 08, so the product drew one scaled chart and one unscaled
  one, and the unscaled one was the flagship.
- **A MAGNITUDE AND A PROBABILITY SHARE NO AXIS, SO LABELLING ONE MAKES THE OTHER A LIE.** Volume in
  dollars sat inside the same plot as the odds in per cent, and the moment the per-cent numerals
  went in, the volume ribbon read as a third line hovering near 30. It moves into a strip of its own
  under `.hf-split` and the caption says it has no scale. **Adding a scale is not free: it makes
  every other mark in the box a claim about that scale.**
- **`ch` IS THE WIDTH OF A ZERO, WHICH IS THE RIGHT UNIT FOR A MONO GUTTER AND THE WRONG ONE
  EVERYWHERE ELSE.** `--measure` had to leave `ch` on 2026-08-12 for this reason; the chart's numeral
  column is the case where it is exact, because on a monospace face every glyph is one advance.
  Measured: `3.5ch` gives 23.1px and holds a 20.8px "70%" in the paint, over `http://` and over
  `file://`, in both engines. **The grey tree has no mono face, so the same declaration gives 19.25px
  for a 21.16px label, and that is the lesson stated from the other side.** It is NOT a defect, and
  the predicate that called it one is the twin of `scrollWidth > clientWidth`: the criterion is
  whether a numeral is CLIPPED or crowds the plot, and measured on both trees, both engines and five
  widths it is **0 clipped and 0 overlapping, worst left margin 15.09px inside the clipping
  ancestor**. A box wider than its column is not text that has been cut off.
- **INJECTING A STYLESHEET STARTS A TRANSITION, AND THE VALUE AT t=0 IS THE VALUE IT IS LEAVING.**
  The before-and-after census of outcome colour on the feed reported `ground 22 -> 22, edge 0 -> 0,
  identical painted area`, over an edit that took a tint off 32 buttons. `addStyleTag` had applied
  correctly; `.yesno :is(a,button)` carries `transition:background var(--dur-fast)`, and two
  `requestAnimationFrame`s into a 150ms transition the computed background is still the old one.
  Freeze `transition` and `animation` FIRST, then inject, then read: the same census then returned
  **ground 54 -> 22, edge 32 -> 0, 220,689px2 of outcome colour down to 18,025**. This is the
  root file's "a reading that does not move when the input moves", met from the direction where the
  instrument is the thing that moved and the page is not.

- **`aria-busy` IS A PROPERTY OF A REGION AND NOT A MESSAGE, so 19 loading screens said nothing at
  all.** Every one of them marked the region busy and marked the shapes decorative, which is
  correct and is not an announcement: a person who cannot see 42 pulsing rectangles was told
  nothing. `.sk-status` is one hidden sentence per busy region, `role="status"` on its own `<p>`,
  and **the `<p>` is the decision**. Putting the live region on `.grid` itself would make twelve
  event cards the thing announced the moment the skeletons are replaced, which is the feed read
  aloud to somebody who asked whether it had finished. **Hidden from the eye is not hidden from the
  tree, and this file has now paid for both directions of that on one day**: `clip-path:inset(50%)`
  keeps the status line in the tree at 1x1, while `color:transparent;font-size:0` on `.thumb` kept
  the grey tree's "thumbnail placeholder" label in the tree on 105 screens, 24 `StaticText` nodes on
  the feed alone.
- **QUERY THE TREE, NOT THE ELEMENT: `uninteresting` on a wrapper does not prune its text.** The
  first check of the thumbnail label read the `<span class="thumb">` nodes through CDP and came back
  `ignored=true, reason=uninteresting` on all of them, which reads as clean. The full tree has the
  StaticText child standing, not ignored, 24 of them. **And the same instrument cleared a finding
  the other way in the same run**: 4 SVGs on `how-it-works.html` are written with no `aria-hidden`
  and all four are ignored anyway, `reason=ariaHiddenSubtree`, because the span around them carries
  it. A grep over the source cannot see either result.
- **A COMMENT IS NOT A SELECTOR SEPARATOR, AND THIS REPOSITORY HAS NOW PAID FOR "A COMMENT IS NOT
  INERT" TWICE.** `yesno.css` lost `display:flex` on 2026-08-10 to a comment terminator; this pass
  inserted a rule into 19 grey files immediately before `.sk-thumb` and turned
  `.card.skeleton .sk-thumb` into `.card.skeleton <comment> .sk-status`, a descendant selector
  matching nothing. It failed silently and the browser said 16px where the rule said 13. **Anchor an
  insertion on a comment or a brace, never on the second half of a compound selector**, and read the
  computed value back before believing the edit landed.

- **A TONE THAT TWO SURFACES OF THREE WEAR IS NOT A TONE THE SYSTEM LACKS, IT IS ONE SURFACE THAT
  NEVER JOINED.** The critique read "there is no error tone" and the true half of that is only that
  there is no error HUE, which is a settled consequence of green being YES and brass being the
  brand. Measured before the edit: `.state-block.state-problem` and `.toast.toast-error` both took
  `--border-notice`, one danger triangle and a 600 message, and `.inline-error` took the plain
  hairline, **0 marks and 400**. Same ground on all three. **The quietest was the one that says a bet
  did not register**, quieter than the `.reconcile-box` two lines above it in the same panel, which
  frames a price CHANGE in brass. Before designing a tone, census the surfaces that should already
  be wearing it: the answer was three declarations, not a new colour.
- **A HEAD ANSWERS FOR THE MOMENT ITS DIALOG NAMES, NOT FOR THE WORST LINE INSIDE IT.** Two dialogs
  wore the full brass plate head, radial corner and 210px glow, over "Card declined" and
  "Verification rejected", and `platehead.css` had already argued the fix for a different moment:
  the loss head has no glow "since inheriting the face now means inheriting a brass one". They are
  one selector rather than two faces. **The other six dialogs carrying an error keep the brass and
  each was read before it was left alone** - a sign-in sheet is still offering to sign you in, a
  provider conflict is a guard, and `win-error` is a WIN whose share card failed. A grep for
  `inline-error` would have repainted all eight.

## Where the record is

`../DESIGN.md` for the visual language, `../docs/decisions.md` for why a thing was decided, and
`../docs/kit-archive/` for the per-component writing of the deleted vitrine: 48 pages of what each
component IS, its rule and its anti-rule. Nothing reads that folder; it is there so the same
measurement is not taken twice.
