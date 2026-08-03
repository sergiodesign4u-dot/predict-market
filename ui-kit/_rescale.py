#!/usr/bin/env python3
"""Move every consumer onto the rescaled primitives. Idempotent, dry-runnable.

    python3 ui-kit/_rescale.py --dry-run
    python3 ui-kit/_rescale.py

Why this file exists. The token file was READ out of the painted product, and
reading is the right method for a colour role and the wrong one for a scale:
every literal the grey wireframe happened to type became a token, so space had
25 steps with 1 2 3 4 5 6 7 8 9 10 in a row, text had five half pixels left over
from rem arithmetic, and radius carried two names for the same pill. This maps
each of those onto a scale and rewrites the consumers.

The maps below ARE the record of the change: what moved, to where, and by the
rule stated with each family. Nothing here is invented. Every target is a value
that already stood in the file; a value that sits exactly between two steps
breaks toward the HEAVIER neighbour, measured on the declaration counts before
the change, which on this product always means the smaller step, so no layout
inflates.

What it does not touch, by the rule already written in ui-kit/docs/architecture.md:
the offsets and blur radii inside a box-shadow, gradient stop positions, transform
distances, border widths, and decorative one-off geometry (the 224px glow blob,
mask radii, svg stroke widths). Those are not a scale and a token would only hide
what the number is doing.

Idempotent: once applied, a second run reports 0 rewrites, which is what gate 12
in ui-kit/_check_kit.py leans on. No em dash.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# components/patterns/ is in the list on purpose. A pattern is not a component,
# but it is a stylesheet of this system and it reads the same roles, so the
# Reads: header belongs on it for the same reason it belongs on the others: the
# file says what it depends on and a script keeps that true.
TARGETS = ([p for p in sorted((ROOT / "components").glob("*.css"))
            if p.name not in ("tokens.css", "index.css")]
           + sorted((ROOT / "components" / "patterns").glob("*.css"))
           + [ROOT / "ui-kit" / "_page.css", ROOT / "ui-kit" / "_specimen.css"])

# Properties that take a distance. A token landing on one of these is spacing;
# on one of the SIZE properties it is the measurement of a thing, and the two
# read differently: 1px of padding is a small gap, 1px of height is a line.
SPACING = {"padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
           "margin", "margin-top", "margin-right", "margin-bottom", "margin-left",
           "gap", "row-gap", "column-gap", "grid-gap"}
SIZE = {"width", "height", "min-width", "min-height", "max-width", "max-height",
        "flex", "flex-basis", "inset", "top", "right", "bottom", "left", "size"}

# ---------------------------------------------------------------------- space
# The grid is 4px. 2 is the only half step. 1px is not a distance, it is a line,
# so it leaves the scale for --hairline wherever it measures something.
#   6 -> 8 and 10 -> 8 collapse three near identical small steps into one.
#   14 -> 12, 18 -> 16, 22 -> 20, 26 -> 24, 30 -> 28: tie, heavier neighbour.
SPACE = {
    "--space-1":  {"size": "--hairline", "spacing": "--space-2"},
    "--space-2":  "--space-2",
    "--space-3":  "--space-4",
    "--space-4":  "--space-4",
    "--space-5":  "--space-4",     # also the odds bar: 4px still reads thin
    "--space-6":  "--space-8",
    "--space-7":  "--space-8",
    "--space-8":  "--space-8",
    "--space-9":  "--space-8",
    "--space-10": "--space-8",
    "--space-12": "--space-12",
    "--space-14": "--space-12",
    "--space-16": "--space-16",
    "--space-18": "--space-16",
    "--space-20": "--space-20",
    "--space-22": "--space-20",
    "--space-24": "--space-24",
    "--space-26": "--space-24",
    "--space-28": "--space-28",
    "--space-30": "--space-28",
    "--space-34": "--space-32",
    "--space-40": "--space-40",
    "--space-42": "--space-40",
    "--space-44": "--space-40",
    "--space-56": {"size": "--size-56", "spacing": "--space-56"},
}

# --------------------------------------------------------------------- radius
# Five corners, one per job: 2 the near square card of the Vault, 6 a small chip,
# 10 the default control, 16 a sheet, pill a track.
# --radius-round (1000px) rendered the same pill as --radius-pill on every
# control that used it, and --radius-circle had no consumer at all.
RADIUS = {
    "--radius-2": "--radius-2",
    "--radius-4": "--radius-6",
    "--radius-6": "--radius-6",
    "--radius-8": "--radius-10",
    "--radius-10": "--radius-10",
    "--radius-12": "--radius-10",
    "--radius-14": "--radius-16",
    "--radius-16": "--radius-16",
    "--radius-20": "--radius-16",
    "--radius-pill": "--radius-pill",
    "--radius-round": "--radius-pill",
}

# ------------------------------------------------------------ control and icon
# Value named, like every other geometry token, and each one carries its job as a
# comment in tokens.css. --control-38 was a number with no job.
CONTROL = {
    "--control-sm": "--control-32",
    "--control-md": "--control-36",
    "--control-38": "--control-36",
    "--control-lg": "--control-44",
    # "--control-xl": "--control-52" stood here and went with the token on
    # 2026-08-03. A rename map is a map to something that EXISTS: the target left
    # tokens.css when .btn-lg, its only reader, left components/, and the dry run
    # said so in the same minute. It is deleted rather than pointed at
    # --control-44, because 52 and 44 are different heights and a migration that
    # quietly resizes a control is worse than one that does not run. If the old
    # name ever comes back, gate 11's dangling-var check is what catches it.
    "--icon-15": "--icon-16",
    "--icon-16": "--icon-16",
    "--icon-17": "--icon-18",
    "--icon-18": "--icon-18",
    "--icon-22": "--icon-22",
    "--size-thumb": "--size-56",
    "--size-avatar": "--size-72",
}

# ----------------------------------------------------------------------- text
# Ten steps: 10 11 12 13 14 16 18 20 24 30. The half pixels came from the grey
# wireframe's rem arithmetic and round UP, so every line that moves gets bigger,
# never smaller. 8 and 9 were below the floor a mobile product should set.
TEXT = {
    "--text-8": "--text-10",
    "--text-9": "--text-10",
    "--text-9-5": "--text-10",
    "--text-10": "--text-10",
    "--text-10-5": "--text-11",
    "--text-11": "--text-11",
    "--text-11-5": "--text-12",
    "--text-12": "--text-12",
    "--text-12-5": "--text-13",
    "--text-13": "--text-13",
    "--text-13-5": "--text-14",
    "--text-14": "--text-14",
    "--text-15": "--text-16",
    "--text-16": "--text-16",
    "--text-18": "--text-18",
    "--text-20": "--text-20",
    "--text-24": "--text-24",
    "--text-30": "--text-30",
}

# -------------------------------------------------------------------- leading
# 1.04 and 1.05 are the same line. 1.45, 1.5, 1.55 and 1.6 were four body
# leadings; two of them are enough (a body measure and a reading measure).
LEADING = {
    "--leading-flat": "--leading-flat",
    "--leading-heading": "--leading-flat",
    "--leading-tight": "--leading-tight",
    "--leading-snug": "--leading-snug",
    "--leading-body": "--leading-base",
    "--leading-base": "--leading-base",
    "--leading-relaxed": "--leading-base",
    "--leading-loose": "--leading-loose",
}

# ------------------------------------------------------------ colour, level 1
# Primitives only. Components read colour through a role, so nothing in a
# component file changes here: the roles keep their names and point at fewer raw
# values. Two rules decide a merge, and both have to hold:
#   1. the pair is under deltaE 1.5 in Lab, which no eye separates side by side;
#   2. the two never MEET, not as two stops of one gradient and not as parent and
#      child on screen. That is why --graphite-850 (a chip) does not fold into
#      --graphite-830 (the surface a chip sits on) even at deltaE 0.49, and why
#      --graphite-920 (the card gradient end) stays out of --graphite-930 (the
#      page): folding it would give the card the same gradient as its own plate.
GRAPHITE_MERGE = {
    "--graphite-935": "--graphite-940",   # dE 1.17  chart well and input well: one recess
    "--graphite-915": "--graphite-910",   # dE 0.43  course sidebar and content plate
    "--graphite-905": "--graphite-900",   # dE 0.76  card base and device canvas
    "--graphite-895": "--graphite-900",   # dE 0.99  the prompt on hover
    "--graphite-890": "--graphite-880",   # dE 0.51  the mobile dock and the quiet block
    "--graphite-865": "--graphite-860",   # dE 1.49  dock gradient start and slab base
    "--graphite-855": "--graphite-860",   # dE 0.95  a chip pressed
    "--graphite-840": "--graphite-830",   # dE 0.94  sticky header and raised surface
    "--graphite-790": "--graphite-800",   # dE 0.72  dialog head gradient and control hover
}
# One family, one ladder. An alpha step of 0.05 on a hairline, a tint or a shadow
# is below the threshold of a screen; fifteen steps of one brass were not a
# decision anyone made, they were fifteen numbers that got typed.
ALPHA_MERGE = {
    "--brass-a055": "--brass-a06", "--brass-a08": "--brass-a09",
    "--brass-a14": "--brass-a16", "--brass-a24": "--brass-a30",
    "--brass-a35": "--brass-a30", "--brass-a40": "--brass-a45",
    "--brass-a42": "--brass-a45", "--brass-a50": "--brass-a45",
    "--brass-a55": "--brass-a60",
    "--black-a35": "--black-a30", "--black-a40": "--black-a45",
    "--black-a42": "--black-a45", "--black-a50": "--black-a45",
    "--black-a55": "--black-a60", "--black-a70": "--black-a72",
    "--black-a78": "--black-a72", "--black-a80": "--black-a85",
    "--black-a90": "--black-a85",
    "--white-a03": "--white-a04", "--white-a05": "--white-a06",
    "--white-a09": "--white-a10", "--white-a14": "--white-a16",
    "--white-a15": "--white-a16", "--white-a17": "--white-a16",
    "--green-a10": "--green-a12", "--red-a10": "--red-a12",
    "--bone-150": "--bone-100",           # dE 1.47  chip label on hover is primary text
    "--red-320": "--red-300",             # the pair the file already flagged for this step
}
PRIMITIVE_MERGE = dict(GRAPHITE_MERGE)
PRIMITIVE_MERGE.update(ALPHA_MERGE)

# ------------------------------------------------------------ colour, level 2
# Only the roles whose NAME carries the old alpha. A role named after a value it
# no longer holds is worse than either name, so the number follows the ladder.
# Where two of them land on one name they were one role all along.
ROLE_RENAME = {
    "--tint-brass-08": "--tint-brass-09",
    "--tint-brass-14": "--tint-brass-16",
    "--tint-brass-24": "--tint-brass-30",
    "--tint-brass-40": "--tint-brass-45",
    "--tint-brass-42": "--tint-brass-45",
    "--shadow-ink-40": "--shadow-ink-45",
    "--shadow-ink-42": "--shadow-ink-45",
    "--shadow-ink-55": "--shadow-ink-60",
    "--shadow-ink-70": "--shadow-ink-72",
    "--shadow-ink-soft": "--shadow-ink-72",
    "--shadow-ink-80": "--shadow-ink-85",
    "--shadow-ink-90": "--shadow-ink-85",
    "--shadow-ink-deep": "--shadow-ink-85",
}

TOKENS = {}
for m in (SPACE, RADIUS, CONTROL, TEXT, LEADING, ROLE_RENAME):
    TOKENS.update(m)

# ------------------------------------------------------------------- literals
# A raw value that IS a scale step, written past the variable. Property scoped:
# only the six properties where a number is a scale value. Everything else keeps
# its literal, because a 27px gradient stop or a 1px border is not a step.
# (file, before, after) so each rewrite is named and reviewable.
LITERAL = [
    # the display ramp: nine clamp() written out, none of them behind a token
    ("feed.css", "font-size:clamp(28px,4vw,38px)", "font-size:var(--display-feed)"),
    ("hiw-dialog.css", "font-size:clamp(30px,7vw,38px)", "font-size:var(--display-hiw)"),
    ("dialog.css", "font-size:clamp(24px,5.6vw,30px)", "font-size:var(--display-sheet)"),
    ("dialog.css", "font-size:clamp(23px,5.4vw,29px)", "font-size:var(--display-sheet)"),
    ("seo-plate.css", "font-size:clamp(20px,2.6vw,24px)", "font-size:var(--display-seo)"),
    ("event-detail.css", "font-size:clamp(19px,2vw,24px)", "font-size:var(--display-question)"),
    # the hero title kept its own ramp: folding it into --display-question grew it
    # from 19.2px to 24px at 1280, which is a redesign and not a rounding
    ("hero.css", "font-size:clamp(19px,1.5vw,23px)", "font-size:var(--display-hero)"),
    ("hero.css", "font-size:clamp(20px,1.85vw,26px)", "font-size:var(--display-quote)"),
    ("seo-plate.css", "font-size:clamp(23px,2.3vw,31px)", "font-size:var(--display-tagline)"),
    # the two sizes that were declared as tokens and never wired
    ("card.css", "flex:0 0 56px", "flex:0 0 var(--size-56)"),
    ("skeleton.css", "flex:0 0 56px", "flex:0 0 var(--size-56)"),
    ("event-detail.css", "width:72px;height:72px;flex:0 0 72px",
     "width:var(--size-72);height:var(--size-72);flex:0 0 var(--size-72)"),
    ("profile.css", "width:72px;height:72px;flex:0 0 72px",
     "width:var(--size-72);height:var(--size-72);flex:0 0 var(--size-72)"),
    ("hero.css", "flex:0 0 42px", "flex:0 0 var(--space-40)"),
    ("hiw-dialog.css", "flex:0 0 34px", "flex:0 0 var(--space-32)"),
    ("trustbar.css", "flex:0 0 15px", "flex:0 0 var(--icon-16)"),
    # the last off-grid values, each one a number typed straight into a rule.
    # A layout position above 64px (the 104px rail offset, the 118px inset behind
    # an overlapping figure, the 220px sidebar) is NOT a step and stays literal,
    # except the sidebar, which had a token declared for it all along.
    ("betpanel.css", "padding:11px var(--space-8)", "padding:var(--space-12) var(--space-8)"),
    ("base.css", "padding:13px var(--space-12)", "padding:var(--space-12) var(--space-12)"),
    ("base.css", "padding-left:220px!important", "padding-left:var(--container-sidebar)!important"),
    ("catnav.css", "font-size:14.5px", "font-size:var(--text-14)"),
    ("comments.css", "margin-left:32px", "margin-left:var(--space-32)"),
    ("header.css", "font-size:8.5px", "font-size:var(--text-10)"),
    ("hiw-dialog.css", "padding:32px var(--space-24)", "padding:var(--space-32) var(--space-24)"),
    ("options.css", "padding:4px 12px", "padding:var(--space-4) var(--space-12)"),
    ("profile.css", "font-size:22px", "font-size:var(--text-20)"),
    ("seo-plate.css", "padding:36px var(--space-40)", "padding:var(--space-40) var(--space-40)"),
    # line heights written past the scale. File is None: the mapping is the same
    # wherever it stands, so it does not need naming a file to be reviewable.
    # line-height:0 is NOT here; it is an icon reset, not a leading.
    (None, "line-height:1.4", "line-height:var(--leading-base)"),
    (None, "line-height:1.35", "line-height:var(--leading-snug)"),
    (None, "line-height:1.25", "line-height:var(--leading-snug)"),
    (None, "line-height:1.2", "line-height:var(--leading-tight)"),
    (None, "line-height:1.1", "line-height:var(--leading-flat)"),
    (None, "line-height:1.06", "line-height:var(--leading-flat)"),
    (None, "line-height:1", "line-height:var(--leading-none)"),
]

VAR = re.compile(r"var\((--[\w-]+)\)")


def prop_at(src, i):
    """The property whose value contains offset i, or ''. Scans back to the last
    declaration boundary, which is enough: css has no nested declarations."""
    start = max(src.rfind(c, 0, i) for c in ";{}")
    m = re.match(r"\s*([a-z-]+)\s*:", src[start + 1:i])
    return m.group(1) if m else ""


def rewrite(src):
    """-> (new source, [(old, new, property)])"""
    edits, moved = [], []
    for m in VAR.finditer(src):
        old = m.group(1)
        rule = TOKENS.get(old)
        if rule is None:
            continue
        if isinstance(rule, dict):
            p = prop_at(src, m.start())
            kind = "size" if p in SIZE else "spacing"
            new = rule[kind]
        else:
            new = rule
        if new == old:
            continue
        edits.append((m.start(1), m.end(1), new))
        moved.append((old, new, prop_at(src, m.start())))
    for a, b, new in reversed(edits):
        src = src[:a] + new + src[b:]
    return src, moved


def merge_tokens(src):
    """The colour half: fold the merged primitives out of tokens.css and repoint
    every role that read one. Roles keep their names except where the name spells
    an alpha the value no longer has (ROLE_RENAME). -> (new source, [(old, new)])"""
    moved = []
    for old, new in PRIMITIVE_MERGE.items():
        # the declaration, its trailing comment and its newline
        pat = re.compile(r"[ \t]*" + re.escape(old) + r":[^;]*;[ \t]*(?:/\*(?:[^*]|\*(?!/))*\*/)?[ \t]*\n?")
        src, n = pat.subn("", src)
        if n:
            moved.append((old, new))
    for old, new in list(PRIMITIVE_MERGE.items()) + list(ROLE_RENAME.items()):
        src, n = re.subn(r"var\(" + re.escape(old) + r"\)", "var(%s)" % new, src)
        if n and (old, new) not in moved:
            moved.append((old, new))
    for old, new in ROLE_RENAME.items():
        src, n = re.subn(r"(?m)^([ \t]*)" + re.escape(old) + r":", r"\g<1>%s:" % new, src)
        if n:
            moved.append((old, new))
    # a rename can leave the same role declared twice; the later one wins in css,
    # and both carry the same value, so the earlier declaration is dropped.
    # PER BLOCK, and the word matters. When this was written the file had one
    # block, so "declared twice" and "declared twice in the same block" were the
    # same sentence. Then section 3 arrived and re-declared six of these roles
    # with the values daylight needs, and the sweep ate them: a theme override IS
    # the same name a second time, deliberately, in a different selector.
    seen, depth, out = set(), 0, []
    for line in src.splitlines(True):
        m = re.match(r"[ \t]*(--[\w-]+):", line)
        if m and depth == 1 and m.group(1) in ROLE_RENAME.values():
            if m.group(1) in seen:
                continue
            seen.add(m.group(1))
        out.append(line)
        depth += line.count("{") - line.count("}")
        if depth == 0:
            seen.clear()          # a new block declares its own names
    return "".join(out), moved


def refresh_header(src, roles):
    """The "Reads:" line at the top of a component file lists the colour roles it
    uses. It is derived data, so after a rename it is derived again rather than
    left to rot: a header that lies is worse than no header."""
    mine = sorted({m for m in re.findall(r"var\((--[\w-]+)\)", src) if m in roles})
    if not mine:
        return src
    return re.sub(r"(?m)^(   Reads:  ?).*$", lambda m: m.group(1) + ", ".join(mine), src, count=1)


def main():
    dry = "--dry-run" in sys.argv
    tokens_path = ROOT / "components" / "tokens.css"
    declared = set(re.findall(r"(--[\w-]+)\s*:", tokens_path.read_text(encoding="utf-8")))
    total, files, report = 0, 0, {}
    tok_was = tokens_path.read_text(encoding="utf-8")
    tok_now, merged = merge_tokens(tok_was)
    if tok_now != tok_was:
        files += 1
        total += len(merged)
        for old, new in merged:
            report[(old, new)] = report.get((old, new), 0) + 1
        if not dry:
            tokens_path.write_text(tok_now, encoding="utf-8")
        declared = set(re.findall(r"(--[\w-]+)\s*:", tok_now))
    roles = set(re.findall(r"(--[\w-]+)\s*:", tok_now[tok_now.index("2. SEMANTIC"):]))
    for path in TARGETS:
        src = was = path.read_text(encoding="utf-8")
        for name, before, after in LITERAL:
            if name not in (None, path.name):
                continue
            # the guard matters: "line-height:1" is a prefix of "line-height:1.4",
            # and replacing the prefix would write var(--leading-none).4
            pat = re.compile(re.escape(before) + r"(?![\w.%-])")
            src, n = pat.subn(after.replace("\\", "\\\\"), src)
            if n:
                report.setdefault((before, after), 0)
                report[(before, after)] += n
                total += n
        src, moved = rewrite(src)
        for old, new, _prop in moved:
            report.setdefault((old, new), 0)
            report[(old, new)] += 1
        total += len(moved)
        headed = refresh_header(src, roles)
        if headed != src:
            report.setdefault(("Reads: header", "recomputed"), 0)
            report[("Reads: header", "recomputed")] += 1
            total += 1
            src = headed
        if src != was:
            files += 1
            if not dry:
                path.write_text(src, encoding="utf-8")
    print("%s %d rewrites on %d of %d files" %
          ("would apply" if dry else "applied", total, files, len(TARGETS)))
    for (old, new), n in sorted(report.items(), key=lambda kv: -kv[1]):
        print("  %-46s -> %-34s x%d" % (old[:46], new[:34], n))
    # A rewrite that points at a name the token file does not declare would be a
    # silent broken var(). Cheap to check here, so it is checked here.
    wanted = {v for v in TOKENS.values() if isinstance(v, str)}
    wanted |= {v for r in TOKENS.values() if isinstance(r, dict) for v in r.values()}
    wanted |= set(re.findall(r"var\((--[\w-]+)\)", " ".join(a for _f, _b, a in LITERAL)))
    missing = sorted(w for w in wanted if w not in declared)
    if missing:
        print("\nMISSING from components/tokens.css: %s" % ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
