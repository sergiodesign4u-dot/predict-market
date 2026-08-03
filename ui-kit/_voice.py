#!/usr/bin/env python3
"""
_voice.py  -  a trader term in a place a person meets while ACTING.

THE RULE IT ENFORCES, and it is a rule and not a word list. `voice/docs/voice.md`
bans a set of trader terms from the UI, and for one whole stage that ban was a
LIST OF WORDS. A list of words cannot answer the question the product actually
asks, because the same word is right in one place and wrong in another: `AMM` on
the How It Works page is the mechanism being named, and `(AMM)` trailing the fine
print under Confirm is a word met while deciding. Five placements shipped in both
trees under a rule that had already banned all five, because the rule was written
as instances instead of as an invariant.

The invariant, from `voice/docs/voice.md`:

    the ban is about PLACE, not about the word. A trader term is forbidden
    wherever a person meets it while ACTING - a control label, a heading, a
    figure read to decide - and allowed inside a block whose whole job is to
    explain the mechanism, glossed in plain words. And the head of an exempt
    block is NOT inside the exemption, because a summary, a tab and a title are
    read by everyone who never opens them.

So this file is two lists crossed: the TERMS, and the PLACES where a person acts.
Neither is a judgement at check time. A term found in an acting place fails
unless it is in EXEMPT, which names the file, the place, the term and the reason.

WHY THE PLACES ARE MARKUP AND NOT PROSE. A checker asks the markup, not the text
(`CLAUDE.md`): the same sentence is copy in one element and an explanation in
another, and only the element can tell them apart. Prose inside `<p>`, inside an
explanation panel, inside a document page is not read at all, which is the whole
point - the ban was never on the word.

THE CONTROL EVERY DECLARED LIST IN THIS REPO CARRIES. An EXEMPT row that matches
nothing fails as loudly as an unexempted hit. A list that can go quiet by being
stale is a list that stops being read.

    python3 ui-kit/_voice.py           report
    python3 ui-kit/_voice.py --places  print every acting place it can see

No em dash.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREES = ["wireframes", "ui-visual"]

# ---- the terms -------------------------------------------------------------
# Straight out of the "Not allowed in the UI (trader jargon)" list in
# voice/docs/voice.md. Written as whole words so `positions` in a class name and
# `Marketing` in prose are not the same string as `position` and `Market`.
# `liquidity` is on the list as "liquidity as a headline number", which is what
# a figure place IS, so the place list carries that qualifier rather than a
# second term entry.
TERMS = {
    "AMM": r"\bAMM\b",
    "CLOB": r"\bCLOB\b",
    "order book": r"\border book\b",
    "liquidity": r"\bliquidit(?:y|ies)\b",
    "spread": r"\bspread\b",
    "market": r"\bmarkets?\b",
    "position": r"\bpositions?\b",
    "shares": r"\bshares\b",
    "long": r"\blong\b",
    "short": r"\bshort\b",
    "buy": r"\bbuy\b",
    # `holder` is not in the lexicon's list and it should be: it is the noun form
    # of `position`, which IS banned, and it shipped on a control for a whole
    # stage because the list held the verb and not the person. Found by this
    # gate's own two-way proof, which put `Holders` back on the comment sort and
    # went green. A checker that cannot fail on the defect it was written for is
    # the clean bill of health `ui-kit/docs/defects.md` row 42 is about.
    "holder": r"\bholders?\b",
    "sell": r"\bsell\b",
}

# ---- the places a person meets a word while ACTING --------------------------
# A control label, a heading, and a figure read to decide. Each is markup: the
# element a person presses, the element that names a screen, and the element
# that carries a number they are about to bet against. The value is what the
# report calls it, so a finding reads as a sentence.
ACTING_TAGS = {
    "button": "a control label",
    "summary": "the head of a collapsed block",
    "label": "a field label",
    "h1": "a heading", "h2": "a heading", "h3": "a heading",
    "h4": "a heading", "h5": "a heading", "h6": "a heading",
}
# and the classes that are a figure or a label without being one of those tags
ACTING_CLASSES = {
    "ms-label": "a figure label", "ms-val": "a figure read to decide",
    "field-label": "a field label", "fine": "fine print read while deciding",
    "opt-name": "an outcome label", "bp-sel-name": "the chosen outcome",
    "stat-label": "a figure label", "market-title": "the head of a block",
    "rules-tab": "a tab label", "toc-link": "a contents link",
}

# ---- what is allowed, and why ----------------------------------------------
# THE EXEMPTIONS THIS FILE DOES NOT NEED, and the fact is worth more than the
# list would be. The first draft carried six rows for `md-sub` and How It Works,
# copied out of the sorted decision in `docs/backlog.md` 29, and the idle control
# failed all six on the first run. It was right: those are not acting places, so
# the scan never visits them, and an exemption for a place nobody looks at is a
# sentence that reads like protection and protects nothing. The invariant is
# enforced by WHERE THE SCAN LOOKS, not by a list of pardons, which is what
# "the ban is about place" means when it is mechanised instead of recited.
#
# (term, phrase, reason). Matched against the TEXT of an acting place, because a
# proper noun is the same proper noun wherever it stands and a place list would
# need one row per screen.
EXEMPT_PHRASES = [
    ("market", "Predict Market",
     "the product's own name. The ban is on `market` for the EVENT, which is the "
     "trader's word for the thing a person bets on; a brand is a proper noun and "
     "carries no instruction. It stands in the logo button on 192 acting places "
     "across both trees and in the maintenance heading on 2, and if the name "
     "itself is ever reconsidered that is a brand decision, not a copy one"),
    ("long", "however long",
     "ordinary English, not a bet side. The lexicon bans long / short as the "
     "trader's names for the two sides of a bet; this is the adverb, in the "
     "multi-outcome fine print, 4 places across both trees. Written as a phrase "
     "and not as a place, so that if the sentence is ever rewritten the idle "
     "control asks the question again instead of pardoning the whole block"),
]

# (term, place-substring, reason). A place exemption says a whole location is
# outside the ban. There are none, and that is the finding, not an omission.
EXEMPT_PLACES = []

TAG_RE = re.compile(
    r"<(button|summary|label|h[1-6])\b([^>]*)>(.*?)</\1>", re.S | re.I)
# START TAGS ONLY, and the body is taken by scanning forward. The first cut
# matched whole elements with `<(\w+)[^>]*class="..."[^>]*>(.*?)</\1>` and MISSED
# TWO OF THE FIVE PLACEMENTS IT WAS WRITTEN FOR, because `finditer` does not
# overlap: the enclosing `<div class="market-stats">` matched first, was skipped
# for not being an acting class, and took its own `<span class="ms-label">`
# children out of the scan with it. A checker that silently reads less than it
# says it reads is exactly the defect in `ui-kit/docs/defects.md` row 42, and it
# was caught here only because the two-way proof reverted each of the five and
# demanded a red for every one.
OPEN_RE = re.compile(r'<(\w+)\b([^>]*?)class="([^"]*)"([^>]*)>')
STRIP = re.compile(r"<[^>]+>")


def places(src):
    """Every (place-name, text) a person meets while acting, in one document."""
    out = []
    for m in TAG_RE.finditer(src):
        tag = m.group(1).lower()
        cls = re.search(r'class="([^"]*)"', m.group(2) or "")
        name = ACTING_TAGS[tag] + (" ." + cls.group(1).split()[0] if cls and cls.group(1).strip() else "")
        out.append((name, STRIP.sub(" ", m.group(3))))
    for m in OPEN_RE.finditer(src):
        tag = m.group(1).lower()
        for cls in m.group(3).split():
            if cls not in ACTING_CLASSES:
                continue
            end = src.find("</%s>" % tag, m.end())
            body = src[m.end():end] if end != -1 else src[m.end():m.end() + 400]
            out.append((ACTING_CLASSES[cls] + " ." + cls, STRIP.sub(" ", body)))
    return out


def findings():
    """(violations, exemptions that matched nothing)."""
    bad, used = [], set()
    for tree in TREES:
        for path in sorted((ROOT / tree).glob("*.html")):
            src = path.read_text(encoding="utf-8", errors="ignore")
            rel = "%s/%s" % (tree, path.name)
            for name, text in places(src):
                for term, pat in TERMS.items():
                    if not re.search(pat, text, re.I):
                        continue
                    where = "%s %s" % (rel, name)
                    # a phrase in which the word is not the word, then a place
                    # that is outside the ban entirely
                    hit = None
                    for i, (t, phrase, _why) in enumerate(EXEMPT_PHRASES):
                        if t == term and phrase.lower() in text.lower():
                            hit = ("phrase", i)
                            break
                    if hit is None:
                        for i, (t, place, _why) in enumerate(EXEMPT_PLACES):
                            if t == term and place.lower() in where.lower():
                                hit = ("place", i)
                                break
                    if hit is not None:
                        used.add(hit)
                        continue
                    bad.append("%s: %r in %s" % (where, term, text.strip()[:60]))
    idle = (["%s in the phrase %r" % (t, p)
             for i, (t, p, _w) in enumerate(EXEMPT_PHRASES) if ("phrase", i) not in used] +
            ["%s in %s" % (t, p)
             for i, (t, p, _w) in enumerate(EXEMPT_PLACES) if ("place", i) not in used])
    return sorted(set(bad)), idle


if __name__ == "__main__":
    if "--places" in sys.argv:
        src = (ROOT / "ui-visual" / "event-detail.html").read_text(encoding="utf-8")
        for name, text in places(src):
            print("%-34s %s" % (name, text.strip()[:70]))
        sys.exit(0)
    bad, idle = findings()
    print("%d acting place(s) carry a trader term, %d idle exemption(s)" % (len(bad), len(idle)))
    for b in bad[:40]:
        print("   " + b)
    if len(bad) > 40:
        print("   ... and %d more" % (len(bad) - 40))
    for i in idle:
        print("   IDLE EXEMPTION: " + i)
    sys.exit(1 if (bad or idle) else 0)
