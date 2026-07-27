#!/usr/bin/env python3
"""
page_heading.py  -  give every screen the one heading that says what the page is.

WHAT WAS WRONG. 74 of the 77 screens had no <h1> at all. The document started at
h2 and every level below it was correct, so nothing looked broken; what was
missing was the top of the outline. Three system pages (404, 500, maintenance)
already had one, which is how the gap was visible at all.

WHY IT MATTERS TWICE. For a person on a screen reader the h1 is how you learn
what page you are on without reading it; jumping by heading is the normal way to
move, and a page whose top level is h2 answers "what is this" with a section
name. And ia/docs/pages/seo.md, written in stage 03b, specifies exactly one H1
per indexed page and names the text for each family. The wireframes predated
that document and were never reconciled with it.

WHAT CHANGES. Only the tag. No text is written, no element moves, no rule is
added except `.feed-head :is(h1,h2)` in feed.css so the promoted heading keeps
the size it already had. Three shapes carry a page heading:

    .feed-head > h2   the page title on every list and account screen, and the
                      feed heading that echoes the active category
    h2.ed-q           the event question, which seo.md names as the H1 of an
                      event page
    h2.state-title    on the two screens where the state IS the page (an event
                      that failed to load), matching what 404 already does

Structure is owned by wireframes/, so it runs over both trees, grey first.

Deliberately left alone: the overlay-only screens (deposit, sign-in, win, loss),
where the page behind the dialog is another screen and the dialog carries its
own heading. Inventing a heading for them would be inventing copy.

Idempotent. No em dash.

    python3 wireframes/_generators/page_heading.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TREES = ("wireframes", "ui-visual")

FEED_HEAD = re.compile(r'(class="feed-head"[^>]*>(?:\s*<!--.*?-->)*\s*)<h2([^>]*)>(.*?)</h2>', re.S)
ED_Q = re.compile(r"<h2(\s+class=\"ed-q\"[^>]*)>(.*?)</h2>", re.S)
STATE_TITLE = re.compile(r"<h2(\s+class=\"state-title\"[^>]*)>(.*?)</h2>", re.S)

# the state block is the page only where the page itself failed to arrive
STATE_IS_THE_PAGE = {"event-detail-error.html", "event-detail-logged-out-error.html"}


def promote(html, fname):
    out, n = FEED_HEAD.subn(lambda m: "%s<h1%s>%s</h1>" % (m.group(1), m.group(2), m.group(3)), html, count=1)
    out, k = ED_Q.subn(lambda m: "<h1%s>%s</h1>" % (m.group(1), m.group(2)), out, count=1)
    n += k
    if fname in STATE_IS_THE_PAGE:
        out, k = STATE_TITLE.subn(lambda m: "<h1%s>%s</h1>" % (m.group(1), m.group(2)), out, count=1)
        n += k
    return out, n


def main():
    dry = "--dry-run" in sys.argv
    total = pages = 0
    for tree in TREES:
        d = os.path.join(ROOT, tree)
        if not os.path.isdir(d):
            continue
        t = p = 0
        for fname in sorted(os.listdir(d)):
            if not fname.endswith(".html"):
                continue
            path = os.path.join(d, fname)
            html = open(path, encoding="utf-8").read()
            if "<h1" in html:
                continue
            new, n = promote(html, fname)
            if not n:
                continue
            t += n
            p += 1
            if not dry:
                open(path, "w", encoding="utf-8").write(new)
        print("%-12s %d headings promoted on %d screens" % (tree, t, p))
        total += t
        pages += p
    print("%d in total%s" % (total, " (dry run)" if dry else ""))


if __name__ == "__main__":
    main()
