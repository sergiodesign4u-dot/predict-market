#!/usr/bin/env python3
"""Extract product UI text from the wireframes for the microcopy inventory.

Scope = inside <div class="device"> and inside any <dialog>. Excludes the
wireframe tooling (.wf-* screen tree, .page-label bar, .state-switch), which all
live OUTSIDE .device. Emits, per page, a list of rows: zone, type, tag, text.
"""
import os, glob, json, html
from html.parser import HTMLParser

WF = "/Users/sergiyshevchenko/Claud Projects/Project One/wireframes"

HEADING = {"h1", "h2", "h3", "h4", "h5"}
SKIP_TEXT_IN = {"script", "style", "svg", "title"}

ZONE_BY_ID = {"signinDialog": "Sign-in dialog", "depositDialog": "Deposit dialog"}


def classes(attrs):
    d = dict(attrs)
    return set((d.get("class") or "").split()), d


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # list of (tag, classset, id)
        self.device_depth = None # stack depth where .device opened
        self.dialog_depth = None
        self.skip_depth = None   # inside script/style/svg
        self.rows = []
        self._pending = None     # (tag, classset) awaiting text for button aria fallback
        self._buf = []
        self._buf_ctx = None

    # -- scope helpers
    def in_scope(self):
        return self.device_depth is not None or self.dialog_depth is not None

    def current_zone(self):
        for tag, cls, _id in reversed(self.stack):
            if _id in ZONE_BY_ID:
                return ZONE_BY_ID[_id]
            if tag == "dialog":
                return "Dialog"
            if tag == "header" or "app-header" in cls:
                return "Header"
            if "cat-nav" in cls:
                return "Category nav"
            if "bottom-nav" in cls:
                return "Bottom nav"
            if tag == "footer":
                return "Footer"
            if "bet-panel" in cls or "bet-dock" in cls:
                return "Bet panel"
            if "ed-tabbar" in cls or "ed-tabwrap" in cls:
                return "Content tabs"
        return "Main"

    def parent_tag(self):
        return self.stack[-1][0] if self.stack else ""

    def parent_cls(self):
        return self.stack[-1][1] if self.stack else set()

    def handle_starttag(self, tag, attrs):
        cls, d = classes(attrs)
        _id = d.get("id")
        self.stack.append((tag, cls, _id))
        depth = len(self.stack)
        if tag == "div" and "device" in cls and self.device_depth is None:
            self.device_depth = depth
        if tag == "dialog" and self.dialog_depth is None:
            self.dialog_depth = depth
        if tag in SKIP_TEXT_IN and self.skip_depth is None:
            self.skip_depth = depth
        # capture placeholder as its own row
        if self.in_scope() and self.skip_depth is None:
            ph = d.get("placeholder")
            if ph and ph.strip():
                self.rows.append({"zone": self.current_zone(), "type": "Placeholder",
                                  "tag": tag, "text": ph.strip()})
            # icon-only button: remember to fall back to aria-label
            if tag == "button":
                self._pending = {"zone": self.current_zone(), "aria": (d.get("aria-label") or "").strip(),
                                 "got_text": False}

    def handle_startendtag(self, tag, attrs):
        # e.g. <input ... /> placeholder
        cls, d = classes(attrs)
        if self.in_scope() and self.skip_depth is None:
            ph = d.get("placeholder")
            if ph and ph.strip():
                self.rows.append({"zone": self.current_zone(), "type": "Placeholder",
                                  "tag": tag, "text": ph.strip()})

    def handle_endtag(self, tag):
        depth = len(self.stack)
        # flush button aria fallback
        if tag == "button" and self._pending is not None:
            if not self._pending["got_text"] and self._pending["aria"]:
                self.rows.append({"zone": self._pending["zone"], "type": "Icon button (aria-label)",
                                  "tag": "button", "text": self._pending["aria"]})
            self._pending = None
        if self.skip_depth == depth:
            self.skip_depth = None
        if self.device_depth == depth:
            self.device_depth = None
        if self.dialog_depth == depth:
            self.dialog_depth = None
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if not self.in_scope() or self.skip_depth is not None:
            return
        text = " ".join(data.split())
        if not text:
            return
        ptag = self.parent_tag()
        pcls = self.parent_cls()
        if self._pending is not None:
            self._pending["got_text"] = True
        # classify type
        if ptag in HEADING:
            typ = "Heading"
        elif ptag == "button":
            typ = "Button"
        elif ptag == "label" or "field-label" in pcls or "sub-label" in pcls:
            typ = "Field label"
        elif "ed-q" in pcls or "card-q" in pcls or "q-title" in pcls:
            typ = "Event title (user content)"
        elif ptag == "a":
            typ = "Link"
        elif ptag in ("strong", "em", "b", "span", "small", "code"):
            typ = "Inline/label"
        elif ptag in ("p", "li", "div", "td", "th", "caption", "figcaption", "blockquote"):
            typ = "Text"
        else:
            typ = ptag
        self.rows.append({"zone": self.current_zone(), "type": typ, "tag": ptag,
                          "text": text, "pcls": " ".join(sorted(pcls))[:40]})


def extract(path):
    p = Extractor()
    p.feed(open(path, encoding="utf-8").read())
    return p.rows


def main():
    out = {}
    for f in sorted(glob.glob(os.path.join(WF, "*.html"))):
        name = os.path.basename(f)
        out[name] = extract(f)
    sc = os.path.dirname(os.path.abspath(__file__))
    json.dump(out, open(os.path.join(sc, "microcopy_raw.json"), "w"), indent=1, ensure_ascii=False)
    # quick stats
    tot = sum(len(v) for v in out.values())
    print("pages:", len(out), "rows:", tot)


if __name__ == "__main__":
    main()
