# navitem

## Sources

- `ui-kit/docs/atoms.md`, which named this atom before it had a file: **a thing a person taps that GOES somewhere and that draws NOTHING until it is pointed at.** It is the second atom to be cut against the map and the first that had no file at all, so this is a new component rather than a move.
- `components/bottomnav.css`, where the slot lived until 2026-08-06, and `components/header.css`, where the account-menu row did. Neither file was wrong to have drawn one; both were wrong to be the only place it was written down.
- `ui-kit/_worn.py`, the census, which files both as **nav**: pressing one takes you somewhere, and nothing is carried between presses.
- The measurement that started it, in `ui-kit/docs/atoms.md`: reading the four `navitem` kinds out at 1440 and 380 is what found the social mark in the wrong atom, and what found the sub-category row measuring as a pill on a phone.

## Purpose

The control a person uses to move around the product. It is the quietest thing in the system on purpose: no ground, no edge, no corner, the width of the row it sits in. Where a `button` commits and a `chip` chooses, this one goes.

## Anatomy

- `.nav-item` - the atom, and it is four declarations: full width, transparent, no border, no corner. Everything else belongs to a face. **It is an `<a>` where the slot navigates and a `<button>` where it opens the sign-in sheet**, which is the right answer to both and is what `ui-kit/docs/defects.md` row 78 settled on 2026-08-07: until then the navigating one was a `<button>` inside an `<a>`, two controls in the tab order where a person can see one.
- `.nav-item.nav-slot` - a mark over a label, centred, 10px, `--text-muted`, in the bottom bar. Its current-page state is the one thing the bar says at a glance.
- `.nav-item.nav-row` - a line of a menu: full width, left aligned, 11px, `--text-primary`.

## When to use

For anything that navigates and stands in a list, a bar or a menu. If it commits, opens or submits, it is `button`; if it selects among alternatives and carries a value, it is `chip`.

## Rule

**The current item is stated by ONE thing.** In the bottom bar the ink says where you are, so the ground answers the pointer and the colour does not. If pointing at a slot pulled its label toward brass, the one signal the bar carries would be said by two different things at once, and a hover can stick after a tap on a phone, so the wrong slot would go on claiming to be current after the finger left.

**The state is reached from the ancestor, and the attribute is what is named.** `aria-current="page"` sits on the `<li>` in this product, so the rule is `[aria-current="page"] .nav-item.nav-slot`. It names the attribute alone and not the bar, because being the current item is the ATOM's state wherever the atom stands.

**Every hover here is written at the face's own two-class weight.** `.nav-slot:hover` would be (0,2,0) and would lose to the current-page rule at (0,3,0) on exactly the slot a person taps most. `components/bottomnav.css` bought the same weight by naming the `<li>`; this file buys it by naming the atom and the face together, and the press comes last at the same weight so that a tie is broken by source order.

## Anti-rule

Never give one a ground at rest. The moment a nav item has a fill, a row of them reads as a row of buttons and the current one stops being the only thing standing out.

Never draw one from `button`. That family gives a quiet control `--bg-control` and a 10px corner, which is the opposite of every value here.

Seen: `ui-kit/docs/atoms.md`, and `ui-kit/docs/backlog.md` S45 and S46 for the two things this atom's arrival did not settle.

## States

- `a.nav-item.nav-slot @navitem-slots` - **The slot at rest, all four faces.** `--text-muted` on nothing at all: no ground, no edge, no corner, which is what makes the one current slot the only thing in the bar that stands out. The hover is a neutral wash, `--tint-hover`, which lightens on graphite and darkens on chalk by itself; the press is `--bg-pressed`, the one press ground in the system. Measured on this bar they are `rgba(255,255,255,.06)` and `#191b1f` over `#1c1f24` in the dark, and on chalk both darken, so the wash is the bigger step of the two. A tap fires hover and press at once and the press, written last at equal weight, is the one that shows.
- `a.nav-item.nav-slot @navitem-slots (2)` - **The current slot, and it splits off at REST, which is the point.** `--text-brass` and bold where the others are muted and regular, measured before any pointer arrives, so `states.cjs` reads it as its own face rather than as a state of the first. That is the correct reading: being where you are is a state of the ITEM and not an answer to a pointer. **The ink is the whole signal and the ground is the whole answer to the pointer**, deliberately: if pointing at a slot pulled its label toward brass, the one thing this bar says at a glance would be said by two different things, and a hover can stick after a tap on a phone, so the wrong slot would go on claiming to be current after the finger left. Its hover reaches it at all only because every hover in this file is written at the face's own two-class weight.
- `a.nav-item.nav-row.nav-row-stack @.app-header` - **The menu row and the notification row are one control with two contents, and this is both of them.** The account menu's line and a notification's title-and-detail rest transparent at 8/8 with `--text-primary`, answer the pointer with the header's 10 per cent brass wash and press to `--bg-pressed` - and those three were literally one selector each in `components/header.css` before the migration split them. What separates the two is `display`: a menu row is one line and takes the button default, a notification is a block because it holds a title over a detail. The 2px between rows is the product's density and the stand is not padded to flatter the camera, so 3px of the focus ring is shared with the row above.
