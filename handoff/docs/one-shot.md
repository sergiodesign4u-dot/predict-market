# How to add a screen

**This file is a prompt.** Paste the whole of it in front of the thing you want built, and add the
one paragraph that says which feature. It is written for a person or a model meeting this
repository for the first time, and everything it asks for has a reason recorded somewhere in the
repository rather than here, because a copy of a reason is the first thing to go stale.

**It is deliberately not a checklist of edits.** Any tool can be told which files to touch. What
this file carries is the two or three decisions that are irreversible once made wrongly, and the
order that keeps them from being made at all.

---

## THE PROMPT

> Read these four files before writing anything, in this order. They are the whole briefing and none
> of them repeats another.
>
> 1. `CLAUDE.md` at the root, then the `CLAUDE.md` in every folder you are about to touch. Each rule
>    there carries the measurement that produced it. **A rule you disagree with is a rule whose
>    reason you have not read yet.**
> 2. `handoff/docs/behaviour.md` for what the product DOES: the flows, every terminal and its
>    recovery, the states each surface already has, and what each field enforces. **If the thing you
>    are building appears in the NOT DECIDED list at the foot of that file, stop and ask.** That list
>    is addressed to a person and it is not a to-do list.
> 3. `handoff/docs/map.md` for what a screen is made of, and for the inverted list, which is the one
>    that answers *if I change this, what moves*. Read it before you decide that something is
>    missing: **most of what looks missing is a component you have not found yet.**
> 4. `handoff/docs/a11y.md` for what is already promised and by which instrument. Anything you add
>    inherits every promise in it, and the three rows marked as debt are debts you must not deepen.
>
> Then work in this order, and do not reorder it. Each step exists because doing it later costs more
> than doing it first.

### 1. The map decides before the screen does

A screen exists because a person is trying to do something. `ia/docs/sitemap.md` holds every place a
reader can go. **If the thing you are adding is not a node there, it is not a screen yet; it is a
proposal.**

**A node that IS there is in one of three states, and they are not two.** This sentence used to name
two and a reader building from it met the third on their first move:

| The node says | What it means | What you do |
|---|---|---|
| built | it has a screen | you are extending, not adding. Read the screen first |
| `[ORPHAN]` | **no confirmed job maps here** | do not build it. This is a decision, not an oversight, and the reason is written beside the node |
| reserved, deferred, post-MVP | **a job exists and the release does not carry it yet** | you MAY build it, and the deferral's own reason is the thing you have to answer. It was written on a premise; find the premise and say whether it still holds. If it does, stop. If it does not, say so in `docs/decisions.md` and turn the node in the same commit |

**The middle row and the bottom row look identical in a hurry and are opposites.** An orphan has no
job; a deferral has a job and a date. The one test that separates them is whether the map gives a
reason that is about the READER or about the RELEASE.

Then `ia/docs/flows.md` for how a reader arrives and where they can end up, and `ia/docs/blocks.md`
for whether the composition you need has already been banked. Metadata for a new indexed page is
written in `ia/docs/pages/seo.md` and stays there: **a document head is never computed from the
page, so a copy of it beside the page is a second edition of one fact.**

### 2. New goes into the SYSTEM first and onto a screen second, never the other way round

This is the rule that decides more than any other here, and it is the one most often broken by
someone who is nearly finished.

**It does not say do not add anything.** It says the addition has a place, and the place is not the
screen file. What is missing appears in `components/` first, complete: its stylesheet, its import in
its own level group, its page in `ui-kit/`, and its row in the inventory. Only then does it stand on
a screen. A component is a component when it stands on three screens or more; two screens is a
candidate and stays markup.

**A screen that grows a part every time it meets a new page has not been tested by that page, it has
been edited by it.**

### 3. What a screen file may never contain

These four are copied word for word from `components/CLAUDE.md`, because they are the rules that
keep the system whole as it grows and a paraphrase of a rule is a weaker rule:

> **MOTION LIVES IN A TOKEN, A COMPONENT OR A PATTERN, AND `transition`, `animation` AND
> `@keyframes` ARE FORBIDDEN IN A SCREEN FILE, EXACTLY AS `@media` IS.**

> **A MEDIA QUERY MAY NOT STAND IN A SCREEN FILE, EVER.**

To which the same folder adds two that catch the same mistake one level down: a literal duration or
a bare easing keyword is a defect and not a shorthand, and **never on the element** - a `style=`
attribute is a rule in the one place the system cannot see. Three things are not styling and may
stay: a datum, the event photograph, and a value the page script writes at run time.

**Adaptation and movement are not forbidden. Inventing them in a screen file is.** They live in a
token, a component, a pattern or the shell, and a movement names its job before it is written:
a response, an arrival, or a status. A moment for which none of the three can be named does not get
a movement.

### 4. The file, and the registration, which is the half that gets forgotten

**A state is a page, in both trees.** Not a toggle, not a variant inside one file, not a query
parameter. The base file is the success state; every other real state is its own file beside it,
named `<screen>-<state>.html` in lower kebab-case, with the same state name in both trees.

**On a screen that is a CONTROL rather than a view, the success state and the representative state
are different pages, and the base file is the representative one** - the state every reader meets on
their first visit, which is usually the one with nothing set yet. The convention says "success or
representative" and does not say which wins when they part. They part on every settings surface.
Write down which you chose and why, in the block bank entry for the type.

The screen exists **twice**, and the two are not copies of each other:

| | `wireframes/` | `ui-visual/` |
|---|---|---|
| owns | structure and copy | the visual layer only |
| stylesheet | **none.** One inline `<style>` block per file | **exactly one link**, to `components/index.css`, and nothing else |
| built | first, in grey | second, from the grey |
| what may legitimately differ | the seven declared differences in `wireframes/_conventions.md` and nothing else | the same seven |

Anything else that differs between them is drift by that document's own definition, and the check
that finds it is a diff of the two file lists plus a reading taken by hand.

**Then register the screen, in four places that are four different mechanisms.** This is where a new
screen most often ends up existing only on disk:

| Where | What it is | The trap |
|---|---|---|
| the panel in `wireframes/` | `.wf-nav` / `.wf-tree`, with `.wf-screen` rows and their `.wf-states` sublists | hand-written markup **in every grey document**, not a registry file |
| the panel in `ui-visual/` | `.sidebar` / `#rmSidebar`, with `sidebar-page-link` and `sidebar-sub-link` rows | hand-written markup **in every painted document**, and **it shares no class with the grey panel** |
| `ui-kit/_nav.js` | a real registry, one route for the whole stand | only if the work added a component |
| `assets/_roadmap.js` | a real registry, the course roadmap | only if the work added a stage |

**Two of those four are hand-copied into every document of their tree, and they do not share a
single class name.** A sweep written for one of them edits that tree and silently misses the other,
which is exactly what a reader with no context concluded when they read one panel and assumed the
other. **The panel a document marks as current must be the document itself**, and the two trees'
panels must name the same set of screens: a panel that is confidently wrong adds no height, no
sideways scroll, no duplicate id and no page error, so nothing here can catch it but reading it.

### 5. The words are a third tree, not a second

Every string a person reads is registered in `voice/docs/microcopy.md` and must obey
`voice/docs/voice.md`, whose lexicon bans particular words in particular PLACES: the ban is about
place and not about the word, so a term forbidden on a control label can be correct inside a block
whose whole job is explaining the mechanism.

**And a string ships in three trees, not two.** The grey screen, the painted screen, and the
component's own page in `ui-kit/` where that component is shown carrying it. A specimen on the stand
holds either a QUOTATION, which must equal the screen, or a DEMONSTRATION, which may say anything
because it is showing a property rather than a placement. **A wrong word renders perfectly**, so no
instrument in this repository will ever tell you about it.

**The stand carries COMPONENT strings, not SCREEN strings**, so a screen whose words stand on no
specimen touches two trees and not three. Do not assume that; check it, by searching the stand for
the strings you changed. The third tree is a place a string may live, not a place every string
lives.

**And the inventory is a tree too, not a note about the other two.** It is the file a person is told
to read before writing a word, so a string that has drifted in the inventory and not in the screens
is the version the next writer will copy.

### 6. Then measure, and measure the instrument first

Nothing above is finished until it has been read from a browser, because **reading the source is not
reading the page** and **a missing value is a value**. The minimum, and every one of these is a rule
in `CLAUDE.md` with the defect that bought it written beside it:

- **two engines and both protocols.** Chromium and WebKit, over `file://` as well as `http://`. Three
  defects here were invisible to one engine, and `file://` gives every file its own opaque origin.
- **at the rungs and one pixel either side**, not at two comfortable widths. A defect can live
  entirely between the two widths everybody reads, and the ladder is in `rem`, so it moves with the
  reader's own default font size.
- **both themes, with a theme control.** These pages boot the theme from storage and the boot script
  REMOVES the attribute when the key is absent, so setting the attribute is not setting the theme.
  The page ground has to DIFFER between the two runs or you have measured one theme twice.
- **the branch you are measuring has to be the branch that is on.** The touch floor lives inside a
  coarse-pointer query and a headless browser is a fine pointer, so assert the query matches inside
  the page before believing a tap-target number.
- **document height, in both trees.** One number per render and the cheapest check here. A dialog
  missing its open attribute once put a tall sheet after the footer on nearly every painted document
  and every other instrument passed it.
- **a positive control on every sweep.** Prove the probe can see the thing before believing that it
  saw nothing. **A reading that cannot come back red is a reading of the guard, not of the thing**,
  and a zero from a blind probe is indistinguishable from a zero from a clean tree.
- **read the SET, not the document.** The defects that survive everything above are the ones that
  need two documents to be visible at once: the same market Open on one tab and won on the next, a
  panel marking the wrong row as current, a string that drifted in one tree. Every instrument here
  reads one document, so a fact standing on two documents is owned by neither.

**And write the sweep in a scratch folder, run it, delete it, and describe it in the commit.** A
script kept in the repository is a script somebody runs later against a tree that has moved on.

### 7. What to write down, and where

- What was decided and why goes in `docs/decisions.md`, dated, newest first, never edited.
- What you found and did not fix goes in `docs/backlog.md`, as a row with its source.
- A rule you had to invent to finish goes in the `CLAUDE.md` of the folder it governs, **with the
  measurement that produced it.** A rule with no reason is a rule that gets argued away by whoever
  meets it next.
- A count you type is a live claim that nothing will ever re-check. **Compute it, or date it and say
  the day.**

---

## The one paragraph you add

Say what the feature is, which node in `ia/docs/sitemap.md` it corresponds to, and which job it
closes. Then say what you expect the state list to be, and let the repository disagree with you:
`wireframes/_conventions.md` and the flow are what decide it, and a state you did not expect is more
often a state that exists than a state you should skip.

If you cannot name the node, that is the first thing to resolve and it is not a design question.

---

## What this file does not own

What the product does, in `behaviour.md`. What a screen is made of, in `map.md`. What is promised to
a reader who cannot use the product the ordinary way, in `a11y.md`. What a reader with no context
could not work out, in `onboarding-gaps.md`. Every rule this file points at, in the `CLAUDE.md` that
owns it.
