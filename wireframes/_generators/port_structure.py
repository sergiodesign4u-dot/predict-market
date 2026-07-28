#!/usr/bin/env python3
"""
port_structure.py  -  bring the structure back to the tree that owns it.

THE DEFECT. The rule in CLAUDE.md is that wireframes/ owns structure and copy and
ui-visual/ owns the visual layer only. Stage 08 broke it quietly: the Event Detail
was REDESIGNED while it was being painted, and the redesign stayed in the paint.
Measured on the <main> of every screen with a twin, 55 of 72 differ; event-detail
carries 792 tags in colour against 570 in grey, and the extra 222 are not styling.
They are a whole AMM market panel with its price-by-size table, a chart rebuilt as
head / plot / axis / range, a rules-and-context tab split where the grey tree has
two flat sections, a share-and-save cluster, an odds bar, a real <input> where the
grey tree has a <span> pretending to be a field, and thumbnails and a "see all"
link in the related list.

So the source of truth was the copy, and the copy was the source. Nothing checked
it, which is the real finding: a rule with no gate behind it is a preference.

WHAT THIS DOES. Takes the painted <main> and writes it into the grey twin, minus
the four things that genuinely belong to the paint:

  1. the plate wrappers .cat-layout, .cat-main, .feed-inner. A wrapper whose only
     job is to draw a stone plate is not structure; porting it would put an empty
     div in the wireframe to record a shadow.
  2. the event photograph (style="background-image:..."). The grey tree keeps its
     "thumbnail placeholder" element, which is the same element with the picture
     taken off.
  3. the sprite. The painted tree draws an icon with <use href="#id"> against an
     inline <symbol> set; the grey tree draws raw paths. One mechanism per tree,
     so every <use> is resolved back into the paths it points at.
  4. the colour. Which is the whole point: the grey rules below are derived from
     components/ by keeping the layout properties and dropping every colour,
     shadow, gradient and font-family. A grey box is the painted component with
     its paint scraped off, so the wireframe shows the same shapes in the same
     places and none of the finish.

The three regions this does NOT touch are the header, the bottom nav and the
footer. They differ too, and their differences are written down as declared
exceptions in wireframes/_conventions.md and checked by gate 18, so drift fails
the build instead of being discovered a stage later.

Idempotent: it reads the painted twin and rewrites the grey main from it, so a
second run produces the same bytes. NEVER writes to ui-visual/.

Usage:
    python3 wireframes/_generators/port_structure.py            # port
    python3 wireframes/_generators/port_structure.py --check    # report only
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GREY = os.path.join(ROOT, "wireframes")
PAINT = os.path.join(ROOT, "ui-visual")
COMP = os.path.join(ROOT, "components")

# Divs that exist so the Vault can draw a plate. Unwrapped, children kept.
WRAPPERS = {"cat-layout", "cat-main", "feed-inner"}

# Classes the grey tree already styles, whose rules were written for markup the
# port replaces. "Already styled" is the wrong question for these: the category
# bar used to hang off the device beside <main> as li > button, and the painted
# tree puts it inside <main> as li > a > button in a strip that scrolls sideways.
# The old grey rules still match something, so nothing looked missing, and the
# feed came out 14px wider than the phone it was drawn for. Listed by hand and
# kept short on purpose: a general "restyle everything in main" rule would be
# stable too, and would quietly redraw the whole wireframe from the product.
RESTYLE = {"cat-nav"}

VOID = {"br", "img", "input", "use", "path", "circle", "meta", "link",
        "polyline", "source", "rect", "line", "hr", "ellipse", "stop"}

MARKER = "/* ---- ported from the painted twin by port_structure.py ---- */"

# ---------------------------------------------------------------- markup ----


def region(html, tag, cls=None):
    """The outer html of the first <tag> (optionally with class) and its span."""
    pat = r"<%s\b[^>]*?>" % tag if cls is None else r'<%s\b[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls)
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


def unwrap(html, names):
    """Drop the tags of a wrapper div, keep everything inside it."""
    out, stack = [], []
    pos = 0
    for m in re.finditer(r"<(/?)([a-z0-9]+)([^>]*?)(/?)>", html):
        close, tag, attrs, self = m.groups()
        out.append(html[pos:m.start()])
        pos = m.end()
        void = bool(self) or tag in VOID
        if close:
            drop = stack.pop() if stack else False
            if not drop:
                out.append(m.group(0))
            continue
        cl = re.search(r'class="([^"]*)"', attrs)
        classes = set(cl.group(1).split()) if cl else set()
        drop = tag == "div" and bool(classes & names)
        if not void:
            stack.append(drop)
        if not drop:
            out.append(m.group(0))
    out.append(html[pos:])
    return "".join(out)


def symbols_of(html):
    """id -> the markup inside its <symbol>, so a <use> can be resolved."""
    out = {}
    for m in re.finditer(r'<symbol id="([\w-]+)"[^>]*>(.*?)</symbol>', html, re.S):
        out[m.group(1)] = m.group(2).strip()
    return out


def inline_sprite(html, symbols):
    def sub(m):
        body = symbols.get(m.group(1))
        return body if body is not None else m.group(0)
    return re.sub(r'<use href="#([\w-]+)"\s*/?>(?:</use>)?', sub, html)


def strip_photo(html):
    """The photograph is content in colour and paint in grey: the wireframe keeps
       the element and loses the picture. A width is a datum and stays."""
    def sub(m):
        keep = [d for d in m.group(1).split(";")
                if d.strip() and not d.strip().startswith("background-image")]
        return ' style="%s"' % ";".join(keep) if keep else ""
    html = re.sub(r'\s*style="([^"]*)"', sub, html)
    # An <img> is the other way a photograph travels, and the grey tree had none:
    # 104 wireframes, zero image elements, because a wireframe draws a box where a
    # picture goes. The port brought four across (the featured hero, the brand
    # tile, two pieces of how-it-works art) and one of them was 1400px wide, which
    # is also how the overflow at 380px arrived. The container stays and keeps its
    # grey fill; only the picture goes.
    html = re.sub(r"<img\b[^>]*>", "", html)
    # A colour can also ride on an SVG presentation attribute, which no style
    # rule and no stylesheet link would ever show. The hero gradient carried
    # stop-color="var(--color-action)" and an axis carried stroke="var(--text-brass)":
    # six live references to the token file, inside the tree that must not know
    # the token file exists. A hardcoded brand hex is the same defect wearing a
    # literal, and the grey tree's own rule is monochrome outline icons only.
    # fill="none" and fill="currentColor" are structure, not colour, and stay.
    return re.sub(r'\s(fill|stroke|stop-color|flood-color|lighting-color)='
                  r'"(?:var\(--[^"]*|#[0-9a-fA-F]{3,8})"', "", html)


def drop_outer_catnav(html):
    """The category bar is not new, it MOVED: the grey tree hangs it off the
       device beside <main> and the painted tree puts it inside, above the feed
       head. Porting the painted main without this leaves the page carrying two
       of them, one styled and one not, which is worse than the divergence it was
       fixing. Only the copy outside <main> goes."""
    m = re.search(r'<main\b', html)
    if not m or 'class="cat-nav"' not in html[:m.start()]:
        return html
    nav, a, b = region(html[:m.start()], "nav", "cat-nav")
    if not nav:
        return html
    return html[:a] + html[b:]


def seed_chart(html, paint_html):
    """A wireframe draws its data, it does not compute it.

       The painted chart ships with points="" and an empty x-axis and fills both
       from a script on load; the grey chart it replaced had its squiggle typed
       into the markup. Port the painted structure as-is and the wireframe loses
       its chart line, which is the one thing that section is there to show.

       So the default series is read OUT of the painted script (the range button
       carrying .sel, which is 'all') and written into the markup statically. Read,
       not retyped: change the data in the product and re-run, and the wireframe
       follows. The five multi-outcome lines get the same treatment."""
    def pts(series):
        n = len(series)
        return " ".join("%.1f,%.1f" % (i / (n - 1) * 300, 100 - v)
                        for i, v in enumerate(series))

    m = re.search(r"'all':\s*\{s:\[([\d,\s]+)\],\s*x:\[([^\]]+)\]\}", paint_html)
    if m:
        series = [int(v) for v in m.group(1).split(",") if v.strip()]
        labels = re.findall(r"'([^']+)'", m.group(2))
        html = html.replace('<polyline points=""/>', '<polyline points="%s"/>' % pts(series), 1)
        html = re.sub(r'(<div class="ed-xaxis"[^>]*>)(</div>)',
                      lambda mm: mm.group(1) + "".join("<span>%s</span>" % t for t in labels)
                      + mm.group(2), html)

    multi = re.search(r"var DATA=\[\s*((?:\[[\d,\s]+\],?\s*)+)\]", paint_html)
    if multi and 'class="ml-line" points=""' in html:
        rows = [[int(v) for v in r.split(",") if v.strip()]
                for r in re.findall(r"\[([\d,\s]+)\]", multi.group(1))]
        for row in rows:
            html = html.replace('<polyline class="ml-line" points=""/>',
                                '<polyline class="ml-line" points="%s"/>' % pts(row), 1)
    return html


def port_main(grey_html, paint_html):
    src, _, _ = region(paint_html, "main")
    dst, a, b = region(grey_html, "main")
    if not src or not dst:
        return grey_html, False
    new = seed_chart(strip_photo(inline_sprite(unwrap(src, WRAPPERS), symbols_of(paint_html))),
                     paint_html)
    out = grey_html[:a] + new + grey_html[b:]
    if 'class="cat-nav"' in new:
        out = drop_outer_catnav(out)
    if out == grey_html:
        return grey_html, False
    return out, True


# ------------------------------------------------------------------- css ----
# A grey box is the painted component with its finish taken off. So the rules are
# not invented here: they are read out of components/, kept only where they place
# something, and re-drawn in the wireframe palette. Anything that makes a surface
# look like a surface is dropped.
KEEP = re.compile(r"^(display|flex|flex-\w+|grid|grid-\w+|gap|row-gap|column-gap|order|"
                  r"align-\w+|justify-\w+|place-\w+|padding|padding-\w+|margin|margin-\w+|"
                  r"width|height|min-width|min-height|max-width|max-height|inset|"
                  r"top|right|bottom|left|position|overflow|overflow-\w+|box-sizing|"
                  r"font-size|font-weight|font-style|text-transform|letter-spacing|"
                  r"line-height|text-align|white-space|text-overflow|word-break|"
                  r"list-style|list-style-type|aspect-ratio|table-layout|"
                  r"grid-template-columns|grid-template-rows|grid-column|grid-row|"
                  r"vertical-align|writing-mode|transform-origin|content|visibility)$")
DROP_VALUE = re.compile(r"var\(|calc\(|clamp\(|color-mix\(")

# The wireframe palette, from wireframes/_conventions.md. Nothing else may appear.
INK, LINE, FILL, SOFT = "#222", "#999", "#dcdcdc", "#555"


def tokens():
    """primitive -> literal, so a ported rule can be written without var()."""
    src = open(os.path.join(COMP, "tokens.css"), encoding="utf-8").read()
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    flat = dict(re.findall(r"(--[\w-]+)\s*:\s*([^;}]+)", src))
    for _ in range(4):                       # resolve var() chains
        for k, v in list(flat.items()):
            flat[k] = re.sub(r"var\((--[\w-]+)\)",
                             lambda m: flat.get(m.group(1), m.group(0)), v).strip()
    return flat


TOK = tokens()


def literal(value):
    v = re.sub(r"var\((--[\w-]+)(?:,[^)]*)?\)",
               lambda m: TOK.get(m.group(1), ""), value).strip()
    return v if v and not DROP_VALUE.search(v) else None


def split_selector(sel):
    """Split a selector LIST on its top-level commas.

       Not sel.split(","): a comma also separates the arguments of :is(), :where()
       and :not(), and cutting there produces ".ed-chart-head :is(h2" with an
       unbalanced paren. A browser drops a rule it cannot parse AND everything
       after it in the same sheet, so one bad selector silenced the whole chart
       layout below it and the axes rendered as running text. Same shape of defect
       gate 16 exists for, one tree over."""
    parts, depth, cur = [], 0, ""
    for ch in sel:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def blocks_of(body):
    """(at_rule_or_None, selector, declarations) for every rule in a file.

       The first cut deleted @media blocks before reading anything, which is why
       the ported feed came out 14px wider than a 380px phone: the hero stacks at
       620px and that instruction lives nowhere else. A breakpoint is layout, and
       layout is exactly what a wireframe is for."""
    out = []
    i = 0
    while i < len(body):
        at = body.find("@media", i)
        if at == -1:
            for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", body[i:]):
                out.append((None, m.group(1).strip(), m.group(2)))
            break
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", body[i:at]):
            out.append((None, m.group(1).strip(), m.group(2)))
        head_end = body.find("{", at)
        cond = " ".join(body[at:head_end].split())
        depth, j = 1, head_end + 1
        while j < len(body) and depth:
            if body[j] == "{":
                depth += 1
            elif body[j] == "}":
                depth -= 1
            j += 1
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", body[head_end + 1:j - 1]):
            out.append((cond, m.group(1).strip(), m.group(2)))
        i = j
    return out


def rules_for(classes):
    """Every rule in components/ whose subject is one of these classes, reduced
       to what it PLACES. Cascade order is the import order of index.css."""
    order = [ln.split('"')[1][:-4] for ln in
             open(os.path.join(COMP, "index.css"), encoding="utf-8").read().splitlines()
             if ln.startswith("@import")]
    out = []
    for name in order:
        path = os.path.join(COMP, name + ".css")
        if not os.path.exists(path):
            continue
        body = re.sub(r"/\*.*?\*/", "", open(path, encoding="utf-8").read(), flags=re.S)
        for cond, sel, decls in blocks_of(body):
            if ":hover" in sel or ":focus" in sel or "::" in sel or "[" in sel:
                continue
            wanted = []
            for part in split_selector(sel):
                subject = re.findall(r"\.([\w-]+)", part.split(":")[0])
                if subject and subject[-1] in classes:
                    wanted.append(part)
            if not wanted:
                continue
            sel = ", ".join(wanted)
            keep = []
            for d in decls.split(";"):
                if ":" not in d:
                    continue
                prop, _, val = d.partition(":")
                prop = prop.strip()
                if not KEEP.match(prop):
                    continue
                lit = literal(val)
                if lit:
                    keep.append("%s: %s" % (prop, lit))
            if keep:
                # The scope hooks and the plate wrappers are not in the grey tree,
                # so a selector that names one can never match there. Dropping
                # .app-case is obvious; dropping .feed-inner is the same fact one
                # step along, and missing it left nine rules in the page that
                # nothing could ever match, including the one that makes the
                # category strip scroll instead of push.
                short = ", ".join(strip_scope(p) for p in split_selector(sel))
                out.append(((cond, short), "; ".join(keep)))
    return out


def strip_scope(sel):
    sel = re.sub(r"^dialog\.app-dialog\s+", "", re.sub(r"^\.app-case\s+", "", sel))
    for w in WRAPPERS:
        sel = re.sub(r"(^|\s)\." + re.escape(w) + r"\s*[>]?\s*", r"\1", sel)
    return " ".join(sel.split()) or "*"


def grey_block(classes):
    """One idempotent style block: layout from components/, colour from the
       wireframe palette. A ported block reads as a grey box and nothing else."""
    lines = [MARKER,
             "    /* Layout taken from components/, every colour replaced by the",
             "       wireframe palette. See wireframes/_generators/port_structure.py. */"]
    seen = set()
    plain, media = [], []
    for (cond, sel), decls in rules_for(classes):
        if (cond, sel, decls) in seen:
            continue
        seen.add((cond, sel, decls))
        (plain if cond is None else media).append((cond, sel, decls))
    for _, sel, decls in plain:
        lines.append("    %s { %s; }" % (sel, decls))
    # Breakpoints last, so a narrow rule still beats the wide one it corrects.
    for cond in sorted({c for c, _, _ in media}, reverse=True):
        lines.append("    %s {" % cond)
        for c, sel, decls in media:
            if c == cond:
                lines.append("      %s { %s; }" % (sel, decls))
        lines.append("    }")
    # The few things that need an edge to read as a box at all.
    lines += [
        "    .ed-oddsbar .track, .md-bar { background: %s; }" % FILL,
        "    .ed-oddsbar .fill { background: %s; }" % SOFT,
        "    .ed-act, .rules-tab, .ed-range button { border: 1px solid %s;" % LINE,
        "      background: #eee; color: %s; font-size: 10px; }" % INK,
        "    .rules-tab.sel, .ed-range button.sel { background: %s; font-weight: bold; }" % FILL,
        "    .market-box, .md-table { border: 1px solid #ccc; }",
        "    .market-head { padding: 6px 8px; background: #eee; cursor: pointer; }",
        "    .ms-label, .md-sub, .rules-note, .ed-chart-now, .bp-cash { color: %s; }" % SOFT,
        "    .rel-thumb { width: 40px; height: 40px; border: 1px solid %s;" % LINE,
        "      background: %s; flex: 0 0 40px; }" % FILL,
        "    .ed-yaxis span, .ed-xaxis span { font-size: 9px; color: %s; }" % SOFT,
        "    .ed-plot { border: 1px solid #ccc; }",
        "    .rules-panel[hidden] { display: none; }",
    ]
    # A generated stylesheet has to be checked by the thing that generates it. One
    # unbalanced paren above cost every rule below it, and the only symptom was an
    # axis that read as running text, which looks like a missing rule and is not.
    for ln in lines:
        if "{" in ln and ln.count("(") != ln.count(")"):
            raise SystemExit("port_structure: unbalanced selector, would kill the "
                             "rest of the sheet:\n  " + ln)
    return "\n".join(lines)


BLOCK_RE = re.compile(re.escape(MARKER) + r".*?(?=\n\s*</style>)", re.S)


def apply_css(html, classes):
    block = grey_block(classes)
    if MARKER in html:
        return BLOCK_RE.sub(lambda _: block, html)
    return html.replace("</style>", block + "\n  </style>", 1)


def classes_in(html):
    out = set()
    for m in re.findall(r'class="([^"]*)"', html):
        out |= set(m.split())
    return out


def styled(html):
    """Classes the page's own grey-box css already covers. The block this script
       writes is removed first, or the second run would ask a smaller question
       than the first and shrink its own output: the block styles the classes,
       so counting it makes them look already covered."""
    # The block is cut out of the DOCUMENT, not out of the joined css: four pages
    # carry two <style> elements, and splitting the joined text at the marker
    # threw away the whole second element with it. Those four then reported their
    # own already-styled classes as uncovered and grew a longer block every run.
    css = "\n".join(re.findall(r"<style>(.*?)</style>", BLOCK_RE.sub("", html), re.S))
    return {c for c in re.findall(r"\.([\w-]+)", css)}


def main():
    check = "--check" in sys.argv
    changed = ported = 0
    for name in sorted(os.listdir(GREY)):
        if not name.endswith(".html"):
            continue
        twin = os.path.join(PAINT, name)
        if not os.path.exists(twin):
            continue
        gpath = os.path.join(GREY, name)
        grey = open(gpath, encoding="utf-8").read()
        paint = open(twin, encoding="utf-8").read()
        out, moved = port_main(grey, paint)
        if moved:
            ported += 1
        now = classes_in(region(out, "main")[0] or "")
        new_classes = (now - styled(out)) | (now & RESTYLE)
        if new_classes:
            out = apply_css(out, new_classes)
        if out != grey:
            changed += 1
            print("%-46s %s%s" % (name, "main " if moved else "",
                                  "+%d classes" % len(new_classes) if new_classes else ""))
            if not check:
                open(gpath, "w", encoding="utf-8").write(out)
    print("---", "%d page(s), %d main(s) %s" %
          (changed, ported, "would change" if check else "rewritten"))


if __name__ == "__main__":
    main()
