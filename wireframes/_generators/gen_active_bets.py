import _shell as S

FILES = {"success": "active-bets.html", "empty-new": "active-bets-empty-new.html",
         "empty-resolved": "active-bets-empty-resolved.html", "error": "active-bets-error.html",
         "loading": "active-bets-loading.html"}
LABELS = [("success", "Success"), ("empty-new", "Empty (new)"), ("empty-resolved", "Empty (resolved)"),
          ("error", "Error"), ("loading", "Loading")]


def switcher(state):
    cells = []
    for key, lbl in LABELS:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{FILES[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


def tabs():
    return S.tabs("active")


POS_SUCCESS = """        <div class="pos-list">

          <article class="pos">
            <div class="pos-top">
              <span class="pos-q">Will the US government shut down before March 1, 2027?</span>
              <span class="pos-side">YES</span>
            </div>
            <div class="pos-figures">
              <span class="pos-fig">Stake<b>$5.00</b></span>
              <span class="pos-fig">Current value<b>$5.40</b></span>
              <span class="pos-fig">Potential payout<b>$13.20</b></span>
              <span class="pos-fig">Avg price<b>38%</b></span>
            </div>
            <span class="pos-status">Open &middot; just placed</span>
          </article>

          <article class="pos">
            <div class="pos-top">
              <span class="pos-q">Will Bitcoin close above $150,000 before October 1, 2026?</span>
              <span class="pos-side">YES</span>
            </div>
            <div class="pos-figures">
              <span class="pos-fig">Stake<b>$25.00</b></span>
              <span class="pos-fig">Current value<b>$31.80</b></span>
              <span class="pos-fig">Potential payout<b>$41.00</b></span>
              <span class="pos-fig">Avg price<b>61%</b></span>
            </div>
            <span class="pos-status">Open</span>
          </article>

          <article class="pos">
            <div class="pos-top">
              <span class="pos-q">Which party will win the most seats in the next UK general election?</span>
              <span class="pos-side">NO &middot; Conservatives</span>
            </div>
            <div class="pos-figures">
              <span class="pos-fig">Stake<b>$10.00</b></span>
              <span class="pos-fig">Current value<b>$8.10</b></span>
              <span class="pos-fig">Potential payout<b>$22.50</b></span>
              <span class="pos-fig">Avg price<b>33%</b></span>
            </div>
            <span class="pos-status">Open</span>
          </article>

        </div>
"""


def main_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: My Bets (Active tab: open positions; the just-placed bet appears here, MJ terminal T14)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + tabs()
            + POS_SUCCESS
            + '      </div>\n'
            + '    </main>\n')


def main_block(zone, icon, title, msg, actions):
    return (f'    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            f'      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + tabs()
            + f'        <div class="state-block">\n'
            f'          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>\n'
            f'          <h2 class="state-title">{title}</h2>\n'
            f'          <p class="state-msg">{msg}</p>\n'
            f'          <div class="state-actions">{actions}</div>\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </main>\n')


ICON_INBOX = '<path d="M3 13l3-8h12l3 8M3 13v6h18v-6M3 13h5l2 3h4l2-3h5"/>'
ICON_CHECK = '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>'
ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'


def main_empty_new():
    return main_block(
        "zone: My Bets (empty-new: no bets placed yet, CTA to Event Feed to find events)",
        ICON_INBOX, "No active bets yet",
        "You haven't placed any bets. Find an event you have an opinion on and put a real stake on the outcome.",
        '<a href="event-feed.html"><button type="button" class="state-btn primary">Find events</button></a>')


def main_empty_resolved():
    return main_block(
        "zone: My Bets (empty-resolved: all positions closed, CTA to History tab)",
        ICON_CHECK, "All your positions are closed",
        "You have no open bets right now. Your settled bets are in the History tab.",
        '<a href="active-bets-history.html"><button type="button" class="state-btn primary">See resolved bets (History tab)</button></a>'
        '<a href="event-feed.html"><button type="button" class="state-btn">Find new events</button></a>')


def main_error():
    return main_block(
        "zone: My Bets (error: failed to load positions, retry)",
        ICON_WARN, "Couldn't load your positions",
        "Something went wrong while loading your bets. Check your connection and try again.",
        '<a href="active-bets.html"><button type="button" class="state-btn primary">Try again</button></a>')


def main_loading():
    rows = ""
    for w in ("w70", "w40", "w70"):
        rows += (f'          <article class="pos skeleton" aria-hidden="true">\n'
                 f'            <div class="sk-line {w}"></div>\n'
                 f'            <div class="sk-line w40"></div>\n'
                 f'          </article>\n')
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: My Bets (loading: fetching positions)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + tabs()
            + '        <div class="pos-list" aria-busy="true">\n'
            + rows
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Open positions list</strong> -&gt; EJ1: monitoring the position move my way. Each row shows stake, current value and potential payout so the user tracks the event they have skin in.</li>
        <li><strong>Just-placed bet at the top</strong> -&gt; MJ success terminal (IA/flows.md T14): the bet placed at the end of the main flow lands here, marked "just placed".</li>
        <li><strong>Active / History tabs</strong> -&gt; Active = open positions; History = resolved bets (the FJ5 / EJ3 conscious-loss and SJ1 win-share entry points reach the Loss / Win screens from History).</li>
        <li><strong>empty-new vs empty-resolved</strong> -&gt; a brand-new account routes to the feed to find events; an account that has cleared all positions routes to History. Two different non-dead exits.</li>
        <li><strong>Account-bound (logged-in only)</strong> -&gt; positions require an account, so there is no logged-out variant of this screen (the auth axis does not apply here).</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (main-flow spine)</span>
<pre>Main-flow spine (MJ, News Junkie):

Event Feed
   v
Event Detail
   v
Bet Screen
   v
Sign In / Register
   v
Deposit
   v
[Active Bets]    &lt;- current screen (MJ success, T14)</pre>
        <p class="ref">Flow position: MJ success terminal (IA/flows.md, techOk -&gt; Active Bets -&gt;
          T14). Serves EJ1, MJ, and the FJ5 / EJ3 resolved-bet entry.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (open positions), empty-new (no bets yet -&gt; feed),
          empty-resolved (all closed -&gt; History), error (load failed, retry),
          loading (fetching positions). No auth axis: account-bound screen.</p>
      </section>
    </div>
"""


def build(state):
    cur_file = FILES[state]
    main = {"success": main_success, "empty-new": main_empty_new, "empty-resolved": main_empty_resolved,
            "error": main_error, "loading": main_loading}[state]()
    device = S.HEADER_IN_OPEN + main + S.bottom_in("mybets") + "    " + S.FOOTER + "\n"
    authstate = "logged in - state: " + {
        "success": "success (open positions)", "empty-new": "empty-new (no bets yet)",
        "empty-resolved": "empty-resolved (all closed)", "error": "error (load failed)",
        "loading": "loading (fetching positions)"}[state]
    title = f"Wireframe - Active Bets ({authstate})"
    html = S.assemble(title, cur_file, "Active Bets", authstate, switcher(state), device, SIDE)
    return S.write(cur_file, html)


print("\n".join(build(s) for s in ("success", "empty-new", "empty-resolved", "error", "loading")))
