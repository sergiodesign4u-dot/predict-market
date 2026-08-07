# ui-kit/ - the vitrine, being rebuilt from 2026-08-07

The kit shows the system to a person and it holds no product code. Right now it holds three pages:
`overview.html`, which says what is happening, `vitrine.html`, the ten atoms in every face they wear
with both themes side by side, and `_page.css`, the stand furniture the three index pages use.

## What was here and why it is not

65 generated pages, 18 Python scripts, 9 browser scripts, 41 build gates in 109 checks, a
state-capture instrument and 145 MB of screenshots. Deleted in one commit. The reason, in one
sentence: **the measurement had become a machine, so a one-line change to a stylesheet cost a
regeneration, a re-capture, 41 gates, 525 snapshots and an audit.** The full account is in
`../docs/decisions.md`, dated 2026-08-07, and the writing that was worth keeping is in
`../docs/kit-archive/`.

## The rules for the rebuild

- **A page is written by hand.** No generator, ever. If two pages share furniture, that is a rule in
  `_page.css`, not a script that stamps both.
- **A measurement is an act, not a machine.** Walk the screens, write down what was found, decide,
  keep the report. The moment a measurement becomes a permanent check, every later edit pays for it
  again.
- **A stand page may never style a product class.** `_page.css` is `.tk-*` only and grows one rule at
  a time, as a page actually needs it. The previous one reached 854 lines of which 800 painted
  classes nothing rendered.
- **The kit reads the system and never a copy of it.** A page links `../components/index.css`. If a
  specimen needs markup, the markup is the same markup the screen ships.
- **A page carries states, in both themes, side by side.** That is the whole reason this vitrine
  exists rather than a Figma frame: a hover, a press and a focus ring are things a person raises with
  a pointer and a Tab. Each `.tk-theme-fig` carries its own `data-theme`, so both themes resolve in
  one document with no screenshots and no switching.

## The plan, in order

1. **Census.** Five anchor screens with their states, walked in a browser at 390 and 1280 in both
   themes, computed values rather than written rules. Output: `docs/census.md`.
2. **Levels.** Atom, molecule, organism declared once with a reason each. Output: `docs/inventory.md`.
2.5 **The vitrine, atoms.** DONE 2026-08-07, `vitrine.html`. Built BEFORE the consolidation on
   purpose: it is the picture of the system to compare the next pass against, and a change to a
   value that nobody can look at is a diff rather than a decision. It found two things the census
   and the inventory both missed, because both read markup and this one renders it: **the unscoped
   `.amount-input` takes its ground and its ink from the User Agent and shows as a white box in the
   dark theme**, and **the card odds bar exists in no screen's markup at all**, being written by a
   page script at run time, which is where its 213 uses came from.
3. **Consolidation.** One pass where a value may change: the radius scale, the hairline, the icon
   stroke, the size ramp. Every change measured before and after. Output: `docs/consolidation.md`.
4. **The pages.** One per component: a live specimen, its states in both themes, its classes, its
   rule and anti-rule, and the screens it stands on.
5. **One audit run**, as a report.

The five anchors: event feed, event detail, active bets, deposit, sign in, with their loading, empty,
error and logged-out variants. 41 screens of the 106.
