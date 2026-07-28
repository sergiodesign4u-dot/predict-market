#!/usr/bin/env python3
"""
subfilter.py  -  the Trending sub-filter filters Trending, instead of leaving it.

THE DEFECT. The Event Feed carries two controls that look different and did the
same thing. The band at the top of the page (Trending / Politics / Crypto /
Culture / General) navigates: each category is its own indexed URL, which is what
ia/docs/pages/seo.md specifies and what the four category pages are for. The chip
row under the "Trending" heading is labelled "Filter events by category" and was
five more links to the same four pages. So the page offered a filter that was a
second navigation, and pressing Politics inside Trending left Trending.

A control is named by what it does. This one says filter, so it filters: the
twelve trending events stay on the page and the ones from other categories are
hidden. Nothing about the top band changes, because a category page is a real
destination with its own H1, its own SEO body and its own URL.

WHAT IT NEEDS, AND WHERE EACH PIECE LIVES.
  the control      a group of buttons, not a nav of links. aria-pressed says
                   which is on; the styling hook stays li[aria-current="page"],
                   which is what both trees already paint.
  the datum        a card has to say which category it is, so every .card gets
                   data-cat. It is read from the painted feed's own photographs
                   (assets/event-<category>.jpg), because that mapping already
                   exists and a second hand-typed list of it would be a fork.
                   The two trees carry the same twelve events in the same order,
                   so the grey tree takes it by position.
  the behaviour    one script, the same in both trees. It hides with the hidden
                   ATTRIBUTE rather than a class, so a card that is filtered out
                   is out of the accessibility tree too, not just invisible.

Idempotent, and it edits BOTH trees, because a control is structure and structure
is owned by wireframes/ while the paint has to carry the same markup (gate 18).

Usage:
    python3 wireframes/_generators/subfilter.py            # apply
    python3 wireframes/_generators/subfilter.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PAINT = os.path.join(ROOT, "ui-visual")
GREY = os.path.join(ROOT, "wireframes")
PAGE = "event-feed.html"

sys.path.insert(0, HERE)
from port_structure import CHROME_MARKER  # noqa: E402

CATS = [("all", "All"), ("politics", "Politics"), ("crypto", "Crypto"),
        ("culture", "Culture"), ("general", "General")]

NAV_RE = re.compile(r'<nav class="feed-subfilter"[^>]*>.*?</nav>', re.S)
GROUP_RE = re.compile(r'<div class="feed-subfilter"[^>]*>.*?</div><!-- /feed-subfilter -->', re.S)
CARD_RE = re.compile(r'<article class="card(?: [^"]*)?"')
PHOTO_RE = re.compile(r'<span class="thumb"[^>]*event-([a-z]+)\.jpg')

SCRIPT = """<script id="uv-subfilter">
/* The Trending sub-filter filters Trending. Built by
   wireframes/_generators/subfilter.py; see that file for why this is not the
   category nav. A hidden card is hidden by the ATTRIBUTE, so it leaves the
   accessibility tree with the layout. */
(function () {
  var group = document.querySelector('.feed-subfilter');
  if (!group) return;
  var grid = document.querySelector('.grid');
  if (!grid) return;
  group.addEventListener('click', function (e) {
    var btn = e.target.closest('button[data-filter]');
    if (!btn) return;
    var want = btn.getAttribute('data-filter');
    var all = group.querySelectorAll('button[data-filter]');
    for (var i = 0; i < all.length; i++) {
      var on = all[i] === btn;
      all[i].setAttribute('aria-pressed', on ? 'true' : 'false');
      all[i].parentNode.toggleAttribute('aria-current', false);
      if (on) { all[i].parentNode.setAttribute('aria-current', 'page'); }
      else { all[i].parentNode.removeAttribute('aria-current'); }
    }
    var cards = grid.querySelectorAll('.card');
    for (var j = 0; j < cards.length; j++) {
      var cat = cards[j].getAttribute('data-cat');
      cards[j].toggleAttribute('hidden', want !== 'all' && cat !== want);
    }
  });
})();
</script>"""


def control():
    rows = []
    for i, (key, label) in enumerate(CATS):
        cur = ' aria-current="page"' if i == 0 else ""
        rows.append('            <li%s><button type="button" data-filter="%s" '
                    'aria-pressed="%s">%s</button></li>'
                    % (cur, key, "true" if i == 0 else "false", label))
    return ('<div class="feed-subfilter" role="group" aria-label="Filter events by category">\n'
            '          <ul>\n' + "\n".join(rows) + "\n          </ul>\n"
            "        </div><!-- /feed-subfilter -->")


def cats_of(painted):
    """The category of each card, in order, read from the photograph it carries."""
    return PHOTO_RE.findall(painted)


def mark_cards(html, cats):
    """Every card says which category it is, once, in the order the two trees
       share. Cards already marked are left alone, which is what makes a re-run
       a no-op."""
    n = [0]

    def sub(m):
        if n[0] >= len(cats):
            return m.group(0)
        cat = cats[n[0]]
        n[0] += 1
        cls = re.search(r'class="([^"]*)"', m.group(0)).group(1)
        return '<article class="%s" data-cat="%s"' % (cls, cat)

    return re.sub(r'<article class="card(?: [^"]*)?"(?! data-cat)', sub, html)


def one(path, cats, check):
    html = open(path, encoding="utf-8").read()
    out = html
    why = []

    if NAV_RE.search(out):
        out = NAV_RE.sub(lambda m: control(), out, count=1)
        why.append("control")
    elif GROUP_RE.search(out):
        new = control()
        if GROUP_RE.search(out).group(0) != new:
            out = GROUP_RE.sub(lambda m: new, out, count=1)
            why.append("control")

    marked = mark_cards(out, cats)
    if marked != out:
        out = marked
        why.append("data-cat")

    # The grey tree carries its own inline css and never links index.css, so the
    # [hidden] invariant base.css declares cannot reach it. Without it the filter
    # sets the attribute and the browser goes on drawing the card, because
    # .card{display:flex} in the grey sheet beats the user agent's display:none.
    # WHERE THE OTHER GENERATOR'S WORK ENDS. port_chrome.py owns everything from
    # its marker to </style> and rewrites that whole span, so a rule appended
    # before </style> lands inside its territory and is deleted on its next run,
    # which put the two tools in a loop: one rewrote the page, the other rewrote
    # it back, forever. The rule goes ABOVE the marker, in the page's own sheet.
    mark = "/* subfilter: hidden is a state */"
    rule = "    %s\n    [hidden] { display: none !important; }\n" % mark
    if mark not in out and "<style" in out:
        i = out.find(CHROME_MARKER)
        if i == -1:
            i = out.index("</style>")
        out = out[:i] + rule + out[i:]
        why.append("hidden")

    if 'id="uv-subfilter"' not in out:
        out = out.replace("</body>", SCRIPT + "\n</body>", 1)
        why.append("script")

    if out != html:
        print("%-34s %s" % (os.path.relpath(path, ROOT), " ".join(why)))
        if not check:
            open(path, "w", encoding="utf-8").write(out)
        return 1
    return 0


def main():
    check = "--check" in sys.argv
    painted = open(os.path.join(PAINT, PAGE), encoding="utf-8").read()
    cats = cats_of(painted)
    if len(cats) < 12:
        raise SystemExit("subfilter: read %d card photographs on the painted feed, "
                         "expected 12. The category of a card is read from its "
                         "picture; without one there is nothing to read." % len(cats))
    n = one(os.path.join(PAINT, PAGE), cats, check)
    n += one(os.path.join(GREY, PAGE), cats, check)
    print("---", "%d page(s) %s" % (n, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
