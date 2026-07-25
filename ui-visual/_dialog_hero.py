#!/usr/bin/env python3
"""Propagate the shared-dialog hero SUBTITLE across every ui-visual page.

The hero visual (brass band, display title, floating round close, corner glow) is
CSS in `_theme.css` and needs no markup. Only the subtitle line is content, so this
idempotent post-processor inserts one `.sheet-sub` into the Sign-in and Add-funds
dialogs and relocates the sign-in lead out of the body (it now lives in the hero).

Voice-safe: no new marketing copy. The sign-in subtitle is the existing body lead,
condensed; the deposit subtitle is the existing 1:1 trust line, condensed. Logged in
`voice/docs/microcopy.md`.

Scope guard: it matches ONLY the block-form dialog (the <h2> on its own indented
line). The inline `outcome-dialog signin-dialog` / `outcome-dialog deposit-dialog`
variants (used inside the Win/Loss flow) keep `<h2>` inline, so they never match -
consistent with the CSS, which excludes `.outcome-dialog` from the hero.

Idempotent: re-running is a no-op. NEVER touches wireframes/ or regenerates a base.
Run from the repo root or the ui-visual/ dir: `python3 ui-visual/_dialog_hero.py`
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

SIGNIN_H2 = "Sign in or create account"
DEPOSIT_H2 = "Add funds"
SIGNIN_SUB = "You are about to place a bet. No crypto wallet required."
DEPOSIT_SUB = "Card or crypto. Your USDC is held 1:1."


def insert_sub(html, h2_text, sub_text):
    """Insert one <p class="sheet-sub"> right after a block-form <h2>, once."""
    pat = re.compile(
        r'(?P<line>(?P<ind>[ \t]+)<h2>' + re.escape(h2_text) + r'</h2>\n)'
        r'(?P<nextsub>[ \t]*<p class="sheet-sub")?'
    )

    def repl(m):
        if m.group("nextsub"):
            return m.group(0)  # already carries the subtitle - leave as is
        return m.group("line") + m.group("ind") + '<p class="sheet-sub">' + sub_text + "</p>\n"

    return pat.subn(repl, html, count=1)


def strip_signin_lead(html):
    """Remove the old sign-in body lead (its message now lives in the hero subtitle)."""
    return re.subn(r'\n[ \t]*<p class="fine signin-lead">.*?</p>', "", html, count=1, flags=re.S)


def main():
    pages = sorted(glob.glob(os.path.join(HERE, "*.html")))
    touched = 0
    for path in pages:
        with open(path, encoding="utf-8") as f:
            html = f.read()
        orig = html
        html, _ = insert_sub(html, SIGNIN_H2, SIGNIN_SUB)
        html, _ = insert_sub(html, DEPOSIT_H2, DEPOSIT_SUB)
        html, _ = strip_signin_lead(html)
        if html != orig:
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            touched += 1
            print("  updated", os.path.basename(path))
    print(f"dialog-hero subtitle: {touched} page(s) updated of {len(pages)} scanned")


if __name__ == "__main__":
    main()
