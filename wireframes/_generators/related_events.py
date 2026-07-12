"""Idempotent Event Detail "Related events" block (WF reconcile, Krok 6).

seo.md section 2 specs a crawlable Related-events internal-linking block below the tabs on the
Event Detail pages. The audit found it absent. Voice-safe in-place stamp (no regeneration).

Applies only to full-content Event Detail pages (those that carry the content tab strip
'edtab-comments'); the loading / error states are skipped. Idempotent: skips a page that
already has the block. The related links point to existing wireframes (sibling event details +
Browse more events); the event questions are sample content.
"""
import pathlib

ROOT = pathlib.Path("/Users/sergiyshevchenko/Claud Projects/Project One/wireframes")

REL_CSS = """
    /* ---- Event Detail Related events block (WF reconcile, Krok 6) ---- */
    .related-events { border-top: 1px solid #ccc; margin: 14px 0 0; padding: 12px 0 4px; }
    .related-events h2 { font-size: 14px; margin: 0 0 8px; }
    .related-list { list-style: none; padding: 0; margin: 0; }
    .related-list li { border-bottom: 1px solid #e2e2e2; }
    .related-list a { display: flex; justify-content: space-between; gap: 12px; padding: 8px 0; color: #333; font-size: 13px; }
    .rel-odds { color: #555; white-space: nowrap; }
"""

REL_BLOCK = """      <!-- Related events (crawlable internal-linking block, WF reconcile) -->
      <section class="related-events" aria-label="Related events">
        <h2>Related events</h2>
        <ul class="related-list">
          <li><a href="event-detail.html">Will Bitcoin close above $150,000 before October 1, 2026?<span class="rel-odds">YES 61%</span></a></li>
          <li><a href="event-detail.html">Will Ethereum complete its next major network upgrade before November 1, 2026?<span class="rel-odds">YES 72%</span></a></li>
          <li><a href="event-detail-multi.html">Which party will win the most seats in the next UK general election?<span class="rel-odds">4 options</span></a></li>
          <li><a href="event-feed.html">Browse more events</a></li>
        </ul>
      </section>
"""

ANCHOR = "\n    </main>"


def process(html):
    if 'edtab-comments' not in html:          # not a full-content Event Detail page
        return html, False
    if 'related-events' in html:              # already stamped
        return html, False
    if ANCHOR not in html:
        return html, False
    # CSS
    new = html.replace("\n  </style>", REL_CSS + "  </style>", 1)
    if new == html:
        new = html.replace("</style>", REL_CSS + "</style>", 1)
    html = new
    # block before </main>
    html = html.replace(ANCHOR, "\n" + REL_BLOCK + "    </main>", 1)
    return html, True


def main():
    changed = []
    for p in sorted(ROOT.glob("event-detail*.html")):
        html = p.read_text()
        new, c = process(html)
        if c:
            if "—" in new or "–" in new:
                raise SystemExit("EM/EN-DASH introduced in " + p.name)
            p.write_text(new)
            changed.append(p.name)
    print("Related events added to {} pages:".format(len(changed)))
    for n in changed:
        print("  ", n)


if __name__ == "__main__":
    main()
