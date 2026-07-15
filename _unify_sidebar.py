#!/usr/bin/env python3
"""
_unify_sidebar.py  -  Give every non-wireframe course page the SAME left-sidebar
look: the "Signal" dark-violet chrome already used on concept/directions.html.

Why an override injector (not a var edit): on the root viz pages (research/,
user-research/, ia/, voice/), concept/concept.html and the ia/annotations/ pages
the sidebar borrows the SAME palette vars (--surface/--border/--accent/...) that
theme the whole page body. We only want to restyle the SIDEBAR, not re-theme each
page's content. So this injects one canonical Signal-sidebar <style> override as
the LAST node in <head> (equal specificity, later source order -> it wins) and
touches nothing else.

Depth-agnostic: an inline <style> needs no ../ vs ../../ path, so 1-deep root
pages and 2-deep ia/annotations/ pages take the identical block.

NOT handled here (already single-sourced elsewhere, same literal colors):
  - ui-visual/*  -> the sidebar reads --rm-* in ui-visual/_theme.css (edit there)
  - concept/directions.html, directions-signal.html -> reference look already,
    self-contained via concept/_directions_sidebar.py

Idempotent: keyed on the marker comment. Re-run any time; re-inject after an edit
by first removing the old block (this script does that automatically).

Usage:
    python3 _unify_sidebar.py          # inject / refresh everywhere
    python3 _unify_sidebar.py --check  # report only, no write
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

MARKER = "unified-sidebar (Signal)"

# The one canonical Signal sidebar palette (identical to concept/directions.html
# and to ui-visual/_theme.css --rm-*). Only colour-bearing properties are set, so
# each page keeps its own sidebar geometry.
BLOCK = """<style>
  /* {marker} - injected by _unify_sidebar.py; keep colours in sync with concept/directions.html + ui-visual/_theme.css --rm-* */
  .sidebar{{background:#14121f;border-right-color:#2a2440}}
  .sidebar-brand{{border-bottom-color:#2a2440}}
  .sidebar-project-name{{color:#9b7bff}}
  .sidebar-page-link{{color:#d7d3e6}}
  .sidebar-page-link:hover:not(.planned){{background:rgba(255,255,255,.04)}}
  .sidebar-page-link.active{{color:#9b7bff}}
  .sidebar-page-link.planned{{color:#8b86a3}}
  .sidebar-page-link.planned::after{{color:#8b86a3;border-color:#2a2440;background:rgba(255,255,255,.04)}}
  .sidebar-page-link.planned.next::after{{color:#9b7bff;border-color:#8b5cf6}}
  .sidebar-divider{{color:#8b86a3}}
  .sidebar-sub-link{{color:#8b86a3}}
  .sidebar-sub-link:hover{{color:#d7d3e6}}
  .sidebar-sub-link.active{{color:#d7d3e6}}
  .sidebar-sub-link.active::before{{background:#9b7bff}}
  .sidebar-back{{color:#8b86a3;border-bottom-color:#2a2440}}
  .sidebar-back:hover{{color:#9b7bff}}
  .sidebar-sub-head{{color:#8b86a3}}
  .sidebar-note{{color:#8b86a3}}
  .menu-toggle{{background:#151322;border-color:#2a2440}}
  .menu-toggle span{{background:#e8eaf0}}
</style>""".format(marker=MARKER)

# The pages whose sidebar borrows page-wide palette vars.
TARGETS = [
    "research/research.html",
    "user-research/personas.html",
    "user-research/jtbd.html",
    "user-research/cjm-as-is.html",
    "user-research/cjm-to-be.html",
    "ia/ia.html",
    "ia/sitemap.html",
    "ia/flows.html",
    "ia/concept-map.html",
    "ia/seo.html",
    "ia/system.html",
    "voice/voice.html",
    "concept/concept.html",
]
TARGETS += sorted(
    os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "ia", "annotations", "*.html"))
)

BLOCK_RE = re.compile(
    r"[ \t]*<style>\s*/\* " + re.escape(MARKER) + r".*?</style>\n?",
    re.DOTALL,
)


def process(rel_path, write=True):
    path = os.path.join(ROOT, rel_path)
    if not os.path.exists(path):
        return "missing"
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    if "</head>" not in html:
        return "no-head"
    stripped = BLOCK_RE.sub("", html)
    new_html = stripped.replace("</head>", BLOCK + "\n</head>", 1)
    if new_html == html:
        return "unchanged"
    status = "refreshed" if MARKER in html else "injected"
    if write:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
    return status


def main():
    check = "--check" in sys.argv
    counts = {}
    for rel in TARGETS:
        status = process(rel, write=not check)
        counts[status] = counts.get(status, 0) + 1
        print("{:10s} {}".format(status, rel))
    print("---", ", ".join("{} {}".format(v, k) for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
