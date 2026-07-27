#!/usr/bin/env python3
"""
_destyle.py  -  take the styling off the elements and give it to the system.

WHAT WAS THERE. 110 style attributes on 30 painted screens, left from the grey
wireframe and never picked up by any of the passes that built the system: type
(font-size:24px, font-weight:bold, letter-spacing), geometry (margin:0 0 8px,
padding:12px 14px, width:72px next to a --size-72 that exists), layout variants
(justify-content:center;width:100%), and twelve places where a component was
undone on the element (border:none, background:none, position:static).

WHY THEY SURVIVED. Gate 9 asks whether a screen has a <style> block or a second
stylesheet; an attribute is neither. Gate 12 forbids a raw scale value inside
components/*.css; an attribute is not in components/. So the one place the rules
did not look is the one place the values stayed.

WHAT THE PASS FOUND ON THE WAY. Half of them were already dead: the system had
grown a rule that said the same thing, and the attribute was a duplicate nobody
had noticed (`.app-case .ed-main>.card` is already border:0, `.confirm-btn` is
already width:100%, `.outcome-dialog .reconcile-box` already centres). Two more
explain an `!important`: profile.css and state-block.css were shouting to beat an
inline style, and once the attribute goes the shout goes with it.

THE ONE THING THAT MOVES. Four bet-dock buttons and one CTA bar lose 2px of
padding, because 14px and 10px are not on the 4px grid and step 6's own map
sends them to 12 and 8. Values in an attribute never went through that pass.
Everything else is verified identical.

Idempotent, and it refuses to guess: an attribute this table does not describe
is reported and left alone.

    python3 ui-visual/_destyle.py [--dry-run]
No em dash.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (tag, class, style) -> why it can go.
#   "same"  the system already says it, the attribute is a duplicate
#   "moved" the declaration is now a rule; the comment names it
RULES = {
    ("span", "pos-status", "white-space:nowrap;"):
        ("moved", "profile.css .app-case .pos-top .pos-status"),
    ("a", "", "text-decoration:none;color:inherit;display:block;"):
        ("moved", "position.css .app-case a:has(>.pos)"),
    ("button", "provider-btn", "justify-content:center;width:100%;"):
        ("moved", "button.css bet-panel/bet-sheet provider-btn centres; width:100% already base"),
    ("button", "provider-btn", "justify-content:center;"):
        ("moved", "button.css, same rule"),
    ("article", "card", "border:none;"):
        ("same", "card.css .app-case .ed-main>.card is border:0"),
    ("article", "card skeleton", "border:none;"):
        ("same", "card.css, same rule"),
    ("p", "pos-note", "margin:0 0 8px;"):
        ("moved", "position.css .app-case .ed-panel-activity .pos-note"),
    ("p", "fine", "font-weight:bold;font-size:13px;margin:0;"):
        ("moved", "dialog.css .outcome-dialog .sheet-body>.fine:first-child"),
    ("div", "pos-figures", "font-size:11px;"):
        ("moved", "position.css, the two standalone stat blocks"),
    ("div", "reconcile-box", "align-items:center;text-align:center;"):
        ("same", "notice.css .outcome-dialog .reconcile-box"),
    ("p", "pos-status", "margin:10px 0 2px;text-transform:uppercase;letter-spacing:.04em;"):
        ("same", "profile.css p.pos-status already wins, and can now drop its !important"),
    ("p", "pos-status", "margin:12px 0 4px;text-transform:uppercase;letter-spacing:.04em;"):
        ("same", "profile.css, same rule"),
    ("button", "confirm-btn", "width:auto;padding:12px 14px;"):
        ("moved", "button.css .app-case .bet-dock .confirm-btn, 14px onto the grid at 12"),
    ("button", "confirm-btn", "width:100%;"):
        ("same", "button.css .confirm-btn is already width:100%"),
    ("button", "confirm-btn", "width:100%"):
        ("same", "button.css, same rule"),
    ("strong", "", "font-size:24px;"):
        ("moved", "notice.css .win-dialog .reconcile-box strong"),
    ("strong", "", "font-size:20px;"):
        ("moved", "notice.css .loss-dialog .reconcile-box strong"),
    ("span", "sk-thumb", "width:72px;height:72px;flex:0 0 72px;"):
        ("moved", "skeleton.css .ed-head .sk-thumb, onto --size-72"),
    ("div", "", "flex:1;"):
        ("moved", "skeleton.css .card.skeleton .ed-head>div"),
    ("div", "chart-svg", "display:flex;align-items:center;justify-content:center;color:var(--text-muted);font-size:11px;"):
        ("moved", "chart.css div.chart-svg, the loading placeholder"),
    ("a", "", "flex:1;"):
        ("moved", "account.css .app-case .cta-bar>a"),
    ("button", "", "width:100%;"):
        ("moved", "account.css .app-case .cta-bar>a>button"),
    ("button", "", "flex:1;"):
        ("same", "account.css .app-case .cta-bar button is already flex:1"),
    ("div", "state-block", "margin:8px;"):
        ("same", "state-block.css forces margin:0 on the resolved panel, and can now drop its !important"),
    ("div", "cta-bar", "position:static;border:none;background:none;padding:10px 0 0;"):
        ("moved", "account.css .cta-bar.flat, 10px onto the grid at 8"),
    ("div", "cta-bar", "position:static;padding:8px 0 0;border:none;background:none;"):
        ("moved", "account.css .cta-bar.flat"),
    ("div", "cta-bar", "position:static;"):
        ("moved", "account.css .cta-bar.static"),
}

# the two CTA bars that are not the sticky dock get told so in the markup
FLAT = {
    "position:static;border:none;background:none;padding:10px 0 0;": "flat",
    "position:static;padding:8px 0 0;border:none;background:none;": "flat",
    "position:static;": "static",
}

TAG = re.compile(r"<(\w+)([^>]*?)\sstyle=\"([^\"]*)\"([^>]*)>")


def keep(style):
    """a width that is a datum, a photograph, or a value the script writes"""
    s = style.strip()
    if "'+" in s or "' +" in s:
        return True
    if re.fullmatch(r"width:\d+(\.\d+)?%;?", s) or s == "position:absolute":
        return True
    return "background-image:url" in s


def main():
    dry = "--dry-run" in sys.argv
    removed = 0
    unknown = {}
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(HERE, fname)
        html = open(path, encoding="utf-8").read()

        def sub(m):
            nonlocal removed
            tag, a, style, b = m.group(1), m.group(2), m.group(3), m.group(4)
            if keep(style):
                return m.group(0)
            cls = re.search(r'class="([^"]*)"', a + b)
            cls = cls.group(1).strip() if cls else ""
            key = (tag, cls, style)
            if key not in RULES:
                unknown[key] = unknown.get(key, 0) + 1
                return m.group(0)
            removed += 1
            mod = FLAT.get(style)
            attrs = (a + b)
            if mod:
                attrs = re.sub(r'class="([^"]*)"', lambda x: 'class="%s %s"' % (x.group(1), mod), attrs)
            attrs = re.sub(r"\s+", " ", attrs).strip()
            return "<%s%s>" % (tag, (" " + attrs) if attrs else "")

        new = TAG.sub(sub, html)
        if new != html and not dry:
            open(path, "w", encoding="utf-8").write(new)
    print("%d style attributes %s" % (removed, "would go" if dry else "removed"))
    if unknown:
        print("NOT described by the table, left alone:")
        for (t, c, s), n in sorted(unknown.items(), key=lambda x: -x[1]):
            print("  %2d  <%s class=\"%s\"> %s" % (n, t, c, s))


if __name__ == "__main__":
    main()
