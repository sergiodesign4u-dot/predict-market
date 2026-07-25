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

size_html = ['<div class="tk-sizes">']
for t in sizes["tokens"]:
    v = resolve(t["value"])
    if "icon" in t["name"]:
        size_html.append(f'<div class="tk-size"><i style="width:var({t["name"]});height:var({t["name"]});'
                         f'border-radius:4px"></i><span>{esc(t["name"])}<br>{esc(v)}</span></div>')
    else:
        size_html.append(f'<div class="tk-size"><i style="height:var({t["name"]})"></i>'
                         f'<span>{esc(t["name"])}<br>{esc(v)}</span></div>')
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

SIDEBAR = """<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open roadmap"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar">
  <a href="../research/research.html" class="sidebar-back"><span class="bk-arrow" aria-hidden="true">&larr;</span> Course roadmap</a>
  <div class="sidebar-brand"><div class="sidebar-project-name">UI Kit - components</div></div>
  <nav class="sidebar-nav">
    <a href="../ui-visual/event-feed.html" class="sidebar-page-link">UI + Visual - screens</a>
    <a class="sidebar-page-link active">Tokens</a>
    <div class="sidebar-sub">
      <a href="#colour" class="sidebar-sub-link">Colour primitives</a>
      <a href="#material" class="sidebar-sub-link">Material</a>
      <a href="#geometry" class="sidebar-sub-link">Geometry</a>
      <a href="#type" class="sidebar-sub-link">Type</a>
      <a href="#motion" class="sidebar-sub-link">Motion</a>
      <a href="#roles" class="sidebar-sub-link">Semantic roles</a>
      <a href="#contrast" class="sidebar-sub-link">Contrast</a>
      <a href="#log" class="sidebar-sub-link">Merges and open items</a>
    </div>
    <a href="kit.html" class="sidebar-page-link">UI Kit</a>
    <a href="shell.html" class="sidebar-page-link">Shell</a>
  </nav>
</aside>"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Tokens</title>
<link rel="stylesheet" href="kit.css">
<link rel="stylesheet" href="../components/tokens.css">
<link rel="stylesheet" href="_page.css">
</head>
<body>
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
    <p class="tk-note">Every value here already stood in <code>ui-kit/kit.css</code>. Nothing was
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
    {scale_rows(space["tokens"])}
    <h3 class="tk-subh">radius</h3>
    {radius_html}
    <h3 class="tk-subh">control and icon sizes</h3>
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
    <h2 data-n="08">Merges and open items</h2>
    <h3 class="tk-subh">drift merged into one value</h3>
    <table class="tk-tbl"><thead><tr><th>was</th><th>now</th><th>why it is safe</th></tr></thead><tbody>
      <tr><td class="tk-hex">#14161a</td><td class="tk-hex">#141619</td><td>one step in the blue channel, the same canvas stone</td></tr>
      <tr><td class="tk-hex">#20242b</td><td class="tk-hex">#20242a</td><td>one step in the blue channel, the same hover fill</td></tr>
      <tr><td class="tk-hex">#e88a84</td><td class="tk-hex">#e79087</td><td>two quiet reds for one job: the NO figure and the NO button</td></tr>
      <tr><td class="tk-hex">border-radius 1000px</td><td class="tk-hex">100px</td><td>every control it is used on is under 60px tall, so both render the same pill</td></tr>
      <tr><td class="tk-hex">--brass, --lime</td><td class="tk-hex">--brass-500, --brass-300</td><td>exact duplicates of the accent pair, left over from an earlier direction</td></tr>
    </tbody></table>
    <h3 class="tk-subh">not merged, on purpose</h3>
    <p class="tk-note"><code>--green-200</code> stays its own value. It draws the YES line over the hero
    photograph, where the quieter green loses against the image. Two values, two jobs, not drift.</p>
    <h3 class="tk-subh">open until step 7</h3>
    <p class="tk-note"><code>--brass-800</code> (bronze) and <code>--graphite-820</code> (the old
    <code>--slab</code>) have no consumer: documented in DESIGN.md, never wired. They either find a place
    or they go.<br>
    <code>--bg-card-quiet</code> is the one intentional pixel change of this stage. Five surfaces
    (<code>.pos</code>, <code>.cta-bar</code>, <code>.toast</code>, <code>.cc-banner</code>,
    <code>.wd-flow</code>) read <code>var(--card)</code>, which is declared nowhere, so they render
    transparent today. The value restored is <code>--card3d</code>, the token the previous stage declared
    for exactly this and never wired.<br>
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
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}  ({n_prim} primitives, {n_sem} roles, "
      f"{len(PRIM)} primitive groups, {len(SEM)} role groups)")
