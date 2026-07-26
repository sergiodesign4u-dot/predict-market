#!/usr/bin/env python3
"""
_use_system.py  -  put the painted screens on the design system.

Until now every screen carried its own copy of the cascade: a 25 to 42 KB inline
<style> (the grey-box skeleton it was color-copied from) plus a link to
_theme.css, which imports _theme-vault.css. Seventy six pages, seven distinct
copies of that block, and no way to change a card without editing all of them.

components/index.css is the same cascade, split into one file per component and
imported in the order the flat kit layered it. So the swap is:

    <style> ... 25-42 KB ... </style>          removed
    <link rel="stylesheet" href="_theme.css">  becomes ../components/index.css

and nothing else. The markup, the classes, the copy, the states and the sidebar
are not touched: this is a refactor, and the screens have to render the same
afterwards. What proves they do is a computed-style snapshot of all 76 pages at
two viewports, taken before and after and diffed element by element.

The font <link>s stay: web fonts are not part of the system's css.

Idempotent: a page that already links the system is left alone. Never edits
wireframes/ or components/.

Usage:
    python3 _use_system.py            # rewrite every screen
    python3 _use_system.py --check    # report what would change
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SYSTEM = '<link rel="stylesheet" href="../components/index.css">'
THEME_RE = re.compile(r'[ \t]*<link rel="stylesheet" href="_theme\.css">')
STYLE_RE = re.compile(r"[ \t]*<style>.*?</style>\n", re.DOTALL)


def process(fname, write=True):
    path = os.path.join(HERE, fname)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    if SYSTEM in html:
        return "done"
    if not THEME_RE.search(html):
        return "no-theme-link"
    n_style = len(STYLE_RE.findall(html))
    if n_style != 1:
        return "styles=%d" % n_style
    new = STYLE_RE.sub("", html, count=1)
    new = THEME_RE.sub("  " + SYSTEM, new, count=1)
    if write:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
    return "moved"


def main():
    check = "--check" in sys.argv
    counts = {}
    for fname in sorted(f for f in os.listdir(HERE)
                        if f.endswith(".html") and f != "overview.html"):
        status = process(fname, write=not check)
        counts[status] = counts.get(status, 0) + 1
        print("{:14s} {}".format(status, fname))
    print("\n" + ", ".join("%s: %d" % kv for kv in sorted(counts.items())))


if __name__ == "__main__":
    main()
