#!/usr/bin/env python3
"""
_worn.py  -  does the vitrine stage every form the product wears, and only those?

THE RULE THIS ANSWERS, in the words it was given in: everything that is on the
project has to be in the design system, and everything in the design system has
to be on the project. Both directions, and the second one is the half a vitrine
usually skips: a stand that shows a control nobody ships is teaching a scheme
that was never adopted, which is what `.btn-primary` with `.btn-sm` / `.btn-md` /
`.btn-lg` was until gate 30 counted it.

WHAT A FORM IS, AND WHY IT IS NOT A CLASS. `.provider-btn` is one class and four
different controls: 13px left-aligned in a deposit sheet, 14px centred with a
brand mark in the sign-in sheet, 14px bold centred in an outcome sheet, 13px
semibold centred in the bet panel. The stylesheet decides that by SCOPE, so a
form is the pair

    (the family class it carries, plus .primary or not)
  x (the scoping classes above it that components/button.css actually reads)

and both halves are read out of the repo rather than typed here. The family is
the four names the component's own header declares; the scopes are every other
class that appears in a selector of `components/button.css`, minus the parts
(`.ic`, `.prov-*`) and minus `.app-case`, which is on every screen and every
specimen and so separates nothing.

WHAT IT CANNOT SEE, and it says so rather than passing quietly: a control whose
container ships closed. `dialog.app-dialog.bet-sheet` has no `open` attribute in
`ui-visual/`, and `.app-case .bet-sheet .confirm-btn` sets the only padding of 16
in the family. A pass that measured the rendered tree would score that control at
zero width and never reach it. This one reads MARKUP, so it finds it, and that is
the reason it reads markup.

    python3 ui-kit/_worn.py            the two lists and the difference
    python3 ui-kit/_worn.py --check    exits 1 on a form in one list and not the other

No em dash.
"""
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
UV = ROOT / "ui-visual"
CSS = ROOT / "components" / "button.css"
COMP = ROOT / "components"

# The parts of the component rather than scopes of it, and `.app-case`, which is
# the product's own wrapper and stands above every button in both trees.
#
# `.app-dialog` JOINED THEM ON 2026-08-05, and it is a declared exception with a
# check anyone can run: `grep app-dialog components/button.css` returns one
# selector and it is `dialog.app-dialog.signin-dialog .btn`, a compound in which
# the deciding class is the second one. The scope reader takes every class it
# finds in a selector, so it was reporting `app-dialog` as a scope of its own and
# splitting four forms into eight - the same control counted twice because a
# class that decides nothing stood above it. A scope is a class the stylesheet
# reads ALONE, and this one never is. If a rule is ever written for
# `dialog.app-dialog .btn`, this entry has to come out, and the grep is how you
# would know.
NOT_A_SCOPE = {"app-case", "app-dialog", "ic", "prov-x", "prov-apple", "prov-google", "primary"}

# The specimen that is the answer, and it is ONE since 2026-08-05. It was two,
# because `components/betpanel.css` hides `.bet-dock` above 760 and `.bet-panel`
# below it, and the two forms that only the phone wore could not stand in the
# same document as the rest. A form is a set of classes now and not a place, so
# the dock's content-width brass button is `btn btn-primary btn-md` and stands
# anywhere. The vocabulary untied the forms from their scopes, and one specimen
# holds all ten.
STANDS = ["button-matrix"]

# ---- a scope that changes nothing is not a second form ----------------------
# THE FIRST CUT OF THIS CHECK STAGED SIXTEEN CONTROLS AND THE PRODUCT HAS EIGHT.
# A form here is (class, scope), which is what the markup can be asked for
# without a browser, and it OVER-COUNTS: `.confirm-btn` is written under
# `dialog.app-dialog`, under `.outcome-dialog` and under `.bet-panel`, and in
# all three the stylesheet gives it exactly the same control. Staging three of
# them put three identical brass rows on the page inside three different plates,
# which is what made the matrix read as a scatter instead of as a system.
#
# THE COMPARISON THAT DECIDES THIS IS A MEASUREMENT AND IT CANNOT LIVE IN A
# PYTHON GATE. Whether a scope changes a control is the cascade resolved, and
# resolving the cascade needs a browser. So it is a DECLARED list, in the shape
# every declared list in this repo has: each entry names the worn combination,
# the staged control that renders identically, and what was compared. The
# control on it is the usual one in both directions - an entry whose source
# nothing wears, or whose target nothing stages, fails as loudly as a missing
# form.
#
# Measured 2026-08-04 in a browser, each worn control against the same markup
# with no scope above it, in a container of the same width, over thirteen
# properties: background, gradient, edge, edge width, ink, radius, padding, font
# size, weight, justification, text alignment, gap, min-height. The four
# combinations NOT here are the four where that comparison came back different,
# and each of them is staged in its own scope.
# EMPTY SINCE 2026-08-05, AND THAT IS THE MIGRATION'S RECEIPT. Every entry here
# named a place-name whose scope changed nothing about it: `.provider-btn` under
# `dialog.app-dialog` rendering as the bare one, `.confirm-btn` under three
# different scopes rendering as one control, `.state-btn` in a resolved panel
# differing only by a width. Six rows, each carrying the sentence "the scope gives
# it a width and nothing else".
# A vocabulary has nowhere for that to hide. Width is `.btn-block`, padding is
# `.btn-lg`, and a form is now the classes the element carries, so two controls
# that render the same ARE the same name. The map stays as a mechanism because
# the next component to be migrated will need it before it needs to be empty, and
# the control on it is unchanged: an entry whose source nothing wears, or whose
# target nothing stages, fails as loudly as a missing form.
SAME = {}



# ---- where each kind can be SEEN, without a second copy of its markup --------
# THE TABLE ANSWERED "WHERE IS IT" AND NOT "WHAT DOES IT LOOK LIKE", which is
# half of what a person opening a page called Buttons wants. The obvious fix is
# to stage one example of each kind here, and it is the wrong one: `.sheet-close`
# already stands in `dialog-shared`, `.icon-btn` in `header-in`, and a third copy
# of each is a third thing to keep in step.
#
# THREE ANSWERS WERE TRIED AND THE THIRD IS THE ONE THAT STANDS. First a
# screenshot per control, which is a photograph and goes stale silently. Then a
# live window: an iframe onto the specimen, cropped to a measured box. That was
# the same photograph with extra machinery, and it needed a crop instrument, a
# freshness contract and a gate of its own to hold numbers nobody could read.
# All of it is deleted.
#
# What is left is the answer that was available the whole time. `pick()` slices
# one element out of a document with its TRUE ancestor chain and drops its
# siblings, so the control on the page is the same single markup it already was,
# carrying the current stylesheet, both themes and every state, because it IS the
# specimen. The chain is kept for the cascade and marked `kit-nude`, which takes
# the host's surface and leaves its arrangement. Nothing is re-staged and nothing
# is photographed.

def _css():
    return re.sub(r"/\*.*?\*/", " ", CSS.read_text(encoding="utf-8"), flags=re.S)


def family():
    """The vocabulary, from the component header the build already checks.

    Read from the RAW file and not from `_css()`, which strips comments: the
    header IS a comment, so the first cut of this function looked for the one
    declaration list in the file inside the text with that list removed and
    found nothing. It failed to an EMPTY family, which matched every bare
    button and no named one, and the check went green on one row.

    IT USED TO ASK FOR NAMES ENDING IN `-btn` and that is the shape of the
    question the migration of 2026-08-05 answered. Five place-names
    (`.auth-btn`, `.state-btn`, `.provider-btn`, `.confirm-btn` and the bare
    button of an action bar) became one marker plus modifiers, so the test is
    now the prefix and not the suffix: `.btn` and every `.btn-*` it takes.
    """
    raw = CSS.read_text(encoding="utf-8")
    head = re.search(r"Classes:\s*(.+?)\.\s*$", raw[:1200], re.M)
    names = {c.strip().lstrip(".") for c in head.group(1).split(",")} if head else set()
    fam = {n for n in names if n == "btn" or n.startswith("btn-")}
    if "btn" not in fam:
        raise SystemExit("_worn: components/button.css declares no .btn in its header")
    return fam


def scopes():
    """Every class components/button.css reads that is not the subject."""
    body = _css()
    sel = " ".join(m.group(1) for m in re.finditer(r"([^{}]+)\{", body))
    return {c for c in re.findall(r"\.([\w-]+)", sel)} - family() - NOT_A_SCOPE


class Forms(HTMLParser):
    """Every button of the family, keyed by what the stylesheet decides."""

    def __init__(self, fam, scope):
        super().__init__(convert_charrefs=True)
        self.fam, self.scope = fam, scope
        self.stack, self.found, self.depth = [], [], 0
        self.label = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        if tag not in ("img", "br", "input", "meta", "link", "hr", "source", "use", "path"):
            self.stack.append((tag, cls))
        if tag != "button":
            return
        # THE MARKER DECIDES MEMBERSHIP AND THE MODIFIERS ARE THE NAME. Before the
        # migration this had to special-case a bare <button> inside `.cta-bar`,
        # because that control was this component's and carried no class of its
        # own; it carries one now, so the exception is gone with the names.
        if "btn" not in cls:
            return
        mine = cls & self.fam
        above = set()
        for _t, c in self.stack[:-1]:
            above |= c & self.scope
        name = ".".join(sorted(mine))
        self.found.append((name, " ".join(sorted(above)) or "bare", []))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.found and not self.found[-1][2] and data.strip():
            self.found[-1][2].append(data.strip()[:34])


def read(paths, fam, scope):
    """form -> {"uses": n, "files": {name}, "label": str}"""
    out = {}
    for f in paths:
        p = Forms(fam, scope)
        p.feed(f.read_text(encoding="utf-8"))
        for name, above, label in p.found:
            row = out.setdefault((name, above), {"uses": 0, "files": set(), "label": ""})
            row["uses"] += 1
            row["files"].add(f.name)
            if not row["label"] and label:
                row["label"] = label[0]
    return out


def compare():
    """(worn, staged, worn-and-not-staged, staged-and-not-worn, idle SAME rows).

    A worn combination is covered when it is staged itself OR when `SAME` says it
    renders as one that is. A staged control is justified when the product wears
    it OR when it is the target of a `SAME` row. Both directions, and the map
    itself is held in both too.
    """
    fam, scope = family(), scopes()
    worn = read(sorted(UV.glob("*.html")), fam, scope)
    stood = read([KIT / "specimens" / (s + ".html") for s in STANDS], fam, scope)
    targets = {t for t, _why in SAME.values()}
    missing = sorted(k for k in worn
                     if k not in stood and SAME.get(k, (None,))[0] not in stood)
    idle = sorted(k for k in stood if k not in worn and k not in targets)
    # a row of the map that no longer describes anything: the source is not worn,
    # or the target is not staged. Either way the sentence beside it is now a
    # claim about nothing, which is the state every declared list in this repo
    # is checked against.
    stale = sorted("%s @ %s -> %s @ %s" % (k[0], k[1], v[0][0], v[0][1])
                   for k, v in SAME.items() if k not in worn or v[0] not in stood)
    return worn, stood, missing, idle, stale


# ---- the second question: every OTHER control that is a button ---------------
# WHY THE PAGE CALLED BUTTONS SHOWED ONE CONTROL IN TWENTY THREE. This vitrine is
# grouped by which stylesheet owns the paint, because that is the address for a
# CHANGE: `.icon-btn` is drawn by components/header.css, and a person who found
# it on the button page would go and edit the wrong file. The grouping is right
# and its side effect is not: `components/button.css` owns four class names, so
# the page named Buttons answers for 710 of the product's 5,000-odd button
# placements and says nothing at all about the other twenty two kinds.
#
# A person opening Buttons wants every button. That is a navigation question and
# it gets a navigation answer: this census names every kind, counts it, and sends
# the reader to the frame that draws it. **Nothing is re-staged here.** A third
# copy of `.sheet-close` would be a third thing to keep in step, and the rule
# this repo has paid for twice is that a fact written twice drifts.
#
# WHY NOT SIMPLY MOVE THE CSS INTO button.css. For some of these it is a cost and
# for three of them it would be wrong. `yesno` is outcome semantics, and DESIGN.md
# decides that green and red mean YES and NO and nothing else, so an action
# component owning them would carry the outcome colour. The three closes are the
# chrome of their own overlay. The chip family is named in this component's own
# anti-rule as the thing a button is NOT. And the @import order in index.css is
# computed from what contains what, so moving classes between files reorders the
# cascade.
#
# ---- the role, which is the column the first cut of this census did not have --
# A `<button>` IS A TAG AND NOT A ROLE, and reading the tag as the answer is what
# put a tab strip, a category chip, a row of the account menu and five social
# marks on the page called Buttons. The reader who opened it asked for buttons and
# was handed 5,281 controls, of which 1,856 are buttons.
#
# Three roles, and the test for each is a question about the CONTROL rather than
# about its markup:
#
#   action    press it and something happens, and it has no state of its own to
#             carry. Confirm bet, close the sheet, load more, post a comment.
#   selector  it carries a VALUE and the selected one is a state, not a press.
#             Every chip, every tab, the toggle, the YES / NO pair, the outcome
#             side of a bet. Pressing it does not do a thing, it CHOOSES a thing,
#             and the reason the choice is visible is that the control stays lit.
#   nav       it goes somewhere. A row of the account menu, a slot of the bottom
#             nav, the logo, a social mark. It is a link wearing a button's tag
#             (or, for the logo and the menu rows, a button doing a link's job).
#   stand     not product at all: the furniture of this vitrine.
#
# The page called Buttons keeps the actions and lists the rest with the door to
# their own page. That is not a filing preference: a selector's whole subject is
# its selected state and its group, so a page that stages one of them alone shows
# the half that does not matter. Gate 38 holds the split in both directions.
#
# THE LOGO LEFT `icon only, in the header` FOR THIS REASON. It was in that row
# because it is a mark-sized button in the header band, which is a description of
# how it LOOKS. It navigates home, so it is nav, and the row it was in is now
# honestly all-action.
#
# Every row is (kind, own classes, ancestor classes, owning component, role, the
# reason it is drawn there). A button that matches no row fails the build, and a
# row that matches nothing fails just as loudly.
ROLES = ("action", "selector", "nav", "stand")
ROLE_WHY = {
    "action": "a press, and nothing is carried between presses. These are staged here.",
    "selector": "it carries a value, and the selected one is a state rather than a press. "
                "A selector is its group and its selected state, so it is staged on the page "
                "of the component that owns the group.",
    "nav": "it goes somewhere. It wears a button's tag and does a link's job.",
    "stand": "furniture of this vitrine, not product.",
}
KINDS = [
    # THE FIVE THAT ADOPTED `.btn` ON 2026-08-06 SIT ABOVE THE FAMILY ROW, and the
    # reason is the one gate 38 has now taught three times: the reader returns on the
    # FIRST row whose classes match, so a kind that adopts an atom and keeps its own
    # name has to be read before the generic row that would swallow it. Each of these
    # is `.btn` plus an emphasis and a size on the element now, and each still owns a
    # name because a region still says where it sits.
    ("how it works, in the header", {"hiw-btn"}, set(),
     "button", "action", "the header's quietest labelled press: a transparent pill, and the "
                         "third emphasis this family turned out to have"),
    # `.cmt-post` NOW STYLES NOTHING AND IS KEPT ANYWAY, which is a first for this
    # migration and is declared in `_adoption.UNSTYLED` rather than assumed. Once the
    # Post button wore `btn btn-primary btn-sm` it became the family in every value,
    # so the name is what tells the composer's commitment from 78 other small brass
    # presses, and this census is the only reader it has left. Deleting it was TRIED
    # and reverted the same hour: the specimen corpus stages `.cmt-post` and stages
    # `.cmt-signin` nowhere, so retiring the name would have left the signed-out
    # composer, a control on two real screens, with no stand at all. S47.
    ("post a comment", {"cmt-post", "cmt-signin"}, set(),
     "comments", "action", "the composer's own commitment, and the signed-out prompt "
                           "beside it, whose --bg-well ground is not an emphasis this "
                           "family has"),
    ("a comment's own action", set(), {"cmt-actions"},
     "button", "action", "reply and like sit in the comment row: no ground, no edge, no "
                         "corner, which is the fourth emphasis"),
    ("cookie consent", {"cc-btn"}, set(),
     "button", "action", "the banner is one block and its answers are quiet controls of "
                         "the family, at the family's middle step"),
    ("edit, on the profile", {"edit"}, set(),
     "button", "action", "one placement, and one placement is the wrong size for an "
                         "exception: it takes the family's small step"),

    ("the button family", {"btn"}, set(),
     "button", "action", "this page, staged in full above"),
    # `.hiw-btn` LEFT THIS ROW ON 2026-08-06, and it left for the reason the logo
    # left it before: the row was a description of WHERE a control sits, and this
    # one has a LABEL. `<button class="hiw-btn">How it works</button>`, 105
    # placements, reading "icon only" on every screen in the product. Found the
    # same way `.subcat` was, by reading the family out before migrating it.
    # ORDER MATTERS FROM HERE DOWN, AND IT STARTED MATTERING ON 2026-08-06. The
    # reader returns on the FIRST row whose classes match, which was harmless
    # while every kind owned a name nothing else used. It stopped being harmless
    # the moment a control adopted an ATOM: `.sheet-close` now reads
    # `class="icon-btn icon-btn-photo sheet-close"`, so the generic row below
    # would claim all 333 of them and `close, a sheet` would go idle, which is
    # exactly what gate 38 said. A row that names a FACE is more specific than
    # one that names the atom, so it comes first. Every kind that adopts an atom
    # from here on joins this block.
    # ONE ROW SINCE 2026-08-05, AND IT WAS TWO. `.hiw-close` was this same control
    # under a second name in a second file; the merge gave it this name, and the
    # census stopped reporting one control as two kinds on two pages.
    ("close, a sheet", {"sheet-close"}, set(),
     "dialog", "action", "chrome of the overlay it closes"),
    ("bookmark, on a card", {"bookmark-btn"}, set(),
     "card", "action", "it is part of the card's own furniture and sized to it"),
    # THE LAST TWO JOINED THIS BLOCK ON 2026-08-06, which is the day the last two
    # icon-only kinds adopted the atom and `iconbutton` reached one file. The row
    # below is the last one that has to be read for what it is rather than where
    # it sits, and it is here for the same reason as the four above it.
    ("close, a toast", {"toast-close"}, set(),
     "toast", "action", "chrome of the overlay it closes"),
    # matched on the PARENT and not on `.ed-act`, which is the class the buttons
    # carry as the detail script's hook. Matching the parent means this census
    # goes on naming them the day that class is deleted. It has to sit above the
    # generic row all the same: the buttons now carry `.icon-btn` themselves, and
    # a reader that returns on the first match would hand all 27 to the header.
    ("an event's action row", set(), {"ed-actions"},
     "event-detail", "action", "favourite, comments and share sit under the question and belong to it"),

    # `social` JOINED THIS LIST ON 2026-08-07 AND STOPPED BEING A MECHANISM OF ITS
    # OWN. It was in ANCHOR_KINDS, matched by a regex over its container, for one
    # reason: the census read `<button>` and these five are anchors. The census
    # reads a CONTROL now, so an anchor wearing `.icon-btn-lift` is found the same
    # way every other kind is, and the parallel path is gone rather than kept in
    # step by hand. It has to sit above the row below, which names `.icon-btn`
    # and would otherwise claim all 525 of them for the header.
    ("social", {"icon-btn-lift"}, {"social-row"},
     "iconbtn", "nav", "five marks in the footer brand block, and each one leaves the site"),
    ("icon only, in the header", {"icon-btn", "bal-add", "bal-swap"}, set(),
     "header", "action", "the header owns its own row of marks, and their size is the header's rhythm"),
    ("the logo, home", {"logo-btn"}, set(),
     "header", "nav", "it is the mark and the way back to the feed, and both belong to the header"),
    ("a row of the account dropdown", {"nav-row"}, {"dropdown"},
     "navitem", "nav", "a line of a menu and a notification's title over its detail: one "
                       "control with two contents, and the display is the only thing between them"),
    ("YES / NO, the outcome pair", set(), {"yesno"},
     "yesno", "selector", "green and red are outcome semantics in this product and nowhere else"),
    ("the outcome side of a bet", {"bp-side"}, set(),
     "betpanel", "selector", "it carries the odds and the selection, which is panel state rather than an action"),
    ("the sheet grab", {"sheet-grab"}, set(),
     "betpanel", "action", "a real control that is also the drawer's own handle"),
    # `.subcat` LEFT THIS ROW ON 2026-08-06, and the measurement that was
    # supposed to start the chip migration is what took it out. A sub-category
    # control is `<nav aria-label="Sub-categories">` holding buttons that
    # components/catnav.css draws `width:100%` with `justify-content:
    # space-between`: a full-width row with a label on the left and a count on
    # the right, which is a list row and not a chip. Reading it as a chip was
    # reading the FAMILY NAME, which is the same mistake as reading the tag.
    # THE FOUR ROWS BELOW GAINED A CLASS SET ON 2026-08-07, AND THE REASON IS AN
    # INSTRUMENT DEFECT THIS PASS WALKED INTO. `atom_gap()` asks which FILE draws
    # a kind by testing whether a rule ENDS at the control, and it recognises the
    # control by the classes the row names. A row that names only ANCESTORS is
    # recognised only while the control is reached by its tag - `.cat-nav button`
    # - which is exactly the spelling a migration deletes. So the moment these
    # kinds adopted `.chip`, the file that draws them became invisible to the
    # metric and the distance would have fallen by two for a move that closed
    # one. Naming the face fixes it in the direction of MORE truth: the row says
    # both what the control is and where it stands.
    # IT ADOPTED THE CHIP ON 2026-08-07 AND ITS ROLE DID NOT MOVE. Load more
    # fetches, so it is an `action`; its face is `--bg-chip` on `--bevel-notice`
    # at a 10 corner in 14px semibold, which is `.chip-nav` in every value, and
    # its hover and press were that chip's byte for byte in a second file. A role
    # is what a control MEANS and an atom is where its RULES live, which is the
    # correction the social mark forced a day earlier.
    ("load more", {"load-more"}, set(),
     "loadmore", "action", "the category chip at the foot of a list: same ground, same "
                           "edge, same corner, same hover and same press, in a second file"),
    ("chip, a category", {"chip-nav", "chip-quiet"}, {"cat-nav", "cat-condensed", "feed-subfilter"},
     "chip", "selector", "one graphite chip family, with a lighter press than this one"),
    ("a sub-category row", {"chip-lane"}, {"subcat"},
     "chip", "nav", "a chip whose surface changes with the window: a pill in a scroller at "
                    "380, a full-width row with a count in a sticky rail above 900"),
    ("chip, a quick amount", {"chip-amount"}, {"quick"},
     "chip", "selector", "it sets the value of the field beside it, so it belongs to the field"),
    # TWO ROWS BECAME ONE ON 2026-08-05, and this census is the instrument that
    # said they should. It had already filed the sort segment and the chart range
    # as one ROLE with one face and two names, 27 placements and 36; the css
    # said the rest, because `.cmt-controls .seg button` in comments.css and
    # `.ed-range button` in tabs.css were the same declaration block byte for
    # byte. Matched on the CLASS the buttons now carry rather than on either
    # parent, because the control is the class and the two troughs belong to the
    # components that hold them.
    ("chip, quiet, in a rail", {"chip-rail"}, set(),
     "chip", "selector", "one control the product picks a value with, in the two rails "
                         "that hold it: the comment sorter and the chart range"),
    ("tab", {"rules-tab"}, {"tabs"},
     "tabs", "selector", "a tab is a selector, and the selected one is a state and not a press"),
    ("bottom nav slot", {"nav-slot"}, {"bottom-nav"},
     "navitem", "nav", "the quietest control in the product: no ground, no edge, no corner, "
                       "and the one thing the bar says at a glance is which slot is current"),
    ("toggle", {"toggle"}, set(),
     "filters", "selector", "a switch is not a button: it carries a value, not an action"),
    ("the vitrine's own chrome", {"rm-toggle", "theme-switch"}, set(),
     "course-chrome", "stand", "stand furniture, not product: it is how you read these pages"),
]
# Not a <button>, and declared rather than quietly skipped: the social row is
# five anchors carrying a mark and no text, which is a button in every way a
# reader can tell and an anchor because each one navigates away.
# WHAT MAKES AN <a> A CONTROL, and it is read out of the list above rather than
# typed: every class any kind NAMES. An anchor wearing one of these is a control
# that happens to navigate - a nav slot, a category chip, a social mark - and an
# anchor wearing none of them is a link. The census asks this and nothing else,
# so a kind that gains a face gains its anchors in the same edit.
CONTROL_CLASSES = {c for _k, own, _a, _o, _r, _w in KINDS for c in own}

# ANCHOR_KINDS WAS HERE AND IT IS GONE, 2026-08-07. It held one row - the
# footer's five social marks - and it existed because `Census` read the tag
# `<button>` while those five are anchors carrying a mark and no text. Reading
# the CONTROL instead of the tag dissolves the special case: `social` is an
# ordinary row of KINDS above, found by the class it wears, and this file no
# longer has two ways of counting the same thing. The regex it used could only
# see a container that closed with `</div>`, which would have found none of the
# 1,134 controls that stopped being buttons in the same commit.


class Census(HTMLParser):
    """Every CONTROL in a document, with the kind it belongs to.

    IT READ A TAG UNTIL 2026-08-07 AND IT READS A CONTROL NOW, which is the
    change `ui-kit/docs/defects.md` row 78 forced and, in hindsight, the change
    ANCHOR_KINDS had been asking for since it was written. The docstring used to
    say "every <button>", and the footer's five social marks needed a whole
    parallel mechanism - a regex over a container - because they are anchors that
    are buttons in every way a reader can tell. When the bottom-nav slot and the
    two category strips stopped being a <button> inside an <a> and became the
    <a>, 1,134 named controls would have vanished from this census in one commit
    and gate 38 would have reported them as gone rather than as changed.

    An <a> is a control here when it CARRIES ONE, which is the same test the rest
    of this file uses: it wears a class that a kind names. An anchor with no such
    class is a link, and a link is not a button-shaped control.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.found = [], []

    def handle_starttag(self, tag, attrs):
        cls = set((dict(attrs).get("class") or "").split())
        if tag not in ("img", "br", "input", "meta", "link", "hr", "source", "use", "path"):
            self.stack.append((tag, cls))
        if tag == "a":
            if not (cls & CONTROL_CLASSES):
                return
        elif tag != "button":
            return
        above = set()
        for _t, c in self.stack[:-1]:
            above |= c
        for kind, own, anc, owner, role, why in KINDS:
            if (own & cls) or (anc & above):
                self.found.append((kind, ""))
                return
        self.found.append((None, " ".join(sorted(cls)) or "(no class)"))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return


def census():
    """(kind -> {"uses", "files"}, [unnamed controls], [idle kinds])."""
    seen = {}
    unnamed = {}
    for f in sorted(UV.glob("*.html")):
        p = Census()
        p.feed(f.read_text(encoding="utf-8"))
        for kind, raw in p.found:
            if kind is None:
                unnamed.setdefault(raw, set()).add(f.name)
                continue
            row = seen.setdefault(kind, {"uses": 0, "files": set()})
            row["uses"] += 1
            row["files"].add(f.name)
    idle = [k[0] for k in KINDS if k[0] not in seen]
    return seen, sorted("%s on %d screen(s)" % (k, len(v)) for k, v in unnamed.items()), sorted(idle)


# ---- the atom each kind belongs to, and the distance to it ------------------
# THE TARGET, IN CODE. `ui-kit/docs/atoms.md` decides what the atoms ARE, from
# this census rather than from the files, and this is the same decision written
# where the build can read it. Without it every pass fixes a real defect and
# none of them moves the system toward a stated shape, which is what four passes
# in a row did before 2026-08-05.
#
# The kind list is the product as it is. This is the product as it should be
# partitioned, and gate 41 measures the gap between the two, in both directions:
# a kind naming no atom fails, and an atom no kind names fails just as loudly.
ATOMS = {
    "button": "a press with a LABEL, that does a thing. Emphasis, size and block are its "
              "modifiers, and it said 'nothing else in it is' until 2026-08-06, when the "
              "family was read out in the browser. There are THREE emphases and not two: "
              "brass, quiet on --bg-control, and a transparent pill the header band wears "
              "on 105 placements. 710 of the 911 are already `.btn`; every one of the 201 "
              "that is not differs from it by a VALUE rather than by a modifier - a 13px "
              "font off a 12/14 ramp, a border nobody gave it, an 11px pill - which makes "
              "this the first atom on the map where nothing adopts at zero",
    "iconbutton": "a press whose whole content is a MARK. Not a modifier of `button`: it "
                  "has no label to size, and its own box is the whole target",
    "chip": "a label a person PICKS BETWEEN, carrying a value. The chosen one is a brass "
            "tint, which DESIGN.md decides twice",
    "outcome": "the YES / NO pair, where the COLOUR states a result. It had three kinds until "
               "2026-08-06 and has two: the hero band was drawing its own copy of the card's "
               "pair, same three roles, same markup shape, because every selector in yesno.css "
               "hangs off `.yesno` and the hero did not carry it. It carries it now. It never "
               "folds into "
               "`chip`, because green and red are outcome semantics and an accent may not "
               "borrow the win or lose colour",
    "tab": "a selector whose selection swaps a PANEL rather than carrying a value, which "
           "is the distinction its accessible role already makes. Added 2026-08-06: the "
           "map put its 36 placements in `chip` on the strength of the drawing, and the "
           "measurement that was to start the chip migration refused it. `.rules-tab` is "
           "transparent with no corner and a 2px underline; `.tabs button` is a pill on "
           "`--bg-chip`. An underline against a pill is a FACE and not a modifier, so "
           "they were never one chip, and `.ed-tablabel` and `.ptab-lbl` are the same "
           "control again as labels",
    "switch": "one setting, on or off, answered on the spot. It says yes or no to one "
              "thing rather than choosing among several, which is what keeps it out of "
              "`chip`",
    "navitem": "a thing a person taps that GOES somewhere and draws NOTHING until it is "
               "pointed at: transparent, no edge, no corner, a label the row is as wide "
               "as. A slot with a mark over a label and a row with a label are one "
               "control at two sizes. It said three until 2026-08-06, and the third was "
               "the social mark, which measured as an icon button in every value a face "
               "has and was moved. An atom is what a set of RULES is shared by, so it is "
               "settled by the face; the role is what catches two faces that agree and "
               "MEAN different things, which is `tab` against `chip`",
}
NOT_AN_ATOM = {
    "the logo, home": "one brand mark. There is exactly one, it never varies, and giving "
                      "it a modifier vocabulary would be inventing a system for a single "
                      "element",
    "the sheet grab": "a handle and not a press: it answers a drag, and the four of them "
                      "are the drawer's own furniture",
    "the vitrine's own chrome": "not the product. course-chrome.css draws the panel this "
                                "repo wraps around every page",
}
ATOM = {
    "the button family": "button",
    "post a comment": "button",
    "cookie consent": "button",
    "edit, on the profile": "button",
    "icon only, in the header": "iconbutton",
    "how it works, in the header": "button",
    "close, a sheet": "iconbutton",
    "bookmark, on a card": "iconbutton",
    # NOT AN ICON BUTTON, and the reading found it the same way it found
    # `.hiw-btn` and `.subcat`. The two controls in a comment's meta row are
    # `<button><svg/>24</button>` and `<button>Reply</button>`: one is a mark
    # beside a COUNT and the other is a word. Neither is icon-only, and the row
    # they sit in is text. A press with a label is `button`.
    "a comment's own action": "button",
    "an event's action row": "iconbutton",
    "close, a toast": "iconbutton",
    "chip, a category": "chip",
    "chip, a quick amount": "chip",
    "chip, quiet, in a rail": "chip",
    "load more": "chip",
    # THE ROW THE MAP WAS NOT SURE OF, AND THE MEASUREMENT SETTLED IT ON
    # 2026-08-06. It was `chip` for one day, on the strength of the drawing.
    # Then the chip family was read out file by file to start the migration and
    # the drawing turned out not to agree with itself: `.rules-tab` is
    # transparent, has no corner and carries a 2px underline, while `.tabs
    # button` is a pill on --bg-chip at 13px. An underline against a pill is a
    # face and not a modifier, so the counter-argument atoms.md had written down
    # is the one that holds. The atom is what the control DOES.
    "tab": "tab",
    # AND IT WAS WRONG AGAIN, IN THE SAME DIRECTION, AND THE SAME KIND OF
    # MEASUREMENT SETTLED IT ON 2026-08-07. `navitem` was read off the DESKTOP
    # rule alone: a full-width row with a label left and a count right, which is
    # a list row. At 380 the same control is a 114x41 hairline PILL in a
    # horizontal scroller, `--border-hairline` on a 100px corner. A nav item is
    # transparent with NO edge and NO corner, and this thing carries a 1px band
    # and a corner at both widths, so it was never that atom. It is a chip whose
    # SURFACE changes with the window, which is the first one in the product, and
    # the face carries the query. `ui-kit/docs/atoms.md`, and backlog S46.
    "a sub-category row": "chip",
    "YES / NO, the outcome pair": "outcome",
    "the outcome side of a bet": "outcome",
    "toggle": "switch",
    # AND IT WAS ANSWERED ON 2026-08-06, BY MEASURING IT. The row above used to
    # read "rule 1 is the role, and rule 1 has not been wrong here yet". It was
    # wrong here. `navitem` claimed a slot with a mark over a label, a row with a
    # label and a bare mark were "one control at three sizes"; read in the
    # browser at 1440 and 380 they are not one control at all.
    #     bottom nav slot   transparent   0px border   0px radius   column, 10px
    #     dropdown row      transparent   0px border   0px radius   inline-block
    #     social            --bg-control  1px hairline 10px radius  centred flex
    # The first two agree with each other on every one of those and share nothing
    # with the third. The third agrees with `.icon-btn-tile` at 28 on ALL of it:
    # same ground rgb(36,40,47), same edge rgb(43,47,56), same 10px corner, same
    # centred flex, same 18px mark. A ground, an edge and a corner against
    # transparent, none and none is a FACE, which is rule 2, and rule 2 says these
    # were never one atom. The role stays `nav` - it is what this control MEANS -
    # and the atom is where its RULES live. `ui-kit/docs/atoms.md`.
    "social": "iconbutton",
    "bottom nav slot": "navitem",
    "a row of the account dropdown": "navitem",
}


def atom_gap():
    """(kinds with no atom, atoms no kind names, the table, the distance).

    THE DISTANCE IS FILE-SLOTS MINUS ATOMS, and it goes to zero. Each atom
    should be drawn in exactly one file; today `chip` is drawn in four files and
    `iconbutton` in six.

    A FILE COUNTS WHEN IT DRAWS THE CONTROL, NOT WHEN IT PLACES THE CONTAINER,
    and the first cut of this got that wrong. Asking `_adoption.styled()` which
    files mention the class put `base.css` and `patterns/browse-shell.css` on
    the chip's list, because both style `.cat-nav` - the PLATE the rail stands
    on, its padding and its ground. That is a region doing exactly what a region
    is allowed to do. So the test is on the selector's last simple-selector: the
    file draws the control when a rule ENDS at the control itself, and merely
    holds it when the rule ends at something above it. The distance went 19 to
    the honest number the moment that was fixed, which is the whole reason the
    metric is computed rather than counted by eye.
    """
    rows = kind_rows()
    named = {r["kind"] for r in rows}
    homeless = sorted(k for k in named if k not in ATOM and k not in NOT_AN_ATOM)
    idle_atom = sorted(a for a in ATOMS if a not in set(ATOM.values()))
    stale = sorted(k for k in list(ATOM) + list(NOT_AN_ATOM) if k not in named)
    # A RULE THAT ONLY PLACES A CONTROL IS NOT A RULE THAT DRAWS ONE, and this is
    # the second correction the metric needed. `components/header.css` keeps
    # `.app-header .left > .icon-btn{display:none}` on purpose - hiding a control
    # in a band is the band's decision, and the map says so in as many words -
    # but the selector ENDS at the control, so the first version of this test
    # counted header as still drawing the icon button and the distance went UP
    # after a move that took every face rule out of it. Placement is where and
    # whether; a face is what it looks like, and a rule has to set at least one
    # face property to count.
    # WIDTH JOINED THEM ON 2026-08-07, AND IT IS THE THIRD CORRECTION THIS TEST
    # HAS NEEDED. `components/cookie-consent.css` keeps `.cc-btn{flex:1 1 auto;
    # min-width:96px}` so that three answers divide the banner and none collapses
    # under its own label, and it is one sentence: `flex` was already read as
    # placement and `min-width` was read as a face. A WIDTH IS WHAT A CONTAINER
    # DECIDES, the same as a flex basis or an order; a HEIGHT is not, because
    # under a coarse pointer a height is a target size and belongs to the
    # control. That asymmetry is the point rather than an inconsistency, and it
    # is why `min-height` is deliberately absent from this list.
    PLACEMENT = ("display", "position", "top", "right", "bottom", "left", "z-index",
                 "margin", "flex", "order", "align-self", "justify-self", "grid",
                 "visibility", "float", "overflow", "inset", "place-self",
                 "width", "min-width", "max-width")
    rules = []
    for path in sorted(COMP.glob("*.css")) + sorted((COMP / "patterns").glob("*.css")):
        if path.name in ("index.css", "tokens.css", "fonts.css"):
            continue
        body = re.sub(r"/\*.*?\*/", " ", path.read_text(encoding="utf-8"), flags=re.S)
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", body):
            props = [d.split(":")[0].strip() for d in m.group(2).split(";") if ":" in d]
            if not props or all(p.startswith(PLACEMENT) for p in props):
                continue
            for sel in m.group(1).split(","):
                sel = " ".join(sel.split())
                if sel and not sel.startswith("@"):
                    rules.append((path.stem, sel))

    def draws(sel, own, anc):
        """Does this selector END at the control, rather than above it?"""
        last = re.split(r"[ >+~]", sel)[-1]
        last = re.sub(r"(:{1,2}[\w-]+(\([^)]*\))?|\[[^\]]*\])+$", "", last)
        if any(re.search(r"\.%s(?![\w-])" % re.escape(c), last) for c in own):
            return True
        return last in ("button", "a") and any(
            re.search(r"\.%s(?![\w-])" % re.escape(c), sel) for c in anc)

    table = {}
    for kind, own, anc, _owner, _role, _why in KINDS:
        a = ATOM.get(kind)
        if not a:
            continue
        e = table.setdefault(a, {"uses": 0, "kinds": [], "files": set()})
        e["kinds"].append(kind)
        for stem, sel in rules:
            if draws(sel, own, anc):
                e["files"].add(stem)
    for r in rows:
        a = ATOM.get(r["kind"])
        if a:
            table[a]["uses"] += r["uses"]
    slots = sum(len(e["files"]) for e in table.values())
    return homeless, idle_atom, stale, table, slots - len(table)


def kind_rows():
    """The census as the page generator wants it: one row per kind, ordered by
       how much of the product it is."""
    seen, _unnamed, _idle = census()
    rows = []
    for kind, own, anc, owner, role, why in KINDS:
        r = seen.get(kind, {"uses": 0, "files": set()})
        # A SELECTOR AND NOT A BARE NAME, because the two halves of a row mean
        # different things and the old notation spelled them the same. `own` is a
        # class the control CARRIES; `anc` is a class ABOVE it, and the rule that
        # paints the control is `.cmt-actions button`. Printing both as
        # `sheet-close` and `.cmt-actions` said "here are some class names" when
        # the honest answer is "here is what the stylesheet matches", and a reader
        # who copied the second one onto a button would have painted nothing.
        # A row that has both prints both: `tab` is `.rules-tab` on the profile
        # and `.tabs button` in My Bets, and it is one kind either way.
        rows.append({"kind": kind,
                     "classes": sorted("." + c for c in own)
                                + sorted("." + a + " button" for a in anc),
                     "owner": owner, "role": role, "why": why,
                     "uses": r["uses"], "screens": len(r["files"])})
    return sorted(rows, key=lambda r: -r["uses"])


# ---- which action stands where, and the answer is read out of the map ---------
# THE ROLE SPLIT ONLY MEANS SOMETHING IF THE ACTIONS ACTUALLY STAND. A page that
# says "these fourteen are the buttons" and stages nine of them has moved the
# defect rather than fixed it, so the staging is checked the way everything else
# here is: from both ends.
#
# Two of the fourteen are not in the census specimen and must not be, because
# they are already the subject of the page: `the button family` and `action bar`
# are the matrix at the top. Naming them here is what keeps the gate from
# demanding a second copy of the thing the page is about.
IN_MATRIX = {"the button family"}
CENSUS_SPECIMENS = ("button-census",)


def staged_kinds():
    """The kinds the census specimen stages, read from specimens.map.json."""
    import json
    spec = json.loads((KIT / "specimens.map.json").read_text(encoding="utf-8"))
    out = {}
    for entry in spec["specimens"]:
        if entry["id"] not in CENSUS_SPECIMENS:
            continue
        for part in entry.get("compose", []):
            if "kind" not in part:
                raise SystemExit("_worn: %s has a part with no `kind`: %s"
                                 % (entry["id"], part.get("pick")))
            out.setdefault(part["kind"], []).append(entry["id"])
    return out


def roles():
    """(rows by role, actions not staged, staged things that are not actions)."""
    rows = kind_rows()
    by_role = {r: [x for x in rows if x["role"] == r] for r in ROLES}
    staged = staged_kinds()
    named = {r["kind"] for r in rows}
    unstaged = sorted(r["kind"] for r in by_role["action"]
                      if r["kind"] not in staged and r["kind"] not in IN_MATRIX)
    wrong = sorted(k for k in staged
                   if k not in named
                   or next(r for r in rows if r["kind"] == k)["role"] != "action")
    return by_role, unstaged, wrong


if __name__ == "__main__":
    worn, stood, missing, idle, stale = compare()
    print("%d form(s) worn by %d placement(s) in ui-visual, %d staged in %s, "
          "%d covered by a scope that changes nothing"
          % (len(worn), sum(r["uses"] for r in worn.values()), len(stood),
             ", ".join(STANDS), len(SAME)))
    if "--check" not in sys.argv:
        for (name, above), row in sorted(worn.items(), key=lambda kv: -kv[1]["uses"]):
            how = ("staged" if (name, above) in stood
                   else "as %s" % SAME[(name, above)][0][0] if (name, above) in SAME
                   else "NOT STAGED")
            print("   %-22s %-34s %4d uses  %3d screens  %-10s %s"
                  % (name, above, row["uses"], len(row["files"]), how, row["label"]))
    for k in missing:
        print("   WORN AND NOT STAGED: %s @ %s (%d uses, e.g. %s)"
              % (k[0], k[1], worn[k]["uses"], worn[k]["label"]))
    for k in idle:
        print("   STAGED AND NOT WORN: %s @ %s" % (k[0], k[1]))
    for s in stale:
        print("   IDLE ROW IN THE SAME MAP: %s" % s)

    seen, unnamed, idle_kinds = census()
    rows = kind_rows()
    print("\n%d kind(s) of button-shaped control, %d placement(s), %d component(s) draw them"
          % (len(rows), sum(r["uses"] for r in rows), len({r["owner"] for r in rows})))
    by_role, unstaged, wrong = roles()
    print("   by role: " + ", ".join(
        "%s %d kind(s) / %d placement(s)"
        % (r, len(by_role[r]), sum(x["uses"] for x in by_role[r])) for r in ROLES))
    if "--check" not in sys.argv:
        for role in ROLES:
            print("  -- %s" % role)
            for r in by_role[role]:
                print("   %-34s %-16s %5d uses %4d screens  %s"
                      % (r["kind"], r["owner"], r["uses"], r["screens"],
                         ", ".join(r["classes"])[:40]))
    for u in unnamed:
        print("   NOT NAMED BY THE CENSUS: %s" % u)
    for k in idle_kinds:
        print("   NAMED AND NOT WORN: %s" % k)
    for k in unstaged:
        print("   AN ACTION THAT STANDS NOWHERE: %s" % k)
    for k in wrong:
        print("   STAGED ON THE BUTTON PAGE AND NOT AN ACTION: %s" % k)
    sys.exit(1 if (missing or idle or stale or unnamed or idle_kinds or unstaged or wrong) else 0)
