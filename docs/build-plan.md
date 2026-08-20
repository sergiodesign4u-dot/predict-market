# Build plan - v1

**This file is not loaded into a session.** `PRODUCT.md` says what the product is,
`docs/launch-catalog.md` says which seven markets the first release opens with, and this says how the
thing gets built and in what order. Written 2026-08-20, closing `docs/backlog.md` 218.

**It is a build plan and not more design.** Every screen, every string and every component this needs
already exists: 116 painted screens, 116 grey, 49 components in one stylesheet, every string in
`voice/docs/microcopy.md`, every entity in `ia/docs/sitemap.md`. **Nothing here asks for a new
drawing.** If a question turns out to need one, it stops and goes through the pipeline in order,
`ia/` then `wireframes/` then `ui-visual/`, the way `docs/decisions.md` records for the multi
outcome screens.

**Done means:** a stranger opens a URL on a phone, reads seven live markets, signs in with Google,
places a bet in points, comes back when it resolves, and can check the reading that decided it.

---

## 1. The stack, and what it costs

| layer | choice | why this one | cost |
|---|---|---|---|
| markup and styles | **the tree as it stands** | `ui-visual/` is semantic HTML linking exactly one stylesheet. It is not a prototype to be redrawn, it is the output | 0 |
| renderer | **Astro** | an `.astro` file is HTML with a fenced script on top, so the existing markup pastes in and the loops go around it. It imposes no client framework, which matters because this system's whole discipline is one stylesheet and no per-screen CSS. The inline per-screen scripts are vanilla and survive | 0 |
| data, auth, jobs | **Supabase** | Postgres, Google and X sign-in, which are the two `PRODUCT.md` names, row-level security so a reader can only read their own bets, `pg_cron` plus an Edge Function for the resolver | 0, then **$25/mo** when the database must stop pausing |
| hosting | **Cloudflare Pages** or Vercel | static output plus a few server routes | 0 |
| domain | one | | ~$12/yr |

**$0 a month to start and $25 when it has to stay awake.** That is the whole capital requirement,
because the currency is points: `PRODUCT.md`, Liquidity and risk.

**Two constraints disappear the moment this is served rather than opened from disk**, and both cost
this repository real days: `file://` gives every document its own opaque origin, so the icon sprite
had to be a script and fonts had to be watched, and the theme had to boot from `localStorage` before
first paint. On a server the sprite can be a fetched SVG and the theme can be a cookie read on the
server. **Neither is a reason to change anything now**; they are savings to collect later, and the
current arrangement works on both.

**Not chosen, with reasons.** Next.js: more machinery than six routes need, and its idioms pull
towards CSS-in-JS, which this system refuses. A component framework of any kind: the components are
already CSS classes, and wrapping them in React would create a second component system whose
boundaries disagree with `components/`. A headless CMS: seven markets and one operator.

## 2. 116 documents are 6 routes, and that is the point

A static tree needs a document per combination of category, auth state and load state. A running app
gets all three from data. **This is where the apparent size of the build collapses.**

| route | painted documents it covers | what varies |
|---|---|---|
| `/` feed | **44** | 5 categories, signed in or out, success / empty / error / loading, search open |
| `/e/[slug]` event | **14** | binary or multi, open or settled, the bet panel's five states, signed out |
| `/bets` my bets | **9** | active or history tab, empty / error / loading |
| `/me` profile | **3** | loading, error |
| `/wallet` balance | **3** | loading, error |
| **`/admin`** | **0** | new, and the only thing in v1 with no drawing |
| sign-in | 4 | a dialog over whatever route you were on, not a route |
| win / loss | 7 | an overlay reached from `/bets` or a notification, not a route |

**91 of the 116 painted documents live inside those routes.** The remaining 25 are the static
content pages, the system pages and families v1 does not open: deposit (7, no money), notifications
(5), favorites (4), public profile (4), and the five documents plus 404 / 500 / maintenance /
cookie / toasts.

**The admin is the one surface with no drawing, and it does not get one from these trees.** Its
reader is the operator, not Alex, which is why `ia/docs/sitemap.md` registers it in Under Question as
explicitly not a node of that map. It is three lists and two buttons: markets needing review,
generated markets awaiting approval, and a resolve-by-hand form. It may look like a table with no
brand on it and that is correct.

## 3. The data model

Mirrors `ia/docs/sitemap.md` exactly, because the IA owns the model. Names are the IA's names.

```
user          id, provider, handle, display_name, avatar_url, created_at
              (Google or X only. No email/password, no wallet, no KYC in v1)

event         id, slug, question, category, subcat, type (binary|multi),
              frequency, series_id, image, closes_at,
              status (active|closed|resolved|needs_review|cancelled),
              b            -- the liquidity parameter, per market
              resolver     -- jsonb: {source, query, test} or {"source":"manual"}
              rules_text, context_text          -- the reader's half

option        id, event_id, name, position       -- multi only; binary has two implicit sides

quote         event_id, option_id, price, at     -- append-only. The number on screen
                                                 -- is the latest row; the chart is all of them

bet           id, user_id, event_id, option_id, side (yes|no),
              stake, price, shares, placed_at,
              idempotency_key UNIQUE             -- a double-tapped Confirm is one bet
              -- shares = stake / price, exactly, which is what 18 documents already print

resolution    event_id PK, outcome, outcome_option_id,
              reading jsonb   -- {endpoint, raw, value, threshold, read_at}
              resolved_by, evidence_url, note, closed_at, read_at

ledger        id, user_id, delta, reason (grant|stake|payout|refund), ref_id, at
              -- double entry from day one even though the currency is points,
              -- because a balance computed from a sum is a balance that can be audited
              -- and a balance stored in a column is a balance that drifts
```

**Three rules the schema enforces rather than the code.** `bet.idempotency_key` is unique.
`ledger` is append-only and the balance is `sum(delta)`, never a stored column. `resolution` is one
row per event, so a market cannot resolve twice.

## 4. The pricing module

One file, and it is small. `PRODUCT.md`, Liquidity and risk, is the specification.

- **Quote.** The current price is the latest `quote` row. The screen prints it.
- **Fill at the quote.** `shares = stake / price`, exactly, which is what the trees print on 18
  documents and what `The price is locked when you confirm` promises.
- **Move the quote after the fill**, by the scoring rule, `b` per market. The curve decides where the
  quote goes next; it does not price the bet in front of you.
- **`b` starts small and rises with flow.** Three $5 bets one way move a market to 63 per cent at
  `b = $50` and to 50.7 at `b = $1,000`, so a large `b` makes the number the opening quote wearing a
  crowd's clothes. Under points the subsidy is a row in a table, which is the whole reason this can
  be learned from live flow instead of guessed.
- **The reconcile (S5) is a comparison, not a lock.** Confirm sends the price the reader saw; if the
  latest quote differs, the server returns the new one and the screen shows it before committing.
  `event-detail-bet-reconcile.html` is already drawn.

## 5. The resolver job

`pg_cron` every five minutes, one Edge Function. Three transitions and one rule.

1. `closes_at` passed and status `active` -> **`closed`**. Trading stops. The outcome is usually not
   readable yet, which is why this state exists.
2. status `closed` and a resolver that answers -> **`resolved`**, write `resolution.reading` with the
   raw response, settle every bet through `ledger`.
3. resolver errors, times out or answers ambiguously -> **`needs_review`**, appears in `/admin`.

> **Silence is never read as NO.** A failed read routes to a human, never to an outcome. A market
> that resolves because nothing answered is the cheapest possible way to lose the one thing
> `PRODUCT.md` names as the #1 churn driver.

**The generator is the same job on a different schedule.** For each template: read the source, solve
the threshold for a 50 per cent open (`K = S x exp(-o^2 T / 2)`), create the next instance, open it.
`docs/launch-catalog.md` rows 1 to 4.

## 6. Order of work

Each phase ends with something a person can open. Weeks are evenings, not full days.

| # | phase | ends when | ~weeks |
|---|---|---|---|
| 1 | **Shell**: Astro project, `components/index.css` imported once, the feed rendered from a hand-written JSON of the seven | the feed is live at a URL and looks exactly like `ui-visual/event-feed.html` | 1 |
| 2 | **Data**: Supabase, the schema above, the feed and the event page reading from Postgres | changing a row changes the page | 1 to 2 |
| 3 | **Identity**: Google and X sign-in, a points grant on first sign-in, the balance | you can sign in and see a balance | 1 |
| 4 | **The bet**: quote, fill, ledger, idempotency, the reconcile, `/bets` | you can place a bet and see it | 2 |
| 5 | **Resolution**: the cron, the three states, settlement, the reading on the outcome screen, `/admin` | a market closes and pays out with nobody watching | 2 |
| 6 | **The seven live**: the four templates, the generator, real sources | the catalog runs itself for a week without you | 1 to 2 |
| 7 | **Open it**: one small community, and watch | strangers return after a resolution | - |

**8 to 10 weeks of evenings**, and phase 5 is the one that decides whether this is a product or a
demo, because it is the only phase whose output happens while nobody is looking.

## 7. What is not built, and each is a decision rather than an omission

- **Money.** No deposit, no withdrawal, no fiat rail, no KYC, no chain, no wallet. The currency is
  points, `PRODUCT.md` Liquidity and risk, and this is what makes the mechanism free.
- **Commission.** 0 while the currency is points: a fee on play money buys nothing and costs the
  trust line that says what the fee is for.
- **Notifications.** No push, no service worker. An email on resolution is the whole of it, and only
  after phase 5 proves resolutions happen on time.
- **Search.** 7 markets. `ia/docs/sitemap.md` deferred it below roughly 25 for exactly this reason
  and the trees keep the three screens for when it returns.
- **Favorites, public profiles, comments, share cards, the leaderboard.** All drawn, none opened.
- **The 25-market catalog.** `docs/launch-catalog.md` opens 7 of them.

## 8. What will actually go wrong

- **A source changes its shape and the resolver reads garbage.** The `needs_review` state is the
  answer and it must be tested by breaking a resolver on purpose before launch. A resolver that has
  never failed in testing is a resolver whose failure path does not exist.
- **The first week has no bets, so every price is the opening quote.** That is not a bug and the
  copy must not pretend otherwise. It is the argument for a small `b`.
- **Points feel worthless and nobody comes back.** The honest test is phase 7 and the measure is
  whether strangers return AFTER a resolution, not how many sign up.
- **The operator stops.** One editorial market is the capacity statement in
  `docs/launch-catalog.md`, and it is the number to lower first if the week gets heavy.
