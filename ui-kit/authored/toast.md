# toast

## Sources

- `ui-kit/docs/inventory.md` L144 - "Toast (`.toast`: message + close, stacked)", filed L2, and its location column says **toasts (spec page)**: the row itself records that this component has no home in the product.
- The painted screens: exactly 1, `ui-visual/toasts.html`, which is the catalogue of every toast rather than a screen a person reaches.
- `voice/docs/microcopy.md` Step 15, where the toast copy was written with the other system nodes (404, 500, maintenance, cookie-consent) rather than with a flow.
- `wireframes/_critique.md` L245, where those five system pages were found ABSENT and built, which is why the catalogue exists and the placements do not.
- `ui-kit/docs/backlog.md` S11's neighbourhood: `.tc-page`, the page a toast is demonstrated on, was declared in `components/toast.css` and had to move to `components/base.css`, because the catalogue is not part of the component.

## Purpose

The product's transient message: something happened, it was not important enough to stop you, and it will go away. A line of text, a mark for the kind, a close, and a stack so that two of them do not fight for the same corner.

**It stands on one screen and that screen is its own catalogue.** No flow in this product currently raises a toast: the deposit confirms in its sheet, the bet confirms in the panel, an error takes a `notice`. So this component is a decision that has been drawn and not yet spent, and the honest reading of its one screen is not "we use toasts everywhere" but "we agreed what a toast would look like before the first flow needs one".

## Anatomy

- `.toast-group` - the stack. It exists so the second message has a defined place, which is the part a person only notices when it is missing.
- `.toast` - one message: the quiet card, its mark and its text.
- `.toast-inner` - the row inside it.
- `.toast-msg` - the sentence. One sentence, because a toast that needs two is a `notice`.
- `.toast-close` - the dismiss, and the only control in the component.
- `.toast-error` - the error kind, which takes the outcome red on its mark and its edge and nowhere else.

## When to use

When something succeeded and the person does not need to do anything about it, and only then. A toast is the weakest thing the product can say: it does not block, it does not persist, and a person who looks away misses it entirely.

Anything a person must act on, must read, or must be able to find again is a `notice`: it stays on the page, it can carry a control, and it does not disappear on a timer. Anything that must be answered before continuing is a `dialog`.

Because nothing raises one yet, the first flow that wants a toast is also the moment to check that a toast is the right answer. The question to ask is what happens to a person who blinks.

## Rule

One sentence, one kind, one dismiss, and it must be safe to miss: if losing the message costs a person anything, this is the wrong component.

## Anti-rule

Never use it for an error a person has to act on: an error with a next step is a `notice`, which stays on the screen and can carry the control, and a five-second message about money that has not arrived is a support ticket rather than a notification.

Seen: `voice/docs/microcopy.md` Step 15, where the toast copy was drafted alongside the 404, 500 and maintenance pages, and every error in the product's actual flows was written as a `notice` or a state screen instead. The split was made in the copy before it was made in the system.

## States

None, and it is declared in `ui-kit/_levels.py` STATIC. A toast is read and then it leaves; the one thing in it a person can press is the dismiss, and on 2026-08-06 the dismiss went to `components/iconbtn.css` as the atom's fifth face. This file keeps `flex:0 0 auto` on it, which says the message takes the slack and the control does not, and that is a fact about a two-item flex row rather than about what an icon button looks like.

One thing changed on the way out and it was decided rather than carried: the hover. This control used to brighten its own edge where the other 388 outlined circles in the product tint their ground and take a brass edge. Four against 388, so the four were the divergence. `ui-kit/docs/backlog.md` S44 asked it and it is answered; the picture is on the iconbtn page.
