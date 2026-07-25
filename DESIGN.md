---
name: Predict Market
description: A spectator's clarity, cast in graphite and brass - a mobile-first prediction market that is not a trader's terminal.
colors:
  page: "#0f1013"
  graphite: "#141619"
  slab: "#191b1f"
  plate: "#121417"
  card: "#14161a"
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
    lineHeight: 1.04
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(19px, 2vw, 24px)"
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "-0.02em"
  body:
    fontFamily: "DM Sans, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "11.5px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.06em"
  mono:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.03em"
rounded:
  xs: "6px"         # every radius is even too (the 2px rule); count chips, badges
  sm: "8px"         # small buttons, dialog close
  md: "10px"        # cards, option rows
  cta: "10px"       # DEFAULT: buttons, inputs, confirm
  lg: "12px"        # chips, dropdowns, feed cards
  xl: "16px"        # dialogs
  sheet: "20px"     # bottom-sheet top edge
  pill: "1000px"    # fully round: sort filter, feed YES/NO, icon circles
spacing:            # 2px grid. Primary steps 4/8/12/16/20/24; 2/6/10/14 for fine-tuning. Every value is divisible by 2.
  "2": "2px"        # hairline nudges, icon gaps
  "4": "4px"        # tight inner (label to value)
  "6": "6px"        # chip gaps
  "8": "8px"        # inner group gap, small padding
  "10": "10px"      # button/pair gaps
  "12": "12px"      # component padding, inner section gap
  "14": "14px"      # -
  "16": "16px"      # block gap, card padding
  "20": "20px"      # OUTER gap between groups (bet sheet)
  "24": "24px"      # section separation
  gutter: "40px"    # page gutter
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

Sources of the language: `concept/docs/concept.md` (taste and the five attributes) and `concept/docs/references.md` (Refero research), realized in `concept/concept.html`, and applied to the product as color copies of the grey wireframes in `ui-visual/` via `ui-visual/_theme.css` (which `@import`s `ui-visual/_theme-vault.css`). The theme owns color / type / surface only; structure, copy, and the state set stay owned by `wireframes/`.

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
- **Card Face** (`#14161a`): floating cards, hero blocks, footer trust cards.
- **Surface / Surface-2** (`#1c1f24` / `#24282f`): raised chrome (header, dropdowns, chips, inputs-at-rest).
- **Border** (`#2b2f38`): hairline chrome border.
- **Groove Dark** (`#0b0c0e`): the recessed dark line of every engraved divider, paired with a `rgba(237,231,218,.055)` highlight below it.
- **Ink** (`#ede7da`): warm off-white body text. Never pure white.
- **Muted** (`#a49d8f`): secondary text, labels, stone captions.

### Named Rules
**The One-Accent Rule.** Brass carries identity, the active state, and primary CTAs only. It is never a decorative fill and never competes with the outcome colors. If a screen has brass on more than the logo, the active chip, and the primary action, it is overspent.

**The Reserved-Outcome Rule.** Green is YES, red is NO, forever. They never appear as brand, error, success, or decoration. The odds bar (green fill on a red track) carries the outcome color so the YES/NO buttons can stay quiet tints.

## 3. Typography

**Display Font:** Space Grotesk (with sans-serif fallback)
**Body Font:** DM Sans (with system-ui fallback)
**Label/Mono Font:** IBM Plex Mono (numbers, meta, provenance)

**Character:** A three-family pairing on a clear contrast axis, never two lookalike sans. Space Grotesk gives the headings and card questions a confident, slightly mechanical cut; DM Sans keeps the UI plain and legible; IBM Plex Mono makes every number read as a measured figure, not decoration. Numbers are always mono, which is the spectator's honesty cue.

### Hierarchy
- **Display** (Space Grotesk 700, `clamp(28px, 4vw, 38px)`, line-height 1.04, ls -0.03em): the feed H1 / page heading. `text-wrap: balance`.
- **Headline** (Space Grotesk 700, `clamp(19px, 2vw, 24px)`, line-height 1.14, ls -0.01em): the event question on Event Detail, featured-market title, section titles.
- **Title** (Space Grotesk 600, 13px, line-height 1.14, ls -0.02em): the feed card question; hot-list heads and market-stat values run 15px/700.
- **Body** (DM Sans 400/500, 13-14px, line-height 1.5): the story-led "why" line, resolution text, comments. Cap prose at 60-75ch (the SEO plate holds `max-width: 60ch`).
- **Label** (DM Sans 700, 11.5px, uppercase, ls 0.06-0.07em): category eyebrows and section kickers, in brass on the darker plates. Used deliberately, not above every block.
- **Mono** (IBM Plex Mono 400/500, 10.5-12.5px): Volume / Closes, odds percentages, market stats, provenance tags.

### Named Rules
**The Numbers-Are-Mono Rule.** Every figure a spectator weighs (probability, volume, close time, pool size) is set in IBM Plex Mono. Prose and labels are never mono; numbers are never in the prose face.

## 4. Spacing & Grid

**The 2px grid.** Every gap, padding and margin is a multiple of 2. The primary steps are **4 / 8 / 12 / 16 / 20 / 24** (the 8pt-grid backbone); **2 / 6 / 10 / 14** exist for fine-tuning small elements. The only rule you must never break: **the value is divisible by 2** - 16, never 15; 10, never 11. This removes the "13 or 14px?" decision, keeps elements optically aligned, and makes the layout translate cleanly to code.

- **Scale:** `2` (hairline nudges, icon gaps) · `4` (tight inner: label to value) · `6` (chip gaps) · `8` (inner group gap, small padding) · `10` (button / pair gaps) · `12` (component padding) · `16` (block gap, card padding) · `20` (outer gap between groups) · `24` (section separation) · `40` (page gutter).
- **The inner/outer rhythm.** Within a group, gaps stay small (4-10); between groups, they open up (16-24). The bet sheet is the reference: ~20px between the header / YES-NO / amount / breakdown / confirm groups, ~6-12px inside each. Small-inside, bigger-outside is what makes a dense panel read as ordered rather than crammed.
- **Exceptions are still even.** A one-off `2`, `6` or `10` for optical alignment is fine; an odd value (13, 15, 21) is not. When a legacy component needs a `9px` or `11px` tweak, round to the nearest even step.
- **Touch targets** are a separate constraint layered on top: interactive controls are ≥44px on the tap surface (mobile), achieved with padding, not by breaking the grid.
- **Enforcement status.** The Vault theme (`ui-visual/_theme.css` + `_theme-vault.css`, the source of truth for the component skins) is fully snapped to the grid - audited to 0 odd padding / margin / gap and 0 odd radius. The grey-box wireframe shell inherited into the pages still carries structural odd values; those are the structure layer, snapped page-by-page only when a screen is reworked, not swept blind. New Vault CSS must land even.

## 5. Elevation

Depth is the whole point of this system, and it is built from embossing plus real shadow, not from glass or glow. The surface is two stacked stones: a lighter outer slab (`#191b1f`) and darker inset plates and cards (`#121417` / `#14161a`) that hover above it. Every plate is a casting with an inset top highlight, inset side and bottom shadows (the "cast rim"), and a soft drop shadow beneath. Dividers are engraved, not drawn: a dark recessed line with a faint highlight below it. Motion is minimal and physical: cards lift on hover (`translateY(-3px)` with a deeper shadow, `ease` on a `cubic-bezier(.2,.7,.2,1)` curve), and the condensed category strip slides into the sticky header on scroll. Every transform has a `prefers-reduced-motion` fallback that drops to shadow-only.

### Shadow Vocabulary
- **Cast rim (every plate)** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.17), inset 1px 0 0 rgba(255,255,255,.05), inset -1px 0 0 rgba(0,0,0,.35), inset 0 -1px 0 rgba(0,0,0,.55)`): the embossed top highlight + dark rim that makes a plate read as cast metal.
- **Plate drop** (`0 30px 58px -34px rgba(0,0,0,.85), 0 12px 26px -18px rgba(0,0,0,.7)`): the soft shadow that lifts the content plate, bet panel and dialogs off the slab.
- **Card rest** (`0 16px 30px -18px rgba(0,0,0,.8), 0 5px 12px -6px rgba(0,0,0,.6)` + cast rim): the floating feed card.
- **Card hover** (`translateY(-3px)` + `0 26px 44px -20px rgba(0,0,0,.85), 0 10px 18px -8px rgba(0,0,0,.7)`): a quiet physical lift, never a color change.
- **Engraved divider** (`border-top: 1px solid #0b0c0e; box-shadow: inset 0 1px 0 rgba(237,231,218,.055)`): every section rule, meta separator and footer divider.

### Named Rules
**The Cast-Plate Rule.** Every panel is a stone casting: dark near-black rim plus an inset top highlight, on its own drop shadow. Big plates are never given a brass outline (brass hairline frames belong only to the small notched tiles: the SEO brand plate, the hero brand tile, the footer trust cards). If a big surface has a bright outline, it is wrong.

## 6. Components

### Buttons
- **Shape:** primary CTA at 10px (`rounded.cta`); YES/NO at 9px (`rounded.md`); minimum touch target 44px.
- **Primary (brass CTA):** a brass gradient (`linear-gradient(135deg, #c7a24e, #d9b968)`), near-black text (`#180810`), used for Confirm bet / Add funds inside dialogs and for state primary actions. One per view.
- **YES / NO (tinted, not filled):** YES is `rgba(79,169,107,.12)` with text `#77d19b` and border `#3f7d55`; NO is `rgba(200,90,80,.12)` with text `#e79087` and border `#8f4841`. They stay quiet at rest; the color deepens on hover/intent. The odds bar, not the buttons, carries the outcome weight.
- **Ghost icon buttons:** transparent on a `#2b2f38` hairline, `999px`, 44px; hover shifts to a brass-tinted border. Used for the header utility cluster and the event actions (comment / share / save into Favorites).

### Chips
- **Style:** one graphite chip across the family: face `#1b1e23`, hairline `rgba(255,255,255,.06)`, 12px radius (`rounded.lg`), DM Sans 600. Category nav carries a filled icon + label; the sub-filter and Load-more share the same chip.
- **State:** active is a brass tint (`rgba(199,162,78,.08)` fill, `rgba(199,162,78,.42)` border, `#e7d6a6` text, a faint brass glow). Brass appears only on the active chip. A condensed, icon-less version slides into the sticky header on scroll.

### Cards / Containers
- **Corner Style:** floating event cards are near-square at 7px (`rounded.sm`); stone plates and the footer trust cards are 9px (`rounded.md`).
- **Background:** card face `#14161a` with a fine stone grain and a 160deg gradient; a faint brass graph-grid fades in from the top-right corner; a symbolic Ionic-column watermark bleeds off the left edge (opacity ~.20) as a "built on trust" cue.
- **Shadow Strategy:** the Card rest / Card hover vocabulary from Elevation. Cards float; plates hover; nothing is flat at rest.
- **Border:** a dark cast rim (`1px solid rgba(0,0,0,.4)` plus inset highlights), never a bright 1px line and never a nested card inside a card.
- **Internal Padding:** card body 13px; content plate 24px 28px 30px; sections 16px 20px.

### Inputs / Fields
- **Style:** the amount / text field sits recessed at `#0d0f12` with the `#2b2f38` hairline and a 12px radius, so it reads as cut into the plate rather than raised.
- **Focus:** a 2px brass focus ring (`outline: 2px solid #d7ac53; outline-offset: 2px`) on every interactive control.

### Navigation
- **Sticky app bar:** rides at the top on scroll on an opaque slab (`#1c1e22`) with an engraved bottom groove and a soft drop shadow; the logo is the brass up-trend tick + wordmark.
- **Category band:** page-level chips on the content plate (Trending is the featured hero page; Politics / Crypto / Culture / General are their own pages); active chip is the brass tint.
- **Mobile bottom nav:** four slots on `#1c1f24` with an engraved top groove; the active slot is brass-text with a brass icon. Money stays a utility (a balance figure), not a primary destination.

### Signature Components
- **Event card, binary (treatment B):** editorial thumbnail (masked, bleeding left) + question (Space Grotesk) + a 2-line story "why" + the **odds bar** (a thin 5px pill: green YES fill with a soft glow on a red NO track, YES%/NO% labels in mono) + tinted YES/NO + a mono meta row (Volume / Closes) + bookmark. The action band is vertically centered so odds bars line up across cards.
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
