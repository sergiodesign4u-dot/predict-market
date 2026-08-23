# Map

Which screen is made of which components, which tokens those components read, and where each zone
gets its words. Then the same data read backwards, which is the question this file exists for:
**if I change this token, what moves.**

**Taken from the code on 2026-08-23, not recalled.** Screen to component from the class names
standing in the markup, against each stylesheet's own declared `Classes:` contract. Component to
token from every `var()` in the stylesheet body, not from the `Reads:` header, which is the colour
register only and would miss every space, size and duration. Zone from the landmark elements a
document actually has.

**The reverse list is an INVERSION of exactly that data**, never a second pass over the code. Two
readings of one thing drift, and the one used less often goes stale first.

---

## The instrument, and what it cannot see

Three blind spots, found by running it. Each is named here because a map that hides its own edge is
worse than a shorter map.

1. **A class declared by more than one stylesheet attributes nothing.** Nine class names are declared
   by two or more components. A shared selection class is claimed by four of them, and the two
   outcome words by two. Attributing a shared class to every claimant put components on screens they
   have never stood on. The sweep now credits only classes owned by exactly one file, and the nine
   are listed at the foot of this file rather than silently resolved.
2. **A token a page script writes is invisible to it.** The multi-outcome chart chooses its line
   colours in an inline script, so four chart-series roles read as unread by every component. They
   are alive; the reader is a screen. This is the same shape as an atom whose class is written at run
   time, and it is why the idle control below asks WHICH zero before it reports one.
3. **A token whose only reader is the thing that shows it.** Two primitives read as unread here and
   are drawn as swatches by the vitrine's own page stylesheet. **This is a settled judgement, not a
   new finding**: `ui-kit/docs/consistency.md` §4 measured the same four candidates, found all four
   were the instrument, and recorded that a sweep for dead values that does not read the vitrine
   deletes the swatches first. Reproduced here, not re-opened.

**The stack was the fourth, and it was mine.** The first take of this sweep put twenty-one components
in the page level of a screen that has six, because the HTML parser fires an end tag for a
self-closing glyph and a naive push-and-pop drifts by one on every icon. Popping by name rather than
by count moved every class into a real landmark and left the page level empty. **A reading that puts
everything in the default bucket is a reading of the instrument.**

---

## Zones

Six, and they are the landmarks the documents have rather than a vocabulary invented here.

| Zone | What it is | Where its words come from |
|---|---|---|
| header | the top bar, on every screen | `copy > Global chrome > Header` |
| main | the screen's own content, the only zone that differs by family | `copy > Screens > <family>` |
| footer | the trust strip and link columns | `copy > Global chrome > Footer` |
| bottom nav | the four slots, narrow widths only | `copy > Global chrome > Bottom nav` |
| overlay | the shared dialogs carried by every screen | `copy > Global chrome > Sign-in dialog`, `> Deposit dialog`, and `copy > Screens > How It Works, the dialog` |
| explainer still | the miniature specimens inside the explainer's stage | it quotes the product; see the split below |
| review chrome | the reviewer's panel and theme control. **Not the product**, and excluded from every count in this file | none |

**The global zones have no per-screen copy, by construction.** The copy inventory keeps header,
footer and bottom-nav strings in its Global chrome section, which has no screens column: those
strings stand on every screen and there is nothing to list. In this map they carry the zone `global`
and their screen set is all of them.

---

## The global layer

Same components in the same zone on every screen. Counted 2026-08-23 over the painted tree.

| Zone | Components, on all 119 screens | Components on some |
|---|---|---|
| header | `button`, `header`, `iconbtn`, `logo`, `search` | `navitem` on 83, `chip` on 65 |
| footer | `filters`, `footer`, `logo`, `trustbar` | none |
| bottom nav | `bottomnav`, `navitem` | none |
| overlay | `button`, `chip`, `dialog`, `hiw`, `iconbtn`, `input`, `navitem`, `notice`, `platehead`, `quick`, `search` | `yesno` and `betpanel` on 12, `options` on 4 |

**Four dialogs ship on every screen** - sign in, add funds, how it works, and the search sheet - so
eleven components stand in the overlay zone of a document whose visible content has nothing to do
with them. **A closed dialog is a state, not a missing surface**, and it is also not a placement: the
split below is the whole point.

---

## The main zone, by family

The only zone that differs. One row per family; a family's state pages carry a subset of its own
components, never a different set.

| Family | Components in `main` |
|---|---|
| Event Feed (and the four category pages) | `browse-shell`, `card-grid`, `card`, `catnav`, `chip`, `feed`, `filters`, `hero`, `iconbtn`, `list-head`, `loadmore`, `logo`, `notice`, `options`, `search`, `seo-plate`, `skeleton`, `state-block`, `button`, `yesno` |
| Event Detail | `detail-shell`, `event-detail`, `betpanel`, `bets-table`, `card`, `catnav`, `chart`, `chip`, `comments`, `dialog`, `iconbtn`, `input`, `market`, `notice`, `oddsbar`, `options`, `position`, `quick`, `related`, `skeleton`, `state-block`, `tabs`, `yesno`, `browse-shell`, `feed`, `button` |
| Favorites | `browse-shell`, `card-grid`, `card`, `catnav`, `chip`, `feed`, `filters`, `iconbtn`, `list-head`, `options`, `skeleton`, `state-block`, `toggle`, `yesno`, `button` |
| My Bets (active and history) | `browse-shell`, `feed`, `list-head`, `position-list`, `position`, `skeleton`, `state-block`, `tabs`, `button` |
| Wallet | `browse-shell`, `feed`, `list-head`, `position-list`, `position`, `notice`, `skeleton`, `state-block`, `action-bar`, `button` |
| Notifications | `browse-shell`, `feed`, `list-head`, `position-list`, `position`, `dialog`, `notice`, `skeleton`, `state-block`, `button` |
| My profile / public profile | `profile`, `position-list`, `position`, `tabs`, `card`, `crumb`, `dialog`, `list-head`, `skeleton`, `state-block`, `action-bar`, `browse-shell`, `feed`, `button` |
| How It Works | `hiw`, `hero`, `platehead`, `position`, `crumb`, `action-bar`, `logo`, `browse-shell`, `feed`, `button` |
| The five documents | `browse-shell`, `crumb`, `feed`, `list-head`, `notice`, `related`, `toc`, `seo-plate` |
| System pages (missing, server, maintenance) | `browse-shell`, `feed`, `state-block`, `button` |
| Consent and transient messages | `cookie-consent`, `toast`, `browse-shell`, `feed`, `iconbtn`, `input`, `list-head`, `state-block`, `button` |
| Sign in, Add funds, Win, Loss | **`feed` only** | 

**The last row is a finding, not a formatting slip.** Four families have no product content in
`main` at all: they are the feed with a dialog over it, and their entire surface is the overlay. A
probe scoped to the content area reports them as having no heading, which is what happened once
already. **Read what the container excludes before believing what a scope counted.**

`toc` stands on the four document pages that have a contents rail; `seo-plate` on the feed family and
on the document that carries a plate. `related` on the documents and on Event Detail, which are two
different jobs wearing one component - a related-events list and a related-documents list.

---

## The reverse list: if I change this, what moves

**Derived by inverting the two tables above. It is not a second reading of the code.**

**It opens in two knees, and the second is not optional.** A component reads colour through a
semantic role and never through a raw value, so a one-knee inversion asks which components name a
primitive, gets nothing, and reports the entire primitive level as dead. The chain is:

```
primitive  ->  semantic role  ->  component  ->  screen
```

Worked, from the data:

| Token | Level | Carried by | Read by | Stands on |
|---|---|---|---|---|
| `--brass-400` | primitive | four roles: the focus ring, the chrome accent, brass text, brass icon | 26 components | 119 screens |
| `--text-primary` | role | resolves to the Vault ink and the Daylight ink | 37 components | 119 screens |
| `--color-action` | role | resolves to one brass primitive | 13 components | 119 screens |
| `--outcome-yes-text` | role | resolves to a green primitive in each theme | 10 components | 119 screens |
| `--bg-card` | role | resolves to one graphite and one chalk primitive | 3 components | 119 screens |

**`--brass-400` is the row to read twice.** Named directly by no component at all. Change it and 26
components in 119 screens move, in both themes, through four roles that have nothing to do with each
other: a focus ring, the review chrome, a word and a glyph. That is the answer a one-knee list gets
exactly backwards.

**The shape of the reach.** The widest-reaching tokens are the ink and the hairline, at 33 to 38
components and every screen. The narrowest sit at one component and three screens - the display
sizes and the translucent overlays that only the hero uses. **Between those two ends there is no
middle-sized token in this system**: a value here is either structural and everywhere, or it belongs
to one component. That is what a two-level token file produces, and it is the reason a change to a
role is never a local change.

**Reading order for a proposed change:** find the token here, take its screen count, and if the count
is the whole tree the change is a change to the product rather than to a screen. Then check both
themes, because a role has a value in each and only one of them is on the page you are looking at.

---

## Idle control

Closed with numbers, and every zero says which zero it is.

| Question | Answer | Which zero |
|---|---|---|
| A component standing on no screen | **0 of 49** | none to explain |
| A component whose only stand is the explainer's stage | **0 of 49** | none |
| A token read by no component | **6 candidates, 0 genuinely dead** | 4 are the chart series, read by a page script the sweep cannot see; 2 are drawn as swatches by the vitrine, which `ui-kit/docs/consistency.md` §4 settled and this run reproduced |
| A class declared and owned by more than one file | **9** | listed below; each is a real ambiguity in the contract, not a dead class |

**Stage 08 asked the component question before the tree had finished growing, and the answer could
have changed since. It has not: every component stands somewhere.** The interesting result is not the
zero, it is the split below.

---

## Placement against still

**Four components read 119 screens and are doing their job on far fewer.** The explainer dialog
carries three miniature specimens - a card, a bet panel and a position row - inside an
`aria-hidden` stage, and that dialog ships on every screen.

| Component | On N screens | Doing its job on | A specimen inside the explainer on |
|---|---|---|---|
| `betpanel` | 119 | 15 | 104 |
| `position` | 119 | 27 | 92 |
| `yesno` | 119 | 29 | 90 |
| `card` | 119 | 43 | 76 |

**A count that does not separate these two answers the wrong question.** "This component stands on
119 screens" reads as *it is everywhere in the product*; the truth is that it is everywhere in one
shut dialog and in a quarter of the product. A change to `betpanel` moves fifteen screens a reader
uses and a hundred and four illustrations of it, which are different risks and want different
checks - the illustrations are quotations of the product and must keep agreeing with it.

The `Stands on:` lines in the stylesheet headers are dated readings taken before this split existed
and are not corrected here: **this file states the split and the headers keep their date**, which is
what a dated reading is for.

---

## Roll-call

| Set | In this map | Deliberately not |
|---|---|---|
| Painted documents | **120 of 120** | 0 |
| of which product screens | 119 | the index of the tree is not a screen and carries the only second stylesheet in the tree |
| Components | **49 of 49** | 0 |
| Zones | 6 product zones + the review chrome, excluded | the review chrome, because it is not the product |
| Tokens reached by the inversion | **348 of 354** declared in the two levels | 6, each explained in the idle control |

**The painted tree has no registry**, so the screen set here is the directory listing rather than a
declared list, and the roll-call is a count of files. `ui-kit/_nav.js` names this as a standing debt
in its own header. It is filed rather than fixed: closing it is an edit to every document in both
trees, which this stage does not make.

---

## The nine shared class names

Each is declared by more than one stylesheet, so a class alone cannot say which component is
standing. They are not defects on their own - two of them are a deliberate shared vocabulary - but a
sweep that resolves them by guessing produces a map that is confidently wrong.

| Class | Declared by |
|---|---|
| the selected state | `chip`, `options`, `tabs`, `yesno` |
| the two outcome words | `hero`, `yesno` |
| three skeleton widths | `cookie-consent`, `skeleton` |
| the sub-category name | `browse-shell`, `catnav` |
| the SEO plate | `browse-shell`, `seo-plate` |
| the contents rail | `browse-shell`, `toc` |

The last three are a pattern naming the slot and a component naming itself, which is the shell
declaring where a thing goes and the thing declaring what it is. The first two are one vocabulary
shared on purpose. **Nothing here is proposed as a change**; it is stated so the next reader of this
map knows why a class name is not an identifier.

---

## What this file does not own

What each component IS and what level it sits at, in `ui-kit/docs/inventory.md`. What every token
means and why the levels are two, in `components/tokens.css` and `components/CLAUDE.md`. Every
string, in `voice/docs/microcopy.md`. What the product DOES, in `behaviour.md` beside this file.
