#!/usr/bin/env python3
"""
_unfork.py  -  one element, one rule. Delete the grey-box layer that the Vault
layer already overrides.

WHAT IS WRONG. Step 1 read the styling out of the painted product, and the
painted product had two stylesheets on it: the grey-box skeleton the wireframe
generator wrote inline, and the Vault theme file loaded after it. The extraction
kept both and concatenated them, so a component file describes the same element
twice: once as a grey box, once as it actually ships. `loadmore.css` writes the
button twice over, nine properties apart. Nothing renders the first version,
because every place a component stands is inside `.app-case`, so the second rule
always wins on specificity.

Across 31 files: 114 selectors declared twice, 220 property declarations in the
first layer that the second one overrides. That is not a style, it is a fossil.

WHAT THIS DOES. For every top level rule with selector S, if a top level rule
with selector `.app-case S` exists, delete from the first rule every property the
second one declares. `.app-case S` is S plus one class, so it is strictly more
specific and wins wherever both apply, whatever the source order and whatever
media block either sits in. When the first rule empties out, the line goes.

WHAT IT DELIBERATELY DOES NOT DO. It does not touch a rule inside `@media`, and
it does not match a twin loosely (`.app-case .a .b` is not treated as the twin of
`.b`, even where it would in fact dominate it). Both would need reasoning the
diff cannot check. It also leaves the `.app-case` prefix in place: the prefix is
the scope marker that keeps product rules off the vitrine chrome, so stripping it
is a separate question from deleting a corpse.

Verified with ui-kit/_verify: snapshot 76 screens at 5 widths before and after,
diff by element and property. This pass is meant to change nothing on screen.

Idempotent. No em dash.

    python3 ui-kit/_unfork.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMP = os.path.join(ROOT, "components")
SKIP = {"index.css", "tokens.css"}

RULE = re.compile(r"^([^{}@/][^{}]*)\{([^{}]*)\}\s*$")

# Selectors that look dominated and are not, because they match elements that
# live OUTSIDE the device case. Measured, not guessed: every candidate was run
# through document.querySelectorAll on all 77 painted screens and all 45 stands,
# asking whether any match has no .app-case ancestor.
#
#   .filter-menu summary   the footer language menu sits under the device
#   .field-label           the shared <dialog>s are appended at the end of the
#   .protect               body, so a dialog is a sibling of .app-case and not
#                          a descendant. For those the unprefixed rule IS the
#                          shipped one, and the .app-case twin is what is dead
#                          there. Left alone on purpose.
#
# IT WAS FIVE AND IS THREE SINCE 2026-08-05. `.confirm-btn` and `.provider-btn`
# were on this list for the same reason, and the vocabulary migration ended the
# reason rather than the entries: components/button.css no longer writes
# `.app-case` at ALL, so a button selector can never become a candidate here and
# an entry for one protects nothing. An exception that cannot fire is not a
# safeguard, it is a claim about the stylesheet that has stopped being true, so
# it comes out with the names it was written for.
OUTSIDE_THE_CASE = {
    ".filter-menu summary", ".field-label", ".protect",
}


def props_of(body):
    """property names declared in a rule body, in order, custom properties included"""
    out = []
    depth = 0
    cur = ""
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    names = []
    for d in out:
        if ":" in d:
            names.append(d.split(":", 1)[0].strip())
    return names


def split_decls(body):
    out = []
    depth = 0
    cur = ""
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [d for d in out if d.strip()]


def top_level_lines(text):
    """yield (index, line) for lines that are a whole rule at top level.

    The files are written one rule per line, except a handful of box-shadow
    values that wrap. A rule that does not open and close on its own line is
    joined with the lines that follow it before it is considered.
    """
    lines = text.split("\n")
    out = []
    i = 0
    depth = 0
    while i < len(lines):
        line = lines[i]
        start = i
        buf = line
        if buf.strip().startswith("@") or (depth and "{" not in buf):
            depth += buf.count("{") - buf.count("}")
            i += 1
            continue
        if depth > 0:
            depth += buf.count("{") - buf.count("}")
            i += 1
            continue
        while buf.count("{") > buf.count("}") and i + 1 < len(lines):
            i += 1
            buf += "\n" + lines[i]
        if buf.count("{") == buf.count("}") and buf.count("{") == 1:
            out.append((start, i, buf))
        else:
            depth += buf.count("{") - buf.count("}")
        i += 1
    return lines, out


def main():
    dry = "--dry-run" in sys.argv
    total_sel = total_props = total_rules = 0
    for fname in sorted(os.listdir(COMP)):
        if not fname.endswith(".css") or fname in SKIP:
            continue
        path = os.path.join(COMP, fname)
        text = open(path, encoding="utf-8").read()
        lines, rules = top_level_lines(text)

        # what the .app-case layer declares, per bare selector
        skin = {}
        for _, _, buf in rules:
            m = RULE.match(buf.strip() + "\n")
            if not m:
                continue
            for sel in m.group(1).split(","):
                s = " ".join(sel.split())
                if s.startswith(".app-case "):
                    skin.setdefault(s[len(".app-case "):], set()).update(props_of(m.group(2)))

        drop_lines = set()
        edits = {}
        for start, end, buf in rules:
            m = RULE.match(buf.strip() + "\n")
            if not m:
                continue
            sels = [" ".join(s.split()) for s in m.group(1).split(",")]
            if any(s.startswith(".app-case") for s in sels):
                continue
            if any(s in OUTSIDE_THE_CASE for s in sels):
                continue
            # every selector in the list must be dominated, or the rule stays
            covered = [skin.get(s) for s in sels]
            if not all(covered):
                continue
            killed = set.intersection(*[set(c) for c in covered])
            if not killed:
                continue
            keep = [d for d in split_decls(m.group(2))
                    if d.split(":", 1)[0].strip() not in killed]
            total_props += len(split_decls(m.group(2))) - len(keep)
            total_sel += 1
            if keep:
                edits[start] = "%s{%s}" % (m.group(1), ";".join(d.strip() for d in keep))
                for k in range(start + 1, end + 1):
                    drop_lines.add(k)
            else:
                total_rules += 1
                for k in range(start, end + 1):
                    drop_lines.add(k)

        if not edits and not drop_lines:
            continue
        out = []
        for i, line in enumerate(lines):
            if i in drop_lines:
                continue
            out.append(edits.get(i, line))
        new = "\n".join(out)
        print("%-22s %2d selectors thinned, %2d rules gone" % (
            fname, sum(1 for i in edits), sum(1 for i in drop_lines)))
        if not dry:
            open(path, "w", encoding="utf-8").write(new)
    print("\n%d selectors, %d dead declarations, %d rules removed entirely"
          % (total_sel, total_props, total_rules))


if __name__ == "__main__":
    main()
