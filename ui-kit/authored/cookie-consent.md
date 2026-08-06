# cookie-consent

## Sources

- `voice/docs/microcopy.md` L1226 - the banner sentence, recorded with the verdict "plain, no dark pattern"; and L1227, the three actions *Accept all* / *Reject all* / *Manage*, with the reason "reject as easy as accept (equal weight)".
- `wireframes/_critique.md` L245, where the five system nodes including this one were found ABSENT from the product and built.
- The 2 painted screens: `ui-visual/cookie-consent.html`, the page, and `ui-visual/toasts.html`, where the banner stands in the catalogue.
- `components/base.css`, the fonts paragraph: the reason a font host may not be called is that the request carries a visitor's IP to a third party BEFORE this banner has asked anything, and gate 20 fails the build on it.
- `ui-kit/docs/inventory.md` has no row for this component, which is itself a finding and is recorded in this file's Purpose.

## Purpose

The one place where the product asks permission instead of asking for a decision about money, and the one place where the honest answer costs the product something. GDPR and ePrivacy require a real choice, and a real choice means Reject is exactly as easy as Accept.

Everything about the banner is that sentence made into markup: three actions of equal weight, no pre-ticked category, plain language about what each kind of cookie does, and no second-guessing after a person answers. It is the component most likely to be quietly degraded later, because every dark pattern in this space is a small change to one of those four things.

## Anatomy

- `.cc-banner` - the band. `.cc-inner` is the row inside it and `.cc-text` the sentence.
- `.cc-actions` - the three controls, and their EQUAL weight is the decision: none of the three is the brass action, because a brass Accept beside a quiet Reject is a choice with a thumb on the scale.
- `.cc-btn` - one of those controls, from the quiet chip family.
- `.cc-manage` - the second layer, where the categories are.
- `.cc-cats`, `.cc-cat`, `.cc-cat-main`, `.cc-cat-name`, `.cc-cat-desc` - one category: its switch, its name and one plain sentence saying what it does. The description is not optional; a category a person cannot understand is not a category they can consent to.
- `.cc-policy` - the link out to the full text, which is the only link in the component.
- `.cc-note` - the line under the categories.
- `.cc-page`, `.cc-ph`, `.cc-ph-line`, `.w90` - the standalone page and its placeholder lines, which is where the banner is read rather than answered.

## When to use

Once, on first arrival, before anything measurable happens. The banner is the whole product's gate, not a screen's, and it is why the fonts in this system are served from this repository: a font host would have carried a visitor's address to a third party before the banner had drawn.

The page behind it is for the person who wants to change their mind. It is not a marketing page and it does not repeat the argument for consenting.

There is no third use. A permission prompt for notifications is not this component: it is the operating system's, and the product's own screen for it is a `notice` explaining why the ask is coming.

## Rule

Reject is as easy as Accept, always: same weight, same size, same distance from the thumb, and no category ticked before a person has looked at it.

## Anti-rule

Never make one of these three the brass action: a primary `button` here would turn a legal choice into a recommendation, and the product would be reading consent it did not honestly get.

Seen: `voice/docs/microcopy.md` L1227, where the equal weight of the three actions was written into the copy record with the reason, before the component was drawn. That row is what this rule is enforcing, and it is the only place in the repo where it is written down.

## States

- The three answers are no longer captured here. They went to `components/button.css` on 2026-08-06 as `.btn.btn-secondary.btn-md`, which is what they already were in every value but one: their font was 13 against a ramp of 12 and 14. What this file still owns about them is how they share the row, `flex:1 1 auto` and a 96 floor, so three of them divide the banner and none collapses under its own label.
- `input @cookie-consent` - A category switch, off. The necessary category ships disabled and on, which is a fact about what the switch can do rather than a style.
- `input @cookie-consent (2)` - The same switch on, in brass rather than green, because green means an outcome in this product and consent is not one.
- `a @cookie-consent` - The policy link, the one link in the component, underlined at rest rather than on hover: a person deciding what to allow should be able to see where the full text is without pointing at it.
