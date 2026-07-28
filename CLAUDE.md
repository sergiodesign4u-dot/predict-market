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
keep it honest (`python3 ui-kit/_check_kit.py`, twenty checks, exits non-zero on the first failure).
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

### Step 7d (done, 2026-07-28): the readiness pass, and the rule that had no gate

Run against the course's own "done when" list rather than as a defect hunt, which is why it found a
different kind of defect. **Eleven findings, nine closed, two of them my own measurement error.**
Full record in `ui-kit/docs/architecture.md`, "What step 7d settled".

- **A rule with no gate behind it is a preference.** `wireframes/` owns structure and copy has been
  written here since Stage 08 and nothing checked it, so Stage 08 **redesigned the Event Detail while
  painting it** and the redesign never came back: an AMM market panel with a price-by-size table, a
  chart rebuilt as head / plot / axis / range, a rules-and-context tab split, a share-and-save
  cluster, an odds bar, and a real `<input>` where the grey tree had a `<span>` pretending to be a
  field. 55 of 72 twinned `<main>` elements differed, Event Detail by 222 elements. Ported back by
  `wireframes/_generators/port_structure.py` (idempotent, reads the painted twin, never writes to
  `ui-visual/`), which derives the grey-box rules from `components/` by keeping what a rule PLACES
  and dropping every colour: **a grey box is the painted component with its finish scraped off.**
  **Gate 18** fails the build when the two trees disagree; the four differences that ARE the
  boundary are declared in `wireframes/_conventions.md` (plate wrappers, icon mechanism, photograph,
  and chart data, because a wireframe draws its data and a product computes it).
- **The copy inventory was not the source of truth for a whole stage.** 43 strings the product had
  been shipping since Stage 08 had no row in `voice/docs/microcopy.md`, including every label of the
  market panel and the line that keeps the context tab from being read as the resolution rule. Logged
  as Step 24. Two lines were opened as defects and closed as correct, and the first is the useful
  one: `Closes: Sep 1, 2027` looks like the product's only stray colon and the colon is a
  **delimiter** the feed script splits the meta row on. **A style rule that would break a script is a
  style rule with a missing fact in it.**
- **Four bugs in my own generator, each one a rule.** Splitting a selector list on commas cuts
  `:is(h2,h3)` in half, and a browser drops an unparseable rule AND everything after it in the sheet
  (the symptom was a chart axis rendering as running text). Deleting `@media` before reading a file
  deletes the layout, so the feed came out 14px wider than the phone it was drawn for. "Already
  styled" is the wrong question when the markup moved. A selector naming a scope the target tree does
  not have can never match.
- **A photograph travels two ways.** `background-image` was stripped and `<img>` was not, so four
  pictures entered a tree with zero image elements across 104 pages, one of them 1400px wide.
- **Two findings were my own measurement error**, recorded because a false positive costs the same
  attention as a real one: a case-sensitive scan called six documented token coincidences
  undocumented. **A checker that has not been run against a case it should pass is not a checker.**
- **Gate 17**, the other direction of gate 3: 14 marks stood on screens and were on no sheet,
  including the chevron at 176 uses and the three sign-in brand marks, because step 7c collected
  icons with a regex wanting `class="ic"` as the first attribute. An `<svg>` on a screen is either a
  MARK or a drawing of DATA; there are two drawings. One checkmark drawn two ways is now drawn one.
- Also: the eleven `--z-*` tokens are now a section of `tokens.html`, drawn as a stack written
  **highest first** so only the tokens can produce the right picture; the field gained a rendered
  state set (`input-states`), and its first cut on the bare canvas rendered four white boxes because
  every rule in `input.css` is scoped under `dialog.app-dialog`; the roadmap sidebar was true in
  `LAYOUT` and false on 21 pages that keep their own copy, fixed by `_resync_roadmap.py`; and
  `.chart-wrap` / `.chart-cap` died the moment the port took the last markup they could match, which
  is a fossil pair working as intended.
- **Verified:** 104 grey pages at 380 and 1280, **0 horizontal overflow, 0 page errors, 0 colour
  outside the wireframe palette**, against the same sweep run on a worktree of the previous commit.
  Structural parity 55 of 55. Gate 18 was tested by injecting drift and confirming it fails.
  **Gates: 18.** (The colour claim was read out of the SOURCE and step 7e re-read it out of the
  BROWSER, where it was false; see below.)

### Step 7e (done, 2026-07-28): the other three regions, and a gate that certified one

Step 7d put a gate behind "wireframes/ owns structure", and that gate compared `<main>`. **A gate
that reads one region of a page certifies one region of a page**: the header, the bottom nav and the
footer stayed the one place two trees could drift with every gate green, and they had. Ten findings,
all closed, two of them the tools' own. Full record in `ui-kit/docs/architecture.md`, "What step 7e
settled".

- **The drift ran both ways, so the fix is two tools in a fixed order.** The paint got the SHAPE
  right and the STATE wrong; the grey tree got the state right and the shape wrong. Reading that as
  "one tree is behind" is what makes a one-directional port write the wrong answer into 104 files.
  **The paint owns the shape of the chrome; the grey tree owns which state it is in.**
  `ui-visual/_reconcile_chrome.py` gives the paint back three state facts, then
  `wireframes/_generators/port_chrome.py` copies the corrected shape back.
  The paint had `aria-current="page"` on the **Events** slot of all 76 painted screens whatever
  screen it was (the grey tree marks 54 Events / 9 My Bets / 3 Favorites / 6 Portfolio / 15 none, and
  the painted Wallet screen was announcing "Events, current page"); a logged-in header over a bottom
  nav pointing home at `event-feed-logged-out.html` on ten screens, one chrome disagreeing with
  itself about whether anybody is signed in; and three unread notifications in the dropdown of the
  three screens whose whole subject is that a new user has nothing yet. The grey tree had no
  `.cat-condensed` at all (the category strip that slides into the sticky header, a whole navigation
  control, on 68 painted screens and 0 grey), the footer trust block as three bare sentences, and a
  `<span>` pretending to be the deposit amount field.
- **An auth variant was not a fact to read, it was a decision to make.** Ten screens disagreed and
  neither tree is a copy of the other, so each is answered by a reason, written once: `how-it-works`
  + `public-profile` x4 logged OUT (documented as pre-auth since Stage 08), `cookie-consent` because
  a consent banner IS a first visit, `maintenance` because the app is down and there is no session to
  read; `404`, `500`, `toasts` logged IN, because showing a signed-in person Sign in / Sign up turns
  "this page is missing" into "you were logged out".
- **A port copies markup, and a href IS markup.** The category pages are `event-feed-politics.html`
  in colour and `politics.html` in grey, and step 7d carried the painted hrefs across with the
  markup: **110 links in the grey tree pointed at files that do not exist there**, while the link
  check run at the time counted links instead of resolving targets.
- **A missing colour is a colour**, twice, and both are the step-6b theme lesson from the other side:
  a checker that reads the source cannot see a value the browser supplies. The grey sheet styles a
  link in fourteen scoped places and never as a bare element, so every `<a>` outside them rendered in
  the user agent's `#0000EE`: **992 computed colour values** in a tree whose contract opens with
  "neutral greys only" and whose source has 0 non-neutral hex. And `fill`/`stroke` are not in the
  port's KEEP list, so **the feed hero chart has been a solid black rectangle since step 7d**, since
  an SVG with no fill is black.
- **Where a rule may reach, part two.** Gate 14 counted `wireframes/*.html` as markup for
  `components/`, which cannot apply to it (the grey tree has its own inline css and never links
  `index.css`). Four rules lived on that mistake and are deleted. **A class carried only by the tree a
  stylesheet cannot see is a class it does not have.**
- **Two boundaries added, six now** (`wireframes/_conventions.md`): the `TBD` chip, because a
  wireframe is obliged to mark an unbuilt destination and a product must not show a user the
  bookkeeping; and the page behind an invoked overlay, which convention 5 has specified since the
  wireframes were built. That sixth one is **checked rather than skipped**: grey must carry no chrome
  on those 17 screens and the paint must carry all of it.
- **Two tool bugs, one shape.** An idempotent generator has to be idempotent about whitespace: **the
  removal has to be the exact inverse of the insertion**, and getting it approximately right cost 74
  pages on one re-run and 13 on the next. And a painted overlay page carries four dialogs with the
  shared ones first, so "the first `.sheet-body`" is the sign-in provider list on all 17: the port
  wrote sign-in buttons into the grey Win, Loss and Deposit wireframes, caught by eye in a
  screenshot. A screen's own overlay has an id, and the tool now checks both trees give the sheet the
  same `aria-label` before copying. Also: two generators writing into one `<style>` have to know
  where each other's work ends, or one silently deletes the other (72 pages).
- **Not fixed, on purpose:** the paint made the invoked overlay a centred modal at BOTH breakpoints,
  so "bottom sheet on mobile" ships only in grey. A product decision, recorded beside the convention
  it contradicts.
- **Verified:** grey 208 page loads at 380 and 1280 (**0 overflow, 0 page errors, 992 colour leaks ->
  0**); painted 308 page loads across both themes (**61956 text pairs, 0 below AA, 0 overflow**);
  **16597 grey links, 110 broken -> 0**. Gate 18 tested by injecting drift into each of the five
  compared regions in turn. All five tools reach their fixed point in one run. **Gates: 18.**

### Step 7f (done, 2026-07-28): one dialog, one copy, and scope as a place

Found by looking at the product instead of the build: the sign-in dialog on `ui-visual/sign-in.html`
did not look like the sign-in dialog on every other screen. **A screen can disagree with its grey
twin, and it can also disagree with its own second copy in the same tree, and only the first of those
was ever checked.** Full record in `ui-kit/docs/architecture.md`, "What step 7f settled".

- **A dialog that also has a page has two copies.** Sign In and Deposit each exist as the shared
  `<dialog>` on all 76 painted screens AND as the standalone page that IS that dialog. Stage 08
  painted the shared copy and left the standalone on the grey generator's markup, so **the page a
  person actually opens carried the wireframe placeholders, the one standing in for Google being a
  circle with a plus in it**, while the shared dialog carried the real brand marks. Four copies of
  that body existed in the repo and all four differed.
- **"The newer copy wins" would have deleted the best thing on the screen.** The standalone Deposit
  had three things the shared one had lost: a label over the payment widget, the sentence saying card
  payments are converted via Transak, and **an exit to How It Works, which is the trust affordance
  that screen exists to earn**. Merged element by element, then one markup from there
  (`ui-visual/_unify_dialogs.py`). **Gate 19** fails the build when it drifts again, in either tree,
  and checks the marks by name, because `shape()` drops `<path>` and `<circle>` and so cannot see
  that a button is drawing the wrong logo.
- **Scope is where a block may stand.** The How It Works page rendered as an unstyled document
  because every rule for the hero, the icon chips and the FAQ list began `.app-dialog.hiw-dialog`:
  the page the dialog links to as "the full guide" could not reach one of them. A rule that describes
  a BLOCK is now written unscoped; only what is about being a dialog keeps the ancestor.
- **A page is not a bigger dialog.** The page was composed, not re-marked: page text size instead of
  a sheet's 13px, sections apart instead of stacked, and the brand tile and the resolved-events count
  moved into a side column, because **a claim and its proof belong beside the argument, not after
  it**. It also gained what a page called How It Works owed a reader and did not have: how to place a
  bet. One line of copy written (Step 27 in `microcopy.md`), the rest already shipped.
- Also: the heading `Proven, not promised` had been sitting in a `<section>` **with nothing in it**,
  above three numbers in a different element; `.app-case .hiw-sec > :is(h2,h3)` from step 7c stopped
  matching the moment the heading moved, a fossil created by the fix for a fossil; and `.hiw-sec`
  joined `port_structure.RESTYLE`, because **"already styled" is the wrong question when the markup
  changed shape** and the wireframe was drawing the chip above the heading in a layout that puts it
  beside.
- **Two checkers reported their own defects**, both mine: gate 19's first cut asked for "the first
  `<dialog>` in the document" and got the shared sign-in sheet that every standalone page embeds
  first, so **a page with several of a thing has to be asked by id**; and `_unify_dialogs.py` had to
  be told that a button with no mark keeps none, since swapping a placeholder for the real logo ends
  a fork but putting a logo on a control that never had one starts a design decision.
- **Verified:** both trees at 380 and 1280, grey 0 overflow / 0 errors / 0 colour outside the
  palette, painted 0 below AA in both themes, 0 broken links either side. Gate 19 tested by injecting
  each of its three kinds of drift. **Gates: 19.**

### Step 8 (done, 2026-07-28): the coverage pass, and the family no gate could see

Run against the three things step 7f left open (an overlay contradicting its own convention, a font
host called before consent, a note that the trees disagreed about how many category screens exist),
and the third one turned out to be the largest hole this stage has found. **Fifteen findings, all
closed.** Full record in `ui-kit/docs/architecture.md`, "What step 8 settled".

- **A pair that does not exist is not a pair that agrees.** Gate 18 pairs the trees by FILENAME, and
  one family does not share filenames: a category page is `politics.html` in grey and
  `event-feed-politics.html` in colour. The gate skipped every unpaired page in silence, so **32 grey
  category screens sat against 4 painted ones** and the family drifted through two stages with every
  gate green. Zero drift out of zero pairs reads exactly like zero drift out of all of them. The map
  is now **`_twins.py`** at the root, one copy for six tools and the gate; it had existed in FIVE
  hand-written copies, and the four that only knew the BASE pages are why nobody noticed. Gate 18
  gained **every screen has a twin**, one declared exception (`overview.html`). The 28 missing
  screens are built by `ui-visual/_apply_theme.py`, generalized from the Event Feed's state
  generator: a category page is the same listing with one filter on it, so it is the same machine
  with a different shell, not a second generator.
- **An anchor another tool can remove is not an anchor.** `_apply_theme.py` built the stone plate by
  finding `<div class="feed-inner">` in the grey fragment, and step 7d's port unwraps plate wrappers
  on the way into grey, so the anchor had stopped matching and the next run would have shipped eight
  state pages with no plate. `_gen_category.py` had the same defect one function away and it had
  already fired: its heading substitution read `<h2 id="feedHeading">` and step 7b made that an
  `<h1>`, so one re-run put the shell's **"Trending"** on all four category pages and silenced the
  sub-category rail, which picks its list by the heading's text.
- **A category page owes its own SEO body, not the home page's.** `seo.md` section 3B lists "About
  {category} events" as the category template's fourth H2; the painted pages had inherited the feed's
  two generic sections instead, the same text on all five URLs, which section E of the same spec
  forbids. The copy is read out of the grey twin at generation time, because a generator that types a
  sentence is a second source for it.
- **A listing does not change its contents when nobody is signed in.** The logged-out category state
  was built from a grey card set drawn in Stage 05: no `.top-txt`, so no story-led "why", and YES/NO
  a logged-out person could not press, in a product whose whole inversion is that you browse and
  build a bet before the gate. And **nobody signed in has saved anything**: a pressed bookmark shipped
  on five logged-out screens in both trees, the filled brass mark meaning "this is in your
  Favorites", to a visitor whose header offers them Sign up.
- **A missing colour is a colour, on a control this time.** Every colour in `yesno.css` hung off
  `> a`, so a `.yesno` whose buttons are not wrapped in an anchor fell back to the user agent's
  `buttontext`: near black on graphite, **1.42:1**. **A side is a POSITION IN THE PAIR, not a fact
  about being wrapped in a link.**
- **A frame rule reached a dialog.** `.app-case{position:relative}` in `base.css` took back the user
  agent's `position:fixed` for `dialog:modal` on the 17 standalone overlay pages, which put the app
  frame class on the `<dialog>` itself, so the sheet scrolled off the top with the page behind it.
- **The bottom sheet came back, and it is geometry, not markup.** Under 640px an invoked dialog is
  full width on the bottom edge, top corners rounded, rising into place, head fixed and body
  scrolling; above 640px nothing changed. **`:modal`, not `[open]`**, because a standalone overlay
  page opens its dialog as the page it IS and a sheet that rises over nothing is a page that jumps on
  load, and because **an author declaration beats a UA one whatever the specificity**, so a bare
  `display:flex` would have opened every dialog on 76 screens at once. No grab handle: the grey tree
  draws one and drag-to-dismiss is not built.
- **Where a font comes from is a decision.** The three families are served from this repo now: 18
  woff2 files (latin + latin-ext, `font-display:swap`) in `assets/fonts/`, declared once in
  `components/fonts.css`. **Gate 20 is three checks**, because the defect returns three ways: a page
  re-adding the tag, a GENERATOR re-adding it to every page it writes (five had it in a template),
  and an `@font-face` naming a file nobody committed.
- **Verified:** painted 105 screens x 2 themes x {380, 1280} = **420 page loads, 86534 text pairs, 0
  below AA, 0 overflow, 0 page errors**; grey 104 x 2 widths, **0 overflow, 0 errors, 0 non-neutral
  colour** (its 1212 sub-AA pairs are the screen-tree drawer's own notes and the identical count comes
  off a worktree of the previous commit). **16770 grey + 15535 painted links, 0 broken.** The sweep's
  first cut reported 116 sub-AA pairs and 4690 overflowing elements; calibrating it on three
  known-good pages returned 0 and 438, so the overflow question is asked of the DOCUMENT now and the
  116 turned out to be real. **A measurement not checked against a known-good case is a claim, not a
  proof. Gates: 20.**

### Step 8b (done, 2026-07-28): the documents, the skin, and the sheet that could not scroll

One item was on a list and two came from looking at the product. **Nine findings, all closed.** Full
record in `ui-kit/docs/architecture.md`, "What step 8b settled".

- **A document nobody can open is not documentation.** Every stage renders its reasoning
  (`ia/docs/sitemap.md` -> `ia/sitemap.html`); Stage 09 was the one that did not, and its four
  documents are 144 KB. Worse, the vitrine already LINKED one: **39 component pages pointed at
  `docs/coverage.md`**, a href into a file the browser downloads instead of drawing. They are pages of
  the vitrine now (`ui-kit/_gen_docs.py`), painted by the system they describe, with a contents rail,
  a swatch beside every colour literal and a link on every file name the vitrine has a page for.
  Generated, because these documents change every step and a hand copy is stale by the next one;
  **gate 21** re-renders in memory and compares, because a file can be newer than its source and still
  be wrong, and fails on any link into a raw `.md`. Run `_gen_component_pages.py` first: it writes
  `docs/coverage.md`. The long read also found that **a section label is not a heading** - `.tk-sec>h2`
  is small brass capitals, right over a specimen and wrong seventeen times down a page.
- **A gate that compares the body certifies the body.** Gate 19 has guarded the Sign In / Deposit fork
  since step 7f by comparing the sheet BODY, and the fork left was on the element the body hangs from:
  all 17 standalone overlay pages carried `outcome-dialog`, which is the RESULT skin (`dialog.css`
  splits the head on it and only `:not(.outcome-dialog)` gets the brass-lit plate). **The sign-in sheet
  a person actually opens had the flat result head while the same sheet on the other 75 screens had
  the lit one.** A skin is named for what the sheet IS: sign-in and deposit take the shared dialog's
  own class list, win and loss keep theirs. Computed in `_unify_dialogs.py` from the canonical dialog,
  with the family read from the page NAME, because **a rule that can only recognise its own input
  before it has run once is not idempotent**. Gate 19 compares the skin now.
- **A modal is bounded by the viewport, so it has to be able to scroll.** The user agent gives
  `dialog:modal` both `max-height` and `overflow:auto`; `dialog.app-dialog{overflow:clip}` took the
  second away. At 1280x620 the deposit sheet was cut with its **Add funds** button 116px past the edge
  and nothing to scroll; the how-it-works sheet was unreachable below 900px of viewport at any width.
  This is step 7's finding read backwards: there `overflow:hidden` was wrong for making a decorative
  box a scroll container, here `overflow:clip` is wrong for stopping a box that has to be one. **Clip
  decoration, or contain content** - one question, one property. The frame clips and the BODY scrolls,
  so the head and the close stay put. Verified as the question a person asks: **64 sheet-and-viewport
  combinations, last control reachable in all 64.**
- **Three checkers were reading text as markup**, all surfaced by the documents: the renderer left the
  quote unescaped, so a code block quoting `<link ... href="_theme.css">` failed gates 4 and 9; gate 4
  also read a `url()` inside a `<pre>` (**text inside `<code>` or `<pre>` is a quotation, not a
  reference**, which the component pages needed too, since each ends with its own source); and gate 20
  searched the whole text for a font host, so the page explaining why the host was dropped failed the
  gate that exists because of it (**a mention is not a call** - ask a `src`/`href` attribute and an
  `@import`).
- **A colour follows the surface it stands on.** The course sidebar keeps one dark palette in both
  grounds, and `.ck-note-link` inside it read `--text-brass`, which in daylight is the dark brass for a
  pale surface: **2.39:1 in the light theme on every page of the vitrine**. One role, `--chrome-accent`.
  The vitrine's sub-AA pairs went 434 to 158, all that is left being `kit.html` (frozen) and the value
  labels drawn ON their own swatches in `tokens.html`.
- Also: `ui-kit/fonts.html` existed because step 8 taught gate 2 that fonts is not a component with a
  stand and did not teach the page generator; the `Stands on:` header of 24 component files still said
  76 screens; and `.outcome-dialog a{text-decoration:none}` had been paying for another skin's markup
  (**a link that wraps a control is not a text link**, now in `dialog.css` for both trees).
- **One measure for the page** (reported by eye at a wide window). `--container-max` is 1400 and only
  the footer obeyed it: at 1920 the content ran 1620 while the footer under it stopped at 1400. Five
  bands carried `max-width:none` from the colour pass and read the token now, so the band spans the
  window and what is inside it (header row, category strip, trust bar, content, footer) shares one
  left edge.
- **An empty box is invisible to every sweep we run.** The four category pages and two feed states had
  a 56px photograph box with no photograph, because step 7c moved the picture out of
  `.grid > .card:nth-of-type(N) .thumb` onto the element and reached the pages that exist as files,
  not the cards a generator writes. **A missing picture passes a contrast sweep, an overflow sweep and
  a link check alike**; gate 9 asks for it now. The library has one photograph per category, so what
  varies on a single-category page is the CROP of it. And **a photograph is not one declaration**: the
  port stripped `background-image` on the way into grey and let `background-position` through, which
  is the framing of a picture that is not there.
- **A control is named by what it does.** The Event Feed had two controls doing the same thing: the
  top band navigates (a category is its own indexed URL), and the chip row labelled "Filter events by
  category" was five more links to the same pages, so pressing Politics inside Trending left Trending.
  It filters in place now (`wireframes/_generators/subfilter.py`, both trees, `data-cat` read out of
  the photograph each card already carries). Three shapes came with it: **hidden is a state, not a
  style** (the attribute was set and nothing moved, because `.card{display:flex}` beats the user
  agent's `display:none` whatever the specificity, so `base.css` carries the one `!important` in
  `components/`); **a checker that reads the attribute does not read the page** (the first run
  reported success while twelve cards were on screen); and **two generators writing into one sheet
  have to know where each other's work ends**, the step-7e lesson, paid for again when `port_chrome`
  and `subfilter` rewrote the same page back and forth forever.
- **A container holds its inset at every width.** Centring the content band by turning
  `margin:var(--gutter)` into `margin:var(--gutter) auto` spent the horizontal gutter on the centring,
  so under 1400 the plate sat against the window edge. The inset is padding; above the cap the auto
  margin centres. Measured at eight widths from 1920 to 380: header, content, plate and footer on one
  x at every one, gutter 40 above 640 and 14 below.
- **Half of twelve is six.** The two bars of the close X sat at `calc(50% - 7px)`, one pixel left of
  the disc, on every close button in the product. The vertical half was right, which is what made it
  hard to see.
- **Verified:** painted **420 page loads x 2 themes, 86534 text pairs, 0 below AA, 0 overflow, 0 page
  errors**; the vitrine 196 loads in both themes, every remaining failure present at HEAD; standalone
  dialog against shared, matched by class, **0 differences that paint**. Gates 19 and 21 tested by
  injecting the drift they exist to catch. **Gates: 21.**

### Step 9 (done, 2026-07-28): one panel, and the region no gate could see into

Started as a question about looks, why the two side panels look and work differently, and the answer
was not in the stylesheet: they are painted by one file and share every class name. **Twenty
findings, all closed.** Full record in `ui-kit/docs/architecture.md`, "What step 9 settled".

- **A gate that masks a region cannot see into it.** Gate 1 masks the `<aside>` when it asks whether
  a painted screen moved, correctly, because the panel is chrome and not the screen, and that made
  the panel the one thing nothing read. **Forty screens marked the wrong page as "you are here":**
  every category page and every feed state said `Event Feed -> success`. The cause is the shape this
  repo keeps meeting, `_apply_theme.py` and `_gen_category.py` build a screen from the finished
  Event Feed and swap the regions that differ, so **a new screen arrives carrying the shell's idea
  of where it is** and nobody re-ran `_resync_sidebar.py` after step 8. **Gate 22** is four checks:
  every screen marks its own file, every panel is what its generator would write today, every stand
  page names itself against the registry, and a page off the tree is still linked.
- **The thing that navigates was drawn quieter than the thing that does not.** A family name was a
  `.sidebar-page-link` with no href (13px, hover highlight, pointer cursor, no destination, 14 per
  screen on 105 screens) and the screen it named was a quiet nested row; in the vitrine those two
  classes mean the opposite. One vocabulary now: a **label** names a run of rows and opens nothing
  (`.sidebar-divider`, `.sub` when nested; `.sidebar-sub-head` deleted, and it had been drawn HEAVIER
  than the label above it, so depth read backwards), a **row** that opens a page is a link, the page
  you are **on** is `.active` at either level in one colour, and the group you are **in** is marked
  on its label, which the vitrine did not have at all.
- **Quiet is a colour, not an opacity.** Both labels, the note and a planned stage were dimmed with
  `opacity`, and opacity fades text INTO its background: `--chrome-muted` is 5.03:1 on the panel and
  the same value at `opacity:.55` is **2.37:1**. Five places under AA for as long as the panel has
  existed, and **no sweep this repo has run could see them, because they all read
  `getComputedStyle().color`, which does not carry opacity.** The step-6b lesson one level deeper: a
  checker that reads the computed colour is still not reading the rendered one.
- **One behaviour, two machines, one string.** Marking the row and never showing it is most of the
  way to not marking it (4066px of tree in a 900px panel; on `toasts.html` the brass row sat 3813px
  down). Both panels reveal it on load from one string in `ui-visual/_panel_reveal.py`.
  **`scrollTop`, not `scrollIntoView`**: the panel is `position:fixed` and asking an element inside a
  fixed box to scroll itself into view lets the browser scroll THE PAGE. The script lives inside the
  `<aside>`, which is the span gate 1 masks, so a panel can gain behaviour without 105 screens
  reading as product changes.
- **One component, seven descriptions.** The 28 course pages never linked the system file: 41 to 43
  rules each in **five distinct copies**, plus a sixth block injected by `_unify_sidebar.py` to force
  a violet palette. That is also why the four `.planned` rules had no markup in any tree
  `course-chrome.css` reaches: **the only panel with a planned row was the one it did not paint.**
  `_course_chrome.py` deletes the copies and the override, renames the drawer to the system's classes
  (its script addresses the elements by id, so only the paint moves) and links `fonts.css`,
  `tokens.css`, `course-chrome.css` last in `<head>`. `_unify_sidebar.py` deleted. Two things
  checked and not assumed: the course pages declare 14 variables against tokens.css's 348 and the
  sets **do not intersect at all**, so linking tokens cannot repaint their content; and the z ladder
  had to move together, because their 199/200/201 against the system's 8/9/10 would have opened the
  panel behind its own scrim.
- **A component that changes with the page it stands on is not a component**, so `.sidebar` names its
  own font instead of inheriting Inter on a course page.
- **A comment is not a rule, and a quotation is not an element.** Writing those comments broke the
  vitrine's own coverage table and exposed two defects in it: `parse_component` cut only the header
  comment, so `.css` and `.color` sat in the deletion-candidate list harvested out of the words
  "components/index.css" and "Colour goes through a role", and the kit bucket read the specimens and
  `kit.html` but not the 46 stand pages, so a class carried only by the vitrine's chrome fell through
  every bucket. **Deletion candidates: 28 to 2**, on a list step 7 acted on.
- Also: `.ck-note-link` moved from `ui-kit/_page.css` into `.sidebar-note a`, because a link in the
  note is the panel's own and it had been rendering in the browser's blue everywhere the vitrine's
  stylesheet is not loaded; a planned stage is a `<span>`; the tree is a named `<nav>` in all three
  panels; the note's mention of ui-kit is a link, so the way in exists in both directions, with no
  new copy written; `resync_sidebar.py` stops writing panel css, which it had been inserting into the
  page's own sheet reading `var(--accent)`, that page's violet; and `mark_group` lives in one file
  and is imported by the other, because for one turn the two tools each had their own idea of the
  mark and undid each other for ever.
- **One checker's own defect, recorded:** the light-theme sweep reported 105 failures at 1.12:1 and
  they were the `<script>` the reveal added inside the `<aside>`, counted as text. On graphite a
  script inherits light ink and passes; the moment the ground inverts it reads dark on dark. **A
  checker with a missing guard fails in one theme and looks exactly like a finding.**
- **Verified:** the panel in both trees and both themes, 308 loads, **18028 text pairs, 0 below AA**
  with opacity composited, 0 browser-blue, 0 overflow, 0 page errors, on a sweep calibrated first
  against a pair whose answer is known; the reveal on 153 panels at two viewport heights, **0 with
  the mark out of view, 0 documents scrolled**; the course pages, **795 text pairs, 0 below AA, 0
  dead anchors, 0 violet left**, one shape on all 28; their own content compared element by element
  against a worktree of HEAD, **28 of 28 identical**; **348 pages, 35773 internal links, 0 broken**.
  Gate 22 tested by injecting each of its four kinds of drift; all six generators reach a fixed point
  together over three rounds. **Gates: 22.**

### The rule for a change, from here on

Replaces the Stage-07 wording that pointed at `ui-kit/kit.css` and `ui-kit/kit.html`; neither has
that role any more.

- **A value** goes to the token of its own level and reaches every screen by itself: a colour is a
  **semantic role** in section 2 of `components/tokens.css`, a raw value is a **primitive** in
  section 1. A component may never read a colour primitive (gate 13) and may never write a raw scale
  value (gate 12).
- **Markup** goes to two places and only two: the component's page in `ui-kit/`, and the screens in
  `ui-visual/` where it stands. Never to a third copy. **A dialog that also has a standalone page is
  one markup, not two** (gate 19): the canonical copy is the one in `ui-visual/event-feed.html`, and
  only the head, the wiring and the state screens may differ, for the reasons written in
  `wireframes/_conventions.md`.
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
  `python3 ui-kit/_check_kit.py` has to pass, all twenty-one.
- **A document in `ui-kit/docs/` is a page of the vitrine.** It is rendered by `ui-kit/_gen_docs.py`
  and registered in `_gen_docs.PAGES`, which is also where `_gen_component_pages.py` reads the side
  panel group from; run the component generator first, because it writes `docs/coverage.md`. Nothing
  in `ui-kit/` or `ui-visual/` may link a raw `.md`: a browser downloads one instead of drawing it
  (gate 21).
- **A checker asks the markup, not the text.** A page that quotes markup is normal here (every
  component page ends with its own css, and the documents quote both), so a scan for a path, a
  `url()` or a font host has to skip what is inside `<code>` and `<pre>` and look at the attribute
  that would make the request. Three gates were reading a sentence as a reference.
- **`ui-kit/kit.html` is frozen.** It is the flat kit the system was read out of and it is kept as
  provenance; a component is never added to it. **`ui-kit/shell.html` composes** the header and
  bottom-nav specimens and holds no markup of its own.
- **Two token levels, not three.** Primitive + semantic. Colour is the only thing with a second
  level, because a radius or a gap has nothing for a theme to override; a component level is not
  part of this stage.
- **A dialog is bounded by the viewport and its BODY scrolls**, at every width. The frame keeps
  `overflow:clip` because it clips its own corners; a box cannot both clip decoration and contain
  content, and the answer is that the head stays and the body moves. A skin (`outcome-dialog`,
  `signin-dialog`) is named for what the sheet IS, and a standalone overlay page wears the shared
  dialog's own class list plus `app-case` (gate 19).
- **A screen has a twin, and the map is one file.** The two trees do not name every screen the
  same way (`politics.html` in grey, `event-feed-politics.html` in colour). That map is `_twins.py`
  at the root and nowhere else, because gate 18 pairs the trees by filename and an unpaired page is
  skipped in SILENCE: 32 grey category screens sat against 4 painted ones behind five hand-written
  copies of a map that all stopped at the base page. A new screen is built in both trees, or its
  absence is a declared exception.
- **A font is served from this repo.** No page may call a font host: the request carries a visitor's
  IP to a third party before the consent banner has asked anything (gate 20). Faces are woff2 in
  `assets/fonts/`, declared once in `components/fonts.css`, imported first by `index.css`.
- **Never paint `wireframes/`.** Structure and copy are owned there and stay grey; `ui-visual/` owns
  the visual layer only. **And the traffic runs the other way too**: a new block, a new control, a new
  section is decided in `wireframes/` and the colour copy follows. Gate 18 fails the build when the
  two trees disagree inside `<main>`, `<header>`, the bottom nav, `<footer>` or the sheet body of an
  invoked overlay; the six differences that are the layer boundary (plate wrappers, icon mechanism,
  photograph, chart data, the `TBD` chip, the page behind an overlay) are declared in
  `wireframes/_conventions.md`.
- **A state is the grey tree's; a shape is the paint's.** Inside the chrome the two trees answer
  different questions, so neither is simply the source: the paint owns what the header IS and the
  wireframe owns which state it is IN (auth variant, bottom-nav active slot, empty notifications).
  Reconcile in that order, `ui-visual/_reconcile_chrome.py` then
  `wireframes/_generators/port_chrome.py`, or a port carries the wrong answer into 104 files.
- **The side panel is one component with one vocabulary, in all three trees.** A **label** names a run
  of rows and opens nothing (`.sidebar-divider`, `.sub` when nested); a **row** that opens a page is a
  link (`.sidebar-page-link`, `.sidebar-sub-link` when nested under one); the page you are **on** is
  `.active` at whichever level it sits and the group you are **in** is `.active` on its label. A row
  that goes nowhere is not an `<a>`. The tree is a named `<nav>`. No page describes the panel in its
  own stylesheet: `ui-visual/` and `ui-kit/` reach it through `components/index.css`, the 28 course
  pages link `fonts.css` + `tokens.css` + `course-chrome.css` last in `<head>` (`_course_chrome.py`),
  and a panel's behaviour is one string in `ui-visual/_panel_reveal.py` emitted two ways.
- **Quiet is a colour, not an opacity.** `opacity` fades text into its background and no sweep that
  reads `getComputedStyle().color` can see it: `--chrome-muted` is 5.03:1 on the panel and 2.37:1 at
  `opacity:.55`. Depth is a colour role, so the value being chosen is the value being checked.
- **Gate 1 masks the `<aside>`, so nothing else reads it.** Gate 22 does: every screen's panel marks
  its own file, and every panel generator is at its fixed point, because a generator that copies a
  shell copies the shell's idea of where it is.
- **A checker that reads the source does not read the page.** "0 non-neutral hex in the wireframes"
  was true while 992 links rendered in the browser's blue, and "the chart is ported" was true while
  it drew as a black rectangle, because an SVG with no `fill` is black. **A missing value is a
  value.** Measure the computed result, in a browser, at both widths.
- **A UI string gets a row in `voice/docs/microcopy.md` before it ships**, then goes into both trees.
  That table is the source of truth for copy, and for one stage it was not: 43 shipped lines had no
  row in it.
