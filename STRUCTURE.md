# Project Structure

This repo follows a 12-stage design-engineering course layout. One folder per stage,
in course order. Convention: raw markdown lives in each stage's `docs/`; the stage's
HTML page sits flat at the stage-folder root (for example `research/research.html`,
not `research/html/research.html`).

## The 12 stages

Where each stage lives. **Which stage is done is recorded in the status table in `README.md` and
nowhere else** - a second copy of a status is a copy that goes stale.

| # | Stage | Folder | HTML page |
|---|---|---|---|
| 01 | Foundation Research | `research/` | `research/research.html` |
| 02 | User Research (Personas + JTBD) | `user-research/` | `personas.html`, `jtbd.html` |
| 02+ | CJM (As-Is + To-Be) - inside User Research, not a stage of its own | `user-research/` | `cjm-as-is.html`, `cjm-to-be.html` |
| 03a | Information Architecture, Basic layer | `ia/` | `flows.html`, `concept-map.html` |
| 03b | Information Architecture, Detailed layer | `ia/` | `ia.html`, `sitemap.html`, `seo.html`, `system.html` |
| 04 | Wireframes | `wireframes/` | 104 grey pages |
| 05 | Voice | `voice/` | `voice/voice.html` |
| 06 | Concept | `concept/` | `concept.html` (+ `directions.html`) |
| 07 | UI + Visual | `ui-visual/` | 106 painted screens, every family and every state |
| 08 | Tokens + Components | `components/` (the system) | `ui-kit/overview.html` |
| 09 | Design System | `components/patterns/` (6 files) + `ui-kit/` (55 of 55 pages, rebuilt by hand 2026-08-07 to 2026-08-08: a shelf per level plus one page per component, every component in the system) | `ui-kit/overview.html` |
| 10 | Responsive | | - |
| 11 | Animation | | - |
| 12 | Handoff | | - |

The CJM keeps its own row in the README status table, because it is a deliverable that can be
done or not done; it does not keep a number, because it is built inside User Research. The two
IA layers are one stage answered in two passes and share the folder.

**These numbers changed on 2026-08-02.** The project used to count thirteen stages, one ahead of
the course from Information Architecture onward, so a document or a commit written before that date
says "Stage 09" where this table says 08. The old-to-new key is in the header of
[`docs/decisions.md`](./docs/decisions.md). Dated records were not renumbered: an entry is true as
of its own date, and rewriting it would make it disagree with the commit it describes. What was
renumbered is every reference that points FORWARD, at work not yet done, because that is the one a
reader acts on.

`ia/annotations/` (wireframe annotations) is an IA/Wireframes artifact, not a separate stage, though
it does carry its own row in the sidebar.

**Every generator in this repository was deleted on 2026-08-07** - 54 Python scripts and 9 browser
scripts, along with the vitrine and the 41 gates they fed. What they used to write is still here and
still correct; it is simply static now. So the paragraphs below say where a thing IS rather than what
writes it, and a change to any of them is made in the files that carry it.

The shared left sidebar is markup inside each page: the root viz pages, the annotation pages,
`concept/concept.html` and the archived stands under `concept/old/` each hold their own copy of the
roadmap. Three scripts used to keep those copies in step. **There is no longer anything that does**,
so the roadmap is one list in prose here and in `README.md`, and a change to it is a search and a
sweep by hand. The panel's LOOK is not per-page and never was: it is one component,
`components/course-chrome.css`, linked by the 28 course pages with `fonts.css` and `tokens.css`.

Structure flows one way between the two screen trees: `wireframes/` decides it and `ui-visual/`
follows. A check used to fail the build when the trees disagreed inside `<main>`, `<header>`, the
bottom nav, `<footer>` or the sheet body of an invoked overlay. It is gone, and the six differences
that ARE the layer boundary are still declared in `wireframes/_conventions.md`, which is now read
before the edit rather than enforced after it.

The two trees do not name every screen the same way: a category page is `politics.html` in grey and
`event-feed-politics.html` in colour. That map lived in `_twins.py` and is now read by a person. It
is worth knowing why it existed at all: pairing by filename cannot see an unpaired page, so 32 grey
category screens stood against 4 painted ones for two stages, in silence, behind five hand-written
copies of the map.

The chrome is the exception that proves the one-way rule. Inside `<header>`, the bottom nav and
`<footer>` the two trees answer different questions: the paint owns what the header IS, the grey tree
owns which state it is IN (auth variant, active nav slot, empty notifications). Reconcile in that
order. A dialog that also has a standalone page is one markup and not two, and a screen can drift
from its own second copy inside the same tree, which is the drift nothing was watching before a check
was written for it and nothing is watching now.

## Old -> new map (the restructure)

The repo was reorganized from a flat, ~9-stage anticipated layout to the layout above.

### Files moved

| Old path | New path |
|---|---|
| `research/competitive-analysis.md` | `research/docs/competitors.md` |
| `research/benchmark-trust.md` | `research/docs/benchmark.md` |
| `research/aarrr.md` | `research/docs/aarrr.md` |
| `research/ux-patterns.md` | `research/docs/ux-patterns.md` |
| `research/master-research.md` | `research/docs/research.md` (the 7-section synthesis) |
| `research.html` | `research/research.html` |
| `research/personas.md` | `user-research/docs/personas.md` |
| `research/jtbd.md` | `user-research/docs/jtbd.md` |
| `personas.html`, `jtbd.html` | `user-research/personas.html`, `user-research/jtbd.html` |
| `IA/sitemap.md`, `IA/flows.md` | `ia/docs/sitemap.md`, `ia/docs/flows.md` |
| `ia.html`, `sitemap.html`, `flows.html` | `ia/ia.html`, `ia/sitemap.html`, `ia/flows.html` |
| `IA/annotations/` | `ia/annotations/` |
| `voice/voice.md`, `voice/microcopy.md` | `voice/docs/voice.md`, `voice/docs/microcopy.md` |
| `voice.html` | `voice/voice.html` |
| `tokens/`, `components/` | the code lives in `components/`; the planned `tokens-components/` folder was never used and was deleted in step 7. The vitrine that stood in `ui-kit/` was deleted on 2026-08-07 and its writing is kept in `docs/kit-archive/` |
| `assets/icons.js` | **the ONE icon sprite, 34 symbols in two families**, added 2026-08-09 and given its second family 2026-08-13. Every screen and every kit page loads it once and reaches a glyph as `<use href="#i-name">` for the 30 filled marks or `<use href="#l-name">` for the 4 line marks; no document carries a copy. **The line family could not be in this file until the day it arrived**, because `base.css` turned every `<use>` into the filled family with an `!important` and a two-stroke drawing with no area paints nothing; the floor keys on `#i-` now, so a symbol declares its family by its NAME and no document has to. 983 hand-written paths left 119 documents, and the proof that move changed nothing is 238 full-page screenshots at two widths, 0 differing, against a control of 0. **One of the 30 filled marks is the product's own**, `i-plus-b`: `.bal-add` is the only control standing on a solid brass ground, where a 1.65px stroke reads as unfinished, and all 85 plus marks in the product stand there. It was inlined into 112 documents until that day: 1,756 KB, 23 per cent of the painted tree, half of it unused on any given screen, and one glyph had drifted into two versions. **It is a SCRIPT and not an `.svg`**, which was the same day's correction: an external `<use>` is a cross-document reference and `file://` gives every file its own origin, so a page opened from disk drew 0 of 34 glyphs. A script loads from disk and from a server alike. **It was 35 until 2026-08-14, when `l-menu` left with the control it was drawn for**: the header's hamburger was a `<button>` labelled "Menu (reserved for future scaling)" with no handler, no drawer and no destination, `display:none` below the desk on top of that, standing on 105 painted screens, 87 grey ones and 10 kit specimens. A symbol whose only remaining reader is the page that documents the sprite is a glyph with no placement. |
| `assets/_roadmap.js` | **the ONE registry of the course roadmap**, added 2026-08-13. The same outline stood as hand-written markup in 28 documents across five folders, 890 lines of it, and one page had silently stood four rows behind since stage 09. A page carries an empty `<aside class="sidebar" id="sidebar">`, declares its own section anchors and nothing else, and takes its depth and its active row from the script and from its own path. It is `ui-kit/_nav.js` one folder over, and the same three rules: the active row is computed and never declared, a row with no page is a visible `<span>`, and it brings no CSS of its own. `docs/backlog.md` 117 |
| `assets/` | every shipped image, at the root and owned by neither layer. It was `ui-visual/assets/` until step 7c, which meant `components/` reached into the product's screen folder to draw a component. `assets/fonts/` joined it in step 8: 18 woff2 faces, so no page calls a font host. **It holds only what a screen asks for, since 2026-08-13**: five 1254x1254 masters and two unused SVGs sat here unreferenced until then, and moving them to `visuals/masters/`, where the README always said masters live, took the folder from 9,690,253 bytes to 1,339,606. `docs/backlog.md` 138. **And to 1,193,741 in 25 tracked files later the same day**, when three of the four trust drawings stopped being files and became `data:` URIs in `components/trust-art.css`, **and to 985,277 in 23 on 2026-08-14**, when the fourth placement went the same way and `trust-column.webp` and `trust-globe.webp` followed `trust-source.webp` and `trust-column-full.webp` to `visuals/masters/`. **No trust artwork is fetched by anything now.** `assets/fonts/` still holds its 8 woff2 files and only 4 of them are ever requested: the other four are the latin-ext safety net, measured at **0 requests across all 163 documents**, and the four that are used are inlined into `components/fonts.css`. `docs/backlog.md` 140, 147 and 148 |
| `components/trust-art.css` | **the four trust drawings, carried as values rather than fetched**, added 2026-08-13. Four `--trust-art-*` custom properties, each a `data:` URI holding a q20 luminance mask, read by `trustbar.css`, `card.css` and `seo-plate.css`. It is NOT a component: no selector of a product element, no page in the kit, no row in the inventory. **It exists because a mask image is a CORS-enabled fetch and a background image is not**, and these pages are read from disk, where every file is its own opaque origin: `mask-image:url("../assets/x.webp")` is blocked in Chromium AND in WebKit from a `file://` page while the same file loads as a background in the same document. This is the same origin rule that made `assets/icons.js` a script instead of an `.svg`, and the same one that leaves WebKit without DM Sans or Space Grotesk on a disk page, which is `docs/backlog.md` 147. Three footer tiles 346,492 bytes to 87,558; the whole set 113,742, or 153,439 as base64 on every screen against 488,842 on the heaviest. `docs/backlog.md` 140 |

### New artifacts (did not exist before)

| File | Notes |
|---|---|
| `research/docs/lean-ux-canvas.md` | Lean UX Canvas v2 (Jeff Gothelf), compiled from the existing strategy + synthesis + JTBD |
| CJM As-Is + To-Be (under `user-research/`) | New stage, built in the CJM pass (2 md + 2 pages); lives inside User Research per the course layout |
| `ia/docs/blocks.md` | The block bank: what a page of a given TYPE is made of, before one is drawn. Created 2026-08-03, when the Design System stage walked its four sources for the next screen and found that the IA map could name a node while nothing could say what the node was made of. Banked by TYPE, so one pass covers every node of that type |

### Retired (content folded, then removed)

| Old file | Where its content went |
|---|---|
| `research/strategy.md` | folded into `research/docs/research.md` Strategy section + seeded `lean-ux-canvas.md` |
| `research/product-model.md` | retired (AIDA framework superseded by strategy) |
| old `research/research.md` (competitor v1) | groupings superseded by `competitors.md`; competitor-voice already in `voice/` |

Git history preserves the retired files. During the migration they were staged under
`research/docs/_legacy/` and removed once their content was folded.
