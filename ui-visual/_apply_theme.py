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
transforms on them: product .html links -> "#", and the Favorites heart -> bookmark.
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


def neutralize(frag):
    """Grey wireframe fragment -> concept-stand fragment (links dead, heart -> bookmark)."""
    frag = re.sub(r'href="[^"]*\.html[^"]*"', 'href="#"', frag)
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


def build(slug, wf_name, logged_out, title_suffix):
    wf = (WF / wf_name).read_text()
    out = SHELL

    # main (always)
    _, _, wf_main = block(wf, '<main class="feed">', "</main>")
    out = swap(out, '<main class="feed">', "</main>", distill(neutralize(wf_main)))

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
