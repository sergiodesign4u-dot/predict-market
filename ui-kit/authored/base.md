# base

## Sources

- All 105 painted screens: `.device` and `.app-case` are on every one of them, and `.feed-inner` on 104.
- `DESIGN.md` L185, which names the graphite canvas as the device base, and the material section that specifies the two-stone slab and the plate it holds.
- `ui-kit/docs/backlog.md` S2, closed by the reading layout, where the answer turned out to belong to a container rather than to a text component.
- `ui-kit/_adoption.py`, whose declared list carries this file's two provenance classes and its one offer with no taker.
- `components/base.css` itself, which records what LEFT it: three components that had arrived with the flat kit and were living in the file named for the frame.

## Purpose

Not a component. The page frame: the reset, the body type, the slab the product sits on, the plate a screen stands on, and the handful of utilities every screen needs before a single component is loaded. If a rule here is wrong, nothing in the system is right, and that is the whole reason it is a file and not a folder.

Four things live here that could plausibly live elsewhere, and each is here because it belongs to the FRAME rather than to any component: the focus ring, declared once for the whole system; the reduced-motion block, for the same reason; the scrollbar, thin and quiet, so one rule reaches every scroller; and the two-stone plate, which is the surface a page stands on and was living in two component files because those were the two that first needed a page to stand on.

## Anatomy

- `.device` - the slab. The physical object the product is printed on: the graphite stone, the coarse grain, the vertical gradient.
- `.app-case` - the product itself, and it is TRANSPARENT on purpose, so the slab shows through. On the frozen kit the app-case is the body, which is why one rule gives a body that carries the class its own background.
- `.desk-only` - the visibility utility, and the one rule in this system marked important that has to stay so: the elements it hides carry their own display from their own component, and base.css loads first.
- `.tbd` - a grey-tree annotation chip, kept because `ui-kit/kit.html` is frozen and still carries the markup. Declared in gate 30 as provenance.
- `.placeholder-line` - the same family, the same reason.
- `.groove-sep` - the frame's groove separator, staged on this page and taken by no screen yet. The one declared line in gate 30 with a shelf life.
- `.tc-page` - the section of the toast catalogue that stands in for the page a toast would be covering. It arrived here from `toast.css`, where it had made the toast read as containing the cookie banner.

## When to use

Never by choice. Nothing is "built with base": a screen gets it by existing, because `components/index.css` imports it second, after the fonts and before everything else.

The question this page actually answers is the opposite one: when a rule you are about to write belongs HERE rather than on your component. It does when it holds for every screen regardless of what is on it. The focus ring is the clearest case: fourteen component files carried their own copy and twenty-four did not, and a person navigating by keyboard is not asking each component separately.

## Rule

If the rule would have to be repeated by the next component to arrive, it is a frame rule and it belongs in this file, declared once.

## Anti-rule

Never let a component's page-level wrapper live in the component's own file: a plate under a browse screen is `browse-shell`, a plate under a detail screen is `detail-shell`, and the material both stand on is here, because a component that owns a page plate reads as containing the entire page.

Seen: `ui-kit/_levels.py` SPECIMEN_DEBT, whose entries for `feed` and `event-detail` are exactly this defect, half-paid on 2026-08-03 when the plate came here and the arrangement went to `components/patterns/`.

## States

None of its own. The one state rule in this file is `:focus-visible`, and it is not this component's state: it is the system's, declared here once so that no component has to remember it. A browser sweep of 153 pages in both themes found 0 of 179 ring kinds missing after it moved.
