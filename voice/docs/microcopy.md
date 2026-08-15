# Microcopy inventory - Prediction Market Platform

> **What this is.** A full inventory of the product interface text pulled from every `wireframes/*.html` (99 pages), with the places where screens say the same thing differently marked. **Nothing is rewritten here** - this is the read-only source of truth we will edit from next. Bootstrapped from the wireframes by `wireframes/_generators/microcopy_extract.py` + `microcopy_build.py`; from here it is **hand-maintained** (re-running the bootstrap would overwrite manual edits). The wireframes stay the render surface.

Columns: **Zone** (where on the screen), **Type** (heading / button / field label / placeholder / state message / link), **Line** (the exact text), **Flag** (a marked issue - see the legend). Pure data values ($0.38, 320 shares, 2h ago), avatar initials and sample social content are excluded from the copy tables and collected under **User-written content** at the end (we do not touch those).

## Legend of flags

| Flag | Meaning |
|---|---|
| **same-thing / event vs market** | one object named two ways: *event* here, *market* there |
| **same-thing / bet vs position** | *bet(s)* here, *position(s)* there for the same object |
| **same-thing / Deposit vs Add funds** | the funding action is labelled both ways |
| **same-thing / Bookmark vs save vs Favorites** | one save action, three names |
| **same-thing / Log in vs Sign in** | the auth entry is labelled both ways |
| **same-action / go-to-events button varies** | one 'take me to the feed' action, many button labels |
| **same-action / place-bet button varies** | one 'place the bet' action, many button labels |
| **AI-cliche tone** | generic / bright filler such as 'Something went wrong' |
| **leftover spec-note (internal codes)** | a developer note (T1/T2/T3, S5, 'underlying screen dimmed') that leaked into the UI, not user copy |
| **placeholder** | unfinished text (logo placeholder, TBD, licensing line, Transak widget) |

## Consistency findings (roll-up of the marks)

Read-only summary of every marked issue, with the exact variants and where they
appear. Nothing here is a rewrite; it is the punch-list for the editing pass.

### A. Same thing, different names

1. **event vs market** - the core object. The product mostly says *event(s)*
   (bottom-nav "Events", "Find events", "No events match your filters", "new
   events in this category") but switches to *market(s)* in the footer
   ("Markets", "By category", "View all markets"), on Event Detail ("One-time
   market"), in the tabs ("Positions update as the market trades") and in the
   feed empty body ("There are no markets for this category..."). The **Event
   Feed empty state uses both in adjacent lines**: heading "No events match your
   filters" over body "There are no markets for this category and filter
   combination."
2. **bet vs position** - *My Bets* / *place a bet* / *Bet* everywhere, but
   *position(s)* in the My Bets error ("Couldn't load your positions"), the
   "Positions" tab and "Positions update as the market trades", and the bet
   panel "View your position".
3. **Deposit vs Add funds** - the same funding action is *Deposit* (avatar item
   "Wallet / Deposit", My Profile button, Wallet button) and *Add funds* (header
   "+" control, Deposit dialog heading + button, How It Works button, bet-panel
   "Add funds"); the field is "Amount to add".
4. **Bookmark vs save vs Favorites** - one save action, three words: *Favorites*
   (header icon, bottom-nav slot, screen title), *Bookmark* + *save event*
   (Event Detail control), and the IA entity name *Saved events*.
5. **Log in vs Sign in** - the logged-out header shows *Log in* (and *Sign up*),
   while the dialog and comment prompt say *Sign in* ("Sign in or create
   account", "Sign in to join the discussion").

### B. Same action, different button labels

6. **Go to the events feed** - one destination, at least eight labels:
   "See next events" (Win), "Browse events" (Loss / How It Works / Favorites
   empty), "Find events" (My Bets empty), "Find events to follow" (Notifications
   empty), "Go to events" (Public Profile not found), "Back to feed" (Deposit
   KYC error), "Back to your bets" (Loss), plus "Notify me of new events in this
   category" (Feed empty).
7. **Place the bet** - "Bet" (panel primary) vs "Confirm bet" (intent) vs
   "Confirm at new price (41%)" (reconcile) vs the heading "Place your bet" vs
   "Bet $3.00 instead".
8. *Already consistent (keep as the standard):* retry is uniformly **"Try
   again"** (Feed / My Bets / Wallet / bet panel), and load-error headings are
   uniformly **"Couldn't load ..."**.

### C. AI-cliche / bright tone

9. **"Something went wrong ..."** on the Event Feed error and the My Bets error
   is generic filler (the Wallet error avoids it: "We couldn't fetch your
   balance..."). Otherwise the tone is already restrained: **no exclamation
   marks, no emoji, no "Congratulations / Welcome / Oops" anywhere** in the
   product text; Win is "You were right" (deliberately no confetti), Loss is
   "Here's what happened." This is a good baseline to protect.

### D. Leftover placeholders and spec-notes (not user-facing copy)

10. **Placeholders:** footer "logo placeholder", "Tagline placeholder", the
    "TBD / post-MVP / dynamic" roadmap tags, the "[Regulatory / licensing line -
    placeholder, to be set...]" strip, "Copyright ... Sample wireframe content";
    Event Detail "thumbnail placeholder"; Deposit "Transak payment widget (card
    to USDC)"; Win "Share Card ... (image placeholder)".
11. **Spec-notes / internal codes that leaked into visible text:** "underlying
    screen dimmed: ..." (Win / Loss / overlays); bet-panel rationale ("on-chain
    error (T3): ...", "insufficient-balance: inline guard...", "S5 reconcile:
    ..."); the dialog notes ("Opens over the current page ... see reference
    pages ..."); and real messages that carry a parenthetical code -
    "Your card was declined (T2)", "KYC verification was rejected (T1)", "Your
    bet did not register on-chain (T3)", "We couldn't generate your Share Card
    (T11)". The codes must come out of the user-facing copy.

### E. User-written content (do not touch)

Event questions, outcome names, per-event editorial (why-this-price, arguments,
resolution notes), share-card text, comments, usernames and holdings. Listed in
full at the end of this file.


## Global chrome (shared on every screen)

Header, category nav, bottom nav, footer and the two shared dialogs (Sign in, Deposit) are byte-identical across pages, so they are listed once here rather than repeated per screen.

### Skip link

Added 2026-08-12 with the fix for WCAG 2.4.1. It is the FIRST focusable element in every screen that
has a header, 105 painted and 87 grey, and it is invisible until a keyboard reaches it, so it is the
one string in the product that a person only ever meets by pressing Tab.

| Zone | Type | Line | Flag |
|---|---|---|---|
| Skip link | Link | Skip to main content |  |

The line is the platform's own convention rather than this product's voice on purpose. `voice.md`
asks for plain, specific, human copy, and a skip link is the one control where a familiar phrase
beats a well-written one: a screen-reader user recognises it by its exact wording, and an inventive
version of it costs them the recognition without buying anything.

### Header

| Zone | Type | Line | Flag |
|---|---|---|---|
| Header | Icon button | Menu (reserved for future scaling) |  |
| Header | Button | Yonder |  |
| Header | Label | Portfolio |  |
| Header | Icon button | Swap balance (showing Portfolio) |  |
| Header | Icon button | Add funds | **same-thing / Deposit vs Add funds** |
| Header | Icon button | Favorites | **same-thing / Bookmark vs save vs Favorites** |
| Header | Label | Position resolved |  |
| Header | Label | US government shutdown before Mar 1 - YES won |  |
| Header | Label | Odds moved |  |
| Header | Label | Bitcoin above $150k - now 61% |  |
| Header | Label | Deadline approaching |  |
| Header | Label | Eurovision 2027 final closes in 24h |  |
| Header | Link | See all notifications |  |
| Header | Button | My Profile |  |
| Header | Button | My Bets | **same-thing / bet vs position** |
| Header | Button | Wallet / Deposit | **same-thing / Deposit vs Add funds** |
| Header | Button | How It Works |  |
| Header | Button | Logout |  |

### Category nav

| Zone | Type | Line | Flag |
|---|---|---|---|
| Category nav | Button | Trending |  |
| Category nav | Button | Politics |  |
| Category nav | Button | Crypto |  |
| Category nav | Button | Culture |  |
| Category nav | Button | General |  |

### Bottom nav

| Zone | Type | Line | Flag |
|---|---|---|---|
| Bottom nav | Label | Events |  |
| Bottom nav | Label | My Bets | **same-thing / bet vs position** |
| Bottom nav | Label | Favorites | **same-thing / Bookmark vs save vs Favorites** |
| Bottom nav | Label | Portfolio |  |

### Footer

| Zone | Type | Line | Flag |
|---|---|---|---|
| Footer | Label | logo placeholder | **placeholder** |
| Footer | Text | Tagline placeholder | **placeholder** |
| Footer | Label | TBD | **placeholder** |
| Footer | Label | English |  |
| Footer | Option | Spanish |  |
| Footer | Option | Portuguese |  |
| Footer | Option | German |  |
| Footer | Option | French |  |
| Footer | Heading | Markets |  |
| Footer | Field label | By category | **same-thing / event vs market** |
| Footer | Link | Politics |  |
| Footer | Link | Crypto |  |
| Footer | Link | Culture |  |
| Footer | Link | General |  |
| Footer | Link | Sports |  |
| Footer | Label | post-MVP | **placeholder** |
| Footer | Field label | By topic |  |
| Footer | Link | Trending topics |  |
| Footer | Label | dynamic | **placeholder** |
| Footer | Link | View all markets | **same-thing / event vs market** |
| Footer | Heading | Product |  |
| Footer | Link | How It Works |  |
| Footer | Link | Leaderboard |  |
| Footer | Link | Wallet |  |
| Footer | Link | My Bets | **same-thing / bet vs position** |
| Footer | Link | API / Developers |  |
| Footer | Link | Status |  |
| Footer | Heading | Support |  |
| Footer | Link | Help Center |  |
| Footer | Link | FAQ |  |
| Footer | Link | Contact |  |
| Footer | Heading | Company |  |
| Footer | Link | About |  |
| Footer | Link | Careers |  |
| Footer | Link | Press |  |
| Footer | Link | Brand |  |
| Footer | Link | Terms |  |
| Footer | Link | Privacy |  |
| Footer | Link | Responsible play |  |
| Footer | Link | Geo restrictions |  |
| Footer | Text | Prediction markets involve risk of loss. Not available in restricted regions. |  |
| Footer | Text | [Regulatory / licensing line - placeholder, to be set. No US real-money markets; geo-restrictions and KYC per regulatory requirements.] | **placeholder** |
| Footer | Text | Copyright (c) Yonder. Sample wireframe content. | **placeholder** |

### Sign-in dialog

| Zone | Type | Line | Flag |
|---|---|---|---|
| Sign-in dialog | Heading | Sign in or create account | **same-thing / Log in vs Sign in** |
| Sign-in dialog | Text | You are about to place a bet. Sign in or create an account to continue. No crypto wallet required. |  |
| Sign-in dialog | Button | Continue with Google |  |
| Sign-in dialog | Button | Continue with X |  |
| Sign-in dialog | Button | Continue with Apple |  |
| Sign-in dialog | Text | By continuing you agree to the |  |
| Sign-in dialog | Link | Terms |  |
| Sign-in dialog | Text | and |  |
| Sign-in dialog | Link | Privacy Policy |  |
| Sign-in dialog | Text | Opens over the current page; closing keeps you here. Error / loading / provider-conflict: see reference pages sign-in-*.html. | **leftover spec-note (internal codes)** |

### Deposit dialog

| Zone | Type | Line | Flag |
|---|---|---|---|
| Deposit dialog | Heading | Add funds | **same-thing / Deposit vs Add funds** |
| Deposit dialog | Field label | Amount to add | **same-thing / Deposit vs Add funds** |
| Deposit dialog | Text | Transak payment widget (card to USDC) | **placeholder** |
| Deposit dialog | Text | Your USDC is held 1:1 - we do not lend or invest deposited funds. |  |
| Deposit dialog | Text | Minimum deposit $10. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead. |  |
| Deposit dialog | Text | Opens over the current page after sign-in. States (card declined / KYC / widget fail / pending / minimum): see reference pages deposit-*.html. | **leftover spec-note (internal codes)** |

## Screens

### Event Feed

_9 state page(s): event-feed-empty.html, event-feed-error.html, event-feed-loading.html, event-feed-logged-out-empty.html, event-feed-logged-out-error.html, event-feed-logged-out-loading.html, event-feed-logged-out.html, event-feed-push-permission-missing.html, event-feed.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Trending |  |
| Main | Label | Show: | The label on the category sub-filter, added 2026-08-14. Its five chips say the SAME five words as the category navigation 100px above them, and the two do different things: that one ROUTES to a category page, this one NARROWS the list already on screen. `Show:` is what says which, and it is the shape the feed's other two filters have always had, `Sort:` and `How often:` |
| Main | Heading | Filters | Below DESK 640 only, and it is the SHEET's title rather than the button's label: the control that opens it is a mark with no text. It is `Filters` and not `Filter` because the sheet holds more than one, and not `Sort` because sort is one of them |
| Main | Label (hidden) | Show filters | The accessible name of the checkbox behind the mark. A `<label>` is not focusable and this one has no text, so the name has to sit on the control that is |
| Main | Button | Show results | Below DESK 640 only, the sheet's way out. `Show results` and not `Apply`: every radio in the sheet is live, so the list behind the scrim has already changed and `Apply` would name a step that does not exist |
| Main | Button | Reset | Below DESK 640 only, and it appears ONLY while a filter is off its default. It is the other half of the dot on the closed control: the dot says the list is not the default one, this is the way back |
| Main | Label (hidden) | Close filters | Below DESK 640 only. The accessible name of the cross in the sheet's head, which is a `<button>` and not a `<label>` since 2026-08-14: a label is correct for a pointer and is not a tab stop |
| Main | Label | Sort: |  |
| Main | Option | Volatile |  |
| Main | Option | New |  |
| Main | Option | Closing soon |  |
| Main | Option | Volume |  |
| Main | Option | 50-50 (most contested) |  |
| Main | Label | Reverse sort |  |
| Main | Label | How often: | **Renamed from `Frequency:` on 2026-08-14.** Voice principle 3: we use the words a news-follower already owns, and `frequency` is the vocabulary of whoever built the market. The Event attribute is still called Frequency in `PRODUCT.md` and `ia/docs/sitemap.md`: **the model keeps its word and the reader gets theirs** |
| Main | Option | Any | The default of `How often`, renamed from `All` the same day: `How often: All` is not a sentence and `How often: Any` is |
| Main | Option | One-time |  |
| Main | Option | Hourly |  |
| Main | Option | Daily |  |
| Main | Option | Weekly |  |
| Main | Option | Monthly |  |
| Main | Label | Category: |  |
| Main | Option | Politics |  |
| Main | Option | Crypto |  |
| Main | Option | Culture |  |
| Main | Option | General |  |
| Main | Text | No events match your filters | **same-thing / event vs market** |
| Main | Text | There are no markets for this category and filter combination right now. Try clearing the filters, or get notified when a new event shows up here. |  |
| Main | Button | Clear filters |  |
| Main | Button | Notify me of new events in this category | **same-thing / event vs market** |
| Main | Text | Couldn't load events | **same-thing / event vs market** |
| Main | Text | Something went wrong reaching the network. Check your connection and try again. | **AI-cliche tone** |
| Main | Button | Try again |  |
| Main | Label | thumbnail placeholder | **placeholder** |
| Main | Link | +1 more outcome | *added 2026-08-10, backlog 81* |
| Main | Link | +2 more outcomes | *added 2026-08-10, backlog 81. The multi-outcome card shows two rows of a longer field and said nothing about the rest. The count is the smallest the arithmetic forces: the remainder over the smallest percentage shown, rounded up. A card whose rows sum to 100 carries no such row.* |
| Main | Label | Volume: $84,200 |  |
| Main | Label | Closes: Mar 1, 2027 |  |
| Main | Icon button | Bookmark | **same-thing / Bookmark vs save vs Favorites** |
| Main | Label | Volume: $212,900 |  |
| Main | Label | Closes: Oct 1, 2026 |  |
| Main | Icon button | Bookmarked |  |
| Main | Label | Volume: $61,500 |  |
| Main | Label | Closes: May 15, 2027 |  |
| Main | Label | Volume: $147,650 |  |
| Main | Label | Closes: Nov 1, 2026 |  |
| Main | Label | Volume: $19,400 |  |
| Main | Label | Closes: Dec 31, 2026 |  |
| Main | Label | Volume: $58,700 |  |
| Main | Label | Closes: Jul 1, 2027 |  |
| Main | Label | Volume: $33,100 |  |
| Main | Label | Closes: Jan 1, 2028 |  |
| Main | Label | Volume: $26,300 |  |
| Main | Label | Closes: Apr 1, 2027 |  |
| Main | Label | Enable notifications to get live updates on the events you follow. |  |
| Main | Button | Enable notifications |  |
| Main | Button | Not now |  |

### Event Detail

_13 state page(s): event-detail-bet-error.html, event-detail-bet-insufficient.html, event-detail-bet-processing.html, event-detail-bet-reconcile.html, event-detail-error.html, event-detail-loading.html, event-detail-logged-out-error.html, event-detail-logged-out-loading.html, event-detail-logged-out-multi.html, event-detail-logged-out.html, event-detail-multi.html, event-detail-resolved.html, event-detail.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | thumbnail placeholder | **placeholder** |
| Main | Label | Politics · One-time market |  |
| Main | Heading | Price chart |  |
| Main | Label | 1d · 1w · 1m · all |  |
| Main | Label | YES 38% now |  |
| Main | Label | Volume |  |
| Main | Label | Liquidity |  |
| Main | Label | Closes |  |
| Main | Label | Mar 1, 2027 |  |
| Main | Label | Frequency |  |
| Main | Label | One-time |  |
| Main | Label | Bookmark | **same-thing / Bookmark vs save vs Favorites** |
| Main | Label | save event | **same-thing / Bookmark vs save vs Favorites** |
| Main | Heading | Why this price |  |
| Main | Text | YES is priced at 38%. Funding talks have stalled twice this quarter, but the last three deadlines were settled at the last minute. What is moving the number: |  |
| Main | Heading | For YES |  |
| Main | Text | Budget talks stalled in committee, no scheduled vote. |  |
| Main | Text | A bloc has committed to opposing the stopgap bill. |  |
| Main | Heading | For NO |  |
| Main | Text | Last three deadlines met with short-term funding. |  |
| Main | Text | Both parties signalled willingness to extend. |  |
| Main | Heading | Resolution conditions |  |
| Main | Label | Resolves YES |  |
| Main | Text | if a federal funding gap causes a shutdown beginning before 00:00 ET on March 1, 2027. |  |
| Main | Label | Resolves NO |  |
| Main | Text | if funding is in place through that date. |  |
| Main | Label | Source: |  |
| Main | Text | official US Office of Management and Budget notices. Resolved by the Yonder team. |  |
| Content tabs | Field label | Comments |  |
| Content tabs | Field label | Top Holders |  |
| Content tabs | Field label | Positions | **same-thing / bet vs position** |
| Content tabs | Field label | Activity |  |
| Content tabs | Label | 128 comments |  |
| Content tabs | Button | Newest |  |
| Content tabs | Button | Top |  |
| Content tabs | Button | Holders |  |
| Content tabs | Label | Add a comment... |  |
| Content tabs | Button | Post |  |
| Content tabs | Button | Reply |  |
| Content tabs | Heading | YES holders |  |
| Content tabs | Heading | NO holders |  |
| Content tabs | Text | Holder |  |
| Content tabs | Text | Side |  |
| Content tabs | Text | Shares |  |
| Content tabs | Text | Avg |  |
| Content tabs | Text | Value |  |
| Content tabs | Text | You |  |
| Content tabs | Text | Your row is highlighted. Positions update as the market trades. |  |
| Content tabs | Text | Recent trades, largest first. Filter: over $5. |  |
| Bet panel | Heading | Place your bet | **same-action / place-bet button varies** |
| Bet panel | Label | execute failed |  |
| Bet panel | Field label | Amount |  |
| Bet panel | Text | Your bet did not register on-chain (T3). No funds were taken. | **leftover spec-note (internal codes)** |
| Bet panel | Button | Try again |  |
| Bet panel | Button | Check wallet |  |
| Bet panel | Text | on-chain error (T3): retry the execute step, or check your wallet balance. | **leftover spec-note (internal codes)** |
| Bet panel | Label | $5 to win |  |
| Bet panel | Button | Bet | **same-action / place-bet button varies** |
| Bet panel | Label | amount over balance |  |
| Bet panel | Text | You have $3.00. You can bet up to $3.00, or add funds to bet more. |  |
| Bet panel | Button | Add funds | **same-thing / Deposit vs Add funds** |
| Bet panel | Button | Bet $3.00 instead | **same-action / place-bet button varies** |
| Bet panel | Text | insufficient-balance: inline guard in the panel before the gate fires. | **leftover spec-note (internal codes)** |
| Bet panel | Label | submitting |  |
| Bet panel | Text | Registering your bet on-chain... |  |
| Bet panel | Label | A few seconds. Keep this open. |  |
| Bet panel | Button | View your position (on success) |  |
| Bet panel | Text | execute on-chain processing: transitional. On success it lands on Active Bets (T14); on failure, the on-chain error state (T3). | **leftover spec-note (internal codes)** |
| Bet panel | Label | price changed |  |
| Bet panel | Label | The price moved while you signed in |  |
| Bet panel | Label | Was 38% -> Now 41%. Payout $13.20 -> $12.20 for $5. |  |
| Bet panel | Button | Confirm at new price (41%) | **same-action / place-bet button varies** |
| Bet panel | Button | Cancel and re-evaluate |  |
| Bet panel | Text | S5 reconcile: shown after the Sign In / Deposit gate, before execute. Confirm goes to execute; cancel re-evaluates the event (T16). | **leftover spec-note (internal codes)** |
| Main | Heading | Couldn't load this event |  |
| Main | Text | Something went wrong while loading the event details. Check your connection and try again. |  |
| Main | Button | Try again |  |
| Main | Button | Back to feed | **same-action / go-to-events button varies** |
| Main | Text | loading chart... |  |
| Main | Label | Politics · One-time market · 5 outcomes |  |
| Main | Text | Leading: JD Vance |  |
| Main | Heading | Outcomes |  |
| Main | Label | selected |  |
| Main | Label | Other |  |
| Main | Text | Tap YES or NO on an outcome to load it into the bet panel. The panel stays focused on the one you picked, however long this list gets. |  |
| Main | Label | JD Vance 41% now |  |
| Main | Label | Jul 1, 2028 |  |
| Main | Text | JD Vance leads at 41% as the incumbent-aligned candidate, with Trump-endorsed momentum the main swing factor. What is moving the field: |  |
| Main | Heading | For the leader (Vance) |  |
| Main | Text | Strong early-state polling and party-establishment backing. |  |
| Main | Text | Front-runner fundraising lead over the rest of the field. |  |
| Main | Heading | Against / for the field |  |
| Main | Text | A late entrant could consolidate the anti-front-runner vote. |  |
| Main | Text | Early primaries historically reshuffle the order. |  |
| Main | Label | Resolves to the candidate |  |
| Main | Text | who is the Republican Party's official presidential nominee at the 2028 national convention. All other outcomes resolve NO. |  |
| Main | Text | official Republican National Committee certification. Resolved by the Yonder team. |  |
| Content tabs | Button | Sign in to join the discussion | **same-thing / Log in vs Sign in** |
| Content tabs | Text | Outcome |  |
| Bet panel | Label | YES pre-selected |  |
| Bet panel | Field label | Your outcome |  |
| Bet panel | Link | Change |  |
| Bet panel | Label | Price now |  |
| Bet panel | Label | Fee (1.5% of your bet) |  |
| Bet panel | Label | Potential payout |  |
| Bet panel | Label | Your balance |  |
| Bet panel | Button | Confirm bet | **same-action / place-bet button varies** |
| Bet panel | Text | $1 minimum, no maximum. The price you see is the price you get. Confirm opens sign-in (over this page), then deposit if needed. | Rewritten 2026-08-10 with the product decisions in `docs/backlog.md` 7 and 10: the minimum is $1, and the payout is shares at a locked price rather than a rule that depends on timing, so the sentence says what a person can check. |
| Bet panel | Button | JD Vance YES |  |
| Main | Heading | This event just resolved |  |
| Main | Text | The market closed while you were reading (event-closed). Betting is no longer available. You hold a position, so you can open your result. |  |
| Main | Button | See your position |  |
| Main | Label | Politics · One-time market · Trading closed |  |
| Main | Label | YES 38% at close |  |

### Category Page

_32 state page(s): event-feed-crypto-empty.html, event-feed-crypto-error.html, event-feed-crypto-loading.html, event-feed-crypto-logged-out-empty.html, event-feed-crypto-logged-out-error.html, event-feed-crypto-logged-out-loading.html, event-feed-crypto-logged-out.html, event-feed-crypto.html, event-feed-culture-empty.html, event-feed-culture-error.html, event-feed-culture-loading.html, event-feed-culture-logged-out-empty.html, event-feed-culture-logged-out-error.html, event-feed-culture-logged-out-loading.html, event-feed-culture-logged-out.html, event-feed-culture.html, event-feed-general-empty.html, event-feed-general-error.html, event-feed-general-loading.html, event-feed-general-logged-out-empty.html, event-feed-general-logged-out-error.html, event-feed-general-logged-out-loading.html, event-feed-general-logged-out.html, event-feed-general.html, event-feed-politics-empty.html, event-feed-politics-error.html, event-feed-politics-loading.html, event-feed-politics-logged-out-empty.html, event-feed-politics-logged-out-error.html, event-feed-politics-logged-out-loading.html, event-feed-politics-logged-out.html, event-feed-politics.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Text | Sub-categories |  |
| Main | Button | All |  |
| Main | Label | 2K |  |
| Main | Button | Bitcoin |  |
| Main | Button | Ethereum |  |
| Main | Button | Solana |  |
| Main | Button | Price Predictions |  |
| Main | Button | ETFs |  |
| Main | Button | Stablecoins |  |
| Main | Button | Memecoins |  |
| Main | Button | Layer 2s |  |
| Main | Button | Fed & Macro |  |
| Main | Heading | Crypto |  |
| Main | Heading | Filters | Below DESK 640 only, and it is the SHEET's title rather than the button's label: the control that opens it is a mark with no text. It is `Filters` and not `Filter` because the sheet holds more than one, and not `Sort` because sort is one of them |
| Main | Label (hidden) | Show filters | The accessible name of the checkbox behind the mark. A `<label>` is not focusable and this one has no text, so the name has to sit on the control that is |
| Main | Button | Show results | Below DESK 640 only, the sheet's way out. `Show results` and not `Apply`: every radio in the sheet is live, so the list behind the scrim has already changed and `Apply` would name a step that does not exist |
| Main | Button | Reset | Below DESK 640 only, and it appears ONLY while a filter is off its default. It is the other half of the dot on the closed control: the dot says the list is not the default one, this is the way back |
| Main | Label (hidden) | Close filters | Below DESK 640 only. The accessible name of the cross in the sheet's head, which is a `<button>` and not a `<label>` since 2026-08-14: a label is correct for a pointer and is not a tab stop |
| Main | Label | Sort: |  |
| Main | Label | Trending |  |
| Main | Option | Volatile |  |
| Main | Option | New |  |
| Main | Option | Closing soon |  |
| Main | Option | Volume |  |
| Main | Option | 50-50 (most contested) |  |
| Main | Label | Reverse sort |  |
| Main | Label | How often: | **Renamed from `Frequency:` on 2026-08-14.** Voice principle 3: we use the words a news-follower already owns, and `frequency` is the vocabulary of whoever built the market. The Event attribute is still called Frequency in `PRODUCT.md` and `ia/docs/sitemap.md`: **the model keeps its word and the reader gets theirs** |
| Main | Option | One-time |  |
| Main | Option | Hourly |  |
| Main | Option | Daily |  |
| Main | Option | Weekly |  |
| Main | Option | Monthly |  |
| Main | Heading | No events match these filters |  |
| Main | Text | No Crypto markets match the current sub-category and filters. Clear the filters, or get notified when new ones open. |  |
| Main | Button | Clear filters |  |
| Main | Button | Notify me of new Crypto events |  |
| Main | Heading | Couldn't load Crypto |  |
| Main | Text | Something went wrong while loading these markets. Check your connection and try again. |  |
| Main | Button | Try again |  |
| Main | Button | Back to Trending |  |
| Main | Label | thumbnail placeholder | **placeholder** |
| Main | Label | Volume: $212,900 |  |
| Main | Label | Closes: Oct 1, 2026 |  |
| Main | Icon button | Bookmarked |  |
| Main | Label | Volume: $147,650 |  |
| Main | Label | Closes: Nov 1, 2026 |  |
| Main | Icon button | Bookmark | **same-thing / Bookmark vs save vs Favorites** |
| Main | Label | Volume: $540,000 |  |
| Main | Label | Closes: Jan 1, 2027 |  |
| Main | Label | Volume: $61,200 |  |
| Main | Label | Closes: Jul 1, 2027 |  |
| Main | Label | Volume: $30,100 |  |
| Main | Label | Volume: $18,400 |  |
| Main | Label | 1.4K |  |
| Main | Button | Movies |  |
| Main | Button | Music |  |
| Main | Button | Awards |  |
| Main | Button | TV & Streaming |  |
| Main | Button | Celebrities |  |
| Main | Button | Internet & Memes |  |
| Main | Button | Books |  |
| Main | Button | Gaming |  |
| Main | Heading | Culture |  |
| Main | Text | No Culture markets match the current sub-category and filters. Clear the filters, or get notified when new ones open. |  |
| Main | Button | Notify me of new Culture events |  |
| Main | Heading | Couldn't load Culture |  |
| Main | Label | Volume: $19,400 |  |
| Main | Label | Closes: Dec 31, 2026 |  |
| Main | Label | Taylor Swift |  |
| Main | Label | Kendrick Lamar |  |
| Main | Label | Volume: $44,500 |  |
| Main | Label | Closes: Feb 1, 2027 |  |
| Main | Label | Volume: $27,800 |  |
| Main | Label | Volume: $15,900 |  |
| Main | Label | Volume: $61,500 |  |
| Main | Label | Closes: May 15, 2027 |  |
| Main | Label | Volume: $12,300 |  |
| Main | Label | 1.1K |  |
| Main | Button | Science & Tech |  |
| Main | Button | Climate |  |
| Main | Button | Space |  |
| Main | Button | AI |  |
| Main | Button | Health |  |
| Main | Button | Business |  |
| Main | Button | World |  |
| Main | Heading | General |  |
| Main | Text | No General markets match the current sub-category and filters. Clear the filters, or get notified when new ones open. |  |
| Main | Button | Notify me of new General events |  |
| Main | Heading | Couldn't load General |  |
| Main | Label | Volume: $26,300 |  |
| Main | Label | Closes: Apr 1, 2027 |  |
| Main | Label | Volume: $48,700 |  |
| Main | Label | Closes: Jan 1, 2028 |  |
| Main | Label | Nvidia |  |
| Main | Label | Apple |  |
| Main | Label | Volume: $210,000 |  |
| Main | Label | Volume: $33,400 |  |
| Main | Label | Volume: $33,100 |  |
| Main | Label | Volume: $22,600 |  |
| Main | Button | Trump |  |
| Main | Button | Trump Daily |  |
| Main | Button | Midterm Elections |  |
| Main | Button | Global Elections |  |
| Main | Button | Primaries |  |
| Main | Button | Congress |  |
| Main | Button | Trump Cabinet |  |
| Main | Button | Courts |  |
| Main | Button | Epstein |  |
| Main | Button | Government Shutdown |  |
| Main | Button | LA Mayor |  |
| Main | Heading | Politics |  |
| Main | Text | No Politics markets match the current sub-category and filters. Clear the filters, or get notified when new ones open. |  |
| Main | Button | Notify me of new Politics events |  |
| Main | Heading | Couldn't load Politics |  |
| Main | Label | Volume: $84,200 |  |
| Main | Label | Closes: Mar 1, 2027 |  |
| Main | Label | Volume: $410,000 |  |
| Main | Label | Closes: Nov 3, 2026 |  |
| Main | Label | Volume: $1,200,000 |  |
| Main | Label | Closes: Jul 1, 2028 |  |
| Main | Label | Volume: $96,500 |  |
| Main | Label | Volume: $52,300 |  |
| Main | Label | Volume: $73,800 |  |

### My Bets

_9 state page(s): active-bets-empty-new.html, active-bets-empty-resolved.html, active-bets-error.html, active-bets-history-empty.html, active-bets-history-error.html, active-bets-history-loading.html, active-bets-history.html, active-bets-loading.html, active-bets.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | My Bets | **same-thing / bet vs position** |
| Main | Button | Active |  |
| Main | Button | History |  |
| Main | Heading | No active bets yet | **same-thing / bet vs position** |
| Main | Text | You haven't placed any bets. Find an event you have an opinion on and put a real stake on the outcome. |  |
| Main | Button | Find events | **same-action / go-to-events button varies** |
| Main | Heading | All your positions are closed |  |
| Main | Text | You have no open bets right now. Your settled bets are in the History tab. |  |
| Main | Button | See resolved bets (History tab) |  |
| Main | Button | Find new events |  |
| Main | Heading | Couldn't load your positions | **same-thing / bet vs position** |
| Main | Text | Something went wrong while loading your bets. Check your connection and try again. | **AI-cliche tone**, **same-thing / bet vs position** |
| Main | Button | Try again |  |
| Main | Heading | No resolved bets yet |  |
| Main | Text | Your settled bets will appear here once the events you bet on resolve. None of yours have resolved yet. |  |
| Main | Heading | Couldn't load your history |  |
| Main | Text | Something went wrong while loading your resolved bets. Check your connection and try again. |  |
| Main | Label | WON |  |
| Main | Label | Stake |  |
| Main | Label | Payout |  |
| Main | Label | +$13.20 |  |
| Main | Label | Your side |  |
| Main | Label | Result |  |
| Main | Label | Resolved Jun 27 · tap to see your win |  |
| Main | Label | +$31.80 |  |
| Main | Label | Resolved Jun 20 · tap to see your win |  |
| Main | Label | Spot ETH ETF approved in H1 2027? |  |
| Main | Label | LOST |  |
| Main | Label | -$5.00 |  |
| Main | Label | Resolved Jun 12 · tap to see what happened |  |
| Main | Label | +$21.10 |  |
| Main | Label | NO · Conservatives |  |
| Main | Label | Resolved Jun 2 · tap to see your win |  |
| Main | Label | Current value |  |
| Main | Label | Potential payout |  |
| Main | Label | Avg price |  |
| Main | Label | Open · just placed |  |
| Main | Label | Open |  |

### Favorites

_3 state page(s): favorites-empty.html, favorites-loading.html, favorites.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Favorites | **same-thing / Bookmark vs save vs Favorites** |
| Main | Heading | Filters | Below DESK 640 only, and it is the SHEET's title rather than the button's label: the control that opens it is a mark with no text. It is `Filters` and not `Filter` because the sheet holds more than one, and not `Sort` because sort is one of them |
| Main | Label (hidden) | Show filters | The accessible name of the checkbox behind the mark. A `<label>` is not focusable and this one has no text, so the name has to sit on the control that is |
| Main | Button | Show results | Below DESK 640 only, the sheet's way out. `Show results` and not `Apply`: every radio in the sheet is live, so the list behind the scrim has already changed and `Apply` would name a step that does not exist |
| Main | Button | Reset | Below DESK 640 only, and it appears ONLY while a filter is off its default. It is the other half of the dot on the closed control: the dot says the list is not the default one, this is the way back |
| Main | Label (hidden) | Close filters | Below DESK 640 only. The accessible name of the cross in the sheet's head, which is a `<button>` and not a `<label>` since 2026-08-14: a label is correct for a pointer and is not a tab stop |
| Main | Label | Sort: |  |
| Main | Label | Trending |  |
| Main | Option | Volatile |  |
| Main | Option | New |  |
| Main | Option | Closing soon |  |
| Main | Option | Volume |  |
| Main | Option | 50-50 (most contested) |  |
| Main | Label | Reverse sort |  |
| Main | Label | How often: | **Renamed from `Frequency:` on 2026-08-14.** Voice principle 3: we use the words a news-follower already owns, and `frequency` is the vocabulary of whoever built the market. The Event attribute is still called Frequency in `PRODUCT.md` and `ia/docs/sitemap.md`: **the model keeps its word and the reader gets theirs** |
| Main | Option | Any | The default of `How often`, renamed from `All` the same day: `How often: All` is not a sentence and `How often: Any` is |
| Main | Option | One-time |  |
| Main | Option | Hourly |  |
| Main | Option | Daily |  |
| Main | Option | Weekly |  |
| Main | Option | Monthly |  |
| Main | Label | Category: |  |
| Main | Option | Politics |  |
| Main | Option | Crypto |  |
| Main | Option | Culture |  |
| Main | Option | General |  |
| Main | Text | No favorites yet |  |
| Main | Text | You have not saved any events yet. Tap the bookmark on any event to keep it here for quick access. |  |
| Main | Button | Browse events | **same-action / go-to-events button varies** |
| Main | Label | thumbnail placeholder | **placeholder** |
| Main | Label | Volume: $84,200 |  |
| Main | Label | Closes: Mar 1, 2027 |  |
| Main | Icon button | Bookmark | **same-thing / Bookmark vs save vs Favorites** |
| Main | Label | Volume: $212,900 |  |
| Main | Label | Closes: Oct 1, 2026 |  |
| Main | Icon button | Bookmarked |  |
| Main | Label | Volume: $61,500 |  |
| Main | Label | Closes: May 15, 2027 |  |
| Main | Label | Volume: $147,650 |  |
| Main | Label | Closes: Nov 1, 2026 |  |
| Main | Label | Volume: $19,400 |  |
| Main | Label | Closes: Dec 31, 2026 |  |
| Main | Label | Volume: $58,700 |  |
| Main | Label | Closes: Jul 1, 2027 |  |
| Main | Label | Volume: $33,100 |  |
| Main | Label | Closes: Jan 1, 2028 |  |
| Main | Label | Volume: $26,300 |  |
| Main | Label | Closes: Apr 1, 2027 |  |

### Deposit

_7 state page(s): deposit-error-card.html, deposit-error-kyc.html, deposit-loading.html, deposit-minimum-not-met.html, deposit-pending.html, deposit-widget-load-failure.html, deposit.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Sign In / Register (just authenticated) | **leftover spec-note (internal codes)** |
| Main | Heading | Card declined |  |
| Main | Text | Your card was declined (T2). No funds were taken. Try another card, or connect a USDC wallet to skip cards entirely. | **leftover spec-note (internal codes)** |
| Main | Field label | Amount to add | **same-thing / Deposit vs Add funds** |
| Main | Button | Try another card |  |
| Main | Button | Connect a USDC wallet instead |  |
| Main | Heading | Verification rejected |  |
| Main | Text | KYC verification was rejected (T1), so card deposits are not available on this account. You can still bet with crypto by connecting a USDC wallet (no KYC), or contact support. | **leftover spec-note (internal codes)** |
| Main | Button | Connect a USDC wallet (no KYC) |  |
| Main | Button | Contact support |  |
| Main | Button | Back to feed | **same-action / go-to-events button varies** |
| Main | Heading | Add funds | **same-thing / Deposit vs Add funds** |
| Main | Text | Loading Transak... |  |
| Main | Label | KYC may be requested inside the widget. This can take a moment. |  |
| Main | Text | Do not close this window while the payment widget loads. |  |
| Main | Text | Minimum deposit is $10. Enter $10 or more to continue. |  |
| Main | Text | Your USDC is held 1:1 - we do not lend or invest deposited funds. |  |
| Main | Heading | Payment pending |  |
| Main | Text | Payment under review |  |
| Main | Label | This usually takes under 5 minutes. We will notify you when your funds are ready. |  |
| Main | Button | Back to the event |  |
| Main | Button | Go to My Bets |  |
| Main | Heading | Payment didn't load |  |
| Main | Text | Payment widget failed to load. |  |
| Main | Label | The Transak iframe was blocked or the network dropped. |  |
| Main | Button | Open Transak directly |  |
| Main | Text | Fallback per S3: route around the embedded widget when it cannot load. |  |
| Main | Field label | Pay with |  |
| Main | Text | Transak payment widget (card to USDC) | **placeholder** |
| Main | Text | Minimum deposit $10. Card payments are converted to USDC via Transak. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead. |  |
| Main | Button | How it works | **The parenthetical `(what happens to my money)` was dropped on 2026-08-14**, for two reasons that agree. It broke the button onto two lines at 320 and 360, on 105 screens. And the header's own control has said plain `How it works` all along, so **one destination had two names**, 105 placements each, which is the `same-action / label varies` flag this file already carries for the go-to-events button. The promise it made is kept two lines above it by the `.protect` sentence, *Your USDC is held 1:1 - we do not lend or invest your funds*, which is voice principle 2 and is the answer to the question the bracket was asking |

### Sign In / Register

_4 state page(s): sign-in-error.html, sign-in-loading.html, sign-in-provider-conflict.html, sign-in.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Event Detail (Confirm in the bet panel) | **leftover spec-note (internal codes)** |
| Main | Heading | Sign in or create account | **same-thing / Log in vs Sign in** |
| Main | Text | Sign-in failed. The provider did not complete authentication. You can try again or use a different provider. |  |
| Main | Button | Continue with Google |  |
| Main | Button | Continue with X |  |
| Main | Button | Continue with Apple |  |
| Main | Text | No crypto wallet required. By continuing you agree to the |  |
| Main | Link | Terms |  |
| Main | Text | and |  |
| Main | Link | Privacy Policy |  |
| Main | Text | . Deposits via card require KYC; crypto-only accounts can connect a wallet instead. |  |
| Main | Heading | Signing you in |  |
| Main | Text | Redirecting to Google to sign in... |  |
| Main | Label | Waiting for the provider. This window stays open. |  |
| Main | Button | Cancel and choose another provider |  |
| Main | Heading | Account already exists |  |
| Main | Text | This email is already registered with |  |
| Main | Label | X |  |
| Main | Text | . To keep one account, continue with X, or link Google to your existing account. |  |
| Main | Button | Continue with X | **The parenthetical `(your original provider)` was dropped on 2026-08-14.** It broke the button onto two lines at 360, and it said a second time what the error line directly above it already says: *This email is already registered with X.* A label that repeats the sentence over it is not context, it is the same sentence at a smaller size |
| Main | Button | Link Google to this account |  |
| Main | Text | You are about to place a bet. Sign in or create an account to continue. It takes a few seconds. |  |

### My Profile

_3 state page(s): my-profile-error.html, my-profile-loading.html, my-profile.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | My Profile |  |
| Main | Heading | Couldn't load your profile |  |
| Main | Text | Something went wrong while loading your track record. Try again. |  |
| Main | Button | Try again |  |
| Main | Text | Portfolio |  |
| Main | Label | Portfolio total |  |
| Main | Label | Cash (available) |  |
| Main | Label | In-play |  |
| Main | Button | Deposit | **same-thing / Deposit vs Add funds** |
| Main | Button | Open Wallet |  |
| Main | Label | avatar |  |
| Main | Label | alex_predicts |  |
| Main | Label | Your public track record |  |
| Main | Button | Edit name & avatar |  |
| Main | Text | Track record |  |
| Main | Label | Total bets |  |
| Main | Label | Win rate |  |
| Main | Label | Resolved |  |
| Main | Label | Member since |  |
| Main | Label | Win rate is % correct on resolved bets (public). Reputation = the track record, not the balance. |  |
| Main | Text | Share cards (past wins) |  |
| Main | Text | Win card: US shutdown YES +$13.20 |  |
| Main | Text | Win card: BTC > $150k YES +$6.80 |  |
| Main | Text | Win card: ETF approval NO +$9.40 |  |
| Main | Text | Resolved predictions (public) |  |
| Main | Label | US government shutdown before Mar 1, 2027 |  |
| Main | Label | WON |  |
| Main | Label | YES · resolved Jun 27 · +$13.20 |  |
| Main | Label | Bitcoin above $150,000 before Oct 1, 2026 |  |
| Main | Label | YES · resolved Jun 20 · +$6.80 |  |
| Main | Label | Spot ETH ETF approved in H1 2027 |  |
| Main | Label | LOST |  |
| Main | Label | NO · resolved Jun 12 · -$5.00 |  |
| Main | Label | Which party wins the most UK seats |  |
| Main | Label | NO · Conservatives · resolved Jun 2 · +$11.10 |  |

### Public Profile

_4 state page(s): public-profile-error.html, public-profile-loading.html, public-profile-not-found.html, public-profile.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Profile |  |
| Main | Heading | Couldn't load this profile |  |
| Main | Text | Something went wrong while loading this track record. Try again, or go back to events. |  |
| Main | Button | Try again |  |
| Main | Button | Back to events |  |
| Main | Heading | Profile not found |  |
| Main | Text | This profile no longer exists or the share link has expired. The track record may have been removed. |  |
| Main | Button | Go to events | **same-action / go-to-events button varies** |
| Main | Label | avatar |  |
| Main | Label | crypto_dan |  |
| Main | Label | Public track record · read-only |  |
| Main | Text | You opened this from a shared win card. This is a public, read-only track record - no balance or private data is shown. |  |
| Main | Text | Track record |  |
| Main | Label | Total bets |  |
| Main | Label | Win rate |  |
| Main | Label | Resolved |  |
| Main | Label | Member since |  |
| Main | Label | Win rate is % correct on resolved bets (public). Reputation = the track record, not the balance. |  |
| Main | Text | Share cards (past wins) |  |
| Main | Text | Win card: US shutdown YES +$13.20 |  |
| Main | Text | Win card: BTC > $150k YES +$6.80 |  |
| Main | Text | Win card: ETF approval NO +$9.40 |  |
| Main | Text | Resolved predictions (public) |  |
| Main | Label | US government shutdown before Mar 1, 2027 |  |
| Main | Label | WON |  |
| Main | Label | YES · resolved Jun 27 · +$13.20 |  |
| Main | Label | Bitcoin above $150,000 before Oct 1, 2026 |  |
| Main | Label | YES · resolved Jun 20 · +$6.80 |  |
| Main | Label | Spot ETH ETF approved in H1 2027 |  |
| Main | Label | LOST |  |
| Main | Label | NO · resolved Jun 12 · -$5.00 |  |
| Main | Label | Which party wins the most UK seats |  |
| Main | Label | NO · Conservatives · resolved Jun 2 · +$11.10 |  |

### Wallet

_3 state page(s): wallet-error.html, wallet-loading.html, wallet.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Wallet |  |
| Main | Heading | Couldn't load your wallet |  |
| Main | Text | We couldn't fetch your balance and transactions. Your funds are safe; this is a display issue. Try again. |  |
| Main | Button | Try again |  |
| Main | Label | Portfolio total |  |
| Main | Label | Cash (available) |  |
| Main | Label | In-play (open bets) |  |
| Main | Label | Portfolio = Cash + In-play. In-play is locked in open positions until they resolve. |  |
| Main | Button | Deposit | **same-thing / Deposit vs Add funds** |
| Main | Button | Withdraw |  |
| Main | summary | Withdraw funds (USDC) |  |
| Main | Field label | Amount to withdraw |  |
| Main | Label | Available to withdraw: $92.00 (Cash only; in-play funds are locked). |  |
| Main | Field label | Destination USDC address |  |
| Main | Label | 0x1A2b...9F3c |  |
| Main | Text | Withdrawals are in USDC only at MVP (no fiat payout rail). PIX payout is Phase 2 (Brazil). Network fee applies. |  |
| Main | Button | Confirm withdrawal |  |
| Main | Text | After confirm, the withdrawal moves through: pending (on-chain) -> confirmed, or failed (funds returned to Cash). Tracked in the history below. |  |
| Main | Text | Your USDC is held 1:1 - we do not lend or invest your funds. Deposits, payouts and withdrawals are recorded below. |  |
| Main | Text | Transaction history |  |
| Main | Label | Withdrawal to USDC address |  |
| Main | Label | -$30.00 |  |
| Main | Label | Jun 28 · pending (on-chain) |  |
| Main | Label | Payout: US government shutdown - YES won |  |
| Main | Label | +$13.20 |  |
| Main | Label | Jun 27 · completed |  |
| Main | Label | Platform fee (won bet) |  |
| Main | Label | -$0.40 |  |
| Main | Label | Stake: Bitcoin above $150,000 - YES |  |
| Main | Label | -$25.00 |  |
| Main | Label | Jun 26 · locked in-play |  |
| Main | Label | Deposit via card (Transak) |  |
| Main | Label | +$20.00 |  |
| Main | Label | Jun 26 · completed |  |

### Notifications

_5 state page(s): notifications-empty.html, notifications-error.html, notifications-loading.html, notifications-push.html, notifications.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Notifications |  |
| Main | Heading | No notifications yet |  |
| Main | Text | When an event you follow moves, approaches its deadline, or resolves, you'll see it here. Follow an event to start getting alerts. |  |
| Main | Button | Find events to follow | **same-action / go-to-events button varies** |
| Main | Heading | Couldn't load notifications |  |
| Main | Text | Something went wrong while loading your alerts. Check your connection and try again. |  |
| Main | Button | Try again |  |
| Main | Label | Push is off. Enable notifications to get live updates on the events you follow. |  |
| Main | Button | Open system settings |  |
| Main | Button | Not now |  |
| Main | Text | In-app notifications still work here. Enable system push so alerts reach you when the app is closed. |  |
| Main | Text | Unread |  |
| Main | Label | Your bet resolved: US government shutdown - YES won. Tap to see your win. |  |
| Main | Label | 2m |  |
| Main | Label | [unread] |  |
| Main | Label | Position resolved |  |
| Main | Label | Odds moved: "Bitcoin above $150,000" jumped from 58% to 64%. |  |
| Main | Label | 18m |  |
| Main | Label | Odds moved significantly |  |
| Main | Label | Closing soon: "Which party wins the most UK seats" closes in 6 hours. |  |
| Main | Label | 1h |  |
| Main | Label | Event deadline approaching |  |
| Main | Text | Earlier |  |
| Main | Label | New in Crypto: "Will ETH flip BTC by 2027?" is now live. |  |
| Main | Label | Yesterday |  |
| Main | Label | New event in a followed category |  |
| Main | Label | Your bet resolved: ETF approval - NO. Tap to see what happened. |  |
| Main | Label | 2d |  |

### How It Works, the dialog

_The stepper on all 105 painted screens. Rewritten 2026-08-14: it was two explainer sections plus a
FAQ plus a "Read the full guide" button, and it is three steps with a picture each and a way in at
the end. The dialog and the page stopped being one markup on purpose, and the sentence that says
where that is written is in `docs/decisions.md`. Every line below is in the dialog and nowhere else._

| Zone | Type | Line | Flag |
|---|---|---|---|
| Step 1 | Label | Step 1 of 3 |  |
| Step 1 | Heading | Pick an event you follow |  |
| Step 1 | Text | Every event asks one question, with a date and a named source. You see the odds, the one-line why and how it resolves before you put in a cent. |  |
| Step 1 | Button | Next |  |
| Step 2 | Label | Step 2 of 3 |  |
| Step 2 | Heading | Back YES or NO |  |
| Step 2 | Text | The odds are a live price set by what people bet. Your payout settles at the price you took, so being early and right is worth more. One dollar minimum. |  |
| Step 2 | Button | Next |  |
| Step 3 | Label | Step 3 of 3 |  |
| Step 3 | Heading | Get paid when it resolves |  |
| Step 3 | Text | It resolves against the source it named and the result is written on-chain. Until then your money is held 1:1, never lent and never moved. |  |
| Step 3 | Button | Create account | goes to `sign-in.html`, whose own heading is "Sign in or create account" |
| Step 3 | Link | Browse events first | the quiet way out, and it is the product's own stance: you can build a bet before you connect a wallet |
| Stage | Label | Step 1 / Step 2 / Step 3 | the accessible names of the three dots |
| Stage | Label | Step 1 of 3, pick an event | the radio's own name, one per step |

**Struck on 2026-08-14, and struck rather than moved, because the page still says all of it**:
"Back the events you follow, in plain language.", "How betting works here", "Why the odds move",
"Common questions", "Do I need crypto to start?", "What is the smallest bet?", "How does an event
resolve?" and "Read the full guide". The dialog's job is fifteen seconds and a way in; the page's is
the answer to a question the reader already has, and it is the only place the 1:1 sentence is
written out in full.

### How It Works

_1 state page(s): how-it-works.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | How It Works |  |
| Main | Text | You always know what you are doing, why, and what happens to your money. This is a promise, not a FAQ. |  |
| Main | Heading | Your money is held 1:1 |  |
| Main | Text | Your USDC is held 1:1. We never lend it, invest it, or move it. It is yours until you place a bet or withdraw - deposits, payouts and withdrawals are all recorded in your Wallet. |  |
| Main | Heading | How events resolve |  |
| Main | Text | Each event has clear resolution conditions, written before betting opens. When the event happens, the platform team resolves it against public evidence (official sources, on-chain data, named references). |  |
| Main | Text | Every resolution is recorded on-chain, so the outcome and the payout are verifiable and cannot be changed after the fact. |  |
| Main | Heading | How pricing and payouts work |  |
| Main | Text | Prices move with the market (AMM). Your payout depends on when you bet: earlier stakes at a better price earn more. The amount and potential payout are always shown before you confirm. |  |
| Main | Text | There is no subscription. The platform earns a small fee only when you win - never on a losing bet. |  |
| Main | Heading | Proven, not promised |  |
| Main | Label | Markets resolved |  |
| Main | Label | On-chain proofs |  |
| Main | Label | USDC held 1:1 |  |
| Main | Label | always |  |
| Main | Label | Resolved-market count as social proof (benchmark.md Top 3 trust mechanisms). |  |
| Main | Button | Browse events | **same-action / go-to-events button varies** |
| Main | Button | Add funds | **same-thing / Deposit vs Add funds** |
| Main | Text | Reachable before you deposit anything (from the menu and the footer) and from the Deposit dialog "learn more" link, so the answer to "what happens to my money" comes before the money does. |  |

### Win Screen

_4 state page(s): win-error.html, win-loading.html, win-payout-pending.html, win.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Active Bets (resolved item) or a tapped win notification | **leftover spec-note (internal codes)** |
| Main | Heading | You were right |  |
| Main | Field label | You were right - you won |  |
| Main | Label | +$13.20 |  |
| Main | Label | $5.00 stake returned + $8.20 winnings. You held YES, avg price 38%. |  |
| Main | Text | We couldn't generate your Share Card (T11). Your win and payout are not affected. You can share as text instead. | **leftover spec-note (internal codes)** |
| Main | Button | Share as text |  |
| Main | Button | See next events | **same-action / go-to-events button varies** |
| Main | Text | Per ia/docs/flows.md SJ1: a missing card (T11) falls back to a text share (T13a), not a dead end - the win is still shown. | **leftover spec-note (internal codes)** |
| Main | Text | Generating your Share Card... |  |
| Main | Label | Your win and payout are confirmed. The shareable card is being created. |  |
| Main | Label | You held YES, avg price 38%. Payout is settling on-chain. |  |
| Main | Text | Your payout is on the way |  |
| Main | Label | It will arrive in your balance in a few minutes (on-chain settlement delay). You can still share now. |  |
| Main | Field label | Share Card (auto-generated) |  |
| Main | Text | Share Card: "Called it - US shutdown, YES from 38%. +$13.20 on Yonder." (image placeholder) |  |
| Main | Button | Share |  |
| Main | Field label | What happened |  |
| Main | Text | The federal government entered a shutdown on Feb 18, 2027 after Congress missed the funding deadline. The market resolved YES, the side you held. |  |
| Main | Text | One moment, then move on - no confetti loop. Share is the primary action; "see next events" is deliberately secondary (research F5: the first win, not loss, drives overconfidence and escalation). | **leftover spec-note (internal codes)** |

### Loss Screen

_2 state page(s): loss-loading.html, loss.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Active Bets (resolved item) or a tapped resolution notification (G1: 1 tap) | **leftover spec-note (internal codes)** |
| Main | Heading | Here's what happened |  |
| Main | Text | Loading the resolution... |  |
| Main | Label | Fetching what resolved and why. |  |
| Main | Field label | What happened |  |
| Main | Text | Congress passed a stopgap funding bill on Feb 27, 2027, two days before the deadline, so no shutdown occurred. The market resolved NO. You held YES. |  |
| Main | Field label | Result |  |
| Main | Label | -$5.00 |  |
| Main | Label | Your $5.00 stake on YES did not return. Avg price 38%. |  |
| Main | Button | Back to your bets | **same-action / go-to-events button varies** |
| Main | Button | Browse events | **same-action / go-to-events button varies** |
| Main | Text | One clear next step, and no "bet again" prompt. The resolution note is shown first so the outcome is understood before any new bet (FJ5 + EJ3: a conscious exit, no impulse to chase). | **leftover spec-note (internal codes)** |

## User-written content (do NOT rewrite)

These lines are authored per event or by other users - event questions, outcome names, the per-event editorial (why-this-price, arguments, resolution notes), share cards, comments, usernames and holdings. Our voice work does not touch them; they get a separate content guideline for whoever creates markets.

**Event questions (titles):**

- Which coin will have the highest market cap on January 1, 2027?
- Which company will reach a $5T market cap first?
- Which party will win the most seats in the next UK election?
- Which party will win the most seats in the next UK general election?
- Who will win Album of the Year at the 2027 Grammys?
- Who will win the 2027 Eurovision final?
- Who will win the 2028 Republican presidential nomination?
- Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?
- Will Bitcoin close above $150,000 before October 1, 2026?
- Will Democrats win control of the House in the 2026 midterms?
- Will Ethereum complete its next major network upgrade before November 1, 2026?
- Will Trump's average approval exceed 45% in Q1 2027?
- Will USDC remain fully backed 1:1 through 2026?
- Will a crewed mission launch toward the Moon before January 1, 2028?
- Will a major AI model pass a recognized medical-licensing exam in 2026?
- Will a new Supreme Court justice be confirmed before July 1, 2027?
- Will a new global pandemic be declared by the WHO in 2026?
- Will a reunion tour by a 1990s band be announced before 2027?
- Will a single film cross $2B at the global box office in 2026?
- Will a spot Solana ETF be approved before July 1, 2027?
- Will any memecoin enter the top 10 by market cap before 2027?
- Will the EU formally admit a new member state before January 1, 2028?
- Will the US government shut down before March 1, 2027?
- Will the full Epstein files be released before January 1, 2027?
- Will the most-streamed show of 2026 be a returning series?
- Will the next lead actor for the Bond film be announced before December 31, 2026?

**Outcome names / sample social content (comments, usernames, holdings, trades):** marketmaven, deadline_dan, polly_predicts, newhere, whale_07, alpha_ape, satoshi_jr, hedge_hannah, caut_carl, riskoff; outcome options JD Vance / Donald Trump / Ron DeSantis / Nikki Haley, Sweden / Italy, Labour / Conservatives; plus every comment body and the per-event *Why this price* / *For YES* / *For NO* / *Resolution conditions* / *What happened* narrative and the auto-generated *Share Card* text.

---

## Rewrite log

Lines rewritten against `voice.md`, one screen at a time. Structure and markup
unchanged; only text. User-written content is never touched.

### Step 05 - Event Feed (event-feed + -empty / -error / -loading, both auth variants)

| Page(s) | Element | Was | Became | Rule applied |
|---|---|---|---|---|
| event-feed-empty, event-feed-logged-out-empty | Empty - body | There are no markets for this category and filter combination right now. Try clearing the filters, or get notified when a new event shows up here. | There are no events for this category and filters right now. Clear the filters, or get notified when a new event shows up here. | Lexicon: **market -> event**; Microcopy/empty: say why + a direct next step ("Clear the filters", imperative) |
| event-feed-error, event-feed-logged-out-error | Error - body | Something went wrong reaching the network. Check your connection and try again. | We couldn't reach the network. Check your connection and try again. | Forbidden: drop **"Something went wrong"**; Microcopy/error: say what happened + what to do |
| event-feed-empty | Empty - title | No events match your filters | *(unchanged)* | Already compliant (event, concrete) |
| event-feed-error | Error - title | Couldn't load events | *(unchanged)* | Already compliant (matches the "Couldn't load ..." pattern) |
| event-feed-empty | Empty - buttons | Clear filters · Notify me of new events in this category | *(unchanged)* | Already compliant (verb + object; event) |
| event-feed-error | Error - button | Try again | *(unchanged)* | Already the canonical retry label |
| event-feed-loading, -logged-out-loading | Loading | *(silent skeleton, no text)* | *(unchanged)* | Microcopy/loading: silent is correct |
| event-feed-push-permission-missing | Push banner | Enable notifications to get live updates on the events you follow. + "Enable notifications" / "Not now" | *(unchanged)* | Already compliant (concrete benefit, verb buttons, no hype) |

**Not changed here (shared components, handled in a global pass so they stay
identical across all 99 pages, not diverged on 4):** header + avatar menu
("Wallet / Deposit" -> "Add funds"), logged-out header ("Log in" -> "Sign in"),
bottom nav, footer (placeholders + "Markets" -> events), the card component
(bookmark "Save"), and the shared Sign in / Add funds dialogs. These carry lexicon
and Forbidden changes too, but touching them on the Event Feed only would break
the byte-identical chrome. Flagged for the chrome pass.

### Global chrome pass (shared frame, applied byte-identical across all pages)

Header, logged-out header, footer and the shared dialogs, changed once everywhere
so they stay identical on all 99 pages.

| Where | Element | Was | Became | Rule | Pages |
|---|---|---|---|---|---|
| Header (logged-in) | Avatar menu item | Wallet / Deposit | Wallet | Lexicon: retire "Deposit" (funding = **Add funds**, already the header "+" control); the item routes to the Wallet screen | 53 |
| Header (logged-out) | Auth button | Log in | Sign in | Lexicon: auth = **Sign in / Sign up** | 29 |
| Footer | Column heading | Markets | Events | Lexicon: **market -> event** in the UI | 82 |
| Footer | Directory link | View all markets | View all events | Lexicon: **market -> event** | 82 |
| Shared Add funds dialog | Helper line | Minimum deposit $10. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead. | Minimum $10. KYC is required to add funds by card; crypto-only users can connect a USDC wallet instead. | Lexicon: drop the **deposit** noun (funding = Add funds) | 99 |

**Deliberately NOT touched in this pass (flagged, need their own surface / a structural micro-pass):**
- **Notif dropdown label "Position resolved" -> "Bet resolved"** (bet vs position): the same string is notification *content* that also renders on the Notifications screen; done in the Notifications screen pass so that screen stays coherent.
- **Card bookmark "Bookmark" / "Bookmarked" (aria) and Event Detail `Bookmark / save event` -> "Save" / "Saved"**: a shared *card* component + the Event Detail control; done with the card / Event Detail pass.
- **Leaked dev-notes - DONE (removed 2026-07-03).** The dialog `dlg-note` ("Opens over the current page ... see reference pages ...") and the overlay `dim-note` ("underlying screen dimmed ...") were deleted: 198 dlg-note lines across 99 pages + 17 dim-note lines across 17 pages. These were spec-notes, not shippable copy (Forbidden). Dialog / overlay structure verified intact; the now-unused `.dlg-note` / `.dim-note` CSS rules are left in place (invisible, harmless).
- **Footer wireframe placeholders** ("logo placeholder", "Tagline placeholder", the "[Regulatory / licensing line ...]" strip, "Sample wireframe content", and the TBD / post-MVP / dynamic roadmap tags): kept on purpose - they are honest grey-box stand-ins for content that is genuinely not set yet, not copy to invent (P5).

### Step 06 - Event Detail (13 state pages: binary / multi / resolved / loading / error / bet-processing / -reconcile / -insufficient / -error, + logged-out variants)

Only product copy touched; the per-event editorial (**Why this price** body, **For YES** / **For NO** arguments, **Resolution conditions** text, the event question) is user content and left untouched.

| Element | Was | Became | Rule | Pages |
|---|---|---|---|---|
| Meta line (frequency) | Politics · One-time **market** | Politics · One-time **event** | Lexicon: market -> event | 9 |
| Place-bet CTA | **Bet** (button) | **Confirm bet** | Lexicon: place-bet = "Confirm bet" (was inconsistent: 8 "Bet" vs 4 "Confirm bet") | 8 |
| Bookmark control (Event Detail) | Bookmark / save event | **Save** / to Favorites | Lexicon: Save into Favorites | 9 |
| Bookmark control (shared card, aria) | Bookmark / Bookmarked | **Save** / **Saved** | Lexicon: Save (feed / category / favorites cards) | 12 |
| Processing CTA | View your **position (on success)** | View your **bet** | Lexicon: bet not position; drop the "(on success)" dev note | 1 |
| Bet-error body | Your bet did not register on-chain **(T3)**. No funds were taken. | Your bet did not register on-chain. No funds were taken. | Forbidden: strip internal code | 1 |
| Bet-panel spec-notes (4) | `.fine` notes: "on-chain error (T3): ...", "insufficient-balance: inline guard ...", "S5 reconcile: ...", "execute on-chain processing: transitional ..." | *(removed)* | Forbidden: leaked spec-notes with internal codes, deleted | 4 |

**Already on-voice, kept:** "Place your bet", "Why this price", "For YES" / "For NO", "Resolution conditions", "Price chart", "Resolves YES" / "Resolves NO", "Source:", the insufficient-balance message ("You have $3.00. You can bet up to $3.00, or add funds to bet more." + "Add funds" / "Bet $3.00 instead"), and the reconcile message ("The price moved while you signed in" + "Was 38% -> Now 41% ..." + "Confirm at new price (41%)" / "Cancel and re-evaluate").

**Flagged - needs a decision / its own sub-pass:**
- **"Liquidity" stat label - RESOLVED (2026-07-03):** relabelled to **"Open to bet"** (`<span>Open to bet<b>$31,500</b></span>`, 9 pages). Plain, spectator-legible (P3).
- **Content tabs surface** (Comments / Top Holders / **Positions** / Activity, plus the Positions table columns **Shares** / Avg / Value and the Activity **trade** feed, and the helper "Positions update as the market trades"): this is a Polymarket-style social/trading panel built on trader vocabulary. The lexicon says bet-not-position, and "shares" / "liquidity" are forbidden - but reworking it is a real design question (do we show "shares" at all?). Held for its own sub-pass rather than half-changed here.
- **Status chips** ("execute failed", "amount over balance", "price changed", "submitting"): terse dev-ish state labels; low priority, left for now.

### Step 07 - Category Pages (Politics / Crypto / Culture / General, 32 pages: base / empty / error / loading x logged-in / logged-out)

Structurally the Event Feed filtered to one category; same rules. Cards use the shared component (bookmark already "Save"). Event questions in cards ("... market cap ...") are user content, untouched.

| Element | Was | Became | Rule | Pages |
|---|---|---|---|---|
| Empty - body | No {Category} **markets** match the current sub-category and filters. Clear the filters, or get notified when new ones open. | No {Category} **events** match the current sub-category and filters. Clear the filters, or get notified when new ones open. | Lexicon: market -> event | 8 |
| Error - body | **Something went wrong** while loading these **markets**. Check your connection and try again. | We couldn't load these **events**. Check your connection and try again. | Forbidden: drop "Something went wrong"; Lexicon: market -> event | 8 |
| Empty - title | No events match these filters | *(unchanged)* | already compliant |  |
| Error - title | Couldn't load {Category} | *(unchanged)* | already compliant |  |
| Empty / error - buttons | Clear filters · Notify me of new {Category} events · Try again · Back to Trending | *(unchanged)* | already compliant (verb + object, event) |  |
| Loading | *(silent skeleton)* | *(unchanged)* | Microcopy/loading: silent is correct |  |

Sub-category rail ("Sub-categories" + counts) and category headings: already clean. No other "market" in category product copy (the remaining ones are event-question titles = user content).

### Step 08 - My Bets (Active Bets: 9 pages - Active + History tabs x success / empty / error / loading)

The bet lists themselves were already spectator-clean (columns "Stake", "Status", "Payout", "Result", "WON" / "LOST" - no "position" / "shares" / "P&L"). Only state copy changed.

| Page | Element | Was | Became | Rule |
|---|---|---|---|---|
| active-bets-empty-resolved | Empty title | All your **positions** are closed | All your **bets** are settled | Lexicon: bet not position |
| active-bets-error | Error title | Couldn't load your **positions** | Couldn't load your **bets** | Lexicon: bet not position |
| active-bets-error | Error body | **Something went wrong** while loading your bets. Check your connection and try again. | We couldn't load your bets. Check your connection and try again. | Forbidden: drop "Something went wrong" |
| active-bets-history-error | Error body | **Something went wrong** while loading your resolved bets. ... | We couldn't load your resolved bets. Check your connection and try again. | Forbidden: drop "Something went wrong" |
| active-bets-empty-new, -history-empty | CTA | Find events | **Browse events** | Lexicon: one go-to-events label |
| active-bets-empty-resolved | CTA | Find new events | **Browse events** | Lexicon: one go-to-events label |

**Kept (already on-voice):** heading "My Bets", tabs "Active" / "History", empty-new body ("You haven't placed any bets. Find an event you have an opinion on and put a real stake on the outcome."), empty-resolved body + "See resolved bets (History tab)", history-empty title/body ("No resolved bets yet. ..."), "Try again". The header notif-dropdown "Position resolved" (visible here too) is chrome and is handled in the Notifications pass.

### Step 09 - Deposit (7 pages: form / loading / pending / minimum-not-met / error-card / error-KYC / widget-load-failure)

Each page also carries the shared Sign in / Add funds dialogs (already on-voice). Only page-specific state copy changed.

| Page | Element | Was | Became | Rule |
|---|---|---|---|---|
| all (shared protect line) | Trust line | Your USDC is held 1:1 - we do not lend or invest **deposited funds**. | ... we do not lend or invest **your funds**. | Lexicon: retire "deposit" |
| deposit (form) | Helper | **Minimum deposit $10.** ... KYC is required for **card deposits**; ... | Minimum $10. ... KYC is required to **add funds by card**; ... | Lexicon: retire "deposit" noun |
| deposit-minimum-not-met | Validation | **Minimum deposit is $10.** Enter $10 or more to continue. | The minimum is $10. Enter $10 or more to continue. | Lexicon + Form-field validation rule |
| deposit-error-card | Body | Your card was declined **(T2)**. No funds were taken. Try another card, or connect a USDC wallet to skip cards entirely. | Your card was declined. No funds were taken. ... | Forbidden: strip internal code |
| deposit-error-KYC | Body | KYC verification was rejected **(T1)**, so **card deposits are** not available ... | KYC verification was rejected, so **adding funds by card is** not available ... | Forbidden: strip code; Lexicon |
| deposit-error-KYC | CTA | Back to feed | **Browse events** | Lexicon: one go-to-events label |
| deposit-widget-load-failure | Body | The Transak **iframe** was blocked or the network dropped. | The **payment widget** was blocked or the network dropped. | P3: drop dev jargon |
| deposit-widget-load-failure | Spec-note | `.fine` "Fallback per S3: route around the embedded widget ..." | *(removed)* | Forbidden: leaked spec-note |

**Kept (already on-voice):** "Add funds" headings + buttons, "Amount to add", "Pay with", "Payment pending" + "This usually takes under 5 minutes. We will notify you when your funds are ready.", the loading notes ("KYC may be requested inside the widget. This can take a moment." / "Do not close this window while the payment widget loads."), "Payment didn't load" + "Open Transak directly", "Card declined" / "Verification rejected" headings, "Try another card" / "Connect a USDC wallet instead" / "Connect a USDC wallet (no KYC)" / "Contact support".

### Step 10 - Sign In (4 pages) + Wallet (3 pages)

**Sign In** was already on-voice ("Sign in or create account", "Continue with Google / X / Apple", "Sign-in failed. The provider did not complete authentication. You can try again or use a different provider.", "Account already exists", "Waiting for the provider. This window stays open."). One change:

| Page(s) | Element | Was | Became | Rule |
|---|---|---|---|---|
| sign-in, -error, -provider-conflict | Fine print | **Deposits via card require KYC**; crypto-only accounts can connect a wallet instead. | **Adding funds by card requires KYC**; crypto-only accounts can connect a wallet instead. | Lexicon: retire "deposit" |

**Wallet:**

| Page | Element | Was | Became | Rule |
|---|---|---|---|---|
| wallet, my-profile | Funding button | Deposit | **Add funds** | Lexicon (also fixed the same button on My Profile) |
| wallet | Transaction type | **Deposit** via card (Transak) | **Added funds** via card (Transak) | Lexicon |
| wallet | Trust line suffix | ... your funds. **Deposits**, payouts and withdrawals are recorded below. | ... your funds. **Added funds**, payouts and withdrawals are recorded below. | Lexicon |
| wallet | Withdraw note | Withdrawals are in USDC only **at MVP (no fiat payout rail). PIX payout is Phase 2 (Brazil).** Network fee applies. | Withdrawals are in USDC only. A network fee applies. | P5 / drop internal roadmap language (kept in planning docs) |
| wallet | Withdraw note | After confirm, the withdrawal moves through: pending (on-chain) -> confirmed, or failed (funds returned to Cash). Tracked in the history below. | **On-chain transfers can't be reversed, so check the address before you confirm.** After that, the withdrawal shows as pending, then confirmed once it settles, or failed with the funds returned to your Cash. It's tracked in the history below. | Microcopy: dangerous / irreversible action - warn before the press (folded into the existing note, no new element) |

**Kept (already on-voice):** "Wallet", "Withdraw" / "Amount to withdraw" / "Destination USDC address" / "Confirm withdrawal", "Available to withdraw: $92.00 (Cash only; in-play funds are locked).", the wallet error ("Couldn't load your wallet. We couldn't fetch your balance and transactions. Your funds are safe; this is a display issue. Try again." - the model error), transaction rows ("Withdrawal to USDC address", "Payout: ...", "Platform fee (won bet)", "Stake: ..."; the event names in them are user content), wallet-loading is a silent skeleton.

### Step 11 - Notifications (5 pages) + the deferred header-dropdown fix

| Where | Element | Was | Became | Rule | Pages |
|---|---|---|---|---|---|
| Header notif dropdown + Notifications screen | Notification type | **Position resolved** | **Bet resolved** | Lexicon: bet not position (this closes the item deferred from the chrome pass) | 50 |
| notifications-empty | CTA | Find events to follow | **Browse events** | Lexicon: one go-to-events label | 1 |
| notifications-error | Error body | **Something went wrong** while loading your alerts. Check your connection and try again. | We couldn't load your alerts. Check your connection and try again. | Forbidden: drop "Something went wrong" | 1 |

**Kept (already on-voice):** "Notifications", groups "Unread" / "Earlier", notification types "Odds moved" / "Deadline approaching", empty title/body ("No notifications yet" + "When an event you follow moves, approaches its deadline, or resolves, you'll see it here. Follow an event to start getting alerts."), "Couldn't load notifications" title, "Try again", the push prompt ("Enable notifications to get live updates on the events you follow." + "Open system settings" / "Not now"), and notifications-loading (silent skeleton). Notification rows reference sample events = user content, untouched.

### Step 12 - Win Screen (4 pages) + Loss Screen (2 pages)

Already the most carefully toned screens (Win "You were right", no confetti; Loss "Here's what happened", no "bet again"). Changes were removing the design rationale that had leaked in as visible fine print, plus one code and the CTA label.

| Page | Element | Was | Became | Rule |
|---|---|---|---|---|
| win, win-payout-pending, win-error | CTA | See next events | **Browse events** | Lexicon: one go-to-events label |
| win-error | Body | We couldn't generate your Share Card **(T11)**. Your win and payout are not affected. You can share as text instead. | We couldn't generate your Share Card. Your win and payout are not affected. You can share as text instead. | Forbidden: strip internal code |
| win | Rationale note | `.fine` "One moment, then move on - no confetti loop. Share is the primary action ... (research F5 ...)." | *(removed)* | Forbidden: leaked spec-note |
| loss | Rationale note | `.fine` "One clear next step, and no "bet again" prompt. ... (FJ5 + EJ3 ...)." | *(removed)* | Forbidden: leaked spec-note |
| win-error | Spec-note | `.fine` "Per ia/docs/flows.md SJ1: a missing card (T11) falls back to a text share (T13a) ..." | *(removed)* | Forbidden: leaked spec-note |

**Kept (already on-voice):** "You were right" / "You were right - you won", "What happened", "Result", "Share" / "Share as text", "Share Card (auto-generated)", "Here's what happened", "Back to your bets" (goes to My Bets, not the feed), "Your payout is on the way" + the settlement note, win-loading / loss-loading. The resolution narrative and Share Card text are per-event / user content, untouched. (The state-switcher chip "Card failed (T11)" is wireframe tooling, not product copy.)

### Step 13 - The rest of the screens (Favorites 3 pages, My Profile 3, Public Profile 4, How It Works 1)

The remaining screen families in the tree, same pattern: only states already present in the inventory, no new copy invented. The track-record blocks on My / Public Profile were already spectator-clean ("Total bets", "Win rate", "Resolved predictions", "bets" not "positions"), and the profile funding button was already fixed to "Add funds" in the Step 10 Wallet pass. Sample usernames, event titles, win-card text, resolved-list rows and figures are user content, untouched.

| Page | Element | Was | Became | Rule |
|---|---|---|---|---|
| favorites-empty | Empty body | You have not saved any events yet. Tap **the bookmark** on any event to keep it here for quick access. | ... Tap **Save** on any event ... | Lexicon: Save (not "bookmark", browser jargon) - matches the card control now labelled "Save" |
| my-profile-error | Error body | **Something went wrong** while loading your track record. Try again. | We couldn't load your track record. Try again. | Forbidden: drop "Something went wrong"; Microcopy/error |
| public-profile-error | Error body | **Something went wrong** while loading this track record. Try again, or **go back to events**. | We couldn't load this track record. Try again, or **browse events**. | Forbidden: drop "Something went wrong"; Lexicon: one go-to-events label |
| public-profile-error | Error CTA | **Back to events** | **Browse events** | Lexicon: one go-to-events label |
| public-profile-not-found | Not-found CTA | **Go to events** | **Browse events** | Lexicon: one go-to-events label |
| how-it-works | Money-held body | ... place a bet or withdraw - **deposits**, payouts and withdrawals are all recorded in your Wallet. | ... **added funds**, payouts and withdrawals ... | Lexicon: retire the "deposit" noun (matches the Wallet pass) |
| how-it-works | Social-proof stat | **Markets resolved** (1,240) | **Events resolved** (1,240) | Lexicon: market -> event in the UI (consistency with the whole product; the source phrase in `benchmark.md` uses "markets", but the UI lexicon is "event") |
| how-it-works | Rationale note | `.fine` "Reachable before you deposit anything (from the menu and the footer) ... so the answer to 'what happens to my money' comes before the money does." | *(removed)* | Forbidden: leaked spec-note (describes where the screen sits, not user copy) |

**Kept (already on-voice):** Favorites - "Favorites" heading, "No favorites yet", sort/frequency/category filter labels, "Browse events", card controls (aria already "Save" / "Saved" from the Step 06 shared-card pass). My / Public Profile - "My Profile" / "Profile", "Couldn't load your/this profile", "Try again", "Portfolio" / "Cash (available)" / "In-play" / "Open Wallet", "Add funds" (fixed in Step 10), "Track record" / "Total bets" / "Win rate" / "Resolved" / "Member since", the win-rate gloss ("Reputation = the track record, not the balance"), "Resolved predictions (public)", "Edit name & avatar", "Public track record · read-only" + the read-only trust line, "Profile not found" + its body. How It Works - the intro ("You always know what you are doing ... a promise, not a FAQ"), all section headings + bodies (already P5-specific: resolution conditions, on-chain, AMM-timing payout, "fee only when you win"), "On-chain proofs" / "USDC held 1:1" / "always", "Browse events", "Add funds".

**Checked and deliberately NOT changed:**
- **Screen-tree label "Deposit"** (`<li class="wf-screen"><a href="deposit.html">Deposit</a>`, on all 99 pages): first flagged as a "footer Deposit link", but on inspection it is the **left screen-tree scaffolding** (the wireframe's IA index of screen families + states), not product copy - the real product `<footer>` carries no deposit link (its funding entry is "Wallet"). This is the IA node name for the screen family (route `deposit.html`), in the same tooling class as the state-switcher chips; it is out of scope for the copy rewrite and left as-is. The user-facing funding action is already "Add funds" everywhere. No lexicon violation remains.


### Step 14 - Krok 7 (check and finalize): straggler fixes + content-tabs spectator rewrite

The closing verification pass of the voice workstream (Lesson 05, step 7): a full
audit of every `wireframes/*.html` against `voice.md` (Lexicon / Forbidden /
per-element rules) surfaced the lines the screen-by-screen rewrite (Steps 05-13)
had missed, plus the one item it had deliberately deferred. Method: a
chrome-stripped visible-text grep for each Lexicon term (market / position / shares
/ Deposit / bookmark / Log in / trader jargon) and each Forbidden pattern, then
per-hit judgement (brand name "Yonder", the voice-sanctioned "the market
resolved YES/NO", and user content excluded). Clean on `bookmark`, `Log in`,
`cents/spread/liquidity/order book/buy-sell`, `Oops/Welcome/Congratulations/Sorry`,
exclamations and emoji. The stragglers and the deferred cluster, fixed:

| Screen(s) | Was | Became | Rule |
|---|---|---|---|
| 73 painted + 56 grey + 2 kit specimens, the account dropdown | five rows: `My Profile`, `My Bets`, `Wallet`, `How It Works`, `Logout` | a sixth, **`Favorites`**, between `My Bets` and `Wallet` | 2026-08-13, backlog 130. **No new string**: it is the label the bottom-bar slot and the desktop header heart already use, which is why this row records a placement rather than a word. The reason is the keyboard: the heart is desktop-only and the bottom bar sits after the footer in the document, so on a phone Favorites had no reach before tab stop 96 on the feed, while My Bets and My Profile sat at 10 and 9 through this same dropdown. Position is beside `My Bets` because those two and `My Profile` are the three top-level destinations the dropdown holds, and `Wallet` / `How It Works` / `Logout` are not |
| 105 painted + 87 grey, the sticky header's category strip | no accessible name, and `aria-hidden="true"` over five live links | **`Categories (sticky header)`** | 2026-08-13, backlog 118. The strip is a `<nav>` now and says what it is. It repeats the five categories of `Categories (second level)` once that band has scrolled away, so the two need names that tell them apart rather than one of them claiming not to exist: on the 57 screens where the strip opens, a screen reader was told a visible, operable band with five reachable links was not there. The parenthetical follows the house pattern already set by `Categories (second level)`, `Primary (mobile)` and `Language (placeholder)`, and it names the PLACE rather than the state, because "condensed" describes the CSS and "sticky header" describes where the person will find it |
| 48 painted + 30 grey, the same strip where nothing can open it | five live category links, named and unreachable | **(the strip is gone)** | 2026-08-13, backlog 142. The line above named it on 105 painted and 87 grey; it stands on 57 and 57 now. The observer that reveals it watches `.feed-inner > .cat-nav` and returns early where there is none, so on those 48 the band could not open at any width, and 240 anchors in the paint and 150 in the grey carried a name for a route no eye and no keyboard reached. **A name is a promise about something a person can get to**, so the answer was the markup rather than a second anchor for the observer: giving those screens a category route is a navigation decision and belongs to 03a |
| footer, all 105 painted + 87 grey | `X`, `Discord`, `Telegram`, `Instagram`, `TikTok`, five `aria-label`s over `href="#"` | **(the row is gone)** | 2026-08-13, backlog 144. **525 anchors in the paint and 435 in the grey, the largest placeholder group in the product by a factor of five**, and the five labels were the only thing making them look like destinations. They were a third kind of placeholder: row 27 cut a link the map REFUSES and row 28 kept a link the map registers with no screen yet, and a social account can never become an internal route, so it cannot be waiting for one. They stood directly under the footer trust strip. The labels come back with the accounts |
| `deposit*`, `sign-in*` (7 + 4, both trees) | close control `aria-label="Close"` | **`Back to the event`** | 2026-08-11, backlog 97. On a standalone overlay page there is nothing to close: the page IS the overlay, and the control navigates. A name that says Close on a control that goes to another screen describes something that does not happen. The 105 in-page dialogs keep `Close`, because theirs is a button that closes |
| `win*`, `loss*` (4 + 2, both trees) | close control `aria-label="Close"` | **`Back to My Bets`** | 2026-08-11, backlog 97. Same rule, and these six already agreed on the destination |
| 14 screens per tree, the binary card pair (126 controls), the feed hero pair (2) and the SELECTED outcome row (2) | accessible name **`YES`** / **`NO`**, and `Back YES` in the hero | **`Will Bitcoin close above $150,000 before October 1, 2026? YES`**, `Will the US government shut down before March 1, 2027? Back NO`, `JD Vance selected YES` | 2026-08-13, backlog 103. **The same rule as row 96 below, and it writes no new string**: `aria-labelledby` points at the question the card already shows and then at the control, so this file keeps owning the wording. The binary card's outcome is not a word the way `Sweden` is, it is the card's question, so the name is 61 characters where row 96's are 11. **That length is the measurement and not the defect**: the alternative is a short title per market, a second string per event that would then have to be kept true against the first. Before this, 12 documents carried two or more controls sharing one name, five `YES` and five `NO` on a single category feed. The selected outcome row was a straggler of row 96, skipped because its `.opt-name` wraps a nested `selected` tag, and it is the row a person is most likely to act on |
| 14 feed screens per tree, 100 controls each | accessible name **`YES`** / **`NO`** | **`Sweden YES`**, `JD Vance NO`, and so on | 2026-08-11, backlog 96. A person tabbing heard "YES link, NO link" ten times with nothing to tell one row from the next. The name is built with `aria-labelledby` pointing at the outcome span and then at the control, so **the outcome wording stays in the one place this file owns it** and is not typed into the markup a second time |
| `event-detail*` painted bet sheet (4) | `YES selected` | **`YES pre-selected`** | 2026-08-11, backlog 87. The sheet was the one string in that block with no row in this inventory; the panel five lines above it already said the rowed one |
| 9 screens per tree | tab strip `role="tablist"` + `role="tab"` + `aria-selected` | **`<nav>` + `aria-current="page"`** | 2026-08-11, backlog 89. The tablist owned nothing, there is no tabpanel in that family, and the tabs navigate to another document. It is navigation with a current-page marker, which is the idiom this product already writes 1,228 times |
| `event-detail-error`, `event-detail-logged-out-error` | **Something went wrong** while loading the event details. Check your connection and try again. | We couldn't load this event. Check your connection and try again. | Forbidden: drop "Something went wrong" |
| `event-detail-error`, `-logged-out-error`, `-resolved` | CTA **Back to feed** | **Browse events** | Lexicon: one go-to-events label |
| `event-detail-resolved` | The **market** closed while you were reading **(event-closed)**. ... You hold a **position**, so you can open your result. | The **event** closed while you were reading. ... You hold a **bet**, so you can open your result. | Lexicon (market->event, position->bet) + strip leaked state code |
| `event-detail-resolved` | CTA **See your position** | **See your bet** | Lexicon: position->bet |
| `wallet` | In-play is locked in open **positions** until they resolve. | ... in open **bets** until they resolve. | Lexicon: position->bet |
| `how-it-works` | `.pos-status` "Resolved-market count as social proof **(benchmark.md Top 3 trust mechanisms)**." | *(removed)* | Forbidden: leaked spec-note |
| `event-detail`, `-multi`, `-logged-out`, `-logged-out-multi` | `.fine` "... Payout depends on when you bet (AMM). **Confirm opens sign-in (over this page), then deposit if needed.**" | "... Payout depends on when you bet (AMM)." | Forbidden: trailing spec-note trimmed |

**Content tabs -> spectator language (the deferred cluster from Step 06, 9 Event
Detail pages, binary + multi).** The Polymarket-style Comments / Top Holders /
Positions / Activity strip was built on trader vocabulary; per the user's call it
was rewritten to a spectator, not a trader, reading (P3):

| Element | Was | Became |
|---|---|---|
| Tab labels | **Top Holders** / **Positions** | **Biggest bets** / **Bets** |
| Holders headers | YES holders / NO holders / Top holders by outcome | Biggest YES bets / Biggest NO bets / Biggest bets by outcome |
| Holders amount | "1,240 **shares**" | "$1,240" (spectator $, illustrative grey-box figure) |
| Bets table | columns **Holder · Side · Shares · Avg · Value** | **Bettor · Side · Amount** (dropped the trader Shares/Avg columns; Amount = the $ figure) |
| Helper | Your row is highlighted. **Positions** update as the **market trades**. | Your bet is highlighted. **Bets** update as the **odds move**. |
| Logged-out prompt | Sign in to open and track your **position** | Sign in to place and track your **bet** |
| Activity feed | "whale_07 **bought 500 YES at $0.35** ($175)" / "marketmaven **sold 80 YES at $0.39** ($31)" | "whale_07 **bet $175 on YES**" / "marketmaven **cashed out $31 on YES**" |

Sample usernames and the sample figures stay illustrative (grey-box); the
"Biggest bets" $ amounts are not reconciled row-for-row against the "Bets" table
(different sample panels), which is acceptable for a wireframe. **Not touched:** the
AMM line "Prices move with the market (AMM)" on How It Works (voice.md allows
"market" in a mechanics gloss); "The market resolved YES/NO" on Win/Loss (voice.md
P4 example). The stale `_generators/gen_event_detail.py` was **not** regenerated -
it still holds pre-rewrite copy ("Liquidity", bare "Bet", "One-time market",
"Bookmark"), so regenerating would revert Steps 05-14; the pages are hand-maintained
from here (do not regenerate without back-porting the rewrite into the generator).

Health after the pass: 0 em-dash, 0 broken internal links across all 99 pages.

### Krok 6 reconciliation - same action, same label across all screens

The closing deliverable of the roll-out step (Lesson 05 step 6): after every screen
was rewritten, reconcile that one action carries one label everywhere. Method: extract
every product button / CTA / state-action label across all 99 pages (chrome + tooling
stripped), bucket by action, and flag any action with more than one distinct label.

| Action | Labels found | Verdict |
|---|---|---|
| Retry a load | **Try again** (x19) | one label - clean |
| Add funds | **Add funds** (x99) | one label - clean |
| Save / Favorites shelf | **Save** / **Saved** (card aria) into **Favorites** (x82) | one label - clean |
| Sign in | **Sign in** + **Sign up** | correct: two *different* actions (return vs new), not a discrepancy |
| Place the bet | **Confirm bet** (primary) · **Bet $3.00 instead** (insufficient-balance fallback) · **Confirm at new price (41%)** (S5 reconcile) | correct: three different moments; the reconcile label must show the new price (dangerous-action rule) |
| Go to the events feed | **Browse events** ... and **Back to Trending** (8 category-error pages) | **DISCREPANCY -> fixed**: "Back to Trending" went to `event-feed.html`, the same destination as "Browse events"; unified to **Browse events** on all 8 category-error pages (`{politics,crypto,culture,general}-error` + `-logged-out-error`). Now one label (x24). |

**Left as context-appropriate (surfaced, not forced):**
- **Subscribe to new events** - "Notify me of new **{Category}** events" on category pages vs "Notify me of new events **in this category**" on the Event Feed empty state. Same action, but the category page can name the category while the feed empty is category-agnostic (it depends on the active filter). Kept.
- **Go to My Bets** - "**Back to your bets**" on the Loss screen (FJ5-scripted, a calm *return* - you arrived from Active Bets) vs "**Go to My Bets**" on deposit-pending (a *forward* nav - you came from the bet flow). Same destination, but "back" vs "go" is accurate to each context. Kept.

Everything else (event vs market, bet vs position, Add funds, Sign in, one go-to-events
label) was already reconciled in the screen passes and the step-7 audit. Health: 0 em-dash,
0 broken internal links.

---

### Step 15 - System and global nodes (new pages: 404 / 500 / maintenance / cookie-consent / toasts)

New wireframes for the IA Detailed-layer system nodes (`ia/docs/pages/system.md`). This copy is
NEW (not a rewrite), written to the voice from the start: an error names what happened and the
way out, no apology, no joke, no "something went wrong", no exclamation; the funds-safety and
consent lines follow "one plain sentence of trust before the ask" and "say the specific
provable thing". Source of truth for the text is `system.md`; the wireframes render it verbatim.

| Page | Element | Text | Rule / source |
|---|---|---|---|
| 404.html | H1 | **This page does not exist** | error names what happened, not "Something went wrong" |
| 404.html | Body | **The link may be old, or the event may have been removed.** | plain reason |
| 404.html | Primary / secondary | **Browse events** + quick links (Home, How it works, the 4 categories) | never a dead-end; go-to-events label reused |
| 500.html | H1 | **We could not load this page** | names the failure plainly |
| 500.html | Body | **This is on our side, not your bet or your funds. Your money is safe.** | trust before the ask, even in an error |
| 500.html | Actions | **Try again** + **Home** | visible exit; reuses the canonical retry label |
| maintenance.html | H1 | **Yonder is down for scheduled maintenance** | states the fact, planned not crashed |
| maintenance.html | Body | **Your bets and funds are safe. We will be back shortly.** | trust reassurance |
| maintenance.html | Action | **Try again** | visible exit |
| cookie-consent.html | Banner text | **We use cookies to run the site and, only if you allow it, to measure and improve it.** | plain, no dark pattern |
| cookie-consent.html | Actions | **Accept all** / **Reject all** / **Manage** | reject as easy as accept (equal weight) |
| cookie-consent.html | Toggles | **Necessary (always on)** / **Analytics** / **Marketing** | Analytics + Marketing off by default, nothing pre-ticked |
| toasts.html | Success | **Bet placed** · **Funds added** · **Saved into Favorites** | state the fact, no celebration; labels reuse the lexicon |
| toasts.html | Error | **We could not place your bet. Try again.** | names it + the way out |

User content (sample resolved counts, placeholder legal-page labels) is not rewritten. Health
after this step: 0 em-dash on the 5 new pages, 0 broken internal links across all 104 wireframes.

---

### Step 16 - Footer reconcile (trust strip + SEO popular-links, stamped on all 87 footer pages)

New footer copy from the IA footer node (`ia/docs/pages/seo.md`), stamped in place by
`_generators/footer_reconcile.py` (idempotent, voice-safe: does not regenerate pages). The
trust-strip lines follow "one plain sentence of trust before the ask" and "say the specific
provable thing"; the popular-links block is the second internal-linking plane (crawlable).

| Element | Text | Rule / source |
|---|---|---|
| Trust strip 1 | **Your USDC is held 1:1, we never lend it.** | funds-safety line, persistent site-wide |
| Trust strip 2 | **Every event resolves against a public source.** | specific provable thing, not a superlative |
| Trust strip 3 | **1,284 events resolved** | resolved-count trust signal (sample figure, user content) |
| Popular block heading | **Popular right now** | SEO internal-linking surface |
| Popular links | **Politics events** / **Crypto events** / **Culture events** / **General events** / **Trending events** / **Ending soon** / **How it works** | crawlable links to priority pages |
| Legal re-entry | **Cookie preferences** | reopens the cookie-consent banner |

Real hrefs also wired where a wireframe exists (categories, How It Works, Wallet, My Bets, View
all events); legal pages that are not built yet (Terms, Privacy, About) stay placeholder links.
Health: 0 em-dash across all 104 wireframes, 0 broken internal links (16025 checked).

---

### Step 17 - Win screen F5 overconfidence-friction (win + win-error + win-payout-pending)

The audit found the Win screen had share + no "bet again" (correct) but no CJM F5
overconfidence-friction (the first win drives overconfidence into the next bet). Added a
grounding note on the path from Share to Browse events, on all three "you won" pages. Voice
principle 4 (mark the win without lighting a fuse) + "say the specific provable thing": it
states a fact, does not moralize, has no exclamation, and does not push the next bet.

| Page(s) | Element | Text (new) | Rule / source |
|---|---|---|---|
| win.html, win-error.html, win-payout-pending.html | Grounding note (label) | **Before the next one** | placed between Share and Browse events |
| same | Grounding body | **One right call is not a streak. The next event has its own odds, and this win does not change them. Read the next one on its own terms.** | CJM F5; voice principle 4 (mark the win, no fuse); spectator "read the event" framing |

Not touched: `win-loading.html` (skeleton). Health: 0 em-dash on the 3 pages, no new links.
(The generator `gen_resolution.py` is intentionally not back-ported, per the voice-safe rule.)

---

### Step 18 - Feed story-led reconcile: per-card "why" + below-fold SEO sections

The audit found the feed cards carried plain odds but no per-card "why" (the story-led entry is
the product differentiator, and it only lived on Event Detail), and the seo.md below-the-fold
SEO sections were missing. Stamped in place by `_generators/feed_reconcile.py` (idempotent,
voice-safe): a one-line why under each of the 8 cards on the 3 populated feed pages, and the 3
SEO sections on the two indexed feed success pages. The why lines are sample editorial content
(spectator language, specific, no superlative, no motivational tone); the SEO section copy is
lifted verbatim from `seo.md` section 1.

Per-card why (one line under each card question, story-led):

| Card question (sample) | Why line (new) |
|---|---|
| US government shutdown | One right sentence of context under the number: "Funding talks have stalled twice this quarter, but past deadlines settled late." |
| Bitcoin above $150k | "Price has held above $120k for three weeks as inflows climb." |
| Eurovision 2027 | "Three acts are polling close after the national finals." |
| Ethereum upgrade | "The upgrade is on the testnet with a target window announced." |
| Bond lead actor | "The studio says casting is underway, with no shortlist confirmed." |
| UK election seats | "Two parties are within the margin of error in recent polls." |
| EU new member | "Accession talks are open but no candidate has cleared the final chapters." |
| 2026 warmest years | "The year is tracking near record heat through the first quarter." |

Below-fold SEO sections (event-feed.html + event-feed-logged-out.html, verbatim from seo.md §1):
**How betting works here** (what the platform is, no wallet to start), **Why the odds move**
(explain-the-number), **Common questions** (FAQ x3: crypto to start / smallest bet / how it
resolves). The why lines and event questions are user/editorial content, not voice-forced.
Health: 0 em-dash, 16025 links / 0 broken. Category-card "why" is handled in the Category step.

---

### Step 19 - Event Detail "Related events" block (9 full-content pages)

seo.md section 2 specced a crawlable Related-events internal-linking block below the tabs; the
audit found it absent. Added by `_generators/related_events.py` (idempotent, voice-safe) to the
9 full-content Event Detail pages (binary / multi / resolved / logged-out / logged-out-multi +
the 4 bet-panel states); skipped on the loading and error states.

| Element | Text | Rule / source |
|---|---|---|
| Heading | **Related events** | seo.md section 2 B (internal-linking block) |
| Row (sample) | event question + odds, linking to a sibling event detail | crawlable internal link; questions + odds are sample content |
| Last row | **Browse more events** (-> event-feed.html) | category-agnostic exit, works on every variant |

Health: 0 em-dash, 16061 links / 0 broken (+36 = 4 links x 9 pages).

---

### Step 20 - Category reconcile: per-card "why" + "About {category}" text (8 success pages)

Finishes the story-led feed pattern on the category pages and adds the seo.md section-3 "About
{category} events" text. Stamped by `_generators/category_reconcile.py` (idempotent, voice-safe)
on the 8 category success pages (politics / crypto / culture / general x logged-in + logged-out);
empty / error / loading skipped. Shared events reuse the same why as the feed for consistency.

| Element | Text | Rule / source |
|---|---|---|
| Per-card why | one line under each of the 6 cards per category (spectator, specific, no hype) | story-led; sample editorial content, reused from the feed where the event repeats |
| About heading | **About {Category} events** | seo.md section 3 C |
| About body (template) | **Follow {category} events and back your opinion with a real stake. These events cover {fill}. You see the odds in plain language and how each event resolves before you bet, from one dollar, with no wallet to start.** | seo.md section 3 |
| Fill per category | Politics = elections, policy votes, appointments; Crypto = token prices, launches, upgrades; Culture = awards, releases, sports and entertainment milestones; General = real-world questions that do not fit the others | seo.md section 3 table |

Health: 0 em-dash across all 104 wireframes, 16061 links / 0 broken. The story-led "why" now
covers both the feed and the category pages; the feed + category SEO sections are all rendered.

### Step 21 - How it works header dialog (button next to the logo, 87 header pages)

Surfaces the feed explainer as a quick, always-available header affordance: a `How it works`
button next to the logo opens a native `<dialog>` with the same three sections, and a link out
to the full How It Works page. Stamped by `_generators/howitworks.py` (idempotent, voice-safe,
self-contained `.hiw-*` styling) on every page that carries the shared app-header (87 pages);
the 17 header-less pages (win/loss overlays, 404 / 500 / maintenance, cookie, toasts) are not
touched. The three section bodies are reused verbatim from the feed SEO sections (Step 18), so
the only genuinely new strings are the trigger label and the read-more link.

| Element | Text | Rule / source |
|---|---|---|
| Header trigger | **How it works** | button; sentence case, matches the footer link; opens the dialog |
| Dialog title | **How it works** | heading; names the thing, no greeting |
| Section labels | **How betting works here** / **Why the odds move** / **Common questions** | reused from the feed SEO sections (Step 18) |
| Section bodies + Q&A | reused verbatim from the feed below-fold SEO sections | Step 18; explain-the-number, spectator voice |
| Read-more link | **Read the full guide** | button; sends to how-it-works.html so the dialog is not a dead end |

Health: 0 em-dash across all 104 wireframes, 16148 links / 0 broken (the read-more link adds 87).
The feed keeps its below-fold SEO sections; the dialog is the interactive quick version.

### Step 22 - Shared dialog hero: Sign in + Add funds subtitles (ui-visual layer, 76 pages)

A visual-layer change only (like the How-it-works hero tagline, which the grey wireframe
does not carry): the Sign-in and Add-funds `<dialog>`s were pulled up to the How-it-works hero
style - a brass band, a Space Grotesk display title and a one-line subtitle. The hero visual is
CSS in `ui-visual/_theme.css`; the subtitle text is stamped into the two block-form dialogs by
`ui-visual/_dialog_hero.py` (idempotent, voice-safe; the inline `outcome-dialog` Win/Loss
variants are excluded, matching the CSS). No new marketing copy: each subtitle is an existing
line condensed. The wireframes are untouched.

| Element | Was | Became | Rule / source |
|---|---|---|---|
| Sign-in hero subtitle | body lead: **You are about to place a bet. Sign in or create an account to continue. No crypto wallet required.** | hero subtitle: **You are about to place a bet. No crypto wallet required.** (body lead removed - the title already says "Sign in or create account") | voice 2 (one plain line before the ask); relocated, not new |
| Add-funds hero subtitle | (none) | **Card or crypto. Your USDC is held 1:1.** | voice 2 (trust before the ask); condensed from the protect line, which stays in the body with the full "we do not lend or invest" clause |

Health: 0 em-dash across ui-visual; wireframes untouched; 76 pages carry both subtitles (152
occurrences), 0 old `signin-lead` body leads remain. Win/Loss outcome dialogs keep their quiet
green/red header (no brass hero, no subtitle).

### Step 23 - Withdraw becomes a dialog (wallet, grey + color)

Adding funds and taking them out are the same kind of act, and one of them was a dialog while the
other was a collapse in the middle of the page. No new lines were written: the summary became the
heading, one fine-print line became the subtitle, and the warning that matters most was promoted out
of the closing paragraph to sit above the button, where a person reads it before they act instead of
after.

| was | became | where | why |
|---|---|---|---|
| `Withdraw funds (USDC)` (summary of a collapse) | `Withdraw funds` (dialog heading) | `.sheet-head h2` | the currency is in the subtitle now, so the heading says the act |
| (none) | `Withdrawals are in USDC only. A network fee applies.` | `.sheet-sub` | moved up from the body, where it was a fine-print line under the address |
| `On-chain transfers can't be reversed, so check the address before you confirm. After that, the withdrawal shows as pending, then confirmed once it settles, or failed with the funds returned to your Cash. It's tracked in the history below.` | split: `On-chain transfers can't be reversed, so check the address before you confirm.` above the button, the rest below it | `.protect` + `.fine` | principle 2: one plain sentence of trust before the ask. What cannot be undone belongs before the button; what happens next belongs after it |

### Step 24 - The copy the paint wrote and this table never saw (Event Detail redesign, feed hero, brand tile)

Not a rewrite. This is the inventory catching up with itself, and the way it was found is the point:
the Stage-09 structure port copied the painted `<main>` back into `wireframes/`, which owns copy, and
43 strings arrived that no row here describes. All of them have been shipping in `ui-visual/` since
Stage 08, when the Event Detail was redesigned during the colour pass and the feed hero and brand
tile were built. **The table is the source of truth for copy, and for one stage it was the copy.**

Sample content is not inventoried by the rules above (event questions, volumes, usernames, dates),
so what follows is the interface copy only. It is logged as written, not edited: it was already read
against `voice.md` when it shipped, and the two lines that were not are marked.

| line | where | rule it answers |
|---|---|---|
| `Market` | `.market-title`, the AMM panel head | lexicon: the concept is the market, the thing you back is an event |
| `Yes price` / `No price` / `24h` / `Volume` / `Liquidity` | `.ms-label` | principle 1: name the number before showing it |
| `Price by bet size` | `.md-title` | says what the table is, not what it is called internally (no "depth chart") |
| `How the YES price moves as your bet grows. This market runs on an AMM, not an order book.` | `.md-sub` | principle 1 and principle 3: explains the mechanism in a spectator's words, and says what it is NOT, because an order book is what a trader would assume |
| `Bet` / `Avg YES price` / `You receive if YES` | `.md-row-head` | column heads in the lexicon: bet, not position; receive, not payout |
| `Rules` / `Market Context` | `.rules-tab` | two tabs, because what decides the outcome and what explains the odds are different promises. See the note below |
| `Background from the Yonder team to explain the odds. It plays no role in how this market resolves.` | `.rules-note` | the sharpest line of the redesign: it exists so the context tab can never be mistaken for the resolution rule |
| `Not just news.` / `Opinions have value.` / `The market decides.` | `.brand-tile` | principle 5: three specific claims, no superlative |
| `Every outcome is public and verifiable.` / `1,284 events resolved on-chain` | `.hero-trust` | principle 2: one plain sentence of trust, with a number that can be checked |
| `Back YES` / `Back NO` | `.hf-btn`, the featured hero | the hero is the one place the verb is written out; the cards keep bare `YES` / `NO` |
| `Hot right now` / `See all hot events` | `.hh-head`, `.hh-all` | a heading and its exit, per the empty-state rule that every block gives a way out |
| `Live odds &amp; volume &middot; last 30 days` | `.hf-chart-cap` | says what the chart is measuring and over what window |
| `Load more events` | `.load-more` | lexicon: events, never markets, in a control |
| `Browse more events` | `.related-more` | same verb as the empty states, so leaving a dead end reads the same everywhere |

**Two lines were opened as defects and both were closed as correct.** Recorded because the reasoning
is the useful part, and because the first one is a line that looks wrong and must not be changed.

| line | the objection | the answer |
|---|---|---|
| `Closes: Sep 1, 2027` | every other label in the product is `label value`, so the colon reads like the one inconsistency | the colon is not punctuation here, it is a **delimiter**: the feed script splits the meta row on it into `.m-label` and `.m-val`, which is why `coverage.md` lists both classes as built at runtime. Take the colon out and the row stops splitting. A style rule that would break a script is a style rule with a missing fact in it |
| `Trending now &middot; Politics` | reads like the tiny tracked eyebrow above every section, which is a named AI tell | kept: it appears once, on the featured hero, and it says WHERE you are rather than announcing the section below it. One named location is voice; an eyebrow on every block is grammar |

Health: the grey tree and the colour tree now carry identical copy inside `<main>` on all 55 twinned
screens, which gate 18 checks. 0 em-dash. No line was invented for the wireframe.

### Step 25 - The switch that said its own state (19 screens, both trees)

Found by re-measuring contrast, not by reading: `button.toggle[role=switch]` on the sort panel
carried the word `off` inside the pill, drawn in the browser's default black on graphite at
**1.42:1**. It was never meant to be read. The switch is drawn by CSS as a track and a knob, so the
word sat under the knob, invisible to a person and a WCAG AA failure to a checker.

The defect is not the colour. **The text content of a switch is its NAME, and this one was its
STATE**, which `aria-checked` already carries and carries better: a screen reader announces on/off
from the attribute, so the word was a second, silent, contradictory copy of the same fact.

| was | became | where | why |
|---|---|---|---|
| `off` as the button's text | removed; `aria-label="Reverse sort"` instead | `.reverse-row .toggle[role=switch]`, 19 screens x 2 trees | the visible label `Reverse sort` already sits beside it in the row; the button now takes that as its name and lets `aria-checked` say the state |

Health: 31068 text pairs measured across 77 painted screens in both themes, **0 below AA** (was 3).

### Step 26 - The footer trust block, and the last five strings the paint wrote alone

Step 24 caught the copy the Stage-08 paint wrote inside `<main>`. It could not catch the footer,
because gate 18 compared `<main>` and nothing else, so the footer was never read against the grey
twin at all. Step 7e compares all four regions, and the trust strip came back with five strings no
row here describes and two it replaced.

The paint had turned three bare sentences in a row into a headed block with an icon, a claim and a
second line under each. That is a better shape for the same promise, and it is structure, so it now
stands in `wireframes/` too. Logged as written, not edited: the lines were read against `voice.md`
when they shipped.

| was (grey, since the Stage-04 reconcile) | became (both trees) | rule it answers |
|---|---|---|
| (nothing) | `Built on trust, not on your balance` | principle 5: the specific provable thing. It says what the section is about and refuses the obvious pun about money |
| `Your USDC is held 1:1, we never lend it.` | `Your USDC is held 1:1` + `We never lend it.` | principle 2: one plain sentence of trust. Splitting the claim from its guarantee lets the eye take the claim and the sentence answer it |
| `Every event resolves against a public source.` | `Every event resolves against a public source` + `You can check it.` | same split. The second line is the one that makes it a promise rather than a policy |
| `1,284 events resolved` | `1,284 events resolved` + `On-chain, verifiable.` | principle 5 again: the number was already checkable and never said where |

Not new copy, but new to this table for the same reason: `No notifications yet. We will let you know
when an event you follow moves or resolves.` has stood in three grey wireframes since they were
built (`active-bets-empty-new`, `favorites-empty`, `notifications-empty`) and in no painted screen,
because the colour pass grafted one canonical header onto every screen and flattened the state. It
ships in both trees now. The row it already had stands.

Health: 5 strings added to the grey tree, 2 replaced, 0 invented. Both trees carry identical copy in
`<main>`, `<header>`, the bottom nav and `<footer>` on all 55 twinned screens, which gate 18 checks.
0 em-dash.

### Step 27 - One dialog, one copy, and the page that was left as a document

Step 7f closed a fork nobody had a check for: Sign In and Deposit each exist twice, as the shared
`<dialog>` on 76 screens and as the standalone page that IS that dialog, and the two had drifted since
Stage 08. Merging them moved four lines from the page onto 76 screens, and none of them was written
here first, because the page they were written on was outside the last two audits.

**Merged into the shared dialog** (was on the standalone page only, now on both):

| line | where | rule it answers |
|---|---|---|
| `Adding funds by card requires KYC; crypto-only accounts can connect a wallet instead.` | the sign-in `.fine` | principle 2: the ask names its own condition before it is made, not after |
| `Pay with` | a `.field-label` over the payment widget | the field rule: a field says what it is. The widget had no label at all in the dialog |
| `Card payments are converted to USDC via Transak.` | the deposit `.fine` | principle 1: explain the number, and here the mechanism. A card charge that arrives as USDC needs a sentence or it reads as a swap nobody agreed to |
| `How it works` | a `.provider-btn` under the deposit fine print | principle 2 again, and it is the reason this merge went this way: the exit to How It Works is the trust affordance the deposit screen is there to earn, and the shared dialog had lost it  **`(what happens to my money)` dropped 2026-08-14: two lines at 320 and 360 on 105 screens, and the header's control already said plain `How it works`** |

**Moved from the dialog to the page** (the page is the full version the dialog links to, so this is
the same string on a second surface, not a rewrite): `How betting works here` and its paragraph, and
the three questions under `Common questions`. The page never said how to place a bet, which is the
first thing a page with that title owes a reader.

**Written for this pass, one line:**

| line | where | why it exists |
|---|---|---|
| `Every figure here is a count you can check, not a claim.` | `.pos-note`, under `Proven, not promised` in the How It Works side column | principle 5. The heading `Proven, not promised` used to sit in a section of its own with nothing in it, above three numbers that never said what made them proof. The sentence is the difference between a stat strip and evidence |

Health: 1 line written, 4 moved onto 76 screens, 4 moved onto one page, 0 rewritten. Gate 19 now
fails the build when a screen and its family's shared dialog disagree, in either tree. 0 em-dash.

---

### Step 28 - Five trader terms in the five places a person meets them while ACTING

The rule this pass applies was written the same day it was applied, and that is the finding. The
lexicon has carried the ban since step 01 (`shares`, `spread`, `liquidity as a headline number`,
`order book`, `position`, `AMM`, `market` for the event), and the ban was a LIST OF WORDS. A list of
words cannot answer the question the product actually asks, which is why `AMM` on the How It Works
page is right and `(AMM)` under the Confirm button is wrong. `voice/docs/voice.md` now states the
invariant instead: **the ban is about PLACE, not about the word.** A trader term is forbidden
wherever a person meets it while ACTING - a control label, a heading, a figure read to decide - and
allowed inside a block whose whole job is to explain the mechanism, glossed in plain words. **And the
head of an exempt block is not inside the exemption**, because a summary, a tab and a title are read
by everyone who never opens them.

Sorted by that invariant, eight placements. **Five fail and are rewritten here:**

| was | is | where | which half of the invariant |
|---|---|---|---|
| `Holders` | `Bettors` | a `.seg` button in the Comments tab, 9 screens per tree | a control label. The lexicon's word for a person's stake is **bet**, and `position` is the trader's word for the same thing |
| `Liquidity` | `Available to bet` | `.ms-label` beside its figure, 9 per tree | a figure read to decide. The panel it stands in IS exempt, for EXPLANATION, and a naked number explains nothing, so it also fails principle 1 |
| `Market` | `How the odds are set` | the `<summary>` of the collapsed panel, `.market-title`, 9 per tree | the head of the exempt block. It is read by everyone who never opens the panel, and it now says what is inside instead of naming the mechanism |
| `Market Context` | `Background` | a `.rules-tab` beside `Rules`, 9 per tree | a tab label is an invitation, not an explanation. This was the worst spot in the product for the product's most-confused word: it sat next to the one panel that exists to keep `market` unconfused |
| `Payout depends on when you bet (AMM).` | `Payout depends on when you bet.` | `.fine` under Confirm, 4 screens, 8 painted occurrences and 4 grey | fine print read while deciding. The mechanism is still named where it is explained, one screen away |

**Three pass and are untouched**, which is the half of the invariant that keeps it from being a
find-and-replace: `order book` and `AMM` inside `.md-sub`, which is the mechanism being explained and
which says what it is NOT ("This market runs on an AMM, not an order book"), 9 per tree each; and
`AMM` on How It Works, 1 per tree.

**Route.** `wireframes/_generators/voice_reconcile.py`, idempotent and in place, both trees in one
run, because `CLAUDE.md` forbids regenerating the grey tree and a text edit is not a regeneration.
97 replacements on 22 files, second run 0. Both trees carry every string at the same count, so gate
18 is quiet and correct.

Health: 0 lines written from nothing, 5 rewritten, 3 deliberately kept, 0 em-dash. **And the class
this belongs to is the third instance in this repo: an invariant kept as a list of instances.** The
screen map was five hand copies before `_twins.py`; step 24 found 43 shipped strings with no row
here; step 14 declared itself "clean on cents / spread / liquidity / order book" while leaving every
instance outside its own list, including the `.fine` line it edited in that same pass.
