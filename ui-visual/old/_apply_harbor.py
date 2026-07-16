#!/usr/bin/env python3
"""
Build the Harbor Event Feed family from the Pulse one.

Harbor and Pulse share the exact same structure, fonts (Space Grotesk / DM Sans /
IBM Plex Mono), Solar Bold icon sprite and <use> icons - they differ ONLY in the
colour layer (the linked stylesheet). So each Harbor page is its Pulse twin with:
  - _theme-pulse.css  -> _theme-harbor.css   (navy calm + magenta-pink gradient)
  - "UI + Visual - Pulse" / title "... - Pulse"  -> "... - Harbor"
  - every event-feed-pulse*.html link (+ sign-in target) -> event-feed-harbor*.html

Covers success + all 8 states. Idempotent: regenerates each Harbor page from its
Pulse source every run. NEVER edits wireframes/ or the Signal / Pulse sources.
"""
import re
import pathlib

UIV = pathlib.Path(__file__).resolve().parent

SLUGS = ["", "empty", "error", "loading", "push-permission-missing",
         "logged-out", "logged-out-empty", "logged-out-error", "logged-out-loading"]


def pulse_name(slug):
    return "event-feed-pulse.html" if slug == "" else f"event-feed-pulse-{slug}.html"


def harbor_name(slug):
    return "event-feed-harbor.html" if slug == "" else f"event-feed-harbor-{slug}.html"


if __name__ == "__main__":
    for slug in SLUGS:
        html = (UIV / pulse_name(slug)).read_text()
        html = html.replace('_theme-pulse.css', '_theme-harbor.css')  # <link> + sprite comment
        html = html.replace('icon sprite (Pulse)', 'icon sprite (Harbor)')
        html = html.replace('UI + Visual - Pulse', 'UI + Visual - Harbor')
        html = html.replace('UI Visual - Event Feed - Pulse', 'UI Visual - Event Feed - Harbor')
        for s in SLUGS:
            html = html.replace(f'href="{pulse_name(s)}"', f'href="{harbor_name(s)}"')
            html = html.replace(f'data-loggedin-target="{pulse_name(s)}"',
                                f'data-loggedin-target="{harbor_name(s)}"')
        (UIV / harbor_name(slug)).write_text(html)
        print("built", harbor_name(slug))
