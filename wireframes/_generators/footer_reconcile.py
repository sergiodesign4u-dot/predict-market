"""Idempotent footer reconcile (WF reconcile, Krok 3). Run after the generators.

The footer is byte-identical across the 82 pages that have it (1 variant). This stamps
the IA Detailed-layer footer node (ia/docs/pages/seo.md) into every footer in place, WITHOUT
regenerating (which would revert the hand-applied voice copy):
  1. a persistent trust strip above the footer (funds-safety + resolution signal),
  2. an SEO popular-links block (second internal-linking plane, crawlable <a>),
  3. real hrefs where a wireframe target exists (categories, How it works, Wallet, My Bets),
  4. a Cookie preferences re-entry in the legal strip (opens cookie-consent.html).

Idempotent: each transform is skipped when its result is already present. Only pages that
carry <footer class="app-footer"> are touched (the 17 overlay pages have no footer).
"""
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

FOOTER_CSS = """
    /* ---- Footer trust strip + SEO popular-links (WF reconcile, Krok 3) ---- */
    .footer-trust { display: flex; flex-wrap: wrap; gap: 8px 18px; justify-content: center; padding: 10px 12px; border-bottom: 1px solid #ccc; font-size: 12px; color: #444; }
    .footer-trust .trust-item { display: inline-block; }
    .footer-popular { padding: 10px 12px; border-top: 1px solid #ccc; }
    .footer-popular h3 { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: #555; margin: 0 0 6px; }
    .popular-links { display: flex; flex-wrap: wrap; gap: 6px 14px; list-style: none; padding: 0; margin: 0; font-size: 12px; }
    .popular-links a { color: #444; }
"""

TRUST_STRIP = """        <!-- Trust strip (persistent funds-safety + resolution signal, WF reconcile) -->
        <div class="footer-trust">
          <span class="trust-item">Your USDC is held 1:1, we never lend it.</span>
          <span class="trust-item">Every event resolves against a public source.</span>
          <span class="trust-item">1,284 events resolved</span>
        </div>

"""

POPULAR_BLOCK = """        <!-- SEO popular-links block (second internal-linking plane, WF reconcile) -->
        <div class="footer-popular">
          <h3>Popular right now</h3>
          <ul class="popular-links">
            <li><a href="politics.html">Politics events</a></li>
            <li><a href="crypto.html">Crypto events</a></li>
            <li><a href="culture.html">Culture events</a></li>
            <li><a href="general.html">General events</a></li>
            <li><a href="event-feed.html">Trending events</a></li>
            <li><a href="event-feed.html">Ending soon</a></li>
            <li><a href="how-it-works.html">How it works</a></li>
          </ul>
        </div>

"""

# Real hrefs where a wireframe target exists. Naturally idempotent: after the first pass the
# "#" form is gone, so a re-run finds nothing to replace.
HREF_FIXES = [
    ('<li><a href="#">Politics</a></li>', '<li><a href="politics.html">Politics</a></li>'),
    ('<li><a href="#">Crypto</a></li>', '<li><a href="crypto.html">Crypto</a></li>'),
    ('<li><a href="#">Culture</a></li>', '<li><a href="culture.html">Culture</a></li>'),
    ('<li><a href="#">General</a></li>', '<li><a href="general.html">General</a></li>'),
    ('<li><a href="#">View all events</a></li>', '<li><a href="event-feed.html">View all events</a></li>'),
    ('<li><a href="#">How It Works</a></li>', '<li><a href="how-it-works.html">How It Works</a></li>'),
    ('<li><a href="#">Wallet</a></li>', '<li><a href="wallet.html">Wallet</a></li>'),
    ('<li><a href="#">My Bets</a></li>', '<li><a href="active-bets.html">My Bets</a></li>'),
]

COOKIE_OLD = '<li><a href="#">Geo restrictions</a> <span class="tbd">TBD</span></li>'
COOKIE_NEW = (COOKIE_OLD +
              '\n              <li><a href="cookie-consent.html">Cookie preferences</a></li>')


def process(html):
    if '<footer class="app-footer"' not in html:
        return html, False
    orig = html
    # 1. CSS
    if '.footer-trust {' not in html:
        new = html.replace("\n  </style>", FOOTER_CSS + "  </style>", 1)
        if new == html:
            new = html.replace("</style>", FOOTER_CSS + "</style>", 1)
        html = new
    # 2. Trust strip (before footer-top)
    if 'footer-trust' not in html.split('</style>')[-1]:  # not yet in body
        html = html.replace('        <div class="footer-top">',
                            TRUST_STRIP + '        <div class="footer-top">', 1)
    # 3. Popular block (before the legal strip)
    if 'footer-popular' not in html.split('</style>')[-1]:
        html = html.replace('        <!-- Legal strip -->',
                            POPULAR_BLOCK + '        <!-- Legal strip -->', 1)
    # 4. Real hrefs
    for old, new in HREF_FIXES:
        html = html.replace(old, new)
    # 5. Cookie preferences re-entry
    if 'cookie-consent.html">Cookie preferences' not in html:
        html = html.replace(COOKIE_OLD, COOKIE_NEW, 1)
    return html, html != orig


def main():
    changed = []
    for p in sorted(ROOT.glob("*.html")):
        txt = p.read_text()
        new, c = process(txt)
        if c:
            if "—" in new or "–" in new:
                raise SystemExit("EM/EN-DASH introduced in " + p.name)
            p.write_text(new)
            changed.append(p.name)
    print("footer reconciled on {} pages".format(len(changed)))
    for n in changed[:6]:
        print("  ", n)


if __name__ == "__main__":
    main()
