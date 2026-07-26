#!/usr/bin/env python3
"""Put the navigation back into the painted screens.

    python3 ui-visual/_relink.py            # write
    python3 ui-visual/_relink.py --dry-run  # report only

Where a link goes is structure, and structure is owned by wireframes/. The
Stage 08 colour pass did not honour that: `neutralize()` in _apply_theme.py and
_apply_family.py flattened every product `.html` link to `#` while grafting a
grey fragment into a painted shell, so the coloured product came out with no
navigation at all. The wireframes stayed clickable end to end; their colour
copies did not.

This restores the target of each anchor and changes nothing else. It is not a
translation table anyone has to keep in step with the product: every target is
read at run time out of the wireframes or out of another painted screen, so
when a flow moves in wireframes/ the next run moves it here too.

Six passes, each one taking over where the one before it has nothing to say.

  1. The twin, aligned. The two files are colour copies of each other, so their
     anchors come in the same order. The sequences are aligned with difflib on a
     tolerant key (aria-label, class without state words, visible text) and a
     target is taken only from a block the aligner reports as EQUAL. That is
     what makes it safe where the painted screen deliberately differs: an
     injected category bar, a distilled control, the redesigned profile. Those
     land in a non-equal block and are left alone.

  2. The twin, by key. An anchor the aligner had to skip may still take a
     target by key, but only when every anchor with that key in the twin points
     at the same page. One YES on a feed of binary cards is unambiguous; a YES
     on a feed that mixes binary and multi-outcome cards is not.

  3. Shared chrome, from another painted screen. Half the painted pages have a
     header the grey twin never had: the colour pass grafted the full shell
     onto screens that are standalone in grey (deposit, sign-in, win, loss, the
     system pages). There is nothing to read the targets from, so they are read
     sideways instead: pages whose header, bottom nav or footer is the same
     markup form a group, and inside a group an anchor takes the target its
     twins already carry. Identical markup means the anchor sequences line up
     index by index, so this is a copy, not a guess.

  4. Cards, from the card next to them. The painted feed carries events the
     grey feed does not, and the four category feeds are generated here, so
     their cards have no twin at all. A card's links go to its own event, and
     which event page that is follows from the card: binary or multi-outcome.
     The rule is not written down here, it is measured from the cards that the
     passes before it did resolve, first in the same article, then among the
     article's siblings on the page, then across the painted tree.

  5. The painted tree, by key. The group in pass 3 has to be strict about
     shape, and a header whose notification list holds different sample events
     is a different shape, so a few anchors fall out of every group. They are
     picked up by the same argument as pass 2, run over the painted tree
     instead of over one twin: what does this key resolve to on the screens
     that do resolve it. It runs after the cards, because a card's YES is the
     one key in the product that genuinely means two pages, and by now it is
     already answered from its own card.

  6. What only the painted tree has. Three blocks were drawn in the colour
     pass and exist in no wireframe, so no amount of reading can say where they
     point. That is a product decision, and the six links it covers are written
     down in PAINTED_ONLY below with the reason.

Two things stay dead afterwards, both on purpose
    A link the wireframe itself leaves at `#` (Terms, the social row, the
    orphan destinations Leaderboard and Help Center), and a link to a screen
    that exists in grey but was never painted (the category state pages, which
    only the hidden grey screen tree points at). Pointing either at a page that
    is not there would trade a dead link for a broken one.

Idempotent: an anchor that already has a target is never touched, so a second
run reports 0 changes. No em dash.
"""
import collections
import difflib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
UV = ROOT / "ui-visual"
WF = ROOT / "wireframes"

# The four category feeds are the one place where the two trees disagree on a
# file name: grey calls the page politics.html, the colour pass named it after
# the family it belongs to. Both directions are needed, one to find the twin
# and one to translate the targets read out of it.
CATS = ("politics", "crypto", "culture", "general")
TWIN = {"event-feed-%s.html" % c: "%s.html" % c for c in CATS}
RENAME = {"%s.html" % c: "event-feed-%s.html" % c for c in CATS}

A_TAG = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.S)
HREF = re.compile(r'href="([^"]*)"')
SIDEBAR = re.compile(r'<aside class="sidebar" id="rmSidebar">.*?</aside>', re.S)
ARTICLE = re.compile(r"<article\b[^>]*>.*?</article>", re.S)
STATE_WORDS = {"active", "on", "sel", "current"}
# The shared chrome. A region is a piece of markup the shell puts on every
# screen unchanged, which is exactly the condition pass 3 needs.
REGIONS = (
    ("header", re.compile(r'<header class="app-header">.*?</header>', re.S)),
    ("bottom nav", re.compile(r'<nav class="bottom-nav".*?</nav>', re.S)),
    ("footer", re.compile(r"<footer\b.*?</footer>", re.S)),
)
# Two cards are the same kind of card when they resolve the same way. The only
# distinction the feed makes is binary against multi-outcome, and the option
# rows are what tells them apart.
MULTI = re.compile(r'class="[^"]*\bopt\b|opt-row')

# The blocks the colour pass invented, by the class of the anchor. Nothing can
# be read for these: they are on no wireframe, so where they go is a decision,
# not a fact, and it is written here rather than guessed by a rule.
#   hh-name  the hot list beside the hero names five events, and the painted
#            tree has one binary event page for all of them
#   hh-all   "See all hot events" is the whole feed
#   all      the sub-filter marks the page you are on, and every other chip in
#            that row links to its own feed, so this one links to this feed
# Each rule is (the class on the anchor, the text in it or None for any, the
# block it has to sit in or None for anywhere) -> where it goes.
PAINTED_ONLY = (
    (("hh-name", None, None), "event-detail.html"),
    (("hh-all", None, None), "event-feed.html"),
    (("", "All", re.compile(r'<nav class="feed-subfilter".*?</nav>', re.S)), "event-feed.html"),
)


def key(attrs, inner):
    """What makes an anchor recognisable across two files.

    Not the icon: the colour pass renamed the sprite symbols (i-heart became
    i-bookmark-b), so an icon-only anchor is recognised by its aria-label.
    Not a state class either, since the active page differs per file.
    """
    aria = (re.search(r'aria-label="([^"]*)"', attrs) or ["", ""])[1]
    cls = (re.search(r'class="([^"]*)"', attrs) or ["", ""])[1]
    cls = " ".join(sorted(w for w in cls.split() if w not in STATE_WORDS))
    txt = " ".join(re.sub(r"<[^>]+>", " ", inner).split())
    return "%s|%s|%s" % (aria, cls, txt)


def anchors(text):
    """Every anchor in document order: its key, its target, where the target is."""
    out = []
    for m in A_TAG.finditer(text):
        h = HREF.search(m.group(1))
        out.append({
            "key": key(m.group(1), m.group(2)),
            "href": h.group(1) if h else "",
            "span": (m.start(1) + h.start(1), m.start(1) + h.end(1)) if h else None,
            "at": m.start(),
        })
    return out


def shape(fragment):
    """The markup of a fragment with everything page-specific taken out.

    Two fragments with the same shape are the same chrome: same elements in the
    same order, differing only in where the links go and which item is marked as
    the page you are on.
    """
    f = HREF.sub('href=""', fragment)
    f = re.sub(r'\s*aria-current="[^"]*"', "", f)
    f = re.sub(r'class="([^"]*)"',
               lambda m: 'class="%s"' % " ".join(w for w in m.group(1).split()
                                                 if w not in STATE_WORDS), f)
    return re.sub(r"\s+", " ", f).strip()


def translate(href, painted):
    """A wireframe target as the painted tree spells it, or "" if it has none."""
    base, _, frag = href.partition("#")
    base = base.split("?")[0]
    if not base.endswith(".html"):
        return ""
    base = RENAME.get(base, base)
    if base not in painted:
        return ""
    return base + ("#" + frag if frag else "")


class Screen(object):
    def __init__(self, path):
        self.path = path
        self.src = path.read_text(encoding="utf-8")
        # The course sidebar exists only on this side. Blanking it keeps the
        # anchor sequence comparable with the twin while the offsets stay valid
        # for writing back.
        self.masked = SIDEBAR.sub(lambda m: " " * len(m.group(0)), self.src)
        self.anchors = anchors(self.masked)
        self.fix = {}                       # anchor index -> new target

    def dead(self, i):
        a = self.anchors[i]
        return a["span"] and i not in self.fix and a["href"] in ("#", "")

    def target(self, i):
        """Where anchor i goes once this run is written out."""
        return self.fix.get(i) or self.anchors[i]["href"]

    def region(self, rx):
        """(fragment, anchor indexes inside it) for the first match of rx."""
        m = rx.search(self.masked)
        if not m:
            return None, []
        return m.group(0), [i for i, a in enumerate(self.anchors)
                            if m.start() <= a["at"] < m.end()]

    def write(self):
        if not self.fix:
            return 0
        src = self.src
        for i in sorted(self.fix, reverse=True):
            s, e = self.anchors[i]["span"]
            src = src[:s] + self.fix[i] + src[e:]
        if "--dry-run" not in sys.argv:
            self.path.write_text(src, encoding="utf-8")
        return len(self.fix)


def from_twin(sc, painted, report):
    """Passes 1 and 2: read the targets out of the grey twin."""
    twin = WF / TWIN.get(sc.path.name, sc.path.name)
    if not twin.exists():
        report["no twin"].append(sc.path.name)
        return
    theirs = anchors(twin.read_text(encoding="utf-8"))

    sm = difflib.SequenceMatcher(None, [a["key"] for a in sc.anchors],
                                 [a["key"] for a in theirs], autojunk=False)
    aligned = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        # An equal-length replace between two equal blocks is the same control
        # under a new label: the colour pass renamed the class (the Related
        # events link became .related-more) or reworded the item. Same count, in
        # the same place, between two anchors that both matched, so it is still
        # a copy. An insertion or a deletion is not, and is skipped.
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            for d in range(i2 - i1):
                aligned[i1 + d] = theirs[j1 + d]["href"]

    unique = {}
    for a in theirs:
        unique.setdefault(a["key"], set()).add(a["href"])
    unique = {k: v.pop() for k, v in unique.items() if len(v) == 1}

    for i in range(len(sc.anchors)):
        if not sc.dead(i):
            continue
        t = translate(aligned.get(i, ""), painted)
        how = "1 twin aligned"
        if not t:
            t = translate(unique.get(sc.anchors[i]["key"], ""), painted)
            how = "2 twin by key"
        if t:
            sc.fix[i] = t
            report[how] += 1


def from_chrome(screens, report):
    """Pass 3: an anchor in shared chrome takes the target its twins carry."""
    for name, rx in REGIONS:
        groups = collections.defaultdict(list)
        for sc in screens:
            frag, idx = sc.region(rx)
            if frag:
                groups[shape(frag)].append((sc, idx))
        for members in groups.values():
            width = len(members[0][1])
            if any(len(idx) != width for _, idx in members):
                continue                    # same shape must mean same anchors
            for pos in range(width):
                seen = {sc.target(idx[pos]) for sc, idx in members}
                seen = {t for t in seen if t.endswith(".html")}
                if len(seen) != 1:
                    continue                # no agreement, so no donation
                target = seen.pop()
                for sc, idx in members:
                    if sc.dead(idx[pos]):
                        sc.fix[idx[pos]] = target
                        report["3 chrome " + name] += 1


def by_key(screens, report):
    """Pass 5: what this anchor means on the screens that already resolved it.

    A strict majority, not unanimity, because a handful of screens legitimately
    send the same control somewhere else: "See all notifications" goes to
    notifications.html on 38 screens and to notifications-empty.html on the
    three that show the empty inbox. Requiring one answer everywhere would let
    those three veto the other 38 and leave the control dead.

    Running after the cards is what makes a majority safe. The one key with a
    genuinely split meaning is YES and NO on a feed card, and by the time this
    pass runs those are already resolved from their own card.
    """
    seen = collections.defaultdict(collections.Counter)
    for sc in screens:
        for i, a in enumerate(sc.anchors):
            t = sc.target(i)
            if t.endswith(".html"):
                seen[a["key"]][t] += 1
    settled = {}
    for k, c in seen.items():
        top, n = c.most_common(1)[0]
        if n * 2 > sum(c.values()):
            settled[k] = top
    for sc in screens:
        for i, a in enumerate(sc.anchors):
            if sc.dead(i) and a["key"] in settled:
                sc.fix[i] = settled[a["key"]]
                report["5 tree by key"] += 1


def from_cards(screens, report):
    """Pass 4: a card's links go where the cards around it go."""
    cards = []                              # (screen, anchor indexes, kind, targets)
    for sc in screens:
        for m in ARTICLE.finditer(sc.masked):
            idx = [i for i, a in enumerate(sc.anchors) if m.start() <= a["at"] < m.end()]
            if not idx:
                continue
            kind = "multi" if MULTI.search(m.group(0)) else "binary"
            cards.append([sc, idx, kind,
                          {sc.target(i) for i in idx if sc.target(i).endswith(".html")}])
    everywhere = collections.defaultdict(collections.Counter)
    for sc, idx, kind, tg in cards:
        for t in tg:
            everywhere[kind][t] += 1
    for sc, idx, kind, tg in cards:
        if not any(sc.dead(i) for i in idx):
            continue
        # the card itself, then the cards beside it, then every card of its kind
        siblings = {t for s2, i2, k2, t2 in cards
                    if s2 is sc and k2 == kind for t in t2}
        common = everywhere[kind].most_common(1)
        pick = (tg if len(tg) == 1 else
                siblings if len(siblings) == 1 else
                {common[0][0]} if common else set())
        if len(pick) != 1:
            continue
        target = pick.pop()
        for i in idx:
            if sc.dead(i):
                sc.fix[i] = target
                report["4 card"] += 1


def painted_only(screens, report):
    """Pass 6: the three blocks that exist in colour and nowhere else."""
    for sc in screens:
        for (cls, txt, block), target in PAINTED_ONLY:
            inside = None
            if block:
                m = block.search(sc.masked)
                if not m:
                    continue
                inside = (m.start(), m.end())
            for i, a in enumerate(sc.anchors):
                if not sc.dead(i):
                    continue
                aria, acls, atxt = a["key"].split("|", 2)
                if acls != cls or (txt is not None and atxt != txt):
                    continue
                if inside and not inside[0] <= a["at"] < inside[1]:
                    continue
                sc.fix[i] = target
                report["6 painted only"] += 1


def main():
    painted = {p.name for p in UV.glob("*.html")}
    screens = [Screen(p) for p in sorted(UV.glob("*.html"))]
    report = collections.Counter()
    report["no twin"] = []

    for sc in screens:
        from_twin(sc, painted, report)
    from_chrome(screens, report)
    from_cards(screens, report)
    by_key(screens, report)
    painted_only(screens, report)

    total = sum(sc.write() for sc in screens)
    touched = sum(1 for sc in screens if sc.fix)
    print("%s: %d links restored on %d of %d screens"
          % ("would relink" if "--dry-run" in sys.argv else "relinked",
             total, touched, len(screens)))
    for k in sorted(k for k in report if k[0].isdigit()):
        print("   %-18s %d" % (k, report[k]))

    dead = collections.Counter()
    for sc in screens:
        for i in range(len(sc.anchors)):
            if sc.dead(i):
                dead[sc.anchors[i]["key"]] += 1
    print("still dead: %d anchors, %d distinct" % (sum(dead.values()), len(dead)))
    for k, n in dead.most_common(6):
        print("   %4d  %s" % (n, k[:88]))
    if report["no twin"]:
        print("no wireframe twin (nothing to read): %s" % ", ".join(report["no twin"]))


if __name__ == "__main__":
    main()
