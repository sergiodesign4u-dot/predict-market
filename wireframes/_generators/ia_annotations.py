#!/usr/bin/env python3
"""
ia_annotations.py  -  Extract wireframe annotations into IA visualization pages.

Two responsibilities (run in order):
  1. build_ia_pages()  -> reads wireframes/*.html, writes ia/annotations/*.html
                          (one page per screen family, all states inside; zone maps,
                          zone->job/finding annotations, nav-tree / structure notes).
  2. strip_wireframes() -> removes the .side annotation block and the inline
                          <span class="zone-tag">zone: ...</span> tags from every
                          wireframe so the wireframes render clean.

Idempotent, like fixpack.py. The wireframes stay the render surface; the IA
annotation pages become the single home for the zone/annotation/structure notes.

Usage:
    python3 ia_annotations.py build     # only (re)build ia/annotations/
    python3 ia_annotations.py strip     # only strip wireframes
    python3 ia_annotations.py all       # build then strip  (default)
"""
import os
import re
import sys
import glob
import html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
WF_DIR = os.path.dirname(HERE)                       # wireframes/
ROOT = os.path.dirname(WF_DIR)                        # repo root
OUT_DIR = os.path.join(ROOT, "ia", "annotations")     # ia/annotations/

sys.path.insert(0, ROOT)
# The roadmap is one list and one renderer, at the repo root, because it
# belongs to no stage and three generators draw it.
from _roadmap import render_aside  # noqa: E402
from _course_chrome import head_links  # noqa: E402

# The panel is a component and the page links it, last in <head> so it wins
# on source order. This used to be 23 lines of inline css describing the
# panel here, which _course_chrome.py then deleted and replaced with these
# links every time it ran: the pages were right and the generator was not,
# the same shape as the roadmap. The block is built by the file that owns it.
CHROME_LINKS = head_links(os.path.join(OUT_DIR, "index.html"))

# ---------------------------------------------------------------------------
# Screen families: title -> list of (filename, state-label). Base state first.
# Category pages (politics/crypto/culture/general) are structurally identical;
# one doc represents the template (politics) and lists all four instances.
# ---------------------------------------------------------------------------
FAMILIES = [
    ("event-feed", "Event Feed", [
        ("event-feed.html", "Default (logged in)"),
        ("event-feed-loading.html", "Loading"),
        ("event-feed-empty.html", "Empty"),
        ("event-feed-error.html", "Error"),
        ("event-feed-push-permission-missing.html", "Push permission missing"),
        ("event-feed-logged-out.html", "Logged out"),
        ("event-feed-logged-out-loading.html", "Logged out - loading"),
        ("event-feed-logged-out-empty.html", "Logged out - empty"),
        ("event-feed-logged-out-error.html", "Logged out - error"),
    ]),
    ("event-detail", "Event Detail", [
        ("event-detail.html", "Binary (logged in)"),
        ("event-detail-multi.html", "Multi-outcome"),
        ("event-detail-resolved.html", "Resolved"),
        ("event-detail-loading.html", "Loading"),
        ("event-detail-error.html", "Error"),
        ("event-detail-bet-processing.html", "Bet - processing"),
        ("event-detail-bet-reconcile.html", "Bet - price reconcile"),
        ("event-detail-bet-insufficient.html", "Bet - insufficient balance"),
        ("event-detail-bet-error.html", "Bet - error"),
        ("event-detail-logged-out.html", "Logged out - binary"),
        ("event-detail-logged-out-multi.html", "Logged out - multi"),
        ("event-detail-logged-out-loading.html", "Logged out - loading"),
        ("event-detail-logged-out-error.html", "Logged out - error"),
    ]),
    ("category", "Category Page (Politics / Crypto / Culture / General)", [
        ("politics.html", "Default (logged in)"),
        ("politics-loading.html", "Loading"),
        ("politics-empty.html", "Empty"),
        ("politics-error.html", "Error"),
        ("politics-logged-out.html", "Logged out"),
        ("politics-logged-out-loading.html", "Logged out - loading"),
        ("politics-logged-out-empty.html", "Logged out - empty"),
        ("politics-logged-out-error.html", "Logged out - error"),
    ]),
    ("active-bets", "My Bets (Active Bets)", [
        ("active-bets.html", "Active tab"),
        ("active-bets-loading.html", "Active - loading"),
        ("active-bets-empty-new.html", "Active - empty (new user)"),
        ("active-bets-empty-resolved.html", "Active - empty (all resolved)"),
        ("active-bets-error.html", "Active - error"),
        ("active-bets-history.html", "History tab"),
        ("active-bets-history-loading.html", "History - loading"),
        ("active-bets-history-empty.html", "History - empty"),
        ("active-bets-history-error.html", "History - error"),
    ]),
    ("favorites", "Favorites", [
        ("favorites.html", "Default"),
        ("favorites-loading.html", "Loading"),
        ("favorites-empty.html", "Empty"),
    ]),
    ("deposit", "Deposit", [
        ("deposit.html", "Default"),
        ("deposit-loading.html", "Loading"),
        ("deposit-pending.html", "Pending"),
        ("deposit-minimum-not-met.html", "Minimum not met"),
        ("deposit-error-card.html", "Error - card"),
        ("deposit-error-kyc.html", "Error - KYC"),
        ("deposit-widget-load-failure.html", "Widget load failure"),
    ]),
    ("sign-in", "Sign In / Register", [
        ("sign-in.html", "Default"),
        ("sign-in-loading.html", "Loading"),
        ("sign-in-error.html", "Error"),
        ("sign-in-provider-conflict.html", "Provider conflict"),
    ]),
    ("my-profile", "My Profile", [
        ("my-profile.html", "Default"),
        ("my-profile-loading.html", "Loading"),
        ("my-profile-error.html", "Error"),
    ]),
    ("public-profile", "Public Profile", [
        ("public-profile.html", "Default"),
        ("public-profile-loading.html", "Loading"),
        ("public-profile-error.html", "Error"),
        ("public-profile-not-found.html", "Not found"),
    ]),
    ("wallet", "Wallet", [
        ("wallet.html", "Default"),
        ("wallet-loading.html", "Loading"),
        ("wallet-error.html", "Error"),
    ]),
    ("notifications", "Notifications", [
        ("notifications.html", "Default"),
        ("notifications-loading.html", "Loading"),
        ("notifications-empty.html", "Empty"),
        ("notifications-error.html", "Error"),
        ("notifications-push.html", "Push permission prompt"),
    ]),
    ("how-it-works", "How It Works", [
        ("how-it-works.html", "Default"),
    ]),
    ("win", "Win Screen", [
        ("win.html", "Default"),
        ("win-loading.html", "Loading"),
        ("win-payout-pending.html", "Payout pending"),
        ("win-error.html", "Error"),
    ]),
    ("loss", "Loss Screen", [
        ("loss.html", "Default"),
        ("loss-loading.html", "Loading"),
    ]),
]

# Category doc note: the four category instances and their state files.
CATEGORY_INSTANCES = ["politics", "crypto", "culture", "general"]

MARK = "<!-- ANNOTATIONS + NAV TREE (out of layout flow) -->"

# ---------------------------------------------------------------------------
# HTML slicing helpers
# ---------------------------------------------------------------------------
def _match_div(html, start):
    """Given index of a '<div' that opens a block, return index just past its
    matching '</div>'. Counts nested <div ...> / </div>."""
    depth = 0
    i = start
    tag = re.compile(r"<(/?)div\b", re.I)
    while True:
        m = tag.search(html, i)
        if not m:
            return len(html)
        if m.group(1):  # closing
            depth -= 1
            if depth == 0:
                end = html.find(">", m.end())
                return end + 1
        else:
            depth += 1
        i = m.end()


def slice_side(html):
    """Return (side_html, start, end) for the <div class="side"> block, or (None, -1, -1)."""
    m = re.search(r'<div class="side">', html)
    if not m:
        return None, -1, -1
    start = m.start()
    end = _match_div(html, start)
    return html[start:end], start, end


def extract_zones(body_html):
    """Ordered list of (is_primary, text) for every inline zone-tag chip.

    Primary zones carry a 'zone: ' prefix (top-level layout regions); the rest
    are sub-region / component labels that sit inside a parent zone (e.g. the
    avatar dropdown inside the header). Document order is the layout order, so
    sub-labels naturally follow their parent zone."""
    zones = []
    for m in re.finditer(r'<span class="zone-tag"[^>]*>(.*?)</span>', body_html, re.S):
        txt = _clean(m.group(1))
        if txt.lower().startswith("zone:"):
            zones.append((True, txt[5:].strip()))
        else:
            zones.append((False, txt))
    return zones


def extract_annotations(side_html):
    """Return inner HTML of the annotations <ol>, or ''."""
    m = re.search(r'<aside class="annotations"[^>]*>.*?<ol>(.*?)</ol>', side_html, re.S)
    return m.group(1).strip() if m else ""


def extract_nav_sections(side_html):
    """Return list of (title, inner_html) for each <section class="navtree">."""
    out = []
    for sec in re.finditer(r'<section class="navtree"[^>]*>(.*?)</section>', side_html, re.S):
        inner = sec.group(1)
        t = re.search(r'<span class="zone-tag"[^>]*>(.*?)</span>', inner, re.S)
        title = _clean(t.group(1)) if t else "note"
        rest = inner[t.end():] if t else inner
        out.append((title, rest.strip()))
    return out


def _clean(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------------------
# Page rendering
# ---------------------------------------------------------------------------
def _zbox(text, primary):
    label, _, desc = text.partition(" (")
    desc = desc[:-1] if desc.endswith(")") else desc
    cls = "zbox" if primary else "zbox zsub"
    return '<div class="{}"><span class="zname">{}</span>{}</div>'.format(
        cls,
        _html.escape(label.strip()),
        '<span class="zdesc">{}</span>'.format(_html.escape(desc.strip())) if desc.strip() else "",
    )


def render_zone_stack(zones):
    if not zones:
        return '<p class="muted">No inline zone chips on this state (inherits the layout of the base state).</p>'
    return '<div class="zstack">' + "".join(_zbox(t, p) for p, t in zones) + "</div>"


def render_state(fname, label, is_base):
    path = os.path.join(WF_DIR, fname)
    if not os.path.exists(path):
        return ""
    html = open(path, encoding="utf-8").read()
    side, s, e = slice_side(html)
    body = html[:s] + html[e:] if side else html
    zones = extract_zones(body)
    ann = extract_annotations(side or "")
    open_attr = " open" if is_base else ""
    rel = "../../wireframes/" + fname
    ann_block = (
        '<div class="ann"><h4>Annotations <span class="muted">(zone to job / finding)</span></h4><ol>{}</ol></div>'.format(ann)
        if ann else ""
    )
    return """
    <details class="state"{open_attr}>
      <summary><span class="stlabel">{label}</span> <code>{fname}</code>
        <a class="wflink" href="{rel}" target="_blank" rel="noopener">open wireframe &#8599;</a></summary>
      <div class="stbody">
        <div class="cols">
          <div class="col-zones">
            <h4>Zone map</h4>
            {stack}
          </div>
          <div class="col-ann">
            {ann_block}
          </div>
        </div>
      </div>
    </details>""".format(
        open_attr=open_attr,
        label=_html.escape(label),
        fname=_html.escape(fname),
        rel=rel,
        stack=render_zone_stack(zones),
        ann_block=ann_block or '<p class="muted">No page-specific annotations (inherits the base state).</p>',
    )


def render_structure_notes(base_file):
    """Pull the nav-tree / structure sections from the base wireframe."""
    html = open(os.path.join(WF_DIR, base_file), encoding="utf-8").read()
    side, _, _ = slice_side(html)
    if not side:
        return ""
    secs = extract_nav_sections(side)
    parts = []
    for title, inner in secs:
        parts.append(
            '<section class="note"><h4>{}</h4>{}</section>'.format(_html.escape(title), inner)
        )
    return "".join(parts)


def render_family(slug, title, states):
    base_file = states[0][0]
    state_html = "".join(render_state(f, lbl, i == 0) for i, (f, lbl) in enumerate(states))
    notes = render_structure_notes(base_file)

    cat_note = ""
    if slug == "category":
        rows = []
        for cat in CATEGORY_INSTANCES:
            links = " &middot; ".join(
                '<a href="../../wireframes/{c}{suf}.html" target="_blank" rel="noopener">{name}</a>'.format(
                    c=cat, suf=suf, name=name)
                for suf, name in [("", "default"), ("-loading", "loading"), ("-empty", "empty"),
                                  ("-error", "error"), ("-logged-out", "logged out")]
            )
            rows.append("<tr><th>{}</th><td>{}</td></tr>".format(cat.capitalize(), links))
        cat_note = (
            '<div class="callout"><strong>This template applies to all four category pages.</strong> '
            'The zone map and annotations below use <code>politics</code> as the representative; '
            '<code>crypto</code>, <code>culture</code> and <code>general</code> are structurally identical '
            '(each with the same eight states).<table class="cattable">{}</table></div>'.format("".join(rows))
        )

    esc = _html.escape(title)
    return (PAGE_TMPL
            .replace("@@SIDEBAR@@", render_sidebar(slug))
            .replace("@@TITLE@@", esc)
            .replace("@@SLUG@@", slug)
            .replace("@@CATNOTE@@", cat_note)
            .replace("@@STRUCTURE@@", notes)
            .replace("@@STATES@@", state_html)
            .replace("@@NSTATES@@", str(len(states))))


# ---------------------------------------------------------------------------
# Shared shell (matches the root IA visualizations: research.html etc.)
# ---------------------------------------------------------------------------
# Short sidebar labels per family, in nav order.
SIDEBAR_LABELS = {
    "event-feed": "Event Feed", "event-detail": "Event Detail",
    "category": "Category Pages", "active-bets": "My Bets",
    "favorites": "Favorites", "deposit": "Deposit", "sign-in": "Sign In",
    "my-profile": "My Profile", "public-profile": "Public Profile",
    "wallet": "Wallet", "notifications": "Notifications",
    "how-it-works": "How It Works", "win": "Win Screen", "loss": "Loss Screen",
}


# The drawer chrome, in the vocabulary components/course-chrome.css uses. It
# used to be emitted as .menu-toggle / .sidebar-overlay and renamed afterwards by
# _course_chrome.py, which is the same shape as the roadmap defect below: a
# generator writing one thing and a post-processor correcting it, so the pages
# were right and the generator was not.
SIDEBAR_CHROME = """<button class="rm-toggle" id="menuToggle" aria-label="Open navigation">
  <span></span><span></span><span></span>
</button>
<div class="rm-overlay" id="sidebarOverlay"></div>"""


def render_sidebar(active_slug):
    """The shared dark sidebar. active_slug = a family slug, or '__index__' for
    the index page.

    THE ROWS COME FROM _roadmap.py, and that is the whole point of this function
    being three lines long. It used to hold its own typed copy of the roadmap,
    and that copy fell two stages behind the pages it writes: it still offered
    "UI Kit -> ui-kit/kit.html", frozen as provenance since step 4, and showed
    Tokens + Components as the NEXT thing to build while these pages document a
    stage after it. _resync_roadmap.py had corrected the fifteen OUTPUT pages and
    only one of the two generators, so the mistake was armed and waiting for
    whoever ran this next.

    Three things are local to an annotation page, so three things are passed in:
    it sits two folders deep, its own row links sideways instead of through the
    root, and it carries the family list beneath itself. Both groups always
    render collapsed here, because an annotation page lives under the Wireframe
    Annotations row and never inside User Research or Information Architecture,
    and a group expands only around the page you are standing on.
    """
    subs = []
    for slug, _t, _s in FAMILIES:
        cls = "sidebar-sub-link active" if slug == active_slug else "sidebar-sub-link"
        subs.append('<a href="{slug}.html" class="{cls}">{label}</a>'.format(
            slug=slug, cls=cls, label=_html.escape(SIDEBAR_LABELS[slug])))
    family_list = (['    <div class="sidebar-sub">']
                   + ["      " + row for row in subs]
                   + ['    </div>'])
    return SIDEBAR_CHROME + "\n" + render_aside(
        "../../",
        active="annotations",
        href_override={"annotations": "index.html"},
        extra_after={"annotations": family_list},
    )


SIDEBAR_JS = """<script>
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  const toggle = document.getElementById('menuToggle');
  const openSidebar = () => { sidebar.classList.add('open'); overlay.classList.add('open'); };
  const closeSidebar = () => { sidebar.classList.remove('open'); overlay.classList.remove('open'); };
  toggle.addEventListener('click', openSidebar);
  overlay.addEventListener('click', closeSidebar);
  document.querySelectorAll('.sidebar a[href]').forEach(l => {
    l.addEventListener('click', () => { if (window.innerWidth < 860) closeSidebar(); });
  });
</script>"""


# ---------------------------------------------------------------------------
# Templates (dark theme, shared sidebar shell - matches research.html)
# ---------------------------------------------------------------------------
CSS = """
:root{--bg:#0e0e0e;--surface:#161616;--surface2:#1c1c1c;--border:#242424;--text:#e8e8e8;--muted:#666;--accent:#c8ff00;--blue:#5fa8ff;--green:#5fdb8f;--red:#ff5f5f;--r:8px;--font:'Inter',system-ui,-apple-system,sans-serif;--mono:'JetBrains Mono','Fira Code',monospace}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font);font-size:14px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}
/* ---- layout ---- */
main{padding:60px 20px 80px}
@media(min-width:860px){main{margin-left:220px;padding:48px 48px 100px}}
.wrap{max-width:1040px}
/* ---- content ---- */
.crumbs{font-size:11px;letter-spacing:.04em;color:var(--muted);margin-bottom:14px}
.crumbs a{color:var(--muted)}
.section-label{font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
h1{font-size:26px;font-weight:700;letter-spacing:-.01em;margin:0 0 8px}
h2{font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin:44px 0 14px;padding-top:24px;border-top:1px solid var(--border)}
h4{font-size:10px;font-weight:700;margin:0 0 8px;text-transform:uppercase;letter-spacing:.09em;color:var(--muted)}
.muted{color:var(--muted)}
.sub{color:#9a9a9a;font-size:13.5px;max-width:70ch}
code{background:var(--surface2);border:1px solid var(--border);padding:1px 5px;border-radius:4px;font-family:var(--mono);font-size:11.5px;color:#cdd6a0}
.callout{background:rgba(95,168,255,.06);border:1px solid rgba(95,168,255,.22);border-radius:var(--r);padding:14px 16px;margin:16px 0;font-size:13px}
.callout strong{color:#e8e8e8}
.cattable{border-collapse:collapse;margin-top:12px;width:100%}
.cattable th{text-align:left;padding:5px 12px 5px 0;white-space:nowrap;vertical-align:top;color:#cfcfcf;font-weight:600}
.cattable td{padding:5px 0;font-size:12px;color:var(--muted)}
.note{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:14px 16px;margin:0 0 10px}
.note h4{margin-bottom:8px;color:var(--accent);opacity:.85}
.note pre{background:#0a0a0a;border:1px solid var(--border);border-radius:6px;padding:10px 12px;overflow:auto;font-family:var(--mono);font-size:11.5px;line-height:1.5;white-space:pre-wrap;margin:8px 0 0;color:#bcd08a}
.note .ref{font-size:12.5px;color:#9a9a9a;margin:8px 0 0}
.note .ref strong{color:var(--text)}
.zstack{display:flex;flex-direction:column;gap:5px}
.zbox{background:var(--surface2);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:5px;padding:7px 11px}
.zbox.zsub{margin-left:22px;background:var(--surface);border-left:3px dashed #3a3a3a;padding:5px 11px}
.zbox.zsub .zname{font-weight:500;font-size:11.5px;color:#c4c4c4}
.zname{font-weight:600;display:block;font-size:12.5px;color:var(--text)}
.zdesc{color:var(--muted);font-size:11.5px}
details.state{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);margin:0 0 10px}
details.state[open]{border-color:#333}
details.state>summary{cursor:pointer;padding:12px 15px;font-weight:600;list-style:none;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
details.state>summary::-webkit-details-marker{display:none}
details.state>summary::before{content:"\\25B8";color:var(--muted);font-weight:400}
details.state[open]>summary::before{content:"\\25BE";color:var(--accent)}
details.state>summary:hover{background:rgba(255,255,255,.02)}
.stlabel{font-size:14px}
.wflink{margin-left:auto;font-weight:500;font-size:11.5px;color:var(--blue)}
.stbody{padding:4px 15px 16px;border-top:1px solid var(--border)}
.cols{display:grid;grid-template-columns:1fr;gap:20px;margin-top:14px}
.ann ol{margin:0;padding-left:20px}
.ann li{margin-bottom:9px;font-size:13px;color:#c4c4c4}
.ann li strong{color:var(--text)}
.toc{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr;gap:2px}
.toc li{margin:0}
.toc a{display:flex;align-items:baseline;justify-content:space-between;gap:12px;padding:11px 14px;border:1px solid var(--border);border-radius:var(--r);background:var(--surface);color:var(--text);transition:border-color .15s,background .15s}
.toc a:hover{border-color:#3a3a3a;background:var(--surface2);text-decoration:none}
.toc .tname{font-weight:600;font-size:14px}
.toc .tmeta{font-size:11px;color:var(--muted);white-space:nowrap}
@media(min-width:640px){.toc{grid-template-columns:1fr 1fr;gap:8px}}
@media(min-width:900px){.cols{grid-template-columns:minmax(240px,330px) 1fr}}
"""

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@ - Wireframe Annotations</title>
<style>""" + CSS + """</style>
""" + CHROME_LINKS + """
</head>
<body>
@@SIDEBAR@@
<main>
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Wireframe Annotations</a> &nbsp;/&nbsp; @@TITLE@@</div>
    <div class="section-label">Wireframe Annotations</div>
    <h1>@@TITLE@@</h1>
    <p class="sub">Zone maps, zone&#8594;job / finding annotations and structural notes for this screen and all @@NSTATES@@ of its states. Extracted from the wireframes so the wireframes themselves stay clean grey-box UI.</p>
    @@CATNOTE@@
    <h2>Structure &amp; flow</h2>
    @@STRUCTURE@@
    <h2>States &amp; annotations</h2>
    @@STATES@@
  </div>
</main>
""" + SIDEBAR_JS + """
</body>
</html>
"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wireframe Annotations - Prediction Market Platform</title>
<style>""" + CSS + """</style>
""" + CHROME_LINKS + """
</head>
<body>
@@SIDEBAR@@
<main>
  <div class="wrap">
    <div class="crumbs">Information Architecture &nbsp;/&nbsp; Wireframe Annotations</div>
    <div class="section-label">Plan</div>
    <h1>Wireframe Annotations</h1>
    <p class="sub">The zone maps, zone&#8594;job / finding annotations and structure / nav-tree notes that used to live inside every wireframe, moved out here so the wireframes render as clean grey-box UI. One page per screen; every state of that screen sits inside its page.</p>
    <h2>Screens &middot; @@N@@ families &middot; @@PAGES@@ wireframe pages</h2>
    <ul class="toc">
      @@ITEMS@@
    </ul>
    <p class="sub" style="margin-top:28px">Source of truth for the IA remains <code>ia/docs/sitemap.md</code> and <code>ia/docs/flows.md</code>. These pages are generated by <code>wireframes/_generators/ia_annotations.py</code> from the wireframe HTML.</p>
  </div>
</main>
""" + SIDEBAR_JS + """
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------
def build_ia_pages():
    os.makedirs(OUT_DIR, exist_ok=True)
    items = []
    total_pages = 0
    for slug, title, states in FAMILIES:
        out = render_family(slug, title, states)
        with open(os.path.join(OUT_DIR, slug + ".html"), "w", encoding="utf-8") as fh:
            fh.write(out)
        n = len(states)
        if slug == "category":
            n = 8 * len(CATEGORY_INSTANCES)  # all four instances
        total_pages += n
        items.append(
            '<li><a href="{slug}.html"><span class="tname">{title}</span>'
            '<span class="tmeta">{n} state{s}</span></a></li>'.format(
                slug=slug, title=_html.escape(SIDEBAR_LABELS[slug]), n=n, s="" if n == 1 else "s")
        )
    idx = (INDEX_TMPL
           .replace("@@SIDEBAR@@", render_sidebar("__index__"))
           .replace("@@ITEMS@@", "\n      ".join(items))
           .replace("@@N@@", str(len(FAMILIES)))
           .replace("@@PAGES@@", str(total_pages)))
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(idx)
    print("built {} family pages + index in {}".format(len(FAMILIES), OUT_DIR))


def strip_wireframes():
    n = 0
    for path in glob.glob(os.path.join(WF_DIR, "*.html")):
        html = open(path, encoding="utf-8").read()
        orig = html
        # 1. remove the .side annotation block
        side, s, e = slice_side(html)
        if side:
            pre = html[:s].rstrip()
            # drop a trailing annotations comment on the preceding line
            pre = re.sub(r'\s*<!--\s*=*\s*ANNOTATIONS.*?-->\s*$', '\n', pre, flags=re.S | re.I)
            html = pre + "\n\n  " + html[e:].lstrip()
        # 2. remove every inline zone-tag chip (top-level zones + sub-region labels)
        html = re.sub(r'[ \t]*<span class="zone-tag"[^>]*>.*?</span>\n?', "", html, flags=re.S)
        if html != orig:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html)
            n += 1
    print("stripped annotations from {} wireframes".format(n))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("build", "all"):
        build_ia_pages()
    if mode in ("strip", "all"):
        strip_wireframes()
