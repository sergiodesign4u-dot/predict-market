#!/usr/bin/env python3
"""
_course_chrome.py  -  the course pages stop describing the side panel and start
loading it.

WHAT WAS THERE. One component, seven descriptions. components/course-chrome.css
is the real one and paints the 105 painted screens and the 48 vitrine pages.
The 28 course pages (research/, user-research/, ia/, ia/annotations/, voice/,
concept/) never linked it: each carried 41 to 43 rules of its own, in FIVE
distinct copies, and on top of those _unify_sidebar.py injected one more block to
force a dark violet "Signal" palette. So the panel a person sees while reading
the research is a different panel from the one in the product, drawn by rules the
design system cannot see, and the four .planned rules in the system file had no
markup in any tree it reaches, because the only panel with a planned row is the
one it does not paint.

WHAT THIS DOES, per page and idempotently:
  1. drops the injected Signal block;
  2. drops every rule for a class components/course-chrome.css owns, and only
     those, leaving the page's own layout (main{margin-left:220px}) alone;
  3. renames the page's drawer classes to the system's (.menu-toggle ->
     .rm-toggle, .sidebar-overlay -> .rm-overlay). The drawer script addresses
     them BY ID, so only the paint moves;
  4. links components/fonts.css, tokens.css and course-chrome.css as the last
     nodes of <head>, so they win on source order over whatever the page still
     says, at the right depth for the folder;
  5. brings the markup to the vocabulary the other two panels now use: the tree
     is a named <nav>, the row you are on is a link like every other row rather
     than an <a> with no href, and the group you are in is marked on its label.

WHY LINKING TOKENS IS SAFE, checked and not assumed: the course pages declare
fourteen variables of their own (--bg, --surface, --text, --accent, --border ...)
and tokens.css declares 348, and the two sets do not intersect at all. So the
token file cannot repaint a single line of their content; it only supplies the
values the panel asks for.

WHY THE Z LADDER MATTERS HERE. Their drawer was 199 / 200 / 201 and the system's
is 8 / 9 / 10. Deleting the page's z-index without moving its scrim and toggle
onto the same ladder would have opened the panel BEHIND its own scrim. They are
one vocabulary now, so all three numbers come from tokens.css.

Not done, and recorded rather than hidden: these pages keep their own inline
stylesheet for their own content, and the panel is the only thing this touches.

    python3 _course_chrome.py            # apply
    python3 _course_chrome.py --check    # report only

Idempotent. No em dash.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = ("ui-visual", "ui-kit", "wireframes", "components", "assets", "old")

# What components/course-chrome.css owns. A page rule is deleted when every
# selector in its list is one of these plus, at most, a state class or a bare
# descendant tag: .menu-toggle span is the toggle's bars, .sidebar-sub-link.active
# is a row in a state, and both are the component's business.
OWNED = {"sidebar", "sidebar-brand", "sidebar-project-name", "sidebar-nav",
         "sidebar-page-link", "sidebar-sub", "sidebar-sub-link", "sidebar-back",
         "sidebar-sub-head", "sidebar-divider", "sidebar-note", "sidebar-overlay",
         "menu-toggle", "rm-toggle", "rm-overlay", "theme-switch", "bk-arrow"}
STATE = {"active", "open", "planned", "next", "sub"}

RENAME = (("menu-toggle", "rm-toggle"), ("sidebar-overlay", "rm-overlay"))

LINKS = ("fonts.css", "tokens.css", "course-chrome.css")
MARK = "course chrome: the panel is a component, so the page loads it"
SIGNAL = "unified-sidebar (Signal)"


def pages():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(base, f)
            if 'class="sidebar"' in open(p, encoding="utf-8").read():
                out.append(p)
    return sorted(out)


def owned(selector_list):
    """True when the whole selector list belongs to the component.

       The comment goes first. A section is often labelled in place, and one of
       those labels is "/* ---- sidebar (shared with research.html) ---- */",
       where research.html reads as a class token called html: the rule then
       looks like it belongs to something else and survives the sweep."""
    selector_list = re.sub(r"/\*.*?\*/", " ", selector_list, flags=re.S)
    for sel in selector_list.split(","):
        cls = re.findall(r"\.([\w-]+)", sel)
        if not cls or cls[0] not in OWNED or any(c not in OWNED | STATE for c in cls):
            return False
    return True


def strip_rules(css):
    """Delete the owned rules, top level and one level inside an at-rule. An
       at-rule is edited, never dropped: the same @media carries the page's own
       main{margin-left:220px}, and taking the block would take the layout."""
    out, i, n, dropped = [], 0, len(css), []
    while i < n:
        at = css.find("@", i)
        brace = css.find("{", i)
        if brace == -1:
            out.append(css[i:])
            break
        if at != -1 and at < brace:
            # an at-rule: keep its head, recurse into its body
            depth, j = 0, brace
            while j < n:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            inner, sub = strip_rules(css[brace + 1:j])
            dropped += sub
            out.append(css[i:brace + 1] + inner + css[j:j + 1])
            i = j + 1
            continue
        close = css.find("}", brace)
        if close == -1:
            out.append(css[i:])
            break
        sel = css[i:brace].strip()
        if sel and owned(sel):
            dropped.append(sel)
        else:
            out.append(css[i:close + 1])
        i = close + 1
    return "".join(out), dropped


def head_links(path):
    depth = os.path.relpath(path, ROOT).count(os.sep)
    up = "../" * depth
    rows = ['  <!-- %s. Built by _course_chrome.py. -->' % MARK]
    rows += ['  <link rel="stylesheet" href="%scomponents/%s">' % (up, f) for f in LINKS]
    return "\n".join(rows)


def mark_group(html):
    """The group you are in, marked on its label: the nearest divider above the
       active row, and none at all when the row sits above every divider.

       IMPORTED, NOT COPIED. wireframes/_generators/resync_sidebar.py re-renders
       the whole <aside> for twelve of these pages from its own LAYOUT, and this
       file rewrites the other sixteen, so for one turn each tool undid the
       other's mark and neither reached a fixed point. Two tools may edit one
       region; they may not each have their own idea of what it should say."""
    out = html.replace('<div class="sidebar-divider active">', '<div class="sidebar-divider">')
    nav = out.find('class="sidebar-nav"')
    a = out.find('class="sidebar-page-link active"')
    if nav == -1 or a == -1:
        return out
    d = out.rfind('<div class="sidebar-divider">', nav, a)
    if d == -1:
        return out
    return out[:d] + '<div class="sidebar-divider active">' + out[d + len('<div class="sidebar-divider">'):]


def one(path, check):
    src = open(path, encoding="utf-8").read()
    out, why = src, []

    # 1. the injected Signal override, whole <style> block
    m = re.search(r"\n?<style>\s*\n?\s*/\* %s.*?</style>" % re.escape(SIGNAL), out, re.S)
    if m:
        out = out[:m.start()] + out[m.end():]
        why.append("signal")

    # 2. the page's own copy of the component
    def sweep(mm):
        body, dropped = strip_rules(mm.group(1))
        if dropped:
            why.append("%d rules" % len(dropped))
        return "<style>" + body + "</style>"

    out = re.sub(r"<style>(.*?)</style>", sweep, out, flags=re.S)

    # 3. the drawer joins the system's vocabulary. Class only: the script that
    #    opens it addresses the three elements by id.
    for old, new in RENAME:
        if 'class="%s"' % old in out:
            out = out.replace('class="%s"' % old, 'class="%s"' % new)
            why.append(old + "->" + new)

    # 4. the links, last in <head> so they win on source order
    out = re.sub(r"\n?  <!-- %s.*?\n(?:  <link[^\n]*\n)+" % re.escape(MARK), "\n", out)
    out = out.replace("</head>", head_links(path) + "\n</head>", 1)
    if "%s" % MARK not in src:
        why.append("links")

    # 5. the markup vocabulary
    if '<div class="sidebar-nav">' in out:
        out = out.replace('<div class="sidebar-nav">',
                          '<nav class="sidebar-nav" aria-label="Course roadmap">', 1)
        # the matching close: the last </div> before </aside>
        a = out.find('<nav class="sidebar-nav"')
        z = out.find("</aside>", a)
        k = out.rfind("</div>", a, z)
        out = out[:k] + "</nav>" + out[k + 6:]
        why.append("nav")

    # A PLANNED STAGE IS NOT A LINK. It was an <a> with no href, so the markup
    # said link and the badge said Soon. Sixteen of these pages carry a hand copy
    # of the tree that wireframes/_generators/resync_sidebar.py does not manage,
    # which is why the generator's own fix does not reach them.
    n = len(re.findall(r'<a class="sidebar-page-link planned', out))
    if n:
        out = re.sub(r'<a (class="sidebar-page-link planned[^"]*")>(.*?)</a>',
                     r'<span \1>\2</span>', out, flags=re.S)
        why.append("%d planned" % n)

    # the row you are on is a link, like every other row. Its destination is
    # itself, which is what the vitrine's active row has always been.
    m = re.search(r'<a class="sidebar-page-link active">', out)
    if m:
        out = out[:m.start()] + '<a href="%s" class="sidebar-page-link active">' % os.path.basename(path) \
            + out[m.end():]
        why.append("self href")

    marked = mark_group(out)
    if marked != out:
        out = marked
        why.append("group mark")

    if out != src:
        print("%-42s %s" % (os.path.relpath(path, ROOT), " ".join(why)))
        if not check:
            open(path, "w", encoding="utf-8").write(out)
        return 1
    return 0


def main():
    check = "--check" in sys.argv
    ps = pages()
    n = sum(one(p, check) for p in ps)
    print("--- %d of %d page(s) %s" % (n, len(ps), "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
