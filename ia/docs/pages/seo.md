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

---

## 2. Event Detail

- Node: Event Detail - Type: page (inline bet panel, no separate URL) - serves MJ (the bet happens here), FJ2 (understand the odds), SJ1 (share)
- URL / slug: `/event/{slug}` - `{slug}` is the event question slugified, stable, and it does NOT change when the odds move
- Breadcrumbs: `Home > {Category} > {Event}` (e.g. `Home > Politics > Will the incumbent win`)
- Indexation: `index,follow` - the deep-link target of every share and search result

The event question, the one-line why, the news story, comments, usernames and sample figures
are user or team content and are never voice-rewritten (see voice rule). Below, those are
template slots `{...}`; only the evergreen / reusable copy is fixed.

### A. Meta tags

- `title` (template, <= 60): **{Question} - Predict Market**. If the question is long, truncate the question, keep the brand suffix. Example: **Will Bitcoin close above $100k on Dec 31? - Predict Market** (58 chars).
- `meta description` (template, <= 155): **{YES}% YES right now on: {Question, truncated}. See the odds in plain language, why they moved, and how this event resolves. Bet from $1.** Dynamic parts are the odds and the question. Example: **62% YES right now on Bitcoin above $100k by Dec 31. See the odds in plain language, why they moved, and how it resolves. Bet from $1.** (133 chars)
- `canonical`: `{ROOT}/event/{slug}`
- `hreflang`: `en` -> `{ROOT}/event/{slug}` (more locales `[?]`)
- `robots`: `index,follow` (a resolved event stays `index,follow`, see E)
- `og:title`: {Question}
- `og:description`: the short "{YES}% YES, plain-language odds, how it resolves" line
- `og:type`: `website` (NOT `article`; the page is a live market, not a dated article)
- `og:url`: `{ROOT}/event/{slug}`
- `og:image`: `{ROOT}/og/event/{slug}.png` - the per-event Share Card (question + current odds, 1200x630), regenerated on an odds snapshot; this is the SJ1 share asset
- `twitter:card`: `summary_large_image`; title / description / image mirror OG

### B. Heading structure

- `H1`: **{the event question}** (exactly one H1, the question itself)
- `H2` in mobile block order:
  1. **Odds** (the YES / NO odds and the inline bet panel)
  2. **Why this number** (the one-line why and the news story)
  3. **How this event resolves** (the resolution rule and its source)
  4. **Comments** (user discussion; fresh, long-tail content)
  5. **Related events** (crawlable links to sibling events in the same category)

Wireframe delta: blocks 1-4 already render in `event-detail.html` (odds + inline bet panel,
the content tabs incl. Comments). "Related events" is an SEO internal-linking block to add
below the tabs; small, optional, logged for the wireframe to validate.

### C. Ready SEO body text

**Evergreen intro (reusable on every event).** Back YES or NO on this event. You see the odds
in plain language and how it resolves before you bet. The minimum is one dollar, and you can
build your bet before you connect a wallet.

**Why this number (template).** Right now the odds put YES at {YES}%. {One-line why - team
editorial, e.g. "The latest polls moved toward the incumbent this week."} The number is a live
price, so it moves as people bet.

**How this event resolves (template, mostly reusable).** This event resolves YES if {the
condition stated on the event}. The team resolves it against the real-world outcome using
{named source}. Resolution date: {date}. Once resolved, the outcome and the timing of every
bet stay visible.

### D. Structured data - the per-event schema decision (resolves the §1 `[?]`)

**Use `WebPage` + `BreadcrumbList`.** Optionally add `Comment` for the discussion and `FAQPage`
for the resolution Q&A if surfaced.

Rejected, with reasons:
- **`schema.org/Event`** - NO. It models a scheduled real-world happening (startDate, location,
  performer) and makes the page eligible for Google event rich results, which would misrepresent
  a prediction market as a ticketed event. A market question is not an `Event`.
- **`QAPage`** - declined. It expects one user question with an accepted answer and an answer
  count; a market question with betting + comments does not fit that shape.
- **`Product` / `Offer`** - declined. Treating a bet as a product invites e-commerce price
  rich results (price, availability) that misframe a wager and carry compliance risk.

So: `WebPage` (name = the question, `breadcrumb`), `BreadcrumbList` (Home > Category > Event),
plus `Comment` / `FAQPage` where the content exists. This stays honest and avoids a rich-result
mismatch. `[?]` resolved.

### E. Optimization checklist

- Exactly one `H1` = the event question; unique `title` and `description` per event (templated from question + odds), no duplicate meta across events.
- Slug is human-readable and stable; it does not change when odds move.
- A **resolved** event keeps its URL, stays `200` and `index,follow`, and shows the resolved state (outcome + at-close odds); it is never redirected or 404'd. It is an indexed archive, not a dead-end (matches `event-detail-resolved.html`).
- Crawlable `<a>` to Related events and to the parent Category (internal linking).
- Odds are live text on the page (not only baked into the OG image).
- Canonical self-referential; strip share / tracking params (`?ref=`, `?utm=`) via canonical.
- Comments and tab content are in the DOM (crawlable), not loaded only on interaction.
- Core Web Vitals: LCP = the question + odds block; reserve the bet-panel height to avoid CLS as odds load.

---

## 3. Category

- Node: Category - Type: page (one canonical listing template for all categories) - serves FJ1 (browse by interest)
- URL / slug: `/c/{category}`, `{category}` in `politics | crypto | culture | general` (more categories post-MVP)
- Breadcrumbs: `Home > {Category}`
- Indexation: `index,follow` on the clean category URL; facet combinations are `noindex` (see E)

One template renders every category; only the H1, the "about" copy, and the meta differ. Sports
and other post-MVP categories reuse the same template.

### A. Meta tags

- `title` (template, <= 60): **{Category} events - Predict Market**. Example: **Politics events - Predict Market** (32 chars).
- `meta description` (template, <= 155): **Bet YES or NO on live {category} events. Plain-language odds, a one-line why, and how each resolves. Browse {category} now, no wallet to start.** Example (politics): **Bet YES or NO on live politics events. Plain-language odds, a one-line why, and how each resolves. Browse politics now, no wallet to start.** (139 chars)
- `canonical`: `{ROOT}/c/{category}`
- `hreflang`: `en` -> `{ROOT}/c/{category}` (more locales `[?]`)
- `robots`: `index,follow`
- `og:title`: {Category} events; `og:description`: the short listing line; `og:type`: `website`; `og:url`: `{ROOT}/c/{category}`; `og:image`: `{ROOT}/og/c/{category}.png` (`[?]` asset TBD)
- `twitter:card`: `summary_large_image`; mirrors OG

### B. Heading structure

- `H1`: **{Category} events** (the active category echoes into the H1, e.g. "Politics events")
- `H2` in mobile block order:
  1. **Trending in {category}**
  2. **Ending soon**
  3. **All {category} events**
  4. **About {category} events** (SEO body, below the fold)
  5. **Common questions** (reuses the home FAQ set)

Wireframe delta: the four category pages exist (`category-*.html`) with the event bands (1-3).
"About {category} events" is the one SEO text block to add below the fold; small, optional.

### C. Ready SEO body text

**About {category} events (template).** Follow {category} events and back your opinion with a
real stake. You see the odds in plain language and how each event resolves before you bet, from
one dollar, with no wallet to start. The one-line "what this category covers" fill per category:

| Category | "This category covers ..." fill |
|---|---|
| Politics | elections, policy votes, appointments, and other public decisions |
| Crypto | token prices, launches, network upgrades, and protocol milestones |
| Culture | awards, releases, sports and entertainment milestones, and cultural firsts |
| General | real-world questions that do not fit the other categories |

### D. Structured data

- `CollectionPage` - the category listing; `mainEntity` -> the `ItemList`.
- `BreadcrumbList` - `Home > {Category}`.
- `ItemList` - the category's events, each `ListItem` linking to its Event Detail URL (`/event/{slug}`).
- `WebSite` / `Organization` inherited site-wide (declared once on the home, §1).

### E. Optimization checklist

- Exactly one `H1` = "{Category} events"; unique `title` / `description` per category, no duplication across categories.
- **Facet control:** the clean `/c/{category}` is indexed; sort and frequency combinations (`?sort=`, `?freq=hourly`) are `noindex,follow` and canonical back to `/c/{category}`, so facets do not bloat the index.
- Crawlable `<a>` to every event, to the sibling categories (cross-linking), and back to the home.
- **Pagination:** if a category paginates, page URLs are `?page=N` with a self-referential canonical per page; `rel=next/prev` is optional `[?]`.
- **Empty category:** a category with no live events is still a valid page with a way out (upcoming or recently resolved), not a soft-404; consider `noindex` only while genuinely empty `[?]` (matches the empty-state wireframe).
- Text not in images; server-render the first cards; reserve card heights (CLS).
- Core Web Vitals budget as §1.
