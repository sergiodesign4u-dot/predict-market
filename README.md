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
| [`wireframes/`](./wireframes/) | **Grey-box wireframes**: 104 pages, every sitemap screen + all states + Favorites view + the 5 system pages, flow-linked, header / nav wired, clickable end to end. Owns structure and copy: gate 18 fails the build when a painted screen disagrees with its grey twin |
| [`voice/`](./voice/) | **Voice & Microcopy**: `docs/voice.md` + `docs/microcopy.md` + `voice.html` |
| [`concept/`](./concept/) | **Concept**: the **Vault** visual language - `docs/references.md` (Refero) + `docs/concept.md` (designer taste, 5 attribute pairs, locked decisions); `concept.html` (the stand: palette / type / form / contrast); superseded explorations archived in `old/` |
| [`ui-visual/`](./ui-visual/) | **UI + Visual**: 105 color copies of the wireframes in the Vault language. A screen carries no styles of its own: it links `components/index.css` and nothing else. Generated and reconciled by `_apply_theme.py`; the grey wireframes stay grey |
| [`components/`](./components/) | **The design system**: `tokens.css` (primitive + semantic + the light theme), `base.css`, one file per component, all reached through `index.css` |
| [`ui-kit/`](./ui-kit/) | **The vitrine and the gates**: a stand page per component, the token page, the icon sheet, the stage's five documents rendered as pages, and `_check_kit.py` (<!-- gates:start -->**41 gates** in 109 checks<!-- gates:end -->) |
| [`docs/`](./docs/) | **The record**: [`decisions.md`](./docs/decisions.md) (what was done and why, dated, newest first) and [`backlog.md`](./docs/backlog.md) (what is still open) |
| `components/patterns/` | **Design System (09)**, not built yet: the second shelf of the system package, for compositions that stand on three screens or more. The system already lives in `components/` and does not move there |
| Responsive (10) | no folder: the breakpoints go into `components/tokens.css` by the mechanism already there |
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
| UI + Visual | ✅ Done - every screen painted in Vault (105 today, 76 at the close of the stage; step 8 added the 28 category states); every one links exactly `components/index.css`. `/impeccable critique` 31 -> 38 / 40 |
| Tokens + Components | ✅ Done - two token levels, three geometry scales, <!-- counts:start -->**41 components**, 39 of them composed on three levels (7 atoms, 13 molecules, 19 organisms, computed from the markup) and 2 that are the substrate a screen stands on rather than a part of one (`base`, `course-chrome`)<!-- counts:end -->, 48 pages in the vitrine (36 stands + the token page, the icon sheet and the stage's five documents), <!-- gates:start -->**41 gates** in 109 checks<!-- gates:end -->, and a light theme as the proof of the semantic layer. Nine audit passes (7 to 9) are recorded in [`docs/decisions.md`](./docs/decisions.md); the surfaces they stopped short of are in [`docs/backlog.md`](./docs/backlog.md) |
| Design System | ⬜ Not started |
| Responsive | ⬜ Not started |
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

- [CLAUDE.md](./CLAUDE.md) - **the rules**: how work is done here, what owns what, which gate holds it
- [PRODUCT.md](./PRODUCT.md) - **the product**: JTBD, audience, market types, MVP scope, business model, compliance
- [docs/decisions.md](./docs/decisions.md) - **the record**: every stage and audit pass, with its date and its reasoning
- [docs/backlog.md](./docs/backlog.md) - **what is open**: 14 items, with the stage that owns each
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
