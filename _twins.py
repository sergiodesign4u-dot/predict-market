#!/usr/bin/env python3
"""
_twins.py  -  the one place a painted screen and its grey twin are matched.

WHY THIS FILE EXISTS. Gate 18 pairs the two trees by FILENAME, and one family
does not share filenames: a category page is politics.html in grey and
event-feed-politics.html in colour, because the grey tree calls it a Category
screen and the paint files it as a variant of the Event Feed. Both names are
defensible and neither is wrong, but the consequence was: the four painted
category pages had no twin under their own name, so gate 18 skipped them in
silence, and the whole family drifted for two stages with every gate green.

That is the same shape as every other defect this stage has found. A gate that
cannot see a pair certifies nothing about it, and a check that reports zero
because it looked at nothing reads exactly like a check that reports zero
because everything agrees.

The map itself already existed, in FIVE copies (_apply_theme, _apply_family,
_relink twice over, port_structure's HREF), each written by hand at the moment
its own tool needed it. Step 7c settled this for the component inventory and the
same rule applies here: two artifacts of one system disagreeing is the defect,
one computation feeding both is the fix.

WHAT IS AND IS NOT IN HERE. Only the rename. A screen that exists in one tree
and not in the other is a COVERAGE question and belongs to whoever owns that
tree, not to a lookup table.
"""

CATS = ("politics", "crypto", "culture", "general")

# The state set a category page carries, as the grey tree names it. The empty
# string is the base page. This is the Event Feed's own state set, because a
# category page is the same listing with one filter applied, and a listing that
# can be empty on Trending can be empty on Politics.
STATES = ("", "-empty", "-error", "-loading",
          "-logged-out", "-logged-out-empty", "-logged-out-error",
          "-logged-out-loading")

# grey name -> painted name. One direction is written, the other is derived, so
# they cannot disagree.
PAINTED = {"%s%s.html" % (c, s): "event-feed-%s%s.html" % (c, s)
           for c in CATS for s in STATES}
GREY = {v: k for k, v in PAINTED.items()}


def painted_of(grey_name):
    """The painted twin of a grey screen, or the same name when it is shared."""
    return PAINTED.get(grey_name, grey_name)


def grey_of(painted_name):
    """The grey twin of a painted screen, or the same name when it is shared."""
    return GREY.get(painted_name, painted_name)


# --------------------------------------------------------- the two exceptions --
# A PAINTED PAGE WITH NO GREY TWIN IS NOT ONE FACT, IT IS TWO, and they must not
# share a bucket. Both look identical to gate 18 (a name in one tree and not in
# the other) and they mean opposite things, so a single list would in six months
# read as "the folder of files that are exempt", and the next screen built from
# the system would land in it in silence. That is the exact failure this map was
# created to end, one level up.
#
# Each entry carries its own reason, and the gate reports the two separately.

# NOT A SCREEN OF THE PRODUCT. There is nothing for it to be a twin OF. This is
# an artifact about the tree rather than a page inside it.
NOT_A_SCREEN = {
    "overview.html":
        "the index OF the painted screens, built by ui-visual/_gen_overview.py. "
        "It has no grey twin because it is not a screen: it is the map of them",
}

# A SCREEN OF THE PRODUCT, ASSEMBLED FROM THE SYSTEM. The opposite reason: it IS
# a product page, and the grey original is missing precisely BECAUSE the system
# built it. The grey tree exists to decide structure and copy before the paint
# has a system to lean on. Once the system carries the blocks, the type and the
# usage rules, a grey pass would be a transcription of decisions already made in
# ia/docs/blocks.md, voice/docs/microcopy.md and components/. Skipping it is the
# result of the stage, not a shortcut around it.
#
# THE COST IS REAL AND IS WRITTEN HERE RATHER THAN DISCOVERED LATER: gate 18
# compares five regions between the trees, and for these pages it compares
# nothing. What replaces it is that the page is assembled from banked blocks and
# shipped components, so the thing gate 18 protects against, a paint that invents
# a block, cannot happen without a new class, and a new class fails gate 6.
SYSTEM_BUILT = {
    "terms.html":
        "Terms of Service, built 2026-08-03 by the Design System stage, step 7. "
        "Blocks from ia/docs/blocks.md type 1 (DOCUMENT profile), SEO from "
        "ia/docs/pages/seo.md section 6, every class from components/. First "
        "page of the product with no grey original",
}


def no_twin_reason(painted_name):
    """Why this painted page has no grey twin, or None if it should have one."""
    for label, table in (("not a screen", NOT_A_SCREEN),
                         ("built from the system", SYSTEM_BUILT)):
        if painted_name in table:
            return label, table[painted_name]
    return None


def map_href_grey(html):
    """Painted hrefs rewritten for the grey tree.

       A port copies markup and a href IS markup, so a port that does not carry
       the map moves the links too: step 7d left 110 grey links pointing at files
       that do not exist in the grey tree, and the link check run at the time
       counted links instead of resolving targets."""
    import re
    return re.sub(r'href="([^"#?]+\.html)((?:[#?][^"]*)?)"',
                  lambda m: 'href="%s%s"' % (grey_of(m.group(1)), m.group(2)),
                  html)


if __name__ == "__main__":
    print("%d category pairs" % len(PAINTED))
    for g in sorted(PAINTED):
        print("  %-34s %s" % (g, PAINTED[g]))
