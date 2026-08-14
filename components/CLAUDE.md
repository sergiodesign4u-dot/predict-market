# components/ - the system itself

This folder IS the design system. **54 stylesheets, 9,802 lines**: 48 here and 6 in `patterns/`,
re-counted 2026-08-14 by `cat components/*.css components/patterns/*.css | wc -l` after the filters
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

**163 documents link `index.css` and nothing else, and they are not the ones this line used to
name.** Counted 2026-08-12 with `grep -l`: **106 of 106** documents in `ui-visual/` and **57 of 57**
pages in `ui-kit/`. **0 of the 104 in `wireframes/` link any stylesheet at all**, and they carry 104
inline `<style>` blocks instead, which this file already says out loud further down and said the
opposite of here for as long as both sentences stood. So **an edit here reaches every painted screen
and every kit page at once and none of them can override it, and it reaches the grey tree not at
all.** There is no build step and no gate: what you write is what ships.

**106 and 105 are both right and they count different things, so every number below says which.**
`ui-visual/` holds **106 documents**; **105 of them are screens** and `overview.html` is the index of
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
- **A MEDIA QUERY MAY NOT STAND IN A SCREEN FILE, EVER**, and it is written here and in
  `ui-visual/CLAUDE.md` both, because a rule kept in one place is a rule half the hands never meet.
  Adaptation lives in a token, a component, a pattern or the shell. Measured at Responsive step 4:
  **32 width queries in this folder, 0 in any of the 106 documents in `ui-visual/`.** It was 33, then
  35 on 2026-08-12 when the outcome row and the outcome pair each took one at the desk rung, and 33
  again on 2026-08-13 when backlog 129 deleted the one in `tokens.css` and the one in `card.css`
  **and put nothing in either place**: the two page insets ramp with a `clamp()` now and the bookmark
  pull is unconditional. **A query that leaves with no replacement was answering a question its
  subject never asked.** The counterpart
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
  the ladder is kept by being read. **There are 32 width rules, and this line has said 33, then 35,
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
  bottom nav, the footer and all 337 dialogs stand outside it, so what the wrapper actually did was
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

## Where the record is

`../DESIGN.md` for the visual language, `../docs/decisions.md` for why a thing was decided, and
`../docs/kit-archive/` for the per-component writing of the deleted vitrine: 48 pages of what each
component IS, its rule and its anti-rule. Nothing reads that folder; it is there so the same
measurement is not taken twice.
