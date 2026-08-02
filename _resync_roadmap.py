#!/usr/bin/env python3
"""
_resync_roadmap.py  -  make every hand-authored roadmap sidebar agree with the
one that is generated.

The roadmap lives in ONE list, `LAYOUT` in _roadmap.py beside this file, and that
list has been right since Tokens + Components shipped: the stage is not planned,
its href is ui-kit/overview.html, and the "Next" badge belongs to Design System.
Every page whose panel is GENERATED renders from it and says so: twelve root viz
pages, fifteen annotation pages, and the two Concept exploration pages.

Twenty-one other pages do not render from it. They carry a copy of the roadmap
typed into their own generator or into the file itself, and every one of them
still showed a finished stage as planned, wearing the badge for the NEXT thing to
build. A visitor reading any annotation page was told the project stopped one
stage earlier than it did.

They are not re-rendered from LAYOUT here, and that is deliberate: several carry
local entries LAYOUT knows nothing about (Directions, Concept - Signal, Concept -
Pulse, a Pulse UI stand), and a full re-render would delete them to win an
argument about single-sourcing. What is wrong is three lines, so three lines are
what this touches:

  1. Tokens + Components: planned link -> real link to ui-kit/overview.html
  2. the "Next" badge: off the finished stage, onto Design System
  3. "UI Kit -> ui-kit/kit.html": kit.html is frozen provenance and has not been
     the way in since step 4. The row it duplicates is Tokens + Components.

It also repairs the depth of the archived pages under concept/old/, which were
copied a folder deeper without their ../ being counted again, so every link out
of them pointed at a path that does not exist.

The generators can no longer disagree with this, because they no longer hold an
opinion: ia_annotations.py and concept/_directions_sidebar.py both render from
_roadmap.py. This docstring used to claim they had been "fixed at the same time",
and for concept/ that was true while for ia_annotations.py it was not: it still
offered "UI Kit -> ui-kit/kit.html" and showed Tokens + Components as the next
thing to build, so running it would have rolled fifteen annotation pages back
past the stage they document. A docstring that says a thing is safe is worse than
no docstring, because it is read instead of the code.

Idempotent: every rule is a rewrite of a shape that only exists when it is wrong.

Usage:
    python3 _resync_roadmap.py            # fix
    python3 _resync_roadmap.py --check    # report, no write
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Folders a roadmap link can point at. Used to count ../ correctly.
TOP = ("research", "user-research", "ia", "wireframes", "voice", "concept",
       "ui-visual", "ui-kit")

# Pages whose sidebar is generated from LAYOUT already, or which carry their own
# panel instead of the roadmap.
SKIP_DIRS = ("wireframes", "ui-visual", "ui-kit", ".git", "figmosha2", "visuals")

DONE_HREF = "ui-kit/overview.html"
DONE_LABEL = "Tokens + Components"
NEXT_LABEL = "Design System"


def targets():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(base, f)
            with open(path, encoding="utf-8") as fh:
                if ">" + DONE_LABEL + "<" in fh.read():
                    yield path


def depth_prefix(path):
    """../ repeated as many times as the file is folders deep from the root."""
    rel = os.path.relpath(path, ROOT)
    return "../" * (len(rel.split(os.sep)) - 1)


def fix(html, pfx):
    n = 0

    # 1. the finished stage is a link, not a plan
    done = re.compile(r'<a class="sidebar-page-link planned(?: next)?">'
                      + re.escape(DONE_LABEL) + r"</a>")
    html, k = done.subn('<a href="{}{}" class="sidebar-page-link">{}</a>'
                        .format(pfx, DONE_HREF, DONE_LABEL), html)
    n += k

    # 2. the badge moves to the first thing still unbuilt
    nxt = re.compile(r'<a class="sidebar-page-link planned">' + re.escape(NEXT_LABEL) + r"</a>")
    if 'planned next">' + NEXT_LABEL not in html:
        html, k = nxt.subn('<a class="sidebar-page-link planned next">{}</a>'.format(NEXT_LABEL),
                           html)
        n += k

    # 3. the frozen kit is not a destination
    kit = re.compile(r'\s*<a href="[^"]*ui-kit/kit\.html" class="sidebar-page-link">UI Kit</a>')
    html, k = kit.subn("", html)
    n += k
    return html, n


def fix_depth(html, path):
    """Only for the archived copies, which were moved deeper without recounting."""
    pfx = depth_prefix(path)
    n = 0
    for top in TOP:
        wrong = re.compile(r'href="((?:\.\./)+)' + re.escape(top) + "/")
        for m in set(wrong.findall(html)):
            if m != pfx:
                html = html.replace('href="{}{}/'.format(m, top),
                                    'href="{}{}/'.format(pfx, top))
                n += 1
    return html, n


def main():
    check = "--check" in sys.argv
    total = 0
    for path in sorted(targets()):
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        pfx = depth_prefix(path)
        out, n = fix(src, pfx)
        if os.path.relpath(path, ROOT).startswith("concept" + os.sep + "old"):
            out, d = fix_depth(out, path)
            n += d
        if out != src:
            total += 1
            print("%-46s %d" % (os.path.relpath(path, ROOT), n))
            if not check:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(out)
    print("---", "%d page(s) %s" % (total, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
