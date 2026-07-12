# SEO structural layer - IA Detailed layer (Stage 03b)

This file is the structural SEO layer for the indexed public pages. It is part of the
Information Architecture, not a production content pass: it fixes URL, headings, schema,
indexation and internal-linking now, so the wireframe only has to validate the layout and
production only has to supply final copy and real query volumes (SEO-ahead, see CLAUDE.md
IA > Detailed layer). The 99 wireframes are the per-page B/W render; this file does not
redraw them, it adds the SEO structure they deliberately do not carry.

**Scope (targeted reconcile).** A-E blocks are written only for the pages that are actually
indexed (below). Every private or transactional zone is `noindex` and gets no schema; those
are listed once in the indexation policy, not spec'd page by page.

**Convention.** `{ROOT}` = the production origin (domain not chosen yet, `[?]`). All canonical
URLs are shown relative to it. Language rule: analysis and labels are English; the ready
product copy inside A-E blocks (title, H1/H2, body text) is the product language (English
here), because a wireframe or a build carries it verbatim as real UI text. No em dash.

---

## Indexation policy

One row per screen family. `index,follow` = crawled and eligible to rank; `noindex,follow` =
kept out of the index but its links are still followed; private and transactional zones are
`noindex`. Only the `index` rows get an A-E block in this file.

| Screen family | URL pattern | Robots | Why |
|---|---|---|---|
| Event Feed (home) | `/` | `index,follow` | The entry page and the main ranking surface. §1 |
| Event Detail | `/event/{slug}` | `index,follow` | The money pages; one indexed URL per event, the deep-link target of shares and search. §2 |
| Category | `/c/{category}` | `index,follow` | Intent landing per category (Politics, Crypto, Culture, General). §3 |
| How It Works | `/how-it-works` | `index,follow` | Trust and explainer page; ranks for "how do prediction markets work" intent. §4 |
| Public Profile | `/u/{handle}` | `index,follow` `[?]` | Public reputation / track record. Indexed by default; per-user opt-out to `noindex` is a `[?]` for the privacy pass. §5 |
| Favorites view | `/favorites` | `noindex,follow` | Personal watchlist, requires auth, no unique public content |
| Sign In / Register | `/signin` | `noindex,follow` | Thin transactional gate; links followed |
| Deposit / Add funds | `/deposit` | `noindex` | Transactional, auth-gated, no schema |
| Wallet | `/wallet` | `noindex` | Private balance and transactions |
| Bet panel | inline on Event Detail | n/a | No own URL (inline panel), inherits Event Detail |
| Win / Loss | invoked overlay | `noindex` | Personal outcome, reached from a notification, no own indexable URL |
| Active Bets / History | `/my-bets` | `noindex` | Private positions |
| Notifications | `/notifications` | `noindex` | Private |
| My Profile (self) | `/profile` | `noindex` | Private; the Public Profile (§5) is the indexed twin |
| Search results | `/search` | `noindex,follow` | Deferred until catalog scale; when live, results are `noindex,follow` |
| System (404 / 500 / 503) | n/a | `noindex` | Error and maintenance pages, never indexed. See `system.md` |
| Cookie consent | banner component | n/a | Not a page. See `system.md` |
| Orphans: Settings | `/settings` | `noindex` | Private |
| Orphans: Leaderboard | `/leaderboard` | `index,follow` `[?]` | Post-MVP; indexed when built |
| Orphans: Help / FAQ | `/help` | `index,follow` `[?]` | Post-MVP; indexed when built |

---

## The A-E template

Every indexed page below carries the same five blocks.

- **A. Meta tags (ready copy).** `title` (<= 60 chars), `meta description` (<= 155),
  `canonical`, `hreflang`, `robots`, Open Graph (`og:title`, `og:description`, `og:type`,
  `og:url`, `og:image`), Twitter (`twitter:card`, `title`, `description`, `image`).
- **B. Heading structure.** Exactly one `H1`, then the ordered `H2` list in the same order as
  the mobile-first block stack.
- **C. Ready SEO body text.** The copy that actually ships in the page's text sections, in the
  product voice. Not "fill in later".
- **D. Structured data.** The schema.org types for the page and their key properties.
- **E. Optimization checklist.** One H1, LCP target, crawlable `<a>`, canonical + hreflang,
  text-not-in-images, Core Web Vitals budget, correct robots directive.

---

## 1. Event Feed (home)

- Node: Event Feed - Type: page - serves FJ1 (find / return), FJ2 (understand the odds), MJ (entry to the main job)
- URL / slug: `/` - Breadcrumbs: none (home is the root)
- Indexation: `index,follow` - the single most important ranking page

### A. Meta tags

- `title`: **Predict Market - bet YES or NO on live events** (46 chars)
- `meta description`: **Browse live events and back your opinion with a real stake. Plain-language odds, a one-line why, and how each event resolves. Start with no wallet.** (147 chars)
- `canonical`: `{ROOT}/`
- `hreflang`: `en` -> `{ROOT}/` (single locale now; more locales `[?]` TBD)
- `robots`: `index,follow`
- `og:title`: Predict Market - bet YES or NO on live events
- `og:description`: Back your opinion on real-world events with a real stake. Odds in plain language, no wallet to start.
- `og:type`: `website`
- `og:url`: `{ROOT}/`
- `og:image`: `{ROOT}/og/home.png` (1200x630, the Share Card asset; `[?]` asset TBD)
- `twitter:card`: `summary_large_image`; `twitter:title` / `twitter:description` / `twitter:image` mirror the OG values

### B. Heading structure

- `H1`: **Live events** (the feed heading; on a Category page the active category echoes into the H1, see §3)
- `H2` in mobile block order:
  1. **Trending now** (default sort band)
  2. **Ending soon**
  3. **Browse by category** (Politics, Crypto, Culture, General - each a crawlable `<a>`)
  4. **How betting works here** (short explainer, links to How It Works)
  5. **Why the odds move** (the explain-the-number teaser)
  6. **Common questions** (feeds the FAQPage schema)

Wireframe delta: bands 1-3 already render in `event-feed.html`. Sections 4-6 are SEO content
blocks that belong below the fold; adding them to the feed is a small, optional delta (they do
not change the primary layout), logged here so the wireframe can validate the slot later.

### C. Ready SEO body text

**How betting works here.** Predict Market turns the events you follow into a real stake. Pick
an event, read the odds in plain language, and back YES or NO. You see the current odds, a
one-line why, and how the event resolves before you put in a cent. The minimum bet is one
dollar, and you can browse and build your bet before you connect a wallet.

**Why the odds move.** The odds are a live price set by what people bet, not a fixed quote.
When more money backs YES, YES costs more and NO costs less. Your payout depends on the odds
at the moment you bet, not only on the outcome, so reading an event early and being right is
worth more.

**Common questions.**
- **Do I need crypto to start?** No. You can browse events and build a bet with no wallet. You
  add funds by card or crypto only when you confirm.
- **What is the smallest bet?** One dollar. The default is five.
- **How does an event resolve?** Each event states its resolution rule up front. The team
  resolves it against the real-world outcome, and you can see the record of resolved events.

### D. Structured data

- `WebSite` - `name` "Predict Market", `url` `{ROOT}/`. No `SearchAction` (search is deferred, `[?]`).
- `Organization` - `name`, `url`, `logo`, `sameAs` social profiles `[?]`.
- `CollectionPage` - the feed itself; `mainEntity` -> the `ItemList` below.
- `ItemList` - the visible events, each `ListItem` linking to its Event Detail URL (`/event/{slug}`). The rich per-event schema lives on Event Detail (§2), not here.
- `FAQPage` - the three "Common questions" Q&A pairs.

### E. Optimization checklist

- Exactly one `H1` ("Live events").
- LCP: server-render the first ~6 event cards (above the fold) so LCP is a card, not a late JS paint; no large blocking hero image.
- Crawlable `<a>`: every event card and every category is a real `<a href>`, not a JS-only handler, so crawlers reach Event Detail (§2) and Category (§3).
- Canonical self-referential (`{ROOT}/`); sort and filter params (`?sort=`, `?freq=`) canonical back to `{ROOT}/` and are `noindex` facet combinations.
- `hreflang` present (`en` only now; more locales `[?]`).
- Text not in images (odds and labels are live text).
- Core Web Vitals budget: LCP < 2.5s, CLS < 0.1 (reserve card heights so odds loading does not shift layout), INP < 200ms.
- `robots`: `index,follow` confirmed.
