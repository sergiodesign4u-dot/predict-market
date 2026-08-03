#!/usr/bin/env python3
"""
_fill_inventory.py  -  give ui-kit/docs/inventory.md the three columns it was
missing: which css file owns the component, which stand page shows it, and what
level it sits at.

WHY IT MATTERS. The inventory was read out of the product before the system
existed, so it was a list of things a screen contains. Once the system exists,
the same table has to answer the question a person actually arrives with: I am
looking at this thing, where do I edit it, and where do I see it on its own.
Without those columns the table is a census; with them it is an index.

WHY LEVEL IS HERE AND NOT TYPED IN. Atom, molecule, organism is the input to two
decisions the table cannot make on its own: the @import order in
components/index.css (a whole must not be imported before its parts, and today
header comes before button and card before both) and the grouping in
ui-kit/_nav.js (named by purpose, so a button and a sign-in dialog sit together).
The level is arithmetic over containment, not an opinion, so it is computed in
_levels.py and read here. Typing it into the markdown would make this table a
second source for a fact the markup already answers, and it would be wrong the
first time a component gained a part. That pair, one system described twice, is
the defect step 7c closed between coverage.md and the css headers.

HOW THE MAPPING IS MADE. A row that quotes a class (`.card`, `.opt-row`) is
matched against the `Classes:` header every component file carries, so most of
the table maps itself and stays correct when a class moves file. The rows that
name their component in prose instead are in TITLE below, one line each, and
that list is the only hand-written part.

A row with no component is not a gap: some rows are layout facts (a responsive
grid) or one-off screen furniture. Those get a dash, and the dash is a claim in
its own right, so it is written here rather than left blank.

Idempotent: rebuilds all three columns from scratch on every run. The strip is
written by SHAPE, not by counting cells, because the table shipped for one stage
with two generated columns and a run that assumes three would eat the first real
cell of every row. The header is stripped the same way the data rows are: a
generator that is not idempotent on ALL of its row kinds is not idempotent, and
this one grew a header by two cells a run for seven runs.

    python3 ui-kit/_fill_inventory.py [--check]
No em dash.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _levels import label as level_label  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = os.path.join(ROOT, "ui-kit", "docs", "inventory.md")
COMP = os.path.join(ROOT, "components")
KIT = os.path.join(ROOT, "ui-kit")

# ROWS THAT NAME THEIR COMPONENT IN PROSE RATHER THAN BY CLASS, and this is the
# hand-written half of the map. Both false file cells in `ui-kit/docs/backlog.md`
# S21 came from here, which is what a hand-written half is for. It now carries
# the control every declared list in this repo carries: an entry that matches no
# row fails the build. On the run that added the control, EIGHT of forty one
# matched nothing - `Win overlay`, `Loss overlay`, `Shared dialog shell`,
# `Profile tabs`, `Active / History tabs`, `Resolution block`, `Section divider`
# and `hero trust cards` - because every one of those rows had since gained a
# quoted class and was already resolving without the hand map. Eight dead rows
# in the one place two defects came from, and nothing had said so. They are
# deleted, and the rebuilt table is byte-identical without them.
TITLE = {
    "App header (lean)": "header",
    "Logo (Events home)": "header",
    "Balance / Portfolio-Cash swap": "header",
    "Notifications bell + mini-dropdown": "header",
    "Avatar menu (dropdown)": "header",
    "How-it-works button": "header",
    "Icon button (ghost)": "header",
    "Auth entries (Log in / Sign up)": "button",
    "Category nav band": "catnav",
    "Bottom nav (mobile, 4 slots)": "bottomnav",
    "Footer language menu": "footer",
    "Screen-tree drawer / roadmap sidebar": "course-chrome",
    "Event card, binary (treatment B)": "card",
    "Event card, multi (treatment D)": "card",
    "Odds bar (thin, green YES on red track)": "oddsbar",
    "Tinted YES / NO buttons": "yesno",
    "Probability figure": "card",
    "Card meta row (Volume / Closes + bookmark)": "card",
    "Responsive card grid": "feed",
    "Load-more control": "loadmore",
    "Content tab strip": "tabs",
    "Provider buttons (Google / X / Apple, real brand marks)": "button",
    "Amount field + quick-amount chips": "input",
    "Field label": "input",
    "Primary CTA (brass)": "button",
    "Bottom-sheet / modal overlay (grab, backdrop)": "dialog",
    "Filter menu (Sort / Frequency)": "filters",
    "Reverse-order toggle switch": "filters",
    "Share Card (auto-generated win visual, reused in profile gallery)": "dialog",
    "Reputation stat-grid": "profile",
    "Transaction list (deposits/payouts/fees/stakes)": "position",
    "Product footer (brand, markets, product, support, company, legal)": "footer",
    "Footer trust strip": "trustbar",
}

# a component file whose stand page is named differently
PAGE = {
    "dialog": ["dialog", "outcome-dialog", "signin"],
    "profile": ["profile"],
    "tabs": ["tabs"],
}

# What a generated cell looks like. The strip asks these instead of counting,
# so the same run works on a table that carries two of the three columns.
CSS_CELL = re.compile(r"^-$|^`[\w.-]+\.css`(, `[\w.-]+\.css`)*$")
PAGE_CELL = re.compile(r"^-$|^\[[\w.-]+\]\(\.\./[\w.-]+\.html\)"
                       r"(, \[[\w.-]+\]\(\.\./[\w.-]+\.html\))*$")
LEVEL_CELL = re.compile(r"^L[123]$|^-$")


def class_owner():
    owner = {}
    for fname in sorted(os.listdir(COMP)):
        if not fname.endswith(".css"):
            continue
        with open(os.path.join(COMP, fname), encoding="utf-8") as fh:
            head = fh.read(2000)
        m = re.search(r"Classes:\s*([^\n]*)", head)
        if not m:
            continue
        for c in re.findall(r"\.([\w-]+)", m.group(1)):
            owner.setdefault(c, fname[:-4])
    return owner


def stems_for(title, owner, used=None):
    """Which component file(s) a row belongs to, from the classes it quotes and
    only then from the hand map.

    A TAG-QUALIFIED SELECTOR IS STILL A CLASS. This used to read
    `c.lstrip(".").split(".")[0]`, which takes the FIRST dot-separated part, so
    `p.pos-status` resolved to `p`, nothing owns `p`, and the row fell silently
    through to the hand map and was filed under the wrong file for a whole stage
    (`ui-kit/docs/backlog.md` S21, L155). Four rows in the table are written
    that way and three were right by coincidence, because `dialog.app-dialog`
    and `dialog.outcome-dialog` happen to have a tag that is also a component
    name. Every part is tried now, LEFT TO RIGHT, and the first one an owner
    claims wins. Left to right and not longest first, which was the second cut
    and broke a row while fixing one: `.card.skeleton` is a card in a state, and
    the longest part is the STATE, so the row lost `card.css` and kept only the
    file that happens to declare the modifier. The tag is always leftmost and is
    almost never a component, so trying it first costs nothing and keeps a
    compound selector reading as "the thing, then what is done to it"."""
    classes = re.findall(r"`\.?([\w.-]+)", title)
    stems = []
    for c in classes:
        for part in c.lstrip(".").split("."):
            if part in owner:
                if owner[part] not in stems:
                    stems.append(owner[part])
                break
    if stems:
        return stems
    for key, stem in TITLE.items():
        if key.lower() in title.lower():
            if used is not None:
                used.add(key)
            return [stem]
    return []


def main(check=None):
    check = ("--check" in sys.argv) if check is None else check
    with open(INV, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    owner = class_owner()
    pages = {f[:-5] for f in os.listdir(KIT) if f.endswith(".html")}
    out, filled, dashed, header_width = [], 0, 0, 0
    used = set()
    for line in lines:
        if not (line.startswith("|") and line.count("|") >= 7):
            out.append(line)
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] == "Component":
            # Strip every group a previous run added, then add one back. Without this
            # the header grew by two cells per run while the data rows below it did
            # not (they have their own strip), so after seven runs every table in the
            # document had a 21-cell header over 9-cell rows and none of them
            # rendered. A generator that is not idempotent on ALL of its row kinds is
            # not idempotent.
            while len(cells) >= 3 and cells[1] == "CSS file" and cells[2] == "Page":
                cells = cells[:1] + cells[3:]
            if len(cells) >= 2 and cells[1] == "Level":
                cells = cells[:1] + cells[2:]
            cells = cells[:1] + ["CSS file", "Page", "Level"] + cells[1:]
            header_width = len(cells)
            out.append("| " + " | ".join(cells) + " |")
            continue
        if set(cells[0]) <= set("-: "):
            # rebuilt from the header just written, never grown from its own last state
            out.append("| " + " | ".join(["---"] * header_width) + " |")
            continue
        # Drop every group a previous run added, then add one back. It loops because
        # a run that failed to recognise its own output once left two groups behind.
        # Each cell is recognised by its SHAPE: asking "does cell 1 end in .css" and
        # then removing a fixed number of cells is how a dashed row (three dashes in
        # a row) would have eaten the first real cell of the table.
        while len(cells) >= 3 and CSS_CELL.match(cells[1]) and PAGE_CELL.match(cells[2]):
            cells = cells[:1] + cells[3:]
        if len(cells) >= 2 and LEVEL_CELL.match(cells[1]):
            cells = cells[:1] + cells[2:]
        stems = stems_for(cells[0], owner, used)
        if stems:
            css = ", ".join("`%s.css`" % s for s in stems)
            pg = []
            for s in stems:
                for cand in PAGE.get(s, [s]):
                    if cand in pages and cand not in pg:
                        pg.append(cand)
            page = ", ".join("[%s](../%s.html)" % (p, p) for p in pg) or "-"
            lvl = level_label(stems)
            filled += 1
        else:
            css, page, lvl = "-", "-", "-"
            dashed += 1
        out.append("| " + " | ".join(cells[:1] + [css, page, lvl] + cells[1:]) + " |")
    text = "\n".join(out) + "\n"
    if not check:
        with open(INV, "w", encoding="utf-8") as fh:
            fh.write(text)
    idle = sorted(set(TITLE) - used)
    print("rows with a component: %d, rows deliberately dashed: %d, hand map %d of %d used"
          % (filled, dashed, len(used), len(TITLE)))
    if idle:
        print("hand-map rows that match nothing: " + "; ".join(idle))
    fill_readme(check)
    return text, idle


# ------------------------------------------------------- the count in README --
# README carried "36 components (6 atoms, 9 molecules, 19 organisms)" and those
# three add up to 34. Neither number was wrong: 36 is every component file, and
# 34 is how many of them are COMPOSED, because base and course-chrome are the
# substrate and a substrate has no level. The sentence was wrong, because it
# printed one number and broke it down by the other.
#
# It is written from _levels.py here for the same reason the inventory's level
# column is: a count typed by hand is a second source for something the markup
# already answers, and it drifts on the first component that is added, split or
# folded in. Gate 2 fails the build when this span stops matching.
README = os.path.join(ROOT, "README.md")
SPAN = re.compile(r"(<!-- counts:start -->).*?(<!-- counts:end -->)", re.S)
# The gate count was typed into README.md in two places and the states pass made
# both wrong on the same afternoon. Counted here from the one file that has them,
# by the number each check() announces itself with: the checker prints that number
# and a reader looks it up, so the label and the total cannot disagree.
GATES = re.compile(r"(<!-- gates:start -->).*?(<!-- gates:end -->)", re.S)


def counts():
    """The sentence, from the one place that knows: file count from the same
    rule gate 2 uses, breakdown from the computed level."""
    from _levels import LEVEL, NOT_A_COMPONENT
    files = {f[:-4] for f in os.listdir(COMP) if f.endswith(".css")} - {
        "index", "tokens", "fonts"}
    n = {lvl: sum(1 for c in files if LEVEL.get(c) == lvl) for lvl in (1, 2, 3)}
    substrate = sorted(c for c in files if c in NOT_A_COMPONENT)
    return ("**%d components**, %d of them composed on three levels "
            "(%d atoms, %d molecules, %d organisms, computed from the markup) "
            "and %d that are the substrate a screen stands on rather than a part "
            "of one (`%s`)" % (
                len(files), n[1] + n[2] + n[3], n[1], n[2], n[3],
                len(substrate), "`, `".join(substrate)))


def gate_counts():
    """"N gates in M checks", read out of _check_kit.py."""
    with open(os.path.join(KIT, "_check_kit.py"), encoding="utf-8") as fh:
        src = fh.read()
    calls = re.findall(r'check\(\s*"(\d+) ', src)
    return "**%d gates** in %d checks" % (len(set(calls)), len(calls))


def fill_readme(check=False):
    with open(README, encoding="utf-8") as fh:
        src = fh.read()
    if not SPAN.search(src):
        print("README: no counts span, nothing written")
        return
    new = SPAN.sub(lambda m: m.group(1) + counts() + m.group(2), src)
    new = GATES.sub(lambda m: m.group(1) + gate_counts() + m.group(2), new)
    if new == src:
        print("README counts            unchanged")
        return
    if check:
        print("README counts            STALE")
        return
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    print("README counts            rewritten")


def current():
    """(the inventory as it would be rebuilt, the hand-map rows that match
    nothing). Used by gate 34, which is why main() returns them: a cell that a
    generator would write differently is a document row that does not match the
    product, and a hand-map row that matches nothing is the same defect with the
    arrow reversed."""
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        text, idle = main(check=True)
    with open(INV, encoding="utf-8") as fh:
        return text == fh.read(), idle


if __name__ == "__main__":
    main()
