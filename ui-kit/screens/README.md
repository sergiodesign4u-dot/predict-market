# Pixel proof: the patterns step

Twenty screens at 360 and 1440, shot before and after the six patterns were cut out of the component
files and `.tc-page` moved out of `toast.css`. The question a refactor owes is the only one asked
here: **did anything move.** No em dash.

## Why the images are not in git

The forty pairs are 118 MB of full-page PNG. They were taken, they were compared, and the comparison
is below; keeping them would put 118 MB into every clone to prove a sentence this file already
carries, and they regenerate in about ninety seconds. So `*.png` here is ignored and this is what is
kept.

## The answer

**0 of 61,162 elements moved.** That is the load-bearing measurement: every element on 42 screens at
360 and 1440, its box and 24 computed properties, before against after, with the browser cache
disabled. Not one differed.

## Read a screenshot diff only with its control

A pixel diff on this product is close to useless on its own, and the run that produced this file
proved it twice. Both times the instrument, not the css.

**Trap one: two screenshot batches taken in different browser regimes.** The `-before` frames were
shot in a reused page with a warm cache; the `-after` frames in a fresh context with the cache
disabled. Nine screens at 1440 came back 7,500 to 11,200 pixels apart. Re-shooting `-before` in the
SAME regime collapsed every one of them:

| screen at 1440 | across regimes | same regime |
|---|---|---|
| deposit | 10,702 | **0** |
| notifications | 7,616 | **0** |
| wallet | 7,567 | **0** |
| win | 8,017 | **0** |
| event-detail-resolved | 8,722 | **0** |
| toasts | 11,168 | **4** |
| event-detail | 8,717 | **11** |
| 404 | 11,209 | **42** |
| my-profile | 8,116 | **83** |

**Trap two: the page draws itself differently between loads.** Some screens plot a chart or compute a
figure on load, so the same version differs from ITSELF. `how-it-works` at 360 measured 133 pixels
against the change and **33,478 against a second shot of the same file**, and `sign-in` at 1440
measured exactly the same figure both ways. The scripts behind that have never been read as code
(`docs/backlog.md`, unread surface 3).

So a screenshot comparison here needs two controls before it means anything: **the same version shot
twice, and both versions shot in the same regime.** Without them it reports the browser's weather as
your regression, and it did.

## The one thing a stale stylesheet nearly hid

Moving `.tc-page` from `toast.css` to `base.css` first measured as a defect: `margin-bottom` read
`16px` before and `0px` after, and the page grew 16 pixels shorter. The rule was in the file and the
server was serving it; the browser was holding an older `base.css` in a reused context, so the DOM
carried the old cascade while the file on disk carried the new one. In a fresh context with
`Network.setCacheDisabled` it reads `16px` and `1154px` on both sides, unchanged.

**That is the same failure in the other direction.** A stale sheet can invent a defect, and it can
equally hide one by making after look exactly like before. Every number on this page was taken with
the cache off.
