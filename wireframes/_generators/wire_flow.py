# Krok 7 - flow linking. Wires Event Feed / category card questions and YES/NO
# trigger-entries to the correct Event Detail (binary vs multi-outcome; logged-in
# vs logged-out), per IA/flows.md MJ edge "found -> ED" (neutral + pre-selected).
# Idempotent: safe to re-run. Re-run after regenerating feed / category pages
# (same convention as wire_catnav.py / inject_signin.py).
import pathlib
import re

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

CARD_RE = re.compile(r'<article class="card">.*?</article>', re.S)
Q_RE = re.compile(r'(<a class="q" href=")[^"]*(")')
BIN_YESNO = '<div class="yesno"><button type="button">YES</button><button type="button">NO</button></div>'
MULTI_YESNO = '<span class="yesno compact"><button type="button">YES</button><button type="button">NO</button></span>'


def wire_card(block, target):
    # question link -> target
    block = Q_RE.sub(lambda m: m.group(1) + target + m.group(2), block)
    # binary YES/NO -> wrap each button in a link to target (idempotent)
    if BIN_YESNO in block:
        block = block.replace(
            BIN_YESNO,
            f'<div class="yesno"><a href="{target}"><button type="button">YES</button></a>'
            f'<a href="{target}"><button type="button">NO</button></a></div>')
    # multi compact YES/NO (per option row) -> wrap each button
    if MULTI_YESNO in block:
        block = block.replace(
            MULTI_YESNO,
            f'<span class="yesno compact"><a href="{target}"><button type="button">YES</button></a>'
            f'<a href="{target}"><button type="button">NO</button></a></span>')
    return block


def process(path):
    html = path.read_text()
    if 'class="yesno"' not in html:
        return None
    suffix = "-logged-out" if "logged-out" in path.name else ""

    def repl(m):
        block = m.group(0)
        multi = ("opt-row" in block) or ("yesno compact" in block)
        target = f"event-detail{suffix}{'-multi' if multi else ''}.html"
        return wire_card(block, target)

    new = CARD_RE.sub(repl, html)
    if new != html:
        path.write_text(new)
        assert "—" not in new, f"em dash in {path.name}"
        return path.name
    return None


done = [process(p) for p in sorted(ROOT.glob("*.html"))]
print("\n".join(d for d in done if d) or "no changes")
