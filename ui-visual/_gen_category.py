#!/usr/bin/env python3
"""Generate the per-category feed pages from the canonical event-feed.html.

The top category nav (Trending / Politics / Crypto / Culture / General) is the
primary category switcher: each tab is its OWN page. "Trending" = event-feed.html
(keeps the featured hero band + the content sub-filter). The other four are
category pages that DROP the trending hero and the sub-filter chips (the sub-filter
only filters the Trending feed), keep only their own events, and light up their
tab in both navs.

This script is idempotent and voice-safe:
- it only rewrites the two category navs in event-feed.html (wires the hrefs), never
  its hero / sub-filter / grid;
- each category page is derived fresh from event-feed.html every run.

Run from the ui-visual/ directory:  python3 _gen_category.py
"""
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "event-feed.html"

# key, Label, filename, cat-nav icon id
CATS = [
    ("trending", "Trending", "event-feed.html",          "i-cat-fire"),
    ("politics", "Politics", "event-feed-politics.html", "i-cat-politics"),
    ("crypto",   "Crypto",   "event-feed-crypto.html",   "i-cat-crypto"),
    ("culture",  "Culture",  "event-feed-culture.html",  "i-cat-culture"),
    ("general",  "General",  "event-feed-general.html",  "i-cat-general"),
]

# --------------------------------------------------------------------------- navs
def build_catnav(active):
    lis = []
    for key, label, href, icon in CATS:
        cur = ' aria-current="page"' if key == active else ''
        lis.append(
            f'            <li{cur}><a href="{href}"><button type="button">'
            f'<svg class="cat-ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#{icon}"/></svg>'
            f'<span>{label}</span></button></a></li>'
        )
    return ('<nav class="cat-nav" aria-label="Categories (second level)">\n'
            '          <ul>\n' + "\n".join(lis) + '\n          </ul>\n        </nav>')

def build_condensed(active):
    lis = []
    for key, label, href, _icon in CATS:
        cur = ' aria-current="page"' if key == active else ''
        lis.append(f'          <li{cur}><a href="{href}"><button type="button">{label}</button></a></li>')
    return ('<div class="cat-condensed" aria-hidden="true">\n'
            '        <ul>\n' + "\n".join(lis) + '\n        </ul>\n      </div>')

CATNAV_RE    = re.compile(r'<nav class="cat-nav".*?</nav>', re.S)
CONDENSED_RE = re.compile(r'<div class="cat-condensed"[^>]*>.*?</div>', re.S)
HERO_RE      = re.compile(r'\n\s*<!-- Featured hero band.*?</section>', re.S)
SUBFILTER_RE = re.compile(r'\n\s*<!-- #90:.*?</nav>', re.S)
GRID_RE      = re.compile(r'(<div class="grid">).*?(\n\s*</div>\s*\n\s*<!-- Load more)', re.S)
# The level is not part of the question. This read <h2 id="feedHeading"> and the
# heading has been an <h1> since step 7b gave every screen exactly one, so the
# substitution had been matching nothing: the four category pages kept the
# shell's "Trending" as their heading the moment anyone re-ran this file, and the
# sub-category rail, which picks its list by the heading's text, rendered none.
# A generator whose anchor another pass has moved fails silently and passes every
# gate, which is the same defect _apply_theme.py had two functions away.
HEADING_RE   = re.compile(r'(<h([1-6]) id="feedHeading"[^>]*>)[^<]*(</h\2>)')
TITLE_RE     = re.compile(r'(<title>).*?(</title>)')

# Where a card goes. The painted tree has one event page per market type, so a
# card links by its type: the question, and both outcome buttons with it, since
# tapping either is the same request to open the event with that side chosen.
# These were "#" until the relink pass, which is how the four category feeds
# shipped with dead cards.
DETAIL = "event-detail.html"
DETAIL_MULTI = "event-detail-multi.html"


# --------------------------------------------------------------------------- cards
def binary(q, why, p, vol, close, bm=False):
    pressed = "true" if bm else "false"
    lab = "Saved" if bm else "Save"
    return f'''          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb" data-photo>thumbnail placeholder</span>
                <div class="top-txt"><a class="q" href="{DETAIL}">{q}</a><p class="why">{why}</p></div>
              </div>
              <p class="prob-line">YES <span class="prob">{p}%</span></p>
              <div class="yesno"><a href="{DETAIL}"><button type="button">YES</button></a><a href="{DETAIL}"><button type="button">NO</button></a></div>
              <p class="meta">
                <span class="meta-txt"><span>Volume: {vol}</span><span>Closes: {close}</span></span>
                <button type="button" class="bookmark-btn" aria-pressed="{pressed}" aria-label="{lab}">
                  <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-bookmark-b"/></svg>
                </button>
              </p>
            </div>
          </article>'''

def multi(q, why, opts, vol, close):
    rows = "\n".join(
        f'                <div class="opt-row"><span class="opt-name">{name}</span>'
        f'<span class="opt-prob">{pr}%</span><span class="yesno compact">'
        f'<a href="{DETAIL_MULTI}"><button type="button">YES</button></a>'
        f'<a href="{DETAIL_MULTI}"><button type="button">NO</button></a></span></div>'
        for name, pr in opts
    )
    return f'''          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb" data-photo>thumbnail placeholder</span>
                <div class="top-txt"><a class="q" href="{DETAIL_MULTI}">{q}</a><p class="why">{why}</p></div>
              </div>
              <div class="options">
{rows}
              </div>
              <p class="meta">
                <span class="meta-txt"><span>Volume: {vol}</span><span>Closes: {close}</span></span>
                <button type="button" class="bookmark-btn" aria-pressed="false" aria-label="Save">
                  <svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-bookmark-b"/></svg>
                </button>
              </p>
            </div>
          </article>'''

# Per-category event sets (existing events kept where they fit + new ones so each
# page reads full, ~6 cards). User content only; voice-safe, no em-dash.
GRIDS = {
    "politics": [
        binary("Will the US government shut down before March 1, 2027?",
               "Funding talks have stalled twice this quarter, but past deadlines settled late.",
               38, "$84,200", "Mar 1, 2027"),
        multi("Which party will win the most seats in the next UK general election?",
              "Two parties are within the margin of error in recent polls.",
              [("Labour", 44), ("Conservatives", 33)], "$58,700", "Jul 1, 2027"),
        binary("Will the next US federal budget pass before the October deadline?",
               "Committee talks are moving but the largest line items stay open.",
               41, "$52,800", "Oct 1, 2026"),
        multi("Which party will control the US Senate after the next election?",
              "The count is within a few seats across recent polling.",
              [("Republicans", 52), ("Democrats", 48)], "$96,400", "Nov 3, 2026"),
        binary("Will the EU formally admit a new member state before January 1, 2028?",
               "Accession talks are open but no candidate has cleared the final chapters.",
               23, "$33,100", "Jan 1, 2028"),
        binary("Will a snap national election be called in France before July 1, 2027?",
               "The government holds a thin majority after two close confidence votes.",
               29, "$27,400", "Jul 1, 2027"),
    ],
    "crypto": [
        binary("Will Bitcoin close above $150,000 before October 1, 2026?",
               "Price has held above $120k for three weeks as inflows climb.",
               61, "$212,900", "Oct 1, 2026", bm=True),
        binary("Will Ethereum complete its next major network upgrade before November 1, 2026?",
               "The upgrade is on the testnet with a target window announced.",
               72, "$147,650", "Nov 1, 2026"),
        binary("Will a spot Solana ETF be approved before September 1, 2027?",
               "Two issuers have active filings under review this quarter.",
               44, "$71,300", "Sep 1, 2027"),
        binary("Will Ethereum stay above $4,000 through the end of 2026?",
               "It has traded in a tight band above $4k for a month.",
               54, "$63,200", "Dec 31, 2026"),
        binary("Will a US spot XRP ETF be approved before June 1, 2027?",
               "One filing cleared its first review step this month.",
               31, "$38,900", "Jun 1, 2027"),
        multi("Which chain will hold the largest stablecoin supply at the end of 2026?",
              "The top two chains are within a few points on current balances.",
              [("Ethereum", 58), ("Tron", 34)], "$44,100", "Dec 31, 2026"),
    ],
    "culture": [
        multi("Who will win the 2027 Eurovision final?",
              "Three acts are polling close after the national finals.",
              [("Sweden", 34), ("Italy", 27)], "$61,500", "May 15, 2027"),
        binary("Will the next lead actor for the Bond film be announced before December 31, 2026?",
               "The studio says casting is underway, with no shortlist confirmed.",
               47, "$19,400", "Dec 31, 2026"),
        binary("Will the next major game console launch before the 2026 holiday season?",
               "The maker confirmed a release window but has not set a date.",
               58, "$18,900", "Nov 1, 2026"),
        binary("Will the top-grossing 2026 film pass $2 billion worldwide?",
               "The summer slate is stacked but no title has broken out yet.",
               22, "$24,700", "Jan 15, 2027"),
        binary("Will a debut album top the 2026 year-end chart?",
               "Two first-time acts are leading the mid-year streaming counts.",
               35, "$12,300", "Jan 1, 2027"),
        multi("Which genre will lead the 2026 summer box office?",
              "The release calendar is split between two crowded genres.",
              [("Superhero", 46), ("Animation", 31)], "$21,800", "Sep 1, 2026"),
    ],
    "general": [
        binary("Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?",
               "The year is tracking near record heat through the first quarter.",
               55, "$26,300", "Apr 1, 2027"),
        binary("Will a new monthly global temperature record be set before September 1, 2026?",
               "Recent months have run close to prior highs.",
               48, "$17,600", "Sep 1, 2026"),
        binary("Will a crewed mission return from lunar orbit before January 1, 2028?",
               "The flight is on the schedule but the launch date keeps moving.",
               39, "$30,200", "Jan 1, 2028"),
        binary("Will a Category 5 hurricane form in the Atlantic during the 2026 season?",
               "Forecasters are calling for warmer than average ocean temperatures.",
               62, "$22,900", "Nov 30, 2026"),
        binary("Will global renewable capacity set a new annual record in 2026?",
               "Installations are running ahead of last year through the first half.",
               74, "$15,400", "Dec 31, 2026"),
        multi("Which energy source will add the most new capacity in 2026?",
              "The two leaders are close on projects already under construction.",
              [("Solar", 51), ("Wind", 32)], "$19,700", "Dec 31, 2026"),
    ],
}


SEO_SEC = re.compile(r'<section class="feed-seo"[^>]*>.*?</section>', re.S)
SEO_TEXT = re.compile(r'(<div class="seo-text">\s*).*?(\s*</div><!-- /seo-text -->)', re.S)
GREY = HERE.parent / "wireframes"


# --------------------------------------------------------------------------- photo
# THE CARD SHOWS ITS EVENT'S PHOTOGRAPH, and the sample library has one per
# category, so on a category page every card draws the same file. That is not a
# rendering choice, it is what the library is: a page whose six events are all
# Politics has one Politics photograph to draw them with. What varies is the
# CROP. The thumbnail is a 56px strip masked to transparent at 52 per cent, so a
# different slice of a 1600px photograph reads as a different picture while
# staying a true picture of the same subject.
#
# Until step 7c this came from components/, as .grid > .card:nth-of-type(N)
# .thumb, which meant a card's photograph was decided by its POSITION in a grid.
# That step moved it onto the element, where it belongs, on the pages it walked;
# these cards are written here, so they lost the picture and kept the empty box.
# Nothing saw it for two steps, because an empty photograph is invisible to a
# contrast sweep, an overflow sweep and a link check alike.
CROPS = ["22% center", "62% center", "40% 30%", "80% center", "50% 70%", "12% center"]


def photograph(html, key):
    """Every marked thumbnail gets this category's photograph, cropped by its
       place in the grid so no two cards on a page show the same slice."""
    n = [0]

    def fill(m):
        pos = CROPS[n[0] % len(CROPS)]
        n[0] += 1
        return ('<span class="thumb" style="background-image:url(../assets/event-%s.jpg);'
                'background-position:%s">' % (key, pos))

    out = re.sub(r'<span class="thumb" data-photo>', fill, html)
    if not n[0]:
        raise SystemExit("_gen_category: no card to photograph on %s" % key)
    return out


def category_seo(html, key, label):
    """The below-fold SEO body a CATEGORY page owes, not the home page's.

       ia/docs/pages/seo.md section 3B lists five H2s for this template, and the
       fourth is "About {category} events". The four painted category pages were
       derived from the painted feed and inherited ITS body instead: the same two
       generic sections on all five URLs, and the one section that is about this
       category missing from the one page that is about this category. Section E
       of the same spec is explicit that a category must not duplicate its
       siblings.

       The copy is read out of the grey twin rather than typed here, because copy
       is owned by wireframes/ and voice/, and a generator that types a sentence
       is a second source for it."""
    grey = (GREY / ("%s.html" % key)).read_text(encoding="utf-8")
    about = SEO_SEC.search(grey)
    if not about:
        raise SystemExit("_gen_category: no feed-seo section in grey %s.html" % key)
    # TEXT, not inner html. This read the heading's markup, and the grey twin is
    # written by port_structure.py out of THIS file's own output, so the second
    # run read back the icon this file had just put in the heading and wrote it
    # into an aria-label: a label containing an <svg>, an icon the vitrine could
    # not account for (gate 17), and a pair of tools rewriting eight pages on
    # every run of the chain, for ever. A generator that reads its own output
    # through another tool has to read the part of it that does not change.
    head = re.sub(r"<[^>]+>", "", re.search(r"<h2[^>]*>(.*?)</h2>", about.group(0), re.S).group(1)).strip()
    body = re.sub(r"<[^>]+>", "", re.search(r"<p>(.*?)</p>", about.group(0), re.S).group(1)).strip()
    faq = next((s for s in SEO_SEC.findall(html) if "Common questions" in s), "")
    new = (
        '<section class="feed-seo" aria-label="%s">\n'
        '          <h2><svg class="seo-h-ic" viewBox="0 0 24 24" aria-hidden="true">'
        '<use href="#i-seo-guide"/></svg>%s</h2>\n'
        '          <p>%s</p>\n'
        '        </section>' % (head, head, body)
    )
    return SEO_TEXT.sub(
        lambda m: m.group(1) + new + ("\n        " + faq if faq else "") + m.group(2),
        html, count=1)


def make_page(key, label, filename):
    html = SRC.read_text(encoding="utf-8")
    # wire both navs, active on this category
    html = CATNAV_RE.sub(lambda m: build_catnav(key), html, count=1)
    html = CONDENSED_RE.sub(lambda m: build_condensed(key), html, count=1)
    # drop the trending hero and the content sub-filter
    html = HERO_RE.sub("", html, count=1)
    html = SUBFILTER_RE.sub("", html, count=1)
    # heading + title
    html = HEADING_RE.sub(lambda m: m.group(1) + label + m.group(3), html, count=1)
    html = TITLE_RE.sub(lambda m: m.group(1) + f"UI Visual - {label} Events (Vault 3D)" + m.group(2), html, count=1)
    # swap in the category's own events
    cards = "\n\n".join(GRIDS[key])
    html = GRID_RE.sub(lambda m: m.group(1) + "\n\n" + cards + m.group(2), html, count=1)
    # and the SEO body this category owes, in place of the home page's
    html = photograph(html, key)
    html = category_seo(html, key, label)
    (HERE / filename).write_text(html, encoding="utf-8")
    n = len(GRIDS[key])
    print(f"  {filename:34s}  {n} events")


def patch_main():
    """Wire the two navs in event-feed.html so the top tabs navigate; leave its
    hero / sub-filter / grid untouched."""
    html = SRC.read_text(encoding="utf-8")
    html = CATNAV_RE.sub(lambda m: build_catnav("trending"), html, count=1)
    html = CONDENSED_RE.sub(lambda m: build_condensed("trending"), html, count=1)
    SRC.write_text(html, encoding="utf-8")
    print(f"  {'event-feed.html':34s}  navs wired (Trending active)")


if __name__ == "__main__":
    print("Wiring the main feed nav ...")
    patch_main()
    print("Generating category pages ...")
    for key, label, filename, _icon in CATS:
        if key == "trending":
            continue
        make_page(key, label, filename)
    print("Done.")
