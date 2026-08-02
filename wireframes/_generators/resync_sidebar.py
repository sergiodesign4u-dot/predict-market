#!/usr/bin/env python3
"""
resync_sidebar.py  -  Single source of truth for the shared left sidebar nav on
the root visualization pages (research/, user-research/, ia/, voice/).

The 12-stage course taxonomy and the markup for it live in _roadmap.py at the
repo root, imported here and by the two other generators that draw the same
panel. This script owns only WHICH root page is which row, and rebuilds the
<aside class="sidebar" id="sidebar"> ... </aside> block on each of them.

STATIC accordion (no JS). A collapsible group (a stage with sub-pages) shows its
sub-links ONLY on its own pages; on every other page it collapses to a single
link to its first page. So on any page exactly one group is expanded - the one
you are in. The active page's own on-page section sub-links (<div class="sidebar-
sub">) are preserved by extracting and re-inserting them under the active item.
Idempotent, like fixpack.py.

All root viz pages sit one folder deep (research/research.html etc.), so root
links use a single "../" prefix. The generated ia/annotations/ pages render the
same rows two levels deep, from the same module.

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
# The stage list and the row markup are one module, at the root, because the
# roadmap belongs to no stage and three generators draw it.
from _roadmap import render_aside  # noqa: E402

ASIDE_RE = re.compile(r'<aside class="sidebar" id="sidebar">.*?</aside>', re.DOTALL)
SUB_RE = re.compile(r'\s*<div class="sidebar-sub">.*?</div>', re.DOTALL)


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
    new_aside = render_aside(PREFIX, active_key, subs_block=subs_block)
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
