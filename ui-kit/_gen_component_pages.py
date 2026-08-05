#!/usr/bin/env python3
"""Build one stand page per component, plus the hub and the registry.

For every components/<name>.css it writes ui-kit/<name>.html carrying:
  - the component live, in a frame of its own, at the width it is meant to be
    read at (a mobile-only piece gets 360, so the media query shows it instead
    of being overridden);
  - the states the markup carries, and the rules behind the states it cannot
    hold still (hover, focus) quoted from the file rather than faked;
  - the semantic roles the file reads, each with a swatch;
  - the classes it owns and how many painted screens carry each one;
  - the screens in ui-visual/ where the component stands, as links;
  - the rules of use that name it, extracted from the ONE table that holds them
    in ui-kit/docs/architecture.md, so the rule is authored once and read where
    a person is standing;
  - the css itself, so the file and the page never drift apart.

Specimens come from ui-kit/specimens/, built by _extract_specimens.py out of the
labelled blocks of the frozen kit. A component page frames every specimen one of
its measured faces stands in, and not only the ones the registry files under its
name. The old rule was "render what you OWN, link the rest", and on the biggest
component in the system it showed two controls out of five: `.provider-btn` and
`.confirm-btn` are 574 of the button family's 704 placements and neither stands
in a specimen registered to `button`, so a page whose whole subject is the
family rendered the two smallest members and sent the reader to a list of links
for the rest. `ui-kit/_verify/states.cjs` already had to solve this to find
anything to photograph, and its comment says why in the same words.

THAT IS NOT A SECOND COPY OF THE MARKUP. A specimen is one file. Framing it from
two pages is one document read through two doors, and the rule it appears to
bend - never show markup twice - is about never AUTHORING it twice, which still
holds: nothing here writes markup, and the frame carries the specimen's own url.
What is still linked rather than framed is every OTHER document the component
merely appears inside, which is the part that would have been repetition.

Also writes ui-kit/_nav.js (the one registry), ui-kit/overview.html (the hub)
and ui-kit/_frames.js (the parent half of the frame height handshake).

    python3 ui-kit/_extract_specimens.py && python3 ui-kit/_gen_component_pages.py

Idempotent. Never touches components/ or ui-visual/. No em dash.
"""
import glob
import html
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "components"
KIT = ROOT / "ui-kit"
UV = ROOT / "ui-visual"

# the theme switch is written once, in the tree that also puts it on the 76
# painted screens. Importing it keeps the stand pages and the product on the
# same boot script instead of two copies that can drift.
sys.path.insert(0, str(UV))
from _theme_switch import BOOT as THEME_BOOT, BUTTON as THEME_BUTTON, button  # noqa: E402
# the panel opens showing where you are, and the screens tree does the same
# thing from the same string: two panels, one behaviour, one source.
from _panel_reveal import BODY as REVEAL_BODY, CALL as REVEAL_CALL  # noqa: E402
# the four documents are rows in the same registry as the components, and the
# table that names them lives with the renderer, not here: two lists of one
# fact is how coverage.md and the css headers came to disagree.
sys.path.insert(0, str(KIT))
from _gen_docs import PAGES as DOC_PAGES  # noqa: E402
# The rules of use are authored in ONE table, in ui-kit/docs/architecture.md.
# This reads that table instead of keeping a second list of the same nine facts,
# which is the rule the repo has paid to learn twice. Gate 26 checks the pairing
# in both directions, so a rule cannot name a component whose page is silent and
# a page cannot carry a rule the document has never heard of.
from _gen_docs import usage_rules, inline as md_inline  # noqa: E402
# ONE MARKDOWN READER, NOT TWO. The authored half of a stand page used to go
# through a reader written here that knew a paragraph and a `- ` list and nothing
# else. `ui-kit/authored/button.md` answers "when to use" with an eleven-row
# table of four axes and two `###` headings, because a decision made of four
# values IS a table, and every pipe of it printed on the page as running text.
# Gate 35 could not see it: it asks for `](` and `**`, the two marks that can
# only ever be a failed render, and a pipe is a character a sentence may contain.
# The documents already have a reader that handles GFM tables, headings, quotes
# and code blocks, so the fix is to stop having a second one.
from _gen_docs import blocks as md_blocks  # noqa: E402
THEME_BUTTON_INLINE = button(inline=True)

SPECIMENS = json.loads((KIT / "specimens" / "index.json").read_text(encoding="utf-8"))
TOKENS = (COMP / "tokens.css").read_text(encoding="utf-8")
SEM = set(re.findall(r"(--[\w-]+)\s*:", TOKENS[TOKENS.index("2. SEMANTIC"):]))

# The panel is grouped by LEVEL, and inside a group it reads in the order the
# cascade loads. It used to be grouped by PURPOSE, which is the right way to
# group a product and the wrong way to group a system: a group named for where a
# thing is used answers a question the screens already answer, and it puts a
# button next to a sign-in dialog because both appear in a form. Grouped by
# level, the panel answers the question a system has instead, which is what may
# be built out of what, and reading it top to bottom is reading index.css.
#
# Derived, not typed, from the same map that orders the cascade: two lists of one
# fact is how coverage.md and the css headers came to disagree.
from _levels import LEVEL as _LEVEL, ORDER as _ORDER, NOT_A_COMPONENT as _NOT_COMP  # noqa: E402
from _levels import PATTERNS as _PATTERNS                             # noqa: E402

# The panel reads top to bottom the way index.css loads: Foundations, then the
# three levels in cascade order, then Patterns. Patterns come last for the same
# reason their @imports do, and it is not tidiness: a pattern has to be able to
# place what it holds, so it loads after everything it holds. The panel showing a
# different order to the one the cascade uses would be a second answer to a
# question the file already answers.
#
# A pattern has no level, so it cannot be sorted into the three groups above, and
# the group page leads its own group because it is the door: the choice rule
# between taking a pattern whole and assembling from components is on it.
_PAT_STEMS = [f.split("/", 1)[1] for f in _PATTERNS]
GROUPS = [("Foundations", ["tokens", "icons", "base", "course-chrome"])] + [
    (name, [f for f in _ORDER if _LEVEL.get(f) == n and f not in _NOT_COMP])
    for n, name in ((1, "Atoms"), (2, "Molecules"), (3, "Organisms"))
] + [("Patterns", ["patterns"] + _PAT_STEMS)]

# What each row points at in the code. Derived where it can be and declared where
# it cannot: three rows are not a components/<name>.css and each says why.
def code_path(name):
    if name == "tokens":
        return "components/tokens.css"
    if name == "icons":
        return "ui-kit/icons.html"          # a sprite, not a stylesheet
    if name == "patterns":
        return "components/patterns/"       # the folder, because the row is the group
    if name in _PAT_STEMS:
        return "components/patterns/%s.css" % name
    return "components/%s.css" % name
LABEL = {
    "patterns": "Patterns", "browse-shell": "Browse shell", "detail-shell": "Detail shell",
    "card-grid": "Card grid", "list-head": "List head", "position-list": "Position list",
    "action-bar": "Action bar",
    "tokens": "Tokens", "icons": "Icons", "base": "Base and page frame",
    "course-chrome": "Course chrome",
    "header": "App header", "catnav": "Category nav", "bottomnav": "Bottom nav", "tabs": "Tabs",
    "footer": "Footer", "trustbar": "Trust bar and cards", "feed": "Feed layout", "card": "Event card",
    "oddsbar": "Odds bar", "yesno": "YES / NO buttons", "options": "Outcome rows", "hero": "Featured hero",
    "seo-plate": "SEO plate", "loadmore": "Load more", "filters": "Sort and filters",
    "event-detail": "Event Detail layout", "chart": "Price chart", "betpanel": "Bet panel and dock",
    "market": "AMM market panel", "comments": "Comments", "bets-table": "Bets and activity",
    "related": "Related events", "button": "Buttons", "input": "Fields and amounts",
    "dialog": "Shared dialog", "hiw-dialog": "How-it-works dialog",
    "notice": "Notices and banners", "state-block": "State block", "skeleton": "Skeletons",
    "toast": "Toasts",
    "profile": "Profile identity", "position": "Position rows", "account": "Account bars",
    "cookie-consent": "Cookie consent",
}
NOTE = {
    "base": "Not a component: the page frame, the reset, the shared utilities and the neutralisation "
            "block that hides the grey-box scaffolding the wireframes left behind.",
    "course-chrome": "Not product: the roadmap sidebar every page of this repo carries. It ships with "
                     "the system only because the painted screens render it.",
}
# Sections on tokens.html that answer a foundation question. One page, several doors.
FOUNDATION_DOORS = [
    ("Colour", "tokens.html#colour", "Every graphite step and every brass, and the roles that read them."),
    ("Material", "tokens.html#material", "The two-stone plates, the grain, the bevels and the grooves."),
    ("Geometry", "tokens.html#geometry", "Spacing, radius, control sizes, the container and the gutter."),
    ("Type", "tokens.html#type", "Three families, the size ramp, weight and leading."),
    ("Motion", "tokens.html#motion", "Durations and easings, shown moving."),
]

STATE_PAT = re.compile(r":hover|:focus-visible|:focus|:active|:disabled|:checked|"
                       r"\[aria-current|\[aria-checked|\[open\]|\[disabled\]|"
                       r"\.sel\b|\.active\b|\.open\b|\.scrolled\b|\.skeleton\b|\.is-[\w-]+")


def esc(s):
    return html.escape(s, quote=False)


# ---- where a class is actually used ----------------------------------------
# A class the painted screens do not carry can still be alive. A zero means one
# of five things, and the Classes table says which, because "0" on its own reads
# as "delete me" and four times out of five that would be wrong.
#
# THE READING MOVED TO _adoption.py ON 2026-08-03, and it moved because it grew
# a second consumer: gate 30 fails the build on a class the system declares and
# the product does not wear, which is this same question with the answer made
# load-bearing. It was computed here, and a truth computed in the place that
# PRINTS it is a truth the checker has to compute again; two readings of one
# thing is what drifted between coverage.md and the css headers, and again
# between the two panel generators. So the reading is there, the reasons are
# declared there beside it, and this file reads them.
sys.path.insert(0, str(KIT))
from _adoption import classes_in, flat, uv_classes, where     # noqa: E402,F401
from _adoption import kit_used, wf_used, docs_used, uv_used   # noqa: E402,F401

# ---- every class any component file declares, for the orphan check ----------
declared = set()
for path in COMP.glob("*.css"):
    if path.stem in ("index", "tokens"):
        continue
    # A CLASS NAMED IN A COMMENT IS NOT A CLASS THE FILE STYLES. Only the url()
    # was cut here, so a note explaining which class a rule replaced put that
    # class straight back into the declared set, and coverage.md listed it as a
    # deletion candidate that had already been deleted. Both .ck-note-link and
    # .sidebar-sub-head came back that way in the same pass that removed them.
    body = re.sub(r"/\*.*?\*/", " ", path.read_text(encoding="utf-8"), flags=re.S)
    body = re.sub(r"url\([^)]*\)", "", body)
    declared.update(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", body))


# ---- which file OWNS a class, and therefore where a component STANDS --------
# The map moved to _levels.py, which needs the same answer to work out what
# stands INSIDE a component. Two copies of one map is the defect step 7c closed
# between coverage.md and the css headers and step 9 closed again between the two
# panel generators: one computation feeds both, or they drift and nobody can tell
# which to believe. The reasoning for the map is written there with it.
from _levels import SUBJECTS, OWNER, STATIC  # noqa: E402


def parse_component(name):
    css = (COMP / (name + ".css")).read_text(encoding="utf-8")
    head = css[:css.index("*/") + 2] if "*/" in css else ""
    body = css[len(head):].strip()
    # WHAT THE FILE STYLES IS READ FROM ITS RULES, NOT FROM ITS PROSE. Only the
    # header comment was cut, so every later comment was scanned as css: that is
    # where .css and .color came from in the deletion-candidate table, harvested
    # out of the words "components/index.css" and "Colour goes through a role",
    # and it is how .ck-note-link and .sidebar-sub-head reappeared in the same
    # pass that deleted them, listed as candidates for a deletion already done.
    # body itself keeps its comments: it is also what the stand page prints.
    prose_free = re.sub(r"/\*.*?\*/", " ", body, flags=re.S)
    roles = sorted({m for m in re.findall(r"var\((--[\w-]+)\)", prose_free) if m in SEM})
    classes = sorted({c for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)",
                                            re.sub(r"url\([^)]*\)", "", prose_free))})
    rules = len(re.findall(r"\{", prose_free))
    owned = sorted(c for c in SUBJECTS.get(name, {}) if OWNER.get(c) == name)
    screens = sorted([p for p, cs in uv_classes.items() if cs & set(owned)])
    # prose_free and not body: a comment sitting above a rule is part of the
    # match, so the selector cell used to print a paragraph of reasoning and then
    # the selector. Everything else on this page already reads the stripped text.
    states = []
    for m in re.finditer(r"([^{}\n][^{}]*)\{([^{}]*)\}", prose_free):
        sel = " ".join(m.group(1).split())
        if STATE_PAT.search(sel) and not sel.startswith("@"):
            states.append((sel, m.group(2).strip()))
    return dict(css=css, body=body, roles=roles, classes=classes, rules=rules,
                screens=screens, owned=owned, states=states)


# ---------------------------------------------------------------- sections ---
def live_specimens(name):
    """The specimens this page frames: the ones it OWNS, and only those.

    A DETOUR WORTH RECORDING, BECAUSE THE PROBLEM IT SOLVED IS REAL AND THE
    SOLUTION WAS NOT. The button page framed two controls out of five, because
    `.provider-btn` and `.confirm-btn` have no ground outside the dialog, panel
    or bar they ship in and no specimen registered to `button` holds one. On
    2026-08-04 this function was widened to frame every document a measured face
    stood in, and the button page grew a whole sign-in dialog and a whole profile
    header: three hundred lines of other components, to show one row.

    THAT IS SHOWING THE HOST INSTEAD OF THE CONTROL. The scope is needed for the
    paint, and the scope is `<dialog class="app-dialog">`, not the dialog with
    its heading, its amount field, its chips and its fine print. So the fix went
    where it belonged, into the specimen: `button-matrix` stages every variant
    the product wears inside the smallest wrapper that paints it, and this
    function went back to the one line it was.

    AND IT EXCLUDES WHAT ANOTHER SECTION OWNS. `button-census` is registered to
    `button` like every other specimen of this page, so this function framed it,
    and `census_table()` framed it again under the role tables that explain it.
    The page shipped the same twelve controls twice and, worse, two elements
    carrying `id="sp-button-census"`, so the jump link and every `#sp-` anchor
    resolved to whichever came first. The list is read from `_worn` rather than
    typed here, because the section that owns those specimens is the one that
    already names them.
    """
    owned = set(_worn.CENSUS_SPECIMENS)
    return [s for s in SPECIMENS if s["component"] == name and s["id"] not in owned]


def live(name):
    mine = live_specimens(name)
    if not mine:
        return ('<p class="tk-note">No specimen of its own yet. It is rendered inside the specimens '
                'linked below.</p>')
    out = []
    for s in mine:
        w = s.get("width", 900)
        cap = []
        if s.get("state"):
            cap.append('<span class="ck-cap-k">state</span> ' + esc(s["state"]))
        if s.get("note"):
            cap.append(esc(s["note"]))
        caption = ('<p class="ck-cap">' + "<br>".join(cap) + "</p>") if cap else ""
        out.append(
            f'<figure class="ck-scene" id="sp-{s["id"]}">'
            f'<figcaption class="ck-scene-lbl"><b>{esc(s["title"])}</b>'
            f'<span class="ck-w">{w}px</span><span class="ck-zoom" hidden></span>'
            f'<a href="specimens/{s["id"]}.html" target="_blank" rel="noopener">open on its own</a>'
            f"</figcaption>"
            f'<div class="ck-frame" style="width:{w}px">'
            f'<iframe data-specimen="{s["id"]}" src="specimens/{s["id"]}.html" '
            f'width="{w}" height="{s.get("height", 320)}" loading="lazy" '
            f'title="{esc(s["title"])}"></iframe></div>{caption}</figure>')
    return "\n".join(out)


ROLE_TITLE = {
    "action": "Actions, and every one of them stands above",
    "selector": "Selectors, which are not buttons",
    "nav": "Navigation, wearing a button's tag",
    "stand": "Not product",
}


def census_table(name):
    """Every button-shaped control in the product, split by what it actually IS.

    A `<button>` IS A TAG AND NOT A ROLE, and the first cut of this section read
    the tag as the answer. So the page called Buttons listed 5,281 controls, of
    which 1,856 are buttons: the other 3,425 are chips, tabs, a toggle, the
    YES / NO pair, rows of the account menu, slots of the bottom nav and five
    social marks. Two of them were staged live on this page, which is worse than
    listing them, because a selector's whole subject is its group and its selected
    state and one of them standing alone shows the half that does not matter.

    Three roles and one non-product, defined in `_worn.KINDS` and held by gate 38
    in both directions. The actions stand live above, sliced out of the specimens
    they already ship in. The rest is an index: what it is, how much of the
    product it is, and the door to the page that draws it.
    """
    if name != "button":
        return ""
    by_role, _unstaged, _wrong = _worn.roles()

    def rows_for(role):
        out = []
        for r in by_role[role]:
            owner = r["owner"]
            page = KIT / (owner + ".html")
            first = next((s["id"] for s in SPECIMENS if s["component"] == owner), None)
            where = esc(LABEL.get(owner, owner))
            if page.exists():
                href = "%s.html%s" % (owner, "#sp-" + first if first else "")
                where = '<a href="%s">%s</a>' % (href, where)
            classes = " ".join("<code>%s</code>" % esc(c) for c in r["classes"])
            out.append("<tr><td>%s</td><td class='tk-role'>%s</td><td class='tk-hex'>%d</td>"
                       "<td class='tk-hex'>%d</td><td>%s</td><td class='tk-from'>%s</td></tr>"
                       % (esc(r["kind"]), classes, r["uses"], r["screens"], where, esc(r["why"])))
        return "".join(out)

    # in the same scrolling box a document's table gets: seven columns do not
    # fold into 360 and a page that scrolls sideways is worse than a table that
    # does. Measured after: button.html was +21px at 360 with the table bare, 0
    # with it in the box.
    def table(role):
        n = sum(r["uses"] for r in by_role[role])
        # `.tk-subh` and not a class of its own: this is the sub-heading style the
        # vitrine already has, and a second one would be a second decision about
        # the same thing.
        return ('<h3 class="tk-subh">%s</h3><p class="tk-note">%s '
                '<b>%d kind(s), %d placement(s).</b></p>'
                '<div class="tk-doc-tbl"><table class="tk-tbl ck-census"><thead><tr>'
                '<th>what it is</th><th>class</th><th>uses</th><th>screens</th>'
                '<th>drawn on</th><th>why there and not here</th>'
                "</tr></thead><tbody>%s</tbody></table></div>"
                % (ROLE_TITLE[role], esc(_worn.ROLE_WHY[role]), len(by_role[role]), n,
                   rows_for(role)))

    frames = "".join(
        '<figure class="ck-scene" id="sp-%s"><figcaption class="ck-scene-lbl"><b>%s</b>'
        '<span class="ck-w">%dpx</span><span class="ck-zoom" hidden></span>'
        '<a href="specimens/%s.html" target="_blank" rel="noopener">open on its own</a>'
        '</figcaption><div class="ck-frame" style="width:%dpx">'
        '<iframe data-specimen="%s" src="specimens/%s.html" width="%d" height="320" '
        'loading="lazy" title="%s"></iframe></div></figure>'
        % (s["id"], esc(s["title"]), s.get("width", 900), s["id"], s.get("width", 900),
           s["id"], s["id"], s.get("width", 900), esc(s["title"]))
        for s in SPECIMENS if s["id"] == "button-census")
    return frames + "".join(table(r) for r in _worn.ROLES)




def elsewhere(name):
    other = [s for s in SPECIMENS if name in s.get("also", [])]
    if not other:
        return ""
    links = "".join(
        f'<a href="{s["component"]}.html#sp-{s["id"]}">{esc(s["title"])}</a>' for s in other)
    return ('<section class="tk-sec" id="inside"><h2 data-n="02">Also rendered inside</h2>'
            '<p class="tk-note">The same markup, shown once on the page of the component that owns '
            'it. Nothing here is a second copy.</p>'
            f'<div class="ck-screens">{links}</div></section>')


# A page that says nothing where a state should be reads the same whether the
# absence was decided or forgotten, and the reader has no way to tell which. So
# an empty States section is not allowed to be silent: it either quotes the
# declaration in _levels.STATIC, reason and all, or it says out loud that this is
# a gap. Gate 25 makes the same list load-bearing in both directions, so the two
# can never drift: a component here without an entry fails the build.
def states_table(states, name=""):
    if not states:
        why = STATIC.get(name)
        if why:
            return ('<p class="tk-note"><b>No states: not interactive.</b> '
                    'Declared in <code>ui-kit/_levels.py</code>, and gate 25 holds it: '
                    '%s. A state belongs to what a person can press or type into, and '
                    'inventing one here would inflate the system the way an empty '
                    'semantic role would.</p>' % esc(why))
        return ('<p class="tk-note"><b>A gap, not a decision.</b> This file declares no state '
                'rule and is not on the declared static list, so the component looks the same '
                'at rest, on hover and while it is held down.</p>')
    rows = "".join(
        f"<tr><td class='tk-role'>{esc(sel)}</td><td class='ck-decl'>{esc(decl)}</td></tr>"
        for sel, decl in states[:24])
    more = ("<p class='tk-note'>%d more in the file below.</p>" % (len(states) - 24)) \
        if len(states) > 24 else ""
    return ('<table class="tk-tbl"><thead><tr><th>selector</th><th>what moves</th></tr></thead>'
            f"<tbody>{rows}</tbody></table>{more}")


# The tokens a STATE reads, shown on both grounds at once. A state that is a
# token and not a style is only provable one way: put the token on the page in
# both themes and let the browser resolve it. The table above says which selector
# moves what; this says what the value it moves to actually looks like, and it is
# the only part of the page that can catch a token declared in one theme and not
# the other, because that failure has no appearance in the file at all. The
# mechanism is the one section 2 of tokens.css was written for: any element may
# carry data-theme and its subtree resolves in that theme, which is what lets
# both grounds stand on one page in whichever theme the reader is in.
def state_tokens(states, roles):
    """Roles that only a state rule reads, in the order they appear."""
    seen, out = set(), []
    for sel, decl in states:
        for m in re.findall(r"var\((--[\w-]+)\)", decl):
            if m in seen:
                continue
            seen.add(m)
            if m in SEM or m.startswith("--opacity-"):
                out.append(m)
    return out


def state_grounds(tokens):
    if not tokens:
        return ""
    # A ROLE IS SHOWN DOING ITS OWN JOB, and the caption says which job that is.
    # Every row used to read "the value this state moves to", eight times per
    # panel, which is a sentence about the section rather than about the token;
    # and every row painted the value as a BACKGROUND, so --text-on-brass drew
    # black on black and the two ink roles were unreadable rectangles. The kind
    # is read from the role's own name, which is the one place in this system
    # where a name is load-bearing: tokens.css is written --bg-*, --text-*,
    # --border-*/--line-*, --opacity-*, --focus-*.
    def sample(tok):
        if tok.startswith("--opacity-"):
            return ('<span class="ck-st-row"><span class="ck-st-chip" style="opacity:var(%s)">'
                    'Confirm bet</span><span class="ck-st-chip">Confirm bet</span>'
                    '<em>how far the control fades, beside the same control at rest</em></span>'
                    % tok)
        if "focus" in tok or "ring" in tok:
            return ('<span class="ck-st-row"><span class="ck-st-chip" '
                    'style="outline:var(--ring) solid var(%s);outline-offset:var(--ring)">'
                    'Confirm bet</span><em>the ring, at the width and offset it ships with</em>'
                    '</span>' % tok)
        if tok.startswith("--text-"):
            return ('<span class="ck-st-row"><span class="ck-st-chip ck-ink" style="color:var(%s)">'
                    'Confirm bet</span><em>the label, on the ground this state puts it on</em>'
                    '</span>' % tok)
        if tok.startswith("--border-") or tok.startswith("--line-"):
            return ('<span class="ck-st-row"><span class="ck-st-chip ck-line" '
                    'style="border-color:var(%s)">Confirm bet</span>'
                    '<em>the edge this state draws</em></span>' % tok)
        klass = "ck-st-chip ck-ground" if tok.startswith("--bg-") else "ck-st-chip"
        return ('<span class="ck-st-row"><span class="%s" style="background:var(%s)">'
                'Confirm bet</span><em>the ground the control settles onto</em></span>'
                % (klass, tok))
    figs = []
    for ground, label in (("dark", "Vault"), ("light", "Daylight")):
        rows = "".join('<div class="ck-st-tok"><code>%s</code>%s</div>' % (esc(t), sample(t))
                       for t in tokens)
        figs.append('<div class="tk-theme-fig" data-theme="%s"><b>%s</b>%s</div>'
                    % (ground, label, rows))
    return ('<h3 class="tk-subh">The tokens these states read, on both grounds</h3>'
            '<p class="tk-note">Neither panel is a screenshot. Each carries <code>data-theme</code> '
            'itself, so the token resolves inside it and a role that was given a value in only one '
            'theme shows up here as a control that does not move.</p>'
            '<div class="tk-theme-grid">%s</div>' % "".join(figs))


def role_swatches(roles):
    if not roles:
        return '<p class="tk-note">Reads no colour role: this file is geometry and layout only.</p>'
    cells = "".join(f'<span class="ck-role"><i style="background:var({r})"></i><code>{esc(r)}</code></span>'
                    for r in roles)
    return f'<div class="ck-roles">{cells}</div>'


def class_table(classes):
    rows = []
    for c in classes:
        n = sum(1 for cs in uv_classes.values() if c in cs)
        kind, why = where(c)
        tag = f'<span class="ck-kind ck-{kind}" title="{esc(why)}">{kind}</span>' if kind else ""
        rows.append(f"<tr><td class='tk-role'>.{esc(c)}</td><td class='tk-hex'>{n}</td>"
                    f"<td class='tk-hex'>{tag}</td></tr>")
    return ('<table class="tk-tbl"><thead><tr><th>class</th><th>screens</th><th>if zero</th>'
            "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


# The one section on this page that is not read out of the css. Everything else
# here answers "what is this component"; a rule of use answers "what may it do
# beside the others", and no file in components/ can hold that, because every one
# of them describes a component alone.
#
# It is an EXTRACT and never a paraphrase: the id, the rule as the document
# states it, its class and its one-glance check, with the link back to where it
# was decided. The reasoning, the numbers and the source stay in the document,
# because a rule restated in two voices is a rule with two meanings.
#
# A component no rule names gets no section at all. That is the opposite of the
# States rule above, on purpose: every interactive component is EXPECTED to have
# states, so silence there is ambiguous, while most components legitimately have
# no usage rule and a row saying so on 27 pages would be noise pretending to be
# a decision.
RULES = usage_rules()


def constraints(name):
    mine = [r for r in RULES if name in r["components"]]
    if not mine:
        return ""
    rows = "".join(
        "<tr><td class='tk-role'>%s</td><td>%s</td><td class='tk-hex'>%s</td>"
        "<td>%s</td></tr>"
        % (esc(r["id"]), md_inline(r["title"]), esc(r["cls"]), md_inline(r["check"]))
        for r in mine)
    return """
  <section class="tk-sec" id="rules">
    <h2 data-n="07">Constraints</h2>
    <p class="tk-note">What this component may do beside the others: how many of it a screen may
    carry, and where it may not stand. %s that %s this component, quoted from
    <a href="architecture.html#rules-of-use">Rules of use</a>, which is where each one was decided
    and where its numbers and its source are. This is an extract and not a second copy: gate 26
    fails the build if a rule names a component whose page is silent, and equally if a page carries
    a rule the document does not have.</p>
    <table class="tk-tbl ck-rules"><thead><tr><th>rule</th><th>what it says</th><th>class</th>
    <th>check it at a glance</th></tr></thead><tbody>%s</tbody></table>
  </section>
""" % ("The %d rules" % len(mine) if len(mine) > 1 else "The one rule",
       "name" if len(mine) > 1 else "names", rows)


def screen_links(screens):
    if not screens:
        return '<p class="tk-note">Not on a painted screen yet.</p>'
    return '<div class="ck-screens">' + "".join(
        f'<a href="../ui-visual/{s}">{esc(s[:-5])}</a>' for s in screens) + "</div>"


# ---- the half a generator cannot compute, and the half it photographs -------
# _authored.py holds the reasoning: a program can read how many rules a file has
# and never what the component is FOR, so the three blocks that carry judgement
# were missing from every page. _states.py holds the pictures: a hover shown as
# `background:var(--bg-control-hover)` is a fact about the file and tells nobody
# what a hover looks like.
import _authored                                                      # noqa: E402
import _states                                                        # noqa: E402
# the census of every control in the product that is a button, and who draws it.
# Read here rather than re-counted, for the reason every list in this repo is
# read from one place: two counts of one fact are two facts.
import _worn                                                          # noqa: E402

AUTHORED = {p.stem: _authored.parse(p)
            for p in sorted((KIT / "authored").glob("*.md"))} if (KIT / "authored").exists() else {}
CAPTURED = _states.by_component()


def png_size(path, shot):
    """The CSS size the picture should be laid out at, so the box is reserved
    before the image arrives. Recorded at capture time rather than derived from
    the file, because the capture scale is now per element: a control is shot at
    two device pixels per css pixel and a panel at one."""
    if shot.get("w"):
        return shot["w"], shot["h"]
    b = path.read_bytes()[16:24]
    return (int.from_bytes(b[:4], "big"), int.from_bytes(b[4:], "big"))


STATE_ORDER = ["rest", "hover", "active", "focus", "disabled"]
STATE_WHAT = {"rest": "rest", "hover": "hover", "active": "held down",
              "focus": "focused by keyboard", "disabled": "disabled"}


# WHAT A FACE IS MADE OF, in the order `browser.cjs face()` writes it. Nine
# values, and each one is named here for a reader rather than for a stylesheet:
# the second column is how it should be shown, because a colour that is printed
# as six characters of hex is a fact nobody checks and a colour shown as itself
# is one anybody can.
#
# TWO OF THE NINE ARRIVE CLIPPED. `face()` takes 50 characters of
# background-image and 60 of box-shadow, which is enough to tell a gradient from
# no gradient and a glow from no glow and not enough to rebuild either. So they
# are printed as what was recorded, with the clip marked, and nothing on this
# page pretends to redraw them: the thing that draws them is the live frame
# above, painted by components/index.css like every other screen in the repo.
FACE = [("ground", "colour"), ("gradient", "text"), ("edge", "colour"),
        ("edge width", "len"), ("ink", "colour"), ("corner", "len"),
        ("lift", "text"), ("shadow", "text"), ("fade", "text"),
        # THE TENTH, ADDED 2026-08-05, and it is the one focus actually moves.
        # It is a sentence rather than a swatch because it is four values -
        # style, width, colour, offset - and a colour with no width is a ring
        # that may not be drawn at all. `none 0px rgb(...) 0px` is a control
        # with no ring, and QUIET below is what keeps that out of the rest row.
        ("ring", "text")]
FACE_CLIP = {1: 50, 7: 60}
QUIET = {"none", "1", "0px", "normal"}


def no_ring(val):
    """A ring that is not drawn, whatever colour the browser reports for it.

    `outlineColor` always has a value: with no rule at all it comes back as the
    element's own `color`, so a rest row would print "ring: none 0px rgb(237,
    231, 218) 0px" on every control in the product and the one row that matters
    would be lost in it. The ring exists when the style is not `none` and the
    width is not zero, which is two words of the four."""
    bits = (val or "").split()
    return len(bits) < 2 or bits[0] == "none" or bits[1] in ("0px", "0")


def face_bits(value):
    """The nine measured values, split and paired with their names."""
    return list(zip(FACE, (value or "").split(" | ")))


# A TRANSFORM IS RECORDED AS A MATRIX, because that is what getComputedStyle
# returns and the capture writes down what it read. `matrix(1, 0, 0, 1, 0, -1)`
# is the one pixel of lift components/button.css declares as translateY(-1px),
# and nobody reads it as that. The rewrite is lossless and only for the identity
# with a translation in it: any other matrix is a rotation, a scale or a skew and
# is printed as recorded, because a name for it would be a guess.
LIFT = re.compile(r"^matrix\(1,\s*0,\s*0,\s*1,\s*(-?[\d.]+),\s*(-?[\d.]+)\)$")


def face_cell(kind, val, i):
    """One measured value, shown as the kind of thing it is."""
    mark = "" if len(val) < FACE_CLIP.get(i, 10 ** 6) else '<abbr title="recorded clipped">...</abbr>'
    if kind == "colour":
        return ('<i class="ck-sw" style="background:%s"></i><code>%s</code>'
                % (esc(val), esc(val)))
    m = LIFT.match(val)
    if m:
        return ('<code><abbr title="%s">translate(%spx, %spx)</abbr></code>'
                % (esc(val), m.group(1), m.group(2)))
    return "<code>%s</code>%s" % (esc(val), mark)


def face_row(bits, base=None):
    """A state, as the values that make it. With `base`, only what MOVED.

    A state read as a difference is the thing a person actually asks about: the
    rest face answers "what is it" once, and every row under it answers "what
    does this state change", which is one or two values rather than nine. The
    photographs this section used to carry could not say that at all. Four
    pictures of a control that moves by one pixel are four pictures of the same
    control, and the reader is left to spot the difference, which is the job the
    instrument had already done and thrown away.
    """
    out = []
    for i, ((label, kind), val) in enumerate(bits):
        # a gradient and a shadow are sentences, not swatches, so they take a
        # line of their own rather than being squeezed into a column beside a
        # colour and broken mid-token
        cls = "ck-fx ck-fx-wide" if kind == "text" else "ck-fx"
        if base is not None:
            if val == base[i][1]:
                continue
            was = base[i][1]
            # A RING THAT IS NOT DRAWN CANNOT MOVE, and it changes value all the
            # time. `outline-color` defaults to `currentColor`, so a control that
            # takes brighter ink on hover reports a different ring in the same
            # breath, while `outline-style` stays `none` and nothing is painted.
            # The first run said "hover and press move ground, edge, ink and
            # ring" on 12 groups for exactly that reason: a value read where no
            # rule was ever written.
            if label == "ring" and no_ring(val) and no_ring(was):
                continue
            # THE RING ARRIVES, it does not move from something. Printing
            # "ring: 2px solid brass from none 0px rgb(237,231,218) 0px" is a
            # true sentence in which the half a reader needs is second and the
            # half that is a browser default is first.
            if label == "ring" and no_ring(was):
                out.append('<span class="%s"><em>%s arrives</em>%s</span>'
                           % (cls, esc(label), face_cell(kind, val, i)))
                continue
            if label == "ring" and no_ring(val):
                out.append('<span class="%s"><em>%s goes</em></span>' % (cls, esc(label)))
                continue
            out.append('<span class="%s"><em>%s</em>%s <span class="ck-fx-to">from</span> %s</span>'
                       % (cls, esc(label), face_cell(kind, val, i), face_cell(kind, was, i)))
            continue
        if val in QUIET or (label == "ring" and no_ring(val)):
            continue
        out.append('<span class="%s"><em>%s</em>%s</span>' % (cls, esc(label), face_cell(kind, val, i)))
    if not out:
        return '<span class="ck-fx ck-fx-same">nothing in the ten values moves</span>'
    return "".join(out)


# THE SHORT NAME OF A STATE, for the one line that stands where the table used to.
# STATE_WHAT above is written for a table cell, where "focused by keyboard" has a
# column of its own and all the room it needs; a digest is a sentence, and
# "hover and focused by keyboard move nothing" is a sentence nobody finishes.
STATE_SHORT = {"hover": "hover", "active": "press", "focus": "focus",
               "disabled": "disabled"}


def human_list(items, join="and"):
    items = list(items)
    if len(items) < 3:
        return (" %s " % join).join(items)
    return ", ".join(items[:-1]) + " %s %s" % (join, items[-1])


def face_digest(moved):
    """What actually moves, in one line, so the ten values can stay folded.

    THE TABLE UNDER THIS WAS A QUARTER OF THE PAGE and most of its cells said
    "nothing in the ten values moves". Measured on 2026-08-05: the states
    section is 24.3 per cent of the switch's page, 20.6 of the card's and 15.4
    of the button's, and it is a grid of rgb triples in two themes for every
    face. Those numbers are the evidence and they have to stay reachable; they
    are not what a person opening the page of a switch came to read.

    So the section keeps saying what a reader needs and stops saying it in a
    table: which faces exist, what each one IS in the authored caption, and one
    computed line naming what each state MOVES. The values are one click under
    it, unchanged, still measured, still stale-checked by `_states.py`.

    The move set is the UNION of the two themes, not the Vault reading. A rule
    that fires in one theme and not the other is exactly the defect this section
    exists to catch, and a digest taken from one ground would hide it under a
    summary that reads correct.
    """
    # TWO STATES THAT MOVE THE SAME VALUE ARE ONE FACT, and saying it twice is
    # how a digest becomes the thing it replaced: "hover moves ground; press
    # moves ground; nothing moves on focus" is three clauses for two. The values
    # are named in the order the table prints them, never alphabetically, so a
    # reader who opens the fold finds them where the line said they would be.
    order = {label: i for i, (label, _k) in enumerate(FACE)}
    groups, quiet = [], []
    for st in STATE_ORDER:
        if st == "rest" or st not in moved:
            continue
        key = tuple(sorted(moved[st], key=lambda n: order.get(n, len(FACE))))
        if not key:
            quiet.append(STATE_SHORT[st])
            continue
        for k, sts in groups:
            if k == key:
                sts.append(STATE_SHORT[st])
                break
        else:
            groups.append((key, [STATE_SHORT[st]]))
    parts = ["%s move%s %s" % (human_list(sts), "" if len(sts) > 1 else "s", human_list(key))
             for key, sts in groups]
    if quiet:
        parts.append("nothing moves on " + human_list(quiet, "or"))
    return "; ".join(parts)


def state_gallery(name):
    """Every distinct face, live, and what the browser measured it at.

    IT USED TO BE FORTY PHOTOGRAPHS PER PAGE and that was the wrong answer to a
    right question. The question was "a table of `background:var(--bg-control
    -hover)` tells nobody what a hover looks like", and the answer taken was to
    photograph one, with a real pointer, in both themes, for every state of every
    face. What that produces is a page of small pictures whose entire content is
    a control the reader can already see three sections up, cropped by an
    instrument whose padding is derived per side from the distance to the nearest
    neighbour: 12px on the left of an action-bar button and 4px on its right, 9
    above a confirm button and 12 below. Gate 31 called none of that a crop
    because it asks one question, whether the ring and the glow fitted, and never
    whether the subject is centred in its own frame. A photograph also cannot be
    hovered, which is the one thing the subject of the section is for.

    So the frames in Live are the rendering, and this section is the reading of
    them: what each face IS at rest, and what each state MOVES, in the values the
    capture recorded. The capture still runs and still needs a browser, a real
    pointer and a real Tab, because those numbers cannot be read out of css: a
    hover value is the cascade resolved, not a declaration. What changed is that
    the page shows the measurement instead of a picture of it.

    THE RING IS THE TENTH AND IT WAS NOT THERE UNTIL 2026-08-05. The argument
    for leaving it out was that `outline` is drawn outside the border box, so a
    focus row saying nothing moved was saying the FACE does not move, which is
    true and is not what a reader of a focus row is asking. The consequence was
    93 groups reporting that focus does nothing, and two close buttons that ring
    brass and white being merged into one answer. See `browser.cjs face()`.
    """
    groups = CAPTURED.get(name)
    if not groups:
        return ""
    doc = AUTHORED.get(name, {})
    caps = _authored.state_captions(doc.get("States", ""))
    figs = []
    for g in groups:
        shots = g.get("shots", {})
        panels, moved = [], {}
        for theme, label in (("dark", "Vault"), ("light", "Daylight")):
            rest = shots.get("rest-%s" % theme)
            if not rest:
                continue
            base = face_bits(rest["value"])
            rows = ['<tr><td class="tk-role">rest</td><td class="ck-fx-cell">%s</td></tr>'
                    % face_row(base)]
            for st in STATE_ORDER:
                shot = shots.get("%s-%s" % (st, theme))
                if not shot or st == "rest":
                    continue
                bits = face_bits(shot["value"])
                # the same guard face_row() applies, and for the same reason: a
                # ring nobody draws still changes value, because outline-color
                # defaults to currentColor
                moved.setdefault(st, set()).update(
                    fname for i, ((fname, _kind), val) in enumerate(bits)
                    if val != base[i][1]
                    and not (fname == "ring" and no_ring(val) and no_ring(base[i][1])))
                rows.append('<tr><td class="tk-role">%s</td><td class="ck-fx-cell">%s</td></tr>'
                            % (esc(STATE_WHAT[st]), face_row(bits, base)))
            panels.append('<div class="tk-theme-fig" data-theme="%s"><b>%s</b>'
                          '<table class="tk-tbl ck-face-tbl"><thead><tr><th>state</th>'
                          '<th>what the browser measured</th></tr></thead><tbody>%s</tbody>'
                          "</table></div>" % (theme, label, "".join(rows)))
        # THE NUMBERS FOLD, THE READING DOES NOT. What is left standing is the
        # digest: one computed line saying which state moves which value, which
        # is the sentence the grid of rgb triples was being read FOR. See
        # face_digest() for the measurement that asked for this.
        panels = ('<details class="ck-nums"><summary><span class="ck-nums-say">%s</span>'
                  '<span class="ck-nums-open">the ten values, both themes</span></summary>'
                  '<div class="tk-theme-grid">%s</div></details>'
                  % (esc(face_digest(moved)) or "measured", "".join(panels))) if panels else ""
        missing = [s for s in ("hover", "active", "focus")
                   if not shots.get("%s-dark" % s)]
        note = ('<p class="tk-note ck-shot-gap">Not staged: %s. No specimen puts this one '
                'where the state can be raised, which is a specimen debt and not a missing '
                'rule.</p>' % ", ".join(missing)) if missing else ""
        # WHAT ELSE THIS ONE PICTURE ANSWERS FOR. A gallery is a DIFFERENCE and
        # not an occurrence, so a group that covers three placements has to say
        # the other two out loud: otherwise the page looks like it forgot them,
        # which is exactly the reading that put eight galleries on the button
        # page where there are five. Silent when a group covers only itself.
        covers = [c for c in g.get("covers", []) if c != (
            g["el"] + (" @" + g["scope"] if g.get("scope") else ""))]
        also_line = ('<p class="tk-note ck-gal-covers">Same answer, measured across all four '
                     'states in both themes: <code>%s</code>.</p>'
                     % "</code>, <code>".join(esc(c) for c in covers)) if covers else ""
        # DISABLED IS THE ONE STATE A READER CANNOT RAISE. Every other row in the
        # table above is a thing a person does to a live control that is three
        # sections up this page; a disabled one answers no pointer by
        # definition, so the picture of it stays. Four in the whole vitrine, on
        # cookie-consent and input.
        dis = []
        for theme, label in (("dark", "Vault"), ("light", "Daylight")):
            shot = shots.get("disabled-%s" % theme)
            if not shot or not (KIT / "_states" / shot["file"]).exists():
                continue
            w, h = png_size(KIT / "_states" / shot["file"], shot)
            dis.append('<figure class="ck-shot"><img src="_states/%s" width="%d" height="%d" '
                       'alt="%s, disabled, %s theme" loading="lazy">'
                       '<figcaption>%s</figcaption></figure>'
                       % (shot["file"], w, h, esc(g["el"]), theme, esc(label)))
        dis = ('<div class="ck-shot-row"><b>disabled, and it is the one state a pointer cannot '
               'raise</b><div class="ck-shot-strip">%s</div></div>' % "".join(dis)) if dis else ""
        # the in-page anchor only where the frame is actually on this page: the
        # capture files a face under the document it was found in, and that
        # document is not always one this component owns
        framed = {s["id"] for s in live_specimens(name)}
        here = ('<a href="#sp-%s">hover it in the frame above</a>' % g["specimen"]
                if g["specimen"] in framed else "")
        figs.append(
            '<figure class="ck-gal">'
            '<figcaption class="ck-gal-head"><b>%s</b>'
            '<span class="ck-w">%s</span>%s'
            '<a href="specimens/%s.html" target="_blank" rel="noopener">the specimen</a>'
            '</figcaption>%s%s%s%s%s</figure>'
            % (esc(g["el"]), esc(g.get("scope") or "on the bare canvas"),
               here, g["specimen"],
               also_line,
               ('<p class="ck-gal-cap">%s</p>' % md_inline(caps[g["key"]]))
               if g["key"] in caps else "",
               panels, dis, note))
    return "".join(figs)


def authored_block(name, section):
    """An authored section, through the reader the documents already use.

    It had a reader of its own here, eight lines long, that knew a paragraph and
    a `- ` list. Everything else an author wrote went out as running text with
    its marks still in it, and the only file that used anything else was the one
    with the most to say: `ui-kit/authored/button.md` decides the component on
    four axes, which is a table, and printed eleven rows of pipes into a
    paragraph. A generator that silently degrades what it cannot parse is the
    same defect shape as a checker that reports clean about what it did not
    read.
    """
    doc = AUTHORED.get(name, {})
    body = doc.get(section, "").strip()
    if not body:
        return ""
    # the section body carries no `## `, so nothing here opens a <section>: the
    # caller owns that, and a `###` inside an authored answer stays a subheading
    html_out, _toc = md_blocks(body.splitlines())
    return html_out


def sections_for(name, c):
    """The page, as an ordered list of sections, numbered where they land.

    THE ORDER IS THE ARGUMENT. A stand page exists to answer "what is this and
    how do I use it", and until 2026-08-03 it opened with a live frame and then
    went straight to a table of selectors: everything that carried judgement was
    absent and everything that carried facts was first. So the authored blocks
    come first where they exist, the STATES ARE PICTURES rather than a column of
    declarations, and the selector table keeps its place at the foot with the
    css, under a heading that says what it is: what the file says, for a person
    who is about to edit it.

    A component with no authored source keeps the old order rather than losing
    its states section: the fan-out writes those files one at a time, and a page
    that is thin is better than a page that is empty."""
    doc = AUTHORED.get(name, {})
    gallery = state_gallery(name)
    table = states_table(c["states"], name) + state_grounds(state_tokens(c["states"], c["roles"]))
    out = []

    def sec(sid, title, note, body):
        """A note may be a string, or (what a reader needs, what the machinery is).

        THE SECOND HALF WAS THE PAGE'S BIGGEST BLOCK OF TEXT AND NOBODY CAME FOR
        IT. The note above Live ran ten lines about frames, viewports and why a
        scope is present, above a control 196px tall; the note above States ran
        eleven about pointers and settling; the census note ran fourteen. All of
        it is true and worth keeping, and none of it is what a person opening the
        page of a switch is looking for. So a note is a sentence, and everything
        that explains how the sentence was arrived at folds into a disclosure the
        reader opens on purpose."""
        if not body:
            return
        out.append((sid, title, note, body))

    # THE THING FIRST. Until 2026-08-05 this page opened with two blocks of prose
    # and put the component third, 750px down, after 1,900 characters about it.
    # Measured on the switch: the page was 5,618px tall and 13,040 characters, and
    # the live control was 196px of it - three and a half per cent. A stand whose
    # subject is the smallest thing on it is a document about a design system
    # rather than one. So Live opens the page, and every sentence that used to
    # stand between a reader and the control now stands under it.
    sec("live", "Live",
        ("These are live pages and not pictures. Hover them, press them, Tab into them.",
         "The component in the markup it ships with, quoted from the frozen kit, inside the "
         "product's own wrapper and painted by <code>components/index.css</code> alone. Each frame "
         "is a page of its own, so the width under the title is a real viewport and the media "
         "queries answer to it. One row per CONTROL, in one column, and a scope is present only "
         "where the scope is what the row is about: twelve of the sixteen combinations the product "
         "wears were measured against the same markup with no scope above them and came out "
         "identical over thirteen properties, so a plate around those would be showing the reader "
         "a dialog to prove something about a button. The numbers for every row are in the axis "
         "table further down, written once."), live(name))
    # the inside-of block writes its own <section>, so it goes in as a passthrough
    # rather than through sec(); it belongs directly under Live, because it is the
    # rest of the answer to "where can I see this thing"
    ins = elsewhere(name)
    if ins:
        out.append(("__passthrough__", "", "", ins))
    sec("purpose", "What it is", "", authored_block(name, "Purpose"))
    sec("anatomy", "Anatomy",
        "Which part is which, in the product's own words. Every class named here is one this "
        "file styles, and the build fails if it is not.",
        authored_block(name, "Anatomy"))
    sec("census", "Every other action in the product, and what is not one",
        ("A <code>&lt;button&gt;</code> is a tag, not a role: an <b>action</b> is a press, a "
         "<b>selector</b> carries a value, <b>navigation</b> goes somewhere. Only the actions "
         "stand live here.",
         "Reading the tag as the answer put a tab strip, a category chip, a row of the account "
         "menu and five social marks on the page called Buttons, and staged two of them live. The "
         "actions below are each sliced out of the specimen they already ship in, on the page "
         "ground with no plate under them. The other two roles are an index to the page that owns "
         "them, because a chip shown alone is a chip with its subject removed. Counted by "
         "<code>ui-kit/_worn.py</code> and held by gate 38 in both directions: a control the "
         "census cannot name fails the build, a kind named here that nothing wears fails just as "
         "loudly, an action that stands nowhere fails, and so does anything staged here that is "
         "not an action."),
        census_table(name))
    if gallery:
        sec("states", "States, as they measure",
            ("One block per distinct face. Rest says what the face IS; every row under it says "
             "only what that state MOVES.",
             "The frames above are the rendering; this is the reading of them. Every number was "
             "taken in a browser with a REAL pointer, a real Tab and the mouse button really held "
             "down (<code>ui-kit/_verify/states.cjs</code>), because a hover value is the cascade "
             "resolved and cannot be read out of a declaration. Nothing here is a state faked with "
             "a stand class. Two elements that measure the same in all four states in both themes "
             "are one answer, however many screens carry them, and that grouping is computed "
             "rather than chosen. The ring is the tenth value and it joined on 2026-08-05: "
             "<code>outline</code> is drawn outside the border box, so it is not the face in the "
             "strict sense, and for a stage this page said so and reported that focus moves "
             "nothing on 93 groups, which is the one state whose whole content it was not "
             "reading. The numbers go "
             "stale the moment a rule changes, so each block records the files it was measured "
             "from and <code>python3 ui-kit/_states.py</code> fails when their bytes move."),
            gallery)
    else:
        sec("states", "States",
            "Hover and focus are not faked here with a stand class. The frames above are live, so "
            "hover them; what follows is what the file says will move.", table)
    sec("when", "When to use",
        "The judgement a generator cannot read out of css, and the reason "
        "<code>ui-kit/authored/%s.md</code> exists." % name,
        authored_block(name, "When to use"))
    rule = authored_block(name, "Rule")
    anti = authored_block(name, "Anti-rule")
    if rule or anti:
        sec("rule", "The rule, and the anti-rule",
            "One sentence to follow and one mistake worth naming. An anti-rule has to name the "
            "component that should have been used instead, or it is a complaint rather than an "
            "address, and the build checks that it does.",
            ('<div class="ck-rule"><b>Do</b>%s</div>' % rule if rule else "") +
            ('<div class="ck-rule ck-anti"><b>Never</b>%s</div>' % anti if anti else ""))
    out.append(("__constraints__", "", "", constraints(name)))
    sec("roles", "Roles it reads",
        "Colour comes in only through these. Change one on <a href=\"tokens.html\">the token "
        "page</a> and it changes here and on every screen at once.", role_swatches(c["roles"]))
    sec("classes", "Classes",
        "Every class this file styles, and how many of the %d painted screens carry it. A zero is "
        "not automatically dead: the last column says whether the class is built at runtime, shown "
        "only in the kit, a leftover of the grey wireframes, used by a course page, or genuinely "
        "used by nothing. Gate 30 fails the build on the last kind." % len(uv_classes),
        class_table(c["classes"]))
    sec("screens", "Where it stands", "", screen_links(c["screens"]))
    sec("sources", "Written from",
        ("The one artefact here no gate can read, because a sentence cannot be checked for being "
         "true. Read it if you doubt a claim above.",
         "So the authored half names its sources before it says anything, and the build fails "
         "when one of them does not exist."), authored_block(name, "Sources"))
    sec("css", "What the file says",
        "The selectors and the css, for a person about to edit them. To change this component, "
        "edit <code>components/%s.css</code>; to change a value it reads, edit the role in "
        "<code>components/tokens.css</code>." % name,
        # BOTH HALVES OF THIS SECTION ARE FOR THE SAME PERSON, so both are
        # folded the same way. The source already was; the state-rule table was
        # not, and it is the visible half of a section that measures 15.3 per
        # cent of the switch's page and 13.5 of the card's, standing open under
        # a heading that says it is for somebody about to edit the file. A
        # reader who is not about to edit it scrolls past a table of selectors;
        # a reader who is opens the file anyway.
        (('<details class="ck-src"><summary>every state rule, and what it moves'
          '</summary>%s</details>' % table) if gallery else "") +
        '<details class="ck-src"><summary>components/%s.css</summary><pre>%s</pre></details>'
        % (name, esc(c["css"])))

    html = []
    for sid, title, note, body in out:
        if sid in ("__constraints__", "__passthrough__"):
            html.append(body)          # writes its own <section> and its own number
            continue
        lead, folded = (note if isinstance(note, tuple) else (note, ""))
        head = ('    <p class="tk-note">%s</p>\n' % lead) if lead else ""
        if folded:
            head += ('    <details class="tk-how"><summary>How this is read</summary>'
                     '<p class="tk-note">%s</p></details>\n' % folded)
        html.append('  <section class="tk-sec" id="%s">\n    <h2 data-n="00">%s</h2>\n%s%s\n'
                    '  </section>\n' % (sid, esc(title), head, body))
    # THE NUMBERS ARE THE READING ORDER, so they are stamped last and over
    # everything. Two of these sections bring their own markup and their own
    # hard-coded number (the constraints block, the inside-of block), and a page
    # whose numbers run 05, 06, 07, 07, 08 is a page that was assembled rather
    # than written. Counting here is the only place that can see all of them.
    page, n = [], 0
    for chunk in re.split(r'(data-n="\d+")', "".join(html)):
        if re.fullmatch(r'data-n="\d+"', chunk):
            n += 1
            chunk = 'data-n="%02d"' % n
        page.append(chunk)
    return "".join(page)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - {label}</title>
{theme_boot}
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
    <p>{note}</p>
    <div class="tk-badges">
      <span class="tk-badge">components/{name}.css</span>
      <span class="tk-badge">{rules} rules</span>
      <span class="tk-badge">{nclasses} classes</span>
      <span class="tk-badge">{nscreens} screens</span>
    </div>
  </header>
{sections}
</main>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""

built = []
for path in sorted(COMP.glob("*.css")):
    name = path.stem
    # index is the entry point, tokens are the values, fonts are eighteen
    # @font-face rules that style nothing: none of the three is a component with
    # a stand, and gate 2 has said so about all three since step 8. This loop
    # only knew about two, so re-running it built ui-kit/fonts.html, a page whose
    # own quoted css names a font host and fails gate 20.
    if name in ("index", "tokens", "fonts"):
        continue
    c = parse_component(name)
    page = PAGE.format(
        theme_boot=THEME_BOOT, name=name, label=LABEL.get(name, name), note=esc(NOTE.get(name, (
            "Every rule that paints this component, in one file. "
            "Colour through a role, geometry straight from a primitive."))),
        rules=c["rules"], nclasses=len(c["classes"]), nscreens=len(c["screens"]),
        sections=sections_for(name, c))
    (KIT / (name + ".html")).write_text(page, encoding="utf-8")
    built.append((name, c))

# ------------------------------------------------------------------ registry --
entries = []
for group, names in GROUPS:
    for n in names:
        if n in ("tokens", "icons", "patterns") or n in _PAT_STEMS \
                or (COMP / (n + ".css")).exists():
            entries.append((group, n, n + ".html", LABEL.get(n, n), code_path(n)))
extra = [n for n, _ in built if n not in [e[1] for e in entries]]
for n in sorted(extra):
    entries.append(("Unfiled", n, n + ".html", LABEL.get(n, n), code_path(n)))

nav = ["""/* ui-kit/_nav.js - the ONE registry of stand pages.

   It renders two things from the same list: the cards on overview.html and the
   kit-only side panel on every stand page. A component without a line here does
   not exist as far as the system is concerned. Own namespace (window.KIT_NAV) so
   it never collides with the course roadmap renderer in the repo root.
   Generated by _gen_component_pages.py. No em dash. */
window.KIT_DOORS = %s;
window.KIT_DOCS = %s;
window.KIT_NAV = [""" % (json.dumps([{"label": a, "file": b, "blurb": d}
                                     for a, b, d in FOUNDATION_DOORS]),
                         json.dumps([{"name": "doc-" + s, "file": s + ".html",
                                      "label": lab, "blurb": blurb}
                                     for s, lab, blurb in DOC_PAGES]))]
for g, n, f, l, path in entries:
    nav.append('  {group: %s, name: %s, file: %s, label: %s, path: %s},'
               % (json.dumps(g), json.dumps(n), json.dumps(f), json.dumps(l), json.dumps(path)))
nav.append("""];

%(REVEAL_BODY)s

(function () {
  var host = document.querySelector('[data-kit-nav]');
  var current = document.body.getAttribute('data-kit-page') || '';
  if (host) {
    // The back arrow leaves the system for the thing the system is for: the
    // painted screens. Overview is not a component, so it is not in the
    // registry below; it is its own row above the first group, the way the
    // screens have an Overview row above their families.
    var h = ['<a href="../ui-visual/overview.html" class="sidebar-back"><span class="bk-arrow" aria-hidden="true">&larr;</span> Painted screens</a>',
             '<div class="sidebar-brand"><div class="sidebar-project-name">Design system</div></div>',
             // the switch acts on the page, not on the tree, so it sits above the
             // tree: the panel is 40 rows long and a control at its foot needs scrolling
             '<button type="button" class="theme-switch" aria-pressed="false"><span class="ts-swatches" aria-hidden="true"><span class="ts-sw ts-dark"></span><span class="ts-sw ts-light"></span></span><span class="ts-label">Vault</span></button>',
             '<nav class="sidebar-nav" aria-label="Design system">',
             '<a href="overview.html" class="sidebar-page-link' + (current === 'overview' ? ' active' : '') + '">Overview</a>'];
    // The group you are IN is marked as well as the page you are ON. The tree is
    // 45 rows in a panel that shows about 25, so on most pages the brass row is
    // below the fold and the panel opens saying nothing about where you are. The
    // screens tree has always marked the family; this is the same answer, and it
    // is what makes the two panels one vocabulary rather than two.
    var here = null;
    window.KIT_NAV.forEach(function (e) { if (e.name === current) here = e.group; });
    var group = null;
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== group) {
        group = e.group;
        h.push('<div class="sidebar-divider' + (group === here ? ' active' : '') +
               '">' + group + '</div>');
      }
      h.push('<a href="' + e.file + '" class="sidebar-page-link' + (e.name === current ? ' active' : '') + '">' + e.label + '</a>');
      if (e.name === 'tokens') {
        h.push('<div class="sidebar-sub">');
        window.KIT_DOORS.forEach(function (d) {
          h.push('<a href="' + d.file + '" class="sidebar-sub-link">' + d.label + '</a>');
        });
        h.push('</div>');
      }
    });
    // The documents are the last group and not the first, because they are the
    // reasoning and the components are the thing. They are pages of the vitrine
    // like any other, so they are rows in the same tree: a link that leaves for
    // a .md file is a link out of the browser.
    var inDocs = window.KIT_DOCS.some(function (d) { return d.name === current; });
    h.push('<div class="sidebar-divider' + (inDocs ? ' active' : '') + '">The reasoning</div>');
    window.KIT_DOCS.forEach(function (d) {
      h.push('<a href="' + d.file + '" class="sidebar-page-link' + (d.name === current ? ' active' : '') + '">' + d.label + '</a>');
    });
    h.push('</nav>');
    // why.html is here and NOT a row in the tree above, and the difference is
    // what the tree is: a registry of things the system HAS. The guide is not a
    // component, a pattern or a document of the reasoning; it is the way in for
    // someone who has none of that vocabulary yet, so it sits where a person
    // looks when the tree has not helped. Gate 22 accepts a page off the tree
    // only when something still links it, and this is that link.
    // ON ONE LINE, and the comment may not name the class either. Gate 22 finds
    // this note by searching for its class name and reading to the end of the
    // LINE, so two things break it and both did: splitting the push across two
    // JS lines hides every link after the first, and writing the class name in a
    // comment ABOVE the push makes the search land on the comment, which has no
    // links at all. The second one turned shell.html and why.html unreachable in
    // the same run, from a comment that was explaining the first one.
    h.push('<div class="sidebar-note">New here? <a href="why.html">Why the system is like this</a><br>The kit itself: <a href="kit.html">kit.html</a>, <a href="shell.html">shell.html</a>, <a href="selftest.html">self test</a></div>');
    host.innerHTML = h.join('');
    // the tree exists only now, so the reveal happens here and not on load
    %(REVEAL_CALL)s
  }
  var cards = document.getElementById('kitCards');
  if (cards) {
    var g = null, out = [];
    window.KIT_NAV.forEach(function (e) {
      if (e.group !== g) { g = e.group; out.push('</div><h3 class="tk-subh">' + g + '</h3><div class="ck-cards">'); }
      var thumb = window.KIT_THUMBS && window.KIT_THUMBS[e.name];
      // A CARD WITH NO SPECIMEN IS A DOOR, and it has to say so. Two of the
      // sixty have none - the token page and the pattern index, which are pages
      // OF the system rather than components IN it - and in a grid row that
      // stretches to the tallest card they stood as a 224px plate with a label
      // at the bottom and nothing above it, which reads exactly like a
      // thumbnail that failed to load.
      out.push('<a class="ck-card' + (thumb ? '' : ' ck-card-door') + '" href="' + e.file + '">' +
               (thumb ? '<span class="ck-thumb"><iframe src="' + thumb.src +
                        '" width="' + thumb.w + '" height="' + thumb.h +
                        '" style="transform:scale(' + thumb.s + ')" loading="lazy" tabindex="-1" aria-hidden="true" title=""></iframe></span>' : '') +
               '<b>' + e.label + '</b><code>' + e.path + '</code></a>');
    });
    cards.innerHTML = (out.join('') + '</div>').replace(/^<\\/div>/, '');
  }
  var doors = document.getElementById('kitDoors');
  if (doors) {
    doors.innerHTML = window.KIT_DOORS.map(function (d) {
      return '<a class="ck-card" href="' + d.file + '"><b>' + d.label + '</b><code>' + d.blurb + '</code></a>';
    }).join('');
  }
  var docs = document.getElementById('kitDocs');
  if (docs) {
    docs.innerHTML = window.KIT_DOCS.map(function (d) {
      return '<a class="ck-card" href="' + d.file + '"><b>' + d.label + '</b><code>' + d.blurb + '</code></a>';
    }).join('');
  }
  var sb = document.querySelector('[data-kit-nav]'), ov = document.getElementById('rmOverlay'), tg = document.getElementById('rmToggle');
  if (sb && ov && tg) {
    var o = function () { sb.classList.add('open'); ov.classList.add('open'); },
        c = function () { sb.classList.remove('open'); ov.classList.remove('open'); };
    tg.addEventListener('click', o); ov.addEventListener('click', c);
  }
})();
""" % {"REVEAL_BODY": REVEAL_BODY, "REVEAL_CALL": REVEAL_CALL})
(KIT / "_nav.js").write_text("\n".join(nav), encoding="utf-8")

# ------------------------------------------------------------------ frames ---
(KIT / "_frames.js").write_text("""/* ui-kit/_frames.js - the parent half of the specimen frame handshake.

   A specimen is a page of its own, so the vitrine cannot measure it by reading
   its document: under file:// every document has its own opaque origin. The
   specimen posts its height instead, which crosses origins by design. The frame
   is matched by identity (contentWindow), not by the origin string, because
   from file:// that string is "null" for everyone. No em dash. */
(function () {
  /* A specimen is rendered at the width it declares, because that width is what
     its media queries answer to. When the column is narrower, the frame is
     scaled down rather than squeezed: the layout stays the layout, and the
     label says what it is being shown at. */
  function fit(f) {
    var box = f.parentElement, w = +f.getAttribute('width');
    /* The available width is the figure's, not the box's: the box is about to be
       resized to whatever we decide, so measuring it would measure our own
       previous answer. */
    var avail = box.parentElement.clientWidth;
    var s = Math.min(1, avail / w);
    var h = parseFloat(f.style.height || f.getAttribute('height'));
    f.style.transformOrigin = '0 0';
    f.style.transform = s < 1 ? 'scale(' + s + ')' : 'none';
    /* The border hugs the specimen instead of leaving a strip of empty canvas. */
    box.style.width = Math.ceil(w * s) + 'px';
    box.style.height = Math.ceil(h * s) + 'px';
    var tag = box.parentElement.querySelector('.ck-zoom');
    if (tag) { tag.textContent = s < 1 ? Math.round(s * 100) + '%' : ''; tag.hidden = s >= 1; }
  }

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.specimen || !(d.height > 0)) return;
    var frames = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        frames[i].style.height = d.height + 'px';
        fit(frames[i]);
        return;
      }
    }
  });
  window.addEventListener('resize', function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) fit(f[i]);
  });
  /* A frame that finished before this script ran has already spoken and will
     not speak again, so ask it once it is there. */
  var ask = function (f) {
    try { f.contentWindow.postMessage({ping: true}, '*'); } catch (err) {}
  };
  var all = function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) { ask(f[i]); f[i].addEventListener('load', ask.bind(null, f[i])); }
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all);
  else all();
  window.addEventListener('load', all);
})();
""", encoding="utf-8")

# ---------------------------------------------------------------------- hub ---
THUMB_W = 236
thumbs = {}
for s in SPECIMENS:
    if s["component"] in thumbs:
        continue
    w = s.get("width", 900)
    scale = round(THUMB_W / w, 4)
    thumbs[s["component"]] = {"src": "specimens/%s.html" % s["id"], "w": w,
                              "h": int(140 / scale), "s": scale}
# A pattern has no specimen, so its card frames the scene page directly. That is
# the whole reason the src is a field now instead of a specimen id: two kinds of
# page feed the same card, and a hard-coded specimens/ prefix could only ever
# show one of them.
for _p in _PAT_STEMS:
    _scale = round(THUMB_W / 360, 4)
    thumbs[_p] = {"src": "patterns/%s.html" % _p, "w": 360,
                  "h": int(140 / _scale), "s": _scale}

total_rules = sum(c["rules"] for _, c in built)
hub = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Design system</title>
{THEME_BOOT}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="overview">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<main class="tk-wrap">
  <header class="tk-hero">
    <h1>The system</h1>
    <p>Two levels of tokens, {len(built)} component files and {len(_PAT_STEMS)} patterns. The code
    lives in <code>components/</code> and is what a screen links; these pages are the vitrine, and
    they link the same <code>components/index.css</code> the product does, so nothing here can drift
    from what ships.</p>
    <div class="tk-badges">
      <span class="tk-badge">{len(built)} components</span>
      <span class="tk-badge">{len(_PAT_STEMS)} patterns</span>
      <span class="tk-badge">{total_rules} rules</span>
      <span class="tk-badge">{len(SPECIMENS)} specimens</span>
      <span class="tk-badge">one entry point</span>
    </div>
    <div class="tk-theme">{THEME_BUTTON_INLINE}<span class="tk-theme-note">The whole product, on the
      other ground. Only roles move; not one primitive is redefined. Section 3 of
      <code>components/tokens.css</code> is the entire theme.</span></div>
    <div class="tk-jump"><a href="why.html">Why it is like this</a><a href="tokens.html">Tokens</a>
      <a href="icons.html">Icons</a><a href="patterns.html">Patterns</a><a href="kit.html">Frozen kit</a><a href="selftest.html">Self test</a>
      <a href="../ui-visual/overview.html">Painted screens</a></div>
  </header>

  <!-- THE SYSTEM FIRST, and it is the same correction the component pages took
       on 2026-08-05. This door opened with twelve TEXT cards over two sections -
       five doors into the token page and seven into the documents - and the
       first rendered component stood 1,250px down. A front door whose first
       screen is a table of contents is a contents page, and every one of those
       twelve links is already a row in the tree on the left, which is on screen
       the whole time. So the grid of live components opens the page, and the
       two card sections stand under it as what they are: ways in, for a reader
       who wants the reasoning rather than the thing. -->
  <section class="tk-sec" id="cards">
    <h2 data-n="01">Every file, every page</h2>
    <p class="tk-note">Every component in the system, live. One component is one css file, one page
    here and one line in the registry, and missing any of the three means it does not exist yet.</p>
    <details class="tk-how"><summary>How this is read</summary><p class="tk-note">Each card frames
    the component's own specimen, scaled down and made inert, so it cannot go stale the way a
    screenshot does. The groups are the levels, computed from what each component contains by
    <code>python3 ui-kit/_levels.py</code> and declared where the map is blind. The last group is
    the second level of the system: a <a href="patterns.html">pattern</a> is an arrangement that
    repeated on three or more screens, and it has a file and a page but no level, no specimen and
    no states. Its card frames the pattern itself, because that page is the only place a pattern
    exists outside the product.</p></details>
    <div id="kitCards"></div>
  </section>

  <section class="tk-sec" id="foundations">
    <h2 data-n="02">Foundations</h2>
    <p class="tk-note">Colour, material, geometry, type and motion are one page, because they are one
    file: <code>components/tokens.css</code> generates all of it. These are the doors into it.</p>
    <div class="ck-cards" id="kitDoors"></div>
  </section>

  <section class="tk-sec" id="docs">
    <h2 data-n="03">The reasoning</h2>
    <p class="tk-note">Why the system is shaped like this, what it was read out of, and what each
    part reaches. Rendered from <code>ui-kit/docs/</code> by <code>ui-kit/_gen_docs.py</code>; the
    markdown stays the source.</p>
    <div class="ck-cards" id="kitDocs"></div>
  </section>
</main>

<script>window.KIT_THUMBS = {json.dumps(thumbs)};</script>
<script src="_nav.js"></script>
</body>
</html>
"""
(KIT / "overview.html").write_text(hub, encoding="utf-8")

# ----------------------------------------------------------------- coverage --
rows = []
buckets = {}
for name, c in built:
    mine = [s for s in SPECIMENS if s["component"] == name]
    inside = [s for s in SPECIMENS if name in s.get("also", [])]
    rows.append("| %s | %d | %s | %d | %d | %d |" % (
        name, len(mine), ", ".join(s["id"] for s in mine) or "-",
        len(inside), len(c["owned"]), len(c["screens"])))
    for cls in c["classes"]:
        kind, why = where(cls)
        if kind:
            buckets.setdefault(kind, []).append((cls, name, why))

ORDER = [("unused", "Deletion candidates", "Styled, and carried by no element in the repo: not by a "
          "painted screen, not by the kit, not by a wireframe, not by a course page, and not by any "
          "script. Nothing is removed yet. The screens still carry their own inline style and only "
          "move onto components/index.css in step 5, so the measurement is not final until then; "
          "step 7 is the pass that acts on this list."),
         ("wireframe", "Carried only by the grey tree", "Dead, and this section used to say the "
          "opposite: it called them the wireframe version of a block the paint replaced and said "
          "removing them needed the markup gone from wireframes/ first. It does not. wireframes/ "
          "carries its own inline grey-box css and never links index.css, so no rule in components/ "
          "has ever applied to it, and a class carried only there is a class this sheet does not "
          "have. Step 7e deleted the ones that were left and took wireframes/ out of gate 14's "
          "markup scan, which had been keeping them alive."),
         ("docs", "Used only by a course page", "Carried by a page in ia/, concept/, research/, "
          "voice/ or user-research/. Those pages have their own inline styles and do not load the "
          "system, so the rule here reaches nothing."),
         ("kit", "Shown in the kit, not in the product", "A real component the painted screens have "
          "not adopted. An offer, not debris. Do not delete without deciding against it first."),
         ("runtime", "Built or toggled at runtime", "Never written into a file. Deleting any of "
          "these breaks a screen silently, because the grep that says they are unused is wrong.")]

sections = []
for kind, title, blurb in ORDER:
    items = sorted(buckets.get(kind, []))
    sections.append("### %s (%d)\n\n%s\n\n| class | file | why |\n|---|---|---|\n%s\n"
                    % (title, len(items), blurb,
                       "\n".join("| `.%s` | %s.css | %s |" % (c, f, w) for c, f, w in items)
                       or "| - | - | none |"))

(KIT / "docs" / "coverage.md").write_text("""# Vitrine coverage

Generated by `ui-kit/_gen_component_pages.py`. Do not edit by hand.

What each column means: **own** is how many specimens the component's page renders itself, **inside**
is how many other specimens contain it and link to it instead of repeating it, **classes** is how many classes the
file OWNS (a class it styles with the fewest ancestors; a class it only reaches through someone
else's belongs to that someone else), and **screens** is how many of the %d painted screens carry at
least one of them. Counting every class a file merely mentions is what made this column read 76 for
thirty-four of thirty-six components, a market-depth panel included.

A component with 0 own specimens does not exist as far as the vitrine is concerned, and the build
says so. No em dash.

| component | own | specimens | inside | classes | screens |
|---|---|---|---|---|---|
%s

%d specimens over %d components.

---

## Classes the painted screens do not carry

Every class styled in `components/` that no `ui-visual` screen puts on an element, sorted by what
that actually means. The Classes table on each component page shows the same verdict per row.

%s
""" % (len(uv_classes), "\n".join(rows), len(SPECIMENS), len(built), "\n".join(sections)),
    encoding="utf-8")

# ------------------------------------------------- the css header line -------
# The `Classes:` and `Stands on:` lines in each component file used to be prose
# someone typed once. They said the truth and coverage.md said 76, and a reader
# had no way to know which to believe. They are written from the same OWNER map
# now, so there is one computation and two places that read it. Idempotent: the
# line is replaced, never appended, and a file that carries neither is left alone
# (base.css and course-chrome.css describe themselves in a sentence instead).
hdr_written = 0
for name, c in built:
    path = COMP / (name + ".css")
    text = path.read_text(encoding="utf-8")
    if "*/" not in text:
        continue
    head, rest = text[:text.index("*/") + 2], text[text.index("*/") + 2:]
    before = head
    if "Classes:" in head:
        head = re.sub(r"Classes:[^\n]*",
                      "Classes: %s." % ", ".join("." + x for x in c["owned"]), head, count=1)
    if "Stands on:" in head:
        shown = ", ".join(c["screens"][:5]) + (", ..." if len(c["screens"]) > 5 else "")
        head = re.sub(r"Stands on:[^\n]*",
                      "Stands on: %d ui-visual screens (%s)" % (len(c["screens"]), shown or "none"),
                      head, count=1)
    if head != before:
        path.write_text(head + rest, encoding="utf-8")
        hdr_written += 1

print("built %d component pages + overview.html + _nav.js + _frames.js + docs/coverage.md, %d css headers" % (len(built), hdr_written))
missing = [n for n, _ in built if not any(s["component"] == n for s in SPECIMENS)]
if missing:
    print("no specimen of its own:", ", ".join(missing))
