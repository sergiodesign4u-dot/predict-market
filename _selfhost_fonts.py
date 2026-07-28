#!/usr/bin/env python3
"""
_selfhost_fonts.py  -  take the three families off Google's CDN.

THE DEFECT. Every painted screen and every vitrine page carried three tags in
its head:

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:...">

so a visitor's IP and User-Agent went to a third party BEFORE the cookie banner
this product ships had asked them anything. A consent banner over a page that
has already made the call is not a consent banner. Step 7b found the same URL
@import-ed from base.css, deleted the duplicate, and wrote down that where the
font comes from is a decision and not a default. This is the decision.

WHAT REPLACES THEM. components/fonts.css: eighteen @font-face rules over
eighteen woff2 files in assets/fonts/, latin and latin-ext, font-display:swap.
It is imported first by components/index.css, so a page that links the system
gets the faces with it and needs no tag of its own. A page that does NOT link
the system (the Stage 07 concept stand) gets a direct link to fonts.css instead,
because the family list is not a thing to write twice.

NOT TOUCHED: anything under an old/ folder. Those are archived stands kept as
provenance, and rewriting an archive to match a decision taken after it was
archived makes it stop being one.

Idempotent both ways: the removal is the exact inverse of what was there, which
is the rule this repo has had to learn twice (see _reconcile_chrome.py).

Usage:
    python3 _selfhost_fonts.py            # apply
    python3 _selfhost_fonts.py --check    # report only
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TREES = ("ui-visual", "ui-kit", "concept")
SYSTEM = "components/index.css"
FONTS = "components/fonts.css"

# The three tags, each with the newline and indent that put it on its own line.
# Matched as a group so the whole block comes out and nothing is left behind.
BLOCK = re.compile(
    r'\n[ \t]*<link rel="preconnect" href="https://fonts\.googleapis\.com">'
    r'\n[ \t]*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>'
    r'\n[ \t]*<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">')
ANY = re.compile(r'\n[ \t]*<link[^>]*fonts\.(?:googleapis|gstatic)\.com[^>]*>')
SYSTEM_LINK = re.compile(r'\n([ \t]*)<link rel="stylesheet" href="([^"]*components/index\.css)">')
HEAD_END = re.compile(r'\n([ \t]*)</head>')


def rel(path, target):
    """The href from this document to a repo-root path."""
    return os.path.relpath(os.path.join(ROOT, target), os.path.dirname(path))


def main():
    check = "--check" in sys.argv
    changed = skipped = 0
    for tree in TREES:
        for dirpath, dirnames, files in os.walk(os.path.join(ROOT, tree)):
            dirnames[:] = [d for d in dirnames if d != "old"]
            for name in sorted(files):
                if not name.endswith(".html"):
                    continue
                path = os.path.join(dirpath, name)
                html = open(path, encoding="utf-8").read()
                if "fonts.googleapis.com" not in html and "fonts.gstatic.com" not in html:
                    continue
                out = BLOCK.sub("", html)
                if out == html:
                    out = ANY.sub("", html)          # a page with a partial set
                if SYSTEM not in out.replace("\\", "/"):
                    # No system stylesheet on this page, so the faces need their
                    # own link. Put it where the block was, which is the head.
                    link = '\n  <link rel="stylesheet" href="%s">' % rel(path, FONTS)
                    if link.strip() not in out:
                        m = HEAD_END.search(out)
                        out = out[:m.start()] + link + out[m.start():]
                if out != html:
                    changed += 1
                    print("%-52s %s" % (os.path.relpath(path, ROOT),
                                        "system" if SYSTEM in out.replace("\\", "/") else "direct link"))
                    if not check:
                        open(path, "w", encoding="utf-8").write(out)
                else:
                    skipped += 1
    print("---", "%d page(s) %s, %d left alone"
          % (changed, "would change" if check else "rewritten", skipped))


if __name__ == "__main__":
    main()
