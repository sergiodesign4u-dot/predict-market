#!/usr/bin/env python3
"""_levels.py  -  which file OWNS a class, what each component CONTAINS, and
therefore what level it sits at: atom, molecule, organism.

WHY THIS FILE EXISTS. Two questions in this repo need the same answer and used
to compute it twice. `_gen_component_pages.py` needs the owner map to say which
classes a component owns and which screens it stands on; the inventory needs it
to say what stands INSIDE a component, which is the level. Two copies of one map
is the defect step 7c closed between coverage.md and the css headers, and step 9
closed again between the two panel generators: one computation feeds both, or
they drift and nobody can tell which to believe. So the map lives here and both
tools import it.

WHY THE LEVEL IS COMPUTED AND NOT TYPED. A level is not an opinion, it is
arithmetic over containment: level = 1 + the highest level of what the component
contains, with 3 as the ceiling. Typing it into inventory.md by hand would make
the table a second source for a fact the markup already answers, and it would be
stale the first time a component gains a part.

HOW CONTAINMENT IS READ, AND THE TRAP IN IT. From the specimen DOM, and only
from the DESCENDANTS of the component's own root element. A specimen wraps its
subject in the context it needs in order to render: the yesno pair sits inside
.card inside .grid inside main.feed. A flat scan of class attributes therefore
reads ANCESTORS as contents, and every component in the product comes out an
organism (the first cut of this file returned 33 of 38). The question is what
stands inside the element this component owns, not what the page around it is.

PATTERNS is read from the folder rather than typed, because a file in
components/patterns/ IS the declaration; what this file adds is the consequence,
which is that it loads last and is counted as nothing else.

WHAT IS DECLARED HERE RATHER THAN COMPUTED. Seven lists, and a reader should
know they exist before being surprised by a level: SHARED (words no component
owns), NOT_A_COMPONENT (the substrate), MODIFIER (words that name a state),
RAISE (the floors below), ORDER_BREAK (containment cycles, dropped for ordering
only), SPECIMEN_DEBT (stands that are short for a known reason, and every entry
a debt) and STATIC (the components that deliberately get no interaction states).
Each entry is one line with its reason. `ui-kit/docs/architecture.md` has the
table of all seven and who closes each.

WHAT ARITHMETIC CANNOT SEE. Two things:

  - a component whose parts are all its OWN classes contains nothing a class map
    can name, so containment reads zero. The featured hero band is four blocks
    (a market with a chart, trust cards, a brand tile, a ranked list) and 51
    classes, all of them hero's, so the arithmetic calls it an atom;
  - a screen SHELL is an organism because of what it is, not because of what it
    happens to hold. The bottom nav holds no component and is still the tab bar
    of every screen.

WHAT THE MAP CANNOT SEE. It knows components and does not know STATES, so a
state word written as a subject gets handed to whichever file wrote it with the
fewest ancestors, and every element in that state then reads as a root of the
wrong component. MODIFIER below names them; the reasoning is at the declaration.

Those are RAISE below, one line and one reason each, read rather than matched by
pattern, in the shape SHARED already uses in _gen_component_pages.py. A raise is
a FLOOR, so it propagates: raising yesno to a molecule makes the option row that
holds it an organism. And it only ever goes UP, because an error downward breaks
the cascade (a part imported after the whole) while an error upward only makes a
group less homogeneous.

    python3 ui-kit/_levels.py            # the table
    python3 ui-kit/_levels.py --why      # with every class that was found inside

No em dash.
"""
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
SPEC = ROOT / "ui-kit" / "specimens"

# ---- which file OWNS a class, and therefore where a component STANDS --------
# `classes` in the page generator is every class a file mentions, which is the
# right answer to "what does this file style" and the WRONG one to "where does
# this component stand". market.css styles `.market-title .ic`: the icon is the
# subject of that rule, so `.ic` landed in market's class list, `.ic` is on all
# 76 screens, and coverage.md reported that a market-depth panel stands on every
# screen in the product, 404 included. Thirty-four of thirty-six rows read 76 for
# that reason, while the "Stands on:" line hand-written in each css header read
# the truth. Two artifacts of one system disagreeing is the defect; one
# computation feeding both is the fix, so this block writes that header line too.
#
# A class is OWNED by the file that styles it with the FEWEST ancestors. base.css
# says `.ic{}` with none, card.css reaches it as `.card .ic`, and the file that
# describes a thing in its own right owns it. A tie goes to the earlier file in
# the cascade, which is an order index.css already fixes on purpose.
#
# SHARED is the short hand-checked list of words no component owns: a state and
# three widths that six and three files respectively write as a modifier on their
# own class. Attributing `.sel` to whichever file happens to mention it most is
# how a bet panel came to stand on 76 screens. Every entry was read, not matched
# by pattern.
SHARED = {
    "sel": "the selected state, written by six components on their own class",
    "w40": "a skeleton width, written by three components on their own line",
    "w60": "a skeleton width, written by three components on their own line",
    "w70": "a skeleton width, written by three components on their own line",
    "w80": "a skeleton width, written by three components on their own line",
}
COMBINATOR = re.compile(r"\s*[>+~]\s*|\s+")
PSEUDO = re.compile(r"::?[a-zA-Z-]+(?:\([^)]*\))?")


def split_top(sel):
    """The selector list, split only at commas OUTSIDE brackets.

       A plain .split(",") is right until the day a selector uses :is() with more
       than two members, and then it is wrong in a way nothing shows. Splitting
       `.app-case :is(.bet-panel,.bet-sheet,.bet-dock) .confirm-btn` on every comma
       hands back `.bet-sheet` on its own: a bare class at depth 0, which reads as
       a component's ROOT. `.bet-sheet` moved from betpanel to button on that
       fragment alone, and with it the level of two organisms and four rows of the
       containment map. A two-member :is() hides it, because the middle fragment
       still carries the tail; the third member is what puts a comma on both sides
       of one name.
       Found on 2026-08-02 by gate 24, which is the gate for exactly this: it asks
       whether a stand still shows what the product contains, and the answer went
       false because the reader changed its mind about who owns a class."""
    out, depth, cur = [], 0, []
    for ch in sel:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append("".join(cur))
            cur = []
            continue
        cur.append(ch)
    out.append("".join(cur))
    return out


def subjects_of(body):
    """class -> the fewest other classes in any selector where it is the subject."""
    found = {}
    text = re.sub(r"/\*.*?\*/", "", re.sub(r"url\([^)]*\)", "", body), flags=re.S)
    for m in re.finditer(r"([^{}]+)\{", text):
        sel = m.group(1)
        if sel.lstrip().startswith("@"):
            continue
        for one in split_top(sel):
            one = one.strip()
            if not one:
                continue
            depth = len(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", PSEUDO.sub("", one))) - 1
            last = PSEUDO.sub("", COMBINATOR.split(one)[-1])
            for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)", last):
                found[c] = min(found.get(c, 99), depth)
    return found


_CASCADE = [ln.split('"')[1][:-4] for ln in
            (COMP / "index.css").read_text(encoding="utf-8").splitlines()
            if ln.startswith("@import")]
SUBJECTS = {}
for _path in sorted(COMP.glob("*.css")):
    if _path.stem in ("index", "tokens"):
        continue
    # subjects_of strips every comment itself, so the header slice this used to
    # take is not needed and was never enough: it cut only the first block.
    SUBJECTS[_path.stem] = subjects_of(_path.read_text(encoding="utf-8"))
OWNER = {}
for _c in {c for d in SUBJECTS.values() for c in d}:
    if _c in SHARED:
        continue
    OWNER[_c] = sorted(((d[_c], _CASCADE.index(f) if f in _CASCADE else 99, f)
                        for f, d in SUBJECTS.items() if _c in d))[0][2]
OWNED = {}
for _c, _f in OWNER.items():
    OWNED.setdefault(_f, set()).add(_c)

# ---- what stands inside, read from the specimen DOM -------------------------
# A component is not a level; a component's CONTENTS are. base.css is the page
# frame and course-chrome.css is the course sidebar: neither is a thing a screen
# is composed of, and the inventory has said so about the sidebar since it was
# written. fonts.css has no markup at all.
NOT_A_COMPONENT = {
    "base": "the page frame and the groove system, the substrate rather than a part",
    "course-chrome": "course chrome, not product (the inventory says so on its own row)",
    "fonts": "no markup: it declares the faces",
}

# ---- the words that name a state and not a thing ----------------------------
# The ownership map knows components and does not know STATES, so when a state
# word is written as a subject anywhere it has to be given to somebody, and the
# somebody is arbitrary. `.skeleton` is the loading state of whatever it sits on.
# `position.css` writes `.app-case .pos.skeleton{gap:...}` with it as the subject
# and `skeleton.css` only ever writes it as an ancestor (`.card.skeleton
# .sk-thumb`), so "fewest ancestors" handed the word to position. Both rules are
# correct where they stand: a position in the loading state really does want a
# different gap. What was wrong is the map, so the map is where this is fixed.
#
# The consequence of not declaring it: `<article class="card skeleton">` on
# nineteen loading screens read as a POSITION root, and position came out
# containing card, account, event-detail and hiw-dialog. Four phantom edges, one
# of them enough to move a level.
#
# The reader skips these in BOTH directions, and it has to be both. Skipping them
# only at the root leaves the same phantom one element higher: the feed holds the
# card, so the feed would then read as containing position. A state is not a part
# of anything, wherever it is found.
#
# Ownership itself is left alone on purpose. `position.css` does style
# `.pos.skeleton`, so coverage.md is right to list the class under position; the
# question this map answers is a different one, and only this map was wrong.
#
# Stage 09 is the reason it is a declaration and not a special case: hover,
# focus-visible and disabled are the same species, states written by one file as
# a modifier on another file's element. Moving css under each of them would be
# this work six more times.
MODIFIER = {
    "skeleton": "the loading state of whatever it sits on, written as a subject "
                "by position.css and as an ancestor by skeleton.css",
}

# ---- the components that get no states, and why -----------------------------
# The states pass has to answer for all 36 files, and "this one has no :hover"
# reads identically whether it was decided or forgotten. So the decision is
# written down, one line each, and gate 25 makes the list load-bearing in both
# directions: nothing here may declare a :hover or an :active, and nothing NOT
# here may lack them. An exception list that can absorb a component quietly is
# not a declaration, it is a way of switching the check off.
#
# The rule that produced it: a state belongs to what a person can press or type
# into. A badge, a heading, a bar drawn to a width and a table of figures have no
# interaction to have a state OF, and inventing one inflates the system exactly
# the way an empty semantic role did on the previous stage. Where a block LOOKS
# interactive but the control inside it belongs to another file, the entry says
# which file, because that is the question the next reader will actually have.
# ---- the third answer to "does this control have a press" --------------------
# GATE 25 ASKS FOR HOVER AND ACTIVE AND KNEW TWO ANSWERS: a component has both,
# or it is in STATIC and has neither. `input` is the case that is neither, and it
# only became visible on 2026-08-05, when `.quick` left that file for
# components/quick.css and took the press with it.
#
# A TEXT FIELD HAS NO PRESS, and that is a fact about the control rather than a
# gap in it. The pointer going down on a field moves the caret; what follows is
# FOCUS, which this component declares twice on purpose (`:focus` for "the field
# is active, however you got here" and `:focus-visible` for the keyboard ring),
# with the reasoning written at the rules. Inventing an `:active` to satisfy a
# gate would put a state on the screen that answers nothing, which is the exact
# defect gate 25 exists to prevent, arrived at from the other side.
#
# The list is deliberately not "components that may skip a state". Every entry
# names the state it does not have and why the control cannot have it, and the
# gate still requires the OTHER one: a row here with no hover would fail.
NO_PRESS = {
    "input": "a text field. The pointer going down on it moves the caret, and the "
             "state that follows is focus, not press. It declares hover, :focus and "
             ":focus-visible; an :active would be a face that answers nothing",
}

STATIC = {
    "base": "the page frame. It owns the one :focus-visible the whole system reads "
            "and has no control of its own except a visibility utility",
    "oddsbar": "a datum drawn to a width. It reports the market and answers no pointer",
    "skeleton": "the loading mark. It stands where a control will be and is replaced by it",
    "seo-plate": "the reading block at the foot of a feed: prose and a brand column, "
                 "with no link inside it on any of the 105 screens",
    "trustbar": "three trust statements. A claim, not a destination",
    "bets-table": "the holders and activity rows. Read-only figures; a row opens nothing",
    "chart": "the plot. Its time-range switch is .ed-range and lives in tabs.css, "
             "which does have states",
    "feed": "the grid the cards stand in. Every control inside it belongs to card, "
            "catnav or loadmore",
    "notice": "the banners and boxes. Their buttons are .state-btn and belong to button",
    "account": "the action bar's own surface, and nothing else since 2026-08-03: a stone, "
               "a hairline along the top edge, two rounded corners, and the three "
               "declarations .flat takes them away with. The button it used to paint went "
               "to button.css where the rest of that family already was (backlog S11), so "
               "the bar answers no pointer because a bar is not a control. This entry is "
               "the same shape as notice above and for the same reason",
    # TWO ENTRIES ADDED 2026-08-06, AND BOTH WERE EARNED RATHER THAN CLAIMED.
    # Neither file went quiet by losing a state; each went quiet by losing a
    # CONTROL to components/iconbtn.css, and what is left in both is a surface
    # and a placement. That is the shape this list already had: `notice` and
    # `account` are here for exactly the same reason, one migration earlier.
    "bottomnav": "the bar the slots stand in, and nothing else since 2026-08-06: sticky to the "
                 "bottom, one ground, a groove along its top edge, a list, a rule between slots "
                 "and the balance figure one of them carries. The slot went to navitem with its "
                 "hover, its press and its current-page state, and a BAND is not pressed. Same "
                 "reason as notice and account below, one migration later",
    "profile": "the identity row, the reputation grid and the gallery. Its one control, Edit, went to button on 2026-08-06 and took its hover and its press with it: one placement is the wrong size for an exception, so the element takes the family's small step. What is left is a head and a rail, and neither is pressed",
    "event-detail": "the head, the facts strip and the sections of one event. The three "
                    "marks in the corner of the head went to iconbtn on 2026-08-06 and "
                    "took their hover, their press and their favourited state with them; "
                    "what is left is where that row sits, and a row is not a control",
    "toast": "a message, a lift and a place for one control. The dismiss went to "
             "iconbtn on 2026-08-06 with everything that answered a pointer, and the "
             "one declaration left here is `flex:0 0 auto`, which says the message "
             "takes the slack. A toast itself is not pressed: it is read and it leaves",
    "options": "the multi-outcome list. The row is a <div>; what a person presses is "
               "the .yesno pair inside it, which has its own states. The row ALSO "
               "carries a JS click handler and no keyboard path, which is a defect "
               "of the markup and belongs to the grey tree, not to a state rule",
}

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class _Node:
    __slots__ = ("tag", "cls", "kids", "parent")

    def __init__(self, tag, cls, parent):
        self.tag, self.cls, self.kids, self.parent = tag, cls, [], parent


class _Tree(HTMLParser):
    """Enough of a DOM to ask what is under an element. A regex cannot answer
    that question: it has no idea where an element ends."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = _Node("#root", set(), None)
        self.cur = self.root
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
            return
        if self.skip:
            return
        cls = set((dict(attrs).get("class") or "").split())
        node = _Node(tag, cls, self.cur)
        self.cur.kids.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.cur.tag == tag:
            self.cur = self.cur.parent

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or tag in VOID:
            return
        node = self.cur
        while node is not self.root and node.tag != tag:
            node = node.parent
        if node is not self.root:
            self.cur = node.parent


def _walk(node):
    for kid in node.kids:
        yield kid
        yield from _walk(kid)


def read_containment(paths, component_of=None, only=None):
    """What stands inside each component, read from a set of documents.

    ONE READING, TWO CORPORA, and the difference between them is only the outer
    loop. A SPECIMEN is one document for one component, so `component_of(path)`
    names which one; a SCREEN is one document holding every component at once,
    so `component_of` is None and each component is looked for in turn. The
    reading itself, and the trap it avoids, must be the same in both or the two
    answers cannot be compared, which is the entire point of comparing them.

    THE TRAP. Take the TOPMOST elements carrying a class the component owns, and
    then only what stands UNDER them. Anything above is the context the document
    needed in order to render: a specimen wraps its subject in a card in a grid
    in `main.feed`, and a screen wraps everything in `.device`. A flat scan of
    class attributes reads those ANCESTORS as contents, and returned 33
    organisms out of 38 the first time it was tried.

    `only` names which components to look FOR, and defaults to the composable
    ones. It is a parameter rather than a constant because an audit has to be
    able to ask about `base` and `course-chrome` too: they are declared not to be
    parts, and a declaration that is never tested is the same silent gap this
    file exists to close. What they may CONTAIN is filtered separately, below,
    and that filter is not optional: the substrate is not a level.

    MODIFIER is skipped on both sides, for the reason written where it is
    declared: a state word names no thing, so it neither opens a root nor counts
    as something standing inside one.

    Returns {component: {other_component: {the classes that linked them}}}.
    """
    found = {}
    for path in paths:
        tree = _Tree()
        tree.feed(path.read_text(encoding="utf-8"))
        nodes = list(_walk(tree.root))
        if component_of is None:
            comps = list(only) if only is not None else [
                c for c in SUBJECTS if c not in NOT_A_COMPONENT]
        else:
            one = component_of(path)
            if one is None:
                continue
            comps = [one]
        for comp in comps:
            mine = OWNED.get(comp, set()) - set(MODIFIER)
            if not mine:
                continue
            roots = []
            for node in nodes:
                if not (node.cls & mine):
                    continue
                up, covered = node.parent, False
                while up is not None:
                    if up in roots:
                        covered = True
                        break
                    up = up.parent
                if not covered:
                    roots.append(node)
            for root in roots:
                for kid in _walk(root):
                    for cls in kid.cls - set(MODIFIER):
                        other = OWNER.get(cls)
                        if other and other != comp and other not in NOT_A_COMPONENT:
                            found.setdefault(comp, {}).setdefault(other, set()).add(cls)
    for name in SUBJECTS:
        found.setdefault(name, {})
    return found


def _read_containment():
    index = json.loads((SPEC / "index.json").read_text(encoding="utf-8"))
    of_specimen = {s["id"]: s["component"] for s in index}
    return read_containment(sorted(SPEC.glob("*.html")),
                            component_of=lambda p: of_specimen.get(p.stem))


CONTAINS = _read_containment()

# ---- the floors arithmetic cannot reach -------------------------------------
# Each line is a component whose level the containment map reads too low, with
# the reason. Two kinds only: a block whose parts are all its own classes, and a
# shell that is an organism because of what it IS. A floor propagates.
RAISE = {
    # screen shells
    "header": (3, "a screen shell: the chrome band every screen carries"),
    "bottomnav": (3, "a screen shell: the mobile tab bar"),
    "catnav": (3, "a screen shell: it owns .cat-layout and .cat-main, the page content plate"),
    # footer was here and was deleted on 2026-08-02. Every entry was tested by
    # removing it and asking whether the level moved; footer's did not. It holds
    # a language menu and a trust bar, so the arithmetic reaches L3 on its own
    # and the floor was carrying nothing. A declaration that changes no answer is
    # worse than none: it reads as the reason, and the real reason goes unread.
    "state-block": (3, "the empty and error block, an organism by definition"),
    "hiw-dialog": (3, "the arithmetic cannot prove this one while the page and the dialog "
                      "live in one file. .hiw-hero and .hiw-cols are blocks of the "
                      "standalone How It Works PAGE, under main.feed, and the narrow "
                      "shared sheet hangs under body: two components sharing one "
                      "vocabulary, which is backlog item 16. Until they are split, "
                      "what the specimen shows is a choice between them and not a "
                      "reading of either"),
    # parts that are all the component's own classes
    "hero": (3, "four blocks in one band (featured market with its chart, trust cards, "
                "brand tile, ranked list), 51 classes, every one of them hero's"),
    "market": (2, "a collapsible with a head, a body and a price table, all its own classes"),
    # Added 2026-08-03, and it is the SECOND half of moving `.seg` into this file
    # (docs/backlog.md 17). While the sort switcher was declared in tabs.css the
    # arithmetic read comments as containing tabs and called it an organism; with
    # the class in its own file it contains nothing a class map can name and the
    # arithmetic calls it an ATOM, next to button. Both readings are the map being
    # right about the wrong question. Structurally it is `market`: a section with a
    # head, a control strip, a list and a compose box, every class its own.
    "comments": (2, "a thread with a sort switcher, a compose box and per-comment "
                    "actions, all its own classes"),
    "related": (2, "a list of rows"),
    "seo-plate": (2, "two columns of sections"),
    "trustbar": (2, "a strip of trust items"),
    "account": (2, "a bar of two actions whose buttons carry no class of their own"),
    "toast": (2, "a message and a close, stacked"),
    "yesno": (2, "a pair of controls in a container"),
    # ---- 2026-08-05, and these four are the whole of the atom shelf being read
    # rather than assumed. See TRUE_ATOM below for why they had no line until now.
    # PAID 2026-08-05, and the line stays because the level is still declared.
    # `input` and `filters` were raised as FINDINGS on the morning of the same day,
    # each with "closes by splitting" in it, and the split is what happened: `.quick`
    # went to components/quick.css and `.toggle` to components/toggle.css. What is
    # left in each file is one thing, and each is still a molecule for a reason the
    # containment map cannot see, which is what a RAISE is for.
    "filters": (2, "a disclosure over a panel over a list of labelled radios, all its "
                   "own classes. It held a switch as well until 2026-08-05 and that is "
                   "the part that was wrong, not the level"),
    "quick": (2, "a ROW of chips a person chooses between. The chip is the atom and the "
                 "row is this; the chip is also drawn in four other files, which is the "
                 "merge backlog S41 still owes"),
    # EXAMINED 2026-08-05 AND FOUND CORRECT AS FILES, WRONG ONLY AS LEVELS. Both
    # were on the unexamined atom shelf; neither owes a cut. Named here so the next
    # reader does not go looking for one.
    "skeleton": (2, "`.sk-line` and `.sk-thumb` are the atoms and `.sk-head` and "
                    "`.sk-row` ARRANGE them, which is the whole of why this is L2. "
                    "`.sk-btn` reads at first like a placeholder named after another "
                    "component's control and it is not a defect: standing where a "
                    "specific thing will be is the entire job of a skeleton, and the "
                    "name says which thing"),
    "toc": (2, "a disclosure over a list of numbered links, the same shape `related` "
               "is declared at: `.toc-d` is a `<details>`, `.toc-head` its summary, "
               "`.toc-list` the list, `.toc-link` the row. It stands on ONE painted "
               "screen, terms.html, and that was checked rather than assumed: one "
               "screen is a small component, not a wrong one, and `toast` stands on "
               "one too"),
}

# ---- the answer the arithmetic gives when it has NOTHING to read -------------
# AN EMPTY CONTAINMENT IS NOT EVIDENCE OF BEING AN ATOM, and until 2026-08-05
# this file could not tell the two apart. `_level()` returns 1 when `CONTAINS` is
# empty, and `CONTAINS` is empty in two completely different situations: the
# component really is ONE control with nothing inside it, or the component is
# built entirely out of its OWN classes and the map, which only knows component
# names, can see nothing at all. The docstring above says as much in the section
# headed "WHAT ARITHMETIC CANNOT SEE" and RAISE exists to answer it.
#
# What was missing is the check that anyone LOOKED. Seventeen components have an
# empty containment. Ten carried a RAISE with a reason. The other seven were the
# entire atom shelf - button, filters, input, loadmore, oddsbar, skeleton, toc -
# and not one of them had ever been examined: they were called atoms by a
# function that had no information, and `ui-kit/docs/inventory.md` and the
# vitrine's side panel then printed that as a design decision.
#
# So an empty containment is now a QUESTION the build asks. A component with one
# has to be in RAISE (the map cannot see inside it, here is what is in there) or
# in this list (the map saw nothing because there is nothing: it is one control).
# Gate 39 fails when a component is in neither, and when a row here names a
# component whose containment is NOT empty, because then the arithmetic has an
# answer of its own and a declaration is a second one.
TRUE_ATOM = {
    "iconbtn": "one control and two modifiers, and nothing may be put inside it but the "
               "mark it exists to hold. It is not a modifier of `button` either: it has no "
               "label to size, and its own box IS the target, which is why the 44 floor is "
               "written on the box rather than around it",
    "chip": "one control and one shared modifier. `.chip` is a label a person picks "
            "between, and `.sel` says which one is picked; there is nothing inside it and "
            "nothing may be put inside it. The containers it stands in are somebody "
            "else's - the `.seg` trough belongs to the comment controls, the `.ed-range` "
            "rail to the chart head - which is the whole reason it needed a file rather "
            "than a home in one of them",
    "button": "one control and three modifiers. It was five names and a size encoded in "
              "a place until 2026-08-05, and the migration is what makes this line "
              "sayable: `.btn` plus an emphasis, a size and an optional `.btn-block`, "
              "and nothing else in the file",
    "oddsbar": "a bar. `.track`, `.fill` and the two labels are its own anatomy and not "
               "controls of their own: nothing in it can be pressed, and no other "
               "component may stand inside it",
    "input": "a label, a field and the row that holds them. It held `.quick`, a GROUP "
             "of chips, until 2026-08-05, and that is what made the empty containment "
             "a lie rather than an answer; the group is components/quick.css now and "
             "what is left really is one control",
    "toggle": "a track and a knob. It stood inside components/filters.css until "
              "2026-08-05, beside a sort menu it shares nothing with but a file name, "
              "and the stand had been saying so since it was built by needing two "
              "specimens for one component",
    "loadmore": "one control, and the level is right while the COMPONENT is not. Read in "
                "a browser over 105 painted screens, `.load-more` and `.cat-nav button` "
                "are the same graphite chip: same ground `--bg-chip`, same 6 per cent "
                "edge, same corner, same 14px semibold, same hover and press. They "
                "disagree on side padding (24 against 20), on letter-spacing and on "
                "min-height, and nothing predicts which a place gets. An atom that "
                "duplicates another component's control is still an atom; it is also a "
                "component that should not exist. Backlog S41",
}

# ---- the stands that are short, and are short for a KNOWN reason -------------
# `_audit_specimens.py` compares what a component contains in its stand against
# what it contains on the 105 painted screens. A stand that is short makes the
# containment map short, the level comes out low, and a RAISE floor covers the
# difference: the level is then DECLARED and nothing says it was. That comparison
# only becomes a gate once the base is clean, so every difference that is NOT a
# thin stand is written out here, with what closes it.
#
# EVERY ENTRY IS A DEBT AND NOT A DESIGN. Read one of these in six months and the
# temptation is to read it as configuration, which would make the page plate
# inside a component file a legitimate arrangement. It is not one. Each line says
# what closes it, and closing means SPLITTING the component, never extending the
# exception.
#
# A part of "*" means the difference is unbounded by cause: the component owns a
# CONTAINER (a page plate, a tab panel, a page of its own), so whatever the page
# happens to hold reads as standing inside it, and listing today's contents would
# be a list that churns with every screen. A NAMED part is used where the cause is
# one specific element or one class in the wrong file, because there a new name is
# a new fact and the gate should say so.
_PLATE = ("owns a page-level plate, so on a screen the whole page is its "
          "descendant. True, and useless. Closes when the plate leaves the "
          "component file, see item 16, not by widening this line")
SPECIMEN_DEBT = {
    # ("catnav", "*") was here and is PAID, 2026-08-03. .cat-layout and .cat-main
    # went to components/patterns/browse-shell.css and their plate to base.css, so
    # catnav owns no page-level anything and its stand shows the whole of it. This
    # is what a debt looks like when it closes: the line is deleted, not widened.
    ("feed", "*"): "main.feed, the screen's own <main>, so on a screen everything is "
                   "its descendant. HALF PAID on 2026-08-03: .feed-inner and the "
                   "plate left for base.css with the rest of the frame, and .grid, "
                   ".feed-head and .feed-controls left for patterns/. What is left is "
                   "the element itself, and that closes when main.feed is read as the "
                   "page rather than as a component, not by moving another rule",
    ("event-detail", "*"): ".ed-section, a content panel that holds a chart, a market "
                           "box or a tab set, so the first one on a screen reads as "
                           "containing them. HALF PAID on 2026-08-03: .ed-layout went "
                           "to patterns/detail-shell.css and the .ed-main plate to "
                           "base.css, which is the half this entry used to name. The "
                           "rest is item 16d, the detail page being several things in "
                           "one file",
    # OPENED BY THE VOCABULARY, 2026-08-05, and it is a defect the class map could
    # not see before. The action bar's two buttons carried NO class of their own
    # until the migration, so no containment reader could name them; they carry
    # `.btn` now, and the moment they did, `position` read as containing a button.
    # It does, on exactly one screen: `ui-visual/my-profile.html` puts the CTA bar
    # INSIDE `<article class="pos">`, and `ui-visual/wallet.html` puts the same bar
    # beside it as a sibling. Two screens disagree about whose child that bar is,
    # which is backlog item 16d seen from the containment side rather than from the
    # file side. Declared rather than staged, because staging it would teach the
    # arrangement that is probably the wrong one of the two.
    ("position", "button"): "the CTA bar is a child of article.pos on my-profile and a "
                            "sibling of it on wallet, so one of the two screens is wrong "
                            "about the bar's owner. Item 16d; closes when the two agree",
    ("tabs", "*"): "the .ptab-panel is a content panel, so a profile tab holds a card "
                   "gallery and a position record. The switcher and the panel are one "
                   "file, item 16; closes when they are two",
    # ("toast", "*") was here and is PAID, 2026-08-03. .tc-page moved to base.css:
    # it is the section of the catalogue that stands in for the page underneath,
    # not a part of a toast, and having it in toast.css is why the toast read as
    # containing the cookie banner. Backlog item 16c.
    ("hiw-dialog", "*"): "the standalone How It Works PAGE and the narrow shared sheet "
                         "are one file with one vocabulary, so the hero band and the "
                         "position plate on the page read as inside the dialog. This is "
                         "the debt that keeps the last guessed level alive: item 18, and "
                         "it closes by splitting the page from the dialog",
    ("dialog", "hiw-dialog"): ".app-dialog and .hiw-dialog sit on ONE element, so each "
                              "reads as containing the other. Item 15: fold it in, or "
                              "split it, but not a third copy of the sheet",
    ("dialog", "betpanel"): ".app-dialog and .bet-sheet sit on one element, and the three "
                            ".bet-sheet rules are inside dialog.css. Item 17: they belong "
                            "in betpanel.css",
    ("dialog", "options"): "the same element again: the option summary stands inside the "
                           "bet sheet, which the dialog only appears to hold because "
                           "the two classes share a root. Closes with the line above",
    ("position", "account"): "`.pos` is used as a generic plate on my-profile.html and "
                             "holds an account CTA bar. position is four things in one "
                             "file (row, list, summary, resolved history), item 16",
    ("position", "hiw-dialog"): "`.pos` used as a plate again, this time in the How It "
                                "Works side column. Closes with item 16, and the hiw "
                                "half of it with item 18",
}


def debt_covers(comp, part):
    """Is this (component contains part) difference already declared?"""
    return (comp, "*") in SPECIMEN_DEBT or (comp, part) in SPECIMEN_DEBT


def examined():
    """Gate 39: every empty containment is a decision somebody took.

    Returns (unexamined, idle, count), where `unexamined` is every component the
    map could see nothing inside and that neither RAISE nor TRUE_ATOM speaks
    about, `idle` is every TRUE_ATOM row for a component whose containment is NOT
    empty (the arithmetic has its own answer there, so the row is a second one),
    and `count` is how many empty containments were read.

    The check runs in both directions on purpose, which is the shape every
    declared list in this repo carries: a missing row is a component nobody
    looked at, and an idle row is a claim that stopped being about anything.
    """
    empty = [n for n in sorted(SUBJECTS)
             if n not in NOT_A_COMPONENT and not CONTAINS.get(n)]
    unexamined = [n for n in empty if n not in RAISE and n not in TRUE_ATOM]
    idle = [n for n in sorted(TRUE_ATOM) if n not in empty]
    return unexamined, idle, len(empty)


LEVEL = {}


def _level(name, seen=()):
    if name in LEVEL:
        return LEVEL[name]
    if name in seen:
        # tabs holds the panels and a panel holds a tab strip. A cycle is two
        # organisms by construction, so the ceiling is the answer.
        return 3
    inner = CONTAINS.get(name, {})
    value = 1 if not inner else min(3, 1 + max(_level(i, seen + (name,)) for i in inner))
    value = max(value, RAISE.get(name, (0, ""))[0])
    LEVEL[name] = value
    return value


for _name in SUBJECTS:
    if _name in NOT_A_COMPONENT:
        LEVEL[_name] = 0
for _name in SUBJECTS:
    _level(_name)

NAME = {0: "-", 1: "L1", 2: "L2", 3: "L3"}

# ---- the order the cascade has to load them in ------------------------------
# A part is imported BEFORE the whole that holds it. Not a preference: two files
# of equal specificity that reach the same element are decided by source order,
# and the one that describes the smaller thing has to be the one that can be
# overridden, not the one that overrides. The order this replaced was the order
# the rules had been layered in inside the flat kit, and it put twenty six wholes
# ahead of their parts, header before button and card before both of the controls
# it holds.
#
# The order is a topological sort of CONTAINS, and among components that no
# constraint separates it keeps the order the file already had, because the
# smallest reordering that satisfies the rule is the one least likely to move a
# pixel.
#
# ORDER_BREAK is the only hand-written part, and it exists because containment
# has one cycle in it: the tab strip holds the comments panel, and the comments
# panel holds a segmented switcher, and every switcher in the product is written
# in tabs.css. A cycle has no topological order, so the tie is declared rather
# than resolved by whichever name sorts first. It is dropped for ORDERING ONLY:
# the edge is real, so it still counts toward the level, and comments stays an
# organism.
#
# The three added on 2026-08-02 arrived with the specimen fixes, and every one of
# them is a cycle both halves of which are readable in the markup. A cycle is not
# a defect in the reading, it is what a class graph does when two components
# stand inside each other on different screens; what has to be declared is which
# way round the CASCADE needs them, and that is decided by which file restyles
# the other's insides.
# TWO OF THE FOUR WENT AWAY ON 2026-08-03, and not by a better tie-break: the CYCLES went
# away, because both were made of a class declared in the wrong file (docs/backlog.md 17).
# `.seg` moved from tabs.css to comments.css and `.rp-inner` from event-detail.css to
# betpanel.css, and with them the edges that had to be declared by hand. That is the
# argument for reading the order out of the markup rather than typing it: a hand-written
# tie-break is a place where the map stopped agreeing with the files, so an entry here is
# a finding waiting to be closed, not a setting.
ORDER_BREAK = {
    ("card", "event-detail"): "the header of the detail page is composed as a card, so the card "
                              "really does hold .ed-head; event-detail.css restyles what is "
                              "inside a card and not the other way round, so the card is the "
                              "part and loads first",
    ("notice", "dialog"): ".fine is the small print, a typographic role that dialog.css happens "
                          "to own and that stands in bet panels and spinner boxes too. The "
                          "dialog holds the notice, so the dialog loads after it",
    ("navitem", "bottomnav"): "the map reads this one BOTH ways and it is right both times: the "
                              "bar holds five slots, and the Portfolio slot holds .bn-bal, the "
                              "bar's own balance figure. A real cycle, not a misreading. The bar "
                              "is the whole - it is a band of one screen and the slot is a "
                              "control that also stands in an account menu - so the slot is the "
                              "part and loads first, and .bn-bal is one <span> of content the "
                              "bar puts inside its own control. Added 2026-08-06 with "
                              "components/navitem.css",
}
FIRST = ["fonts", "tokens", "base", "course-chrome"]
# ---- and the other end of the cascade ---------------------------------------
# A PATTERN IS NOT A COMPONENT, and every list in this file has to keep meaning
# one thing. components/patterns/ holds stable compositions of components, so a
# pattern has no level (it stands ABOVE the three), no owner (it owns no class
# another file could want), no specimen and no states. It is not in SUBJECTS
# because this file globs components/*.css without recursing, which is luck
# rather than design, so it is named here and the naming is the design.
#
# What it DOES have is a position: last. A pattern is assembled out of components,
# so it must be able to restyle what it holds, and in a cascade that means loading
# after all of them. FIRST pins the head for the same reason and by the same
# argument.
#
# It is NOT in STATIC either, and that is the distinction worth keeping: STATIC
# says "a component that gets no states". A pattern is not a component, so an
# entry there would be a category error, and six declarations that each mean one
# thing are worth more than seven that overlap.
PATTERNS = sorted("patterns/" + p.stem for p in (COMP / "patterns").glob("*.css"))


def _order_depth(name, seen=()):
    if name in _DEPTH:
        return _DEPTH[name]
    if name in seen:
        return 0
    inner = [i for i in CONTAINS.get(name, {})
             if i in SUBJECTS and i not in FIRST and (name, i) not in ORDER_BREAK]
    value = 0 if not inner else 1 + max(_order_depth(i, seen + (name,)) for i in inner)
    _DEPTH[name] = value
    return value


_DEPTH = {}
_CURRENT = {f: i for i, f in enumerate(_CASCADE)}
_BODY = [f for f in _CASCADE if f not in FIRST]
for _f in _BODY:
    _order_depth(_f)
_BODY = [f for f in _BODY if f not in PATTERNS]
ORDER = (FIRST
         + sorted(_BODY, key=lambda f: (LEVEL.get(f, 0), _DEPTH[f], _CURRENT[f]))
         + PATTERNS)


def order_problems(cascade):
    """Every (whole, part) the given cascade loads the wrong way round."""
    at = {f: i for i, f in enumerate(cascade)}
    out = []
    for whole in cascade:
        # the frame and the course sidebar are pinned at the head and are not
        # composed of anything: what their specimens show inside is the sample
        # content a frame needs in order to be a frame.
        if whole in NOT_A_COMPONENT:
            continue
        for part in CONTAINS.get(whole, {}):
            if part in at and (whole, part) not in ORDER_BREAK and at[part] > at[whole]:
                out.append((whole, part))
    return out


def label(stems):
    """The level of an inventory row: the highest of the components it maps to.
    A row with no component keeps the dash the CSS file column already gives it,
    because a dash is a claim of its own and not a blank."""
    levels = [LEVEL[s] for s in stems if s in LEVEL and LEVEL[s]]
    return NAME[max(levels)] if levels else "-"


def _main():
    if "--order" in sys.argv:
        for f in ORDER:
            print('@import url("%s.css");' % f)
        bad = order_problems(_CASCADE)
        print("\n# current cascade loads %d whole(s) before a part; this order loads %d"
              % (len(bad), len(order_problems(ORDER))), file=sys.stderr)
        return
    why = "--why" in sys.argv
    for lvl in (1, 2, 3):
        names = sorted(n for n in SUBJECTS if LEVEL.get(n) == lvl)
        print("\nLEVEL %d  %s  (%d)" % (lvl, {1: "atoms", 2: "molecules",
                                              3: "organisms"}[lvl], len(names)))
        for n in names:
            inner = CONTAINS.get(n, {})
            mark = " ^" if n in RAISE else "  "
            if why and inner:
                detail = "; ".join("%s (%s)" % (o, ", ".join("." + c for c in sorted(cs)))
                                   for o, cs in sorted(inner.items()))
            else:
                detail = ", ".join(sorted(inner)) or "-"
            print("  %-16s%s %s" % (n, mark, detail))
            if n in RAISE:
                print("  %-16s   raised: %s" % ("", RAISE[n][1]))
    print("\nNOT A COMPONENT (%d)" % len(NOT_A_COMPONENT))
    for n, why_not in sorted(NOT_A_COMPONENT.items()):
        print("  %-16s %s" % (n, why_not))
    print("\n%d components: %d atoms, %d molecules, %d organisms" % (
        sum(1 for n in SUBJECTS if LEVEL.get(n)),
        sum(1 for n in SUBJECTS if LEVEL.get(n) == 1),
        sum(1 for n in SUBJECTS if LEVEL.get(n) == 2),
        sum(1 for n in SUBJECTS if LEVEL.get(n) == 3)))


if __name__ == "__main__":
    _main()
