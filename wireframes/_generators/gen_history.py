import _shell as S

FILES = {"success": "active-bets-history.html", "empty": "active-bets-history-empty.html",
         "error": "active-bets-history-error.html", "loading": "active-bets-history-loading.html"}
LABELS = [("success", "Success"), ("empty", "Empty"), ("error", "Error"), ("loading", "Loading")]


def switcher(state):
    cells = []
    for key, lbl in LABELS:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{FILES[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


def resolved(q, outcome, href, stake, payout, side, result, meta):
    return (f'          <a href="{href}" style="text-decoration:none;color:inherit;display:block;">\n'
            f'            <article class="pos">\n'
            f'              <div class="pos-top">\n'
            f'                <span class="pos-q">{q}</span>\n'
            f'                <span class="pos-side">{outcome}</span>\n'
            f'              </div>\n'
            f'              <div class="pos-figures">\n'
            f'                <span class="pos-fig">Stake<b>{stake}</b></span>\n'
            f'                <span class="pos-fig">Payout<b>{payout}</b></span>\n'
            f'                <span class="pos-fig">Your side<b>{side}</b></span>\n'
            f'                <span class="pos-fig">Result<b>{result}</b></span>\n'
            f'              </div>\n'
            f'              <span class="pos-status">{meta}</span>\n'
            f'            </article>\n'
            f'          </a>\n')


HISTORY_LIST = (
    resolved("Will the US government shut down before March 1, 2027?", "WON", "win.html",
             "$5.00", "+$13.20", "YES", "YES", "Resolved Jun 27 &middot; tap to see your win")
    + resolved("Will Bitcoin close above $150,000 before October 1, 2026?", "WON", "win.html",
               "$25.00", "+$31.80", "YES", "YES", "Resolved Jun 20 &middot; tap to see your win")
    + resolved("Spot ETH ETF approved in H1 2027?", "LOST", "loss.html",
               "$5.00", "-$5.00", "NO", "YES", "Resolved Jun 12 &middot; tap to see what happened")
    + resolved("Which party will win the most seats in the next UK election?", "WON", "win.html",
               "$10.00", "+$21.10", "NO &middot; Conservatives", "Conservatives", "Resolved Jun 2 &middot; tap to see your win")
)


def main_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: My Bets (History tab: resolved bets - won / lost, payout, outcome; taps route to Win / Loss)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + S.tabs("history")
            + '        <div class="pos-list">\n'
            + HISTORY_LIST
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


def main_block(zone, icon, title, msg, actions):
    return (f'    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            f'      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + S.tabs("history")
            + f'        <div class="state-block">\n'
            f'          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>\n'
            f'          <h2 class="state-title">{title}</h2>\n'
            f'          <p class="state-msg">{msg}</p>\n'
            f'          <div class="state-actions">{actions}</div>\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </main>\n')


ICON_INBOX = '<path d="M3 13l3-8h12l3 8M3 13v6h18v-6M3 13h5l2 3h4l2-3h5"/>'
ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'


def main_empty():
    return main_block(
        "zone: My Bets (History tab empty: no resolved bets yet, CTA to Event Feed)",
        ICON_INBOX, "No resolved bets yet",
        "Your settled bets will appear here once the events you bet on resolve. None of yours have resolved yet.",
        '<a href="event-feed.html"><button type="button" class="state-btn primary">Find events</button></a>')


def main_error():
    return main_block(
        "zone: My Bets (History tab error: failed to load resolved bets, retry)",
        ICON_WARN, "Couldn't load your history",
        "Something went wrong while loading your resolved bets. Check your connection and try again.",
        '<a href="active-bets-history.html"><button type="button" class="state-btn primary">Try again</button></a>')


def main_loading():
    rows = ""
    for w in ("w70", "w40", "w70"):
        rows += ('          <article class="pos skeleton" aria-hidden="true">\n'
                 f'            <div class="sk-line {w}"></div>\n'
                 '            <div class="sk-line w40"></div>\n'
                 '          </article>\n')
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: My Bets (History tab loading: fetching resolved bets)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>My Bets</h2></div>\n'
            + S.tabs("history")
            + '        <div class="pos-list" aria-busy="true">\n'
            + rows
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>History tab inside My Bets</strong> -&gt; G5 resolved: Bet History is the History tab on the Active Bets screen, not a standalone screen. Active = open positions; History = resolved bets.</li>
        <li><strong>Private resolved bets: won / lost, payout, outcome</strong> -&gt; the user's own settlement record. The public track record lives on My Profile / Public Profile, not here (this is private).</li>
        <li><strong>Tap a resolved item -&gt; Win / Loss Screen</strong> -&gt; the SJ1 win-share entry (tap a won item -&gt; Win Screen) and the FJ5 / EJ3 conscious-loss entry (tap a lost item -&gt; Loss Screen) both start here.</li>
        <li><strong>empty -&gt; Event Feed</strong> -&gt; no resolved bets yet routes to the feed to find events (not a dead end).</li>
        <li><strong>Account-bound (logged-in only)</strong> -&gt; settled positions require an account, so no logged-out variant. No auth axis.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (My Bets)</span>
<pre>My Bets (account-bound):

Active Bets  ---- tab ---- [Bet History]   &lt;- current
(open positions)           (resolved bets)
                                |
                                +-- tap won  --&gt; Win Screen  (SJ1)
                                '-- tap lost --&gt; Loss Screen (FJ5 + EJ3)</pre>
        <p class="ref">Flow position: the History tab of My Bets (IA/sitemap.md Bet History,
          G5). Serves SJ1 (win-share entry) and FJ5 / EJ3 (loss entry).</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (resolved list -&gt; Win / Loss), empty (no resolved bets yet
          -&gt; feed), error (load failed, retry), loading (fetching). Account-bound, no auth axis.</p>
      </section>
    </div>
"""

AUTHSTATE = {"success": "success (resolved bets)", "empty": "empty (no resolved bets yet)",
             "error": "error (load failed)", "loading": "loading (fetching resolved)"}


def build(state):
    cur_file = FILES[state]
    main = {"success": main_success, "empty": main_empty, "error": main_error, "loading": main_loading}[state]()
    device = S.HEADER_IN_OPEN + main + S.bottom_in("mybets") + "    " + S.FOOTER + "\n"
    authstate = "logged in - state: " + AUTHSTATE[state]
    title = f"Wireframe - Bet History ({authstate})"
    html = S.assemble(title, cur_file, "Bet History (History tab)", authstate, switcher(state), device, SIDE)
    return S.write(cur_file, html)


print("\n".join(build(s) for s in ("success", "empty", "error", "loading")))
