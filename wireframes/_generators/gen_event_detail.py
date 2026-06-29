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
    for name, pct, sel in OUTCOMES:  # sel = the outcome currently loaded in the bet panel
        rowcls = "opt-row sel" if sel else "opt-row"
        tag = ' <span class="opt-sel-tag">selected</span>' if sel else ''
        yescls = ' class="sel"' if sel else ''
        rows.append(f'              <div class="{rowcls}"><span class="opt-name">{name}{tag}</span>'
                    f'<span class="opt-prob">{pct}</span>'
                    f'<span class="yesno compact"><button type="button"{yescls}>YES</button><button type="button">NO</button></span></div>')
    return ('          <section class="ed-section" id="edOutcomes">\n'
            '            <h3>Outcomes</h3>\n'
            '            <div class="options opt-list">\n' + "\n".join(rows) + '\n            </div>\n'
            '            <p class="fine">Tap YES or NO on an outcome to load it into the bet panel. The panel stays focused on the one you picked, however long this list gets.</p>\n'
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
        # Focused on the outcome picked in the left list (scales past a long list,
        # 10-20 outcomes, since the panel never repeats the whole list).
        return ('              <span class="field-label">Your outcome</span>\n'
                '              <div class="bp-selected">\n'
                '                <span class="bp-sel-name">JD Vance <span class="opt-prob">41%</span></span>\n'
                '                <a href="#edOutcomes" class="bp-change">Change</a>\n'
                '              </div>\n'
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


# ---------- content tabs (Comments / Top Holders / Positions / Activity) ----------
TAB_CSS = """
    /* ---- Event Detail content tabs (Comments / Top Holders / Positions / Activity) ---- */
    .ed-tabs { padding: 0; }
    .ed-tabwrap { border-top: 1px solid #ccc; }
    .ed-tabradio { position: absolute; left: -9999px; }
    .ed-tabbar { display: flex; gap: 0; overflow-x: auto; border-bottom: 1px solid #999; background: #ededed; }
    .ed-tablabel { flex: 0 0 auto; padding: 9px 12px; font-size: 12px; cursor: pointer; border-right: 1px solid #ccc; white-space: nowrap; color: #555; }
    .ed-tab-count { font-size: 10px; color: #777; }
    .ed-tabpanel { display: none; padding: 10px; }
    #edtab-comments:checked ~ .ed-tabbar label[for="edtab-comments"],
    #edtab-holders:checked ~ .ed-tabbar label[for="edtab-holders"],
    #edtab-positions:checked ~ .ed-tabbar label[for="edtab-positions"],
    #edtab-activity:checked ~ .ed-tabbar label[for="edtab-activity"] { background: #f4f4f4; color: #111; font-weight: bold; box-shadow: inset 0 -2px 0 #777; }
    #edtab-comments:checked ~ .ed-panel-comments,
    #edtab-holders:checked ~ .ed-panel-holders,
    #edtab-positions:checked ~ .ed-panel-positions,
    #edtab-activity:checked ~ .ed-panel-activity { display: block; }
    .cmt-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; font-size: 11px; color: #555; }
    .cmt-controls .seg { display: inline-flex; border: 1px solid #999; }
    .cmt-controls .seg button { border: none; border-right: 1px solid #999; background: #e2e2e2; padding: 4px 8px; font-size: 11px; cursor: pointer; }
    .cmt-controls .seg button:last-child { border-right: none; }
    .cmt-controls .seg button.sel { background: #c4c4c4; font-weight: bold; }
    .cmt-compose { display: flex; gap: 8px; align-items: center; border: 1px solid #bbb; background: #ededed; padding: 8px; margin-bottom: 10px; }
    .cmt-av { width: 28px; height: 28px; flex: 0 0 28px; border: 1px solid #999; background: #d2d2d2; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 8px; color: #555; }
    .cmt-input { flex: 1; border: 1px solid #888; background: #fff; padding: 8px; font-size: 12px; color: #777; }
    .cmt-post { border: 1px solid #888; background: #c4c4c4; padding: 8px 12px; font-size: 12px; font-weight: bold; cursor: pointer; }
    .cmt-signin { width: 100%; border: 1px dashed #999; background: #ededed; padding: 12px; font-size: 12px; text-align: center; cursor: pointer; }
    .cmt-list { display: flex; flex-direction: column; gap: 12px; }
    .cmt { display: flex; gap: 8px; }
    .cmt.reply { margin-left: 32px; }
    .cmt-body { flex: 1; min-width: 0; }
    .cmt-meta { font-size: 11px; color: #555; display: flex; gap: 6px; flex-wrap: wrap; align-items: baseline; }
    .cmt-user { font-weight: bold; color: #222; font-size: 12px; }
    .cmt-badge { border: 1px solid #bbb; background: #e6e6e6; font-size: 9px; padding: 0 5px; }
    .cmt-text { font-size: 12px; margin: 3px 0; }
    .cmt-actions { display: flex; gap: 14px; font-size: 11px; color: #555; }
    .cmt-actions button { border: none; background: transparent; padding: 0; font-size: 11px; color: #555; cursor: pointer; display: inline-flex; gap: 4px; align-items: center; }
    .cmt-actions .ic { width: 13px; height: 13px; }
    .hold-cols { display: flex; flex-direction: column; gap: 12px; }
    .hold-col h4 { font-size: 12px; margin: 0 0 4px; }
    .hold-row { display: flex; align-items: center; gap: 8px; font-size: 12px; padding: 5px 0; border-top: 1px solid #e0e0e0; }
    .hold-row:first-of-type { border-top: none; }
    .hold-rank { width: 14px; color: #777; font-size: 11px; }
    .hold-name { flex: 1; }
    .hold-out { border: 1px solid #bbb; background: #e6e6e6; font-size: 9px; padding: 0 5px; white-space: nowrap; }
    .hold-amt { color: #555; font-size: 11px; white-space: nowrap; }
    .ptable { width: 100%; font-size: 11px; border-collapse: collapse; }
    .ptable th, .ptable td { text-align: left; padding: 6px 6px; border-bottom: 1px solid #e0e0e0; }
    .ptable th { color: #555; font-size: 10px; text-transform: uppercase; letter-spacing: .03em; }
    .ptable tr.you td { background: #e6e6e6; font-weight: bold; }
    .pos-side { border: 1px solid #999; background: #dcdcdc; padding: 0 5px; font-size: 10px; }
    .pos-note { font-size: 11px; color: #555; margin: 8px 0 0; }
    .act-list { display: flex; flex-direction: column; }
    .act-row { display: flex; gap: 8px; align-items: center; font-size: 12px; padding: 7px 0; border-top: 1px solid #e0e0e0; }
    .act-row:first-child { border-top: none; }
    .act-txt { flex: 1; min-width: 0; }
    .act-time { color: #777; font-size: 10px; white-space: nowrap; }
    /* multi: left list marks the selected outcome; right panel focuses on it */
    .opt-row.sel { background: #e6e6e6; border-left: 3px solid #777; padding-left: 6px; }
    .opt-sel-tag { font-size: 9px; border: 1px solid #999; background: #dcdcdc; padding: 0 5px; }
    .bp-selected { display: flex; align-items: center; justify-content: space-between; gap: 8px; border: 1px solid #888; background: #dcdcdc; padding: 8px; }
    .bp-sel-name { font-size: 13px; font-weight: bold; display: flex; align-items: center; gap: 6px; }
    .bp-change { font-size: 10px; color: #333; text-decoration: underline; white-space: nowrap; }
    @media (min-width: 640px) {
      .hold-cols { flex-direction: row; }
      .hold-col { flex: 1; }
      .hold-col:first-child { border-right: 1px solid #ddd; padding-right: 12px; }
    }
"""

HEART = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 '
         '6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>')


def _cmt(av, user, badge, time, text, likes, reply=False):
    b = f'<span class="cmt-badge">{badge}</span>' if badge else ''
    cls = "cmt reply" if reply else "cmt"
    return (f'                <div class="{cls}">\n'
            f'                  <span class="cmt-av">{av}</span>\n'
            f'                  <div class="cmt-body">\n'
            f'                    <div class="cmt-meta"><span class="cmt-user">{user}</span>{b}<span>{time}</span></div>\n'
            f'                    <p class="cmt-text">{text}</p>\n'
            f'                    <div class="cmt-actions"><button type="button">{HEART}{likes}</button><button type="button">Reply</button></div>\n'
            f'                  </div>\n'
            f'                </div>\n')


def comments_panel(auth, view):
    badge1 = "Holds 320 JD Vance" if view == "multi" else "Holds 320 YES"
    badge2 = "Holds 150 Donald Trump" if view == "multi" else "Holds 150 NO"
    if auth == "in":
        compose = ('              <div class="cmt-compose">\n'
                   '                <span class="cmt-av">you</span>\n'
                   '                <span class="cmt-input">Add a comment...</span>\n'
                   '                <button type="button" class="cmt-post">Post</button>\n'
                   '              </div>\n')
    else:
        compose = '              <button type="button" class="cmt-signin" data-open="signin">Sign in to join the discussion</button>\n'
    lst = (_cmt("mm", "marketmaven", badge1, "2h ago",
               "These always go to the wire. I am holding my position and adding if it dips.", "24")
           + _cmt("dd", "deadline_dan", "", "1h ago",
                  "The committee bloc looks firmer this time though.", "6", reply=True)
           + _cmt("pp", "polly_predicts", badge2, "5h ago",
                  "Volume jumped right after the headline. Watching how it settles.", "11")
           + _cmt("nh", "newhere", "", "1d ago",
                  "First bet here. The resolution source being official notices makes this easy to trust.", "8"))
    return ('            <div class="ed-tabpanel ed-panel-comments" role="tabpanel" aria-label="Comments">\n'
            '              <div class="cmt-controls">\n'
            '                <span>128 comments</span>\n'
            '                <span class="seg"><button type="button" class="sel">Newest</button>'
            '<button type="button">Top</button><button type="button">Holders</button></span>\n'
            '              </div>\n'
            + compose
            + '              <div class="cmt-list">\n' + lst + '              </div>\n'
            '            </div>\n')


def holders_panel(view):
    open_tag = '            <div class="ed-tabpanel ed-panel-holders" role="tabpanel" aria-label="Top holders">\n'
    if view == "multi":
        # multi-outcome: one ranked list, each holder tagged with the outcome they hold
        rows = [("whale_07", "JD Vance", "1,240"), ("hedge_hannah", "Donald Trump", "980"),
                ("marketmaven", "JD Vance", "620"), ("alpha_ape", "Ron DeSantis", "410"),
                ("satoshi_jr", "Nikki Haley", "250"), ("riskoff", "Other", "180")]
        rr = "".join(
            f'                <div class="hold-row"><span class="hold-rank">{i}</span>'
            f'<span class="cmt-av">{n[:2]}</span>'
            f'<span class="hold-name">{n} <span class="hold-out">{out}</span></span>'
            f'<span class="hold-amt">{a} shares</span></div>\n' for i, (n, out, a) in enumerate(rows, 1))
        return (open_tag
                + '              <div class="hold-cols">\n'
                '                <div class="hold-col">\n                  <h4>Top holders by outcome</h4>\n'
                + rr + '                </div>\n              </div>\n            </div>\n')
    yes = [("whale_07", "1,240"), ("marketmaven", "320"), ("alpha_ape", "280"), ("satoshi_jr", "150")]
    no = [("hedge_hannah", "980"), ("polly_predicts", "150"), ("caut_carl", "120"), ("riskoff", "90")]

    def col(title, rows):
        rr = "".join(
            f'                <div class="hold-row"><span class="hold-rank">{i}</span>'
            f'<span class="cmt-av">{n[:2]}</span><span class="hold-name">{n}</span>'
            f'<span class="hold-amt">{a} shares</span></div>\n' for i, (n, a) in enumerate(rows, 1))
        return f'              <div class="hold-col">\n                <h4>{title}</h4>\n' + rr + '              </div>\n'
    return (open_tag + '              <div class="hold-cols">\n' + col("YES holders", yes) + col("NO holders", no)
            + '              </div>\n            </div>\n')


def positions_panel(auth, view):
    if view == "multi":
        col2 = "Outcome"
        rows = [("whale_07", "JD Vance", "1,240", "$0.35", "$434"), ("hedge_hannah", "Donald Trump", "980", "$0.20", "$196"),
                ("marketmaven", "JD Vance", "620", "$0.41", "$254"), ("polly_predicts", "Ron DeSantis", "150", "$0.14", "$21")]
        you = ('                <tr class="you"><td>You</td><td><span class="pos-side">JD Vance</span></td>'
               '<td>13</td><td>$0.41</td><td>$5.33</td></tr>\n') if auth == "in" else ''
    else:
        col2 = "Side"
        rows = [("whale_07", "YES", "1,240", "$0.35", "$471"), ("hedge_hannah", "NO", "980", "$0.60", "$588"),
                ("marketmaven", "YES", "320", "$0.41", "$121"), ("polly_predicts", "NO", "150", "$0.58", "$87")]
        you = ('                <tr class="you"><td>You</td><td><span class="pos-side">YES</span></td>'
               '<td>13</td><td>$0.38</td><td>$4.94</td></tr>\n') if auth == "in" else ''
    body = you + "".join(
        f'                <tr><td>{u}</td><td><span class="pos-side">{s}</span></td>'
        f'<td>{sh}</td><td>{a}</td><td>{v}</td></tr>\n' for u, s, sh, a, v in rows)
    note = ('              <p class="pos-note">Your row is highlighted. Positions update as the market trades.</p>\n'
            if auth == "in"
            else '              <button type="button" class="cmt-signin" data-open="signin">Sign in to open and track your position</button>\n')
    return ('            <div class="ed-tabpanel ed-panel-positions" role="tabpanel" aria-label="Positions">\n'
            '              <table class="ptable">\n'
            f'                <thead><tr><th>Holder</th><th>{col2}</th><th>Shares</th><th>Avg</th><th>Value</th></tr></thead>\n'
            '                <tbody>\n' + body + '                </tbody>\n'
            '              </table>\n' + note + '            </div>\n')


def activity_panel(view):
    if view == "multi":
        acts = [("wh", "whale_07", "bought", "500 JD Vance YES", "$0.41", "$205", "2m ago"),
                ("hh", "hedge_hannah", "bought", "300 Donald Trump YES", "$0.22", "$66", "14m ago"),
                ("mm", "marketmaven", "sold", "80 JD Vance YES", "$0.41", "$33", "1h ago"),
                ("po", "polly_predicts", "bought", "150 Ron DeSantis YES", "$0.14", "$21", "3h ago"),
                ("nh", "newhere", "bought", "20 Nikki Haley YES", "$0.08", "$1.60", "5h ago")]
    else:
        acts = [("wh", "whale_07", "bought", "500 YES", "$0.35", "$175", "2m ago"),
                ("hh", "hedge_hannah", "bought", "300 NO", "$0.60", "$180", "14m ago"),
                ("mm", "marketmaven", "sold", "80 YES", "$0.39", "$31", "1h ago"),
                ("pp", "polly_predicts", "bought", "150 NO", "$0.58", "$87", "3h ago"),
                ("nh", "newhere", "bought", "13 YES", "$0.38", "$4.94", "5h ago")]
    rows = "".join(
        f'              <div class="act-row"><span class="cmt-av">{av}</span>'
        f'<span class="act-txt"><b>{u}</b> {act} <b>{sz}</b> at {pr} ({val})</span>'
        f'<span class="act-time">{t}</span></div>\n' for av, u, act, sz, pr, val, t in acts)
    return ('            <div class="ed-tabpanel ed-panel-activity" role="tabpanel" aria-label="Activity">\n'
            '              <p class="pos-note" style="margin:0 0 8px;">Recent trades, largest first. Filter: over $5.</p>\n'
            '              <div class="act-list">\n' + rows + '              </div>\n'
            '            </div>\n')


def tabs_section(view, auth):
    return ('          <section class="ed-section ed-tabs">\n'
            '            <div class="ed-tabwrap">\n'
            '              <input type="radio" name="edtab" id="edtab-comments" class="ed-tabradio" checked>\n'
            '              <input type="radio" name="edtab" id="edtab-holders" class="ed-tabradio">\n'
            '              <input type="radio" name="edtab" id="edtab-positions" class="ed-tabradio">\n'
            '              <input type="radio" name="edtab" id="edtab-activity" class="ed-tabradio">\n'
            '              <div class="ed-tabbar" role="tablist">\n'
            '                <label class="ed-tablabel" for="edtab-comments">Comments <span class="ed-tab-count">128</span></label>\n'
            '                <label class="ed-tablabel" for="edtab-holders">Top Holders</label>\n'
            '                <label class="ed-tablabel" for="edtab-positions">Positions</label>\n'
            '                <label class="ed-tablabel" for="edtab-activity">Activity</label>\n'
            '              </div>\n'
            + comments_panel(auth, view) + holders_panel(view) + positions_panel(auth, view) + activity_panel(view)
            + '            </div>\n'
            '          </section>\n')


def main_success(view, panel_state, auth):
    zone = ("binary: chart, facts, why-this-price, resolution, tabs + sticky bet panel" if view == "binary"
            else "multi-outcome: outcomes, chart, why-this-price, tabs + sticky bet panel (pick an outcome)")
    return ('    <main class="feed">\n'
            f'      <span class="zone-tag">zone: event detail ({zone})</span>\n'
            '      <div class="ed-layout">\n'
            '        <div class="ed-main">\n'
            + main_text(view)
            + tabs_section(view, auth)
            + '        </div>\n'
            + bet_panel(view, panel_state)
            + '      </div>\n'
            '    </main>\n'
            + bet_dock(view))


def main_resolved(auth="in"):
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
    # Reuse the live binary body, but reframe it for a closed market: the meta line
    # marks trading closed and the chart caption reads "at close" rather than "now",
    # so the body no longer implies live, actionable odds (the bet panel/dock are
    # already omitted on this state). Outcome is opened from the position (Active Bets).
    body = (main_text("binary")
            .replace('Politics &middot; One-time market',
                     'Politics &middot; One-time market &middot; Trading closed', 1)
            .replace('YES 38% now', 'YES 38% at close', 1))
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: event detail (resolved-while-reading / event-closed: market closed)</span>\n'
            + banner
            + '      <div class="feed-inner"><div class="ed-main">\n' + body
            + tabs_section("binary", auth) + '      </div></div>\n'
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
        <li><strong>Content tabs (Comments / Top Holders / Positions / Activity)</strong> -&gt; below the event content, a Polymarket-style tab strip (CSS-only switch). Comments has sort + composer (logged-out prompts sign-in); Positions highlights your row when logged in; Holders and Activity are public. Depth / social proof for FJ2 and engagement.</li>
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
        main = main_success(view, panel, auth)
    elif state_key == "resolved":
        main = main_resolved(auth)
    else:
        main = {"error": main_error, "loading": main_loading}[state_key]()
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
    if state_key in ("binary", "multi", "resolved"):
        html = html.replace("\n  </style>", TAB_CSS + "  </style>", 1)
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
