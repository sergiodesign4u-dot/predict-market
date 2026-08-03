#!/usr/bin/env python3
"""The gates for the vitrine. One command, exits non-zero on the first failure.

    python3 ui-kit/_check_kit.py

Twenty-two checks, each one a defect that actually happened at least once:

  1. the product did not move        components/ and wireframes/ clean, and a
                                     ui-visual/ page differs only in its sidebar
  2. every component has a specimen  and every id is unique
  3. no dead icon reference          a use with no symbol in the same document
  4. every relative path resolves    the one thing a directory move breaks
  5. no duplicated specimen          the same markup shown on two pages
  6. layer purity                    no stand class in components/, no product class in _page.css
  7. no em dash                      the house rule
  8. the registry is whole           every also target and every nav file exists
  9. one source of css               no screen styles itself, in a block OR in an
                                     attribute; every screen links
                                     components/index.css and nothing else
 10. the painted product navigates   no link is dead in colour that is live in grey
 11. no orphan token                 a value nobody reads is a transcript, not a system
 12. no raw scale value              a number typed into a rule is how a scale stops
                                     being one, and a stacking order is a scale
 13. colour goes through a role      a component reads a role, never a primitive,
                                     and every screen and frame can switch theme
 14. no selector without markup      a rule nothing on any page can match is a
                                     fossil, the other half of gate 11
 15. one h1, no skipped level        in BOTH trees, because structure is owned by
                                     wireframes/ and the paint only follows
 16. every declaration parses        prose inside a block drops every rule after it
 17. every mark is on the sheet      the other direction of gate 3: an icon a screen
                                     draws that the vitrine does not show
 18. the two trees agree             structure, in five regions, AND every screen in
                                     either tree has a twin in the other, because a
                                     pair that does not exist is not a pair that agrees
 19. one dialog, one copy            a dialog that also has a standalone page is one
                                     markup, not two
 20. no external font host           the faces are in this repo, every page reaches
                                     them, and every file an @font-face names exists
 21. every document has a page       a .md in ui-kit/docs/ is rendered, and current,
                                     and nothing links a raw one
 22. the panel says where you are    every screen's side panel marks its own file,
                                     and every panel is at its generator's fixed
                                     point, because a generator that copies a shell
                                     copies the shell's idea of where it is

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
UVIS = ROOT / "ui-visual"
SPECS = KIT / "specimens"
# EVERY STYLESHEET OF THE SYSTEM, which after the patterns step is not the same
# set as "every component". components/patterns/ holds compositions rather than
# components: they get no level, no specimen, no stand page and no states, so
# gate 2 and gate 25 must NOT see them. But they are css in this system, they
# read the same roles and they ship on the same screens, so every gate about how
# a stylesheet is WRITTEN has to: no em dash, no dangling var, no colour
# primitive, no raw scale value, no selector without markup, no unparsable
# declaration. A gate that stops at the folder boundary is a gate that stops.
SHEETS = sorted(COMP.glob("*.css")) + sorted((COMP / "patterns").glob("*.css"))

# EVERY GENERATED PAGE OF THE VITRINE, and the same lesson one level up. Three
# gates spelled their corpus as KIT.glob("*.html") + SPECS.glob("*.html"), which
# was every generated page right up until step 4 added a second folder of them:
# ui-kit/patterns/ holds the scene each pattern is rendered in, and those are
# generated documents exactly like a specimen. Proved by planting a dead icon
# reference, a src at a file that does not exist and an em dash in one scene:
# gates 3, 4 and 7 all reported clean. A corpus written as a folder goes blind
# the day a second folder of the same thing appears, and it goes blind SILENTLY,
# which is the only kind of blindness that matters.
SCENES = KIT / "patterns"
GENERATED_PAGES = (sorted(KIT.glob("*.html")) + sorted(SPECS.glob("*.html"))
                   + sorted(SCENES.glob("*.html")))

fails = []
notes = []


def check(name, ok, detail=""):
    (notes if ok else fails).append("%-34s %s%s" % (name, "ok" if ok else "FAIL",
                                                    (" - " + detail) if detail else ""))


# 1 -------------------------------------------------------------- untouched --
# The three zones hold different kinds of file, so "untouched" has to mean a
# different thing in each. What decides it is not the folder, it is whether the
# file IS a screen or WRITES one.
#
#   components/  no exception at all. A .css here is not a description of the
#                product, it is the thing that paints it, so the file and the
#                product are one object and there is no second copy to measure
#                against.
#   wireframes/  the .html files are the screens and are compared whole, byte
#                for byte. The .py files under _generators/ are tooling.
#   ui-visual/   the .html files are the screens, but they are allowed exactly
#                one kind of edit: the course sidebar, which is chrome wrapped
#                AROUND the screen and not the screen. So the file is compared
#                with HEAD twice, once as it is and once with the <aside> masked
#                out. If masking makes the difference disappear, only the tree
#                moved and the product did not. Everything else in the zone is
#                tooling.
#
# So two zones have a tooling bucket and one does not, and the argument is the
# same sentence in both of them: a generator is not a screen, and whatever it
# did to the screens is already measured on the pages it wrote. The bucket was
# open to ui-visual/ only, which meant editing a COMMENT in a wireframes
# generator failed the gate, and that is worth fixing for a reason that has
# nothing to do with tidiness: a gate that fails on something harmless teaches
# you to wave it through, and after the third false positive it has stopped
# meaning anything.
ASIDE = re.compile(r'<aside class="sidebar" id="rmSidebar">.*?</aside>', re.DOTALL)
# the theme boot script is chrome by the same argument as the sidebar: it is
# wrapped around the screen, sets an attribute on <html> and paints nothing.
# Built and removed by ui-visual/_theme_switch.py.
BOOT = re.compile(r'\n?<script id="uvTheme">.*?</script>', re.DOTALL)


def bare(html):
    return BOOT.sub("", ASIDE.sub("", html))


def is_tooling(zone, path):
    """A file in this zone that writes screens rather than being one."""
    if zone == "ui-visual":
        return not path.endswith(".html")
    if zone == "wireframes":
        return path.startswith("wireframes/_generators/") and path.endswith(".py")
    return False           # components/ is the product, not a description of it


moved, chrome_only, tooling = [], [], []
for zone in ("components", "wireframes", "ui-visual"):
    # not .strip(): the leading space of " M path" is part of the status field.
    porcelain = subprocess.run(["git", "status", "--porcelain", "--", zone],
                               cwd=ROOT, capture_output=True, text=True).stdout
    for line in filter(None, porcelain.splitlines()):
        status, path = line[:2].strip(), line[2:].strip()
        if status == "??":
            continue                      # a new file adds nothing to a screen
        if status == "M" and is_tooling(zone, path):
            tooling.append(path)
            continue
        if zone != "ui-visual" or status != "M":
            moved.append(path)
            continue
        was = subprocess.run(["git", "show", "HEAD:" + path],
                             cwd=ROOT, capture_output=True, text=True).stdout
        now = (ROOT / path).read_text(encoding="utf-8")
        (chrome_only if bare(was) == bare(now) else moved).append(path)
check("1 product untouched", not moved, "%d: %s" % (len(moved), ", ".join(sorted(moved)[:4])))
if chrome_only:
    notes.append("%-34s %s" % ("1 sidebar only", "%d ui-visual pages, screens identical"
                               % len(chrome_only)))
if tooling:
    notes.append("%-34s %s" % ("1 tooling changed", ", ".join(sorted(tooling))))

# 2 ------------------------------------------------------------- specimens --
manifest = json.loads((SPECS / "index.json").read_text(encoding="utf-8"))
ids = [s["id"] for s in manifest]
# index is the entry point and tokens are the values, so neither is a
# component with a stand. fonts joined them in step 8 for the same reason:
# it declares eighteen faces and styles nothing, and a stand page showing
# "the font component" would be showing every other page.
components = {p.stem for p in COMP.glob("*.css")} - {"index", "tokens", "fonts"}
owned = {s["component"] for s in manifest}
check("2 every component has one", not (components - owned), ", ".join(sorted(components - owned)))
check("2 specimen ids unique", len(ids) == len(set(ids)))
# README used to say "36 components (6 atoms, 9 molecules, 19 organisms)", and
# those three add to 34. Both numbers were right and the sentence was not: 36 is
# every component file, 34 is how many of them are COMPOSED, because base and
# course-chrome are the substrate and a substrate has no level. It is written by
# _fill_inventory.py now, from _levels.py, and a generated span is only single
# sourced while something fails when it goes stale.
sys.path.insert(0, str(KIT))
import _levels                                                        # noqa: E402
from _fill_inventory import counts as readme_counts, SPAN as README_SPAN  # noqa: E402
from _fill_inventory import gate_counts, GATES as README_GATES            # noqa: E402

_readme = (ROOT / "README.md").read_text(encoding="utf-8")
_span = README_SPAN.search(_readme)
check("2 the README count is current", bool(_span) and _span.group(0) ==
      "<!-- counts:start -->" + readme_counts() + "<!-- counts:end -->",
      "run: python3 ui-kit/_fill_inventory.py")
# The same lesson one line down. "24 gates" was typed into README.md twice and
# this file grew a twenty-fifth, so both sentences were wrong the moment the gate
# landed. Counted from the numbers the checks announce themselves with, and both
# spans have to agree, because a fact written twice is a fact that drifts.
#
# The first cut of this check did not fail when it should have, and it is worth
# the two lines it costs to say why: it asked whether the correct sentence was IN
# the file, once, which one right span satisfies however wrong the other one is.
# `in` answers a question about the document; the question here is about each
# span. So it counts, and both have to be right.
_want = "<!-- gates:start -->" + gate_counts() + "<!-- gates:end -->"
check("2 the README gate count is current",
      len(README_GATES.findall(_readme)) == _readme.count(_want) == 2,
      "run: python3 ui-kit/_fill_inventory.py")

# 3 ------------------------------------------------------------- dead icons --
dead = []
for page in GENERATED_PAGES:
    src = page.read_text(encoding="utf-8")
    have = set(re.findall(r'<symbol id="([\w-]+)"', src))
    for ref in set(re.findall(r'href="#(i-[\w-]+)"', src)):
        if ref not in have:
            dead.append("%s -> #%s" % (page.name, ref))
check("3 no dead icon reference", not dead, "%d: %s" % (len(dead), ", ".join(dead[:4])))

# 4 ------------------------------------------------------------ every path --
missing = []
ATTR = re.compile(r'(?:src|href)="([^"#][^"]*)"')
GENERATED = [p for p in GENERATED_PAGES if p.name not in ("kit.html", "shell.html")]
# The screens' index is checked here too. It is not a stand page, but it reaches
# across into ui-kit/ for the stand stylesheet, and that path is exactly the kind
# a directory move breaks silently.
GENERATED.append(ROOT / "ui-visual" / "overview.html")
# Text inside <code> or <pre> is a QUOTATION, not a reference. The vitrine quotes
# css by the file (every component page ends with its own source) and, since the
# documents render here, prose that quotes a stylesheet link or a url(). Scanning
# it reported a missing path that was a sentence about a path. Strip the quoted
# text first and ask the rest.
QUOTED = re.compile(r"<(code|pre)\b[^>]*>.*?</\1>", re.DOTALL)
for page in GENERATED:
    src = QUOTED.sub("", page.read_text(encoding="utf-8"))
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
    # the reporting script is the LAST thing in the body, but there is a script
    # in the head now too (the theme boot), so the search has to start at <body>.
    # Without the offset every slice came out empty and every specimen "matched".
    start = body.index("<body")
    body = body[start:body.index("<script", start)]
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
for path in SHEETS:
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    if re.search(r"\.(tk|ck)-[\w-]+", body):
        stand_in_comp.append(path.name)
check("6 components carry no stand class", not stand_in_comp, ", ".join(stand_in_comp))

# 7 --------------------------------------------------------------- em dash --
dash = [p.name for p in
        GENERATED_PAGES + list(KIT.glob("*.css"))
        + list(KIT.glob("*.py")) + list(KIT.glob("*.json")) + list((KIT / "docs").glob("*.md"))
        + list((KIT / "_verify").glob("*")) + SHEETS
        if p.is_file() and "\u2014" in p.read_text(encoding="utf-8", errors="ignore")]
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

# 9 ------------------------------------------------------- one source of css --
# What step 5 bought: a screen has no styles of its own. Not one inline <style>,
# not one stylesheet besides the system (the font <link>s are not css of ours).
# The moment a screen carries a rule again, the system has stopped being the
# source and the vitrine starts lying about what ships.
UV = ROOT / "ui-visual"
carries, wrong_link = [], []
for page in sorted(UV.glob("*.html")):
    src = page.read_text(encoding="utf-8")
    if "<style" in src:
        carries.append(page.name)
    sheets = [h for h in re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', src)
              if not h.startswith("http")]
    if sheets != ["../components/index.css"] and page.name != "overview.html":
        wrong_link.append("%s -> %s" % (page.name, ", ".join(sheets) or "none"))
check("9 no screen styles itself", not carries, "%d: %s" % (len(carries), ", ".join(carries[:4])))

# ...and a style attribute is a rule too. This is the hole step 7b found: gate 9
# asked about <style> and a second stylesheet, gate 12 looked inside components/,
# so 110 declarations lived for two stages in the one place neither looked. Three
# kinds of attribute are not styling and stay: a datum (a bar drawn to a width,
# an absolutely placed stop), the event photograph, and a value the page script
# writes at run time.
def is_styling(style):
    s = style.strip()
    if "'+" in s or "' +" in s:
        return False
    if re.fullmatch(r"width:\d+(\.\d+)?%;?", s) or s == "position:absolute":
        return False
    return "background-image:url" not in s


styled = []
for page in sorted(UV.glob("*.html")):
    hits = [s for s in re.findall(r'style="([^"]*)"', page.read_text(encoding="utf-8"))
            if is_styling(s)]
    if hits:
        styled.append("%s: %s" % (page.name, hits[0][:40]))
check("9 no screen styles an element", not styled, "%d: %s" % (len(styled), "; ".join(styled[:3])))
check("9 every screen links the system", not wrong_link,
      "%d: %s" % (len(wrong_link), "; ".join(wrong_link[:3])))
# Three stylesheets have been deleted across this stage: kit.css (the flat kit the
# system was read out of), and _theme.css with _theme-vault.css (the colour layer
# step 5 replaced). This check named only the first, and kit.css was already gone
# when it was written, so it could not fail and it guarded nothing. It names all
# three now, which is the only version of it that is a test.
DEAD_SHEETS = ("kit.css", "_theme.css", "_theme-vault.css")
gone_kit = ["%s -> %s" % (p.relative_to(ROOT), d) for p in
            list(ROOT.glob("*/*.html")) + list(ROOT.glob("*/*.css"))
            for d in DEAD_SHEETS
            if ('href="%s"' % d) in p.read_text(encoding="utf-8", errors="ignore")]
check("9 nothing loads a deleted sheet", not gone_kit, ", ".join(gone_kit))

# An empty photograph box is the other half of the rule above. The event picture
# is one of the three things allowed on the element, and until step 7c it was not
# there: components/ carried .grid > .card:nth-of-type(N) .thumb, so a card's
# photograph was decided by its POSITION in a grid. Moving it onto the element
# reached the pages that existed as files and missed the ones written by a
# generator, so the four category pages and two feed states shipped a 56px empty
# box for two steps. Nothing saw it: an absent picture passes a contrast sweep,
# an overflow sweep and a link check alike.
unphotographed = []
for page in sorted(UV.glob("*.html")):
    for m in re.finditer(r'<span class="thumb"([^>]*)>', page.read_text(encoding="utf-8")):
        if "background-image" not in m.group(1):
            unphotographed.append(page.name)
            break
check("9 every card has its photograph", not unphotographed,
      "%d: %s" % (len(unphotographed), ", ".join(unphotographed[:4])))

# 10 --------------------------------------------------- the product navigates --
# The colour pass shipped with every product link flattened to "#": the painted
# screens looked finished and went nowhere, and nothing here noticed for two
# stages. ui-visual/_relink.py is the repair, and it is also the test. It reads
# the target of each anchor out of the grey twin, so a dry run that wants to
# change something means a link is dead in colour that is live in grey.
relink = subprocess.run([sys.executable, str(ROOT / "ui-visual" / "_relink.py"), "--dry-run"],
                        cwd=ROOT, capture_output=True, text=True)
first = (relink.stdout or "\n").splitlines()[0]
check("10 painted product navigates", relink.returncode == 0 and " 0 links" in first,
      first.strip() or relink.stderr.strip()[:80])

# 11 -------------------------------------------------------- no orphan token --
# How the token file grew to 348 entries: it was READ out of the painted product,
# so every literal anyone had typed became a token, and nothing ever asked whether
# a token was read back. A declared value nobody reads is not a system, it is a
# transcript. ui-kit/tokens.html is not a consumer: it shows every token by
# definition, so counting it would make this gate always pass.
TOK = (COMP / "tokens.css").read_text(encoding="utf-8")
TOK_BODY = re.sub(r"/\*.*?\*/", "", TOK, flags=re.S)
declared = set(re.findall(r"(--[\w-]+)\s*:", TOK_BODY))
readers = [p for p in SHEETS if p.name not in ("tokens.css", "index.css")]
readers += [KIT / "_page.css", KIT / "_specimen.css"] + list(SPECS.glob("*.html"))
# A screen is a reader too. Most of them consume the system through a class, but
# a value can also be written straight into markup, and the multi-outcome chart
# does exactly that: its page script hands the five --series-* roles to the SVG
# so the browser resolves them live and the lines follow the theme. Counting
# only the stylesheets would call those five roles orphans and lose them.
readers += list(UVIS.glob("*.html"))
read = set(re.findall(r"var\((--[\w-]+)", TOK_BODY))   # a role reading a primitive
for p in readers:
    read |= set(re.findall(r"var\((--[\w-]+)", p.read_text(encoding="utf-8", errors="ignore")))
# The one exception, with its reason: DESIGN.md names bronze as part of the brand
# metal, so it is documented rather than dead. Anything else has to go or be wired.
RESERVED = set()   # --brass-800 (bronze) was the one exception; step 7 deleted it instead
orphan = sorted(declared - read - RESERVED)
check("11 no orphan token", not orphan, "%d: %s" % (len(orphan), ", ".join(orphan[:5])))
dangling = sorted({m for p in readers
                   for m in re.findall(r"var\((--[\w-]+)", p.read_text(encoding="utf-8", errors="ignore"))
                   if m not in declared})
check("11 no dangling var()", not dangling, "%d: %s" % (len(dangling), ", ".join(dangling[:5])))

# 12 ------------------------------------------------------ no raw scale value --
# A number typed into a rule is how a scale stops being one. Only the properties
# where a number IS a step are checked, and only up to 64px: above that it is a
# layout position (the 104px rail offset, the 118px inset behind a figure), which
# architecture.md already rules out of the scale.
SCALE_PROPS = {"padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
               "margin", "margin-top", "margin-right", "margin-bottom", "margin-left",
               "gap", "row-gap", "column-gap", "font-size", "border-radius", "line-height"}
# named, with the reason, the same way the orphan gate names its one exception
RAW_OK = {("chart.css", "font-size")}   # svg text inside a scaled viewBox: not a screen px
raw = []
for path in SHEETS:
    if path.name in ("tokens.css", "index.css"):
        continue
    body = re.sub(r'url\("[^"]*"\)', "URL", re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"),
                                                   flags=re.S))
    for m in re.finditer(r"(?:^|[;{])\s*([a-z-]+)\s*:\s*([^;{}]*)", body):
        prop, val = m.group(1), m.group(2)
        if prop not in SCALE_PROPS or (path.name, prop) in RAW_OK:
            continue
        if prop == "line-height":
            if re.fullmatch(r"[\d.]+", val.strip()) and float(val.strip()) != 0:
                raw.append("%s %s:%s" % (path.name, prop, val.strip()))
            continue
        for lit in re.findall(r"(?<![\w.-])(\d+(?:\.\d+)?)px", val):
            if float(lit) <= 64:
                raw.append("%s %s:%s" % (path.name, prop, val.strip()[:40]))
                break
check("12 no raw scale value", not raw, "%d: %s" % (len(raw), "; ".join(raw[:3])))

# A z-index is a scale too, and it was the last one written as loose numbers:
# 0 1 2 3 4 5 6 10 40 49 50 60 199 200 201 across twelve files, three of them
# doing one job. The order lives in tokens.css under --z-*, and nowhere else.
zraw = ["%s %s" % (path.name, m.group(0))
        for path in SHEETS if path.name != "tokens.css"
        for m in re.finditer(r"z-index:\s*-?\d+", path.read_text(encoding="utf-8"))]
check("12 the stacking order is named", not zraw, "%d: %s" % (len(zraw), "; ".join(zraw[:3])))

# The migration is its own test, the way _relink.py is: if a consumer still reads
# a name the scales moved, a dry run wants to change something.
rescale = subprocess.run([sys.executable, str(KIT / "_rescale.py"), "--dry-run"],
                         cwd=ROOT, capture_output=True, text=True)
line = (rescale.stdout or "\n").splitlines()[0]
check("12 every consumer rescaled", rescale.returncode == 0 and " 0 rewrites" in line,
      line.strip() or rescale.stderr.strip()[:80])

# 14 ----------------------------------------------- no selector without markup --
# The other half of gate 11: a token nobody reads is a transcript, and so is a
# rule nobody can match. 21 of them were still here at step 7b, all inherited
# from grey-box css that the extraction copied along with everything else.
#
# MARKUP IS NOT ONLY IN .html FILES, which is the mistake the first cut of this
# gate made and the user caught by eye: the vitrine's own side panel is built at
# run time by _nav.js out of a template string, so `.sidebar-divider` looked dead
# to a scan that only read HTML, and deleting it turned every group heading in
# the panel into unstyled text. A class in a template string is markup. So the
# .js files are read too, and a class toggled by script counts as carried
# (classList add/remove/toggle).
#
# MARKUP THIS FILE CAN REACH, which is not the same set (step 7e). wireframes/
# was in this list and does not belong: the grey tree carries its own inline
# grey-box css, it never links index.css, and no rule in components/ has ever
# applied to it. Counting it as markup kept four rules alive that nothing could
# match: .backdrop, .sheet and .grab (the grey tree's bottom-sheet frame, where
# the paint uses a centred dialog.app-dialog) and .wf-screen > a.planned::after
# (the grey screen drawer, 2392 uses there and none here). A class carried only
# by the tree a stylesheet cannot see is a class it does not have.
carried = set()
for page in (list(UV.glob("*.html")) + list(KIT.glob("*.html")) + list(SPECS.glob("*.html"))
             + list(UV.glob("*.js")) + list(KIT.glob("*.js"))):
    src = page.read_text(encoding="utf-8", errors="ignore")
    for group in re.findall(r'class=\\?["\']([^"\'\\]*)', src):
        carried.update(group.split())
    for call in re.findall(r"classList\.(?:add|remove|toggle)\(([^)]*)\)", src):
        carried.update(re.findall(r"['\"]([\w-]+)['\"]", call))

unmatched = []
for path in SHEETS:
    if path.name in ("tokens.css", "index.css"):
        continue
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    for block_sel in re.findall(r"([^{}]+)\{", body):
        block_sel = block_sel.strip()
        if block_sel.startswith("@") or not block_sel:
            continue
        for sel in _levels.split_top(block_sel):
            classes = re.findall(r"\.([\w-]+)", sel)
            if classes and not any(c in carried for c in classes):
                unmatched.append("%s %s" % (path.name, " ".join(sel.split())[:40]))
check("14 no selector without markup", not unmatched,
      "%d: %s" % (len(unmatched), "; ".join(unmatched[:3])))

# 13 ------------------------------------------------- colour through a role --
# architecture.md states it as a rule and nothing enforced it, so it drifted in
# six places at once and only the light theme found them. A primitive here is
# any section-1 token whose value is a colour or a material (a gradient, a noise,
# a data URI mark): those are what a theme moves. Geometry, type and motion
# primitives are read directly on purpose and are not in this set.
tok = (COMP / "tokens.css").read_text(encoding="utf-8")
prim_src = tok[tok.index("1. PRIMITIVE"):tok.index("2. SEMANTIC")]
COLOURISH = re.compile(r"#[0-9a-fA-F]{3,8}|rgba?\(|url\(|gradient\(")
colour_prims = {m.group(1) for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;]+);", prim_src)
                if COLOURISH.search(m.group(2))}
leaks = []
for path in SHEETS:
    if path.name == "tokens.css":
        continue
    body = path.read_text(encoding="utf-8")
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.DOTALL)   # the Reads: header is a list, not a read
    for name in sorted(set(re.findall(r"var\((--[\w-]+)\)", body))):
        if name in colour_prims:
            leaks.append("%s reads %s" % (path.name, name))
check("13 colour goes through a role", not leaks,
      "%d: %s" % (len(leaks), "; ".join(leaks[:3])))

# The switch itself has to survive a rebuild, in both trees, or the proof is only
# true of whichever tree was regenerated last.
boot_missing = [p.name for p in sorted(UVIS.glob("*.html"))
                if "<script id=\"uvTheme\">" not in p.read_text(encoding="utf-8")]
btn_missing = [p.name for p in sorted(UVIS.glob("*.html"))
               if 'class="theme-switch"' not in p.read_text(encoding="utf-8")]
check("13 every screen can switch", not boot_missing and not btn_missing,
      "%d without boot, %d without button" % (len(boot_missing), len(btn_missing)))

# A specimen is a page of its own, so it does NOT inherit the attribute from the
# vitrine that frames it. This is how the first cut of the theme shipped: every
# stand page went pale and every frame inside it stayed graphite. The frames are
# where the system is actually shown, so a specimen without the boot is the
# whole vitrine lying about the theme.
framed = list(SPECS.glob("*.html")) + [KIT / "selftest.html"]
frame_missing = [p.name for p in sorted(framed)
                 if "<script id=\"uvTheme\">" not in p.read_text(encoding="utf-8")]
check("13 every frame follows", not frame_missing,
      "%d of %d framed pages without boot: %s"
      % (len(frame_missing), len(framed), ", ".join(frame_missing[:3])))

# 12 ------------------------------------------- a distance is not a measurement --
# The other half of "no raw scale value". tokens.css says a --space-* step is the
# distance BETWEEN things and that the size OF a thing is --size-*, --control-* or
# --icon-*; the rule was written in step 6 and fifty-seven declarations broke it,
# because the measurement scale shipped with two steps and the product needed ten.
# A var() is invisible to the raw-value check, so this is the only place it shows.
MEASURE = re.compile(r"(?<![\w-])(width|height|min-width|min-height|max-width|max-height"
                     r"|flex|flex-basis)\s*:[^;{}]*?var\(--space-\d+\)")
space_as_size = []
for path in SHEETS:
    if path.stem == "tokens":
        continue
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if MEASURE.search(line):
            space_as_size.append("%s:%d" % (path.name, i))
check("12 a distance is not a size", not space_as_size,
      "%d: %s" % (len(space_as_size), ", ".join(space_as_size[:4])))

# 16 ------------------------------------------------------- the css parses --
# Added because this pass shipped a broken declaration and no gate saw it. A note
# was appended to a token WITHOUT its comment markers, which put bare prose inside
# the :root block; the browser dropped every declaration after it, and the whole
# NO side of the outcome palette rendered transparent on twenty-eight screens. A
# snapshot at five widths caught it. That is the right last line of defence and
# the wrong first one, because it costs two browser runs and this costs nothing.
DECL = re.compile(r"^\s*(?:--)?[-a-zA-Z*][\w-]*\s*:")
parse_bad = []
for path in SHEETS:
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    for block in re.finditer(r"\{([^{}]*)\}", body):
        for part in block.group(1).split(";"):
            if part.strip() and not DECL.match(part):
                parse_bad.append("%s: %s" % (path.name, " ".join(part.split())[:40]))
check("16 every declaration parses", not parse_bad,
      "%d: %s" % (len(parse_bad), "; ".join(parse_bad[:3])))

# 15 -------------------------------------------------------------- headings --
# One h1 per screen and no skipped level, in BOTH trees. Structure is owned by
# wireframes/ and the colour copy follows, so a check that reads only the painted
# tree can pass while the thing it is a copy OF is wrong: that is exactly how the
# grey tree kept an h1-to-h3 jump on 46 pages after step 7b fixed the paint.
# The two Event Detail loading skeletons carry no h1 on purpose. A skeleton has no
# question yet, and inventing a heading is inventing copy.
NO_H1 = {"event-detail-loading.html", "event-detail-logged-out-loading.html"}
head_bad = []
for tree in ("wireframes", "ui-visual"):
    for page in sorted((ROOT / tree).glob("*.html")):
        src = page.read_text(encoding="utf-8")
        n1 = len(re.findall(r"<h1[ >]", src))
        want = 0 if page.name in NO_H1 else 1
        if n1 != want:
            head_bad.append("%s/%s h1=%d" % (tree, page.name, n1))
        prev = 0
        for lvl in [int(m.group(1)) for m in re.finditer(r"<h([1-6])[ >]", src)]:
            if prev and lvl > prev + 1:
                head_bad.append("%s/%s h%d after h%d" % (tree, page.name, lvl, prev))
                break
            prev = lvl
check("15 one h1, no skipped level", not head_bad,
      "%d: %s" % (len(head_bad), ", ".join(head_bad[:4])))

# 17 --------------------------------------------------------- icon coverage --
# Gate 3 asks whether a reference points at a symbol that exists. Nothing asked
# the other direction: whether a mark standing on a screen is shown anywhere a
# person could find it. Fourteen were not, including the chevron, which at 176
# uses is the most drawn icon in the product, and the three sign-in brand marks.
# The section built in step 7c to end "the vitrine documents one of two icon
# mechanisms" had collected its shapes with a regex that wanted class="ic" as the
# first attribute, so it was itself showing part of one mechanism.
#
# An <svg> on a screen is either a MARK or a drawing of DATA. There are two
# drawings; everything else has to be on the sheet.
DATA_SVG = {"chart-svg", "hf-graph"}
SVG_RE = re.compile(r'<svg\b[^>]*?class="([^"]*)"[^>]*>(.*?)</svg>', re.S)


def marks(text):
    """every distinct shape drawn by an icon in this document"""
    out = set()
    for m in SVG_RE.finditer(text):
        if set(m.group(1).split()) & DATA_SVG or "<use" in m.group(2):
            continue
        for d in re.findall(r'\sd="([^"]+)"', m.group(2)):
            out.add(" ".join(d.split()))
        for s in re.findall(r"<(?:circle|rect|line|polyline|ellipse)[^>]*/>", m.group(2)):
            out.add(" ".join(s.split()))
    return out


sheet = marks((KIT / "icons.html").read_text(encoding="utf-8"))
unshown = {}
for page in sorted((ROOT / "ui-visual").glob("*.html")):
    for shape in marks(page.read_text(encoding="utf-8")) - sheet:
        unshown.setdefault(shape, page.name)
check("17 every mark is on the sheet", not unshown,
      "%d: %s" % (len(unshown), ", ".join("%s (%s)" % (s[:22], p)
                                          for s, p in list(unshown.items())[:3])))

# 18 ------------------------------------------------------- the two trees ---
# The rule has been in CLAUDE.md since Stage 08: wireframes/ owns structure and
# copy, ui-visual/ owns the visual layer. Nothing enforced it, and Stage 08 broke
# it quietly by REDESIGNING the Event Detail while painting it: an AMM panel, a
# rebuilt chart, a rules tab split, a real <input> where the grey tree had a span
# pretending to be a field. 55 of 72 <main> elements differed and the tree that
# owns structure was the one that was wrong. A rule with no gate behind it is a
# preference.
#
# Three differences are the LAYER BOUNDARY and are declared, not erased:
#   - the plate wrappers .cat-layout / .cat-main / .feed-inner exist to draw a
#     stone plate, so they are paint and are unwrapped before comparing
#   - the icon mechanism: colour draws <use href="#id">, grey draws raw paths
#   - the photograph: <img> and background-image are paint, the box stays
#
# STEP 7E: THE OTHER THREE REGIONS. This compared <main> and nothing else, so the
# header, the bottom nav and the footer were the one place two trees could drift
# with every gate green, and they had: a whole category strip in the sticky
# header on 68 painted screens and 0 grey ones, a rewritten footer trust block on
# 55, aria-current="page" on the Events slot of all 76 painted screens whatever
# screen it was, and a logged-in header over a logged-out bottom nav on ten. All
# four regions are compared now.
PLATE = {"cat-layout", "cat-main", "feed-inner"}
# The FIFTH boundary. A wireframe is obliged to mark a destination nobody has
# built; a product that shows a user the word TBD is showing them the
# bookkeeping. 14 span.tbd and one p.placeholder-line stand in every grey footer
# and in none of the painted ones, and that is the two layers being right rather
# than one of them being behind.
GREY_ONLY = {"tbd", "placeholder-line"}
# A fourth boundary, and the one worth naming: a wireframe DRAWS its data and a
# product COMPUTES it. The painted chart ships an empty x-axis and fills it from
# a script on load; the wireframe types the labels in, because a wireframe with a
# blank axis shows nothing about the axis. Same element, same place, contents
# owned by different layers, so the contents are not compared.
DATA_HELD = {"ed-xaxis", "ed-legend"}
SELFCLOSE = {"br", "img", "input", "use", "path", "circle", "meta", "link",
             "polyline", "source", "rect", "line", "hr", "ellipse", "stop"}
TAG = re.compile(r"<(/?)([a-z0-9]+)([^>]*?)(/?)>")


def shape(html):
    """tag.firstclass for every element, minus the four declared exceptions."""
    out, stack, blind = [], [], 0
    for m in TAG.finditer(html):
        close, tag, attrs, self = m.groups()
        void = bool(self) or tag in SELFCLOSE
        cl = re.search(r'class="([^"]*)"', attrs)
        classes = cl.group(1).split() if cl else []
        if close:
            if blind:
                blind -= 1
                if not blind:
                    continue
            if stack and stack.pop():
                continue
            if blind:
                continue
            out.append("/" + tag)
            continue
        if blind:
            if not void:
                blind += 1
            continue
        drop = (tag == "div" and bool(set(classes) & PLATE)) \
            or bool(set(classes) & GREY_ONLY)
        if tag in ("use", "path", "circle", "line", "polyline", "rect", "ellipse", "img"):
            continue                       # icon mechanism and photography
        if not void:
            stack.append(drop)
        if not drop:
            out.append(tag + ("." + classes[0] if classes else ""))
        if set(classes) & DATA_HELD and not void:
            blind = 1
            stack.pop()
            out.append("/" + tag)
    return out


REGIONS = {
    "main": re.compile(r"<main\b.*?</main>", re.S),
    "header": re.compile(r"<header\b.*?</header>", re.S),
    "nav": re.compile(r'<nav[^>]*class="[^"]*bottom-nav[^"]*"[^>]*>.*?</nav>', re.S),
    "footer": re.compile(r"<footer\b.*?</footer>", re.S),
}
# The SIXTH boundary, and the only one that is checked instead of skipped.
# Convention 5 in wireframes/_conventions.md has said since the wireframes were
# built that the invoked screens "render as modal or bottom-sheet overlay
# content, not as a full-page layout". The paint puts a whole feed behind the
# sheet, because a scrim has to be a scrim over something. Both trees are right
# for their own layer, so their page frames are not compared. What IS compared is
# the sheet body, where the grey tree had a <span> pretending to be the amount
# field, and the rule itself: grey carries no chrome on these and the paint
# carries all of it, so neither side can drift into the other by accident.
OVERLAY = re.compile(r"^(deposit|sign-in|win|loss)(-|\.html$)")
OWN_DIALOG = re.compile(r'<dialog[^>]*id="outcomeDialog".*?</dialog>', re.S)


def region(html, tag, cls=None):
    """The outer html of the first <tag> with that class, by counting depth.

       A regex cannot do this and the first cut of the sheet-body check proved
       it: `.*?</div>\\s*</section>` anchored on a closing tag only the grey tree
       has, so it matched there, missed in the paint, and the fallback ran greedy
       past the end of the sheet. Seventeen screens then reported drift that was
       the checker's own."""
    pat = r"<%s\b[^>]*?>" % tag if cls is None else \
        r'<%s\b[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls)
    m = re.search(pat, html)
    if not m:
        return None
    depth, i = 0, m.start()
    for t in re.finditer(r"<(/?)(%s)\b[^>]*?(/?)>" % tag, html[i:]):
        if t.group(1):
            depth -= 1
            if depth == 0:
                return html[i:i + t.end()]
        elif not t.group(3):
            depth += 1
    return None

# STEP 8: A PAIR THAT DOES NOT EXIST IS NOT A PAIR THAT AGREES. This gate pairs
# the trees by FILENAME and skipped anything unpaired in silence, so a family
# that does not share filenames was never compared: a category page is
# politics.html in grey and event-feed-politics.html in colour, and behind that
# rename sat 32 grey screens against 4 painted ones, drifting for two stages with
# every gate green. Zero drift out of zero pairs reads exactly like zero drift
# out of all of them.
#
# So the map is read from _twins.py (one copy, all tools), and the coverage is a
# check of its own: a screen in either tree with no twin has to be a declared
# exception, not a silent skip.
sys.path.insert(0, str(ROOT))
import _twins                                                   # noqa: E402
# TWO KINDS OF EXCEPTION, AND THEY ARE NOT ONE LIST. A painted page with no grey
# twin is either NOT A SCREEN (overview.html, the index of the tree) or a screen
# the SYSTEM BUILT, which is the opposite fact: it is a product page and the grey
# original is missing because the blocks, the copy and the components were all
# decided before it was drawn. Both are declared in _twins.py with their own
# reason, and they are reported apart so that a shared bucket never turns the
# second into "another service file". The set below is only the union used to
# find pages that are in NEITHER.
NO_TWIN = set(_twins.NOT_A_SCREEN) | set(_twins.SYSTEM_BUILT)
painted = {p.name for p in (ROOT / "ui-visual").glob("*.html")}
greys = {p.name for p in (ROOT / "wireframes").glob("*.html")}
lonely = sorted([n for n in painted - NO_TWIN if _twins.grey_of(n) not in greys] +
                [n for n in greys if _twins.painted_of(n) not in painted])
check("18 every screen has a twin", not lonely,
      "%d: %s" % (len(lonely), ", ".join(lonely[:5])))
# The other direction, the same shape every declaration here has: an entry that
# names a file which does not exist is a stale exemption, and a stale exemption
# is a hole that reads as a decision.
ghost = sorted(n for n in NO_TWIN if n not in painted)
check("18 no exemption without a page", not ghost,
      "%d: %s" % (len(ghost), ", ".join(ghost[:4])))
check("18 built from the system, declared", True,
      "%d not a screen, %d system-built: %s" % (
          len(_twins.NOT_A_SCREEN), len(_twins.SYSTEM_BUILT),
          ", ".join(sorted(_twins.SYSTEM_BUILT))))

drift, frame = [], []
for page in sorted((ROOT / "ui-visual").glob("*.html")):
    twin = ROOT / "wireframes" / _twins.grey_of(page.name)
    if not twin.exists():
        continue
    paint, grey = page.read_text(encoding="utf-8"), twin.read_text(encoding="utf-8")
    if OVERLAY.match(page.name):
        # The rule, not the shape.
        for name, rx in REGIONS.items():
            if name == "main":
                continue
            if rx.search(grey) or not rx.search(paint):
                frame.append("%s %s" % (page.name, name))
        own = OWN_DIALOG.search(paint)
        a = region(own.group(0), "div", "sheet-body") if own else None
        b = region(region(grey, "section", "sheet") or "", "div", "sheet-body")
        if a and b and shape(a) != shape(b):
            drift.append("%s sheet-body" % page.name)
        continue
    for name, rx in REGIONS.items():
        a, b = rx.search(paint), rx.search(grey)
        if not a or not b:
            if bool(a) != bool(b):
                drift.append("%s %s (one side only)" % (page.name, name))
            continue
        if shape(a.group(0)) != shape(b.group(0)):
            drift.append("%s %s" % (page.name, name))
check("18 the two trees agree", not drift and not frame,
      "%d: %s" % (len(drift) + len(frame), ", ".join((drift + frame)[:4])))

# 19 --------------------------------------------------- one dialog, one copy --
# Gate 18 compares a screen with its GREY TWIN, and never with its own second
# copy in the same tree. Sign In and Deposit each have one: the shared <dialog>
# embedded on all 76 screens, and the standalone page that IS that dialog. Stage
# 08 painted the shared copy into a real component and left the standalone on
# the markup the grey generator wrote, and for two stages nothing looked: the
# shared dialog carries the real Google, X and Apple marks while the page a
# person actually opens carries the wireframe placeholders, the one standing in
# for Google being a circle with a plus in it.
#
# THREE THINGS DIFFER BY CONTEXT AND ARE NOT DRIFT, which is why this compares
# the BODY and not the dialog:
#   the head. A dialog is opened over a page, so it heads with <h2> and closes
#       with data-close-dialog; a page heads with <h1> (gate 15) and closes with
#       a link back to where it came from.
#   the wiring. In a dialog a provider button opens the next sheet over the page
#       you are already on; on a page it navigates, so each control is wrapped in
#       an <a>. The wrapper is dropped before comparing; what it wraps is not.
#   the state screens. sign-in-error and the rest are states, not copies, so only
#       the BASE page of each family is compared.
#
# And a mark is not a shape, which shape() cannot see: it drops <path> and
# <circle> because the two trees draw an icon by different mechanisms. So the
# provider marks are checked by name, wherever a provider button stands.
PAIRS = {"signinDialog": "sign-in.html", "depositDialog": "deposit.html"}
UNWRAP_A = re.compile(r"</?a\b[^>]*>")

forked = []
for did, page in PAIRS.items():
    for tree in ("ui-visual", "wireframes"):
        home = ROOT / tree
        base = home / page
        if not base.exists():
            continue
        anchor = next((p for p in sorted(home.glob("*.html"))
                       if re.search(r'<dialog[^>]*id="%s"' % did, p.read_text(encoding="utf-8"))), None)
        if anchor is None:
            continue
        m = re.search(r'<dialog[^>]*id="%s"' % did, anchor.read_text(encoding="utf-8"))
        shared = region(anchor.read_text(encoding="utf-8")[m.start():], "dialog")
        html = base.read_text(encoding="utf-8")
        # By id, never "the first dialog": the standalone page embeds the shared
        # sign-in, deposit and how-it-works dialogs BEFORE its own, so the first
        # one in the document is the sign-in sheet on every page of both trees.
        # The first cut of this gate asked for the first dialog and reported a
        # fork that was its own.
        om = re.search(r'<dialog[^>]*id="outcomeDialog"', html)
        own = region(html[om.start():], "dialog") if om else \
            region(html, "section", "sheet")
        a = region(shared or "", "div", "sheet-body")
        b = region(own or "", "div", "sheet-body")
        if not a or not b:
            forked.append("%s/%s no body" % (tree, page))
            continue
        if shape(UNWRAP_A.sub("", a)) != shape(UNWRAP_A.sub("", b)):
            forked.append("%s/%s body" % (tree, page))

# THE SKIN, which the body comparison above cannot see. All 17 standalone
# overlay pages were written from one template and all 17 carried
# `app-case app-dialog outcome-dialog <family>-dialog`, so the sign-in page a
# person opens wore the RESULT skin: dialog.css splits the head on
# .outcome-dialog and only :not(.outcome-dialog) gets the brass-lit plate. The
# shared sheet on the other 75 screens had the lit head and the page did not.
#
# A gate that compares the body certifies the body. This compares the class list,
# and it asks ui-visual/_unify_dialogs.py which family a page belongs to rather
# than keeping a second list of the same fact.
sys.path.insert(0, str(UVIS))
import _unify_dialogs as ud                                          # noqa: E402
canon = (UVIS / "event-feed.html").read_text(encoding="utf-8")
skin_of = {}
for fam, (did, _) in ud.FAMILIES.items():
    m = re.search(r'<dialog\b[^>]*id="%s"[^>]*>' % did, canon)
    skin_of[fam] = "app-case " + re.search(r'class="([^"]*)"', m.group(0)).group(1)
for pagefile in sorted((ROOT / "ui-visual").glob("*.html")):
    fam = ud.family_of(pagefile.name)
    if not fam:
        continue
    m = re.search(r'<dialog\b[^>]*id="outcomeDialog"[^>]*>',
                  pagefile.read_text(encoding="utf-8"))
    if not m:
        continue
    got = re.search(r'class="([^"]*)"', m.group(0)).group(1)
    if got != skin_of[fam]:
        forked.append("%s skin (%s)" % (pagefile.name, got))

PROVIDERS = [("Google", "prov-google"), ("Apple", "prov-apple"), ("with X", "prov-x")]
for pagefile in sorted((ROOT / "ui-visual").glob("*.html")):
    html = pagefile.read_text(encoding="utf-8")
    for m in re.finditer(r'<button\b[^>]*class="[^"]*\bprovider-btn\b[^"]*"[^>]*>', html):
        btn = region(html[m.start():], "button") or ""
        if "<svg" not in btn:
            continue                      # a control with no mark is not a fork
        label = re.sub(r"<[^>]+>", " ", btn)
        want = next((cls for text, cls in PROVIDERS if text in label), None)
        if want and want not in btn:
            forked.append("%s %s" % (pagefile.name, want))
check("19 one dialog, one copy", not forked,
      "%d: %s" % (len(forked), ", ".join(forked[:4])))

# 20 ------------------------------------------------------------ the fonts --
# Every screen used to call fonts.googleapis.com from its head, which sends a
# visitor's IP to a third party before the cookie banner this product ships has
# asked them anything, and a consent banner over a page that has already made
# the call is not a consent banner. Step 7b deleted a second copy of the same
# URL out of base.css and wrote down that where a font comes from is a decision;
# step 8 made it. The families are in assets/fonts/ and declared once in
# components/fonts.css.
#
# Three checks, because the defect can come back three ways: a page can re-add
# the tag, a GENERATOR can re-add it to every page it writes (five of them had
# it in a template), and an @font-face can name a file nobody committed.
# A MENTION IS NOT A CALL. The first cut searched the whole text, which is right
# for a page and wrong for a document: ui-kit/architecture.html renders the
# section that explains why the host was dropped, so naming it failed the gate
# that exists because of it. The question is whether a URL is REQUESTED, so it is
# asked of the places a request comes from: a src/href attribute and an @import.
FONT_HOST = re.compile(r'(?:src|href)="[^"]*fonts\.(?:googleapis|gstatic)\.com'
                       r'|@import[^;]*fonts\.(?:googleapis|gstatic)\.com')
LIVE = [p for tree in ("ui-visual", "ui-kit", "concept", "components", "wireframes")
        for p in (ROOT / tree).rglob("*")
        if p.suffix in (".html", ".css", ".py") and "old" not in p.parts
        and p.name != "fonts.css" and p.name != "_check_kit.py"]
calls = [str(p.relative_to(ROOT)) for p in LIVE
         if FONT_HOST.search(p.read_text(encoding="utf-8"))]
check("20 no external font host", not calls,
      "%d: %s" % (len(calls), ", ".join(sorted(calls)[:4])))

faces = (COMP / "fonts.css").read_text(encoding="utf-8")
missing = [u for u in re.findall(r"url\(([^)]+)\)", faces)
           if not (COMP / u).exists()]
check("20 every face is committed", not missing,
      "%d: %s" % (len(missing), ", ".join(missing[:3])))

# A screen renders the product's type, so it has to reach the faces: through the
# system stylesheet, which imports them first, or by naming fonts.css itself.
unfaced = []
for tree in ("ui-visual", "ui-kit"):
    for page in sorted((ROOT / tree).rglob("*.html")):
        if "old" in page.parts:
            continue
        src = page.read_text(encoding="utf-8")
        if "components/index.css" not in src and "components/fonts.css" not in src:
            unfaced.append(str(page.relative_to(ROOT)))
check("20 every page reaches the faces", not unfaced,
      "%d: %s" % (len(unfaced), ", ".join(unfaced[:3])))

# 21 ------------------------------------------------------- the documents --
# Stage 09 was the only stage whose reasoning existed as markdown and nothing
# else, while thirty-nine component pages linked docs/coverage.md: a href into a
# file the browser downloads rather than draws. ui-kit/_gen_docs.py renders the
# four, and this is what keeps the render current, because a hand-checked copy of
# a document that changes every step is stale by the next one.
#
# The comparison is a re-render in memory, not a timestamp: a file can be newer
# than its source and still be wrong.
sys.path.insert(0, str(KIT))
import _gen_docs                                                     # noqa: E402
stale = []
for slug, _, _ in _gen_docs.PAGES:
    page = KIT / (slug + ".html")
    if not page.exists():
        stale.append(slug + ".html missing")
    elif page.read_text(encoding="utf-8") != _gen_docs.render(slug):
        stale.append(slug + ".html stale")
stale += ["%s.md has no row in _gen_docs.PAGES" % s
          for s in sorted({p.stem for p in (KIT / "docs").glob("*.md")}
                          - {slug for slug, _, _ in _gen_docs.PAGES})]
check("21 every document has a page", not stale, "%d: %s" % (len(stale), ", ".join(stale[:3])))

RAW_MD = re.compile(r'href="[^"]*\.md"')
raw = [str(p.relative_to(ROOT))
       for tree in ("ui-kit", "ui-visual")
       for p in sorted((ROOT / tree).rglob("*.html"))
       if "old" not in p.parts and RAW_MD.search(p.read_text(encoding="utf-8"))]
check("21 no link into a raw .md", not raw, "%d: %s" % (len(raw), ", ".join(raw[:3])))

# 22 ------------------------------------------- the panel says where you are --
# The side panel is the one piece of chrome gate 1 masks, on the argument that it
# is not product. So it was the one piece nothing read, and it had been lying on
# forty screens: every category page and every feed state said "Event Feed ->
# success", which is a different file.
#
# The cause is the shape this repo keeps meeting. _apply_theme.py and
# _gen_category.py build a screen by starting from the finished Event Feed and
# swapping the regions that differ, and the panel is not one of those regions, so
# a new screen arrives carrying the SHELL'S idea of where it is. That is correct
# right up to the moment nobody re-runs _resync_sidebar.py, and after step 8
# nobody did.
#
# Two checks, because they can fail apart. The first is the claim a person can
# see: the row marked "you are here" is this page. The second is the claim about
# the tooling: the panel on disk is what the generator would write today, so a
# family added to FAMILIES and never re-rendered fails here rather than in a
# screenshot. It is a re-render in memory, the way gate 21 reads a document.
sys.path.insert(0, str(UVIS))
import _resync_sidebar                                               # noqa: E402

ASIDE = re.compile(r'<aside class="sidebar" id="rmSidebar">.*?</aside>', re.DOTALL)
ACTIVE_LEAF = re.compile(r'<a href="([^"]+)" class="sidebar-sub-link active"')

lost = []
for page in sorted(UVIS.glob("*.html")):
    src = page.read_text(encoding="utf-8")
    m = ASIDE.search(src)
    if not m:
        continue
    marked = ACTIVE_LEAF.findall(m.group(0))
    if page.name == _resync_sidebar.INDEX_FILE:
        # the index is its own row above the families, so it marks no leaf
        want = []
    else:
        want = [page.name]
    if marked != want:
        lost.append("%s marks %s" % (page.name, ", ".join(marked) or "nothing"))
check("22 every screen marks its own file", not lost,
      "%d: %s" % (len(lost), "; ".join(lost[:3])))

drifted = [f for f in sorted(_resync_sidebar.STATE_FILES | {_resync_sidebar.INDEX_FILE})
           if _resync_sidebar.process(f, write=False) == "updated"]
check("22 the screen panel is at its fixed point", not drifted,
      "%d: %s" % (len(drifted), ", ".join(drifted[:3])))

# The vitrine's panel is rendered at run time, so it cannot drift the same way:
# what it can do is mark a row that is not this page, because the page names
# itself in data-kit-page and _nav.js matches that against the registry. A page
# whose attribute is missing, misspelled or left over from the file it was copied
# from marks nothing, or marks a sibling.
#
# A page outside the registry is not a defect by itself: shell.html composes the
# specimens and kit.html is frozen provenance, and neither is a component. What
# would be a defect is a page outside the tree that nothing links, so the second
# half asks the note, which is the only other way in.
NAVJS = (KIT / "_nav.js").read_text(encoding="utf-8")
REG = dict(re.findall(r'"?name"?:\s*"([^"]+)",\s*"?file"?:\s*"([^"]+)"', NAVJS))
REG["overview"] = "overview.html"
NOTED = set(re.findall(r'href="([^"]+)"', re.search(r'sidebar-note.*', NAVJS).group(0)))

misnamed, unreachable = [], []
for page in sorted(KIT.glob("*.html")):
    src = page.read_text(encoding="utf-8")
    if "data-kit-nav" not in src:
        continue
    m = re.search(r'<body[^>]*\bdata-kit-page="([^"]*)"', src)
    name = m.group(1) if m else ""
    if name in REG:
        if REG[name] != page.name:
            misnamed.append("%s says %s, which is %s" % (page.name, name, REG[name]))
    elif page.name not in NOTED:
        unreachable.append("%s (says %s)" % (page.name, name or "nothing"))
check("22 every stand page names itself", not misnamed,
      "%d: %s" % (len(misnamed), "; ".join(misnamed[:3])))
check("22 a page off the tree is still linked", not unreachable,
      "%d: %s" % (len(unreachable), "; ".join(unreachable[:3])))

# 23 ------------------------------------------------------ a part comes first --
# The cascade decides which of two rules of equal specificity wins, so the order
# of the @imports is a rule and not a formatting choice. A part is imported
# BEFORE the whole that holds it, or the smaller thing silently overrides the
# bigger one: an odds bar would restyle every card that contains it, and a card
# could not restyle its own odds bar.
#
# It had never been asked. The order was the order the rules had been layered in
# inside the flat kit the system was read out of, and it put TWENTY FIVE wholes
# ahead of their parts, header before button and card before both of the controls
# it holds. Nothing rendered wrong, because no two files write the same selector
# any more (step 7b deleted those), which is exactly why no sweep could see it: a
# cascade defect is invisible until the day someone adds the rule that collides.
#
# The order is computed in _levels.py from what each component CONTAINS, read out
# of the specimen DOM. This gate re-derives it and compares, the way gate 21 does
# with the documents: a file can be newer than its source and still be wrong.
sys.path.insert(0, str(KIT))
from _levels import ORDER as LEVEL_ORDER, order_problems, SUBJECTS as LEVEL_SUBJECTS  # noqa: E402
from _levels import STATIC as LEVEL_STATIC                            # noqa: E402
from _levels import PATTERNS as LEVEL_PATTERNS                        # noqa: E402

cascade = [ln.split('"')[1][:-4] for ln in
           (COMP / "index.css").read_text(encoding="utf-8").splitlines()
           if ln.startswith("@import")]
# A PATTERN IS IMPORTED OR IT IS NOT IN THE SYSTEM. It has no specimen, no stand
# page and no level, so gate 2 and gate 24 cannot notice it going missing, and a
# file in components/patterns/ that index.css never loads would be exactly the
# artifact without a reader this whole stage is written against. The one place it
# CAN be caught is here, where the cascade is read.
missing = sorted((set(LEVEL_SUBJECTS) | {"tokens"} | set(LEVEL_PATTERNS)) - set(cascade))
check("23 index.css imports them all", not missing, "%d: %s" % (len(missing), ", ".join(missing)))
wrong = order_problems(cascade)
check("23 a part is imported first", not wrong, "%d: %s" % (
    len(wrong), "; ".join("%s before %s" % (w, p) for w, p in wrong[:3])))
check("23 the order is the computed one", cascade == LEVEL_ORDER,
      "run: python3 ui-kit/_levels.py --order")
# AND A PATTERN CARRIES NO COLOUR, which is the rule that keeps it a pattern.
# A composition says where things go: grid, order, gap, width, sticky. The moment
# it says what something LOOKS like it has become a component with no page, no
# specimen and no states, and the next screen that needs the same arrangement in
# a different skin has to fork it. So the paint stays with whatever owns the
# surface, and the arrangement comes here. Written as a property list rather than
# a value scan because `border:1px solid var(--x)` hides a colour inside a
# shorthand, and because a pattern has no business drawing an edge either.
PAINT_PROP = re.compile(r"^(background|color|border(?!-radius)|box-shadow|fill|stroke|"
                        r"opacity|filter|backdrop-filter|text-shadow|outline)")
painted = []
for f in sorted((COMP / "patterns").glob("*.css")):
    body = re.sub(r"/\*.*?\*/", "", f.read_text(encoding="utf-8"), flags=re.S)
    for sel, decl in re.findall(r"([^{}]+)\{([^{}]*)\}", body):
        if sel.strip().startswith("@"):
            continue
        for one in decl.split(";"):
            prop = one.split(":")[0].strip()
            if prop and PAINT_PROP.match(prop):
                painted.append("%s %s{%s}" % (f.name, sel.strip()[:24], one.strip()[:28]))
check("23 a pattern carries no colour", not painted,
      "%d: %s" % (len(painted), "; ".join(painted[:3])))

# 24 ------------------------------------------------- a stand shows the whole --
# The level is arithmetic over what a component CONTAINS, and containment is read
# out of the specimen DOM. So a stand that shows a narrower case than the product
# does makes the map short, the arithmetic comes out low, and a RAISE floor
# covers the difference: the level is then declared and nothing on the page says
# it was. That is not a hypothesis. It is how `hiw-dialog` came to be an organism
# by assertion, and how five more stands were found short on 2026-08-02.
#
# The check is a containment comparison, not a picture comparison: what the
# component contains in `ui-kit/specimens/` against what it contains on the 105
# painted screens, both read by the SAME function, minus what
# `_levels.SPECIMEN_DEBT` declares. It fails at the moment a component gains a
# case that nobody stages, which is the moment its level stops being computed.
#
# THE SECOND CHECK IS THE IMPORTANT ONE. A list of declared exceptions that can
# be quietly extended is not a gate, it is the switch that turns one off: the
# cheapest way past the first check would be to add a line to SPECIMEN_DEBT. So
# an entry that covers no real difference fails just as loudly, and a debt that
# gets paid has to be deleted rather than left lying.
#
# It costs a second: 105 documents parsed once. That is the price of asking the
# rendered tree instead of the source, which is the rule this repo learned the
# expensive way.
from _audit_specimens import gap as specimen_gap  # noqa: E402

undeclared, superfluous, _real = specimen_gap()
flat = ["%s contains %s (.%s)" % (c, p, ", .".join(cls))
        for c, parts in sorted(undeclared.items()) for p, cls in sorted(parts.items())]
check("24 a stand shows the whole component", not flat,
      "%d: %s" % (len(flat), "; ".join(flat[:3])))
check("24 no declared exception is idle", not superfluous,
      "%d: %s" % (len(superfluous), ", ".join("%s -> %s" % e for e in superfluous)))

# 25 -------------------------------------------------------- four states, or --
# The states pass has to answer for all 36 files, and a file with no `:hover`
# reads identically whether that was decided or forgotten. `_levels.STATIC` is
# the decision, one line of reason each, and this makes it load-bearing BOTH
# ways: a component not on the list must declare hover and press, and a
# component on it must declare neither. Without the second half the cheapest way
# past the first would be to add a line to STATIC, which is how an exception
# list stops being a declaration and becomes the switch that turns a gate off.
#
# Focus is deliberately NOT in this count. `base.css` declares :focus-visible
# once for the whole system and a browser sweep of 153 pages in both themes
# found 0 of 179 ring kinds missing; fourteen component files used to carry
# their own copy and twenty-four did not, and gathering it was the point. A
# component only speaks up when its GROUND needs something different, so
# counting :focus-visible per file would push the system straight back into the
# shape base.css was written to undo.
#
# The third check is the one that keeps a state a TOKEN rather than a style, and
# it asks about COLOUR only. A colour written into a state rule is a colour no
# theme can reach, so it fails in the theme nobody was looking at; a length, an
# angle or a shadow offset has nothing for a theme to override, which is the same
# reason geometry gets no semantic level in tokens.css. `filter:brightness()` is
# counted as colour on purpose: it multiplies whatever is underneath, so it is a
# colour decision wearing a number, and the same 1.08 lightens a dark brass in
# one theme and washes out a pale one in the other.
STATE = re.compile(r":(hover|active)\b")
COLOUR_VALUE = re.compile(r"#[0-9a-f]{3,8}\b|\brgba?\(|\bhsla?\(|"
                          r"\b(?:brightness|saturate|contrast|invert|sepia)\(", re.I)
mute, loud, styled = [], [], []
for f in sorted(COMP.glob("*.css")):
    if f.stem in ("tokens", "index", "fonts"):
        continue
    body = re.sub(r"/\*.*?\*/", "", f.read_text(encoding="utf-8"), flags=re.S)
    rules = [(s.strip(), d) for s, d in re.findall(r"([^{}]+)\{([^{}]*)\}", body)
             if not s.strip().startswith("@") and STATE.search(s)]
    kinds = {k for s, _ in rules for k in STATE.findall(s)}
    if f.stem in LEVEL_STATIC:
        if kinds:
            loud.append("%s (%s)" % (f.stem, ", ".join(sorted(kinds))))
        continue
    if {"hover", "active"} - kinds:
        mute.append("%s (has %s)" % (f.stem, ", ".join(sorted(kinds)) or "none"))
    for sel, decl in rules:
        for one in decl.split(";"):
            if ":" not in one:
                continue
            prop, val = [x.strip() for x in one.split(":", 1)]
            if not prop or prop.startswith("--"):
                continue
            if COLOUR_VALUE.search(re.sub(r"var\(--[a-z0-9-]+\)", "", val)):
                styled.append("%s %s{%s:%s}" % (f.stem, sel[:26], prop, val[:24]))
check("25 an interactive component has hover and press", not mute,
      "%d: %s" % (len(mute), ", ".join(mute[:4])))
check("25 no component declared static has one", not loud,
      "%d: %s" % (len(loud), ", ".join(loud[:4])))
check("25 a state is a token, not a value", not styled,
      "%d: %s" % (len(styled), "; ".join(styled[:3])))

# 26 --------------------------------------------- a rule of use, in two places --
# A rule of use is the only thing in this system that is about several components
# at once, so it has no component file to live in and it is authored in prose:
# the "Rules of use" table in docs/architecture.md. Prose is where a fact goes to
# be duplicated, and this one is duplicated on purpose, because a person about to
# place a component is reading that component's page and not a contract. So the
# extract is generated from the table, and this gate is what stops the copy from
# becoming a second author.
#
# Three checks, and the third is the one that makes the pair honest. Without it
# the cheapest way to satisfy the second would be to write a rule onto a page and
# never decide it in the document, which is precisely the failure the table was
# built to prevent: a preference that learned to sound like a measurement.
rules = _gen_docs.usage_rules()
sourceless = ["%s (%s)" % (r["id"], what) for r in rules for what in
              (["no source"] if not r["source"] else []) +
              (["no component"] if not r["components"] else []) +
              (["class %r" % r["cls"]] if r["cls"] not in ("COMPOSITION", "CONTEXT") else []) +
              (["names %s, which has no file" % c for c in r["components"]
                if not (COMP / (c + ".css")).exists()])]
ids = [r["id"] for r in rules]
if len(ids) != len(set(ids)):
    sourceless.append("duplicate id")
check("26 every rule has a source and an owner", rules and not sourceless,
      "%d rule(s), %d problem(s): %s" % (len(rules), len(sourceless), ", ".join(sourceless[:4])))

RULE_SEC = re.compile(r'<section class="tk-sec" id="rules">(.*?)</section>', re.S)
want = {}
for r in rules:
    for c in r["components"]:
        want.setdefault(c, set()).add(r["id"])
# Patterns are in this loop and NOT in gate 25's or gate 2's, and the difference
# is the whole distinction: those two ask what a component IS, and a pattern is
# not one. This asks whether a rule written about a thing reaches the page of
# that thing, and a pattern has a page.
unpaired = []
for path in sorted(COMP.glob("*.css")) + sorted((COMP / "patterns").glob("*.css")):
    name = path.stem if path.parent == COMP else "patterns/" + path.stem
    if name in ("index", "tokens", "fonts"):
        continue
    page = KIT / (path.stem + ".html")
    if not page.exists():
        continue
    sec = RULE_SEC.search(page.read_text(encoding="utf-8"))
    got = set(re.findall(r">(R\d+)<", sec.group(1))) if sec else set()
    if got != want.get(name, set()):
        unpaired.append("%s page %s, table %s" % (
            name, sorted(got) or "-", sorted(want.get(name, set())) or "-"))
check("26 every rule is on the pages it names", not unpaired,
      "%d: %s" % (len(unpaired), "; ".join(unpaired[:3])))

orphan_rule = sorted({rid for path in KIT.glob("*.html")
                      for sec in RULE_SEC.findall(path.read_text(encoding="utf-8"))
                      for rid in re.findall(r">(R\d+)<", sec)} - set(ids))
check("26 no page carries a rule the document lacks", not orphan_rule,
      "%d: %s" % (len(orphan_rule), ", ".join(orphan_rule[:4])))

# 27 ------------------------------------------ a pattern, and its only render --
# A component has two renders outside the product, a specimen and a stand. A
# pattern has one, because step 3 took patterns out of gate 24's corpus on
# purpose: that gate asks what a component CONTAINS, and a pattern contains
# whatever the screen puts in it. So the page is not documentation of the
# pattern, it is the only test of it, and a pattern whose page is missing is a
# pattern that exists only inside the product.
#
# The second check is the load-bearing one, and it is the threshold itself made
# executable. A pattern is admitted for standing on THREE OR MORE SCREENS, so
# that is the one claim its page has to be able to prove: the screens are read
# from the markup of ui-visual/ here, not from the page, and compared with what
# the page lists. A page that names two screens is not a thin pattern, it is a
# composition that stopped qualifying while nobody was counting.
#
# The third is the mirror, in the shape every declaration in this system has: a
# page in the Patterns group with no file behind it. Without it the cheapest way
# to satisfy the first two would be to write a page and never write a pattern.
PAT_CSS = sorted((COMP / "patterns").glob("*.css"))
SCREEN_FILES = [p for p in sorted(UVIS.glob("*.html")) if p.name != "overview.html"]
SCREEN_CLS = {p.name: {c for m in re.findall(r'class="([^"]*)"',
                                             p.read_text(encoding="utf-8")) for c in m.split()}
              for p in SCREEN_FILES}
sys.path.insert(0, str(KIT))
import _gen_pattern_pages as _gpp                                     # noqa: E402

pageless, thin = [], []
declared_scene = {s["name"]: s for s in _gpp.SCENES}
for css in PAT_CSS:
    name = css.stem
    page = KIT / (name + ".html")
    scene = KIT / "patterns" / (name + ".html")
    if not page.exists():
        pageless.append(name + ".html missing")
        continue
    if not scene.exists():
        pageless.append("patterns/%s.html missing, so the page frames nothing" % name)
        continue
    spec = declared_scene.get(name)
    if not spec:
        pageless.append(name + " has no scene declared")
        continue
    src = page.read_text(encoding="utf-8")
    listed = set(re.findall(r'href="\.\./ui-visual/([\w.-]+\.html)"', src))
    real = {n for n, cs in SCREEN_CLS.items() if spec["root"] in cs}
    if len(real) < 3:
        thin.append("%s stands on %d screens" % (name, len(real)))
    elif not real <= listed:
        thin.append("%s lists %d of %d screens" % (name, len(listed & real), len(real)))
check("27 every pattern has a page and a scene", not pageless,
      "%d: %s" % (len(pageless), ", ".join(pageless[:3])))
check("27 a pattern still stands on three screens", not thin,
      "%d: %s" % (len(thin), ", ".join(thin[:3])))

NAV_PAT = re.compile(r'group: "Patterns", name: "([^"]+)", file: "([^"]+)"')
_stems = {p.stem for p in PAT_CSS}
ghost = ["%s (%s)" % (n, f) for n, f in NAV_PAT.findall(NAVJS)
         if n != "patterns" and n not in _stems]
check("27 no page in the group without a file", not ghost,
      "%d: %s" % (len(ghost), ", ".join(ghost[:3])))

# 28 ---------------------------------------------- the guide names its sources --
# WHY THIS GATE EXISTS, and it is a different argument from every other gate here.
# The others catch a defect a reader would eventually see. This one catches a
# LOSS NOBODY CAN SEE, and that is the whole point.
#
# concept/docs/references.md was written at Concept and has had no reader since.
# Nothing between that stage and this one opens it, and nothing after this one
# has any reason to. So the four references it names arrive on why.html or they
# leave the project: not deferred, not degraded, gone, and gone silently, because
# the page still renders and still reads well with a row missing. There is no
# reader left to notice, by construction.
#
# So the page is not trusted to be a copy. The two documents are parsed HERE,
# independently of the generator that built the page, and every row either
# document declares has to appear on it. Reading them through _gen_why_page would
# check the generator against itself.
# The page escapes what it prints, so the document's text has to be escaped the
# same way before it is looked for. Comparing raw markdown against escaped html
# is how a check reports a missing row that is on the page in front of it.
from html import escape as _esc                                       # noqa: E402


def html_escape(s):
    """quote=False, matching the page. The default turns an apostrophe into
       &#x27;, and A3 is "A spectator's clarity": the check reported a missing
       attribute that was on the page in front of it."""
    return _esc(s, quote=False)
_why = KIT / "why.html"
_refs_md = ROOT / "concept" / "docs" / "references.md"
_concept_md = ROOT / "concept" / "docs" / "concept.md"
lost = []
if not _why.exists():
    lost.append("why.html missing")
else:
    _wt = _why.read_text(encoding="utf-8")
    _rt = _refs_md.read_text(encoding="utf-8")
    for line in _rt[_rt.index("## Source index"):].split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] == "Source" or set(cells[0]) <= set("-: "):
            continue
        if html_escape(cells[0]) not in _wt:
            lost.append("reference %r" % cells[0])
    for m in re.finditer(r"^### (A\d) - (.+)$", _concept_md.read_text(encoding="utf-8"), re.M):
        if m.group(1) not in _wt or html_escape(m.group(2).strip()) not in _wt:
            lost.append("attribute %s" % m.group(1))
    for path, _ in [(p, n) for p, n in __import__("_gen_why_page").SOURCES]:
        if not (ROOT / path).exists():
            lost.append("%s does not exist" % path)
        elif path not in _wt:
            lost.append("%s is not cited" % path)
check("28 the guide names every source it was built from", not lost,
      "%d: %s" % (len(lost), ", ".join(lost[:4])))

# The mirror, and the same shape the other declarations have: a page that lists a
# reference the document no longer holds is the copy quietly becoming the
# original. Read the names off the page and ask the document about each.
import _gen_why_page                                                  # noqa: E402
_declared = {r["name"] for r in _gen_why_page.references()}
_on_page = set(re.findall(r'<td class="tk-role">([^<]+)</td>',
                          _why.read_text(encoding="utf-8"))) if _why.exists() else set()
invented = sorted(n for n in _on_page if html_escape(n) not in
                  {html_escape(d) for d in _declared})
check("28 the guide invents no source", not invented,
      "%d: %s" % (len(invented), ", ".join(invented[:3])))

# And the page is what its sources render to today, not what they rendered to
# when someone last ran the generator. Same argument as gate 21: a file can be
# newer than its sources and still be wrong.
check("28 the guide is current", _why.exists() and
      _why.read_text(encoding="utf-8") == _gen_why_page.render(),
      "run: python3 ui-kit/_gen_why_page.py")

# 29 ------------------------------------------------------------- current ---
# THE CLASS GATE 28 SAW IN ONE PAGE, FOR EVERY PAGE A GENERATOR OWNS. A
# generated page nobody rebuilds stays TRUE about a product that no longer
# exists, and every other gate reads what the page says, so the page passes
# while being wrong about the world. Two of them were found by hand on the same
# afternoon: icons.html said "76 of 76 screens carry the sprite" for a
# 104-screen tree and counted 39 inline shapes against 37, and tokens.html
# counted 133 roles against the 137 the states pass left behind. Neither was
# edited by anyone. Both were simply not re-run.
#
# Gate 28 answered it for why.html by comparing the file to what its generator
# renders today. That shape does not generalise by import: three of the eight
# generators do their work at module level, so importing them to ask would
# WRITE, and a checker that writes is not a checker. So the same question is
# asked the only other way it can be: copy what the generators read into a
# scratch tree, run them there, and compare. The working tree is never touched.
#
# The comparison is a gate and not a coin flip because the generators are
# deterministic: the whole chain was run twice in a row against a clean tree and
# the second run changed nothing.
#
# WHAT IS DECLARED OUT, and why it is a declaration rather than an omission.
# Three generators are not the sole author of the page they write, so comparing
# a page to its generator would fail forever, and a permanently red gate is
# worse than no gate at all: it teaches the next person that red is the normal
# colour. Each one is named with the second author.
GENERATOR_CHAIN = (
    "_extract_specimens", "_gen_component_pages", "_gen_pattern_pages",
    "_gen_icons_page", "_gen_tokens_page", "_fill_inventory", "_gen_docs",
    "_gen_why_page",
)
SECOND_AUTHOR = {
    "ui-visual/_gen_overview.py":
        "the painted tree's index. _resync_sidebar.py writes the course panel "
        "into it afterwards, so the generator alone drops 193 lines of it",
    "ui-visual/_gen_category.py":
        "the four category screens. _apply_family.py, _panel_reveal.py and "
        "_resync_sidebar.py all run after it, and re-running it regresses all four",
    "wireframes/_generators/gen_*.py":
        "CLAUDE.md forbids running them at all: the voice rewrite went into the "
        "grey HTML by hand and was never back-ported, so a rebuild reverts it",
}
# What the chain writes, and therefore what is compared. A hand-kept page in
# ui-kit/ is copied and never written, so it matches by construction and costs
# nothing; the number reported is the number a generator owns.
GENERATED_GLOBS = ("ui-kit/*.html", "ui-kit/_nav.js", "ui-kit/_frames.js",
                   "ui-kit/specimens/*", "ui-kit/patterns/*",
                   "ui-kit/docs/*.md", "README.md")
HAND_KEPT = {"kit.html", "shell.html", "specimens.extra.html"}
_COPY = ("components", "ui-kit", "ui-visual", "wireframes", "concept", "docs",
         "voice", "ia", "assets", "user-research", "research")
_SKIP = {"screens", "old", "__pycache__", ".git", "node_modules"}

import shutil                                                         # noqa: E402
import tempfile                                                       # noqa: E402

_stale, _broke, _owned = [], [], 0
_scratch = pathlib.Path(tempfile.mkdtemp(prefix="kit-current-"))
try:
    for _d in _COPY:
        if (ROOT / _d).exists():
            shutil.copytree(ROOT / _d, _scratch / _d, symlinks=True,
                            ignore=lambda d, names: [n for n in names if n in _SKIP])
    for _f in list(ROOT.glob("*.py")) + list(ROOT.glob("*.md")):
        shutil.copy2(_f, _scratch / _f.name)
    for _g in GENERATOR_CHAIN:
        _r = subprocess.run([sys.executable, str(_scratch / "ui-kit" / (_g + ".py"))],
                            capture_output=True, cwd=str(_scratch))
        if _r.returncode:
            _broke.append("%s: %s" % (_g, _r.stderr.decode("utf-8", "replace")
                                      .strip().splitlines()[-1][:90]))
    for _pat in GENERATED_GLOBS:
        for _new in sorted(_scratch.glob(_pat)):
            _rel = _new.relative_to(_scratch)
            if _new.name in HAND_KEPT or not _new.is_file():
                continue
            _owned += 1
            _old = ROOT / _rel
            if not _old.exists() or _old.read_bytes() != _new.read_bytes():
                _stale.append(str(_rel))
finally:
    shutil.rmtree(_scratch, ignore_errors=True)

check("29 every generator still runs", not _broke,
      "%d: %s" % (len(_broke), "; ".join(_broke[:2])))
check("29 every generated page is current", not _stale,
      "%d of %d: %s" % (len(_stale), _owned, ", ".join(_stale[:4])))
check("29 a second author is declared", len(SECOND_AUTHOR) == 3,
      "%d generator(s) whose page they do not solely own" % len(SECOND_AUTHOR))

# 30 ------------------------------------------- the product wears it, or not --
# THE OTHER HALF OF GATE 14, and the half that had never been asked. Gate 14
# fails on a selector no markup ANYWHERE can match, so its corpus is the union of
# every tree this stylesheet reaches: the painted screens, the specimens, the
# frozen kit, the vitrine's own pages and the scripts. A class carried only by
# the kit passes it, which is correct for the question it asks and useless for
# this one.
#
# The question here is narrower and it is the one that costs: does the PRODUCT
# wear what the system declares? A class styled in components/ and carried by
# none of the 105 painted screens is either dead code or a naming convention
# nobody adopted, and the second is the expensive kind, because the stand goes on
# teaching it. On 2026-08-03 that was six classes of button.css - .btn-primary,
# .btn-secondary, .btn-sm, .btn-md, .btn-lg, .btn-block - half of what the
# component declared, with two specimens of their own and a size ramp, against
# 704 uses of the four names the product actually writes. The next person to
# build a screen would have read the page, taken .btn-secondary, and added a
# seventh class no product rule paints. Two more fell out with them on the first
# run: .signin-lead, carried by no element in any tree, and .delta .row, which
# lived in header.css and describes a course page.
#
# THE SECOND CHECK IS THE ONE THAT KEEPS IT HONEST, exactly as in gate 24. A
# zero is right for four reasons and only a person can tell them apart, so
# _adoption.NOT_WORN declares each one with its reason; and the cheapest way past
# the first check would then be a new line there. So a declared class that is NOT
# a zero fails just as loudly. That half earned its keep immediately: .track and
# .fill were declared as run-time classes on the first draft, copied from a note
# the stand pages carried, and the painted screens ship both in the markup.
#
# The reading is in _adoption.py and not here because _gen_component_pages.py
# needs the same answer for docs/coverage.md and for the Classes table on every
# stand page. Two readings of one truth is the defect this repo has already paid
# for twice, between coverage.md and the css headers and between the two panel
# generators.
from _adoption import unadopted, NOT_WORN                             # noqa: E402

_unworn, _idle = unadopted()
check("30 the product wears what is declared", not _unworn,
      "%d: %s" % (len(_unworn), "; ".join(_unworn[:4])))
check("30 no declared exception is idle", not _idle,
      "%d: %s" % (len(_idle), ", ".join(_idle)))
notes.append("%-34s %s" % ("30 declared, and not worn",
                           "%d class(es), each with its reason" % len(NOT_WORN)))

# ---- 32. the authored half is checked, and it is checked BEFORE it is written -
# THE ONE ARTEFACT NO GATE COULD READ, until this one. Everything else in this
# vitrine is held against something: a class against the css, a rule against the
# document, a picture against the bytes it was taken from. A SENTENCE cannot be
# checked for being true, and that was taken to mean it could not be checked at
# all. It can be checked for the four things that make the difference between a
# written page and a fluent one: that it exists or is declared absent with a
# reason, that its sections are all answered, that every class and every source
# it names is real, and that its anti-rule sends the reader to a named component
# with an honest provenance.
#
# WHY IT IS HERE AND NOT AT THE END OF THE FAN-OUT. It was going to be, and the
# ordering was wrong. `ui-kit/authored/account.md` was committed on 2026-08-03
# with two source paths written without their folder; it failed its own checker
# from the first minute and nothing said so, because the checker was a script a
# person had to remember to run and the round it belonged to had already been
# reported green. A gate that arrives after the last author has not paid for a
# single line of writing. So it goes in first, and the six pattern files are
# written under it: this gate is RED while they are missing, by name, one line
# each, and each file that lands turns one line green.
#
# The reading is in `_authored.py` with the reasoning, and this gate is the
# place it becomes load-bearing. `--check` and a gate are not the same promise.
from _authored import check as _authored_check, COMPUTED_ONLY as _computed_only  # noqa: E402
from _authored import registry_names as _authored_names, pattern_screens as _pat_screens  # noqa: E402

_a_names = _authored_names()
_a_groups = _states.by_component() if "_states" in dir() else __import__("_states").by_component()
_a_rules = usage_rules() if "usage_rules" in dir() else __import__("_gen_docs").usage_rules()
_a_rule_ids = {r["id"] for r in _a_rules}
_a_counted = _pat_screens()
_a_bad = []
for _c in sorted(_a_names):
    _text = " ".join(r["title"] + " " + r["check"] for r in _a_rules if _c in r["components"])
    for _b in _authored_check(_c, _a_groups.get(_c), _text, _a_names, _a_rule_ids,
                              _a_counted.get(_c)):
        _a_bad.append("%s: %s" % (_c, _b))
_a_idle = sorted(set(_computed_only) & {p.stem for p in (KIT / "authored").glob("*.md")})
check("32 every component has an author", not _a_bad,
      "%d: %s" % (len(_a_bad), "; ".join(_a_bad[:4])))
check("32 no computed-only claim is idle", not _a_idle,
      "%d: %s" % (len(_a_idle), ", ".join(_a_idle)))
notes.append("%-34s %s" % ("32 declared computed-only",
                           "%d component(s), each with its reason" % len(_computed_only)))

# ---------------------------------------------------------------- verdict ---
for line in notes + fails:
    print(line)
print("\n%d specimens, %d components, %d stand pages" %
      (len(manifest), len(components), len(list(KIT.glob("*.html")))))
if fails:
    print("\n%d gate(s) failed" % len(fails))
    sys.exit(1)
print("all gates pass")
