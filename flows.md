# User Flows - Prediction Market Platform

> Built from: sitemap.md - jtbd.md
> `[Square brackets]` = screens from sitemap.md. `{Diamonds}` = decisions. `([Stadiums])` = terminal states.
> Success terminals: T14/mjDone, fj2Done, fj5Done, sj1Done. Error/churn terminals T1-T3, T5-T13, T15-T16 each have at least one recovery edge. T4 retired as terminal (replaced by escalation-path edge in FJ5).

---

## Terminal map

| T# | Meaning | Flow | Type |
|---|---|---|---|
| T1 | KYC rejected | MJ - Deposit branch | error |
| T2 | Card declined | MJ - Deposit branch | error |
| T3 | Bet registration failed on-chain | MJ - after execute | error |
| T4 | RETIRED - was chasing risk sink | FJ5 | retired |
| T5 | Auth error | MJ - Sign In branch | error |
| T6 | Empty feed (first visit, no events) | MJ - after Event Feed | churn |
| T7 | Not convinced / context insufficient | MJ + FJ2 - after Event Detail | churn |
| T8 | Event Detail load error | MJ + FJ2 | error |
| T9 | Resolved bet not noticed | FJ5 - Active Bets | churn |
| T10 | Dormant (closed app) | FJ5 - conscious-exit path | churn |
| T11 | Share Card not generated | SJ1 - after Win Screen | error |
| T12 | Profile only (shared nothing) | SJ1 - shares no | churn |
| T13 | Returned after share | SJ1 - after external share | recovery |
| T14 | MJ closed - bet placed | MJ - success | success |
| T15 | Wallet connect failed | MJ - Crypto Native branch | error |
| T16 | Price rejected at S5 reconcile | MJ - priceConfirm no | churn |

---

## MJ - When an event I follow is approaching resolution, I want a real stake on the outcome

```mermaid
flowchart TD
    walletOk{"wallet connected?"}
    S5{"S5: AMM price moved during gate?"}
    priceConfirm{"accept new price?"}

    triggerFeed(["external trigger: news, notification"])
    triggerLink(["deep link from news or notification to event"])

    triggerFeed --> EF["Event Feed"]
    EF --> found{"found a relevant event?"}
    found -->|"no"| T6(["T6 - empty feed, no matching events"])
    T6 -->|"subscribe: notify me of new events in category"| EF

    found -->|"yes"| ED["Event Detail"]
    triggerLink --> ED

    ED --> ctxOk{"context loaded?"}
    ctxOk -->|"no"| T8(["T8 - load error"])
    T8 -->|"retry"| ED
    ctxOk -->|"yes"| wantsBet{"wants to bet?"}

    wantsBet -->|"no"| T7(["T7 - not convinced, exits without bet"])
    T7 -->|"back to feed"| EF
    wantsBet -->|"yes - taps YES or NO"| BS1["Bet Screen (intent)"]

    BS1 --> confirmedIntent{"confirms the bet?"}
    confirmedIntent -->|"no, changed mind"| ED
    confirmedIntent -->|"yes - gate fires"| personaType{"account type?"}

    personaType -->|"News Junkie"| SI["Sign In / Register"]
    personaType -->|"Crypto Native"| walletOk

    SI --> authOk{"auth successful?"}
    authOk -->|"no"| T5(["T5 - auth error"])
    T5 -->|"retry or use other provider"| SI
    authOk -->|"yes"| DEP["Deposit"]

    DEP --> moreInfo{"wants to understand fund safety?"}
    moreInfo -->|"yes"| HIW["How It Works"]
    HIW --> DEP
    moreInfo -->|"no"| depOk{"deposit successful?"}
    depOk -->|"card declined"| T2(["T2 - card declined"])
    T2 -->|"try another card or connect a USDC wallet"| DEP
    depOk -->|"KYC rejected"| T1(["T1 - KYC rejected"])
    T1 -->|"connect a USDC wallet, no KYC"| walletOk
    T1 -->|"contact support"| supportContact(["i - contact support"])
    depOk -->|"yes"| S5

    walletOk -->|"no"| T15(["T15 - wallet connect failed"])
    T15 -->|"retry connect"| walletOk
    T15 -->|"switch to News Junkie path: social login and deposit"| SI
    walletOk -->|"yes"| S5

    S5 -->|"no change"| BS2["Bet Screen (execute)"]
    S5 -->|"yes - was X, now Y"| priceConfirm
    priceConfirm -->|"no"| T16(["T16 - price rejected, bet cancelled"])
    T16 -->|"re-evaluate event"| ED
    T16 -->|"re-enter at new price"| BS1
    priceConfirm -->|"yes"| BS2

    BS2 --> techOk{"bet registered on-chain?"}
    techOk -->|"no"| T3(["T3 - bet registration failed on-chain"])
    T3 -->|"retry"| BS2
    T3 -->|"check balance"| WA["Wallet"]
    techOk -->|"yes"| AB["Active Bets"]

    AB --> mjDone(["T14 - MJ closed: bet placed, user follows the event"])
    mjDone -->|"monitor position"| EDmon["Event Detail"]
```

---

## FJ2 - When I see an event and its probability, I want to understand why the market prices it that way

```mermaid
flowchart TD
    trigger(["trigger: saw percentage on Event Feed or arrived from an article"])
    trigger --> EF["Event Feed"]
    EF --> ED["Event Detail"]

    ED --> ctxOk{"context loaded?"}
    ctxOk -->|"no"| T8(["T8 - load error"])
    T8 -->|"retry"| ED
    ctxOk -->|"yes"| understood{"understood why this probability?"}

    understood -->|"no, context insufficient"| T7(["T7 - unclear, exits without bet"])
    T7 -->|"back to feed"| EF
    understood -->|"yes"| hasEdge{"has information edge over the market?"}

    hasEdge -->|"no, market may be right"| watcher(["i - watcher: understood, not betting. FJ2 closed, MJ no."])
    hasEdge -->|"yes, confident in own position"| BS["Bet Screen"]

    BS --> fj2Done(["FJ2 closed - understood the odds, moved to bet"])
```

---

## FJ5 + EJ3 - When an event I bet on resolves with a loss, I want to exit consciously without the impulse to chase

```mermaid
flowchart TD
    nextAction{"next action?"}

    %% Path A: G1 - resolution notification routes directly to Loss Screen (fast path)
    %% Loss Screen is otherwise 4 taps deep; G1 cuts this so the resolution note reaches the user before the impulse to chase.
    triggerNotif(["resolution notification"])
    triggerNotif -->|"G1: direct to Loss Screen"| LS["Loss Screen"]

    %% Path B: manual - user opens Active Bets, finds the resolved item
    triggerManual(["user opens Active Bets"])
    triggerManual --> AB["Active Bets"]
    AB --> seesResolved{"sees a resolved losing bet?"}
    seesResolved -->|"no"| T9(["T9 - resolved bet not noticed"])
    T9 -->|"sees recently-resolved section in Active Bets"| LS
    seesResolved -->|"yes"| LS

    LS --> readsNote{"reads the resolution explanation?"}
    readsNote -->|"no - bets immediately"| BS["Bet Screen"]
    BS --> escalationConfirm{"confirms next bet?"}
    escalationConfirm -->|"no, reconsiders"| nextAction
    escalationConfirm -->|"yes - escalation path (F5 risk)"| AB

    readsNote -->|"yes"| nextAction
    nextAction -->|"closes app"| T10(["T10 - dormant, churn risk D7 (Casual Experimenter)"])
    T10 -->|"scheduled push: new event in category fires later"| EF["Event Feed"]
    nextAction -->|"browses events"| EF

    EF --> fj5Done(["FJ5 + EJ3 closed - exited consciously, no impulse to chase"])
```

---

## SJ1 - When I win a bet on an event everyone talked about, I want to easily show that to my circle

```mermaid
flowchart TD
    trigger(["event resolved - win"])
    trigger --> WS["Win Screen"]

    WS --> cardOk{"Share Card auto-generated?"}
    cardOk -->|"no"| T11(["T11 - Share Card not generated, SJ1 blocked"])
    T11 -->|"fallback: share as text"| T13(["T13 - returned after share"])
    T13 -->|"Win Screen: what next?"| EF["Event Feed"]
    EF --> sj1Done(["SJ1 closed - win publicly shown"])

    cardOk -->|"yes"| shares{"user shares?"}
    shares -->|"no"| MP["My Profile"]
    MP --> T12(["T12 - profile only, track record updated, SJ1 no"])
    T12 -->|"find a new event"| EF

    shares -->|"yes"| ext(["external share: Twitter/X, WhatsApp, Telegram"])
    ext --> newUser{"new user follows the link?"}
    newUser -->|"yes"| EF
    newUser -->|"no"| T13
```
