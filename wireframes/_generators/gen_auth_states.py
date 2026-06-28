#!/usr/bin/env python3
import os

WF = "/Users/sergiyshevchenko/Claud Projects/Project One/wireframes"
with open(os.path.join(WF, "event-feed.html"), encoding="utf-8") as f:
    src = f.read()

def must_replace(s, old, new, tag):
    assert old in s, "MISSING for %s:\n%r" % (tag, old[:120])
    return s.replace(old, new, 1)

# ---------- exact blocks captured from the current file ----------
LOGGED_IN_HEADER = '''    <header class="app-header">
      <span class="zone-tag">zone: header (lean, same at all widths; logo = Events home)</span>
      <div class="row">
        <div class="left">
          <button type="button" class="icon-btn" aria-label="Menu (reserved for future scaling)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          </button>
          <button type="button" class="logo-btn" aria-label="Predict Market - go to Events home">Predict Market</button>
        </div>

        <div class="utility">
          <!-- Balance: one figure + swap icon (Portfolio <-> Cash). Desktop only. -->
          <div class="bal-toggle desk-only">
            <span class="bal-figure"><span class="bal-label" id="balLabel">Portfolio</span> <span class="bal-amt" id="balAmt">$142.00</span></span>
            <button type="button" class="icon-btn bal-swap" id="balSwap" aria-label="Swap balance (showing Portfolio)">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h12l-3-3M17 17H5l3 3"/></svg>
            </button>
          </div>

          <!-- Favorites: desktop header only (on mobile it is the bottom-bar slot). -->
          <button type="button" class="icon-btn desk-only" aria-label="Favorites">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          </button>

          <!-- Notifications bell: header on both breakpoints (badge = retention anchor). -->
          <span class="bell-wrap">
            <button type="button" class="icon-btn" aria-label="Notifications, 3 unread">
              <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
            </button>
            <span class="badge-dot">3</span>
          </span>

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
    </header>'''

LOGGED_OUT_HEADER = '''    <header class="app-header">
      <span class="zone-tag">zone: header (logged-out: no account; Log in / Sign up replace balance and avatar)</span>
      <div class="row">
        <div class="left">
          <button type="button" class="icon-btn" aria-label="Menu (reserved for future scaling)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          </button>
          <button type="button" class="logo-btn" aria-label="Predict Market - go to Events home">Predict Market</button>
        </div>

        <div class="utility">
          <!-- Favorites kept as an affordance; tapping it logged-out routes to Sign In (saving needs an account). -->
          <button type="button" class="icon-btn desk-only" aria-label="Favorites (sign in to save)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"/></svg>
          </button>

          <!-- Notifications kept as an affordance; tapping it logged-out routes to Sign In. No unread badge when logged out. -->
          <button type="button" class="icon-btn" aria-label="Notifications (sign in)">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
          </button>

          <!-- Auth entries replace the balance figure and the avatar dropdown entirely. -->
          <div class="auth-btns">
            <button type="button" class="auth-btn">Log in</button>
            <button type="button" class="auth-btn primary">Sign up</button>
          </div>
        </div>
      </div>
    </header>'''

LOGGED_IN_BNAV = '''<li><button type="button" aria-label="Portfolio, balance $142">
          <span class="bn-bal">$142</span>
          <span>Portfolio</span>
        </button></li>'''

LOGGED_OUT_BNAV = '''<li><button type="button" aria-label="Sign in">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 12h10M16 8l4 4-4 4M14 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8"/></svg>
          <span>Sign in</span>
        </button></li>'''

OLD_SWITCH_NAV = '''  <nav class="state-switch" aria-label="States of this screen">
    <span class="ss-label">Event Feed states</span>
    <a href="event-feed.html" aria-current="page">Success</a>
    <a href="event-feed-empty.html">Empty</a>
    <a href="event-feed-error.html">Error</a>
    <a href="event-feed-loading.html">Loading</a>
    <a href="event-feed-push-permission-missing.html">Push denied</a>
  </nav>'''

OLD_TREE_EF = '''      <li class="wf-screen">
        <a href="event-feed.html" class="active" aria-current="page">Event Feed</a>
        <ul class="wf-states">
          <li class="cur"><a href="event-feed.html">success - logged in (this page)</a></li>
          <li><a href="event-feed.html#logged-out">success - logged out (header delta)</a></li>
          <li><a href="event-feed-empty.html">empty</a></li>
          <li><a href="event-feed-error.html">error</a></li>
          <li><a href="event-feed-loading.html">loading</a></li>
          <li><a href="event-feed-push-permission-missing.html">push-permission-missing</a></li>
        </ul>
      </li>'''

OLD_SWITCH_CSS = '''    .state-switch { border: 1px dashed #888; background: #e3e3e3; padding: 6px 10px; font-size: 11px;
      display: flex; flex-wrap: wrap; align-items: center; gap: 6px; }
    .state-switch .ss-label { text-transform: uppercase; letter-spacing: .05em; color: #555; font-size: 10px; margin-right: 2px; }
    .state-switch a { color: #222; text-decoration: none; border: 1px solid #999; background: #d6d6d6; padding: 2px 8px; }
    .state-switch a:hover { background: #cccccc; }
    .state-switch a[aria-current="page"] { background: #bdbdbd; font-weight: bold; }'''

NEW_SWITCH_CSS = '''    .state-switch { border: 1px dashed #888; background: #e3e3e3; padding: 7px 10px; font-size: 11px;
      display: flex; flex-direction: column; gap: 5px; }
    .state-switch .ss-row { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; }
    .state-switch .ss-label { text-transform: uppercase; letter-spacing: .05em; color: #555; font-size: 10px; width: 44px; flex: 0 0 44px; }
    .state-switch a { color: #222; text-decoration: none; border: 1px solid #999; background: #d6d6d6; padding: 2px 8px; }
    .state-switch a:hover { background: #cccccc; }
    .state-switch a[aria-current="page"] { background: #bdbdbd; font-weight: bold; }
    .auth-btns { display: flex; gap: 6px; }
    .auth-btn { border: 1px solid #888; background: #d6d6d6; padding: 6px 10px; font-size: 12px; cursor: pointer; }
    .auth-btn.primary { background: #c4c4c4; font-weight: bold; }
    .wf-states .wf-substate { padding: 7px 12px 2px 20px; color: #555; font-size: 10px; text-transform: uppercase; letter-spacing: .05em; font-weight: bold; }
    .wf-states .wf-substate::before { display: none; }'''

# ---------- body blocks ----------
grid_start = src.index('        <div class="grid">')
tail_marker = '\n      </div>\n    </main>'
tail_idx = src.index(tail_marker, grid_start)
SUCCESS_BODY = src[grid_start:tail_idx]  # original 8-card grid

EMPTY_BODY = '''        <div class="state-block" role="status" aria-live="polite">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>
          <p class="state-title">No events match your filters</p>
          <p class="state-msg">There are no markets for this category and filter combination right now. Try clearing the filters, or get notified when a new event shows up here.</p>
          <div class="state-actions">
            <button type="button" class="state-btn primary">Clear filters</button>
            <button type="button" class="state-btn">Notify me of new events in this category</button>
          </div>
        </div>'''

ERROR_BODY = '''        <div class="state-block" role="alert">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l9 16H3z"/><path d="M12 10v4"/><path d="M12 17h.01"/></svg>
          <p class="state-title">Couldn't load events</p>
          <p class="state-msg">Something went wrong reaching the network. Check your connection and try again.</p>
          <div class="state-actions">
            <button type="button" class="state-btn primary">Try again</button>
          </div>
        </div>'''

skel_card = '''          <article class="card skeleton" aria-hidden="true">
            <div class="card-body">
              <div class="top">
                <span class="sk-thumb"></span>
                <span class="sk-head"><span class="sk-line w80"></span><span class="sk-line w60"></span></span>
              </div>
              <span class="sk-line w40"></span>
              <div class="sk-row"><span class="sk-btn"></span><span class="sk-btn"></span></div>
              <span class="sk-line w60"></span>
            </div>
          </article>'''
LOADING_BODY = '        <div class="grid" aria-busy="true">\n\n' + "\n\n".join([skel_card]*6) + "\n\n        </div>"

PUSH_BANNER = '''        <div class="push-banner" role="region" aria-label="Notifications permission">
          <span class="push-msg">
            <svg class="ic" viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>
            Enable notifications to get live updates on the events you follow.
          </span>
          <span class="push-actions">
            <button type="button" class="state-btn primary">Enable notifications</button>
            <button type="button" class="state-btn">Not now</button>
          </span>
        </div>'''
PUSH_BODY = PUSH_BANNER + "\n\n" + SUCCESS_BODY

BODY = {"success": SUCCESS_BODY, "empty": EMPTY_BODY, "error": ERROR_BODY,
        "loading": LOADING_BODY, "push": PUSH_BODY}

# ---------- file map / labels ----------
def fname(auth, state):
    if auth == "in":
        return {"success": "event-feed.html", "empty": "event-feed-empty.html",
                "error": "event-feed-error.html", "loading": "event-feed-loading.html",
                "push": "event-feed-push-permission-missing.html"}[state]
    return {"success": "event-feed-logged-out.html", "empty": "event-feed-logged-out-empty.html",
            "error": "event-feed-logged-out-error.html", "loading": "event-feed-logged-out-loading.html"}[state]

IN_STATES = ["success", "empty", "error", "loading", "push"]
OUT_STATES = ["success", "empty", "error", "loading"]
SW_NAME = {"success": "Success", "empty": "Empty", "error": "Error", "loading": "Loading", "push": "Push denied"}
TREE_NAME = {"success": "success", "empty": "empty", "error": "error", "loading": "loading", "push": "push-permission-missing"}
LBL = {"success": "success", "empty": "empty (no events match filters)",
       "error": "error (load failure)", "loading": "loading (initial fetch)",
       "push": "push-permission-missing (banner)"}

def a_attr(is_cur):
    return ' aria-current="page"' if is_cur else ''

def build_switcher(auth, state):
    # Auth row: link to the same state in the other variant (fall back to success if missing)
    in_href = fname("in", state)
    out_href = fname("out", state) if state in OUT_STATES else fname("out", "success")
    rows = []
    rows.append('    <div class="ss-row"><span class="ss-label">Auth</span>'
                + '<a href="%s"%s>Logged in</a>' % (in_href, a_attr(auth == "in"))
                + '<a href="%s"%s>Logged out</a></div>' % (out_href, a_attr(auth == "out")))
    states = IN_STATES if auth == "in" else OUT_STATES
    links = "".join('<a href="%s"%s>%s</a>' % (fname(auth, s), a_attr(s == state), SW_NAME[s]) for s in states)
    rows.append('    <div class="ss-row"><span class="ss-label">State</span>' + links + '</div>')
    return '  <nav class="state-switch" aria-label="States of this screen (auth and screen state)">\n' + "\n".join(rows) + '\n  </nav>'

def build_tree(auth, state):
    def states_block(a, slist):
        out = ['          <li class="wf-substate">%s</li>' % ("Logged in" if a == "in" else "Logged out")]
        for s in slist:
            cur = (a == auth and s == state)
            cls = ' class="cur"' if cur else ''
            suffix = ' (this page)' if cur else ''
            out.append('          <li%s><a href="%s">%s%s</a></li>' % (cls, fname(a, s), TREE_NAME[s], suffix))
        return "\n".join(out)
    return ('      <li class="wf-screen">\n'
            '        <a href="event-feed.html" class="active" aria-current="page">Event Feed</a>\n'
            '        <ul class="wf-states">\n'
            + states_block("in", IN_STATES) + "\n"
            + states_block("out", OUT_STATES) + "\n"
            '        </ul>\n'
            '      </li>')

# ---------- build template (shared edits) ----------
tpl = src
tpl = must_replace(tpl, OLD_SWITCH_CSS, NEW_SWITCH_CSS, "switch CSS")
tpl = must_replace(tpl, LOGGED_IN_HEADER, "__HEADER__", "header")
tpl = must_replace(tpl, LOGGED_IN_BNAV, "__BNAV__", "bnav slot")
tpl = must_replace(tpl, OLD_SWITCH_NAV, "__SWITCHER__", "switcher nav")
tpl = must_replace(tpl, OLD_TREE_EF, "__TREE__", "tree EF node")
# body
g0 = tpl.index('        <div class="grid">'); t0 = tpl.index(tail_marker, g0)
tpl = tpl[:g0] + "__BODY__" + tpl[t0:]
# page-label
tpl = must_replace(tpl, "base state: success (registered)", "__LABEL__", "label")
tpl = must_replace(tpl, "file: wireframes/event-feed.html", "file: wireframes/__FILE__", "file")
# remove delta block
d0 = tpl.index('  <!-- ============ LOGGED-OUT HEADER DELTA')
a0 = tpl.index('  <!-- ============ ANNOTATIONS + NAV TREE')
tpl = tpl[:d0] + tpl[a0:]

assert "__HEADER__" in tpl and "__BNAV__" in tpl and "__SWITCHER__" in tpl and "__TREE__" in tpl and "__BODY__" in tpl

# ---------- emit pages ----------
combos = [("in", s) for s in IN_STATES] + [("out", s) for s in OUT_STATES]
for auth, state in combos:
    page = tpl
    page = page.replace("__HEADER__", LOGGED_IN_HEADER if auth == "in" else LOGGED_OUT_HEADER)
    page = page.replace("__BNAV__", LOGGED_IN_BNAV if auth == "in" else LOGGED_OUT_BNAV)
    page = page.replace("__SWITCHER__", build_switcher(auth, state))
    page = page.replace("__TREE__", build_tree(auth, state))
    page = page.replace("__BODY__", BODY[state])
    auth_lbl = "logged in" if auth == "in" else "logged out"
    page = page.replace("__LABEL__", "%s - state: %s" % (auth_lbl, LBL[state]))
    fn = fname(auth, state)
    page = page.replace("__FILE__", fn)
    with open(os.path.join(WF, fn), "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote %-42s auth=%-3s state=%-8s em-dash=%d" % (fn, auth, state, page.count("—")))

print("done:", len(combos), "pages")
