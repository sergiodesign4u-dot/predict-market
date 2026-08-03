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

SECTIONS = ["Sources", "Purpose", "Anatomy", "When to use", "Rule", "Anti-rule", "States"]

# THE ONE ARTEFACT IN THIS SYSTEM NO GATE CAN READ. Everything else here is
# checked against something: a class against the css, a rule against the
# document, a picture against the bytes it was taken from. A SENTENCE cannot be
# checked for being true or for being useful, and that makes this the riskiest
# file in the repo: forty-two fluent paragraphs, each passing every check, none
# of them saying anything. The median with no source, written freely and looking
# like work.
#
# Three things stand against that and two of them are mechanical.
#
# SOURCES ARE NAMED BEFORE THE SENTENCES. Every authored file opens with what it
# was written FROM - the inventory row, the screens the component actually
# stands on, the rules of use that name it, the microcopy rows, the critique
# lines - and the check below fails when one of those does not exist. A
# component whose source list would be empty does not get a file at all: it goes
# in COMPUTED_ONLY with its reason.
#
# AN ANTI-RULE CARRIES ITS PROVENANCE. Naming another component is cheap: a
# plausible pair is invented in a second and reads exactly like a measured one.
# So the section ends with either `Seen:` and a place the confusion actually
# happened, or `Predicted:` and the admission that it has not. Both are allowed.
# Passing one off as the other is not, and a reader can now tell them apart.
SEEN = re.compile(r"^(Seen|Predicted):\s*(.+)$", re.M)

# A reference the checker can follow: a path in the repo, a rule of use, or a
# painted screen. Anything else in a source line is prose and is not checked.
REF = re.compile(r"`([\w./-]+\.(?:md|css|html|py|cjs|json))`|\b(R\d+)\b")


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


def refs(text, rule_ids):
    """(what this text points at, what it points at that does not exist)."""
    found, missing = [], []
    for path, rule in REF.findall(text):
        if path:
            found.append(path)
            if not (ROOT / path).exists():
                missing.append(path)
        elif rule:
            found.append(rule)
            if rule_ids and rule not in rule_ids:
                missing.append(rule)
    return found, missing


def check(component, groups=None, rules_text="", registry=None, rule_ids=None):
    """Every problem with one authored file, as a list of sentences."""
    bad = []
    path = SRC / (component + ".md")
    if not path.exists():
        if component in COMPUTED_ONLY:
            return []
        return ["no authored source: write ui-kit/authored/%s.md, or declare it in "
                "_authored.COMPUTED_ONLY with the reason" % component]
    if component in COMPUTED_ONLY:
        return ["declared in COMPUTED_ONLY and yet authored: delete one of the two"]
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

    # THE SOURCES ARE FOLLOWED, not just present. A source list that names a file
    # which is not there is the same defect as a picture whose bytes moved, one
    # level up: the sentence may still be true and nothing can tell.
    src_refs, src_missing = refs(doc["Sources"], rule_ids)
    if len(doc["Sources"].splitlines()) < 2:
        bad.append("Sources lists fewer than two things; if there is nothing to "
                   "write from, declare the component in COMPUTED_ONLY instead")
    if not src_refs:
        bad.append("Sources points at nothing a checker can follow: name a file, "
                   "a screen or a rule of use")
    for m in src_missing:
        bad.append("Sources names %s, which does not exist" % m)

    # THE ANTI-RULE HAS TO SEND YOU SOMEWHERE. A prohibition with no address is
    # a complaint, and the reader is left where they started.
    others = (registry or set()) - {component}
    named = [o for o in others if re.search(r"\b%s\b" % re.escape(o), doc["Anti-rule"])]
    if not named:
        bad.append("Anti-rule names no other component: say what to use instead")
    if rules_text and overlap(doc["Anti-rule"], rules_text) > 0.6:
        bad.append("Anti-rule repeats the Constraints block; they answer different questions")
    # and it has to say whether anyone has actually made the mistake
    seen = SEEN.findall(doc["Anti-rule"])
    if len(seen) != 1:
        bad.append("Anti-rule must end with exactly one 'Seen: ...' or 'Predicted: ...' line, "
                   "so a reader can tell a measured confusion from a plausible one")
    elif seen[0][0] == "Seen":
        _, gone = refs(seen[0][1], rule_ids)
        if not _:
            bad.append("'Seen:' points at nothing a checker can follow; if it has not "
                       "actually happened, say Predicted")
        for g in gone:
            bad.append("'Seen:' names %s, which does not exist" % g)

    if groups is not None:
        caps = state_captions(doc["States"])
        keys = {g["key"] for g in groups}
        for k in sorted(keys - set(caps)):
            bad.append("no caption for the state group `%s`" % k)
        for k in sorted(set(caps) - keys):
            bad.append("caption for `%s`, which no capture produced" % k)
    return bad


# The components with nothing to say beyond what the page already computes, and
# the reason for each. This is the exception list of gate 32, so it carries the
# same control every declared list in this repo carries: an entry that ALSO has
# an authored file fails, and a component with neither fails. A line here is a
# DECISION that was made and can be argued with; silence would be a decision
# nobody took.
COMPUTED_ONLY = {}


def registry_names():
    return {p.stem for p in COMP.glob("*.css") if p.stem not in ("index", "tokens", "fonts")} \
        | {p.stem for p in (COMP / "patterns").glob("*.css")}


if __name__ == "__main__":
    sys.path.insert(0, str(KIT))
    import _states
    from _gen_docs import usage_rules

    groups = _states.by_component()
    rules = usage_rules()
    rule_ids = {r["id"] for r in rules}
    names = registry_names()
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    have = sorted(p.stem for p in SRC.glob("*.md")) if SRC.exists() else []
    todo = want or have
    fails = 0
    for c in todo:
        text = " ".join(r["title"] + " " + r["check"] for r in rules if c in r["components"])
        bad = check(c, groups.get(c), text, names, rule_ids)
        print("%-16s %s" % (c, "ok" if not bad else "FAIL"))
        for b in bad:
            print("   " + b)
        fails += bool(bad)
    missing = sorted(names - set(have) - set(COMPUTED_ONLY))
    idle = sorted(set(COMPUTED_ONLY) & set(have))
    print("\n%d authored, %d declared computed-only, %d with neither"
          % (len(have), len(COMPUTED_ONLY), len(missing)))
    if missing:
        print("   " + ", ".join(missing))
    if idle:
        print("declared computed-only AND authored: " + ", ".join(idle))
        fails += 1
    sys.exit(1 if fails else 0)
