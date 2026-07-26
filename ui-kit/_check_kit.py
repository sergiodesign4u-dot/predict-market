#!/usr/bin/env python3
"""The gates for the vitrine. One command, exits non-zero on the first failure.

    python3 ui-kit/_check_kit.py

Eight checks, each one a defect that actually happened at least once:

  1. the product did not move        components/ and wireframes/ clean, and a
                                     ui-visual/ page differs only in its sidebar
  2. every component has a specimen  and every id is unique
  3. no dead icon reference          a use with no symbol in the same document
  4. every relative path resolves    the one thing a directory move breaks
  5. no duplicated specimen          the same markup shown on two pages
  6. layer purity                    no stand class in components/, no product class in _page.css
  7. no em dash                      the house rule
  8. the registry is whole           every also target and every nav file exists

The live half of the verification is ui-kit/selftest.html, which loads every
specimen in a frame and asks it whether it rendered. No em dash.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
COMP = ROOT / "components"
SPECS = KIT / "specimens"

fails = []
notes = []


def check(name, ok, detail=""):
    (notes if ok else fails).append("%-34s %s%s" % (name, "ok" if ok else "FAIL",
                                                    (" - " + detail) if detail else ""))


# 1 -------------------------------------------------------------- untouched --
# components/ and wireframes/ may not move at all. ui-visual/ is allowed exactly
# one kind of edit: the course sidebar, which is chrome wrapped AROUND the screen
# and not the screen. So the file is compared with HEAD twice, once as it is and
# once with the <aside> masked out. If masking makes the difference disappear,
# only the tree moved and the product did not.
ASIDE = re.compile(r'<aside class="sidebar" id="rmSidebar">.*?</aside>', re.DOTALL)
moved, chrome_only, tooling = [], [], []
for zone in ("components", "wireframes", "ui-visual"):
    # not .strip(): the leading space of " M path" is part of the status field.
    porcelain = subprocess.run(["git", "status", "--porcelain", "--", zone],
                               cwd=ROOT, capture_output=True, text=True).stdout
    for line in filter(None, porcelain.splitlines()):
        status, path = line[:2].strip(), line[2:].strip()
        if status == "??":
            continue                      # a new file adds nothing to a screen
        if zone != "ui-visual" or status != "M":
            moved.append(path)
            continue
        if not path.endswith(".html"):
            # a generator in ui-visual/ is tooling. What it did to the screens is
            # already measured by the mask check on the pages it wrote.
            tooling.append(path)
            continue
        was = subprocess.run(["git", "show", "HEAD:" + path],
                             cwd=ROOT, capture_output=True, text=True).stdout
        now = (ROOT / path).read_text(encoding="utf-8")
        (chrome_only if ASIDE.sub("", was) == ASIDE.sub("", now) else moved).append(path)
check("1 product untouched", not moved, "%d: %s" % (len(moved), ", ".join(sorted(moved)[:4])))
if chrome_only:
    notes.append("%-34s %s" % ("1 sidebar only", "%d ui-visual pages, screens identical"
                               % len(chrome_only)))
if tooling:
    notes.append("%-34s %s" % ("1 tooling changed", ", ".join(sorted(tooling))))

# 2 ------------------------------------------------------------- specimens --
manifest = json.loads((SPECS / "index.json").read_text(encoding="utf-8"))
ids = [s["id"] for s in manifest]
components = {p.stem for p in COMP.glob("*.css")} - {"index", "tokens"}
owned = {s["component"] for s in manifest}
check("2 every component has one", not (components - owned), ", ".join(sorted(components - owned)))
check("2 specimen ids unique", len(ids) == len(set(ids)))

# 3 ------------------------------------------------------------- dead icons --
dead = []
for page in sorted(list(KIT.glob("*.html")) + list(SPECS.glob("*.html"))):
    src = page.read_text(encoding="utf-8")
    have = set(re.findall(r'<symbol id="([\w-]+)"', src))
    for ref in set(re.findall(r'href="#(i-[\w-]+)"', src)):
        if ref not in have:
            dead.append("%s -> #%s" % (page.name, ref))
check("3 no dead icon reference", not dead, "%d: %s" % (len(dead), ", ".join(dead[:4])))

# 4 ------------------------------------------------------------ every path --
missing = []
ATTR = re.compile(r'(?:src|href)="([^"#][^"]*)"')
GENERATED = [p for p in sorted(list(KIT.glob("*.html")) + list(SPECS.glob("*.html")))
             if p.name not in ("kit.html", "shell.html")]
# The screens' index is checked here too. It is not a stand page, but it reaches
# across into ui-kit/ for the stand stylesheet, and that path is exactly the kind
# a directory move breaks silently.
GENERATED.append(ROOT / "ui-visual" / "overview.html")
for page in GENERATED:
    src = page.read_text(encoding="utf-8")
    for url in set(ATTR.findall(src)) | set(re.findall(r"url\(([^)\"']+)\)", src)):
        # %23 is a "#" inside an already encoded data uri: a nested url(#id)
        # filter reference, not a path to a file.
        if url.startswith(("http", "data:", "mailto:", "#", "%23")):
            continue
        target = (page.parent / url.split("#")[0].split("?")[0]).resolve()
        if not target.exists():
            missing.append("%s -> %s" % (page.name, url))
check("4 every relative path resolves", not missing,
      "%d: %s" % (len(missing), ", ".join(sorted(set(missing))[:4])))

# 5 ------------------------------------------------------------ duplicates --
seen, dupes = {}, []
for s in manifest:
    body = (SPECS / (s["id"] + ".html")).read_text(encoding="utf-8")
    body = body[body.index("<body"):body.index("<script")]
    digest = hashlib.sha256(body.encode()).hexdigest()
    if digest in seen:
        dupes.append("%s == %s" % (s["id"], seen[digest]))
    seen[digest] = s["id"]
check("5 no duplicated specimen", not dupes, ", ".join(dupes))

# 6 ----------------------------------------------------------- layer purity --
page_css = (KIT / "_page.css").read_text(encoding="utf-8")
sels = re.findall(r"(?m)^([.#][^{@]*)\{", re.sub(r"/\*.*?\*/", "", page_css, flags=re.S))
impure = [s.strip() for s in sels
          if not all(re.match(r"^[.](tk|ck)-", part.strip())
                     for part in re.split(r"[ ,>+~]+", s.strip()) if part.strip().startswith("."))]
check("6 _page.css styles no product", not impure, "; ".join(impure[:3]))

stand_in_comp = []
for path in COMP.glob("*.css"):
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    if re.search(r"\.(tk|ck)-[\w-]+", body):
        stand_in_comp.append(path.name)
check("6 components carry no stand class", not stand_in_comp, ", ".join(stand_in_comp))

# 7 --------------------------------------------------------------- em dash --
dash = [p.name for p in
        list(KIT.glob("*.html")) + list(SPECS.glob("*.html")) + list(KIT.glob("*.css"))
        + list(KIT.glob("*.py")) + list(KIT.glob("*.json")) + list((KIT / "docs").glob("*.md"))
        if "\u2014" in p.read_text(encoding="utf-8")]
check("7 no em dash", not dash, ", ".join(dash))

# 8 -------------------------------------------------------------- registry --
nav = (KIT / "_nav.js").read_text(encoding="utf-8")
nav_files = set(re.findall(r'file: "([^"]+)"', nav))
gone = sorted(f for f in nav_files if not (KIT / f).exists())
check("8 every registry page exists", not gone, ", ".join(gone))
# The sidebar writes its own links (the back arrow, the Overview row, the note).
# They are strings inside a script, so gate 4 never sees them.
nav_links = {u for u in re.findall(r"href=\\?\"([^\"'+]+)\\?\"", nav)
             if not u.startswith(("http", "#"))}
nav_dead = sorted(u for u in nav_links if not (KIT / u.split("#")[0]).exists())
check("8 every sidebar link resolves", not nav_dead, ", ".join(nav_dead))
bad_also = sorted({a for s in manifest for a in s.get("also", []) if a not in components})
check("8 every cross reference exists", not bad_also, ", ".join(bad_also))

# ---------------------------------------------------------------- verdict ---
for line in notes + fails:
    print(line)
print("\n%d specimens, %d components, %d stand pages" %
      (len(manifest), len(components), len(list(KIT.glob("*.html")))))
if fails:
    print("\n%d gate(s) failed" % len(fails))
    sys.exit(1)
print("all gates pass")
