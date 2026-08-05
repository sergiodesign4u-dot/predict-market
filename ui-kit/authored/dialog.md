# dialog

## Sources

- `ui-kit/docs/inventory.md` L120 - "Shared dialog shell (`dialog.app-dialog`, stone-plate material)", filed L3, "every page (emitted in shell)", states "open / close (backdrop, Esc); modal (desktop) / sheet (mobile)", 104.
- `ui-kit/docs/inventory.md` L127 and L128 - the bottom-sheet overlay with its grab and backdrop (17 screens) and the sign-in dialog with its four states.
- `CLAUDE.md` and gate 19 in `ui-kit/_check_kit.py` - "A dialog that also has a standalone page is one markup, not two": the canonical copy is the one in `ui-visual/event-feed.html`, and only the head, the wiring and the state screens may differ.
- `voice/docs/microcopy.md` Step 22, Step 23 and Step 27 - the shared dialog hero across 76 pages, Withdraw becoming a dialog in both trees, and "One dialog, one copy, and the page that was left as a document", which is the step that closed the split gate 19 now holds.
- R9 in `ui-kit/docs/architecture.md` - the seventeen screens whose content IS an invoked overlay still carry the bottom nav, because these are pages in this product and not modal traps.
- The 105 painted screens.

## Purpose

The one overlay in the product, and the material it is made of: a stone plate, a head, a body, a close, and a backdrop that dismisses. Sign in, Add funds, Withdraw, the win and loss outcomes and the how-it-works sheet are all this shell with different contents.

Its shape is decided by a stance rather than by a pattern. An overlay here is a PAGE that happens to be drawn over another one: it has a URL in the painted tree, it keeps the bottom nav, and a person who changes their mind leaves the way they leave anything else. That is why the close is a courtesy rather than the only exit, and why nothing in this component traps focus into a corner a person has to argue with.

## Anatomy

- `.app-dialog` - the shell. A real `dialog` element, so Esc, the backdrop and the top layer are the browser's job and not a script's.
- `.sheet-head`, `.sheet-sub` - the head and its one-line subtitle, which is the same hero on every overlay since Step 22.
- `.sheet-body` - what the overlay is for. Everything inside it belongs to another component.
- `.sheet-close` - the dismiss, and since 2026-08-05 it is the ONLY one in the product's overlays. A 32px disc 12px in from the corner, a pill, a 34 per cent scrim ground under a hairline edge, and the close icon at 16px in `--text-on-photo`. It was three declarations before: this file wrote it twice, once for `.outcome-dialog` and once for everything else, and `components/hiw-dialog.css` wrote it a third time as `.hiw-close`. The three agreed on every value that matters and disagreed on the corner, on the `z-index` and on how the cross is drawn.
- `.fine` - the small print at the foot of an overlay: the line that says what happens to the money and on what terms.
- `.signin-dialog` - the auth variant, which is the only one with four states of its own.
- `.outcome-dialog` - the win and loss variant. It is named for the outcome because that is the one place in this product where green and red are allowed to mean something.

## When to use

When the answer is needed before the flow continues, and the flow is worth returning to. Signing in mid-bet, adding funds mid-bet, confirming a withdrawal: in every case there is a page underneath that the person still wants.

At 360 it is a sheet and above the breakpoint it is a modal, and that is one component rather than two: the same markup, the same copy, a different geometry.

Not for something a person can safely miss - that is a `toast` - and not for something that stays true after they look away, which is a `notice` standing in the page. The question to ask is whether the screen behind it still makes sense while this is open. If it does not, this is right.

Never as a second copy of a page. Five of these overlays also exist as standalone screens, and gate 19 exists because they were two markups once: one canonical body, and only the head, the wiring and the state screens may differ.

## Rule

The overlay is a page over a page: the bottom nav stays, the backdrop and Esc dismiss, and nothing in it prevents a person from leaving without answering.

## Anti-rule

Never build the sheet's material a second time inside the thing it holds: `hiw-dialog` is the case that proves it, and it owns only the body of its sheet while the plate, the head, the close and the sheet-versus-modal behaviour come from here. A component that redraws the shell would give this product two answers to what an overlay looks like.

Seen: gate 19 in `ui-kit/_check_kit.py`, which was written because a dialog and its standalone page had drifted into two markups, and `voice/docs/microcopy.md` Step 27, the step that reconciled them. The split was found in the copy first and in the markup second, which is the usual order here.

## States

- `button.sheet-close @dialog.signin-dialog` - The dismiss, at rest, hovered, held and focused, **and since 2026-08-05 this one gallery is every close button in the product**: the 32px disc answers a pointer with more scrim and nothing else, 34 per cent at rest, 55 hovered, 72 held. It is deliberately quiet: the backdrop and Esc are the real exits and this is the visible one, so a person who is looking for a way out finds it without being urged. It merged three declarations into one, and ten controls in the stand set now sit in these four pictures where nine sat in them before.
- `button.sheet-close @dialog.hiw-dialog` - **The same disc on the how-it-works head, and the ONE thing that separates it is the ring.** It takes `--text-strong` rather than the system's brass, because `.hiw-glow` puts a brass radial in exactly the corner the ring lands in and a brass ring reads 2.52:1 against it. Measured with the element focused: `rgb(255, 255, 255)` here against `rgb(215, 172, 83)` on every other head in the Vault, `rgb(33, 31, 25)` against `rgb(104, 79, 24)` in daylight.

  **This group did not exist until 2026-08-05, and the sentence that stood in its place said so.** A face was nine properties and the outline was not one of them, so the tenth occurrence of this control joined the group above instead of opening its own, and the gap had to be written out by hand right here to stop the page reading as "this control has one answer" while the stylesheet said two. The ring is the tenth value now, `ui-kit/_verify/browser.cjs` `face()`, and the instrument opens the group by itself. `ui-kit/docs/backlog.md` S40, closed, and `ui-kit/docs/defects.md` row 62.
- `a @dialog.signin-dialog` - A link in the sign-in body, all four faces. Underlined at rest, because in an overlay about an account the terms a person is agreeing to must be visibly reachable before they act.
- `a.hiw-full @dialog.hiw-dialog` - The how-it-works sheet's link to its full page, photographed here as well as on `hiw-dialog`: the same element seen from the shell that holds it, which is what a shared component's page is for.
- `a @dialog.win-dialog` - A link in the outcome overlay. This is the one dialog variant where green and red carry meaning, and the link takes neither: the outcome colours state the result, and a control that borrows one would read as a recommendation about the next bet.
