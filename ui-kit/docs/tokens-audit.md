# Tokens audit - the flat kit read against the painted product

Stage 09 (Tokens + Components), step 1. Facts first: where every value stands, which roles hide
behind it, and where a value is written past the variable. Nothing is renamed or fixed here.

**Sources read:** `ui-kit/kit.css` (2123 lines), `ui-kit/kit.html`, `ui-kit/shell.html`,
`ui-kit/docs/inventory.md`, and all 76 painted pages in `ui-visual/` with their state pages, plus
`ui-visual/_theme.css` and `ui-visual/_theme-vault.css`. Both files were deleted in step 7: step 5
moved every screen onto `components/index.css` and nothing had loaded them since. This document is
the record of what was read out of them, and it is kept as provenance, not as a live path.
**Not read, by rule:** `wireframes/` - the grey prototype runs on its own `_wf.css` and owns no
product token.

---

## 0. What the painted product actually loads

The lesson assumes every screen links `kit.css`. Ours does not. Each painted page carries its own
inline `<style>` (the grey-box skeleton grafted from the wireframe) and then one link to
`_theme.css`, which `@import`s `_theme-vault.css` and repaints on top by source order:

```
ui-visual/<screen>.html
  <style> ... 25000 to 42000 chars of structural grey-box CSS ... </style>   <- structure + grey colour
  <link rel="stylesheet" href="_theme.css">                                  <- @import _theme-vault.css (Vault tokens + skin)
                                                                             <- then the two-stone layer
```

There are only **7 distinct inline blocks** across the 76 pages, so the material is far smaller than
76 copies suggests:

| Block | Pages | Size | Representative |
|---|---|---|---|
| A | 41 | 35860 | `404.html` (the shared shell: header, footer, dialogs, state pages) |
| B | 15 | 25007 | `event-feed-crypto.html` (feed and category) |
| C | 9 | 41866 | `event-detail-bet-error.html` (feed shell + Event Detail) |
| D | 4 | 35962 | `active-bets-empty-new.html` (shell + position list) |
| E | 4 | 35866 | `event-detail-error.html` |
| F | 2 | 36773 | `my-profile.html` (shell + profile cluster) |
| G | 1 | 25202 | `favorites-empty.html` |

**`kit.css` is a true superset of that cascade.** Rule-level diff of every block against `kit.css`:
each block has only 5 or 6 rules that `kit.css` does not carry, and every one of them is deliberate:

- `* { box-sizing: border-box; }` (the builder drops the bare universal rule; `kit.css` re-declares it)
- the four `@media (min-width:1440px)` rules of the wireframe screen-tree rail (`.wf-nav`,
  `.wf-toggle`, `body{padding-left:250px}`, `.page-label`) - stripped on purpose, no kit markup uses them
- `.notif-empty` (blocks D and G only) - a genuine miss, see finding C4

So step 3 splits **one** file, not eight, and the split covers the whole product. The theme files add
nothing that `kit.css` lacks either (8 and 19 non-identical rules, all of them the `:root` block and
`@media` header re-wrapping).

**Consequence for step 5.** Migrating a screen is not "swap one link". It is: delete the inline
`<style>` block, delete the `_theme.css` link, add one `../components/index.css`. The pixel test is
what proves the delete was safe.

---

## 1. The 32 declared custom properties

Value, how many declarations read it in `kit.css`, which properties it lands on, and the role that
reading shows. Sorted by group, not alphabetically, because the group is the finding.

### 1.1 Surfaces

| Variable | Value | Decls | Lands on | Role read from the usage |
|---|---|---|---|---|
| `--page` | `#0f1013` | 4 | `background` on `body`, `.uv-bar`, `.feed-trustbar` | the page behind everything |
| `--canvas` | `#141619` | 5 | `background` on `.device`, `.cat-nav`, `.feed`; `box-shadow` on `.idrow .av` | the app canvas (device stone) |
| `--surface` | `#1c1f24` | 18 | `background` on `.app-header`, `.card`, dropdowns, `.filter-panel`, `.state-block`, `.app-footer`, `dialog.app-dialog`, `.subcat .cnt` | a raised surface: card, header, dialog, panel |
| `--surface-2` | `#24282f` | 58 | `background` only: `.bal-toggle`, `.load-more`, `.toggle`, `.quick button`, `.provider-btn`, `.btn-secondary`, `.notif-all`, every hover fill | the quiet control fill (one property, one meaning) |
| `--slab` | `#1e2126` | 0 | nowhere | intended outer stone, never referenced (see C1) |
| `--plate` | `#121317` | 0 | nowhere | intended inner stone, never referenced (see C1) |
| `--card3d` | `#15171b` | 0 | nowhere | intended card stone, never referenced (see C1) |
| `--card` | (undeclared) | 5 | `background` on `.pos`, `.cta-bar`, `.wd-flow`, `.cc-banner`, `.toast` | broken reference (see C4) |

### 1.2 Text

| Variable | Value | Decls | Lands on | Role read from the usage |
|---|---|---|---|---|
| `--ink` | `#ede7da` | 113 | `color` x111 (`body` down), `stroke` x2 | primary text |
| `--muted` | `#a49d8f` | 98 | `color` x93, `stroke` x3, `background` x1 (`.toggle::after`), `fill` x1 (chart labels) | secondary text and quiet icon |

### 1.3 Brass (brand)

| Variable | Value | Decls | Lands on | Role read from the usage |
|---|---|---|---|---|
| `--accent` | `#c7a24e` | 77 | `background` x43 (CTA gradient start, `.badge-dot`, hover tints, `.feed-trustbar` 6 percent, `.protect`, `.push-banner`, trust cards), `border-color` x17, `box-shadow` x7, `border` x7 | two things at once: the action surface and the trust tint (see B1) |
| `--accent-2` | `#d9b968` | 17 | `background` x16 (always the second stop of the same gradient), `color` x1 | the lit end of the brass gradient |
| `--accent-text` | `#d7ac53` | 56 | `color` x37, `stroke` x8, `outline` x5, `border-*` x5, `fill` x1 | brass that is safe as text on graphite, and today also the focus ring (see B2) |
| `--brass-2` | `#e6c877` | 15 | `color` x13 (`.seo-h-ic`, `.seo-tagline em`, `.seo-by`, `.hf-eyebrow`, `.ht-badge`, `.bt-quote em`), `stroke`, `fill` | a brighter brass used only in the hero and SEO plate (see A2) |
| `--brass` | `#c7a24e` | 0 | nowhere | exact duplicate of `--accent` (see A1) |
| `--lime` | `#d9b968` | 0 | nowhere | exact duplicate of `--accent-2`, name inherited from an older direction (see A1) |
| `--bronze` | `#6e5a2e` | 0 | nowhere | documented in `DESIGN.md`, never used in code |
| `--brass-line` | `rgba(199,162,78,.30)` | 10 | `border` x6 (`.card`, `.ed-thumb`, `.cmt-av`, `.cmt-badge`, plate frames), `background` x2, `border-color` x1 | the inset brass hairline of the Vault plate |

### 1.4 Edges

| Variable | Value | Decls | Lands on | Role read from the usage |
|---|---|---|---|---|
| `--border` | `#2b2f38` | 97 | `border` x66, `border-top` x13, `border-bottom` x9, `color` x2 (`.ft-sep`, `.uv-bar .sep`) | the ordinary hairline |
| `--groove-dark` | `#0b0c0e` | 27 | `border-top` x14, `border-bottom` x11, `border-left/right` x2 | the recessed half of the engraved separator |
| `--groove-light` | `rgba(237,231,218,.055)` | 25 | `box-shadow` x25 only | the lit half of the same separator (always paired with the line above) |

### 1.5 Outcome (green = YES, red = NO; reserved)

| Variable | Value | Decls | Lands on | Role read from the usage |
|---|---|---|---|---|
| `--yes` | `#4fa96b` | 17 | `background` x9 (odds-bar fill, selected bet side), `border-color` x4, `box-shadow` x2 (the fill glow), `color` x2 | the YES / won outcome |
| `--no` | `#c85a50` | 9 | `background` x5 (odds-bar track), `border-color` x3, `color` x1 | the NO / lost outcome |
| `--on-yes` | `#0d1410` | 2 | `color` on the filled YES side | text on a filled YES |
| `--on-no` | `#160b09` | 2 | `color` on the filled NO side | text on a filled NO |

### 1.6 Material (texture, not colour)

| Variable | Value | Decls | Lands on | Role |
|---|---|---|---|---|
| `--stone-light` | inline SVG grain, 150px, opacity .9 | 1 | `background-image` on `.device` | outer stone grain |
| `--stone-dark` | inline SVG grain, 130px, opacity .8 | 7 | `background-image` on `.card`, the plates, trust cards, hero | inner stone grain |

### 1.7 Geometry (the only one that exists)

| Variable | Value | Decls | Lands on | Role |
|---|---|---|---|---|
| `--gutter` | `40px`, `14px` under `@media` | 4 | `padding-left/right` of header row, trust bar, category nav; `margin` of `.feed-inner` | the two-stone inset. Not drift: one responsive override, declared once per breakpoint |

### 1.8 Course chrome (not product)

`--rm-bg` `#131417`, `--rm-border` `#282b32`, `--rm-text` `#d8d2c6`, `--rm-muted` `#8b8579`,
`--rm-accent` `#d7ac53`. 24 declarations across `.sidebar*` and `.rm-*` only. This is the roadmap
sidebar every course page carries, not the product. It stays a separate block with its own prefix,
and it must keep shipping: the painted pages render that sidebar.

---

## 2. Finding A: drift (same role, more than one value)

| # | Drift | Where | What to do in step 2 |
|---|---|---|---|
| A1 | `--brass` = `--accent` = `#c7a24e`, and `--lime` = `--accent-2` = `#d9b968` | `:root` of `_theme-vault.css` | one primitive each, the duplicate name dies |
| A2 | three brasses that all read as "brass text": `--accent-text` `#d7ac53`, `--brass-2` `#e6c877`, `--accent` `#c7a24e` used as `color` in a few places | `.seo-*`, `.hf-eyebrow`, `.ht-badge` vs everything else | keep two primitives (`#d7ac53` text-safe, `#e6c877` lit), decide per role which is read; log the third as a bug candidate for step 7 |
| A3 | two generations of tinted YES/NO buttons stacked in the cascade: `#123726 / #4fd694 / #2c6f4b` and `#3a1620 / #ff868a / #8a3b40` (Harbor), overridden later by `rgba(79,169,107,.12) / #77d19b / #3f7d55` and `rgba(200,90,80,.12) / #e79087 / #8f4841` (Vault) | `_theme-vault.css` base vs its own texture block | only the Vault generation survives; the Harbor pair is dead weight |
| A4 | `#4fd694` and `#77d19b` and `#e88a84` and `#e79087`: two greens and two reds for "quiet outcome text" | `.yesno` vs `.pos-won` / `.pos-lost` / win-loss figures | one quiet-YES and one quiet-NO primitive |
| A5 | the graphite ramp is written both as tokens and as literals: `#0f1013` (`--page`) also appears raw x7, `#141619` (`--canvas`) as `#14161a` x5, plus `#191b1f`, `#1c1e22`, `#17191d`, `#121417`, `#111316`, `#15171b`, `#1b1e23`, `#20242a`, `#20242b`, `#0d0f12` | the two-stone layer in `_theme.css` | one graphite ramp of primitives, sorted by lightness; every literal points at it |
| A6 | `font-weight:bold` x44 and `font-weight:700` x44 for the same weight | throughout | one spelling |
| A7 | `font-family:'DM Sans',system-ui,sans-serif` (body) vs `'DM Sans',sans-serif` (x35 elsewhere) | `body` vs components | one stack per family |
| A8 | breakpoints: `520 / 560 / 620 / 640 / 640(min) / 760 / 860 / 900 / 960 / 980 / 1280 / 1440` | throughout | recorded, NOT fixed here. Responsive is stage 10; changing a breakpoint changes pixels |

Half-step type sizes (`9.5 / 10.5 / 11.5 / 12.5 / 13.5px`) are frequent enough to be a real scale,
not drift: 12.5px alone appears 19 times. They stay.

---

## 3. Finding B: one variable, several roles

| # | Variable | The roles it serves | Can they diverge? |
|---|---|---|---|
| B1 | `--accent` | (a) the **action** surface: Confirm bet, Add funds, the balance "+", `.btn-primary`, the active category tab, `.badge-dot`; (b) the **trust** tint: `.feed-trustbar` 6 percent, `dialog .protect` (USDC held 1:1), `.push-banner`, the footer trust cards, the shield icon | Yes. This is the textbook split: the action colour and the trust colour are one brass today and have no reason to stay one. Two tokens in step 2 |
| B2 | `--accent-text` | (a) brass **text and icon** on graphite (links, active nav, active bookmark, the logo tick); (b) the **focus ring** on 30-plus selectors (`outline:2px solid`) | Yes, and a focus colour has to survive both themes independently. Deferred by the lesson to the states stage, but recorded here with evidence so it is not re-discovered |
| B3 | `--surface` | (a) card / dialog / header **material**; (b) `.subcat .cnt` and `.filter-menu summary` **control** fill, which everywhere else is `--surface-2` | Yes, and today it is an inconsistency, not a role: same-looking chips read two different tokens |
| B4 | `--yes` / `--no` | (a) the odds bar and the selected bet **side**; (b) the resolved **result** (`.pos-won`, `.pos-lost`, the win and loss overlays) | Arguably. Same meaning ("this outcome won"), so step 2 keeps one pair and logs the split as an open question, not a silent decision |
| B5 | `--canvas` | (a) page-level **background** of `.device`, `.cat-nav`, `.feed`; (b) the **ring** around the profile avatar (`box-shadow`) | The ring only reads as a ring because it matches the background. Same role, keep |
| B6 | `--border` | (a) hairline **border** x89; (b) **text colour** of the two separator dots `.ft-sep`, `.uv-bar .sep` | A dot painted in border grey is a separator, not text. Same role, keep |

---

## 4. Finding C: values written past the variables

| # | What | Count | Where | Note |
|---|---|---|---|---|
| C1 | `--slab`, `--plate`, `--card3d` are declared, and the two-stone layer paints its stones with literals instead: `#191b1f`, `#1c1e22`, `#17191d`, `#121417`, `#111316` | 3 tokens dead, ~30 literals | `_theme.css` two-stone block | the biggest single hole: the signature surface of the product runs entirely on literals |
| C2 | `#180810` (near-black plum) hardcoded as the text and stroke colour on every brass CTA | 15 selectors, 30 occurrences | `.confirm-btn`, `.btn-primary`, `.state-btn.primary`, `.auth-btn.primary`, `.cat-nav [aria-current] button`, `.badge-dot`, `.quick button.sel`, `.tr-ic`, `.bal-add .ic`, `.hiw-arrow`, `.cmt-post`, `.cta-bar` first child | a real missing role: text on brass. It is the pair `--on-yes`/`--on-no` already model |
| C3 | outcome tints written raw: `#77d19b`, `#3f7d55`, `rgba(79,169,107,.12)`, `#e79087`, `#8f4841`, `rgba(200,90,80,.12)`, `#e88a84` | ~40 | `.yesno`, `.pos-won`, `.pos-lost`, win and loss overlays, `.hf-yes` / `.hf-no` | the quiet-outcome pair has no token |
| C4 | `var(--card)` read 5 times, never declared anywhere | 5 | `.pos`, `.cta-bar`, `.wd-flow`, `.cc-banner`, `.toast` | broken today: the declaration is invalid and those five surfaces fall back to transparent. Fix in step 2 by pointing them at the surface role. This is the one place where step 3 may legitimately change a pixel, and it must be called out |
| C5 | `.notif-empty` is styled in two inline blocks but is missing from `kit.css` | 1 rule, 2 pages | `active-bets-*`, `favorites-empty` | must be carried into the notifications component |
| C6 | Harbor leftovers that paint nothing because the Vault block overrides them: `#030a1e` (input bg), `#0a1a42` + `#020713` (HIW hero navy), the A3 tinted pair | 7 | `_theme-vault.css` | delete on the split, they are provably overridden |
| C7 | greys of the grey-box skeleton written raw in every inline block: `#999` x320, `#888` x250, `#555` x240, `#d6d6d6`, `#ccc`, `#222`, `#ededed`, `#dcdcdc`, and around 40 more | ~1800 occurrences | the inline `<style>` of all 76 pages | this is the wireframe skeleton, not the product. Most of it is repainted or hidden by the Vault layer. Step 3 keeps the geometry of those rules and drops the grey colour declarations; the pixel diff is exactly what proves each drop |
| C8 | `style="color:#8f8aa8"` in the markup | 76 (one per page) | the `.uv-bar` provenance strip, which the theme hides (`display:none`) | invisible in the product; delete with the strip or leave the strip alone. No pixel risk |
| C9 | inline `style=` in markup that IS visible: `background-image:url(assets/event-*.jpg)` on cards, `width:NN%` on chart and depth bars | ~60 | feed, category, event detail | data, not styling. Stays as markup |
| C10 | `box-shadow` written as 24 distinct literal recipes, 13 of them one-offs with raw `rgba(255,255,255,.17)` bevels | 24 | the embossed plate system | shadows are material, not colour roles. They go to primitives plus a material page, not to semantic tokens |

---

## 5. List 1: candidates for semantic roles

Each role below is proposed **only** because the usage table above shows it. The name is read from
our own product and `DESIGN.md` (graphite, brass, plate, groove, outcome), not from a foreign system.

### Roles with clear evidence

| Proposed role | Points at | Evidence (from section 1) |
|---|---|---|
| `--bg-page` | `#0f1013` | `body`, the page behind the device |
| `--bg-canvas` | `#141619` | `.device`, `.cat-nav`, `.feed` |
| `--bg-slab` | the outer stone graphite | the two-stone outer slab, today literal (C1) |
| `--bg-plate` | the inner stone graphite | the inset content plate, today literal (C1) |
| `--bg-surface` | `#1c1f24` | card, header, dialog, panel, footer, state block: 18 declarations |
| `--bg-control` | `#24282f` | 58 declarations, `background` only: every chip, quiet button, hover fill |
| `--text-primary` | `#ede7da` | 113 declarations |
| `--text-muted` | `#a49d8f` | 98 declarations |
| `--text-brass` | `#d7ac53` | 37 `color` + 8 `stroke`: links, active nav, active bookmark |
| `--text-brass-lit` | `#e6c877` | 13 `color` in the hero and SEO plate |
| `--text-on-brass` | `#180810` | 30 occurrences, no token today (C2) |
| `--border-hairline` | `#2b2f38` | 89 border declarations |
| `--border-brass` | `rgba(199,162,78,.30)` | the plate and card hairline, 10 declarations |
| `--edge-groove-dark` | `#0b0c0e` | 27, always the line of the engraved separator |
| `--edge-groove-light` | `rgba(237,231,218,.055)` | 25, always the highlight of the same separator |
| `--color-action` | brass `#c7a24e` | Confirm bet, Add funds, `.btn-primary`, active category tab, `.badge-dot` (B1a) |
| `--color-action-lit` | `#d9b968` | the second stop of every action gradient |
| `--color-trust` | brass `#c7a24e` | trust bar, `.protect`, push banner, footer trust cards (B1b). **Same value as `--color-action` today, different role: the trust tint and the action colour can diverge and the lesson's split applies** |
| `--outcome-yes` | `#4fa96b` | odds-bar fill, selected YES, won |
| `--outcome-no` | `#c85a50` | odds-bar track, selected NO, lost |
| `--text-on-yes` | `#0d1410` | filled YES side |
| `--text-on-no` | `#160b09` | filled NO side |
| `--outcome-yes-quiet` | `#77d19b` text on `rgba(79,169,107,.12)` with `#3f7d55` border | the tinted, spectator-not-trader YES button (C3) |
| `--outcome-no-quiet` | `#e79087` text on `rgba(200,90,80,.12)` with `#8f4841` border | the tinted NO button (C3) |

### Not roles: single-place colours (kept as primitives, revisited in step 7)

| Colour | The one place | Why it is not a role yet |
|---|---|---|
| `#cbc3b2` | `.ic,.ic-sm{stroke:...}` default icon stroke | one declaration; may be the same role as `--text-primary` at a lower weight |
| `#ded6c5` | `.notif-menu summary .ic:has(use)` | one declaration, looks like an accident next to `--ink` |
| `#e9e3d7` | hero heading | one place, near `--ink` |
| `#e7d6a6` | hero brass detail | one place, a fourth brass |
| `#1b1e23` | the graphite chip of the control family | one value used by the chip family; may be `--bg-control` at plate depth |
| `#0d0f12` | dialog amount input | one place, the darkest input well |
| `#fff` | 6 places (toggle knob, hover text, HIW hero heading, close icon) | pure white; a role only if the product decides "text on photo" is a role |
| `#000` | shadow colour in 5 recipes | material, not a colour role |

### Deliberately not created here

- `--color-focus` - real (B2, 30-plus selectors) but the lesson defers focus and component states to
  the Design System stage, in both themes at once. Recorded, not created.
- component-level tokens (`--button-bg`, `--card-radius`) - not on this product's scale.
- geometry roles - radius, spacing and control height repeat, they do not carry meaning that a theme
  overrides. They stay primitives and components read them directly.

---

## 6. List 2: the split into component files

476 classes are styled in `kit.css`. Below they are assigned. Rule used: a file exists when the
inventory has the row and the class family is real on the painted pages; the number is how many of
the 76 pages carry the leading class.

### `components/` shared spine

| File | Contents |
|---|---|
| `tokens.css` | primitive + semantic (step 2), plus `[data-theme="dark"]` in step 6 |
| `base.css` | `@font-face` imports, `*{box-sizing}`, `body`, `.device`, `.app-case`, container widths (1400 grid, `.feed-inner`, `.row`), the utility set (`.w40`-`.w90`, `.desk-only`, `.fine`, `.primary`, `.sel`, `.active`, `.cur`), `.ic` / `.ic-sm` icon sizing and stroke defaults, `.groove-sep` / `.groove-sep-b`, and the neutralisation block that hides the grey-box scaffolding (`.wf-*`, `.page-label`, `.zone-tag`, `.side`, `.delta`, `.uv-bar`, `.tbd`, `.placeholder-line`) |
| `index.css` | `@import` in fixed order: `tokens.css`, `base.css`, then every component alphabetically |
| `course-chrome.css` | `.sidebar*`, `.rm-*`, `.bk-arrow`: the roadmap sidebar the course pages render. Not product, kept apart on purpose, still shipped because every painted page has it |

### Navigation and chrome (inventory group 1)

| File | Classes (leading ones, page count) | Stand page |
|---|---|---|
| `header.css` | `.app-header` 76, `.row`, `.left`, `.utility`, `.logo-btn` 76, `.hiw-btn` 76, `.icon-btn` 76, `.bal-toggle` / `.bal-figure` / `.bal-amt` / `.bal-label` / `.bal-swap` / `.bal-add` 68, `.badge-dot` 68, `.bell-wrap` 68, `.notif-menu` / `.notif-drop` / `.notif-all` 68, `.avatar-menu` / `.dropdown` 68, `.auth-btns` 8, `.cat-condensed` 68, `.scrolled` | `ui-kit/header.html` |
| `catnav.css` | `.cat-nav` 26, `.cat-ic` 26, `.cat-layout` / `.cat-main` 48, `.subcat` / `.subcat-head` / `.cnt` 5, `.feed-subfilter` 1, body classes `.cat-politics` / `.cat-crypto` / `.cat-culture` / `.cat-general` | `ui-kit/catnav.html` |
| `bottomnav.css` | `.bottom-nav` 76, `.bn-bal` 68 | `ui-kit/bottomnav.html` |
| `tabs.css` | `.tabs` 9 (My Bets), `.seg` 9, `.rules-tabs` / `.rules-tab` 9, `.ed-range` 9, `.ed-tabs` / `.ed-tabbar` / `.ed-tablabel` / `.ed-tabradio` / `.ed-tabpanel` / `.ed-tabwrap` / `.ed-tab-count` 9, `.ptabs` / `.ptab-bar` / `.ptab-in` / `.ptab-lbl` / `.ptab-panel` 2 | `ui-kit/tabs.html` |
| `footer.css` | `.app-footer` 76, `.footer-inner` / `-top` / `-brand` / `-cols` / `-col` / `-tagline` / `-logo` / `-popular` / `-legal` 76, `.popular-links`, `.legal-links`, `.social-row`, `.lang-menu`, `.sub-label` | `ui-kit/footer.html` |
| `trustbar.css` | `.feed-trustbar` / `.ft-inner` / `.ft-item` / `.ft-ic` / `.ft-sep` 76, `.footer-trust` / `.trust-head` / `.trust-items` / `.trust-item` / `.tr-ic` / `.tr-txt` 76 | `ui-kit/trustbar.html` |

### Browse: feed and cards (group 2)

| File | Classes | Stand page |
|---|---|---|
| `card.css` | `.card` 24, `.card-body` 11, `.top` / `.top-txt`, `.thumb` 8, `.q` 8, `.why` 7, `.prob` 17, `.prob-line` 8, `.meta` / `.meta-txt` / `.m-label` / `.m-val` 8, `.bookmark-btn` 8 | `ui-kit/card.html` |
| `oddsbar.css` | `.oddsbar`, `.track`, `.fill`, `.lbls`, `.l-yes`, `.l-no` (JS-injected markup), `.ed-oddsbar` 9 | `ui-kit/oddsbar.html` |
| `yesno.css` | `.yesno` 10, `.compact` 10 | `ui-kit/yesno.html` |
| `options.css` | `.options` 10, `.opt-row` 10, `.opt-name` 10, `.opt-prob` 21, `.opt-list` 2, `.opt-sel-tag` 2 | `ui-kit/options.html` |
| `feed.css` | `.feed` 76, `.feed-inner` 76, `.feed-head` 43, `.feed-controls` 16, `.grid` 11, `.grid-l` 9 | `ui-kit/feed.html` |
| `hero.css` | `.feed-hero`, `.hero-duo` / `-main` / `-side` / `-feature` / `-trust` / `-promo` / `-hot`, `.hf-*` (28 classes), `.hh-*` (6), `.ht-*` (3), `.brand-tile` + `.bt-*` (5) - all on `event-feed.html` only, but a named block of the inventory | `ui-kit/hero.html` |
| `seo-plate.css` | `.feed-seo` 6, `.feed-seo-wrap` 5, `.seo-brand` / `.seo-text` / `.seo-tagline` / `.seo-by` / `.seo-h-ic` / `.seo-tick` 5 | `ui-kit/seo-plate.html` |
| `loadmore.css` | `.load-more` 5, `.load-more-wrap` 5 | `ui-kit/loadmore.html` |
| `filters.css` | `.filter-menu` 76, `.filter-panel` 76, `.reverse-row` 3, `.toggle[role=switch]` 3 | `ui-kit/filters.html` |

### Event Detail (group 3)

| File | Classes | Stand page |
|---|---|---|
| `event-detail.css` | `.ed-layout` / `.ed-main` / `.ed-head` / `.ed-thumb` / `.ed-cat` / `.ed-q` / `.ed-prob-big` / `.ed-actions` / `.ed-section` / `.ed-facts` 9-11, `.args` / `.arg-col` 9, `.resolution` / `.rules-note` 9, `.resolved-panel` / `.rp-inner` 1 | `ui-kit/event-detail.html` |
| `chart.css` | `.chart-svg` 11, `.ed-chart` / `-head` / `-now` / `-area` / `-foot` / `-multi` 9, `.ed-plot` / `.ed-xaxis` / `.ed-yaxis` / `.nowline` / `.ml-line` / `.ed-legend` 9 | `ui-kit/chart.html` |
| `betpanel.css` | `.bet-panel` 11, `.bp-inner` / `.bp-head` / `.bp-dir` / `.bp-side` / `.bp-pct` / `.bp-cash` / `.bp-hint` / `.bp-amount-row` / `.bp-amount-lbl` / `.bp-change` / `.bp-selected` / `.bp-sel-name` 8-10, `.bet-dock` 8, `.dock-meta` 4, `.bet-sheet` / `.sheet-grab` 4 | `ui-kit/betpanel.html` |
| `market.css` | `.market-box` / `-head` / `-title` / `-chevron` / `-body` / `-stats` / `-depth` 9, `.md-*` (10 classes) 9, `.ms-*` (5) 9 | `ui-kit/market.html` |
| `comments.css` | `.cmt` / `-list` / `-av` / `-user` / `-meta` / `-text` / `-body` / `-actions` / `-controls` / `-badge` 9, `.cmt-compose` / `.cmt-input` / `.cmt-post` 7, `.cmt-signin` 2, `.reply` 9 | `ui-kit/comments.html` |
| `bets-table.css` | `.ptable` 9, `.hold-cols` / `.hold-col` / `.hold-row` / `.hold-name` / `.hold-amt` / `.hold-rank` / `.hold-out` 9, `.act-list` / `.act-row` / `.act-txt` / `.act-time` 9, `.you` 7 | `ui-kit/bets-table.html` |
| `related.css` | `.related-events` / `.related-list` / `.related-more` / `.rel-q` / `.rel-thumb` / `.rel-odds` 9 | `ui-kit/related.html` |

### Forms, dialogs, inputs (group 4)

| File | Classes | Stand page |
|---|---|---|
| `button.css` | `.btn-primary` / `.btn-secondary` / `.btn-sm` / `.btn-md` / `.btn-lg` / `.btn-block` (stand only today, 0 product pages), `.confirm-btn` 76, `.state-btn` 24, `.auth-btn` 8, `.provider-btn` + `.prov-x` / `.prov-apple` / `.prov-google` 76, `.hf-btn`, `.hf-cta` | `ui-kit/button.html` |
| `input.css` | `.amount-row` / `.amount-input` 76, `.quick` 76, `.field-label` 76, `.cmt-input` 7, `.cc-cat input[type=checkbox]` | `ui-kit/input.html` |
| `dialog.css` | `dialog.app-dialog` 76, `.sheet-head` / `.sheet-body` / `.sheet-close` / `.sheet-sub` 76, `.grab`, `::backdrop`, `.dlg-note`, `.fine` | `ui-kit/dialog.html` |
| `hiw-dialog.css` | `.hiw-dialog` + `.hiw-hero` / `-hero-inner` / `-glow` / `-tagline` / `-body` / `-sec` / `-sec-txt` / `-ic` / `-label` / `-faq` / `-full` / `-arrow` / `-close` / `-lead` 76 | `ui-kit/hiw-dialog.html` |
| `signin.css` | `.signin-dialog` 76, `.signin-lead` | `ui-kit/signin.html` |
| `notice.css` | `.protect` 76, `.widget-box` 76, `.inline-error` 8, `.spinner-box` 6, `.reconcile-box` 6, `.push-banner` / `.push-msg` / `.push-actions` 2 | `ui-kit/notice.html` |

### Feedback and states (group 5)

| File | Classes | Stand page |
|---|---|---|
| `state-block.css` | `.state-block` / `.state-title` / `.state-msg` / `.state-actions` 22, `.sys-links` / `.sys-link-list` / `.sys-note` 1-2 | `ui-kit/state-block.html` |
| `skeleton.css` | `.skeleton` 11, `.sk-line` 11, `.sk-thumb` 5, `.sk-btn` / `.sk-head` / `.sk-row` 3 | `ui-kit/skeleton.html` |
| `toast.css` | `.toast` / `.toast-wrap` / `-group` / `-inner` / `-msg` / `-close` / `-error` 1 (the spec page), `.tc-page` | `ui-kit/toast.html` |
| `outcome-dialog.css` | `.outcome-dialog` 17, `.win-dialog` 4, `.loss-dialog` 2, the share card | `ui-kit/outcome-dialog.html` |
| `notifications.css` | `.notif-empty` (from C5), notification list rows | `ui-kit/notifications.html` |

### Profile and account (group 6)

| File | Classes | Stand page |
|---|---|---|
| `profile.css` | `.idrow` / `.av` / `.name` / `.handle` / `.edit` / `.who` 2, `.gallery` 2, `.pos-status` 7 | `ui-kit/profile.html` |
| `position.css` | `.pos` 14, `.pos-list` 13, `.pos-side` 13, `.pos-note` 9, `.pos-q` / `.pos-top` / `.pos-status` 7, `.pos-figures` / `.pos-fig` 6, `.pos-won` / `.pos-lost` 2, `.pos-yes` / `.pos-no` 1 | `ui-kit/position.html` |
| `account.css` | `.cta-bar` 3, `.wd-flow` 1 (wallet withdraw), the transaction list | `ui-kit/account.html` |

### System pages (group: one-off by the inventory, but the CSS needs a home)

| File | Classes | Note |
|---|---|---|
| `cookie-consent.css` | `.cc-*` (16 classes), 1 page | one-off by the inventory rule, but its CSS cannot stay inline once the inline blocks are deleted. It gets a file and a stand page; the inventory row stays "one-off" |

### Classes that belong to no component

- **Parser artifacts, not classes:** `com`, `googleapis`, `jpg`, `webp`, `ref` (fragments of URLs).
- **Grey-box scaffolding, hidden by the theme:** `.wf-nav`, `.wf-toggle`, `.wf-overlay`, `.wf-tree`,
  `.wf-sec`, `.wf-screen`, `.wf-states`, `.wf-substate`, `.wf-note`, `.wf-nav-head`, `.wf-nav-close`,
  `.page-label`, `.zone-tag`, `.side`, `.delta`, `.uv-bar`, `.tag`, `.sep`, `.cur`, `.tbd`,
  `.placeholder-line`, `.state-switch` / `.ss-row` / `.ss-label`, `.navtree`, `.mini-header`,
  `.nav-col`, `.annotations`, `.brand`. All go to the neutralisation block in `base.css`, none get a
  stand page. **Question for step 7:** delete them outright instead of hiding them. Deleting is
  cleaner but is a pixel risk only if something is not actually hidden, so it waits for the diff.
- **Styled but on no page, and not scaffolding** (candidates to delete in step 7): `.bp-opt`,
  `.bp-opts`, `.bp-opt-pct`, `.chart-box`, `.chart-cap`, `.chart-wrap`, `.dim-note`, `.dir-pill`,
  `.hero-mini`, `.hiw-head`, `.lg-item`, `.preselect-note`, `.sheet`, `.open`, `.next`, `.planned`,
  `.sidebar-divider`, `.m-label`, `.m-val`, `.signin-lead`, `.grab`.
- **In the markup with no style** (11): `.prov-google` (needs none, the mark is a coloured SVG),
  `.ed-act`, `.ed-chart`, `.ed-market`, `.rules-panel`, `.deposit-dialog`, `.hiw-lead`,
  `.toast-wrap`, `.ed-chart-multi`, and two JS-string fragments. Check each in step 3: a hook with no
  style is fine, a component with no style is a bug.

### One-off list from stage 08, re-counted on the assembled product

| One-off row | Real count now | Verdict |
|---|---|---|
| Cookie-consent panel `.cc-*` | 1 page | stays one-off, gets a file (see above) |
| Withdraw flow `.wd-flow` | 1 page | stays one-off, lives in `account.css` |
| 404 / 500 / maintenance bodies | 3 pages, all composed from `.state-block` + `.sys-links` | confirmed: not components, the state block already is one |
| Provider-conflict / not-found / minimum-not-met notices | 1 page each, built from `.inline-error` + `.state-block` | confirmed one-off |
| Toast set `.toast*` | 1 page (the spec page) | **promoted**: the inventory already lists it as a component and it is a product mechanism, not a page block |
| `.notif-empty` | 2 pages | **promoted** into `notifications.css` (C5) |

---

## 7. List 3: the foundation pages

| Page | What goes on it |
|---|---|
| `ui-kit/color.html` | the primitive palette (graphite ramp, brass family, outcome pair, greys), then every semantic role with the primitive it points at and the "grew out of" note, then the contrast pairs (text on page, text on surface, text on control, brass text on graphite, on-brass text on brass, outcome text on tint) with the ratio and the AA verdict. After step 6, each role is shown in light and dark side by side |
| `ui-kit/typography.html` | three families (Space Grotesk display, DM Sans body, IBM Plex Mono figures) with the one canonical stack each (A7), the size scale actually in use (8, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 15, 16, 18, 19, 20, 23, 24, 30, 38 plus the two `clamp()` display sizes), weights 500 / 600 / 700 (A6 resolved), line-heights 1.04 to 1.6, and the reading widths (60ch, 32ch, 800px SEO column). Live samples come from `voice/docs/microcopy.md`, never lorem |
| `ui-kit/geometry.html` | spacing scale 2 to 40 shown as blocks, radius scale 2 / 6 / 8 / 10 / 12 / 16 / 100px / 1000px / 50 percent, control heights 32 / 36 / 44 / 52, the 44px touch-target rule, `--gutter` at both breakpoints, the 1400 grid and the container widths (420, 464, 800, 1400), and the page frame from `base.css` |
| `ui-kit/icons.html` | the 15 Solar filled symbols, all referenced today (`i-bookmark-b` 181 uses, `i-shield-b` 77, `i-verified-b` 77, `i-bell-b` 68, `i-heart-b` 36, the five `i-cat-*`, `i-chat-b`, `i-share-b`, the three `i-seo-*`), plus the inline outline set that `.ic` / `.ic-sm` carry, at working sizes (15 / 16 / 17 / 18 / 22px) and in the role colours |
| `ui-kit/material.html` (fifth page, the material that does not fit the four above) | the two-stone system (grain textures `--stone-light` / `--stone-dark`, slab and plate depths), the engraved groove pair, the brass hairline and the notched corner, the shadow set (24 recipes today, C10) and the glow used on the odds-bar fill. Without this page the signature of the product is nowhere documented, and C1 says it is exactly the part that is running on literals |

Coverage rule for step 7: after the pages exist, every token in `tokens.css` and every class in
`base.css` must appear on one of these five, or it is deleted.

---

## 8. What step 2 has to decide (open questions)

1. **B1 split confirmed?** `--color-action` and `--color-trust` as two roles on one brass today.
2. **B4:** one outcome pair, or a second pair for the resolved result (`won` / `lost`)? Proposed: one
   pair now, note in the file, revisit in step 7.
3. **C4 `var(--card)`:** point the five surfaces at `--bg-surface`. This is the single change in the
   whole stage that can move a pixel, and it moves it towards correct. Flag it in the diff, do not
   hide it.
4. **A8 breakpoints:** recorded, not touched. Fixing them is stage 10.
5. **Grey-box scaffolding:** hide (safe) or delete (clean) in step 3. Decision after the first diff.

---

## 9. What step 6 closed, and what the audit got wrong about itself

The audit above is a reading of a product, and it read the colour layer correctly: the roles it
proposed in section 5 are still the roles, and step 6 changed none of their names. It read the
geometry and type layer the same way, and there the method was wrong. A colour in a screen is
evidence of a decision. A `9.5px` in a screen is evidence that someone typed `.72rem`. Recording
every literal as a token produced 348 entries: not a system, a transcript.

Step 6 turned each family into a scale with a rule (`architecture.md`, "The scales"). The count went
348 -> 265, and the map is data in `ui-kit/_rescale.py`.

| Finding | What became of it |
|---|---|
| A4, two quiet reds for one job | merged. `#e88a84` -> `#e79087`, the one colour move above deltaE 1.5 (3.44) and the only one a person can see |
| A5, the ramp written as tokens and as literals | closed by gate 12: a raw value in a scale property fails the build |
| C1, the tokens declared and never wired | `--card3d` became `--bg-card-quiet` in step 2; `--slab` (`--graphite-820`) and the two 160px grains had no job and were deleted; `--surface-grid`, `--logo-tick`, `--bg-slab-to` and `--container-sidebar` turned out to be written as literals in a component and are now wired |
| C4, `var(--card)` declared nowhere | closed in step 2 |
| C10, 24 literal shadow recipes | the recipes stay (a box-shadow keeps its own offsets, by rule), but the inks under them went from 14 alphas to 5 |
| B4, one outcome pair or two | two. `--result-won-*` and `--result-lost-*` existed since step 2 and nothing read them: `.pos-won` and `.pos-lost` were sharing the live outcome rule. They are wired now, at the same values, so the split is real and no pixel moved |
| the coverage rule ("every token appears on a page or is deleted") | superseded by something stronger: gate 11 fails the build on a token nobody READS. Appearing on a page is not use |

Two things this step found that the audit did not look for:

- **A size wearing a spacing name.** `--space-5` was the height of the odds bar, `--space-3` a status
  dot, `--space-1` a hairline and a 1x1 hidden input. Counting them as spacing is what let the space
  scale reach 25 steps, and no amount of merging fixes a scale that is measuring two different things.
- **A touch target built out of padding.** The deposit amount field reached 45px because its padding
  happened to add up; on the 4px grid the same padding lands at 41 and the target is gone. It now
  reads `min-height:var(--control-44)`, because a target is a rule and has to be written as one.
