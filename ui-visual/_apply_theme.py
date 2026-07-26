#!/usr/bin/env python3
"""
Apply the Signal colour layer to the event-feed STATE pages.

Strategy: "shell + swap". ui-visual/event-feed.html is the finished, themed shell
(head links, roadmap sidebar, uv-bar, transformed header / bottom-nav / footer,
redesigned How-it-works dialog, scripts). For each state page we start from that
shell and swap in ONLY the regions that differ from the logged-in base:
  - logged-in states (empty/error/loading/push): swap <main> only.
  - logged-out states: swap <header>, <main>, and the mobile <nav.bottom-nav>.
Grafted fragments come from wireframes/ (grey), so we run two voice-safe text
transforms on them: the Favorites heart -> bookmark, and a product link is kept
if the screen it points at has been painted (only an unpainted destination is
flattened to "#"; see _relink.py, which repaired the pages this file used to
flatten wholesale).
Everything the theme needs is class-based, so the swapped content colours itself.

Idempotent: re-running regenerates each state file from the current shell.
NEVER edits wireframes/ and NEVER regenerates the base event-feed.html.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UIV = ROOT / "ui-visual"
WF = ROOT / "wireframes"

SHELL = (UIV / "event-feed.html").read_text()

# What the painted tree can be linked to, and the one family the colour pass
# renamed on the way in (grey politics.html is painted as event-feed-politics.html).
PAINTED = {p.name for p in UIV.glob("*.html")}
RENAME = {"%s.html" % c: "event-feed-%s.html" % c
          for c in ("politics", "crypto", "culture", "general")}

HEART = "M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"
BOOKMARK = "M6 3h12v18l-6-4-6 4z"

# (state slug, wireframe filename, logged_out?, <title> suffix)
STATES = [
    ("empty", "event-feed-empty.html", False, "empty state"),
    ("error", "event-feed-error.html", False, "error state"),
    ("loading", "event-feed-loading.html", False, "loading state"),
    ("push-permission-missing", "event-feed-push-permission-missing.html", False, "push-permission missing"),
    ("logged-out", "event-feed-logged-out.html", True, "logged out"),
    ("logged-out-empty", "event-feed-logged-out-empty.html", True, "logged out, empty"),
    ("logged-out-error", "event-feed-logged-out-error.html", True, "logged out, error"),
    ("logged-out-loading", "event-feed-logged-out-loading.html", True, "logged out, loading"),
]


def block(html, open_marker, close_tag):
    """Return the substring from open_marker's start through close_tag (inclusive)."""
    s = html.index(open_marker)
    e = html.index(close_tag, s) + len(close_tag)
    return s, e, html[s:e]


def swap(html, open_marker, close_tag, new):
    s, e, _ = block(html, open_marker, close_tag)
    return html[:s] + new + html[e:]


def keep_or_kill(m):
    """A grey link the painted tree can honour, or '#'.

    This used to flatten every product link without asking, which is how the
    whole coloured product ended up with no navigation (fixed by _relink.py).
    Where a link goes is structure and structure belongs to the wireframes, so
    the only thing worth deciding here is whether the destination has been
    painted yet: if it has, the link stands; if it has not, pointing at it
    would be a broken link rather than a dead one.
    """
    href = m.group(1)
    base, _, frag = href.partition("#")
    base = RENAME.get(base.split("?")[0], base.split("?")[0])
    if base in PAINTED:
        return 'href="%s"' % (base + ("#" + frag if frag else ""))
    return 'href="#"'


def neutralize(frag):
    """Grey wireframe fragment -> painted fragment (heart -> bookmark)."""
    frag = re.sub(r'href="([^"]*\.html[^"]*)"', keep_or_kill, frag)
    frag = frag.replace(HEART, BOOKMARK)
    return frag


def distill(frag):
    """Match the reference screen's /distill pass: drop the duplicate Category
    dropdown (the chip band already covers it), the 'Volatile' trader-jargon sort,
    and the reverse-sort toggle. Idempotent no-op where a block is absent."""
    frag = re.sub(r'\s*<details class="filter-menu" id="catMenu">.*?</details>', "", frag, flags=re.S)
    frag = re.sub(r'\s*<li><label><input type="radio" name="sort" value="Volatile">\s*Volatile</label></li>', "", frag)
    frag = re.sub(r'\s*<div class="reverse-row">.*?</div>', "", frag, flags=re.S)
    return frag


# The themed second-level category bar lives inside <main> on the reference screen,
# so swapping the whole <main> would drop it. Grab it once and re-inject it into each
# state main, and put the head + state content on the same stone plate the feed uses,
# so a state page reads as "the same feed, minus the cards", not a decapitated page.
_, _, SHELL_CATNAV = block(SHELL, '<nav class="cat-nav"', "</nav>")


def wrap_state_main(main_frag):
    """Add the category bar and wrap the head + state content in .cat-layout/.cat-main
    (the shared stone-plate structure), so states match event-feed.html's chrome."""
    frag = main_frag.replace(
        '<div class="feed-inner">',
        '<div class="feed-inner">\n        ' + SHELL_CATNAV
        + '\n        <div class="cat-layout">\n        <div class="cat-main">',
        1,
    )
    cut = frag.rfind("</div>", 0, frag.rfind("</main>"))   # feed-inner's closing tag
    return frag[:cut] + "</div><!-- /cat-main --></div><!-- /cat-layout -->\n      " + frag[cut:]


def build(slug, wf_name, logged_out, title_suffix):
    wf = (WF / wf_name).read_text()
    out = SHELL

    # main (always). Inject the category bar + shared plate AFTER neutralize so the
    # bar's real category hrefs (event-feed-politics.html ...) survive and navigate.
    _, _, wf_main = block(wf, '<main class="feed">', "</main>")
    out = swap(out, '<main class="feed">', "</main>", wrap_state_main(distill(neutralize(wf_main))))

    if logged_out:
        _, _, wf_header = block(wf, '<header class="app-header">', "</header>")
        out = swap(out, '<header class="app-header">', "</header>", neutralize(wf_header))
        _, _, wf_nav = block(wf, '<nav class="bottom-nav"', "</nav>")
        out = swap(out, '<nav class="bottom-nav"', "</nav>", neutralize(wf_nav))

    # title + uv-bar provenance
    out = re.sub(
        r"<title>.*?</title>",
        f"<title>Concept - Event Feed ({title_suffix})</title>",
        out, count=1, flags=re.S,
    )
    out = out.replace(
        "Color copy of wireframes/event-feed.html",
        f"Color copy of wireframes/{wf_name}",
        1,
    )

    dest = UIV / f"event-feed-{slug}.html"
    dest.write_text(out)
    return dest.name


if __name__ == "__main__":
    for slug, wf_name, logged_out, title_suffix in STATES:
        name = build(slug, wf_name, logged_out, title_suffix)
        print(f"built {name}")
