#!/usr/bin/env python3
"""Render ui-kit/docs/*.md as pages of the vitrine.

THE DEFECT. Every stage of this course renders its reasoning: ia/docs/sitemap.md
has ia/sitemap.html, voice/docs/voice.md has voice/voice.html. Stage 09 was the
one that did not. Its four documents, 144 KB of them, existed only as markdown,
and the vitrine already LINKED one: thirty-nine component pages point at
docs/coverage.md, which a browser downloads rather than draws. A link into a file
the browser will not render is a dead end with a href on it.

WHY A GENERATOR AND NOT FOUR HAND-BUILT PAGES. These documents change every step;
architecture.md gained four sections in the last two. A hand copy is stale one
commit later, and this repo has paid for that twice (the roadmap true in one file
and false in twenty-one, coverage.md disagreeing with the css headers). One
computation feeds both, and gate 21 fails the build when the page is not what the
markdown renders to.

WHAT IT IS NOT. Not a markdown library: it reads the subset these four documents
use, which is headings, paragraphs, GFM tables, bullet and numbered lists, block
quotes, fenced code, `code`, **bold**, and nothing else. A construct that is not
in the documents is not implemented, because an implementation nothing exercises
is a guess. If a document grows one, this is where it goes.

THE LOOK IS THE VITRINE'S OWN. A page about the system is painted by the system:
components/index.css plus _page.css, the kit side panel, the theme switch. It
reads its own tokens, which is also the cheapest test there is of whether a long
document is legible in both themes.

TWO THINGS THE RENDER ADDS, both read out of the text and neither invented:
  a swatch beside a colour literal, because tokens-audit.md is 24 tables of hex;
  a link on a file name the vitrine has a page for, because architecture.md names
      one in almost every paragraph.

ORDER. Run this AFTER _gen_component_pages.py, which writes docs/coverage.md.
Rendering first means rendering the previous coverage table, and gate 21 says so
in the same breath.

Usage:
    python3 ui-kit/_gen_docs.py            # write the pages
    python3 ui-kit/_gen_docs.py --check    # report which would change
"""
import html as _html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
DOCS = KIT / "docs"
COMP = ROOT / "components"

sys.path.insert(0, str(ROOT / "ui-visual"))
from _theme_switch import BOOT as THEME_BOOT  # noqa: E402

# slug -> the label in the side panel and the line on the hub card. The order is
# the order a person meets them: what the system IS, what it was read out of,
# what it contains, what each part reaches.
PAGES = [
    ("architecture", "Architecture",
     "How the system is put together, what each level may hold, and where a change goes."),
    ("tokens-audit", "Tokens audit",
     "The reading the system was built from: every value the painted product had, and what it meant."),
    ("inventory", "Inventory",
     "Every component, its css file, its page and the screens it stands on."),
    ("coverage", "Coverage",
     "Every class, and how many painted screens carry it. A zero is not a verdict."),
]
LABEL = {slug: label for slug, label, _ in PAGES}

COLOUR = re.compile(r"^(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\))$")
FILEREF = re.compile(r"^(?:components/([\w-]+)\.css|ui-kit/([\w-]+)\.html|"
                     r"(?:ui-kit/)?docs/([\w-]+)\.md)$")


def esc(s):
    """Quotes are escaped too, and that is not cosmetic. These documents quote
       markup: tokens-audit.md has a code block containing
       <link rel="stylesheet" href="_theme.css">, and with the quote left alone
       the rendered page carries a string that every regex-based checker in this
       repo reads as a real href. Gate 4 reported a path that does not resolve
       and gate 9 reported a page loading a stylesheet deleted in step 7, both
       times pointing at a sentence. The browser draws &quot; as a quote either
       way; only the checkers can tell the difference."""
    return _html.escape(s, quote=True)


def slugify(text):
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "section"


def code_html(raw):
    """One `code` span. A colour gets its colour shown; a file the vitrine has a
       page for gets a link to it. Everything else is a code span and no more."""
    body = "<code>%s</code>" % esc(raw)
    if COLOUR.match(raw.strip()):
        # the value IS the datum, so it goes on the element (the same idiom
        # tokens.html uses for a role swatch)
        return '<i class="tk-dot" style="background:%s"></i>%s' % (esc(raw.strip()), body)
    m = FILEREF.match(raw.strip())
    if m:
        stand, page, doc = m.groups()
        target = None
        if stand and (KIT / (stand + ".html")).exists():
            target = stand + ".html"
        elif page and (KIT / (page + ".html")).exists():
            target = page + ".html"
        elif doc and doc in LABEL:
            target = doc + ".html"
        if target:
            return '<a class="tk-doc-ref" href="%s">%s</a>' % (target, body)
    return body


def inline(text):
    """Inline markup. Code spans are lifted out FIRST and put back last, so a **
       or a < inside one is a character and not a rule."""
    spans = []

    def keep(m):
        spans.append(m.group(1))
        return "\0%d\0" % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", keep, text)
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text, flags=re.S)
    return re.sub(r"\0(\d+)\0", lambda m: code_html(spans[int(m.group(1))]), text)


def table(rows):
    """A GFM table. The first row is the head, the second is the rule that says
       it was one, and it is dropped."""
    def cells(line):
        return [c.strip() for c in line.strip().strip("|").split("|")]

    head = cells(rows[0])
    out = ['<table class="tk-tbl"><thead><tr>']
    out += ["<th>%s</th>" % inline(c) for c in head]
    out.append("</tr></thead><tbody>")
    for line in rows[2:]:
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in cells(line)) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def blocks(lines):
    """The document, one block at a time. Returns html plus the heading tree the
       contents column is built from."""
    out, toc, i, n = [], [], 0, 0
    open_section = False

    def close():
        if open_section:
            out.append("</section>")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            # a rule between sections is what the section border already draws
            i += 1
            continue

        m = re.match(r"^(#{2,4})\s+(.*)$", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2)
            slug = slugify(text)
            if level == 2:
                close()
                n += 1
                out.append('<section class="tk-sec" id="%s">' % slug)
                out.append('<h2 data-n="%02d">%s</h2>' % (n, inline(text)))
                open_section = True
                toc.append((2, slug, re.sub(r"<[^>]+>", "", inline(text))))
            else:
                out.append('<h%d id="%s" class="tk-doc-h%d">%s</h%d>'
                           % (level, slug, level, inline(text), level))
                if level == 3:
                    toc.append((3, slug, re.sub(r"<[^>]+>", "", inline(text))))
            i += 1
            continue

        if stripped.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("```"):
                j += 1
            out.append('<pre class="tk-doc-pre">%s</pre>'
                       % esc("\n".join(lines[i + 1:j])))
            i = j + 1
            continue

        if stripped.startswith("|"):
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            out.append('<div class="tk-doc-tbl">%s</div>' % table(lines[i:j]))
            i = j
            continue

        if stripped.startswith("> "):
            j, quoted = i, []
            while j < len(lines) and lines[j].strip().startswith(">"):
                quoted.append(lines[j].strip().lstrip(">").strip())
                j += 1
            out.append('<blockquote class="tk-doc-quote">%s</blockquote>'
                       % inline(" ".join(quoted)))
            i = j
            continue

        bullet = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if bullet:
            ordered = bool(re.match(r"^\d+\.$", bullet.group(2)))
            items, j = [], i
            while j < len(lines):
                b = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[j])
                if b and bool(re.match(r"^\d+\.$", b.group(2))) == ordered:
                    items.append([b.group(3)])
                    j += 1
                elif items and lines[j].startswith(("  ", "\t")) and lines[j].strip():
                    items[-1].append(lines[j].strip())          # a wrapped item
                    j += 1
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append('<%s class="tk-doc-list">%s</%s>'
                       % (tag, "".join("<li>%s</li>" % inline(" ".join(it)) for it in items), tag))
            i = j
            continue

        para, j = [], i
        while j < len(lines) and lines[j].strip() and not re.match(
                r"^\s*(#{2,4}\s|[-*]\s|\d+\.\s|\||>|```|---\s*$)", lines[j]):
            para.append(lines[j].strip())
            j += 1
        if not para:                       # a line no rule claimed; keep the text
            para, j = [stripped], i + 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
        i = j

    close()
    return "".join(out), toc


def contents(toc):
    rows = ['<details class="tk-doc-toc" open><summary>Contents</summary><nav>']
    for level, slug, text in toc:
        cls = "tk-doc-toc-2" if level == 2 else "tk-doc-toc-3"
        rows.append('<a class="%s" href="#%s">%s</a>' % (cls, slug, esc(text)))
    rows.append("</nav></details>")
    return "".join(rows)


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
<body data-kit-page="doc-{slug}">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap tk-doc">
  <header class="tk-hero">
    <h1>{title}</h1>
    <p>{lead}</p>
    <div class="tk-badges">
      <span class="tk-badge">{words} words</span>
      <span class="tk-badge">{sections} sections</span>
      <span class="tk-badge">docs/{slug}.md</span>
    </div>
    <div class="tk-jump">{jump}</div>
  </header>
  <div class="tk-doc-cols">
    {toc}
    <div class="tk-doc-body">{body}</div>
  </div>
  <p class="tk-doc-src">Rendered from <code>ui-kit/docs/{slug}.md</code> by
  <code>ui-kit/_gen_docs.py</code>. The markdown is the source; this page is the
  reading copy, and gate 21 fails the build when the two disagree.</p>
</main>

<script src="_nav.js"></script>
</body>
</html>
"""


def render(slug):
    """One markdown file, one page. Pure: takes a slug, returns the html."""
    text = (DOCS / (slug + ".md")).read_text(encoding="utf-8")
    lines = text.split("\n")
    title = re.sub(r"^#\s+", "", lines[0]).strip()

    # the lead is the paragraph under the title, and it does not repeat in the
    # body: a hero that says the same thing twice is a hero and a first paragraph
    i, lead = 1, []
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
        lead.append(lines[i].strip())
        i += 1

    body, toc = blocks(lines[i:])
    jump = "".join('<a href="%s.html">%s</a>' % (s, lab)
                   for s, lab, _ in PAGES if s != slug)
    jump += '<a href="overview.html">The system</a>'
    return PAGE.format(
        boot=THEME_BOOT, slug=slug, label=LABEL[slug], title=esc(title),
        lead=inline(" ".join(lead)), words=len(text.split()),
        sections=sum(1 for lv, _, _ in toc if lv == 2),
        jump=jump, toc=contents(toc), body=body)


def main():
    check = "--check" in sys.argv
    have = {p.stem for p in DOCS.glob("*.md")}
    known = {s for s, _, _ in PAGES}
    if have != known:
        raise SystemExit("_gen_docs: docs/ holds %s, the table knows %s. A document "
                         "with no row here has no page, and gate 21 will say so."
                         % (sorted(have), sorted(known)))
    changed = 0
    for slug, _, _ in PAGES:
        page = KIT / (slug + ".html")
        new = render(slug)
        old = page.read_text(encoding="utf-8") if page.exists() else ""
        if new != old:
            changed += 1
            print("%-22s %s" % (slug + ".html", "new" if not old else "rewritten"))
            if not check:
                page.write_text(new, encoding="utf-8")
    print("---", "%d of %d page(s) %s" % (changed, len(PAGES),
                                          "would change" if check else "written"))


if __name__ == "__main__":
    main()
