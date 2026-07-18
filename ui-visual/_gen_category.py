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
HEADING_RE   = re.compile(r'(<h2 id="feedHeading">)[^<]*(</h2>)')
TITLE_RE     = re.compile(r'(<title>).*?(</title>)')

# --------------------------------------------------------------------------- cards
def binary(q, why, p, vol, close, bm=False):
    pressed = "true" if bm else "false"
    lab = "Saved" if bm else "Save"
    return f'''          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb">thumbnail placeholder</span>
                <div class="top-txt"><a class="q" href="#">{q}</a><p class="why">{why}</p></div>
              </div>
              <p class="prob-line">YES <span class="prob">{p}%</span></p>
              <div class="yesno"><a href="#"><button type="button">YES</button></a><a href="#"><button type="button">NO</button></a></div>
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
        f'<a href="#"><button type="button">YES</button></a>'
        f'<a href="#"><button type="button">NO</button></a></span></div>'
        for name, pr in opts
    )
    return f'''          <article class="card">
            <div class="card-body">
              <div class="top">
                <span class="thumb">thumbnail placeholder</span>
                <div class="top-txt"><a class="q" href="#">{q}</a><p class="why">{why}</p></div>
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


def make_page(key, label, filename):
    html = SRC.read_text(encoding="utf-8")
    # wire both navs, active on this category
    html = CATNAV_RE.sub(lambda m: build_catnav(key), html, count=1)
    html = CONDENSED_RE.sub(lambda m: build_condensed(key), html, count=1)
    # drop the trending hero and the content sub-filter
    html = HERO_RE.sub("", html, count=1)
    html = SUBFILTER_RE.sub("", html, count=1)
    # heading + title
    html = HEADING_RE.sub(lambda m: m.group(1) + label + m.group(2), html, count=1)
    html = TITLE_RE.sub(lambda m: m.group(1) + f"UI Visual - {label} Events (Vault 3D)" + m.group(2), html, count=1)
    # swap in the category's own events
    cards = "\n\n".join(GRIDS[key])
    html = GRID_RE.sub(lambda m: m.group(1) + "\n\n" + cards + m.group(2), html, count=1)
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
