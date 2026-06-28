# Shared shell for Step 6 wireframe pages. Extracts the canonical CSS / footer /
# scripts from event-feed.html (so they stay byte-identical) and rebuilds the
# screen-tree nav, headers, and page frame around per-screen bodies.
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")
canon = (ROOT / "event-feed.html").read_text()

# --- Verbatim blocks lifted from the canonical page ---
CSS_BASE = canon.split("<style>", 1)[1].split("</style>", 1)[0]
FOOTER = ("<!-- Footer (global element) -->"
          + canon.split("<!-- Footer (global element) -->", 1)[1].split("</footer>", 1)[0]
          + "</footer>")
SCRIPTS = "<script>" + canon.split("<script>", 1)[1].split("</script>", 1)[0] + "</script>"

CSS_EXTRA = """
    /* ---- Event Detail ---- */
    .ed-head { display: flex; gap: 10px; padding: 10px; align-items: flex-start; }
    .ed-thumb { width: 72px; height: 72px; flex: 0 0 72px; border: 1px solid #999; background: #d2d2d2;
      display: flex; align-items: center; justify-content: center; font-size: 8px; text-align: center; padding: 2px; }
    .ed-cat { font-size: 10px; text-transform: uppercase; letter-spacing: .04em; color: #555; }
    .ed-q { font-size: 16px; font-weight: bold; margin: 4px 0 6px; }
    .ed-prob-big { font-size: 13px; margin: 0; }
    .ed-prob-big .prob { font-weight: bold; border: 1px solid #999; background: #dcdcdc; padding: 1px 6px; font-size: 14px; }
    .ed-section { padding: 10px; border-top: 1px solid #ccc; }
    .ed-section h3 { font-size: 12px; text-transform: uppercase; letter-spacing: .04em; margin: 0 0 6px; }
    .chart-box { border: 1px dashed #999; background: #ededed; height: 120px; display: flex; align-items: center;
      justify-content: center; font-size: 11px; color: #555; text-align: center; padding: 6px; }
    .args { display: flex; flex-direction: column; gap: 12px; }
    .arg-col h4 { margin: 0 0 4px; font-size: 11px; }
    .arg-col ul { margin: 0; padding-left: 16px; font-size: 12px; }
    .arg-col li { margin-bottom: 4px; }
    .resolution { font-size: 12px; line-height: 1.5; }
    .opt-list { display: flex; flex-direction: column; }
    .preselect-note { border: 1px solid #999; background: #e0e0e0; padding: 6px 8px; font-size: 11px; margin: 0 10px 0; }
    .cta-bar { position: sticky; bottom: 0; background: #e2e2e2; border: 1px solid #999; padding: 8px 10px; display: flex; gap: 8px; }
    .cta-bar button { flex: 1; border: 1px solid #888; background: #d6d6d6; padding: 12px; font-size: 13px; font-weight: bold; cursor: pointer; }
    @media (min-width: 640px) { .args { flex-direction: row; } .arg-col { flex: 1; } }

    /* ---- Invoked overlays (Bet / Sign In / Deposit): modal on desktop, bottom sheet on mobile ---- */
    .backdrop { background: #cfcfcf; flex: 1; position: relative; min-height: 70vh; display: flex;
      align-items: flex-end; justify-content: center; }
    .dim-note { position: absolute; top: 8px; left: 8px; font-size: 10px; color: #555; background: #dcdcdc; border: 1px solid #aaa; padding: 2px 6px; }
    .sheet { width: 100%; background: #f0f0f0; border: 1px solid #999; border-bottom: none; }
    .grab { width: 36px; height: 4px; background: #bbb; border-radius: 2px; margin: 6px auto 0; }
    .sheet-head { display: flex; align-items: center; justify-content: space-between; padding: 8px 10px; border-bottom: 1px solid #ccc; }
    .sheet-head h2 { font-size: 14px; margin: 0; }
    .sheet-close { border: 1px solid #888; background: #d6d6d6; font-size: 12px; cursor: pointer; padding: 2px 8px; }
    .sheet-body { padding: 10px; display: flex; flex-direction: column; gap: 10px; }
    @media (min-width: 640px) { .backdrop { align-items: center; padding: 24px; } .sheet { max-width: 420px; border-bottom: 1px solid #999; } }

    .dir-pill { border: 1px solid #888; background: #dcdcdc; padding: 4px 10px; font-weight: bold; font-size: 12px; display: inline-block; }
    .field-label { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: #555; }
    .amount-row { display: flex; align-items: center; gap: 8px; }
    .amount-input { flex: 1; border: 1px solid #888; background: #fff; padding: 10px; font-size: 18px; }
    .quick { display: flex; gap: 6px; flex-wrap: wrap; }
    .quick button { border: 1px solid #888; background: #d6d6d6; padding: 6px 10px; font-size: 12px; cursor: pointer; }
    .quick button.sel { background: #b8b8b8; font-weight: bold; }
    .line { display: flex; justify-content: space-between; font-size: 12px; padding: 4px 0; border-top: 1px solid #ddd; }
    .line.total { font-weight: bold; border-top: 1px solid #999; }
    .inline-error { border: 1px solid #999; background: #e0e0e0; padding: 8px; font-size: 12px; }
    .reconcile-box { border: 1px solid #999; background: #e6e6e6; padding: 8px; font-size: 12px; display: flex; flex-direction: column; gap: 4px; }
    .confirm-btn { border: 1px solid #888; background: #c4c4c4; padding: 12px; font-size: 14px; font-weight: bold; cursor: pointer; width: 100%; }
    .provider-btn { display: flex; align-items: center; gap: 10px; border: 1px solid #888; background: #d6d6d6; padding: 12px; font-size: 13px; cursor: pointer; width: 100%; text-align: left; }
    .provider-btn .ic { width: 18px; height: 18px; }
    .spinner-box { border: 1px dashed #999; background: #ededed; padding: 24px; text-align: center; font-size: 12px; color: #555; }
    .fine { font-size: 11px; color: #555; line-height: 1.5; }
    .widget-box { border: 1px dashed #999; background: #ededed; min-height: 160px; display: flex; align-items: center;
      justify-content: center; font-size: 11px; color: #555; text-align: center; padding: 8px; }
    .protect { border: 1px solid #999; background: #e6e6e6; padding: 8px; font-size: 11px; }

    /* ---- Active Bets ---- */
    .tabs { display: flex; gap: 0; margin: 0 0 10px; }
    .tabs button { border: 1px solid #888; border-bottom: 1px solid #bbb; background: #dcdcdc; padding: 8px 14px; font-size: 12px; cursor: pointer; }
    .tabs button[aria-selected="true"] { background: #f4f4f4; font-weight: bold; border-bottom-color: #f4f4f4; }
    .pos-list { display: flex; flex-direction: column; gap: 8px; }
    .pos { border: 1px solid #bbb; background: #ededed; padding: 8px 10px; display: flex; flex-direction: column; gap: 6px; }
    .pos-top { display: flex; justify-content: space-between; gap: 8px; align-items: flex-start; }
    .pos-q { font-size: 13px; font-weight: bold; }
    .pos-side { font-size: 11px; border: 1px solid #999; background: #dcdcdc; padding: 1px 6px; height: max-content; white-space: nowrap; }
    .pos-figures { display: flex; gap: 16px; font-size: 10px; flex-wrap: wrap; color: #555; }
    .pos-fig b { display: block; font-size: 12px; color: #222; }
    .pos.skeleton .sk-line { height: 10px; background: #d8d8d8; margin: 6px 0; }
    .pos.skeleton .w70 { width: 70%; } .pos.skeleton .w40 { width: 40%; }
    .pos-status { font-size: 10px; text-transform: uppercase; letter-spacing: .03em; color: #555; }

    /* ---- Event Detail two-column: scrolling content + sticky bet panel ---- */
    .ed-layout { display: flex; flex-direction: column; }
    .ed-main { flex: 1; min-width: 0; }
    /* schematic probability chart (raised fidelity per design call: a drawn grey line, still no color) */
    .chart-wrap { padding: 0; }
    .chart-svg { width: 100%; height: 130px; display: block; border: 1px solid #bbb; background: #ededed; }
    .chart-svg polyline { fill: none; stroke: #777; stroke-width: 1.5; }
    .chart-svg .grid-l { stroke: #d2d2d2; stroke-width: 1; }
    .chart-svg .nowline { stroke: #999; stroke-width: 1; stroke-dasharray: 3 3; }
    .chart-svg text { fill: #777; font-size: 7px; }
    .chart-cap { font-size: 10px; color: #555; margin: 4px 0 0; display: flex; justify-content: space-between; }
    .ed-facts { display: flex; flex-wrap: wrap; gap: 16px; font-size: 10px; color: #555; padding: 8px 10px; border-top: 1px solid #ccc; }
    .ed-facts b { display: block; font-size: 12px; color: #222; }

    /* bet panel (desktop sticky sidebar) */
    .bet-panel { display: none; }
    .bet-panel .bp-inner { padding: 10px; display: flex; flex-direction: column; gap: 9px; }
    .bp-head { display: flex; align-items: center; justify-content: space-between; }
    .bp-head h3 { font-size: 13px; margin: 0; }
    .bp-hint { font-size: 10px; color: #555; }
    .bp-dir { display: flex; gap: 6px; }
    .bp-side { flex: 1; border: 1px solid #888; background: #d6d6d6; padding: 10px 6px; font-size: 12px; font-weight: bold; cursor: pointer; }
    .bp-side.sel { background: #b8b8b8; border-width: 2px; }
    .bp-side .bp-pct { display: block; font-size: 11px; font-weight: normal; }
    .bp-opts { display: flex; flex-direction: column; gap: 0; border: 1px solid #ccc; max-height: 168px; overflow: auto; }
    .bp-opt { display: flex; align-items: center; gap: 8px; padding: 7px 8px; border-top: 1px solid #ddd; font-size: 12px; cursor: pointer; }
    .bp-opt:first-child { border-top: none; }
    .bp-opt.sel { background: #dcdcdc; font-weight: bold; }
    .bp-opt .bp-opt-pct { margin-left: auto; border: 1px solid #999; background: #e0e0e0; padding: 0 5px; font-size: 11px; }

    /* mobile sticky bet dock (collapsed bar above the bottom nav; taps expand to a sheet) */
    .bet-dock { position: sticky; bottom: 52px; z-index: 4; background: #e2e2e2; border: 1px solid #999; border-bottom: none;
      display: flex; align-items: center; gap: 6px; padding: 8px; }
    .bet-dock .bp-side { padding: 11px 6px; }
    .bet-dock .dock-meta { font-size: 9px; color: #555; flex: 0 0 auto; text-align: center; }
    .bet-dock .dock-meta b { display: block; font-size: 12px; color: #222; }

    @media (min-width: 640px) {
      .ed-layout { flex-direction: row; align-items: flex-start; }
      .ed-main { border-right: 1px solid #999; }
      .bet-panel { display: block; flex: 0 0 300px; position: sticky; top: 8px; align-self: flex-start; }
      .bet-dock { display: none; }
    }

    /* ---- Category page: side sub-category panel + filtered feed ---- */
    .cat-layout { display: flex; flex-direction: column; gap: 0; }
    .cat-main { flex: 1; min-width: 0; }
    .subcat { background: #ededed; }
    .subcat .zone-tag { background: #d2d2d2; }
    .subcat-head { font-size: 10px; text-transform: uppercase; letter-spacing: .04em; color: #555; padding: 8px 10px 0; }
    .subcat ul { list-style: none; margin: 0; padding: 8px; display: flex; gap: 6px; overflow-x: auto; flex-wrap: nowrap; }
    .subcat li { flex: 0 0 auto; }
    .subcat button { border: 1px solid #888; background: #d6d6d6; padding: 5px 9px; font-size: 11px; cursor: pointer;
      white-space: nowrap; display: inline-flex; gap: 6px; align-items: center; }
    .subcat li[aria-current="page"] button { background: #b8b8b8; border-width: 2px; font-weight: bold; }
    .subcat .cnt { font-size: 9px; color: #555; border: 1px solid #bbb; background: #e8e8e8; padding: 0 4px; }
    @media (min-width: 640px) {
      .cat-layout { flex-direction: row; align-items: flex-start; }
      .subcat { flex: 0 0 210px; position: sticky; top: 8px; border: 1px solid #999; }
      .subcat ul { flex-direction: column; overflow: visible; flex-wrap: nowrap; }
      .subcat button { width: 100%; justify-content: space-between; }
    }
    /* Category grid adapts to the width left by the sub-category rail (no fixed 4-col overflow). */
    .cat-main .grid { grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }

    /* ---- Shared in-page dialogs (native <dialog>, opened over the current page) ---- */
    dialog.app-dialog { width: 92%; max-width: 420px; border: 1px solid #999; background: #f0f0f0; color: #222; padding: 0; }
    dialog.app-dialog::backdrop { background: rgba(0,0,0,.4); }
    dialog.app-dialog .sheet-body { padding: 10px; display: flex; flex-direction: column; gap: 10px; }
    .dlg-note { font-size: 10px; color: #555; padding: 6px 10px; border-top: 1px dashed #bbb; margin: 0; }

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


def style():
    return "<style>" + CSS_BASE + CSS_EXTRA + "  </style>"


# ---- Screen-tree nav (rebuilt identically on every page; current node marked) ----
# Each screen: (label, base_file, built?, auth_axis?, in_states, out_states/flat_states)
# states are (state_label, file) for built screens, or (state_label, None) for planned.

def _states_ul(states, cur_file, screen_built):
    out = ['        <ul class="wf-states">']
    for lbl, href in states:
        if href is None or not screen_built:
            out.append(f"          <li>{lbl}</li>")
        elif href == cur_file:
            out.append(f'          <li class="cur"><a href="{href}">{lbl} (this page)</a></li>')
        else:
            out.append(f'          <li><a href="{href}">{lbl}</a></li>')
    out.append("        </ul>")
    return "\n".join(out)


def _states_ul_auth(in_states, out_states, cur_file, screen_built):
    out = ['        <ul class="wf-states">', '          <li class="wf-substate">Logged in</li>']

    def emit(lbl, href):
        if href is None or not screen_built:
            return f"          <li>{lbl}</li>"
        if href == cur_file:
            return f'          <li class="cur"><a href="{href}">{lbl} (this page)</a></li>'
        return f'          <li><a href="{href}">{lbl}</a></li>'

    for lbl, href in in_states:
        out.append(emit(lbl, href))
    out.append('          <li class="wf-substate">Logged out</li>')
    for lbl, href in out_states:
        out.append(emit(lbl, href))
    out.append("        </ul>")
    return "\n".join(out)


# Built screens this step:
ED_IN = [("success / binary", "event-detail.html"), ("success / multi-outcome", "event-detail-multi.html"),
         ("error", "event-detail-error.html"), ("loading", "event-detail-loading.html"),
         ("resolved-while-reading", "event-detail-resolved.html"),
         ("bet panel: insufficient-balance", "event-detail-bet-insufficient.html"),
         ("bet panel: S5 reconcile", "event-detail-bet-reconcile.html"),
         ("bet panel: processing", "event-detail-bet-processing.html"),
         ("bet panel: on-chain error", "event-detail-bet-error.html")]
ED_OUT = [("success / binary", "event-detail-logged-out.html"), ("success / multi-outcome", "event-detail-logged-out-multi.html"),
          ("error", "event-detail-logged-out-error.html"), ("loading", "event-detail-logged-out-loading.html")]
EF_IN = [("success", "event-feed.html"), ("empty", "event-feed-empty.html"), ("error", "event-feed-error.html"),
         ("loading", "event-feed-loading.html"), ("push-permission-missing", "event-feed-push-permission-missing.html")]
EF_OUT = [("success", "event-feed-logged-out.html"), ("empty", "event-feed-logged-out-empty.html"),
          ("error", "event-feed-logged-out-error.html"), ("loading", "event-feed-logged-out-loading.html")]
SI_STATES = [("success / form", "sign-in.html"), ("error (auth failed)", "sign-in-error.html"),
             ("loading (OAuth in-progress)", "sign-in-loading.html"), ("provider-conflict", "sign-in-provider-conflict.html")]
DEP_STATES = [("success / form", "deposit.html"), ("error-card (declined)", "deposit-error-card.html"),
              ("error-KYC (rejected)", "deposit-error-kyc.html"), ("widget-load-failure", "deposit-widget-load-failure.html"),
              ("loading (widget in-progress)", "deposit-loading.html"), ("pending (under review)", "deposit-pending.html"),
              ("minimum-not-met", "deposit-minimum-not-met.html")]
BET_STATES = [("intent (base, logged out)", "bet-screen.html"), ("S5-reconcile (price moved)", "bet-screen-reconcile.html"),
              ("insufficient-balance", "bet-screen-insufficient-balance.html"), ("event-closed", "bet-screen-event-closed.html"),
              ("error (on-chain, T3)", "bet-screen-error.html"), ("execute processing", "bet-screen-processing.html")]
AB_STATES = [("success (open positions)", "active-bets.html"), ("empty-new", "active-bets-empty-new.html"),
             ("empty-resolved", "active-bets-empty-resolved.html"), ("error", "active-bets-error.html"),
             ("loading", "active-bets-loading.html")]
WIN_STATES = [("success", "win.html"), ("loading (share card)", "win-loading.html"),
              ("error (card not generated, T11)", "win-error.html"),
              ("payout-pending", "win-payout-pending.html")]
LOSS_STATES = [("success", "loss.html"), ("loading", "loss-loading.html")]
NOTIF_STATES = [("success", "notifications.html"), ("empty", "notifications-empty.html"),
                ("error", "notifications-error.html"), ("loading", "notifications-loading.html"),
                ("push-permission-missing", "notifications-push.html")]
WALLET_STATES = [("success", "wallet.html"), ("loading", "wallet-loading.html"),
                 ("error", "wallet-error.html")]
MYPROFILE_STATES = [("success", "my-profile.html"), ("loading", "my-profile-loading.html"),
                    ("error", "my-profile-error.html")]
# Saved view (Favorites target). Logged-in only - a filter over the feed, built as
# its own page so the Favorites control (header heart + bottom slot) has a destination.
SAVED_STATES = [("success", "saved.html"), ("empty", "saved-empty.html"),
                ("loading", "saved-loading.html")]
PUBPROFILE_STATES = [("success", "public-profile.html"), ("loading", "public-profile-loading.html"),
                     ("error", "public-profile-error.html"),
                     ("not-found / link-expired", "public-profile-not-found.html")]
HISTORY_STATES = [("success", "active-bets-history.html"), ("empty", "active-bets-history-empty.html"),
                  ("error", "active-bets-history-error.html"), ("loading", "active-bets-history-loading.html")]
HIW_STATES = [("success (static trust page)", "how-it-works.html")]


# My Bets tabs (Active = open positions / Active Bets; History = resolved bets / Bet History).
# Shared so both screens render identical, linked tabs. active in {"active","history"}.
def tabs(active="active"):
    a_cur = ' aria-selected="true"' if active == "active" else ' aria-selected="false"'
    h_cur = ' aria-selected="true"' if active == "history" else ' aria-selected="false"'
    return ('        <div class="tabs" role="tablist" aria-label="My Bets">\n'
            f'          <a href="active-bets.html"><button type="button" role="tab"{a_cur}>Active</button></a>\n'
            f'          <a href="active-bets-history.html"><button type="button" role="tab"{h_cur}>History</button></a>\n'
            '        </div>\n')


def cat_state_files(stem):
    """Category auth x state file lists for the screen tree / switchers."""
    inn = [("success", f"{stem}.html"), ("empty", f"{stem}-empty.html"),
           ("error", f"{stem}-error.html"), ("loading", f"{stem}-loading.html")]
    out = [("success", f"{stem}-logged-out.html"), ("empty", f"{stem}-logged-out-empty.html"),
           ("error", f"{stem}-logged-out-error.html"), ("loading", f"{stem}-logged-out-loading.html")]
    return inn, out


def nav_tree(cur_file):
    L = []
    a = L.append
    a('  <nav class="wf-nav" id="wfNav" aria-label="Wireframe screens">')
    a('    <div class="wf-nav-head">')
    a('      Wireframes - screen tree')
    a('      <button type="button" class="wf-nav-close" id="wfClose" aria-label="Close screen tree">x</button>')
    a('    </div>')
    a('    <ul class="wf-tree">')

    def screen(label, base, built, cur_file, axis=None, instates=None, outstates=None, flat=None):
        active = "active" if (built and base == cur_file_screen_base(cur_file, base, flat, instates, outstates)) else ""
        is_cur_screen = built and _file_in(cur_file, flat, instates, outstates)
        cls = "active" if is_cur_screen else ("planned" if not built else "")
        attr = f' class="{cls}"' if cls else ""
        aria = ' aria-current="page"' if is_cur_screen else ""
        a('      <li class="wf-screen">')
        a(f'        <a href="{base}"{attr}{aria}>{label}</a>')
        if axis:
            a(_states_ul_auth(instates, outstates, cur_file, built))
        else:
            a(_states_ul(flat, cur_file, built))
        a('      </li>')

    a('      <li class="wf-sec">Events</li>')
    screen("Event Feed", "event-feed.html", True, cur_file, axis=True, instates=EF_IN, outstates=EF_OUT)
    screen("Event Detail", "event-detail.html", True, cur_file, axis=True, instates=ED_IN, outstates=ED_OUT)
    a('      <li class="wf-note">Bet intent + states (reconcile, insufficient-balance, event-closed, processing, on-chain error) now live in the Event Detail bet panel - states to come (the standalone Bet modal was removed).</li>')
    screen("Saved (Favorites)", "saved.html", True, cur_file, flat=SAVED_STATES)
    a('      <li class="wf-note">Saved view - a filter over the feed (logged-in only); the Favorites control opens it.</li>')

    a('      <li class="wf-sec">Category pages (second-level nav -> own page)</li>')
    for _cn, _stem in (("Politics", "politics"), ("Crypto", "crypto"), ("Culture", "culture"), ("General", "general")):
        _in, _out = cat_state_files(_stem)
        screen(_cn, _stem + ".html", True, cur_file, axis=True, instates=_in, outstates=_out)

    a('      <li class="wf-sec">Activation gate</li>')
    screen("Sign In / Register", "sign-in.html", True, cur_file, flat=SI_STATES)
    screen("Deposit", "deposit.html", True, cur_file, flat=DEP_STATES)

    a('      <li class="wf-sec">Resolution</li>')
    screen("Win Screen", "win.html", True, cur_file, flat=WIN_STATES)
    screen("Loss Screen", "loss.html", True, cur_file, flat=LOSS_STATES)

    a('      <li class="wf-sec">My Bets</li>')
    screen("Active Bets", "active-bets.html", True, cur_file, flat=AB_STATES)
    screen("Bet History (History tab)", "active-bets-history.html", True, cur_file, flat=HISTORY_STATES)

    a('      <li class="wf-sec">Notifications</li>')
    screen("Notifications", "notifications.html", True, cur_file, flat=NOTIF_STATES)

    a('      <li class="wf-sec">Wallet</li>')
    screen("Wallet", "wallet.html", True, cur_file, flat=WALLET_STATES)
    a('      <li class="wf-note">Withdrawal is a flow inside Wallet (amount -&gt; USDC address -&gt; confirm; pending / confirmed / failed), not a separate screen.</li>')

    a('      <li class="wf-sec">Profile</li>')
    screen("My Profile", "my-profile.html", True, cur_file, flat=MYPROFILE_STATES)
    screen("Public Profile", "public-profile.html", True, cur_file, flat=PUBPROFILE_STATES)

    a('      <li class="wf-sec">How It Works</li>')
    screen("How It Works", "how-it-works.html", True, cur_file, flat=HIW_STATES)

    a('      <li class="wf-sec">Orphans [SIROTA] - not built (no confirmed job)</li>')
    a('      <li class="wf-note">Settings / Notification Preferences, Leaderboard, Help / FAQ.</li>')

    a('    </ul>')
    a('  </nav>')
    return "\n".join(L)


def _file_in(cur_file, flat, instates, outstates):
    files = []
    for grp in (flat, instates, outstates):
        if grp:
            files += [h for _, h in grp if h]
    return cur_file in files


def cur_file_screen_base(*_):  # unused helper kept for clarity
    return None


WF_HEAD = """  <!-- ===== Wireframe screen-tree nav (meta navigation, identical on every wireframe page) ===== -->
  <button type="button" class="wf-toggle" id="wfToggle" aria-label="Open screen tree" aria-expanded="false">
    <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    Screens
  </button>
  <div class="wf-overlay" id="wfOverlay"></div>
"""

# ---- Headers ----
HEADER_IN_OPEN = """    <!-- Header (lean: logo = Events/home, right icon cluster) -->
    <header class="app-header">
      <span class="zone-tag">zone: header (lean, same at all widths; logo = Events home)</span>
      <div class="row">
        <div class="left">
          <button type="button" class="icon-btn" aria-label="Menu (reserved for future scaling)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          </button>
          <button type="button" class="logo-btn" aria-label="Predict Market - go to Events home">Predict Market</button>
        </div>
        <div class="utility">
          <div class="bal-toggle desk-only">
            <span class="bal-figure"><span class="bal-label" id="balLabel">Portfolio</span> <span class="bal-amt" id="balAmt">$142.00</span></span>
            <button type="button" class="icon-btn bal-swap" id="balSwap" aria-label="Swap balance (showing Portfolio)">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h12l-3-3M17 17H5l3 3"/></svg>
            </button>
            <button type="button" class="icon-btn bal-add" data-open="deposit" aria-label="Add funds">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
          </div>
          <button type="button" class="icon-btn desk-only" aria-label="Favorites">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          </button>
          <details class="notif-menu">
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
          </details>
          <details class="avatar-menu">
            <summary aria-label="Account menu">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>
              <svg class="ic-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
            </summary>
            <div class="dropdown" role="menu">
              <span class="zone-tag">avatar dropdown (collapsed by default, click to open)</span>
              <ul>
                <li><button type="button" role="menuitem">My Profile</button></li>
                <li><button type="button" role="menuitem">My Bets</button></li>
                <li><button type="button" role="menuitem">Wallet / Deposit</button></li>
                <li><button type="button" role="menuitem">How It Works</button></li>
                <li><button type="button" role="menuitem">Logout</button></li>
              </ul>
            </div>
          </details>
        </div>
      </div>
    </header>
"""

HEADER_OUT_OPEN = """    <!-- Header (logged-out: no account; Log in / Sign up replace balance and avatar) -->
    <header class="app-header">
      <span class="zone-tag">zone: header (logged-out: no account; Log in / Sign up replace balance and avatar)</span>
      <div class="row">
        <div class="left">
          <button type="button" class="icon-btn" aria-label="Menu (reserved for future scaling)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          </button>
          <button type="button" class="logo-btn" aria-label="Predict Market - go to Events home">Predict Market</button>
        </div>
        <div class="utility">
          <button type="button" class="icon-btn desk-only" data-open="signin" aria-label="Favorites (sign in to save)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          </button>
          <button type="button" class="icon-btn" data-open="signin" aria-label="Notifications (sign in)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
          </button>
          <div class="auth-btns">
            <button type="button" class="auth-btn" data-open="signin">Log in</button>
            <button type="button" class="auth-btn primary" data-open="signin">Sign up</button>
          </div>
        </div>
      </div>
    </header>
"""

CAT_NAV = """    <!-- Second-level navigation: categories -->
    <nav class="cat-nav" aria-label="Categories (second level)">
      <span class="zone-tag">zone: second-level navigation (categories)</span>
      <ul>
        <li aria-current="page"><button type="button">Trending</button></li>
        <li><button type="button">Politics</button></li>
        <li><button type="button">Crypto</button></li>
        <li><button type="button">Culture</button></li>
        <li><button type="button">General</button></li>
      </ul>
    </nav>
"""

# Category second-level nav as real links to their own pages. active in
# {"Trending","Politics","Crypto","Culture","General"}; zone note overridable.
CAT_FILES = {"Trending": "event-feed.html", "Politics": "politics.html", "Crypto": "crypto.html",
             "Culture": "culture.html", "General": "general.html"}


def cat_nav(active="Trending", note="zone: second-level navigation (each category opens its own page)"):
    lis = []
    for name in ("Trending", "Politics", "Crypto", "Culture", "General"):
        cur = ' aria-current="page"' if name == active else ""
        lis.append(f'        <li{cur}><a href="{CAT_FILES[name]}"><button type="button">{name}</button></a></li>')
    return ('    <!-- Second-level navigation: categories route to their own pages (links) -->\n'
            '    <nav class="cat-nav" aria-label="Categories (second level)">\n'
            f'      <span class="zone-tag">{note}</span>\n'
            '      <ul>\n' + "\n".join(lis) + '\n      </ul>\n'
            '    </nav>\n')

# Bottom nav. active in {"events","mybets","fav","portfolio"}.
def bottom_in(active="events"):
    def cur(slot):
        return ' aria-current="page"' if slot == active else ""
    return f"""    <!-- Bottom navigation (mobile only) -->
    <nav class="bottom-nav" aria-label="Primary (mobile)">
      <span class="zone-tag">zone: bottom nav (mobile only, icons; slot 4 = Portfolio with balance)</span>
      <ul>
        <li{cur('events')}><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg>
          <span>Events</span>
        </button></li>
        <li{cur('mybets')}><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h10"/></svg>
          <span>My Bets</span>
        </button></li>
        <li{cur('fav')}><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          <span>Favorites</span>
        </button></li>
        <li{cur('portfolio')}><button type="button" aria-label="Portfolio, balance $142">
          <span class="bn-bal">$142</span>
          <span>Portfolio</span>
        </button></li>
      </ul>
    </nav>
"""

def bottom_out(active="events"):
    # active in {"events","none"}: "none" marks no slot current (public pages
    # reached out of the bottom-nav context, e.g. Public Profile / How It Works).
    ev = ' aria-current="page"' if active == "events" else ""
    return f"""    <!-- Bottom navigation (mobile only, logged-out: slot 4 = Sign in) -->
    <nav class="bottom-nav" aria-label="Primary (mobile)">
      <span class="zone-tag">zone: bottom nav (mobile only; logged-out slot 4 = Sign in)</span>
      <ul>
        <li{ev}><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg>
          <span>Events</span>
        </button></li>
        <li><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h10"/></svg>
          <span>My Bets</span>
        </button></li>
        <li><button type="button">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          <span>Favorites</span>
        </button></li>
        <li><button type="button" data-open="signin" aria-label="Sign in">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 17l5-5-5-5M15 12H3M14 4h5v16h-5"/></svg>
          <span>Sign in</span>
        </button></li>
      </ul>
    </nav>
"""


# ---- Shared in-page dialogs: defined once, emitted on every page, opened over
# the current screen (close stays on the page). Deep states keep their reference
# pages (sign-in-*.html / deposit-*.html). ----
SIGNIN_DIALOG = """  <dialog id="signinDialog" class="app-dialog" aria-label="Sign in or create account">
    <div class="sheet-head">
      <h2>Sign in or create account</h2>
      <button type="button" class="sheet-close" data-close-dialog aria-label="Close">x</button>
    </div>
    <div class="sheet-body">
      <p class="fine">You are about to place a bet. Sign in or create an account to continue. No crypto wallet required.</p>
      <button type="button" class="provider-btn" data-flow="signin-to-deposit">
        <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/></svg>
        Continue with Google
      </button>
      <button type="button" class="provider-btn" data-flow="signin-to-deposit">
        <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
        Continue with X
      </button>
      <button type="button" class="provider-btn" data-flow="signin-to-deposit">
        <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7c1-2 3-3 4-3 0 2-1 3-2 4M9 9c-2 0-4 2-4 5s2 6 4 6c1 0 1.5-.5 3-.5s2 .5 3 .5c1.5 0 3-2 3-4-2-1-2-4 0-5-1-1.5-3-1.5-4-1.5S11 9 9 9z"/></svg>
        Continue with Apple
      </button>
      <p class="fine">By continuing you agree to the <a href="#">Terms</a> and <a href="#">Privacy Policy</a>.</p>
    </div>
    <p class="dlg-note">Opens over the current page; closing keeps you here. Error / loading / provider-conflict: see reference pages sign-in-*.html.</p>
  </dialog>
"""

DEPOSIT_DIALOG = """  <dialog id="depositDialog" class="app-dialog" aria-label="Add funds">
    <div class="sheet-head">
      <h2>Add funds</h2>
      <button type="button" class="sheet-close" data-close-dialog aria-label="Close">x</button>
    </div>
    <div class="sheet-body">
      <div>
        <span class="field-label">Amount to add</span>
        <div class="amount-row"><span class="amount-input">$20.00</span></div>
        <div class="quick"><button type="button">$10</button><button type="button" class="sel">$20</button><button type="button">$50</button><button type="button">$100</button></div>
      </div>
      <div class="widget-box">Transak payment widget (card to USDC)</div>
      <p class="protect">Your USDC is held 1:1 - we do not lend or invest deposited funds.</p>
      <p class="fine">Minimum deposit $10. KYC is required for card deposits; crypto-only users can connect a USDC wallet instead.</p>
      <button type="button" class="confirm-btn" data-close-dialog>Add funds</button>
    </div>
    <p class="dlg-note">Opens over the current page after sign-in. States (card declined / KYC / widget fail / pending / minimum): see reference pages deposit-*.html.</p>
  </dialog>
"""

DIALOG_JS = """  <script>
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
  </script>
"""


def head(title):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            '  <meta charset="UTF-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'  <title>{title}</title>\n'
            + style() + "\n</head>\n<body>\n")


def page_label(screen, authstate, file_name):
    return (f'  <div class="page-label">\n'
            f'    <strong>Wireframe:</strong> {screen} &nbsp;|&nbsp;\n'
            f'    {authstate} &nbsp;|&nbsp;\n'
            f'    responsive (mobile-first) &nbsp;|&nbsp;\n'
            f'    file: wireframes/{file_name}\n'
            f'  </div>\n')


def assemble(title, cur_file, screen, authstate, switcher, device_inner, side_inner):
    return (head(title)
            + WF_HEAD
            + nav_tree(cur_file) + "\n\n"
            + page_label(screen, authstate, cur_file)
            + "\n" + switcher + "\n\n"
            + '  <div class="device">\n' + device_inner + '\n  </div>\n\n'
            + '  <div class="side">\n' + side_inner + '\n  </div>\n\n'
            + "  " + SCRIPTS + "\n\n"
            + SIGNIN_DIALOG + "\n" + DEPOSIT_DIALOG + "\n" + DIALOG_JS + "\n"
            + "</body>\n</html>\n")


def write(file_name, html):
    (ROOT / file_name).write_text(html)
    # guard: no em dash
    assert "—" not in html, f"em dash in {file_name}"
    return file_name
