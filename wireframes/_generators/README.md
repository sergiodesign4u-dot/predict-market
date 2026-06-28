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
   `gen_howitworks.py`, `gen_auth_states.py`, `gen_states.py`, `gen_saved.py`.
2. **Post-processors** (idempotent, run after the generators):
   - `resync.py` - rebuild the left screen-tree panel on every page from `nav_tree`.
   - `wire_catnav.py` - second-level category nav -> real links.
   - `wire_flow.py` - main-flow links (card question + YES/NO trigger-entries).
   - `inject_signin.py` - inject the shared dialogs into the hand-authored event-feed family.
   - `fixpack.py` - wire header + bottom-nav controls and inject the dialog CSS
     for the event-feed family (the chrome-wiring fix pass).

All post-processors are safe to re-run; each skips work already applied.

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
