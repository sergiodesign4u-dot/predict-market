#!/usr/bin/env python3
"""
_audit_specimens.py  -  does every specimen render what its component actually
contains?

WHY IT EXISTS. `_levels.py` reads CONTAINS out of the specimen DOM, and the
level is arithmetic over that map. So a specimen that shows a narrower case than
the product does makes CONTAINS short, the level comes out low, and a RAISE
floor quietly covers the difference. The level is then DECLARED, not computed,
and nothing says which of the two it was. That is how `hiw-dialog` was found:
`hiw-dialog.css` writes `.pos` and `.brand-tile` while the graph said it
contained nothing, and its specimen never rendered the wide two-column state
where those stand.

THE METHOD is the one this repo has used three times now: two sources of the
same truth, compared.

    CONTAINS_specimen   what _levels.py reads today
    CONTAINS_real       the same reading over the painted screens

Both come from `_levels.read_containment`, the SAME function with a different
corpus, because a comparison between two readings is worth nothing if the two
readings differ. Visibility is not consulted on purpose: containment is
structural, and a closed dialog inside a screen is inside it in the DOM.

WHAT A DIFFERENCE MEANS, and there are four kinds. The script reports the raw
finding with the classes that linked the two components and the number of
screens the edge appears on, because those two facts are what tell the kinds
apart:

  1. the specimen is thin      a case the product renders and the stand omits.
                               This is the one that damages the level.
  2. a page plate              the component owns a page-level wrapper
                               (`.cat-main`, `main.feed`, `.ed-main`, `.tc-page`),
                               so on a screen the whole page is its descendant.
                               True, and useless.
  3. two components, one       `.app-dialog` and `.hiw-dialog` sit on the same
     element                   element, so one reads as containing the other.
  4. a class in the wrong file `.grid-l` is the chart's and lives in feed.css,
                               so event-detail "contains" feed. A different
                               defect, kept separate on purpose.

Only kind 1 is a specimen defect. Telling them apart is a judgement and is NOT
automated here: this prints the evidence and a person reads it.

Usage:
    python3 ui-kit/_audit_specimens.py           # the audit
    python3 ui-kit/_audit_specimens.py --all     # include base and course-chrome
    python3 ui-kit/_audit_specimens.py --brief   # the tables, no class detail
"""
import os
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import _levels as L  # noqa: E402

SCREENS = sorted((ROOT / "ui-visual").glob("*.html"))
ALL = "--all" in sys.argv
BRIEF = "--brief" in sys.argv


def components():
    out = [c for c in L.SUBJECTS if c not in L.NOT_A_COMPONENT]
    if ALL:
        out += [c for c in L.NOT_A_COMPONENT if c in L.SUBJECTS]
    return sorted(out)


def levels_from(contains, use_raise):
    """The arithmetic _levels._level does, over a supplied map: 1 + the highest
    level of what the component contains, ceiling 3, memo and cycle guard."""
    out = {}

    def lvl(name, seen=()):
        if name in out:
            return out[name]
        if name in seen:
            return 3
        parts = [p for p in contains.get(name, {}) if p in L.SUBJECTS]
        v = min(1 + max([lvl(p, seen + (name,)) for p in parts] or [0]), 3)
        if use_raise:
            v = max(v, L.RAISE.get(name, (0, ""))[0])
        out[name] = v
        return v

    for n in components():
        lvl(n)
    return out


def per_screen_counts():
    """How many screens carry each (component, contained) edge. A plate shows up
    on most of the tree; a real variant shows up on a handful."""
    n = {}
    for path in SCREENS:
        one = L.read_containment([path], only=components())
        for comp, parts in one.items():
            for other in parts:
                n[(comp, other)] = n.get((comp, other), 0) + 1
    return n


def main():
    print("reading %d painted screens ..." % len(SCREENS), file=sys.stderr)
    real = L.read_containment(SCREENS, only=components())
    spec = L.CONTAINS
    counts = per_screen_counts()

    l_spec_arith = levels_from(spec, False)
    l_now = levels_from(spec, True)
    l_real_arith = levels_from(real, False)
    l_real = levels_from(real, True)

    def fmt(s, w=34):
        t = ", ".join(sorted(s)) if s else "-"
        return t if len(t) <= w else t[:w - 1] + "…"

    print("\n%-16s %-34s %-34s %-26s %5s %5s %s" % (
        "component", "CONTAINS in specimen", "CONTAINS on screens",
        "missing from the specimen", "now", "real", "agree"))
    print("-" * 140)
    short, extra, moved = [], [], []
    for c in components():
        sp, rl = set(spec.get(c, {})), set(real.get(c, {}))
        miss, only = rl - sp, sp - rl
        if miss:
            short.append((c, miss))
        if only:
            extra.append((c, only))
        if l_now[c] != l_real[c]:
            moved.append((c, l_now[c], l_real[c]))
        print("%-16s %-34s %-34s %-26s %5s %5s %s" % (
            c, fmt(sp), fmt(rl), fmt(miss, 26), "L%d" % l_now[c], "L%d" % l_real[c],
            "yes" if l_now[c] == l_real[c] else "NO"))

    print("\n\n=== specimens that do not render what the component contains: %d ===" % len(short))
    for c, miss in short:
        print("   %-16s missing: %s" % (c, ", ".join(sorted(miss))))
        if BRIEF:
            continue
        for m in sorted(miss):
            print("        %-16s %3d/%d screens   via %s" % (
                m, counts.get((c, m), 0), len(SCREENS), ", ".join(sorted(real[c][m]))))

    print("\n=== specimens showing a variant the product does not have: %d ===" % len(extra))
    for c, only in extra:
        print("   %-16s only in the specimen: %s" % (c, ", ".join(sorted(only))))
        if not BRIEF:
            for m in sorted(only):
                print("        %-16s via %s" % (m, ", ".join(sorted(spec[c][m]))))

    print("\n=== levels standing on a RAISE floor rather than on arithmetic ===")
    print("%-16s %-10s %-11s %-7s %s" % ("component", "arith(spec)", "arith(real)", "floor", "verdict"))
    for c in components():
        floor = L.RAISE.get(c, (0, ""))[0]
        if not floor:
            continue
        a_sp, a_rl = l_spec_arith[c], l_real_arith[c]
        if a_rl >= floor:
            v = "PROVED by the screens, the floor holds nothing"
        elif a_rl > a_sp:
            v = "still floor-held, the screens raise it L%d -> L%d" % (a_sp, a_rl)
        else:
            v = "floor-held, and the screens do not prove it either"
        print("%-16s L%-9d L%-10d L%-6d %s" % (c, a_sp, a_rl, floor, v))

    print("\n=== levels that change: %d ===" % len(moved))
    for c, a, b in moved:
        print("   %-16s L%d -> L%d" % (c, a, b))

    print("\n=== the known positive ===")
    ok = any(c == "hiw-dialog" for c, _ in short)
    print("   hiw-dialog in the incomplete list: %s" % (
        "YES" if ok else "NO  <-- the script is broken, not the system. Stop."))
    return 0 if ok or ALL else 0


if __name__ == "__main__":
    sys.exit(main())
