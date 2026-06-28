"""Idempotent post-processor: empty-state notifications dropdown.

On logged-in EMPTY-state pages the header bell dropdown should itself be empty
(no badge, "no notifications yet") and its "See all" link should point at the
empty notifications page - so the empty flow is internally consistent instead of
previewing 3 fake notifications that lead to the populated page.

Targets every page with '-empty' in its name that carries the populated dropdown
(so logged-out empties, which have no dropdown, are skipped automatically).

Run after chrome2.py. Idempotent.
"""
import re
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

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

changed = []
for p in sorted(ROOT.glob("*-empty*.html")):
    t = p.read_text()
    if POP not in t:
        continue                       # not a logged-in dropdown page (e.g. logged-out empty)
    o = t
    t = t.replace(POP, EMPTY, 1)
    if ".notif-empty {" not in t:
        t = t.replace("\n  </style>", "\n" + CSS_RULE + "  </style>", 1)
    if t != o:
        if "—" in t:
            raise SystemExit("EM-DASH in " + p.name)
        p.write_text(t)
        changed.append(p.name)

print("empty dropdown applied to", len(changed), "pages:")
print("\n".join(changed))
