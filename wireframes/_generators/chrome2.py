"""Idempotent post-processor: header notifications dropdown + in-context deposit
"+" + logged-out redirect after sign-in.

1. Header bell (logged-in) becomes a native <details> dropdown (no chevron): a
   mini-list of recent notifications + a "See all" link to notifications.html, so
   clicking it does NOT navigate away from the current page.
2. A "+" button next to the desktop balance opens the deposit dialog directly
   (data-open="deposit"), so a user can top up in context.
3. On logged-out pages, completing sign-in then closing / funding the deposit
   dialog redirects to the logged-in counterpart (body[data-loggedin-target]);
   closing the sign-in dialog before signing in still keeps you put.

Run after the generators + fixpack.py. Idempotent.
"""
import re
import pathlib
import _shell as S

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

# ---- new CSS (mirrors .avatar-menu; injected before </style>) ----
NEW_CSS = """
    /* notifications dropdown (header bell -> mini-list, no chevron) */
    .notif-menu { position: relative; }
    .notif-menu summary { list-style: none; cursor: pointer; display: inline-flex; align-items: center; }
    .notif-menu summary::-webkit-details-marker { display: none; }
    .notif-menu .dropdown { position: absolute; right: 0; top: calc(100% + 4px); width: 260px; max-width: 80vw; border: 1px solid #888; background: #e6e6e6; z-index: 10; }
    .notif-menu .dropdown .zone-tag { background: #cdcdcd; }
    .notif-drop ul { list-style: none; margin: 0; padding: 0; }
    .notif-drop li { border-top: 1px solid #ccc; }
    .notif-drop li:first-child { border-top: none; }
    .notif-drop li a { display: block; padding: 8px 10px; text-decoration: none; color: #222; }
    .notif-drop li a strong { display: block; font-size: 12px; }
    .notif-drop li a span { display: block; font-size: 10px; color: #555; }
    .notif-all { display: block; text-align: center; padding: 8px; border-top: 1px solid #999; font-size: 11px; text-decoration: none; color: #222; background: #dcdcdc; }
    .bal-add { padding: 3px; }
"""

# ---- bell-wrap (already wired by fixpack to a link) -> notifications dropdown ----
BELL_WRAP_RE = re.compile(r'<span class="bell-wrap">.*?</span>\s*</span>', re.S)
NOTIF_DETAILS = """<details class="notif-menu">
            <summary aria-label="Notifications, 3 unread">
              <span class="bell-wrap">
                <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
                <span class="badge-dot">3</span>
              </span>
            </summary>
            <div class="dropdown notif-drop" role="menu">
              <span class="zone-tag">latest notifications (tap a row, or see all)</span>
              <ul>
                <li><a href="win.html"><strong>Position resolved</strong><span>US government shutdown before Mar 1 - YES won</span></a></li>
                <li><a href="event-detail.html"><strong>Odds moved</strong><span>Bitcoin above $150k - now 61%</span></a></li>
                <li><a href="event-detail.html"><strong>Deadline approaching</strong><span>Eurovision 2027 final closes in 24h</span></a></li>
              </ul>
              <a class="notif-all" href="notifications.html">See all notifications</a>
            </div>
          </details>"""

# ---- "+" deposit button inserted after the balance swap button ----
SWAP_BLOCK = """            <button type="button" class="icon-btn bal-swap" id="balSwap" aria-label="Swap balance (showing Portfolio)">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h12l-3-3M17 17H5l3 3"/></svg>
            </button>"""
ADD_BTN = """
            <button type="button" class="icon-btn bal-add" data-open="deposit" aria-label="Add funds">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>"""

# ---- new dialog JS with the logged-out redirect ----
NEW_DIALOG_JS = """  <script>
    // Shared dialogs: open over the current page. On logged-out pages, completing
    // sign-in then closing / funding the deposit lands on the logged-in counterpart
    // (body[data-loggedin-target]); closing sign-in before signing in stays put.
    (function () {
      function dlg(id) { return document.getElementById(id); }
      function open(id) { var d = dlg(id); if (!d) return; if (d.showModal) d.showModal(); else d.setAttribute('open', ''); }
      function close(d) { if (!d) return; if (d.close) d.close(); else d.removeAttribute('open'); }
      var target = document.body.getAttribute('data-loggedin-target');
      var signedIn = false;
      document.addEventListener('click', function (e) {
        var o = e.target.closest('[data-open]');
        if (o) { e.preventDefault(); open(o.getAttribute('data-open') === 'deposit' ? 'depositDialog' : 'signinDialog'); return; }
        var f = e.target.closest('[data-flow="signin-to-deposit"]');
        if (f) { e.preventDefault(); signedIn = true; close(dlg('signinDialog')); open('depositDialog'); return; }
        var c = e.target.closest('[data-close-dialog]');
        if (c) { close(c.closest('dialog')); return; }
      });
      ['signinDialog', 'depositDialog'].forEach(function (id) {
        var d = dlg(id); if (!d) return;
        d.addEventListener('click', function (e) { if (e.target === d) close(d); });
      });
      var dep = dlg('depositDialog');
      if (dep) dep.addEventListener('close', function () { if (target && signedIn) window.location.href = target; });
    })();
  </script>"""


def loggedin_target(name, files):
    if "-logged-out" in name:
        tgt = name.replace("-logged-out", "")
        return tgt if tgt in files else None
    return None  # how-it-works / public-profile handled below


files = {p.name for p in ROOT.glob("*.html")}
stats = {"css": 0, "bell": 0, "add": 0, "js": 0, "target": 0}

for p in sorted(ROOT.glob("*.html")):
    t = p.read_text()
    orig = t

    # 1. CSS (only where the logged-in header / dropdown can appear; harmless elsewhere,
    #    but we gate on bell presence to keep diffs tight)
    has_bell = '<span class="bell-wrap">' in t or '<details class="notif-menu">' in t
    if has_bell and '.notif-menu {' not in t:
        t = t.replace("\n  </style>", NEW_CSS + "  </style>", 1)
        stats["css"] += 1

    # 2. bell-wrap link -> dropdown
    if '<details class="notif-menu">' not in t and BELL_WRAP_RE.search(t):
        t = BELL_WRAP_RE.sub(NOTIF_DETAILS, t, count=1)
        stats["bell"] += 1

    # 3. "+" deposit button
    if 'class="icon-btn bal-add"' not in t and SWAP_BLOCK in t:
        t = t.replace(SWAP_BLOCK, SWAP_BLOCK + ADD_BTN, 1)
        stats["add"] += 1

    # 4. dialog JS
    if S.DIALOG_JS in t:
        t = t.replace(S.DIALOG_JS, NEW_DIALOG_JS, 1)
        stats["js"] += 1

    # 5. logged-out redirect target on <body>
    if 'data-loggedin-target=' not in t:
        tgt = loggedin_target(p.name, files)
        if tgt is None and '>Log in</button>' in t and 'data-open="signin"' in t:
            tgt = "event-feed.html"        # how-it-works / public-profile -> home
        if tgt:
            t = t.replace("<body>", f'<body data-loggedin-target="{tgt}">', 1)
            stats["target"] += 1

    if t != orig:
        if "—" in t:
            raise SystemExit("EM-DASH in " + p.name)
        p.write_text(t)

print(stats)
