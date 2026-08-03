#!/usr/bin/env python3
"""
_authored.py  -  the half of a stand page a generator cannot compute.

WHY IT EXISTS. Every stand page in this vitrine was written by a generator, and
a generator returns what it can READ: how many rules the file has, which roles
it reads, which classes it styles, how many screens carry each. Those are facts
and they are worth having. But the three things a person actually needs from a
component page cannot be read out of css at all:

    ANATOMY       which part is which, in the product's own words
    WHEN TO USE   the judgement that decides between this and its neighbour
    RULE and      what to do, and the mistake that is worth naming, with the
    ANTI-RULE     component that should have been used instead

So they were not on the page. Not because anyone decided against them: because
the only author was a program, and a program had nothing to say. This file is
the other author. One markdown per component, six sections, and the generator
joins them: **the facts stay computed and the judgement stays written**, and
neither can quietly replace the other.

THE SECTIONS, and what each is checked for.

    ## Purpose      one paragraph. What the component IS.
    ## Anatomy      one line per part, each naming a class this file styles.
    ## When to use  the judgement. Free prose.
    ## Rule         one sentence a person can follow.
    ## Anti-rule    one sentence, and it MUST name another component. A
                    prohibition with no alternative is a complaint; the whole
                    value of this line is the address it sends you to.
    ## States       one caption per photographed group, keyed by what the group
                    IS (see _states.keyed). Every group needs one and a caption
                    for a group that does not exist is a caption nobody reads.

WHAT IT IS NOT. It is not the Constraints block. That is Rules of use, quoted
into the page by gate 26, and it answers a different question: how many of this
component a SCREEN may carry and where it may not stand. The anti-rule is about
this component against its neighbours. The two are checked for overlap, because
the day they say the same thing one of them stops being read.

    python3 ui-kit/_authored.py            every authored file, validated
    python3 ui-kit/_authored.py button     one

No em dash.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "ui-kit"
COMP = ROOT / "components"
SRC = KIT / "authored"

SECTIONS = ["Purpose", "Anatomy", "When to use", "Rule", "Anti-rule", "States"]


def parse(path):
    """The six sections, by name. Nothing clever: a heading opens a section and
    the next heading closes it, so a file that is missing one is missing it
    visibly rather than silently inheriting the one above."""
    text = path.read_text(encoding="utf-8")
    out, name, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if name:
                out[name] = "\n".join(buf).strip()
            name, buf = m.group(1), []
        elif name is not None:
            buf.append(line)
    if name:
        out[name] = "\n".join(buf).strip()
    return out


def styled(component):
    """Every class the component's own file styles, read from its rules."""
    path = COMP / (component + ".css")
    if not path.exists():
        path = COMP / "patterns" / (component + ".css")
    if not path.exists():
        return set()
    body = re.sub(r"/\*.*?\*/", " ", path.read_text(encoding="utf-8"), flags=re.S)
    body = re.sub(r"url\([^)]*\)", "", body)
    return set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", body))


def state_captions(section):
    """The `key` - caption pairs of the States section."""
    out = {}
    for line in section.splitlines():
        m = re.match(r"^-\s+`([^`]+)`\s*[-–]\s*(.+?)\s*$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def anatomy_parts(section):
    out = []
    for line in section.splitlines():
        m = re.match(r"^-\s+`\.([\w-]+)`\s*[-–]\s*(.+?)\s*$", line)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def overlap(a, b):
    """How much of the shorter sentence is the longer one, word for word. A
    cheap measure and the right one: the failure this guards against is a person
    pasting the constraint into the anti-rule, not a paraphrase."""
    wa = {w for w in re.findall(r"[a-z]{4,}", a.lower())}
    wb = {w for w in re.findall(r"[a-z]{4,}", b.lower())}
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / min(len(wa), len(wb))


def check(component, groups=None, rules_text="", registry=None):
    """Every problem with one authored file, as a list of sentences."""
    bad = []
    path = SRC / (component + ".md")
    if not path.exists():
        return ["no authored source: write ui-kit/authored/%s.md" % component]
    doc = parse(path)
    for name in SECTIONS:
        if not doc.get(name):
            bad.append("section '%s' is missing or empty" % name)
    if bad:
        return bad

    mine = styled(component)
    # every class the author names in Anatomy has to be one this file styles
    parts = anatomy_parts(doc["Anatomy"])
    if not parts:
        bad.append("Anatomy names no class: one line per part, `- `.class` - what it is`")
    for cls, _ in parts:
        if cls not in mine:
            bad.append("Anatomy names .%s, which components/%s.css does not style"
                       % (cls, component))

    # THE ANTI-RULE HAS TO SEND YOU SOMEWHERE. A prohibition with no address is
    # a complaint, and the reader is left where they started.
    others = (registry or set()) - {component}
    named = [o for o in others if re.search(r"\b%s\b" % re.escape(o), doc["Anti-rule"])]
    if not named:
        bad.append("Anti-rule names no other component: say what to use instead")
    if rules_text and overlap(doc["Anti-rule"], rules_text) > 0.6:
        bad.append("Anti-rule repeats the Constraints block; they answer different questions")

    if groups is not None:
        caps = state_captions(doc["States"])
        keys = {g["key"] for g in groups}
        for k in sorted(keys - set(caps)):
            bad.append("no caption for the state group `%s`" % k)
        for k in sorted(set(caps) - keys):
            bad.append("caption for `%s`, which no capture produced" % k)
    return bad


def registry_names():
    return {p.stem for p in COMP.glob("*.css") if p.stem not in ("index", "tokens", "fonts")} \
        | {p.stem for p in (COMP / "patterns").glob("*.css")}


if __name__ == "__main__":
    sys.path.insert(0, str(KIT))
    import _states
    from _gen_docs import usage_rules

    groups = _states.by_component()
    rules = usage_rules()
    names = registry_names()
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    have = sorted(p.stem for p in SRC.glob("*.md")) if SRC.exists() else []
    todo = want or have
    fails = 0
    for c in todo:
        text = " ".join(r["title"] + " " + r["check"] for r in rules if c in r["components"])
        bad = check(c, groups.get(c), text, names)
        print("%-16s %s" % (c, "ok" if not bad else "FAIL"))
        for b in bad:
            print("   " + b)
        fails += bool(bad)
    missing = sorted(names - set(have))
    print("\n%d authored, %d without a source" % (len(have), len(missing)))
    if missing:
        print("   " + ", ".join(missing))
    sys.exit(1 if fails else 0)
