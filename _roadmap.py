#!/usr/bin/env python3
"""
_roadmap.py  -  the course roadmap: which stages exist, in what order, and the
markup that draws them. One list, one renderer, three generators.

WHY IT IS AT THE ROOT. The roadmap belongs to no stage. It was declared inside
wireframes/_generators/resync_sidebar.py, which made concept/ have to reach into
the wireframes tree to draw its own panel, a dependency the folder layout denies.
It sits beside the other maps owned by neither layer: _twins.py (which screen is
which screen's twin), _course_chrome.py (what the panel looks like), and
_resync_roadmap.py, which patches the hand-typed copies this file cannot reach.

WHAT IT REPLACED, AND WHAT THAT COST. The list existed four times: LAYOUT here,
and literal HTML typed into ia_annotations.py, into concept/_directions_sidebar.py
and into two stand specimens. Three of the four called themselves the sidebar.
The defect had already fired and had not gone off yet: ia_annotations.py still
held "UI Kit -> ui-kit/kit.html" and "Tokens + Components" as `planned next`,
two stages behind the pages it writes, because _resync_roadmap.py had corrected
the OUTPUT and only one of the two generators. Whoever ran it next would have
rolled fifteen annotation pages back to a roadmap that ended before the stage
they were reading about, and pointed them at a kit frozen as provenance. This is
the pair _levels.py closed between two other generators, in the same shape: one
computation feeds all of its consumers, or they drift and no one can say which
one is lying.

WHAT IS DELIBERATELY NOT HERE. The two stand specimens
(ui-kit/specimens/course-chrome-roadmap.html, ui-kit/specimens.extra.html) show
what the PANEL LOOKS LIKE. Their rows are `href="#"` and abridged on purpose,
and a specimen that re-rendered itself from the truth would start failing when
the truth changed, which is the opposite of what a specimen is for. Each says so
in a comment on its first row.

HOW A CONSUMER DIFFERS FROM ANOTHER. Only in four things, and each is an
argument, so each is a parameter:
  prefix          how deep the page sits (../ or ../../)
  active          which row is the page you are on
  href_override   a row a page can reach without going through the root
  extra_before / extra_after
                  rows this page has and the course does not: the annotation
                  family list, the Concept exploration pages

No em dash.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from _course_chrome import mark_group  # noqa: E402

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
# href is relative to repo root; the caller's prefix is prepended at render time.
#
# Twelve stages, thirteen rows: Wireframe Annotations is an artifact of two
# stages rather than a stage of its own, and it earns a row because it is a
# place you can stand. CJM has no row here at all for the opposite reason: it is
# built inside User Research, so it is one of that group's sub-pages.
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
# collapsed link instead (see _render_group).
NEXT_KEY = next((e[1] for e in LAYOUT if e[0] == "item" and e[4]), None)

# The shell every consumer wraps the rows in. The tree is a NAMED <nav>, per
# CLAUDE.md: a panel with no accessible name is a list of links to a screen
# reader, and there are three lists of links on some of these pages.
SHELL_OPEN = [
    '<aside class="sidebar" id="sidebar">',
    '  <div class="sidebar-brand">',
    '    <div class="sidebar-project-name">Prediction Market</div>',
    '  </div>',
    '  <nav class="sidebar-nav" aria-label="Course roadmap">',
]
SHELL_CLOSE = ['  </nav>', '</aside>']


def _render_item(key, label, href, planned, prefix, active, subs_block,
                 href_override, indent):
    """One top-level or in-group row, and its tag says whether it goes anywhere.

    A PLANNED STAGE IS NOT A LINK, so it is not an <a>. It used to be an anchor
    with no href, which is a link element with nothing to open; the badge said
    Soon and the markup said link. A row that goes nowhere is a <span>, and the
    styling never depended on the tag.

    THE ROW YOU ARE ON IS A LINK LIKE EVERY OTHER ROW, which is what the vitrine
    has always done: an active row with no href is a hole in the tree at exactly
    the place a person is standing.
    """
    is_active = key == active
    cls = "sidebar-page-link"
    if is_active:
        cls += " active"
    if planned:
        cls += " planned"
    if key == NEXT_KEY:
        cls += " next"
    if planned:
        out = ['{i}<span class="{cls}">{label}</span>'.format(i=indent, cls=cls, label=label)]
    else:
        target = href_override.get(key)
        if target is None:
            target = prefix + href
        out = ['{i}<a href="{href}" class="{cls}">{label}</a>'.format(
            i=indent, href=target, cls=cls, label=label)]
    if is_active and subs_block:
        out.append(subs_block)
    return out


def _render_group(gkey, prefix, active, subs_block, href_override, indent):
    """Expanded (label divider + rows) when the active page is inside the group,
    otherwise collapsed to one link to the group's first page."""
    g = GROUPS[gkey]
    if active not in g["keys"]:
        cls = "sidebar-page-link"
        if NEXT_KEY in g["keys"]:            # Next rides the collapsed group
            cls += " next"
        return ['{i}<a href="{pfx}{href}" class="{cls}">{label}</a>'.format(
            i=indent, pfx=prefix, href=g["first"], cls=cls, label=g["label"])]
    lines = ['{i}<div class="sidebar-divider">{l}</div>'.format(i=indent, l=g["label"])]
    for row in g["rows"]:
        if row[0] == "divider":
            lines.append('{i}<div class="sidebar-divider">{l}</div>'.format(i=indent, l=row[1]))
        else:
            _, key, label, href = row
            lines.extend(_render_item(key, label, href, False, prefix, active,
                                      subs_block, href_override, indent))
    return lines


def render_rows(prefix, active=None, subs_block="", href_override=None,
                extra_before=None, extra_after=None, indent="    "):
    """Every row of the roadmap, in order, as a list of lines.

    extra_before / extra_after are keyed by the LAYOUT key (or group key) they
    hang off, and their lines are emitted verbatim, so a consumer can add rows
    the course does not have without the course having to know about them.
    """
    href_override = href_override or {}
    extra_before = extra_before or {}
    extra_after = extra_after or {}
    lines = []
    for entry in LAYOUT:
        if entry[0] == "divider":
            lines.append('{i}<div class="sidebar-divider">{l}</div>'.format(i=indent, l=entry[1]))
            continue
        key = entry[1]
        lines.extend(extra_before.get(key, []))
        if entry[0] == "group":
            lines.extend(_render_group(key, prefix, active, subs_block, href_override, indent))
        else:
            _, _, label, href, planned = entry
            lines.extend(_render_item(key, label, href, planned, prefix, active,
                                      subs_block, href_override, indent))
        lines.extend(extra_after.get(key, []))
    return lines


def render_aside(prefix, active=None, **kw):
    """The whole <aside>: brand, named <nav>, every row, and the group you are in
    marked on its label.

    The mark is applied by _course_chrome.mark_group and by nothing else.
    IMPORTED, NOT COPIED: that file rewrites the sixteen course pages these
    generators do not manage, and for one turn each tool undid the other's mark
    and neither reached a fixed point. Two tools may edit one region; they may
    not each have their own idea of what it should say.
    """
    lines = list(SHELL_OPEN) + render_rows(prefix, active, **kw) + list(SHELL_CLOSE)
    return mark_group("\n".join(lines))


def stages():
    """The stages, in course order, as (number, label). Wireframe Annotations is
    a row and not a stage, so it is not numbered."""
    out, n = [], 0
    for e in LAYOUT:
        if e[0] == "group":
            n += 1
            out.append(("%02d" % n, GROUPS[e[1]]["label"]))
        elif e[0] == "item" and e[1] != "annotations":
            n += 1
            out.append(("%02d" % n, e[2]))
    return out


if __name__ == "__main__":
    for num, label in stages():
        print(num, label)
