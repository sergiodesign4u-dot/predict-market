# Asking the browser

Two classes of defect in this product exist ONLY in the browser, and no scan of the source finds
either: a value a css function hides (`color-mix(in oklab, ...)` comes back from
`getComputedStyle()` verbatim) and a value that is nowhere in the repository at all (an `<a>` with
no rule behind it is still painted, by the User Agent, at 1.76:1 on graphite). So the question is
asked of a browser, and this folder is where that is done.

## One reader, and why it exists

**`browser.cjs` is the only file here that opens a browser.** Everything else asks it.

That is a correction, made in step 6 of the Design System stage. Before it, every check that needed
a browser was written for one step and thrown away: the contrast sweep of step 1, the focus sweep of
step 2, the pixel proof of step 3, the pattern render of step 4, the guide render of step 5. Six
instrument bugs were therefore found six times and fixed in six places, and two of them were the
SAME bug found twice, because the file that had learned the lesson no longer existed by the time the
next check was written. This is the move `_levels.py` made for containment: one computation, many
consumers.

Fourteen things it knows out of the box, each with the case that taught it written beside it in the
file: the colour is parsed by a canvas and never a regex; alpha is composited up the ancestor stack;
inert subtrees are skipped and focus is a real Tab; both batches of a comparison run in the same
regime, fresh context with the cache off; a measurement waits for the theme transition the document
itself declares; a colour painted through a blend or a filter cannot be read from `color`; a console
error is attributed by URL rather than by its text; a gradient is not a `background-color`; a pinned
box taller than the window hides its own tail; text with transparent ink or a 0px face paints no
glyph, so it has no contrast to measure; a hover is a real pointer and reaches only what is in the
window; the code that implements lesson 5 was measuring nothing at all; a broken instrument that
reports all clear is caught by nobody; and a photograph of a cropped subject looks exactly like a
photograph. **None of the fourteen is
defensive coding.** Each is a wrong answer this project has already published, so anyone who reads
one as excessive caution should read the line above it first.

Nine is the one worth reading twice: every other question in this folder is about a PIXEL, so a page
whose contents rail was pinned 81px below the bottom of a 640px window passed all of them, twice. A
check that asks whether a person can reach the pixel is a different question from any of the colour
ones, and it needs its own window: it is measured at `SHORTEST_VIEWPORT`, because a capped dialog and
a stranded rail are indistinguishable in a tall one.

**Twelve is the one worth acting on.** `settleMs()` is the whole of lesson 5 - it returns the longest
transition the document declares, and everything that measures after a state change waits on it - and
it returned **0** from the day it was written, for three reasons stacked on each other. It read the
declaration TEXT, and every transition in this system is written `var(--dur-quick)`, so no number was
ever there to match. Two of its three regexes reached the browser with their backslashes eaten,
because the probe is a template literal and `\d` in one is an escape node swallows: the pattern
arrived as `/^[d.]+m?s$/`. And its walk recursed on `rule.cssRules`, which only `@media` and
`@supports` used to have - Chrome ships CSS Nesting now, every style rule carries an empty list, an
empty list is truthy, and **1263 of 1285 rules were skipped before their declarations were read**. It
now returns 300. Nothing already published was wrong because of it, since the values that were read
had arrived; what was missing was the guarantee, which is the whole point of an instrument. A checker
with a broken instrument reports clean.

**Thirteen is the rule the other twelve are instances of, and it is about which way a broken
instrument fails.** Every one of the twelve above was caught the same way: it reported something
wrong, somebody went to look, and the instrument was the thing that turned out to be lying. The
`color-mix` regex reported a 2.72:1 ring that did not exist. `settleMs()` returning 0 was found while
chasing a hover that would not settle. Lesson 8's gradient reported 1.18:1 on a button that measures
about 5.5:1.

**A broken instrument that reports a DEFECT gets caught, because somebody goes to look and finds the
instrument lying. A broken instrument that reports ALL CLEAR is caught by nobody, because there is
nothing to go and look at.** The most dangerous output of a broken check is not a false alarm, it is
a clean bill of health, and this repo has paid for that once at full price: fifteen printings of
"0 below AA" across three documents, over corpora up to 86,534 text pairs, while 378 elements stood
below 4.5:1 the whole time. The correction is at the end of `ui-kit/docs/history.md`; the finding is
row 42 of `ui-kit/docs/defects.md`.

What follows from it, operationally: **a check that has never failed has not proved anything, it has
only never been audited.** So every declared list in this repo carries the control that an entry
covering nothing fails as loudly as an undeclared item (gates 24, 25, 30, 31 and 32), and every gate
added since is proved in both directions before it is believed - green on the real tree, red on a
deliberate break. A gate that has only ever been seen green is in exactly the position the zero was.

Eleven arrived the same afternoon and is the reason twelve was found. `snap.cjs` measures the REST
state, so a pass whose entire intended change lives inside `:hover` cannot be verified by the diff
that proves nothing else moved. There is no class to set: `:hover` is the browser's answer to a real
mouse, so `paint()` marks every visible match and `hoverAt()` scrolls it into view and puts the
pointer on it. The scroll is not a nicety - the first cut moved the mouse to the box centre `paint()`
reported, which is viewport-relative, so every control below the fold reported its rest state as its
hover, and that looks exactly like a missing rule.

**Fourteen is thirteen arriving in pixels, and it is the reason gate 31 grew a third question.**
`boxAt()` pads each side of a state picture to at most HALF the distance to the nearest neighbour,
which is correct and is what keeps a control's picture from showing the one below it. It then let
that halving win against the SUBJECT's own paint. `ui-kit/_specimen.css` set `.kit-row{gap:14px}`, so
every facing side was capped at **7px** whatever the caller asked for, and the specimen page had no
padding at all, so a control beginning at x=0 kept nothing on that side. **36 of 790 state pictures
were short, and every one of them was a FOCUS picture** - the single state whose entire subject is a
ring drawn OUTSIDE the box, `--ring` 2px at 2px offset, 4px on every side.

The crop was in the png. No change to the page that displays the picture could put back a pixel that
was never captured, and nothing on that page could report it either, because a confidently rendered
photograph of a cropped thing looks exactly like a photograph.

So the pad is now DERIVED, from the element being photographed, in the state it is in: `extentAt()`
reads the computed outline and every non-inset shadow and returns the four sides, blur/2 + spread +
offset being where the paint actually stops. Over all 790 pictures **the widest answer in the whole
tree is 4px** and no shadow on any photographed element reaches outside it, which is a fact worth
having written down rather than assumed. That number is a FLOOR the neighbour rule may not go under;
the row gap is twice the 12px `shoot()` asks for, so the halving no longer caps anything; and what
the frame actually managed is written into the manifest next to what it needed, so
`python3 ui-kit/_states.py --crop` and gate 31 can fail on a crop **without a browser**.

## What they do

| Script | Opens a browser through | What it answers |
|---|---|---|
| `browser.cjs` | it IS the reader | How to ask: the colour of a thing, the ground behind it, the ring at a tab stop, what is inert, how long a theme takes to settle. Measures no product decision of its own. |
| `audit.cjs` | `browser.cjs` | The questions on any set of pages: contrast against the real ground, links with no rule behind them, horizontal overflow, dead icon references, failed requests, a pinned box taller than the window it is pinned to, and optionally the ring at every tab stop. Exits 1 on any finding. |
| `snap.cjs` | `browser.cjs` | For every screen at five widths: for every element, is it painted, where is its box, and what are its 55 computed properties. Writes one gzipped json per page per width. Every animation is FINISHED and every scroller zeroed first, because neither is a stylesheet property and both were putting a floor of 1,745 changed boxes under the diff. |
| `diff.cjs` | no browser | Compares two snapshot folders, element by element and property by property, and names what moved. |
| `causes.cjs` | no browser | The same comparison grouped by root cause instead of by page, so 20000 shifted boxes read as the six rules that shifted them. |
| `whys.cjs` | `browser.cjs` | For a list of (page, selector, property), which css rule wins before the change and which wins after. This is what turns a difference into a fix. |
| `side.cjs` | `browser.cjs` | One element, shot from the old markup and the new one, so a person can look at it. |

## Running them

The scripts drive the system Chrome through Playwright and read the screens over http, because a
`file://` page cannot load `../components/index.css` the way a served one does.

    python3 -m http.server 8901                 # from the repo root, in another shell

    node ui-kit/_verify/audit.cjs --kit          # every vitrine page, both themes, 360 and 1440
    node ui-kit/_verify/audit.cjs --screens --focus
    node ui-kit/_verify/audit.cjs ui-kit/why.html

    node ui-kit/_verify/snap.cjs /tmp/before    # with the old state checked out
    node ui-kit/_verify/snap.cjs /tmp/after     # with the new state
    node ui-kit/_verify/diff.cjs /tmp/before /tmp/after
    node ui-kit/_verify/causes.cjs /tmp/before /tmp/after

`git stash push -- ui-visual components` is the usual way to get the two states without editing
anything twice.

`PLAYWRIGHT_MODULE` overrides where the playwright module is found (the default is the npx cache on
this machine). The five widths are one per band the system has a breakpoint for (640, 860, 900,
1440), so a rule that escaped its media query cannot hide between two of them.

## What they deliberately do not compare

- Elements invisible in both states. The grey-box scaffolding (`.wf-nav`, `.zone-tag`, `.page-label`)
  is `display:none` under both cascades, so its colours may differ freely.
- A colour on an element with no text of its own, and a border colour under a 0px border. Neither
  paints anything; both changed on hundreds of wrappers and all of it was noise.
- Head elements. The inline `<style>` is what step 5 removes, and its disappearance would shift every
  index after it and make each page read as entirely different.

Two runs of `snap.cjs` over the same state produce byte-identical output, which is what makes a
difference in the diff mean something.

## Three scripts that do not open a browser, on purpose

`diff.cjs`, `causes.cjs` and `visible.cjs` compare snapshot FILES. They are outside `browser.cjs`
because they ask nothing of a page: handing them a browser session would give them a capability
they have no use for and a reason to drift. The line is about what a script needs, not about where
it sits. No em dash.
