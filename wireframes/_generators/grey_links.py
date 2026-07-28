#!/usr/bin/env python3
"""
grey_links.py  -  the wireframe palette, as the browser actually paints it.

_conventions.md opens with "neutral greys only, no color", and every check ever
run against it read the SOURCE: 0 non-neutral hex in 104 files, which was true
and was not the question. A colour can also arrive because nobody set one. The
grey sheet styles a link in fourteen scoped places (.wf-screen > a, .card a.q,
.yesno > a and so on) and never as a bare element, so every <a> outside those
selectors renders in the user agent's own #0000EE, underlined, and purple once
visited. Measured in Chrome at 380 and 1280: 992 computed colour values across
the tree before this pass, on links that have been there since the wireframes
were built.

One rule, first in the sheet, weaker than every scoped rule already in it:

    a { color: inherit; }

Colour only. The underline stays, because in a grey box an underline is how a
link says it is one, and taking it away would remove information rather than
paint. outline-color follows currentColor, so it comes back to grey with it.

This is the same lesson as the theme in step 6b, from the other side: a checker
that reads the source cannot see a value the browser supplies. Verified by
computing every colour on every element, not by grepping for a hash.

Idempotent.

Usage:
    python3 wireframes/_generators/grey_links.py            # apply
    python3 wireframes/_generators/grey_links.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GREY = os.path.join(os.path.dirname(os.path.dirname(HERE)), "wireframes")

MARKER = "/* a link takes the ink around it, never the browser's blue. */"
# The removal has to be the exact inverse of the insertion, or the file grows a
# line every run. This is the second time in one pass: substituting "\n" for a
# block that was inserted with its own leading "\n" adds one each time, and 104
# pages changed on a re-run that should have been a no-op. The blank-line
# collapse below is there so the tool converges from a tree an earlier, wrong
# version of it already wrote.
RULE = "\n    %s\n    a { color: inherit; }" % MARKER
RULE_RE = re.compile(r"\n\s*" + re.escape(MARKER) + r"\n\s*a \{ color: inherit; \}")
OPEN = "<style>"


def main():
    check = "--check" in sys.argv
    changed = 0
    for name in sorted(os.listdir(GREY)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(GREY, name)
        html = open(path, encoding="utf-8").read()
        out = re.sub(re.escape(OPEN) + r"\n{2,}", OPEN + "\n", RULE_RE.sub("", html))
        i = out.find(OPEN)
        if i == -1:
            continue
        out = out[:i + len(OPEN)] + RULE + out[i + len(OPEN):]
        if out != html:
            changed += 1
            if not check:
                open(path, "w", encoding="utf-8").write(out)
    print("%d page(s) %s" % (changed, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
