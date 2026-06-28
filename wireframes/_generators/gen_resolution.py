import _shell as S


def switcher(files, labels, state):
    cells = []
    for key, lbl in labels:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{files[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


def overlay(dim_label, zone, title, body, close_to):
    return f"""    <div class="backdrop">
      <span class="zone-tag" style="position:absolute;left:8px;bottom:8px;">{zone}</span>
      <span class="dim-note">underlying screen dimmed: {dim_label}</span>
      <section class="sheet" aria-label="{title}">
        <div class="grab"></div>
        <div class="sheet-head">
          <h2>{title}</h2>
          <a href="{close_to}"><button type="button" class="sheet-close" aria-label="Close">x</button></a>
        </div>
        <div class="sheet-body">
{body}
        </div>
      </section>
    </div>
"""


def page(cur_file, screen, authstate, switch, device, side):
    title = f"Wireframe - {screen} ({authstate})"
    html = S.assemble(title, cur_file, screen, authstate, switch, device, side)
    return S.write(cur_file, html)


# Shared event line used across resolution states (the bet that resolved).
EVENT_Q = ('          <p class="fine" style="font-weight:bold;font-size:13px;color:#222;margin:0;">'
           'Will the US government shut down before March 1, 2027?</p>')

# =========================================================================
# WIN SCREEN  (SJ1 win-share + EJ1 edge; F5 measured tone)
# =========================================================================
WIN_FILES = {"success": "win.html", "loading": "win-loading.html",
             "error": "win-error.html", "payout-pending": "win-payout-pending.html"}
WIN_LABELS = [("success", "Success"), ("loading", "Loading (card)"),
              ("error", "Card failed (T11)"), ("payout-pending", "Payout pending")]

WIN_AMOUNT = """          <div class="reconcile-box" style="align-items:center;text-align:center;">
            <span class="field-label">You were right - you won</span>
            <strong style="font-size:24px;">+$13.20</strong>
            <span class="fine">$5.00 stake returned + $8.20 winnings. You held YES, avg price 38%.</span>
          </div>"""

WIN_WHAT = """          <div>
            <span class="field-label">What happened</span>
            <p class="protect">The federal government entered a shutdown on Feb 18, 2027 after Congress missed the funding deadline. The market resolved YES, the side you held.</p>
          </div>"""

WIN_SHARECARD = """          <div>
            <span class="field-label">Share Card (auto-generated)</span>
            <div class="widget-box">Share Card: "Called it - US shutdown, YES from 38%. +$13.20 on Predict Market." (image placeholder)</div>
          </div>"""

WIN_F5_NOTE = ('          <p class="fine" style="text-align:center;">One moment, then move on - no confetti loop. '
               'Share is the primary action; "see next events" is deliberately secondary (research F5: the first win, '
               'not loss, drives overconfidence and escalation).</p>')


def win_success():
    body = (EVENT_Q + "\n" + WIN_AMOUNT + "\n" + WIN_WHAT + "\n" + WIN_SHARECARD + "\n"
            '          <button type="button" class="confirm-btn">Share</button>\n'
            '          <a href="event-feed.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">See next events</button></a>\n'
            + WIN_F5_NOTE)
    return overlay("Active Bets (resolved item) or a tapped win notification",
                   "zone: Win Screen - success (amount won, resolution summary, Share Card; CTA Share / See next events)",
                   "You were right", body, "active-bets.html")


def win_loading():
    body = (EVENT_Q + "\n" + WIN_AMOUNT + "\n"
            '          <div class="spinner-box">Generating your Share Card...<br><span class="fine">Your win and payout are confirmed. The shareable card is being created.</span></div>')
    return overlay("Active Bets (resolved item) or a tapped win notification",
                   "zone: Win Screen - loading (Share Card generation in progress)",
                   "You were right", body, "active-bets.html")


def win_error():
    body = (EVENT_Q + "\n" + WIN_AMOUNT + "\n"
            '          <div class="inline-error">We couldn\'t generate your Share Card (T11). Your win and payout are not affected. You can share as text instead.</div>\n'
            '          <button type="button" class="confirm-btn">Share as text</button>\n'
            '          <a href="event-feed.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">See next events</button></a>\n'
            '          <p class="fine" style="text-align:center;">Per IA/flows.md SJ1: a missing card (T11) falls back to a text share (T13a), not a dead end - the win is still shown.</p>')
    return overlay("Active Bets (resolved item) or a tapped win notification",
                   "zone: Win Screen - error (Share Card not generated, SJ1 blocked - T11; text-share fallback)",
                   "You were right", body, "active-bets.html")


def win_payout_pending():
    body = (EVENT_Q + "\n"
            '          <div class="reconcile-box" style="align-items:center;text-align:center;">\n'
            '            <span class="field-label">You were right - you won</span>\n'
            '            <strong style="font-size:24px;">+$13.20</strong>\n'
            '            <span class="fine">You held YES, avg price 38%. Payout is settling on-chain.</span>\n'
            '          </div>\n'
            '          <div class="spinner-box">Your payout is on the way<br><span class="fine">It will arrive in your balance in a few minutes (on-chain settlement delay). You can still share now.</span></div>\n'
            + WIN_SHARECARD + "\n"
            '          <button type="button" class="confirm-btn">Share</button>\n'
            '          <a href="event-feed.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">See next events</button></a>')
    return overlay("Active Bets (resolved item) or a tapped win notification",
                   "zone: Win Screen - payout-pending (payout settling on-chain; sharing not blocked)",
                   "You were right", body, "active-bets.html")


WIN_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>"You were right" + amount won + why</strong> -&gt; EJ1: the sense of edge (own forecast beat the market) is named here, with the plain resolution summary.</li>
        <li><strong>Share Card auto-generated, Share is the primary CTA</strong> -&gt; SJ1: show the win to my circle with one tap; the card is the shareable artifact (IA/sitemap.md Share Card entity).</li>
        <li><strong>"See next events" deliberately secondary</strong> -&gt; research F5: the first WIN triggers overconfidence and escalation, not loss. Celebratory but measured - no confetti loop, no "bet again" push.</li>
        <li><strong>error = Share Card not generated (T11)</strong> -&gt; IA/flows.md SJ1 fallback: text-share (T13a), never a dead end; win still shown.</li>
        <li><strong>payout-pending</strong> -&gt; on-chain settlement delay; the win and sharing are not gated on settlement (SJ1 share-impulse window preserved).</li>
        <li><strong>Invoked overlay over a dimmed screen</strong> -&gt; reached 1 tap from a win notification (G1-equivalent), or from a resolved item in My Bets. No auth axis (account-bound).</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (resolution flow, SJ1)</span>
<pre>Resolution flow (SJ1 - win share):

win notification --- 1 tap (G1-equiv) ---+
                                         v
My Bets (History) -- tap won item --&gt; [Win Screen]   &lt;- current
                                         v
                          Share Card --&gt; external share (X / WhatsApp / Telegram)
                                         '--&gt; See next events (secondary, F5)</pre>
        <p class="ref">Flow position: IA/flows.md SJ1 (triggerNotif -&gt; Win Screen -&gt; cardOk -&gt;
          shares). Serves SJ1 (primary) and EJ1 (the edge). Not on the MJ spine.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (amount won, summary, Share Card), loading (card generating),
          error (card not generated, T11 - text-share fallback), payout-pending (on-chain
          settlement delay). Invoked overlay, account-bound, no auth axis.</p>
      </section>
    </div>
"""

WIN_AUTHSTATE = {"success": "state: success (amount won + Share Card)", "loading": "state: loading (Share Card)",
                 "error": "state: error (card not generated, T11)", "payout-pending": "state: payout-pending"}


def build_win():
    fns = {"success": win_success, "loading": win_loading, "error": win_error, "payout-pending": win_payout_pending}
    out = []
    for st in ("success", "loading", "error", "payout-pending"):
        out.append(page(WIN_FILES[st], "Win Screen", WIN_AUTHSTATE[st],
                        switcher(WIN_FILES, WIN_LABELS, st), fns[st](), WIN_SIDE))
    return out


# =========================================================================
# LOSS SCREEN  (FJ5 + EJ3 conscious-loss exit; primary retention intervention)
# =========================================================================
LOSS_FILES = {"success": "loss.html", "loading": "loss-loading.html"}
LOSS_LABELS = [("success", "Success"), ("loading", "Loading")]

LOSS_AMOUNT = """          <div class="reconcile-box" style="align-items:center;text-align:center;">
            <span class="field-label">Result</span>
            <strong style="font-size:20px;">-$5.00</strong>
            <span class="fine">Your $5.00 stake on YES did not return. Avg price 38%.</span>
          </div>"""

LOSS_WHAT = """          <div>
            <span class="field-label">What happened</span>
            <p class="protect">Congress passed a stopgap funding bill on Feb 27, 2027, two days before the deadline, so no shutdown occurred. The market resolved NO. You held YES.</p>
          </div>"""


def loss_success():
    body = (EVENT_Q + "\n" + LOSS_WHAT + "\n" + LOSS_AMOUNT + "\n"
            '          <a href="active-bets.html"><button type="button" class="confirm-btn">Back to your bets</button></a>\n'
            '          <a href="event-feed.html"><button type="button" class="provider-btn" style="justify-content:center;width:100%;">Browse events</button></a>\n'
            '          <p class="fine" style="text-align:center;">One clear next step, and no "bet again" prompt. The resolution note is shown first so the outcome is understood before any new bet (FJ5 + EJ3: a conscious exit, no impulse to chase).</p>')
    return overlay("Active Bets (resolved item) or a tapped resolution notification (G1: 1 tap)",
                   "zone: Loss Screen - success (plain resolution note first, amount lost, one calm next step; FJ5 + EJ3)",
                   "Here's what happened", body, "active-bets.html")


def loss_loading():
    body = (EVENT_Q + "\n"
            '          <div class="spinner-box">Loading the resolution...<br><span class="fine">Fetching what resolved and why.</span></div>')
    return overlay("Active Bets (resolved item) or a tapped resolution notification (G1: 1 tap)",
                   "zone: Loss Screen - loading (fetching the resolution note)",
                   "Here's what happened", body, "active-bets.html")


LOSS_SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Plain-language resolution note shown first</strong> -&gt; FJ5 + EJ3: understand what resolved and why before any next action. The note leads, the figures follow.</li>
        <li><strong>Amount lost stated plainly, no euphemism</strong> -&gt; trust / transparency: the outcome is owned, not softened.</li>
        <li><strong>One calm next step, no "bet again" promo</strong> -&gt; this screen is our primary retention intervention against loss-chasing (a gap every competitor leaves undesigned). Default exits are "back to your bets" / "browse events", not a re-bet push.</li>
        <li><strong>No refund / payout state at MVP</strong> -&gt; cancelled-event refunds are deferred post-MVP (IA/sitemap.md), so this screen has only success and loading.</li>
        <li><strong>G1 fast path</strong> -&gt; reached 1 tap from a resolution notification, so the note reaches the user before the impulse to chase (IA/flows.md FJ5 triggerNotif -&gt; Loss Screen). No auth axis (account-bound).</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (resolution flow, FJ5 + EJ3)</span>
<pre>Resolution flow (FJ5 + EJ3 - conscious-loss exit):

resolution notification --- G1: 1 tap ---+
                                         v
My Bets -- resolved item ------------&gt; [Loss Screen]   &lt;- current
                                         v
                          read resolution note (default first)
                                         v
                   browse events / close  (no chase)
                   escalation path -.-&gt; bet panel (friction beat, F5)</pre>
        <p class="ref">Flow position: IA/flows.md FJ5 + EJ3 (triggerNotif / Active Bets -&gt;
          Loss Screen -&gt; readsNote -&gt; nextAction). Not on the MJ spine.</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (resolution note, amount lost, one next step), loading
          (fetching the resolution). No error/payout state at MVP (refunds deferred).
          Invoked overlay, account-bound, no auth axis.</p>
      </section>
    </div>
"""

LOSS_AUTHSTATE = {"success": "state: success (resolution note + amount lost)", "loading": "state: loading"}


def build_loss():
    fns = {"success": loss_success, "loading": loss_loading}
    out = []
    for st in ("success", "loading"):
        out.append(page(LOSS_FILES[st], "Loss Screen", LOSS_AUTHSTATE[st],
                        switcher(LOSS_FILES, LOSS_LABELS, st), fns[st](), LOSS_SIDE))
    return out


allf = build_win() + build_loss()
print("\n".join(allf))
