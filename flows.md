# User Flows - Prediction Market Platform

> Built from: sitemap.md - jtbd.md
> `[Square brackets]` = screens from sitemap.md. `{Diamonds}` = decisions. `([Stadiums])` = terminal states.
> Dead-end and error terminals: T1-T14. Info states labeled with i.

---

## MJ - When an event I follow is approaching resolution, I want a real stake on the outcome

```mermaid
flowchart TD
    S5{"S5: AMM price moved during gate?"}
    priceConfirm{"accept new price?"}

    triggerFeed(["external trigger: news, notification"])
    triggerLink(["G1 - direct link to event, bypasses Event Feed"])

    triggerFeed --> EF["Event Feed"]
    EF --> found{"found a relevant event?"}
    found -->|"no"| T1(["T1 - no matching events, exits"])
    found -->|"yes"| ED["Event Detail"]

    triggerLink --> ED

    ED --> ctxOk{"context loaded?"}
    ctxOk -->|"no"| T2(["T2 - load error, exits"])
    ctxOk -->|"yes"| wantsBet{"wants to bet?"}

    wantsBet -->|"no"| T3(["T3 - not convinced, exits without bet"])
    wantsBet -->|"yes - taps YES or NO"| BS1["Bet Screen (intent)"]

    BS1 --> confirmedIntent{"confirms the bet?"}
    confirmedIntent -->|"no, changed mind"| ED
    confirmedIntent -->|"yes - gate fires"| personaType{"account type?"}

    personaType -->|"News Junkie"| SI["Sign In / Register"]
    SI --> authOk{"auth successful?"}
    authOk -->|"no"| T4(["T4 - auth error"])
    authOk -->|"yes"| DEP["Deposit"]

    DEP --> moreInfo{"wants to understand fund safety?"}
    moreInfo -->|"yes"| HIW["How It Works"]
    HIW --> DEP
    moreInfo -->|"no"| depOk{"deposit successful?"}
    depOk -->|"card declined"| T5(["T5 - card declined"])
    depOk -->|"KYC rejected"| T6(["T6 - KYC rejected"])
    depOk -->|"yes"| S5

    personaType -->|"Crypto Native"| walletOk{"wallet connected?"}
    walletOk -->|"no"| T7(["T7 - wallet connect failed"])
    walletOk -->|"yes"| S5

    S5 -->|"no change"| BS2["Bet Screen (execute)"]
    S5 -->|"yes - was X, now Y"| priceConfirm
    priceConfirm -->|"no"| T8(["T8 - price rejected, bet cancelled"])
    priceConfirm -->|"yes"| BS2

    BS2 --> techOk{"bet registered on-chain?"}
    techOk -->|"no"| T9(["T9 - bet registration failed"])
    techOk -->|"yes"| AB["Active Bets"]

    AB --> mjDone(["MJ closed - bet placed, user follows the event"])
```

---

## FJ2 - When I see an event and its probability, I want to understand why the market prices it that way

```mermaid
flowchart TD
    trigger(["trigger: saw percentage on Event Feed or arrived from an article"])
    trigger --> EF["Event Feed"]
    EF --> ED["Event Detail"]

    ED --> ctxOk{"context loaded?"}
    ctxOk -->|"no"| T10(["T10 - load error, exits"])
    ctxOk -->|"yes"| understood{"understood why this probability?"}

    understood -->|"no, context insufficient"| T11(["T11 - unclear, exits without bet"])
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

    trigger(["notification: event resolved, or user opens Active Bets"])
    trigger --> AB["Active Bets"]

    AB --> seesResolved{"sees a resolved losing bet?"}
    seesResolved -->|"no"| T12(["T12 - did not notice, waits for next notification"])
    seesResolved -->|"yes"| LS["Loss Screen"]

    LS --> readsNote{"reads the resolution explanation?"}
    readsNote -->|"no - bets immediately"| BS["Bet Screen"]
    BS --> escalationConfirm{"confirms next bet?"}
    escalationConfirm -->|"no, reconsiders"| nextAction
    escalationConfirm -->|"yes - escalation path (F5 risk)"| AB

    readsNote -->|"yes"| nextAction
    nextAction -->|"closes app"| T13(["T13 - dormant. Casual Experimenter churn risk D7"])
    nextAction -->|"browses events"| EF["Event Feed"]

    EF --> fj5Done(["FJ5 + EJ3 closed - exited consciously, no impulse to chase"])
```

---

## SJ1 - When I win a bet on an event everyone talked about, I want to easily show that to my circle

```mermaid
flowchart TD
    trigger(["event resolved - win"])
    trigger --> WS["Win Screen"]

    WS --> cardOk{"Share Card auto-generated?"}
    cardOk -->|"no"| T14(["T14 - Share Card not generated, SJ1 blocked"])
    cardOk -->|"yes"| shares{"user shares?"}

    shares -->|"no"| MP["My Profile"]
    MP --> profileOnly(["i - track record updated in profile, SJ2 closed, SJ1 no"])

    shares -->|"yes"| ext(["external: Twitter/X, WhatsApp, Telegram"])
    ext --> newUser{"new user follows the link?"}
    newUser -->|"no"| sj1Done(["SJ1 closed - win publicly shown"])
    newUser -->|"yes"| EF["Event Feed"]
    EF --> sj1Done
```
