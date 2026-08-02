#!/usr/bin/env python3
"""Build one stand page per component, plus the hub and the registry.

For every components/<name>.css it writes ui-kit/<name>.html carrying:
  - the component live, in a frame of its own, at the width it is meant to be
    read at (a mobile-only piece gets 360, so the media query shows it instead
    of being overridden);
  - the states the markup carries, and the rules behind the states it cannot
    hold still (hover, focus) quoted from the file rather than faked;
  - the semantic roles the file reads, each with a swatch;
  - the classes it owns and how many painted screens carry each one;
  - the screens in ui-visual/ where the component stands, as links;
  - the css itself, so the file and the page never drift apart.

Specimens come from ui-kit/specimens/, built by _extract_specimens.py out of the
labelled blocks of the frozen kit. A component page renders only the specimens
it OWNS; where it merely appears inside a bigger one, it links instead, so no
markup is shown twice.

Also writes ui-kit/_nav.js (the one registry), ui-kit/overview.html (the hub)
and ui-kit/_frames.js (the parent half of the frame height handshake).

    python3 ui-kit/_extract_specimens.py && python3 ui-kit/_gen_component_pages.py

Idempotent. Never touches components/ or ui-visual/. No em dash.
"""
import glob
import html
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
KIT = ROOT / "ui-kit"
UV = ROOT / "ui-visual"

# the theme switch is written once, in the tree that also puts it on the 76
# painted screens. Importing it keeps the stand pages and the product on the
# same boot script instead of two copies that can drift.
sys.path.insert(0, str(UV))
from _theme_switch import BOOT as THEME_BOOT, BUTTON as THEME_BUTTON, button  # noqa: E402
# the panel opens showing where you are, and the screens tree does the same
# thing from the same string: two panels, one behaviour, one source.
from _panel_reveal import BODY as REVEAL_BODY, CALL as REVEAL_CALL  # noqa: E402
# the four documents are rows in the same registry as the components, and the
# table that names them lives with the renderer, not here: two lists of one
# fact is how coverage.md and the css headers came to disagree.
sys.path.insert(0, str(KIT))
from _gen_docs import PAGES as DOC_PAGES  # noqa: E402
THEME_BUTTON_INLINE = button(inline=True)

SPECIMENS = json.loads((KIT / "specimens" / "index.json").read_text(encoding="utf-8"))
TOKENS = (COMP / "tokens.css").read_text(encoding="utf-8")
SEM = set(re.findall(r"(--[\w-]+)\s*:", TOKENS[TOKENS.index("2. SEMANTIC"):]))

# The panel is grouped by LEVEL, and inside a group it reads in the order the
# cascade loads. It used to be grouped by PURPOSE, which is the right way to
# group a product and the wrong way to group a system: a group named for where a
# thing is used answers a question the screens already answer, and it puts a
# button next to a sign-in dialog because both appear in a form. Grouped by
# level, the panel answers the question a system has instead, which is what may
# be built out of what, and reading it top to bottom is reading index.css.
#
# Derived, not typed, from the same map that orders the cascade: two lists of one
# fact is how coverage.md and the css headers came to disagree.
from _levels import LEVEL as _LEVEL, ORDER as _ORDER, NOT_A_COMPONENT as _NOT_COMP  # noqa: E402

GROUPS = [("Foundations", ["tokens", "icons", "base", "course-chrome"])] + [
    (name, [f for f in _ORDER if _LEVEL.get(f) == n and f not in _NOT_COMP])
    for n, name in ((1, "Atoms"), (2, "Molecules"), (3, "Organisms"))
]
LABEL = {
    "tokens": "Tokens", "icons": "Icons", "base": "Base and page frame",
    "course-chrome": "Course chrome",
    "header": "App header", "catnav": "Category nav", "bottomnav": "Bottom nav", "tabs": "Tabs",
    "footer": "Footer", "trustbar": "Trust bar and cards", "feed": "Feed layout", "card": "Event card",
    "oddsbar": "Odds bar", "yesno": "YES / NO buttons", "options": "Outcome rows", "hero": "Featured hero",
    "seo-plate": "SEO plate", "loadmore": "Load more", "filters": "Sort and filters",
    "event-detail": "Event Detail layout", "chart": "Price chart", "betpanel": "Bet panel and dock",
    "market": "AMM market panel", "comments": "Comments", "bets-table": "Bets and activity",
    "related": "Related events", "button": "Buttons", "input": "Fields and amounts",
    "dialog": "Shared dialog", "hiw-dialog": "How-it-works dialog",
    "notice": "Notices and banners", "state-block": "State block", "skeleton": "Skeletons",
    "toast": "Toasts",
    "profile": "Profile identity", "position": "Position rows", "account": "Account bars",
    "cookie-consent": "Cookie consent",
}
NOTE = {
    "base": "Not a component: the page frame, the reset, the shared utilities and the neutralisation "
            "block that hides the grey-box scaffolding the wireframes left behind.",
    "course-chrome": "Not product: the roadmap sidebar every page of this repo carries. It ships with "
                     "the system only because the painted screens render it.",
}
# Sections on tokens.html that answer a foundation question. One page, several doors.
FOUNDATION_DOORS = [
    ("Colour", "tokens.html#colour", "Every graphite step and every brass, and the roles that read them."),
    ("Material", "tokens.html#material", "The two-stone plates, the grain, the bevels and the grooves."),
    ("Geometry", "tokens.html#geometry", "Spacing, radius, control sizes, the container and the gutter."),
    ("Type", "tokens.html#type", "Three families, the size ramp, weight and leading."),
    ("Motion", "tokens.html#motion", "Durations and easings, shown moving."),
]

STATE_PAT = re.compile(r":hover|:focus-visible|:focus|:active|:disabled|:checked|"
                       r"\[aria-current|\[aria-checked|\[open\]|\[disabled\]|"
                       r"\.sel\b|\.active\b|\.open\b|\.scrolled\b|\.skeleton\b|\.is-[\w-]+")


def esc(s):
    return html.escape(s, quote=False)


# ---- where a class is actually used ----------------------------------------
# A class the painted screens do not carry can still be alive. A zero means one
# of five things, and the Classes table says which, because "0" on its own reads
# as "delete me" and four times out of five that would be wrong.
#
# The runtime list is short and each entry was checked by hand against the
# script that creates it. It is not derived by pattern, because a pattern
# matches "brand" inside "sidebar-brand".
RUNTIME = {
    "oddsbar": "built by the feed script from the probability text",
    "track": "part of the odds bar the feed script builds",
    "fill": "part of the odds bar the feed script builds",
    "m-label": "the card meta row, split by the feed script",
    "m-val": "the card meta row, split by the feed script",
    "lg-item": "the chart legend, built by the detail script",
    "scrolled": "added to the header by a scroll observer",
    "open": "toggled on the drawer and the overlay by script",
}


def classes_in(pattern, strip_style=False, strip_quoted=False):
    out = {}
    for f in sorted(glob.glob(pattern)):
        text = open(f, encoding="utf-8", errors="ignore").read()
        if strip_style:
            text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.S)
        if strip_quoted:
            # A stand page ends with the component's own css and every document
            # quotes markup, so class="x" inside <pre> or <code> is a QUOTATION,
            # not an element. Same rule three gates had to learn in step 8b.
            text = re.sub(r"<(pre|code)\b[^>]*>.*?</\1>", "", text, flags=re.S)
        cs = set()
        for m in re.finditer(r'class="([^"]*)"', text):
            cs.update(m.group(1).split())
        out[os.path.basename(f)] = cs
    return out


def flat(d):
    return set().union(*d.values()) if d else set()


uv_classes = classes_in(str(UV / "*.html"), strip_style=True)
# overview.html lives in ui-visual/ but is the index OF the screens, not one of
# them. Counting it would inflate every screen count by one and, worse, would let
# a class the index happens to use pass as "carried by a painted screen".
uv_classes.pop("overview.html", None)
# The specimens, the frozen kit, the composed shell AND the stand pages. The
# stand pages were missing, so a class carried only by the vitrine's own chrome
# fell through every bucket and was reported as a deletion candidate:
# .theme-switch-inline is real markup on overview.html and was on that list.
kit_used = flat(classes_in(str(KIT / "specimens" / "*.html"))) \
    | flat(classes_in(str(KIT / "kit.html"))) | flat(classes_in(str(KIT / "shell.html"))) \
    | flat(classes_in(str(KIT / "*.html"), strip_quoted=True))
wf_used = flat(classes_in(str(ROOT / "wireframes" / "*.html"), strip_style=True))
docs_used = flat(classes_in(str(ROOT / "*" / "*.html"), strip_style=True)) \
    - flat(uv_classes) - kit_used
uv_used = flat(uv_classes)


def where(c):
    """Why this class shows the count it shows."""
    if c in uv_used:
        return "", ""
    if c in RUNTIME:
        return "runtime", RUNTIME[c]
    if c in kit_used:
        return "kit", "shown in the frozen kit, never on a painted screen"
    if c in wf_used:
        return "wireframe", "carried only by wireframes/, which never loads this sheet"
    if c in docs_used:
        return "docs", "used by a course page, which does not load the system"
    return "unused", "styled and carried by no element anywhere"

# ---- every class any component file declares, for the orphan check ----------
declared = set()
for path in COMP.glob("*.css"):
    if path.stem in ("index", "tokens"):
        continue
    # A CLASS NAMED IN A COMMENT IS NOT A CLASS THE FILE STYLES. Only the url()
    # was cut here, so a note explaining which class a rule replaced put that
    # class straight back into the declared set, and coverage.md listed it as a
    # deletion candidate that had already been deleted. Both .ck-note-link and
    # .sidebar-sub-head came back that way in the same pass that removed them.
    body = re.sub(r"/\*.*?\*/", " ", path.read_text(encoding="utf-8"), flags=re.S)
    body = re.sub(r"url\([^)]*\)", "", body)
    declared.update(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", body))


# ---- which file OWNS a class, and therefore where a component STANDS --------
# The map moved to _levels.py, which needs the same answer to work out what
# stands INSIDE a component. Two copies of one map is the defect step 7c closed
# between coverage.md and the css headers and step 9 closed again between the two
# panel generators: one computation feeds both, or they drift and nobody can tell
# which to believe. The reasoning for the map is written there with it.
from _levels import SUBJECTS, OWNER  # noqa: E402


def parse_component(name):
    css = (COMP / (name + ".css")).read_text(encoding="utf-8")
    head = css[:css.index("*/") + 2] if "*/" in css else ""
    body = css[len(head):].strip()
    # WHAT THE FILE STYLES IS READ FROM ITS RULES, NOT FROM ITS PROSE. Only the
    # header comment was cut, so every later comment was scanned as css: that is
    # where .css and .color came from in the deletion-candidate table, harvested
    # out of the words "components/index.css" and "Colour goes through a role",
    # and it is how .ck-note-link and .sidebar-sub-head reappeared in the same
    # pass that deleted them, listed as candidates for a deletion already done.
    # body itself keeps its comments: it is also what the stand page prints.
    prose_free = re.sub(r"/\*.*?\*/", " ", body, flags=re.S)
    roles = sorted({m for m in re.findall(r"var\((--[\w-]+)\)", prose_free) if m in SEM})
    classes = sorted({c for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)",
                                            re.sub(r"url\([^)]*\)", "", prose_free))})
    rules = len(re.findall(r"\{", prose_free))
    owned = sorted(c for c in SUBJECTS.get(name, {}) if OWNER.get(c) == name)
    screens = sorted([p for p, cs in uv_classes.items() if cs & set(owned)])
    states = []
    for m in re.finditer(r"([^{}\n][^{}]*)\{([^{}]*)\}", body):
        sel = " ".join(m.group(1).split())
        if STATE_PAT.search(sel) and not sel.startswith("@"):
            states.append((sel, m.group(2).strip()))
    return dict(css=css, body=body, roles=roles, classes=classes, rules=rules,
                screens=screens, owned=owned, states=states)


# ---------------------------------------------------------------- sections ---
def live(name):
    mine = [s for s in SPECIMENS if s["component"] == name]
    if not mine:
        return ('<p class="tk-note">No specimen of its own yet. It is rendered inside the specimens '
                'linked below.</p>')
    out = []
    for s in mine:
        w = s.get("width", 900)
        cap = []
        if s.get("state"):
            cap.append('<span class="ck-cap-k">state</span> ' + esc(s["state"]))
        if s.get("note"):
            cap.append(esc(s["note"]))
        caption = ('<p class="ck-cap">' + "<br>".join(cap) + "</p>") if cap else ""
        out.append(
            f'<figure class="ck-scene" id="sp-{s["id"]}">'
            f'<figcaption class="ck-scene-lbl"><b>{esc(s["title"])}</b>'
            f'<span class="ck-w">{w}px</span><span class="ck-zoom" hidden></span>'
            f'<a href="specimens/{s["id"]}.html" target="_blank" rel="noopener">open on its own</a>'
            f"</figcaption>"
            f'<div class="ck-frame" style="width:{w}px">'
            f'<iframe data-specimen="{s["id"]}" src="specimens/{s["id"]}.html" '
            f'width="{w}" height="{s.get("height", 320)}" loading="lazy" '
            f'title="{esc(s["title"])}"></iframe></div>{caption}</figure>')
    return "\n".join(out)


def elsewhere(name):
    other = [s for s in SPECIMENS if name in s.get("also", [])]
    if not other:
        return ""
    links = "".join(
        f'<a href="{s["component"]}.html#sp-{s["id"]}">{esc(s["title"])}</a>' for s in other)
    return ('<section class="tk-sec" id="inside"><h2 data-n="02">Also rendered inside</h2>'
            '<p class="tk-note">The same markup, shown once on the page of the component that owns '
            'it. Nothing here is a second copy.</p>'
            f'<div class="ck-screens">{links}</div></section>')


def states_table(states):
    if not states:
        return ('<p class="tk-note">This file declares no state rule: the component looks the same '
                'at rest, on hover and on focus.</p>')
    rows = "".join(
        f"<tr><td class='tk-role'>{esc(sel)}</td><td class='ck-decl'>{esc(decl)}</td></tr>"
        for sel, decl in states[:24])
    more = ("<p class='tk-note'>%d more in the file below.</p>" % (len(states) - 24)) \
        if len(states) > 24 else ""
    return ('<table class="tk-tbl"><thead><tr><th>selector</th><th>what moves</th></tr></thead>'
            f"<tbody>{rows}</tbody></table>{more}")


def role_swatches(roles):
    if not roles:
        return '<p class="tk-note">Reads no colour role: this file is geometry and layout only.</p>'
    cells = "".join(f'<span class="ck-role"><i style="background:var({r})"></i><code>{esc(r)}</code></span>'
                    for r in roles)
    return f'<div class="ck-roles">{cells}</div>'


def class_table(classes):
    rows = []
    for c in classes:
        n = sum(1 for cs in uv_classes.values() if c in cs)
        kind, why = where(c)
        tag = f'<span class="ck-kind ck-{kind}" title="{esc(why)}">{kind}</span>' if kind else ""
        rows.append(f"<tr><td class='tk-role'>.{esc(c)}</td><td class='tk-hex'>{n}</td>"
                    f"<td class='tk-hex'>{tag}</td></tr>")
    return ('<table class="tk-tbl"><thead><tr><th>class</th><th>screens</th><th>if zero</th>'
            "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def screen_links(screens):
    if not screens:
        return '<p class="tk-note">Not on a painted screen yet.</p>'
    return '<div class="ck-screens">' + "".join(
        f'<a href="../ui-visual/{s}">{esc(s[:-5])}</a>' for s in screens) + "</div>"


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - {label}</title>
{theme_boot}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="{name}">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>{label}</h1>
    <p>{note}</p>
    <div class="tk-badges">
      <span class="tk-badge">components/{name}.css</span>
      <span class="tk-badge">{rules} rules</span>
      <span class="tk-badge">{nclasses} classes</span>
      <span class="tk-badge">{nscreens} screens</span>
    </div>
  </header>

  <section class="tk-sec" id="live">
    <h2 data-n="01">Live</h2>
    <p class="tk-note">The component in the markup it ships with, quoted from the frozen kit, inside
    the product's own wrapper and painted by <code>components/index.css</code> alone. Each frame is a
    page of its own, so the width under the title is a real viewport and the media queries answer to
    it.</p>
    {live}
  </section>
{inside}
  <section class="tk-sec" id="states">
    <h2 data-n="03">States</h2>
    <p class="tk-note">Hover and focus are not faked here with a stand class. The frames above are
    live, so hover them; what follows is what the file says will move.</p>
    {states}
  </section>

  <section class="tk-sec" id="roles">
    <h2 data-n="04">Roles it reads</h2>
    <p class="tk-note">Colour comes in only through these. Change one on
    <a href="tokens.html">the token page</a> and it changes here and on every screen at once.</p>
    {roles}
  </section>

  <section class="tk-sec" id="classes">
    <h2 data-n="05">Classes</h2>
    <p class="tk-note">Every class this file styles, and how many of the {nuv} painted screens carry
    it. A zero is not automatically dead: the last column says whether the class is built at runtime,
    shown only in the kit, a leftover of the grey wireframes, used by a course page, or genuinely
    used by nothing. Only the last kind is a deletion candidate, and they are collected in
    <a href="coverage.html">coverage</a>.</p>
    {classes}
  </section>

  <section class="tk-sec" id="screens">
    <h2 data-n="06">Where it stands</h2>
    {screens}
  </section>

  <section class="tk-sec" id="css">
    <h2 data-n="07">The file</h2>
    <p class="tk-note">To change this component, edit <code>components/{name}.css</code>. To change a
    value it reads, edit the role in <code>components/tokens.css</code>.</p>
    <details class="ck-src"><summary>components/{name}.css</summary><pre>{css}</pre></details>
  </section>
</main>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""

built = []
for path in sorted(COMP.glob("*.css")):
    name = path.stem
    # index is the entry point, tokens are the values, fonts are eighteen
    # @font-face rules that style nothing: none of the three is a component with
    # a stand, and gate 2 has said so about all three since step 8. This loop
    # only knew about two, so re-running it built ui-kit/fonts.html, a page whose
    # own quoted css names a font host and fails gate 20.
    if name in ("index", "tokens", "fonts"):
        continue
    c = parse_component(name)
    page = PAGE.format(
        theme_boot=THEME_BOOT, name=name, label=LABEL.get(name, name), note=esc(NOTE.get(name, (
            "Every rule that paints this component, in one file. "
            "Colour through a role, geometry straight from a primitive."))),
        rules=c["rules"], nclasses=len(c["classes"]), nscreens=len(c["screens"]),
        nuv=len(uv_classes),
        live=live(name), inside=elsewhere(name), states=states_table(c["states"]),
        roles=role_swatches(c["roles"]), classes=class_table(c["classes"]),
        screens=screen_links(c["screens"]), css=esc(c["css"]))
    (KIT / (name + ".html")).write_text(page, encoding="utf-8")
    built.append((name, c))

# ------------------------------------------------------------------ registry --
entries = []
for group, names in GROUPS:
    for n in names:
        if n in ("tokens", "icons"):
            entries.append((group, n, n + ".html", LABEL[n]))
        elif (COMP / (n + ".css")).exists():
            entries.append((group, n, n + ".html", LABEL.get(n, n)))
extra = [n for n, _ in built if n not in [e[1] for e in entries]]
for n in sorted(extra):
    entries.append(("Unfiled", n, n + ".html", LABEL.get(n, n)))

nav = ["""/* ui-kit/_nav.js - the ONE registry of stand pages.

   It renders two things from the same list: the cards on overview.html and the
   kit-only side panel on every stand page. A component without a line here does
   not exist as far as the system is concerned. Own namespace (window.KIT_NAV) so
   it never collides with the course roadmap renderer in the repo root.
   Generated by _gen_component_pages.py. No em dash. */
window.KIT_DOORS = %s;
window.KIT_DOCS = %s;
window.KIT_NAV = [""" % (json.dumps([{"label": a, "file": b, "blurb": d}
                                     for a, b, d in FOUNDATION_DOORS]),
                         json.dumps([{"name": "doc-" + s, "file": s + ".html",
                                      "label": lab, "blurb": blurb}
                                     for s, lab, blurb in DOC_PAGES]))]
for g, n, f, l in entries:
    nav.append('  {group: %s, name: %s, file: %s, label: %s},'
               % (json.dumps(g), json.dumps(n), json.dumps(f), json.dumps(l)))
nav.append("""];

%(REVEAL_BODY)s

(function () {
  var host = document.querySelector('[data-kit-nav]');
  var current = document.body.getAttribute('data-kit-page') || '';
  if (host) {
    // The back arrow leaves the system for the thing the system is for: the
    // painted screens. Overview is not a component, so it is not in the
    // registry below; it is its own row above the first group, the way the
    // screens have an Overview row above their families.
    var h = ['<a href="../ui-visual/overview.html" class="sidebar-back"><span class="bk-arrow" aria-hidden="true">&larr;</span> Painted screens</a>',
             '<div class="sidebar-brand"><div class="sidebar-project-name">Design system</div></div>',
             // the switch acts on the page, not on the tree, so it sits above the
             // tree: the panel is 40 rows long and a control at its foot needs scrolling
             '<button type="button" class="theme-switch" aria-pressed="false"><span class="ts-swatches" aria-hidden="true"><span class="ts-sw ts-dark"></span><span class="ts-sw ts-light"></span></span><span class="ts-label">Vault</span></button>',
             '<nav class="sidebar-nav" aria-label="Design system">',
             '<a href="overview.html" class="sidebar-page-link' + (current === 'overview' ? ' active' : '') + '">Overview</a>'];
    // The group you are IN is marked as well as the page you are ON. The tree is
    // 45 rows in a panel that shows about 25, so on most pages the brass row is
    // below the fold and the panel opens saying nothing about where you are. The
    // screens tree has always marked the family; this is the same answer, and it
    // is what makes the two panels one vocabulary rather than two.
    var here = null;
    window.KIT_NAV.forEach(function (e) { if (e.name === current) here = e.group; });
    var group = null;
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== group) {
        group = e.group;
        h.push('<div class="sidebar-divider' + (group === here ? ' active' : '') +
               '">' + group + '</div>');
      }
      h.push('<a href="' + e.file + '" class="sidebar-page-link' + (e.name === current ? ' active' : '') + '">' + e.label + '</a>');
      if (e.name === 'tokens') {
        h.push('<div class="sidebar-sub">');
        window.KIT_DOORS.forEach(function (d) {
          h.push('<a href="' + d.file + '" class="sidebar-sub-link">' + d.label + '</a>');
        });
        h.push('</div>');
      }
    });
    // The documents are the last group and not the first, because they are the
    // reasoning and the components are the thing. They are pages of the vitrine
    // like any other, so they are rows in the same tree: a link that leaves for
    // a .md file is a link out of the browser.
    var inDocs = window.KIT_DOCS.some(function (d) { return d.name === current; });
    h.push('<div class="sidebar-divider' + (inDocs ? ' active' : '') + '">The reasoning</div>');
    window.KIT_DOCS.forEach(function (d) {
      h.push('<a href="' + d.file + '" class="sidebar-page-link' + (d.name === current ? ' active' : '') + '">' + d.label + '</a>');
    });
    h.push('</nav>');
    h.push('<div class="sidebar-note">The kit itself: <a href="kit.html">kit.html</a>, <a href="shell.html">shell.html</a>, <a href="selftest.html">self test</a></div>');
    host.innerHTML = h.join('');
    // the tree exists only now, so the reveal happens here and not on load
    %(REVEAL_CALL)s
  }
  var cards = document.getElementById('kitCards');
  if (cards) {
    var g = null, out = [];
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== g) { g = e.group; out.push('</div><h3 class="tk-subh">' + g + '</h3><div class="ck-cards">'); }
      var thumb = window.KIT_THUMBS && window.KIT_THUMBS[e.name];
      out.push('<a class="ck-card" href="' + e.file + '">' +
               (thumb ? '<span class="ck-thumb"><iframe src="specimens/' + thumb.id +
                        '.html" width="' + thumb.w + '" height="' + thumb.h +
                        '" style="transform:scale(' + thumb.s + ')" loading="lazy" tabindex="-1" aria-hidden="true" title=""></iframe></span>' : '') +
               '<b>' + e.label + '</b><code>' +
               (e.name === 'tokens' ? 'components/tokens.css'
                : e.name === 'icons' ? 'ui-kit/icons.html' : 'components/' + e.name + '.css') +
               '</code></a>');
    });
    cards.innerHTML = (out.join('') + '</div>').replace(/^<\\/div>/, '');
  }
  var doors = document.getElementById('kitDoors');
  if (doors) {
    doors.innerHTML = window.KIT_DOORS.map(function (d) {
      return '<a class="ck-card" href="' + d.file + '"><b>' + d.label + '</b><code>' + d.blurb + '</code></a>';
    }).join('');
  }
  var docs = document.getElementById('kitDocs');
  if (docs) {
    docs.innerHTML = window.KIT_DOCS.map(function (d) {
      return '<a class="ck-card" href="' + d.file + '"><b>' + d.label + '</b><code>' + d.blurb + '</code></a>';
    }).join('');
  }
  var sb = document.querySelector('[data-kit-nav]'), ov = document.getElementById('rmOverlay'), tg = document.getElementById('rmToggle');
  if (sb && ov && tg) {
    var o = function () { sb.classList.add('open'); ov.classList.add('open'); },
        c = function () { sb.classList.remove('open'); ov.classList.remove('open'); };
    tg.addEventListener('click', o); ov.addEventListener('click', c);
  }
})();
""" % {"REVEAL_BODY": REVEAL_BODY, "REVEAL_CALL": REVEAL_CALL})
(KIT / "_nav.js").write_text("\n".join(nav), encoding="utf-8")

# ------------------------------------------------------------------ frames ---
(KIT / "_frames.js").write_text("""/* ui-kit/_frames.js - the parent half of the specimen frame handshake.

   A specimen is a page of its own, so the vitrine cannot measure it by reading
   its document: under file:// every document has its own opaque origin. The
   specimen posts its height instead, which crosses origins by design. The frame
   is matched by identity (contentWindow), not by the origin string, because
   from file:// that string is "null" for everyone. No em dash. */
(function () {
  /* A specimen is rendered at the width it declares, because that width is what
     its media queries answer to. When the column is narrower, the frame is
     scaled down rather than squeezed: the layout stays the layout, and the
     label says what it is being shown at. */
  function fit(f) {
    var box = f.parentElement, w = +f.getAttribute('width');
    /* The available width is the figure's, not the box's: the box is about to be
       resized to whatever we decide, so measuring it would measure our own
       previous answer. */
    var avail = box.parentElement.clientWidth;
    var s = Math.min(1, avail / w);
    var h = parseFloat(f.style.height || f.getAttribute('height'));
    f.style.transformOrigin = '0 0';
    f.style.transform = s < 1 ? 'scale(' + s + ')' : 'none';
    /* The border hugs the specimen instead of leaving a strip of empty canvas. */
    box.style.width = Math.ceil(w * s) + 'px';
    box.style.height = Math.ceil(h * s) + 'px';
    var tag = box.parentElement.querySelector('.ck-zoom');
    if (tag) { tag.textContent = s < 1 ? Math.round(s * 100) + '%' : ''; tag.hidden = s >= 1; }
  }

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.specimen || !(d.height > 0)) return;
    var frames = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        frames[i].style.height = d.height + 'px';
        fit(frames[i]);
        return;
      }
    }
  });
  window.addEventListener('resize', function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) fit(f[i]);
  });
  /* A frame that finished before this script ran has already spoken and will
     not speak again, so ask it once it is there. */
  var ask = function (f) {
    try { f.contentWindow.postMessage({ping: true}, '*'); } catch (err) {}
  };
  var all = function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) { ask(f[i]); f[i].addEventListener('load', ask.bind(null, f[i])); }
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all);
  else all();
  window.addEventListener('load', all);
})();
""", encoding="utf-8")

# ---------------------------------------------------------------------- hub ---
THUMB_W = 236
thumbs = {}
for s in SPECIMENS:
    if s["component"] in thumbs:
        continue
    w = s.get("width", 900)
    scale = round(THUMB_W / w, 4)
    thumbs[s["component"]] = {"id": s["id"], "w": w, "h": int(140 / scale), "s": scale}

total_rules = sum(c["rules"] for _, c in built)
hub = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Design system</title>
{THEME_BOOT}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="overview">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>The system</h1>
    <p>Two levels of tokens and {len(built)} component files. The code lives in
    <code>components/</code> and is what a screen links; these pages are the vitrine, and they link
    the same <code>components/index.css</code> the product does, so nothing here can drift from what
    ships.</p>
    <div class="tk-badges">
      <span class="tk-badge">{len(built)} components</span>
      <span class="tk-badge">{total_rules} rules</span>
      <span class="tk-badge">{len(SPECIMENS)} specimens</span>
      <span class="tk-badge">one entry point</span>
    </div>
    <div class="tk-theme">{THEME_BUTTON_INLINE}<span class="tk-theme-note">The whole product, on the
      other ground. Only roles move; not one primitive is redefined. Section 3 of
      <code>components/tokens.css</code> is the entire theme.</span></div>
    <div class="tk-jump"><a href="tokens.html">Tokens</a><a href="icons.html">Icons</a>
      <a href="kit.html">Frozen kit</a><a href="selftest.html">Self test</a>
      <a href="../ui-visual/overview.html">Painted screens</a></div>
  </header>

  <section class="tk-sec" id="foundations">
    <h2 data-n="01">Foundations</h2>
    <p class="tk-note">Colour, material, geometry, type and motion are one page, because they are one
    file: <code>components/tokens.css</code> generates all of it. These are the doors into it.</p>
    <div class="ck-cards" id="kitDoors"></div>
  </section>

  <section class="tk-sec" id="docs">
    <h2 data-n="02">The reasoning</h2>
    <p class="tk-note">Why the system is shaped like this, what it was read out of, and what each
    part reaches. Rendered from <code>ui-kit/docs/</code> by <code>ui-kit/_gen_docs.py</code>; the
    markdown stays the source.</p>
    <div class="ck-cards" id="kitDocs"></div>
  </section>

  <section class="tk-sec" id="cards">
    <h2 data-n="03">Every file, every page</h2>
    <p class="tk-note">One component is one css file, one page here and one line in the registry.
    Missing any of the three means the component does not exist yet.</p>
    <div id="kitCards"></div>
  </section>
</main>

<script>window.KIT_THUMBS = {json.dumps(thumbs)};</script>
<script src="_nav.js"></script>
</body>
</html>
"""
(KIT / "overview.html").write_text(hub, encoding="utf-8")

# ----------------------------------------------------------------- coverage --
rows = []
buckets = {}
for name, c in built:
    mine = [s for s in SPECIMENS if s["component"] == name]
    inside = [s for s in SPECIMENS if name in s.get("also", [])]
    rows.append("| %s | %d | %s | %d | %d | %d |" % (
        name, len(mine), ", ".join(s["id"] for s in mine) or "-",
        len(inside), len(c["owned"]), len(c["screens"])))
    for cls in c["classes"]:
        kind, why = where(cls)
        if kind:
            buckets.setdefault(kind, []).append((cls, name, why))

ORDER = [("unused", "Deletion candidates", "Styled, and carried by no element in the repo: not by a "
          "painted screen, not by the kit, not by a wireframe, not by a course page, and not by any "
          "script. Nothing is removed yet. The screens still carry their own inline style and only "
          "move onto components/index.css in step 5, so the measurement is not final until then; "
          "step 7 is the pass that acts on this list."),
         ("wireframe", "Carried only by the grey tree", "Dead, and this section used to say the "
          "opposite: it called them the wireframe version of a block the paint replaced and said "
          "removing them needed the markup gone from wireframes/ first. It does not. wireframes/ "
          "carries its own inline grey-box css and never links index.css, so no rule in components/ "
          "has ever applied to it, and a class carried only there is a class this sheet does not "
          "have. Step 7e deleted the ones that were left and took wireframes/ out of gate 14's "
          "markup scan, which had been keeping them alive."),
         ("docs", "Used only by a course page", "Carried by a page in ia/, concept/, research/, "
          "voice/ or user-research/. Those pages have their own inline styles and do not load the "
          "system, so the rule here reaches nothing."),
         ("kit", "Shown in the kit, not in the product", "A real component the painted screens have "
          "not adopted. An offer, not debris. Do not delete without deciding against it first."),
         ("runtime", "Built or toggled at runtime", "Never written into a file. Deleting any of "
          "these breaks a screen silently, because the grep that says they are unused is wrong.")]

sections = []
for kind, title, blurb in ORDER:
    items = sorted(buckets.get(kind, []))
    sections.append("### %s (%d)\n\n%s\n\n| class | file | why |\n|---|---|---|\n%s\n"
                    % (title, len(items), blurb,
                       "\n".join("| `.%s` | %s.css | %s |" % (c, f, w) for c, f, w in items)
                       or "| - | - | none |"))

(KIT / "docs" / "coverage.md").write_text("""# Vitrine coverage

Generated by `ui-kit/_gen_component_pages.py`. Do not edit by hand.

What each column means: **own** is how many specimens the component's page renders itself, **inside**
is how many other specimens contain it and link to it instead of repeating it, **classes** is how many classes the
file OWNS (a class it styles with the fewest ancestors; a class it only reaches through someone
else's belongs to that someone else), and **screens** is how many of the %d painted screens carry at
least one of them. Counting every class a file merely mentions is what made this column read 76 for
thirty-four of thirty-six components, a market-depth panel included.

A component with 0 own specimens does not exist as far as the vitrine is concerned, and the build
says so. No em dash.

| component | own | specimens | inside | classes | screens |
|---|---|---|---|---|---|
%s

%d specimens over %d components.

---

## Classes the painted screens do not carry

Every class styled in `components/` that no `ui-visual` screen puts on an element, sorted by what
that actually means. The Classes table on each component page shows the same verdict per row.

%s
""" % (len(uv_classes), "\n".join(rows), len(SPECIMENS), len(built), "\n".join(sections)),
    encoding="utf-8")

# ------------------------------------------------- the css header line -------
# The `Classes:` and `Stands on:` lines in each component file used to be prose
# someone typed once. They said the truth and coverage.md said 76, and a reader
# had no way to know which to believe. They are written from the same OWNER map
# now, so there is one computation and two places that read it. Idempotent: the
# line is replaced, never appended, and a file that carries neither is left alone
# (base.css and course-chrome.css describe themselves in a sentence instead).
hdr_written = 0
for name, c in built:
    path = COMP / (name + ".css")
    text = path.read_text(encoding="utf-8")
    if "*/" not in text:
        continue
    head, rest = text[:text.index("*/") + 2], text[text.index("*/") + 2:]
    before = head
    if "Classes:" in head:
        head = re.sub(r"Classes:[^\n]*",
                      "Classes: %s." % ", ".join("." + x for x in c["owned"]), head, count=1)
    if "Stands on:" in head:
        shown = ", ".join(c["screens"][:5]) + (", ..." if len(c["screens"]) > 5 else "")
        head = re.sub(r"Stands on:[^\n]*",
                      "Stands on: %d ui-visual screens (%s)" % (len(c["screens"]), shown or "none"),
                      head, count=1)
    if head != before:
        path.write_text(head + rest, encoding="utf-8")
        hdr_written += 1

print("built %d component pages + overview.html + _nav.js + _frames.js + docs/coverage.md, %d css headers" % (len(built), hdr_written))
missing = [n for n, _ in built if not any(s["component"] == n for s in SPECIMENS)]
if missing:
    print("no specimen of its own:", ", ".join(missing))
