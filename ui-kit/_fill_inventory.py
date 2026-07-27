#!/usr/bin/env python3
"""
_fill_inventory.py  -  give ui-kit/docs/inventory.md the two columns it was
missing: which css file owns the component, and which stand page shows it.

WHY IT MATTERS. The inventory was read out of the product before the system
existed, so it was a list of things a screen contains. Once the system exists,
the same table has to answer the question a person actually arrives with: I am
looking at this thing, where do I edit it, and where do I see it on its own.
Without those two columns the table is a census; with them it is an index.

HOW THE MAPPING IS MADE. A row that quotes a class (`.card`, `.opt-row`) is
matched against the `Classes:` header every component file carries, so most of
the table maps itself and stays correct when a class moves file. The rows that
name their component in prose instead are in TITLE below, one line each, and
that list is the only hand-written part.

A row with no component is not a gap: some rows are layout facts (a responsive
grid) or one-off screen furniture. Those get a dash, and the dash is a claim in
its own right, so it is written here rather than left blank.

Idempotent: rebuilds both columns from scratch on every run.

    python3 ui-kit/_fill_inventory.py [--check]
No em dash.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = os.path.join(ROOT, "ui-kit", "docs", "inventory.md")
COMP = os.path.join(ROOT, "components")
KIT = os.path.join(ROOT, "ui-kit")

# rows that name their component in prose rather than by class
TITLE = {
    "App header (lean)": "header",
    "Logo (Events home)": "header",
    "Balance / Portfolio-Cash swap": "header",
    "Notifications bell + mini-dropdown": "header",
    "Avatar menu (dropdown)": "header",
    "How-it-works button": "header",
    "Icon button (ghost)": "header",
    "Auth entries (Log in / Sign up)": "button",
    "Category nav band": "catnav",
    "Bottom nav (mobile, 4 slots)": "bottomnav",
    "Active / History tabs": "tabs",
    "Footer language menu": "footer",
    "Screen-tree drawer / roadmap sidebar": "course-chrome",
    "Event card, binary (treatment B)": "card",
    "Event card, multi (treatment D)": "card",
    "Odds bar (thin, green YES on red track)": "oddsbar",
    "Tinted YES / NO buttons": "yesno",
    "Probability figure": "card",
    "Card meta row (Volume / Closes + bookmark)": "card",
    "Responsive card grid": "feed",
    "hero trust cards": "hero",
    "Load-more control": "loadmore",
    "Resolution block": "event-detail",
    "Content tab strip": "tabs",
    "Shared dialog shell": "dialog",
    "Provider buttons (Google / X / Apple, real brand marks)": "button",
    "Amount field + quick-amount chips": "input",
    "Field label": "input",
    "Primary CTA (brass)": "button",
    "Bottom-sheet / modal overlay (grab, backdrop)": "dialog",
    "Filter menu (Sort / Frequency)": "filters",
    "Reverse-order toggle switch": "filters",
    "Win overlay": "dialog",
    "Loss overlay": "dialog",
    "Share Card (auto-generated win visual, reused in profile gallery)": "dialog",
    "Section divider": "position",
    "Reputation stat-grid": "profile",
    "Profile tabs": "profile",
    "Transaction list (deposits/payouts/fees/stakes)": "account",
    "Product footer (brand, markets, product, support, company, legal)": "footer",
    "Footer trust strip": "trustbar",
}

# a component file whose stand page is named differently
PAGE = {
    "dialog": ["dialog", "outcome-dialog", "signin"],
    "profile": ["profile"],
    "tabs": ["tabs"],
}


def class_owner():
    owner = {}
    for fname in sorted(os.listdir(COMP)):
        if not fname.endswith(".css"):
            continue
        with open(os.path.join(COMP, fname), encoding="utf-8") as fh:
            head = fh.read(2000)
        m = re.search(r"Classes:\s*([^\n]*)", head)
        if not m:
            continue
        for c in re.findall(r"\.([\w-]+)", m.group(1)):
            owner.setdefault(c, fname[:-4])
    return owner


def stems_for(title, owner):
    classes = re.findall(r"`\.?([\w.-]+)", title)
    stems = []
    for c in classes:
        c = c.lstrip(".").split(".")[0]
        if c in owner and owner[c] not in stems:
            stems.append(owner[c])
    if stems:
        return stems
    for key, stem in TITLE.items():
        if key.lower() in title.lower():
            return [stem]
    return []


def main():
    check = "--check" in sys.argv
    with open(INV, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    owner = class_owner()
    pages = {f[:-5] for f in os.listdir(KIT) if f.endswith(".html")}
    out, filled, dashed = [], 0, 0
    for line in lines:
        if not (line.startswith("|") and line.count("|") >= 7):
            out.append(line)
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] == "Component":
            cells = cells[:1] + ["CSS file", "Page"] + cells[1:]
            out.append("| " + " | ".join(cells) + " |")
            continue
        if set(cells[0]) <= set("-: "):
            out.append("| " + " | ".join(["---"] * (len(cells) + 2)) + " |")
            continue
        # drop every pair a previous run added, then add one back. It loops because a
        # run that failed to recognise its own output once left two pairs behind.
        while len(cells) >= 3:
            prev = cells[1].strip("`")
            if prev.endswith(".css") or prev == "-":
                cells = cells[:1] + cells[3:]
            else:
                break
        stems = stems_for(cells[0], owner)
        if stems:
            css = ", ".join("`%s.css`" % s for s in stems)
            pg = []
            for s in stems:
                for cand in PAGE.get(s, [s]):
                    if cand in pages and cand not in pg:
                        pg.append(cand)
            page = ", ".join("[%s](../%s.html)" % (p, p) for p in pg) or "-"
            filled += 1
        else:
            css, page = "-", "-"
            dashed += 1
        out.append("| " + " | ".join(cells[:1] + [css, page] + cells[1:]) + " |")
    text = "\n".join(out) + "\n"
    if not check:
        with open(INV, "w", encoding="utf-8") as fh:
            fh.write(text)
    print("rows with a component: %d, rows deliberately dashed: %d" % (filled, dashed))


if __name__ == "__main__":
    main()
