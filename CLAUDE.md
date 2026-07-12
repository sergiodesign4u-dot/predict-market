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

IA sources (source of truth): `ia/docs/sitemap.md` (entities, screens, navigation, desktop layer, depth map, tracing) and `ia/docs/flows.md` (user flows). The HTML visualizations `ia/ia.html`, `ia/sitemap.html`, `ia/flows.html` are re-synced to the markdown (green "Synced" banners); the markdown stays the source of truth if they ever diverge again.

**Repo layout:** 13-stage course structure, one folder per stage, raw markdown in each stage's `docs/` and the stage HTML flat at the folder root. Full map in `STRUCTURE.md`. User Research now has 4 pages (Personas, JTBD, CJM As-Is, CJM To-Be); CJM (As-Is + To-Be) is a separate status row and lives inside User Research. The CJM sharpens the MVP scope above (one version, not a fork).

### Detailed layer (Stage 03b) - stance + scope

Three decisions that govern every page-level IA node:
- **Stance: mobile-first, fully adaptive.** Desktop <-> mobile responsive, but mobile is the priority; block priority and the first screen are reasoned from mobile (base 360px). Desktop is designed deliberately, not derived.
- **Two IA layers.** Global (Stage 03a - concept-map + flows, done) answers "where can the user go"; per-page (this layer) answers "what is on each page and how it behaves" (blocks, states, components, SEO).
- **SEO-ahead.** The structural SEO layer (URL/slug, H1/H2, breadcrumbs, schema.org, indexation, internal-linking) is defined here in IA. The wireframe validates layout only; production supplies final content + real query volumes. The three are not mixed, so finding "a block is missing" never means redrawing a wireframe.

**Scope = targeted reconcile (2026-07-12), not the full node-by-node build.** The 99 wireframes already exist and ARE the per-page B/W render, so we do NOT redraw pages, write a `pages/*.md` per screen, add an `ia/_nav.js`, or renumber the sitemap to X.Y (all would duplicate the wireframes or `resync_sidebar.py`). We build only what the wireframes deliberately omit and a launch needs:
- the **A-E SEO structural layer** for the indexed public pages (Event Feed, Event Detail, Category, How It Works, Public Profile); every private/transactional zone is `noindex`, no schema;
- the **footer** as an SEO / internal-linking node;
- the **system / global nodes** (404, 500, maintenance 503, cookie-consent grounded in law, toasts).

New sources live in `ia/docs/pages/` (`seo.md`, `system.md`); rendered B/W as `ia/seo.html`, `ia/system.html`. The shared sidebar stays single-source via `resync_sidebar.py` (not `_nav.js`); new IA pages register there.

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

- **Status: complete.** 99 pages - every screen in the IA screen tree, each state its own page, plus the Favorites view (`favorites.html` + empty + loading). Orphans `[SIROTA]` (Settings, Leaderboard, Help/FAQ) unbuilt by design; the standalone Bet Screen is dissolved into the inline Event Detail bet panel.
- **Style:** neutral greys only - no color, type, shadows, icons-as-art, or finished UI (those are the Concept phase). Monochrome outline SVG icons only. A left screen-tree panel is on every page.
- **Annotations moved out (2026-07-03):** the wireframes are now clean grey-box UI only. The inline `zone:` chips and the bottom `.side` block (the `zone -> job / finding` annotation list + nav-tree / header-model / responsive / variant notes) were extracted into a dedicated IA visualization at **`ia/annotations/`** - one HTML page per screen family, every state inside it, each state showing a nested zone map + its annotations + a link to the live wireframe, plus shared structure/flow notes. Entry point: `ia/annotations/index.html`. Styled in the dark research/IA-viz theme and wired into the **shared left sidebar** as "Wireframe Annotations" (under the Plan section, after Wireframes) on all root viz pages (`research/personas/jtbd/ia/sitemap/flows.html`); the annotation pages carry that same sidebar (with a sub-link per screen). Generated + stripped idempotently by `wireframes/_generators/ia_annotations.py` (`build` then `strip`; run `build` before `strip`). IA source of truth stays `ia/docs/sitemap.md` + `ia/docs/flows.md`.
- **States & auth:** browse screens (Event Feed, Event Detail, Category pages) have logged-in and logged-out variants; each screen carries its full state set (loading/empty/error/success + product-specific). Public Profile and How It Works carry the logged-out header (reached pre-auth).
- **Flow-linked:** the main flow is clickable end to end (Event Feed -> Event Detail -> gate dialogs -> Active Bets) with branch exits and no dead-ends, wired along `ia/docs/flows.md`. Sign In / Deposit are shared in-page `<dialog>`s; Win / Loss are invoked overlays. A 2026-07-07 flow-wiring audit (step 7) verified every edge against `ia/docs/flows.md` and fixed the last naked recovery buttons (`Try again` on the Event Feed + Category error pages, `Try another card` on `deposit-error-card`); see `wireframes/_critique.md`.
- **Interface copy rewritten against the product voice (2026-07):** every UI line was edited line-by-line against `voice/docs/voice.md` (five principles + lexicon + forbidden + per-element rules). `voice/docs/microcopy.md` holds the read-only text inventory it was edited from plus the full rewrite log (all screen families done, incl. the step-13 "rest of the screens" pass). The wireframes stay the render surface; to change shipped copy, edit the HTML and log it there.
- **Chrome wiring:** header (Favorites -> Favorites view, bell -> Notifications, avatar dropdown -> Profile/My Bets/Wallet/How It Works/Logout) and the mobile bottom nav are real links, not dead buttons; logged-out controls open the sign-in dialog. Favorites resolves to the Favorites view. See `wireframes/_conventions.md` Shared chrome wiring. Applied by the idempotent `fixpack.py` post-processor.
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
