# Product voice - Prediction Market Platform

> **What this is.** The rules by which the product speaks - the voice behind every
> line in `microcopy.md`. Step 2 of the voice workstream: principles first, the
> shared lexicon and the rewrite come next. Every principle here is derived from a
> named source line (personas / jtbd / research / benchmark / competitive
> analysis); nothing is taken on taste alone.

**Context that sets the tone.** This is crypto money, on real-world events, among
strangers, with no regulatory badge we are allowed to show (`benchmark.md`:
"Regulatory badges ... require real licenses we do not hold"). In that context
**trust matters more than wit**. The reader is a news-follower who arrives from a
headline, not a trader - they need the concrete thing (a date, a source, a plain
sentence about their money), not advertising, and not to be made to feel stupid.
Our one differentiator is being **more understandable** than Polymarket, Kalshi
and Futuur (`personas.md`: "differentiator is being more understandable").

The five principles are ordered by how often they fire, most-used first.

---

## Principles

### 1. Explain the number, never just show it

**Rule.** Every number carries the one plain reason it is what it is; we never
leave a bare figure to speak for itself.

**Example.**
- "YES 38%. Funding talks have stalled twice this quarter - that is what is holding the price down."
- "Resolves YES if a shutdown begins before 00:00 ET on Mar 1. Source: official OMB notices."
- "If YES wins, your $5 becomes $13.20."

**Anti-example.**
- "YES 38%" (and nothing else).
- "Buy Yes 37¢."

**Why (from the data).** This is the confirmed differentiator, not a nicety.
`research.md:95` - competitors have "No clear 'why this number?' explanation";
`ux-patterns.md:67` - "No competitor explains why the price is what it is ...
This is our differentiator"; `jtbd.md:60` (FJ2) - the user wants to understand
"почему рынок считает именно так ... а не ставить вслепую"; `personas.md:64-68` -
Alex "doesn't understand why the price is 67%, what affects it, or what
'resolves' means." Competitor language confirms the gap: all of them lead with a
naked % / cents / gauge ("The % is the language of the genre",
`competitors.md`). Our voice is the sentence next to the number.
`research.md:111` even scripts it: show "if YES wins, you get $X", not abstract ¢.

---

### 2. One plain sentence of trust, before the ask - never borrowed authority

**Rule.** Before we move a user's money or take an action, we say what happens to
it in one plain sentence, and we show the cost before Confirm; we never dress up
authority (badges, "bank-grade", "fully protected") that we do not actually hold.

**Example.**
- "Your USDC is held 1:1. We never lend it without your permission." (on the deposit screen)
- "You pay a 2% fee only if you win. Nothing on a loss." (shown before Confirm, not after)
- "We are not a bank or broker. Your USDC sits in a smart contract, not lent out."

**Anti-example.**
- "Bank-grade security. Your funds are fully protected. 🔒"
- Fee revealed only on the confirmation receipt.

**Why (from the data).** `benchmark.md:86` gives the model sentence
verbatim - "Your USDC is held 1:1. We never lend it without your permission. Not
legal text - one plain sentence" - and `:110-113` sets the rule "Transparency
over authority", warning at `:106-108` that faking authority signals "reads as
fake ... destroys trust the moment a user checks." `personas.md:76` lists Alex's
trust trigger as exactly "One clear sentence about funds before he deposits", and
`:81` names his primary fear, "What happens to my money?"; `jtbd.md:133` (EJ2)
wants the safety anxiety gone "до того, как я нажму 'подтвердить'." Fee timing is
a scored criterion: `benchmark.md:17` (C3, "cost visible BEFORE the user
confirms") and `personas.md:78` ("Understands the fee before he bets - no
surprises"). Competitor contrast: Polymarket has "no 'where is my USDC' copy"
(`competitors.md:102,142`); the model to borrow is Coinbase's "Your
crypto is safe here" (`:84`).

---

### 3. Speak to a spectator with an opinion, not to a trader

**Rule.** We use the words a news-follower already owns - event, bet, YES / NO,
"if YES wins you get $X" - and keep trading-desk jargon (shares, cents, spread,
liquidity-as-hero, order book) out of the primary path. Clarity for the newcomer,
but never a tone that patronises the fluent user.

**Example.**
- "Bet YES - if it happens, $5 becomes $13.20."
- Profile: "Your record: 12 calls, 9 right."
- Marketing / identity layer may say "predict" and "forecast"; the button the finger presses says "Bet".

**Anti-example.**
- "Buy 13 YES shares at $0.38 avg, spread 2¢."
- "Provide liquidity to this market."
- A wall of numbers with no event in sight (the Market Board / trading-grid view).

**Why (from the data).** `ux-patterns.md:82` - "A table with prices in cents is
the language of a trader, not a spectator"; `jtbd.md:316` rejects the Market
Board outright: "Мова трейдера, не глядача. Для Alex - дропаут", and `:194` (HJ1)
wants the payoff "без сложности трейдинга." The nuance is load-bearing and comes
from `personas.md:41-43`: **identity = analyst, action = bet** - use
"predict / forecast" in marketing and profile framing, accept "bet / position" in
functional UI, and the emotional payoff to reach for is "I was right / I called
it", not "I predicted." Do not over-explain to the fluent user either:
`personas.md:122` - Dan "knows what AMM and CLOB mean. He doesn't need a
tutorial." Competitor language shows the trap: Manifold "buying and selling
shares of a market", Polymarket cents, Kalshi trending to a "Bloomberg Terminal"
(see research.md Competitor language).

---

### 4. Design the loss; mark the win without lighting a fuse

**Rule.** After a result we explain what happened in plain words and offer one
calm next step. We acknowledge being right without confetti, and we never nudge
"bet again" after a loss.

**Example.**
- Win: "You were right. +$13.20. The market resolved YES, the side you held."
- Loss: "Here's what happened: Congress passed a stopgap bill two days before the deadline, so no shutdown. The market resolved NO; you held YES." + one next step ("Back to your bets").

**Anti-example.**
- "Congratulations, you WON! Ride your streak - bet again now!"
- After a loss: "Don't give up - win it back!" (or an empty screen with nothing).

**Why (from the data).** `personas.md:262` warns directly: "Confetti or 'you were
right!' copy without friction may accelerate the pattern"; `:68` names the current
competitor failure, "After a loss - nothing. No context, no 'here's what
happened,' no next step." The jobs demand a calm exit: `jtbd.md:101` (FJ5) "уйти
с ощущением честной игры, а не импульсивно увеличить ставку", `:145` (EJ3) "не с
желанием отыграться", `:303` scripts the loss screen as "один чіткий наступний
крок (не промо нової ставки)", because `:151` traces "early wins → overconfidence
→ loss-chasing." No competitor designs this: `jtbd.md:301` "Жоден конкурент не має
екрану між 'програв' і 'наступна ставка'"; the anti-model is Robinhood's "confetti
on first trade" (`competitors.md:85`). And the stakes are retention:
`personas.md:264` - "Platform betrayal ... is the documented #1 churn driver -
more than losing a bet."

---

### 5. Say the specific, provable thing - not a superlative

**Rule.** We name the concrete fact - a date, a source, a real count - instead of
marketing scale; if we cannot prove it today, we do not claim it.

**Example.**
- "214 markets resolved since March 2026. Verify every one on-chain."
- "All settlements are on the blockchain. Any user can check any resolved market."

**Anti-example.**
- "The world's most trusted prediction market."
- "Join millions of winners!" (unprovable at launch - reads as fake).

**Why (from the data).** This is the principle drawn straight from competitor
language: Polymarket "The World's Largest Prediction Market™", Manifold "the
world's largest social prediction market", Bet365 "world's favourite", Metaculus
"Collective intelligence for the public good" - **everyone leads with a
superlative scale claim** (research.md Competitor language). We cannot match that
claim at launch and, per `benchmark.md:108`, "Attempting to match their
authority signals ... with no history reads as fake." The honest alternative is
specified at `benchmark.md:96` - "N markets resolved correctly · since
[date] · all on-chain verifiable" - and `:111-113` "show the resolution source,
the criteria, and the outcome for every resolved market. Let the track record
build itself." Where they all write the same superlative, our difference is the
specific, checkable fact.

---

## How to use this

- These five are the test every product line must pass. When two lines disagree
  (see the flags in `microcopy.md`), the one that better fits these principles
  wins.
- The **Lexicon** and **Forbidden** sections below settle the word list and the
  bans; after them, the remaining step is the line-by-line rewrite of
  `microcopy.md` against this file.
- Sources of truth: `research/` (personas, jtbd, research, benchmark-trust,
  competitive-analysis, ux-patterns), `CLAUDE.md` (Design Principles: "Clarity
  first", "Trust signals everywhere"), and the competitor language section of
  `research/docs/research.md`.
- The five principles say *how* we sound. The three sections below make them
  operational: the **Lexicon** (which word), **Forbidden** (what we never write),
  and **Microcopy** (how each element type is written).

---

## Lexicon

One concept, one word. Each entry resolves a discrepancy already marked in
`microcopy.md` (step 01) - no new hunt, no invented terms; every word here
already exists in the product or the research. The reason is given in the
persona's own language, not in bureaucratic register.

| Concept | We say | Not | Why (persona / research) |
|---|---|---|---|
| The thing you bet on | **event** | market, question | Alex arrives "from the news", "follows news daily", "has opinions about everything" (`personas.md`); the job is literally "follow **events** with real skin in the game" (`jtbd.md` MJ). "Market" is the trader's word (P3); we keep it only in mechanics docs, never in the UI. |
| Putting money on an outcome | **bet** (verb + noun); **YES / NO** for the side | position, wager, trade, buy/sell shares | "Even the most analytical users say 'I bet', 'placing bets' ... nobody used 'I predicted'" (`personas.md:41`). "Position" is Dan's trader word. |
| Your record / identity layer | **predict / forecast**, and **"I was right / I called it"** | - | The split from `personas.md:41-43`: "identity = analyst, action = bet ... use predict/forecast in marketing and profile framing, accept bet/position in functional UI. The emotional payoff to activate: 'I was right / I called it'." So the button says **bet**; the profile and share say **predict / called it**. |
| Your bets, collected | **My Bets** | My Positions, Portfolio, Dashboard | Same reason as *bet*: it is the user's word for the stakes they took, not a trader's ledger. |
| Putting money in | **Add funds** | Deposit, top up, fund account | Alex wants "ordinary money without learning unfamiliar technology" (`jtbd.md` FJ3); "add funds" is ordinary-money language, while "deposit" carries the bank framing the product openly disclaims ("We are not a bank or broker", `benchmark.md`). *(Close call; if we prefer the shorter IA name, flip the whole product to "Deposit" - but pick one.)* |
| Keeping an event to watch it | **Save** (action) into **Favorites** (the shelf) | Bookmark, save event, watchlist | The user "follows" events they care about (`jtbd.md` FJ1: "an event you follow"); "save" is the plain everyday verb, "bookmark" is browser jargon. "Favorites" is the settled shelf name (the IA entity is "Saved events"). |
| Entering the account | **Sign in** (returning) / **Sign up** or **Create account** (new) | Log in, Login, Register (as a button) | The primary surface already frames it this way - "Sign in or create account", "Continue with Google". One pair, used on every screen. |
| Going to the feed | **Browse events** | Find events, See next events, Go to events, Back to feed, markets | One label for one action. The object is always **events** (never "feed" or "markets"), so the same button reads the same on the win screen, the empty state and the profile. |
| Placing the bet (the commit) | heading **"Place your bet"**, button **"Confirm bet"** | bare "Bet", "Buy", "Submit" | Verb + object that shows the result (Button rule); "Confirm" marks it as the real, consequential step (MJ: "a real stake ... with real consequences"). |

**How we address the user.** Always **"you" / "your"**, second person, direct, the
same on every screen. Never "users" or "the user" in copy, never a formal register
("Dear customer", "the client"), never third person about the reader. English has
no ти/ви split; the equivalent decision is register - **informal and plain, never
corporate**. We do not greet by name or say "Welcome".

**Which domain terms are allowed.** This product cannot avoid some finance and
crypto vocabulary; the rule is spectator-legible, not trader-fluent (P3).

- **Allowed (plain, load-bearing):** YES / NO, odds, chance / %, fee, payout,
  stake, resolve / resolution, wallet, USDC, on-chain, event.
- **Allowed once, with a plain gloss the first time:** USDC ("held 1:1"),
  on-chain ("anyone can verify it on the blockchain").
- **Not allowed in the UI (trader jargon):** shares, cents / ¢ pricing, spread,
  liquidity as a headline number, order book, position (for the user's own bet),
  buy / sell, long / short, AMM / CLOB, "market" for the event. These are "the
  language of a trader, not a spectator" (`ux-patterns.md`).

---

## Forbidden

What we never write. Each with the before -> after, so the ban is testable. These
are the tone leaks marked in `microcopy.md` (step 01) plus the register the
research rules out.

- **AI-cliche error copy.** No "Oops", no "Something went wrong", no filler.
  - Was: "Something went wrong reaching the network. Check your connection and try again." (real, flagged on the Event Feed and My Bets errors)
  - Better: "Couldn't load events. Check your connection and try again."
- **Cheerful greetings / congratulations.** No "Welcome", no "Congratulations!".
  - Was: "Welcome back! Great to see you again."
  - Better: "You're signed in." (or nothing - just show the feed)
  - Was: "Congratulations, you won!"
  - Better: "You were right. +$13.20." (P4: mark the win without a fuse)
- **Motivational / journey tone.** We state the concrete next step, we do not sell an experience.
  - Was: "Start your journey to being right - begin your winning streak today!"
  - Better: "No active bets yet. Find an event you have an opinion on and put a real stake on it." (real Active Bets empty copy)
- **Exclamation marks in system messages.** Calm by default.
  - Was: "Bet placed successfully!"
  - Better: "Bet placed. It is in My Bets now."
- **Emoji in system messages.** None in status, errors, confirmations, or on the win screen.
  - Was: "Deposit complete ✅🎉"
  - Better: "Funds added. Your balance is updated."
- **The word "successfully" (and "success").** Name the fact and the next step instead.
  - Was: "Withdrawal submitted successfully."
  - Better: "Withdrawal submitted. It will arrive in a few minutes."
- **Apologies.** We fix the problem, we do not apologise.
  - Was: "Sorry for the inconvenience, please try again later."
  - Better: "Couldn't load your wallet. Your funds are safe. Try again."
- **Internal codes and placeholder text in shipped copy.** The `(T2)`, `(T3)`, `S5`,
  "underlying screen dimmed" and "placeholder" strings flagged in `microcopy.md`
  are notes, never user-facing.
  - Was: "Your card was declined (T2). No funds were taken."
  - Better: "Your card was declined. No funds were taken. Try another card, or connect a USDC wallet."

---

## Microcopy

The principles applied at the level of a single element. Each rule ends with one
real example from our own screens (`wireframes/_screens.md` / `microcopy.md`) and the
principle it enforces.

**On the lexicon.** The words below are fixed by the **Lexicon** section above:
**event** (the object), **bet / YES / NO** (the action), **Add funds**, **Save**
into **Favorites**, **Sign in**, **My Bets**. The `[lexicon: ...]` tag on each
rule points to the entry it draws from.

### Button
**Rule.** An action verb whose object shows the result; never a bare "OK",
"Next", "Submit" or a naked "Bet".
- **Ours:** "Confirm bet" · "Add funds" · "Browse events" · "Try again". On the bet panel the payout line "$5 to win $13.20" sits beside the button so the result is visible before the press.
- **Not:** "OK" · "Next" · "Submit" · bare "Buy" (trader word).
- **From:** P3 (spectator verb, not "Buy") + P1 (the result is shown). `[lexicon: bet, Add funds, Browse events]`

### Screen heading
**Rule.** Name the place in the words the user already uses, from the lexicon; not
a generic or trading-desk label.
- **Ours:** "My Bets" · "Wallet" · "Notifications" · "How events resolve" (a How It Works section).
- **Not:** "Dashboard" · "Portfolio Overview" · "My Positions" (trader framing).
- **From:** P3. `[lexicon: My Bets - "bets", not "positions"]`

### Form field
**Rule.** The label says *what* to enter, the hint says *how*, the validation
error says *exactly what to fix* - all in specific words.
- **Ours (Deposit):** label "Amount to add" · hint "Minimum deposit is $10. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead." · error (minimum-not-met) "Minimum deposit is $10. Enter $10 or more to continue."
- **Not:** label "Amount" · no hint · error "Invalid input" or "Something went wrong".
- **From:** P1 (say the specific thing) + P2 (fee / KYC surfaced before the ask). `[lexicon: Add funds]`

### Empty state
**Rule.** Say why it is empty and give the one next step; never a bare icon or a
cheerful "Nothing here yet".
- **Ours (Active Bets, empty-new):** "No active bets yet. You haven't placed any bets. Find an event you have an opinion on and put a real stake on it." + button "Browse events".
- **Not:** an empty panel with only an illustration · "It's quiet in here!"
- **From:** P1 (concrete why) + P3 (spectator framing: "an opinion", "a real stake"). `[lexicon: event, Browse events]`

### Error
**Rule.** Say what happened and what to do next, plainly; no apology, no joke, no
generic filler.
- **Ours (Wallet):** "Couldn't load your wallet. We couldn't fetch your balance and transactions. Your funds are safe; this is a display issue. Try again."
- **Not:** "Oops! Something went wrong." (our own flagged cliche on the Event Feed and My Bets errors) · any "😅"/"!" softener · leaked codes like "(T2)".
- **From:** P2 (reassure about money: "your funds are safe") + P5 (specific, no filler). `[lexicon: -]`

### Loading
**Rule.** Stay silent (a skeleton), or name exactly what is loading; never a
hype line.
- **Ours:** the Event Feed loading state is a silent skeleton grid; the bet execute state says the specific thing, "Registering your bet on-chain...".
- **Not:** "Please wait..." · "Loading, hang tight! 🚀".
- **From:** P1 (specific) + P4 (no hype). `[lexicon: bet]`

### Success
**Rule.** Name the fact and the next step; mark being right, but do not celebrate.
- **Ours (Win):** "You were right. +$13.20. The market resolved YES, the side you held." + "See next events".
- **Not:** "Congratulations, you WON! Ride your streak - bet again!" · confetti.
- **From:** P4 (mark the win without a fuse) + P5 (state the fact). `[lexicon: -]`

### Dangerous or irreversible action
**Rule.** Before the press, say what will happen and what cannot be undone; state
the change, do not hide it behind a bare "Confirm".
- **Ours (Bet reconcile, real):** "The price moved while you signed in. Was 38%, now 41%. Payout $13.20 -> $12.20 for $5." then "Confirm at new price (41%)". For a Wallet withdrawal: "Sending USDC to a wallet address you control. On-chain transfers are final and cannot be reversed - check the address before you confirm." then "Confirm withdrawal".
- **Not:** a bare "Confirm" with the price change or the finality hidden · "Are you sure?".
- **From:** P2 (transparency before the ask) + P1 (show the number that changed). `[lexicon: bet]`

---

_With these sections `voice.md` is complete: the five principles (how we sound),
the Lexicon (which word), the Forbidden list (what we never write), and the
element rules (how each line is written). From here every product line in
`microcopy.md` is written and rewritten against this file._
