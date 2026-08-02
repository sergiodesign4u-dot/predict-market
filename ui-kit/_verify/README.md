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

Six things it knows out of the box, each with the case that taught it written beside it in the file:
the colour is parsed by a canvas and never a regex; alpha is composited up the ancestor stack; inert
subtrees are skipped and focus is a real Tab; both batches of a comparison run in the same regime,
fresh context with the cache off; a measurement waits for the theme transition the document itself
declares; and a console error is attributed by URL rather than by its text. **None of the six is
defensive coding.** Each is a wrong answer this project has already published, so anyone who reads
one as excessive caution should read the line above it first.

## What they do

| Script | Opens a browser through | What it answers |
|---|---|---|
| `browser.cjs` | it IS the reader | How to ask: the colour of a thing, the ground behind it, the ring at a tab stop, what is inert, how long a theme takes to settle. Measures no product decision of its own. |
| `audit.cjs` | `browser.cjs` | The four questions on any set of pages: contrast against the real ground, links with no rule behind them, horizontal overflow, dead icon references, failed requests, and optionally the ring at every tab stop. Exits 1 on any finding. |
| `snap.cjs` | `browser.cjs` | For every screen at five widths: for every element, is it painted, where is its box, and what are its 55 computed properties. Writes one gzipped json per page per width. |
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
