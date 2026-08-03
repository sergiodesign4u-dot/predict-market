"""Idempotent voice reconcile: the five trader terms a person meets while ACTING.

WHY THIS IS A POST-PROCESSOR AND NOT A GENERATOR. `CLAUDE.md` forbids running
`gen_*.py`: the voice rewrite was applied to the grey HTML by hand and never
back-ported, so regenerating reverts it. The grey tree is frozen against
REGENERATION, not against a text edit, so a change to shipped copy goes in place
and idempotently, the way `footer_reconcile.py` and `category_reconcile.py` do.

WHAT IT CHANGES, and why these five and not the eight that were found.
`voice/docs/voice.md` carries the invariant: the ban is about PLACE, not about
the word. A trader term is forbidden wherever a person meets it while ACTING - a
control label, a heading, a figure read to decide - and allowed inside a block
whose whole job is to explain the mechanism. And the head of an exempt block is
not inside the exemption, because a summary, a tab and a title are read by
everyone who never opens them.

Sorted by that invariant (`docs/backlog.md` 29), eight placements, five fail:

  1. `Holders`  on a `.seg` button in the Comments tab. A control label.
  2. `Liquidity` in `.ms-label`. A bare figure, and the panel is exempt for
     EXPLANATION, which a naked number is not.
  3. `Market` as `.market-title`, the `<summary>` of the collapsed panel. The
     head of an exempt block is not inside the exemption.
  4. `Market Context` as a `.rules-tab`. A tab label is an invitation, not an
     explanation, and this is the product's most-confused word sitting next to
     the one panel that exists to keep it unconfused.
  5. `(AMM)` trailing `.fine` under Confirm. Fine print read while deciding.

THREE PASS AND ARE NOT TOUCHED: `order book` and `AMM` inside `.md-sub`, which is
the mechanism being explained and says what it is NOT, and `AMM` on How It Works.

Both trees, same strings, same counts, so gate 18 stays quiet. Idempotent: every
replacement is skipped when its result is already there.

    python3 wireframes/_generators/voice_reconcile.py [--dry-run]

No em dash.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TREES = [ROOT / "wireframes", ROOT / "ui-visual"]

# (what it is, before, after). Anchored on the markup around the word rather than
# on the word, so a mention inside an explanation block cannot be caught by
# accident: `Market` alone appears in prose on nine screens and must stay there.
EDITS = [
    ("a control label, the comment sort",
     '<button type="button">Holders</button>',
     '<button type="button">Bettors</button>'),
    ("a figure read to decide",
     '<span class="ms-label">Liquidity</span>',
     '<span class="ms-label">Available to bet</span>'),
    ("the head of the exempt block",
     '<span class="market-title">Market ',
     '<span class="market-title">How the odds are set '),
    ("a tab label, which is an invitation",
     '>Market Context</button>',
     '>Background</button>'),
    ("fine print read before Confirm",
     'when you bet (AMM).',
     'when you bet.'),
]

# The page script names the tab by its own label, so the string lives twice: once
# in the markup and once in a comment beside the handler. A comment is not copy,
# but a comment naming a label that no longer exists is a document that does not
# match the product, which is the class gate 34 is for.
COMMENTS = [("/* Rules / Market Context tabs */", "/* Rules / Background tabs */")]


def main():
    dry = "--dry-run" in sys.argv
    total, files = 0, 0
    per = {}
    for tree in TREES:
        for path in sorted(tree.glob("*.html")):
            src = was = path.read_text(encoding="utf-8")
            for what, before, after in EDITS + [(c[0], c[0], c[1]) for c in COMMENTS]:
                n = src.count(before)
                if not n:
                    continue
                src = src.replace(before, after)
                key = (tree.name, what)
                per[key] = per.get(key, 0) + n
                total += n
            if src != was:
                files += 1
                if not dry:
                    path.write_text(src, encoding="utf-8")
    print("%s %d replacement(s) on %d file(s)"
          % ("would apply" if dry else "applied", total, files))
    for (tree, what), n in sorted(per.items()):
        print("   %-10s %-34s x%d" % (tree, what, n))


if __name__ == "__main__":
    main()
