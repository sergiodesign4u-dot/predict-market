#!/usr/bin/env python3
"""
Apply the Pulse colour layer to the event-feed STATE pages (alternative to Signal).

Takes each Signal-themed ui-visual/event-feed-<state>.html and re-skins it to Pulse,
writing ui-visual/event-feed-pulse-<state>.html. Mirrors exactly the by-hand skinning
that produced event-feed-pulse.html:
  - head font link -> Pulse fonts (Space Grotesk / DM Sans / IBM Plex Mono)
  - _theme.css -> _theme-pulse.css
  - Solar Bold icon sprite injected after <body>
  - bookmark x-N / header bell / trust shield + check -> <use> (Solar Bold)
  - sidebar project name + all event-feed state links -> Pulse
  - <title> -> Pulse

Also patches the hand-built event-feed-pulse.html so its sidebar state links point
at the Pulse state files.

Idempotent: regenerates each Pulse state file from its Signal source every run.
NEVER edits wireframes/ or the Signal event-feed*.html / _theme.css.
"""
import re
import pathlib

UIV = pathlib.Path(__file__).resolve().parent

# (state slug, <title> suffix)
STATES = [
    ("empty", "empty"),
    ("error", "error"),
    ("loading", "loading"),
    ("push-permission-missing", "push-permission missing"),
    ("logged-out", "logged out"),
    ("logged-out-empty", "logged out, empty"),
    ("logged-out-error", "logged out, error"),
    ("logged-out-loading", "logged out, loading"),
]

# every event-feed page slug (""=success) so sidebar / uv-bar links retarget to Pulse
SLUGS = ["", "empty", "error", "loading", "push-permission-missing",
         "logged-out", "logged-out-empty", "logged-out-error", "logged-out-loading"]

FONT_OLD = ('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
            '&family=Sora:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')
FONT_NEW = ('<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700'
            '&family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">')

# Solar Bold sprite (identical to the one hand-injected into event-feed-pulse.html)
SPRITE = '''  <!-- Solar Bold icon sprite (Pulse): filled glyphs referenced via <use>; rendered filled by _theme-pulse.css .ic:has(use) -->
  <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
    <symbol id="i-bookmark-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M21 11.098v4.993c0 3.096 0 4.645-.734 5.321c-.35.323-.792.526-1.263.58c-.987.113-2.14-.907-4.445-2.946c-1.02-.901-1.529-1.352-2.118-1.47a2.2 2.2 0 0 0-.88 0c-.59.118-1.099.569-2.118 1.47c-2.305 2.039-3.458 3.059-4.445 2.945a2.24 2.24 0 0 1-1.263-.579C3 20.736 3 19.188 3 16.091v-4.994C3 6.81 3 4.666 4.318 3.333S7.758 2 12 2s6.364 0 7.682 1.332S21 6.81 21 11.098M8.25 6A.75.75 0 0 1 9 5.25h6a.75.75 0 0 1 0 1.5H9A.75.75 0 0 1 8.25 6" clip-rule="evenodd"/></symbol>
    <symbol id="i-bell-b" viewBox="0 0 24 24"><path fill="currentColor" d="M18.75 9.71v-.705C18.75 5.136 15.726 2 12 2S5.25 5.136 5.25 9.005v.705a4.4 4.4 0 0 1-.692 2.375L3.45 13.81c-1.011 1.575.062 3.68 1.966 3.843a51 51 0 0 0 13.167 0c1.904-.163 2.977-2.268 1.966-3.843l-1.108-1.725a4.4 4.4 0 0 1-.692-2.375"/><path fill="currentColor" d="M7.243 18.545a5.002 5.002 0 0 0 9.513 0c-3.145.28-6.367.281-9.513 0"/></symbol>
    <symbol id="i-shield-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.378 5.082C3 5.62 3 7.22 3 10.417v1.574c0 5.638 4.239 8.375 6.899 9.536c.721.315 1.082.473 2.101.473c1.02 0 1.38-.158 2.101-.473C16.761 20.365 21 17.63 21 11.991v-1.574c0-3.198 0-4.797-.378-5.335c-.377-.537-1.88-1.052-4.887-2.081l-.573-.196C13.595 2.268 12.812 2 12 2s-1.595.268-3.162.805L8.265 3c-3.007 1.03-4.51 1.545-4.887 2.082M15.06 10.5a.75.75 0 0 0-1.12-.999l-3.011 3.374l-.87-.974a.75.75 0 0 0-1.118 1l1.428 1.6a.75.75 0 0 0 1.119 0z" clip-rule="evenodd"/></symbol>
    <symbol id="i-verified-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M9.592 3.2a6 6 0 0 1-.495.399c-.298.2-.633.338-.985.408c-.153.03-.313.043-.632.068c-.801.064-1.202.096-1.536.214a2.71 2.71 0 0 0-1.655 1.655c-.118.334-.15.735-.214 1.536a6 6 0 0 1-.068.632c-.07.352-.208.687-.408.985c-.087.13-.191.252-.399.495c-.521.612-.782.918-.935 1.238c-.353.74-.353 1.6 0 2.34c.153.32.414.626.935 1.238c.208.243.312.365.399.495c.2.298.338.633.408.985c.03.153.043.313.068.632c.064.801.096 1.202.214 1.536a2.71 2.71 0 0 0 1.655 1.655c.334.118.735.15 1.536.214c.319.025.479.038.632.068c.352.07.687.209.985.408c.13.087.252.191.495.399c.612.521.918.782 1.238.935c.74.353 1.6.353 2.34 0c.32-.153.626-.414 1.238-.935c.243-.208.365-.312.495-.399c.298-.2.633-.338.985-.408c.153-.03.313-.043.632-.068c.801-.064 1.202-.096 1.536-.214a2.71 2.71 0 0 0 1.655-1.655c.118-.334.15-.735.214-1.536c.025-.319.038-.479.068-.632c.07-.352.209-.687.408-.985c.087-.13.191-.252.399-.495c.521-.612.782-.918.935-1.238c.353-.74.353-1.6 0-2.34c-.153-.32-.414-.626-.935-1.238a6 6 0 0 1-.399-.495a2.7 2.7 0 0 1-.408-.985a6 6 0 0 1-.068-.632c-.064-.801-.096-1.202-.214-1.536a2.71 2.71 0 0 0-1.655-1.655c-.334-.118-.735-.15-1.536-.214a6 6 0 0 1-.632-.068a2.7 2.7 0 0 1-.985-.408a6 6 0 0 1-.495-.399c-.612-.521-.918-.782-1.238-.935a2.71 2.71 0 0 0-2.34 0c-.32.153-.626.414-1.238.935m6.781 6.663a.814.814 0 0 0-1.15-1.15l-4.85 4.85l-1.596-1.595a.814.814 0 0 0-1.15 1.15l2.17 2.17a.814.814 0 0 0 1.15 0z" clip-rule="evenodd"/></symbol>
  </defs></svg>
'''

# scoped icon swaps (full-element matches so only the intended glyphs convert)
BELL_OLD = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>')
BELL_NEW = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-bell-b"/></svg>'
SHIELD_OLD = ('<svg class="ft-ic" viewBox="0 0 24 24" aria-hidden="true">'
              '<path d="M12 3l7 3v6c0 4-3 6.5-7 9-4-2.5-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>')
SHIELD_NEW = '<svg class="ft-ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-shield-b"/></svg>'
CHECK_OLD = ('<svg class="ft-ic" viewBox="0 0 24 24" aria-hidden="true">'
             '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>')
CHECK_NEW = '<svg class="ft-ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-verified-b"/></svg>'
BOOKMARK_OLD = '<path d="M6 3h12v18l-6-4-6 4z"/>'
BOOKMARK_NEW = '<use href="#i-bookmark-b"/>'


def link_map(html):
    """Retarget every event-feed*.html sidebar/uv-bar link (and any sign-in target) to the Pulse copy."""
    for slug in SLUGS:
        base = "event-feed.html" if slug == "" else f"event-feed-{slug}.html"
        dst = "event-feed-pulse.html" if slug == "" else f"event-feed-pulse-{slug}.html"
        html = html.replace(f'href="{base}"', f'href="{dst}"')
        html = html.replace(f'data-loggedin-target="{base}"', f'data-loggedin-target="{dst}"')
    return html


def skin(html, title_suffix):
    html = html.replace('href="_theme.css"', 'href="_theme-pulse.css"')
    html = html.replace(FONT_OLD, FONT_NEW)
    html = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + "\n" + SPRITE, html, count=1)
    html = html.replace(BOOKMARK_OLD, BOOKMARK_NEW)
    html = html.replace(BELL_OLD, BELL_NEW)
    html = html.replace(SHIELD_OLD, SHIELD_NEW)
    html = html.replace(CHECK_OLD, CHECK_NEW)
    html = html.replace('UI + Visual - screens', 'UI + Visual - Pulse')
    html = re.sub(r'<title>.*?</title>',
                  f'<title>UI Visual - Event Feed - Pulse ({title_suffix})</title>',
                  html, count=1, flags=re.S)
    html = link_map(html)
    return html


if __name__ == "__main__":
    for slug, suffix in STATES:
        src = UIV / f"event-feed-{slug}.html"
        out = skin(src.read_text(), suffix)
        dest = UIV / f"event-feed-pulse-{slug}.html"
        dest.write_text(out)
        print("built", dest.name)
    # patch the hand-built success page so its sidebar state links point at the Pulse states
    succ = UIV / "event-feed-pulse.html"
    succ.write_text(link_map(succ.read_text()))
    print("patched event-feed-pulse.html links")
