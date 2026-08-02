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

WHAT ARITHMETIC CANNOT SEE, AND THE ONLY HAND-WRITTEN PART. Two things:

  - a component whose parts are all its OWN classes contains nothing a class map
    can name, so containment reads zero. The featured hero band is four blocks
    (a market with a chart, trust cards, a brand tile, a ranked list) and 51
    classes, all of them hero's, so the arithmetic calls it an atom;
  - a screen SHELL is an organism because of what it is, not because of what it
    happens to hold. The bottom nav holds no component and is still the tab bar
    of every screen.

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


def subjects_of(body):
    """class -> the fewest other classes in any selector where it is the subject."""
    found = {}
    text = re.sub(r"/\*.*?\*/", "", re.sub(r"url\([^)]*\)", "", body), flags=re.S)
    for m in re.finditer(r"([^{}]+)\{", text):
        sel = m.group(1)
        if sel.lstrip().startswith("@"):
            continue
        for one in sel.split(","):
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
            mine = OWNED.get(comp, set())
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
                    for cls in kid.cls:
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
    "footer": (3, "a screen shell"),
    "state-block": (3, "the empty and error block, an organism by definition"),
    "hiw-dialog": (3, "it IS a dialog: .app-dialog and .hiw-dialog sit on one element, "
                      "so the frame is not a descendant and containment reads zero"),
    # parts that are all the component's own classes
    "hero": (3, "four blocks in one band (featured market with its chart, trust cards, "
                "brand tile, ranked list), 51 classes, every one of them hero's"),
    "market": (2, "a collapsible with a head, a body and a price table, all its own classes"),
    "related": (2, "a list of rows"),
    "seo-plate": (2, "two columns of sections"),
    "trustbar": (2, "a strip of trust items"),
    "account": (2, "a bar of two actions whose buttons carry no class of their own"),
    "toast": (2, "a message and a close, stacked"),
    "yesno": (2, "a pair of controls in a container"),
}

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
ORDER_BREAK = {
    ("comments", "tabs"): "the .seg sort switcher, which lives in tabs.css because that file "
                          "owns every switcher; the real nesting is the other way, the tab "
                          "strip wraps the thread",
}
FIRST = ["fonts", "tokens", "base", "course-chrome"]


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
ORDER = FIRST + sorted(_BODY, key=lambda f: (LEVEL.get(f, 0), _DEPTH[f], _CURRENT[f]))


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
