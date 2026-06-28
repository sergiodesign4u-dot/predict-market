"""Idempotent post-processor: empty-state notifications dropdown (narrowed).

On the new-account empty pages the header bell dropdown is itself empty (no badge,
"No notifications yet") and its "See all" link points at notifications-empty.html,
so the empty flow stays consistent. Scope is deliberately narrow: only pages where
an empty account genuinely implies zero notifications.

KEEP = the empty notifications page itself + the brand-new-user empties (no bets,
no favorites). Every other '-empty' page keeps the populated preview; this script
reverts them if a previous broader run had emptied them.

Run after chrome2.py. Idempotent.
"""
import re
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

KEEP = {"notifications-empty.html", "active-bets-empty-new.html", "favorites-empty.html"}

# the populated dropdown, taken verbatim from a non-empty page (exact match target)
POP = re.search(r'<details class="notif-menu">.*?</details>',
                (ROOT / "event-feed.html").read_text(), re.S).group(0)

EMPTY = """<details class="notif-menu">
            <summary aria-label="Notifications, none">
              <span class="bell-wrap">
                <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
              </span>
            </summary>
            <div class="dropdown notif-drop" role="menu">
              <span class="zone-tag">latest notifications (empty)</span>
              <p class="notif-empty">No notifications yet. We will let you know when an event you follow moves or resolves.</p>
              <a class="notif-all" href="notifications-empty.html">See all notifications</a>
            </div>
          </details>"""

CSS_RULE = "    .notif-empty { margin: 0; padding: 14px 10px; text-align: center; font-size: 11px; color: #555; }\n"

emptied, reverted = [], []
for p in sorted(ROOT.glob("*-empty*.html")):
    t = p.read_text()
    o = t
    if p.name in KEEP:
        if POP in t:
            t = t.replace(POP, EMPTY, 1)
        if ".notif-empty {" not in t and "notif-empty" in t:
            t = t.replace("\n  </style>", "\n" + CSS_RULE + "  </style>", 1)
        if t != o:
            emptied.append(p.name)
    else:
        if EMPTY in t:                       # revert a previous broad run
            t = t.replace(EMPTY, POP, 1)
            reverted.append(p.name)
    if t != o:
        if "—" in t:
            raise SystemExit("EM-DASH in " + p.name)
        p.write_text(t)

print("empty dropdown on:", sorted(KEEP))
print("emptied this run:", emptied)
print("reverted to populated:", reverted)
