#!/usr/bin/env python3
"""
_adoption.py  -  does the PRODUCT wear what the system declares?

WHY IT EXISTS. Gate 14 asks whether a rule can match ANY markup: a selector no
element anywhere carries is a transcript, and 21 of those were found in step 7b.
That question is answered by the union of every tree this stylesheet can reach,
so a class carried only by the frozen kit, only by a specimen or only by the
vitrine's own chrome passes it.

Nobody was asking the other half. A class the system styles, shows on a stand,
and NO painted screen carries is one of exactly two things:

  * dead code, or
  * a naming convention the product never adopted,

and the second is the expensive one, because the stand goes on teaching it. Six
classes of `button.css` were in that state on 2026-08-03: `.btn-primary`,
`.btn-secondary`, `.btn-sm`, `.btn-md`, `.btn-lg`, `.btn-block`, half of what
the component declared, rendered on two specimens, with a size ramp and a
primary/secondary vocabulary the 105 painted screens never used once. The next
person to build a screen would have read the stand, taken `.btn-secondary`, and
added a seventh dead class. That is not a tidiness problem, it is the stand
lying about the system.

WHAT IS MEASURED. For every class styled by a file in `components/` (the folder
and `patterns/`, minus `index.css` and `tokens.css`, and read from the RULES and
not from the prose), how many of the painted screens in `ui-visual/` carry it on
an element. Zero is the finding.

WHAT IS DECLARED. `NOT_WORN` below. A zero can be right for four reasons and
each entry says which, because the same number means "delete me" and "the script
writes this at run time" and only a person can tell those apart. The second
check is the one that keeps the list honest, the way gate 24's does: an entry
that covers no real zero fails just as loudly as an undeclared one, so the
cheapest way past this gate cannot be a new line here, and a debt that gets paid
has to be deleted rather than left lying.

ONE COMPUTATION, TWO CONSUMERS. `_gen_component_pages.py` writes the same answer
into `docs/coverage.md` and into the Classes table of every stand page, and it
used to compute it itself. Two readings of one truth is the defect this repo has
paid for between coverage.md and the css headers, and again between the two
panel generators, so the reading is here and both read it.

    python3 ui-kit/_adoption.py            # the report
    python3 ui-kit/_adoption.py --all      # including what is declared

No em dash.
"""
import glob
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
UV = ROOT / "ui-visual"
KIT = ROOT / "ui-kit"


# ---- the two readings -------------------------------------------------------
def classes_in(pattern, strip_style=False, strip_quoted=False, strip_script=False):
    """Which classes each file puts on an element, by file."""
    out = {}
    for f in sorted(glob.glob(pattern)):
        text = open(f, encoding="utf-8", errors="ignore").read()
        if strip_style:
            text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.S)
        if strip_script:
            # A CLASS INSIDE A JS STRING IS NOT A CLASS ON AN ELEMENT, and this
            # reader was counting one as the other. `.l-yes`, `.l-no` and `.lbls`
            # are on **0** of the 105 painted screens and named in the script of
            # all 105, because the feed script writes the odds bar's labels at
            # run time; gate 30 had been passing all three on the strength of a
            # string literal. It is the rule CLAUDE.md already states - a checker
            # asks the markup, not the text - arriving from a third direction.
            # The tokenizer also picked up `lg-item'+(i===sel?'` and `sel':'')+'`
            # as CLASS NAMES, which is what a reverse gate would have reported as
            # a name the system does not know.
            text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.S)
        if strip_quoted:
            # A stand page ends with the component's own css and every document
            # quotes markup, so class="x" inside <pre> or <code> is a QUOTATION,
            # not an element. The same rule three gates had to learn in step 8b.
            text = re.sub(r"<(pre|code)\b[^>]*>.*?</\1>", "", text, flags=re.S)
        cs = set()
        for m in re.finditer(r'class="([^"]*)"', text):
            cs.update(m.group(1).split())
        out[os.path.basename(f)] = cs
    return out


def flat(d):
    return set().union(*d.values()) if d else set()


uv_classes = classes_in(str(UV / "*.html"), strip_style=True, strip_script=True)
# overview.html lives in ui-visual/ but is the index OF the screens, not one of
# them. Counting it would inflate every screen count by one and, worse, would let
# a class the index happens to use pass as "carried by a painted screen".
uv_classes.pop("overview.html", None)
uv_used = flat(uv_classes)

kit_used = flat(classes_in(str(KIT / "specimens" / "*.html"))) \
    | flat(classes_in(str(KIT / "kit.html"))) | flat(classes_in(str(KIT / "shell.html"))) \
    | flat(classes_in(str(KIT / "*.html"), strip_quoted=True))
wf_used = flat(classes_in(str(ROOT / "wireframes" / "*.html"), strip_style=True,
                          strip_script=True))
docs_used = flat(classes_in(str(ROOT / "*" / "*.html"), strip_style=True)) - uv_used - kit_used


def styled():
    """Every class a component file STYLES, and which file styles it.

    Read from the rules: a class named in a comment is not a class the file
    styles, and a class inside a url() is not a class at all. Both mistakes have
    been made here before and both put an already-deleted class back on the
    deletion list.
    """
    out = {}
    for path in sorted(COMP.glob("*.css")) + sorted((COMP / "patterns").glob("*.css")):
        if path.name in ("index.css", "tokens.css"):
            continue
        body = re.sub(r"/\*.*?\*/", " ", path.read_text(encoding="utf-8"), flags=re.S)
        body = re.sub(r"url\([^)]*\)", "", body)
        for c in set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", body)):
            out.setdefault(c, []).append(path.name)
    return out


# ---- the classes the product does not wear, and why -------------------------
# Never derived by pattern: a pattern that matches "brand" also matches
# "sidebar-brand". Every line was checked by hand against the script that writes
# the class, or against the page that carries it.
#
# FOUR REASONS A ZERO CAN BE RIGHT, and the wording of each entry says which:
#
#   run time   the class is never written into a file. The product wears it, a
#              scan of the markup cannot see it, and deleting it breaks a screen
#              in silence.
#   not the    course-chrome.css draws the roadmap panel this REPO wraps around
#   product    every page. It ships with the system because the painted screens
#              render the panel, but its states belong to the course pages, and
#              those carry their own inline copy and never load this sheet.
#   provenance base.css keeps two rules alive for ui-kit/kit.html, which is
#              frozen and must go on rendering the way it did.
#   an offer   a real utility with a stand and no taker yet. This is the only
#              reason with a shelf life: it is the exact shape the six button
#              classes had, and it closes by a screen taking it or by deletion,
#              never by widening this line.
NOT_WORN = {
    "oddsbar": "run time: the feed script builds the whole bar out of the "
               "probability text, so no screen file contains the element",
    # `.track` and `.fill` were here on the first run and the second check threw
    # them straight back out: the feed script builds the bar, but the painted
    # screens ALSO ship one in the markup, so neither is a zero and neither
    # needed declaring. They were copied from the note the stand pages used to
    # carry, which had no gate under it to notice.
    # THE THREE THE READER USED TO SEE THROUGH A JS STRING. Measured 2026-08-05:
    # each is on an element of 0 painted screens and named in the script of all
    # 105, and the reader was counting the string literal as a placement. Same
    # component and same reason as the entry above; three lines rather than one
    # because this list is keyed by class and a merged line cannot be checked
    # idle.
    "l-yes": "run time: the YES label of the odds bar, written by the feed "
             "script out of the probability text",
    "l-no": "run time: the NO label of the same bar, same script",
    "lbls": "run time: the row that holds those two labels, same script",
    "m-label": "run time: the card meta row, split by the feed script",
    "m-val": "run time: the card meta row, split by the feed script",
    "lg-item": "run time: the chart legend, built by the detail script",
    "scrolled": "run time: added to .app-header by the scroll observer that 192 "
                "painted screens carry, and the condensed strip is drawn from it",
    "open": "run time: toggled on the roadmap drawer and its overlay by script",
    "next": "not the product: a roadmap state on a course page, and the 28 course "
            "pages carry their own inline copy of the panel and never load this sheet",
    "planned": "not the product: the same roadmap state, four rows per course page",
    "theme-switch-inline": "not the product: the theme control of this vitrine, on "
                           "ui-kit/overview.html",
    "tbd": "provenance: ui-kit/kit.html still carries the grey tree's [TBD] chips and "
           "must keep rendering as it did. The painted screens have no such markup, "
           "because ui-visual/_strip_wireframe.py removed it",
    "placeholder-line": "provenance: the same chip family in the same frozen page",
    "groove-sep": "an offer: the frame's groove separator, staged on base.html and "
                  "carried by the frozen kit. Every separator the product ships today "
                  "is a border on the thing it separates. It closes when a screen takes "
                  "it or when it is deleted, not by widening this line",
}


def unadopted():
    """(what the product does not wear and nobody declared, what is declared idle)."""
    worn = {}
    for cs in uv_classes.values():
        for c in cs:
            worn[c] = worn.get(c, 0) + 1
    by_file = styled()
    zero = {c: fs for c, fs in by_file.items() if not worn.get(c)}
    undeclared = sorted("%s (%s)" % (c, ", ".join(fs))
                        for c, fs in zero.items() if c not in NOT_WORN)
    idle = sorted(set(NOT_WORN) - set(zero))
    return undeclared, idle


# ---- the other half: what the product wears that the system does not know ---
# Gate 30 asks system -> product. This asks PRODUCT -> SYSTEM, and it is the
# question nobody in this repo had ever put: for every class a painted screen
# carries, is there a rule in `components/` that reads it?
#
# A NAME WITH NO RULE IS NOT HARMLESS. It looks exactly like a component: the
# next person reads `class="ed-chart"` off a screen, goes looking for
# `components/ed-chart.css`, finds nothing, and either invents it or copies the
# name onto something else. It is gate 14's dead selector seen from the other
# end - there the rule had no element, here the element has no rule - and the
# cost is the same one the six dead button classes cost, a vocabulary the
# product teaches and the system does not have.
#
# THREE REASONS A BARE CLASS CAN BE RIGHT, and the wording of each entry says
# which:
#
#   a hook      a script in the page queries it. It is markup a machine reads,
#               so it has no rule and must not be deleted.
#   excluded    a rule names its siblings and leaves this one out ON PURPOSE.
#               The class is how a person knows which one that is.
#   debt        worn, styled by nothing, read by nothing. It closes by a rule
#               or by deletion, never by widening this line.
#
# Checked one at a time on 2026-08-05, against the inline scripts of the screens
# that carry it and against every rule in components/.
UNSTYLED = {
    "load-more": "a hook and a name, and it stopped carrying paint on 2026-08-07. "
                 "The feed's script reaches for it, and the census names the kind by "
                 "it; what it LOOKS like is `.chip.chip-nav`, which the element now "
                 "carries, because the two were the same graphite chip drawn in two "
                 "files. Same shape as .cmt-post, one migration later: the name tells "
                 "the foot of a list from a category in a strip, and nothing else",
    "ed-act": "a hook: the detail script queries it. Every one of them also "
              "stands inside .ed-actions, which styles `button`, so the class "
              "carries no paint and the control is not bare",
    "ed-chart": "a hook: the detail script queries the chart section to draw "
                "into it. Its parts are styled - .ed-chart-head, -area, -foot, "
                "-now in components/chart.css - and the section itself is an "
                ".ed-section",
    "ed-chart-multi": "a hook: the same script, telling a multi-outcome chart "
                      "from a binary one",
    "rules-panel": "a hook: the detail script shows and hides it, which is why "
                   "one of the two ships with `hidden` on it",
    "prov-google": "excluded: components/button.css recolours .prov-x and "
                   ".prov-apple to the brand mark and deliberately does NOT "
                   "name this one, because the Google logotype is full-colour "
                   "and a recoloured logotype is the wrong mark. The class is "
                   "how a reader knows the omission was a decision",
    "cmt-post": "a name the CENSUS reads, and the first class this repo has kept for "
                "that reason alone. The Post button adopted `btn btn-primary btn-sm` on "
                "2026-08-06 and is the family in every value, so nothing paints it and "
                "no script queries it; what the name still does is tell the composer's "
                "one commitment from 78 other small brass presses in `_worn.KINDS`, "
                "which is what keeps `.cmt-signin` staged beside it. Deleting it was "
                "tried and reverted, and the reason is written on that row",
    "ed-market": "debt: a second name on a section that is already an "
                 ".ed-section, read by no script and matched by no rule. 9 "
                 "screens. It closes by a rule or by deletion",
    "toast-wrap": "debt: the wrapper around the toast specimens on one screen, "
                  "read by no script and matched by no rule. 1 screen",
}


def unstyled():
    """(worn with no rule and nobody declared, declared idle, every bare class).

    The reading is `ui-visual/` only. wireframes/ carries its own inline
    grey-box css and never links components/index.css, so a class there is not a
    class this system was ever asked about.
    """
    known = set(styled())
    bare = sorted(c for c in uv_used if c not in known)
    undeclared = [c for c in bare if c not in UNSTYLED]
    idle = [c for c in sorted(UNSTYLED) if c not in bare]
    return undeclared, idle, bare


def where(c):
    """Why this class shows the count it shows. Used by the stand pages."""
    if c in uv_used:
        return "", ""
    if c in NOT_WORN:
        kind = NOT_WORN[c].split(":")[0]
        return ("runtime" if kind == "run time" else
                "kit" if kind in ("provenance", "an offer") else "docs"), NOT_WORN[c]
    if c in kit_used:
        return "kit", "shown in the kit, never on a painted screen, and not declared"
    if c in wf_used:
        return "wireframe", "carried only by wireframes/, which never loads this sheet"
    if c in docs_used:
        return "docs", "used by a course page, which does not load the system"
    return "unused", "styled and carried by no element anywhere"


if __name__ == "__main__":
    undeclared, idle = unadopted()
    by_file = styled()
    print("%d classes styled in components/, %d of them on 0 of %d painted screens"
          % (len(by_file), len([c for c in by_file if c not in flat(uv_classes)]),
             len(uv_classes)))
    print("\n%d not declared:" % len(undeclared))
    for u in undeclared:
        print("   ." + u)
    if idle:
        print("\n%d declared and idle (the zero is gone, delete the line):" % len(idle))
        for i in idle:
            print("   ." + i)
    if "--all" in sys.argv:
        print("\n%d declared:" % len(NOT_WORN))
        for c in sorted(NOT_WORN):
            print("   .%-20s %s" % (c, NOT_WORN[c]))

    # the other direction, printed by the same command because it is the same
    # two readings and a person asking one question wants both answers
    bare_undeclared, bare_idle, bare = unstyled()
    print("\n%d of the %d classes the painted screens wear have no rule in "
          "components/" % (len(bare), len(uv_used)))
    if bare_undeclared:
        print("\n%d not declared:" % len(bare_undeclared))
        for u in bare_undeclared:
            print("   ." + u)
    if bare_idle:
        print("\n%d declared and idle (the class is styled now, delete the line):"
              % len(bare_idle))
        for i in bare_idle:
            print("   ." + i)
    if "--all" in sys.argv:
        print("\n%d declared bare:" % len(UNSTYLED))
        for c in sorted(UNSTYLED):
            print("   .%-20s %s" % (c, UNSTYLED[c]))
    sys.exit(1 if (undeclared or idle or bare_undeclared or bare_idle) else 0)
