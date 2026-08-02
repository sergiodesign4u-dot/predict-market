#!/usr/bin/env python3
"""
resync_sidebar.py  -  Single source of truth for the shared left sidebar nav on
the root visualization pages (research/, user-research/, ia/, voice/).

The 12-stage course taxonomy is defined ONCE below (thirteen rows: Wireframe
Annotations is an artifact of two stages, not a stage). This script rebuilds the
<aside class="sidebar" id="sidebar"> ... </aside> block on each root viz page and
ensures the sidebar CSS carries the "Next" badge rule.

STATIC accordion (no JS). A collapsible group (a stage with sub-pages) shows its
sub-links ONLY on its own pages; on every other page it collapses to a single
link to its first page. So on any page exactly one group is expanded - the one
you are in. The active page's own on-page section sub-links (<div class="sidebar-
sub">) are preserved by extracting and re-inserting them under the active item.
Idempotent, like fixpack.py.

All root viz pages sit one folder deep (research/research.html etc.), so root
links use a single "../" prefix. The generated ia/annotations/ pages keep their
own sidebar (see ia_annotations.py render_sidebar), which mirrors this taxonomy
and accordion two levels deep.

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
# Collapsible GROUPS - stage clusters with more than one sub-page. When the
# active page is inside a group the group renders EXPANDED (its label divider +
# rows). Otherwise it renders COLLAPSED: one link to the group's first page.
#   rows: ("divider", label) | ("item", key, label, href)
# ---------------------------------------------------------------------------
GROUPS = {
    "user-research": {
        "label": "User Research",
        "first": "user-research/personas.html",
        "keys": {"personas", "jtbd", "cjm-as-is", "cjm-to-be"},
        "rows": [
            ("item", "personas", "Personas", "user-research/personas.html"),
            ("item", "jtbd", "JTBD", "user-research/jtbd.html"),
            ("item", "cjm-as-is", "CJM As-Is", "user-research/cjm-as-is.html"),
            ("item", "cjm-to-be", "CJM To-Be", "user-research/cjm-to-be.html"),
        ],
    },
    "ia": {
        "label": "Information Architecture",
        "first": "ia/flows.html",
        "keys": {"flows", "concept-map", "overview", "sitemap", "seo", "system"},
        "rows": [
            ("divider", "Basic layer"),
            ("item", "flows", "Flows", "ia/flows.html"),
            ("item", "concept-map", "Concept map", "ia/concept-map.html"),
            ("divider", "Detailed layer"),
            ("item", "overview", "Overview", "ia/ia.html"),
            ("item", "sitemap", "Sitemap", "ia/sitemap.html"),
            ("item", "seo", "SEO layer", "ia/seo.html"),
            ("item", "system", "System nodes", "ia/system.html"),
        ],
    },
}

# ---------------------------------------------------------------------------
# Top-level roadmap order. Entries:
#   ("item",    key, label, href_or_None, planned_bool)
#   ("group",   group_key)                 # one of GROUPS
#   ("divider", label)                     # standalone section header
# href is relative to repo root; PREFIX is prepended at render time.
# ---------------------------------------------------------------------------
LAYOUT = [
    ("item", "foundation", "Foundation Research", "research/research.html", False),
    ("group", "user-research"),
    ("group", "ia"),
    ("divider", "Plan"),
    ("item", "wireframes", "Wireframes", "wireframes/event-feed.html", False),
    ("item", "annotations", "Wireframe Annotations", "ia/annotations/index.html", False),
    ("item", "voice", "Voice", "voice/voice.html", False),
    ("divider", "Design and Delivery"),
    ("item", "concept", "Concept", "concept/concept.html", False),
    ("item", "ui-visual", "UI + Visual", "ui-visual/event-feed.html", False),
    ("item", "tokens-components", "Tokens + Components", "ui-kit/overview.html", False),
    ("item", "design-system", "Design System", None, True),
    ("item", "responsive", "Responsive", None, True),
    ("item", "animation", "Animation", None, True),
    ("item", "handoff", "Handoff", None, True),
]

# The "Next" badge marks the next unbuilt stage: the first planned top-level item.
# If that page ever lives inside a collapsed group, the badge rides the group's
# collapsed link instead (see render_group).
NEXT_KEY = next((e[1] for e in LAYOUT if e[0] == "item" and e[4]), None)

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
    "ia/seo.html": "seo",
    "ia/system.html": "system",
    "voice/voice.html": "voice",
}

sys.path.insert(0, ROOT)
from _course_chrome import mark_group  # noqa: E402

ASIDE_RE = re.compile(r'<aside class="sidebar" id="sidebar">.*?</aside>', re.DOTALL)
SUB_RE = re.compile(r'\s*<div class="sidebar-sub">.*?</div>', re.DOTALL)


def render_item(key, label, href, planned, active_key, subs_block):
    """One top-level or in-group row, and its tag says whether it goes anywhere.

    A PLANNED STAGE IS NOT A LINK, so it is not an <a>. It used to be an anchor
    with no href, which is a link element with nothing to open; the badge said
    Soon and the markup said link. A row that goes nowhere is a <span>, and the
    styling never depended on the tag.

    THE ROW YOU ARE ON IS A LINK LIKE EVERY OTHER ROW, which is what the vitrine
    has always done: an active row with no href is a hole in the tree at exactly
    the place a person is standing.
    """
    is_active = key == active_key
    cls = "sidebar-page-link"
    if is_active:
        cls += " active"
    if planned:
        cls += " planned"
    if key == NEXT_KEY:
        cls += " next"
    if planned:
        out = ['    <span class="{cls}">{label}</span>'.format(cls=cls, label=label)]
    else:
        out = ['    <a href="{pfx}{href}" class="{cls}">{label}</a>'.format(
            pfx=PREFIX, href=href, cls=cls, label=label)]
    if is_active and subs_block:
        out.append(subs_block)
    return out


def render_group(gkey, active_key, subs_block):
    """Expanded (label divider + rows) when the active page is inside the group,
    otherwise collapsed to one link to the group's first page."""
    g = GROUPS[gkey]
    if active_key not in g["keys"]:
        cls = "sidebar-page-link"
        if NEXT_KEY in g["keys"]:            # Next rides the collapsed group
            cls += " next"
        return ['    <a href="{pfx}{href}" class="{cls}">{label}</a>'.format(
            pfx=PREFIX, href=g["first"], cls=cls, label=g["label"])]
    lines = ['    <div class="sidebar-divider">{}</div>'.format(g["label"])]
    for row in g["rows"]:
        if row[0] == "divider":
            lines.append('    <div class="sidebar-divider">{}</div>'.format(row[1]))
        else:
            _, key, label, href = row
            lines.extend(render_item(key, label, href, False, active_key, subs_block))
    return lines


def render_aside(active_key, subs_block):
    lines = [
        '<aside class="sidebar" id="sidebar">',
        '  <div class="sidebar-brand">',
        '    <div class="sidebar-project-name">Prediction Market</div>',
        '  </div>',
        '  <nav class="sidebar-nav" aria-label="Course roadmap">',
    ]
    for entry in LAYOUT:
        if entry[0] == "divider":
            lines.append('    <div class="sidebar-divider">{}</div>'.format(entry[1]))
        elif entry[0] == "group":
            lines.extend(render_group(entry[1], active_key, subs_block))
        else:
            _, key, label, href, planned = entry
            lines.extend(render_item(key, label, href, planned, active_key, subs_block))
    lines.append('  </nav>')
    lines.append('</aside>')
    # The group you are in is marked on its label, by the one function that
    # decides it. _course_chrome.py rewrites the sixteen course pages this
    # generator does not manage, and a second idea of the same mark would leave
    # the two tools undoing each other for ever.
    return mark_group("\n".join(lines))


def ensure_next_css(html):
    """Nothing. The panel is painted by components/course-chrome.css, which every
    course page links since _course_chrome.py ran, so this generator writes
    markup and no style at all.

    It used to insert the .next badge rule into the page's own stylesheet. Two
    generators writing into one sheet is the shape this repo has paid for twice,
    and this one would have written a rule reading var(--accent), which on a
    course page is that page's own violet."""
    return html, False


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
    html2, css_changed = ensure_next_css(html)     # CSS lives in <head>, before the aside
    if new_aside == old_aside and not css_changed:
        return "unchanged"
    if write:
        m2 = ASIDE_RE.search(html2)                # re-locate after the CSS insert shifted indices
        new_html = html2[:m2.start()] + new_aside + html2[m2.end():]
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
