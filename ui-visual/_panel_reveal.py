#!/usr/bin/env python3
"""
_panel_reveal.py  -  the side panel opens showing where you are.

THE DEFECT. Both panels mark the current page and neither could be relied on to
show that mark. The screens tree is 4066px tall in a 900px panel: on toasts.html
the brass row sits 3813px down, on wallet.html 2968px, so the panel opened on
somebody else's family and a person had to scroll a 105-row list to find
themselves. The vitrine is 2302px, which is the same problem two thirds as tall.
Marking the row and never showing it is most of the way to not marking it.

ONE SOURCE FOR TWO TREES, which is why this is a module and not twelve lines
typed twice. The panels are built by different machines: ui-visual/ has the
markup written into 105 files by _resync_sidebar.py, the vitrine renders it at
run time from _nav.js. So the same behaviour has to arrive two ways, as a
<script> in one and as a function call in the other, and both come from the _JS
string below.

WHY scrollTop AND NOT scrollIntoView. The panel is position:fixed, and asking an
element inside a fixed box to scroll itself into view lets the browser scroll the
PAGE as well to satisfy the request. Setting the panel's own scrollTop cannot
move anything else. It is also instant, so there is no animation to exempt under
prefers-reduced-motion and no visible travel on load.

A third of the way down, not centred and not at the edge: the row a person is
looking for is worth more with its family label above it than alone in the
middle of the panel.

Nothing to run. _resync_sidebar.py imports SCRIPT, _gen_component_pages.py
imports BODY and CALL. No em dash.
"""

# The function, once. It is written as a named function so the vitrine can call
# it again after it renders the tree, and so the drawer can call it on open.
_JS = """function pmRevealPanelRow() {
  var panel = document.querySelector('.sidebar');
  if (!panel) return;
  var row = panel.querySelector('.sidebar-page-link.active, .sidebar-sub-link.active') ||
            panel.querySelector('.sidebar-divider.active');
  if (!row) return;
  var r = row.getBoundingClientRect(), p = panel.getBoundingClientRect();
  if (r.top >= p.top && r.bottom <= p.bottom) return;   /* already shown: do not jump */
  panel.scrollTop += (r.top - p.top) - p.height / 3;
}"""

# On a screen the panel is markup, so the script sits INSIDE the <aside>: that is
# where the behaviour belongs, and it is also the span gate 1 masks when it asks
# whether a page moved, so the panel can gain a script without 105 screens
# reading as product changes.
SCRIPT = """<script id="uvPanelReveal">
/* The panel opens showing where you are. One source for both trees:
   ui-visual/_panel_reveal.py. No em dash. */
%s
pmRevealPanelRow();
/* the drawer starts closed under 860px, so the first reveal happens off screen
   and the panel is scrolled back to nothing by the time it slides in */
document.addEventListener('click', function (e) {
  if (e.target.closest && e.target.closest('#rmToggle')) setTimeout(pmRevealPanelRow, 0);
});
</script>""" % _JS

# In the vitrine the panel does not exist until _nav.js has written it, so the
# same function is part of that file and is called at the end of the render.
BODY = _JS
CALL = "pmRevealPanelRow();"
