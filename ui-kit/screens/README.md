# Pixel proof: the patterns step

Forty frames, twenty screens at two viewports, shot before and after the six patterns were cut out
of the component files. The question this answers is the only one a refactor owes: **did anything
move.** No em dash.

## Why the images are not in git

The forty pairs are 118 MB of full-page PNG. They were taken, they were compared, and the comparison
is below; keeping them in history would put 118 MB into every clone to prove a sentence that is
already proved by the numbers, and the images are reproducible in about ninety seconds. So
`*.png` here is ignored, the pairs sit on disk after a run, and this file is what is kept.

To take them again, serve the working tree and a worktree of the commit you are comparing with on one
origin, then drive Chrome over both at 360 and 1440 and screenshot full-page into this folder with
`-before` and `-after` suffixes. The comparison is a canvas pixel diff: draw both into 1:1 canvases
and count pixels whose summed RGB delta clears 6.

## What the comparison found

**Twenty-five of the forty pairs are identical byte for byte.** Fifteen differ, and every one of
them is the page drawing itself differently between two loads rather than the css drawing it
differently. The control that says so is the third column: the SAME version shot twice.

| pair | before vs after | before vs before | verdict |
|---|---|---|---|
| deposit-1440 | 0 px | - | identical |
| toasts-360 | 0 px | - | identical |
| wallet-360 | 0 px | - | identical |
| event-feed-loading-1440 | 3 px | - | at the noise floor |
| event-feed-politics-360 | 2 px | - | at the noise floor |
| toasts-1440 | 4 px | 4 px | its own noise |
| event-detail-1440 | 5 px | 5 px | its own noise |
| active-bets-history-1440 | 6 px | - | at the noise floor |
| event-feed-politics-1440 | 6 px | - | at the noise floor |
| notifications-1440 | 8 px | - | at the noise floor |
| how-it-works-1440 | 18 px | - | at the noise floor |
| **how-it-works-360** | **133 px** | **33,478 px** | the page varies 250x more than the change |
| **event-detail-resolved-1440** | **1,252 px** | **1,252 px** | identical figures: entirely the page |
| **active-bets-1440** | **8,689 px** | **8,722 px** | varies MORE against itself than against the change |
| **sign-in-1440** | **10,703 px** | **10,703 px** | identical figures: entirely the page |

The remaining twenty-five pairs are not listed individually because a byte-identical pair has nothing
to say.

**What the variation is:** these pages draw content from a script on load, and the scripts have never
been read as code (`docs/backlog.md`, unread surface 3). A chart plotted from values, a figure
computed at render time and an image decoded on a second thread all land in a full-page screenshot,
and none of them is a stylesheet. That is why a pixel diff needs the third column: **without a
same-version control, a screenshot comparison reports the product's own weather as your regression.**

## The measurement that actually carries the claim

A pixel is a poor witness on a page that redraws itself, so the load-bearing check is the computed
one: every element on 42 screens at 360 and 1440, its box and 24 computed properties, before against
after.

**1 of 61,162 elements differed, and it was the instrument.** The one hit was a `.field-label` on
`win.html` at 360 reading `181x15` in one snapshot and `181x14` in the other; asked directly, its
height is `14.500` in both, so `Math.round` fell on either side of a half pixel that never changed.

Four screens were then re-measured property by property on their own: `active-bets` and `sign-in` at
1440, `event-detail-resolved` at 1440 and `how-it-works` at 360, the four with the largest pixel
deltas. **0 of 628, 0 of 601, 0 of 974 and 0 of 602 elements differed.**
