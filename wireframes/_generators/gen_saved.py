"""Build the Saved view pages (Favorites target): saved.html + empty + loading.

Saved is the logged-in 'filter over the feed' from the IA. Derived from the
event-feed family so the chrome stays byte-identical; the screen-tree entry is
added in _shell.nav_tree and pushed by resync.py. Run BEFORE fixpack.py so the
fixpack wires the saved pages' header / bottom-nav too.
"""
import re
import pathlib
import _shell as S

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")


def state_switch(cur):
    def a(href, label):
        c = ' aria-current="page"' if href == cur else ''
        return f'<a href="{href}"{c}>{label}</a>'
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            '    <div class="ss-row"><span class="ss-label">State</span>'
            + a("saved.html", "Success") + a("saved-empty.html", "Empty")
            + a("saved-loading.html", "Loading") + '</div>\n'
            '  </nav>\n')


SWITCH_RE = re.compile(r'  <nav class="state-switch".*?</nav>\n', re.S)
CAT_TRENDING_ON = '<li aria-current="page"><a href="event-feed.html"><button type="button">Trending</button></a></li>'
CAT_TRENDING_OFF = '<li><a href="event-feed.html"><button type="button">Trending</button></a></li>'


def derive(src, dst, title, cur, extra=()):
    txt = (ROOT / src).read_text()

    # title (state-specific)
    txt = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', txt, count=1)
    # feed heading + zone note (cosmetic; replace if present)
    txt = txt.replace('>Trending</h2>', '>Saved</h2>')
    txt = txt.replace('zone: feed (heading row + sort control, responsive grid, decluttered cards)',
                      'zone: feed (Saved view - your saved events; a filter over the feed)')
    # category sub-nav: nothing is an active category in the Saved view
    txt = txt.replace(CAT_TRENDING_ON, CAT_TRENDING_OFF)
    # bottom nav: Favorites slot is the current one here
    assert S.bottom_in("events") in txt, f"{src}: events bottom-nav not found"
    txt = txt.replace(S.bottom_in("events"), S.bottom_in("fav"), 1)
    # state switcher -> saved states (drop the auth row: Saved is logged-in only)
    assert SWITCH_RE.search(txt), f"{src}: state-switch not found"
    txt = SWITCH_RE.sub(state_switch(cur), txt, count=1)
    # per-page extra replacements
    for old, new in extra:
        assert old in txt, f"{src}: missing extra {old!r}"
        txt = txt.replace(old, new, 1)

    assert "—" not in txt, f"{dst}: em-dash"
    (ROOT / dst).write_text(txt)
    print("wrote", dst)


derive("event-feed.html", "saved.html",
       "Wireframe - Saved (Favorites view, registered, responsive)", "saved.html")

derive("event-feed-loading.html", "saved-loading.html",
       "Wireframe - Saved (loading, registered, responsive)", "saved-loading.html")

derive("event-feed-empty.html", "saved-empty.html",
       "Wireframe - Saved (empty, registered, responsive)", "saved-empty.html",
       extra=[
           ('<p class="state-title">No events match your filters</p>',
            '<p class="state-title">No saved events yet</p>'),
           ('There are no markets for this category and filter combination right now. Try clearing the filters, or get notified when a new event shows up here.',
            'You have not saved any events yet. Tap the bookmark on any event to keep it here for quick access.'),
           ('<button type="button" class="state-btn primary">Clear filters</button>\n            <button type="button" class="state-btn">Notify me of new events in this category</button>',
            '<a href="event-feed.html"><button type="button" class="state-btn primary">Browse events</button></a>'),
       ])
