# Consolidation - the one pass where a value was allowed to change

Step 3e of the rebuild, 2026-08-08. The four foundation pages found what was wrong; this is what was
done about it, what it cost, and what was deliberately left alone. **Read once, written down, done.**
Nothing runs any of this on a schedule and no check reads this file.

The reports it acts on: [`census.md`](./census.md), [`inventory.md`](./inventory.md),
[`../icons.html`](../icons.html), [`../colour.html`](../colour.html),
[`../typography.html`](../typography.html), [`../geometry.html`](../geometry.html).

---

## The instrument, and the first one was useless

**A before-and-after needs an instrument that returns the same answer twice.** The first one did not.
It hashed every element's box and computed style over 68 renders, 17 screens at 390 and 1280 in both
themes, 39,104 elements. Run twice with **no change at all between the runs**, it reported
**45 of 68 renders different.**

The pages carry scripts that write at run time: the card odds bar is built as a string, the chart
draws from generated data, a theme is applied after load. A whole-page snapshot measures those as
well as the cascade, so it cannot answer "did this edit change anything". It was thrown away.

**What replaced it, for the reorder, is a proof rather than a comparison.** A change to `@import`
order can only move a rendered value where two files declare **the same property at the same
specificity** for selectors that both match **the same element**. Everything else is decided by
specificity, which order does not touch. So:

| | |
|---|---|
| pairs of files whose relative order flipped | **59** |
| same property, same specificity, across a flipped pair | **2,131 candidates** |
| distinct selector pairs among them | 1,358 |
| elements in the product matched by **both** halves of any pair, over 26 screens | **0** |

The reorder is inert by construction, and that is stronger than any number of identical renders.

For the value changes, the instrument is narrower and deterministic: the specific axis, on rendered
elements only, over 104 renders (26 screens at 390 and 1280 in both themes, 37,688 rendered
elements).

---

## What changed

### 1. The import order, nine files

`components/index.css` grouped its imports by level and eight of them disagreed with the level
`inventory.md` declares. `toast`, `navitem` and `yesno` were filed as molecules and hold nothing, so
they are atoms. `trustbar` and `market` were filed as atoms and hold their own named parts, so they
are molecules. `bottomnav`, `position`, `notice`, `options` and `state-block` were filed as organisms
and hold atoms, so they are molecules.

**Nine files moved. 59 pairs changed relative order. 0 elements affected**, by the proof above.

### 2. 148 borders now read `--hairline`

`--hairline:1px` was declared, used **ten times**, and `1px` was typed **148 times**, always inside a
`border` shorthand. `border:1px solid var(--border-hairline)` tokenises the colour and leaves the
width a number, and nobody notices **because the colour looks done**.

Substitution only, `1px` to `var(--hairline)` inside a border or border-width declaration. The token
is 1px, so the render is identical by definition. **0 raw border widths left in `components/`.**

### 3. Ten ladder-step literals

`8px`, `12px`, `16px` typed where `--space-*` or `--size-*` already had the number: the scrollbar
box, three absolute offsets, the roadmap toggle. Now tokens. **0 ladder-step literals left.**

### 4. `--weight-regular:400`

400 is the root default and the weight **192 of 260** text elements on the feed render at, and it was
the one step of the ramp with no name. `betpanel.css` had already needed it and written
`font-weight:normal`, the single weight literal in the system. Both fixed. **0 weight literals left.**

### 5. Tracking: 13 values and no tokens, to 8 tokens

The last axis in the type system without one. 61 declarations, 13 distinct values, including two
spellings of nothing.

The **tighten** half was already a scale and only needed names: `-.03em` for display at 24px and up,
`-.02em` for 13 to 20px, `-.01em` for a question set as a heading. Three tokens, no value moved.

The **open** half was seven values doing one job at 10 to 13px. It collapses to three:
`--track-caps-lg:.01em` for uppercase at display size, `--track-label:.03em` for the 10 to 11px
micro-label (12 declarations, the base), `--track-caps:.06em` for a 12 to 13px small-caps heading,
and `--track-caps-loud:.1em` kept for the divider.

| | |
|---|---|
| declarations tokenised | 61 |
| declarations whose **value moved** | **14** |
| largest single move | **.02em** (`.08em` and `.04em` to `.06em`) |
| text clipped or wrapped that was not before, over 40 renders | **0** |
| horizontal page scroll introduced | **0** |

**A gentler collapse was chosen on purpose.** Two open tokens instead of four would have moved values
by up to `.06em`, and at 10px over a twelve character label that is enough to force a wrap. Which
label should be louder than which is a design decision and not a sweep's to take.

### 6. Fonts: 18 files and 373 KB, to 8 files and 131 KB

Checksums said DM Sans and Space Grotesk were fetched as **variable** fonts and then copied once per
declared weight, four and three times each, every copy byte for byte identical. One `@font-face` per
family over a weight **range** replaces them.

**Verified by ink, not by looking**: painted-pixel counts for one string at 48px, before and after.

| | 400 | 500 | 600 | 700 |
|---|---|---|---|---|
| Space Grotesk, before and after | 5188 | 5188 | 5627 | 6072 |
| DM Sans, before and after | 4333 | 4886 | 5554 | 6005 |
| IBM Plex Mono, before and after | 5380 | 5380 | 5993 | 5993 |

**All twelve identical.** 242 KB of duplication removed, 10 files deleted, nothing rendered
differently. IBM Plex Mono keeps its four files, because its 500 and 600 really are two fonts.

### 7. Thirty-seven dead references, in 20 files

Comments in `components/` cited **24 gate numbers** and **15 deleted scripts** as the authority for a
rule: "found by gate 24", "invisible to `ui-kit/_rescale.py`", "fails the build". Neither the gates
nor the scripts have existed since 2026-08-07.

**Every one now names what was found rather than what found it.** A rule whose reason is a gate
number is a rule with a dangling reason, and the next reader either believes in a check that is gone
or throws the rule out with the citation. **0 left.**

---

## What was deliberately not changed, and why

**The two theme roles named as candidates by `colour.html` are not holes.** Reading where each is
used settles both: `--control-knob` is the dot in the switch and the switch's ON ground is
`--color-action`, which does not theme, so white is right in both; `--line-brass-strong` is
`--brass-a60`, and an alpha over a theming ground is theme-aware by construction. **Forty roles are
declared once and all forty are correct.** The page is corrected rather than the file.

**The icon set is not a value pass.** Two families with four jobs drawn in both, a stroke that renders
0.90px to 2.67px, four safe fields where there should be one: every one of those is a redrawing or a
product decision about which family wins, and a consolidation that redrew 52 glyphs would be a
different stage wearing this one's name. Backlog 29, 30, 31.

**Control height is not a sweep either.** Three tokens are declared and twelve render; 192 of 317
boxed controls get their height from padding plus font size plus a border. The fix is that a control
reads a height token and computes its padding from it, which is a change to how every control is
written, not to a value. Backlog 40.

**The brass ink ladder collapsing to one value in daylight** is a design decision, not a rounding:
either the ladder is real in both themes or it is one role with three aliases, and both are
defensible. Backlog 33.

**The 81 layout dimensions stay literals.** A 120px panel column and a 560px sheet are not rhythm
steps, and forcing them onto a 4px ladder would be the ladder pretending to decide something it
cannot see. That question belongs to Responsive.

---

## What the verification found on its way past

**`.chip-amount` inside a `<dialog>` is outside `.app-case`, and there are 28 of them.**
`chip.css` writes `.app-case .chip-amount`, so a chip that is not inside that class gets no rule at
all: the User Agent's `2px outset` border, a `rgb(239,239,239)` ground and square corners, in a dark
product.

**All 28 are inside closed dialogs and none renders today.** The 12 that do render are all inside
`.app-case` and all correct. So it is latent, and it is the third time this pass that the same shape
has appeared: the unscoped `.amount-input` rendering as a white User Agent field, a chip that is not
a chip outside `.app-case`, and now this. **`.app-case` is a dependency the system requires and never
declares.** Backlog 42.

---

## The state of the axes after the pass

| Axis | Before | After |
|---|---|---|
| import order vs declared levels | 8 disagreements | 0 |
| border width literals | 148 | 0 |
| ladder-step literals | 10 | 0 |
| weight literals | 1 | 0 |
| tracking tokens | 0, on 13 values | 8, on 61 declarations |
| font files / bytes | 18 / 373 KB | 8 / 131 KB |
| dead gate and script references | 37 in 20 files | 0 |
| horizontal page scroll, 104 renders | 0 | 0 |
| border widths on rendered edges | 1px, 2px, 1.5px | unchanged, and the two exceptions are underlines |
