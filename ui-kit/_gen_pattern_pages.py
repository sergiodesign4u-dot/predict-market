#!/usr/bin/env python3
"""Build the vitrine for components/patterns/: one page per pattern, plus the group page.

WHY THIS IS NOT _gen_component_pages.py WITH A FLAG
---------------------------------------------------
A component has TWO renders outside the product: a specimen (a standalone page
cut from the frozen kit) and a stand page that frames it. A pattern has no
specimen and will not get one, because step 3 deliberately took patterns out of
gate 24's corpus: gate 24 compares what a component CONTAINS in its stand against
what it contains on the screens, and a pattern contains whatever the screen puts
in it. That decision has a consequence this file is built around.

  The page a pattern gets here is the ONLY place the pattern exists outside the
  product. It is not documentation of the pattern; it is the only test of it.

So the scene is live markup, cut out of a real painted screen, not a screenshot
and not a description. Every string on it is the shipped microcopy, because it
was never retyped: the region is sliced out of ui-visual/*.html byte for byte,
with its true ancestor chain, exactly the way _extract_specimens.py slices a
specimen out of kit.html. There is no lorem on the stand because there is no
authored text on the stand.

WHAT IS COMPUTED AND WHAT IS DECLARED
-------------------------------------
Computed, and therefore incapable of going stale:
  the screens a pattern stands on      - counted from ui-visual/*.html
  the classes it owns                  - parsed from its own css
  the components it is assembled from  - the owners of every class inside the
                                         scene, read through _levels.OWNER
  the css it ships                     - the file
Declared, one line each with its reason:
  which screen the scene is cut from, and which element
  the widths the scene is framed at
  the anatomy captions, the rule and the anti-rule
A caption is prose about what a zone IS, and no map can write that. Everything
that is a fact about the product is read from the product.

OUTPUT
------
  ui-kit/patterns/<name>.html   the scene: one standalone page per pattern
  ui-kit/<name>.html            the stand page
  ui-kit/patterns.html          the group page, with the choice rule and the
                                candidates that did not reach three screens

Run AFTER _gen_component_pages.py, which writes _nav.js and _frames.js: the
scenes speak the same postMessage protocol as the specimens and are sized by the
same parent script.

    python3 ui-kit/_gen_pattern_pages.py

Idempotent. Touches nothing outside ui-kit/. No em dash.
"""
import html as _html
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
COMP = ROOT / "components"
PATDIR = COMP / "patterns"
UV = ROOT / "ui-visual"
OUT = KIT / "patterns"

sys.path.insert(0, str(ROOT / "ui-visual"))
from _theme_switch import BOOT as THEME_BOOT, button as theme_button  # noqa: E402
sys.path.insert(0, str(KIT))
import _extract_specimens as ex                                       # noqa: E402
from _levels import OWNER, PATTERNS as PATTERN_FILES                  # noqa: E402
from _gen_docs import usage_rules, inline as md_inline                # noqa: E402


def esc(s):
    return _html.escape(str(s), quote=False)


# ---------------------------------------------------------------- the six ---
# The scene source is a decision, so it carries its reason. The rule behind every
# one of them: take the screen where the pattern is MOST ITSELF, which is not
# always the canonical screen.
SCENES = [
    {
        "name": "browse-shell",
        "label": "Browse shell",
        "root": "cat-layout",
        "screen": "event-feed-crypto-empty.html",
        "pick": "div.cat-layout",
        "widths": [360, 1040],
        "depth": 2,
        "why_screen":
            "The rail is the point of this pattern and the base category pages do not show it: "
            "on those nine the markup ships <code>&lt;nav class=\"subcat\" hidden&gt;</code> and a "
            "page script fills it. Twenty four screens carry it filled and visible, and every one "
            "of them is a STATE screen, so the scene is cut from one. Nothing here is set or "
            "unset by the generator: this is that screen's markup.",
        "lead":
            "A sub-category rail beside a content column, stacked under 900px and side by side "
            "above it. It owns none of what it holds and paints none of it; it says where the two "
            "columns are.",
        "when": [
            "The screen browses a set: a category, a list of bets, a wallet ledger, a profile.",
            "There is a second, narrower axis of navigation that belongs BESIDE the content "
            "rather than above it.",
            "Fourteen different sets of content stand in the column across the 76 screens, which "
            "is the argument for a pattern rather than a component: the arrangement is stable and "
            "what it holds is not.",
        ],
        "rule": "The rail goes first in the markup and the column second, at every width. The "
                "stacked order under 900px is the source order, so a rail written after the "
                "column would land under it on a phone and beside it on a desktop.",
        "antirule": "Do not put the page's own surface on it. The two-stone plate under this "
                    "shell is in <code>components/base.css</code> with the rest of the frame, "
                    "because it is what the PAGE is made of and not what this arrangement is. A "
                    "pattern that carries a background is a component with the label filed off.",
        "anatomy": [
            (".cat-layout", None, "The shell. Column at 360, row at 900 and up, and the gap "
                                 "changes with the direction because the distance between two "
                                 "columns is not the distance between two stacked blocks."),
            (".subcat", "catnav", "The rail. Its own component: this pattern decides that it "
                                 "stands here, not what it looks like."),
            (".cat-main", None, "The content column. <code>flex:1;min-width:0</code>, and the "
                               "min-width is what stops a long word inside a card from pushing "
                               "the rail off screen."),
        ],
        "variants": [
            (".cat-layout:not(:has(.subcat))",
             "No rail, so nothing to align to: the column takes the full height instead of "
             "hanging at the top of a row it is the only member of. Specificity 0,3,0 against "
             "0,1,0, so this is decided by the selector and not by the order of the files."),
        ],
    },
    {
        "name": "detail-shell",
        "label": "Detail shell",
        "root": "ed-layout",
        "screen": "event-detail.html",
        "pick": "div.ed-layout",
        "widths": [360, 1040],
        "depth": 2,
        "why_screen":
            "The canonical detail screen, in its ordinary state. The other ten are the same "
            "arrangement holding a different content set, which is exactly what the pattern claims.",
        "lead":
            "A content column beside a sticky side panel, stacked under 760px and side by side "
            "above it. The panel is the bet panel today and the pattern does not know that.",
        "when": [
            "One subject fills the screen and one persistent action must stay reachable while a "
            "person reads about it.",
            "The action needs its own column on a desktop and its own dock at the foot of a phone.",
        ],
        "rule": "The breakpoint is 760 and not 900, and it is the panel's own: at 760 the bet "
                "panel appears and the dock disappears, which is one swap in "
                "<code>components/betpanel.css</code>. Two arrangements changing at two different "
                "widths would leave a band where the page has both or neither.",
        "antirule": "Do not reach into the column from here. <code>.ed-main</code> gets "
                    "<code>flex:1;min-width:0</code> and nothing else; its plate, its clip and its "
                    "dropped right edge are in <code>components/base.css</code>.",
        "anatomy": [
            (".ed-layout", None, "The shell. Column at 360, row at 760 and up."),
            (".ed-main", None, "The content column, and the only one of the two this pattern "
                              "sizes."),
            (".bet-panel", "betpanel", "The side panel. Sticky at 120px from the top, and that "
                                      "belongs to the panel, not here."),
        ],
        "variants": [],
    },
    {
        "name": "card-grid",
        "label": "Card grid",
        "root": "grid",
        "screen": "event-feed.html",
        "pick": "div.grid",
        "widths": [360, 1040],
        "depth": 1,
        "trim": 4,
        "why_screen":
            "The feed, which is where the track was read from. Trimmed to the first four cards of "
            "twelve so the frame stays readable; nothing else is changed, and four is enough to "
            "show the track step from one column to two to three.",
        "lead":
            "A fluid track of event cards, one column to four, with no media query at all.",
        "when": [
            "A screen lists things of one kind and the number of them is decided by the data.",
            "The items are the same shape, so a track that reflows beats a layout that is "
            "authored per width.",
        ],
        "rule": "One grid per screen. It is <code>auto-fit</code> over "
                "<code>minmax(min(100%, 300px), 1fr)</code>, so the column count is arithmetic on "
                "the available width and there is nothing to keep in step with a breakpoint.",
        "antirule": "Do not add breakpoints to it. Three of them used to sit beside this rule, "
                    "stepping 2 - 3 - 4 columns, plus a category variant at auto-fill 240px. All "
                    "four were dead: they lost to the auto-fit rule on source order, and the "
                    "variant was only ever held up by an <code>!important</code> that is now gone. "
                    "A fluid track needs no breakpoints, which is why this file has none.",
        "anatomy": [
            (".grid", None, "The track. Three declarations: it is a grid, it stretches its items to "
                           "equal height, and the columns are computed."),
            (".card", "card", "What stands in it. The card decides nothing about where it stands, "
                             "and the track decides nothing about what a card looks like."),
        ],
        "variants": [],
    },
    {
        "name": "list-head",
        "label": "List head",
        "root": "feed-head",
        "screen": "event-feed.html",
        "pick": "div.feed-head",
        "widths": [360, 900],
        "depth": 3,
        "why_screen":
            "The feed's own head, which is the widest case: a title, a live count and the full "
            "control row. Sixty nine other screens carry a thinner version of the same row.",
        "lead":
            "A title on one side, the controls that act on the list on the other, wrapping to two "
            "rows when there is no room for one.",
        "when": [
            "A list needs a name and the list needs controls, and both belong to the list rather "
            "than to the page.",
            "Twenty six of the seventy screens that carry the head have a title and nothing to "
            "sort, and the row is correct with the control side empty.",
        ],
        "rule": "The sort control lives here and not in the category band. Categories are "
                "navigation; a sort is a control over THIS list, and putting it in the band makes "
                "it look like a place you can go.",
        "antirule": "The heading's type is not here. A display face and its colour are what the "
                    "block LOOKS like, so they stay in <code>components/feed.css</code>; this file "
                    "is the row and nothing else.",
        "anatomy": [
            (".feed-head", None, "The row. <code>flex-wrap</code> with "
                                "<code>space-between</code>, so the controls drop under the title "
                                "instead of squeezing it."),
            (".feed-controls", None, "The control side. A wrapping row of its own, because two "
                                    "controls that do not fit should sit under each other and not "
                                    "shrink."),
            (".filter-menu", "filters", "What usually stands in the control side."),
        ],
        "variants": [],
    },
    {
        "name": "position-list",
        "label": "Position list",
        "root": "pos-list",
        "screen": "active-bets.html",
        "pick": "div.pos-list",
        "widths": [360, 900],
        "depth": 1,
        "why_screen":
            "My Bets, where the list is longest and the rows are the real thing rather than a "
            "loading stand-in.",
        "lead":
            "A vertical stack of bet rows at one distance. Two declarations and one gap.",
        "when": [
            "Rows of one kind stack and the distance between them is the only thing to decide.",
            "The stack also holds the loading skeletons and the resolved record block, so what "
            "stacks is not always a position row.",
        ],
        "rule": "The gap is the list's, never the row's. A row that carried its own bottom margin "
                "would double the distance the moment two lists sat one under the other, and the "
                "last row would push the plate's padding out by a step.",
        "antirule": "Do not use it as a plate. A <code>.pos</code> carries its own stone, its own "
                    "edge and its own ink; what this file decides is that the rows stack and how "
                    "far apart, which is the one thing a row cannot know about itself.",
        "anatomy": [
            (".pos-list", None, "The stack. A column flex box with one gap."),
            (".pos", "position", "The row. Its own component, whole."),
        ],
        "variants": [],
    },
    {
        "name": "action-bar",
        "label": "Action bar",
        "root": "cta-bar",
        "screen": "wallet.html",
        "pick": "div.cta-bar",
        "widths": [360, 900],
        "depth": 2,
        "why_screen":
            "The wallet, which carries the <code>.static</code> variant. The other two screens "
            "carry <code>.flat</code>, so between them the three screens show two of the three "
            "positions this bar has.",
        "lead":
            "One or two actions held at the foot of a column, sticky by default and flat where the "
            "page has no scroll to hold them against.",
        "when": [
            "A screen has one action that is the reason a person came to it, and the content above "
            "it is long enough that the action would otherwise scroll away.",
            "THREE SCREENS, WHICH IS THE THRESHOLD EXACTLY. This pattern clears the bar by one "
            "screen and that is said here rather than rounded up: it is a pattern by a margin of "
            "one, and if any of the three loses its bar it stops being one.",
        ],
        "rule": "The bar holds the actions; the buttons stay themselves. Each action is an "
                "<code>&lt;a&gt;</code> at <code>flex:1</code> holding a button at "
                "<code>width:100%</code>, so two actions split the row evenly and one fills it, "
                "without either button learning a width of its own.",
        "antirule": "Do not put a second one on a screen, and do not use it for a link that is not "
                    "the reason the screen exists. A sticky bar is the loudest thing on a phone "
                    "and a screen with two of them has told a person nothing about which to press.",
        "anatomy": [
            (".cta-bar", None, "The bar. Sticky to the foot of the column, above the bottom nav "
                               "on the stacking order."),
            ("&lt;button&gt;", "account",
             "The action, and the one part of this folder a class map cannot see: it is a bare "
             "<code>&lt;button&gt;</code> with no class at all, and it is NOT painted by "
             "<code>components/button.css</code>. Nine rules in "
             "<code>components/account.css</code> style it by descent "
             "(<code>.app-case .cta-bar button</code>), including the brass on the first child, "
             "its hover and its press. So the bar and its buttons are one component's paint, which "
             "is half of backlog item 16d: <code>account</code> is a CTA bar and a transaction "
             "list in one file."),
        ],
        "variants": [
            (".cta-bar.static", "Position only, for a page whose column does not scroll under it."),
            (".cta-bar.flat", "Position and surface: the stone, the hairline and the two rounded "
                              "corners come off, and it reads as a row at the end of the content. "
                              "The three declarations that take the surface away are in "
                              "<code>components/account.css</code> and not here, which is the one "
                              "declared paint exception of the patterns step."),
        ],
    },
]

# The compositions that did NOT reach three screens. They are on the group page
# rather than in a commit message, because an invisible candidate is one the next
# round counts again from scratch. Measured in step 3 and re-measured here.
CANDIDATES = [
    {
        "classes": ".ptabs, .ptab-bar, .ptab-panel",
        "where": "tabs",
        "screens": ["my-profile.html", "public-profile.html"],
        "note": "The profile tab strip, six occurrences over two screens. The threshold is three "
                "SCREENS and not three occurrences, on purpose: a composition that repeats inside "
                "one screen is that screen's layout, and only a third screen proves the "
                "arrangement is not a local decision. It is also half of backlog item 16b, because "
                "<code>tabs</code> is an L1 switcher and an L3 tab panel in one file.",
    },
    {
        "classes": ".opt-list",
        "where": "options",
        "screens": ["event-detail-multi.html", "event-detail-logged-out-multi.html"],
        "note": "The full outcome list, on the two multi-outcome detail screens. Those two are one "
                "screen in two auth states rather than two arrangements, so the third is further "
                "away than the count suggests. It is already governed as a rule of use: R5 says "
                "the list never stands inside a card.",
    },
]


# ------------------------------------------------------------ measurement ---
SCREENS = [p for p in sorted(UV.glob("*.html")) if p.name != "overview.html"]
SCREEN_TEXT = {p.name: p.read_text(encoding="utf-8") for p in SCREENS}


def classes_of(text):
    return {c for m in re.finditer(r'class="([^"]*)"', text) for c in m.group(1).split()}


SCREEN_CLASSES = {n: classes_of(t) for n, t in SCREEN_TEXT.items()}


def owned_classes(name):
    """Every class the pattern's own stylesheet writes."""
    body = re.sub(r"/\*.*?\*/", "", (PATDIR / (name + ".css")).read_text(encoding="utf-8"),
                  flags=re.S)
    sels = [s for s, _ in re.findall(r"([^{}]+)\{([^{}]*)\}", body) if not s.strip().startswith("@")]
    return sorted({c for s in sels for c in re.findall(r"\.([\w-]+)", s)})


def stands_on(root):
    return [n for n in sorted(SCREEN_CLASSES) if root in SCREEN_CLASSES[n]]


def subtree(html, root_class):
    """The pattern's own element, without the ancestor chain pick() kept.

    The chain matters for RENDERING (every `.app-case` descendant selector needs
    it) and says nothing about what the pattern holds, so it is kept in the scene
    and dropped everywhere a question is asked about content. Reading it as
    content is what first made every pattern here look as though it were
    assembled from `feed`, because the chain runs through `<main class="feed">`."""
    doc = ex.Spans(html)
    hit = next(i for i, n in enumerate(doc.nodes) if root_class in ex.classes(n))
    n = doc.nodes[hit]
    return html[n["start"]:n["end"]]


def assembled_from(inner, own, declared):
    """The components inside the pattern, in document order.

    Read through _levels.OWNER, the same map that computes the level and orders
    the cascade, so this cannot disagree with the ladder. A pattern's own classes
    are removed, and so is the substrate.

    THE MAP CANNOT SEE A BARE ELEMENT, and one pattern is built out of them: the
    action bar holds `<button>` with no class at all, styled by a descendant
    selector. A class map answers "which file styles this word" and there is no
    word. So the anatomy's declared owners are unioned in, and they are declared
    with a reason exactly like every other list in this system that a computation
    could not reach."""
    seen, out = set(), []
    for m in re.finditer(r'class="([^"]*)"', inner):
        for c in m.group(1).split():
            if c in own or c in seen:
                continue
            seen.add(c)
            o = OWNER.get(c)
            if o and o not in [x for x, _ in out] and o not in ("base", "course-chrome"):
                out.append((o, "." + c))
    for d in declared:
        if d and d not in [x for x, _ in out]:
            out.append((d, "declared"))
    return out


# ------------------------------------------------------------- the outline ---
def outline(html, depth):
    """The scene's markup with everything below `depth` replaced by a comment
    naming what was dropped.

    A pattern's markup is worth copying and its content is not: a person taking
    the card grid wants the track and the shape of one item, not twelve events.
    So this keeps the tree to a stated depth and says what it elided, rather than
    printing 16 KB or paraphrasing it into something nobody shipped."""
    doc = ex.Spans(html)
    nodes = doc.nodes
    if not nodes:
        return html
    root = min(range(len(nodes)), key=lambda i: nodes[i]["start"])
    level = {root: 0}
    for i, n in enumerate(nodes):
        p = n["parent"]
        if p in level:
            level[i] = level[p] + 1
    keep, cut = [], {}
    for i, n in enumerate(nodes):
        if level.get(i, 99) <= depth:
            keep.append(i)
        elif level.get(n["parent"], 99) == depth:
            cut.setdefault(n["parent"], []).append(i)
    out = []

    def render(i, ind):
        n = nodes[i]
        open_tag = html[n["start"]:html.index(">", n["start"]) + 1]
        pad = "  " * ind
        kids = [k for k in keep if nodes[k]["parent"] == i]
        if n["tag"] in ex.VOID:
            out.append(pad + open_tag)
            return
        if not kids and i not in cut:
            body = html[html.index(">", n["start"]) + 1:n["end"]]
            body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
            body = re.sub(r"\s+", " ", body).strip()
            out.append(pad + open_tag + body + "</%s>" % n["tag"])
            return
        out.append(pad + open_tag)
        for k in kids:
            render(k, ind + 1)
        if i in cut:
            kinds = {}
            for c in cut[i]:
                cls = ex.classes(nodes[c])
                key = "." + sorted(cls)[0] if cls else "<%s>" % nodes[c]["tag"]
                kinds[key] = kinds.get(key, 0) + 1
            what = ", ".join("%d x %s" % (v, k) if v > 1 else k for k, v in kinds.items())
            out.append("  " * (ind + 1) + "<!-- %s -->" % what)
        out.append(pad + "</%s>" % n["tag"])

    render(root, 0)
    return "\n".join(out)


# ------------------------------------------------------------- the scenes ---
SPRITE = {}


def build_scene(p):
    """One standalone page per pattern, cut out of a painted screen."""
    src = SCREEN_TEXT[p["screen"]]
    html = ex.pick(src, p["pick"], 1)
    # pick() was written for a block inside a body; handed a whole document it
    # returns the document's own chain as well, and the page template supplies
    # those two tags itself.
    html = re.sub(r'^<html[^>]*><body[^>]*>', "", html)
    html = re.sub(r"</body></html>$", "", html)
    if p.get("trim"):
        html = trim_children(html, p["root"], p["trim"])
    html, _ = ex.relocate(html)
    used = set(re.findall(r'href="#(i-[\w-]+)"', html))
    missing = sorted(used - set(SPRITE))
    if missing:
        raise SystemExit("%s uses undefined symbols: %s" % (p["name"], missing))
    sprite = ""
    if used:
        sprite = ('<svg width="0" height="0" aria-hidden="true" style="position:absolute">'
                  "<defs>" + "".join(SPRITE[u] for u in sorted(used)) + "</defs></svg>\n")
    (OUT / (p["name"] + ".html")).write_text(
        ex.HEAD.format(title="Pattern - " + p["label"], theme_boot=THEME_BOOT, cls="")
        + html + "\n" + ex.TAIL.format(sprite=sprite, id=p["name"]),
        encoding="utf-8")
    return html


def trim_children(html, root_class, keep):
    """Keep the first `keep` element children of the pattern root, drop the rest.

    Only ever used to stop a frame being twelve cards tall, and the page says so
    beside the frame. Nothing else about the markup is touched."""
    doc = ex.Spans(html)
    nodes = doc.nodes
    hit = next(i for i, n in enumerate(nodes) if root_class in ex.classes(n))
    kids = [i for i, n in enumerate(nodes) if n["parent"] == hit]
    if len(kids) <= keep:
        return html
    cut_from = nodes[kids[keep]]["start"]
    cut_to = nodes[kids[-1]]["end"]
    return html[:cut_from] + html[cut_to:]


# -------------------------------------------------------------- the pages ---
def frames(p):
    out = []
    for w in p["widths"]:
        out.append(
            f'<figure class="ck-scene" id="sc-{p["name"]}-{w}">'
            f'<figcaption class="ck-scene-lbl"><b>{esc(p["label"])}</b>'
            f'<span class="ck-w">{w}px</span><span class="ck-zoom" hidden></span>'
            f'<a href="patterns/{p["name"]}.html" target="_blank" rel="noopener">open on its own</a>'
            f'</figcaption>'
            f'<div class="ck-frame" style="width:{w}px">'
            f'<iframe data-specimen="{p["name"]}-{w}" src="patterns/{p["name"]}.html" '
            f'width="{w}" height="420" loading="lazy" title="{esc(p["label"])} at {w}px">'
            f"</iframe></div></figure>")
    return "\n".join(out)


def anatomy_table(p, own):
    """The caption LINKS. A row that only named the zone would leave a reader
       with the one question the page cannot answer, which is what the part looks
       like: that lives on the component's page, and this pattern decides
       placement only."""
    rows = []
    for sel, comp, note in p["anatomy"]:
        if comp:
            who = '<a href="%s.html">%s</a>' % (esc(comp), esc(comp))
        elif sel.lstrip(".") in own:
            who = '<span class="ck-kind ck-kit">this pattern</span>'
        else:
            who = "-"
        rows.append("<tr><td class='tk-role'>%s</td><td class='tk-hex'>%s</td><td>%s</td></tr>"
                    % (esc(sel), who, note))
    return ('<table class="tk-tbl ck-anat"><thead><tr><th>part</th><th>whose it is</th>'
            "<th>what it does here</th></tr></thead><tbody>%s</tbody></table>" % "".join(rows))


def variants_block(p):
    if not p["variants"]:
        return ('<p class="tk-note">No variants. The pattern has one arrangement, and a screen '
                'that needs a different one needs a different pattern.</p>')
    return "".join('<div class="ck-var"><code>%s</code><p>%s</p></div>' % (esc(sel), note)
                   for sel, note in p["variants"])


def screens_block(p, screens):
    links = "".join('<a href="../ui-visual/%s">%s</a>' % (esc(s), esc(s[:-5])) for s in screens)
    thin = ""
    if len(screens) == 3:
        thin = ('<p class="tk-note"><b>Three, which is the threshold exactly.</b> This is the '
                'thinnest proof in the folder and it is not hidden behind a phrase: one of these '
                'three losing its bar takes the pattern below the line that admitted it.</p>')
    return ('<p class="tk-note">The existence proof. A composition is a pattern here because it '
            'stands on three or more screens, so this list is not a footnote: it is the reason the '
            'file exists. Counted from the markup of all %d painted screens, not from a list.</p>'
            "%s<div class=\"ck-screens\">%s</div>" % (len(SCREENS), thin, links))


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - {label}</title>
{boot}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="{name}">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>{label}</h1>
    <p>{lead}</p>
    <div class="tk-badges">
      <span class="tk-badge">components/patterns/{name}.css</span>
      <span class="tk-badge">{nscreens} screens</span>
      <span class="tk-badge">{nmade} components</span>
      <span class="tk-badge">no specimen, by decision</span>
    </div>
    <div class="tk-jump"><a href="patterns.html">All patterns</a>{made_links}</div>
  </header>

  <section class="tk-sec" id="live">
    <h2 data-n="01">Live</h2>
    <p class="tk-note">Cut out of <a href="../ui-visual/{screen}">{screen}</a> byte for byte, with
    the ancestor chain it has there, and painted by <code>components/index.css</code> alone. Every
    string is the shipped microcopy, because none of it was retyped. {why_screen}</p>
    <p class="tk-note"><b>This is the only place the pattern exists outside the product.</b> A
    component has a specimen as well as a stand; a pattern has neither, because step 3 took patterns
    out of gate 24's corpus deliberately: that gate compares what a component contains against what
    it contains on the screens, and a pattern contains whatever the screen puts in it. So this frame
    is not an illustration of the pattern, it is the test of it.</p>
    {frames}
  </section>

  <section class="tk-sec" id="anatomy">
    <h2 data-n="02">Anatomy</h2>
    <p class="tk-note">What each part is and whose it is. A part that belongs to a component links
    to that component's page, because the answer to "how does this look" is there and not here: this
    file decides placement and nothing else.</p>
    {anatomy}
    <p class="tk-note"><b>Everything inside, read from the markup:</b> {made_note}. The class in
    brackets is what put each component in the list, through the same ownership map that computes
    the level and orders the cascade. A name here that surprises you is worth following: a class
    declared in the wrong file makes a pattern read as holding a component it has never seen.</p>
  </section>

  <section class="tk-sec" id="variants">
    <h2 data-n="03">Variants</h2>
    {variants}
  </section>

  <section class="tk-sec" id="use">
    <h2 data-n="04">When to use it</h2>
    <ul class="ck-when">{when}</ul>
    <h3 class="tk-subh">The rule</h3>
    <p class="ck-rule">{rule}</p>
    <h3 class="tk-subh">The anti-rule</h3>
    <p class="ck-antirule">{antirule}</p>
  </section>

  <section class="tk-sec" id="screens">
    <h2 data-n="05">Where it stands</h2>
    {screens}
  </section>
{constraints}
  <section class="tk-sec" id="markup">
    <h2 data-n="06">The markup</h2>
    <p class="tk-note">The scene above, to a depth of {depth}, with everything below it replaced by
    a comment naming what was elided. Copy the shape; the content is the screen's.</p>
    <details class="ck-src" open><summary>the shape, from {screen}</summary><pre>{markup}</pre></details>
  </section>

  <section class="tk-sec" id="css">
    <h2 data-n="07">The file</h2>
    <p class="tk-note">A pattern loads LAST in <code>components/index.css</code>, after every
    component, because it has to be able to place what it holds. It carries no colour at all, and
    gate 23 fails the build if one appears.</p>
    <details class="ck-src"><summary>components/patterns/{name}.css</summary><pre>{css}</pre></details>
  </section>
</main>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""


def constraints_block(name):
    """A rule of use may name a pattern as well as a component. None does today,
       and the machinery is here so that the day one does, gate 26 has a page to
       check against instead of dropping the reference in silence."""
    mine = [r for r in usage_rules() if "patterns/" + name in r["components"]]
    if not mine:
        return ""
    rows = "".join(
        "<tr><td class='tk-role'>%s</td><td>%s</td><td class='tk-hex'>%s</td><td>%s</td></tr>"
        % (esc(r["id"]), md_inline(r["title"]), esc(r["cls"]), md_inline(r["check"]))
        for r in mine)
    return """
  <section class="tk-sec" id="rules">
    <h2 data-n="08">Constraints</h2>
    <p class="tk-note">The rules of use that name this pattern, quoted from
    <a href="architecture.html#rules-of-use">Rules of use</a>. Gate 26 holds the pair.</p>
    <table class="tk-tbl ck-rules"><thead><tr><th>rule</th><th>what it says</th><th>class</th>
    <th>check it at a glance</th></tr></thead><tbody>%s</tbody></table>
  </section>
""" % rows


GROUP = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Patterns</title>
{boot}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="patterns">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>Patterns</h1>
    <p>A pattern is an arrangement of components that repeated. It owns no colour, has no level, no
    specimen and no states, and it loads last in <code>components/index.css</code> because it has to
    be able to place what it holds.</p>
    <div class="tk-badges">
      <span class="tk-badge">{n} patterns</span>
      <span class="tk-badge">components/patterns/</span>
      <span class="tk-badge">{total} screens covered</span>
      <span class="tk-badge">three screens to exist</span>
    </div>
    <div class="tk-jump"><a href="overview.html">The system</a><a href="architecture.html">Architecture</a>
      <a href="inventory.html">Inventory</a></div>
  </header>

  <section class="tk-sec" id="choose">
    <h2 data-n="01">Which of the two to reach for</h2>
    <p class="tk-note">This is the part of the page that decides something. The list below is the
    inventory; this is the rule, and it is written with this product's own cases because a rule
    stated in the abstract gets read as advice.</p>
    <div class="ck-choice">
      <div class="ck-choice-col">
        <h3 class="tk-subh">Take the pattern whole</h3>
        <p>When the screen is <b>doing the job the arrangement is for</b>, whatever it puts inside
        it. Favorites, My Bets, Wallet, Notifications and the four category feeds all browse a set,
        so all of them take <a href="browse-shell.html">the browse shell</a> and then fill the
        column with fourteen different things. The arrangement is the answer; the content is the
        variable.</p>
        <p>The test is whether you would describe the screen with the pattern's own sentence. "A
        rail beside a column" describes Wallet. If it does, take the whole thing, including the
        parts you do not think you need: the 900px switch and the
        <code>:not(:has(.subcat))</code> fallback are what make it work on the screen that has no
        rail yet.</p>
      </div>
      <div class="ck-choice-col">
        <h3 class="tk-subh">Assemble from components</h3>
        <p>When the arrangement would be a <b>coincidence</b>. The system pages (404, 500,
        maintenance) put one state block on a plate, and a state block on a plate is not a browse
        shell that happens to be empty: R8 says a system screen carries the frame and not the
        navigation, so reaching for the shell there would import a rail the screen is not allowed
        to have.</p>
        <p>The second case is a count of one. <code>.feed-hero</code> stands on a single screen and
        <code>.cc-banner</code> on a single screen, so neither is a pattern and neither gets one: a
        composition used once is that screen's layout, and giving it a shared file makes the next
        person believe it repeats.</p>
      </div>
    </div>
    <p class="tk-note ck-threshold"><b>The condition for existing is three screens.</b> Not three
    occurrences: three distinct files that carry the composition. A thing that repeats twelve times
    inside one screen is that screen's layout, and only a third screen proves the arrangement is not
    a local decision. Six compositions cleared it and two did not, and the two are named at the foot
    of this page rather than forgotten.</p>
  </section>

  <section class="tk-sec" id="all">
    <h2 data-n="02">The six</h2>
    <p class="tk-note">Each card frames the pattern live at 360, because the page it links to is the
    only place the pattern exists outside the product.</p>
    <div class="ck-pat-cards">{cards}</div>
  </section>

  <section class="tk-sec" id="candidates">
    <h2 data-n="03">Candidates, waiting for a third screen</h2>
    <p class="tk-note">Compositions that repeat on exactly two screens. They are NOT patterns and
    nothing here is extracted, but they are on this page rather than in a commit message, because a
    candidate nobody can see is one the next round counts again from scratch.</p>
    {candidates}
  </section>
</main>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""


def build():
    global SPRITE
    SPRITE = ex.sprite_symbols((KIT / "kit.html").read_text(encoding="utf-8"))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    declared = {p["name"] for p in SCENES}
    have = {f.stem for f in PATDIR.glob("*.css")}
    if declared != have:
        raise SystemExit("patterns/ holds %s, this file knows %s. A pattern with no entry here "
                         "has no page, and gate 27 will say so." % (sorted(have), sorted(declared)))

    manifest = []
    for p in SCENES:
        own = owned_classes(p["name"])
        scene = build_scene(p)
        screens = stands_on(p["root"])
        if len(screens) < 3:
            raise SystemExit("%s stands on %d screens, which is not a pattern"
                             % (p["name"], len(screens)))
        inner = subtree(scene, p["root"])
        made = assembled_from(inner, set(own), [c for _, c, _ in p["anatomy"]])
        css = (PATDIR / (p["name"] + ".css")).read_text(encoding="utf-8")
        made_links = "".join('<a href="%s.html">%s</a>' % (m, m) for m, _ in made)
        # Every attribution is traceable to the class that made it, because two
        # of the six read as holding a component nobody would expect: the detail
        # shell "contains feed" through .grid-l, the chart's grid line declared
        # in feed.css, and the position list "contains profile" through
        # .pos-status. Both are backlog item 17, a class in the wrong file, and
        # the vitrine found them again without being asked. A bare component
        # name would have read as a mistake in this generator.
        made_note = ", ".join("%s (%s)" % (m, via) for m, via in made)
        page = PAGE.format(
            boot=THEME_BOOT, name=p["name"], label=esc(p["label"]), lead=p["lead"],
            nscreens=len(screens), nmade=len(made), made_links=made_links,
            made_note=made_note,
            screen=esc(p["screen"]), why_screen=p["why_screen"], frames=frames(p),
            anatomy=anatomy_table(p, set(own)), variants=variants_block(p),
            when="".join("<li>%s</li>" % w for w in p["when"]),
            rule=p["rule"], antirule=p["antirule"],
            screens=screens_block(p, screens),
            constraints=constraints_block(p["name"]),
            depth=p["depth"], markup=esc(outline(inner, p["depth"])), css=esc(css))
        (KIT / (p["name"] + ".html")).write_text(page, encoding="utf-8")
        manifest.append({"name": p["name"], "label": p["label"], "screens": screens,
                         "made": [m for m, _ in made], "via": dict(made),
                         "own": own, "widths": p["widths"]})

    cards = "".join(
        '<a class="ck-pat-card" href="{n}.html">'
        '<span class="ck-thumb ck-pat-thumb"><iframe src="patterns/{n}.html" width="360" '
        'height="900" loading="lazy" tabindex="-1" aria-hidden="true" title=""></iframe></span>'
        '<b>{l}</b><code>components/patterns/{n}.css</code>'
        '<span class="ck-pat-meta">{s} screens &middot; {m}</span></a>'.format(
            n=m["name"], l=esc(m["label"]), s=len(m["screens"]),
            m=", ".join(m["made"]) or "no component of its own")
        for m in manifest)

    cand = "".join(
        '<div class="ck-cand"><code>{c}</code>'
        '<p>{note}</p><p class="ck-cand-where">{n} screens: {links}. Styled in '
        '<a href="{w}.html">components/{w}.css</a>.</p></div>'.format(
            c=esc(c["classes"]), note=c["note"], n=len(c["screens"]), w=c["where"],
            links=", ".join('<a href="../ui-visual/%s">%s</a>' % (s, s[:-5])
                            for s in c["screens"]))
        for c in CANDIDATES)

    (KIT / "patterns.html").write_text(
        GROUP.format(boot=THEME_BOOT, n=len(manifest),
                     total=len({s for m in manifest for s in m["screens"]}),
                     cards=cards, candidates=cand), encoding="utf-8")

    (OUT / "index.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    write_inventory(manifest)
    print("wrote %d pattern pages + patterns.html, %d scenes into ui-kit/patterns/"
          % (len(manifest), len(manifest)))
    return manifest


# --------------------------------------------------------- the inventory ---
# The inventory described one level of the system. A generated block is added to
# it rather than hand-written rows, for the reason every generated span in this
# repo carries: a table of screens per pattern is a fact the markup answers, and
# a copy of it goes stale on the next screen. Five columns, so six pipes, which
# is under the seven _fill_inventory.py uses to recognise a component row: the
# two generators write into one file and neither can eat the other's work.
INV_START = "<!-- patterns:start -->"
INV_END = "<!-- patterns:end -->"


def inventory_block(manifest):
    rows = "\n".join(
        "| **%s** | `patterns/%s.css` | [%s](../%s.html) | %d | %s |"
        % (m["label"], m["name"], m["name"], m["name"], len(m["screens"]),
           ", ".join("`%s`" % x for x in m["made"]) or "-")
        for m in manifest)
    return """%s
## Patterns (Design System step 3)

The second level of the system, and the reason this table now describes both. A pattern is an
arrangement that repeated on three or more screens. It has no level, no specimen and no states: it
owns placement and nothing else, and it loads last in `components/index.css` so that it can place
what it holds. The screens column is the existence proof, counted from the markup of all %d painted
screens.

| Pattern | CSS file | Page | Screens | Assembled from |
|---|---|---|---|---|
%s

Two compositions repeat on exactly two screens and are therefore NOT patterns: `.ptabs` / `.ptab-bar`
/ `.ptab-panel` (`tabs`, on `my-profile` and `public-profile`) and `.opt-list` (`options`, on the two
multi-outcome detail screens). They are listed on [patterns](../patterns.html) so that the next count
starts from what the last one found.
%s""" % (INV_START, len(SCREENS), rows, INV_END)


def write_inventory(manifest):
    path = KIT / "docs" / "inventory.md"
    text = path.read_text(encoding="utf-8")
    block = inventory_block(manifest)
    if INV_START in text:
        text = re.sub(re.escape(INV_START) + r".*?" + re.escape(INV_END), lambda _: block,
                      text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n---\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    build()
