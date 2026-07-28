#!/usr/bin/env python3
"""
_gen_overview.py  -  builds ui-visual/overview.html, the door into the painted
screens.

Why it exists: the 76 screens had no front page. You could reach one from the
left tree, and the design system's back arrow had nowhere product-shaped to go.
This page is that place: every screen as a chip, grouped by family and by the
substate the tree already groups them under.

Where the list comes from: _resync_sidebar.FAMILIES, the same list that renders
the left tree, so a screen can never appear in one and not the other. Add a page
there, re-run this, and it shows up here too.

What it is styled by: components/index.css (the system) plus ui-kit/_page.css
(the stand layer, the .tk-* vocabulary the design system pages use). This page is
an index, not a screen, which is why it may link the stand layer at all: no
product screen does.

Order, because the sidebar is written by a second script:

    python3 _gen_overview.py
    python3 _resync_sidebar.py

No em dash.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from _resync_sidebar import FAMILIES  # noqa: E402
# The boot has to be emitted HERE, not stamped on afterwards. It was added to this
# page by a separate run of _theme_switch.py, so the first regeneration of the file
# quietly dropped it and the index alone stopped following the switch. A generator
# that does not know about a later pass will undo it every time it runs.
from _theme_switch import BOOT  # noqa: E402


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build():
    states = [r for fam in FAMILIES if fam.get("built")
              for r in fam["rows"] if r[0] == "state"]
    families = [f for f in FAMILIES if f.get("built")]

    out = []
    for i, fam in enumerate(families, 1):
        rows = fam["rows"]
        count = len([r for r in rows if r[0] == "state"])
        out.append('  <section class="tk-sec" id="%s">' % fam["key"])
        out.append('    <h2 data-n="%02d">%s</h2>' % (i, esc(fam["label"])))
        out.append('    <p class="tk-note">%d %s.</p>'
                   % (count, "page" if count == 1 else "pages, one per state"))
        # A family either splits into substates (Logged in, Logged out, and so
        # on) or it does not. Keep the tree's own grouping rather than invent a
        # second one.
        chips, head = [], None
        for row in rows:
            if row[0] == "head":
                if chips:
                    out.extend(_row(head, chips))
                    chips = []
                head = row[1]
            else:
                chips.append(row)
        if chips:
            out.extend(_row(head, chips))
        out.append("  </section>")
    return "\n".join(out), len(states), len(families)


def _row(head, chips):
    L = []
    if head:
        L.append('    <h3 class="tk-subh">%s</h3>' % esc(head))
    L.append('    <div class="tk-jump">')
    for _, fpath, label in chips:
        L.append('      <a href="%s" title="%s">%s</a>' % (fpath, fpath, esc(label)))
    L.append("    </div>")
    return L


SECTIONS, N_SCREENS, N_FAMILIES = build()

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{boot}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - UI screens</title>
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="../ui-kit/_page.css">
</head>
<body>
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the screen tree"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar"></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>The painted screens</h1>
    <p>Every screen of the product in the Vault visual system: {families} families, {screens} pages,
    one page per state. Structure, copy and the state set are owned by the grey wireframes in
    <code>wireframes/</code>; this layer owns colour, type and surface only, which is why a screen
    here reads the same as the grey one beside it.</p>
    <div class="tk-badges">
      <span class="tk-badge">{screens} screens</span>
      <span class="tk-badge">{families} families</span>
      <span class="tk-badge">one page per state</span>
      <span class="tk-badge">mobile first</span>
    </div>
    <div class="tk-jump"><a href="../ui-kit/overview.html">Design system</a><a href="../ui-kit/tokens.html">Tokens</a>
      <a href="../wireframes/event-feed.html">Grey wireframes</a><a href="../research/research.html">Course roadmap</a></div>
  </header>

{sections}
</main>

<script>
(function () {{
  var sb = document.getElementById('rmSidebar'),
      ov = document.getElementById('rmOverlay'),
      tg = document.getElementById('rmToggle');
  if (!sb || !ov || !tg) return;
  tg.addEventListener('click', function () {{ sb.classList.add('open'); ov.classList.add('open'); }});
  ov.addEventListener('click', function () {{ sb.classList.remove('open'); ov.classList.remove('open'); }});
}})();
</script>
</body>
</html>
""".format(boot=BOOT, sections=SECTIONS, screens=N_SCREENS, families=N_FAMILIES)


def main():
    path = os.path.join(HERE, "overview.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PAGE)
    print("built overview.html: %d screens in %d families" % (N_SCREENS, N_FAMILIES))
    print("now run: python3 _resync_sidebar.py")


if __name__ == "__main__":
    main()
