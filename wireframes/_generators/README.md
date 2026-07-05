# Wireframe generators

The 99 grey-box pages in `wireframes/*.html` are **generated**, not hand-authored.
This folder is the source that produces them. The committed artifact is still the
HTML; these scripts are kept so the set can be regenerated or extended instead of
hand-edited. They were authored in a session scratchpad and copied here for
preservation.

## How it works

`_shell.py` is the heart: it extracts the canonical CSS / footer / scripts from
`event-feed.html` and exposes the shared chrome (headers by auth, bottom nav,
category nav, shared sign-in / deposit `<dialog>`s, the left screen-tree panel via
`nav_tree`, the My-Bets tabs, `assemble()`/`write()`). Every per-screen generator
imports `_shell as S` and emits one family of pages.

To change shared chrome, edit `_shell.py` and regenerate; do not hand-edit
individual pages.

## Run order

1. **Per-screen generators** (independent, any order): `gen_event_detail.py`,
   `gen_category.py`, `gen_active_bets.py`, `gen_history.py`, `gen_overlays.py`,
   `gen_resolution.py`, `gen_notifications.py`, `gen_wallet.py`, `gen_profile.py`,
   `gen_howitworks.py`, `gen_auth_states.py`, `gen_states.py`, `gen_favorites.py`.
2. **Post-processors** (idempotent, run after the generators):
   - `resync.py` - rebuild the left screen-tree panel on every page from `nav_tree`.
   - `wire_catnav.py` - second-level category nav -> real links.
   - `wire_flow.py` - main-flow links (card question + YES/NO trigger-entries).
   - `inject_signin.py` - inject the shared dialogs into the hand-authored event-feed family.
   - `fixpack.py` - wire header + bottom-nav controls and inject the dialog CSS
     for the event-feed family (the chrome-wiring fix pass).
   - `chrome2.py` - turn the notifications bell into a `<details>` dropdown, add
     the "+" in-context deposit button by the balance, and add
     `body[data-loggedin-target]` so logged-out pages redirect to their logged-in
     counterpart after sign-in. Run after `fixpack.py`.
   - `chrome3.py` - swap the bell dropdown to its empty variant (linking to
     `notifications-empty.html`) on logged-in `*-empty*` pages. Run after `chrome2.py`.
   - `ia_annotations.py` - extract the zone chips + `.side` annotation/nav-tree
     blocks into `IA/annotations/` (one page per screen family) and strip them
     from the wireframes so the wireframes render clean. `build` (extract),
     `strip` (remove from wireframes), `all` (both). **Run `build` before
     `strip`**: strip reads the annotations from the wireframes, so once stripped
     they are gone from the source (restore with `git checkout -- ../*.html` to
     rebuild). Run last, after the chrome post-processors.

All post-processors are safe to re-run; each skips work already applied.

## Microcopy inventory (one-time bootstrap, not a post-processor)

- `microcopy_extract.py` - walk every `wireframes/*.html`, pull the product UI
  text (scoped to `.device` + dialogs, excluding the `.wf-*` / `.page-label` /
  `.state-switch` tooling) into `microcopy_raw.json`.
- `microcopy_build.py` - read that JSON and write `../../voice/microcopy.md`: a
  curated, per-screen inventory (Zone / Type / Line / Flag) with consistency
  issues marked (event vs market, Deposit vs Add funds, go-to-events button
  variants, leftover spec-notes, placeholders, ...) plus a user-content list.

Run `microcopy_extract.py` then `microcopy_build.py`. **This is a bootstrap:**
`microcopy.md` becomes the hand-maintained source of truth for product text, so
re-running clobbers manual edits - only re-run to re-baseline from scratch.

## Caveats

- **Hardcoded path.** `_shell.py` (and a few generators) hardcode
  `ROOT = /Users/sergiyshevchenko/Claud Projects/Project One/wireframes`. Update
  this constant if the repo lives elsewhere.
- **Python 3**, standard library only (`pathlib`, `re`). No third-party deps.
- `event-feed*.html` (the Event Feed family) were hand-authored in an earlier pass
  and are NOT emitted by `assemble()`; the post-processors patch them in place,
  which is why `inject_signin.py` / `fixpack.py` special-case that family.

## Conventions

The build contract is `wireframes/_conventions.md`; the defect / critique log is
`wireframes/_critique.md`. Grey-box only: neutral greys, monochrome outline SVG
icons, no em-dash, no color / type / shadows.
