# bets-table

## Sources

- `ui-kit/docs/inventory.md` L110 - "Biggest bets columns (`.hold-col` / `.hold-row`)", filed L3, on the Event Detail Bets tab, states "binary / multi (outcome-tagged)", 16.
- `ui-kit/docs/inventory.md` L111 - "Bets table (`.ptable`, \"you\" highlight)", states "logged-in (your row) / logged-out", 9.
- `ui-kit/docs/inventory.md` L112 - "Activity feed (`.act-row`)", the Activity tab, 9.
- `voice/docs/microcopy.md` Step 14, the content-tabs cluster - the rewrite that made this component readable: *Top Holders* became **Biggest bets**, *Positions* became **Bets**, "1,240 shares" became "$1,240", the columns *Holder / Side / Shares / Avg / Value* became **Bettor / Side / Amount**, and "whale_07 bought 500 YES at $0.35" became "whale_07 bet $175 on YES". The reason is recorded as P3: a spectator reading, not a trader one.
- `voice/docs/microcopy.md` L1016 - the same cluster before it was done, held for its own sub-pass because "this is a Polymarket-style social/trading panel built on trader vocabulary" and reworking it was a real design question.
- `voice/docs/microcopy.md` L1170 - the standing note that the "Biggest bets" figures are not reconciled row-for-row against the "Bets" table, "which is acceptable for a wireframe".
- `ui-kit/_levels.py` STATIC - "the holders and activity rows. Read-only figures; a row opens nothing".
- The 9 painted screens, all Event Detail variants.

## Purpose

What other people did, under the event they did it on. Three lists behind three tabs: the biggest bets by outcome, the full table of bets with your own row marked, and the activity feed of what just happened.

It is the product's social proof, and its whole design problem is that social proof about money reads as a trading terminal unless somebody stops it. The Step 14 rewrite is that stopping: no shares, no average price, no buy and sell, no order sizes. A person, a side, an amount, and when.

## Anatomy

- `.hold-cols`, `.hold-col` - the two columns of biggest bets, one per outcome.
- `.hold-row` - one of them: rank, who, how much.
- `.hold-rank`, `.hold-name`, `.hold-amt` - the three cells of that row. The amount is a dollar figure, which is what it became when "shares" left.
- `.hold-out` - the outcome tag, for a multi-outcome event where the columns are not simply YES and NO.
- `.ptable` - the full bets table: bettor, side, amount.
- `.you` - your own row in it, marked rather than moved to the top, so the ordering still means what it says.
- `.act-list`, `.act-row`, `.act-txt`, `.act-time` - the activity feed and one line of it: what somebody did, and how long ago.
- `.lg-item` - the logged-out face, where the lists still show and the prompt to sign in stands where your row would be.

## When to use

Inside the Event Detail tabs, under the analysis, never above it. A person reading an event should meet the odds, the reasons and the rule before they meet the crowd, because a list of what other people did is the most persuasive and least informative thing on the screen.

Logged out, the lists still show. Social proof that requires an account is not proof, it is a gate, and this product asks for the account at submit and not at the door.

Not on a feed, a card or a profile. The rows are about one event; a person's own record across events is `position`, which draws the same kind of row from the other direction.

## Rule

Every row is a person, a side and an amount, in that order and in plain money: the moment a column needs a gloss to be understood, it is a trader's column and does not belong here.

## Anti-rule

Never let these rows borrow the outcome colours from `yesno`: a side in this table is a fact about somebody else's bet, and tinting the column green and red would turn a list of what happened into two stacks of controls on the screen that also carries the one control that commits.

Seen: `voice/docs/microcopy.md` Step 14, which had to rewrite this exact surface out of trader vocabulary once it shipped - and the row above it, L1016, where the cluster was held back precisely because "shares / liquidity are forbidden" and the panel had been built on them anyway. The pressure this anti-rule resists is the one that already won once here.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC: these are read-only figures and a row opens nothing. There is no sort here, no expand, no link on a name, and the one thing that changes between screens - your row being marked - is a fact about who is signed in rather than an answer to a pointer.

**One thing about this component is worth knowing before editing it, and it is not a style.** The copy left the trader's vocabulary in Step 14 and the CLASS NAMES did not. `.hold-row`, `.hold-name`, `.hold-amt` and `.hold-out` draw a tab labelled *Biggest bets*; `.ptable` draws a tab labelled *Bets*. `components/tabs.css` carries the same split in `.ed-panel-holders` and `.ed-panel-positions`. Nothing is wrong on the screen, and a person grepping for `holder` will find the system and a person grepping for `bets` will find the product. The file name is on the product's side of that split and the classes inside it are not.
