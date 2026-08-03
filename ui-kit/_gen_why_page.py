#!/usr/bin/env python3
"""Build ui-kit/why.html, the guide: why the system looks like this, and how to use it.

WHAT IT IS FOR. Every other page in the vitrine answers a question someone
already knows to ask. This one is for the person who has never seen the system:
it says why the product looks the way it does, where each value came from, which
of the four doors to walk through, and what to do when nothing fits.

WHY IT IS A GENERATOR AND NOT A HAND-WRITTEN PAGE, and this is the load-bearing
reason rather than a habit. This stage is the LAST READER of
concept/docs/references.md. Stage 06 wrote it; nothing between then and here has
opened it; and if its four references do not arrive on this page they are not
deferred, they are lost, because no later stage has any reason to go looking. So
the reference table is not retyped here. It is PARSED out of the Source index of
references.md, and the five attribute pairs are parsed out of concept.md, and
gate 28 fails the build if a row exists in either document and not on this page.

  A source that only a generator reads is still read. A source that only a
  sentence mentions is a file waiting to be forgotten.

WHAT IS DECLARED. One line per attribute saying what it MEANS IN THE SYSTEM and
where it is visible, and the anatomy of the choice rule. Those are judgements
about this system and no document holds them. Everything factual, which is the
reference names, their roles, the anxiety each answers and the attribute
headings, is read from the two documents.

Sources, all four cited on the page itself and checked by gate 28:
  concept/docs/references.md   the visual language: base, borrows, rejections
  concept/docs/concept.md      the designer taste and the five attribute pairs
  DESIGN.md                    the shipped token spec
  ui-kit/docs/architecture.md  the contract

    python3 ui-kit/_gen_why_page.py

Idempotent. Touches nothing but ui-kit/why.html. No em dash.
"""
import html as _html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
CONCEPT = ROOT / "concept" / "docs"

sys.path.insert(0, str(ROOT / "ui-visual"))
from _theme_switch import BOOT as THEME_BOOT  # noqa: E402

# The four files this page is built out of. Every one is cited on the page, and
# gate 28 checks that the citation is still there: the first of them has no other
# reader left in the project, so a link lost in an edit is a file lost for good.
SOURCES = [
    ("concept/docs/references.md", "The visual language: which product is the base, which technique "
     "was borrowed from where, and what was rejected on sight. This page is its last reader."),
    ("concept/docs/concept.md", "The designer taste, the five attribute pairs, and the honest "
     "divergence where the shipped accent left the one the taste locked."),
    ("DESIGN.md", "The shipped spec: the graphite ramp, the brass, the type, the material."),
    ("ui-kit/docs/architecture.md", "The contract: what the system is, and where a change goes."),
]


def esc(s):
    return _html.escape(str(s), quote=False)


# ------------------------------------------------------- read the documents ---
def references():
    """The Source index table of references.md, parsed. Four sources and a
       rejection, each with the role it plays and the anxiety line it serves."""
    text = (CONCEPT / "references.md").read_text(encoding="utf-8")
    out = []
    for line in text[text.index("## Source index"):].split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] in ("Source", "---") or set(cells[0]) <= set("-: "):
            continue
        out.append({"name": cells[0], "uuid": cells[1], "role": cells[2], "serves": cells[3]})
    return out


def attributes():
    """The five attribute pairs, parsed out of concept.md's `### A<n> - ...`
       headings plus the "From the data" line under each. The heading is the
       pair; the data line is what stops it being an adjective."""
    text = (CONCEPT / "concept.md").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"^### (A(\d) - (.+))$", text, re.M):
        body = text[m.end():]
        body = body[:body.find("\n### ") if "\n### " in body else len(body)]
        d = re.search(r"\*\*From the data:\*\*(.+?)(?=\n- \*\*)", body, re.S)
        out.append({"key": "A" + m.group(2), "pair": m.group(3).strip(),
                    "data": re.sub(r"\s+", " ", d.group(1)).strip() if d else ""})
    return out


# WHAT EACH PAIR MEANS IN THE SYSTEM, and where a person can go and see it. This
# is the declared half, and it is declared because it is a judgement about this
# system rather than a fact in a document: no file says "A1 became the two-stone
# emboss". Each row is concrete on purpose. "Warm and human" would be worse than
# an empty row, because an empty row admits it has no answer and an abstract one
# pretends it does.
MEANS = {
    "A1": ("The canvas is graphite `#0f1013` and not white, and there is exactly ONE accent on it: "
           "matte brass `#c7a24e`. Contrast does the work colour usually does, so the page can be "
           "quiet and still feel live. Every surface is a two-stone emboss (a lit lip on top, a "
           "cast shadow under) rather than a flat fill, which is where the aliveness comes from now "
           "that the glow and the dot-grid of the earlier direction are gone.",
           [("tokens.html#colour", "the graphite ramp and the brass"),
            ("tokens.html#material", "the two-stone plates and the bevels")]),
    "A2": ("Brass appears on identity, on the active state and on ONE call to action per zone, and "
           "nowhere else. That is not restraint for its own sake: an accent used as decoration "
           "stops meaning \"press this\", and a money product that shouts reads as a casino. The "
           "rule is executable, not advisory, and R1 in the contract is the counted version of it.",
           [("architecture.html#rules-of-use", "R1, one primary action per zone"),
            ("button.html", "the one brass button")]),
    "A3": ("Numbers are always mono, because a proportional figure looks like prose and a mono one "
           "looks like a reading. The market state is a pool and a depth curve, never an order "
           "book. The odds bar carries the outcome colour so the YES / NO buttons can stay quiet "
           "tinted shapes instead of two loud fills.",
           [("oddsbar.html", "the bar that carries the colour"),
            ("yesno.html", "the quiet YES / NO pair"),
            ("market.html", "a pool and a curve, not a book")]),
    "A4": ("The funds line sits NEXT TO the action rather than in a legal wall at the foot of the "
           "page, and it is drawn on neutral stone with no accent and no colour: a reassurance that "
           "is styled to persuade reads as marketing, and the whole point is that it reads as fact.",
           [("trustbar.html", "the trust strip and its cards"),
            ("notice.html", "the plain line beside the action")]),
    "A5": ("A card leads with a real event photograph, masked so it bleeds into the graphite, and "
           "carries a one-line \"why\" under the question. A grey placeholder is not allowed to "
           "ship: the whole attribute is that the market is attached to something happening, and a "
           "grey box is the visual form of \"this question came from nowhere\".",
           [("card.html", "the event card"),
            ("hero.html", "the featured hero")]),
}

# The four doors. The fourth is listed apart from the third on purpose, and the
# reason is behavioural rather than tidy: a person assembling a screen for the
# first time goes looking for PERMISSION, and meets a prohibition only after they
# have already done it their own way. A rule filed inside "the rules" is a rule
# found too late.
DOORS = [
    ("Which component do I take?", "overview.html",
     "Every component file, its page and the level it sits at, in the order the cascade loads them. "
     "Start here when you know what the thing is."),
    ("Is the arrangement already built?", "patterns.html",
     "Six compositions that repeated on three or more screens, each framed live. Start here when "
     "you know what the SCREEN is, before you know what is in it."),
    ("What are the rules?", "architecture.html",
     "The contract: two token levels, what a component may read, where a change goes, and the "
     "reasoning behind each. Read once, then read the row you need."),
    ("What am I not allowed to do?", "architecture.html#rules-of-use",
     "Nine rules of use: how many of a thing a screen may carry and where it may not stand. This "
     "is a door of its own and not a paragraph of the one above it, because nobody looks for a "
     "prohibition until after they have broken it."),
]

CHAIN = [
    ("A pixel of the shipped plate", None,
     "The system was not designed on a blank page. It was READ OUT of screens that already worked: "
     "every colour in it was sampled from the painted product rather than picked, which is why the "
     "graphite steps are 11.7 L* apart instead of a round number."),
    ("The audit that wrote down what each value was doing", "tokens-audit.html",
     "Twenty four tables of hex, and beside every value the declarations it was read from. This is "
     "the step where a colour stopped being a number and became a ROLE: not \"#1c1f24\" but \"the "
     "surface a chip sits on\"."),
    ("The direction locked at Concept", "why.html#language",
     "Vault: graphite, one matte brass, reserved green and red. The reference table above is where "
     "that came from, and it is the only part of the chain that is a judgement rather than a "
     "measurement."),
    ("The theme, which is the proof the roles are real", "tokens.html#contrast",
     "A light theme was built over the same roles, and NOT ONE PRIMITIVE was redefined. That is the "
     "test a rebrand cannot run: the ground inverts, the ink inverts, and the action still has to "
     "read as the action, which is only writable if the reason a colour is in a place is stored "
     "somewhere. It found twelve holes, and every one of them was a component reading a raw value."),
    ("`components/tokens.css`, in two levels", "tokens.html",
     "A primitive is a value; a role is why that value is in that place. A component may read a "
     "role and never a colour primitive, and gate 13 fails the build when one does."),
]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Why the system is like this</title>
{boot}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="why">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap tk-why">
  <header class="tk-hero">
    <h1>Why the system is like this</h1>
    <p>The guide. Not a list of what exists, which is what
    <a href="overview.html">the system</a> is for, but the four things a person needs before they
    touch it: why the product looks the way it does, where its values came from, which door to walk
    through, and what to do when nothing fits.</p>
    <div class="tk-badges">
      <span class="tk-badge">{nattr} attributes</span>
      <span class="tk-badge">{nref} references</span>
      <span class="tk-badge">4 doors</span>
      <span class="tk-badge">read, not invented</span>
    </div>
    <div class="tk-jump"><a href="overview.html">The system</a><a href="patterns.html">Patterns</a>
      <a href="architecture.html">Architecture</a>
      <a href="architecture.html#rules-of-use">What you may not do</a></div>
  </header>

  <section class="tk-sec" id="language">
    <h2 data-n="01">Why the system looks like this</h2>
    <p class="tk-note">Five attribute pairs, decided at Concept. Each is "this, not that", each
    traces to a line of research rather than to a mood, and each turned into something you can point
    at in the system. The left column is the pair as
    <code>concept/docs/concept.md</code> states it; the middle is what it became here; the right is
    where you can go and see it.</p>
    {attributes}

    <h3 class="tk-subh">The brand plate</h3>
    <p class="tk-note">Every value below is the shipped one, from <code>DESIGN.md</code>, resolved
    live by the page you are reading rather than printed as a swatch: if a token moved, this moved
    with it.</p>
    {plate}

    <h3 class="tk-subh">Where the language came from</h3>
    <p class="tk-note">One base reference, two borrowed techniques, one on watch and one whole
    family rejected on sight. Read from the Source index of
    <code>concept/docs/references.md</code>, which after Concept has no other reader in this
    project: if a row is missing here it is missing everywhere, and gate 28 fails the build when
    that happens.</p>
    {refs}
    <p class="tk-note ck-divergence"><b>One divergence, named rather than buried.</b> The taste
    locked electric violet as the brand accent and acid lime as the highlight, from the MELEE
    reference. The product ships matte brass on graphite. That was a designer decision taken on the
    stand on 2026-07-16, not a drift: brass answers the same complaint the violet was chosen for
    (an accent with no contrast against its ground) while reading as weighty rather than neon, which
    serves A2 and the documented "this looks like crypto, so it looks like a scam" fear better than
    lime did. Anyone re-reading the taste table in <code>concept/docs/concept.md</code> should treat
    brass as final.</p>
  </section>

  <section class="tk-sec" id="provenance">
    <h2 data-n="02">Where the values came from</h2>
    <p class="tk-note">The short answer is that none of them was chosen at this stage. The system
    was read out of a product that already worked, and every step of that reading is still on
    disk.</p>
    <ol class="ck-chain">{chain}</ol>
    <p class="tk-note"><b>And the contrast figures are measured, not computed.</b> That belongs
    here rather than in a footnote, because it is part of where a value comes from.
    <code>getComputedStyle()</code> returns what the author wrote, and modern css lets an author
    write a colour that is not a literal: <code>color-mix(in oklab, ...)</code> comes back verbatim,
    and a regex reading it as sRGB bytes reported a pale brass banner as near black. Every ratio in
    this system is taken by handing the computed string to a 2D canvas, filling one pixel and
    reading it back, with the ancestor stack composited for alpha. A figure that did not come from
    that path does not go in the token file.</p>
  </section>

  <section class="tk-sec" id="use">
    <h2 data-n="03">How to use it</h2>
    <p class="tk-note">Four questions, four doors. They are four and not three on purpose: the last
    one is the question nobody thinks to ask.</p>
    <div class="ck-doors">{doors}</div>
    <h3 class="tk-subh">And when you are not sure which</h3>
    <ol class="ck-order">
      <li><b>Look for a pattern first.</b> If the screen you are building is doing the job an
      arrangement already exists for, take the whole arrangement, including the parts you think you
      do not need.</li>
      <li><b>No pattern: assemble from components.</b> Two screens sharing a shape is a coincidence
      until a third one turns up. Building it out of components is the correct answer, not a
      fallback.</li>
      <li><b>No component either: that is an order for the SYSTEM, not an exception for the
      screen.</b> A screen that styles itself is the one failure this whole structure exists to
      prevent, and it is the failure that looks most like getting the work done. A new component is
      a css file, an <code>@import</code> at the position the cascade computes, a stand page and a
      row in the inventory. It is five minutes of work and it is never the wrong call.</li>
    </ol>
  </section>

  <section class="tk-sec" id="grow">
    <h2 data-n="04">How to grow it</h2>
    <p class="tk-note">One sentence, and the full version is written at the next step: <b>a new
    thing is built in the system first and used on a screen second, never the other way round.</b>
    The order is the whole rule, because a thing built on a screen and lifted afterwards arrives
    carrying that screen's assumptions, and nobody ever finds them again. The mechanics are in
    <a href="architecture.html#how-to-add-a-component">how to add a component</a> and
    <a href="architecture.html#how-to-add-a-pattern-which-is-four-things-and-not-five">how to add a
    pattern</a>.</p>
  </section>

  <section class="tk-sec" id="backlog">
    <h2 data-n="05">The system backlog</h2>
    <p class="tk-note"><b>Filled at step 7, and filled the only way that produces a true list.</b>
    Step 7 built <a href="../ui-visual/terms.html">Terms of Service</a>, the first page of a TYPE
    this system had never drawn, under one rule: nothing is added to the system while a screen is
    being assembled. A missing component, state, token or copy line becomes a row instead. A system
    that grows a part every time it meets a new page has not been tested by that page, it has been
    edited by it.</p>
    <p class="tk-note">Nine rows came out of one screen, and the shape of them is the answer. The
    SHELL of an unfamiliar page type cost nothing: the plate, the header, the theme, the focus ring
    and the four nav slots arrived by linking one stylesheet. Everything missing was in the BODY of
    a long document, which is the one thing this product had never asked for. The largest is a
    token: the reading column is 800px, which at the body size is about 122 characters against the
    60 to 75 that <code>DESIGN.md</code> decided.</p>
    <p class="tk-note">The list is <a href="backlog.html">the system backlog</a>. The product's own
    open questions stay where they are, in <code>docs/backlog.md</code>: what a component is missing
    and what a product has not decided are two lists with two readers.</p>
  </section>

  <section class="tk-sec" id="sources">
    <h2 data-n="06">What this page was built from</h2>
    <p class="tk-note">Four documents, and the citation is the point rather than the courtesy. The
    first of them has had no reader since Concept: nothing in the stages between then and now opens
    it, so if its contents had not been brought here they would not have been deferred, they would
    have been lost. Gate 28 checks that every reference it names still appears above.</p>
    <ul class="ck-sources">{sources}</ul>
  </section>
</main>

<script src="_nav.js"></script>
</body>
</html>
"""


def attribute_rows(attrs):
    rows = []
    for a in attrs:
        means, links = MEANS.get(a["key"], ("", []))
        where = "".join('<a href="%s">%s</a>' % (h, esc(t)) for h, t in links)
        rows.append(
            '<tr><td class="ck-attr-k"><b>%s</b><span>%s</span></td>'
            '<td class="ck-attr-m">%s</td>'
            '<td class="ck-attr-w"><div class="ck-screens">%s</div></td></tr>'
            % (esc(a["key"]), esc(a["pair"]), means, where))
    return ('<table class="tk-tbl ck-attrs"><thead><tr><th>the pair, from Concept</th>'
            "<th>what it means in the system</th><th>where you see it</th></tr></thead>"
            "<tbody>%s</tbody></table>" % "".join(rows))


def ref_rows(refs):
    rows = []
    for r in refs:
        rej = "REJECT" in r["role"].upper()
        rows.append('<tr%s><td class="tk-role">%s</td><td>%s</td><td class="tk-from">%s</td></tr>'
                    % (' class="ck-reject"' if rej else "", esc(r["name"]),
                       esc(r["role"]), esc(r["serves"])))
    return ('<table class="tk-tbl ck-refs"><thead><tr><th>source</th><th>what was taken</th>'
            "<th>the anxiety it answers</th></tr></thead><tbody>%s</tbody></table>"
            % "".join(rows))


# The plate reads its own tokens, so it cannot print a colour the system does not
# have. Each swatch is a role, not a hex: a hex on this page would be a fifth copy
# of a value that already lives in tokens.css.
PLATE = [
    ("--bg-page", "page", "graphite, and the reason nothing else has to shout"),
    ("--bg-plate", "plate", "the inset stone a screen stands on"),
    ("--bg-card", "card", "the floating stone a card is cut from"),
    ("--color-action", "brass", "the one accent: identity, active state, one action per zone"),
    ("--outcome-yes", "YES", "reserved. Never an accent, never a brand colour"),
    ("--outcome-no", "NO", "the other half of the same reservation"),
    ("--text-primary", "ink", "bone, warm, on a faintly cool stone"),
]


def plate():
    cells = "".join(
        '<div class="ck-plate-sw"><i style="background:var(%s)"></i>'
        '<b>%s</b><code>var(%s)</code><span>%s</span></div>' % (t, esc(lab), t, esc(note))
        for t, lab, note in PLATE)
    return ('<div class="ck-plate">%s</div>'
            '<p class="tk-note">Three families and nothing else: Space Grotesk for display, DM Sans '
            'for body, IBM Plex Mono for every number. The mono is not decoration. A figure set in '
            'a proportional face reads as prose, and a person checking what a market says needs it '
            'to read as a reading.</p>' % cells)


def chain_html():
    out = []
    for title, href, note in CHAIN:
        head = ('<a href="%s">%s</a>' % (href, title)) if href else "<b>%s</b>" % title
        out.append("<li>%s<p>%s</p></li>" % (head, note))
    return "".join(out)


def doors_html():
    return "".join(
        '<a class="ck-door" href="%s"><b>%s</b><span>%s</span><code>%s</code></a>'
        % (href, esc(q), note, esc(href))
        for q, href, note in DOORS)


def render():
    """The page, as a string. Split out from build() so gate 28 can re-render in
       memory and compare, the way gate 21 reads a document: a file can be newer
       than its sources and still be wrong."""
    attrs = attributes()
    refs = references()
    if len(attrs) < 5 or len(refs) < 4:
        raise SystemExit("_gen_why_page: read %d attributes and %d references, which is fewer than "
                         "the documents have. The parser is looking at the wrong shape."
                         % (len(attrs), len(refs)))
    missing = [k for k in (a["key"] for a in attrs) if k not in MEANS]
    if missing:
        raise SystemExit("_gen_why_page: %s has no line in MEANS. An attribute with no answer is "
                         "the one thing this page may not ship." % ", ".join(missing))
    sources = "".join('<li><code>%s</code><span>%s</span></li>' % (esc(p), n) for p, n in SOURCES)
    return PAGE.format(
        boot=THEME_BOOT, nattr=len(attrs), nref=len(refs),
        attributes=attribute_rows(attrs), plate=plate(), refs=ref_rows(refs),
        chain=chain_html(), doors=doors_html(), sources=sources)


def build():
    (KIT / "why.html").write_text(render(), encoding="utf-8")
    print("wrote ui-kit/why.html: %d attributes, %d references, %d doors, %d sources"
          % (len(attributes()), len(references()), len(DOORS), len(SOURCES)))


if __name__ == "__main__":
    build()
