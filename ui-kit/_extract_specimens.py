#!/usr/bin/env python3
"""Cut the labelled blocks of the frozen kit into one standalone specimen page each.

Why this exists
---------------
A component only looks like itself inside the markup it ships in. The painted
product wraps every screen in `<div class="device"><div class="app-case">`, and
423 rules across components/ are scoped under `.app-case`, so a fragment lifted
out of that wrapper renders as raw browser default. ui-kit/kit.html already
stages every component in its real context, under a human label, with dialogs
open and states set. So the block IS the specimen: nothing is cut out of its
ancestors, and nothing has to be guessed back.

Sources
-------
  ui-kit/kit.html               read only, never written
  ui-kit/specimens.extra.html   hand-authored blocks for what kit.html does not stage
  ui-kit/specimens.map.json     the curation: which block becomes which specimen

Output
------
  ui-kit/specimens/<id>.html    one standalone document per specimen
  ui-kit/specimens/index.json   the manifest the page generator reads

Each specimen page links the same components/index.css the product links, plus
ui-kit/_specimen.css (staging only: it stops sticky chrome sticking to the frame
and lets an open dialog sit in the flow). It inlines only the sprite symbols it
actually uses, and posts its height to the parent so the iframe can size itself.

    python3 ui-kit/_extract_specimens.py

Idempotent. Touches nothing outside ui-kit/specimens/. No em dash.
"""
import json
import pathlib
import re
import shutil
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
# A specimen is a page of its own, so it does not inherit the theme from the
# vitrine around it. It carries the same boot block and is told by postMessage.
import sys; sys.path.insert(0, str(ROOT / "ui-visual"))
from _theme_switch import BOOT as THEME_BOOT  # noqa: E402
OUT = KIT / "specimens"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


# ---------------------------------------------------------------- parsing ---
class Spans(HTMLParser):
    """Records where every element starts and ends, so markup can be sliced
    out of the source text byte for byte instead of being re-serialized."""

    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.line_start = [0]
        for line in text.splitlines(keepends=True):
            self.line_start.append(self.line_start[-1] + len(line))
        self.nodes = []
        self.stack = []
        self.feed(text)
        self.close()

    def _off(self):
        line, col = self.getpos()
        return self.line_start[line - 1] + col

    def _open(self, tag, attrs, self_closing):
        start = self._off()
        raw = self.get_starttag_text() or ""
        self.nodes.append(dict(tag=tag, attrs=dict(attrs), start=start,
                               tag_end=start + len(raw), end=start + len(raw),
                               parent=self.stack[-1] if self.stack else None))
        if not self_closing and tag not in VOID:
            self.stack.append(len(self.nodes) - 1)

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs, False)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, attrs, True)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.nodes[self.stack[i]]["tag"] == tag:
                closed = self.stack[i]
                del self.stack[i:]
                self.nodes[closed]["end"] = self._off() + len(tag) + 3
                return


def classes(node):
    return set((node["attrs"].get("class") or "").split())


def inner_text(text, node):
    out = []
    for part in text[node["start"]:node["end"]].replace("\n", " ").split("<"):
        if ">" in part:
            out.append(part.split(">", 1)[1])
    return " ".join("".join(out).split())


def parse_blocks(text):
    """One dict per labelled block of a kit page: section, label, html."""
    doc = Spans(text)
    nodes = doc.nodes
    kids = {}
    for i, n in enumerate(nodes):
        kids.setdefault(n["parent"], []).append(i)
    blocks = []

    def flush(section, label, spans):
        if spans:
            blocks.append(dict(section=section, label=label or section,
                               html="\n".join(text[a:b] for a, b in spans)))

    for si, sec in enumerate(nodes):
        if "kit-sec" not in classes(sec):
            continue
        section = sec["attrs"].get("id") or "?"
        label, spans = None, []
        for ci in kids.get(si, []):
            child = nodes[ci]
            cls = classes(child)
            if child["tag"] in ("h2", "h3") and not spans and label is None:
                label = inner_text(text, child)
                continue
            if "kit-note" in cls:
                continue
            if "kit-subh" in cls:
                flush(section, label, spans)
                label, spans = inner_text(text, child), []
                continue
            spans.append((child["start"], child["end"]))
        flush(section, label, spans)
    return blocks


def sprite_symbols(text):
    doc = Spans(text)
    return {n["attrs"]["id"]: text[n["start"]:n["end"]]
            for n in doc.nodes if n["tag"] == "symbol" and n["attrs"].get("id")}


def _match(nodes, selector, nth):
    want_tag, _, want_cls = selector.strip().partition(".")
    hits = [i for i, n in enumerate(nodes)
            if (not want_tag or n["tag"] == want_tag)
            and (not want_cls or want_cls in classes(n))]
    if len(hits) < nth:
        raise SystemExit("pick %r #%d found %d matches" % (selector, nth, len(hits)))
    return hits[nth - 1]


def pick(html, selector, nth=1, unwrap=()):
    """Return the picked element(s) together with their true ancestor chain,
    siblings dropped. The chain is the one the element actually has in the kit,
    so every descendant selector that painted it there still paints it here.

    `selector` may name several comma-separated siblings, which are emitted in
    document order inside one shared chain. `unwrap` drops named wrappers from
    that chain: the only use is a tab panel, which is display:none until its
    radio is checked, and the radio is not part of the component being shown."""
    doc = Spans(html)
    nodes = doc.nodes
    picked = [_match(nodes, s, nth) for s in selector.split(",")]
    parents = {nodes[i]["parent"] for i in picked}
    if len(parents) > 1:
        raise SystemExit("pick %r spans several parents" % selector)
    picked.sort(key=lambda i: nodes[i]["start"])

    chain, cur = [], nodes[picked[0]]["parent"]
    while cur is not None:
        if not (classes(nodes[cur]) & set(unwrap)):
            chain.append(cur)
        cur = nodes[cur]["parent"]
    chain.reverse()
    opens = "".join(html[nodes[i]["start"]:nodes[i]["tag_end"]] for i in chain)
    closes = "".join("</%s>" % nodes[i]["tag"] for i in reversed(chain))
    body = "\n".join(html[nodes[i]["start"]:nodes[i]["end"]] for i in picked)
    return opens + body + closes


# -------------------------------------------------------------------- urls ---
UV_PAGES = {p.name for p in (ROOT / "ui-visual").glob("*.html")}
ASSET_ATTR = re.compile(r'\b(src|href|srcset|poster|data)="([^"]+)"')


def set_attrs(html, rules):
    """Put an attribute on an element the way the product puts it there: the
    open attribute a summary or showModal sets, the checked a tab radio carries.
    Nothing else is edited, and every use is captioned on the page."""
    for rule in rules:
        doc = Spans(html)
        i = _match(doc.nodes, rule["pick"], rule.get("nth", 1))
        node = doc.nodes[i]
        tag = html[node["start"]:node["tag_end"]]
        add = "".join(' %s="%s"' % (k, v) for k, v in rule["attrs"].items())
        html = html[:node["start"]] + tag[:tag.index(" ")] + add + tag[tag.index(" "):] + \
            html[node["tag_end"]:]
    return html


def relocate(html):
    """A specimen page sits one directory deeper than the kit it was cut from,
    so every relative path needs one more step up. Product links written as a
    bare page name are pointed at the painted screen they mean, which makes the
    specimen clickable instead of dead. Returns (html, number of rewrites)."""
    n = [0]

    def one(value):
        if value.startswith("../"):
            n[0] += 1
            return "../" + value
        if value in UV_PAGES:
            n[0] += 1
            return "../../ui-visual/" + value
        return value

    def attr(m):
        return '%s="%s"' % (m.group(1), one(m.group(2)))

    html = ASSET_ATTR.sub(attr, html)
    html, k = re.subn(r"url\((\.\./)", lambda m: "url(../../", html)
    n[0] += k
    return html, n[0]


# ----------------------------------------------------------------- output ---
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{theme_boot}
<link rel="stylesheet" href="../../components/index.css">
<link rel="stylesheet" href="../_specimen.css">
</head>
<body{cls}>
"""

TAIL = """{sprite}<script>
/* Report to the vitrine: how tall this specimen is, and whether it rendered.
   postMessage crosses origins, so this works from file:// as well as from a
   server, where reading the frame document from the parent would not. */
(function () {{
  var errors = [];
  window.addEventListener("error", function (e) {{ errors.push(String(e.message)); }});

  function shown(el) {{
    if (el.checkVisibility) return el.checkVisibility({{opacityProperty: true, visibilityProperty: true}});
    var s = getComputedStyle(el);
    return s.display !== "none" && s.visibility !== "hidden" && s.opacity !== "0";
  }}

  function height() {{
    /* An open dialog and the mobile bet sheet are out of flow, so scrollHeight
       alone reports next to nothing for them. Sweep the boxes as well, but only
       the ones a person can see: a closed dropdown still has a box. */
    var h = document.body.scrollHeight, y = window.scrollY || 0, all = document.body.getElementsByTagName("*");
    for (var i = 0; i < all.length; i++) {{
      var r = all[i].getBoundingClientRect();
      if (r.height && r.bottom + y > h && shown(all[i])) h = Math.ceil(r.bottom + y);
    }}
    return h;
  }}

  /* A link with no rule behind it falls back to the browser blue, which is the
     one colour the Vault has no place for. Counted, so it can never come back
     unnoticed. Only links that render text of their own count: the product wraps
     a button in a bare <a> in several places, and that anchor paints nothing. */
  var UA_LINK = {{"rgb(0, 0, 238)": 1, "rgb(85, 26, 139)": 1, "rgb(0, 0, 255)": 1}};

  function paintsText(el) {{
    for (var i = 0; i < el.childNodes.length; i++) {{
      var n = el.childNodes[i];
      if (n.nodeType === 3 && n.textContent.trim()) return true;
    }}
    return false;
  }}

  function send() {{
    var doc = document.documentElement;
    var dead = 0, uses = document.querySelectorAll("use");
    for (var i = 0; i < uses.length; i++) {{
      var ref = uses[i].getAttribute("href") || "";
      if (ref.charAt(0) === "#" && !document.getElementById(ref.slice(1))) dead++;
    }}
    var ua = 0, links = document.querySelectorAll("a");
    for (var j = 0; j < links.length; j++) {{
      if (UA_LINK[getComputedStyle(links[j]).color] && paintsText(links[j])) ua++;
    }}
    try {{
      parent.postMessage({{
        specimen: "{id}",
        height: height(),
        elements: document.body.getElementsByTagName("*").length,
        overflowX: doc.scrollWidth - doc.clientWidth,
        deadIcons: dead,
        uaLinks: ua,
        errors: errors
      }}, "*");
    }} catch (e) {{}}
  }}

  /* The vitrine may finish loading after this frame does, so it also asks. */
  window.addEventListener("message", function (e) {{ if (e.data && e.data.ping) send(); }});
  window.addEventListener("load", send);
  window.addEventListener("resize", send);
  if (window.ResizeObserver) new ResizeObserver(send).observe(document.documentElement);
  if (document.fonts) document.fonts.ready.then(send);
  setTimeout(send, 80);
}})();
</script>
</body>
</html>
"""


SELFTEST = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Predict Market - specimen self test</title>
{THEME_BOOT}
<link rel="stylesheet" href="../components/index.css">
<link rel="stylesheet" href="_page.css">
</head>
<body data-kit-page="selftest">
<div class="tk-wrap">
  <header class="tk-hero">
    <h1>Specimen self test</h1>
    <p>Every specimen is loaded in a frame at its declared width and asked how it went. A specimen
    passes when it rendered something, kept its icons, stayed inside its width and threw nothing.
    Open this page after any change to the kit or to a component file.</p>
    <div class="tk-badges"><span class="tk-badge" id="stVerdict">running</span>
      <span class="tk-badge">{n} specimens</span></div>
  </header>
  <section class="tk-sec">
    <h2 data-n="01">Result</h2>
    <table class="tk-tbl"><thead><tr><th>specimen</th><th>width</th><th>height</th>
      <th>elements</th><th>overflow</th><th>dead icons</th><th>ua links</th><th>errors</th>
      <th></th></tr></thead>
      <tbody id="stRows"></tbody></table>
  </section>
</div>
<div id="stFrames" style="position:absolute;left:-99999px;top:0" aria-hidden="true"></div>
<script>
var SPECS = {specs};
var seen = {{}};
var host = document.getElementById("stFrames");
SPECS.forEach(function (s) {{
  var f = document.createElement("iframe");
  f.src = "specimens/" + s.id + ".html";
  f.width = s.width; f.height = 600; f.style.border = "0";
  host.appendChild(f);
}});
window.addEventListener("message", function (e) {{
  var d = e.data;
  if (!d || !d.specimen || seen[d.specimen]) return;
  seen[d.specimen] = d;
  render();
}});
function render() {{
  var rows = [], bad = 0;
  SPECS.forEach(function (s) {{
    var d = seen[s.id];
    if (!d) {{ rows.push("<tr><td class='tk-role'>" + s.id + "</td><td colspan='8'>waiting</td></tr>"); return; }}
    var fail = [];
    if (d.height <= 8) fail.push("empty");
    if (!d.elements) fail.push("no elements");
    if (d.overflowX > 1) fail.push("overflow");
    if (d.deadIcons) fail.push("dead icons");
    if (d.uaLinks) fail.push("unstyled link");
    if (d.errors.length) fail.push("error");
    if (fail.length) bad++;
    rows.push("<tr><td class='tk-role'>" + s.id + "</td><td class='tk-hex'>" + s.width +
      "</td><td class='tk-hex'>" + d.height + "</td><td class='tk-hex'>" + d.elements +
      "</td><td class='tk-hex'>" + d.overflowX + "</td><td class='tk-hex'>" + d.deadIcons +
      "</td><td class='tk-hex'>" + d.uaLinks + "</td><td class='tk-hex'>" + d.errors.length +
      "</td><td class='tk-hex'>" + (fail.length ? fail.join(", ") : "pass") + "</td></tr>");
  }});
  document.getElementById("stRows").innerHTML = rows.join("");
  var done = Object.keys(seen).length;
  document.getElementById("stVerdict").textContent =
    done < SPECS.length ? (done + " of " + SPECS.length) : (bad ? bad + " failing" : "all pass");
}}
render();
</script>
</body>
</html>
"""


def write_selftest(manifest):
    specs = [{"id": m["id"], "width": m.get("width", 900)} for m in manifest]
    (KIT / "selftest.html").write_text(
        # the boot goes in LAST, after the brace unescape: it is javascript and
        # carries a "}}" of its own, which the unescape would eat.
        SELFTEST.replace("{n}", str(len(specs))).replace("{specs}", json.dumps(specs))
        .replace("{{", "{").replace("}}", "}").replace("{THEME_BOOT}", THEME_BOOT),
        encoding="utf-8")


def build():
    kit_src = (KIT / "kit.html").read_text(encoding="utf-8")
    extra_path = KIT / "specimens.extra.html"
    extra_src = extra_path.read_text(encoding="utf-8") if extra_path.exists() else ""

    symbols = sprite_symbols(kit_src)
    blocks = {}
    for source, text in (("kit.html", kit_src), ("specimens.extra.html", extra_src)):
        if not text:
            continue
        for b in parse_blocks(text):
            blocks[(source, b["section"], b["label"])] = b["html"]

    spec_map = json.loads((KIT / "specimens.map.json").read_text(encoding="utf-8"))
    used_labels = set()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    manifest = []
    for entry in spec_map["specimens"]:
        key = (entry.get("from", "kit.html"), entry["section"], entry["label"])
        if key not in blocks:
            raise SystemExit("no block %s in %s" % (key[1:], key[0]))
        used_labels.add(key)
        html = blocks[key]
        if entry.get("pick"):
            html = pick(html, entry["pick"], entry.get("nth", 1), entry.get("unwrap", ()))
        if entry.get("set"):
            html = set_attrs(html, entry["set"])
        if entry.get("wrap") is not False:
            # .device is the product's outer stone. A layout belongs on it. A single
            # control does not: on a screen a button stands on a plate or a card, so
            # framing it on the raw stone invents a surface and draws a box around
            # something that has none. Those specimens get .app-case alone, which is
            # transparent, and stand on the page.
            open_ = '<div class="app-case">' if entry.get("canvas") is False \
                else '<div class="device"><div class="app-case">'
            close = "</div>" if entry.get("canvas") is False else "</div></div>"
            html = "%s\n%s\n%s" % (open_, html, close)
        html, rewrites = relocate(html)
        used = {m for m in re.findall(r'href="#(i-[\w-]+)"', html)}
        missing = sorted(used - set(symbols))
        if missing:
            raise SystemExit("%s uses undefined symbols: %s" % (entry["id"], missing))
        sprite = ""
        if used:
            sprite = ('<svg width="0" height="0" aria-hidden="true" style="position:absolute">'
                      "<defs>" + "".join(symbols[u] for u in sorted(used)) + "</defs></svg>\n")
        (OUT / (entry["id"] + ".html")).write_text(
            HEAD.format(title=entry["title"], theme_boot=THEME_BOOT,
                        cls=' class="spec-inflow"' if entry.get("inflow") else "") + html + "\n" +
            TAIL.format(sprite=sprite, id=entry["id"]),
            encoding="utf-8")
        manifest.append({k: entry[k] for k in
                         ("id", "component", "title", "width") if k in entry}
                        | {k: entry[k] for k in ("also", "note", "state", "height")
                           if k in entry}
                        | {"source": "%s / %s / %s" % key, "rewrites": rewrites})

    skipped = {tuple(s["block"]) for s in spec_map.get("skip_blocks", [])}
    unmapped = sorted(k for k in blocks
                      if k not in used_labels
                      and k[1] not in spec_map.get("skip_sections", [])
                      and (k[1], k[2]) not in skipped)
    if unmapped:
        raise SystemExit("blocks with no map entry:\n  " +
                         "\n  ".join("%s / %s / %s" % k for k in unmapped))

    (OUT / "index.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    write_selftest(manifest)
    print("wrote %d specimen pages into ui-kit/specimens/" % len(manifest))
    by_comp = {}
    for m in manifest:
        by_comp.setdefault(m["component"], []).append(m["id"])
    print("components covered: %d" % len(by_comp))
    return manifest


if __name__ == "__main__":
    build()
