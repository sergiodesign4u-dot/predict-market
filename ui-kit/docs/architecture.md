# System architecture

How the design system is put together, what each level is allowed to hold, and where a change goes.
Written in step 3 of the Tokens + Components stage, kept current from here on. No em dash.

---

## Two folders, two jobs

| Folder | What is in it | Who links it |
|---|---|---|
| `components/` | the CODE: `tokens.css`, `base.css`, one file per component, `index.css` as the single entry | the product (`ui-visual/*.html`) and the stand |
| `ui-kit/` | the VITRINE: a page per component, `tokens.html`, the hub `overview.html`, the registry `_nav.js`, the stand-only `_page.css`, and `docs/` | a person in a browser |

`components/` can be lifted into another project as it stands: one link to `index.css` and the system
travels. The stand does not come with it, because the stand exists to work ON the system, not to run it.

Two rules follow, and both are checked in step 7:

- a product class must never be styled in `ui-kit/_page.css`;
- a stand class (`.tk-*`, `.ck-*`) must never appear in `components/`.

---

## Two levels of tokens

`components/tokens.css` holds both, in one file, in this order.

**Primitive** is a raw value with no opinion: `--graphite-830`, `--brass-400`, `--space-12`,
`--radius-10`, `--text-13`, `--dur-quick`. It answers "which value".

**Semantic** is a role: `--bg-surface`, `--text-muted`, `--color-action`, `--outcome-yes`,
`--shadow-ink-45`. It answers "why this colour is in this place". Every role points at a primitive
through `var()` and carries the usage it was read from.

### Foundations are one page, with several doors

The course asks for `colour.html`, `typography.html`, `geometry.html` and `icons.html`. We build one
of the four, and the reason is the rule above it: one component is one css file, one page, one
registry line. Colour, material, geometry, type and motion are all generated out of
`components/tokens.css` and already render as sections of `tokens.html`. Four hand-built pages beside
it would be a second answer to the same question, and would disagree with it the first time a token
moved. So the hub carries five **doors** into `tokens.html#colour`, `#material`, `#geometry`, `#type`
and `#motion`, and there are no separate pages behind them.

`icons.html` is built, because it is the one foundation that is not a value. An icon is markup, no
token file can hold it, and until this step the sprite existed only inside `kit.html`, which is why
43 icon references across the stand pages pointed at symbols that were not in the document.

This is a deliberate deviation, of the same kind as the non-alphabetical import order above.

There is no component level (`--button-bg`, `--card-radius`). On a product this size it would only add
a third round of renaming: to change the colour of a button you would walk three files instead of one.
It becomes justified when a component has to differ from the role systematically (a brand theme over a
product theme, several products on one system), which is a later stage if the product gets there.

### What a component may read

| Kind of value | Reads from | Why |
|---|---|---|
| colour | **semantic role only** | colour is what a theme and a rebrand move. A component that reads a primitive colour is a hole, and the first theme finds it |
| geometry: space, radius, control size, container | **primitive directly** | a radius has nothing for a theme to override. It just repeats |
| type: family, size, weight, leading | **primitive directly** | same reason |
| motion: duration, easing | **primitive directly** | same reason, and the Animation stage will systematise them |

### The exceptions, written down so they are not mistaken for sloppiness

- **Decorative one-off geometry stays literal** inside a component: the 224px blur blob behind the
  how-it-works hero, mask radii, background sizes, SVG stroke widths, letter spacing. These are not a
  scale, and a token would only hide what the number is doing.
- **Composite values keep their own numbers**: the offsets and blur radii inside a `box-shadow`, the
  stops inside a gradient, `transform` distances. The colour inside them still goes through a role.
- **Negative values stay literal** (`margin:-8px`), because the scale has no negative steps.

---

## Naming

Roles are read out of the product, not borrowed. The audit (`tokens-audit.md`) lists, for every role,
the declarations it grew from. Names come from what the Vault actually is: `--bg-plate`, `--bg-slab`,
`--edge-groove-dark`, `--border-brass`, `--outcome-yes`, `--result-won`. Names from other people's
systems (`--color-primary`, `--surface-2`, `--gray-500`) are not used, because they describe someone
else's product.

Two rules that look contradictory and are not:

- **Two roles, two tokens, even when the value matches today.** `--color-action` and `--color-trust`
  are the same brass right now. They answer different questions and can move apart, so they are two.
- **One place is not a role.** A colour that stands in exactly one declaration stays a primitive until
  it repeats. A role that nothing reads is noise that hides the real ones.

The depth family (`--shadow-ink-40` to `--shadow-ink-90`, `--bevel-*`, `--tint-brass-06` to `-60`) is
deliberately mechanical: one role per ink depth. Light is a colour like any other, and a light theme
turns every highlight into a shadow, so these cannot stay literal inside the components.

---

## The entry point and the order of the cascade

`components/index.css` imports `tokens.css`, then `base.css`, then every component. A screen links
that one file. A new component is added there once, instead of being wired into 76 screens.

**The component order is not alphabetical, and that is deliberate.** These files came out of one flat
kit where the cascade was a straight line: the grey structural layer first, the Vault skin on top.
Several components carry rules of equal specificity that touch the same element (an `h3` inside a
chart head and an `h3` inside a section; a dropdown and a filter panel), and there the file imported
last wins. The import list therefore repeats the order in which those rules were layered in the kit.
Alphabetical order would have changed four outcomes silently. If a future component has no such
overlap, put it anywhere; if it does, put it where its cascade needs it and say so in a comment.

A rule whose selector list spans several components is split per component, in place, so each file
keeps the rule at its original position in the cascade.

---

## How a specimen is made

A component only looks like itself inside the markup it ships in. The painted product wraps every
screen in `<div class="device"><div class="app-case">`, and 423 rules across `components/` are scoped
under `.app-case`: the two-stone plates, the chip family, the condensed strip. A fragment lifted out
of that wrapper renders as raw browser default, which is what the first version of these pages did.

So a specimen is never a fragment. It is a **labelled block of the frozen kit**, taken whole, with
the ancestors it already had.

| File | Owner | What it is |
|---|---|---|
| `ui-kit/kit.html` | frozen | the source. 12 sections, 47 labelled blocks, each already staged in its real context, dialogs already open, the sprite. Read, never written |
| `ui-kit/specimens.extra.html` | hand | blocks for the three things the kit does not stage: the page frame, the roadmap sidebar, the cookie banner. Same shape as a kit section |
| `ui-kit/specimens.map.json` | hand | the curation: which block becomes which specimen, under what title, at what width, on whose page |
| `ui-kit/specimens/<id>.html` | generated | one standalone page per specimen |
| `ui-kit/specimens/index.json` | generated | the manifest the page generator reads |

A map entry can take the whole block or `pick` one element out of it. A pick keeps the element's
**real ancestor chain**, copied from the kit byte for byte, and drops only its siblings, so every
descendant selector that painted it there still paints it here. `unwrap` removes a named wrapper from
that chain, and exists for exactly one case: a tab panel is `display:none` until a radio outside the
component is checked, and the radio is not part of the component being shown. `set` puts an attribute
on an element the way the product puts it there (the `open` a summary toggles, the `checked` a tab
radio carries), and every use of it is captioned on the page.

### Why each specimen is a page, and why it is framed

Each specimen is a real document, loaded in an `<iframe>` at a declared width.

- **The width is the point.** `.bottom-nav` is `display:none` above 640px, so on a desktop stand page
  the old bottom-nav specimen was an empty box. In a 360px frame it simply shows itself, because the
  media query is telling the truth. Same for the bet dock and the bottom sheet.
- **The stand cannot leak in.** A specimen page links `components/index.css` and `_specimen.css` and
  nothing else. `_page.css` is not there to reach it.
- **Sticky stays sticky, ids stay unique.** Four specimens can each carry `#edtab-comments` without
  colliding, because they are four documents.
- A frame reports its own height by `postMessage`, which crosses origins and therefore works from
  `file://`, where reading the frame document from the parent does not. If the column is narrower
  than the declared width the frame is scaled down rather than squeezed, and the label says by how
  much.

`ui-kit/_specimen.css` is the staging layer: it stops page-level behaviour (a header that sticks to
the viewport, a dialog that positions itself against the page, a `min-height:100vh` canvas) from
fighting a one-component frame, and it carries the `.kit-*` helpers the kit uses to lay several
variants side by side. It restyles no product class beyond that, and the two rules that do touch one
say why in a comment.

### States

Hover and focus are not faked with a stand class. The frames are live, so a hover is a real hover;
next to them the page prints the state rules **read out of the component's own file**, so what moves
is quoted rather than described. The states that live in the markup (`open`, `checked`,
`aria-current`, `.sel`, `.scrolled`, `.skeleton`, logged out) are shown as separate specimens and
captioned with how the product sets them.

### Three rules a specimen has to obey

1. **It shows product markup, not invented markup.** The first version of the base specimen carried
   a bare `<a>` and a bare `<ul>` to illustrate the reset. Nothing in `components/` styles either, so
   the page showed browser blue and browser bullets and demonstrated the browser rather than the
   system. If the system does not style something, the specimen does not contain it.
2. **The declared width is the smallest one at which the component looks like itself**, not the width
   of the screen it was cut from. A three-button row in a 720px frame is mostly empty canvas.
3. **The frame draws nothing.** No border, no corner radius, no background of its own: all three
   cut into the components, because a rounded corner clips a control that sits flush to the edge of
   its viewport and a hairline draws a line across it. What a specimen stands on is decided by the
   specimen. A layout brings the product's own stone and plate, because that is the screen. A single
   control is wrapped in `.app-case` alone, which is transparent, so a button stands on the page
   rather than on a rectangle of stone it would never sit on in the product. `canvas: false` in the
   map is what says so, and it is set for the button rows, the dialogs, the toast, the toggles, the
   icon sets and the separator demo.

   When the column is too narrow the frame scales the whole page down and the label says by how much.

### Why a zero in the Classes table is not a verdict

The table counts how many painted screens carry each class. A zero means one of five different
things, and the last column says which: `runtime` (a script creates it, like the odds bar the feed
builds from the probability text), `kit` (a real component the product has not adopted, like the
`.btn-*` size ladder), `wireframe` (the grey-era version of a block the paint replaced), `docs` (a
course page carries it, and those pages do not load the system), or `unused`. Only `unused` is a
deletion candidate. All five lists are generated into `docs/coverage.md`.

Nothing is deleted from `components/` while the painted screens still carry their own inline styles:
until step 5 puts them all on `index.css`, a class can look unreachable from here and still be
styled locally on a screen. Step 7 acts on the list.

## How to add a component

Five things, or it does not exist:

1. `components/<name>.css` - the file, with the header comment: the roles it reads, its stand page,
   the screens it stands on.
2. a block to show it: either a labelled block already in `ui-kit/kit.html`, or a new one in
   `ui-kit/specimens.extra.html`.
3. an entry in `ui-kit/specimens.map.json` pointing at that block.
4. a line in `ui-kit/_nav.js` - the registry that renders both the hub cards and the side panel.
5. a row in `ui-kit/docs/inventory.md`.

`ui-kit/<name>.html` is not on the list because it is generated. So is `docs/coverage.md`, which
reports what each component actually renders.

The build is three commands, in this order, all idempotent, none of which touches `components/` or
`ui-visual/`:

```
python3 ui-kit/_extract_specimens.py     # blocks  -> specimens/ + selftest.html
python3 ui-kit/_gen_component_pages.py   # css     -> 38 pages + overview + _nav.js + coverage.md
python3 ui-kit/_gen_icons_page.py        # sprite  -> icons.html
python3 ui-kit/_check_kit.py             # the gates
```

`ui-kit/tokens.html` is generated separately by `ui-kit/_gen_tokens_page.py` from
`components/tokens.css`.

A block in the kit with no map entry is a **build failure**, not a silent omission, and so is a map
entry pointing at a block that no longer exists. A block we deliberately do not show is listed in
`skip_blocks` with the reason: there is one, the input-states row, which is stand markup demonstrating
no product class at all.

---

## Where a change goes

| The change | Where it goes | What it does |
|---|---|---|
| a colour in a role (the action brass, the muted text) | `components/tokens.css`, semantic level | reaches every component and every screen at once |
| a raw value (a graphite step, a new spacing step) | `components/tokens.css`, primitive level | reaches every role that points at it |
| how one component looks | `components/<name>.css` | reaches every screen that carries it |
| what a component is made of (markup) | the stand page in `ui-kit/` and every screen in `ui-visual/` that carries it | markup is not centralised, the class is |
| how the stand itself looks | `ui-kit/_page.css` | never `components/base.css`. The product is not bent to fit the vitrine |

A change made on one screen is a desync by definition. If a screen needs something the component does
not have, either the component grows a variant class or the screen is wrong.

---

## The inheritance from the flat kit

- `ui-kit/kit.css` is the flat file this system came out of. It stays until the painted screens move
  onto `index.css` (step 5), then it goes; git remembers it.
- `ui-kit/kit.html` is a frozen smoke test AND the specimen source. It is pointed at
  `../components/index.css` and it shows the kit as it stood at the end of the previous stage: if it
  still looks like yesterday, the split was clean. New components do NOT get added to it as pages;
  they get a labelled block, which is what a specimen is cut from. Renaming a block heading there
  breaks the build on purpose.
- `ui-kit/shell.html` is a composition (how the header and the tab bar stand together), not a source.
  The source of each part is its component page.

---

## What the split changed on purpose

The refactor moved no pixels except in one place, and it is listed here so it is never mistaken for a
regression:

- **`var(--card)` was declared nowhere.** Five surfaces read it (`.pos`, `.cta-bar`, `.toast`,
  `.cc-banner`, `.wd-flow`) and rendered transparent. They now read `--bg-card-quiet`, which restores
  `--card3d`, the value the previous stage declared for exactly this and never wired.
- **`.opt-sel-tag` had a grey-box border** (`#999`) that the Vault layer never repainted. It now reads
  `--border-hairline`.
- Everything else is identical: 2223 elements compared property by property and box by box on the
  frozen kit, with only those two changes and the stand's own renamed labels showing up.
