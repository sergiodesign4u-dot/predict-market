# profile

## Sources

- `ui-kit/docs/inventory.md` L154 - "Identity row (`.idrow`: ringed 72px avatar `.av`, name, handle, Edit pill)", filed L3, on my-profile and public-profile, states "own (Edit) / read-only".
- `ui-kit/docs/inventory.md` L156 - "Reputation stat-grid (Track record: tiles, brass win-rate hero tile)".
- `ui-kit/docs/inventory.md` L158 - "Share-card gallery (`.gallery` horizontal rail of win cards)", 7, art column "art / generated".
- `ui-kit/docs/inventory.md` L155 - "Section divider (`p.pos-status`, brass tick)". **The row said `components/position.css` and was false when it was read on 2026-08-03**: the six rules including the brass tick were in `components/profile.css`, and `components/position.css` did not mention the class once. It was the second row of that table found naming the wrong file; the first was L163, found while writing `account`. **Both are closed now, and in opposite directions**: L163 was corrected to `components/position.css`, and L155 was made true by MOVING the class to the file its name always claimed, so the divider of a position list is no longer declared by the profile that happens to show one. `ui-kit/docs/backlog.md` S21, and gate 34 now rebuilds those cells rather than trusting them.
- `voice/docs/microcopy.md` Step 13 - the profile copy, kept rather than rewritten because it was already spectator-clean, and the line that decides this component: **"Reputation = the track record, not the balance."** Also "Resolved predictions (public)", "Public track record - read-only", "Edit name & avatar".
- `voice/docs/voice.md`, the Lexicon row for the identity layer - "identity = analyst, action = bet ... use predict/forecast in marketing and profile framing, accept bet/position in functional UI". This is the one component on the profile side of that split, so it says *predictions* where the rest of the product says *bets*.
- The 7 painted screens, and the redesign recorded in this project's Stage 08: identity-first, a reputation stat-grid, and CSS-only Track-record / Past-wins / Resolved tabs whose structure stayed grey.

## Purpose

Who somebody is here, measured by what they got right. A ringed avatar, a name and a handle, then a grid of figures with the win rate as the largest of them, then the wins they chose to keep.

The component is built on one refusal. In a product where every screen can show a balance, a profile that led with money would make the identity a wallet, and the copy says so in a gloss written into the screen itself: reputation is the track record, not the balance. So the figure the layout makes biggest is the win rate, the history is public, and the balance is not on this screen at all.

## Anatomy

- `.idrow` - the identity row: avatar, name, handle, and the Edit pill on your own profile only.
- `.av` - the ringed avatar. A portrait, so it is content.
- `.who` - the column beside it.
- `.name` and `.handle` - the display name and the handle under it. The handle is the stable one; the name is the one a person may change.
- `.edit` - *Edit name & avatar*. Present on your own profile, absent on somebody else's, which is the whole difference between the two screens.
- `.gallery` - the horizontal rail of share cards: the wins a person kept. Generated art, and the only place in the product where a past result is displayed as an object rather than as a row.

## When to use

On the two profile screens, and only there. A person's identity appears elsewhere in this product as a name on a comment or a row in a table, and that is deliberately thin: the full record is a place you go to, not something that follows a person around the interface.

Your own profile and somebody else's are the same component with one control removed. The read-only screen states that it is read-only rather than showing a disabled Edit, because a greyed control invites a person to work out why.

Never as an account-settings surface. Nothing here changes an email, a wallet or a preference; the identity row edits a name and an avatar, and everything else about an account lives in the wallet and its dialogs.

## Rule

The record is what is measured and the balance is not on the screen: a profile in this product answers how often somebody was right, and nothing in it may make being rich look like being right.

## Anti-rule

Never build its history list here: a resolved prediction is a `position` row, the same component that draws My Bets, and drawing a second version on the profile would put a person's public record and their private one in two files that agree by hand. The tabs above it are `tabs`, for the same reason.

Seen: `ui-kit/docs/inventory.md` L159 - "Resolved-predictions history (`.pos-side.pos-won` green / `.pos-lost` red)", filed under `components/position.css` and located on **my-profile, public-profile, active-bets-history**: three screens, two of them this component's, one of them not, and one file drawing all three. The row is what stopped it becoming two.

## States

- `button.edit @profile-identity` - *Edit name & avatar*, at rest, hovered, held and focused. It is the only control the component owns, and it is a quiet pill rather than a brass action: on a screen about a record, editing your own name is not the primary thing anyone came to do.
