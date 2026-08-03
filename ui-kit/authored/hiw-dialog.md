# hiw-dialog

## Sources

- `ui-kit/docs/inventory.md` L129 - "How-it-works dialog (`.hiw-dialog`: hero + icon chips + FAQ)", filed L3, on every header page, state open, 87, art column marked.
- `ui-kit/docs/inventory.md` L60 - the button that opens it, which belongs to `components/header.css` and stands next to the logo. The opener and the sheet are two components on purpose.
- `voice/docs/microcopy.md` Step 21 - "How it works header dialog (button next to the logo, 87 header pages)", where this became reachable from everywhere rather than from one page.
- `ui-kit/_levels.py` RAISE, which carries the longest reason in that file: the arithmetic cannot read this component's level while the standalone PAGE and the shared sheet live in one vocabulary. That is `docs/backlog.md` item 16.
- The 105 painted screens, `ui-visual/how-it-works.html` for the page and any header screen for the sheet.

## Purpose

The answer to "what is this, and what happens to my money", available from the logo row of every screen without leaving the one you are on. A hero line, a row of icon chips for the mechanics, and an FAQ, ending in a link to the full page for a person who wants more than a sheet.

It exists because the product's first design principle is that a new user is never lost, and the place a new user gets lost is not a screen, it is a moment: halfway down an event, deciding whether this is real. A dialog answers there. A page would have made them leave.

## Anatomy

- `.hiw-dialog` - the sheet. A `dialog` element, so Esc and the backdrop already work and no script owns the open state.
- `.hiw-hero`, `.hiw-hero-inner`, `.hiw-tagline`, `.hiw-glow` - the head: the one-line claim and the brass wash behind it, which is the only decorative surface in the component.
- `.hiw-label` - the eyebrow above the claim.
- `.hiw-body`, `.hiw-cols`, `.hiw-col-main`, `.hiw-col-side` - the body and its two columns, which become one at 360.
- `.hiw-sec`, `.hiw-sec-txt`, `.hiw-ic` - a mechanic: an icon chip, a heading and a plain sentence. The icon is a mark, not an illustration.
- `.hiw-faq` - the questions, as `<details>`, so the sheet opens short.
- `.hiw-full`, `.hiw-arrow` - the way out to the full page.
- `.hiw-close` - the dismiss.

## When to use

From the header, on any screen, at the moment a person hesitates. That is its only invocation and it is why the opener sits beside the logo rather than in the footer: the footer is where a person goes when they have already decided to look something up.

Not as an onboarding gate. Nothing in this product blocks a first screen with an explainer, and the sheet is opened by a person rather than shown to them.

Not for one mechanic. If a screen needs to explain one thing at the moment it happens - what a fee is, what "resolves" means, that funds are held 1:1 - that is a `notice` standing where the question arises, and it stays on the page after the sheet would have closed.

## Rule

It opens over the screen a person was reading and returns them to it unchanged: nothing in this sheet navigates, and the only link out is the last thing in it.

## Anti-rule

Never build it as a second `dialog` shell: the sheet material, the head, the close and the mobile-versus-modal behaviour all belong to `dialog`, and this component owns only what is inside the body. A copy of the shell here would be a second answer to how an overlay looks, and this product has one.

Seen: `voice/docs/microcopy.md` Step 27, "One dialog, one copy, and the page that was left as a document", which closed exactly that split elsewhere, and gate 19 in `ui-kit/_check_kit.py`, which now fails the build when a dialog that also has a standalone page carries two markups. This component is the one where the split is still OPEN: `ui-kit/_levels.py` RAISE says so, and `docs/backlog.md` item 16 is the row.

## States

- `button.hiw-close @dialog.hiw-dialog` - The dismiss, at rest, hovered, held and focused. It sits on the brass wash rather than on the sheet stone, so its quiet face is measured against the head and not against the body.
- `a.hiw-full @dialog.hiw-dialog (2)` - The link to the full page: the last thing in the sheet, with its arrow. Underlined at rest rather than on hover, because it is the only exit and a person should see it without pointing.
