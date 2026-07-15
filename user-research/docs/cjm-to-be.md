# CJM To-Be - Future Experience

**Focus: Alex (News Junkie, primary persona) x Main Job (MJ)**

Main job (English gloss): "When an event I follow nears its outcome, I want a real stake in the result, so it is not just news but my personal participation with real consequences."
Source: `user-research/docs/jtbd.md` (## MJ · Main Job), `research/docs/lean-ux-canvas.md` §4.

## To-Be path (ideal in-product journey)

Design half. The future is designed, but every step pays with a trace to a concrete As-Is barrier / growth zone (from `cjm-as-is.md`) or a job (`jtbd.md`). A step that closes no barrier and serves no job is an orphan and is cut. This sharpens the existing MVP core (`lean-ux-canvas.md` Solutions + the wireframes MJ flow); it does not fork it.

| # | Step in product | Goal (job) | Closes (trace) | Capability / feature (diverge -> converge) | Target emotion (vs As-Is) |
|---|---|---|---|---|---|
| 1 | Arrive on a live event, not a signup | Act on the take immediately (MJ) | As-Is phase 2 discovery `[?]`; "first page = live events, not sign up" (JTBD product implication) | Story-led event cards as home. Candidates: generic market list / story-led cards / category-first -> **story-led** (generic reads as the "Excel spreadsheet" complaint; category-first buries the live moment) | "this is my event" +4 (As-Is peak kept, not crashed) |
| 2 | Understand the market before any account | Understand the bet and why the price (FJ2) | **GZ2** (phase 4: no "why this price", event in isolation) | "Explain the number": plain probability + one-line why + the news story, spectator language. Candidates: tooltip / inline + story / full explainer page -> **inline + story** (tooltip too shallow; full page too heavy for the moment) | "I get it" -4 -> +3 |
| 3 | Tap YES / NO and see the bet intent before signing in | Reach the bet without the crypto wall (MJ) | **GZ1** (phase 3 wall) - the core inversion; the gate fires at Confirm, not at entry | Browse + bet-intent with no wallet upfront; gate at Confirm. Candidates: wallet-connect first / social login + custodial stablecoin / guest bet then auth -> **guest-bet then auth + social login** (wallet-first IS the wall we are killing) | "in flow, not blocked" -5 -> +2 (deepest dip flattened) |
| 4 | Sign in and fund with one clear funds-safety line | Fund the bet without fear | **GZ3** (phase 5: money question, opaque fees) | Social login; fiat -> stablecoin on-ramp; "Your USDC is held 1:1, we never lend it"; fee shown before Confirm. Candidates: ToS link / one plain sentence / badge only -> **one plain sentence** (Revolut C2 5/5, benchmark Top 3 #2) | "reassured" -4 -> +2 |
| 5 | Confirm the bet with the price reconciled | Have real skin in the game (MJ) | Attrition (phase 6, few reached) + AMM price move (S5 reconcile in flows) | Confirm screen: fee + potential outcome + AMM reconcile if the price moved. Candidates: instant confirm / reconcile on move -> **reconcile** (D1 AMM; a silent price change breaks trust) | "committed, clear" +3 |
| 6 | Follow your bet with live context | Track the stake against reality (MJ + track) | Tracking happens outside the product (phase 6) | Active Bets + outcome notifications (retention anchor). Candidates: email / in-app / push -> **push + in-app** (email = low salience) | "in the loop" +3 |
| 7 | Resolution designed both ways | Vindication (win) / closure (loss), without betrayal | **GZ4** (phase 7 loss) + **GZ5** (betrayal fear) | Win "You were right" + share (with overconfidence friction, F5); Loss "Here's what happened" + context + a next step that is NOT "bet again"; transparent resolution + resolved-markets count. Loss-CTA candidates: "bet again" / context + neutral next step / nothing -> **context + neutral next step** ("bet again" weaponizes the loss-chasing in the mined "$2300, make it back"; "nothing" is the As-Is void) | win +4 (share window) / loss -5 -> -1 (closure, not void) |

**Tracing is clean:** every step closes a specific As-Is barrier / growth zone or a job, so there are no orphans. It is a sharpening, not a fork: the path matches the existing MVP flow (feed -> detail -> YES / NO -> bet panel -> gate at Confirm -> Active Bets; win / loss screens; voice principles).

## Backlog and MVP core

Each item has a parent (an As-Is barrier or a job), a priority, and a success signal. This is one list that sharpens the existing MVP core (`lean-ux-canvas.md` Solutions + the `jtbd.md` matrix + CLAUDE.md), not a second parallel backlog.

### MVP - without it the To-Be path breaks

| Feature | Parent (trace) | Success signal (metric-hypothesis, AARRR) |
|---|---|---|
| Story-led event feed (home) | JTBD "first page = live events" + GZ2 | % of sessions that open an event within N seconds (Activation) |
| "Explain the number" (inline probability + why + story, spectator language) | GZ2 / FJ2 | % who reach bet-intent after opening an event (Activation) |
| **Browse + bet-intent with no wallet upfront; gate at Confirm** | **GZ1 (crypto wall)** - the core inversion | bounce at the first wallet prompt drops; first-bet within 24h > 40% (O3) |
| Social login (Google / X) | GZ1 | signup completion rate |
| Fiat on-ramp (card -> stablecoin) | GZ1 / GZ3 | deposit completion rate |
| Funds-safety line "USDC held 1:1, we never lend it" | GZ3 / GZ5 | deposit conversion after the line (H4) |
| Fee shown before Confirm | GZ3 | fewer post-bet fee complaints (H6) |
| Confirm + AMM price reconcile (S5) | AMM / trust | bet-completion at Confirm; zero "silent price move" complaints |
| $1 / $5 bet sizing (low min, $5 default) | low barrier + `[?]` "real but not scary" | distribution of first-bet sizes |
| Active Bets view | track (phase 6) | return rate to Active Bets (Retention) |
| Outcome / position notifications | tracking happens outside the product | notification-driven return (D30 > 15%, O2) |
| Win "You were right" + share (overconfidence friction) | SJ / win | share rate; SJ1 share window |
| **Loss "Here's what happened" + context + a next step that is NOT "bet again"** | **GZ4** | post-loss retention without a loss-chasing spike (guardrail) |
| Transparent resolution + resolved-markets count | GZ5 (betrayal fear) | resolved-count visibility -> deposit / return |

### Later - improves, but the path works without it
- **Multi-outcome markets** - product scope, not derived by this CJM (the focus was binary). Kept in MVP scope as scope, marked not-CJM-derived.
- **Leaderboard, Staking (TBD)** - orphans relative to this CJM (in the old core, not mapped to any To-Be step). Moved to Later, outside this focus.

### Reconcile with the existing MVP core (sharpening, not a fork)
- **Confirmed by To-Be:** social login, fiat on-ramp, funds-safety line, fee-before-confirm, AMM / S5, $1/$5 sizing, Active Bets, notifications, win + share, story-driven discovery.
- **Sharpened:** "explain the number" -> spectator language; **no wallet until Confirm** (the key inversion); the loss screen carries **no "bet again"** (straight from the mined "$2300, make it back" chasing quote).
- **Orphans relative to this CJM:** Leaderboard and Staking (TBD) -> Later; Multi-outcome stays as scope, marked. One consistent list.

## Critique and consistency (step 9)

- **Every MVP feature traces to a parent; no orphans.** Two weaker parents, kept but flagged: **Confirm + AMM reconcile** is mechanism-derived (AMM D1 / S5), not a felt As-Is pain; **$1 / $5 sizing** traces to the `[?]` "real but not scary" unknown, so its default is a hypothesis to test, not a settled fact.
- **Sharpening, not a fork:** the backlog matches `lean-ux-canvas.md` §5 Solutions. The one sharpening to propagate is **"no wallet until Confirm"**, which must be reflected in the CLAUDE.md MVP block so the core stays one version (done in step 11).
- **MVP vs the riskiest assumption:** the riskiest assumption ("the barrier is friction, not motivation") was substantially refuted (research.md §9 F4 - motivation must be activated pre-deposit). The MVP is friction-heavy, so the two motivation features - the **story-led entry (step 1)** and **"explain the number" (step 2)** - are **co-equal MVP**, not secondary; no-wallet is not a silver bullet. The first test (`lean-ux-canvas.md` §8 landing A/B) measures motivation, not only funnel completion.
- **Path-break vs differentiator:** strictly path-breaking MVP = story-led feed, explain the number, no-wallet, social login, on-ramp, confirm + reconcile, win / loss. The trust items (funds-safety line, fee-before-Confirm, resolved-count) are MVP for the differentiator (clarity + trust), not for the raw path; kept MVP, marked honestly.
- **Carried `[?]`:** the bet size that feels "real but not scary" (parent of $1 / $5 sizing).

<!-- Step 10: build cjm-as-is.html + cjm-to-be.html on the research.html shell; step 11: propagate the sharpened MVP core to CLAUDE.md + README. -->



