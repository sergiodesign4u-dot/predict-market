#!/usr/bin/env python3
"""
Apply the Vault colour layer to the remaining non-feed / non-detail families,
one general applicator for all of them (Active Bets, Wallet, Notifications,
Profile, Win/Loss, Favorites, How It Works, System, ...).

Same "shell + swap" as _apply_theme.py / _apply_detail.py: ui-visual/event-feed.html
is the finished, themed shell (head links, roadmap sidebar, uv-bar, themed header /
bottom-nav / footer, dialogs, scripts). For every page we start from that shell and:
  1. swap the shell's <main class="feed"> for the wireframe's <main> content,
     re-wrapped in one feed-inner > cat-layout > cat-main so it rides the same
     two-stone slab the feed uses (a raw .state-block is wrapped the same way,
     matching event-feed-*-error);
  2. graft the family's own grey inline LAYOUT CSS into <head>; _theme.css, linked
     after, re-skins the colour (Vault rules for the family's components live there);
  3. for logged-out variants, swap the header + mobile bottom-nav too;
  4. neutralise product .html links to "#", except a per-family keep-list (e.g. the
     Active / History tabs point at each other, which DO exist in ui-visual).

Idempotent. NEVER edits wireframes/, NEVER regenerates event-feed.html.
Run:  python3 _apply_family.py [family ...]   then   python3 _resync_sidebar.py
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UIV = ROOT / "ui-visual"
WF = ROOT / "wireframes"

SHELL = (UIV / "event-feed.html").read_text()

HEART = "M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"
BOOKMARK = "M6 3h12v18l-6-4-6 4z"


# ---- families: dest -> (wireframe, logged_out, title). keep = live intra-links.
FAMILIES = {
    "win-loss": {
        "kind": "overlay",
        "keep": ("active-bets.html", "event-feed.html"),
        "pages": [
            # (dest, wireframe, variant, title). variant -> win-dialog / loss-dialog accent.
            ("win.html",              "win.html",              "win",  "Win - You were right"),
            ("win-payout-pending.html","win-payout-pending.html","win",  "Win - payout pending"),
            ("win-loading.html",      "win-loading.html",      "win",  "Win - loading"),
            ("win-error.html",        "win-error.html",        "win",  "Win - error"),
            ("loss.html",             "loss.html",             "loss", "Loss - Here is what happened"),
            ("loss-loading.html",     "loss-loading.html",     "loss", "Loss - loading"),
        ],
    },
    "notifications": {
        "keep": (),
        "pages": [
            ("notifications.html",         "notifications.html",         False, "Notifications"),
            ("notifications-empty.html",   "notifications-empty.html",   False, "Notifications, empty"),
            ("notifications-error.html",   "notifications-error.html",   False, "Notifications, error"),
            ("notifications-loading.html", "notifications-loading.html", False, "Notifications, loading"),
            ("notifications-push.html",    "notifications-push.html",    False, "Notifications, push permission"),
        ],
    },
    "wallet": {
        "keep": (),
        "pages": [
            ("wallet.html",         "wallet.html",         False, "Wallet"),
            ("wallet-loading.html", "wallet-loading.html", False, "Wallet, loading"),
            ("wallet-error.html",   "wallet-error.html",   False, "Wallet, error"),
        ],
    },
    "my-profile": {
        "keep": ("active-bets.html", "wallet.html"),
        "pages": [
            ("my-profile.html",         "my-profile.html",         False, "My Profile"),
            ("my-profile-loading.html", "my-profile-loading.html", False, "My Profile, loading"),
            ("my-profile-error.html",   "my-profile-error.html",   False, "My Profile, error"),
        ],
    },
    "public-profile": {
        "keep": (),
        "pages": [
            ("public-profile.html",           "public-profile.html",           False, "Public Profile"),
            ("public-profile-loading.html",   "public-profile-loading.html",   False, "Public Profile, loading"),
            ("public-profile-error.html",     "public-profile-error.html",     False, "Public Profile, error"),
            ("public-profile-not-found.html", "public-profile-not-found.html", False, "Public Profile, not found"),
        ],
    },
    "favorites": {
        "keep": (),
        "pages": [
            ("favorites.html",         "favorites.html",         False, "Favorites"),
            ("favorites-empty.html",   "favorites-empty.html",   False, "Favorites, empty"),
            ("favorites-loading.html", "favorites-loading.html", False, "Favorites, loading"),
        ],
    },
    "how-it-works": {
        "keep": ("event-feed.html",),
        "pages": [
            ("how-it-works.html", "how-it-works.html", False, "How It Works"),
        ],
    },
    "sign-in": {
        "kind": "overlay",
        "keep": ("event-feed.html", "deposit.html"),
        "close": "event-feed.html",
        "pages": [
            ("sign-in.html",                  "sign-in.html",                  "signin", "Sign in"),
            ("sign-in-loading.html",          "sign-in-loading.html",          "signin", "Sign in, loading"),
            ("sign-in-error.html",            "sign-in-error.html",            "signin", "Sign in, error"),
            ("sign-in-provider-conflict.html","sign-in-provider-conflict.html","signin", "Sign in, provider conflict"),
        ],
    },
    "deposit": {
        "kind": "overlay",
        "keep": ("event-feed.html", "wallet.html"),
        "close": "event-feed.html",
        "pages": [
            ("deposit.html",                    "deposit.html",                    "deposit", "Add funds"),
            ("deposit-loading.html",            "deposit-loading.html",            "deposit", "Add funds, loading"),
            ("deposit-pending.html",            "deposit-pending.html",            "deposit", "Payment pending"),
            ("deposit-error-card.html",         "deposit-error-card.html",         "deposit", "Card declined"),
            ("deposit-error-kyc.html",          "deposit-error-kyc.html",          "deposit", "Verification rejected"),
            ("deposit-minimum-not-met.html",    "deposit-minimum-not-met.html",    "deposit", "Add funds, minimum not met"),
            ("deposit-widget-load-failure.html","deposit-widget-load-failure.html","deposit", "Payment did not load"),
        ],
    },
    "system": {
        "keep": ("event-feed.html",),
        "pages": [
            ("404.html",            "404.html",            False, "404 Not Found"),
            ("500.html",            "500.html",            False, "500 Server Error"),
            ("maintenance.html",    "maintenance.html",    False, "Maintenance"),
            ("cookie-consent.html", "cookie-consent.html", False, "Cookie consent"),
            ("toasts.html",         "toasts.html",         False, "Toasts"),
        ],
    },
    "active-bets": {
        "keep": ("active-bets.html", "active-bets-history.html"),
        "pages": [
            ("active-bets.html",               "active-bets.html",               False, "Active"),
            ("active-bets-loading.html",        "active-bets-loading.html",        False, "Active, loading"),
            ("active-bets-error.html",          "active-bets-error.html",          False, "Active, error"),
            ("active-bets-empty-new.html",      "active-bets-empty-new.html",      False, "Active, empty (new)"),
            ("active-bets-empty-resolved.html", "active-bets-empty-resolved.html", False, "Active, empty (resolved)"),
            ("active-bets-history.html",        "active-bets-history.html",        False, "History"),
            ("active-bets-history-loading.html","active-bets-history-loading.html",False, "History, loading"),
            ("active-bets-history-error.html",  "active-bets-history-error.html",  False, "History, error"),
            ("active-bets-history-empty.html",  "active-bets-history-empty.html",  False, "History, empty"),
        ],
    },
}


def block(html, open_marker, close_tag):
    s = html.index(open_marker)
    e = html.index(close_tag, s) + len(close_tag)
    return s, e, html[s:e]


def swap(html, open_marker, close_tag, new):
    s, e, _ = block(html, open_marker, close_tag)
    return html[:s] + new + html[e:]


def neutralize(frag, keep=()):
    """Product .html links -> '#', except targets in `keep` (they exist in ui-visual)."""
    def repl(m):
        base = m.group(1).split("#")[0].split("?")[0]
        return m.group(0) if any(base == k or base.endswith("/" + k) for k in keep) else 'href="#"'
    return re.sub(r'href="([^"]*\.html[^"]*)"', repl, frag)


def neutralize_chrome(frag, keep=()):
    return neutralize(frag, keep).replace(HEART, BOOKMARK)


def first_style(html):
    s = html.index("<style>")
    e = html.index("</style>", s)
    return s, e, html[s + len("<style>"):e]


SHELL_STYLE_LINES = {ln.strip() for ln in first_style(SHELL)[2].splitlines()}


def graft_css(out, wf):
    """Graft the family's grey inline LAYOUT CSS (the lines the shell's <style>
    lacks) before </style>; _theme.css, linked after, re-skins the colour."""
    css = first_style(wf)[2]
    extra = [ln for ln in css.splitlines()
             if ln.strip() and ln.strip() not in SHELL_STYLE_LINES]
    if not extra:
        return out
    graft = ("\n    /* ---- family layout, grafted from the wireframe; "
             "_theme.css re-skins colour ---- */\n" + "\n".join(extra) + "\n  ")
    _, e, _ = first_style(out)
    return out[:e] + graft + out[e:]


def strip_feed_inner(inner):
    """Remove a wireframe's own <div class="feed-inner"> wrapper by balanced matching."""
    tag = '<div class="feed-inner">'
    i = inner.find(tag)
    if i < 0:
        return inner
    j = i + len(tag)
    depth = 1
    for m in re.finditer(r"<div\b|</div>", inner[j:]):
        if m.group() == "</div>":
            depth -= 1
            if depth == 0:
                cs, ce = j + m.start(), j + m.end()
                return inner[:i] + inner[j:cs] + inner[ce:]
        else:
            depth += 1
    return inner


def _balanced_div(frag, open_marker):
    i = frag.find(open_marker)
    if i < 0:
        return None
    j = frag.index(">", i) + 1
    depth = 1
    for m in re.finditer(r"<div\b|</div>", frag[j:]):
        if m.group() == "</div>":
            depth -= 1
            if depth == 0:
                end = j + m.end()
                return (i, end, frag[i:end])
        else:
            depth += 1
    return None


def tag_pos_sides(inner):
    """Tag each .pos-side chip so the theme can tint it (outcome semantics):
    YES / NO -> green / red side; WON / LOST -> green / red result. The win/lose
    colour is reserved for outcomes, so a resolved-bet result reads at a glance.
    No-op on families without .pos-side."""
    def repl(m):
        txt = m.group(1)
        up = txt.strip().upper()
        if up.startswith("YES"):
            cls = "pos-side pos-yes"
        elif up.startswith("NO"):
            cls = "pos-side pos-no"
        elif up.startswith("WON"):
            cls = "pos-side pos-won"
        elif up.startswith("LOST"):
            cls = "pos-side pos-lost"
        else:
            cls = "pos-side"
        return f'<span class="{cls}">{txt}</span>'
    return re.sub(r'<span class="pos-side">(.*?)</span>', repl, inner, flags=re.S)


def wrap_content_plate(inner):
    """Re-wrap the content in feed-inner > cat-layout > cat-main so it rides the
    two-stone slab. A raw .state-block (empty / error) is wrapped the same way, so
    it matches event-feed-*-error (the state-block goes borderless via _theme.css)."""
    if 'class="cat-layout"' in inner:
        return inner
    body = inner.strip()
    return ('<div class="cat-layout">\n        <div class="cat-main">\n        '
            + body + '\n        </div><!-- /cat-main --></div><!-- /cat-layout -->')


def build(dest, wf_name, logged_out, title, keep):
    wf = (WF / wf_name).read_text()

    _, _, wf_main = block(wf, '<main class="feed">', "</main>")
    inner = wf_main[len('<main class="feed">'):-len("</main>")]
    inner = strip_feed_inner(inner)
    inner = neutralize(inner, keep).replace(' style="background:#e0e0e0;"', "")
    inner = tag_pos_sides(inner)
    inner = wrap_content_plate(inner)
    new_main = ('<main class="feed">\n      <div class="feed-inner">\n        '
                + inner + '</div><!-- /feed-inner -->\n    </main>')
    out = swap(SHELL, '<main class="feed">', "</main>", new_main)

    if logged_out:
        _, _, wf_header = block(wf, '<header class="app-header">', "</header>")
        out = swap(out, '<header class="app-header">', "</header>", neutralize_chrome(wf_header, keep))
        _, _, wf_nav = block(wf, '<nav class="bottom-nav"', "</nav>")
        out = swap(out, '<nav class="bottom-nav"', "</nav>", neutralize_chrome(wf_nav, keep))

    out = graft_css(out, wf)

    out = re.sub(r"<title>.*?</title>",
                 f"<title>UI Visual - {title}</title>", out, count=1, flags=re.S)
    out = out.replace("Color copy of wireframes/event-feed.html",
                      f"Color copy of wireframes/{wf_name}", 1)

    (UIV / dest).write_text(out)
    return dest


OUTCOME_JS = ("<script>(function(){var d=document.getElementById('outcomeDialog');"
              "if(d){if(d.showModal){try{d.showModal();}catch(e){d.setAttribute('open','');}}"
              "else{d.setAttribute('open','');}}})();</script>")


def strip_grey(frag):
    """Drop the grey-box inline colours the wireframe hard-codes (color:#222 etc.),
    so _theme.css owns the text colour. Layout inline styles are left intact."""
    frag = re.sub(r'color:\s*#[0-9a-fA-F]{3,6}\s*;?', "", frag)
    frag = re.sub(r'style="\s*;?\s*"', "", frag)
    return frag


def build_overlay(dest, wf_name, variant, title, keep, close_href="active-bets.html"):
    """A wireframe's .backdrop > .sheet overlay (Win / Loss / Sign in / Deposit and
    their states) is re-homed as a modal <dialog class="app-dialog {variant}-dialog">,
    so it inherits the whole themed dialog system; showModal() supplies the real dimmed
    ::backdrop over a clean graphite main. _theme.css adds any per-variant accent.
    close_href = where the sheet-close returns (per family: bets / feed / ...)."""
    wf = (WF / wf_name).read_text()
    _, _, sheet = block(wf, '<section class="sheet"', "</section>")
    h2m = re.search(r"<h2>(.*?)</h2>", sheet, flags=re.S)
    h2 = h2m.group(1) if h2m else "Outcome"
    sb = _balanced_div(sheet, '<div class="sheet-body">')
    body = strip_grey(neutralize(sb[2], keep)) if sb else ""
    label = re.sub(r"<[^>]+>", "", h2)
    close = (f'<a href="{close_href}"><button type="button" class="sheet-close"'
             ' aria-label="Close">x</button></a>')
    # `app-case` on the dialog: showModal renders it in the top layer OUTSIDE the
    # .device that carries app-case, so without this the .app-case-scoped theme rules
    # (reconcile-box brass, spinner-box, ...) never reach the sheet content.
    dialog = (f'<dialog class="app-case app-dialog outcome-dialog {variant}-dialog" id="outcomeDialog" aria-label="{label}">'
              f'<div class="sheet-head"><h2>{h2}</h2>{close}</div>' + body + "</dialog>")

    minimal = '<main class="feed">\n      <div class="feed-inner"></div>\n    </main>'
    out = swap(SHELL, '<main class="feed">', "</main>", minimal)
    out = graft_css(out, wf)
    out = out.replace("</body>", dialog + "\n  " + OUTCOME_JS + "</body>", 1)
    out = re.sub(r"<title>.*?</title>",
                 f"<title>UI Visual - {title}</title>", out, count=1, flags=re.S)
    out = out.replace("Color copy of wireframes/event-feed.html",
                      f"Color copy of wireframes/{wf_name}", 1)
    (UIV / dest).write_text(out)
    return dest


def run(names):
    for fam in names:
        cfg = FAMILIES[fam]
        keep = cfg.get("keep", ())
        kind = cfg.get("kind", "main")
        close_href = cfg.get("close", "active-bets.html")
        for page in cfg["pages"]:
            if kind == "overlay":
                dest, wf_name, variant, title = page
                print("built", build_overlay(dest, wf_name, variant, title, keep, close_href))
            else:
                dest, wf_name, lo, title = page
                print("built", build(dest, wf_name, lo, title, keep))


if __name__ == "__main__":
    run(sys.argv[1:] or list(FAMILIES))
