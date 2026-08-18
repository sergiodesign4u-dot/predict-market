# Prediction Market Platform

A mobile-first Web3 platform for prediction markets. Users bet YES/NO on real-world events using stablecoins (USDC/USDT). Outcomes resolve against reality.

**Core bet:** better clarity and onboarding than existing competitors (Polymarket, Kalshi).
**Audience:** 20-40, trust-driven.
**Platform:** Mobile-first web, then responsive desktop.

---

## Live Research Summary

**[View research.html live](https://sergiodesign4u-dot.github.io/predict-market/research/research.html)**

Single-page summary of all research phases. Open the link above in any browser - no local server needed.

**CJM (live):** [As-Is](https://sergiodesign4u-dot.github.io/predict-market/user-research/cjm-as-is.html) - [To-Be](https://sergiodesign4u-dot.github.io/predict-market/user-research/cjm-to-be.html) (these paths go live once the branch is merged to main, which serves GitHub Pages). Takeaway: the deepest As-Is dip is the crypto wall (mass abandonment); To-Be flattens it by letting Alex browse and form the bet intent before any wallet, with the auth / crypto gate at Confirm.

---

## Repo Structure

Per-stage layout: raw markdown lives in each stage's `docs/`, and the stage's HTML page sits flat at the stage-folder root (for example `research/research.html`).

| Folder / File | What's inside |
|---|---|
| [`research/`](./research/) | **Foundation Research**: `docs/` (competitors, benchmark, lean-ux-canvas, aarrr, ux-patterns, and the `research.md` synthesis), `screens/` (competitor screenshots), and `research.html` |
| [`user-research/`](./user-research/) | **User Research + CJM**: personas + JTBD + the Customer Journey Maps (`docs/` incl. `cjm-as-is.md` / `cjm-to-be.md`; pages `personas.html`, `jtbd.html`, `cjm-as-is.html`, `cjm-to-be.html`) |
| [`ia/`](./ia/) | **Information Architecture**: `docs/sitemap.md` + `docs/flows.md` + `docs/pages/` (Detailed-layer sources `seo.md`, `system.md`); visualizations `ia.html` / `sitemap.html` / `flows.html` / `concept-map.html` (Basic) and `seo.html` / `system.html` (Detailed); `annotations/` (wireframe annotations, generated) |
| [`wireframes/`](./wireframes/) | **Grey-box wireframes**: every sitemap screen + all states + Favorites view + the 5 system pages, flow-linked, header / nav wired, clickable end to end. Owns structure and copy: a painted screen must not disagree with its grey twin. **How many documents stand here is counted in [`CLAUDE.md`](./CLAUDE.md), which owns it**, and this row said 105 while 109 stood on disk |
| [`voice/`](./voice/) | **Voice & Microcopy**: `docs/voice.md` + `docs/microcopy.md` + `voice.html` |
| [`concept/`](./concept/) | **Concept**: the **Vault** visual language - `docs/references.md` (Refero) + `docs/concept.md` (designer taste, 5 attribute pairs, locked decisions); `concept.html` (the stand: palette / type / form / contrast); superseded explorations archived in `old/` |
| [`ui-visual/`](./ui-visual/) | **UI + Visual**: the colour copies of the wireframes in the Vault language, plus `overview.html`, which is the index of the tree rather than a screen in it. **Two counts are therefore true of this folder, the documents and the screens one fewer, and every number written anywhere has to say which it is.** Both are in [`CLAUDE.md`](./CLAUDE.md), which owns them, and this row said 106 and 105 while 110 and 109 stood on disk. A screen carries no styles of its own: it links `components/index.css` and nothing else. The grey wireframes stay grey |
| [`components/`](./components/) | **The design system**: `tokens.css` (primitive + semantic + the light theme), `base.css`, one file per component, all reached through `index.css` |
| [`ui-kit/`](./ui-kit/) | **Rebuilt by hand, 2026-08-07 to 2026-08-08.** One page per component, one shelf per level, the foundation pages, `_page.css` and the one route `_nav.js`. **The enumeration that stood here has drifted four times now**: 55 in one place, 54 in another, `responsive.html` called the 57th page in a third, and last 57 pages with twelve atoms and five foundations while 60 stood on disk with fourteen and six. **A list written out by hand has to be re-typed on every change and a tally does not**, so the tally is in [`CLAUDE.md`](./CLAUDE.md) and the kit's own panel computes it from `_nav.js`, and this row now carries neither. **A level is a shelf and a component is a page**, and every component has a row in `_nav.js` whether or not it has a page yet. **0 generators and 0 gates.** The vitrine that stood here (65 generated pages, 54 Python scripts, 41 gates, 145 MB of screenshots) was deleted in one commit and the product did not move a pixel; its writing is kept in [`docs/kit-archive/`](./docs/kit-archive/). The **seven** reports are in [`ui-kit/docs/`](./ui-kit/docs/), the newest being [`consistency.md`](./ui-kit/docs/consistency.md) of 2026-08-15, the first that read the system against the product rather than the product against itself: **22 selector parts that draw nothing anywhere, of which 17 were deleted the same day and 4 of `print.css`'s were repaired instead because deleting them would have thrown away the intent; 379 of 379 tokens read and 52 of 53 contract lines exact; and nine places where the stand and the product disagree, six of them the stand drawing MORE than the product ships.** **Three of its seven findings were the instrument**, two of them struck: the four dead tokens are read by `_page.css`, whose job is to show them. **Every row of it was closed the same day and two of them were not what the report said.** The how-it-works sheet was not a stand problem at all: it was rebuilt on 2026-08-14 and its stylesheet was not, and one of the eight orphaned rules had been the sheet's SCROLL CONTAINER, so at 320x480 121px stood outside the clip with the step navigation unreachable and `scrollTop` reading back 0. **The chosen-NO face was the SCREENS**, and the grey tree proves it, because a paint that had lost a state would disagree with grey and both showed only YES: 127 chosen sides in the paint and every one YES, against a `?side=no` route with 212 anchors, so one screen in both trees is a NO bet now and the face measures 4.64:1 against the chosen YES's 6.42:1. **`.icon-btn-lift` should never have been on the list**: it is a face with no placements rather than a component with no face, decided on 2026-08-13, and the only thing wrong was a 525 the kit had not re-counted |
| [`docs/`](./docs/) | **The record**: [`decisions.md`](./docs/decisions.md) (what was done and why, dated, newest first) and [`backlog.md`](./docs/backlog.md) (what is still open) |
| [`components/patterns/`](./components/patterns/) | **Design System (09)**, built: the second shelf of the system package, **6 files** for compositions that stand on three screens or more (`card-grid`, `browse-shell`, `detail-shell`, `list-head`, `position-list`, `action-bar`). They carry arrangement only: **56 declarations over 19 properties in 28 rules**, re-counted 2026-08-18, and not one colour, face, border or surface among them. **One of the nineteen is `container-type`**, which is here rather than in a component because a place is not a property of a brick. The system itself stays in `components/` and did not move |
| Responsive (10) | **built, no folder**: the ladder is a registry in `components/tokens.css`, the record is `ui-kit/docs/responsive.md` and the stand is `ui-kit/responsive.html`, **the fifth foundation page of the kit** |
| Animation (11) | **built, no folder**: two durations and two curves in `components/tokens.css`, the transitions on the components that already carried a state, the record in `ui-kit/docs/motion.md` and the stand in `ui-kit/motion.html`, **the sixth foundation page of the kit** |
| Handoff (12) | no folder: the vitrine is the handoff |

The old→new folder map is recorded in [`STRUCTURE.md`](./STRUCTURE.md).

---

## Status

This table is the only place a stage status is recorded. `CLAUDE.md` holds rules and no statuses;
the dated record of how each stage got here is in [`docs/decisions.md`](./docs/decisions.md).

| Stage | Status |
|---|---|
| Foundation Research | ✅ Done (competitors, benchmark, Lean UX Canvas, AARRR, UX patterns, synthesis; screens captured) |
| User Research (Personas + JTBD) | ✅ Done |
| CJM (As-Is + To-Be) | ✅ Done (Alex x MJ; As-Is emotional curve + 5 growth zones, To-Be map + MVP backlog; 2 pages) |
| Information Architecture (Basic + Detailed) | ✅ Done - Basic (flows + concept-map by intent) + Detailed (overview + sitemap + SEO layer + system nodes); flows color-coded by outcome + traced to CJM, jobs x screens matrix, no orphans. Detailed layer (targeted reconcile, since the wireframes already render pages): A-E SEO for the 5 indexed pages + footer, and 404 / 500 / 503 / cookie / toast grounded in law |
| Wireframes | ✅ Done (all screens + states + Favorites + Event Detail tabs + 5 system pages, flow-linked, header / nav wired, critique pass). Stage-04 reconcile: system pages (404/500/503/cookie/toasts), footer trust strip + SEO links, story-led per-card "why" + SEO sections, Related events, Win F5 friction |
| Voice | ✅ Done (5 principles, lexicon, forbidden list, per-element rules; every screen rewritten line-by-line, closing audit clean) |
| Concept | ✅ Done - the **Vault** visual language: designer taste captured, 5 attribute pairs traced to data + borrowed technique, contrasting directions explored (Newsroom / Signal / Arena, archived to `concept/old/`), Vault chosen and locked; palette / type / form / photography / icons contrast-checked (WCAG AA) on the stand `concept.html` |
| UI + Visual | ✅ Done - every screen painted in Vault (76 at the close of the stage; step 8 added the 28 category states, and the tree grew again with every stage after this one, which is why the size of it is counted in [`CLAUDE.md`](./CLAUDE.md) and not here); every one links exactly `components/index.css`. `/impeccable critique` 31 -> 38 / 40 |
| Tokens + Components | ✅ Done - two token levels, three geometry scales, **49 components** (43 in `components/` plus 6 in `components/patterns/`) alongside **7** files that are the substrate a screen stands on rather than a part of one (`base`, `course-chrome`, `fonts`, `index`, `print`, `tokens`, `trust-art`), and a light theme as the proof of the semantic layer. **The level split is DECLARED and no longer computed**: **14 atoms, 16 molecules, 13 organisms and 6 patterns**, each with its reason, in [`ui-kit/docs/inventory.md`](./ui-kit/docs/inventory.md), which owns the split. Re-counted 2026-08-18 from the `@import` groups of `components/index.css` and from the pages of the kit, which agree; this row said 47 and 12 atoms, and both had been true. **This row said 40, and 10 / 14 / 13 / 6, and that all three of `account`, `cookie-consent` and `toc` were marked unmeasured**; re-counted 2026-08-12 against the filesystem and the inventory, **all six of the unmeasured were walked on 2026-08-08 and `account` was deleted the same day**, which the next row already said. The reading this row used to carry, 6 atoms and 13 molecules and 21 organisms computed from the markup, was the arithmetic's blind spot: a component built from its own class names reads as containing nothing. The vitrine and its 41 gates were deleted on 2026-08-07 and were rebuilt by hand from five anchor screens. Nine audit passes (7 to 9) are recorded in [`docs/decisions.md`](./docs/decisions.md); the surfaces they stopped short of are in [`docs/backlog.md`](./docs/backlog.md) |
| Design System | ✅ Done - the patterns shelf (**6 files**, arrangement only) and the vitrine rebuilt by hand: **61 of 61 pages** (54 at the close of the stage; `logo`, `platehead` and `responsive` landed on 2026-08-11), a shelf per level plus a page per component, one route in `_nav.js`, **0 generators and 0 gates**. **Every component in `components/` has a page**, every page was measured in a browser at 390 and 1280 before it was written, and **all six components the inventory called unmeasured were walked and given a level on 2026-08-08**. Eleven backlog rows were found by writing the pages. Five reports in [`ui-kit/docs/`](./ui-kit/docs/): census, inventory, consolidation, audit, responsive. **The list here named four of the five**, the same defect as the four-foundation list; the registry lists all five. The audit ran once over 115 documents at two widths in two themes, **460 renders**, and **found eight defects in itself and one in the product**, the eighth being that it had measured the whole product with a mouse. The 44px touch floor is one rule in `base.css` since 2026-08-08. **One row stays open under this stage**: 28, the footer's dead links, and it is blocked on IA's item 27. The last unblocked one, 51, closed on 2026-08-08 when the cookie row became a `<label>` and the target went from 18x18 to 233x44 under a finger |
| Responsive | ✅ Done - **three rungs in `rem`, named by what arrives at them** (40rem DESK, 47.5rem DETAIL, 56.25rem RAIL, which are 640, 760 and 900 at the default browser font and move with it: at a 24px default the desk arrives at 960) plus a harness at 1140 that is not the product's, kept as a **registry** in `components/tokens.css` because `@media` cannot read a variable and the limitation is therefore the instrument: **35 width queries in the system, 0 in any of the 110 documents in `ui-visual/`** (re-counted 2026-08-17 when the search field took the RAIL rung and the multi-outcome card took the DESK one: it was 33 before those passes and this line said 34, so the figure had drifted by one in the direction prose always drifts) (it was 33 until 2026-08-14 and 32 until 2026-08-15, and the count is re-taken from the comment-stripped source every time it is written down: 29 name one of the three rungs, 16 at the desk, 5 at the detail and 8 at the rail, 2 name the 1140 harness and 4 are one-offs carrying their reason beside themselves. **Re-counted 2026-08-18 the figure was 35 and this line said 37**, with the rail up two and the detail down one, which is the fourth time the total here has been wrong in the direction prose always drifts. One of the six at the detail is the course chrome's, which moved from `759.98px` to `47.49875rem` on 2026-08-14 because a boundary borrowed from another file has to be borrowed in that file's unit; **the two that arrived on 2026-08-15 are both at the desk's narrow side and both a control a desk sizes one way and a thumb another**, the chart's range group dropping its frame and the category chip dropping from 48 to 44 with the padding that was actually holding the box), and no number in a product query that is not on the list. The stage began with a **transcript** (twelve distinct widths already in the product, three of them on no ladder) and an **audit with one row per screen** (SAME 22, WIDER 82, **NEW BEHAVIOUR 0**, refused on `flows.md` rather than on taste). The shell fork is **A**, read off 03a and already built, and it was proved rather than designed: the bottom bar leaves the paint, the tab order and the accessibility tree at one pixel. **The type scale went to `rem` on 2026-08-12** (ten `--text-*` steps and eight `--display-*` clamps as ratios to the root, proved inert at the default with 0 differing font sizes of 44,547 readings, and a 24px-default reader goes from a 0.2 per cent longer page with no extra word to a 38.4 per cent longer one with every word), **and the RUNGS followed on 2026-08-13**, backlog 115 closed then 135 closed: 6,300 readings over 105 screens at twenty widths and three browser defaults give 0 horizontal scroll and exactly one navigation carrier everywhere, with 0 differing readings of 2,100 at the default. **The first instrument for it measured nothing**, because it set `html{font-size}` and a length in a media query resolves against the INITIAL font size and ignores every declaration on the root element. **`--measure:46ch` (it was `66ch` until the critique of 2026-08-12 found that `ch` is the advance of a zero and not a character), `--grid-col-min:300px`, `--rail-width:214px` and `--menu-min:196px` added; `--grid-gap`, a column-count token, a `--sticky-gap` and `rem` rungs all refused, each with its measurement.** Backlog **43 and 116 closed**, 115, 117 and 118 opened. The closing sweep is 320 to 1600 at 50 widths: **10,500 readings, 0 chasm widths, 5,250 carrier readings, 0 disagreements**, with a deliberate overflow seen 20 of 20 first, because 0 is also what a blind probe reports. The record is [`ui-kit/docs/responsive.md`](./ui-kit/docs/responsive.md) and the stand is [`ui-kit/responsive.html`](./ui-kit/responsive.html). **One finding of this stage was re-measured on 2026-08-12 and reversed**: the per-component width table was built from one placement each and three of its five FIXED verdicts were wrong, so it was retaken over every placement of all 47 components on the 105 screens at thirteen widths, with a control of 0 differing cells in 4,238. The counterpart reading is **10 of 47 filling everywhere, 26 of 47 with no query of their own, 8 of 47 both** rather than one number, and **the refusal of container queries no longer holds on the ground it was refused**: the threshold named was the first component standing in two columns of different widths, and **35 of 47 do**. The table, the method and the three components that carry the case (`card`, the `catnav` / `chip` rail pair, `navitem`) are in [`ui-kit/docs/inventory.md`](./ui-kit/docs/inventory.md), behaviour on width. **Backlog 129 answered it on 2026-08-13 and the threshold turned out to be the wrong test**: one component in two columns is necessary and not sufficient, because 35 of 45 components have no width behaviour at all, so the 52 selectors standing inside the 33 queries were classified instead (14 page frame, shell or harness, 2 a positioning context, 36 a component in a slot) and the 25 that stand on both sides of their own rung were tested for whether ANY container width divides the placements the way the rung does: **24 of 25 did**, so a container query would have resolved identically at every placement. **What the pass found instead was the opposite defect and it was one token**: `--gutter` and `--plate-inset` both STEPPED at 640, 38px a side spent at the pixel where the window gained one, so the content column went 611 to 560 and the feed card 577 to 502. Both ramp now from DESK to DETAIL, at a length that is derived and not chosen, and `card.css`'s query is gone because its rule was never about the window: **84 cards were cutting a pixel off a 44px target at every width from 640 to 1600.** Two queries left the registry and nothing replaced either. **And the refusal of container queries stopped being total on 2026-08-14, which this row went on saying it was**: `.ed-main` carries the system's first and only `container-type`, declared by `patterns/detail-shell.css` because the shell is what knows the column is a context, and `event-detail.css` asks it at 460px. It is the 25th of the 25 selectors the refusal measured and the one where **the window and the container move in opposite directions, twice**: `.ed-head` is 611 at a 640 window, 645 at 700 and **341 at 760**, because that is where the bet panel arrives and takes 322 of the row, and it happens again at 1140 when the review sidebar docks. A window query cannot say that the head is narrow here |
| Animation | ✅ Done - **two durations, not three, and the count is the finding**: `--dur-fast` .16s for a control answering a finger and `--dur-slow` .25s for an element arriving, with `--pulse-period` 1.4s beside them as a PERIOD rather than a rung, and two curves. The stage asks for three and the inventory of moments found two jobs with movement in them, the middle one having exactly one member which turned out to be a response. **The product already had five durations and not one was a literal**, so the work was never tidying loose numbers: measured by computed style over 163 documents in Chromium 151 and WebKit 26.5, 4,904 moving elements on the 105 screens, **the drift was in the CURVE**, with 12,821 of 13,406 easing slots on the bare keyword `ease` (and the closing audit corrected the stage's own published "0 bare keywords left" to **1**, a deliberate `linear` on a longhand that the stage's check never read), and **one ROLE wore four durations**, a hover at 160ms on a button, 180 on a photo tile, 250 on a trust plate and 300 on a card. 69 declarations were read, given one of three jobs and rewritten; five token names lived one step as aliases and were deleted after the last reader moved. **Six components had a state and no movement**, `navitem` at 1,068 placements and `position` at 996 among them, and **the status job was performed nowhere**: 482 skeleton marks on 19 loading screens, every one a flat box, now `sk-pulse`. Two expensive properties converted (`left` off the toggle knob, `width` off the step dot), one refused with its reason (`max-height` on the condensed band, because no transform removes a box from the flow) and five `box-shadow` kept because all five sit on the element's own hover, so at most one element paints a shadow at a time. **The reduced-motion check could not fail and now can**: `base.css` carried a blanket net on `*`, under which a component reading no token is indistinguishable from one reading every token, and it reported 115,028 moving elements against 6,555 with 0 defects; taken off, with a positive control at 999ms proving the probe sees a rule that disobeys, the same 163 documents gave **1,392 offending elements, 0 of them in the system and every one in the stand**, and 0 after both were repaired at source. The net is deleted rather than restored. **Motion was the SEVENTH boundary difference between the trees and nobody had declared it**, and the grey tree answers the setting on 0 of its 105 documents because it links no stylesheet at all. Three rulings taken out loud: no cross-document view transition (measured first: it fires in both engines over http and **not in WebKit from disk**), no motion at a rung, and the scroll edge fade held apart as an affordance because the reader's own hand drives it. The record is [`ui-kit/docs/motion.md`](./ui-kit/docs/motion.md) and the stand is [`ui-kit/motion.html`](./ui-kit/motion.html), the **sixth foundation and the 58th page of the kit**, where every specimen has to be operated because a screenshot shows a frame and never a movement |
| Handoff | ⬜ Not started |

---

## Wireframes

Grey-box (low-fidelity) wireframes for the whole product, mobile-first and
responsive. Neutral greys only - no color, type, shadows, or finished UI (those
belong to the Concept phase). Open any file in [`wireframes/`](./wireframes/) in a
browser; a left screen-tree panel navigates the whole set.

**[View the main screen live](https://sergiodesign4u-dot.github.io/predict-market/wireframes/event-feed.html)** - opens the rendered Event Feed in any browser, no local server needed.

**Start here:** [`wireframes/event-feed.html`](./wireframes/event-feed.html) - the
main-flow entry (the Event Feed). From there the journey is clickable end to end:
Event Feed -> Event Detail -> sign-in / deposit gate -> Active Bets.

- **Coverage:** 109 pages - every screen in the IA screen tree, each state its own
  page. Event Feed, Event Detail (binary + multi, inline bet panel), 4 Category
  pages, Favorites view (Favorites), Sign In / Deposit (shared in-page dialogs), Win /
  Loss, Notifications, Wallet, My Profile / Public Profile, How It Works, Active
  Bets / Bet History.
- **Auth axis:** browse screens have logged-in and logged-out variants.
- **Flow-linked:** the main flow is clickable end to end (Event Feed -> Event
  Detail -> gate -> Active Bets), with branch exits and no dead-ends, wired and
  audited edge-by-edge against the routes in [`ia/docs/flows.md`](./ia/docs/flows.md)
  (loading -> success, error -> try again, empty -> filled; branches both ways).
- **Chrome wired:** header (Favorites / Notifications / avatar dropdown) and the
  mobile bottom nav are real links, not dead buttons; logged-out controls open the
  sign-in dialog.
- **Interface copy** rewritten line-by-line against the product voice
  ([`voice/docs/voice.md`](./voice/docs/voice.md)); the rewrite log and the read-only text
  inventory it was edited from live in [`voice/docs/microcopy.md`](./voice/docs/microcopy.md).
- **Quality gates:** 0 em-dash, 0 broken links, 0 style leaks; the defect passes
  are recorded in [`wireframes/_critique.md`](./wireframes/_critique.md) - two full
  critiques (the second a 2026-06-29 multi-agent re-audit), a flow-wiring audit
  against `ia/docs/flows.md`, a 99/99 coverage audit against `ia/docs/sitemap.md`, and a final
  six-category defect pass, all clean. The build contract is
  [`wireframes/_conventions.md`](./wireframes/_conventions.md).

---

## Voice

The product voice is **rules, not a mood** - every rule carries an example, an
anti-example, and the research line it comes from, so every UI line reads the same
whoever writes it.

- **[`voice/docs/voice.md`](./voice/docs/voice.md)** - the contract: five **principles**
  (explain the number, trust before the ask, speak to a spectator not a trader,
  design the loss / mark the win without a fuse, say the specific provable thing),
  a **lexicon** (event not market, bet not position, Add funds, Save, Sign in,
  Browse events, Confirm bet), a **forbidden** list (no "Something went wrong",
  greetings, celebrations, "successfully", exclamations, emoji, apologies, internal
  codes), and per-element **microcopy** rules.
- **[`voice/docs/microcopy.md`](./voice/docs/microcopy.md)** - the read-only text inventory
  (with same-thing / same-action / cliche flags) and the line-by-line rewrite log.
  Every screen was rewritten against the voice and the closing audit is clean.
  The Event Detail social panel was moved from trader vocabulary
  (Top Holders / Positions / shares) to spectator language (Biggest bets / Bets).
- **State tone:** errors say what happened and what to do (no joke, no apology),
  empty states give a way out, and results state the fact without celebrating
  (Win = "You were right", no confetti; Loss = "Here's what happened", no "bet
  again").

---

## Key Docs

Four files at the root, and each answers one question. **`CLAUDE.md` = the rules** that must act next
time (it is loaded into every session, so it stays short). **`PRODUCT.md` = what the product is.**
**`docs/decisions.md` = what was done and why**, dated, newest first. **`docs/backlog.md` = what is
still open.** A status lives in the table above, and it is RENDERED from two registries that are turned by hand with it: `assets/_roadmap.js` for the 28 course documents and `ui-kit/_nav.js` for the 60 stand pages. This line said "and nowhere else" until 2026-08-18, while `_roadmap.js` had been printing SOON on Animation since the day it shipped.

- [CLAUDE.md](./CLAUDE.md) - **the rules**: how work is done here, what owns what, and the reason each rule exists now that no gate holds it
- [PRODUCT.md](./PRODUCT.md) - **the product**: JTBD, audience, market types, MVP scope, business model, compliance
- [docs/decisions.md](./docs/decisions.md) - **the record**: every stage and audit pass, with its date and its reasoning
- [docs/backlog.md](./docs/backlog.md) - **what is open**: 13 items, with the stage that owns each
- [STRUCTURE.md](./STRUCTURE.md) - the 12-stage layout and the old→new folder map
- [DESIGN.md](./DESIGN.md) - the shipped visual system (Vault): palette, type, form, tokens, contrast tables
- [wireframes/_conventions.md](./wireframes/_conventions.md) - **Wireframe contract**: grey-box rules, zones, nav, states, the build passes
- [wireframes/_critique.md](./wireframes/_critique.md) - **Wireframe critique**: defect tables and resolutions (Krok 9, 2026-06-29 re-audit, flow-wiring / coverage / final passes)
- [voice/docs/voice.md](./voice/docs/voice.md) - **Product voice**: five principles, lexicon, forbidden list, per-element rules
- [voice/docs/microcopy.md](./voice/docs/microcopy.md) - **Microcopy**: read-only text inventory + the line-by-line rewrite log
- [ia/docs/sitemap.md](./ia/docs/sitemap.md) - **IA source**: entities, screens, navigation, depth map, coverage matrix
- [ia/docs/flows.md](./ia/docs/flows.md) - **IA source**: four user flows (MJ, FJ2, FJ5+EJ3, SJ1)
- [research/docs/research.md](./research/docs/research.md) - **Research synthesis**: all research phases in one document (single source of truth)
- [research/docs/lean-ux-canvas.md](./research/docs/lean-ux-canvas.md) - **Lean UX Canvas v2**: the one-page strategy (problem, audience, hypotheses, riskiest assumption, first test)
- [user-research/docs/personas.md](./user-research/docs/personas.md) - **Personas**: Alex (primary), Dan, Maria, Loss-Prone overlay - with confidence levels and post-research updates
- [user-research/docs/jtbd.md](./user-research/docs/jtbd.md) - **JTBD**: full job hierarchy (MJ -> FJ/EJ/SJ/HJ), importance matrix, MVP conclusions
- [research/docs/aarrr.md](./research/docs/aarrr.md) - AARRR framework: acquisition, activation, retention, revenue, referral
- [research/docs/competitors.md](./research/docs/competitors.md) - Full competitor comparison: HARD / SOFT / ASPIRATIONAL groups, matrix, patterns, differences, open questions
- [research/docs/benchmark.md](./research/docs/benchmark.md) - Trust benchmark: 5 products x 8 criteria, top mechanisms for MVP
- [research/docs/ux-patterns.md](./research/docs/ux-patterns.md) - UX patterns: 5 approaches, behavioral analysis, pattern selection for MVP
