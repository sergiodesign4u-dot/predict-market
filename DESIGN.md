---
name: Predict Market
description: A spectator's clarity, cast in graphite and brass - a mobile-first prediction market that is not a trader's terminal.
colors:
  page: "#0f1013"
  graphite: "#141619"
  slab: "#191b1f"
  plate: "#121417"
  card: "#141619"
  surface: "#1c1f24"
  surface-2: "#24282f"
  border: "#2b2f38"
  ink: "#ede7da"
  muted: "#a49d8f"
  brass: "#c7a24e"
  brass-2: "#d9b968"
  brass-text: "#d7ac53"
  brass-bright: "#e6c877"
  bronze: "#6e5a2e"
  groove-dark: "#0b0c0e"
  yes: "#4fa96b"
  yes-text: "#77d19b"
  no: "#c85a50"
  no-text: "#e79087"
  on-brass: "#180810"
typography:
  display:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(28px, 4vw, 38px)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(19px, 2vw, 24px)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: "DM Sans, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "0.06em"
  mono:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.03em"
textScale:          # ten steps, by 1 up to 14 and then by 2 and 4. 10px is the floor
  "10": "10px"      # a mono tag, a badge
  "11": "11px"      # a kicker, a meta line
  "12": "12px"      # a label, a chip, a compact row
  "13": "13px"      # the body default and the card question
  "14": "14px"      # long prose, a control label
  "16": "16px"      # a figure on a card
  "18": "18px"      # a small heading, the amount field
  "20": "20px"      # a section heading
  "24": "24px"      # a stat figure
  "30": "30px"      # the largest fixed size; above this a heading is fluid
leading:            # six measures
  none: 1           # an icon or a badge: the box is the line
  flat: 1.05        # display headings
  tight: 1.15       # a card question, a headline
  snug: 1.3         # a compact row
  base: 1.5         # body, and every long line
  loose: 1.6        # a reading column
rounded:            # one corner per job, five of them
  chip: "6px"       # chips, tags, small wells
  cta: "10px"       # DEFAULT: buttons, inputs, cards, option rows, confirm
  sheet: "16px"     # dialogs, sheets, plates
  card: "2px"       # the near-square Vault corner, used on marks and notches
  pill: "100px"     # fully round: sort filter, feed YES/NO, icon circles
spacing:            # the grid is 4px and 2 is the only half step. Nothing else is a distance.
  "2": "2px"        # the half step: a nudge, an icon gap
  "4": "4px"        # tight inner (label to value)
  "8": "8px"        # inner group gap, small padding
  "12": "12px"      # component padding, inner section gap
  "16": "16px"      # block gap, card padding
  "20": "20px"      # OUTER gap between groups (bet sheet)
  "24": "24px"      # section separation
  "28": "28px"      # a wide block inset
  "32": "32px"      # a hero inset
  "40": "40px"      # the largest step
  "56": "56px"      # a full band
  hairline: "1px"   # a line, not a distance: a rule, a 1px inset, a hidden input
  gutter: "40px"    # page gutter
control:            # the height of the box a finger or a pointer lands on
  dense: "32px"     # a desktop icon button
  base: "36px"      # the standard control
  tap: "44px"       # the mobile touch target (WCAG 2.5.5). Written as min-height, never as padding
  hero: "52px"      # the primary action on a sheet
icon:               # the mark inside a control. No odd sizes
  sm: "16px"
  md: "18px"
  lg: "22px"
components:
  button-primary:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.on-brass}"
    rounded: "{rounded.cta}"
    padding: "13px"
    height: "44px"
  button-yes:
    backgroundColor: "#4fa96b1f"
    textColor: "{colors.yes-text}"
    rounded: "{rounded.md}"
    height: "44px"
  button-no:
    backgroundColor: "#c85a501f"
    textColor: "{colors.no-text}"
    rounded: "{rounded.md}"
    height: "44px"
  chip:
    backgroundColor: "#1b1e23"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "11px 19px"
  chip-active:
    backgroundColor: "#c7a24e14"
    textColor: "#e7d6a6"
    rounded: "{rounded.lg}"
  card:
    backgroundColor: "{colors.card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "13px"
  dialog:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
  input:
    backgroundColor: "#0d0f12"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "12px"
---

# Design System: Predict Market

## 1. Overview

**Creative North Star: "The Brass Vault"**

A tactile graphite-and-brass system for a prediction market that must read as credible before it reads as anything else. The surface is a near-black graphite canvas cut into embossed stone plates, each with an inset top highlight and a dark cast rim, floating on their own drop shadow. One matte-brass accent does all the identity work; green and red are spent only on the YES / NO outcome and never on brand. Real event photography carries the story. The feeling is a cast metal plate and a vault fitting, not a casino floor and not a trading terminal.

This system is built for Alex, a News Junkie, whose documented fear is "this looks like crypto, so it is a scam." Every choice answers that fear with weight and restraint: contrast and one loud accent supply the energy, never shine or color-drench. The odds bar carries the outcome color so the buttons can stay quiet; the plate emboss supplies depth so nothing needs a glow. It explicitly rejects the trader-terminal look (order books, leverage sliders, PNL ranks, ticker walls, gamified loot), the beige / warm / soft-pastel AI-default palette, the low-contrast Kalshi complaint, and the muddy-navy Hedgehog look. The standing risk to pull back from is the green/red "wall of YES/NO buttons" trader-floor reflex.

Sources of the language: `concept/docs/concept.md` (taste and the five attributes) and `concept/docs/references.md` (Refero research), realized in `concept/concept.html`, and applied to the product as color copies of the grey wireframes in `ui-visual/`, every one of which links exactly one stylesheet, `components/index.css` (the two theme files that used to carry this were deleted in step 7). The theme owns color / type / surface only; structure, copy, and the state set stay owned by `wireframes/`.

**Key Characteristics:**
- Graphite canvas, one matte-brass accent, green/red reserved for outcome only.
- Two-stone plates: a lighter outer slab, darker inset plates and cards that float and cast shadow.
- Every panel is an embossed casting (inset top highlight + dark cast rim), never a flat fill.
- Restrained-to-committed color strategy: color is rare and structural, never decorative fill.
- Three typefaces on a contrast axis: Space Grotesk display, DM Sans body, IBM Plex Mono numbers.
- Real event photography in thumbnails and hero, masked and veiled into the graphite, never a grey placeholder.

## 2. Colors

A graphite grayscale tilted warm, with a single matte-brass accent and a reserved green/red outcome pair. Color is rare; the surface is stone.

### Primary
- **Matte Brass** (`#c7a24e`): the one brand accent. Identity (the up-trend logo tick), the active tab/chip, and primary CTAs only. `#d9b968` (`brass-2`) and `#e6c877` (`brass-bright`) are the lit variants for gradients, brass art, and eyebrow text on the darker plates; `#d7ac53` (`brass-text`) is the text/link-safe brass. `#6e5a2e` (`bronze`) is the deep shadow tone. Brass-line `rgba(199,162,78,.30)` draws the inset hairline frame on notched tiles. Text on brass fills is near-black `#180810`.

### Secondary
- **Outcome Green** (`#4fa96b`, `yes`): YES only. It fills the odds bar; on the tinted YES button the text is the lighter `#77d19b`. Never a brand or UI color.
- **Outcome Red** (`#c85a50`, `no`): NO only. It is the odds-bar track; on the tinted NO button the text is `#e79087`. Reserved strictly for the NO outcome; never used for errors, alerts, or destructive chrome.

### Neutral
- **Page** (`#0f1013`): the void behind the device.
- **Graphite Canvas** (`#141619`): the device base.
- **Outer Slab** (`#191b1f`): the lighter stone slab the header, categories and trust ride on.
- **Content Plate** (`#121417`): the darker inset plates (content, event detail, bet panel, dialogs).
- **Card Face** (`#141619`): floating cards, hero blocks, footer trust cards.
- **Surface / Surface-2** (`#1c1f24` / `#24282f`): raised chrome (header, dropdowns, chips, inputs-at-rest).
- **Border** (`#2b2f38`): hairline chrome border.
- **Groove Dark** (`#0b0c0e`): the recessed dark line of every engraved divider, paired with a `rgba(237,231,218,.055)` highlight below it.
- **Ink** (`#ede7da`): warm off-white body text. Never pure white.
- **Muted** (`#a49d8f`): secondary text, labels, stone captions.

### Series (multi-outcome charts only)
Five categorical colors for the lines of a multi-outcome chart, where each line is a candidate and not an answer: `#45c8d8` cyan, `#5b9df0` blue, `#c77dff` violet, `#f07ab8` magenta, `#9aa0aa` slate. In daylight they darken to `#17697a`, `#22589b`, `#7038a4`, `#a33372`, `#4f5560`, because the reading under the chart is drawn in the selected line's color and has to stay legible; all five clear 4.5:1 on the chart well in both themes.

**Green, red and gold are reserved.** The first cut of the series read `#4fd694` and `#d9b968`, which are the YES line and the lit brand brass: a candidate line drawn in the ink that means "this side won" and another in the ink that means "this is us". A reader cannot be asked to hold two meanings for one color. So the series lives in the arc the three reserved meanings leave free, cyan 187 through magenta 328, plus one desaturated neutral.

### Daylight (the light theme)
The product is dark; its theme is a light one, and it exists as a proof of the semantic layer rather than as a shipped feature. Only roles move, never primitives.

- **Chalk** (the pale stone, 8 steps `#fdfbf5` to `#eeece6`, plus one hairline at `#acaaa4`): the graphite ramp **reflected about its own ground**, `chalk L* = page L* - (graphite step L* - graphite page L*)`. In the Vault the page is the darkest thing on screen and every surface rises off it toward the light; reflected, the page is the lightest thing on screen and every surface settles onto it by getting darker. Each step is within 0.2 L* of its computed target and carries the number of the graphite step it answers to, so `--chalk-900` answers `--graphite-900`. The ramp is as long as the stone is: eight steps for the eight graphite fills that carry depth. Nearly **neutral**: R minus B is a constant +8, the same faint offset the graphite carries in the other direction. The warmth of the Vault is in the ink and the metal, not in the stone.
- **Presence does not invert.** On graphite, lightness carries two jobs at once: how deep a stone sits, and how far forward an object stands. A reflection can only invert one of them. Depth inverts, which is what makes daylight the Vault. Presence cannot: the Vault spends 6 to 11 L* lifting a control off its page and daylight has 1.7 L* of room above white, so reflecting it buries the most present thing in the system and the header, the dropdowns and the pills read as dirt. Six roles therefore leave the reflection and sit at the top of the ramp in the Vault's own order and direction (a control lighter than a panel, a hover darker than its rest, a pressed chip deeper than an idle one), and the **edge** carries what the fill gave up. That trade is only available on chalk: its hairline runs at 2.2:1 against its surface where the Vault's runs at 1.1:1.
- **Area is the tell.** A chip 6.5 L* under white is a quiet pill; a header band the same 7 L* under white is a dirty field. How deep a fill reads depends on how much of the screen it covers.
- **An icon is not a word, and ink is not light.** Reflecting a glyph keeps its contrast and changes its weight: the unsaved bookmark measures 6.7:1 on graphite and 7.2:1 on chalk and still looks twice as heavy, because a light shape on a dark ground spreads and thins while ink on paper sits solid. So a filled glyph has its own roles: `--icon-quiet` (`#787262`, 4.3:1) and `--icon-brass` (`#a9822f`, 3.2:1, the bar for a graphic). The text-safe brass reads brown at 16px, so a saved bookmark drawn in it stops meaning gold.
- **The reflection is total, gradients included**, which costs one thing and buys another. A graded face reads as lit from below, since its lit stop reflects into the shaded one. In exchange every separation keeps the Vault's own size: a category chip stands 4.0 L* off its bar in both themes, where a ramp merely translated into a light range put it at 9.5 and made the chips read as grey blocks. Holding the light overhead and reflecting only the fills is the alternative, and it is worse: an element sitting on the light end of a gradient loses its ground. The bevel keeps a lit lip on top in both themes, so a face is never read upside down.
- **Ink** (`#211f19` primary, `#565042` muted, `#6e6757` icon): warm, not neutral. The Vault reads warm in the dark because its light ink is bone; a neutral black would cool the whole product on the way over.
- **Dark brass** (`#684f18`): one, not three. On graphite there is room to separate a link brass from a lit brass from a chip brass and keep all three legible; on chalk there is not, and a legible brass beats a distinguishable one. The value is solved against brass-on-brass (a selected chip), not against bare stone.
- **Outcome ink** (`#225b35` YES, `#863228` NO): solved over their own 12% fills.
- **What does not move:** `--color-action`, because a mid-luminance metal reads on both stones; the white glyph on a photographic dialog head and the disc behind it, because a photograph does not get lighter; the course chrome, because it is the frame and not the product.
- **What inverts that looks like it should not:** the hairline, which is lighter than its surface on graphite and has to be darker on chalk; the emboss, where the lit lip goes from `rgba(255,255,255,.16)` to `.70`; and the photo veils, which follow the ink rather than the photograph.
- **The grain is the Vault's own**, at the same strength. An overlay blend bites less on a pale ground, not more.
- **The shade ladder is not scaled as a unit.** A 1px inset edge takes the quiet end (`.10` to `.16`) and a blurred drop takes the loud one (`.32` to `.44`). Scaling them together is what makes a light theme look flat.

### The token file, in two levels
`components/tokens.css` is the whole system and it has exactly two levels.

- **Primitive** (section 1): raw values with no opinion about purpose. The graphite ramp, bone, brass, the outcome greens and reds, the series, the alphas, the grain, and daylight's own primitives (chalk, ink, dark brass, the darker outcomes). A primitive is never read by a component.
- **Semantic** (section 2): 133 roles, colour only, `--focus-ring` among them (same value as `--text-brass` today and split from it on purpose, so a states pass can re-tone focus without moving every link). Each one points at a primitive through `var()` and carries the usage it was read from. A component may read a colour ONLY through a role; gate 13 fails the build otherwise.
- **Geometry has three scales, not one.** `--space-*` is the distance between things, `--size-*` the side of a thing, `--control-*` and `--icon-*` the box and the mark of an interactive element. They carry the same numbers and answer to different questions, which is why they carry different names.
- **Geometry, type and motion get no second level.** A radius or a gap has nothing for a theme to override, so components read those primitives directly. That is a decision, not an omission.
- **Section 3 is the theme**, not a third level: the same roles again with the values daylight needs.
- **The stacking order is a scale too**, and it is a list of eleven named layers in section 1, not a set of loose numbers: `--z-under` (the thing something else is read against), `--z-content`, `--z-float`, `--z-close`, `--z-dock`, `--z-nav`, `--z-header`, `--z-menu`, then the three course-chrome layers. The number is only the order; the name is the reason. A component may not type a raw `z-index`.

**Pairs and their ratios, both themes.** Measured down each theme's own `var()` chain, against the tint the label actually sits on.

| text role | on | Vault | Daylight |
|---|---|---|---|
| `--text-primary` | `--bg-page` | 15.4:1 | 15.8:1 |
| `--text-primary` | the deepest fill | 12.0:1 | 13.9:1 |
| `--text-muted` | `--bg-surface` | 6.1:1 | 7.4:1 |
| `--text-icon` | `--bg-surface` | 9.4:1 | 5.2:1 |
| `--text-brass` | `--bg-surface` | 7.8:1 | 7.1:1 |
| `--text-brass-chip` | `--bg-chip` over a brass tint | 10.0:1 | 6.2:1 |
| `--outcome-yes-text` | its own 12% fill | 8.3:1 | 6.5:1 |
| `--outcome-no-text` | its own 12% fill | 6.7:1 | 6.6:1 |
| `--icon-quiet` (a filled glyph) | `--bg-card` | 6.7:1 | 4.3:1 |
| `--icon-brass` (a saved mark) | `--bg-card` | 8.6:1 | 3.2:1 |

The last two are graphics, not words: the bar is 3:1. Everything else clears 4.5:1 in both themes.

**Contrast, both themes.** Every text pair is computed down each theme's own chain and against the tint it actually sits on. Daylight clears AA (4.5:1 text, 3:1 lines and icons) on every pair, measured across all 77 painted screens at 380 and 1280. It does not clear it by the Vault's margin: on graphite the muted text sits at 6.1:1 and the brass link at 7.8:1, which no pale ground can match while staying brass.

### Named Rules
**The One-Accent Rule.** Brass carries identity, the active state, and primary CTAs only. It is never a decorative fill and never competes with the outcome colors. If a screen has brass on more than the logo, the active chip, and the primary action, it is overspent.

**The Reserved-Outcome Rule.** Green is YES, red is NO, forever. They never appear as brand, error, success, or decoration. The odds bar (green fill on a red track) carries the outcome color so the YES/NO buttons can stay quiet tints.

**The Veil Rule.** A veil over a photograph is not a dark color, it is the layer that guarantees the words on top of it. It follows the ink: dark ink means a pale veil. A scrim behind a white glyph is a different thing and stays dark in both themes.

## 3. Typography

**Display Font:** Space Grotesk (with sans-serif fallback)
**Body Font:** DM Sans (with system-ui fallback)
**Label/Mono Font:** IBM Plex Mono (numbers, meta, provenance)

**Character:** A three-family pairing on a clear contrast axis, never two lookalike sans. Space Grotesk gives the headings and card questions a confident, slightly mechanical cut; DM Sans keeps the UI plain and legible; IBM Plex Mono makes every number read as a measured figure, not decoration. Numbers are always mono, which is the spectator's honesty cue.


**Where the families come from.** Space Grotesk, DM Sans and IBM Plex Mono are **served from this repo**: 18 woff2 files (latin and latin-ext, `font-display:swap`) in `assets/fonts/`, declared once in `components/fonts.css`, which `components/index.css` imports first. `components/tokens.css` names what has to arrive (`--font-display`, `--font-body`, `--font-mono`). Until step 8 every head carried a `<link>` to `fonts.googleapis.com` and `base.css` `@import`ed the same URL as well: one dependency declared twice, a render-blocking third-party request three hops down a CSS chain, and a call that sends a visitor's IP to a third party BEFORE the cookie banner this product ships has asked them anything. A consent banner over a page that has already made the call is not a consent banner. Gate 20 checks three ways it could come back: a page re-adding the tag, a generator re-adding it to every page it writes, and an `@font-face` naming a file nobody committed. 373 KB committed, 0 external requests measured.

### Hierarchy
- **Display** (Space Grotesk 700, `clamp(28px, 4vw, 38px)`, line-height 1.05, ls -0.03em): the feed H1 / page heading. `text-wrap: balance`.
- **Headline** (Space Grotesk 700, `clamp(19px, 2vw, 24px)`, line-height 1.15, ls -0.01em): the event question on Event Detail and the section titles. The featured card title runs one rank down at `clamp(19px, 1.5vw, 23px)`, so a card never competes with a page heading.
- **Title** (Space Grotesk 600, 13px, line-height 1.15, ls -0.02em): the feed card question; hot-list heads and market-stat values run 16px/700.
- **Body** (DM Sans 400/500, 13-14px, line-height 1.5): the story-led "why" line, resolution text, comments. Cap prose at 60-75ch (the SEO plate holds `max-width: 60ch`).
- **Label** (DM Sans 700, 12px, uppercase, ls 0.06-0.07em): category eyebrows and section kickers, in brass on the darker plates. Used deliberately, not above every block.
- **Mono** (IBM Plex Mono 400/500, 11-13px): Volume / Closes, odds percentages, market stats, provenance tags.

### Named Rules
**The Numbers-Are-Mono Rule.** Every figure a spectator weighs (probability, volume, close time, pool size) is set in IBM Plex Mono. Prose and labels are never mono; numbers are never in the prose face.

## 4. Spacing, size and the grid

**The 4px grid, and two scales on it, not one.** Every gap, padding and margin is a step of
`--space-*`: **4 / 8 / 12 / 16 / 20 / 24 / 28 / 32 / 40 / 56**, with `2` as the only half step and
`--hairline` (1px) kept out of it, because 1px is a line and not a distance. The scale used to have
25 steps with 1 2 3 4 5 6 7 8 9 10 in a row; step 6 rounded every value to the nearest step, ties
toward the heavier neighbour, and a number stopped being a step above 64px.

**A distance is not a measurement.** The side of a thing has its own scale, `--size-*`: **2 / 4 / 8 /
12 / 16 / 20 / 24 / 28 / 32 / 40 / 56 / 72**. Same numbers as the spacing scale today, different
reason, so a different name: a gap is a rhythm and can be retuned as one; the side of an avatar, an
icon plate, a legend swatch or a track moves when the thing moves. That scale shipped with two steps
(56 and 72) and fifty-seven declarations therefore borrowed a `--space-*` step for their own width
and height. Gate 12 fails the build on that now.

**A control and a mark have their own names.** `--control-32 / 36 / 44 / 52` is the height of the box
a finger or a pointer lands on; `--icon-12 / 16 / 18 / 22` is the drawn mark inside it. `--ring` (2px)
is the width and the offset of the focus outline.

- **The inner/outer rhythm.** Within a group, gaps stay small (4-12); between groups they open up
  (16-24). The bet sheet is the reference: ~20px between the header / YES-NO / amount / breakdown /
  confirm groups, 8-12px inside each. Small-inside, bigger-outside is what makes a dense panel read
  as ordered rather than crammed.
- **Touch targets follow the POINTER, not the viewport.** `@media(pointer:coarse)` gives every
  interactive control 44px; a fine pointer keeps 36, which clears WCAG 2.5.8 (24x24) with room. Binding
  that to `max-width:640px` is the bug it replaced: a touch tablet at 900px got the mouse target.
- **Enforcement.** The system is `components/` and nothing else. Gate 12 fails on a raw scale value in
  a component, on a `--space-*` step used as a measurement, and on a raw `z-index`; gate 9 fails on a
  `<style>` block or a `style=` attribute on a screen; gate 13 fails on a colour read past its role.

## 5. Elevation

Depth is the whole point of this system, and it is built from embossing plus real shadow, not from glass or glow. The surface is two stacked stones: a lighter outer slab (`#191b1f`) and darker inset plates and cards (`#121417` / `#141619`) that hover above it. Every plate is a casting with an inset top highlight, inset side and bottom shadows (the "cast rim"), and a soft drop shadow beneath. Dividers are engraved, not drawn: a dark recessed line with a faint highlight below it. Motion is minimal and physical: cards lift on hover (`translateY(-3px)` with a deeper shadow, `ease` on a `cubic-bezier(.2,.7,.2,1)` curve), and the condensed category strip slides into the sticky header on scroll. Every transform has a `prefers-reduced-motion` fallback that drops to shadow-only.

### Shadow Vocabulary
- **Cast rim (every plate)** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.17), inset 1px 0 0 rgba(255,255,255,.05), inset -1px 0 0 rgba(0,0,0,.35), inset 0 -1px 0 rgba(0,0,0,.55)`): the embossed top highlight + dark rim that makes a plate read as cast metal.
- **Plate drop** (`0 30px 58px -34px rgba(0,0,0,.85), 0 12px 26px -18px rgba(0,0,0,.7)`): the soft shadow that lifts the content plate, bet panel and dialogs off the slab.
- **Card rest** (`0 16px 30px -18px rgba(0,0,0,.8), 0 5px 12px -6px rgba(0,0,0,.6)` + cast rim): the floating feed card.
- **Card hover** (`translateY(-3px)` + `0 26px 44px -20px rgba(0,0,0,.85), 0 10px 18px -8px rgba(0,0,0,.7)`): a quiet physical lift, never a color change.
- **Engraved divider** (`border-top: 1px solid #0b0c0e; box-shadow: inset 0 1px 0 rgba(237,231,218,.055)`): every section rule, meta separator and footer divider.

### The order of the layers

| layer | what sits there |
|---|---|
| `--z-under` | a photograph, a veil, a decorative pseudo, the fill behind the text of its own row |
| `--z-content` | content lifted above its own decoration |
| `--z-float` | a frame or a control floating over a card |
| `--z-close` | the close control on a photographic head |
| `--z-dock` | sticky furniture at the foot of the content (the bet dock, the CTA bar) |
| `--z-nav` | the mobile bottom nav, over the dock it meets |
| `--z-header` | the sticky app header |
| `--z-menu` | what opens from the header or the toolbar |
| `--z-chrome-scrim` / `--z-chrome` / `--z-chrome-top` | the course drawer, which is not the product |

**The Layer Rule.** Depth on screen is the shadow vocabulary above; depth in the code is this list.
They are not the same thing and they are not interchangeable: a card reads as raised because of its
cast rim and its drop, not because of a number. A `z-index` only ever answers "which of these two
overlapping things wins", and if a component needs a new answer it needs a new name here, not a
larger number.

### Named Rules
**The Cast-Plate Rule.** Every panel is a stone casting: dark near-black rim plus an inset top highlight, on its own drop shadow. Big plates are never given a brass outline (brass hairline frames belong only to the small notched tiles: the SEO brand plate, the hero brand tile, the footer trust cards). If a big surface has a bright outline, it is wrong.

## 6. Components

### Buttons
- **Shape:** primary CTA at 10px (`rounded.cta`); YES/NO at 9px (`rounded.md`); minimum touch target 44px.
- **Primary (brass CTA):** a brass gradient (`linear-gradient(135deg, #c7a24e, #d9b968)`), near-black text (`#180810`), used for Confirm bet / Add funds inside dialogs and for state primary actions. One per view.
- **YES / NO (tinted, not filled):** YES is `rgba(79,169,107,.12)` with text `#77d19b` and border `#3f7d55`; NO is `rgba(200,90,80,.12)` with text `#e79087` and border `#8f4841`. They stay quiet at rest; the color deepens on hover/intent. The odds bar, not the buttons, carries the outcome weight.
- **Ghost icon buttons:** transparent on a `#2b2f38` hairline, `999px`, 44px; hover shifts to a brass-tinted border. Used for the header utility cluster and the event actions (comment / share / save into Favorites).

### Chips
- **Style:** one graphite chip across the family: face `#1b1e23`, hairline `rgba(255,255,255,.06)`, 10px radius (`rounded.cta`), DM Sans 600. Category nav carries a filled icon + label; the sub-filter and Load-more share the same chip.
- **State:** active is a brass tint (`rgba(199,162,78,.08)` fill, `rgba(199,162,78,.42)` border, `#e7d6a6` text, a faint brass glow). Brass appears only on the active chip. A condensed, icon-less version slides into the sticky header on scroll.

### Cards / Containers
- **Corner Style:** floating event cards are near-square at 7px (`rounded.sm`); stone plates and the footer trust cards are 9px (`rounded.md`).
- **Background:** card face `#141619` with a fine stone grain and a 160deg gradient; a faint brass graph-grid fades in from the top-right corner; a symbolic Ionic-column watermark bleeds off the left edge (opacity ~.20) as a "built on trust" cue.
- **Shadow Strategy:** the Card rest / Card hover vocabulary from Elevation. Cards float; plates hover; nothing is flat at rest.
- **Border:** a dark cast rim (`1px solid rgba(0,0,0,.4)` plus inset highlights), never a bright 1px line and never a nested card inside a card.
- **Internal Padding:** card body 13px; content plate 24px 28px 30px; sections 16px 20px.

### Inputs / Fields
- **Style:** the amount / text field sits recessed at `#0d0f12` with the `#2b2f38` hairline and a 10px radius, so it reads as cut into the plate rather than raised.
- **Focus:** a 2px brass focus ring (`outline: 2px solid #d7ac53; outline-offset: 2px`) on every interactive control.

### Navigation
- **Sticky app bar:** rides at the top on scroll on an opaque slab (`#1c1e22`) with an engraved bottom groove and a soft drop shadow; the logo is the brass up-trend tick + wordmark.
- **Category band:** page-level chips on the content plate (Trending is the featured hero page; Politics / Crypto / Culture / General are their own pages); active chip is the brass tint.
- **Mobile bottom nav:** four slots on `#1c1f24` with an engraved top groove; the active slot is brass-text with a brass icon. Money stays a utility (a balance figure), not a primary destination.

### Signature Components
- **Event card, binary (treatment B):** editorial thumbnail (masked, bleeding left) + question (Space Grotesk) + a 2-line story "why" + the **odds bar** (a thin 4px pill: green YES fill with a soft glow on a red NO track, YES%/NO% labels in mono) + tinted YES/NO + a mono meta row (Volume / Closes) + bookmark. The action band is vertically centered so odds bars line up across cards.
- **Event card, multi (treatment D):** option rows (name + probability in Space Grotesk + compact tinted YES/NO), each row a flat `#1b1e23` chip.
- **Featured hero band:** a featured market (photo backdrop under a veil, AMM price chart), two trust cards, a notched brass brand tile, and a "hot right now" list, each on the shared card-face stone.
- **Event Detail:** two floating plates (scrolling content + a sticky bet panel), a mobile sticky bet dock, an AMM "Market" depth panel (a pool + curve, not an order book), and content tabs (Comments / Biggest bets / Bets / Activity) in spectator language.

## 7. Do's and Don'ts

### Do:
- **Do** keep the canvas graphite (`#0f1013` / `#141619`) and spend brass (`#c7a24e`) only on identity, the active state, and one primary CTA per view.
- **Do** let the odds bar carry the outcome color and keep the YES/NO buttons as quiet tints, so the feed reads as a spectator surface.
- **Do** build depth from the cast-plate emboss and real drop shadow: inset top highlight + dark rim + soft shadow.
- **Do** set every number in IBM Plex Mono and every heading in Space Grotesk; keep body prose in DM Sans at 13-14px and 60-75ch.
- **Do** use real event photography, masked and veiled into the graphite; never a grey placeholder.
- **Do** state trust in one plain provable line ("USDC held 1:1, we never lend it. / N events resolved on-chain") near the action, in neutral stone, not in red.
- **Do** hold WCAG AA: body >= 4.5:1, large/UI >= 3:1; 44px touch targets; a brass `:focus-visible` ring on every control.

### Don't:
- **Don't** build a trader's terminal: no order books, leverage sliders, PNL ranks, ticker walls, or gamified loot. The AMM state is shown as a pool + depth curve, never a CLOB.
- **Don't** let the green/red YES/NO buttons become a "wall" of full-saturation fills; that trader-floor reflex is the standing risk to pull back from.
- **Don't** use beige, cream, warm, or soft-pastel palettes, or any AI-default "trustworthy/cozy" neutral. The canvas is graphite.
- **Don't** ship low-contrast (the Kalshi complaint) or muddy navy (the Hedgehog look); energy comes from contrast + one loud accent.
- **Don't** reuse green or red for anything but the YES / NO outcome, and never use red for an error or alert state.
- **Don't** put a brass outline on a big plate; brass hairline frames belong only to the small notched tiles.
- **Don't** use gradient text, decorative glassmorphism, `border-left`/`border-right` > 1px colored side-stripes, an identical-card-grid as a crutch, or a tiny uppercase tracked eyebrow above every section.
- **Don't** nest a card inside a card; a state message rides directly on the shared stone plate, borderless.

## 8. Contributing

- **Do** put the thing into the system before it appears on a screen: a value becomes a token, a component becomes a file and a page, an arrangement that has stood on three screens becomes a pattern. That order is the whole of it, and it only ever runs one way.
- **Do** give a state a token of its own and a value in both themes. A hover that exists on graphite and not on chalk is not a hover, it is a hover on one theme, and nothing in the file says so.
- **Don't** style a screen. A screen carrying its own rule is the one thing this spec cannot see, and it is invisible on the day it is written, not on the day it breaks.
- **Don't** append an `@import` at the end of `components/index.css` to make something work. The end is where an organism belongs; the position is computed by `python3 ui-kit/_levels.py --order`.

The addresses in full, and the gates that hold each one: `ui-kit/docs/architecture.md`, "Contributing to the system".

### The state tokens, and what each one was solved against

Six roles carry every interactive state in the product, and `--opacity-disabled` is the seventh that is not a colour. Each ratio is the text that stands on that state, measured in a browser down the theme's own `var()` chain: the value assigned to an element, the computed string handed back to the browser's own parser, the alpha composited up the ancestor stack. A figure here comes from that path or it does not go in the file.

| state role | the text on it | Vault | Daylight |
|---|---|---|---|
| `--bg-control-hover` | `--text-primary` | 12.65:1 | 15.38:1 |
| `--bg-pressed` | `--text-primary` | 13.99:1 | 14.59:1 |
| `--color-action-pressed` | `--text-on-brass` | 5.48:1 | 5.48:1 |
| `--tint-hover`, over `--bg-chip` | `--text-primary` | 11.49:1 | 12.15:1 |
| `--chrome-pressed` | `--chrome-text` | 11.46:1 | 11.46:1 |
| `--focus-ring`, on page / card / control | the ground it is drawn against | 8.98 / 8.56 / 6.98:1 | 7.40 / 6.96 / 7.40:1 |
| `--opacity-disabled` | `.45` in both themes | *not a pair* | *not a pair* |

Three things the table says that a list of values would not. **`--color-action-pressed` is the tightest in the system at 5.48:1**, and it is the only state where the ink is dark on a light ground: a pressed brass CTA is the one state that cannot be made deeper without taking the label with it. **`--chrome-pressed` reads the same in both themes on purpose** - the course chrome is the frame around the work and does not follow the product's theme, so its state does not either. **`--opacity-disabled` is the exception the other six exist to make rare**: opacity is the one state that is not a colour, so no sweep reading `getComputedStyle().color` can see it, and it stays at `.45` on exactly three rules rather than becoming a habit.
