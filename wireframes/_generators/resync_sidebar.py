#!/usr/bin/env python3
"""
resync_sidebar.py  -  Single source of truth for the shared left sidebar nav on
the root visualization pages (research/, user-research/, ia/, voice/).

The 13-stage course taxonomy is defined ONCE in NAV below. This script rebuilds
the <aside class="sidebar" id="sidebar"> ... </aside> block on each root viz page,
preserving that page's own on-page section sub-links (the <div class="sidebar-sub">
block) by extracting it and re-inserting it under the active item. Idempotent,
like fixpack.py / ia_annotations.py.

All root viz pages sit one folder deep (research/research.html etc.), so root
links use a single "../" prefix. The generated ia/annotations/ pages keep their
own sidebar (see ia_annotations.py render_sidebar), which mirrors this taxonomy
two levels deep.

Usage:
    python3 resync_sidebar.py          # rewrite all root pages
    python3 resync_sidebar.py --check  # report which pages would change, no write
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))        # repo root
PREFIX = "../"                                        # root pages are 1 folder deep

# ---------------------------------------------------------------------------
# The 13-stage taxonomy (course order). Each entry is one of:
#   ("item",    key, label, href_or_None, planned_bool)
#   ("divider", label)                       # multi-page stage header
# href is relative to repo root; PREFIX is prepended at render time.
# key is matched against the active page to decide .active + where subs go.
# ---------------------------------------------------------------------------
NAV = [
    ("item", "foundation", "Foundation Research", "research/research.html", False),
    ("divider", "User Research"),
    ("item", "personas", "Personas", "user-research/personas.html", False),
    ("item", "jtbd", "JTBD", "user-research/jtbd.html", False),
    ("item", "cjm-as-is", "CJM As-Is", "user-research/cjm-as-is.html", False),
    ("item", "cjm-to-be", "CJM To-Be", "user-research/cjm-to-be.html", False),
    ("divider", "Information Architecture"),
    ("divider", "Basic layer"),
    ("item", "flows", "Flows", "ia/flows.html", False),
    ("item", "concept-map", "Concept map", "ia/concept-map.html", False),
    ("divider", "Detailed layer"),
    ("item", "overview", "Overview", "ia/ia.html", False),
    ("item", "sitemap", "Sitemap", "ia/sitemap.html", False),
    ("divider", "Plan"),
    ("item", "wireframes", "Wireframes", "wireframes/event-feed.html", False),
    ("item", "annotations", "Wireframe Annotations", "ia/annotations/index.html", False),
    ("item", "voice", "Voice", "voice/voice.html", False),
    ("divider", "Design and Delivery"),
    ("item", "concept", "Concept", None, True),
    ("item", "ui-visual", "UI + Visual", None, True),
    ("item", "tokens-components", "Tokens + Components", None, True),
    ("item", "design-system", "Design System", None, True),
    ("item", "responsive", "Responsive", None, True),
    ("item", "animation", "Animation", None, True),
    ("item", "handoff", "Handoff", None, True),
]

# Root viz page (relative to repo root) -> active nav key.
PAGES = {
    "research/research.html": "foundation",
    "user-research/personas.html": "personas",
    "user-research/jtbd.html": "jtbd",
    "user-research/cjm-as-is.html": "cjm-as-is",
    "user-research/cjm-to-be.html": "cjm-to-be",
    "ia/ia.html": "overview",
    "ia/sitemap.html": "sitemap",
    "ia/flows.html": "flows",
    "ia/concept-map.html": "concept-map",
    "voice/voice.html": "voice",
}

ASIDE_RE = re.compile(r'<aside class="sidebar" id="sidebar">.*?</aside>', re.DOTALL)
SUB_RE = re.compile(r'\s*<div class="sidebar-sub">.*?</div>', re.DOTALL)


def render_aside(active_key, subs_block):
    """Build the full <aside> for a page. subs_block is that page's own
    <div class="sidebar-sub"> ... </div> (or '') re-inserted under the active item."""
    lines = [
        '<aside class="sidebar" id="sidebar">',
        '  <div class="sidebar-brand">',
        '    <div class="sidebar-project-name">Prediction Market</div>',
        '  </div>',
        '  <div class="sidebar-nav">',
    ]
    for entry in NAV:
        if entry[0] == "divider":
            lines.append('    <div class="sidebar-divider">{}</div>'.format(entry[1]))
            continue
        _, key, label, href, planned = entry
        is_active = key == active_key
        cls = "sidebar-page-link"
        if is_active:
            cls += " active"
        if planned:
            cls += " planned"
        if planned or is_active:
            # planned + active items carry no href
            lines.append('    <a class="{cls}">{label}</a>'.format(cls=cls, label=label))
        else:
            lines.append('    <a href="{pfx}{href}" class="{cls}">{label}</a>'.format(
                pfx=PREFIX, href=href, cls=cls, label=label))
        if is_active and subs_block:
            lines.append(subs_block.strip("\n"))
    lines.append('  </div>')
    lines.append('</aside>')
    return "\n".join(lines)


def process(rel_path, active_key, write=True):
    path = os.path.join(ROOT, rel_path)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    m = ASIDE_RE.search(html)
    if not m:
        return "no-aside"
    old_aside = m.group(0)
    subm = SUB_RE.search(old_aside)
    subs_block = ("    " + subm.group(0).strip()) if subm else ""
    new_aside = render_aside(active_key, subs_block)
    if new_aside == old_aside:
        return "unchanged"
    if write:
        new_html = html[:m.start()] + new_aside + html[m.end():]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
    return "updated"


def main():
    check = "--check" in sys.argv
    for rel_path, active_key in PAGES.items():
        status = process(rel_path, active_key, write=not check)
        print("{:10s} {}".format(status, rel_path))


if __name__ == "__main__":
    main()
