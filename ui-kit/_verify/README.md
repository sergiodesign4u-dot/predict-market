# Proving the screens did not move

A refactor of the styling layer is only honest if you can show the product renders the same
afterwards. A screenshot proves that as well as the eye reading it; these five scripts measure it.

They were written for step 5 of the Tokens + Components stage, where all 76 painted screens dropped
their inline `<style>` and their `_theme.css` link and moved onto `components/index.css`. They are
kept because step 6 (a dark theme over the same roles) and step 7 (the deletion pass) need the same
proof, and because a claim that nothing changed should be repeatable by anyone.

## What they do

| Script | What it answers |
|---|---|
| `snap.cjs` | For every screen at five widths: for every element, is it painted, where is its box, and what are its 55 computed properties. Writes one gzipped json per page per width. |
| `diff.cjs` | Compares two snapshot folders, element by element and property by property, and names what moved. |
| `causes.cjs` | The same comparison grouped by root cause instead of by page, so 20000 shifted boxes read as the six rules that shifted them. |
| `whys.cjs` | For a list of (page, selector, property), which css rule wins before the change and which wins after. This is what turns a difference into a fix. |
| `side.cjs` | One element, shot from the old markup and the new one, so a person can look at it. |

## Running them

The scripts drive the system Chrome through Playwright and read the screens over http, because a
`file://` page cannot load `../components/index.css` the way a served one does.

    python3 -m http.server 8901                 # from the repo root, in another shell

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
difference in the diff mean something. No em dash.
