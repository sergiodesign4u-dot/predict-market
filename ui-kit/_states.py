#!/usr/bin/env python3
"""
_states.py  -  are the state pictures still true?

THE PROBLEM A PICTURE HAS. `ui-kit/_verify/states.cjs` photographs every state of
every component with a real pointer, a real Tab and a real press, which is the
only honest way to show what a hover LOOKS like. A photograph then starts going
out of date the moment somebody edits a rule, and it goes out of date SILENTLY:
a stale png renders exactly as confidently as a fresh one. That is the class of
defect gate 29 exists for, one level up.

WHAT THE STAND PAGES ACTUALLY SHOW, SINCE 2026-08-04, AND IT IS NO LONGER THE
PICTURE. The capture writes two things per state per theme, a png and the nine
values the face was read at, and the pages now render the values: what the face
IS at rest, and what each state MOVES. A photograph of a control is a photograph
of something the reader can hover three sections up the same page, and the crop
around it was derived per side from the distance to the nearest neighbour, so
the subject sat off centre in its own frame. The picture survives on `disabled`,
which is the one state nobody can raise by hand. Everything below is unchanged
and now guards the numbers as well as the four remaining images, which is the
same question either way: is this what the browser would produce today. The 710
pictures the pages stopped linking are `ui-kit/docs/backlog.md` S30.

WHY IT IS NOT A PIXEL COMPARISON. The obvious check is "take the picture again
and compare". It cannot be a build gate: it needs a browser, a served tree and
about a minute, and `_check_kit.py` is Python that runs anywhere in a second and
a half. A comparison that only some machines can run is a comparison nobody
runs.

WHAT IS COMPARED INSTEAD. A picture is a function of its sources, and the
sources are files. For each captured group the manifest records which classes
stood in the document it was shot from; those map to the component files that
paint them through `_levels.OWNER`, and the hash covers:

    components/tokens.css        every colour resolves through it
    components/base.css          the frame the specimen stands in
    components/fonts.css         the faces, so a metric change is caught
    components/<owner>.css       every component visible in that document
    ui-kit/specimens/<id>.html   the markup that was photographed
    ui-kit/_specimen.css         the staging the specimen page adds
    ui-kit/_verify/states.cjs    how the picture was taken

If none of those bytes moved, the picture is what the browser would produce
today. If any of them moved, it MIGHT not be, and "might not" is what a gate is
for: the answer is to run the capture again, which is one command.

    python3 ui-kit/_states.py --stamp    after a capture, write the hashes
    python3 ui-kit/_states.py --check    exits 1 if anything is stale

No em dash.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
COMP = ROOT / "components"
OUT = KIT / "_states"
INDEX = OUT / "index.json"

sys.path.insert(0, str(KIT))
from _levels import OWNER                                             # noqa: E402

# Read by every document, so a change to any of them can change any picture.
ALWAYS = ["components/tokens.css", "components/base.css", "components/fonts.css",
          "ui-kit/_specimen.css", "ui-kit/_verify/states.cjs",
          # browser.cjs decides a picture as much as states.cjs does and was not
          # in this list. It holds what a face IS, how long a state is allowed to
          # settle before it is read, and how the frame is derived from the
          # subject: changing any of the three changes every picture and every
          # value in the manifest, and the hash said nothing had moved. Added
          # 2026-08-04, when a settle fix in that file would otherwise have left
          # 95 groups stamped as current against an instrument that no longer
          # produces them.
          "ui-kit/_verify/browser.cjs"]


def sources(row):
    """The files whose bytes decide this group's pictures, sorted and unique."""
    files = set(ALWAYS)
    files.add("ui-kit/specimens/%s.html" % row["specimen"])
    for spec in row.get("also", []):
        files.add("ui-kit/specimens/%s.html" % spec)
    for cls in row.get("classes", []):
        owner = OWNER.get(cls)
        if not owner:
            continue
        # patterns/ files own classes too and are named with their folder
        path = COMP / (owner + ".css")
        if path.exists():
            files.add("components/%s.css" % owner)
        elif (COMP / "patterns" / (owner.split("/")[-1] + ".css")).exists():
            files.add("components/patterns/%s.css" % owner.split("/")[-1])
    return sorted(files)


def digest(files):
    h = hashlib.sha256()
    for rel in files:
        path = ROOT / rel
        h.update(rel.encode("utf-8"))
        h.update(path.read_bytes() if path.exists() else b"<missing>")
    return h.hexdigest()[:16]


def load():
    return json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else []


def stale():
    """(rows whose sources moved, rows whose picture file is gone)."""
    moved, missing = [], []
    for row in load():
        want = digest(sources(row))
        if row.get("sha") != want:
            moved.append("%s %s" % (row["component"], row["id"]))
        for key, shot in row.get("shots", {}).items():
            if not (OUT / shot["file"]).exists():
                missing.append("%s %s %s" % (row["component"], row["id"], key))
    return moved, missing


# The name a person writes a caption against, and it may not be the group id.
# `g3` is a counter: a recapture that finds a new face renumbers everything after
# it and silently re-points every caption in the authored file. The key is what
# the element IS - its own label and the scope it stands in - which survives a
# recapture, and an ordinal is added only where one document holds two faces of
# the same thing (the action bar, whose first child is brass and whose second is
# quiet, and neither carries a class of its own).
def keyed(rows):
    seen = {}
    out = []
    for row in sorted(rows, key=lambda r: (r["component"], int(r["id"][1:]))):
        base = "%s @%s" % (row["el"], row.get("scope") or row["specimen"])
        seen[base] = seen.get(base, 0) + 1
        row = dict(row)
        row["key"] = base if seen[base] == 1 else "%s (%d)" % (base, seen[base])
        out.append(row)
    return out


def by_component():
    """The manifest as the page generator wants it: component -> [group]."""
    out = {}
    for row in keyed(load()):
        out.setdefault(row["component"], []).append(row)
    return out


# ---- the components with no photograph, and why -----------------------------
# FRESHNESS IS HALF THE QUESTION. A stamp says a picture is what its sources
# would produce today; it says nothing about a picture that was never taken, and
# a picture never taken is fresh forever. An empty gallery reads as "this
# component has no states", and on two pages that is FALSE: `position.css` and
# `state-block.css` each declare a hover and each photographed nothing.
#
# So the second half of gate 31 asks the reverse, and the answer is a declared
# list with the control every declared list in this repo carries: an entry that
# DOES have pictures fails as loudly as a component that has none and is not
# here.
#
# Two kinds, and the second is a debt rather than a decision:
#
#   STATIC     the component was decided to have no interaction at all, one line
#              and one reason each in `_levels.STATIC`. Read from there rather
#              than repeated, because gate 25 already holds that list in both
#              directions and a second copy would drift.
#   NOT_SHOT   the component HAS a state and the instrument could not take it.
#              Each line names the selector and the reason, and neither of the
#              two is a fact about the component.
NOT_SHOT = {
    "position": "`.app-case a:has(>.pos):hover>.pos`. The element that CHANGES is the row and "
                "the element that is HOVERED is the anchor around it, and states.cjs points at "
                "the subject of the rule, so the pass hovered a row that answers no pointer and "
                "recorded no difference. In the product 36 screens of lists do answer. A reader "
                "gap: closing it means teaching states.cjs to hover an ancestor, which changes "
                "what every gallery measures",
    "state-block": "`.app-case .sys-link-list a:hover`. The three specimens are the empty and "
                   "error blocks of a browse screen and none carries a system screen's link "
                   "list, so there was nothing to open. A stand debt, not a reader bug",
}


# ---- the third question, and it is about the INSTRUMENT rather than the tree --
# FRESHNESS AND COVERAGE BOTH ASSUME THE PICTURE SHOWS THE SUBJECT. Neither asks
# whether the frame was big enough to hold it, and for 36 of 790 pictures it was
# not: `boxAt` padded each side to at most HALF the distance to the nearest
# neighbour, which is right, and then let that halving win against the subject's
# own paint, which is not. The specimen row set a 14px gap, so every facing side
# was capped at 7px whatever the caller asked for; the page had no padding, so a
# control at x=0 got nothing at all. Both bit hardest on the FOCUS pictures,
# which is the one state whose entire subject is a ring drawn OUTSIDE the box.
#
# THE CROP WAS IN THE PNG, so nothing on the page that displays it could have put
# a pixel back, and nothing on the page could have reported it either: a
# confidently rendered photograph of a cropped thing looks exactly like a
# photograph. That is `ui-kit/docs/defects.md` row 43, and it is row 42's shape -
# an instrument reporting a clean result about a subject it was not fully
# looking at.
#
# So the capture now DERIVES the pad from the element it is photographing, in the
# state it is in, and records both what it needed and what it got. This reads the
# difference back out of the manifest. It is the cheap half of the check and it
# is the half that can be a gate: no browser, no served tree, just the number the
# capture wrote down.
# The frames that are short and are short for a reason ABOUT THE PRODUCT rather
# than about the stand, one line and one reason each, and the same control every
# declared list here carries: an entry that is no longer short fails as loudly as
# an undeclared crop. The fix took 36 crops to 6 and these are the 6.
TIGHT = {
    ("tabs", "g1"): "`input.ed-tabradio` is parked at `left:-9999px` and the ring the "
                    "system draws on :focus-visible is therefore painted off the left "
                    "edge of the document. That is not a crop, it is the reason "
                    "`tabs.css` moves the visible indicator onto the LABEL and says so "
                    "at the declaration. A frame that held this ring would be a picture "
                    "of a thing no person can see",
    # g8 and g9 until 2026-08-04. A group id is a counter, and adding the scope
    # to the capture key renumbered every group after the first change: this list
    # is keyed on the id, so both entries pointed one row to the left. The idle
    # control is what said so, which is the whole reason a declared list carries
    # one. The subjects are unchanged and are named here so the next renumbering
    # is a lookup rather than a puzzle.
    ("header", "g9"): "a link inside the notifications dropdown, 2px from its neighbour, "
                      "so the halving leaves 1 of the 4 the ring needs. The stand is not "
                      "padded to flatter the camera: the density is the product's, the "
                      "ring is drawn, and 3px of it are shared with the row above",
    ("header", "g10"): "`a.notif-all`, the same dropdown and the same 2px, for the same "
                       "reason",
}


def cropped():
    """(pictures whose frame did not hold what the subject paints outside its box
    and are not declared, declared entries that are no longer short)."""
    out, seen = [], set()
    for row in load():
        for key, shot in row.get("shots", {}).items():
            if not shot.get("short"):
                continue
            k = (row["component"], row["id"])
            if k in TIGHT:
                seen.add(k)
                continue
            out.append("%s %s %s short %dpx (needed %s, got %s)"
                       % (row["component"], row["id"], key, shot["short"],
                          shot.get("needed"), shot.get("pad")))
    idle = ["%s %s" % k for k in sorted(set(TIGHT) - seen)]
    return out, idle


# ---- the fourth question: is this group a DIFFERENCE or an OCCURRENCE? -------
# WHAT A GALLERY IS FOR. The button page carried eight of them and the product
# has five decisions, because the capture keyed a group on the element's class
# name plus its REST face, so one control under two names came out as two
# pictures. `ui-kit/authored/button.md` said so itself, three times, in its own
# prose - "Identical answers, which is the point", "Same three-step", "the answer
# is the family's" - and the vitrine photographed all three anyway: 24 pictures
# whose content was that two things look the same. A page built that way grows
# one gallery per PLACE, so it tracks the product's markup instead of the
# system's decisions, which is backwards for a page whose whole job is to say
# what the decisions are.
#
# THE FORMULA, AND WHY THIS IS IT. "The number of galleries equals the number of
# named differences plus one base set" is the same sentence as "no two groups are
# the same answer": the group that differs from nothing is the base, and every
# other one is a difference or it should not be a gallery. This is the second
# form because it is the one that can be computed. Gate 32 already binds one
# authored caption to one group in both directions, so counting captions and
# counting groups is the same count, and a count compared with itself proves
# nothing.
#
# WHAT COUNTS AS THE SAME ANSWER: the face in all four states in both themes,
# read out of the manifest, which records what each picture was TAKEN at. Not the
# rest face alone. `.provider-btn` and `.auth-btn` rest identically and part
# company on hover by one pixel, and the instrument could not see even that until
# `transform` and `box-shadow` were added to what a face is made of.
def signature(row):
    """What this group answers, in every state and both themes."""
    shots = row.get("shots", {})
    return "\n".join("%s=%s" % (k, shots[k].get("value")) for k in sorted(shots))


def duplicated():
    """component -> [[group ids that are one answer], ...]. Empty is the goal."""
    out = {}
    for name, groups in by_component().items():
        seen = {}
        for row in groups:
            seen.setdefault(signature(row), []).append(row["id"])
        same = [ids for ids in seen.values() if len(ids) > 1]
        if same:
            out[name] = sorted(same)
    return out


def orphans():
    """Pictures on disk that belong to no group. The other direction of the
       missing-file check, and it was not free: two `tabs` focus pictures had
       been sitting in the tree with nothing pointing at them, kept alive by a
       check that only ever asked whether a named file was still there."""
    known = {shot["file"] for row in load() for shot in row.get("shots", {}).values()}
    return sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*.png")
                  if str(p.relative_to(OUT)) not in known)


def unphotographed():
    """(components that should have a picture and have none and are not
    declared; declared entries that DO have pictures)."""
    import _levels
    shot = set(by_component())
    live = {p.stem for p in COMP.glob("*.css")
            if p.stem not in ("index", "tokens", "fonts")} - set(_levels.STATIC)
    return sorted(live - shot - set(NOT_SHOT)), sorted(set(NOT_SHOT) & shot)


if __name__ == "__main__":
    rows = load()
    if "--stamp" in sys.argv:
        for row in rows:
            row["sources"] = sources(row)
            row["sha"] = digest(row["sources"])
        INDEX.write_text(json.dumps(rows, indent=1) + "\n", encoding="utf-8")
        print("stamped %d group(s), %d picture(s)"
              % (len(rows), sum(len(r.get("shots", {})) for r in rows)))
    elif "--crop" in sys.argv:
        short, idle = cropped()
        print("%d undeclared crop(s) of %d picture(s), %d declared, %d idle"
              % (len(short), sum(len(r.get("shots", {})) for r in rows),
                 len(TIGHT), len(idle)))
        for c in short:
            print("   " + c)
        for c in idle:
            print("   IDLE: " + c)
        sys.exit(1 if (short or idle) else 0)
    else:
        moved, missing = stale()
        print("%d group(s), %d picture(s), %d component(s)"
              % (len(rows), sum(len(r.get("shots", {})) for r in rows),
                 len({r["component"] for r in rows})))
        if moved:
            print("stale, a source moved (re-run ui-kit/_verify/states.cjs):")
            for m in moved:
                print("   " + m)
        if missing:
            print("missing picture file:")
            for m in missing:
                print("   " + m)
        if not moved and not missing:
            print("every picture is what its sources would produce today")
        sys.exit(1 if (moved or missing) else 0)
