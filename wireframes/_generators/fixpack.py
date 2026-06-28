"""Idempotent fixpack post-processor (run after the generators).

Fixes three reported defects across wireframes/*.html:
  1. Dialog CSS missing on the 9 hand-authored event-feed pages (dialog markup +
     JS were injected, but the CSS rules were not, so the dialog rendered broken).
  2. Logged-in header controls were dead <button>s (Favorites, Notifications bell,
     avatar-dropdown items) - wire them to their target pages.
  3. Bottom-nav slots were dead <button>s - wire Events / My Bets / Favorites /
     Portfolio (logged-in) and Events (logged-out); logged-out My Bets / Favorites
     open the sign-in dialog.

Idempotent: each replacement is skipped when its wired form is already present.
"""
import re
import pathlib
import _shell as S

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

# ---- 1. Dialog CSS (self-contained: every rule the signin / deposit dialogs use) ----
DIALOG_CSS = """
    /* ---- Shared in-page dialogs (native <dialog>) - injected for event-feed family ---- */
    dialog.app-dialog { width: 92%; max-width: 420px; border: 1px solid #999; background: #f0f0f0; color: #222; padding: 0; }
    dialog.app-dialog::backdrop { background: rgba(0,0,0,.4); }
    dialog.app-dialog .sheet-head { display: flex; align-items: center; justify-content: space-between; padding: 8px 10px; border-bottom: 1px solid #ccc; }
    dialog.app-dialog .sheet-head h2 { font-size: 14px; margin: 0; }
    dialog.app-dialog .sheet-close { border: 1px solid #888; background: #d6d6d6; font-size: 12px; cursor: pointer; padding: 2px 8px; }
    dialog.app-dialog .sheet-body { padding: 10px; display: flex; flex-direction: column; gap: 10px; }
    dialog.app-dialog .fine { font-size: 11px; color: #555; line-height: 1.5; }
    dialog.app-dialog .field-label { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: #555; }
    dialog.app-dialog .amount-row { display: flex; align-items: center; gap: 8px; }
    dialog.app-dialog .amount-input { flex: 1; border: 1px solid #888; background: #fff; padding: 10px; font-size: 18px; }
    dialog.app-dialog .quick { display: flex; gap: 6px; flex-wrap: wrap; }
    dialog.app-dialog .quick button { border: 1px solid #888; background: #d6d6d6; padding: 6px 10px; font-size: 12px; cursor: pointer; }
    dialog.app-dialog .quick button.sel { background: #b8b8b8; font-weight: bold; }
    dialog.app-dialog .provider-btn { display: flex; align-items: center; gap: 10px; border: 1px solid #888; background: #d6d6d6; padding: 12px; font-size: 13px; cursor: pointer; width: 100%; text-align: left; }
    dialog.app-dialog .provider-btn .ic { width: 18px; height: 18px; }
    dialog.app-dialog .widget-box { border: 1px dashed #999; background: #ededed; min-height: 160px; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #555; text-align: center; padding: 8px; }
    dialog.app-dialog .protect { border: 1px solid #999; background: #e6e6e6; padding: 8px; font-size: 11px; }
    dialog.app-dialog .confirm-btn { border: 1px solid #888; background: #c4c4c4; padding: 12px; font-size: 14px; font-weight: bold; cursor: pointer; width: 100%; }
    .dlg-note { font-size: 10px; color: #555; padding: 6px 10px; border-top: 1px dashed #bbb; margin: 0; }
"""


def fix_dialog_css(html):
    if 'id="signinDialog"' not in html:
        return html, False          # no dialog on this page
    if 'dialog.app-dialog {' in html:
        return html, False          # CSS already present
    new = html.replace("\n  </style>", DIALOG_CSS + "  </style>", 1)
    if new == html:                 # fallback: some pages use "</style>" without 2-space indent
        new = html.replace("</style>", DIALOG_CSS + "</style>", 1)
    return new, new != html


# ---- 2. Header wiring -------------------------------------------------------
def _extract(pattern):
    m = re.search(pattern, S.HEADER_IN_OPEN, re.S)
    assert m, "header block not found: " + pattern
    return m.group(0)

FAV_OLD = _extract(r' *<button type="button" class="icon-btn desk-only" aria-label="Favorites">.*?</button>')
BELL_OLD = _extract(r' *<button type="button" class="icon-btn" aria-label="Notifications, 3 unread">.*?</button>')

FAV_NEW = '<a href="favorites.html" aria-label="Favorites, see saved events">' + FAV_OLD.strip() + '</a>'
# keep the original indentation of the favorites button line
FAV_NEW = FAV_OLD[:len(FAV_OLD) - len(FAV_OLD.lstrip())] + FAV_NEW
BELL_NEW = BELL_OLD[:len(BELL_OLD) - len(BELL_OLD.lstrip())] + \
    '<a href="notifications.html">' + BELL_OLD.strip() + '</a>'

AVATAR = [
    ('My Profile', 'my-profile.html'),
    ('My Bets', 'active-bets.html'),
    ('Wallet / Deposit', 'wallet.html'),
    ('How It Works', 'how-it-works.html'),
    ('Logout', 'event-feed-logged-out.html'),
]


def wire_header(html):
    changed = False
    for old, new in ((FAV_OLD, FAV_NEW), (BELL_OLD, BELL_NEW)):
        if new in html:
            continue
        if old in html:
            html = html.replace(old, new, 1)
            changed = True
    for label, href in AVATAR:
        old = f'<li><button type="button" role="menuitem">{label}</button></li>'
        new = f'<li><a href="{href}"><button type="button" role="menuitem">{label}</button></a></li>'
        if new in html:
            continue
        if old in html:
            html = html.replace(old, new, 1)
            changed = True
    return html, changed


# ---- 3. Bottom-nav wiring (block-based, idempotent) ------------------------
# Works on the actual <nav class="bottom-nav"> found in each file, so it handles
# every variant (logged-in active=any/none, logged-out, hand-authored pages whose
# comment / Sign-in icon differs from the generator) uniformly.
def _wrap_btn(nav, label, attr):
    pat = re.compile(
        r'(<a [^>]*>\s*)?'                                  # 1: existing <a> wrap
        r'<button type="button"'
        r'((?: aria-label="[^"]*")?)'                        # 2: aria-label
        r'((?: data-open="[^"]*")?)>'                        # 3: existing data-open
        r'((?:(?!</button>).)*?<span>' + re.escape(label) + r'</span>\s*)'  # 4: inner
        r'</button>(\s*</a>)?', re.S)
    m = pat.search(nav)
    if not m or m.group(1) or m.group(3):
        return nav                                          # missing, or already wired
    btn = f'<button type="button"{m.group(2)}{{extra}}>{m.group(4)}</button>'
    if attr.startswith('href'):
        new = f'<a {attr}>' + btn.format(extra='') + '</a>'
    else:
        new = btn.format(extra=' ' + attr)
    return nav[:m.start()] + new + nav[m.end():]

IN_SLOTS = [('Events', 'href="event-feed.html"'), ('My Bets', 'href="active-bets.html"'),
            ('Favorites', 'href="favorites.html"'), ('Portfolio', 'href="my-profile.html"')]
OUT_SLOTS = [('Events', 'href="event-feed-logged-out.html"'), ('My Bets', 'data-open="signin"'),
             ('Favorites', 'data-open="signin"')]


def wire_bottom(html):
    changed = [False]

    def repl(m):
        nav = m.group(0)
        out = '<span>Sign in</span>' in nav or 'logged-out slot 4 = Sign in' in nav
        for label, attr in (OUT_SLOTS if out else IN_SLOTS):
            nav2 = _wrap_btn(nav, label, attr)
            if nav2 != nav:
                changed[0] = True
            nav = nav2
        return nav

    html = re.sub(r'<nav class="bottom-nav".*?</nav>', repl, html, flags=re.S)
    return html, changed[0]


# ---- run -------------------------------------------------------------------
stats = {"dialog": [], "header": [], "bottom": []}
for p in sorted(ROOT.glob("*.html")):
    txt = p.read_text()
    orig = txt
    txt, c1 = fix_dialog_css(txt)
    if c1:
        stats["dialog"].append(p.name)
    txt, c2 = wire_header(txt)
    if c2:
        stats["header"].append(p.name)
    txt, c3 = wire_bottom(txt)
    if c3:
        stats["bottom"].append(p.name)
    if txt != orig:
        if "—" in txt:
            raise SystemExit("EM-DASH introduced in " + p.name)
        p.write_text(txt)

for k, v in stats.items():
    print(f"{k}: {len(v)} pages")
