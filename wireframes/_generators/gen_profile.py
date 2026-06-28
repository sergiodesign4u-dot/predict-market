import _shell as S

# Page-local CSS (scoped to the profile pages; not added to the shared shell).
PROFILE_CSS = """  <style>
    .idrow { display: flex; align-items: center; gap: 12px; padding: 4px 0 10px; }
    .idrow .av { width: 56px; height: 56px; flex: 0 0 56px; border: 1px solid #999; background: #d2d2d2;
      display: flex; align-items: center; justify-content: center; font-size: 8px; text-align: center; }
    .idrow .who { flex: 1; min-width: 0; }
    .idrow .name { font-size: 16px; font-weight: bold; }
    .idrow .handle { font-size: 11px; color: #555; }
    .idrow .edit { border: 1px solid #888; background: #d6d6d6; padding: 6px 10px; font-size: 11px; cursor: pointer; }
    .gallery { display: flex; gap: 8px; flex-wrap: wrap; }
    .gallery .card { flex: 0 0 auto; width: 120px; height: 74px; border: 1px dashed #999; background: #ededed;
      display: flex; align-items: center; justify-content: center; text-align: center; font-size: 9px; color: #555; padding: 4px; }
  </style>
"""


def section_label(text):
    return f'        <p class="pos-status" style="margin:12px 0 4px;text-transform:uppercase;letter-spacing:.04em;">{text}</p>\n'


def stats():
    return ('        <article class="pos" aria-label="Track record">\n'
            '          <div class="pos-figures" style="font-size:11px;">\n'
            '            <span class="pos-fig">Total bets<b>23</b></span>\n'
            '            <span class="pos-fig">Win rate<b>61%</b></span>\n'
            '            <span class="pos-fig">Resolved<b>18</b></span>\n'
            '            <span class="pos-fig">Member since<b>2026</b></span>\n'
            '          </div>\n'
            '          <span class="pos-status">Win rate is % correct on resolved bets (public). Reputation = the track record, not the balance.</span>\n'
            '        </article>\n')


def gallery():
    cards = (
        '          <div class="card">Win card: US shutdown YES +$13.20</div>\n'
        '          <div class="card">Win card: BTC &gt; $150k YES +$6.80</div>\n'
        '          <div class="card">Win card: ETF approval NO +$9.40</div>\n')
    return ('        <div class="gallery">\n' + cards + '        </div>\n')


def resolved_row(q, side, outcome, meta):
    return (f'          <article class="pos">\n'
            f'            <div class="pos-top">\n'
            f'              <span class="pos-q">{q}</span>\n'
            f'              <span class="pos-side">{outcome}</span>\n'
            f'            </div>\n'
            f'            <span class="pos-status">{side} &middot; {meta}</span>\n'
            f'          </article>\n')


def resolved_history():
    rows = (
        resolved_row("US government shutdown before Mar 1, 2027", "YES", "WON", "resolved Jun 27 &middot; +$13.20")
        + resolved_row("Bitcoin above $150,000 before Oct 1, 2026", "YES", "WON", "resolved Jun 20 &middot; +$6.80")
        + resolved_row("Spot ETH ETF approved in H1 2027", "NO", "LOST", "resolved Jun 12 &middot; -$5.00")
        + resolved_row("Which party wins the most UK seats", "NO &middot; Conservatives", "WON", "resolved Jun 2 &middot; +$11.10"))
    return ('        <div class="pos-list">\n' + rows + '        </div>\n')


# ---- Portfolio summary (My Profile only: the account hub surfaces money on top) ----
PORTFOLIO_SUMMARY = """        <article class="pos" aria-label="Portfolio summary">
          <div class="pos-figures" style="font-size:11px;">
            <span class="pos-fig">Portfolio total<b>$142.00</b></span>
            <span class="pos-fig">Cash (available)<b>$92.00</b></span>
            <span class="pos-fig">In-play<b>$50.00</b></span>
          </div>
          <div class="cta-bar" style="position:static;padding:8px 0 0;border:none;background:none;">
            <button type="button" data-open="deposit">Deposit</button>
            <a href="wallet.html" style="flex:1;"><button type="button" style="width:100%;">Open Wallet</button></a>
          </div>
        </article>
"""


# =========================================================================
# MY PROFILE  (SJ1 + SJ2; the Portfolio account hub on mobile)
# =========================================================================
MY_FILES = {"success": "my-profile.html", "loading": "my-profile-loading.html", "error": "my-profile-error.html"}
MY_LABELS = [("success", "Success"), ("loading", "Loading"), ("error", "Error")]


def my_id():
    return ('        <div class="idrow">\n'
            '          <span class="av">avatar</span>\n'
            '          <span class="who"><span class="name">alex_predicts</span><br><span class="handle">Your public track record</span></span>\n'
            '          <button type="button" class="edit">Edit name &amp; avatar</button>\n'
            '        </div>\n')


def my_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: My Profile (Portfolio account hub: portfolio summary on top, then public track record; SJ1 / SJ2)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>My Profile</h2></div>\n'
            + section_label("Portfolio")
            + PORTFOLIO_SUMMARY
            + my_id()
            + section_label("Track record")
            + stats()
            + section_label("Share cards (past wins)")
            + gallery()
            + section_label("Resolved predictions (public)")
            + resolved_history()
            + '      </div>\n'
            + '    </main>\n')


# =========================================================================
# PUBLIC PROFILE  (SJ2; read-only view of another user)
# =========================================================================
PUB_FILES = {"success": "public-profile.html", "loading": "public-profile-loading.html",
             "error": "public-profile-error.html", "not-found": "public-profile-not-found.html"}
PUB_LABELS = [("success", "Success"), ("loading", "Loading"), ("error", "Error"), ("not-found", "Not found")]


def pub_id():
    return ('        <div class="idrow">\n'
            '          <span class="av">avatar</span>\n'
            '          <span class="who"><span class="name">crypto_dan</span><br><span class="handle">Public track record &middot; read-only</span></span>\n'
            '        </div>\n')


def pub_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Public Profile (another user, read-only; reached via a shared win card or leaderboard; SJ2)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Profile</h2></div>\n'
            + pub_id()
            + '        <p class="fine">You opened this from a shared win card. This is a public, read-only track record - no balance or private data is shown.</p>\n'
            + section_label("Track record")
            + stats()
            + section_label("Share cards (past wins)")
            + gallery()
            + section_label("Resolved predictions (public)")
            + resolved_history()
            + '      </div>\n'
            + '    </main>\n')


# ---- shared state blocks ----
def state_block(heading, zone, icon, title, msg, actions):
    return (f'    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            f'      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>{heading}</h2></div>\n'
            f'        <div class="state-block">\n'
            f'          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>\n'
            f'          <h2 class="state-title">{title}</h2>\n'
            f'          <p class="state-msg">{msg}</p>\n'
            f'          <div class="state-actions">{actions}</div>\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </main>\n')


ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'
ICON_USER = '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>'
ICON_GHOST = '<circle cx="12" cy="12" r="9"/><path d="M8 10h.01M16 10h.01M8 15h8"/>'


def loading_block(heading, zone):
    sk = ('          <article class="pos skeleton" aria-hidden="true">\n'
          '            <div class="sk-line w70"></div>\n'
          '            <div class="sk-line w40"></div>\n'
          '          </article>\n')
    return ('    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            '      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>{heading}</h2></div>\n'
            '        <article class="pos skeleton" aria-hidden="true">\n'
            '          <div class="sk-line w40"></div>\n'
            '          <div class="sk-line w70"></div>\n'
            '        </article>\n'
            '        <div class="pos-list" aria-busy="true">\n'
            + sk * 3
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


# ---- side panels ----
MY_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Track record = reputation</strong> -&gt; SJ2: total bets, win rate and resolved predictions are the public proof of being right. Reputation is the track record, not the balance.</li>
        <li><strong>Share card gallery (past wins)</strong> -&gt; SJ1: the cards generated on the Win Screen collect here, a re-shareable history of called-it moments.</li>
        <li><strong>Portfolio summary on top</strong> -&gt; this screen IS the mobile Portfolio account hub (slot 4): My Profile extended with Portfolio / Cash + Deposit / Wallet above the track record (IA/sitemap.md slot-4 note). Identity and money in one hub, identity first.</li>
        <li><strong>Editable name &amp; avatar</strong> -&gt; the owner can edit display name and avatar (the only write controls; the record itself is not editable).</li>
        <li><strong>Reached from the avatar dropdown (desktop) / Portfolio slot (mobile)</strong> -&gt; account-bound, logged-in only - no auth axis. The Portfolio slot is the current marker.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (identity hub)</span>
<pre>Identity / reputation (SJ1 + SJ2):

avatar dropdown (desktop) ----+
Portfolio slot (mobile) ------+--&gt; [My Profile]   &lt;- current
   |                                  (= account hub: portfolio
   |                                   summary + track record)
   +-- Win Screen --&gt; Share Card --&gt; gallery here</pre>
        <p class="ref">Flow position: identity surface off the betting spine (IA/sitemap.md
          My Profile). Serves SJ1 (share history) and SJ2 (public reputation).</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (track record + gallery + portfolio summary), loading
          (profile fetch), error (retry). empty-state (first-time, no predictions) deferred.
          Account-bound, no auth axis.</p>
      </section>
    </div>
"""

PUB_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Same data, read-only</strong> -&gt; SJ2: another user's public track record. No balance, no private data, no edit controls, no portfolio summary.</li>
        <li><strong>Reached via a shared win card or leaderboard</strong> -&gt; the SJ1 share lands a new or existing user here. In-app discovery of other profiles is deferred post-MVP (G3); the MVP path is the external shared-card link.</li>
        <li><strong>Dan (Crypto Native) uses this more</strong> -&gt; reputation-first behavior; Alex (News Junkie) arrives here secondarily, via a shared card.</li>
        <li><strong>not-found / link-expired</strong> -&gt; a stale or removed profile link routes to a clear dead-end recovery (back to the Event Feed), never a blank page.</li>
        <li><strong>No auth axis</strong> -&gt; a public page about another user; the viewer's own login state does not change what is shown. Not a browse screen, so no logged-in / logged-out variants are built.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (external entry)</span>
<pre>Public reputation (SJ2):

shared win card / leaderboard link
   |
   v
[Public Profile]   &lt;- current (read-only, another user)
   |
   '-- (in-app discovery of profiles: deferred post-MVP, G3)</pre>
        <p class="ref">Flow position: SJ2 public reputation surface, reached via external
          shared-card link at MVP (IA/sitemap.md Public Profile). Read-only.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (read-only track record + gallery), loading (profile fetch),
          error (retry or back to feed), not-found / link-expired (stale link -&gt; Event Feed).
          No auth axis.</p>
      </section>
    </div>
"""


def build_my(state):
    cur_file = MY_FILES[state]
    if state == "success":
        main = my_success()
    elif state == "loading":
        main = loading_block("My Profile", "zone: My Profile (loading: profile data fetching)")
    else:
        main = state_block("My Profile", "zone: My Profile (error: profile failed to load - retry)",
                           ICON_WARN, "Couldn't load your profile",
                           "Something went wrong while loading your track record. Try again.",
                           '<a href="my-profile.html"><button type="button" class="state-btn primary">Try again</button></a>')
    device = S.HEADER_IN_OPEN + main + S.bottom_in("portfolio") + "    " + S.FOOTER + "\n"
    authstate = "logged in - state: " + {"success": "success (track record + portfolio)",
                                         "loading": "loading (profile fetch)", "error": "error (load failed)"}[state]
    title = f"Wireframe - My Profile ({authstate})"
    html = S.assemble(title, cur_file, "My Profile", authstate, switcher(MY_FILES, MY_LABELS, state), device, MY_SIDE)
    html = html.replace("</head>", PROFILE_CSS + "</head>", 1)
    return S.write(cur_file, html)


def build_pub(state):
    cur_file = PUB_FILES[state]
    if state == "success":
        main = pub_success()
    elif state == "loading":
        main = loading_block("Profile", "zone: Public Profile (loading: profile data fetching)")
    elif state == "error":
        main = state_block("Profile", "zone: Public Profile (error: failed to load - retry or back to feed)",
                           ICON_WARN, "Couldn't load this profile",
                           "Something went wrong while loading this track record. Try again, or go back to events.",
                           '<a href="public-profile.html"><button type="button" class="state-btn primary">Try again</button></a>'
                           '<a href="event-feed.html"><button type="button" class="state-btn">Back to events</button></a>')
    else:  # not-found
        main = state_block("Profile", "zone: Public Profile (not-found / link-expired: stale link -> Event Feed)",
                           ICON_GHOST, "Profile not found",
                           "This profile no longer exists or the share link has expired. The track record may have been removed.",
                           '<a href="event-feed.html"><button type="button" class="state-btn primary">Go to events</button></a>')
    # Public, read-only view of another user, reached via an external shared-card
    # link (viewer is often logged out), so it carries the logged-out header.
    device = S.HEADER_OUT_OPEN + main + S.bottom_out("none") + "    " + S.FOOTER + "\n"
    authstate = "viewing another user - state: " + {"success": "success (read-only track record)",
                                                    "loading": "loading (profile fetch)", "error": "error (load failed)",
                                                    "not-found": "not-found / link-expired"}[state]
    title = f"Wireframe - Public Profile ({authstate})"
    html = S.assemble(title, cur_file, "Public Profile", authstate, switcher(PUB_FILES, PUB_LABELS, state), device, PUB_SIDE)
    html = html.replace("</head>", PROFILE_CSS + "</head>", 1)
    return S.write(cur_file, html)


def switcher(files, labels, state):
    cells = []
    for key, lbl in labels:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{files[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


out = [build_my(s) for s in ("success", "loading", "error")]
out += [build_pub(s) for s in ("success", "loading", "error", "not-found")]
print("\n".join(out))
