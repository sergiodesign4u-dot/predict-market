# Behaviour

What this product DOES: the flows a person walks, the states each surface can be in, the edges that
recover from a failure, and the rules a field enforces. It is the one thing no page in this
repository answers, because a page renders a state and cannot tell you what reaches it or what it
reaches.

**It describes; it does not decide.** Every row carries the source that already said it. A row with
no source is not written here at all - it is in **NOT DECIDED** at the foot of this file, addressed
to the person who owns it. Behaviour is exactly where a spec with no source produces a plausible
median, and a median is indistinguishable from a decision by eye.

**It references and never duplicates.** No colour, no pixel figure, no interface string and no CSS
appears below. A control is named as its component and variant; a string is addressed by its place
in the copy inventory; a figure is addressed by the file that owns it. A value copied here would
show yesterday's truth with a confident face inside a week.

---

## How to read a row

**Three sources, and only three.** Every row cites at least one:

| Tag | Source | What it proves |
|---|---|---|
| **S1** | the screen file in `ui-visual/` | the state EXISTS as a drawn surface, at a named file |
| **S2** | `ia/docs/flows.md` | the transition EXISTS in a flow, with its terminal |
| **S3** | `ia/docs/sitemap.md` (node requirements and `States:` lines); `ia/docs/blocks.md` for what a page TYPE is made of; `ia/docs/pages/system.md` for the out-of-cluster nodes | the node REQUIRES it |

**S1 is the painted tree and nothing else.** A behaviour read from anywhere but the surface a person
actually meets is a behaviour of a different document.

**Copy is addressed, not quoted**, as `copy > <section> > <zone>`, resolving in
`voice/docs/microcopy.md`. **That inventory has no key column** - its columns are Zone, Type, Line,
Flag - so there is no identifier to cite and the address is a coordinate rather than a key. This is
the one place where the reference rule cannot be fully kept, and the fix is owned elsewhere: see
NOT DECIDED, row N6.

**Controls are addressed as component + variant + state**, resolving in `components/` and, for what
each is and where it stands, `ui-kit/docs/inventory.md`.

---

## Roll-call

**Flows: 5 of 5 described, 0 deliberately not.**

`ia/docs/flows.md` carries MJ, FJ1, FJ2, FJ5 + EJ3 and SJ1. Each has a section below.

**Two files still say there are four, and they NAME the four**: `README.md` key-docs list and
`ia/CLAUDE.md` opening line both read "four user flows (MJ, FJ2, FJ5+EJ3, SJ1)". FJ1 was written on
2026-08-18 and neither line was turned. This is worse than a stale count, because a list that names
its members reads as complete: the missing one is the browse layer, which is four surfaces wide and
holds the search route that a reader reported broken the day after it shipped. Repaired at step 5.

**Terminals: 17 of 17 described, 0 deliberately not.** T1, T2, T3, T5, T6, T7, T8, T9, T10, T11,
T12, T13a, T13b, T14, T15, T16, T17. T4 is retired by `flows.md` and is not counted.

**Screen surfaces named by a flow: 25 of 25 accounted for**, which is `flows.md`'s own dated reading
of 2026-08-20 and is not re-taken here. This file adds the surfaces no flow names - the system
nodes, the account cluster and the two document faces - from S3.

**One node is deliberately not described**, and it is the only one: `sessionHook` in FJ5, which
`flows.md` labels *reserved, post-MVP, not built*. It has no surface, by decision.

---

## MJ - place a real stake on an outcome

The main job, and the only flow that crosses the activation gate. Its success terminal is T14.

| # | Step | What happens | States that exist for it | Source |
|---|---|---|---|---|
| MJ1 | Arrive | A session starts on the feed, from an external trigger, or lands directly on one event from a deep link. No account is asked for and none is needed to reach any step up to MJ7. | `event-feed`, and the four `event-feed-{category}` browse pages; each carries loading / empty / error and the logged-out half of the auth axis | S1, S2, S3 |
| MJ2 | Feed resolves | The feed is fetched. Nothing found is not an error: it is the T6 churn terminal, whose recovery edge is a subscription to new events in the category. | `-loading`, `-empty`, `-error` on the feed and on each category page, in both auth states | S1, S2, S3 |
| MJ3 | Enter an event | Two edges, one destination. Tapping the card body or the question opens the event neutrally. Tapping YES or NO on the card opens the SAME event with the side, and for multi-outcome the option, already chosen. **Neither places a bet and neither skips the event.** The pre-selection travels in the URL query, not in the click, so it survives a share, a bookmark and the back button. | `event-detail` and `event-detail-multi`; the arrival state is drawn as `event-detail-bet-ready` | S1, S2, S3 |
| MJ4 | Context loads | Failure is T8 and its recovery edge is a retry that returns to the same event. | `event-detail-loading`, `event-detail-error`, and their logged-out twins | S1, S2, S3 |
| MJ5 | Understand or leave | A reader who is not convinced exits to the feed. This is T7, a churn terminal with a recovery edge, not a failure. | no state of its own; it is an exit edge | S2 |
| MJ6 | Build the bet | The bet is built in the bet panel on the event itself - a rail at the wide end, a dock that opens a sheet at the narrow end. Side, amount, fee and both outcomes are all in the panel before anything is committed. The panel is reachable and operable **logged out**. | `event-detail-bet-ready`; the panel's own guard states are MJ7 to MJ12 below | S1, S2, S3 |
| MJ7 | Confirm fires the gate | **This is the only gate in the product.** It fires at Confirm and never at the YES / NO tap. Two branches: a social sign-in then funding, or an existing USDC wallet with no fiat and no identity check on this platform. | `sign-in` as a dialog over the page, and as a page for the per-state reference | S1, S2, S3 |
| MJ8 | Authenticate | Failure is T5 with a retry or another provider. A provider collision - an account that exists under a different provider - is its own state, not an error message. | `sign-in-loading`, `sign-in-error`, `sign-in-provider-conflict` | S1, S2, S3 |
| MJ9 | Fund | Funding runs inside a third-party widget; identity verification happens there and not here. A funds-safety line stands inline before submit. Five failures are distinct surfaces: the card is declined (T2), identity is rejected (T1), the widget itself never loads, the payment is under review, and the amount is under the floor. | `deposit`, `-loading`, `-pending`, `-error-card`, `-error-kyc`, `-widget-load-failure`, `-minimum-not-met` | S1, S2, S3 |
| MJ10 | Understand the money first | From funding a reader may open the explainer instead of paying. **The explainer is a way in, not a leaf**: it can start a signup, and it can send a reader back to browse. Both edges are drawn on the map deliberately, because a single funnel-shaped exit would contradict the sentence the explainer has just made. | `how-it-works` as a page, and the dialog carried on the feed | S1, S2, S3 |
| MJ11 | Wallet branch | The crypto path connects an existing wallet instead of funding. Failure is T15, which shares its surface with the auth failure, and it carries a second edge: switch to the social path. | `sign-in-error` | S2, S3 |
| MJ12 | Price reconcile | **A mandatory step, not an error.** Between Confirm and execution the reader was away authenticating and funding, so the price is re-read. Unchanged, it executes. Moved, the reader is shown the old price against the new one and must accept it again. Declining is T16, a churn terminal with two recovery edges: re-read the event, or re-enter at the new price. | `event-detail-bet-reconcile` | S1, S2, S3 |
| MJ13 | Insufficient balance | An inline guard inside the panel, not a page and not a rejection: it states what can be bet and offers funding. | `event-detail-bet-insufficient` | S1, S3 |
| MJ14 | Execute | Registration runs as a wait with a status. Failure is T3, whose edges are a retry and a look at the balance. | `event-detail-bet-processing`, `event-detail-bet-error` | S1, S2, S3 |
| MJ15 | Closed | The reader lands on their own bets, holding the position. T14. | `active-bets` and its loading / two empties / error | S1, S2, S3 |

**The rule this flow exists to hold:** nothing bypasses the event. There is no edge from the feed, or
from search, that places a bet. Every path builds the bet on the event that explains it.

---

## FJ1 - find the event before the topic goes cold

The browse layer, four surfaces wide. Written 2026-08-18, when search shipped with no route on any
chart and the job the whole layer exists for turned out to be the one job nobody had drawn.

| # | Step | What happens | States that exist for it | Source |
|---|---|---|---|---|
| F1.1 | On the first screen | The catalog is small enough to scan, so the first edge closes the job with no query at all. | `event-feed` | S1, S2, S3 |
| F1.2 | By topic | A category opened as its own page, scoped, with the sub-category rail. **The rail is built from the cards on the page**, so no reader is offered a value that returns an empty grid. | the four `event-feed-{category}` pages with the full auth x state matrix | S1, S2, S3 |
| F1.3 | Saved earlier | A view over the feed, not a separate screen: it fetches from the same place and fails the same way, so it carries the feed's state set. | `favorites`, `-loading`, `-empty`, `-error` | S1, S2, S3 |
| F1.4 | By name | **Two faces, one destination, and the split is a measurement rather than a taste.** Below the widest rung the mark opens a sheet over the page you are on; at and above it the field stands in the header row. Both submit to the same results page, which is also the deep-link target and the escape from a missing page. | `event-feed-search` (the page), `event-feed-search-results`, `event-feed-search-empty`; the sheet is `searchSheet` on the feed | S1, S2, S3 |
| F1.5 | Nothing matches | T17, a churn terminal and **not an error**: nothing failed, the answer is that no open market matches. Three recovery edges: a shorter word, browse everything, or read how events are chosen. | `event-feed-search-empty` | S1, S2 |
| F1.6 | Closed | The event is open on screen, in time. | `event-detail` | S1, S2 |

**Scope, and it is a behaviour rather than a limitation to be fixed:** search indexes the OPEN set
only. A settled market is reached from the reader's own history, which is why F1.5 is churn.

**A cost the surface carries and cannot compute:** the search catalog is extracted from the painted
tree by hand into `assets/search.js`. An event added to a screen and not re-taken there is an event
search cannot find. The file states this about itself.

---

## FJ2 - understand why the market prices it that way

The differentiator, and the shortest flow. Its success terminal feeds MJ6.

| # | Step | What happens | States that exist for it | Source |
|---|---|---|---|---|
| F2.1 | Arrive with a number in hand | A percentage seen on the feed or in an article. | `event-feed`, `event-detail` | S1, S2 |
| F2.2 | The context block answers | Probability, the price history, the one-line why, the narrative, the resolution conditions and the source - in that order, with the panel leading. **This block is the sole home of the differentiator.** | `event-detail`, `event-detail-multi`, and the recurring and resolved faces | S1, S2, S3 |
| F2.3 | Load failure | T8, shared with MJ4, one retry edge. | `event-detail-error` | S1, S2 |
| F2.4 | Not enough context | T7, an exit to the feed. | exit edge | S2 |
| F2.5 | Understood, not betting | **A named success, not a drop-off.** A reader who understands the number and judges the market right has closed this job and answered no to the next one. | exit edge | S2 |
| F2.6 | Understood, has an edge | Into the bet panel, which is MJ6. | `event-detail-bet-ready` | S1, S2 |

---

## FJ5 + EJ3 - exit a loss consciously

The guardrail flow. Its shape is a deliberate beat between a loss and the next bet.

| # | Step | What happens | States that exist for it | Source |
|---|---|---|---|---|
| F5.1 | Fast path | A resolution notification routes straight to the loss surface, which is otherwise four taps deep. The point of the edge is that the resolution reaches the reader before the impulse does. | `loss`, `loss-loading`, `loss-multi` | S1, S2, S3 |
| F5.2 | Manual path | The reader opens their own bets and finds the resolved one. Not seeing it is T9, whose recovery edge is a recently-resolved section on that screen. | `active-bets`, `active-bets-history` and their states | S1, S2, S3 |
| F5.3 | The note is read | The default beat: what happened, why, and a next step that is deliberately not "bet again". | `loss` | S1, S2, S3 |
| F5.4 | The note is skipped | The escalation path routes through a friction node rather than straight to a new bet. | no surface of its own; it is a beat | S2 |
| F5.5 | Next action | Closing the app is T10, a churn terminal whose recovery edge is a later scheduled notification. Browsing is the success edge. | `notifications` and its four states | S1, S2, S3 |
| F5.6 | Reserved | A session-aware chasing check. **Post-MVP and not built**, by decision. | none, deliberately | S2 |

**The win half of the same resolution rule is SJ1 below.** A resolution is designed both ways and
the two are not symmetrical: the loss surface has no error state, on purpose, because its only
failure mode - a share card that would not generate - does not exist on it.

---

## SJ1 - show a win

| # | Step | What happens | States that exist for it | Source |
|---|---|---|---|---|
| S1.1 | Fast path | A win notification routes to the win surface in one tap. | `win`, `win-loading`, `win-multi` | S1, S2, S3 |
| S1.2 | Manual path | From the history tab of the reader's own bets. | `active-bets-history` | S1, S2, S3 |
| S1.3 | Share card | Generated automatically. Failure is T11, which blocks this job and falls back to sharing as text; the reader returns through T13a. | `win-error` | S1, S2, S3 |
| S1.4 | Payout delay | Settlement can lag the resolution. It is a state, not an error. | `win-payout-pending` | S1, S3 |
| S1.5 | Shares | External. A new reader following the link arrives at the feed; no click-through is T13b, a recovery terminal. | exit edge | S2 |
| S1.6 | Does not share | The public profile still records it. T12, with an edge back to finding a new event. | `my-profile`, `public-profile` and their states | S1, S2, S3 |
| S1.7 | The secondary exit | "See next events" is deliberately the LOWER-emphasis call on this screen, because the risk this flow guards against is overconfidence after a win. **A build that promotes it has changed the product, not the layout.** | `win` | S1, S2, S3 |

---

## Surfaces no flow names

Covered by S3 alone, which is a complete source: a system node exists because a node requires it,
not because a journey passes through it.

| Surface | Behaviour | States | Source |
|---|---|---|---|
| Wallet | Balance, funding and withdrawal. **No empty state, on purpose**: a wallet with no transactions still has a balance and a funds-safety line to show. Withdrawal is a dialog on this screen. | `wallet`, `-loading`, `-error` | S1, S3 |
| Notifications | The return trigger. A denied OS permission is its own state with an in-app route to system settings, not a silent failure. | `notifications`, `-loading`, `-empty`, `-error`, `-push`; and `event-feed-push-permission-missing` | S1, S3 |
| My profile / public profile | Reputation and track record. A public profile can be gone or its link expired, which is its own state and not an error. | `my-profile` + 2, `public-profile` + 3 including `-not-found` | S1, S3 |
| The five documents | Terms, Privacy, Cookie policy, Responsible betting, About. One page TYPE, banked once. They are prose read end to end, which is a different reading mode from every other surface here. | `terms`, `privacy`, `cookies`, `responsible-betting`, `about` | S1, S3 |
| Page missing / server error / maintenance | Three distinct failures with three different recoveries. The missing-page escape routes into search, which is why search exists as a page and not only as a sheet. | `404`, `500`, `maintenance` | S1, S2 (the escape edge), S3 |
| Consent | A row that is a label, so the whole row is the target rather than the box. | `cookie-consent` | S1, S3 |
| Transient messages | The status layer, shown as a specimen page because a transient state cannot be caught in a screenshot of the screen it appears on. | `toasts` | S1, S3 |

---

## Validation

Every rule below is enforced **inline, before submit, against the field**, and each is drawn as its
own state rather than reported after the fact.

| Field | Rule | How it is expressed | Where the value is owned | Source |
|---|---|---|---|---|
| Bet amount | A floor, no ceiling. Two decimal places. | `data-min` and `pattern` on the amount field of the `input` component inside the `betpanel`; quick-select chips beside it are the `chip` component, amount variant | `PRODUCT.md` > Business model | S1, S3 |
| Bet side | **A bet cannot be confirmed without a side.** The Confirm control is held by `aria-disabled` and points at the sentence that says why, through `aria-describedby` - so the reason is announced rather than implied by a dimmed button. | `button` component, primary variant, held state; the sentence resolves at `copy > Event Detail > bet panel` | this file | S1 |
| Bet amount vs balance | Over balance is a guard inside the panel, not a rejection: it says what can be bet and offers funding. | drawn as `event-detail-bet-insufficient` | `PRODUCT.md` | S1, S3 |
| Funding amount | A floor. Under it, the field carries `aria-invalid` and is described by an inline error that stands with the field. | `data-min` on the amount field; the `notice` component, inline-error variant | `PRODUCT.md` > Business model | S1, S3 |
| Fee | Charged on the stake, stated before submit, never after. Both outcomes are shown against the amount, not only the chosen one. | the panel's own breakdown rows | `PRODUCT.md` > Business model | S1, S3 |
| Price | **The price shown is the price filled.** No slippage, no partial fill. The only thing that can move it is the gate, and that is MJ12, which asks again rather than absorbing the difference. | the panel's fine print | `PRODUCT.md` > Liquidity and risk | S1, S3 |

---

## Edge cases

Each of these is a case where the obvious build is wrong, and each is drawn.

| Case | The behaviour | Why it is not the obvious one | Source |
|---|---|---|---|
| An event resolves while the reader is on it | Route by whether they hold a position: to their own win or loss surface if they do, to the feed if they do not. | The obvious build shows a disabled panel and leaves the reader on a dead page. | S3 |
| A reader arrives with a side already chosen | The panel opens holding that side, with both outcomes already priced against the default amount. | The obvious build treats the query as a hint and clears it, which is what a first attempt at this screen did: the side was pressed in the markup and rendered unpressed. | S1, S2 |
| A multi-outcome event | The outcomes stand in the main column and the panel asks for one before it asks for a side. The odds bar is binary-only. | The obvious build reuses the binary panel and asks YES / NO on an event with four answers. | S1, S3 |
| A recurring event | The header states the cadence, and every instance sits inside its current period. A resolved instance in a series is the one immediately before the open one. | The obvious build ships a fixed date, and a cadence with a stale instance breaks its own promise silently. | S1, S3 |
| Two tabs of one screen | Active and history are two views of one reader's account and must agree about any market they both name. | The obvious build validates each page alone. Every instrument in this repository reads one document, and a market that is open on one tab and won on the other is valid on both. | S1 |
| A dialog that also has a page | Sign-in and funding exist as dialogs over the current page AND as standalone pages, which are the per-state reference. **One markup, one copy.** | The obvious build lets the two drift, and only one of them is ever checked. | S1, S3 |
| A closed overlay | A state file ships its dialog closed. It is a state, not a missing surface. | The obvious read reports the heading as absent, because the dialog sits outside the device frame the probe scoped to. | S1 |
| The explainer as a way in | It carries an outgoing edge to signup AND a quieter one back to browsing. | The obvious build makes it a leaf with one exit, which contradicts the sentence it has just made about betting before connecting anything. | S2 |

---

## NOT DECIDED

Rows that had no source. **They are not in the spec above**, because a behaviour with no source is a
plausible guess wearing a specification's format. Each is addressed to the person who owns it.

| # | The question | Why it is not answerable from the repository | Where the answer belongs when it is taken |
|---|---|---|---|
| N1 | Must a new indexed page have its metadata section written BEFORE the page is built, or after? | `ia/docs/pages/seo.md` specifies six page families completely and states which half lives where, but not the ordering. The one precedent went both ways. | `ia/docs/pages/seo.md`, then a line in `one-shot.md` |
| N2 | Is `ia/annotations/` frozen, incomplete, or optional for a new screen family? | 15 pages against 15 original families; search, the five documents and the system nodes have none, and the tool that built them is gone. Nothing states which of the three it is. | `docs/decisions.md`, and the route on `handoff.html` |
| N3 | What is the ceiling on a page script? | The rule for the two shared scripts is explicit. Nothing states how much behaviour may live inline, whether a script may write a class the system styles - it does - or how a hook is registered beyond the CSS half. | `components/CLAUDE.md`, and `one-shot.md` |
| N4 | For a page TYPE that has never been banked, which steps of the banking method are mandatory? | `ia/docs/blocks.md` states four rules a row obeys and demonstrates the method once. Whether the two-source research pass is required every time or was specific to that instance is not written. | `ia/docs/blocks.md` |
| N5 | What domain does the product live at? | Open by decision, with the cost written beside it: no canonical and no share URL can be written without it. The trigger is named; the decider is named. | `ia/docs/pages/seo.md`, when the trigger fires |
| N6 | How is a string referenced without quoting it? | The copy inventory has Zone / Type / Line / Flag and **no key column**, so nothing can address a string except by repeating it - which is the duplication this package forbids. Every copy reference above is a coordinate, and a coordinate breaks when a section is re-ordered. | `voice/docs/microcopy.md`, as a key column; filed in `docs/backlog.md` |
| N7 | Withdrawal has a drawn surface and no flow. | The withdrawal dialog stands on the wallet screen. `ia/docs/flows.md` lists a minimal withdrawal flow under deferred polish, so the surface shipped ahead of the map. | `ia/docs/flows.md` |
| N8 | Is a support surface buildable now? | Its node row registers it and describes its shape; a paragraph seventeen lines further down decides it does NOT ship at this release. A reader who takes the row and not the paragraph builds a deferred screen. | the node row itself, which should carry the decision it is governed by |

---

## What this file does not own

The visual system, in `DESIGN.md` and `components/`. Every string, in `voice/docs/microcopy.md`. What
a component is and where it stands, in `ui-kit/docs/inventory.md`. Which screen is assembled from
what, in `map.md` beside this file. How the product is built as software, in `docs/build-plan.md`.
Why any of it was decided this way, in `docs/decisions.md`.
