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
    to USDC)"; Win "Share Card ... (image placeholder)". **All three were answered on
    2026-08-16 and the answer was different for each**: the thumbnail label is the grey
    tree's and left the paint entirely, the two widget slots are a declared component
    and now say what they are in a sentence. See the dated section at the end.
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
| Header | Label | US government shutdown before Jul 1, 2026 - YES won |  |
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
| Footer | Text | Copyright (c) Yonder. | shipped 2026-08-21, was `Copyright (c) Yonder. Sample wireframe content.` |

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
| Deposit dialog | Text | The payment widget loads here (card to USDC) | the slot says what will stand in it, in the same words the loading and failure copy already use. Was `Transak payment widget (card to USDC)`, a noun phrase written for whoever was building the screen |
| Deposit dialog | Text | Your USDC is held 1:1 - we do not lend or invest deposited funds. |  |
| Deposit dialog | Text | Minimum deposit $10. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead. |  |
| Deposit dialog | Text | Opens over the current page after sign-in. States (card declined / KYC / widget fail / pending / minimum): see reference pages deposit-*.html. | **leftover spec-note (internal codes)** |

## Screens

### Event Feed

_9 state page(s): event-feed-empty.html, event-feed-error.html, event-feed-loading.html, event-feed-logged-out-empty.html, event-feed-logged-out-error.html, event-feed-logged-out-loading.html, event-feed-logged-out.html, event-feed-push-permission-missing.html, event-feed.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Trending |  |
| Main | Label | ~~Show:~~ | The label on the category sub-filter, added 2026-08-14. Its five chips say the SAME five words as the category navigation 100px above them, and the two do different things: that one ROUTES to a category page, this one NARROWS the list already on screen. `Show:` is what says which, and it is the shape the feed's other two filters have always had, `Sort:` and `How often:` | **Struck 2026-08-17, docs/backlog.md 182.** The row it labelled is deleted: two strips wore the same pill about 1,580px apart on the feed, one routing to a category page and one narrowing the list already on screen, and nothing on either said which. The band above keeps the taxonomy.
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
| Main | Option | ~~Hourly~~ | **Struck 2026-08-20, `docs/backlog.md` 224.** Off the CONTROL, not out of the vocabulary: `ia/docs/sitemap.md` keeps all four cadences on Event.Frequency and `docs/launch-catalog.md` opens no market at either, so these were two options that could never match. They return with the first hourly market |
| Main | Option | ~~Daily~~ | Struck with the row above, same date, same reason |
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
| Main | Link | +2 more outcomes | *added 2026-08-10, backlog 81. **Rewritten 2026-08-17 without a character changing.** It used to count what the DATA omitted, derived as the remainder over the smallest percentage shown, rounded up, which is a guess about a field nobody had written down. Every market carries its whole field now and sums to 100, so the row counts what the LAYOUT hides: two rows below the desk rung, none at it and above, where the link is `display:none`. **The numbers are the same** because each field was completed to exactly the size the card had already claimed, and the singular is written: `+1 more outcome` on three of the five.* |
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

_16 state page(s), re-counted 2026-08-20 when the two recurring specimens and the resolved multi landed: event-detail-bet-error.html, event-detail-bet-insufficient.html, event-detail-bet-processing.html, event-detail-bet-reconcile.html, event-detail-error.html, event-detail-loading.html, event-detail-logged-out-error.html, event-detail-logged-out-loading.html, event-detail-logged-out-multi.html, event-detail-logged-out.html, event-detail-multi.html, event-detail-recurring.html, event-detail-recurring-multi.html, event-detail-resolved.html, event-detail-resolved-multi.html, event-detail.html_

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
| Main | Label | Resolved YES on Jun 27, 2026 | resolved state only, `.ed-result`, 1 per tree |
| Main | Label | At close: YES 38% NO 62% | resolved state only, `.ed-prob-big` |
| Main | Label | YES at close | resolved state only, `.ms-label` |
| Main | Label | NO at close | resolved state only, `.ms-label` |
| Main | Label | Final volume | resolved state only, `.ms-label` |
| Main | Label | Settled | resolved state only, `.ms-label` |
| Main | Label | How the odds were set | resolved state only, the `<summary>` in past tense, 1 per tree |
| Main | Heading | How it settled | resolved state only, `.md-title`, replaces the price-by-bet-size table |
| Main | Text | Trading closed on Jun 27, 2026. Everyone holding YES was paid in full and everyone holding NO was not, against the source named in the rules. There is no price now and nothing to bet. | resolved state only, `.md-sub`. Spectator language: no shares, no settlement price, no order book |
| Main | Text | YES closed at 38%. Funding talks had stalled twice that quarter, and the three deadlines before it were settled at the last minute. What was moving the number: | resolved state only, the Background panel in past tense |
| Main | Text | A bloc had committed to opposing the stopgap bill. | resolved state only |
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
| Bet panel | Label | not sent | Rewritten 2026-08-16, and it now stands TWICE per screen: the mobile sheet carries the same `.bp-inner` as the aside. Was `execute failed`, an internal state name in a slot a person reads. The on-chain call is what failed and the person is not holding one. |
| Bet panel | Field label | Amount |  |
| Bet panel | Text | Your bet did not register on-chain (T3). No funds were taken. | **leftover spec-note (internal codes)** |
| Bet panel | Button | Try again |  |
| Bet panel | Button | Check wallet |  |
| Bet panel | Text | on-chain error (T3): retry the execute step, or check your wallet balance. | **leftover spec-note (internal codes)** |
| Bet panel | Label | $5 to win |  |
| Bet panel | Button | Bet | **same-action / place-bet button varies** |
| Bet panel | Label | over your balance | Rewritten 2026-08-16, and it now stands TWICE per screen: the mobile sheet carries the same `.bp-inner` as the aside. Was `amount over balance`, an internal state name in a slot a person reads. Same fact, said to a person rather than about a field. |
| Bet panel | Text | You have $3.00. You can bet up to $3.00, or add funds to bet more. |  |
| Bet panel | Button | Add funds | **same-thing / Deposit vs Add funds** |
| Bet panel | Button | Bet $3.00 instead | **same-action / place-bet button varies** |
| Bet panel | Text | insufficient-balance: inline guard in the panel before the gate fires. | **leftover spec-note (internal codes)** |
| Bet panel | Label | sending | Rewritten 2026-08-16, and it now stands TWICE per screen: the mobile sheet carries the same `.bp-inner` as the aside. Was `submitting`, an internal state name in a slot a person reads. A state, not the verb a form posts with. |
| Bet panel | Text | Registering your bet on-chain... |  |
| Bet panel | Label | A few seconds. Keep this open. |  |
| Bet panel | Button | View your position (on success) |  |
| Bet panel | Text | execute on-chain processing: transitional. On success it lands on Active Bets (T14); on failure, the on-chain error state (T3). | **leftover spec-note (internal codes)** |
| Bet panel | Label | price moved | Rewritten 2026-08-16, and it now stands TWICE per screen: the mobile sheet carries the same `.bp-inner` as the aside. Was `price changed`, an internal state name in a slot a person reads. The word the reconcile notice beside it already uses. |
| Bet panel | Label | The price moved while you signed in |  |
| Bet panel | Label | Was 38% -> Now 41%. Payout $13.16 -> $12.20 for $5. |  |
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
| Bet panel | Label | Pick a side | Replaced `YES pre-selected` on 2026-08-16. The old string existed to APOLOGISE for a default the product should not have had: `sel yes` was typed into the markup of every event detail, so the app chose a side on a two-sided money decision and then had to say so. Nothing is chosen at load now, and this is what the slot reads until the person chooses. |
| Bet panel | Label | YES selected / NO selected | The same slot after a side is chosen, whether the reader chose it here or arrived from a card that already said which. It was `YES pre-selected` in the sheet's own script and `YES selected` in the panel's, two strings for one state, both replaced by the second. |
| Bet panel | Field label | Your outcome |  |
| Bet panel | Link | Change |  |
| Bet panel | Label | ~~Price now~~ | **Struck 2026-08-17, docs/backlog.md 180.** It printed 38% while both sides read `aria-pressed="false"`, so "the price" was the YES price standing in for a choice nobody had made. The two side buttons already carry 38% and 62%, which is the same fact without picking one of them for the reader. |
| Bet panel | Label | Fee (1.5% of your bet) |  |
| Bet panel | Label | Total to pay | New 2026-08-16. The panel showed a stake, a price, a fee and a payout and never once said what Confirm was about to take. It is the fee rounded to cents PLUS the stake, so the two figures a person can see add up: 1.5% of $5.00 is 7.5 cents, and a raw fee prints $0.07 beside a raw total of $5.08. |
| Bet panel | Label | ~~Potential payout~~ | **Struck 2026-08-17, docs/backlog.md 180**, and replaced by the pair below. It was `$13.16`, which is 5 / 0.38, computed from a side the reader had not picked and drawn in the one brass on the plate, so the panel promised a win and said nothing at all about a loss. |
| Bet panel | Label | If YES wins / If NO wins | **New 2026-08-17.** Both outcomes or neither, same face, same weight, one of them `$0.00`. `PRODUCT.md` voice principle 4 is design the loss, and the loss was designed on the screen AFTER it happens and nowhere on the screen where it is chosen. The reader's own side takes `, your side` after the label rather than a mark of its own, because the chosen button is already lit eight pixels above and a second signal would be the accent spent twice. |
| Bet panel | Label | Pick a side to see what each outcome pays. | **New 2026-08-17.** It stands where the figures were, at body scale, and it is the whole block until a side is pressed. `Pick a side` alone stays in the head slot at 11px, which is the right size for a word that comments on a state and the wrong size for the one input standing between the reader and every number the block would print. The Confirm button points at this sentence with `aria-describedby`, so the reason it is held is reachable rather than only visible. | **2026-08-17, docs/backlog.md 186**: it is removed at run time the moment a side is pressed, whether the press came from the panel or from a card that carried `?side=`, and the pair takes its place in the same block.
| Bet panel | Label | Your balance |  |
| Bet panel | Button | Confirm bet | **same-action / place-bet button varies** |
| Bet panel | Text | $1 minimum, no maximum. The price you see is the price you get. Confirm opens sign-in (over this page), then deposit if needed. | Rewritten 2026-08-10 with the product decisions in `docs/backlog.md` 7 and 10: the minimum is $1, and the payout is shares at a locked price rather than a rule that depends on timing, so the sentence says what a person can check. |
| Bet panel | Button | JD Vance YES |  |
| Main | Heading | This event just resolved |  |
| Main | Text | The market closed while you were reading (event-closed). Betting is no longer available. You hold a position, so you can open your result. |  |
| Main | Button | See your position |  |
| Main | Label | Politics · One-time market · Trading closed |  |
| Main | Label | YES 38% at close, resolved YES |  |
| Main | Label | Repeats: Weekly | **New 2026-08-20, `docs/backlog.md` 224.** On recurring cards only. It went in as a bare `Weekly` and at 390 the meta row rendered `Weekly Volume: $46,300`, naming a figure this product does not have: every other span in that row is `Label: value` and a bare word joins the next label. The ATTRIBUTE `data-freq` is on all 432 cards; the WORD is news only when there is one |
| Main | Label | Repeats: Monthly | With the row above, same date |
| Main | Label | Crypto · Weekly series | **New 2026-08-20.** The `.ed-cat` line of `event-detail-recurring.html`. `series` and not `event`, because the reader is on one week of a run |
| Main | Label | Weekly | The `How often` fact on the recurring detail, beside `One-time` on the others |
| Main | Text | Resolves YES if the BTC-USD daily close on Friday, August 28, 2026 at 16:00 ET is above $119,500. Resolves NO if it is at or below that figure. | **New 2026-08-20.** The rule half a READER reads; `ia/docs/sitemap.md` Resolver is the half a program reads, and they have to agree |
| Main | Text | Source: CoinGecko BTC-USD daily close. Read automatically at 16:05 ET, so no person decides it. | **New 2026-08-20.** `docs/launch-catalog.md` admits a recurring market only if it is machine-resolved, so the detail says which machine |
| Main | Text | This is one week of a weekly series. It settles on its own, and when it closes the next week opens as a separate market with its own threshold. A bet here does not carry over. | **New 2026-08-20.** The one question a recurring reader has and a one-time reader never asks. It is the model of `ia/docs/sitemap.md` Frequency said in the reader's words |
| Main | Heading | Earlier in this series | **New 2026-08-20.** A second placement of the related component. There is no series page: the record IS the list |
| Main | Label | Resolved YES / Resolved NO | **New 2026-08-20.** The `.rel-odds` slot on a past instance, where a live row carries `YES 61%` |
| Main | Text | The threshold opened at this week's price, so Friday's close decides it. | **New 2026-08-20.** The card's `why`. It said `The strike opened at this week's spot`: voice principle 3, `strike` and `spot` are the desk's words and `threshold` and `price` are the reader's |
| Main | Label | Crypto · Monthly series · 3 outcomes | **New 2026-08-20.** The `.ed-cat` of `event-detail-recurring-multi.html`. The two axes cross here: the cadence and the outcome count in one line |
| Main | Text | Resolves to the chain holding the largest stablecoin supply when the reading is taken at 00:00 UTC on October 1, 2026. All other outcomes resolve NO. | **New 2026-08-20.** A multi rule resolves to an OPTION and every other option resolves NO, which is the sentence a binary rule cannot say |
| Main | Text | This is one month of a monthly series. It settles on its own, and when it closes the next month opens as a separate market with its own reading. A bet here does not carry over. | **New 2026-08-20.** The monthly twin of the weekly sentence |
| Main | Text | The series has run twice, for July and for August 2026, and Ethereum held the largest supply on both. | **New 2026-08-20, and it is prose because it cannot be a list.** The binary recurring detail carries its record as `Earlier in this series`, a list of resolved events. A resolved MULTI event has no page of its own, so linking these months would put a multi row on the binary resolved specimen, which is what `docs/backlog.md` 222 closed for the win and loss screens. `docs/backlog.md` 229 |
| Main | Text | ~~The series has run twice, for July and for August 2026, and Ethereum held the largest supply on both.~~ | **Struck 2026-08-20, the same day it was written.** It was prose because a resolved multi event had no page to link to; `event-detail-resolved-multi.html` exists now, so the record is `Earlier in this series`, the same block the binary twin carries. `docs/backlog.md` 229 |
| Main | Label | Crypto · One-time event · 3 outcomes · Trading closed | **New 2026-08-20.** The `.ed-cat` of the resolved multi. Four facts in one line, and `Trading closed` is the one the binary resolved twin also carries |
| Main | Label | Resolved **Ethereum** on Jul 1, 2026 | **New 2026-08-20.** The binary twin says `Resolved YES`; a multi resolution names an OPTION, which is the sentence `ia/docs/sitemap.md` says a binary screen cannot reach |
| Main | Label | paid $1.00 a share | **New 2026-08-20.** In the `.opt-sel-tag` slot, where a live page says `selected`. On a closed market the row that matters is the one that paid, and this is what it paid |
| Main | Text | Trading is closed. Ethereum paid one dollar a share and the other two paid nothing, against the source named in the rules. | **New 2026-08-20**, replacing `Tap YES or NO on an outcome to load it into the bet panel` on the resolved page, where there is no panel |
| Main | Text | Resolved Ethereum on Jul 1, 2026 at 00:05 ET. Ethereum held $73.4B in stablecoins against Tron at $61.2B and Solana at $12.8B. | **The Reading, and it is quoted rather than written.** `loss-multi.html` has printed this sentence since the outcome family took its multi half; the detail is the third surface it stands on and it had to equal the other two |
| Main | Label | Repeats: Monthly | The card that leads here, converted the same day from `at the end of 2026` to `at the end of September 2026` |

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
| Main | Option | ~~Hourly~~ | **Struck 2026-08-20, `docs/backlog.md` 224.** Off the CONTROL, not out of the vocabulary: `ia/docs/sitemap.md` keeps all four cadences on Event.Frequency and `docs/launch-catalog.md` opens no market at either, so these were two options that could never match. They return with the first hourly market |
| Main | Option | ~~Daily~~ | Struck with the row above, same date, same reason |
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
| Main | Label | Paid out |  |
| Main | Label | $13.16 |  |
| Main | Label | Your side |  |
| Main | Label | Result |  |
| Main | Label | Resolved Jun 27, 2026 · tap to see your win |  |
| Main | Label | $31.80 |  |
| Main | Label | Resolved Jun 20, 2026 · tap to see your win |  |
| Main | Label | Was a spot ETH ETF approved before July 1, 2026? |  |
| Main | Label | LOST |  |
| Main | Label | $0.00 |  |
| Main | Label | Resolved Jun 12, 2026 · tap to see what happened |  |
| Main | Label | $21.10 |  |
| Main | Label | NO · Action |  |
| Main | Label | Resolved Jun 2, 2026 · tap to see your win |  |
| Main | Label | Current value |  |
| Main | Label | Potential payout | The open position's figure, and a different string from the bet panel's struck one: this is what the row PAYS if the side held wins. **Corrected 2026-08-17, docs/backlog.md 181**: two of the three rows on `active-bets.html` printed a figure no price produces. $25 at 61% pays $40.98 and read $41.00; $10 at 33% pays $30.30 and read $22.50, which implies 44.4% and is neither the outcome's price nor its complement. Shares at a locked price, a winning share pays $1, so the payout is the stake over the price and nothing else. |
| Main | Label | ~~Current value~~ | **Struck 2026-08-17, docs/backlog.md 181.** A mark-to-market dollar figure on a product with no sell path: it moves, it can only make a reader feel worse, and it was defined on none of the 110 screens. What a person can act on is the price, so the slot carries `Price now` instead and the row reads what was paid against what the market says today. |
| Main | Label | Price now | **New 2026-08-17.** The current price of the side held, beside `Avg price`, which is what was paid for it. The two together are the whole story of an open position without inventing a dollar figure or implying an exit that does not exist. The three values are DERIVED from the ones they replace: $5.40 over 13.16 shares is 41%, $31.80 over 40.98 is 78%, $8.10 over 30.30 is 27%. The same words stood in the bet panel until the day before and were struck there for saying "the price" while meaning the YES price; here the side is known, so the label is exact. |
| Main | Label | Avg price |  |
| Main | Label | Open · just placed |  |
| Main | Label | Open |  |

### Favorites

_4 state page(s): favorites-empty.html, favorites-error.html, favorites-loading.html, favorites.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | Favorites | **same-thing / Bookmark vs save vs Favorites** |
| Main | Heading | Couldn't load your favorites | Error state, written 2026-08-18. Takes the register the inventory already calls the standard: load-error headings are uniformly **Couldn't load ...** and the retry is uniformly **Try again**. `your favorites` and not `favorites` for the same reason as `Couldn't load your bets` and `Couldn't load your wallet`: the thing that failed is yours, and the feed's own `Couldn't load events` is about the catalog |
| Main | Text | We couldn't load your saved events. Check your connection and try again. | Error state, written 2026-08-18. `saved events` and not `favorites` twice in two lines: the heading names the place, the message names the thing. It is the same shape as My Bets, whose message repeats the noun of its heading, and it does not promise a cause the product cannot know |
| Main | Button | Try again | Error state, written 2026-08-18. Points at `favorites.html`, not at the feed: a retry returns to what failed |
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
| Main | Option | ~~Hourly~~ | **Struck 2026-08-20, `docs/backlog.md` 224.** Off the CONTROL, not out of the vocabulary: `ia/docs/sitemap.md` keeps all four cadences on Event.Frequency and `docs/launch-catalog.md` opens no market at either, so these were two options that could never match. They return with the first hourly market |
| Main | Option | ~~Daily~~ | Struck with the row above, same date, same reason |
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
| Main | Text | The payment widget loads here (card to USDC) | same slot, same sentence, on the page rather than in the dialog |
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
| Main | Text | Win card: US shutdown YES net +$8.16 |  |
| Main | Text | Win card: BTC above $100k YES net +$6.80 |  |
| Main | Text | Win card: Spring box office NO Action net +$11.10 |  |
| Main | Text | Resolved predictions (public) |  |
| Main | Label | US government shutdown before Jul 1, 2026 |  |
| Main | Label | WON |  |
| Main | Label | YES · resolved Jun 27, 2026 · net +$8.16 |  |
| Main | Label | Bitcoin above $100,000 in H1 2026 |  |
| Main | Label | YES · resolved Jun 20, 2026 · net +$6.80 |  |
| Main | Label | Spot ETH ETF before Jul 1, 2026 |  |
| Main | Label | LOST |  |
| Main | Label | NO · resolved Jun 12, 2026 · net -$5.00 |  |
| Main | Label | Genre leading the 2026 spring box office |  |
| Main | Label | NO · Action · resolved Jun 2, 2026 · net +$11.10 |  |

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
| Main | Text | Win card: US shutdown YES net +$8.16 |  |
| Main | Text | Win card: BTC above $100k YES net +$6.80 |  |
| Main | Text | Win card: Spring box office NO Action net +$11.10 |  |
| Main | Text | Resolved predictions (public) |  |
| Main | Label | US government shutdown before Jul 1, 2026 |  |
| Main | Label | WON |  |
| Main | Label | YES · resolved Jun 27, 2026 · net +$8.16 |  |
| Main | Label | Bitcoin above $100,000 in H1 2026 |  |
| Main | Label | YES · resolved Jun 20, 2026 · net +$6.80 |  |
| Main | Label | Spot ETH ETF before Jul 1, 2026 |  |
| Main | Label | LOST |  |
| Main | Label | NO · resolved Jun 12, 2026 · net -$5.00 |  |
| Main | Label | Genre leading the 2026 spring box office |  |
| Main | Label | NO · Action · resolved Jun 2, 2026 · net +$11.10 |  |

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
| Main | Label | Payout: US government shutdown before Jul 1, 2026 - YES won |  |
| Main | Label | $13.16 |  |
| Main | Label | Jun 27 · completed |  |
| Main | Label | Platform fee (1.5% of stake) | Renamed 2026-08-16. The row said `(won bet)` and carried `-$0.40`, which is 3% of the payout: the `0.03 * payout` model `PRODUCT.md` retired on 2026-08-10 and which nothing had taken out of the ledger. The fee is charged at Confirm, so the row also moved to sit with the stake it was taken on. |
| Main | Label | -$0.38 | 1.5% of the $25.00 stake it now stands beside, rounded to cents. |
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
| Main | Label | Your bet resolved: US government shutdown before Jul 1, 2026 - YES won. Tap to see your win. |  |
| Main | Label | 2m |  |
| Main | Label | [unread] |  |
| Main | Label | Position resolved |  |
| Main | Label | Odds moved: "Bitcoin above $150,000" jumped from 58% to 64%. |  |
| Main | Label | 18m |  |
| Main | Label | Odds moved significantly |  |
| Main | Label | Closing soon: "Genre leading the 2026 spring box office" closes in 6 hours. |  |
| Main | Label | 1h |  |
| Main | Label | Event deadline approaching |  |
| Main | Text | Earlier |  |
| Main | Label | New in Crypto: "Will ETH flip BTC by 2027?" is now live. |  |
| Main | Label | Yesterday |  |
| Main | Label | New event in a followed category |  |
| Main | Label | Your bet resolved: Spot ETH ETF before Jul 1, 2026 - NO. Tap to see what happened. |  |
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
| Step 3 | Text | It resolves against the source it named, and what was read is published with the result. Until then your money is held 1:1, never lent and never moved. | **REWRITTEN 2026-08-19, 211 placements over 114 painted and 97 grey documents, the largest single string in this product.** It said `the result is written on-chain`, and the half of the sentence carrying a RESOLUTION claim was resting on the wrong proof: a hash proves that a decision was recorded and cannot say what the decision was made FROM, which is the only question a person who suspects the platform is actually asking. The Resolution entity gained a **Reading** the same day (`ia/docs/sitemap.md`), so the sentence now points at something a reader can open. **The custody half of the same sentence is untouched and the chain stays wherever it does real work**: a segregated balance you can check, a settlement that is pending, a bet that failed to register. 217 placements moved and about 364 kept the word, and the line between them is claim against mechanism, not vocabulary |
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
| Main | Text | Every resolution is published with what was read, the source and the time it was read, so you can check the outcome yourself instead of taking our word for it. | **REWRITTEN 2026-08-19, 2 placements.** The same correction as Step 3 and the sharper case, because this sentence is the whole resolution promise on the page that exists to make it. `cannot be changed after the fact` was the hash's argument and it answered tamper-proofing, which nobody had accused us of; `you can check the outcome yourself` answers the fear `PRODUCT.md` documents |
| Main | Heading | How pricing and payouts work |  |
| Main | Text | Prices move as people bet. You buy YES or NO at the price on screen, and that price is locked when you confirm. A winning share pays one dollar, so a lower price buys more shares and a larger payout. The amount, the fee and the payout are all shown before you confirm. | Rewritten 2026-08-16. The old line framed the payout as depending on WHEN you bet, which is the model `docs/backlog.md` 10 replaced on 2026-08-10 with shares at a locked price. The bet panel took that decision the same day (the row further up says so); How It Works did not, and kept the retired mechanic for six days. |
| Main | Text | There is no subscription. The fee is 1.5% of your bet, added when you confirm, and the panel shows it in cents before you commit. It is the same whether you win or lose. | Rewritten 2026-08-16. The old sentence promised a fee only on a win while the panel beside it charged 1.5% of the stake at Confirm and the wallet ledger charged 3% of the payout: three surfaces, three fee models, on a product whose number one churn driver is platform betrayal. `docs/backlog.md` 6 decided 1.5% of the stake. |
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

_5 state page(s): win-error.html, win-loading.html, win-multi.html, win-payout-pending.html, win.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Active Bets (resolved item) or a tapped win notification | **leftover spec-note (internal codes)** |
| Main | Heading | You were right |  |
| Main | Field label | You were right - you won |  |
| Main | Label | $13.16 |  |
| Main | Label | $5.00 stake returned + $8.16 winnings. You held YES, avg price 38%. |  |
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
| Main | Text | Share Card: "Called it - US shutdown, YES from 38%. Paid out $13.16 on Yonder." (image placeholder) |  |
| Main | Button | Share |  |
| Main | Field label | What happened |  |
| Main | Text | The federal government entered a shutdown on Jun 26, 2026 after Congress missed the funding deadline. The market resolved YES on Jun 27, the side you held. |  |
| Main | Field label | How this was decided | **NEW 2026-08-19.** Labels the Reading block on Win, Loss and `event-detail-resolved`. Deliberately not `Proof` and not `Verification`: both borrow authority, which principle 5 forbids, and both promise more than one sentence and a link can carry. It names what the block is and lets the reader decide whether it satisfies them |
| Main | Text | Resolved YES on Jun 27, 2026 at 09:14 ET. A federal funding gap began before the Jul 1 deadline the rules named. | **NEW 2026-08-19**, `.reading-line`. Carries the outcome, the instant and the condition in the words the rules used, so the reader compares two sentences rather than a sentence and a hash |
| Main | Text | Source: OMB notice of Jun 26, 2026. Read by the Yonder team at 09:14 ET. | **NEW 2026-08-19**, `.reading-src`, and the source is a LINK. **This is the face for a market only a person can settle**, and the Loss screen carries the other |
| Main | Text | One moment, then move on - no confetti loop. Share is the primary action; "see next events" is deliberately secondary (research F5: the first win, not loss, drives overconfidence and escalation). | **leftover spec-note (internal codes)** |
| Main | Text | Which genre led the 2026 spring box office? | **NEW 2026-08-20**, `win-multi.html`, the multi-outcome win. **The binary screen's sentence cannot be written here**: it says `the market resolved YES, the side you held`, and this market resolved **Animation**, an option the reader never touched, while they won because the option they DID take lost |
| Main | Label | $10.00 stake returned + $11.10 winnings. You held NO on Action, avg price 53%. | **NEW 2026-08-20.** A multi position is an option AND a side, so the figure line names both. `active-bets-history.html` has printed `NO &middot; Action` in its Your side column since the row was written |
| Main | Text | Animation led the 2026 spring box office. You bet that Action would not lead. Action did not lead, so your side paid. | **NEW 2026-08-20**, and the ORDER is the whole design. Winner first, then what you backed, then the conclusion, so the reader is never asked to carry a double negative themselves. Principle 1 (explain the number) and principle 3 (a spectator, not a trader): the trader's version is `NO on Action resolved in the money`, and nobody outside a desk reads that |
| Main | Text | Resolved Animation on Jun 2, 2026 at 11:00 ET. Animation took $412.6M of the spring window against Action at $308.1M, so Action did not lead and NO on Action paid. | **NEW 2026-08-20**, `.reading-line`. A multi reading names the winning OPTION where a binary one names a side, and it carries the reader's option too, because the outcome alone does not say why they were paid |
| Main | Text | Source: Box Office Mojo spring grosses. Read by the Yonder team at 11:00 ET. | **NEW 2026-08-20**, `.reading-src` |
| Main | Text | Share card image, generated here: "Called it - Action would not lead the spring box office. Paid out $21.10 on Yonder." | **NEW 2026-08-20.** The share line says what was CALLED rather than which option won, because the call is the thing the reader got right |

### Loss Screen

_3 state page(s): loss-loading.html, loss-multi.html, loss.html_

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Label | underlying screen dimmed: Active Bets (resolved item) or a tapped resolution notification (G1: 1 tap) | **leftover spec-note (internal codes)** |
| Main | Heading | Here's what happened |  |
| Main | Text | Loading the resolution... |  |
| Main | Label | Fetching what resolved and why. |  |
| Main | Field label | What happened |  |
| Main | Text | The first spot ETH ETFs were approved on Jun 10, 2026, inside the window the market named. It resolved YES on Jun 12. You held NO. |  |
| Main | Field label | How this was decided | **NEW 2026-08-19**, the same label as the Win screen |
| Main | Text | Resolved YES on Jun 12, 2026 at 14:02 ET. A spot ETH ETF approval was published on Jun 10, inside the window the rules named. | **NEW 2026-08-19**, `.reading-line` |
| Main | Text | Source: SEC EDGAR. Read automatically at 14:02 ET. | **NEW 2026-08-19**, `.reading-src`, **the machine-read face, and it is placed on purpose.** Five rules in `yesno.css` once drew a chosen NO that had never stood on an element, so a face the system styles gets a placement or the styling is a claim nobody can test. The words differ from the Win screen's and the drawing does not: a reader should not learn two shapes to check two markets |
| Main | Field label | Result |  |
| Main | Label | $0.00 |  |
| Main | Label | Your $5.00 stake on NO did not return. Avg price 62%. |  |
| Main | Button | Back to your bets | **same-action / go-to-events button varies** |
| Main | Button | Browse events | **same-action / go-to-events button varies** |
| Main | Text | One clear next step, and no "bet again" prompt. The resolution note is shown first so the outcome is understood before any new bet (FJ5 + EJ3: a conscious exit, no impulse to chase). | **leftover spec-note (internal codes)** |
| Main | Text | Which chain held the largest stablecoin supply at the end of H1 2026? | **NEW 2026-08-20**, `loss-multi.html`, the multi-outcome loss, and it exists because principle 4 is `design the loss, mark the win`. Drawing only the winning half of a symmetric control is the mistake the chosen NO cost this repository |
| Main | Text | Ethereum held the largest stablecoin supply when the window closed on Jul 1. You bet on Solana, which finished third, so your side did not pay. | **NEW 2026-08-20.** `which finished third` is the sentence a binary loss never needs: on a multi market the reader wants to know not only that they were wrong but by how far |
| Main | Label | Your $8.00 stake on YES for Solana did not return. Avg price 24%. | **NEW 2026-08-20**, and the phrasing is `YES for Solana` rather than `YES on Solana` so the option reads as the thing backed and not as a venue |
| Main | Text | Resolved Ethereum on Jul 1, 2026 at 00:05 ET. Ethereum held $73.4B in stablecoins against Tron at $61.2B and Solana at $12.8B, so YES for Solana did not pay. | **NEW 2026-08-20**, `.reading-line`, **and this is the Reading's third sentence shape**, the one `docs/backlog.md` 221 filed as an unmade placement before the routing measurement showed it was data rather than a face. A multi machine read compares figures ACROSS options, which a binary read has no way to do |
| Main | Text | Source: DefiLlama stablecoin supply by chain. Read automatically at 00:05 ET. | **NEW 2026-08-20**, `.reading-src`, the automatic face on a multi market. Stablecoin supply by chain is one of the 6 machine-resolvable questions in the catalog census of 2026-08-19 |

### Cancelled event

_4 state page(s): cancelled-loading.html, cancelled-multi.html, cancelled-refund-pending.html, cancelled.html_

**NEW 2026-08-23.** The third outcome. Every line here is written against the two that already
exist, because a reader who has met the Win and the Loss screens must not have to learn a third
shape to check a third thing: same heading rank, same `.fine` question first, same What happened,
same Reading block under a label, same figure box, same two exits.

| Zone | Type | Line | Flag |
|---|---|---|---|
| Main | Heading | This event was cancelled | The other two headings say what the reader's judgement turned out to be, `You were right` and `Here's what happened`. This one cannot: the reader's judgement was never tested. So it states the fact about the EVENT, which is design principle 3 in `CLAUDE.md` - engagement is about events, not money - and the money is the next line down |
| Main | Text | Will the OPEC+ meeting on June 30, 2026 raise output quotas? | user-written content, the event question |
| Main | Field label | What happened | the same label the Win and Loss screens carry |
| Main | Text | The June 30 OPEC+ meeting was called off and no replacement was set before this event closed, so nothing can say whether quotas were raised. The event was cancelled and every stake on it was returned. | Principle 1: explain the number, and here the number is the absence of one. It says WHY nobody could settle it before it says what happened to the money, because a reader who is told their money is back and not told why will assume the platform changed its mind |
| Main | Field label | Why this was cancelled | **The Reading block's third label.** Win and Loss carry `How this was decided` over the same component; nothing was decided here, so the label says what the block actually holds. It is deliberately not `Reason` or `Explanation`: it names the block by the reader's own question, the way `How this was decided` does |
| Main | Text | Cancelled on Jun 30, 2026 at 12:40 ET. The meeting this event named did not take place, so the source has nothing to report for June and no reading can be taken either way. | `.reading-line`. Same shape as the two resolution wordings: the instant, then the condition in the words the rules used. **The clause that matters is `either way`**, because the one thing a reader fears here is that the market was settled quietly against them |
| Main | Text | Source: OPEC press releases. Read automatically at 12:40 ET. | `.reading-src`, the machine-read face, and the source is a LINK, exactly as on the other two. A cancellation with no checkable source is the borrowed authority principle 2 forbids |
| Main | Field label | Returned | the figure box label. Not `Result`, which is the Loss screen's and implies one, and not `Refund` - see the lexicon entry of the same date |
| Main | Label | $8.12 | the stake AND the fee. `PRODUCT.md` charges 1.5% of the stake at Confirm and the panel prints it as `Total to pay`, so `Total to pay` is what left the balance and it is what comes back. A product that keeps the fee on an event it could not settle has charged for nothing |
| Main | Label | Your $8.00 stake on YES and the $0.12 fee are back in your balance. Nothing was won and nothing was lost. | The last sentence is the whole screen. Without it a reader has to work out from a figure whether they came out ahead |
| Main | Button | Back to your bets | same label as the Loss screen's primary |
| Main | Button | Browse events | the lexicon's one label for going to the feed |
| Main | Text | Which OPEC+ member will announce the largest quota increase on June 30, 2026? | `cancelled-multi.html`, user-written content |
| Main | Text | The June 30 OPEC+ meeting was called off, so no member announced anything and none of the four options can be read as the answer. The event was cancelled and every stake on it, on every option, was returned. | **NEW 2026-08-23.** `on every option` is the sentence a binary screen never needs and a multi reader immediately asks |
| Main | Text | Cancelled on Jun 30, 2026 at 12:40 ET. The meeting this event named did not take place, so no member made an announcement and the four options cannot be compared against each other at all. | `.reading-line` on a multi cancellation. The multi RESOLUTION reading compares figures across options; this one says the comparison could not be made, which is the same sentence with its verb taken out |
| Main | Label | Your $6.00 stake on YES for UAE and the $0.09 fee are back in your balance. Nothing was won and nothing was lost. | `YES for UAE`, the phrasing settled on 2026-08-20, so the option reads as the thing backed and not as a venue |
| Main | Text | Loading the cancellation note... | `cancelled-loading.html`, against the Loss screen's `Loading the resolution...`. Names exactly what is loading, which is the Loading rule |
| Main | Label | Fetching why this event was cancelled and what came back. |  |
| Main | Label | Your $8.00 stake on YES and the $0.12 fee. Settling on-chain. | `cancelled-refund-pending.html`, the figure box while the money is still in flight |
| Main | Text | Your stake is on the way | against the Win screen's `Your payout is on the way`. One word differs and it is the only word that can |
| Main | Label | It will arrive in your balance in a few minutes (on-chain settlement delay). Nothing was won and nothing was lost. |  |
| Main | Label | RETURNED | `active-bets-history.html`, the settled row's chip, beside WON and LOST. The bare `.pos-side` face, no outcome colour |
| Main | Label | Cancelled Jun 30, 2026 - tap to see why | the row's status line, against `Resolved Jun 27, 2026 - tap to see your win` |
| Main | Label | Returned | the row's figure column, where a resolved row says `Paid out`. Two labels because they are two different figures: a payout depends on the side you took and a return does not |
| Main | Label | Cancelled | the row's `Result` column, where a resolved row names the outcome |
| Main | Text | Cancelled: "OPEC+ meeting on June 30, 2026" was called off, so nothing can settle it. Your stake is back. | `notifications.html`, the fifth notification type. **The last four words are the reason this is not the `Bet resolved` type wearing different text**: the only alert in the product that reports money coming back |
| Main | Label | Event cancelled, stake returned | the notification's own type label, beside `Bet resolved`, `Odds moved significantly`, `Event deadline approaching` and `New event in a followed category` |

## User-written content (do NOT rewrite)

These lines are authored per event or by other users - event questions, outcome names, the per-event editorial (why-this-price, arguments, resolution notes), share cards, comments, usernames and holdings. Our voice work does not touch them; they get a separate content guideline for whoever creates markets.

**Event questions (titles):**

- Which coin will have the highest market cap on January 1, 2027?
- Which company will reach a $5T market cap first?
- Which genre led the 2026 spring box office?
- Which party will win the most seats in the next UK general election?
- Who will win Album of the Year at the 2027 Grammys?
- Who will win the 2027 Eurovision final?
- Who will win the 2028 Republican presidential nomination?
- Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?
- Did Bitcoin close above $100,000 in the first half of 2026?
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
- Did the US government shut down before July 1, 2026?
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
  **THE REASON HELD FOR TWO OF THEM AND NOT FOR THE THIRD, 2026-08-21.** A stand-in is honest when it stands in for content that is not set. The
  copyright holder IS set: the line already reads `Copyright (c) Yonder.` and `Sample wireframe content` stood in for nothing - it is a label about
  the ARTEFACT, fused to the product's own legal sentence, and it rendered as the last line a reader meets on **221 documents: 119 painted, 100
  grey and 2 in the kit**. The painted tree is not a wireframe, and `wireframes/_conventions.md` declares the differences between the two trees;
  a divergent copyright line is not one of them, so the string leaves both. `about.html` already carries the honest version of what it was trying
  to say, labelled as its own sentence rather than smuggled into the copyright: *"Prototype page. The structure and the copy here are real; the
  figures are sample data from this prototype's own catalog."* The regulatory strip went the same way on 2026-08-20 for the same reason, off 100
  grey documents, and it stood directly ABOVE this one.

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
- **Status chips**: were "execute failed", "amount over balance", "price changed", "submitting", filed here as terse dev-ish state labels and left. **Closed 2026-08-16** as "not sent", "over your balance", "price moved", "sending", because the same pass copied that slot into the mobile sheet and duplicating a known defect is how a defect becomes a convention.

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
| `event-detail*` painted bet sheet (4) | `YES selected` | **`YES pre-selected`** | 2026-08-11, backlog 87. The sheet was the one string in that block with no row in this inventory; the panel five lines above it already said the rowed one. **Superseded 2026-08-16**: the word the two disagreed about was the wrong word for both, because the state it named was a default nobody had decided |
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
| ~~`How the YES price moves as your bet grows. This market runs on an AMM, not an order book.`~~ **REWRITTEN 2026-08-16: `How the YES price moves as your bet grows. Your own bet moves it, so a bigger bet buys at a worse average price.`** | `.md-sub`, 9 screens per tree | The old row claimed principle 1 and principle 3 and it broke both. **The reason it gave, "an order book is what a trader would assume", names the one reader principle 3 says not to write for**, and the one `PRODUCT.md` excludes in a line of its own: "NOT a trader terminal: no order books". To the spectator both halves are unknown words; to the trader the sentence is redundant: **a sentence with no reader.** And the lexicon exemption that allowed the term has a second half, "where it is glossed in plain words", which was never met: `AMM` stood on 9 screens per tree and was glossed on none. The new line says what the table under it proves, in the voice How It Works already uses for the same mechanic |
| `Bet` / `Avg YES price` / `You receive if YES` | `.md-row-head` | column heads in the lexicon: bet, not position; receive, not payout |
| `Rules` / `Market Context` | `.rules-tab` | two tabs, because what decides the outcome and what explains the odds are different promises. See the note below |
| `Background from the Yonder team to explain the odds. It plays no role in how this market resolves.` | `.rules-note` | the sharpest line of the redesign: it exists so the context tab can never be mistaken for the resolution rule |
| `Not just news.` / `Opinions have value.` / `The market decides.` | `.brand-tile` | principle 5: three specific claims, no superlative |
| `Every outcome is public and verifiable.` / `1,284 events resolved against a named source` | `.hero-trust` | principle 2: one plain sentence of trust, with a number that can be checked. **The second half read `resolved on-chain` until 2026-08-19, 4 placements**, and it named the ledger the record sits in rather than the thing the record is checked against. The row below records that this figure was already corrected once for giving a number without saying where; this is the same correction applied to WHERE |
| `Back YES` / `Back NO` | `.hf-btn`, the featured hero | the hero is the one place the verb is written out; the cards keep bare `YES` / `NO` |
| `Hot right now` / `See all hot events` | `.hh-head`, `.hh-all` | a heading and its exit, per the empty-state rule that every block gives a way out |
| `YES probability, last 30 days &middot; volume below, no scale` | `.hf-chart-cap` | says what the chart is measuring, over what window, and what the second series is NOT. It read `Live odds &amp; volume &middot; last 30 days` until 2026-08-16, which named both series and gave the reader no way to tell that only one of them has an axis |
| `70%` `60%` `50%` `40%` `30%` | `.hf-axis` | the chart's scale, `aria-hidden` because the SVG beside it is. New on 2026-08-16: the four ruled lines it replaces stood at 68.05, 55.38, 42.72 and 30.05 per cent, which is a scale nobody could read a value off |
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
| `1,284 events resolved` | `1,284 events resolved` + ~~`On-chain, verifiable.`~~ `Every reading is published.` | principle 5 again: the number was already checkable and never said where. **The qualifier was turned 2026-08-20**, on 223 placements: `docs/backlog.md` 217 moved every resolution claim off the chain and onto the Reading, and this tile was the one it did not reach, because it proves a RESOLUTION count with a chain on the same page About now states the mechanism at length. `On-chain, verifiable.` survives only in the frozen `ui-visual/old/`. The tile beside it already says *against a public source*, so the new qualifier had to be the thing neither of the other two says |

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
| `Liquidity` | `Available to bet` | `.ms-label` beside its figure, 8 per tree since 2026-08-17, when the resolved state stopped claiming anything was available | a figure read to decide. The panel it stands in IS exempt, for EXPLANATION, and a naked number explains nothing, so it also fails principle 1 |
| `Market` | `How the odds are set` | the `<summary>` of the collapsed panel, `.market-title`, 8 per tree since 2026-08-17, the resolved state saying `were` instead | the head of the exempt block. It is read by everyone who never opens the panel, and it now says what is inside instead of naming the mechanism |
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

### 2026-08-16 - one fee, one payout, and a line the panel had never had

Ordered by the `/impeccable critique` of the painted product, P0: the same $5 bet was described by
three surfaces as three incompatible products, and the sweep below is what it took to make them one.

| Surface | Said | Says |
|---|---|---|
| Bet panel, computed | `Fee (1.5% of your bet) $0.07` at Confirm | `Fee (1.5% of your bet) $0.08`, and a new `Total to pay $5.08` under it |
| How It Works | "a small fee only when you win - never on a losing bet" | 1.5% of the bet, added at Confirm, the same win or lose |
| Wallet ledger | `Platform fee (won bet) -$0.40`, dated at the resolution | `Platform fee (1.5% of stake) -$0.38`, dated at the bet and standing beside it |

**The payout figure was a fourth answer and nobody had counted it.** `$13.20` stood on **298
occurrences across three trees** (231 painted, 46 kit, 21 grey) while the price beside it said 38%
and the arithmetic says `5 / 0.38 = 13.16`. The reconcile panel had both in one sentence: "Payout
$13.20 -> $12.20", where the second figure is `5 / 0.41` to the cent and the first is not `5 / 0.38`
at all. It is `$13.16` everywhere now.

**The static markup was the version that shipped when the script did not.** All eight bet panels
carried `$0.40` and `$13.20` in the HTML, and only a page script rewrote them; the four screens with
no script, and any screen whose script failed, showed the retired model with nothing to say so.

**The rounding is the reason `Total to pay` needed a decision rather than a sum.** 1.5% of $5.00 is
7.5 cents. A fee taken raw prints `$0.07` and a total taken raw prints `$5.08`, so the two numbers a
person can read do not add up. The fee is rounded to cents FIRST and the total is built out of the
rounded fee: `$0.08` and `$5.08`. The fee that is charged is the fee that is shown.

**Not touched, and this is the half that keeps it honest.** The historical pass records above
(Krok 6, the `voice_reconcile` route, the "Kept (already on-voice)" lines) still name
`Platform fee (won bet)`, "fee only when you win" and "Prices move with the market (AMM)" as kept.
They were true when written and they are the record of a decision, not a claim about today. The
inventory tables above are the source of truth and they are what moved.

## 2026-08-16 - a caption that named two series and gave the reader no way to tell which one has an axis

The palette pass changed two strings and added five, and all seven are about the same thing: the
hero chart draws a probability and a volume in one box, and only one of them can be read off a
scale.

| Was | Is | Why |
|---|---|---|
| `Live odds &amp; volume &middot; last 30 days` | `YES probability, last 30 days &middot; volume below, no scale` | The old line named both series as if they were one reading. `Live odds` is also vaguer than the chart: what is drawn is the YES probability, and the NO curve is its mirror. `no scale` is the part the product owes the reader, because the volume ribbon has none and a caption that stayed silent about it would let the new numerals vouch for it |
| (nothing) | `70%` `60%` `50%` `40%` `30%` | The chart had four ruled lines standing at 68.05, 55.38, 42.72 and 30.05 per cent. A scale nobody can read a value off is a claim, so the lines are re-keyed to the decades and the decades are written down. `aria-hidden`, because the SVG they label is |

**The pass changed no other copy**, and the two lines it was tempted to are worth naming. *YES* and
*NO* on the buttons stayed exactly as they are: the pass took the colour off the ground and left it
in the word, so the word is now carrying more than it was and rewriting it would have been the
opposite move. And the `Vol` legend tag stayed three letters, because it labels a swatch beside two
other three-to-seven character tags and the caption underneath is where the sentence goes.

## 2026-08-16 - the minor observations, and two of the six were the source rather than the page

The pass after the palette one, working the `/impeccable critique`'s Minor Observations and its
accessibility red flags. **Seven strings changed and 48 are new**, and every one of them was read
out of the accessibility tree rather than out of a file.

| Was | Is | Why |
|---|---|---|
| `thumbnail placeholder` inside every `.thumb` and `.ed-thumb` in the paint | nothing | The photography boundary is declared in `wireframes/_conventions.md`: grey draws the empty box, the paint carries the picture. The grey tree's LABEL for that box had been copied into the paint with it, where `color:transparent;font-size:0` hides it from the eye and leaves it standing in the tree. Measured on `event-feed.html`: **24 `StaticText "thumbnail placeholder"` nodes, none of them ignored**, one beside every event question on 105 screens. It stays in the grey tree, where it is the label of a box that has no picture, on 21 files |
| `aria-label="Language (placeholder)"` | `aria-label="Language"` | The label overrode the visible word `English` with the bookkeeping the wireframe uses to mark an unbuilt destination, and it reached only a screen-reader user, so it was not even doing the wireframe's job. The two menus beside it read `Sort by` and `Filter by how often an event repeats`, so this is the peer form, not a new one. 197 places in three trees |
| `<nav class="footer-col" aria-label="Markets">` over `<h2>Events</h2>` | `aria-label="Events"` | The other two footer columns agree with their headings, `Product` over Product and `Support` over Support. This one disagreed, and the word it disagreed with is the one the lexicon forbids: a landmark named `Markets` sat over a column visibly headed Events, and the sighted user and the screen-reader user were told different things |
| `Transak payment widget (card to USDC)` | `The payment widget loads here (card to USDC)` | Not a placeholder in the unfinished sense: `.widget-box` is a declared component and `ui-kit/notice.html` calls it "the slot a third-party payment widget will load into". What was wrong is that a slot was speaking in a noun phrase written for whoever was building it. It is a sentence now, and it uses `payment widget`, which is the term the loading line and the failure screen already settled on |
| `Share Card: "Called it - ..." (image placeholder)` | `Share card image, generated here: "Called it - ..."` | Same slot, same fix, and the parenthesis was the whole defect: the line already said `Share Card:` and the field above it says `Share Card (auto-generated)`, so the bookkeeping word was the third time in one block |
| (nothing) | `Loading events`, `Loading your open bets`, `Loading your settled bets`, `Loading this event`, `Loading the bet panel`, `Loading your profile`, `Loading this profile`, `Loading your track record`, `Loading this track record`, `Loading your wallet`, `Loading your transactions`, `Loading your notifications`, `Loading your saved events` | **48 new lines, one per busy region across the two screen trees.** 19 of 19 loading screens set `aria-busy` and said nothing: `aria-busy` is a property of a region, not a message, so 42 pulsing rectangles were the entire signal to anyone who could not see them. Each line names what is loading, and it is `role="status"` on its own `<p>` rather than on the region, so a screen reader gets one sentence instead of twelve event cards the moment the skeletons are replaced |

**Two of the six observations were readings of the source and not of the page, and both are recorded
rather than fixed.** The critique reported 4 of 22 SVGs on `how-it-works.html` with no `aria-hidden`
and no label; read out of the accessibility tree, **all four are ignored**, with
`ariaHiddenSubtree` as the reason, because their parent `<span class="hiw-ic" aria-hidden="true">`
covers them. And the deposit slot is a documented component rather than unfinished work. The
thumbnail label went the other way: the SPAN is ignored as uninteresting and its TEXT NODE is not,
which is why querying the element said clean and querying the tree said 24.

## 2026-08-17 - the search surface, and five strings for a control that used to be a page

Search moved from a destination to a control on 2026-08-17: below the RAIL rung it is a sheet over
the screen, at the rung and above it is a field in the header. **The copy that already existed did
not move an inch** - the placeholder, the clear label, the count and the no-match block are the same
words in a different container, which is the test a voice inventory is for. Five strings are new and
every one of them is a LABEL over a group rather than a sentence, because a surface a person opened
on purpose does not need to be told what it is.

| String | Where | Why |
|---|---|---|
| `Cancel` | `.search-cancel`, the sheet's way out | A word and not a cross. The sheet is the whole screen, and a cross at the top of a full-bleed surface is the one control people read as "close the app". `Cancel` says the search is abandoned and the screen underneath is still there |
| `Categories` | `.search-group-label` over the five tiles | The word the product already uses for this rail: `aria-label="Categories (second level)"` on the feed, `Categories` in the sidebar group. **Not `Topics`** and not `Browse`, which would be a second name for a thing that has one |
| `Popular right now` | `.search-group-label` over the pre-query rows | It says WHY these four and not four others, which `Suggested` and `For you` do not: the four are the highest volume in the catalog, and volume is the one popularity figure this product prints anyway. It is also a sibling of `Hot right now` in the hero, deliberately: the same claim, one surface quieter |
| `Results` | `.search-group-label` once a query is typed | The idle groups go and this one arrives, so the label is the whole announcement. One word, because the count is already in the seam below |
| `See all 3 results` | `.search-seeall`, the seam to the results page | The number is the point. It is what decides whether a person needs the page at all, so the count is IN the link rather than beside it, and the singular is written: `See all 1 result` |

**The one string this pass deleted a reason for.** `12 events, every one currently open` is still the
idle count on the search page, and it is now the only place that sentence stands: the surface's own
idle state shows categories and popular events instead of a number, because a person who has just
opened a search has not asked how many there are.

## 2026-08-16 - the search screen, and a deferral re-opened rather than a gap filled

Search is not new copy on an old screen: it is a destination the IA had **decided against**, with a
condition attached. `ia/docs/sitemap.md` read "Search - Deferred until catalog scale. At 10-20
curated markets, users scan the Event Feed; they do not search." Measured before anything was
written: **the product draws 25 distinct events**, so the premise moved from 10-20 to 25 and was not
overturned by scale. What overturned it is reachability, which the 404 had been arguing in the
markup for as long as it has existed.

| String | Where | Why |
|---|---|---|
| `Search events` | `.icon-btn` in the header on 105 of 105 screens, and the `<h1>` of the search page | The same three words name the way in and the place it leads. The verb is `Search` and the noun is `events`, never `markets`: the lexicon is the same here as everywhere |
| `Search events` | `.search-input` placeholder and its `aria-label` | The placeholder is the label rather than a hint, because the field has no visible label above it and a placeholder that vanishes on the first keystroke cannot be one on its own. Both carry the same words so nothing is announced that is not also drawn |
| `Clear the search` | `.search-clear` | Not "Clear" alone: a screen reader hears this control out of context, and what it clears is the query rather than the results |
| `12 events, every one currently open` | `.search-count`, empty field | The idle count is doing two jobs. It says how many there are, and it says what "all" MEANS here: this list is the open events, not the 1,284 the footer strip has resolved. Those two numbers sit on the same page and count different things |
| `2 events for "election"` | `.search-count`, a query with matches | The figure is computed from the same pass that hides the cards, so the number and the grid under it cannot disagree. The singular is written: `1 event`, never `1 events` |
| `0 events for "tennis"` | `.search-count`, a query with none | Zero is stated in the same sentence as any other number, because a search that finds nothing is an answer and not an error |
| `No events match "tennis"` | `.state-title` on the no-match block | It names the query back, so a person who mistyped can see what was actually searched for |
| `Yonder runs a curated list, so the event you want may not be open yet. Try a shorter word, or browse a category.` | `.state-msg` | Principle 1, explain rather than apologise. **The honest reason for an empty result here is the product's own shape**: 25 curated events, not a search that failed. The two suggestions are the two things that actually work |
| `Browse all events` / `How events are chosen` | `.state-actions` | The empty-state rule: every block gives a way out, and this one gives two, because "there is nothing here" has two different questions behind it |
| `Search events` | the 404 quick-link list | The page has drawn a magnifier over "This page does not exist" since it was written, and `ia/docs/pages/system.md` has named its escapes as "search or quick links" for just as long. It shipped the second half only |

**The one string this pass did not write is the one it was most tempted to.** There is no "no
results found" and no "we could not find anything": the count line already says `0 events for
"tennis"` in the product's own arithmetic voice, and a second sentence saying the same thing in a
softer one would be the apology this product's voice does not make.

## 2026-08-16 - no new strings, and half the ones the visitor needed moved 3,249 pixels up

The logged-out trending feed was missing the hero band that carries the product's own proof, so
every string in it was written, inventoried and shown only to the reader who had already signed in.
**No copy was written or changed in this pass**; the rows for `.hf-eyebrow`, `.hf-title`, `.hf-why`,
`Back YES` / `Back NO`, `Hot right now`, `See all hot events`, the two `.hero-trust` claims and the
three `.brand-tile` lines now stand on two screens instead of one, and the count in each of those
rows is the only thing about them that moved.

**What that is worth, measured**: "1,284 events resolved on-chain" sat at y=4,095 on a phone for a
visitor and at y=846 for a signed-in reader. It is at 846 for both now. "Your USDC is held 1:1" went
from 3,885 to 748. **A sentence written to convince somebody who has not signed up was below three
and a half thousand pixels of scroll for exactly that person.**

## 2026-08-16 - six new strings, and five of them are one word the product already says

The breadcrumb (`crumb`) landed on three page types. Every string in it is a name the product
already uses somewhere, which is the point: a trail that renames the place it points at is a trail
that teaches a second vocabulary.

| string | where | note |
|---|---|---|
| `Home` | every crumb, the first item, the only link in the trail on all six screens | **Not "Events" and not "Yonder".** The bottom-nav slot is `Events` and the logo says `Yonder`, and both of those go to the same feed, so a third name for one destination would be the fee's three-products defect in miniature. `Home` is the word a breadcrumb has, and `ia/docs/pages/seo.md` writes the trail with it: `Home > {Category} > {Event}`. It is the IA's word, taken rather than invented |
| `How it works` | the crumb on `how-it-works.html` | Sentence case, and the `<h1>` above it reads `How It Works` in title case. **That difference is deliberate and it is one this repository has ruled on before**: a crumb is a location in a sentence, a heading is a name. The IA writes the trail in sentence case at `seo.md` line 298 |
| `Legal` | the crumb on `terms.html`, middle item | Text, not a link, because the product has no legal index screen: three of the four legal pages do not exist yet. The word is the IA's (`Home > Legal > {document}`, `seo.md` line 464) and it is the same word the footer's fourth nav column carries, so a reader who follows the footer arrives where the crumb says they are |
| `Terms of Service` | the crumb on `terms.html`, last item | Identical to the `<h1>`, and this one IS title case because it is the document's NAME rather than a place |
| `crypto_dan` | the crumb on `public-profile.html`, last item | The handle, per the IA's `Home > {handle}`. **A datum, not a string**: it changes with the profile and it is the same value the identity row already prints |
| `Profile` | the crumb on the three public-profile states where the handle is not known yet | Loading, error and not-found. The trail still has to end somewhere, and ending it on the h1's word is the only answer that does not invent a placeholder |
| `Breadcrumb` | the `aria-label` on the `<nav>`, all six screens | Never seen, and it is the landmark's name. The separator is drawn with `li + li::before` for the same reason a label is not typed: a `/` written as a text node reads as part of the next link and would need a row of its own here for a character nobody wrote |

**The count line and the trail now say the same thing in two places on `terms.html` and that is not a
duplicate.** The crumb says where the page sits; the 14-item table of contents says what is inside
it. A person who arrived from a search engine needs the first before the second.

## 2026-08-16 - one string rewritten, and the exemption that protected it had a condition nobody had measured

`AMM` and `order book` stood in one line, `.md-sub` under "Price by bet size", on **9 event-detail
screens per tree, 20 occurrences across the three trees**. The critique of the same morning called it
the only sentence in the product that assumes prior knowledge, standing on the screen where money is
committed. Three things were measured before a word was changed, and each one moved the answer.

**One: the lexicon did not forbid it, and the exemption has two halves.** `voice.md` bans trader
terms by PLACE rather than by word, and allows them "inside a block whose whole job is to explain the
mechanism, **where it is glossed in plain words**". The first half was quoted every time this line
came up. **The second half was never checked.** `AMM` was named on 9 screens per tree and glossed on
none, here or anywhere else in the product.

**Two: the example the rule gives for the legitimate place does not exist.** `voice.md` illustrates
the exemption with "*AMM* in the How It Works explanation is the mechanism being named". Measured:
`how-it-works.html` contains the string `AMM` **zero** times, in either tree. The term lived only in
the place the exemption did not reach and was absent from the one place the rule holds up as correct.

**Three: the reason this row itself gave names the wrong reader.** It read "says what it is NOT,
because an order book is what a trader would assume". Principle 3 is "speak to a spectator with an
opinion, **not to a trader**", and `PRODUCT.md` spends a line of its own on it: "NOT a trader
terminal: no order books". To the spectator the sentence is two unknown words; to the trader it is
redundant. **A sentence with no reader.**

**And the explanation the product needed was already written, four sections away.** How It Works
says: "Prices move as people bet. You buy YES or NO at the price on screen, and that price is locked
when you confirm. A winning share pays one dollar, so a lower price buys more shares and a larger
payout." Plain, complete, no term. So the caption did not need to name a mechanism; it needed to say
what its own table proves.

| was | is |
|---|---|
| `How the YES price moves as your bet grows. This market runs on an AMM, not an order book.` | `How the YES price moves as your bet grows. Your own bet moves it, so a bigger bet buys at a worse average price.` |

The table below it reads $10 at 38 per cent, $100 at 39, $1,000 at 42, $5,000 at 49. **The new second
sentence is the caption of that column and the old one was a footnote about the engine.** `AMM` and
`order book` now read **0 in `ui-visual/`, 0 in `wireframes/`**, and in `ui-kit/` only inside
`market.html`'s prose about this decision. `ia/docs/` keeps its 9: those are the spec naming the
mechanic to its own writers, which is what a mechanics document is for.

### 2026-08-20 - the five document pages get the lede they were banked with, and About stops describing itself

`ia/docs/blocks.md` B3 is **H1 + a one-line lede in the product voice, saying what this document
decides for the reader**, banked MVP for BOTH body profiles. **It stood on 0 of the 5.** All five
went H1 straight into the prototype notice, so the row filed against `about.html` was reading one
page where the defect was the set, which is the same shape as the auth convention nineteen pairs of
twenty obeyed. `docs/backlog.md` 214.

| page | lede |
|---|---|
| About Yonder | Yonder is where an opinion about what happens next becomes a bet you can be paid for. |
| Terms of Service | What you agree to when you back an event here: your account, your funds, how an event resolves, and what happens when something goes wrong. |
| Privacy Policy | What we collect, why we collect it, who else sees it, and how you get it back or have it deleted. |
| Cookie Policy | Which cookies this site sets, what each one is for, and how to turn off the ones it does not need to run. |
| Responsible betting | The limits you can set on yourself, the signs worth watching for, and where to get help that is not us. |

**On About that line is also B15, the statement hero.** The bank asks B15 for "what the product is,
in one sentence", and B3 for what the document decides; on the page whose subject IS the product
those are one sentence, and two of the same rank stacked under one H1 is what rule 1 of that bank
throws out. The content rule survives the merge intact: **a sentence about the reader's job and not
a mission statement about the company**, which is the discipline the event card's story line already
follows.

**The body was five sections describing what each section would say.** Every paragraph began "This
section states" or "It exists because", which is a page about a page. The four that stayed say the
thing: what a prediction market is and who it is for, how an event resolves and what happens when the
source fails, where the balance sits and what is never done with it, and the three numbers.

**`#regulation` came off, and it is the only section here that was in neither source.** It is not in
the block bank and not in the STATEMENT H2 list of `ia/docs/pages/seo.md`; B14 puts a region note on
the DOCUMENT profile and marks it LATER; and `PRODUCT.md` carries **Jurisdiction: `[?]`**, so a
section stating which jurisdictions the service is offered in could only ever have been the
placeholder it was. Removed rather than rewritten, and recorded so the next reader finds the decision.

| block | line |
|---|---|
| B17 figure | `1,284` events resolved since launch |
| B17 figure | `25` events open right now |
| B17 figure | `2` challenged and re-read |
| B17 | Volume is the number this category leads with. It says how much money moved and nothing about whether anyone was paid, so it is not here. |
| B19 | **Browse events** - the lexicon's one label for going to the feed. It routes to the feed and not to signup, which the bank rules out by name on a page about the company |
| B21 | Prototype page. The structure and the copy here are real; the figures are sample data from this prototype's own catalog and are not a record of anything that happened. |
| B10 | A question about Yonder goes to hello@yonder.example, which is not product support. A reply is sent within five working days. |

**B21's wording had to change because the old one was now false.** It said the body text "describes
what each section would decide and is not an operative legal term", which is still exactly right on
the four legal pages and wrong on About the moment About says something. The four keep it; About
carries the version above, and what is unproven there is named precisely: the figures.

**B10's address changed with it.** `legal@yonder.example` is right for a question about a term and
wrong for a question about the company, and B10 is "the one address for a question about THIS
document".

**One concept, one word, checked after writing rather than assumed.** The first draft of this copy
said *settle* eleven times beside a heading reading *How an event resolves*. The Lexicon in
`voice/docs/voice.md` allows **resolve / resolution** and does not list *settle*, so 12 placements
were turned. It is the same-thing flag this file exists to catch, produced by the person holding the
file.

### 2026-08-20 - the panel prices the bet in the box, and one line appears only when it moved

`docs/backlog.md` 216 said there is no maximum bet and the locked-price promise gets more expensive
with every dollar of one. Both halves are answered by the same change and neither answer is a limit:
**the price offered is the price of the bet being placed**, so there is no size at which the promise
costs anything and nothing depends on a ceiling. `PRODUCT.md` Liquidity and risk, `docs/decisions.md`
2026-08-20.

| zone | type | line | note |
|---|---|---|---|
| Bet panel | Label | Your price | **New 2026-08-20.** One `.line` above `Fee`, written by the script and removed by it. It stands ONLY where the amount moved the quote, because a row restating the number on the button three inches above it is a second answer to a question already answered. At the $5 default it never appears: measured at `b = 1000` against every price the shipped catalog carries, the size-adjusted quote rounds to the same whole per cent as the market quote on **19 of 19**, and it first differs at $25 by one point |

**No string was retired and that is the finding.** `$1 minimum, no maximum. The price you see is the
price you get.` stands on 24 placements and stays true word for word, and so does the market block's
`The price is locked when you confirm, so it cannot move against you between the panel and the bet.`
**`docs/backlog.md` 211 quoted that sentence without its last clause** and deleted a face on the
reading, and the clause it dropped is the one that scopes the promise to an INTERVAL rather than to
size. A price computed for your stake, shown to you and then held is exactly what the line
guarantees.

| was | is |
|---|---|
| `The price is locked when you confirm, so it cannot move against you between the panel and the bet.` | ...unchanged, **plus** `Your own bet moves the price, so the panel quotes the amount in the box and locks THAT number, not this one.` |

**26 placements, both trees plus the stand.** It is the same idea the deleted ladder's own caption
carried, *Your own bet moves it, so a bigger bet buys at a worse average price*, said in the block
that ships rather than in a table that did not, and now the panel actually does it.

**One screen draws the line and it is the one whose job is what you are about to pay.**
`event-detail-bet-ready.html` went from the $5 default to **$25**, the largest amount the panel's own
quick chips offer, in both trees: `Your price 39%`, `Fee $0.38`, `Total to pay $25.38`,
`If YES wins, your side $64.10`. **Every figure divides**, because the quote is rounded to the
displayed whole per cent first and the payout is the stake over that: 25 / 0.39 = 64.10. A number that
does not divide is a number that was not explained, which is `voice/docs/voice.md` principle 1.

### 2026-08-20 - the four legal pages stop describing themselves, and two of the product's own surfaces had to move first

`docs/backlog.md` 228. Every section of `terms`, `privacy`, `cookies` and `responsible-betting` read
*"This section describes X"* and then *"It would also state Y"*: a specification of the copy standing
where the copy goes. **47 sections are written**, from what this repository has already decided and
from nothing else. 2,168 words on Terms, 1,505 on Privacy, 925 on Cookies, 1,284 on Responsible
betting.

**This is a draft for review, and B21 says so rather than pretending otherwise.** The wording had to
change because the old one became false the day the sections said something.

| was | is |
|---|---|
| Prototype page. The section headings, the structure and the dates are real; the body text describes what each section would decide and is not an operative legal term. Nothing on this page is in force. | Draft for review. The structure, the headings and the dates are real, and the wording below is a first draft written from what this product has already decided rather than an operative term: it has not been through legal review and nothing here is in force. Where a fact is not settled yet, the section that needs it says so. |

**Three facts are open and the sections that need them say so** rather than inventing an answer: the
operating entity and its registered address (Terms 2), the law that governs a dispute (Terms 13), and
the list of excluded regions (Terms 8). `PRODUCT.md` carries **Jurisdiction: `[?]`**, and this is what
that costs on the page a reader actually reads.

**Two headings changed, and a heading on these pages is in THREE places.**

| was | is |
|---|---|
| `4. The limits you can set` | `4. Limits, and what to do while there are none` |
| `6. Closing your account` | `6. Closing your account, and self-exclusion` |

`responsible-betting` sections 4, 5 and 6 described a deposit ceiling, a loss ceiling, a cooldown and
self-exclusion as if a reader could reach them. **`ia/docs/sitemap.md` marks the whole Responsible-play
slot reserved, post-MVP, not built.** A page about self-protection that lists controls nobody can
reach is the worst version of that page, so section 4 opens with **Account limits are not built yet**,
says what the asymmetry will be when they are, and gives the two things a person can do today: a limit
at the bank, or a freeze by writing to us that we will not lift early. The lede changed with it, from
*The limits you can set on yourself* to *What this can cost you*.

**The heading lives in the `h2`, the section's `aria-label` and the contents row, and the first pass
reached two of the three.** `ia/docs/pages/seo.md` said a section in the body and not in the contents
is impossible BY CONSTRUCTION; both lists are hand-written and nothing reads one against the other.
Rendered and compared: **94 contents rows against 94 headings over four documents and two trees, 0
disagreeing.**

**And the Cookie Policy could not be written truthfully while the banner contradicted it.**

| where | was | is |
|---|---|---|
| `cookie-consent.html`, both trees | a third category, **Marketing**, *Used to show you relevant campaigns. Off unless you turn it on.* | removed |

Section 5 of that policy commits that **no advertising and no cross-site cookie is set**. The banner
offered a toggle for cookies this product does not set, that `PRODUCT.md` has no surface for, and that
`ia/docs/sitemap.md` never specified: it banks the banner as *prior opt-in, reject as easy as accept,
no pre-ticked, reopen from footer* and never as three groups. **A choice about a thing that does not
exist is a choice about nothing.** It returns as a NEW category, which section 9 of the same policy
says resets the reader's answer rather than carrying it forward.

### 2026-08-20 - the lexicon read against the render for the first time, and the two biggest hits were a word this file bans and a rule three lines above it

**Every rule in `voice/docs/voice.md` is a claim about words a person MEETS, and nothing had ever
read the words a person meets.** Rendered over 239 product documents, **38,748 text nodes**, the grey
tree's declared annotation faces and user-written comments excluded, every hit classified by whether
the reader is ACTING (a control, a heading, a figure read to decide) or being explained to, with the
probe proved against a planted `Oops, buy shares in this market (T2)` before any number was believed.

**Six distinct strings where a person is acting. Two remain and both are the category naming itself.**

| was | is | placements | why |
|---|---|---|---|
| `Portfolio` | **`Balance`** | 296 | The lexicon bans it by name and it was the label on the desktop money pill, the profile summary, the swap control's accessible name and the script that swaps them. `Cash` and `In-play` were already the product's own words; only their SUM wore the trader's. |
| `Portfolio` (bottom-nav slot 4) | **`Profile`** | included above | The other three slots name a destination. This one named a figure and routed to `my-profile.html`. |
| `Portfolio total` | **`Balance`** | 4 | On the profile, beside `Cash` and `In-play`, which stay. |
| `Your payout settles at the price you took` | **`Your payout is fixed at the price you took`** | 219 | `resolve / resolution` is the allowed word; *settles* reads as the event resolving when it means the payout is computed. The largest string in the product after the how-it-works step. |
| `All your bets are settled` | **`All your bets have resolved`** | 2 | |
| `Your settled bets are in the History tab` / `will appear here` / `Loading your settled bets` | **`resolved`** | 6 | |
| `Settled` (market stats) / `How it settled` | **`Resolved`** / **`How it resolved`** | 8 | |
| `It settles on its own, and when it closes...` | **`It resolves on its own...`** | 4 | Written on 2026-08-20 and turned the same day. |
| `KYC is required to add funds by card; crypto-only users can connect a USDC wallet instead.` | **`...; if you fund only with crypto you can connect a USDC wallet instead.`** | 240 | The address rule: always **you**, never **users**. It is stated three lines above the lexicon and had never been measured. |
| `paid $1.00 a share` | **`paid in full`** | 2 | `shares` and `cents` pricing are the desk's words. Written the same day and caught by the sweep that followed it. |
| `Ethereum paid one dollar a share and the other two paid nothing` | **`Ethereum paid in full and the other two paid nothing`** | 4 | |
| `How a market resolves` (About) | **`How an event resolves`** | 2 | `market` for the EVENT, on a chip, two blocks below a heading that says *event*. |
| `a separate market with its own threshold` / `swept between markets` | **`event`** / **`events`** | 8 | Same slip, same day, mine. |
| `the card on-ramp inside the deposit flow` | **`inside Add funds`** | 4 | `Add funds` is the lexicon's word and it is what the screen is called. |

**And the grey footer carried a placeholder standing directly under the line that replaced it.**
`[Regulatory / licensing line - placeholder, to be set...]` stood on **100 grey documents and 0
painted ones**, below `Prediction markets involve risk of loss. Not available in restricted regions.`
So the two trees said different things in one slot and the grey one said both. What it carried that
the shipped line does not is in `PRODUCT.md` Financials and compliance and in `terms.html` section 8,
and its own words were *to be set*, which `PRODUCT.md` now answers with a decider and a trigger.

**Three classes came back and are KEPT with the reason, so the next sweep does not re-open them.**
*A prediction market* is the category naming itself, and the ban is on `market` for the EVENT.
*A YES share costs 38 cents and pays $1 if the event happens* is the exemption working exactly as
written: a mechanism block that glosses the term in the same sentence it uses it, which is the
condition that exemption carries and which nothing had ever satisfied before. And *past deadlines
settled late* is ordinary English about politics rather than this product's resolution.

---

## 2026-08-21 - reading every page as a reader, which is the one instrument that had never been built

Every check in this repository renders a page and asks whether it is CORRECT. This pass asked what a
person reads, straight through, in reading order, across the whole product: **120 painted documents
rendered with every `<details>` and `<dialog>` opened, 1,727 text blocks, 339 of them distinct once
the repeated chrome is collapsed.** Six findings, and **not one of them is visible to any renderer**,
because every one of them renders perfectly.

| what a reader met | where | fixed to |
|---|---|---|
| `Copyright (c) Yonder. Sample wireframe content.` | **221 documents**, the last line of every page | `Copyright (c) Yonder.` |
| the thumb bar's balance `$132`, formerly `$142` | **149 documents** at 390, against `$132.00` on 5 | `$132`, which is what Wallet derives |
| `Price now 41% / 78% / 54%` on My Bets | 1 painted, 1 grey, 6 kit specimens | `38% / 61% / 67%`, the prices the rest of the tree prints |
| `On-chain proofs 100%` under *every figure here is a count* | `how-it-works` in three trees | `Open right now 25`, the set `about.html` already publishes |
| `New in Crypto: "Will ETH flip BTC by 2027?"` | 6 placements, an event held by 0 other documents | a Crypto event the catalog actually opens |
| `Closing soon ... closes in 6 hours` against `Closes: Jul 1, 2027` | 4 documents against 13 | **not fixable as copy**, filed as `docs/backlog.md` 231 |

**The balance is the sharpest of the six and it is the repository's own rule arriving again.** A
reader's balance is one entity, and `wallet.html` derives it: *Balance = Cash + In-play*, `$92.00 +
$40.00`, and the three open stakes on `active-bets.html` sum to exactly `$40.00`. **The derived
number stood on 5 documents and the undecided one on 149.** The header pill was corrected to
`$132.00` on 2026-08-20 and the thumb bar three inches below it was not, which is what happens when a
fact is corrected where somebody remembered rather than over its set.

**And the set read found four more that reading alone would have missed.** Every `.pos` row in all
three trees, keyed on its question: **`ui-kit/position.html` carried a `$10.00` stake at a `45%`
price that appears nowhere in the product, a WON Bitcoin row wearing the SHUTDOWN market's `+$13.16`,
and two rows labelling `Your side` twice where every sibling labels side and result.**
`position-list.html` and `patterns.html` put one product row - the UK election, NO on Conservatives -
under **two different market names, neither of them the UK election**, and flipped a YES to a NO.
**Every value in the position set now agrees across the three trees**, checked by grouping every row
by its question and requiring one distinct reading, with the two surviving groups being a compact
face that carries fewer figures rather than different ones.
