import _shell as S

IN_STATE = {"binary": "event-detail.html", "multi": "event-detail-multi.html", "error": "event-detail-error.html",
            "loading": "event-detail-loading.html", "resolved": "event-detail-resolved.html"}
OUT_STATE = {"binary": "event-detail-logged-out.html", "multi": "event-detail-logged-out-multi.html",
             "error": "event-detail-logged-out-error.html", "loading": "event-detail-logged-out-loading.html"}
PANEL = {"intent": "event-detail.html", "insufficient": "event-detail-bet-insufficient.html",
         "reconcile": "event-detail-bet-reconcile.html", "processing": "event-detail-bet-processing.html",
         "error": "event-detail-bet-error.html"}


def switcher(auth, state_key, panel_key):
    in_t = IN_STATE.get(state_key, "event-detail.html")
    out_t = OUT_STATE.get(state_key, "event-detail-logged-out.html")
    a_in = ' aria-current="page"' if auth == "in" else ""
    a_out = ' aria-current="page"' if auth == "out" else ""
    rows = ['  <nav class="state-switch" aria-label="States of this screen (auth, view and bet-panel state)">']
    rows.append(f'    <div class="ss-row"><span class="ss-label">Auth</span>'
                f'<a href="{in_t}"{a_in}>Logged in</a><a href="{out_t}"{a_out}>Logged out</a></div>')
    # State / view row
    items = [("binary", "Binary"), ("multi", "Multi"), ("error", "Error"), ("loading", "Loading")]
    if auth == "in":
        items.append(("resolved", "Resolved"))
    table = IN_STATE if auth == "in" else OUT_STATE
    cells = []
    for k, lbl in items:
        cur = ' aria-current="page"' if k == state_key else ''
        cells.append(f'<a href="{table[k]}"{cur}>{lbl}</a>')
    rows.append(f'    <div class="ss-row"><span class="ss-label">View</span>{"".join(cells)}</div>')
    # Bet-panel row (logged-in only)
    if auth == "in":
        pitems = [("intent", "Intent"), ("insufficient", "Insufficient"), ("reconcile", "S5 reconcile"),
                  ("processing", "Processing"), ("error", "On-chain error")]
        pcells = []
        for k, lbl in pitems:
            cur = ' aria-current="page"' if (state_key == "binary" and k == panel_key) else ''
            pcells.append(f'<a href="{PANEL[k]}"{cur}>{lbl}</a>')
        rows.append(f'    <div class="ss-row"><span class="ss-label">Bet</span>{"".join(pcells)}</div>')
    rows.append('  </nav>')
    return "\n".join(rows)


# ---------- main content ----------
HEAD_BINARY = """          <article class="card" style="border:none;">
            <div class="ed-head">
              <span class="ed-thumb">thumbnail placeholder</span>
              <div>
                <span class="ed-cat">Politics &middot; One-time market</span>
                <h2 class="ed-q">Will the US government shut down before March 1, 2027?</h2>
                <p class="ed-prob-big">YES <span class="prob">38%</span> &nbsp; NO <span class="prob">62%</span></p>
              </div>
            </div>
          </article>
"""

HEAD_MULTI = """          <article class="card" style="border:none;">
            <div class="ed-head">
              <span class="ed-thumb">thumbnail placeholder</span>
              <div>
                <span class="ed-cat">Politics &middot; One-time market &middot; 5 outcomes</span>
                <h2 class="ed-q">Who will win the 2028 Republican presidential nomination?</h2>
                <p class="ed-prob-big">Leading: JD Vance <span class="prob">41%</span></p>
              </div>
            </div>
          </article>
"""

OUTCOMES = [("JD Vance", "41%", True), ("Donald Trump", "22%", False), ("Ron DeSantis", "14%", False),
            ("Nikki Haley", "8%", False), ("Other", "15%", False)]


def outcomes_section():
    rows = []
    for name, pct, lead in OUTCOMES:
        tag = ' <span class="ed-cat">leading</span>' if lead else ''
        rows.append(f'              <div class="opt-row"><span class="opt-name">{name}{tag}</span>'
                    f'<span class="opt-prob">{pct}</span>'
                    f'<span class="yesno compact"><button type="button">YES</button><button type="button">NO</button></span></div>')
    return ('          <section class="ed-section">\n'
            '            <h3>Outcomes</h3>\n'
            '            <div class="options opt-list">\n' + "\n".join(rows) + '\n            </div>\n'
            '            <p class="fine">Each outcome trades YES / NO independently. Pick one in the bet panel to stake.</p>\n'
            '          </section>\n')


CHART = """          <section class="ed-section">
            <h3>Price chart</h3>
            <div class="chart-wrap">
              <svg class="chart-svg" viewBox="0 0 300 100" preserveAspectRatio="none" role="img" aria-label="YES probability over the last 30 days (schematic)">
                <line class="grid-l" x1="0" y1="25" x2="300" y2="25"/>
                <line class="grid-l" x1="0" y1="50" x2="300" y2="50"/>
                <line class="grid-l" x1="0" y1="75" x2="300" y2="75"/>
                <polyline points="0,58 25,55 50,63 75,52 100,57 125,49 150,55 175,47 200,52 225,44 250,50 275,43 300,62"/>
                <line class="nowline" x1="300" y1="0" x2="300" y2="100"/>
              </svg>
              <p class="chart-cap"><span>30 days ago</span><span>1d &middot; 1w &middot; 1m &middot; all</span><span>__NOW__</span></p>
            </div>
          </section>
"""

FACTS = """          <div class="ed-facts">
            <span>Volume<b>__VOL__</b></span>
            <span>Liquidity<b>__LIQ__</b></span>
            <span>Closes<b>__CLOSE__</b></span>
            <span>Frequency<b>One-time</b></span>
            <span>Bookmark<b>save event</b></span>
          </div>
"""

WHY_BINARY = """          <section class="ed-section">
            <h3>Why this price</h3>
            <p class="resolution">YES is priced at 38%. Funding talks have stalled twice this quarter, but the last three deadlines were settled at the last minute. What is moving the number:</p>
            <div class="args">
              <div class="arg-col">
                <h4>For YES</h4>
                <ul>
                  <li>Budget talks stalled in committee, no scheduled vote.</li>
                  <li>A bloc has committed to opposing the stopgap bill.</li>
                </ul>
              </div>
              <div class="arg-col">
                <h4>For NO</h4>
                <ul>
                  <li>Last three deadlines met with short-term funding.</li>
                  <li>Both parties signalled willingness to extend.</li>
                </ul>
              </div>
            </div>
          </section>

          <section class="ed-section">
            <h3>Resolution conditions</h3>
            <p class="resolution"><strong>Resolves YES</strong> if a federal funding gap causes a shutdown beginning before 00:00 ET on March 1, 2027. <strong>Resolves NO</strong> if funding is in place through that date.<br>
            <strong>Source:</strong> official US Office of Management and Budget notices. Resolved by the Predict Market team.</p>
          </section>
"""

WHY_MULTI = """          <section class="ed-section">
            <h3>Why this price</h3>
            <p class="resolution">JD Vance leads at 41% as the incumbent-aligned candidate, with Trump-endorsed momentum the main swing factor. What is moving the field:</p>
            <div class="args">
              <div class="arg-col">
                <h4>For the leader (Vance)</h4>
                <ul>
                  <li>Strong early-state polling and party-establishment backing.</li>
                  <li>Front-runner fundraising lead over the rest of the field.</li>
                </ul>
              </div>
              <div class="arg-col">
                <h4>Against / for the field</h4>
                <ul>
                  <li>A late entrant could consolidate the anti-front-runner vote.</li>
                  <li>Early primaries historically reshuffle the order.</li>
                </ul>
              </div>
            </div>
          </section>

          <section class="ed-section">
            <h3>Resolution conditions</h3>
            <p class="resolution"><strong>Resolves to the candidate</strong> who is the Republican Party's official presidential nominee at the 2028 national convention. All other outcomes resolve NO.<br>
            <strong>Source:</strong> official Republican National Committee certification. Resolved by the Predict Market team.</p>
          </section>
"""


def main_text(view):
    if view == "multi":
        chart = CHART.replace("__NOW__", "JD Vance 41% now")
        facts = FACTS.replace("__VOL__", "$1,200,000").replace("__LIQ__", "$180,000").replace("__CLOSE__", "Jul 1, 2028")
        return HEAD_MULTI + outcomes_section() + chart + facts + WHY_MULTI
    chart = CHART.replace("__NOW__", "YES 38% now")
    facts = FACTS.replace("__VOL__", "$84,200").replace("__LIQ__", "$31,500").replace("__CLOSE__", "Mar 1, 2027")
    return HEAD_BINARY + chart + facts + WHY_BINARY


# ---------- bet panel (parameterised by view + panel state) ----------
def panel_dir(view):
    if view == "multi":
        opts = []
        for name, pct, sel in OUTCOMES:
            cls = " sel" if sel else ""
            ch = " checked" if sel else ""
            opts.append(f'                <label class="bp-opt{cls}"><input type="radio" name="bpopt"{ch}> {name} '
                        f'<span class="bp-opt-pct">{pct}</span></label>')
        return ('              <span class="field-label">Pick an outcome</span>\n'
                '              <div class="bp-opts">\n' + "\n".join(opts) + '\n              </div>\n'
                '              <span class="bp-hint">Betting on: <strong>JD Vance</strong></span>\n'
                '              <div class="bp-dir">\n'
                '                <button type="button" class="bp-side sel">YES <span class="bp-pct">41%</span></button>\n'
                '                <button type="button" class="bp-side">NO <span class="bp-pct">59%</span></button>\n'
                '              </div>\n')
    return ('              <div class="bp-dir">\n'
            '                <button type="button" class="bp-side sel">YES <span class="bp-pct">38%</span></button>\n'
            '                <button type="button" class="bp-side">NO <span class="bp-pct">62%</span></button>\n'
            '              </div>\n')


def panel_amount(value="$5.00", sel="$5"):
    chips = ""
    for c in ("$5", "$10", "$25", "$50"):
        cls = ' class="sel"' if c == sel else ''
        chips += f'<button type="button"{cls}>{c}</button>'
    return ('              <div>\n'
            '                <span class="field-label">Amount</span>\n'
            f'                <div class="amount-row"><span class="amount-input">{value}</span></div>\n'
            f'                <div class="quick">{chips}</div>\n'
            '              </div>\n')


LINES = """              <div>
                <div class="line"><span>Price now</span><span>__P__</span></div>
                <div class="line"><span>Fee (only if you win)</span><span>$0.40</span></div>
                <div class="line total"><span>Potential payout</span><span>__PAY__</span></div>
                <div class="line"><span>Your balance</span><span>$42.00</span></div>
              </div>
"""


def panel_tail(state, view):
    p = "41%" if view == "multi" else "38%"
    pay = "$12.20" if view == "multi" else "$13.20"
    lines = LINES.replace("__P__", p).replace("__PAY__", pay)
    if state == "intent":
        return (lines
                + '              <button type="button" class="confirm-btn" data-open="signin">Confirm bet</button>\n'
                + '              <p class="fine">No minimum or maximum. Payout depends on when you bet (AMM). Confirm opens sign-in (over this page), then deposit if needed.</p>\n')
    if state == "insufficient":
        return ('              <div class="inline-error">You have $3.00. You can bet up to $3.00, or add funds to bet more.</div>\n'
                + '              <button type="button" class="confirm-btn" data-open="deposit">Add funds</button>\n'
                + '              <button type="button" class="provider-btn" style="justify-content:center;">Bet $3.00 instead</button>\n'
                + '              <p class="fine">insufficient-balance: inline guard in the panel before the gate fires.</p>\n')
    if state == "reconcile":
        return ('              <div class="reconcile-box">\n'
                '                <strong>The price moved while you signed in</strong>\n'
                '                <span>Was 38% &nbsp;-&gt;&nbsp; Now 41%. Payout $13.20 &nbsp;-&gt;&nbsp; $12.20 for $5.</span>\n'
                '              </div>\n'
                + '              <a href="event-detail-bet-processing.html"><button type="button" class="confirm-btn" style="width:100%;">Confirm at new price (41%)</button></a>\n'
                + '              <a href="event-detail.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Cancel and re-evaluate</button></a>\n'
                + '              <p class="fine">S5 reconcile: shown after the Sign In / Deposit gate, before execute. Confirm goes to execute; cancel re-evaluates the event (T16).</p>\n')
    if state == "processing":
        return ('              <div class="spinner-box">Registering your bet on-chain...<br><span class="fine">A few seconds. Keep this open.</span></div>\n'
                + '              <a href="active-bets.html"><button type="button" class="confirm-btn" style="width:100%;">View your position (on success)</button></a>\n'
                + '              <p class="fine">execute on-chain processing: transitional. On success it lands on Active Bets (T14); on failure, the on-chain error state (T3).</p>\n')
    if state == "error":
        return ('              <div class="inline-error">Your bet did not register on-chain (T3). No funds were taken.</div>\n'
                + '              <a href="event-detail-bet-processing.html"><button type="button" class="confirm-btn" style="width:100%;">Try again</button></a>\n'
                + '              <a href="wallet.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Check wallet</button></a>\n'
                + '              <p class="fine">on-chain error (T3): retry the execute step, or check your wallet balance.</p>\n')
    return lines


PANEL_HINT = {"intent": "YES pre-selected", "insufficient": "amount over balance",
              "reconcile": "price changed", "processing": "submitting", "error": "execute failed"}


def bet_panel(view, state):
    hint = PANEL_HINT[state]
    amount = panel_amount("$25.00", "") if state == "insufficient" else panel_amount()
    return ('          <aside class="bet-panel">\n'
            '            <span class="zone-tag">zone: bet panel (sticky right rail; fast entry, MJ). States migrated from the old Bet modal.</span>\n'
            '            <div class="bp-inner">\n'
            f'              <div class="bp-head"><h3>Place your bet</h3><span class="bp-hint">{hint}</span></div>\n'
            + panel_dir(view)
            + amount
            + panel_tail(state, view)
            + '            </div>\n'
            '          </aside>\n')


def bet_dock(view):
    if view == "multi":
        left = ('        <button type="button" class="bp-side sel">JD Vance YES <span class="bp-pct">41%</span></button>\n'
                '        <button type="button" class="bp-side">NO <span class="bp-pct">59%</span></button>\n')
        meta = '$5 to win<b>$12.20</b>'
    else:
        left = ('        <button type="button" class="bp-side sel">YES <span class="bp-pct">38%</span></button>\n'
                '        <button type="button" class="bp-side">NO <span class="bp-pct">62%</span></button>\n')
        meta = '$5 to win<b>$13.20</b>'
    return ('      <!-- Mobile sticky bet dock (above the bottom nav; taps expand to a confirm sheet) -->\n'
            '      <div class="bet-dock" aria-label="Place your bet">\n'
            + left
            + f'        <span class="dock-meta">{meta}</span>\n'
            '        <button type="button" class="confirm-btn" data-open="signin" style="width:auto;padding:11px 14px;">Bet</button>\n'
            '      </div>\n')


def main_success(view, panel_state):
    zone = ("binary: chart, facts, why-this-price, resolution + sticky bet panel" if view == "binary"
            else "multi-outcome: outcomes list, chart, why-this-price + sticky bet panel (pick an outcome)")
    return ('    <main class="feed">\n'
            f'      <span class="zone-tag">zone: event detail ({zone})</span>\n'
            '      <div class="ed-layout">\n'
            '        <div class="ed-main">\n'
            + main_text(view)
            + '        </div>\n'
            + bet_panel(view, panel_state)
            + '      </div>\n'
            '    </main>\n'
            + bet_dock(view))


def main_resolved():
    banner = """      <div class="state-block" style="margin:8px;">
        <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>
        <h2 class="state-title">This event just resolved</h2>
        <p class="state-msg">The market closed while you were reading (event-closed). Betting is no longer available. You hold a position, so you can open your result.</p>
        <div class="state-actions">
          <a href="active-bets.html"><button type="button" class="state-btn primary">See your position</button></a>
          <a href="event-feed.html"><button type="button" class="state-btn">Back to feed</button></a>
        </div>
      </div>
"""
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: event detail (resolved-while-reading / event-closed: market closed)</span>\n'
            + banner
            + '      <div class="feed-inner"><div class="ed-main">\n' + main_text("binary") + '      </div></div>\n'
            + '    </main>\n')


def main_error():
    return """    <main class="feed">
      <span class="zone-tag">zone: event detail (error: load failed, T8 - retry returns to Event Detail)</span>
      <div class="state-block" style="margin:8px;">
        <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>
        <h2 class="state-title">Couldn't load this event</h2>
        <p class="state-msg">Something went wrong while loading the event details. Check your connection and try again.</p>
        <div class="state-actions">
          <a href="event-detail.html"><button type="button" class="state-btn primary">Try again</button></a>
          <a href="event-feed.html"><button type="button" class="state-btn">Back to feed</button></a>
        </div>
      </div>
    </main>
"""


def main_loading():
    return """    <main class="feed">
      <span class="zone-tag">zone: event detail (loading: event data fetching)</span>
      <div class="ed-layout">
        <div class="ed-main" aria-busy="true">
          <article class="card skeleton" style="border:none;">
            <div class="ed-head">
              <span class="sk-thumb" style="width:72px;height:72px;flex:0 0 72px;"></span>
              <div style="flex:1;">
                <div class="sk-line w40"></div><div class="sk-line w80"></div><div class="sk-line w60"></div>
              </div>
            </div>
          </article>
          <section class="ed-section">
            <div class="sk-line w40"></div>
            <div class="chart-svg" style="display:flex;align-items:center;justify-content:center;color:#777;font-size:11px;">loading chart...</div>
          </section>
          <section class="ed-section">
            <div class="sk-line w40"></div><div class="sk-line w80"></div><div class="sk-line w80"></div><div class="sk-line w60"></div>
          </section>
        </div>
        <aside class="bet-panel">
          <div class="bp-inner" aria-busy="true">
            <div class="sk-line w60"></div>
            <div class="bp-dir"><span class="bp-side" style="background:#e0e0e0;">&nbsp;</span><span class="bp-side" style="background:#e0e0e0;">&nbsp;</span></div>
            <div class="sk-line w80"></div><div class="sk-line w40"></div>
          </div>
        </aside>
      </div>
    </main>
"""


def side(view, panel_state):
    return f"""    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Sticky bet panel (right rail desktop / bottom dock mobile)</strong> -&gt; fast entry (MJ): the bet stays in view while scrolling. Binary = YES / NO; multi-outcome = pick one outcome, then YES / NO on it.</li>
        <li><strong>Bet states migrated into the panel</strong> -&gt; intent, insufficient-balance (inline guard), S5 reconcile (price moved during the gate), execute processing, on-chain error (T3). The old standalone Bet modal is gone; event-closed is the resolved state.</li>
        <li><strong>Price chart (schematic) + Why this price</strong> -&gt; FJ2 differentiator, below the chart and facts so the panel leads.</li>
        <li><strong>Confirm fires the gate</strong> -&gt; opens the Sign In dialog over this page, then Deposit (insufficient-balance jumps straight to the Deposit dialog).</li>
        <li><strong>Auth + states</strong> -&gt; logged-in / logged-out, binary / multi success, error (T8), loading, resolved-while-reading.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (main-flow spine)</span>
<pre>Event Feed
   v
[Event Detail]   &lt;- current ({view}; bet panel: {panel_state})
   v
Sign In / Deposit (dialogs over the page)
   v
Active Bets    (MJ success, T14)</pre>
        <p class="ref">Flow position: MJ, one node after Event Feed. Bet intent + states
          live in the panel; the gate (Sign In, Deposit) fires on Confirm as dialogs.</p>
      </section>
    </div>
"""


def build(auth, state_key, view="binary", panel="intent"):
    cur_file = (IN_STATE if auth == "in" else OUT_STATE)[state_key]
    if state_key == "binary" and panel != "intent":
        cur_file = PANEL[panel]
    header = S.HEADER_IN_OPEN if auth == "in" else S.HEADER_OUT_OPEN
    bottom = S.bottom_in("events") if auth == "in" else S.bottom_out()
    if state_key in ("binary", "multi"):
        main = main_success(view, panel)
    else:
        main = {"error": main_error, "loading": main_loading, "resolved": main_resolved}[state_key]()
    device = header + S.cat_nav("Politics", "zone: second-level navigation (categories; active = this event's category)") + main + bottom + "    " + S.FOOTER + "\n"
    view_lbl = {"binary": "binary", "multi": "multi-outcome"}.get(view, view)
    if state_key in ("binary", "multi"):
        st = f"success / {view_lbl}" + ("" if panel == "intent" else f" - bet panel: {panel}")
    else:
        st = {"error": "error (load failed, T8)", "loading": "loading (fetching event)",
              "resolved": "resolved-while-reading / event-closed"}[state_key]
    authstate = ("logged in" if auth == "in" else "logged out") + " - state: " + st
    html = S.assemble(f"Wireframe - Event Detail ({authstate})", cur_file, "Event Detail",
                      authstate, switcher(auth, state_key, panel), device, side(view_lbl, panel))
    return S.write(cur_file, html)


built = []
# logged-in
built.append(build("in", "binary", "binary", "intent"))            # event-detail.html
built.append(build("in", "multi", "multi", "intent"))              # event-detail-multi.html
built.append(build("in", "error"))
built.append(build("in", "loading"))
built.append(build("in", "resolved"))
for ps in ("insufficient", "reconcile", "processing", "error"):     # bet-panel states (binary)
    built.append(build("in", "binary", "binary", ps))
# logged-out
built.append(build("out", "binary", "binary", "intent"))
built.append(build("out", "multi", "multi", "intent"))
built.append(build("out", "error"))
built.append(build("out", "loading"))
print(f"{len(built)} event-detail pages")
print("\n".join(built))
