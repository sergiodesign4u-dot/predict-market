#!/usr/bin/env python3
import os

BASE_DIR = "/Users/sergiyshevchenko/Claud Projects/Project One/wireframes"
base_path = os.path.join(BASE_DIR, "event-feed.html")
with open(base_path, encoding="utf-8") as f:
    base = f.read()

# --- locate the success grid block ---
grid_start = base.index('        <div class="grid">')
tail_marker = '\n      </div>\n    </main>'
tail_idx = base.index(tail_marker, grid_start)
original_grid = base[grid_start:tail_idx]  # includes grid's own closing </div>

# --- state main contents ---
EMPTY_MAIN = '''        <div class="state-block" role="status" aria-live="polite">
          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>
          <p class="state-title">No events match your filters</p>
          <p class="state-msg">There are no markets for this category and filter combination right now. Try clearing the filters, or get notified when a new event shows up here.</p>
          <div class="state-actions">
            <button type="button" class="state-btn primary">Clear filters</button>
            <button type="button" class="state-btn">Notify me of new events in this category</button>
          </div>
        </div>'''

ERROR_MAIN = '''        <div class="state-block" role="alert">
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
LOADING_MAIN = '        <div class="grid" aria-busy="true">\n\n' + "\n\n".join([skel_card]*6) + "\n\n        </div>"

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
PUSH_MAIN = PUSH_BANNER + "\n\n" + original_grid

states = [
    dict(file="event-feed-empty.html", label="state: empty (no events match filters)",
         sw_text="Empty", sw_href="event-feed-empty.html",
         tree_text="empty", tree_href="event-feed-empty.html", main=EMPTY_MAIN),
    dict(file="event-feed-error.html", label="state: error (load failure)",
         sw_text="Error", sw_href="event-feed-error.html",
         tree_text="error", tree_href="event-feed-error.html", main=ERROR_MAIN),
    dict(file="event-feed-loading.html", label="state: loading (initial fetch)",
         sw_text="Loading", sw_href="event-feed-loading.html",
         tree_text="loading", tree_href="event-feed-loading.html", main=LOADING_MAIN),
    dict(file="event-feed-push-permission-missing.html", label="state: push-permission-missing (banner)",
         sw_text="Push denied", sw_href="event-feed-push-permission-missing.html",
         tree_text="push-permission-missing", tree_href="event-feed-push-permission-missing.html", main=PUSH_MAIN),
]

for s in states:
    c = base

    # 1) page-label
    c = c.replace("base state: success (registered)", s["label"])
    c = c.replace("file: wireframes/event-feed.html", "file: wireframes/" + s["file"])

    # 2) state-switch: move aria-current from Success to the target
    c = c.replace('<a href="event-feed.html" aria-current="page">Success</a>',
                  '<a href="event-feed.html">Success</a>')
    c = c.replace('<a href="%s">%s</a>' % (s["sw_href"], s["sw_text"]),
                  '<a href="%s" aria-current="page">%s</a>' % (s["sw_href"], s["sw_text"]))

    # 3) tree: move the cur marker
    c = c.replace('<li class="cur"><a href="event-feed.html">success - logged in (this page)</a></li>',
                  '<li><a href="event-feed.html">success - logged in</a></li>')
    c = c.replace('<li><a href="%s">%s</a></li>' % (s["tree_href"], s["tree_text"]),
                  '<li class="cur"><a href="%s">%s (this page)</a></li>' % (s["tree_href"], s["tree_text"]))

    # 4) main content surgery
    g0 = c.index('        <div class="grid">')
    t0 = c.index(tail_marker, g0)
    c = c[:g0] + s["main"] + c[t0:]

    out = os.path.join(BASE_DIR, s["file"])
    with open(out, "w", encoding="utf-8") as f:
        f.write(c)
    # report
    emdash = c.count("—")
    print("wrote %-44s em-dash=%d  bytes=%d" % (s["file"], emdash, len(c)))

print("done")
