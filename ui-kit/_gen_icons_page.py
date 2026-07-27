#!/usr/bin/env python3
"""Build ui-kit/icons.html, the one foundation page that is not a token.

Colour, material, geometry, type and motion are all generated from
components/tokens.css and live on tokens.html. Icons are the exception: they are
markup, not a value, so no token file can hold them. Until now they lived only
inside kit.html, which is exactly why 43 icon references across the stand pages
pointed at symbols that were not there.

The page carries:
  - the named icons, each rendered from the sprite at its shipped sizes, with
    the id, the use snippet, and how many painted screens reference it;
  - the inlining rule, because a <use href="#id"> only resolves against a symbol
    in the same document;
  - the sizing contract, quoted from components/base.css;
  - the three icon blocks of the frozen kit, live, in their own frames.

    python3 ui-kit/_gen_icons_page.py

Idempotent. Reads only. No em dash.
"""
import glob
import html
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
# one definition of the theme switch, shared with the painted screens
import sys; sys.path.insert(0, str(ROOT / "ui-visual"))
from _theme_switch import BOOT as THEME_BOOT  # noqa: E402
UV = ROOT / "ui-visual"

kit_src = (KIT / "kit.html").read_text(encoding="utf-8")
SYMBOLS = re.findall(r'(<symbol id="([\w-]+)".*?</symbol>)', kit_src, re.S)
SPECIMENS = [s for s in json.loads((KIT / "specimens" / "index.json").read_text(encoding="utf-8"))
             if s["component"] == "icons"]

# how many painted screens use each symbol, and how many carry the sprite.
# overview.html is the index OF the screens, not a screen, so it is not counted.
SCREENS = [f for f in sorted(glob.glob(str(UV / "*.html")))
           if os.path.basename(f) != "overview.html"]
uses = {sid: 0 for _, sid in SYMBOLS}
carriers = 0
for f in SCREENS:
    src = open(f, encoding="utf-8").read()
    if "<symbol id=" in src:
        carriers += 1
    for _, sid in SYMBOLS:
        if 'href="#%s"' % sid in src:
            uses[sid] += 1

base = (ROOT / "components" / "base.css").read_text(encoding="utf-8")
SIZE_RULES = [(" ".join(m.group(1).split()), m.group(2).strip())
              for m in re.finditer(r"([^{}\n][^{}]*)\{([^{}]*)\}", base)
              if re.search(r"\.ic\b|\.ic-sm\b|svg", m.group(1))]


def esc(s):
    return html.escape(s, quote=False)


tiles = "".join(
    f'<figure class="ck-ico"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true">'
    f'<use href="#{sid}"></use></svg>'
    f"<figcaption>{esc(sid)}</figcaption><code>{uses[sid]} screens</code></figure>"
    for _, sid in SYMBOLS)

size_rows = "".join(
    f"<tr><td class='tk-role'>{esc(sel)}</td><td class='ck-decl'>{esc(decl)}</td></tr>"
    for sel, decl in SIZE_RULES[:14])

frames = "".join(
    f'<figure class="ck-scene" id="sp-{s["id"]}">'
    f'<figcaption class="ck-scene-lbl"><b>{esc(s["title"])}</b>'
    f'<span class="ck-w">{s.get("width", 1120)}px</span><span class="ck-zoom" hidden></span>'
    f'<a href="specimens/{s["id"]}.html" target="_blank" rel="noopener">open on its own</a>'
    f'</figcaption><div class="ck-frame"><iframe data-specimen="{s["id"]}" '
    f'src="specimens/{s["id"]}.html" width="{s.get("width", 1120)}" height="320" '
    f'loading="lazy" title="{esc(s["title"])}"></iframe></div></figure>'
    for s in SPECIMENS)

PAGE = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - Icons</title>
{THEME_BOOT}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="icons">
<button type="button" class="rm-toggle" id="rmToggle" aria-label="Open the system"><span></span><span></span><span></span></button>
<div class="rm-overlay" id="rmOverlay"></div>
<aside class="sidebar" id="rmSidebar" data-kit-nav></aside>

<svg width="0" height="0" aria-hidden="true" style="position:absolute"><defs>
{"".join(sym for sym, _ in SYMBOLS)}
</defs></svg>

<div class="tk-wrap">
  <header class="tk-hero">
    <h1>Icons</h1>
    <p>The one foundation that is not a token. Colour, material, geometry, type and motion are values
    and live on <a href="tokens.html">the token page</a>; an icon is markup, so it has a page of its
    own. Everything below is read out of the sprite the product ships.</p>
    <div class="tk-badges">
      <span class="tk-badge">{len(SYMBOLS)} named icons</span>
      <span class="tk-badge">{carriers} of {len(SCREENS)} screens carry the sprite</span>
      <span class="tk-badge">inline only</span>
    </div>
  </header>

  <section class="tk-sec" id="named">
    <h2 data-n="01">Named icons</h2>
    <p class="tk-note">Each one is a <code>&lt;symbol&gt;</code> in the sprite, drawn with
    <code>&lt;svg class="ic"&gt;&lt;use href="#id"&gt;</code>. The count is how many of the painted
    screens reference it.</p>
    <div class="ck-icos">{tiles}</div>
  </section>

  <section class="tk-sec" id="rule">
    <h2 data-n="02">The sprite has to be in the document</h2>
    <p class="tk-note">A <code>use</code> reference resolves against a symbol in the same document.
    An external reference (<code>href=&quot;sprite.svg#id&quot;</code>) does not load from
    <code>file://</code>, so every page that draws an icon inlines the symbols it needs, and a page
    that draws none inlines nothing. That is why each specimen page here carries its own subset, and
    why a reference with no symbol behind it is a build error rather than a blank square.</p>
  </section>

  <section class="tk-sec" id="sizing">
    <h2 data-n="03">Sizing and stroke</h2>
    <p class="tk-note">Quoted from <code>components/base.css</code>. A filled sprite icon and an
    outline glyph are drawn differently, which is what the last rule handles.</p>
    <table class="tk-tbl"><thead><tr><th>selector</th><th>declarations</th></tr></thead>
      <tbody>{size_rows}</tbody></table>
  </section>

  <section class="tk-sec" id="sets">
    <h2 data-n="04">The sets, live</h2>
    <p class="tk-note">The three icon blocks of the frozen kit, each in a frame of its own.</p>
    {frames}
  </section>
</div>

<script src="_frames.js"></script>
<script src="_nav.js"></script>
</body>
</html>
"""

(KIT / "icons.html").write_text(PAGE, encoding="utf-8")
print("built icons.html: %d symbols, %d live blocks" % (len(SYMBOLS), len(SPECIMENS)))
