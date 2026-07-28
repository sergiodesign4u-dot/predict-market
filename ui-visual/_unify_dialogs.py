#!/usr/bin/env python3
"""
_unify_dialogs.py  -  one markup per dialog, in every place that dialog stands.

THE DEFECT. Sign In and Deposit each exist twice in the painted tree: as the
shared <dialog> embedded on all 76 screens, and as the standalone page that IS
that dialog (ui-visual/sign-in.html, ui-visual/deposit.html). Stage 08 painted
the shared copy into a real component and left the standalone on the markup the
grey generator wrote, so the two drifted for two stages with every gate green:
gate 18 compares a screen with its GREY TWIN and never with its own second copy
in the same tree.

What that looked like on screen. The shared dialog carries the real Google, X and
Apple marks; the standalone page carries the wireframe placeholders, and the one
standing in for Google is a circle with a plus in it. The shared puts the lead
line in the head as .sheet-sub where dialog.css styles it; the standalone leaves
it as a .fine at the top of the body. Every provider button on the page is
wrapped in an <a>, which is how a wireframe fakes a flow.

WHICH COPY WINS, AND WHY IT IS NOT ONE ANSWER. "The paint is newer, take the
paint" is wrong here, and reading both is what shows it: the standalone Deposit
had three things the shared one had lost, a label over the payment widget, the
sentence that says card payments are converted via Transak, and an exit to How It
Works, which is the trust affordance the whole screen is there to earn. Those
were merged INTO the canonical copy by hand before this file was written. What
this file does from there is keep one markup, not choose between two.

  the canonical dialog is the one in ui-visual/event-feed.html
  every other painted screen gets that dialog, byte for byte
  the standalone page gets its BODY, rewired for a page

TWO THINGS DIFFER BY CONTEXT, AND ARE NOT DRIFT:

  the head. A dialog is opened over a page, so it heads with <h2> and closes with
      data-close-dialog. A page is a page, so it heads with <h1> (gate 15) and
      closes with a link to where it came from. The head is left alone.
  the wiring. In a dialog a provider button opens the next dialog over the same
      page; on a page it navigates. Same control, wired to its context, and the
      table below is the one place either wiring is written.

Idempotent. Writes ui-visual/ only.

Usage:
    python3 ui-visual/_unify_dialogs.py            # apply
    python3 ui-visual/_unify_dialogs.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAINT = HERE
CANON = "event-feed.html"

# family -> (shared dialog id, the standalone page that is this dialog)
FAMILIES = {
    "signin": ("signinDialog", "sign-in.html"),
    "deposit": ("depositDialog", "deposit.html"),
}

# Where a control goes when the dialog is a PAGE. In the dialog these same
# controls carry data-flow / data-open / data-close-dialog and open the next
# sheet over the screen you were already on; on a page there is nothing behind to
# stay on, so they navigate. One table, both wirings, no third copy.
WIRING = {
    "signin": [('data-flow="signin-to-deposit"', "deposit.html")],
    "deposit": [('data-open="howitworks"', "how-it-works.html"),
                ("data-close-dialog", "event-detail-bet-reconcile.html")],
}

# A provider mark is one drawing wherever that button stands. The three state
# screens (sign-in error, loading, provider conflict) are not copies of the base
# and must not be overwritten by it, but the button inside them is the same
# button, and all three were drawing the wireframe placeholders: a circle with a
# plus in it for Google, a bare cross for X, a hand-drawn apple. The mark is
# swapped in place, matched by what the button says.
#
# Only a mark that is already there is replaced. A button with no mark keeps
# none: putting one on it would be a design decision, and this file's job is to
# end a fork, not to start one.
PROVIDER = [("Google", "prov-google"), ("Apple", "prov-apple"), ("with X", "prov-x")]

VOID = {"br", "img", "input", "use", "path", "circle", "meta", "link",
        "polyline", "source", "rect", "line", "hr", "ellipse", "stop"}


def region(html, tag, attr="", cls=""):
    if attr:
        pat = r"<%s[^>]*%s[^>]*>" % (tag, attr)
    elif cls:
        pat = r'<%s\b[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls)
    else:
        pat = r"<%s\b[^>]*>" % tag
    m = re.search(pat, html)
    if not m:
        return None, None, None
    depth, i = 0, m.start()
    for t in re.finditer(r"<(/?)(%s)\b[^>]*?(/?)>" % tag, html[i:]):
        if t.group(1):
            depth -= 1
            if depth == 0:
                return html[i:i + t.end()], i, i + t.end()
        elif not t.group(3):
            depth += 1
    return None, None, None


def marks_of(dialog):
    """provider key -> its <svg>, read out of the canonical dialog."""
    out = {}
    for m in re.finditer(r'<svg class="ic (prov-[\w-]+)".*?</svg>', dialog, re.S):
        out[m.group(1)] = m.group(0)
    return out


def set_marks(html, marks):
    """Every provider button draws its provider's mark."""
    out, pos, changed = [], 0, False
    for m in re.finditer(r'<button\b[^>]*class="[^"]*\bprovider-btn\b[^"]*"[^>]*>', html):
        if m.start() < pos:
            continue
        btn, a, b = region(html[m.start():], "button")
        if not btn:
            continue
        a, b = m.start() + a, m.start() + b
        svg = re.search(r"<svg\b.*?</svg>", btn, re.S)
        label = re.sub(r"<[^>]+>", " ", btn)
        want = next((marks[cls] for text, cls in PROVIDER
                     if text in label and cls in marks), None)
        if svg and want and svg.group(0) != want:
            out.append(html[pos:a])
            out.append(btn[:svg.start()] + want + btn[svg.end():])
            pos, changed = b, True
    if not changed:
        return html, False
    out.append(html[pos:])
    return "".join(out), True


def rewire(body, family):
    """The dialog's wiring swapped for a page's. Each control keeps its markup
       and gains the link its flow needs."""
    for attr, href in WIRING[family]:
        while True:
            m = re.search(r"<button\b[^>]*" + re.escape(attr) + r"[^>]*>", body)
            if not m:
                break
            btn, a, b = region(body[m.start():], "button")
            if not btn:
                break
            a, b = m.start() + a, m.start() + b
            clean = btn.replace(" " + attr, "").replace(attr + " ", "").replace(attr, "")
            body = body[:a] + '<a href="%s">%s</a>' % (href, clean) + body[b:]
    return body


def main():
    check = "--check" in sys.argv
    canon = open(os.path.join(PAINT, CANON), encoding="utf-8").read()
    shared = {}
    for fam, (did, _) in FAMILIES.items():
        blk = region(canon, "dialog", 'id="%s"' % did)[0]
        if not blk:
            raise SystemExit("_unify_dialogs: no #%s in %s" % (did, CANON))
        shared[fam] = blk
    marks = marks_of(shared["signin"])
    if len(marks) != 3:
        raise SystemExit("_unify_dialogs: expected 3 provider marks in the "
                         "canonical sign-in dialog, found %d" % len(marks))

    changed = 0
    for name in sorted(os.listdir(PAINT)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(PAINT, name)
        html = out = open(path, encoding="utf-8").read()
        why = []

        # 1. the shared dialog, byte for byte, wherever it is embedded
        for fam, (did, _) in FAMILIES.items():
            old, a, b = region(out, "dialog", 'id="%s"' % did)
            if old is not None and old != shared[fam]:
                out = out[:a] + shared[fam] + out[b:]
                why.append(did)

        # 2. the standalone page that IS one of those dialogs: same body, same
        #    sub-line, its own heading level and its own wiring
        for fam, (did, page) in FAMILIES.items():
            if name != page:
                continue
            src = region(shared[fam], "div", cls="sheet-body")[0]
            own = region(out, "dialog", 'id="outcomeDialog"')[0]
            if not (src and own):
                continue
            want = rewire(src, fam)
            old, a, b = region(own, "div", cls="sheet-body")
            if old is not None and old != want:
                oa = out.find(own)
                out = out[:oa + a] + want + out[oa + b:]
                own = region(out, "dialog", 'id="outcomeDialog"')[0]
                why.append("body")

            # The head is the page's, but only its HEADING LEVEL and its close are.
            # The sub-line under the title is the sentence that says why you are
            # being asked, and the page had none: the first cut of this file moved
            # the body across and left the page with a title and three buttons. A
            # declared difference has to be the difference that was declared.
            sub = re.search(r'<p class="sheet-sub">.*?</p>', shared[fam], re.S)
            head, ha, hb = region(own, "div", cls="sheet-head")
            if sub and head is not None and sub.group(0) not in head:
                new = re.sub(r"(</h[12]>)", lambda m: m.group(1) + sub.group(0), head, count=1)
                if new != head:
                    oa = out.find(own)
                    out = out[:oa + ha] + new + out[oa + hb:]
                    why.append("sub")

        # 3. and wherever else a provider button stands, it draws the same mark
        out, swapped = set_marks(out, marks)
        if swapped:
            why.append("marks")

        if out != html:
            changed += 1
            print("%-34s %s" % (name, " ".join(why)))
            if not check:
                open(path, "w", encoding="utf-8").write(out)
    print("---", "%d page(s) %s" % (changed, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
