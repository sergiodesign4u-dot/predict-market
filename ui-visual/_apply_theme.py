#!/usr/bin/env python3
"""
Paint the STATE pages of a listing family, from the family's own finished page.

Strategy: "shell + swap". A finished painted page is the shell (head links,
roadmap sidebar, transformed header / bottom-nav / footer, the shared dialogs,
scripts). For each state we start from that shell and swap in only the regions
that differ from the logged-in base:
  - logged-in states (empty / error / loading / push): <main> only.
  - logged-out states: <header>, <main>, and the mobile <nav.bottom-nav>.
Grafted fragments come from wireframes/ (grey), so we run two voice-safe text
transforms on them: the Favorites heart -> bookmark, and a product link is kept
if the screen it points at has been painted (only an unpainted destination is
flattened to "#"; see _relink.py, which repaired the pages this file used to
flatten wholesale).
Everything the theme needs is class-based, so the swapped content colours itself.

TWO FAMILIES, ONE MACHINE (step 8). This built the Event Feed's eight states and
nothing else, with event-feed.html hard-coded as the shell, so the four category
pages shipped with a base and no states: 32 grey category screens against 4
painted ones, and gate 18 could not see it because it pairs the trees by
filename and this family does not share filenames (see _twins.py). A category
page is the same listing with one filter on it, so it is the same machine with a
different shell, not a second generator.

THE PLATE IS BUILT, NOT PATCHED. The first cut inserted the plate wrappers by
finding <div class="feed-inner"> in the GREY fragment, which worked until step 7d
ported this file's own output back into the grey tree and step 18's unwrap took
the plate out of it again (a plate is paint, so the port drops it). The anchor
then matched nothing, the swap became a silent no-op, and re-running this file
would have shipped eight state pages with no stone plate under them. An anchor
that can be removed by another tool is not an anchor: the wrapper structure is
written out from scratch here, every run, whatever the grey fragment arrives in.

Idempotent: re-running regenerates each state file from the current shell.
NEVER edits wireframes/ and NEVER regenerates a base page.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UIV = ROOT / "ui-visual"
WF = ROOT / "wireframes"
sys.path.insert(0, str(ROOT))
import _twins                                                   # noqa: E402

HEART = "M12 21s-7-4.5-9.5-9C1 9 2.6 5.5 6 5.5c2 0 3.2 1.3 4 2.4.8-1.1 2-2.4 4-2.4 3.4 0 5 3.5 3.5 6.5C19 16.5 12 21 12 21z"
BOOKMARK = "M6 3h12v18l-6-4-6 4z"

WRAPPERS = {"cat-layout", "cat-main", "feed-inner"}
VOID = {"br", "img", "input", "use", "path", "circle", "meta", "link",
        "polyline", "source", "rect", "line", "hr", "ellipse", "stop"}

# (state slug, grey suffix, logged_out?, <title> suffix)
FEED_STATES = [
    ("empty", "-empty", False, "empty state"),
    ("error", "-error", False, "error state"),
    ("loading", "-loading", False, "loading state"),
    ("push-permission-missing", "-push-permission-missing", False, "push-permission missing"),
    ("logged-out", "-logged-out", True, "logged out"),
    ("logged-out-empty", "-logged-out-empty", True, "logged out, empty"),
    ("logged-out-error", "-logged-out-error", True, "logged out, error"),
    ("logged-out-loading", "-logged-out-loading", True, "logged out, loading"),
]
# A category page has no push-permission state: the permission prompt belongs to
# the first screen a person lands on, and _twins.STATES is the list both this
# file and gate 18 read.
CAT_STATES = [(s.lstrip("-"), s, "logged-out" in s, s.lstrip("-").replace("-", ", "))
              for s in _twins.STATES if s]

LABEL = {"politics": "Politics", "crypto": "Crypto",
         "culture": "Culture", "general": "General"}

# What this run will be able to link to: what is painted now PLUS what it is
# about to write, so a link into a state page is not flattened on the first run
# only to come back on the second.
PAINTED = {p.name for p in UIV.glob("*.html")} | set(_twins.PAINTED.values())


def block(html, open_marker, close_tag):
    """Return the substring from open_marker's start through close_tag (inclusive)."""
    s = html.index(open_marker)
    e = html.index(close_tag, s) + len(close_tag)
    return s, e, html[s:e]


def swap(html, open_marker, close_tag, new):
    s, e, _ = block(html, open_marker, close_tag)
    return html[:s] + new + html[e:]


def element(html, tag, cls):
    """The outer html of the first <tag class="... cls ...">, by counting depth."""
    m = re.search(r'<%s\b[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls), html)
    if not m:
        return None
    depth, i = 0, m.start()
    for t in re.finditer(r"<(/?)(%s)\b[^>]*?(/?)>" % tag, html[i:]):
        if t.group(1):
            depth -= 1
            if depth == 0:
                return html[i:i + t.end()]
        elif not t.group(3):
            depth += 1
    return None


def unwrap(html, names):
    """Drop the tags of a wrapper div, keep everything inside it.

       A generic DOM helper, deliberately a second copy of the one in
       port_structure.py: what must not be duplicated is a FACT about this system
       (which screen twins which, which class is a plate), and those live in
       _twins.py and in the WRAPPERS set above."""
    out, stack, pos = [], [], 0
    for m in re.finditer(r"<(/?)([a-z0-9]+)([^>]*?)(/?)>", html):
        close, tag, attrs, self = m.groups()
        out.append(html[pos:m.start()])
        pos = m.end()
        if close:
            if not (stack.pop() if stack else False):
                out.append(m.group(0))
            continue
        cl = re.search(r'class="([^"]*)"', attrs)
        classes = set(cl.group(1).split()) if cl else set()
        drop = tag == "div" and bool(classes & names)
        if not (self or tag in VOID):
            stack.append(drop)
        if not drop:
            out.append(m.group(0))
    out.append(html[pos:])
    return "".join(out)


def drop_element(html, tag, cls):
    el = element(html, tag, cls)
    return html.replace(el, "", 1) if el else html


def keep_or_kill(m):
    """A grey link the painted tree can honour, or '#'.

    This used to flatten every product link without asking, which is how the
    whole coloured product ended up with no navigation (fixed by _relink.py).
    Where a link goes is structure and structure belongs to the wireframes, so
    the only thing worth deciding here is whether the destination has been
    painted yet: if it has, the link stands; if it has not, pointing at it
    would be a broken link rather than a dead one.
    """
    href = m.group(1)
    base, _, frag = href.partition("#")
    base = _twins.painted_of(base.split("?")[0])
    if base in PAINTED:
        return 'href="%s"' % (base + ("#" + frag if frag else ""))
    return 'href="#"'


def neutralize(frag):
    """Grey wireframe fragment -> painted fragment (heart -> bookmark)."""
    frag = re.sub(r'href="([^"]*\.html[^"]*)"', keep_or_kill, frag)
    frag = frag.replace(HEART, BOOKMARK)
    return frag


def distill(frag):
    """Match the reference screen's /distill pass: drop the duplicate Category
    dropdown (the chip band already covers it), the 'Volatile' trader-jargon sort,
    and the reverse-sort toggle. Idempotent no-op where a block is absent."""
    frag = re.sub(r'\s*<details class="filter-menu" id="catMenu">.*?</details>', "", frag, flags=re.S)
    frag = re.sub(r'\s*<li><label><input type="radio" name="sort" value="Volatile">\s*Volatile</label></li>', "", frag)
    frag = re.sub(r'\s*<div class="reverse-row">.*?</div>', "", frag, flags=re.S)
    return frag


def plate(main_frag, catnav):
    """The state's content on the same stone plate the family's base page uses,
       so a state reads as "the same listing, minus the cards" and not as a
       decapitated page.

       Built from the inside out: whatever plate the grey fragment arrived with
       is unwrapped first, so this is the same answer on a fragment that has
       never been through here and on one that has."""
    inner = block(main_frag, "<main", "</main>")[2]
    inner = inner[inner.index(">") + 1:inner.rindex("</main>")]
    inner = unwrap(inner, WRAPPERS)
    # A wrapper leaves a comment behind. unwrap() takes the tags out and the
    # port carried the closing comments into the grey tree as text, so a
    # fragment arrives here already marked "/cat-main" with no cat-main in it.
    inner = re.sub(r"[ \t]*<!-- /(?:cat-main|cat-layout) -->", "", inner)
    inner = drop_element(inner, "nav", "cat-nav")           # the shell owns it
    subcat = element(inner, "nav", "subcat") or ""
    if subcat:
        inner = inner.replace(subcat, "", 1)
    inner = re.sub(r"\n[ \t]*(?=\n)", "", inner).rstrip() + "\n      "
    return (
        '<main class="feed">\n'
        '      <div class="feed-inner">\n'
        '        ' + catnav + '\n'
        '        <div class="cat-layout">\n'
        + (("        " + subcat.strip() + "\n") if subcat else "")
        + '        <div class="cat-main">'
        + inner
        + '</div><!-- /cat-main --></div><!-- /cat-layout -->\n'
        '      </div>\n'
        '    </main>'
    )


# A GRAFTED CARD ARRIVES WITHOUT ITS PHOTOGRAPH. The main of a state page is
# taken from the GREY twin, and the grey tree draws a grey box where the product
# shows a picture: that is one of the six declared layer boundaries, and it is
# right. It also means every card that comes across has an empty .thumb, which is
# what shipped on the logged-out feed and on the push-permission state. A logged
# out visitor sees the same twelve events, so they see the same twelve
# photographs; the shell page is where they are written, so it is where they are
# read from.
THUMB = re.compile(r'<span class="thumb"[^>]*>')


def photograph(frag, shell):
    """Give each grafted card the photograph its event carries on the shell."""
    have = [m.group(0) for m in THUMB.finditer(shell) if "background-image" in m.group(0)]
    if not have:
        return frag
    n = [0]

    def fill(m):
        if "background-image" in m.group(0) or n[0] >= len(have):
            return m.group(0)
        tag = have[n[0]]
        n[0] += 1
        return tag

    return THUMB.sub(fill, frag)


def build(shell_name, grey_name, out_name, logged_out, title, own_main=True):
    shell = (UIV / shell_name).read_text()
    wf = (WF / grey_name).read_text()
    catnav = element(shell, "nav", "cat-nav")
    out = shell

    if own_main:
        _, _, wf_main = block(wf, "<main", "</main>")
        out = swap(out, "<main", "</main>",
                   photograph(plate(distill(neutralize(wf_main)), catnav), shell))

    if logged_out:
        _, _, wf_header = block(wf, '<header class="app-header">', "</header>")
        out = swap(out, '<header class="app-header">', "</header>", neutralize(wf_header))
        _, _, wf_nav = block(wf, '<nav class="bottom-nav"', "</nav>")
        out = swap(out, '<nav class="bottom-nav"', "</nav>", neutralize(wf_nav))
        # NOBODY SIGNED IN HAS SAVED ANYTHING. The card carried a pressed
        # bookmark into every logged-out listing, five screens, both trees: the
        # brass filled mark that means "this one is in your Favorites", shown to
        # a visitor whose header is offering them Sign up. The attribute is the
        # state, so it is set here rather than styled away.
        s, e, m = block(out, "<main", "</main>")
        out = out[:s] + m.replace('aria-pressed="true" aria-label="Saved"',
                                  'aria-pressed="false" aria-label="Save"') + out[e:]

    out = re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, out, count=1, flags=re.S)
    out = re.sub(r"Color copy of wireframes/[\w.-]+",
                 "Color copy of wireframes/" + grey_name, out, count=1)
    (UIV / out_name).write_text(out)
    return out_name


def jobs():
    for slug, suffix, logged_out, words in FEED_STATES:
        yield ("event-feed.html", "event-feed%s.html" % suffix,
               "event-feed-%s.html" % slug, logged_out,
               "Concept - Event Feed (%s)" % words, True)
    for cat in _twins.CATS:
        for slug, suffix, logged_out, words in CAT_STATES:
            # A CATEGORY LISTING DOES NOT CHANGE ITS CONTENTS WHEN NOBODY IS
            # SIGNED IN, so its logged-out success state is the base page with
            # logged-out chrome and nothing else. The grey tree drew that page
            # its own card set in Stage 05, before the card had a story line or
            # an outcome button that navigates, and taking main from there put
            # Stage-05 cards on four painted screens: no .top-txt, so no
            # story-led "why" the CJM added in Stage 04, and YES/NO that a
            # logged-out person could not press, in a product whose whole
            # inversion is that you browse and build a bet BEFORE the gate.
            # The empty / error / loading states still come from grey, because
            # there the state IS the content.
            yield ("event-feed-%s.html" % cat, "%s%s.html" % (cat, suffix),
                   "event-feed-%s-%s.html" % (cat, slug), logged_out,
                   "UI Visual - %s Events (Vault 3D, %s)" % (LABEL[cat], words),
                   slug != "logged-out")


if __name__ == "__main__":
    n = 0
    for shell_name, grey_name, out_name, logged_out, title, own_main in jobs():
        if not (WF / grey_name).exists():
            print("skip  %-42s no grey source" % out_name)
            continue
        print("built %s" % build(shell_name, grey_name, out_name, logged_out, title, own_main))
        n += 1
    print("---", "%d state page(s)" % n)
