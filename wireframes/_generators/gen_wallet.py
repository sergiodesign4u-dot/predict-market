import _shell as S

FILES = {"success": "wallet.html", "loading": "wallet-loading.html", "error": "wallet-error.html"}
LABELS = [("success", "Success"), ("loading", "Loading"), ("error", "Error")]


def switcher(state):
    cells = []
    for key, lbl in LABELS:
        cur = ' aria-current="page"' if key == state else ""
        cells.append(f'<a href="{FILES[key]}"{cur}>{lbl}</a>')
    return ('  <nav class="state-switch" aria-label="States of this screen">\n'
            f'    <div class="ss-row"><span class="ss-label">State</span>{"".join(cells)}</div>\n'
            '  </nav>')


BALANCE = """        <article class="pos" aria-label="Balance summary">
          <div class="pos-figures" style="font-size:11px;">
            <span class="pos-fig">Portfolio total<b>$142.00</b></span>
            <span class="pos-fig">Cash (available)<b>$92.00</b></span>
            <span class="pos-fig">In-play (open bets)<b>$50.00</b></span>
          </div>
          <span class="pos-status">Portfolio = Cash + In-play. In-play is locked in open positions until they resolve.</span>
        </article>
"""

ACTIONS = """        <div class="cta-bar" style="position:static;">
          <button type="button" data-open="deposit">Deposit</button>
          <button type="button" onclick="var d=document.getElementById('wd');if(d){d.open=!d.open;d.scrollIntoView();}">Withdraw</button>
        </div>
"""

WITHDRAW = """        <details id="wd" class="wd-flow">
          <summary>Withdraw funds (USDC)</summary>
          <div class="sheet-body" style="padding:10px 0;">
            <div>
              <span class="field-label">Amount to withdraw</span>
              <div class="amount-row"><span class="amount-input">$30.00</span></div>
              <span class="fine">Available to withdraw: $92.00 (Cash only; in-play funds are locked).</span>
            </div>
            <div>
              <span class="field-label">Destination USDC address</span>
              <div class="amount-row"><span class="amount-input" style="font-size:12px;">0x1A2b...9F3c</span></div>
            </div>
            <p class="fine">Withdrawals are in USDC only at MVP (no fiat payout rail). PIX payout is Phase 2 (Brazil). Network fee applies.</p>
            <button type="button" class="confirm-btn">Confirm withdrawal</button>
            <p class="fine">After confirm, the withdrawal moves through: pending (on-chain) -&gt; confirmed, or failed (funds returned to Cash). Tracked in the history below.</p>
          </div>
        </details>
"""

PROTECT = '        <p class="protect">Your USDC is held 1:1 - we do not lend or invest your funds. Deposits, payouts and withdrawals are recorded below.</p>\n'


def tx(label, amount, meta):
    return (f'          <article class="pos">\n'
            f'            <div class="pos-top">\n'
            f'              <span class="pos-q">{label}</span>\n'
            f'              <span class="pos-status" style="white-space:nowrap;">{amount}</span>\n'
            f'            </div>\n'
            f'            <span class="pos-status">{meta}</span>\n'
            f'          </article>\n')


TX_LIST = (
    tx("Withdrawal to USDC address", "-$30.00", "Jun 28 &middot; pending (on-chain)")
    + tx("Payout: US government shutdown - YES won", "+$13.20", "Jun 27 &middot; completed")
    + tx("Platform fee (won bet)", "-$0.40", "Jun 27 &middot; completed")
    + tx("Stake: Bitcoin above $150,000 - YES", "-$25.00", "Jun 26 &middot; locked in-play")
    + tx("Deposit via card (Transak)", "+$20.00", "Jun 26 &middot; completed")
)


def main_success():
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Wallet (balance + transaction history + deposit / withdraw; funds-protection, FJ4 / EJ2)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Wallet</h2></div>\n'
            + BALANCE
            + ACTIONS
            + WITHDRAW
            + PROTECT
            + '        <p class="pos-status" style="margin:10px 0 2px;text-transform:uppercase;letter-spacing:.04em;">Transaction history</p>\n'
            + '        <div class="pos-list">\n'
            + TX_LIST
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


def main_block(zone, icon, title, msg, actions):
    return (f'    <main class="feed">\n'
            f'      <span class="zone-tag">{zone}</span>\n'
            f'      <div class="feed-inner">\n'
            f'        <div class="feed-head"><h2>Wallet</h2></div>\n'
            f'        <div class="state-block">\n'
            f'          <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>\n'
            f'          <h2 class="state-title">{title}</h2>\n'
            f'          <p class="state-msg">{msg}</p>\n'
            f'          <div class="state-actions">{actions}</div>\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </main>\n')


ICON_WARN = '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>'


def main_error():
    return main_block(
        "zone: Wallet (error: wallet data failed to load - retry)",
        ICON_WARN, "Couldn't load your wallet",
        "We couldn't fetch your balance and transactions. Your funds are safe; this is a display issue. Try again.",
        '<a href="wallet.html"><button type="button" class="state-btn primary">Try again</button></a>')


def main_loading():
    sk = ('          <article class="pos skeleton" aria-hidden="true">\n'
          '            <div class="sk-line w70"></div>\n'
          '            <div class="sk-line w40"></div>\n'
          '          </article>\n')
    return ('    <main class="feed">\n'
            '      <span class="zone-tag">zone: Wallet (loading: initial balance + history fetch)</span>\n'
            '      <div class="feed-inner">\n'
            '        <div class="feed-head"><h2>Wallet</h2></div>\n'
            '        <article class="pos skeleton" aria-hidden="true">\n'
            '          <div class="sk-line w40"></div>\n'
            '          <div class="sk-line w70"></div>\n'
            '        </article>\n'
            '        <div class="pos-list" aria-busy="true">\n'
            + sk * 3
            + '        </div>\n'
            + '      </div>\n'
            + '    </main>\n')


# Small page-local CSS for the withdraw <details> (scoped; not added to the shared shell).
WALLET_CSS = """  <style>
    .wd-flow { border: 1px solid #999; background: #ededed; margin: 8px 0; }
    .wd-flow > summary { cursor: pointer; padding: 10px; font-size: 13px; font-weight: bold; }
    .wd-flow[open] > summary { border-bottom: 1px solid #ccc; }
    .wd-flow .sheet-body { padding: 10px; }
  </style>
"""

SIDE = """    <aside class="annotations" aria-label="Annotations">
      <span class="zone-tag">annotations: zone to job / finding</span>
      <ol>
        <li><strong>Balance split: Cash (available) vs In-play (locked)</strong> -&gt; FJ4: a clear answer to "where is my money". Portfolio = Cash + In-play; in-play is locked in open positions until they resolve.</li>
        <li><strong>Funds-protection line (held 1:1)</strong> -&gt; EJ2 (secondary): the same trust message as Deposit, visible at the money hub too.</li>
        <li><strong>Transaction history (deposits, payouts, fees, stakes, withdrawals)</strong> -&gt; the audit trail: every movement is recorded, supporting the transparency principle.</li>
        <li><strong>Deposit opens the shared Deposit dialog</strong> -&gt; standalone top-up reuses the same Deposit flow (no second deposit screen); IA/sitemap.md "deposit again (same Deposit screen)".</li>
        <li><strong>Withdraw is a flow inside Wallet, not a screen</strong> -&gt; amount -&gt; USDC address -&gt; confirm, with pending / confirmed / failed states tracked in history. USDC-only at MVP (no fiat payout); PIX is Phase 2.</li>
        <li><strong>Reached from the avatar dropdown (desktop) / the Portfolio hub (mobile)</strong> -&gt; money is a utility, not a primary destination (G4). Account-bound, logged-in only - no auth axis.</li>
      </ol>
    </aside>

    <div class="nav-col">
      <section class="navtree" aria-label="Navigation tree">
        <span class="zone-tag">on-page nav tree (account hub)</span>
<pre>Account / money (off the betting spine):

avatar dropdown (desktop) -----+
Portfolio hub (mobile) --------+--&gt; [Wallet]   &lt;- current
                                      |
                                      +-- Deposit (shared dialog)
                                      '-- Withdraw (in-Wallet flow:
                                            amount -&gt; USDC addr -&gt; confirm)</pre>
        <p class="ref">Flow position: standalone money management off the betting flow
          (IA/sitemap.md Wallet). Serves FJ4 (primary) and EJ2 (secondary).</p>
      </section>

      <section class="navtree" aria-label="States">
        <span class="zone-tag">states of this screen</span>
        <p class="ref">success (balance + history + deposit / withdraw), loading (initial
          balance fetch), error (wallet data failed, retry). balance-syncing deferred.
          Withdrawal sub-states (pending / confirmed / failed) live inside the flow.
          Account-bound, no auth axis.</p>
      </section>
    </div>
"""

AUTHSTATE = {"success": "success (balance + history)", "loading": "loading (balance fetch)",
             "error": "error (data failed to load)"}


def build(state):
    cur_file = FILES[state]
    main = {"success": main_success, "error": main_error, "loading": main_loading}[state]()
    device = S.HEADER_IN_OPEN + main + S.bottom_in("portfolio") + "    " + S.FOOTER + "\n"
    authstate = "logged in - state: " + AUTHSTATE[state]
    title = f"Wireframe - Wallet ({authstate})"
    html = S.assemble(title, cur_file, "Wallet", authstate, switcher(state), device, SIDE)
    # inject the page-local withdraw CSS just before </head>
    html = html.replace("</head>", WALLET_CSS + "</head>", 1)
    return S.write(cur_file, html)


print("\n".join(build(s) for s in ("success", "loading", "error")))
