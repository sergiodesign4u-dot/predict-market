"""Idempotent 'How it works' header button + quick-explainer dialog (WF).

Adds, on every wireframe page that carries the shared app-header (87 pages):
  1. a 'How it works' button in the header next to the logo (data-open trigger),
  2. a self-contained native <dialog id="howitworksDialog"> with the feed explainer
     copy (How betting works here / Why the odds move / Common questions) and a
     'Read the full guide' link to how-it-works.html,
  3. the CSS for both,
  4. the open() + backdrop-close JS wiring for the new dialog.

The dialog is SELF-CONTAINED: it styles itself through scoped .hiw-* classes and
only relies on the universal `dialog.app-dialog` base rule + ::backdrop. It does
NOT reuse .sheet-head / .field-label / .protect / .confirm-btn, because those are
only defined on the 25 event-feed-family pages, not on the other 62 header pages.
So it renders identically everywhere.

Voice-safe in-place post-processor (the fixpack.py pattern): plain string replace,
skip-if-already-applied, em-dash guard. Never runs gen_*.py. The copy mirrors the
feed below-fold SEO sections (already voice-approved), so nothing new to log.

Usage:
    python3 howitworks.py            # apply to all header pages
    python3 howitworks.py --check    # report which pages would change, no write

THE CLOSE IS `.sheet-close` AND ITS MARK IS THE ICON, SINCE 2026-08-05. It was
`.hiw-close` with the letter x, and both went when the product's two closes were
merged into one control in components/dialog.css. This generator must never be
run (see CLAUDE.md), and it is corrected anyway: a script that writes a class no
stylesheet declares is a trap set for whoever forgets that rule, and the rule is
about the VOICE rewrite rather than about the markup being right.
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)                             # wireframes/

CSS_ANCHOR = "    dialog.app-dialog::backdrop { background: rgba(0,0,0,.4); }"
CSS_BLOCK = """
    /* ---- How it works: header button + quick-explainer dialog (WF) ---- */
    .hiw-btn { border: 1px solid #999; background: #e0e0e0; padding: 5px 10px; font-size: 12px; cursor: pointer; }
    dialog.app-dialog .hiw-head { display: flex; align-items: center; justify-content: space-between; padding: 8px 10px; border-bottom: 1px solid #ccc; }
    dialog.app-dialog .hiw-head h2 { font-size: 14px; margin: 0; }
    dialog.app-dialog .hiw-body { padding: 10px; display: flex; flex-direction: column; gap: 10px; }
    dialog.app-dialog .hiw-label { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: #555; }
    dialog.app-dialog .hiw-sec p { font-size: 13px; color: #333; line-height: 1.5; margin: 4px 0 0; }
    dialog.app-dialog .hiw-sec dl { margin: 0; }
    dialog.app-dialog .hiw-sec dt { font-size: 13px; font-weight: bold; margin: 8px 0 2px; }
    dialog.app-dialog .hiw-sec dd { font-size: 13px; color: #333; line-height: 1.5; margin: 0; }
    dialog.app-dialog .hiw-full { display: block; box-sizing: border-box; border: 1px solid #888; background: #c4c4c4; padding: 12px; font-size: 14px; font-weight: bold; text-align: center; text-decoration: none; color: #222; }"""

LOGO = '<button type="button" class="logo-btn" aria-label="Predict Market - go to Events home">Predict Market</button>'
BTN = '\n          <button type="button" class="hiw-btn" data-open="howitworks" aria-label="How it works">How it works</button>'

DIALOG = """  <dialog id="howitworksDialog" class="app-dialog" aria-label="How it works">
    <div class="hiw-head">
      <h2>How it works</h2>
      <button type="button" class="sheet-close" data-close-dialog aria-label="Close"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    </div>
    <div class="hiw-body">
      <div class="hiw-sec">
        <span class="hiw-label">How betting works here</span>
        <p>Predict Market turns the events you follow into a real stake. Pick an event, read the odds in plain language, and back YES or NO. You see the current odds, a one-line why, and how the event resolves before you put in a cent. The minimum bet is one dollar, and you can browse and build your bet before you connect a wallet.</p>
      </div>
      <div class="hiw-sec">
        <span class="hiw-label">Why the odds move</span>
        <p>The odds are a live price set by what people bet, not a fixed quote. When more money backs YES, YES costs more and NO costs less. Your payout depends on the odds at the moment you bet, not only on the outcome, so reading an event early and being right is worth more.</p>
      </div>
      <div class="hiw-sec">
        <span class="hiw-label">Common questions</span>
        <dl>
          <dt>Do I need crypto to start?</dt>
          <dd>No. You can browse events and build a bet with no wallet. You add funds by card or crypto only when you confirm.</dd>
          <dt>What is the smallest bet?</dt>
          <dd>One dollar. The default is five.</dd>
          <dt>How does an event resolve?</dt>
          <dd>Each event states its resolution rule up front. The team resolves it against the real-world outcome, and you can see the record of resolved events.</dd>
        </dl>
      </div>
      <a href="how-it-works.html" class="hiw-full">Read the full guide</a>
    </div>
  </dialog>

"""

SCRIPT_ANCHOR = "  <script>\n    // Shared dialogs:"

JS_OLD = "open(o.getAttribute('data-open') === 'deposit' ? 'depositDialog' : 'signinDialog')"
JS_NEW = ("var dv = o.getAttribute('data-open'); open(dv === 'deposit' ? 'depositDialog' : "
          "dv === 'howitworks' ? 'howitworksDialog' : 'signinDialog')")

FOREACH_OLD = "['signinDialog', 'depositDialog'].forEach"
FOREACH_NEW = "['signinDialog', 'depositDialog', 'howitworksDialog'].forEach"

# guard our own injected text at import time
for _s in (CSS_BLOCK, BTN, DIALOG, JS_NEW, FOREACH_NEW):
    if "—" in _s or "–" in _s:
        raise SystemExit("em/en-dash in a howitworks constant")


def process(html):
    changed = False
    if ".hiw-btn {" not in html and CSS_ANCHOR in html:
        html = html.replace(CSS_ANCHOR, CSS_ANCHOR + CSS_BLOCK, 1)
        changed = True
    if 'data-open="howitworks"' not in html and LOGO in html:
        html = html.replace(LOGO, LOGO + BTN, 1)
        changed = True
    if 'id="howitworksDialog"' not in html and SCRIPT_ANCHOR in html:
        html = html.replace(SCRIPT_ANCHOR, DIALOG + SCRIPT_ANCHOR, 1)
        changed = True
    if JS_OLD in html:
        html = html.replace(JS_OLD, JS_NEW, 1)
        changed = True
    if FOREACH_OLD in html:
        html = html.replace(FOREACH_OLD, FOREACH_NEW, 1)
        changed = True
    return html, changed


def main():
    check = "--check" in sys.argv
    done = skipped = 0
    for path in sorted(glob.glob(os.path.join(WF, "*.html"))):
        html = open(path, encoding="utf-8").read()
        if 'class="app-header"' not in html:           # only pages with the shared header
            continue
        new, changed = process(html)
        if not changed:
            skipped += 1
            continue
        if not check:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
        done += 1
        print(("would update " if check else "updated ") + os.path.basename(path))
    print("header pages updated: {}, already-applied/skipped: {}".format(done, skipped))


if __name__ == "__main__":
    main()
