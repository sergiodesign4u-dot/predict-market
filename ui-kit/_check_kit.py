#!/usr/bin/env python3
"""The gates for the vitrine. One command, exits non-zero on the first failure.

    python3 ui-kit/_check_kit.py

Seventeen checks, each one a defect that actually happened at least once:

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
# the theme boot script is chrome by the same argument as the sidebar: it is
# wrapped around the screen, sets an attribute on <html> and paints nothing.
# Built and removed by ui-visual/_theme_switch.py.
BOOT = re.compile(r'\n?<script id="uvTheme">.*?</script>', re.DOTALL)


def bare(html):
    return BOOT.sub("", ASIDE.sub("", html))

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
for path in COMP.glob("*.css"):
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    if re.search(r"\.(tk|ck)-[\w-]+", body):
        stand_in_comp.append(path.name)
check("6 components carry no stand class", not stand_in_comp, ", ".join(stand_in_comp))

# 7 --------------------------------------------------------------- em dash --
dash = [p.name for p in
        list(KIT.glob("*.html")) + list(SPECS.glob("*.html")) + list(KIT.glob("*.css"))
        + list(KIT.glob("*.py")) + list(KIT.glob("*.json")) + list((KIT / "docs").glob("*.md"))
        + list((KIT / "_verify").glob("*")) + list(COMP.glob("*.css"))
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
readers = [p for p in COMP.glob("*.css") if p.name not in ("tokens.css", "index.css")]
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
for path in sorted(COMP.glob("*.css")):
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
        for path in sorted(COMP.glob("*.css")) if path.name != "tokens.css"
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
carried = set()
for page in (list(UV.glob("*.html")) + list(KIT.glob("*.html")) + list(SPECS.glob("*.html"))
             + list((ROOT / "wireframes").glob("*.html"))
             + list(UV.glob("*.js")) + list(KIT.glob("*.js"))):
    src = page.read_text(encoding="utf-8", errors="ignore")
    for group in re.findall(r'class=\\?["\']([^"\'\\]*)', src):
        carried.update(group.split())
    for call in re.findall(r"classList\.(?:add|remove|toggle)\(([^)]*)\)", src):
        carried.update(re.findall(r"['\"]([\w-]+)['\"]", call))

unmatched = []
for path in sorted(COMP.glob("*.css")):
    if path.name in ("tokens.css", "index.css"):
        continue
    body = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    for block_sel in re.findall(r"([^{}]+)\{", body):
        block_sel = block_sel.strip()
        if block_sel.startswith("@") or not block_sel:
            continue
        for sel in block_sel.split(","):
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
for path in sorted(COMP.glob("*.css")):
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
for path in sorted(COMP.glob("*.css")):
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
for path in sorted(COMP.glob("*.css")):
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
# Everything else has to match. header, footer and bottom nav are NOT compared:
# they carry their own declared differences (the wireframe screen-tree drawer,
# the TBD chips) and are written up in wireframes/_conventions.md.
PLATE = {"cat-layout", "cat-main", "feed-inner"}
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
        drop = tag == "div" and bool(set(classes) & PLATE)
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


MAIN = re.compile(r"<main\b.*?</main>", re.S)
drift = []
for page in sorted((ROOT / "ui-visual").glob("*.html")):
    twin = ROOT / "wireframes" / page.name
    if not twin.exists():
        continue
    a = MAIN.search(page.read_text(encoding="utf-8"))
    b = MAIN.search(twin.read_text(encoding="utf-8"))
    if not a or not b:
        continue
    if shape(a.group(0)) != shape(b.group(0)):
        drift.append(page.name)
check("18 the two trees agree", not drift,
      "%d: %s" % (len(drift), ", ".join(drift[:4])))

# ---------------------------------------------------------------- verdict ---
for line in notes + fails:
    print(line)
print("\n%d specimens, %d components, %d stand pages" %
      (len(manifest), len(components), len(list(KIT.glob("*.html")))))
if fails:
    print("\n%d gate(s) failed" % len(fails))
    sys.exit(1)
print("all gates pass")
