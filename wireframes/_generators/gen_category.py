import _shell as S


def binary_card(q, pct, vol, closes, marked=False):
    pressed = "true" if marked else "false"
    lbl = "Bookmarked" if marked else "Bookmark"
    return f"""          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb">thumbnail placeholder</span>
                <a class="q" href="event-detail.html">{q}</a>
              </div>
              <p class="prob-line">YES <span class="prob">{pct}</span></p>
              <div class="yesno"><button type="button">YES</button><button type="button">NO</button></div>
              <p class="meta">
                <span class="meta-txt"><span>Volume: {vol}</span><span>Closes: {closes}</span></span>
                <button type="button" class="bookmark-btn" aria-pressed="{pressed}" aria-label="{lbl}">
                  <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4z"/></svg>
                </button>
              </p>
            </div>
          </article>"""


def multi_card(q, o1, p1, o2, p2, vol, closes):
    return f"""          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb">thumbnail placeholder</span>
                <a class="q" href="event-detail.html">{q}</a>
              </div>
              <div class="options">
                <div class="opt-row"><span class="opt-name">{o1}</span><span class="opt-prob">{p1}</span><span class="yesno compact"><button type="button">YES</button><button type="button">NO</button></span></div>
                <div class="opt-row"><span class="opt-name">{o2}</span><span class="opt-prob">{p2}</span><span class="yesno compact"><button type="button">YES</button><button type="button">NO</button></span></div>
              </div>
              <p class="meta">
                <span class="meta-txt"><span>Volume: {vol}</span><span>Closes: {closes}</span></span>
                <button type="button" class="bookmark-btn" aria-pressed="false" aria-label="Bookmark">
                  <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4z"/></svg>
                </button>
              </p>
            </div>
          </article>"""


CATEGORIES = {
    "Politics": {
        "stem": "politics",
        "subcats": [("All", "2K"), ("Trump", "297"), ("Trump Daily", "3"), ("Midterm Elections", "537"),
                    ("Global Elections", "122"), ("Primaries", "106"), ("Congress", "42"), ("Trump Cabinet", "16"),
                    ("Courts", "30"), ("Epstein", "22"), ("Government Shutdown", "3"), ("LA Mayor", "5")],
        "cards": [
            binary_card("Will the US government shut down before March 1, 2027?", "38%", "$84,200", "Mar 1, 2027"),
            binary_card("Will Democrats win control of the House in the 2026 midterms?", "53%", "$410,000", "Nov 3, 2026", marked=True),
            multi_card("Who will win the 2028 Republican presidential nomination?", "JD Vance", "41%", "Donald Trump", "22%", "$1,200,000", "Jul 1, 2028"),
            binary_card("Will Trump's average approval exceed 45% in Q1 2027?", "34%", "$96,500", "Apr 1, 2027"),
            binary_card("Will a new Supreme Court justice be confirmed before July 1, 2027?", "19%", "$52,300", "Jul 1, 2027"),
            binary_card("Will the full Epstein files be released before January 1, 2027?", "27%", "$73,800", "Jan 1, 2027"),
        ],
    },
    "Crypto": {
        "stem": "crypto",
        "subcats": [("All", "2K"), ("Bitcoin", "312"), ("Ethereum", "168"), ("Solana", "74"),
                    ("Price Predictions", "220"), ("ETFs", "33"), ("Stablecoins", "19"), ("Memecoins", "58"),
                    ("Layer 2s", "27"), ("Fed & Macro", "41")],
        "cards": [
            binary_card("Will Bitcoin close above $150,000 before October 1, 2026?", "61%", "$212,900", "Oct 1, 2026", marked=True),
            binary_card("Will Ethereum complete its next major network upgrade before November 1, 2026?", "72%", "$147,650", "Nov 1, 2026"),
            multi_card("Which coin will have the highest market cap on January 1, 2027?", "Bitcoin", "88%", "Ethereum", "9%", "$540,000", "Jan 1, 2027"),
            binary_card("Will a spot Solana ETF be approved before July 1, 2027?", "44%", "$61,200", "Jul 1, 2027"),
            binary_card("Will USDC remain fully backed 1:1 through 2026?", "96%", "$30,100", "Jan 1, 2027"),
            binary_card("Will any memecoin enter the top 10 by market cap before 2027?", "23%", "$18,400", "Jan 1, 2027"),
        ],
    },
    "Culture": {
        "stem": "culture",
        "subcats": [("All", "1.4K"), ("Movies", "180"), ("Music", "120"), ("Awards", "64"),
                    ("TV & Streaming", "90"), ("Celebrities", "145"), ("Internet & Memes", "38"),
                    ("Books", "22"), ("Gaming", "51")],
        "cards": [
            binary_card("Will the next lead actor for the Bond film be announced before December 31, 2026?", "47%", "$19,400", "Dec 31, 2026"),
            multi_card("Who will win Album of the Year at the 2027 Grammys?", "Taylor Swift", "29%", "Kendrick Lamar", "24%", "$44,500", "Feb 1, 2027"),
            binary_card("Will a single film cross $2B at the global box office in 2026?", "31%", "$27,800", "Jan 1, 2027"),
            binary_card("Will the most-streamed show of 2026 be a returning series?", "58%", "$15,900", "Jan 1, 2027"),
            multi_card("Who will win the 2027 Eurovision final?", "Sweden", "34%", "Italy", "27%", "$61,500", "May 15, 2027"),
            binary_card("Will a reunion tour by a 1990s band be announced before 2027?", "63%", "$12,300", "Jan 1, 2027"),
        ],
    },
    "General": {
        "stem": "general",
        "subcats": [("All", "1.1K"), ("Science & Tech", "160"), ("Climate", "88"), ("Space", "54"),
                    ("AI", "132"), ("Health", "70"), ("Business", "96"), ("World", "140")],
        "cards": [
            binary_card("Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?", "55%", "$26,300", "Apr 1, 2027"),
            binary_card("Will a crewed mission launch toward the Moon before January 1, 2028?", "42%", "$48,700", "Jan 1, 2028"),
            multi_card("Which company will reach a $5T market cap first?", "Nvidia", "46%", "Apple", "21%", "$210,000", "Jan 1, 2028"),
            binary_card("Will a major AI model pass a recognized medical-licensing exam in 2026?", "67%", "$33,400", "Jan 1, 2027"),
            binary_card("Will the EU formally admit a new member state before January 1, 2028?", "23%", "$33,100", "Jan 1, 2028"),
            binary_card("Will a new global pandemic be declared by the WHO in 2026?", "12%", "$22,600", "Jan 1, 2027"),
        ],
    },
}

STATE_LABELS = [("success", "Success"), ("empty", "Empty"), ("error", "Error"), ("loading", "Loading")]


def files_for(stem):
    inn = {"success": f"{stem}.html", "empty": f"{stem}-empty.html",
           "error": f"{stem}-error.html", "loading": f"{stem}-loading.html"}
    out = {"success": f"{stem}-logged-out.html", "empty": f"{stem}-logged-out-empty.html",
           "error": f"{stem}-logged-out-error.html", "loading": f"{stem}-logged-out-loading.html"}
    return inn, out


def switcher(stem, auth, state):
    inn, out = files_for(stem)
    a_in = ' aria-current="page"' if auth == "in" else ""
    a_out = ' aria-current="page"' if auth == "out" else ""
    rows = ['  <nav class="state-switch" aria-label="States of this screen (auth and screen state)">']
    rows.append(f'    <div class="ss-row"><span class="ss-label">Auth</span>'
                f'<a href="{inn[state]}"{a_in}>Logged in</a>'
                f'<a href="{out[state]}"{a_out}>Logged out</a></div>')
    table = inn if auth == "in" else out
    cell_list = []
    for k, lbl in STATE_LABELS:
        cur = ' aria-current="page"' if k == state else ''
        cell_list.append(f'<a href="{table[k]}"{cur}>{lbl}</a>')
    cells = "".join(cell_list)
    rows.append(f'    <div class="ss-row"><span class="ss-label">State</span>{cells}</div>')
    rows.append('  </nav>')
    return "\n".join(rows)


def subcat_panel(name, subcats):
    lis = []
    for i, (sub, cnt) in enumerate(subcats):
        cur = ' aria-current="page"' if i == 0 else ""
        lis.append(f'        <li{cur}><button type="button">{sub} <span class="cnt">{cnt}</span></button></li>')
    return (f'      <nav class="subcat" aria-label="{name} sub-categories">\n'
            '        <span class="zone-tag">zone: sub-categories (left rail on desktop, scrolling chips on mobile; counts are sample data)</span>\n'
            '        <p class="subcat-head">Sub-categories</p>\n'
            '        <ul>\n' + "\n".join(lis) + '\n        </ul>\n'
            '      </nav>\n')


def head_row(name):
    return f"""        <div class="feed-head">
          <h2 id="feedHeading">{name}</h2>
          <div class="feed-controls">

            <details class="filter-menu" id="sortMenu">
              <summary aria-label="Sort by">
                <svg class="ic-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h12M4 12h8M4 17h4"/></svg>
                <span>Sort: <span id="sortCurrent">Trending</span></span>
                <svg class="ic-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
              </summary>
              <div class="filter-panel">
                <span class="zone-tag">sort options</span>
                <ul role="radiogroup" aria-label="Sort by">
                  <li><label><input type="radio" name="sort" value="Trending" checked> Trending</label></li>
                  <li><label><input type="radio" name="sort" value="Volatile"> Volatile</label></li>
                  <li><label><input type="radio" name="sort" value="New"> New</label></li>
                  <li><label><input type="radio" name="sort" value="Closing soon"> Closing soon</label></li>
                  <li><label><input type="radio" name="sort" value="Volume"> Volume</label></li>
                  <li><label><input type="radio" name="sort" value="50-50"> 50-50 (most contested)</label></li>
                </ul>
                <div class="reverse-row">
                  <span>Reverse sort</span>
                  <button type="button" class="toggle" role="switch" aria-checked="false">off</button>
                </div>
              </div>
            </details>

            <details class="filter-menu" id="freqMenu">
              <summary aria-label="Filter by frequency">
                <svg class="ic-sm" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
                <span>Frequency: <span id="freqCurrent">All</span></span>
                <svg class="ic-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
              </summary>
              <div class="filter-panel">
                <span class="zone-tag">event frequency (recurring markets)</span>
                <ul role="radiogroup" aria-label="Frequency">
                  <li><label><input type="radio" name="freq" value="All" checked> All</label></li>
                  <li><label><input type="radio" name="freq" value="One-time"> One-time</label></li>
                  <li><label><input type="radio" name="freq" value="Hourly"> Hourly</label></li>
                  <li><label><input type="radio" name="freq" value="Daily"> Daily</label></li>
                  <li><label><input type="radio" name="freq" value="Weekly"> Weekly</label></li>
                  <li><label><input type="radio" name="freq" value="Monthly"> Monthly</label></li>
                </ul>
              </div>
            </details>

          </div>
        </div>
"""


SK_CARD = """          <article class="card skeleton" aria-hidden="true">
            <div class="card-body">
              <div class="top"><span class="sk-thumb"></span><div class="sk-head"><div class="sk-line w80"></div><div class="sk-line w60"></div></div></div>
              <div class="sk-line w40"></div>
              <div class="sk-row"><span class="sk-btn"></span><span class="sk-btn"></span></div>
            </div>
          </article>"""

ICON_INBOX = '<path d="M3 13l3-8h12l3 8M3 13v6h18v-6M3 13h5l2 3h4l2-3h5"/>'
ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'


def grid_for(name, cards, state, clear_href="event-feed.html"):
    if state == "success":
        return '          <div class="grid">\n\n' + "\n".join(cards) + '\n\n          </div>\n'
    if state == "loading":
        return ('          <div class="grid" aria-busy="true">\n\n'
                + "\n".join([SK_CARD] * 6) + '\n\n          </div>\n')
    if state == "empty":
        return (f'          <div class="state-block">\n'
                f'            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICON_INBOX}</svg>\n'
                f'            <h2 class="state-title">No events match these filters</h2>\n'
                f'            <p class="state-msg">No {name} markets match the current sub-category and filters. Clear the filters, or get notified when new ones open.</p>\n'
                f'            <div class="state-actions">\n'
                f'              <a href="{clear_href}"><button type="button" class="state-btn primary">Clear filters</button></a>\n'
                f'              <button type="button" class="state-btn">Notify me of new {name} events</button>\n'
                f'            </div>\n'
                f'          </div>\n')
    if state == "error":
        return (f'          <div class="state-block">\n'
                f'            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICON_WARN}</svg>\n'
                f'            <h2 class="state-title">Couldn\'t load {name}</h2>\n'
                f'            <p class="state-msg">Something went wrong while loading these markets. Check your connection and try again.</p>\n'
                f'            <div class="state-actions">\n'
                f'              <button type="button" class="state-btn primary">Try again</button>\n'
                f'              <a href="event-feed.html"><button type="button" class="state-btn">Back to Trending</button></a>\n'
                f'            </div>\n'
                f'          </div>\n')


def main_for(name, c, state, clear_href="event-feed.html"):
    zone = {"success": "sub-category rail + sort/frequency + filtered grid",
            "empty": "empty: no events match the sub-category / filters (T6 subscribe exit)",
            "error": "error: failed to load, retry",
            "loading": "loading: fetching markets (skeleton grid)"}[state]
    return ('    <main class="feed">\n'
            f'      <span class="zone-tag">zone: {name} category ({zone})</span>\n'
            '      <div class="cat-layout">\n'
            + subcat_panel(name, c["subcats"])
            + '      <div class="cat-main">\n'
            + '        <div class="feed-inner">\n'
            + head_row(name)
            + grid_for(name, c["cards"], state, clear_href)
            + '        </div>\n'
            + '      </div>\n'
            + '      </div>\n'
            + '    </main>\n')


def side(name):
    return f"""    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Category = its own page (not an in-feed toggle)</strong> -&gt; the second-level nav routes to a real page per category ({name} here). Trending stays the main feed (event-feed.html).</li>
        <li><strong>Sub-category side panel with counts</strong> -&gt; Polymarket-style drill-down inside the category. Left sticky rail on desktop, scrolling chips on mobile. Counts are illustrative sample data (Addition B).</li>
        <li><strong>Auth axis (logged in / logged out)</strong> -&gt; a browse screen like Event Feed: the body and rail are identical, only the header differs (logged-out drops the account and shows Log in / Sign up, which open the Sign In dialog over this page).</li>
        <li><strong>States</strong> -&gt; success (grid), empty (no match: Clear filters or "Notify me", the T6 subscribe edge), error (Try again or back to Trending), loading (skeleton grid). Each is its own page.</li>
        <li><strong>Cards reuse the shared S3 pattern</strong> -&gt; binary and multi-outcome, question links to Event Detail, YES/NO trigger-entry, bookmark in the meta row.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (where this sits)</span>
<pre>Events (browse)
   Event Feed  (Trending = main)
   Politics / Crypto / Culture / General
        ^ [{name}]   &lt;- current category page
        v
   Event Detail
        v
   Sign In / Deposit (dialogs) -> Active Bets</pre>
        <p class="ref">A category page is a browse entry parallel to the main feed
          (IA/sitemap.md second-level navigation), with the auth axis and the
          success / empty / error / loading states.</p>
      </section>

      <section class="navtree" aria-label="Rollout">
        <span class="zone-tag">rollout status</span>
        <p class="ref">Built: Politics, Crypto, Culture, General, each with logged-in
          and logged-out x success / empty / error / loading. Still to come: the real
          sub-category taxonomy per category and the sitemap.md update (category pages
          + sub-categories).</p>
      </section>
    </div>
"""


def build(name, auth, state):
    c = CATEGORIES[name]
    inn, out = files_for(c["stem"])
    cur_file = (inn if auth == "in" else out)[state]
    header = S.HEADER_IN_OPEN if auth == "in" else S.HEADER_OUT_OPEN
    bottom = S.bottom_in("events") if auth == "in" else S.bottom_out()
    # Clear filters -> the cleared (unfiltered) category view, same auth variant.
    clear_href = (inn if auth == "in" else out)["success"]
    device = header + S.cat_nav(name) + main_for(name, c, state, clear_href) + bottom + "    " + S.FOOTER + "\n"
    authstate = (("logged in" if auth == "in" else "logged out") + " - state: "
                 + {"success": f"success ({name}, sub-categories)", "empty": "empty (no match)",
                    "error": "error (load failed)", "loading": "loading (skeleton)"}[state])
    html = S.assemble(f"Wireframe - Category: {name} ({authstate})", cur_file,
                      f"{name} (category)", authstate, switcher(c["stem"], auth, state), device, side(name))
    return S.write(cur_file, html)


out = []
for nm in CATEGORIES:
    for au in ("in", "out"):
        for st in ("success", "empty", "error", "loading"):
            out.append(build(nm, au, st))
print(f"{len(out)} category pages")
print("\n".join(out))
