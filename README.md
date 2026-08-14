# Prediction Market Platform

A mobile-first Web3 platform for prediction markets. Users bet YES/NO on real-world events using stablecoins (USDC/USDT). Outcomes resolve against reality.

**Core bet:** better clarity and onboarding than existing competitors (Polymarket, Kalshi).
**Audience:** 20-40, trust-driven.
**Platform:** Mobile-first web, then responsive desktop.

---

## Live Research Summary

**[View research.html live](https://sergiodesign4u-dot.github.io/predict-market/research/research.html)**

Single-page summary of all research phases. Open the link above in any browser - no local server needed.

**CJM (live):** [As-Is](https://sergiodesign4u-dot.github.io/predict-market/user-research/cjm-as-is.html) - [To-Be](https://sergiodesign4u-dot.github.io/predict-market/user-research/cjm-to-be.html) (these paths go live once the branch is merged to main, which serves GitHub Pages). Takeaway: the deepest As-Is dip is the crypto wall (mass abandonment); To-Be flattens it by letting Alex browse and form the bet intent before any wallet, with the auth / crypto gate at Confirm.

---

## Repo Structure

Per-stage layout: raw markdown lives in each stage's `docs/`, and the stage's HTML page sits flat at the stage-folder root (for example `research/research.html`).

| Folder / File | What's inside |
|---|---|
| [`research/`](./research/) | **Foundation Research**: `docs/` (competitors, benchmark, lean-ux-canvas, aarrr, ux-patterns, and the `research.md` synthesis), `screens/` (competitor screenshots), and `research.html` |
| [`user-research/`](./user-research/) | **User Research + CJM**: personas + JTBD + the Customer Journey Maps (`docs/` incl. `cjm-as-is.md` / `cjm-to-be.md`; pages `personas.html`, `jtbd.html`, `cjm-as-is.html`, `cjm-to-be.html`) |
| [`ia/`](./ia/) | **Information Architecture**: `docs/sitemap.md` + `docs/flows.md` + `docs/pages/` (Detailed-layer sources `seo.md`, `system.md`); visualizations `ia.html` / `sitemap.html` / `flows.html` / `concept-map.html` (Basic) and `seo.html` / `system.html` (Detailed); `annotations/` (wireframe annotations, generated) |
| [`wireframes/`](./wireframes/) | **Grey-box wireframes**: 104 pages, every sitemap screen + all states + Favorites view + the 5 system pages, flow-linked, header / nav wired, clickable end to end. Owns structure and copy: a painted screen must not disagree with its grey twin |
| [`voice/`](./voice/) | **Voice & Microcopy**: `docs/voice.md` + `docs/microcopy.md` + `voice.html` |
| [`concept/`](./concept/) | **Concept**: the **Vault** visual language - `docs/references.md` (Refero) + `docs/concept.md` (designer taste, 5 attribute pairs, locked decisions); `concept.html` (the stand: palette / type / form / contrast); superseded explorations archived in `old/` |
| [`ui-visual/`](./ui-visual/) | **UI + Visual**: 106 documents, of which **105 are colour copies of the wireframes** in the Vault language and `overview.html` is the index of the tree rather than a screen in it. Both numbers are true and every count here says which it is. A screen carries no styles of its own: it links `components/index.css` and nothing else. The grey wireframes stay grey |
| [`components/`](./components/) | **The design system**: `tokens.css` (primitive + semantic + the light theme), `base.css`, one file per component, all reached through `index.css` |
| [`ui-kit/`](./ui-kit/) | **Rebuilt by hand, 2026-08-07 to 2026-08-08.** **All 57 pages of the plan**, counted 2026-08-12 by listing `ui-kit/*.html` and by parsing `_nav.js`, which agree: `overview`, **five** foundations (`colour`, `typography`, `geometry`, `icons`, `responsive`), a shelf per rung, all four (`vitrine` for the atoms, `molecules`, `organisms`, `patterns`) and **one page per atom, all twelve** (`button`, `iconbtn`, `chip`, `navitem`, `oddsbar`, `input`, `yesno`, `toast`, `skeleton`, `toggle`, `logo`, `platehead`), **one per molecule, all sixteen**, **one per organism, all thirteen** and **one per pattern, all six**, plus `_page.css` and the one route `_nav.js`. **This row said 55 in one place, 54 in another and called `responsive.html` the 57th page in a third**, because the enumeration it was added up from was still the four-foundation list. **A level is a shelf and a component is a page**, and every component has a row in `_nav.js` whether or not it has a page yet. **0 generators and 0 gates.** The vitrine that stood here (65 generated pages, 54 Python scripts, 41 gates, 145 MB of screenshots) was deleted in one commit and the product did not move a pixel; its writing is kept in [`docs/kit-archive/`](./docs/kit-archive/). The five reports are in [`ui-kit/docs/`](./ui-kit/docs/) |
| [`docs/`](./docs/) | **The record**: [`decisions.md`](./docs/decisions.md) (what was done and why, dated, newest first) and [`backlog.md`](./docs/backlog.md) (what is still open) |
| [`components/patterns/`](./components/patterns/) | **Design System (09)**, built: the second shelf of the system package, **6 files** for compositions that stand on three screens or more (`card-grid`, `browse-shell`, `detail-shell`, `list-head`, `position-list`, `action-bar`). They carry arrangement only: 59 declarations over 16 properties and not one colour, face, border or surface among them. The system itself stays in `components/` and did not move |
| Responsive (10) | **built, no folder**: the ladder is a registry in `components/tokens.css`, the record is `ui-kit/docs/responsive.md` and the stand is `ui-kit/responsive.html`, **the fifth foundation page of the kit and one of its 57** |
| Animation (11) | no folder: durations and easing become tokens, transitions go on the components that already carry a state |
| Handoff (12) | no folder: the vitrine is the handoff |

The old→new folder map is recorded in [`STRUCTURE.md`](./STRUCTURE.md).

---

## Status

This table is the only place a stage status is recorded. `CLAUDE.md` holds rules and no statuses;
the dated record of how each stage got here is in [`docs/decisions.md`](./docs/decisions.md).

| Stage | Status |
|---|---|
| Foundation Research | ✅ Done (competitors, benchmark, Lean UX Canvas, AARRR, UX patterns, synthesis; screens captured) |
| User Research (Personas + JTBD) | ✅ Done |
| CJM (As-Is + To-Be) | ✅ Done (Alex x MJ; As-Is emotional curve + 5 growth zones, To-Be map + MVP backlog; 2 pages) |
| Information Architecture (Basic + Detailed) | ✅ Done - Basic (flows + concept-map by intent) + Detailed (overview + sitemap + SEO layer + system nodes); flows color-coded by outcome + traced to CJM, jobs x screens matrix, no orphans. Detailed layer (targeted reconcile, since the wireframes already render pages): A-E SEO for the 5 indexed pages + footer, and 404 / 500 / 503 / cookie / toast grounded in law |
| Wireframes | ✅ Done (104 pages: all screens + states + Favorites + Event Detail tabs + 5 system pages, flow-linked, header / nav wired, critique pass). Stage-04 reconcile: system pages (404/500/503/cookie/toasts), footer trust strip + SEO links, story-led per-card "why" + SEO sections, Related events, Win F5 friction |
| Voice | ✅ Done (5 principles, lexicon, forbidden list, per-element rules; every screen rewritten line-by-line, closing audit clean) |
| Concept | ✅ Done - the **Vault** visual language: designer taste captured, 5 attribute pairs traced to data + borrowed technique, contrasting directions explored (Newsroom / Signal / Arena, archived to `concept/old/`), Vault chosen and locked; palette / type / form / photography / icons contrast-checked (WCAG AA) on the stand `concept.html` |
| UI + Visual | ✅ Done - every screen painted in Vault (106 today, 76 at the close of the stage; step 8 added the 28 category states); every one links exactly `components/index.css`. `/impeccable critique` 31 -> 38 / 40 |
| Tokens + Components | ✅ Done - two token levels, three geometry scales, **47 components** (41 in `components/` plus 6 in `components/patterns/`) alongside 5 files that are the substrate a screen stands on rather than a part of one (`base`, `course-chrome`, `fonts`, `index`, `tokens`), and a light theme as the proof of the semantic layer. **The level split is DECLARED and no longer computed**: **12 atoms, 16 molecules, 13 organisms and 6 patterns**, each with its reason, in [`ui-kit/docs/inventory.md`](./ui-kit/docs/inventory.md). **This row said 40, and 10 / 14 / 13 / 6, and that all three of `account`, `cookie-consent` and `toc` were marked unmeasured**; re-counted 2026-08-12 against the filesystem and the inventory, **all six of the unmeasured were walked on 2026-08-08 and `account` was deleted the same day**, which the next row already said. The reading this row used to carry, 6 atoms and 13 molecules and 21 organisms computed from the markup, was the arithmetic's blind spot: a component built from its own class names reads as containing nothing. The vitrine and its 41 gates were deleted on 2026-08-07 and were rebuilt by hand from five anchor screens. Nine audit passes (7 to 9) are recorded in [`docs/decisions.md`](./docs/decisions.md); the surfaces they stopped short of are in [`docs/backlog.md`](./docs/backlog.md) |
| Design System | ✅ Done - the patterns shelf (**6 files**, arrangement only) and the vitrine rebuilt by hand: **57 of 57 pages** (54 at the close of the stage; `logo`, `platehead` and `responsive` landed on 2026-08-11), a shelf per level plus a page per component, one route in `_nav.js`, **0 generators and 0 gates**. **Every component in `components/` has a page**, every page was measured in a browser at 390 and 1280 before it was written, and **all six components the inventory called unmeasured were walked and given a level on 2026-08-08**. Eleven backlog rows were found by writing the pages. Five reports in [`ui-kit/docs/`](./ui-kit/docs/): census, inventory, consolidation, audit, responsive. **The list here named four of the five**, the same defect as the four-foundation list; the registry lists all five. The audit ran once over 115 documents at two widths in two themes, **460 renders**, and **found eight defects in itself and one in the product**, the eighth being that it had measured the whole product with a mouse. The 44px touch floor is one rule in `base.css` since 2026-08-08. **One row stays open under this stage**: 28, the footer's dead links, and it is blocked on IA's item 27. The last unblocked one, 51, closed on 2026-08-08 when the cookie row became a `<label>` and the target went from 18x18 to 233x44 under a finger |
| Responsive | ✅ Done - **three rungs in `rem`, named by what arrives at them** (40rem DESK, 47.5rem DETAIL, 56.25rem RAIL, which are 640, 760 and 900 at the default browser font and move with it: at a 24px default the desk arrives at 960) plus a harness at 1140 that is not the product's, kept as a **registry** in `components/tokens.css` because `@media` cannot read a variable and the limitation is therefore the instrument: **32 width queries in the system, 0 in any of the 106 documents in `ui-visual/`** (it was 33 until 2026-08-14, and the count is re-taken from the comment-stripped source every time it is written down: 25 name one of the three rungs, 2 name the 1140 harness, 4 are one-offs carrying their reason beside themselves, and 1 is the course chrome's, which moved from `759.98px` to `47.49875rem` the same day because a boundary borrowed from another file has to be borrowed in that file's unit), and no number in a product query that is not on the list. The stage began with a **transcript** (twelve distinct widths already in the product, three of them on no ladder) and an **audit with one row per screen** (SAME 22, WIDER 82, **NEW BEHAVIOUR 0**, refused on `flows.md` rather than on taste). The shell fork is **A**, read off 03a and already built, and it was proved rather than designed: the bottom bar leaves the paint, the tab order and the accessibility tree at one pixel. **The type scale went to `rem` on 2026-08-12** (ten `--text-*` steps and eight `--display-*` clamps as ratios to the root, proved inert at the default with 0 differing font sizes of 44,547 readings, and a 24px-default reader goes from a 0.2 per cent longer page with no extra word to a 38.4 per cent longer one with every word), **and the RUNGS followed on 2026-08-13**, backlog 115 closed then 135 closed: 6,300 readings over 105 screens at twenty widths and three browser defaults give 0 horizontal scroll and exactly one navigation carrier everywhere, with 0 differing readings of 2,100 at the default. **The first instrument for it measured nothing**, because it set `html{font-size}` and a length in a media query resolves against the INITIAL font size and ignores every declaration on the root element. **`--measure:46ch` (it was `66ch` until the critique of 2026-08-12 found that `ch` is the advance of a zero and not a character), `--grid-col-min:300px`, `--rail-width:214px` and `--menu-min:196px` added; `--grid-gap`, a column-count token, a `--sticky-gap` and `rem` rungs all refused, each with its measurement.** Backlog **43 and 116 closed**, 115, 117 and 118 opened. The closing sweep is 320 to 1600 at 50 widths: **10,500 readings, 0 chasm widths, 5,250 carrier readings, 0 disagreements**, with a deliberate overflow seen 20 of 20 first, because 0 is also what a blind probe reports. The record is [`ui-kit/docs/responsive.md`](./ui-kit/docs/responsive.md) and the stand is [`ui-kit/responsive.html`](./ui-kit/responsive.html). **One finding of this stage was re-measured on 2026-08-12 and reversed**: the per-component width table was built from one placement each and three of its five FIXED verdicts were wrong, so it was retaken over every placement of all 47 components on the 105 screens at thirteen widths, with a control of 0 differing cells in 4,238. The counterpart reading is **10 of 47 filling everywhere, 26 of 47 with no query of their own, 8 of 47 both** rather than one number, and **the refusal of container queries no longer holds on the ground it was refused**: the threshold named was the first component standing in two columns of different widths, and **35 of 47 do**. The table, the method and the three components that carry the case (`card`, the `catnav` / `chip` rail pair, `navitem`) are in [`ui-kit/docs/inventory.md`](./ui-kit/docs/inventory.md), behaviour on width. **Backlog 129 answered it on 2026-08-13 and the threshold turned out to be the wrong test**: one component in two columns is necessary and not sufficient, because 35 of 45 components have no width behaviour at all, so the 52 selectors standing inside the 33 queries were classified instead (14 page frame, shell or harness, 2 a positioning context, 36 a component in a slot) and the 25 that stand on both sides of their own rung were tested for whether ANY container width divides the placements the way the rung does: **24 of 25 did**, so a container query would have resolved identically at every placement. **What the pass found instead was the opposite defect and it was one token**: `--gutter` and `--plate-inset` both STEPPED at 640, 38px a side spent at the pixel where the window gained one, so the content column went 611 to 560 and the feed card 577 to 502. Both ramp now from DESK to DETAIL, at a length that is derived and not chosen, and `card.css`'s query is gone because its rule was never about the window: **84 cards were cutting a pixel off a 44px target at every width from 640 to 1600.** Two queries left the registry and nothing replaced either |
| Animation | ⬜ Not started |
| Handoff | ⬜ Not started |

---

## Wireframes

Grey-box (low-fidelity) wireframes for the whole product, mobile-first and
responsive. Neutral greys only - no color, type, shadows, or finished UI (those
belong to the Concept phase). Open any file in [`wireframes/`](./wireframes/) in a
browser; a left screen-tree panel navigates the whole set.

**[View the main screen live](https://sergiodesign4u-dot.github.io/predict-market/wireframes/event-feed.html)** - opens the rendered Event Feed in any browser, no local server needed.

**Start here:** [`wireframes/event-feed.html`](./wireframes/event-feed.html) - the
main-flow entry (the Event Feed). From there the journey is clickable end to end:
Event Feed -> Event Detail -> sign-in / deposit gate -> Active Bets.

- **Coverage:** 104 pages - every screen in the IA screen tree, each state its own
  page. Event Feed, Event Detail (binary + multi, inline bet panel), 4 Category
  pages, Favorites view (Favorites), Sign In / Deposit (shared in-page dialogs), Win /
  Loss, Notifications, Wallet, My Profile / Public Profile, How It Works, Active
  Bets / Bet History.
- **Auth axis:** browse screens have logged-in and logged-out variants.
- **Flow-linked:** the main flow is clickable end to end (Event Feed -> Event
  Detail -> gate -> Active Bets), with branch exits and no dead-ends, wired and
  audited edge-by-edge against the routes in [`ia/docs/flows.md`](./ia/docs/flows.md)
  (loading -> success, error -> try again, empty -> filled; branches both ways).
- **Chrome wired:** header (Favorites / Notifications / avatar dropdown) and the
  mobile bottom nav are real links, not dead buttons; logged-out controls open the
  sign-in dialog.
- **Interface copy** rewritten line-by-line against the product voice
  ([`voice/docs/voice.md`](./voice/docs/voice.md)); the rewrite log and the read-only text
  inventory it was edited from live in [`voice/docs/microcopy.md`](./voice/docs/microcopy.md).
- **Quality gates:** 0 em-dash, 0 broken links, 0 style leaks; the defect passes
  are recorded in [`wireframes/_critique.md`](./wireframes/_critique.md) - two full
  critiques (the second a 2026-06-29 multi-agent re-audit), a flow-wiring audit
  against `ia/docs/flows.md`, a 99/99 coverage audit against `ia/docs/sitemap.md`, and a final
  six-category defect pass, all clean. The build contract is
  [`wireframes/_conventions.md`](./wireframes/_conventions.md).

---

## Voice

The product voice is **rules, not a mood** - every rule carries an example, an
anti-example, and the research line it comes from, so every UI line reads the same
whoever writes it.

- **[`voice/docs/voice.md`](./voice/docs/voice.md)** - the contract: five **principles**
  (explain the number, trust before the ask, speak to a spectator not a trader,
  design the loss / mark the win without a fuse, say the specific provable thing),
  a **lexicon** (event not market, bet not position, Add funds, Save, Sign in,
  Browse events, Confirm bet), a **forbidden** list (no "Something went wrong",
  greetings, celebrations, "successfully", exclamations, emoji, apologies, internal
  codes), and per-element **microcopy** rules.
- **[`voice/docs/microcopy.md`](./voice/docs/microcopy.md)** - the read-only text inventory
  (with same-thing / same-action / cliche flags) and the line-by-line rewrite log.
  Every screen was rewritten against the voice and the closing audit is clean.
  The Event Detail social panel was moved from trader vocabulary
  (Top Holders / Positions / shares) to spectator language (Biggest bets / Bets).
- **State tone:** errors say what happened and what to do (no joke, no apology),
  empty states give a way out, and results state the fact without celebrating
  (Win = "You were right", no confetti; Loss = "Here's what happened", no "bet
  again").

---

## Key Docs

Four files at the root, and each answers one question. **`CLAUDE.md` = the rules** that must act next
time (it is loaded into every session, so it stays short). **`PRODUCT.md` = what the product is.**
**`docs/decisions.md` = what was done and why**, dated, newest first. **`docs/backlog.md` = what is
still open.** A status lives in the table above and nowhere else.

- [CLAUDE.md](./CLAUDE.md) - **the rules**: how work is done here, what owns what, and the reason each rule exists now that no gate holds it
- [PRODUCT.md](./PRODUCT.md) - **the product**: JTBD, audience, market types, MVP scope, business model, compliance
- [docs/decisions.md](./docs/decisions.md) - **the record**: every stage and audit pass, with its date and its reasoning
- [docs/backlog.md](./docs/backlog.md) - **what is open**: 13 items, with the stage that owns each
- [STRUCTURE.md](./STRUCTURE.md) - the 12-stage layout and the old→new folder map
- [DESIGN.md](./DESIGN.md) - the shipped visual system (Vault): palette, type, form, tokens, contrast tables
- [wireframes/_conventions.md](./wireframes/_conventions.md) - **Wireframe contract**: grey-box rules, zones, nav, states, the build passes
- [wireframes/_critique.md](./wireframes/_critique.md) - **Wireframe critique**: defect tables and resolutions (Krok 9, 2026-06-29 re-audit, flow-wiring / coverage / final passes)
- [voice/docs/voice.md](./voice/docs/voice.md) - **Product voice**: five principles, lexicon, forbidden list, per-element rules
- [voice/docs/microcopy.md](./voice/docs/microcopy.md) - **Microcopy**: read-only text inventory + the line-by-line rewrite log
- [ia/docs/sitemap.md](./ia/docs/sitemap.md) - **IA source**: entities, screens, navigation, depth map, coverage matrix
- [ia/docs/flows.md](./ia/docs/flows.md) - **IA source**: four user flows (MJ, FJ2, FJ5+EJ3, SJ1)
- [research/docs/research.md](./research/docs/research.md) - **Research synthesis**: all research phases in one document (single source of truth)
- [research/docs/lean-ux-canvas.md](./research/docs/lean-ux-canvas.md) - **Lean UX Canvas v2**: the one-page strategy (problem, audience, hypotheses, riskiest assumption, first test)
- [user-research/docs/personas.md](./user-research/docs/personas.md) - **Personas**: Alex (primary), Dan, Maria, Loss-Prone overlay - with confidence levels and post-research updates
- [user-research/docs/jtbd.md](./user-research/docs/jtbd.md) - **JTBD**: full job hierarchy (MJ -> FJ/EJ/SJ/HJ), importance matrix, MVP conclusions
- [research/docs/aarrr.md](./research/docs/aarrr.md) - AARRR framework: acquisition, activation, retention, revenue, referral
- [research/docs/competitors.md](./research/docs/competitors.md) - Full competitor comparison: HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, differences, open questions
- [research/docs/benchmark.md](./research/docs/benchmark.md) - Trust benchmark: 5 products x 8 criteria, top mechanisms for MVP
- [research/docs/ux-patterns.md](./research/docs/ux-patterns.md) - UX patterns: 5 approaches, behavioral analysis, pattern selection for MVP
