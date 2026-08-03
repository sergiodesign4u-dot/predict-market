#!/usr/bin/env python3
"""
_states.py  -  are the state pictures still true?

THE PROBLEM A PICTURE HAS. `ui-kit/_verify/states.cjs` photographs every state of
every component with a real pointer, a real Tab and a real press, which is the
only honest way to show what a hover LOOKS like. A photograph then starts going
out of date the moment somebody edits a rule, and it goes out of date SILENTLY:
a stale png renders exactly as confidently as a fresh one. That is the class of
defect gate 29 exists for, one level up.

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
          "ui-kit/_specimen.css", "ui-kit/_verify/states.cjs"]


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


if __name__ == "__main__":
    rows = load()
    if "--stamp" in sys.argv:
        for row in rows:
            row["sources"] = sources(row)
            row["sha"] = digest(row["sources"])
        INDEX.write_text(json.dumps(rows, indent=1) + "\n", encoding="utf-8")
        print("stamped %d group(s), %d picture(s)"
              % (len(rows), sum(len(r.get("shots", {})) for r in rows)))
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
