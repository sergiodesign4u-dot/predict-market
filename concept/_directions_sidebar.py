#!/usr/bin/env python3
"""
_directions_sidebar.py  -  Give the two Concept EXPLORATION pages
(directions.html, directions-signal.html) the same course-roadmap left sidebar
the rest of the root viz pages carry, so they are no longer navigation
dead-ends (you could reach them but not get back).

These two pages were hand-authored WITHOUT the sidebar infrastructure and use
their own per-direction palettes (--page-ink / --canvas / ...), not the shared
--surface/--text/--accent vars. So this injects a SELF-CONTAINED sidebar:
hardcoded Signal-dark colors, a mobile drawer (toggle + overlay), the desktop
dock via `body{padding-left:220px}`, and a mobile `.wrap` padding bump so the
toggle never overlaps the masthead. Uniquely-named .rmx-toggle/.rmx-overlay
avoid any class collision.

The ROWS are not written here. They come from _roadmap.py at the repo root, the
one list all three panel generators draw from; this file owns only the two rows
the course does not have (Directions, and the Signal deep-dive under it) and the
self-contained styling above.

BOTH TARGETS ARE CURRENTLY ARCHIVED. directions.html and directions-signal.html
moved to concept/old/pre-vault-3d/ when Vault was chosen, so this script has
nothing live to write and reports "gone" for each rather than raising, which is
what it used to do. Whether the archived copies should still carry a panel is a
decision about the archive; the script is kept honest either way, and it is no
longer a place the roadmap can rot.

Idempotent: skips a file that already carries id="sidebar". Same spirit as
resync_sidebar.py / the ui-visual _resync_sidebar.py.

Usage:
    python3 _directions_sidebar.py          # inject where missing
    python3 _directions_sidebar.py --check  # report, no write
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))       # concept/
ROOT = os.path.dirname(HERE)                            # repo root
sys.path.insert(0, ROOT)
# The stage list is one module at the root. This file used to hold its own
# typed copy of it, which is the pair _roadmap.py exists to close.
from _roadmap import render_aside  # noqa: E402

CSS_BLOCK = """<style>
  /* course roadmap sidebar - self-contained (Signal dark), injected by _directions_sidebar.py */
  .rmx-toggle{position:fixed;top:12px;left:12px;z-index:201;background:#151322;border:1px solid #2a2440;border-radius:6px;width:36px;height:36px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;cursor:pointer}
  .rmx-toggle span{display:block;width:15px;height:1.5px;background:#e8eaf0;border-radius:1px}
  .rmx-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:199;backdrop-filter:blur(2px)}
  .rmx-overlay.open{display:block}
  .sidebar{position:fixed;top:0;left:0;width:220px;height:100vh;background:#14121f;border-right:1px solid #2a2440;display:flex;flex-direction:column;overflow-y:auto;scrollbar-width:none;z-index:200;transform:translateX(-100%);transition:transform .25s cubic-bezier(.4,0,.2,1)}
  .sidebar.open{transform:translateX(0)}
  .sidebar::-webkit-scrollbar{display:none}
  .sidebar-brand{padding:20px 16px 16px;border-bottom:1px solid #2a2440;flex-shrink:0}
  .sidebar-project-name{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#9b7bff;line-height:1.4}
  .sidebar-nav{padding:12px 0;flex:1}
  .sidebar-page-link{display:flex;align-items:center;justify-content:space-between;font-size:13px;font-weight:500;color:#d7d3e6;text-decoration:none;padding:7px 16px;cursor:pointer}
  .sidebar-page-link:hover:not(.planned){background:rgba(255,255,255,.04)}
  .sidebar-page-link.active{color:#9b7bff}
  .sidebar-page-link.planned{color:#8b86a3;cursor:default;opacity:.6}
  .sidebar-page-link.planned::after{content:'Soon';font-size:9px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;background:rgba(255,255,255,.04);color:#8b86a3;padding:2px 5px;border-radius:3px;border:1px solid #2a2440}
  .sidebar-page-link.planned.next{opacity:1}
  .sidebar-page-link.planned.next::after{content:'Next';color:#9b7bff;border-color:#8b5cf6}
  .sidebar-sub{padding:2px 0 8px}
  .sidebar-sub-link{display:block;font-size:12px;color:#8b86a3;text-decoration:none;padding:5px 16px 5px 28px;position:relative}
  .sidebar-sub-link:hover{color:#d7d3e6}
  .sidebar-sub-link.active{color:#d7d3e6}
  .sidebar-sub-link.active::before{content:'';position:absolute;left:17px;top:50%;transform:translateY(-50%);width:3px;height:3px;border-radius:50%;background:#9b7bff}
  .sidebar-divider{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#8b86a3;padding:16px 16px 6px;opacity:.55}
  @media(max-width:859px){.wrap{padding-top:64px!important}}
  @media(min-width:860px){
    .rmx-toggle,.rmx-overlay{display:none!important}
    .sidebar{transform:translateX(0);transition:none}
    body{padding-left:220px}
  }
</style>"""

# The drawer chrome. The ROWS are not here: they come from _roadmap.py, so this
# page cannot fall behind the course the way it had.
CHROME = """<button class="rmx-toggle" id="rmxToggle" aria-label="Open navigation"><span></span><span></span><span></span></button>
<div class="rmx-overlay" id="rmxOverlay"></div>"""


def nav_for(fname):
    """The panel for one exploration page: the course roadmap, with this page's
    own two rows spliced in ahead of Concept, where they belong in the story."""
    local = PAGES[fname]
    return CHROME + "\n" + render_aside(
        "../",
        href_override={"concept": "concept.html"},
        extra_before={"concept": [
            "    " + local["DIR"],
            '    <div class="sidebar-sub">',
            "      " + local["SIG"],
            "    </div>",
        ]},
    )


JS_BLOCK = """<script>
  (function(){
    var sb=document.getElementById('sidebar'),ov=document.getElementById('rmxOverlay'),tg=document.getElementById('rmxToggle');
    if(tg)tg.addEventListener('click',function(){sb.classList.add('open');ov.classList.add('open');});
    if(ov)ov.addEventListener('click',function(){sb.classList.remove('open');ov.classList.remove('open');});
  })();
</script>"""

# Per file: which entry is the current page.
PAGES = {
    "directions.html": {
        "DIR": '<a class="sidebar-page-link active">Directions</a>',
        "SIG": '<a href="directions-signal.html" class="sidebar-sub-link">Signal deep-dive</a>',
    },
    "directions-signal.html": {
        "DIR": '<a href="directions.html" class="sidebar-page-link">Directions</a>',
        "SIG": '<a class="sidebar-sub-link active">Signal deep-dive</a>',
    },
}


def process(fname, write=True):
    path = os.path.join(HERE, fname)
    if not os.path.exists(path):
        # Both targets were archived to concept/old/pre-vault-3d/ when Vault was
        # chosen. Reported, not repaired: whether the archive keeps a live panel
        # is a decision about the archive, not about this script.
        return "gone"
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    if 'id="sidebar"' in html:
        return "already"
    if "</head>" not in html or "<body>" not in html or "</body>" not in html:
        return "no-anchor"
    nav = nav_for(fname)
    html = html.replace("</head>", CSS_BLOCK + "\n</head>", 1)
    html = html.replace("<body>", "<body>\n" + nav + "\n", 1)
    html = html.replace("</body>", JS_BLOCK + "\n</body>", 1)
    if write:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
    return "injected"


def main():
    check = "--check" in sys.argv
    for fname in PAGES:
        print("{:10s} {}".format(process(fname, write=not check), fname))


if __name__ == "__main__":
    main()
