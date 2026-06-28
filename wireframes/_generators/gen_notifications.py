import _shell as S

FILES = {"success": "notifications.html", "empty": "notifications-empty.html",
         "error": "notifications-error.html", "loading": "notifications-loading.html",
         "push": "notifications-push.html"}
LABELS = [("success", "Success"), ("empty", "Empty"), ("error", "Error"),
          ("loading", "Loading"), ("push", "Push denied")]


def switcher(state):
    cells = []
    for key, lbl in LABELS:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{FILES[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


# One alert row -> links to its target screen (tap navigates: Event Detail / Active Bets / Win / Loss).
def item(text, type_label, time, href, unread):
    dot = '<span aria-label="unread">[unread] </span>' if unread else ""
    return (f'          <a href="{href}" style="text-decoration:none;color:inherit;display:block;">\n'
            f'            <article class="pos">\n'
            f'              <div class="pos-top">\n'
            f'                <span class="pos-q">{text}</span>\n'
            f'                <span class="pos-status" style="white-space:nowrap;">{time}</span>\n'
            f'              </div>\n'
            f'              <span class="pos-status">{dot}{type_label}</span>\n'
            f'            </article>\n'
            f'          </a>\n')


def divider(label):
    return f'          <p class="pos-status" style="margin:10px 0 2px;text-transform:uppercase;letter-spacing:.04em;">{label}</p>\n'


# Alert types per IA/sitemap.md entity 8 / Notifications screen:
# position resolved (-> Win/Loss), odds moved (-> Event Detail), deadline approaching
# (-> Event Detail), new event in followed category (-> Event Detail / feed).
NOTIF_LIST = (
    divider("Unread")
    + item("Your bet resolved: US government shutdown - YES won. Tap to see your win.",
           "Position resolved", "2m", "win.html", True)
    + item("Odds moved: \"Bitcoin above $150,000\" jumped from 58% to 64%.",
           "Odds moved significantly", "18m", "event-detail.html", True)
    + item("Closing soon: \"Which party wins the most UK seats\" closes in 6 hours.",
           "Event deadline approaching", "1h", "event-detail-multi.html", True)
    + divider("Earlier")
    + item("New in Crypto: \"Will ETH flip BTC by 2027?\" is now live.",
           "New event in a followed category", "Yesterday", "crypto.html", False)
    + item("Your bet resolved: ETF approval - NO. Tap to see what happened.",
           "Position resolved", "2d", "loss.html", False)
)


def main_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Notifications (list of unread + recent alerts; tap routes to target screen)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Notifications</h2></div>\n'
            '        <div class="pos-list">\n'
            + NOTIF_LIST
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


def main_push():
    banner = ("""        <div class="push-banner" role="region" aria-label="Notifications permission">
          <span class="push-msg">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
            Push is off. Enable notifications to get live updates on the events you follow.
          </span>
          <span class="push-actions">
            <button type="button" class="state-btn primary">Open system settings</button>
            <button type="button" class="state-btn">Not now</button>
          </span>
        </div>
""")
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Notifications (push-permission-missing: OS push denied; in-app banner + settings deep-link, list still shown)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Notifications</h2></div>\n'
            + banner
            + '        <p class="fine">In-app notifications still work here. Enable system push so alerts reach you when the app is closed.</p>\n'
            + '        <div class="pos-list">\n'
            + NOTIF_LIST
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


def main_block(zone, icon, title, msg, actions):
    return (f'    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            f'      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>Notifications</h2></div>\n'
            f'        <div class="state-block">\n'
            f'          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>\n'
            f'          <h2 class="state-title">{title}</h2>\n'
            f'          <p class="state-msg">{msg}</p>\n'
            f'          <div class="state-actions">{actions}</div>\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </main>\n')


ICON_BELL = '<path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/>'
ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'


def main_empty():
    return main_block(
        "zone: Notifications (empty: no notifications yet - new user or no events followed)",
        ICON_BELL, "No notifications yet",
        "When an event you follow moves, approaches its deadline, or resolves, you'll see it here. Follow an event to start getting alerts.",
        '<a href="event-feed.html"><button type="button" class="state-btn primary">Find events to follow</button></a>')


def main_error():
    return main_block(
        "zone: Notifications (error: failed to load - retry)",
        ICON_WARN, "Couldn't load notifications",
        "Something went wrong while loading your alerts. Check your connection and try again.",
        '<a href="notifications.html"><button type="button" class="state-btn primary">Try again</button></a>')


def main_loading():
    rows = ""
    for w in ("w70", "w40", "w70", "w40"):
        rows += ('          <article class="pos skeleton" aria-hidden="true">\n'
                 f'            <div class="sk-line {w}"></div>\n'
                 '            <div class="sk-line w40"></div>\n'
                 '          </article>\n')
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Notifications (loading: fetching the alert list)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Notifications</h2></div>\n'
            '        <div class="pos-list" aria-busy="true">\n'
            + rows
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>In-app alert list</strong> -&gt; the return trigger discovered in tracing (IA/sitemap.md): FJ1, FJ5 and EJ3 all depend on delivery via notification. Without this screen, a missed OS alert is unrecoverable; here it has in-app history.</li>
        <li><strong>Four alert types</strong> -&gt; position resolved (routes to Win / Loss), odds moved significantly, event deadline approaching, new event in a followed category. They map to the hot / warm return signals in aarrr.md (D1-D3).</li>
        <li><strong>Tap routes to the target screen</strong> -&gt; each item navigates to where the action is: Event Detail (odds / deadline / new event) or the resolution screen (Win / Loss). A resolved-position tap is the 1-tap G1 path to Win / Loss.</li>
        <li><strong>Reached from the header bell (both breakpoints)</strong> -&gt; Notifications is a header bell with a permanent unread badge, not a bottom-nav slot (the wireframe pass swapped it with Favorites). The badge stays visible as the retention anchor.</li>
        <li><strong>push-permission-missing</strong> -&gt; if OS push is denied, an in-app banner offers a system-settings deep-link; in-app alerts still show. Same banner surfaces on the Event Feed.</li>
        <li><strong>Account-bound (logged-in only)</strong> -&gt; alerts need an account; logged-out, the bell routes to Sign In and shows no badge. No auth axis on this screen.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (return trigger)</span>
<pre>Return trigger (FJ1 / FJ5 / EJ3):

[Notifications]   &lt;- current (header bell, both breakpoints)
   |
   +-- position resolved --&gt; Win / Loss Screen
   +-- odds moved        --&gt; Event Detail
   +-- deadline approaching --&gt; Event Detail
   '-- new in category   --&gt; Event Detail / category</pre>
        <p class="ref">Flow position: the return-trigger source (IA/sitemap.md Notifications;
          IA/flows.md FJ5 / SJ1 triggerNotif). Serves FJ1, FJ5, EJ3; aarrr.md D1-D3.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (unread + earlier list), empty (no alerts yet -&gt; follow events),
          error (load failed, retry), loading (fetching), push-permission-missing (OS push
          denied, in-app banner + settings deep-link). Account-bound, no auth axis.</p>
      </section>
    </div>
"""


def build(state):
    cur_file = FILES[state]
    main = {"success": main_success, "empty": main_empty, "error": main_error,
            "loading": main_loading, "push": main_push}[state]()
    # Header bell is the entry; no bottom-nav slot is current on this screen.
    device = S.HEADER_IN_OPEN + main + S.bottom_in("none") + "    " + S.FOOTER + "\n"
    authstate = "logged in - state: " + {
        "success": "success (alert list)", "empty": "empty (no alerts yet)",
        "error": "error (load failed)", "loading": "loading (fetching list)",
        "push": "push-permission-missing (OS push denied)"}[state]
    title = f"Wireframe - Notifications ({authstate})"
    html = S.assemble(title, cur_file, "Notifications", authstate, switcher(state), device, SIDE)
    return S.write(cur_file, html)


print("\n".join(build(s) for s in ("success", "empty", "error", "loading", "push")))
