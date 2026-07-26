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

## How to add a component

Four things, or it does not exist:

1. `components/<name>.css` - the file, with the header comment: the roles it reads, its stand page,
   the screens it stands on.
2. `ui-kit/<name>.html` - the stand page: the component live, the roles, the classes, the screens, the
   file itself.
3. a line in `ui-kit/_nav.js` - the registry that renders both the hub cards and the side panel.
4. a row in `ui-kit/docs/inventory.md` - with the css file and the page filled in.

The stand pages and the registry are generated by `ui-kit/_gen_component_pages.py` from
`components/*.css` plus the specimens in `ui-kit/_specimens.json`; `ui-kit/tokens.html` is generated
by `ui-kit/_gen_tokens_page.py` from `components/tokens.css`. Re-run either after a change; both are
idempotent and neither touches `components/` or `ui-visual/`.

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
- `ui-kit/kit.html` is a frozen smoke test, not a vitrine. It is pointed at `../components/index.css`
  and it shows the kit as it stood at the end of the previous stage: if it still looks like yesterday,
  the split was clean. New components do NOT get added to it. Their home is their own page.
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
