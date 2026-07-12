"""Idempotent Category reconcile (WF reconcile, Krok 7). Run after the generators.

Two things on the category pages (voice-safe in-place, no regeneration):
  1. a one-line "why" under each category card question (story-led, matching the feed),
  2. the seo.md section-3 "About {category} events" text block on the success pages.

Applies to politics / crypto / culture / general and their logged-out success variants (pages
that actually render a card grid); empty / error / loading states are skipped. Shared event
questions reuse the same why as the feed (feed_reconcile.py) for consistency. Idempotent.
"""
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

CATS = {
    "politics": ("Politics", "elections, policy votes, appointments, and other public decisions"),
    "crypto": ("Crypto", "token prices, launches, network upgrades, and protocol milestones"),
    "culture": ("Culture", "awards, releases, sports and entertainment milestones, and cultural firsts"),
    "general": ("General", "real-world questions that do not fit the other categories"),
}

# question (as in the card <a class="q">) -> one-line why. Shared events reuse the feed why.
WHY = {
    # politics
    "Will the US government shut down before March 1, 2027?": "Funding talks have stalled twice this quarter, but past deadlines settled late.",
    "Will Democrats win control of the House in the 2026 midterms?": "Generic-ballot polls have narrowed to within a point since summer.",
    "Who will win the 2028 Republican presidential nomination?": "No single contender has pulled clear in early primary polling.",
    "Will Trump's average approval exceed 45% in Q1 2027?": "Approval has sat in the low 40s for most of the past year.",
    "Will a new Supreme Court justice be confirmed before July 1, 2027?": "No vacancy has opened yet, so this needs a retirement first.",
    "Will the full Epstein files be released before January 1, 2027?": "Court motions are pending, with no release date set.",
    # crypto
    "Will Bitcoin close above $150,000 before October 1, 2026?": "Price has held above $120k for three weeks as inflows climb.",
    "Will Ethereum complete its next major network upgrade before November 1, 2026?": "The upgrade is on the testnet with a target window announced.",
    "Which coin will have the highest market cap on January 1, 2027?": "Bitcoin leads by a wide margin, with Ethereum second.",
    "Will a spot Solana ETF be approved before July 1, 2027?": "Filings are in review, with no decision date confirmed.",
    "Will USDC remain fully backed 1:1 through 2026?": "Reserves have been attested monthly with no shortfall reported.",
    "Will any memecoin enter the top 10 by market cap before 2027?": "One memecoin has traded just outside the top 10 this quarter.",
    # culture
    "Will the next lead actor for the Bond film be announced before December 31, 2026?": "The studio says casting is underway, with no shortlist confirmed.",
    "Who will win Album of the Year at the 2027 Grammys?": "Several nominees are close after a crowded release year.",
    "Will a single film cross $2B at the global box office in 2026?": "No 2026 release has passed $1.5B so far.",
    "Will the most-streamed show of 2026 be a returning series?": "Returning series have led the charts for three years running.",
    "Who will win the 2027 Eurovision final?": "Three acts are polling close after the national finals.",
    "Will a reunion tour by a 1990s band be announced before 2027?": "Two bands have hinted at dates without confirming.",
    # general
    "Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?": "The year is tracking near record heat through the first quarter.",
    "Will a crewed mission launch toward the Moon before January 1, 2028?": "The program has slipped once, with a new window under review.",
    "Which company will reach a $5T market cap first?": "Two firms are within reach after this year's rally.",
    "Will a major AI model pass a recognized medical-licensing exam in 2026?": "Recent models have scored near the passing mark in trials.",
    "Will the EU formally admit a new member state before January 1, 2028?": "Accession talks are open but no candidate has cleared the final chapters.",
    "Will a new global pandemic be declared by the WHO in 2026?": "The WHO is tracking several outbreaks but has raised no global alarm.",
}

WHY_CSS = """
    /* ---- Per-card why + category About block (WF reconcile, Krok 7) ---- */
    .why { font-size: 12px; color: #555; margin: 3px 0 0; line-height: 1.4; }
    .feed-seo { border-top: 1px solid #ccc; padding: 12px 4px; }
    .feed-seo h2 { font-size: 14px; margin: 0 0 6px; }
    .feed-seo p { font-size: 13px; color: #333; margin: 0; line-height: 1.5; }
"""

ANCHOR = "\n    </main>"


def add_css(html):
    if '.feed-seo {' in html:
        return html, False
    new = html.replace("\n  </style>", WHY_CSS + "  </style>", 1)
    if new == html:
        new = html.replace("</style>", WHY_CSS + "</style>", 1)
    return new, new != html


def add_why(html):
    changed = False
    for q, why in WHY.items():
        idx = html.find(">" + q + "</a>")
        if idx == -1:
            continue
        div_close = html.find("</div>", idx)
        if div_close == -1:
            continue
        at = div_close + len("</div>")
        if why in html[at:at + len(why) + 60]:
            continue
        html = html[:at] + '\n              <p class="why">' + why + '</p>' + html[at:]
        changed = True
    return html, changed


def about_block(cat):
    label, fill = CATS[cat]
    return (
        '      <!-- About {c} events (SEO text, WF reconcile) -->\n'
        '      <section class="feed-seo" aria-label="About {label} events">\n'
        '        <h2>About {label} events</h2>\n'
        '        <p>Follow {c} events and back your opinion with a real stake. These events cover '
        '{fill}. You see the odds in plain language and how each event resolves before you bet, '
        'from one dollar, with no wallet to start.</p>\n'
        '      </section>\n'
    ).format(c=cat, label=label, fill=fill)


def add_about(html, cat):
    if 'feed-seo' in html.split('</style>')[-1]:      # already in body
        return html, False
    if '<article class="card">' not in html:          # not a success page
        return html, False
    if ANCHOR not in html:
        return html, False
    return html.replace(ANCHOR, "\n" + about_block(cat) + "    </main>", 1), True


def main():
    stats = {"why": 0, "about": 0}
    for cat in CATS:
        for p in sorted(ROOT.glob(cat + "*.html")):
            html = p.read_text()
            orig = html
            html, cw = add_why(html)
            html, ca = add_about(html, cat)
            if cw or ca:                       # only inject CSS where content was added
                html, _ = add_css(html)
            if html != orig:
                if "—" in html or "–" in html:
                    raise SystemExit("EM/EN-DASH introduced in " + p.name)
                p.write_text(html)
            stats["why"] += int(cw)
            stats["about"] += int(ca)
    print("category why-cards: {} pages, About block: {} pages".format(stats["why"], stats["about"]))


if __name__ == "__main__":
    main()
