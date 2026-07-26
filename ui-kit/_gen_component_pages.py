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

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
KIT = ROOT / "ui-kit"
UV = ROOT / "ui-visual"

SPECIMENS = json.loads((KIT / "specimens" / "index.json").read_text(encoding="utf-8"))
TOKENS = (COMP / "tokens.css").read_text(encoding="utf-8")
SEM = set(re.findall(r"(--[\w-]+)\s*:", TOKENS[TOKENS.index("2. SEMANTIC"):]))

GROUPS = [
    ("Foundations", ["tokens", "icons", "base", "course-chrome"]),
    ("Navigation and chrome", ["header", "catnav", "bottomnav", "tabs", "footer", "trustbar"]),
    ("Browse: feed and cards", ["feed", "card", "oddsbar", "yesno", "options", "hero", "seo-plate",
                                "loadmore", "filters"]),
    ("Event Detail", ["event-detail", "chart", "betpanel", "market", "comments", "bets-table", "related"]),
    ("Forms, dialogs and inputs", ["button", "input", "dialog", "hiw-dialog", "signin", "notice"]),
    ("Feedback and states", ["state-block", "skeleton", "toast", "outcome-dialog"]),
    ("Profile and account", ["profile", "position", "account"]),
    ("System", ["cookie-consent"]),
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
    "dialog": "Shared dialog", "hiw-dialog": "How-it-works dialog", "signin": "Sign in dialog",
    "notice": "Notices and banners", "state-block": "State block", "skeleton": "Skeletons",
    "toast": "Toasts", "outcome-dialog": "Win and loss overlays",
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


# ---- how many painted screens carry each class -----------------------------
uv_classes = {}
for f in sorted(glob.glob(str(UV / "*.html"))):
    body = re.sub(r"<style[^>]*>.*?</style>", "", open(f, encoding="utf-8").read(), flags=re.S)
    cs = set()
    for m in re.finditer(r'class="([^"]*)"', body):
        cs.update(m.group(1).split())
    uv_classes[os.path.basename(f)] = cs

# ---- every class any component file declares, for the orphan check ----------
declared = set()
for path in COMP.glob("*.css"):
    if path.stem in ("index", "tokens"):
        continue
    body = re.sub(r"url\([^)]*\)", "", path.read_text(encoding="utf-8"))
    declared.update(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", body))


def parse_component(name):
    css = (COMP / (name + ".css")).read_text(encoding="utf-8")
    head = css[:css.index("*/") + 2] if "*/" in css else ""
    body = css[len(head):].strip()
    roles = sorted({m for m in re.findall(r"var\((--[\w-]+)\)", body) if m in SEM})
    classes = sorted({c for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)", re.sub(r"url\([^)]*\)", "", body))})
    rules = len(re.findall(r"\{", body))
    screens = sorted([p for p, cs in uv_classes.items() if cs & set(classes)])
    states = []
    for m in re.finditer(r"([^{}\n][^{}]*)\{([^{}]*)\}", body):
        sel = " ".join(m.group(1).split())
        if STATE_PAT.search(sel) and not sel.startswith("@"):
            states.append((sel, m.group(2).strip()))
    return dict(css=css, body=body, roles=roles, classes=classes, rules=rules,
                screens=screens, states=states)


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
            f'<div class="ck-frame"><iframe data-specimen="{s["id"]}" src="specimens/{s["id"]}.html" '
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
        rows.append(f"<tr><td class='tk-role'>.{esc(c)}</td><td class='tk-hex'>{n}</td></tr>")
    return ('<table class="tk-tbl"><thead><tr><th>class</th><th>screens</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table>")


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
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="{name}">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<div class="tk-wrap">
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
    it. A class on no screen is either a state the markup toggles or a candidate for deletion.</p>
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
</div>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""

built = []
for path in sorted(COMP.glob("*.css")):
    name = path.stem
    if name in ("index", "tokens"):
        continue
    c = parse_component(name)
    page = PAGE.format(
        name=name, label=LABEL.get(name, name), note=esc(NOTE.get(name, (
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
window.KIT_NAV = [""" % json.dumps([{"label": a, "file": b, "blurb": d}
                                    for a, b, d in FOUNDATION_DOORS])]
for g, n, f, l in entries:
    nav.append('  {group: %s, name: %s, file: %s, label: %s},'
               % (json.dumps(g), json.dumps(n), json.dumps(f), json.dumps(l)))
nav.append("""];

(function () {
  var host = document.querySelector('[data-kit-nav]');
  var current = document.body.getAttribute('data-kit-page') || '';
  if (host) {
    var h = ['<a href="overview.html" class="sidebar-back"><span class="bk-arrow" aria-hidden="true">&larr;</span> Whole system</a>',
             '<div class="sidebar-brand"><div class="sidebar-project-name">Design system</div></div>',
             '<nav class="sidebar-nav">'];
    var group = null;
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== group) { group = e.group; h.push('<div class="sidebar-divider">' + group + '</div>'); }
      h.push('<a href="' + e.file + '" class="sidebar-page-link' + (e.name === current ? ' active' : '') + '">' + e.label + '</a>');
      if (e.name === 'tokens') {
        h.push('<div class="sidebar-sub">');
        window.KIT_DOORS.forEach(function (d) {
          h.push('<a href="' + d.file + '" class="sidebar-sub-link">' + d.label + '</a>');
        });
        h.push('</div>');
      }
    });
    h.push('</nav>');
    h.push('<div class="sidebar-note">The kit itself: <a href="kit.html">kit.html</a>, <a href="shell.html">shell.html</a>, <a href="selftest.html">self test</a></div>');
    host.innerHTML = h.join('');
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
  var sb = document.querySelector('[data-kit-nav]'), ov = document.getElementById('rmOverlay'), tg = document.getElementById('rmToggle');
  if (sb && ov && tg) {
    var o = function () { sb.classList.add('open'); ov.classList.add('open'); },
        c = function () { sb.classList.remove('open'); ov.classList.remove('open'); };
    tg.addEventListener('click', o); ov.addEventListener('click', c);
  }
})();
""")
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
    var s = Math.min(1, box.clientWidth / w);
    f.style.transformOrigin = '0 0';
    f.style.transform = s < 1 ? 'scale(' + s + ')' : 'none';
    box.style.height = Math.ceil(parseFloat(f.style.height || f.getAttribute('height')) * s) + 'px';
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
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="overview">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<div class="tk-wrap">
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
    <div class="tk-jump"><a href="tokens.html">Tokens</a><a href="icons.html">Icons</a>
      <a href="kit.html">Frozen kit</a><a href="selftest.html">Self test</a>
      <a href="../ui-visual/event-feed.html">Painted screens</a></div>
  </header>

  <section class="tk-sec" id="foundations">
    <h2 data-n="01">Foundations</h2>
    <p class="tk-note">Colour, material, geometry, type and motion are one page, because they are one
    file: <code>components/tokens.css</code> generates all of it. These are the doors into it.</p>
    <div class="ck-cards" id="kitDoors"></div>
  </section>

  <section class="tk-sec" id="cards">
    <h2 data-n="02">Every file, every page</h2>
    <p class="tk-note">One component is one css file, one page here and one line in the registry.
    Missing any of the three means the component does not exist yet.</p>
    <div id="kitCards"></div>
  </section>
</div>

<script>window.KIT_THUMBS = {json.dumps(thumbs)};</script>
<script src="_nav.js"></script>
</body>
</html>
"""
(KIT / "overview.html").write_text(hub, encoding="utf-8")

# ----------------------------------------------------------------- coverage --
rows = []
for name, c in built:
    mine = [s for s in SPECIMENS if s["component"] == name]
    inside = [s for s in SPECIMENS if name in s.get("also", [])]
    rows.append("| %s | %d | %s | %d | %d | %d |" % (
        name, len(mine), ", ".join(s["id"] for s in mine) or "-",
        len(inside), len(c["classes"]), len(c["screens"])))

(KIT / "docs" / "coverage.md").write_text("""# Vitrine coverage

Generated by `ui-kit/_gen_component_pages.py`. Do not edit by hand.

What each column means: **own** is how many specimens the component's page renders itself, **inside**
is how many other specimens contain it and link to it instead of repeating it, **classes** is what the
css file styles, **screens** is how many of the %d painted screens carry at least one of those classes.

A component with 0 own specimens does not exist as far as the vitrine is concerned, and the build
says so. No em dash.

| component | own | specimens | inside | classes | screens |
|---|---|---|---|---|---|
%s

%d specimens over %d components.
""" % (len(uv_classes), "\n".join(rows), len(SPECIMENS), len(built)), encoding="utf-8")

print("built %d component pages + overview.html + _nav.js + _frames.js + docs/coverage.md" % len(built))
missing = [n for n, _ in built if not any(s["component"] == n for s in SPECIMENS)]
if missing:
    print("no specimen of its own:", ", ".join(missing))
