#!/usr/bin/env python3
"""
_strip_wireframe.py  -  take the wireframe's own furniture out of the painted
screens, where it has been shipping invisibly.

WHAT WAS THERE. Each painted screen is a colour copy of a grey wireframe, and
the copy took everything, including the parts that belong to the wireframe and
not to the product:

  - the wireframe screen-tree drawer (a button, an overlay, a <nav> of roughly
    150 links, and the script that opens it). 899 KB across 76 screens, 16 per
    cent of all the HTML in ui-visual, hidden by one display:none in base.css.
    The painted screens already carry their own roadmap sidebar, so this is the
    second navigation on the page and the invisible one.
  - the [TBD] and [placeholder] chips, wireframe annotations that say a thing is
    post-MVP or that a line of copy is still owed. Hidden the same way.
  - two zone tags left over from the 2026-07-03 pass that moved the grey-box
    annotations out to ia/annotations/.

WHY IT GOES. Hidden is not gone: it parses, it sits in the DOM, it turns up in
every link count, and it makes the file that a person opens to read the product
five times longer than the product. And a rule that hides something is a rule
about something, so base.css was carrying twenty-five rules to style a drawer it
also hid.

The record is not lost: wireframes/ still has all of it, visible, and structure
is owned there. This only stops the colour copy from carrying it.

Nothing on screen moves, since every element removed was display:none. Proven
with ui-kit/_verify: 76 screens at 5 widths, before and after.

Idempotent. No em dash.

    python3 ui-visual/_strip_wireframe.py [--dry-run]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# the drawer: its comment, the toggle, the overlay and the <nav>
BLOCK = re.compile(
    r"\n\s*<!-- =+ Wireframe screen-tree nav[^>]*?-->"
    r".*?</nav>\s*", re.S)
# the script that opens it
SCRIPT = re.compile(
    r"\n\s*// Wireframe screen-tree drawer[^\n]*\n\s*\(function \(\) \{.*?\n\s*\}\)\(\);", re.S)
# the annotation chips
CHIP = re.compile(r"\s*<(span|p|div)[^>]*class=\"(?:tbd|placeholder-line|zone-tag)\"[^>]*>.*?</\1>")


def strip(html):
    out = BLOCK.sub("\n", html)
    out = SCRIPT.sub("", out)
    out = CHIP.sub("", out)
    return out


def main():
    dry = "--dry-run" in sys.argv or "--check" in sys.argv
    changed = saved = 0
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(HERE, fname)
        html = open(path, encoding="utf-8").read()
        new = strip(html)
        if new == html:
            continue
        changed += 1
        saved += len(html) - len(new)
        if not dry:
            open(path, "w", encoding="utf-8").write(new)
    print("%d screens %s, %.0f KB of hidden markup removed"
          % (changed, "would change" if dry else "changed", saved / 1024))


if __name__ == "__main__":
    main()
