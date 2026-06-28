import _shell as S

# Page-local CSS (scoped; not in the shared shell). Simple trust-declaration sections.
HIW_CSS = """  <style>
    .hiw-sec { padding: 12px 0; border-top: 1px solid #ccc; }
    .hiw-sec:first-of-type { border-top: none; }
    .hiw-sec h3 { font-size: 13px; margin: 0 0 6px; }
    .hiw-sec p { font-size: 13px; line-height: 1.5; margin: 0 0 6px; }
    .hiw-lead { font-size: 15px; font-weight: bold; line-height: 1.45; }
  </style>
"""


def sec(title, *paras):
    body = "".join(f'          <p>{p}</p>\n' for p in paras)
    return (f'        <section class="hiw-sec">\n'
            f'          <h3>{title}</h3>\n'
            + body
            + '        </section>\n')


def main_success():
    proof = ('        <article class="pos" aria-label="Resolved markets">\n'
             '          <div class="pos-figures" style="font-size:11px;">\n'
             '            <span class="pos-fig">Markets resolved<b>1,240</b></span>\n'
             '            <span class="pos-fig">On-chain proofs<b>100%</b></span>\n'
             '            <span class="pos-fig">USDC held 1:1<b>always</b></span>\n'
             '          </div>\n'
             '          <span class="pos-status">Resolved-market count as social proof (benchmark-trust.md Top 3 trust mechanisms).</span>\n'
             '        </article>\n')
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: How It Works (trust declaration, not a FAQ; funds protection + resolution + on-chain proof; FJ4 / EJ2)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>How It Works</h2></div>\n'
            '        <p class="hiw-lead">You always know what you are doing, why, and what happens to your money. This is a promise, not a FAQ.</p>\n'
            + sec("Your money is held 1:1",
                  "Your USDC is held 1:1. We never lend it, invest it, or move it. It is yours until you place a bet or withdraw - deposits, payouts and withdrawals are all recorded in your Wallet.")
            + sec("How events resolve",
                  "Each event has clear resolution conditions, written before betting opens. When the event happens, the platform team resolves it against public evidence (official sources, on-chain data, named references).",
                  "Every resolution is recorded on-chain, so the outcome and the payout are verifiable and cannot be changed after the fact.")
            + sec("How pricing and payouts work",
                  "Prices move with the market (AMM). Your payout depends on when you bet: earlier stakes at a better price earn more. The amount and potential payout are always shown before you confirm.",
                  "There is no subscription. The platform earns a small fee only when you win - never on a losing bet.")
            + sec("Proven, not promised")
            + proof
            + '        <div class="cta-bar" style="position:static;border:none;background:none;padding:10px 0 0;">\n'
            + '          <a href="event-feed.html" style="flex:1;"><button type="button" style="width:100%;">Browse events</button></a>\n'
            + '          <button type="button" data-open="deposit" style="flex:1;">Add funds</button>\n'
            + '        </div>\n'
            + '        <p class="fine">Reachable before you deposit anything (from the menu and the footer) and from the Deposit dialog "learn more" link, so the answer to "what happens to my money" comes before the money does.</p>\n'
            + '      </div>\n'
            + '    </main>\n')


SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Funds protection, one sentence</strong> -&gt; FJ4 + EJ2: "Your USDC is held 1:1". The clear answer to "what happens to my money", stated as a promise.</li>
        <li><strong>Resolution process: who decides, what evidence, on-chain proof</strong> -&gt; the core trust differentiator: no competitor explains resolution at this depth. Conditions written up front, resolved against public evidence, recorded on-chain.</li>
        <li><strong>Pricing and payout, transparently</strong> -&gt; AMM timing (earlier = better), fee only on a win, no subscription. Teaching that used to be in onboarding now lives on a live trust page.</li>
        <li><strong>Resolved-markets count as social proof</strong> -&gt; benchmark-trust.md Top 3 mechanisms: a real number of settled markets earns more trust than copy.</li>
        <li><strong>A trust declaration, not a FAQ</strong> -&gt; written as a promise. Reachable before any deposit (menu / footer) and from the Deposit dialog, so FJ4 can close before the first deposit.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (trust anchor)</span>
<pre>Trust anchor (FJ4 + EJ2):

main menu / footer ------+
Deposit dialog ("learn   +--&gt; [How It Works]   &lt;- current
  more" link) -----------+         |
                                   '-- Browse events / Add funds</pre>
        <p class="ref">Flow position: pre-bet trust signal, reachable before depositing
          (IA/sitemap.md How It Works; IA/flows.md Deposit moreInfo -&gt; HIW -&gt; back). Serves FJ4, EJ2.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (static trust page). A static declaration - no loading / error /
          empty states. Reachable logged-in or logged-out (no auth axis built; content is identical).</p>
      </section>
    </div>
"""


def build():
    cur_file = "how-it-works.html"
    # Public / pre-deposit trust page: reachable before sign-in (footer / menu /
    # Deposit "learn more"), so it carries the logged-out header (no balance / avatar).
    device = S.HEADER_OUT_OPEN + main_success() + S.bottom_out("none") + "    " + S.FOOTER + "\n"
    authstate = "state: success (static trust page)"
    title = "Wireframe - How It Works (static trust page)"
    switcher = ('  <nav class="state-switch" aria-label="States of this screen">\n'
                '    <div class="ss-row"><span class="ss-label">State</span><a href="how-it-works.html" aria-current="page">Static trust page</a></div>\n'
                '  </nav>')
    html = S.assemble(title, cur_file, "How It Works", authstate, switcher, device, SIDE)
    html = html.replace("</head>", HIW_CSS + "</head>", 1)
    return S.write(cur_file, html)


print(build())
