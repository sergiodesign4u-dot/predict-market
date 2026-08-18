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

## What is built, and where each half lives, 2026-08-16

**This file is the home of the head layer and it stays the home.** Measured before anything was
written: both screen trees carried **0 of the five metadata classes** (description, canonical, og,
twitter, ld+json) across 217 documents, and both prove why in the same element. Their `<title>` names
the ARTEFACT rather than the page: `UI Visual - Event Feed` and
`Wireframe - Event Detail (logged in - state: success / binary)`. **Neither tree models a document
head; each labels a drawing.** Copying the A-block meta tags into 109 painted files would also make
109 copies of facts that live here once, which the root `CLAUDE.md` forbids by name, with drift as
the stated cost. And `{ROOT}` is still `[?]`: a canonical or an `og:url` cannot be written without
inventing a domain nobody has chosen.

**The D block is different and it is built.** Structured data is the only half that RESTATES the
page's own visible content, so it is the only half that can drift from the page, and drift is
measurable only where both halves stand together. `BreadcrumbList` must match the trail,
`ItemList` must match the cards, `FAQPage` must match the `<dl>`, `dateModified` must match the date
the page renders. That is this file's own rule, written under §6: "One date, two consumers: if the
page shows a date the schema does not, the schema is wrong."

**58 of 108 painted documents carry one `application/ld+json` block**, one `@graph` each, over **12
distinct page `@id`s**: home (`WebSite`, `Organization`, `CollectionPage`, `ItemList`, `FAQPage`),
the four categories (`CollectionPage`, `BreadcrumbList`, `ItemList`), the event detail (`WebPage`,
`BreadcrumbList`), How It Works (`WebPage`, `BreadcrumbList`, `FAQPage`), the public profile
(`ProfilePage`, `Person`, `BreadcrumbList`) and Terms (`WebPage` with `dateModified`,
`BreadcrumbList`). The other 50 are the `noindex` families in the table below, and they carry none.

**URLs are relative and that is not a shortcut.** `/`, `/c/politics`, `/event/{slug}`,
`/how-it-works`, `/u/{handle}`, `/legal/terms` are the product's URL space as this file writes it.
The prototype's file names are not that space, and the schema describes the product.

**A STATE MAY SHOW LESS, NEVER SOMETHING DIFFERENT.** One URL carries one `@id`, and its states
carry node sets that are subsets of the success state's: the empty, error and loading feeds have no
`ItemList`, because there is no list on them to describe. Two documents carry no schema at all,
`event-detail-loading` and its logged-out twin, because the only thing that URL's schema is about is
the question, and a loading skeleton does not show it. Verified on both engines: **58 of 58 parse, 0
banned types, 0 nodes disagreeing with the visible page, 0 subset violations.** The three types this
file rejects by name, `Event`, `QAPage` and `Product` / `Offer`, are checked for and read 0.

**What is specified here and could not be built**: `Organization.logo` and `sameAs` (no asset, and
the social marks were removed by backlog 144), and `WebSite.SearchAction` (search shipped on
2026-08-16 but the deferral's scale condition has not, `docs/backlog.md` 164).

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
| Static content | `/legal/{slug}`, `/about` | `index,follow` | Terms, Privacy, Cookie Policy, Responsible betting, About. Registered as page nodes in `sitemap.md` and promised by the footer on all 104 screens; this file had no row for them until 2026-08-03. §6 |
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

- `title`: **Yonder - bet YES or NO on live events** (46 chars)
- `meta description`: **Browse live events and back your opinion with a real stake. Plain-language odds, a one-line why, and how each event resolves. Start with no wallet.** (147 chars)
- `canonical`: `{ROOT}/`
- `hreflang`: `en` -> `{ROOT}/` (single locale now; more locales `[?]` TBD)
- `robots`: `index,follow`
- `og:title`: Yonder - bet YES or NO on live events
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

**How betting works here.** Yonder turns the events you follow into a real stake. Pick
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

- `WebSite` - `name` "Yonder", `url` `{ROOT}/`. No `SearchAction` (search is deferred, `[?]`).
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

- `title` (template, <= 60): **{Question} - Yonder**. If the question is long, truncate the question, keep the brand suffix. Example: **Will Bitcoin close above $100k on Dec 31? - Yonder** (58 chars).
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

- `title` (template, <= 60): **{Category} events - Yonder**. Example: **Politics events - Yonder** (32 chars).
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

---

## 4. How It Works

- Node: How It Works - Type: page - serves SJ2 (understand and trust the mechanics), HJ (help)
- URL / slug: `/how-it-works` - Breadcrumbs: `Home > How it works`
- Indexation: `index,follow` - the trust and explainer page; the ranking target for "how do prediction markets work" and "how to bet on events" intent

This is a genuine content page (not user content), so the copy below is real ships-copy.

### A. Meta tags

- `title` (<= 60): **How prediction markets work - Yonder** (44 chars)
- `meta description` (<= 155): **See how betting on real-world events works: pick an event, read the odds in plain language, back YES or NO, and see how it resolves. Bet from $1.** (145 chars)
- `canonical`: `{ROOT}/how-it-works`
- `hreflang`: `en` -> `{ROOT}/how-it-works` (more locales `[?]`)
- `robots`: `index,follow`
- `og:title`: How prediction markets work; `og:description`: the short explainer line; `og:type`: `website`; `og:url`: `{ROOT}/how-it-works`; `og:image`: `{ROOT}/og/how-it-works.png` (`[?]`)
- `twitter:card`: `summary_large_image`; mirrors OG

### B. Heading structure

- `H1`: **How it works** (the product heading; the query "prediction markets" is carried by the title and the first H2)
- `H2` in mobile block order:
  1. **What a prediction market is**
  2. **Pick an event and read the odds**
  3. **Back YES or NO**
  4. **Why the odds move**
  5. **How events resolve**
  6. **Your money and safety**
  7. **Common questions**

### C. Ready SEO body text

**What a prediction market is.** A prediction market lets you back your opinion on a real-world
event with a real stake. Each event is a yes-or-no question, like whether something will happen
by a date. You bet YES or NO, and you earn or lose based on the outcome.

**Pick an event and read the odds.** Every event shows its odds as a plain-language number,
plus a one-line why and the news behind it. The odds are the current price, not a fixed quote.

**Back YES or NO.** Choose a side and an amount. The minimum is one dollar and the default is
five. You can browse and build your bet before you connect a wallet; you add funds by card or
crypto only when you confirm, and the fee is shown before you confirm.

**Why the odds move.** The odds are set by what people bet. When more money backs YES, YES costs
more and NO costs less. Your payout depends on the odds at the moment you bet, not only on the
outcome, so reading an event early and being right is worth more.

**How events resolve.** Each event states its resolution rule up front. The team resolves it
against the real-world outcome, and you can see the record of resolved events. If you were
right, you can see it and share it; if not, you can see what happened.

**Your money and safety.** Funds are held in USDC, one to one, and we never lend it out. You
can add or withdraw at any time. The fee for a bet is shown before you confirm.

**Common questions.** Reuses the home FAQ set (do I need crypto to start, the smallest bet, how
an event resolves), plus one: **Can I lose more than I bet?** No. Your loss is limited to what
you staked on the bet.

### D. Structured data

- `WebPage` + `BreadcrumbList` (`Home > How it works`).
- `FAQPage` - the "Common questions" block.
- `schema.org/HowTo` is declined: Google deprecated HowTo rich results (2023), so it earns no
  enhanced result and adds risk. A plain `WebPage` with clear headings is the honest choice.

### E. Optimization checklist

- Exactly one `H1`; evergreen, indexable content; no thin or duplicate text.
- Crawlable `<a>` to Event Feed and the categories (the page CTA is "Browse events"); the home and footer link IN to this page.
- FAQ Q&A is in the DOM (crawlable), matching the visible `FAQPage` schema.
- Text not in images; canonical self-referential.
- Core Web Vitals budget as §1.

---

## 5. Public Profile

- Node: Public Profile - Type: page - serves SJ1 / SJ2 (reputation, track record as trust)
- URL / slug: `/u/{handle}` - Breadcrumbs: `Home > {handle}`
- Indexation: `index,follow` by default, with a per-user opt-out to `noindex` `[?]` (privacy pass). The private self-view (My Profile, `/profile`) is always `noindex` (policy table).

Stats, the handle, and figures are user data and are never voice-rewritten; below they are
template slots `{...}`. Only public fields are ever indexed - never email, wallet, or balance.

### A. Meta tags

- `title` (template, <= 60): **{Handle} - track record - Yonder**. Example (handle "alex"): **alex - track record - Yonder** (36 chars).
- `meta description` (template, <= 155): **See {handle}'s prediction track record on Yonder: resolved events, the calls that were right, and current bets.** Example: **See alex's prediction track record on Yonder: resolved events, the calls that were right, and current bets.** (115 chars)
- `canonical`: `{ROOT}/u/{handle}`
- `hreflang`: `en` -> `{ROOT}/u/{handle}` (more locales `[?]`)
- `robots`: `index,follow` (per-user opt-out -> `noindex` `[?]`)
- `og:title`: {handle} on Yonder; `og:description`: the short track-record line; `og:type`: `profile`; `og:url`: `{ROOT}/u/{handle}`; `og:image`: `{ROOT}/og/u/{handle}.png` (`[?]`)
- `twitter:card`: `summary_large_image`; mirrors OG

### B. Heading structure

- `H1`: **{handle}** (the public handle or display name; exactly one H1)
- `H2` in mobile block order:
  1. **Track record** (resolved calls and the record)
  2. **Current bets** (public bets only)
  3. **Recent activity**

### C. Ready SEO body text

**Evergreen line (reusable).** This is {handle}'s public track record on Yonder. The
numbers count resolved events only. Follow real-world events and back your opinion with a real
stake. The remaining content (record, current bets, activity) is the user's own data.

### D. Structured data

- `ProfilePage` (schema.org/ProfilePage) - the honest fit for a person's public profile.
- `Person` - `name` / handle, public fields only.
- `BreadcrumbList` - `Home > {handle}`.

### E. Optimization checklist

- Exactly one `H1` = the handle; `index,follow` by default with a per-user `noindex` opt-out `[?]`.
- The private self-view `/profile` is `noindex` (policy table); do not let it and `/u/{handle}` index the same content.
- Only public fields are indexed - never email, wallet address, or balance (PII).
- Crawlable `<a>` from the profile to the user's public events.
- The handle in the URL is stable; a rename sets a `301` from the old handle `[?]`.
- **Thin profile:** a profile with no resolved bets is thin; consider `noindex` until it has public content `[?]`.
- Canonical self-referential; text not in images; Core Web Vitals budget as §1.

---

## 6. Static content (Terms, Privacy, Cookie Policy, Responsible betting, About)

- Nodes: the five page nodes registered under SYSTEM AND GLOBAL in `sitemap.md` - Type: page - `index,follow`
- URLs: `/legal/terms`, `/legal/privacy`, `/legal/cookies`, `/legal/responsible-betting`, `/about`
- Blocks: `ia/docs/blocks.md`, Type 1. Two body profiles, DOCUMENT for the four legal pages and STATEMENT for About; the A-E below is written per profile where they differ.

**One A-E for five nodes, because the SEO layer is decided by page TYPE.** These five share a
template and differ only in the slug, the H1 and the body copy, which is exactly the reason the
block bank is banked by type. Contact / Support is not here: it carries a form, so it is a different
type in both files.

### A. Meta tags (ready copy)

- `title`: `{Document name} | Yonder` for the four legal pages (`Terms of Service | Yonder`, 33 chars); `About Yonder` for About (20). All under 60.
- `meta description`: written per node, under 155, and it states what the document DECIDES rather than that it exists. Terms: `The rules you agree to when you back an event on Yonder: your account, your funds, how a market resolves, and how disputes are handled.` (144). About: `Who builds Yonder, how an event resolves, where your USDC sits, and how many events we have settled.` (107).
- `canonical`: self-referential, one per node. **No `?print` or `?v=` parameter is ever canonical**, which matters because block B12 (download / print view) is banked as LATER.
- `hreflang`: `en` only at MVP, with `pt-BR` reserved for the Brazil Phase 2 already named in `sitemap.md`. A jurisdiction variant of a legal page is a different document, not a translation, so a future geo split gets its own URL rather than an `hreflang` alternate.
- `robots`: `index,follow`. These pages are a ranking surface for brand-plus-trust queries and the destination of every footer link on 109 painted screens and 92 grey ones, re-counted 2026-08-18; it said 104 while the trees were 109 and 110.
- Open Graph: `og:type` = `website` for About, `article` for the four legal pages, because a legal document has an `article:modified_time` and that is the field block B4 already carries on the page.
- `og:image`: the shared brand card, not a screenshot. A legal page has no image of its own and inventing one is the one place this type would grow decoration.

### B. Heading structure

DOCUMENT profile, in the mobile-first block order from `blocks.md`:

- `H1` - the document name, exactly once (B3).
- `H2` - one per document section (B6), numbered, written as the reader's own question. The H2 list IS the table of contents (B5); the anchors are generated from it, so a section added to the body and not to the contents is impossible by construction.
- `H3` - only where a section has genuinely subordinate parts. No skipped levels, in both trees, which gate 15 already reads.
- The effective-date block (B4) and the money answer (B7) are **not** headings. They stand between the H1 and the first H2 as content, so the outline stays the document's own.

STATEMENT profile: `H1` = `About Yonder`; `H2` in block order - what we are, how an event resolves, where your money sits, the numbers, people (LATER), then the closing action.

### C. Ready SEO body text

The one paragraph that must ship in the text, on Terms and on Privacy, is block B7 - the money answer, lifted above the contents:

> **Your USDC is held 1:1 and we never lend it.** It sits in a segregated on-chain balance you can verify at any time; it is not lent, staked or used as working capital. Every event resolves against a named public source, and the resolution is recorded on-chain. [How resolution works](/how-it-works)

On About, the equivalent is the resolution paragraph (B16), which names who resolves, against which public source, and the resolved count. Both are the site-wide trust line from the footer strip, said once at length in the one place a person came looking for it.

### D. Structured data

- `WebPage` for all five, with `dateModified` bound to the same value block B4 renders. One date, two consumers: if the page shows a date the schema does not, the schema is wrong, and it is the schema a search result quotes.
- `BreadcrumbList` for the four legal pages: `Home > Legal > {document}` (block B2). About sits at `Home > About`.
- `Organization` on About only, with `name`, `url`, `logo`, `sameAs` (the social profiles the footer already lists) and `contactPoint` pointing at the Contact node.
- **No `FAQPage`**, even though block B6 writes section titles as questions. The question form is a voice decision for a human reader; marking it up as an FAQ would claim a rich result for text that is not a FAQ, and a trust product does not open with a schema it cannot defend.

### E. Optimization checklist

- Exactly one `H1`; no skipped heading level; the H2 list and the on-page contents are the same list.
- Every H2 carries a stable `id`, and the anchors are part of the internal-linking plane: the cookie banner links straight to the Cookie Policy section it is about.
- The sibling block (B9) gives all five pages a crawlable path to each other. Today they are reachable only from the footer, which is the second linking plane and not the first.
- Crawlable `<a>` throughout; the contents on mobile collapses but stays in the DOM, the same rule the footer columns already follow.
- Text is never in an image. **Named explicitly for this type**: the live crawl found the largest competitor serving its entire Terms of Use inside a `docs.google.com` iframe, which is the same defect in a different costume - the content is not in the page, so it is not indexed, not themeable and not searchable.
- `dateModified` in the schema equals the date rendered on the page.
- LCP is the H1 block; there is no hero image on the DOCUMENT profile to compete with it.
- Core Web Vitals budget as §1. This type is the lightest page in the product and should measure as such.

---

## Global: Footer - internal-linking and trust surface

- Node: Footer - Type: global component (on every page) - not indexed itself; its value is the second internal-linking plane plus a repeated trust signal
- No H1 (a global component never owns the page H1); rendered in a `<footer>` landmark

The footer is the one place this reconcile adds a structural node rather than a per-page SEO
block, because it is a site-wide SEO surface. Structure (adapting the existing wireframe footer):

- **Trust strip** (a thin band above the footer, on every page): the funds-safety line
  repeated site-wide - "USDC held 1:1, we never lend it" - next to "Transparent resolution" and
  the resolved-events count. This is the voice "trust before the ask" principle made persistent.
- **Link columns** (all crawlable `<a>`):
  - Product: Browse events, How it works, the four categories (Politics, Crypto, Culture, General)
  - Company and legal: About, Terms, Privacy, Responsible betting, Cookie preferences (opens the consent banner, see `system.md`)
  - Support: Help / FAQ (`[?]` orphan, post-MVP), Contact
- **SEO popular-links block:** a crawlable `<a>` list to priority pages - the categories, trending or ending-soon events, and How it works. The block structure is fixed now; the exact link list is keyword-research-driven `[?]` and finalized in production.
- **Bottom row:** copyright, the geo-restriction note (no US real-money markets), USDC / chain badge where appropriate, social links `[?]`.

### SEO / a11y

- Every footer link is a real crawlable `<a>` (the second internal-linking plane); never a JS-only handler.
- Global component, no H1; `<footer>` semantic plus `nav` landmarks; tap targets >= 44px.
- Mobile: the link columns and the SEO block collapse into accordions, but stay in the DOM (collapsed, still crawled).
- **Register every destination the footer promises** (About, Terms, Privacy, Responsible betting, Cookie preferences, Contact) as a node in `sitemap.md`, so the map and the footer do not diverge. This is a Step 7 reconcile item.

Wireframe delta: `event-feed.html` already has `<footer class="app-footer">` with brand,
tagline, link columns and a legal row. Missing vs this spec: the trust strip above the footer
and the SEO popular-links block. Both are small additions, logged here for the wireframe.
