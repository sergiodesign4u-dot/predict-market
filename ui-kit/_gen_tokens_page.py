#!/usr/bin/env python3
"""Build ui-kit/tokens.html from components/tokens.css.

The stand page for the token file: every primitive shown as the thing it is (a
swatch, a bar, a radius, a type size, a grain), and every semantic role shown
with the primitive it points at, the value that resolves out of the chain, and
the usage it was read from. The page LINKS the real tokens.css, so a colour on
screen is the colour in the file; only the names, the values and the notes are
generated text.

Idempotent: rewrites ui-kit/tokens.html from scratch on every run. Never edits
components/ or ui-visual/. Run after any edit to tokens.css.

    python3 ui-kit/_gen_tokens_page.py
"""
import os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "components" / "tokens.css"
OUT = ROOT / "ui-kit" / "tokens.html"

# ---------------------------------------------------------------- parsing ---

def parse(text):
    """-> [ {title, note, tokens:[{name,value,comment}]} ] for one level."""
    groups, cur = [], {"title": "", "note": "", "tokens": []}
    i, n, last_end, pending = 0, len(text), -1, ""
    while i < n:
        if text.startswith("/*", i):
            end = text.find("*/", i)
            if end == -1:
                break            # a section header cut off by the level split
            j = end + 2
            body = text[i + 2:j - 2].strip()
            between = text[last_end:i] if last_end != -1 else "\n"
            if cur["tokens"] and "\n" not in between and last_end != -1:
                cur["tokens"][-1]["comment"] = clean(body)     # trailing: same line as the value
            elif "----" in body:
                head, _, rest = body.partition("\n")
                if cur["tokens"] or cur["title"]:
                    groups.append(cur)
                cur = {"title": head.strip().strip("-").strip(), "note": clean(rest), "tokens": []}
                pending = ""
            else:
                pending = clean(body)                          # leading: belongs to the next value
            i = j
            continue
        if text.startswith("--", i):
            m = re.match(r"(--[\w-]+)\s*:", text[i:])
            if m:
                name = m.group(1)
                k = i + m.end()
                depth, start = 0, k
                while k < n:
                    c = text[k]
                    if c == "(":
                        depth += 1
                    elif c == ")":
                        depth -= 1
                    elif c in ";}" and depth == 0:
                        break   # the last declaration of a block may have no semicolon
                    k += 1
                value = " ".join(text[start:k].split())
                cur["tokens"].append({"name": name, "value": value, "comment": pending})
                pending = ""
                i = last_end = k + 1
                continue
        i += 1
    if cur["tokens"] or cur["title"]:
        groups.append(cur)
    return groups


def clean(s):
    return " ".join(s.replace("*", " ").split()).strip(" -")


src = SRC.read_text(encoding="utf-8")
head_end = src.index("1. PRIMITIVE")
split = src.index("2. SEMANTIC")
PRIM = parse(src[head_end:split])
SEM = parse(src[split:])

# the one responsive token is declared twice (base + the mobile @media). Keep the
# base declaration in "page frame" and remember the override for the caption.
GUTTER_MOBILE = ""
for g in PRIM:
    if "page frame" not in g["title"].lower():
        for t in list(g["tokens"]):
            if t["name"] == "--gutter":
                GUTTER_MOBILE = t["value"]
                g["tokens"].remove(t)

FLAT = {}
for g in PRIM + SEM:
    for t in g["tokens"]:
        FLAT[t["name"]] = t["value"]


def resolve(value, depth=0):
    """follow var() chains down to a literal"""
    if depth > 8:
        return value
    m = re.fullmatch(r"var\((--[\w-]+)\)", value.strip())
    if m and m.group(1) in FLAT:
        return resolve(FLAT[m.group(1)], depth + 1)
    return value


# --------------------------------------------------------------- contrast ---

def rgb(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3})", v)
    if m:
        return tuple(int(c * 2, 16) for c in m.group(1)) + (1.0,)
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        h = m.group(1)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
    m = re.fullmatch(r"rgba?\(([^)]*)\)", v)
    if m:
        p = [x.strip() for x in m.group(1).split(",")]
        a = float(p[3]) if len(p) > 3 else 1.0
        return (int(p[0]), int(p[1]), int(p[2]), a)
    return None


def over(fg, bg):
    """composite fg (with alpha) over opaque bg"""
    if fg[3] >= 1:
        return fg[:3]
    return tuple(round(fg[i] * fg[3] + bg[i] * (1 - fg[3])) for i in range(3))


def lum(c):
    def ch(x):
        x /= 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def ratio(fg_tok, bg_tok, tint_tok=None):
    fg, bg = rgb(resolve(FLAT[fg_tok])), rgb(resolve(FLAT[bg_tok]))
    if not fg or not bg:
        return None
    base = bg[:3]
    if tint_tok:
        t = rgb(resolve(FLAT[tint_tok]))
        if t:
            base = over(t, base)
    f = over(fg, base)
    l1, l2 = sorted((lum(f), lum(base)), reverse=True)
    return round((l1 + 0.05) / (l2 + 0.05), 2)


PAIRS = [
    ("--text-primary", "--bg-page", None, "body text on the page"),
    ("--text-primary", "--bg-plate", None, "text on the content plate"),
    ("--text-primary", "--bg-surface", None, "text on a card, header, dialog"),
    ("--text-primary", "--bg-control", None, "label inside a quiet control"),
    ("--text-muted", "--bg-page", None, "secondary line on the page"),
    ("--text-muted", "--bg-plate", None, "secondary line on the plate"),
    ("--text-muted", "--bg-surface", None, "secondary line on a card"),
    ("--text-icon", "--bg-surface", None, "default icon stroke"),
    ("--text-brass", "--bg-page", None, "brass link on the page"),
    ("--text-brass", "--bg-surface", None, "brass link on a card"),
    ("--text-brass-lit", "--bg-plate", None, "hero and SEO brass"),
    ("--text-brass-chip", "--bg-chip", None, "active chip label"),
    ("--text-on-brass", "--color-action", None, "label on a brass CTA"),
    ("--text-on-yes", "--outcome-yes", None, "label on a filled YES"),
    ("--text-on-no", "--outcome-no", None, "label on a filled NO"),
    ("--outcome-yes-text", "--bg-surface", "--outcome-yes-fill", "tinted YES button"),
    ("--outcome-no-text", "--bg-surface", "--outcome-no-fill", "tinted NO button"),
    ("--result-won-text", "--bg-card-quiet", "--result-won-fill", "WON chip"),
    ("--result-lost-text", "--bg-card-quiet", "--result-lost-fill", "LOST chip"),
    ("--chrome-text", "--chrome-bg", None, "course sidebar"),
]

# ------------------------------------------------------------------ render --

SAMPLES = ["Will the ECB cut rates in March?", "Confirm bet", "You were right",
           "USDC held 1:1, we never lend it", "Browse events", "Add funds",
           "Here is what happened", "Save into Favorites"]

COLOUR_GROUPS = ("graphite", "bone", "brass", "plum", "green", "red", "neutral")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ramp_strip(tokens):
    """the opaque steps of a colour family, side by side and sorted by lightness,
       so the ramp reads as a ramp and not as 20 near-black tiles"""
    steps = []
    for t in tokens:
        c = rgb(resolve(t["value"]))
        if c and c[3] >= 1:
            steps.append((lum(c[:3]), t))
    if len(steps) < 3:
        return ""
    steps.sort()
    cells = "".join(
        f'<i style="background:var({t["name"]})" title="{esc(t["name"])} {esc(resolve(t["value"]))}">'
        f'<b>{esc(t["name"].rsplit("-", 1)[-1])}</b></i>' for _, t in steps)
    return f'<div class="tk-ramp">{cells}</div>'


def swatch_grid(tokens):
    out = ['<div class="tk-swatches">']
    for t in tokens:
        val = resolve(t["value"])
        out.append(
            f'<div class="tk-sw"><span class="tk-sw-chip"><i style="background:var({t["name"]})"></i></span>'
            f'<span class="tk-sw-meta"><b class="tk-sw-name">{esc(t["name"])}</b>'
            f'<span class="tk-sw-val">{esc(val)}</span>'
            + (f'<span class="tk-sw-cmt">{esc(t["comment"])}</span>' if t["comment"] else "")
            + "</span></div>")
    out.append("</div>")
    return "\n".join(out)


def px(v):
    m = re.match(r"([\d.]+)px", v)
    return float(m.group(1)) if m else None


def scale_rows(tokens, cap=None):
    out = ['<div class="tk-scale">']
    mx = max((px(resolve(t["value"])) or 0) for t in tokens) or 1
    for t in tokens:
        v = px(resolve(t["value"])) or 0
        w = min(100, v / (cap or mx) * 100)
        out.append(f'<div class="tk-scale-row"><span class="tk-scale-lbl">{esc(t["name"])} '
                   f'{esc(resolve(t["value"]))}</span>'
                   f'<span class="tk-scale-bar" style="width:{w:.1f}%"></span></div>')
    out.append("</div>")
    return "\n".join(out)


def role_table(g):
    rows = []
    for t in g["tokens"]:
        target = re.fullmatch(r"var\((--[\w-]+)\)", t["value"].strip())
        target = target.group(1) if target else t["value"]
        val = resolve(t["value"])
        from_note = t["comment"]
        if from_note.lower().startswith("from:"):
            from_note = from_note[5:].strip()
        rows.append(
            f'<tr><td><span class="tk-dot" style="background:var({t["name"]})"></span></td>'
            f'<td class="tk-role">{esc(t["name"])}</td>'
            f'<td class="tk-points">{esc(target)}</td>'
            f'<td class="tk-hex">{esc(val)}</td>'
            f'<td class="tk-from">{esc(from_note)}</td></tr>')
    note = f'<p class="tk-note">{esc(g["note"])}</p>' if g["note"] else ""
    return (f'<h3 class="tk-subh">{esc(g["title"])}</h3>{note}'
            '<table class="tk-tbl"><thead><tr><th></th><th>role</th><th>points at</th>'
            '<th>resolves to</th><th>read from</th></tr></thead><tbody>'
            + "\n".join(rows) + "</tbody></table>")


def find(groups, key):
    return [g for g in groups if key in g["title"].lower()]


parts = []

# ---- primitive: colours
for g in PRIM:
    low = g["title"].lower()
    if not any(k in low for k in COLOUR_GROUPS):
        continue
    parts.append(f'<h3 class="tk-subh">{esc(g["title"])}</h3>')
    if g["note"]:
        parts.append(f'<p class="tk-note">{esc(g["note"])}</p>')
    parts.append(ramp_strip(g["tokens"]))
    parts.append(swatch_grid(g["tokens"]))
colour_html = "\n".join(parts)

# ---- primitive: material
mat = find(PRIM, "material")[0]
mat_html = ['<div class="tk-mats">']
for t in mat["tokens"]:
    if "grain" in t["name"]:
        # the product paints a grain the same way: over the stone, blended, never on its own
        style = (f'background-color:var(--bg-plate);background-image:var({t["name"]});'
                 f'background-blend-mode:overlay')
    elif "grid" in t["name"]:
        style = f'background-color:var(--bg-card);background-image:var({t["name"]})'
    else:
        style = f'background:var(--bg-plate) var({t["name"]}) no-repeat center/40px'
    mat_html.append(f'<div class="tk-mat"><i style="{style}"></i>'
                    f'<span><b>{esc(t["name"])}</b>{esc(t["comment"] or "material")}</span></div>')
mat_html.append("</div>")
mat_html = "\n".join(mat_html)

# ---- primitive: geometry
space = find(PRIM, "space")[0]
radius = find(PRIM, "radius")[0]
sizes = find(PRIM, "control and icon")[0]
frame = find(PRIM, "page frame")[0]

radius_html = ['<div class="tk-radii">']
for t in radius["tokens"]:
    radius_html.append(f'<div class="tk-radius"><i style="border-radius:var({t["name"]})"></i>'
                       f'<span>{esc(t["name"])}<br>{esc(resolve(t["value"]))}</span></div>')
radius_html.append("</div>")
radius_html = "\n".join(radius_html)

# Three shapes, because the three families are three different things and showing
# them all as one bar is what made "control" unreadable: a control is a box a
# finger lands on, an icon is the mark inside it, a size is a piece of content.
size_html = ['<div class="tk-sizes">']
for t in sizes["tokens"]:
    v, job = resolve(t["value"]), esc(t["comment"] or "")
    if t["name"].startswith("--icon-"):
        box = (f'width:var({t["name"]});height:var({t["name"]});border-radius:var(--radius-2);'
               f'background:var(--text-icon)')
    elif t["name"].startswith("--size-"):
        box = (f'width:var({t["name"]});height:var({t["name"]});border-radius:var(--radius-2);'
               f'border:1px solid var(--border-brass)')
    else:
        box = (f'width:var({t["name"]});height:var({t["name"]});border-radius:var(--radius-10)')
    size_html.append(f'<div class="tk-size"><i style="{box}"></i>'
                     f'<span>{esc(t["name"])}<br>{esc(v)}<br><em>{job}</em></span></div>')
size_html.append("</div>")
size_html = "\n".join(size_html)

# ---- primitive: type
typ = find(PRIM, "type")[0]
fonts = [t for t in typ["tokens"] if t["name"].startswith("--font-")]
texts = [t for t in typ["tokens"] if t["name"].startswith("--text-") or t["name"].startswith("--display-")]
weights = [t for t in typ["tokens"] if t["name"].startswith("--weight-")]
leads = [t for t in typ["tokens"] if t["name"].startswith("--leading-")]

font_html = ['<div class="tk-fonts">']
for t, role in zip(fonts, ["headings, figures that must feel cut",
                           "every running line of the interface",
                           "money, odds, counts, anything a person compares"]):
    font_html.append(f'<div class="tk-font"><b style="font-family:var({t["name"]})">Predict Market</b>'
                     f'<span>{esc(t["name"])}: {esc(t["value"])}</span><i>{role}</i></div>')
font_html.append("</div>")
font_html = "\n".join(font_html)

type_html = []
for i, t in enumerate(texts):
    v = resolve(t["value"])
    fam = "--font-display" if t["name"].startswith("--display-") else "--font-body"
    type_html.append(f'<div class="tk-type-row"><span class="tk-type-lbl">{esc(t["name"])} {esc(v)}</span>'
                     f'<span class="tk-type-smp" style="font-size:var({t["name"]});font-family:var({fam})">'
                     f'{esc(SAMPLES[i % len(SAMPLES)])}</span></div>')
type_html = "\n".join(type_html)

wl_html = []
for t in weights:
    wl_html.append(f'<div class="tk-type-row"><span class="tk-type-lbl">{esc(t["name"])} {esc(t["value"])}</span>'
                   f'<span class="tk-type-smp" style="font-weight:var({t["name"]});font-size:16px">'
                   f'Confirm bet</span></div>')
for t in leads:
    wl_html.append(f'<div class="tk-type-row"><span class="tk-type-lbl">{esc(t["name"])} {esc(t["value"])}</span>'
                   f'<span class="tk-type-smp" style="line-height:var({t["name"]});font-size:13px;'
                   f'white-space:normal;max-width:52ch">You bet YES at 34 cents. The market resolved YES, '
                   f'so the payout is settled at the price you paid.</span></div>')
wl_html = "\n".join(wl_html)

# ---- primitive: motion
motion = find(PRIM, "motion")[0]
motion_html = []
for t in motion["tokens"]:
    if t["name"].startswith("--dur"):
        motion_html.append(f'<div class="tk-type-row"><span class="tk-type-lbl">{esc(t["name"])} '
                           f'{esc(t["value"])}</span><span class="tk-type-smp" style="display:block;height:14px;'
                           f'width:60px;border-radius:3px;background:var(--color-action);'
                           f'transition:width var({t["name"]}) var(--ease-out)" '
                           f'onmouseover="this.style.width=\'240px\'" '
                           f'onmouseout="this.style.width=\'60px\'"></span></div>')
    else:
        motion_html.append(f'<div class="tk-type-row"><span class="tk-type-lbl">{esc(t["name"])}</span>'
                           f'<span class="tk-type-smp" style="font-family:var(--font-mono);font-size:11px">'
                           f'{esc(t["value"])}</span></div>')
motion_html = "\n".join(motion_html)

# ---- semantic tables
sem_html = "\n".join(role_table(g) for g in SEM if g["tokens"])

# ---- contrast
crows = []
for fg, bg, tint, what in PAIRS:
    r = ratio(fg, bg, tint)
    if r is None:
        continue
    verdict = ('<span class="tk-pass">AA</span>' if r >= 4.5
               else '<span class="tk-warn">AA large</span>' if r >= 3
               else '<span class="tk-fail">below AA</span>')
    crows.append(f'<tr><td class="tk-role">{esc(fg)}</td><td class="tk-points">{esc(bg)}'
                 + (f' + {esc(tint)}' if tint else "")
                 + f'</td><td class="tk-hex">{r}:1</td><td>{verdict}</td>'
                 f'<td class="tk-from">{esc(what)}</td></tr>')
contrast_html = ('<table class="tk-tbl"><thead><tr><th>text</th><th>on</th><th>ratio</th>'
                 '<th>WCAG</th><th>where</th></tr></thead><tbody>'
                 + "\n".join(crows) + "</tbody></table>")

n_prim = sum(len(g["tokens"]) for g in PRIM)
n_sem = sum(len(g["tokens"]) for g in SEM)

SIDEBAR = """<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Tokens</title>
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="tokens">
{SIDEBAR}

<div class="tk-wrap">
  <header class="tk-hero">
    <h1>Tokens</h1>
    <p>Two levels. <b>Primitive</b> is a raw value with no opinion: a graphite step, a brass step, a
    gap, a radius, a type size. <b>Semantic</b> is a role: why this colour is in this place. A component
    reads colour only through a role, and reads geometry straight from the primitive, because a radius
    has nothing for a theme to override and a colour does.</p>
    <p>This page links the real <code>components/tokens.css</code>, so every swatch below is painted by
    the file itself. Names, values and notes are generated from it by
    <code>ui-kit/_gen_tokens_page.py</code>; the reading behind the roles is in
    <code>ui-kit/docs/tokens-audit.md</code>.</p>
    <div class="tk-badges">
      <span class="tk-badge">{n_prim} primitives</span>
      <span class="tk-badge">{n_sem} roles</span>
      <span class="tk-badge">0 new values</span>
      <span class="tk-badge">Vault</span>
    </div>
    <div class="tk-jump">
      <a href="#colour">Colour</a><a href="#material">Material</a><a href="#geometry">Geometry</a>
      <a href="#type">Type</a><a href="#motion">Motion</a><a href="#roles">Roles</a>
      <a href="#contrast">Contrast</a><a href="#log">Merges</a>
    </div>
  </header>

  <section class="tk-sec" id="colour">
    <h2 data-n="01">Colour primitives</h2>
    <p class="tk-note">Every value here already stood in the flat kit these files were split from. Nothing was
    invented for this file; the four merged pairs are marked on the swatch that survived. Transparent
    values sit on a checker so the alpha is visible.</p>
    {colour_html}
  </section>

  <section class="tk-sec" id="material">
    <h2 data-n="02">Material</h2>
    <p class="tk-note">The Vault is stone, not flat fill: each surface carries a grain, the card carries
    a brass graph grid that fades from its corner, and the wordmark carries a brass tick. These are raw
    values too, so they live in the primitive level.</p>
    {mat_html}
  </section>

  <section class="tk-sec" id="geometry">
    <h2 data-n="03">Geometry</h2>
    <p class="tk-note">Space, radius and size get no semantic level. They repeat, but they carry no
    meaning a theme or a rebrand would move, so a component reads them directly.</p>
    <h3 class="tk-subh">space</h3>
    <p class="tk-note"><b>The grid is 4px and 2 is the only half step.</b> A value off the grid is not a
    distance: 1px is a line, so it is <code>--hairline</code>, and the measurement of a thing is a
    control or a size below. The scale was 25 steps read out of the wireframe, including 1 3 5 7 9 in a
    row; each one moved to its nearest step, and a value that sat exactly between two broke toward the
    heavier one, so nothing inflated and nothing moved more than 2px.</p>
    {scale_rows(space["tokens"])}
    <h3 class="tk-subh">radius</h3>
    <p class="tk-note">One corner per job, five of them. <code>--radius-round</code> (1000px) rendered
    the same pill as <code>--radius-pill</code> on every control it touched, and
    <code>--radius-circle</code> had no consumer at all.</p>
    {radius_html}
    <h3 class="tk-subh">control and icon sizes</h3>
    <p class="tk-note">A <b>control</b> size is the height of the box a finger or a pointer lands on; an
    <b>icon</b> size is the drawn mark inside it; a <b>size</b> is a fixed piece of content. Shown at
    the real size, with the job each one is for.</p>
    {size_html}
    <h3 class="tk-subh">page frame</h3>
    {scale_rows(frame["tokens"])}
    <p class="tk-note">The gutter is the only responsive token: {esc(GUTTER_MOBILE)} below 640px, so the
    inset plate still breathes on a phone.</p>
  </section>

  <section class="tk-sec" id="type">
    <h2 data-n="04">Type</h2>
    <p class="tk-note">Three families, one stack each. Samples are real product lines, not lorem.</p>
    {font_html}
    <h3 class="tk-subh">size scale</h3>
    {type_html}
    <h3 class="tk-subh">weight and leading</h3>
    {wl_html}
  </section>

  <section class="tk-sec" id="motion">
    <h2 data-n="05">Motion</h2>
    <p class="tk-note">Collected from the kit as it stands. Hover a bar to see the duration. The
    Animation stage decides which of these survive as a system.</p>
    {motion_html}
  </section>

  <section class="tk-sec" id="roles">
    <h2 data-n="06">Semantic roles</h2>
    <p class="tk-note">Colour only. Each role points at a primitive through <code>var()</code> and
    carries the usage it was read from. Two roles may share a value and stay separate: that is the
    point of the level, not a mistake.</p>
    {sem_html}
  </section>

  <section class="tk-sec" id="contrast">
    <h2 data-n="07">Contrast</h2>
    <p class="tk-note">Computed from the resolved values, tinted fills composited over their surface.
    AA is 4.5:1 for body text and 3:1 for large text and interface edges. The dark theme adds its own
    column here in step 6.</p>
    {contrast_html}
  </section>

  <section class="tk-sec" id="log">
    <h2 data-n="08">What the rescale moved</h2>
    <p class="tk-note">The file was <b>read out of the painted product</b>, which was the right method for
    a colour role and the wrong one for a scale: every literal anyone had typed became a token. 348 of
    them. This is what became of the families, and the whole map is data in
    <code>ui-kit/_rescale.py</code>, so any one of these can be traced to the declarations it moved.</p>
    <table class="tk-tbl"><thead><tr><th>family</th><th>was</th><th>now</th><th>the rule it now follows</th></tr></thead><tbody>
      <tr><td class="tk-hex">space</td><td class="tk-hex">25</td><td class="tk-hex">11</td><td>the grid is 4px, 2 is the only half step; nothing moved more than 2px, and a tie broke toward the heavier neighbour, so nothing inflated</td></tr>
      <tr><td class="tk-hex">radius</td><td class="tk-hex">12</td><td class="tk-hex">5</td><td>one corner per job. 1000px and 100px rendered the same pill; 50% had no consumer</td></tr>
      <tr><td class="tk-hex">control and icon</td><td class="tk-hex">10</td><td class="tk-hex">9</td><td>value named like the rest of the geometry, each with its job. No odd sizes: 15 and 17 are gone, and so is the nameless 38</td></tr>
      <tr><td class="tk-hex">text</td><td class="tk-hex">21</td><td class="tk-hex">10</td><td>the half pixels were rem arithmetic and rounded UP, so no line got smaller. Three sizes existed only inside a clamp</td></tr>
      <tr><td class="tk-hex">display</td><td class="tk-hex">5 declared, 0 used</td><td class="tk-hex">7 used</td><td>nine clamp() were written straight into the components; now every fluid heading reads a token</td></tr>
      <tr><td class="tk-hex">leading</td><td class="tk-hex">8</td><td class="tk-hex">6</td><td>1.04 and 1.05 are the same line, and 1.45 / 1.5 / 1.55 were three body measures. 22 literal line heights joined the scale</td></tr>
      <tr><td class="tk-hex">graphite</td><td class="tk-hex">24</td><td class="tk-hex">15</td><td>a step merged only if it was under deltaE 1.5 AND the two never meet, so a chip does not fold into the surface it sits on</td></tr>
      <tr><td class="tk-hex">alphas</td><td class="tk-hex">54</td><td class="tk-hex">28</td><td>one ladder per family. A step of .05 on a hairline, a tint or a shadow is below what a screen shows</td></tr>
    </tbody></table>
    <h3 class="tk-subh">the one change a person can see</h3>
    <p class="tk-note"><code>#e88a84</code> folded into <code>#e79087</code>: two quiet reds for one job,
    the NO figure and the NO button. At deltaE 3.44 it is the only colour move above the threshold of an
    eye, and the file had already marked the pair for this step. Everything else measured under 1.5.</p>
    <h3 class="tk-subh">not merged, on purpose</h3>
    <p class="tk-note"><code>--green-200</code> stays its own value. It draws the YES line over the hero
    photograph, where the quieter green loses against the image. Two values, two jobs, not drift.<br>
    <code>--display-hero</code> stays apart from <code>--display-question</code>. Folding them grew the
    featured card title from 19.2px to 24px at 1280, which is a redesign and not a rounding.<br>
    <code>--graphite-920</code> stays out of <code>--graphite-930</code> at deltaE 1.23: it ends the card
    gradient, and merging it would give a card the same gradient as the plate it sits on.</p>
    <h3 class="tk-subh">open until step 7</h3>
    <p class="tk-note"><code>--brass-800</code> (bronze) is the one token nothing reads. DESIGN.md names it
    as part of the brand metal, so it is documented rather than dead, and gate 11 carries it as its single
    exception. It either finds a place or it goes.<br>
    Three bevel roles (<code>--bevel-md</code>, <code>--bevel-lit</code>, <code>--bevel-hi</code>) now share
    one value. They were one role per ink depth, and the depths merged; whether the roles follow is a
    question for the deletion pass.<br>
    <code>.ic-sm</code> is still drawn at a literal 13px, below the icon ramp. It is a mark sized to a line
    of text rather than to a control, which is an argument, not yet a decision.<br>
    The focus ring is real (30-plus selectors read the brass text role for it) but it does not get its own
    role here. Focus and the component states belong to the Design System stage, in both themes at once.</p>
  </section>
</div>

<script>
(function(){{
  var sb=document.getElementById('rmSidebar'),ov=document.getElementById('rmOverlay'),tg=document.getElementById('rmToggle');
  if(sb&&ov&&tg){{
    var o=function(){{sb.classList.add('open');ov.classList.add('open');}},
        c=function(){{sb.classList.remove('open');ov.classList.remove('open');}};
    tg.addEventListener('click',o);ov.addEventListener('click',c);
    sb.querySelectorAll('.sidebar-sub-link').forEach(function(a){{a.addEventListener('click',c);}});
  }}
}})();
</script>
<script src="_nav.js"></script>
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}  ({n_prim} primitives, {n_sem} roles, "
      f"{len(PRIM)} primitive groups, {len(SEM)} role groups)")
