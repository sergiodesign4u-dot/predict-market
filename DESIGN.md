# DESIGN.md - the "Signal" visual system

Authoritative for visual decisions. Applied as color copies of the grey wireframes in `ui-visual/` via `ui-visual/_theme.css` (linked after each page's inline `<style>`; owns color/type only, structure stays in `wireframes/`). Source of the language: `concept/concept.html` + `concept/docs/concept.md`.

## Identity sentence
Dark near-black canvas with one electric-violet brand accent at maximum contrast, real event photography, and a subtle glow / dot-grid; green and red are reserved strictly for the YES / NO outcome and never used as brand color. Spectator's clarity, not a trader's terminal.

## Palette (tokens, `:root` in `ui-visual/_theme.css`)
- `--canvas:#0b0a12` (page/device), `--page:#08090c`, `--surface:#151322`, `--surface-2:#1d1a2e`, `--border:#2a2440`
- `--ink:#f1edff` (body text, 15.9:1), `--muted:#a7a0c4` (secondary, 7.4:1)
- `--accent:#8b5cf6` (electric violet = brand / action / active state), `--accent-text:#9b7bff` (violet for text/links, 5.8:1), `--lime:#c9f24e` (acid highlight, used sparingly)
- Outcome semantics only: `--yes:#2fbf73` (green = YES), `--no:#f0555a` (red = NO). On the tinted buttons: YES text `#43cf83` on `#17301f`, NO text `#ff868a` on `#301419`.
- Roadmap course-chrome tokens (sidebar): `--rm-*` (near-black `#161616`, lime accent `#c8ff00`). Not product.

## Color strategy
Restrained-to-committed on dark: tinted-neutral surfaces + ONE loud accent (violet). Color is rare and loud, never decorative fill. The **odds bar** (green fill on red track) carries the outcome color; the YES/NO buttons are tinted-not-fill and stay quiet, so the feed reads as a spectator surface, not a trading floor. Green/red revealed more strongly on hover/intent.

## Typography
- **Sora** (display: headings, card questions, numbers, buttons-as-labels) - weights 600/700/800.
- **Inter** (body/UI) - 400/500/600/700.
- **JetBrains Mono** (mono: code/provenance tags) - 400/500.
- Scale synced to the concept stand: h1 `clamp(28px,4vw,38px)` weight 800 ls -0.02em; h2 `clamp(20px,2.6vw,24px)` weight 700 ls -0.01em; body 13-14px. `text-wrap:balance` on headings.

## Form / surface
- Radius: cards 16px, buttons 10-12px, chips/pills 999px, small controls 7-10px.
- Cards: dark surface, 1px `--border`, a soft violet glow drop-shadow, and a corner dot-grid texture (radial-dot mask fading top-right -> bottom-left). Photography = real event/subject imagery (thumbnails), never a grey placeholder.
- Glow / dot-grid is the signature "backlit" detail (Jupiter/MELEE lineage); use it as ambient depth, not decoration.

## Components (established)
- **Event card (binary = treatment B):** photo thumbnail + question (Sora) + one-line plain "why" + **odds bar** (YES%/NO% split, text labels, not color-only) + tinted YES/NO buttons + meta (volume/closes) + bookmark.
- **Event card (multi = treatment D):** option rows (name, prob, compact tinted YES/NO).
- **Trust bar** above the feed: "USDC held 1:1, we never lend it. / N events resolved on-chain" - trust near the action, on first paint incl. logged-out.
- **How-it-works dialog:** native `<dialog>` with a violet glow hero (radial glow orb + dot-grid), big Sora heading, icon-led sections, FAQ, accent CTA.
- **Filter dropdowns** (Sort / Frequency): pill summary + native `<details>` panel.
- **States:** empty (accent icon + two actions), error (warning icon + "Try again"), loading (skeleton cards), push banner. No state uses alarmist red (red stays reserved for NO).

## Accessibility
WCAG AA throughout: body >= 4.5:1, large/UI >= 3:1. Every measured pair passes (NO button 5.48:1, footer 6.04:1). 44px touch targets on mobile for all primary controls. `:focus-visible` accent ring on the dark canvas. The odds bar is not color-only (carries a % text label).

## Motion (to build in the Animation stage; currently mostly static)
Ease-out (quart/expo), no bounce. Candidate signature: a one-time odds-bar fill on load + a subtle odds-delta / "updated Nm ago" live cue. Reduced-motion alternative required. Skeletons should shimmer.

## Bans (from the shared Impeccable laws, reaffirmed here)
No gradient text, no glassmorphism-by-default, no side-stripe borders, no identical-card-grid as a crutch, no tiny uppercase tracked eyebrows on every section, no cream/beige. Keep the accent for action/active only.
