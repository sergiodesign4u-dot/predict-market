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
| [`ia/`](./ia/) | **Information Architecture**: `docs/sitemap.md` + `docs/flows.md` (sources), `ia.html` / `sitemap.html` / `flows.html` (visualizations), and `annotations/` (wireframe annotations, generated) |
| [`wireframes/`](./wireframes/) | **Grey-box wireframes**: 99 pages, every sitemap screen + all states + Favorites view, flow-linked, header / nav wired, clickable end to end |
| [`voice/`](./voice/) | **Voice & Microcopy**: `docs/voice.md` + `docs/microcopy.md` + `voice.html` |
| [`concept/`](./concept/) | Concept: visual direction, moodboard |
| [`ui-visual/`](./ui-visual/) | UI + Visual design |
| [`tokens-components/`](./tokens-components/) | Design tokens + UI component specs |
| [`design-system/`](./design-system/) | Full design system documentation |
| [`responsive/`](./responsive/) | Responsive design pass |
| [`animation/`](./animation/) | Motion + animation |
| [`handoff/`](./handoff/) | Dev-ready specs and assets |

The old→new folder map is recorded in [`STRUCTURE.md`](./STRUCTURE.md).

---

## Status

| Stage | Status |
|---|---|
| Foundation Research | ✅ Done (competitors, benchmark, Lean UX Canvas, AARRR, UX patterns, synthesis; screens captured) |
| User Research (Personas + JTBD) | ✅ Done |
| CJM (As-Is + To-Be) | ✅ Done (Alex x MJ; As-Is emotional curve + 5 growth zones, To-Be map + MVP backlog; 2 pages) |
| Information Architecture (Basic + Detailed) | ✅ Done (sources + 3 visualizations, synced) |
| Wireframes | ✅ Done (99 pages: all screens + states + Favorites view + Event Detail tabs, flow-linked, header / nav wired, critique pass) |
| Voice | ✅ Done (5 principles, lexicon, forbidden list, per-element rules; all 99 pages rewritten) |
| Concept | ⬜ Not started |
| UI + Visual | ⬜ Not started |
| Tokens + Components | ⬜ Not started |
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

- **Coverage:** 99 pages - every screen in the IA screen tree, each state its own
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
  Every screen was rewritten against the voice; the closing audit is clean across
  all 99 pages. The Event Detail social panel was moved from trader vocabulary
  (Top Holders / Positions / shares) to spectator language (Biggest bets / Bets).
- **State tone:** errors say what happened and what to do (no joke, no apology),
  empty states give a way out, and results state the fact without celebrating
  (Win = "You were right", no confetti; Loss = "Here's what happened", no "bet
  again").

---

## Key Docs
- [CLAUDE.md](./CLAUDE.md) - full project brief, principles, scope, IA summary
- [STRUCTURE.md](./STRUCTURE.md) - the 13-stage layout and the old→new folder map
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
