# CLAUDE.md - Prediction Market Platform

## Project Overview
A mobile-first prediction market platform where users bet YES/NO on real-world events.
Users stake crypto on whether an event will happen or not, and earn/lose based on the outcome.

## JTBD - Jobs To Be Done

**Primary:**
> "When I follow events that matter to me - I want to have real skin in the game, so it's not just news, but my personal stake with a real outcome"

**Secondary:**
> "And if I understand the situation better than others - I want that to convert into money, simply and without the complexity of trading"

**Product implications:**
- First page - live events happening now, not "sign up"
- Onboarding: event → mechanics → bet (not the other way around)
- Retention: notifications about events, not about topping up balance
- Profile: prediction track record as reputation

---

## Core Differentiator
**Clarity and accessibility for new users.** Competitors (Polymarket, Kalshi, Manifold) can feel opaque to newcomers. This platform prioritizes transparency - users always understand what they're doing, why, and what happens next.

## Target Audience
- Age: 20–40
- Primary driver: **Trust** - the platform must feel credible, transparent, secure
- Secondary: Engagement - users come back to follow events they bet on

## Platform
- **Mobile-first web** → then responsive desktop
- Web3 / blockchain-based

---

## Product

### Market Types (MVP)
- **Binary markets** - YES / NO on a single event
- **Multi-outcome markets** - multiple options, each with YES / NO
- **Frequency (orthogonal to type, added in the wireframe pass)** - markets are one-time or recurring (Hourly / Daily / Weekly / Monthly). Powers the Frequency filter on the Event Feed. Resolution mechanics for recurring markets to be detailed (each cadence instance resolves on its own schedule). See `ia/docs/sitemap.md` Event entity.

### Event Resolution
- Events are real-world occurrences
- Platform team creates and resolves events (MVP)
- Resolution mechanism: AMM-style dynamic pricing - payout depends on *when* the bet was placed, not just the outcome
- If you bet YES and event doesn't happen → you lose (partial loss based on timing of stake)

### Categories
- MVP: Politics, Crypto, Culture, General
- Post-MVP: Sports and expansion based on interest/demand

### MVP Feature Scope
Sharpened by the CJM To-Be backlog (`user-research/docs/cjm-to-be.md`, Alex x main job). One list, ordered by the To-Be path. The motivation features (story-led entry, explain the number) are co-equal MVP with the friction fixes, since the riskiest assumption "the barrier is friction, not motivation" was substantially refuted (research §9 F4).
- Story-led event feed as the first page (live events, not a signup) - the motivation entry
- "Explain the number": plain-language odds + one-line why + the news story, spectator language (not trader)
- Browse and form the bet intent with no wallet upfront; the auth / crypto gate fires at Confirm, not at entry (the core clarity inversion)
- User account via social login (Google, X)
- Fiat on-ramp (card -> stablecoin); a crypto wallet stays available for crypto-native users but is not required until Confirm
- One plain funds-safety line before deposit ("USDC held 1:1, we never lend it") + the fee shown before Confirm
- Confirm with AMM price reconcile if the price moved (S5)
- Binary YES/NO and multi-outcome markets (multi is product scope, not CJM-derived)
- $1 / $5 bet sizing (low min, $5 default); the size that feels "real but not scary" is a `[?]` to test
- Active Bets + outcome / position notifications (retention anchor)
- Win screen ("You were right") + share, with overconfidence friction; Loss screen ("Here's what happened") with context and a next step that is NOT "bet again"
- Transparent resolution + a resolved-markets count (against the #1 trust killer: platform betrayal)
- Post-MVP / Later: Leaderboard, Staking (TBD) - orphans relative to this CJM; Sports (needs Maria's own CJM)

---

## Business Model
- **Commission per bet** (primary) - exact % TBD, needs competitive research
- Spread - possible secondary model
- No subscriptions
- No min/max bet limits at launch (Polymarket uses $0.01 minimum - research needed)

---

## Financials & Compliance
- **All transactions in crypto** - stablecoins (USDC, USDT) as primary
- Fiat on-ramp supported (user converts fiat → crypto on platform)
- **KYC**: Required for fiat deposits; crypto-only users - KYC TBD (Polymarket operates without KYC for crypto)
- **Geo**: Global, with geo-restrictions based on regulatory requirements (no US for real-money prediction markets)

---

## Competitors & Research
| Platform | Notes |
|---|---|
| Polymarket | AMM model, good mobile UX, 3-level nav can be complex for new users |
| Kalshi | US-regulated, fiat-based |
| Manifold Markets | Play money, social focus |
| Metaculus | Forecasting community, no real money |

**Research still needed:**
- Commission rates across competitors
- Min/max bet limits
- KYC thresholds
- Specific blockchain/chain selection (Ethereum, Polygon, Base, etc.)
- AMM mechanism specifics

---

## Design Principles
1. **Clarity first** - every screen should be self-explanatory; new users should never feel lost
2. **Trust signals everywhere** - transparent odds, clear resolution rules, audit trail
3. **Mobile-first** - design for thumb, test on mobile before desktop
4. **Engagement loops** - notify users about events they care about, show live odds movement

---

## Tech Stack (TBD)
- Frontend: Web (mobile-first)
- Blockchain: Web3, specific chain TBD (likely Polygon, Base, or Arbitrum for low fees)
- Wallet connection: WalletConnect / MetaMask + social login
- Smart contracts: AMM-based market resolution

---

## Timeline
~3 months to MVP

## Team
Solo - product, design, and development

---

## Information Architecture

IA sources (source of truth): `ia/docs/sitemap.md` (entities, screens, navigation, desktop layer, depth map, tracing), `ia/docs/flows.md` (user flows), and the Detailed-layer page sources `ia/docs/pages/seo.md` (the A-E SEO structural layer) + `ia/docs/pages/system.md` (system / global nodes). The HTML visualizations `ia/ia.html`, `ia/sitemap.html`, `ia/flows.html`, `ia/concept-map.html`, `ia/seo.html`, `ia/system.html` render the markdown; the markdown stays the source of truth if they ever diverge.

**Repo layout:** 13-stage course structure, one folder per stage, raw markdown in each stage's `docs/` and the stage HTML flat at the folder root. Full map in `STRUCTURE.md`. User Research now has 4 pages (Personas, JTBD, CJM As-Is, CJM To-Be); CJM (As-Is + To-Be) is a separate status row and lives inside User Research. The CJM sharpens the MVP scope above (one version, not a fork).

### Detailed layer (Stage 03b) - DONE (targeted reconcile)

Three decisions that govern every page-level IA node:
- **Stance: mobile-first, fully adaptive.** Desktop <-> mobile responsive, but mobile is the priority; block priority and the first screen are reasoned from mobile (base 360px). Desktop is designed deliberately, not derived.
- **Two IA layers.** Global (Stage 03a - concept-map + flows, done) answers "where can the user go"; per-page (this layer) answers "what is on each page and how it behaves" (blocks, states, components, SEO).
- **SEO-ahead.** The structural SEO layer (URL/slug, H1/H2, breadcrumbs, schema.org, indexation, internal-linking) is defined here in IA. The wireframe validates layout only; production supplies final content + real query volumes. The three are not mixed, so finding "a block is missing" never means redrawing a wireframe.

**Scope = targeted reconcile (2026-07-12), not the full node-by-node build.** The 99 wireframes already exist and ARE the per-page B/W render, so we do NOT redraw pages, write a `pages/*.md` per screen, add an `ia/_nav.js`, or renumber the sitemap to X.Y (all would duplicate the wireframes or `resync_sidebar.py`). We build only what the wireframes deliberately omit and a launch needs:
- the **A-E SEO structural layer** for the indexed public pages (Event Feed, Event Detail, Category, How It Works, Public Profile); every private/transactional zone is `noindex`, no schema;
- the **footer** as an SEO / internal-linking node;
- the **system / global nodes** (404, 500, maintenance 503, cookie-consent grounded in law, toasts).

New sources live in `ia/docs/pages/` (`seo.md`, `system.md`); rendered B/W as `ia/seo.html`, `ia/system.html`. The shared sidebar stays single-source via `resync_sidebar.py` (not `_nav.js`); new IA pages register there.

**Built (2026-07-12).** `seo.md` carries the indexation policy (every screen family index vs noindex) + the A-E template + full A-E for Event Feed, Event Detail (with the per-event schema decision: `WebPage` + `BreadcrumbList`, `schema.org/Event` rejected), Category, How It Works, Public Profile, and the footer node. `system.md` carries 404 / 500 / 503 / cookie-consent (grounded in GDPR + ePrivacy + UA Law 2297-VI, cited) / toasts; Search stays deferred. Both render to `ia/seo.html` + `ia/system.html`, wired into the shared sidebar under IA > Detailed layer (SEO layer, System nodes) on all pages. `sitemap.md` registers the system + footer/legal destinations (SYSTEM AND GLOBAL). Link check: 27 pages, 743 links, 0 broken. Deliberately not done (would duplicate the wireframes): per-screen B/W redraws, `pages/*.md` per screen, `ia/_nav.js`, X.Y renumbering.

### Top-level navigation (revised in the wireframe pass)

Mobile-first. Mobile = bottom nav, 4 slots with icons; desktop = lean header (no center nav row). Full rationale in `ia/docs/sitemap.md` Desktop layer.

Mobile bottom nav - 4 slots:

| Slot | Label | Opens | Jobs |
|---|---|---|---|
| 1 | Events | Event Feed (the logo is also Events/home on desktop) | FJ1, FJ2, MJ |
| 2 | My Bets | Active Bets (Active + History tabs) | EJ1, MJ, FJ5, EJ3 |
| 3 | Favorites | Favorites view (a filter over the feed) | FJ1 (return / watchlist) |
| 4 | Portfolio | My Profile + a portfolio summary (account hub); shows the balance figure in place of an icon | SJ1, SJ2, FJ4 |

Desktop lean header: logo = Events/home; hamburger (reserved for scaling); right utility cluster = Portfolio/Cash balance swap, Favorites (heart), Notifications (bell + permanent badge), avatar dropdown (My Profile, My Bets, Wallet/Deposit, How It Works, Logout). Categories are a second-level sub-nav band under the header; the feed heading echoes the active category and the sort is a dropdown on that row. Notifications is a header bell on both breakpoints (badge = retention anchor), not a bottom slot. Money stays a utility, not a primary destination (G4 spirit; refined - the Portfolio slot surfaces a balance but opens the account hub, not a bare wallet).

### Primary screen hierarchy

- Level 0: Event Feed, Active Bets (My Bets), Favorites view (Favorites), Portfolio hub (My Profile + balance). Notifications is reached via the header bell.
- Level 1: Event Detail (under Events); Wallet/Deposit and How It Works (avatar dropdown, footer, and the Portfolio hub).
- Flow/invoked: Bet Screen, Win Screen, Loss Screen, Sign In/Register, Deposit, Public Profile

### Depth to main job (Alex, News Junkie)

- MJ path: Events (L0) - Event Detail (1 tap) - Bet Screen (2 taps) - gate fires at Confirm (3 taps). Within 3-tap rule.
- G1 retention path: resolution notification - Loss Screen directly, 1 tap.
- G1-equivalent win path: win notification - Win Screen directly, 1 tap (SJ1 share impulse window preserved).
- Re-deposit: invoked from Bet Screen insufficient-balance state, 1 step in context.

### Main flow (MJ)

Event Feed - found event - Event Detail - YES/NO tap - Bet Screen (intent) - Confirm gate - two branches:
- News Junkie: Sign In/Register - Deposit - S5 reconcile - Bet Screen (execute) - Active Bets.
- Crypto Native: wallet connect - S5 reconcile - Bet Screen (execute) - Active Bets.

S5 = AMM price reconcile node (price may move during auth/deposit). Four flows total: MJ, FJ2 (understand odds), FJ5+EJ3 (conscious loss exit with friction node), SJ1 (win share, overconfidence friction per F5).

---

## Wireframes

Grey-box (low-fidelity) wireframes for the whole product live in `wireframes/`. Contract: `wireframes/_conventions.md` (grey-box rules, zones, nav, states, mobile-first, no em-dash, the build passes). Critique log: `wireframes/_critique.md`.

- **Status: complete, plus a Stage-04 reconcile (2026-07-12).** 104 pages - every screen in the IA screen tree, each state its own page, plus the Favorites view (`favorites.html` + empty + loading) and the 5 system/global pages added in the reconcile (`404` / `500` / `maintenance` / `cookie-consent` / `toasts`). Orphans `[SIROTA]` (Settings, Leaderboard, Help/FAQ) unbuilt by design; the standalone Bet Screen is dissolved into the inline Event Detail bet panel.
- **Stage-04 reconcile (wireframes vs the new IA Detailed layer + CJM):** the 99 wireframes predated the IA Detailed layer (03b) and the CJM, so Stage 04 ran as a targeted reconcile that rendered the newly-specced IA and closed two CJM gaps, all voice-safe (new pages hand-authored; shared/global changes by idempotent in-place post-processors; `gen_*.py` never re-run). Added: the 5 system pages (from `system.md`); a footer trust strip (USDC 1:1) + "Popular right now" SEO block + real hrefs + Cookie-preferences re-entry (all 87 footer pages, `footer_reconcile.py`); a per-card story-led "why" + below-fold SEO sections on the feed (`feed_reconcile.py`) and category pages (`category_reconcile.py`); a Related-events block on Event Detail (`related_events.py`); and the Win F5 overconfidence-friction ("Before the next one", no "bet again"). Course Stage-04 infra (`screens.md`/`_nav.js`/`_wf.css`/`index.html`) was skipped as EQUIVALENT to ours (`_screens.md` + `_shell.py nav_tree`/`resync.py` + inlined CSS + the per-page screen-tree). New copy logged in `voice/docs/microcopy.md` (Steps 15-20); the reconcile audit + fixes are in `wireframes/_critique.md`. Gates: 104 pages, 16061 internal links, 0 broken, 0 em-dash.
- **Style:** neutral greys only - no color, type, shadows, icons-as-art, or finished UI (those are the Concept phase). Monochrome outline SVG icons only. A left screen-tree panel is on every page.
- **Annotations moved out (2026-07-03):** the wireframes are now clean grey-box UI only. The inline `zone:` chips and the bottom `.side` block (the `zone -> job / finding` annotation list + nav-tree / header-model / responsive / variant notes) were extracted into a dedicated IA visualization at **`ia/annotations/`** - one HTML page per screen family, every state inside it, each state showing a nested zone map + its annotations + a link to the live wireframe, plus shared structure/flow notes. Entry point: `ia/annotations/index.html`. Styled in the dark research/IA-viz theme and wired into the **shared left sidebar** as "Wireframe Annotations" (under the Plan section, after Wireframes) on all root viz pages (`research/personas/jtbd/ia/sitemap/flows.html`); the annotation pages carry that same sidebar (with a sub-link per screen). Generated + stripped idempotently by `wireframes/_generators/ia_annotations.py` (`build` then `strip`; run `build` before `strip`). IA source of truth stays `ia/docs/sitemap.md` + `ia/docs/flows.md`.
- **States & auth:** browse screens (Event Feed, Event Detail, Category pages) have logged-in and logged-out variants; each screen carries its full state set (loading/empty/error/success + product-specific). Public Profile and How It Works carry the logged-out header (reached pre-auth).
- **Flow-linked:** the main flow is clickable end to end (Event Feed -> Event Detail -> gate dialogs -> Active Bets) with branch exits and no dead-ends, wired along `ia/docs/flows.md`. Sign In / Deposit are shared in-page `<dialog>`s; Win / Loss are invoked overlays. A 2026-07-07 flow-wiring audit (step 7) verified every edge against `ia/docs/flows.md` and fixed the last naked recovery buttons (`Try again` on the Event Feed + Category error pages, `Try another card` on `deposit-error-card`); see `wireframes/_critique.md`.
- **Interface copy rewritten against the product voice (2026-07):** every UI line was edited line-by-line against `voice/docs/voice.md` (five principles + lexicon + forbidden + per-element rules). `voice/docs/microcopy.md` holds the read-only text inventory it was edited from plus the full rewrite log (all screen families done, incl. the step-13 "rest of the screens" pass). The wireframes stay the render surface; to change shipped copy, edit the HTML and log it there.
- **Chrome wiring:** header (Favorites -> Favorites view, bell -> Notifications, avatar dropdown -> Profile/My Bets/Wallet/How It Works/Logout) and the mobile bottom nav are real links, not dead buttons; logged-out controls open the sign-in dialog. Favorites resolves to the Favorites view. A `How it works` button sits in the header next to the logo and opens a native `<dialog>` quick-explainer (the feed's three explainer sections + a link to the full How It Works page); self-contained `.hiw-*` styling, on all 87 header pages via the idempotent `howitworks.py` post-processor (Step 21, `voice/docs/microcopy.md`). See `wireframes/_conventions.md` Shared chrome wiring. Applied by the idempotent `fixpack.py` post-processor.
- **Event Detail content tabs:** below the event content, a Polymarket-style tab strip (CSS-only radio switch, no JS) - **Comments** (sort + composer with likes/replies; logged-out prompts sign-in), **Biggest bets** (YES/NO columns), **Bets** (table Bettor/Side/Amount; your bet highlighted when logged in), **Activity** (recent-bets feed). On binary + multi + resolved, logged-in and logged-out. Rewritten from trader vocabulary (Top Holders / Positions / shares / "bought N YES at $X") to spectator language in the voice step-14 pass; see `voice/docs/microcopy.md`.
- **Generated, not hand-authored (but generators are now STALE):** pages were built by Python generators in `wireframes/_generators/` from a shared shell that extracts canonical CSS/footer/scripts from `event-feed.html`, so chrome stays byte-identical. **The voice/microcopy rewrite (Steps 05-14) was applied to the HTML by hand, not back-ported to the generators**, so `gen_event_detail.py` et al. still hold pre-rewrite copy - do NOT regenerate without back-porting, or the rewrite reverts. Pages are hand-maintained from here. To change shared *chrome* only, use the idempotent post-processors (`fixpack.py`).
- **Quality gates:** 0 em-dash, 0 broken internal links, 0 style leaks; consistency reconciled across all families (Krok 8) and multiple defect passes applied, all recorded in `wireframes/_critique.md`: Krok 9, the 2026-06-29 multi-agent re-critique (all 99 pages across five families - clean bar one minor clarity fix on `event-detail-resolved.html`, live "now" odds reframed as "Trading closed / at close"), then the 2026-07-07 finalization trio - a flow-wiring audit (step 7), a 99/99 coverage audit against `ia/docs/sitemap.md` (step 8, every sitemap screen + state has a page; deliberate exclusions documented), and a final six-category defect pass (step 9: style leak / placeholders / missing states / dead-ends / zone-without-action / off-map - all clean).

---

## Voice

Product voice + microcopy live in `voice/`. The voice is **rules, not a mood**: every rule has an example, an anti-example, and the `personas.md` / `research.md` line it derives from, so any line - written by a human or by Claude - comes out the same.

- **`voice/docs/voice.md`** (the contract) - five **Principles** (1. explain the number, never just show it · 2. one plain sentence of trust before the ask, never borrowed authority · 3. speak to a spectator with an opinion, not a trader · 4. design the loss, mark the win without lighting a fuse · 5. say the specific provable thing, not a superlative), then the **Lexicon** (one concept -> one word: event not market, bet not position, Add funds not Deposit, Save into Favorites, Sign in, Browse events, Confirm bet), the **Forbidden** list (no "Something went wrong" / "Welcome" / "Congratulations" / "successfully" / exclamations / emoji / apologies / internal codes / motivational tone), and the per-element **Microcopy** rules (button, heading, field, empty, error, loading, success, dangerous action).
- **`voice/docs/microcopy.md`** - the read-only text **inventory** (every UI line, with same-thing / same-action / cliche flags) and the **rewrite log** (Steps 05-14): every screen family rewritten line-by-line against `voice.md`. The wireframes are the render surface; **to change shipped copy, edit the HTML and add a was/became row to the log** (the table stays the source of truth - no line in a screen outside the table). User-written content (event questions, comments, usernames, sample figures) is never rewritten.
- **State tone** is set by the rules: the error names what happened and what to do (no joke, no apology), the empty state gives a way out, success states the fact and the next step without celebrating (Win = "You were right", no confetti; Loss = "Here's what happened", no "bet again").
- **Status: complete.** Lesson 05 steps 1-7 done; the step-7 finalization audit (Step 14 in the log) is clean - 0 lexicon/forbidden violations in product copy across all 99 pages (excluding the brand name "Predict Market", the voice-sanctioned "the market resolved YES/NO", and the AMM mechanics gloss).

---

## Concept (Stage 07) - DONE

The visual language, decided as **rules traced to data + taste**, not a mood. Sources in `concept/docs/`: `references.md` (Refero research, dark base) and `concept.md` (designer taste captured verbatim + 5 attribute pairs A1-A5, each traced to a data line and a borrowed technique + the locked decisions). Explored across contrasting directions (Newsroom after dark / Signal / Arena, then a Signal refinement); those exploration stands were archived to `concept/old/pre-vault-3d/` when Vault won. The chosen-and-refined stand is `concept/concept.html` (Vault). The full shipped visual system is documented in **`DESIGN.md`**.

**Locked - Direction: Vault (2026-07-16; superseded the earlier Signal exploration):**
- **Vault** - graphite canvas (page `#0f1013`, device `#141619`), matte **brass** brand (`#c7a24e`, text-safe `#d7ac53`) + **bronze** `#6e5a2e`; **green = YES / red = NO reserved as outcome semantics only** (brass never collides with the win/lose color); real event photography + **two-stone embossed plates** with inset brass hairlines + notched corners, cards that float. Fonts: **Space Grotesk** (display), **DM Sans** (body), **IBM Plex Mono** (numbers/mono).
- Binary feed card = **treatment B** (odds bar), multi-outcome = **treatment D** (option rows). Reference screen for the color pass = `event-feed.html`.
- All accent/text-on-graphite pairs contrast-checked WCAG AA on the stand. Full system: `DESIGN.md`.

## UI + Visual (Stage 08) - DONE (76 painted screens, every family)

**The color layer lives in `ui-visual/` as COLOR COPIES of the grey wireframes.** Hard rule (like the wireframes voice-safe rule): **never paint `wireframes/`** - they stay grey; `ui-visual/` owns ONLY the visual layer (color, type, radius, photos, texture), structure/text/state-set stay owned by `wireframes/`.

- **NAVIGATION RESTORED (2026-07-26), a Stage-08 defect:** the color pass had flattened **every** product `.html` link to `#` (`neutralize()` in `_apply_theme.py` / `_apply_family.py`, plus hard-coded `#` in the `_gen_category.py` card templates), so all 76 painted screens looked finished and went nowhere while the grey wireframes stayed clickable end to end. **9633 links restored** by `ui-visual/_relink.py` (idempotent, six passes: aligned against the grey twin, by key in the twin, shared chrome donated between painted screens, cards by their own kind, by key across the painted tree, then a 3-entry table for the blocks that exist only in color). Only `href` values changed - the 76 files are byte-identical otherwise, so nothing moved a pixel. 17372 internal links, 0 broken; the 1604 anchors still dead are dead in the wireframes too (footer placeholders marked "to be built"). The three generators no longer flatten a link whose destination has been painted, and **gate 10** in `ui-kit/_check_kit.py` runs `_relink.py --dry-run` so a re-broken link fails the build.
- **SUPERSEDED IN STAGE 09, STEP 5 (2026-07-26):** a screen no longer carries any styles of its own. The inline `<style>` (25 to 42 KB of grey-box skeleton, 7 distinct copies across the 76 pages) and the `_theme.css` link were both removed; every screen now links exactly **`../components/index.css`** and nothing else. `ui-visual/_theme.css` + `_theme-vault.css` are still on disk but nothing loads them; they are deletion candidates for step 7. The migration is `ui-visual/_use_system.py` (idempotent). Gate 9 in `ui-kit/_check_kit.py` enforces the one-source rule from here on. The paragraph below describes how it worked BEFORE that step and is kept for provenance.
- **`ui-visual/_theme.css`** (historical) - the Vault color layer; it `@import`s **`ui-visual/_theme-vault.css`** (base Vault tokens + component skin) and was linked AFTER each page's inline `<style>` so it overrode by source order (owns color/type/surface only). Vault tokens in `:root` (graphite/brass, `--groove-*` engraved edges, `--stone-dark` grain). Hides the grey-box scaffolding + the wireframe screen-tree.
- **`ui-visual/event-feed.html`** - the reference screen: 12 event cards, JS-injected **odds bar** (renders treatment B from the `.prob` text, thin 5px), multi-outcome option rows (D), **tinted-not-fill YES/NO buttons** (the odds bar carries the outcome color, buttons stay quiet - "spectator, not trader"), a redesigned **How-it-works `<dialog>`** (brass-tinted hero + icon chips), a **trust bar** (USDC 1:1 + resolved count) + a footer **trust-cards strip** (gold column/source/globe art), the **graphite chip control family** (cat-nav chips with icons + a condensed sticky strip, filters, Load-more - one `#1b1e23` chip, 12px, brass on active), and the roadmap-sidebar course chrome.
- **8 state pages** (`event-feed-empty/-error/-loading/-push-permission-missing`, `-logged-out` + logged-out empty/error/loading) generated by **`ui-visual/_apply_theme.py`** with a **"shell + swap"** strategy: start from the finished `event-feed.html` shell, swap in only the regions that differ (always `<main>`; for logged-out also `<header>` + `<nav.bottom-nav>`), then run two voice-safe transforms on the grafted fragment (a product link is kept when its destination is painted, Favorites heart -> bookmark) + a `distill()` pass. As of 2026-07-18 it also **injects the themed category bar** and wraps the head + state content in the shared `.cat-layout` stone plate, so a state reads as "the feed minus the cards" (the `.state-block` goes borderless on the plate). Idempotent; **never edits `wireframes/`, never regenerates the base**.
- **Critiqued with `/impeccable critique` (dual-agent), snapshots in `.impeccable/critique/`. Score 33 -> 34 / 40** (Signal-era pass; the P1/P2 hardening carried into Vault). P1/P2 hardened: NO-button contrast 3.41 -> 5.48:1, footer 3.37 -> 6.04:1, 44px touch targets (bet/bookmark/bell + cat-nav/filters), `:focus-visible` rings, tinted YES/NO (spectator not trader), trust bar near the action, distilled controls (dropped the duplicate Category dropdown, "Volatile" jargon, reverse toggle). Presentation-clean: `.uv-bar` + `.tbd`/placeholder chips hidden, footer shows a real "Predict Market" wordmark. P3 deferred (live odds-delta animation, error-vs-empty differentiation).
- **Category pages (2026-07-16):** the top category nav is page-level - `event-feed-{politics,crypto,culture,general}.html` (generated by `_gen_category.py`; each drops the trending hero + sub-filter and shows only that category's events, ~6). Trending stays `event-feed.html`. Nav wired on both levels; the old client-side category-switch handler was removed so tabs navigate. **Order:** run `_gen_category.py` then `_resync_sidebar.py`.
- **Sidebar (`_resync_sidebar.py`)** - single source of the ui-visual left screen-tree; gained a **Categories** group under Event Feed (Politics/Crypto/Culture/General), active-marked per page.
- **Concept + DESIGN.md synced to Vault (2026-07-18):** `concept/concept.html` matches the shipped card (thin odds bar, tinted YES/NO) + a new **Controls** panel showing the chip family; `DESIGN.md` fully rewritten Signal -> Vault.
- **Remaining:** apply the Vault language to the other screen families (Event Detail, Bet, Win/Loss, Profile, etc.).

---

## Tokens + Components (Stage 09) - DONE

The styling layer became a system. `components/` holds `tokens.css` plus one css file per component,
all reached through `components/index.css`; `ui-kit/` is the vitrine that shows it and the gates that
keep it honest (`python3 ui-kit/_check_kit.py`, sixteen checks, exits non-zero on the first failure).
Contract and reasoning: `ui-kit/docs/architecture.md`. The reading it grew from: `ui-kit/docs/tokens-audit.md`.

- **Step 5 (done):** every painted screen dropped its inline `<style>` and its `_theme.css` link and
  links exactly `../components/index.css`. Proof tooling lives in `ui-kit/_verify/` (snapshot every
  screen at five widths, diff by element and property, group by cause). `ui-visual/_theme.css` and
  `_theme-vault.css` were deleted in step 7.
- **Step 6 (done, 2026-07-27): the primitives became scales.** The token file had been READ out of the
  product, which is right for a colour role and wrong for a scale: every literal anyone had typed
  became a token, 348 of them. Space had 25 steps with 1 2 3 4 5 6 7 8 9 10 in a row, text had five
  half pixels left from rem arithmetic, radius had two names for one pill, and the graphite ramp had 46
  pairs no eye can separate. Now **265 tokens**: space 25 -> 11 on a 4px grid (plus `--hairline`, since
  1px is a line and not a distance), radius 12 -> 5, control and icon value named with no odd sizes,
  text 21 -> 10 with the half pixels rounded UP, display 5 declared and unused -> 7 wired (nine literal
  `clamp()` gone), leading 8 -> 6, graphite 24 -> 15, alphas 54 -> 28. The whole map is data in
  **`ui-kit/_rescale.py`** (idempotent, `--dry-run`), which is both the migration and its own test.
  Rules now written down in `architecture.md`: round to the nearest step and break a tie toward the
  heavier neighbour; a number is a step only up to 64px; a colour merges only under deltaE 1.5 AND when
  the two never meet on screen. Two new gates stop the harvest growing back: **11** no orphan token,
  **12** no raw scale value.
- **Deliberate, measured pixel movement.** This is the one pass that moves the product on purpose. Every
  change was checked against the map with `_verify/`: 1274 distinct property changes, all of them
  layout or type or a colour under deltaE 1.5, except `#e88a84` -> `#e79087` (two quiet reds for one
  job, the pair the file had already marked). No touch target fell below 44px (the deposit amount field
  now says `min-height:var(--control-44)` instead of reaching 45px by accident).
- **Step 6b (done, 2026-07-27): the theme, as the proof of the semantic layer.** The product is dark,
  so its theme is a LIGHT one and the attribute says what it is: `[data-theme="light"]`, section 3 of
  `components/tokens.css`. It exists as a proof, not as a feature (`ui-visual/_theme_switch.py
  --strip` removes the harness in one command); whether daylight ships is a separate decision. A
  rebrand would prove nothing, because swapping primitives works on a flat file with no roles at all.
  A theme is the test that needs the second level: the ground inverts, the ink inverts, light and
  shade swap places, and the action still has to read as the action.
  **Roles only, 89 of them; not one primitive redefined.** Daylight's values are their own primitives
  at the end of section 1 (chalk ramp, warm ink ramp + alphas, one dark brass, darker green/red, five
  chalk veil alphas, the Vault's own grain, a second logo mark). 265 -> 320 tokens, growth that buys a
  second theme rather than harvest. The semantic selector is now `:root,[data-theme="dark"]`, so any
  element can be marked and its subtree renders in that theme: `tokens.html` shows every role in both
  grounds at once, live, and its contrast table has a column per theme.
  **What the theme found, twelve holes, all fixed:** the stone grain read straight from a primitive
  (11 declarations in 10 files -> `--surface-grain`); the brass logo mark, same category
  (`--mark-logo`); the drawer backdrop reading the emboss shade instead of the scrim; the close disc
  on a photographic head reading the ink of a drop shadow (-> `--scrim-photo`); a SELECTED state
  painted with the focus-ring role (`tabs.css` x2, `options.css`); **five hex literals drawing the
  multi-outcome chart from inside the page script on 13 screens** (a whole categorical palette the
  token file could not see -> `--series-1..5`, handed to the SVG as `var()` so it follows the theme
  live); a wireframe-era grey in a style attribute; **nine `mask-image` stops reading `--shadow-ink`
  for "opaque"** (a mask keeps only the ALPHA, so every masked photograph faded to a third in daylight
  -> `--mask-solid` / `--mask-mid`, never themed); and `--bg-brand-mark`, a role named for the plate
  under the X and Apple marks that is really the colour of the marks (1.06:1 on a pale button, now
  `--ink-900`); **a hover fill and a chart grid line both painted with the LIT LIP of an emboss**
  (`--bevel-faint` did three jobs; on chalk a hover cannot reach for more light and a white grid line
  on a white chart is not there -> `--tint-hover`, `--line-grid`); and **a filled glyph taking a text
  role** (the bookmark: the reflection kept its contrast, 6.7:1 -> 7.2:1, and doubled its weight,
  because light on dark spreads and ink on paper sits solid -> `--icon-quiet` 4.3:1, `--icon-brass`
  3.2:1; the text-safe brass also reads brown at 16px, so the saved state stopped meaning gold).
  Also found: `_rescale.py`'s duplicate-role sweep was file-wide and ate 8 theme
  overrides, now per block.
  **The sharpest lesson:** a veil is not a dark colour over a picture, it is the layer that
  guarantees the words, so it follows the INK, not the photograph. `--scrim-photo` and
  `--veil-photo-*` look like one idea and are two.
  **Five corrections the first cut needed** (all user-caught by eye, then measured): the stone was
  yellow (chalk warmed with depth, +8 to +36; the graphite is faintly COOL at -4..-8 and all the
  warmth is in the ink, bone +19 - now a constant +8 at unchanged luminance); the blocks went flat
  (the shade ladder was scaled as a unit, right for a 1px inset edge and wrong for a blurred drop -
  now split, edge .10/.16, drop .32/.44); the grain vanished (dropped to a third on a backwards
  reading of `overlay`, which above mid grey behaves like screen and bites LESS - now the Vault's own
  0.9/0.8); and **the ramp was translated, not reflected**, the deepest of the four. The first cut
  inverted the ORDER and not the DIRECTION: the page sat mid-ramp at L* 85.6 and every surface still
  came forward by getting LIGHTER, so daylight was a generic grey theme for a structural reason, and
  it ran a third too loud (graphite fills span 11.7 L*, that chalk ramp 15.5; a category chip stood
  9.5 L* off its bar where the Vault puts it at 4.0). Daylight is now the graphite ramp **reflected
  about its own ground**, computed not picked: `chalk L* = page L* - (graphite step L* - graphite
  page L*)`. The page becomes the lightest thing on screen, every surface settles onto it, every
  separation keeps the Vault's size with the sign flipped; 12 steps, each within 0.2 L* of target,
  and a chalk step carries the number of the graphite step it answers to (`--chalk-850` answers
  `--graphite-850`), so the theme block is checkable line by line against section 2. The reflection
  is TOTAL, gradients included: a graded face then reads as lit from below, which is the right trade,
  because reflecting the fills but not the gradients loses the ground under anything sitting on a
  gradient's light end (that is where the chip problem came back). Fifth: **the reflection went one
  role too far.** Lightness on graphite carries depth AND presence, and only depth can invert:
  reflecting a control puts the most present thing in the system 11 L* under the page, which reads as
  dirt, and it is the exact grey the grey-box wireframes used. So six roles (surface, slab-from,
  control, control-hover, chip, chip-pressed, dialog-head) leave the reflection and sit at the top of
  the ramp in the Vault's own order and direction, and the EDGE carries what the fill gave up
  (daylight's hairline is 2.2:1 against its surface, the Vault's 1.1:1). The chalk ramp is now 8
  steps + 1 hairline, as long as the stone is. **Area is the tell:** a chip 6.5 L* under white is a
  quiet pill, a header band the same 7 L* under white is a dirty field - depth is read against how
  much of the screen it covers, which no token file can see.
  **Switch:** above the tree in both panels, single-source markup + boot in
  `ui-visual/_theme_switch.py` (imported by `_resync_sidebar.py` and `_gen_component_pages.py`);
  inline in `<head>` so daylight never flashes graphite; `localStorage` key `pm-theme`. Gate 1 masks
  it as chrome, like the sidebar. **Gate 13** is new: colour goes through a role (a component reading
  a colour or material primitive fails the build) + every screen can switch.
  **A frame is a document.** The first cut of the theme lied in the vitrine: every stand page went
  pale while every `<iframe>` inside it stayed graphite, because a specimen is its own page and
  `data-theme` does not cross into it. Fixed both ways - the boot block is now in every specimen and
  in `selftest.html` (so a frame is right at its own first paint), and the parent tells every frame
  by `postMessage` on toggle and on `load` (so an open frame follows the switch). postMessage, not
  `contentDocument`, for the reason `_frames.js` already had: from `file://` every document has an
  opaque origin. Gate 13 gained "every frame follows"; gate 5 had to start its search at `<body>`,
  since a head script now exists and its slice was coming out empty.
  **Verified:** 77 screens x 2 themes x {380, 1280} - 0 below AA, 0 overflow, 0 console errors;
  selftest "all pass" in both themes. Pre-existing defect found, NOT theme-related, logged for step
  7: the win overlay h2 renders 52px left of its content box and `overflow:hidden` clips it to "u
  were right" in both themes.
- **Step 7 (done, 2026-07-27): the deletion pass, the defect table, the finish.** Audited
  `components/` + `ui-kit/` + all 77 painted screens against the step-7 checklist and `/impeccable
  audit` (16/20 Good). **34 findings, all closed.** The ones that changed a rule and not just a line:
  - **`overflow:hidden` makes a box scrollable, it only hides the bar.** Thirteen stones clip a
    decorative pseudo; one was actually scrolled (`.sheet-head`, `scrollLeft:52`), which dragged the
    win overlay heading out of its box and clipped it to "u were right" in both themes on 4 screens.
    All thirteen are `overflow:clip` now, which creates no scroll container. Sweep: 0 scrolled.
  - **Target size follows the POINTER, not the viewport.** 44px was bound to `max-width:640px`, so a
    touch laptop got 36px. Now `@media(pointer:coarse)`; a fine pointer keeps 36, which clears
    2.5.8 (24x24). The card bookmark was 16x16 (fails both bars) and now carries a 44px box with a
    negative margin, so the target grew and not one pixel moved.
  - **Reduced motion, once, in `base.css`** (3 of 23 components had a block; a promise is not made
    component by component).
  - **A candidate is not an outcome:** the multi-outcome series drew line 1 in the YES green and
    line 3 in the lit brand brass. Green, red and gold are reserved; the series moved into the arc
    they leave free (cyan 187 -> magenta 328 + one neutral), all five >= 4.5:1 in both themes.
  - **Two roles may share a value** (27 groups do): a role is a reason, not a value. The rule is
    written above section 2 and the coincidences are declared where they happen.
  - **A third copy is a fork:** `shell.html` held its own hand-kept header next to `header.html` and
    76 screens; it composes the specimens now and holds no markup.
  - Also: `.opt-row.sel` side-stripe -> tint (an impeccable absolute ban), 13px/19px icons onto the
    scale (`--icon-12` added), `--brass-800` orphan deleted with its gate exception, `.uv-bar` +
    its wireframe-era grey gone from 76 screens, the Favorites category bar restored from the grey
    twin (and its now-duplicate Category dropdown dropped), `<img>` given `width`/`height`/`lazy`.
  - **Deleted:** `ui-visual/_theme.css` + `_theme-vault.css` (132 KB, unloaded since step 5) and the
    empty `tokens-components/`.
  - **Living documents:** `inventory.md` gained **CSS file** and **Page** columns, filled for all 87
    component rows by `ui-kit/_fill_inventory.py` (class-matched against each file's `Classes:`
    header, so it stays true when a class moves); `coverage.md` records the decision on the six
    kit-only classes (all six stay, with the reason); `architecture.md` gained "What step 7 settled";
    `DESIGN.md` gained the two-level token section + the both-theme contrast table; `STRUCTURE.md`,
    `README.md` and the roadmap sidebar mark 08 and 09 Done.

### Step 7b (done, 2026-07-27): the second audit, and what a passing build hides

Run against `components/` and every painted screen on the premise that a system passing its own
gates is where the interesting defects live. **14 findings, all closed.** Contrast was already clean
in both themes and stayed clean; what the gates could not see was where the styling lived.

- **One element, one rule.** Step 1 read the styling off the painted product, and the product had
  TWO stylesheets on it: the grey-box skeleton written inline by the wireframe generator, and the
  Vault theme loaded after it. The extraction concatenated them, so **116 selectors were written
  twice and 200 declarations in the first layer rendered nowhere** (`loadmore.css` described one
  button twice over, nine properties apart). Deleted by `ui-kit/_unfork.py`, whose argument is that
  `.app-case S` is S plus one class and therefore always wins. **Five exceptions, measured not
  assumed:** the footer language menu and the shared `<dialog>`s live OUTSIDE `.app-case` (a dialog
  is appended at the end of the body, so it is a sibling), and for those the unprefixed rule is the
  shipped one. The first cut deduced instead of measuring, deleted the footer menu's padding, and
  the diff caught it in one run.
- **An attribute is a rule.** Gate 9 asked about `<style>` blocks, gate 12 looked inside
  `components/`, so **110 style attributes on 30 screens** were the one place neither looked: type,
  geometry (`width:72px` beside an existing `--size-72`), layout variants, and twelve places where a
  component was undone on the element. Half were already dead. Two explain an `!important`:
  `profile.css` and `state-block.css` were shouting to beat an inline style, and both stopped.
  **An `!important` is usually a fossil of something no longer there.** Gate 9 reads attributes now
  (`ui-visual/_destyle.py`).
- **Hidden is not gone.** Every painted screen carried the wireframe's screen-tree drawer, about
  150 links hidden by one `display:none`: **1024 KB, 16 per cent of all HTML in `ui-visual/`**, a
  second and invisible navigation on a page that has its own. `base.css` was carrying 25 rules to
  style a drawer it also hid, plus `.device` four times and `body` three, each undoing the last;
  117 lines to 66. Removed by `ui-visual/_strip_wireframe.py`; the record stays in `wireframes/`,
  which owns structure.
- **A stacking order is a list, so it is written as one.** 0 1 2 3 4 5 6 10 40 49 50 60 199 200 201
  across twelve files became **eleven named layers** in `tokens.css` (`--z-under` to
  `--z-chrome-top`). Three of the old numbers did one job; **199 next to 201 is the shape of a value
  picked to win an argument rather than to sit in an order.**
- **Every screen has exactly one `<h1>`.** 74 of 77 had none, while `ia/docs/pages/seo.md` has
  specified one per indexed page since stage 03b. Only the tag moved, grey tree first
  (`wireframes/_generators/page_heading.py`); the 19 overlay-only screens keep none, because
  inventing a heading is inventing copy. Three section headings went h3 to h2 to close the skip the
  promotion opened. **Heading skips across the painted tree: 0.**
- **A system stylesheet names the font it needs; the document loads it.** `base.css` `@import`ed the
  Google Fonts URL every page already `<link>`ed: one dependency declared twice, and the CSS copy
  three hops from discovery. It is also the wrong place for the decision, since the call sends a
  visitor's IP to a third party before consent in a product that ships a GDPR cookie banner.
  **Self-hosting the three families is the production answer and is now an open decision, not a
  silent default.**
- Also: the bet amount field took `outline:none` and gave back a 1.5px underline colour change, the
  only control in the product without a focus indicator and the field a person types a bet size
  into; `<meta charset>` sat at byte 2064 on all 77 screens because the theme boot was inserted
  ahead of it; 21 selectors nothing on any page could match; the four how-it-works section headings
  had no rule at all (18.72px is what a browser gives an unstyled h3); 15 half-pixel type sizes in
  the vitrine's own chrome; a comment naming `_theme.css`, deleted in step 7, on 76 screens.
- **Two things this pass got wrong and had to come back for**, both the same shape. `.sidebar-divider`
  is written at run time by `ui-kit/_nav.js` out of a template string, so a scan that read only
  `class="..."` in HTML called it dead; deleting it left every group heading in the vitrine's side
  panel as unstyled text. **A class inside a template string is markup**, and gate 14 reads the
  scripts now. The reason nobody noticed is worse than the bug: `_verify/snap.cjs` walked
  `ui-visual/` and nothing else, so a pass editing `components/` could prove the product and say
  nothing about the vitrine the same file paints. It takes `--kit` now, and re-running it against a
  worktree of the pre-pass tree found two more: `kit.html` has `<body class="app-case">` and
  `.app-case` is transparent by design, so the body stopped painting the page; and one label took an
  inline margin the removed `!important` had been out-shouting. **Removing an `!important` is only
  safe once you have found what it was arguing with.**
- **Three new gates**, so none of it grows back: **9** now fails on a style attribute, **12** owns
  the stacking order, **14** fails on a selector no markup can match (the other half of gate 11).
- **How it was verified, and a tool that had to exist.** `_verify/diff.cjs` walks two snapshots in
  step, which is right while the DOM is fixed and useless the moment a pass removes markup: every
  index after the removal points at a different element. **`_verify/visible.cjs`** keeps only what
  the browser reports as visible and compares those sequences, so a `display:none` deletion proves
  itself and a real side effect (a moved sibling, a renumbered `:nth-child`) still shows. Across the
  whole pass, at 76 screens x 5 widths, what moved: four dock buttons and one CTA bar lost 2px of
  padding (14px and 10px were never on the 4px grid, and an attribute never went through step 6),
  six section labels took the system's `.1em` tracking, and four headings went 18.72px to 18px.
  Everything else identical to measure; 0 text pairs below AA in either theme.

### Step 7c (done, 2026-07-28): the third audit, on a build where every gate was green

Run against `components/`, `ui-kit/` and all 77 painted screens, plus `/impeccable audit` (16/20
Good, no AI tells). **24 findings, 23 closed, 1 recorded as a decision.** Full record with the
reasoning in `ui-kit/docs/architecture.md`, "What step 7c settled". What changed a rule:

- **A generator that is not idempotent on all of its row kinds is not idempotent.**
  `_fill_inventory.py` stripped its own columns from data rows and not from headers, so the header
  grew two cells a run: seven runs later every table in `inventory.md` had a 21-cell header over
  9-cell rows and none of them rendered.
- **A class a file mentions is not a class it owns.** `coverage.md` said 76 screens for 34 of 36
  components, because `market.css` styles `.market-title .ic` and `.ic` is on every screen. Ownership
  is now the file that styles a class with the fewest ancestors (ties to cascade order) plus a
  five-word hand-checked SHARED list. The same map writes the `Classes:` and `Stands on:` lines in
  each css header, which were prose someone typed once and had been telling the truth while
  coverage.md said 76. **Two artifacts of one system disagreeing is the defect; one computation
  feeding both is the fix.**
- **A distance is not a measurement.** The rule was written in step 6 and 57 declarations broke it,
  because the measurement scale shipped with two steps (56, 72) and the product needs twelve. A rule
  with no scale behind it cannot be followed. `--size-2 .. --size-72` now, and **gate 12 fails on a
  `--space-*` step in a width, height or flex basis**, which the raw-value check cannot see.
- **Removing an `!important` means ending the argument, not deleting the word.** `.grid` carried one,
  and dropping it let `.cat-main .grid` win: the category pages would have changed their column
  track. Four rules above it were already dead (three breakpoints losing on source order, the
  category variant losing to the shout). Deleting the four made the shout removable without moving a
  card.
- **A rule applied to two files is not applied.** Step 7 moved touch targets to `pointer:coarse` and
  reached `catnav` and `header`; six components still bound 44px to `max-width:640px`, so a touch
  tablet above 640px got the 36px control, the exact device the rule was written for. Measured after:
  coarse pointer at 380 and at 1280, every control 44px; fine pointer 36, which clears 2.5.8.
- **Structure is owned by `wireframes/`, so fixing only the paint leaves the owner wrong.** Step 7b
  reported "heading skips across the painted tree: 0" and the grey tree, which owns structure, still
  had an h1-to-h3 jump on 46 pages and no `<h1>` on 19. **Gate 15 reads both trees.** Footer columns
  went h3 to h2 in both; the Event Detail column heads went h4 to h3, which made them match the
  `.ed-section` label rule, so that rule became a CHILD selector (**a section label is the section's
  own heading, not any heading inside it**); the 17 dialog-host screens took the `<h1>` from the
  heading their own dialog already carries, so no copy was invented. The two Event Detail loading
  skeletons keep none on purpose and gate 15 names them.
- **A UI string is not a style hook.** `[aria-label="Track record"]` carried seven rules, so the
  profile reputation grid hung off an English phrase owned by `voice/`. Now `.pos-record`.
  `[aria-current="page"]` stays: a state attribute is a state.
- **A promise made component by component is not made.** 14 files carried the identical
  `:focus-visible` rule, 24 did not, and there was no default. One rule in `base.css`, one new role
  (`--focus-ring`, split from `--text-brass`), three exceptions that say why.
- **Where the system layer may reach.** `components/` held 24 `url(../ui-visual/assets/...)`: the
  system depended on the product's screen folder. Assets are `assets/` at the root now. Sixteen of
  those were worse than a path: `.grid > .card:nth-of-type(1..12) .thumb` encoded WHICH feed card
  shows which photograph, and the event photograph belongs on the element by this file's own rule.
- Also: three stale comments in `tokens.css` (a note that outlived the defect it described, a pointer
  at a primitive merged away in step 6, a role promising a difference it never had, deleted); 12 of
  the 27 same-value role groups now say so; motion moved onto the declared duration scale (21 raw
  timings, none of which was a step); the vitrine's `_page.css` dropped 93 frozen Vault hex values;
  **`icons.html` gained the 29 icons the product DRAWS inline** beside the 15 it references from the
  sprite, because a vitrine that documents one of two mechanisms describes the smaller one; every
  stand page gained a `<main>` landmark; and gate 9's "nothing loads the flat kit" was repointed,
  since `kit.css` had already been deleted when it was written and it could not fail.
- **Gate 16 exists because this pass shipped a broken declaration.** A note appended to a token
  without its comment markers put bare prose inside `:root`; the browser dropped every declaration
  after it and the NO side of the outcome palette went transparent on 28 screens. Fifteen gates saw
  nothing; a 380-page snapshot did. Gate 16 walks every block in `components/` and fails on anything
  inside it that is not a declaration.
- **Recorded as a decision, not fixed:** 20 declarations build a colour with `color-mix(in oklab,
  var(--color-action) N%, ...)` at 16 different percentages, an undeclared second alpha ladder beside
  the declared `--brass-a*` one. Gate 13 is satisfied (all of them read a role). Which steps that
  ladder should have is a states question, and rounding them now would move hover and selected states
  for the legibility of the file rather than of the product.
- **Verified:** both trees, 5 widths, before and after, compared by what the browser reports as
  visible. 380 product snapshots, **0 with a different visible element count**; what moved was the
  asset URLs (same files) and two chart polylines caught mid-transition. 175 vitrine pages changed
  element count, all of them the corrected screen lists and the new icon section. Target size
  measured, not reasoned about: coarse pointer 44px at 380 and at 1280, fine pointer 36px. Then the
  whole product in both themes at 380 and 1280: **54774 text pairs, 0 below AA, 0 page errors, 0
  horizontal overflow.** Two earlier runs of that sweep were wrong (950 failures that were gradient
  buttons the checker could not read, then 405 that were a theme swap measured mid-transition):
  **a measurement not checked against a known-good case is a claim, not a proof.** **Gates: 16.**

### The rule for a change, from here on

Replaces the Stage-07 wording that pointed at `ui-kit/kit.css` and `ui-kit/kit.html`; neither has
that role any more.

- **A value** goes to the token of its own level and reaches every screen by itself: a colour is a
  **semantic role** in section 2 of `components/tokens.css`, a raw value is a **primitive** in
  section 1. A component may never read a colour primitive (gate 13) and may never write a raw scale
  value (gate 12).
- **Markup** goes to two places and only two: the component's page in `ui-kit/`, and the screens in
  `ui-visual/` where it stands. Never to a third copy.
- **Never on the element.** A `style=` attribute is a rule in the one place the system cannot see, so
  it fails gate 9. Three things are not styling and may stay: a datum (a bar drawn to a width), the
  event photograph, and a value the page script writes at run time.
- **A heading level is structure**, so it is decided in `wireframes/` and the colour copy follows.
  Exactly one `<h1>` per screen, no skipped level, **in both trees** (gate 15 reads both, because a
  check that reads only the copy can pass while the original is wrong).
- **Geometry has three scales and they are not interchangeable.** `--space-*` is the distance BETWEEN
  things, `--size-*` the side OF a thing, `--control-*` and `--icon-*` the box and the mark of an
  interactive element. Same numbers, different questions (gate 12).
- **A sample photograph is content**, so it goes on the element as `style="background-image:..."`,
  which is one of the three things gate 9 lets through. A shared image asset lives in `assets/` at the
  root, owned by neither layer.
- **A new component** = css in `components/` + a page in `ui-kit/` + an entry in `ui-kit/_nav.js` +
  a row in `ui-kit/docs/inventory.md` (with its CSS file and Page columns). Then
  `python3 ui-kit/_check_kit.py` has to pass, all sixteen.
- **`ui-kit/kit.html` is frozen.** It is the flat kit the system was read out of and it is kept as
  provenance; a component is never added to it. **`ui-kit/shell.html` composes** the header and
  bottom-nav specimens and holds no markup of its own.
- **Two token levels, not three.** Primitive + semantic. Colour is the only thing with a second
  level, because a radius or a gap has nothing for a theme to override; a component level is not
  part of this stage.
- **Never paint `wireframes/`.** Structure and copy are owned there and stay grey; `ui-visual/` owns
  the visual layer only.
