#!/usr/bin/env python3
"""
_img_attrs.py  -  give every <img> on a painted screen the three attributes a
browser needs before it has the file: how big it is, when to fetch it, and how
to decode it.

WHY. Without width and height the browser cannot reserve the box, so every photo
that arrives shoves the text under it: that is Cumulative Layout Shift, and it is
worst on the slow connection the shift matters most on. Without loading="lazy"
the feed fetches twelve photographs before the first one is on screen. Neither
is a style, which is why neither belongs in components/: they are facts about
the file, and they live on the element.

The sizes are read off the assets with sips, not guessed. A file that is not in
the table is left alone rather than given a wrong box, since a wrong aspect ratio
is worse than none.

Above the fold is not lazy: the first hero photograph and the two trust cards on
the feed are loaded eagerly with fetchpriority="high", because lazy-loading the
thing a person is already looking at is a slower page, not a faster one.

Usage:
    python3 _img_attrs.py            # apply
    python3 _img_attrs.py --check    # report, write nothing
No em dash.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# asset -> (width, height), measured with `sips -g pixelWidth -g pixelHeight`
SIZE = {
    "avatar-1.jpg": (400, 400),
    "avatar-2.jpg": (400, 400),
    "brand-columns.webp": (1200, 900),
    "event-crypto.jpg": (1600, 1073),
    "event-culture.jpg": (1600, 1073),
    "event-general.jpg": (1600, 1073),
    "event-politics.jpg": (1600, 1073),
    "event-sports.jpg": (900, 600),
    "hero-capitol.webp": (1400, 788),
    "spare-markets-dark.jpg": (900, 600),
    "spare-newspapers.jpg": (900, 1200),
    "spare-reader.jpg": (900, 601),
    "trust-column-full.webp": (520, 600),
    "trust-column.webp": (640, 392),
    "trust-globe.webp": (640, 393),
    "trust-source.webp": (640, 449),
    "trust-column.png": (1254, 1254),
    "trust-column-full.png": (1254, 1254),
    "trust-globe.png": (1254, 1254),
    "trust-source.png": (1254, 1254),
    "trust-source-alt.png": (1254, 1254),
}

# the classes that are above the fold on the screen they appear on
EAGER = ("hf-photo", "ht-art")

IMG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ATTR = re.compile(r'\s(width|height|loading|decoding|fetchpriority)="[^"]*"', re.IGNORECASE)


def rewrite(tag):
    src = re.search(r'src="([^"]+)"', tag)
    if not src:
        return tag
    name = os.path.basename(src.group(1))
    if name not in SIZE:
        return tag
    w, h = SIZE[name]
    cls = re.search(r'class="([^"]*)"', tag)
    eager = bool(cls) and any(c in cls.group(1).split() for c in EAGER)
    clean = ATTR.sub("", tag)
    extra = ' width="%d" height="%d" decoding="async"' % (w, h)
    extra += ' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    return clean[:-1].rstrip() + extra + ">"


def process(path, check):
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    new = IMG.sub(lambda m: rewrite(m.group(0)), html)
    if new == html:
        return "unchanged"
    if not check:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
    return "updated"


def main():
    check = "--check" in sys.argv or "--dry-run" in sys.argv
    counts = {}
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".html"):
            continue
        s = process(os.path.join(HERE, fname), check)
        counts[s] = counts.get(s, 0) + 1
    for s in sorted(counts):
        print("%-10s %d" % (s, counts[s]))


if __name__ == "__main__":
    main()
