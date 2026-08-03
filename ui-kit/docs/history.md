# What each pass settled

The long form. Nine audit passes ran over the Tokens and Components stage, and this file holds what
eight of them found, at the length the finding needed; [`docs/decisions.md`](../../docs/decisions.md)
holds the dated DECISION that came out of each, at the length a record needs. Pass 7c never had a
section here and is in the record only.

That is the whole split, and it is worth stating once because the two files read as if they overlap
and do not: measured against each other, only 7 to 32 per cent of the wording here appears there.
The record says what was decided and on what grounds. This says what was measured, what the first
attempt got wrong, and which of the checks could see it. If you want to know whether a thing is
still true, read the record; if you want to know how it was found, read this.

Sections are in the order the passes ran. Nothing here is edited after the fact, for the same reason
nothing in the record is: an entry is true as of its own date, and rewriting it would make it
disagree with the commit it describes.

No em dash.

---

## What step 7 settled

The deletion pass and the defect table. Thirty-four findings, all closed; the ones that changed a rule
rather than a line are here.

### A box that clips decoration must not be a scroll container

`overflow:hidden` makes a box scrollable, it only hides the scrollbar. Thirteen stones in this system
clip a decorative pseudo-element (a brass glow, a photographic head, a grain plate), and one of them
was actually scrolled: `.sheet-head` sat at `scrollLeft:52`, which dragged the win overlay's heading
out of its own box and clipped "You were right" to "u were right", in both themes, on four screens.

`overflow:clip` creates no scroll container at all, so the same clipping cannot move. All thirteen are
`clip` now, and the rule is: **hidden is for a box that may scroll and you do not want the bar; clip is
for a box that must never scroll.** Almost every decorative clip in a product is the second one.

### Target size follows the pointer, not the viewport

WCAG 2.5.5 asks for 44px because a finger is 44px wide, and a finger does not get smaller when the
window gets wider: a touch laptop at 1280 needs what a phone needs. The rule was bound to
`max-width:640px`, so every icon button on a touch screen above that width was 36px. It is bound to
`@media (pointer:coarse)` now. A fine pointer keeps 36px, which clears 2.5.8 (24x24) with room to
spare, and the two levels of the standard end up matching the two kinds of hand.

### A filled glyph is neither a line nor a word

The card bookmark was a 16x16 target: below 2.5.5, below 2.5.8, and small enough that it is a miss
rather than a tap. It now carries a 44px box with a negative margin equal to half the difference, so
the target grew and not one pixel moved.

### Reduced motion is a promise, so it is made once

Three components carried a `prefers-reduced-motion` block and twenty did not. A person who asks the
operating system for less motion is not asking twenty components individually, so the block is in
`base.css` now, once, for everything.

### A candidate is not an outcome

The multi-outcome chart drew its first line in `--green-200` and its third in `--brass-300`: the same
pixels the product uses to mean "this side won" and "this is us". Green, red and gold are reserved
meanings here, so the categorical series moved into the arc those leave free, cyan 187 through
magenta 328, with one desaturated neutral. All five clear 4.5:1 on the chart well in both themes,
because the reading under the chart is drawn in the selected line's colour.

### Two roles may share a value

Twenty-seven groups of roles resolve to one colour in both themes. That is not duplication to merge:
a role is a reason, not a value, and the day an outcome and a result need to differ, the file has
somewhere to put the difference. The rule written above section 2 is that a coincidence is declared
where it happens, and the gate for a role with no reason at all is 11.

### A third copy is a fork

`shell.html` held its own hand-kept copy of the app header, next to the copy on `header.html` and the
copy on 76 painted screens. It composes the component specimens now and holds no markup of its own.

### The register decides whether a small-caps label is a tell

`PRICE CHART`, `VOLUME`, `WHAT HAPPENED`. In a landing page an eyebrow above every section is AI
grammar; in a product these are field labels over data groups, and removing them would cost a reader
the name of what they are looking at. Kept, deliberately, and written down here so the next audit does
not re-open it.
## What step 7b settled

A second audit, run against `components/` and every painted screen, on the assumption that a system
which passes its own gates is exactly where the interesting defects hide. Fourteen findings. Four of
them changed a rule.

### One element, one rule

Step 1 read the styling out of the painted product, and the painted product had **two** stylesheets on
it: the grey-box skeleton the wireframe generator wrote inline, and the Vault theme file loaded after
it. The extraction kept both and concatenated them, so 116 selectors were written twice over. 200
declarations in the first layer were overridden by the second and rendered nowhere at all;
`loadmore.css` described one button twice, nine properties apart.

Nothing rendered them because every place a component stands is inside `.app-case`, and `.app-case S`
is S plus one class, so it wins wherever both apply, whatever the source order and whatever media
block either sits in. That argument is what made the deletion safe, and `ui-kit/_unfork.py` is the
argument written down.

**The five exceptions are the interesting part.** `.filter-menu summary`, `.confirm-btn`,
`.field-label`, `.protect` and `.provider-btn` match elements that live OUTSIDE the case: the footer
language menu sits under the device, and a `<dialog>` is appended at the end of the body, so it is a
sibling of `.app-case` and not a descendant. For those five the unprefixed rule is the shipped one and
the `.app-case` twin is what is dead. That was not deduced, it was measured, by running every candidate
through `querySelectorAll` on 77 screens and 45 stands and asking whether any match had no `.app-case`
ancestor. The first cut of the pass did deduce it, deleted the footer menu's padding, and the diff
caught it in one run.

### An attribute is a rule

Gate 9 asked whether a screen carries a `<style>` block or a second stylesheet. Gate 12 asked whether a
raw scale value appears inside `components/*.css`. **A style attribute is neither**, so 110 declarations
lived through two stages in the one place nothing looked: type (`font-size:24px`), geometry
(`width:72px`, next to a `--size-72` that already existed), layout variants, and twelve places where a
component was undone on the element with `border:none` or `position:static`.

Half of them were already dead, which is what happens when nobody looks: the system had grown a rule
saying the same thing. Two more explain an `!important`. `profile.css` and `state-block.css` were
shouting to beat an inline style, and once the attribute went the shout went with it. **An `!important`
in a system is usually a fossil of something that is no longer there**, and it is worth asking what,
before adding another.

Gate 9 reads the attribute now.

### Hidden is not gone

Every painted screen carried the wireframe's own screen-tree drawer: a button, an overlay and a `<nav>`
of about 150 links, hidden by one `display:none` in `base.css`. 1024 KB across 76 screens, **16 per cent
of all the HTML in `ui-visual/`**, and the second navigation on a page that already has its own. And
because a rule that hides something is still a rule about something, `base.css` was carrying 25
declarations to style a drawer it also hid, plus `.device` said four times and `body` three, each
undoing the last.

The record is not lost: `wireframes/` still has all of it, visible, and structure is owned there. Gate
14 is the general form: **a rule nothing on any page can match is a fossil**, the other half of the
orphan-token gate.

### A stacking order is a list, so write it as one

`z-index` was 0 1 2 3 4 5 6 10 40 49 50 60 199 200 201 across twelve files. Three of those did the same
job, five belonged to markup deleted in this pass, and **199 next to 201 is the shape of a number picked
to win an argument rather than to sit in an order**. It is eleven named layers in `tokens.css` now, from
`--z-under` (the thing something else is read against) to `--z-chrome-top`, and gate 12 covers it.

### Two smaller rules, both about where a declaration belongs

**A heading level is structure, and structure is owned by `wireframes/`.** 74 of 77 screens had no
`<h1>`; the outline started at h2, nothing looked broken, and `ia/docs/pages/seo.md` had specified one
H1 per indexed page since stage 03b. The promotion ran over the grey tree first and the colour copy
after, which is the same rule the Profile redesign set.

**A system stylesheet names the font it needs; the document loads it.** `base.css` `@import`ed the
Google Fonts URL that every page already carried a `<link>` to: one dependency declared twice, and the
CSS copy was on the slowest possible path, three hops before the browser could even discover it. It is
also the wrong place for the decision: a third-party font call sends the visitor's IP before consent,
in a product that ships a cookie banner grounded in GDPR and ePrivacy. Self-hosting the three families
is the production answer; until then the call is visible in every head instead of buried in the CSS.

### Markup is not only in .html files

The first cut of gate 14 read `class="..."` out of the HTML and `classList` out of the scripts, and
concluded that `.sidebar-divider` was dead. It is not: the vitrine's own side panel is built at run
time by `_nav.js` out of a template string, so deleting the rule turned every group heading in the
panel into unstyled default text, in both themes, on all 45 stand pages. **A class inside a template
string is markup**, and the gate reads the `.js` files now.

The deeper mistake was in the verification, not the scan. `_verify/snap.cjs` walked `ui-visual/` and
nothing else, so a pass that edits `components/` could prove the product and say nothing at all about
the vitrine that the same file paints. It takes `--kit` now, and the pass was re-run against the tree
as it stood before step 7b, from a git worktree on a second port. That comparison found two more
things the deletion of an `!important` had let go: `kit.html` has `<body class="app-case">`, and
`.app-case` is transparent by design so the device slab shows through, so the body stopped painting
the page; and one section label on the same page took an inline margin the component had been
out-shouting. **An `!important` is a fossil of something that is no longer there, and removing it is
only safe once you have found what it was arguing with.**

### How this pass was verified

The product and the vitrine, both trees, at five widths, before and after, compared by what the
browser reports as VISIBLE (`_verify/visible.cjs`, since markup was added and removed and an
index-aligned diff would read every page as different). **380 product snapshots, 0 with a different
visible element count.** What moved, and nothing else did: every `background-image` URL, same file,
new folder; and two chart polylines caught mid-transition because a duration moved 20ms. In the
vitrine, 175 pages changed their element count, all of them the corrected screen lists and the new
icon section (a component that claimed 76 screens now links the nine it stands on).

Target size was measured rather than reasoned about: coarse pointer at 380px and at 1280px, every
control 44px; fine pointer, 36px, which clears 2.5.8. Then the whole product in both themes at 380
and 1280: **54774 text pairs measured, 0 below AA, 0 page errors, 0 horizontal overflow.**

Two of those numbers were wrong the first time and the reason is worth keeping. A first contrast run
reported 950 failures, every one of them a brass CTA: the checker read `background-color`, a gradient
button has none, so it compared plum ink against the stone three levels up. A second run reported
405, every one of them a theme swap measured 40ms after the attribute changed, mid-transition between
graphite and chalk. **A measurement that has not been checked against a known-good case is a claim,
not a proof.**
## What step 7d settled

A fourth pass, run as a readiness check against the course's own "done when" list rather than as a
hunt for defects, which is why it found a different kind. Eleven findings. Two of my own measurements
were wrong and are recorded here as findings against the method, because a false positive costs the
same attention as a real one.

### A rule with no gate behind it is a preference

`CLAUDE.md` has said since Stage 08 that `wireframes/` owns structure and copy and `ui-visual/` owns
the visual layer. Nothing checked it. Stage 08 then **redesigned the Event Detail while painting it**:
an AMM market panel with a price-by-size table, a chart rebuilt as head / plot / axis / range, a
rules-and-context tab split where the grey tree has two flat sections, a share-and-save cluster, an
odds bar, and a real `<input>` where the grey tree had a `<span>` pretending to be a field. Measured
on `<main>`, 55 of 72 twinned screens differed, Event Detail by 222 elements. The copy inventory in
`voice/docs/microcopy.md`, which is the source of truth for copy, did not carry 43 of the strings the
product had been shipping for a stage.

The structure was ported back by `wireframes/_generators/port_structure.py`, and **gate 18** now
fails the build when the two trees disagree. The four differences that ARE the boundary are declared
in `wireframes/_conventions.md` and the gate is blind to those and nothing else: the plate wrappers,
the icon mechanism, the photograph, and chart data (a wireframe draws its data, a product computes
it).

### Four bugs in the porter, and they are the useful part

The generator was written, run, and wrong four times before it was right. Each one is a rule.

- **Splitting a selector list on commas cuts `:is(h2,h3)` in half.** The generated sheet contained
  `.ed-chart-head :is(h2 { margin: 0; }`, and a browser that cannot parse a rule drops it AND
  everything after it in the same sheet. The visible symptom was a chart axis rendering as running
  text, which looks like a missing rule and is not. Gate 16 exists for this shape one tree over; the
  porter now checks its own output for balance before writing.
- **Deleting `@media` blocks before reading a file deletes the layout.** The hero stacks at 620px and
  that instruction lives nowhere else, so the ported feed came out 14px wider than the phone it was
  drawn for. A breakpoint is layout, and layout is what a wireframe is for.
- **"Already styled" is the wrong question when the markup moved.** The category bar used to hang off
  the device beside `<main>` as `li > button`; the painted tree puts it inside as `li > a > button` in
  a strip that scrolls sideways. The old grey rules still matched something, so nothing looked
  missing.
- **A selector naming a scope the target tree does not have can never match.** Nine ported rules named
  `.feed-inner`, which the port had just unwrapped.

### A photograph travels two ways

`background-image` was stripped and `<img>` was not, so four pictures entered a tree that had zero
image elements across 104 pages, one of them 1400px wide. Both are the picture; only one of them
looks like styling.

### Two findings that were my own measurement error

Recorded, because the correction is worth as much as the finding. A scan for undocumented same-value
token groups reported six; the check was **case-sensitive** and every one of the six is documented,
starting with a capital. A scan for roles without provenance reported two; both sit under a group
comment that covers them. All 31 coincidences and all 133 roles are accounted for. **A checker that
has not been run against a case it should pass is not a checker yet.**

### The vitrine was showing part of one of two icon mechanisms

Step 7c added the inline-drawn icons because the sheet documented only the sprite. It collected them
with a regex wanting `class="ic"` as the **first** attribute, which is a question about how markup
happens to be typed. Fourteen marks were missing, including the chevron, which at 176 uses is the
most drawn icon in the product, and the three sign-in brand marks. The rule is now the question the
section is asking: an `<svg>` on a screen is either a MARK or a drawing of DATA, there are two
drawings, name those and take the rest. **Gate 17** checks the other direction of gate 3: a mark on a
screen that the sheet does not show. One checkmark was drawn two ways for one meaning and is now
drawn one way.

### The stacking order is the one scale that cannot be a bar

Eleven `--z-*` tokens were declared in step 7b and shown on no foundations page. They are now a
section of `tokens.html`, drawn as the stack they are, with the plates written into the page
**highest first**: source order alone would stack them backwards, so the picture is only right while
every token is. A specimen that would still look correct with the tokens removed proves nothing.

### A specimen without its ancestor is not the product's element

The field page listed its states as a table of selectors and rendered none, which is the one
component where reading `opacity: .45` is not seeing it. The states that a state actually IS (an
attribute, a class) now render. The first cut put them on the bare canvas and got four white boxes on
graphite: every rule in `input.css` is scoped under `dialog.app-dialog`. Hover and focus stay in the
table and are not faked with a stand class, because the moment a specimen carries `.is-hover` the
page describes itself instead of the product.

### The roadmap was true in one place and false in twenty-one

`LAYOUT` in `wireframes/_generators/resync_sidebar.py` has had Tokens + Components finished since it
shipped. Twelve root pages render from it. Sixteen annotation pages and five archived concept pages
carry a copy typed into their own generator, and every one still showed a finished stage as planned,
wearing the "Next" badge that belongs to the next thing to build. Fixed by `_resync_roadmap.py`,
which rewrites the three lines that are wrong rather than re-rendering the whole nav, because several
of those pages carry local entries `LAYOUT` knows nothing about and a full re-render would delete
them to win an argument about single-sourcing.

### A fossil is only visible once the thing it was a fossil of is gone

`.chart-wrap` and `.chart-cap` were listed in `coverage.md` as "the grey-era version of a block the
paint replaced" and kept because the grey tree still carried the markup. Porting the rebuild took the
last element either could match, and gate 14 called them within the same run.
## What step 7e settled

Step 7d put a gate behind the rule that `wireframes/` owns structure, and the gate compared `<main>`.
That sentence contains the whole of this pass: **a gate that reads one region of a page certifies one
region of a page.** The header, the bottom nav and the footer were the place two trees could drift
with every gate green, and they had. Ten findings, all closed; two of them were the tools' own.

### The drift ran both ways, so the fix is two tools in a fixed order

The paint got the SHAPE right and the STATE wrong; the grey tree got the state right and the shape
wrong. Reading that as "one tree is behind" is what makes a one-directional port write the wrong
answer into 104 files. So:

> **The paint owns the shape of the chrome. The grey tree owns which state it is in.**

`ui-visual/_reconcile_chrome.py` runs first and gives the paint back three state facts, then
`wireframes/_generators/port_chrome.py` copies the corrected shape back. Run them the other way and
the second tool carries `aria-current="page"` on the Events slot into every wireframe.

What the paint had wrong, all of it from `_apply_family.py` grafting one canonical header onto every
screen: `aria-current="page"` on the Events slot of all 76 painted screens (the grey tree marks 54
Events, 9 My Bets, 3 Favorites, 6 Portfolio, 15 none, which is what a screen reader reads out, so the
painted Wallet screen announced "Events, current page"); a logged-in header over a bottom nav whose
home slot pointed at `event-feed-logged-out.html`, on ten screens, the two halves of one chrome
disagreeing about whether anybody is signed in; and the notifications dropdown listing three unread
items on the three screens whose whole subject is that a new user has nothing yet.

What the grey tree had wrong: no `.cat-condensed` on any page, a whole navigation control (the
category strip that slides into the sticky header once the full bar scrolls away, on 68 painted
screens); the footer trust block as three bare sentences where the product ships a headed block; and
a `<span>` pretending to be the deposit amount field, which is the same defect step 7d found in the
bet panel, one family over.

### An auth variant was not a fact to read, it was a decision to make

Ten screens disagreed about whether they are signed in, and there is no tree to defer to when both
say something and neither is a copy of the other. Each one is answered by a reason, written once:
`how-it-works` and the four `public-profile` screens are logged OUT because CLAUDE.md has said since
Stage 08 that they are reached pre-auth; `cookie-consent` because a consent banner IS a first visit;
`maintenance` because the app server is down and there is no session to read a balance out of; `404`,
`500` and `toasts` are logged IN, because showing a signed-in person Sign in / Sign up turns "this
page is missing" into "you were logged out", which is a worse error than the one they hit.

### A port copies markup, and a href is markup

The two trees do not name the same screen the same way: the category pages are
`event-feed-politics.html` in colour and `politics.html` in grey. Step 7d ported `<main>` and carried
the painted hrefs with it, so **110 links in the grey tree pointed at files that do not exist there**,
and the link check run at the time counted links rather than resolving targets. The map lives in
`port_structure.HREF` and both ports reach for the same one.

### A missing colour is a colour

Two of these, and they are the same shape as the theme finding in step 6b, from the other side: a
checker that reads the source cannot see a value the browser supplies.

- `_conventions.md` opens with "neutral greys only, no color" and every check ever run against it read
  the source: 0 non-neutral hex in 104 files, true, and not the question. The grey sheet styles a link
  in fourteen scoped places and never as a bare element, so every `<a>` outside them rendered in the
  user agent's `#0000EE`. Measured in Chrome: **992 computed colour values** across the tree, on links
  that have been there since the wireframes were built. One rule fixes it, first in the sheet and
  weaker than every scoped rule already there: `a { color: inherit; }`. Colour only, because in a grey
  box an underline is how a link says it is one.
- `fill` and `stroke` are not in the port's `KEEP` list, so every declaration `components/` had for
  the five shapes of the feed hero chart was dropped, and **an SVG with no fill is black**. Since step
  7d the wireframe has been drawing that chart as a solid black rectangle, and nothing could see it:
  the markup is right, the palette scan is right, the page has no error.

### Where a rule may reach, part two

Gate 14 (no selector without markup) was counting `wireframes/*.html` as markup for `components/`.
It cannot be: the grey tree carries its own inline grey-box css and never links `index.css`, so no
rule in `components/` has ever applied to it. Four rules were alive on that mistake, `.backdrop`,
`.sheet` and `.grab` (the grey tree's bottom-sheet frame, where the paint uses a centred
`dialog.app-dialog`) and `.wf-screen > a.planned::after` (the grey screen drawer, 2392 uses there and
none here). **A class carried only by the tree a stylesheet cannot see is a class it does not have.**

### Two findings were the tools' own, and both are the same bug

An idempotent generator has to be idempotent about whitespace. `port_chrome.py` inserted a script
block with its own leading newline and removed it by substituting one, so pages that end
`</script></body>` with no break kept two spaces on the first run and a newline on the second: 74
pages changed on a re-run that should have been a no-op. Widening the removal to `\s*` on the front
then ate a newline the page already had, on the 13 that have one. **The removal has to be the exact
inverse of the insertion, not an approximation of it.** `grey_links.py` made the same mistake an hour
later, which is why it carries a blank-line collapse: a generator has to converge from a tree an
earlier, wrong version of itself already wrote.

The other one is worse and was caught by eye in a screenshot. A painted overlay page carries four
dialogs, the shared sign-in, deposit and how-it-works plus its own, and the shared ones are emitted
first, so "the first `.sheet-body` in the document" is the sign-in provider list on every one of the
17. The port wrote the sign-in buttons into the grey Win, Loss and Deposit wireframes. **A screen's
own overlay has an id**, and the tool now also checks that both trees give the sheet the same
`aria-label` before copying anything, which is the check that would have caught it without a
screenshot.

### Two generators writing into one sheet have to know where each other's work ends

`port_structure.py`'s block regex ran from its marker to `</style>`, which was right while there was
one generator. With two, this file's block came first and the non-greedy run spanned both, so every
re-run of `port_structure.py` silently deleted `port_chrome.py`'s block from 72 pages. The only
symptom was a marker count. Both now use `block_re(marker)`, which stops at `</style>` or at the next
generated marker, whichever comes first.

### What was not fixed, on purpose

The paint made the invoked overlay a centred modal at both breakpoints, so the "bottom sheet on
mobile" half of convention 5 ships only in the grey tree. That is a product decision about how an
overlay presents, not a mechanical difference, and this pass had no mandate to make it. Recorded in
`wireframes/_conventions.md` beside the convention it contradicts.

### Verified

Both trees, 380 and 1280, in Chrome, before and after. Grey: 208 page loads, **0 horizontal
overflow, 0 page errors, 992 computed colour leaks -> 0**. Painted: 308 page loads across both
themes, **61956 text pairs, 0 below AA, 0 overflow**. Links: 16597 internal `.html` links in the grey
tree, **110 broken -> 0**. Gate 18 was tested by injecting drift into each of the five compared
regions in turn and confirming it names the right one. All three ports and both post-processors reach
their fixed point in one run. **Gates: 18.**
## What step 7f settled

Step 7e gave the chrome a gate. This pass answers the question that gate does not ask: **a screen can
disagree with its grey twin, and it can also disagree with its own second copy in the same tree, and
only the first of those was ever checked.** Found by looking at the product rather than at the build:
the sign-in dialog on `ui-visual/sign-in.html` did not look like the sign-in dialog on every other
screen.

### A dialog that also has a page has two copies, and nobody was comparing them

Sign In and Deposit each exist twice per tree: the shared `<dialog>` embedded on all 76 painted
screens, and the standalone page that IS that dialog. Stage 08 painted the shared copy into a real
component and left the standalone on the markup the grey generator wrote. What that looked like: the
shared dialog carries the real Google, X and Apple marks; **the page a person actually opens carried
the wireframe placeholders, and the one standing in for Google is a circle with a plus in it.** Four
copies of the sign-in body existed in the repo (grey shared, grey standalone, painted shared, painted
standalone) and all four differed.

### "The newer copy wins" would have deleted the best thing on the screen

The obvious rule is wrong here, and reading both copies is what shows it. The standalone Deposit had
three things the shared one had lost: a label over the payment widget, the sentence saying card
payments are converted via Transak, and **an exit to How It Works, which is the trust affordance the
deposit screen exists to earn**. A merge decided element by element, then one markup from there.
`ui-visual/_unify_dialogs.py` keeps it; **gate 19** fails the build when it drifts again, in either
tree, and it also checks the marks by name, because `shape()` drops `<path>` and `<circle>` (the icon
mechanism is a declared boundary) and therefore cannot see that a button is drawing the wrong logo.

Three differences are context and are declared in `wireframes/_conventions.md`: the head (h2 and
`data-close-dialog` in a dialog, h1 and a link back on a page), the wiring (a dialog opens the next
sheet over the page you are on, a page navigates, so each control is wrapped in an `<a>`), and the
state screens, which are states and not copies.

### Scope is where a block may stand

The How It Works page rendered as an unstyled document, and the cause was one word in a selector:
every rule for the hero, the glow, the icon chips, the section rhythm and the FAQ list began
`.app-dialog.hiw-dialog`. The page the dialog links to as "the full guide" could not reach a single
one of them. **A rule that describes a BLOCK is written unscoped**; what stays scoped is what is
about being a dialog, its width, its close disc, a sheet's body padding.

The page was then composed rather than re-marked: a page is not a bigger dialog. It has room, so the
sections take the page text size instead of a sheet's 13px, they sit apart instead of stacked in a
scroll, and the two things that are not the guide (the brand tile and the count of resolved events)
moved into a side column, because **a claim and its proof belong beside the argument, not after it**.
One line of copy was written (Step 27 in `microcopy.md`); everything else already shipped, four
sections on the page and the rest in the dialog this page is the full version of. The page also
gained the one thing a page called How It Works owed a reader and did not have: how to place a bet.

Two smaller things fell out of it. The heading `Proven, not promised` had been sitting in a
`<section>` of its own **with nothing in it**, above three numbers in a different element. And
`.app-case .hiw-sec > :is(h2,h3)`, added in step 7c to pin a heading nobody had sized, stopped
matching the moment the heading became `.hiw-label` inside `.hiw-sec-txt`: a fossil created by the
fix for a fossil.

### Already styled is the wrong question when the markup changed shape

`.hiw-sec` used to be a section with a heading and a paragraph in it; it is now a row with an icon
chip beside a text column. The grey tree's old rule still matched, so the port left it alone and
nothing looked missing, and the wireframe drew the chip above the heading in a layout that puts it
beside. It joins `.cat-nav` in `port_structure.RESTYLE`, which is the second time that list has
grown for exactly this reason.

### Two checkers that reported their own defects

Both were mine and both are the same shape as the ones in 7c and 7e. Gate 19's first cut asked for
"the first `<dialog>` in the document" and got the shared sign-in sheet, which every standalone page
embeds before its own, so it reported a fork in Deposit that did not exist. **A page with several of
a thing has to be asked by id.** And `_unify_dialogs.py` had to be told that a button with no mark
keeps none: swapping a placeholder for the real logo ends a fork, but putting a logo on a control
that never had one starts a design decision, and a tool doing that quietly is worse than the drift.

### Verified

Both trees at 380 and 1280. Grey: 208 page loads, 0 overflow, 0 page errors, 0 colour outside the
wireframe palette. Painted: 308 page loads across both themes, 0 below AA, 0 overflow. Links: 0
broken in either tree. Gate 19 was tested by injecting each of its three kinds of drift (a stale mark
on the page, a block dropped from the page, the shared copy edited alone) and confirming it names the
right one. Every tool reaches its fixed point in one run. **Gates: 19.**
## What step 8 settled

Run as a readiness pass, not a defect hunt: three things were open at the end of step 7f (an overlay
that contradicted its own convention, a font host called before consent, and a note that the two
trees disagreed about how many category screens exist), and closing the third one turned out to open
the largest hole this stage has found. **Fifteen findings, all closed.**

### A pair that does not exist is not a pair that agrees

Gate 18 pairs the trees by FILENAME. One family does not share filenames: a category page is
`politics.html` in grey and `event-feed-politics.html` in colour, because the grey tree files it as
a Category screen and the paint as a variant of the Event Feed. Both names are defensible. The
consequence was not: the gate skipped every unpaired page **in silence**, so **32 grey category
screens sat against 4 painted ones** and the family drifted through two stages with every gate
green. Zero drift out of zero pairs reads exactly like zero drift out of all of them.

- The map is now **`_twins.py`** at the root, one copy read by six tools and by the gate. It had
  existed in **five hand-written copies**, and the four that only knew the BASE pages are the reason
  nobody noticed: every one of them could translate `politics.html` and none of them had ever heard
  of `politics-empty.html`.
- **Gate 18 gained a second check**, `every screen has a twin`, with one declared exception
  (`overview.html`, the index OF the painted screens, which is not a screen of the product). The
  coverage is the check; the shape comparison is what it enables.
- The 28 missing screens are built by `ui-visual/_apply_theme.py`, which was the Event Feed's state
  generator with `event-feed.html` hard-coded as its shell. A category page is the same listing with
  one filter on it, so it is the same machine with a different shell, not a second generator.

### An anchor another tool can remove is not an anchor

`_apply_theme.py` built the stone plate by finding `<div class="feed-inner">` in the GREY fragment
and inserting around it. Step 7d then ported this file's own output back into the grey tree, and the
port unwraps plate wrappers on the way (a plate is paint). The anchor stopped matching, the insert
became a silent no-op, and **the next run of that file would have shipped eight state pages with no
plate under them**. The wrapper structure is written out from scratch now, every run, whatever shape
the fragment arrives in.

`_gen_category.py` had the same defect one function away and had already fired: its heading
substitution read `<h2 id="feedHeading">` and step 7b made that heading an `<h1>`, so a single re-run
put the shell's **"Trending"** on all four category pages and left the sub-category rail, which picks
its list by the heading's text, rendering nothing. **A generator whose anchor a later pass has moved
fails silently and passes every gate.**

### A category page owes its own SEO body, not the home page's

`ia/docs/pages/seo.md` section 3B lists five H2s for the category template, and the fourth is
**"About {category} events"**. The four painted pages were derived from the painted feed and
inherited ITS body: the same two generic sections on all five URLs, and the one section that is about
this category missing from the one page that is about this category, while section E of the same spec
is explicit that a category must not duplicate its siblings. The copy is now read out of the grey
twin at generation time rather than typed into the generator, because copy is owned by `wireframes/`
and `voice/` and a generator that types a sentence is a second source for it.

### A listing does not change its contents when nobody is signed in

The logged-out state of a category page was being built from the grey twin, whose card set was drawn
in Stage 05, before a card had a story line or an outcome button that navigates. That put Stage-05
cards on four painted screens: no `.top-txt`, so no story-led "why" the CJM added in Stage 04, and
YES/NO that a logged-out person could not press, **in a product whose whole inversion is that you
browse and build a bet before the gate**. Its logged-out success state is the base page with
logged-out chrome and nothing else now; empty, error and loading still come from grey, because there
the state IS the content.

And **nobody signed in has saved anything**: the card carried a pressed bookmark into every
logged-out listing, five screens in both trees, the brass filled mark that means "this is in your
Favorites", shown to a visitor whose header is offering them Sign up. The attribute is the state, so
it is set rather than styled away.

### A missing colour is a colour, again, and this time on a control

Chasing that markup found the defect under it. Every colour in `yesno.css` hung off `> a`:

    .yesno > a:first-of-type button { color: var(--outcome-yes-text) ... }

so a `.yesno` whose buttons are not wrapped in an anchor got no `color` from anywhere and fell back to
the user agent's `buttontext`. Near black on a graphite card: **1.42:1**. Same shape as the 992
browser-blue links step 7e found in the grey tree, one level down. **A side is a POSITION IN THE
PAIR, not a fact about being wrapped in a link**, and a component has to say what it is whatever
markup it stands in.

### A frame rule reached a dialog

`base.css` has `.app-case{position:relative}`, and the 17 standalone overlay pages put the app frame
class on the `<dialog>` itself. That took back the user agent's `position:fixed` for `dialog:modal`,
so **the sheet scrolled with the page behind it**: on `win.html` at 380 the page sat 412px down and
the sheet's top edge was 313px above the screen. Same category as a text role on a filled glyph or an
emboss shade under a photograph: the class was named for a job it is not doing here.

### The bottom sheet was geometry, not markup

Convention 5 has said since the wireframes were built that an invoked screen is a bottom sheet on
mobile; the paint shipped a centred modal at both widths and step 7e recorded that as a decision left
open. Made: under 640px an invoked dialog is full width on the bottom edge with its top two corners
rounded, rising into place, the head fixed and the body scrolling. Above 640px nothing changed.

- **`:modal`, not `[open]`.** A standalone overlay page opens its dialog as the page it IS, and a
  sheet that rises over nothing is a page that jumps on load. Only a dialog invoked over a screen is
  a sheet. It also keeps layout rules off a closed dialog: the UA closes one with
  `dialog:not([open]){display:none}` and **an author declaration beats a UA one whatever the
  specificity**, so a bare `display:flex` here would have opened every dialog on 76 screens at once.
- **No grab handle.** The grey tree draws one and drag-to-dismiss is not built.

### Where a font comes from is a decision

Every screen carried `<link href="https://fonts.googleapis.com/css2?...">`, so a visitor's IP and
User-Agent reached a third party **before the cookie banner this product ships had asked them
anything**. Step 7b deleted a second copy of that URL out of `base.css` and wrote down that this was
a decision and not a default. It is made: 18 woff2 files (latin and latin-ext, `font-display:swap`)
in `assets/fonts/`, declared once in **`components/fonts.css`**, imported first by `index.css`.
373 KB committed, 0 external requests measured.

**Gate 20 is three checks**, because the defect can come back three ways: a page can re-add the tag,
a GENERATOR can re-add it to every page it writes (five of them had it in a template, and removing it
from 211 documents without removing it from those five would have lasted until the next run), and an
`@font-face` can name a file nobody committed.

### How it was verified, and the checker that had to be corrected first

- **The painted tree**, 105 screens x 2 themes x {380, 1280}: **420 page loads, 86534 text pairs, 0
  below AA, 0 horizontal overflow, 0 page errors.**
- **The grey tree**, 104 screens x {380, 1280}: **0 overflow, 0 page errors, 0 non-neutral text
  colour.** Its 1212 sub-AA pairs are the screen-tree drawer's own notes at 3.33:1 and the identical
  count comes off a worktree of the previous commit, so they are the wireframe's chrome and not this
  pass.
- **Links: 16770 grey and 15535 painted, 0 broken** either side.
- **Gates: 20.**

The first cut of the sweep reported **116 sub-AA pairs and 4690 overflowing elements**, and running
it against three known-good pages returned 0 and 438. The 438 were the notifications dropdown, laid
out where it will appear and never on screen, so the overflow question is asked of the DOCUMENT now
(`scrollWidth > innerWidth`) and every element is filtered through `checkVisibility()`. The 116 were
real, and only the calibration told the two apart. **A measurement not checked against a known-good
case is a claim, not a proof** was written down in step 7c; this is the pass where it paid.

---
## What step 8b settled

Three things, and only one of them was on a list. The documents were: Stage 09 was the one stage
whose reasoning existed as markdown and nothing else. The other two came from looking at the product
instead of at the build, which is now twice in a row that this has found more than an audit did.

### A document nobody can open is not documentation

`ia/docs/sitemap.md` has `ia/sitemap.html`. `voice/docs/voice.md` has `voice/voice.html`. This
stage's four documents, 144 KB of them, had nothing, and the vitrine already linked one: **thirty-nine
component pages pointed at `docs/coverage.md`**, a href into a file the browser downloads instead of
drawing. A dead end with a link on it.

They are pages of the vitrine now (`ui-kit/_gen_docs.py`), painted by the system they describe:
`components/index.css` plus `_page.css`, the kit side panel, the theme switch. That is not decoration.
A long document on the product's own tokens is the cheapest test there is of whether the type ramp and
the two grounds hold up over twelve thousand words, and it found one thing immediately: **a section
label is not a heading.** `.tk-sec > h2` is small brass capitals, which is right over a specimen and
wrong seventeen times down a page, because capitals are read letter by letter.

Generated, not hand-built, for the reason this repo keeps paying for: these documents change every
step, and a hand copy is stale by the next one. **Gate 21** re-renders in memory and compares, because
a file can be newer than its source and still be wrong; it also fails on any link into a raw `.md`.
The renderer reads the subset these four documents use and nothing else, since an implementation
nothing exercises is a guess.

Run order is `_gen_component_pages.py` then `_gen_docs.py`: the first one writes `docs/coverage.md`,
so rendering first renders the previous coverage table.

### A gate that compares the body certifies the body

Step 7f ended the Sign In / Deposit fork and gate 19 has guarded it since, by comparing the sheet
BODY. The fork that was left is on the element the body hangs from. All 17 standalone overlay pages
were written from one template, so all 17 carried `app-case app-dialog outcome-dialog
<family>-dialog`, and `.outcome-dialog` is not a synonym for "an overlay that is its own page". It is
the RESULT skin: `dialog.css` splits the head on it, and `:not(.outcome-dialog)` is the branch that
gets the brass-lit plate. **So the sign-in sheet a person actually opens had the flat result head
while the same sheet on the other 75 screens had the lit one**, and the deposit page had its
`.protect` line and its field labels overridden into muted grey that the shared copy does not
override.

A skin is named for what the sheet IS. sign-in and deposit take the shared dialog's own class list;
win and loss keep `outcome-dialog`, because that is what they are. `app-case` stays on all of them and
is not a skin: a standalone overlay page has no screen behind the sheet, so the sheet IS the app
frame, and `.app-case .protect`, `.app-case .confirm-btn`, `.app-case .provider-btn` reach it only
through that class. The skin is computed from the canonical dialog in `_unify_dialogs.py` rather than
typed, and the family comes from the page NAME rather than from a class the first run removes:
**a rule that can only recognise its own input before it has run once is not idempotent.**

One rule was quietly being paid for by the wrong skin. `.outcome-dialog a{text-decoration:none}` was
suppressing the underline on every provider label, because a standalone page wires a button by
wrapping it in an `<a>`. **A link that wraps a control is not a text link**, and that now says so in
`dialog.css`, once, for both trees.

Measured after: the standalone dialog and the shared one, matched by class rather than by position,
differ on nothing that paints. The one property left is `display: inline-block` against `block`,
which is the `<a>` wrapper making the button not a flex item, and the box is identical to the pixel.

### A modal is bounded by the viewport, so it has to be able to scroll

The user agent gives `dialog:modal` both halves of the answer: `max-height: calc(100% - 38px)` and
`overflow: auto`. `dialog.app-dialog{overflow:clip}` took the second one away. At 1280x620 the deposit
sheet was cut at 582px with its **Add funds** button 116px past the edge and nothing to scroll, and
the how-it-works sheet, 764px tall, was unreachable below 900px of viewport at any width, phone
included.

This is step 7's own finding read backwards. There, `overflow:hidden` was wrong because it made a
decorative box a scroll container. Here `overflow:clip` is wrong because it stops a box that has to be
one. **Both are the same question asked of one property: clip decoration, or contain content.** The
frame goes on clipping its own corners and the BODY scrolls, so the head and the close button stay put
while the content moves; the same rule reaches `.hiw-body` from `hiw-dialog.css` rather than from
`dialog.css`, because a class belongs to the component that owns it and the `Classes:` line is
computed. `.bet-sheet` is excluded and says why: it is a dock with its own geometry.

The bottom-sheet block at 640px keeps only what is about being a sheet, which is where it sits, what
shape it is and how it arrives. Verified as the question a person actually asks: **64 dialog and
viewport combinations, from 1280x900 down to 360x440, last control reachable in all 64.**

### Two more places where a checker read text as markup

Both surfaced the moment the documents rendered, and both are the same shape as "a missing colour is a
colour" from step 7e, in the other direction: a checker that reads the source cannot always tell what
the source IS.

- **A document that quotes markup must not read as markup.** The renderer escaped `<` and `>` and
  left the quote alone, so `<link rel="stylesheet" href="_theme.css">` inside a code block became a
  string that gate 4 read as a path and gate 9 read as a page loading a sheet deleted in step 7.
  Escaping the quote costs nothing on screen and ends both.
- **Text inside `<code>` or `<pre>` is a quotation, not a reference.** Gate 4 also scans `url()`, and
  a document that quotes a css declaration has one. It strips the quoted text first now, which the
  component pages needed too: each of them ends with its own source.
- **A mention is not a call.** Gate 20 searched the whole text for a font host, so the page that
  explains why the host was dropped failed the gate that exists because of it. The question is whether
  a URL is REQUESTED, so it is asked of a `src`/`href` attribute and an `@import`.

And one page existed that should not: `ui-kit/fonts.html`. Step 8 added `components/fonts.css` and
gate 2 was told that fonts, like `index` and `tokens`, is not a component with a stand; the page
generator was not, so the next run built one. Its own quoted css names a font host, which is how it
was found.

### A colour follows the surface it stands on, not the page

Found by the sweep once the documents gave it four more pages to walk. The course sidebar keeps ONE
dark palette in both grounds (`--chrome-*`, deliberately outside the theme block), and
`.ck-note-link` inside it was reading `--text-brass`, which in daylight becomes the dark brass meant
for a pale surface. Dark brass on the dark panel: **2.39:1, in the light theme, on every page of the
vitrine**, 43 of them before these four. It is the veil lesson from step 6b one level down, and the
fix is one role: `--chrome-accent`. The vitrine's sub-AA pairs went 434 to 158, and what is left is
`kit.html` (frozen provenance) and the value labels drawn ON their own swatches in `tokens.html`,
where the label IS the colour being shown.

### One measure for the page, and an inset that survives it

Reported by eye at a wide window: the content ran edge to edge while the footer under it stopped at
1400. Measured at 1920, the content was 1620 and the footer 1400, so a page had two measures and the
token that names the wider one, `--container-max`, was obeyed by the footer alone. Five of the six
bands carried `max-width:none` from the colour pass. They read the token now, so the band still spans
the window and what is INSIDE it (header row, category strip, trust bar, content, footer) shares one
left edge: 370..1770 at 1920, all four.

The first cut of that fix broke the other direction. Centring the content band by turning
`margin:var(--gutter)` into `margin:var(--gutter) auto` spent the horizontal gutter on the centring,
so under 1400 the plate sat against the window edge. **A container holds its inset at every width**:
the inset is padding, and above the cap the auto margin does the centring. Measured at eight widths
from 1920 to 380, the header row, the content, the plate and the footer start on the same x at every
one of them, and the gutter drops from 40 to 14 below 640 exactly where the token says. The footer's
own inset moved from 20 to the gutter for the same reason: its first column had been sitting 20px
left of the first card.

### An empty box is invisible to every sweep we run

The four category pages and two feed states had a 56px photograph box with no photograph. Until step
7c the picture came from `components/` as `.grid > .card:nth-of-type(N) .thumb`, which decided a
card's photograph by its POSITION in a grid; that step moved it onto the element, where it belongs,
and reached the pages that exist as files. These cards are written by a generator, so they lost the
picture and kept the box, and **a missing picture passes a contrast sweep, an overflow sweep and a
link check alike**. Gate 9 asks for it now, beside the rule that says the element is where a
photograph may live.

The sample library has one photograph per category, so on a page whose six events are all Politics
there is one Politics photograph to draw them with. What varies is the CROP: the thumbnail is a 56px
strip masked to transparent at 52 per cent, so a different slice of a 1600px photograph reads as a
different picture while staying a true picture of the same subject. A state page grafts its `<main>`
from the grey twin, which by the layer boundary has no picture at all, so it takes the photographs
its own shell carries: the same twelve events, the same twelve pictures.

**A photograph is not one declaration.** The port strips it on the way into grey and stripped
`background-image` only, so the crop crossed the boundary without the picture: the framing of
something that is not there, on 24 cards. The whole `background-*` family goes now.

### A control is named by what it does

The Event Feed carried two controls that looked different and did the same thing. The band at the top
navigates, which is right: a category is its own indexed URL with its own H1 and its own SEO body. The
chip row under the Trending heading is labelled "Filter events by category" and was five more links to
the same four pages, so **pressing Politics inside Trending left Trending**. It filters now: the twelve
events stay and the other categories are hidden. Buttons rather than links, `aria-pressed` for which is
on, and `data-cat` on each card read out of the photograph it already carries, because a second
hand-typed mapping of the same fact is a fork. Both trees, one script, in
`wireframes/_generators/subfilter.py`.

Three things it taught, all of them shapes this repo has met before:

- **Hidden is a state, not a style.** The filter set the attribute and nothing moved: the user agent
  hides with `display:none` from ITS sheet, and `.card{display:flex}` beats that whatever the
  specificity. Raising the specificity would only move the argument to the next component that
  declares a display. `[hidden]{display:none!important}` in `base.css` is the one place in
  `components/` that carries the word, and it is the case the word is for, an invariant of the frame
  rather than a preference between rules.
- **A checker that reads the attribute does not read the page.** The first run reported the filter
  working, counting `:not([hidden])`, while twelve cards were on screen. Counting what the browser
  reports as visible found it in one run.
- **Two generators writing into one sheet have to know where each other's work ends**, which step 7e
  wrote down and this pass paid for again: `port_chrome.py` owns everything from its marker to
  `</style>` and rewrites that whole span, so a rule appended before `</style>` landed in its
  territory. The two rewrote the page back and forth forever. The rule goes above the marker now.
- Also: `_gen_category.py` recognised the sub-filter by `</nav>` and drops it from the four category
  pages, so the day it stopped being a `<nav>` it would have left a Trending filter on every category
  page. **A generator that recognises its input by a tag name breaks when the tag changes for a good
  reason.**

### Half of twelve is six

The two bars of the close X are 12px wide and sat at `calc(50% - 7px)`, one pixel left of the disc,
on every close button in the product. The vertical half was right, which is what made it hard to
see: a mark centred in one axis and not the other reads as slightly wrong rather than as misplaced.

### Verified

- **Dialogs**: 8 sheets x 8 viewports, **64 of 64 with the last control reachable**, scrolling
  whatever scrolls. The three elements still reporting a clipped overflow are `.sheet-head`,
  `.hiw-hero` and the win head, each clipping a decorative pseudo 33px taller than its box, which is
  the case `overflow:clip` was chosen for.
- **The two copies**: standalone against shared, matched by class, **0 painting differences**.
- **Gates: 21.** 19 and 21 were both tested by injecting the drift they exist to catch.
## What step 9 settled

The pass began as a question about looks: why do the two side panels look and behave differently.
They are painted by one file, `components/course-chrome.css`, and share every class name, so the
answer was not in the stylesheet. It was that the two trees used one vocabulary for two different
things, and behind that sat a panel that had been lying on forty screens with every gate green.

### A gate that masks a region cannot see into it

Gate 1 masks the `<aside>` when it asks whether a painted screen moved, on the argument that the
panel is chrome and not the screen. That argument is right and it made the panel the one thing
nothing read. Forty screens marked the wrong page as "you are here": every category page and every
feed state said `Event Feed -> success`, which is a different file.

The cause is a shape this repo keeps meeting. `_apply_theme.py` and `_gen_category.py` build a
screen by starting from the finished Event Feed and swapping the regions that differ, and the panel
is not one of those regions, so a new screen arrives carrying **the shell's idea of where it is**.
Correct until nobody re-runs `_resync_sidebar.py`, and after step 8 nobody did. **Gate 22** is four
checks: every screen marks its own file, every panel is what its generator would write today (a
re-render in memory, the way gate 21 reads a document), every stand page names itself against the
registry, and a page off the tree is still linked from the note.

### The thing that navigates was drawn quieter than the thing that does not

In the screens tree a family name was a `.sidebar-page-link` with no href: 13px, full chrome text,
hover highlight, pointer cursor, and no destination, fourteen of them on each of 105 screens. The
screen it named was a `.sidebar-sub-link`: 12px, muted, indented. In the vitrine the same two
classes mean the opposite, because there a `.sidebar-page-link` IS a page and a `.sidebar-sub-link`
is a section inside one.

One vocabulary now, and it is written as a rule rather than as two coincidences. A **label** names a
run of rows and opens nothing (`.sidebar-divider`, `.sub` when nested; `.sidebar-sub-head` is
deleted, and it had been drawn HEAVIER than the label above it, so depth read backwards). A **row**
that opens a page is a link. The page you are **on** is `.active` at whichever level it sits, in one
colour rather than brass in one panel and grey-plus-a-dot in the other. The group you are **in** is
`.active` on its label, which the vitrine did not have at all: 45 rows in a panel showing 25 means
the brass row is usually below the fold.

### Quiet is a colour, not an opacity

Both labels, the note, and a planned stage were dimmed with `opacity`, and opacity fades the text
into its background. `--chrome-muted` is 5.03:1 on the panel; the same value at `opacity:.55` is
**2.37:1**. Five places were under AA and had been for as long as the panel has existed.

No contrast sweep this repo has run could see it, because they all read
`getComputedStyle().color`, **which does not carry opacity**. It is the step-6b lesson one level
deeper: there a checker that read the source could not see a value the browser supplied, here a
checker that reads the computed colour still is not reading the rendered one. Depth is a colour role
now, so the value being chosen is the value being checked.

### One behaviour, two machines, one string

Marking the row and never showing it is most of the way to not marking it: the screens tree is
4066px in a 900px panel, so on `toasts.html` the brass row sat 3813px down. Both panels reveal it on
load now, from one string in `ui-visual/_panel_reveal.py`, emitted as a `<script>` inside the
`<aside>` for the tree that is markup and as a function in `_nav.js` for the tree that is rendered.

`scrollTop`, not `scrollIntoView`: the panel is `position:fixed`, and asking an element inside a
fixed box to scroll itself into view lets the browser scroll **the page** to satisfy the request.
Measured across 153 panels at two viewport heights: 0 documents moved. It is also instant, so there
is no animation to exempt under `prefers-reduced-motion`. The script sits inside the `<aside>`
because that is the span gate 1 masks, so a panel can gain behaviour without 105 screens reading as
product changes.

### One component, seven descriptions

The 28 course pages (`research/`, `user-research/`, `ia/`, `ia/annotations/`, `voice/`, `concept/`)
never linked the system file. Each carried 41 to 43 rules of its own, in **five distinct copies**,
and `_unify_sidebar.py` injected a sixth block on top to force a dark violet palette. So the panel a
person reads the research beside was a different panel from the one in the product, drawn by rules
the design system cannot see. That is also why the four `.planned` rules in `course-chrome.css` had
no markup in any tree the file reaches: the only panel with a planned row is the one it did not
paint.

`_course_chrome.py` deletes the copies and the override, renames the drawer to the system's classes
(the script that opens it addresses the three elements by id, so only the paint moves), and links
`fonts.css`, `tokens.css` and `course-chrome.css` last in `<head>`. `_unify_sidebar.py` is deleted.

Two things had to be checked rather than assumed. **Linking tokens cannot repaint their content**:
the course pages declare fourteen variables and `tokens.css` declares 348, and the two sets do not
intersect at all. **The z ladder had to move together**: their drawer was 199 / 200 / 201 and the
system's is 8 / 9 / 10, so deleting the page's `z-index` without moving its scrim and toggle onto the
same ladder would have opened the panel behind its own scrim.

`.sidebar` also names its own font now. On a painted screen it inherited the product's body font; on
a course page it would have inherited Inter. **A component that changes with the page it stands on
is not a component.**

### A comment is not a rule, and a quotation is not an element

Writing those comments broke the vitrine's own coverage table, which is how the last two defects
surfaced. `parse_component` cut only the header comment, so every later comment was scanned as css:
the deletion-candidate list held `.css` and `.color`, harvested out of the words
"components/index.css" and "Colour goes through a role", and `.ck-note-link` and `.sidebar-sub-head`
came back into it in the same pass that removed them, listed as candidates for a deletion already
done. And the "used by the kit" bucket looked at the specimens, `kit.html` and `shell.html` but not
at the 46 stand pages, so a class carried only by the vitrine's own chrome fell through every bucket.
Reading those pages means skipping `<pre>` and `<code>`, because a stand page ends with the
component's own css. **Deletion candidates: 28 to 2**, and step 7 acted on that list.

### Also settled

- A link in the panel's note is the panel's own, so `.ck-note-link` moved out of `ui-kit/_page.css`
  into `.sidebar-note a`. It had been rendering in the browser's blue everywhere the vitrine's
  stylesheet is not loaded, which is every specimen of the component and all 105 painted screens.
- A planned stage is a `<span>`. An `<a>` with no href is a link element with nothing to open, and
  the badge already says Soon.
- The tree is a named `<nav>` in all three panels. One of them was a `<div>`, so it was a stack of
  links rather than a landmark, on a screen that carries two other navigations.
- The vitrine's back arrow leaves for the painted screens and nothing led the other way, so the
  note's mention of ui-kit is a link. No new copy was written.
- `wireframes/_generators/resync_sidebar.py` stops writing panel css. It used to insert the `.next`
  badge rule into the page's own stylesheet, reading `var(--accent)`, which on a course page is that
  page's violet. Two generators writing into one sheet is the shape this repo has now paid for three
  times.
- `mark_group` lives in one file and is imported by the other, because for one turn the two tools
  each had their own idea of the mark and undid each other for ever.

### Verified

- **The panel, both trees, both themes**: 154 pages x 2 = 308 loads, **18028 text pairs, 0 below AA**
  with opacity composited, 0 browser-blue links, 0 leftover `.sidebar-sub-head`, 0 overflow, 0 page
  errors. The sweep was calibrated first on a pair whose answer is known, white on black at 21.00 and
  the same at `opacity:.2` at 1.66, before any of its numbers were believed.
- **The reveal**: 153 panels at 900 and at 620 tall, **0 with the mark out of view**, 0 where the
  document scrolled; at 380 the drawer is right closed and open.
- **The course pages**: 28 pages, 795 text pairs, 0 below AA, **0 dead anchors, 0 violet left**, one
  shape on all 28.
- **Their content did not move**: every visible element outside the panel compared against a
  worktree of HEAD, tag, position, size, colour and font. **28 of 28 identical.**
- **Links**: 348 pages, **35773 internal links, 0 broken**.
- Gate 1 reports "105 ui-visual pages, screens identical" throughout, and gate 22 was tested by
  injecting each of the four kinds of drift it exists to catch. All six generators reach a fixed
  point together over three rounds. **Gates: 22.**

### One checker's own defect, recorded

The light-theme sweep reported 105 failures at 1.12:1 and they were the `<script>` the reveal added
inside the `<aside>`: the checker counted a script's source as text. In the dark theme a script
inherits light ink on the dark panel and passes; the moment the ground inverts it reads dark on dark.
**A checker with a missing guard fails in one theme and looks exactly like a finding.**

---

## 2026-08-03 - The correction this file cannot make by editing

**This section exists because nothing above it may be changed.** The rule at the top of this file is
that an entry is true as of its own date and is never edited afterwards, so a measurement recorded
here that turns out to have been WRONG stays readable forever. The only correction available is a
later entry that names the earlier lines. This is it.

### The lines

Six Verified blocks above record a contrast result that was not true when it was printed:

| line | what it says |
|---|---|
| L192 | "54774 text pairs measured, **0 below AA**, 0 page errors, 0 horizontal overflow" |
| L414 | "Painted: 308 page loads across both themes, 61956 text pairs, **0 below AA**, 0 overflow" |
| L493 | "Painted: 308 page loads across both themes, **0 below AA**, 0 overflow" |
| L615 | "... **0 below AA**, 0 horizontal overflow, 0 page errors" |
| L946 | "The panel, both trees, both themes: 154 pages x 2 = 308 loads, 18028 text pairs, **0 below AA**" |
| L952 | "The course pages: 28 pages, 795 text pairs, **0 below AA**" |

**What is true instead.** `ui-kit/docs/backlog.md` **S14**, re-measured 2026-08-03: **378 elements
below 4.5:1**, in three equal groups of 126 - `span.l-no` at 4.35:1 on graphite, `span.l-no` at
3.76:1 in daylight, and `span.l-yes` at **2.62:1** in daylight. Twelve screens, both widths,
`components/oddsbar.css:14`. S14 states the part that makes this a correction and not a regression:
**"Pre-existing: measured identical at HEAD before this pass and after it."** The 378 were on the
screens on every one of the dates above.

The same claim stands in two more documents and is corrected here for all three: `docs/decisions.md`
carries it eight times and `voice/docs/microcopy.md` once. **Fifteen printings of one zero.**

### Why it survived fifteen printings, which is the part worth keeping

Nobody lied and nobody was careless. The zero came out of an instrument carrying three defects this
repo had already found and written down: a regex that read the components of `color-mix(in oklab,
...)` as sRGB bytes, so a brass-tinted ground measured as near black; a print limit that stopped at
six findings per render, which **32 of 48 renders hit exactly**, so the number a person read was the
cap; and `mix-blend-mode`, which no computed style can resolve at all.

Each of those was found the same way: it reported something wrong, somebody went to look, and the
instrument was caught. **That is the asymmetry.**

> **A broken instrument that reports a DEFECT gets caught, because somebody goes to look and finds
> the instrument lying. A broken instrument that reports ALL CLEAR is caught by nobody, because
> there is nothing to go and look at. The most dangerous output of a broken check is not a false
> alarm, it is a clean bill of health.**

It is a rule about where verification effort belongs, not an episode about one sweep. A check that
has never failed is not a check that has proved anything; it is a check nobody has had a reason to
audit. The practical form of it in this repo is the control every declared list carries: an entry
that covers nothing fails as loudly as an undeclared item, so a list cannot go quiet by being empty.
Gates 24, 25, 30, 31 and 32 all carry that control, and they carry it for this reason.

### What the sweep found beyond the contrast claims

79 claims of the "nothing was found" form across the repo's markdown, sorted by what stands behind
each of them today:

- **29 are gated**, so they are still true by construction rather than by memory: 0 em dash is gate
  7, 0 broken internal links is gates 4, 8 and 21, "all gates pass" is the build itself.
- **18 are about contrast**, which is the class corrected above.
- **30 were measured by a browser and are gated by nothing**: true as of the run that printed them,
  and unknown today. They are `ui-kit/docs/defects.md` rows 24 to 30, and what they owe is a re-run
  and a date, not a search.
