#!/usr/bin/env python3
"""
_reconcile_chrome.py  -  give the painted chrome back the state the grey tree owns.

THE DEFECT. Gate 18 compares <main> and nothing else, so the header, the bottom
nav and the footer were the one place where the two trees could drift with every
gate green. They did, and the drift runs BOTH ways, which is why it needs two
tools and not one:

  the paint got the shape right and the state wrong
      aria-current="page" sits on the Events slot of all 76 painted screens. The
      grey tree marks the slot the page actually is (54 Events, 9 My Bets, 3
      Favorites, 6 Portfolio, 15 none), which is correct and is what a screen
      reader reads out. On the painted Wallet screen it announces "Events,
      current page".
      Ten screens carry the logged-IN header over a bottom nav whose home slot
      points at event-feed-logged-out.html. That is not a decision anyone made,
      it is _apply_family.py grafting one canonical header onto every screen: the
      two halves of the same chrome disagree about whether anybody is signed in.
      Three screens whose whole subject is an empty state (a new user with no
      bets, no favorites, no notifications) got the notifications dropdown with
      three unread items in it.

  the grey tree got the state right and the shape wrong
      no .cat-condensed anywhere, and a footer trust strip of three bare lines
      where the product ships a headed block. That half is port_chrome.py.

So this file fixes the paint from the grey tree, and port_chrome.py then copies
the corrected paint back. The order matters: state first, then shape, or the port
would carry the paint's wrong state into the tree that owns state.

  THE PAINT OWNS THE SHAPE OF THE CHROME.
  THE GREY TREE OWNS WHICH STATE IT IS IN.

Three state facts come from wireframes/: the auth variant, the bottom-nav active
slot, and whether the notifications dropdown is empty. Everything else is paint.

THE AUTH SPLIT. Ten screens disagreed and each one is answered by a reason, not
by a rule about which tree wins:

  logged OUT, already documented  how-it-works, public-profile x4. CLAUDE.md:
                                  "Public Profile and How It Works carry the
                                  logged-out header (reached pre-auth)."
  logged OUT, by what the screen  cookie-consent, because the banner is by
  is                              definition a first visit; maintenance, because
                                  the app server is down and there is no session
                                  to read a balance out of.
  logged IN                       404, 500, toasts. A signed-in person who hits a
                                  404 must not be shown Sign in / Sign up: the
                                  page would read as "you were logged out", which
                                  is a worse error than the one they hit.

Idempotent. Writes ui-visual/ only, reads wireframes/ only.

Usage:
    python3 ui-visual/_reconcile_chrome.py            # apply
    python3 ui-visual/_reconcile_chrome.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAINT = HERE
GREY = os.path.join(ROOT, "wireframes")

# The auth variant, where the two trees disagreed. Everything not named here
# takes the variant its grey twin has.
LOGGED_OUT = {
    "how-it-works.html",            # CLAUDE.md, reached pre-auth
    "public-profile.html",
    "public-profile-error.html",
    "public-profile-loading.html",
    "public-profile-not-found.html",
    "cookie-consent.html",          # a consent banner IS a first visit
    "maintenance.html",             # the app is down, there is no session
}
LOGGED_IN = {
    "404.html",                     # do not tell a signed-in person to sign in
    "500.html",
    "toasts.html",
}

# Not product screens, so they have no chrome state to reconcile.
SKIP = {"overview.html"}

VOID = {"br", "img", "input", "use", "path", "circle", "meta", "link",
        "polyline", "source", "rect", "line", "hr", "ellipse", "stop"}


def region(html, tag, cls=None):
    """The outer html of the first <tag> (optionally with class) and its span."""
    pat = r"<%s\b[^>]*?>" % tag if cls is None else \
        r'<%s\b[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls)
    m = re.search(pat, html)
    if not m:
        return None, None, None
    depth, i = 0, m.start()
    for t in re.finditer(r"<(/?)(%s)\b[^>]*?(/?)>" % tag, html[i:]):
        if t.group(1):
            depth -= 1
            if depth == 0:
                return html[i:i + t.end()], i, i + t.end()
        elif not t.group(3):
            depth += 1
    return None, None, None


def read(tree, name):
    path = os.path.join(tree, name)
    if not os.path.exists(path):
        return None
    return open(path, encoding="utf-8").read()


# ----------------------------------------------------------------- state ----


def auth_of(header):
    """The auth variant a header IS. .auth-btns is the Sign in / Sign up pair,
       which exists in that variant and nowhere else."""
    return "out" if 'class="auth-btns"' in header else "in"


def slot_of(nav):
    """Which bottom-nav slot claims to be the current page, or None."""
    for i, attrs in enumerate(re.findall(r"<li\b([^>]*)>", nav)):
        if "aria-current" in attrs:
            return i
    return None


def set_slot(nav, want):
    """aria-current is a claim about where the reader is, so exactly one slot may
       carry it and only the slot that is true. Removing it everywhere first is
       what makes this idempotent."""
    nav = re.sub(r'<li aria-current="page">', "<li>", nav)
    if want is None:
        return nav
    n = [0]

    def sub(m):
        n[0] += 1
        return '<li aria-current="page">' if n[0] - 1 == want else m.group(0)
    return re.sub(r"<li>", sub, nav)


NOTIF_EMPTY = re.compile(r'<p class="notif-empty">.*?</p>', re.S)


def notif_of(header):
    """('empty'|'filled', the See-all href). A dropdown listing three unread
       items on a screen whose whole subject is "you have nothing yet" is not a
       styling difference, it is the screen contradicting itself."""
    if not re.search(r'class="notif-menu"', header):
        return None, None
    href = re.search(r'<a class="notif-all" href="([^"]+)"', header)
    return ("empty" if "notif-empty" in header else "filled",
            href.group(1) if href else None)


def set_notif(header, want, href, grey_header):
    """Carry the grey tree's empty dropdown into the paint. The copy is not
       written here: it is lifted from the wireframe, which owns copy."""
    if want is None or 'class="notif-menu"' not in header:
        return header
    if want == "empty":
        body = NOTIF_EMPTY.search(grey_header or "")
        if not body:
            return header
        drop, a, b = region(header, "div", "notif-drop")
        if drop and "notif-empty" not in drop:
            keep = re.search(r'<a class="notif-all".*?</a>', drop, re.S)
            head = re.match(r'<div[^>]*>', drop).group(0)
            header = header[:a] + head + body.group(0) + \
                (keep.group(0) if keep else "") + "</div>" + header[b:]
        # No unread count, so no badge and no count in the label.
        header = re.sub(r'<span class="badge-dot">[^<]*</span>', "", header)
        header = re.sub(r'<summary aria-label="Notifications[^"]*">',
                        '<summary aria-label="Notifications, none">', header, count=1)
    if href:
        header = re.sub(r'(<a class="notif-all" href=")[^"]*"',
                        lambda m: m.group(1) + href + '"', header)
    return header


CONDENSED = re.compile(r'<div class="cat-condensed".*?</div>\s*(?=</header>)', re.S)


def condensed_of(header):
    m = CONDENSED.search(header)
    return m.group(0) if m else None


def set_condensed(header, strip):
    """The condensed strip and the full category bar are the same control at two
       scroll positions, so a header that has one variant of them and not the
       other is a defect in the variant that lacks it. The painted logged-out
       header had no strip at all: scroll the feed signed out and the categories
       leave the screen with nothing to bring them back."""
    if strip is None or CONDENSED.search(header):
        return header
    return header.replace("</header>", strip + "</header>", 1)


# ------------------------------------------------------------------ main ----


def main():
    check = "--check" in sys.argv
    feed = read(PAINT, "event-feed.html")
    out_feed = read(PAINT, "event-feed-logged-out.html")
    canon = {
        ("header", "in"): region(feed, "header")[0],
        ("header", "out"): region(out_feed, "header")[0],
        ("nav", "in"): region(feed, "nav", "bottom-nav")[0],
        ("nav", "out"): region(out_feed, "nav", "bottom-nav")[0],
    }
    strip = condensed_of(canon[("header", "in")])
    canon[("header", "out")] = set_condensed(canon[("header", "out")], strip)

    changed = 0
    for name in sorted(os.listdir(PAINT)):
        if not name.endswith(".html") or name in SKIP:
            continue
        html = read(PAINT, name)
        grey = read(GREY, name)
        head, ha, hb = region(html, "header")
        nav, na, nb = region(html, "nav", "bottom-nav")
        if not head or not nav:
            continue
        gh = region(grey, "header")[0] if grey else None
        gn = region(grey, "nav", "bottom-nav")[0] if grey else None

        # 1. the auth variant
        want = "out" if name in LOGGED_OUT else "in" if name in LOGGED_IN else \
            (auth_of(gh) if gh else auth_of(head))
        why = []
        if auth_of(head) != want:
            keep = condensed_of(head)
            head = set_condensed(canon[("header", want)], keep or strip)
            nav = canon[("nav", want)]
            why.append("auth->" + want)

        # 2. the active slot, and 3. the notifications dropdown
        slot = slot_of(gn) if gn else slot_of(nav)
        if slot_of(nav) != slot:
            nav = set_slot(nav, slot)
            why.append("slot->%s" % slot)
        head = set_condensed(head, strip)
        gwant, ghref = notif_of(gh) if gh else (None, None)
        before = head
        head = set_notif(head, gwant, ghref, gh)
        if head != before:
            why.append("notif->%s" % gwant)

        # The nav goes back first. It sits below the header in the document, so
        # rewriting it leaves the header's offsets alone; the other order would
        # need arithmetic, and arithmetic here is a bug waiting for a page whose
        # header is a different length.
        new = html[:na] + nav + html[nb:]
        new = new[:ha] + head + new[hb:]
        if new != html:
            changed += 1
            print("%-34s %s" % (name, " ".join(why) or "chrome"))
            if not check:
                open(os.path.join(PAINT, name), "w", encoding="utf-8").write(new)
    print("---", "%d page(s) %s" % (changed, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
