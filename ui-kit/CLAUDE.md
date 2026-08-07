# ui-kit/ - the vitrine, being rebuilt from 2026-08-07

The kit shows the system to a person and it holds no product code. Right now it holds six pages plus
its stylesheet: `overview.html`, which says what is happening, `vitrine.html`, the ten atoms in every
face they wear with both themes side by side, **all four foundation pages** (`icons.html`,
`colour.html`, `typography.html`, `geometry.html`), and `_page.css`, the stand furniture they all
share.

**A swatch never carries a value.** `_page.css` holds one class per role and per primitive,
`.c-bg-plate{--sw:var(--bg-plate)}`, and the page wears the class. That is why there is not a single
`style=` attribute on `colour.html`: a colour written inline is a value this stylesheet cannot see,
and a colour page whose colours are invisible to the system is the exact thing being audited.

**The foundations are `colour`, `typography`, `geometry` and `icons`, one flat page each**, and they
are the visible half of step 3. A value may only change in that step, and it changes in the page and
in `components/` together.

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
3. **Consolidation, and it carries the foundations.** One pass where a value may change, in four
   pages plus the value work. **3a icons is DONE, 2026-08-07, `icons.html`**: 52 glyphs audited
   against the paint, and the axis had never been measured at all because the census counts controls
   and an icon is not a control. What it found: **two families**, 33 hand-drawn stroked and 15
   bought filled, with **four jobs drawn in both**; the stroke declared once at 1.6 in user units so
   it renders **0.90px to 2.67px** across six sizes, which is no optical weight at all; **four
   different safe fields** in the stroked family, 2.2 to 5.2, against the filled family's 2.0 on 13
   of 15; **seven jobs, eight to fourteen drawings**; three glyphs whose centre is 1.7 to 2.0
   modules out. **3b colour is DONE, 2026-08-07, `colour.html`**: 212 primitives, 133 roles, and
   **134 contrast readings against the composited ground with 0 below floor**, at two floors,
   4.5:1 for a word and 3:1 for a glyph. What it found: `icon-brass` in daylight is **3.20:1**, two
   hundredths of headroom and the only role in the system with nowhere to go; **the brass ink ladder
   has four rungs in the Vault and one in daylight**, so three roles do nothing there; `icon-quiet`
   is identical to `text-muted` in the Vault and separate in daylight, which is the two-level system
   earning its cost; and **40 roles are declared once**, of which 37 correctly so and two,
   `control-knob` and `line-brass-strong`, stand on a ground that inverts. **3c typography is DONE,
   2026-08-07, `typography.html`**: three families, 18 faces, ten fixed sizes and eight fluid ones,
   three named weights, six leadings. What it found: **DM Sans and Space Grotesk are variable fonts
   copied once per weight**, so 242 KB of the 373 KB payload is the same bytes seven times;
   **`--weight-bold` is 700 and IBM Plex Mono has no 700 face**, a trap rather than a live defect
   because nothing asks for it yet; **400 is the weight 192 of 260 elements render at and it has no
   token**, so one component had to type `normal`; **tracking is 13 values, 59 declarations and zero
   tokens**, including two spellings of nothing; and the census's `19.2px` **is not a leak**, it is
   `clamp(19px,1.5vw,23px)` resolving at a 1280 viewport, with two more fluid values doing the same
   there. **3d geometry is DONE, 2026-08-07, `geometry.html`**: measured over 10 screens at 1280,
   2,905 padding readings, 1,454 gaps, 1,144 borders, 1,264 corners, and **2 readings in 4,359 off
   the 4px grid**. What it found: **`--hairline:1px` is used 10 times and `1px` is typed 145 times**,
   always inside a `border` shorthand; **three control heights are declared and twelve render**, with
   33, 34 and 35 inside two pixels of each other and 192 of 317 controls taking their height from
   arithmetic; `50%` is a sixth corner shape the ladder does not name, 28 readings; and the two
   ladders with identical values, `--space-*` and `--size-*`, are **correct**, because every step of
   both has a job written beside it. It also **half corrects the census**: the height finding stands,
   the padding one does not (a `padding` shorthand was counted as one value and it is four), border
   is one width and 16 colours, and radius has five declared steps in use rather than three. Still
   open: **3e the values** (import order,
   17 paddings, 29 heights, 17 borders, the `19.2px` leak, 20 files citing gates that no longer
   exist, and the four decisions `inventory.md` forced). Output: `docs/consolidation.md`.
4. **The pages.** One per component: a live specimen, its states in both themes, its classes, its
   rule and anti-rule, and the screens it stands on.
5. **One audit run**, as a report.

The five anchors: event feed, event detail, active bets, deposit, sign in, with their loading, empty,
error and logged-out variants. 41 screens of the 106.
