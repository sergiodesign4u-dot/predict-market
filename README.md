# Prediction Market Platform

A mobile-first Web3 platform for prediction markets. Users bet YES/NO on real-world events using stablecoins (USDC/USDT). Outcomes resolve against reality.

**Core bet:** better clarity and onboarding than existing competitors (Polymarket, Kalshi).
**Audience:** 20-40, trust-driven.
**Platform:** Mobile-first web, then responsive desktop.

---

## Live Research Summary

**[View research.html live](https://sergiodesign4u-dot.github.io/predict-market/research.html)**

Single-page summary of all research phases. Open the link above in any browser - no local server needed.

---

## Repo Structure

| Folder / File | What's inside |
|---|---|
| [`IA/sitemap.md`](./IA/sitemap.md) | **IA source**: entities, screens, navigation design, depth map, coverage matrix |
| [`IA/flows.md`](./IA/flows.md) | **IA source**: four user flows (MJ, FJ2, FJ5+EJ3, SJ1) in Mermaid |
| [`ia.html`](./ia.html) | **IA Overview** visualization: screen tree, nav, depth, MJ flow, coverage summary |
| [`sitemap.html`](./sitemap.html) | **Sitemap** visualization: full entity/screen/nav/tracing detail |
| [`flows.html`](./flows.html) | **Flows** visualization: all four flows rendered as Mermaid diagrams |
| [`research/`](./research/) | Competitor analysis, strategy, JTBD, personas, AARRR |
| [`research/screens/`](./research/screens/) | Competitor screenshots |
| [`wireframes/`](./wireframes/) | **Grey-box wireframes**: 99 pages, every sitemap screen + all states + Favorites view, flow-linked, header / nav wired, clickable end to end |
| [`concept/`](./concept/) | Visual direction, moodboard |
| [`tokens/`](./tokens/) | Design tokens: color, type, spacing |
| [`components/`](./components/) | UI component specs |
| [`design-system/`](./design-system/) | Full design system documentation |
| [`handoff/`](./handoff/) | Dev-ready specs and assets |

---

## Status

| Phase | Status |
|---|---|
| Brief | ✅ Done |
| Research | ✅ Done (competitive analysis, screens captured) |
| IA (sitemap + flows) | ✅ Done (sources + 3 visualizations, synced) |
| Wireframes | ✅ Done (99 pages: all screens + states + Favorites view + Event Detail tabs, flow-linked, header / nav wired, critique pass) |
| Concept | ⬜ Not started |
| Design system | ⬜ Not started |
| Components | ⬜ Not started |
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
  audited edge-by-edge against the routes in [`IA/flows.md`](./IA/flows.md)
  (loading -> success, error -> try again, empty -> filled; branches both ways).
- **Chrome wired:** header (Favorites / Notifications / avatar dropdown) and the
  mobile bottom nav are real links, not dead buttons; logged-out controls open the
  sign-in dialog.
- **Interface copy** rewritten line-by-line against the product voice
  ([`voice/voice.md`](./voice/voice.md)); the rewrite log and the read-only text
  inventory it was edited from live in [`voice/microcopy.md`](./voice/microcopy.md).
- **Quality gates:** 0 em-dash, 0 broken links, 0 style leaks; the defect passes
  are recorded in [`wireframes/_critique.md`](./wireframes/_critique.md) - two full
  critiques (the second a 2026-06-29 multi-agent re-audit), a flow-wiring audit
  against `IA/flows.md`, a 99/99 coverage audit against `IA/sitemap.md`, and a final
  six-category defect pass, all clean. The build contract is
  [`wireframes/_conventions.md`](./wireframes/_conventions.md).

---

## Voice

The product voice is **rules, not a mood** - every rule carries an example, an
anti-example, and the research line it comes from, so every UI line reads the same
whoever writes it.

- **[`voice/voice.md`](./voice/voice.md)** - the contract: five **principles**
  (explain the number, trust before the ask, speak to a spectator not a trader,
  design the loss / mark the win without a fuse, say the specific provable thing),
  a **lexicon** (event not market, bet not position, Add funds, Save, Sign in,
  Browse events, Confirm bet), a **forbidden** list (no "Something went wrong",
  greetings, celebrations, "successfully", exclamations, emoji, apologies, internal
  codes), and per-element **microcopy** rules.
- **[`voice/microcopy.md`](./voice/microcopy.md)** - the read-only text inventory
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
- [wireframes/_conventions.md](./wireframes/_conventions.md) - **Wireframe contract**: grey-box rules, zones, nav, states, the build passes
- [wireframes/_critique.md](./wireframes/_critique.md) - **Wireframe critique**: defect tables and resolutions (Krok 9, 2026-06-29 re-audit, flow-wiring / coverage / final passes)
- [voice/voice.md](./voice/voice.md) - **Product voice**: five principles, lexicon, forbidden list, per-element rules
- [voice/microcopy.md](./voice/microcopy.md) - **Microcopy**: read-only text inventory + the line-by-line rewrite log
- [IA/sitemap.md](./IA/sitemap.md) - **IA source**: entities, screens, navigation, depth map, coverage matrix
- [IA/flows.md](./IA/flows.md) - **IA source**: four user flows (MJ, FJ2, FJ5+EJ3, SJ1)
- [research/master-research.md](./research/master-research.md) - **Master synthesis**: all research phases in one document
- [research/strategy.md](./research/strategy.md) - **Strategy**: objectives, audience segments, business model, riskiest assumption (replaces product-model.md)
- [research/personas.md](./research/personas.md) - **Personas**: Alex (primary), Dan, Maria, Loss-Prone overlay - with confidence levels and post-research updates
- [research/jtbd.md](./research/jtbd.md) - **JTBD**: full job hierarchy (MJ → FJ/EJ/SJ/HJ), importance matrix, MVP conclusions
- [research/aarrr.md](./research/aarrr.md) - AARRR framework: acquisition, activation, retention, revenue, referral
- [research/competitive-analysis.md](./research/competitive-analysis.md) - Full competitor comparison: HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, differences, open questions
- [research/benchmark-trust.md](./research/benchmark-trust.md) - Trust benchmark: 5 products × 8 criteria, top mechanisms for MVP
- [research/ux-patterns.md](./research/ux-patterns.md) - UX patterns: 5 approaches, behavioral analysis, pattern selection for MVP
- [research/product-model.md](./research/product-model.md) - Prior product model (history, preserved)
