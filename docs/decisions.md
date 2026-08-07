# Decisions

What was done, why it was done that way, what was rejected and on what grounds.
Entries carry a date, newest first.

**This file is not loaded into a session.** `CLAUDE.md` holds the rules that must act next
time; this holds the record of how they were arrived at. An entry is written once and is
not edited afterwards: a later entry supersedes an earlier one rather than rewriting it,
so a claim here is true as of its own date and nowhere else.

Open items are not here either. They are in [`backlog.md`](./backlog.md).

## The stage numbers in this file are the old ones

The project used to count thirteen stages and ran one number ahead of the course from Information
Architecture onward. It was renumbered to twelve on 2026-08-02, and the entries below were
deliberately **not** rewritten: an entry is true as of its own date, and renumbering it would make
it disagree with the commit message it describes. Read them through this key.

| Written here | Means, in course numbering | Stage |
|---|---|---|
| Stage 01 | 01 | Foundation Research |
| Stage 02 | 02 | User Research |
| Stage 03 | 02+ | CJM, inside User Research |
| Stage 04 | 03a / 03b | Information Architecture |
| Stage 05 | 04 | Wireframes |
| Stage 06 | 05 | Voice |
| Stage 07 | 06 | Concept |
| Stage 08 | 07 | UI + Visual |
| Stage 09 | 08 | Tokens + Components |
| Stage 10 | 09 | Design System |
| Stage 11 | 10 | Responsive |
| Stage 12 | 11 | Animation |
| Stage 13 | 12 | Handoff |

01 and 02 did not move, so a number below 03 means the same thing either way. Everything from
Information Architecture on is one higher than the course. References that point FORWARD, at work
not yet done, were renumbered wherever they live, because those are the ones a reader acts on:
`README.md`, `STRUCTURE.md`, `CLAUDE.md`, `backlog.md` and the two documents in `ui-kit/docs/`.

Per-stage detail lives with its stage: `docs/kit-archive/docs/architecture.md` (the full Stage-09
record, moved there on 2026-08-07), `wireframes/_critique.md` (the wireframe defect tables),
`voice/docs/microcopy.md` (the copy rewrite log).

---

## 2026-08-07 - The instrument was deleted, and the product was not touched

**What was deleted.** `ui-kit/` in full: 65 generated pages, 18 Python scripts, 9 browser scripts,
41 build gates in 109 checks, a state-capture instrument, 288 tracked files and 145 MB of
screenshots. With it, `wireframes/_generators/` (36 scripts), `ui-visual/*.py` (18), five scripts at
the repository root and four elsewhere. **The repository now contains zero Python** outside
`figmosha2/`, which is a Figma bridge and has nothing to do with the design system.

**What was not touched.** `components/` (51 stylesheets, 5,651 lines), `ui-visual/` (106 painted
screens), `wireframes/` (104 grey screens), `ia/`, `voice/`, `research/`, `concept/`, `DESIGN.md`,
`PRODUCT.md`. Not one pixel of the product moved, because the product reads
`components/index.css` and nothing in that path was edited. The single reference the screens had
into the deleted tree was one sidebar line per file pointing at `ui-kit/overview.html`, and that
page still exists.

**Why.** The measurement had become a machine. A one-line change to a stylesheet cost a
regeneration of 42 pages, a re-capture of the state readings in a browser, 41 gates, 525 snapshots
and an audit run: minutes of compute and an hour of care, for an edit that moved one value. Seven
days of work in the last stage produced 14 closed backlog rows and an atom-map distance of 0, and
every one of those closes was real - and the same seven days produced no new screen, no new
component and no answer to the product's own open questions. **An instrument that costs more than
what it measures is not rigour, it is overhead wearing rigour's clothes.**

**What the comparison said.** `Stack sportpit`, the same author's project one stage behind, holds
71 components in 5,349 lines of CSS and 35 hand-written kit pages, with **zero scripts and zero
gates**. Project One held 51 components in 5,651 lines - the same system, to within five per cent -
behind 63 scripts and 41 gates. The census in that project is a one-off report in `census.md` and
`consolidation.md`: walked once, written down, decided, done. Here the same census became a
permanent check that every later edit re-paid.

**What was kept, and where.** `docs/kit-archive/` holds the eight documents and the 48 authored
component pages, read by nothing. The four things worth taking forward are named in its README: the
level formula, the S34 size measurement (9,648 readings, 66 distinct faces of one control kind), the
rule and anti-rule per component, and the defect log. **What was rejected** is keeping any of it
running: a gate that is kept "just in case" is the whole cost with none of the decision.

**What replaces it**, in order: a census of five anchor screens with their states, read in a browser
at two widths in both themes; atomic levels declared once in an inventory; one consolidation pass
where a value is allowed to change and every change is measured; one hand-written page per component
carrying its states in both themes; one audit run as a report. The five anchors are event feed,
event detail, active bets, deposit and sign in, with their loading, empty, error and logged-out
variants: 41 screens of the 106.

**And `CLAUDE.md` inverted its own rule.** It used to say a rule may leave that file once a gate
holds it. With no gates, nothing holds anything except reading, so every rule in it now carries the
reason it exists rather than the number of the check that enforced it.

---

## 2026-08-04 - How much the instrument was missing, measured, and why the merge comes after the shot

**S27 closed, and the useful number is not the one it opened on.** It opened at 64 duplicate
pictures across five components. That was an arithmetic assumption, not a count: it multiplied the
redundant groups by 8, and three of them do not hold 8 pictures. A `card` group holds 6, because a
card is not focusable; a `tabs` group holds 4, because a hidden radio raises no hover and no press.
**The real upper bound was 56**, and the pair list was right in every case. The correction was
reported before anything was deleted, which is the only reason it mattered: the number was in four
documents and none of them was load-bearing, but a count nobody re-derives is how the false zero got
printed fifteen times.

**The result per component, because the verdict is the deliverable and not the total.** `card`:
two pairs, both duplicates, 12 pictures. `hero`: one pair, duplicate, 8. `event-detail`: one pair,
duplicate, 8. `header`: one group of four, duplicate, 24. `tabs`: **nothing merged**, and the pair
became a defect instead. **44 of the 56 were duplicates, 4 were a defect, and 8 were a real
difference the old instrument could not see.** System 766 pictures to 714, 94 groups over 24
components, `NOT_RECAPTURED` empty, gate 36 now unconditional.

**HOW MUCH THE OLD FACE WAS MISSING, which is the measurement worth keeping.** A face was five
values and it is nine now. What the five could not see, found by re-capturing:

- **`card`'s entire hover.** `.card:hover` is `translateY(-3px)` plus a shadow, and neither
  `transform` nor `box-shadow` was among the five, so the recorded value under the hover picture was
  **the same string** as the value under the rest picture. The pictures were right; the number
  printed under them, which is the thing that makes a picture checkable rather than decorative, said
  nothing had moved. On a component that stands on every browse screen.
- **`header`'s `.bal-add`.** It merged into the group of four under the old reading and does not
  under the new one: the plus that opens Add funds gives a different answer from the three ghost
  circles beside it. **8 pictures that would have been deleted as duplicates are evidence.**
- **`tabs`'s two hidden radios.** They differ by `opacity`, 1 against 0, which the old five could
  not see either.

That is the answer to "how much was the instrument missing": one component's whole interaction
layer, one real difference that a merge would have destroyed, and one defect that could not have
been found at all.

**AND THIS IS WHY THE MERGE HAPPENS AFTER THE SHOT AND NEVER IN THE KEY.** The cheap implementation
is to drop the element selector out of the grouping key, which is decided at rest, before a pointer
has touched anything. `card` is the proof that it is wrong: at rest a loaded card and a skeleton
card and, under the old face, a hovered card are all one string. Key on rest and one of a pair is
never photographed, so the difference is not merged away, **it is never measured**, and the page
then shows a single gallery with nothing to say it is missing anything. Everything is shot, and only
then does what agrees in all four states in both themes become one picture. It costs pictures that
are immediately deleted and it is the only order that can be checked afterwards.

**`tabs` is the pass's third verdict, and the pass is worth more for having one.** Its pair is not a
duplicate and not a real difference: `components/tabs.css` hides a CSS-only tab's radio twice,
differently. Line 12 parks `.ed-tabradio` at `left:-9999px`, measured as a 13x13 box at x = -9941;
line 18 gives `.ptab-in` a 1x1 box at `opacity:0`. The file's own comment says the first painted the
focus indicator off the left edge of the document, and that the second was written so the ring lands
in the right place and is then painted at zero alpha, "which is the same nothing". **The second
mechanism exists because the first one failed, and the first one is still there.** Nothing merged,
the pictures stay, and it is `ui-kit/docs/defects.md` row 48 with a closing condition written as
something a check could ask: one hiding idiom per repository, declared once, and any second one
fails.

**The warning about `header` was checked directly and the answer was the opposite.** A group of
four, three of them a button holding one mark and the fourth a `<summary>` holding a wrapper with a
mark AND a count badge, which is an extra zone and a different element. It merged anyway, and the
evidence is in the stylesheet rather than in a reading: `components/header.css` gathers `.icon-btn`,
`.notif-menu summary` and `.avatar-menu summary` into one rest declaration, one hover and one press,
after measuring the shape across all 105 screens at 360 and 1440. What differs is the ELEMENT,
because a summary opens a dropdown and a button does not. The same comment records that the
logged-in against logged-out reading was investigated from a screenshot and rejected. The badge is
content inside the circle, carries no state rule of its own, and is live on the page in the
logged-in specimen.

**Nothing was merged without asking what evidence it deletes**, and in three cases the answer was
the same: the thing that would be lost is live on a page. The skeleton card's own look is
`skeleton.html` with `skeleton-grid` in a frame; the bell with its badge is `header.html` with
`header-in` in a frame; `.hh-name`'s size is `hero.html`. Where the answer would have been "nothing
shows this", the pair stays.

**One finding that was not a merge at all.** `event-detail`'s two groups were split by `.ed-act`, a
class written 27 times in each tree and read by **no stylesheet and no script**: the rule that paints
the row is `.ed-actions button`, which matches with the class and without it. So the two faces were
identical by construction and dead markup was the only thing telling them apart. `ui-kit/docs/backlog.md`
S28. Checked and deliberately not filed with it: `.prov-google` is read by no rule either and
correctly so, because that mark carries its own brand colours while `.prov-x` and `.prov-apple` are
filled with the current colour and need one.

**Browser, 360 and 1440, both themes, over the five touched pages: 0 findings after one repair.**
20 combinations, every state picture forced eager and waited for, 188 pictures loaded, 0 broken, 0
console errors, every live specimen driven with a real pointer. The repair is its own commit and was
not this pass's doing: `tabs.html` pushed the document 22px sideways at 360, and measuring the rest
of the vitrine found feed +46 and footer +27 with the same cause, a path or a selector inside prose
with nothing in it to break at. One element rule, three selectors after the two that matched nothing
were removed, `pre` deliberately excluded. **4 of 56 stand pages overflowed at 360, now 1**, and the
one left is a different cause with a number and a closing condition rather than a guess: S29.

**One false negative caught in the instrument rather than reported as a defect.** The first browser
pass said `tabs.html`'s live specimens do not answer a pointer. They do: the script had hovered the
tab that was already current, whose ink is already at the strong value. Driven on a non-current tab,
both specimens move from `rgb(164, 157, 143)` to `rgb(237, 231, 218)`. A clean result about the
wrong object is the shape this repository keeps finding, and it is worth noting that this time it
was found in the checking script within the same hour rather than in a document fifteen printings
later.

## 2026-08-04 - The unit of a picture is a difference, not an occurrence

**What was on the page.** `ui-kit/button.html` carried **eight state galleries** for a component
that makes **five decisions**. The three extra were `.state-btn` beside `.auth-btn`,
`.state-btn.primary` beside `.auth-btn.primary`, and the second child of `.cta-bar`, and the
authored source names all three as the same answer in its own prose: "Identical answers, which is
the point", "Same three-step", "the answer is the family's". **24 of that component's 64 pictures
existed to show that two things look the same.** Every gate was green.

**Why a page like that gets worse as the product grows, which is the actual reason to fix it.** A
gallery per PLACE tracks the markup: add a sixth place for the same control and the page grows a
sixth gallery and says nothing new. A gallery per DIFFERENCE tracks the system: add a sixth place
and the page does not move, because no decision was taken. The same inversion runs through the whole
page, which is why the axis matrix was rebuilt at the same time and in the same direction: **the
page specifies the axes and the five names are a column**, not five sections.

**THE MECHANISM, and it is the part worth carrying forward.** The capture keyed a group on
`element selector | rest face`, so the class name was part of the identity and one control under two
names was two groups by construction. The selector is out of the key now. The merge deliberately
happens AFTER the shooting rather than before it, and that is not an implementation detail: a
difference is free to live in any of the four states, so keying at rest means one of a pair is never
shot at all. That does not merge a difference away, it stops it being measured.

**And the instrument could not see the difference it was being asked about.** A face was five
values. The two things that make this family's members differ are a one-pixel lift and a glow -
`transform` and `box-shadow` - and neither was among the five. So `.provider-btn` read as identical
to `.auth-btn` while both `components/button.css` and the authored page said it is not, and a merge
on that reading would have deleted the picture of a real difference. **The list was also written in
three places** (twice in `browser.cjs`, once in `states.cjs`) and had already drifted by a property.
It is one function now, in `browser.cjs`, and it carries transform, box-shadow and opacity. Size
stays out on purpose: a different padding is the same face at a different size. This is the fourth
time this run that the finding was "the check was clean about something it never looked at".

**Result, measured.** button: **8 groups to 5, 64 pictures to 40, 24 deleted**, which is exactly the
three groups the source itself called identical. The system: **792 pictures to 766**, the other two
being `tabs` focus pictures that belonged to no group at all and had been sitting in the tree behind
a check that only ever asked whether a NAMED file was still there. The five that remain are one base
set plus one named difference each: the modifier, the one-pixel lift, the missing edge, and the dark
ink on the first child of an action bar.

**Gate 36, proved in three directions.** Forward: putting one occurrence back as its own group turns
it red, and gate 32 goes red beside it, which is the pair working as intended - 32 asks whether every
group is described, 36 asks whether the group should exist. Backward: a declared not-re-captured
entry that holds no duplicate fails as idle, and a picture copied into the tree with nothing pointing
at it fails as an orphan. **Five components still hold the same defect** - `card`, `header`,
`event-detail`, `hero`, `tabs`, 64 pictures - and they are declared rather than fixed, because they
were shot under the old five-value face and their count is an upper bound that only a re-capture can
settle. `ui-kit/docs/backlog.md` **S27**, and the list clears itself.

**The size axis has no rule, and the page says so in those words.** This is the one place the work
was asked to derive a rule from the product and the product refused. Measured in Chrome at 1440 and
360: container height does not predict the font step (the state block is 245 tall and takes the
smallest, the action bar is 70 and takes the middle one), and the share of the container looks
monotone until two placements break it in both directions - `.resolved-panel .state-btn` is full
width at 12 and `.bet-dock .confirm-btn` is fit width at 14. **The step follows the NAME.** Worse,
one class carries two steps: `.provider-btn` is 13 in its own rule and **14 inside the sign-in and
outcome sheets, which is 322 of its 444 uses**, so the size a person meets is not the size the
stylesheet declares first. The page prints "a fact without a rule" rather than a plausible sentence,
because an invented rule is worse than a missing one: a missing rule sends the next person to look,
an invented one sends them away satisfied. `ui-kit/docs/backlog.md` **S25**.

**The other three axes do have rules, and each was tested rather than asserted.** WIDTH: full when
the control owns its row, shared when the row is split evenly, fit otherwise - **0 exceptions in 710
placements**, and the two that look like exceptions are the rule being applied by the container.
EMPHASIS: one brass action per zone - **zones carrying more than one, 0**, counted over every dialog
and action bar in the painted tree. ICON, which is the fourth axis and did not exist on the page
before: a mark only where the label names a third party - **322 of 710 carry one and every one is a
brand mark on a Continue with row**, the other 388 carry none. The mark had been written up as a
private detail of one place, so "a button with an icon" was not something the system had declared.

**Every empty cell carries a verdict and a source.** Three are FORBIDDEN with a product counter
behind them - icon with brass (0 of 710), icon at fit width (0), full width in the header (0, and it
is the width rule applied rather than a separate ban) - and two are UNCLOSED ZONE with a backlog
number: a disabled control anywhere but `.confirm-btn`, which the product has simply never had, and a
marked control at fit width inside a sheet, which two rules each half-forbid and neither settles.
`ui-kit/docs/backlog.md` **S26**. A blank cell is neither, and there are none.

**S24 is not closed and was not touched.** It is the CSS consolidation and its closing condition is
still the markup thaw: the stylesheet is unchanged, the 13 reconciliation rules are still 13. What
its row gained is one sentence saying the page now answers with axes instead of a list of places.

**Asked of a browser: 360 and 1440, both themes.** 5 galleries, 2 covers notes, 40 pictures, 0 broken
images, 0 horizontal overflow on the page and 0 inside the live frame, and the specimen driven with a
real pointer and a real focus: the quiet ground moves on hover, the brass one takes its glow, the
ring is solid 2px. **0 console errors** on three of the four combinations; the fourth is Chrome asking
the static server for `/favicon.ico`, which this repo does not ship and which appears on the first
context of any launch. Watched at the network layer instead, the page makes **0 failed requests**.

## 2026-08-04 - 104 marks of markdown on four pages, and every gate green

**What was there.** `ui-kit/_gen_docs.py` renders the stage's seven documents as pages of the
vitrine. It does not implement links. Markdown links were therefore printed rather than rendered:
**102 of them**, in 97 rows of `inventory.html` where `](../header.html)` sat in the open beside
the word it was meant to be a link on, and in three paragraphs of `architecture.html`,
`history.html` and `backlog.html`. Two more marks were `**` from a bold span that never fired. 104
literal marks on four shipped pages, and the build was green on all 34 gates.

**Why nothing saw them, and this is the part that generalises.** Gate 21 re-renders each document
in memory and compares the result with the page. That certifies the page is what the generator
makes and nothing else, which is the right question about drift and the wrong question about
correctness: **a defect in the renderer is reproduced identically on both sides and reads as
agreement.** A generator compared with itself is a tautology. It is the same shape as row 42 in
`ui-kit/docs/defects.md` - a check reporting clean about the wrong object - and the same answer as
gate 22, which asks the panel where it is rather than asking the shell.

**Three defects, not one, and the second is the one worth the entry.**

**1. Links were not implemented.** Now they are, and the order inside `inline()` is the whole of it:
after the code-span lift-out, so the label of ``[`history.md`](./history.md)`` is already a
placeholder and the backtick cannot be read as anything else; after `esc()`, so the address arrives
attribute-safe and is not escaped a second time. Inside a link label, FILEREF linking is
**suppressed**, and that is named in the code because the markup it prevents is invalid rather than
merely ugly: the label of ``[`history.md`](./history.md)`` is a code span whose text FILEREF
matches, so left alone it would have produced `<a>` inside `<a>`. It also settles a subtler one the
same way. In ``[`docs/backlog.md`](../../docs/backlog.md)`` the label's TEXT resolves through the
mirror map to this stage's backlog page while the ADDRESS means the root document, so linking the
label sent the reader somewhere the author did not write. The address is the link; the label is
what it is called.

**2. Every address was one directory off, and that is where the real defect was hiding.** The
sources are in `ui-kit/docs/` and the pages are written in `ui-kit/`, one level up, so an address
carried across unchanged points somewhere else: `../position.html` in the markdown means
`ui-kit/position.html` and from the page has to be `position.html`, and `../../docs/decisions.md`
has to become `../docs/decisions.md`. `rebase()` moves each address from the document's directory
to the page's and **fails the build** on one that does not resolve from the directory the page is
in. That is deliberate and it is gate 4's idiom moved one step earlier: a generator that can prove
an href before writing it should not leave a dead link for a gate to find afterwards. Proved by
changing one address to `../history.md`: the generator exits 1 naming the document, the address and
what it resolved to, and `_check_kit.py` exits 1 with it.

**3. A number that ends a sentence is not a list.** These documents wrap at 100 columns, so
`history.md` has lines beginning `17. The port wrote...` and `1400. Measured at 1920...` - the tail
of "on every one of the 17." and of "stopped at 1400." The paragraph ended at the digits, the next
block was read as an ordered list, and a `**bold span**` that straddled the break was opened in a
`<li>` and closed in a `<p>`, so neither half fired and the asterisks printed. The rule that
settles it is CommonMark's, and it is the rule because it exists for exactly this: **an ordered
marker may interrupt a paragraph only when its number is 1.** At the top of a block any number
still starts a list. That one-character change rewrote nothing but the two pages that carried the
defect, which is the evidence that it is a rule and not a patch.

**A link to a `.md` with no mirror stays a `.md`, and it is a named exception.** A document this
stage renders is linked at its PAGE - that map already exists and gate 21 keeps it current. The
root `docs/decisions.md` and `docs/backlog.md` have no page to be linked at: they belong to the
project rather than to the stage, nothing renders them, and the documents genuinely cite them, so
the choice is an honest `.md` href or a sentence that names a file and cannot reach it. Gate 21's
"no link into a raw `.md`" now exempts those **two addresses** rather than any page, because
whether a mirror exists is a property of the target and of nothing else, and it carries the control
every declared list in this repo carries.

**Gate 35, proved in both directions.** Forward: disabling the link substitution and re-rendering
turns gate 35 red on all 102 marks **while gate 21 stays green**, which is the tautology
demonstrated rather than argued; reverting the ordered-marker rule alone turns it red on the 2
remaining `**`, again with gate 21 green. Backward: a declared exception that covers nothing fails
as loudly as an undeclared defect - a `MD_LITERAL` entry for a page with no literal markdown and a
`MIRRORLESS` address nobody links both failed on the first run. The corpus is **every generated
page**, 132 of them, not the seven documents, for the same reason the SCENES comment gives at the
top of `_check_kit.py`: `inline()` is imported by the component and pattern generators too, so a
link authored into a rule or an authored section is rendered by the same code and belongs to the
same question. Measured before and after: **104 marks -> 0.**

**And it went red on the document that describes it**, which is how it learned the last rule it was
missing. The `defects.md` row written for this gate quotes both marks inside `code` spans, so the
first green build after the row was added was not green. A quotation is not a survival: the scan now
strips `<code>` and `<pre>` first, using the same `QUOTED` that gate 4 has used since prose about a
path was reported as a path. That is the **fourth** checker in this file to have to learn to stop
reading a sentence as the thing the sentence is about, and it costs the gate nothing here, because
all 104 marks were in running text - a table cell and a paragraph break - and not one of them was
inside a quotation. The two-way proof was re-run with the strip in place before it was kept.

**Asked of a browser as well, because a checker that reads the source does not read the page.**
Seven document pages at 360 and at 1440, Chrome, and the question asked of `innerText` with every
`<code>` and `<pre>` removed first, so the instrument asks what the gate asks: **0 visible markdown,
0 nested anchors, 0 dead hrefs resolved from the page's own directory, 0 horizontal overflow, 0
console errors** over all 14 renders. **225 `a.tk-doc-ref` anchors** per width, 102 of them the
links this entry is about and the rest the file references the vitrine already drew, and every one
of the 225 carries its border in the computed style, which is the difference between an `<a>` and a
word that used to be sitting next to a bracket.

**Two stale counts corrected while the row was added**, both hand-written and neither gated:
`ui-kit/docs/defects.md` said "34 gates over 80 checks" when the file held 82, and its PROVEN table
said 25 classes over 26 rows. They are 35 gates, 85 checks and 27 rows now. The README's two spans
are computed by `_fill_inventory.py` and were right, which is the difference the computed span buys.

## 2026-08-04 - Step 8, and the six things a taxonomy could not have told us

The inherited plan for this step was eighteen classes of defect, hunted by hand, over 105 screens in
two themes at two widths. What it became is `ui-kit/docs/defects.md`, whose first column is not a
category but **which gate catches it**, because a green gate is a proof and a manual pass over a
gated class is a second, worse instrument reporting on the same thing. The table opened at 23
proven, 7 measured and 15 open; it closes this step at **26 proven, 7 measured, 11 open**.

Four gates were added or grown, and every one of them was proved in both directions and given the
control this repo puts on every declared list: an entry that covers nothing fails as loudly as an
undeclared item.

### The five things that were found by fixing, not by looking

**1. The contrast defect was never a token value question.** `oddsbar.css` put `--outcome-yes` and
`--outcome-no`, the FILL roles of a 4px band, onto 12px bold TEXT. Surfaces answer to 3:1 and take
it; text answers to 4.5:1 and did not, on 266 elements across 105 painted screens. The text roles
already existed. **The fix is one word in each of two declarations**, no token moved and no value
edited, and all four measurements changed including the one that already passed, because leaving it
on the fill role would mean one component reading a different token per theme for the same word.
`ui-kit/docs/history.md` records this as the run's best evidence for having a semantic token level
at all: without a separate text role the only repair available would have been the VALUE, and the
bar would have moved with the label.

**2. Two of the three keyboard findings were not defects, and the real one was already written
down.** The test that settles it is the RESULT, not the handler. `.rules-panel` is not a control at
all - the control is `.rules-tab`, a real `<button>` on all 18 instances - and the four
`<span class="bp-side">` are skeleton placeholders on two loading screens, which must not be
focusable. `.opt-row` has a working keyboard route: Enter and Space on the inner button produce a
state identical to a mouse click in every field measured. **The one real blocker was
`docs/backlog.md` 22**, which had been sitting there since step 2: 16 filter inputs at
`display:none`, so three radiogroups on 104 screens could be operated by a mouse and by nothing
else. Closed with the idiom the system had already chosen twice, and the "eight or so new tab stops
per screen" objection in the original row is answered with a number: **zero when the menu is closed,
one when it is open**, because a radiogroup is one tab stop by construction.

**3. Both new gates failed on the defect they were written for, and that is why they are gates.**
Gate 33's two-way proof reverted each of the five trader-term placements one at a time and demanded
a red for each. Two came back GREEN: `holder` was not in the lexicon at all, because the list held
`position` and not the person who has one; and the scanner could not see inside an element whose
parent it had already consumed, because `finditer` does not overlap. Gate 34's idle control found
**eight dead rows of forty one** in the hand-written half of the inventory map, which is the same
half both false file cells had come from.

**4. Two hand-written cascade cycles were made of misfiled classes.** Moving 17 rules to the files
that own them took `_levels.ORDER_BREAK` from four entries to two, because `(comments, tabs)` and
`(betpanel, event-detail)` were not real nestings - they were `.seg` living in `tabs.css` and
`.rp-inner` living in `event-detail.css`. **A hand-written tie-break is a place where the map
stopped agreeing with the files**, so an entry there is now readable as a finding waiting to be
closed rather than as a setting. 525 snapshots at three widths, 0 differ, 0 elements changed.

**5. The instrument was cropping the subject of its own photograph**, and fixing it found two more
instrument defects underneath. 36 of 790 state pictures were short, every one a FOCUS picture -
the single state whose whole subject is a ring drawn outside the box. The pad is now DERIVED from
the element being photographed, in the state it is in. Underneath: a frame past the last pixel of
the document took the whole run down (a bet sheet is `position:fixed` and is not in the document's
scroll extent), and the clip and `boxAt()` had never agreed on a coordinate system - which was
invisible for as long as every specimen was too short to scroll.

### The two things that were measured and deliberately not paid

**The button family is not consolidated.** 5 names, 3 axes, 30 rules of which 13 are reconciliation.
The measurement is the decision: the axes do not fit inside `components/button.css` (the position
mechanism belongs to a pattern and the width to a `state-block` context), and the right answer for
emphasis is `.primary` in markup that is frozen. What is paid instead is the PAGE, which now opens
with the axis matrix. `ui-kit/docs/backlog.md` **S24**, closing condition written in: with the
markup thaw, not before.

**The inventory's `#f` column is not computed and cannot be yet.** 38 of the 54 rows whose classes
are findable disagree with a count of the files carrying them, and the disagreement is not all
error: some cells mean "files that carry the markup" and some mean "screens where a person sees it",
and a dialog emitted into 105 screens and opened on 4 is both. **S23**: a definition first, a column
second.

### The taxonomy re-run, with the caveat it has to carry

`node ui-kit/_verify/audit.cjs --screens` after every edit above: **106 pages, 2 themes, 2 widths =
424 renders, 0 findings**, 720 pinned boxes measured at 640px of window, 660 unmeasurable through a
blend or a filter and 380 painting no glyph, both counted apart. That instrument's zero is the one
that stood in three documents fifteen times while 378 elements measured under the floor, so it is
written here with its date and its corpus and not as a claim: it is not gated, and it is only as
good as its next audit.

## 2026-08-03 - The rail is a slot, and it took a real screen to find out

**What happened.** Step 7 of the Design System stage set out to test whether the system is
self-sufficient: build `ui-visual/terms.html`, a page of a TYPE the system had never drawn, out of
`components/` alone and count what was missing. It did that, and it also did something that was not
on the plan. It changed what `browse-shell` IS.

**The pattern stands on 77 screens** and had been read, correctly, as "a sub-category rail beside a
content column". Every one of the 76 screens that existed before Terms put the SAME component in the
rail: `catnav`'s `.subcat`. So the rail and the category rail were one idea, and nothing in the
product could tell them apart, because nothing in the product had ever put anything else there.

Terms put a table of contents there. After that the pattern reads differently: **the rail is a SLOT,
and the shell does not know which component is standing in it.** `components/toc.css` is a new
component that stands in the same place at a different sticky offset (66px against 120px, measured
rather than assumed, because a document page has no category bar for the header strip to condense
into), and `browse-shell` needed no change at all to hold it.

**Why this is recorded on its own, apart from the four backlog rows Terms opened.** The rows (S1,
S2, S5 closed the same day; S3, S4, S6, S7, S8 left open) are what the step promised: a list of what
the system does not have. This is not that. It is a correction to what the system already had, on
its most-used arrangement, and **it was not derivable from the 76 screens** - not because anybody
read them carelessly, but because a set of 76 identical answers cannot show you which part of the
answer was the question.

**The decision this settles for the stages after.** A demo screen tests whether the parts exist. A
real screen of an unseen type tests whether the parts mean what their names say. The two are not
the same exercise, and only the second one can rewrite a definition. Step 7 was scoped as the first
and delivered the second, so the next stage that wants to test the system should be scoped as the
second on purpose: **one real page nobody has drawn, not five variations of one that exists.**

**What it cost to get there:** no new class, no new token, no new state and no new rule on the page
itself, and 104 screens at two widths with 84,836 element boxes compared before and after, 0 moved.
The definition changed; the product did not.

---

## 2026-08-02 - Four states, three press mechanisms, and the hovers that were only true in one theme

Step 2 of the Design System stage: the states roll-out. The reference component was accepted in the
browser, and the format went out to the rest of the system through subagents, one round per level,
bottom up.

### The estimate, in three columns and not two

The pack assumes no component has states yet. This one had them in **24 of 36 files**, all of them
`:hover`, so the roll-out had to align a format rather than write one. The census, taken by asking
each file which of its selector SUBJECTS is an interactive element in the shipped markup:

| | count | |
|---|---|---|
| already had states | 24 | every one of them `:hover` only. One `:active` in the whole system (`loadmore`), three `:disabled`, four `:focus-visible` |
| interactive, no state at all | 3 | `market` (a `<summary>`), `bottomnav` (the tab bar, touched more than any other control), `position` (a card-link on 15 rows, which read as static because the anchor is written with `:has()`) |
| not interactive, gets none | 9 | declared in `_levels.STATIC`, one line of reason each |

The format audit of the first column found exactly three things, and only three: six
`filter:brightness()` hovers, no `:active` anywhere but one file, and no `:disabled` on the one
control the product actually disables.

### Rounds by the computed order, and only the css fanned out

Rounds came from `python3 ui-kit/_levels.py --order`, which gate 23 already enforces, not from a list
written by hand: atoms, molecules, then organisms in two batches, the ones containing another
organism last. Within a level the subagents ran in parallel; between levels, sequentially, because a
card that adds a hover before its button has one will draw the button a second answer.

**The fanout is narrower than the pack's and that is a strength.** The pack gives each agent its own
css AND its own page. Here the pages are generated and the states table is read out of the css, so an
agent touches exactly `components/<name>.css` and the parent regenerates every page in one pass. The
conflict disappears by construction and the page stays a projection of the code rather than a second
copy of it. `tokens.css`, `index.css`, `base.css` and `_nav.js` stayed with the parent, and an agent
short of a token stopped and said so rather than inventing one. Two did, and both were right.

### Three roles, and no component level

- `--bg-pressed`, the ground a held control settles onto. It existed as `--bg-chip-pressed` with a
  single consumer; the roll-out gave it twenty. Renamed for the STATE, because the icon button in the
  header is not a chip and settling it onto a chip's ground is a category error the next reader
  inherits.
- `--color-action-pressed`, brass held down, and it is needed by exactly the controls that are FLAT
  brass: the filter switch that is ON and a ticked cookie checkbox. Everything else brass is a
  gradient and presses by geometry.
- `--chrome-pressed`, the same step for the course panel. It cannot borrow the product role: section 3
  overrides that one and does not touch the chrome, so a shared role would press a graphite row to
  chalk on a daylight page.

**No component-level tokens.** The stage before this one deferred the decision to here with a
criterion: a component token is justified only where a state lands on no semantic role. Every state in
this pass landed on one, so the answer is none, and an empty component level "so it exists" would be a
third round of renaming with no flexibility bought.

### Three press mechanisms, each forced by a number

A press had to be answered three different ways, and the third one is the interesting one.

1. **A quiet control** settles onto `--bg-pressed`.
2. **A brass gradient** reverses its own angle, 135deg to 315deg, and drops its glow. The light falls
   to the bottom right, which is what a plate pushed IN looks like. It reads the two roles the rest
   state already reads and costs no value at all.
3. **A filled outcome control presses by DEPTH, not colour.** `--text-on-no` on a flat `--outcome-no`
   is 4.64:1, the floor with 0.14 to spare, and darkening the ground through the only role available
   costs 4.48:1 at 92 per cent and 4.29:1 at 82. A mix small enough to pass is a mix nobody notices.
   So the fill does not move: an inset shade at the top edge does, `--edge-shade-strong`, the same
   role every lifted stone in this system uses, and the ground the ink was measured on stays exactly
   where it was. Half a pair was refused on the way: YES has the room and NO does not, and a YES that
   darkens beside a NO that does not reads as a broken NO.

The same measurement fixed a second surface later: `--bg-pressed` LIGHTENS a `--bg-card-quiet` row in
the Vault and resolves to the same chalk step in daylight, so a position row also pays for its press
out of depth.

### Focus is a substrate answer, and this is the deliberate deviation from the pack

The pack asks for `:focus-visible` on every component. `base.css` declares it once for all 36 files,
and a browser sweep of 153 pages in both themes had already found 0 of 179 ring kinds without a
visible ring. Fourteen component files used to carry their own copy of that rule and twenty-four did
not, and gathering it was the whole point of the previous stage; adding twenty more copies would undo
it. **A component speaks up only when its GROUND needs something different**, which is the rule
committed earlier the same day.

Four did, and one of them was a real hole nobody had seen: the Event Detail tab strip and the profile
tab strip are radio groups, so the ring was being painted on the visually hidden `<input>` and a
person tabbing through either strip saw nothing at all. It moves to the label. The other three are
clipping: the category strip and both tab bars are scroll containers that cut an outset ring, and the
sheet grab sits flush at the top of a sheet that clips its own corners. All four take an inset offset
and keep the ring colour. The fifth is the how-it-works close disc, which sits inside a brass radial
glow where the brass ring measures 2.52:1 at the brightest point: it reads `--text-strong` instead,
5.33:1 and 10.13:1.

### Seven defects that only a press could find

Giving a control a state means reading its rest state, and that is where these came from.

| what | measured |
|---|---|
| `.bet-dock .confirm-btn` had no `background` anywhere | the rule names the panel and the sheet and not the dock, so Confirm bet rendered in the user agent's own ButtonFace grey on the four screens where a person places money |
| `confirm-btn[aria-disabled="true"]` on `deposit-minimum-not-met` | styled exactly like an enabled button |
| `.hh-all:hover` read `--color-action-lit` | 9.57:1 on graphite, **1.71:1 on chalk**. A pale brass meant to sit UNDER dark ink, used as ink: in daylight the link vanished at the moment a person pointed at it |
| `.hf-title:hover` and `.hh-name:hover` read `--text-strong` | which IS `--text-primary` on chalk: 14.85 over 14.85, a state that existed in one theme only |
| `.bp-side:hover` read `--bevel-strong` | a lit LIP role that section 3 raises to 70 per cent white: 1.02:1 as a border on a chalk control. A lip is not an edge |
| `.notif-all` had no hover | it is a sibling of the dropdown list rather than a member, so it fell out of the selector and out of every later reading of the file |
| `.hiw-full` had no hover | the only brass action in the system without one: the arrow nudged and nothing under it moved |

Six `filter:brightness()` hovers are gone with them. A filter multiplies whatever is beneath it, so no
theme and no role can reach it, and the same 1.08 is a different decision on each of the two stones.

### What was found and NOT fixed, and why

Three, all in the backlog as items 22 to 24. The filter panel hides every option with `display:none`,
which takes it out of the tab order and out of the accessibility tree, so the sort radiogroup on 104
screens works with a mouse and nothing else; the fix is css-only but it changes behaviour, and that is
a product decision rather than a state. A multi-outcome row is a `<div>` with a click handler and no
keyboard path, and the fix is markup, which the grey tree owns. And the `aria-live` row turned out to
rest on a premise that does not hold, below.

### The aria-live row was re-measured, and the count was right while the conclusion was not

The entry gate for this step asked whether gate 18 compares ATTRIBUTES or only structure, because a
live region is an attribute on a shipped screen. It compares structure only: `shape()` in
`_check_kit.py` builds `tag.firstclass` per element and reads no other attribute, and gate 19 uses the
same function. So the edit was clear.

The premise was not. Measured in BOTH trees: the 9 screens with a live region are identical in grey
and in colour, and the toast on `toasts.html` already carries `role="status" aria-live="polite"` and
`role="alert" aria-live="assertive"` on its two groups. There is no missing toast announcement to add.
What IS missing is the form-error axis, `aria-invalid` and `aria-describedby` at 0 of 105 while three
screens ship a visible error tied to no field, and that is a markup change the grey tree owns.
`aria-expanded` at 0 is correct rather than a gap, because every disclosure here is a native
`<details>`. Item 4 is struck and replaced by item 24.

### The gate, and the instrument

**Gate 25**, three checks: a component not on `_levels.STATIC` declares hover and press, a component
on it declares neither, and no state carries a colour value. The second check is the one that matters,
for the reason gate 24 already carries: an exception list that can absorb a component quietly is not a
declaration, it is a way of switching the check off.

**Measured at rest: 14 of 36,150 elements moved** over 25 screens in both themes, against a **noise
floor of 10** taken by diffing the same version against itself. Four of the fourteen are real and both
are named in the table above. **Focus: 0 of 128 ring kinds flagged** over 33 pages in both themes.

Two instrument bugs were found and fixed on the way, and both were caused by this pass adding
transitions. A control mid-transition between themes reports the tween rather than the value, which
produced 17 false flags in one run. And a ring was being measured against the control's own fill
rather than the surface it stands on: with `outline-offset` positive the ring is painted OUTSIDE the
border box, so a brass ring on a selected YES read 1.37:1 against a green it never touches. **A ring
answers to what it stands on** is not only a design rule; it is how the ring has to be measured.

## 2026-08-02 - A regex cannot read a colour, and one of the three defects it found did not exist

Two measurement bugs in one day, in the same sweep, and the second one invented a defect. Both are
worth the entry because the conclusion is the same and it is a rule: **the tool that reads the page
has to be checked as hard as the page.**

- **A closed `<dialog>` is inert, and a scripted `.focus()` on it fails silently.** The element does
  not become `document.activeElement`, `getComputedStyle` returns its resting style, and a sweep
  that measures the outline reads NO RING. The dialog amount field was reported broken by that
  sweep AFTER it had been fixed, and it was pressing Tab by hand that showed the ring was there. The
  sweep skips inert subtrees now.
  **What that invalidates:** every earlier "no ring" verdict on an element inside a closed dialog.
  There were two, both from the first pass over `event-feed.html` on 2026-08-02, `a.notif-all` and
  one unclassed `<button>`, and both were reported in chat only. Nothing in the repo carries them:
  the only "no ring" verdict written to a file was `.kit-field` in backlog item 21, and `.kit-field`
  is not in a dialog, so it stood, and it has since been fixed. No file needed correcting. That is
  luck rather than process: a verdict from a tool with a known blind spot was one commit away from
  being written down as a fact.
- **A regex cannot read a colour, and `color-mix(in oklab, ...)` is the case where it silently
  lies.** `getComputedStyle().backgroundColor` returns that function verbatim, and pulling numbers
  out of it with `/[\d.]+/g` yields the oklab components, 0.95 and 0.0005 and 0.016, which the
  contrast maths then treats as sRGB bytes. **A pale brass-tinted banner measured as near black.**
  On that reading the focus ring on the push banner's buttons came out at 2.72:1 against a 3:1
  floor, on three screens, and it was written into the backlog as a defect to fix.
  It is not a defect. Measured with the browser doing the parsing, the same ring is **6.95:1 in the
  Vault and 6.73:1 in daylight**. The fix is to stop parsing: a 2D canvas resolves any css colour
  string to sRGB bytes, so `ctx.fillStyle = <whatever the computed style says>` and read the pixel.
  The ancestor stack is then composited in order, alpha by alpha, instead of guessed at.
- **What that invalidates, and it is more than one number.** Every contrast figure this repo has
  taken with the regex sweep, wherever the ground came through `color-mix`. Two were written into
  `tokens.css` beside `--focus-ring` and are corrected in the same commit: the true spans are
  **6.67:1 to 9.06:1** in the Vault and **5.71:1 to 7.46:1** in daylight, measured over every
  focusable control on 153 pages. The direction of the error is the interesting part: it made
  things look WORSE, not better, so nothing shipped on a false pass. The next one might not be so
  kind.
- **What survives, and it is the useful half.** Two of the three rings were real and both are fixed.
  The one that was not real would have cost a new token and a new role, invented to solve a number
  that a canvas could have disproved in ten seconds. **A finding is not a finding until the
  instrument has been checked**, and the check is cheap: measure something whose answer you already
  know. A pale banner is pale.

---

## 2026-08-02 - The two "now, or never" surfaces are closed as NEVER, and that is the decision

`architecture.md` has carried a table of five unread surfaces since the close of Tokens and
Components. Three of them name a later stage as their owner. Two named no owner at all, only "now,
or never", and a row that says "now, or never" is not a decision, it is a decision postponed in a
form that never comes back up. Both are closed here, as NEVER, with the reason.

- **The 28 course pages' own content: 203 KB of inline css nothing has read.** Not read, and not
  going to be. Those pages are the course frame around the work, not the product: the one thing in
  them that a reader of this repo interacts with is the roadmap panel, and step 9 already took that
  out into `components/course-chrome.css` and holds the 28 pages to it with a generator and gate 22.
  What is left is 203 KB describing lesson pages, and a finding in it would be a finding about the
  frame.
- **The grey tree's inline css: 34 distinct `<style>` bodies over 104 pages, the largest 52 KB.**
  This one is closed by a rule we made ourselves and would have to break in order to act. The grey
  tree is frozen: `wireframes/` owns structure and copy, it is never painted, and the generators
  that would rewrite it are the ones `CLAUDE.md` forbids running because the voice rewrite was
  applied to the HTML by hand and never back-ported. **Every finding in those 34 bodies would be a
  finding we have already forbidden ourselves to act on**, and gate 14 was deliberately narrowed
  away from that stylesheet in step 7e for exactly this reason. Reading it would produce a list
  whose only possible next line is "not fixed, by rule".

The distinction worth keeping is between a surface nobody has read and a surface nobody may act on.
The first is a risk. The second is a boundary, and writing it down as an open item makes the
boundary look like neglect. Three rows of that table stay open with a stage against each; these two
stop being rows.

---

## 2026-08-02 - The audit thread closes with a gate, and the defect it found gets fixed behind it

Two things in one day, in that order on purpose: the gate first, on a clean base, then the product
change so the new gate is what checks it.

- **Eight components stayed short, and none of the eight is a thin stand.** Four own a page-level
  plate (`catnav`, `feed`, `event-detail`, `toast`) so on a screen the whole page is their
  descendant; one owns a tab PANEL (`tabs`), so a profile tab holds a card gallery; two carry two
  components on one element (`dialog` with `hiw-dialog`, and with the bet sheet); and two are `.pos`
  used as a generic plate. Eleven entries in `_levels.SPECIMEN_DEBT`, each a line with its reason.
- **Every entry says it is a DEBT and what closes it.** Without that sentence the list reads as
  configuration in six months, and a page plate living inside a component file becomes a legitimate
  arrangement rather than something nine of these eleven lines name a backlog item for. Closing means
  splitting the component, never widening the line. A part of `*` is used only where the cause is a
  CONTAINER, because there the contents churn with every screen and today's list is noise; a named
  part is used where the cause is one element or one class in the wrong file, because there a new
  name is a new fact.
- **Gate 24 is the comparison the audit already made, narrowed.** What a component contains in its
  stand against what it contains on the 105 painted screens, both from one function, minus the
  eleven. It fails at the moment a component gains a case nobody stages, which is the moment its
  level stops being computed and becomes a guess held up by a floor. One second, 105 documents.
- **Its second half is the one that matters, and it is the reason the list can be trusted.** An
  exception list that can be quietly extended is not part of a gate, it is the switch that turns one
  off: the cheapest way past the first check would always be one more line. So an entry covering no
  real difference fails just as loudly. Proved in three directions rather than one: gutting the
  loading scene out of the card stand turned the first check red and named `card contains skeleton`;
  restoring it turned it green; two fictitious exceptions, one wildcard on a component with no gap
  and one named pair that exists nowhere, turned the second red and named both.
- **Six declarations now, and a reader is told they exist.** `NOT_A_COMPONENT` 3, `SHARED` 5,
  `MODIFIER` 1, `RAISE` 13, `ORDER_BREAK` 4, `SPECIMEN_DEBT` 11. Most of what this system says about
  itself is computed, and the part that is not is now in one table in
  `ui-kit/docs/architecture.md`, with what each is for and who closes it. Someone surprised by a
  level or an `@import` position should find the surprise declared.
- **Then item 20, and the fix had to be css.** 52 of 482 skeleton marks drew at zero size on five
  loading screens. The tempting fix is the markup, and it is closed to us: a painted screen has a
  grey twin frozen since stage 04, and gate 18 compares the two trees inside `<main>`. So
  `<span class="sk-line">` stays a span and eight lines of BASE rules give it a box, `display` first
  because it is the property that decides whether height and width mean anything. They win nothing:
  every scoped rule below reaches the same element with more classes, so a card mark and a position
  mark keep the treatment they had.
- **Measured on the 19 screens that carry a mark, three widths.** Only `.sk-*` selectors were added,
  so only those 19 could move, and that is an argument rather than a sample. Fourteen came out
  identical to the property. The five that changed are the five the item named: on the feed screens
  exactly 12 elements each, changing `display`, `width` and the box and nothing else; on the two
  detail screens the 8 bars gained height, margin and a fill, and 176 more boxes moved down because
  a bar that was 601x0 is now 601x8. **0 of 482 marks now render at zero.**

---

## 2026-08-02 - A state is not a component, and five stands were showing less than the product ships

The specimen audit of the day before compared what each component contains in its stand against what
it contains on the 105 painted screens, using one reading for both. Eleven components came out
short. This entry is what was done about them.

- **The ownership map knew components and did not know states.** `.skeleton` is a subject in
  `position.css` (`.app-case .pos.skeleton{gap:...}`) and only ever an ancestor in `skeleton.css`
  (`.card.skeleton .sk-thumb`), so "fewest ancestors" handed the word to `position`. Both rules are
  correct where they stand. What was wrong is that a state word had to be given to somebody at all:
  every `<article class="card skeleton">` on nineteen loading screens then read as a POSITION root,
  and position came out containing card, account, event-detail and hiw-dialog. Four phantom edges
  from one misplaced word. Fixed in the map, not in the css: `_levels.MODIFIER`, one entry with its
  reason, skipped by the reader in **both** directions, because skipping it only at the root leaves
  the same phantom one element higher (the feed holds the card, so the feed would then contain
  position). Stage 09 brings hover, focus-visible and disabled, which are the same species.
- **It was checked for company before it was declared.** A sweep over all three trees asked which
  classes stand as a second class on another component's element: 20 in the painted screens, 16 in
  the specimens, 18 in the grey tree, the same list every time. Nineteen of the twenty are something
  else, and the distinction is what the word NAMES. `.tr-ic` and `.prov-x` are a component's own
  decoration of a shared atom; `.lang-menu` on `.filter-menu` is the footer skinning the filter
  dropdown; `.hiw-dialog` beside `.app-dialog` is two components on one element (item 16);
  `.rp-inner`, `.ed-tabs` and `.bet-sheet` are classes in the wrong file (item 17). The two the
  guess had named, `.scrolled` and `.resolved`, were neither: `.scrolled` is never a subject in any
  file, so the map has never held it and the reader has never seen it, and `.resolved` does not
  exist (the class is `.resolved-panel`, and that is item 17). One entry, and the mechanism is now
  there for the five that Stage 09 will bring.
- **The five thin stands were filled from the screens, not from the kit.** `kit.html` is frozen
  provenance and it stages an earlier product: its skeleton card is missing a line, its detail plate
  is a `div` where the product ships an `article` and carries three sections the product's card does
  not. So the blocks were copied out of `ui-visual/event-feed-loading.html`, `event-detail.html`,
  `active-bets-loading.html`, `event-detail-{multi,loading,resolved}.html` and `win.html`, each
  named at its block in `specimens.extra.html`. Every one keeps the real ancestor chain above the
  component's own root and adds nothing around it: a reconcile box outside the dialog is a grey
  rectangle, because three of the four rules that draw it are scoped under `.app-case`,
  `.outcome-dialog` and `.win-dialog`.
- **Three cycles appeared, and a cycle is not a defect in the reading.** `card` holds `.ed-head`
  because the detail page's header IS a card, and `event-detail` holds the card: both halves are in
  the markup. `betpanel` holds `event-detail` only through `.rp-inner`, and `notice` holds `dialog`
  only through `.fine`. All three were declared in `ORDER_BREAK`, which drops an edge for ORDERING
  and keeps it for the level, with the direction decided by which file restyles the other's insides.
  Two of the three name a backlog item as their reason, which is the point of writing the reason
  down: the declaration says how long it should live.
- **One level moved, and one line of `index.css` moved with it.** `notice` L2 -> L3, because `.fine`
  is attributed to `dialog`. `notice.css` therefore sorts into the organisms and moves from #17 to
  #23, behind `cookie-consent`, `bottomnav`, `hiw-dialog`, `hero`, `comments` and `catnav`. None of
  those six writes a selector `notice.css` also writes, and none of them has a rule that reaches a
  class `notice` owns, so the move is inert by reading. It was measured anyway, the way the cascade
  reorder was: 8 screens carrying a notice, three widths, 35 computed properties and the box per
  element. **0 of 16,662 elements changed.** Whether `.fine` should belong to `dialog` at all is a
  new question and is backlog item 19.
- **The floors were revised mechanically, one at a time.** Each of the fourteen `RAISE` entries was
  removed and the whole level table recomputed: thirteen changed an answer, one did not. `footer`
  holds a language menu and a trust bar, so the arithmetic reaches L3 without help, and its floor
  had been carrying nothing. Deleted, with the reason in its place. `hiw-dialog` keeps its floor and
  gets a new reason: the old one said the frame is not a descendant, and the markup says otherwise.
  It is backlog item 18 now, and the only one of the thirteen that a split would remove.
- **A generated file was corrected in the wrong copy, and re-running the generator proved it.** The
  dialog merge had removed the dangling `signin` reference from `specimens/index.json`, which is
  OUTPUT. `specimens.map.json`, which is the source, still said `"component": "signin"`, so the
  first extractor run after the merge brought the deleted component straight back and gate 8 failed.
  Fixed at the source, with the mistake written into the entry's note.
- **README said 36 components and broke them down into 34.** Both numbers were right and the
  sentence was not: 36 is every component file, 34 is how many are COMPOSED, because `base` and
  `course-chrome` are the substrate a screen stands on and a substrate has no level. It is written
  by `_fill_inventory.py` from `_levels.py` now, between two markers, and gate 2 fails when the span
  goes stale. A generated span is only single sourced while something fails when it drifts; the
  gate was proved by breaking the number and watching it go red.

---

## 2026-08-02 - Two dialog skins were never components, and the merge risk was one line of the cascade

`signin.css` held 2 rules. `outcome-dialog.css` held 2. The outcome dialog is made of 26 rules and
**24 of them were already inside `dialog.css`**, along with 3 for `.signin-dialog`, 3 for
`.bet-sheet`, 2 for `.win-dialog` and 1 for `.loss-dialog`: 33 of that file's 59 rules were about a
variant. The merge had already happened in the css and only the file boundary pretended otherwise.

- **The test was anatomy, and anatomy was read from the DOM.** Zone for zone the shared sheet, the
  sign-in sheet and the win overlay are the same object: a top band carrying the title, a body, and
  nothing else. What differs is what stands in a zone (an h1 and a link instead of an h2 and a
  sub-line) and a width, and a width is a value. **Nobody in the family has an action row**, which
  was a claim on the record until the markup was read: the confirm button sits inside the body in
  every one of them, and an earlier reading had scored the how-it-works dialog as different for
  losing a row that does not exist. A selector says who STYLES a thing; only the DOM says what it is
  MADE OF, and the first pass had asked the css.
- **The containment graph said the same thing independently.** `outcome-dialog` CONTAINS `dialog`
  and so does `signin`. A variant that contains its own base is the signature of a skin.
- **The whole risk of the move was four lines, and it was real.** `dialog.app-dialog:modal` in the
  mobile block is (0,2,1) and so is `dialog.app-dialog.signin-dialog`, so between 411px and 640px
  the two contest `max-width` at EQUAL specificity and **only source order decides**. As separate
  files these rules loaded after `dialog.css` and won. Appended to the end of `dialog.css` they
  still win; moved to the top they would lose and the sheet would go full bleed. So they are at the
  end, and the file says why on the line above them.
- **Measured, and calibrated against the failure it was looking for.** Seven screens where the family
  is actually painted, at 360, **500** and 1280, element by element on 35 computed properties plus
  the box, old tree against new: **0 of 15,585 elements changed**. Then the same four rules were put
  at the TOP of the file on purpose: the win overlay at 500px went from `[40,159,420,741]` to
  `[0,176,500,724]`, 420px inset to 500px full bleed. **At 360 and at 1280 that same break measured
  zero.** The width that could see it was the one added because the specificity tie predicted it,
  which is the argument for deriving the test from the mechanism rather than from habit. A repeat run
  on the unchanged tree moved 162 elements on `sign-in`, all of them inside the `<aside>` and none
  carrying a dialog class: the panel artifact from the cascade pass, still there, still not the
  product.
- **What it cost the system.** 41 css files to 39, 38 components to 36, 40 imports to 38, 49 stand
  pages to 47, 40 rows in `_nav.js` to 38. The two specimens do not disappear, because each variant
  still has to be shown: they re-point at `dialog` in `specimens/index.json`, and gate 8 caught the
  cross-reference left behind when only one of the two was repointed. `inventory.md` healed itself,
  because it derives the file and page cells from the classes named in each row.
- **Levels and order did not move.** `CONTAINS(dialog)` is unchanged, so `dialog` stays an organism;
  nothing holds `signin` or `outcome-dialog`, so no other level shifts. `index.css` was rewritten
  from `_levels.py --order` and gate 23 re-derives it.
- **Not merged, with the reason on the record.** `bet-sheet` has no top band, no close button and a
  `.sheet-grab` instead: a different zone set, so a different component, and the 3 rules for it
  inside `dialog.css` are now a misplacement rather than a variant. `toast` and `notice` do not merge
  either, and in both directions: the toast has a close and no actions, the push banner has actions
  and no close. `hiw-dialog` has the same anatomy and is still separate, because folding it moves 52
  rules across nine files rather than four across none, and that deserves its own measurement.

---

## 2026-08-02 - The level, the cascade order, and the panel that was grouped by the wrong question

Three artifacts had the same missing input. `components/index.css` was ordered by insertion, the
vitrine's side panel was grouped by purpose, and `ui-kit/docs/inventory.md` had no level column. All
three want one fact: what is this component made of. It is now computed once, in
**`ui-kit/_levels.py`**, and read by all three.

- **A level is arithmetic, not an opinion.** `level = 1 + the highest level of what the component
  CONTAINS`, ceiling 3, so a dialog holding a form stays an organism instead of inventing a fourth
  level. **36 components: 6 atoms, 9 molecules, 21 organisms**, plus two that are not composed of
  anything (`base` is the page frame, `course-chrome` is the course sidebar, which the inventory had
  already said on its own row). Typing that into the markdown would have made the table a second
  source for a fact the markup answers, which is the pair step 7c closed between coverage.md and the
  css headers, so `_fill_inventory.py` writes the column and the level never has to be maintained.
- **Containment is read from the specimen DOM, and only from the DESCENDANTS of the component's own
  root.** The first cut scanned class attributes flat and returned **33 organisms out of 38**, which
  is the tell that the measurement is wrong rather than the product. A specimen wraps its subject in
  the context it needs in order to render: the YES/NO pair sits inside a card inside the grid inside
  `main.feed`. **A flat scan reads ANCESTORS as contents.** The question is what stands inside the
  element this component owns, not what the page around it is.
- **Two things arithmetic cannot see**, declared in `RAISE`, one reason each, in the shape `SHARED`
  already uses: a block whose parts are all its own classes (the hero band is four blocks and 51
  classes, none of them another component's, so containment reads zero and it looks like an atom),
  and a **screen shell**, which is an organism because of what it is (the bottom nav holds nothing
  and is still the tab bar of every screen). A floor propagates, and it only ever goes up, because an
  error downward breaks the cascade and an error upward only makes a group less homogeneous. Raising
  the YES/NO pair to a molecule is what moved the option row that holds it to an organism.
- **The cascade was loading twenty five wholes ahead of their parts.** header before button, feed
  before card, card before both of the controls it holds. The order was the order the rules had been
  layered in inside the flat kit the system was read out of. **Nothing rendered wrong**, because step
  7b deleted every pair of files that write the same selector, and that is exactly why no sweep could
  see it: **a cascade defect is invisible until the day someone adds the rule that collides**, and
  then it presents as "my override does not work" three files away from its cause. The order is now a
  topological sort of containment, and among files that no constraint separates it keeps the order
  the file already had, because the smallest reordering that satisfies the rule is the one least
  likely to move a pixel. **Gate 23** re-derives it and compares, the way gate 21 does with the
  documents: a file can be newer than its source and still be wrong.
- **One cycle had to be declared rather than resolved.** The tab strip holds the comments panel and
  the comments panel holds a segmented switcher, and every switcher in the product is written in
  `tabs.css`. A cycle has no topological order, so `ORDER_BREAK` drops that one edge with its reason.
  It is dropped **for ordering only**: the edge is real, so it still counts toward the level and
  comments stays an organism. Which is the other half of a finding already on the record - `.seg` is
  a control that lives in the tab file because that file owns every switcher, and the same is true of
  `.grid-l`, the CHART's grid line, declared in `feed.css`.
- **The panel was grouped by purpose, which is the right way to group a product and the wrong way to
  group a system.** A group named for where a thing is used answers a question the screens already
  answer, and it put a button next to a sign-in dialog because both appear in a form. Grouped by
  level it answers the question a system has instead, which is what may be built out of what, and
  reading it top to bottom is reading `index.css`. Derived from the same map, so there is no second
  list to keep in step.
- **The column had to go in the generator, and where it goes in the row is a rule too.** `Level`
  sits after `Page`. Before `CSS file` it would have broken the file exactly the way step 7c did: the
  header strip tests `cells[1] == "CSS file"`, the test would stop matching, and the header would
  grow two cells a run. The strip is now written by SHAPE rather than by counting, because the table
  shipped for a whole stage with two generated columns and a run that assumes three eats the first
  real cell of every row.
- **Verified.** Product **503 of 520 snapshots identical to the property, 0 elements changed**;
  vitrine specimens **305 of 310 identical**. The rest are the mobile sheet caught mid-rise, and they
  differ by the same amount between two snapshots of an **unchanged** tree, which is how that was
  established rather than assumed. The OWNER map does not move under the new cascade (the cascade is
  its tie-break, so a reorder could have changed which file owns a class, and therefore the levels
  themselves; measured: 0 classes change owner). Gate 23 tested by injecting drift. All generators
  reach a fixed point in one round. **Gates: 23.**
- **Measured again on the screens where the moved components are actually painted.** The first
  verification ran on the five densest product screens, and the components the reorder moved furthest
  are exactly the ones those screens do not show: a dialog is present in the markup of all 104 screens
  and closed on nearly all of them, so **a class in the markup proves nothing**. Method: two passes,
  `git show HEAD:components/index.css` against the new file, full height, 360 and 1280, first as
  full-page pixels and then element by element on 35 computed properties plus the box. Result, the
  five base screens: **10 of 10 pairs pixel identical**, and `active-bets` **0 of 624 elements
  changed** at both widths. Result, nine state screens chosen so that each of the eight most-moved
  components is *painted* on at least one of them (`sign-in` and `win` for the dialog skin,
  `how-it-works` for the how-it-works dialog, `win` for the outcome dialog, `event-feed-loading` for
  the skeleton, `deposit` and `event-detail-bet-reconcile` for the notice family, `toasts`,
  `event-feed-empty` for the state block, plus `cookie-consent`): **0 of 11,914 measured elements
  changed**. Visibility was asked of the rendered box, not of the class attribute, for the reason
  above.
- **The one difference that showed up was in the capture, not in the product.** The first pass
  reported `active-bets` at 360 differing by 7,814 pixels. Shooting the SAME file twice reproduced
  the same 7,814 in the same rectangle, and the old file then matched a later shot of the new file at
  zero, which is what turned it from a finding into an artifact. The cause: `aside.sidebar` is
  `position:fixed` and is assembled by a run-time script, and a full-page capture paints a fixed
  element once, so a frame taken mid-build lands the panel half assembled. The cure is a **600 ms
  settle after `document.fonts.ready`**, applied identically to both passes. Written here because the
  next run needs to know it; the twenty screenshots were deleted, since every pair was byte identical
  and a picture proves nothing a row of numbers does not.

---

## 2026-07-28 - Stage 09, step 9: one panel, and the region no gate could see into

Started as a question about looks, why the two side panels look and work differently, and the answer
was not in the stylesheet: they are painted by one file and share every class name. **Twenty
findings, all closed.** Full record in `ui-kit/docs/architecture.md`, "What step 9 settled".

- **A gate that masks a region cannot see into it.** Gate 1 masks the `<aside>` when it asks whether
  a painted screen moved, correctly, because the panel is chrome and not the screen, and that made
  the panel the one thing nothing read. **Forty screens marked the wrong page as "you are here":**
  every category page and every feed state said `Event Feed -> success`. The cause is the shape this
  repo keeps meeting, `_apply_theme.py` and `_gen_category.py` build a screen from the finished
  Event Feed and swap the regions that differ, so **a new screen arrives carrying the shell's idea
  of where it is** and nobody re-ran `_resync_sidebar.py` after step 8. **Gate 22** is four checks:
  every screen marks its own file, every panel is what its generator would write today, every stand
  page names itself against the registry, and a page off the tree is still linked.
- **The thing that navigates was drawn quieter than the thing that does not.** A family name was a
  `.sidebar-page-link` with no href (13px, hover highlight, pointer cursor, no destination, 14 per
  screen on 105 screens) and the screen it named was a quiet nested row; in the vitrine those two
  classes mean the opposite. One vocabulary now: a **label** names a run of rows and opens nothing
  (`.sidebar-divider`, `.sub` when nested; `.sidebar-sub-head` deleted, and it had been drawn HEAVIER
  than the label above it, so depth read backwards), a **row** that opens a page is a link, the page
  you are **on** is `.active` at either level in one colour, and the group you are **in** is marked
  on its label, which the vitrine did not have at all.
- **Quiet is a colour, not an opacity.** Both labels, the note and a planned stage were dimmed with
  `opacity`, and opacity fades text INTO its background: `--chrome-muted` is 5.03:1 on the panel and
  the same value at `opacity:.55` is **2.37:1**. Five places under AA for as long as the panel has
  existed, and **no sweep this repo has run could see them, because they all read
  `getComputedStyle().color`, which does not carry opacity.** The step-6b lesson one level deeper: a
  checker that reads the computed colour is still not reading the rendered one.
- **One behaviour, two machines, one string.** Marking the row and never showing it is most of the
  way to not marking it (4066px of tree in a 900px panel; on `toasts.html` the brass row sat 3813px
  down). Both panels reveal it on load from one string in `ui-visual/_panel_reveal.py`.
  **`scrollTop`, not `scrollIntoView`**: the panel is `position:fixed` and asking an element inside a
  fixed box to scroll itself into view lets the browser scroll THE PAGE. The script lives inside the
  `<aside>`, which is the span gate 1 masks, so a panel can gain behaviour without 105 screens
  reading as product changes.
- **One component, seven descriptions.** The 28 course pages never linked the system file: 41 to 43
  rules each in **five distinct copies**, plus a sixth block injected by `_unify_sidebar.py` to force
  a violet palette. That is also why the four `.planned` rules had no markup in any tree
  `course-chrome.css` reaches: **the only panel with a planned row was the one it did not paint.**
  `_course_chrome.py` deletes the copies and the override, renames the drawer to the system's classes
  (its script addresses the elements by id, so only the paint moves) and links `fonts.css`,
  `tokens.css`, `course-chrome.css` last in `<head>`. `_unify_sidebar.py` deleted. Two things
  checked and not assumed: the course pages declare 14 variables against tokens.css's 348 and the
  sets **do not intersect at all**, so linking tokens cannot repaint their content; and the z ladder
  had to move together, because their 199/200/201 against the system's 8/9/10 would have opened the
  panel behind its own scrim.
- **A component that changes with the page it stands on is not a component**, so `.sidebar` names its
  own font instead of inheriting Inter on a course page.
- **A comment is not a rule, and a quotation is not an element.** Writing those comments broke the
  vitrine's own coverage table and exposed two defects in it: `parse_component` cut only the header
  comment, so `.css` and `.color` sat in the deletion-candidate list harvested out of the words
  "components/index.css" and "Colour goes through a role", and the kit bucket read the specimens and
  `kit.html` but not the 46 stand pages, so a class carried only by the vitrine's chrome fell through
  every bucket. **Deletion candidates: 28 to 2**, on a list step 7 acted on.
- Also: `.ck-note-link` moved from `ui-kit/_page.css` into `.sidebar-note a`, because a link in the
  note is the panel's own and it had been rendering in the browser's blue everywhere the vitrine's
  stylesheet is not loaded; a planned stage is a `<span>`; the tree is a named `<nav>` in all three
  panels; the note's mention of ui-kit is a link, so the way in exists in both directions, with no
  new copy written; `resync_sidebar.py` stops writing panel css, which it had been inserting into the
  page's own sheet reading `var(--accent)`, that page's violet; and `mark_group` lives in one file
  and is imported by the other, because for one turn the two tools each had their own idea of the
  mark and undid each other for ever.
- **One checker's own defect, recorded:** the light-theme sweep reported 105 failures at 1.12:1 and
  they were the `<script>` the reveal added inside the `<aside>`, counted as text. On graphite a
  script inherits light ink and passes; the moment the ground inverts it reads dark on dark. **A
  checker with a missing guard fails in one theme and looks exactly like a finding.**
- **Verified:** the panel in both trees and both themes, 308 loads, **18028 text pairs, 0 below AA**
  with opacity composited, 0 browser-blue, 0 overflow, 0 page errors, on a sweep calibrated first
  against a pair whose answer is known; the reveal on 153 panels at two viewport heights, **0 with
  the mark out of view, 0 documents scrolled**; the course pages, **795 text pairs, 0 below AA, 0
  dead anchors, 0 violet left**, one shape on all 28; their own content compared element by element
  against a worktree of HEAD, **28 of 28 identical**; **348 pages, 35773 internal links, 0 broken**.
  Gate 22 tested by injecting each of its four kinds of drift; all six generators reach a fixed point
  together over three rounds. **Gates: 22.**

### Where the audit passes stopped (written 2026-07-28)

Nine passes ran over this stage (7, 7b, 7c, 7d, 7e, 7f, 8, 8b, 9), yielding 34, 14, 24, 11, 10, 8,
15, 9 and 20 findings. **That sequence does not decay, and that is the argument for stopping rather
than running a tenth.** A pass re-reading a region it had already read would tail off; each of these
instead found a region nobody had read. Yield tracked unread surface, not effort, and the surfaces
with nothing pointed at them are now countable. That list moved to [`backlog.md`](./backlog.md).

Not a defect list: no entry is a known bug, each is a place a bug would be invisible. And not a
claim that accessibility is undone, which was checked before the table was written because a large
hole there would have changed the answer: **0 buttons without an accessible name** across 105
screens, every `<img>` with `alt`, native `<dialog>` supplying `aria-modal` and inerting the page,
tab strips as radio groups that arrow keys already drive. The one real gap is the announcement, and
a toast is a state, so Stage 10 owns it.

---

## 2026-07-28 - Stage 09, step 8b: the documents, the skin, and the sheet that could not scroll

One item was on a list and two came from looking at the product. **Nine findings, all closed.** Full
record in `ui-kit/docs/architecture.md`, "What step 8b settled".

- **A document nobody can open is not documentation.** Every stage renders its reasoning
  (`ia/docs/sitemap.md` -> `ia/sitemap.html`); Stage 09 was the one that did not, and its four
  documents are 144 KB. Worse, the vitrine already LINKED one: **39 component pages pointed at
  `docs/coverage.md`**, a href into a file the browser downloads instead of drawing. They are pages of
  the vitrine now (`ui-kit/_gen_docs.py`), painted by the system they describe, with a contents rail,
  a swatch beside every colour literal and a link on every file name the vitrine has a page for.
  Generated, because these documents change every step and a hand copy is stale by the next one;
  **gate 21** re-renders in memory and compares, because a file can be newer than its source and still
  be wrong, and fails on any link into a raw `.md`. Run `_gen_component_pages.py` first: it writes
  `docs/coverage.md`. The long read also found that **a section label is not a heading** - `.tk-sec>h2`
  is small brass capitals, right over a specimen and wrong seventeen times down a page.
- **A gate that compares the body certifies the body.** Gate 19 has guarded the Sign In / Deposit fork
  since step 7f by comparing the sheet BODY, and the fork left was on the element the body hangs from:
  all 17 standalone overlay pages carried `outcome-dialog`, which is the RESULT skin (`dialog.css`
  splits the head on it and only `:not(.outcome-dialog)` gets the brass-lit plate). **The sign-in sheet
  a person actually opens had the flat result head while the same sheet on the other 75 screens had
  the lit one.** A skin is named for what the sheet IS: sign-in and deposit take the shared dialog's
  own class list, win and loss keep theirs. Computed in `_unify_dialogs.py` from the canonical dialog,
  with the family read from the page NAME, because **a rule that can only recognise its own input
  before it has run once is not idempotent**. Gate 19 compares the skin now.
- **A modal is bounded by the viewport, so it has to be able to scroll.** The user agent gives
  `dialog:modal` both `max-height` and `overflow:auto`; `dialog.app-dialog{overflow:clip}` took the
  second away. At 1280x620 the deposit sheet was cut with its **Add funds** button 116px past the edge
  and nothing to scroll; the how-it-works sheet was unreachable below 900px of viewport at any width.
  This is step 7's finding read backwards: there `overflow:hidden` was wrong for making a decorative
  box a scroll container, here `overflow:clip` is wrong for stopping a box that has to be one. **Clip
  decoration, or contain content** - one question, one property. The frame clips and the BODY scrolls,
  so the head and the close stay put. Verified as the question a person asks: **64 sheet-and-viewport
  combinations, last control reachable in all 64.**
- **Three checkers were reading text as markup**, all surfaced by the documents: the renderer left the
  quote unescaped, so a code block quoting `<link ... href="_theme.css">` failed gates 4 and 9; gate 4
  also read a `url()` inside a `<pre>` (**text inside `<code>` or `<pre>` is a quotation, not a
  reference**, which the component pages needed too, since each ends with its own source); and gate 20
  searched the whole text for a font host, so the page explaining why the host was dropped failed the
  gate that exists because of it (**a mention is not a call** - ask a `src`/`href` attribute and an
  `@import`).
- **A colour follows the surface it stands on.** The course sidebar keeps one dark palette in both
  grounds, and `.ck-note-link` inside it read `--text-brass`, which in daylight is the dark brass for a
  pale surface: **2.39:1 in the light theme on every page of the vitrine**. One role, `--chrome-accent`.
  The vitrine's sub-AA pairs went 434 to 158, all that is left being `kit.html` (frozen) and the value
  labels drawn ON their own swatches in `tokens.html`.
- Also: `ui-kit/fonts.html` existed because step 8 taught gate 2 that fonts is not a component with a
  stand and did not teach the page generator; the `Stands on:` header of 24 component files still said
  76 screens; and `.outcome-dialog a{text-decoration:none}` had been paying for another skin's markup
  (**a link that wraps a control is not a text link**, now in `dialog.css` for both trees).
- **One measure for the page** (reported by eye at a wide window). `--container-max` is 1400 and only
  the footer obeyed it: at 1920 the content ran 1620 while the footer under it stopped at 1400. Five
  bands carried `max-width:none` from the colour pass and read the token now, so the band spans the
  window and what is inside it (header row, category strip, trust bar, content, footer) shares one
  left edge.
- **An empty box is invisible to every sweep we run.** The four category pages and two feed states had
  a 56px photograph box with no photograph, because step 7c moved the picture out of
  `.grid > .card:nth-of-type(N) .thumb` onto the element and reached the pages that exist as files,
  not the cards a generator writes. **A missing picture passes a contrast sweep, an overflow sweep and
  a link check alike**; gate 9 asks for it now. The library has one photograph per category, so what
  varies on a single-category page is the CROP of it. And **a photograph is not one declaration**: the
  port stripped `background-image` on the way into grey and let `background-position` through, which
  is the framing of a picture that is not there.
- **A control is named by what it does.** The Event Feed had two controls doing the same thing: the
  top band navigates (a category is its own indexed URL), and the chip row labelled "Filter events by
  category" was five more links to the same pages, so pressing Politics inside Trending left Trending.
  It filters in place now (`wireframes/_generators/subfilter.py`, both trees, `data-cat` read out of
  the photograph each card already carries). Three shapes came with it: **hidden is a state, not a
  style** (the attribute was set and nothing moved, because `.card{display:flex}` beats the user
  agent's `display:none` whatever the specificity, so `base.css` carries the one `!important` in
  `components/`); **a checker that reads the attribute does not read the page** (the first run
  reported success while twelve cards were on screen); and **two generators writing into one sheet
  have to know where each other's work ends**, the step-7e lesson, paid for again when `port_chrome`
  and `subfilter` rewrote the same page back and forth forever.
- **A container holds its inset at every width.** Centring the content band by turning
  `margin:var(--gutter)` into `margin:var(--gutter) auto` spent the horizontal gutter on the centring,
  so under 1400 the plate sat against the window edge. The inset is padding; above the cap the auto
  margin centres. Measured at eight widths from 1920 to 380: header, content, plate and footer on one
  x at every one, gutter 40 above 640 and 14 below.
- **Half of twelve is six.** The two bars of the close X sat at `calc(50% - 7px)`, one pixel left of
  the disc, on every close button in the product. The vertical half was right, which is what made it
  hard to see.
- **Verified:** painted **420 page loads x 2 themes, 86534 text pairs, 0 below AA, 0 overflow, 0 page
  errors**; the vitrine 196 loads in both themes, every remaining failure present at HEAD; standalone
  dialog against shared, matched by class, **0 differences that paint**. Gates 19 and 21 tested by
  injecting the drift they exist to catch. **Gates: 21.**

---

## 2026-07-28 - Stage 09, step 8: the coverage pass, and the family no gate could see

Run against the three things step 7f left open (an overlay contradicting its own convention, a font
host called before consent, a note that the trees disagreed about how many category screens exist),
and the third one turned out to be the largest hole this stage has found. **Fifteen findings, all
closed.** Full record in `ui-kit/docs/architecture.md`, "What step 8 settled".

- **A pair that does not exist is not a pair that agrees.** Gate 18 pairs the trees by FILENAME, and
  one family does not share filenames: a category page is `politics.html` in grey and
  `event-feed-politics.html` in colour. The gate skipped every unpaired page in silence, so **32 grey
  category screens sat against 4 painted ones** and the family drifted through two stages with every
  gate green. Zero drift out of zero pairs reads exactly like zero drift out of all of them. The map
  is now **`_twins.py`** at the root, one copy for six tools and the gate; it had existed in FIVE
  hand-written copies, and the four that only knew the BASE pages are why nobody noticed. Gate 18
  gained **every screen has a twin**, one declared exception (`overview.html`). The 28 missing
  screens are built by `ui-visual/_apply_theme.py`, generalized from the Event Feed's state
  generator: a category page is the same listing with one filter on it, so it is the same machine
  with a different shell, not a second generator.
- **An anchor another tool can remove is not an anchor.** `_apply_theme.py` built the stone plate by
  finding `<div class="feed-inner">` in the grey fragment, and step 7d's port unwraps plate wrappers
  on the way into grey, so the anchor had stopped matching and the next run would have shipped eight
  state pages with no plate. `_gen_category.py` had the same defect one function away and it had
  already fired: its heading substitution read `<h2 id="feedHeading">` and step 7b made that an
  `<h1>`, so one re-run put the shell's **"Trending"** on all four category pages and silenced the
  sub-category rail, which picks its list by the heading's text.
- **A category page owes its own SEO body, not the home page's.** `seo.md` section 3B lists "About
  {category} events" as the category template's fourth H2; the painted pages had inherited the feed's
  two generic sections instead, the same text on all five URLs, which section E of the same spec
  forbids. The copy is read out of the grey twin at generation time, because a generator that types a
  sentence is a second source for it.
- **A listing does not change its contents when nobody is signed in.** The logged-out category state
  was built from a grey card set drawn in Stage 05: no `.top-txt`, so no story-led "why", and YES/NO
  a logged-out person could not press, in a product whose whole inversion is that you browse and
  build a bet before the gate. And **nobody signed in has saved anything**: a pressed bookmark shipped
  on five logged-out screens in both trees, the filled brass mark meaning "this is in your
  Favorites", to a visitor whose header offers them Sign up.
- **A missing colour is a colour, on a control this time.** Every colour in `yesno.css` hung off
  `> a`, so a `.yesno` whose buttons are not wrapped in an anchor fell back to the user agent's
  `buttontext`: near black on graphite, **1.42:1**. **A side is a POSITION IN THE PAIR, not a fact
  about being wrapped in a link.**
- **A frame rule reached a dialog.** `.app-case{position:relative}` in `base.css` took back the user
  agent's `position:fixed` for `dialog:modal` on the 17 standalone overlay pages, which put the app
  frame class on the `<dialog>` itself, so the sheet scrolled off the top with the page behind it.
- **The bottom sheet came back, and it is geometry, not markup.** Under 640px an invoked dialog is
  full width on the bottom edge, top corners rounded, rising into place, head fixed and body
  scrolling; above 640px nothing changed. **`:modal`, not `[open]`**, because a standalone overlay
  page opens its dialog as the page it IS and a sheet that rises over nothing is a page that jumps on
  load, and because **an author declaration beats a UA one whatever the specificity**, so a bare
  `display:flex` would have opened every dialog on 76 screens at once. No grab handle: the grey tree
  draws one and drag-to-dismiss is not built. (This closes the step-7e note that "bottom sheet on
  mobile ships only in grey".)
- **Where a font comes from is a decision.** The three families are served from this repo now: 18
  woff2 files (latin + latin-ext, `font-display:swap`) in `assets/fonts/`, declared once in
  `components/fonts.css`. **Gate 20 is three checks**, because the defect returns three ways: a page
  re-adding the tag, a GENERATOR re-adding it to every page it writes (five had it in a template),
  and an `@font-face` naming a file nobody committed. (This closes the step-7b note that self-hosting
  was "an open decision, not a silent default".)
- **Verified:** painted 105 screens x 2 themes x {380, 1280} = **420 page loads, 86534 text pairs, 0
  below AA, 0 overflow, 0 page errors**; grey 104 x 2 widths, **0 overflow, 0 errors, 0 non-neutral
  colour** (its 1212 sub-AA pairs are the screen-tree drawer's own notes and the identical count comes
  off a worktree of the previous commit). **16770 grey + 15535 painted links, 0 broken.** The sweep's
  first cut reported 116 sub-AA pairs and 4690 overflowing elements; calibrating it on three
  known-good pages returned 0 and 438, so the overflow question is asked of the DOCUMENT now and the
  116 turned out to be real. **A measurement not checked against a known-good case is a claim, not a
  proof. Gates: 20.**

---

## 2026-07-28 - Stage 09, step 7f: one dialog, one copy, and scope as a place

Found by looking at the product instead of the build: the sign-in dialog on `ui-visual/sign-in.html`
did not look like the sign-in dialog on every other screen. **A screen can disagree with its grey
twin, and it can also disagree with its own second copy in the same tree, and only the first of those
was ever checked.** Full record in `ui-kit/docs/architecture.md`, "What step 7f settled".

- **A dialog that also has a page has two copies.** Sign In and Deposit each exist as the shared
  `<dialog>` on all 76 painted screens AND as the standalone page that IS that dialog. Stage 08
  painted the shared copy and left the standalone on the grey generator's markup, so **the page a
  person actually opens carried the wireframe placeholders, the one standing in for Google being a
  circle with a plus in it**, while the shared dialog carried the real brand marks. Four copies of
  that body existed in the repo and all four differed.
- **"The newer copy wins" would have deleted the best thing on the screen.** The standalone Deposit
  had three things the shared one had lost: a label over the payment widget, the sentence saying card
  payments are converted via Transak, and **an exit to How It Works, which is the trust affordance
  that screen exists to earn**. Merged element by element, then one markup from there
  (`ui-visual/_unify_dialogs.py`). **Gate 19** fails the build when it drifts again, in either tree,
  and checks the marks by name, because `shape()` drops `<path>` and `<circle>` and so cannot see
  that a button is drawing the wrong logo.
- **Scope is where a block may stand.** The How It Works page rendered as an unstyled document
  because every rule for the hero, the icon chips and the FAQ list began `.app-dialog.hiw-dialog`:
  the page the dialog links to as "the full guide" could not reach one of them. A rule that describes
  a BLOCK is now written unscoped; only what is about being a dialog keeps the ancestor.
- **A page is not a bigger dialog.** The page was composed, not re-marked: page text size instead of
  a sheet's 13px, sections apart instead of stacked, and the brand tile and the resolved-events count
  moved into a side column, because **a claim and its proof belong beside the argument, not after
  it**. It also gained what a page called How It Works owed a reader and did not have: how to place a
  bet. One line of copy written (Step 27 in `microcopy.md`), the rest already shipped.
- Also: the heading `Proven, not promised` had been sitting in a `<section>` **with nothing in it**,
  above three numbers in a different element; `.app-case .hiw-sec > :is(h2,h3)` from step 7c stopped
  matching the moment the heading moved, a fossil created by the fix for a fossil; and `.hiw-sec`
  joined `port_structure.RESTYLE`, because **"already styled" is the wrong question when the markup
  changed shape** and the wireframe was drawing the chip above the heading in a layout that puts it
  beside.
- **Two checkers reported their own defects**, both mine: gate 19's first cut asked for "the first
  `<dialog>` in the document" and got the shared sign-in sheet that every standalone page embeds
  first, so **a page with several of a thing has to be asked by id**; and `_unify_dialogs.py` had to
  be told that a button with no mark keeps none, since swapping a placeholder for the real logo ends
  a fork but putting a logo on a control that never had one starts a design decision.
- **Verified:** both trees at 380 and 1280, grey 0 overflow / 0 errors / 0 colour outside the
  palette, painted 0 below AA in both themes, 0 broken links either side. Gate 19 tested by injecting
  each of its three kinds of drift. **Gates: 19.**

---

## 2026-07-28 - Stage 09, step 7e: the other three regions, and a gate that certified one

Step 7d put a gate behind "wireframes/ owns structure", and that gate compared `<main>`. **A gate
that reads one region of a page certifies one region of a page**: the header, the bottom nav and the
footer stayed the one place two trees could drift with every gate green, and they had. Ten findings,
all closed, two of them the tools' own. Full record in `ui-kit/docs/architecture.md`, "What step 7e
settled".

- **The drift ran both ways, so the fix is two tools in a fixed order.** The paint got the SHAPE
  right and the STATE wrong; the grey tree got the state right and the shape wrong. Reading that as
  "one tree is behind" is what makes a one-directional port write the wrong answer into 104 files.
  **The paint owns the shape of the chrome; the grey tree owns which state it is in.**
  `ui-visual/_reconcile_chrome.py` gives the paint back three state facts, then
  `wireframes/_generators/port_chrome.py` copies the corrected shape back.
  The paint had `aria-current="page"` on the **Events** slot of all 76 painted screens whatever
  screen it was (the grey tree marks 54 Events / 9 My Bets / 3 Favorites / 6 Portfolio / 15 none, and
  the painted Wallet screen was announcing "Events, current page"); a logged-in header over a bottom
  nav pointing home at `event-feed-logged-out.html` on ten screens, one chrome disagreeing with
  itself about whether anybody is signed in; and three unread notifications in the dropdown of the
  three screens whose whole subject is that a new user has nothing yet. The grey tree had no
  `.cat-condensed` at all (the category strip that slides into the sticky header, a whole navigation
  control, on 68 painted screens and 0 grey), the footer trust block as three bare sentences, and a
  `<span>` pretending to be the deposit amount field.
- **An auth variant was not a fact to read, it was a decision to make.** Ten screens disagreed and
  neither tree is a copy of the other, so each is answered by a reason, written once: `how-it-works`
  + `public-profile` x4 logged OUT (documented as pre-auth since Stage 08), `cookie-consent` because
  a consent banner IS a first visit, `maintenance` because the app is down and there is no session to
  read; `404`, `500`, `toasts` logged IN, because showing a signed-in person Sign in / Sign up turns
  "this page is missing" into "you were logged out".
- **A port copies markup, and a href IS markup.** The category pages are `event-feed-politics.html`
  in colour and `politics.html` in grey, and step 7d carried the painted hrefs across with the
  markup: **110 links in the grey tree pointed at files that do not exist there**, while the link
  check run at the time counted links instead of resolving targets.
- **A missing colour is a colour**, twice, and both are the step-6b theme lesson from the other side:
  a checker that reads the source cannot see a value the browser supplies. The grey sheet styles a
  link in fourteen scoped places and never as a bare element, so every `<a>` outside them rendered in
  the user agent's `#0000EE`: **992 computed colour values** in a tree whose contract opens with
  "neutral greys only" and whose source has 0 non-neutral hex. And `fill`/`stroke` are not in the
  port's KEEP list, so **the feed hero chart has been a solid black rectangle since step 7d**, since
  an SVG with no fill is black.
- **Where a rule may reach, part two.** Gate 14 counted `wireframes/*.html` as markup for
  `components/`, which cannot apply to it (the grey tree has its own inline css and never links
  `index.css`). Four rules lived on that mistake and are deleted. **A class carried only by the tree a
  stylesheet cannot see is a class it does not have.**
- **Two boundaries added, six now** (`wireframes/_conventions.md`): the `TBD` chip, because a
  wireframe is obliged to mark an unbuilt destination and a product must not show a user the
  bookkeeping; and the page behind an invoked overlay, which convention 5 has specified since the
  wireframes were built. That sixth one is **checked rather than skipped**: grey must carry no chrome
  on those 17 screens and the paint must carry all of it.
- **Two tool bugs, one shape.** An idempotent generator has to be idempotent about whitespace: **the
  removal has to be the exact inverse of the insertion**, and getting it approximately right cost 74
  pages on one re-run and 13 on the next. And a painted overlay page carries four dialogs with the
  shared ones first, so "the first `.sheet-body`" is the sign-in provider list on all 17: the port
  wrote sign-in buttons into the grey Win, Loss and Deposit wireframes, caught by eye in a
  screenshot. A screen's own overlay has an id, and the tool now checks both trees give the sheet the
  same `aria-label` before copying. Also: two generators writing into one `<style>` have to know
  where each other's work ends, or one silently deletes the other (72 pages).
- **Not fixed, on purpose:** the paint made the invoked overlay a centred modal at BOTH breakpoints,
  so "bottom sheet on mobile" ships only in grey. A product decision, recorded beside the convention
  it contradicts. *(Closed in step 8: the sheet came back as geometry.)*
- **Verified:** grey 208 page loads at 380 and 1280 (**0 overflow, 0 page errors, 992 colour leaks ->
  0**); painted 308 page loads across both themes (**61956 text pairs, 0 below AA, 0 overflow**);
  **16597 grey links, 110 broken -> 0**. Gate 18 tested by injecting drift into each of the five
  compared regions in turn. All five tools reach their fixed point in one run. **Gates: 18.**

---

## 2026-07-28 - Stage 09, step 7d: the readiness pass, and the rule that had no gate

Run against the course's own "done when" list rather than as a defect hunt, which is why it found a
different kind of defect. **Eleven findings, nine closed, two of them my own measurement error.**
Full record in `ui-kit/docs/architecture.md`, "What step 7d settled".

- **A rule with no gate behind it is a preference.** `wireframes/` owns structure and copy has been
  written here since Stage 08 and nothing checked it, so Stage 08 **redesigned the Event Detail while
  painting it** and the redesign never came back: an AMM market panel with a price-by-size table, a
  chart rebuilt as head / plot / axis / range, a rules-and-context tab split, a share-and-save
  cluster, an odds bar, and a real `<input>` where the grey tree had a `<span>` pretending to be a
  field. 55 of 72 twinned `<main>` elements differed, Event Detail by 222 elements. Ported back by
  `wireframes/_generators/port_structure.py` (idempotent, reads the painted twin, never writes to
  `ui-visual/`), which derives the grey-box rules from `components/` by keeping what a rule PLACES
  and dropping every colour: **a grey box is the painted component with its finish scraped off.**
  **Gate 18** fails the build when the two trees disagree; the four differences that ARE the
  boundary are declared in `wireframes/_conventions.md` (plate wrappers, icon mechanism, photograph,
  and chart data, because a wireframe draws its data and a product computes it).
- **The copy inventory was not the source of truth for a whole stage.** 43 strings the product had
  been shipping since Stage 08 had no row in `voice/docs/microcopy.md`, including every label of the
  market panel and the line that keeps the context tab from being read as the resolution rule. Logged
  as Step 24. Two lines were opened as defects and closed as correct, and the first is the useful
  one: `Closes: Sep 1, 2027` looks like the product's only stray colon and the colon is a
  **delimiter** the feed script splits the meta row on. **A style rule that would break a script is a
  style rule with a missing fact in it.**
- **Four bugs in my own generator, each one a rule.** Splitting a selector list on commas cuts
  `:is(h2,h3)` in half, and a browser drops an unparseable rule AND everything after it in the sheet
  (the symptom was a chart axis rendering as running text). Deleting `@media` before reading a file
  deletes the layout, so the feed came out 14px wider than the phone it was drawn for. "Already
  styled" is the wrong question when the markup moved. A selector naming a scope the target tree does
  not have can never match.
- **A photograph travels two ways.** `background-image` was stripped and `<img>` was not, so four
  pictures entered a tree with zero image elements across 104 pages, one of them 1400px wide.
- **Two findings were my own measurement error**, recorded because a false positive costs the same
  attention as a real one: a case-sensitive scan called six documented token coincidences
  undocumented. **A checker that has not been run against a case it should pass is not a checker.**
- **Gate 17**, the other direction of gate 3: 14 marks stood on screens and were on no sheet,
  including the chevron at 176 uses and the three sign-in brand marks, because step 7c collected
  icons with a regex wanting `class="ic"` as the first attribute. An `<svg>` on a screen is either a
  MARK or a drawing of DATA; there are two drawings. One checkmark drawn two ways is now drawn one.
- Also: the eleven `--z-*` tokens are now a section of `tokens.html`, drawn as a stack written
  **highest first** so only the tokens can produce the right picture; the field gained a rendered
  state set (`input-states`), and its first cut on the bare canvas rendered four white boxes because
  every rule in `input.css` is scoped under `dialog.app-dialog`; the roadmap sidebar was true in
  `LAYOUT` and false on 21 pages that keep their own copy, fixed by `_resync_roadmap.py`; and
  `.chart-wrap` / `.chart-cap` died the moment the port took the last markup they could match, which
  is a fossil pair working as intended.
- **Verified:** 104 grey pages at 380 and 1280, **0 horizontal overflow, 0 page errors, 0 colour
  outside the wireframe palette**, against the same sweep run on a worktree of the previous commit.
  Structural parity 55 of 55. Gate 18 was tested by injecting drift and confirming it fails.
  **Gates: 18.** (The colour claim was read out of the SOURCE and step 7e re-read it out of the
  BROWSER, where it was false; see the step-7e entry.)

---

## 2026-07-28 - Stage 09, step 7c: the third audit, on a build where every gate was green

Run against `components/`, `ui-kit/` and all 77 painted screens, plus `/impeccable audit` (16/20
Good, no AI tells). **24 findings, 23 closed, 1 recorded as a decision.** Full record with the
reasoning in `ui-kit/docs/architecture.md`, "What step 7c settled". What changed a rule:

- **A generator that is not idempotent on all of its row kinds is not idempotent.**
  `_fill_inventory.py` stripped its own columns from data rows and not from headers, so the header
  grew two cells a run: seven runs later every table in `inventory.md` had a 21-cell header over
  9-cell rows and none of them rendered.
- **A class a file mentions is not a class it owns.** `coverage.md` said 76 screens for 34 of 36
  components, because `market.css` styles `.market-title .ic` and `.ic` is on every screen. Ownership
  is now the file that styles a class with the fewest ancestors (ties to cascade order) plus a
  five-word hand-checked SHARED list. The same map writes the `Classes:` and `Stands on:` lines in
  each css header, which were prose someone typed once and had been telling the truth while
  coverage.md said 76. **Two artifacts of one system disagreeing is the defect; one computation
  feeding both is the fix.**
- **A distance is not a measurement.** The rule was written in step 6 and 57 declarations broke it,
  because the measurement scale shipped with two steps (56, 72) and the product needs twelve. A rule
  with no scale behind it cannot be followed. `--size-2 .. --size-72` now, and **gate 12 fails on a
  `--space-*` step in a width, height or flex basis**, which the raw-value check cannot see.
- **Removing an `!important` means ending the argument, not deleting the word.** `.grid` carried one,
  and dropping it let `.cat-main .grid` win: the category pages would have changed their column
  track. Four rules above it were already dead (three breakpoints losing on source order, the
  category variant losing to the shout). Deleting the four made the shout removable without moving a
  card.
- **A rule applied to two files is not applied.** Step 7 moved touch targets to `pointer:coarse` and
  reached `catnav` and `header`; six components still bound 44px to `max-width:640px`, so a touch
  tablet above 640px got the 36px control, the exact device the rule was written for. Measured after:
  coarse pointer at 380 and at 1280, every control 44px; fine pointer 36, which clears 2.5.8.
- **Structure is owned by `wireframes/`, so fixing only the paint leaves the owner wrong.** Step 7b
  reported "heading skips across the painted tree: 0" and the grey tree, which owns structure, still
  had an h1-to-h3 jump on 46 pages and no `<h1>` on 19. **Gate 15 reads both trees.** Footer columns
  went h3 to h2 in both; the Event Detail column heads went h4 to h3, which made them match the
  `.ed-section` label rule, so that rule became a CHILD selector (**a section label is the section's
  own heading, not any heading inside it**); the 17 dialog-host screens took the `<h1>` from the
  heading their own dialog already carries, so no copy was invented. The two Event Detail loading
  skeletons keep none on purpose and gate 15 names them.
- **A UI string is not a style hook.** `[aria-label="Track record"]` carried seven rules, so the
  profile reputation grid hung off an English phrase owned by `voice/`. Now `.pos-record`.
  `[aria-current="page"]` stays: a state attribute is a state.
- **A promise made component by component is not made.** 14 files carried the identical
  `:focus-visible` rule, 24 did not, and there was no default. One rule in `base.css`, one new role
  (`--focus-ring`, split from `--text-brass`), three exceptions that say why.
- **Where the system layer may reach.** `components/` held 24 `url(../ui-visual/assets/...)`: the
  system depended on the product's screen folder. Assets are `assets/` at the root now. Sixteen of
  those were worse than a path: `.grid > .card:nth-of-type(1..12) .thumb` encoded WHICH feed card
  shows which photograph, and the event photograph belongs on the element by this file's own rule.
- Also: three stale comments in `tokens.css` (a note that outlived the defect it described, a pointer
  at a primitive merged away in step 6, a role promising a difference it never had, deleted); 12 of
  the 27 same-value role groups now say so; motion moved onto the declared duration scale (21 raw
  timings, none of which was a step); the vitrine's `_page.css` dropped 93 frozen Vault hex values;
  **`icons.html` gained the 29 icons the product DRAWS inline** beside the 15 it references from the
  sprite, because a vitrine that documents one of two mechanisms describes the smaller one; every
  stand page gained a `<main>` landmark; and gate 9's "nothing loads the flat kit" was repointed,
  since `kit.css` had already been deleted when it was written and it could not fail.
- **Gate 16 exists because this pass shipped a broken declaration.** A note appended to a token
  without its comment markers put bare prose inside `:root`; the browser dropped every declaration
  after it and the NO side of the outcome palette went transparent on 28 screens. Fifteen gates saw
  nothing; a 380-page snapshot did. Gate 16 walks every block in `components/` and fails on anything
  inside it that is not a declaration.
- **Recorded as a decision, not fixed:** 20 declarations build a colour with `color-mix(in oklab,
  var(--color-action) N%, ...)` at 16 different percentages, an undeclared second alpha ladder beside
  the declared `--brass-a*` one. Gate 13 is satisfied (all of them read a role). Which steps that
  ladder should have is a states question, and rounding them now would move hover and selected states
  for the legibility of the file rather than of the product. *(Open; see backlog.md.)*
- **Verified:** both trees, 5 widths, before and after, compared by what the browser reports as
  visible. 380 product snapshots, **0 with a different visible element count**; what moved was the
  asset URLs (same files) and two chart polylines caught mid-transition. 175 vitrine pages changed
  element count, all of them the corrected screen lists and the new icon section. Target size
  measured, not reasoned about: coarse pointer 44px at 380 and at 1280, fine pointer 36px. Then the
  whole product in both themes at 380 and 1280: **54774 text pairs, 0 below AA, 0 page errors, 0
  horizontal overflow.** Two earlier runs of that sweep were wrong (950 failures that were gradient
  buttons the checker could not read, then 405 that were a theme swap measured mid-transition):
  **a measurement not checked against a known-good case is a claim, not a proof.** **Gates: 16.**

---

## 2026-07-27 - Stage 09, step 7: the deletion pass, the defect table, the finish

Audited `components/` + `ui-kit/` + all 77 painted screens against the step-7 checklist and
`/impeccable audit` (16/20 Good). **34 findings, all closed.** The ones that changed a rule and not
just a line:

- **`overflow:hidden` makes a box scrollable, it only hides the bar.** Thirteen stones clip a
  decorative pseudo; one was actually scrolled (`.sheet-head`, `scrollLeft:52`), which dragged the
  win overlay heading out of its box and clipped it to "u were right" in both themes on 4 screens.
  All thirteen are `overflow:clip` now, which creates no scroll container. Sweep: 0 scrolled.
- **Target size follows the POINTER, not the viewport.** 44px was bound to `max-width:640px`, so a
  touch laptop got 36px. Now `@media(pointer:coarse)`; a fine pointer keeps 36, which clears
  2.5.8 (24x24). The card bookmark was 16x16 (fails both bars) and now carries a 44px box with a
  negative margin, so the target grew and not one pixel moved.
- **Reduced motion, once, in `base.css`** (3 of 23 components had a block; a promise is not made
  component by component).
- **A candidate is not an outcome:** the multi-outcome series drew line 1 in the YES green and
  line 3 in the lit brand brass. Green, red and gold are reserved; the series moved into the arc
  they leave free (cyan 187 -> magenta 328 + one neutral), all five >= 4.5:1 in both themes.
- **Two roles may share a value** (27 groups do): a role is a reason, not a value. The rule is
  written above section 2 and the coincidences are declared where they happen.
- **A third copy is a fork:** `shell.html` held its own hand-kept header next to `header.html` and
  76 screens; it composes the specimens now and holds no markup.
- Also: `.opt-row.sel` side-stripe -> tint (an impeccable absolute ban), 13px/19px icons onto the
  scale (`--icon-12` added), `--brass-800` orphan deleted with its gate exception, `.uv-bar` +
  its wireframe-era grey gone from 76 screens, the Favorites category bar restored from the grey
  twin (and its now-duplicate Category dropdown dropped), `<img>` given `width`/`height`/`lazy`.
- **Deleted:** `ui-visual/_theme.css` + `_theme-vault.css` (132 KB, unloaded since step 5) and the
  empty `tokens-components/`.
- **Living documents:** `inventory.md` gained **CSS file** and **Page** columns, filled for all 87
  component rows by `ui-kit/_fill_inventory.py` (class-matched against each file's `Classes:`
  header, so it stays true when a class moves); `coverage.md` records the decision on the six
  kit-only classes (all six stay, with the reason); `architecture.md` gained "What step 7 settled";
  `DESIGN.md` gained the two-level token section + the both-theme contrast table; `STRUCTURE.md`,
  `README.md` and the roadmap sidebar mark 08 and 09 Done.

---

## 2026-07-27 - Stage 09, step 7b: the second audit, and what a passing build hides

Run against `components/` and every painted screen on the premise that a system passing its own
gates is where the interesting defects live. **14 findings, all closed.** Contrast was already clean
in both themes and stayed clean; what the gates could not see was where the styling lived.

- **One element, one rule.** Step 1 read the styling off the painted product, and the product had
  TWO stylesheets on it: the grey-box skeleton written inline by the wireframe generator, and the
  Vault theme loaded after it. The extraction concatenated them, so **116 selectors were written
  twice and 200 declarations in the first layer rendered nowhere** (`loadmore.css` described one
  button twice over, nine properties apart). Deleted by `ui-kit/_unfork.py`, whose argument is that
  `.app-case S` is S plus one class and therefore always wins. **Five exceptions, measured not
  assumed:** the footer language menu and the shared `<dialog>`s live OUTSIDE `.app-case` (a dialog
  is appended at the end of the body, so it is a sibling), and for those the unprefixed rule is the
  shipped one. The first cut deduced instead of measuring, deleted the footer menu's padding, and
  the diff caught it in one run.
- **An attribute is a rule.** Gate 9 asked about `<style>` blocks, gate 12 looked inside
  `components/`, so **110 style attributes on 30 screens** were the one place neither looked: type,
  geometry (`width:72px` beside an existing `--size-72`), layout variants, and twelve places where a
  component was undone on the element. Half were already dead. Two explain an `!important`:
  `profile.css` and `state-block.css` were shouting to beat an inline style, and both stopped.
  **An `!important` is usually a fossil of something no longer there.** Gate 9 reads attributes now
  (`ui-visual/_destyle.py`).
- **Hidden is not gone.** Every painted screen carried the wireframe's screen-tree drawer, about
  150 links hidden by one `display:none`: **1024 KB, 16 per cent of all HTML in `ui-visual/`**, a
  second and invisible navigation on a page that has its own. `base.css` was carrying 25 rules to
  style a drawer it also hid, plus `.device` four times and `body` three, each undoing the last;
  117 lines to 66. Removed by `ui-visual/_strip_wireframe.py`; the record stays in `wireframes/`,
  which owns structure.
- **A stacking order is a list, so it is written as one.** 0 1 2 3 4 5 6 10 40 49 50 60 199 200 201
  across twelve files became **eleven named layers** in `tokens.css` (`--z-under` to
  `--z-chrome-top`). Three of the old numbers did one job; **199 next to 201 is the shape of a value
  picked to win an argument rather than to sit in an order.**
- **Every screen has exactly one `<h1>`.** 74 of 77 had none, while `ia/docs/pages/seo.md` has
  specified one per indexed page since stage 03b. Only the tag moved, grey tree first
  (`wireframes/_generators/page_heading.py`); the 19 overlay-only screens keep none, because
  inventing a heading is inventing copy. Three section headings went h3 to h2 to close the skip the
  promotion opened. **Heading skips across the painted tree: 0.**
- **A system stylesheet names the font it needs; the document loads it.** `base.css` `@import`ed the
  Google Fonts URL every page already `<link>`ed: one dependency declared twice, and the CSS copy
  three hops from discovery. It is also the wrong place for the decision, since the call sends a
  visitor's IP to a third party before consent in a product that ships a GDPR cookie banner.
  **Self-hosting the three families is the production answer and is now an open decision, not a
  silent default.** *(Closed in step 8.)*
- Also: the bet amount field took `outline:none` and gave back a 1.5px underline colour change, the
  only control in the product without a focus indicator and the field a person types a bet size
  into; `<meta charset>` sat at byte 2064 on all 77 screens because the theme boot was inserted
  ahead of it; 21 selectors nothing on any page could match; the four how-it-works section headings
  had no rule at all (18.72px is what a browser gives an unstyled h3); 15 half-pixel type sizes in
  the vitrine's own chrome; a comment naming `_theme.css`, deleted in step 7, on 76 screens.
- **Two things this pass got wrong and had to come back for**, both the same shape. `.sidebar-divider`
  is written at run time by `ui-kit/_nav.js` out of a template string, so a scan that read only
  `class="..."` in HTML called it dead; deleting it left every group heading in the vitrine's side
  panel as unstyled text. **A class inside a template string is markup**, and gate 14 reads the
  scripts now. The reason nobody noticed is worse than the bug: `_verify/snap.cjs` walked
  `ui-visual/` and nothing else, so a pass editing `components/` could prove the product and say
  nothing about the vitrine the same file paints. It takes `--kit` now, and re-running it against a
  worktree of the pre-pass tree found two more: `kit.html` has `<body class="app-case">` and
  `.app-case` is transparent by design, so the body stopped painting the page; and one label took an
  inline margin the removed `!important` had been out-shouting. **Removing an `!important` is only
  safe once you have found what it was arguing with.**
- **Three new gates**, so none of it grows back: **9** now fails on a style attribute, **12** owns
  the stacking order, **14** fails on a selector no markup can match (the other half of gate 11).
- **How it was verified, and a tool that had to exist.** `_verify/diff.cjs` walks two snapshots in
  step, which is right while the DOM is fixed and useless the moment a pass removes markup: every
  index after the removal points at a different element. **`_verify/visible.cjs`** keeps only what
  the browser reports as visible and compares those sequences, so a `display:none` deletion proves
  itself and a real side effect (a moved sibling, a renumbered `:nth-child`) still shows. Across the
  whole pass, at 76 screens x 5 widths, what moved: four dock buttons and one CTA bar lost 2px of
  padding (14px and 10px were never on the 4px grid, and an attribute never went through step 6),
  six section labels took the system's `.1em` tracking, and four headings went 18.72px to 18px.
  Everything else identical to measure; 0 text pairs below AA in either theme.

---

## 2026-07-27 - Stage 09, step 6b: the theme, as the proof of the semantic layer

The product is dark, so its theme is a LIGHT one and the attribute says what it is:
`[data-theme="light"]`, section 3 of `components/tokens.css`. It exists as a proof, not as a feature
(`ui-visual/_theme_switch.py --strip` removes the harness in one command); whether daylight ships is
a separate decision. A rebrand would prove nothing, because swapping primitives works on a flat file
with no roles at all. A theme is the test that needs the second level: the ground inverts, the ink
inverts, light and shade swap places, and the action still has to read as the action.

**Roles only, 89 of them; not one primitive redefined.** Daylight's values are their own primitives
at the end of section 1 (chalk ramp, warm ink ramp + alphas, one dark brass, darker green/red, five
chalk veil alphas, the Vault's own grain, a second logo mark). 265 -> 320 tokens, growth that buys a
second theme rather than harvest. The semantic selector is now `:root,[data-theme="dark"]`, so any
element can be marked and its subtree renders in that theme: `tokens.html` shows every role in both
grounds at once, live, and its contrast table has a column per theme.

**What the theme found, twelve holes, all fixed:** the stone grain read straight from a primitive
(11 declarations in 10 files -> `--surface-grain`); the brass logo mark, same category
(`--mark-logo`); the drawer backdrop reading the emboss shade instead of the scrim; the close disc
on a photographic head reading the ink of a drop shadow (-> `--scrim-photo`); a SELECTED state
painted with the focus-ring role (`tabs.css` x2, `options.css`); **five hex literals drawing the
multi-outcome chart from inside the page script on 13 screens** (a whole categorical palette the
token file could not see -> `--series-1..5`, handed to the SVG as `var()` so it follows the theme
live); a wireframe-era grey in a style attribute; **nine `mask-image` stops reading `--shadow-ink`
for "opaque"** (a mask keeps only the ALPHA, so every masked photograph faded to a third in daylight
-> `--mask-solid` / `--mask-mid`, never themed); and `--bg-brand-mark`, a role named for the plate
under the X and Apple marks that is really the colour of the marks (1.06:1 on a pale button, now
`--ink-900`); **a hover fill and a chart grid line both painted with the LIT LIP of an emboss**
(`--bevel-faint` did three jobs; on chalk a hover cannot reach for more light and a white grid line
on a white chart is not there -> `--tint-hover`, `--line-grid`); and **a filled glyph taking a text
role** (the bookmark: the reflection kept its contrast, 6.7:1 -> 7.2:1, and doubled its weight,
because light on dark spreads and ink on paper sits solid -> `--icon-quiet` 4.3:1, `--icon-brass`
3.2:1; the text-safe brass also reads brown at 16px, so the saved state stopped meaning gold).
Also found: `_rescale.py`'s duplicate-role sweep was file-wide and ate 8 theme
overrides, now per block.

**The sharpest lesson:** a veil is not a dark colour over a picture, it is the layer that
guarantees the words, so it follows the INK, not the photograph. `--scrim-photo` and
`--veil-photo-*` look like one idea and are two.

**Five corrections the first cut needed** (all user-caught by eye, then measured): the stone was
yellow (chalk warmed with depth, +8 to +36; the graphite is faintly COOL at -4..-8 and all the
warmth is in the ink, bone +19 - now a constant +8 at unchanged luminance); the blocks went flat
(the shade ladder was scaled as a unit, right for a 1px inset edge and wrong for a blurred drop -
now split, edge .10/.16, drop .32/.44); the grain vanished (dropped to a third on a backwards
reading of `overlay`, which above mid grey behaves like screen and bites LESS - now the Vault's own
0.9/0.8); and **the ramp was translated, not reflected**, the deepest of the four. The first cut
inverted the ORDER and not the DIRECTION: the page sat mid-ramp at L* 85.6 and every surface still
came forward by getting LIGHTER, so daylight was a generic grey theme for a structural reason, and
it ran a third too loud (graphite fills span 11.7 L*, that chalk ramp 15.5; a category chip stood
9.5 L* off its bar where the Vault puts it at 4.0). Daylight is now the graphite ramp **reflected
about its own ground**, computed not picked: `chalk L* = page L* - (graphite step L* - graphite
page L*)`. The page becomes the lightest thing on screen, every surface settles onto it, every
separation keeps the Vault's size with the sign flipped; 12 steps, each within 0.2 L* of target,
and a chalk step carries the number of the graphite step it answers to (`--chalk-850` answers
`--graphite-850`), so the theme block is checkable line by line against section 2. The reflection
is TOTAL, gradients included: a graded face then reads as lit from below, which is the right trade,
because reflecting the fills but not the gradients loses the ground under anything sitting on a
gradient's light end (that is where the chip problem came back). Fifth: **the reflection went one
role too far.** Lightness on graphite carries depth AND presence, and only depth can invert:
reflecting a control puts the most present thing in the system 11 L* under the page, which reads as
dirt, and it is the exact grey the grey-box wireframes used. So six roles (surface, slab-from,
control, control-hover, chip, chip-pressed, dialog-head) leave the reflection and sit at the top of
the ramp in the Vault's own order and direction, and the EDGE carries what the fill gave up
(daylight's hairline is 2.2:1 against its surface, the Vault's 1.1:1). The chalk ramp is now 8
steps + 1 hairline, as long as the stone is. **Area is the tell:** a chip 6.5 L* under white is a
quiet pill, a header band the same 7 L* under white is a dirty field - depth is read against how
much of the screen it covers, which no token file can see.

**Switch:** above the tree in both panels, single-source markup + boot in
`ui-visual/_theme_switch.py` (imported by `_resync_sidebar.py` and `_gen_component_pages.py`);
inline in `<head>` so daylight never flashes graphite; `localStorage` key `pm-theme`. Gate 1 masks
it as chrome, like the sidebar. **Gate 13** is new: colour goes through a role (a component reading
a colour or material primitive fails the build) + every screen can switch.

**A frame is a document.** The first cut of the theme lied in the vitrine: every stand page went
pale while every `<iframe>` inside it stayed graphite, because a specimen is its own page and
`data-theme` does not cross into it. Fixed both ways - the boot block is now in every specimen and
in `selftest.html` (so a frame is right at its own first paint), and the parent tells every frame
by `postMessage` on toggle and on `load` (so an open frame follows the switch). postMessage, not
`contentDocument`, for the reason `_frames.js` already had: from `file://` every document has an
opaque origin. Gate 13 gained "every frame follows"; gate 5 had to start its search at `<body>`,
since a head script now exists and its slice was coming out empty.

**Verified:** 77 screens x 2 themes x {380, 1280} - 0 below AA, 0 overflow, 0 console errors;
selftest "all pass" in both themes. Pre-existing defect found, NOT theme-related, logged for step
7: the win overlay h2 renders 52px left of its content box and `overflow:hidden` clips it to "u
were right" in both themes. *(Closed in step 7.)*

---

## 2026-07-27 - Stage 09, step 6: the primitives became scales

The token file had been READ out of the product, which is right for a colour role and wrong for a
scale: every literal anyone had typed became a token, 348 of them. Space had 25 steps with 1 2 3 4 5
6 7 8 9 10 in a row, text had five half pixels left from rem arithmetic, radius had two names for one
pill, and the graphite ramp had 46 pairs no eye can separate. Now **265 tokens**: space 25 -> 11 on a
4px grid (plus `--hairline`, since 1px is a line and not a distance), radius 12 -> 5, control and icon
value named with no odd sizes, text 21 -> 10 with the half pixels rounded UP, display 5 declared and
unused -> 7 wired (nine literal `clamp()` gone), leading 8 -> 6, graphite 24 -> 15, alphas 54 -> 28.
The whole map is data in **`ui-kit/_rescale.py`** (idempotent, `--dry-run`), which is both the
migration and its own test. Rules now written down in `architecture.md`: round to the nearest step and
break a tie toward the heavier neighbour; a number is a step only up to 64px; a colour merges only
under deltaE 1.5 AND when the two never meet on screen. Two new gates stop the harvest growing back:
**11** no orphan token, **12** no raw scale value.

**Deliberate, measured pixel movement.** This is the one pass that moves the product on purpose. Every
change was checked against the map with `_verify/`: 1274 distinct property changes, all of them
layout or type or a colour under deltaE 1.5, except `#e88a84` -> `#e79087` (two quiet reds for one
job, the pair the file had already marked). No touch target fell below 44px (the deposit amount field
now says `min-height:var(--control-44)` instead of reaching 45px by accident).

---

## 2026-07-26 - Stage 09, step 5: one source of css, and Stage 08's navigation restored

**Step 5.** Every painted screen dropped its inline `<style>` (25 to 42 KB of grey-box skeleton, 7
distinct copies across the 76 pages) and its `_theme.css` link, and links exactly
**`../components/index.css`** and nothing else. The migration is `ui-visual/_use_system.py`
(idempotent). Gate 9 in `ui-kit/_check_kit.py` enforces the one-source rule from here on. Proof
tooling lives in `ui-kit/_verify/` (snapshot every screen at five widths, diff by element and
property, group by cause). `ui-visual/_theme.css` and `_theme-vault.css` were left on disk unloaded
and deleted in step 7.

*Provenance, how it worked before:* `ui-visual/_theme.css` was the Vault colour layer; it
`@import`ed `ui-visual/_theme-vault.css` (base Vault tokens + component skin) and was linked AFTER
each page's inline `<style>` so it overrode by source order (owning colour/type/surface only). Vault
tokens sat in `:root` (graphite/brass, `--groove-*` engraved edges, `--stone-dark` grain), and it hid
the grey-box scaffolding + the wireframe screen-tree.

**NAVIGATION RESTORED, a Stage-08 defect.** The colour pass had flattened **every** product `.html`
link to `#` (`neutralize()` in `_apply_theme.py` / `_apply_family.py`, plus hard-coded `#` in the
`_gen_category.py` card templates), so all 76 painted screens looked finished and went nowhere while
the grey wireframes stayed clickable end to end. **9633 links restored** by `ui-visual/_relink.py`
(idempotent, six passes: aligned against the grey twin, by key in the twin, shared chrome donated
between painted screens, cards by their own kind, by key across the painted tree, then a 3-entry
table for the blocks that exist only in colour). Only `href` values changed - the 76 files are
byte-identical otherwise, so nothing moved a pixel. 17372 internal links, 0 broken; the 1604 anchors
still dead are dead in the wireframes too (footer placeholders marked "to be built"). The three
generators no longer flatten a link whose destination has been painted, and **gate 10** runs
`_relink.py --dry-run` so a re-broken link fails the build.

---

## 2026-07-18 - Concept + DESIGN.md synced to Vault

`concept/concept.html` matches the shipped card (thin odds bar, tinted YES/NO) + a new **Controls**
panel showing the chip family; `DESIGN.md` fully rewritten Signal -> Vault.

Also on this date: `_apply_theme.py` began injecting the themed category bar and wrapping the head +
state content in the shared `.cat-layout` stone plate, so a state reads as "the feed minus the cards"
(the `.state-block` goes borderless on the plate).

---

## 2026-07-16 - Concept locked: Vault. UI + Visual, the Event Feed family

**Direction: Vault** (superseded the earlier Signal exploration). Graphite canvas (page `#0f1013`,
device `#141619`), matte **brass** brand (`#c7a24e`, text-safe `#d7ac53`) + **bronze** `#6e5a2e`;
**green = YES / red = NO reserved as outcome semantics only** (brass never collides with the
win/lose colour); real event photography + **two-stone embossed plates** with inset brass hairlines +
notched corners, cards that float. Fonts: **Space Grotesk** (display), **DM Sans** (body), **IBM Plex
Mono** (numbers/mono). Binary feed card = **treatment B** (odds bar), multi-outcome = **treatment D**
(option rows). Reference screen for the colour pass = `event-feed.html`. All accent/text-on-graphite
pairs contrast-checked WCAG AA on the stand. The shipped system is `DESIGN.md`.

The visual language was decided as **rules traced to data + taste**, not a mood. Sources in
`concept/docs/`: `references.md` (Refero research, dark base) and `concept.md` (designer taste
captured verbatim + 5 attribute pairs A1-A5, each traced to a data line and a borrowed technique +
the locked decisions). Explored across contrasting directions (Newsroom after dark / Signal / Arena,
then a Signal refinement); those exploration stands were archived to `concept/old/pre-vault-3d/` when
Vault won.

**The reference screen** `ui-visual/event-feed.html`: 12 event cards, JS-injected **odds bar**
(renders treatment B from the `.prob` text, thin 5px), multi-outcome option rows (D), **tinted-not-fill
YES/NO buttons** (the odds bar carries the outcome colour, buttons stay quiet - "spectator, not
trader"), a redesigned **How-it-works `<dialog>`** (brass-tinted hero + icon chips), a **trust bar**
(USDC 1:1 + resolved count) + a footer **trust-cards strip**, the **graphite chip control family**
(cat-nav chips with icons + a condensed sticky strip, filters, Load-more - one `#1b1e23` chip, 12px,
brass on active), and the roadmap-sidebar course chrome.

**8 state pages** (`event-feed-empty/-error/-loading/-push-permission-missing`, `-logged-out` +
logged-out empty/error/loading) generated by **`ui-visual/_apply_theme.py`** with a **"shell + swap"**
strategy: start from the finished `event-feed.html` shell, swap in only the regions that differ
(always `<main>`; for logged-out also `<header>` + `<nav.bottom-nav>`), then run two voice-safe
transforms on the grafted fragment (a product link is kept when its destination is painted, Favorites
heart -> bookmark) + a `distill()` pass. Idempotent; never edits `wireframes/`, never regenerates the
base.

**Category pages:** the top category nav is page-level - `event-feed-{politics,crypto,culture,general}.html`
(generated by `_gen_category.py`; each drops the trending hero + sub-filter and shows only that
category's events, ~6). Trending stays `event-feed.html`. Nav wired on both levels; the old
client-side category-switch handler was removed so tabs navigate. **Order:** run `_gen_category.py`
then `_resync_sidebar.py`. `_resync_sidebar.py` is the single source of the ui-visual left screen-tree
and gained a **Categories** group under Event Feed, active-marked per page.

**Critiqued with `/impeccable critique` (dual-agent), snapshots in `.impeccable/critique/`. Score 33
-> 34 / 40** (Signal-era pass; the P1/P2 hardening carried into Vault; the whole-stage score at the
end of Stage 08 was 31 -> 38 / 40). P1/P2 hardened: NO-button contrast 3.41 -> 5.48:1, footer 3.37 ->
6.04:1, 44px touch targets (bet/bookmark/bell + cat-nav/filters), `:focus-visible` rings, tinted
YES/NO (spectator not trader), trust bar near the action, distilled controls (dropped the duplicate
Category dropdown, "Volatile" jargon, reverse toggle). Presentation-clean: `.uv-bar` + `.tbd`/placeholder
chips hidden, footer shows a real "Predict Market" wordmark. **P3 deferred** (live odds-delta
animation, error-vs-empty differentiation) - see backlog.md.

---

## 2026-07-12 - Stage 04: the wireframe reconcile against the IA Detailed layer + CJM

The 99 wireframes predated the IA Detailed layer (03b) and the CJM, so Stage 04 ran as a targeted
reconcile that rendered the newly-specced IA and closed two CJM gaps, all voice-safe (new pages
hand-authored; shared/global changes by idempotent in-place post-processors; `gen_*.py` never
re-run). Added: the 5 system pages (from `system.md`); a footer trust strip (USDC 1:1) + "Popular
right now" SEO block + real hrefs + Cookie-preferences re-entry (all 87 footer pages,
`footer_reconcile.py`); a per-card story-led "why" + below-fold SEO sections on the feed
(`feed_reconcile.py`) and category pages (`category_reconcile.py`); a Related-events block on Event
Detail (`related_events.py`); and the Win F5 overconfidence-friction ("Before the next one", no "bet
again"). Course Stage-04 infra (`screens.md`/`_nav.js`/`_wf.css`/`index.html`) was skipped as
EQUIVALENT to ours (`_screens.md` + `_shell.py nav_tree`/`resync.py` + inlined CSS + the per-page
screen-tree). New copy logged in `voice/docs/microcopy.md` (Steps 15-20); the reconcile audit + fixes
are in `wireframes/_critique.md`. Gates: 104 pages, 16061 internal links, 0 broken, 0 em-dash.

Result: 104 pages - every screen in the IA screen tree, each state its own page, plus the Favorites
view (`favorites.html` + empty + loading) and the 5 system/global pages (`404` / `500` / `maintenance`
/ `cookie-consent` / `toasts`). Orphans `[SIROTA]` (Settings, Leaderboard, Help/FAQ) unbuilt by
design; the standalone Bet Screen is dissolved into the inline Event Detail bet panel.

---

## 2026-07-12 - IA Detailed layer (Stage 03b), as a targeted reconcile

**Scope = targeted reconcile, not the full node-by-node build.** The 99 wireframes already exist and
ARE the per-page B/W render, so we did NOT redraw pages, write a `pages/*.md` per screen, add an
`ia/_nav.js`, or renumber the sitemap to X.Y (all would duplicate the wireframes or
`resync_sidebar.py`). We built only what the wireframes deliberately omit and a launch needs:

- the **A-E SEO structural layer** for the indexed public pages (Event Feed, Event Detail, Category,
  How It Works, Public Profile); every private/transactional zone is `noindex`, no schema;
- the **footer** as an SEO / internal-linking node;
- the **system / global nodes** (404, 500, maintenance 503, cookie-consent grounded in law, toasts).

New sources live in `ia/docs/pages/` (`seo.md`, `system.md`); rendered B/W as `ia/seo.html`,
`ia/system.html`. The shared sidebar stays single-source via `resync_sidebar.py` (not `_nav.js`); new
IA pages register there.

**Built.** `seo.md` carries the indexation policy (every screen family index vs noindex) + the A-E
template + full A-E for Event Feed, Event Detail (with the per-event schema decision: `WebPage` +
`BreadcrumbList`, `schema.org/Event` rejected), Category, How It Works, Public Profile, and the footer
node. `system.md` carries 404 / 500 / 503 / cookie-consent (grounded in GDPR + ePrivacy + UA Law
2297-VI, cited) / toasts; Search stays deferred. Both render to `ia/seo.html` + `ia/system.html`,
wired into the shared sidebar under IA > Detailed layer (SEO layer, System nodes) on all pages.
`sitemap.md` registers the system + footer/legal destinations (SYSTEM AND GLOBAL). Link check: 27
pages, 743 links, 0 broken. Deliberately not done (would duplicate the wireframes): per-screen B/W
redraws, `pages/*.md` per screen, `ia/_nav.js`, X.Y renumbering.

---

## 2026-07 - Voice: the interface copy rewritten (Steps 05-14)

Every UI line was edited line-by-line against `voice/docs/voice.md` (five principles + lexicon +
forbidden + per-element rules). `voice/docs/microcopy.md` holds the read-only text inventory it was
edited from plus the full rewrite log (all screen families done, incl. the step-13 "rest of the
screens" pass).

**Event Detail content tabs** were rewritten from trader vocabulary (Top Holders / Positions / shares
/ "bought N YES at $X") to spectator language in the step-14 pass: below the event content, a
Polymarket-style tab strip (CSS-only radio switch, no JS) - **Comments** (sort + composer with
likes/replies; logged-out prompts sign-in), **Biggest bets** (YES/NO columns), **Bets** (table
Bettor/Side/Amount; your bet highlighted when logged in), **Activity** (recent-bets feed). On binary +
multi + resolved, logged-in and logged-out.

**Chrome wiring** landed in the same period: header (Favorites -> Favorites view, bell ->
Notifications, avatar dropdown -> Profile/My Bets/Wallet/How It Works/Logout) and the mobile bottom
nav are real links, not dead buttons; logged-out controls open the sign-in dialog. A `How it works`
button sits in the header next to the logo and opens a native `<dialog>` quick-explainer (the feed's
three explainer sections + a link to the full How It Works page); self-contained `.hiw-*` styling, on
all 87 header pages via the idempotent `howitworks.py` post-processor (Step 21 in `microcopy.md`).
Applied by the idempotent `fixpack.py` post-processor.

**Status at close:** Lesson 05 steps 1-7 done; the step-7 finalization audit (Step 14 in the log) is
clean - 0 lexicon/forbidden violations in product copy across all 99 pages (excluding the brand name
"Predict Market", the voice-sanctioned "the market resolved YES/NO", and the AMM mechanics gloss).

---

## 2026-07-07 - Wireframes: the finalization trio

Three audits, all recorded in `wireframes/_critique.md`:

- a **flow-wiring audit** (step 7) that verified every edge against `ia/docs/flows.md` and fixed the
  last naked recovery buttons (`Try again` on the Event Feed + Category error pages, `Try another
  card` on `deposit-error-card`);
- a **99/99 coverage audit** (step 8) against `ia/docs/sitemap.md` - every sitemap screen + state has
  a page, deliberate exclusions documented;
- a final **six-category defect pass** (step 9: style leak / placeholders / missing states /
  dead-ends / zone-without-action / off-map) - all clean.

Earlier passes in the same log: Krok 8 (consistency reconciled across all families), Krok 9, and the
**2026-06-29 multi-agent re-critique** (all 99 pages across five families - clean bar one minor
clarity fix on `event-detail-resolved.html`, live "now" odds reframed as "Trading closed / at close").
Standing gates: 0 em-dash, 0 broken internal links, 0 style leaks.

---

## 2026-07-03 - Wireframe annotations moved out of the wireframes

The wireframes became clean grey-box UI only. The inline `zone:` chips and the bottom `.side` block
(the `zone -> job / finding` annotation list + nav-tree / header-model / responsive / variant notes)
were extracted into a dedicated IA visualization at **`ia/annotations/`** - one HTML page per screen
family, every state inside it, each state showing a nested zone map + its annotations + a link to the
live wireframe, plus shared structure/flow notes. Entry point: `ia/annotations/index.html`. Styled in
the dark research/IA-viz theme and wired into the shared left sidebar as "Wireframe Annotations"
(under the Plan section, after Wireframes) on all root viz pages; the annotation pages carry that same
sidebar (with a sub-link per screen). Generated + stripped idempotently by
`wireframes/_generators/ia_annotations.py` (`build` then `strip`; run `build` before `strip`).
