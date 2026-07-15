"""Idempotent feed reconcile (WF reconcile, Krok 5). Run after the generators.

Closes the CJM story-led gap on the feed (the audit found the feed cards carry plain odds but
no one-line why, and the below-the-fold SEO sections from seo.md are missing). Voice-safe: edits
in place, never regenerates (which would revert the hand-applied voice copy).

  1. a one-line "why" under each event card's question (story-led entry, spectator language),
  2. the below-the-fold SEO sections from seo.md section 1 (How betting works here / Why the odds
     move / Common questions), on the two indexed feed success pages.

The three populated feed pages share the same 8 sample cards, so one map covers them. The why
lines and SEO body are sample/editorial content in the product voice (specific, no superlative,
no motivational tone). Idempotent: each insert is skipped when already present.
"""
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

WHY_PAGES = ["event-feed.html", "event-feed-logged-out.html",
             "event-feed-push-permission-missing.html"]
SEO_PAGES = ["event-feed.html", "event-feed-logged-out.html"]

# question (as it appears in the card <a class="q">) -> one-line why (spectator language)
WHY = [
    ("Will the US government shut down before March 1, 2027?",
     "Funding talks have stalled twice this quarter, but past deadlines settled late."),
    ("Will Bitcoin close above $150,000 before October 1, 2026?",
     "Price has held above $120k for three weeks as inflows climb."),
    ("Who will win the 2027 Eurovision final?",
     "Three acts are polling close after the national finals."),
    ("Will Ethereum complete its next major network upgrade before November 1, 2026?",
     "The upgrade is on the testnet with a target window announced."),
    ("Will the next lead actor for the Bond film be announced before December 31, 2026?",
     "The studio says casting is underway, with no shortlist confirmed."),
    ("Which party will win the most seats in the next UK general election?",
     "Two parties are within the margin of error in recent polls."),
    ("Will the EU formally admit a new member state before January 1, 2028?",
     "Accession talks are open but no candidate has cleared the final chapters."),
    ("Will 2026 be confirmed as one of the three warmest years on record before April 1, 2027?",
     "The year is tracking near record heat through the first quarter."),
]

WHY_CSS = """
    /* ---- Per-card why + feed SEO sections (WF reconcile, Krok 5) ---- */
    .why { font-size: 12px; color: #555; margin: 3px 0 0; line-height: 1.4; }
    .feed-seo { border-top: 1px solid #ccc; padding: 12px 4px; }
    .feed-seo h2 { font-size: 14px; margin: 0 0 6px; }
    .feed-seo p { font-size: 13px; color: #333; margin: 0; line-height: 1.5; }
    .feed-seo dl { margin: 0; }
    .feed-seo dt { font-size: 13px; font-weight: bold; margin: 8px 0 2px; }
    .feed-seo dd { font-size: 13px; color: #333; margin: 0 0 6px; line-height: 1.5; }
"""

SEO_SECTIONS = """        <!-- SEO content sections (below the fold, WF reconcile) -->
        <section class="feed-seo" aria-label="How betting works here">
          <h2>How betting works here</h2>
          <p>Predict Market turns the events you follow into a real stake. Pick an event, read the odds in plain language, and back YES or NO. You see the current odds, a one-line why, and how the event resolves before you put in a cent. The minimum bet is one dollar, and you can browse and build your bet before you connect a wallet.</p>
        </section>
        <section class="feed-seo" aria-label="Why the odds move">
          <h2>Why the odds move</h2>
          <p>The odds are a live price set by what people bet, not a fixed quote. When more money backs YES, YES costs more and NO costs less. Your payout depends on the odds at the moment you bet, not only on the outcome, so reading an event early and being right is worth more.</p>
        </section>
        <section class="feed-seo" aria-label="Common questions">
          <h2>Common questions</h2>
          <dl>
            <dt>Do I need crypto to start?</dt>
            <dd>No. You can browse events and build a bet with no wallet. You add funds by card or crypto only when you confirm.</dd>
            <dt>What is the smallest bet?</dt>
            <dd>One dollar. The default is five.</dd>
            <dt>How does an event resolve?</dt>
            <dd>Each event states its resolution rule up front. The team resolves it against the real-world outcome, and you can see the record of resolved events.</dd>
          </dl>
        </section>
"""

SEO_ANCHOR = "\n      </div>\n    </main>"


def add_css(html):
    if '.feed-seo {' in html:
        return html, False
    new = html.replace("\n  </style>", WHY_CSS + "  </style>", 1)
    if new == html:
        new = html.replace("</style>", WHY_CSS + "</style>", 1)
    return new, new != html


def add_why(html):
    changed = False
    for q, why in WHY:
        idx = html.find(">" + q + "</a>")
        if idx == -1:
            continue
        div_close = html.find("</div>", idx)
        if div_close == -1:
            continue
        at = div_close + len("</div>")
        if why in html[at:at + len(why) + 60]:   # already inserted
            continue
        html = html[:at] + '\n              <p class="why">' + why + '</p>' + html[at:]
        changed = True
    return html, changed


def add_seo(html):
    if 'feed-seo' in html.split('</style>')[-1]:   # already in body
        return html, False
    if SEO_ANCHOR not in html:
        return html, False
    return html.replace(SEO_ANCHOR, "\n\n" + SEO_SECTIONS + "      </div>\n    </main>", 1), True


def main():
    stats = {"css": 0, "why": 0, "seo": 0}
    for name in WHY_PAGES:
        p = ROOT / name
        if not p.exists():
            continue
        html = p.read_text()
        orig = html
        html, c1 = add_css(html)
        html, c2 = add_why(html)
        c3 = False
        if name in SEO_PAGES:
            html, c3 = add_seo(html)
        if html != orig:
            if "—" in html or "–" in html:
                raise SystemExit("EM/EN-DASH introduced in " + name)
            p.write_text(html)
        stats["css"] += int(c1)
        stats["why"] += int(c2)
        stats["seo"] += int(c3)
    print("css injected: {} pages, why-cards added: {} pages, SEO sections: {} pages".format(
        stats["css"], stats["why"], stats["seo"]))


if __name__ == "__main__":
    main()
