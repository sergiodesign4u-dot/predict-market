#!/usr/bin/env python3
"""
port_chrome.py  -  the three regions gate 18 could not see, plus the sheet body.

port_structure.py brought <main> back to the tree that owns structure. It left
the header, the bottom nav and the footer alone on purpose, because their
differences had not been read yet and a silent extension of that pass would have
been a guess. Read now, they are four things:

  .cat-condensed, on 68 painted screens and 0 grey ones. A whole navigation
      control: the category strip that slides into the sticky header once the
      full bar scrolls away. Not styling by any reading.
  the footer trust block, rewritten in paint on 55 screens. Grey has three bare
      sentences in a row, the product has a heading, an icon per claim and a
      second line under each.
  the sheet body of the invoked overlays, where the deposit amount is a <span>
      pretending to be a field in grey and a real <input> in colour. The same
      defect step 7d found in the bet panel, one family over.
  110 broken links, which this pass did not find in the chrome at all: it found
      them by asking why the two trees name the same screen differently. The map
      and the reasoning live in port_structure.HREF, because that is the port
      that carried them across; both files reach for the same one.

This is the second half of a pair. ui-visual/_reconcile_chrome.py runs FIRST and
gives the painted chrome back the state the grey tree owns (auth variant, active
slot, empty notifications). Only then is the paint a safe source, because:

  THE PAINT OWNS THE SHAPE OF THE CHROME.
  THE GREY TREE OWNS WHICH STATE IT IS IN.

Run in the other order and this file would carry the paint's aria-current="page"
on the Events slot into all 104 wireframes.

TWO THINGS THIS DOES NOT PORT, both declared in wireframes/_conventions.md:

  the TBD chips. 14 span.tbd and one p.placeholder-line live in every grey
      footer and in none of the painted ones. A wireframe is obliged to mark a
      destination nobody has built; a product showing a user the word TBD is
      showing them the bookkeeping. So the footer port is surgical: only the
      div.footer-trust block is replaced and the rest of the footer is left
      exactly where it is.
  the page behind an invoked overlay. Convention 5 has said since the wireframes
      were built that Sign In, Deposit, Win and Loss "render as modal or
      bottom-sheet overlay content, not as a full-page layout". The paint puts a
      whole feed behind the sheet, because a scrim needs something to be a scrim
      over. Both are right for their own layer, which is what a boundary is.

Idempotent. NEVER writes to ui-visual/.

Usage:
    python3 wireframes/_generators/port_chrome.py            # port
    python3 wireframes/_generators/port_chrome.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import port_structure as ps                                    # noqa: E402

ROOT = ps.ROOT
GREY = ps.GREY
PAINT = ps.PAINT

# Declared in port_structure, with the other one, because the two generators
# write into the same <style> and each has to know where the other's work ends.
MARKER = ps.CHROME_MARKER

# Not product screens.
SKIP = {"overview.html"}

# The shared dialogs, which are chrome by every test that matters: one markup,
# embedded on every screen, wrapped around the page rather than part of it. They
# were never compared either, and the how-it-works one had drifted furthest of
# anything in the repo, 42 elements in grey against 64 in colour, because Stage
# 08 rebuilt it with a hero, icon chips and an FAQ list and the tree that owns
# structure never heard. Ported from the canonical painted copy, like the header.
SHARED_DIALOGS = ("signinDialog", "depositDialog", "howitworksDialog")

# The overlay THIS SCREEN IS. A painted overlay page carries four dialogs (the
# shared sign-in, deposit and how-it-works, plus its own), and the shared ones
# are emitted before it, so "the first .sheet-body in the document" is the
# sign-in provider list on every one of the 17. The first cut asked exactly that
# question and wrote the sign-in buttons into the grey Win, Loss and Deposit
# wireframes. A screen's own overlay has an id.
OUTCOME_ID = "outcomeDialog"


def overlay_body(paint, grey):
    """The sheet body of the screen's own dialog, and only if it is the same
       sheet. The aria-label is the check: both trees name the sheet, and a port
       that has picked up the wrong dialog says "Sign in or create account"
       where the wireframe says "Add funds"."""
    m = re.search(r'<dialog[^>]*id="%s"' % OUTCOME_ID, paint)
    if not m:
        return None
    dialog = ps.region(paint[m.start():], "dialog")[0]
    sheet = ps.region(grey, "section", "sheet")[0]
    if not dialog or not sheet:
        return None
    want = re.search(r'aria-label="([^"]*)"', sheet)
    got = re.search(r'aria-label="([^"]*)"', dialog)
    if not want or not got or want.group(1) != got.group(1):
        return "MISMATCH %s vs %s" % (want and want.group(1), got and got.group(1))
    return ps.region(dialog, "div", "sheet-body")[0]


def grey_of(block, paint_html):
    """A grey box is the painted component with its finish scraped off. The same
       four transforms port_structure uses, imported from it rather than written
       again, so one tree cannot drift from the other in what "greyed" means or
       in how a screen that is named differently on each side is linked."""
    return ps.map_href(ps.strip_photo(ps.inline_sprite(
        ps.unwrap(block, ps.WRAPPERS), ps.symbols_of(paint_html))))


# ------------------------------------------------------------- the strip ----
# The condensed strip is revealed by scrolling, not by navigating, so it is not
# a state with a page of its own. The painted tree reveals it with an
# IntersectionObserver on the full category bar; ported without that, the grey
# tree would carry 68 copies of a block that max-height:0 makes permanently
# invisible, which is exactly the defect step 7b removed 1024 KB of.
#
# The selector loses .feed-inner, which is a plate wrapper the grey tree does not
# have, and it does not gain "main " in its place: the 32 untwinned category
# pages still hang their category bar off the device beside <main>, and a
# selector written for the other layout would leave the strip hidden on exactly
# the third of the tree that has the most categories in it. On a screen with no
# category bar the observer returns early, in both trees, so the strip is inert
# there and not hidden.
STRIP_JS_ID = "wf-catstrip"
STRIP_JS = """  <script id="%s">
    // Reveals the condensed category strip in the sticky header once the full
    // category bar has scrolled up under it. Ported from the painted twin; the
    // selector drops .feed-inner, which is a plate the wireframe does not draw.
    (function () {
      var header = document.querySelector('.app-header');
      var fullNav = document.querySelector('.cat-nav');
      if (!header || !fullNav || !('IntersectionObserver' in window)) return;
      new IntersectionObserver(function (e) {
        header.classList.toggle('scrolled', !e[0].isIntersecting);
      }, { rootMargin: '-60px 0px 0px 0px', threshold: 0 }).observe(fullNav);
    })();
  </script>
""" % STRIP_JS_ID

# Exactly the text set_strip_js inserts, with only the body of the script left
# open. \s* would be the obvious thing to write on both ends and it is the wrong
# thing: it eats whitespace that was already in the page, so the removal takes
# out more than the insertion put in and the file changes on every other run.
STRIP_JS_RE = re.compile(r'\n  <script id="%s">.*?</script>\n' % STRIP_JS_ID, re.S)


def set_strip_js(html, wanted):
    """Remove exactly what is inserted, so the removal is the inverse and not an
       approximation of it. Two runs at this cost two goes: the pages end
       </script></body> with no break, so a "\\n" substitution left two spaces on
       the first run and a newline on the second (74 pages), and a \\s* on the
       front then ate a newline the page already had (13 pages). An idempotent
       generator has to be idempotent about whitespace too."""
    html = STRIP_JS_RE.sub("", html)
    if wanted:
        html = html.replace("</body>", "\n" + STRIP_JS + "</body>", 1)
    return html


# ------------------------------------------------------------- the ports ----


def swap(html, block, tag, cls=None):
    old, a, b = ps.region(html, tag, cls)
    if old is None or old == block:
        return html, False
    return html[:a] + block + html[b:], True


def auth_of(header):
    return "out" if 'class="auth-btns"' in header else "in"


def slot_of(nav):
    for i, attrs in enumerate(re.findall(r"<li\b([^>]*)>", nav)):
        if "aria-current" in attrs:
            return i
    return None


def set_slot(nav, want):
    nav = re.sub(r'<li aria-current="page">', "<li>", nav)
    if want is None:
        return nav
    n = [0]

    def sub(m):
        n[0] += 1
        return '<li aria-current="page">' if n[0] - 1 == want else m.group(0)
    return re.sub(r"<li>", sub, nav)


NOTIF_EMPTY = re.compile(r'<p class="notif-empty">.*?</p>', re.S)


def set_notif(header, empty, href, old_header):
    """Carry this page's own notifications state onto the ported shape. The state
       is read from the grey page being rewritten, not from the paint: the paint
       was told this same fact by _reconcile_chrome.py, and asking the tree that
       owns a fact is shorter than asking the tree that was told."""
    if 'class="notif-menu"' not in header:
        return header
    if empty:
        body = NOTIF_EMPTY.search(old_header or "")
        if body:
            drop, a, b = ps.region(header, "div", "notif-drop")
            if drop and "notif-empty" not in drop:
                keep = re.search(r'<a class="notif-all".*?</a>', drop, re.S)
                head = re.match(r"<div[^>]*>", drop).group(0)
                header = header[:a] + head + body.group(0) + \
                    (keep.group(0) if keep else "") + "</div>" + header[b:]
        header = re.sub(r'<span class="badge-dot">[^<]*</span>', "", header)
        header = re.sub(r'<summary aria-label="Notifications[^"]*">',
                        '<summary aria-label="Notifications, none">', header, count=1)
    if href:
        header = re.sub(r'(<a class="notif-all" href=")[^"]*"',
                        lambda m: m.group(1) + href + '"', header)
    return header


def main():
    check = "--check" in sys.argv
    feed = open(os.path.join(PAINT, "event-feed.html"), encoding="utf-8").read()
    out_feed = open(os.path.join(PAINT, "event-feed-logged-out.html"),
                    encoding="utf-8").read()
    canon = {
        ("header", "in"): grey_of(ps.region(feed, "header")[0], feed),
        ("header", "out"): grey_of(ps.region(out_feed, "header")[0], out_feed),
        ("nav", "in"): grey_of(ps.region(feed, "nav", "bottom-nav")[0], feed),
        ("nav", "out"): grey_of(ps.region(out_feed, "nav", "bottom-nav")[0], out_feed),
        "trust": grey_of(ps.region(feed, "div", "footer-trust")[0], feed),
    }
    for did in SHARED_DIALOGS:
        m = re.search(r'<dialog[^>]*id="%s"' % did, feed)
        blk = ps.region(feed[m.start():], "dialog")[0] if m else None
        canon[did] = grey_of(blk, feed) if blk else None

    changed = 0
    for name in sorted(os.listdir(GREY)):
        if not name.endswith(".html") or name in SKIP:
            continue
        gpath = os.path.join(GREY, name)
        grey = open(gpath, encoding="utf-8").read()
        ppath = os.path.join(PAINT, ps._twins.painted_of(name))
        paint = open(ppath, encoding="utf-8").read() if os.path.exists(ppath) else None
        out, moved = grey, []

        # 1. the sheet body of an invoked overlay
        if paint:
            src = overlay_body(paint, out)
            if src and src.startswith("MISMATCH"):
                raise SystemExit("port_chrome: %s, the two trees name this sheet "
                                 "differently, so one of them is not this "
                                 "screen: %s" % (name, src))
            if src:
                out, ok = swap(out, grey_of(src, paint), "div", "sheet-body")
                if ok:
                    moved.append("sheet-body")
            # The sub-line under the sheet title is copy, and copy is owned here.
            # The head itself is not ported: its heading level and its close are
            # the declared per-context difference, and this sentence is neither.
            #
            # Read out of the screen's OWN dialog, never out of the document. The
            # first cut asked the page for its first .sheet-sub and got the shared
            # sign-in one, which every overlay page embeds before its own, so the
            # grey Deposit was told "You are about to place a bet. No crypto
            # wallet required." That is the same trap gate 19's first cut fell
            # into an hour earlier in this same pass: a page with several of a
            # thing has to be asked by id, and knowing the rule is not the same
            # as applying it.
            om = re.search(r'<dialog[^>]*id="%s"' % OUTCOME_ID, paint)
            mine = ps.region(paint[om.start():], "dialog")[0] if om else ""
            head = ps.region(out, "div", "sheet-head")[0]
            sub = re.search(r'<p class="sheet-sub">.*?</p>', mine or "", re.S)
            if head is not None and sub and sub.group(0) not in head:
                new = re.sub(r"(</h[12]>)", lambda m: m.group(1) + sub.group(0),
                             head, count=1)
                if new != head:
                    out, ok = swap(out, new, "div", "sheet-head")
                    if ok:
                        moved.append("sheet-sub")

        # 1b. the shared dialogs, one markup wherever they are embedded
        for did in SHARED_DIALOGS:
            if not canon[did]:
                continue
            m = re.search(r'<dialog[^>]*id="%s"' % did, out)
            if not m:
                continue
            old, a, b = ps.region(out[m.start():], "dialog")
            if old is None or old == canon[did]:
                continue
            out = out[:m.start() + a] + canon[did] + out[m.start() + b:]
            moved.append(did)

        # 2. the footer trust block, and only it
        old, a, b = ps.region(out, "div", "footer-trust")
        if old is not None and old != canon["trust"]:
            out = out[:a] + canon["trust"] + out[b:]
            moved.append("trust")

        # 3. the bottom nav, keeping this page's own active slot
        #
        # The auth variant comes from the PAINTED twin, and it is the one state
        # fact that does. Ten screens disagreed about it, which means there was
        # no fact to read: it had to be DECIDED, page by page and with a reason
        # each. That decision is written once, in ui-visual/_reconcile_chrome.py,
        # and both trees follow it from there. Reading it out of grey instead
        # would leave 404, 500 and toasts logged out here and logged in in
        # colour, which is the drift this pass exists to end. The 32 untwinned
        # category pages have nobody to ask and keep their own.
        head_now = ps.region(out, "header")[0]
        want_auth = auth_of(ps.region(paint, "header")[0]) if paint and \
            ps.region(paint, "header")[0] else (auth_of(head_now) if head_now else None)

        old = ps.region(out, "nav", "bottom-nav")[0]
        if old is not None and want_auth is not None:
            want = set_slot(canon[("nav", want_auth)], slot_of(old))
            out, ok = swap(out, want, "nav", "bottom-nav")
            if ok:
                moved.append("nav")

        # 4. the header, keeping this page's own notifications state
        if head_now is not None:
            href = re.search(r'<a class="notif-all" href="([^"]+)"', head_now)
            want = set_notif(canon[("header", want_auth)],
                             "notif-empty" in head_now,
                             href.group(1) if href else None, head_now)
            out, ok = swap(out, want, "header")
            if ok:
                moved.append("header")

        # 5. the observer that reveals the strip, only where a strip landed
        before = out
        out = set_strip_js(out, "cat-condensed" in (ps.region(out, "header")[0] or ""))
        if out != before:
            moved.append("strip-js")

        # 6. the grey rules for whatever the port introduced
        classes = set()
        for tag, cls in (("header", None), ("nav", "bottom-nav"),
                         ("footer", None), ("section", "sheet")):
            blk = ps.region(out, tag, cls)[0]
            if blk:
                classes |= ps.classes_in(blk)
        for did in SHARED_DIALOGS:
            m = re.search(r'<dialog[^>]*id="%s"' % did, out)
            if m:
                classes |= ps.classes_in(ps.region(out[m.start():], "dialog")[0] or "")
        new_classes = classes - styled(out)
        if new_classes:
            out = apply_css(out, new_classes)
            moved.append("+%d classes" % len(new_classes))

        if out != grey:
            changed += 1
            print("%-38s %s" % (name, " ".join(moved)))
            if not check:
                open(gpath, "w", encoding="utf-8").write(out)
    print("---", "%d page(s) %s" % (changed, "would change" if check else "rewritten"))


BLOCK_RE = ps.block_re(MARKER)


def styled(html):
    """Classes the page's own grey-box css already covers. Both generated blocks
       come out first: counting either would make a class look covered by the
       very rule that is being decided. Same function port_structure uses, for
       the same reason and with the same answer."""
    return ps.styled(html)


def grey_block(classes):
    """The same derivation port_structure uses, minus its tail.

       ps.grey_block() ends with a hand-written list of edges for the market box,
       the odds bar and the chart, which are <main> and belong to that block.
       Calling it here would write those declarations a second time, in a second
       block, on the same page: which is the "one element, one rule" defect step
       7b spent a whole pass deleting."""
    lines = [MARKER,
             "    /* Layout taken from components/, every colour replaced by the",
             "       wireframe palette. See wireframes/_generators/port_chrome.py. */"]
    seen, plain, media = set(), [], []
    for (cond, sel), decls in ps.rules_for(classes):
        if (cond, sel, decls) in seen:
            continue
        seen.add((cond, sel, decls))
        (plain if cond is None else media).append((cond, sel, decls))
    for _, sel, decls in plain:
        lines.append("    %s { %s; }" % (sel, decls))
    for cond in sorted({c for c, _, _ in media}, reverse=True):
        lines.append("    %s {" % cond)
        for c, sel, decls in media:
            if c == cond:
                lines.append("      %s { %s; }" % (sel, decls))
        lines.append("    }")
    for ln in lines:
        if "{" in ln and ln.count("(") != ln.count(")"):
            raise SystemExit("port_chrome: unbalanced selector, would kill the "
                             "rest of the sheet:\n  " + ln)
    return "\n".join(lines)


def apply_css(html, classes):
    block = grey_block(classes)
    if MARKER in html:
        return BLOCK_RE.sub(lambda _: block, html)
    return html.replace("</style>", block + "\n  </style>", 1)


if __name__ == "__main__":
    main()
