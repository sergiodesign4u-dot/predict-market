# components/ - the system itself

This folder IS the design system. 51 stylesheets, 5,651 lines, `tokens.css` plus one file per
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

## Where the record is

`../DESIGN.md` for the visual language, `../docs/decisions.md` for why a thing was decided, and
`../docs/kit-archive/` for the per-component writing of the deleted vitrine: 48 pages of what each
component IS, its rule and its anti-rule. Nothing reads that folder; it is there so the same
measurement is not taken twice.
