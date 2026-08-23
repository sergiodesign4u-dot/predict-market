# Onboarding gaps

What a reader with no context could not work out from this repository, and what they worked out
wrongly. This is the critique log of the Handoff stage, and it is the stage's entry order: every row
here is either closed by a Handoff artefact or is refused out loud with a reason.

**It was not written by imagining a newcomer.** Whoever built this product cannot read it, only
recall it: every "unclear" has an answer in their head that is on no page. So the reading was done by
a subagent with a clean context, on 2026-08-23, and the two lists below are its own.

---

## How the reading was produced

**The order.** Get oriented (what is this, which folder is the product, what is the entry point,
what is the system, where do strings live, which theme is primary, is there code), then prepare to
build ONE screen that does not exist yet. Read-only: nothing in the repository was created, edited
or deleted, and the working tree was clean before and after.

**The three rules the prompt carried, each as an explicit line.**

1. **Read from disk.** A file already sitting in context is a snapshot taken earlier and is not a
   source. Without this line an agent reports on text the file no longer holds, and does it
   confidently.
2. **Forbidden paths, named one by one, not as a class.** "No critique logs" does not work, because
   the logs sit inside folders the agent was just handed. Named: `wireframes/_critique.md`,
   `ui-kit/docs/audit.md`, `ui-kit/docs/census.md`, `ui-kit/docs/consistency.md`,
   `ui-kit/docs/consolidation.md`, `docs/kit-archive/`, `concept/old/`, `ui-visual/old/`,
   `handoff/`, and any Critique / Defect section inside `research/`, `ia/`, `voice/`.
3. **A reading journal**: every file opened, in the order it was opened. The journal is the proof of
   isolation, and it is checked against the forbidden list. A hit voids the run; it does not
   discount it.

**Isolation held.** 56 journal entries, 0 forbidden reads. Two near-misses were disclosed by the
agent rather than found: a listing of `ui-kit/docs/` showed the four forbidden filenames with no
content, and a `find` over `.impeccable/` printed critique filenames. `.impeccable/` is a critique
log that Rule 2 did not name, which is the rule proving itself: a class-level ban leaks and a path
list does not. Neither file was opened.

**One environment finding, recorded here because it changes how the next reader measures.** The
Playwright MCP in this session refuses `file://` outright. This repository's whole method rests on
reading pages from disk, because `file://` gives every document its own opaque origin and that is
what makes the icon sprite a script and the fonts and trust art `data:` URIs. The agent had to serve
the tree over `http://127.0.0.1`, which is the one protocol the doctrine says is not sufficient on
its own. A disk reading needs the global `playwright@1.62.0` driver directly, not this MCP.

**Roll-call.** The agent returned **12** rows in LIST A and **93** in LIST B. Every row below is
verified: **12 of 12** and **93 of 93**, none dropped, none merged.

**One input the pack expects and this repository does not have.** Half of this step is normally
already done, by the Rollout stage's "subagent questions" section. There was no Rollout stage here:
the tree was painted at UI + Visual (stage 08) and every stage after it kept the tree in step, so
`ui-kit/docs/rollout.md` does not exist and there is no pre-taken set of reader questions. The whole
of step 1 therefore stands on the single run above. Said out loud rather than compensated for.

---

## LIST A - could not work out

Verified line by line against the disk on 2026-08-23. Four verdicts, and the fourth is the one that
becomes a written decision rather than a document:

- **ABSENT** - the answer genuinely is not in the repository
- **ELSEWHERE** - it is there, in a place the reader had no reason to look
- **MISSED** - it is there, where they were looking, and they did not see it
- **DELIBERATE** - it is a decision that was taken, and it is written down nowhere

| # | Question | Verdict | What the disk says | Closed by |
|---|---|---|---|---|
| A1 | Is there a procedure for adding a SCREEN, the way there is for a component and a pattern? | **ABSENT** | `ui-kit/docs/architecture.md` has fifteen numbered sections. §11 is "How to add a component", §12 "How to add a pattern", §13 "Where a change goes". There is no section for a screen, and the procedure really is spread over six files. | `one-shot.md`, step 7 - it is exactly the missing §11.5, written as a prompt |
| A2 | When I add a screen, who updates the navigation panel in the other documents, and how? | **DELIBERATE** | Correct that no registry covers the screen trees and that the scripts that held them were deleted with all 63 generators. The rule that answers it ("a sweep is a throwaway script") is in root `CLAUDE.md` and does not name this job. See B72: the reader also got the shape of the panels wrong, which makes this the most expensive unwritten thing in the repository. | `behaviour.md` is not the place; this goes to `one-shot.md` "file and registration" and to `docs/backlog.md` as the registry debt |
| A3 | `ia/docs/blocks.md` banks exactly one page type. What do I do for a type it has not banked? | **ABSENT** (the method), **present** (the rule) | `blocks.md` has one type section, "Type 1: the static content page", plus "The four rules a row obeys". The four rules are the method's contract; the two-source procedure (competitor crawl + Refero by page type) exists only as one worked instance and is nowhere stated as mandatory or optional. | `one-shot.md` names the four rules as the gate and refuses to invent the rest; the banking method is a `docs/backlog.md` row |
| A4 | What is actually open in `docs/backlog.md`? | **MISSED**, and the file earned it | The header does say "**Open: 0**, counted from the rows below on 2026-08-21" - dated, computed, correct. Measured now: **234 rows, 234 struck, 0 open.** But it is buried under four consecutive paragraphs of superseded self-counts (45, 47, 44, 0, 2), each correcting the last, in a 518 KB file. A dated true number that reads as one more correction is a number nobody can spend. | `handoff.html`, "what was deliberately not done", routes to the backlog with the count computed on the day |
| A5 | Does a new screen family need a page in `ia/annotations/`? | **DELIBERATE** | 15 annotation pages against 15 screen families; search, the four static documents and the system pages have none, and the generator that built them is gone. Nothing states whether the folder is frozen, incomplete or optional. It is frozen in practice and that has never been written. | A decision entry in `docs/decisions.md`, plus one line in `handoff.html`'s route |
| A6 | Which metadata does a new indexed page get, and must it exist before the page is built? | **ELSEWHERE** | `ia/docs/pages/seo.md` has six numbered page-family sections plus a global footer section and the A-E template. A seventh type has no section. The ordering question (A-E before or after the build) is genuinely unanswered; `terms.html` is the only precedent and it went both ways. | `behaviour.md` source column, and the ordering goes to the NOT DECIDED list for the owner |
| A7 | What domain does the product live at? | **DELIBERATE, and already written** | `{ROOT}` is `[?]` by a stated decision with its cost written beside it (`seo.md` line 30): no canonical and no `og:url` can be written without it. The README's GitHub Pages links use `predict-market`, which is neither the folder name nor the product name Yonder - that half is unverified and is a real README defect. | `handoff.html` "who decides after handoff"; the README links are checked by the route instrument at step 5 |
| A8 | Is there any test, lint or CI? | **ABSENT by decision, and the decision is loud** | No `package.json`, no `.github/`, no `Makefile` - verified. "0 gates, 0 generators, no build step" is stated in three files with the seven days and 145 MB it cost. What is genuinely unexplained is `venv/` and `pw/`, two Python virtualenvs sitting untracked inside the folder with nothing naming either. | `handoff.html` PACKAGE BOUNDARY; the two venvs get one line in the route |
| A9 | Who owns product decisions after handoff? | **DELIBERATE** | `PRODUCT.md` says "Solo: product, design and development" and names counsel as the decider for jurisdiction, "the one open item in this file whose owner is not in this repository". Everything else is unattributed: no CODEOWNERS, no maintainer list, no contact. The answer is true and is written nowhere as governance. | `handoff.html` WHO DECIDES - a required section of the page for exactly this reason |
| A10 | How many markets have fixture data, and where is the canonical list? | **ELSEWHERE, and the three numbers are three different questions** | `PRODUCT.md`: about 25 open at once, curated - the product's design target. `assets/search.js`: 27 events extracted from the tree on 2026-08-20 - a dated hand copy. `docs/launch-catalog.md`: 7 markets with a named resolver each - what release 1 opens. All three are correct and none is the canonical fixture set, which is the markup of 119 documents and exists in no data file. | `behaviour.md` names the three and which question each answers |
| A11 | Where does a page script go and what may it do? | **ABSENT** | The rule for the two shared scripts is explicit and correct. The ceiling is not written anywhere: how much behaviour may live inline, whether a script may write a class the system styles (it does - `oddsbar` has 0 source placements and 72 rendered), and how a hook is registered. `Script hooks:` in a stylesheet header is the CSS half only. | `one-shot.md` and a `docs/backlog.md` row for the missing script contract |
| A12 | What is `figmosha2/` and does it matter? | **DELIBERATE, and written in the one place nobody reads for this** | `.gitignore` line 7 excludes it as a nested tool repo. It is not part of the 679 tracked files. No repository document mentions it. | `handoff.html` PACKAGE BOUNDARY, which lists what is inside the folder and outside the package |

---

## LIST B - understood it as

93 confident conclusions. This is the more expensive list: "could not work out" is a known hole, and
"understood it as" with a wrong conclusion is a hole no other instrument in this repository can see,
because the reader was not confused, they were sure.

**Roll-call: 93 = 84 correct + 1 wrong + 5 correct from a source that is stale + 3 correct and
written down nowhere.**

The 84 were checked against the source each row cites and stand as written; they are the reader
correctly recovering the rules, and they are the evidence that most of this repository transmits.
The nine that did not are below.

### The one that was wrong

| # | The conclusion | Verdict | What the disk says | Closed by |
|---|---|---|---|---|
| B72 | "The screen-tree panel is hand-written markup inside `<aside class="sidebar" id="rmSidebar">` in every one of the 120 painted and 119 grey documents, so adding one screen means editing 239 files' panels." | **WRONG in the half that matters** | The mechanism is right and the cost is roughly right. The identity is not. **The two trees carry two different panels.** Painted: `.sidebar` / `#rmSidebar`, with `sidebar-page-link` and `sidebar-sub-link` rows - **120 of 120**, and **0 of 119 grey**. Grey: `.wf-nav` / `.wf-tree` / `.wf-screen` / `.wf-states` / `.wf-substate`, 28 screen rows with their state sublists - **119 of 119**, and **0 of 120 painted**. Different classes, different shape, different row grammar. **A sweep written from this conclusion edits 120 files and silently misses 119**, which is this repository's own "a rule stated over a set is measured over the set" arriving as a defect in the reader rather than in the code. | `map.md` records both panels as two registries; `one-shot.md` names both by class; `docs/backlog.md` carries the registry debt |

### Correct, from a source that has gone stale

Every one of these is the reader trusting a prose file. The rule they were trusting it against is
root `CLAUDE.md`'s own: **a count is COMPUTED, or it is DATED and says the day; it is never typed as
a live fact.** Six files break it today, and the reader found five of them without being asked.

| # | The conclusion | Verdict | Measured 2026-08-23 | Closed by |
|---|---|---|---|---|
| B60 | Five prose files carry tree counts behind the disk | **CORRECT, and undercounted by one** | `ui-visual/CLAUDE.md` says 115 / 114 (disk 120 / 119). `wireframes/CLAUDE.md` says 114 (disk 119). `ui-kit/docs/architecture.md` says 116 grey and 117 / 116 painted. `ui-kit/overview.html` body prose says "55 hand-written pages" and "the 106 painted screens and the 104 grey ones" while its own panel computes 61 from `_nav.js` three inches above. **The sixth is `docs/build-plan.md`**, which opens "116 painted screens, 116 grey" and sizes the whole Astro migration on it - and the reader cited that file as authoritative in B12 without noticing. | Documentation, so it is repaired in this stage rather than filed: step 5 |
| B61 | The grey tree's only self-check is switched off | **CORRECT, and it is the largest single instance** | Every inline stylesheet in the grey tree declares itself **"ONE OF 114 COPIES"** - **119 of 119 documents**, against 119 on disk. The `SHARED (N of M, R rules)` denominators read **2,125 markers at "of 114", 100 at "of 116", 5 at "of 117"**. That header is the only check a tree linking no stylesheet can carry: a reduced copy is supposed to contradict its own header, and with the denominator five documents behind, it cannot. | `docs/backlog.md` - it is a product edit across 119 files and this stage does not make product edits |
| B62 | `components/CLAUDE.md`'s "the product contains 0 `<form>` elements" is now false | **CORRECT** | **238 `<form>` elements across 119 painted documents**, since search shipped on 2026-08-16. It was a true dated reading over 106 documents. The argument it supported still holds, because the amount fields stand outside those forms - so the sentence is stale and the ruling is not. | Documentation: step 5 |
| B12 | The v1 stack is decided: Astro, Supabase, Cloudflare, 116 documents collapse to 6 routes | **CORRECT about the stack, stale in its arithmetic** | The routes decision stands. The document count it is computed from is 116 against 119, and "91 of the 116 painted documents live inside those routes" is arithmetic on a tree three documents larger. | Documentation: step 5 |
| B92 | Twelve of thirteen stages are Done and Handoff is Not started | **CORRECT as a reading of the table, and the table disagrees with `STRUCTURE.md`** | `README.md` has 13 status rows, 12 ✅ and 1 ⬜. `STRUCTURE.md` declares **12 stages** and says CJM is inside User Research and not a stage of its own, having renumbered from 13 to 12 on 2026-08-02. So the two files count the same work differently and neither is wrong; nothing says they are counting different things. | `handoff.html` carries the one status table; step 5 reconciles the sentence |

### Correct, and written down nowhere

These are the rows that become sections of `handoff.html` rather than corrections. Each is a true
thing the reader had to derive, and deriving it is exactly what the next reader will get wrong.

| # | The conclusion | Verdict | Why it matters | Closed by |
|---|---|---|---|---|
| B26 | The theme toggle is review chrome, not a product control: `.theme-switch` sits inside `ASIDE.sidebar` on every screen and `.app-case .theme-switch` is null. The shipped product has no theme switch. | **CORRECT and unwritten** | Only the browser could tell them this. From the source the toggle is just a button, and a developer who reads the source will ship a theme switch into the product. | `handoff.html` WHICH THEME IS PRIMARY - a required section |
| B9 / B10 | This is not an application. 679 tracked files, 361 HTML, 60 CSS, 4 JS, 0 lines of product code, no build step, no server, no API. `venv/`, `pw/`, `figmosha2/`, `.impeccable/`, `.claude/` are ~40 MB of tooling inside the folder and outside the package. | **CORRECT and unwritten** | The reader had to run `git ls-files` and a `.gitignore` read to find the edge of the deliverable. Nothing states it. A person who is handed this and expects to run it will look for a start command for an hour. | `handoff.html` PACKAGE BOUNDARY - a required section |
| B90 | Open questions are decided by the one person who wrote all 531 commits, with one named exception: jurisdiction, decided by counsel before the first real dollar. | **CORRECT and unwritten as governance** | Both open lists in this package (`docs/backlog.md`, the NOT DECIDED list in `behaviour.md`) are addressed to a person. Without an addressee the first such row stops the work. | `handoff.html` WHO DECIDES - a required section |

### One thing the reader found that was not asked for

**`ui-kit/why.html` is the actual front door, and no file at the repository root points at it.**
`README.md`, `STRUCTURE.md` and root `CLAUDE.md` all route a newcomer into prose. The page that says
"here is the five-minute path, here is what will bite you, here is where everything lives" is a
stand page, reachable only by opening the kit and looking. The reader found it by browsing, not by
reading, and named it the developer front door on their own. Closed by step 5: the route from the
root reaches it in one click.

---

## What is closed where

Every row above carries a "closed by" cell, which is this file's own idle control: a gap with no
closure is a gap that reads as handled and is not. Steps 2 to 7 fill them; step 7 appends the
examination's own findings to this file. Nothing here is repaired by editing the product: a product
edit after stage 12 was accepted cancels every pixel comparison the acceptance stood on, so a
finding that needs one goes to `docs/backlog.md` and is named here with its row.

---

## THE EXAMINATION, RUN 1, 2026-08-23

The audit at step 1 asked a reader with no context to UNDERSTAND the package. This asks one to USE
it: a different subagent, a written prompt and nothing else, and a real feature to build. **The two
find different things, and this one is closer to what actually happens next**, because a person
taking a package over does not read it, they need something from it.

**The brief.** `handoff/docs/one-shot.md` as the entry point and the only briefing. The feature was
the responsible-play slot, a node `ia/docs/sitemap.md` had held reserved since the map was written,
with the volume named in numbers before the run so the result could be measured against it: one
screen family, four states at minimum, both trees, so eight documents at minimum. The same three
isolation rules as step 1 - read from disk, forbidden paths named one by one including this file,
and a reading journal as the proof.

**Isolation held.** The journal names 28 reads in order and no forbidden path is among them. **One
disclosure the reader made unprompted**: a repository-wide grep will have scanned four forbidden
files, and no line from any of them appeared in its output. A disclosed accident is recoverable and
this is the behaviour the journal exists to produce.

**What it built.** Five states in both trees, registered in both hand-copied panels across 244
documents, with the deferral overturned in the map, a second page type banked, a copy section
written and eight backlog rows filed. Verified independently before anything was decided: 130
renders per engine, 0 page errors, 0 sideways, exactly one level-one heading per document, no
dialog contributing height, the grey inline stylesheets byte-identical to the file they were copied
from, and in the paint no media query, no transition, no keyframes and two element styles both
inside the permitted set.

**The screen is reverted and kept addressable on a branch**, on the user's decision and for the
stage's own reason. It is not on this branch and the trees are the size they were.

### What it could not work out: 10

This is the number run 2 has to beat. Only the rows that produced a change are listed; the full
list is in the run's report.

| # | The gap | Closed by |
|---|---|---|
| A1 | **The stop condition in `one-shot.md` named two node states and the map has three.** Built and `[ORPHAN]` were covered; **reserved / deferred / post-MVP** was not, and it is the state the feature was actually in. An orphan has no job and a deferral has a job and a date, and in a hurry they look identical | `one-shot.md` section 1 now carries the three states as a table, with the one test that separates the middle from the bottom: whether the map's reason is about the READER or about the RELEASE |
| A2 | **Which state is the base page, when the screen is a CONTROL rather than a view.** The convention says the base is "the success or representative state" and does not say which wins when they part. On any settings surface they always part | `one-shot.md` section 4: the base is the representative state, and the choice is written into the block bank entry for the type |
| A3 | **The waiting period on loosening a limit is promised in shipped copy and its number exists nowhere.** The direction is specified in both trees; the figure is in no file. The asymmetry IS the mechanism, so the number is the difference between a limit and a suggestion | `behaviour.md` **N9**, addressed to a person, with the two precedents for a clock-bounded number named |
| A7 | **What counts as "the words", when a screen's strings stand on no component specimen.** The rule says a string goes into three trees; nothing says what to do when the third has no place for it | `one-shot.md` section 5: the stand carries COMPONENT strings, so such a screen touches two trees, and check rather than assume. The inventory is named as a tree in its own right, which row 241 then proved it had to be |
| A8 | **Where a private, account-level screen is reached from.** Decided once for Wallet by name and never generalised, beside a written refusal to add to the global chrome. The next account screen has a precedent and a refusal and no rule | `behaviour.md` **N10**, with the cost stated: one row in the avatar dropdown is an edit to every document in both trees |

Four more were repository questions the package already carries as open rows and needed no new
writing: whether the banking method is mandatory for a new page type (**N4**), whether
`ia/annotations/` is still live (**N2**), the grey tree's stale shared-region denominators (backlog
236), and `map.md` being a dated reading that its own method forbids editing by hand.

### What it worked out and stated flatly: 26

The expensive list at step 1 was the one where a confident reader was WRONG. **This one is the
opposite result and it is the finding**: the conclusions are right, including the one that had been
wrong before.

**B72 at step 1 concluded that both trees carry one panel under one class and that a screen costs
239 identical edits.** They share no class name at all, and a sweep written from that conclusion
edits one tree and silently misses the other. This reader, given one paragraph in `one-shot.md`,
concluded the mechanism correctly, named both class families, and put a number on it: **261 files
for one screen family with five states, of which 244 are the panel and there is no registry to edit
instead.** One paragraph closed a gap that would have cost 119 silently skipped documents.

**And it found four defects nobody here had seen**, all pre-existing, all re-measured against the
reverted tree, all filed: twelve documents whose panel names a smaller set than their tree does and
the two trees disagreeing about which (**239**); four documents with no level-one heading at all
(**240**); the copy inventory still carrying a word the lexicon bans by name, on 11 rows, while the
trees carry it on none (**241**); and all four hand-written renderings in `ia/` standing behind
their markdown (**242**).

**240 landed on this package rather than on the product.** `a11y.md` row 13 carried a status
inherited from an earlier stage with the instrument named and not run, on a sound argument. The
argument was sound and the status was still unearned: the four headings were missing the whole time
and every instrument here passed them. **A status inherited from an earlier tree is a status about
that tree**, and the row is a debt now with its measurement beside it.
