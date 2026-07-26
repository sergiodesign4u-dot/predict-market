#!/usr/bin/env python3
"""Build one stand page per component in ui-kit/, plus the hub and the registry.

For every components/<name>.css it writes ui-kit/<name>.html carrying:
  - the component live, in the markup it actually ships with (specimens lifted
    from the frozen ui-kit/kit.html, so nothing is invented for the stand),
  - the semantic roles the file reads, each with a swatch,
  - the classes it owns and how many painted screens carry each one,
  - the screens in ui-visual/ where the component stands, as links,
  - the CSS itself, so the file and the page never drift apart.

Also writes ui-kit/_nav.js (the one registry of stand pages) and
ui-kit/overview.html (the hub of cards). Idempotent: re-run after any change to
components/ or after re-extracting ui-kit/_specimens.json.

    python3 ui-kit/_gen_component_pages.py
"""
import json, os, re, glob, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
KIT = ROOT / "ui-kit"
UV = ROOT / "ui-visual"

SPEC = json.loads(json.load(open(KIT / "_specimens.json", encoding="utf-8"))) \
    if (KIT / "_specimens.json").exists() else {}

TOKENS = (COMP / "tokens.css").read_text(encoding="utf-8")
SEM = set(re.findall(r"(--[\w-]+)\s*:", TOKENS[TOKENS.index("2. SEMANTIC"):]))

GROUPS = [
    ("Foundations", ["tokens", "base", "course-chrome"]),
    ("Navigation and chrome", ["header", "catnav", "bottomnav", "tabs", "footer", "trustbar"]),
    ("Browse: feed and cards", ["feed", "card", "oddsbar", "yesno", "options", "hero", "seo-plate",
                                "loadmore", "filters"]),
    ("Event Detail", ["event-detail", "chart", "betpanel", "market", "comments", "bets-table", "related"]),
    ("Forms, dialogs and inputs", ["button", "input", "dialog", "hiw-dialog", "signin", "notice"]),
    ("Feedback and states", ["state-block", "skeleton", "toast", "outcome-dialog", "notifications"]),
    ("Profile and account", ["profile", "position", "account"]),
    ("System", ["cookie-consent"]),
]
LABEL = {
    "tokens": "Tokens", "base": "Base and page frame", "course-chrome": "Course chrome",
    "header": "App header", "catnav": "Category nav", "bottomnav": "Bottom nav", "tabs": "Tabs",
    "footer": "Footer", "trustbar": "Trust bar and cards", "feed": "Feed layout", "card": "Event card",
    "oddsbar": "Odds bar", "yesno": "YES / NO buttons", "options": "Outcome rows", "hero": "Featured hero",
    "seo-plate": "SEO plate", "loadmore": "Load more", "filters": "Sort and filters",
    "event-detail": "Event Detail layout", "chart": "Price chart", "betpanel": "Bet panel and dock",
    "market": "AMM market panel", "comments": "Comments", "bets-table": "Bets and activity",
    "related": "Related events", "button": "Buttons", "input": "Fields and amounts",
    "dialog": "Shared dialog", "hiw-dialog": "How-it-works dialog", "signin": "Sign in dialog",
    "notice": "Notices and banners", "state-block": "State block", "skeleton": "Skeletons",
    "toast": "Toasts", "outcome-dialog": "Win and loss overlays", "notifications": "Notifications",
    "profile": "Profile identity", "position": "Position rows", "account": "Account bars",
    "cookie-consent": "Cookie consent",
}
NOTE = {
    "base": "Not a component: the page frame, the reset, the shared utilities and the neutralisation "
            "block that hides the grey-box scaffolding the wireframes left behind.",
    "course-chrome": "Not product: the roadmap sidebar every page of this repo carries. It ships with "
                     "the system only because the painted screens render it.",
    "tokens": "The values behind everything else. Its own page is tokens.html.",
}

# ---- how many painted screens carry each class -----------------------------
uv_classes = {}
for f in sorted(glob.glob(str(UV / "*.html"))):
    body = re.sub(r"<style[^>]*>.*?</style>", "", open(f, encoding="utf-8").read(), flags=re.S)
    cs = set()
    for m in re.finditer(r'class="([^"]*)"', body):
        cs.update(m.group(1).split())
    uv_classes[os.path.basename(f)] = cs


def esc(s):
    return html.escape(s, quote=False)


def parse_component(name):
    css = (COMP / (name + ".css")).read_text(encoding="utf-8")
    head = css[:css.index("*/") + 2] if "*/" in css else ""
    body = css[len(head):].strip()
    roles = sorted({m for m in re.findall(r"var\((--[\w-]+)\)", body) if m in SEM})
    classes = sorted({c for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)", re.sub(r"url\([^)]*\)", "", body))})
    rules = len(re.findall(r"\{", body))
    screens = sorted([p for p, cs in uv_classes.items() if cs & set(classes)])
    return dict(css=css, head=head, body=body, roles=roles, classes=classes, rules=rules, screens=screens)


SCENE_WRAP = {"card": "grid", "options": "card", "oddsbar": "card", "yesno": "card"}


def scene(name, spec):
    if not spec["specimens"]:
        return ('<p class="tk-note">No standalone specimen: this file styles a page-level block. '
                'Open it on a screen below.</p>')
    out = []
    for i, s in enumerate(spec["specimens"], 1):
        big = len(s) > 9000
        w = SCENE_WRAP.get(name)
        inner = f'<div class="{w}">{s}</div>' if w and w not in s[:60] else s
        out.append(f'<div class="ck-scene"><span class="ck-scene-lbl">specimen {i}</span>'
                   f'<div class="ck-stage{" ck-stage-wide" if big else ""}">{inner}</div></div>')
    return "\n".join(out)


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
    <p class="tk-note">The component in the markup it ships with, lifted from the frozen kit so the
    stand cannot drift from the product. Painted by <code>components/index.css</code>, nothing else.</p>
    {scene}
  </section>

  <section class="tk-sec" id="roles">
    <h2 data-n="02">Roles it reads</h2>
    <p class="tk-note">Colour comes in only through these. Change one on
    <a href="tokens.html">the token page</a> and it changes here and on every screen at once.</p>
    {roles}
  </section>

  <section class="tk-sec" id="classes">
    <h2 data-n="03">Classes</h2>
    <p class="tk-note">Every class this file styles, and how many of the 76 painted screens carry it.
    A class on no screen is either a state the markup toggles or a candidate for deletion in step 7.</p>
    {classes}
  </section>

  <section class="tk-sec" id="screens">
    <h2 data-n="04">Where it stands</h2>
    {screens}
  </section>

  <section class="tk-sec" id="css">
    <h2 data-n="05">The file</h2>
    <p class="tk-note">To change this component, edit <code>components/{name}.css</code>. To change a
    value it reads, edit the role in <code>components/tokens.css</code>.</p>
    <details class="ck-src"><summary>components/{name}.css</summary><pre>{css}</pre></details>
  </section>
</div>

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
    spec = SPEC.get(name, {"specimens": []})
    page = PAGE.format(
        name=name, label=LABEL.get(name, name), note=esc(NOTE.get(name, (
            "Every rule that paints this component, in one file. "
            "Colour through a role, geometry straight from a primitive."))),
        rules=c["rules"], nclasses=len(c["classes"]), nscreens=len(c["screens"]),
        scene=scene(name, spec), roles=role_swatches(c["roles"]),
        classes=class_table(c["classes"]), screens=screen_links(c["screens"]),
        css=esc(c["css"]))
    (KIT / (name + ".html")).write_text(page, encoding="utf-8")
    built.append((name, c, spec))

# ------------------------------------------------------------------ registry --
entries = []
for group, names in GROUPS:
    for n in names:
        if n == "tokens":
            entries.append((group, n, "tokens.html", LABEL[n]))
        elif (COMP / (n + ".css")).exists():
            entries.append((group, n, n + ".html", LABEL.get(n, n)))
extra = [n for n, _, _ in built if n not in [e[1] for e in entries]]
for n in sorted(extra):
    entries.append(("Unfiled", n, n + ".html", LABEL.get(n, n)))

nav = ["""/* ui-kit/_nav.js - the ONE registry of stand pages.

   It renders two things from the same list: the cards on overview.html and the
   kit-only side panel on every stand page. A component without a line here does
   not exist as far as the system is concerned. Own namespace (window.KIT_NAV) so
   it never collides with the course roadmap renderer in the repo root.
   No em dash. */
window.KIT_NAV = ["""]
for g, n, f, l in entries:
    nav.append('  {group: %s, name: %s, file: %s, label: %s},' % (json.dumps(g), json.dumps(n), json.dumps(f), json.dumps(l)))
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
    });
    h.push('</nav>');
    h.push('<div class="sidebar-note">The kit itself: <a href="kit.html">kit.html</a>, <a href="shell.html">shell.html</a></div>');
    host.innerHTML = h.join('');
  }
  var cards = document.getElementById('kitCards');
  if (cards) {
    var g = null, out = [];
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== g) { g = e.group; out.push('</div><h3 class="tk-subh">' + g + '</h3><div class="ck-cards">'); }
      out.push('<a class="ck-card" href="' + e.file + '"><b>' + e.label + '</b><code>' +
               (e.name === 'tokens' ? 'components/tokens.css' : 'components/' + e.name + '.css') + '</code></a>');
    });
    cards.innerHTML = (out.join('') + '</div>').replace(/^<\\/div>/, '');
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

# ---------------------------------------------------------------------- hub ---
total_rules = sum(c["rules"] for _, c, _ in built)
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
      <span class="tk-badge">one entry point</span>
    </div>
    <div class="tk-jump"><a href="tokens.html">Tokens</a><a href="kit.html">Frozen kit</a>
      <a href="shell.html">Shell</a><a href="../ui-visual/event-feed.html">Painted screens</a></div>
  </header>

  <section class="tk-sec" id="cards">
    <h2 data-n="01">Every file, every page</h2>
    <p class="tk-note">One component is one css file, one page here and one line in the registry.
    Missing any of the three means the component does not exist yet.</p>
    <div id="kitCards"></div>
  </section>
</div>

<script src="_nav.js"></script>
</body>
</html>
"""
(KIT / "overview.html").write_text(hub, encoding="utf-8")

print("built %d component pages + overview.html + _nav.js" % len(built))
missing = [n for n, _, s in built if not s["specimens"]]
if missing:
    print("no live specimen for:", ", ".join(missing))
