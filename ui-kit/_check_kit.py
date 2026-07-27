#!/usr/bin/env python3
"""The gates for the vitrine. One command, exits non-zero on the first failure.

    python3 ui-kit/_check_kit.py

Thirteen checks, each one a defect that actually happened at least once:

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
gone_kit = [str(p.relative_to(ROOT)) for p in
            list(ROOT.glob("*/*.html")) + list(ROOT.glob("*/*.css"))
            if 'href="kit.css"' in p.read_text(encoding="utf-8", errors="ignore")]
check("9 nothing loads the flat kit", not gone_kit, ", ".join(gone_kit))

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
# from grey-box css that the extraction copied along with everything else. A
# class toggled by script counts as carried, so classList add/remove/toggle is
# read out of the pages too.
carried = set()
for page in (list(UV.glob("*.html")) + list(KIT.glob("*.html")) + list(SPECS.glob("*.html"))
             + list((ROOT / "wireframes").glob("*.html"))):
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

# ---------------------------------------------------------------- verdict ---
for line in notes + fails:
    print(line)
print("\n%d specimens, %d components, %d stand pages" %
      (len(manifest), len(components), len(list(KIT.glob("*.html")))))
if fails:
    print("\n%d gate(s) failed" % len(fails))
    sys.exit(1)
print("all gates pass")
