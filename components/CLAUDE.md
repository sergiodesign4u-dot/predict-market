# components/ - the system itself

This folder IS the design system. 50 stylesheets, 7,034 lines (re-counted 2026-08-10: it said 51 and
5,651, and the 51st was `account.css`, deleted on 2026-08-08 by backlog 63), `tokens.css` plus one file per
component, all reached through `index.css`. The 210 screens in `ui-visual/` and `wireframes/` link
`index.css` and nothing else, so **an edit here reaches every screen at once and no screen can
override it.** There is no build step and no gate: what you write is what ships.

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
- **A component may not invent a width.** There are three rungs, named by what arrives at them:
  **640** the desk, **760** the detail's second column, **900** the rail beside the content. If a
  file needs a break that is not one of them it is a one-off and says so in a comment beside itself,
  or it is a fourth rung and gets named in the ladder in `tokens.css` FIRST. A breakpoint cannot be a
  token: a media query condition does not read a custom property and there is no build step here, so
  the ladder is kept by being read, and each of the 32 media rules names its rung. The alternative
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
  painted screens: a pattern is only consulted at form validation, so it validated nothing at any
  moment and read as a constraint to everyone who opened the markup. The other 8 did not carry it
  and the two trees disagreed about which. **Absent and inert are the same amount of nothing**, which
  is why the divergence went unnoticed. The field is `type="number"` now and the browser is the
  guard, verified by typing into it.
- **A scope is a claim about where the product IS, and it is the claim least likely to be checked.**
  `.app-case` opened **415 selectors in 36 of the 50 files, 31 per cent of everything declared here**,
  and it existed to keep these rules off the course chrome. Measured across 106 painted screens with
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
- **A pointer is a claim, and nothing checks a comment.** Every file here carries a `Stand:` line, and
  from 2026-08-07 to 2026-08-08 **all 42 of them pointed at a file that did not exist**: they named
  the generated per-component pages, which were deleted with the vitrine, and no reader noticed
  because a comment has none. They point at the level page and its anchor now, verified by opening
  all 44 in a browser rather than by grepping for the id. If a line here names a path, open it.

## Where the record is

`../DESIGN.md` for the visual language, `../docs/decisions.md` for why a thing was decided, and
`../docs/kit-archive/` for the per-component writing of the deleted vitrine: 48 pages of what each
component IS, its rule and its anti-rule. Nothing reads that folder; it is there so the same
measurement is not taken twice.
