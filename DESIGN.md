# DESIGN.md - the "Vault" visual system

Authoritative for visual decisions. Applied as color copies of the grey wireframes in `ui-visual/` via `ui-visual/_theme.css`, which `@import`s `ui-visual/_theme-vault.css` (the Vault base tokens + component skin). The theme is linked after each page's inline `<style>` and owns color / type / surface only; structure, copy, and state-set stay owned by `wireframes/`. Source of the language: `concept/concept.html` + `concept/docs/concept.md` (+ `references.md`).

## Identity sentence
A tactile graphite-and-brass system: a near-black graphite canvas with one matte-brass accent, real event photography, embossed stone panels with inset brass hairlines and notched corners, and cards that float with real depth. Green and red are reserved strictly for the YES / NO outcome and are never used as brand color. Spectator's clarity, cast in graphite and brass - not a trader's terminal.

## Palette (tokens, `:root` in `ui-visual/_theme-vault.css`)
- `--page:#0f1013` (page), `--canvas:#141619` (device/graphite), `--surface:#1c1f24`, `--surface-2:#24282f`, `--border:#2b2f38`
- `--ink:#ede7da` (warm off-white body, never pure white), `--muted:#a49d8f` (secondary / stone)
- `--accent`/`--brass:#c7a24e` (matte brass = brand / action / active state), `--accent-2:#d9b968`, `--accent-text:#d7ac53` (brass for text/links), `--bronze:#6e5a2e`, `--brass-line:rgba(199,162,78,.30)`
- Engraved edges: `--groove-dark:#0b0c0e`, `--groove-light:rgba(237,231,218,.055)` (the inset top-highlight + dark-line that emboss every panel and divider)
- Outcome semantics only: `--yes:#4fa96b` (green = YES), `--no:#c85a50` (red = NO). On the tinted buttons: YES text `#4fd694` on `#123726` (border `#2c6f4b`), NO text `#ff868a` on `#3a1620` (border `#8a3b40`).
- Roadmap course-chrome tokens (sidebar) are separate and not product.

## Color strategy
Restrained-to-committed on graphite: stone-tinted neutral surfaces + ONE matte accent (brass). Color is rare and structural, never decorative fill. The **odds bar** (green fill on a red track) carries the outcome color; the YES/NO buttons are **tinted-not-fill** and stay quiet, so the feed reads as a spectator surface, not a trading floor. Green/red are revealed more strongly on hover / intent. Brass is spent on identity, the active tab, and primary CTAs only.

## Typography
- **Space Grotesk** (display: headings, card questions, the balance figure, buttons-as-labels) - weights 600/700.
- **DM Sans** (body / UI / chips) - 400/500/600/700.
- **IBM Plex Mono** (numbers, meta figures like Volume / Closes, provenance tags) - 400/500.
- Scale synced to the concept stand: feed h1 `clamp(28px,4vw,38px)` weight 700 ls -0.03em; card question ~15-16px weight 600/700 ls -0.01em; body 13-14px. `text-wrap:balance` on headings.

## Form / surface
- **Two-stone plates.** The device is one graphite slab (`#141619`); the feed content sits on darker stone plates (`#121417` + SVG fractalNoise grain `--stone-dark` + a 162deg gradient), each with an embossed rim (`inset` top highlight + inner shadow) and a drop shadow, radius 9px. The category bar, the content block, and the SEO block are three separate slabs that hover with their own shadow.
- **Cards float** on the content plate: darker stone face, 1px `--border`, radius 16px, a deep low drop-shadow; a faint gold column watermark bleeds up from the bottom-left corner (opacity ~.20). Photography = real event imagery in the thumbnail (12px radius), never a grey placeholder.
- **Inset brass edge + notched corner** is the signature frame: the SEO plate, the brand social tile, and the footer trust cards carry a `clip-path` notch (bottom-right, ~20px) plus a short brass hairline. Use it as the "cast plate" cue, not decoration.
- **Radius family:** cards 16px, stone plates 9px, chips / buttons 9-12px (YES/NO 9, cat-nav chip + Load-more 12, option rows 12), dialogs 16px, thumbnails 12px, icon buttons 999px.

## Components (established)
- **Event card (binary = treatment B):** photo thumbnail + question (Space Grotesk) + one-line plain "why" (clamped to 2 lines) + **odds bar** (thin 5px, green fill w/ glow on a red track, YES%/NO% text labels) + tinted YES/NO buttons + meta (Volume / Closes in mono) + bookmark. Action band is vertically centered so it aligns across cards.
- **Event card (multi = treatment D):** option rows (name, prob in Space Grotesk, compact tinted YES/NO).
- **Chip control family (one graphite chip):** the category nav (icon + label, with the active tab in a brass tint + brass hairline + faint glow), the Sort / Frequency filter summaries, and the Load-more button all share ONE chip - face `#1b1e23`, hairline `rgba(255,255,255,.06)`, 12px radius, DM Sans 600, brass only on the active state. A condensed icon-less category strip slides into the sticky header on scroll.
- **Category pages:** the top nav is page-level - Trending = `event-feed.html` (keeps the featured hero band + the content sub-filter); Politics / Crypto / Culture / General are their own pages that drop the hero + sub-filter and show only that category's events.
- **Trust cues:** a one-line trust bar can sit above the feed ("USDC held 1:1, we never lend it. / N events resolved on-chain"); the primary visible cue on the stand is the **footer trust strip** - three stone cards with a gold badge icon and gold line-art (column / source / globe) bleeding off the right, framed like the hero trust cards.
- **Brand tiles:** the hero promo tile ("The market decides. Opinions have value.") and the below-fold SEO brand plate ("Not just news. Your stake.") - notched brass frame, brass `em`, Predict Market byline.
- **How-it-works / Deposit dialogs:** native `<dialog>` on the graphite surface, brass-tinted icon chips and a brass-gradient primary CTA, FAQ / section layout.
- **States:** empty (brass icon + two actions), error (warning icon + "Try again"), loading (skeleton cards), push banner. Each state now rides the shared stone plate - the category bar + heading + state content on the `.cat-layout` slab, so a state reads as "the feed minus the cards", and the message block is borderless on the plate (no nested card). No state uses alarmist red (red stays reserved for NO).

## Accessibility
WCAG AA throughout: body >= 4.5:1, large / UI >= 3:1. Every accent and text-on-graphite pair is contrast-checked on the concept stand (the NO-button and footer pairs were the tightest and were tuned to pass). 44px touch targets on mobile for all primary controls (bet / bookmark / bell, cat-nav, filters). `:focus-visible` brass ring on the graphite canvas. The odds bar is not color-only (carries a % text label).

## Motion (to build in the Animation stage; currently mostly static)
Ease-out (quart / expo), no bounce. Candidate signature: a one-time odds-bar fill on load + a subtle odds-delta / "updated Nm ago" live cue; the condensed category strip already slides into the sticky header on scroll. Skeletons should shimmer. Reduced-motion alternative required for every animation.

## Bans (from the shared Impeccable laws, reaffirmed here)
No gradient text, no glassmorphism-by-default, no side-stripe borders, no identical-card-grid as a crutch, no tiny uppercase tracked eyebrows on every section, no cream / beige (the canvas is graphite). Keep brass for action / active / identity only.
