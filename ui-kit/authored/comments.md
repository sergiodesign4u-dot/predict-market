# comments

## Sources

- `ui-kit/docs/inventory.md` L108 - "Comment (`.cmt`: user, text, actions, badge, reply)", filed L3, on the Event Detail Comments tab, states "logged-in / logged-out (`.cmt-signin` prompt)", 36.
- `ui-kit/docs/inventory.md` L109 - "Comment composer (`.cmt-compose`)", the same tab, the same two states, 7.
- `voice/docs/microcopy.md` L312 and L316 to L317 - the tab and its controls as inventoried: *Comments*, the count line *128 comments*, and the sort *Newest* / *Top*.
- `CLAUDE.md` - "User-written content (event questions, comments, usernames, sample figures) is never rewritten." This component is the one whose entire body is that content.
- The 9 painted screens, every one an Event Detail variant, and the specimen `ui-kit/specimens/comments-thread.html`, which renders it inside `tabs` rather than alone.

## Purpose

What other people think, under the event they think it about. A comment is an avatar, a name, an optional badge, the text, a time and two actions; the composer above the list is where a signed-in person adds one, and where a signed-out person is asked to sign in instead of being shown a dead box.

It is the only block in this product whose content the product does not write and may not edit. Everything else here is copy that went through `voice/docs/microcopy.md` before it shipped; a comment goes up as typed. The component's whole job is to hold text it has no opinion about and still look like it belongs to this system.

## Anatomy

- `.cmt-list` - the thread.
- `.cmt` - one comment, and `.cmt-body` the column beside the avatar.
- `.cmt-av` - the avatar, which is a portrait and therefore content.
- `.cmt-user`, `.cmt-meta` - who and when.
- `.cmt-badge` - the one mark the product adds to a person: a record worth knowing about, and nothing else. It is the identity layer the voice contract calls predict-and-forecast rather than bet.
- `.cmt-text` - the comment, wrapped and never clamped. A truncated opinion is an opinion misquoted.
- `.cmt-actions`, `.reply` - the two things a reader can do.
- `.cmt-compose`, `.cmt-controls`, `.cmt-input`, `.cmt-post` - the composer: the field, its row of controls and the post button.
- `.cmt-signin` - what stands in the composer's place when nobody is signed in. It is a prompt with a way in, not a disabled field.

## When to use

On an event, under the analysis, inside the Comments tab. There is one thread per event and it is the fourth thing a person meets on that screen, after the odds, the argument and the chart.

Not as a general discussion surface. The product has no forum, no profile wall and no direct messages, and a comment here is anchored to one question by design: it is the argument about THIS event, which is what makes it worth reading beside the odds.

Not as a notification source. The third design principle is that engagement is about events rather than money, and a reply is not an event. Nothing in this component raises anything.

## Rule

The text a person wrote goes up as they wrote it, whole: no truncation, no clamp, no tidying, and the system's only addition to a person is `.cmt-badge`.

## Anti-rule

Never let the sort strip above the thread grow into a second tab bar: *Newest* and *Top* are a segmented control and belong to `tabs`, which owns `.seg` and already draws the same strip on the rules and the chart range. A second implementation here would be the third copy of one shape.

Seen: `ui-kit/docs/backlog.md` S16 and S17, both closed on 2026-08-03 and both the same defect - one shape declared more than once and kept in step by hand, in five names and then in two. The strip above this thread is the same shape already declared in `components/tabs.css`, and the reason it has not become a third is that it was never written here.

## States

- `button.cmt-post @tabs-detail` - The post button, at rest, hovered, held and focused. It is the composer's one commitment and it takes the quiet control face rather than the brass one: posting an opinion is not the screen's primary action, backing it is.
- `button @tabs-detail` - A comment's own action, all four faces. Quiet at rest, ground answers, and the row does not shift: a thread where every hover nudges the text is a thread that is hard to read while pointing.
